# Example: Best-in-Class Design Swarm

## Goal

Redesign checkout for a premium productivity SaaS so users understand the value, trust the price, and complete purchase without feeling pressured.

## Recommended Swarm

| Role | Persona | Responsibility |
|---|---|---|
| Coordinator | Swarm Coordinator | Decompose, dispatch, synthesize evidence |
| Input | Prompt Architect | Reprompt raw brief into professional execution brief |
| Research | Research Synthesizer | Inspect competitors and checkout patterns |
| Psychology | Conversion Psychologist | Map motivation, ability, trust, value-before-ask |
| Design | Design Specialist | Design tokens, layout, states, copy strategy |
| Jury | Design Jury Lead | Rendered critique, psychology score, stop-ship issues |
| Code | Code Reviewer | If implemented, review diff and tests |

## Execution Prompt

```text
You are the Helix Swarm Coordinator.
Goal: Redesign checkout for a premium productivity SaaS so users understand value, trust price, and complete purchase without pressure.
Load references/09-swarm-orchestration.md, references/12-prompt-reprompt-engine.md, references/10-design-reasoning-engine.md, references/11-advanced-design-psychology.md, and PERSONA_CATALOG.md.
Run intake first. Then decompose into parallel specialist briefs and synthesize with a master evidence ledger.
```

## Expected Evidence

- Reprompted brief
- Psychological friction map
- Competitor/pattern table
- Design system decisions
- Desktop and mobile screenshots
- Console/overflow status
- Rubric v3 score
- Final PASS/PASS WITH RISKS/FAIL from Design Jury Lead
