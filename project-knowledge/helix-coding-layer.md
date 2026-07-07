# Helix Coding Layer

## Repo Inspection Workflow
1. **Manifest first:** package.json (or equivalent) — stack, versions, scripts, package manager (check the lockfile).
2. **Config second:** framework config, tsconfig, styling config — reveals conventions and constraints.
3. **Structure third:** top two folder levels — where pages, components, lib, and API code live.
4. **Task-relevant files fourth:** Grep for the feature's keywords; read every candidate match, not just the first.
5. **Pattern extraction:** before writing anything, find one existing example of the same kind of thing (a similar component, route, query) and mirror it.

## File Reading Order
manifest → config → the file named in the task → its parents/wrappers → its imports → similar siblings. Stop when you can predict how the codebase would want the change written.

## Rules Before Editing
- Never edit a file you haven't read this session.
- Never import a package you haven't confirmed is installed (install first, code second).
- Confirm the file you found is the one actually rendered/used — trace the import chain if there are look-alikes.
- If the change touches shared code, Grep for all consumers before changing the signature.

## Scope Control
- Implement exactly what was asked. The diff should read as one intentional change.
- No drive-by refactors, renames, reformatting, or "while I'm here" fixes. If you spot debt, note it in one sentence instead.
- When removing code: remove usage first, then the import — never the reverse.

## Component Reuse
- Search for an existing component/utility before writing a new one. Most codebases already have the button, the modal, the fetcher.
- Extend existing components via props/variants rather than forking near-duplicates.
- New UI gets split into focused components — no 400-line page files.

## Styling Rules
- Match the project's system (Tailwind version, tokens, CSS modules — whatever exists).
- Use semantic tokens (`bg-background`, `text-foreground`), never raw hex or `text-white` when a token system exists.
- Spacing via the scale (`p-4`, `gap-6`), not arbitrary values. Gap over margin-chains. Mobile-first, then responsive prefixes.
- If you change a background, you must set the paired text color.

## Testing Rules
- Run the narrowest test that proves the change first; widen only if it passes.
- New logic with branches gets a test if the repo has a test setup; match the existing test patterns.
- Never mark tests as skipped/todo to get green.

## Debugging Rules
1. Read the entire error — the answer is usually in line one.
2. Form a hypothesis before editing. Say it out loud (or in a comment/log).
3. Instrument with targeted logs (`[debug] state:`, values not vibes) rather than changing code blindly.
4. Fix the root cause; delete the debug logs after.
5. Two failed fixes = stop, discard the hypothesis, and re-derive from the evidence. Never attempt fix #3 on the same theory.

## Screenshot Verification
- Every user-visible change: render it, snapshot the structure, screenshot the layout.
- Check the actual failure mode class: overlap, blank sections, off-screen content, broken contrast, unstyled fallback fonts.
- For reported bugs: reproduce the original symptom after the fix, not just the happy path.

## Commit Summary Format
```
<verb> <what changed> — <why, if not obvious>

- <file/area>: <one-line change>
Verified: <what was run/rendered/tested>
```
Example: `Fix cart badge overcount — badge was reading line items, not quantities. Verified: added 2×item, badge shows 2, screenshot checked.`

## Failure Recovery Rules
- Build fails → read the first error only; later errors are usually cascade noise.
- Type errors → fix the type at its source, never `as any` to silence.
- Missing module → install it; don't vendor or stub.
- Flaky/unclear → reproduce minimally before touching production code.
- Blocked by missing access/secrets → state exactly what's needed and park the dependent work, continue elsewhere.

## Anti-Patterns to Avoid
- Rewriting a whole file to change three lines.
- "Fixing" by adding try/catch that swallows the error.
- Inventing APIs from memory instead of checking node_modules or docs.
- Creating `utils2.ts` because you didn't find `utils.ts`.
- Declaring done off a clean compile with zero rendering or execution.
- Batching unrelated changes so failures can't be isolated.
