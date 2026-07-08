# Helix Reference Scouting

Purpose: prevent blind UI changes. Before substantial UI/UX generation or redesign, Helix must gather and distill proven references from real products and design libraries.

## Mandatory trigger
Load this module for:
- landing page redesigns
- onboarding, checkout, signup, pricing, dashboards, or app shells
- any request to make UI "better", "premium", "high-converting", "Mobbin-like", or "best in class"

## Rule
Do not copy reference screens. Extract transferable patterns and adapt them to the product truth, brand tokens, information architecture, and user behavior map.

## Source hierarchy
Use accessible, legitimate sources only:
1. User-provided screenshots, Figma exports, design zips, or URLs.
2. The app's own design system and screenshots.
3. Mobbin / Page Flows / Screenlane / SaaSFrame / Refero / Land-book / Godly / official design systems when the user has access.
4. Public app store screenshots, product tours, marketing pages, docs, and open-source examples.

## Safety and licensing
- Use Mobbin and paid reference tools only through the user's legitimate access.
- Do not bypass paywalls, CAPTCHAs, auth, or usage limits.
- Do not reproduce exact layouts, copy, brand assets, iconography, or proprietary screens.
- Store citations and abstract lessons, not cloned assets, unless the user provided owned assets.

## Reference board schema
Every reference board should include:
- project, surface, target user, behavior goal
- source name, URL/path, app/product, screen/flow
- screenshot path if captured
- useful pattern
- behavior/psychology mechanism
- adaptation for this product
- do-not-copy notes
- confidence and evidence

Use `schemas/reference-board.schema.json`.

## Mobbin-specific extraction prompts
For each Mobbin/proven app screen, answer:
1. What user belief/action does this screen support?
2. What is the first visual object the user understands?
3. Where is risk reduced before commitment?
4. What is the CTA timing and commitment size?
5. How are numbers, proof, and state represented?
6. What mobile pattern is reusable?
7. What must not be copied?

## Output artifacts
Recommended project-local outputs:
```text
design/helix-memory/reference-board.json
design/helix-memory/reference-contact-sheet.html
design/helix-memory/reference-lessons.md
```

## Browser Harness integration
Browser Harness can be used for reference scouting when installed and authorized:
- connect to the user's real browser via CDP
- capture reference screenshots
- create site/domain skills for repeated navigation
- preserve source URLs and screenshots as evidence

Do not make Browser Harness mandatory. Fall back to user-provided screenshots, public URLs, or manual reference notes when unavailable.
