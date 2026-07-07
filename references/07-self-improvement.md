# Helix Self-Improvement System

Helix improves itself through structured, evidence-based loops rather than vague "learn from experience."

## Core Loop (The Helix Meta-Loop)

1. **Detect opportunity** — From handoff, failed verification, eval score, user feedback, or scheduled research.
2. **Scope** — Pick one narrow area (a single reference, skill, script function, or mode rule).
3. **Baseline** — Run current version on representative cases. Capture evidence (scores, screenshots, outputs, failures).
4. **Research** — Use `helix_design_research.py` (or live analyzer) to find external patterns. Load `external-agent-patterns.md` and `ui-design-autonomy-repo-patterns.md` (or equivalent for the domain).
5. **Variant generation** — Produce 2–4 materially different improvements. Each declares what it changes and why.
6. **Tournament / Scoring** — Apply the relevant rubric (design-rubric-v2 for UI, or custom meta-rubric). Use `helix_design_tournament.py` style or `score_output.py`. Prefer real evidence (runs, screenshots, test results).
7. **Repair loop** — Patch the best variant, re-eval, repeat until gains plateau or evidence is strong.
8. **Lesson extraction** — Turn the delta into a durable lesson (see 05-memory-lessons.md).
9. **Commit** — Update the reference/skill/script in the canonical repo. Create handoff or PR.
10. **Verify** — Run `verify_install.py` + relevant tests. Only claim improvement with before/after evidence.

## When to Trigger Self-Improvement

- After a handoff that reveals a recurring weakness.
- When eval harness scores drop or plateau.
- Scheduled (e.g., weekly "Helix health check").
- When researching external improvements (new papers, better agent repos, UX psychology updates).
- When a new domain (e.g., the UX psychology addition) is added — immediately run a meta-pass on how it integrates with existing loops.

## Meta Rubric (for scoring Helix's own behavior)

Use or extend the design rubric when the target is UI-related. General dimensions:

- **Evidence strength**: Claims backed by concrete artifacts, runs, or citations.
- **Narrow scope**: Improvement targets one thing instead of everything.
- **Verification discipline**: Includes before/after + how to re-verify.
- **Portability**: Change works across Claude Code, Codex, Hermes (no hard-coded paths).
- **Lesson durability**: Results in a clean lesson file or reference update that prevents regression.
- **Anti-slop**: No generic "be more careful" language. Specific, actionable, testable.

Target: Measurable lift (e.g., +5 points on rubric, fewer verification failures, faster handoffs, better external pattern adoption).

## Tools for Self-Improvement

- `scripts/helix_eval.py` + `score_output.py` — quantitative scoring.
- `scripts/helix_self_improve.py` (this system's driver — see below).
- `scripts/helix_design_research.py` + `helix_live_design_analyzer.py` — external pattern intake.
- `scripts/helix_design_tournament.py` — variant comparison (generalize beyond UI).
- Critique mode + verifier subagents.
- `references/critique.md`, `verification.md`, `handoff.md`.
- Lessons directory (`lessons/<category>/`).

## Integration with Existing Systems

- **Mode router**: Add "meta" / "self-improve" mode (see 01-mode-router.md update).
- **After every handoff**: Run a lightweight self-critique pass on the handoff process itself.
- **Lesson system**: Every accepted improvement must produce or update at least one lesson file.
- **Portable by default**: All self-improvement rules and scripts must remain runnable in Claude Code, Codex, and Hermes. No Hermes-only paths in core logic.
- **GitHub as long-term memory**: Improvements are committed back to the repo. Tags mark stable versions.

## Anti-Patterns

- Vague "Helix should be better at X".
- Updating without before/after evidence.
- Broad refactors that touch many files without narrow testing.
- Treating every task output as a lesson (only durable patterns).
- Forgetting portability — changes must not break non-Hermes users.

## Example Self-Improvement Trigger

Handoff reveals that many UI tasks still start without loading `ux-psychology-principles.md`.

1. Scope: "Ensure psychology reference is loaded for all commitment flows".
2. Baseline: Run design tournament on 2 onboarding briefs without the reference.
3. Research: Pull recent onboarding examples via live analyzer.
4. Variant: Add explicit check in mode-router + design-masterclass + critique.skill.md.
5. Score: New variants show +12–18 on Commitment & Conversion dimension.
6. Update files + add lesson.
7. Re-run tournament as verification.

## Activation

Load this reference (`07-self-improvement.md`) together with `05-memory-lessons.md`, `06-eval-harness.md`, and `03-verifier-subagents.md`.

Run:
```bash
python scripts/helix_self_improve.py --area "mode-router" --brief "ensure UX psychology is loaded for onboarding flows"
```

The script (when implemented) will drive the loop above and produce an evidence-backed proposal.

Helix's goal is not to become a bigger prompt. It is to become a system that reliably diagnoses its own weaknesses and ships measurable upgrades to its own references, skills, and scripts.
