"""EQ4-P exploration x13 -- the c = 1 sector problem (x12): x5's greedy with NON-extreme candidates, started from
S_tw = twirl(B_tw) = G-orbits of (1,1,0,0,0,0,0,0) and (1,1,1,1,1,-1,1,-1) (x12) instead of S u G.seed.  Copy of x5:  EXPLORATION (exact integer arithmetic, but a heuristic search; outputs are leads only).  Research only.

x4 tried only extreme rays of K* as additions and got STUCK on every non-orthant branch; that proves nothing, because a
self-dual completion may need non-extreme points of K* (e.g. y = sigma.nu + c.1 is addable to cone(S u G.W3) for
c in [0.19, 0.4)).  Here, at each step, with ext = ext(K*) (exact double description) and "outside" = ext rays of K*
not in K (they pair negatively with some ext ray of K*), the candidates are y = z + c w with z an outside ray, w an
ext ray of K* inside K, c in {1/4, 1/2, 1, 2, 4}, and the H_z-twirl (stabilizer of z's negative position) of z and of
those y.  A candidate is admissible iff y is outside K and its G-orbit is self-positive (then cone(K u G.y) is
self-positive).  Choose the admissible candidate whose orbit cuts the most outside rays (pairs negatively with them);
ties broken by the smallest canonical integer vector.  Stop at FOUND (K* self-positive, so K = K*) or STUCK, or after
the step limit.  Seeds: W3 = (-1,1,1,1,1,1,1,1) or kappa = (3,-1,1,1,1,1,1,1) (argv[1]); step limit argv[2].
Output: progress lines.  No VERDICT line (exploration).
"""
import sys
import time
from fractions import Fraction as Fr
from itertools import permutations, product
from math import gcd


def prim(v):
    g = 0
    for x in v:
        g = gcd(g, abs(x))
    return tuple(x // g for x in v) if g else tuple(v)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


GR = []
for perm in permutations(range(4)):
    for eps in product((0, 1), repeat=4):
        if sum(eps) % 2 == 0:
            GR.append(tuple(2 * perm[b] + (t ^ eps[b]) for b in range(4) for t in range(2)))
assert len(set(GR)) == 192


def act(g, v):
    w = [0] * 8
    for i in range(8):
        w[g[i]] = v[i]
    return tuple(w)


def orbit(v):
    return sorted(set(act(g, v) for g in GR))


def canon(v):
    return min(orbit(v))


def rank(rows):
    if not rows:
        return 0
    M = [[Fr(x) for x in r] for r in rows]
    rk = 0
    ncol = len(M[0])
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
    assert len(basis) == n
    rays = list(inverse_cols([rows[k] for k in basis]))
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
                if all(not (r != p and r != q and (Z[r] & common) == common) for r in range(len(rays))):
                    nr.append(prim(tuple(vals[p] * rays[q][t] - vals[q] * rays[p][t] for t in range(n))))
                    nz.append(common | (1 << i))
        rays, Z = nr, nz
    return sorted(set(rays))


def e(j):
    return tuple(int(k == j) for k in range(8))


def stab_twirl(z):
    j = min(range(8), key=lambda k: (z[k], k))
    H = [g for g in GR if g[j] == j]
    acc = [0] * 8
    for g in H:
        w = act(g, z)
        for k in range(8):
            acc[k] += w[k]
    return prim(tuple(acc))


S = sorted(set(tuple(a + b for a, b in zip(e(j), e(k))) for j in range(8) for k in range(8) if j != k))
steps = int(sys.argv[1]) if len(sys.argv) > 1 else 12
STW = sorted(set(orbit((1, 1, 0, 0, 0, 0, 0, 0)) + orbit((1, 1, 1, 1, 1, -1, 1, -1))))
gens = list(STW)
reps = []
for step in range(steps):
    t0 = time.time()
    ext = extreme_rays(gens)
    outside = [z for z in ext if any(dot(z, w) < 0 for w in ext)]
    inside = [z for z in ext if z not in set(outside)]
    # prune generators to the extreme rays of K (facets of K*)
    keep = []
    for w in gens:
        tight = [z for z in ext if dot(w, z) == 0]
        if rank(tight) == 7:
            keep.append(w)
    gens = sorted(set(keep))
    print("step %d: ext(K) %d, ext(K*) %d, outside %d (orbit reps %s) [%.1fs]"
          % (step, len(gens), len(ext), len(outside), sorted(set(canon(z) for z in outside))[:4], time.time() - t0),
          flush=True)
    if not outside:
        print("FOUND: K* is self-positive, K = K*; added reps:", reps)
        print("  ext(K*) orbit reps:", sorted(set(canon(z) for z in ext)))
        break
    out_set = outside
    cands = set()
    zreps = sorted(set(canon(z) for z in outside))
    zs = [z for z in outside if canon(z) in set(zreps)]
    for z in zs:
        cands.add(prim(z))
        cands.add(stab_twirl(z))
        for w in inside:
            for num, den in ((1, 4), (1, 2), (1, 1), (2, 1), (4, 1)):
                y = prim(tuple(den * a + num * b for a, b in zip(z, w)))
                cands.add(y)
                cands.add(stab_twirl(y))
    best = None
    for y in sorted(cands):
        # y must be in K*: <y, gens> >= 0 (true for combinations of K* elements; checked anyway)
        if any(dot(y, w) < 0 for w in gens):
            continue
        # y outside K
        if not any(dot(y, z) < 0 for z in ext):
            continue
        oy = orbit(y)
        if any(dot(y, w) < 0 for w in oy):
            continue
        cut = sum(1 for z in out_set if any(dot(w, z) < 0 for w in oy))
        key = (-cut, canon(y))
        if best is None or key < best[0]:
            best = (key, y)
    if best is None:
        print("STUCK: no admissible candidate; outside reps", zreps[:6])
        break
    y = canon(best[1])
    reps.append(y)
    print("   add orbit of %s (cuts %d outside rays)" % (y, -best[0][0]), flush=True)
    gens = sorted(set(gens + orbit(y)))
else:
    print("step limit reached; reps:", reps)
