# /designme — invoke with /designme

One skill that spawns 1 agent per repo, 1 griller/planner, 1 QA loop.

## Invoke
```
/designme premium 9:16 launch reel, Linear + Stripe refs, heavy physical feel, no AI purple slop
```

## Structure
- SKILL.md — name: designme, so /designme triggers
- agents/ — 13 agents (6 creative IG + 6 engineering TT + 1 planner + 1 QA)
- references/ — grilling questions, QA rubric, asset pipeline, missing checklist, orchestrator state
- manifest.json — all repos

## What Was Missing (now fixed)
See references/missing-checklist.md — dependency graph, invocation contract, asset pipeline, determinism, cost, memory, escalation, testing.

## Install
```bash
npx skills add CloudAI-X/threejs-skills greensock/gsap-skills zanwei/design-dna LottieFiles/motion-design-skill https://genjutsu.athevon.dev heygen-com/hyperframes obra/superpowers vercel-labs/agent-browser thedotmack/claude-mem -g
npx skills add https://github.com/anthropics/skills --skill frontend-design --skill skill-creator --skill mcp-builder --skill webapp-testing -g
npx skills add vercel-labs/skills --skill find-skills --skill taste --skill gsd -g
cp -r ./designme ~/.claude/skills/designme
```

Claude Code will now show /designme in slash menu.
