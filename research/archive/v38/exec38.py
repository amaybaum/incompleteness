#!/usr/bin/env python3
"""Scratch: execute one V3-8 stage in the repository, reading the frozen edits, sites and README
paragraphs back from the preregistration at B. Never landed.

Usage: exec38.py <B> <stage 1|2|3>
Applies the stage's changes to the working tree and runs its checkpoint controls with the tool from
the repository (stage 1: C1, C6, C7; stage 2: C1, C2, C6; stage 3: C1, C6). It commits nothing."""
import json
import os
import re
import shutil
import subprocess
import sys
import types

REPO = os.environ.get('EXEC_REPO', '/home/user/incompleteness')
HERE = os.path.dirname(os.path.abspath(__file__))
B, n = sys.argv[1], int(sys.argv[2])
P = 'verification/infrastructure/round-v3-8-publication-removal/preregistration.md'
TOOL, ARCH, README = 'tools/v3_verifier.py', 'verification/infrastructure/v3/architecture.md', 'verification/README.md'
CONF = 'verification/infrastructure/v3/conformance/'
RETIRED, CONVERTED = 'mc2-counter-host-merge', 'mc2-pass-base-drift'
ADDED = ['reach-false-moved-base-lacks-q', 'reach-true-host-merge-contains-q', 'reach-undecidable-shallow-history']
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


def section(t, start, end):
    return t[t.index(start):t.index(end)]


def blocks(s):
    return re.findall(r'```text\n(.*?)\n```', s, re.S)


def rd(p):
    return open(os.path.join(REPO, p), encoding='utf-8').read()


def wr(p, s):
    open(os.path.join(REPO, p), 'w', encoding='utf-8').write(s)


def tool(*a):
    p = subprocess.run([sys.executable, TOOL] + list(a), cwd=REPO, capture_output=True)
    return p.returncode, p.stdout.decode().strip()


pre = git('show', '%s:%s' % (B, P))
if n == 1:
    spec = section(pre, '## The specification, FROZEN as text', '## The implementation, FROZEN')
    ids = re.findall(r'^#### `(N\d+)`', spec, re.M)
    b = blocks(spec)
    assert ids == ['N%d' % i for i in range(1, 22)] and len(b) == 2 * len(ids), (ids, len(b))
    a = rd(ARCH)
    for i, nid in enumerate(ids):
        assert a.count(b[2 * i]) == 1, (nid, a.count(b[2 * i]))
        a = a.replace(b[2 * i], b[2 * i + 1])
    wr(ARCH, a)
    print('stage 1: %d edit(s) applied, %s to %s' % (len(ids), ids[0], ids[-1]))
    for bad in ('PUBLISHED', 'T8', 'tip of `main` when', 'publication makes', 'publication is a fast-forward',
                'live tip of `main` is publication'):
        report('C7 architecture no longer contains %r' % bad, bad not in a)
    print('stage 1 architecture blob %s' % git('hash-object', ARCH).strip())
else:
    sec = section(pre, '### Stage %d' % n, '### Stage 3' if n == 2 else '## The README paragraph')
    pat = re.compile(r'#### Site `(s%d\.\d+)`\n\nThe site:\n\n```text\n(.*?)\n```\n\n'
                     r'The drafting-time replacement \(a prediction\):\n\n```text\n(.*?)\n```' % n, re.S)
    sites = pat.findall(sec)
    assert sites and len(sites) * 2 == len(blocks(sec))
    parent = rd(TOOL)
    src = parent
    for sid, old, new in sites:
        assert src.count(old) == 1, (sid, src.count(old))
        src = src.replace(old, new)
    wr(TOOL, src)
    print('stage %d: %d site(s) applied: %s' % (n, len(sites), ', '.join(s[0] for s in sites)))
    if n == 2:
        gen = os.path.join(HERE, 'gen-exec')
        shutil.rmtree(gen, ignore_errors=True)
        subprocess.run([sys.executable, os.path.join(HERE, 'gen38.py'), B, gen], check=True)
        git('rm', '-q', CONF + RETIRED + '.json')
        for v in [CONVERTED] + ADDED:
            shutil.copy(os.path.join(gen, v + '.json'), os.path.join(REPO, CONF, v + '.json'))
        git('add', CONF)
        conf = os.path.join(REPO, CONF)
        V = {f[:-5]: json.load(open(os.path.join(conf, f), encoding='utf-8')) for f in os.listdir(conf) if f.endswith('.json')}
        report('C2 retired vector absent', RETIRED not in V)
        pm, sm = load('parent', parent), load('stage', src)
        for v in ADDED + [CONVERTED]:
            rp, rs = pm.run_vector(V[v], REPO)[0], sm.run_vector(V[v], REPO)[0]
            report('C2 %-36s parent %s, stage %s' % (v, 'as expected' if rp else 'not', 'as expected' if rs else 'not'),
                   not rp and rs)
        report('C2 no publication( or s10:not-q-itself in the stage-2 tool',
               'publication(' not in src and 's10:not-q-itself' not in src)
    else:
        old = re.search(r'The paragraph at `B`:\n\n```text\n(.*?)```', pre, re.S).group(1)
        new = re.search(r'The paragraph at `E`:\n\n```text\n(.*?)```', pre, re.S).group(1)
        r = rd(README)
        assert r.count(old) == 1
        wr(README, r.replace(old, new))
        print('stage 3: README paragraph replaced; README blob %s' % git('hash-object', README).strip())
    print('stage %d tool blob %s' % (n, git('hash-object', TOOL).strip()))

want = {1: 133, 2: 135, 3: 135}[n]
rc, out = tool('--corpus')
last = out.split('\n')[-1]
report('C1 %s' % last, rc == 0 and last == 'CORPUS  %d vector(s), exact and as expected' % want)
rc, out = tool('--self-test')
report('C6 %s' % out, rc == 0)
print('STAGE %d CHECKPOINT %s' % (n, 'PASS' if ok else 'FAIL'))
sys.exit(0 if ok else 1)
