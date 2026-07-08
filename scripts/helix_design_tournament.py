#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import tempfile
import threading
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from playwright.sync_api import sync_playwright, Error as PlaywrightError
    HAS_PLAYWRIGHT = True
except Exception:
    HAS_PLAYWRIGHT = False
    sync_playwright = None  # type: ignore
    PlaywrightError = Exception  # type: ignore

HOME = Path.home()
AGENT = HOME / ".hermes/agents/helix-system"
DEFAULT_OUT = AGENT / "evals" / "design-tournaments"

RUBRIC = {
    "design_dna": ["token", "typography", "palette", "spacing", "radius", "motion", "brand"],
    "visual_proof": ["screenshot", "desktop", "mobile", "preview", "render", "figma", "storybook"],
    "interaction_states": ["loading", "empty", "error", "success", "hover", "active", "focus"],
    "agentic_loop": ["variant", "critique", "repair", "score", "evidence", "handoff"],
    "anti_slop": ["wcag", "contrast", "responsive", "no ai", "accessible", "component"],
}


def text_from_variant(variant: dict[str, Any]) -> str:
    return " ".join(
        str(variant.get(k, "")) for k in ("name", "description", "html", "notes", "tokens", "interactions")
    ).lower()


def score_variant(variant: dict[str, Any]) -> dict[str, Any]:
    text = text_from_variant(variant)
    breakdown: dict[str, int] = {}
    total = 0
    for category, terms in RUBRIC.items():
        hits = sum(1 for term in terms if term in text)
        pts = min(10, hits * 2)
        breakdown[category] = pts
        total += pts

    html_text = str(variant.get("html", ""))
    total += min(12, len(re.findall(r"<section|<article|<main|<nav|<button", html_text, flags=re.I)) * 2)
    total += min(8, len(html_text) // 350)

    # Visual evidence bonuses (populated by browser render)
    ev = variant.get("visual_evidence") or {}
    if ev.get("desktop_screenshot"):
        total += 12
        breakdown["visual_proof"] = min(20, breakdown.get("visual_proof", 0) + 8)
    if ev.get("mobile_screenshot"):
        total += 10
        breakdown["visual_proof"] = min(20, breakdown.get("visual_proof", 0) + 6)
    if ev.get("visual_verified"):
        total += 4
    if ev.get("has_horizontal_overflow") is False:
        total += 8
        breakdown["anti_slop"] = min(14, breakdown.get("anti_slop", 0) + 4)
    if ev.get("console_errors") == []:
        total += 8
        breakdown["anti_slop"] = min(14, breakdown.get("anti_slop", 0) + 4)

    return {**variant, "score": total, "breakdown": breakdown}


def score_variants(variants: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted((score_variant(v) for v in variants), key=lambda v: v["score"], reverse=True)


def slug(name: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return value or "variant"


def _make_standalone_html(raw_html: str, title: str = "Helix Variant") -> str:
    """Wrap raw HTML fragment into a full, self-contained document for reliable rendering."""
    safe = raw_html or "<main><p>No content</p></main>"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <style>
    :root {{ color-scheme: light dark; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.5; }}
    main, section, article, nav, header, footer {{ display: block; }}
    img {{ max-width: 100%; height: auto; }}
    button {{ cursor: pointer; }}
  </style>
</head>
<body>
{safe}
</body>
</html>"""


def _render_with_playwright(html_path: Path, out_dir: Path, base_slug: str) -> dict[str, Any]:
    """Render desktop + mobile screenshots, capture console + overflow. Returns evidence dict."""
    evidence: dict[str, Any] = {
        "visual_verified": False,
        "desktop_screenshot": None,
        "mobile_screenshot": None,
        "console_errors": [],
        "has_horizontal_overflow": None,
    }
    if not HAS_PLAYWRIGHT:
        return evidence

    desktop_png = out_dir / f"{base_slug}-desktop.png"
    mobile_png = out_dir / f"{base_slug}-mobile.png"

    console_errors: list[str] = []

    def on_console(msg):
        if msg.type in ("error", "warning"):
            console_errors.append(f"{msg.type}: {msg.text}")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            # Desktop
            page = browser.new_page()
            page.set_viewport_size({"width": 1280, "height": 800})
            page.on("console", on_console)
            page.goto(f"file://{html_path.resolve()}", wait_until="networkidle", timeout=8000)
            page.wait_for_timeout(250)
            page.screenshot(path=str(desktop_png), full_page=True)
            try:
                overflow = page.evaluate(
                    "() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 4"
                )
            except Exception:
                overflow = None
            evidence["desktop_screenshot"] = str(desktop_png.relative_to(out_dir))
            evidence["has_horizontal_overflow"] = bool(overflow) if overflow is not None else None

            # Mobile
            page.set_viewport_size({"width": 390, "height": 844})
            page.goto(f"file://{html_path.resolve()}", wait_until="networkidle", timeout=8000)
            page.wait_for_timeout(200)
            page.screenshot(path=str(mobile_png), full_page=True)
            evidence["mobile_screenshot"] = str(mobile_png.relative_to(out_dir))

            browser.close()
        evidence["console_errors"] = console_errors[:8]  # cap
        evidence["visual_verified"] = bool(desktop_png.exists() and mobile_png.exists())
    except PlaywrightError as e:
        evidence["console_errors"].append(f"playwright_error: {str(e)[:120]}")
    except Exception as e:
        evidence["console_errors"].append(f"render_error: {str(e)[:120]}")

    return evidence


def _render_with_node_playwright(html_path: Path, out_dir: Path, base_slug: str) -> dict[str, Any]:
    """Render screenshots with Node Playwright when Python Playwright is unavailable.

    This is the portable fallback for Next/Vite/Tailwind projects that already have
    Playwright in node_modules. The script is written inside out_dir so Node's
    normal module resolution can walk up into the target project's node_modules.
    """
    evidence: dict[str, Any] = {
        "visual_verified": False,
        "desktop_screenshot": None,
        "mobile_screenshot": None,
        "console_errors": [],
        "has_horizontal_overflow": None,
        "renderer": "node-playwright",
    }
    script_path = out_dir / f"{base_slug}-render.mjs"
    desktop_png = out_dir / f"{base_slug}-desktop.png"
    mobile_png = out_dir / f"{base_slug}-mobile.png"
    script = f"""
import {{ chromium }} from 'playwright';
const htmlPath = {json.dumps(str(html_path.resolve()))};
const desktopPng = {json.dumps(str(desktop_png.resolve()))};
const mobilePng = {json.dumps(str(mobile_png.resolve()))};
const evidence = {{
  visual_verified: false,
  desktop_screenshot: {json.dumps(desktop_png.name)},
  mobile_screenshot: {json.dumps(mobile_png.name)},
  console_errors: [],
  has_horizontal_overflow: null,
  renderer: 'node-playwright'
}};
const browser = await chromium.launch({{ headless: true }});
try {{
  for (const [label, viewport, png] of [
    ['desktop', {{ width: 1280, height: 800 }}, desktopPng],
    ['mobile', {{ width: 390, height: 844 }}, mobilePng]
  ]) {{
    const page = await browser.newPage({{ viewport }});
    page.on('console', msg => {{
      if (['error', 'warning'].includes(msg.type())) evidence.console_errors.push(`${{label}} ${{msg.type()}}: ${{msg.text()}}`);
    }});
    await page.goto('file://' + htmlPath, {{ waitUntil: 'networkidle', timeout: 8000 }});
    await page.waitForTimeout(250);
    await page.screenshot({{ path: png, fullPage: true }});
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 4);
    if (label === 'desktop') evidence.has_horizontal_overflow = overflow;
    if (label === 'mobile' && overflow) evidence.has_horizontal_overflow = true;
    await page.close();
  }}
  evidence.visual_verified = true;
}} finally {{
  await browser.close();
}}
console.log(JSON.stringify(evidence));
"""
    try:
        script_path.write_text(script, encoding="utf-8")
        result = subprocess.run(
            ["node", str(script_path)],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(out_dir),
        )
        if result.returncode != 0:
            msg = (result.stderr or result.stdout or "node playwright failed").strip()
            evidence["console_errors"].append(f"node_playwright_error: {msg[:200]}")
            return evidence
        payload = json.loads(result.stdout.strip().splitlines()[-1])
        evidence.update(payload)
        evidence["visual_verified"] = bool((out_dir / str(evidence.get("desktop_screenshot"))).exists() and (out_dir / str(evidence.get("mobile_screenshot"))).exists())
    except FileNotFoundError:
        evidence["console_errors"].append("node_playwright_error: node executable not found")
    except Exception as exc:
        evidence["console_errors"].append(f"node_playwright_error: {str(exc)[:200]}")
    return evidence

def contact_sheet_html(scored: list[dict[str, Any]], brief: str, visual_mode: str) -> str:
    cards = []
    for idx, variant in enumerate(scored, 1):
        name = html.escape(str(variant.get("name", "variant")))
        body = variant.get("html") or f"<pre>{html.escape(json.dumps(variant, indent=2))}</pre>"

        ev = variant.get("visual_evidence") or {}
        shots = ""
        if ev.get("desktop_screenshot") or ev.get("mobile_screenshot"):
            d = ev.get("desktop_screenshot")
            m = ev.get("mobile_screenshot")
            shots = '<div class="shots">'
            if d:
                shots += f'<div><small>Desktop</small><br><img src="{html.escape(d)}" alt="desktop"></div>'
            if m:
                shots += f'<div><small>Mobile</small><br><img src="{html.escape(m)}" alt="mobile"></div>'
            shots += "</div>"

        errors = ev.get("console_errors") or []
        err_html = ""
        if errors:
            err_html = "<details><summary>Console (" + str(len(errors)) + ")</summary><pre>" + html.escape("\n".join(errors)) + "</pre></details>"
        overflow = "overflow" if ev.get("has_horizontal_overflow") else ("clean" if ev.get("has_horizontal_overflow") is False else "n/a")

        cards.append(f"""
        <article class="card">
          <header>
            <span>#{idx}</span>
            <strong>{name}</strong>
            <b>{variant['score']} pts</b>
          </header>
          <div class="frame">{body}</div>
          {shots}
          <div class="meta">
            <span>overflow: {overflow}</span>
            {err_html}
          </div>
          <pre>{html.escape(json.dumps(variant.get('breakdown', {}), indent=2))}</pre>
        </article>
        """)

    style = """
:root { color-scheme: dark; --bg:#09090b; --panel:#15151a; --line:#2a2a32; --text:#f4f4f5; --muted:#a1a1aa; --accent:#7dd3fc; }
* { box-sizing: border-box; }
body { margin:0; font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, sans-serif; background:var(--bg); color:var(--text); }
main { max-width: 1600px; margin: 0 auto; padding: 32px; }
.grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(420px, 1fr)); gap: 20px; }
.card { border:1px solid var(--line); background:var(--panel); border-radius:20px; overflow:hidden; }
.card > header { display:flex; justify-content:space-between; gap:16px; padding:14px 16px; border-bottom:1px solid var(--line); color:var(--muted); }
.card strong { color:var(--text); }
.card b { color:var(--accent); }
.frame { min-height:220px; background:white; color:#111; padding:18px; overflow:auto; border-bottom:1px solid var(--line); }
.shots { display:flex; gap:12px; padding:12px; background:#0f0f12; }
.shots img { max-width:100%; border:1px solid var(--line); border-radius:8px; }
.meta { padding:8px 16px; font-size:12px; color:var(--muted); display:flex; gap:16px; align-items:center; }
pre { white-space:pre-wrap; color:var(--muted); padding:14px 16px; margin:0; border-top:1px solid var(--line); font-size:12px; }
.hero { margin-bottom: 24px; }
.hero p { color: var(--muted); max-width: 80ch; }
"""

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Helix Design Tournament</title>
<style>{style}</style>
</head>
<body>
<main>
<section class="hero"><h1>Helix Design Tournament</h1><p>{html.escape(brief)}</p><p><small>visual mode: {visual_mode}</small></p></section>
<section class="grid">{''.join(cards)}</section>
</main>
</body>
</html>"""


def write_tournament(out_root: Path, brief: str, variants: list[dict[str, Any]], use_browser: bool = True) -> Path:
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    out = out_root / ts
    out.mkdir(parents=True, exist_ok=True)

    visual_mode = "heuristic"
    processed: list[dict[str, Any]] = []
    browser_modes: set[str] = set()

    for idx, variant in enumerate(variants, 1):
        v = dict(variant)  # copy
        name = str(v.get("name", f"variant-{idx}"))
        s = slug(name)
        raw_html = str(v.get("html", ""))

        standalone = _make_standalone_html(raw_html, name)
        html_path = out / f"{idx:02d}-{s}.html"
        html_path.write_text(standalone, encoding="utf-8")

        ev: dict[str, Any] = {}
        if use_browser:
            if HAS_PLAYWRIGHT:
                ev = _render_with_playwright(html_path, out, f"{idx:02d}-{s}")
                if ev.get("visual_verified"):
                    browser_modes.add("python-playwright")
            else:
                ev = _render_with_node_playwright(html_path, out, f"{idx:02d}-{s}")
                if ev.get("visual_verified"):
                    browser_modes.add("node-playwright")

        v["visual_evidence"] = ev
        v["html_file"] = str(html_path.relative_to(out))
        processed.append(v)

    if browser_modes:
        visual_mode = "browser-" + "+".join(sorted(browser_modes))

    scored = score_variants(processed)
    manifest = {
        "brief": brief,
        "visual_mode": visual_mode,
        "winner": scored[0] if scored else None,
        "variants": scored,
        "generated_at": datetime.now().isoformat(),
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (out / "contact-sheet.html").write_text(contact_sheet_html(scored, brief, visual_mode), encoding="utf-8")
    return out


def variants_from_json(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and "variants" in data:
        return list(data["variants"])
    if not isinstance(data, list):
        raise ValueError("variant JSON must be a list or object with variants")
    return data


def main() -> None:
    ap = argparse.ArgumentParser(description="Score a Helix UI variant tournament with optional real browser screenshots.")
    ap.add_argument("--brief", required=True)
    ap.add_argument("--variants-json", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--no-browser", action="store_true", help="Force heuristic-only scoring (no Playwright)")
    args = ap.parse_args()

    use_browser = not args.no_browser
    out = write_tournament(args.out_dir, args.brief, variants_from_json(args.variants_json), use_browser=use_browser)
    print(out)


if __name__ == "__main__":
    main()
