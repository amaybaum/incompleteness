"""EQ2-A probe A2b -- the chart steps of the conditional all-copy theorem, exact.  Research only; base bcbc516f.
Usage: python3 -I -B a2b_chart_steps.py

DECISION RULE (fixed before the first run): verdict `A2b-CHART-STEPS-EXACT` iff every check passes:
  S3a  T . Ad_U . T = Ad_conj(U) on 2-qubit matrices (T the full transpose) for an exact unitary U over Q(i)
  S3b  PT_A . Ad_U . PT_A = PT_B . Ad_conj(U) . PT_B  (so R_A PU(4) R_A = R_B PU(4) R_B)
  S3c  countercontrol: PT_B . Ad_U . PT_B is NOT a unitary conjugation for U = CNOT (its action on the matrix units
       is not multiplicative: it fails Phi(E_ij E_jk) = Phi(E_ij) Phi(E_jk) for some units)
  S3d  tau-twisted 2-colouring: for every labelled tree on n = 2..6 vertices and every tau on its edges there is
       eps with eps_i XOR eps_j = tau_ij (exhaustive over Pruefer trees and all tau); countercontrol: on the triangle
       with odd tau no eps exists
  S0a  conditioning commutes with idle extension: for g on copies (0,1) and any effect f on copy 2,
       cond_f((g (x) id) w) = g(cond_f w)   (symbolic 3-copy table, symbolic g)
  S0b  conditioning commutes with per-token charts up to transporting the effect: cond_f(chi_eps w) =
       (eps_0 (x) eps_1)(cond_{f . eps_2} w)  (symbolic, eps from exact orthogonal matrices)
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import I, Matrix, Rational as R, eye, zeros  # noqa: E402

import eq2a_lib as L  # noqa: E402

check = L.check


def zero(M):
    return M.applyfunc(sp.expand).is_zero_matrix


U = L.exact_unitary(4, seed=31)
check("S3 U is an exact unitary over Q(i)", L.is_unitary(U))
Xs = Matrix(4, 4, lambda i, j: sp.Symbol(f"x{i}_{j}"))
Uc = U.applyfunc(sp.conjugate)
check("S3a T . Ad_U . T = Ad_conj(U) (symbolic input)", zero(L.ad(U, Xs.T).T - L.ad(Uc, Xs)))
lhs = L.pt(L.ad(U, L.pt(Xs, 0, [2, 2])), 0, [2, 2])
rhs = L.pt(L.ad(Uc, L.pt(Xs, 1, [2, 2])), 1, [2, 2])
check("S3b PT_A . Ad_U . PT_A = PT_B . Ad_conj(U) . PT_B (symbolic input)", zero(lhs - rhs))
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
phi = lambda X: L.pt(L.ad(CNOT, L.pt(X, 1, [2, 2])), 1, [2, 2])  # noqa: E731


def E(i, j):
    M = zeros(4, 4)
    M[i, j] = 1
    return M


bad = any(not zero(phi(E(i, j) * E(j, k)) - phi(E(i, j)) * phi(E(j, k)))
          for i in range(4) for j in range(4) for k in range(4))
check("S3c countercontrol: PT_B . Ad_CNOT . PT_B is not multiplicative on matrix units (so not Ad of any unitary)", bad)


def pruefer_trees(n):
    if n == 2:
        yield [(0, 1)]
        return
    for seq in itertools.product(range(n), repeat=n - 2):
        deg = [1] * n
        for v in seq:
            deg[v] += 1
        es = []
        for v in seq:
            leaf = min(i for i in range(n) if deg[i] == 1)
            es.append((leaf, v))
            deg[leaf] -= 1
            deg[v] -= 1
        u, w = [i for i in range(n) if deg[i] == 1]
        es.append((u, w))
        yield es


ok = True
count = 0
for n in range(2, 7):
    for es in pruefer_trees(n):
        for tau in itertools.product((0, 1), repeat=len(es)):
            found = any(all((eps[a] ^ eps[b]) == t for (a, b), t in zip(es, tau))
                        for eps in itertools.product((0, 1), repeat=n))
            ok = ok and found
            count += 1
check(f"S3d every tau on every labelled tree (n = 2..6; {count} (tree, tau) cases) admits eps with eps_i^eps_j = tau_ij", ok)
tri = [(0, 1), (1, 2), (0, 2)]
check("S3d countercontrol: on the triangle with tau = (0,0,1) no eps exists",
      not any(all((eps[a] ^ eps[b]) == t for (a, b), t in zip(tri, (0, 0, 1))) for eps in itertools.product((0, 1), repeat=3)))

Om = {idx: sp.Symbol("o%d%d%d" % idx, real=True) for idx in itertools.product(range(4), repeat=3)}
Gs = Matrix(16, 16, lambda i, j: sp.Symbol(f"g{i}_{j}", real=True))
gmap = lambda w: Matrix(4, 4, lambda m, n: sum(Gs[4 * m + n, 4 * p + q] * w[p, q]  # noqa: E731
                                               for p in range(4) for q in range(4)))
f = sp.symbols("f0:4", real=True)


def cond2(T, fv):
    return Matrix(4, 4, lambda m, n: sp.expand(sum(T[(m, n, c)] * fv[c] for c in range(4))))


ext = L.idle_ext(gmap, Om, (0, 1))
check("S0a cond_f((g (x) id) w) = g(cond_f w) (symbolic g, w, f)", zero(cond2(ext, f) - gmap(cond2(Om, f))))
skews = [Matrix([[0, R(1, 2), R(-1, 3)], [R(-1, 2), 0, R(2, 5)], [R(1, 3), R(-2, 5), 0]]),
         Matrix([[0, 3, 1], [-3, 0, R(-7, 4)], [-1, R(7, 4), 0]])]
eps = [L.hom_map(L.cayley(skews[0])), L.hom_map(L.cayley(skews[1]) * L.REFLY), L.hom_map(L.REFLY)]
chi = {}
for (a, b, c) in itertools.product(range(4), repeat=3):
    chi[(a, b, c)] = sp.expand(sum(eps[0][a, p] * eps[1][b, q] * eps[2][c, r] * Om[(p, q, r)]
                                   for p in range(4) for q in range(4) for r in range(4)))
lhs = cond2(chi, f)
f_tr = [sp.expand(sum(f[c] * eps[2][c, r] for c in range(4))) for r in range(4)]
rhs = eps[0] * cond2(Om, f_tr) * eps[1].T
check("S0b cond_f(chi_eps w) = (eps_0 (x) eps_1)(cond_{f . eps_2} w) (symbolic)", zero(lhs - rhs))

ok = L.summary("a2b_chart_steps")
print("VERDICT " + ("A2b-CHART-STEPS-EXACT" if ok else "A2b-NOT-RENDERED"))
sys.exit(0 if ok else 1)
