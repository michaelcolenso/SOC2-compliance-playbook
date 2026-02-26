# Agent 4.4: Beta Reader Coordinator

## Mission
Execute this agent according to the orchestrated workflow in `output.md`, detailed prompt patterns in `output2.md`, and the sequencing/quality cadence in `output3.md`.

## Workflow context
- Phase: 4
- Dependencies: 3.1a, 3.1b, 3.1c, 3.1d, 3.2, 4.1
- Parallelizable: false
- Timeout (seconds): 7200
- Retries: 2

## Required inputs
- chapters/
- templates/generated/
- case_studies/

## Required outputs
- feedback/beta_feedback.json
- feedback/priority_changes.md

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
