# Agent Desktop interaction and verification

Default interactive backend: [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop), Apache-2.0. The existing `browser-agent` role stays stable for research and QA callers; its interaction tool is now `agent-desktop`. This replaces the former agent-browser/browser-use interaction routing. Do not silently reinstall or fall back to those retired interaction tools.

Agent Desktop is a local native accessibility CLI, not a browser engine, DOM evaluator or deterministic video renderer. Chromium/Playwright, Open 3D site-check/frame-capture, img2threejs pass rendering and the film renderers retain their measurement/capture/render responsibilities. BrowserCode can remain an optional preview compatibility check only when requested by the deliverable; it is not an interaction backend or a mandatory installation.

## Installation and prerequisites

Run `bash scripts/install-agent-desktop.sh` from the Designme skill directory. It installs the official npm CLI if missing, verifies `agent-desktop version`, and prints (without applying) the required session/permission follow-up. Also install the official harness skill:

```bash
npx skills add https://github.com/vercel-labs/agent-desktop --skill agent-desktop -g
```

Record the installed version, source, harness-skill path and actual capability checks in `motion-skills-installed.md`. Read the CLI's version-matched docs before the first operation:

```bash
agent-desktop skills get desktop
agent-desktop skills get platform
agent-desktop status
agent-desktop permissions
agent-desktop list-apps
```

Read `agent-desktop <command> --help` before using unfamiliar flags and platform-specific navigation/window/capture operations. No global package installation, version output or installed binary proves access to browser windows.

- macOS needs Accessibility permission; screenshots additionally need Screen Recording. Use `permissions` to report actual state; do not claim grants or silently open permission prompts. Native-headless semantic actions still need an accessible running desktop app.
- Windows operations depend on the target app's integrity level; inspect the current platform docs rather than elevating silently.
- Linux needs the signed-in user's graphical session and working AT-SPI bus. The upstream supported baseline is Ubuntu 24.04+/GNOME, with a glibc 2.35 loader floor. Containers/TTYs/SSH shells without the session may have no apps. X11 and Wayland input/window/screenshot capabilities differ; inspect `status` and version-matched platform docs. Never restart a bus or user's desktop merely to make QA work.

A required desktop check without the session/permission/capability is BLOCKED with its exact prerequisite. Continue independent rendering/measurement work where possible and label its evidence separately; do not report desktop interaction as passed because headless tests passed.

## Observe → act → verify

1. Discover apps/windows using the installed CLI. Select only the task's browser app and exact preview/reference window; record app/window identifiers locally in browser-report.md. Do not operate an unrelated window or rely on a stale title. For navigation, use supported launch arguments or the address/location UI exposed in a fresh snapshot; check current command help instead of guessing URL flags.
2. Take `agent-desktop snapshot --app <actual-app-name> -i` (and a supported `--window-id` when multiple windows match). For dense windows use `--skeleton`, then drill into the region with `--root` from that snapshot. Capture the app-scoped screenshot through the current screenshot interface when visual evidence is needed.
3. Act only on returned, snapshot-qualified refs (`@snapshot_id:eN`). Do not invent refs, use bare @eN, or carry refs across UI changes. Re-read the affected region/window after each action and verify the intended visible/app state, not just `ok: true` delivery.
4. Parse the JSON envelope and action/error dispositions. Retry or substitute only when `disposition.retry` is `safe` (not delivered). Otherwise inspect live state first to avoid duplicate clicks, text or submissions. On STALE_REF/SNAPSHOT_NOT_FOUND snapshot again; on AMBIGUOUS_TARGET narrow the app/window/region or exact role/name. Use supported waits for async state, not arbitrary long sleeps.
5. Ref actions use semantic accessibility calls by default. The official skill permits global `--headed` physical pointer/focus/keyboard input only with explicit user authorization. Do not escalate to it automatically after a semantic failure. If a required hover/drag/parallax-pointer check needs unsupported physical input, record the blocked capability and use independent programmatic test evidence for that behavior where available; do not label it an Agent Desktop check.
6. Browser/canvas accessibility trees may omit decorative 3D geometry. Inspect actual app screenshots and targeted motion captures alongside the tree; a complete accessibility snapshot does not establish correct WebGL appearance, pointer parallax, animation smoothness or color contrast.

Keep snapshots/screenshots/traces scoped to the task app and store raw desktop artifacts locally. They may contain private desktop content; do not commit/upload them as public repository evidence. Do not collect clipboard/notifications or operate other apps unless the task actually requires them.

## Evidence and measurement boundary

Wave 2 supporting browser-agent research navigates reference pages and inspects supplied images through Agent Desktop, with actual screenshot/motion observations and a browser-report.md handoff before dependent Design DNA/background planning. Approximate visual color/font guesses must be labeled estimates; exact computed tokens come from a separately recorded local DOM/Playwright measurement when available.

For integrated QA, use Agent Desktop to observe and exercise accessible navigation, controls, forms, scroll and local preview/player UI; inspect screenshots and verify before/after states. Use a local test-only submission target or stop before a consequential production submission unless the user authorized it. Exact viewport size (including mobile emulation), console/network failures, document overflow, computed styles, renderer counters, reduced-motion media emulation and deterministic captures use the existing Playwright/site-check/render scripts. Resizing an OS window alone does not prove a CSS viewport size. Report which backend produced each artifact; never invent DOM/evaluate/device-emulation commands for Agent Desktop.

Validate desktop/tablet/phone, keyboard/CTA access, reduced-motion/fallbacks and parallax/cursor/scroll behaviors through the appropriate real evidence. Where a native input mode is unavailable or unauthorized, label the unexecuted interaction and its impact. Required missing evidence remains BLOCKED; unrelated checks can proceed. Existing measured performance caveats, one scene/progress owner and renderer determinism rules remain binding.

## Orchestration and repair

Keep browser-agent as a Wave 2 reference prerequisite and resume it with QA after integration. State records `interaction_backend: agent-desktop`, `desktop_status`, target app/window, permission/capability status, desktop evidence, separate measurement evidence and limitations. Only the coordinator writes shared state. The final QA agent compares live output and specialist artifacts against brief/design/plan, then dispatches reproducible findings to actual owners and rechecks integrated fixes within the existing three-loop cap.

browser-report.md and audit.md identify installed version, app/window scope, actual interactions/observations, screenshot/motion artifacts, exact measurement tools, blocked prerequisites and plan compliance. A missing desktop/session check cannot be laundered into PASS by an unrelated screenshot or source review.
