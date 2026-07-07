# Helix UI Design Autonomy Repo Patterns

Use this reference when improving Helix's UI/UX generation system, especially when the goal is to compete with Claude Design, v0, Lovable, Bolt, or agentic Figma workflows.

## Source hygiene
- Study repositories for architecture and workflows, not copyable prose.
- Prefer MIT/Apache/ISC repos for direct code study.
- Treat GPL/AGPL/no-license repos as pattern inspiration only unless the user explicitly approves license obligations.
- Keep Helix runtime rules original and Hermes-native.

## High-leverage repo patterns

| Pattern | Repos to study | Helix adaptation |
|---|---|---|
| Vision-to-code conversion | `abi/screenshot-to-code`, `emilwallner/Screenshot-to-code` | Add screenshot/Figma/screen-recording intake, then generate structured design DNA before writing UI. |
| Conversational UI preview | `wandb/openui`, `SujalXplores/v0.diy`, `21st-dev/magic-mcp` | Make every design generation runnable with live preview, revision, and export path. |
| Full app generation loop | `dyad-sh/dyad`, `stackblitz/bolt.new`, `AntonOsika/gpt-engineer` | Pair UI generation with package install, run, edit, and deployment-aware verification. |
| Figma read/write bridge | `grab/cursor-talk-to-figma-mcp`, `vkhanhqui/figma-mcp-go`, `TranHoaiHung/figma-ui-mcp` | Treat Figma as a live tool: read tokens/components, write frames/prototypes, verify output on canvas. |
| Design-system enforcement | `natdexterra/work-with-design-systems`, `senlindesign/claude2figma`, `redongreen/uSpec` | Add audits for token binding, component instances, state matrices, WCAG, component descriptions, and Storybook parity. |
| Component registry context | `shadcn-ui/ui`, `Jpisnice/shadcn-ui-mcp-server`, `magicuidesign/mcp`, `21st-dev/magic-mcp` | Retrieve exact component code/demos from registry context instead of hallucinating component APIs. |
| Canvas-native design workspace | `tldraw/tldraw`, `plasmicapp/plasmic`, `BuilderIO/builder` | Add spatial/canvas planning for layouts, variant comparison, and user-editable design artifacts. |
| Visual evaluation | `storybookjs/storybook`, `microsoft/playwright-mcp`, `browser-use/browser-use` | Screenshot every variant at desktop/mobile, check console/overflow/interactions, produce contact sheets, then repair. |

## Helix autonomous design loop

1. **Intake**: collect brief, screenshots, URLs, Figma link, repo state, brand assets, competitor examples.
2. **Design DNA extraction**: infer tokens, typography, components, layout families, content voice, motion language, anti-patterns.
3. **Variant tournament**: generate 3-5 materially different directions. Each declares design read, tokens, component sources, interaction map, and risk.
4. **Render**: create standalone HTML/React prototype or repo-integrated route. If reusable components are involved, create Storybook stories.
5. **Visual verify**: screenshot desktop/mobile, check console, measure horizontal overflow, smoke-test primary interactions.
6. **Critic pass**: apply Helix anti-slop rubric, WCAG, visual hierarchy, copy audit, and AI-tell detector.
7. **Repair loop**: patch concrete defects, rerender, rescore. Do not stop at first plausible output.
8. **Handoff**: report changed files, screenshot paths, exact verification, remaining decisions, and next implementation map.

## What would make Helix boundary-breaking

- **Multi-agent design jury**: separate visual critic, accessibility critic, conversion critic, code critic, and brand critic.
- **Design memory per project**: keep design DNA, winning variants, rejected tells, preferred palettes, component decisions, and screenshot evidence.
- **Bidirectional parity**: keep Figma, repo tokens, component registry, Storybook states, and screenshots synchronized.
- **Autonomous visual tournaments**: generate many directions, score them, combine strongest parts, and repair before user sees them.
- **Evidence-backed design claims**: every “better” claim links to screenshot, rubric score, component state, or source artifact.

## Shortlist for hands-on study

1. `abi/screenshot-to-code`
2. `wandb/openui`
3. `dyad-sh/dyad`
4. `stackblitz/bolt.new`
5. `grab/cursor-talk-to-figma-mcp`
6. `vkhanhqui/figma-mcp-go`
7. `TranHoaiHung/figma-ui-mcp`
8. `natdexterra/work-with-design-systems`
9. `senlindesign/claude2figma`
10. `marvkr/better-design`
11. `redongreen/uSpec`
12. `shadcn-ui/ui`
13. `Jpisnice/shadcn-ui-mcp-server`
14. `magicuidesign/mcp`
15. `tldraw/tldraw`
16. `storybookjs/storybook`
17. `microsoft/playwright-mcp`
18. `browser-use/browser-use`

## Completion rule for design-autonomy work

Use: `Verified: screenshots + console/overflow/interactions + rubric score`.
If no browser render occurred, say: `Implemented, unverified: visual render not completed`.
