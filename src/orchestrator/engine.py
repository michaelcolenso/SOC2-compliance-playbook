from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .agent_runner import AgentRunner
from .quality_gates import QualityGateEvaluator
from .state_manager import StateManager


@dataclass
class OrchestratorEngine:
    workflow_file: Path
    state_file: Path
    output_dir: Path

    def __post_init__(self) -> None:
        self.state = StateManager(self.state_file)
        self.runner = AgentRunner()
        self.gates = QualityGateEvaluator()

    def load_workflow(self) -> dict[str, Any]:
        return json.loads(self.workflow_file.read_text())

    def init(self) -> dict[str, Any]:
        workflow = self.load_workflow()
        return self.state.initialize(workflow)

    def status(self) -> dict[str, Any]:
        return self.state.load()

    def deploy(self, phase: int | None = None, agent_id: str | None = None, run_all: bool = False) -> dict[str, Any]:
        workflow = self.load_workflow()
        state = self.state.load()

        candidates = workflow["agents"]
        if agent_id:
            candidates = [a for a in candidates if a["agent_id"] == agent_id]
        elif phase is not None:
            candidates = [a for a in candidates if a["phase"] == phase]
        elif not run_all:
            raise ValueError("Specify --phase, --agent, or --all")

        completed = set(state["agents"]["completed"])
        for agent in candidates:
            deps = set(agent.get("dependencies", []))
            if not deps.issubset(completed):
                state["agents"]["blocked"].append(agent["agent_id"])
                continue
            if agent["agent_id"] in state["agents"]["pending"]:
                state["agents"]["pending"].remove(agent["agent_id"])
            state["agents"]["running"].append(agent["agent_id"])
            self.runner.run(agent, self.output_dir)
            state["agents"]["running"].remove(agent["agent_id"])
            state["agents"]["completed"].append(agent["agent_id"])
            completed.add(agent["agent_id"])

        state["quality_gates"] = self.gates.evaluate(workflow, self.output_dir)
        self.state.save(state)
        return state
