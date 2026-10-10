#!/usr/bin/env python3
"""Thread X (EXOT), node X4 -- exact instance tests of self-duality for single-defect cones, with countercontrols.

Run (cwd pt/X/): python3 -I -B x2_k1_selfdual.py > x2_k1_selfdual.out 2> x2_k1_selfdual.err

Density-matrix form (ipW = 4 tr, so every ratio below is scale-free). For a Hermitian defect e (tr e > 0, e not PSD)
the single-defect cone is K(e) = (PSD n e^*) + R_+ e. Written lemma SD1 (NOTES N4, RESULT 1): K(e) is self-dual iff
  (GL)  for every z >= 0 with tr(z e) < 0:  z + tau e >= 0, where tau = -tr(z e)/tr(e e)
(tau e is the orthogonal correction that puts z + tau e on the hyperplane e^perp), and (GL) holds whenever
e >= beta (I - 2 g g^*) for a unit g and beta > 0. This script does NOT prove SD1; it tests (GL) exactly on finite
families (instance-scoped [X]) and runs the self-duality procedure with its controls:
  T1  (GL) for e = pauliW(E0) on every Gaussian-integer vector v in {a+bi : a,b in {-1,0,1}}^4 (z = v v^*);
  T2  (GL) on rank-2 real mixtures (all pairs of the 80 nonzero vectors in {-1,0,1}^4);
  T3  (GL) on rank-3 real mixtures (all triples of 40 sign-representatives);
  T4  (GL) on rank-2 complex mixtures (pairs of 60 Gaussian representatives).
Countercontrols (each must be REJECTED by the same test):
  C1  e_c = (I + (3/2)(X(x)Z - Y(x)Y))/4: spectrum {1, 4, -2, 1}/4 violates e >= beta(I - 2gg^*); (GL) must fail on T1;
  C2  W = (|phi><phi|)^{T_B}, phi = (24|00> + 7|11>)/25 (block-positive, spectrum {576, 49, 168, -168}/625):
      (GL) must fail on T1;
  C3  the procedure must reject maxCone and K_E (generator pair E0, P_v with negative pairing), and SEP and K_gen
      (dual probe E0 not in the cone, since it is not PSD); and must accept Q3 (pairings of PSD tables >= 0 on
      the T1 family; dual probes = the same family, all PSD).

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1. One PASS/FAIL line per check, tagged (enumerate, witness, countercontrol); counts printed as INFO.
  R2. A T-check PASSES iff (GL) holds on every member of its family with tr(z e) < 0 and that subfamily is nonempty.
  R3. A countercontrol PASSES iff the test REJECTS the control object (at least one exact failure, printed).
  R4. VERDICT only if all checks pass; else 'X2-K1-SELFDUAL: FAILED -- <ids>' and exit 1.
  R5. Exact arithmetic only (fractions.Fraction); no floating point, randomness or timing.
"""
import sys
from fractions import Fraction as Fr
from itertools import combinations, product

CHECKS = []


def chk(cid, name, ok, kind):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}", flush=True)


def section(t):
    print()
    print(f"== {t}", flush=True)


R4 = range(4)
I4 = [[Fr(int(i == j)) for j in R4] for i in R4]
XZ = [[0, 0, 1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, -1, 0, 0]]        # X (x) Z, basis |00>,|01>,|10>,|11>
YY = [[0, 0, 0, -1], [0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0]]        # Y (x) Y (real)


def lin(*terms):
    """sum of coefficient * real 4x4 matrix"""
    return [[sum(Fr(c) * Fr(M[i][j]) for c, M in terms) for j in R4] for i in R4]


E_E0 = lin((Fr(1, 4), I4), (Fr(1, 4), XZ), (Fr(-1, 4), YY))            # pauliW(E0)
E_C = lin((Fr(1, 4), I4), (Fr(3, 8), XZ), (Fr(-3, 8), YY))              # pauliW(e_c), c = 3/2
a, b = Fr(24, 25), Fr(7, 25)
E_W = [[a * a, 0, 0, 0], [0, 0, a * b, 0], [0, a * b, 0, 0], [0, 0, 0, b * b]]   # (|phi><phi|)^{T_B}
E_W = [[Fr(x) for x in row] for row in E_W]


def herm_of(vs):
    """sum_k v_k v_k^* for Gaussian-integer vectors v_k given as lists of (re, im); returns (Re, Im)."""
    Re = [[Fr(0)] * 4 for _ in R4]
    Im = [[Fr(0)] * 4 for _ in R4]
    for v in vs:
        for i in R4:
            for j in R4:
                (p, q), (r, s) = v[i], v[j]          # v_i conj(v_j) = (p + iq)(r - is)
                Re[i][j] += p * r + q * s
                Im[i][j] += q * r - p * s
    return Re, Im


def tr_real(Re, e):
    return sum(Re[i][j] * e[j][i] for i in R4 for j in R4)


def psd_real_sym(M):
    """exact PSD test of a real symmetric Fraction matrix by Schur-complement pivoting."""
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
    n = 4
    big = [[Fr(0)] * 8 for _ in range(8)]
    for i in range(n):
        for j in range(n):
            big[i][j] = Re[i][j]
            big[i + n][j + n] = Re[i][j]
            big[i][j + n] = -Im[i][j]
            big[i + n][j] = Im[i][j]
    return psd_real_sym(big)


def gl_test(vs, e, tee):
    """returns None if tr(z e) >= 0; True/False for (GL) otherwise."""
    Re, Im = herm_of(vs)
    t = tr_real(Re, e)
    if t >= 0:
        return None
    tau = -t / tee
    Re2 = [[Re[i][j] + tau * e[i][j] for j in R4] for i in R4]
    return psd_herm(Re2, Im)


def run_family(fam, e):
    tee = sum(e[i][j] * e[i][j] for i in R4 for j in R4)
    neg = good = 0
    first_bad = None
    for vs in fam:
        r = gl_test(vs, e, tee)
        if r is None:
            continue
        neg += 1
        if r:
            good += 1
        elif first_bad is None:
            first_bad = vs
    return neg, good, first_bad


# ---- families (deterministic enumeration)
UNITS = [(Fr(p), Fr(q)) for p in (-1, 0, 1) for q in (-1, 0, 1)]
GAUSS = [list(v) for v in product(UNITS, repeat=4) if any(c != (0, 0) for c in v)]
REAL = [[(Fr(p), Fr(0)) for p in v] for v in product((-1, 0, 1), repeat=4) if any(v)]


def first_nonzero(v):
    return next(c for c in v if c != (0, 0))


REP40 = [v for v in REAL if first_nonzero(v) == (1, 0)]
G5 = [(Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(-1), Fr(0)), (Fr(0), Fr(1)), (Fr(0), Fr(-1))]
GREP = [list(v) for v in product(G5, repeat=4) if any(c != (0, 0) for c in v) and first_nonzero(v) == (1, 0)]
GREP60 = GREP[:60]
FAMS = [('T1', 'pure states z = v v^*, v Gaussian-integer in {a+bi: a,b in {-1,0,1}}^4', [[v] for v in GAUSS]),
        ('T2', 'rank-2 real mixtures, all pairs of the 80 nonzero vectors of {-1,0,1}^4',
         [list(p) for p in combinations(REAL, 2)]),
        ('T3', 'rank-3 real mixtures, all triples of 40 sign-representatives', [list(t) for t in combinations(REP40, 3)]),
        ('T4', 'rank-2 complex mixtures, all pairs of 60 Gaussian representatives',
         [list(p) for p in combinations(GREP60, 2)])]
print(f"INFO family sizes: T1={len(FAMS[0][2])} T2={len(FAMS[1][2])} T3={len(FAMS[2][2])} T4={len(FAMS[3][2])}")


def show(vs):
    return ' + '.join('v v^*, v=(' + ', '.join(f"{p}{'+' if q >= 0 else '-'}{abs(q)}i" for p, q in v) + ')' for v in vs)


# =====================================================================================================
section('T  (GL) for e = pauliW(E0) on exact families (instance-scoped; the universal statement is lemma SD1 [W])')
for tid, desc, fam in FAMS:
    neg, good, bad = run_family(fam, E_E0)
    print(f"INFO {tid}: members with tr(z e) < 0: {neg}; (GL) holds on {good}")
    chk(tid, f'(GL) holds on every member with tr(z e) < 0 of: {desc}', neg > 0 and good == neg and bad is None,
        'enumerate')

# =====================================================================================================
section('C  countercontrols: the same test must reject defects that violate e >= beta(I - 2 g g^*)')
for cid, desc, e in [('C1', 'e_c = (I + (3/2)(X(x)Z - Y(x)Y))/4 (not in maxCone; spectrum {1,4,-2,1}/4)', E_C),
                     ('C2', 'W = (|phi><phi|)^{T_B}, phi = (24|00> + 7|11>)/25 (block-positive; spectrum '
                            '{576, 49, 168, -168}/625)', E_W)]:
    neg, good, bad = run_family(FAMS[0][2], e)
    print(f"INFO {cid}: members with tr(z e) < 0: {neg}; (GL) holds on {good}; first failure: "
          f"{show(bad) if bad else 'none'}")
    chk(cid, f'(GL) fails on T1 for {desc}: K(e) is not self-dual (witness x = z + tau e in K(e)^* \\ K(e))',
        bad is not None, 'countercontrol')

# =====================================================================================================
section('P  the self-duality procedure: accept Q3 and K1, reject maxCone, K_E, SEP, K_gen')
pure = [herm_of([v]) for v in REAL]
q3_s1 = all(sum(Re1[i][j] * Re2[j][i] - Im1[i][j] * Im2[j][i] for i in R4 for j in R4) >= 0
            for (Re1, Im1), (Re2, Im2) in combinations(pure, 2))
q3_s2 = all(psd_herm(Re, Im) for Re, Im in pure)
chk('P1', 'Q3 accepted: (S1) pairings tr(z z\') >= 0 on the 80 real pure states; (S2) the dual probes (Q3^* = Q3 '
    '[K JordanClassification.lean:84]) are PSD', q3_s1 and q3_s2, 'countercontrol')
vbad = [(Fr(1), Fr(0)), (Fr(-1), Fr(0)), (Fr(-1), Fr(0)), (Fr(-1), Fr(0))]
ReV, ImV = herm_of([vbad])
pair_E0_Pv = 4 * tr_real(ReV, E_E0) / 4                 # ipW(E0, P_v) with |v|^2 = 4
chk('P2', 'maxCone and K_E rejected by (S1): E0 (in K_E, x1_k1_core C2 + B1) and P_v (in Q3, contained in K_E) '
    'have ipW(E0, P_v) = -1 < 0', pair_E0_Pv == -1, 'countercontrol')
chk('P3', 'SEP and K_gen rejected by (S2): the dual probe E0 (in maxCone = SEP^* and K_E = K_gen^*) is not PSD, '
    'and SEP <= K_gen <= Q3', not psd_herm(E_E0, [[Fr(0)] * 4 for _ in R4]), 'countercontrol')
chk('P4', 'K1 accepted: (S1) generators E0 and PSD z with tr(z e) >= 0 pair nonnegatively by construction, '
    'ipW(E0, E0) = 4 tr(e e) = 3; (S2) the dual probes z + tau E0 from T1-T4 are PSD on E0^perp (T1-T4)',
    4 * sum(E_E0[i][j] ** 2 for i in R4 for j in R4) == 3 and all(c[2] for c in CHECKS if c[0] in
                                                                    ('T1', 'T2', 'T3', 'T4')), 'witness')

# =====================================================================================================
print()
failed = [c[0] for c in CHECKS if not c[2]]
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('enumerate', 'witness', 'countercontrol')), flush=True)
if failed:
    print(f"X2-K1-SELFDUAL: FAILED -- {len(failed)} of {len(CHECKS)}: {', '.join(failed)}", flush=True)
    sys.exit(1)
print(f'VERDICT X2-K1-SELFDUAL-INSTANCES -- {len(CHECKS)} checks (instance-scoped; universal step = lemma SD1 [W])',
      flush=True)
