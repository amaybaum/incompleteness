"""Exact window simulator for record-writing invasive observation on the leap substratum.

The state is the exact joint distribution over (configuration of the window |i| <= a around site 0, record
string so far), with every site outside the window uniform and independent of everything else.  Exactness:
  * initially the state is the uniform product measure (window radius 0);
  * a leap from window radius a to radius a' <= a+1 enumerates the uniform sites of the ring
    a < |i| <= a'+1 explicitly (all their (u, v) values, equal weight) and keeps only |i| <= a';
    every site beyond stays uniform and independent (the new v_i = F(..) + u_i is masked by the uniform u_i);
  * sites dropped at |i| > a' never influence a later reading at site 0, because a' >= the number of
    leaps remaining (causal cone, RegionTower.iterate_dependsOnlyOn_ball), so marginalizing them is exact.
Counts are integers; the total mass is 4 * 4^(number of enumerated sites); probabilities = counts / mass.

Steps: 'o' read v_0 -> record b -> disturb pair by kappa_b -> leap;  'm' the same with the record forgotten;
'i' leap;  'f' flip v_0;  's' swap (u_0, v_0);  'p' passive read then leap (kappa = identity; controls).
kappa = (k0, k1): k_b is a tuple (img of u=0, img of u=1), images are pair codes p = u + 2 v.
"""
import numpy as np

PASSIVE = ((0, 1), (2, 3))      # (u, b) -> (u, b): code u + 2b


def F_bits(l, c, r, rule):
    if rule == 'linear':
        return l ^ r
    if rule == 'nonlinear':
        return (l & r) ^ c
    if rule == 'majority':
        return (l & r) | (l & c) | (r & c)
    raise ValueError(rule)


class State:
    def __init__(self):
        self.a = 0
        self.P = np.ones((4, 1), dtype=object)   # window radius 0: pair (u0, v0) uniform; one empty record
        self.mass_log4 = 1                         # total mass = 4^mass_log4

    # ---- configuration encoding: site k = i + a, u at bit 2k, v at bit 2k+1
    def bits(self, idx, a):
        n = 2 * a + 1
        u = [(idx >> (2 * k)) & 1 for k in range(n)]
        v = [(idx >> (2 * k + 1)) & 1 for k in range(n)]
        return u, v

    def leap(self, a_new, rule):
        a = self.a
        R = a_new + 1                              # region needed: v up to a_new+1, u up to a_new
        extra = [i for i in range(-R, R + 1) if abs(i) > a]
        nold = 1 << (2 * (2 * a + 1))
        idx = np.arange(nold, dtype=np.int64)
        u_old = {i: (idx >> (2 * (i + a))) & 1 for i in range(-a, a + 1)}
        v_old = {i: (idx >> (2 * (i + a) + 1)) & 1 for i in range(-a, a + 1)}
        nnew = 1 << (2 * (2 * a_new + 1))
        Pn = np.zeros((nnew, self.P.shape[1]), dtype=object)
        for combo in range(1 << (2 * len(extra))):
            u = dict(u_old)
            v = dict(v_old)
            for j, i in enumerate(extra):
                u[i] = np.full(nold, (combo >> (2 * j)) & 1, dtype=np.int64)
                v[i] = np.full(nold, (combo >> (2 * j + 1)) & 1, dtype=np.int64)
            new = np.zeros(nold, dtype=np.int64)
            for i in range(-a_new, a_new + 1):
                nu = v[i]
                nv = F_bits(v[i - 1], v[i], v[i + 1], rule) ^ u[i]
                k = i + a_new
                new |= (nu << (2 * k)) | (nv << (2 * k + 1))
            np.add.at(Pn, new, self.P)
        self.P = Pn
        self.a = a_new
        self.mass_log4 += len(extra)

    def pair_map(self, fn, record):
        """Apply a map on the site-0 pair; fn(p) -> (new pair, recorded bit or None)."""
        a = self.a
        n = self.P.shape[0]
        idx = np.arange(n, dtype=np.int64)
        sh = 2 * a
        p = (idx >> sh) & 3
        cleared = idx & ~(np.int64(3) << sh)
        newp = np.zeros(n, dtype=np.int64)
        bit = np.zeros(n, dtype=np.int64)
        for q in range(4):
            np_, b = fn(q)
            newp[p == q] = np_
            bit[p == q] = 0 if b is None else b
        newidx = cleared | (newp << sh)
        if record:
            nrec = self.P.shape[1]
            Pn = np.zeros((n, 2 * nrec), dtype=object)
            for b in (0, 1):
                sel = bit == b
                np.add.at(Pn[:, b::2], newidx[sel], self.P[sel])   # new record = 2*rec + b
            self.P = Pn
        else:
            Pn = np.zeros_like(self.P)
            np.add.at(Pn, newidx, self.P)
            self.P = Pn


def kappa_fn(kappa):
    def fn(q):
        u, b = q & 1, q >> 1
        return kappa[b][u], b
    return fn


def run(protocol, rule, kappa):
    """Joint record distribution of a protocol: (integer counts per record string, total mass)."""
    T = sum(1 for s in protocol if s in 'oimp')
    st = State()
    left = T
    for s in protocol:
        if s in 'om':
            st.pair_map(kappa_fn(kappa), record=(s == 'o'))
        elif s == 'p':
            st.pair_map(kappa_fn(PASSIVE), record=True)
        elif s == 'f':
            st.pair_map(lambda q: (q ^ 2, None), record=False)
        elif s == 's':
            st.pair_map(lambda q: (((q & 1) << 1) | (q >> 1), None), record=False)
        if s in 'oimp':
            left -= 1
            st.leap(min(st.a + 1, left), rule)
    counts = [int(x) for x in st.P.sum(axis=0)]
    return counts, 4 ** st.mass_log4
