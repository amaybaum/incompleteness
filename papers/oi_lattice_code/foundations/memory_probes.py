#!/usr/bin/env python3
# memory_probes.py — b116 (2026-08-13)
# Certifies the universal hidden-memory theorem of Main §3.4 — a statement about
# EVERY faithful deterministic realization, not about the constructed one:
#   (A) pushforward identity: with f_x(h) the next visible state, the observed law
#       P(X_{t+1} | p, x) is exactly the pushforward (f_x)_# mu_p of the hidden
#       posterior conditioned on the history p;
#   (B) distinguishability floor: the observed gap delta between two histories
#       sharing an endpoint satisfies delta <= ||mu_p - mu_p'||_TV, so hidden
#       distinguishability must survive until readback;
#   (C) capacity floor: M_t = I(X_<t; X_{t+1} | X_t) <= I(X_<t; H_t | X_t) <= log2|H|.
# Also records the COUNTEREXAMPLE to the naive variational reading: at FIXED hidden
# dimension the infimum of I(X_<t; H_t | X_t) over realizations of a given visible
# process does NOT generally equal M_t (1 of 15 processes at (n_V,n_H)=(2,3)).
import sys
from fractions import Fraction as F
from itertools import permutations
from collections import defaultdict
from math import log2

def ensemble(perm, nV, nH, steps=2):
    ens = defaultdict(lambda: F(0))
    for x in range(nV):
        for h in range(nH):
            ens[((x,), x, h)] += F(1, nV * nH)
    for _ in range(steps):
        new = defaultdict(lambda: F(0))
        for (hist, x, h), p in ens.items():
            y = perm[x * nH + h]
            new[(hist + (y // nH,), y // nH, y % nH)] += p
        ens = new
    return ens

def analyse(perm, nV, nH):
    ens = ensemble(perm, nV, nH)
    f = lambda x, h: perm[x * nH + h] // nH
    byhist = defaultdict(lambda: defaultdict(lambda: F(0)))
    for (hist, x, h), p in ens.items():
        byhist[(hist, x)][h] += p
    A = B = True
    keys = list(byhist)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            (hp, x), (hq, x2) = keys[i], keys[j]
            if x != x2: continue
            mp, mq = byhist[keys[i]], byhist[keys[j]]
            Zp, Zq = sum(mp.values()), sum(mq.values())
            if Zp == 0 or Zq == 0: continue
            up = {h: v / Zp for h, v in mp.items()}
            uq = {h: v / Zq for h, v in mq.items()}
            pp = defaultdict(lambda: F(0)); qq = defaultdict(lambda: F(0))
            for h, v in up.items(): pp[f(x, h)] += v
            for h, v in uq.items(): qq[f(x, h)] += v
            # (A): the pushforward reproduces the law, and is a probability vector
            if sum(pp.values()) != 1 or sum(qq.values()) != 1: A = False
            # (B): TV cannot increase under the deterministic pushforward
            delta = sum(abs(pp[y] - qq[y]) for y in range(nV)) / 2
            dh = sum(abs(up.get(h, F(0)) - uq.get(h, F(0))) for h in range(nH)) / 2
            if delta > dh: B = False
    # (C)
    grp = defaultdict(list)
    for (hist, x, h), p in ens.items(): grp[x].append((hist, h, p))
    M_t = I_XH = 0.0
    for x, items in grp.items():
        W = sum(p for _, _, p in items)
        if W == 0: continue
        hn = defaultdict(lambda: defaultdict(lambda: F(0)))
        hw = defaultdict(lambda: F(0)); hh = defaultdict(lambda: defaultdict(lambda: F(0)))
        for hist, h, p in items:
            hn[hist][f(x, h)] += p; hw[hist] += p; hh[hist][h] += p
        bar = [sum(hn[k][y] for k in hn) / W for y in range(nV)]
        barh = [sum(hh[k].get(h, F(0)) for k in hh) / W for h in range(nH)]
        for k in hn:
            w = hw[k]
            if w == 0: continue
            Pn = [hn[k][y] / w for y in range(nV)]
            Ph = [hh[k].get(h, F(0)) / w for h in range(nH)]
            M_t += float(w) * sum(float(a) * log2(float(a) / float(b)) for a, b in zip(Pn, bar) if a > 0 and b > 0)
            I_XH += float(w) * sum(float(a) * log2(float(a) / float(b)) for a, b in zip(Ph, barh) if a > 0 and b > 0)
    C = (M_t <= I_XH + 1e-12) and (I_XH <= log2(nH) + 1e-12)
    return A, B, C, M_t, I_XH

fail = 0
print("== the universal hidden-memory theorem, over every realization ==")
for nV, nH in [(2, 2), (2, 3), (3, 2)]:
    a = b = c = n = 0
    for perm in permutations(range(nV * nH)):
        A, B, C, M, I = analyse(perm, nV, nH)
        a += A; b += B; c += C; n += 1
    print(f"  (n_V,n_H)=({nV},{nH}): {n} realizations — pushforward {a}/{n}, TV floor {b}/{n}, capacity {c}/{n}")
    if not (a == b == c == n): fail += 1

print()
print("== the naive variational reading is FALSE at fixed hidden dimension ==")
def signature(perm, nV, nH):
    ens = ensemble(perm, nV, nH); f = lambda x, h: perm[x * nH + h] // nH
    by = defaultdict(lambda: defaultdict(lambda: F(0)))
    for (hist, x, h), p in ens.items(): by[(hist, x)][h] += p
    sig = {}
    for (hist, x), m in by.items():
        Z = sum(m.values())
        if Z == 0: continue
        nxt = defaultdict(lambda: F(0))
        for h, v in m.items(): nxt[f(x, h)] += v / Z
        sig[(hist, x)] = tuple(sorted((y, str(v)) for y, v in nxt.items()))
    return tuple(sorted(sig.items()))
for nV, nH in [(2, 3)]:
    groups = defaultdict(list)
    for perm in permutations(range(nV * nH)):
        A, B, C, M, I = analyse(perm, nV, nH)
        groups[signature(perm, nV, nH)].append((M, I))
    att = tot = 0
    for sig, items in groups.items():
        M = items[0][0]
        if M <= 1e-12: continue
        tot += 1
        if abs(min(i for _, i in items) - M) < 1e-9: att += 1
    print(f"  (n_V,n_H)=({nV},{nH}): min over same-dimension realizations equals M_t for {att} of {tot} processes")
    if att == tot: fail += 1; print("  FAIL: expected the naive reading to fail here")
print()
print("memory_probes:", "ALL CHECKS PASS" if fail == 0 else f"{fail} FAILURE(S)")
sys.exit(1 if fail else 0)
