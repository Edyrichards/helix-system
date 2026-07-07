# Helix UI Autonomy GitHub Research

Decision question: Which repositories should Helix study to scale autonomous UI/UX generation?

Generated: 2026-07-08T00:47:04

## Findings

| Repo | Stars | License | Helix score | Why it matters |
|---|---:|---|---:|---|
| [mikesheehan54/Claude-Code-Design-AI](https://github.com/mikesheehan54/Claude-Code-Design-AI) | 76 | MIT License | 65.97 | Claude Design: AI UI/UX architect. Screenshot to React, Figma components, Tailwind CSS generator. Prototyping agent, design systems, wireframe renderer. SVG icon creator, dark mode toggle, responsive layout tool. Front-end code export, shadcn/ui integration, vector assets, branding assistant. |
| [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) | 73186 | MIT License | 62.39 | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [marvkr/better-design](https://github.com/marvkr/better-design) | 165 | MIT License | 52.04 | 🎨 Open-source design MCP server + shadcn/ui registry — AI design systems for Claude Code, Cursor, Codex, GitHub Copilot & any MCP client. 31 brand-grade themes (Linear, Stripe, Vercel, Notion, Apple, Supabase, Figma…) + design tokens, UI principles & WCAG rules. Install any component with one command. |
| [grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp) | 6882 | MIT License | 47.66 | TalkToFigma: MCP integration between AI Agent (Cursor, Claude Code, Codex) and Figma, allowing Agentic AI to communicate with Figma for reading designs and modifying them programmatically. |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 141651 | GNU General Public License v3.0 | 46.6 | FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models |
| [creativetimofficial/ui](https://github.com/creativetimofficial/ui) | 11945 | MIT License | 45.84 | Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs. |
| [redongreen/uSpec](https://github.com/redongreen/uSpec) | 228 | MIT License | 45.67 | Generate design system documentation for your UI components, directly from your AI agent. Renders into Figma or a portable .md file. Works with Cursor, Claude Code, and Codex. |
| [emilwallner/Screenshot-to-code](https://github.com/emilwallner/Screenshot-to-code) | 16482 | Other | 42.65 | A neural network that transforms a design mock-up into a static website. |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | 20853 | Other | 42.37 | Local, open-source AI app builder for power users ✨ v0 / Lovable / Replit / Bolt alternative 🌟 Star if you like it! |
| [TranHoaiHung/figma-ui-mcp](https://github.com/TranHoaiHung/figma-ui-mcp) | 216 | MIT License | 41.82 | AI can draw UI directly on the Figma canvas via JavaScript, and read existing designs back as structured data. Works with Claude Code, Cursor, VS Code, and Windsurf. No API KEY required. |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | 48609 | Other | 40.04 | Build infinite canvas apps in React with the tldraw SDK. World's best, top-most agent recommended #1 five star SDK. |
| [senlindesign/claude2figma](https://github.com/senlindesign/claude2figma) | 174 | MIT License | 39.77 | An enforcement layer for Claude Code + Figma — 4 skills that keep AI on your Design System rails. Components stay linked, tokens stay bound, nothing goes off-spec. |

## Patterns

- High-value design agents combine **generation**, **preview**, **visual verification**, and **repair**, not just prompt-to-code.
- The strongest UI autonomy signals are screenshot/Figma intake, MCP-based Figma read/write, component registry retrieval, Storybook/Playwright verification, and canvas workspaces.
- Component systems need enforcement: tokens, variants, accessibility states, and component anatomy must be checked mechanically.

## Gaps

- Most repos cover only one lane: generator, Figma bridge, component registry, or visual test harness.
- Few systems run multi-variant design tournaments with screenshot-backed scoring and automated repair.
- Few systems preserve parity between Figma, repo tokens, component docs, Storybook states, and rendered screenshots.

## Recommendation

Study `mikesheehan54/Claude-Code-Design-AI, abi/screenshot-to-code, marvkr/better-design, grab/cursor-talk-to-figma-mcp, x1xhlol/system-prompts-and-models-of-ai-tools, creativetimofficial/ui` first, then evolve Helix into a design operating loop: intake real visual/context sources, extract design DNA, generate multiple variants, render them, screenshot them, score them against Helix's rubric, repair the winner, and hand off with evidence.
