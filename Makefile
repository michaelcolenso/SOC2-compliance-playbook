PYTHON ?= python3

init:
	$(PYTHON) -m src.orchestrator init

status:
	$(PYTHON) -m src.orchestrator status

bootstrap:
	$(PYTHON) -m src.orchestrator bootstrap

kickoff:
	$(PYTHON) -m src.orchestrator kickoff

phase:
	$(PYTHON) -m src.orchestrator deploy --phase $(N)

agent:
	$(PYTHON) -m src.orchestrator deploy --agent $(A)

run-all:
	$(PYTHON) -m src.orchestrator deploy --all

report:
	$(PYTHON) -m src.monitor.reporter

test:
	pytest -q
