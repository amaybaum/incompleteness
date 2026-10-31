"""Re-check of 6e5db447: G_filt specificity rule, admissible window under clock charge."""
import importlib.util, sys, io, contextlib
from fractions import Fraction as Fr
from collections import Counter
from math import ceil, log2
spec = importlib.util.spec_from_file_location("c", sys.argv[1]); c = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(c)

print("== NC-2 specificity rule: at every K where both G_filt and G_lin records are injective,")
print("   B2(lambda=n+1) on G_filt must be strictly smaller than on G_lin")
for n in range(3, 9):
    S = c.states(n); lin = c.gen("lin", n, c.P[n]); filt = c.gen("filt", n, c.P[n])
    fails, first_inj = [], None
    for K in range(0, 4 * n + 6):
        rl = Counter(c.record(lin, s, K) for s in S); rf = Counter(c.record(filt, s, K) for s in S)
        if len(rl) < len(S) or len(rf) < len(S):
            continue
        if first_inj is None: first_inj = K
        N = K + 1
        pQ = Fr(sum(c.count_formula(N, L) for L in range(min(n + 1, N) + 1)), 2 ** N)
        al = abs(1 - pQ)
        pf = Fr(sum(w for r, w in rf.items() if c.lc(r) <= n + 1), len(S))
        af = abs(pf - pQ)
        if not af < al: fails.append((K, str(al), str(af)))
    print(f"n={n}: first K with both injective = {first_inj}; strict-inequality failures (K, adv_lin, adv_filt): {fails}")

print("== Admissible (small-regime) K for a counterexample: m + ceil(log2(K+1)) + 1 <= n,")
print("   window [K-3,K] above PC zero (G_lin: K-3 >= n+1), K <= K_cx(G_lin) = 2^(n-1)-1")
for n in range(3, 9):
    row = []
    for m in range(1, 5):
        ks = [K for K in range(0, 4 * 2 ** n) if m + (ceil(log2(K + 1)) if K > 0 else 0) + 1 <= n]
        top = max(ks) if ks else None
        assert top is None or top == 2 ** (n - m - 1) - 1, (n, m, top)
        lo, hi = n + 4, min(top if top is not None else -1, 2 ** (n - 1) - 1)
        row.append(f"m={m}: K in [{lo},{hi}]" if lo <= hi else f"m={m}: empty")
    print(f"n={n}: " + "; ".join(row))
print("clock-bound identity K <= 2^(n-m-1)-1 verified")

print("== table size formula: rho tables m*2^m each, a 2^m, F 2^(m+1)")
for m in range(1, 5): print(m, 2 * m * 2 ** m + 2 ** m + 2 ** (m + 1))
