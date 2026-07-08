# Helix Product Strategy Layer

## How to Identify the Product Loop
The loop is the repeated cycle: **trigger → action → reward → reinvestment** that brings the user back. Find it by asking: "What does the user do the *second* time they open this, and why?" If there's no answer, there's no product yet — only a feature.
- Example: a habit app's loop is *reminder → check-in → streak grows → streak raises the cost of quitting*. Everything else (themes, stats, social) either feeds this loop or is decoration.

## How to Define the User
One persona, one sentence, with a constraint that shapes design: "A freelance designer juggling 5 clients who loses billable hours to invoice admin." Not "creatives," not "busy professionals." A user you can't picture is a user you can't design for.

## How to Define the Job-to-be-Done
The outcome they'd pay for, phrased without your product in it: "Get paid faster without chasing clients" — not "use our invoicing dashboard." Test: if a competitor did the job better, the user would switch — that's the job.

## How to Define the Wedge
The narrowest entry point where you can be clearly best on day one. Pick by intersecting: (a) an underserved segment, (b) a moment of acute pain, (c) something incumbents structurally won't do. Reject wedges that require being better at everything.

## How to Define USP
One sentence: "The only <category> that <specific capability> for <specific user>." If the sentence works with a competitor's name substituted in, it's not a USP — sharpen until it doesn't.

## How to Prioritize Features
Score every candidate: **Does it strengthen the core loop?** (Yes/No — No means backlog, not "later phase"). Then rank survivors by: pain severity × frequency ÷ build cost. Feature *ideas* are cheap and additive; product *loops* are singular — protect the loop from the ideas.

## How to Decide MVP
MVP = the smallest version where the *entire loop* completes. Not the smallest feature list — a complete but narrow loop beats a broad but broken one.
- Bad MVP: invoicing app with clients, invoices, dashboard, settings — but payment isn't wired up (loop broken).
- Good MVP: create invoice → send → client pays → money lands. Four screens, complete loop.

## How to Connect Design with Product Strategy
The design differentiator must express the USP visually. If the USP is "fastest," the design differentiator is aggressive speed cues (instant transitions, zero-confirmation flows, keyboard-first). Design decisions that don't map to strategy default to generic — which is how every AI-built app ends up looking the same.

## How to Avoid Building Generic Apps
- Ban the default: if the first idea is a dashboard with cards + sidebar + stats, it's the generic answer. Ask what the *loop* needs and design that screen instead.
- Every project gets one memorable, opinionated element (an interaction, a layout, a data view) that a template wouldn't have.
- Name the anti-persona: who is this deliberately *not* for? Generic apps have no anti-persona.

## How to Create a Build Roadmap
- **Phase 1 — Loop:** the complete core loop, ugly-but-real data flow. Ship when one user can complete it.
- **Phase 2 — Retention:** the mechanics that make the second visit better than the first (history, streaks, saved state, notifications).
- **Phase 3 — Expansion:** adjacent jobs for the same user (not new users).
Rule: no phase may contain a feature that can't be traced to a loop step. Each phase ends with something usable, never with infrastructure alone.

## One-Page Strategy Template
```markdown
# <Product> Strategy
**User:** <one persona, one sentence>
**Job-to-be-done:** <outcome, product-free phrasing>
**Core loop:** <trigger> → <action> → <reward> → <reinvestment>
**Wedge:** <narrow entry + why we win it>
**USP:** The only ___ that ___ for ___.
**Design differentiator:** <the visual/interaction expression of the USP>
**MVP:** <the smallest complete loop, ≤7 items>
**Not doing:** <≥5 tempting things, banned>
**Roadmap:** P1 loop / P2 retention / P3 expansion — one line each
```
