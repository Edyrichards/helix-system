# Helix UI Pro-Max Preflight

Use this before shipping, rendering, or scoring any Helix UI.

## 1. Product clarity
- [ ] I can state the screen's one job in one sentence.
- [ ] The visually loudest element supports that job.
- [ ] The primary CTA is the next useful user action.
- [ ] Secondary actions are visually quieter.

## 2. Design-system fit
- [ ] Existing tokens/components were inspected.
- [ ] Colors use semantic tokens or an intentional palette.
- [ ] One accent color dominates; random competing accents removed.
- [ ] Radius, shadow, border, and icon style are consistent.
- [ ] No hardcoded hex values unless the project already uses them or this is a standalone mockup.

## 3. Layout quality
- [ ] Mobile around 375px works without horizontal scroll.
- [ ] Desktop composition is intentional, not stretched mobile.
- [ ] Flexbox used for 1D; grid only for real 2D layout.
- [ ] Core layout does not depend on fragile absolute positioning.
- [ ] Cards are used only where they clarify hierarchy.

## 4. Typography and copy
- [ ] Body lines stay readable around 65-75ch.
- [ ] Headings are balanced and not overflowing.
- [ ] Buttons name outcomes, not mechanisms.
- [ ] Error/empty/success copy tells the user what happened and what to do.
- [ ] Visible copy was re-read for AI-ish filler or broken grammar.

## 5. States and interaction
- [ ] Empty state exists where data can be absent.
- [ ] Loading uses skeletons that match final layout.
- [ ] Error state has fix/retry path where useful.
- [ ] Success confirms and advances.
- [ ] Focus state is visible.
- [ ] Active/pressed state gives tactile feedback.
- [ ] Hover effects are gated for pointer devices where needed.

## 6. Motion and performance
- [ ] Every animation has a reason: hierarchy, feedback, causality, or state change.
- [ ] UI animations are mostly 150-300ms.
- [ ] Motion respects `prefers-reduced-motion`.
- [ ] Animations use transform/opacity rather than layout properties.
- [ ] No scroll listener jank; use IntersectionObserver/Motion/GSAP/CSS timelines.
- [ ] Blur/backdrop-filter is not applied to large scrolling containers.

## 7. Anti-slop scan
- [ ] No generic AI purple gradient unless brand requested.
- [ ] No badge-pill AI hero by default.
- [ ] No emoji icons in serious UI.
- [ ] No identical three-card feature grid.
- [ ] No fake trust claims.
- [ ] No placeholder-as-label.
- [ ] No spinner-only content loading.
- [ ] No decorative section numbers/eyebrows everywhere.
- [ ] No duplicate CTA intent.
- [ ] No gradient text by default.

## 8. Verification
- [ ] Built/rendered locally if code was changed.
- [ ] Mobile screenshot inspected.
- [ ] Desktop screenshot inspected.
- [ ] Overflow, clipping, wrapping, contrast, z-index, and states checked.
- [ ] Final answer says exactly what was verified and where evidence is saved.


## 9. Design-system-first gate
- [ ] Intake questions were asked, or assumptions were explicitly stated.
- [ ] Design system location is named (`DESIGN.md`, tokens file, `globals.css`, shadcn theme, Material theme, etc.).
- [ ] New UI uses tokens/components from that system.
- [ ] Any new token/component variant was added to the system before use.
- [ ] shadcn/Radix, Material, Motion, and chart-library choices are adapted to project tokens rather than shipped as defaults.
- [ ] Chart tokens cover categorical, sequential, positive, negative, neutral, grid, axis, and tooltip roles where data viz exists.
- [ ] Future screens have a clear rule for following the same design system.
