"""EQ2-A probe A4d -- the one-orbit obstruction does not decide the self-duality wall, exact.  Research only; base
bcbc516f.  Usage: python3 -I -B a4d_orbit_extension.py

Context (a4c): F, G = Ad_{S (x) S (x) 1} F lie in B_tw* and tr(F G) = -1/2, so B_tw is not self-dual, and a c = 1
three-copy composite K_3 (local-unitary invariant, K_3 = K_3*, B_tw inside K_3) lies strictly between B_tw and B_tw*.
The simplest way to exclude such a K_3 would be: every x in B_tw* \\ B_tw pairs negatively with some local-unitary image
of itself (then K_3 = B_tw, which is not self-dual).  CLAIM checked here: that argument fails.
  x = F + t 1 with t = 1/10.  x is in B_tw* (F and 1 are); tr(G x) = 3t - 1/2 < 0, so x is not in B_tw.
  Written bound: x = s 1 + B with s = 1/2 + t and B = (1/2)|G+><G+| - (3/2)|G-><G-| (G+- = (|000> +- |111>)/sqrt 2),
  so for EVERY unitary U, tr(x U x U^H) = 8 s^2 + 2 s tr B + tr(B U B U^H) >= 8 s^2 - 2 s - 3/2 = 8t^2 + 6t - 1/2,
  because tr(B U B U^H) >= -(3/4)(tr(P_a U P_b U^H) + tr(P_b U P_a U^H)) >= -3/2 for rank-one projectors P_a, P_b.
  At t = 1/10 the bound is 9/50 > 0.  Hence B_tw + cone(LU . x) is a local-unitary-invariant cone inside its own dual
  that strictly contains B_tw.

DECISION RULE (fixed before the first run): verdict `A4d-ORBIT-OBSTRUCTION-FAILS` iff all pass:
  M1  every conditional <phi|_k PT_j(x)|phi>_k equals the a4c sum of squares plus t(|alpha|^2 + |beta|^2) 1
      (three pairs, symbolic phi), so x is in B_tw*
  M2  tr(G x) = -1/5 < 0 (x is not in B_tw)
  M3  x = s 1 + (1/2)|G+><G+| - (3/2)|G-><G-| exactly, with s = 3/5
  M4  the bound 8t^2 + 6t - 1/2 equals 9/50; it is attained at U = S (x) S (x) 1 (tightness control); 6 random exact
      global unitaries and 6 random exact local unitaries over Q(i) give tr(x U x U^H) >= 9/50 (controls)
  M5  countercontrol: at t = 1/20 the value at U = S (x) S (x) 1 is negative (-9/50), so the bound is not vacuous and
      the orbit argument does exclude x_{1/20}
all pass.  Exact Gaussian-rational and symbolic arithmetic only.
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import I, Matrix, Rational as R, eye, zeros  # noqa: E402

import eq2a_lib as L  # noqa: E402

check = L.check
PAIRS = [(0, 1), (0, 2), (1, 2)]


def zero(M):
    return M.applyfunc(sp.expand).is_zero_matrix


def ket(bits):
    return Matrix([1 if i == int(bits, 2) else 0 for i in range(2 ** len(bits))])


def conditional(Op, pair, phi):
    i, j = pair
    k = [c for c in range(3) if c not in pair][0]
    M = zeros(4, 4)
    for xi, xj, yi, yj in itertools.product(range(2), repeat=4):
        s = 0
        for c in range(2):
            for d in range(2):
                a, b = [0, 0, 0], [0, 0, 0]
                a[i], a[j], a[k] = xi, xj, c
                b[i], b[j], b[k] = yi, yj, d
                s += sp.conjugate(phi[c]) * phi[d] * Op[4 * a[0] + 2 * a[1] + a[2], 4 * b[0] + 2 * b[1] + b[2]]
        M[2 * xi + xj, 2 * yi + yj] = s
    return M.applyfunc(sp.expand)


P6 = eye(8) - ket("000") * ket("000").T - ket("111") * ket("111").T
Xc = ket("000") * ket("111").T + ket("111") * ket("000").T
F = P6 / 2 + Xc
G = P6 / 2 - Xc
t = R(1, 10)
x = F + t * eye(8)
Sg = sp.diag(1, I)
U_ss = L.kron(Sg, Sg, L.S0)

# M1
a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1", real=True)
al, be = a0 + I * a1, b0 + I * b1
n2a, n2b = sp.expand(al * sp.conjugate(al)), sp.expand(be * sp.conjugate(be))
u = Matrix([0, sp.conjugate(al), sp.conjugate(be), 0])
w = Matrix([0, be, al, 0])
D = zeros(4, 4)
D[0, 0], D[3, 3] = n2b / 2, n2a / 2
sosF = (D + (u * u.H + w * w.H) / 2).applyfunc(sp.expand)
okM1 = all(zero(conditional(L.pt(x, p[1], [2, 2, 2]), p, [al, be]) - sosF - t * (n2a + n2b) * eye(4)) for p in PAIRS)
check("M1 every conditional of PT_j(x) = a4c sum of squares + t(|alpha|^2+|beta|^2) 1 (symbolic)  =>  x in B_tw*", okM1)

# M2
v2 = sp.expand((G * x).trace())
print(f"     tr(G x) = {v2}")
check("M2 tr(G x) = -1/5 < 0 with G in B_tw*  =>  x is not in B_tw", v2 == R(-1, 5))

# M3
gp, gm = (ket("000") + ket("111")) / 1, (ket("000") - ket("111")) / 1
s = R(1, 2) + t
check("M3 x = s 1 + (1/2)|G+><G+| - (3/2)|G-><G-| exactly (s = 3/5)",
      s == R(3, 5) and zero(x - (s * eye(8) + R(1, 2) * gp * gp.T / 2 - R(3, 2) * gm * gm.T / 2)))

# M4
bound = 8 * t ** 2 + 6 * t - R(1, 2)
print(f"     bound 8t^2 + 6t - 1/2 = {bound}")
val_ss = sp.expand((x * L.ad(U_ss, x)).trace())
print(f"     tr(x U x U^H) at U = S (x) S (x) 1: {val_ss}")
check("M4 the bound equals 9/50 > 0 and is attained at U = S (x) S (x) 1 (tightness)",
      bound == R(9, 50) and val_ss == R(9, 50))
okg = True
vals = []
for seed in range(101, 107):
    U = L.exact_unitary(8, seed)
    v = sp.expand((x * L.ad(U, x)).trace())
    vals.append(v)
    okg = okg and v.is_Rational is True and v >= R(9, 50)
check("M4 control: 6 random exact global unitaries over Q(i) give tr(x U x U^H) >= 9/50", okg)
okl = True
for seed in range(201, 207):
    U = L.kron(L.exact_unitary(2, seed), L.exact_unitary(2, seed + 50), L.exact_unitary(2, seed + 100))
    v = sp.expand((x * L.ad(U, x)).trace())
    okl = okl and v.is_Rational is True and v >= R(9, 50)
check("M4 control: 6 random exact local unitaries over Q(i) give tr(x U x U^H) >= 9/50", okl)

# M5
t2 = R(1, 20)
x2 = F + t2 * eye(8)
v5 = sp.expand((x2 * L.ad(U_ss, x2)).trace())
print(f"     countercontrol: t = 1/20, tr(x U x U^H) at U = S (x) S (x) 1 = {v5}")
check("M5 countercontrol: at t = 1/20 the value at U = S (x) S (x) 1 is -9/50 < 0", v5 == R(-9, 50))

ok = L.summary("a4d_orbit_extension")
print("VERDICT " + ("A4d-ORBIT-OBSTRUCTION-FAILS" if ok else "A4d-NOT-RENDERED"))
sys.exit(0 if ok else 1)
