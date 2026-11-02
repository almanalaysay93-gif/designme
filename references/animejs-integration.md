# Anime.js integration and animated-word research

Anime.js is a first-class animation engine, especially for landing pages. It animates text, DOM elements, SVG, and JavaScript object properties; it is not a video renderer.

## Sources and installation

- Official repository: https://github.com/juliangarnier/anime (MIT).
- Current API documentation: https://animejs.com/documentation/
- Animated typography reference gallery: https://tobiasahlin.com/moving-letters/

The gallery contains older Anime.js examples: use it for visual inspiration and rewrite against the selected v4 API. Do not paste v3 syntax into v4 projects. Verify the installed version's documentation for text splitting, scopes, timeline seeking and scroll APIs before using them; use local accessible span splitting when necessary.

During every Designme installation, run `bash scripts/install-animejs.sh` from the skill directory to download the official repository into `~/.agents/tools/animejs` (override with `DESIGNME_ANIMEJS_REPO_DIR`). The helper verifies and reuses an existing official checkout without pulling, resetting or overwriting it; mismatched destinations or download failures block install completion. Record the checkout path and `git rev-parse HEAD` in `motion-skills-installed.md`. Both the research agent and Anime.js specialist should consult this local source.

Separately, install `animejs@4` in the target build with its existing package manager, only when animation is selected; commit its lockfile to pin the resolved version. This skill repository is instruction-only and needs no root npm dependency. Anime.js is a library, not an invented external skill package. Use local bundled assets for offline rendering.

## Coordinator routing

1. During briefing, classify the deliverable and record `brief.json.animation` with `engine` (`animejs`, `gsap`, `mixed`, or `none`), `reason`, `textResearch`, and `reducedMotion`. Default landing pages with motion to Anime.js; honor an explicit stack choice or static requirement. For other builds, prefer Anime.js for word/line reveals, staggered elements, SVG accents and lightweight UI motion; retain GSAP when its specialized controls are needed.
2. In Wave 1, `prompt-reference-agent` acts as the animation research agent. It produces `word-animation-references.md` before Wave 2 design decisions. `browser-agent` can capture motion samples at meaningful timestamps.
3. Wave 2's `motion-design-agent` consumes that research and chooses a coherent text-motion language. The coordinator writes `animation-plan.json` before Wave 3, assigning each component/selector and property set to exactly one engine, with reference IDs, trigger, duration/delay in milliseconds, easing, replay, final state and reduced-motion behavior. For mixed builds, split by component or property; never let both engines write the same property on the same element, including transform shorthands and their axes.
4. `animejs-agent` implements only its assigned targets in Wave 3 after design and ownership freeze. `gsap-agent` owns only its assigned targets. Skip either implementation role if it owns nothing. Record skips and reasons in `orchestrator.json`.
5. The coordinator integrates dependencies and entry points; craft review and QA consume research, plan and actual browser evidence. Landing pages ship as web builds; the one-final-owner rule applies per video deliverable, with assigned intermediate asset renders permitted under production-plan.json.

## Research contract

For landing pages and builds with animated words, research 3–5 relevant public examples using the brief's audience, claim, typography, tone, and desired pacing. Include at least one official Anime.js example/docs source and brand-relevant live examples when accessible. Do not apply an arbitrary text effect to every heading.

Write `word-animation-references.md` with stable IDs, exact source URLs, title/creator where available, observed word/line/character behavior, trigger, approximate timing/easing (label estimates), readability and mobile/reduced-motion concerns, and the proposed location/copy in this build. Shortlist 1–2 treatments and explain fit and rejected alternatives. Distinguish live-observed motion from docs-only evidence or inference. If browsing is unavailable, record the limitation and provide a provisional docs-based treatment; never claim to have inspected animation you could not see.

Research patterns such as clipped word reveals, line masks, staggered keywords, restrained type changes, and SVG/text pairings. Adapt them to the approved brand tokens. Credit inspiration; do not copy proprietary assets or a whole site's visual identity. Follow the existing free/local-only policy.

## Acceptance

Verify desktop and mobile, font-loaded line wraps, first paint/no-JS readability, semantic reading without duplicate text, keyboard/CTA access, reduced-motion changes, replay and unmount cleanup. Record actual evidence in `animejs-validation.md` and `audit.md`. Video use additionally requires repeatable forward/backward seeks from the canonical clock, with seconds converted to milliseconds, and the existing final-render checks.
