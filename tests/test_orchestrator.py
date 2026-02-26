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


def test_deploy_phase_is_idempotent_for_completed_agents(tmp_path: Path) -> None:
    workflow_file = Path("workflows/soc2_playbook.json")
    state_file = tmp_path / "state.json"
    output_dir = tmp_path / "outputs"

    engine = OrchestratorEngine(workflow_file=workflow_file, state_file=state_file, output_dir=output_dir)
    engine.init()

    first_run = engine.deploy(phase=1)
    second_run = engine.deploy(phase=1)

    assert len(first_run["agents"]["completed"]) == 3
    assert len(second_run["agents"]["completed"]) == 3
    assert second_run["current_phase"] == 1


def test_blocked_agents_are_recomputed_per_deploy(tmp_path: Path) -> None:
    workflow_file = Path("workflows/soc2_playbook.json")
    state_file = tmp_path / "state.json"
    output_dir = tmp_path / "outputs"

    engine = OrchestratorEngine(workflow_file=workflow_file, state_file=state_file, output_dir=output_dir)
    engine.init()

    blocked_state = engine.deploy(phase=2)
    assert "2.1" in blocked_state["agents"]["blocked"]

    unblocked_state = engine.deploy(phase=1)
    assert unblocked_state["agents"]["blocked"] == []
