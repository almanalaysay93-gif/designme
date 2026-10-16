---
name: designme
description: Premium anti-AI-slop design and motion studio. Invoke with /designme for high-craft web animation, launch films, showreels, interactive figures, and deterministic HTML video. Combines Three.js, GSAP, Design DNA, motion principles, Genjutsu, HyperFrames, launch direction, beat sync, code-generated sound, frame review, Hairline, Remotion, and QA in one orchestrated command.
allowed-tools: Task, Read, Write, Edit, Bash, Glob, Grep
---

# /designme — The Anti-Slop Design Studio

Invoke: `/designme <brief>` — e.g. `/designme premium 9:16 launch reel, Linear + Stripe refs, heavy physical feel, no AI purple slop`

## What This Is

One command for brand-led, code-authored motion and interactive web visuals. HyperFrames remains the default video renderer, Remotion is an optional local React-video renderer, and Hairline is an optional interactive-figure engine; motionmaxxing is an optional local director/critic with strict G0-G5 gates. Blotato and Remotion are also used as free prompt/reference sources for future projects. It adds only complementary production disciplines:

- **Design DNA + motion principles:** extract a visual system and a motion doctrine before code.
- **Direction:** develop competing creative directions, a one-claim story arc, camera language, and shot plan.
- **Beat sync:** make a shared beat/timeline table that drives visuals, transitions, captions, and audio cues.
- **Craft:** use GSAP for choreography, Three.js for hero 3D, and pure `render(t)` functions for seek-safe generative layers.
- **Sound:** write code-generated cues or wire approved audio against the same timeline, then master and verify it.
- **Review:** render stills/contact sheets at beats and inspect them before final MP4 rendering.
- **Motion skill packs:** route the approved iart-ai packs to the agents that need them; install only the smallest compatible set.
- **Motionmaxxing:** optionally run brand-led idea/world direction, seek-safe craft checks, and evidence-based G0-G5 repair on launch films and motion promos.
- **Optional capabilities:** discuss Remotion, Hairline, and motion-skill pack selection during grilling, recommend what is needed, and activate only the user-approved choices.
- **QA:** run anti-slop, determinism, readability, audio, accessibility, and final-frame checks with targeted feedback loops.

## Invocation Contract

Claude Code sees `/designme` because the skill folder is named `designme` and frontmatter name is `designme`. When the user types `/designme`, `designme`, or asks for premium animation that does not look AI-generated, load this skill.

## Mandatory Orchestration (DO NOT SKIP)

### 0 — Install Gate

Check whether the dependencies are installed. If not, install the selected skills:

```bash
npx skills add CloudAI-X/threejs-skills greensock/gsap-skills zanwei/design-dna LottieFiles/motion-design-skill https://genjutsu.athevon.dev heygen-com/hyperframes -g
npx skills add whaleyxbt/claude-motion AbubakrChan/product-launch-motion Sunwood-ai-labs/hyperframes-motion-reel-skill -g
npx skills add remotion-dev/skills -g  # official prompt/reference guidance; local Remotion only
npx skills add lucasmarkes/hairline -g  # optional interactive figures; free/local only
# Install motionmaxxing locally; its installer checks requirements and installs nothing system-wide
if [ ! -d "$HOME/.claude/skills/motionmaxxing" ]; then git clone https://github.com/Tejashmakwana/motionmaxxing "$HOME/.claude/skills/motionmaxxing"; fi
# Install only the approved iart-ai packs selected during grilling; see references/motion-skills-packs.md
npx skills add obra/superpowers vercel-labs/agent-browser thedotmack/claude-mem -g
npx skills add https://github.com/anthropics/skills --skill frontend-design --skill skill-creator --skill mcp-builder --skill webapp-testing -g
npx skills add vercel-labs/skills --skill find-skills --skill taste --skill gsd -g
```

Do not use Remotion as a second renderer for a HyperFrames composition. Activate `remotion-agent` only when the brief explicitly requires a React/Remotion deliverable, and record the renderer decision. Activate `hairline-agent` only when the brief explicitly requests Hairline or an interactive figure. Activate `motionmaxxing-agent` only when the user approves it or explicitly asks for motionmaxxing; keep its work local and free-only.

## Free-Only Execution Policy

Use only free, local, open-source, or already-installed tools and APIs. Never call a paid API, paid tier, metered SaaS endpoint, premium model, paid voice service, paid asset service, or billing-enabled integration. Never create a subscription, start a trial, enter payment details, or consume credits. Do not ask the user for API keys for a paid service. If a requested capability requires payment or a paid API, stop that part, explain the limitation, and propose a free/local alternative such as Python, FFmpeg, Chromium, Playwright, system tools, or deterministic code-generated assets.

### 1 — The Griller (1 agent) — ALWAYS FIRST — BLOCKING

Spawn `planner-griller` with `references/grilling-questions.md`. It must cover goal, audience, references, anti-slop list, duration, aspect, resolution, story arc, audio/voice needs, stack, constraints, success metric, verification needs, the optional-agent gate, and motion-skill pack selection.

The griller must produce an explicit recommendation for all optional agents, including motionmaxxing:

```json
{
  "optionalAgents": {
    "remotion-agent": {"requested": false, "needed": false, "reason": "HyperFrames is sufficient"},
    "hairline-agent": {"requested": false, "needed": false, "reason": "No interactive figure requested"},
    "motionmaxxing-agent": {"requested": false, "needed": false, "reason": "Existing HyperFrames + QA is sufficient"}
  },
  "motionSkillPacks": []
}
```

Show the thesis, renderer choice, optional-agent recommendations, and brief to the user. Do not proceed until the user approves them.

### 2 — Parallel Spawn — dependency-aware

**Wave 1 (no dependencies):**

- `design-dna-agent` — extracts tokens from references.
- `memory-agent` — loads past taste and prior constraints.
- `find-skills-agent` — discovers only missing, compatible skills.
- `browser-agent` — captures reference screenshots with real Chrome.
- `prompt-reference-agent` — curates free prompt patterns from Blotato and Remotion for briefs and future projects.
- `find-skills-agent` — routes approved iart-ai motion-skill packs to the owning agents and records local installs.

**Wave 2 (needs brief and Wave 1 context):**

- `motion-design-agent` — writes timing, easing, weight, and choreography doctrine.
- `launch-director-agent` — writes three visual directions, kills two, and creates the story/shot/camera/look plan.
- `superpowers-agent` — writes the execution plan and tests.

**Wave 3 (needs Wave 2 outputs):**

- `beat-sync-agent` — creates the shared BPM/frame beat map, transition schedule, and audio cue plan.
- `gsap-agent` — implements the seekable choreography timeline.
- `threejs-agent` — implements only the necessary hero 3D or generative layer.
- `genjutsu-agent` — writes thesis and anti-slop MASTER.md.
- `taste-gsd-agent` — performs the aesthetic gate and execution critique.

**Wave 4 (needs all design and engineering outputs):**

- `hyperframes-agent` — assembles the deterministic HTML composition and renders drafts by default.
- `remotion-agent` — runs only if `brief.json.optionalAgents.remotion-agent.requested` is true or the user explicitly approved it; otherwise mark skipped.
- `hairline-agent` — runs only if `brief.json.optionalAgents.hairline-agent.requested` is true or the user explicitly approved it; otherwise mark skipped.
- `motionmaxxing-agent` — runs only if `brief.json.optionalAgents.motionmaxxing-agent.requested` is true or the user explicitly approved it; otherwise mark skipped.
- `motion-craft-agent` — runs still/contact-sheet review, checks frame collisions and safe areas, wires code-generated or approved sound, and records fixes.
- `motionmaxxing-agent` — audits or repairs launch-film craft using local G0-G5 gates and writes evidence.

Pass `brief.json`, the approved `motionSkillPacks`, and the relevant output paths to every agent. Never write animation code in the orchestrator; delegate it.

### 3 — QA Anti-Slop Loop — ALWAYS LAST

Spawn `qa-anti-slop-agent` after composition and craft review. It reads `references/qa-rubric.md` and `references/missing-checklist.md`.

If `FAIL` or `SLOP`, write `feedback.md` naming the exact agent, file, line or timestamp, and fix. Re-spawn only that agent. Allow at most 3 loops. On the third failure, escalate with `audit.md` and the concrete risk.

If `PASS`, render the final MP4 and verify:

```bash
npx hyperframes render --width <width> --height <height> --fps 60
ffprobe -v error -show_streams -show_format output/final.mp4
```

Compare two final renders by hash. If voice or music is present, verify captions, peak timing, loudness, and no drift. If Hairline is selected, include its browser/look validation in the QA evidence. If motionmaxxing is selected, include `motionmaxxing-note.md`, gate evidence for G0-G5, and all skipped-provider substitutions.

## Output Contract

- `/hyperframes/output/final.mp4`
- `/hyperframes/composition/` with `index.html`, `style.css`, `script.js`, `tokens.css`, and assets
- `brief.json`, `design-dna.json`, `motion-doctrine.md`, `directions.md`, `shot-plan.md`
- `timeline.json` or `beat-map.json`, `audio-cues.md`, and `audio_meta.json` when applicable
- `thesis.md`, `plan.md`, `browser-report.md`, `prompt-reference.md`, `brief-enhancements.md`, `motion-skills-installed.md`, `hairline-design.md` when applicable, `hairline-validation.md` when applicable, `contact-sheet.png`, and `audit.md`

No generic gradients, default purple-on-black SaaS styling, unmotivated bounce, or code-first production. Every visual and sound cue must have an intentional role in the approved thesis.
