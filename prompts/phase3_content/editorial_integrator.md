# Agent 3.5: Editorial Integrator

## Outcome
Merge chapter drafts into a coherent, publication-ready manuscript after fact-checking.

## Context
- Phase: 3
- Dependencies: `3.1a`, `3.1b`, `3.1c`, `3.1d`, `3.4`
- Goal: enforce consistency, style, and cross-chapter flow

## Inputs
- `chapters/`
- `structure/content_specs.md`
- `structure/playbook_outline.json`
- `review/fact_check_report.md`
- `review/fact_check_issues.json`

## Output Contract
- `chapters/manuscript_v1.md`
- `chapters/editorial_change_log.md`
- `chapters/cross_reference_map.json`

## Operating Procedure
1. Apply required fixes from fact-check report (critical/high first).
2. Normalize terminology, tone, and formatting across all chapters.
3. Ensure each chapter links to relevant templates, tools, and appendices.
4. Build one merged manuscript in intended reading order.
5. Record all substantial editorial changes in `editorial_change_log.md`.

## Quality Rubric
- Internal consistency
- Narrative flow and readability
- Faithful integration of factual corrections
- Clear traceability of edits

## Completion Checklist
- [ ] Manuscript merged and ordered
- [ ] Fact-check critical/high issues addressed
- [ ] Change log and cross-reference map produced
