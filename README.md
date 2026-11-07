# /designme — invoke with /designme

One skill that spawns a griller/planner, a visual-style director, parallel creative and engineering agents, an optional procedural 3D reconstruction agent (`img2threejs-agent`), a direction pass, a beat-sync pass, a motion-craft review, and a final anti-slop QA loop with Agent Desktop UI and local render verification.

> **Scope:** HyperFrames is the default renderer. Remotion, motionmaxxing and Open 3D are normal specialists that contribute useful components, supporting footage, motion guidance and integrated review alongside HyperFrames. `hairline-agent` is optional and runs only for interactive figures or pointer-responsive web visuals. `img2threejs-agent` is optional and runs only when a project provides a 2D reference image to reconstruct as a procedural Three.js `THREE.Group` model in code from [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs). Blotato supplies prompt references; Remotion supplies both references and useful local supporting sequences. All agents follow a free-only policy with no paid APIs, cloud rendering, publishing, scheduling, or credits. `opus5-videos-agent` is optional and only researches prompts from [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos). motionmaxxing must not call ElevenLabs. `qa-anti-slop-agent` uses [Agent Desktop](https://github.com/vercel-labs/agent-desktop) for live UI verification and local render/measurement tools for technical evidence.

## Invoke

```text
/designme premium 9:16 launch reel, Linear + Stripe refs, heavy physical feel, no AI purple slop
```

## Optional-agent grilling gate

During the first grilling session, `planner-griller` must select a visual language from the 20-style library, then recommend whether each optional agent and iart-ai motion-skill pack is needed and ask for approval:

| Optional agent | Use it when | Default recommendation |
|---|---|---|
| `hairline-agent` | The brief requires an interactive line figure, pointer-responsive diagram, technical illustration, or self-contained Hairline visual | Ask the user; state whether the brief matches the trigger. Never assume skip |
| `opus5-videos-agent` | The brief explicitly wants a starting prompt from the Opus 5.5 code-video catalog | Ask the user. It researches prompts only and does not render |
| `ui-ux-pro-max-agent` | UI, landing page, dashboard, product demo, forms, navigation, charts, mobile UI, or UX/accessibility review | Run for any interface. Ask the user only for pure non-UI films |
| `img2threejs-agent` | The brief supplies a 2D reference image of an object, product, prop, or character and requires a procedural code-only Three.js `THREE.Group` reconstruction | Ask the user whether a reference-image reconstruction is wanted. Never assume skip |

Full dispatch rule: every core agent in this file runs on every invocation. Only the optional agents above are gated, and each gate is resolved by asking the user, never by assumption. A skip needs the user's answer, recorded in `brief.json.optionalAgents`.

The recommendation is stored in `brief.json.optionalAgents`. Optional agents are never silently activated. A user request can approve an agent even when it is not strictly necessary, with the tradeoff recorded. There is one final owner per deliverable, normally HyperFrames for films; normal specialists may produce intermediate assets under the production contract.

## Procedural 3D reconstruction (`img2threejs-agent`)

`img2threejs-agent` adds [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) (Apache-2.0, v2.0.0) as an optional Wave 2 agent. It gates reconstruction through `forge/state.py` and `forge/next.py` across 8 passes (`blockout` to `optimization`), verifies each pass in local Chromium, and hands a deterministic `create<ObjectName>Model(spec, options)` `THREE.Group` factory to `threejs-agent` in Wave 3.

See [`references/img2threejs.md`](references/img2threejs.md).

## Agent Desktop and render QA

`browser-agent` and final QA use `vercel-labs/agent-desktop` for task-scoped app/window snapshots, native accessibility ref actions, UI observations and visual evidence. This replaces the former interactive browser tool while preserving role names and report handoffs. Actual OS/session permissions and capability checks are required; a headless container is not assumed to have an accessible desktop.

Playwright/Chromium and Open 3D checks retain exact viewport/DOM/console/network/performance and deterministic rendering responsibilities. Agent Desktop is not a DOM evaluator or video engine. Missing required native interaction evidence is reported as BLOCKED. BrowserCode is only an optional requested preview target.

See [installation, interaction loop, platform requirements and evidence contract](references/agent-desktop-integration.md).

## UI/UX Pro Max design intelligence

`ui-ux-pro-max-agent` adds the MIT-licensed [UI/UX Pro Max skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) as an optional local design-intelligence layer. It searches styles, palettes, typography, UX rules, charts, icons, GSAP presets, and stack guidance, then writes `uiux-design-system.md` and `uiux-audit.md`. It is selected during grilling for interface-containing projects and skipped for pure non-UI films.

See [`references/ui-ux-pro-max-integration.md`](references/ui-ux-pro-max-integration.md).

## 20-style visual language library

Designme now includes a style library for: neon glow, particle swarm, pixel art, glitch, glassmorphism, liquid morph, holographic foil, clay 3D, kinetic typography, vaporwave grid, halftone dots, Bauhaus shapes, ASCII art, paper cutout, flow fields, dithering, risograph print, metaballs, topographic lines, and ray-marched fractals. During grilling, choose one primary and at most one supporting style. `visual-style-agent` writes `style-spec.md` with the material system, palette, motion grammar, hero beat, build sample, renderer handoff, and anti-slop checks.

Read [`references/visual-style-library.md`](references/visual-style-library.md) for the full recipes and code patterns.

## iart-ai motion-skill packs

The reel points to [`iart-ai/motion-skills`](https://github.com/iart-ai/motion-skills), a free MIT library of 51 skills across 15 packs. Designme routes the smallest compatible pack set to existing agents instead of blindly running every pack. The selected packs are recorded in `brief.json.motionSkillPacks`, installed only after approval, and verified through the normal render/screenshot/probe QA loop.

See [`references/motion-skills-packs.md`](references/motion-skills-packs.md) for the complete pack matrix and agent ownership.

## What was added

The update keeps **HyperFrames as the default renderer** and adds compatible production skills from the supplied list. Remotion is available through its dedicated conditional agent when explicitly requested:

- `AbubakrChan/product-launch-motion` → `launch-director-agent`: competing directions, launch-film story, word-locked reveals, motivated camera language, look, and finishing.
- `Sunwood-ai-lab/hyperframes-motion-reel-skill` → `beat-sync-agent`: BPM/frame grids, morphing transitions, deterministic timelines, and code-generated score planning.
- `whaleyxbt/claude-motion` → `motion-craft-agent`: contact-sheet self-review, frame-level checks, web-sim guidance, and deterministic code-authored sound.
- `Blotato-Inc/blotato-skills` + `remotion-dev/skills` → `prompt-reference-agent`: free prompt patterns for brand intake, hooks, grading, repurposing, React/video composition, captions, and future projects.
- `remotion-dev/remotion` + `remotion-dev/skills` → `remotion-agent`: explicit local React-to-video builds with frame-accurate compositions, captions, audio, and still-frame QA.
- `iart-ai/motion-skills` → routed pack library: short-form, data, explainer, web, kinetic typography, WebGL, Manim, map, ad, ecommerce, and generative-illustration workflows.
- `lucasmarkes/hairline` → `hairline-agent`: optional accessible interactive line figures and pointer-responsive web visuals, validated in a browser.
- `Tejashmakwana/motionmaxxing` → `motionmaxxing-agent`: normal brand-specific motion/depth/pacing planning and integrated craft review; an explicit standalone film can still use its runtime and G0–G5 gates. See [`references/motionmaxxing.md`](references/motionmaxxing.md).
- `yihui-dev/awesome-opus5-5-videos` → `opus5-videos-agent`: optional MIT prompt catalog. Picks a few code-authored video prompts, credits the creators, and rewrites the craft for this brand. See [`references/opus5-videos.md`](references/opus5-videos.md).
- `img2threejs/img2threejs` → `img2threejs-agent`: optional Apache-2.0 procedural image-to-Three.js reconstruction agent. See [`references/img2threejs.md`](references/img2threejs.md).
- `vercel-labs/agent-desktop` → browser-agent and QA: native UI interaction and scoped reference/visual evidence; separate local Playwright/site-check tools supply exact browser/render measurements.

## Free-only rule

All 30 agents are restricted to free, local, open-source, or already-installed tooling. They must not call paid APIs, paid tiers, metered SaaS, premium models, paid voice or asset services, subscriptions, trials, billing, or credit-consuming services. If a capability is not available for free, the agent must stop that part and offer a local or deterministic alternative. The motionmaxxing skill's ElevenLabs voice path is off, and `img2threejs-agent` paid/external neural mesh adapters are off.

## Structure

- `SKILL.md` — `/designme` contract, install gate, dependency waves, optional-agent gate, and output contract
- `agents/` — creative direction, motion engineering, visual-style direction, UI/UX Pro Max intelligence, normal Remotion/motionmaxxing/Open 3D specialists and optional Hairline/Opus-prompt/img2threejs agents, craft review, and QA agents
- `references/` — grilling questions, prompt sources, iart motion-pack routing, motionmaxxing contract, Opus 5.5 prompt catalog, img2threejs integration, Agent Desktop + render QA verification, visual-style library, UI/UX Pro Max integration, Superlite adapter, UX laws, QA rubric, asset pipeline, missing checklist, and orchestration state
- `manifest.json` — selected source repositories and agent responsibilities

## Install

```bash
# Required: download official Anime.js source when installing Designme.
# Run from the designme repository root. Reuses a verified existing checkout.
bash scripts/install-animejs.sh
npx skills add CloudAI-X/threejs-skills greensock/gsap-skills zanwei/design-dna LottieFiles/motion-design-skill https://genjutsu.athevon.dev heygen-com/hyperframes -g
npx skills add whaleyxbt/claude-motion AbubakrChan/product-launch-motion Sunwood-ai-labs/hyperframes-motion-reel-skill -g
npx skills add remotion-dev/skills lucasmarkes/hairline Tejashmakwana/motionmaxxing -g
git clone https://github.com/img2threejs/img2threejs.git ~/.agents/skills/img2threejs
# Optional UI/UX Pro Max local skill (MIT, bundled data + Python search)
npm install -g ui-ux-pro-max-cli && uipro init --ai claude --global
# Opus prompt catalog is cloned by opus5-videos-agent when approved; see references/opus5-videos.md
# Add only the iart-ai packs approved during grilling; see references/motion-skills-packs.md
bash scripts/install-agent-desktop.sh
npx skills add https://github.com/vercel-labs/agent-desktop --skill agent-desktop -g
npx skills add thedotmack/claude-mem -g
# Superlite adapter is bundled; optional native plugin: references/superlite-integration.md
npx skills add https://github.com/anthropics/skills --skill frontend-design --skill skill-creator --skill mcp-builder --skill webapp-testing -g
npx skills add vercel-labs/skills --skill find-skills -g
# taste: install from Leonxlnx/taste-skill (folder taste-skill). gsd is not used.
cp -r ./designme ~/.claude/skills/designme
```

Claude Code will now show `/designme` in the slash menu.

## Superlite execution

This skill now uses a bundled [Superlite execution adapter](references/superlite-integration.md) for
dependency-aware tasks, single-owner file contracts, targeted repairs and fresh
final review. Its specialty workflow and quality gates remain in charge. No native
plugin or model service is required. The reference includes optional native-plugin
setup and host limitations. Never enable Superlite alongside Superpowers.

## Mandatory UX laws

The bundled [14-law UX reference](references/ux-laws.md) now applies to planning,
implementation and post-build review. Plans map the laws to actual flows; every
build or significant change produces `UX_LAWS_AUDIT.md` with evidence, fixes and
re-audit results. Completion requires no violations and documented reasons for
any justified Partial results. See [the audit workflow](references/ux-laws-workflow.md).

## Anime.js for landing pages and animated words

Anime.js is the default for animated landing-page text, staggered elements, SVG accents, and ordinary UI motion. The existing `prompt-reference-agent` researches 3–5 relevant animated-word examples, cites sources, and shortlists treatments that fit the build's copy, brand, audience, and pacing. `motion-design-agent` uses those references before `animejs-agent` implements the selected treatment.

The coordinator records engine choice in `brief.json.animation` and target/property ownership in `animation-plan.json`, preventing Anime.js/GSAP conflicts. Static briefs and explicit stack choices take precedence. The Designme installer downloads the official Anime.js repository to `~/.agents/tools/animejs` using `scripts/install-animejs.sh`. Existing official checkouts are verified and reused. Install `animejs@4` only in the target build and pin its lockfile; no additional external skill is required. QA verifies mobile wrapping, semantic readable text, keyboard access, reduced motion, cleanup, and deterministic video seeking where applicable. Web-only landing pages do not require video rendering.

See [Anime.js integration and research contract](references/animejs-integration.md) and the [Anime.js specialist](agents/animejs-agent.md).

## Open 3D specialist in the loop

`open-3d-agent` integrates selected [Open 3D Skills](https://github.com/Moh4696/open-3d-skills): procedural scenes, exploded product views, scroll films, transparent media, cursor rigs and browser/performance checks. It plans in Wave 2, implements assigned modules in Wave 3 and validates the integrated draft in Wave 4. Craft/QA findings return to the responsible agent and are rechecked within the existing three-loop repair cap.

The coordinator assigns one scene owner alongside `threejs-agent` and preserves Anime.js for landing-page text/UI. All eight upstream skills are made available and assessed; the agent executes every relevant capability, with explicit reasons for skips and required local dependencies installed as needed; paid generation remains disabled and media comes from supplied/local assets. Capture stays within the existing final-renderer decision.

See [integration, install, ownership and repair contract](references/open-3d-integration.md) and [agent instructions](agents/open-3d-agent.md).

Full-library use is tracked in `open-3d-capabilities.json`: all eight skills get use/skip/blocked decisions and used skills get tasks, outputs, checks and execution evidence. Asset planning/logs and local repair tools are included. Enabled animated/3D web builds require site-check, with targeted motion recordings when stills cannot verify the behavior.

## Normal production loop, especially 3D parallax websites

Remotion, motionmaxxing and Open 3D are assessed on every build and dispatched when relevant without separate opt-in gates. Remotion creates useful supporting sequences, Open 3D supplies live scenes/media/captured footage, and motionmaxxing contributes motion direction and reviews the integrated result. HyperFrames assembles final films from verified local assets. Record a no-work reason rather than manufacturing unnecessary output.

For a **3D parallax website**, enable the dedicated profile: parallax-background-agent builds background layers with Open 3D techniques and an explicit scene owner; motionmaxxing guides depth/camera/scroll pacing, Anime.js animates assigned text/UI, and one normalized scroll progress drives the consumers. Remotion assesses useful pre-rendered sequences. The website stays live and interactive, with mobile, reduced-motion, readable CTA and performance checks. A companion film uses captured scene footage inside HyperFrames only when requested.

See [normal specialist routing, intermediate-asset contract and 3D parallax profile](references/normal-motion-orchestration.md).

## Goal-led animated backgrounds

`parallax-background-agent` designs and builds multilayer 3D/parallax animated website backgrounds based on website type, primary goal/CTA, brand, reference images and device budgets. It researches/inspects references, plans depth/layers and provider handoffs, implements owned background modules, validates the integrated site and receives targeted repairs through the normal loop.

It assesses HyperFrames, Remotion, motionmaxxing, Open 3D, html-video and img2threejs. Live scenes, image-based 2.5D layers, procedural animation and justified footage can be combined while preserving one scene/progress owner, readable CTAs and mobile/reduced-motion/static fallbacks. img2threejs is used when an approved reference object needs procedural reconstruction; a single image is not treated as a complete 3D environment. The corrected [nexu-io/html-video](https://github.com/nexu-io/html-video) source supplies goal-fit HTML templates and local supporting footage; see [its local install/render contract](references/html-video-integration.md) for engine discovery and frame-accuracy limitations. Paid audio/model generation stays disabled.

See [background architecture, provider decisions, reference routing and verification](references/parallax-background-integration.md).

## Motion accessibility, performance and /buildme handoff

The core schedule is now: Wave 1 planner-griller; Wave 2 design-dna and motion-design; Wave 3 gsap, threejs, hyperframes and motion-a11y; Wave 4 genjutsu thesis, render-perf-budget, final QA and token-handoff-exporter, in that order. Existing agents remain intact and retain supporting tasks under SKILL.md's dependency rules.

The three new contracts are [motion accessibility](agents/motion-a11y-agent.md), [render/performance budgets](agents/render-perf-budget-agent.md) and [versioned token/motion handoff](agents/token-handoff-exporter.md). The exporter runs last, only after QA PASS on the tested revision, and validates actual /buildme token names, complete files/assets, versions and executable import compatibility before publishing /handoff/.
