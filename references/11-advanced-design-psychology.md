# Helix Advanced Design Psychology

**Purpose**: make Helix best-in-class at ethical design psychology for product, onboarding, conversion, retention, trust, and decision-making.

This extends `ux-psychology-principles.md`. It is not a bag of dark patterns. Helix uses psychology to reduce confusion and align the user's motivation with real value.

## Ethical Line

Use psychology to:
- reduce uncertainty
- reveal value earlier
- make progress legible
- increase user control
- prevent errors
- build deserved trust

Do not use psychology to:
- obscure cost
- manufacture false urgency
- trick users into commitments
- hide destructive actions
- exploit fear without user benefit

## Core Models

### Fogg Behavior Model
Behavior happens when **motivation + ability + prompt** converge.

For every target action, ask:
| Dimension | Question | Design implications |
|---|---|---|
| Motivation | Why would the user care now? | relevance, payoff, urgency grounded in value |
| Ability | How easy is the action? | defaults, fewer fields, chunking, previews |
| Prompt | What asks at the right moment? | CTA, inline nudge, state-based prompt |

If motivation is low, do not merely make the button louder. Increase value clarity.  
If ability is low, reduce steps before adding persuasion.

### BJ Fogg Tiny Habits / Starter Step
Ask for the smallest meaningful action that creates momentum.

Examples:
- not "Create full workspace" → "Import one file"
- not "Configure automation" → "Choose your first trigger"
- not "Start trial" → "Preview your first result"

### Cialdini Principles (ethical use)
| Principle | Ethical design use | Abuse to avoid |
|---|---|---|
| Reciprocity | give a useful demo/sample before signup | fake freebies with hidden cost |
| Commitment/Consistency | small progressive steps | trapping users after sunk cost |
| Social Proof | specific credible proof | fake logos/testimonials |
| Authority | expert evidence, compliance, citations | vague badges |
| Liking | brand voice that resonates | manipulative flattery |
| Scarcity | real capacity limits | fake countdowns |
| Unity | community identity | exclusionary pressure |

### Kahneman/System 1 and 2
- System 1: fast recognition, emotion, pattern matching.
- System 2: deliberate comparison, pricing, trust review.

Great UI supports both:
- clear first impression for System 1
- transparent details for System 2

### Cognitive Load Theory
Lower extraneous load:
- chunk forms
- show one primary action
- use plain labels
- progressive disclosure
- align visual grouping to mental grouping

Do not remove germane load: users sometimes need enough detail to trust a serious decision.

### Hick's Law
More choices increase decision time. Use:
- default recommendation
- comparison framing
- grouping
- "best for" labels

### Miller's Law / Chunking
Group related items into 3-5 chunks. Avoid flat long lists.

### Peak-End Rule
Users judge experiences disproportionately by the emotional peak and ending. Make:
- first success moment memorable
- completion state rewarding and clear
- error recovery respectful

### Zeigarnik Effect / Open Loops
Incomplete tasks stay mentally active. Use carefully:
- progress indicators
- saved drafts
- "continue setup" nudges

Never create artificial incomplete loops just to nag.

### Endowment Effect
Users value what they feel they already own. Let them create/preview before asking them to commit.

### Loss Aversion
Use only for real user-owned value:
- "Your draft will be lost" is valid.
- "You will miss out forever" without real scarcity is not.

### Anchoring and Contrast
Use honest comparison:
- before/after
- current workflow vs improved workflow
- plan comparison with real differences

Do not anchor with fake inflated prices or fake baselines.

### Trust Equation
Trust = credibility + reliability + intimacy - self-orientation.

Design implications:
- credible evidence
- stable states
- clear privacy/permission copy
- show user benefit before company benefit

## Design Psychology Checklist

For any commitment flow:

- [ ] What belief must change before the user acts?
- [ ] What is the user's primary anxiety?
- [ ] What is the smallest meaningful next step?
- [ ] Is value shown before the ask?
- [ ] Are defaults helpful and reversible?
- [ ] Does progress feel real?
- [ ] Is social proof specific and credible?
- [ ] Is scarcity/urgency real or removed?
- [ ] Does the CTA name the outcome, not just the action?
- [ ] Does the completion state create confidence?

## Psychology Scoring Rubric (50 pts)

| Dimension | Points |
|---|---:|
| User motivation clarity | 5 |
| Ability/friction reduction | 5 |
| Prompt timing and CTA quality | 5 |
| Value before ask / reciprocity | 5 |
| Ethical progress / goal gradient | 5 |
| Trust and credibility | 5 |
| Cognitive fluency | 5 |
| Autonomy and control | 5 |
| Emotional peak/end state | 5 |
| Ethical integrity | 5 |

Any dark-pattern violation caps score at 25.

## Psychological Brief Template

```markdown
## Target Behavior
<what user should do>

## Current Resistance
- Motivation gap:
- Ability gap:
- Trust gap:
- Timing gap:

## Psychological Strategy
- Primary mechanism:
- Supporting mechanisms:
- Ethical guardrail:

## Design Moves
- Copy:
- Layout:
- Interaction:
- Proof:
- Default:

## Measurement
- User behavior:
- Qualitative signal:
- Failure signal:
```

## Best-in-Class Standard

A Helix design should be able to answer: *why will this exact user make this exact decision here, and how do we know the design helped rather than manipulated?*
