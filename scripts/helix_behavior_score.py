#!/usr/bin/env python3
"""Create and validate behavior maps for Helix UI/UX work.

This helper is intentionally lightweight: it turns explicit CLI fields into a
schema-shaped behavior map that can be fed into UI Pro tournaments.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def split_items(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(';') if item.strip()]


def build(args: argparse.Namespace) -> dict:
    return {
        'project': args.project,
        'surface': args.surface,
        'target_user': args.target_user,
        'trigger': args.trigger,
        'current_emotional_state': args.current_emotional_state,
        'current_belief': args.current_belief,
        'desired_belief': args.desired_belief,
        'primary_action': args.primary_action,
        'secondary_action': args.secondary_action,
        'blockers': split_items(args.blockers),
        'psychology_models': split_items(args.psychology_models),
        'psychology_strategy': split_items(args.psychology_strategy),
        'above_fold_requirement': split_items(args.above_fold_requirement),
        'measurement_signals': split_items(args.measurement_signals),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description='Build a Helix behavior map JSON artifact')
    ap.add_argument('--project', required=True)
    ap.add_argument('--surface', required=True)
    ap.add_argument('--target-user', required=True)
    ap.add_argument('--trigger', default='')
    ap.add_argument('--current-emotional-state', default='')
    ap.add_argument('--current-belief', required=True)
    ap.add_argument('--desired-belief', required=True)
    ap.add_argument('--primary-action', required=True)
    ap.add_argument('--secondary-action', default='')
    ap.add_argument('--blockers', required=True, help='semicolon-separated')
    ap.add_argument('--psychology-models', default='Fogg Behavior Model;Cognitive Load Theory;Trust Equation')
    ap.add_argument('--psychology-strategy', required=True, help='semicolon-separated')
    ap.add_argument('--above-fold-requirement', required=True, help='semicolon-separated')
    ap.add_argument('--measurement-signals', required=True, help='semicolon-separated')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    data = build(args)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(args.out)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
