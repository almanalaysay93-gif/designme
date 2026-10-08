# Orchestrator State

File: orchestrator.json (written by main skill, updated by each agent)

{
  "brief_version": 1,
  "waves": {
    "wave1": {"design-dna-agent": "pending", "memory-agent": "pending", "browser-agent": "pending", "find-skills-agent": "pending"},
    "wave2": {"motion-design-agent": "pending", "superpowers-agent": "pending"},
    "wave3": {"gsap-agent": "pending", "threejs-agent": "pending", "genjutsu-agent": "pending", "taste-gsd-agent": "pending"},
    "wave4": {"hyperframes-agent": "pending"}
  },
  "qa_loops": 0,
  "max_loops": 3,
  "cost_estimate": "$0",
  "deterministic_hash": null
}

Each agent updates its status to pass/fail/slop.
