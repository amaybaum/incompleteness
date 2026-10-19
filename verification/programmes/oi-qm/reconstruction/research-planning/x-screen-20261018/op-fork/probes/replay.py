#!/usr/bin/env python3
"""replay.py -- deterministic replay of the op-fork probes and generation of the fork verdict.  Research only.

Runs q1-q3 and the parent ../../probes/p3_fixtures_op.py (control C7) twice each with `python3 -I -B`, requires
rc 0 and byte-identical stdout across the two runs, writes runs/<name>.out, then applies the frozen rule of
../PREREG.md section 3 to the RESULT lines and writes runs/verdict.out.  The verdict is VOID if any control is not
green.  Finally writes runs/SHA256SUMS over probes/ and runs/ (excluding SHA256SUMS itself and the replay log).
"""
import hashlib, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
RUNS = os.path.join(ROOT, 'runs'); PARENT = os.path.dirname(ROOT)
PY = [sys.executable, '-I', '-B']
P3_DIGEST = '7d1d1db99ad26054f0e6b7a4960cd39ce95151d0f5765bad6b05caed81e538e1'
jobs = [(n, os.path.join(HERE, n + '.py')) for n in ('q1_maxcone_extreme', 'q2_zf_cones', 'q3_fixture_table')]
jobs.append(('upstream_p3_fixtures_op', os.path.join(PARENT, 'probes', 'p3_fixtures_op.py')))
sha = lambda b: hashlib.sha256(b).hexdigest()
det_ok = True; outs = {}
for name, path in jobs:
    rr = [subprocess.run(PY + [path], capture_output=True, timeout=3000, cwd=ROOT) for _ in range(2)]
    det = rr[0].stdout == rr[1].stdout and all(r.returncode == 0 for r in rr)
    open(os.path.join(RUNS, name + '.out'), 'wb').write(rr[0].stdout)
    outs[name] = rr[0].stdout.decode()
    print('%-26s deterministic=%s rc=%s,%s sha256=%s' % (name, det, rr[0].returncode, rr[1].returncode, sha(rr[0].stdout)))
    det_ok &= det

R = {}
for name, txt in outs.items():
    for line in txt.splitlines():
        if line.startswith('RESULT '):
            parts = line.split()[1:]
            key = parts[0]
            if '=' in key:
                for p in parts:
                    k, v = p.split('=', 1); R[k] = v
            else:
                R[key] = dict(p.split('=', 1) for p in parts[1:])
c7 = sha(outs['upstream_p3_fixtures_op'].encode()) == P3_DIGEST
controls = {
    'C1 positive (Q3, Gamma(Q3))': R.get('C1') == 'GREEN',
    'C2 existence can fail (K_B, SEP)': R.get('C2_existence_fails') == 'GREEN',
    'C2 mutated cut': R.get('C2_mutated_cut') == 'GREEN',
    'C3 U-weak can fail (K_mut)': R.get('C3_uweak_fails') == 'GREEN',
    'C4 nullspace countercontrol': R.get('C4') == 'GREEN',
    'C5 identification of R = O(3)': R.get('C5') == 'GREEN',
    'C6 U-strong can fail / can pass': R.get('C6', {}).get('ustrong_fail_KGamma') == 'GREEN' and R.get('C6', {}).get('ustrong_pass_Q3_GQ3') == 'GREEN',
    'C7 upstream p3 digest': c7,
    'determinism (2 runs, rc 0)': det_ok,
}
n1 = R.get('N1_maxcone_ext_rank1_and_gamma') == 'GREEN'
cands = []
for key, label in (('N3_KZF', 'K(Z_F) = (Q3 n Z_F*) + cone(Z_F)'), ('N4_L', 'L = Q3 n Z_F*'), ('N5_KGamma', 'K_Gamma = Q3 + R+ Gamma(B)')):
    d = R.get(key, {})
    need = ['domain', 'existence_all_marginals', 'uweak_all_marginals', 'distinct'] + (['pure_classification'] if 'pure_classification' in d else [])
    if n1 and d and all(d.get(k) == 'GREEN' for k in need):
        cands.append((label, d.get('ustrong'), d.get('uweakSO')))
lines = []
lines.append('CONTROLS')
for k, v in controls.items(): lines.append('  %-36s %s' % (k, 'GREEN' if v else 'RED'))
lines.append('  %-36s %s' % ('N1 maxCone extreme rays (input)', 'GREEN' if n1 else 'RED'))
allc = all(controls.values()) and n1
if not allc:
    lines.append('FORK VERDICT: VOID (a control or N1 is not green; no verdict is rendered)')
elif cands:
    lines.append('FORK VERDICT: RETIRE branch of the frozen rule (PREREG section 3).')
    lines.append('  %d exact domain cone(s) other than Q3 and Gamma(Q3) satisfy E and U-weak at every marginal:' % len(cands))
    for label, us, uso in cands:
        lines.append('    - %s   [U-strong: %s%s]' % (label, us, '; U-weak-SO: %s' % uso if uso else ''))
    lines.append('  OP-weak => OP-strong is therefore false on the domain (each listed cone fails U-strong).')
    lines.append('  Wording (owner scope clarification, PR #864 comment 6247198574): OP-weak is INSUFFICIENT ALONE as a standalone')
    lines.append('  cone-selection condition under the tested premises. This is not a global rejection of purification as a')
    lines.append('  component of a later, independently sourced X; G2, G3 and G6 are unchanged.')
    n7 = R.get('N7', {})
    lines.append('  Side (record-only): the K(Z_F) and L counterexamples are invariant under %s native permutations (PC=%s).' % (n7.get('native_perm_invariant'), n7.get('PC')))
    m = R.get('N6_maxCone', {})
    lines.append('  Side (record-only, N6): maxCone U-strong=%s, TS-a=%s, TS-b=%s, PC=%s.' % (m.get('ustrong'), m.get('TS_a'), m.get('TS_b'), m.get('PC')))
else:
    lines.append('FORK VERDICT: UNDECIDED by computation (no candidate cone certified; KEEP needs a written argument).')
txt = '\n'.join(lines) + '\n'
open(os.path.join(RUNS, 'verdict.out'), 'w').write(txt)
print(txt, end='')
sums = []
for d in ('probes', 'runs'):
    for f in sorted(os.listdir(os.path.join(ROOT, d))):
        p = os.path.join(ROOT, d, f)
        if f in ('SHA256SUMS', 'replay.log') or not os.path.isfile(p): continue
        sums.append('%s  %s/%s' % (sha(open(p, 'rb').read()), d, f))
open(os.path.join(RUNS, 'SHA256SUMS'), 'w').write('\n'.join(sums) + '\n')
print('REPLAY', 'GREEN' if allc else 'RED')
