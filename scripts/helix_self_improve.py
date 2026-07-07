#!/usr/bin/env python3
"""
Helix Self-Improvement Driver
Drives the meta-loop: detect, scope, baseline, research, variant, tournament, repair, lesson, propose patch.

Usage examples:
  python scripts/helix_self_improve.py --area "mode-router" --brief "ensure UX psychology loads for all commitment flows"
  python scripts/helix_self_improve.py --area "eval-harness" --limit 5
  python scripts/helix_self_improve.py --full-health-check
"""
from __future__ import annotations
import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List

AGENT = Path(__file__).resolve().parents[1]
EVALS = AGENT / "evals" / "self-improvement"
EVALS.mkdir(parents=True, exist_ok=True)

def run_cmd(cmd: List[str], timeout=120) -> Dict:
    try:
        result = subprocess.run(cmd, cwd=AGENT, capture_output=True, text=True, timeout=timeout)
        return {"cmd": " ".join(cmd), "stdout": result.stdout[-2000:], "stderr": result.stderr[-500:], "returncode": result.returncode}
    except Exception as e:
        return {"cmd": " ".join(cmd), "error": str(e)}

def load_reference(name: str) -> str:
    p = AGENT / "references" / name
    return p.read_text() if p.exists() else f"Reference {name} not found"

def baseline_eval(area: str) -> Dict:
    """Run relevant existing harness for baseline."""
    if "design" in area or "ui" in area:
        return run_cmd(["python", "scripts/helix_design_tournament.py", "--brief", f"baseline for {area}", "--variants-json", "evals/design-tournaments/sample-helix-ui-variants.json"])
    else:
        # Fall back to general eval prep
        return run_cmd(["python", "scripts/helix_eval.py", "--limit", "3"])

def research(area: str) -> Dict:
    """Pull external patterns."""
    if "design" in area or "onboard" in area:
        return run_cmd(["python", "scripts/helix_design_research.py", "--limit", "8"])
    return {"note": "General research not yet scripted for this area. Load external-agent-patterns.md manually."}

def generate_variants(area: str, brief: str, baseline: Dict) -> List[Dict]:
    """Simple heuristic variants. In full version this would call an LLM with the brief + references."""
    variants = [
        {"name": f"{area}-current", "change": "No change (baseline)", "score_hint": "current"},
        {"name": f"{area}-explicit-check", "change": f"Add explicit load of relevant reference in mode-router and critique for {brief}", "score_hint": "likely +8-15"},
        {"name": f"{area}-lesson-gated", "change": "Require a lesson update + evidence before accepting change in this area", "score_hint": "higher durability"},
    ]
    return variants

def score_variants(variants: List[Dict], area: str) -> List[Dict]:
    """Stub scoring. Integrate with score_output.py or rubric in real runs."""
    for v in variants:
        v["score"] = 50 + (10 if "explicit" in v["name"] else 0) + (15 if "lesson" in v["name"] else 0)
    return sorted(variants, key=lambda x: x.get("score", 0), reverse=True)

def extract_lesson(area: str, winner: Dict, brief: str) -> str:
    ts = datetime.now().strftime("%Y%m%d")
    lesson = f"""# Lesson: {area} improvement - {ts}

**Trigger:** {brief}
**Change adopted:** {winner['name']} — {winner['change']}
**Evidence:** See self-improvement run in evals/self-improvement/
**Rule for future:** When working on {area}, always load 07-self-improvement.md + relevant reference. Require before/after evidence.

**Verification:** Re-run the same brief after change and confirm score lift.
"""
    return lesson

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--area", default="general")
    ap.add_argument("--brief", default="improve Helix self-diagnosis and update quality")
    ap.add_argument("--limit", type=int, default=4)
    ap.add_argument("--full-health-check", action="store_true")
    args = ap.parse_args()

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = EVALS / ts
    out_dir.mkdir(parents=True)

    print(f"=== Helix Self-Improvement Run {ts} ===")
    print(f"Area: {args.area}")
    print(f"Brief: {args.brief}")

    manifest = {
        "timestamp": ts,
        "area": args.area,
        "brief": args.brief,
        "steps": []
    }

    # 1. Baseline
    print("\n[1] Baseline")
    baseline = baseline_eval(args.area)
    manifest["baseline"] = baseline
    (out_dir / "01_baseline.json").write_text(json.dumps(baseline, indent=2))

    # 2. Research
    print("\n[2] Research external patterns")
    research_result = research(args.area)
    manifest["research"] = research_result

    # 3. Variants
    print("\n[3] Generate variants")
    variants = generate_variants(args.area, args.brief, baseline)
    scored = score_variants(variants, args.area)
    manifest["variants"] = scored
    (out_dir / "03_variants.json").write_text(json.dumps(scored, indent=2))

    winner = scored[0]
    print(f"Winner: {winner['name']} (score {winner.get('score')})")

    # 4. Lesson
    lesson = extract_lesson(args.area, winner, args.brief)
    lesson_file = AGENT / "lessons" / args.area / f"{ts}-{args.area}.md"
    lesson_file.parent.mkdir(parents=True, exist_ok=True)
    lesson_file.write_text(lesson)
    manifest["lesson_file"] = str(lesson_file.relative_to(AGENT))

    # 5. Proposal
    proposal = {
        "recommendation": f"Adopt {winner['name']}",
        "change": winner["change"],
        "evidence_dir": str(out_dir),
        "next_steps": [
            "Load 07-self-improvement.md + relevant references",
            "Apply the change to the target file(s)",
            "Re-run this script as verification",
            "Update handoff or commit with evidence"
        ]
    }
    (out_dir / "05_proposal.json").write_text(json.dumps(proposal, indent=2))
    manifest["proposal"] = proposal

    # 6. Full report
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(f"\n=== Self-improvement run complete ===")
    print(f"Evidence: {out_dir}")
    print(f"Proposed lesson: {lesson_file}")
    print("Load references/07-self-improvement.md and the generated proposal for next action.")

if __name__ == "__main__":
    main()
