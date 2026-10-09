# QA Rubric — Anti-Slop

## Direction and Story
- [ ] One approved direction is documented; two alternatives were killed with reasons
- [ ] One claim and one emotional thesis are visible in the shot plan
- [ ] First three seconds contain a hook
- [ ] Every shot has a purpose and every camera move is motivated

## Design DNA
- [ ] Palette extracted, max 5 colors, not #8b5cf6 generic purple
- [ ] Typography specific (e.g., "Suisse Int'l 500 for headings" not "modern sans")
- [ ] tokens.css actually used in composition

## Motion Design (LottieFiles)
- [ ] Duration scale defined and respected
- [ ] Easing chosen with intent, not default ease-out
- [ ] Choreography: stagger 40-120ms, overlap not all at once
- [ ] Disney: anticipation, follow-through, weight
- [ ] Holds are readable and the hook is not delayed by empty frames

## GSAP and Three.js
- [ ] useGSAP with cleanup or gsap.context()
- [ ] Timeline used, not scattered tweens
- [ ] Only transform/opacity for ordinary UI motion
- [ ] ScrollTrigger: anticipatePin, scrub 0.5-1.5, no markers in prod
- [ ] 3D assets are disposed and seeded layers are repeatable

## Beat and Timeline Contract
- [ ] One canonical timeline drives picture, captions, sound, and review timestamps
- [ ] BPM cuts and impacts land on the declared beat map
- [ ] Voice reveals use real word timings when voice exists
- [ ] Key visual lands on the drop or strongest narrative word

## Frame Craft
- [ ] Contact sheet includes every scene peak and sync-check timestamp
- [ ] No clipping, collisions, unsafe margins, accidental flash, or pop frame
- [ ] Camera actually moves with intent; no perpetual drift
- [ ] Product/UI copy and facts are approved and readable

## Audio
- [ ] 48kHz, no drift, and cues share the visual timeline
- [ ] Voice/music/SFX are individually audible and not masked
- [ ] True peak below -2 dBFS and loudness approximately -14 LUFS unless brief overrides
- [ ] Captions match voice timing and remain readable

## Genjutsu Anti-Slop List (MUST AVOID)
- Generic aurora / mesh gradient background
- Cards floating with y:-10 infinite yoyo
- Everything bouncy with elastic.out
- Inter font by default
- 2s fade-in for everything
- Purple on black "AI SaaS" look
- No thesis, code first

## HyperFrames
- [ ] No Math.random(), Date.now(), timers, or window.scrollY
- [ ] Timeline seekable: hf.onSeek(t) => timeline.seek(t)
- [ ] Pure render(t) layers are seeded and repeatable
- [ ] Captions overlay if voice
- [ ] Deterministic render tested: 2 renders identical hash
- [ ] ffprobe confirms expected FPS, dimensions, duration, and audio stream
