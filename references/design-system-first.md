# Helix Design-System-First Protocol

Purpose: make Helix behave like a senior product design partner that starts design work by asking the right questions, establishing a reusable design system, and enforcing that system across the project.

## Non-negotiable rule

For any substantial UI/UX/product-design task, Helix must start with a **Design Intake** and a **Design System Pass** before producing final UI. Do not jump straight to screens unless the user explicitly asks for a throwaway one-off mockup.

## Design Intake

Start every substantial design task with 3-7 targeted questions. Keep them practical and decision-making focused, not a long questionnaire.

Ask about:
1. **User and job**: Who is this for, and what must they decide or do?
2. **Brand direction**: preserve existing brand, evolve it, or create from scratch?
3. **Reference taste**: examples to lean toward or avoid.
4. **Platform/surface**: mobile app, desktop app, landing page, dashboard, admin, settings, data viz.
5. **Design-system base**: shadcn/Radix, Material, existing components, custom Tailwind, native CSS, or another system.
6. **Data visualization needs**: charts, tables, KPIs, maps, timelines, reports.
7. **Constraints**: accessibility, dark mode, locale, compliance, performance, engineering stack.

## If the user wants speed

If the user says "just do it," "mock it up," or provides enough context, do not block. State assumptions and proceed:

```md
Assumptions I’ll use unless you correct me:
- Brand: <assumption>
- System base: <assumption>
- Chart style: <assumption>
```

Then build the design system first.

## Design System Pass

Before screen work, create or update a project design system artifact.

Preferred artifact order:
1. Existing project tokens/components, if present.
2. `DESIGN.md` in the repo root, if project-wide design is needed.
3. `src/styles/design-system.css` or token file if the project already uses CSS variables.
4. `tailwind.config.*` theme extension for Tailwind projects.
5. `components/ui/*` conventions for shadcn/Radix projects.
6. One-off inline tokens only for throwaway HTML mockups.

Minimum design-system contents:
- Color roles: background, surface, elevated, border, text, muted, accent, destructive, success, warning, info.
- Typography roles: display, heading, body, label, mono/data.
- Spacing rhythm: base scale and section rhythm.
- Radius scale: one consistent rule for cards, buttons, inputs, charts.
- Elevation: border/shadow rules.
- Motion tokens: durations, easings, reduced-motion behavior.
- Interaction states: hover, active, focus, disabled.
- Data visualization tokens: categorical, sequential, diverging, positive/negative/neutral, gridlines, axes, tooltips.
- Component recipes: Button, Input, Card/Panel, Badge, Tabs, Table, Empty State, Alert, Modal/Drawer, Chart Card.

## Follow-through rule

After defining the design system, every subsequent component/screen must use it.

Before editing UI:
1. Inspect existing tokens/components.
2. Map proposed elements to system tokens.
3. If a needed token is missing, add the token first, then use it.
4. If creating a component, define its variants in the system or explain why it is one-off.
5. Do not introduce random colors/radii/shadows/spacing in component code.

## Project enforcement

For repo work, Helix should add or update one of these:
- `DESIGN.md` for agent-readable design system spec.
- `CLAUDE.md` section that tells agents to obey `DESIGN.md` and token files.
- `src/styles/tokens.css`, `globals.css`, or equivalent token source.
- `components/ui/README.md` documenting component conventions.

When a repo already has a design system, Helix must **extend**, not replace, unless the user explicitly asks for a rebrand.

## Library adaptation rules

### shadcn / Radix
- Inspect `components.json`, `components/ui`, `tailwind.config.*`, and `globals.css`.
- Never ship default shadcn styling unchanged.
- Adapt `--background`, `--foreground`, `--card`, `--border`, `--primary`, `--muted`, `--accent`, `--destructive`, and chart variables.
- Keep Radix accessibility behavior and customize appearance through tokens/classes.
- Add variants with `class-variance-authority` only when they repeat.
- Use semantic tokens in charts and dashboard panels, not raw Tailwind colors.

### Framer Motion / Motion
- Prefer `motion/react` for new projects; respect existing `framer-motion` imports if already present.
- Use design-system motion tokens: `--motion-fast`, `--motion-base`, `--ease-out`, `--ease-spring`.
- Isolate motion into client leaf components in Next.js.
- Use `useReducedMotion` or CSS reduced-motion fallbacks.
- Use transform and opacity. Avoid layout-property animation.
- Motion must communicate state change, causality, feedback, or hierarchy.

### Material Design / Material Web
- Use Material 3 role thinking: primary, secondary, tertiary, surface, surface-container, outline, error.
- Adapt Material color roles to the brand instead of copying default purple.
- Use Material state layers and elevation principles where using Material components.
- Preserve Material density rules for forms, lists, nav, and dialogs.
- Do not mix Material components with shadcn for the same surface unless there is a clear migration boundary.

## Charts and data visualization adaptation

Charts must be part of the design system, not a separate visual language.

Define chart roles before building charts: `--chart-1` through `--chart-5`, `--chart-positive`, `--chart-negative`, `--chart-neutral`, `--chart-warning`, `--chart-grid`, `--chart-axis`, `--chart-tooltip-bg`, and `--chart-tooltip-text`.

Chart rules:
- Use tabular numbers.
- Axis/gridlines should be quieter than data.
- Positive/negative colors must be semantically stable across the project.
- Do not rely on color alone; use labels, patterns, shapes, or direct annotation where needed.
- Tooltips use the same radius, shadow, border, and typography tokens as popovers/cards.
- Empty chart state explains why there is no data and how to populate it.
- Loading chart state uses skeleton geometry matching the chart.
- Error state explains the failed data source and retry path.
- For dashboards, a chart must answer a decision question. If it does not, use a table, insight card, or sentence instead.

Library adaptation:
- **Recharts**: map series to `var(--chart-n)`, tooltip to system panel tokens, axes to muted text/grid tokens.
- **Chart.js**: build a theme adapter object using system tokens; avoid global random palettes.
- **Nivo/Visx/D3**: create a theme object from tokens; direct-label critical values.
- **Material charts**: preserve Material density/state logic but map roles to project tokens.

## Design-system output format

When starting a new design project, Helix should produce this before screens:

```md
## Design system foundation

### Questions / assumptions
- ...

### Design read
...

### Token direction
| Role | Value | Use |
|---|---|---|

### Component rules
| Component | Variants | States | Notes |
|---|---|---|---|

### Chart rules
| Role | Token | Use |
|---|---|---|

### Enforcement
- Files to create/update: ...
- Rules future screens must follow: ...
```

## Completion gate

A UI task is not complete unless Helix can answer:
- Where is the design system defined?
- Which tokens/components did this screen use?
- What did we add to the design system?
- How are charts/data visuals themed?
- How will future screens follow this?
- What was visually verified?
