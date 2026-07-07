# Helix Prompt Library

Copy-paste-ready prompts. Replace `<...>` placeholders. Each prompt encodes: role → context → deliverable → constraints → output format → verification.

---

## 1. Vague Idea → Build Brief
```
Turn this idea into a build brief: <idea>.

Output exactly these sections:
1. User — one specific persona, one sentence
2. Job-to-be-done — the outcome they hire this for
3. Core loop — the repeated action → reward cycle (3–5 steps)
4. MVP scope — the smallest complete loop, as a checklist of ≤7 items
5. Explicitly out of scope — ≥5 items
6. Differentiator — one thing a generic version would not have
7. First screen — describe the exact UI of the most important screen

Do not add features beyond the loop. If the idea is too broad, pick the sharpest wedge and say why.
```

## 2. Inspect a Repo Before Coding
```
Before writing any code, inspect this repo and report back. Do not edit anything yet.

1. Read package.json / config files — list stack, versions, scripts.
2. Map the folder structure (top 2 levels).
3. Find and read the 3–5 files most relevant to: <task>.
4. Identify existing patterns I must follow (state management, styling, data fetching, error handling).
5. List anything that already partially implements <task>.

Output: stack summary, relevant files with one-line roles, patterns to follow, risks, and your proposed minimal change plan (files to touch + why). Wait for my approval.
```

## 3. Critique a UI
```
Critique this UI: <screenshot/URL/code>.

Rules: max 3 critical issues, ranked by user impact. For each: what's wrong, why it hurts (usability/hierarchy/trust), and the exact fix (specific values — spacing, color, copy — not "improve spacing"). Then list up to 5 minor issues in one line each. End with the single change that would most improve this screen, written as a build instruction I can paste into a coding agent.
Do not praise. Do not list 30 equal-weight nitpicks.
```

## 4. Improve Your Own Output
```
Review the output you just produced as if a demanding senior <designer/engineer/editor> wrote a rejection note on it.

1. Find the 3 weakest parts. Be specific — quote them.
2. Explain what a stronger version does differently.
3. Produce the improved version in full.

Do not defend the original. Do not make cosmetic changes and call them improvements.
```

## 5. HTML Prototype → React/Tailwind
```
Convert this HTML prototype to React + Tailwind: <code/file>.

Rules:
- Split into components at natural boundaries (nav, sections, cards, forms) — no single giant component.
- Replace inline styles/CSS with Tailwind utilities; move colors to design tokens.
- Extract repeated markup into mapped data arrays.
- Preserve the exact visual result — render both and compare before declaring done.
- TypeScript, semantic HTML, accessible labels.

Output: component files with paths, plus a note on anything that could not be converted 1:1 and why.
```

## 6. Create a Design System
```
Create a design system for <product> with this personality: <adjectives>.

Deliver:
1. Color tokens — exactly 1 primary, 2–3 neutrals, 1–2 accents, as CSS custom properties with semantic names (--background, --foreground, --primary, --accent). No purple unless requested.
2. Typography — max 2 font families, with a scale (sizes, weights, line-heights) for display/heading/body/caption.
3. Spacing scale and radius token.
4. 3 example components (button, card, input) using only the tokens.
5. One sentence explaining the personality each choice expresses.

Do not exceed 5 colors. Do not use gradients.
```

## 7. Competitor Research
```
Research competitors for <product> to inform <specific decision, e.g., "our onboarding flow">.

1. Pick the 3–4 most relevant competitors (say why each is relevant).
2. For each, extract only what bears on the decision: their approach, one strength to steal, one weakness to exploit.
3. Output a comparison table, then "Patterns" (what everyone does — table stakes), then "Gaps" (what no one does well).
4. End with a recommendation: what we should do, in one paragraph, justified by the table.

Cite the source for every factual claim. No generic market-size filler.
```

## 8. Create a Product Strategy
```
Create a one-page product strategy for <product>.

Sections: Target user (one persona) / Job-to-be-done / Core loop (diagram in text) / Wedge (why we win entry) / USP (one sentence) / MVP (smallest complete loop) / Not-doing list / 3-phase roadmap where each phase strengthens the loop.

Constraint: every feature in the roadmap must map to a step in the core loop. Delete anything that doesn't. One page max.
```

## 9. Debug an Error
```
Debug this error: <full error text + context>.

Process:
1. State your hypothesis for the root cause before changing anything.
2. Read the exact files/lines involved — quote the offending code.
3. If the hypothesis needs testing, add targeted logging or a minimal reproduction — do not shotgun changes.
4. Apply the smallest fix. Explain why it addresses the cause, not the symptom.
5. Verify by reproducing the original failure path and showing it now succeeds.

Do not refactor surrounding code. Do not fix what isn't broken. If two fixes failed, stop and re-derive the hypothesis from scratch.
```

## 10. Create a Project Knowledge File
```
Compress everything decided in this conversation into a project knowledge file.

Include: goal, stack, key decisions with one-line rationale, conventions, current state (done/in-progress/blocked), and open questions. Exclude: conversational back-and-forth, abandoned directions, anything re-derivable from the code.
Format as markdown, ≤80 lines, named <project>-knowledge.md. It must let a fresh model continue without reading this chat.
```

## 11. Create a CLAUDE.md
```
Inspect this repo and write a CLAUDE.md for it.

Include: what the project is (2 lines), commands (dev/build/test/lint — verified from package.json), architecture map (key folders, one line each), conventions to follow (found by reading actual code, not assumed), things to never do in this repo, and how to verify changes.
Rules: every command must actually exist; every convention must cite an example file; ≤100 lines.
```

## 12. Model-Evaluates-Model
```
Evaluate this output produced by another AI for the task: <task>.

Score 1–5 on: correctness, completeness vs. the actual ask, specificity (concrete vs. generic), usability (could I act on it immediately), and scope discipline (did it do the task, not a different one).
For each score ≤3, quote the evidence. Then state: what the output gets right, the single biggest failure, and the revision instruction you would give.
Judge the work, not the writing style. Confident prose with generic content scores low.
```

## 13. Compress a Playbook into Project Instructions
```
Compress this playbook into project instructions: <file/content>.

Rules:
- Keep only operational rules — things that change behavior on a specific decision. Cut philosophy, motivation, and examples.
- Merge duplicates; resolve conflicts by keeping the stricter rule.
- Group under ≤8 headings. Target ≤120 lines.
- Every line must pass the test: "would a competent model behave differently without this line?" If not, delete it.
```
