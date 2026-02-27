# Agentic Content Creation Workflow (SOC 2 Playbook)

## Objective
Design a production-ready, multi-agent workflow that reliably produces a complete and publishable digital information product (the SOC 2 Compliance Playbook) with consistent quality, traceability, and handoff discipline.

## Core design principles
1. Single-responsibility agents: each agent has one clear job and explicit outputs.
2. Contract-first instructions: prompts define role, inputs, output schema, quality rubric, and handoff format.
3. Dependency-aware orchestration: upstream outputs are validated before downstream execution.
4. Parallel where safe: chapter writing and asset generation run concurrently after architecture freeze.
5. Progressive hardening: draft -> technical review -> editorial integration -> final packaging.
6. Evidence and auditability: every major output includes assumptions, source anchors, and decision logs.
7. Gate-driven completion: no phase exits without satisfying measurable acceptance criteria.

## Workflow map

### Phase 1 - Research Intelligence
- 1.1 Market Research Synthesizer
- 1.2 Expert Interview Coordinator
- 1.3 Compliance Documentation Analyzer

**Exit criteria**
- Quantified pain/cost evidence.
- Founder voice-of-customer data.
- SOC 2 controls, evidence requirements, and MVCS baseline.

### Phase 2 - Content Architecture
- 2.1 Playbook Architect (book-level blueprint)
- 2.2 Template Designer (template specifications)

**Exit criteria**
- Locked outline with chapter objectives and target audience level.
- Content specs including style, reading time, and artifact requirements.

### Phase 3 - Content Production (primary creation stage)
- 3.1a-3.1d Chapter Writer pods (parallel writing streams)
- 3.2 Template Generator
- 3.3 AI Tool Developer
- 3.4 Content Fact Checker (new)
- 3.5 Editorial Integrator (new)

**Exit criteria**
- Full manuscript drafted.
- Claims validated against approved sources.
- Unified editorial pass complete (voice, structure, cross-references, consistency).

### Phase 4 - Validation
- 4.1 Case Study Compiler
- 4.2 Visual Designer
- 4.3 Technical Reviewer
- 4.4 Beta Reader Coordinator

**Exit criteria**
- Technical correctness and practical usability validated.
- Visual reinforcement assets produced.
- Priority changes identified and ranked.

### Phase 5 - Productization and Launch
- 5.1 Product Packager
- 5.2 Sales Page Creator
- 5.3 Launch Coordinator

**Exit criteria**
- Delivery package complete.
- Go-to-market assets complete.
- Launch execution plan approved.

## Instruction formatting standard (recommended)
Use the following section order in every agent prompt:
1. `# Agent ID + Name`
2. `## Outcome`
3. `## Context`
4. `## Inputs`
5. `## Output Contract`
6. `## Operating Procedure`
7. `## Quality Rubric`
8. `## Handoff Notes`
9. `## Completion Checklist`

This format is implemented in `prompts/_shared/instruction_contract.md` and applied to content-critical prompts.

## Handoff contract (mandatory)
Every agent should append a `DONE` block:
- `Status`: complete / partial / blocked
- `What shipped`: exact output paths
- `Quality self-score`: 1-5 against rubric
- `Known issues`: factual gaps, unresolved conflicts, TODOs
- `Recommended next agent actions`: specific, ordered bullets

## Quality guardrails for content creation
- No unsupported claims: every non-obvious assertion must include a source anchor.
- Audience fit: write for bootstrapped SaaS founders with limited compliance bandwidth.
- Actionability: include implementation steps, owner roles, and estimated effort.
- Consistency: terminology must align with `compliance/mvcs.md` and control matrix naming.
- Reusability: templates and tools must map directly to chapter workflows.

## Metrics to track
- Draft completeness (% of required chapters generated)
- Review defect density (major issues per chapter)
- Evidence coverage (% of claims with source anchors)
- Rework rate (post-review changes per chapter)
- Time-to-publish (phase 1 start -> packaging complete)
