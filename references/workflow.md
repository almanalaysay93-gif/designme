# Workflow Diagram

1. User `/designme` -> `planner-griller` gathers goal, thesis, shot, motion, audio, renderer, and verification requirements.
2. User approves `brief.json` -> Wave 1 extracts Design DNA, memory, references, and missing skills. If approved, `opus5-videos-agent` writes `opus-prompt-brief.md` here.
3. Wave 2 writes motion doctrine, competing creative directions, the selected shot plan, and execution plan.
4. Wave 3 creates the canonical beat/frame map, GSAP/Three.js implementation or notes, thesis, and taste critique.
5. Wave 4 assembles exactly one video renderer: HyperFrames by default, or the approved Remotion or motionmaxxing film. Then run draft contact-sheet and sound review. Hairline, if approved, is an interactive figure beside that renderer, not a second video.
6. `qa-anti-slop-agent` checks visual, timing, beat sync, audio, accessibility, and determinism. If motionmaxxing owns the film, it also checks quoted G0–G5 evidence. If the Opus catalog was used, it checks credits and that the film is not a clone.
7. If needed, re-run only the responsible agent for up to 3 loops.
8. On PASS, render the final MP4 with the approved renderer, compare two render hashes, run `ffprobe`, and write `audit.md`.
