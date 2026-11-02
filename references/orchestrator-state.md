# Orchestrator State

File: `orchestrator.json` (written and updated by the coordinator from specialist handoffs)

```json
{
  "brief_version": 9,
  "execution_adapter": "superlite",
  "coordinator": "designme",
  "tasks": [],
  "engineering_review": "pending",
  "subagent_count": 27,
  "waves": {
    "wave1": {
      "design-dna-agent": "pending",
      "memory-agent": "pending",
      "browser-agent": "pending",
      "find-skills-agent": "pending",
      "prompt-reference-agent": "pending",
      "opus5-videos-agent": "skipped-unless-approved"
    },
    "wave2": {
      "remotion-agent": "pending-assessment",
      "motionmaxxing-agent": "pending-assessment",
      "open-3d-agent": "pending-if-assigned",
      "visual-style-agent": "pending",
      "ui-ux-pro-max-agent": "skipped-unless-approved",
      "img2threejs-agent": "skipped-unless-approved",
      "motion-design-agent": "pending",
      "launch-director-agent": "pending",
      "superlite-agent": "pending",
      "parallax-background-agent": "pending-assessment"
    },
    "wave3": {
      "remotion-agent": "pending-assessment",
      "open-3d-agent": "pending-if-assigned",
      "animejs-agent": "pending-if-assigned",
      "beat-sync-agent": "pending",
      "gsap-agent": "pending",
      "threejs-agent": "pending",
      "genjutsu-agent": "pending",
      "taste-gsd-agent": "pending",
      "parallax-background-agent": "pending-assessment"
    },
    "wave4": {
      "open-3d-agent": "pending-if-assigned",
      "hyperframes-agent": "pending",
      "remotion-agent": "pending-assessment",
      "hairline-agent": "skipped-unless-approved",
      "motionmaxxing-agent": "pending-assessment",
      "motion-craft-agent": "pending",
      "parallax-background-agent": "pending-assessment"
    },
    "qa": {
      "qa-anti-slop-agent": "pending"
    }
  },
  "visual_style": {
    "primary": null,
    "secondary": null,
    "approved": false,
    "style_spec": null
  },
  "motion_skill_packs": [],
  "motion_skill_pack_approval": false,
  "video_renderer": "hyperframes",
  "production_plan": null,
  "production": {
    "deliverable": "video",
    "profile": "standard",
    "finalRenderer": "hyperframes",
    "specialists": {
      "remotion-agent": {
        "mode": "contribute",
        "reason": "Assess supporting sequences"
      },
      "motionmaxxing-agent": {
        "mode": "review",
        "reason": "Motion planning and craft review"
      },
      "open-3d-agent": {
        "mode": "contribute",
        "reason": "Assess scenes, media and capture"
      },
      "parallax-background-agent": {
        "mode": "contribute",
        "reason": "Assess goal-led multilayer backgrounds"
      }
    }
  },
  "animation": {
    "engine": null,
    "reason": "",
    "textResearch": false,
    "reducedMotion": "show-final-state"
  },
  "open3d": {
    "enabled": false,
    "skills": [],
    "reason": "",
    "capabilities": null,
    "assets": null,
    "plan": null,
    "validation": null
  },
  "animation_plan": null,
  "word_animation_references": null,
  "optional_agents": {
    "hairline-agent": {
      "requested": false,
      "needed": false,
      "approved": false,
      "reason": ""
    },
    "opus5-videos-agent": {
      "requested": false,
      "needed": false,
      "approved": false,
      "reason": ""
    },
    "ui-ux-pro-max-agent": {
      "requested": false,
      "needed": false,
      "approved": false,
      "reason": ""
    },
    "img2threejs-agent": {
      "requested": false,
      "needed": false,
      "approved": false,
      "reason": ""
    }
  },
  "qa_verification": {
    "design_verified": false,
    "plan_verified": false,
    "interaction_backend": "agent-desktop",
    "desktop_status": "unchecked",
    "desktop_version": null,
    "target_app": null,
    "target_window": null,
    "permissions": {},
    "capabilities": {},
    "desktop_evidence": [],
    "measurement_tools": [],
    "measurement_evidence": [],
    "limitations": [],
    "optional_preview": null
  },
  "qa_loops": 0,
  "max_loops": 3,
  "cost_estimate": "$0",
  "free_only": true,
  "audio": {
    "loudness_lufs": null,
    "true_peak_dbfs": null,
    "drift_ms": null
  },
  "deterministic_hash": null,
  "background": {
    "enabled": false,
    "websiteType": null,
    "goal": null,
    "referenceImages": [],
    "reason": "",
    "plan": null,
    "validation": null,
    "htmlVideoAvailability": "source-verified"
  }
}
```

The griller fills `optional_agents` from the approved `brief.json`. No optional agent may start while `approved` is false. `video_renderer` records the final owner (`hyperframes` by default, explicit `remotion`, `motionmaxxing`, `frame-capture`, or null for websites); normal specialists may contribute intermediate assets regardless of the final owner. Keep it equal to `production.finalRenderer`. `opus5-videos-agent` and `img2threejs-agent` may run beside the renderer when approved. The coordinator records each agent's status to `pass`, `fail`, or `slop`.

The coordinator records each task ID, dependencies, owner, allowed files, status and
evidence paths in `tasks`. Only the coordinator writes shared state; specialists
return status updates. Fresh engineering review must pass before final QA.

For web-only landing pages, set `video_renderer` to null and skip unnecessary final-video tasks, retaining normal specialist assessment and useful contributions. Copy `animation` from the brief; record `animation-plan.json` and `word-animation-references.md` paths when applicable. Anime.js defaults on for animated landing pages; mark animation roles without target/property assignments skipped with a reason.

Copy `open3d` selection from the approved brief; the coordinator tracks its planning, implementation and integrated validation tasks separately in `tasks`, with dependencies, owned files, evidence paths and existing QA retry counts. If disabled, mark all open-3d-agent phase entries skipped with a reason. An explicitly requested web recording may use `video_renderer: "frame-capture"` only under the [capture boundary](open-3d-integration.md); skip all film renderers in that case.

Normal specialist tasks follow `references/normal-motion-orchestration.md`; legacy Remotion/motionmaxxing optional flags never suppress HyperFrames or block contribution dispatch. Translate an explicit standalone renderer request into production.finalRenderer. Website captures depend on an integrated ready page, and their consuming final film depends on completed capture assets.

Track background research → layer/reconstruction plan → assigned model/assets → background implementation → integration → validation/repairs as dependency tasks. Keep provider availability/evidence in background-plan.json and state; missing providers are never recorded as executed.

Agent Desktop capability/status fields describe observed native UI access, not binary installation alone. Required unavailable session/permission/input checks remain BLOCKED; record separate headless measurements and exact tools without substituting them for missing desktop evidence.
