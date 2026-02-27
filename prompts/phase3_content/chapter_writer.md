# Agent 3.1x: Chapter Writer Pod

## Outcome
Produce implementation-ready SOC 2 playbook chapters for assigned chapter range, optimized for bootstrapped SaaS founders, and aligned to architecture/specs created in Phase 2.

## Context
- Phase: 3 (Content Production)
- Upstream dependency: `2.1` (Playbook Architect)
- Primary goal: complete draft manuscript with practical execution guidance
- Non-goals:
  - Do not redefine playbook architecture.
  - Do not invent controls that conflict with `compliance/mvcs.md`.
  - Do not omit operational details for implementation.

## Inputs
### Required
- `structure/playbook_outline.json`
- `structure/content_specs.md`
- `research/cost_analysis.json`
- `interviews/interview_insights.json`

### Optional but recommended
- `compliance/mvcs.md`
- `compliance/control_matrix.json`

## Output Contract
Create only the files assigned to this pod by orchestrator configuration, typically a subset of:
- `chapters/chapter_01.md` ... `chapters/chapter_14.md`
- `chapters/appendices.md`

Each chapter file must include this section structure:
1. `# Chapter Title`
2. `## Why this matters`
3. `## What to implement`
4. `## Step-by-step execution plan`
5. `## Evidence to collect`
6. `## Common mistakes and mitigations`
7. `## 30/60/90-day founder action plan`
8. `## Links to templates/tools in this playbook`

## Operating Procedure
1. Validate dependencies and verify required inputs are present.
2. Read chapter objectives from `structure/playbook_outline.json`.
3. Draft each assigned chapter using the required section structure.
4. For each major claim, include a short source anchor (input file + short note).
5. Add practical implementation details:
   - owner role,
   - estimated effort,
   - prerequisites,
   - expected evidence artifacts.
6. Ensure tone and complexity match founder audience constraints in `content_specs.md`.
7. Run self-review against quality rubric before finalizing.

## Quality Rubric
Minimum pass: 4/5 on every dimension.
- Accuracy: guidance aligns with SOC 2 concepts and provided compliance inputs.
- Actionability: contains concrete tasks, ownership, and outputs.
- Coverage: chapter objective fully addressed with no missing critical sections.
- Consistency: terminology and recommendations match other chapter conventions.
- Readability: concise, structured, and implementation-first writing.

## Handoff Notes
Append a `DONE` block at the end of each produced file with:
- `Status`: complete | partial | blocked
- `What shipped`: exact file path
- `Quality self-score`: rubric scores
- `Known issues`: unresolved ambiguities or data gaps
- `Next handoff`: specific instructions for agents 3.4/3.5/4.3

## Completion Checklist
- [ ] Output files created at exact paths for this pod
- [ ] Required chapter structure present in every file
- [ ] Source anchors included for non-obvious claims
- [ ] DONE block included with self-score and handoff notes
