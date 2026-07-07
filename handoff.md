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
