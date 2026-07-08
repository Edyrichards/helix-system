# Helix benchmark: agent harnesses, design reasoning, prompt rewriting, orchestration

Date: 2026-07-08. Method: lightweight current benchmark via public web/GitHub metadata and docs excerpts; clean-room synthesis only, no proprietary prompt copying.

## Current best-in-class resources and signals

| Area | Benchmarks / resources | Why they matter for Helix |
|---|---|---|
| Agent harnesses / runtimes | Claude Code (136k stars), OpenAI Codex (96k), LangGraph (36.8k), OpenAI Agents SDK (27.7k), Google ADK (20.5k), Mastra (25.9k), Vercel AI SDK (25.4k) | Winning harnesses combine terminal-native execution, durable state, tool permissions, tracing, human-in-loop, provider-agnostic models, MCP, and easy local/cloud parity. |
| Multi-agent orchestration | CrewAI (55.1k), Microsoft AutoGen (59.6k; now maintenance mode, successor Microsoft Agent Framework), LangGraph, OpenAI Agents SDK, mcp-agent | Market is converging away from “agent swarms” hype toward explicit graph/workflow runtimes, handoffs, subagents-as-tools, and simple composable patterns. |
| Browser / visual agents | browser-use (103k), Stagehand (23.4k), Playwright (92.4k), Browserbase | Browser control is shifting from brittle pure-natural-language actions to hybrid code + natural language + DOM/vision verification. Visual verification is a major trust differentiator. |
| Evaluation / observability | promptfoo (23k), DeepEval (16.7k), OpenAI evals (18.9k), Arize Phoenix (10.5k), Opik (20.4k), LangSmith/openevals | Production agents need regression gates, LLM-as-judge, golden tasks, trace replay, red-team tests, cost/latency/quality metrics, and CI integration. |
| Memory / context | MCP servers (88.2k), GitHub MCP server (31.3k), Graphiti (28.5k), LangGraph memory | Context is becoming an interoperable ecosystem: MCP connectors + durable session state + knowledge graphs for cross-run learning. |
| Prompt engineering / rewriting | OpenAI prompt engineering guide, Anthropic prompt engineering docs, Prompt Engineering Guide, Anthropic “Building Effective Agents” | Best practice is not static magic prompts; it is task decomposition, concrete success criteria, examples, tool affordance design, eval-driven iteration, and input clarification/rewrite loops. |
| UX psychology / design reasoning | NN/g “AI: First New UI Paradigm in 60 Years”, Laws of UX, human-in-loop patterns | AI UX is about shifting locus of control while preserving user agency: progressive disclosure, reversibility, uncertainty surfacing, preview-before-act, familiar mental models, and cognitive load reduction. |
| Agent distribution / marketplace | wshobson/agents (37.6k): 90 plugins, 199 agents, 161 skills, 106 commands, multi-harness source of truth | Distribution is becoming harness-agnostic. A “skill/plugin marketplace” with native adapters for Claude, Codex, Cursor, Gemini, Copilot, etc. can compound faster than a closed app surface. |

## Patterns Helix should implement

### 1) Design Reasoning Engine, not just code generation
- Add a pre-build “design intent model”: user goal, user persona, product context, constraints, emotional tone, accessibility targets, conversion objective, and brand traits.
- Generate an explicit design rationale for every UI decision: hierarchy, affordances, feedback, spacing, motion, copy, and empty/error/loading states.
- Use UX heuristics as first-class checks: Jakob’s Law/familiarity, Hick’s Law/choice reduction, Fitts’s Law/tap target size, Miller/cognitive load, Tesler/conservation of complexity, aesthetic-usability effect, accessibility contrast and keyboardability.
- Store design decisions as structured metadata so later iterations know why an element exists instead of treating the UI as pixels/code only.

### 2) Input re-prompting / prompt rewriting layer
- Before execution, rewrite vague user input into a structured brief: goal, audience, surfaces, data model, style references, constraints, acceptance criteria, and risks.
- Ask clarifying questions only when ambiguity changes the artifact materially; otherwise proceed with assumptions and make them visible.
- Offer a “brief diff”: show what Helix inferred, what it changed, and what it will build.
- Maintain multiple prompt lenses: product manager brief, designer brief, engineer brief, QA brief. Same source request, different optimized internal prompts.
- Add a “negative prompt”/anti-goals section: what not to do, banned patterns, brand exclusions, accessibility pitfalls.

### 3) Visual verification and UI QA loop
- Run built artifacts in a browser, capture screenshots at breakpoints, and compare against intent using a multimodal reviewer.
- Use Playwright-style deterministic assertions plus AI visual critique: alignment, truncation, contrast, overflow, responsive behavior, empty/error/loading states.
- Create a “pixel-to-rationale” trace: each visual issue maps back to design intent and code location.
- Add before/after previews and a user approval checkpoint before destructive or broad changes.
- Maintain reusable visual eval suites by component type: forms, dashboards, landing pages, data tables, onboarding, modals.

### 4) Eval-first agent harness
- Every Helix run should produce: task plan, tool trace, artifacts, screenshots, eval results, cost/latency, and unresolved risks.
- Include golden task suites for common Helix jobs: build landing page, refactor design system, add checkout form, create dashboard, migrate component library.
- Gate merges/build completion on: no runtime errors, no TypeScript/lint errors where applicable, screenshot generated, accessibility smoke test, and core acceptance criteria pass.
- Use regression replay: rerun prior user prompts against new model/prompt versions and compare quality/cost/latency.
- Add human approval for high-risk tool calls and all externally visible deploy/publish actions.

### 5) Multi-agent architecture that avoids swarm chaos
- Use a graph runtime with typed state and explicit handoffs rather than free-form multi-agent chat.
- Recommended roles: Brief Rewriter, Product Strategist, UX Psychologist, Visual Designer, Frontend Engineer, Accessibility QA, Visual Verifier, Release Manager.
- Subagents should be callable tools with bounded inputs/outputs, not autonomous peers endlessly debating.
- Add an arbiter/evaluator node that scores outputs against the structured brief and sends targeted repair tasks.
- Support parallel exploration: generate 2–3 concept directions, score them, then converge into one implementation.

### 6) MCP-native tool ecosystem
- Treat MCP as the integration layer for GitHub, Figma, Linear/Jira, analytics, docs, design systems, screenshot services, and deployment providers.
- Provide safe permission tiers: read-only, branch-local write, browser-only, deploy-preview, production deploy.
- Ship a Helix MCP server so other agent harnesses can call Helix capabilities: design brief rewrite, visual review, component generation, UI eval, design-system lookup.

### 7) Marketplace and distribution
- Build a Helix “skills/components/evals” marketplace, not only templates.
- Marketplace item types: design-system adapters, brand kits, prompt lenses, UI eval packs, Playwright recipes, MCP connectors, industry landing-page packs, accessibility policies, conversion copy packs.
- Make every marketplace item harness-portable: Claude Code, Codex, Cursor, Gemini, Copilot, and Helix-native adapters from a single source format.
- Let agencies and design-system owners publish paid/private packs; this turns Helix into a platform rather than a single generator.

## Differentiators Helix can own

1. **Design psychology compiler**: converts user/product intent into concrete UI heuristics and measurable checks.
2. **Prompt-to-brief transparency**: users see and edit the structured brief before the agent acts.
3. **Visual proof, not textual claims**: every UI change ships with screenshot evidence and visual/accessibility evals.
4. **Design rationale memory**: Helix remembers the “why” behind design choices across sessions and branches.
5. **Agentic distribution layer**: Helix skills can run inside other harnesses, bringing Helix to where developers already work.
6. **Eval packs as moat**: quality improves through domain-specific, reusable UI/product eval suites rather than model choice alone.

## GTM implications

- **Positioning:** “The design-aware agent harness for production UI” is stronger than “AI website builder.” Compete on trust, taste, evals, and workflow integration.
- **Beachhead:** teams with existing React/Next/design-system repos that need safe, reviewable UI automation; agencies and internal tools teams are likely early adopters.
- **Wedge product:** free visual UI reviewer / prompt-to-brief tool that outputs actionable issues and patches; upgrade to autonomous implementation, eval gates, and team memory.
- **Enterprise value:** audit trails, permissioning, private marketplace, design-system enforcement, eval dashboards, VPC/self-hosted runners, compliance logs.
- **Community motion:** open-source Helix eval packs and MCP server; paid cloud for screenshots, traces, marketplace hosting, collaboration, and regression suites.
- **Marketplace economics:** share revenue with component/design-system/prompt/eval creators; make Helix the distribution channel for high-quality agent skills.
- **Trust messaging:** emphasize “preview, verify, approve” and “agent output with evidence” to reduce buyer fear of autonomous code/design changes.

## Recommended roadmap

### 0–30 days
- Implement structured brief rewriting with assumption visibility.
- Add screenshot capture and basic visual/accessibility checks to every UI run.
- Introduce run artifacts: plan, trace, diffs, screenshots, eval summary.
- Create 10 golden UI tasks and CI regression runner.

### 30–60 days
- Add design psychology/rationale engine and design-decision memory.
- Add multi-agent graph: brief → design → build → visual verify → repair → final.
- Build MCP connectors for GitHub, Figma/design tokens, Playwright/browser, issue tracker.
- Launch private beta with teams using real repos/design systems.

### 60–90 days
- Release Helix MCP server and harness adapters.
- Launch marketplace MVP: brand kits, eval packs, design-system adapters, prompt lenses.
- Add team dashboards for quality, cost, latency, visual regressions, and acceptance-rate metrics.
- Publish public benchmark: Helix vs generic coding agent on UI tasks with screenshots and eval rubric.

## Source notes

GitHub signals checked: Claude Code, OpenAI Codex, browser-use, Playwright, LangGraph, CrewAI, Microsoft AutoGen/Agent Framework note, OpenAI Agents SDK, Google ADK, Mastra, Vercel AI SDK, Stagehand, promptfoo, Opik, DeepEval, Phoenix, OpenAI evals, MCP servers, GitHub MCP server, Graphiti, wshobson/agents.

Public docs/articles checked: Anthropic Building Effective Agents; Anthropic Claude Code best practices; Anthropic test/evaluate success criteria; OpenAI prompt engineering guide; Prompt Engineering Guide; NN/g AI paradigm; Laws of UX.
