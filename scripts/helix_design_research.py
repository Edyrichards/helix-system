#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

HOME = Path.home()
AGENT = HOME / ".hermes/agents/helix-system"
DEFAULT_OUT = AGENT / "research"

QUERIES = [
    '"screenshot to code" stars:>100',
    '"AI app builder" "Lovable" stars:>100',
    '"v0" "Lovable" "Bolt" stars:>100',
    '"Figma" "MCP" "Claude" stars:>100',
    '"design system" "AI" "Claude Code" stars:>10',
    '"website builder" "AI" "React" stars:>100',
    '"shadcn" "AI" "component" stars:>100',
    '"magic ui" stars:>100',
    '"infinite canvas" "React" stars:>1000',
]

KNOWN_REPOS = [
    "abi/screenshot-to-code",
    "wandb/openui",
    "dyad-sh/dyad",
    "stackblitz/bolt.new",
    "tldraw/tldraw",
    "grab/cursor-talk-to-figma-mcp",
    "vkhanhqui/figma-mcp-go",
    "TranHoaiHung/figma-ui-mcp",
    "natdexterra/work-with-design-systems",
    "senlindesign/claude2figma",
    "marvkr/better-design",
    "redongreen/uSpec",
    "gabelul/stitch-kit",
    "plugin87/ux-ui-agent-skills",
    "shadcn-ui/ui",
    "Jpisnice/shadcn-ui-mcp-server",
    "magicuidesign/mcp",
    "21st-dev/magic-mcp",
    "storybookjs/storybook",
    "microsoft/playwright-mcp",
    "browser-use/browser-use",
    "plasmicapp/plasmic",
    "BuilderIO/builder",
]

WEIGHTS = {
    "screenshot": 16,
    "convert": 8,
    "code": 5,
    "figma": 10,
    "mcp": 8,
    "design system": 8,
    "component": 6,
    "registry": 5,
    "storybook": 7,
    "playwright": 7,
    "browser": 5,
    "canvas": 7,
    "react": 4,
    "tailwind": 4,
    "agent": 5,
    "builder": 5,
    "prototype": 5,
    "preview": 5,
    "v0": 5,
    "lovable": 5,
    "bolt": 5,
}

LICENSE_PENALTY = {"NOASSERTION": -4, "NONE": -5, "GPL-3.0": -5, "AGPL-3.0": -8}


def normalize_repo(raw: dict[str, Any]) -> dict[str, Any]:
    repo = dict(raw)
    if "nameWithOwner" in repo and "fullName" not in repo:
        repo["fullName"] = repo["nameWithOwner"]
    if "stargazerCount" in repo and "stargazersCount" not in repo:
        repo["stargazersCount"] = repo["stargazerCount"]
    if "forkCount" in repo and "forksCount" not in repo:
        repo["forksCount"] = repo["forkCount"]
    lic = repo.get("license") or repo.get("licenseInfo") or {}
    if isinstance(lic, dict):
        repo["license_spdx"] = lic.get("spdxId") or lic.get("spdx_id") or lic.get("name") or "NOASSERTION"
    else:
        repo["license_spdx"] = lic or "NOASSERTION"
    return repo


def relevance_score(repo: dict[str, Any]) -> float:
    text = " ".join(str(repo.get(k, "")) for k in ("fullName", "description", "language")).lower()
    score = 0.0
    for term, weight in WEIGHTS.items():
        if term in text:
            score += weight
    stars = int(repo.get("stargazersCount") or 0)
    forks = int(repo.get("forksCount") or 0)
    score += min(math.log10(max(stars, 1)) * 4, 22)
    score += min(math.log10(max(forks, 1)) * 1.5, 6)
    lic = str(repo.get("license_spdx") or "NOASSERTION").upper()
    score += LICENSE_PENALTY.get(lic, 0)
    if any(word in text for word in ["awesome", "cookbook", "wallpaper", "system-prompts", "prompts-and-models", "leaked"]):
        score -= 35
    if "gnu general public license" in lic or "affero" in lic:
        score -= 12
    return round(score, 2)


def rank_repositories(repos: list[dict[str, Any]], limit: int = 25) -> list[dict[str, Any]]:
    seen: dict[str, dict[str, Any]] = {}
    for raw in repos:
        repo = normalize_repo(raw)
        name = repo.get("fullName")
        if not name:
            continue
        repo["helix_score"] = relevance_score(repo)
        seen[name] = repo
    ranked = sorted(seen.values(), key=lambda r: (r["helix_score"], int(r.get("stargazersCount") or 0)), reverse=True)
    return ranked[:limit]


def run_gh_json(args: list[str]) -> list[dict[str, Any]]:
    proc = subprocess.run(args, capture_output=True, text=True, timeout=90)
    if proc.returncode != 0:
        print(proc.stderr or proc.stdout, file=sys.stderr)
        return []
    return json.loads(proc.stdout or "[]")


def collect_from_github(limit_per_query: int = 20) -> list[dict[str, Any]]:
    repos: list[dict[str, Any]] = []
    fields = "fullName,description,stargazersCount,forksCount,updatedAt,license,language,url"
    for query in QUERIES:
        repos.extend(run_gh_json(["gh", "search", "repos", query, "--limit", str(limit_per_query), "--sort", "stars", "--json", fields]))
    for full in KNOWN_REPOS:
        proc = subprocess.run(
            ["gh", "repo", "view", full, "--json", "nameWithOwner,description,stargazerCount,forkCount,updatedAt,licenseInfo,primaryLanguage,url"],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if proc.returncode == 0:
            data = json.loads(proc.stdout)
            data["language"] = (data.get("primaryLanguage") or {}).get("name")
            repos.append(data)
    return repos


def source_row(repo: dict[str, Any]) -> str:
    name = repo.get("fullName", "unknown")
    url = repo.get("url") or f"https://github.com/{name}"
    stars = repo.get("stargazersCount") or repo.get("stargazerCount") or 0
    license_spdx = repo.get("license_spdx", "NOASSERTION")
    desc = (repo.get("description") or "").replace("|", "\\|")
    score = repo.get("helix_score", "")
    return f"| [{name}]({url}) | {stars} | {license_spdx} | {score} | {desc} |"


def render_report(ranked: list[dict[str, Any]], decision: str) -> str:
    rows = "\n".join(source_row(r) for r in ranked)
    top_names = ", ".join(r.get("fullName", "") for r in ranked[:6])
    return f"""# Helix UI Autonomy GitHub Research

Decision question: {decision}

Generated: {datetime.now().isoformat(timespec='seconds')}

## Findings

| Repo | Stars | License | Helix score | Why it matters |
|---|---:|---|---:|---|
{rows}

## Patterns

- High-value design agents combine **generation**, **preview**, **visual verification**, and **repair**, not just prompt-to-code.
- The strongest UI autonomy signals are screenshot/Figma intake, MCP-based Figma read/write, component registry retrieval, Storybook/Playwright verification, and canvas workspaces.
- Component systems need enforcement: tokens, variants, accessibility states, and component anatomy must be checked mechanically.

## Gaps

- Most repos cover only one lane: generator, Figma bridge, component registry, or visual test harness.
- Few systems run multi-variant design tournaments with screenshot-backed scoring and automated repair.
- Few systems preserve parity between Figma, repo tokens, component docs, Storybook states, and rendered screenshots.

## Recommendation

Study `{top_names}` first, then evolve Helix into a design operating loop: intake real visual/context sources, extract design DNA, generate multiple variants, render them, screenshot them, score them against Helix's rubric, repair the winner, and hand off with evidence.
"""


def main() -> None:
    ap = argparse.ArgumentParser(description="Search/rank GitHub repos that can improve Helix UI design autonomy.")
    ap.add_argument("--from-json", type=Path, help="Use an existing JSON array instead of calling gh.")
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--decision", default="Which repositories should Helix study to scale autonomous UI/UX generation?")
    args = ap.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    repos = json.loads(args.from_json.read_text()) if args.from_json else collect_from_github()
    ranked = rank_repositories(repos, limit=args.limit)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    json_path = args.out_dir / f"helix-ui-repos-ranked-{ts}.json"
    report_path = args.out_dir / f"helix-ui-repos-ranked-{ts}.md"
    json_path.write_text(json.dumps(ranked, indent=2), encoding="utf-8")
    report_path.write_text(render_report(ranked, args.decision), encoding="utf-8")
    print(report_path)


if __name__ == "__main__":
    main()
