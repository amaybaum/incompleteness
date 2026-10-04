"""Same exact window simulator as record_sim.py, re-implemented for speed only:
  * int64 counts instead of Python objects (total mass <= 4^(window sites) stays far below 2^62 here);
  * prefix sharing: protocols with the same total number of leaps T have identical states on a common prefix
    (the leap radius min(a+1, leaps left) depends only on the prefix and T), so a trie is walked depth first.
Output is checked equal to record_sim.run on every protocol of the validation sets (validate_fast.py).
"""
import numpy as np
from record_sim import F_bits, PASSIVE

LEAPS = 'oimp'


class St:
    __slots__ = ('a', 'P', 'm')

    def __init__(self, a, P, m):
        self.a, self.P, self.m = a, P, m


def initial():
    return St(0, np.ones((4, 1), dtype=np.int64), 1)


def leap(st, a_new, rule):
    a = st.a
    R = a_new + 1
    extra = [i for i in range(-R, R + 1) if abs(i) > a]
    nold = 1 << (2 * (2 * a + 1))
    idx = np.arange(nold, dtype=np.int64)
    u_old = {i: (idx >> (2 * (i + a))) & 1 for i in range(-a, a + 1)}
    v_old = {i: (idx >> (2 * (i + a) + 1)) & 1 for i in range(-a, a + 1)}
    nnew = 1 << (2 * (2 * a_new + 1))
    Pn = np.zeros((nnew, st.P.shape[1]), dtype=np.int64)
    for combo in range(1 << (2 * len(extra))):
        u = dict(u_old)
        v = dict(v_old)
        for j, i in enumerate(extra):
            u[i] = (combo >> (2 * j)) & 1
            v[i] = (combo >> (2 * j + 1)) & 1
        new = np.zeros(nold, dtype=np.int64)
        for i in range(-a_new, a_new + 1):
            nu = v[i]
            nv = F_bits(v[i - 1], v[i], v[i + 1], rule) ^ u[i]
            k = i + a_new
            new |= (np.int64(1) * nu << (2 * k)) | (np.int64(1) * nv << (2 * k + 1))
        np.add.at(Pn, new, st.P)
    return St(a_new, Pn, st.m + len(extra))


def pair_map(st, fn, record):
    a = st.a
    n = st.P.shape[0]
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
    nrec = st.P.shape[1]
    if record:
        Pn = np.zeros((n, 2 * nrec), dtype=np.int64)
        for b in (0, 1):
            sel = bit == b
            sub = np.zeros((n, nrec), dtype=np.int64)
            np.add.at(sub, newidx[sel], st.P[sel])
            Pn[:, b::2] = sub
    else:
        Pn = np.zeros((n, nrec), dtype=np.int64)
        np.add.at(Pn, newidx, st.P)
    return St(a, Pn, st.m)


def kfn(kappa):
    return lambda q: (kappa[q >> 1][q & 1], q >> 1)


def step(st, s, rule, kappa, left_after):
    if s in 'om':
        st = pair_map(st, kfn(kappa), s == 'o')
    elif s == 'p':
        st = pair_map(st, kfn(PASSIVE), True)
    elif s == 'f':
        st = pair_map(st, lambda q: (q ^ 2, None), False)
    elif s == 's':
        st = pair_map(st, lambda q: (((q & 1) << 1) | (q >> 1), None), False)
    if s in LEAPS:
        st = leap(st, min(st.a + 1, left_after), rule)
    return st


def run_all(protocols, rule, kappa):
    """dict protocol -> (counts per record string, total mass); identical to record_sim.run per protocol."""
    out = {}
    groups = {}
    for pr in set(protocols):
        groups.setdefault(sum(1 for s in pr if s in LEAPS), []).append(pr)
    for T, prs in groups.items():
        trie = {}
        for pr in prs:
            node = trie
            for s in pr:
                node = node.setdefault(s, {})
            node[None] = pr

        def walk(node, st, left):
            if None in node:
                out[node[None]] = ([int(x) for x in st.P.sum(axis=0)], 4 ** st.m)
            for s, ch in node.items():
                if s is None:
                    continue
                la = left - (1 if s in LEAPS else 0)
                walk(ch, step(st, s, rule, kappa, la), la)
        walk(trie, initial(), T)
    return out
