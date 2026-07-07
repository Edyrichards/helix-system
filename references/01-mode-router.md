# Helix Mode Router
**Always run `08-intake-sufficiency-prompt-restructuring.md` (sufficiency check + internal restructuring) BEFORE classifying mode.**



Select the primary mode before acting. Load the matching reference files and apply the verification gate.

| Mode | Trigger | Load | Required output | Verification gate |
|---|---|---|---|---|
| Code/debug | edit, inspect, fix, implement, repo, error, test | `coding.md`, `tool-use.md`, `verification.md` | diff/artifact + commands run | manifest/config inspected; relevant files read; narrow test/build/repro run or explicitly blocked |
| UI/UX/design | screen, component, landing, dashboard, visual, screenshot, UX | `design-system-first.md`, `charts-and-design-system-adapters.md`, `design-masterclass.md`, `ui-pro-max-preflight.md`, `design-rubric-v2.md`, plus `design.md`, `uiux-system-prompt.md`, `repo-design-section.md`, `verification.md` | design read + screen job + implemented/critique details | rendered or screenshot inspected at mobile + desktop when possible; states/preflight checked |
| Product strategy | product idea, MVP, roadmap, features, positioning | `product-strategy.md`, `critique.md` | one-page strategy | user/JTBD/core loop/wedge/MVP/not-doing all present |
| Research | current facts, competitors, docs, market, papers | `research.md`, `evidence-ledger.md` | findings table + patterns + gaps + recommendation | sources opened; load-bearing claims cited; recommendation traceable |
| Critique/review | critique, review, evaluate output, compare | `critique.md`, `verification.md` | max 3 critical issues + exact fixes + next build instruction | judged against stated goal; no praise padding; evidence quoted |
| Prompt writing | prompt, agent prompt, handoff prompt, system instruction | `prompt-library.md`, `operating-contract.md` | copy-paste prompt block | role/context/deliverable/constraints/output/verification included |
| Handoff | continue later, give to Claude/Codex/Cursor/v0/Lovable/human | `handoff.md`, `evidence-ledger.md` | handoff brief | goal/current state/verification labels/next task/materials included |
| Meta / Self-Improve | improve helix, self-critique, update references/skills, meta-loop, lesson extraction | `07-self-improvement.md`, `05-memory-lessons.md`, `06-eval-harness.md`, `03-verifier-subagents.md`, `critique.md` | evidence-backed proposal + before/after + lesson or patch | narrow eval or tournament run; evidence ledger; portability check; git diff or proposed changes |
| Data/document | CSV, spreadsheet, PDF, doc, report, deck | `verification.md`, relevant document/data skills | file/report | output opened/read/spot-checked; row/page/section counts verified |

## Multi-mode rule
If a task spans modes, sequence them. Example: app feature = product loop -> coding -> UI verification -> handoff. Do not blend all rules into one unfocused response.

## Delegation rule
Use verifier subagents for major/high-stakes work, complex code changes, UI screenshots, research with citations, or handoffs meant for another model. See `03-verifier-subagents.md`.
