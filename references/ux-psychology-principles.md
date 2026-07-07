# Helix UX Psychology Principles

Purpose: Make Helix design flows that actually convert by understanding how humans decide and commit.

These principles come from rigorous study (Cialdini, Kahneman, goal gradient research, endowment effect studies) and real top-product patterns (analyzed via resources like Mobbin). Helix must apply them, especially on onboarding, sign-up, upgrade, checkout, and any commitment screen.

**Core rule**: Never design a commitment screen by only making it pretty or clear. Design it to reduce psychological resistance and create momentum or obligation.

## The Six Principles

### 1. Smart Defaults (Reduce Decision Fatigue)
- Pre-fill every field with the statistically most common choice.
- The button should communicate that work is already done ("12 results waiting" instead of "Search").
- 70-90% of users never change defaults. Treat defaults as a strong recommendation.
- Helix action: In any form or setup screen, identify the most common real-world choice and pre-select it. Show the "already decided for you" signal.

### 2. Goal Gradient Effect (Never Start at Zero)
- People accelerate as they feel closer to completion.
- Never show 0% progress or an empty checklist at the beginning of onboarding.
- Give an artificial but honest head start: "Step 1 of 5 — already 20% complete" or pre-check the first item.
- LinkedIn example: profile strength meter starts above zero on signup.
- Helix action: For any multi-step flow, calculate and display progress that reflects work the user has conceptually already done (e.g., "You've already chosen your language" before account creation).

### 3. Reciprocity (Give Value Before Asking)
- Humans feel a powerful pull to return a favor.
- Do not ask for an account before the user has received something genuinely useful.
- Bad: "Enter email to see your report" (results blurred behind paywall).
- Good: Show a real (partial) report with score + top issues first. Then "Want the complete breakdown? Save your report."
- Free samples, 30-day trials, and partial useful output all work because of this.
- Helix action: In any gated flow, deliver a real, usable artifact (score, top 3 issues, preview) before the account wall.

### 4. IKEA / Endowment Effect (Let Them Build Before They Commit)
- People value what they have invested time or choices into.
- Let the user make meaningful choices (name, palette, card style, goal, first content) before the sign-up button appears.
- Change the final button from "Sign up" to "Continue" or "Create my X".
- Duolingo example: user picks language, sets goal, completes first lesson before account creation.
- Helix action: For onboarding or setup, move customization and first-value creation as early as possible. The account creation screen should feel like abandoning something the user has already started building.

### 5. Loss Aversion (Threat Beats Pitch)
- The pain of losing something is ~2× the pleasure of gaining the same thing (Kahneman).
- Never sell only what the user will gain. Show what they are about to lose.
- Bad: Clean "Upgrade now" with feature list + "Maybe later".
- Good: "Your files [actual names] will stop syncing in 3 days" + "I'll risk it" as the dismiss.
- Helix action: On upgrade or commitment screens, surface the user's actual current state (files, progress, data) and make the cost of inaction concrete and personal.

### 6. Contrast / Anchoring (Control the First Number)
- The brain does relative, not absolute, evaluation.
- Never show a price or cost in isolation.
- Show a larger anchor first (the $1900 laptop makes the $50 protection plan feel like 2.6%).
- Restaurants put the expensive steak on the menu to make the salmon look reasonable.
- Helix action: When showing pricing, upgrades, or any numeric ask, always present a relevant higher anchor immediately before (or in the same view) so the target number feels small by comparison.

## Additional Operating Rules for Helix

### Mobbin-First Research
Before designing any onboarding, upgrade, checkout, or high-stakes flow:
1. Load this reference.
2. Use web research tools to study real examples from top products (search Mobbin or equivalent for "onboarding", "upgrade modal", "checkout", "first run experience").
3. Extract concrete patterns: where they place value delivery, how they show progress, what they let users customize pre-signup, how they frame loss.
4. Never guess. Reference real screens.

### When to Apply These Principles
Apply strongly on any screen where the user must give something (email, payment, time, attention):
- Onboarding / first-run
- Sign up / account creation
- Upgrade / paywall
- Checkout
- "Save report" or "Unlock full results"
- Any multi-step wizard

Apply lightly or not at all on pure utility screens inside an already-committed session.

### Integration with Existing Helix Rules
- These principles sit **on top of** design-system-first, hierarchy, states, and verification.
- A beautiful screen that ignores reciprocity or starts at 0% progress fails the psychology audit.
- In variant tournaments and critique passes, explicitly score against these six principles (see updated rubric).

### Critique Prompts (internal)
When reviewing a flow:
- "Where is the first value delivered? Before or after the ask?"
- "Does the user feel they have already started building something?"
- "Is progress shown as already underway?"
- "Is the ask framed as protecting what the user already has?"
- "What anchor does the user see right before the price/commitment?"

## Evidence Standard
Any Helix-designed commitment flow must be able to answer:
- What value was given before the ask?
- What progress head-start was created?
- What did the user build or customize before committing?
- What concrete loss was made visible?
- What anchor was used before showing the target number?

If the answer is weak or missing on any, the design is incomplete.

This reference must be loaded for any onboarding, auth, or conversion-critical design work.
