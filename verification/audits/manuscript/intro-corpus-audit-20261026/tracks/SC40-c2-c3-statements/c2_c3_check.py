#!/usr/bin/env python3
"""SC-40 checks: the quantity bounded by Main's physical-memory theorem, and the C3 attainment.

Run with `python3 -I c2_c3_check.py`. Standard library only. Deterministic (fixed seed).

(1) Range of the bound. g(e) = 2[e log2(n-1) + h(e)] increases on [0, 1-1/n] from 0 to 2 log2 n
    (float check of the closed-form endpoint and of monotonicity on a grid; the algebra is in the
    README). Hence eps_min(M, n) is defined exactly for 0 <= M <= 2 log2 n.
(2) The I* form is not well formed in general. Exact (dyadic) computation: the copy process with
    n_V = 2 (three fair bits, a fixed present, the three bits again) has I(X_<3; X_>3 | X_3) = 3 bits,
    above 2 log2 n_V = 2, so eps_min(I*, n_V) does not exist; every one-step memory M_k is at most
    1 bit = log2 n_V there, so eps_min(M_k, n_V) exists at every order.
(3) Control for the chain-rule link: I(X_<t; X_>t | X_t) <= sum_{j>=t} M_j on random laws
    (float, tolerance 1e-12); and the same inequality is an equality-free bound, not an identity:
    some sampled law has strict inequality.
(4) C3 attainment, exact: at (n_V, |C_H|) = (2,2) and (3,2), a bijection under the uniform prior
    with M_1 = I* = log2|C_H| = 1 bit, every logarithm a log of a power of two.
"""
from fractions import Fraction as F
from itertools import product, permutations
from collections import defaultdict
from math import log2
import random

fails = 0
def check(cond, msg):
    global fails
    print(('PASS  ' if cond else 'FAIL  ') + msg)
    if not cond:
        fails += 1

# ---------- exact information quantities for dyadic laws ----------
def exact_log2(q):
    """log2 of a positive rational that is a power of two, exactly; None otherwise."""
    q = F(q)
    n, d = q.numerator, q.denominator
    if n & (n - 1) == 0 and d & (d - 1) == 0:
        return F(n.bit_length() - 1) - F(d.bit_length() - 1)
    return None

def marg(P, idx):
    out = defaultdict(F)
    for traj, p in P.items():
        out[tuple(traj[i] for i in idx)] += p
    return out

def cmi(P, A, B, C, exact=True):
    """I(X_A; X_B | X_C) for a law P on trajectories (dict tuple->prob)."""
    pabc, pac, pbc, pc = marg(P, A + B + C), marg(P, A + C), marg(P, B + C), marg(P, C)
    tot = F(0) if exact else 0.0
    nA, nB = len(A), len(B)
    for k, p in pabc.items():
        if p == 0:
            continue
        a, b, c = k[:nA], k[nA:nA + nB], k[nA + nB:]
        ratio = p * pc[c] / (pac[a + c] * pbc[b + c])
        if exact:
            l = exact_log2(ratio)
            if l is None:
                return None
            tot += p * l
        else:
            tot += float(p) * log2(float(ratio))
    return tot

# ---------- (1) the range of g ----------
def h2(e):
    return 0.0 if e in (0.0, 1.0) else -e * log2(e) - (1 - e) * log2(1 - e)
def g(e, n):
    return 2 * (e * (log2(n - 1) if n > 2 else 0.0) + h2(e))
ok_end, ok_mono = True, True
for n in range(2, 12):
    top = 1 - 1 / n
    ok_end &= abs(g(top, n) - 2 * log2(n)) < 1e-12
    grid = [top * i / 2000 for i in range(2001)]
    vals = [g(e, n) for e in grid]
    ok_mono &= all(vals[i] < vals[i + 1] for i in range(2000))
check(ok_end, '(1) g(1-1/n, n) = 2 log2 n for n = 2..11')
check(ok_mono, '(1) g strictly increasing on [0, 1-1/n] (2001-point grid, n = 2..11)')

# ---------- (2) the copy process ----------
P = {}
for b in product((0, 1), repeat=3):
    P[b + (0,) + b] = F(1, 8)  # X_0..X_2 fair bits, X_3 = 0, X_4..X_6 copy X_0..X_2
Istar_t3 = cmi(P, [0, 1, 2], [4, 5, 6], [3])
check(Istar_t3 == 3, f'(2) copy process: I(X_<3; X_>3 | X_3) = {Istar_t3} bits exactly')
check(Istar_t3 > 2 * 1, '(2) exceeds 2 log2 n_V = 2: eps_min(I*, 2) is undefined')
Ms = [cmi(P, list(range(k)), [k + 1], [k]) for k in range(1, 6)]
check(all(m is not None and m <= 1 for m in Ms), f'(2) every M_k <= log2 n_V = 1 (M_1..M_5 = {[str(m) for m in Ms]})')

# ---------- (3) chain-rule control ----------
random.seed(20261028)
worst, strict = -1.0, False
for trial in range(300):
    K, n = 4, 2 + trial % 2
    w = {traj: random.randint(1, 9) for traj in product(range(n), repeat=K + 1)}
    Z = sum(w.values())
    Q = {k: F(v, Z) for k, v in w.items()}
    for t in range(1, K):
        lhs = cmi(Q, list(range(t)), list(range(t + 1, K + 1)), [t], exact=False)
        rhs = sum(cmi(Q, list(range(j)), [j + 1], [j], exact=False) for j in range(t, K))
        worst = max(worst, lhs - rhs)
        strict |= rhs - lhs > 1e-6
check(worst <= 1e-12, f'(3) I(X_<t; X_>t | X_t) <= sum_j M_j on 300 random laws (max lhs-rhs = {worst:.2e})')
check(strict, '(3) the inequality is strict on some sampled law (it is a bound, not an identity)')

# ---------- (4) exact C3 attainment ----------
def visible_law(perm, nV, nH, K):
    """law of (X_0..X_K) from the uniform initial law on C_V x C_H under the bijection perm."""
    out = defaultdict(F)
    for x in range(nV):
        for hh in range(nH):
            s, traj = x * nH + hh, [x]
            for _ in range(K):
                s = perm[s]
                traj.append(s // nH)
            out[tuple(traj)] += F(1, nV * nH)
    return out

for nV, nH in [(2, 2), (3, 2)]:
    K, found = 3, None
    for perm in permutations(range(nV * nH)):
        L = visible_law(perm, nV, nH, K)
        m1 = cmi(L, [0], [2], [1])
        if m1 == 1:
            i1 = cmi(L, [0], [2, 3], [1])
            if i1 == 1:
                found = (perm, m1, i1)
                break
    check(found is not None,
          f'(4) ({nV},{nH}): bijection {found[0] if found else None} has M_1 = I(X_<1; X_>1 | X_1) = 1 = log2|C_H| exactly')

print('\nSC-40 checks:', 'ALL PASS' if fails == 0 else f'{fails} FAILED')
raise SystemExit(1 if fails else 0)
