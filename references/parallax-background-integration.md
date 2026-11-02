# Multilayer animated background orchestration

`parallax-background-agent` designs and builds goal-led 3D/multilayer parallax animated website backgrounds. It is a normal assessed role, automatically active when the approved build asks for that treatment. Use [normal motion orchestration](normal-motion-orchestration.md) for final output and intermediate assets. All six providers are assessed; executing all six on every site is not required.

## Goal and technique selection

| Website type / primary goal | Starting treatment | Useful contributors |
| --- | --- | --- |
| SaaS, services, lead capture, checkout | Quiet depth planes/lighting or small procedural accents, stable text/CTA zone, fast static fallback | motionmaxxing for restraint, Open 3D for lightweight layers; no unnecessary video |
| Product/ecommerce | Realistic product/space layers, motivated camera, factual detail and unobscured purchase controls | Open 3D; img2threejs for a reference product needing procedural reconstruction; Remotion for justified supporting media |
| Portfolio, entertainment, storytelling | Richer spatial layers, sequenced camera/depth reveals and readable scroll holds | Open 3D, motionmaxxing, locally produced clip layers when useful |
| Architecture, travel, immersive spatial experience | Live procedural/loaded scenes where viewpoints matter, or local scrubbed footage where a fixed path is sufficient | Open 3D, optional reference-object reconstruction and verified local clip pipelines |
| Editorial, education, accessibility-sensitive or constrained device | Minimal depth, deliberate reading holds, simple image/procedural layers, static mode | Prefer low-cost layers over heavy scene/video pipelines |

These are starting recommendations, not templates. The approved site goal, reference and measured budget override category defaults. Record rejected alternatives and the chosen effect's purpose.

## Reference-image routing

Wave 1 research/browser roles inspect supplied images and cite actual visual observations in `background-references.md`: subject, scale/perspective, lighting, materials/palette, composition and text-safe region; propose a depth map/layer sketch conceptually without claiming measured depth. Keep image provenance/path and mark inferred occluded regions. Do not destructively edit the source or fabricate a successful background-removal/depth model run.

- A mood/reference image can guide procedural layers without reconstruction.
- Existing artwork with separable subjects can become local cutouts/planes with approved masks and conservative hidden-region treatment; label 2.5D technique honestly. Missing masks/assets require real local production or a documented fallback.
- For a clear object/character that benefits from an actual code-authored 3D representation, request img2threejs with that specific target, required views/pivots and quality evidence. Record the recommendation under the existing optionalAgents entry. An approved brief asking for this reconstruction already authorizes the agent; do not ask again. A reference image by itself is not a mandate to reconstruct everything.
- img2threejs runs after the background's reconstruction spec is ready in Wave 2; scene implementation in Wave 3 waits for its gated deterministic model factory and evidence. Consume its passes/report; report single-image hidden-angle approximation and preserve local-only generic/character profiles.
- Without an image, research site-goal/brand-fit examples and build a procedural or supplied-asset treatment; no reconstruction dependency.

## Provider contract

| Provider | Role in this background | Availability / boundary |
| --- | --- | --- |
| HyperFrames | Supporting HTML-rendered footage or requested companion film; default final-film assembler | Normal existing specialist; live website remains primary |
| Remotion | Assigned local frame-based layer/clip when useful | Normal existing specialist; obey production asset metadata and local licensing/free-only checks |
| motionmaxxing | Goal-specific depth/camera/pacing plan and actual integrated motion review | Contribution mode; do not apply film-only UI prohibitions to a website |
| Open 3D | Procedural scenes, scroll media, alpha layers, cursor techniques, site-check and capture | Read/assess all eight skills; preserve one scene/progress owner |
| html-video | Goal-fit HTML templates/source and assigned local supporting footage | Verified source https://github.com/nexu-io/html-video (Apache-2.0); use [local provider contract](html-video-integration.md), inspect installed engines, and verify capture timing/alpha instead of assuming them |
| img2threejs | Reference object/character → deterministic THREE.Group factory | Conditional reconstruction via existing approved-brief gate, not a full-image depth conversion service |

For html-video, follow [its verified-source installation and runtime contract](html-video-integration.md). The installed source/engine list is authoritative; source availability, dependency readiness and successful render validation are separate statuses. Never start paid soundtrack/model/agent generation paths. Use source reauthoring or a tested deterministic capture route when real-time recording cannot meet the consumer's frame-accuracy requirements. Record the actual producer, template/license, commands, output and fallback reason. Missing required prerequisites block dependent work, not unrelated background construction.

## Plan schema and ownership

The coordinator copies `brief.json.background` selection into state and schedules tasks. The specialist writes background-plan.json, including at least:

```json
{
  "websiteType": "saas",
  "goal": "Make the product clear and increase demo enquiries",
  "technique": "live-3d",
  "referenceImages": [],
  "sceneOwner": "parallax-background-agent",
  "host": "background-only-scene",
  "progressOwner": "shared-scroll-adapter",
  "layers": [
    {"id": "far", "purpose": "quiet spatial context", "depth": -12, "source": "procedural", "owner": "parallax-background-agent"},
    {"id": "mid", "purpose": "product-related forms outside CTA", "depth": -6, "source": "procedural", "owner": "parallax-background-agent"},
    {"id": "near", "purpose": "subtle foreground depth cue", "depth": -2, "source": "procedural", "owner": "parallax-background-agent"}
  ],
  "providers": [
    {"id": "hyperframes", "decision": "skip", "reason": "No footage or film needed"},
    {"id": "remotion", "decision": "skip", "reason": "Live geometry is sufficient"},
    {"id": "motionmaxxing", "decision": "use", "reason": "Depth/pacing guidance and review"},
    {"id": "open3d", "decision": "use", "reason": "Scene techniques and browser/capture validation"},
    {"id": "html-video", "decision": "skip", "availability": "source-verified", "reason": "Live geometry is sufficient; templates/rendering available for useful supporting layers"},
    {"id": "img2threejs", "decision": "skip", "reason": "No reference object needing reconstruction"}
  ],
  "budgets": {"targetFps": 60, "maxDpr": 1.5, "maxDrawCalls": 80, "maxTriangles": 150000, "maxInitialMediaBytes": 2000000},
  "textSafeArea": "Keep the heading and demo CTA on a stable high-contrast surface",
  "reducedMotion": "Static composition with complete readable content",
  "fallback": "Local poster/CSS treatment if WebGL/media is unavailable"
}
```

The example budgets are planning targets, not evidence of performance. Add concrete asset/source references, scroll/camera key ranges, idle/pointer amplitude caps, responsive crop/light rules, trigger/time units, lifecycle and verification paths. All six provider rows are required, with `use`, `skip`, `unavailable` or `blocked` decisions and concrete reasons. Actual used providers need input/output/task/evidence mappings and passing required checks before QA PASS. Do not force three planes if the reference/goal calls for another composition.

A background-only canvas defaults to parallax-background-agent as owner. In a shared Open 3D scene, Open 3D can remain sole renderer/camera/clock owner and the background agent builds named Group/layer factories and material/media modules. The coordinator freezes this boundary in animation-plan.json/plan.md before implementation; match background-plan.json.sceneOwner. No duplicate renderer/camera/RAF, competing scroll smoother or double transform writes. Keep Anime.js/GSAP ownership limited to assigned text/UI properties. Research/design/code can overlap only on disjoint owned files.

## Lifecycle in Designme

1. Briefing infers website type/goal and records background enablement/reference paths. Wave 1 researchers inspect references and supply background-references.md before the plan.
2. Wave 2 background design consumes research/style/motion direction, coordinates motionmaxxing guidance, proposes source assets and any reconstruction. Freeze production/animation ownership after planning and reconstruction handoff. Do not create a cycle: background requirements precede img2threejs; finished models precede scene implementation.
3. Wave 3 implements assigned background modules after asset/model dependencies. Supporting HyperFrames/Remotion clip tasks may run before web assembly; a capture of the website itself waits until page integration.
4. Wave 4 integrates the functional website, resumes the background owner for validation, runs Open 3D site-check/targeted motion capture and motionmaxxing/craft review. If requested, source captures then feed companion-film assembly.
5. Engineering/final QA findings identify actual layer/provider/scene owners and evidence; repair only affected tasks, rerun producer/consumer checks and review the integrated result inside the existing three-loop cap.

## Acceptance

Check layering/occlusion/camera coherence; visible reference fit and honest approximations; text/CTA contrast and non-intercepting background; desktop/tablet/phone and short viewports; pointer/touch, fast/reverse scroll and resize; first paint, media/asset budgets and supported hardware frame performance; reduced-motion initial/change and no-WebGL/context-loss/static fallback; offscreen pause and mount/unmount disposal. Use actual screenshots, site-check reports and targeted motion captures. Missing executable checks are BLOCKED, not a fictional PASS. Verify film clip frame/alpha/color/audio joins only when media/film assets are used. Decorative backgrounds need no semantic focus targets and must never hide essential information.
