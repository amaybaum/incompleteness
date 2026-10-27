#!/usr/bin/env python3
"""Independent re-implementation of Main.md:498 (response-table extension), exact symbolic.

State: (x, ledger, u, clock); u = (u_c)_c over contexts c = (x_0..x_k), 0 <= k < K;
prior mu(u) = prod_c kern_c(u_c) on {ledger blank, clock 0}; step x' = u_{c(ledger, x)}.
Kernels contain irrational entries (sqrt2, pi) and zeros; some contexts have probability 0.

Checks: A bijection of the full product; B prior normalised (symbolically) and x0-free;
C every root, every k <= K, every joint point equal to the kernel chain (sympy simplify == 0);
E countercontrol: a prior that correlates two contexts (non-product, same one-context
marginals) must FAIL to reproduce a law where both contexts lie on one trajectory.
"""
import itertools
import sympy as sp

PAD = -1
r2, pi = sp.sqrt(2), sp.pi

def contexts(n, K):
    return [p for k in range(K) for p in itertools.product(range(n), repeat=k + 1)]

def build(kern, n, K, prior_fn=None):
    ctx = contexts(n, K)
    tables = list(itertools.product(range(n), repeat=len(ctx)))
    ledgers = list(itertools.product(list(range(n)) + [PAD], repeat=K))
    wf = lambda L, c: all(L[i] != PAD for i in range(c)) and all(L[i] == PAD for i in range(c, K))
    idx = {c: i for i, c in enumerate(ctx)}
    states = [(x, L, u, c) for x in range(n) for L in ledgers for u in range(len(tables)) for c in range(K + 1)]
    part = {}
    for (x, L, u, c) in states:
        if c < K and wf(L, c):
            past = tuple(L[:c]) + (x,)
            part[(x, L, u, c)] = (tables[u][idx[past]], tuple(L[:c]) + (x,) + (PAD,) * (K - c - 1), u, c + 1)
    imgs = list(part.values())
    assert len(set(imgs)) == len(imgs), "A: partial step not injective"
    dc, ic = sorted(set(states) - set(part)), sorted(set(states) - set(imgs))
    phi = dict(part); phi.update(zip(dc, ic))
    assert set(phi.values()) == set(states) and len(phi) == len(states), "A: not a bijection"
    if prior_fn is None:
        prior = {u: sp.Mul(*[kern(ctx[i])[tables[u][i]] for i in range(len(ctx))]) for u in range(len(tables))}
    else:
        prior = prior_fn(ctx, tables)
    tot = sp.nsimplify(sp.simplify(sum(prior.values())))
    assert sp.simplify(tot - 1) == 0, "B: prior not normalised"
    assert all(sp.simplify(w) >= 0 for w in prior.values()), "B: negative prior weight"
    return phi, prior, len(states), len(ctx)

def realized(phi, prior, n, K, x0, k):
    out = {}
    for u, w in prior.items():
        if w == 0: continue
        st = (x0, (PAD,) * K, u, 0); tail = []
        for _ in range(k):
            st = phi[st]; tail.append(st[0])
        out[tuple(tail)] = out.get(tuple(tail), 0) + w
    return out

def target(kern, n, x0, k):
    out = {}
    for tail in itertools.product(range(n), repeat=k):
        tr = (x0,) + tail; p = sp.Integer(1)
        for j in range(k): p *= kern(tr[:j + 1])[tr[j + 1]]
        out[tail] = p
    return out

def compare(phi, prior, kern, n, K):
    for x0 in range(n):
        for k in range(K + 1):
            R, T = realized(phi, prior, n, K, x0, k), target(kern, n, x0, k)
            for key in set(R) | set(T):
                if sp.simplify(sp.expand(R.get(key, 0) - T.get(key, 0))) != 0:
                    return False, (x0, k, key, R.get(key, 0), T.get(key, 0))
    return True, None

# irrational, non-Markov, zeros; root x0 = 1 forbids x1 = 0, so context (1,0) has probability 0
a = r2 / 2
b = pi / 4
def kern1(p):
    c = len(p) - 1
    if c == 0: return (a, 1 - a) if p[0] == 0 else (sp.Integer(0), sp.Integer(1))
    if p[0] == p[1]: return (b, 1 - b)
    return (1 - a, a)
for (n, K, kern, name) in [(2, 1, kern1, "irrational K=1"), (2, 2, kern1, "irrational non-Markov w/ zero contexts K=2")]:
    phi, prior, S, C = build(kern, n, K)
    ok, why = compare(phi, prior, kern, n, K)
    assert ok, why
    print(f"{name}: n={n} K={K} contexts={C} |S|={S}: bijection OK, prior normalised, all roots/all k<=K/all joints EXACT")

# n = 3, K = 1 with irrational kernel
def kern3(p):
    if p[0] == 0: return (a / 2, 1 - a, a / 2)
    if p[0] == 1: return (b, sp.Integer(0), 1 - b)
    return (sp.Integer(1) / 3, sp.Integer(1) / 3, sp.Integer(1) / 3)
phi, prior, S, C = build(kern3, 3, 1)
ok, why = compare(phi, prior, kern3, 3, 1); assert ok, why
print(f"irrational n=3 K=1: |S|={S}: EXACT")

# countercontrol: correlate contexts (0,) and (0,0) -- both on the trajectory 0 -> 0 -> .
def corr_prior(kern):
    def f(ctx, tables):
        i0, i1 = ctx.index((0,)), ctx.index((0, 0))
        base = {u: sp.Mul(*[kern(ctx[i])[tables[u][i]] for i in range(len(ctx)) if i not in (i0, i1)]) for u in range(len(tables))}
        # joint of (u_(0), u_(0,0)) with the declared one-context marginals but correlated
        p0 = kern(ctx[i0]); p1 = kern(ctx[i1])
        eps = sp.Rational(1, 20)
        J = {(y0, y1): p0[y0] * p1[y1] + (eps if y0 == y1 else -eps) for y0 in range(2) for y1 in range(2)}
        return {u: base[u] * J[(tables[u][i0], tables[u][i1])] for u in range(len(tables))}
    return f
phi, prior, S, C = build(kern1, 2, 2, prior_fn=corr_prior(kern1))
ok, why = compare(phi, prior, kern1, 2, 2)
assert not ok, "E: correlated-prior countercontrol did not fail"
print("E: non-product prior with correct one-context marginals FAILS on the joint (control live):", why[:3])
print("response_check: COMPLETE")
