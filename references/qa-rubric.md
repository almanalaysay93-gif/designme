# QA Rubric — Anti-Slop

## Design DNA
- [ ] Palette extracted, max 5 colors, not #8b5cf6 generic purple
- [ ] Typography specific (e.g., "Suisse Int'l 500 for headings" not "modern sans")
- [ ] tokens.css actually used in composition

## Motion Design (LottieFiles)
- [ ] Duration scale defined and respected
- [ ] Easing chosen with intent, not default ease-out
- [ ] Choreography: stagger 40-120ms, overlap not all at once
- [ ] Disney: anticipation, follow-through, weight

## GSAP (Official)
- [ ] useGSAP with cleanup or gsap.context()
- [ ] Timeline used, not scattered tweens
- [ ] Only transform/opacity
- [ ] ScrollTrigger: anticipatePin, scrub 0.5-1.5, no markers in prod

## Three.js
- [ ] Renderer antialias + PCFSoft shadows
- [ ] GLTF Draco + texture caching
- [ ] Controls damping enabled
- [ ] No memory leak (dispose on unmount)

## Genjutsu Anti-Slop List (MUST AVOID)
- Generic aurora / mesh gradient background
- Cards floating with y:-10 infinite yoyo
- Everything bouncy with elastic.out
- Inter font by default
- 2s fade-in for everything
- Purple on black "AI SaaS" look
- No thesis, code first

## HyperFrames
- [ ] No Math.random(), Date.now(), window.scrollY
- [ ] Timeline seekable: hf.onSeek(t) => timeline.seek(t)
- [ ] Captions overlay if voice
- [ ] Deterministic render tested: 2 renders identical hash
