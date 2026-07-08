# Quickstart for Claude Users (Claude Code, Cursor, Projects, etc.)

Helix is a portable execution-first agent harness. It makes Claude dramatically better at:
- Not hallucinating (mandatory intake + sufficiency check)
- Internally restructuring prompts with advanced techniques (invisible to you)
- Shipping verified artifacts instead of talking about them
- Strong design work (tokens first, real screenshots, UX psychology)
- Self-improving over time

## One-time clone
```bash
git clone https://github.com/Edyrichards/helix-system.git
```

## Recommended setup in your project

1. **Bootstrap** (in your target project folder):
   ```bash
   python /path/to/helix-system/scripts/helix_init.py . --write
   ```
   This creates a tailored `CLAUDE.md`.

2. **Install the skills**:
   ```bash
   mkdir -p .claude/skills
   cp /path/to/helix-system/source-skills/*.skill.md .claude/skills/
   ```

3. **Add the master rules** (in a new Claude Project or as custom instructions):
   - Open `master-claude-project-instructions.md` from the repo and paste the entire block into your Project Instructions.

4. **Load the layers** (highly recommended):
   In your project, add as Project Knowledge or custom instructions:
   - `project-knowledge/helix-execution-layer.md`
   - `project-knowledge/helix-skill-system.md`
   - `project-knowledge/helix-verification-layer.md`
   - `project-knowledge/helix-handoff-layer.md`
   - For design: `project-knowledge/helix-design-layer.md`

5. **Load key references** when needed (paste or attach):
   - `references/08-intake-sufficiency-prompt-restructuring.md` (the new anti-hallucination system)
   - `references/ux-psychology-principles.md` (for onboarding/UX work)
   - `references/design-masterclass.md`

## What changes in practice

- Claude will now **always start by listening and checking** whether it has enough information.
- If something is missing that would cause guessing, it asks 1-3 precise questions instead of hallucinating.
- Once it has enough, it internally rewrites the task using advanced prompt engineering, then executes cleanly.
- You get more "Verified: ..." outcomes and fewer vague plans.

## Bonus tools (run from the cloned repo)

- Design research + real browser tournaments with screenshots
- Self-improvement: `python scripts/helix_self_improve.py --area "..."`

Repo: https://github.com/Edyrichards/helix-system

Let me know what you think or if you want help setting it up on a specific project.
