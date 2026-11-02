# Grilling Questions — Get the Real Goal

Don't accept the first answer. Dig until the project, renderer, interactions, and optional capabilities are clear.

1. **Goal:** What exact outcome? “30s launch video for X” not “cool animation”.
2. **Audience & Context:** Who sees it, where? (IG reel, landing hero, pitch, product UI, interactive diagram?)
3. **Vibe:** 3 adjectives + 2 reference links/screenshots. If none, ask for concrete references.
4. **Anti-Slop:** What do you hate? Show 2 examples of AI-looking animation or UI you do not want.
5. **Constraints:** Duration, aspect, resolution, tech stack (React/Next/Vanilla?), assets, logo, browser, and performance limits.
6. **Story:** One sentence story arc. “From chaos to calm” or “From sketch to product”.
7. **Success Metric:** What makes you say “this is premium, not AI”?
8. **Optional-agent gate:** Should this project use an optional agent?
   - **Hairline:** select only for an interactive line figure, pointer-responsive diagram, technical illustration, or self-contained Hairline visual. Otherwise skip it.
   - **Opus 5.5 videos:** select only when the user wants a starting prompt from that code-video catalog. It does not change the renderer. See `references/opus5-videos.md`.
   - **UI/UX Pro Max:** select for UI, landing pages, dashboards, product demos, forms, navigation, charts, mobile UI, or UX/accessibility reviews. It uses local searchable data and does not render video. See `references/ui-ux-pro-max-integration.md`.
   - **img2threejs:** select when the user supplies a 2D reference image of an object, product, prop, or character and wants a procedural code-only Three.js `THREE.Group` model (`create<ObjectName>Model`). See `references/img2threejs.md`.

9. **Visual-style gate:** Choose one primary style from `references/visual-style-library.md` and optionally one supporting style. Which of the 20 styles fits the brand and claim? The agent must recommend a style, material, motion grammar, hero beat, and anti-slop boundaries.

10. **Motion-skills pack gate:** Which format and craft packs are needed? Use the smallest compatible set from `references/motion-skills-packs.md`—for example TikTok/Reels, data animation, explainer, kinetic typography, WebGL, or web animation.

The planner must make a recommendation for each optional agent and motion-skill pack, explain why it is or is not needed, and ask the user to approve the selection before dispatch. One final owner per deliverable; supporting asset renders may coexist.

Output: `brief.json`

```json
{
  "goal": "",
  "audience": "",
  "vibe": ["", "", ""],
  "references": ["url1", "url2"],
  "antiSlop": ["no...", "no..."],
  "duration": "15s",
  "aspect": "9:16",
  "resolution": "1080x1920",
  "tech": "HTML + HyperFrames",
  "production": {"deliverable":"video","profile":"standard","finalRenderer":"hyperframes","specialists":{"remotion-agent":{"mode":"contribute","reason":"Assess supporting sequences"},"motionmaxxing-agent":{"mode":"review","reason":"Motion planning and integrated review"},"open-3d-agent":{"mode":"contribute","reason":"Assess scenes and capture"}}},
  "optionalAgents": {
    "hairline-agent": {"requested": false, "needed": false, "reason": ""},
    "opus5-videos-agent": {"requested": false, "needed": false, "reason": ""},
    "ui-ux-pro-max-agent": {"requested": false, "needed": false, "reason": ""},
    "img2threejs-agent": {"requested": false, "needed": false, "reason": ""}
  },
  "motionSkillPacks": [
    {"pack": "iart-ai/motion-design-skills", "requested": false, "needed": false, "reason": ""}
  ],
  "successMetric": "",
  "interactionThesis": "",
  "visualStyle": {
    "primary": "particle-swarm",
    "secondary": null,
    "requested": true,
    "reason": "",
    "material": "",
    "motionGrammar": "",
    "heroBeat": "",
    "antiSlop": []
  }
}
```

## Text and element animation routing

Read `references/animejs-integration.md`. For landing pages with motion, default `brief.json.animation` to `{"engine":"animejs","reason":"Landing-page text and element motion","textResearch":true,"reducedMotion":"show-final-state"}`. Honor explicit stack or static requirements; use `mixed` only for disjoint ownership and `none` for static builds. Schedule `prompt-reference-agent` to find animated-word references that fit the brand/copy before motion planning. The coordinator records target/property ownership in `animation-plan.json` before implementation. This is core routing, not an extra optional-agent approval gate.

## Open 3D selection

Read `references/open-3d-integration.md`. Recommend the relevant Open 3D skills for procedural scenes, exploded views, scroll films, transparent media, cursor rigs or extra 3D QA. Record `brief.json.open3d` as `{"enabled":true,"skills":["threejs-scene","site-check","frame-capture"],"reason":"3D parallax website"}` or the selected enabled scope in the approved brief. Keep paid motion-assets generation disabled; use local/supplied assets. Explain scene ownership alongside threejs-agent and preserve Anime.js for assigned landing-page text.

## Normal specialists and 3D parallax

Read `references/normal-motion-orchestration.md`. Assess Remotion, motionmaxxing and Open 3D normally; do not request separate opt-in for their contribution roles or put them in optionalAgents. Record `production` deliverable/profile/finalRenderer/specialist modes and reasons in the brief, then coordinator-owned `production-plan.json`. Default films to HyperFrames and websites to no final renderer. For 3D parallax websites enable Open 3D, assign depth/camera/pacing guidance to motionmaxxing, assess useful Remotion layers/clips, and preserve Anime.js text/UI with one canonical scroll progress source. Record no-work reasons when a specialist adds no value.
