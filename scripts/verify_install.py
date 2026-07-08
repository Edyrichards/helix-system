#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
HOME = Path.home()
agent = HOME/'.hermes/agents/helix-system'
skill = HOME/'.hermes/skills/helix-system'
required_agent = [
    'references/00-operating-contract.md','references/01-mode-router.md','references/02-evidence-ledger.md',
    'references/03-verifier-subagents.md','references/design-system-first.md','references/charts-and-design-system-adapters.md','references/ui-design-autonomy-repo-patterns.md','scripts/helix_init.py','scripts/helix_eval.py','scripts/helix_design_system_init.py','scripts/helix_design_research.py','scripts/helix_design_tournament.py','scripts/score_output.py',
    'references/10-design-reasoning-engine.md','references/11-advanced-design-psychology.md','references/12-prompt-reprompt-engine.md','GO_TO_MARKET.md','PERSONA_CATALOG.md','research/agency-agents-dissection-2026-07.md','scripts/helix_reprompt.py','scripts/validate_personas.py','personas/conversion-psychologist.md','personas/prompt-architect.md','personas/design-jury-lead.md','personas/gtm-strategist.md','scripts/install_helix.sh','examples/reprompt-onboarding.md','examples/design-swarm-checkout.md','BEST_IN_CLASS_ROADMAP.md','catalog/tools.json','catalog/modules.json','catalog/personas.json','runbooks/runbooks.json','scripts/check_catalog.py','scripts/helix_convert.py','references/architecture.md','references/hermes-takeover-contract.md','references/hermes-runtime-integration.md','references/safety-security-model.md','docs/capability-map.md','docs/helix-product-strategy.md','tests/test_docs_integrity.py','CHANGELOG.md','README.md','agent.md'
]
required_skill = ['SKILL.md','references/00-operating-contract.md','references/01-mode-router.md','references/ui-design-autonomy-repo-patterns.md','scripts/helix_init.py','scripts/helix_eval.py','scripts/helix_design_system_init.py']
errors = []
for rel in required_agent:
    if not (agent/rel).exists(): errors.append(f'missing agent/{rel}')
for rel in required_skill:
    if not (skill/rel).exists(): errors.append(f'missing skill/{rel}')
content = (skill/'SKILL.md').read_text(encoding='utf-8') if (skill/'SKILL.md').exists() else ''
if not content.startswith('---\n') or '\n---\n' not in content[4:]: errors.append('SKILL.md invalid frontmatter')
if len(content.splitlines()) > 500: errors.append(f'SKILL.md too long: {len(content.splitlines())} lines')
try:
    out = subprocess.run(['hermes','skills','list'], capture_output=True, text=True, timeout=20)
    if 'helix-system' not in (out.stdout + out.stderr): errors.append('hermes skills list does not show helix-system')
except Exception as e:
    errors.append(f'could not run hermes skills list: {e}')
if errors:
    print('Helix install verification FAILED')
    for e in errors: print('-', e)
    sys.exit(1)
print('Helix install verification PASSED')
print('agent_dir:', agent)
print('skill_dir:', skill)
print('skill_lines:', len(content.splitlines()))
