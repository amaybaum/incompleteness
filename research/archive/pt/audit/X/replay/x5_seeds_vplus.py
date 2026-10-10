#!/usr/bin/env python3
"""Thread X (EXOT), nodes X2/X3 -- the seed F, the V+ sub-problem, and the one-parameter family K(e_c).

Run (cwd pt/X/): python3 -I -B x5_seeds_vplus.py > x5_seeds_vplus.out 2> x5_seeds_vplus.err

Checked exactly:
  S  the seed F = E00/2 - T_psi/4 with T_psi = actT R_H phiW (R_H as in the landed probe kt4_prem1_probe.py:119)
     equals the defect e_(1,1) of x3_g16_k4; cnot F = e_(-1,-1); ipW(F, cnot F) = 0. Hence cone(K_gen u {F})
     extends to the two-defect cone K2F = K({F, cnot F}) (lemma SD2) and to K4.
  V  V+ and V- (the +1/-1 eigenspaces of cnot) have dimensions 10 and 6; <k, cnot k> = |k+|^2 - |k-|^2 (symbolic);
     the pinching identity (rho + CNOT rho CNOT)/2 = P+ rho P+ + P- rho P- and, for a pure product |ab>,
     P- |ab> = (a1 (b0 - b1)/sqrt 2) |1->, P+ |ab> = a0 b0 |00> + a0 b1 |01> + (a1 (b0 + b1)/sqrt 2) |1+>
     (symbolic, complex a, b): the generators of K_gen+ = K_gen n V+ are the symmetrized products
     (|v_ab><v_ab|, |<1-|ab>|^2); E0 lies in V+ and outside PSD(3) + R_+ (= Q3 n V+).
  F  the family e_c = E00 + c (E13 - E22): cnot-fixed; pauliW(e_c) has spectrum {1-2c, 1, 1+2c, 1}/4 on the basis
     (g, f1, f3, f4); ipW(e_c, prodState x y) = (1 - c) + c (1 + x1 y3 - x2 y2) (symbolic), so e_c is in maxCone
     for 0 <= c <= 1; the SD1 certificate pauliW(e_c) - ((2c-1)/4)(I - 2 g g^T) equals diag(0, (1-c)/2, 1/2, (1-c)/2)
     in the basis (g, f1, f3, f4) (symbolic in c), PSD exactly when c <= 1. Instance c = 3/4 (strict) recorded.
Countercontrols: (Sc) ipW(F, F) = 1/4 != 0 (the orthogonality test is not vacuous: it separates distinct defects from
equal ones); (Vc) the axis product prodState(e1, e3) (|+0>) has nonzero V- part (the projector test is not vacuous); (Fc) for c = 3/2 the
certificate has a negative diagonal entry (the c <= 1 condition is load-bearing).

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1. One PASS/FAIL line per check, tagged (identity, enumerate, witness, countercontrol).
  R2. A countercontrol PASSES iff the test REJECTS the control object.
  R3. VERDICT only if all checks pass; else 'X5-SEEDS-VPLUS: FAILED -- <ids>' and exit 1.
  R4. Exact arithmetic only (sympy rationals and sqrt(2) as an exact algebraic number); no floats or randomness.
"""
import sys

import sympy as sp

R4 = range(4)
iu = sp.I
CHECKS = []


def chk(cid, name, ok, kind):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}", flush=True)


def section(t):
    print()
    print(f"== {t}", flush=True)


def mzero(M):
    return all(sp.simplify(sp.expand(v)) == 0 for v in M)


SGN_NEG = {(1, 3), (2, 2)}
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in SGN_NEG else 1) * w[PC[m][n], PT[m][n]])


def ipW(a, b):
    return sum(a[m, n] * b[m, n] for m in R4 for n in R4)


def E(m, n):
    M = sp.zeros(4, 4)
    M[m, n] = 1
    return M


SIG = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
SS = [[sp.kronecker_product(SIG[m], SIG[n]) for n in R4] for m in R4]


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * SS[m][n]
    return out / 4


E00 = E(0, 0)
CNOTU = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

# =====================================================================================================
section('S  the seed F (Thread A / S2 dual witness) is one of the four defects')
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
H4 = sp.diag(1, RH)
phiW = sp.diag(1, 1, -1, 1)
Tpsi = phiW * H4.T                                   # actT R_H phiW: (actT N w)[m, :] = homMap(N) w[m, :]
F = E00 / 2 - Tpsi / 4
T11 = E(0, 0) + E(1, 3) + E(2, 2) + E(3, 1)
Tmm = E(0, 0) - E(1, 3) - E(2, 2) + E(3, 1)
chk('S1', 'T_psi = actT R_H phiW = E00 + E13 + E22 + E31 = T_(1,1); F = E00/2 - T_psi/4 = e_(1,1)',
    Tpsi == T11 and F == E00 / 2 - T11 / 4, 'identity')
chk('S2', 'cnot F = E00/2 - (E00 - E13 - E22 + E31)/4 = e_(-1,-1), and ipW(F, cnot F) = 0',
    cnot(F) == E00 / 2 - Tmm / 4 and ipW(F, cnot(F)) == 0, 'identity')
chk('Sc', 'countercontrol: ipW(F, F) = 1/4 (the orthogonality test separates a defect from itself)',
    ipW(F, F) == sp.Rational(1, 4), 'countercontrol')

# =====================================================================================================
section('V  the V+ sub-problem: dimensions, the |k-| <= |k+| identity, the symmetrized products, E0 in V+')
C16 = sp.zeros(16, 16)
for k in range(16):
    img = cnot(E(k // 4, k % 4))
    for i in range(16):
        C16[i, k] = img[i // 4, i % 4]
chk('V1', 'dim V+ = rank (I + cnot)/2 = 10 and dim V- = rank (I - cnot)/2 = 6',
    ((sp.eye(16) + C16) / 2).rank() == 10 and ((sp.eye(16) - C16) / 2).rank() == 6, 'enumerate')
ksym = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'k{m}{n}', real=True))
kp, km = (ksym + cnot(ksym)) / 2, (ksym - cnot(ksym)) / 2
chk('V2', '<k, cnot k> = |k+|^2 - |k-|^2 for a generic table k, symbolic (so every k in a cnot-invariant self-dual '
    'cone has |k-| <= |k+|)', sp.expand(ipW(ksym, cnot(ksym)) - ipW(kp, kp) + ipW(km, km)) == 0, 'identity')
rs = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'r{i}{j}'))
Pp, Pm = (sp.eye(4) + CNOTU) / 2, (sp.eye(4) - CNOTU) / 2
chk('V3', 'pinching: (rho + CNOT rho CNOT)/2 = P+ rho P+ + P- rho P-, symbolic (P+- the CNOT eigenprojectors)',
    mzero((rs + CNOTU * rs * CNOTU) / 2 - Pp * rs * Pp - Pm * rs * Pm), 'identity')
a0, a1, b0, b1 = sp.symbols('a0 a1 b0 b1')
ab = sp.Matrix([a0 * b0, a0 * b1, a1 * b0, a1 * b1])
r2 = sp.sqrt(2)
ket_1p, ket_1m = sp.Matrix([0, 0, 1, 1]) / r2, sp.Matrix([0, 0, 1, -1]) / r2
chk('V4', 'P- |ab> = (a1 (b0 - b1)/sqrt 2) |1->, P+ |ab> = a0 b0 |00> + a0 b1 |01> + (a1 (b0 + b1)/sqrt 2) |1+>, '
    'symbolic: K_gen+ is generated by (|v_ab><v_ab|, |<1-|ab>|^2), v_ab = P+ |ab>',
    mzero(Pm * ab - a1 * (b0 - b1) / r2 * ket_1m)
    and mzero(Pp * ab - (a0 * b0 * sp.Matrix([1, 0, 0, 0]) + a0 * b1 * sp.Matrix([0, 1, 0, 0])
                         + a1 * (b0 + b1) / r2 * ket_1p)), 'identity')
E0 = E(0, 0) + E(1, 3) - E(2, 2)
g = sp.Matrix([1, -1, -1, -1]) / 2
chk('V5', 'E0 lies in V+ (cnot E0 = E0) and outside Q3 n V+ = PSD(3) + R_+ (g^T pauliW(E0) g = -1/4): K1 n V+ is a '
    'self-dual cone of V+ containing K_gen+ and different from PSD(3) + R_+',
    cnot(E0) == E0 and (g.T * pauliW(E0) * g)[0, 0] == sp.Rational(-1, 4), 'witness')
pe1 = sp.Matrix([1, 1, 0, 0]) * sp.Matrix([1, 0, 0, 1]).T          # prodState(e1, e3): |+0>
chk('Vc', 'countercontrol: the axis product prodState(e1, e3) has a nonzero V- part (p != cnot p)',
    pe1 != cnot(pe1), 'countercontrol')

# =====================================================================================================
section('F  the one-parameter family e_c = E00 + c (E13 - E22), c in (1/2, 1]')
c = sp.Symbol('c', real=True)
ec = E(0, 0) + c * (E(1, 3) - E(2, 2))
f1 = sp.Matrix([1, 1, 1, -1]) / 2
f3 = sp.Matrix([1, -1, 1, 1]) / 2
f4 = sp.Matrix([1, 1, -1, 1]) / 2
xs = [sp.Symbol(f'x{i}', real=True) for i in range(3)]
ys = [sp.Symbol(f'y{i}', real=True) for i in range(3)]
pxy = sp.Matrix([1] + xs) * sp.Matrix([1] + ys).T
chk('F1', 'cnot e_c = e_c (symbolic c)', mzero(cnot(ec) - ec), 'identity')
chk('F2', 'pauliW(e_c) = ((1-2c) g g^T + f1 f1^T + (1+2c) f3 f3^T + f4 f4^T)/4, symbolic in c',
    mzero(pauliW(ec) - ((1 - 2 * c) * g * g.T + f1 * f1.T + (1 + 2 * c) * f3 * f3.T + f4 * f4.T) / 4), 'identity')
chk('F3', 'ipW(e_c, prodState x y) = (1 - c) + c (1 + x1 y3 - x2 y2), symbolic: e_c in maxCone for 0 <= c <= 1 '
    '(1 + x1 y3 - x2 y2 >= 0 on the ball, x1_k1_core C2)',
    sp.expand(ipW(ec, pxy) - ((1 - c) + c * (1 + xs[0] * ys[2] - xs[1] * ys[1]))) == 0, 'identity')
cert = pauliW(ec) - (2 * c - 1) / 4 * (sp.eye(4) - 2 * g * g.T)
chk('F4', 'SD1 certificate: pauliW(e_c) - ((2c-1)/4)(I - 2 g g^T) = ((1-c)/2) f1 f1^T + (1/2) f3 f3^T + '
    '((1-c)/2) f4 f4^T, symbolic in c (PSD iff c <= 1); e_c is not PSD iff c > 1/2',
    mzero(cert - ((1 - c) / 2 * f1 * f1.T + f3 * f3.T / 2 + (1 - c) / 2 * f4 * f4.T)), 'identity')
c34 = sp.Rational(3, 4)
chk('F5', 'instance c = 3/4: lowest eigenvalue (1 - 2c)/4 = -1/8 < 0 and certificate coefficients (1-c)/2 = 1/8 > 0: '
    'K(e_{3/4}) meets H1-H3 with a strict SD1 inequality and differs from Q3',
    (1 - 2 * c34) / 4 == sp.Rational(-1, 8) and (1 - c34) / 2 == sp.Rational(1, 8), 'witness')
chk('Fc', 'countercontrol: at c = 3/2 the certificate coefficient (1-c)/2 = -1/4 < 0 (and e_c leaves maxCone, '
    'x1_k1_core C1c): the c <= 1 condition is load-bearing',
    ((1 - c) / 2).subs(c, sp.Rational(3, 2)) == sp.Rational(-1, 4), 'countercontrol')

# =====================================================================================================
print()
failed = [cc[0] for cc in CHECKS if not cc[2]]
print('kinds: ' + ', '.join(f"{k} {sum(1 for cc in CHECKS if cc[1] == k)}"
                            for k in ('identity', 'enumerate', 'witness', 'countercontrol')), flush=True)
if failed:
    print(f"X5-SEEDS-VPLUS: FAILED -- {len(failed)} of {len(CHECKS)}: {', '.join(failed)}", flush=True)
    sys.exit(1)
print(f'VERDICT X5-SEEDS-VPLUS-EXACT -- {len(CHECKS)} checks', flush=True)
