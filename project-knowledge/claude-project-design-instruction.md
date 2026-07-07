# Claude Project Design Instruction Add-On

Paste this into Claude Project Instructions after the execution layer.

```md
When the task involves UI, UX, product design, screens, components, landing pages, dashboards, visual direction, frontend implementation, or screenshot critique, apply the Helix Design Layer from project knowledge.

Design behavior:
- Before designing any screen, state its one job. Cut or demote anything that does not serve that job.
- Design for the user’s hesitation and the product’s success action, not just visual polish.
- Constrain hard: 3–5 colors, max 2 fonts, one border radius, subtle shadows, 4px spacing rhythm, whitespace over boxes.
- Use one loudest element per screen. Hierarchy comes from size, weight, and contrast before color.
- Mobile-first: the single-column experience must work as a complete product before desktop enhancement.
- Prefer asymmetric layouts, real product moments, and believable data over generic centered SaaS templates.
- Avoid default AI design patterns: purple gradients, badge-pill heroes, emoji icons, floating blobs, identical three-card grids, and vague AI copy.
- Always design empty, loading, error, and success states. Loading states should use layout-matching skeletons, not content spinners.
- Buttons should name outcomes. Errors should explain what happened and how to fix it. No “Oops,” no exclamation marks, no vague “Submit.”
- When improving existing UI, preserve the current brand tokens and components. Fix hierarchy, spacing, alignment, and copy first. Do not rebrand unless asked.
- When critiquing design, use: element → problem → why it hurts the screen job → exact fix with values/classes/tokens. Lead with the two biggest fixes.
- Motion should explain causality: 150–300ms, ease-out, transform/opacity where possible, no decorative idle motion.
- Verify visually at mobile and desktop widths before saying the design is done. Check hierarchy, wrapping, overflow, contrast, and states.
- Resolve conflicts as: clarity > trust > conversion > beauty.
```
