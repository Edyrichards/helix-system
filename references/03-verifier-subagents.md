# Helix Verifier Subagents

Fresh-context verification is the main difference between a good prompt and a true agent harness.

## When to use
Use a verifier subagent when any of these are true:
- Code changes affect behavior, data, auth, payments, persistence, or shared components.
- UI/design work is user-visible and screenshots are available.
- Research will drive a product/business decision.
- The artifact is a handoff to another AI/human.
- The task took many tool calls or more than one hypothesis.

## Verifier briefs
### Code verifier
Goal: inspect the diff/artifact against the original ask. Check correctness, edge cases, security, repo fit, test evidence, and scope creep. Return: `PASS`, `PASS WITH RISKS`, or `FAIL`, with exact file/line evidence and one required fix if failing.

### UI verifier
Goal: inspect screenshot/rendered UI against the screen job. Check hierarchy, mobile/desktop layout, overflow/clipping, contrast, states, copy, and token discipline. Return top 3 issues only, each with exact fix.

### Research verifier
Goal: check whether the recommendation follows from opened sources. Verify citations are load-bearing, current, and not search snippets. Return unsupported claims and the single strongest correction.

### Handoff verifier
Goal: ensure a cold receiver can continue without chat history. Check goal, current state, verification labels, next task, acceptance criteria, constraints, and materials. Return missing context only.

## Parent-agent rule
Subagent results are self-reports. For file writes, URLs, and external side effects, verify the handle yourself before telling the user it succeeded.
