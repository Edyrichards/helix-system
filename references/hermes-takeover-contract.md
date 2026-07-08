# Hermes Takeover Contract

This defines what it would mean for Helix to "take over Hermes" responsibly.

## Meaning

Helix should not replace Hermes infrastructure. It should become the highest-quality operating layer on top of Hermes capabilities.

| Hermes capability | Helix responsibility |
|---|---|
| Skills | route and load only needed capability modules |
| Tools | choose safe tool path, execute, verify |
| Delegation | plan swarms, brief specialists, synthesize evidence |
| Memory | promote only durable lessons, avoid stale task logs |
| Cron | schedule self-improvement/health checks only with explicit user intent |
| Plugins | lazy-load catalogs/personas/references without context bloat |
| Profiles | respect profile boundaries and avoid cross-profile writes |

## Takeover readiness gates

- Catalogs and docs integrity pass.
- Broken references fail CI.
- Persona/runbook schemas pass.
- Swarm outputs are structured and verifiable.
- Safety/security model is loaded for side effects.
- Benchmark suite shows improvement over baseline host behavior.

## Non-goals

- Do not bypass Hermes permission/tool safety.
- Do not auto-modify memories/cron/plugins without user intent.
- Do not load all personas/references into every context.
