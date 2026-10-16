# UI/UX Pro Max Integration

Source: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

The source is MIT-licensed and provides local, searchable design intelligence. The current catalog includes 79 searchable UI styles, 192 product palettes, 74 font pairings, 119 UX guidelines, 25 chart types, icon guidance, GSAP presets, and 22 technology-stack profiles. The data and Python search engine run locally with the Python standard library.

## Use in designme

`ui-ux-pro-max-agent` is an optional 23rd agent. Recommend it during grilling for any UI-containing work: landing pages, dashboards, product demos, interactive web visuals, mobile app UI, forms, navigation, charts, or accessibility/UX reviews.

It complements the other designme agents:

- `design-dna-agent` extracts the visual tokens from references.
- `visual-style-agent` selects the broader motion/visual language.
- `ui-ux-pro-max-agent` resolves interface style, palette, typography, UX rules, stack behavior, and accessibility.
- `browser-agent` verifies the UI at real viewport sizes.
- `qa-anti-slop-agent` checks the final evidence.

Skip it for a pure non-UI film with no interface or interaction proof.

## Local installation

The official repository documents this free/open-source install:

```bash
npm install -g ui-ux-pro-max-cli
uipro init --ai claude --global
```

For this designme workspace, a checked-out copy of `.claude/skills/ui-ux-pro-max` is also sufficient. The agent needs the local folder containing `SKILL.md`, `scripts/search.py`, and the bundled `data/` CSV files. No network call is required for a search.

## Search domains

Use explicit domains instead of guessing:

- `product` — product-type patterns and recommendations
- `style` — UI style systems and CSS direction
- `color` — product-specific palettes
- `typography` — font pairings and imports
- `ux` — accessibility, interaction, forms, navigation, and responsive guidance
- `icons` — consistent icon families and import guidance
- `chart` — chart types and data-display patterns
- `landing` — landing-page structure
- `gsap` — interaction and motion presets
- `react` — React/Next performance patterns
- `web` — app-interface and platform guidance

Use `--stack` for implementation guidance, such as `html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `astro`, `shadcn`, `threejs`, `swiftui`, `react-native`, or `flutter`.

## Design-system dials

When generating a design system, use the optional local dials deliberately:

```bash
python3 "$UIPRO_MAX/scripts/search.py" \
  "analytics dashboard calm" \
  --design-system --variance 6 --motion 5 --density 8 \
  --json -p "Project Name"
```

- `--variance` controls centered/minimal to bold/asymmetric direction.
- `--motion` controls subtle to complex choreography and returns matching GSAP guidance.
- `--density` controls spacious to dashboard-dense spacing tokens.

The agent must record the chosen values in `uiux-design-system.md`.

## Outputs

- `uiux-design-system.md` — resolved style, palette, type, spacing, component states, motion, and stack rules.
- `uiux-audit.md` — evidence from responsive, keyboard, focus, contrast, semantics, reduced-motion, and interaction checks.
- `uiux-search-results.json` — raw local search output when `--json` is used.

The output must include source queries and rejected alternatives so later agents can reproduce the decisions.

## Free-only boundary

The agent may use bundled data, local scripts, open-source icon/font metadata, user-provided assets, and deterministic code. It must not use premium design-system services, paid font/asset APIs, AI image generation, paid models, or hosted analytics. If a font is selected, prefer a bundled/open-licensed or already-installed font and record the license/source.
