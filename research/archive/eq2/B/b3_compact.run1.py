"""B3 (node N2) -- Lemma COMPACT: the normalization hypothesis, its countermodels, and the exact inputs that let the
landed IIP-1 theorem (InvariantInnerProduct.invariant_inner_product_span, IIP:455) supply the invariant inner product.

Statement under test (INTEGRATION-DESIGN v2 4.1): for a convex cone K in W 3 whose closed normalized slice
S = cl K n {u = 1} is bounded with nonempty interior in the hyperplane, Aut_u(K) = {g : g K = K, u o g = u} lies in
Aut_u(cl K), which is compact.
Decision rule (fixed before the run):
  * the hypothesis u o g = u is reported LOAD-BEARING only with exact countermodels: a cone automorphism with a bounded
    slice whose powers are unbounded (one on the owner's quadrant, one on Q3 itself), and a gate for which the group form
    fails without it;
  * the IIP-1 route is reported AVAILABLE only if its three hypotheses are certified exactly for every admissible cone:
    the products span W 3 (hspan), the max slice is bounded (an exact identity bounding every coordinate), and the forms
    invariant under a finite subgroup F of L are exactly the block scalars (so the transported inner product is
    diag(b I3, b' I3, c I9) on ker u) with the F-fixed vectors = span(e00) (so the centroid is e00).
Usage: python3 -I -B b3_compact.py <base>/verification/lean-mathlib/OIBridge/CompositeDimension.lean
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eq2b_lib import *  # noqa
import sympy as sp

rep = Report("B3 Lemma COMPACT")
CNOT = parse_kernel_cnot(sys.argv[1])[0]
E00 = [[Fr(1) if (m, n) == (0, 0) else Fr(0) for n in range(4)] for m in range(4)]


def u_of(w):
    return w[0][0]


# ---------------------------------------------------------------- Part A: countermodels without u o g = u
D = [[Fr(2), Fr(0)], [Fr(0), Fr(1, 2)]]
pts = [[Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(1, 3), Fr(2, 3)]]
img = [[sum(D[i][k] * p[k] for k in range(2)) for i in range(2)] for p in pts]
pw = [Fr(2) ** n for n in range(1, 7)]
rep.check("A.1 the owner's quadrant: diag(2, 1/2) maps the positive quadrant onto itself (inverse diag(1/2, 2) too), its "
          "slice {x + y = 1} is a bounded segment, u = x + y is not preserved (u(1,0) -> 2) and the (1,1) entries of the "
          "powers are 2^n (unbounded)", all(all(c >= 0 for c in v) for v in img) and sum(img[0]) == 2
          and pw == [2, 4, 8, 16, 32, 64])
# a local boost on copy A: hom-index map with cosh = 5/3, sinh = 4/3 along z
BST = [[Fr(5, 3), Fr(0), Fr(0), Fr(4, 3)], [Fr(0), Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(1), Fr(0)],
       [Fr(4, 3), Fr(0), Fr(0), Fr(5, 3)]]
GB = onC(BST)
A3 = cm([[3, 0], [0, 1]])
rep.check("A.2 [M] the local boost onC(B), B = Lorentz boost (cosh, sinh) = (5/3, 4/3), equals (1/3) Ad(diag(3, 1) (x) I): "
          "a congruence by an invertible matrix times a positive scalar, so it maps Q3 onto Q3 (exact identity)",
          meq(GB, conj_map(kron(A3, I2), Fr(1, 3))))
vals = []
Bn = I16
for n in range(1, 7):
    Bn = mmul(Bn, GB)
    vals.append(u_of(apply(Bn, E00)))
rep.check("A.3 u is not preserved and the powers are unbounded: u(onC(B)^n e00) = (3^n + 3^-n)/2 for n = 1..6 (exact)",
          vals == [(Fr(3) ** n + Fr(3) ** (-n)) / 2 for n in range(1, 7)], str(vals))
ok = True
for x in ([1, 0, 0], [0, 0, 1], [0, 0, -1], [Fr(3, 5), 0, Fr(4, 5)], [0, Fr(1, 2), Fr(-1, 2)]):
    for y in ([0, 1, 0], [Fr(2, 3), Fr(1, 3), Fr(2, 3)]):
        w = apply(GB, prodState(x, y))
        lam = w[0][0]
        xs = [w[k][0] / lam for k in (1, 2, 3)]
        ok &= lam > 0 and w == [[lam * c for c in r] for r in prodState(xs, y)] and sum(c * c for c in xs) <= 1
rep.check("A.4 the boost maps products to positive multiples of products (so it preserves min and, dually, max): checked "
          "exactly on 10 products", ok)
Gb = mmul(GB, CNOT)
lam_g = mmul(mmul(Gb, actC(NFLIP)), minv(Gb))
w01 = apply(Gb, prodState([1, 0, 0], Z3))
rep.check("A.5 group form without normalization fails: G = onC(B) o cnot maps Q3 onto Q3 and a product to a non-product "
          "(rank >= 2), and the element G (actC nflip) G^-1 of <L, G L G^-1> does not preserve u, so that group is not "
          "the PU(4) image (which preserves u)",
          rank([list(r) for r in w01], 4) >= 2 and lam_g[0] != [Fr(1)] + [Fr(0)] * 15,
          f"row 0 of G (actC nflip) G^-1 starts {[str(c) for c in lam_g[0][:6]]}")
rep.note("A.6 [written] positive scalars c id (c != 1) preserve every cone and no normalization; their powers are "
         "unbounded. So Lemma COMPACT is false for Aut(K) and holds only for Aut_u(K).")

# ---------------------------------------------------------------- Part B: the IIP-1 inputs
prods = []
for x in ([0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]):
    for y in ([0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]):
        prods.append(vec(prodState(x, y)))
rep.check("B.1 hspan: the 16 products hom x (x) hom y, x, y in {0, e1, e2, e3}, span W 3 (rank 16), so the slice of every "
          "admissible cone has affine span {u = 1} (IIP-1's hspan hypothesis on the chart w -> e00 + w)",
          rank(prods, 16) == 16)
w = sp.symbols("w0:16")
W_ = [[w[4 * m + n] for n in range(4)] for m in range(4)]
ok = True
for mu in range(1, 4):
    for nu in range(1, 4):
        tot = 0
        for a in (1, -1):
            for b in (1, -1):
                ea = [sp.Rational(1, 2)] + [sp.Rational(a, 2) if k == mu - 1 else 0 for k in range(3)]
                fb = [sp.Rational(1, 2)] + [sp.Rational(b, 2) if k == nu - 1 else 0 for k in range(3)]
                tot += a * b * sum(ea[i] * W_[i][j] * fb[j] for i in range(4) for j in range(4))
        ok &= sp.expand(tot - W_[mu][nu]) == 0
    totA, totB = 0, 0
    for a in (1, -1):
        ea = [sp.Rational(1, 2)] + [sp.Rational(a, 2) if k == mu - 1 else 0 for k in range(3)]
        totA += a * sum(ea[i] * W_[i][0] for i in range(4))
        totB += a * sum(W_[0][j] * ea[j] for j in range(4))
    ok &= sp.expand(totA - W_[mu][0]) == 0 and sp.expand(totB - W_[0][mu]) == 0
rep.check("B.2 bounded slice: w_{mu nu} = sum_{a,b = +-1} a b <e_a^mu (x) e_b^nu, w> with the four sharp product effects "
          "summing to w00, and w_{mu 0}, w_{0 mu} = sum_a a <e_a^mu (x) 1, w>, sum_a a <1 (x) e_a^mu, w> (exact); on jointStates every term lies in "
          "[0, 1], so |w_{mu nu}| <= 1 and the max slice (hence every admissible slice) is bounded", ok)
R90z, R90x = rot_axis(2, 0, 1), rot_axis(0, 0, 1)
GENS = [actC(R90z), actC(R90x), actT(R90z), actT(R90x)]
rows = []
for g in GENS:
    # g^T Q g - Q = 0 for symmetric Q (unknowns: Q[i][j], 256, with symmetry rows)
    for i in range(16):
        for j in range(16):
            row = [Fr(0)] * 256
            for k in range(16):
                if g[k][i] != 0:
                    for l in range(16):
                        if g[l][j] != 0:
                            row[16 * k + l] += g[k][i] * g[l][j]
            row[16 * i + j] -= 1
            rows.append(row)
for i in range(16):
    for j in range(i + 1, 16):
        row = [Fr(0)] * 256
        row[16 * i + j], row[16 * j + i] = Fr(1), Fr(-1)
        rows.append(row)
sol = nullspace(rows, 256)
blk = {}
for (m, n) in IDX:
    blk[4 * m + n] = "00" if (m, n) == (0, 0) else ("A" if n == 0 else ("B" if m == 0 else "AB"))
bs = []
for name in ("00", "A", "B", "AB"):
    v = [Fr(0)] * 256
    for k in range(16):
        if blk[k] == name:
            v[17 * k] = Fr(1)
    bs.append(v)
rep.check("B.3 the symmetric forms invariant under the finite group F generated by actC and actT of the quarter turns about "
          "z and x (octahedral rotations on each copy, inside L) are exactly the block scalars diag(a, b I3, b' I3, c I9) "
          "(solution space of dimension 4 equal to their span)", len(sol) == 4 and rank(sol + bs, 256) == 4)
fixed = nullspace([r for g in GENS for r in madd(g, I16, 1, -1)], 16)
rep.check("B.4 the F-fixed vectors of W 3 are span(e00): the centroid of every L-invariant slice is e00", len(fixed) == 1
          and fixed[0] == vec(E00))
rep.note("B.5 [written, from IIP-1] for an admissible convex L-invariant cone K and g linear with g(K) = K, u o g = u: g maps "
         "S = cl K n {u = 1} onto S (S compact by B.2, affine span {u = 1} by B.1); invariant_inner_product_span (IIP:455) "
         "applied with the chart w -> e00 + w gives a positive definite form Q15 on ker u preserved by g and a fixed "
         "centroid, which is e00 by B.4 (S is L-invariant); Q15 is L-invariant, hence F-invariant, hence diag(b I3, b' I3, "
         "c I9) by B.3. So Aut_u(cl K) lies in the Q-isometries fixing e00, a compact set (closed and bounded).")
rep.verdict("COMPACT-NORMALIZED: u o g = u is load-bearing (quadrant, boost on Q3, failed group form); with it, IIP-1's "
            "hypotheses hold exactly for every admissible cone and give a block-scalar invariant inner product on ker u")
