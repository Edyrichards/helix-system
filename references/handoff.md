# Helix Handoff Layer

## How to Hand Work to Another AI
A model receiving your work has zero shared context and infinite willingness to guess. The brief must eliminate guessing:
1. **Goal** — the outcome, one sentence, in the original user's terms.
2. **Current state** — what exists, where, and its verification status.
3. **Exact next task** — one task, scoped, with acceptance criteria.
4. **Constraints** — stack, patterns to follow, files not to touch, decisions already made (with one-line rationale so they aren't relitigated).
5. **Materials** — only the files/snippets the receiver must read. Attach or path them; never say "see our earlier discussion."

## How to Hand Work to a Developer
Lead with what changed and how to run it: entry point, commands, env vars needed, what's verified vs. not, known gaps, and where the bodies are buried (hacks, TODOs, fragile spots). Developers forgive missing polish; they don't forgive undisclosed landmines.

## How to Hand Work to a Designer
Give the goal, the user, the constraints (tokens, brand, platform), the current rendered state (screenshots, not code), and the specific problems to solve — not the solutions. Include what must not change and why.

## How to Hand Work to a Business Stakeholder
One page: decision needed (first line), recommendation, 3 supporting points, risks, cost/effort, and what happens if we do nothing. No implementation detail unless asked. The artifact should be forwardable without you in the room.

## How to Summarize Context
Compress by *decision*, not by chronology: what was decided, why (one line), and what's still open. A good summary lets the receiver reconstruct the state; it never requires them to reconstruct the conversation.

## How to Remove Noise
Cut: abandoned approaches (unless the receiver might retry them — then one line: "tried X, failed because Y"), conversational detours, praise, process narration, and anything re-derivable from the code or files provided.
Keep: decisions, constraints, verification status, open questions, gotchas.

## How to Include Constraints
Constraints are the highest-value lines in a handoff — they prevent expensive wrong turns. State them as rules with reasons: "Use the existing `api-client.ts` wrapper (it handles auth refresh); direct fetch calls will 401 after 15 min."

## How to Include Verification Status
Three labels, applied per deliverable, never omitted:
- ✅ **Verified:** <how> — e.g., "ran E2E on checkout, screenshot attached"
- ⚠️ **Implemented, unverified:** <exact step to verify>
- ❌ **Not done:** <why + what's needed>

## How to Make One Model Critique Another
Strip authorship and framing — present the output cold with the original task. Give the critique rubric (see `helix-critique-layer.md`), demand quoted evidence for every score, and forbid style-based judgment. Never tell the critic which model made it or what you hope the verdict is.

## How to Compare Outputs Fairly
Same prompt, same context, same materials, verbatim. Score against pre-written criteria (written *before* seeing outputs). Randomize which is "A" and "B". Score dimensions independently; a fluent output must not get a correctness halo.

## Handoff Templates

### AI-to-AI Handoff Brief
```markdown
# Handoff: <task name>
**Goal:** <one sentence>
**Stack/context:** <framework, versions, key libs>
**Current state:**
- <deliverable>: ✅/⚠️/❌ <status detail>
**Your task:** <one scoped task>
**Acceptance criteria:** <observable outcomes, ≤5>
**Constraints:**
- <rule + reason>
**Do not:** <files/behaviors off-limits>
**Materials:** <paths/attachments only — no chat history>
```

### Developer Handoff
```markdown
# Dev Handoff: <feature>
**Run it:** <commands, env vars>
**What changed:** <files + one line each>
**Verified:** <what/how> | **Unverified:** <what/how to>
**Known gaps/hacks:** <the honest list>
**Next steps:** <ordered>
```

### Stakeholder Handoff
```markdown
# <Decision needed>
**Recommendation:** <one sentence>
**Why:** <3 bullets>
**Risks:** <2–3 bullets>
**Cost/effort:** <one line>
**If we do nothing:** <one line>
```
