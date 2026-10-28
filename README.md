# /designme — invoke with /designme

One skill that spawns a griller/planner, a visual-style director, parallel creative and engineering agents, an optional procedural 3D reconstruction agent (`img2threejs-agent`), a direction pass, a beat-sync pass, a motion-craft review, and a final anti-slop QA loop with live Chromium and BrowserCode verification.

> **Scope:** HyperFrames is the default renderer. The local `remotion-agent` is optional and runs only when a project explicitly requests React/Remotion. `motionmaxxing-agent` is optional and runs only when a project explicitly requests a measured-motion HTML film from [Tejashmakwana/motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing). `hairline-agent` is optional and runs only for interactive figures or pointer-responsive web visuals. `img2threejs-agent` is optional and runs only when a project provides a 2D reference image to reconstruct as a procedural Three.js `THREE.Group` model in code from [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs). Blotato and Remotion references are used for prompt patterns only. All agents follow a free-only policy with no paid APIs, cloud rendering, publishing, scheduling, or credits. `opus5-videos-agent` is optional and only researches prompts from [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos). motionmaxxing must not call ElevenLabs. `qa-anti-slop-agent` inspects live output in local Chromium (`chromium-1248`) and [leaningtech/browsercode](https://github.com/leaningtech/browsercode).

## Invoke

```text
/designme premium 9:16 launch reel, Linear + Stripe refs, heavy physical feel, no AI purple slop
```

## Optional-agent grilling gate

During the first grilling session, `planner-griller` must select a visual language from the 20-style library, then recommend whether each optional agent and iart-ai motion-skill pack is needed and ask for approval:

| Optional agent | Use it when | Default recommendation |
|---|---|---|
| `remotion-agent` | The brief explicitly requires a React/Remotion video deliverable or Remotion-specific composition | Skip it and use HyperFrames |
| `hairline-agent` | The brief requires an interactive line figure, pointer-responsive diagram, technical illustration, or self-contained Hairline visual | Skip it unless the interaction needs it |
| `motionmaxxing-agent` | The brief explicitly requires a motionmaxxing film: brand-from-URL launch, sting, kinetic type, social ad, or a slop-cut upgrade through its G0–G5 gates | Skip it and use HyperFrames. Never run it beside another video renderer |
| `opus5-videos-agent` | The brief explicitly wants a starting prompt from the Opus 5.5 code-video catalog | Skip it. It researches prompts only and does not render |
| `ui-ux-pro-max-agent` | UI, landing page, dashboard, product demo, forms, navigation, charts, mobile UI, or UX/accessibility review | Skip it for pure non-UI films |
| `img2threejs-agent` | The brief supplies a 2D reference image of an object, product, prop, or character and requires a procedural code-only Three.js `THREE.Group` reconstruction | Skip it when no custom 3D reconstruction from a reference photo is needed |

The recommendation is stored in `brief.json.optionalAgents`. Optional agents are never silently activated. A user request can approve an agent even when it is not strictly necessary, with the tradeoff recorded. Exactly one video renderer runs: HyperFrames, Remotion, or motionmaxxing.

## Procedural 3D reconstruction (`img2threejs-agent`)

`img2threejs-agent` adds [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) (Apache-2.0, v2.0.0) as an optional Wave 2 agent. It gates reconstruction through `forge/state.py` and `forge/next.py` across 8 passes (`blockout` to `optimization`), verifies each pass in local Chromium, and hands a deterministic `create<ObjectName>Model(spec, options)` `THREE.Group` factory to `threejs-agent` in Wave 3.

See [`references/img2threejs.md`](references/img2threejs.md).

## Chromium and BrowserCode QA verification

`qa-anti-slop-agent` and `browser-agent` verify live rendered output using local Chromium (`~/Library/Caches/ms-playwright/chromium-1248/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing`) and [leaningtech/browsercode](https://github.com/leaningtech/browsercode) (`~/.agents/tools/leaningtech-browsercode`) to check that the rendered output matches the approved design and that every scheduled agent followed `plan.md` and `orchestrator.json`.

See [`references/browsercode-chromium-qa.md`](references/browsercode-chromium-qa.md).

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
- `Tejashmakwana/motionmaxxing` → `motionmaxxing-agent`: optional measured-motion HTML film. Brand-owned idea, world, seek-safe runtime, local Chrome/ffmpeg render, and G0–G5 gates. See [`references/motionmaxxing.md`](references/motionmaxxing.md).
- `yihui-dev/awesome-opus5-5-videos` → `opus5-videos-agent`: optional MIT prompt catalog. Picks a few code-authored video prompts, credits the creators, and rewrites the craft for this brand. See [`references/opus5-videos.md`](references/opus5-videos.md).
- `img2threejs/img2threejs` → `img2threejs-agent`: optional Apache-2.0 procedural image-to-Three.js reconstruction agent. See [`references/img2threejs.md`](references/img2threejs.md).
- `leaningtech/browsercode` + local Chromium → `qa-anti-slop-agent` and `browser-agent`: live Chromium and BrowserCode verification of design fidelity and plan execution. See [`references/browsercode-chromium-qa.md`](references/browsercode-chromium-qa.md).

## Free-only rule

All 24 agents are restricted to free, local, open-source, or already-installed tooling. They must not call paid APIs, paid tiers, metered SaaS, premium models, paid voice or asset services, subscriptions, trials, billing, or credit-consuming services. If a capability is not available for free, the agent must stop that part and offer a local or deterministic alternative. The motionmaxxing skill's ElevenLabs voice path is off, and `img2threejs-agent` paid/external neural mesh adapters are off.

## Structure

- `SKILL.md` — `/designme` contract, install gate, dependency waves, optional-agent gate, and output contract
- `agents/` — creative direction, motion engineering, visual-style direction, UI/UX Pro Max intelligence, optional Remotion/Hairline/motionmaxxing/Opus-prompt/img2threejs agents, craft review, and QA agents
- `references/` — grilling questions, prompt sources, iart motion-pack routing, motionmaxxing contract, Opus 5.5 prompt catalog, img2threejs integration, BrowserCode + Chromium QA verification, visual-style library, UI/UX Pro Max integration, Superlite adapter, UX laws, QA rubric, asset pipeline, missing checklist, and orchestration state
- `manifest.json` — selected source repositories and agent responsibilities

## Install

```bash
npx skills add CloudAI-X/threejs-skills greensock/gsap-skills zanwei/design-dna LottieFiles/motion-design-skill https://genjutsu.athevon.dev heygen-com/hyperframes -g
npx skills add whaleyxbt/claude-motion AbubakrChan/product-launch-motion Sunwood-ai-labs/hyperframes-motion-reel-skill -g
npx skills add remotion-dev/skills lucasmarkes/hairline Tejashmakwana/motionmaxxing -g
git clone https://github.com/img2threejs/img2threejs.git ~/.agents/skills/img2threejs
git clone https://github.com/leaningtech/browsercode.git ~/.agents/tools/leaningtech-browsercode
# Optional UI/UX Pro Max local skill (MIT, bundled data + Python search)
npm install -g ui-ux-pro-max-cli && uipro init --ai claude --global
# Opus prompt catalog is cloned by opus5-videos-agent when approved; see references/opus5-videos.md
# Add only the iart-ai packs approved during grilling; see references/motion-skills-packs.md
npx skills add vercel-labs/agent-browser thedotmack/claude-mem -g
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
