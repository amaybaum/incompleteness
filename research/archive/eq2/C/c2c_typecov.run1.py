"""EQ2-C, C2(c): EQ-E T2 (the NOT-conjugacy reduction) refined to the gate route's CtrlGate form.

Statement (UNBUILT, RESULT.md): a two-NOT control gate (frame, posFwd, posInv on maxCone (eball d), and
relC with the control's NOT N_A and the target's NOT N_B: actC N_A (G (actC N_A w)) = actT N_B (G w)), together with
type covariance N_B = g N_A g^-1 for a linear g fixing z and preserving the ball, gives
CtrlGate (eball d) z N_A (actT g^-1 . G . actT g)  -- no relT is read, so RSB's dim_of_ctrlGate (RSB:739) applies.

DECISION RULE (fixed before the first run). Verdict "TYPECOV-CTRL" prints only if all pass:
  TC.1 the quantum instance (EQ-E s4/T6): the kernel cnot satisfies the two-NOT relC with N_B = nflip and
       N_A = [[-7/25, 24/25, 0], [24/25, 7/25, 0], [0, 0, -1]] (the pi-rotation about (3/5, 4/5, 0)); N_A is a NOT.
  TC.2 g = the rotation about z carrying (3/5, 4/5, 0) to e1: g z = z, g orthogonal, N_B = g N_A g^-1.
  TC.3 T~ = actT g^-1 . cnot . actT g has the frame and relC with the common NOT N_A (CtrlGate's relation).
  TC.4 the positivity transfer identities, symbolic: actT A (prodState x y) = prodState x (A y);
       pairVal a b (actT A w) = pairVal a (homMap(A)^T b) w; homMap(A)^T preserves the Lorentz cone for orthogonal A.
  TC.5 countercontrol: conjugating by a rotation that does not fix z breaks the frame.
  TC.6 load-bearing: gC5 with N_A' = diag(1,-1,1,-1,-1) and N_B = nC5 satisfies the frame and the two-NOT relC
       (NB-1's C2N pair, EQ-B C5), N_A' is a NOT of eball 5 with z5, and no linear g conjugates N_A' to nC5
       (traces -1 and -3): the two-NOT CtrlGate clauses do not give type covariance.
  TC.7 the relation actC N (actT M w) = actT M (actC N w) used in the proof (symbolic, d = 3).
Exact (sympy rationals and polynomials).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "vendor_bal"))
from c_common import Checks  # noqa: E402
from sympy import Matrix, Rational as R, eye, zeros, diag, symbols, expand  # noqa: E402
from relt_common import (hom, homMap, apply, actT_mat, actC_mat, frame, prod, pairVal, isNot, dim1_cnot)  # noqa
from bal_gates import landed_gC5  # noqa: E402

C = Checks("c2c_typecov")

z3 = Matrix([0, 0, 1])
nflip = diag(1, -1, -1)
G = dim1_cnot()
NA = Matrix([[R(-7, 25), R(24, 25), 0], [R(24, 25), R(7, 25), 0], [0, 0, -1]])


def relC2(G, NA, NB):
    return (actC_mat(NA) * G * actC_mat(NA) - actT_mat(NB) * G).is_zero_matrix


C.check("TC.1 the kernel cnot satisfies the two-NOT relation relC(N_A, nflip) with N_A the pi-rotation about "
        "(3/5, 4/5, 0); N_A is a NOT of the ball (unit z, involution, orthogonal, flips z); N_A != nflip",
        relC2(G, NA, nflip) and all(isNot(z3, NA).values()) and NA != nflip)
g = Matrix([[R(3, 5), R(4, 5), 0], [R(-4, 5), R(3, 5), 0], [0, 0, 1]])
C.check("TC.2 type covariance: g (rotation about z, (3/5,4/5,0) -> e1) fixes z, is orthogonal with det 1, and "
        "nflip = g N_A g^-1", g * z3 == z3 and g.T * g == eye(3) and g.det() == 1 and g * NA * g.inv() == nflip)
Gt = actT_mat(g.inv()) * G * actT_mat(g)
C.check("TC.3 T~ = actT g^-1 . cnot . actT g has the frame on +-z and relC(N_A, N_A): a CtrlGate with the common NOT "
        "N_A", frame(Gt, z3) and relC2(Gt, NA, NA))
xs, ys = symbols("x0:3"), symbols("y0:3")
a_s, b_s = symbols("a0:4"), symbols("b0:4")
w_s = Matrix(4, 4, symbols("w0:16"))
A_s = Matrix(3, 3, symbols("m0:9"))
lhs1 = apply(actT_mat(A_s), prod(Matrix(xs), Matrix(ys)))
rhs1 = prod(Matrix(xs), A_s * Matrix(ys))
lhs2 = pairVal(Matrix(a_s), Matrix(b_s), apply(actT_mat(A_s), w_s))
rhs2 = pairVal(Matrix(a_s), homMap(A_s).T * Matrix(b_s), w_s)
bt = homMap(g).T * Matrix(b_s)
C.check("TC.4 positivity transfer (symbolic): actT A (prodState x y) = prodState x (A y) [kernel K2G:173]; "
        "pairVal a b (actT A w) = pairVal a (homMap(A)^T b) w; for orthogonal g, homMap(g)^T fixes b0 and the "
        "tail norm (so it maps the Lorentz cone onto itself and effects to effects)",
        expand(lhs1 - rhs1) == Matrix.zeros(4, 4) and expand(lhs2 - rhs2) == 0 and bt[0] == b_s[0]
        and expand(sum(bt[i] ** 2 for i in range(1, 4)) - sum(b_s[i] ** 2 for i in range(1, 4))) == 0)
gx = Matrix([[1, 0, 0], [0, R(3, 5), R(-4, 5)], [0, R(4, 5), R(3, 5)]])     # rotation about x: moves z
Gx = actT_mat(gx.inv()) * G * actT_mat(gx)
C.check("TC.5 countercontrol: conjugating cnot by a rotation about x (which moves z) breaks the frame",
        gx * z3 != z3 and not frame(Gx, z3))
z5 = Matrix([0, 0, 0, 0, 1])
nC5 = diag(1, -1, -1, -1, -1)
NA5 = diag(1, -1, 1, -1, -1)
G5 = landed_gC5()
C.check("TC.6 load-bearing: gC5 satisfies the frame and the two-NOT relC(N_A', nC5) with N_A' = diag(1,-1,1,-1,-1) a "
        "NOT of eball 5 (axis z5); trace N_A' = -1, trace nC5 = -3, so no linear g gives nC5 = g N_A' g^-1",
        frame(G5, z5) and relC2(G5, NA5, nC5) and all(isNot(z5, NA5).values()) and NA5.trace() == -1
        and nC5.trace() == -3)
M_s = Matrix(3, 3, symbols("n0:9"))
C.check("TC.7 actC N (actT M w) = actT M (actC N w) (symbolic N, M, w at d = 3): the two local actions commute",
        expand(actC_mat(A_s) * actT_mat(M_s) - actT_mat(M_s) * actC_mat(A_s)) == Matrix.zeros(16, 16))

sys.exit(C.finish("TYPECOV-CTRL: type covariance reduces the two-NOT control gate to a CtrlGate with one NOT "
                  "(no relT read); QM instance exact; the conjugating map must fix z; the two-NOT clauses alone do "
                  "not give type covariance (gC5 with NB-1's C2N pair)"))
