from pathlib import Path

from src.orchestrator.engine import OrchestratorEngine


def test_init_and_deploy_phase(tmp_path: Path) -> None:
    workflow_file = Path("workflows/soc2_playbook.json")
    state_file = tmp_path / "state.json"
    output_dir = tmp_path / "outputs"

    engine = OrchestratorEngine(workflow_file=workflow_file, state_file=state_file, output_dir=output_dir)
    state = engine.init()
    assert state["workflow_id"] == "soc2-playbook-v1"

    state = engine.deploy(phase=1)
    assert all(a in state["agents"]["completed"] for a in ["1.1", "1.2", "1.3"])
