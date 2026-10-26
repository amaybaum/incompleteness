#!/usr/bin/env python3
"""Exact check of the history-length convention in the readback lemma (papers/Main.md §2.3).

The lemma concludes I(X_{<k}; X_{k+1} | X_k) >= p0 delta^2 / ln 2. Its hypothesis compares
next-step laws P(X_{k+1} | X_{<k} = p, X_k = c) for two pasts p != p' of X_{<k} = (X_0..X_{k-1}),
length k, followed by a common present X_k = c, with p0 bounding Pr[X_{<k} = p, X_k = c].

Target law L (k = 2): X_0, X_1, X_2 i.i.d. uniform bits, X_3 = X_0 xor X_2.
  * pasts X_{<2} (length 2) with present X_2: gap delta = 1, p0 = 1/8, CMI = 1 bit.
  * length-2 windows ending at the present, (X_1, X_2): no gap, although the order-2 CMI is
    positive. A hypothesis indexed that way would not cover a (C4) gap at order 2, so the
    readback lemma could not be applied to (iii)'s (C4) at k in the proof of (iii) => (ii).
  * the K = 2 restriction (X_0, X_1, X_2) is memory-free: no order-1 gap under either
    indexing, so no faithful realization of it carries a readback gap (pushforward identity),
    and the unrestricted every-horizon reading fails for L at K = 2 (and K = 1).
Controls: X_3 = X_1 xor X_2 (both indexings fire); X_3 = X_2, Markov (neither fires, CMI = 0).
Probabilities are exact rationals; the CMI is a float used only for the strict sign and the bound.
Run: python3 -I verification/audits/manuscript/f29-followups-20261026/readback_indexing_probe.py
"""
from fractions import Fraction as F
from itertools import product
from math import log, log2

LN2 = log(2.0)


def law(rule, K):
    """Joint law of (x_0..x_K), K <= 3: i.i.d. uniform x_0..x_2 and x_3 = rule(x_0, x_1, x_2)."""
    out = {}
    for x in product((0, 1), repeat=3):
        traj = x + ((rule(*x),) if K >= 3 else ())
        traj = traj[:K + 1]
        out[traj] = out.get(traj, F(0)) + F(1, 8)
    return out


def split(lw, k, window):
    """dict (past, present, next) -> prob; past = x_{<k} ('full') or x_{1..k-1} ('suffix')."""
    tab = {}
    for traj, p in lw.items():
        past = traj[:k] if window == "full" else traj[1:k]
        key = (past, traj[k], traj[k + 1])
        tab[key] = tab.get(key, F(0)) + p
    return tab


def best_gap(tab):
    """Exact max over present c and past pairs of (p0, delta), p0 = min joint weight."""
    laws = {}
    for (a, c, b), p in tab.items():
        laws.setdefault((a, c), {})
        laws[(a, c)][b] = laws[(a, c)].get(b, F(0)) + p
    best = (F(0), F(0))
    keys = sorted(laws)
    for i, ki in enumerate(keys):
        for kj in keys[i + 1:]:
            if ki[1] != kj[1]:
                continue
            wi, wj = sum(laws[ki].values()), sum(laws[kj].values())
            supp = set(laws[ki]) | set(laws[kj])
            tv = sum(abs(laws[ki].get(b, F(0)) / wi - laws[kj].get(b, F(0)) / wj) for b in supp) / 2
            p0 = min(wi, wj)
            if p0 * tv * tv > best[0] * best[1] * best[1]:
                best = (p0, tv)
    return best


def cmi(tab):
    pc, pac, pcb, total = {}, {}, {}, 0.0
    for (a, c, b), p in tab.items():
        pc[c] = pc.get(c, F(0)) + p
        pac[(a, c)] = pac.get((a, c), F(0)) + p
        pcb[(c, b)] = pcb.get((c, b), F(0)) + p
    for (a, c, b), p in tab.items():
        if p:
            total += float(p) * log2(float(p * pc[c] / (pac[(a, c)] * pcb[(c, b)])))
    return total


results = []


def check(name, cond):
    results.append((name, bool(cond)))
    print(f"{'PASS' if cond else 'FAIL'}  {name}")


L = lambda x0, x1, x2: x0 ^ x2
C1 = lambda x0, x1, x2: x1 ^ x2
MARKOV = lambda x0, x1, x2: x2  # depends on the present only

# Target L at order k = 2 on horizon K = 3.
full = split(law(L, 3), 2, "full")
suff = split(law(L, 3), 2, "suffix")
p0, d = best_gap(full)
I = cmi(full)
print(f"L, k=2, K=3: past X_<2 (length 2) + present X_2: p0={p0}, delta={d}, CMI={I:.6f} bits")
check("L.full.gap", (p0, d) == (F(1, 8), F(1)))
check("L.full.cmi_positive", I > 0.5)
check("L.full.readback_bound", I >= float(p0 * d * d) / LN2)
ps, dsuf = best_gap(suff)
print(f"L, k=2, K=3: length-2 window (X_1, X_2) ending at the present: delta={dsuf}")
check("L.suffix.no_gap", dsuf == 0)
# K = 2 restriction: memory-free.
for window in ("full", "suffix"):
    _, d1 = best_gap(split(law(L, 2), 1, window))
    check(f"L.K2.order1.{window}.no_gap", d1 == 0)
check("L.K2.order1.cmi_zero", abs(cmi(split(law(L, 2), 1, "full"))) < 1e-12)

# Controls.
for window in ("full", "suffix"):
    _, dc = best_gap(split(law(C1, 3), 2, window))
    check(f"control.xor_x1_x2.{window}.gap", dc == 1)
for window in ("full", "suffix"):
    _, di = best_gap(split(law(MARKOV, 3), 2, window))
    check(f"control.memoryless.{window}.no_gap", di == 0)
check("control.memoryless.cmi_zero", abs(cmi(split(law(MARKOV, 3), 2, "full"))) < 1e-12)

ok = all(r for _, r in results)
print(f"VERDICT: {'PASS' if ok else 'FAIL'} - {sum(r for _, r in results)}/{len(results)} checks")
raise SystemExit(0 if ok else 1)
