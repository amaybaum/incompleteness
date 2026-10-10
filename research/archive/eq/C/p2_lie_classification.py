"""P2 (node N2, decisive) -- run 2.  The Lie algebra of every compact connected group H of normalization-
preserving linear maps with L = local SO(3)^2 <= H, preserving an admissible two-ball cone (min <= K <= maxCone).

Setting: W 3 = R^4 (x) R^4 with DIM-1's coordinates. X ranges over 16x16 real matrices with u o X = 0
(u = the (0,0) coordinate, normalization): 240 unknowns.

First-order (necessary) condition V1: if exp(tX) preserves a cone K with min <= K <= maxCone, then for every
pure product state w = hom x (x) hom y (|x| = |y| = 1) and product effect E = (1,a) (x) (1,b) with E(w) = 0
(a = -x or b = -y), t -> E(exp(tX) w) >= 0 vanishes at t = 0, so E(X w) = 0.  As the (1,b), |b| = 1, span R^4:
(1,-x)^T (X w) = 0 and (X w)(1,-y) = 0.

Run 1 (kept as p2_lie_classification.run1.*) refuted the draft expectation dim V1 = 24: the exact upper bound is 33.
Run 2 adds the identified 9-dimensional piece N = {J_a (x) J_b on the correlation block} to the lower bound and the
compactness step that removes it.

Decision rule (fixed before run 2):
  * dim V1 is reported only if the exact upper bound (rational rank) equals an explicit lower bound verified
    symbolically for all unit x, y;
  * the compactness step is rendered only if: the l-invariant symmetric bilinear forms are exactly the block
    scalars (dimension 4, exact), M1 and M2 have zero (3,3)->(3,3) block, l has antisymmetric (3,3)->(3,3)
    block, and N -> (its (3,3)->(3,3) block) is injective with symmetric image (all exact);
  * the classification verdict is printed only if, in addition, the submodule/bracket checks pass and the
    controls pass (l, M1, M2, N in V1; generic so(15) not in V1).
Usage: python3 -I p2_lie_classification.py
"""
import sys
import os
import time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eqclib import *  # noqa
import sympy as sp

t0 = time.time()
rep = Report("P2 Lie classification (run 2)")

# ------------------------------------------------------------------ the pieces
L_ = [ad_herm(SIG2[(i, 0)]) for i in (1, 2, 3)] + [ad_herm(SIG2[(0, j)]) for j in (1, 2, 3)]
M1 = [ad_herm(SIG2[(i, j)]) for i in (1, 2, 3) for j in (1, 2, 3)]
RB = actT_mat(REFLY)
PB = actT_mat(MINUS)
M2 = [matmul(matmul(RB, m), RB) for m in M1]
PHI = [matmul(matmul(PB, m), PB) for m in M1]  # phi(v) = Pi_B v Pi_B, an l-module map M1 -> M2


def so3gen(k):
    """J_k: (J_k)_{ij} = -eps_{kij} (rotation generator about axis k)."""
    J = [[Fr(0)] * 3 for _ in range(3)]
    eps = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
    for (a, b, c), s in eps.items():
        if a == k:
            J[b][c] = Fr(-s)
    return J


def corr_tensor(A, B):
    """16x16 matrix of w -> (A M B^T) on the correlation block M = w[1:,1:], zero elsewhere."""
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
rep.check("2.0a dim l = 6, dim M1 = 9, dim M2 = 9, dim N = 9, dim(l + M1 + M2 + N) = 33",
          span_rank(fl(L_)) == 6 and span_rank(fl(M1)) == 9 and span_rank(fl(M2)) == 9
          and span_rank(fl(NN)) == 9 and span_rank(fl(L_ + M1 + M2 + NN)) == 33)
rep.check("2.0b span(phi(M1)) = M2 (phi = conjugation by Pi_B = actT(-I))",
          span_rank(fl(M2) + fl(PHI)) == 9)


def gen(i, j):
    Lm = [[0] * 3 for _ in range(3)]
    Lm[i][j], Lm[j][i] = 1, -1
    return Lm


def hom_gen(Lm, side):
    H = zeros(4, 4)
    for a in range(3):
        for b in range(3):
            H[a + 1][b + 1] = Fr(Lm[a][b])
    M = zeros(16, 16)
    for (m, n) in IDX:
        for k in range(4):
            if side == "T" and H[n][k] != 0:
                M[4 * m + n][4 * m + k] = H[n][k]
            if side == "C" and H[m][k] != 0:
                M[4 * m + n][4 * k + n] = H[m][k]
    return M


kern_l = [flat(hom_gen(gen(i, j), s)) for s in ("C", "T") for (i, j) in [(0, 1), (0, 2), (1, 2)]]
rep.check("2.0c l = span of the generators of the kernel lifts actC R, actT R (R in SO(3))",
          span_rank(kern_l) == 6 and span_rank(kern_l + fl(L_)) == 6)

# ------------------------------------------------------------------ lower bound: symbolic V1 membership
s1, t1, s2, t2 = sp.symbols("s1 t1 s2 t2", real=True)


def sym_unit(s, t):
    d = 1 + s * s + t * t
    return [2 * s / d, 2 * t / d, (s * s + t * t - 1) / d]


xs, ys = sym_unit(s1, t1), sym_unit(s2, t2)
hx = [sp.Integer(1)] + xs
hy = [sp.Integer(1)] + ys
wsym = [hx[m] * hy[n] for (m, n) in IDX]
hmx = [sp.Integer(1)] + [-c for c in xs]
hmy = [sp.Integer(1)] + [-c for c in ys]


def v1_symbolic(X):
    V = [sum((sp.Rational(X[r][c].numerator, X[r][c].denominator) * wsym[c] for c in range(16) if X[r][c] != 0),
             sp.Integer(0)) for r in range(16)]
    conds = [sum(hmx[m] * V[4 * m + n] for m in range(4)) for n in range(4)]
    conds += [sum(V[4 * m + n] * hmy[n] for n in range(4)) for m in range(4)]
    return all(sp.simplify(sp.together(c)) == 0 for c in conds) and all(X[0][c] == 0 for c in range(16))


rep.check("2.1a control: every element of l satisfies V1 for all unit x, y (symbolic)", all(map(v1_symbolic, L_)))
rep.check("2.1b control: every element of M1 satisfies V1 symbolically", all(map(v1_symbolic, M1)))
rep.check("2.1c control: every element of M2 = R_B M1 R_B satisfies V1 symbolically", all(map(v1_symbolic, M2)))
rep.check("2.1d every element of N = {J_a (x) J_b on the correlation block} satisfies V1 symbolically",
          all(map(v1_symbolic, NN)))
print(f"  [lower bound done, {time.time() - t0:.1f}s]", file=sys.stderr)

# ------------------------------------------------------------------ upper bound: exact rank
NU = 240


def cond_rows(x, y):
    w = vec(prodState(x, y))
    hmx_ = [Fr(1)] + [-F(c) for c in x]
    hmy_ = [Fr(1)] + [-F(c) for c in y]
    rows = []
    for n in range(4):
        row = [Fr(0)] * NU
        for m in range(4):
            r = 4 * m + n
            if r == 0:
                continue
            for c in range(16):
                if w[c] != 0:
                    row[(r - 1) * 16 + c] += hmx_[m] * w[c]
        rows.append(row)
    for m in range(4):
        row = [Fr(0)] * NU
        for n in range(4):
            r = 4 * m + n
            if r == 0:
                continue
            for c in range(16):
                if w[c] != 0:
                    row[(r - 1) * 16 + c] += hmy_[n] * w[c]
        rows.append(row)
    return rows


pool = [unit_vector(s, t) for (s, t) in [(0, 0), (1, 0), (0, 1), (2, 0), (0, 3), (1, 1), (Fr(1, 2), 2), (3, -1),
                                         (-2, Fr(1, 3)), (Fr(2, 5), Fr(-3, 4)), (5, 7), (-1, -4)]]
pool += [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0]]
inc = IncRank(NU)
history = []
npairs = 0
for x in pool:
    for y in pool:
        for row in cond_rows(x, y):
            inc.add(row)
        npairs += 1
    history.append((npairs, inc.rank))
print("  rank history (pairs used, rank):", history)
up = NU - inc.rank
rep.note(f"upper bound: dim V1 <= {up} (rank {inc.rank} of the conditions from {npairs} rational pairs)")


def unk(X):
    return [X[r][c] for r in range(1, 16) for c in range(16)]


rows_basis = list(inc.basis.values())
basis33 = L_ + M1 + M2 + NN
rep.check("2.2a each of the 33 basis elements satisfies every finite condition used (exact)",
          all(all(sum(a * b for a, b in zip(row, unk(X))) == 0 for row in rows_basis) for X in basis33))
rep.check("2.2b lower bound = upper bound: V1 = l + M1 + M2 + N exactly, dim 33", up == 33)
print(f"  [upper bound done, {time.time() - t0:.1f}s]", file=sys.stderr)

import random
rnd = random.Random(7)
A = zeros(16, 16)
for i in range(1, 16):
    for j in range(i + 1, 16):
        v = Fr(rnd.randint(-5, 5))
        A[i][j], A[j][i] = v, -v
V1flat = fl(basis33)
rep.check("2.3 countercontrol: a generic so(15) element on the traceless part is NOT in V1",
          span_rank(V1flat + [flat(A)]) == 33 + 1)

# ------------------------------------------------------------------ compactness step: N is excluded
# (i) l-invariant symmetric bilinear forms G (G^T = G, X^T G + G X = 0 for X in l): exactly the block scalars
NG = 16 * 16
grows = []
for i in range(16):
    for j in range(i + 1, 16):
        row = [Fr(0)] * NG
        row[i * 16 + j] += 1
        row[j * 16 + i] -= 1
        grows.append(row)
for X in L_:
    for i in range(16):
        for j in range(16):
            row = [Fr(0)] * NG
            # (X^T G + G X)_{ij} = sum_k X_{ki} G_{kj} + G_{ik} X_{kj}
            for k in range(16):
                if X[k][i] != 0:
                    row[k * 16 + j] += X[k][i]
                if X[k][j] != 0:
                    row[i * 16 + k] += X[k][j]
            grows.append(row)
gi = IncRank(NG)
for r in grows:
    gi.add(r)
gns = gi.nullspace()
blk = {0: "11"}
for (m, n) in IDX:
    k = 4 * m + n
    blk[k] = "11" if (m == 0 and n == 0) else ("31" if n == 0 else ("13" if m == 0 else "33"))
block_scalars = []
for name in ("11", "31", "13", "33"):
    G = [Fr(0)] * NG
    for k in range(16):
        if blk[k] == name:
            G[k * 16 + k] = Fr(1)
    block_scalars.append(G)
rep.check("2.4a the l-invariant symmetric bilinear forms on W 3 are exactly the block scalars "
          "diag(a, b I3, b' I3, c I9): solution space of dimension 4 equal to their span",
          len(gns) == 4 and span_rank(gns + block_scalars) == 4)


def block(X, rb, cb):
    return [[X[r][c] for c in range(16) if blk[c] == cb] for r in range(16) if blk[r] == rb]


rep.check("2.4b every M1 and M2 element has zero (3,3)->(3,3) block",
          all(all(v == 0 for row in block(X, "33", "33") for v in row) for X in M1 + M2))
rep.check("2.4c every l element has an antisymmetric (3,3)->(3,3) block",
          all(block(X, "33", "33") == [[-v for v in r] for r in transpose(block(X, "33", "33"))] for X in L_))
NB = [block(X, "33", "33") for X in NN]
rep.check("2.4d every N element has a symmetric (3,3)->(3,3) block, and N -> block is injective (rank 9)",
          all(B == transpose(B) for B in NB) and span_rank([flat(B) for B in NB]) == 9)
rep.note("2.4e [written] Let H be compact with L <= H <= Aut_u(K). An H-invariant inner product exists (average); "
         "it is l-invariant, hence a block scalar G = diag(a, b, b', c) with c > 0 by 2.4a. Every X in Lie(H) is "
         "G-antisymmetric, so its (3,3)->(3,3) block is antisymmetric. Writing X = X_l + X_M1 + X_M2 + X_N (2.2b), "
         "that block is (antisymmetric, 2.4c) + 0 (2.4b) + (symmetric, 2.4d), so the N-block vanishes and X_N = 0 "
         "by injectivity. Hence Lie(H) <= l + M1 + M2.")

# ------------------------------------------------------------------ submodules of M1 + M2 and brackets
def coords(basis_flat, X):
    n = len(basis_flat)
    rows = [list(r) + [x] for r, x in zip(zip(*basis_flat), flat(X))]
    piv, R = rref(rows, n + 1)
    assert n not in piv, "not in span"
    c = [Fr(0)] * n
    for k, p in enumerate(piv):
        c[p] = R[k][n]
    return c


def module_matrices(Mb, Ls):
    return [[[c for c in coords(fl(Mb), bracket(a, b))] for b in Mb] for a in Ls]


adM1 = module_matrices(M1, L_)
adM2 = module_matrices(M2, L_)


def hom_space_dim(ad1, ad2):
    """dim of {C (9x9) : C ad1(a) = ad2(a) C for all a in l}; ad[a][b] = coords of [a, basis_b]."""
    NC = 81
    rows = []
    for k in range(len(ad1)):
        D1 = [[ad1[k][b][i] for b in range(9)] for i in range(9)]
        D2 = [[ad2[k][b][i] for b in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                row = [Fr(0)] * NC
                for t in range(9):
                    row[i * 9 + t] += D1[t][j]
                    row[t * 9 + j] -= D2[i][t]
                rows.append(row)
    return NC - rank(rows, NC)


rep.check("2.5a End_l(M1) is 1-dimensional (M1 ~ (3,3) is absolutely irreducible)", hom_space_dim(adM1, adM1) == 1)
rep.check("2.5b Hom_l(M1, M2) is 1-dimensional (spanned by phi): the l-submodules of M1 + M2 are 0, the graphs "
          "G[a:b] = {a v + b phi(v)}, and M1 + M2 [written: isotypic component (3,3) (x) R^2 with End = R]",
          hom_space_dim(adM1, adM2) == 1)
rep.check("2.5c [l, M1] <= M1, [l, M2] <= M2, [M1, M1] <= l, [M2, M2] <= l (l+M1, l+M2 are Lie algebras)",
          all(span_rank(fl(M1) + [flat(bracket(a, b))]) == 9 for a in L_ for b in M1)
          and all(span_rank(fl(M2) + [flat(bracket(a, b))]) == 9 for a in L_ for b in M2)
          and all(span_rank(fl(L_) + [flat(bracket(a, b))]) == 6 for a in M1 for b in M1)
          and all(span_rank(fl(L_) + [flat(bracket(a, b))]) == 6 for a in M2 for b in M2))
rep.check("2.5d phi = Ad(Pi_B) fixes l pointwise and phi^2 = id",
          all(matmul(matmul(PB, a), PB) == a for a in L_) and matmul(PB, PB) == eye(16))
lm12 = fl(L_ + M1 + M2)
bad = None
for ai, v in enumerate(M1):
    for bi, w in enumerate(M1):
        Cvw = madd(bracket(v, PHI[bi]), bracket(PHI[ai], w))
        if span_rank(V1flat + [flat(Cvw)]) > 33:
            bad = (ai, bi)
            break
    if bad:
        break
rep.check("2.5e some C(v,w) = [v, phi w] + [phi v, w] lies outside V1 (hence outside l + M1 + M2): for ab != 0, "
          "[a v + b phi v, a w + b phi w] = (a^2+b^2)[v,w] + ab C(v,w) leaves l + G[a:b], so no graph with "
          "ab != 0 is a subalgebra", bad is not None, f"(v,w) = M1[{bad[0]}], M1[{bad[1]}]" if bad else "")
mix = None
for v in M1:
    for w in M2:
        if span_rank(V1flat + [flat(bracket(v, w))]) > 33:
            mix = True
            break
    if mix:
        break
rep.check("2.5f some [M1, M2] lies outside V1: l + M1 + M2 is not a subalgebra", mix is True)
print(f"  [brackets done, {time.time() - t0:.1f}s]", file=sys.stderr)

span_inc = IncRank(256)
for X in L_ + M1 + M2:
    span_inc.add(flat(X))
frontier = list(L_ + M1 + M2)
while frontier and span_inc.rank < 256:
    new = []
    for a in L_ + M1 + M2:
        for b in frontier:
            Bm = bracket(a, b)
            if span_inc.add(flat(Bm)):
                new.append(Bm)
    frontier = new
rep.note(f"identification: the Lie algebra generated by l + M1 + M2 has dimension {span_inc.rank} (so(15): 105)")
print(f"  [done, {time.time() - t0:.1f}s]", file=sys.stderr)
rep.verdict("V1-CLASSIFIED: V1 = l + M1 + M2 + N (dim 33, exact); compactness removes N; the Lie algebra of every "
            "compact group H with L <= H <= Aut_u(K), K admissible, is l, l + M1 (the su(4) image) or "
            "l + M2 (its R_B conjugate)")
