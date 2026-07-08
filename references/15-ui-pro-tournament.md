# Helix UI Pro Tournament

Purpose: replace one-shot UI generation with a multi-variant, reference-informed, behavior-scored design studio loop.

## Required pipeline
1. Intake and sufficiency check.
2. Behavior Map (`references/17-behavior-psychology-map.md`).
3. Reference Scout (`references/13-reference-scouting.md`).
4. Reference Pattern Distillation (`references/20-reference-pattern-distillation.md`).
5. Generate 3-5 variants.
6. Render desktop and mobile screenshots.
7. Behavioral + visual jury.
8. Repair top candidate at least twice for high-value work.
9. Implement winner in repo only after screenshot proof.
10. Verify and save lessons.

## Variant requirements
Each variant must declare:
- name and direction
- target behavior hypothesis
- reference patterns used
- primary fold hierarchy
- CTA strategy
- trust/risk reducer
- mobile collapse strategy
- risk/unknowns

## Recommended variant families
For product/landing UI:
- proof-first product instrument
- workflow/ritual narrative
- before/after decomposition
- trust/safety-first
- mobile-first app preview

## Scoring weights
Use stricter scoring than basic browser checks:
| Category | Weight |
|---|---:|
| First 5-second recognition | 15 |
| Behavior/anxiety reduction | 15 |
| Product truth | 15 |
| Reference-informed pattern quality | 10 |
| Product instrument / core object clarity | 15 |
| Visual originality and premium craft | 10 |
| Mobile rhythm | 10 |
| Trust/risk reduction | 5 |
| Browser/accessibility correctness | 5 |

Browser checks are necessary but cannot dominate. No-overflow and no-console-errors prove baseline competence, not excellent design.

## Jury roles
- Product strategist: product truth, positioning, IA
- UX psychologist: belief shift, motivation/ability/prompt, anxiety
- Visual director: hierarchy, composition, taste, originality
- Mobile reviewer: fold, pacing, touch targets, long-page fatigue
- Accessibility reviewer: labels, contrast, motion, semantics
- Anti-slop critic: AI tells, fake proof, generic cards, copied references

## Outputs
```text
design/helix-memory/tournaments/<timestamp>/
  behavior-map.json
  reference-board.json
  variants.json
  screenshots/
  visual-critiques.json
  repairs.json
  contact-sheet.html
  winner.md
  lessons.md
```
