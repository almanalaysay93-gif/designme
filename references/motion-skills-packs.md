# iart-ai Motion Skills Pack Routing

Source: https://github.com/iart-ai/motion-skills

`iart-ai/motion-skills` provides 51 open-source MIT skills in 15 installable packs. Use the packs as focused production references and workflows; do not install or run every pack for every project.

## Pack matrix

| Pack | Use for | Primary designme agents |
|---|---|---|
| `iart-ai/tiktok-video-skills` | TikTok, Reels, Shorts, vertical hooks, retention beats | `launch-director-agent`, `beat-sync-agent`, `motion-craft-agent` |
| `iart-ai/text-message-video-skills` | Text-message story videos and chat narratives | `launch-director-agent`, `prompt-reference-agent` |
| `iart-ai/youtube-video-skills` | YouTube/podcast clips and long-form-to-short repurposing | `launch-director-agent`, `prompt-reference-agent` |
| `iart-ai/ecommerce-video-skills` | Product, commerce, feature, and catalog videos | `launch-director-agent`, `hyperframes-agent`, `prompt-reference-agent` |
| `iart-ai/ad-video-skills` | Brand advertisements, paid-social creative, conversion hooks | `launch-director-agent`, `motion-design-agent`, `qa-anti-slop-agent` |
| `iart-ai/data-animation-skills` | Charts, KPI stories, dashboards, data-driven animation | `beat-sync-agent`, `remotion-agent`, `hyperframes-agent` |
| `iart-ai/explainer-video-skills` | Educational, product, and process explainers | `launch-director-agent`, `beat-sync-agent`, `prompt-reference-agent` |
| `iart-ai/map-animation-skills` | Editorial maps and geographic storytelling | `remotion-agent`, `threejs-agent`, `launch-director-agent` |
| `iart-ai/web-animation-skills` | Accessible web motion, SVG, GSAP, Lottie, and UI animation | `motion-design-agent`, `gsap-agent`, `hairline-agent` |
| `iart-ai/motion-design-skills` | Motion principles, timing, transitions, and visual polish | `motion-design-agent`, `motion-craft-agent`, `qa-anti-slop-agent` |
| `iart-ai/kinetic-typography-skills` | Kinetic type, captions, titles, and text choreography | `motion-design-agent`, `beat-sync-agent`, `remotion-agent` |
| `iart-ai/freelance-motion-skills` | Client briefs, handoff, revisions, and studio delivery | `planner-griller`, `superpowers-agent`, `qa-anti-slop-agent` |
| `iart-ai/webgl-animation-skills` | Three.js, WebGL, shaders, and technical 3D motion | `threejs-agent`, `motion-design-agent`, `qa-anti-slop-agent` |
| `iart-ai/manim-skills` | Mathematical and educational animation | `remotion-agent`, `threejs-agent`, `launch-director-agent` |
| `iart-ai/generative-illustration-skills` | Generative illustration and creative coding | `threejs-agent`, `hairline-agent`, `motion-design-agent` |

## Selection rules

1. The griller asks about audience, channel, artifact, data, interaction, and visual format before selecting packs.
2. Recommend the smallest compatible pack set. Do not enable all 15 by default.
3. Select packs in `brief.json.motionSkillPacks` and record the reason for each.
4. Install only approved packs, using their public `npx skills add` command. Never use paid APIs, generation providers, cloud rendering, subscriptions, trials, or credits.
5. Existing designme agents remain the owners of execution. Packs provide focused instructions and references; they do not create duplicate renderers or duplicate agents.
6. HyperFrames remains the default video renderer. Remotion, Hairline, and Manim are conditional capabilities selected during grilling.
7. Every pack-driven artifact must use a render/screenshot/probe/check loop. Do not hand over an unverified animation.

## Install command pattern

```bash
npx skills add iart-ai/<approved-pack> -g
```

Record installed packs in `motion-skills-installed.md`. If a pack cannot be installed locally, use the public README as reference and note the limitation rather than substituting a paid service.
