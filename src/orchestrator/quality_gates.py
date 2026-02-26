from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class QualityGateEvaluator:
    def evaluate(self, workflow: dict[str, Any], output_dir: Path) -> dict[str, dict[str, Any]]:
        gates: dict[str, dict[str, Any]] = {}
        for gate_id, gate in workflow.get("quality_gates", {}).items():
            gate_type = gate.get("type")
            if gate_type == "file_count":
                gates[gate_id] = self._eval_file_count(gate, output_dir)
            elif gate_type == "data_points":
                gates[gate_id] = self._eval_data_points(gate, output_dir)
            elif gate_type == "interviews":
                gates[gate_id] = self._eval_interviews(gate, output_dir)
            elif gate_type == "page_count":
                gates[gate_id] = self._eval_page_count(gate, output_dir)
            elif gate_type == "beta_feedback":
                gates[gate_id] = self._eval_beta_feedback(gate, output_dir)
            elif gate_type == "custom":
                gates[gate_id] = {"status": "pending", "type": gate_type, "reason": "custom gate not implemented"}
            else:
                gates[gate_id] = {"status": "pending", "type": gate_type, "reason": "unknown gate type"}
        return gates

    def _eval_file_count(self, gate: dict[str, Any], output_dir: Path) -> dict[str, Any]:
        files = gate.get("files", [])
        existing = [f for f in files if (output_dir / f).exists()]
        min_count = int(gate.get("min_count", len(files)))
        status = "passed" if len(existing) >= min_count else "pending"
        return {
            "status": status,
            "type": "file_count",
            "matched": len(existing),
            "required": min_count,
        }

    def _eval_data_points(self, gate: dict[str, Any], output_dir: Path) -> dict[str, Any]:
        target = output_dir / gate["file"]
        min_count = int(gate.get("min_count", 0))
        field = gate.get("field")
        count = 0

        if target.exists():
            try:
                data = json.loads(target.read_text())
                if field and isinstance(data, dict):
                    value = data.get(field, [])
                    count = len(value) if isinstance(value, list) else int(bool(value))
                elif isinstance(data, list):
                    count = len(data)
                elif isinstance(data, dict):
                    count = len(data)
                else:
                    count = int(bool(data))
            except (json.JSONDecodeError, ValueError):
                count = 0

        return {
            "status": "passed" if count >= min_count else "pending",
            "type": "data_points",
            "count": count,
            "required": min_count,
        }

    def _eval_interviews(self, gate: dict[str, Any], output_dir: Path) -> dict[str, Any]:
        interview_dir = output_dir / "interviews"
        min_count = int(gate.get("min_count", 0))
        count = len(list(interview_dir.glob("founder_*_transcript.md"))) if interview_dir.exists() else 0
        return {
            "status": "passed" if count >= min_count else "pending",
            "type": "interviews",
            "count": count,
            "required": min_count,
        }

    def _eval_page_count(self, gate: dict[str, Any], output_dir: Path) -> dict[str, Any]:
        chapters_dir = output_dir / gate.get("chapters_dir", "chapters")
        min_pages = int(gate.get("min_pages", 0))
        if not chapters_dir.exists():
            return {"status": "pending", "type": "page_count", "pages": 0, "required": min_pages}

        markdown_files = list(chapters_dir.glob("*.md"))
        words = sum(len(path.read_text().split()) for path in markdown_files)
        estimated_pages = words // 500
        return {
            "status": "passed" if estimated_pages >= min_pages else "pending",
            "type": "page_count",
            "pages": estimated_pages,
            "required": min_pages,
        }

    def _eval_beta_feedback(self, gate: dict[str, Any], output_dir: Path) -> dict[str, Any]:
        feedback_file = output_dir / "feedback" / "beta_feedback.json"
        if not feedback_file.exists():
            return {"status": "pending", "type": "beta_feedback", "responses": 0}

        try:
            payload = json.loads(feedback_file.read_text())
        except json.JSONDecodeError:
            return {"status": "pending", "type": "beta_feedback", "responses": 0, "reason": "invalid json"}

        responses = payload.get("responses", []) if isinstance(payload, dict) else []
        min_responses = int(gate.get("min_responses", 0))
        min_rating = float(gate.get("min_rating", 0.0))
        min_would_pay = float(gate.get("min_would_pay_percent", 0.0))

        avg_rating = (
            sum(float(r.get("rating", 0)) for r in responses) / len(responses)
            if responses
            else 0.0
        )
        would_pay_ratio = (
            sum(1 for r in responses if r.get("would_pay") is True) / len(responses)
            if responses
            else 0.0
        )

        passed = (
            len(responses) >= min_responses
            and avg_rating >= min_rating
            and would_pay_ratio >= min_would_pay
        )

        return {
            "status": "passed" if passed else "pending",
            "type": "beta_feedback",
            "responses": len(responses),
            "avg_rating": round(avg_rating, 2),
            "would_pay_ratio": round(would_pay_ratio, 2),
        }
