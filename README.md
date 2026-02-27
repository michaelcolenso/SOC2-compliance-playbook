# SOC2 Compliance Playbook

Bootstrapped orchestration scaffold for running the SOC 2 multi-agent workflow.

## What is set up

- Workflow definition at `workflows/soc2_playbook.json`
- Detailed workflow design notes at `docs/agentic_content_workflow.md`
- Shared instruction contract template at `prompts/_shared/instruction_contract.md`
- Agent instruction prompts at `prompts/` (sourced from `output.md`, `output2.md`, `output3.md`)
- CLI orchestrator at `src/orchestrator`
- Reporting utility at `src/monitor/reporter.py`
- Local state/output directories (`data/`, `outputs/`, `logs/`, `reports/`)

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
make init
make kickoff
make status
make phase N=1
```

## Common commands

- `make init` – initialize state file
- `make status` – show orchestration status
- `make bootstrap` – initialize state (if needed) and run phase 1 agents
- `make kickoff` – bootstrap and run the full workflow
- `make phase N=1` – run a workflow phase
- `make agent A=1.1` – run one agent
- `make run-all` – run all agents with dependency checks
- `make report` – show summarized progress
- `make test` – run test suite


## Workflow enhancements

- Added **3.4 Content Fact Checker** to verify claims across drafted chapters.
- Added **3.5 Editorial Integrator** to apply fact-check corrections and generate a unified manuscript.
- Updated downstream dependencies so validation and launch phases consume editorially integrated content.
