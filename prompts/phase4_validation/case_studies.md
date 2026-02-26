# Agent 4.1: Case Study Compiler

## Mission
Execute this agent according to the orchestrated workflow in `output.md`, detailed prompt patterns in `output2.md`, and the sequencing/quality cadence in `output3.md`.

## Workflow context
- Phase: 4
- Dependencies: 1.2, 3.1a, 3.1b, 3.1c, 3.1d
- Parallelizable: true
- Timeout (seconds): 3600
- Retries: 2

## Required inputs
- interviews/founder_01_transcript.md
- interviews/founder_02_transcript.md
- interviews/founder_03_transcript.md
- interviews/interview_insights.json
- research/cost_analysis.json

## Required outputs
- case_studies/case_study_01.md
- case_studies/case_study_02.md
- case_studies/case_study_03.md
- case_studies/case_study_04.md
- case_studies/case_study_05.md
- case_studies/summary_table.json

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
