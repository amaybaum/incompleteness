"""B4 (node N3) -- exact inputs of a Lie-light route for the general gate case and the continuous case.

The route (written in NOTES N3): let Gamma be a group of linear maps of W 3, each preserving cl K (K admissible) and u.
Y := {gamma'(0) : gamma a differentiable curve in Gamma with gamma(0) = 1}, s := span Y. Then
  (i)  every element of Y satisfies the first-order condition V1 and is antisymmetric for the IIP-1 form Q;
  (ii) s is a Lie algebra (Y is Ad_Gamma-invariant; the derivative of Ad_gamma(t) W is [gamma'(0), W]);
  (iii) l <= s <= V1 n so(Q) <= l + M1 + M2, and the l-module and bracket facts leave s in {l, l + M1, l + M2};
  (iv) s = l forces every element of Gamma to normalize l, hence to map products to products (EQ-C P3);
  (v)  a basis of s drawn from Y and the inverse function theorem give all of Ad SU(4) inside Gamma.
Decision rule (fixed before run 1; A.1 restated for run 2 after run 1 refuted its expected count): each exact input
below is reported only with its control/countercontrol:
  * Q-antisymmetry: V1 n so(Q) is reported as an explicit l-module only if its exact dimension equals that of the
    explicit module and their spans coincide (five block scalars Q); the bracket test decides which are Lie algebras;
  * the span of Ad_w l over short words w in cnot and P (Pauli-sign elements of L) is exactly l + M1 (dimension 15),
    for cnot' exactly l + M2, and for T cnot again l + M1; each conjugated generator lies in V1 and is Euclidean-skew;
  * countercontrol: for the non-normalizing G = onC(boost) o cnot, Ad_G l leaves the u-preserving maps;
  * the Lie closure of l and Ad_cnot l has dimension 15, and with Ad_cnot' l added 105 (no admissible cone for both).
Usage: python3 -I -B b4_lie_light.py <base>/verification/lean-mathlib/OIBridge/CompositeDimension.lean
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eq2b_lib import *  # noqa

rep = Report("B4 Lie-light route inputs")
CNOT = parse_kernel_cnot(sys.argv[1])[0]
CN2 = mmul(mmul(RB, CNOT), RB)
L_ = [ad_herm(SIG2[(i, 0)]) for i in (1, 2, 3)] + [ad_herm(SIG2[(0, j)]) for j in (1, 2, 3)]
M1 = [ad_herm(SIG2[(i, j)]) for i in (1, 2, 3) for j in (1, 2, 3)]
M2 = [mmul(mmul(RB, m), RB) for m in M1]


def so3gen(k):
    J = [[Fr(0)] * 3 for _ in range(3)]
    i, j = [(1, 2), (2, 0), (0, 1)][k]
    J[i][j], J[j][i] = Fr(-1), Fr(1)
    return J


def corr_tensor(A, B):
    X = zeros(16, 16)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l_ in range(3):
                    v = A[i][k] * B[j][l_]
                    if v != 0:
                        X[4 * (i + 1) + (j + 1)][4 * (k + 1) + (l_ + 1)] += v
    return X


NN = [corr_tensor(so3gen(a), so3gen(b)) for a in range(3) for b in range(3)]
fl = lambda S: [flat(X) for X in S]  # noqa


def unit_vec(s, t):
    s, t = F(s), F(t)
    d = 1 + s * s + t * t
    return [2 * s / d, 2 * t / d, (s * s + t * t - 1) / d]


POOL = [unit_vec(s, t) for (s, t) in [(0, 0), (1, 0), (0, 1), (2, 0), (0, 3), (1, 1), (Fr(1, 2), 2), (3, -1),
                                         (-2, Fr(1, 3)), (Fr(2, 5), Fr(-3, 4)), (5, 7), (-1, -4)]]
POOL += [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0]]


def in_V1(X):
    """First-order condition at sampled pure products and u o X = 0 (necessary test; V1 itself is EQ-C P2's exact 33)."""
    if any(c != 0 for c in X[0]):
        return False
    for x in POOL:
        for y in POOL:
            w = apply(X, prodState(x, y))
            hx, hy = hom([-F(c) for c in x]), hom([-F(c) for c in y])
            if any(sum(hx[m] * w[m][n] for m in range(4)) != 0 for n in range(4)):
                return False
            if any(sum(w[m][n] * hy[n] for n in range(4)) != 0 for m in range(4)):
                return False
    return True


rep.check("A.0 controls: l, M1, M2, N each satisfy the sampled first-order condition and u o X = 0; together they span 33 "
          "(EQ-C's V1, replayed separately)", all(in_V1(X) for X in L_ + M1 + M2 + NN)
          and rank(fl(L_ + M1 + M2 + NN), 256) == 33)

# ---------------------------------------------------------------- Part A: antisymmetry for block-scalar Q
blk = {}
for (m, n) in IDX:
    blk[4 * m + n] = "00" if (m, n) == (0, 0) else ("A" if n == 0 else ("B" if m == 0 else "AB"))


def Qmat(b, bp, c):
    val = {"00": Fr(1), "A": F(b), "B": F(bp), "AB": F(c)}
    M = zeros(16, 16)
    for k in range(16):
        M[k][k] = val[blk[k]]
    return M


def skew_Q(X, Q):
    return is_zero(madd(mmul(tr(X), Q), mmul(Q, X)))


PIB = actT(diag3(-1, -1, -1))                      # Pi_B: phi(X) = Pi_B X Pi_B maps M1 onto M2 (EQ-C P2 2.0b)
GMINUS = [madd(X, mmul(mmul(PIB, X), PIB), 1, -1) for X in M1]   # connects the A-marginal block and the correlations
GPLUS = [madd(X, mmul(mmul(PIB, X), PIB), 1, 1) for X in M1]     # connects the B-marginal block and the correlations


def V1_soQ(Q):
    """Exact basis of V1 n so(Q) inside span(l, M1, M2, N) (= V1 by EQ-C P2)."""
    basis = L_ + M1 + M2 + NN
    cols = [flat(madd(mmul(tr(X), Q), mmul(Q, X))) for X in basis]
    rows = [[cols[k][i] for k in range(len(basis))] for i in range(256)]
    out = []
    for c in nullspace(rows, len(basis)):
        X = zeros(16, 16)
        for k, ck in enumerate(c):
            if ck != 0:
                X = madd(X, basis[k], 1, ck)
        out.append(X)
    return out


expect = {"Euclid (1,1,1)": L_ + M1 + M2, "(1,2,1)": L_ + GMINUS, "(2,1,1)": L_ + GPLUS, "(1,1,2)": L_,
          "(2,3,5)": L_}
res, ident = {}, True
for name, q in [("Euclid (1,1,1)", (1, 1, 1)), ("(1,2,1)", (1, 2, 1)), ("(2,1,1)", (2, 1, 1)), ("(1,1,2)", (1, 1, 2)),
                ("(2,3,5)", (2, 3, 5))]:
    Q = Qmat(*q)
    S = V1_soQ(Q)
    res[name] = len(S)
    ident &= rank(fl(S), 256) == rank(fl(expect[name]), 256) == rank(fl(S + expect[name]), 256)
    ident &= all(skew_Q(X, Q) for X in L_)
rep.note("dim V1 n so(Q) for Q = diag(1, b I3, b' I3, c I9): " + str(res))
rep.check("A.1 [run 1 expected 6 for every non-Euclidean Q; refuted] l is Q-skew for every block scalar Q, and V1 n so(Q) "
          "is exactly l + M1 + M2 (b = b' = c), l + G- (b = c != b'), l + G+ (b' = c != b), or l (c differs from both), "
          "with G-+ = {X -+ phi X : X in M1} the two graph submodules", ident
          and [res[k] for k in expect] == [24, 15, 15, 6, 6])
wit = None
for i, X in enumerate(GMINUS):
    for j, Y in enumerate(GMINUS):
        if rank(fl(L_ + GMINUS + [bracket(X, Y)]), 256) > 15 and not in_V1(bracket(X, Y)):
            wit = (i, j)
            break
    if wit:
        break
witp = None
for i, X in enumerate(GPLUS):
    for j, Y in enumerate(GPLUS):
        if rank(fl(L_ + GPLUS + [bracket(X, Y)]), 256) > 15 and not in_V1(bracket(X, Y)):
            witp = (i, j)
            break
    if witp:
        break
rep.check("A.2 G- and G+ are 9-dimensional and neither l + G- nor l + G+ is closed under brackets: an exact bracket of "
          "two graph elements leaves V1 (so a Lie algebra s with l <= s <= V1 n so(Q) is l unless Q is Euclidean)",
          rank(fl(GMINUS), 256) == 9 and rank(fl(GPLUS), 256) == 9 and wit is not None and witp is not None,
          f"witness pairs {wit}, {witp}")
rep.note("A.3 [written] so the IIP-1 form alone does not exclude the graphs; the bracket obstruction does. An admissible "
         "cone with a symmetry that does not normalize L therefore has a Euclidean IIP-1 form on ker u; for Q3 this is the "
         "Hilbert-Schmidt form.")

# ---------------------------------------------------------------- Part B: the span of Ad_w l
SO_DIAG = [diag3(1, 1, 1), diag3(1, -1, -1), diag3(-1, 1, -1), diag3(-1, -1, 1)]
PGRP = [mmul(actC(D), actT(Dp)) for D in SO_DIAG for Dp in SO_DIAG]
ROTS = [mmul(actC(rot_axis(a, Fr(3, 5), Fr(4, 5))), actT(rot_axis(b, Fr(5, 13), Fr(12, 13)))) for a in range(3)
        for b in range(3)]


def conj(g, X):
    return mmul(mmul(g, X), minv(g))


def span_words(gate):
    words = [I16, gate]
    for r in ROTS[:4] + PGRP[1:6]:
        words.append(mmul(gate, r))
        words.append(mmul(mmul(gate, r), gate))
    gens = []
    for w in words:
        for Y in L_:
            gens.append(conj(w, Y))
    return gens


GC = span_words(CNOT)
ok_v1 = all(in_V1(X) and skew_Q(X, Qmat(1, 1, 1)) for X in GC[:60])
rep.check("B.1 the conjugated generators Ad_w Y (w a word in cnot and local rotations, Y in l) satisfy V1 and are "
          "Euclidean-skew (first 60 checked exactly)", ok_v1)
rS = rank(fl(GC), 256)
rep.check(f"B.2 span of Ad_w l over the cnot words has dimension {rS} and equals l + M1 (the su(4) image)",
          rS == 15 and rank(fl(GC + M1 + L_), 256) == 15)
GC2 = span_words(CN2)
rep.check("B.3 for cnot' the same span is l + M2 (the twisted image), dimension 15",
          rank(fl(GC2), 256) == 15 and rank(fl(GC2 + M2 + L_), 256) == 15 and rank(fl(GC2 + M1), 256) > 15)
GT = span_words(mmul(TT, CNOT))
rep.check("B.4 for the antiunitary gate T cnot the span is again l + M1 (T acts on su(4) as X -> -X^T)",
          rank(fl(GT), 256) == 15 and rank(fl(GT + M1 + L_), 256) == 15)
basis15 = []
for X in GC:
    if rank(fl(basis15 + [X]), 256) > len(basis15):
        basis15.append(X)
rep.check("B.5 a basis of s = l + M1 can be drawn from the conjugated generators themselves (15 independent elements of "
          "Y, as the inverse-function step needs)", len(basis15) == 15)

# ---------------------------------------------------------------- Part C: countercontrol, normalization
BST = [[Fr(5, 3), Fr(0), Fr(0), Fr(4, 3)], [Fr(0), Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(1), Fr(0)],
       [Fr(4, 3), Fr(0), Fr(0), Fr(5, 3)]]
Gb = mmul(onC(BST), CNOT)
bad = [conj(Gb, Y) for Y in L_]
rep.check("C.1 countercontrol: for G = onC(boost) o cnot (maps Q3 onto Q3, not u-preserving) some Ad_G Y, Y in l, has "
          "u o X != 0, so it lies outside V1 and the Lie-light route does not apply",
          any(any(c != 0 for c in X[0]) for X in bad))

# ---------------------------------------------------------------- Part D: Lie closures
def lie_closure(gens, cap=256):
    basis = []
    for X in gens:
        if rank(fl(basis + [X]), 256) > len(basis):
            basis.append(X)
    frontier = list(basis)
    while frontier and len(basis) < cap:
        new = []
        for A in basis:
            for B in frontier:
                C = bracket(A, B)
                if rank(fl(basis + [C]), 256) > len(basis):
                    basis.append(C)
                    new.append(C)
        frontier = new
    return len(basis)


d1 = lie_closure(L_ + [conj(CNOT, Y) for Y in L_])
rep.check(f"D.1 the Lie algebra generated by l and Ad_cnot l has dimension {d1} = 15", d1 == 15)
rep.note("D.2 the closure with Ad_cnot' l added is EQ-C P2's 'l + M1 + M2 generates 105' (replayed in replay/), so no "
         "admissible cone carries both cnot and cnot' (also K2Guard and B2's chains)")
rep.verdict("LIE-LIGHT-INPUTS: Q-skewness with the bracket obstruction forces a Euclidean form once s != l; the conjugated generators of cnot (cnot', "
            "T cnot) span exactly l + M1 (l + M2, l + M1) and contain a basis of it; normalization is load-bearing; "
            "the generated algebra is 15-dimensional")
