# Normal motion orchestration

Remotion, motionmaxxing, Open 3D and parallax-background-agent are normal specialists, not optional-agent toggles. Assess all four for every build, dispatch applicable planning/build/review tasks without a separate approval gate, and record a concrete reason for no-work decisions. Do not produce an unnecessary clip or 3D effect merely to exercise a tool. Existing brief approval and unrelated optional-agent gates remain in place.

## Delivery and ownership

- **Video:** HyperFrames owns final assembly/render by default. Remotion and Open 3D frame-capture may produce assigned source clips consumed by that composition; these are asset producers, not competing final renders. motionmaxxing contributes craft guidance and reviews the integrated draft in contribution mode.
- **Website:** ship the live website with `finalRenderer: null`; do not substitute a film for a website. Open 3D owns assigned scene/media modules and Anime.js owns assigned text/UI properties. Remotion may produce useful supporting clips or advise on frame-based sequences. motionmaxxing advises on motion/depth and reviews actual interactions.
- **Website plus video:** retain the website and record assigned scene/scroll sequences through Open 3D; HyperFrames assembles the final video when a film is requested. An explicitly requested raw website recording can name frame-capture as its sole final capture backend. Record this exception in `renderer-decision.md`.
- Explicit standalone Remotion/motionmaxxing deliverables remain supported by setting `finalRenderer` accordingly, not by enabling optional agents. Their contribution modes still participate normally. One final owner per deliverable, any number of assigned intermediate assets.

The coordinator writes `production-plan.json` after specialist planning, before implementation. The brief contains `production` with `deliverable` (`website`, `video`, or `website-and-video`), `profile` (`standard` or `3d-parallax`), `finalRenderer`, and a `specialists` object for remotion-agent, motionmaxxing-agent, open-3d-agent and parallax-background-agent, each with `mode` and `reason`. Modes are `contribute`, `review`, `final`, or `no-work`; final applies only to the explicit standalone final owner. State tracks tasks/dependencies/evidence; specialists return updates, never edit shared state themselves.

## Intermediate asset contract

`production-plan.json` contains `assets`, initially empty. Each assigned asset records id, producer, source/output paths, destination composition/scene, startFrame, durationInFrames, width, height, fps, colorSpace, alpha format/background, audio policy, font dependencies, readiness, and validation evidence. Freeze filenames/timing before producer and consumer implementation. For web assets also record media-byte/mobile/poster/reduced-motion requirements.

Use one canonical output FPS/frame map for film. Intermediate assets match it or get an explicit coordinator-owned conversion; check frame 0, last included frame, joins, alpha edges, color and audio alignment. Opaque clips use a compatible video encoding; transparency uses a format proven by the installed consumer, or a local PNG/WebP sequence. Never assume a rendered MP4 contains alpha. Audio is either explicitly part of the master mix or muted in the clip to prevent double playback. Capture-ready flags include fonts, decoded media and a rendered scene. Preserve editable source and actual ffprobe/browser evidence. Render only assigned sequences, not a duplicate final film.

HyperFrames consumes verified assets as local media/sequences under its supported APIs, with seek/readiness checks at boundaries and no live external runtime dependency on Remotion or an upstream demo. Timelines use seconds at the host boundary and documented milliseconds/frames in adapters. Repeated forward/backward seeks and final renders must preserve the existing determinism checks.

## 3D parallax website profile

Automatically set `profile: 3d-parallax` and `open3d.enabled: true` when the build calls for 3D parallax. The normal role allocation is:

1. Research references for layer depth, camera paths, scroll pacing, text readability and mobile treatment. motionmaxxing contributes a depth/camera/motion plan; Open 3D assesses all eight skills and plans the scene. Remotion evaluates whether a pre-rendered layer or explanatory sequence adds value; use `no-work` with a reason if live 3D is sufficient.
2. In `animation-plan.json`, assign one owner to each scene/renderer/camera and one canonical normalized scroll progress `p` in [0,1]. Assign each DOM transform/opacity property to Anime.js or GSAP. A single progress adapter drives camera/layer/text consumers; do not run competing ScrollTrigger, Anime.js observer, ScrollFilm smoothing or independent camera animations for the same target. Optional pointer offsets remain a separately defined input.
3. parallax-background-agent designs/builds assigned background layers; Open 3D supplies scene techniques, geometry/media work and checks with the project Three.js version. The coordinator assigns the dedicated background or existing scene owner explicitly; threejs-agent supplies isolated geometry/model work or review under the ownership map. If a scene uses pre-rendered scroll media instead, reuse the same progress source and declare frame holds. Do not force a scroll-film or exploded view into an unsuitable brief.
4. Ensure restrained depth, readable text holds, semantic links/CTAs and keyboard access, no scroll trapping, mobile/touch/short-viewport layouts, poster-first loading, bounded assets and target-device frame budgets. Honor reduced motion initially and on change: remove decorative parallax/camera travel and expose readable static/key states without hiding content. Stop offscreen work and dispose listeners, GPU resources and observers.
5. Open 3D runs site-check and targeted scroll/pointer frame-capture for motion evidence, including fast forward/back scroll, pin release, resize, loading and reduced-motion changes. motionmaxxing reviews the actual site motion and frame evidence; film-only no-page-chrome/flat-frame gates do not apply to website navigation or reading holds. Unsupported hardware performance evidence is reported as a limitation, not a passing GPU budget.
6. If a companion film is requested, map the page's capture mode to the canonical clock and provide named intermediate clips for HyperFrames; preserve the functional website deliverable.

## Dependency and repair loop

Wave 1 gathers references/prerequisites. Wave 2 runs applicable specialist planning and freezes production/animation contracts after style and direction. Wave 3 creates assigned scene modules, Remotion clips and Open 3D media/captures only after dependencies and video timing exist. A website capture depends on a working integrated page: schedule that producer after page integration, then wait for the clip before final-film assembly. Wave 4 validates assets, integrates the page/HyperFrames draft, and runs motionmaxxing contribution review plus craft/site checks. Fresh engineering review and final QA follow. Send findings to the actual producer/scene/property owner, rerun affected producer and consumer checks, re-review the integrated result, and keep the existing three repair loops.

## Completion evidence

`production-plan.json`, `motionmaxxing-plan.md`, `motionmaxxing-review.md` when review is applicable, Remotion plan/source/clip evidence when assigned, Open 3D capability/validation evidence, and the integrated output are reviewed by QA. Missing required assets/checks block PASS. Clearly label N/A film gates on websites and no-work specialists; never claim unexecuted scripts or apply film-only style restrictions to useful web UI.

## 3D parallax brief example

```json
{
  "production": {
    "deliverable": "website",
    "profile": "3d-parallax",
    "finalRenderer": null,
    "specialists": {
      "remotion-agent": {
        "mode": "contribute",
        "reason": "Assess pre-rendered supporting layers; record no-work if live 3D is sufficient"
      },
      "motionmaxxing-agent": {
        "mode": "review",
        "reason": "Plan depth/camera/pacing and review integrated parallax"
      },
      "open-3d-agent": {
        "mode": "contribute",
        "reason": "Own scene, shared scroll adapter, site-check and motion evidence"
      },
      "parallax-background-agent": {
        "mode": "contribute",
        "reason": "Assess goal-led multilayer backgrounds"
      }
    }
  },
  "open3d": {
    "enabled": true,
    "skills": [
      "threejs-scene",
      "site-check",
      "frame-capture"
    ],
    "reason": "Live 3D parallax website"
  },
  "animation": {
    "engine": "animejs",
    "reason": "Assigned text/UI motion",
    "textResearch": true,
    "reducedMotion": "show-final-state"
  },
  "background": {
    "enabled": true,
    "websiteType": "product",
    "goal": "Clarify the product and support its primary CTA",
    "referenceImages": [],
    "reason": "Requested multilayer/parallax background"
  }
}
```

This is a briefing assessment, not proof of finished execution. Update specialist modes/reasons after assessment. The coordinator expands this into production-plan.json with concrete assets/tasks and fills the eight-skill Open 3D matrix. For website-and-video, set that deliverable and `finalRenderer: hyperframes`, declare capture assets, and wait for page readiness before capture and film assembly.

## Background specialist

`parallax-background-agent` is an additional normal assessed specialist. For 3D parallax/multilayer animated backgrounds it designs goal/reference-fit layers and builds owned modules under `references/parallax-background-integration.md`. It can own a dedicated background scene or contribute layers to the existing Open 3D-owned scene; the coordinator explicitly freezes which. All six background providers receive a use/skip/unavailable/blocked decision. html-video is a verified local template/asset provider under `references/html-video-integration.md`; distinguish source/build/render readiness and test timing/alpha before use. img2threejs is used for approved reference-object reconstruction, with background requirements before model production and model evidence before scene integration.
