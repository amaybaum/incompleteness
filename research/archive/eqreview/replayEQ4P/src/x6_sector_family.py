"""EQ4-P exploration x6 -- sector problem SP (see x3-x5): a two-parameter family of candidate cones.
EXPLORATION (exact integer arithmetic; a scan; outputs are leads only).  Research only.

Written observation (NOTES): an element of S* with two zero entries is nonnegative, so for a non-orthant G-invariant
self-dual K the two-position faces are K n V_{i,i'} = cone{(1, t), (t, 1)} (partner positions) and
K n V_{i,p} = cone{(1, s), (s, 1)} (different fibres), with t = 1/m_t, s = 1/m_s, where m_t (m_s) is the least
partner (other-fibre) entry of a normalized negative element (entry -1) of K.  Candidate:
  K(m_t, m_s) = cone{ m_t e_i + e_i' , m_s e_i + e_p , rho_i }  (i' = partner of i, p in another fibre),
  rho_i = G-orbit of (-1, m_t, m_s, m_s, m_s, m_s, m_s, m_s).
Scan rational m_t, m_s >= 1 with m_t <= 3 m_s^2 (orbit self-positivity of rho).  For each: self-positivity of the
generators (exact), ext(K*) by exact double description, K* self-positive (iff K = K*).
Output: one line per grid point.  No VERDICT line (exploration).
"""
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


def gens(mt, ms):
    den = mt.denominator * ms.denominator
    a, b = int(mt * den), int(ms * den)          # m_t, m_s scaled by den
    out = []
    for i in range(8):
        ip = i ^ 1
        v = [0] * 8
        v[i], v[ip] = a, den
        out.append(prim(tuple(v)))
        for p in range(8):
            if p // 2 != i // 2:
                v = [0] * 8
                v[i], v[p] = b, den
                out.append(prim(tuple(v)))
    rho = prim(tuple([-den, a] + [b] * 6))
    out += orbit(rho)
    return sorted(set(out))


vals = [Fr(1), Fr(5, 4), Fr(3, 2), Fr(2), Fr(5, 2), Fr(3), Fr(4), Fr(6)]
for ms in vals:
    for mt in vals + [Fr(8), Fr(12)]:
        if mt > 3 * ms * ms:
            continue
        W = gens(mt, ms)
        sp = all(dot(W[i], W[j]) >= 0 for i in range(len(W)) for j in range(i, len(W)))
        if not sp:
            print("m_t=%s m_s=%s: generators not self-positive" % (mt, ms), flush=True)
            continue
        ext = extreme_rays(W)
        outside = [z for z in ext if any(dot(z, w) < 0 for w in ext)]
        print("m_t=%s m_s=%s: ext(K*) %d, outside %d %s" % (mt, ms, len(ext), len(outside),
              sorted(set(canon(z) for z in outside))[:3]), flush=True)
