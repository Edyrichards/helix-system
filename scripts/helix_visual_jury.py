#!/usr/bin/env python3
"""Helix Visual Jury: score rendered UI artifacts using behavior + visual criteria.

Input is a JSON object with a `variants` list. Each variant may include:
- name
- html_path or screenshot_paths
- behavior_map
- reference_patterns
- notes

This helper performs deterministic text/probe scoring only. Pair it with human or
vision-model review for final judgment.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CRITERIA = {
    'recognition': ['problem', 'why', 'changed', 'for you', 'household', 'review'],
    'anxiety_reduction': ['calm', 'no blame', 'not your fault', 'safe', 'control', 'no bank login'],
    'trust': ['export', 'privacy', 'paid product', 'optional', 'data', 'no ads'],
    'action': ['get early access', 'join', 'email', 'start', 'demo'],
    'reference_quality': ['pattern', 'reference', 'mobbin', 'adapted', 'do not copy'],
    'anti_slop_avoidance': ['testimonial', 'trusted by', 'purple', 'seamless', 'elevate', 'unleash', '—', '–'],
}

WEIGHTS = {
    'recognition': 15,
    'anxiety_reduction': 15,
    'trust': 10,
    'action': 10,
    'reference_quality': 10,
}


def text_for_variant(v: dict, base: Path) -> str:
    parts = [json.dumps(v, ensure_ascii=False)]
    html = v.get('html_path')
    if html:
        path = (base / html).resolve() if not Path(html).is_absolute() else Path(html)
        if path.exists():
            parts.append(path.read_text(errors='replace'))
    return '\n'.join(parts)


def score_variant(v: dict, base: Path) -> dict:
    text = text_for_variant(v, base)
    low = text.lower()
    breakdown = {}
    total = 0.0
    for key, terms in WEIGHTS.items():
        hits = sum(1 for t in CRITERIA[key] if t in low)
        pts = min(hits / len(CRITERIA[key]), 1) * terms
        breakdown[key] = {'hits': hits, 'possible': len(CRITERIA[key]), 'points': round(pts, 1)}
        total += pts
    anti_hits = [t for t in CRITERIA['anti_slop_avoidance'] if t.lower() in low]
    penalty = min(len(anti_hits) * 4, 24)
    breakdown['anti_slop_penalty'] = {'hits': anti_hits, 'points': -penalty}
    total -= penalty
    # Browser/probe data can be injected by upstream screenshot harness.
    probe = v.get('probe', {})
    if probe:
        bonus = 0
        if probe.get('no_horizontal_overflow') is True:
            bonus += 5
        if probe.get('console_errors', 1) == 0:
            bonus += 5
        if probe.get('cta_visible_above_fold') is True:
            bonus += 5
        breakdown['browser_bonus'] = {'points': bonus}
        total += bonus
    return {**v, 'score': round(max(0, min(100, total)), 1), 'breakdown': breakdown}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--variants-json', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    data = json.loads(args.variants_json.read_text())
    variants = data.get('variants', data if isinstance(data, list) else [])
    scored = sorted((score_variant(v, args.variants_json.parent) for v in variants), key=lambda x: x['score'], reverse=True)
    report = {'winner': scored[0] if scored else None, 'variants': scored}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(args.out)
    if scored:
        print(f"winner={scored[0].get('name', 'unnamed')} score={scored[0]['score']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
