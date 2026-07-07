#!/usr/bin/env python3
"""
Helix Live Design Analyzer
Uses Playwright (browser) to visit real sites (e.g. Mobbin examples, competitor onboarding flows),
capture screenshots of key commitment screens, and produce structured critique
against UX Psychology Principles + Helix Design Rubric.

Example:
  python scripts/helix_live_design_analyzer.py \
    --urls "https://example.com/onboarding" "https://app.example.com/signup" \
    --flow "onboarding" \
    --out-dir research/live-onboarding
"""
from __future__ import annotations
import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict

try:
    from playwright.sync_api import sync_playwright, Page
    HAS_PLAYWRIGHT = True
except ImportError:
    HAS_PLAYWRIGHT = False

AGENT_ROOT = Path(__file__).resolve().parents[1]

PSYCH_PRINCIPLES = [
    "smart_defaults",
    "goal_gradient",
    "reciprocity",
    "endowment_ikea",
    "loss_aversion",
    "anchoring_contrast"
]

def analyze_page(page: Page, url: str, flow_type: str = "onboarding") -> Dict:
    """Visit page, take screenshots, extract signals, basic heuristic critique."""
    print(f"Analyzing: {url}")
    page.goto(url, wait_until="networkidle", timeout=30000)
    
    desktop_path = f"live_{datetime.now().strftime('%Y%m%d-%H%M%S')}_desktop.png"
    mobile_path = f"live_{datetime.now().strftime('%Y%m%d-%H%M%S')}_mobile.png"
    
    # Desktop
    page.set_viewport_size({"width": 1280, "height": 800})
    page.screenshot(path=desktop_path, full_page=True)
    
    # Mobile
    page.set_viewport_size({"width": 390, "height": 844})
    page.screenshot(path=mobile_path, full_page=True)
    
    # Basic signals (in real version this would be LLM + vision or more JS)
    content = page.content().lower()
    
    signals = {
        "has_signup_wall_before_value": any(x in content for x in ["create account", "sign up to", "enter email to see"]),
        "shows_partial_value": any(x in content for x in ["score", "report", "top issues", "preview"]),
        "shows_progress": "%" in content or "step" in content or "complete" in content,
        "lets_customize_before_ask": any(x in content for x in ["choose", "select", "palette", "name your", "set your goal"]),
        "frames_as_loss": any(x in content for x in ["lose", "stop", "risk", "expire", "miss out"]),
        "has_anchor": any(x in content for x in ["$", "was", "now", "%"]),
    }
    
    # Score against psychology (heuristic 0-5)
    psych_score = sum([
        1 if not signals["has_signup_wall_before_value"] else 0,
        1 if signals["shows_partial_value"] else 0,
        1 if signals["shows_progress"] else 0,
        1 if signals["lets_customize_before_ask"] else 0,
        1 if signals["frames_as_loss"] else 0,
        1 if signals["has_anchor"] else 0,
    ])
    
    return {
        "url": url,
        "flow_type": flow_type,
        "desktop_screenshot": str(desktop_path),
        "mobile_screenshot": str(mobile_path),
        "signals": signals,
        "psychology_score": psych_score,
        "psychology_notes": "Heuristic scoring. Load ux-psychology-principles.md for full critique.",
        "recommendations": []
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", nargs="+", required=True, help="Live URLs to analyze")
    parser.add_argument("--flow", default="onboarding", choices=["onboarding", "upgrade", "checkout", "signup"])
    parser.add_argument("--out-dir", default="research/live-flows")
    args = parser.parse_args()
    
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    if not HAS_PLAYWRIGHT:
        print("Playwright not installed. Run: python -m playwright install chromium")
        return
    
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        for url in args.urls:
            try:
                res = analyze_page(page, url, args.flow)
                results.append(res)
            except Exception as e:
                print(f"Failed {url}: {e}")
        
        browser.close()
    
    manifest = {
        "timestamp": datetime.now().isoformat(),
        "flow": args.flow,
        "results": results,
        "principles_reference": "references/ux-psychology-principles.md",
        "rubric_note": "See updated design-rubric-v2.md for psychology + commitment dimensions"
    }
    
    (out_dir / "live_analysis.json").write_text(json.dumps(manifest, indent=2))
    print(f"\nAnalysis saved to {out_dir}/live_analysis.json")
    print("Screenshots captured for desktop + mobile.")
    print("Next: load ux-psychology-principles.md and critique the captured flows.")

if __name__ == "__main__":
    main()
