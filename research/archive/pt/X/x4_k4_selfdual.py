#!/usr/bin/env python3
"""Thread X (EXOT), level (ii), node X4 -- exact instance tests of lemma SD2 for K4 = (Q3 n X^*) + cone(X).

Run (cwd pt/X/): python3 -I -B x4_k4_selfdual.py > x4_k4_selfdual.out 2> x4_k4_selfdual.err

Density form (ipW = 4 tr; all ratios scale-free). X = {e_s = (I - 2 P_s)/8}, P_s = psi_s psi_s^T,
psi_s = (1, s1 s2, s1, -s2)/2 (x3_g16_k4 C1-C4). Lemma SD2 (NOTES N6; RESULT 1): for pairwise orthogonal defects each
satisfying (GL), every y = z + sum_s s_s e_s in X^* (z >= 0, s_s >= 0) decomposes as
  y = q + sum_s (s_s - t_s) e_s,  q = z + sum_s t_s e_s,  t_s = max(0, -tr(z e_s)/tr(e_s e_s)) <= s_s,
with q >= 0 and tr(q e_s) >= 0. The universal statement is the written lemma; this script tests exactly:
  E1  q >= 0 (and tr(q e_s) >= 0) for every Gaussian pure state z = v v^*, v in {a+bi: a,b in {-1,0,1}}^4, that has
      some tr(z e_s) < 0;
  E2  the same on rank-2 real mixtures (all pairs of the 80 nonzero vectors of {-1,0,1}^4);
  E3  the same on rank-2 complex mixtures (all pairs of 60 Gaussian representatives);
  E4  (GL) for each single defect e_s on the E1 family;
  E5  the procedure accepts K4: (S1) the generators pair nonnegatively (orthogonal defects, tr(e_s e_s) = 1/16 > 0,
      Q3 n X^* against X by definition, PSD against PSD); (S2) every dual probe q built in E1-E3 is PSD.
Countercontrol:
  Ec  the scaled defects e'_s = (I - 3 P_s)/8 (SD1 hypothesis violated): the same decomposition test must fail on the
      E1 family (exact witness printed), and X' = {e'_s} is not even subdual (tr(e'_s e'_t) < 0 for s != t).

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1. One PASS/FAIL line per check, tagged (enumerate, witness, countercontrol); counts as INFO lines.
  R2. An E-check PASSES iff the decomposition (resp. (GL)) holds on every member of its family with some negative
      pairing, and that subfamily is nonempty.
  R3. A countercontrol PASSES iff the test REJECTS the control object.
  R4. VERDICT only if all checks pass; else 'X4-K4-SELFDUAL: FAILED -- <ids>' and exit 1.
  R5. Exact arithmetic only (fractions.Fraction); no floating point, randomness or timing.
"""
import sys
from fractions import Fraction as Fr
from itertools import combinations, product

CHECKS = []
R4 = range(4)


def chk(cid, name, ok, kind):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}", flush=True)


def section(t):
    print()
    print(f"== {t}", flush=True)


S4 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
PSI = {s: [Fr(1, 2), Fr(s[0] * s[1], 2), Fr(s[0], 2), Fr(-s[1], 2)] for s in S4}


def defect(s, k):            # (I - k P_s)/8
    p = PSI[s]
    return [[(Fr(int(i == j)) - k * p[i] * p[j]) / 8 for j in R4] for i in R4]


EX = {s: defect(s, 2) for s in S4}
EXP = {s: defect(s, 3) for s in S4}


def herm_of(vs):
    Re = [[Fr(0)] * 4 for _ in R4]
    Im = [[Fr(0)] * 4 for _ in R4]
    for v in vs:
        for i in R4:
            for j in R4:
                (p, q), (r, t) = v[i], v[j]
                Re[i][j] += p * r + q * t
                Im[i][j] += q * r - p * t
    return Re, Im


def tr_real(Re, e):
    return sum(Re[i][j] * e[j][i] for i in R4 for j in R4)


def psd_real_sym(M):
    M = [row[:] for row in M]
    act = list(range(len(M)))
    while act:
        if any(M[i][i] < 0 for i in act):
            return False
        for i in act:
            if M[i][i] == 0 and any(M[i][j] != 0 for j in act):
                return False
        piv = next((i for i in act if M[i][i] > 0), None)
        if piv is None:
            return True
        p = M[piv][piv]
        for i in act:
            if i != piv and M[i][piv] != 0:
                f = M[i][piv] / p
                for j in act:
                    M[i][j] -= f * M[piv][j]
        act.remove(piv)
    return True


def psd_herm(Re, Im):
    big = [[Fr(0)] * 8 for _ in range(8)]
    for i in R4:
        for j in R4:
            big[i][j] = big[i + 4][j + 4] = Re[i][j]
            big[i][j + 4] = -Im[i][j]
            big[i + 4][j] = Im[i][j]
    return psd_real_sym(big)


def decomp_test(vs, X):
    """None if every pairing >= 0; else True/False: q = z + sum t_s e_s is PSD with tr(q e_s) >= 0 for all s."""
    Re, Im = herm_of(vs)
    pair = {s: tr_real(Re, X[s]) for s in S4}
    if all(c >= 0 for c in pair.values()):
        return None
    t = {s: max(Fr(0), -pair[s] / tr_real(X[s], X[s])) for s in S4}
    Rq = [[Re[i][j] + sum(t[s] * X[s][i][j] for s in S4) for j in R4] for i in R4]
    return psd_herm(Rq, Im) and all(tr_real(Rq, X[s]) >= 0 for s in S4)


def gl_test(vs, e):
    Re, Im = herm_of(vs)
    c = tr_real(Re, e)
    if c >= 0:
        return None
    tau = -c / tr_real(e, e)
    return psd_herm([[Re[i][j] + tau * e[i][j] for j in R4] for i in R4], Im)


def tally(fam, fn):
    neg = good = 0
    bad = None
    for vs in fam:
        r = fn(vs)
        if r is None:
            continue
        neg += 1
        if r:
            good += 1
        elif bad is None:
            bad = vs
    return neg, good, bad


UNITS = [(Fr(p), Fr(q)) for p in (-1, 0, 1) for q in (-1, 0, 1)]
GAUSS = [list(v) for v in product(UNITS, repeat=4) if any(c != (0, 0) for c in v)]
REAL = [[(Fr(p), Fr(0)) for p in v] for v in product((-1, 0, 1), repeat=4) if any(v)]
G5 = [(Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(-1), Fr(0)), (Fr(0), Fr(1)), (Fr(0), Fr(-1))]
GREP60 = [list(v) for v in product(G5, repeat=4)
          if any(c != (0, 0) for c in v) and next(c for c in v if c != (0, 0)) == (1, 0)][:60]
F1 = [[v] for v in GAUSS]
F2 = [list(p) for p in combinations(REAL, 2)]
F3 = [list(p) for p in combinations(GREP60, 2)]
print(f"INFO family sizes: E1={len(F1)} E2={len(F2)} E3={len(F3)}")


def show(vs):
    return ' + '.join('v v^*, v=(' + ', '.join(f"{p}{'+' if q >= 0 else '-'}{abs(q)}i" for p, q in v) + ')' for v in vs)


# =====================================================================================================
section('E  lemma SD2 on exact families (instance-scoped; the universal step is the written lemma)')
results = {}
for cid, desc, fam in [('E1', 'Gaussian pure states (all v in {a+bi: a,b in {-1,0,1}}^4)', F1),
                       ('E2', 'rank-2 real mixtures (all pairs of the 80 nonzero vectors of {-1,0,1}^4)', F2),
                       ('E3', 'rank-2 complex mixtures (all pairs of 60 Gaussian representatives)', F3)]:
    neg, good, bad = tally(fam, lambda vs: decomp_test(vs, EX))
    results[cid] = (neg, good, bad)
    print(f"INFO {cid}: members with some tr(z e_s) < 0: {neg}; decomposition valid on {good}")
    chk(cid, f'q = z + sum t_s e_s is PSD with tr(q e_s) >= 0 on every member with a negative pairing: {desc}',
        neg > 0 and good == neg and bad is None, 'enumerate')
gl_ok = True
for s in S4:
    neg, good, bad = tally(F1, lambda vs: gl_test(vs, EX[s]))
    print(f"INFO E4 defect s={s}: members with tr(z e_s) < 0: {neg}; (GL) holds on {good}")
    gl_ok = gl_ok and neg > 0 and good == neg
chk('E4', '(GL) holds for each single defect e_s on every Gaussian pure state with tr(z e_s) < 0', gl_ok, 'enumerate')
s1_ok = (all(tr_real(EX[s], EX[t]) == (Fr(1, 16) if s == t else 0) for s in S4 for t in S4))
chk('E5', 'the procedure accepts K4: tr(e_s e_t) = (1/16)[s = t] (subdual defect set; generators of Q3 n X^* pair '
    'nonnegatively with X by definition and with each other as PSD tables), and every dual probe q from E1-E3 is PSD',
    s1_ok and all(results[c][1] == results[c][0] for c in ('E1', 'E2', 'E3')), 'witness')

# =====================================================================================================
section('Ec  countercontrol: defects violating the SD1 hypothesis')
neg, good, bad = tally(F1, lambda vs: decomp_test(vs, EXP))
print(f"INFO Ec: members with a negative pairing: {neg}; decomposition valid on {good}; first failure: "
      f"{show(bad) if bad else 'none'}")
not_subdual = all(tr_real(EXP[s], EXP[t]) < 0 for s in S4 for t in S4 if s != t)
chk('Ec', "the decomposition test rejects X' = {e'_s = (I - 3 P_s)/8}: it fails on the E1 family, and X' is not "
    "subdual (tr(e'_s e'_t) = -1/32 < 0 for s != t)",
    bad is not None and not_subdual and tr_real(EXP[(1, 1)], EXP[(1, -1)]) == Fr(-1, 32), 'countercontrol')

# =====================================================================================================
print()
failed = [c[0] for c in CHECKS if not c[2]]
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('enumerate', 'witness', 'countercontrol')), flush=True)
if failed:
    print(f"X4-K4-SELFDUAL: FAILED -- {len(failed)} of {len(CHECKS)}: {', '.join(failed)}", flush=True)
    sys.exit(1)
print(f'VERDICT X4-K4-SELFDUAL-INSTANCES -- {len(CHECKS)} checks (instance-scoped; universal step = lemma SD2 [W])',
      flush=True)
