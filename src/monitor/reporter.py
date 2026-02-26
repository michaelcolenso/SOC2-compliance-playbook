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
    summary = {
        "completed": len(state["agents"]["completed"]),
        "pending": len(state["agents"]["pending"]),
        "blocked": len(state["agents"]["blocked"]),
        "failed": len(state["agents"]["failed"]),
    }
    pprint(summary)


if __name__ == "__main__":
    main()
