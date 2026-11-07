#!/usr/bin/env python3
"""Check instruction/metadata consistency; does not certify generated app runtime."""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


def read_json(path):
    try:
        return json.loads((ROOT / path).read_text())
    except (OSError, ValueError) as error:
        errors.append(f'{path}: {error}')
        return {}


manifest = read_json('manifest.json')
about = read_json('.github/repository-about.json')
roles = {path.stem for path in (ROOT / 'agents').glob('*.md')}
orch = manifest.get('orchestration', {})
require(len(roles) == orch.get('subagent_count'), 'Agent files and manifest count differ')
require(len(roles) == 30, 'Current supported catalog must retain all 30 agents')
expected = {
    'wave1': ['planner-griller'],
    'wave2': ['design-dna-agent', 'motion-design-agent'],
    'wave3': ['gsap-agent', 'threejs-agent', 'hyperframes-agent', 'motion-a11y-agent'],
    'wave4': ['genjutsu-agent', 'render-perf-budget-agent', 'qa-anti-slop-agent', 'token-handoff-exporter'],
}
require(orch.get('wave_order') == expected, 'Manifest core wave order differs from SKILL contract')
core = {name for names in expected.values() for name in names}
registered = {
    item.get('agent')
    for group in ['creative_track', 'engineering_track_from_tiktok']
    for item in manifest.get(group, [])
} | {item.get('agent') for item in orch.get('agents', [])}
require(roles == registered, 'Manifest agent registry does not cover exactly the on-disk roles')

for name in roles:
    text = (ROOT / 'agents' / f'{name}.md').read_text()
    require(bool(re.search(rf'^name: {re.escape(name)}$', text, re.M)), f'{name}: frontmatter identity mismatch')

readme = (ROOT / 'README.md').read_text()
skill = (ROOT / 'SKILL.md').read_text()
require(set(re.findall(r'\]\(agents/([\w-]+)\.md\)', readme)) == roles, 'README catalog omits or invents agents')
require(f'**{len(roles)}-agent' in readme, 'README overview count is stale')
require(re.findall(r'^### Wave (\d) ', skill, re.M) == ['1', '2', '3', '4'], 'SKILL must declare the four ordered waves once')
for name in core:
    require(f'`{name}`' in skill, f'SKILL does not dispatch {name}')
require('LAST and only after final QA PASS' in skill, 'SKILL exporter QA/last gate is missing')
require(orch.get('handoff_gate', {}).get('runs_last') is True, 'Manifest handoff must run last')
for gate in ['motion_accessibility', 'performance', 'final_qa', 'handoff']:
    require(gate in orch.get('quality_gates', {}), f'Manifest lacks {gate} gate')

# Validate complete JSON examples in authoritative scheduling/state documents.
state = {}
for relative in ['SKILL.md', 'references/orchestrator-state.md', 'references/normal-motion-orchestration.md']:
    for block in re.findall(r'```json\n(.*?)\n```', (ROOT / relative).read_text(), re.S):
        try:
            obj = json.loads(block)
            if relative.endswith('orchestrator-state.md'):
                state = obj
        except ValueError as error:
            errors.append(f'{relative}: invalid JSON example: {error}')
require(state.get('subagent_count') == len(roles), 'State agent count is stale')
for wave, names in expected.items():
    require([name for name in state.get('waves', {}).get(wave, {}) if name != 'supporting_tasks'] == names, f'State {wave} ordering differs')
require(core | set(state.get('supporting_agent_status', {})) == roles, 'State loses core/supporting roles')
require(state.get('waves', {}).get('wave4', {}).get('token-handoff-exporter') == 'blocked-until-final-qa-pass', 'State exporter readiness gate missing')
for key in ['motion_a11y', 'performance', 'handoff']:
    require(key in state, f'State lacks {key} evidence')
require(state.get('qa_verification', {}).get('interaction_backend') == 'agent-desktop', 'State interaction backend is stale')

summary = about.get('description', '')
require(bool(summary) and len(summary) <= 350 and '\n' not in summary, 'GitHub About needs one nonempty description of at most 350 characters')
require(summary == manifest.get('description'), 'Manifest description and tracked GitHub About differ')
require(f'{len(roles)}-agent' in summary, 'GitHub About count is stale')

for path in [ROOT / 'README.md', ROOT / 'SKILL.md', *(ROOT / 'references').glob('*.md')]:
    text = path.read_text()
    for target in re.findall(r'\]\(([^)]+)\)', text):
        target = target.strip().strip('<>')
        if urlparse(target).scheme or target.startswith('#'):
            continue
        relative = unquote(target.split('#', 1)[0])
        require((path.parent / relative).exists(), f'{path.relative_to(ROOT)}: missing local Markdown target {target}')
    if path.parent.name == 'references':
        for stale in [r'Wave 1 (?:research|browser-agent|gathers references)', r'Within Wave 4, assemble', r'all three normal specialists', r'optional \d+(?:st|nd|rd|th) agent']:
            require(not re.search(stale, text), f'{path.relative_to(ROOT)}: stale scheduling text {stale}')

rubric = (ROOT / 'references/qa-rubric.md').read_text()
for token in ['motion-a11y.md', 'perf-budget.json', 'perf-report.md', 'token-handoff-exporter']:
    require(token in rubric, f'QA rubric omits {token}')

if errors:
    for error in errors:
        print(f'FAIL: {error}', file=sys.stderr)
    sys.exit(1)
print(f'PASS: {len(roles)} roles, four waves, state, gates, README catalog, local links and About metadata')
print('Runtime accessibility/performance/desktop/import evidence is checked by the generated-build agents, not this validator.')
