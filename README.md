# /designme — invoke with /designme

One skill that spawns a griller/planner, parallel creative and engineering agents, a direction pass, a beat-sync pass, a motion-craft review, and a final anti-slop QA loop.

> **Scope:** HyperFrames is the default renderer. The local `remotion-agent` is optional and runs only when a project explicitly requests React/Remotion. `hairline-agent` is optional and runs only for interactive figures or pointer-responsive web visuals. `motionmaxxing-agent` is optional and runs only when approved for brand-led launch films, motion audits, or G0-G5 repair. Blotato and Remotion references are used for prompt patterns only. All agents follow a free-only policy with no paid APIs, cloud rendering, publishing, scheduling, or credits.

## Invoke

```text
/designme premium 9:16 launch reel, Linear + Stripe refs, heavy physical feel, no AI purple slop
```

## Optional-agent grilling gate

During the first grilling session, `planner-griller` must recommend whether each optional agent—including motionmaxxing—and iart-ai motion-skill pack is needed and ask for approval:

| Optional agent | Use it when | Default recommendation |
|---|---|---|
| `remotion-agent` | The brief explicitly requires a React/Remotion video deliverable or Remotion-specific composition | Skip it and use HyperFrames |
| `hairline-agent` | The brief requires an interactive line figure, pointer-responsive diagram, technical illustration, or self-contained Hairline visual | Skip it unless the interaction needs it |
| `motionmaxxing-agent` | Brand-led launch film, product promo, kinetic type, social ad, or strict G0-G5 motion audit/repair | Skip for simple motion; recommend for film-level craft review |

The recommendation is stored in `brief.json.optionalAgents`. Optional agents are never silently activated. A user request can approve an agent even when it is not strictly necessary, with the tradeoff recorded.

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
- `Tejashmakwana/motionmaxxing` → `motionmaxxing-agent`: optional local brand capture, idea/world direction, seek-safe HTML/GSAP craft, G0-G5 gates, page-chrome lint, and blind review.

## Free-only rule

All 20 agents are restricted to free, local, open-source, or already-installed tooling. They must not call paid APIs, paid tiers, metered SaaS, premium models, paid voice or asset services, subscriptions, trials, billing, or credit-consuming services. If a capability is not available for free, the agent must stop that part and offer a local or deterministic alternative.

## Structure

- `SKILL.md` — `/designme` contract, install gate, dependency waves, optional-agent gate, and output contract
- `agents/` — creative direction, motion engineering, optional Remotion/Hairline/motionmaxxing agents, craft review, and QA agents
- `references/` — grilling questions, prompt sources, iart motion-pack routing, motionmaxxing integration, QA rubric, asset pipeline, missing checklist, and orchestration state
- `manifest.json` — selected source repositories and agent responsibilities

## Install

```bash
npx skills add CloudAI-X/threejs-skills greensock/gsap-skills zanwei/design-dna LottieFiles/motion-design-skill https://genjutsu.athevon.dev heygen-com/hyperframes -g
npx skills add whaleyxbt/claude-motion AbubakrChan/product-launch-motion Sunwood-ai-labs/hyperframes-motion-reel-skill -g
npx skills add remotion-dev/skills lucasmarkes/hairline -g
# Install motionmaxxing locally (the installer checks requirements; it installs nothing system-wide)
git clone https://github.com/Tejashmakwana/motionmaxxing ~/.claude/skills/motionmaxxing
# Add only the iart-ai packs approved during grilling; see references/motion-skills-packs.md
npx skills add obra/superpowers vercel-labs/agent-browser thedotmack/claude-mem -g
npx skills add https://github.com/anthropics/skills --skill frontend-design --skill skill-creator --skill mcp-builder --skill webapp-testing -g
npx skills add vercel-labs/skills --skill find-skills --skill taste --skill gsd -g
cp -r ./designme ~/.claude/skills/designme
```

Claude Code will now show `/designme` in the slash menu.
