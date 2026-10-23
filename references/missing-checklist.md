# What You're Missing — /designme gaps before this fix

You had the right idea (1 agent per repo + griller + QA), but v1/v2 was missing:

### 1. Dependency Graph (you were spawning all 12 in parallel)
- design-dna MUST finish before motion-design (motion needs tokens)
- motion-doctrine MUST finish before gsap + threejs (they need easing/timing)
- genjutsu thesis MUST finish before hyperframes (it needs to know what NOT to do)
- browser-agent MUST finish before design-dna (real tokens, not hallucinated)

Fix: now 4 waves, not 1 big parallel.

### 2. Invocation Contract
- Skill folder was named hypercraft-studio, so /designme never triggered
- Claude Code uses folder name + frontmatter name for slash. Now both = designme
- Added allowed-tools frontmatter so Task spawning works

### 3. Asset Pipeline (critical miss)
- No font licensing check — you extract font from ref but never download/license
- No image optimization — GLB/ Lottie JSON not compressed, will blow up MP4
- No caption/narration handling for HyperFrames
Fix added: hyperframes-agent now has asset checklist in references/asset-pipeline.md

### 4. Determinism & Anti-Flake
- HyperFrames needs headless clock locking, no Math.random/Date.now/window.scroll
- No hash compare of 2 renders to prove deterministic
- No reduced-motion + a11y check

### 5. Cost & Concurrency
- 12 agents parallel = $$$ and rate limits. Now waved + concurrency limit 3-4
- No token budget. Added: Superlite execution plan includes cost estimate, user approves before Wave 2

### 6. State & Memory
- brief.json was overwritten each time, no versioning
- claude-mem was listed but never wired to inject taste or save session
- No orchestrator.json tracking which agent passed/failed/loop count

### 7. QA Escalation
- QA loop had max 3 but no escalation path — it just stopped
- Now: on 3rd fail, asks user: approve with risk or change brief?

### 8. Testing & Verification
- No browser verification that final MP4 matches refs
- No webapp-testing skill usage (from anthropics/skills)
- No TDD cases from the Superlite execution plan actually executed

### 9. Output Contracts
- No clear output folder structure, so agents wrote random places
- No audit.md scoring (how premium vs slop)
- No Figma/design handoff if user wants web not just video

### 10. Find-Skills Loop
- find-skills-agent existed but never actually searched skills.sh when brief expanded

### Fixed in /designme:
- Added Wave system in SKILL.md
- Added references/asset-pipeline.md, references/missing-checklist.md, references/orchestrator-state.md
- Renamed folder + frontmatter to designme so /designme works
- Added escalation + cost approval + deterministic hash check + a11y check
- Wired claude-mem, browser-agent, taste, gsd properly
