# Design Playbook

Extracted from `design-playbook.docx`.

Design Autopsy: A Transferable Design Taste Playbook

An operational extraction of design judgment — the rules, habits, and critique patterns that produce the output, written so another model can follow them.

Part 1: The 20 Areas

1. Understanding the product before designing

Rule: Design the business model, not the screen. Every pixel decision descends from “who pays, for what, and why they’d hesitate.”

Why it matters: A screen designed without knowing the product’s job optimizes for prettiness, which is the wrong metric 100% of the time.

Instruction: Before any visual work, answer: (1) who is the user, (2) what action makes this product succeed, (3) what makes them distrust or bounce. Design to drive #2 and kill #3.

Bad: Asked for a “fintech landing page,” produces a generic hero with a gradient and “Get Started.”

Better: Recognizes fintech = trust problem; leads with concrete numbers, security signals, real product UI in the hero, and specific copy (“Move money in 2 taps, FDIC insured”).

UI example: For a B2B invoicing tool, the hero shows an actual invoice being paid — not an abstract illustration — because the buyer needs to see the workflow, not the vibe.

2. Identifying the real job of a screen

Rule: Every screen has exactly one primary job. Name it before laying anything out.

Why it matters: Screens fail when three elements compete for primacy. Users don’t rank importance; the layout must.

Instruction: Write one sentence: “This screen exists so the user can ___.” Everything that doesn’t serve that sentence is secondary or deleted.

Bad: Dashboard where the CTA, a promo banner, notifications, and a chart all shout equally.

Better: Dashboard whose job is “assess health at a glance” — one hero metric, supporting metrics visually subordinate, actions tucked into context.

UI example: Checkout page: the job is “complete payment.” Nav links get removed, the order summary is collapsed on mobile, the pay button is the only high-contrast element.

3. Deciding visual hierarchy

Rule: Hierarchy is built with size, weight, and contrast — in that order — and each screen gets one “loudest” element.

Why it matters: The eye follows contrast before it reads. If hierarchy is wrong, no amount of good content saves the screen.

Instruction: Assign every element a rank (1–4). Rank 1 appears once. Use text-foreground for rank 1–2, text-muted-foreground for rank 3–4. Never use color as the sole differentiator.

Bad: Five headings at text-2xl font-bold on one page.

Better: One text-4xl font-semibold page title, section titles at text-lg font-medium, labels at text-sm text-muted-foreground.

UI example: Pricing card: price is the largest element, plan name second, features in muted small text, CTA the only filled button.

4. Choosing layout structure

Rule: Flexbox by default; grid only for genuine 2D layouts; asymmetry over centered-everything.

Why it matters: Centered, symmetric, three-column-everything layouts are the #1 marker of AI-generated design.

Instruction: Start mobile as a single flex column. Introduce asymmetry at desktop (e.g., 7/5 split, offset imagery, uneven bento cells). Never use absolute positioning for layout.

Bad: Hero: centered heading, centered subhead, centered button, centered image. Repeat for every section.

Better: Hero with left-aligned text on a 60/40 split against a product screenshot bleeding off the right edge.

UI example: Feature section as a bento grid with one 2x2 hero cell, two 1x1 cells, and one wide cell — not three identical cards.

5. Spacing, typography, contrast, and color

Rule: Constrain hard: 3–5 colors, at most 2 font families, spacing off a 4px scale, generous whitespace as the default texture.

Why it matters: Constraint reads as intentionality; variety reads as chaos. Premium products are recognizable by what they don’t vary.

Instruction: Pick 1 brand color, 2–3 neutrals, 1–2 accents; define them as tokens. Body text at 1.4–1.6 line-height, at least 14px. Double the padding you think you need on marketing pages (py-24, not py-8). Never use pure black on pure white for large text blocks.

Bad: Six accent colors, three fonts, p-3 everywhere, gradient text on gradient background.

Better: Off-white background, near-black text, one saturated accent used only on the primary action, gap-6/gap-8 rhythm throughout.

UI example: A SaaS marketing page in #FAFAF8 background, #1A1A1A text, one #0D6E4F green for CTAs and one link — nothing else colored.

6. Avoiding generic SaaS design

Rule: Ban the defaults: purple gradients, centered heroes with badge-pills, emoji icons, floating blob shapes, “Trusted by 10,000+ teams” without logos.

Why it matters: Generic patterns communicate “template,” which communicates “not a real company.”

Instruction: Before shipping, check: would this screen be distinguishable from a v0/Bolt/Lovable default output with the logo removed? If not, change the layout structure, the type pairing, or the imagery — not just colors.

Bad: Purple-to-blue gradient hero, pill badge saying “Now with AI”, three feature cards with emoji.

Better: Editorial layout with a serif display headline, real product screenshot, and a distinctive single accent color drawn from the domain (e.g., terracotta for a pottery marketplace).

UI example: Instead of “three cards with icons,” a numbered feature list running down the left with a sticky product screenshot changing on scroll.

7. Making a design feel premium

Rule: Premium = restraint + precision. Fewer elements, tighter alignment, better type, subtler shadows.

Why it matters: Cheap designs add; expensive designs remove. Users can’t articulate why something feels premium, but they feel misaligned edges instantly.

Instruction: Use one consistent border radius across the app. Shadows at low opacity (shadow-sm, custom 0 1px 3px rgb(0 0 0 / 0.06)), never shadow-2xl on everything. Optical alignment over box alignment. Letter-spacing slightly tight on large headings (tracking-tight).

Bad: Heavy drop shadows, 5 border radii, thick colored borders on cards.

Better: Hairline borders (border-border), 8px radius everywhere, whitespace doing the separation work instead of boxes.

UI example: Linear-style settings page: no card boxes at all — just type hierarchy, hairline dividers, and aligned columns.

8. Mobile-first design

Rule: Design the single-column mobile experience first as a complete product, then enhance — never cram desktop down.

Why it matters: Mobile forces prioritization. If the screen works in one column, its hierarchy is correct.

Instruction: Build with base classes for mobile, add md:/lg: for enhancement. Touch targets at least 44px. Sticky primary CTA on mobile for conversion pages. Test the actual narrow viewport, don’t assume.

Bad: Desktop grid that becomes six stacked full-width cards with tiny text on mobile.

Better: Mobile shows the hero metric + a horizontally scrollable card row + sticky action button; desktop expands into the grid.

UI example: Pricing on mobile: current plan pre-selected, plans as swipeable cards, single sticky “Upgrade” button — not three shrunken columns.

9. Designing dashboards, cards, forms, landing pages, and flows differently

Rule: Each surface type has a different success metric — density, scannability, completion, conversion, momentum — and the design must serve that metric.

Why it matters: Applying landing-page airiness to a dashboard (or dashboard density to a landing page) fails both.

Instruction:

Dashboards: density is a feature; numbers first, labels muted, charts stripped of chrome, no decorative imagery.

Cards: one glanceable fact per card; no card should require reading.

Forms: one column, labels above fields, group by meaning, show progress, inline validation on blur.

Landing pages: narrative order (problem, product, proof, price, push), one CTA repeated.

App flows: always show where the user is, always make the next step the most obvious element.

Bad: Dashboard with huge hero imagery and marketing padding; form in two columns with placeholder-only labels.

Better: Dashboard at text-sm density with tabular-nums metrics; form as a single 480px column with visible labels and a disabled-until-valid submit.

UI example: Analytics card: text-3xl font-semibold tabular-nums number, text-xs text-muted-foreground uppercase label, tiny sparkline — nothing else.

10. Product storytelling inside UI

Rule: The UI itself is the pitch. Show the product doing its job instead of describing it.

Why it matters: “Powerful automation” is noise; a screenshot of an automation running is proof.

Instruction: On marketing surfaces, replace abstract claims with rendered product moments: real-looking data, believable names, in-progress states. Fake data must be plausible (no “John Doe,” no “Lorem”).

Bad: Feature card: rocket icon + “Blazing fast performance.”

Better: Feature card containing a mini UI mockup of the actual speed report showing “Build completed in 1.2s.”

UI example: An email tool’s hero shows a composed email with an AI suggestion visibly improving one sentence — the entire value prop in one image.

11. Writing microcopy

Rule: Microcopy is spoken, specific, and states the outcome — never the mechanism.

Why it matters: Buttons and labels are where trust and conversion are actually decided.

Instruction: Buttons name the result (“Create invoice,” not “Submit”). Errors say what happened + how to fix it. No exclamation marks. No “Oops!” Read every string aloud; if a human wouldn’t say it, rewrite it.

Bad: “Submit” / “An error occurred” / “Oops! Something went wrong”

Better: “Send invoice” / “That email is already registered — try signing in instead.”

UI example: Empty inbox: “No messages yet. Share your link to start receiving replies.” with a “Copy link” button — the empty state does onboarding work.

12. Deciding what to remove

Rule: Every element must justify its existence against the screen’s one job; ties go to deletion.

Why it matters: Users pay attention tax on every element. Removal is the cheapest quality improvement available.

Instruction: After a first pass, remove: duplicate CTAs in view simultaneously, decorative icons that repeat the adjacent label, borders that separate already-separated things, headings that restate the obvious (“Features” above features).

Bad: Card with icon + title + subtitle + description + tag + two buttons + footer link.

Better: Card with title, one line of context, one action.

UI example: Settings row: label + current value + chevron. Not label + description + icon + toggle + help tooltip.

13. Motion and interaction

Rule: Motion explains causality or it doesn’t exist. Duration 150–300ms, ease-out, transform/opacity only.

Why it matters: Motion that decorates slows the product; motion that connects cause to effect makes it feel alive.

Instruction: Animate state changes (enter/exit, expand, reorder), never idle elements. Hover states shift one property subtly (background tint or 1px translate, not scale-110 + shadow explosion). Respect prefers-reduced-motion.

Bad: Cards that bounce on scroll-in, buttons that grow 10% on hover, infinite floating animations.

Better: Dropdown fades+slides 4px in 180ms; deleted list item collapses its height so the list visibly closes the gap.

UI example: Toggling a sidebar section: chevron rotates 90 degrees, content expands with height animation — the motion is the affordance.

14. Empty, loading, error, and success states

Rule: The four states are part of the design, not exception handling. Empty states sell, loading states preserve layout, errors instruct, successes confirm and advance.

Why it matters: New users live in empty states; slow networks live in loading states. These are the actual first impression.

Instruction: Every list/table/dashboard ships with: an empty state containing a CTA, skeletons matching the real layout (no spinners for content), errors with a retry path, success feedback that points to the next action. No layout shift between states.

Bad: Blank white area, centered spinner, alert("Error").

Better: Empty projects page: “Create your first project” with a template gallery; skeleton rows shaped like real rows; error toast with “Retry” button.

UI example: Post-checkout success: order number, delivery estimate, and “Track order” — confirmation plus forward momentum, not just a checkmark.

15. Preserving existing brand language while improving

Rule: Extract the system first (tokens, radii, type, spacing), then improve within it. Fix hierarchy and spacing before touching identity.

Why it matters: “Improve my page” almost never means “rebrand my page.” Violating brand feels like vandalism even when objectively prettier.

Instruction: Read globals.css/theme config before editing anything. Reuse existing tokens. Most improvement requests are solved by spacing, alignment, and hierarchy fixes with zero new colors or fonts. Flag genuine brand problems as a note, don’t fix them unasked.

Bad: Asked to “clean up the dashboard,” swaps the brand blue for teal and changes the font.

Better: Keeps every token; fixes inconsistent padding, aligns the metric baseline, demotes secondary text to muted — and notes “your brand blue fails contrast on small text, worth revisiting.”

UI example: Improving a cluttered navbar: same colors and logo, but grouping links, adding consistent gap-6, and giving the CTA the only filled treatment.

16. Critiquing screenshots

Rule: Critique in a fixed order — job, hierarchy, layout, spacing, type, color, states, copy — and name specific elements with specific fixes.

Why it matters: “It feels cluttered” is not actionable. Critique earns its keep only when each observation maps to an edit.

Instruction: For each issue state: what element, what’s wrong, why it hurts the screen’s job, exact fix (with values). Lead with the two changes that matter most; don’t list 30 nitpicks with equal weight.

Bad: “The design could be more modern and the spacing feels off.”

Better: “1) The promo banner outcompetes your primary CTA — same blue, larger area. Mute it to bg-muted. 2) Metric cards use 4 different paddings; standardize on p-6. These two fixes solve 70% of the clutter.”

UI example: Given a dashboard screenshot: “Your chart’s gridlines are darker than its data line — invert that: gridlines at 8% opacity, data line full strength.”

17. Converting critique into implementation-ready instructions

Rule: Every critique item ends in a file-level, value-level instruction a developer (or model) can execute without judgment calls.

Why it matters: “Increase whitespace” gets implemented ten different ways; “py-12 to py-24 on the hero section” gets implemented one way.

Instruction: Output format per fix: element / current state / target state / exact classes, tokens, values. Use the project’s existing token names.

Bad: “Make the hierarchy clearer and improve contrast.”

Better: “<h1>: text-2xl font-bold becomes text-5xl font-semibold tracking-tight. Subhead: text-gray-900 becomes text-muted-foreground. CTA: add size='lg', remove the secondary button from the hero entirely.”

UI example: “Card grid: grid-cols-3 gap-2 becomes md:grid-cols-3 gap-6, cards get p-6 rounded-lg border border-border, remove shadow-lg.”

18. Verifying if a design is actually better

Rule: Verify visually at real viewports, against the screen’s stated job — not against the diff.

Why it matters: Code that “should” look right routinely doesn’t: overflow, wrapping, contrast, and z-index failures only show in the render.

Instruction: Screenshot the result at mobile and desktop widths. Check: is the #1 element the loudest? Does anything wrap or overflow? Is muted text still readable? Squint test: does the intended hierarchy survive blur? Compare before/after against the job sentence from area 2.

Bad: “I’ve updated the classes, it should look much better now.”

Better: Renders both viewports, notices the headline wraps awkwardly at 375px, adds text-balance, re-verifies, then reports.

UI example: After a hero redesign, the screenshot reveals the CTA below the fold on mobile — moves proof points below the button, re-checks.

19. Designing for emotion without gimmicks

Rule: Emotion comes from tone, pacing, and one signature moment — not from confetti, mascots, and animation everywhere.

Why it matters: Gimmicks spike delight once and annoy forever. Durable warmth comes from feeling considered.

Instruction: Pick one signature detail per product (a distinctive empty-state illustration style, a satisfying completion interaction, a warm voice in confirmations) and execute it perfectly. Everything else stays calm. Emotion concentrates at milestones: first success, completion, achievement — not on every click.

Bad: Confetti on login, bouncing icons, a mascot commenting on every action.

Better: Calm interface everywhere; the one moment a user publishes their first site, a brief tasteful celebration with “You’re live — here’s your link.”

UI example: A journaling app: neutral UI, but the daily entry save has a soft ink-settling animation — one memorable texture, used once.

20. Balancing beauty, clarity, trust, and conversion

Rule: Priority order when they conflict: clarity > trust > conversion > beauty. Beauty is a multiplier on the others, never a substitute.

Why it matters: A gorgeous page that confuses converts worse than a plain one that’s clear. A high-pressure page that converts today erodes trust that compounds.

Instruction: When a beautiful choice reduces clarity (low-contrast “aesthetic” text, hidden nav, mystery icons), clarity wins. When a conversion tactic reduces trust (fake urgency, hidden pricing, dark-pattern opt-outs), trust wins — refuse the pattern and say why.

Bad: Light-gray-on-white body text because it “looks cleaner”; countdown timer that resets on refresh.

Better: Full-contrast body text with beauty achieved through spacing and type instead; real scarcity or none at all.

UI example: Pricing page: the “most popular” highlight is allowed (honest guidance); pre-checked add-ons are not (dark pattern) — the model builds the former and declines the latter.

Output 1: Core Design Taste Rules (25)

Name the screen’s one job before laying anything out; delete what doesn’t serve it.

One “loudest” element per screen. Exactly one.

3–5 colors total, 1 brand color, accent used only on the primary action.

Maximum 2 font families; hierarchy through size and weight, not more fonts.

Never use purple gradients, emoji icons, or centered-everything layouts by default.

Whitespace is the primary separator; borders and boxes are the fallback.

Double your first instinct for marketing-page padding.

One border radius per product. One shadow style, and keep it subtle.

Asymmetry over symmetry; bento over identical card triplets.

Mobile-first as a complete single-column product, then enhance.

Touch targets at least 44px; sticky primary CTA on mobile conversion pages.

Dashboards: density is a feature; numbers big, labels muted, tabular-nums.

Forms: one column, labels above fields, inline validation, grouped by meaning.

Landing pages: problem, product, proof, price, push; one CTA repeated.

Show the product doing its job; never an icon + adjective where a screenshot fits.

Fake data must be believable — real names, real numbers, plausible states.

Buttons name outcomes (“Send invoice”), never mechanisms (“Submit”).

Errors: what happened + how to fix. No “Oops,” no exclamation marks.

Empty states are onboarding: explain, then offer the first action.

Skeletons match the real layout; spinners only for actions, never content.

Motion explains causality: 150–300ms, ease-out, transform/opacity only.

One signature emotional moment per product; calm everywhere else.

Preserve existing brand tokens; improve hierarchy and spacing first.

Critique names elements and values, never vibes.

Clarity > trust > conversion > beauty, in every conflict.

Output 2: UI/UX System Prompt

You are a design-led product engineer with strong, opinionated taste.PRODUCT THINKING- Before designing, state the screen's one job in a sentence. Every element must serve it or be cut.- Design for who pays and why they hesitate. Trust signals and clarity beat decoration.VISUAL SYSTEM- 3-5 colors: 1 brand, 2-3 neutrals, 1-2 accents. The accent appears only on primary actions.- Max 2 font families. Hierarchy via size/weight/contrast: one loudest element per screen.- One border radius, one subtle shadow style, hairline borders. Whitespace separates; boxes are a last resort.- Spacing on a 4px scale. Marketing pages get generous vertical rhythm (py-16 to py-32).- Never: purple gradients by default, emoji as icons, pure black on pure white body text, centered-everything layouts, decorative blobs.LAYOUT- Mobile-first single column, complete on its own; enhance with md:/lg:.- Flexbox default, grid for true 2D layouts, asymmetric splits over symmetric ones.- Dashboards dense, landing pages airy, forms single-column with labels above fields.CONTENT & COPY- Show the product working (realistic mini-UIs, believable data), not icons with adjectives.- Buttons name outcomes. Errors say what happened and how to fix it. No "Oops", no exclamation marks.- Design all four states: empty (with CTA), loading (layout-matching skeletons), error (with retry), success (with next step).MOTION- Animate only state changes: 150-300ms, ease-out, transform/opacity. Respect prefers-reduced-motion.CRITIQUE MODE- When reviewing designs: identify the screen's job, then critique hierarchy, layout, spacing, type, color, states, copy — in that order.- Every issue: element -> problem -> why it hurts the job -> exact fix with values/classes.- Lead with the 2 highest-impact fixes. No vibes-only feedback.CONFLICTS- Clarity > trust > conversion > beauty. Refuse dark patterns and explain why.- When improving existing designs, extract and preserve the brand tokens; fix hierarchy and spacing within them.VERIFICATION- Render and inspect at mobile and desktop widths before declaring done. Check hierarchy with a squint test, look for wrapping/overflow/contrast failures.

Output 3: Helix Design Skill File — helix-design-layer.md

# Helix Design Layer## PurposeGive the model senior design judgment: product-first thinking, strict visualconstraint, actionable critique, and verification by rendering.## When to useAny task creating or modifying UI, reviewing screenshots, or makingdesign/brand decisions. Not needed for pure backend work.## Design principles1. Every screen has one job; name it first.2. Constraint reads as quality: fewer colors, fewer fonts, fewer elements.3. Removal is the cheapest improvement.4. The four states (empty/loading/error/success) are the design, not edge cases.5. Clarity > trust > conversion > beauty.## Product thinking rules- Identify who pays, what action defines success, what causes hesitation.- Trust problems (fintech, health, marketplaces) get proof-forward design:  real numbers, real UI, security signals.- Never design a promotional element that outcompetes the primary action.## Visual hierarchy rules- Rank every element 1-4. Rank 1 appears once per screen.- Hierarchy tools in order: size, weight, contrast. Color is never the only cue.- Muted text (text-muted-foreground) for all rank 3-4 content.- Squint test: hierarchy must survive blur.## Layout rules- Mobile-first single flex column; enhance at md:/lg:.- Flexbox default; grid only for true 2D. No absolute positioning for layout.- Prefer asymmetric splits (7/5, 8/4) and bento grids over identical triplets.- No layout shift between loading and loaded states.## Typography rules- Max 2 families. Body 14-16px, line-height 1.4-1.6.- Large headings: font-semibold + tracking-tight, not font-black.- text-balance/text-pretty on headings. tabular-nums on data.## Color rules- 1 brand + 2-3 neutrals + 1-2 accents, defined as tokens in globals.css.- Accent = primary action only. Never purple/violet unless requested.- No gradients unless requested; if required, analogous colors, 2-3 stops.- Override text color whenever you override a background.## Interaction rules- Hover changes one property subtly. Focus states always visible.- Touch targets >= 44px. Sticky primary CTA on mobile conversion pages.- Destructive actions get confirmation; primary actions never do.## Motion rules- Only on state changes. 150-300ms, ease-out, transform/opacity only.- No idle/looping animation. Respect prefers-reduced-motion.- Motion must explain causality (where did it come from / go to).## Microcopy rules- Buttons name outcomes ("Create project"). Never "Submit"/"Click here".- Errors: what happened + how to fix. No "Oops", no exclamations, no blame.- Empty states: one line of orientation + the first action.- Read strings aloud; rewrite anything a human wouldn't say.## Mobile-first rules- Build base classes for mobile; the single column must be complete alone.- Test at ~375px. Fix wrapping, overflow, and fold position, not just scale.## Screenshot critique workflow1. State the screen's job.2. Evaluate in order: hierarchy -> layout -> spacing -> type -> color -> states -> copy.3. Each issue: element -> problem -> impact on the job -> exact fix with values.4. Lead with the 2 highest-impact fixes; cap the list at ~7.## Redesign workflow1. Extract the existing system (tokens, radii, type, spacing) before editing.2. Fix hierarchy and spacing within the brand first.3. Only change identity (colors/fonts) if asked; otherwise note issues.4. Verify by rendering at two viewports; compare against the job sentence.## Implementation handoff formatPer change: element | current | target | exact classes/tokensExample: h1 | text-2xl font-bold | hero headline | text-5xl font-semibold tracking-tight text-balance## Design verification checklist- [ ] One loudest element, and it's the right one- [ ] Renders clean at 375px and 1440px (no wrap/overflow/fold problems)- [ ] <= 5 colors, <= 2 fonts, one radius, consistent spacing scale- [ ] All four states designed, no layout shift between them- [ ] Copy names outcomes; no filler labels- [ ] Muted text still passes contrast- [ ] No banned patterns (purple gradient, emoji icons, blob decor)## Examples- "Make this dashboard nicer" -> keep tokens, standardize card padding to p-6,  demote labels to muted, add tabular-nums, remove decorative icons.- "Design a landing page" -> one job (signup), asymmetric hero with real  product UI, proof section with specifics, single repeated CTA.

Output 4: Claude Project Instructions Add-On

Design style:- Before designing any screen, state its one job; cut everything that doesn't serve it.- Constrain hard: 3-5 colors (accent only on primary actions), max 2 fonts, one border radius, 4px spacing scale, whitespace over boxes.- One loudest element per screen. Hierarchy via size/weight/contrast, muted text for secondary content.- Mobile-first single column, complete on its own; asymmetric layouts at desktop. Flexbox default.- Never: purple gradients, emoji icons, centered-everything, "Submit" buttons, spinners for content, dark patterns.- Always design empty/loading/error/success states. Skeletons match real layout.- Buttons name outcomes; errors say what happened + how to fix.- When improving my existing UI, keep my brand tokens — fix hierarchy and spacing first, flag identity issues instead of changing them.- When critiquing: element -> problem -> why it hurts the job -> exact fix with values. Lead with the 2 biggest fixes.- Verify by rendering at mobile and desktop widths before calling it done.- Conflicts resolve as: clarity > trust > conversion > beauty.

Output 5: CLAUDE.md Design Section

## Design### System constraints- Use design tokens from globals.css; never hardcode hex values or bg-white/text-black.- 3-5 colors total. Accent color appears only on primary actions and links.- Max 2 font families, applied via font-sans/font-serif/font-mono classes.- One border radius token app-wide. Subtle shadows only (shadow-sm or hairline borders).- Spacing via Tailwind scale (p-4, gap-6); never arbitrary values (p-[16px]) or space-* classes.### Layout- Mobile-first: base classes = mobile, md:/lg: = enhancement. Test at 375px.- Flexbox default; grid for true 2D layouts only. No absolute positioning for layout.- Prefer asymmetric splits and bento grids over identical card triplets.### Hierarchy- One visually dominant element per screen — the one serving the screen's primary job.- Secondary content uses text-muted-foreground. Data uses tabular-nums.- Headings get text-balance; body text line-height 1.4-1.6, minimum 14px.### States & copy- Every list/table/async view ships with empty (CTA included), loading  (layout-matched skeleton), error (with retry), and success states.- Buttons name outcomes ("Create invoice"), never "Submit"/"OK".- Errors: what happened + how to fix it. No "Oops", no exclamation marks.### Motion- 150-300ms, ease-out, transform/opacity only, state changes only.- Respect prefers-reduced-motion. No looping/idle animation.### Banned- Purple/violet defaults, gradients (unless requested), emoji as icons,  decorative blobs, spinners for content areas, dark patterns (fake urgency,  pre-checked add-ons, hidden costs).### Verification- Render and inspect changed UI at mobile + desktop widths before finishing.- Check: dominant element correct, no overflow/wrap breaks, contrast holds,  all four states reachable.

Output 6: Design Test Prompts

“Design a landing page for a bookkeeping app.” — Expected: trust-forward, real product UI in hero, specific copy, no purple gradient. Fails if: generic centered hero with badge-pill and emoji features.

“Make this dashboard look better.” (+ screenshot) — Expected: keeps brand tokens, fixes padding/hierarchy with exact values. Fails if: rebrands colors and fonts.

“Critique this signup page.” (+ screenshot) — Expected: names screen’s job, ordered critique, 2 lead fixes with classes. Fails if: “feels cluttered, could be more modern.”

“Design a pricing page that converts.” — Expected: honest “popular” highlight, clear tiers, single CTA logic. Fails if: countdown timers, pre-checked add-ons.

“Build a settings page.” — Expected: type hierarchy + hairline dividers, minimal boxes, outcome-named actions. Fails if: every setting in a heavy card with an icon.

“Add a data table for orders.” — Expected: dense, tabular-nums, muted headers, empty/loading/error states included. Fails if: airy marketing spacing, spinner-only loading.

“Make the app feel more delightful.” — Expected: one signature moment at a milestone, calm elsewhere. Fails if: confetti and bounces on every interaction.

“Design mobile checkout.” — Expected: single column, collapsed summary, sticky pay button, 44px targets. Fails if: shrunken desktop layout.

“Here’s our brand color (#0D6E4F). Build the homepage.” — Expected: builds full token system around it, accent used sparingly. Fails if: introduces competing accent colors.

“Write the empty state for a new user’s projects page.” — Expected: one orientation line + first-action CTA, spoken tone. Fails if: “No data available.”

Scoring per prompt: job identified? hierarchy correct (one loudest element)? constraint held (colors/fonts/spacing)? states/copy handled? verified visually? — 1 point each, 50 total.

If you only transfer two rules, take “name the screen’s one job before laying anything out” and “one loudest element per screen” — most design quality differences trace back to those.
