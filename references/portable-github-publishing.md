# Portable GitHub Publishing for Helix

This document describes how to keep Helix installable across environments (Claude Code, Codex, Hermes, etc.) when publishing updates on GitHub.

## Core Principle
The GitHub repo is the single source of truth. All other installations (Hermes skills, Claude projects, local copies) are derived from it.

## What Lives in the Repo (Portable Core)
- `references/` — on-demand rules (load only what you need)
- `project-knowledge/` — layer files for project instructions / knowledge
- `source-skills/` — individual skill files (copy to `.claude/skills/`)
- `prompts/`, `templates/`, `scripts/`
- `INSTALL.md` and `helix-packaging-plan.md`
- `master-claude-project-instructions.md`

## Publishing Checklist
1. Update relevant references or layers in this repo.
2. Run self-tests: `python scripts/verify_install.py` and `python tests/run_design_autonomy_tests.py`.
3. Update `README.md` and `INSTALL.md` if user-facing instructions changed.
4. Update version in `agent.md` (Hermes frontmatter) and any tags.
5. Commit with clear message.
6. Push + create a tag (e.g. `vX.Y.Z`).
7. (Optional) Announce in relevant communities with link to INSTALL.md.

## How Users Install After a Release
See `INSTALL.md` in the repo root. Typical flows:
- Clone or pull the repo.
- Run `scripts/helix_init.py` in target projects.
- Copy `source-skills/` to `.claude/skills/`.
- Paste `master-claude-project-instructions.md` where appropriate.
- Load `references/ux-psychology-principles.md` etc. for specific domains.

## Cross-Tool Notes
- **Claude Code / Cursor**: Primary target. Use CLAUDE.md + .claude/skills/ + layers as knowledge.
- **Hermes**: The `agent.md` + `SKILL.md` + directory copies under `~/.hermes/agents/` and `~/.hermes/skills/`.
- **Codex / generic agents**: Treat `references/` and `project-knowledge/` as custom instructions or RAG documents. Scripts are standalone.
- **Per-project**: Always prefer generating a project-specific `CLAUDE.md` with the init script rather than global paste.

## Versioning
Tag releases when behavior changes materially (new principles, major script updates, rubric changes). Users can pin to a tag.

## Hygiene
- Keep references original and clean-room where possible.
- Do not include proprietary copied prompts from external sources.
- Maintain the UX psychology, design-system-first, and verification discipline in all updates.

When in doubt, optimize for the Claude Code / Cursor user who clones once and drops files into their projects.
