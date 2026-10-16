# Visual Style Library

Use this library during grilling and read the selected style sections before direction. Choose **one primary style** and at most **one supporting style**. The style is a visual grammar, not a decorative checklist: define what it means for this brand, what moves, what stays quiet, and where the hero moment lands.

## Shared build contract

Every style spec must define:

- **Subject:** one brand/product idea the style makes clearer.
- **Palette:** 2–4 intentional colors and one state/accent meaning.
- **Material:** what the world is made of (ink, glass, paper, light, clay, pixels, etc.).
- **Motion grammar:** one dominant timing/easing system; no effect shopping.
- **Camera:** fixed, orbit, push-in, parallax, macro, or handheld simulation.
- **Hero beat:** the one moment worth a screenshot.
- **Proof:** the real product/content moment that keeps the style from becoming a wallpaper.
- **Anti-slop:** what the style must not become.

Shared HTML/GSAP skeleton:

```html
<canvas id="stage" width="1080" height="1920"></canvas>
<script>
const ctx = stage.getContext('2d');
const TAU = Math.PI * 2;
function render(t) {
  ctx.clearRect(0, 0, stage.width, stage.height);
  // 1. draw the style's world/material
  // 2. draw one focal subject and its proof
  // 3. animate from frame/time, never from mutable history
}
function loop(ms) { render(ms / 1000); requestAnimationFrame(loop); }
requestAnimationFrame(loop);
</script>
```

For deterministic video, use a pure `render(t)` function, seeded randomness, local assets, and one renderer. For SVG/DOM scenes, use GSAP timelines but keep a seek-safe time source.

## 1. Neon glow

**Grammar:** bright tubes, dark depth, restrained bloom, synthwave contrast. Use for energy, night, speed, nightlife, or a product that turns hidden activity visible.

**Build recipe:** SVG paths or canvas strokes → animate `stroke-dashoffset` → add a blurred duplicate behind the sharp line → use one accent color for the state change. Sample: a product workflow draws itself as a cyan circuit, then the final node ignites only when the real result appears.

**Avoid:** generic cyberpunk grids, every object glowing, purple-on-black SaaS defaults, and bloom hiding weak composition.

## 2. Particle swarm

**Grammar:** thousands of seeded points obeying a field, with a legible macro-form. Use for systems, communities, data, emergence, or transformation.

**Build recipe:** precompute Fibonacci-sphere or torus targets; interpolate particles from noise to target with eased spring; rotate the field, not each dot independently. Sample: particles form the product logo, dissolve into a real metric, then reassemble around the proof UI.

**Avoid:** random particle soup, unreadable forms, GPU-only nondeterminism, and a swarm with no brand-specific reason.

## 3. Pixel art

**Grammar:** hard nearest-neighbor edges, limited palette, deliberate frame steps, sprite-like staging. Use for nostalgia, games, playful developer tools, or a product with a clear retro metaphor.

**Build recipe:** render at 1/4 or 1/8 resolution, upscale with `image-rendering: pixelated`, animate on twos, and author a tiny sprite sheet. Sample: an 8-bit avatar walks through three real product states; the final state becomes the CTA.

**Avoid:** smooth easing on pixel elements, too many colors, fake random scanlines, and retro styling disconnected from the claim.

## 4. Glitch effect

**Grammar:** controlled signal failure, RGB separation, scanlines, frame tearing, then a clean resolution. Use for disruption, debugging, before/after, or revealing hidden structure.

**Build recipe:** duplicate the same text/logo into R/G/B masks; offset only during a transition window; add seeded horizontal bands; restore a clean layer for the proof. Sample: an incorrect result tears apart, the real product output locks into alignment.

**Avoid:** permanent glitch, unreadable copy, seizure-risk flashing, and glitch as a substitute for an idea.

## 5. Glassmorphism

**Grammar:** translucent surfaces, refraction, soft gradients, depth through blur and light. Use when the product owns layered information, privacy, or a calm premium interface.

**Build recipe:** place a real product capture behind `backdrop-filter: blur(18px)`, add one strong light source and thin edge highlights, then animate the camera or blob—not every card. Sample: a glass pane reveals the real UI beneath as the user makes one decision.

**Avoid:** floating cards on empty black, excessive blur, unreadable contrast, and invented dashboard chrome.

## 6. Liquid morph

**Grammar:** viscous, soft, continuous shape change with surface tension. Use for flow, conversion, collaboration, or a product that removes friction.

**Build recipe:** animate SVG path points with matched topology or use a metaball field; preserve area and a clear cause/effect handoff. Sample: a messy input blob stretches through the product action and resolves into the real output shape.

**Avoid:** random blob wallpaper, morphing the logo just because it is possible, and no readable pause before the payoff.

## 7. Holographic foil

**Grammar:** iridescent angle-dependent color, sharp specular sweep, sticker/foil material. Use for collectible, premium, playful, or identity-led moments.

**Build recipe:** use a normal map or procedural angle gradient: `h = (nx * .6 + ny * .4 + time * .12) % 1`; map hue through a restrained palette; add one moving highlight over a crisp mark. Sample: the brand mark behaves like a physical foil seal that catches light when the product succeeds.

**Avoid:** rainbow gradients everywhere, flat rainbow text, and holographic treatment on a brand that does not own it.

## 8. Clay 3D

**Grammar:** soft bevels, matte material, squash-and-stretch, friendly physical weight. Use for education, consumer products, characters, or approachable utility.

**Build recipe:** Three.js low-poly forms, large soft key light, ambient occlusion, and one authored squash on impact. Sample: a clay sun/character physically carries a real product task from blocked to complete.

**Avoid:** generic cute mascots, toy motion without product proof, and excessive bounce.

## 9. Kinetic typography

**Grammar:** words act out their meaning through orbit, scale, tracking, rotation, and silence. Use when language is the product or the message is the hero.

**Build recipe:** tokenize words, assign each a semantic motion verb, animate whole words rather than letter rain, and reserve the largest scale for one phrase. Sample: “around” literally orbits the core word while the product proof interrupts the type at the right beat.

**Avoid:** giant cropped words in every shot, circular text as decoration, typewriter effects, and text replacing evidence.

## 10. Vaporwave grid

**Grammar:** sunset gradient, horizon grid, silhouettes, retro perspective, deliberate nostalgia. Use only when the brand can own a playful 80s/90s reference.

**Build recipe:** draw a perspective grid with a horizon line, animate z-depth toward the camera, add one recognizable product silhouette, and keep the sunset palette limited. Sample: the product travels across a retro horizon while real feature outputs appear as signposts.

**Avoid:** stock palm trees, endless grid travel, and aesthetic nostalgia with no claim.

## 11. Halftone dots

**Grammar:** CMYK/pop-art dot scale, hard shapes, comic impact, selective misregistration. Use for bold campaigns, editorial energy, or a product with a clear print/poster voice.

**Build recipe:** convert a luminance mask to a dot grid with `r = map(luma, 0, 1, 0, cell * .48)`, then animate the mask or camera. Sample: the product proof emerges from yellow dots while a red accent marks the state change.

**Avoid:** applying halftone to every layer, illegible micro-dots, and unmotivated comic language.

## 12. Bauhaus shapes

**Grammar:** primary geometry, asymmetric balance, strict grid, functional color. Use for systems, architecture, education, or a brand with an editorial design voice.

**Build recipe:** define circle/rectangle/line primitives and a spacing grid; let one shape cause the next transition. Sample: a red rectangle becomes the real product panel, while a blue circle marks the successful action.

**Avoid:** poster imitation without hierarchy, equal-weight shapes, and decorative geometry unrelated to the story.

## 13. ASCII art

**Grammar:** characters are the image, monospaced texture, terminal rhythm, constrained contrast. Use for developer tools, protocols, data, or an intentionally low-fi identity.

**Build recipe:** sample luminance from a source frame, map it to a fixed character ramp, and animate rows or camera focus. Sample: a real command/output sequence grows from ASCII noise into the readable product result.

**Avoid:** unreadable walls of characters, fake terminal chrome, and using ASCII when the audience needs a real UI.

## 14. Paper cutout

**Grammar:** layered paper planes, tactile edges, shadows, parallax, handmade imperfection. Use for storytelling, editorial brands, climate/nature, or warm human craft.

**Build recipe:** split foreground/midground/background into SVG/PNG layers, add soft directional shadows, and move layers at different camera rates. Sample: paper mountains part to reveal the real product proof in a lit clearing.

**Avoid:** flat sticker piles, random texture, and parallax without depth logic.

## 15. Flow fields

**Grammar:** vector lines respond to a force field like wind, magnetism, or current. Use for movement, networks, navigation, or continuous intelligence.

**Build recipe:** seed lines with a deterministic PRNG, integrate `p += normalize(field(p,t)) * speed`, fade tails, and introduce one attractor tied to the product action. Sample: a field bends toward the exact real feature that solves the user’s problem.

**Avoid:** colorful screensaver behavior, no focal hierarchy, and uncontrolled line density.

## 16. Dithering

**Grammar:** binary/limited-tone image built from ordered or error-diffused dots. Use for archival, technical, monochrome, or resilient low-bandwidth identity.

**Build recipe:** use a Bayer matrix or seeded threshold; animate the threshold or source image, not random noise. Sample: a monochrome product capture resolves from dither into one crisp proof frame.

**Avoid:** noisy surfaces everywhere, poor small-type readability, and mistaking compression artifacts for style.

## 17. Risograph print

**Grammar:** paper grain, limited spot colors, ink overlap, registration drift, imperfect texture. Use for cultural/editorial brands and human-made warmth.

**Build recipe:** separate artwork into 2–3 ink layers, offset each by a few pixels, add restrained paper noise, and animate plate registration only at transitions. Sample: a real product statement is printed in layers until the final ink lands on the proof.

**Avoid:** fake “RISO PRINT” labels, over-grain, and paper texture without a print-world reason.

## 18. Metaballs

**Grammar:** blobs merge through a shared field, organic continuity, fluid boundaries. Use for chemistry, collaboration, merging, or playful transformation.

**Build recipe:** sum radial fields and threshold: `field += r*r / distSq`; render the contour with a stable threshold; keep one blob as the semantic subject. Sample: separate inputs merge only when the product action completes, then become the real output.

**Avoid:** lava-lamp wallpaper, random blob counts, and confusing merging with progress.

## 19. Topographic lines

**Grammar:** contour lines, elevation, map logic, measured depth. Use for geography, analytics, journeys, systems, or layered complexity.

**Build recipe:** generate contours from a seeded scalar field or real data; pan/zoom the camera and highlight one contour path as the proof route. Sample: the user’s messy process becomes a navigable contour map, with the real success path illuminated.

**Avoid:** map decoration with no data or journey, uniform contour density, and faux precision.

## 20. Ray-marched fractals

**Grammar:** deep volumetric distance fields, impossible depth, slow camera reveal, controlled complexity. Use for scientific, generative, technical, or truly surreal hero moments.

**Build recipe:** implement a bounded signed-distance field in a fragment shader, cap iterations, use a fixed camera path, and render a short hero shot rather than a whole film. Sample: the camera dives through a fractal structure and exits into the real product proof.

**Avoid:** unbounded GPU cost, visual noise, no focal exit, and using fractal complexity to hide a missing story.

## Style selection rule

The griller must output:

```json
"visualStyle": {
  "primary": "particle-swarm",
  "secondary": null,
  "requested": true,
  "reason": "The brand's network claim is best shown as a controlled field resolving into real proof.",
  "material": "seeded luminous particles",
  "motionGrammar": "orbit, converge, resolve",
  "heroBeat": "the swarm forms the real output shape",
  "antiSlop": ["no random particle soup", "no generic sci-fi grid"]
}
```

If two styles are selected, assign one a clear role. For example: **paper cutout** for the world + **halftone** for the proof transition. Never combine styles merely because both look attractive.
