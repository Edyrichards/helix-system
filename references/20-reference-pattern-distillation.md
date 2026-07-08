# Helix Reference Pattern Distillation

Purpose: turn proven UI references into abstract patterns that Helix can adapt without copying.

## Distillation pipeline
For each reference:
1. Identify surface and user job.
2. Describe the behavioral mechanism.
3. Map hierarchy: first object, second proof, CTA, risk reducer.
4. Extract layout pattern in abstract terms.
5. Extract interaction/disclosure pattern.
6. Extract mobile adaptation.
7. Define adaptation for the current product.
8. Define what must not be copied.

## Pattern card format
```md
## Pattern: <name>
Source evidence: <reference URL/path/app/screen>
Useful when: <conditions>
Behavior mechanism: <why it works>
Structure: <abstract hierarchy>
Adapt for this product: <specific adaptation>
Avoid copying: <brand/copy/exact layout/assets>
Risks: <when it fails>
```

## Example for Drift
Pattern: Interpreted money movement before signup
Useful when: user fears another budgeting chore.
Behavior mechanism: value-before-ask + anxiety reduction.
Structure: one large interpreted result, cause split, low-risk CTA, safety line.
Adapt: Money Weather instrument with plan/actual, price/habit/one-off, Sunday review.
Avoid copying: any specific Mobbin app layout, copy, icons, or brand styling.
