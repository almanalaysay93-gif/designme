# Designme

Free-only **31-agent design and motion studio** for websites, 3D parallax backgrounds and locally rendered video. Invoke `/designme` to turn a brief and real references into a deliberate visual system, editable motion, verified output and a versioned `/buildme` handoff.

This repository contains orchestration instructions, agent contracts, references and installation/validation helpers. It does not ship a prebuilt website or a promise that any particular host has passed runtime checks. [SKILL.md](SKILL.md) defines dispatch and acceptance; [manifest.json](manifest.json) records roles, providers, core wave order and gates.

## Start

```text
/designme a product landing page with restrained 3D parallax, layered reference-image depth, readable demo CTA and mobile reduced-motion fallback
```

Other briefs can request launch films, explainers, interactive figures, product breakdowns or standalone renderer projects. Website work keeps the live site as its primary deliverable; video is added when requested. The approved brief determines scope, references, optional choices and constraints.

## Four-wave production loop

| Wave | Core agents, in order | Required handoff |
| --- | --- | --- |
| 1 | planner-griller | Approved goal, thesis, references, constraints and optional decisions |
| 1.5 | speckit-theme-builder → speckit-theme-reviewer | Five locked theme/design files, exact read-only review, max two attempts then user decision |
| 2 | design-dna → motion-design | Tokens, visual language, researched motion and frozen dependency/ownership plans |
| 3 | gsap, threejs, hyperframes, motion-a11y | Integrated site/film draft, complete reduced variants and accessibility evidence |
| 4 | genjutsu thesis → render-perf-budget → qa-anti-slop → token-handoff-exporter | Refined thesis, passing performance/accessibility and final QA, then complete versioned export |

All existing specialists retain supporting tasks under those waves. Research precedes dependent design extraction; canonical timing and models/assets precede scene/clip assembly. Core roles must produce their required output or a concrete BLOCKED result, subject only to the explicit owns-nothing/web-only exceptions in SKILL.md. Existing optional approvals remain in force; already-authorized choices do not need repeated permission. See [workflow](references/workflow.md) and [state contract](references/orchestrator-state.md).

The final exporter runs **last, only after QA PASS for the exact tested revision**. Source changes invalidate affected gate evidence. Repairs go to the actual owner and rerun affected producer/consumer checks inside the existing three-loop cap; unresolved defects are never waived into PASS.

## Website and motion capabilities

| Capability | How it participates |
| --- | --- |
| Anime.js and GSAP | Anime.js defaults to landing-page text/elements; GSAP handles assigned specialist timelines. Each target/property has one owner. Animated-word research selects treatments that fit actual copy and brand. |
| Three.js and multilayer parallax | A dedicated background specialist chooses live 3D, procedural layers, honest image-based 2.5D or useful media layers from the website goal, reference image and device budget. One scene/camera/clock and scroll-progress owner prevents conflicts. |
| Open 3D Skills | All eight skills are available and assessed for enabled work; each records use/skip/blocked and real execution evidence. Scenes, exploded views, scroll film, alpha media, cursor rigs, asset planning, site-check and capture compose when useful. |
| HyperFrames | Default final-film assembler, consuming verified local layers and supporting clips. |
| Remotion and motionmaxxing | Normal specialists: Remotion produces useful React sequences/clips; motionmaxxing plans depth/camera/pacing and reviews the integrated result. Explicit standalone final output remains supported. |
| html-video | Verified `nexu-io/html-video` templates/local asset provider. Inspect installed engines and output timing/alpha; real-time capture is not assumed frame-exact. No paid audio/model generation or competing studio-agent loop. |
| Reference images and img2threejs | Inspect actual pixels before claiming fidelity. Use images as style references or layered artwork; approved useful objects/characters can become deterministic model factories with staged reconstruction evidence. Hidden-angle approximations stay explicit. |
| Visual style and UI/UX | Choose one primary style from the 20-style library, with at most one supporting style. Local UI/UX Pro Max and the mandatory 14-law audit support interface work under the current briefing rules. |
| Hairline and prompt catalogs | Approved interactive figures and Opus code-video prompt research remain available without changing the selected final owner. |

One final owner per deliverable permits multiple assigned intermediate assets. Captures of a website wait for a ready integrated page; their consuming film waits for verified footage. Media/frame/alpha/color/audio contracts live in `production-plan.json`. See [normal production](references/normal-motion-orchestration.md), [backgrounds](references/parallax-background-integration.md), [Open 3D](references/open-3d-integration.md), [Anime.js](references/animejs-integration.md) and [html-video](references/html-video-integration.md).

## Evidence and release gates

- **Motion accessibility:** every animation has a reduced variant. Reduced mode has no parallax/infinite loop or autoplay longer than 5 seconds. Temporal contrast, flashing, keyboard/focus/modal behavior, live regions and decorative semantics have PASS/FAIL evidence in `motion-a11y.md`; `gsap-timeline-reduced.js` supplies the approved reduced interface.
- **Render/performance:** `perf-budget.json` and `perf-report.md` document CSR/SSR, real poster/static first paint, JS/GLB/Lottie sizes and limits. LCP < 2.5s, CLS < 0.1 and INP < 200ms use honest measured/estimated provenance. Missing numbers/fallbacks or unresolved budgets prevent PASS; cuts require actual remeasurement.
- **Native UI plus technical checks:** Agent Desktop operates the task's app/window through fresh qualified accessibility refs. Playwright/Chromium and Open 3D tools separately measure exact viewports/DOM/console/network/performance and deterministic frames. Missing required native session/permission evidence is BLOCKED; a headless screenshot is not proof of a successful desktop interaction.
- **Final QA and handoff:** actual integrated visuals, motion, accessibility, performance, UX, audio and determinism evidence must pass before versioned export. Existing source files remain editable and target imports are executable-checked.

Read the [QA rubric](references/qa-rubric.md), [Agent Desktop contract](references/agent-desktop-integration.md), [UX audit workflow](references/ux-laws-workflow.md) and [completion checklist](references/missing-checklist.md). Decorative 3D cannot obscure headings/CTAs or intercept input; mobile/touch/reduced-motion/static fallbacks remain required.

## Versioned /buildme handoff

After final QA PASS, the exporter creates the generated project's `/handoff/` root with:

- `tokens.json`: colors, typography, spacing, radii, shadows and breakpoints; no implicit Inter.
- `motion-spec.json`: animation IDs, durations/units, easings/springs, ScrollTrigger ranges and every reduced mapping.
- `gsap-timeline.js`, `gsap-timeline-reduced.js`, `threejs-scene.js`: deterministic importable modules with the verified lifecycle, including scene resize/dispose.
- `handoff.md`, `handoff-manifest.json`, a target-aware import helper and all referenced assets/dependencies, with immutable releases under `versions/<export-version>/`.

The exporter reads the real `/buildme` token-snapshotter plus the target's design/token/snapshot/import files. The inspected consumer has no universal token-key schema: names must match the actual target. Missing consumer contracts, files, dependency closure, versions or executable import evidence fail export. No manual code/token reconstruction is an acceptable handoff. See [token-handoff-exporter](agents/token-handoff-exporter.md).

## Install

Clone/download this repository, then follow the complete [install gate](SKILL.md#0--install-gate). Helpers reuse verified installations; never overwrite an unrelated checkout or treat an installed binary as a passing runtime check.

```bash
git clone https://github.com/almanalaysay93-gif/designme.git
cd designme
# Only missing/unverified source needs inspection; the helper reuses valid checkouts.
bash scripts/install-animejs.sh
bash scripts/install-agent-desktop.sh
npx skills add https://github.com/vercel-labs/agent-desktop --skill agent-desktop -g
# Install the remaining selected providers/packs from SKILL.md's install gate.
# When html-video is assigned:
# bash scripts/install-html-video.sh
# Install this complete instruction package for Claude Code, preserving all subfolders:
mkdir -p ~/.claude/skills/designme
cp -R SKILL.md agents references scripts manifest.json ~/.claude/skills/designme/
```

The skill folder/frontmatter name is `designme`; compatible harnesses can load the same package using their supported skill installation mechanism. Check existing versions first and do not erase unrelated customizations. Native desktop work needs actual supported OS/session permissions; local rendering needs the selected browser/Node/Python/FFmpeg dependencies. Record exact versions, sources and checks in `motion-skills-installed.md`; optional local providers install only under their current task contract.

All agents use free, local, open-source or already-installed capabilities. Paid generation, cloud rendering, soundtrack/model APIs, billing and credit-consuming paths remain disabled. Engine/license eligibility still needs verification; an open-source instruction package does not grant a third-party commercial engine license. Superlite is the single execution adapter, not a second coordinator; never enable it with Superpowers.

## Speckit theme/design lock before Wave 2

[Speckit Theme Builder](agents/speckit-theme-builder.md) converts approved grill/spec decisions, actual repo facts, real screenshots and moodboard into `/speckit-theme-design/` project_context.md, constitution.md, spec.md, plan.md and tasks.md plus a lock checklist. Theme/design only: no backend/database/business implementation. Missing values become concrete OPEN QUESTION entries in unlocked context and stop work; they are never guessed.

[Speckit Theme Reviewer](agents/speckit-theme-reviewer.md) does not edit those files. It checks sources, completeness, consistency, constitution, component states, reduced mappings and exact T001–T018 / US-1–US-4 traceability, then writes speckit-review.md with file/line fixes and PASS/FAIL. Two review attempts total; second FAIL pauses for **fix brief or approve with risk**. Explicit risk acceptance is scoped/versioned and never supplies missing values or erases later quality gates. T018 remains the last exporter's own package lock, preserving last-after-QA export order.

## Agent catalog

All 31 agent contracts are retained. Core wave membership comes from SKILL.md/manifest.json; other roles run as their supporting dependencies and reviews.

| Agent | Responsibility |
| --- | --- |
| [planner-griller](agents/planner-griller.md) | Approved brief, goal, thesis and optional-agent decisions |
| [speckit-theme-builder](agents/speckit-theme-builder.md) | Five-file evidence-based theme/design specification and lock checklist |
| [speckit-theme-reviewer](agents/speckit-theme-reviewer.md) | Strict read-only review and two-attempt escalation before Wave 2 |
| [design-dna-agent](agents/design-dna-agent.md) | Reference-based design tokens and visual DNA |
| [motion-design-agent](agents/motion-design-agent.md) | Timing, easing, choreography and motion doctrine |
| [gsap-agent](agents/gsap-agent.md) | Assigned GSAP timelines and specialist choreography |
| [threejs-agent](agents/threejs-agent.md) | Assigned 3D scenes, geometry, particles and model integration |
| [hyperframes-agent](agents/hyperframes-agent.md) | Default final-film composition and local rendering |
| [motion-a11y-agent](agents/motion-a11y-agent.md) | Every-animation reduced variants, temporal contrast and focus gate |
| [genjutsu-agent](agents/genjutsu-agent.md) | Refined thesis and anti-slop review before final gates |
| [render-perf-budget-agent](agents/render-perf-budget-agent.md) | First-paint fallback, Web Vitals and JS/GLB/Lottie budget gate |
| [qa-anti-slop-agent](agents/qa-anti-slop-agent.md) | Final integrated design, motion, UX and evidence review |
| [token-handoff-exporter](agents/token-handoff-exporter.md) | Last-after-QA versioned /buildme exports and import validation |
| [animejs-agent](agents/animejs-agent.md) | Default landing-page text, staggered elements and SVG/UI motion |
| [beat-sync-agent](agents/beat-sync-agent.md) | Canonical beat/frame map and audio cue timing |
| [browser-agent](agents/browser-agent.md) | Agent Desktop reference/UI evidence and separate browser measurements |
| [find-skills-agent](agents/find-skills-agent.md) | Verified compatible skills and installed-source records |
| [hairline-agent](agents/hairline-agent.md) | Approved accessible interactive line figures |
| [img2threejs-agent](agents/img2threejs-agent.md) | Approved reference-object/character procedural reconstruction |
| [launch-director-agent](agents/launch-director-agent.md) | Creative directions, story, shot and camera planning |
| [motion-craft-agent](agents/motion-craft-agent.md) | Contact sheets, frame/safe-area/audio review and repairs |
| [motionmaxxing-agent](agents/motionmaxxing-agent.md) | Brand/depth/camera/pacing guidance and integrated craft review |
| [open-3d-agent](agents/open-3d-agent.md) | Eight-skill assessment, 3D/media modules, site-check and capture |
| [opus5-videos-agent](agents/opus5-videos-agent.md) | Approved code-video prompt catalog research |
| [parallax-background-agent](agents/parallax-background-agent.md) | Goal/reference-led multilayer animated background construction |
| [prompt-reference-agent](agents/prompt-reference-agent.md) | Build-fit animated-word/background research and prompt references |
| [remotion-agent](agents/remotion-agent.md) | Assigned React sequences/supporting clips and explicit standalone output |
| [superlite-agent](agents/superlite-agent.md) | Dependency/file ownership planning and engineering review |
| [taste-gsd-agent](agents/taste-gsd-agent.md) | Aesthetic critique and execution feedback |
| [ui-ux-pro-max-agent](agents/ui-ux-pro-max-agent.md) | Local UI/UX design-system and stack intelligence |
| [visual-style-agent](agents/visual-style-agent.md) | One primary visual language and optional supporting style |

## Repository maintenance

- `SKILL.md` owns scheduling and gates; `manifest.json` and state/workflow references must agree.
- `agents/` contains the 31 contracts. Preserve existing agents unless an edit is explicitly requested.
- `references/` connects provider details, research, ownership, UX, QA and handoff requirements.
- `scripts/` contains safe install helpers and the standard-library repository consistency checker.
- [`.github/repository-about.json`](.github/repository-about.json) is the tracked source for GitHub's About description; it is metadata, not another skill.

Run `python3 scripts/validate-repo.py` before publishing documentation changes. The validator checks role coverage, Wave 1.5 readiness/retry limits, wave/state consistency, required gate/export fields, the full catalog, local Markdown file links and About metadata. It does not claim to run a website or pass runtime accessibility/performance tests.

To synchronize the repository's About after the source file is reviewed, an authorized maintainer can run:

```bash
gh api --method PATCH repos/almanalaysay93-gif/designme --input .github/repository-about.json --jq '{description: .description, url: .html_url}'
```

## Twenty practical product-design principles in the plan

The planner incorporates [DP01–DP20](references/product-design-principles.md) into the five Speckit files: clean meaningful content, coherent design tokens/type/icons, real product proof and feature/CTA hierarchy, approved accent color, spacing/derived radii, readable wrapping/contrast/optical alignment, tabular numeric UI, real loading states and useful reduced-safe feedback. Each principle needs a concrete source-backed decision or justified N/A, spec/plan/task acceptance and reviewer coverage. Missing product-specific values/assets remain OPEN QUESTION; no fake screenshots, claims or arbitrary design defaults are introduced.
