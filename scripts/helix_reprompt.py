#!/usr/bin/env python3
"""
Helix Prompt Re-Prompt Helper

Turns raw user input into a structured reprompt brief. This is intentionally lightweight and deterministic: it helps host agents perform Helix intake consistently without calling an LLM.

Usage:
  python scripts/helix_reprompt.py --input "make onboarding better" --mode design
  python scripts/helix_reprompt.py --input-file request.txt --visible
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MODE_KEYWORDS = {
    "design": ["design", "ui", "ux", "screen", "onboarding", "checkout", "landing", "visual", "component"],
    "code": ["fix", "bug", "implement", "repo", "test", "build", "error", "component", "api"],
    "gtm": ["go to market", "gtm", "launch", "positioning", "market", "pricing", "distribution"],
    "research": ["research", "compare", "competitor", "find", "study", "papers", "resources"],
    "meta": ["improve helix", "self", "agent", "prompt", "reprompt", "swarm", "persona"],
}

REQUIRED_BY_MODE = {
    "design": ["target user/persona", "current flow or artifact", "success metric", "brand/design constraints", "verification viewports"],
    "code": ["repo/path", "desired behavior or bug evidence", "commands/tests", "scope boundaries"],
    "gtm": ["product promise", "target customer", "proof/assets", "business model", "launch goal"],
    "research": ["decision question", "scope", "recency needs", "source quality threshold"],
    "meta": ["target subsystem", "failure evidence", "success metric", "portability constraints"],
}

REFERENCE_BY_MODE = {
    "design": ["10-design-reasoning-engine.md", "11-advanced-design-psychology.md", "design-masterclass.md", "design-system-first.md", "browser-visual-verification.md"],
    "code": ["coding.md", "verification.md", "03-verifier-subagents.md"],
    "gtm": ["GO_TO_MARKET.md", "research/agency-agents-dissection-2026-07.md", "product-strategy.md"],
    "research": ["research.md", "02-evidence-ledger.md"],
    "meta": ["07-self-improvement.md", "09-swarm-orchestration.md", "12-prompt-reprompt-engine.md"],
}


def detect_mode(text: str) -> str:
    low = text.lower()
    scores = {mode: sum(1 for kw in kws if kw in low) for mode, kws in MODE_KEYWORDS.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "general"


def missing_slots(text: str, mode: str) -> list[str]:
    low = text.lower()
    req = REQUIRED_BY_MODE.get(mode, [])
    missing = []
    for item in req:
        terms = re.split(r"[/ ]+", item.lower())
        if not any(t and t in low for t in terms if len(t) > 3):
            missing.append(item)
    return missing[:3]


def make_brief(text: str, mode: str | None = None) -> dict:
    mode = mode or detect_mode(text)
    missing = missing_slots(text, mode)
    return {
        "raw_input": text,
        "detected_mode": mode,
        "sufficiency": "needs_clarification" if missing else "sufficient_with_assumptions",
        "critical_questions": [f"What is the {m}?" for m in missing],
        "reprompted_brief": {
            "goal": text.strip(),
            "expert_frame": {
                "design": "senior product designer + behavioral UX strategist + frontend verifier",
                "code": "principal engineer in the target repo",
                "gtm": "founder-led GTM strategist for a developer/agent product",
                "research": "skeptical decision-oriented research synthesizer",
                "meta": "agent harness architect and evaluator",
            }.get(mode, "senior execution partner"),
            "required_references": REFERENCE_BY_MODE.get(mode, ["00-operating-contract.md", "08-intake-sufficiency-prompt-restructuring.md"]),
            "success_criteria": "Produce a concrete artifact, ground assumptions, and verify before claiming completion.",
            "verification": "Define evidence first, then execute and report exact evidence observed.",
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", help="raw user input")
    ap.add_argument("--input-file")
    ap.add_argument("--mode", choices=list(MODE_KEYWORDS) + ["general"])
    ap.add_argument("--visible", action="store_true", help="print markdown instead of JSON")
    args = ap.parse_args()

    text = args.input or (Path(args.input_file).read_text() if args.input_file else "")
    if not text.strip():
        raise SystemExit("Provide --input or --input-file")
    brief = make_brief(text, args.mode)

    if args.visible:
        rb = brief["reprompted_brief"]
        print("# Reprompted Brief")
        print(f"Mode: {brief['detected_mode']}")
        print(f"Sufficiency: {brief['sufficiency']}")
        if brief["critical_questions"]:
            print("\n## Clarifying Questions")
            for i, q in enumerate(brief["critical_questions"], 1):
                print(f"{i}. {q}")
        print("\n## Working Brief")
        print(f"Goal: {rb['goal']}")
        print(f"Expert frame: {rb['expert_frame']}")
        print("References: " + ", ".join(rb["required_references"]))
        print(f"Success criteria: {rb['success_criteria']}")
        print(f"Verification: {rb['verification']}")
    else:
        print(json.dumps(brief, indent=2))


if __name__ == "__main__":
    main()
