from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class AgentRunner:
    """Stubbed runner for orchestration bootstrapping.

    This marks agents as completed and creates placeholder output files.
    """

    def run(self, agent: dict[str, Any], output_dir: Path) -> dict[str, Any]:
        written: list[str] = []
        for rel in agent.get("outputs", []):
            target = output_dir / rel
            if rel.endswith("/"):
                target.mkdir(parents=True, exist_ok=True)
                if "tools/" in rel:
                    index_file = target / "index.html"
                    if not index_file.exists():
                        index_file.write_text("<html><body><h1>Placeholder Tool UI</h1></body></html>\n")
                written.append(rel)
                continue

            target.parent.mkdir(parents=True, exist_ok=True)
            if target.suffix == ".json":
                payload = self._json_placeholder(rel, agent["agent_id"])
                target.write_text(json.dumps(payload, indent=2))
            else:
                target.write_text(
                    f"# Placeholder output\nagent_id: {agent['agent_id']}\n"
                    f"generated_at: {datetime.now(timezone.utc).isoformat()}\n"
                )
            written.append(rel)

        return {"status": "completed", "agent_id": agent["agent_id"], "outputs": written}


    def _json_placeholder(self, rel: str, agent_id: str) -> dict[str, Any]:
        now = datetime.now(timezone.utc).isoformat()
        if rel == "research/cost_analysis.json":
            return {
                "agent_id": agent_id,
                "generated_at": now,
                "status": "placeholder",
                "cost_data_points": list(range(20)),
            }
        return {
            "agent_id": agent_id,
            "generated_at": now,
            "status": "placeholder",
        }
