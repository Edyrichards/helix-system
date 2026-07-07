# Helix Design Layer Test Prompts

Use these prompts to compare Claude before and after installing the Helix Design Layer.

## 1. Landing page

Prompt:

> Design a landing page for a bookkeeping app for solo founders.

Expected behavior:

- Trust-forward hero
- Real product UI moment
- Specific copy
- Clear CTA
- No generic purple gradient
- No emoji feature cards

Fails if:

- It creates a centered hero with badge-pill and vague “AI-powered” feature cards.

---

## 2. Dashboard improvement

Prompt:

> Make this dashboard look better. Keep the brand.

Expected behavior:

- Preserves brand tokens
- Fixes hierarchy and spacing first
- Gives exact values/classes
- Does not rebrand colors or fonts

Fails if:

- It changes the visual identity instead of improving structure.

---

## 3. Signup critique

Prompt:

> Critique this signup page screenshot and tell me exactly what to change.

Expected behavior:

- Names the screen’s job
- Critiques in order: hierarchy, layout, spacing, type, color, states, copy
- Leads with two highest-impact fixes
- Gives exact implementation instructions

Fails if:

- It says “make it cleaner” or “improve hierarchy” without specifics.

---

## 4. Pricing page

Prompt:

> Design a pricing page that converts without feeling pushy.

Expected behavior:

- Clear tier structure
- Honest “most popular” guidance if needed
- Transparent pricing
- One CTA logic
- No fake urgency

Fails if:

- It uses countdown timers, hidden pricing, or pre-checked add-ons.

---

## 5. Settings page

Prompt:

> Build a settings page for a productivity app.

Expected behavior:

- Minimal layout
- Type hierarchy and dividers
- Clear grouping
- Outcome-named actions
- No heavy card around every row

Fails if:

- Every setting becomes a large card with an icon and shadow.

---

## 6. Orders table

Prompt:

> Add a data table for ecommerce orders.

Expected behavior:

- Dense, scannable table
- Muted headers
- Tabular numbers
- Empty/loading/error states
- Useful row actions

Fails if:

- It uses airy marketing spacing or spinner-only loading.

---

## 7. Delight

Prompt:

> Make this app feel more delightful.

Expected behavior:

- One signature emotional moment
- Calm interface elsewhere
- Motion tied to state change

Fails if:

- It adds confetti, bouncing cards, and constant animations everywhere.

---

## 8. Mobile checkout

Prompt:

> Design a mobile checkout flow.

Expected behavior:

- Single-column flow
- Collapsed order summary
- Sticky pay button
- 44px touch targets
- Clear error and success states

Fails if:

- It shrinks a desktop layout into mobile.

---

## 9. Brand color homepage

Prompt:

> Here is our brand color: #0D6E4F. Build the homepage.

Expected behavior:

- Builds a constrained token system around the color
- Uses accent sparingly
- Does not introduce competing accents
- Uses product-specific imagery/copy

Fails if:

- It adds multiple random colors and generic SaaS sections.

---

## 10. Empty state

Prompt:

> Write the empty state for a new user’s projects page.

Expected behavior:

- One orientation line
- One short explanation
- One first-action CTA
- Human tone

Fails if:

- It says “No data available.”

---

## Scoring

Score each response out of 5:

1. Did it identify the screen/job?
2. Is hierarchy clear with one loudest element?
3. Did it hold constraints around color, type, spacing, and layout?
4. Did it handle states and copy properly?
5. Did it provide verification or implementation-ready details?

Total possible score across 10 prompts: 50.
