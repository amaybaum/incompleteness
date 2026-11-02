"""Re-check of 67a5cbe1: admissible-region tables, recomputed independently.
Z(phi): the largest k such that, for EVERY control sequence y_0..y_{k-1} (the x value fed to sigma), the increments
Y_0..Y_{k-1} = f(sigma_{y_0} h), f(sigma_{y_1} sigma_{y_0} h), ... are jointly uniform under uniform h. Then every
observer, passive or active, adaptive included, has adv_pred = 0 at every K' <= Z (proof in RECHECK). A design
quantity of the generator alone, not a PE-01 measurement."""
import importlib.util, sys, io, contextlib
from itertools import product
from collections import Counter
from math import ceil, log2
spec = importlib.util.spec_from_file_location("c", sys.argv[1]); c = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(c)

def parts(name, n):
    L = c.make_L(n, c.P[n]); ell = lambda h: h[0]; g = lambda h: h[0] ^ (h[1] & h[2])
    if name == "lin": return L, L, ell
    if name == "filt": return L, L, g
    if name == "clk": return L, (lambda h: L(L(h))), ell

def Z(name, n):
    s0, s1, f = parts(name, n)
    H = list(product((0, 1), repeat=n))
    k = 0
    while True:
        k1 = k + 1
        ok = True
        for ys in product((0, 1), repeat=k1):
            cnt = Counter()
            for h in H:
                inc = []; hh = h
                for y in ys:
                    hh = (s1 if y else s0)(hh); inc.append(f(hh))
                cnt[tuple(inc)] += 1
            if len(cnt) != 2 ** k1 or len(set(cnt.values())) != 1:
                ok = False; break
        if not ok: return k
        k = k1
        if k > n + 2: return k

KCX = {"lin": lambda n: 2 ** (n - 1) - 1, "filt": lambda n: 2 ** (n - 1) - 1,
       "clk": lambda n: {3: 5, 4: 9, 5: 20, 6: 42, 7: 84, 8: 168}[n]}
Zs = {(g, n): Z(g, n) for g in ("lin", "filt", "clk") for n in range(3, 9)}
print("Z (universal zero horizon, all observers):")
for g in ("lin", "filt", "clk"): print(" ", g, [Zs[(g, n)] for n in range(3, 9)])

def fp(m, K): return m + (ceil(log2(K + 1)) if K > 0 else 0) + 1

def region(g, n, m, theta, floor):
    ks = [K for K in range(3, KCX[g](n) + 1) if K - 3 >= floor and fp(m, K) <= theta]
    return f"[{min(ks)},{max(ks)}]" if ks else "-"

for theta_name, th in (("theta=n", 0), ("theta=n+1", 1)):
    print(f"\n{theta_name}: cells lin(K-3>=Z+1) | filt(K-3>=Z+1) | clk(K-3>=Z+1) || plan's floor-only filt/clk (K>=3)")
    for n in range(3, 9):
        row = []
        for m in range(1, 5):
            a = region("lin", n, m, n + th, Zs[("lin", n)] + 1)
            b = region("filt", n, m, n + th, Zs[("filt", n)] + 1)
            d = region("clk", n, m, n + th, Zs[("clk", n)] + 1)
            e = region("filt", n, m, n + th, 0); e2 = region("clk", n, m, n + th, 0)
            row.append(f"m={m}: {a}|{b}|{d}||{e},{e2}")
        print(f"n={n}: " + "  ".join(row))
