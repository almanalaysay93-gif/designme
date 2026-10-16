# Grilling Questions — Get the Real Goal

Don't accept the first answer. Dig until the project, renderer, interactions, and optional capabilities are clear.

1. **Goal:** What exact outcome? “30s launch video for X” not “cool animation”.
2. **Audience & Context:** Who sees it, where? (IG reel, landing hero, pitch, product UI, interactive diagram?)
3. **Vibe:** 3 adjectives + 2 reference links/screenshots. If none, ask for concrete references.
4. **Anti-Slop:** What do you hate? Show 2 examples of AI-looking animation or UI you do not want.
5. **Constraints:** Duration, aspect, resolution, tech stack (React/Next/Vanilla?), assets, logo, browser, and performance limits.
6. **Story:** One sentence story arc. “From chaos to calm” or “From sketch to product”.
7. **Success Metric:** What makes you say “this is premium, not AI”?
8. **Optional-agent gate:** Should this project use either optional agent?
   - **Remotion:** select only for an explicitly requested React/Remotion video deliverable. Otherwise use HyperFrames by default.
   - **Hairline:** select only for an interactive line figure, pointer-responsive diagram, technical illustration, or self-contained Hairline visual. Otherwise skip it.
   - **Neither:** choose this when the default HyperFrames workflow is sufficient.

9. **Motionmaxxing gate:** Should the project use the optional motionmaxxing director/critic for brand-led launch-film direction, local seek-safe craft, and G0-G5 repair? Recommend skip when HyperFrames + existing QA is sufficient.

10. **Motion-skills pack gate:** Which format and craft packs are needed? Use the smallest compatible set from `references/motion-skills-packs.md`—for example TikTok/Reels, data animation, explainer, kinetic typography, WebGL, or web animation.

The planner must make a recommendation for each optional agent, including motionmaxxing, and each motion-skill pack, explain why it is or is not needed, and ask the user to approve the selection before dispatch.

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
  "optionalAgents": {
    "remotion-agent": {"requested": false, "needed": false, "reason": ""},
    "hairline-agent": {"requested": false, "needed": false, "reason": ""},
    "motionmaxxing-agent": {"requested": false, "needed": false, "reason": ""}
  },
  "motionSkillPacks": [
    {"pack": "iart-ai/motion-design-skills", "requested": false, "needed": false, "reason": ""}
  ],
  "successMetric": "",
  "interactionThesis": ""
}
```
