# Helix Best-in-Class Roadmap

## North Star

Helix should become the agent operating system capable of powering Hermes-grade workflows across Claude Code, Cursor, Codex, Hermes, and future agent hosts.

It must be excellent at four things:
1. **Understanding**: intake + reprompting + context grounding.
2. **Designing**: design reasoning + psychology + system-first craft.
3. **Executing**: tools, code, screenshots, tests, evidence.
4. **Improving**: evals, lessons, self-patches, swarm reflection.

## Immediate Differentiator

Best-in-class **design reasoning and design psychology**, because this is where most AI coding agents visibly fail.

Helix should be known for:
- turning vague product/design intent into professional briefs
- asking the right 1-3 questions
- producing behaviorally reasoned UI
- detecting AI design tells
- verifying with actual screenshots
- running specialist swarms

## Capability Gaps Closed In This Upgrade

| Gap | New Capability |
|---|---|
| agency-agents had stronger public specialist roster | `PERSONA_CATALOG.md` + 8 Helix-native personas |
| weak visible dissection/proof | `research/agency-agents-dissection-2026-07.md` |
| design reasoning needed more rigor | `references/10-design-reasoning-engine.md` |
| psychology needed deeper theory | `references/11-advanced-design-psychology.md` |
| prompt reprompting needed explicit engine | `references/12-prompt-reprompt-engine.md` + script |
| GTM was missing | `GO_TO_MARKET.md` |
| installation less smooth than competitors | `scripts/install_helix.sh` |
| persona quality needed tests | `scripts/validate_personas.py` |
| examples absent | `examples/reprompt-onboarding.md`, `examples/design-swarm-checkout.md` |

## Next Best Upgrades

### Phase 1: Proof Assets
- Create 3 rendered demo projects:
  1. onboarding redesign
  2. checkout redesign
  3. landing page redesign
- For each: raw prompt, reprompted brief, screenshots, rubric score, lessons.

### Phase 2: Real Swarm Execution
- Enhance `helix_swarm.py` to execute real parallel branches where host supports it.
- Add JSON evidence manifests for each branch.
- Add swarm quality scoring.

### Phase 3: Public Distribution
- Create `scripts/convert_helix.py` for Claude/Codex/Cursor/Hermes formats.
- Add a small web/catalog UI or static docs site.
- Add badges, release artifacts, demo GIFs.

### Phase 4: Benchmark Suite
- Compare baseline Claude vs Helix on:
  - vague prompt handling
  - design quality rubric
  - psychology reasoning
  - verification rate
  - hallucination avoidance
- Publish results in `evals/benchmarks/`.

### Phase 5: Hermes Takeover Readiness
- Lazy-router plugin for Helix personas.
- Tool adapters for Hermes-native delegation.
- Skill/router composability.
- First-class scheduled self-improvement jobs.

## Non-Negotiable Standards

- No claims without evidence.
- No copying external prompt text.
- No design completion without screenshots for substantial UI.
- No GTM claim without proof asset.
- No persona accepted without schema validation.
- No self-improvement patch without before/after evidence.

## Definition of "Best"

Helix is best when a user can say something vague like:

> "Make this onboarding better and launch it"

and Helix can:
1. ask only the missing critical questions
2. reprompt the task into an expert brief
3. dispatch a swarm
4. research real patterns
5. apply design psychology
6. implement or spec the work
7. verify with screenshots/tests
8. create launch messaging
9. save lessons
10. improve its own process afterward
