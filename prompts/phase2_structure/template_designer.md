# Agent 2.2: Template Designer

## Mission
Execute this agent according to the orchestrated workflow in `output.md`, detailed prompt patterns in `output2.md`, and the sequencing/quality cadence in `output3.md`.

## Workflow context
- Phase: 2
- Dependencies: 1.3
- Parallelizable: true
- Timeout (seconds): 3600
- Retries: 2

## Required inputs
- compliance/mvcs.md
- compliance/evidence_requirements.json

## Required outputs
- templates/designs/security_policies.md
- templates/designs/access_control.md
- templates/designs/vendor_management.md
- templates/designs/incident_response.md
- templates/designs/audit_prep.md
- templates/customization_guide.md

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
