# Agentic Content Creation Workflow (Best-Practice Edition)

## Objective
Deliver a complete, audit-ready digital information product (SOC 2 Compliance Playbook) with consistent quality, traceability, and packaging readiness.

## Operating Principles
1. **Single source of truth:** the workflow file (`workflows/soc2_playbook.json`) defines dependencies and expected artifacts.
2. **Evidence-first writing:** every claim is tied to input evidence (research, interviews, controls).
3. **Definition of done at every handoff:** each agent outputs artifacts plus a concise DONE block.
4. **Quality gates over speed:** no downstream work proceeds if critical gate criteria fail.
5. **Parallelize safely:** only parallelize work with clean interface boundaries and clear contracts.

## Workflow Architecture

### Phase 1 — Research Foundation
- **1.1 Market Research Synthesizer**: captures costs, pain points, timeline and market gaps.
- **1.2 Expert Interview Coordinator**: converts interviews into structured insights.
- **1.3 Compliance Documentation Analyzer**: builds control matrix, MVCS scope, evidence requirements.

**Exit criteria:** enough market + compliance evidence to draft practical playbook guidance.

### Phase 2 — Product Blueprint
- **2.1 Playbook Architect**: converts research into the master outline and chapter specifications.
- **2.2 Template Designer**: creates design specs for core compliance templates.

**Exit criteria:** approved structure and template design specs ready for content execution.

### Phase 3 — Content Creation Engine
- **3.1a–3.1d Chapter Writer**: writes the complete chapter set using shared writing standards.
- **3.2 Template Generator**: produces implementation-ready templates and a machine-readable index.
- **3.3 AI Tool Developer**: ships practical companion tools for execution and adoption.

**Exit criteria:** full draft content package complete with templates and tools.

### Phase 4 — Validation + Hardening
- **4.1 Case Study Compiler**: converts real founder narratives into actionable case studies.
- **4.2 Visual Designer**: creates graphics that improve comprehension and actionability.
- **4.3 Technical Reviewer**: validates factual and compliance correctness.
- **4.4 Beta Reader Coordinator**: captures user feedback and prioritizes improvements.

**Exit criteria:** validated, corrected, and usability-tested product draft.

### Phase 5 — Packaging + Launch
- **5.1 Product Packager**: builds final product bundle and onboarding assets.
- **5.2 Sales Page Creator**: turns outcomes into compelling conversion assets.
- **5.3 Launch Coordinator**: builds launch plan, calendar, and measurement framework.

**Exit criteria:** launch-ready product, marketing, and execution plan.

## Standard Instruction Format (Use for Every Agent Prompt)
1. **Role + mission** (1 sentence)
2. **Business outcome** (why this matters now)
3. **Inputs + constraints** (what can/cannot be used)
4. **Execution protocol** (step-by-step method)
5. **Output contract** (exact file paths + required sections)
6. **Quality rubric** (objective pass/fail checks)
7. **DONE handoff** (summary, risks, next agent notes)

## Content Quality Rubric (Global)
- **Accuracy:** aligns with SOC 2 controls and does not overstate claims.
- **Actionability:** includes concrete steps, examples, and checklists.
- **Audience fit:** optimized for bootstrapped SaaS founders.
- **Completeness:** each output path exists and contains required sections.
- **Consistency:** terminology and frameworks are reused across chapters/templates.

## Risk Controls
- Track assumptions explicitly in each artifact.
- Add a “Known unknowns” section when evidence is incomplete.
- Flag legal/compliance boundaries with “Not legal advice” language where relevant.
- Prevent stale work by requiring dependency re-check before writing outputs.

## Handoff Template
```md
## DONE
- Output files created:
- Quality gate self-check:
- Assumptions made:
- Open risks/blockers:
- Recommended next agent handoff notes:
```

## Success Definition
The workflow is successful when all required artifacts in phases 1–5 are generated, all quality gates pass, and the product is publication-ready for paid distribution.
