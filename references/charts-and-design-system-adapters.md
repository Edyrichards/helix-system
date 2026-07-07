# Helix Charts and Design-System Adapters

Purpose: make charts, tables, and data-heavy UI feel like part of the product's design system instead of pasted-in library defaults.

## Required data-viz design pass

Before adding a chart, answer:
1. What decision should this chart help the user make?
2. Is a chart better than a sentence, KPI, table, or annotated insight card?
3. What data states exist: empty, loading, error, partial, stale, success?
4. Which token roles map to data semantics?
5. How will color-blind or low-vision users read it?

## Token contract

Charts use semantic CSS variables or Tailwind theme tokens only.

Required roles: chart-1, chart-2, chart-3, chart-4, chart-5, chart-positive, chart-negative, chart-warning, chart-neutral, chart-grid, chart-axis, chart-tooltip-bg, chart-tooltip-text.

## shadcn chart adaptation

If shadcn is present:
- Use or create `components/ui/chart.tsx` following shadcn's chart wrapper pattern.
- Define chart config with semantic labels and colors.
- Use `ChartContainer`, `ChartTooltip`, and `ChartTooltipContent` or equivalent project components.
- Add chart variables to `globals.css` next to shadcn tokens.
- Keep tooltips, legends, cards, and axes aligned with shadcn panel/radius/typography tokens.

Example config shape:

```ts
const chartConfig = {
  revenue: { label: 'Revenue', color: 'hsl(var(--chart-1))' },
  expenses: { label: 'Expenses', color: 'hsl(var(--chart-negative))' },
  forecast: { label: 'Forecast', color: 'hsl(var(--chart-2))' },
} satisfies ChartConfig
```

## Material chart adaptation

If Material is the base:
- Map chart colors to Material roles, not arbitrary palette arrays.
- Use primary for the main series, tertiary for comparison, error for negative/destructive values.
- Use surface-container for chart panels and outline-variant for gridlines.
- Tooltip elevation/radius follows Material menu/popover rules.
- Keep density consistent with Material list/table density.

## Motion in charts

- Animate chart entrance only when it clarifies load or comparison.
- Use short, non-blocking reveals: 180-300ms for bars/lines, stagger under 50ms.
- Respect reduced motion by disabling path drawing, parallax, counters, and sequential reveals.
- Do not animate financial numbers in a way that obscures exact reading.

## Dashboard chart anti-patterns

Avoid rainbow categorical palettes, red/green only without labels, chart cards that answer no decision, tiny low-contrast axes, decorative area gradients that reduce readability, tooltip styles that do not match the rest of the UI, chart library defaults, and loading spinners inside empty chart rectangles.

## Chart verification

- [ ] Chart uses design-system tokens.
- [ ] Tooltip/legend/card styles match project UI.
- [ ] Positive/negative semantics are stable.
- [ ] Empty/loading/error states exist.
- [ ] Axis/labels are readable at mobile width.
- [ ] Critical values are labeled or explained.
- [ ] Reduced-motion behavior is safe.
