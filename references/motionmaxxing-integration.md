# Motionmaxxing Integration

Source: https://github.com/Tejashmakwana/motionmaxxing

`motionmaxxing` is an optional 20th designme agent and local skill for brand-led motion direction, seek-safe HTML/GSAP films, and evidence-based anti-slop review. It complements, rather than replaces, the designme pipeline.

## When to select it

Recommend `motionmaxxing-agent` during grilling when the brief needs one or more of:

- a launch film, product promo, brand sting, kinetic-type piece, or social ad;
- a brand-capture and one-true-idea pass;
- strict no-dead-frame, no-page-chrome, one-hero, short-end-card, and proof-readability checks;
- audit and repair of an existing motion draft;
- a blind A/B review between two motion versions.

Skip it for a simple UI micro-interaction, a data chart with no film treatment, or a project where the existing HyperFrames and QA workflow is sufficient.

## Integration contract

- `planner-griller` recommends the agent and asks for approval.
- `motionmaxxing-agent` runs in Wave 4 after the thesis, direction, beat map, and composition exist.
- `hyperframes-agent` remains the default renderer.
- `qa-anti-slop-agent` remains the final authority and consumes the motionmaxxing evidence.
- The agent may audit or repair the existing composition; it must not silently replace the renderer or approved thesis.

## Quality gates

| Gate | Evidence | Designme use |
|---|---|---|
| G0 | Render decodes, is non-blank, moves, matches planned length, and has planned audio | Required for final render acceptance |
| G1 | Proof is readable and visibly staged in a world | Visual sheet/still review |
| G2 | No run of more than three flat frames, except an intentional designed breath | Motion review and `look.py` |
| G3 | End hold is at most 1.4 seconds and the final shot is at most 25% of the film | `look.py` |
| G4 | One hero per frame; two panels require a clear area or camera-movement reason | Visual sheet review |
| G5 | No page chrome, counters, metadata, progress bars, deck layout, or vibe-coded UI cards | `lint.mjs` |

The agent must quote the actual script output or state that a gate was judged by eye. It must never claim PASS from an uninspected render.

## Local installation

The repository’s installer checks requirements but does not install system software. Install the source skill locally:

```bash
git clone https://github.com/Tejashmakwana/motionmaxxing ~/.claude/skills/motionmaxxing
# Or use the checked-out source:
bash /path/to/motionmaxxing/install.sh --dir ~/.claude/skills/motionmaxxing --copy --force
```

Requirements are local Node 22+, Python 3.9+, FFmpeg, and Chrome. The designme integration does not require optional provider keys.

## Free-only substitutions

The upstream skill can optionally use ElevenLabs for voice/music/SFX and Codex image generation for surface plates. Designme disables those paths. Use:

- code-authored Web Audio, FFmpeg-generated cues, user-provided audio, or silence;
- captured brand assets, deterministic HTML/CSS/JS, SVG, procedural Three.js, or user-provided images;
- local Chromium screenshots and FFmpeg renders;
- HyperFrames or the existing local composition for final output.

Record skipped optional providers and the substitution in `motionmaxxing-note.md`.
