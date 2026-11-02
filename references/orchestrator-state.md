# Orchestrator State

File: `orchestrator.json` (written and updated by the coordinator from specialist handoffs)

```json
{
  "brief_version": 9,
  "execution_adapter": "superlite",
  "coordinator": "designme",
  "tasks": [],
  "engineering_review": "pending",
  "subagent_count": 26,
  "waves": {
    "wave1": {"design-dna-agent": "pending", "memory-agent": "pending", "browser-agent": "pending", "find-skills-agent": "pending", "prompt-reference-agent": "pending", "opus5-videos-agent": "skipped-unless-approved"},
    "wave2": {"open-3d-agent": "pending-if-assigned", "visual-style-agent": "pending", "ui-ux-pro-max-agent": "skipped-unless-approved", "img2threejs-agent": "skipped-unless-approved", "motion-design-agent": "pending", "launch-director-agent": "pending", "superlite-agent": "pending"},
    "wave3": {"open-3d-agent": "pending-if-assigned", "animejs-agent": "pending-if-assigned", "beat-sync-agent": "pending", "gsap-agent": "pending", "threejs-agent": "pending", "genjutsu-agent": "pending", "taste-gsd-agent": "pending"},
    "wave4": {"open-3d-agent": "pending-if-assigned", "hyperframes-agent": "pending", "remotion-agent": "skipped-unless-approved", "hairline-agent": "skipped-unless-approved", "motionmaxxing-agent": "skipped-unless-approved", "motion-craft-agent": "pending"},
    "qa": {"qa-anti-slop-agent": "pending"}
  },
  "visual_style": {"primary": null, "secondary": null, "approved": false, "style_spec": null},
  "motion_skill_packs": [],
  "motion_skill_pack_approval": false,
  "video_renderer": "hyperframes",
  "animation": {"engine": null, "reason": "", "textResearch": false, "reducedMotion": "show-final-state"},
  "open3d": {"enabled": false, "skills": [], "reason": "", "plan": null, "validation": null},
  "animation_plan": null,
  "word_animation_references": null,
  "optional_agents": {
    "remotion-agent": {"requested": false, "needed": false, "approved": false, "reason": ""},
    "hairline-agent": {"requested": false, "needed": false, "approved": false, "reason": ""},
    "motionmaxxing-agent": {"requested": false, "needed": false, "approved": false, "reason": ""},
    "opus5-videos-agent": {"requested": false, "needed": false, "approved": false, "reason": ""},
    "ui-ux-pro-max-agent": {"requested": false, "needed": false, "approved": false, "reason": ""},
    "img2threejs-agent": {"requested": false, "needed": false, "approved": false, "reason": ""}
  },
  "qa_verification": {
    "chromium_binary": "~/Library/Caches/ms-playwright/chromium-1248/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing",
    "browsercode_repo": "~/.agents/tools/leaningtech-browsercode",
    "design_verified": false,
    "plan_verified": false
  },
  "qa_loops": 0,
  "max_loops": 3,
  "cost_estimate": "$0",
  "free_only": true,
  "audio": {"loudness_lufs": null, "true_peak_dbfs": null, "drift_ms": null},
  "deterministic_hash": null
}
```

The griller fills `optional_agents` from the approved `brief.json`. No optional agent may start while `approved` is false. `video_renderer` is `hyperframes`, `remotion`, or `motionmaxxing`. The other video agents stay skipped. `opus5-videos-agent` and `img2threejs-agent` may run beside the renderer when approved. The coordinator records each agent's status to `pass`, `fail`, or `slop`.

The coordinator records each task ID, dependencies, owner, allowed files, status and
evidence paths in `tasks`. Only the coordinator writes shared state; specialists
return status updates. Fresh engineering review must pass before final QA.

For web-only landing pages, set `video_renderer` to null and skip video-render tasks. Copy `animation` from the brief; record `animation-plan.json` and `word-animation-references.md` paths when applicable. Anime.js defaults on for animated landing pages; mark animation roles without target/property assignments skipped with a reason.

Copy `open3d` selection from the approved brief; the coordinator tracks its planning, implementation and integrated validation tasks separately in `tasks`, with dependencies, owned files, evidence paths and existing QA retry counts. If disabled, mark all open-3d-agent phase entries skipped with a reason. An explicitly requested web recording may use `video_renderer: "frame-capture"` only under the [capture boundary](open-3d-integration.md); skip all film renderers in that case.
