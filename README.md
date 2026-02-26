# SOC2-compliance-playbook

agentic-repo/
├── README.md                    # Main documentation
├── AGENTIC_REPO_GUIDE.md        # Complete setup guide
├── requirements.txt             # Python dependencies
├── Makefile                     # Convenience commands
├── Dockerfile                   # Container definition
├── docker-compose.yml           # Multi-service orchestration
├── .env.example                 # Environment template
├── .gitignore                   # Git ignore rules
│
├── workflows/
│   └── soc2_playbook.json       # 21 agents, 15 quality gates
│
├── agents/                      # Agent prompts
│   ├── phase1_research/market_research.md
│   └── phase3_content/chapter_writer.md
│
├── src/orchestrator/            # Core orchestration
│   ├── engine.py                # Main orchestrator
│   ├── state_manager.py         # SQLite state
│   ├── agent_runner.py          # LLM execution
│   ├── quality_gates.py         # Validation
│   └── __main__.py              # CLI
│
├── src/monitor/
│   └── reporter.py              # Progress reports
│
└── tests/
    └── test_orchestrator.py     # Test suite
