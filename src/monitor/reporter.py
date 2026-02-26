from __future__ import annotations

from pathlib import Path
from pprint import pprint

from src.orchestrator.engine import OrchestratorEngine


def main() -> None:
    engine = OrchestratorEngine(
        workflow_file=Path("workflows/soc2_playbook.json"),
        state_file=Path("data/workflow_state.json"),
        output_dir=Path("outputs"),
    )
    state = engine.status()
    passed_gates = sum(1 for gate in state.get("quality_gates", {}).values() if gate.get("status") == "passed")
    summary = {
        "current_phase": state.get("current_phase"),
        "completed": len(state["agents"]["completed"]),
        "pending": len(state["agents"]["pending"]),
        "blocked": len(state["agents"]["blocked"]),
        "failed": len(state["agents"]["failed"]),
        "quality_gates_passed": passed_gates,
        "quality_gates_total": len(state.get("quality_gates", {})),
    }
    pprint(summary)


if __name__ == "__main__":
    main()
