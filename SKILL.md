---
name: designme
description: Premium anti-AI-slop design and motion studio. Invoke with /designme for high-craft web animation, launch films, showreels, interactive figures, procedural 3D object reconstructions, and deterministic HTML video. Combines Three.js, img2threejs, GSAP, Design DNA, motion principles, Genjutsu, HyperFrames, launch direction, beat sync, code-generated sound, frame review, Hairline, Remotion, motionmaxxing, an Opus 5.5 video-prompt researcher, a 20-style visual language library, UI/UX Pro Max design intelligence, Superlite execution, 14 UX laws, and Chromium + BrowserCode QA in one orchestrated command.
allowed-tools: Task, Read, Write, Edit, Bash, Glob, Grep
---

# /designme — The Anti-Slop Design Studio

Invoke: `/designme <brief>` — e.g. `/designme premium 9:16 launch reel, Linear + Stripe refs, heavy physical feel, no AI purple slop`

## What This Is

One command for brand-led, code-authored motion and interactive web visuals. HyperFrames remains the default video renderer, Remotion is an optional local React-video renderer, motionmaxxing is an optional measured-motion HTML film, Hairline is an optional interactive-figure engine, and img2threejs is an optional procedural image-to-3D reconstruction engine. Blotato and Remotion are also used as free prompt/reference sources for future projects. It adds only complementary production disciplines:

- **Design DNA + motion principles:** extract a visual system and a motion doctrine before code.
- **Direction:** develop competing creative directions, a one-claim story arc, camera language, and shot plan.
- **Visual language:** select one primary style and at most one supporting style, then turn it into a material, motion, camera, shader, proof, and anti-slop specification.
- **UI/UX intelligence:** use local UI/UX Pro Max search for interface styles, palettes, typography, UX rules, charts, icons, GSAP guidance, and stack-specific implementation.
- **Procedural 3D reconstruction:** when approved, `img2threejs-agent` rebuilds a 2D reference image of an object or character into a deterministic code-only `THREE.Group` factory (`create<ObjectName>Model`) for `threejs-agent`.
- **Beat sync:** make a shared beat/timeline table that drives visuals, transitions, captions, and audio cues.
- **Craft:** use GSAP for choreography, Three.js for hero 3D, and pure `render(t)` functions for seek-safe generative layers.
- **Sound:** write code-generated cues or wire approved audio against the same timeline, then master and verify it.
- **Review:** render stills/contact sheets at beats and inspect them before final MP4 rendering.
- **Motion skill packs:** route the approved iart-ai packs to the agents that need them; install only the smallest compatible set.
- **Optional capabilities:** discuss Remotion, Hairline, motionmaxxing, img2threejs, the Opus 5.5 video-prompt catalog, and motion-skill pack selection during grilling, recommend what is needed, and activate only the user-approved choices.
- **Opus prompt research:** when approved, `opus5-videos-agent` reads a few matching prompts from the MIT catalog, credits the creators, and rewrites the craft for this brand. It never renders and never replaces the video renderer.
- **Measured-motion film:** when approved, `motionmaxxing-agent` owns one brand-specific HTML film and must pass its G0–G5 gates locally. It never runs beside HyperFrames or Remotion, and it never calls ElevenLabs.
- **QA:** run anti-slop, determinism, readability, audio, accessibility, UX laws, and final-frame checks with live Chromium and BrowserCode verification and targeted feedback loops.

## Invocation Contract

Claude Code sees `/designme` because the skill folder is named `designme` and frontmatter name is `designme`. When the user types `/designme`, `designme`, or asks for premium animation that does not look AI-generated, load this skill.

## Mandatory Orchestration (DO NOT SKIP)

### 0 — Install Gate

Read the [Superlite execution adapter](references/superlite-integration.md).
Designme is the sole coordinator. Superlite replaces the Superpowers engineering
role; never enable both plugins together. The bundled adapter needs no plugin
installation or paid model routing.

Check whether the dependencies are installed. If not, install the selected skills:

```bash
npx skills add CloudAI-X/threejs-skills greensock/gsap-skills zanwei/design-dna LottieFiles/motion-design-skill https://genjutsu.athevon.dev heygen-com/hyperframes -g
npx skills add whaleyxbt/claude-motion AbubakrChan/product-launch-motion Sunwood-ai-labs/hyperframes-motion-reel-skill -g
npx skills add remotion-dev/skills -g  # official prompt/reference guidance; local Remotion only
npx skills add lucasmarkes/hairline -g  # optional interactive figures; free/local only
npx skills add Tejashmakwana/motionmaxxing -g  # optional measured-motion films; free/local only, no ElevenLabs
# Optional img2threejs procedural 3D reconstruction (canonical ~/.agents/skills/img2threejs)
# git clone https://github.com/img2threejs/img2threejs.git ~/.agents/skills/img2threejs
# Local BrowserCode + Chromium QA verification repo:
# git clone https://github.com/leaningtech/browsercode.git ~/.agents/tools/leaningtech-browsercode
# Optional UI/UX Pro Max local skill; MIT, bundled data + Python search, no paid APIs
# npm install -g ui-ux-pro-max-cli && uipro init --ai claude --global
# opus5-videos-agent clones yihui-dev/awesome-opus5-5-videos on approval. It is a prompt catalog, not an npx skill.
# Install only the approved iart-ai packs selected during grilling; see references/motion-skills-packs.md
npx skills add vercel-labs/agent-browser thedotmack/claude-mem -g
# Superlite adapter is bundled; optional native plugin: references/superlite-integration.md
npx skills add https://github.com/anthropics/skills --skill frontend-design --skill skill-creator --skill mcp-builder --skill webapp-testing -g
npx skills add vercel-labs/skills --skill find-skills -g
# taste is installed from Leonxlnx/taste-skill (folder taste-skill); gsd is not used here (no 'gsd' skill exists upstream)
```

Do not use Remotion as a second renderer for a HyperFrames composition. Activate `remotion-agent` only when the brief explicitly requires a React/Remotion deliverable, and record the renderer decision. Activate `hairline-agent` only when the brief explicitly requests Hairline or an interactive figure.

Do not use motionmaxxing as a second video renderer. Activate `motionmaxxing-agent` only when the brief explicitly requests its measured-motion HTML film (brand-from-URL launch, sting, kinetic type, social ad, or a slop-cut upgrade through its gates). When it owns the film, skip HyperFrames and Remotion. Exactly one video renderer runs. Read `references/motionmaxxing.md`.

Activate `opus5-videos-agent` only when the user wants a starting prompt from the Opus 5.5 video catalog. It runs in Wave 1, writes `opus-prompt-brief.md`, and is not a video renderer. Read `references/opus5-videos.md`. Activate `ui-ux-pro-max-agent` for UI-containing work when approved; skip it for pure non-UI films. It runs in Wave 2 and writes `uiux-design-system.md` and `uiux-audit.md`. Activate `img2threejs-agent` only when approved for a 2D reference object or character image that must be reconstructed into a procedural Three.js `THREE.Group` factory in code. It runs in Wave 2 and hands `create<ObjectName>Model` to `threejs-agent` in Wave 3. Read `references/img2threejs.md`.

## Free-Only Execution Policy

Use only free, local, open-source, or already-installed tools and APIs. Never call a paid API, paid tier, metered SaaS endpoint, premium model, paid voice service, paid asset service, or billing-enabled integration. Never create a subscription, start a trial, enter payment details, or consume credits. Do not ask the user for API keys for a paid service. If a requested capability requires payment or a paid API, stop that part, explain the limitation, and propose a free/local alternative such as Python, FFmpeg, Chromium, Playwright, system tools, or deterministic code-generated assets. motionmaxxing's optional ElevenLabs voice, SFX, and music path is a paid API and is forbidden. `img2threejs-agent` must use only local `generic` and `character` profiles and never call Tripo, Hyper3D, CharacterGen, or paid cloud plugins.

### 1 — The Griller (1 agent) — ALWAYS FIRST — BLOCKING

Spawn `planner-griller` with `references/grilling-questions.md`. It must cover goal, audience, references, anti-slop list, duration, aspect, resolution, story arc, audio/voice needs, stack, constraints, success metric, verification needs, the visual-style gate, the optional-agent gate, and motion-skill pack selection.

The griller must produce an explicit recommendation for every optional agent:

```json
{
  "optionalAgents": {
    "remotion-agent": {"requested": false, "needed": false, "reason": "HyperFrames is sufficient"},
    "hairline-agent": {"requested": false, "needed": false, "reason": "No interactive figure requested"},
    "motionmaxxing-agent": {"requested": false, "needed": false, "reason": "HyperFrames is sufficient"},
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
waits for the canonical beat map, and Wave 4 craft review waits for a renderer draft.

**Wave 1 (no dependencies):**

- `design-dna-agent` — extracts tokens from references.
- `memory-agent` — loads past taste and prior constraints.
- `find-skills-agent` — discovers only missing, compatible skills.
- `browser-agent` — captures reference screenshots with local Chromium (`~/Library/Caches/ms-playwright/chromium-1248/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing`).
- `prompt-reference-agent` — curates free prompt patterns from Blotato and Remotion for briefs and future projects.
- `opus5-videos-agent` — runs only if approved. Picks a few catalog prompts and writes `opus-prompt-brief.md` before direction. Otherwise mark skipped.
- `find-skills-agent` — routes approved iart-ai motion-skill packs to the owning agents and records local installs.

**Wave 2 (needs brief and Wave 1 context):**

- `visual-style-agent` — converts the selected visual style into a buildable style specification and sample recipe.
- `ui-ux-pro-max-agent` — runs only when approved for UI/UX work; creates a local searchable design system and UI audit.
- `img2threejs-agent` — runs only when approved for a 2D reference image; runs the staged sculpting pipeline (`blockout` to `optimization`) gated by `forge/state.py` and `forge/next.py` and outputs a deterministic `create<ObjectName>Model` `THREE.Group` factory.
- `motion-design-agent` — writes timing, easing, weight, and choreography doctrine.
- `launch-director-agent` — writes three visual directions, kills two, and creates the story/shot/camera/look plan.
- `superlite-agent` — writes the execution plan and tests.

**Wave 3 (needs Wave 2 outputs):**

- `beat-sync-agent` — creates the shared BPM/frame beat map, transition schedule, and audio cue plan.
- `gsap-agent` — implements the seekable choreography timeline. If motionmaxxing or Remotion owns the renderer, contribute doctrine and timing notes only; do not build a second HyperFrames timeline.
- `threejs-agent` — implements only the necessary hero 3D or generative layer, inside the approved renderer, and mounts `create<ObjectName>Model` when `img2threejs-agent` is active.
- `genjutsu-agent` — writes thesis and anti-slop MASTER.md.
- `taste-gsd-agent` — performs the aesthetic gate and execution critique.

**Wave 4 (needs all design and engineering outputs):**

- `hyperframes-agent` — assembles the deterministic HTML composition and renders drafts by default. Skip if Remotion or motionmaxxing owns the video renderer.
- `remotion-agent` — runs only if `brief.json.optionalAgents.remotion-agent.requested` is true or the user explicitly approved it; otherwise mark skipped. Do not run it if motionmaxxing owns the film.
- `motionmaxxing-agent` — runs only if `brief.json.optionalAgents.motionmaxxing-agent.requested` is true or the user explicitly approved it; otherwise mark skipped. When it runs, it owns the film and HyperFrames and Remotion are skipped.
- `hairline-agent` — runs only if `brief.json.optionalAgents.hairline-agent.requested` is true or the user explicitly approved it; otherwise mark skipped.
- `motion-craft-agent` — runs still/contact-sheet review, checks frame collisions and safe areas, wires code-generated or approved sound, and records fixes. If motionmaxxing owns the film, review `film/look-final/` and `film/NOTE.md` instead of a HyperFrames contact sheet.

Pass `brief.json`, the approved `motionSkillPacks`, and the relevant output paths to every agent. Never write animation code in the orchestrator; delegate it.

Run a fresh findings-only engineering review after integration and craft review;
route fixes to their owners and record evidence before the final QA gate.

### 3 — QA Anti-Slop Loop — ALWAYS LAST

Spawn `qa-anti-slop-agent` after composition and craft review. It reads `references/qa-rubric.md`, `references/browsercode-chromium-qa.md`, and `references/missing-checklist.md`. It boots the rendered output in local Chromium (`~/Library/Caches/ms-playwright/chromium-1248/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing`) and checks `leaningtech/browsercode` (`~/.agents/tools/leaningtech-browsercode`) preview compliance to verify that the visual output matches the approved design and that every agent followed `plan.md`.

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

Compare two final renders by hash. If voice or music is present, verify captions, peak timing, loudness, and no drift. If Hairline is selected, include its browser/look validation in the QA evidence. If UI/UX Pro Max is selected, include `uiux-design-system.md`, `uiux-audit.md`, local search queries, responsive/keyboard/focus evidence, and reduced-motion checks. If `img2threejs-agent` is selected, include `.img2threejs/state.json`, `sculpt-spec.json`, `img2threejs-passes/`, and `img2threejs-report.md` in the QA evidence. If motionmaxxing is selected, `film/NOTE.md` must quote G0–G5 and a fail is not a pass. If the Opus catalog was selected, `opus-prompt-brief.md` must credit its sources and the film must not be a shot-for-shot clone.

## Output Contract

- `/hyperframes/output/final.mp4` when HyperFrames is the renderer
- `/hyperframes/composition/` with `index.html`, `style.css`, `script.js`, `tokens.css`, and assets, when HyperFrames is the renderer
- `film/index.html`, `film/STORYBOARD.md`, `film/NOTE.md`, `film/final.mp4`, and `film/look-final/` when motionmaxxing owns the film
- `renderer-decision.md` when the video renderer is not HyperFrames
- `UX_LAWS_AUDIT.md` with all 14 laws, evidence, fixes and re-audit results
- `brief.json`, `design-dna.json`, `style-spec.md`, `uiux-design-system.md` when applicable, `uiux-audit.md` when applicable, `sculpt-spec.json` and `img2threejs-report.md` when applicable, `motion-doctrine.md`, `directions.md`, `shot-plan.md`
- `timeline.json` or `beat-map.json`, `audio-cues.md`, and `audio_meta.json` when applicable
- `thesis.md`, `plan.md`, `browser-report.md`, `prompt-reference.md`, `opus-prompt-brief.md` when applicable, `brief-enhancements.md`, `motion-skills-installed.md`, `hairline-design.md` when applicable, `hairline-validation.md` when applicable, `contact-sheet.png`, and `audit.md`

No generic gradients, default purple-on-black SaaS styling, unmotivated bounce, or code-first production. The selected visual style must be an intentional system, not a list of effects. Every visual and sound cue must have an intentional role in the approved thesis.

## Mandatory UX laws

Before planning or building, read the complete [UX laws reference](references/ux-laws.md)
and [its workflow](references/ux-laws-workflow.md). Map all 14 laws in the plan and
include the relevant checks in every specialist handoff. After every build or
significant change, complete `UX_LAWS_AUDIT.md`, fix findings and re-audit before
completion. The audit is mandatory even when optional UX tools are skipped.
Unresolved violations or missing evidence block completion; existing repair caps apply.
