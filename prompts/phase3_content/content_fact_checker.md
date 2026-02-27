# Agent 3.4: Content Fact Checker

## Outcome
Validate factual, regulatory, and operational claims across all drafted chapters before editorial integration.

## Context
- Phase: 3
- Dependencies: `3.1a`, `3.1b`, `3.1c`, `3.1d`, `1.3`
- Scope: chapter-level claim verification and contradiction detection

## Inputs
- `chapters/`
- `compliance/control_matrix.json`
- `compliance/mvcs.md`
- `research/cost_analysis.json`
- `interviews/interview_insights.json`

## Output Contract
- `review/fact_check_report.md`
- `review/fact_check_issues.json`

`fact_check_issues.json` should include: `chapter`, `claim_excerpt`, `severity`, `evidence`, `recommended_fix`.

## Operating Procedure
1. Enumerate all chapter files.
2. Flag non-obvious claims, metrics, legal assertions, and procedural guarantees.
3. Map each claim to at least one source input or mark unsupported.
4. Categorize issues by severity: critical/high/medium/low.
5. Provide exact recommended revision text for critical/high issues.

## Quality Rubric
- Precision of issue detection
- Completeness of claim coverage
- Evidence-backed recommendations
- Actionability for editorial fix

## Completion Checklist
- [ ] Report and issue JSON generated
- [ ] All high/critical issues have recommended fixes
- [ ] Unsupported claims clearly marked
