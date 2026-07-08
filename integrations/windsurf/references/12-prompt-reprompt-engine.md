# Helix Prompt Re-Prompt Engine

**Purpose**: turn messy user input into the best possible working brief without exposing prompt-engineering scaffolding unless the user asks.

This extends `08-intake-sufficiency-prompt-restructuring.md`.

## Core Concept

Users should not need to know how to prompt. Helix should:
1. listen carefully
2. identify missing information
3. ask only the questions that matter
4. rewrite the task internally into an expert-grade brief
5. execute from that brief
6. optionally show a concise "Reprompted Brief" if it helps alignment

This is the user-facing wedge: **Helix makes every user better at prompting without making them learn prompt engineering.**

## Three Modes

### Silent Reprompt (default)
Use when the task is clear enough.

- Parse user intent.
- Fill safe assumptions.
- Build internal enhanced brief.
- Execute.
- Do not show the reprompt unless useful.

### Clarifying Reprompt
Use when missing info would materially change the result.

Ask 1-3 questions, max:
```text
To produce the right <artifact> without guessing <risk>, I need:
1. <specific missing input>
2. <specific missing input>
3. <specific missing input>
```

No generic questionnaires.

### Visible Reprompt
Use when the user wants a prompt, handoff, or when alignment is high-stakes.

Output:
```markdown
## Reprompted Brief
Goal:
Context:
Constraints:
Success criteria:
Required references:
Verification:
```

Then either ask approval or execute, depending on risk.

## Reprompt Transformation Pipeline

### 1. Normalize intent
Turn raw language into:
- desired artifact
- target audience/user
- context/source material
- constraints
- success criteria
- verification method
- risk areas

### 2. Add expert frame
Pick the right stance:
- senior product designer
- conversion psychologist
- principal frontend engineer
- research synthesizer
- systems architect
- launch strategist
- prompt architect

### 3. Decompose into jobs
Break task into 3-7 jobs:
- understand/context gather
- design/strategy decision
- artifact creation
- verification
- handoff/iteration

### 4. Inject mode-specific standards
Examples:
- Design: design reasoning + psychology + tokens + visual proof
- Code: repo pattern first + tests + minimal diff
- GTM: user/JTBD/wedge/channel/proof/launch assets
- Research: decision question + sources + pattern/gap/recommendation

### 5. Add verification before execution
Define how the output will be proven.

### 6. Remove scaffolding from user-facing answer
The user sees the artifact, not a prompt-engineering seminar.

## Prompt Pattern Library

### Vague design input
Raw:
```text
Make onboarding better.
```

Internal reprompt:
```markdown
Act as a senior product designer and behavioral UX strategist. Improve the onboarding flow for [product] by identifying the target user, current resistance, desired activation event, and psychological levers. If product/user/flow are unknown, ask up to 3 targeted questions. Once sufficient, define the behavioral hypothesis, propose the flow, design-system implications, copy strategy, and verification plan with mobile/desktop screenshot requirements.
```

### Vague code input
Raw:
```text
Fix the dashboard.
```

Internal reprompt:
```markdown
Act as a principal engineer in this repo. First inspect the dashboard route, related components, package scripts, and existing patterns. Identify the specific failure or weakness from evidence. Apply the smallest safe fix, run relevant checks, and summarize changed files + verification. Ask only if the target bug/desired behavior cannot be inferred from repo state.
```

### Vague GTM input
Raw:
```text
We need go to market.
```

Internal reprompt:
```markdown
Act as a founder/marketing strategist. Create a GTM plan for Helix based on current repo capabilities and competitor positioning. Include ICP, wedge, positioning, launch narrative, distribution channels, proof assets, pricing hypothesis, 30/60/90 plan, and metrics. Ground claims in inspected repo evidence and competitor dissection.
```

## Reprompt Quality Rubric

| Dimension | Pass condition |
|---|---|
| Intent fidelity | preserves the user's actual ask |
| Specificity | names artifact, audience, constraints |
| Non-hallucination | flags unknowns instead of inventing |
| Expertise | selects the right role and standards |
| Verification | defines proof before execution |
| Brevity | no needless meta verbosity |
| Portability | works in Claude/Codex/Hermes |

## Output Contract

When user asks for the prompt itself:
- provide clean prompt block
- include variables/slots
- include success criteria
- include verification instruction

When user asks for work:
- use reprompt internally
- execute
- provide final artifact + verification

## Failure Modes

- Asking too many questions.
- Showing the hidden chain instead of executing.
- Over-rewriting the ask into a different goal.
- Adding fake constraints.
- Using prompt buzzwords without verification.

## Best-in-Class Standard

The user should feel: "I said it roughly, and Helix understood the professional version of what I meant."
