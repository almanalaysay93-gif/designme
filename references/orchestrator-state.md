# Orchestrator State

File: `orchestrator.json` (written by main skill, updated by each agent)

```json
{
  "brief_version": 5,
  "subagent_count": 20,
  "waves": {
    "wave1": {"design-dna-agent": "pending", "memory-agent": "pending", "browser-agent": "pending", "find-skills-agent": "pending", "prompt-reference-agent": "pending"},
    "wave2": {"motion-design-agent": "pending", "launch-director-agent": "pending", "superpowers-agent": "pending"},
    "wave3": {"beat-sync-agent": "pending", "gsap-agent": "pending", "threejs-agent": "pending", "genjutsu-agent": "pending", "taste-gsd-agent": "pending"},
    "wave4": {"hyperframes-agent": "pending", "remotion-agent": "skipped-unless-approved", "hairline-agent": "skipped-unless-approved", "motionmaxxing-agent": "skipped-unless-approved", "motion-craft-agent": "pending"},
    "qa": {"qa-anti-slop-agent": "pending"}
  },
  "motion_skill_packs": [],
  "motion_skill_pack_approval": false,
  "optional_agents": {
    "remotion-agent": {"requested": false, "needed": false, "approved": false, "reason": ""},
    "hairline-agent": {"requested": false, "needed": false, "approved": false, "reason": ""},
    "motionmaxxing-agent": {"requested": false, "needed": false, "approved": false, "reason": ""}
  },
  "qa_loops": 0,
  "max_loops": 3,
  "cost_estimate": "$0",
  "free_only": true,
  "audio": {"loudness_lufs": null, "true_peak_dbfs": null, "drift_ms": null},
  "deterministic_hash": null
}
```

The griller fills `optional_agents`, including the motionmaxxing decision, from the approved `brief.json`. No optional agent may start while `approved` is false. Each agent updates its status to `pass`, `fail`, or `slop`.
