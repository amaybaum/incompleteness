"""EQ4-P exploration x3 -- the GHZ-diagonal sector problem.  EXPLORATION (exact integer arithmetic, but a search:
its outputs are leads; anything claimed is re-certified in a probe with its own decision rule).  Research only.

Question.  Sector problem SP: in the GHZ-basis eigenvalue coordinates lambda in R^8 (positions j = 2b + t, fibre
b = 0..3, t = 0 for GHZ+, 1 for GHZ-; trace pairing = Euclidean), is the orthant R^8_+ the only closed convex cone K with
  (1) K invariant under G = S_4 on fibres x even numbers of within-fibre swaps (order 192),
  (3) K = K* (Euclidean),
  (4) S <= K <= S*, S = cone{e_j + e_k : j != k}?
(Filter invariance (2) is checked separately, only for a lead.)  If SP had the orthant as its only solution, the
GHZ-diagonal section of every admissible K3 would contain GHZ+, and E3 would give IE2; so SP decides whether the
sector route can close the wall.

Method.  Greedy self-dualization by orbits: K = cone(S u G.v_1 u ... ), checked self-positive; ext(K*) by an exact
double-description method (integer rays, combinatorial adjacency test); K = K* iff ext(K*) is pairwise nonnegative
(K <= K* and K* <= K** = K iff K* is self-positive).  If not, add the G-orbit of an extreme ray z of K* outside K whose
orbit is self-positive (<z, g z> >= 0 for all g), and repeat.  Controls: K = R^8_+ gives K* = K; K = S gives a
non-self-positive S*.
Output: progress lines and, if found, the orbit representatives of a self-dual K.  No VERDICT line (exploration).
"""
import sys
import time
from itertools import permutations, product
from math import gcd


def prim(v):
    g = 0
    for x in v:
        g = gcd(g, abs(x))
    return tuple(x // g for x in v) if g else tuple(v)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def group():
    els = []
    for perm in permutations(range(4)):
        for eps in product((0, 1), repeat=4):
            if sum(eps) % 2:
                continue
            m = [0] * 8
            for b in range(4):
                for t in range(2):
                    m[2 * b + t] = 2 * perm[b] + (t ^ eps[b])
            els.append(tuple(m))
    return els


GR = group()
assert len(set(GR)) == 192


def act(g, v):
    w = [0] * 8
    for i in range(8):
        w[g[i]] = v[i]
    return tuple(w)


def orbit(v):
    return sorted(set(act(g, v) for g in GR))


def rank(rows):
    from fractions import Fraction as Fr
    M = [[Fr(x) for x in r] for r in rows]
    rk = 0
    ncol = len(M[0]) if M else 0
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c] / M[rk][c]
                M[i] = [M[i][j] - f * M[rk][j] for j in range(ncol)]
        rk += 1
    return rk


def inverse_cols(B):
    """columns of B^{-1} as primitive integer vectors (B square, integer, invertible)."""
    from fractions import Fraction as Fr
    n = len(B)
    M = [[Fr(x) for x in B[i]] + [Fr(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[c][j] for j in range(2 * n)]
    inv = [row[n:] for row in M]
    cols = []
    for j in range(n):
        col = [inv[i][j] for i in range(n)]
        den = 1
        for x in col:
            den = den * x.denominator // gcd(den, x.denominator)
        cols.append(prim(tuple(int(x * den) for x in col)))
    return cols


def extreme_rays(A, n=8):
    rows = [tuple(a) for a in A]
    basis = []
    for i, a in enumerate(rows):
        if rank([rows[k] for k in basis] + [a]) > len(basis):
            basis.append(i)
        if len(basis) == n:
            break
    assert len(basis) == n, "constraints do not span"
    cols = inverse_cols([rows[k] for k in basis])
    rays = list(cols)
    Z = []
    for j in range(n):
        mask = 0
        for k in range(n):
            if k != j:
                mask |= 1 << basis[k]
        Z.append(mask)
    bset = set(basis)
    for i, a in enumerate(rows):
        if i in bset:
            continue
        vals = [dot(a, r) for r in rays]
        pos = [k for k in range(len(rays)) if vals[k] > 0]
        neg = [k for k in range(len(rays)) if vals[k] < 0]
        zer = [k for k in range(len(rays)) if vals[k] == 0]
        nr = [rays[k] for k in pos] + [rays[k] for k in zer]
        nz = [Z[k] for k in pos] + [Z[k] | (1 << i) for k in zer]
        for p in pos:
            for q in neg:
                common = Z[p] & Z[q]
                if common.bit_count() < n - 2:
                    continue
                ok = True
                for r in range(len(rays)):
                    if r != p and r != q and (Z[r] & common) == common:
                        ok = False
                        break
                if ok:
                    w = prim(tuple(vals[p] * rays[q][t] - vals[q] * rays[p][t] for t in range(n)))
                    nr.append(w)
                    nz.append(common | (1 << i))
        rays, Z = nr, nz
    return sorted(set(rays))


def self_positive(vs):
    for i in range(len(vs)):
        for j in range(i, len(vs)):
            if dot(vs[i], vs[j]) < 0:
                return False, (vs[i], vs[j])
    return True, None


def e(j):
    return tuple(int(k == j) for k in range(8))


S = sorted(set(tuple(a + b for a, b in zip(e(j), e(k))) for j in range(8) for k in range(8) if j != k))
OPLUS = [e(j) for j in range(8)]

# controls
r = extreme_rays(OPLUS)
print("control R8+: ext(K*) = %d rays, self-positive %s" % (len(r), self_positive(r)[0]), flush=True)
r = extreme_rays(S)
print("control S: ext(S*) = %d rays, self-positive %s" % (len(r), self_positive(r)[0]), flush=True)

start = sys.argv[1] if len(sys.argv) > 1 else "kappa"
seeds = {"kappa": [(3, -1, 1, 1, 1, 1, 1, 1)], "w3": [(-1, 1, 1, 1, 1, 1, 1, 1)],
         "both": [(3, -1, 1, 1, 1, 1, 1, 1), (-1, 1, 1, 1, 1, 1, 1, 1)]}[start]
gens = list(S)
reps = []
for v in seeds:
    gens += orbit(v)
    reps.append(v)
gens = sorted(set(gens))
for step in range(40):
    sp_ok, bad = self_positive(gens)
    assert sp_ok, ("generators not self-positive", bad)
    t0 = time.time()
    ext = extreme_rays(gens)
    sp_dual, badd = self_positive(ext)
    print("step %d: %d generators (reps %s), ext(K*) %d rays, K* self-positive %s  [%.1fs]"
          % (step, len(gens), reps, len(ext), sp_dual, time.time() - t0), flush=True)
    if sp_dual:
        print("FOUND self-dual K: reps", reps)
        neg = [v for v in ext if min(v) < 0]
        print("  ext rays with a negative entry:", len(neg), " orbit reps of ext:",
              sorted(set(min(orbit(v)) for v in ext)))
        break
    # candidates: ext rays of K* not in K, with self-positive orbit
    outside = [z for z in ext if any(dot(z, w) < 0 for w in ext)]
    reps_out = sorted(set(min(orbit(z)) for z in outside))
    good = []
    for z in reps_out:
        oz = orbit(z)
        if all(dot(z, w) >= 0 for w in oz):
            good.append(z)
    print("   outside-K ext orbit reps: %d; with self-positive orbit: %d  %s" % (len(reps_out), len(good), good[:6]),
          flush=True)
    if not good:
        print("STUCK: no extreme ray of K* outside K has a self-positive orbit")
        print("  outside reps:", reps_out[:12])
        break
    z = good[0]
    reps.append(z)
    gens = sorted(set(gens + orbit(z)))
