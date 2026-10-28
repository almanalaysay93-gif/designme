# img2threejs Integration

`img2threejs-agent` integrates [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) (Apache-2.0, v2.0.0) into `/designme` as an optional Wave 2 reconstruction agent.
The canonical checkout lives at `C:/Users/ORGANTRANSPLANT/.agents/skills/img2threejs` with junctions across Claude Code, Codex, Grok, Antigravity, Gemini, and OpenCode.

## When to select `img2threejs-agent`

Recommend `img2threejs-agent` during `planner-griller` when the user supplies a 2D reference image of an object, product, prop, or character and wants a custom 3D model built in code without an existing `.glb` file.
Recommend skipping `img2threejs-agent` when the project has no 3D hero object, uses existing `.glb` assets, or needs only abstract Three.js particles and shaders.

## Wave handoff

1. `img2threejs-agent` runs in Wave 2 after `brief.json` approval.
2. `img2threejs-agent` gates every step through `forge/state.py` and `forge/next.py` using Python 3.10+ standard library tools.
3. `img2threejs-agent` outputs `sculpt-spec.json`, `.img2threejs/state.json`, per-pass Chromium screenshots in `img2threejs-passes/`, and a deterministic `create<ObjectName>Model(spec, options)` module.
4. `threejs-agent` in Wave 3 imports `create<ObjectName>Model(spec, options)`, mounts the `THREE.Group` into the scene, and wires its named pivots and sockets to the seek-safe timeline.

## Free-only boundaries

- Use only the built-in `generic` and `character` profiles.
- Do not install or call paid plugins from `@img2threejs/img2`.
- Do not call Tripo, Hyper3D, CharacterGen, or any external neural mesh service.
- Use local Chromium (`C:/Users/ORGANTRANSPLANT/AppData/Local/ms-playwright/chromium-1243/chrome-win64/chrome.exe`) via Playwright for pass screenshot captures.

## QA checks

When `img2threejs-agent` is active, `qa-anti-slop-agent` verifies these items:

- `.img2threejs/state.json` exists and shows completed passes from `blockout` through `optimization`.
- `sculpt-spec.json` contains a complete `detailInventory` and `qualityContract`.
- `img2threejs-passes/` contains real Chromium comparison screenshots for each pass.
- `create<ObjectName>Model` uses deterministic noise seeds and disposes geometries and materials cleanly.
- `threejs-agent` mounts the generated `THREE.Group` without `Math.random()` or `Date.now()`.
