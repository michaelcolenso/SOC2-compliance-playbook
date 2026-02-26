# Agent 5.3: Launch Coordinator

## Mission
Execute this agent according to the orchestrated workflow in `output.md`, detailed prompt patterns in `output2.md`, and the sequencing/quality cadence in `output3.md`.

## Workflow context
- Phase: 5
- Dependencies: 5.1, 5.2
- Parallelizable: false
- Timeout (seconds): 1800
- Retries: 2

## Required inputs
- marketing/sales_page.md
- product/
- case_studies/

## Required outputs
- launch/launch_plan.md
- launch/content_calendar.md
- launch/tracking_sheet.json

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
