#!/usr/bin/env python3
"""Independent re-implementation of Main.md:500 (uniform-tape process dilation).

Written from the manuscript text alone (not from process_dilation_probes.py).
Exact rational arithmetic throughout.

Checks, for each target law:
  A. the partial step on well-formed states (clock c < K) is injective, and the
     lexicographic completion is a bijection of the FULL product C_V x C_H;
  B. mu_H is a probability law and does not depend on x_0 (by construction: one object);
  C. for every root x_0 (including roots of probability 0) and every k <= K, the realized
     law of (x_1..x_k) given x_0 equals the target conditional law, at every joint point;
     and the full joint P(x_0..x_K) with the target's (possibly irrational-free) initial law;
  D. recurrence time of the completed bijection on the prior-supported orbits
     (does the construction deliver K << t_R?  -- the theorem's parenthetical);
  E. negative controls: (i) tape reuse (every step reads s_1) must FAIL on a law whose
     consecutive conditionals are not independent; (ii) a wrong D (not a common
     denominator) must be detected.
"""
from fractions import Fraction as F
import itertools, random, sys

PAD = -1

def target_joint(kern, init, n, K):
    out = {}
    for tr in itertools.product(range(n), repeat=K + 1):
        p = init[tr[0]]
        for k in range(K):
            p *= kern(tr[:k + 1])[tr[k + 1]]
        if p:
            out[tr] = p
    return out

def target_cond(kern, n, K, x0, k):
    """law of (x_1..x_k) given x_0 from the kernels (defined for every root)."""
    out = {}
    for tail in itertools.product(range(n), repeat=k):
        tr = (x0,) + tail
        p = F(1)
        for j in range(k):
            p *= kern(tr[:j + 1])[tr[j + 1]]
        if p:
            out[tail] = p
    return out

def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)

def common_den(kern, n, K):
    D = 1
    for k in range(K):
        for past in itertools.product(range(n), repeat=k + 1):
            for q in kern(past):
                D = lcm(D, q.denominator)
    return D

def build(kern, n, K, D, reuse_tape=False):
    ledgers = list(itertools.product(list(range(n)) + [PAD], repeat=K))
    tapes = list(itertools.product(range(D), repeat=K))
    states = [(x, L, s, c) for x in range(n) for L in ledgers for s in tapes for c in range(K + 1)]
    def wf(L, c):
        return all(L[i] != PAD for i in range(c)) and all(L[i] == PAD for i in range(c, K))
    def Q(past, sym):
        acc = 0
        for y, q in enumerate(kern(past)):
            m = q * D
            if m.denominator != 1:
                raise ValueError("D not a common denominator")
            acc += m.numerator
            if sym < acc:
                return y
        raise ValueError("fibres do not fill Z_D")
    part = {}
    for (x, L, s, c) in states:
        if c < K and wf(L, c):
            past = tuple(L[:c]) + (x,)
            sym = s[0] if reuse_tape else s[c]          # s_{c+1} in 1-based indexing
            part[(x, L, s, c)] = (Q(past, sym), tuple(L[:c]) + (x,) + (PAD,) * (K - c - 1), s, c + 1)
    imgs = list(part.values())
    assert len(set(imgs)) == len(imgs), "A: partial step not injective"
    dom_c = sorted(set(states) - set(part))
    img_c = sorted(set(states) - set(imgs))
    assert len(dom_c) == len(img_c)
    phi = dict(part)
    phi.update(zip(dom_c, img_c))
    assert len(phi) == len(states) and set(phi.values()) == set(states), "A: completion not a bijection"
    prior = {((PAD,) * K, s, 0): F(1, len(tapes)) for s in tapes}
    assert sum(prior.values()) == 1, "B: prior not normalised"
    return phi, prior, len(ledgers) * len(tapes) * (K + 1), states

def realized_cond(phi, prior, x0, k):
    out = {}
    for (L, s, c), w in prior.items():
        st = (x0, L, s, c); tail = []
        for _ in range(k):
            st = phi[st]; tail.append(st[0])
        out[tuple(tail)] = out.get(tuple(tail), F(0)) + w
    return {t: p for t, p in out.items() if p}

def recurrence(phi, prior, x0):
    """orbit length of each prior-supported initial state."""
    lens = []
    for (L, s, c) in prior:
        st0 = (x0, L, s, c); st = phi[st0]; t = 1
        while st != st0:
            st = phi[st]; t += 1
        lens.append(t)
    return min(lens), max(lens)

def certify(name, kern, init, n, K, expect_fail_reuse=None):
    D = common_den(kern, n, K)
    phi, prior, mH, states = build(kern, n, K, D)
    for x0 in range(n):
        for k in range(K + 1):
            assert realized_cond(phi, prior, x0, k) == target_cond(kern, n, K, x0, k), \
                f"C: {name} mismatch x0={x0} k={k}"
    # full joint with the visible initial law
    real = {}
    for x0 in range(n):
        for tail, p in realized_cond(phi, prior, x0, K).items():
            if init[x0] * p:
                real[(x0,) + tail] = init[x0] * p
    assert real == target_joint(kern, init, n, K), f"C: {name} full joint mismatch"
    rmin = min(recurrence(phi, prior, x0)[0] for x0 in range(n))
    msg = f"{name}: n={n} K={K} D={D} |C_H|={mH} |S|={len(states)}  bijection OK, all roots, all k<=K exact; min orbit length={rmin}"
    if expect_fail_reuse is not None:
        phiR, priorR, _, _ = build(kern, n, K, D, reuse_tape=True)
        ok = all(realized_cond(phiR, priorR, x0, k) == target_cond(kern, n, K, x0, k)
                 for x0 in range(n) for k in range(K + 1))
        assert ok != expect_fail_reuse, f"E: reuse-tape control wrong on {name}"
        msg += f"; tape-reuse countercontrol {'FAILS as required' if expect_fail_reuse else 'passes (expected)'}"
    print(msg)
    return rmin

# ---- hand laws ----
def k_coin(p):  # i.i.d. fair coin (Markov)
    return (F(1, 2), F(1, 2))
def k_nm(p):    # non-Markov with zeros
    c = len(p) - 1
    if c == 0: return (F(3, 4), F(1, 4)) if p[0] == 0 else (F(0), F(1))
    if c == 1: return (F(1), F(0)) if p[0] == p[1] else (F(1, 3), F(2, 3))
    return (F(1, 6), F(5, 6)) if p[0] == 0 else (F(1, 2), F(1, 2))
def k_xor(p):   # X1 fair, X2 = X0 xor X1 : max readback, P-divisible
    c = len(p) - 1
    if c == 0: return (F(1, 2), F(1, 2))
    y = p[0] ^ p[1]; return (F(1), F(0)) if y == 0 else (F(0), F(1))
def k_rev(p):   # delayed revival
    c = len(p) - 1
    if c in (0, 2): return (F(1), F(0)) if p[0] == 0 else (F(0), F(1))
    return (F(1, 2), F(1, 2))
def k_det(p):   # deterministic many-to-one visible step: x -> 0
    return (F(1), F(0))

certify("coin K=1", k_coin, (F(1, 2), F(1, 2)), 2, 1, expect_fail_reuse=False)
certify("coin K=3", k_coin, (F(1, 2), F(1, 2)), 2, 3, expect_fail_reuse=True)
certify("non-Markov w/ zeros K=3, P(x0)=(1,0)", k_nm, (F(1), F(0)), 2, 3, expect_fail_reuse=True)
certify("XOR K=2", k_xor, (F(1, 3), F(2, 3)), 2, 2, expect_fail_reuse=False)
certify("delayed revival K=3", k_rev, (F(1, 2), F(1, 2)), 2, 3, expect_fail_reuse=False)
certify("many-to-one deterministic K=2", k_det, (F(1, 2), F(1, 2)), 2, 2)

# ---- wrong-D countercontrol ----
try:
    build(k_nm, 2, 3, 4)   # true D = 12
    print("E(ii): wrong D NOT detected  <-- control failure"); sys.exit(1)
except ValueError:
    print("E(ii): non-common-denominator D rejected (control live)")

# ---- random rational laws, n in {2,3}, with forced zeros ----
rng = random.Random(20261027)
def rand_dist(n, dens=(1, 2, 3, 4, 6)):
    while True:
        d = rng.choice(dens)
        w = [rng.randint(0, d) for _ in range(n)]
        if sum(w):
            tot = sum(w); return tuple(F(x, tot) for x in w)
def rand_kernel(n, K):
    tab = {}
    for k in range(K):
        for past in itertools.product(range(n), repeat=k + 1):
            tab[past] = rand_dist(n)
    return lambda p: tab[tuple(p)]

cnt = 0; worst = None
for (n, K, reps) in [(2, 1, 20), (2, 2, 20), (2, 3, 8), (3, 1, 15), (3, 2, 4)]:
    for _ in range(reps):
        kern = rand_kernel(n, K); init = rand_dist(n)
        D = common_den(kern, n, K)
        if (n + 1) ** K * D ** K * (K + 1) * n > 400000:
            continue
        r = certify(f"random n={n} K={K}", kern, init, n, K)
        cnt += 1
        worst = r if worst is None else min(worst, r)
print(f"random rational laws certified: {cnt}; smallest orbit length seen on prior support = {worst}")
print("tape_check: COMPLETE")
