# Open 3D Skills integration

Source: https://github.com/Moh4696/open-3d-skills (MIT). This library supplies specialist techniques, not a second orchestrator. `open-3d-agent` joins Designme's existing dependency and feedback loop when relevant to the approved build.

## Selection and install

During briefing, record `brief.json.open3d` with `enabled`, `skills`, and `reason`. Default `enabled` to false for unrelated/static builds. Recommend relevant skills for 3D landing pages, product explainers, scroll films, alpha video, cursor interactions, and extra 3D QA; the approved brief authorizes the selected scope. Never activate paid generation or invent a new optional approval step for already-authorized work.

When Open 3D is enabled, `find-skills-agent` ensures all eight skills are available so the agent can compose the full library. Install missing skill folders using the existing skills CLI:

```bash
npx skills add Moh4696/open-3d-skills --skill threejs-scene --skill scroll-film --skill motion-assets --skill alpha-cutout --skill cursor-rig --skill exploded-view --skill site-check --skill frame-capture -g
```

Record all eight available skill paths, the applied subset, upstream commit/version, installed paths, dependency versions and commands in `motion-skills-installed.md`. Read each installed `SKILL.md` before invoking bundled scripts. The upstream README lists Node 22.20+ for the installer/checks, Python 3.9+, FFmpeg/ffprobe, and skill-specific Python/Playwright browser dependencies. Install only what the chosen scripts need, in an appropriate environment. Preserve upstream MIT attribution when adapting code/assets.

## Full-library assessment and execution

For every enabled build, read all eight upstream skill entry points and write `open-3d-capabilities.json` with exactly one row per skill. `brief.json.open3d.skills` is the proposed scope; the matrix becomes the execution record. If a useful capability exceeds the approved brief, propose it and mark it `skip` with a reason that records the deferred proposal rather than silently expanding the deliverable. Use this row shape:

```json
{
  "skills": [
    {
      "skill": "threejs-scene",
      "decision": "use",
      "reason": "Approved procedural product hero",
      "tasks": ["open3d-scene"],
      "inputs": ["design-dna.json"],
      "outputs": ["product-scene.js"],
      "checks": ["desktop/tablet/phone and reduced motion"],
      "execution": "pending",
      "evidence": []
    }
  ]
}
```

Allowed `decision` values are `use`, `skip`, `blocked`; `execution` is `pending`, `pass`, `fail`, `blocked`, or `not-applicable`. Record a concrete reason for every skip and the missing prerequisite for every block. Used skills need task/owner mapping, input/output paths, actual execution status and evidence before completion; used rows cannot stay pending at PASS. Update the matrix after integration and each repair. Make the complete skill set available without requiring every effect in every page.

Apply the full depth of each relevant skill:

- `threejs-scene`: reference dimensions, staged blockout/detail, lighting/shadow/shader guidance, quality tiers, camera views, lifecycle and measured budgets.
- `exploded-view`: scene-part inventory, staged assembly/explosion, selected x-ray/section/picking/label interactions, readable labels and camera/scroll synchronization.
- `motion-assets`: concept and asset manifest, a shared style preamble, exact local production steps/prompts where applicable, keyframes before clips, provenance and reproducibility logs; loop checks and outpaint paste-back when needed. Paid generation remains disabled. A needed unavailable asset is blocked, not invented.
- `scroll-film`: local/supplied clip prep, numeric seam checks, progress/frame holds for readable captions, responsive framing, poster-first loading, media budget, Range-capable serving and fast bidirectional scrubbing.
- `alpha-cutout`: plate selection/preparation where needed, per-frame key inspection, stacked-alpha MP4/appropriate fallbacks, mobile sizes, edge inspection against dark/light/brand backgrounds and reduced-motion stills. Do not assume VP9 alpha works in Safari.
- `cursor-rig`: local pose/clip inventory, alignment/tracking, rig-strip assembly, debug contact sheets, fixed-body/neck seam checks, pointer/touch behavior, alt text, idle/reduced-motion behavior and lifecycle cleanup.
- `site-check`: required for enabled animated/3D web builds, even when another agent implements the scene. Check Chromium and WebKit at desktop/tablet/phone widths, reachable states/scroll positions, reduced motion, errors, blank canvas, overflow, loading and renderer metrics; inspect `report.json` and `sheet.jpg`. Missing browsers block their required evidence. Software-rendered frame times do not establish GPU performance.
- `frame-capture`: record a low-FPS timing pass when seams, cursor response, pin release, alpha loops or camera timing need motion evidence. Use ready/virtual-clock hooks and Range serving; inspect critical frames. Use high-quality capture only for a requested recording or a specific unresolved review need, not repeated full renders for static checks.

Compose useful chains: motion-assets planning → procedural scene/exploded view or local clip/key/rig preparation → scroll/alpha/cursor integration → site-check → targeted frame-capture → findings → owner repair → recheck. Asset preparation may proceed before final module assembly, but shared ownership and clocks must be frozen first. Every used skill participates in the same QA/repair cap.

## Ownership map

| Upstream skill | Open 3D specialist contribution | Integration boundary |
| --- | --- | --- |
| `threejs-scene` | Procedural scenes, lighting, quality tiers and geometry | Coordinator assigns one scene owner between open-3d-agent and threejs-agent; one Three.js version, renderer, camera and loop per scene |
| `exploded-view` | Product breakdown, x-ray, labels and picking | Mount in the assigned scene; do not animate properties assigned to another engine |
| `scroll-film` | Scroll-to-frame media layers and caption holds | Use supplied/local clips; one scroll-progress owner; explicit mobile/loading/reduced-motion fallback |
| `alpha-cutout` | Local keying, alpha-video player and browser formats | Supplied/local clips only; check Chromium and WebKit where supported |
| `cursor-rig` | Local pose-grid preparation and pointer-following layer | Supplied/local pose assets; touch/keyboard alternatives and cleanup |
| `site-check` | Browser, overflow, canvas and performance evidence | Supplements existing QA; failures return to the owning specialist |
| `frame-capture` | Optional review recordings/contact-sheet evidence | Does not replace the selected final renderer or bypass final QA |
| `motion-assets` | Concept/asset planning, consistent style, local production, provenance/logs and loop/outpaint repair | Paid/cloud generation remains disabled under Designme's free-only policy |

The starter pins Three.js r169 and includes CDN imports, a frame loop and recording hooks. Adapt individual techniques to the chosen project's version, bundle local dependencies for offline rendering, and integrate lifecycle instead of pasting a competing app. For shared scenes, threejs-agent may provide a model/geometry factory while open-3d-agent owns the scene, or vice versa; record the exact boundary before either writes code. When img2threejs is selected, consume its approved deterministic model factory; do not rebuild it independently. Anime.js remains the default for landing-page words and DOM elements.

## Dependency and repair loop

1. Briefing identifies `open3d.enabled`, selected skills and scope; Wave 1 research/find-skills gathers references and prerequisites.
2. In Wave 2, open-3d-agent writes its plan after relevant design inputs. The coordinator/superlite-agent freezes file, scene, clock, target/property ownership and dependencies before Wave 3. If assets/models are not ready, block their consumers only.
3. In Wave 3, the specialist implements assigned modules. For video, wait for the canonical beat map and use the selected renderer's deterministic clock; for web, use the declared scroll/interaction clock. No duplicate RAF loops for the same scene.
4. After coordinator integration in Wave 4, resume the same specialist for site-check/validation and evidence handoff to motion-craft and QA. UI/code ownership remains disjoint; the coordinator owns shared state, dependency manifests and integration entry points.
5. Final QA reviews plan compliance, visible design, loading, mobile/reduced motion, resource disposal, measured budgets and actual evidence. Findings identify owner, file/selector or timestamp, reproduction, expected behavior and evidence. Dispatch only that owner, rerun affected checks, then re-audit; retain the existing three-loop cap and engineering review before final PASS.

## Capture boundary

For an existing HyperFrames, Remotion or motionmaxxing film, frame-capture provides review evidence only; final delivery stays with the approved renderer. For an explicitly requested recording of a web-only build, the coordinator may select `frame-capture` as the sole capture backend in `renderer-decision.md` and state; skip the three film renderers. Use the upstream virtual clock/ready hooks, check repeated captures, expected dimensions/FPS/duration and `ffprobe`, and verify any separately added local audio against that clock. This exception does not make frame-capture the default film renderer. Web-only builds without a recording keep `video_renderer: null`.

## Deliverables

`open-3d-capabilities.json`, `open-3d-plan.md` and `open-3d-validation.md` are required when enabled; include `open-3d-assets.md` and provenance/production logs when assets are involved, alongside assigned code/assets, installed-source records, browser reports/contact sheets and targeted repair evidence. Missing executable verification is BLOCKED; a written checklist alone cannot establish PASS.
