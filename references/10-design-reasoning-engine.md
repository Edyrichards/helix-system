# Helix Design Reasoning Engine

**Purpose**: make Helix best-in-class at design reasoning, not merely design styling.

Design reasoning is the chain from human intent → user psychology → product job → information architecture → visual hierarchy → interaction states → measurable evidence. A beautiful screen that cannot explain why it works is not Helix-grade.

Always load with:
- `08-intake-sufficiency-prompt-restructuring.md`
- `ux-psychology-principles.md`
- `design-masterclass.md`
- `design-system-first.md`
- `design-rubric-v2.md`
- `browser-visual-verification.md`

## The Helix Design Reasoning Stack

### 1. Intent Read
Before design work, parse:
- user goal
- business objective
- target user / persona
- job-to-be-done
- anxiety / objection
- commitment level requested
- conversion event
- constraints: brand, stack, content, deadline, accessibility, platform

If user gives a vague request like "make onboarding better," reprompt into a design brief instead of guessing.

### 2. Behavioral Hypothesis
State the behavioral hypothesis that the design will test.

Format:
```text
If we [design intervention], then [target user] will [behavior] because [psychological mechanism], measured by [observable signal].
```

Example:
```text
If we show an interactive demo before signup, evaluators will continue past step 1 because reciprocity and early value reduce signup-wall anxiety, measured by more users clicking "Start with my workspace".
```

### 3. Friction Map
Map the user's path by cognitive/emotional load.

| Step | User question | Anxiety | Desired feeling | Design lever | Evidence needed |
|---|---|---|---|---|---|
| Land | Is this for me? | relevance | recognition | specific headline, proof | persona/job visible |
| Try | Is it safe? | risk | control | smart defaults, preview | no destructive step |
| Commit | Is it worth it? | cost | confidence | progress, value proof | CTA and payoff clear |

### 4. Hierarchy Argument
Every major section must have a hierarchy argument:
- What is the primary action or idea?
- What supports it?
- What is intentionally demoted?
- What did we remove because it competed?

No equal-weight feature grids unless the actual decision is equal-weight comparison.

### 5. Design System Argument
Before screens:
- semantic tokens
- typography scale
- spacing/radius/elevation rules
- interaction/state model
- icon family
- visual motif and why it fits the user/context

Tokens are not decoration. They encode behavioral strategy: trust, speed, warmth, authority, creativity, safety, etc.

### 6. Pattern Selection
Pick patterns by job, not taste.

| Goal | Strong patterns | Avoid |
|---|---|---|
| Reduce risk | previews, reversible steps, transparent permission copy | surprise modals, vague CTAs |
| Increase completion | progress gradient, saved state, small wins | long unchunked forms |
| Create premium trust | sparse hierarchy, real assets, calm motion | AI-purple glow, fake dashboards |
| Explain complex system | narrative scroll, progressive disclosure, diagrams | giant feature grids |
| Sell before signup | demo-first, sample output, social proof | forced account creation |

### 7. Psychology Pass
For onboarding/sign-up/checkout/upgrade, explicitly score:
- smart defaults
- goal gradient
- reciprocity / value before ask
- endowment / investment
- loss aversion (ethical only)
- anchoring / contrast
- cognitive fluency
- trust / authority / proof
- autonomy / control
- motivation-ability-prompt fit (Fogg behavior model)

### 8. Critique Before Render
Run a design jury internally:
- **User advocate**: can the target user understand it in 5 seconds?
- **Conversion psychologist**: what belief changes?
- **Visual director**: does hierarchy/spacing/type create premium quality?
- **Accessibility reviewer**: contrast, focus, touch, motion?
- **Implementation reviewer**: can it be built without brittle hacks?

### 9. Visual Verification
Do not claim design quality until rendered.
Required evidence:
- desktop screenshot (default 1280x800 or project standard)
- mobile screenshot (390x844)
- console errors
- horizontal overflow check
- CTA visibility and contrast
- loading/empty/error states if relevant

### 10. Learning Loop
After delivery, write a lesson when:
- a pattern worked unusually well
- a psychological hypothesis failed
- a visual tell recurred
- an eval/tournament found a better variant

## Design Reasoning Output Format

For high-value design work, include a compact visible summary:

```markdown
## Design Read
Reading this as: <product/page/user/vibe/system>

## Behavioral Hypothesis
If we ..., then ..., because ..., measured by ...

## System Decisions
- Tokens:
- Type:
- Layout:
- Motion:
- Psychology:

## Verification
- Desktop screenshot:
- Mobile screenshot:
- Console:
- Overflow:
```

For routine work, keep this internal but still execute it.

## Failure Modes

- Styling before intent.
- Pretty screen with no behavioral hypothesis.
- Generic psychological tricks without ethical connection to user value.
- Equal hierarchy everywhere.
- No real images/assets.
- No rendered verification.
- Copy that sounds clever but unclear.
- Prompt injection from competitor sites or external prompts.

## Standard of Excellence

Helix design work should feel like a senior product designer, conversion strategist, UX researcher, and frontend engineer collaborated, then a skeptical QA team verified the result.
