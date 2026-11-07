# Orchestrator State

File: `orchestrator.json` (written and updated by the coordinator from specialist handoffs)

```json
{
  "brief_version": 9,
  "execution_adapter": "superlite",
  "coordinator": "designme",
  "tasks": [],
  "engineering_review": "pending",
  "subagent_count": 32,
  "waves": {
    "wave1": {
      "planner-griller": "pending"
    },
    "wave1_5": {
      "speckit-theme-builder": "blocked-until-approved-brief",
      "speckit-theme-reviewer": "blocked-until-complete-builder-baseline",
      "review_attempts": 0,
      "max_review_attempts": 2
    },
    "wave2": {
      "design-dna-agent": "pending",
      "motion-design-agent": "pending",
      "supporting_tasks": []
    },
    "wave3": {
      "gsap-agent": "pending",
      "threejs-agent": "pending",
      "hyperframes-agent": "pending",
      "motion-a11y-agent": "pending",
      "supporting_tasks": []
    },
    "wave4": {
      "genjutsu-agent": "pending",
      "render-perf-budget-agent": "pending",
      "qa-anti-slop-agent": "pending",
      "token-handoff-exporter": "blocked-until-final-qa-pass",
      "supporting_tasks": []
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
  },
  "supporting_agent_status": {
    "memory-agent": "pending",
    "browser-agent": "pending",
    "find-skills-agent": "pending",
    "prompt-reference-agent": "pending",
    "opus5-videos-agent": "skipped-unless-approved",
    "remotion-agent": "pending-assessment",
    "motionmaxxing-agent": "pending-assessment",
    "open-3d-agent": "pending-if-assigned",
    "visual-style-agent": "pending",
    "ui-ux-pro-max-agent": "skipped-unless-approved",
    "img2threejs-agent": "skipped-unless-approved",
    "launch-director-agent": "pending",
    "superlite-agent": "pending",
    "parallax-background-agent": "pending-assessment",
    "animejs-agent": "pending-if-assigned",
    "beat-sync-agent": "pending",
    "taste-gsd-agent": "pending",
    "hairline-agent": "skipped-unless-approved",
    "motion-craft-agent": "pending"
  },
  "motion_a11y": {
    "status": "pending",
    "report": null,
    "reduced_timeline": null,
    "source_revision": null
  },
  "performance": {
    "status": "pending",
    "budget": null,
    "report": null,
    "source_revision": null
  },
  "handoff": {
    "status": "blocked-until-final-qa-pass",
    "version": null,
    "path": null,
    "manifest": null,
    "consumer_contract": null,
    "source_revision": null
  },
  "speckit": {
    "status": "blocked-until-approved-brief",
    "directory": null,
    "version": null,
    "brief_version": null,
    "baseline_hashes": {},
    "review_report": null,
    "review_verdict": null,
    "open_questions": [],
    "risk_acceptance": null,
    "wave2_ready": false
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

The current core wave order is defined in SKILL.md and manifest.json.wave_order. Retained specialists run as dependency tasks in each wave's supporting_tasks; supporting_agent_status tracks their existing contracts. Wave 4 core gates are serial: Genjutsu thesis → performance → final QA → exporter last. Accessibility/performance/QA reports and handoff must match the same tested source revision; source changes invalidate affected statuses. No exporter task is ready while any required gate fails or evidence is missing.

Wave 1.5 is a mandatory theme-only lock/review gate between approved planner input and Wave 2. Track review_attempts separately from the later three-loop implementation repair cap: max two reviewer attempts, second FAIL requires user brief-fix or explicit risk decision. A reset requires a newly versioned user-updated input. Actual PASS or a scoped executable risk authorization can resolve readiness; never invent missing answers, relabel review FAIL, or dispatch Wave 2 while wave2_ready is false. Root execution plans remain distinct from speckit-theme-design/plan.md.
