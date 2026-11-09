---
name: designme
description: Premium anti-AI-slop design and motion studio. Invoke with /designme for high-craft web animation, launch films, showreels, interactive figures, procedural 3D object reconstructions, and deterministic HTML video. Combines goal-led multilayer parallax backgrounds, Three.js, Open 3D Skills, img2threejs, GSAP, Anime.js, Design DNA, motion principles, Genjutsu, HyperFrames, launch direction, beat sync, code-generated sound, frame review, Hairline, Remotion, motionmaxxing, an Opus 5.5 video-prompt researcher, a 20-style visual language library, UI/UX Pro Max design intelligence, Superlite execution, 14 UX laws, Agent Desktop + render QA, mandatory motion accessibility/performance gates, and last-after-QA versioned /buildme handoffs across 31 agents with a strict Speckit theme/design lock gate.
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
- **Quality and handoff:** motion-a11y verifies every reduced variant; render-perf-budget proves fallback, Web Vitals and payloads; final QA checks the exact integrated revision through Agent Desktop and local measurements; token-handoff-exporter runs last to create versioned /buildme-ready artifacts.

## Invocation Contract

Claude Code sees `/designme` because the skill folder is named `designme` and frontmatter name is `designme`. When the user types `/designme`, `designme`, or asks for premium animation that does not look AI-generated, load this skill.

## Mandatory Orchestration (DO NOT SKIP)

Every invocation dispatches every core agent and workflow stage this file defines, through the Agent tool, in the waves it specifies. Do not decide on your own that an agent, stage, or review is unnecessary. Each one ends with its output file or a BLOCKED entry naming the missing dependency and its fix. Optional agents (Hairline, Opus prompt research, img2threejs) are resolved by asking the user during grilling, never by assumption. "Skip" is allowed only where this file says a stage owns nothing or is web-only, and it must be recorded with the reason.

### 0 — Install Gate

Read the [Superlite execution adapter](references/superlite-integration.md).
Designme is the sole coordinator. Superlite replaces the Superpowers engineering
role; never enable both plugins together. The bundled adapter needs no plugin
installation or paid model routing.

Check for Anime.js first: if `~/.agents/tools/animejs` (or `$DESIGNME_ANIMEJS_REPO_DIR`) is already a Git checkout of `juliangarnier/anime` and `git -C <dir> rev-parse --verify HEAD` succeeds, it is installed — do not download or install it again. Only when it is missing, run `bash scripts/install-animejs.sh` from this skill directory to download it, including for static or non-Anime.js builds. Do not mark installation complete if the download/verification fails. Record its path and commit in `motion-skills-installed.md`. Then check whether the remaining dependencies are installed and install the selected skills:

```bash
# Anime.js: skip when ~/.agents/tools/animejs is already a verified checkout.
# Only if missing, run from the designme repository root:
[ -d ~/.agents/tools/animejs/.git ] || bash scripts/install-animejs.sh
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
# Superlite adapter is bundled; optional native plugin: references/superlite-integration.md
npx skills add https://github.com/anthropics/skills --skill frontend-design --skill skill-creator --skill mcp-builder --skill webapp-testing -g
npx skills add vercel-labs/skills --skill find-skills -g
# taste is installed from Leonxlnx/taste-skill (folder taste-skill); gsd is not used here (no 'gsd' skill exists upstream)
```

Read [normal motion orchestration](references/normal-motion-orchestration.md). Remotion, motionmaxxing and Open 3D are normal specialists assessed and dispatched when relevant without separate opt-in gates. HyperFrames owns final film assembly by default; Remotion/Open 3D may render assigned intermediate assets. motionmaxxing normally plans and reviews in contribution mode. One final owner per deliverable, with explicit standalone renderer overrides. Hairline retains its existing optional-agent gate.

Activate `opus5-videos-agent` only when the user wants a starting prompt from the Opus 5.5 video catalog. It runs as an approved Wave 2 research prerequisite, writes `opus-prompt-brief.md`, and is not a video renderer. Read `references/opus5-videos.md`. Activate `ui-ux-pro-max-agent` for UI-containing work when approved; skip it for pure non-UI films. It runs in Wave 2 and writes `uiux-design-system.md` and `uiux-audit.md`. Activate `img2threejs-agent` only when approved for a 2D reference object or character image that must be reconstructed into a procedural Three.js `THREE.Group` factory in code. It runs in Wave 2 and hands `create<ObjectName>Model` to `threejs-agent` in Wave 3. Read `references/img2threejs.md`.

## Free-Only Execution Policy

Use only free, local, open-source, or already-installed tools and APIs. Never call a paid API, paid tier, metered SaaS endpoint, premium model, paid voice service, paid asset service, or billing-enabled integration. Never create a subscription, start a trial, enter payment details, or consume credits. Do not ask the user for API keys for a paid service. If a requested capability requires payment or a paid API, stop that part, explain the limitation, and propose a free/local alternative such as Python, FFmpeg, Chromium, Playwright, system tools, or deterministic code-generated assets. motionmaxxing's optional ElevenLabs voice, SFX, and music path is a paid API and is forbidden. `img2threejs-agent` must use only local `generic` and `character` profiles and never call Tripo, Hyper3D, CharacterGen, or paid cloud plugins.

## Animation engine routing

Read [Anime.js integration](references/animejs-integration.md). Prefer `animejs-agent` for animated landing pages, words, SVG accents, and ordinary elements. The existing `prompt-reference-agent` researches build-specific animated-word references before design planning. Record `brief.json.animation` and coordinator-owned `animation-plan.json`; assign each target/property to one engine before implementation. Honor static briefs and explicit stack choices. Anime.js is not a renderer; web-only builds do not require a video render.

## Open 3D specialist routing

For an explicitly requested recording of a web-only build, the coordinator may select `frame-capture` as the sole capture backend under the integration contract below; skip all film renderers and record `renderer-decision.md`. This is the only Open 3D exception to the film-renderer list.

Read [Open 3D integration](references/open-3d-integration.md). For relevant 3D/scroll/interactive builds, record `brief.json.open3d` and selected skills. Make all eight upstream skills available, assess each in `open-3d-capabilities.json`, and execute every relevant capability through evidence-backed verification. `open-3d-agent` plans in Wave 2, implements assigned modules in Wave 3, validates the integrated draft in Wave 4, and receives targeted QA repairs within the existing three-loop cap. Skip unrelated work with a recorded reason. Freeze ownership alongside Three.js, Anime.js and GSAP; retain the free-only policy.

## Goal-led animated backgrounds

Read [parallax background orchestration](references/parallax-background-integration.md). `parallax-background-agent` is a normal specialist, automatically active for requested 3D/multilayer/parallax animated backgrounds. It selects techniques from website type, primary goal and actually inspected reference images, assesses all six providers, builds assigned layers, and participates in integrated QA/repairs. Use the verified `nexu-io/html-video` provider through `references/html-video-integration.md`; inspect actual engine/runtime availability and preserve frame-accuracy and free-only requirements.

### Wave 1 — planner-griller — ALWAYS FIRST — BLOCKING

Spawn `planner-griller` with `references/grilling-questions.md` and [the 20 product-design principles](references/product-design-principles.md). Capture every DP01–DP20 applicability/source/decision/acceptance record in `brief.json.designPrinciples` and resolve missing product-specific choices; the principles themselves are already supplied requirements. It must cover goal, audience, references, anti-slop list, duration, aspect, resolution, story arc, audio/voice needs, stack, constraints, success metric, verification needs, the visual-style gate, the optional-agent gate, and motion-skill pack selection.

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

### Wave 1.5 — speckit-theme-builder → speckit-theme-reviewer

After the approved planner brief, run `speckit-theme-builder` ([contract](agents/speckit-theme-builder.md)), then `speckit-theme-reviewer` ([contract](agents/speckit-theme-reviewer.md)). This is mandatory theme/design specification work, **not backend/database/business implementation**. It runs before Wave 2, using the approved grill/previous spec, a real repo scan, actual screenshots and moodboard; it must not depend on unfinished downstream design-agent outputs.

The builder must turn DP01–DP20 into concrete audit/rules/specification/implementation/task acceptance across all five Markdown files under `references/product-design-principles.md`; the reviewer checks the full source/spec/task mapping. Do not treat a pasted list as applied design.

The builder produces the generated project's `/speckit-theme-design/project_context.md`, `constitution.md`, `spec.md`, `plan.md`, `tasks.md` and lock checklist with one version/brief/source identity. The files cover evidence/locked direction, non-negotiable constitution, complete token/section/component/state/motion/responsive design, implementation phases A–E and exactly T001–T018 / US-1–US-4. A missing decision is a concrete OPEN QUESTION in **unlocked** project_context.md and an immediate STOP, never a guessed default or a placeholder in a falsely locked file.

The reviewer is read-only with respect to the five files. It writes `speckit-review.md` with PASS/FAIL per file/check and exact file/line fixes; only an all-pass baseline receives **PASS to Wave 2**. Version/hash-match all inputs and reviewed files. No implementation or Wave 2 design dispatch occurs before the gate resolves.

**Maximum two reviewer attempts total:** attempt 1 FAIL → builder repairs only its owned spec files from the issue table → attempt 2 review. On the second FAIL, pause and ask the user **“Fix brief or approve with risk?”**, showing the remaining issues. Do not run a third attempt or assume approval. A brief fix starts a newly versioned cycle; explicit risk acceptance records exact issue IDs, consequences and baseline hashes, keeps the review FAIL and never fabricates missing values. Only an executable scoped user authorization can permit downstream work; unanswered values still require an answer or revised scope. Existing accessibility/performance/final-QA gates are not waived.

T001–T018 are documented future implementation tasks, not work to execute in this wave. T016 includes final QA PASS, T017 is final token/motion export, and T018 is that same exporter's own package verification/version/hash lock. No extra build/review agent follows a successful export. Any behavior-changing defect returns to the affected build/gates and restarts export last.

### Wave 2 — design-dna, motion-design

The four-wave order plus Wave 1.5 lock/review gate in this SKILL.md is authoritative for scheduling. Existing agent files remain unchanged; older wave labels in provider/reference instructions describe dependencies to map into this order, not permission to reorder these gates. Dispatch all core roles as required above, retaining existing optional-agent approvals and supporting specialist responsibilities. Use real host delegation limits and dependency tasks, not blanket parallel dispatch.

- `design-dna-agent` extracts/materializes the reviewed locked reference-based design system and tokens. Use `/speckit-theme-design/` as the approved baseline; do not silently replace its values.
- `motion-design-agent` consumes the reviewed Speckit baseline plus Design DNA/research and materializes its specified timing, easing, weight, choreography and normal/reduced intent; do not finalize the doctrine before the reference/token inputs exist.

Supporting tasks retained in this wave: `find-skills-agent`, `browser-agent`, `prompt-reference-agent`, approved `opus5-videos-agent`, `visual-style-agent`, approved `ui-ux-pro-max-agent`, `launch-director-agent`, `superlite-agent`, and planning contributions from `parallax-background-agent`, `open-3d-agent`, `remotion-agent` and `motionmaxxing-agent`. Finish prerequisite reference inspection before dependent design extraction. When approved, `img2threejs-agent` reconstructs the specified object only after background/model requirements exist; return its gated factory before scene implementation.

Reviewed Speckit files are downstream constraints, not suggestions. New or contradictory design choices return to the builder/reviewer gate with updated input/version rather than being invented by plan/tasks/implementation. The root execution `plan.md` is distinct from `/speckit-theme-design/plan.md`.

The coordinator freezes `plan.md`, `animation-plan.json`, `production-plan.json`, animation IDs and file/scene/property ownership after planning. Record provisional performance/payload budgets, first-paint/poster and CSR/SSR constraints, token-contract source and reduced mappings so the new gates have explicit acceptance criteria. Preserve an approved planner thesis before code; do not defer all creative intent until the final Genjutsu pass.

### Wave 3 — gsap, threejs, hyperframes, motion-a11y

- `gsap-agent` builds assigned seekable choreography under the existing engine/property ownership map. It retains the allowed owns-nothing handling when Anime.js owns all targets.
- `threejs-agent` builds assigned hero/scene/model work with one scene/camera/clock owner, consuming verified img2threejs factories where applicable.
- `hyperframes-agent` integrates verified supporting clips, local sequences and layers into the final-film draft by default. Build the draft only after its producer dependencies; for web-only work retain the functional website and record the existing no-final-film exception. Explicit alternative final owners remain supported.
- `motion-a11y-agent` ([contract](agents/motion-a11y-agent.md)) creates a reduced-motion variant for every animation, writes `gsap-timeline-reduced.js`, checks temporal WCAG AA contrast, flash frequency, keyboard/focus, modal exit/restore, live regions and decorative semantics, then writes `motion-a11y.md` with PASS/FAIL evidence. It can plan beside owners but must inspect the integrated draft before Wave 4. Missing variants, more than 3 flashes/second or lost focus fail the gate.

Supporting tasks retained here: `beat-sync-agent` finishes canonical video timing before producers; `animejs-agent` builds assigned text/UI; `parallax-background-agent` and `open-3d-agent` implement their owned layers/scene/media; `remotion-agent` supplies assigned clips/sequences; approved `hairline-agent` builds its figure. A capture of a website waits for page integration, then completes before its consuming film assembly. No duplicate final films or competing animation properties.

Genjutsu's existing thesis-before-render prerequisite is satisfied by the approved planner thesis handed into implementation; Wave 4 is its refinement/anti-slop review on the integrated result. Drafts do not constitute final approval. Do not rename or rewrite existing specialist agents to implement this schedule.

### Wave 4 — genjutsu thesis, render-perf-budget, qa-anti-slop, token-handoff-exporter

These core gates run in this **serial order**:

1. `genjutsu-agent` refines and checks the approved interaction thesis against the integrated work; writes `thesis.md`, `slop-blacklist.md` and `MASTER.md` when applicable. Return creative defects to the actual owner before acceptance.
2. `render-perf-budget-agent` ([contract](agents/render-perf-budget-agent.md)) proves rendering/first paint, fallback and real JS/GLB/Lottie payloads in `perf-budget.json` and `perf-report.md`. Record CSR/SSR impact, LCP < 2.5s, CLS < 0.1 and INP < 200ms with honest estimate/measurement provenance. No fallback, missing bundle numbers or an exceeded budget without cuts fails; unresolved over-budget work still cannot PASS just because it has a cut plan.
3. `qa-anti-slop-agent` performs the final integrated gate and issues PASS only on the exact tested revision after motion-a11y and performance PASS. Consume both new reports, reduced source, existing UX_LAWS_AUDIT.md, specialist artifacts, actual Agent Desktop UI checks and separate local render/measurement evidence under `references/agent-desktop-integration.md`. Missing required execution is BLOCKED, not a claimed PASS.
4. `token-handoff-exporter` ([contract](agents/token-handoff-exporter.md)) runs **LAST and only after final QA PASS**. Export versioned import-ready `/handoff/` tokens, motion specification, normal/reduced timeline, resize/dispose scene module and target-aware /buildme instructions plus validation manifest/import helper. Every required file, actual consumer token naming, dependency and version must validate; otherwise fail export. Do not start another build/review agent after a successful export.

Before gate 2, retain integrated `motionmaxxing-agent` review, `motion-craft-agent` frame/audio checks, `taste-gsd-agent` aesthetic critique, resumed background/Open 3D/browser validation, and a fresh findings-only engineering review. Route all source changes to their existing owners. Repeat the affected accessibility/performance/visual checks after each repair; a later source change invalidates earlier gate evidence.

Every existing specialist keeps its file contract and actual implementation/validation responsibilities. Only the coordinator writes shared state and entry points. Pass `brief.json`, approved packs, canonical timing, production/animation ownership and relevant paths to each task. Normal role no-work cases and approved optional skips remain recorded under their existing rules; the new accessibility/performance/export gates may never silently disappear.

### Gate repair loop and final handoff

Re-spawn only the responsible owner for FAIL/SLOP findings and rerun affected producer/consumer checks within the existing maximum of three repair loops. The coordinator tracks evidence/revision and unresolved blockers in `audit.md`. Final QA PASS is required before the exporter starts; it is the last review gate, not the last agent. Never export or publish an incomplete handoff as valid.

For video deliverables, final render, contact-sheet/audio/determinism and ffprobe checks below must finish as part of QA evidence before export. If a final render or export adapter reveals a defect or modifies behavior, invalidate the affected PASS, repair and rerun the necessary gates, then restart the exporter last. Websites retain actual mobile/desktop/interaction evidence rather than fabricated video artifacts.

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

- `/speckit-theme-design/project_context.md`, `constitution.md`, `spec.md`, `plan.md`, `tasks.md`, versioned lock checklist and `speckit-review.md`; all-pass reviewed baseline or a recorded user risk decision that never supplies invented/missing values


- `motion-a11y.md` with PASS/FAIL per check and `gsap-timeline-reduced.js`
- `perf-budget.json` with lcp_estimate, cls_estimate, total_js_kb, glb_kb, lottie_kb and fallback_file (plus INP, units, budgets and evidence); `perf-report.md` PASS/FAIL
- `/handoff/tokens.json`, `/handoff/motion-spec.json`, `/handoff/gsap-timeline.js`, `/handoff/gsap-timeline-reduced.js`, `/handoff/threejs-scene.js`, `/handoff/handoff.md`, version/QA-hash manifest, target-aware import helper and referenced assets; immutable versioned releases, only after final QA PASS


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
