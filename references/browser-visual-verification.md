# Browser Visual Verification

Use this for substantial UI/design work. Render the artifact in a browser and collect evidence before claiming design quality.

## Required checks
- Desktop screenshot: default 1280x800.
- Mobile screenshot: default 390x844.
- Console errors captured.
- Horizontal overflow check.
- CTA visibility and contrast checked.
- Empty/loading/error/focus states checked when relevant.

## Preferred implementation
Use Playwright with `file://` for generated static artifacts or the project dev server for real apps. Store outputs under `evals/design-tournaments/<timestamp>/` or an example-specific evidence folder.

`helix_design_tournament.py` now supports two browser renderers:
- Python Playwright when `playwright.sync_api` is installed in the active Python runtime.
- Node Playwright fallback when Python Playwright is unavailable but the tournament output lives inside a project tree with Playwright in `node_modules`.

The Node fallback writes a small temporary `.mjs` renderer beside the tournament artifacts so Node's normal module resolution can find the project dependency. It captures the same evidence shape: desktop/mobile screenshots, console warnings/errors, horizontal overflow, renderer name, and `visual_verified`.

## Verdict language
- `Verified:` only when screenshots/checks were actually produced.
- `Implemented, unverified:` when code exists but browser evidence is missing.
