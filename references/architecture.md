# Helix Architecture

Helix is a portable agent operating system layer. It is not a single prompt and not only a Hermes skill.

## Layers

| Layer | Source | Purpose |
|---|---|---|
| Adapter | `agent.md`, `SKILL.md`, generated integrations | Host-specific entrypoints |
| Operating contract | `references/00-*`, `08-*`, `12-*` | intake, reprompting, routing, completion language |
| Capability modules | `references/`, `project-knowledge/`, `source-skills/` | specialized behavior loaded lazily |
| Persona system | `personas/`, `PERSONA_CATALOG.md`, `catalog/personas.json` | specialist roles with evidence contracts |
| Runtime scripts | `scripts/` | install, convert, eval, reprompt, swarm, verification |
| Catalog/runbooks | `catalog/*.json`, `runbooks/runbooks.json` | productized discovery and generated integrations |
| Evidence/evals | `evals/`, `examples/`, `lessons/` | proof, regression, self-improvement |

## Data flow

1. User input enters through a host adapter.
2. Intake checks sufficiency and hallucination risk.
3. Reprompt engine creates an expert brief or asks targeted questions.
4. Mode router selects references/personas/runbook.
5. Tools/scripts execute work and collect evidence.
6. Verifier/jury checks outputs.
7. Lessons/evals update Helix only after evidence.

## Extension rule

New capabilities must add source docs/scripts, catalog entries, verification, and examples before public claims.
