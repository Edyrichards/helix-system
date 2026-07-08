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

## Verdict language
- `Verified:` only when screenshots/checks were actually produced.
- `Implemented, unverified:` when code exists but browser evidence is missing.
