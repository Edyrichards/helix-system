# Handoff: Helix UI/UX Autonomy Upgrade

## Goal
Scale Helix toward a Claude Design-class autonomous UI/UX generation system by turning GitHub research into reusable Helix runtime references, scripts, and a verifiable variant-tournament harness.

## Current State
- Helix has a new UI autonomy research/reference layer.
- Helix can rank GitHub repos from live `gh` search or existing JSON evidence.
- Helix can score UI variants and generate a local contact-sheet artifact for comparison.
- The install verifier now requires the new autonomy artifacts.
- Tests exist for the two new scripts and verifier wiring.

## Active Files
- `SKILL.md`
- `agent.md`
- `references/ui-design-autonomy-repo-patterns.md`
- `research/ui-agent-repo-research-2026-07-08.md`
- `research/helix-ui-repos-ranked-20260708-004741.md`
- `scripts/helix_design_research.py`
- `scripts/helix_design_tournament.py`
- `scripts/verify_install.py`
- `tests/run_design_autonomy_tests.py`
- `tests/test_helix_design_autonomy.py`
- `evals/design-tournaments/sample-helix-ui-variants.json`
- `evals/design-tournaments/20260708-004704/contact-sheet.html`
- `evals/design-tournaments/20260708-004704/manifest.json`

## Changes Made
- Added `scripts/helix_design_research.py`:
  - ranks GitHub repos by Helix UI autonomy relevance;
  - supports live `gh` collection and `--from-json` offline mode;
  - outputs Markdown and JSON reports.
- Upgraded `scripts/helix_design_tournament.py` to **real browser visual verification** (Playwright):
  - Self-contained HTML per variant.
  - Desktop (1280×800) + mobile (390×844) screenshots via headless Chromium.
  - Console error capture + horizontal overflow JS check.
  - Score bonuses for visual_verified, clean console, no overflow.
  - `contact-sheet.html` now embeds the real PNG screenshots.
  - `--no-browser` flag for fast heuristic mode.
- Updated tests + sample variants.
- Playwright installed.
- SKILL.md / agent.md / handoff updated with browser commands.
- Added tests in `tests/run_design_autonomy_tests.py` and pytest-style companion file.
- Patched `scripts/verify_install.py` to require the new autonomy scripts and reference.
- Copied new scripts into both canonical agent and runtime skill directories.
- Updated `SKILL.md` and `agent.md` with UI autonomy research and tournament commands.
- Regenerated `MANIFEST.sha256`.

## Failed Attempts
- `python3 -m pytest tests/test_helix_design_autonomy.py -q` failed because pytest is not installed in the active Hermes venv.
- Replaced the verification path with a dependency-free custom runner: `python3 tests/run_design_autonomy_tests.py`.
- Initial repo scoring over-ranked a GPL system-prompt repository; scoring was patched to strongly penalize prompt-leak/system-prompt repos and GPL/Affero licenses for direct study.

## Next steps
1. Clone and inspect Tier 1 repos into a scratch directory, starting with:
   - `abi/screenshot-to-code`
   - `wandb/openui`
   - `grab/cursor-talk-to-figma-mcp`
   - `Jpisnice/shadcn-ui-mcp-server`
   - `storybookjs/storybook`
   - `microsoft/playwright-mcp`
2. Extend `helix_design_tournament.py` from heuristic scoring to browser-backed proof:
   - local HTTP server;
   - desktop/mobile screenshots;
   - console error capture;
   - horizontal overflow metrics;
   - contact sheet with screenshots.
3. Add a project-level design memory format for Design DNA, winning variants, rejected patterns, screenshots, and component decisions.
4. Add optional MCP setup docs for Figma, shadcn, Magic UI, 21st.dev, Storybook, and Playwright.
5. Add a multi-agent design jury protocol: visual critic, accessibility critic, conversion critic, code critic, and brand critic.

## Verification
- `python3 tests/run_design_autonomy_tests.py` passed.
- `python3 -m py_compile scripts/*.py tests/run_design_autonomy_tests.py` passed.
- `python3 scripts/verify_install.py` passed.
- Offline research command produced `research/helix-ui-repos-ranked-20260708-004741.md`.
- Sample tournament command produced `evals/design-tournaments/20260708-004704/manifest.json` with winner `Helix Design Operating Loop` scoring `59` vs `Static Prompt UI` scoring `6`.

## Latest verification (browser upgrade)
- `python3 tests/run_design_autonomy_tests.py` → all PASS (including browser path)
- Real tournament run:
  - Output: `evals/design-tournaments/20260708-015907/`
  - `visual_mode: browser`
  - Winner: "Helix Design Operating Loop" score **103**
  - Real files generated:
    - `02-helix-design-operating-loop-desktop.png` (37KB)
    - `02-helix-design-operating-loop-mobile.png` (35KB)
    - Same for baseline variant
    - `contact-sheet.html` (embeds the screenshots)
    - `manifest.json` with full visual_evidence
- No console errors captured.
- Horizontal overflow check executed.

## Next steps (still open)
- Extend to support real component libraries (React + Tailwind live preview).
- Add interaction smoke tests (click primary buttons).
- Integrate with project design memory (store DNA + winning screenshots).
- Wire into full Helix design mode as a first-class step.
- Optional: add visual diffing against baseline or Figma exports.

## GitHub Publication
- Repo created and pushed: https://github.com/Edyrichards/helix-system
- Initial commit: c1df2c9 (all current harness files + browser visual verification work)
- Tag: v2.0.0
- Visibility: PUBLIC
- README enhanced with quick start and capabilities

The canonical source is now on GitHub. Future changes should be developed here and pushed.

## UX Psychology + Web Research Upgrade (current session)
- Created `references/ux-psychology-principles.md` — distilled 6 principles from high-signal UX psychology video (smart defaults, goal gradient, reciprocity, endowment/IKEA, loss aversion, anchoring) + Mobbin research mandate.
- Updated `design-rubric-v2.md` — added "UX Psychology" and "Commitment & Conversion" dimensions (now 12 dimensions / 60 pts total). Psychology is mandatory for commitment flows.
- Updated `design-masterclass.md` and `design-system-first.md` to require loading the psychology reference for onboarding/sign-up/upgrade flows.
- Added `scripts/helix_live_design_analyzer.py` — new web capability using Playwright:
  - Visits real URLs (e.g. competitor onboarding flows).
  - Captures desktop + mobile screenshots.
  - Extracts heuristic signals for the 6 principles.
  - Produces `live_analysis.json` ready for deeper critique.
- Updated `references/ui-design-autonomy-repo-patterns.md` with "Live Web Research for UX Psychology" section (explicitly calls out Mobbin + browser-use style research).
- Updated SKILL.md with usage for the new analyzer.
- Goal: Helix no longer guesses good onboarding — it studies real top-team patterns via web and applies proven psychology.

This directly addresses the user's real motivation: "If you want to get better at designing onboarding that actually works, Mobbin is genuinely the best resource" + "make helix use web".

## Portability Upgrade
- Added comprehensive INSTALL.md covering Claude Code/Cursor, Codex, Hermes, and standalone use.
- Created references/portable-github-publishing.md (was referenced but missing).
- Reworked README to position Helix as multi-tool portable first.
- Added portability clarifications to agent.md.
- The key portable bootstrap remains `scripts/helix_init.py --write` which generates environment-agnostic CLAUDE.md files.
- New UX psychology rules and live web analyzer are included in the portable core.

Users can now install Helix into Claude Code projects, Codex agents, etc. by cloning the GitHub repo and following INSTALL.md. Hermes is just one supported runtime.

## Self-Improvement Capability Added
- Created `references/07-self-improvement.md` defining the full meta-loop (detect, scope, baseline, research, variants, tournament/score, repair, lesson extraction, commit with evidence).
- Added "Meta / Self-Improve" mode to the router.
- Implemented `scripts/helix_self_improve.py` — a portable driver script that runs the loop and produces artifacts (baseline, variants, proposal, lesson file).
- First example run executed successfully on "mode-router" area for UX psychology loading.
- Updated INSTALL.md, README, and agent.md.
- All self-improvement artifacts are portable and evidence-driven (evals/self-improvement/ + lessons/).
- Helix can now systematically upgrade its own references, skills, and behavior across Claude Code, Codex, and Hermes.


## Intake, Sufficiency Check & Sophisticated Internal Prompt Restructuring
- Added `references/08-intake-sufficiency-prompt-restructuring.md` as the mandatory first step (Step 0) before any mode or execution.
- Process: Listen/parse → Sufficiency checklist (anti-hallucination) → Ask targeted questions if gaps → Internally restructure using advanced PE (decomp, CoVe, ToT internally, role elevation, XML scaffolding, few-shot from lessons, natural distillation).
- Integrated into:
  - `00-operating-contract.md` (as explicit Step 0)
  - `helix-execution-layer.md`
  - `master-claude-project-instructions.md`
  - `01-mode-router.md` (pre-step)
  - `07-self-improvement.md` (as high-leverage improvement area)
  - `agent.md` and `INSTALL.md`
- The restructuring is always internal/silent. Output remains natural and follows the contract.
- This directly addresses the request for listening first, checking sufficiency to avoid hallucination, asking more questions when needed, and using sophisticated prompt engineering internally.


## Swarm & Multi-Agent Jury (2026-07)
- Added `references/09-swarm-orchestration.md`
- Added `personas/` directory with core Helix specialists (Swarm Coordinator, Code Reviewer, Design Specialist, Research Synthesizer)
- These are original, not cloned — they deeply integrate intake, evidence ledger, verifier subagents, and self-improvement.
- `scripts/helix_swarm.py` helps with decomposition and prompt generation.
- The multi-agent design jury idea is now realized as the Swarm + Jury pattern.
