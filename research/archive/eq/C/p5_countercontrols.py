"""P5 -- countercontrols for the two-copy theorems and the converse/foil table for candidates (c), (d), (e).

5.1 K_heis: closed convex hull of the exchange-flow orbit of min.  Admissible, convex, closed, satisfies
    continuous exchange (CX) and carries a continuous non-local interaction, but is not Q3: the local-SO(3)^2
    premise of Theorems A and B is load-bearing.  Exact invariant: for a pure state with coefficient matrix Psi,
    S = (Psi + Psi^T)/2, A = (Psi - Psi^T)/2 = c J; on the orbit {cos(2th) a b^T - i sin(2th) b a^T} one has
    |det S| = |c|^2; Psi0 = [[1,2],[3,5]] has |det S| = 5/4 != 1/4 = |c|^2.
5.2 B3 (the Hilbert-Schmidt ball cone): contains products, invariant under SO(15) on the traceless block (so under
    local SO(3)^2 and with SWAP in the identity component), but not inside maxCone: the upper-bound premise is
    load-bearing.
5.3 (c): R_B is Euclidean-orthogonal, so R_B(Q3) is self-dual and homogeneous whenever Q3 is; min != max (so
    neither is Euclidean-self-dual); dim Aut(min) = dim Aut(max) = 13 < 16 (P3), so neither is homogeneous.
5.4 (d): min has no purification of the maximally mixed state; in max, phiW and idW = R_B phiW both purify it, and
    the sign of det(correlation block) separates them under SO(3) x SO(3) (so max fails purification-uniqueness
    with orientation-preserving local reversible maps); the twisted composite inherits purification from Q3.
5.5 (e): SWAP and local O(3)^2 preserve min, max (products to products, product effects to product effects).
Usage: python3 -I p5_countercontrols.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eqclib import *  # noqa
import sympy as sp

rep = Report("P5 countercontrols and candidate foils")

# ------------------------------------------------------------------ 5.1 K_heis
M1 = [ad_herm(SIG2[(i, j)]) for i in (1, 2, 3) for j in (1, 2, 3)]
Hh = cadd(cadd(SIG2[(1, 1)], SIG2[(2, 2)]), SIG2[(3, 3)])
Xh = ad_herm(Hh)
rep.check("5.1a the exchange-flow generator ad(sum_i s_i (x) s_i) lies in M1",
          span_rank([flat(m) for m in M1] + [flat(Xh)]) == 9)
a1, a2, b1, b2, al, be = sp.symbols("a1 a2 b1 b2 alpha beta")
Psi = al * sp.Matrix([a1, a2]) * sp.Matrix([[b1, b2]]) + be * sp.Matrix([b1, b2]) * sp.Matrix([[a1, a2]])
S = (Psi + Psi.T) / 2
A = (Psi - Psi.T) / 2
cc = A[0, 1]
wedge = a1 * b2 - a2 * b1
rep.check("5.1b symbolic identities: det S = -((alpha+beta)/2)^2 (a1 b2 - a2 b1)^2 and "
          "A = c [[0,1],[-1,0]] with c = ((alpha-beta)/2)(a1 b2 - a2 b1)",
          sp.expand(S.det() + ((al + be) / 2) ** 2 * wedge ** 2) == 0
          and sp.expand(cc - (al - be) / 2 * wedge) == 0 and sp.expand(A[0, 0]) == 0 and sp.expand(A[1, 0] + cc) == 0)
cs, sn = sp.symbols("c s", real=True)
# alpha = c (real), beta = -i s (purely imaginary), c^2 + s^2 = 1:  |alpha + beta|^2 = |alpha - beta|^2 = c^2 + s^2
abs2 = lambda z: sp.expand(z * sp.conjugate(z))  # noqa
rep.check("5.1c on the exchange orbit (alpha = cos 2th, beta = -i sin 2th): |alpha+beta|^2 = |alpha-beta|^2 = 1, "
          "hence |det S| = |c|^2 for every orbit point",
          sp.simplify(abs2(cs - sp.I * sn) - (cs ** 2 + sn ** 2)) == 0
          and sp.simplify(abs2(cs + sp.I * sn) - (cs ** 2 + sn ** 2)) == 0)
P0 = [[Fr(1), Fr(2)], [Fr(3), Fr(5)]]
S0 = [[P0[0][0], (P0[0][1] + P0[1][0]) / 2], [(P0[0][1] + P0[1][0]) / 2, P0[1][1]]]
c0 = (P0[0][1] - P0[1][0]) / 2
detS0 = S0[0][0] * S0[1][1] - S0[0][1] * S0[1][0]
rep.check("5.1d Psi0 = [[1,2],[3,5]]: |det S| = 5/4 and |c|^2 = 1/4, so P_Psi0 (a pure state of Q3) is not on the "
          "exchange orbit of any pure product (the invariant is scale- and phase-free)",
          abs(detS0) == Fr(5, 4) and c0 * c0 == Fr(1, 4))
rep.note("5.1e [written] K_heis := conv{ Ad(exp(-i th H)) P_{a(x)b} } (a compact orbit, so the hull is closed). It "
         "contains min, lies in Q3 (unitary images of products) hence in maxCone, is convex and closed, and the "
         "path th in [0, pi/4] puts SWAP in Aut_u(K_heis)_0 (P4.3). A rank-one element of K_heis is extreme in the PSD "
         "cone, so it equals an orbit point; P_Psi0 is not (5.1d), so K_heis != Q3. Hence the local SO(3)^2 premise "
         "of Theorems A and B is load-bearing (with it, both would force K_heis = Q3).")

# ------------------------------------------------------------------ 5.2 B3
def b3_norm(w):
    return sum(w[m][n] ** 2 for (m, n) in IDX if (m, n) != (0, 0))


ok = all(b3_norm(prodState(unit_vector(s, t), unit_vector(u, v))) == 3
         for (s, t, u, v) in [(0, 0, 1, 2), (Fr(1, 3), 2, -1, Fr(1, 2)), (5, -2, Fr(2, 7), 3)])
rep.check("5.2a pure products lie on the boundary of B3 = {sum_{(mu,nu)!=(0,0)} w^2 <= 3 w00^2}", ok)
perm15 = [[SWAP16[r][c] for c in range(1, 16)] for r in range(1, 16)]
rep.check("5.2b SWAP fixes the unit coordinate and acts on the 15 others by a permutation of determinant +1, so "
          "SWAP is in SO(15), a connected group of normalization-preserving symmetries of B3",
          SWAP16[0][0] == 1 and det_frac(perm15) == 1)
z = [0, 0, 1]
pz = prodState(z, z)
w2 = [[(2 if (m, n) == (0, 0) else 0) - pz[m][n] for n in range(4)] for m in range(4)]
rep.check("5.2c 2 e00 - prodState z z lies in B3 (norm^2 3, w00 = 1) and the product effect (1,z)(x)(1,z) takes "
          "the value -2 on it, so B3 is not inside maxCone",
          b3_norm(w2) == 3 and w2[0][0] == 1 and pairVal(hom(z), hom(z), w2) == -2)

# ------------------------------------------------------------------ 5.3 (c)
RB = actT_mat(REFLY)
rep.check("5.3a R_B is orthogonal for the Euclidean pairing of W 3 (R_B^T R_B = I), so (R_B Q3)* = R_B (Q3*)",
          matmul(transpose(RB), RB) == eye(16))
phiW = [[Fr(v) for v in r] for r in [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]]
fsep = lambda w: w[0][0] - w[1][1] + w[2][2] - w[3][3]  # noqa
xs_ = sp.symbols("x1 x2 x3", real=True)
ys_ = sp.symbols("y1 y2 y3", real=True)
fprod = 1 - xs_[0] * ys_[0] + xs_[1] * ys_[1] - xs_[2] * ys_[2]
rep.check("5.3b min != max: f = w00 - w11 + w22 - w33 equals 1 - x1 y1 + x2 y2 - x3 y3 >= 0 on products "
          "(|x.Dy| <= 1, D = diag(1,-1,1)), while f(phiW) = -2 and phiW is in Q3 (P1.7a), hence in maxCone",
          sp.expand(fsep([[(1 if m == 0 else xs_[m - 1]) * (1 if n == 0 else ys_[n - 1]) for n in range(4)]
                          for m in range(4)]) - fprod) == 0 and fsep(phiW) == -2)
rep.note("5.3c [written] so min* = max != min: neither is Euclidean-self-dual; with P3 (dim Aut = 13 < 16) neither is "
         "homogeneous. For self-duality w.r.t. ANY inner product, min would be linearly isomorphic to max; their "
         "extreme rays have dimensions 4 (pure products) and 6 (all pure states and their partial transposes: "
         "Stormer-Woronowicz decomposability + SLOCC images of the exposed Bell ray; literature + written), so no.")

# ------------------------------------------------------------------ 5.4 (d) purification
idW = apply(RB, phiW)
rep.check("5.4a phiW and idW = R_B phiW both have A-marginal 0 (w_{mu 0} = 0 for mu >= 1) and B-marginal 0",
          all(phiW[m][0] == 0 and idW[m][0] == 0 and phiW[0][m] == 0 and idW[0][m] == 0 for m in (1, 2, 3)))
corr = lambda w: [[w[i][j] for j in (1, 2, 3)] for i in (1, 2, 3)]  # noqa
rep.check("5.4b det of the correlation block: -1 for phiW, +1 for idW; actT R, actC R (R in SO(3)) map M to "
          "R_A M R_B^T and preserve det, so no orientation-preserving local map relates the two purifications",
          det_frac(corr(phiW)) == -1 and det_frac(corr(idW)) == 1)
Fsep = [[Fr(0)] * 4 for _ in range(4)]
for (aa, bb) in [((1, 0, 0), (-1, 0, 0)), ((-1, 0, 0), (1, 0, 0)), ((0, 1, 0), (0, 1, 0)), ((0, -1, 0), (0, -1, 0)),
                 ((0, 0, 1), (0, 0, -1)), ((0, 0, -1), (0, 0, 1))]:
    ps = prodState(list(aa), list(bb))
    Fsep = [[Fsep[m][n] + ps[m][n] / 2 for n in range(4)] for m in range(4)]
rep.check("5.4d the exposing functional F = (3 w00 - w11 + w22 - w33)/4 has coefficient array (1/2) x (sum of six pure "
          "products), so F is separable (lies in min = max*), and F(phiW) = 0",
          Fsep == [[Fr(3), 0, 0, 0], [0, Fr(-1), 0, 0], [0, 0, Fr(1), 0], [0, 0, 0, Fr(-1)]]
          and (3 * phiW[0][0] - phiW[1][1] + phiW[2][2] - phiW[3][3]) == 0)
rep.note("5.4c [written] in max both are extreme (phiW is an exposed ray: F = I - P_phi is separable and exposes it; "
         "idW is its image under the automorphism R_B), so the maximally mixed state of A has two purifications "
         "in max not related by SO(3)_B: max fails purification-uniqueness under orientation-preserving local "
         "reversibility (with O(3) local maps, R_B relates them; but Q3 is not O(3)-invariant, P1.7). min: its "
         "pure states are pure products with pure marginals, so a mixed state of A has no purification. The twisted "
         "composite inherits purification from Q3 through the one-copy relabelling R_B.")

# ------------------------------------------------------------------ 5.5 (e)
ok = True
for (s, t, u, v) in [(0, 0, 1, 2), (Fr(1, 3), 2, -1, Fr(1, 2))]:
    x, y = unit_vector(s, t), unit_vector(u, v)
    ok &= apply(SWAP16, prodState(x, y)) == prodState(y, x)
    a = hom(unit_vector(2, 1))
    bb = hom(unit_vector(-1, 3))
    w = [[Fr((3 * m + 5 * n) % 7 - 3) for n in range(4)] for m in range(4)]
    ok &= pairVal(a, bb, apply(SWAP16, w)) == pairVal(bb, a, w)
rep.check("5.5 SWAP maps products to products and product effects to product effects (pairVal a b (SWAP w) = "
          "pairVal b a w), so min and max are SWAP-invariant; with local O(3)^2 invariance of both, candidate (e) "
          "admits min, max, Q3 and R_B(Q3)", ok)
rep.verdict("COUNTERCONTROLS-EXACT: K_heis (local premise), B3 (upper bound), min/max/twisted for (c), (d), (e) as stated")
