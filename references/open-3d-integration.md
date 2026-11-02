# Open 3D Skills integration

Source: https://github.com/Moh4696/open-3d-skills (MIT). This library supplies specialist techniques, not a second orchestrator. `open-3d-agent` joins Designme's existing dependency and feedback loop when relevant to the approved build.

## Selection and install

During briefing, record `brief.json.open3d` with `enabled`, `skills`, and `reason`. Default `enabled` to false for unrelated/static builds. Recommend relevant skills for 3D landing pages, product explainers, scroll films, alpha video, cursor interactions, and extra 3D QA; the approved brief authorizes the selected scope. Never activate paid generation or invent a new optional approval step for already-authorized work.

`find-skills-agent` checks installed skills and installs only the selected subset with the existing skills CLI, for example:

```bash
npx skills add Moh4696/open-3d-skills --skill threejs-scene --skill exploded-view --skill site-check -g
```

Record the selected skills, upstream commit/version, installed paths, dependency versions and commands in `motion-skills-installed.md`. Read each installed `SKILL.md` before invoking bundled scripts. The upstream README lists Node 22.20+ for the installer/checks, Python 3.9+, FFmpeg/ffprobe, and skill-specific Python/Playwright browser dependencies. Install only what the chosen scripts need, in an appropriate environment. Preserve upstream MIT attribution when adapting code/assets.

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
| `motion-assets` | Local media analysis helpers only when needed | Paid/cloud generation remains disabled under Designme's free-only policy |

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

`open-3d-plan.md` and `open-3d-validation.md` are required when enabled, alongside assigned code/assets, installed-source records, browser reports/contact sheets and targeted repair evidence. Missing executable verification is BLOCKED; a written checklist alone cannot establish PASS.
