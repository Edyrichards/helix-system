# Helix Test Suite

Compare a baseline model vs. a Helix-layered model. Run each test with identical prompts and materials. Score each criterion 0–2 (0 absent, 1 partial, 2 full). Write criteria expectations *before* viewing outputs; randomize A/B labels.

---

## Test 1: UI Design from Scratch
**Prompt:** "Build a landing page for a bookkeeping app for freelance photographers."
- **Weak model:** generic hero + 3 feature cards + testimonials; purple gradient; stock copy ("Streamline your workflow"); 6+ colors; never renders it.
- **Helix model:** persona-specific copy (shoots, invoices, tax season); disciplined 3–5 color palette with tokens; one memorable element; mobile-first; renders + screenshots + self-critiques before delivering.
- **Score:** persona-specific content (0–2), palette/typography discipline (0–2), distinctive element (0–2), rendered & verified (0–2), semantic/accessible markup (0–2). /10

## Test 2: UI Critique from Screenshot
**Prompt:** "Critique this signup screen." + screenshot.
- **Weak:** 20 equal-weight observations, half praise, fixes like "improve spacing."
- **Helix:** states the screen's goal; ≤3 ranked critical issues each with exact fix values; ends with one paste-ready build instruction.
- **Score:** goal stated (0–2), ranked ≤3 criticals (0–2), fixes are specific values (0–2), next build instruction (0–2), no filler praise (0–2). /10

## Test 3: HTML Prototype Creation
**Prompt:** "Make me a clickable prototype of a recipe-scaling tool."
- **Weak:** static mockup, non-functional buttons, lorem ipsum.
- **Helix:** single-file working HTML with real scaling logic, realistic data, states (empty/edited), opens and works immediately.
- **Score:** actually functional (0–2), realistic data (0–2), interaction states (0–2), single-file portability (0–2), visual quality (0–2). /10

## Test 4: React/Tailwind Conversion
**Prompt:** "Convert this HTML prototype to React + Tailwind." + file.
- **Weak:** one giant component, inline styles half-converted, visual drift unchecked.
- **Helix:** sensible component split, tokens over raw colors, repeated markup → mapped data, renders both versions and confirms visual parity, notes any 1:1 impossibilities.
- **Score:** component boundaries (0–2), token usage (0–2), data extraction (0–2), visual parity verified (0–2), TypeScript/a11y (0–2). /10

## Test 5: Repo Debugging
**Prompt:** "The cart total is wrong after applying a coupon — fix it." + repo.
- **Weak:** edits the first plausible file, adds a try/catch, claims fixed without reproducing.
- **Helix:** reproduces the bug first, states a hypothesis, traces to root cause with reads/logs, minimal fix, re-runs the reproduction to confirm, no unrelated changes.
- **Score:** reproduced before fixing (0–2), root cause identified (0–2), minimal diff (0–2), reproduction re-run post-fix (0–2), no scope creep (0–2). /10

## Test 6: Product Strategy
**Prompt:** "I want to build an app for dog owners. What should I build?"
- **Weak:** feature list of 15 ideas ("profiles, GPS, social feed, marketplace..."), no user, no loop.
- **Helix:** narrows to one persona + JTBD, defines the core loop, picks a wedge, MVP = smallest complete loop, explicit not-doing list, one page.
- **Score:** specific persona (0–2), loop defined & closed (0–2), wedge justified (0–2), MVP is a complete loop (0–2), not-doing list (0–2). /10

## Test 7: Competitor Research
**Prompt:** "Research competitors before we design onboarding for a budgeting app."
- **Weak:** paragraphs summarizing each competitor's whole product, market-size filler, no recommendation.
- **Helix:** 3–4 relevant competitors in a table scoped to onboarding, patterns vs. gaps lists, cited claims from opened pages, one-paragraph recommendation.
- **Score:** decision-scoped (0–2), comparison table (0–2), patterns/gaps split (0–2), real citations (0–2), actionable recommendation (0–2). /10

## Test 8: Writing Rewrite
**Prompt:** "Rewrite this product announcement to be stronger." + draft.
- **Weak:** synonym-swaps, longer output, keeps the buried lede.
- **Helix:** leads with the user benefit, cuts ≥25%, one claim per section, quotes what it cut and why in 2 lines.
- **Score:** lede fixed (0–2), meaningful cuts (0–2), concrete claims replace vague ones (0–2), voice preserved (0–2), rationale given briefly (0–2). /10

## Test 9: Data Analysis
**Prompt:** "What does this sales CSV tell us? What should we do?" + file.
- **Weak:** restates column stats, a chart nobody asked for, no decision.
- **Helix:** sanity-checks the data first (nulls, ranges, sums), surfaces 2–3 findings with magnitudes spot-checked, ends with recommended actions tied to findings, states data limitations.
- **Score:** data sanity-checked (0–2), findings quantified & spot-checked (0–2), actions tied to findings (0–2), limitations stated (0–2), no stat-dump filler (0–2). /10

## Test 10: Handoff Creation
**Prompt:** "Summarize this project so another AI can continue tomorrow." + long working session.
- **Weak:** chronological recap of the conversation, missing verification status, "we discussed several approaches."
- **Helix:** goal / current state with ✅⚠️❌ labels / one scoped next task with acceptance criteria / constraints with reasons / only needed materials. No chat archaeology required.
- **Score:** decision-based compression (0–2), verification labels (0–2), scoped next task with criteria (0–2), constraints with reasons (0–2), noise removed (0–2). /10

---

## Scoring & Interpretation
- Total per test: /10. Suite total: /100.
- **Signs a model is only sounding good:** confident prose with no specific values; features/findings that can't be traced to the ask; "verified" without a stated verification action; praise and hedging padding; identical structure regardless of task.
- A Helix-layered model should beat baseline most on Tests 2, 5, 6, 10 (prioritization, verification, and compression are where generic models fail hardest).
