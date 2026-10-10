"""B5 (node N4) -- IE1 accounting: what the landed rotation family is, and what Theorem A' needs when the local
invariance holds only for a smaller family.

Claims tested (decision rule fixed before the run):
  * driveWords3 (OrbitNormalization.lean:571) = words(range rot3 u {cyc3}) is reported EQUAL to SO(3) only from: the
    exact conjugation identity cyc3 R_z(t) cyc3^-1 = R_x(t) (symbolic in cos t, sin t), the exact stabilizer identity
    (an orthogonal det-1 matrix fixing e_z is R_z), the landed exists_word_pole (ON:658) and the generators being
    rotations; it is then uncountable (range rot3 is a circle).
  * Countable dense regime: the rational-quaternion rotations D_Q form a countable group (exact quaternion
    multiplicativity of R(q)), and their SU(2) lifts and CNOT have entries in Q(i) (exact). The K_d countermodel's
    exact ingredient (every element of G_D is Ad of a Q(i) matrix, so "U^-1 psi is a product" is a nonzero quadratic
    condition over Q(i)) is checked on the generators.
  * Finite-group regime: with the local invariance restricted to the octahedral rotations F (24 per copy), the group
    generated with cnot is finite (the two-qubit Clifford group modulo phases); a pure state psi is exhibited whose whole
    orbit stays entangled, so cone(<F, cnot> . products) is a closed, convex, admissible, <F, cnot>-invariant cone
    different from Q3 and from R_B Q3. Control: a pure product's orbit contains products. Same for the order-8 native
    group H = <cnot, actC nflip, actT nflip> (k2d T6, re-derived).
Usage: python3 -I -B b5_ie1.py <base>/verification/lean-mathlib/OIBridge/CompositeDimension.lean
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eq2b_lib import *  # noqa
import sympy as sp

rep = Report("B5 IE1 accounting")
CNOT = parse_kernel_cnot(sys.argv[1])[0]

# ---------------------------------------------------------------- Part A: driveWords3 = SO(3)
c, s = sp.symbols("c s", real=True)
CYC = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])      # cyc3 v = (v2, v0, v1) (KF:425)
RZ = sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])      # rotFun (KF:351): rotates coordinates 0, 1, fixes 2
RX = sp.Matrix([[1, 0, 0], [0, c, -s], [0, s, c]])
rep.check("A.1 cyc3 has determinant +1 and cyc3 R_z(t) cyc3^-1 = R_x(t) as a polynomial identity in (cos t, sin t) "
          "(the kernel's rotX, ON:581, is this word)", CYC.det() == 1 and sp.simplify(CYC * RZ * CYC.inv() - RX) == sp.zeros(3, 3))
a, b, cc, d = sp.symbols("a b cc d", real=True)
Mz = sp.Matrix([[a, b, 0], [cc, d, 0], [0, 0, 1]])
# sum-of-squares certificate (no solver: sympy.solve is hash-order dependent under -I, see NOTES N4):
# (a - d)^2 + (b + cc)^2 = (a^2 + cc^2 - 1) + (b^2 + d^2 - 1) - 2 (a d - b cc - 1), and the right side vanishes on
# the orthogonality and determinant equations (the (1,1), (2,2) entries of M^T M - I and det M - 1).
OO = Mz.T * Mz - sp.eye(3)
rep.check("A.2 an orthogonal determinant-1 matrix with third column e_z and third row e_z^T has a = d, b = -c (so it is "
          "R_z): exact identity (a-d)^2 + (b+c)^2 = (M^T M - I)_00 + (M^T M - I)_11 - 2 (det M - 1)",
          sp.expand((a - d) ** 2 + (b + cc) ** 2 - (OO[0, 0] + OO[1, 1] - 2 * (Mz.det() - 1))) == 0
          and sp.expand(OO[0, 0] - (a ** 2 + cc ** 2 - 1)) == 0 and sp.expand(OO[1, 1] - (b ** 2 + d ** 2 - 1)) == 0)
rep.note("A.3 [written, landed pieces] for R in SO(3), exists_word_pole (ON:658) gives a word g = rot3 psi * rotX theta in "
         "driveWords3 with g e_z = R e_z; g^-1 R fixes e_z, has det 1, and is orthogonal, so it is R_z(phi) = rot3 phi by "
         "A.2 (its third row is e_z^T by orthogonality); hence R = g * rot3 phi lies in driveWords3. Conversely every "
         "generator is a rotation. So driveWords3 = SO(3) (as affine maps fixing 0), and range rot3 alone is "
         "uncountable: driveWords3 is NOT countable, and IE1 stated over driveWords3 is exactly IE1 over SO(3).")

# ---------------------------------------------------------------- Part B: the countable dense regime
q1 = sp.symbols("p0:4", real=True)
q2 = sp.symbols("r0:4", real=True)


def Rsym(q):
    a_, b_, c_, d_ = q
    n = a_ ** 2 + b_ ** 2 + c_ ** 2 + d_ ** 2
    return sp.Matrix([[a_ * a_ + b_ * b_ - c_ * c_ - d_ * d_, 2 * (b_ * c_ - a_ * d_), 2 * (b_ * d_ + a_ * c_)],
                      [2 * (b_ * c_ + a_ * d_), a_ * a_ - b_ * b_ + c_ * c_ - d_ * d_, 2 * (c_ * d_ - a_ * b_)],
                      [2 * (b_ * d_ - a_ * c_), 2 * (c_ * d_ + a_ * b_), a_ * a_ - b_ * b_ - c_ * c_ + d_ * d_]]) / n


def qmul(x, y):
    a1, b1, c1, d1 = x
    a2, b2, c2, d2 = y
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)


rep.check("B.1 R(p) R(r) = R(p r) (quaternion product) as a rational-function identity: the rational-quaternion rotations "
          "D_Q form a countable subgroup of SO(3)", sp.simplify(Rsym(q1) * Rsym(q2) - Rsym(qmul(q1, q2))) == sp.zeros(3, 3))
ok = all(all(x.re.denominator == 1 and x.im.denominator == 1 for r in su2_of_quat(q) for x in r)
         for q in [(1, 2, -1, 3), (2, 0, 1, 1), (1, 1, 1, 1)]) and all(x.im == 0 for r in CNOT_U for x in r)
rep.check("B.2 the unnormalized lifts U_q = q0 I - i q.sigma of integer quaternions have Gaussian-integer entries and CNOT "
          "has integer entries, so every element of G_D = <cnot, actC R, actT R : R in D_Q> is Ad of a matrix over Q(i)", ok)
x0, x1, x2, x3 = sp.symbols("x0:4")
detform = x0 * x3 - x1 * x2
Hm = sp.Matrix([[x0, x1], [x2, x3]])
rep.check("B.3 the product test for a pure state psi = (x0, x1, x2, x3) is the nondegenerate quadratic form x0 x3 - x1 x2 "
          "(det of its 2x2 coefficient matrix; Gram determinant nonzero), so for U over Q(i) invertible, "
          "'U^-1 psi is a product' is a nonzero quadratic equation over Q(i) in psi",
          sp.Matrix(4, 4, lambda i, j: sp.diff(detform, [x0, x1, x2, x3][i], [x0, x1, x2, x3][j])).det() != 0
          and sp.expand(Hm.det() - detform) == 0)
rep.note("B.4 [written; literature for one step] K_d := cone(G_D . products) is convex, admissible (inside Q3 since "
         "G_D <= Ad U(4)), G_D-invariant, with closure Q3 (B.5), and not closed: a pure state psi with coordinates "
         "algebraically independent over Q(i) (e.g. (1, e, e^sqrt2, e^sqrt3), Lindemann-Weierstrass [L, unverified; "
         "Mathlib v4.33.0 has only its analytic part]) satisfies no nonzero quadratic equation over Q(i), so psi psi^dag "
         "is not in K_d (a pure state of K_d is extreme in Q3, hence a G_D-image of a pure product). A Baire-category "
         "argument gives the same without transcendence.")
rep.note("B.5 [written; Mathlib v4.33.0 Convex.interior_closure_eq_interior_of_nonempty_interior, "
         "Analysis/Convex/Topology.lean:268, verified present] if K is convex, admissible, cnot- and D-invariant with D "
         "dense, then cl K is closed and invariant under all of SO(3)^2 (continuity), so cl K is Q3 or R_B Q3 by Theorem "
         "A', and interior(cl K) = interior(K): int Q3 <= K <= Q3 (or the twin). Only the boundary is unpinned.")

# ---------------------------------------------------------------- Part C: finite-group regime (Clifford orbit)
R90z, R90x = rot_axis(2, 0, 1), rot_axis(0, 0, 1)
GENS = [actC(R90z), actC(R90x), actT(R90z), actT(R90x), CNOT]


def key(M):
    return tuple(flat(M))


def closure_group(gens, limit=20000):
    seen = {key(I16): I16}
    frontier = [I16]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                p = mmul(h, g)
                k = key(p)
                if k not in seen:
                    seen[k] = p
                    new.append(p)
        frontier = new
        if len(seen) > limit:
            break
    return list(seen.values())


CLIFF = closure_group(GENS)
rep.check(f"C.1 the group generated by the local octahedral rotations and cnot is finite of order {len(CLIFF)} "
          "(11520 = |two-qubit Clifford group / phases|) and consists of signed permutations fixing e00",
          len(CLIFF) == 11520 and all(M[0] == [Fr(1)] + [Fr(0)] * 15 for M in CLIFF[:200]))


def w_of_psi(psi):
    """W coordinates of psi psi^dag / |psi|^2 for a real rational vector psi (normalized so w00 = 1)."""
    R = [[G(F(psi[i]) * F(psi[j])) for j in range(4)] for i in range(4)]
    n = sum(F(t) * F(t) for t in psi)
    w = w_of_rho(R)
    return [[x / n for x in r] for r in w]


def marg_norm2(w):
    return sum(w[k][0] ** 2 for k in (1, 2, 3))


psi = [1, 1, 1, 2]
wpsi = w_of_psi(psi)
norms = [marg_norm2(apply(M, wpsi)) for M in CLIFF]
rep.check("C.2 psi = (1, 1, 1, 2)/sqrt7 is pure (w00 = 1, |all 15 coordinates|^2 = 3) and every element of its Clifford "
          "orbit has a mixed marginal (|Bloch_A|^2 < 1): no Clifford image of psi is a product",
          sum(x * x for r in wpsi for x in r) - 1 == 3 and max(norms) < 1, f"max |Bloch_A|^2 = {max(norms)}")
wprod = prodState([1, 0, 0], [0, 0, 1])
rep.check("C.3 control: a pure product's orbit contains products (marginal norm 1 occurs)",
          max(marg_norm2(apply(M, wprod)) for M in CLIFF) == 1)
H = closure_group([CNOT, actC(NFLIP), actT(NFLIP)])
normsH = [marg_norm2(apply(M, wpsi)) for M in H]
rep.check("C.4 the native group H = <cnot, actC nflip, actT nflip> has order 8 and psi's H-orbit stays entangled "
          "(k2d T6's interval C_H < Q3, re-derived)", len(H) == 8 and max(normsH) < 1)
rep.note("C.5 [written] K_F := cone(<F, cnot> . products) is closed (finite union of compact images, conv-hull of a compact "
         "set), convex, admissible, <F, cnot>-invariant, inside Q3; a pure state of K_F is extreme in Q3, hence a group "
         "image of a pure product; psi psi^dag is not one (C.2), so K_F != Q3 and K_F != R_B Q3 (R_B Q3 is not inside "
         "Q3). Hence IE1 restricted to a finite subgroup fails even for closed cones.")
rep.verdict("IE1-REGIMES: driveWords3 = SO(3) (uncountable; IE1 over it is full IE1); countable dense local families need a "
            "closed cone (otherwise only int Q3 <= K <= Q3); finite local families fail even for closed cones "
            "(Clifford orbit and the native group H)")
