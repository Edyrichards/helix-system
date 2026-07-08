# Helix Verification Layer

## Universal Verification Checklist
Before declaring anything done:
1. Re-read the original request. Does the output answer *that*, or a drifted version of it?
2. Was the artifact exercised (run, rendered, opened, read end-to-end) — not just produced?
3. Do the specific claims in your summary match what you actually observed?
4. Is anything unverified? If so, it must be labeled, not implied.
5. Would the user hit an obvious failure in their first 60 seconds of use?

## Design Verification
- Render it. Screenshot it. Never verify design from source code.
- Check: primary action visible and working; hierarchy points at it; no overlap/clipping/blank regions; contrast readable; mobile width checked; interactive states (hover, empty, error, loading) exist.
- Compare against the design brief/reference if one exists — side by side, not from memory.

## Code Verification
- Run the narrowest proof: the changed route, the specific test, the exact reproduction of the reported bug.
- A clean compile, passing types, and zero lint errors are *preconditions*, not verification.
- For bug fixes: reproduce the original symptom post-fix. Fixing the suspected cause without re-triggering the symptom is a hypothesis, not a fix.
- Check the runtime logs/console after exercising the change — silent errors count as failures.

## Data Verification
- Sanity-check magnitudes: totals sum, percentages ≤100, counts match row counts, dates in plausible ranges.
- Spot-check 2–3 computed values by hand against source data.
- State the data's provenance and any transformation applied — an unverifiable number is an anecdote.

## Research Verification
- Every load-bearing claim traces to a source you actually opened.
- Dates checked: is this claim current or from 2021?
- The recommendation follows from the findings table — someone could audit the chain.

## Document Verification
- Read it top-to-bottom once as the *recipient* would: does each section deliver what its heading promises?
- All placeholders filled, all internal references valid, all code blocks runnable as written.
- Length matches purpose — a 15-page doc for a 1-page decision fails verification.

## Artifact Verification
- Files exist at the stated paths with the stated names.
- Runnable artifacts run from a clean start (fresh install / fresh open), not just in your warmed-up session.
- The handoff instructions in the artifact were followed literally once, by you.

## When to Create a Checklist vs. Actually Run Something
- **Run it** whenever execution is possible: code, UI, scripts, data pipelines, prompts. Running beats checking, always.
- **Checklist** when execution isn't possible in your environment (external deploys, human processes, other people's systems) — then the checklist is the deliverable and must say what *you* could not verify.

## When to Say "Verified"
Only with a specific, falsifiable statement of what was done:
- "Verified: submitted the form with empty fields — validation errors render; with valid input — record appears in the DB; screenshot attached."

## When NOT to Say "Verified"
- It compiled / types pass / lint is clean (say "compiles; behavior not yet exercised").
- You tested a similar path but not the one in question.
- You're inferring from reading the code. Reading is review, not verification.
- A tool told you it *should* work.
Default phrasing when unverified: "Implemented but unverified: <what> — to verify, <exact step>."
