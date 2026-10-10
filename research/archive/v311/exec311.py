#!/usr/bin/env python3
"""Scratch: execute one V3-11 stage in the repository, reading the frozen edits and predicted blobs
back from the preregistration at F. Never landed. Commits nothing.

Usage: exec311.py <F> <stage 1|2|3>
Applies that stage's edits to the working tree and checks each changed file's blob against the
frozen table; exits 1 on any difference."""
import os
import re
import subprocess
import sys

REPO = '/home/user/incompleteness'
F, N = sys.argv[1], int(sys.argv[2])
P = 'verification/infrastructure/round-v3-11-authority-cutover/preregistration.md'


def git(*a, data=None):
    return subprocess.run(['git'] + list(a), cwd=REPO, input=data, capture_output=True,
                          check=True).stdout.decode()


pre = git('show', '%s:%s' % (F, P))
body = pre[pre.index('## The execution, FROZEN'):pre.index('## The controls, FROZEN')]
edits = re.findall(r'### Edit (\d+) — stage (\d), `([^`]+)`\n\nThe text at the parent:\n\n```text\n'
                   r'(.*?)```\n\nIts replacement:\n\n```text\n(.*?)```', body, re.S)
assert len(edits) == 20 and [int(e[0]) for e in edits] == list(range(1, 21)), len(edits)
table = dict((p, b) for st, p, b in re.findall(r'^\| (\d) \| `([^`]+)` \| `[0-9a-f]{8}` \| `([0-9a-f]{40})` \|$',
                                              body, re.M) if int(st) == N)
ok = True
texts = {}
for _n, st, path, old, new in edits:
    if int(st) != N:
        continue
    if path not in texts:
        texts[path] = open(os.path.join(REPO, path), encoding='utf-8').read()
    c = texts[path].count(old)
    if c != 1:
        print('FAIL  edit %s: the text at the parent occurs %d times in %s' % (_n, c, path))
        ok = False
        continue
    texts[path] = texts[path].replace(old, new)
for path, t in texts.items():
    open(os.path.join(REPO, path), 'w', encoding='utf-8').write(t)
    got = git('hash-object', path).strip()
    good = got == table.get(path)
    ok &= good
    print('%-5s stage %d %-48s %s (predicted %s)' % ('PASS' if good else 'FAIL', N, path, got, table.get(path)))
ok &= sorted(texts) == sorted(table)
changed = sorted(x.split('\t')[1] for x in git('diff', '--name-status').strip().split('\n') if x)
ok &= changed == sorted(table)
print('working tree changes: %s' % ', '.join(changed))
print('STAGE %d APPLY %s' % (N, 'PASS' if ok else 'FAIL'))
sys.exit(0 if ok else 1)
