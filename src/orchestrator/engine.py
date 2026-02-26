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
            aid = agent["agent_id"]

            if aid in completed:
                continue

            deps = set(agent.get("dependencies", []))
            if not deps.issubset(completed):
                if aid not in state["agents"]["blocked"]:
                    state["agents"]["blocked"].append(aid)
                continue

            if aid in state["agents"]["blocked"]:
                state["agents"]["blocked"].remove(aid)
            if aid in state["agents"]["pending"]:
                state["agents"]["pending"].remove(aid)

            state["agents"]["running"].append(aid)
            result = self.runner.run(agent, self.output_dir)
            state["agents"]["running"].remove(aid)
            state["agents"]["completed"].append(aid)
            completed.add(aid)

            for rel in result.get("outputs", []):
                artifact = self.output_dir / rel
                state["artifacts"][rel] = {
                    "agent": aid,
                    "exists": artifact.exists(),
                    "size": artifact.stat().st_size if artifact.exists() and artifact.is_file() else 0,
                }

        state["current_phase"] = self._derive_current_phase(workflow, completed)
        state["quality_gates"] = self.gates.evaluate(workflow, self.output_dir)
        self.state.save(state)
        return state

    @staticmethod
    def _derive_current_phase(workflow: dict[str, Any], completed: set[str]) -> int:
        phases = sorted({int(agent["phase"]) for agent in workflow["agents"]})
        for phase in phases:
            phase_agents = [a["agent_id"] for a in workflow["agents"] if int(a["phase"]) == phase]
            if not all(aid in completed for aid in phase_agents):
                return phase
        return phases[-1] if phases else 1
