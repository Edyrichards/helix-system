# Helix Design Masterclass v1

Purpose: teach Helix to design with stronger taste by synthesizing the best portable rules from Helix's original design layer, Taste/design-taste-frontend, Impeccable, Emil Kowalski design engineering, high-end visual design, and Claude-style product-first design guidance.

This is not a copied repo dump. It is Helix's opinionated design operating system.

## Design-system-first amendment

For substantial UI/UX/product-design tasks, also load `design-system-first.md` and `charts-and-design-system-adapters.md`. Helix should start by asking 3-7 design intake questions unless the user explicitly wants a quick throwaway mockup. If proceeding without answers, state assumptions, create/update the design system first, then build screens from that system.

Design work must answer: where is the design system defined, which tokens/components were used, what was added, how charts/data visuals inherit the system, and how future screens must follow it.

## Core principle

Design is not decoration. A Helix UI must make the product easier to understand, trust, and act on.

Every design task follows this sequence:

1. **Design read**: one sentence naming surface, audience, mood, and design family.
2. **Screen job**: one sentence naming the user's one job on this screen.
3. **System read**: inspect existing tokens/components/brand before inventing anything.
4. **Design direction**: pick a layout family, density, motion intensity, and visual register.
5. **Implementation**: build with existing components and tokens first.
6. **State design**: empty, loading, error, success, disabled, and hover/active/focus states where relevant.
7. **Visual verification**: render or screenshot mobile and desktop before claiming visual completion.
8. **Evidence ledger**: record screenshot paths, commands, inspected token files, and known limits.

## Design read format

Before designing or critiquing, write internally or briefly:

```md
Reading this as: <surface type> for <audience>, with a <mood/register>, leaning toward <design family/system>.
Screen job: <one thing the user must understand/do>.
```

Examples:

- Bookkeeping dashboard for solo founders, trust-first and calm, leaning toward dense product UI with editorial financial explanations.
- Premium landing page for technical buyers, restrained and proof-forward, leaning toward Linear/GitHub-style developer trust.
- Consumer finance mobile screen, warm but not cute, leaning toward calm editorial cards and evidence-first microcopy.

## UX Psychology & Conversion Amendment

For any onboarding, sign-up, upgrade, checkout, or commitment flow, **also load** `references/ux-psychology-principles.md`.

Helix must explicitly apply the six principles (smart defaults, goal gradient, reciprocity, endowment/IKEA, loss aversion, anchoring) on these screens.

In design reads and critiques, call out which principles are active and how they were implemented.

See the dedicated reference for full rules and critique prompts. Mobbin-style research of real flows is required before inventing commitment patterns.


## Mode split: product UI vs marketing UI

Helix must not apply landing-page theatrics to dashboards.

| Surface | Primary goal | Best patterns | Avoid |
|---|---|---|---|
| Product app/dashboard | Help user decide or act | dense hierarchy, tables, filters, evidence, progressive disclosure, clear states | overlarge whitespace, hero sections, decorative scroll effects |
| Landing/marketing | Create belief and conversion | narrative sections, proof, real product moments, asymmetric layouts, strong CTA | generic feature grids, fake trust, vague AI copy |
| Settings/forms | Reduce anxiety and errors | one-column forms, labels, helper text, inline validation, grouping | icon cards for every row, placeholder-as-label |
| Data table | scanning and action | compact rows, sticky header/actions, tabular numbers, empty/loading/error states | airy marketing spacing, spinner-only loading |
| Screenshot critique | identify highest-leverage fixes | element -> problem -> why -> exact fix | vibe-only feedback |

## Design dials

Set these silently for each task:

- **Design variance**: 1 predictable -> 10 experimental.
- **Motion intensity**: 1 static -> 10 cinematic.
- **Visual density**: 1 airy -> 10 cockpit.

Default by surface:

| Surface | Variance | Motion | Density |
|---|---:|---:|---:|
| dashboard/product UI | 4-6 | 2-4 | 6-8 |
| mobile app screen | 5-7 | 3-5 | 5-7 |
| SaaS landing | 6-8 | 4-6 | 3-5 |
| premium brand/portfolio | 7-9 | 5-7 | 2-4 |
| public-sector/trust critical | 2-4 | 1-3 | 5-7 |

## Source hierarchy

When rules conflict, resolve in this order:

1. User request and product goal.
2. Existing brand/design system and accessibility.
3. Helix product-first design layer.
4. Impeccable production rules: contrast, responsive, performance, real code.
5. Taste anti-slop rules: avoid saturated AI defaults and pattern repetition.
6. Emil motion rules: purposeful, fast, interruptible, origin-aware.
7. High-end visual rules: premium composition only when the surface supports it.

## Visual system rules

### Color

- Use semantic tokens from the repo when they exist.
- One accent color by default. Accent appears on primary actions, links, and essential highlights.
- 3-5 colors total for most screens.
- Avoid generic AI purple/violet gradients unless the brand explicitly asks.
- Avoid warm beige/cream/brass as the lazy premium-consumer default.
- Use OKLCH or existing token ramps when creating new palettes.
- Gray text on colored/tinted backgrounds often fails. Use a darker shade of the background hue or text-color transparency.
- Body text contrast: WCAG AA minimum 4.5:1. Large text 3:1 minimum.

### Typography

- One or two font families max.
- Do not default to Inter unless the existing project uses it or the brief calls for neutral/Linear/public-sector clarity.
- Prefer hierarchy through size, weight, contrast, and spacing before color.
- Display heading ceiling: around 96px unless the brief demands poster scale.
- Body line length: 65-75ch.
- Use `text-wrap: balance` for headings and `text-wrap: pretty` for prose where supported.
- Avoid random serif insertion for emphasis. Use italic/bold of the same family unless the brand truly calls for mixed type.

### Layout

- Mobile-first. Base layout must work around 375px.
- Use flex for one-dimensional layout, grid for true two-dimensional layout.
- Avoid absolute positioning for core layout.
- Avoid centered-everything unless the screen job is announcement/manifesto.
- Product UI should be compact and scannable. Marketing pages can breathe.
- Cards are not the default. Use spacing, dividers, section grouping, and hierarchy first.
- Nested cards are usually wrong.
- Desktop nav must stay one line; if not, simplify or move to a menu.

### Shape, shadows, borders

- One radius system per surface unless the project already defines a rule.
- Hairline borders and whitespace beat heavy shadows.
- Shadows should be subtle and tinted to the background hue, not pure black.
- Use premium double-bezel/nested shells only when they improve perceived material quality. Do not apply to every simple app row.

## Anti-slop bans

Helix should actively avoid these unless requested:

- purple/violet generic gradients
- AI badge-pill hero patterns
- emoji icons in serious product UI
- decorative blobs
- identical three-card feature grids
- fake trust claims
- fake precision numbers without labeling as sample/mock
- placeholder-as-label forms
- spinner-only content loading
- gradient text as default
- hand-rolled SVG icon paths when icon libraries/project icons exist
- div-based fake screenshots when a real screenshot/component/image should be used
- scroll cues like "Scroll to explore"
- decorative section numbers or tiny uppercase eyebrows above every section
- duplicate CTA intent like "Get started" and "Try free" for the same action
- em-dashes as a stylistic crutch in visible marketing copy

## Interaction and motion rules

Borrowing from strong design-engineering practice:

- First ask: should this animate at all?
- Frequent actions should be instant or nearly instant.
- UI transitions normally stay under 300ms.
- Use ease-out for entering/responding, ease-in-out for movement, linear only for constant motion.
- Never use ease-in for UI entrance/responding.
- Animate transform and opacity, not layout properties.
- Add `:active { transform: scale(.97-.98) }` to pressable controls when appropriate.
- Popovers scale from their trigger, not center. Modals stay centered.
- Never animate from `scale(0)`; start around `.95` with opacity.
- Respect `prefers-reduced-motion`.
- Gate hover effects with `@media (hover: hover) and (pointer: fine)`.
- Avoid `window.addEventListener('scroll')`; use CSS scroll timelines, IntersectionObserver, Motion `useScroll`, or GSAP ScrollTrigger with cleanup.
- Motion must communicate hierarchy, feedback, causality, or state change. If it only says "cool," remove it.

## State design requirements

For every async, list, table, dashboard, or core flow:

- **Empty**: orient user, explain why empty, give first useful action.
- **Loading**: skeleton matching final layout, not a generic spinner for content areas.
- **Error**: say what happened and how to fix it; include retry when useful.
- **Success**: confirm outcome and point to next useful step.
- **Disabled**: explain requirements where unclear.
- **Focus**: visible keyboard focus.
- **Active/pressed**: immediate tactile feedback.

## Product copy rules

- Buttons name outcomes, not mechanisms: "Set aside tax money" beats "Submit".
- Error copy is specific: "Bank feed disconnected. Reconnect Chase to update cash." beats "Oops".
- Empty state copy should be one orientation line, one short explanation, one action.
- Avoid vague AI/productivity copy: "unlock insights," "seamless," "revolutionize," "supercharge".
- Use believable data and product moments.
- For financial/data apps, separate what is known, inferred, and recommended.

## Surface-specific patterns

### Dashboards and app screens

- Start with the main decision, not a grid of metrics.
- Use tabular numbers.
- Put evidence close to claims.
- Show confidence/source where decisions depend on data.
- Prefer one recommended next action over many equal actions.
- Dense does not mean cramped: use clear grouping and scanning rhythm.

### Landing pages

- Start with a sharp product promise and proof, not generic AI slogans.
- Show the product doing the job.
- Keep hero stack to headline, short subtext, one primary CTA, optional secondary CTA.
- Put trust logos/proof below the hero, not stuffed into the hero.
- Vary section layout families. Do not repeat identical feature sections.
- Use real assets or clearly labeled placeholders. Avoid div-only fake screenshots unless building a genuine live component preview.

### Forms/settings

- Labels above inputs. Placeholder never replaces label.
- Inline validation close to the field.
- Group related settings with headings/dividers, not a heavy card per row.
- Destructive actions require clear hierarchy and confirmation when needed.

### Mobile checkout/onboarding

- One column, 44px touch targets, sticky primary action when appropriate.
- Collapse summaries; reveal details progressively.
- Show progress and preserve back/exit paths.

## Critique format

When critiquing UI, lead with the two biggest fixes, then use:

```md
| Element | Problem | Why it hurts the screen job | Exact fix |
|---|---|---|---|
```

Do not say "make it cleaner" without naming spacing, hierarchy, type, color, state, or layout changes.

## Implementation pre-flight

Before finishing UI work, check:

- [ ] Screen job is explicit.
- [ ] Existing tokens/components inspected or absence stated.
- [ ] One loudest element per screen.
- [ ] Mobile layout works around 375px.
- [ ] Desktop layout is not just stretched mobile.
- [ ] Empty/loading/error/success states handled where relevant.
- [ ] CTA labels name outcomes.
- [ ] Body/muted text readable.
- [ ] Focus, hover, active states present for interactive elements.
- [ ] Motion respects reduced motion and does not animate layout properties.
- [ ] No banned AI default patterns slipped in.
- [ ] Rendered/screenshot inspected before claiming visual verification.
