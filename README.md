# /designme — invoke with /designme

One skill that spawns a griller/planner, parallel creative and engineering agents, a direction pass, a beat-sync pass, a motion-craft review, and a final anti-slop QA loop.

## Invoke

```text
/designme premium 9:16 launch reel, Linear + Stripe refs, heavy physical feel, no AI purple slop
```

## What was added

The update keeps **HyperFrames as the only renderer** and adds compatible production skills from the supplied list:

- `AbubakrChan/product-launch-motion` → `launch-director-agent`: competing directions, launch-film story, word-locked reveals, motivated camera language, look, and finishing.
- `Sunwood-ai-labs/hyperframes-motion-reel-skill` → `beat-sync-agent`: BPM/frame grids, morphing transitions, deterministic timelines, and code-generated score planning.
- `whaleyxbt/claude-motion` → `motion-craft-agent`: contact-sheet self-review, frame-level checks, web-sim guidance, and deterministic code-authored sound.
- `Blotato-Inc/blotato-skills` + `remotion-dev/skills` → `prompt-reference-agent`: free prompt patterns for brand intake, hooks, grading, repurposing, React/video composition, captions, and future projects.

Blotato and Remotion are now included as **prompt/reference sources**. Blotato contributes brand intake, hooks, grading, and repurposing patterns. Remotion contributes composition, frame, React/video, captions, and prompt-gallery patterns. Their publishing, scheduling, generation-provider, Lambda, and paid-service paths remain disabled by the free-only policy.

The following were intentionally **not** enabled as runtime systems because they duplicate or conflict with the repository’s current architecture:

- Remotion runtime/rendering is not enabled by default: its official skills and docs are used as prompt/reference material, while HyperFrames remains the default renderer.
- Generic motion catalogs and web-only Motion libraries: useful references, but not orchestration agents for this repo.
- HyperFrames student/tutorial kits: overlapping packaging rather than a distinct designme responsibility.

## Free-only rule

All 17 agents are restricted to free, local, open-source, or already-installed tooling. They must not call paid APIs, paid tiers, metered SaaS, premium models, paid voice or asset services, subscriptions, trials, billing-enabled integrations, or credit-consuming services. If a capability is not available for free, the agent must stop that part and offer a local or deterministic alternative.

## Structure

- `SKILL.md` — `/designme` contract, install gate, dependency waves, and output contract
- `agents/` — creative direction, motion engineering, beat sync, craft review, and QA agents
- `references/` — grilling questions, QA rubric, asset pipeline, missing checklist, and orchestration state
- `manifest.json` — selected source repositories and agent responsibilities

## Install

```bash
npx skills add CloudAI-X/threejs-skills greensock/gsap-skills zanwei/design-dna LottieFiles/motion-design-skill https://genjutsu.athevon.dev heygen-com/hyperframes -g
npx skills add whaleyxbt/claude-motion AbubakrChan/product-launch-motion Sunwood-ai-labs/hyperframes-motion-reel-skill -g
npx skills add obra/superpowers vercel-labs/agent-browser thedotmack/claude-mem -g
npx skills add https://github.com/anthropics/skills --skill frontend-design --skill skill-creator --skill mcp-builder --skill webapp-testing -g
npx skills add vercel-labs/skills --skill find-skills --skill taste --skill gsd -g
cp -r ./designme ~/.claude/skills/designme
```

Claude Code will now show `/designme` in the slash menu.
