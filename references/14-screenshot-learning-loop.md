# Helix Screenshot Learning Loop

Purpose: make Helix learn from rendered pixels, not just prompt text.

## Core principle
No substantial UI claim is complete until rendered screenshots have been inspected and repaired. A screenshot is the design truth.

## Inputs
- generated variant screenshot(s): desktop and mobile minimum
- reference screenshot(s) or reference lessons when available
- behavior map
- product/design constraints
- automated probe data: viewport, overflow, console errors, CTA/input counts, fold position

## Critique dimensions
### Behavior
- What does the user understand in 5 seconds?
- Which anxiety is reduced?
- Is the desired belief change visible?
- Is the primary action obvious and low-risk?
- Does the screen create motivation, ability, and prompt at the right moment?

### Visual craft
- hierarchy: one dominant idea per fold
- spacing rhythm: no cramped or evenly templated sections
- typography: scale, line length, contrast, descender safety
- component quality: no fake dashboards or meaningless rectangles
- color/token fidelity: semantic use, no random accents
- mobile rhythm: deliberate collapse, no tiny labels or long dense blocks

### Trust and conversion
- Is risk reduction near the ask?
- Is proof concrete without fake testimonials or logos?
- Does CTA ask for the smallest meaningful commitment?
- Is pricing/data access explained before user worry grows?

### Accessibility/browser
- no horizontal overflow
- no console errors
- readable contrast
- labels/focus targets/touch size
- reduced motion when motion exists

## Repair protocol
Each visual critique must produce a patch plan:
1. top 3 issues blocking behavior/conversion
2. top 3 visual craft issues
3. exact component/section changes
4. expected score improvement
5. screenshots to recapture

Minimum for UI Pro work:
- render first pass
- critique screenshots
- repair winner
- render again
- only stop when score improves or the reason it cannot improve is documented

## Lesson promotion
Promote a lesson when a screenshot comparison shows a repeatable pattern:
- reference pattern worked
- generated pattern failed
- repair improved clarity/conversion/mobile rhythm
- anti-pattern recurred

Use `schemas/design-lesson.schema.json` and save project-local lessons under `design/helix-memory/`.
