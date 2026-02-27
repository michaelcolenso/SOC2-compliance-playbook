# Agent Instruction Contract (Best-Practice Template)

Use this template for all production agents.

## 1) Outcome
State the single business outcome the agent must produce.

## 2) Context
- Workflow phase and role
- Target audience
- Dependencies that must be complete
- Non-goals (what this agent should not do)

## 3) Inputs
- Required files
- Optional reference files
- Input assumptions if files are missing/stale

## 4) Output Contract
For each output include:
- File path
- Required sections/schema
- Definition of done

## 5) Operating Procedure
Use a deterministic sequence:
1. Validate dependency completion.
2. Inspect required inputs.
3. Produce deliverables in output order.
4. Run self-QA against rubric.
5. Emit handoff notes and DONE block.

## 6) Quality Rubric
Score 1-5 on:
- Accuracy
- Coverage
- Actionability
- Consistency with prior outputs
- Clarity and implementation-readiness

Minimum passing score: 4/5 in every dimension.

## 7) Handoff Notes
Provide:
- What changed
- Open risks
- Next agent recommendations

## 8) Completion Checklist
- [ ] All required outputs created at exact paths
- [ ] Rubric self-score included
- [ ] Open issues documented
- [ ] DONE block appended
