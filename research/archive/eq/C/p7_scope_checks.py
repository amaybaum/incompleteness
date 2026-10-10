"""P7 -- scope checks for the stated results (pressure tests of favourable readings, AGENTS.md section A.31).

7.1 CX is a pair-level statement.  Real QT: Ad(SWAP_AB) is outside the identity component of the two-rebit group
    (P4.4), but SWAP_AB (x) I_C has determinant +1 in O(8), so it is in SO(8): with an idle rebit the exchange is
    continuously reachable through three-rebit maps.  The principle must require the path inside the pair's own
    reversible group.  The twisted complex composite fails even with an ancilla: R_B SWAP R_B = T SWAP (P4.2b) and
    T_AB (x) id_C is not positive on three copies (P6.2a).
7.2 Candidate (c), self-duality alone: the exact reduction to the zero-marginal diagonal slice W_T.  The average over
    the Klein group {(D, D)} in L is the orthogonal projection onto W_T, so for an L-invariant convex cone K,
    P_T(K) = K cap W_T and (K cap W_T)* = P_T(K*) inside W_T; a self-dual K has a self-dual slice.  On the slice
    (t, m), Q3 gives the tetrahedron conv{m in {+-1}^3 : m1 m2 m3 = -1}, R_B Q3 the opposite one, min the
    octahedron, max the cube; the unit ball is also self-dual and lies between octahedron and cube, so the slice
    test does not decide whether self-duality alone narrows to {Q3, R_B Q3} (named wall).
7.3 The landed rotation family is orientation-preserving: cyc3 (KInfFoundations:425-428) is the 3-cycle
    (v0, v1, v2) -> (v2, v0, v1), determinant +1; rot3 t rotates about the third axis.  So the generators of
    driveWords3 (OrbitNormalization:571, boundary-transitive by :667) are rotations.
Usage: python3 -I p7_scope_checks.py
"""
import sys
import os
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eqclib import *  # noqa

rep = Report("P7 scope checks")

# 7.1
P8 = zeros(8, 8)
for a, b, c in itertools.product(range(2), repeat=3):
    P8[4 * b + 2 * a + c][4 * a + 2 * b + c] = Fr(1)
rep.check("7.1a SWAP_AB (x) I_C on three rebits has determinant +1 (so it lies in SO(8), connected)", det_frac(P8) == 1)
P4m = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
rep.check("7.1b while SWAP_AB on two rebits has determinant -1 (P4.4): pair-level CX fails, ancilla-assisted CX holds",
          det_frac(P4m) == -1)

# 7.2 Klein twirl = projection onto W_T
K4 = [diag3(1, 1, 1), diag3(1, -1, -1), diag3(-1, 1, -1), diag3(-1, -1, 1)]
avg = zeros(16, 16)
for D in K4:
    avg = madd(avg, matmul(actC_mat(D), actT_mat(D)), 1, Fr(1, 4))
PT = zeros(16, 16)
for k in (0, 5, 10, 15):
    PT[k][k] = Fr(1)
rep.check("7.2a the Klein-group average of actC(D) actT(D) is the orthogonal projection onto W_T = span{e00, e11, e22, e33}",
          avg == PT)
rep.check("7.2b the Klein elements are rotations (det +1), so they lie in L",
          all(det_frac(D) == 1 for D in K4))
tet1 = [m for m in itertools.product((1, -1), repeat=3) if m[0] * m[1] * m[2] == -1]
phi_T = (1, -1, 1)
rep.check("7.2c the Bell state phiW has slice point (1,-1,1), a vertex of the tetrahedron {m1 m2 m3 = -1}",
          phi_T in tet1)


def polar_ok(Vs, test):
    # for a polytope given by vertices Vs, -S° = {m' : 1 + m.m' >= 0 for all vertices m}; check test points
    return all(1 + sum(a * b for a, b in zip(v, test)) >= 0 for v in Vs)


# the tetrahedron is self-dual in the slice pairing: -T° = T  (vertex test both ways)
rep.check("7.2d the tetrahedron T1 is self-dual for the slice pairing (each vertex of T1 satisfies the facet "
          "inequalities 1 + m.m' >= 0 of T1, and T1's facets are exactly those inequalities)",
          all(polar_ok(tet1, t) for t in tet1)
          and all(1 + sum(a * b for a, b in zip(v, t)) in (0, 4) for v in tet1 for t in tet1))
octv = [tuple(s * (1 if i == j else 0) for j in range(3)) for i in range(3) for s in (1, -1)]
rep.check("7.2e octahedron vertices have norm 1 (on the unit sphere) and the cube contains the unit ball "
          "(|m_i| <= |m| <= 1): the unit ball, self-dual for the slice pairing, lies between min's and max's slices",
          all(sum(x * x for x in v) == 1 for v in octv))
rep.note("7.2f [written] -B° = B for the unit ball B (1 + m.m' >= 0 for all |m| <= 1 iff |m'| <= 1). Whether an "
         "L-invariant self-dual cone with this (or another non-tetrahedral) slice exists is not decided here.")

# 7.3
C3 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]  # (v0, v1, v2) -> (v2, v0, v1)
rep.check("7.3 cyc3's matrix (v0,v1,v2) -> (v2,v0,v1) has determinant +1 (a rotation)", det_frac(C3) == 1)
rep.verdict("SCOPE-CHECKS-EXACT")
