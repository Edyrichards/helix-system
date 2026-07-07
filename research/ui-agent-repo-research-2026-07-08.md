# Helix Research: GitHub repos to scale autonomous UI/UX generation

Decision question: Which GitHub repos should Helix study or integrate from to become an autonomous design-generation agent on par with Claude Design and beyond?

Date: 2026-07-08

## Method

- Searched GitHub with authenticated `gh search repos` across screenshot-to-code, AI app builder, v0/Lovable/Bolt alternatives, Figma MCP, design-system AI, shadcn MCP, Magic UI, and Claude Design queries.
- Fetched repo metadata and README signals for shortlisted repos with `gh repo view` and `gh api repos/<owner>/<repo>/readme`.
- Saved raw evidence to:
  - `github-ui-agent-repos-expanded.json`
  - `ui-agent-repo-readme-signals.json`

## Findings

| Repo | Stars | License | Approach | Strength to steal | Caution / gap |
|---|---:|---|---|---|---|
| [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) | 73,186 | MIT | Screenshot/Figma/screen-recording to HTML, Tailwind, React, Vue, Ionic | Vision-to-code pipeline, multi-output targets, live preview feedback loop | Primarily conversion, not taste/evaluation orchestration |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | 20,853 | Other | Local open-source AI app builder, v0/Lovable/Replit/Bolt alternative | Local-first app-generation UX, power-user workflow | License needs review before code reuse |
| [wandb/openui](https://github.com/wandb/openui) | 22,453 | Apache-2.0 | Natural-language UI description with live rendered preview and conversion to React/Svelte/Web Components | Tight describe → render → revise loop | Less polished than v0 by its own README; likely useful architecturally |
| [stackblitz/bolt.new](https://github.com/stackblitz/bolt.new) | 16,446 | MIT | Full-stack browser IDE powered by WebContainers | Install/run/edit/deploy loop inside generation workflow | More full-stack agent than design-specific |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | 48,609 | Other | Infinite canvas React SDK with agent/canvas workflows | Canvas as design workspace; agents can read/modify visual state | License/trademark constraints need review |
| [grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp) | 6,882 | MIT | MCP bridge between coding agents and Figma via plugin/WebSocket | Programmatic read/write Figma loop for agentic design | Requires Figma Desktop/plugin setup |
| [vkhanhqui/figma-mcp-go](https://github.com/vkhanhqui/figma-mcp-go) | 1,286 | MIT | Figma MCP via plugin, no REST token/rate limit, 73 tools | Full read/write styles, variables, components, prototypes | Smaller ecosystem; must test reliability |
| [TranHoaiHung/figma-ui-mcp](https://github.com/TranHoaiHung/figma-ui-mcp) | 216 | MIT | AI draws UI directly on Figma canvas and reads structured data | Code-like `figma_write` / `figma_read` loop; direct visual artifact creation | Lower stars but highly relevant |
| [natdexterra/work-with-design-systems](https://github.com/natdexterra/work-with-design-systems) | 47 | MIT | Claude Code design-system audits/builds for Figma, WCAG, scoring, token sync | Readiness scoring, component-state matrix, Figma-to-code token loop | Low-star but conceptually excellent for Helix |
| [senlindesign/claude2figma](https://github.com/senlindesign/claude2figma) | 174 | MIT | Claude Code + Figma enforcement skills for token-bound components | Preflight enforcement: instances, variables, no raw values | Skill pack, not an app framework |
| [marvkr/better-design](https://github.com/marvkr/better-design) | 165 | MIT | Open Claude Design-style MCP with themes, tokens, UI principles, WCAG review | Brand-grade design systems as MCP context; output review rules | Young project; validate quality before adopting rules |
| [redongreen/uSpec](https://github.com/redongreen/uSpec) | 228 | MIT | Agent-generated component design-system docs in Markdown/Figma | Component anatomy/spec extraction as artifact | Needs pairing with actual renderer/eval loop |
| [gabelul/stitch-kit](https://github.com/gabelul/stitch-kit) | 35 | Apache-2.0 | Design superpowers for coding agents via Google Stitch MCP, 35 skills, framework targets | Multi-layer design workflow: ideation, batch gen, iteration, conversion | Depends on Google Stitch auth/MCP |
| [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills) | 442 | Unknown | Agent skill pack for design tokens, WCAG, components, many design systems | Token architecture and broad design-system knowledge layer | No detected license in metadata, do not copy without review |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 118,361 | MIT | Open-code component distribution platform | Registry/open-code model; customize components instead of opaque package dependency | Table stakes, not autonomous by itself |
| [Jpisnice/shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server) | 2,835 | MIT | MCP context server for shadcn component code/demos across frameworks | Agents can retrieve exact component code, demos, install info | Should be treated as context provider, not design brain |
| [magicuidesign/mcp](https://github.com/magicuidesign/mcp) | 192 | MIT | Official Magic UI MCP for searchable/installable animated components | High-polish component retrieval inside agent workflow | Component-source dependency, not autonomous evaluation |
| [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) | 5,343 | No detected license | v0-like component generation in Cursor/Windsurf/Cline | `/ui` workflow, real-time preview, component library | No detected license; use as integration if already configured, not code source |
| [storybookjs/storybook](https://github.com/storybookjs/storybook) | 90,508 | MIT | Component workshop/test/documentation environment | Isolated UI examples, regression/testing hub | Heavy; use selectively for Helix design evals |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 34,808 | Apache-2.0 | Browser automation via MCP | Visual verification, screenshot loop, interaction proof | Not design generation, but critical for proof |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 103,326 | MIT | Browser automation for AI agents | Competitor/site research, form workflows, visual browsing | Adds browsing capability, not design taste |
| [plasmicapp/plasmic](https://github.com/plasmicapp/plasmic) | 6,900 | MIT | Visual builder for React/codebases | Bring-your-own-components visual authoring, variants/slots | Product ecosystem, heavier than a Helix internal loop |
| [BuilderIO/builder](https://github.com/BuilderIO/builder) | 8,763 | MIT | Visual development SDKs/plugins/examples | Figma-to-code, visual CMS, component drag/drop | Platform-first; learn architecture, avoid dependency unless needed |

## Patterns: table stakes for Helix

1. **Closed visual loop**: prompt → render → screenshot → critique → patch → re-render. OpenUI, screenshot-to-code, Playwright MCP, and Storybook all point to this.
2. **Figma is a first-class tool, not a handoff**: Figma MCP repos show agents should read tokens/components and write real frames/prototypes.
3. **Component registry retrieval beats memory**: shadcn MCP, Magic UI MCP, 21st.dev, and Creative Tim UI all use searchable/installable component sources.
4. **Design-system compliance needs enforcement**: claude2figma and work-with-design-systems explicitly prevent raw values, detached components, missing states, and token drift.
5. **Canvas matters for autonomous design**: tldraw/Plasmic/Builder prove design generation should not be only text-to-code; agents need a spatial/visual workspace.
6. **Artifacts must be runnable**: Bolt/Dyad show the user experience should include install/run/preview/deploy rather than static generated code.
7. **Evaluation must be visual, not prose**: Storybook, Playwright MCP, visual regression studios, and Helix’s screenshot rule all converge on screenshot-backed evaluation.

## Gaps Helix can exploit

1. **Taste + enforcement + autonomy rarely coexist.** Most repos are either generators, component libraries, Figma bridges, or eval tools. Few combine all four into a single autonomous design loop.
2. **Most AI UI generators lack a strong anti-slop design critic.** They generate plausible UI but do not enforce typography, content, motion, visual hierarchy, or AI-tell bans deeply.
3. **Figma/code parity is still weak.** Repos can write to Figma or write code, but few maintain bidirectional parity between Figma tokens/components, repo components, Storybook states, and screenshots.
4. **Design memory is immature.** Few systems build a reusable project-specific design DNA from screenshots, competitors, tokens, generated variants, user picks, and failed evals.
5. **Autonomous iteration is shallow.** Most loops stop after one preview. Helix can run multi-round visual tournament generation, score variants, repair defects, and save winning patterns.

## Recommendation

Build Helix UI/UX autonomy as a **design operating loop**, not just another text-to-component generator. The immediate stack should combine: screenshot-to-code style vision ingestion, OpenUI-style live render/revise, Figma MCP read/write, shadcn/Magic/21st registry retrieval, Storybook/Playwright visual evaluation, and Helix’s anti-slop design critic. Do not copy source from copyleft/unknown-license repos; use MIT/Apache repos for direct study and use the rest as pattern inspiration only.

## Shortlist for hands-on cloning/study

### Tier 1: study deeply now

1. `abi/screenshot-to-code` - conversion pipeline and preview loop.
2. `wandb/openui` - conversational UI rendering architecture.
3. `grab/cursor-talk-to-figma-mcp` - Figma bridge pattern.
4. `vkhanhqui/figma-mcp-go` or `TranHoaiHung/figma-ui-mcp` - no-token plugin-based Figma read/write.
5. `shadcn-ui/ui` + `Jpisnice/shadcn-ui-mcp-server` - open component registry + MCP context retrieval.
6. `storybookjs/storybook` + `microsoft/playwright-mcp` - component and screenshot verification loop.
7. `tldraw/tldraw` - canvas-native agent workspace pattern.

### Tier 2: inspect for specialized mechanisms

1. `natdexterra/work-with-design-systems` - scoring/audit model.
2. `senlindesign/claude2figma` - token/instance preflight enforcement.
3. `marvkr/better-design` - Claude Design-like MCP context packaging.
4. `redongreen/uSpec` - component anatomy/spec generation.
5. `plugin87/ux-ui-agent-skills` - broad design token/component skill taxonomy, license permitting.
6. `plasmicapp/plasmic` and `BuilderIO/builder` - visual builder integration models.

## Proposed Helix architecture upgrade

```text
Helix Design Autonomy
  1. Intake
     - brief, screenshots, URLs, Figma file, repo state, competitor examples
  2. Design DNA extraction
     - tokens, typography, components, content voice, layout families, motion language
  3. Variant tournament
     - generate 3-5 materially different UI directions
     - each direction must declare design read, tokens, component sources, interaction map
  4. Rendering lane
     - standalone HTML/React prototype or repo-integrated route
     - Storybook stories for reusable components
  5. Visual verification lane
     - desktop/mobile screenshots
     - console check, overflow check, interaction smoke tests
  6. Critic lane
     - Helix anti-slop rubric, WCAG, visual hierarchy, copy audit, AI-tell detector
  7. Repair loop
     - patch concrete issues, re-render, re-score
  8. Handoff/build lane
     - files changed, active components, screenshots, remaining decisions, next implementation map
```

## Next implementation moves

1. Add a Helix reference: `ui-design-autonomy-repo-patterns.md` with the above architecture and shortlisted repos.
2. Add a script: `scripts/helix_design_research.py` to search GitHub, fetch repo metadata/README signals, and update this report.
3. Add a design-eval harness mode: generate N variants, screenshot each at desktop/mobile, produce a contact sheet, run rubric scoring, and pick/repair the winner.
4. Add optional MCP integration notes for Figma, shadcn, Magic UI, 21st.dev, Storybook, and Playwright.
5. Keep all borrowed material clean-room: no copying text/code from unknown/GPL/AGPL repos into Helix runtime.
