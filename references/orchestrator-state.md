# Orchestrator State

File: `orchestrator.json` (written and updated by the coordinator from specialist handoffs)

```json
{
  "brief_version": 8,
  "execution_adapter": "superlite",
  "coordinator": "designme",
  "tasks": [],
  "engineering_review": "pending",
  "subagent_count": 23,
  "waves": {
    "wave1": {"design-dna-agent": "pending", "memory-agent": "pending", "browser-agent": "pending", "find-skills-agent": "pending", "prompt-reference-agent": "pending", "opus5-videos-agent": "skipped-unless-approved"},
    "wave2": {"visual-style-agent": "pending", "ui-ux-pro-max-agent": "skipped-unless-approved", "motion-design-agent": "pending", "launch-director-agent": "pending", "superlite-agent": "pending"},
    "wave3": {"beat-sync-agent": "pending", "gsap-agent": "pending", "threejs-agent": "pending", "genjutsu-agent": "pending", "taste-gsd-agent": "pending"},
    "wave4": {"hyperframes-agent": "pending", "remotion-agent": "skipped-unless-approved", "hairline-agent": "skipped-unless-approved", "motionmaxxing-agent": "skipped-unless-approved", "motion-craft-agent": "pending"},
    "qa": {"qa-anti-slop-agent": "pending"}
  },
  "visual_style": {"primary": null, "secondary": null, "approved": false, "style_spec": null},
  "motion_skill_packs": [],
  "motion_skill_pack_approval": false,
  "video_renderer": "hyperframes",
  "optional_agents": {
    "remotion-agent": {"requested": false, "needed": false, "approved": false, "reason": ""},
    "hairline-agent": {"requested": false, "needed": false, "approved": false, "reason": ""},
    "motionmaxxing-agent": {"requested": false, "needed": false, "approved": false, "reason": ""},
    "opus5-videos-agent": {"requested": false, "needed": false, "approved": false, "reason": ""},
    "ui-ux-pro-max-agent": {"requested": false, "needed": false, "approved": false, "reason": ""}
  },
  "qa_loops": 0,
  "max_loops": 3,
  "cost_estimate": "$0",
  "free_only": true,
  "audio": {"loudness_lufs": null, "true_peak_dbfs": null, "drift_ms": null},
  "deterministic_hash": null
}
```

The griller fills `optional_agents` from the approved `brief.json`. No optional agent may start while `approved` is false. `video_renderer` is `hyperframes`, `remotion`, or `motionmaxxing`. The other video agents stay skipped. `opus5-videos-agent` may run beside the renderer; it only writes a prompt brief. The coordinator records each agent's status to `pass`, `fail`, or `slop`.

The coordinator records each task ID, dependencies, owner, allowed files, status and
evidence paths in `tasks`. Only the coordinator writes shared state; specialists
return status updates. Fresh engineering review must pass before final QA.
