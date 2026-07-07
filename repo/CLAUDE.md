# CLAUDE.md

<!-- Helix repo-level instructions. Fill the <placeholders> per project; the rules below are project-agnostic and ready to use. -->

## Project
<One or two lines: what this app is and who uses it.>
Stack: <framework + version, language, styling, DB, auth>. Package manager: <pnpm/npm/yarn — match the lockfile>.

## Commands
- Dev: `<command>`
- Build: `<command>`
- Test: `<command>` (single file: `<command path>`)
- Lint/typecheck: `<command>`

## Operating Style
- Do exactly what was asked; the diff should read as one intentional change. No drive-by refactors, renames, or reformatting.
- Prefer editing existing files over creating new ones. Never create docs/READMEs unprompted.
- If a request is ambiguous in a way that changes the implementation, ask one specific question; otherwise state your assumption and proceed.

## Before Editing
- Read any file before editing it. Read the manifest/config before your first change of the session.
- Search for existing implementations first — mirror the closest existing pattern (component, route, query) instead of inventing a new one. Examine all search matches, not just the first.
- Install new dependencies before writing code that imports them.
- When changing shared code, find all consumers first.

## Design Rules
- Use the project's design tokens (`<globals.css / theme file>`) — never hardcoded hex or `text-white`/`bg-black` when tokens exist.
- Spacing via the scale (p-4, gap-6), gap over margin chains, mobile-first with responsive prefixes.
- Max 2 font families, 3–5 colors. If you change a background color, set the paired text color.
- Split UI into focused components; no giant page files.

## Coding Rules
- TypeScript strict; fix types at the source — never `as any` to silence.
- Semantic HTML, ARIA where needed, alt text on images.
- Server-side validation for all inputs; parameterized queries; never trust client data.
- Remove usage before removing imports. Delete debug logging before finishing.

## Tool Use
- File search by name → glob tools; by content → grep tools; read → read tool. Don't shell out for these.
- Run the dev server / scripts via the package manager. Background long-running processes.
- Verify library APIs against the installed version (node_modules) or current docs — not memory.

## Testing & Verification
- Run the narrowest proof first: the changed test file, route, or reproduction — then widen.
- UI changes: render in the browser, check structure and take a screenshot before declaring done. Compile/typecheck passing is not verification.
- Bug fixes: reproduce the original symptom after the fix.
- Never skip/disable tests to get green.

## Failure Recovery
- Read the first error line fully before acting; later errors are usually cascade.
- Max 2 attempts per hypothesis, then re-derive from evidence with targeted logging.
- If blocked on secrets/access/decisions, state exactly what's needed and continue with unblocked work.

## Communication Format
- Lead with what changed. Summaries: 2–4 sentences.
- End with verification status: "Verified: <what/how>" or "Unverified: <exact step to verify>".
- Note discovered tech debt in one sentence — don't fix it uninvited.
