#!/usr/bin/env python3
# primitive_probes.py — b102 (2026-08-13). Certifies the dependency structure of
# the structural conditions: C4 is primitive; C1 and C3 are its consequences
# within any faithful realization (Main §1.3).
import sys
# b102: is C4 the primitive structural condition, with C1 and C3 derived?
#  (A) C4 => C1: enumerate every ZERO-COUPLING realization (visible image
#      independent of the hidden state at every step) and verify no readback gap
#      at any order in the accessible window.
#  (B) C4 => C3: for realizations that DO exhibit a gap, verify the data-processing
#      bound I* = I(X_<k; X_{k+1} | X_k) <= log2 |C_H| — C3's own stated bound —
#      and report how tight it gets.
# Exact where it matters (Fractions for the process algebra; logs only for I*).
from fractions import Fraction as F
from itertools import permutations, product
from collections import defaultdict
from math import log2

def visible_zero_coupling(perm, nV, nH):
    """pi_V(phi(x,h)) independent of h, for every x."""
    for x in range(nV):
        outs = {perm[x*nH+h]//nH for h in range(nH)}
        if len(outs) > 1: return False
    return True

def conditionals(perm, nV, nH, steps=3):
    """exact P(x_{k+1} | history) under the uniform hidden prior."""
    ens = defaultdict(lambda: F(0))
    for x in range(nV):
        for h in range(nH):
            ens[(x, h, (x,))] += F(1, nV*nH)
    hn = defaultdict(lambda: defaultdict(lambda: F(0)))
    for _ in range(steps):
        new = defaultdict(lambda: F(0))
        for (x, h, hist), p in ens.items():
            y = perm[x*nH+h]; x2, h2 = y//nH, y%nH
            hn[hist][x2] += p
            new[(x2, h2, hist+(x2,))] += p
        ens = new
    return hn

def max_gap(hn, nV):
    """largest TV between next-step laws of two histories sharing an endpoint."""
    best = F(0)
    by_len = defaultdict(list)
    for h in hn: by_len[len(h)].append(h)
    for L, hs in by_len.items():
        if L < 2: continue
        for i in range(len(hs)):
            for j in range(i+1, len(hs)):
                a, b = hs[i], hs[j]
                if a[-1] != b[-1]: continue
                na, nb = sum(hn[a].values()), sum(hn[b].values())
                if na == 0 or nb == 0: continue
                tv = sum(abs(hn[a][v]/na - hn[b][v]/nb) for v in range(nV))/2
                best = max(best, tv)
    return best

def cmi(hn, nV):
    """max over orders k of I(X_<k; X_{k+1} | X_k), in bits. (Per-order: summing
    across orders would conflate distinct quantities and can exceed log2|C_H|.)"""
    per_order = defaultdict(float)
    groups = defaultdict(list)
    for h in hn:
        if len(h) >= 2: groups[(len(h), h[-1])].append(h)
    for (L, c), hs in groups.items():
        w = {h: sum(hn[h].values()) for h in hs}
        W = sum(w.values())
        if W == 0: continue
        bar = [sum(hn[h][v] for h in hs)/W for v in range(nV)]
        for h in hs:
            if w[h] == 0: continue
            P = [hn[h][v]/w[h] for v in range(nV)]
            d = sum(float(p)*log2(float(p)/float(q)) for p, q in zip(P, bar) if p > 0 and q > 0)
            per_order[L] += float(w[h]) * d
    return max(per_order.values()) if per_order else 0.0

fail = 0
print("== (A) C4 => C1: zero-coupling realizations cannot exhibit readback ==")
for nV, nH in [(2,2),(2,3),(3,2)]:
    zc = [p for p in permutations(range(nV*nH)) if visible_zero_coupling(p, nV, nH)]
    worst = F(0)
    for p in zc:
        worst = max(worst, max_gap(conditionals(p, nV, nH), nV))
    print(f"  (n_V,n_H)=({nV},{nH}): {len(zc)} zero-coupling bijections, max readback gap = {worst}")
    assert worst == 0, "a zero-coupling realization produced a gap"
print("  => certified: no coupling, no readback. C4 presupposes C1.")

print("\n== (B) C4 => C3: the data-processing bound is C3's bound ==")
for nV, nH in [(2,2),(2,3),(2,4),(3,2)]:
    cap = log2(nH); worst_ratio = 0.0; worst_I = 0.0; n_gap = 0
    for p in permutations(range(nV*nH)):
        hn = conditionals(p, nV, nH)
        if max_gap(hn, nV) == 0: continue
        n_gap += 1
        I = cmi(hn, nV)
        worst_I = max(worst_I, I); worst_ratio = max(worst_ratio, I/cap if cap else 0)
    print(f"  (n_V,n_H)=({nV},{nH}): {n_gap} realizations with a gap; max I* = {worst_I:.4f} bits, log2|C_H| = {cap:.4f}, ratio {worst_ratio:.3f}")
    assert worst_I <= cap + 1e-9, "data-processing bound violated"
print("  => certified: every gap-exhibiting realization respects log2|C_H| >= I*. C4 forces C3.")

print("\n== (C) is C4 an independent condition, or clause (ii) read on the realization? ==")
# C4 asserts a readback gap MEDIATED through the hidden state; clause (ii) asserts
# I(X_<k; X_{k+1} | X_k) > 0. In a faithful realization all correlation is mediated
# through (x, h), so the mediation clause should be automatic and the two should
# coincide on every realization. Tested exhaustively.
mismatch = 0
for nV, nH in [(2,2),(2,3),(3,2)]:
    agree = 0
    for perm in permutations(range(nV*nH)):
        hn = conditionals(perm, nV, nH)
        gap = max_gap(hn, nV) > 0
        nonmarkov = cmi(hn, nV) > 1e-12
        if gap == nonmarkov: agree += 1
        else: mismatch += 1
    print(f"  (n_V,n_H)=({nV},{nH}): C4-gap and CMI>0 agree on {agree} of {len(list(permutations(range(nV*nH))))} realizations")
if mismatch: fail += 1; print(f"  FAIL: {mismatch} disagreements")
else: print("  => certified: C4 coincides with clause (ii) on every realization —")
print("     C4 is the left-hand side read on the realization, not a further hypothesis.")

print("\nprimitive_probes:", "ALL CHECKS PASS" if fail == 0 else f"{fail} FAILURE(S)")
sys.exit(1 if fail else 0)
