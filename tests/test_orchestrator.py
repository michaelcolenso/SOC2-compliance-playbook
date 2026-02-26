import json
from pathlib import Path

from src.orchestrator.engine import OrchestratorEngine
from src.orchestrator.quality_gates import QualityGateEvaluator


def test_init_and_deploy_phase(tmp_path: Path) -> None:
    workflow_file = Path("workflows/soc2_playbook.json")
    state_file = tmp_path / "state.json"
    output_dir = tmp_path / "outputs"

    engine = OrchestratorEngine(workflow_file=workflow_file, state_file=state_file, output_dir=output_dir)
    state = engine.init()
    assert state["workflow_id"] == "soc2-playbook-v1"

    state = engine.deploy(phase=1)
    assert all(a in state["agents"]["completed"] for a in ["1.1", "1.2", "1.3"])
    assert state["current_phase"] == 2
    assert "research/cost_analysis.json" in state["artifacts"]


def test_deploy_all_respects_dependencies(tmp_path: Path) -> None:
    workflow_file = Path("workflows/soc2_playbook.json")
    state_file = tmp_path / "state.json"
    output_dir = tmp_path / "outputs"

    engine = OrchestratorEngine(workflow_file=workflow_file, state_file=state_file, output_dir=output_dir)
    engine.init()
    state = engine.deploy(run_all=True)

    assert len(state["agents"]["completed"]) == 18
    assert state["agents"]["blocked"] == []


def test_data_points_gate_uses_field_length(tmp_path: Path) -> None:
    output_dir = tmp_path / "outputs"
    target = output_dir / "research" / "cost_analysis.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps({"cost_data_points": list(range(21))}))

    evaluator = QualityGateEvaluator()
    gate = {"type": "data_points", "file": "research/cost_analysis.json", "field": "cost_data_points", "min_count": 20}
    result = evaluator.evaluate({"quality_gates": {"1.1": gate}}, output_dir)

    assert result["1.1"]["status"] == "passed"
