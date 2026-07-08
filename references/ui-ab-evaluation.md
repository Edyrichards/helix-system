# UI A/B Evaluation

Compare two UI outputs under identical prompt/context.

## Protocol
1. Preserve raw prompt and assumptions.
2. Render variant A and B in desktop and mobile.
3. Capture screenshots, console errors, overflow status.
4. Score both with `design-rubric-v2.md`.
5. Declare a winner only if improvement exceeds the winner rule or fixes a critical failure.

Do not compare a polished implementation against an unrendered sketch.
