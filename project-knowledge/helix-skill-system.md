# Helix Skill System

## What Skills Should Exist
Skills are reusable operating procedures for recurring task *types* — not answers to one-off questions. A skill earns its existence when the same workflow has been (or will be) executed 3+ times, has non-obvious steps, and produces measurably better output when followed.

## Where Each Kind Lives
- **Markdown skill files** (`.claude/skills/` or a skills folder): step-by-step procedures with output formats — coding workflows, critique rubrics, research methods.
- **Project instructions**: cross-cutting behavioral rules that must apply to *every* message in a project (tone, stack, scope discipline). Keep under ~150 lines.
- **Repo-level CLAUDE.md**: conventions bound to *this codebase* — commands, architecture, patterns, do-not-touch zones. Travels with the repo, not the person.

## When to Create a New Skill vs. One-Time Prompt
Create a skill when: the task recurs, the procedure has >3 non-obvious steps, or failure modes are predictable and preventable.
Use a one-time prompt when: the task is unique, the procedure is obvious, or the "skill" would just restate general competence.
Anti-pattern: skills that say "be thorough and careful" — a skill must contain decisions a generic model would get wrong.

## How to Write a Good Skill
1. Name it by the trigger, not the topic (`critique-ui.md` not `design-stuff.md`).
2. Open with one line: when to invoke it.
3. Numbered procedure — each step an action, not a virtue.
4. Exact output format (headings, tables, file names).
5. 2–3 anti-patterns with the correction.
6. Keep it under ~100 lines; link out for depth.

## Skill File Template
```markdown
# Skill: <name>
**Trigger:** Use when <specific situation>.
**Goal:** <the artifact or outcome this produces>

## Procedure
1. <action>
2. <action>
3. <action>

## Output Format
<exact structure of the deliverable>

## Anti-patterns
- <bad behavior> → instead <good behavior>
```

## Recommended Skill Library

### 1. execution-skill.md
- **Purpose:** How to run any task end-to-end without stalling.
- **When:** Every multi-step task.
- **Key rules:** Clarify only blocking ambiguities; bias to a working draft over a perfect plan; one visible deliverable per work session; end each turn with either a finished artifact or a single concrete question.
- **Output:** The artifact + 2–4 sentence summary.

### 2. design-skill.md
- **Purpose:** Produce distinctive, non-generic UI.
- **When:** Any new UI or visual change.
- **Key rules:** 3–5 colors max; 2 font families max; mobile-first; design tokens not hardcoded colors; screenshot and self-critique before delivery; never ship the "default AI look" (purple gradients, emoji icons, centered hero clichés).
- **Output:** Rendered UI + screenshot + token definitions.

### 3. coding-skill.md
- **Purpose:** Modify codebases safely.
- **When:** Any code change in an existing repo.
- **Key rules:** Read before edit; match existing patterns; smallest diff that solves the problem; run the narrowest verification; never drive-by refactor.
- **Output:** Diff-scoped edits + verification statement.

### 4. research-skill.md
- **Purpose:** Turn questions into decisions, not dumps.
- **When:** Anything requiring external facts.
- **Key rules:** Define the decision the research serves before searching; 2–4 queries; cite only load-bearing claims; end with a recommendation.
- **Output:** Findings table → implications → recommendation.

### 5. prompt-writing-skill.md
- **Purpose:** Convert vague asks into executable prompts.
- **When:** Writing prompts for any agent (self or other).
- **Key rules:** Role + context + concrete deliverable + constraints + output format + verification step. Ban filler instructions ("be creative").
- **Output:** Copy-paste-ready prompt block.

### 6. product-strategy-skill.md
- **Purpose:** Find the loop before building features.
- **When:** New product or major feature decisions.
- **Key rules:** Name the user, the job-to-be-done, the core loop, the wedge; MVP = smallest complete loop; reject features that don't feed the loop.
- **Output:** One-page strategy (user/JTBD/loop/wedge/MVP/roadmap).

### 7. artifact-skill.md
- **Purpose:** Pick and package the right output format.
- **When:** Any deliverable.
- **Key rules:** Match format to how the output will be *used* (pasted, run, read, presented); one artifact per deliverable; predictable file names; runnable things must run.
- **Output:** Named file(s) in a stated folder structure.

### 8. verification-skill.md
- **Purpose:** Earn the word "done."
- **When:** Before declaring any task complete.
- **Key rules:** Verify against the requirement, not the implementation; render UI, run code, re-read documents against the spec; state what was and wasn't verified.
- **Output:** One-line verification statement per deliverable.

### 9. critique-skill.md
- **Purpose:** Critique that changes the next build.
- **When:** Reviewing any code/design/writing/strategy.
- **Key rules:** Max 3 critical issues, ranked; every issue paired with a concrete fix; end with the single next build instruction.
- **Output:** Critical / Important / Minor table + next action.

### 10. handoff-skill.md
- **Purpose:** Transfer work without losing context or adding noise.
- **When:** Passing work to another model, developer, or stakeholder.
- **Key rules:** State goal, current state, constraints, verification status, and the exact next task; strip conversational history; include only files the receiver must touch.
- **Output:** Handoff brief using the template in `helix-handoff-layer.md`.
