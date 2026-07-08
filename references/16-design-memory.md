# Helix Design Memory

Purpose: make UI/UX learning durable at project level without polluting global memory with stale artifacts.

## Memory locations
For a project repo, prefer:
```text
design/helix-memory/
  behavior-maps/
  reference-boards/
  reference-patterns.json
  screenshot-critiques/
  tournaments/
  lessons.md
  rejected-directions.md
```

For portable Helix patterns, promote only abstract, reusable lessons into Helix references or skills.

## What to save
Save lessons that are:
- screenshot-backed
- reusable across future UI work
- tied to behavior/psychology or visual craft
- explicit about when not to use them

Do not save:
- raw secrets, private screenshots without user approval
- copied proprietary designs
- temporary task progress
- one-off file paths as global memory

## Lesson format
Use `schemas/design-lesson.schema.json`.

Minimum fields:
- title
- context
- evidence paths
- problem observed
- repair/change
- before/after effect
- reusable rule
- anti-pattern avoided
- applicability
- expiration/review note

## Promotion rule
A lesson becomes a Helix-level rule only after one of:
- it wins in multiple tournaments
- it fixes a recurring failure
- the user explicitly approves promotion
- it is backed by well-established UX/design research
