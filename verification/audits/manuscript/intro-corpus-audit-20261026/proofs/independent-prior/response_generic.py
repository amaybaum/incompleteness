#!/usr/bin/env python3
"""Response-table extension: (1) GENERIC symbolic check -- every kernel entry an independent
indeterminate, so equality is a polynomial identity valid for every real kernel at once
(n=2,K=2 and n=3,K=1); (2) n=2,K=3 and n=3,K=2 with rational non-uniform kernels (Fractions),
including zero entries, bijection on the full product (n=2,K=3) / injectivity on the domain."""
import itertools, sys
import sympy as sp
from fractions import Fraction as F
sys.path.insert(0, __import__('os').path.dirname(__file__))
PAD = -1

def contexts(n, K):
    return [p for k in range(K) for p in itertools.product(range(n), repeat=k + 1)]

def run(n, K, kern, one, full_bijection=True):
    ctx = contexts(n, K); idx = {c: i for i, c in enumerate(ctx)}
    tables = list(itertools.product(range(n), repeat=len(ctx)))
    ledgers = list(itertools.product(list(range(n)) + [PAD], repeat=K))
    wf = lambda L, c: all(L[i] != PAD for i in range(c)) and all(L[i] == PAD for i in range(c, K))
    dom = [(x, L, u, c) for x in range(n) for L in ledgers if True for u in range(len(tables))
           for c in range(K) if wf(L, c)]
    step = lambda st: (tables[st[2]][idx[tuple(st[1][:st[3]]) + (st[0],)]],
                       tuple(st[1][:st[3]]) + (st[0],) + (PAD,) * (K - st[3] - 1), st[2], st[3] + 1)
    imgs = set(step(s) for s in dom)
    assert len(imgs) == len(dom), "partial step not injective"
    if full_bijection:
        states = [(x, L, u, c) for x in range(n) for L in ledgers for u in range(len(tables)) for c in range(K + 1)]
        S = set(states); dset = set(dom)
        assert len(S - dset) == len(S - imgs)      # completion exists (equal-size complements)
    prior = []
    for u in range(len(tables)):
        w = one
        for i, c in enumerate(ctx): w = w * kern(c)[tables[u][i]]
        prior.append(w)
    for x0 in range(n):
        R = {}
        for u, w in enumerate(prior):
            if w == 0: continue
            st = (x0, (PAD,) * K, u, 0); tail = []
            for _ in range(K): st = step(st); tail.append(st[0])
            R[tuple(tail)] = R.get(tuple(tail), 0) + w
        for tail in itertools.product(range(n), repeat=K):
            tr = (x0,) + tail; p = one
            for j in range(K): p = p * kern(tr[:j + 1])[tr[j + 1]]
            d = R.get(tail, 0) - p
            if isinstance(d, sp.Basic): d = sp.expand(d)
            assert d == 0, (x0, tail, d)
    return len(ctx), len(dom)

# (1) generic symbolic
def gen_kernel(n, K):
    syms = {}
    for c in contexts(n, K):
        s = sp.symbols(f"p_{''.join(map(str, c))}_0:{n - 1}")
        syms[c] = tuple(s) + (1 - sum(s),)
    return lambda c: syms[tuple(c)]
for n, K in [(2, 1), (2, 2), (3, 1)]:
    C, d = run(n, K, gen_kernel(n, K), sp.Integer(1))
    print(f"GENERIC n={n} K={K}: {C} contexts, kernel entries free indeterminates -> joint identity holds as a POLYNOMIAL identity (all real kernels)")

# (2) rational non-uniform, zeros, larger K
def kq(c):
    k = len(c) - 1; h = sum(c) % 3
    tab = {0: (F(1, 7), F(6, 7)), 1: (F(0), F(1)), 2: (F(5, 9), F(4, 9))}
    return tab[(h + k) % 3]
C, d = run(2, 3, kq, F(1))
print(f"rational n=2 K=3: {C} contexts, domain {d}: injective, completion exists, full joint exact")
def kq3(c):
    h = (sum(c) + len(c)) % 3
    return [(F(1, 2), F(1, 3), F(1, 6)), (F(0), F(1, 5), F(4, 5)), (F(1), F(0), F(0))][h]
C, d = run(3, 2, kq3, F(1), full_bijection=False)
print(f"rational n=3 K=2: {C} contexts, domain {d}: injective, full joint exact")
print("response_generic: COMPLETE")
