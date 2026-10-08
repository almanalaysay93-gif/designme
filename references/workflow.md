# Workflow Diagram

1. User /hypercraft -> planner-griller (grill session)
2. brief.json approved -> parallel spawn 6 domain agents
3. domain agents -> files
4. hyperframes-agent assembles composition
5. qa-anti-slop-agent checks -> if fail, feedback loop to specific agent (max 3)
6. render MP4 + audit.md
