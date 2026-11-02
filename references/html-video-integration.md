# html-video local provider

Verified source: https://github.com/nexu-io/html-video (singular), Apache-2.0, inspected at `c414ecc07f795add03807d5d9ce4baefd807cea2` on 2026-11-02. Preserve LICENSE, template metadata, ATTRIBUTIONS.md and templates/NOTICE.md when adapting source/assets. Source inspection establishes capabilities, not a successful installed render.

## Role and capability discovery

Designme remains the sole coordinator. Use html-video as a local template/source and assigned intermediate-asset provider for parallax-background-agent, HyperFrames or Remotion. Do not start another studio agent loop or delegate to a CLI/model backend merely to render supplied code; never invoke paid MiniMax soundtrack or Anthropic/other provider generation. Optional network source fetching is unnecessary for local assets.

The README describes HyperFrames as shipped and Remotion as planned, but the inspected source contains `packages/adapter-remotion` and CLI context registers it conditionally through `remotionInstalled()`. `list-engines` and actual validated source/dependency availability take precedence over stale README status. No guessed engine support; do not claim Manim/Motion Canvas/Revideo are installed.

- Templates declare source entry, input schema, engine/version, output constraints and per-template license/provenance in `template.html-video.yaml`. Inspect metadata and relevant template SKILL.md/source before reuse. Choose by site goal, not by copying generic liquid-gradient hero styling; preserve Designme's selected visual language.
- `packages/adapter-hyperframes/src/index.ts` exports `adapter`/default with validate/render/renderToHtml. Its render path records with Playwright recordVideo in real time, then FFmpeg encodes H.264/yuv420p; fixed FPS metadata alone does not prove frame-exact deterministic animation. Do not assume alpha output from MP4 or that advertised metadata proves a capability.
- `renderToHtml` produces a preview/variable injection and placeholder poster in the inspected implementation. Inspect the actual HTML and variable application; do not treat the generated SVG placeholder as a real scene screenshot or final asset.
- Use template techniques/source adapted into the background's canonical `update({progress,timeSeconds,pointer})` module when a live/deterministic layer is required. For time-critical footage, use a tested deterministic host/capture adapter or locally reauthor the assigned source under HyperFrames/Remotion; do not claim real-time recording passes Designme's repeatability gate without actual checks.

## Install when assigned

From the Designme skill root, run `bash scripts/install-html-video.sh` to download/reuse an official checkout at `~/.agents/tools/html-video` (override `DESIGNME_HTML_VIDEO_REPO_DIR`). The helper does not install dependencies, start agents or render. Record source path and commit. Check prerequisites (Node 20+, pnpm 9+, Chromium/Playwright and FFmpeg; inspect the installed source for any newer requirements). In that checkout, the documented build commands are:

```bash
pnpm install
pnpm -r build
node packages/cli/dist/bin.js doctor
node packages/cli/dist/bin.js list-engines
node packages/cli/dist/bin.js search-templates --intent "subtle product background" --top 3
```

Read the installed source/CLI help first; record lockfile and commands. Use isolated local dependencies and respect any engine license eligibility under Designme's free-only policy. Do not request paid-service keys or use an agent backend. Missing required prerequisites block assigned tasks; availability in background-plan.json progresses from `source-verified` to `installed` to `render-verified` only with evidence.

CLI `project-create`, `project-add-asset`, `project-set-template`, `project-set-vars`, `project-preview` and `project-render` are implemented in the inspected source. Derive their exact inputs/output project IDs from current help/JSON output; never guess IDs or template variable names. A direct local EngineAdapter call may be appropriate after reading current types. For fixed-duration assets, use actual `RenderConfig.durationMode: explicit` where supported and verify resulting duration; do not rely on automatic extension. Never call studio generation/audio endpoints in this integration.

## Asset and validation contract

Every assigned output has a production-plan.json producer/source/template/engine/version record, dimensions, FPS, duration/frame count, alpha/background/color policy, audio policy, ready state and evidence. Keep output local; ship a website layer's poster/mobile/reduced-motion fallback and byte budget. Avoid duplicate audio and runtime copies of complete template apps. Verify actual first/last/peak frames, loop seams, alpha edges/decoding and text-safe contrast, along with ffprobe and repeated capture/seek checks required by the consumer.

If direct html-video capture is unsuitable for required frame accuracy, its template/source can still be used while the recorded producer accurately names the deterministic reauthoring/capture route. Report fallback reasons; do not label a reauthored clip an html-video render. Source inspection or a clone alone is never render verification. This provider does not change the one-final-owner-per-deliverable rule.
