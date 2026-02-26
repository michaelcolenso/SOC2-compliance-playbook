from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class AgentRunner:
    """Stubbed runner for orchestration bootstrapping.

    This marks agents as completed and creates placeholder output files.
    """

    def __init__(self, prompt_root: Path | None = None) -> None:
        self.prompt_root = prompt_root or Path("prompts")

    def run(self, agent: dict[str, Any], output_dir: Path) -> dict[str, Any]:
        prompt_file = self.prompt_root / agent["prompt_file"]
        if not prompt_file.exists():
            raise FileNotFoundError(f"Missing agent prompt file: {prompt_file}")

        for rel in agent.get("outputs", []):
            target = output_dir / rel
            if rel.endswith("/"):
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                target.write_text(
                    f"# Placeholder output\nagent_id: {agent['agent_id']}\n"
                    f"prompt_file: {prompt_file.as_posix()}\n"
                    f"generated_at: {datetime.now(timezone.utc).isoformat()}\n"
                )
        return {"status": "completed", "agent_id": agent["agent_id"]}
