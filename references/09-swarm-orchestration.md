# Helix Swarm Orchestration

**Goal**: Helix can decompose complex work into parallel specialist tasks, dispatch them, verify across agents, aggregate evidence, and synthesize a superior result. Swarms are not just "multiple prompts" — they are coordinated execution with full Helix discipline on every branch.

Always start with `08-intake-sufficiency-prompt-restructuring.md`.

## Core Swarm Roles (Helix Native)

**Coordinator** (the orchestrator)
- Performs main intake.
- Decomposes goal into 3-7 independent or loosely-coupled sub-tasks.
- Assigns each to the best specialist (existing or dynamically created).
- Tracks dependencies and parallel execution windows.
- Collects evidence from all workers.
- Runs or commissions cross-verification (jury).
- Synthesizes final artifact + unified evidence ledger.
- Extracts lessons for the swarm itself.

**Specialist Workers** (parallel executors)
- Each receives a scoped sub-brief + full relevant Helix context.
- Runs the complete Helix loop on its slice: intake → mode → execute → evidence → verification.
- Produces self-contained output + evidence package.
- Can be "Helix-Code-Reviewer", "Helix-Design-Specialist", "Helix-Research-Synthesizer", "Helix-Prompt-Architect", or ad-hoc generated personas.

**Jury Verifiers** (cross-check layer)
- Reuse and extend `03-verifier-subagents.md`.
- Multiple verifiers run in parallel on the same or related artifacts (code verifier + UI verifier + research verifier).
- Coordinator resolves conflicts using evidence, not votes.
- Parent (Coordinator) always re-verifies side effects.

**Synthesizer / Final Verifier**
- Takes all worker outputs + jury findings.
- Produces the unified deliverable.
- Updates lessons/ and self-improvement signals if the swarm ran in Meta mode.

## Swarm Protocol (Mandatory Sequence)

1. **Intake & Decomposition** (Coordinator)
   - Run full sufficiency check on the top-level goal.
   - Decompose only after sufficiency is confirmed.
   - Explicitly list: sub-task, specialist type, inputs needed, success criteria, verification method.

2. **Parallel Dispatch**
   - Issue independent briefs to specialists.
   - Specialists may run in true parallel (host tool support) or simulated parallel (separate reasoning traces + tool calls).
   - Each specialist must log its own evidence ledger slice.

3. **Worker Execution**
   - Every worker applies the full Helix operating contract (intake on its brief, gather ground truth, artifact + verification, evidence).
   - Workers surface assumptions and gaps immediately.

4. **Jury Phase** (parallel where possible)
   - Apply relevant verifiers from `03-verifier-subagents.md` plus swarm-specific cross-checks (consistency across workers, no conflicting assumptions, coverage of original goal).
   - Produce per-artifact PASS/FAIL + fixes.

5. **Aggregation & Synthesis** (Coordinator)
   - Merge artifacts.
   - Resolve conflicts with evidence.
   - Produce master evidence ledger.
   - Run final verification against original goal.
   - Deliver outcome-first + artifacts + one next step.

6. **Swarm Reflection** (optional but recommended)
   - What worked in the decomposition?
   - Which specialists were effective?
   - Update or generate improved persona definitions.
   - Log to lessons/swarm/ and feed self-improvement.

## Dynamic Swarm Creation (Helix Strength)

Helix can create new specialists on demand:
- Use research + `helix_design_research.py` or live analyzer patterns.
- Generate a new persona definition that inherits Helix rules (intake, evidence, verifiers).
- Test the new specialist in a mini-tournament or self-improvement cycle before using in production swarms.
- Store generated personas in `personas/` with version and evidence of creation.

## Portable Implementation Notes

- **Claude Code / Cursor / etc.**: The Coordinator issues multiple parallel tool calls or separate "think in this branch" instructions. Each branch follows its own Helix loop.
- **Scripts**: `scripts/helix_swarm.py` can automate decomposition, generate briefs, and (where possible) orchestrate local parallel execution.
- **Hermes**: Leverage any delegation or background tools; fall back to structured multi-turn with clear handoff briefs.
- Always produce machine-readable evidence (JSON manifests + human summary) so swarms compose.

## Anti-Slop Rules for Swarms

- Never run specialists without prior intake on the sub-task.
- Never trust a worker's self-report for side effects — re-verify.
- No specialist may skip verification gates.
- Coordinator must surface and resolve contradictions with explicit evidence.
- Every swarm run produces a lessons entry.

See also: `03-verifier-subagents.md`, `08-intake-...`, `07-self-improvement.md`, `02-evidence-ledger.md`, personas/ directory.
