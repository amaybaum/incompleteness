#!/usr/bin/env python3
"""Scratch: read the frozen edits, sites and README paragraphs back out of the rendered
preregistration, apply them to the objects at D, and compare the blobs to the predictions."""
import re
import subprocess
import sys

REPO = '/home/user/incompleteness'
P = sys.argv[1]
D = 'f557b1ccbdf9e441b33f5f70fa163823fc2ca10a'
t = open(P, encoding='utf-8').read()


def show(path):
    return subprocess.run(['git', 'show', '%s:%s' % (D, path)], cwd=REPO, capture_output=True, check=True).stdout.decode()


def blob(s):
    return subprocess.run(['git', 'hash-object', '--stdin'], input=s.encode(), capture_output=True, check=True).stdout.decode().strip()


def blocks(sec):
    return re.findall(r'```text\n(.*?)\n```', sec, re.S)


def section(start, end):
    return t[t.index(start):t.index(end)]


ok = True
spec = section('## The specification, FROZEN as text', '## The implementation, FROZEN')
ids = re.findall(r'^#### `(N\d+)`', spec, re.M)
b = blocks(spec)
assert ids == ['N%d' % i for i in range(1, 22)] and len(b) == 42, (ids, len(b))
a = show('verification/infrastructure/v3/architecture.md')
for i in range(21):
    assert a.count(b[2 * i]) == 1, ids[i]
    a = a.replace(b[2 * i], b[2 * i + 1])
tool = show('tools/v3_verifier.py')
got = {'arch': blob(a)}
for st, key in ((2, 'tool2'), (3, 'tool3')):
    sec = section('### Stage %d' % st, '### Stage 3' if st == 2 else '## The README paragraph')
    sb = blocks(sec)
    assert len(sb) % 2 == 0 and sb
    for i in range(0, len(sb), 2):
        assert tool.count(sb[i]) == 1, (st, i)
        tool = tool.replace(sb[i], sb[i + 1])
    got[key] = blob(tool)
rs = section('## The README paragraph', '## The vectors, FROZEN')
rb = re.findall(r'```text\n(.*?)```', rs, re.S)
r = show('verification/README.md')
assert len(rb) == 2 and r.count(rb[0]) == 1
got['readme'] = blob(r.replace(rb[0], rb[1]))
for k, v in got.items():
    print(k, v, 'predicted' if v in t else 'NOT IN FILE')
    ok &= v in t
print('ALL FROZEN BLOBS MATCH' if ok else 'MISMATCH')
