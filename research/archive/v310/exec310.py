#!/usr/bin/env python3
"""Scratch: apply V3-10's frozen README change, read back from the preregistration at F, and check
the predicted blob. Never landed. Usage: exec310.py <F>. Commits nothing."""
import os
import re
import subprocess
import sys

REPO = '/home/user/incompleteness'
F = sys.argv[1]
P = 'verification/infrastructure/round-v3-10-native-pilot/preregistration.md'
README = 'verification/README.md'


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True, check=True).stdout.decode()


pre = git('show', '%s:%s' % (F, P))
sec = pre[pre.index('## The execution, FROZEN'):pre.index('## The lifecycle')]
texts = re.findall(r'```text\n(.*?)```', sec, re.S)
assert len(texts) == 2
old, new = texts
pred = re.findall(r"predicted blob afterwards is `([0-9a-f]{40})`", sec)
assert len(pred) == 1
cur = open(os.path.join(REPO, README), encoding='utf-8').read()
assert cur == git('show', '%s:%s' % (F, README)), 'README is not its F bytes'
assert cur.endswith(old) and cur.count(old) == 1, 'the frozen lines are not the last two lines'
out = cur[:-len(old)] + new
open(os.path.join(REPO, README), 'w', encoding='utf-8').write(out)
got = git('hash-object', README).strip()
print('README blob %s, predicted %s' % (got, pred[0]))
diff = git('diff', '--no-renames', '--name-status')
print('working-tree change:', diff.strip().replace('\n', '; '))
ok = got == pred[0] and diff.strip() == 'M\t' + README
print('STAGE 1 CHECKPOINT %s' % ('PASS' if ok else 'FAIL'))
sys.exit(0 if ok else 1)
