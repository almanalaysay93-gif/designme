---
name: designme
description: Premium anti-AI-slop design & motion studio — invoke with /designme. Combines Three.js, GSAP, Design DNA, Motion Design, Genjutsu, HyperFrames + Superpowers, Find-Skills, Claude-Mem, Agent Browser, Taste/GSD into one orchestrated command. Spawns 1 agent per repo, 1 griller/planner, 1 QA anti-slop loop that feeds back on fail/slop. Use when user types /designme or wants premium animation that doesn't look AI.
allowed-tools: Task, Read, Write, Edit, Bash, Glob, Grep
---

# /designme — The Anti-Slop Design Studio

Invoke: `/designme <brief>` — e.g., `/designme premium 9:16 launch reel, Linear + Stripe refs, heavy physical feel, no AI purple slop`

## What This Is
One command that replaces 13 separate skills. Merged from:
- IG: Dd_iThjj32v — CloudAI-X/threejs-skills, greensock/gsap-skills, zanwei/design-dna, LottieFiles/motion-design-skill, AThevon/genjutsu, heygen-com/hyperframes
- TT: ZSbskVqY9 @usamasboard — obra/superpowers, vercel-labs/agent-browser, thedotmack/claude-mem, vercel-labs/skills (find-skills/taste/gsd), anthropics/skills (frontend-design/skill-creator/mcp-builder/webapp-testing)

## Invocation Contract
Claude Code sees `/designme` because skill folder is named `designme` and frontmatter name is `designme`. No extra slash file needed. When user types `/designme` or "designme" or "make it not look AI", this SKILL.md loads.

## Mandatory Orchestration (DO NOT SKIP)

### 0 — Install Gate
Check if deps installed. If not, run:
```bash
npx skills add CloudAI-X/threejs-skills greensock/gsap-skills zanwei/design-dna LottieFiles/motion-design-skill https://genjutsu.athevon.dev heygen-com/hyperframes obra/superpowers vercel-labs/agent-browser thedotmack/claude-mem -g
npx skills add https://github.com/anthropics/skills --skill frontend-design --skill skill-creator --skill mcp-builder --skill webapp-testing -g
npx skills add vercel-labs/skills --skill find-skills --skill taste --skill gsd -g
```

### 1 — The Griller (1 agent) — ALWAYS FIRST — BLOCKING
Spawn Task(subagent_type="planner-griller", prompt="Read references/grilling-questions.md, grill user, output brief.json + thesis, ask for YES").

Grill must cover:
- Creative: goal, audience, vibe 3 words + 2 refs, anti-slop list, duration/aspect/res, story arc
- Engineering: stack, constraints, success metric, plan mode? TDD? browser verification needed?
- Memory: load claude-mem

Output: brief.json {goal,audience,vibe,references,antiSlop,duration,aspect,tech,successMetric,interactionThesis,planMode}

DO NOT PROCEED UNTIL USER SAYS YES. This is Genjutsu rule.

### 2 — Parallel Spawn — 1 Agent Per Repo (dependency-aware)

**Wave 1 (no deps):**
- design-dna-agent (extracts tokens from refs)
- memory-agent (loads past taste)
- find-skills-agent (discovers missing skills)
- browser-agent (screenshots refs with real Chrome)

**Wave 2 (depends on Wave 1):**
- motion-design-agent (needs design-dna.json + browser-report)
- superpowers-agent (needs brief + memory, writes plan.md)

**Wave 3 (depends on Wave 2):**
- gsap-agent (needs motion-doctrine + design-dna)
- threejs-agent (needs doctrine + plan)
- genjutsu-agent (needs all above, writes thesis.md + MASTER.md)
- taste-gsd-agent (needs doctrine + design-dna)

**Wave 4 (depends on Wave 3):**
- hyperframes-agent (composes HTML using all outputs)

Use Task tool for each. Pass brief.json path and outputs from previous waves.

### 3 — QA Anti-Slop Loop (1 agent) — ALWAYS LAST
Spawn qa-anti-slop-agent AFTER composition. It reads references/qa-rubric.md + new references/missing-checklist.md.

If FAIL/SLOP: writes feedback.md targeting specific agent + exact fix, re-spawns ONLY that agent with feedback. Max 3 loops. On 3rd fail, escalate to user: "QA failed 3x, here's audit.md, approve with risk or fix brief?"

If PASS: runs `npx hyperframes render`, outputs MP4 + audit.md + plan.md + memory compression.

## Output Contract
- /hyperframes/output/final.mp4 (or aspect from brief)
- /src/ composition source (index.html, style.css, script.js, tokens.css)
- audit.md (what slop avoided, scores)
- brief.json + design-dna.json + motion-doctrine.md + thesis.md + plan.md + browser-report.md

Never write animation code yourself — delegate to sub-agents.
