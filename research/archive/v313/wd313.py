#!/usr/bin/env python3
"""Scratch: build V3-13's withdrawal W on the candidate head, under S12, and prove it. Never landed.

Usage: wd313.py <F> <candidate head> [<W>]   (with <W>, the proof alone; without, run with the repository at the candidate head, the halted
                                        result note already written in the working tree)

Every path the governed-path block at F governs by an execution entry is set to its state at F
(restored, or removed when absent at F); the result note is committed with it; nothing else."""
import os
import subprocess
import sys

REPO = '/home/user/incompleteness'
sys.path.insert(0, os.path.join(REPO, 'tools'))
import v3_verifier as v3  # noqa: E402

F, HEAD = sys.argv[1], sys.argv[2]
RD = b'verification/infrastructure/round-v3-13-retirement/'
TRAILER = ('\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n'
           'Claude-Session: https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1\n')


def git(*a):
    r = subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True)
    if r.returncode:
        raise SystemExit('git %s: %s' % (a, r.stderr.decode()))
    return r.stdout.decode()


def report(label, cond):
    print('%s  %s' % ('PASS' if cond else 'FAIL', label))
    if not cond:
        raise SystemExit('REFUSED  ' + label)


repo = v3.Repo(REPO)
pre = repo.blob(repo.state(F, RD + b'preregistration.md')[1]).decode('utf-8')
entries = v3.parse_governed_text(pre)
fe, he = repo.entries(F), repo.entries(HEAD)
if len(sys.argv) > 3:
    W = sys.argv[3]
else:
    report('the repository is at the candidate head', git('rev-parse', 'HEAD').strip() == HEAD)
    st = git('status', '--porcelain').split('\n')
    report('the only working-tree change is the result note',
           [x for x in st if x] == [' M ' + (RD + b'result.md').decode()])
    restore, remove = [], []
    for path in sorted(set(fe) | set(he)):
        g = v3.governing(entries, path)
        if g is None or g[0] != 'execution' or fe.get(path) == he.get(path):
            continue
        (restore if path in fe else remove).append(path.decode('utf-8'))
    print('withdrawal: %d path(s) restored to F, %d removed' % (len(restore), len(remove)))
    for i in range(0, len(restore), 200):
        git('checkout', F, '--', *restore[i:i + 200])
    for i in range(0, len(remove), 200):
        git('rm', '-q', '--', *remove[i:i + 200])
    git('add', (RD + b'result.md').decode())
    git('commit', '-q', '-m', 'V3-13: withdrawal W, the round halted under S12\n\n'
        'Restores every execution path of the governed-path block at F to its state\n'
        'at F and records the halted result: the candidate head failed C8 because\n'
        'the frozen transformation deleted five retained control-flow-only\n'
        'statements. The record directory keeps the round\'s record.' + TRAILER)
    W = git('rev-parse', 'HEAD').strip()
print('W = %s' % W)

# the proof
report('W is a single-parent child of the candidate head',
       git('rev-list', '--parents', '-n', '1', W).split()[1:] == [HEAD])
we = repo.entries(W)
bad = [p for p in set(fe) | set(we) if (v3.governing(entries, p) or ('',))[0] == 'execution'
       and fe.get(p) != we.get(p)]
report('the withdrawal invariant: every execution-governed path has its state at F (%d differ)'
       % len(bad), not bad)
d_fw = [r for r in repo.delta(F, W)]
report('delta(F, W) is %d path(s), all under the record directory' % len(d_fw),
       all(r[1].startswith(RD) for r in d_fw))
report('the result note is present at W', RD + b'result.md' in we)
report('the control plane at W is that at F',
       we.get(RD + b'preregistration.md') == fe.get(RD + b'preregistration.md'))
man = __import__('json').loads(repo.blob(repo.state(
    F, b'verification/infrastructure/round-v3-12-retirement-census/legacy-records.json')[1]))
moved = [p for p, b in man['records'].items() if (we.get(p.encode()) or (None, None))[1] != b]
def spaces(ent):
    return {p: s for p, s in ent.items()
            if any(p.decode().startswith(n + '/') for n in man['closed_namespaces'])}
report('every one of the %d legacy records has its blob at W (%d moved)'
       % (len(man['records']), len(moved)), not moved)
report('every closed namespace at W is exactly as at F, path for path, mode and blob (%d files)'
       % len(spaces(we)), spaces(we) == spaces(fe))
extra = sorted(p.decode() for p in spaces(we) if p.decode() not in man['records'])
report('the %d files under closed namespaces outside the population are V2\'s conformance corpus, '
       'as at F and D' % len(extra),
       all(p.startswith('verification/certificates/conformance/') for p in extra))
for path in ('verification/lean/edge_rigidity_probe.py', 'tools/release_gate.py',
             '.github/workflows/verify.yml', 'tools/v3_verifier.py', 'AGENTS.md',
             'verification/README.md', 'verification/infrastructure/v3/architecture.md'):
    report('%s at W is its blob at F' % path, we.get(path.encode()) == fe.get(path.encode()))
for path in ('tools/legacy_records_check.py', 'verification/infrastructure/legacy-records.json'):
    report('%s is absent at W' % path, path.encode() not in we)
