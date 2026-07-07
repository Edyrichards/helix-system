# Helix System Agent — Deep Research Upgrade Plan

**Question:** what would make the installed Helix System Agent closer to a best-in-class execution-first agent?

**Short answer:** the current Helix install has good behavioral rules. To make it meaningfully better, add an **agent harness** around the rules: compact skill loading, explicit task modes, evidence-backed progress, verifier subagents, memory/lesson hygiene, prompt/eval regression tests, and project bootstrap automation.

---

## Executive recommendation

Upgrade Helix from a large “instruction pack” into a **measured agent operating system**:

1. **Make the skill smaller and more navigable** — keep `SKILL.md` as a router under ~500 lines and move detailed layers into reference files loaded on demand.
2. **Add task-mode protocols** — coding, UI, research, critique, handoff, data/doc, and prompt-writing modes with different tool/evidence/verification gates.
3. **Add verifier subagents** — use separate fresh-context verifiers for code, UI, research, and handoff before claiming “done.”
4. **Add evidence-backed progress rules** — every progress claim must point to a tool result, file path, screenshot, command, or source opened in the current run.
5. **Add an eval suite runner** — run Helix’s test prompts automatically and score outputs against rubrics so regressions are visible.
6. **Add project bootstrap tooling** — `helix-init` should inspect a repo and install a filled `CLAUDE.md`, not a placeholder template.
7. **Add a lesson/memory protocol** — one lesson per file, update/delete stale lessons, no duplicate memory, and project-scoped notes rather than global bloat.
8. **Add agent safety boundaries** — clear “assess-only vs change files” rules, destructive action gates, and scope-change detection.

If we only do one thing: **add verifier subagents + eval runner**. That is the highest leverage because Helix’s promise is not just better taste; it is *verified execution*.

---

## Findings from source research

| Source | What it says | Implication for Helix |
|---|---|---|
| Anthropic “Prompting Claude Helix 5” | Helix-style models are strong at long-horizon autonomy, first-shot correctness, vision, code review/debugging, ambiguity navigation, and delegation. The docs specifically recommend evidence-audited progress, subagents, memory systems, and self-verification intervals. | Our Helix agent should not just be a prompt. It should include long-run scaffolding: progress audit, async/delegated verification, memory hygiene, and stop/continue rules. Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-helix-5.md |
| Anthropic “Building effective agents” | Successful agents usually use simple, composable patterns rather than heavy frameworks; start simple and add complexity only when needed. | Helix should avoid becoming a massive rigid framework. Use small protocols: router → task mode → tools → verifier → handoff. Source: https://www.anthropic.com/engineering/building-effective-agents |
| Anthropic prompting best practices | Clear instructions, examples, XML/structured sections, prompt chaining, and tool-use specificity improve reliability. | Convert the current Helix layers into structured tags/templates and add few-shot examples of “good vs bad” outputs for critical modes. Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices.md |
| Anthropic Agent Skills best practices | Skills should use progressive disclosure; keep `SKILL.md` under ~500 lines and move detailed materials into references/scripts. | The current `helix-system/SKILL.md` is too large long-term. It works, but should be refactored into a lightweight router plus references. Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md |
| Anthropic “Define success criteria and build evaluations” | LLM products should define success criteria and build evals to measure performance. | Helix should ship with an executable regression harness for its own test suite. Source: https://platform.claude.com/docs/en/test-and-evaluate/define-success.md |
| ReAct | Interleaving reasoning traces with actions improves grounded problem solving versus pure reasoning or pure acting. | Helix should enforce an observe → decide → act → verify loop, especially for code/research/debugging. Paper: https://arxiv.org/abs/2210.03629 |
| Reflexion | Agents improve by storing verbal reflections from prior trials and using them in later attempts. | Add a disciplined lesson system: “what failed, why, correction, when to apply.” Paper: https://arxiv.org/abs/2303.11366 |
| Voyager | Open-ended agents improve using an automatic curriculum, iterative prompting, and a skill library. | Helix should grow skills from repeated project work and include a curator/eval step before adding new lessons. Paper: https://arxiv.org/abs/2305.16291 |
| Toolformer | Models can learn/use external tools when examples make tool-use valuable and precise. | Add tool-use exemplars: when to search/read/run/screenshot; what not to use tools for. Paper: https://arxiv.org/abs/2302.04761 |
| Cognitive Architectures for Language Agents | Language agents are best understood as architectures combining memory, planning, action, and feedback. | Helix needs architecture, not just instructions: memory store, planner, action loop, evaluator, artifact store. Paper: https://arxiv.org/abs/2309.02427 |
| Multiagent Debate | Multiple agents debating can improve factuality and reasoning. This is a highly relevant MIT-authored paper by Yilun Du, Shuang Li, Antonio Torralba, Joshua Tenenbaum et al. | Add critic/verifier/debate modes for high-stakes research, architecture, and product strategy. Paper: https://arxiv.org/abs/2305.14325 |
| AI Agents That Matter | Agent evals are often misleading; control cost, randomness, baselines, and realistic tasks. | Helix’s eval runner should include cost/time, repeated trials, and baseline comparison, not just “looked good once.” Paper: https://arxiv.org/abs/2407.01502 |
| SWE-agent / SWE-bench | Agent-computer interfaces and realistic issue benchmarks matter for software agents. | Helix coding mode should optimize the interface: repo inspection, narrow tests, issue reproduction, patch validation. Papers: https://arxiv.org/abs/2405.15793 and https://arxiv.org/abs/2310.06770 |
| WebArena / AgentBench | Realistic web/tool environments reveal agent weaknesses missed by static QA. | Helix should test UI/browser/research behavior in realistic tasks, not only text prompts. Papers: https://arxiv.org/abs/2307.13854 and https://arxiv.org/abs/2308.03688 |
| MemGPT | Long-context agents need memory hierarchy and explicit memory management. | Add working memory vs project memory vs long-term lessons, with pruning rules. Paper: https://arxiv.org/abs/2310.08560 |
| System prompt leak repo | Public leaked prompts show common production-agent patterns: tool rules, boundaries, refusal/safety, formatting, and environment-aware behavior. | Use only pattern-level inspiration, not copied proprietary prompts. Helix should be explicit about boundaries, not just taste. Source: https://github.com/asgeirtj/system_prompts_leaks |

---

## What would make Helix materially better

### 1. Replace “one huge skill” with a router skill

**Problem:** the installed Hermes skill embeds almost the whole Helix system. That makes activation reliable, but it is token-heavy and harder to maintain.

**Upgrade:**

```txt
~/.hermes/skills/helix-system/
  SKILL.md                    # <500-line router
  references/
    execution.md
    design.md
    coding.md
    research.md
    critique.md
    verification.md
    handoff.md
    prompt-library.md
    test-suite.md
  scripts/
    helix_eval.py
    helix_init.py
    score_output.py
```

**Why:** Anthropic’s skill guidance recommends progressive disclosure: load the overview first and detailed files only when needed.

**Expected gain:** lower token overhead, fewer instruction conflicts, easier updates.

---

### 2. Add explicit task-mode selection

Right now Helix says “apply coding rules when coding, design rules when design.” Good, but a stronger agent should make mode selection deterministic.

Add this router:

```md
## Helix Mode Router
- Code/debug task → load coding + verification; inspect manifest/config first; require command/test proof.
- UI/design task → load design + verification; require screen job, token check, mobile/desktop visual proof.
- Research task → load research + critique; require decision question, sources opened, findings table, recommendation.
- Strategy task → load product strategy + critique; require user/JTBD/core loop/wedge/MVP/not-doing.
- Prompt task → load prompt library; require role/context/deliverable/constraints/output/verification.
- Handoff task → load handoff; require goal/current state/verification labels/next task/materials.
```

**Expected gain:** fewer missed layers, less generic behavior.

---

### 3. Add evidence-backed progress and completion claims

Anthropic’s Helix guidance specifically warns about fabricated progress and recommends auditing each claim against actual tool results.

Add this rule globally:

```md
Before reporting progress or completion, create an evidence ledger:
| Claim | Evidence from this run | Status |
Only report claims with evidence. If evidence is missing, label it unverified.
```

**Expected gain:** fewer false “done” claims, better trust.

---

### 4. Add fresh-context verifier subagents

Self-critique helps, but separate verifiers are stronger because they see the artifact cold.

Add verifier modes:

| Verifier | Checks |
|---|---|
| Code verifier | Diff scope, correctness, tests, security, no drive-by changes |
| UI verifier | Screenshot/mobile/desktop, hierarchy, clipping, contrast, states |
| Research verifier | Sources opened, citations load-bearing, recommendation follows evidence |
| Handoff verifier | No chat archaeology, clear next task, verification labels |

**Implementation pattern:** use Hermes `delegate_task` for independent verification when stakes are high or after major work.

**Expected gain:** closest upgrade to “Helix-like” quality because it catches confident but wrong output.

---

### 5. Build an executable Helix eval suite

The pack already includes good test prompts. The missing piece is an automated runner.

Add `scripts/helix_eval.py` that:

1. Runs the 10 Helix test prompts.
2. Saves outputs to timestamped files.
3. Scores with the rubric.
4. Compares baseline vs Helix mode.
5. Produces a Markdown report:

```txt
~/.hermes/agents/helix-system/evals/runs/YYYY-MM-DD-HHMM/report.md
```

**Scoring dimensions:** correctness, specificity, tool grounding, scope discipline, verification, design taste, handoff quality.

**Expected gain:** measurable improvement instead of vibes.

---

### 6. Add a repo bootstrapper: `helix-init`

Current repo template has placeholders. Better: inspect the repo and generate a filled `CLAUDE.md`.

`helix-init` should:

1. Detect package manager from lockfile.
2. Read manifest/config.
3. Detect framework/styling/test commands.
4. Find design token files.
5. Fill `CLAUDE.md` with real commands and paths.
6. Merge design section when UI repo detected.
7. Write `.claude/skills/` if Claude Code project skills are desired.

**Expected gain:** Helix becomes usable project-by-project without manual setup.

---

### 7. Add Helix memory/lesson hygiene

Use Reflexion/Voyager/MemGPT patterns, but avoid global memory bloat.

Recommended structure:

```txt
~/.hermes/agents/helix-system/lessons/
  coding/
  design/
  research/
  product/
  handoff/
```

Each lesson:

```md
# <one-line lesson>
Trigger: <when this applies>
Correction: <what to do>
Evidence: <where this was learned>
Expires/review: <date or condition>
```

Rules:

- One lesson per file.
- Update existing lesson instead of duplicating.
- Delete lessons proven wrong.
- Do not save one-off project progress.

**Expected gain:** Helix improves from repeated use without becoming stale or bloated.

---

### 8. Add “assess-only vs execute” boundary

Helix is execution-first, but the best agents avoid unrequested changes.

Add:

```md
If the user is describing, asking, or evaluating, deliver assessment and stop.
If the user asks to build/fix/install/create, execute with tools.
Before destructive/system-changing actions, confirm evidence supports that exact action.
```

**Expected gain:** prevents over-action while preserving execution bias.

---

### 9. Add design-specific “visual proof” workflow

Helix design’s quality depends on rendering, not just taste rules.

Add required UI workflow:

```md
For UI work:
1. State screen job.
2. Identify tokens/components.
3. Implement smallest visual change.
4. Render at ~375px and desktop.
5. Screenshot.
6. Self-critique screenshot against screen job.
7. Patch visual issues.
8. Final: include screenshot path and verification status.
```

**Expected gain:** avoids “pretty code, broken screen.”

---

### 10. Add prompt-output schemas

For recurring deliverables, add schemas so outputs are consistent:

- Product strategy one-pager
- Research report
- UI critique
- Code handoff
- Model-output comparison
- Agent prompt
- Project bootstrap report

Use structured sections or XML-like tags internally when prompts mix many materials.

**Expected gain:** less drift, easier evaluation.

---

## Highest-impact implementation backlog

| Priority | Upgrade | Effort | Impact |
|---:|---|---:|---:|
| 1 | Refactor Helix skill into router + references | Medium | Very high |
| 2 | Add `helix-init` repo bootstrap script | Medium | Very high |
| 3 | Add `helix_eval.py` test runner | Medium | Very high |
| 4 | Add verifier subagent protocols | Low/Medium | Very high |
| 5 | Add evidence ledger completion rule | Low | High |
| 6 | Add mode router | Low | High |
| 7 | Add lessons/memory directory + hygiene rules | Low | Medium/high |
| 8 | Add design visual-proof checklist to runner | Medium | High |
| 9 | Add prompt-output schemas | Low | Medium |
| 10 | Add safety/scope boundary section | Low | Medium |

---

## Proposed v2 file structure

```txt
~/.hermes/agents/helix-system/
  README.md
  agent.md
  MANIFEST.sha256
  references/
    00-operating-contract.md
    01-mode-router.md
    02-evidence-ledger.md
    03-verifier-subagents.md
    04-memory-lessons.md
    execution.md
    design.md
    coding.md
    research.md
    critique.md
    verification.md
    handoff.md
    product-strategy.md
    prompt-library.md
    test-suite.md
  scripts/
    helix_init.py
    helix_eval.py
    score_output.py
    verify_install.py
  templates/
    CLAUDE.md.template
    AGENTS.md.template
    handoff.md.template
    research-report.md.template
  lessons/
    README.md
  evals/
    README.md
```

Hermes skill:

```txt
~/.hermes/skills/helix-system/
  SKILL.md
  references/ -> symlink or copy from agent references
  scripts/ -> symlink or copy from agent scripts
```

---

## What I would change in the installed Helix system next

### Immediate patch

1. Shrink `SKILL.md` into a router.
2. Move embedded layers into `references/`.
3. Add `references/mode-router.md`.
4. Add `references/evidence-ledger.md`.
5. Add `references/verifier-subagents.md`.
6. Add `scripts/verify_install.py`.

### Next build

1. Build `helix_init.py`.
2. Build `helix_eval.py`.
3. Run the Helix eval suite once and save the first benchmark.

### Later

1. Add a dedicated Hermes `helix` profile or launcher that preloads `helix-system`.
2. Add optional cron eval: weekly smoke test against the Helix prompt suite.
3. Add lesson curation workflow.

---

## Caveats

- The linked “system prompts leaks” repo is useful for pattern reconnaissance, but I would not copy leaked proprietary prompts. Use it only to identify common production-agent scaffolding patterns: tool boundaries, safety, formatting, progress, and environment hints.
- Several provided Claude docs are current web docs and were reachable. The `/agents-and-tools/overview` URL was a Not Found page, but the docs index exposed current Agent Skills pages that are more relevant.
- The strongest Helix-like behavior will come less from more instructions and more from **harness design**: tools, verifiers, tests, memory, and evidence checks.

---

## Final verdict

The current Helix System Agent is a strong **A- instruction pack**.

To become an **A+/production-grade agent**, it needs:

- progressive-disclosure skill architecture,
- verifier subagents,
- executable evals,
- repo bootstrap automation,
- evidence-backed completion claims,
- lesson/memory hygiene,
- and visual/browser verification for UI work.

Those changes would make it much closer to the “best agent” pattern shown by the Helix docs, Anthropic’s agent guidance, and the strongest agent research papers.
