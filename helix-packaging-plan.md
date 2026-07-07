# Helix Final Packaging Plan

## GitHub Repo Structure
```
helix/
├── README.md                          # one-paragraph overview + this map
├── CLAUDE.md                          # template — copy into each software repo's root
├── layers/
│   ├── helix-tool-use-layer.md
│   ├── helix-coding-layer.md
│   ├── helix-product-strategy-layer.md
│   ├── helix-research-layer.md
│   ├── helix-critique-layer.md
│   ├── helix-verification-layer.md
│   └── helix-handoff-layer.md
│   # (add your previously extracted execution + design layers here too)
├── skills/                            # mirror of .claude/skills — source of truth
│   ├── helix-skill-system.md          # the meta-doc: how to write/manage skills
│   ├── execution.md
│   ├── design.md
│   ├── coding.md
│   ├── research.md
│   ├── prompt-writing.md
│   ├── product-strategy.md
│   ├── artifact.md
│   ├── verification.md
│   ├── critique.md
│   └── handoff.md
├── prompts/
│   └── helix-prompt-library.md
├── instructions/
│   └── helix-master-project-instructions.md
└── eval/
    └── helix-test-suite.md
```
Derive the individual `skills/*.md` files from the library definitions in `helix-skill-system.md` using its template — each is ~40–80 lines extracted from the matching layer file.

## Claude Project Setup

### Project Instructions (paste, don't upload)
- `helix-master-project-instructions.md` — the entire contents, pasted into the Project Instructions field. This is the only always-on layer. Keep it under ~150 lines forever; it competes for attention with every message.

### Project Knowledge (upload as files)
Upload these so Claude can consult them on demand:
- All 7+ layer files (`layers/*.md`)
- `helix-skill-system.md`
- `helix-prompt-library.md`
- `helix-test-suite.md` (only in projects doing model evaluation — otherwise omit)
Do **not** upload `CLAUDE.md` (repo-scoped, not project-scoped) or the master instructions (already pasted — duplication causes drift).

## Per-Software-Repo Setup
- `CLAUDE.md` → repo root, filled in with that repo's actual commands/stack. One per repo, committed.
- `.claude/skills/` → copy from `helix/skills/`, keeping only skills relevant to that repo (typically: coding, design, verification, critique, handoff). Skip strategy/research skills in pure code repos.
```
your-app/
├── CLAUDE.md
└── .claude/
    └── skills/
        ├── coding.md
        ├── design.md
        ├── verification.md
        ├── critique.md
        └── handoff.md
```

## What Goes Where — Decision Table
| File | Claude Project Instructions | Claude Project Knowledge | Repo root | .claude/skills | Prompt library only |
|---|---|---|---|---|---|
| helix-master-project-instructions.md | ✅ (pasted) | — | — | — | — |
| Layer files (tool-use, coding, product, research, critique, verification, handoff) | — | ✅ | — | — | — |
| helix-skill-system.md | — | ✅ | — | — | — |
| Individual skills (execution…handoff) | — | — | — | ✅ | — |
| CLAUDE.md | — | — | ✅ (filled per repo) | — | — |
| helix-prompt-library.md | — | ✅ (optional) | — | — | ✅ (primary home) |
| helix-test-suite.md | — | eval projects only | — | — | — |
| helix-packaging-plan.md | — | — | helix repo only | — | — |

## Usage Rules
1. **Instructions are always-on; knowledge is on-demand; skills are per-repo.** Don't promote layer files into instructions — bloated instructions dilute compliance.
2. **Prompt library is for humans**, kept open in an editor and pasted per task. Uploading it to knowledge is optional convenience, not activation.
3. **Single source of truth is the GitHub repo.** Claude Project files and repo `.claude/skills` are copies — update the repo first, re-sync copies.
4. **Version it:** tag the repo when layers change materially; note the tag in the master instructions header so you can tell which version a project runs.
5. **Evaluate quarterly:** rerun `helix-test-suite.md` against a bare model to confirm the layers still add measurable lift; delete rules that no longer change behavior.
