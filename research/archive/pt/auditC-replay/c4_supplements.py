#!/usr/bin/env python3
"""Thread C (FOUR-COMP) -- c4: two supplements.

Research only. Exact arithmetic (sympy Rationals); no floating point, no randomness, no time in stdout. Usage:
    python3 -I -B c4_supplements.py <inputs>/fourcopy

S1  The foil K_c = cone(SEP u cnot SEP) of c1 is not IE1: phiW lies in K_c, a rotation R maps it (actC R) to the table G
    of c1, and the effect E0 of c1 (in dualW K_c) takes -1 on G. So the models built on K_c (uniform K_c, and the
    hybrids on (Q3, Q3, K_c, K_c) and (K_c, K_c, Q3, Q3)) violate the conclusion C of the audited theorem, not only FCC.
S2  Where the design proof consumes FCC: source checks that the headline reads the hypothesis only through
    target01/target02 and the parity witnesses, and that the IE1 lemmas read PairLinked.upper / .lower with the two
    link arguments fixed to tables supplied by the gates (Bell tables, rotated links).

DECISION RULE (fixed before the first run). Every check prints PASS or FAIL; a [countercontrol] passes exactly when the
mutated object gives the opposite verdict. 'VERDICT C4-SUPPLEMENTS-EXACT' is printed if and only if every check passes;
otherwise 'VERDICT NOT RENDERED' with the failed ids, and exit status 1.
"""
import re
import sys
from pathlib import Path

import sympy as sp

R4 = range(4)
CHECKS = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def note(cid, text):
    print(f"NOTE [written] {cid}  -- {text}", flush=True)


def section(title):
    print()
    print(f"== {title}", flush=True)


if len(sys.argv) != 2:
    print('usage: c4_supplements.py <inputs/fourcopy dir>')
    sys.exit(2)
FCP = Path(sys.argv[1])

S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
SS = [[sp.kronecker_product(S[m], S[n]) for n in R4] for m in R4]


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * SS[m][n]
    return out / 4


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in R4 for n in R4)


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = R
    return M


def actC(R, w):
    return homMap(R) * w


phiW = sp.diag(1, 1, -1, 1)
E0 = sp.zeros(4, 4)
E0[0, 0], E0[1, 3], E0[2, 2] = 1, 1, -1
G = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0], [0, -1, 0, 0]])

# ===============================================================================================================
section('S1  K_c is not IE1')

Rk = sp.Matrix([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])
chk('N1', 'R = [[0,0,-1],[0,-1,0],[-1,0,0]] is a rotation (R^T R = I, det R = 1)', Rk.T * Rk == sp.eye(3)
    and Rk.det() == 1, 'witness')
chk('N2', 'actC R phiW = G, the table of c1 (c1 K5: pauliW G = psi psi^T)', actC(Rk, phiW) == G, 'witness')
chk('N3', 'ipW E0 G = -1 (E0 in dualW K_c by c1 K1-K3 and note K.W): G is not in K_c, while phiW is (c1 K6)',
    ipW(E0, G) == -1, 'witness')
ev = pauliW(G).eigenvals()
chk('N3c', 'countercontrol: G lies in Q3 (pauliW G has eigenvalues 1, 0, 0, 0): the same rotation keeps phiW inside Q3, '
    'so the failure is a property of K_c', ev == {1: 1, 0: 3}, 'countercontrol', f'eigenvalues {ev}')
note('N.R', 'IE1 fails for K_c (phiW in K_c, actC R phiW not in K_c). With cnot gates and identity locals every '
     'orientation bit is false, so EvenCycle holds and C fails through IE1 for uniform K_c, for (Q3, Q3, K_c, K_c) '
     'and for (K_c, K_c, Q3, Q3).')

# ===============================================================================================================
section('S2  where the design proof consumes FCC (source checks; the reading is written)')

HEAD = (FCP / 'FourCopyHeadline.lean').read_text(encoding='utf-8')
IE1 = (FCP / 'FourCopyIE1.lean').read_text(encoding='utf-8')
uses_head = sorted(set(re.findall(r'FourCopyCoherent\.target0[12] h|parity_all K N A B A\' B\' hcls hadm hgate hinv hie h'
                                  r'|\(hie \.p13\)\)\.2\.2 h', HEAD)))
chk('U1', 'FourCopyHeadline: the FCC hypothesis h enters ie1_all through target01 h and target02 h, and parity_all '
    'through kt4_parity_of_witnesses', 'have h01 := step .p01 .p23 .p02 .p13 (FourCopyCoherent.target01 h)' in HEAD
    and 'have h02 := step .p02 .p13 .p01 .p23 (FourCopyCoherent.target02 h)' in HEAD
    and '(hie .p13)).2.2 h' in HEAD and 'cross_rel (FourCopyCoherent.target01 h)' in HEAD, 'source',
    f'{len(uses_head)} distinct use patterns')
pats = ['exact h.upper X hX Y hY _ ea _ eb', 'exact h.lower _ sa _ sb e he f hf', 'exact h.lower _ hL _ hb e he f hf',
        'exact h.lower _ ha _ hL e he f hf', 'have hv := h.famI _ hX _ hY _ hE _ hF']
counts = {p: IE1.count(p) for p in pats}
chk('U2', 'FourCopyIE1: PairLinked is read only as h.upper at (X, Y, Bell effect ea, Bell effect eb), h.lower at '
    '(Bell state sa, Bell state sb, e, f), h.lower at (rotated link hL, Bell table hb or ha, e, f), and famI at the '
    'four parity witnesses', all(counts[p] >= 1 for p in pats) and len(re.findall(r'\bh\.(upper|lower|famI|famII)\b',
                                                                               IE1)) == sum(counts.values()), 'source',
    f'occurrences {list(counts.values())}')
chk('U2c', 'countercontrol: the pattern search is not vacuous (a mutated pattern is absent)',
    IE1.count('exact h.upper _ sa _ sb e he f hf') == 0, 'countercontrol')
note('U.W', 'reading (written): every use of FCC in FourCopyHeadline and FourCopyIE1 (the headline path; '
     'FourCopyParity\'s incl_I and incl_II are likewise stated at link tables) fixes the two link-pair arguments to tables '
     'supplied by the gates (gate images of product states, the Bell tables and their rotated forms, and the gate '
     'images of sharp product effects) and leaves the target-pair arguments free. So, relative to hcls, hadm, hcl and '
     'hgate, the proof needs FCC only at these link instances. Not kernel-checked in that restricted form (UNBUILT).')

# ===============================================================================================================
print()
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}" for k in ('witness', 'source', 'countercontrol')),
      flush=True)
failed = [c[0] for c in CHECKS if not c[2]]
if failed:
    print(f"{len(CHECKS) - len(failed)}/{len(CHECKS)} checks; failed: {', '.join(failed)}", flush=True)
    print('VERDICT NOT RENDERED', flush=True)
    sys.exit(1)
print(f'{len(CHECKS)}/{len(CHECKS)} checks', flush=True)
print('VERDICT C4-SUPPLEMENTS-EXACT', flush=True)
