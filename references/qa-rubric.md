# QA Rubric — Anti-Slop

## Direction and Story
- [ ] One approved direction is documented; two alternatives were killed with reasons
- [ ] One claim and one emotional thesis are visible in the shot plan
- [ ] First three seconds contain a hook
- [ ] Every shot has a purpose and every camera move is motivated

## Design DNA
- [ ] Palette extracted, max 5 colors, not #8b5cf6 generic purple
- [ ] Typography specific (e.g., "Suisse Int'l 500 for headings" not "modern sans")
- [ ] tokens.css actually used in composition

## Motion Design (LottieFiles)
- [ ] Duration scale defined and respected
- [ ] Easing chosen with intent, not default ease-out
- [ ] Choreography: stagger 40-120ms, overlap not all at once
- [ ] Disney: anticipation, follow-through, weight
- [ ] Holds are readable and the hook is not delayed by empty frames

## GSAP and Three.js
- [ ] When GSAP is used: useGSAP with cleanup or gsap.context()
- [ ] Timeline used, not scattered tweens
- [ ] Only transform/opacity for ordinary UI motion
- [ ] When ScrollTrigger is used: anticipatePin, scrub 0.5-1.5, no markers in prod
- [ ] 3D assets are disposed and seeded layers are repeatable

## Beat and Timeline Contract
- [ ] One canonical timeline drives picture, captions, sound, and review timestamps
- [ ] BPM cuts and impacts land on the declared beat map
- [ ] Voice reveals use real word timings when voice exists
- [ ] Key visual lands on the drop or strongest narrative word

## Frame Craft
- [ ] Contact sheet includes every scene peak and sync-check timestamp
- [ ] No clipping, collisions, unsafe margins, accidental flash, or pop frame
- [ ] Camera actually moves with intent; no perpetual drift
- [ ] Product/UI copy and facts are approved and readable

## Audio
- [ ] 48kHz, no drift, and cues share the visual timeline
- [ ] Voice/music/SFX are individually audible and not masked
- [ ] True peak below -2 dBFS and loudness approximately -14 LUFS unless brief overrides
- [ ] Captions match voice timing and remain readable

## Genjutsu Anti-Slop List (MUST AVOID)
- Generic aurora / mesh gradient background
- Cards floating with y:-10 infinite yoyo
- Everything bouncy with elastic.out
- Inter font by default
- 2s fade-in for everything
- Purple on black "AI SaaS" look
- No thesis, code first

## HyperFrames
- [ ] No Math.random(), Date.now(), timers, or window.scrollY
- [ ] Timeline seekable: hf.onSeek(t) => timeline.seek(t)
- [ ] Pure render(t) layers are seeded and repeatable
- [ ] Captions overlay if voice
- [ ] Deterministic render tested: 2 renders identical hash
- [ ] ffprobe confirms expected FPS, dimensions, duration, and audio stream

## motionmaxxing (only if it owns the film)
- [ ] It is the only video renderer; HyperFrames and Remotion were skipped
- [ ] `renderer-decision.md` records why
- [ ] `film/NOTE.md` quotes G0–G5 from `look.py` and `lint.mjs`, not a self-grade
- [ ] G1 and G4 were judged from the contact sheet
- [ ] No page chrome, deck layout, flat swatch ground, or void card
- [ ] The idea fails a competitor-logo swap
- [ ] No ElevenLabs or other paid voice/music API; audio is local or user-provided
- [ ] Two local renders match by hash and ffprobe matches the plan

## Opus 5.5 prompts (only if that agent ran)
- [ ] `opus-prompt-brief.md` cites 1–3 catalog entries with author and original post
- [ ] The brief says what craft was kept and what was rejected
- [ ] No paid generator, voice, or asset API from a source prompt was called
- [ ] The film is not a shot-for-shot copy of the reference
- [ ] The catalog was not vendored into the project

## img2threejs procedural 3D reconstruction (only if that agent ran)
- [ ] `.img2threejs/state.json` shows all passes completed in order (`blockout` to `optimization`)
- [ ] `sculpt-spec.json` defines a complete `detailInventory` and `qualityContract`
- [ ] `img2threejs-passes/` holds per-pass Chromium screenshots compared against the reference image
- [ ] `create<ObjectName>Model` uses deterministic noise seeds and named pivots/sockets
- [ ] No paid or external neural mesh generator (Tripo, Hyper3D, CharacterGen) was called

## Chromium and BrowserCode Live Inspection
- [ ] Output rendered and inspected in local Chromium (`~/Library/Caches/ms-playwright/chromium-1248/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing` with `--no-sandbox`)
- [ ] BrowserCode sandbox compatibility (`~/.agents/tools/leaningtech-browsercode`) checked where applicable
- [ ] Live render verified against `brief.json`, `design-dna.json`, `style-spec.md`, and `shot-plan.md` ("Did it make the right design?")
- [ ] Workspace artifacts verified against `plan.md` and `orchestrator.json` ("Did every agent follow the plan?")

## Mandatory UX laws (all outputs)

- [ ] Read the complete [UX laws reference](ux-laws.md) and [workflow](ux-laws-workflow.md)
- [ ] `UX_LAWS_AUDIT.md` covers every law with status and concrete evidence
- [ ] No Violated rows remain; justified Partial rows have scope, reason and impact
- [ ] Missing evidence blocks PASS; applicable UI laws are not skipped with optional agents
- [ ] Fix owners, re-audit results and remaining limitations appear in `audit.md`

## Anime.js and animated-word builds

- [ ] Research cites build-fit sources, distinguishes observed motion from inference, and identifies selected reference IDs
- [ ] `animation-plan.json` assigns non-overlapping target/property ownership; implementation matches it
- [ ] Anime.js uses the selected pinned v4 API and component-scoped selectors; GSAP checks apply only where GSAP is used
- [ ] Actual desktop/mobile evidence covers font-loaded wrapping, no-JS/first-paint readability, accessible text and keyboard/CTA access
- [ ] Reduced-motion initial state and preference changes expose full readable content without decorative loops
- [ ] Unmount/replay cleanup restores DOM and removes timelines, observers and listeners
- [ ] When rendered as video, paused Anime.js seeking uses canonical milliseconds and remains repeatable on backward/forward seeks
- [ ] `animejs-validation.md` records actual execution evidence or BLOCKED limitations

## Open 3D (when enabled)

- [ ] `open-3d-plan.md` and approved brief agree on selected upstream skills and allowed local/supplied assets
- [ ] Each scene has one owner, Three.js version, renderer/camera/clock and lifecycle; Anime.js/GSAP have non-overlapping properties
- [ ] Actual integrated browser reports/contact sheets cover desktop/mobile, scroll extremes, alpha playback/cursor states where applicable, loading and reduced motion
- [ ] Frame time, draw calls, geometry/media size meet declared target-device budgets; resources/listeners are disposed on unmount
- [ ] `open-3d-validation.md` records measured evidence and limitations; unavailable required checks are BLOCKED
- [ ] Final capture respects the selected renderer; no paid motion-assets generation was invoked
- [ ] Findings identify the actual owner and are repaired/rechecked within the existing three-loop cap

- [ ] Open 3D capability matrix covers all eight upstream skills with concrete use/skip/blocked reasons
- [ ] Every used skill has task mapping, outputs and actual passing evidence; required blocked or pending rows prevent PASS
- [ ] Asset planning, consistent style, provenance and reproducibility logs exist when assets are involved
- [ ] Enabled animated/3D web builds have Chromium/WebKit site-check evidence at desktop/tablet/phone sizes; motion-only behaviors have targeted capture evidence
