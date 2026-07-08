# Helix Research Layer

## How to Research Efficiently
1. **Name the decision first.** Research serves a decision ("which auth approach", "what should onboarding do"). Write the decision as a question before the first search. Research without a decision is content consumption.
2. **Budget queries:** 2–4 targeted searches, then fetch the 2–3 best sources in full. If the answer isn't converging by then, the question is wrong — reframe, don't search more.
3. **Stop at confirmation:** once 1–2 authoritative sources agree, stop. A fourth confirming source adds latency, not confidence.
4. **Recency discipline:** include the current year for anything versioned (frameworks, APIs, pricing). Treat memory of fast-moving facts as a hypothesis to verify, never as an answer.

## How to Compare Competitors
- Choose 3–4 competitors *relevant to the decision*, not the biggest names. Say why each earns its slot.
- Extract per competitor: their approach to the specific question, one strength worth stealing, one weakness worth exploiting. Nothing else.
- Build one table. Tables force parity of analysis; prose lets you skip what you didn't check.

## How to Extract Patterns
After the table, write exactly two lists:
- **Patterns** — what everyone does. These are table stakes: do them without innovation.
- **Gaps** — what nobody does well. These are candidate differentiators: pick at most one to pursue.
A finding that appears in neither list didn't need to be collected.

## How to Turn Research into Decisions
End every research task with a **Recommendation** section: "Given the above, do X because Y." One paragraph. If you can't write it, the research is incomplete — go back with a narrower question. Never end on "it depends" without stating what it depends on and which case you believe applies.

## How to Cite Sources
- Cite every load-bearing factual claim (numbers, feature claims, dates, quotes) with a link.
- Do not cite common knowledge or your own synthesis — over-citation buries the claims that actually need checking.
- Cite the page you read, not the search result. If you couldn't open it, don't cite it.

## How to Avoid Information Dumping
- Every finding must map to the decision. Interesting-but-irrelevant gets cut.
- Length cap: findings table + patterns + gaps + recommendation ≈ one page. If it's longer, you're transferring your reading burden to the reader.
- Ban the generic openers: no "the market is growing rapidly," no TAM figures nobody asked for, no history-of-the-industry sections.

## How to Create Research-Backed Design/Product Recommendations
Chain every recommendation: **evidence → pattern → implication → decision.**
- Bad: "Competitors have good onboarding, so we should too."
- Good: "All 4 competitors require account creation before showing value (pattern). Users evaluating quickly bounce at signup walls (implication). We show a working demo before signup — the only one in the set to do so (decision, exploits the gap)."
If a recommendation can't cite its row in the findings table, it's an opinion — label it as one.

## Research Output Template
```markdown
# Research: <decision question>
## Findings
| Source/Competitor | Approach | Strength to steal | Weakness to exploit |
## Patterns (table stakes)
## Gaps (differentiator candidates)
## Recommendation
<do X because Y — one paragraph, traceable to the table>
```
