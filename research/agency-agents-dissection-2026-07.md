# Agency Agents Dissection (Clean-Room)

Date: 2026-07-08  
Subject: https://github.com/msitarzewski/agency-agents  
Local clone inspected: `/tmp/agency-agents`

## Why this matters

Edy correctly identified a gap: Helix had strong operating discipline, but agency-agents had a stronger public-facing specialist roster, installer story, and community packaging. This dissection exists so Helix improvements are based on actual repo evidence, not a hand-wave that we "searched resources."

## Evidence reviewed

- `README.md` (1,077 lines)
- `scripts/install.sh`, `scripts/convert.sh`, `scripts/build-hermes-plugin.py`
- `divisions.json`, `tools.json`
- Sample agents, especially:
  - `design/design-ui-designer.md`
  - `engineering/engineering-code-reviewer.md`
  - engineering + design roster tables in README
- Integration directories:
  - `integrations/claude-code`, `cursor`, `codex`, `hermes`, `opencode`, `gemini-cli`, `aider`, `windsurf`, `qwen`, `kimi`, `vibe`, etc.

## Quantitative snapshot

Local clean-room analysis found:

| Metric | Finding |
|---|---:|
| Agent markdown files with frontmatter | 229 |
| Divisions found | 17 |
| Largest divisions | specialized 53, marketing 36, engineering 36, game-development 20, GIS 13 |
| Median agent length | 239 lines |
| Max agent length | 618 lines |
| Common frontmatter keys | `name`, `description`, `color`, `emoji`, `vibe` |
| Common body sections | Identity & Memory, Critical Rules, Core Mission, Advanced Capabilities, Communication Style, Success Metrics, Workflow Process, Learning & Memory |
| Supported integrations | Claude Code, Cursor, Codex, Hermes, Aider, Windsurf, Gemini CLI, OpenCode, Qwen, Kimi, Vibe, GitHub Copilot, etc. |

## What agency-agents does better than Helix today

### 1. Specialist breadth and memorability
Agency-agents has a huge roster of named specialists with clear personalities. The agents feel like a team a user can understand quickly.

**Pattern to adopt**: not the prompts themselves, but the schema:
- frontmatter identity
- role + vibe
- critical rules
- workflow process
- deliverables
- success metrics
- communication style

### 2. Install/distribution UX
Their README has immediate installation options and a desktop app. `install.sh` supports targeted install by tool, division, and agent. `convert.sh` adapts source agents into tool-specific formats.

**Pattern to adopt**:
- one-command install
- selective install by capability
- conversion layer for Claude/Codex/Hermes/Cursor/etc.
- user-facing app or catalog eventually

### 3. Public roster as marketing
The README itself is a catalog. It creates desire because users can imagine using the agents.

**Pattern to adopt**:
- public-facing Helix persona catalog
- "when to use" table
- examples of real swarm workflows
- GTM assets that show outcomes, not internals

### 4. Hermes lazy-router insight
Their Hermes plugin uses a small fixed tool surface and stores the roster in JSON, avoiding bloating the initial skill catalog.

**Pattern to adopt**:
- for large Helix persona rosters, do not expose everything as separate always-loaded skills
- create a router/index that loads specialists lazily

## What Helix already does better

| Capability | Agency Agents | Helix |
|---|---|---|
| Anti-hallucination intake | mostly implicit | explicit `08-intake...` gate |
| Evidence ledger | not global | first-class |
| Fresh-context verification | prompt-level | explicit verifier subagents |
| Real browser screenshots | not systemic | Playwright design tournaments |
| Self-improvement | not a core loop | `07-self-improvement` + script |
| Design psychology | varies by agent | dedicated UX psychology ref |
| Portable harness | many installers | operating-system style refs + scripts |
| Swarm discipline | agent collection | `09-swarm-orchestration` with coordinator/jury |

## Strategic synthesis

Agency-agents is best understood as **the best public specialist catalog**.

Helix must become **the best execution OS for specialists**.

Therefore, Helix should not compete by adding 262 shallow personas. It should:
1. Build a smaller elite specialist roster.
2. Give each specialist the Helix spine: intake, evidence, verification, self-improvement.
3. Add a router/catalog so users can discover and install specialists easily.
4. Make design reasoning and psychology a flagship wedge.
5. Publish proof: screenshots, evals, before/after prompt rewrites, design tournaments.

## Clean-room implementation decisions

Do **not** copy text from agency-agents agents.

Do adopt these structural patterns:
- Persona frontmatter: `name`, `type`, `helix-role`, `vibe`, `when_to_use`, `loads`, `outputs`
- Divisions/categories for public catalog
- Install/conversion scripts
- README roster tables
- Quality/lint scripts
- Hermes lazy-router style for large rosters
- Examples folder with workflows

## Priority upgrades for Helix

1. **Elite Design Intelligence layer**
   - Design reasoning chain
   - psychology-driven critique
   - conversion/onboarding heuristics
   - failure modes and anti-slop rubric

2. **Prompt Re-Prompt Engine**
   - turn raw vague input into structured intent
   - ask target questions only when necessary
   - internally generate enhanced prompt, then execute
   - produce optional visible "Reprompted Brief" artifact for user confirmation

3. **Persona Catalog + Router**
   - small elite roster, not giant bag of prompts
   - every persona inherits Helix contract
   - catalog table in docs
   - install/conversion commands

4. **GTM package**
   - tagline, positioning, landing copy, launch checklist
   - comparison vs prompt packs and agent frameworks
   - proof artifacts and demo scenarios

5. **Quality gates**
   - persona linter
   - coverage checks for references/scripts/docs
   - self-improvement evals

## One-sentence conclusion

Agency-agents wins at public packaging and specialist breadth; Helix should win by becoming the verified, self-improving design-and-execution operating system that can *use* specialists better than any prompt roster can.
