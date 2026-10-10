#!/usr/bin/env python3
"""Scratch: simulate the V3-8 execution from a base commit in a throwaway worktree, measuring the
controls. Never landed; nothing pushed. Usage: sim38.py <base>"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edits38  # noqa

REPO = '/home/user/incompleteness'
BASE = sys.argv[1]
WT = os.path.join(HERE, 'wt')
GEN = os.path.join(HERE, 'gen')
TOOL, ARCH, README = 'tools/v3_verifier.py', 'verification/infrastructure/v3/architecture.md', 'verification/README.md'
CONF = 'verification/infrastructure/v3/conformance/'
RETIRED = 'mc2-counter-host-merge'
CONVERTED = 'mc2-pass-base-drift'
ADDED = ['reach-false-moved-base-lacks-q', 'reach-true-host-merge-contains-q', 'reach-undecidable-shallow-history']
ENV = dict(os.environ, GIT_AUTHOR_NAME='sim', GIT_AUTHOR_EMAIL='sim@invalid', GIT_COMMITTER_NAME='sim',
           GIT_COMMITTER_EMAIL='sim@invalid', GIT_AUTHOR_DATE='1700000000 +0000',
           GIT_COMMITTER_DATE='1700000000 +0000')
ok = True


def git(*a, cwd=WT):
    return subprocess.run(['git'] + list(a), cwd=cwd, env=ENV, capture_output=True, check=True).stdout.decode()


def report(label, cond):
    global ok
    ok &= bool(cond)
    print('%-5s %s' % ('PASS' if cond else 'FAIL', label))


def load(name, text):
    m = types.ModuleType(name)
    m.__file__ = os.path.join(WT, TOOL)
    exec(compile(text, name, 'exec'), m.__dict__)
    return m


def vecs():
    d = os.path.join(WT, CONF)
    return {n[:-5]: json.load(open(os.path.join(d, n), encoding='utf-8')) for n in sorted(os.listdir(d)) if n.endswith('.json')}


def run(tool, vs):
    return {v: tool.run_vector(x, WT)[0] for v, x in vs.items()}


def tool_cmd(*a):
    p = subprocess.run([sys.executable, TOOL] + list(a), cwd=WT, capture_output=True)
    return p.returncode, p.stdout.decode().strip()


def sub(s, old, new, tag):
    assert s.count(old) == 1, (tag, s.count(old))
    return s.replace(old, new)


if os.path.exists(WT):
    subprocess.run(['git', 'worktree', 'remove', '--force', WT], cwd=REPO)
    shutil.rmtree(WT, ignore_errors=True)
subprocess.run(['git', 'worktree', 'prune'], cwd=REPO, check=True)
git('worktree', 'add', '--detach', WT, BASE, cwd=REPO)
subprocess.run([sys.executable, os.path.join(HERE, 'gen38.py'), BASE, GEN], check=True)
blobs = {}

# stage 1: the specification
a = open(os.path.join(WT, ARCH), encoding='utf-8').read()
for nid, old, new in edits38.SPEC:
    a = sub(a, old, new, nid)
open(os.path.join(WT, ARCH), 'w', encoding='utf-8').write(a)
git('add', '-A'); git('commit', '-q', '-m', 'stage 1')
blobs['arch'] = git('rev-parse', 'HEAD:' + ARCH).strip()
for bad in ('PUBLISHED', 'T8', 'tip of `main` when', 'publication makes', 'publication is a fast-forward',
            'live tip of `main` is publication'):
    report('C7 architecture no longer contains %r' % bad, bad not in a)
rc, out = tool_cmd('--corpus')
report('C1 stage 1: %s' % out.split('\n')[-1], rc == 0 and out.split('\n')[-1] == 'CORPUS  133 vector(s), exact and as expected')

# stage 2: the tool's behaviour and the corpus
t0 = open(os.path.join(WT, TOOL), encoding='utf-8').read()
t2 = t0
for sid, st, old, new in edits38.SITES:
    if st == 2:
        t2 = sub(t2, old, new, sid)
open(os.path.join(WT, TOOL), 'w', encoding='utf-8').write(t2)
git('rm', '-q', CONF + RETIRED + '.json')
for v in [CONVERTED] + ADDED:
    shutil.copy(os.path.join(GEN, v + '.json'), os.path.join(WT, CONF, v + '.json'))
git('add', '-A'); git('commit', '-q', '-m', 'stage 2')
blobs['tool2'] = git('rev-parse', 'HEAD:' + TOOL).strip()
rc, out = tool_cmd('--corpus')
report('C1 stage 2: %s' % out.split('\n')[-1], rc == 0 and out.split('\n')[-1] == 'CORPUS  135 vector(s), exact and as expected')
V = vecs()
report('C2 retired vector absent', RETIRED not in V)
p, s = load('p', t0), load('s', t2)
moved = {v: V[v] for v in ADDED + [CONVERTED]}
rp, rs = run(p, moved), run(s, moved)
for v in moved:
    print('      %-40s parent %s, stage %s' % (v, 'as expected' if rp[v] else 'not', 'as expected' if rs[v] else 'not'))
report('C2 each added or converted vector: not as expected on the parent tool, as expected on the stage tool',
       not any(rp.values()) and all(rs.values()))
report('C2 no reference to publication() left in the stage-2 tool code', 'publication(' not in t2 and 's10:not-q-itself' not in t2)

# stage 3: the self-description
t3 = t2
for sid, st, old, new in edits38.SITES:
    if st == 3:
        t3 = sub(t3, old, new, sid)
open(os.path.join(WT, TOOL), 'w', encoding='utf-8').write(t3)
r = open(os.path.join(WT, README), encoding='utf-8').read()
open(os.path.join(WT, README), 'w', encoding='utf-8').write(sub(r, edits38.README_OLD, edits38.README_NEW, 'readme'))
git('add', '-A'); git('commit', '-q', '-m', 'stage 3')
S3 = git('rev-parse', 'HEAD').strip()
blobs['tool3'] = git('rev-parse', 'HEAD:' + TOOL).strip()
blobs['readme'] = git('rev-parse', 'HEAD:' + README).strip()
rc, out = tool_cmd('--corpus')
report('C1 stage 3: %s' % out.split('\n')[-1], rc == 0 and out.split('\n')[-1] == 'CORPUS  135 vector(s), exact and as expected')
rc, out = tool_cmd('--self-test')
report('C6 %s' % out, rc == 0)

# C3 own rule: three wrong diagnostics, each failing exactly the vectors that separate it
REACH_BODY = """    try:
        return ('true' if repo.is_ancestor(q, c) else 'false'), None
    except Undecidable as u:
        return 'undecidable', u.code"""
WRONG = {'always-true': ("    return 'true', None", ['reach-false-moved-base-lacks-q', 'reach-undecidable-shallow-history']),
         'always-false': ("    return 'false', None", ['reach-true-host-merge-contains-q', CONVERTED, 'reach-undecidable-shallow-history']),
         'reversed': ("""    try:
        return ('true' if repo.is_ancestor(c, q) else 'false'), None
    except Undecidable as u:
        return 'undecidable', u.code""", ['reach-true-host-merge-contains-q', CONVERTED])}
ALL = vecs()
for name, (body, own) in WRONG.items():
    rr = run(load(name, sub(t3, REACH_BODY, body, name)), ALL)
    report('C3 %-12s: its %d vector(s) not as expected, the other %d as expected'
           % (name, len(own), len(ALL) - len(own)),
           not any(rr[v] for v in own) and all(rr[v] for v in ALL if v not in own))

# C4 census unchanged
b = os.path.join(HERE, 'tool_at_base.py')
open(b, 'w').write(t0)
pb = subprocess.run([sys.executable, b, '--project', BASE], cwd=WT, capture_output=True).stdout
pe = subprocess.run([sys.executable, TOOL, '--project', BASE], cwd=WT, capture_output=True).stdout
report('C4 --project over the base identical (%d lines, sha256 %s)' % (pe.count(b'\n'), hashlib.sha256(pe).hexdigest()[:12]),
       pe == pb and pe)

# C5 the shadow report and the CLI
rc, out = tool_cmd('--mode', 'shadow', '--subject', S3)
L = out.split('\n')
report('C5 shadow: banner, 12 rules, corpus 135, projection 126, complete',
       rc == 0 and L[0].startswith('v3_verifier shadow report -- SHADOW ONLY')
       and [x[2:6].strip() for x in L if x.startswith('  ') and x[2:3] in 'KG'] ==
       ['K1', 'K2', 'K3', 'K4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12']
       and 'CORPUS  135 vector(s), exact and as expected' in L and 'PROJECTION  cells 126' in L
       and L[-1] == 'v3_verifier: shadow report complete (corpus as expected)')
par = git('rev-parse', BASE + '^1').strip()
r1 = tool_cmd('--reachable', BASE, par)
r2 = tool_cmd('--reachable', par, BASE)
report('C5 --reachable <base> <its parent>: %r exit %d' % (r1[1], r1[0]), r1 == (0, 'REACHABLE true'))
report('C5 --reachable <parent> <base>: %r exit %d' % (r2[1], r2[0]), r2 == (0, 'REACHABLE false'))
r3 = tool_cmd('--publication', BASE, BASE)
report('C5 --publication is gone: exit %d, %r' % (r3[0], r3[1][:60]), r3[0] != 0 and 'VERDICT' not in r3[1])
rd = open(os.path.join(WT, README), encoding='utf-8').read()
report('C5 no "--publication" or "not-q-itself" in the tool or the README',
       '--publication' not in t3 and 'not-q-itself' not in t3 and '--publication' not in rd)
print('blobs:', blobs)
print('stage-3 commit:', S3)
print('ALL CONTROLS PASS' if ok else 'A CONTROL FAILED')
