"""P3 (nodes N3, N4a) -- automorphism Lie algebras of the minimal and maximal tensor cones of two balls, and the
normalizer of the local group inside the admissible maps.

Part A (min, max).  Every linear automorphism of min maps extreme rays to extreme rays; the extreme rays of min are
the pure products r(x,y) = hom x (x) hom y (|x| = |y| = 1), a smooth 4-manifold of rays.  So X in Lie(Aut(min))
satisfies  X r(x,y) in T(x,y) := span{ r(x,y), (0,u) (x) hom y, hom x (x) (0,v) : u _|_ x, v _|_ y }.
Upper bound: exact rank of these conditions at rational pairs.  Lower bound: local Lorentz generators (rotations and
boosts on each factor) and the identity, checked symbolically.
max = min* (Euclidean pairing), so Lie(Aut(max)) = { -Y^T : Y in Lie(Aut(min)) } and normalization u o X = 0 for
X = -Y^T is Y e00 = 0.

Part B (normalizer).  The commutant of l in gl(16) is the block scalars (exact).  A block scalar
D = diag(1, cA I3, cB I3, cAB I9) with D and D^{-1} mapping pure products into maxCone is local:
cA, cB in {+-1}, cAB = cA cB (exact corner analysis).

Decision rule (fixed before the run): dims are reported only when lower bound = upper bound; the min/max verdict
is rendered only if, in addition, the normalization-preserving subalgebras are l (dimension 6, equal span).
Usage: python3 -I p3_minmax_normalizer.py
"""
import sys
import os
import time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eqclib import *  # noqa
import sympy as sp

t0 = time.time()
rep = Report("P3 min/max automorphisms and normalizer")


def lor_gens():
    """so(3,1) generators on homogeneous coordinates (4x4): 3 rotations, 3 boosts."""
    out = []
    for (i, j) in [(1, 2), (1, 3), (2, 3)]:
        J = zeros(4, 4)
        J[i][j], J[j][i] = Fr(1), Fr(-1)
        out.append(J)
    for k in (1, 2, 3):
        K = zeros(4, 4)
        K[0][k], K[k][0] = Fr(1), Fr(1)
        out.append(K)
    return out


def lift(H, side):
    M = zeros(16, 16)
    for (m, n) in IDX:
        for k in range(4):
            if side == "T" and H[n][k] != 0:
                M[4 * m + n][4 * m + k] = H[n][k]
            if side == "C" and H[m][k] != 0:
                M[4 * m + n][4 * k + n] = H[m][k]
    return M


LOR = [lift(H, "C") for H in lor_gens()] + [lift(H, "T") for H in lor_gens()] + [eye(16)]
rep.check("A.0 the local Lorentz generators and the identity span 13 dimensions", span_rank([flat(X) for X in LOR]) == 13)

rep.note("A.0b [written] the 13 generators lie in Lie(Aut(min)): exp of each is a local cone automorphism "
         "g_A (x) g_B with g in R_{>0} x SO(3,1)^+, which maps pure products to pure products, so min to min")


# exact (rational) tangency conditions
def perp_basis(x):
    """two rational vectors spanning x^perp (x a nonzero rational vector)."""
    cands = []
    for e in ([1, 0, 0], [0, 1, 0], [0, 0, 1]):
        c = [x[1] * e[2] - x[2] * e[1], x[2] * e[0] - x[0] * e[2], x[0] * e[1] - x[1] * e[0]]
        if any(v != 0 for v in c):
            cands.append([F(v) for v in c])
    out = []
    for c in cands:
        if span_rank(out + [c]) > len(out):
            out.append(c)
        if len(out) == 2:
            break
    return out


def tangent_space(x, y):
    hx_, hy_ = hom(x), hom(y)
    vs = [vec([[hx_[m] * hy_[n] for n in range(4)] for m in range(4)])]
    for u in perp_basis(x):
        hu = [Fr(0)] + u
        vs.append(vec([[hu[m] * hy_[n] for n in range(4)] for m in range(4)]))
    for v in perp_basis(y):
        hv = [Fr(0)] + v
        vs.append(vec([[hx_[m] * hv[n] for n in range(4)] for m in range(4)]))
    return vs


def annihilator(vs):
    inc = IncRank(16)
    for v in vs:
        inc.add(v)
    return inc.nullspace()


def tangent_rows(x, y, NUk=256):
    w = vec(prodState(x, y))
    rows = []
    for f in annihilator(tangent_space(x, y)):
        row = [Fr(0)] * NUk
        for r in range(16):
            if f[r] != 0:
                for c in range(16):
                    if w[c] != 0:
                        row[r * 16 + c] += f[r] * w[c]
        rows.append(row)
    return rows


pool = [unit_vector(s, t) for (s, t) in [(0, 0), (1, 0), (0, 1), (2, 0), (0, 3), (1, 1), (Fr(1, 2), 2), (3, -1),
                                         (-2, Fr(1, 3)), (Fr(2, 5), Fr(-3, 4))]]
inc = IncRank(256)
hist = []
cnt = 0
for x in pool:
    for y in pool:
        for row in tangent_rows(x, y):
            inc.add(row)
        cnt += 1
    hist.append((cnt, inc.rank))
print("  rank history:", hist)
up = 256 - inc.rank
rep.note(f"upper bound: dim Lie(Aut(min)) <= {up}")
rows_b = list(inc.basis.values())
rep.check("A.1 the 13 lower-bound generators satisfy every tangency condition used (exact)",
          all(all(sum(a * b for a, b in zip(row, flat(X))) == 0 for row in rows_b) for X in LOR))
rep.check("A.2 lower bound = upper bound: dim Lie(Aut(min)) = 13 (local Lorentz + scaling)", up == 13)
ns = inc.nullspace()
# normalization-preserving: u o X = 0 (row 0 of X vanishes)
def sub_with(conds):
    """basis of { X in span(ns) : extra linear conditions } via exact elimination on coefficients."""
    k = len(ns)
    rows = []
    for cond in conds:
        rows.append([cond(ns[i]) for i in range(k)])
    inc2 = IncRank(k)
    for r in rows:
        inc2.add(r)
    coeffs = inc2.nullspace()
    out = []
    for c in coeffs:
        v = [sum(c[i] * ns[i][j] for i in range(k)) for j in range(256)]
        out.append(v)
    return out


L_ = [ad_herm(SIG2[(i, 0)]) for i in (1, 2, 3)] + [ad_herm(SIG2[(0, j)]) for j in (1, 2, 3)]
lflat = [flat(X) for X in L_]
normpres = sub_with([lambda v, c=c: v[0 * 16 + c] for c in range(16)])
rep.check("A.3 Lie(Aut_u(min)) = {X in Lie(Aut(min)) : u o X = 0} = l (dimension 6, equal span)",
          len(normpres) == 6 and span_rank(normpres + lflat) == 6)
fixe00 = sub_with([lambda v, r=r: v[r * 16 + 0] for r in range(16)])
rep.check("A.4 {Y in Lie(Aut(min)) : Y e00 = 0} = l, hence Lie(Aut_u(max)) = -l^T = l",
          len(fixe00) == 6 and span_rank(fixe00 + lflat) == 6 and all(X == [[-v for v in r] for r in transpose(X)] for X in L_))
rep.note("A.5 [written] Aut_u(min)_0 = Aut_u(max)_0 = L (connected Lie subgroups with Lie algebra l). SWAP is not in L: "
         "SWAP(prodState e1 e2) = prodState e2 e1 and SWAP(prodState e1 e3) = prodState e3 e1 would force R e1 = e2 and "
         "R e1 = e3 for the control rotation R.  dim Aut(min) = dim Aut(max) = 13 < 16, so neither cone is "
         "homogeneous (no transitive action on the 16-dimensional interior).")
e1, e2, e3 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
rep.check("A.5b SWAP maps prodState e1 e2 to prodState e2 e1 and prodState e1 e3 to prodState e3 e1 (exact)",
          apply(SWAP16, prodState(e1, e2)) == prodState(e2, e1) and apply(SWAP16, prodState(e1, e3)) == prodState(e3, e1))
print(f"  [part A done, {time.time() - t0:.1f}s]", file=sys.stderr)

# ------------------------------------------------------------------ Part B: normalizer
# commutant of l in gl(16)
crow = []
for X in L_:
    for i in range(16):
        for j in range(16):
            row = [Fr(0)] * 256
            for k in range(16):
                if X[k][j] != 0:
                    row[i * 16 + k] += X[k][j]   # (Y X)_{ij} = sum_k Y_ik X_kj
                if X[i][k] != 0:
                    row[k * 16 + j] -= X[i][k]   # (X Y)_{ij}
            crow.append(row)
ci = IncRank(256)
for r in crow:
    ci.add(r)
comm = ci.nullspace()
blk = {}
for (m, n) in IDX:
    blk[4 * m + n] = "11" if (m == 0 and n == 0) else ("31" if n == 0 else ("13" if m == 0 else "33"))
bs = []
for name in ("11", "31", "13", "33"):
    v = [Fr(0)] * 256
    for k in range(16):
        if blk[k] == name:
            v[k * 16 + k] = Fr(1)
    bs.append(v)
rep.check("B.1 the commutant of l in gl(16) is exactly the block scalars (dimension 4)",
          len(comm) == 4 and span_rank(comm + bs) == 4)
# admissible block scalars: D = diag(1, cA, cB, cAB) and D^{-1} map pure products into maxCone.
# On prodState x y and product effect (1,a)(x)(1,b) the value is 1 + cA s + cB t + cAB s t with s = a.x, t = b.y
# ranging over [-1,1]^2 independently; bilinear, so nonnegativity <=> the four corners.
cA, cB, cAB = sp.symbols("cA cB cAB", real=True)
corner = lambda a, b, c, s, t: 1 + a * s + b * t + c * s * t  # noqa
pairs_ = {"cA": [((1, 1), (1, -1)), ((-1, 1), (-1, -1))], "cB": [((1, 1), (-1, 1)), ((1, -1), (-1, -1))],
          "cAB": [((1, 1), (-1, -1)), ((1, -1), (-1, 1))]}
want = {"cA": [2 + 2 * cA, 2 - 2 * cA], "cB": [2 + 2 * cB, 2 - 2 * cB], "cAB": [2 + 2 * cAB, 2 - 2 * cAB]}
ok = all([sp.expand(corner(cA, cB, cAB, *p1) + corner(cA, cB, cAB, *p2)) for (p1, p2) in pairs_[k]] == want[k]
         for k in pairs_)
rep.check("B.2 pairs of corners sum to 2 +- 2cA, 2 +- 2cB, 2 +- 2cAB, so |cA|, |cB|, |cAB| <= 1 for D; the same "
          "identities for D^{-1} = diag(1, 1/cA, 1/cB, 1/cAB) give |1/c| <= 1; hence |cA| = |cB| = |cAB| = 1", ok)
surv = []
for a in (1, -1):
    for b in (1, -1):
        for c in (1, -1):
            ok = all(corner(a, b, c, s, t) >= 0 for s in (1, -1) for t in (1, -1))
            if ok:
                surv.append((a, b, c))
rep.check("B.3 among cA, cB, cAB in {+-1} exactly the four sign patterns with cAB = cA cB pass (D = D^{-1})",
          sorted(surv) == sorted([(a, b, a * b) for a in (1, -1) for b in (1, -1)]))
ok = True
for (a, b, c) in surv:
    D = zeros(16, 16)
    for k in range(16):
        D[k][k] = {"11": Fr(1), "31": Fr(a), "13": Fr(b), "33": Fr(c)}[blk[k]]
    ok &= D == matmul(actC_mat(diag3(a, a, a)), actT_mat(diag3(b, b, b)))
rep.check("B.4 each surviving D is local: D = actC(cA I) actT(cB I)", ok)
rep.note("B.5 [written] If G is normalization-preserving, normalizes L and G, G^{-1} map products into maxCone, then "
         "conjugation by G is an automorphism of L = SO(3) x SO(3), inner or inner after the factor exchange; so "
         "G = l0 D or G = SWAP l0 D with l0 in L and D in the commutant (B.1), and D is local (B.2-B.4). Such G "
         "maps products to products. Hence an admissible gate that maps some product to a non-product (any "
         "CtrlGate with Entangling, any non-local continuous interaction) does not normalize L.")
rep.verdict("MINMAX-AND-NORMALIZER-EXACT: Lie(Aut(min)) and Lie(Aut(max)) have dimension 13 and their "
            "normalization-preserving parts are l; the admissible normalizer of L is local O(3)^2 x {1, SWAP}")
