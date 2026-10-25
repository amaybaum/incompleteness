"""The computationally bounded named classes B1-B4 (PLAN.md §3), exact.

Every advantage is a Fraction; numpy is used on integer arrays only.
"""
from fractions import Fraction
from itertools import combinations

import numpy as np

from . import gf2, lc

WHT_K = 23          # B1: all T via the integer WHT for K <= 23
B3_KWISE_K = 127    # B3: k <= 3 positions for K <= 127
B3_WMAX = 16        # B3: windows of w <= 16 consecutive positions
B4_DIM_MAX = 20     # B4: exact maximum only over an annihilator space of dimension <= 20
B4_D3_EXACT_N = 24  # B4: d = 3 exact maximum only where K+1 <= 24
B4_CAP = {1: 255, 2: 255, 3: 63}


def record_keys(X, K):
    """Integer key of X_{0:K} with bit t = X_t (K <= 62)."""
    assert K <= 62
    sh = np.arange(K + 1, dtype=np.int64)
    return (X[:, :K + 1].astype(np.int64) << sh).sum(axis=1)


def wht(a):
    """In-place integer Walsh-Hadamard transform of an integer array of length 2^N (|entries| stay <= total)."""
    n = a.shape[0]
    h = 1
    while h < n:
        v = a.reshape(-1, 2 * h)
        x = v[:, :h].copy()
        y = v[:, h:]
        v[:, :h] += y
        v[:, h:] = x - y
        h *= 2
    return a


def parity_of(v):
    v = v.copy()
    out = np.zeros_like(v)
    while True:
        nz = v != 0
        if not nz.any():
            return out
        out ^= v & 1
        v >>= 1


def direct_bias(keys, w, T):
    """sum_seeds w (-1)^{T . r} for one T (direct, no transform)."""
    par = parity_of(keys & np.int64(T))
    return int((w * (1 - 2 * par)).sum())


# ---------------------------------------------------------------- B1

class B1:
    """B1 on one generator: |W(T)| for every T at K = min(23, kcap) via one WHT.

    The law at K is the marginal of the law at K' >= K on the first K+1 coordinates, so its Fourier
    coefficients are those of K' at T subset of [0, K]. IM4 checks this path against the direct
    bias at every K <= 10.
    """

    def __init__(self, law, ktop=WHT_K):
        self.law = law
        self.ktop = min(ktop, law.kcap)
        self.keys = record_keys(law.X, self.ktop)
        assert law.M < (1 << 30)
        c = np.zeros(1 << (self.ktop + 1), dtype=np.int32)
        np.add.at(c, self.keys, law.w.astype(np.int32))
        self.absW = np.abs(wht(c))

    def block_max(self):
        """bm[K] = (max |W(T)| over T with top bit K, first argmax T)."""
        out = {}
        for K in range(self.ktop + 1):
            blk = self.absW[1 << K: 1 << (K + 1)]
            i = int(np.argmax(blk))
            out[K] = (int(blk[i]), (1 << K) + i)
        return out


def b1_curve(law, b=None):
    """B1 K1 curve: exact for K <= 23 (WHT); for K > 23 the bias-+-1 lower bound, exact where the
    support is a uniformly weighted affine subspace (measured, not assumed)."""
    M = law.M
    if b is None:
        b = B1(law)
    bm = b.block_max()
    curve, exact, arg = {}, {}, {}
    best, bestT = -1, None
    for K in range(b.ktop + 1):
        v, T = bm[K]
        if v > best:
            best, bestT = v, T
        curve[K] = Fraction(best, 2 * M)
        exact[K] = True
        arg[K] = bestT
    if law.kcap > b.ktop:
        rk = affine_rank_profile(law)
        rows_int, piv = _rref_dirs([law], law.kcap)
        for K in range(b.ktop + 1, law.kcap + 1):
            T = null_test(rows_int, piv, K)
            curve[K] = bias_of_positions(law, T) if T is not None else Fraction(0)
            exact[K] = bool(rk["affine_uniform"][K])
            arg[K] = None if T is None else "T=%s" % T
    return curve, exact, arg, b


def affine_rank_profile(law):
    """Rank of the direction space of supp P_K (affine hull), for every K, from one column-ordered
    elimination; and whether the support is a uniformly weighted affine subspace at each K."""
    X = law.X
    kcap = law.kcap
    lab = law.labels[kcap]
    # unique full records (one representative row per final class)
    _, first = np.unique(lab, return_index=True)
    R = X[np.sort(first)]
    D = (R[1:] ^ R[0:1]).astype(np.uint8) if R.shape[0] > 1 else np.zeros((0, kcap + 1), dtype=np.uint8)
    rank = {}
    if D.shape[0]:
        P = gf2.pack_rows(D)
        _, piv = gf2.rref_packed(P, kcap + 1)
    else:
        piv = []
    pivs = np.array(piv, dtype=np.int64)
    affine_uniform = {}
    for K in range(kcap + 1):
        rank[K] = int((pivs <= K).sum())
        c = law.counts(K)
        affine_uniform[K] = (len(c) == (1 << rank[K])) and bool((c == c[0]).all())
    return {"rank": rank, "affine_uniform": affine_uniform}


def _rref_dirs(laws, kcap):
    rows = []
    for l in laws:
        lab = l.labels[kcap]
        _, first = np.unique(lab, return_index=True)
        R = l.X[np.sort(first)]
        if R.shape[0] > 1:
            rows.append((R[1:] ^ R[0:1]).astype(np.uint8))
    D = np.concatenate(rows, axis=0)
    Rr, piv = gf2.rref_packed(gf2.pack_rows(D), kcap + 1)
    return [gf2.packed_row_to_int(Rr[i]) for i in range(len(piv))], piv


def null_test(rows_int, piv, K):
    """A nonzero T subset of [0, K] orthogonal to every direction (or None): the first free column
    j <= K together with the pivots whose row has a 1 in column j."""
    ps = [p for p in piv if p <= K]
    pset = set(ps)
    free = next((c for c in range(K + 1) if c not in pset), None)
    if free is None:
        return None
    T = [free] + [p for i, p in enumerate(piv) if p <= K and (rows_int[i] >> free) & 1]
    return sorted(T)


def bias_of_positions(law, T):
    par = law.X[:, T].astype(np.int64).sum(axis=1) & 1
    return Fraction(abs(int((law.w * (1 - 2 * par)).sum())), 2 * law.M)


def b1_k0(laws, named_out=None):
    """B1 K0 over a family. K <= 23: exact worst (max_T min_phi) and average (max_T mean_phi).
    K > 23: T in the intersection of the annihilators of every support's direction space (a lower
    bound for both forms; worst case exact where every support is affine-uniform)."""
    F = len(laws)
    M = laws[0].M
    ktop = min(WHT_K, min(l.kcap for l in laws))
    mn = None
    sm = None
    for li, l in enumerate(laws):
        b = B1(l, ktop)
        if named_out is not None and li in named_out:
            named_out[li] = b1_curve(l, b)
        if mn is None:
            mn = b.absW.copy()
            sm = b.absW.copy()
        else:
            np.minimum(mn, b.absW, out=mn)
            sm += b.absW
        del b
    keys = [record_keys(l.X, ktop) for l in laws]
    worst, avg = {}, {}
    bw, bwT, ba, baT = -1, None, -1, None
    for K in range(ktop + 1):
        blk = mn[1 << K: 1 << (K + 1)]
        i = int(np.argmax(blk))
        if int(blk[i]) > bw:
            bw, bwT = int(blk[i]), (1 << K) + i
        blk = sm[1 << K: 1 << (K + 1)]
        i = int(np.argmax(blk))
        if int(blk[i]) > ba:
            ba, baT = int(blk[i]), (1 << K) + i
        pw = [Fraction(abs(direct_bias(keys[j], laws[j].w, bwT)), 2 * M) for j in range(F)]
        pa = [Fraction(abs(direct_bias(keys[j], laws[j].w, baT)), 2 * M) for j in range(F)]
        worst[K] = {"value": Fraction(bw, 2 * M), "exact": True, "test": "T=%d" % bwT, "per_phi": pw}
        avg[K] = {"value": Fraction(ba, 2 * M * F), "exact": True, "test": "T=%d" % baT, "per_phi": pa}
    kcap = min(l.kcap for l in laws)
    if kcap > ktop:
        profs = [affine_rank_profile(l) for l in laws]
        rows_int, piv = _rref_dirs(laws, kcap)
        for K in range(ktop + 1, kcap + 1):
            T = null_test(rows_int, piv, K)
            allx = all(p["affine_uniform"][K] for p in profs)
            if T is None:
                worst[K] = {"value": Fraction(0), "exact": bool(allx), "test": None, "per_phi": None}
                avg[K] = {"value": Fraction(0), "exact": False, "test": None, "per_phi": None}
                continue
            pp = [bias_of_positions(l, T) for l in laws]
            worst[K] = {"value": min(pp), "exact": bool(allx), "test": "T=%s" % T, "per_phi": pp}
            avg[K] = {"value": sum(pp) / F, "exact": bool(allx), "test": "T=%s" % T, "per_phi": pp}
    return worst, avg


# ---------------------------------------------------------------- B2

def lc_profiles(law):
    """LCP[seed, K] = LC(X_{0:K}) by Berlekamp-Massey on each seed's full record."""
    X = law.X
    return np.array([lc.bm_profile(X[i].tolist()) for i in range(X.shape[0])], dtype=np.int64)


def b2_tables(law, LCP=None):
    """adv_lambda(K) * M * 2^N as exact integers, for every K <= kcap and 0 <= lambda <= K+1."""
    if LCP is None:
        LCP = lc_profiles(law)
    M = law.M
    out = {}
    for K in range(law.kcap + 1):
        N = K + 1
        cnt = np.zeros(N + 1, dtype=np.int64)
        np.add.at(cnt, LCP[:, K], law.w)
        cP = np.cumsum(cnt).tolist()
        cQ = 0
        row = []
        for lam in range(N + 1):
            cQ += lc.count_closed(N, lam)
            row.append(abs(cP[lam] * (1 << N) - cQ * M))
        out[K] = row
    return out, LCP


def b2_den(M, K):
    return M << (K + 1)


def b2_k1(tab, M):
    curve, arg = {}, {}
    for K, row in tab.items():
        i = max(range(len(row)), key=lambda j: (row[j], -j))
        curve[K], arg[K] = Fraction(row[i], b2_den(M, K)), i
    return curve, arg


def b2_k0(tabs, M):
    F = len(tabs)
    worst, avg = {}, {}
    for K in range(min(max(t) for t in tabs) + 1):
        rows = [t[K] for t in tabs]
        nl = len(rows[0])
        mins = [min(r[j] for r in rows) for j in range(nl)]
        sums = [sum(r[j] for r in rows) for j in range(nl)]
        jw = max(range(nl), key=lambda j: (mins[j], -j))
        ja = max(range(nl), key=lambda j: (sums[j], -j))
        den = b2_den(M, K)
        worst[K] = {"value": Fraction(mins[jw], den), "exact": True, "test": "lambda=%d" % jw,
                    "per_phi": [Fraction(r[jw], den) for r in rows]}
        avg[K] = {"value": Fraction(sums[ja], den * F), "exact": True, "test": "lambda=%d" % ja,
                  "per_phi": [Fraction(r[ja], den) for r in rows]}
    return worst, avg


# ---------------------------------------------------------------- B3

def subset_sums(delta):
    """delta (..., k) -> (..., 2^k) with out[..., A] = sum_{z in A} delta[..., z] (A as a bitmask)."""
    out = np.zeros(delta.shape[:-1] + (1,), dtype=np.int64)
    for z in range(delta.shape[-1]):
        out = np.concatenate([out, out + delta[..., z:z + 1]], axis=-1)
    return out


def b3_kwise(laws, kcap=B3_KWISE_K):
    """B3 k-wise (k <= 3 positions, K <= 127): K1 per generator, and K0 (worst, average) over the
    list of laws, exact by enumeration of all 2^(2^k) tests on every position set.

    Values are numerators over the common denominator 8M (k-wise TV is sum_z |c 2^k - M| / (2 M 2^k)).
    Returns k1[j][K], k0w[K], k0a[K] with K the largest position allowed.
    """
    F = len(laws)
    M = laws[0].M
    for l in laws:
        assert l.M == M and (l.w == 1).all()
    K = min(kcap, min(l.kcap for l in laws))
    Xs = [l.X[:, :K + 1].astype(np.int64) for l in laws]
    S = Xs[0].shape[0]
    # per max-index j: best K1 numerator per law, best K0 worst/avg (value numerator, test)
    k1 = [[0] * (K + 1) for _ in range(F)]
    k0w = [(-1, None, None)] * (K + 1)   # (num over 8M, test, per-phi nums)
    k0a = [(-1, None, None)] * (K + 1)   # (num over 8M*F, test, per-phi nums)

    def consider(maxidx, cnts, sets, k):
        # cnts: (B, F, 2^k) counts; sets: list of B position tuples
        delta = cnts * (1 << k) - M                       # numerators over M 2^k
        scale = 1 << (3 - k)
        tv = np.abs(delta).sum(axis=2) * scale            # (B, F) numerators of 2*TV over 8M -> TV num over 16M
        # K1: TV = sum|delta| / (2 M 2^k) = (sum|delta| * 2^(3-k)) / (16 M)
        for j in range(F):
            v = int(tv[:, j].max())
            if v > k1[j][maxidx]:
                k1[j][maxidx] = v
        ss = np.abs(subset_sums(delta)) * scale           # (B, F, 2^(2^k)) |Delta| num over 8M
        mn = ss.min(axis=1)                               # (B, T)
        sm = ss.sum(axis=1)
        b, t = np.unravel_index(int(np.argmax(mn)), mn.shape)
        if int(mn[b, t]) > k0w[maxidx][0]:
            k0w[maxidx] = (int(mn[b, t]), (sets[b], int(t)), [int(x) for x in ss[b, :, t]])
        b, t = np.unravel_index(int(np.argmax(sm)), sm.shape)
        if int(sm[b, t]) > k0a[maxidx][0]:
            k0a[maxidx] = (int(sm[b, t]), (sets[b], int(t)), [int(x) for x in ss[b, :, t]])

    for j in range(K + 1):
        # k = 1: {j}
        cn = np.stack([np.stack([(1 - X[:, j]).sum(), X[:, j].sum()]) for X in Xs])[None]
        consider(j, cn, [(j,)], 1)
        # k = 2: {i, j}, i < j
        if j >= 1:
            idx = np.arange(j)
            c2 = np.zeros((j, F, 4), dtype=np.int64)
            for f, X in enumerate(Xs):
                key = 2 * X[:, :j] + X[:, j:j + 1]       # (S, j)
                flat = (np.arange(j)[None, :] * 4 + key).reshape(-1)
                c2[:, f, :] = np.bincount(flat, minlength=4 * j).reshape(j, 4)
            consider(j, c2, [(int(i), j) for i in idx], 2)
        # k = 3: {i, l, j}, i < l < j
        for l in range(1, j):
            c3 = np.zeros((l, F, 8), dtype=np.int64)
            for f, X in enumerate(Xs):
                key = 4 * X[:, :l] + 2 * X[:, l:l + 1] + X[:, j:j + 1]
                flat = (np.arange(l)[None, :] * 8 + key).reshape(-1)
                c3[:, f, :] = np.bincount(flat, minlength=8 * l).reshape(l, 8)
            consider(j, c3, [(int(i), l, j) for i in range(l)], 3)
    # cumulative maxima over max index <= K
    out1 = []
    for f in range(F):
        best = 0
        cur = {}
        for kk in range(K + 1):
            best = max(best, k1[f][kk])
            cur[kk] = Fraction(best, 16 * M)
        out1.append(cur)
    w_out, a_out = {}, {}
    bw = (-1, None, None)
    ba = (-1, None, None)
    for kk in range(K + 1):
        if k0w[kk][0] > bw[0]:
            bw = k0w[kk]
        if k0a[kk][0] > ba[0]:
            ba = k0a[kk]
        w_out[kk] = {"value": Fraction(bw[0], 8 * M), "exact": True, "test": "S=%s,A=%d" % (list(bw[1][0]), bw[1][1]),
                     "per_phi": [Fraction(x, 8 * M) for x in bw[2]]}
        a_out[kk] = {"value": Fraction(ba[0], 8 * M * F), "exact": True, "test": "S=%s,A=%d" % (list(ba[1][0]), ba[1][1]),
                     "per_phi": [Fraction(x, 8 * M) for x in ba[2]]}
    return out1, w_out, a_out


def b3_window_k1(law, wmax=B3_WMAX):
    """B3 windows: exact marginal TV maximised over windows of w <= 16 consecutive positions inside
    [0, K], for every K <= kcap. Values over the common denominator 2 M 2^16."""
    X = law.X.astype(np.int64)
    S, L = X.shape
    M = law.M
    assert (law.w == 1).all()
    best_end = [0] * L  # best numerator among windows ending at index e
    arg_end = [None] * L
    key = np.zeros((S, L), dtype=np.int64)
    for w in range(1, wmax + 1):
        if w > L:
            break
        # key[:, s] for window [s, s+w-1]
        key = key[:, :L - w + 1] + (X[:, w - 1:] << (w - 1))
        twow = 1 << w
        scale = 1 << (wmax - w)
        for s in range(L - w + 1):
            _, cnt = np.unique(key[:, s], return_counts=True)
            num = (int(np.abs(cnt * twow - M).sum()) + (twow - len(cnt)) * M) * scale
            e = s + w - 1
            if num > best_end[e]:
                best_end[e] = num
                arg_end[e] = (s, w)
    curve, arg = {}, {}
    best, ba = 0, None
    for K in range(L):
        if best_end[K] > best:
            best, ba = best_end[K], arg_end[K]
        curve[K] = Fraction(best, 2 * M * (1 << wmax))
        arg[K] = ba
    return curve, arg


# ---------------------------------------------------------------- B4

def monomials(N, d):
    out = [()]
    for k in range(1, d + 1):
        out.extend(combinations(range(N), k))
    return out


def eval_matrix(R, mons):
    """R: (s, N) uint8 support records; returns (s, len(mons)) uint8 monomial evaluations."""
    s = R.shape[0]
    E = np.empty((s, len(mons)), dtype=np.uint8)
    for j, mo in enumerate(mons):
        if not mo:
            E[:, j] = 1
        elif len(mo) == 1:
            E[:, j] = R[:, mo[0]]
        elif len(mo) == 2:
            E[:, j] = R[:, mo[0]] & R[:, mo[1]]
        else:
            E[:, j] = R[:, mo[0]] & R[:, mo[1]] & R[:, mo[2]]
    return E


def n_monomials(N, d):
    from math import comb
    return sum(comb(N, i) for i in range(d + 1))


def _row_order(s):
    # a fixed pseudo-random row order (rank is order-independent; it only speeds early stopping)
    return np.argsort((np.arange(s, dtype=np.int64) * 2654435761) % 4294967311, kind="stable")


def annihilator_space(R, N, d, need_basis):
    """Annihilators of degree <= d of the point set R (s x N). Returns (dim, basis or None).

    dim = #monomials - rank of the evaluation matrix. Counting certifies existence when
    #monomials > s; the basis is computed only when need_basis and dim <= B4_DIM_MAX.
    """
    nm = n_monomials(N, d)
    s = R.shape[0]
    if nm > s + B4_DIM_MAX:
        return None, None  # dim >= nm - s > 20: exact dimension not needed
    mons = monomials(N, d)
    order = _row_order(s)
    # chunked elimination with early stop at full column rank
    rank = 0
    chunk = max(2 * nm, 256)
    Rr = R[order]
    P_all = None
    piv = []
    start = 0
    while start < s:
        E = eval_matrix(Rr[start:start + chunk], mons)
        P = gf2.pack_rows(E)
        P_all = P if P_all is None else np.concatenate([P_all, P], axis=0)
        Rref, piv = gf2.rref_packed(P_all, nm)
        P_all = Rref
        rank = len(piv)
        start += chunk
        if rank == nm:
            break
    dim = nm - rank
    basis = None
    if need_basis and 0 < dim <= B4_DIM_MAX:
        basis = gf2.nullspace_from_rref(P_all, piv, nm)
    return dim, (basis, mons)


def exists_annihilator(R, N, d):
    nm = n_monomials(N, d)
    if nm > R.shape[0]:
        return True, None
    dim, _ = annihilator_space(R, N, d, need_basis=False)
    return dim > 0, dim


def support_records(law, K):
    lab = law.labels[K]
    _, first = np.unique(lab, return_index=True)
    return law.X[np.sort(first), :K + 1]


def union_records(laws, K):
    X = np.concatenate([l.X[:, :K + 1] for l in laws], axis=0)
    return np.unique(X, axis=0)


# --- weights of quadratics by Dickson reduction (exact Walsh sum) ---

_PAIRPOS = {}


def _pair_tables(mons, N):
    key = (N, len(mons))
    if key not in _PAIRPOS:
        lin_end = 1 + N
        pairs = [mo for mo in mons[lin_end:] if len(mo) == 2]
        _PAIRPOS[key] = (lin_end, pairs)
    return _PAIRPOS[key]


def quad_from_coeffs(c, mons, N):
    """Decode a coefficient vector (monomial order: 1, x_0..x_{N-1}, then pairs) into (const, lin, adj)."""
    lin_end, pairs = _pair_tables(mons, N)
    const = c & 1
    lin = (c >> 1) & ((1 << N) - 1)
    adj = [0] * N
    v = c >> lin_end
    j = 0
    while v:
        if v & 1:
            a, b = pairs[j]
            adj[a] ^= 1 << b
            adj[b] ^= 1 << a
        v >>= 1
        j += 1
    return const, lin, adj


def walsh_sum_quadratic(const, lin, adj, N):
    """S = sum_x (-1)^q(x) for q = sum_{i<j} Q_ij x_i x_j + lin.x + const, by Dickson reduction:
    summing out x_i against its linear form L_i gives 2 [L_i = 0]; solving L_i = 0 for a partner x_j
    and substituting keeps q quadratic in two fewer variables."""
    adj = list(adj)
    active = (1 << N) - 1
    factor = 0
    while True:
        i = -1
        for k in range(N):
            if (active >> k) & 1 and adj[k] & active:
                i = k
                break
        if i < 0:
            break
        Li = adj[i] & active
        j = (Li & -Li).bit_length() - 1
        A = Li & ~(1 << j)               # x_j = sum_{m in A} x_m + l_i  (on L_i = 0)
        ac = (lin >> i) & 1
        Bj = adj[j] & active & ~(1 << i)
        lj = (lin >> j) & 1
        # remove x_i, x_j from the form
        rm = (1 << i) | (1 << j)
        active &= ~rm
        for k in range(N):
            adj[k] &= ~rm
        adj[i] = 0
        adj[j] = 0
        lin &= ~rm
        # substitute x_j := A.x + ac into x_j * Bj(x) + lj x_j
        m = A
        while m:
            t = m & -m
            k = t.bit_length() - 1
            adj[k] ^= Bj & ~t
            m ^= t
        m = Bj
        while m:
            t = m & -m
            k = t.bit_length() - 1
            adj[k] ^= A & ~t
            m ^= t
        lin ^= A & Bj
        if ac:
            lin ^= Bj
        if lj:
            lin ^= A
            const ^= ac
        factor += 1
    if lin & active:
        return 0
    nact = bin(active).count("1")
    return (1 << (factor + nact)) * (-1 if const else 1)


def weight_quadratic(c, mons, N):
    if c >> (N + 1) == 0:          # affine: Dickson rank 0
        lin = c >> 1
        return (1 << (N - 1)) if lin else (c & 1) << N
    const, lin, adj = quad_from_coeffs(c, mons, N)
    S = walsh_sum_quadratic(const, lin, adj, N)
    return ((1 << N) - S) // 2


def weights_by_histogram(basis, mons, N):
    """Weights of every element of span(basis), by enumeration of all 2^N points (N <= 24): the
    Moebius transform of the packed ANF gives each point's evaluation vector; a histogram and a WHT
    give every combination's weight. Returns an int64 array indexed by the combination bitmask."""
    k = len(basis)
    assert N <= 24 and k <= 31
    A = np.zeros(1 << N, dtype=np.int64)
    for bi, c in enumerate(basis):
        j = 0
        v = c
        while v:
            if v & 1:
                mask = 0
                for x in mons[j]:
                    mask |= 1 << x
                A[mask] ^= 1 << bi
            v >>= 1
            j += 1
    for b in range(N):
        v = A.reshape(-1, 2, 1 << b)
        v[:, 1, :] ^= v[:, 0, :]
    H = np.bincount(A, minlength=1 << k).astype(np.int64)
    W = wht(H)
    return ((1 << N) - W) // 2


def gray_combos(basis):
    """All nonzero combinations of the basis in Gray-code order: yields (mask, coeffs)."""
    k = len(basis)
    cur = 0
    mask = 0
    for g in range(1, 1 << k):
        b = (g & -g).bit_length() - 1
        cur ^= basis[b]
        mask ^= 1 << b
        yield mask, cur


def span_ints(basis):
    """All 2^k combinations of int64-representable basis vectors, indexed by combination mask."""
    v = np.zeros(1, dtype=np.int64)
    for b in basis:
        v = np.concatenate([v, v ^ np.int64(b)])
    return v


def max_weight(basis, mons, N, d, method):
    """Maximum weight over the nonzero elements of span(basis).

    dickson: every element is reduced to Dickson's normal form (walsh_sum_quadratic); for an affine
    element (no quadratic part, the rank-0 case) the reduction ends at once: weight 2^(N-1) if the
    linear part is nonzero, else 2^N * const. histogram: enumeration of all 2^N points."""
    if method == "dickson":
        assert d <= 2
        if d == 1 and len(mons) <= 62:
            c = span_ints(basis)[1:]
            lin = c >> 1
            w = np.where(lin != 0, 1 << (N - 1), (c & 1) << N)
            return int(w.max())
        best = -1
        for _, c in gray_combos(basis):
            w = weight_quadratic(c, mons, N)
            if w > best:
                best = w
        return best
    W = weights_by_histogram(basis, mons, N)
    W[0] = -1
    return int(W.max())


def b4_curve(R_of_K, kcap, d, M_unused=None):
    """B4 at degree d. R_of_K(K) -> support point set at K. Returns per-K records:
    {'exists': bool, 'dim': int|None, 'value': Fraction, 'exact': bool} and K_first.

    The least K with an annihilator is found by binary search (existence is monotone in K); the
    exact maximum of wt(q)/2^N is computed where the space has dimension <= 20 (d <= 2: Dickson;
    d = 3: only where K+1 <= 24, by enumeration); elsewhere the certified bound 2^-d is reported.
    """
    cap = min(kcap, B4_CAP[d])

    def ex(K):
        return exists_annihilator(R_of_K(K), K + 1, d)[0]

    lo, hi = 0, cap
    if not ex(cap):
        kfirst = None
    else:
        while lo < hi:
            mid = (lo + hi) // 2
            if ex(mid):
                hi = mid
            else:
                lo = mid + 1
        kfirst = lo
    out = {}
    band_open = True
    for K in range(cap + 1):
        N = K + 1
        if kfirst is None or K < kfirst:
            out[K] = {"exists": False, "dim": 0, "value": Fraction(0), "exact": True}
            continue
        rec = {"exists": True, "dim": None, "value": Fraction(1, 1 << d), "exact": False, "method": "bound"}
        if band_open:
            dim, bm = annihilator_space(R_of_K(K), N, d, need_basis=True)
            if dim is None or dim > B4_DIM_MAX:
                band_open = False  # dimension is non-decreasing in K
            else:
                rec["dim"] = dim
                basis, mons = bm
                if d <= 2:
                    mw = max_weight(basis, mons, N, d, "dickson")
                    rec.update(value=Fraction(mw, 1 << N), exact=True, method="dickson")
                elif N <= B4_D3_EXACT_N:
                    mw = max_weight(basis, mons, N, d, "histogram")
                    rec.update(value=Fraction(mw, 1 << N), exact=True, method="enumeration")
        out[K] = rec
    return out, kfirst


def b4_counting_horizon(n, d):
    """Least K with sum_{i<=d} C(K+1, i) > 2^{n+1} (annihilator for every generator by counting)."""
    K = 0
    while n_monomials(K + 1, d) <= (1 << (n + 1)):
        K += 1
    return K
