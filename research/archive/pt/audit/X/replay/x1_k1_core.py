#!/usr/bin/env python3
"""Thread X (EXOT), node X3/X4 -- exact ingredients of the single-defect cone K1 = (Q3 n E0^*) + R_+ E0.

Run (cwd pt/X/): python3 -I -B x1_k1_core.py > x1_k1_core.out 2> x1_k1_core.err

What is checked (all exact; no floating point, randomness or timing):
  A  primitives: the landed cnot tables (CompositeDimension.lean:741-758) equal conjugation by the CNOT unitary (own
     implementation, control = first qubit); cnot is a signed permutation and an involution (ipW-orthogonal);
     ipW = 4 tr(pauliW pauliW); pauliW(prodState x y) = rho(x) (x) rho(y); det rho(x) = (1 - |x|^2)/4.
  B  E0 = E00 + E13 - E22: cnot E0 = E0; an exact orthonormal eigenbasis of pauliW(E0) with spectrum {-1,1,1,3}/4;
     the certificate pauliW(E0) - (1/4)(I - 2 g g^T) = (1/2) f f^T (the hypothesis of lemma SD1 in NOTES N4).
  C  H1 over the continuous family: ipW(E0, prodState x y) = 1 + x1 y3 - x2 y2 and an SOS identity proving it >= 0
     for x, y in the closed ball; products lie in Q3 (A4, A5).
  D  H2: pauliW(cnot w) = CNOT pauliW(w) CNOT for a generic table w; ipW(cnot w, E0) = ipW(w, E0).
  F  the witness pair: X = E0 (in K1, not PSD) and P_v, v = (1,-1,-1,-1), with ipW(E0, P_v) = -1 < 0.
Countercontrols: the H1 test rejects e_c = E00 + (3/2)(E13 - E22) (negative product value); the H2 test rejects
twin = actT reflY Q3 (idW in twin, cnot idW = chainW has a negative product-effect value); the PSD test rejects E0;
the product-rank test rejects P_v as a product.

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1. One PASS/FAIL line per check, tagged with its kind (identity, enumerate, witness, countercontrol).
  R2. A countercontrol PASSES when the test it controls REJECTS the control object.
  R3. The VERDICT line prints only if every check (countercontrols included) passes; otherwise print
      'X1-K1-CORE: FAILED -- <ids>' and exit 1.
  R4. Exact arithmetic only (sympy rationals / Gaussian rationals).
"""
import sys
from itertools import product

import sympy as sp

Q = sp.Rational
iu = sp.I
R4 = range(4)
CHECKS = []


def chk(cid, name, ok, kind):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}", flush=True)


def section(t):
    print()
    print(f"== {t}", flush=True)


def mzero(M):
    return all(sp.expand(v) == 0 for v in M)


# ---- landed tables (CompositeDimension.lean:741-758), transcribed
SGN_NEG = {(1, 3), (2, 2)}
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in SGN_NEG else 1) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def prodState(x, y):
    return hom(x) * hom(y).T


def ipW(a, b):
    return sum(a[m, n] * b[m, n] for m in R4 for n in R4)


SIG = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
SS = [[sp.kronecker_product(SIG[m], SIG[n]) for n in R4] for m in R4]


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * SS[m][n]
    return out / 4


def table_of(rho):
    return sp.Matrix(4, 4, lambda m, n: sp.expand((SS[m][n] * rho).trace()))


def rho1(x):
    return (SIG[0] + x[0] * SIG[1] + x[1] * SIG[2] + x[2] * SIG[3]) / 2


def E(m, n):
    M = sp.zeros(4, 4)
    M[m, n] = 1
    return M


CNOTU = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])   # control = first qubit
E00 = E(0, 0)
E0 = E(0, 0) + E(1, 3) - E(2, 2)
wsym = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'w{m}{n}', real=True))
xs = [sp.Symbol(f'x{i}', real=True) for i in range(3)]
ys = [sp.Symbol(f'y{i}', real=True) for i in range(3)]

# =====================================================================================================
section('A  primitives (own implementation, compared with the landed tables)')
chk('A1', 'landed cnot table = conjugation by CNOT (control = first qubit) on all 16 basis tables',
    all(mzero(pauliW(cnot(E(a, b))) - CNOTU * pauliW(E(a, b)) * CNOTU) for a in R4 for b in R4), 'enumerate')
perm = sorted((PC[m][n], PT[m][n]) for m in R4 for n in R4)
chk('A2', 'cnot is a signed permutation of the 16 entries and an involution (hence ipW-orthogonal)',
    perm == sorted((a, b) for a in R4 for b in R4) and cnot(cnot(wsym)) == wsym, 'enumerate')
vsym = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'v{m}{n}', real=True))
chk('A3', 'ipW(w, v) = 4 tr(pauliW w pauliW v), symbolic',
    sp.expand(ipW(wsym, vsym) - 4 * (pauliW(wsym) * pauliW(vsym)).trace()) == 0, 'identity')
chk('A4', 'pauliW(prodState x y) = rho(x) (x) rho(y), symbolic',
    mzero(pauliW(prodState(xs, ys)) - sp.kronecker_product(rho1(xs), rho1(ys))), 'identity')
chk('A5', 'tr rho(x) = 1 and det rho(x) = (1 - |x|^2)/4, symbolic (so rho(x) >= 0 on the closed ball)',
    sp.expand(rho1(xs).trace() - 1) == 0
    and sp.expand(rho1(xs).det() - (1 - xs[0] ** 2 - xs[1] ** 2 - xs[2] ** 2) / 4) == 0, 'identity')

# =====================================================================================================
section('B  E0: cnot-fixed; exact spectral decomposition; the SD1 certificate')
g = sp.Matrix([1, -1, -1, -1]) / 2
f1 = sp.Matrix([1, 1, 1, -1]) / 2
f3 = sp.Matrix([1, -1, 1, 1]) / 2
f4 = sp.Matrix([1, 1, -1, 1]) / 2
BAS = [g, f1, f3, f4]
RE0 = pauliW(E0)
chk('B1', 'cnot E0 = E0', cnot(E0) == E0, 'witness')
chk('B2', '{g, f1, f3, f4} orthonormal and pauliW(E0) = (1/4)(-g g^T + f1 f1^T + 3 f3 f3^T + f4 f4^T)',
    all((BAS[i].T * BAS[j])[0, 0] == (1 if i == j else 0) for i in R4 for j in R4)
    and mzero(RE0 - (-g * g.T + f1 * f1.T + 3 * f3 * f3.T + f4 * f4.T) / 4), 'identity')
chk('B3', 'SD1 certificate: pauliW(E0) - (1/4)(I - 2 g g^T) = (1/2) f3 f3^T  (>= 0, rank one)',
    mzero(RE0 - (sp.eye(4) - 2 * g * g.T) / 4 - f3 * f3.T / 2), 'identity')
chk('B4', 'E0 is not in Q3: g^T pauliW(E0) g = -1/4; tr pauliW(E0) = 1 > 0 (so -E0 is not in Q3)',
    (g.T * RE0 * g)[0, 0] == Q(-1, 4) and RE0.trace() == 1, 'witness')
chk('B5', 'ipW(E0, E0) = 3 >= 0 and ipW(E0, E00) = 1', ipW(E0, E0) == 3 and ipW(E0, E00) == 1, 'witness')

# =====================================================================================================
section('C  H1 over the continuous product family (symbolic identities)')
val = ipW(E0, prodState(xs, ys))
chk('C1', 'ipW(E0, prodState x y) = 1 + x1 y3 - x2 y2, symbolic',
    sp.expand(val - (1 + xs[0] * ys[2] - xs[1] * ys[1])) == 0, 'identity')
sos = ((xs[0] + ys[2]) ** 2 + (ys[1] - xs[1]) ** 2 + (1 - xs[0] ** 2 - xs[1] ** 2 - xs[2] ** 2) + xs[2] ** 2
       + (1 - ys[0] ** 2 - ys[1] ** 2 - ys[2] ** 2) + ys[0] ** 2)
chk('C2', 'SOS: 2 ipW(E0, prodState x y) = (x1+y3)^2 + (y2-x2)^2 + (1-|x|^2) + x3^2 + (1-|y|^2) + y1^2, symbolic '
    '(every summand >= 0 on the closed ball: E0 in maxCone)', sp.expand(2 * val - sos) == 0, 'identity')
ec = E00 + Q(3, 2) * (E(1, 3) - E(2, 2))
chk('C1c', 'countercontrol: the same H1 test rejects e_c = E00 + (3/2)(E13 - E22): '
    'ipW(e_c, prodState(e1, -e3)) = -1/2 < 0 (while E0 gives 0 there)',
    ipW(ec, prodState([1, 0, 0], [0, 0, -1])) == Q(-1, 2)
    and ipW(E0, prodState([1, 0, 0], [0, 0, -1])) == 0, 'countercontrol')

# =====================================================================================================
section('D  H2: cnot preserves Q3, the half-space E0^* and E0')
chk('D1', 'pauliW(cnot w) = CNOT pauliW(w) CNOT for a generic table w, symbolic (so cnot Q3 = Q3)',
    mzero(pauliW(cnot(wsym)) - CNOTU * pauliW(wsym) * CNOTU), 'identity')
chk('D2', 'ipW(cnot w, E0) = ipW(w, E0), symbolic (so cnot maps E0^* onto itself)',
    sp.expand(ipW(cnot(wsym), E0) - ipW(wsym, E0)) == 0, 'identity')
phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
actT_reflY = lambda w: w * sp.diag(1, 1, -1, 1)          # actT reflY: homMap(reflY) on the target index
rphi = pauliW(phiW)
a_eff, b_eff = sp.Matrix([1, -1, 0, 0]), sp.Matrix([1, 0, 0, -1])   # lightlike: sharp effects (up to scale)
chk('D1c', 'countercontrol: the H2 test rejects twin = actT reflY Q3: idW = actT reflY phiW with pauliW(phiW) a '
    'pure state (so idW in twin), cnot idW = chainW, and a^T chainW b = -2 < 0 for sharp effects a, b '
    '(chainW not in maxCone, which contains twin)',
    actT_reflY(phiW) == idW and mzero(rphi * rphi - rphi) and rphi.trace() == 1 and cnot(idW) == chainW
    and (a_eff.T * chainW * b_eff)[0, 0] == -2, 'countercontrol')

# =====================================================================================================
section('F  the witness pair for K1 != Q3')
v = sp.Matrix([1, -1, -1, -1])
Pv = table_of(v * v.T / (v.T * v)[0, 0])
rP = pauliW(Pv)
chk('F1', 'P_v (v = (1,-1,-1,-1)) is a pure state (pauliW(P_v)^2 = pauliW(P_v), trace 1) and ipW(E0, P_v) = -1',
    mzero(rP * rP - rP) and rP.trace() == 1 and ipW(E0, Pv) == -1, 'witness')
chk('F2', 'P_v is not a product table and cnot P_v is not a product table (table ranks > 1): P_v is outside SEP '
    'and cnot SEP', Pv.rank() > 1 and cnot(Pv).rank() > 1, 'witness')
chk('F2c', 'control: the rank test returns 1 on the axis product prodState(e1, e3)',
    prodState([1, 0, 0], [0, 0, 1]).rank() == 1, 'countercontrol')
chk('F3', 'countercontrol: the PSD test rejects E0 (B4) but accepts P_v: <v|pauliW(P_v)|v>/|v|^2 = 1 and '
    'pauliW(P_v) = v v^T/|v|^2', mzero(rP - v * v.T / 4) and (g.T * RE0 * g)[0, 0] < 0, 'countercontrol')

# =====================================================================================================
print()
failed = [c[0] for c in CHECKS if not c[2]]
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('identity', 'enumerate', 'witness', 'countercontrol')), flush=True)
if failed:
    print(f"X1-K1-CORE: FAILED -- {len(failed)} of {len(CHECKS)}: {', '.join(failed)}", flush=True)
    sys.exit(1)
print(f'VERDICT X1-K1-CORE-EXACT -- {len(CHECKS)} checks', flush=True)
