#!/usr/bin/env python3
"""Validate Helix personas for required schema and Helix spine."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PERSONAS = ROOT / "personas"
REQUIRED_FRONTMATTER = ["name", "type", "helix-role", "vibe", "when_to_use", "loads", "outputs"]
REQUIRED_BODY_TERMS = ["intake", "evidence", "verification", "workflow", "output"]


def parse_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("malformed YAML frontmatter")
    return parts[1]


def main() -> int:
    failures = []
    files = sorted(PERSONAS.glob("*.md"))
    if not files:
        failures.append("no personas found")
    for path in files:
        text = path.read_text()
        try:
            fm = parse_frontmatter(text)
        except Exception as exc:
            failures.append(f"{path.name}: {exc}")
            continue
        for key in REQUIRED_FRONTMATTER:
            if f"{key}:" not in fm:
                failures.append(f"{path.name}: missing frontmatter key {key}")
        low = text.lower()
        for term in REQUIRED_BODY_TERMS:
            if term not in low:
                failures.append(f"{path.name}: missing required Helix-spine term {term}")
    if failures:
        print("Persona validation FAILED")
        for f in failures:
            print("-", f)
        return 1
    print(f"Persona validation PASSED ({len(files)} personas)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
