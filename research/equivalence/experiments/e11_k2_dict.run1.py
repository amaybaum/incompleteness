"""E11 probe -- the exact content of the formal statements of the design module EqvK2Schema (skeleton S6).

Written 2026-10-11T00:35Z (date -u read at 00:33:35Z before writing; committed 00:35:41Z in 97b6f080), before the
first run and before the module's design run.

PURPOSE.  The module lean/EqvK2Schema.lean states, in Lean, the two-token dictionary of DIM-1's pair carrier W 3 and
the cone step of the K2 schema.  A statement that is false as formalized (a wrong orientation, a missing factor, a wrong
index convention) would fail in the kernel for a reason no proof repair can fix.  This probe checks, in exact
(Gaussian-)rational arithmetic, that each formal statement holds on its instances, with the module's own conventions:

  pauli = [1, X, Y, Z] with Y = [[0, -i], [i, 0]];  tensorOf A B (a1, a2) (b1, b2) = A a1 b1 * B a2 b2 (the kernel's
  MonoidalCompletion.tensorOf, control factor first); tokMat v = sum_mu (v_mu / 2) pauli_mu;
  dict w = sum_{mu,nu} (w_mu_nu / 4) tensorOf pauli_mu pauli_nu;  ipW w e = sum w_mu_nu e_mu_nu;
  coordOf H mu nu = re tr (tensorOf pauli_mu pauli_nu * H);  tens X Y mu nu = X_mu Y_nu, prodState x y = tens (hom x)
  (hom y), hom x = (1, x0, x1, x2);  the kernel's cnot PARSED from CompositeDimension.lean (pc, pt, sgn tables).

CHECKS (each names the module declaration whose statement it instantiates).
  C1  pauli_conjTranspose: each pauli_mu is Hermitian.
  C2  trace_pauli_mul: tr (pauli_mu pauli_nu) = 2 if mu = nu else 0, all 16 pairs.
  C3  pauli_complete: sum_mu (pauli_mu)_ab (pauli_mu)_cd = 2 if (a = d and b = c) else 0, all 16 quadruples.
  C4  tensorOf_mul, trace_tensorOf, tensorOf_conjTranspose on three Gaussian-rational quadruples (A, B, C, D).
  C5  trace_T_mul_T: tr (T_mn T_m'n') = (2 d_mm')(2 d_nn'), all 256.
  C6  dict_tens on three rational (X, Y); dict_prodState on two rational ball points.
  C7  dict_add, dict_smul on rational tables.
  C8  dict_conjTranspose (Hermiticity) on three rational tables.
  C9  trace_T_mul_dict: tr (T_mn dict e) = e_mn, all 16, on two tables.
  C10 trace_dict_mul and ipW_eq_trace: tr (dict w dict e) = ipW w e / 4, on three pairs.
  C11 coordOf_dict on three tables.
  C12 sum_T_entry: the regrouped entry identity, on two Gaussian-rational H and all 16 entries.
  C13 dict_complete4: sum_{mn} tr (T_mn H) T_mn = 4 H, on two non-Hermitian Gaussian-rational H.
  C14 trace_T_mul_real and dict_coordOf: for two Hermitian Gaussian-rational H the coordinates are real and
      dict (coordOf H) = H.
  C15 trace_vecMulVec_mul: tr (x x^H M) = x^H M x, on two (x, M).
  C16 LOWER's factorization step: B B^H = sum_k vecMulVec (B[:, k]) (star B[:, k]), on two Gaussian-rational B.
  C17 the positive control Q3 = dualW Q3 on instances: for PSD rho1 = B1 B1^H and rho2 = B2 B2^H the pairing
      ipW (coordOf rho1) (coordOf rho2) = 4 tr (rho1 rho2) is nonnegative.
  C18 an instance of ReachPure in the module's conventions: with the kernel's cnot (parsed),
      dict (2 * cnot (prodState xplus z3)) = vecMulVec x (star x) for x = (1, 0, 0, 1) on the index order
      (0,0), (0,1), (1,0), (1,1) -- the Bell state reached from a product by one generator, scale 2.
COUNTERCONTROLS (each must fail as stated).
  X1  pauli_complete with the orientation (a = c and b = d) is false for some quadruple.
  X2  the dictionary without its factor 1/4 does not satisfy tr (dict' w dict' e) = ipW w e / 4.

DECISION RULE (fixed before the first run).  VERDICT E11-DICT-STATEMENTS-EXACT iff C1 ... C18 all pass and X1 and X2
both fail as stated; otherwise "VERDICT NOT RENDERED" with the failing items.  The verdict says only that the module's
formal statements are exactly true on these instances with these conventions; it is not a kernel proof, and C18 is one
instance of ReachPure, not ReachPure.
"""
import itertools
import re
import sys

import sympy as sp

KERNEL = '../../../verification/lean-mathlib/OIBridge/CompositeDimension.lean'
RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''), flush=True)


def parse_table(src, name):
    m = re.search(r'def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n)+)' % name, src)
    entries = re.findall(r'(\d), (\d) => (\d)', m.group(1))
    T = {(int(a), int(b)): int(c) for a, b, c in entries}
    assert len(T) == 16
    return T


def parse_sgn(src):
    m = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1',
                  src)
    neg = {(int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))}
    return {(a, b): (-1 if (a, b) in neg else 1) for a in range(4) for b in range(4)}


src = open(KERNEL, encoding='utf-8').read()
PC, PT, SGN = parse_table(src, 'pc'), parse_table(src, 'pt'), parse_sgn(src)
print('parsed: pc, pt, sgn (16 entries each)', flush=True)

I = sp.I
PAULI = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
PAIRS = [(0, 0), (0, 1), (1, 0), (1, 1)]          # index order of Fin 2 x Fin 2
IDX = {p: k for k, p in enumerate(PAIRS)}


def Z(M):
    return M.applyfunc(sp.expand) == sp.zeros(*M.shape)


def tensorOf(A, B):
    return sp.Matrix(4, 4, lambda r, c: A[PAIRS[r][0], PAIRS[c][0]] * B[PAIRS[r][1], PAIRS[c][1]])


T = {(m, n): tensorOf(PAULI[m], PAULI[n]) for m in range(4) for n in range(4)}


def tokMat(v):
    return sum((sp.Rational(1, 2) * v[m] * PAULI[m] for m in range(4)), sp.zeros(2, 2))


def dict_(w, factor=sp.Rational(1, 4)):
    return sum((factor * w[m][n] * T[(m, n)] for m in range(4) for n in range(4)), sp.zeros(4, 4))


def ipW(w, e):
    return sum(w[m][n] * e[m][n] for m in range(4) for n in range(4))


def coordOf(H):
    return [[sp.re(sp.expand((T[(m, n)] * H).trace())) for n in range(4)] for m in range(4)]


def tens(X, Y):
    return [[X[m] * Y[n] for n in range(4)] for m in range(4)]


def hom(x):
    return [1] + list(x)


def cnot(w):
    return [[SGN[(m, n)] * w[PC[(m, n)]][PT[(m, n)]] for n in range(4)] for m in range(4)]


def R(a, b):
    return sp.Rational(a, b)


def table(seed):
    vals = [R((7 * seed + 3 * k) % 11 - 5, (k % 5) + 2) for k in range(16)]
    return [vals[4 * m:4 * m + 4] for m in range(4)]


def gauss_matrix(n, seed):
    return sp.Matrix(n, n, lambda r, c: R(((seed + 3 * r + 5 * c) % 7) - 3, 2) + I * R(((seed * 2 + r + 2 * c) % 5) - 2, 3))


# C1
check('C1 pauli_conjTranspose', all(Z(PAULI[m].H - PAULI[m]) for m in range(4)))
# C2
check('C2 trace_pauli_mul', all(sp.expand((PAULI[m] * PAULI[n]).trace()) == (2 if m == n else 0)
                                for m in range(4) for n in range(4)))
# C3
c3 = all(sp.expand(sum(PAULI[m][a, b] * PAULI[m][c, d] for m in range(4))) == (2 if (a == d and b == c) else 0)
         for a, b, c, d in itertools.product(range(2), repeat=4))
check('C3 pauli_complete (a = d and b = c)', c3)
# C4
ok4 = True
for s in range(3):
    A, B, C, D = (gauss_matrix(2, 4 * s + k) for k in range(4))
    ok4 &= Z(tensorOf(A, B) * tensorOf(C, D) - tensorOf(A * C, B * D))
    ok4 &= sp.expand(tensorOf(A, B).trace() - A.trace() * B.trace()) == 0
    ok4 &= Z(tensorOf(A, B).H - tensorOf(A.H, B.H))
check('C4 tensorOf_mul, trace_tensorOf, tensorOf_conjTranspose', ok4)
# C5
ok5 = all(sp.expand((T[(m, n)] * T[(mm, nn)]).trace()) == (2 if m == mm else 0) * (2 if n == nn else 0)
          for m, n, mm, nn in itertools.product(range(4), repeat=4))
check('C5 trace_T_mul_T (256)', ok5)
# C6
ok6 = True
for s in range(3):
    X = [R(s + k, 3) - 1 for k in range(4)]
    Y = [R(2 * s - k, 5) for k in range(4)]
    ok6 &= Z(dict_(tens(X, Y)) - tensorOf(tokMat(X), tokMat(Y)))
for x, y in [((R(1, 2), R(-1, 3), R(1, 4)), (R(0), R(3, 5), R(-4, 5))), ((R(1), 0, 0), (0, 0, R(1)))]:
    ok6 &= Z(dict_(tens(hom(x), hom(y))) - tensorOf(tokMat(hom(x)), tokMat(hom(y))))
check('C6 dict_tens, dict_prodState', ok6)
# C7
w, e = table(1), table(2)
c = R(-7, 3)
ok7 = Z(dict_([[w[m][n] + e[m][n] for n in range(4)] for m in range(4)]) - dict_(w) - dict_(e))
ok7 &= Z(dict_([[c * w[m][n] for n in range(4)] for m in range(4)]) - c * dict_(w))
check('C7 dict_add, dict_smul', ok7)
# C8
check('C8 dict_conjTranspose', all(Z(dict_(table(s)).H - dict_(table(s))) for s in range(3)))
# C9
ok9 = all(sp.expand((T[(m, n)] * dict_(table(s))).trace()) == table(s)[m][n]
          for s in (3, 4) for m in range(4) for n in range(4))
check('C9 trace_T_mul_dict', ok9)
# C10
ok10 = all(sp.expand((dict_(table(s)) * dict_(table(s + 5))).trace() - ipW(table(s), table(s + 5)) / 4) == 0
           for s in range(3))
check('C10 trace_dict_mul, ipW_eq_trace', ok10)
# C11
check('C11 coordOf_dict', all(coordOf(dict_(table(s))) == table(s) for s in range(3)))
# C12
ok12 = True
for s in (1, 2):
    H = gauss_matrix(4, s)
    for (a1, a2), (b1, b2) in itertools.product(PAIRS, repeat=2):
        lhs = sum((T[(m, n)] * H).trace() * T[(m, n)][IDX[(a1, a2)], IDX[(b1, b2)]]
                  for m in range(4) for n in range(4))
        rhs = sum(H[IDX[(q1, q2)], IDX[(p1, p2)]]
                  * sum(PAULI[m][p1, q1] * PAULI[m][a1, b1] for m in range(4))
                  * sum(PAULI[n][p2, q2] * PAULI[n][a2, b2] for n in range(4))
                  for p1, p2, q1, q2 in itertools.product(range(2), repeat=4))
        ok12 &= sp.expand(lhs - rhs) == 0
check('C12 sum_T_entry (2 x 16 entries)', ok12)
# C13
ok13 = True
for s in (3, 4):
    H = gauss_matrix(4, s)
    ok13 &= not Z(H - H.H)
    ok13 &= Z(sum(((T[(m, n)] * H).trace() * T[(m, n)] for m in range(4) for n in range(4)), sp.zeros(4, 4)) - 4 * H)
check('C13 dict_complete4 (non-Hermitian H)', ok13)
# C14
ok14 = True
for s in (5, 6):
    G = gauss_matrix(4, s)
    H = (G + G.H) / 2
    ok14 &= all(sp.im(sp.expand((T[(m, n)] * H).trace())) == 0 for m in range(4) for n in range(4))
    ok14 &= Z(dict_(coordOf(H)) - H)
check('C14 trace_T_mul_real, dict_coordOf', ok14)
# C15
ok15 = True
for s in (1, 2):
    x = sp.Matrix(4, 1, lambda r, _: R(r - s, 3) + I * R(s + r, 2))
    M = gauss_matrix(4, s + 7)
    ok15 &= sp.expand((x * x.H * M).trace() - (x.H * M * x)[0, 0]) == 0
check('C15 trace_vecMulVec_mul', ok15)
# C16
ok16 = True
for s in (1, 2):
    B = gauss_matrix(4, s + 11)
    ok16 &= Z(B * B.H - sum((B[:, k] * B[:, k].H for k in range(4)), sp.zeros(4, 4)))
check('C16 B B^H = sum of rank-one terms', ok16)
# C17
ok17 = True
for s in (1, 2):
    B1, B2 = gauss_matrix(4, s + 13), gauss_matrix(4, s + 17)
    r1, r2 = B1 * B1.H, B2 * B2.H
    p = ipW(coordOf(r1), coordOf(r2))
    ok17 &= sp.expand(p - 4 * (r1 * r2).trace()) == 0 and sp.expand(p) >= 0
check('C17 Q3 pairing nonnegative on PSD instances', ok17)
# C18
xplus, z3 = (1, 0, 0), (0, 0, 1)
phiw = cnot(tens(hom(xplus), hom(z3)))
xv = sp.Matrix([1, 0, 0, 1])
ok18 = Z(dict_([[2 * phiw[m][n] for n in range(4)] for m in range(4)]) - xv * xv.H)
check('C18 ReachPure instance: dict (2 cnot (prodState xplus z3)) = x x^H, x = (1,0,0,1)', ok18,
      'cnot(prodState xplus z3) = %s' % phiw)
# X1
x1 = all(sp.expand(sum(PAULI[m][a, b] * PAULI[m][c, d] for m in range(4))) == (2 if (a == c and b == d) else 0)
         for a, b, c, d in itertools.product(range(2), repeat=4))
print('COUNTER X1 ' + ('fails as stated' if not x1 else 'DID NOT FAIL'), flush=True)
# X2
x2 = all(sp.expand((dict_(table(s), 1) * dict_(table(s + 5), 1)).trace() - ipW(table(s), table(s + 5)) / 4) == 0
         for s in range(3))
print('COUNTER X2 ' + ('fails as stated' if not x2 else 'DID NOT FAIL'), flush=True)

failures = [n for n, ok in RESULTS if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len(failures)), flush=True)
if not failures and not x1 and not x2:
    print('VERDICT E11-DICT-STATEMENTS-EXACT', flush=True)
else:
    print('VERDICT NOT RENDERED -- failing: %s; X1 failed: %s; X2 failed: %s' % (failures, not x1, not x2), flush=True)
sys.exit(0)
