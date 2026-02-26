from __future__ import annotations

from pathlib import Path
from typing import Any


class QualityGateEvaluator:
    def evaluate(self, workflow: dict[str, Any], output_dir: Path) -> dict[str, dict[str, Any]]:
        gates: dict[str, dict[str, Any]] = {}
        for gate_id, gate in workflow.get("quality_gates", {}).items():
            gate_file = gate.get("file")
            if gate_file:
                exists = (output_dir / gate_file).exists()
                gates[gate_id] = {"status": "passed" if exists else "pending", "type": gate.get("type")}
            else:
                gates[gate_id] = {"status": "pending", "type": gate.get("type")}
        return gates
