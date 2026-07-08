# Helix Behavior & Psychology Map

Purpose: make user behavior and psychology the first-class driver of UI/UX generation.

## Mandatory trigger
Use before substantial UI work, especially:
- landing pages and conversion flows
- onboarding, pricing, checkout, upgrade
- dashboards that must drive decisions
- habit/retention loops
- any redesign where user anxiety or motivation matters

## Required behavior map
Create a behavior map before visual variants:
- target user/persona
- trigger/context
- current emotional state
- current belief
- desired belief after the screen/flow
- primary action
- secondary action
- blockers/anxieties
- ethical psychology strategy
- above-the-fold behavioral requirement
- measurement signals

Use `schemas/behavior-map.schema.json`.

## Psychology models to select from
Do not dump every model. Pick the few that fit.

| Model | Use |
|---|---|
| Fogg Behavior Model | motivation + ability + prompt for the target action |
| Cognitive Load Theory | reduce unnecessary complexity while keeping needed trust detail |
| System 1 / System 2 | fast recognition first, transparent details second |
| Trust Equation | credibility + reliability + intimacy - self-orientation |
| Loss Aversion | only when tied to real user-owned value or risk |
| Endowment Effect | let users preview/own a result before commitment |
| Commitment/Consistency | smallest meaningful next step |
| Hick's Law | reduce above-fold choice count |
| Goal Gradient | make progress toward value visible |
| Peak-End Rule | memorable first insight and final state |
| Social Proof | only real, specific proof; never fake logos/testimonials |

## Behavioral hypothesis format
Every variant needs:
```text
If we [design intervention], then [target user] will [behavior/belief shift], because [psychological mechanism], measured by [observable signal].
```

## Drift example
Target user: household/couple worried spending has drifted.
Current belief: "We do not know if this is inflation, habit creep, or one-offs."
Desired belief: "Drift separates the causes calmly and helps us make one decision together."
Blockers: bank access fear, daily logging fatigue, blame anxiety, another-dashboard fatigue.
Design response: show Money Weather proof before signup, put no-bank-login beside CTA, ask for email only.
