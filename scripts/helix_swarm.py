#!/usr/bin/env python3
"""
Helix Swarm Orchestrator
Helps the Coordinator decompose goals, generate specialist briefs, and (optionally) run or simulate parallel execution.

Usage:
  python scripts/helix_swarm.py --goal "Build complete user onboarding with research, design tokens, implementation, and verification" --swarm-size 4

This script produces:
- Decomposition plan
- Briefs for each specialist
- Suggested personas to use or generate
- A ready-to-paste swarm execution prompt for the host model
- (Future) actual parallel dispatch where the environment supports it
"""

import argparse
import json
from pathlib import Path
from datetime import datetime

PERSONAS = {
    "swarm-coordinator": "personas/swarm-coordinator.md",
    "code-reviewer": "personas/code-reviewer.md",
    "design-specialist": "personas/design-specialist.md",
    "research-synthesizer": "personas/research-synthesizer.md",
}

def decompose_goal(goal: str, swarm_size: int = 4):
    """Simple heuristic decomposition. In real use the LLM Coordinator does the smart version."""
    base = [
        "Understand the problem space and extract decision-critical research",
        "Define or extend the design system + tokens with UX psychology",
        "Implement core flows / components following the system",
        "Review, verify, and produce evidence (screenshots, tests, checks)",
    ]
    return base[:swarm_size]

def generate_briefs(goal: str, subtasks: list):
    briefs = []
    for i, task in enumerate(subtasks):
        persona = list(PERSONAS.keys())[min(i, len(PERSONAS)-1)]
        brief = {
            "subtask_id": f"worker-{i+1}",
            "persona": persona,
            "sub_goal": task,
            "context_from_coordinator": goal,
            "required_outputs": ["evidence_ledger_slice", "artifact_or_spec", "verification_status"],
            "must_follow": ["08-intake-sufficiency-prompt-restructuring.md", "full Helix operating contract for this slice"],
        }
        briefs.append(brief)
    return briefs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--goal", required=True)
    parser.add_argument("--swarm-size", type=int, default=4)
    parser.add_argument("--output-dir", default="evals/swarms")
    args = parser.parse_args()

    subtasks = decompose_goal(args.goal, args.swarm_size)
    briefs = generate_briefs(args.goal, subtasks)

    plan = {
        "timestamp": datetime.utcnow().isoformat(),
        "original_goal": args.goal,
        "decomposition": subtasks,
        "briefs": briefs,
        "coordinator_instructions": "Use references/09-swarm-orchestration.md and the listed personas. Run full intake on the top goal first.",
        "suggested_next": "Load the Swarm Coordinator persona + 09-swarm-orchestration.md and execute the protocol.",
    }

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    out_file = out_dir / f"swarm-plan-{ts}.json"
    out_file.write_text(json.dumps(plan, indent=2))

    print(f"Swarm plan written to {out_file}")
    print("\n=== Quick Swarm Execution Prompt (copy into Claude/Cursor/etc) ===")
    print(f"""
You are the Helix Swarm Coordinator.

Goal: {args.goal}

Follow references/09-swarm-orchestration.md exactly.

Use these personas:
- personas/swarm-coordinator.md (you)
- {" ".join([f"personas/{p}.md" for p in list(PERSONAS.keys())[:args.swarm_size]])}

Decomposition suggested by script:
{chr(10).join(f"- {s}" for s in subtasks)}

Begin with full intake on the goal, then produce the decomposition and dispatch.
""")

if __name__ == "__main__":
    main()
