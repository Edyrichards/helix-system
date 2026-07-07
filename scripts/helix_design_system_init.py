#!/usr/bin/env python3
from pathlib import Path
import argparse, sys, textwrap
def main():
    ap=argparse.ArgumentParser(description='Initialize Helix design-system artifacts')
    ap.add_argument('repo', nargs='?', default='.')
    ap.add_argument('--force', action='store_true')
    args=ap.parse_args()
    root=Path(args.repo).expanduser().resolve()
    if not root.exists(): sys.exit(f'No such repo: {root}')
    design=root/'DESIGN.md'
    design_content = '''---
version: alpha
name: Project Design System
description: Helix-generated starter. Replace assumptions with project truth.
colors:
  background: '#F8FAFC'
  surface: '#FFFFFF'
  elevated: '#FFFFFF'
  border: '#D9E1EA'
  text: '#162033'
  muted: '#637083'
  accent: '#2563EB'
  destructive: '#B42318'
  success: '#087443'
  warning: '#B54708'
  info: '#175CD3'
  chart1: '#2563EB'
  chart2: '#087443'
  chart3: '#B54708'
  chart4: '#7C3AED'
  chart5: '#0E7490'
  chartPositive: '#087443'
  chartNegative: '#B42318'
  chartNeutral: '#637083'
  chartGrid: '#D9E1EA'
typography:
  display:
    fontFamily: System UI
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: '-0.03em'
  body-md:
    fontFamily: System UI
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.55
  data:
    fontFamily: ui-monospace
    fontSize: 0.875rem
    fontWeight: 500
    lineHeight: 1.4
rounded:
  sm: 6px
  md: 10px
  lg: 16px
  xl: 24px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
components:
  button-primary:
    backgroundColor: '{colors.accent}'
    textColor: '#FFFFFF'
    rounded: '{rounded.md}'
    padding: 12px
  chart-card:
    backgroundColor: '{colors.surface}'
    textColor: '{colors.text}'
    rounded: '{rounded.lg}'
    padding: 16px
---

## Overview

This DESIGN.md is the source of truth for Helix UI work in this repo. Replace assumptions with project-specific brand decisions before broad implementation.

## Colors

Use semantic roles rather than raw colors. Accent is reserved for primary actions, links, and essential data highlights.

## Typography

Use display for major page titles, body-md for normal prose, and data for numbers, tables, and charts.

## Layout

Mobile-first. Use the spacing scale consistently. Prefer system components and tokens over one-off values.

## Elevation & Depth

Prefer borders and whitespace. Use shadows sparingly and consistently.

## Shapes

Use one radius system. Cards use lg, controls use md, small badges use sm.

## Components

Buttons, forms, cards, tables, empty states, alerts, modals, and chart cards must use these tokens.

## Charts

Charts inherit design-system tokens. Use chartPositive/chartNegative for semantic values; chart1-chart5 for categorical series. Tooltip, legend, axes, and gridlines should match panel, text, border, and muted tokens.

## Do's and Don'ts

- Do inspect and extend this file before adding new visual patterns.
- Do map shadcn/Radix, Motion, Material, and chart libraries to these tokens.
- Do not introduce random hex colors in components.
- Do not ship default chart palettes.
- Do not use chart color as the only meaning carrier.
'''
    if design.exists() and not args.force:
        print(f'{design} exists; leaving it unchanged. Use --force to overwrite.')
    else:
        design.write_text(design_content, encoding='utf-8')
        print(f'Wrote {design}')
    claude=root/'CLAUDE.md'
    section='''

## Design-system enforcement
- Treat `DESIGN.md` and token files as the source of truth for UI.
- Before changing UI, inspect the design system and map new UI to existing tokens/components.
- Add missing tokens/components to the design system before using them.
- shadcn/Radix, Material, Motion, and chart libraries must be adapted to project tokens, not shipped with defaults.
- Charts must use design-system chart roles for categorical, positive, negative, neutral, grid, axis, and tooltip colors.
'''
    if claude.exists():
        txt=claude.read_text(encoding='utf-8')
        if '## Design-system enforcement' not in txt:
            claude.write_text(txt.rstrip()+section, encoding='utf-8')
            print(f'Updated {claude}')
        else: print(f'{claude} already has design-system enforcement')
    else:
        claude.write_text('# CLAUDE.md\n'+section, encoding='utf-8')
        print(f'Wrote {claude}')
if __name__=='__main__': main()
