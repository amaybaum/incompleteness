"""EQ4-P exploration x8 -- copy of x4 (DFS over orbit choices) with new roots: W3 + omega3, the limit ray of the x5 regress.
EXPLORATION (exact integer arithmetic, but a search: outputs are leads, re-certified elsewhere).  Research only.

Same objects as x3 (positions j = 2b + t; G of order 192; S = cone{e_j + e_k}).  A node is a set of orbit
representatives R; K_R = cone(S u G.R) must be self-positive.  ext(K_R*) is computed by exact double description.
If K_R* is self-positive then K_R = K_R* (FOUND).  Otherwise the children are the orbit representatives of extreme
rays of K_R* outside K_R whose G-orbits are self-positive; a node with none is STUCK (only extreme rays are tried, so
STUCK is not a proof that no self-dual completion exists).  Root seeds: S alone (control: the orthant must be found),
kappa = (3,-1,1,1,1,1,1,1), W3 = (-1,1,1,1,1,1,1,1).
Output: every node visited with its status.  No VERDICT line (exploration).
"""
import sys
from itertools import permutations, product
from math import gcd
from fractions import Fraction as Fr


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


def self_positive(vs):
    return all(dot(vs[i], vs[j]) >= 0 for i in range(len(vs)) for j in range(i, len(vs)))


def e(j):
    return tuple(int(k == j) for k in range(8))


S = sorted(set(tuple(a + b for a, b in zip(e(j), e(k))) for j in range(8) for k in range(8) if j != k))
visited = {}
found = []
MAXN = int(sys.argv[1]) if len(sys.argv) > 1 else 200


def node(reps, depth):
    key = tuple(sorted(reps))
    if key in visited or len(visited) >= MAXN:
        return
    gens = sorted(set(S + [w for v in key for w in orbit(v)]))
    assert self_positive(gens)
    ext = extreme_rays(gens)
    if self_positive(ext):
        visited[key] = "FOUND"
        negs = [v for v in ext if min(v) < 0]
        found.append(key)
        print("%sFOUND  reps=%s  ext(K*)=%d rays (%d with a negative entry), ext orbit reps=%s"
              % ("  " * depth, list(key), len(ext), len(negs), sorted(set(canon(v) for v in ext))), flush=True)
        return
    outside = [z for z in ext if any(dot(z, w) < 0 for w in ext)]
    reps_out = sorted(set(canon(z) for z in outside))
    good = [z for z in reps_out if all(dot(z, w) >= 0 for w in orbit(z))]
    if not good:
        visited[key] = "STUCK"
        print("%sSTUCK  reps=%s  ext(K*)=%d; outside reps %s (no self-positive orbit)"
              % ("  " * depth, list(key), len(ext), reps_out), flush=True)
        return
    visited[key] = "OPEN"
    print("%snode   reps=%s  ext(K*)=%d; children %s" % ("  " * depth, list(key), len(ext), good), flush=True)
    for z in good:
        node(list(key) + [z], depth + 1)


for name, seed in (("W3 + omega3", [(-1, 1, 1, 1, 1, 1, 1, 1), (-1, 1, 1, 1, 1, 1, 1, 3)]),
                   ("kappa + omega3", [(3, -1, 1, 1, 1, 1, 1, 1), (-1, 1, 1, 1, 1, 1, 1, 3)])):
    print("=== root:", name, flush=True)
    node([canon(v) for v in seed], 0)
print("visited %d nodes; FOUND %d: %s" % (len(visited), len(found), found))
