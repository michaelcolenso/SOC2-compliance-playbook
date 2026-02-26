from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class StateManager:
    state_file: Path

    def initialize(self, workflow: dict[str, Any]) -> dict[str, Any]:
        state = {
            "workflow_id": workflow["workflow_id"],
            "current_phase": 1,
            "initialized_at": self._now(),
            "agents": {
                "pending": [a["agent_id"] for a in workflow["agents"]],
                "running": [],
                "completed": [],
                "failed": [],
                "blocked": [],
            },
            "quality_gates": {},
            "artifacts": {},
        }
        self.save(state)
        return state

    def load(self) -> dict[str, Any]:
        if not self.state_file.exists():
            raise FileNotFoundError(f"State file not found: {self.state_file}")
        return json.loads(self.state_file.read_text())

    def save(self, state: dict[str, Any]) -> None:
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        self.state_file.write_text(json.dumps(state, indent=2))

    @staticmethod
    def _now() -> str:
        return datetime.now(timezone.utc).isoformat()
