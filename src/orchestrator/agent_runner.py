from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class AgentRunner:
    """Stubbed runner for orchestration bootstrapping.

    This marks agents as completed and creates placeholder output files.
    """

    def run(self, agent: dict[str, Any], output_dir: Path) -> dict[str, Any]:
        for rel in agent.get("outputs", []):
            target = output_dir / rel
            if rel.endswith("/"):
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                target.write_text(
                    f"# Placeholder output\nagent_id: {agent['agent_id']}\n"
                    f"generated_at: {datetime.now(timezone.utc).isoformat()}\n"
                )
        return {"status": "completed", "agent_id": agent["agent_id"]}
