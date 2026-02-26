# Agent 5.2: Sales Page Creator

## Mission
Execute this agent according to the orchestrated workflow in `output.md`, detailed prompt patterns in `output2.md`, and the sequencing/quality cadence in `output3.md`.

## Workflow context
- Phase: 5
- Dependencies: 4.1
- Parallelizable: true
- Timeout (seconds): 3600
- Retries: 2

## Required inputs
- research/pain_points.md
- case_studies/
- product/soc2_playbook_complete.pdf

## Required outputs
- marketing/sales_page.md
- marketing/email_sequence.md
- marketing/social_posts.md
- marketing/product_mockups/

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
