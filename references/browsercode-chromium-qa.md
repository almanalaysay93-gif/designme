# Interaction and render verification compatibility entry

The active interaction backend is now [Agent Desktop](agent-desktop-integration.md). Read that contract for installation, desktop-session/OS permission requirements, snapshot refs, retry/disposition handling, evidence, measurement boundaries and blocked prerequisites. The browser-agent role and browser-report.md handoffs remain stable.

Chromium/Playwright and Open 3D site-check/frame-capture still perform browser rendering, exact viewport/DOM/console/network checks and deterministic video/canvas evidence. They are not removed by the interaction-backend replacement. Discover the installed browser executable and record its actual version/path; do not assume a macOS cache path exists on another host or universally disable browser sandboxing.

BrowserCode is an optional preview compatibility target only for a deliverable that requires it. Do not install it as the default interaction backend, require a paid BrowserPod key, or treat its URL/config compatibility as proof of live UI/render success. Agent Desktop is the default user-facing interaction path; do not silently reintroduce the retired agent-browser/browser-use tool.
