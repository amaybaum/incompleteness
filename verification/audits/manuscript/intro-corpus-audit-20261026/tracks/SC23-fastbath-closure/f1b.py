#!/usr/bin/env python3
"""sc23 F1b — PREREG2.txt: joint-erosion register model G(d,r). python3 -I f1b.py"""
import sys, itertools
from fractions import Fraction as F
from collections import defaultdict
from decimal import Decimal, getcontext
getcontext().prec = 200
LN2 = Decimal(2).ln()
def D(q): return Decimal(q.numerator) / Decimal(q.denominator)

def init(d):
    ens = defaultdict(F)
    for x0 in (0, 1):
        for rest in itertools.product((0, 1), repeat=d - 1):
            ens[((x0,), (x0,) + rest)] += F(1, 2) * F(1, 2 ** (d - 1))
    return ens

def hmm_G(d, r, K):
    ens = init(d); read_given = {}
    for t in range(K):
        new = defaultdict(F)
        for (h, cells), p in ens.items():
            outs = [(cells, p * r)] + [(ec, p * (1 - r) / 2 ** d) for ec in itertools.product((0, 1), repeat=d)]
            for ec, q in outs:
                if q == 0: continue
                x1 = ec[d - 1]
                rg = read_given.setdefault(h, [F(0), F(0)]); rg[x1] += q
                new[(h + (x1,), (x1,) + ec[:d - 1])] += q
        ens = new
    law = defaultdict(F)
    for (h, c), p in ens.items(): law[h] += p
    return law, read_given

def brute_G(d, r, K):
    law = defaultdict(F)
    for x0 in (0, 1):
        for rest in itertools.product((0, 1), repeat=d - 1):
            for keeps in itertools.product((0, 1), repeat=K):
                wk = F(1)
                for kk in keeps: wk *= r if kk else 1 - r
                if wk == 0: continue
                for fresh in itertools.product((0, 1), repeat=K * d):
                    w = F(1, 2) * F(1, 2 ** (d - 1)) * wk * F(1, 2 ** (K * d))
                    cells = [x0] + list(rest); hist = [x0]
                    for t in range(K):
                        if not keeps[t]:
                            cells = list(fresh[t * d:(t + 1) * d])
                        x = cells[d - 1]; cells = [x] + cells[:d - 1]; hist.append(x)
                    law[tuple(hist)] += w
    return law

def marg(law, n):
    m = defaultdict(F)
    for h, p in law.items(): m[h[:n]] += p
    return m

def gaps(law, K):
    out = {}
    for k in range(1, K):
        Pk1 = marg(law, k + 2); Pk = marg(law, k + 1); best = (F(0), F(0))
        for c in (0, 1):
            hs = [h for h in Pk if Pk[h] > 0 and h[-1] == c]
            cond = {h: Pk1.get(h + (1,), F(0)) / Pk[h] for h in hs}
            for a, b in itertools.combinations(hs, 2):
                cand = (abs(cond[a] - cond[b]), min(Pk[a], Pk[b]))
                if cand > best: best = cand
        out[k] = best
    return out

def cmi(law, k):
    Pk1 = marg(law, k + 2); Pk = marg(law, k + 1)
    pair = defaultdict(F); single = defaultdict(F)
    for h, p in Pk1.items(): pair[(h[-2], h[-1])] += p
    for h, p in Pk.items(): single[h[-1]] += p
    tot = Decimal(0); allone = True
    for h, p in Pk1.items():
        if p == 0: continue
        ratio = (p / Pk[h[:-1]]) / (pair[(h[-2], h[-1])] / single[h[-2]])
        if ratio != 1:
            allone = False; tot += D(p) * D(ratio).ln() / LN2
    return tot, allone

def hbin(e):
    e = D(e)
    if e == 0: return Decimal(0)
    return -(e * e.ln() + (1 - e) * (1 - e).ln()) / LN2

fail = 0
def check(n, ok, info=""):
    global fail
    print(f"  [{'PASS' if ok else 'FAIL'}] {n} {info}"); fail += (not ok)

K = 7; RS = [F(0), F(1, 10 ** 12), F(1, 1000), F(1, 2), F(1)]
res = {}
for d in (2, 3):
    for r in RS:
        law, rg = hmm_G(d, r, K); assert sum(law.values()) == 1
        res[(d, r)] = (law, rg, gaps(law, K))
print("== controls ==")
for d in (2, 3):
    law, rg, g = res[(d, F(0))]
    check(f"G-a d={d} r=0", all(g[k][0] == 0 for k in g) and all(cmi(law, k)[1] for k in g))
    law, rg, g = res[(d, F(1))]
    check(f"G-b d={d} r=1", all(g[k][0] == 1 for k in g if k >= d - 1), str([str(g[k][0]) for k in g]))
for d, Kb in ((2, 5), (3, 4)):
    hb, _ = hmm_G(d, F(1, 2), Kb); bb = brute_G(d, F(1, 2), Kb)
    check(f"G-c d={d} horizon {Kb} brute == HMM", {h: p for h, p in hb.items() if p} == {h: p for h, p in bb.items() if p})
for d in (2, 3):
    for r in RS[1:4]:
        law, rg, g = res[(d, r)]
        for k in g:
            Mk, _ = cmi(law, k); dl, p0 = g[k]
            ec = max(abs(v[1] / (v[0] + v[1]) - F(1, 2)) for h, v in rg.items() if len(h) == k + 1)
            ok = Mk >= D(p0) * D(dl) ** 2 / LN2 and (ec > F(1, 2) or Mk <= 2 * hbin(ec))
            if not ok: check(f"G-d d={d} r={r} k={k}", False, f"M={Mk:.4e}")
print("  [checked] G-d on all cells (failures above)")
print("== data ==")
for d in (2, 3):
    for r in RS[1:4]:
        law, rg, g = res[(d, r)]
        print(f" G d={d} r={r}  tauB/tauS={float(1/(-D(r).ln())):.4f}")
        for k in g:
            Mk, _ = cmi(law, k); dl = g[k][0]
            ec = max(abs(v[1] / (v[0] + v[1]) - F(1, 2)) for h, v in rg.items() if len(h) == k + 1)
            print(f"   k={k} delta_k={float(dl):.6e} (exact {dl if dl.denominator < 10**40 else '...'}) "
                  f"delta_k/r^d={float(dl / r**d) if dl else 0:.6f} r^(k-1)={float(r**(k-1)):.3e} "
                  f"refutes={'Y' if dl > r**(k-1) else 'n'} M_k={float(Mk):.6e} eps_coarse={float(ec):.3e}")
print("== verdicts ==")
if fail:
    print("  VOID")
else:
    w1 = [(d, str(r), k) for (d, r), (_, _, g) in res.items() if 0 < r < 1 for k in g if g[k][0] > r ** (k - 1)]
    print(f"  W1: {'PRINT' if w1 else 'no'}: refuted cells {len(w1)}; first per d: "
          f"{ {d: min(k for dd, rr, k in w1 if dd == d) for d in (2, 3) if any(dd == d for dd, _, _ in w1)} }")
    w2 = [(d, str(r)) for (d, r), (_, _, g) in res.items() if 0 < r < 1 and 1 / (-D(r).ln()) < Decimal('0.2')
          and all(g[k][0] > 0 and g[k][1] > 0 for k in g if k >= d - 1)]
    print(f"  W2: {'PRINT' if w2 else 'no'}: {w2}")
print("f1b:", "ALL CONTROLS GREEN" if not fail else f"{fail} FAILURE(S)")
sys.exit(1 if fail else 0)
