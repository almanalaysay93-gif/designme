# Orchestrator State

File: `orchestrator.json` (written by main skill, updated by each agent)

```json
{
  "brief_version": 2,
  "waves": {
    "wave1": {"design-dna-agent": "pending", "memory-agent": "pending", "browser-agent": "pending", "find-skills-agent": "pending", "prompt-reference-agent": "pending"},
    "wave2": {"motion-design-agent": "pending", "launch-director-agent": "pending", "superpowers-agent": "pending"},
    "wave3": {"beat-sync-agent": "pending", "gsap-agent": "pending", "threejs-agent": "pending", "genjutsu-agent": "pending", "taste-gsd-agent": "pending"},
    "wave4": {"hyperframes-agent": "pending", "remotion-agent": "skipped-unless-requested", "hairline-agent": "skipped-unless-requested", "motion-craft-agent": "pending"},
    "qa": {"qa-anti-slop-agent": "pending"}
  },
  "qa_loops": 0,
  "max_loops": 3,
  "subagent_count": 19,
  "cost_estimate": "$0",
  "free_only": true,
  "deterministic_hash": null,
  "audio": {"loudness_lufs": null, "true_peak_dbfs": null, "drift_ms": null}
}
```

Each agent updates its status to `pass`, `fail`, or `slop`. The canonical timeline and final render hash are written before QA closes the run.
