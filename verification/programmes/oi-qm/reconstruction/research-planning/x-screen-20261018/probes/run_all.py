#!/usr/bin/env python3
"""run_all.py -- deterministic replay of every xscreen probe.  Research only.

Runs each probe twice with `python3 -I -B`, requires byte-identical stdout across the two runs,
saves runs/<name>.out, and writes runs/SHA256SUMS over probes/, src/ and runs/.  Also replays two
upstream checks from pinned copies in src/: the #859 Fact B script and check B
(monitored_law.py, which pins f2_5_dict.py by sha256 itself), and compares check B's stdout with
the digest recorded in the upstream README (634e1639...).
"""
import hashlib, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
RUNS = os.path.join(ROOT, 'runs'); SRC = os.path.join(ROOT, 'src')
PY = [sys.executable, '-I', '-B']
jobs = [(n, [os.path.join(HERE, n + '.py')]) for n in
        ('p1_gamma_static', 'p2_perm_scan', 'p3_fixtures_op', 'p4_ones_fixing_lie', 'p5_m1_retained_law')]
jobs += [('replay_factB', [os.path.join(SRC, 'f2-decision-memo-factB_check.py')]),
         ('replay_checkB', [os.path.join(SRC, 'monitored_law.py'), os.path.join(SRC, 'f2_5_dict.py')])]
sha = lambda b: hashlib.sha256(b).hexdigest()
ok = True
for name, args in jobs:
    outs = [subprocess.run(PY + args, capture_output=True, timeout=3000, cwd=ROOT) for _ in range(2)]
    det = outs[0].stdout == outs[1].stdout and all(o.returncode == 0 for o in outs)
    open(os.path.join(RUNS, name + '.out'), 'wb').write(outs[0].stdout)
    last = outs[0].stdout.decode().strip().splitlines()[-1] if outs[0].stdout else '(no output)'
    print('%-20s deterministic=%s rc=%s sha256=%s' % (name, det, outs[0].returncode, sha(outs[0].stdout)))
    print('    ', last[:200])
    ok &= det
cb = open(os.path.join(RUNS, 'replay_checkB.out'), 'rb').read()
cb_match = sha(cb) == '634e1639637e9e803f9d6a65786023cba47f2f9362aec358118d53f48ffdac5d'
print('check B stdout matches upstream recorded digest:', cb_match); ok &= cb_match
lines = []
for d in ('probes', 'src', 'runs'):
    for f in sorted(os.listdir(os.path.join(ROOT, d))):
        if f == 'SHA256SUMS' or f.startswith('run_all') and d == 'runs': continue
        p = os.path.join(ROOT, d, f)
        if os.path.isfile(p): lines.append('%s  %s/%s' % (sha(open(p, 'rb').read()), d, f))
open(os.path.join(RUNS, 'SHA256SUMS'), 'w').write('\n'.join(lines) + '\n')
print('REPLAY', 'GREEN' if ok else 'RED')
