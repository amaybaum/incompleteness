#!/usr/bin/env python3
"""NATPREP-1 exact controls (paper-only unit; small exact cases).

Every probability is an exact Fraction; entropies that are needed are exact
elements a + b*log2(3), compared by integer arithmetic. Lattice checks are exact
integer computations on small boxes (closed in Z^3, so in-box dynamics is exact)
and on small periodic cubic lattices. Pseudo-random instances use fixed seeds;
each instance is then checked exactly. Decimal values are printed for reading
only; no decimal value certifies an equality or inequality.

Run:  python3 -I natprep_checks.py          (default set; exit 0 iff every check holds)
      python3 -I natprep_checks.py --full   (adds the larger enumerations of S2-full)
"""
from fractions import Fraction as Fr
from itertools import product, combinations
from math import lcm
import random
import sys

RESULTS = []
FULL = '--full' in sys.argv[1:]


def check(name, ok):
    RESULTS.append((name, bool(ok)))
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'}")


# ----------------------------------------------------------------- exact logs
class L:
    """a + b*log2(3), a and b rational."""

    def __init__(self, a=0, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = o if isinstance(o, L) else L(o)
        return L(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return L(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, L) else L(o)))

    def __eq__(self, o):
        o = o if isinstance(o, L) else L(o)
        return self.a == o.a and self.b == o.b

    def __repr__(self):
        return f"{self.a} + {self.b}*log2(3)"


def _v(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k, n


def log2_23(x):
    x = Fr(x)
    a2, rn = _v(x.numerator, 2)
    a3, rn = _v(rn, 3)
    b2, rd = _v(x.denominator, 2)
    b3, rd = _v(rd, 3)
    if rn != 1 or rd != 1:
        raise ValueError(f"not a {{2,3}}-rational: {x}")
    return L(a2 - b2, a3 - b3)


# ================================================================ the rule U2
def g2(s):
    return ((s + 1) // 3) & 1


def gq(s, q):
    return ((s + 1) // 3) % q


class Box:
    """A box of the cubic lattice with free boundary. A box is closed in Z^3
    (DELIVER-1 Lemma 2.3(a)), so for a perturbation supported in it the in-box
    dynamics is the exact Z^3 dynamics. States are (prev_mask, cur_mask)."""

    def __init__(self, dims):
        self.dims = dims
        self.S = list(product(*[range(d) for d in dims]))
        ix = {s: i for i, s in enumerate(self.S)}
        self.n = len(self.S)
        self.NB = []
        for s in self.S:
            m = 0
            for ax in range(len(dims)):
                for d in (1, -1):
                    t = list(s)
                    t[ax] += d
                    if tuple(t) in ix:
                        m |= 1 << ix[tuple(t)]
            self.NB.append(m)
        N = 1 << self.n
        self.N = N
        T = [0] * (N * N)
        for p in range(N):
            for c in range(N):
                nc = 0
                for i in range(self.n):
                    if g2(bin(c & self.NB[i]).count('1')):
                        nc |= 1 << i
                T[p * N + c] = c * N + (nc ^ p)
        self.T = T
        oid, pos, orb = [-1] * (N * N), [0] * (N * N), []
        for s in range(N * N):
            if oid[s] >= 0:
                continue
            o, x = [], s
            while oid[x] < 0:
                oid[x], pos[x] = len(orb), len(o)
                o.append(x)
                x = T[x]
            orb.append(o)
        self.oid, self.pos, self.orb = oid, pos, orb

    def at(self, s, t):
        o = self.orb[self.oid[s]]
        return o[(self.pos[s] + t) % len(o)]

    def period(self, s):
        return len(self.orb[self.oid[s]])

    def cont(self, s, sites_):
        p, c = s // self.N, s % self.N
        return tuple(((p >> i) & 1, (c >> i) & 1) for i in sites_)


BOXES = {}


def box_(dims):
    if dims not in BOXES:
        BOXES[dims] = Box(dims)
    return BOXES[dims]


MODES = ('c', 'p', 'b')  # carrier bit on the current slice, the previous slice, or both


def carrier_bits(cs, modes):
    out = []
    for s_, m_ in zip(cs, modes):
        bits = []
        if m_ in ('c', 'b'):
            bits.append((1, s_))
        if m_ in ('p', 'b'):
            bits.append((0, s_))
        out.append(bits)
    return out


def branches(B, cs, modes, env):
    """env: dict {(slice, site): bit} for the non-carrier bits. Returns [(cv, state)]."""
    cb = carrier_bits(cs, modes)
    p0 = sum(1 << i for (sl, i), v in env.items() if v and sl == 0)
    c0 = sum(1 << i for (sl, i), v in env.items() if v and sl == 1)
    out = []
    for cv in product((0, 1), repeat=len(cs)):
        p, c = p0, c0
        for bl, v in zip(cb, cv):
            if v:
                for sl, i in bl:
                    if sl:
                        c |= 1 << i
                    else:
                        p |= 1 << i
        out.append((cv, p * B.N + c))
    return out


def law_differs(vals, cvs, kk):
    a0 = sorted(v for v, cv in zip(vals, cvs) if cv[kk] == 0)
    a1 = sorted(v for v, cv in zip(vals, cvs) if cv[kk] == 1)
    return a0 != a1


def determines(vals, cvs, kk):
    v0 = {v for v, cv in zip(vals, cvs) if cv[kk] == 0}
    v1 = {v for v, cv in zip(vals, cvs) if cv[kk] == 1}
    return not (v0 & v1)


def delivery(B, cs, modes, env, H, ndel, strict=True, want=None, earliest=False):
    """DT+(R) with eps = 0 for a single-site block H (node 1 of RESULT.md).
    ndel = 1: tau1 < s < tau2, H = w* at tau1 and tau2 for every carrier value, the law of
              W_s(H) depends on c_k, a log block disjoint from carriers and H determines c_k
              at the retention time and meets (R).
    ndel = 2: tau1 < tau2 < tau3; a used in (tau1, tau2); b unused at every t <= tau2 and used in
              (tau2, tau3); both records held at the retention time, each meeting (R).
    strict: retention time = the last refresh time (records held while H is ready).
            Otherwise (literal reading) any later time.
    earliest (ndel = 1, strict only): return the delivery with the smallest tau2 in the window.
    Returns a description of the first delivery found, or None."""
    br = branches(B, cs, modes, env)
    cvs = [cv for cv, _ in br]
    P = lcm(*[B.period(s) for _, s in br])
    W = 3 * P
    traj = [[B.at(s, t) for t in range(W)] for _, s in br]
    k = len(cs)
    hc = [[B.cont(tr[t], (H,))[0] for tr in traj] for t in range(W)]
    ready = [hc[t][0] if all(v == hc[t][0] for v in hc[t]) else None for t in range(W)]
    if want is not None:
        ready = [r if r == want else None for r in ready]
    rt = [t for t in range(W) if ready[t] is not None]
    if len(rt) < 2:
        return None
    use = [[law_differs(hc[t], cvs, kk) for t in range(W)] for kk in range(k)]
    if not any(any(u) for u in use):
        return None
    logsites = [i for i in range(B.n) if i not in cs and i != H]
    recs = []  # per carrier: list of (log block, residues mod P at which it determines)
    for kk in range(k):
        lst = []
        if any(use[kk]):
            s_min = use[kk].index(True)
            for r in range(1, len(logsites) + 1):
                for Lb in combinations(logsites, r):
                    lc = [[B.cont(tr[t], Lb) for tr in traj] for t in range(P)]
                    if any(law_differs(lc[t], cvs, kk) for t in range(min(s_min, P))):
                        continue
                    det = {t for t in range(P) if determines(lc[t], cvs, kk)}
                    if det:
                        lst.append((Lb, det))
        recs.append(lst)

    def rec_at(kk, t):
        return [Lb for Lb, d in recs[kk] if (t % P) in d]

    if ndel == 1 and strict and earliest:
        for t2 in rt:
            for kk in range(k):
                Ls = rec_at(kk, t2) if recs[kk] else []
                if not Ls:
                    continue
                for t1 in rt:
                    if t1 >= t2:
                        break
                    if ready[t2] == ready[t1] and any(use[kk][t1 + 1:t2]):
                        return dict(carrier=kk, taus=(t1, t2), T=t2, log=Ls[0], w=ready[t1], P=P)
        return None
    if ndel == 1:
        for kk in range(k):
            if not recs[kk]:
                continue
            for i1, t1 in enumerate(rt):
                for t2 in rt[i1 + 1:]:
                    if ready[t2] != ready[t1] or not any(use[kk][t1 + 1:t2]):
                        continue
                    if strict:
                        Ls = rec_at(kk, t2)
                        if Ls:
                            return dict(carrier=kk, taus=(t1, t2), T=t2, log=Ls[0], w=ready[t1], P=P)
                    else:
                        for T_ in range(t2, t2 + P):
                            Ls = rec_at(kk, T_)
                            if Ls:
                                return dict(carrier=kk, taus=(t1, t2), T=T_, log=Ls[0], w=ready[t1], P=P)
        return None
    for ka, kb in ((0, 1), (1, 0)):
        if not recs[ka] or not recs[kb]:
            continue
        sb = use[kb].index(True)
        for i1, t1 in enumerate(rt):
            for t2 in rt[i1 + 1:]:
                if t2 >= sb or ready[t2] != ready[t1] or not any(use[ka][t1 + 1:t2]):
                    continue
                for t3 in rt:
                    if t3 <= t2 or ready[t3] != ready[t1] or not any(use[kb][t2 + 1:t3]):
                        continue
                    if rec_at(ka, t3) and rec_at(kb, t3):
                        return dict(carriers=(ka, kb), taus=(t1, t2, t3), T=t3,
                                    logs=(rec_at(ka, t3)[0], rec_at(kb, t3)[0]), w=ready[t1], P=P)
    return None


def env_bits(B, cs, modes):
    occ = {b for bl in carrier_bits(cs, modes) for b in bl}
    return [(sl, i) for sl in (0, 1) for i in range(B.n) if (sl, i) not in occ]


def enumerate_deliveries(dims, k, ndel):
    """All (carrier sites, modes, H, environment) on the box with a strict DT+(R) delivery."""
    B = box_(dims)
    out = []
    for cs in combinations(range(B.n), k):
        for modes in product(MODES, repeat=k):
            eb = env_bits(B, cs, modes)
            for z in range(1 << len(eb)):
                env = {b: (z >> j) & 1 for j, b in enumerate(eb)}
                w = bin(z).count('1')
                for H in range(B.n):
                    if H in cs:
                        continue
                    hit = delivery(B, cs, modes, env, H, ndel)
                    if hit:
                        out.append((cs, modes, H, z, w, len(eb), hit))
    return out


# ============================================================ Node 1 controls
def node1():
    # CC1: the designed pattern of DELIVER-1 2.3(f) as a law on a ring of 10 sites (two copies,
    # period 5, carrier fair): site marginals differ (not translation invariant: fails U1); its
    # random-offset average is translation invariant but not a product law (fails U2).
    pat = lambda c: [(0, c), (0, 0), (0, 1), (0, 0), (0, 1)] * 2
    law = {}
    for c in (0, 1):
        st = tuple(pat(c))
        law[st] = law.get(st, 0) + Fr(1, 2)
    marg = [{} for _ in range(10)]
    for st, p in law.items():
        for i in range(10):
            marg[i][st[i]] = marg[i].get(st[i], 0) + p
    not_ti = len({tuple(sorted(m.items())) for m in marg}) > 1
    avg = {}
    for st, p in law.items():
        for off in range(10):
            sh = st[off:] + st[:off]
            avg[sh] = avg.get(sh, 0) + p / 10
    m0 = {}
    for st, p in avg.items():
        m0[st[0]] = m0.get(st[0], 0) + p
    ti = all(sum(p for st, p in avg.items() if st[i] == v) == m0[v] for i in range(10) for v in m0)
    pair = {}
    for st, p in avg.items():
        pair[(st[0], st[1])] = pair.get((st[0], st[1]), 0) + p
    not_prod = any(pair.get((a, b), 0) != m0[a] * m0[b] for a in m0 for b in m0)
    check("N1-CC1 countercontrol: the designed (f) pattern has unequal site marginals (fails U1); "
          "its random-offset average is translation invariant but not a product law (fails U2)",
          not_ti and ti and not_prod)

    # CC2: conditioning the product law nu_rho on the environment event E_z of a finite region
    # returns exactly the designed deterministic law on that region (fails U3; Lemma N4.1).
    rho = Fr(1, 4)
    bits = 9
    z = 0b101000000  # the (f) environment on the 5-site segment, current slice of sites 2 and 4
    nu = {x: rho ** bin(x).count('1') * (1 - rho) ** (bits - bin(x).count('1')) for x in range(1 << bits)}
    cond = {x: (p / nu[z] if x == z else 0) for x, p in nu.items()}
    check("N1-CC2 countercontrol: nu_rho conditioned on the (f) environment event is the point "
          "mass on the designed pattern (fails U3; it is the designed law)",
          sum(nu.values()) == 1 and cond[z] == 1 and sum(cond.values()) == 1)


# ============================================================ Node 2 controls
def node2():
    # S1: single-site states never leave their site (a singleton is closed), on every box.
    shapes = [(3,), (4,), (5,), (6,), (7,), (2, 2), (2, 3), (3, 3), (2, 2, 2)]
    ok = True
    for d in shapes:
        B = box_(d)
        for j in range(B.n):
            for (pb, cb) in ((0, 1), (1, 0), (1, 1)):
                s = (pb << j) * B.N + (cb << j)
                for x in B.orb[B.oid[s]]:
                    p, c = x // B.N, x % B.N
                    if (p | c) & ~(1 << j):
                        ok = False
    check("S1a every single-site perturbation stays on its site along its whole orbit, on lines "
          "3..7 and boxes 2x2, 2x3, 3x3, 2x2x2 (a singleton is closed; DL1 Theorem 2.2)", ok)

    # S1b: pure parity-uniform supply, K single-site carriers: for every position/mode choice
    # the best predictor of c_k from ALL non-carrier sites errs w.p. >= 2^-K at every time.
    ok, tight = True, False
    for d, K in [((4,), 1), ((5,), 1), ((6,), 1), ((4,), 2), ((5,), 2), ((6,), 2), ((2, 3), 2),
                 ((5,), 3), ((6,), 3), ((2, 2, 2), 2)]:
        B = box_(d)
        for cs in combinations(range(B.n), K):
            logs = tuple(i for i in range(B.n) if i not in cs)
            for modes in product(MODES, repeat=K):
                br = branches(B, cs, modes, {})
                cvs = [cv for cv, _ in br]
                P = lcm(*[B.period(s) for _, s in br])
                for t in range(P):
                    vals = [B.cont(B.at(s, t), logs) for _, s in br]
                    for kk in range(K):
                        err = Fr(0)
                        for v in set(vals):
                            n0 = sum(1 for x, cv in zip(vals, cvs) if x == v and cv[kk] == 0)
                            n1 = sum(1 for x, cv in zip(vals, cvs) if x == v and cv[kk] == 1)
                            err += Fr(min(n0, n1), 2 ** K)
                        if err < Fr(1, 2 ** K):
                            ok = False
                        if err == Fr(1, 2 ** K) and K >= 2:
                            tight = True
    check("S1b pure parity-uniform supply with K = 1..3 single-site carriers (lines 4..6, 2x3, "
          "2x2x2): a log disjoint from the carriers never predicts c_k with error < 2^-K "
          "(Lemma N2.1); the bound is attained for K >= 2", ok and tight)

    # S1c countercontrols: (i) a carrier region that is not closed ({j, j+2} on a line) leaks;
    # (ii) one environment excitation is not enough on these boxes, two are (S2).
    B = box_((5,))
    br = branches(B, (0, 2), ('c', 'c'), {})
    # both carrier sites carry the same bit c: take the branches with equal values
    same = [(cv, s) for cv, s in br if cv[0] == cv[1]]
    leak = any(B.cont(B.at(same[0][1], t), (1,)) != B.cont(B.at(same[1][1], t), (1,))
               for t in range(12))
    check("S1c countercontrol: a carrier region {j, j+2} with both bits equal to c is not closed, "
          "and the site between them depends on c", leak)

    # S2: exhaustive strict DT+(R) enumeration on small boxes, arbitrary environments.
    def summary(dims, k, nd):
        f = enumerate_deliveries(dims, k, nd)
        return len(f), (min(x[4] for x in f) if f else None), f

    res = {}
    for args in [((3,), 1, 1), ((4,), 1, 1), ((5,), 1, 1), ((2, 2), 1, 1),
                 ((2, 2), 2, 1), ((4,), 2, 1), ((2, 2), 2, 2), ((4,), 2, 2), ((5,), 2, 2)]:
        res[args] = summary(*args)
    line = "; ".join(f"{'x'.join(map(str, a[0]))} k={a[1]} N={a[2]}: {res[a][0]} found, min weight {res[a][1]}"
                     for a in res)
    print("   S2 summary:", line)
    n1_ok = all(res[a][1] == 2 for a in [((4,), 1, 1), ((5,), 1, 1), ((2, 2), 1, 1), ((2, 2), 2, 1),
                                         ((4,), 2, 1)]) and res[((3,), 1, 1)][0] == 0
    n2_none = all(res[a][0] == 0 for a in [((2, 2), 2, 2), ((4,), 2, 2), ((5,), 2, 2)])
    check("S2a strict DT+(R) enumeration (eps = 0, all environments, all single-site carrier "
          "positions and modes, all H): single deliveries exist on lines 4, 5 and 2x2 with 1-2 "
          "carriers, none with fewer than 2 environment excitations; none on line 3", n1_ok)
    check("S2b no double delivery (N = 2) on 2x2, line 4 or line 5 with two carriers", n2_none)

    # The (f) placement: carrier at site 0 (current slice), H = site 1, w* = (0,0).
    B5 = box_((5,))
    eb5 = env_bits(B5, (0,), ('c',))
    f_env = {b: 0 for b in eb5}
    f_env[(1, 2)] = f_env[(1, 4)] = 1
    hit_f = delivery(B5, (0,), ('c',), f_env, 1, 1)
    check(f"S2c positive control: DELIVER-1 2.3(f) is a strict single delivery: {hit_f}",
          hit_f is not None and hit_f['taus'] == (0, 5) and hit_f['w'] == (0, 0) and hit_f['log'] == (3,))
    B6 = box_((6,))
    cs6, md6 = (1, 2), ('c', 'c')
    i_env = {b: 0 for b in env_bits(B6, cs6, md6)}
    for b in [(1, 0), (0, 3), (1, 3), (0, 5), (1, 5)]:
        i_env[b] = 1
    hit_i = delivery(B6, cs6, md6, i_env, 3, 2, want=(1, 1))
    check(f"S2d positive control: DELIVER-1 2.3(i) is a strict double delivery: {hit_i}",
          hit_i is not None and hit_i['w'] == (1, 1) and hit_i['logs'] == ((4,), (4,)))

    # Retention-time countercontrol: the 2x2 plaquette with one excitation diagonal to the carrier
    # delivers in the literal reading (record at a later time) but not in the strict reading;
    # its log equals H at every time.
    B4 = box_((2, 2))
    pl_env = {b: 0 for b in env_bits(B4, (0,), ('c',))}
    pl_env[(1, 3)] = 1
    lax = delivery(B4, (0,), ('c',), pl_env, 1, 1, strict=False)
    strict = delivery(B4, (0,), ('c',), pl_env, 1, 1, strict=True)
    br = branches(B4, (0,), ('c',), pl_env)
    mirror = all(B4.cont(B4.at(s, t), (1,)) == B4.cont(B4.at(s, t), (2,)) for _, s in br for t in range(12))
    check(f"S2e countercontrol for the retention time: plaquette delivers in the literal reading "
          f"({lax}) and not in the strict one; its log mirrors H at every time",
          lax is not None and strict is None and mirror)

    # S3: probability of the (f) placement under nu_rho, with an isolation factor.
    def ball_count(seg_len, T):
        cnt = 0
        for x in range(-T, seg_len + T):
            dx = 0 if 0 <= x < seg_len else (-x if x < 0 else x - seg_len + 1)
            r = T - dx
            if r >= 0:
                cnt += 2 * r * r + 2 * r + 1
        return cnt

    def ball_brute(seg_len, T):
        c = 0
        for x in range(-T - 1, seg_len + T + 1):
            for y in range(-T - 1, T + 2):
                for zz in range(-T - 1, T + 2):
                    dx = 0 if 0 <= x < seg_len else (-x if x < 0 else x - seg_len + 1)
                    if dx + abs(y) + abs(zz) <= T:
                        c += 1
        return c

    b5, b16 = ball_count(5, 5), ball_count(6, 16)
    check(f"S3a |B(segment, T)| in Z^3: {b5} for (f) (5 sites, T = 5), {b16} for (i) (6 sites, T = 16)",
          b5 == ball_brute(5, 5) == 475 and b16 == ball_brute(6, 16) == 8742)
    # delivering environments of the (f) placement (carrier 0 'c', H = 1, w* = (0,0)) by weight,
    # each with its earliest horizon tau2 (the record time). The empty-cone factor for horizon T
    # isolates only deliveries with tau2 <= T, so the displayed sum (T = 5) is restricted to them.
    byw, byw5, hor = {}, {}, {}
    w2_tau2 = []
    for zz in range(1 << len(eb5)):
        env = {b: (zz >> j) & 1 for j, b in enumerate(eb5)}
        d = delivery(B5, (0,), ('c',), env, 1, 1, want=(0, 0), earliest=True)
        assert bool(d) == bool(delivery(B5, (0,), ('c',), env, 1, 1, want=(0, 0)))
        if d:
            w = bin(zz).count('1')
            t2 = d['taus'][1]
            byw[w] = byw.get(w, 0) + 1
            hor[t2] = hor.get(t2, 0) + 1
            if t2 <= 5:
                byw5[w] = byw5.get(w, 0) + 1
            if w == 2:
                w2_tau2.append(t2)
    m5 = len(eb5)
    iso = 2 * (b5 - 5)
    def pi_f(r):
        return sum(c * r ** w * (1 - r) ** (m5 - w) for w, c in byw5.items()) * (1 - r) ** iso
    vals = {r: pi_f(r) for r in (Fr(1, 10), Fr(1, 100), Fr(1, 1000))}
    floor = {r: r ** 2 * (1 - r) ** (iso + m5 - 2) for r in vals}
    check(f"S3b (f) placement: delivering environments by weight {dict(sorted(byw.items()))}, "
          f"by earliest tau2 {dict(sorted(hor.items()))}; with tau2 <= 5, by weight "
          f"{dict(sorted(byw5.items()))}; the weight-2 environment has tau2 = {w2_tau2}; "
          f"pi(rho) >= sum_(z: tau2 <= 5) rho^w (1-rho)^(9-w) * (1-rho)^{iso} >= rho^2 (1-rho)^{iso + m5 - 2} > 0; "
          f"at rho = 1/10, 1/100, 1/1000: "
          f"{', '.join(f'{float(v):.3e}' for v in vals.values())}",
          min(byw5) == 2 and w2_tau2 == [5] and sum(byw.values()) == 20
          and all(vals[r] >= floor[r] > 0 for r in vals))

    # S4: dilution. Isolated segment, environment nu_rho on the 9 environment bits, carrier fair.
    # Annealed record error of c from log {3} at t = 5 is >= (1/2)(1-rho)^8 (Lemma N2.3).
    ok4, show = True, []
    for r in (Fr(1, 10), Fr(1, 100)):
        joint = {}
        ready0 = ready5 = Fr(0)
        for zz in range(1 << m5):
            env = {b: (zz >> j) & 1 for j, b in enumerate(eb5)}
            pz = r ** bin(zz).count('1') * (1 - r) ** (m5 - bin(zz).count('1'))
            for cv, s in branches(B5, (0,), ('c',), env):
                p = pz / 2
                key = (B5.cont(B5.at(s, 5), (3,)), cv[0])
                joint[key] = joint.get(key, 0) + p
                if B5.cont(s, (1,))[0] == (0, 0):
                    ready0 += p
                if B5.cont(B5.at(s, 5), (1,))[0] == (0, 0):
                    ready5 += p
        err = sum(min(joint.get((v, 0), 0), joint.get((v, 1), 0)) for v in {k_[0] for k_ in joint})
        bound = Fr(1, 2) * (1 - r) ** 8
        ok4 &= err >= bound
        show.append(f"rho={r}: P(H ready at 0)={float(ready0):.4f}, at 5={float(ready5):.4f}, "
                    f"record error={float(err):.4f} >= {float(bound):.4f}")
    check("S4 dilution on the isolated (f) segment: " + "; ".join(show), ok4)


# ============================================================ Node 3 controls
def tor_nbrs(i, n):
    x, y, z = i
    return [((x + 1) % n, y, z), ((x - 1) % n, y, z), (x, (y + 1) % n, z),
            (x, (y - 1) % n, z), (x, y, (z + 1) % n), (x, y, (z - 1) % n)]


def tor_step(prev, cur, n, g=g2):
    cnt = {}
    for j in cur:
        for i in tor_nbrs(j, n):
            cnt[i] = cnt.get(i, 0) + 1
    return cur, {i for i, c in cnt.items() if g(c) == 1} ^ prev


def tor_closure(A, n):
    D = set(A)
    frontier = set(A)
    while frontier:
        cnt = {}
        for j in D:
            for i in tor_nbrs(j, n):
                if i not in D:
                    cnt[i] = cnt.get(i, 0) + 1
        add = {i for i, c in cnt.items() if c >= 2}
        D |= add
        frontier = add
    return D


def l1(a, b, n):
    return sum(min((x - y) % n, (y - x) % n) for x, y in zip(a, b))


def components(D, n):
    """classes of D under chains of l1-distance <= 2"""
    D = set(D)
    out = []
    while D:
        s = D.pop()
        comp, stack = {s}, [s]
        while stack:
            u = stack.pop()
            near = [v for v in D if l1(u, v, n) <= 2]
            for v in near:
                D.discard(v)
                comp.add(v)
                stack.append(v)
        out.append(frozenset(comp))
    return set(out)


def is_closed_t(D, n):
    cnt = {}
    for j in D:
        for i in tor_nbrs(j, n):
            if i not in D:
                cnt[i] = cnt.get(i, 0) + 1
    return all(c < 2 for c in cnt.values())


def node3():
    # T1: component partition invariant and autonomous (random finite configurations).
    n = 14
    rng = random.Random(20261119)
    ok, nonsplit, merged_ok = True, 0, True
    for trial in range(6):
        prev, cur = set(), set()
        for corner in [(1, 1, 1), (6, 2, 3), (2, 8, 8), (9, 9, 2)]:
            for d in product(range(3), repeat=3):
                site = tuple((c + e) % n for c, e in zip(corner, d))
                if rng.random() < 0.3:
                    cur.add(site)
                if rng.random() < 0.2:
                    prev.add(site)
        A0 = prev | cur
        C0 = components(tor_closure(A0, n), n)
        ok &= all(is_closed_t(D, n) for D in C0)
        ok &= all(min(l1(a, b, n) for a in D1 for b in D2) >= 3 for D1 in C0 for D2 in C0 if D1 != D2)
        iso = {D: (prev & D, cur & D) for D in C0}
        p, c = prev, cur
        for t in range(1, 31):
            p, c = tor_step(p, c, n)
            Ct = components(tor_closure(p | c, n), n)
            ok &= (Ct == C0)
            for D in C0:
                ip, ic = tor_step(*iso[D], n)
                iso[D] = (ip, ic)
                ok &= (ip == p & D and ic == c & D)
        nonsplit += len(C0)
    check(f"T1 component partition of cl2(A_0) is invariant and each class evolves alone "
          f"(6 random finite configurations, {nonsplit} classes, n = 14, 30 ticks); classes are "
          "closed and pairwise at l1-distance >= 3 (Theorem N3.1)", ok)

    # T2: finite-horizon locality on a noisy torus (infinite-support analogue).
    n, rho = 16, 0.06
    ok2, grew, horizon_matters = True, False, False
    for seed in range(1, 9):
        rng = random.Random(seed)
        prev = {s for s in product(range(n), repeat=3) if rng.random() < rho}
        cur = {s for s in product(range(n), repeat=3) if rng.random() < rho}
        R = (0, 0, 0)
        full = [(prev, cur)]
        p, c = prev, cur
        for t in range(10):
            p, c = tor_step(p, c, n)
            full.append((p, c))
        lastD = frozenset()
        for T in range(0, 7):
            ballT = {s for s in product(range(n), repeat=3) if l1(s, R, n) <= T}
            A = (prev | cur) & ballT
            Dt = set()
            for D in components(tor_closure(A, n), n):
                if R in D:
                    Dt |= D
            ok2 &= lastD <= frozenset(Dt)
            grew |= (len(Dt) > len(lastD) > 0)
            lastD = frozenset(Dt)
            ip, ic = prev & Dt, cur & Dt
            for t in range(0, 10):
                same = ((R in ip) == (R in full[t][0])) and ((R in ic) == (R in full[t][1]))
                if t <= T:
                    ok2 &= same
                elif not same:
                    horizon_matters = True
                ip, ic = tor_step(ip, ic, n)
    check("T2 finite-horizon locality (noisy n = 16 torus, rho = 0.06, 8 seeds, T = 0..6): the "
          "history of the origin up to T equals the isolated evolution of D_T; D_T is non-decreasing "
          "and grows in some instance; after T the isolated evolution can differ (countercontrol)",
          ok2 and grew and horizon_matters)

    # T3: the plaquette's components depend on the carrier value.
    n = 8
    C_, H_, L_, E_ = (0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0)
    comp0 = components(tor_closure({E_}, n), n)
    comp1 = components(tor_closure({E_, C_}, n), n)
    check("T3 plaquette: with c = 0 the only class is {E}; with c = 1 it is the 2x2 square "
          "containing H and the log (D*(H) is the square)",
          comp0 == {frozenset({E_})} and comp1 == {frozenset({C_, H_, L_, E_})})

    # T4: the blocking property and its failures.
    prop = g2(0) == g2(1) == 0 and g2(5) == g2(6) == 0
    gm = lambda s: 1 if s == 1 else g2(s)  # mutation: g(1) = 1
    p, c = set(), {(0, 0, 0)}
    p, c = tor_step(p, c, 8, gm)
    leaks = len(c - {(0, 0, 0)}) > 0
    check("T4a blocking property (P): g(0) = g(1) = 0 and g(5) = g(6) = 0; mutation g(1) = 1 "
          "lets a single excitation leave its site (countercontrol)", prop and leaks)
    okq = True
    radii = {}
    for q in (3, 2 ** 16):
        n = 45
        cur = {(0, 0, 0): 2}
        prev = {}
        rr = []
        for t in range(1, 21):
            cnt = {}
            for j, v in cur.items():
                for i in tor_nbrs(j, n):
                    cnt[i] = cnt.get(i, 0) + v
            keys = set(cnt) | set(prev) | set(cur)
            nxt = {}
            for i in keys:
                val = (gq(cnt.get(i, 0), q) - prev.get(i, 0)) % q
                if val:
                    nxt[i] = val
            prev, cur = cur, nxt
            rr.append(max(l1(i, (0, 0, 0), n) for i in set(prev) | set(cur)))
        radii[q] = rr
        okq &= gq(2, q) == 1 and rr[-1] >= 12 and all(a <= b for a, b in zip(rr, rr[1:]))
    check(f"T4b q = 3 and q = 2^16: G(2) = 1, and the two-slice support of a single symbol 2 in "
          f"the vacuum reaches l1-radius {radii[3][-1]} (q = 3) and {radii[2 ** 16][-1]} (q = 2^16) "
          f"at t = 20 (n = 45 torus; radii by tick {radii}); no confinement", okq)


# ============================================================ Node 4 controls
def node4():
    # Exact accounting at rho = 1/4: for an environment pattern z of m bits and weight w,
    # m = log2(1/nu(z)) + log2(nu(z)/u(z)), and the selection cost is log2(1/nu(z)).
    rho = Fr(1, 4)
    ok = True
    rows = []
    for name, m, w, N in (("(f)", 9, 2, 1), ("(i)", 10, 5, 2)):
        nu = rho ** w * (1 - rho) ** (m - w)
        sel = -log2_23(nu)
        sup = log2_23(nu * 2 ** m)
        ok &= (sel + sup) == L(m)
        ok &= m >= N + 1
        rows.append(f"{name}: m={m}, selection cost {sel}, supply term {sup}, (2.4) needs {N + 1}")
    check("A1 accounting identity m = log2(1/nu(z)) + log2(nu(z)/u(z)) and (2.4) slack: " + "; ".join(rows), ok)


# ============================================================ full mode
def full():
    expected = {((6,), 1, 1): (19712, 2), ((2, 3), 1, 1): (56884, 2),
                ((6,), 2, 2): (664, 5), ((2, 3), 2, 2): (760, 5)}
    for args, exp in expected.items():
        f = enumerate_deliveries(*args)
        mw = min(x[4] for x in f) if f else None
        check(f"S2-full {'x'.join(map(str, args[0]))} k={args[1]} N={args[2]}: {len(f)} found, "
              f"min weight {mw}", (len(f), mw) == exp)
        sys.stdout.flush()


def main():
    node1()
    node2()
    node3()
    node4()
    if FULL:
        full()
    bad = [n for n, ok in RESULTS if not ok]
    print(f"{len(RESULTS) - len(bad)}/{len(RESULTS)} checks hold")
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
