"""Observer classes P^emb(m) (PLAN.md §3) and the composite bijection on C_V' x C_H.

An observer is (rho_0, rho_1, a, F) with rho_x a permutation of {0,1}^m, a: {0,1}^m -> {0,1}, and
F a set of cells (v, x). Memory starts at v_0 = 0^m, output at 0. Each round t < K applies
v <- rho_x(v); x <- x XOR a(v); (x, h) <- phi(x, h). At K: out <- out XOR 1[(v_K, x_K) in F].

Enumerated subclasses:
  * all observers with m <= 2 (16 at m = 1, 9216 at m = 2), every F;
  * passive observers with m = 3 up to simultaneous conjugacy fixing v_0, in the canonical form
    given by BFS labelling of the component reachable from v_0;
  * linear-filter observers rho_x(v) = A v XOR x b, A in GL(m, 2), m <= 4 (see LINEAR_A_PASSIVE).
"""
from itertools import permutations

import numpy as np

from . import gf2


class ObsSet:
    """A vectorized observer set: R[o, x, v] = rho_x(v), Aact[o, v] = a(v), pair[o] = id of (rho_0, rho_1)."""

    def __init__(self, name, m, R, Aact, pair, labels=None, passive=None):
        self.name = name
        self.m = m
        self.V = 1 << m
        self.R = np.ascontiguousarray(R, dtype=np.int64)
        self.Aact = np.ascontiguousarray(Aact, dtype=np.int64)
        self.pair = np.asarray(pair, dtype=np.int64)
        self.n = self.R.shape[0]
        self.labels = labels
        self.passive = (self.Aact == 0).all(axis=1) if passive is None else passive

    def subset(self, mask, name):
        idx = np.flatnonzero(mask)
        return ObsSet(name, self.m, self.R[idx], self.Aact[idx], self.pair[idx],
                      None if self.labels is None else [self.labels[i] for i in idx])

    def tables(self, o):
        """Explicit tables of observer o: (rho_0, rho_1, a) as lists."""
        return [self.R[o, 0].tolist(), self.R[o, 1].tolist(), self.Aact[o].tolist()]

    def pair_tables(self):
        """Unique (rho_0, rho_1) pairs: (P, 2, V) array indexed by pair id."""
        ids, first = np.unique(self.pair, return_index=True)
        out = np.zeros((int(ids.max()) + 1, 2, self.V), dtype=np.int64)
        out[ids] = self.R[first]
        return out


def all_observers(m):
    """Every observer with memory m (m <= 2): rho_0, rho_1 in Sym(2^m), a in {0,1}^(2^m)."""
    V = 1 << m
    perms = list(permutations(range(V)))
    P = len(perms)
    nA = 1 << V
    R = np.zeros((P * P * nA, 2, V), dtype=np.int64)
    Aact = np.zeros((P * P * nA, V), dtype=np.int64)
    pair = np.zeros(P * P * nA, dtype=np.int64)
    o = 0
    for i0, r0 in enumerate(perms):
        for i1, r1 in enumerate(perms):
            for a in range(nA):
                R[o, 0] = r0
                R[o, 1] = r1
                Aact[o] = [(a >> v) & 1 for v in range(V)]
                pair[o] = i0 * P + i1
                o += 1
    return ObsSet("emb_m%d_all" % m, m, R, Aact, pair)


def hall_subgroup_counts(kmax):
    """Number of subgroups of index k in the free group of rank 2 (Hall 1949), k = 1..kmax:
    a_k = k (k!) - sum_{j<k} (k-j)! a_j. Equals the number of transitive pointed permutation pairs
    on k points up to relabelling, i.e. of canonical BFS-labelled pairs with k reachable states."""
    from math import factorial
    a = {}
    for k in range(1, kmax + 1):
        a[k] = k * factorial(k) - sum(factorial(k - j) * a[j] for j in range(1, k))
    return a


def canonical_passive(kmax=8):
    """All pairs (rho_0, rho_1) of permutations of a k-point set, k <= kmax, reachable from 0 and in
    canonical BFS labelling: scanning (state, letter) in order, each undefined image is an earlier
    state not yet hit by that letter or the next new label. Each conjugacy class (fixing v_0) of the
    reachable component is generated exactly once."""
    out = []
    r = [[-1] * kmax, [-1] * kmax]
    used = [[False] * kmax, [False] * kmax]

    def rec(pos, k):
        # pos enumerates (state, letter) = divmod(pos, 2)
        s, x = divmod(pos, 2)
        if s == k:
            out.append((k, [r[0][:k], r[1][:k]]))
            return
        for t in range(k):
            if not used[x][t]:
                r[x][s] = t
                used[x][t] = True
                rec(pos + 1, k)
                used[x][t] = False
                r[x][s] = -1
        if k < kmax:
            t = k
            r[x][s] = t
            used[x][t] = True
            rec(pos + 1, k + 1)
            used[x][t] = False
            r[x][s] = -1

    rec(0, 1)
    return out


def passive_m3():
    """The passive m = 3 subclass: canonical forms with k <= 8 reachable states, padded to 8 states by
    the identity on unreachable states (which never carry mass)."""
    forms = canonical_passive(8)
    n = len(forms)
    R = np.zeros((n, 2, 8), dtype=np.int64)
    ks = np.zeros(n, dtype=np.int64)
    for o, (k, (r0, r1)) in enumerate(forms):
        R[o, 0, :] = np.arange(8)
        R[o, 1, :] = np.arange(8)
        R[o, 0, :k] = r0
        R[o, 1, :k] = r1
        ks[o] = k
    obs = ObsSet("emb_m3_passive", 3, R, np.zeros((n, 8), dtype=np.int64), np.arange(n))
    obs.k = ks
    return obs


# ---------------------------------------------------------------- linear filters

# PLAN.md §3 defines linear-filter observers by rho_x(v) = A v XOR x b and does not state a.
# This implementation reads them as passive (a = 0). The reading is PENDING an amendment (see
# pending.py, item LF-A); runs in result mode refuse to start until it is recorded.
LINEAR_A_PASSIVE = True


def gl_matrices(m):
    """All A in GL(m, 2) as tuples of column bitmasks (A e_j = col[j])."""
    out = []
    for cols in np.ndindex(*([1 << m] * m)):
        if gf2.rank_int_rows(list(cols)) == m:
            out.append(tuple(int(c) for c in cols))
    return out


def apply_cols(cols, v):
    r = 0
    j = 0
    while v:
        if v & 1:
            r ^= cols[j]
        v >>= 1
        j += 1
    return r


def krylov_class(cols, b, m):
    """(r, g): dimension of span{b, Ab, ...} and the minimal polynomial g of b under A (g(0) = 1)."""
    vecs = []
    v = b
    basis = {}
    # express each new A^r b in the basis of earlier ones
    coords = []
    while True:
        # reduce v against basis, tracking combination
        w, comb = v, 0
        for h in sorted(basis, reverse=True):
            if (w >> h) & 1:
                w ^= basis[h][0]
                comb ^= basis[h][1]
        if w == 0:
            r = len(vecs)
            # A^r b = sum_{i in comb} A^i b  => g(z) = z^r + sum comb_i z^i
            g = (1 << r) | comb
            return r, g
        idx = len(vecs)
        basis[w.bit_length() - 1] = (w, comb ^ (1 << idx))
        vecs.append(v)
        v = apply_cols(cols, v)


def companion_obs(g, m):
    """Representative of class (r, g): companion(g) on the first r coordinates, identity elsewhere, b = e_0."""
    r = gf2.deg(g) if g else 0
    V = 1 << m
    cols = []
    for j in range(m):
        if j < r - 1:
            cols.append(1 << (j + 1))
        elif j == r - 1:
            cols.append(g & ((1 << r) - 1))
        else:
            cols.append(1 << j)
    b = 1 if r >= 1 else 0
    return tuple(cols), b


def linear_tables(cols, b, m):
    V = 1 << m
    t0 = [apply_cols(cols, v) for v in range(V)]
    t1 = [t ^ b for t in t0]
    return t0, t1


def linear_classes(m):
    """Behavioural classes of linear filters with memory m: b = 0, and every g of degree 1..m with
    g(0) = 1. Returns list of (key, cols, b)."""
    out = [("r0", tuple(1 << j for j in range(m)), 0)]
    for r in range(1, m + 1):
        for low in range(1 << (r - 1)):
            g = (1 << r) | (low << 1) | 1
            cols, b = companion_obs(g, m)
            out.append(("g=%s" % gf2.poly_str(g), cols, b))
    return out


def linear_obsset(m, full=False):
    """Linear filters with memory m: the class representatives (full=False) or every (A, b)."""
    V = 1 << m
    if full:
        items = []
        for cols in gl_matrices(m):
            for b in range(V):
                items.append((cols, b))
    else:
        items = [(c, b) for _, c, b in linear_classes(m)]
    n = len(items)
    R = np.zeros((n, 2, V), dtype=np.int64)
    keys = []
    for o, (cols, b) in enumerate(items):
        t0, t1 = linear_tables(cols, b, m)
        R[o, 0] = t0
        R[o, 1] = t1
        r, g = krylov_class(cols, b, m) if b else (0, 1)
        keys.append("r0" if b == 0 else "g=%s" % gf2.poly_str(g))
    obs = ObsSet("linfilt_m%d%s" % (m, "_full" if full else ""), m, R, np.zeros((n, V), dtype=np.int64),
                 np.arange(n), labels=keys)
    obs.items = items
    return obs


def linear_prediction_masks(m):
    """Linear prediction tests chi(v) = c.v XOR e, as truth tables over v (bitmask over V)."""
    V = 1 << m
    out = []
    for c in range(1 << m):
        for e in (0, 1):
            t = 0
            for v in range(V):
                if (gf2.parity(c & v) ^ e):
                    t |= 1 << v
            out.append(t)
    return out
