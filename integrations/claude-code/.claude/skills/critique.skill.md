# Helix Critique Layer

## Critique Principles
1. **Ranked, not exhaustive.** Max 3 critical issues. A critique's value is its ordering, not its coverage.
2. **Every issue ships with its fix.** "The hierarchy is weak" is a complaint; "make the price 2× the label size and demote the metadata to muted 14px" is a critique.
3. **Judge against the goal, not against taste.** State the goal first ("this screen must get users to start a trial"), then measure everything against it.
4. **No praise padding.** One line of what's working (so it isn't broken by the fixes), then the problems.
5. **End with the next build instruction** — critique that doesn't change the next version was entertainment.

## How to Critique Design
Check in this order (stop-ship items first): (1) Can the user complete the primary action? (2) Is the visual hierarchy pointing at that action? (3) Contrast/readability/touch targets. (4) Consistency with the design system. (5) Distinctiveness — does it look like every template?
Always critique from the rendered artifact (screenshot), never from the code alone.

## How to Critique Code
Order: (1) Correctness — does it do what's claimed, including edge cases? (2) Security — injection, auth, data exposure. (3) Fit — does it follow the codebase's existing patterns or invent parallel ones? (4) Scope — did it change things it shouldn't have? (5) Readability. Style nits go in one collapsed line or nowhere. Quote the exact lines you're criticizing.

## How to Critique Product Strategy
Attack the load-bearing assumptions in order: Is the user real and specific? Does the loop actually close? Is the wedge defensible or just "we'll be better"? Does the MVP complete the loop? A strategy with a beautiful roadmap and a broken loop fails the critique regardless of polish.

## How to Critique Writing
(1) Does the first paragraph earn the rest? (2) Is there one claim per section, or mush? (3) Cut test: what survives deleting 30%? (4) Is anything generic enough to appear in a competitor's doc unchanged? Quote the weakest sentences; rewrite one as a demonstration.

## How to Prioritize Issues
Three buckets, hard limits:
- **Critical (≤3):** blocks the goal, ships a bug, or misleads a user. Must be fixed.
- **Important (≤5):** meaningfully weakens the outcome. Fix next iteration.
- **Minor (one line each, ≤5):** polish. Explicitly optional.
If you found 12 "critical" issues, you haven't prioritized — re-rank until three remain.

## How to Avoid 30 Equal-Weight Nitpicks
- Write the critique *after* deciding the single biggest problem, not while scanning.
- Force ranking with the buckets above; forbid bullet lists longer than the bucket limits.
- Merge related nits into their root cause ("6 spacing inconsistencies" = one issue: "no spacing scale — adopt 4/8/16/24").

## How to Convert Critique into Action
End every critique with:
```
## Next build instruction
<one paste-ready instruction for the builder: what to change, where, to what — specific values, files, or copy>
```
- Bad ending: "Overall, with some refinements, this could be strong."
- Good ending: "Next: in `pricing-card.tsx`, make the price `text-4xl font-semibold`, move the billing-period toggle above the cards, and change the CTA copy to 'Start free — no card'. Re-screenshot after."

## Output Format for Critique
```markdown
# Critique: <artifact> — Goal: <what it must achieve>
**Working:** <one line — what to preserve>

## Critical (fix before ship)
1. <issue> → **Fix:** <exact change>
2. ...
## Important
- <issue> → <fix>
## Minor
- <one-liners>

## Next build instruction
<single paste-ready instruction>
```
