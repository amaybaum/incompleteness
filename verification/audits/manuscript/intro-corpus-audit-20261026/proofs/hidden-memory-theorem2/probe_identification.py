#!/usr/bin/env python3
"""Independent review probe for Main.md:582 (unavoidable hidden predictive memory) and the
Corollary at Main.md:99.  Exact rational arithmetic throughout; logs only for the CMI values,
which are compared against an exact (rational) criterion as an independent control.

For every bijection phi of C_V x C_H at (nV,nH) in {(2,2),(2,3),(3,2)} and a family of initial laws
on C_V x C_H (uniform, product non-uniform, hidden point mass, and several CORRELATED laws), run the
realization from time 0 to horizon K and check, for every t in 1..K-1:

 ID1  the kernel's sample space (X_<t, X_t, H_t) with X_{t+1} := pi_V phi(X_t,H_t) has exactly the
      (X_<t, X_t, X_{t+1}) marginal of the path law  -> memory R = M_t(P)   [time-t identification]
 ID2  kernel nextLaw (computed from w and phi) == P(X_{t+1} | X_<t, X_t) of the path law, exactly
 A    pushforward identity, B  TV floor, C  capacity floor (float, tol 1e-12)
 DIS  posteriors of distinct positive-probability histories sharing x_t have DISJOINT supports,
      equivalently X_<t is a function of (X_t, H_t) on the support, so I(X_<t;H_t|X_t)=H(X_<t|X_t)
 COR  witness(P,t) [exact]  <=>  readout-relevant pair in R [exact]  <=>  M_t > 0 [float]
 C1   readout-relevant pair at (t,x)  =>  f_x non-constant on supp(H_t | X_t = x)
"""
import sys, random
from fractions import Fraction as F
from itertools import permutations, product
from collections import defaultdict
from math import log2

K = 3

def priors(nV, nH, rng):
    S = [(x, h) for x in range(nV) for h in range(nH)]
    out = {}
    out['uniform'] = {s: F(1, len(S)) for s in S}
    vx = [F(i + 1) for i in range(nV)]; vh = [F(2 * j + 1) for j in range(nH)]
    zx, zh = sum(vx), sum(vh)
    out['product'] = {(x, h): vx[x] / zx * vh[h] / zh for (x, h) in S}
    out['hidden_point'] = {(x, h): (F(1, nV) if h == 0 else F(0)) for (x, h) in S}
    # correlated: hidden coordinate tied to visible coordinate, plus random rational laws
    out['corr_diag'] = {(x, h): (F(1, nV) if h == x % nH else F(0)) for (x, h) in S}
    for r in range(3):
        wts = [F(rng.randint(0, 6)) for _ in S]
        if sum(wts) == 0: wts[0] = F(1)
        z = sum(wts)
        out[f'rand{r}'] = {s: w / z for s, w in zip(S, wts)}
    return out

def run(perm, nV, nH, init):
    """state trajectories from time 0; returns list of (prob, [z_0..z_K])"""
    phi = lambda z: divmod(perm[z[0] * nH + z[1]], nH)
    paths = []
    for z0, p in init.items():
        if p == 0: continue
        zs = [z0]
        for _ in range(K): zs.append(phi(zs[-1]))
        paths.append((p, zs))
    return paths, phi

def H(dist):
    return -sum(float(p) * log2(float(p)) for p in dist.values() if p > 0)

def marg(items, key):
    d = defaultdict(F)
    for p, o in items: d[key(o)] += p
    return d

def cmi(items, a, b, c):
    """I(a; c | b) via the kernel's entropy formula H(A,B)+H(C,B)-H(A,B,C)-H(B)"""
    return (H(marg(items, lambda o: (a(o), b(o)))) + H(marg(items, lambda o: (c(o), b(o))))
            - H(marg(items, lambda o: (a(o), b(o), c(o)))) - H(marg(items, b)))

def cmi_kl(items, a, b, c):
    """independent control: I(a;c|b) = sum_b P(b) sum_a P(a|b) KL(P(c|a,b) || P(c|b))"""
    jab = marg(items, lambda o: (a(o), b(o))); jb = marg(items, b)
    jabc = marg(items, lambda o: (a(o), b(o), c(o))); jbc = marg(items, lambda o: (b(o), c(o)))
    tot = 0.0
    for (av, bv, cv), p in jabc.items():
        if p == 0: continue
        pc_ab = p / jab[(av, bv)]; pc_b = jbc[(bv, cv)] / jb[bv]
        tot += float(p) * log2(float(pc_ab) / float(pc_b))
    return tot

fails = defaultdict(int); counts = defaultdict(int)
tally = defaultdict(int)
rng = random.Random(20261027)
for nV, nH in [(2, 2), (2, 3), (3, 2)]:
    pri = priors(nV, nH, rng)
    for perm in permutations(range(nV * nH)):
        for pname, init in pri.items():
            paths, phi = run(perm, nV, nH, init)
            f = lambda x, h: phi((x, h))[0]
            # path law of the visible trajectory
            P = marg(paths, lambda zs: tuple(z[0] for z in zs))
            for t in range(1, K):
                counts['cases'] += 1
                # --- path-law side
                vis_items = [(p, tr) for tr, p in P.items()]
                Pcond = defaultdict(lambda: defaultdict(F)); Pw = defaultdict(F)
                for tr, p in P.items():
                    key = (tr[:t], tr[t]); Pcond[key][tr[t + 1]] += p; Pw[key] += p
                # --- kernel side: w on (X_<t, X_t, H_t); X_{t+1} DEFINED as f(X_t, H_t)
                w = defaultdict(F)
                for p, zs in paths:
                    w[(tuple(z[0] for z in zs[:t]), zs[t][0], zs[t][1])] += p
                witems = [(p, s) for s, p in w.items()]
                # ID1: (X_<t, X_t, X_{t+1}) marginals agree exactly
                m_kernel = marg(witems, lambda s: (s[0], s[1], f(s[1], s[2])))
                m_path = marg(vis_items, lambda tr: (tr[:t], tr[t], tr[t + 1]))
                if {k: v for k, v in m_kernel.items() if v} != {k: v for k, v in m_path.items() if v}:
                    fails['ID1'] += 1
                # posteriors and pushforwards (kernel definitions)
                hp = defaultdict(F)
                for (hist, x, h), p in w.items(): hp[(hist, x)] += p
                post = {}; push = {}
                for (hist, x, h), p in w.items():
                    post.setdefault((hist, x), defaultdict(F))[h] += p / hp[(hist, x)]
                for key, mu in post.items():
                    pf = defaultdict(F)
                    for h, v in mu.items(): pf[f(key[1], h)] += v
                    push[key] = pf
                    # ID2 / A: kernel nextLaw == path-law conditional
                    nl = defaultdict(F)
                    for (hist, x, h), p in w.items():
                        if (hist, x) == key: nl[f(x, h)] += p / hp[key]
                    pc = {y: v / Pw[key] for y, v in Pcond[key].items()}
                    if {k: v for k, v in nl.items() if v} != {k: v for k, v in pc.items() if v}:
                        fails['ID2'] += 1
                    if {k: v for k, v in pf.items() if v} != {k: v for k, v in nl.items() if v}:
                        fails['A'] += 1
                # B, DIS, witness, readout pair, C1
                keys = [k for k in post if hp[k] > 0]
                witness = readout = False
                for i in range(len(keys)):
                    for j in range(i + 1, len(keys)):
                        k1, k2 = keys[i], keys[j]
                        if k1[1] != k2[1]: continue
                        x = k1[1]
                        tvh = sum(abs(post[k1].get(h, 0) - post[k2].get(h, 0)) for h in range(nH)) / 2
                        tvv = sum(abs(push[k1].get(y, 0) - push[k2].get(y, 0)) for y in range(nV)) / 2
                        if tvv > tvh: fails['B'] += 1
                        if set(h for h, v in post[k1].items() if v) & set(h for h, v in post[k2].items() if v):
                            fails['DIS'] += 1
                        pc1 = {y: v / Pw[k1] for y, v in Pcond[k1].items() if v}
                        pc2 = {y: v / Pw[k2] for y, v in Pcond[k2].items() if v}
                        if pc1 != pc2: witness = True
                        if {a: b for a, b in push[k1].items() if b} != {a: b for a, b in push[k2].items() if b}:
                            readout = True
                            supp = set(h for h, v in post[k1].items() if v) | set(h for h, v in post[k2].items() if v)
                            if len(set(f(x, h) for h in supp)) < 2: fails['C1'] += 1
                Mt = cmi(witems, lambda s: s[0], lambda s: s[1], lambda s: f(s[1], s[2]))
                Mt_kl = cmi_kl(vis_items, lambda tr: tr[:t], lambda tr: tr[t], lambda tr: tr[t + 1])
                if abs(Mt - Mt_kl) > 1e-9: fails['CMI-formula-vs-KL'] += 1
                IXH = cmi(witems, lambda s: s[0], lambda s: s[1], lambda s: s[2])
                Hcond = H(marg(witems, lambda s: (s[0], s[1]))) - H(marg(witems, lambda s: s[1]))
                if not (Mt <= IXH + 1e-12 and IXH <= log2(nH) + 1e-12): fails['C'] += 1
                if abs(IXH - Hcond) > 1e-9: fails['I(X<t;H|X)=H(X<t|X)'] += 1
                if witness != readout: fails['COR witness<->readout'] += 1
                if witness != (Mt > 1e-12): fails['COR witness<->M_t>0'] += 1
                tally[('M_t>0', witness)] += 1
                if not witness and IXH > 1e-12: tally['M_t=0 but I(X<t;H_t|X_t)>0'] += 1
print("cases (bijection x prior x t):", counts['cases'])
print("tally:", dict(tally))
for k in ['ID1', 'ID2', 'A', 'B', 'C', 'DIS', 'I(X<t;H|X)=H(X<t|X)', 'C1',
          'COR witness<->readout', 'COR witness<->M_t>0', 'CMI-formula-vs-KL']:
    print(f"  {k:28s} failures: {fails[k]}")
# controls: the checks must be able to fail
ok = all(fails[k] == 0 for k in fails)
print("ALL CHECKS PASS" if ok else "FAILURES PRESENT")
sys.exit(0 if ok else 1)
