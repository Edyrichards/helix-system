# Helix System Agent v2

**Helix** is a portable execution-first agent harness (successor to Fable).

It works across tools: **Claude Code / Cursor**, **Codex**, **Hermes**, and other capable agents.

**GitHub:** https://github.com/Edyrichards/helix-system

See [INSTALL.md](./INSTALL.md) for Claude Code, Codex, and portable setup.

It routes tasks through modes (code, design, research, product), verifier subagents, evidence ledgers, project bootstrap, eval harness, and lesson memory.

## Quick Start (Hermes only)

```bash
# Via Hermes CLI
hermes -s helix-system

# Or in chat
/skill helix-system
```

Aliases still accepted: `helix`, `helix-system`, `helix-agent`.

## Key Capabilities

- **Design-system-first UI/UX work** — starts with tokens + DESIGN.md before screens.
- **UI Autonomy Research & Tournaments**:
  - `scripts/helix_design_research.py` — ranks GitHub repos for screenshot-to-code, Figma MCP, design systems, visual verification.
  - `scripts/helix_design_tournament.py` — runs variant tournaments with **real browser screenshots** (Playwright):
    - Desktop + mobile renders
    - Console error capture
    - Horizontal overflow detection
    - Evidence-backed scoring + contact sheets with embedded images
- Full eval harness (`helix_eval.py`, `score_output.py`)
- Project bootstrap, handoff protocols, and clean-room external pattern references.
- Strong verification discipline (evidence ledger before claiming completion).

## Directory Structure

- `references/` — progressive operating rules (loaded on demand)
- `scripts/` — automation (research, tournaments, init, eval, verify)
- `evals/` — design tournaments with real screenshots
- `research/` — GitHub repo analysis for autonomy patterns
- `tests/` — verification for the harness itself
- `agent.md` / `SKILL.md` — skill definition (also mirrored to `~/.hermes/skills/helix-system/`)
- `handoff.md` — latest session handoff

## Publishing / Portable Use

This repo is the canonical source for Helix.

When using Helix in other projects:
- Copy relevant skills into the target repo's `.claude/skills/` or Hermes skill dir.
- Use `scripts/helix_init.py` to bootstrap a new project with Helix conventions.

See `helix-packaging-plan.md` and `references/` for more.

## Development

Run the harness self-tests:

```bash
python3 tests/run_design_autonomy_tests.py
python3 scripts/verify_install.py
```

## License

Proprietary (internal Hermes + Edy Richardson).  
Contact for usage outside personal Hermes setups.

## Self-Improvement

Helix ships with a full meta-loop (07-self-improvement.md + helix_self_improve.py). It can diagnose weaknesses in its own references, skills, and scripts, research external patterns, run tournaments on proposed changes, extract lessons, and produce evidence-backed patches.

## Status

Actively evolving toward full Claude Design-class autonomy (intake → DNA → variants → browser-verified render → repair → handoff).

Latest upgrades include real Playwright visual proof in the design tournament harness.
