#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def load_script(name: str):
    path = SCRIPTS / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec and spec.loader, f"cannot load {path}"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_design_research_ranks_repos_from_fixture():
    mod = load_script("helix_design_research.py")
    fixture = [
        {"fullName": "tiny/plain", "description": "notes", "stargazersCount": 5, "forksCount": 0, "license": {"spdxId": "MIT"}, "updatedAt": "2026-01-01T00:00:00Z", "url": "https://example.test/plain"},
        {"fullName": "abi/screenshot-to-code", "description": "Drop in a screenshot and convert it to clean React Tailwind code", "stargazersCount": 70000, "forksCount": 9000, "license": {"spdxId": "MIT"}, "updatedAt": "2026-07-07T00:00:00Z", "url": "https://github.com/abi/screenshot-to-code"},
        {"fullName": "figma/mcp", "description": "Figma MCP read write design system components", "stargazersCount": 1200, "forksCount": 100, "license": {"spdxId": "Apache-2.0"}, "updatedAt": "2026-07-07T00:00:00Z", "url": "https://github.com/example/figma-mcp"},
    ]
    ranked = mod.rank_repositories(fixture, limit=2)
    assert [r["fullName"] for r in ranked] == ["abi/screenshot-to-code", "figma/mcp"]
    report = mod.render_report(ranked, decision="Which repos help Helix design autonomy?")
    assert "Patterns" in report
    assert "Gaps" in report
    assert "Recommendation" in report
    assert "screenshot-to-code" in report


def test_design_tournament_scores_and_writes_contact_sheet_data():
    mod = load_script("helix_design_tournament.py")
    variants = [
        {"name": "Plain", "html": "<main><h1>Hello</h1><button>Go</button></main>"},
        {"name": "Strong", "html": "<main><section><h1>Design DNA</h1><p>Tokens, Figma, Storybook, screenshots, mobile, desktop, WCAG, loading, empty, error.</p><button>Preview</button></section></main>"},
    ]
    scored = mod.score_variants(variants)
    assert scored[0]["score"] > scored[1]["score"]

    with tempfile.TemporaryDirectory() as td:
        out = mod.write_tournament(Path(td), "brief text", variants, use_browser=False)
        assert (out / "manifest.json").exists()
        manifest = json.loads((out / "manifest.json").read_text())
        assert manifest["winner"]["name"] == "Strong"
        assert (out / "contact-sheet.html").exists()
        assert "Strong" in (out / "contact-sheet.html").read_text()
        assert manifest.get("visual_mode") == "heuristic"

        # Browser path (will use if available)
        out2 = mod.write_tournament(Path(td), "browser brief", variants, use_browser=True)
        m2 = json.loads((out2 / "manifest.json").read_text())
        winner = m2["winner"]
        assert "visual_evidence" in winner
        ev = winner.get("visual_evidence", {})
        if getattr(mod, "HAS_PLAYWRIGHT", False):
            assert ev.get("visual_verified") or ev.get("desktop_screenshot") is not None
        assert (out2 / "contact-sheet.html").exists()


def test_verify_install_requires_new_autonomy_artifacts():
    verifier = (SCRIPTS / "verify_install.py").read_text()
    assert "helix_design_research.py" in verifier
    assert "helix_design_tournament.py" in verifier
    assert "ui-design-autonomy-repo-patterns.md" in verifier


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_") and callable(v)]
    failures = []
    for test in tests:
        try:
            test()
            print(f"PASS {test.__name__}")
        except Exception as exc:
            failures.append((test.__name__, exc))
            print(f"FAIL {test.__name__}: {exc!r}")
    if failures:
        raise SystemExit(1)
