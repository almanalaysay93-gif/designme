---
name: designme
description: Premium anti-AI-slop design and motion studio. Invoke with /designme for high-craft web animation, launch films, showreels, interactive figures, procedural 3D object reconstructions, and deterministic HTML video. Combines goal-led multilayer parallax backgrounds, Three.js, Open 3D Skills, img2threejs, GSAP, Anime.js, Design DNA, motion principles, Genjutsu, HyperFrames, launch direction, beat sync, code-generated sound, frame review, Hairline, Remotion, motionmaxxing, an Opus 5.5 video-prompt researcher, a 20-style visual language library, UI/UX Pro Max design intelligence, Superlite execution, 14 UX laws, and Agent Desktop + render QA in one orchestrated command.
allowed-tools: Task, Read, Write, Edit, Bash, Glob, Grep
---

# /designme — The Anti-Slop Design Studio

Invoke: `/designme <brief>` — e.g. `/designme premium 9:16 launch reel, Linear + Stripe refs, heavy physical feel, no AI purple slop`

## What This Is

One command for brand-led, code-authored motion and interactive web visuals. HyperFrames remains the default video renderer, Remotion is a normal local React sequence/clip specialist, motionmaxxing is a normal motion-direction and craft-review specialist, Hairline is an optional interactive-figure engine, and img2threejs is an optional procedural image-to-3D reconstruction engine. Blotato and Remotion are also used as free prompt/reference sources for future projects. It adds only complementary production disciplines:

- **Design DNA + motion principles:** extract a visual system and a motion doctrine before code.
- **Direction:** develop competing creative directions, a one-claim story arc, camera language, and shot plan.
- **Visual language:** select one primary style and at most one supporting style, then turn it into a material, motion, camera, shader, proof, and anti-slop specification.
- **UI/UX intelligence:** use local UI/UX Pro Max search for interface styles, palettes, typography, UX rules, charts, icons, GSAP guidance, and stack-specific implementation.
- **Procedural 3D reconstruction:** when approved, `img2threejs-agent` rebuilds a 2D reference image of an object or character into a deterministic code-only `THREE.Group` factory (`create<ObjectName>Model`) for `threejs-agent`.
- **Beat sync:** make a shared beat/timeline table that drives visuals, transitions, captions, and audio cues.
- **Craft:** default to Anime.js for landing-page text and element animation; use GSAP for assigned specialist choreography, Three.js for hero 3D, and pure `render(t)` functions for seek-safe generative layers.
- **Sound:** write code-generated cues or wire approved audio against the same timeline, then master and verify it.
- **Review:** render stills/contact sheets at beats and inspect them before final MP4 rendering.
- **Motion skill packs:** route the approved iart-ai packs to the agents that need them; install only the smallest compatible set.
- **Optional capabilities:** discuss Hairline, img2threejs, the Opus 5.5 video-prompt catalog, and motion-skill pack selection during grilling, recommend what is needed, and activate only the user-approved choices.
- **Opus prompt research:** when approved, `opus5-videos-agent` reads a few matching prompts from the MIT catalog, credits the creators, and rewrites the craft for this brand. It never renders and never replaces the video renderer.
- **Measured motion:** motionmaxxing contributes brand-specific pacing, camera/depth guidance and integrated review alongside HyperFrames; standalone final mode is reserved for an explicit motionmaxxing deliverable.
- **QA:** run anti-slop, determinism, readability, audio, accessibility, UX laws, and final-frame checks with Agent Desktop UI and local render verification and targeted feedback loops.

## Invocation Contract

Claude Code sees `/designme` because the skill folder is named `designme` and frontmatter name is `designme`. When the user types `/designme`, `designme`, or asks for premium animation that does not look AI-generated, load this skill.

## Mandatory Orchestration (DO NOT SKIP)

Every invocation dispatches every core agent and workflow stage this file defines, through the Agent tool, in the waves it specifies. Do not decide on your own that an agent, stage, or review is unnecessary. Each one ends with its output file or a BLOCKED entry naming the missing dependency and its fix. Optional agents (Hairline, Opus prompt research, img2threejs) are resolved by asking the user during grilling, never by assumption. "Skip" is allowed only where this file says a stage owns nothing or is web-only, and it must be recorded with the reason.

### 0 — Install Gate

Read the [Superlite execution adapter](references/superlite-integration.md).
Designme is the sole coordinator. Superlite replaces the Superpowers engineering
role; never enable both plugins together. The bundled adapter needs no plugin
installation or paid model routing.

Always ensure the official Anime.js repository is downloaded during Designme installation, including static or non-Anime.js builds. Run `bash scripts/install-animejs.sh` from this skill directory; the default checkout is `~/.agents/tools/animejs`. Do not mark installation complete if the download/verification fails. Record its path and commit in `motion-skills-installed.md`. Then check whether the remaining dependencies are installed and install the selected skills:

```bash
# Required: download official Anime.js source when installing Designme.
# Run from the designme repository root. Reuses a verified existing checkout.
bash scripts/install-animejs.sh
npx skills add CloudAI-X/threejs-skills greensock/gsap-skills zanwei/design-dna LottieFiles/motion-design-skill https://genjutsu.athevon.dev heygen-com/hyperframes -g
npx skills add whaleyxbt/claude-motion AbubakrChan/product-launch-motion Sunwood-ai-labs/hyperframes-motion-reel-skill -g
npx skills add remotion-dev/skills -g  # official prompt/reference guidance; local Remotion only
npx skills add lucasmarkes/hairline -g  # optional interactive figures; free/local only
npx skills add Tejashmakwana/motionmaxxing -g  # normal craft planning/review; free/local only, no ElevenLabs
# Optional img2threejs procedural 3D reconstruction (canonical ~/.agents/skills/img2threejs)
# git clone https://github.com/img2threejs/img2threejs.git ~/.agents/skills/img2threejs
# Optional UI/UX Pro Max local skill; MIT, bundled data + Python search, no paid APIs
# npm install -g ui-ux-pro-max-cli && uipro init --ai claude --global
# opus5-videos-agent clones yihui-dev/awesome-opus5-5-videos on approval. It is a prompt catalog, not an npx skill.
# html-video source when assigned: bash scripts/install-html-video.sh
# See references/html-video-integration.md for local build/engine checks.
# Install only the approved iart-ai packs selected during grilling; see references/motion-skills-packs.md
bash scripts/install-agent-desktop.sh
npx skills add https://github.com/vercel-labs/agent-desktop --skill agent-desktop -g
npx skills add thedotmack/claude-mem -g
# Superlite adapter is bundled; optional native plugin: references/superlite-integration.md
npx skills add https://github.com/anthropics/skills --skill frontend-design --skill skill-creator --skill mcp-builder --skill webapp-testing -g
npx skills add vercel-labs/skills --skill find-skills -g
# taste is installed from Leonxlnx/taste-skill (folder taste-skill); gsd is not used here (no 'gsd' skill exists upstream)
```

Read [normal motion orchestration](references/normal-motion-orchestration.md). Remotion, motionmaxxing and Open 3D are normal specialists assessed and dispatched when relevant without separate opt-in gates. HyperFrames owns final film assembly by default; Remotion/Open 3D may render assigned intermediate assets. motionmaxxing normally plans and reviews in contribution mode. One final owner per deliverable, with explicit standalone renderer overrides. Hairline retains its existing optional-agent gate.

Activate `opus5-videos-agent` only when the user wants a starting prompt from the Opus 5.5 video catalog. It runs in Wave 1, writes `opus-prompt-brief.md`, and is not a video renderer. Read `references/opus5-videos.md`. Activate `ui-ux-pro-max-agent` for UI-containing work when approved; skip it for pure non-UI films. It runs in Wave 2 and writes `uiux-design-system.md` and `uiux-audit.md`. Activate `img2threejs-agent` only when approved for a 2D reference object or character image that must be reconstructed into a procedural Three.js `THREE.Group` factory in code. It runs in Wave 2 and hands `create<ObjectName>Model` to `threejs-agent` in Wave 3. Read `references/img2threejs.md`.

## Free-Only Execution Policy

Use only free, local, open-source, or already-installed tools and APIs. Never call a paid API, paid tier, metered SaaS endpoint, premium model, paid voice service, paid asset service, or billing-enabled integration. Never create a subscription, start a trial, enter payment details, or consume credits. Do not ask the user for API keys for a paid service. If a requested capability requires payment or a paid API, stop that part, explain the limitation, and propose a free/local alternative such as Python, FFmpeg, Chromium, Playwright, system tools, or deterministic code-generated assets. motionmaxxing's optional ElevenLabs voice, SFX, and music path is a paid API and is forbidden. `img2threejs-agent` must use only local `generic` and `character` profiles and never call Tripo, Hyper3D, CharacterGen, or paid cloud plugins.

## Animation engine routing

Read [Anime.js integration](references/animejs-integration.md). Prefer `animejs-agent` for animated landing pages, words, SVG accents, and ordinary elements. The existing `prompt-reference-agent` researches build-specific animated-word references before design planning. Record `brief.json.animation` and coordinator-owned `animation-plan.json`; assign each target/property to one engine before implementation. Honor static briefs and explicit stack choices. Anime.js is not a renderer; web-only builds do not require a video render.

## Open 3D specialist routing

For an explicitly requested recording of a web-only build, the coordinator may select `frame-capture` as the sole capture backend under the integration contract below; skip all film renderers and record `renderer-decision.md`. This is the only Open 3D exception to the film-renderer list.

Read [Open 3D integration](references/open-3d-integration.md). For relevant 3D/scroll/interactive builds, record `brief.json.open3d` and selected skills. Make all eight upstream skills available, assess each in `open-3d-capabilities.json`, and execute every relevant capability through evidence-backed verification. `open-3d-agent` plans in Wave 2, implements assigned modules in Wave 3, validates the integrated draft in Wave 4, and receives targeted QA repairs within the existing three-loop cap. Skip unrelated work with a recorded reason. Freeze ownership alongside Three.js, Anime.js and GSAP; retain the free-only policy.

## Goal-led animated backgrounds

Read [parallax background orchestration](references/parallax-background-integration.md). `parallax-background-agent` is a normal specialist, automatically active for requested 3D/multilayer/parallax animated backgrounds. It selects techniques from website type, primary goal and actually inspected reference images, assesses all six providers, builds assigned layers, and participates in integrated QA/repairs. Use the verified `nexu-io/html-video` provider through `references/html-video-integration.md`; inspect actual engine/runtime availability and preserve frame-accuracy and free-only requirements.

### 1 — The Griller (1 agent) — ALWAYS FIRST — BLOCKING

Spawn `planner-griller` with `references/grilling-questions.md`. It must cover goal, audience, references, anti-slop list, duration, aspect, resolution, story arc, audio/voice needs, stack, constraints, success metric, verification needs, the visual-style gate, the optional-agent gate, and motion-skill pack selection.

The griller must produce an explicit recommendation for every optional agent:

```json
{
  "optionalAgents": {
    "hairline-agent": {"requested": false, "needed": false, "reason": "No interactive figure requested"},
    "opus5-videos-agent": {"requested": false, "needed": false, "reason": "No Opus 5.5 prompt catalog requested"},
    "ui-ux-pro-max-agent": {"requested": false, "needed": false, "reason": "No UI or UX work requested"},
    "img2threejs-agent": {"requested": false, "needed": false, "reason": "No 2D reference object image for procedural 3D reconstruction"}
  },
  "visualStyle": {"primary": null, "secondary": null, "requested": true, "reason": "", "material": "", "motionGrammar": "", "heroBeat": "", "antiSlop": []},
  "motionSkillPacks": []
}
```

Show the thesis, renderer choice, optional-agent recommendations, and brief to the user. Do not proceed until the user approves them.

### 2 — Parallel Spawn — dependency-aware

The wave lists are dependency groups, not blanket parallel dispatch. Follow the
Superlite adapter: Wave 2 planning waits for design outputs, Wave 3 implementation
waits for animation ownership and, for video, the canonical beat map, and Wave 4 craft review waits for a renderer draft.

**Wave 1 (no dependencies):**

- `design-dna-agent` — extracts tokens from references.
- `memory-agent` — loads past taste and prior constraints.
- `find-skills-agent` — discovers only missing, compatible skills.
- `browser-agent` — uses Agent Desktop to inspect actual task-scoped reference pages/images and UI; records separate local DOM/render measurements in browser-report.md before dependent design planning. Read `references/agent-desktop-integration.md`.
- `prompt-reference-agent` — researches goal-fit background/depth treatments and inspects supplied images into `background-references.md` when needed; also researches 3–5 build-fit animated-word examples for landing pages/text-motion builds and writes `word-animation-references.md`; also curates free Blotato/Remotion prompt patterns.
- `opus5-videos-agent` — runs only if approved. Picks a few catalog prompts and writes `opus-prompt-brief.md` before direction. Otherwise mark skipped.
- `find-skills-agent` — routes approved iart-ai motion-skill packs to the owning agents and records local installs.

**Wave 2 (needs brief and Wave 1 context):**

- `visual-style-agent` — converts the selected visual style into a buildable style specification and sample recipe.
- `ui-ux-pro-max-agent` — runs only when approved for UI/UX work; creates a local searchable design system and UI audit.
- `img2threejs-agent` — runs only when approved for a 2D reference image; runs the staged sculpting pipeline (`blockout` to `optimization`) gated by `forge/state.py` and `forge/next.py` and outputs a deterministic `create<ObjectName>Model` `THREE.Group` factory.
- `motion-design-agent` — consumes `word-animation-references.md`, selects brand-fit text treatments, and writes timing, easing, weight, and choreography doctrine. The coordinator freezes target/property ownership in `animation-plan.json`.
- `launch-director-agent` — writes three visual directions, kills two, and creates the story/shot/camera/look plan.
- `parallax-background-agent` — writes goal/reference/provider/layer architecture and a reconstruction brief when needed; waits for research/style, then coordinates motionmaxxing and specialist handoffs before ownership freeze.
- `open-3d-agent` — when selected, consumes design inputs and writes `open-3d-plan.md` with chosen upstream skills, scene/file ownership, dependencies and acceptance budgets.
- `remotion-agent` — assesses useful React components/supporting clips and returns its plan or no-work reason.
- `motionmaxxing-agent` — contributes brand-specific pacing/camera/depth guidance before plan freeze.
- `superlite-agent` — writes the execution plan and tests, incorporating the Open 3D plan before contracts freeze.

**Wave 3 (needs Wave 2 outputs):**

- `remotion-agent` — builds and validates assigned intermediate clips/sequences against frozen production contracts.
- `beat-sync-agent` — creates the shared BPM/frame beat map, transition schedule, and audio cue plan.
- `parallax-background-agent` — builds assigned background layers/modules/media adapters after model/asset and ownership dependencies; shares one progress source and scene owner.
- `animejs-agent` — implements assigned landing-page/text/element motion after research, design and engine ownership are frozen; writes `animejs-plan.md`, `animejs-motion.js`, and `animejs-validation.md`. Read `references/animejs-integration.md`.
- `gsap-agent` — implements only its assigned seekable choreography targets; skip when Anime.js owns all motion. If motionmaxxing or Remotion owns the renderer, contribute doctrine and timing notes only; do not build a second HyperFrames timeline.
- `open-3d-agent` — resumes after ownership/dependency freeze, implements only assigned scene/media/interaction modules, and preserves one renderer/clock per scene.
- `threejs-agent` — implements only the necessary hero 3D or generative layer, inside the approved renderer, and mounts `create<ObjectName>Model` when `img2threejs-agent` is active.
- `genjutsu-agent` — writes thesis and anti-slop MASTER.md.
- `taste-gsd-agent` — performs the aesthetic gate and execution critique.

**Wave 4 (needs all design and engineering outputs):**

For web-only landing pages, the coordinator integrates the web build, retains specialist assessment/contribution/review tasks, and skips only unnecessary video-render tasks, final MP4 rendering and video-only artifacts. Motion-craft and QA inspect the live page.

- `hyperframes-agent` — consumes verified supporting clips, local sequences and scene layers; assembles the final-film draft by default. Skip only for a web-only deliverable or explicit alternate final owner, never merely because another specialist contributes.
- `remotion-agent` — supports clip integration/repairs; only owns final rendering for an explicit standalone deliverable.
- `motionmaxxing-agent` — reviews the integrated draft in contribution mode; writes `motionmaxxing-review.md` and returns findings to actual owners. Only owns final rendering for an explicit standalone deliverable.
- `hairline-agent` — runs only if `brief.json.optionalAgents.hairline-agent.requested` is true or the user explicitly approved it; otherwise mark skipped.
- `parallax-background-agent` — validates the integrated site, writes `background-validation.md`, and receives layer/provider repairs within the existing three-loop cap.
- `open-3d-agent` — resumes after integration for selected site-check/browser validation, writes `open-3d-validation.md`, and hands evidence/findings to craft review and QA.
- `motion-craft-agent` — reviews intermediate-asset joins and integrated frames, consumes motionmaxxing findings, checks safe areas and audio, and routes repairs to actual owners.

Read `references/normal-motion-orchestration.md`; freeze `production-plan.json` before implementation, and use its `3d-parallax` profile for 3D parallax websites. Captures of integrated pages precede final-film asset consumption.

Pass `brief.json`, the approved `motionSkillPacks`, and the relevant output paths to every agent. Never write animation code in the orchestrator; delegate it.

Run a fresh findings-only engineering review after integration and craft review;
route fixes to their owners and record evidence before the final QA gate.

### 3 — QA Anti-Slop Loop — ALWAYS LAST

Spawn `qa-anti-slop-agent` after composition and craft review. It reads `references/qa-rubric.md`, `references/agent-desktop-integration.md` and `references/missing-checklist.md`. Use Agent Desktop for actual UI/ref/visual verification and the existing local Playwright/site-check/render paths for exact measurements and deterministic evidence. Verify both design fit and every scheduled agent's plan compliance; report missing required desktop/session/permission checks as BLOCKED.

If `FAIL` or `SLOP`, write `feedback.md` naming the exact agent, file, line or timestamp, and fix. Re-spawn only that agent. Allow at most 3 loops. On the third failure, escalate with `audit.md` and the concrete risk.

If `PASS` and HyperFrames is the renderer, render the final MP4 and verify:

```bash
npx hyperframes render --width <width> --height <height> --fps 60
ffprobe -v error -show_streams -show_format output/final.mp4
```

If `PASS` and motionmaxxing owns the film, verify with its gates instead:

```bash
node "$MOTIONMAXXING/scripts/render.mjs" film/index.html film/final.mp4
python3 "$MOTIONMAXXING/scripts/look.py" film/final.mp4 --out film/look-final --expect <s>
node "$MOTIONMAXXING/scripts/lint.mjs" film/index.html
ffprobe -v error -show_streams -show_format film/final.mp4
```

Add `--audio` only when the mix is local or user-provided. Do not call ElevenLabs.

For video deliverables, compare two final renders by hash. If voice or music is present, verify captions, peak timing, loudness, and no drift. If Hairline is selected, include its browser/look validation in the QA evidence. If UI/UX Pro Max is selected, include `uiux-design-system.md`, `uiux-audit.md`, local search queries, responsive/keyboard/focus evidence, and reduced-motion checks. If `img2threejs-agent` is selected, include `.img2threejs/state.json`, `sculpt-spec.json`, `img2threejs-passes/`, and `img2threejs-report.md` in the QA evidence. If motionmaxxing owns an explicit standalone film, `film/NOTE.md` must quote G0–G5 and a fail is not a pass; contribution mode instead requires `motionmaxxing-plan.md` and applicable `motionmaxxing-review.md`. If the Opus catalog was selected, `opus-prompt-brief.md` must credit its sources and the film must not be a shot-for-shot clone.

## Output Contract

- `background-plan.json`, `background-design.md`, assigned `background/` modules/assets, `background-references.md` and `background-validation.md` when backgrounds apply

- `production-plan.json`, `motionmaxxing-plan.md` and `motionmaxxing-review.md` when applicable; assigned Remotion plans/source/clips and validation evidence, with no-work reasons for unneeded specialist work

- `/hyperframes/output/final.mp4` when HyperFrames is the renderer
- `/hyperframes/composition/` with `index.html`, `style.css`, `script.js`, `tokens.css`, and assets, when HyperFrames is the renderer
- `film/index.html`, `film/STORYBOARD.md`, `film/NOTE.md`, `film/final.mp4`, and `film/look-final/` when motionmaxxing owns the film
- `renderer-decision.md` for video deliverables with an explicit final owner other than HyperFrames
- `UX_LAWS_AUDIT.md` with all 14 laws, evidence, fixes and re-audit results
- `brief.json`, `design-dna.json`, `style-spec.md`, `uiux-design-system.md` when applicable, `uiux-audit.md` when applicable, `sculpt-spec.json` and `img2threejs-report.md` when applicable, `motion-doctrine.md`, `directions.md`, `shot-plan.md`
- `timeline.json` or `beat-map.json`, `audio-cues.md`, and `audio_meta.json` when applicable
- `open-3d-capabilities.json`, `open-3d-plan.md`, assigned modules/assets and `open-3d-validation.md` when Open 3D is enabled; `open-3d-assets.md` and provenance logs when assets are involved
- `animation-plan.json` when motion applies; `word-animation-references.md` when text research applies; `animejs-plan.md`, `animejs-motion.js`, and `animejs-validation.md` when Anime.js is used
- `thesis.md`, `plan.md`, `browser-report.md`, `prompt-reference.md`, `opus-prompt-brief.md` when applicable, `brief-enhancements.md`, `motion-skills-installed.md`, `hairline-design.md` when applicable, `hairline-validation.md` when applicable, `contact-sheet.png`, and `audit.md`

No generic gradients, default purple-on-black SaaS styling, unmotivated bounce, or code-first production. The selected visual style must be an intentional system, not a list of effects. Every visual and sound cue must have an intentional role in the approved thesis.

## Mandatory UX laws

Before planning or building, read the complete [UX laws reference](references/ux-laws.md)
and [its workflow](references/ux-laws-workflow.md). Map all 14 laws in the plan and
include the relevant checks in every specialist handoff. After every build or
significant change, complete `UX_LAWS_AUDIT.md`, fix findings and re-audit before
completion. The audit is mandatory even when optional UX tools are skipped.
Unresolved violations or missing evidence block completion; existing repair caps apply.
