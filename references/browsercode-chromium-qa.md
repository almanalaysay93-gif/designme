# BrowserCode and Chromium QA Verification

`qa-anti-slop-agent` and `browser-agent` use local Chromium and `leaningtech/browsercode` to inspect live rendered output, verify design accuracy against the brief, and confirm that every agent followed `plan.md`.

## Local installations

1. **Leaning Technologies BrowserCode (`leaningtech/browsercode`):**
   - Cloned at `C:/Users/ORGANTRANSPLANT/.agents/tools/leaningtech-browsercode` from `https://github.com/leaningtech/browsercode` (Apache-2.0, commit `48d202c`).
   - Provides the WebAssembly BrowserPod IDE and preview grammar (`https://browsercode.io/ide/github/<owner>/<repo>/tree/<ref>/` and `/embed?framework=vite&view=preview`).
   - Also paired with the local `bcode` CLI (`C:/Users/ORGANTRANSPLANT/.bcode/bin/bcode.exe`) when autonomous CDP inspection is requested.
2. **Chromium (`chromium/chromium` runtime):**
   - Installed locally at `C:/Users/ORGANTRANSPLANT/AppData/Local/ms-playwright/chromium-1243/chrome-win64/chrome.exe` and `C:/Users/ORGANTRANSPLANT/AppData/Local/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-win64/chrome-headless-shell.exe`.
   - Do not run `git clone https://github.com/chromium/chromium` during a task because the Chromium C++ source repository exceeds 67 GB.
   - Always pass `--no-sandbox` when launching `chrome.exe` or `chrome-headless-shell.exe` from a Windows child process or Playwright script.

## QA verification workflow

`qa-anti-slop-agent` must run these checks before issuing a `PASS` verdict:

1. **Boot and render in Chromium:**
   - Open the built HTML composition, Vite preview, or video output in local Chromium (`chrome.exe` or `chrome-headless-shell.exe` with `--no-sandbox`).
   - Capture viewport screenshots at desktop (`1440x900`) and mobile (`390x844`) or at the brief target aspect ratio.
   - Inspect computed styles, console errors, network failures, and layout overflow (`document.documentElement.scrollWidth <= window.innerWidth`).
2. **BrowserCode sandbox preview check (when applicable):**
   - For web apps or GitHub-backed Vite/React/Next deliverables compatible with BrowserCode constraints (HTTPS only, no native binary dependencies), verify the preview route or embed config against `C:/Users/ORGANTRANSPLANT/.agents/tools/leaningtech-browsercode` rules (`Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: require-corp`).
   - Do not require a paid `VITE_API_KEY` from `browserpod.io`. Use free local Chromium rendering as the primary authority and free `browsercode.io` URL grammar when a public GitHub branch exists.
3. **Design accuracy check ("Did it make the right design?"):**
   - Compare the live Chromium screenshots against `brief.json`, `design-dna.json`, `style-spec.md`, `shot-plan.md`, and `browser-report.md`.
   - Verify palette tokens, typography, hero beat, camera motion, and anti-slop exclusions.
4. **Plan compliance check ("Did the agents follow the plan?"):**
   - Compare the workspace artifacts against `plan.md` and `orchestrator.json`.
   - Confirm that every scheduled agent in Waves 1 through 4 wrote its required deliverable file and respected renderer exclusivity and the free-only policy.
   - Record the verification results in `audit.md` under `## Chromium & BrowserCode Plan Verification`.
