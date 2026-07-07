# CLAUDE.md Design Section

Add this section to your repo-level `CLAUDE.md`.

```md
## Design

### Product-first design

- Before editing UI, identify the screen’s one job in a sentence.
- Every visual decision should support that job.
- Preserve the existing brand system unless the user explicitly asks for a rebrand.
- Improve hierarchy, spacing, alignment, copy, and states before changing colors or fonts.

### System constraints

- Use design tokens from `globals.css`, theme config, or the project’s existing design system.
- Do not hardcode hex values unless the project already uses that pattern or the user asks.
- Avoid raw `bg-white` / `text-black` defaults when semantic tokens exist.
- 3–5 colors total. Accent color appears only on primary actions, links, and essential highlights.
- Maximum 2 font families.
- Use one border radius system-wide unless existing components define otherwise.
- Use subtle shadows only. Prefer hairline borders and whitespace.
- Use Tailwind spacing scale consistently. Avoid arbitrary values unless required.

### Layout

- Mobile-first: base classes are mobile, `md:` and `lg:` are enhancements.
- Test around 375px width.
- Flexbox by default; grid only for genuine two-dimensional layouts.
- Do not use absolute positioning for core layout.
- Prefer asymmetric splits and bento structures over identical card triplets.
- Avoid centered-everything layouts unless the screen’s job calls for it.

### Hierarchy

- One visually dominant element per screen.
- Use size, weight, and contrast before using color.
- Secondary content should use muted text.
- Data should use tabular numbers.
- Headings should use balanced wrapping where supported.
- Body text should remain readable with line-height around 1.4–1.6.

### States and copy

- Every list, table, dashboard, async view, and key flow should include empty, loading, error, and success states.
- Empty states should orient the user and provide the first useful action.
- Loading states should use skeletons that match the final layout.
- Error states should say what happened and how to fix it, with a retry path where useful.
- Success states should confirm and point to the next useful action.
- Buttons should name outcomes, not mechanisms.
- Avoid “Submit,” “OK,” “Click here,” “Oops,” and vague error copy.

### Motion

- Motion should explain state change or causality.
- Use 150–300ms duration, ease-out, transform/opacity where possible.
- Respect `prefers-reduced-motion`.
- Avoid looping/idle animation unless specifically required.

### Banned defaults

Avoid these unless the user explicitly asks:

- purple/violet gradients
- generic AI badge-pill heroes
- emoji icons
- decorative blobs
- fake trust claims
- identical three-card feature grids
- spinners for content areas
- dark patterns such as fake urgency, hidden costs, or pre-checked add-ons

### Verification

Before finishing UI work:

- Render and inspect at mobile and desktop widths.
- Check the dominant element is correct.
- Check no wrapping, overflow, clipping, or z-index issues exist.
- Check muted text is readable.
- Check all four states are handled where relevant.
- Do not claim visual verification unless the UI was actually rendered or inspected.
```
