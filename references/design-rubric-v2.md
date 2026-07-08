# Helix Design Rubric v3

Score Helix UI/design outputs on **20 dimensions, 0-5 each. Total 100.**

A visually attractive output can still fail if it lacks behavioral reasoning, ethical psychology, verification, or product specificity.

## Scoring Table

| Dimension | 0 | 3 | 5 |
|---|---|---|---|
| 1. Screen job clarity | no clear job | partially clear | one sharp job drives every decision |
| 2. User/JTBD specificity | generic user | plausible segment | concrete user + job + context |
| 3. Behavioral hypothesis | absent | implied | explicit if/then/because/measured-by |
| 4. Product specificity | generic SaaS words | some concrete details | believable domain moments, data, copy |
| 5. Hierarchy | everything competes | primary area visible | one loudest element, clear supports/demotions |
| 6. Information architecture | random sections | mostly ordered | sequence matches user decision path |
| 7. Layout/responsiveness | breaks/generic | works basic | mobile + desktop intentionally composed |
| 8. Design system discipline | random styles | mostly consistent | semantic tokens, type, palette, radius, states coherent |
| 9. State coverage | success-only | some states | empty/loading/error/success/disabled/focus handled |
| 10. Interaction/motion | absent/decorative | acceptable | purposeful, fast, accessible, tactile |
| 11. Accessibility/readability | low contrast/overflow | mostly readable | contrast, focus, touch, line-length, motion respected |
| 12. Anti-slop avoidance | obvious AI tells | minor tells | distinctive, appropriate, no generic slop |
| 13. Visual craft | crude/flat | competent | premium composition, spacing, type, assets |
| 14. Copy clarity | vague/filler | understandable | crisp, specific, action-oriented, no fake cleverness |
| 15. Trust architecture | no credibility | basic proof | credible evidence, transparent permissions/cost/risk |
| 16. UX psychology fit | ignores behavior | 1-2 weak principles | strong, ethical mechanisms tied to user value |
| 17. Friction reduction | high effort/confusion | moderate | smart defaults, chunking, reversibility, autonomy |
| 18. Conversion/commitment design | ask comes too early | some value/progress | value-before-ask, progress, investment, honest contrast |
| 19. Verification honesty | claims only | partial evidence | rendered/inspected with screenshots/errors/overflow |
| 20. Learning potential | no lesson | implicit | captures reusable lesson or eval signal |

## Hard Caps

- Any dark-pattern violation caps score at **50**.
- No rendered screenshot for substantial UI caps score at **70**.
- No mobile check caps score at **75**.
- Generic AI visual tells dominating the page cap score at **60**.
- In onboarding/sign-up/checkout/upgrade, psychology score below 15/25 caps total at **65**.

## Psychology Subscore (25 pts)
Use for dimensions 15-18 plus behavioral hypothesis.

| Mechanism | Points | Check |
|---|---:|---|
| Motivation clarity | 5 | user understands why now |
| Ability/friction reduction | 5 | next action is easy and reversible |
| Trust/proof | 5 | evidence is specific and credible |
| Value before ask | 5 | user receives or previews value first |
| Ethical integrity | 5 | no fake urgency, coercion, hidden costs |

## Winner Rule

A Helix output is meaningfully better than baseline only if:

- total score improves by at least **8/100**, or
- it fixes a critical product/design failure, or
- it produces stronger verified implementation while maintaining similar score.

If the score is close, say so. Do not overclaim Helix improvement.

## Required Evaluation Output

```markdown
## Rubric Score
Total: X/100
Psychology: Y/25
Hard caps triggered: none / <cap>

## Top 3 Reasons
1.
2.
3.

## Stop-Ship Issues
- none / issue list

## Evidence
- Desktop:
- Mobile:
- Console:
- Overflow:
```

## Best-in-Class Bar

A 90+ Helix design output must be:
- behaviorally reasoned
- psychologically ethical and effective
- visually premium
- system-consistent
- rendered and verified
- reusable as a lesson or pattern
