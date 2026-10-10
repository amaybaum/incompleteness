#!/usr/bin/env python3
"""Negative controls on the S2 result note: each mutation is committed as a local, unreferenced object on S1 and must
fail `controls.py check --freeze F` with exactly the named code(s)."""
import re, subprocess, sys
S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/rcs'
S1, F = '216edb986b69309940f58b8d199b15982b194d5e', '1003b029b4949516e615cea8fbf0531c0ced583b'
R = 'verification/programmes/oi-qm/reconstruction/round-relc-select-1/result.md'
note = open(S + '/exec/result.md', encoding='utf-8').read()
EARNED_S = 'The control relation alone already forces odd dimension.'
NONINF_START = '> CtrlGate is the hypothesis of the dimension selector only.'


def drop_noninf(t):
    a = t.index('The non-inference rule:\n')
    b = t.index('\n***\n')
    return t[:a] + t[b:]


def one(cond, label):
    assert cond, label


cases = [
    ('S8: global redundancy claim appended', {'S8'},
     lambda t: t.replace('\n***\n', '\nHence relT is redundant in NativeGate.\n\n***\n', 1)),
    ('S8: an implication between the positivity clauses', {'S8'},
     lambda t: t.replace('\n***\n', '\nForward positivity implies inverse positivity.\n\n***\n', 1)),
    ('S8: "relT is unnecessary" outside the frozen reading', {'S8'},
     lambda t: t.replace('\n***\n', '\nIn short, relT is unnecessary.\n\n***\n', 1)),
    ('V: an extra not-established token', {'V'},
     lambda t: t.replace('\n***\n', '\nNo cell reads RELC-PARITY-NOT-ESTABLISHED.\n\n***\n', 1)),
    ('V: a computed token removed', {'V'},
     lambda t: t.replace('POSITIVITY-SEPARATION-PROVED', 'POSITIVITY-SEPARATION', 99)),
    # an earned reading that is not stated exactly loses its S8 exemption, so its frozen phrase is flagged as well
    ('V+S8: one sentence of the earned reading dropped', {'S8', 'V'},
     lambda t: t.replace(EARNED_S + '\n', '', 1) if (EARNED_S + '\n') in t else t.replace(EARNED_S + ' ', '', 1)),
    ('V: the non-inference rule dropped', {'V'}, drop_noninf),
]
ok = True
for label, codes, f in cases:
    t = f(note)
    if t == note:
        print('  BROKEN  %s: the mutation did not change the note' % label); ok = False; continue
    p = S + '/exec/neg/note.md'
    open(p, 'w', encoding='utf-8').write(t)
    env = dict(__import__('os').environ, GIT_INDEX_FILE=S + '/exec/neg/idx',
               GIT_AUTHOR_DATE='2026-10-08T00:00:00Z', GIT_COMMITTER_DATE='2026-10-08T00:00:00Z')
    run = lambda *a: subprocess.run(a, capture_output=True, text=True, check=True, env=env).stdout.strip()
    run('git', 'read-tree', S1)
    blob = run('git', 'hash-object', '-w', p)
    run('git', 'update-index', '--add', '--cacheinfo', '100644,%s,%s' % (blob, R))
    tree = run('git', 'write-tree')
    c = run('git', '-c', 'user.name=neg', '-c', 'user.email=neg@localhost', 'commit-tree', '--no-gpg-sign', tree, '-p', S1, '-m', 'neg')
    out = subprocess.run(['python3', '-I', S + '/exec/controls.S2.py', 'check', c, '--freeze', F], capture_output=True, text=True).stdout
    last = out.strip().split('\n')[-1]
    m = re.search(r'FAILED \(\d+ of \d+\): (.*)$', last)
    got = set(m.group(1).split()) if m else set()
    good = got == codes
    ok &= good
    print('  %s  %s -> %s' % ('PASS' if good else 'FAIL', label, last))
print('negative controls: %s' % ('OK' if ok else 'FAILED'))
sys.exit(0 if ok else 1)
