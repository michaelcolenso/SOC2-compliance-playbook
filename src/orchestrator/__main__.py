from __future__ import annotations

import argparse
import os
from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv

from .engine import OrchestratorEngine


def build_engine() -> OrchestratorEngine:
    load_dotenv()
    return OrchestratorEngine(
        workflow_file=Path(os.getenv("WORKFLOW_FILE", "workflows/soc2_playbook.json")),
        state_file=Path(os.getenv("STATE_FILE", "data/workflow_state.json")),
        output_dir=Path(os.getenv("OUTPUT_DIR", "outputs")),
        prompt_dir=Path(os.getenv("PROMPT_DIR", "prompts")),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="SOC2 playbook orchestrator")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init")
    sub.add_parser("status")

    deploy = sub.add_parser("deploy")
    deploy.add_argument("--phase", type=int)
    deploy.add_argument("--agent")
    deploy.add_argument("--all", action="store_true")

    args = parser.parse_args()
    engine = build_engine()

    if args.command == "init":
        pprint(engine.init())
    elif args.command == "status":
        pprint(engine.status())
    elif args.command == "deploy":
        pprint(engine.deploy(phase=args.phase, agent_id=args.agent, run_all=args.all))


if __name__ == "__main__":
    main()
