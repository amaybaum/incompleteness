"""s3 -- QE1 nodes N1.4 (K-inf-Drive), N1.5 (K-inf-Trans), N1.8 (K-inf-Geom): which hold beyond the qubit.

Decision rule (fixed before running): a K-inf premise is ELEMENTARY-SCOPED in QM iff it holds for the qubit (kernel
witness or exact check) and fails for the qutrit with an exact witness; it is NOT elementary-scoped iff the qutrit
satisfies it exactly.  Controls: the qubit facts must hold; for K-inf-Trans the failure must be read through the landed
kernel theorem `not_boundaryTransitive_of_nonextreme_boundary` (TransitiveBody:301), whose hypotheses are listed.
"""
import sys
from sympy import Matrix, Rational as R, I, eye, zeros, sqrt, simplify, symbols, cos, sin, pi, expand, trigsimp
from common import *

rep = Report("s3_scope_qutrit")
E = lambda i, j: Matrix(3, 3, lambda a, b: 1 if (a, b) == (i, j) else 0)
k = [Matrix([1 if i == j else 0 for i in range(3)]) for j in range(3)]
proj = lambda v: (v * dag(v)).applyfunc(simplify)
eps, s, t, lam = symbols('epsilon s t lam', real=True)

# ---------------- K-inf-Trans at the qutrit: a non-extreme boundary state
x = (E(0, 0) + E(1, 1)) / 2
y = E(2, 2)
ext = x + eps * (x - y)
rep.check("x = diag(1/2,1/2,0) and y = |2><2| are states", x.trace() == 1 and y.trace() == 1)
rep.check("IsBoundaryState (KF:130): x + eps (x - y) = diag((1+eps)/2,(1+eps)/2,-eps) has the eigenvalue -eps < 0 for "
          "every eps > 0, so it leaves the body", ext == Matrix.diag((1 + eps) / 2, (1 + eps) / 2, -eps))
rep.check("x is NOT extreme: x = (|0><0| + |1><1|)/2 with |0><0| != |1><1| both states", E(0, 0) != E(1, 1))
rep.note("TransitiveBody:301 `not_boundaryTransitive_of_nonextreme_boundary` (compact, convex, interior nonempty in the "
         "8-dimensional chart of traceless Hermitian coordinates, a boundary state that is not extreme) then gives: NO "
         "body-preserving family G is boundary transitive on the qutrit body -- K-inf-Trans fails for every G.")
# dense form too: the extreme points (pure states) form a closed set, and the dense-orbit form's ball theorem
# (DenseOrbit `eq_qBall_of_dense`) would make the qutrit body an ellipsoid; the non-extreme boundary point above rules
# that out as well (an ellipsoid has every boundary point extreme).
rep.note("the dense form fails as well: DenseOrbit:125 `eq_qBall_of_dense` would make the body a Q-ball, all of whose "
         "boundary points are extreme, contradicting the witness above.")

# ---------------- K-inf-Geom at the qutrit (recorded in the corpus; re-verified as a control)
P = E(0, 0) + E(1, 1)
rep.check("SingletonFaces fails at the qutrit: P = diag(1,1,0) is proper (0 on |2><2|) and certain on |0><0| and |1><1|",
          (P * E(2, 2)).trace() == 0 and (P * E(0, 0)).trace() == 1 and (P * E(1, 1)).trace() == 1)

# ---------------- K-inf-Drive at the qutrit: an ElementaryDrivability (KF:264) exists
H = E(0, 1) + E(1, 0)
P01 = E(0, 0) + E(1, 1)
U = lambda tt: E(2, 2) + cos(tt) * P01 - I * sin(tt) * H        # = exp(-i tt H), since H^2 = P01, H^3 = H
rep.check("U(t) = exp(-itH) closed form: dU/dt = -i H U and U(0) = I (symbolic)",
          (U(t).diff(t) + I * H * U(t)).applyfunc(simplify) == zeros(3, 3) and U(0) == eye(3))
rep.check("flow_add: U(s) U(t) = U(s+t) (symbolic trig identity)",
          (U(s) * U(t) - U(s + t)).applyfunc(lambda e: simplify(trigsimp(expand(e, trig=True)))) == zeros(3, 3))
rep.check("flow_preserves: U(t) unitary, so Ad_U(t) preserves the body", (U(t) * dag(U(t))).applyfunc(simplify) == eye(3))
Npi = U(pi)
rep.check("t0 = pi: U(pi) = diag(-1,-1,1), U(pi)^2 = I, so the member at t0 is an involution of the body",
          Npi == Matrix.diag(-1, -1, 1) and Npi * Npi == eye(3))
r02 = proj((k[0] + k[2]) / sqrt(2))
rep.check("N_moves: Ad_U(pi) moves (|0>+|2>)/sqrt2 to (-|0>+|2>)/sqrt2", (Npi * r02 * dag(Npi)) != r02)
Jm = Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])                   # permutation (1 2), J = Ad_Jm, J^-1 = J
lhs = Jm * U(pi / 2) * dag(Jm) * E(0, 0) * dag(Jm * U(pi / 2) * dag(Jm))
rhs = U(s) * E(0, 0) * dag(U(s))
rep.check("J_off_axis: J F(pi/2) J^-1 |0><0| = |2><2|, while F(s)|0><0| has (2,2) entry 0 for every s",
          lhs.applyfunc(simplify) == E(2, 2) and simplify(rhs[2, 2]) == 0)
rep.note("so ElementaryDrivability holds on the qutrit body: K-inf-Drive is NOT elementary-scoped (continuity of the "
         "flow: entries are polynomials in cos t, sin t).")

# ---------------- qubit: the drive's NOT can be aligned with DIM-1's NOT (seam check)
Rx = lambda tt: Matrix([[1, 0, 0], [0, cos(tt), -sin(tt)], [0, sin(tt), cos(tt)]])
cyc = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])                  # kernel cyc3: (v0,v1,v2) -> (v2,v0,v1)
rep.check("qubit drive about the first axis: R_x(pi) = nflip (DIM-1's NOT = Ad_X), R_x a flow of ball automorphisms",
          Rx(pi) == NFLIP and (Rx(t) * Rx(t).T).applyfunc(simplify) == eye(3) and
          (Rx(s) * Rx(t) - Rx(s + t)).applyfunc(lambda e: simplify(trigsimp(expand(e, trig=True)))) == zeros(3, 3))
e1 = Matrix([1, 0, 0])
off = cyc * Rx(pi / 2) * cyc.T * e1
rep.check("J = cyc3 is off-axis for R_x: J R_x(pi/2) J^-1 e1 != e1 = R_x(s) e1 for all s", off != e1,
          "J R J^-1 e1 = %s" % off.T)
rep.check("the kernel's control drive ball3Drive (flow rot3 about the third axis) has NOT diag(-1,-1,1) = Ad_Z, which "
          "FIXES z3: the landed drive and DIM-1's NOT are different maps in the same chart",
          Matrix([[cos(pi), -sin(pi), 0], [sin(pi), cos(pi), 0], [0, 0, 1]]) * Z3 == Z3)

# ---------------- dense K-inf-Trans by a QM-compatible countable family (rational rotations)
def householder(v):
    v = Matrix(v)
    return eye(3) - 2 * v * v.T / (v.T * v)[0]
u = Matrix([0, 0, 1]); w = Matrix([R(2, 3), R(1, 3), R(2, 3)])
Hh1 = householder(u - w)                       # rational reflection mapping u to w
Hh2 = householder(w.cross(Matrix([1, 0, 0])))  # rational reflection fixing w
Rq = Hh2 * Hh1
rep.check("a product of two rational Householder reflections is a rational ROTATION (det +1) mapping z3 to (2/3,1/3,2/3)",
          Rq * u == w and Rq.det() == 1 and Rq * Rq.T == eye(3) and all(e.is_Rational for e in Rq))
rep.note("so the rational rotation group (countable, orientation-preserving, = rational unitary conjugations) carries a "
         "rational unit vector to every rational unit vector: a dense boundary orbit on the Bloch sphere. The kernel's "
         "dense witness `ratRefl` (DenseOrbit:342) is a family of REFLECTIONS (antiunitary in QM), which K2Guard shows "
         "incompatible with cnot on a candidate cone; the rotation family is the QM-compatible choice.")

ok = rep.out()
sys.exit(0 if ok else 1)
