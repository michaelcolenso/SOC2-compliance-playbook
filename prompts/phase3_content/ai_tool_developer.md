# Agent 3.3: AI Tool Developer

## Mission
Execute this agent according to the orchestrated workflow in `output.md`, detailed prompt patterns in `output2.md`, and the sequencing/quality cadence in `output3.md`.

## Workflow context
- Phase: 3
- Dependencies: 2.1
- Parallelizable: true
- Timeout (seconds): 14400
- Retries: 2

## Required inputs
- compliance/mvcs.md
- research/cost_analysis.json
- structure/playbook_outline.json

## Required outputs
- tools/readiness_scorecard/
- tools/policy_generator/
- tools/auditor_matcher/
- tools/evidence_tracker/
- tools/chatbot/

## Execution instructions
1. Confirm all dependencies are complete before starting.
2. Follow the role behavior for this agent from `output.md` (phase architecture + quality gates).
3. Use the agent prompt style from `output2.md`:
   - produce structured, source-backed deliverables,
   - include explicit assumptions,
   - include actionable checklists and practical implementation steps.
4. Follow delivery cadence from `output3.md`:
   - prioritize day/phase milestones,
   - include a concise completion checklist for handoff,
   - call out blockers and next actions.
5. Save outputs exactly to the paths listed above.
6. Include a short `DONE` section with:
   - quality-gate self-check,
   - open risks,
   - recommended next agent handoff notes.
