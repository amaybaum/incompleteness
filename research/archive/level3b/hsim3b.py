"""Level 3B hidden-law enumerator: exact record distributions under a non-product initial measure.

The sealed window simulator (record_sim.py) is exact because the uniform product measure is invariant under the
leap, so sites outside the window are always uniform and independent. Under H_1 (v^0 a Markov chain) or H_2
(u^0 = v^0) this fails, so this simulator never enumerates fresh sites: it materializes the full dependence cone
of site 0 at the first leap and only shrinks it afterwards.

State with `left` leaps remaining: the joint distribution over (u on |i| <= left-1, v on |i| <= left) and the
record string. A leap v' = F(v_{i-1}, v_i, v_{i+1}) ^ u_i on |i| <= left-1, u' = v on |i| <= left-1 maps it to
the state for left-1 (cone shrinks by one; nothing is enumerated). Pair maps act on (u_0, v_0) as in record_sim.
Before the first leap the state is the initial measure with the site-0 pair permuted by the non-leap letters so
far; it is materialized at the first leap (or at the end, for protocols with no leap).

Initial measures (integer weights; total mass a power of two for every T, so analysis3.analyze's common
denominator applies):
  H0  u^0, v^0 uniform and independent                       weight 1
  H1  v^0 stationary Markov, P(v_{i+1} = v_i) = 3/4; u^0 uniform  weight 3^(#equal adjacent v-pairs)
  H2  u^0 = v^0, v^0 uniform                                 weight 1 on u^0 = v^0, 0 otherwise
On H0 this simulator must agree with record3_sim.run3 (normalized counts) -- the built-in control.

Bit layout of a state index with radii (a_u, a_v): u_i at bit (i + a_u) for |i| <= a_u, then v_i at bit
(2 a_u + 1) + (i + a_v) for |i| <= a_v.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
for sub in ('record', 'level3'):
    p = os.path.join(HERE, '..', sub)
    if p not in sys.path:
        sys.path.insert(0, p)
import rules3b                                   # noqa: E402,F401  (installs the extended F_bits)
from record_sim import F_bits as _unused         # noqa: E402,F401
import record_sim                                # noqa: E402
from record3_sim import c_perm                   # noqa: E402
from record_sim import PASSIVE, kappa_fn         # noqa: E402

LEAPS = 'oimp'
NONLEAP = 'fsc'


def perm_of(letter):
    if letter == 'f':
        return lambda q: q ^ 2
    if letter == 's':
        return lambda q: ((q & 1) << 1) | (q >> 1)
    if letter == 'c':
        return c_perm
    raise ValueError(letter)


class HState:
    __slots__ = ('au', 'av', 'idx', 'w', 'rec', 'nrec')
    # idx: int64 array of state indices (bit layout above); w: int64 weights; rec: int64 record strings per row
    # (rows may repeat an idx with different rec); nrec: number of record bits so far

    def __init__(self, au, av, idx, w, rec, nrec):
        self.au, self.av, self.idx, self.w, self.rec, self.nrec = au, av, idx, w, rec, nrec


def initial_cone(T, H):
    """Materialize the initial measure on the cone needed for T leaps: u on |i| <= max(T-1, 0), v on |i| <= T."""
    au, av = max(T - 1, 0), T
    nu, nv = 2 * au + 1, 2 * av + 1
    if H == 'H2':
        # u^0 = v^0: enumerate v on |i| <= av, set u_i = v_i on |i| <= au
        vidx = np.arange(1 << nv, dtype=np.int64)
        u = np.zeros_like(vidx)
        for i in range(-au, au + 1):
            u |= ((vidx >> (i + av)) & 1) << (i + au)
        idx = u | (vidx << nu)
        w = np.ones_like(idx)
    else:
        idx = np.arange(1 << (nu + nv), dtype=np.int64)
        if H == 'H0':
            w = np.ones_like(idx)
        elif H == 'H1':
            v = idx >> nu
            same = np.zeros_like(idx)
            for i in range(-av, av):
                same += 1 - (((v >> (i + av)) ^ (v >> (i + 1 + av))) & 1)
            w = np.int64(3) ** same
        else:
            raise ValueError(H)
    return HState(au, av, idx, w, np.zeros_like(idx), 0)


def site0(st):
    """pair code p = u_0 + 2 v_0 of every row."""
    u0 = (st.idx >> st.au) & 1
    v0 = (st.idx >> (2 * st.au + 1 + st.av)) & 1
    return u0 | (v0 << 1)


def set_site0(st, p):
    nu = 2 * st.au + 1
    mask = ~((np.int64(1) << st.au) | (np.int64(1) << (nu + st.av)))
    return (st.idx & mask) | ((p & 1) << st.au) | ((p >> 1) << (nu + st.av))


def pair_map(st, fn, record):
    p = site0(st)
    newp = np.zeros_like(p)
    bit = np.zeros_like(p)
    for q in range(4):
        np_, b = fn(q)
        sel = p == q
        newp[sel] = np_
        bit[sel] = 0 if b is None else b
    idx = set_site0(st, newp)
    rec = st.rec
    nrec = st.nrec
    if record:
        rec = (rec << 1) | bit      # record string = 2*rec + b, as record_sim
        nrec += 1
    return HState(st.au, st.av, idx, st.w, rec, nrec)


def leap(st, rule):
    """One leap; the cone shrinks: (au, av) -> (av - 1, av - 1 ... ) precisely: u' on |i| <= av-1 ... see below."""
    au, av = st.au, st.av
    nu = 2 * au + 1
    # new radii: with `left` leaps remaining before this leap, au = left-1, av = left; after it left' = left-1,
    # so au' = left-2, av' = left-1. For left = 1 (last leap) we keep au' = 0 (the site-0 pair is the output).
    av2 = av - 1
    au2 = max(av2 - 1, 0)
    assert av2 >= 0
    u = {i: (st.idx >> (i + au)) & 1 for i in range(-au, au + 1)}
    v = {i: (st.idx >> (nu + i + av)) & 1 for i in range(-av, av + 1)}
    nu2 = 2 * au2 + 1
    new = np.zeros_like(st.idx)
    for i in range(-au2, au2 + 1):          # u' = v
        new |= v[i] << (i + au2)
    for i in range(-av2, av2 + 1):          # v' = F(v) ^ u
        nv = F_bits_arr(v[i - 1], v[i], v[i + 1], rule) ^ u[i]
        new |= nv << (nu2 + i + av2)
    return compact(HState(au2, av2, new, st.w, st.rec, st.nrec))


def F_bits_arr(l, c, r, rule):
    return record_sim.F_bits(l, c, r, rule)      # the installed rules3b.F3B; numpy-vectorizable expressions


def compact(st):
    """Merge rows with equal (idx, rec), summing weights."""
    nbits = 2 * st.au + 1 + 2 * st.av + 1
    key = (st.rec << nbits) | st.idx
    order = np.argsort(key, kind='stable')
    key = key[order]
    w = st.w[order]
    first = np.ones(len(key), dtype=bool)
    first[1:] = key[1:] != key[:-1]
    starts = np.nonzero(first)[0]
    wsum = np.add.reduceat(w, starts)
    k = key[starts]
    return HState(st.au, st.av, k & ((np.int64(1) << nbits) - 1), wsum, k >> nbits, st.nrec)


def finish(st):
    """(counts per record string, total mass) as record_sim.run returns them."""
    n = 1 << st.nrec
    counts = np.zeros(n, dtype=np.int64)
    np.add.at(counts, st.rec, st.w)
    return [int(x) for x in counts], int(st.w.sum())


def run_H(protocol, rule, kappa, H):
    """Joint record distribution of one protocol under hidden law H; same output form as record3_sim.run3."""
    T = sum(1 for s in protocol if s in LEAPS)
    st = initial_cone(T, H)
    for s in protocol:
        if s in 'om':
            st = pair_map(st, kappa_fn(kappa), s == 'o')
        elif s == 'p':
            st = pair_map(st, kappa_fn(PASSIVE), True)
        elif s in NONLEAP:
            f = perm_of(s)
            st = pair_map(st, lambda q, f=f: (f(q), None), False)
        elif s != 'i':
            raise ValueError(s)
        if s in LEAPS:
            st = leap(st, rule)
    return finish(st)


def run_all_H(protocols, rule, kappa, H):
    """dict protocol -> (counts, mass), prefix-shared per total leap count T (as record_fast.run_all)."""
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

        def walk(node, st):
            if None in node:
                out[node[None]] = finish(st)
            for s, ch in node.items():
                if s is None:
                    continue
                if s in 'om':
                    nst = pair_map(st, kappa_fn(kappa), s == 'o')
                elif s in NONLEAP:
                    f = perm_of(s)
                    nst = pair_map(st, lambda q, f=f: (f(q), None), False)
                elif s == 'i':
                    nst = st
                else:
                    raise ValueError(s)
                if s in LEAPS:
                    nst = leap(nst, rule)
                walk(ch, nst)
        walk(trie, initial_cone(T, H))
    return out


def make_run_all(H):
    return lambda protocols, rule, kappa: run_all_H(protocols, rule, kappa, H)
