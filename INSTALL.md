# Helix Installation Guide (Portable)

## Sending to a friend who uses Claude

The simplest thing to send is the dedicated quickstart:

→ [QUICKSTART_CLAUDE.md](QUICKSTART_CLAUDE.md)

It contains the exact steps and explanation your friend needs.

---



Helix is designed to be **portable across AI coding environments**, not tied to Hermes.

The core is a set of:
- **References** (`references/`) — on-demand operating rules
- **Project Knowledge layers** (`project-knowledge/`) — deep behavioral layers
- **Skills** (`source-skills/`) — reusable procedures (ready for `.claude/skills/`)
- **Templates** — `templates/CLAUDE.md.template`, `repo/CLAUDE.md`
- **Scripts** — automation (Python, runnable anywhere with the deps)
- **Prompts** and eval harness

Fast install into a project:

```bash
git clone https://github.com/Edyrichards/helix-system.git
cd helix-system
scripts/install_helix.sh /path/to/project
```

Clone the repo once:

```bash
git clone https://github.com/Edyrichards/helix-system.git
cd helix-system
```

Then follow the section for your tool.

## For Claude Code, Cursor, Claude Desktop, Windsurf, or any Anthropic Claude-based tool

### Option 1: Per-Project (Recommended)
1. In your target project, run the bootstrapper (highly recommended):
   ```bash
   python /path/to/helix-system/scripts/helix_init.py . --write
   ```
   This inspects your repo and generates a tailored `CLAUDE.md`.

2. Copy relevant skills:
   ```bash
   mkdir -p .claude/skills
   cp /path/to/helix-system/source-skills/*.skill.md .claude/skills/
   # Or selectively: coding.skill.md design etc.
   ```

3. (Optional but powerful) Add layers as Project Knowledge / custom instructions:
   - Upload or paste content from `project-knowledge/helix-*-layer.md`
   - Especially: `helix-skill-system.md`, `helix-coding-layer.md`, `helix-design-layer.md`, `helix-verification-layer.md`, `helix-handoff-layer.md`

4. For strong design/onboarding work, also load:
   - `references/ux-psychology-principles.md`
   - `references/design-masterclass.md`
   - `references/ui-design-autonomy-repo-patterns.md`

5. Paste the compact master rules when starting a new Claude Project:
   - See `master-claude-project-instructions.md` (paste the whole block into Project Instructions).

### Option 2: Global / Cross-Project
Copy skills to your global Claude skills location (tool-dependent, often `~/.claude/skills` or via UI).

Use the `repo/CLAUDE.md` as a base and customize per project.

## For Codex (OpenAI Codex CLI, custom agents, or similar)

1. Use the references and layers as custom instructions or RAG context.
2. Copy `project-knowledge/` and `references/` into your agent's knowledge base.
3. Use `prompts/helix-prompt-library.md` for task-specific prompts.
4. Run the research/tournament scripts directly when doing design work:
   ```bash
   python scripts/helix_design_research.py ...
   python scripts/helix_live_design_analyzer.py ...   # requires Playwright
   ```
5. For project-specific behavior, generate a `CLAUDE.md` with the init script and adapt the style rules.

## For Hermes (original)

```bash
hermes -s helix-system
# or
/skill helix-system
```

The `agent.md` and `SKILL.md` are the Hermes adapters.

## Standalone / Any Other Agent

- Load files from `references/` on demand (they are progressive — load only what's needed for the task).
- Use `source-skills/` as procedure guides.
- Run scripts for automation (design research, tournaments, live browser analysis, init).
- For UI/UX work, always start with the new UX psychology rules + design system first.

## Key Portable Commands (run from cloned helix-system)

```bash
# Bootstrap a new project with Helix conventions + CLAUDE.md
python scripts/helix_init.py /path/to/your-project --write

# Design research (GitHub patterns)
python scripts/helix_design_research.py --limit 15

# Live browser analysis of real onboarding flows (Mobbin-style)
python scripts/helix_live_design_analyzer.py \
  --urls "https://example.com/onboarding" \
  --flow onboarding

# UI variant tournament with real screenshots
python scripts/helix_design_tournament.py --brief "..." --variants-json ...

# Self verification
python scripts/verify_install.py
python tests/run_design_autonomy_tests.py
```

## What to Copy Where (Summary)

| Your Environment       | What to Use                                      | Location / Action                     |
|------------------------|--------------------------------------------------|---------------------------------------|
| Claude Code / Cursor   | CLAUDE.md + .claude/skills/ + layers             | Per project or global                 |
| Codex / other agents   | references/ + project-knowledge/ + prompts/      | Agent knowledge base                  |
| Hermes                 | Full agent + skill                               | `hermes -s helix-system`              |
| Any project            | `scripts/helix_init.py --write`                  | Generates project-specific CLAUDE.md  |
| Design work            | `references/ux-psychology-principles.md` + design refs | Load explicitly for onboarding flows |

## Keeping in Sync

The GitHub repo (https://github.com/Edyrichards/helix-system) is the single source of truth.

When you improve rules or add capabilities:
1. Update in this repo.
2. Re-clone or pull in your projects.
3. Re-run `helix_init.py` on active projects if the template changed.

## License & Notes

See README for current status. Scripts are Python and should run in most environments (some require Playwright for browser features).

For questions or contributions, open an issue on the GitHub repo.

This structure follows the philosophy in `helix-packaging-plan.md`: instructions are always-on (CLAUDE.md), knowledge is on-demand (layers/references), skills are per-repo or global.


## Self-Improvement (Making Helix Better Over Time)

Helix can improve *itself* using its own systems.

1. Load `references/07-self-improvement.md`
2. Run the driver:
   ```bash
   python scripts/helix_self_improve.py --area "mode-router" --brief "ensure UX psychology is always loaded for onboarding"
   ```
3. Review the evidence in `evals/self-improvement/<timestamp>/`
4. The script produces:
   - Baseline + research
   - Scored variants
   - A proposed lesson file in `lessons/<area>/`
   - A concrete proposal with next steps

This loop uses the same eval, research, tournament, critique, and lesson machinery that Helix uses for user work.

For full autonomy, invoke the Meta mode and let the agent drive multiple iterations with verifier subagents.

See `references/07-self-improvement.md` for the complete architecture (detect → scope → baseline → research → variants → tournament → repair → lesson → commit).


## Built-in Anti-Hallucination Intake

Helix always starts with structured input handling (see `references/08-intake-sufficiency-prompt-restructuring.md`):

1. Listen and parse the user's message.
2. Run explicit sufficiency checklist to detect hallucination risks (missing goals, data, criteria, examples).
3. Ask at most 1-3 targeted clarifying questions if critical gaps exist.
4. Internally restructure the task using sophisticated prompt engineering (decomposition, Chain-of-Verification, Tree-of-Thoughts internally, expert role elevation, scaffolding) then distill to natural, high-quality output.

This process is mandatory and portable. In Claude Code / Cursor load the reference as instructions. The restructuring is invisible — users see either precise questions or clean execution.

This makes Helix dramatically less likely to hallucinate and produces better natural results.


## Swarm & Multi-Agent Capabilities
Load `references/09-swarm-orchestration.md` and the personas in `personas/`.

Example:
1. Load Swarm Coordinator persona.
2. Give it a complex goal.
3. It will decompose, dispatch parallel specialists (each following full Helix rules), run verification jury, and synthesize.

Run `python scripts/helix_swarm.py --goal "..."` for help generating the decomposition and execution prompt.

This is one of Helix's core differentiators: reliable parallel specialist work with evidence and verification built in.


## Best-in-Class Design / Reprompting Stack
For premium design, onboarding, conversion, or product experience work, load:

- `references/08-intake-sufficiency-prompt-restructuring.md`
- `references/12-prompt-reprompt-engine.md`
- `references/10-design-reasoning-engine.md`
- `references/11-advanced-design-psychology.md`
- `references/design-masterclass.md`
- `PERSONA_CATALOG.md`

Recommended swarm:
- Prompt Architect
- Research Synthesizer
- Conversion Psychologist
- Design Specialist
- Design Jury Lead

For GTM, load `GO_TO_MARKET.md` and `personas/gtm-strategist.md`.
