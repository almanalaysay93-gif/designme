# Workflow Diagram

1. User `/designme` -> `planner-griller` gathers goal, thesis, shot, motion, audio, renderer, optional agents (`img2threejs-agent`, `ui-ux-pro-max-agent`, `hairline-agent`, `opus5-videos-agent`), and verification requirements.
2. User approves `brief.json` -> Wave 1 extracts Design DNA, memory, references in local Chromium, and missing skills. If approved, `opus5-videos-agent` writes `opus-prompt-brief.md` here.
3. Wave 2 writes visual style spec, UI/UX design system (if approved), `img2threejs-agent` procedural 3D reconstruction (if approved), motion doctrine, competing creative directions, the selected shot plan, and execution plan (`superlite-agent`).
4. Wave 3 creates the canonical beat/frame map, Anime.js/GSAP/Three.js implementation or notes (mounting `create<ObjectName>Model` when `img2threejs-agent` ran), thesis, and taste critique.
5. Wave 4 validates assigned intermediate clips/captures, assembles the HyperFrames final-film draft by default, and runs motionmaxxing contribution review. Explicit standalone output can select a different final owner; one final owner per deliverable. Then run draft contact-sheet and sound review. Hairline, if approved, is an interactive figure beside that renderer, not a second video.
6. `qa-anti-slop-agent` boots the output in local Chromium (`chromium-1248`) and checks `leaningtech/browsercode` preview rules to verify visual design accuracy, plan compliance (`plan.md` and `orchestrator.json`), timing, beat sync, audio, accessibility, UX laws, and determinism.
7. If needed, re-run only the responsible agent for up to 3 loops.
8. On PASS, deliver the verified live site for website work. For video, render with its final owner, compare two render hashes, run `ffprobe`, and write `audit.md`.

UX laws apply throughout: read `references/ux-laws.md` before planning, map all
14 laws in `plan.md`, pass checks to each specialist, and have final QA complete
`UX_LAWS_AUDIT.md` after each build/significant change. Fix and re-audit within the
existing repair cap; no PASS with violations or missing required evidence.

For animated landing pages, default to Anime.js. Wave 1 researches animated-word references; Wave 2 consumes them and freezes engine/property ownership; Wave 3 implements the assigned motion. Follow `references/animejs-integration.md`. Web-only builds skip video-render tasks and use interaction timings instead of a video beat map.

For selected Open 3D work, open-3d-agent plans in Wave 2, implements its owned modules in Wave 3 and validates the integrated draft in Wave 4. Its findings feed craft review and final QA; failures return to the same owner and are rechecked within the existing three repair loops. Read `references/open-3d-integration.md`.

Normal specialist assessment, contribution and asset handoffs follow `references/normal-motion-orchestration.md`. 3D parallax websites automatically use its profile, with a live site as the primary deliverable and no forced final film.
