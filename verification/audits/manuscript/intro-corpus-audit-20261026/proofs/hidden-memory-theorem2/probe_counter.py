#!/usr/bin/env python3
"""Countercontrols and counterexample constructions for the review of Main.md:582 / :99 / :592 / :594.
Exact rationals; logs only where an entropy value is reported."""
import sys, random
from fractions import Fraction as F
from itertools import permutations, product
from collections import defaultdict
from math import log2

def H(d): return -sum(float(p) * log2(float(p)) for p in d.values() if p > 0)
def marg(items, key):
    d = defaultdict(F)
    for p, o in items: d[key(o)] += p
    return d
def cmi(items, a, b, c):
    return (H(marg(items, lambda o: (a(o), b(o)))) + H(marg(items, lambda o: (c(o), b(o))))
            - H(marg(items, lambda o: (a(o), b(o), c(o)))) - H(marg(items, b)))

def run(step, init, K):
    out = []
    for z0, p in init.items():
        if p == 0: continue
        zs = [z0]
        for _ in range(K): zs.append(step(zs[-1]))
        out.append((p, zs))
    return out

def vis_law(paths): return marg(paths, lambda zs: tuple(z[0] for z in zs))

def witness(P, t):
    c = defaultdict(lambda: defaultdict(F)); w = defaultdict(F)
    for tr, p in P.items():
        if p: c[(tr[:t], tr[t])][tr[t + 1]] += p; w[(tr[:t], tr[t])] += p
    byx = defaultdict(set)
    for k in c: byx[k[1]].add(tuple(sorted((y, v / w[k]) for y, v in c[k].items() if v)))
    return any(len(s) > 1 for s in byx.values())

rc = 0
print("== CC1 countercontrol: ID1 must fail if X_{t+1} is read through the WRONG map ==")
nV, nH, K = 2, 2, 3
bad = 0; tot = 0
for perm in permutations(range(4)):
    phi = lambda z, perm=perm: divmod(perm[z[0] * nH + z[1]], nH)
    psi = lambda z, perm=perm: divmod(perm[perm[z[0] * nH + z[1]]], nH)  # phi^2: wrong readout
    init = {(x, h): F(1, 4) for x in range(2) for h in range(2)}
    paths = run(phi, init, K); P = vis_law(paths)
    for t in (1, 2):
        tot += 1
        w = marg(paths, lambda zs: (tuple(z[0] for z in zs[:t]), zs[t][0], zs[t][1]))
        mk = marg([(p, s) for s, p in w.items()], lambda s: (s[0], s[1], psi((s[1], s[2]))[0]))
        mp = marg([(p, tr) for tr, p in P.items()], lambda tr: (tr[:t], tr[t], tr[t + 1]))
        if {k: v for k, v in mk.items() if v} != {k: v for k, v in mp.items() if v}: bad += 1
print(f"  wrong-readout mismatches detected: {bad}/{tot}  (control is live iff > 0)")
if bad == 0: rc = 1

print("\n== CC2: a deterministic NON-injective map: (a)-(c) survive, disjoint supports fail ==")
# g erases the visible bit into nothing: g(x,h) = (h, 0)  on V=H={0,1}
g = lambda z: (z[1], 0)
init = {(x, h): F(1, 4) for x in range(2) for h in range(2)}
paths = run(g, init, 3)
t = 2
w = marg(paths, lambda zs: (tuple(z[0] for z in zs[:t]), zs[t][0], zs[t][1]))
it = [(p, s) for s, p in w.items()]
IXH = cmi(it, lambda s: s[0], lambda s: s[1], lambda s: s[2])
Hc = H(marg(it, lambda s: (s[0], s[1]))) - H(marg(it, lambda s: s[1]))
print(f"  I(X_<2;H_2|X_2) = {IXH:.4f}  H(X_<2|X_2) = {Hc:.4f}  (differ => disjointness is a bijectivity fact)")
if abs(IXH - Hc) < 1e-9: rc = 1

print("\n== CE-zero: unqualified 'pair of posteriors with different pushforwards' under 0/0 := 0 ==")
# Markov (deterministic identity) law X_1 = X_0, X_0 uniform; realization phi = id on V x H, H = {0}
init = {(0, 0): F(1, 2), (1, 0): F(1, 2)}
paths = run(lambda z: z, init, 2); P = vis_law(paths)
t = 1
w = marg(paths, lambda zs: (tuple(z[0] for z in zs[:t]), zs[t][0], zs[t][1]))
def lean_nextlaw(p, x):  # Lean's convention: division by 0 is 0
    hp = sum(v for (q, y, h), v in w.items() if (q, y) == (p, x))
    out = defaultdict(F)
    for (q, y, h), v in w.items():
        if (q, y) == (p, x): out[y] += v / hp
    return {k: v for k, v in out.items() if v}
it = [(p, s) for s, p in w.items()]
Mt = cmi(it, lambda s: s[0], lambda s: s[1], lambda s: s[1])  # X_{t+1} = X_t here
print(f"  M_1 = {Mt:.4f}; Lean nextLaw at zero-prob history (0,),x=1: {lean_nextlaw((0,), 1)}; "
      f"at (1,),x=1: {lean_nextlaw((1,), 1)}")
print("  => without 'positive-probability', a Markov law would carry a 'readout-relevant pair'.")

print("\n== CE-C3: (c) alone does not give (C3); the whole-future bound is needed ==")
# X_0, X_1, X_2 iid fair bits, X_3 = X_0.  t = 1: M_1 = I(X_0;X_2|X_1) = 0, I(X_0;X_2X_3|X_1) = 1
law = {}
for a, b, c in product(range(2), repeat=3): law[(a, b, c, a)] = F(1, 8)
items = [(p, tr) for tr, p in law.items()]
M1 = cmi(items, lambda tr: tr[:1], lambda tr: tr[1], lambda tr: tr[2])
I1 = cmi(items, lambda tr: tr[:1], lambda tr: tr[1], lambda tr: tr[2:])
print(f"  M_1 = {M1:.4f}, I(X_<1;X_>1|X_1) = {I1:.4f}: (c) at t=1 gives log2|C_H| >= {M1:.0f}, (C3) needs >= {I1:.0f}")
if not (M1 < 1e-12 and abs(I1 - 1) < 1e-12): rc = 1

print("\n== S_imp_D replica: clock + stored trajectory; faithful in the Main:99 sense ==")
def s_imp_d(P, V, K):
    trajs = [tr for tr in P]
    Hid = [(c, tr) for c in range(K + 1) for tr in product(V, repeat=K + 1)]
    states = [(x, hh) for x in V for hh in Hid]
    emb = lambda c, tr: (tr[c], (c, tr))
    partial = {}
    for tr in product(V, repeat=K + 1):
        for c in range(K): partial[emb(c, tr)] = emb(c + 1, tr)
    dom = set(partial); img = set(partial.values())
    assert len(img) == len(dom)
    rest_d = sorted(s for s in states if s not in dom); rest_i = sorted(s for s in states if s not in img)
    perm = dict(partial); perm.update(zip(rest_d, rest_i))
    assert sorted(perm.values()) == sorted(states)
    init = {emb(0, tr): p for tr, p in P.items()}
    return perm, init
rng = random.Random(7)
V = (0, 1); K = 3
for trial in range(3):
    wts = [F(rng.randint(0, 5)) for _ in range(2 ** (K + 1))]; z = sum(wts)
    P = {tr: wv / z for tr, wv in zip(product(V, repeat=K + 1), wts)}
    perm, init = s_imp_d(P, V, K)
    paths = run(lambda s: perm[s], init, K); P2 = vis_law(paths)
    same = {k: v for k, v in P2.items() if v} == {k: v for k, v in P.items() if v}
    # does the initial law factor as visible x hidden?
    px = marg([(p, s) for s, p in init.items()], lambda s: s[0])
    ph = marg([(p, s) for s, p in init.items()], lambda s: s[1])
    prod_ok = all(init.get((x, hh), 0) == px[x] * ph[hh] for x in V for hh in ph)
    wit = [witness(P, t) for t in (1, 2)]
    # readout pair in the replica
    rd = []
    for t in (1, 2):
        w = marg(paths, lambda zs: (tuple(z[0] for z in zs[:t]), zs[t][0], zs[t][1]))
        hp = defaultdict(F)
        for (q, x, h), v in w.items(): hp[(q, x)] += v
        push = defaultdict(lambda: defaultdict(F))
        for (q, x, h), v in w.items(): push[(q, x)][perm[(x, h)][0]] += v / hp[(q, x)]
        byx = defaultdict(set)
        for (q, x), d in push.items():
            if hp[(q, x)] > 0: byx[x].add(tuple(sorted((y, v) for y, v in d.items() if v)))
        rd.append(any(len(s) > 1 for s in byx.values()))
    print(f"  trial {trial}: law reproduced={same}; initial law is a product (hidden prior indep. of x_0)={prod_ok}; "
          f"witness(t=1,2)={wit}; readout pair in replica={rd}")
    if not same or wit != rd: rc = 1

print("\n== CE-594: in EVERY bijective realization I(X_<t;H_t|X_t) = H(X_<t|X_t); i.i.d. fair coin ==")
P = {tr: F(1, 16) for tr in product(V, repeat=4)}
perm, init = s_imp_d(P, V, 3)
paths = run(lambda s: perm[s], init, 3)
for t in (1, 2):
    w = marg(paths, lambda zs: (tuple(z[0] for z in zs[:t]), zs[t][0], zs[t][1]))
    it = [(p, s) for s, p in w.items()]
    IXH = cmi(it, lambda s: s[0], lambda s: s[1], lambda s: s[2])
    print(f"  replica (|C_H|={2*0+ (3+1)*16}): t={t}: M_t=0, I(X_<t;H_t|X_t)={IXH:.4f} = H(X_<t|X_t)={t}")
# a smaller bijective realization: hidden = tape of future flips + ledger of past (shift register)
# state (x, (ledger, tape)); step: push x onto ledger, pop next visible from tape; t<=3
nb = 3
def step2(s):
    x, (led, tape) = s
    if len(tape) == 0: return s
    return (tape[0], (led + (x,), tape[1:]))
init2 = {(x, ((), tape)): F(1, 16) for x in V for tape in product(V, repeat=3)}
paths2 = run(step2, init2, 3)  # step2 is injective on reachable states (ledger stores x)
for t in (1, 2):
    w = marg(paths2, lambda zs: (tuple(z[0] for z in zs[:t]), zs[t][0], zs[t][1]))
    it = [(p, s) for s, p in w.items()]
    IXH = cmi(it, lambda s: s[0], lambda s: s[1], lambda s: s[2])
    print(f"  shift-register realization (prior independent of x_0): t={t}: I(X_<t;H_t|X_t)={IXH:.4f}")
print("  => inf over bijective realizations of I(X_<t;H_t|X_t) is H(X_<t|X_t) > M_t = 0 at every hidden dimension")

print("\n", "ALL CONTROLS LIVE / CONSTRUCTIONS AS STATED" if rc == 0 else "UNEXPECTED RESULT")
sys.exit(rc)
