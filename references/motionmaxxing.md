# motionmaxxing — optional agent

Source: [Tejashmakwana/motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) (Apache-2.0). Install with:

```bash
npx skills add Tejashmakwana/motionmaxxing -g
```

The installed `SKILL.md` is the authority for laws, the never-ship list, script flags, and gates. This file is only the designme routing contract. Do not copy the upstream runtime, `library/`, or bundled GSAP/Three.js into this repo.

## When to select it

Select `motionmaxxing-agent` only when the user explicitly wants that pipeline:

- a brand-from-URL launch film, sting, kinetic-type piece, or social ad built as a measured-motion HTML film
- an upgrade or critique of an existing slop cut using its gates

Otherwise skip it. HyperFrames stays the default video renderer.

Exactly one video renderer per project:

| Renderer | When |
|---|---|
| HyperFrames | Default |
| Remotion | User explicitly wants a React/Remotion deliverable |
| motionmaxxing | User explicitly wants this measured-motion film |

Hairline is not a video renderer and may run beside the chosen one.

## Free-only override

Upstream voice, SFX, and music can call ElevenLabs. **Designme does not.** Never request an ElevenLabs key. Use user-provided audio or local FFmpeg/Python synthesis. If the plan needs paid voice, drop that part and say so in `film/NOTE.md`.

## Required local tools

Node.js 22+, Python 3, ffmpeg, Chrome. Check with the skill's `scripts/providers.sh` before building. A missing tool stops the agent. It does not pretend the film rendered.

## Gates the studio will trust

| Gate | Pass means |
|---|---|
| G0 | Render exists, decodes, is not blank, picture moves, length matches the plan, and planned audio is present and not silent |
| G1 | Proof is readable, lit, and in a world (judged on the contact sheet) |
| G2 | No run of more than 3 consecutive flat frames |
| G3 | End hold is short and the final shot is not most of the film |
| G4 | One hero per frame (judged on the contact sheet) |
| G5 | No page chrome (`lint.mjs`) |

A fail is fixed, never argued. `film/NOTE.md` must quote the gate results. The agent may not self-certify.

## Outputs when this agent owns the film

- `renderer-decision.md` — motionmaxxing is the renderer; HyperFrames and Remotion are skipped
- `film/STORYBOARD.md`
- `film/index.html`
- `film/final.mp4`
- `film/look-final/`
- `film/NOTE.md`
