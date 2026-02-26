# SOC 2 Playbook — Agentic Repository

Multi-agent orchestration system for creating knowledge products. This repository contains the complete infrastructure to deploy, coordinate, and execute 21 specialized agents across 5 phases.

## Quick Start

```bash
# Clone and setup
git clone <repo-url>
cd soc2-playbook-agents

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Initialize workflow state
python -m src.orchestrator.init

# Deploy Phase 1 agents
python -m src.orchestrator.deploy --phase 1

# Monitor execution
python -m src.monitor.dashboard
```

## Repository Structure

```
.
├── agents/                    # Agent definitions and prompts
│   ├── phase1_research/       # Research agents
│   ├── phase2_structure/      # Structure agents
│   ├── phase3_content/        # Content creation agents
│   ├── phase4_validation/     # Validation agents
│   └── phase5_launch/         # Launch agents
├── src/
│   ├── orchestrator/          # Orchestration engine
│   ├── state/                 # State management
│   ├── tools/                 # AI tools (scorecard, generator, etc.)
│   ├── shared/                # Shared utilities
│   └── monitor/               # Monitoring & logging
├── workflows/                 # Workflow definitions
├── outputs/                   # Agent outputs
├── tests/                     # Test suite
├── docker/                    # Container configs
└── docs/                      # Documentation
```

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION ENGINE                      │
│  - State management (SQLite/Redis)                          │
│  - Agent scheduling                                         │
│  - Quality gate enforcement                                 │
│  - Error handling & retries                                 │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐   ┌─────────────────┐   ┌─────────────────┐
│  AGENT POOL   │   │  STATE STORE    │   │  OUTPUT STORE   │
│  (Docker      │   │  (SQLite/       │   │  (File system   │
│   containers) │   │   PostgreSQL)   │   │   + S3)         │
└───────────────┘   └─────────────────┘   └─────────────────┘
```

## Agent Execution Model

Each agent runs as an isolated process with:
- **Input:** Structured data from previous agents
- **Output:** Structured data + artifacts
- **State:** Read/write access to workflow state
- **Logging:** Structured logging to central system

## Workflow State

```json
{
  "workflow_id": "soc2-playbook-v1",
  "current_phase": 3,
  "agents": {
    "completed": ["1.1", "1.2", "1.3", "2.1", "2.2"],
    "running": ["3.1a", "3.1b", "3.2"],
    "pending": ["3.1c", "3.1d", "3.3"],
    "blocked": [],
    "failed": []
  },
  "quality_gates": {
    "1.1": {"status": "passed", "timestamp": "2024-01-15T10:00:00Z"},
    "1.2": {"status": "passed", "timestamp": "2024-01-15T14:00:00Z"}
  },
  "artifacts": {
    "research/cost_analysis.json": {"agent": "1.1", "size": 15234},
    "interviews/founder_01.md": {"agent": "1.2", "size": 8934}
  }
}
```

## Commands

```bash
# Deploy all agents in a phase
python -m src.orchestrator.deploy --phase 3

# Deploy specific agent
python -m src.orchestrator.deploy --agent 3.1a

# Check workflow status
python -m src.orchestrator.status

# View agent logs
python -m src.monitor.logs --agent 3.1a --tail 100

# Force retry failed agent
python -m src.orchestrator.retry --agent 3.1c

# Generate progress report
python -m src.monitor.report --format html
```

## Environment Variables

```bash
# LLM APIs
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-...

# Storage
STATE_DB_URL=sqlite:///data/workflow.db
OUTPUT_DIR=./outputs
S3_BUCKET=soc2-playbook-outputs

# Monitoring
LOG_LEVEL=INFO
SENTRY_DSN=https://...

# Agent Config
MAX_RETRIES=3
AGENT_TIMEOUT=3600
PARALLEL_AGENTS=4
```

## License

MIT
