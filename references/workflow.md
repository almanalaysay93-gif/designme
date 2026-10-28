# Workflow Diagram

1. User `/designme` -> `planner-griller` gathers goal, thesis, shot, motion, audio, renderer, optional agents (`img2threejs-agent`, `ui-ux-pro-max-agent`, `remotion-agent`, `hairline-agent`, `motionmaxxing-agent`, `opus5-videos-agent`), and verification requirements.
2. User approves `brief.json` -> Wave 1 extracts Design DNA, memory, references in local Chromium, and missing skills. If approved, `opus5-videos-agent` writes `opus-prompt-brief.md` here.
3. Wave 2 writes visual style spec, UI/UX design system (if approved), `img2threejs-agent` procedural 3D reconstruction (if approved), motion doctrine, competing creative directions, the selected shot plan, and execution plan (`superlite-agent`).
4. Wave 3 creates the canonical beat/frame map, GSAP/Three.js implementation or notes (mounting `create<ObjectName>Model` when `img2threejs-agent` ran), thesis, and taste critique.
5. Wave 4 assembles exactly one video renderer: HyperFrames by default, or the approved Remotion or motionmaxxing film. Then run draft contact-sheet and sound review. Hairline, if approved, is an interactive figure beside that renderer, not a second video.
6. `qa-anti-slop-agent` boots the output in local Chromium (`chromium-1243`) and checks `leaningtech/browsercode` preview rules to verify visual design accuracy, plan compliance (`plan.md` and `orchestrator.json`), timing, beat sync, audio, accessibility, UX laws, and determinism.
7. If needed, re-run only the responsible agent for up to 3 loops.
8. On PASS, render the final MP4 with the approved renderer, compare two render hashes, run `ffprobe`, and write `audit.md`.

UX laws apply throughout: read `references/ux-laws.md` before planning, map all
14 laws in `plan.md`, pass checks to each specialist, and have final QA complete
`UX_LAWS_AUDIT.md` after each build/significant change. Fix and re-audit within the
existing repair cap; no PASS with violations or missing required evidence.
