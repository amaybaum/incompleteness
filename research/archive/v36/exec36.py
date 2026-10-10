#!/usr/bin/env python3
"""Scratch: execute one V3-6 stage in the repository, reading the frozen sites and the README
paragraphs back from the preregistration at B. Never landed.

Usage: exec36.py <stage 1|2|3>
Applies the stage's edits to the working tree, moves its vectors, and runs its checkpoint controls
(C1, C2 or C5, C6) with the tool from the repository. It commits nothing."""
import json
import os
import re
import subprocess
import sys
import types

REPO = '/home/user/incompleteness'
B = 'bace2e070c6e621c3314b9363ea56314b414f736'
P = 'verification/infrastructure/round-v3-6-final-conformance/preregistration.md'
TOOL = 'tools/v3_verifier.py'
V3 = 'verification/infrastructure/v3/'
CONF, PEND = V3 + 'conformance/', V3 + 'conformance-pending/'
n = int(sys.argv[1])
ok = True


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True, check=True).stdout.decode()


def report(label, cond):
    global ok
    ok &= bool(cond)
    print('%-5s %s' % ('PASS' if cond else 'FAIL', label))


def load(name, text):
    m = types.ModuleType(name)
    m.__file__ = os.path.join(REPO, TOOL)
    exec(compile(text, name, 'exec'), m.__dict__)
    return m


pre = git('show', '%s:%s' % (B, P))
pat = re.compile(r'#### Site `(s(\d)\.\d+)`\n\nThe site:\n\n```text\n(.*?)\n```\n\n'
                 r'The drafting-time replacement \(a prediction\):\n\n```text\n(.*?)\n```', re.S)
sites = [s for s in pat.findall(pre) if int(s[1]) == n]
parent_src = open(os.path.join(REPO, TOOL), encoding='utf-8').read()
src = parent_src
for sid, _, old, new in sites:
    assert src.count(old) == 1, (sid, src.count(old))
    src = src.replace(old, new)
open(os.path.join(REPO, TOOL), 'w', encoding='utf-8').write(src)
print('stage %d: %d site(s) applied: %s' % (n, len(sites), ', '.join(s[0] for s in sites)))

moved = []
if n in (1, 2):
    row = re.search(r'^\| %d \| (.*) \|$' % n, pre.split('## The vectors, FROZEN')[1], re.M).group(1)
    moved = re.findall(r'`([a-z0-9-]+)`', row)
    for v in moved:
        git('mv', PEND + v + '.json', CONF + v + '.json')
    print('stage %d: %d vector(s) moved' % (n, len(moved)))
    pd = os.path.join(REPO, PEND)
    if os.path.isdir(pd) and not os.listdir(pd):
        os.rmdir(pd)
if n == 3:
    old = re.search(r'The paragraph at `B`:\n\n```text\n(.*?)\n```', pre, re.S).group(1) + '\n'
    new = re.search(r'The paragraph at `E`:\n\n```text\n(.*?)\n```', pre, re.S).group(1) + '\n'
    rp = os.path.join(REPO, 'verification/README.md')
    t = open(rp, encoding='utf-8').read()
    assert t.count(old) == 1
    open(rp, 'w', encoding='utf-8').write(t.replace(old, new))
    print('stage 3: README paragraph replaced')

blob = subprocess.run(['git', 'hash-object', TOOL], cwd=REPO, capture_output=True).stdout.decode().strip()
print('stage %d tool blob %s' % (n, blob))
want = {1: 122, 2: 133, 3: 133}[n]
out = subprocess.run([sys.executable, TOOL, '--corpus'], cwd=REPO, capture_output=True)
last = out.stdout.decode().strip().split('\n')[-1]
report('C1 %s' % last, out.returncode == 0 and last == 'CORPUS  %d vector(s), exact and as expected' % want)
out = subprocess.run([sys.executable, TOOL, '--self-test'], cwd=REPO, capture_output=True)
report('C6 %s' % out.stdout.decode().strip(), out.returncode == 0)
if moved:
    vs = {v: json.load(open(os.path.join(REPO, CONF, v + '.json'), encoding='utf-8')) for v in moved}
    tp, ts = load('parent', parent_src), load('stage', src)
    rp_ = {v: tp.run_vector(x, REPO)[0] for v, x in vs.items()}
    rs_ = {v: ts.run_vector(x, REPO)[0] for v, x in vs.items()}
    for v in moved:
        print('      %-58s parent %s, stage %s' % (v, 'as expected' if rp_[v] else 'not as expected',
                                                    'as expected' if rs_[v] else 'not as expected'))
    report('C2 stage %d: %d vector(s) not as expected on the parent tool, as expected on the stage tool'
           % (n, len(moved)), not any(rp_.values()) and all(rs_.values()))
if n == 2:
    left = subprocess.run(['git', 'ls-files', PEND], cwd=REPO, capture_output=True).stdout.decode().strip()
    report('stage 2: conformance-pending/ holds no file in the index', left == '' and not os.path.exists(os.path.join(REPO, PEND)))
print('CHECKPOINT PASS' if ok else 'CHECKPOINT FAIL')
sys.exit(0 if ok else 1)
