# Helix Eval Harness

Helix quality must be measured, not felt.

## Eval types
1. **Prompt-only smoke tests** — use `helix_eval.py` to create timestamped prompt/rubric packs.
2. **Model runs** — use `helix_eval.py --run-model` to call `hermes chat -q` with and without `-s helix-system`.
3. **Human/AI scoring** — use `score_output.py` for heuristic pre-score, then a verifier agent or human for final score.

## Required comparisons
- Same prompt and context.
- Same model/provider when possible.
- Randomized A/B labels for human judging.
- Score dimensions independently; do not let fluent writing hide generic output.
