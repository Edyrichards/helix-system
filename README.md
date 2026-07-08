# Helix System Agent v2

**Helix** is a portable execution-first agent harness .

It works across tools: **Claude Code / Cursor**, **Codex**, **Hermes**, and other capable agents.

**GitHub:** https://github.com/Edyrichards/helix-system

See [QUICKSTART_CLAUDE.md](./QUICKSTART_CLAUDE.md) for the fastest way to use it in Claude Code / Cursor.
See [INSTALL.md](./INSTALL.md) for full details and other tools.

One-command project install:
```bash
scripts/install_helix.sh /path/to/project
```

It routes tasks through modes (code, design, research, product, GTM), verifier subagents, evidence ledgers, project bootstrap, eval harness, lesson memory, reprompting, and specialist swarms.

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


## Swarm Orchestration & Specialists
Helix can now run true agent swarms:
- `references/09-swarm-orchestration.md` — full protocol
- `personas/` — Helix-native specialists (Swarm Coordinator, Code Reviewer, Design Specialist, Research Synthesizer)
- `scripts/helix_swarm.py` — decomposition helper and prompt generator
- Each specialist runs the complete Helix loop (intake → execute → evidence → verification)
- Coordinator aggregates with jury verification
- Helix can dynamically create new personas

This gives you both the "who" (specialists with personality and process) and the "how" (rigorous execution, verification, and self-improvement).


## Why Helix Wins

Helix is being built as the agent OS that could sit underneath Hermes, Claude Code, Cursor, Codex, or any serious AI coding/design workflow.

Its wedge is:
- **Reprompting**: rough user intent becomes a professional execution brief.
- **Design reasoning**: every UI decision traces to user psychology, product job, hierarchy, and evidence.
- **Design psychology**: ethical conversion/onboarding science, not generic persuasion tricks.
- **Verified output**: screenshots, console checks, overflow checks, evidence ledgers.
- **Specialist swarms**: Prompt Architect + Research + Conversion Psychologist + Design Specialist + Jury.
- **Self-improvement**: lessons and meta-loops upgrade Helix itself.

Key files:
- `references/10-design-reasoning-engine.md`
- `references/11-advanced-design-psychology.md`
- `references/12-prompt-reprompt-engine.md`
- `PERSONA_CATALOG.md`
- `GO_TO_MARKET.md`
- `research/agency-agents-dissection-2026-07.md`


## Examples

- `examples/reprompt-onboarding.md` — how Helix turns vague input into a professional design brief.
- `examples/design-swarm-checkout.md` — best-in-class design swarm recipe with psychology + verification.


## Productized Distribution Layer

Helix now includes app-ready manifests and generated integration scaffolding inspired by the clean-room agency-agents dissection:

- `catalog/tools.json` — supported hosts and install formats.
- `catalog/modules.json` — portable modules and load policies.
- `catalog/personas.json` — persona roster for lazy routers/catalog UIs.
- `runbooks/runbooks.json` — machine-readable activation recipes.
- `scripts/check_catalog.py` — drift/broken-reference validation.
- `scripts/helix_convert.py` — generated adapters under `integrations/<tool>/`.

```bash
python3 scripts/check_catalog.py
python3 scripts/helix_convert.py --tool all
```
