# Workflow Diagram

1. User `/designme` -> `planner-griller` gathers goal, thesis, shot, motion, audio, and verification requirements.
2. User approves `brief.json` -> Wave 1 extracts Design DNA, memory, references, and missing skills.
3. Wave 2 writes motion doctrine, competing creative directions, the selected shot plan, and execution plan.
4. Wave 3 creates the canonical beat/frame map, GSAP/Three.js implementation, thesis, and taste critique.
5. Wave 4 assembles the seekable HyperFrames composition and runs draft contact-sheet and sound review.
6. `qa-anti-slop-agent` checks visual, timing, beat sync, audio, accessibility, and determinism.
7. If needed, re-run only the responsible agent for up to 3 loops.
8. On PASS, render final MP4, compare two render hashes, run `ffprobe`, and write `audit.md`.
