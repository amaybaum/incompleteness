#!/usr/bin/env python3
"""Scratch: C7, C9 and C11 at a commit of V3-14's execution. Usage: echecks.py <commit> [--with-note]"""
import ast, json, os, re, subprocess, sys
REPO = '/home/user/incompleteness'
sys.path.insert(0, os.path.join(REPO, 'tools')); import v3_verifier as v3
D = '378073fa9c3ad7a5c6327aa0163dec3619a40d84'; F = 'd0dde3a9efe2e424a0d32fce4e2bed9564a73674'
RD = 'verification/infrastructure/round-v3-14-retirement/'; GUARD = 'verification/lean/edge_rigidity_probe.py'
TREE = 'a31642acd97065d990c28d2b5a01e30501da452b'
C = sys.argv[1]; ok = True
def git(*a, env=None): return subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True, env=env, check=True).stdout.decode()
def rep(label, cond):
    global ok; ok &= bool(cond); print('%s  %s' % ('PASS' if cond else 'FAIL', label))
pre = git('show', F + ':' + RD + 'preregistration.md'); entries = v3.parse_governed_text(pre)
man = json.loads(git('show', D + ':verification/infrastructure/round-v3-12-retirement-census/legacy-records.json'))
delta = [l.split('\t') for l in git('diff', '--no-renames', '--name-status', D, C).strip().split('\n')]
kinds = {k: sum(1 for s, _p in delta if s == k) for k in 'AMD'}
bad = []
for s, p in delta:
    g = v3.governing(entries, p.encode())
    if g is None or s not in g[1]: bad.append((s, p, g))
leg = [p for _s, p in delta if p in man['records']]
rep('C7 delta(D, %s): %d paths (%d added, %d modified, %d deleted); %d not governed or not authorized; %d legacy records'
    % (C[:8], len(delta), kinds['A'], kinds['M'], kinds['D'], len(bad), len(leg)), not bad and not leg)
for b in bad[:5]: print('   ', b)
# C9
g = ast.parse(git('show', C + ':' + GUARD))
lits = {n.value for n in ast.walk(g) if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) >= 6}
rd0 = git('show', D + ':verification/README.md'); rd1 = git('show', C + ':verification/README.md')
f0, f1 = ' '.join(rd0.split()), ' '.join(rd1.split())
lost = [s for s in lits if (s in rd0 and s not in rd1) or (' '.join(s.split()) in f0 and ' '.join(s.split()) not in f1)]
rep('C9 README: %d guard literals lost; anchor present' % len(lost), not lost and '`.github/workflows/verify.yml` runs' in rd1)
wf = git('show', C + ':.github/workflows/verify.yml')
rep('C9 workflow: repertoire_lie, no lake build / lake env lean of an OIBridge module',
    'repertoire_lie' in wf and not re.search(r'lake build\s+OIBridge\.', wf) and not re.search(r'lake env lean\s+OIBridge/', wf))
ag = ' '.join(git('show', C + ':AGENTS.md').split())
rep('C9 AGENTS: the A.35 heading and the registry sentence',
    '## §A.35 Registry contract for the Lean-to-manuscript census' in ag and 'updates the registry in the same commit' in ag)
rep('C9 release gate: lean-manuscript', '"lean-manuscript"' in git('show', C + ':tools/release_gate.py'))
# C11
idx = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v314/e.index'
env = dict(os.environ, GIT_INDEX_FILE=idx)
git('read-tree', C, env=env)
paths = [RD + 'preregistration.md'] + ([RD + 'result.md'] if '--with-note' in sys.argv else [])
git('rm', '-q', '--cached', *paths, env=env)
t = git('write-tree', env=env).strip(); os.unlink(idx)
rep('C11 tree(%s) less %s: %s' % (C[:8], ' and '.join(p.split('/')[-1] for p in paths), t), t == TREE)
print('ECHECKS  %s' % ('all hold' if ok else 'FAILED')); sys.exit(0 if ok else 1)
