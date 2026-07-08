# Helix Go-To-Market Plan

## Positioning

**Helix is the self-improving design-and-execution operating system for AI coding agents.**

It turns Claude, Codex, Cursor, Hermes, and similar tools from smart chat assistants into disciplined execution partners: intake → reprompt → specialist swarm → verified artifact → lessons → self-improvement.

## Category

Not a prompt pack.  
Not another agent framework.  
Not a UI template library.

**Category claim**: Agent Operating System for verified product/design execution.

## Why now

The market has three visible buckets:

1. **Agent frameworks** (AutoGen, CrewAI, LangGraph, OpenAI Agents): powerful orchestration, but developer-heavy and not opinionated about design quality.
2. **Agent/persona collections** (agency-agents): excellent specialist breadth and distribution, but limited global verification and self-improvement.
3. **AI design/code tools** (Claude Code, Cursor, Lovable, v0, etc.): powerful host environments, but quality depends heavily on prompting and verification discipline.

Helix sits across them: a portable discipline layer that makes any host agent reason, reprompt, design, verify, and improve.

## Wedge

**Best-in-class AI design reasoning + psychology + prompt reprompting.**

Lead with the problem people feel immediately:

> "AI can make screens, but most outputs are generic, psychologically shallow, and hallucinate around unclear briefs. Helix turns vague intent into a professional design brief, reasons through the user's psychology, generates verified design artifacts, and improves itself after each run."

## Ideal Customer Profiles

### ICP 1: Founder / indie hacker building products with Claude Code or Cursor
Pain:
- knows what they want but struggles to prompt precisely
- gets generic UI
- wastes time manually checking layout bugs

Promise:
- "Say it roughly. Helix reprompts it professionally and ships verified product/design work."

### ICP 2: Design engineer / frontend lead
Pain:
- AI output looks templated
- lacks design system discipline
- needs real screenshots and acceptance checks

Promise:
- "Design-system-first UI with psychology, real screenshots, and pre-flight gates."

### ICP 3: AI power user / agent builder
Pain:
- prompt packs don't verify
- frameworks require too much glue
- wants portable agent behavior across Claude/Codex/Hermes

Promise:
- "A portable, self-improving harness that makes your favorite agent tool behave like a senior execution team."

### ICP 4: Agencies / consultants
Pain:
- need repeatable quality and handoffs
- multiple AI tools in use
- client deliverables need evidence

Promise:
- "Repeatable AI delivery system with evidence ledgers, design proofs, and swarms."

## Messaging Pillars

### 1. Reprompting
"You don't need to prompt like an expert. Helix turns rough intent into a professional brief."

Proof assets:
- before/after prompt examples
- `scripts/helix_reprompt.py`
- `references/12-prompt-reprompt-engine.md`

### 2. Design Psychology
"Helix designs around behavior, trust, motivation, friction, and conversion, not just aesthetics."

Proof assets:
- `10-design-reasoning-engine.md`
- `11-advanced-design-psychology.md`
- UX psychology scoring rubric
- example onboarding rewrite

### 3. Verified Visual Output
"No more claiming design quality from code. Helix renders and checks."

Proof assets:
- Playwright desktop/mobile screenshots
- contact sheets
- console + overflow checks

### 4. Specialist Swarms
"Researcher, designer, reviewer, and verifier working in parallel under one coordinator."

Proof assets:
- `09-swarm-orchestration.md`
- personas catalog
- `scripts/helix_swarm.py`

### 5. Self-Improvement
"Helix can audit and upgrade itself with evidence."

Proof assets:
- `07-self-improvement.md`
- `helix_self_improve.py`
- lessons directory

## Competitive Positioning

| Alternative | Strength | Weakness | Helix angle |
|---|---|---|---|
| agency-agents | huge specialist roster + installers | static prompts, weak global verification | smaller elite roster + OS discipline + self-improvement |
| AutoGen/CrewAI/LangGraph | powerful orchestration | developer-heavy, not design-specialized | portable rules + scripts for real product/design output |
| Claude Code/Cursor alone | great host model/tooling | quality depends on user prompting | Helix gives Claude a spine |
| v0/Lovable | fast UI generation | generic design, shallow psychology | Helix designs why before building what |
| Prompt packs | easy to copy | no evals, no proof, no learning | Helix includes proof and continuous improvement |

## Product Packaging

### Free/Public Repo
- portable core
- quickstart
- elite personas
- design reasoning docs
- reprompt helper
- swarm helper
- sample evals/screenshots

### Future Premium Possibilities
- desktop installer/catalog app
- hosted persona marketplace
- private design-tournament runners
- team lessons/evidence dashboard
- premium design psychology packs
- client-ready design audit reports

## Launch Narrative

**Title ideas**
- "Helix: The AI Agent OS for Design-Grade Product Execution"
- "Stop Prompting. Start Reprompting."
- "A self-improving design agent harness for Claude Code and Cursor"

**Core launch story**
1. AI can code, but outputs still fail because the brief is vague and verification is weak.
2. Helix starts with intake and reprompting, so the model understands the professional version of the user's intent.
3. It applies design reasoning and psychology, not just UI polish.
4. It dispatches specialists and verifiers like a real team.
5. It proves work with screenshots/evidence and improves itself over time.

## Demo Scenarios

### Demo 1: Vague onboarding input → professional design brief
Input: "make onboarding better"
Output:
- targeted clarifying questions or reprompted brief
- behavioral hypothesis
- psychology map
- revised flow

### Demo 2: Design tournament
Show:
- two/three variants
- contact sheet
- scoring rubric
- winner + reasons

### Demo 3: Swarm mode
Goal: "Create a checkout redesign with research, design, implementation, and verification."
Show:
- Coordinator decomposition
- Research + Design + Code Review branches
- jury verification
- master evidence ledger

### Demo 4: Self-improvement
Show Helix auditing its own prompt intake and producing a patch + lesson.

## Distribution Channels

1. **GitHub**
   - polished README
   - badges
   - screenshots/contact sheets
   - persona catalog table
   - install snippets
   - examples directory

2. **X / LinkedIn build-in-public**
   - before/after prompts
   - screenshot proof
   - "AI design tell" threads
   - swarm diagrams

3. **Hacker News / Reddit**
   - focus on practical portability and evidence, not hype
   - title example: "I built a portable agent OS that reprompts vague requests and verifies UI with screenshots"

4. **Claude/Cursor communities**
   - "Drop this into Claude Code and get better design reasoning"
   - simple quickstart

5. **Agency-agents comparison audience**
   - respectful: "They nailed specialist catalogs; Helix adds an execution OS layer."

## 30 / 60 / 90 Plan

### First 30 days
- Finish design intelligence and reprompting docs/scripts.
- Add persona catalog page.
- Create examples/ with at least 3 end-to-end demos.
- Produce screenshots/contact sheets as proof.
- Improve README to be public launch-ready.

### 60 days
- One-command installer / converter.
- Hermes lazy-router or catalog-style loader.
- More elite personas (Conversion Psychologist, Prompt Architect, Design Jury Lead, GTM Strategist).
- Public launch thread + HN/Reddit post.

### 90 days
- Desktop/web catalog app concept.
- Hosted examples and documentation site.
- Community contribution guide.
- Benchmark suite against baseline Claude/Cursor prompts.

## Metrics

| Funnel stage | Metric |
|---|---|
| Awareness | GitHub stars, repo visits, launch post impressions |
| Activation | clones, quickstart opens, script runs |
| Value | generated screenshot/evidence artifacts, successful installs |
| Retention | repeat self-improvement/eval runs, new lessons |
| Community | issues, PRs, persona contributions |

## Immediate GTM Requirements Before Public Push

- [ ] README hero rewritten around reprompting + design reasoning + proof.
- [ ] `examples/` with real before/after artifacts.
- [ ] Persona catalog visible in docs.
- [ ] Install instructions under 2 minutes.
- [ ] Screenshots/contact sheet linked.
- [ ] Respectful competitor comparison.
- [ ] Clear license decision.

## Tagline Bank

- The self-improving design agent OS.
- Claude's missing execution spine.
- Reprompt vague intent into verified product work.
- Design psychology, specialist swarms, proof-first delivery.
- The agent harness for people who care whether the output actually works.
