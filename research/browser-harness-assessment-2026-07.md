# Browser Harness Assessment for Helix UI Pro

Source reviewed: https://github.com/browser-use/browser-harness README on 2026-07-08.

## What it is
Browser Harness connects an LLM to a real Chrome/Chromium browser through CDP with a thin editable helper layer. The README emphasizes:
- one websocket to Chrome
- editable `agent_helpers.py`
- reusable `domain-skills/`
- browser tasks where the agent writes missing helpers during execution
- optional Browser Use Cloud browsers

## Why it helps Helix
Browser Harness is a strong fit for Helix Reference Scout and Screenshot Learning:
- browse Mobbin/Page Flows/reference sites with legitimate user access
- capture reference screenshots and source URLs
- create site-specific domain skills for repeated reference workflows
- inspect responsive states and browser behavior through the real browser
- gather before/after screenshots for repair loops

## Boundaries
- Not a replacement for Helix's behavior map, visual jury, or design memory.
- Must not bypass paywalls, auth, CAPTCHAs, or site terms.
- Mobbin/proprietary references should be distilled into abstract patterns, not copied.
- Browser Harness should be optional: Helix must still work with user-provided screenshots or public references.

## Recommended integration
Add Browser Harness as an optional Reference Scout backend:
1. Detect `browser-harness` command.
2. If available and user has authorized browser access, capture reference screenshots.
3. Save evidence under `design/helix-memory/reference-boards/`.
4. Distill to pattern cards using `references/20-reference-pattern-distillation.md`.
5. Feed patterns into `scripts/helix_ui_pro_loop.py` workspaces.

## Install note from README
The README suggests asking an agent:

```text
Install or upgrade browser-harness to the latest stable version with uv using Python 3.12, register the skill from `browser-harness skill`, and connect it to my browser. Follow https://github.com/browser-use/browser-harness/blob/main/install.md if setup or connection fails.
```

Use only after explicit user approval because it installs tooling and connects to a browser.
