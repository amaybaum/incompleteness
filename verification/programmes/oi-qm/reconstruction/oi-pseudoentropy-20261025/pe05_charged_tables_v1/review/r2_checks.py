"""Re-review r2 design checks (toy only). Z bound for G_clkfix / G_clkfix_u vs G_clk; theta=n+2 regions for G_clkfix_u."""
import itertools
from math import ceil, log2
src = open("toy_checks.py").read().split("allok = True")[0]
ns = {}; exec(compile(src, "toy_checks_defs", "exec"), ns)
full = open("toy_checks.py").read()
zsrc = full[full.index("def Z_exhaustive_clk"):full.index("for n in (3, 4, 5):\n    print(\"T6")]
exec(compile(zsrc, "zdefs", "exec"), ns)
P = {3: 0b1011, 4: 0b10011, 5: 0b100101, 6: 0b1000011, 7: 0b10000011}
def Z_clkfix(n, p, prior):
    st, seeds = ns["gen_clkfix"](n, p, prior)
    best = 0
    for k in range(1, 2 * n + 2):
        for x0 in (0, 1):
            cnt = {}
            for (x, hq), w in seeds:
                if x != x0: continue
                out = []
                for _ in range(k):
                    x2, hq = st(x, hq); out.append(x2 ^ x); x = x2
                cnt[tuple(out)] = cnt.get(tuple(out), 0) + w
            if len(cnt) != 2 ** k or len(set(cnt.values())) != 1:
                return best
        best = k
    return best
for n in (3, 4, 5, 6, 7):
    zc = ns["Z_exhaustive_clk"](n, P[n]) if n <= 6 else None
    print("n=%d Z(G_clk)=%s Z(clkfix matched)=%d Z(clkfix_u)=%d" % (n, zc, Z_clkfix(n, P[n], "matched"), Z_clkfix(n, P[n], "uniform")))
c = lambda K: ceil(log2(K + 1)); g = lambda x: 2 * (x.bit_length() - 1) + 1
FR = lambda m, K: (m + c(K) + 1) + 2 * m * 2 ** m + 2 ** m + 2 ** (m + 1) + c(K)
FE = lambda m, K: (m + c(K) + 1) + g(m + 1) + 2 * ((0, 1, 5)[m]) + 2 * 2 ** m + g(K + 1)
def kmax(F, m, th):
    best = None
    for K in range(1, 5000):
        if F(m, K) <= th: best = K
    return best
print("theta=n+2 (G_clkfix_u): n, K_R_max(m=0), K_R_max(m=1), K_E_max(m=0), K_E_max(m=1)")
for n in list(range(3, 9)) + list(range(9, 25)):
    print(n, kmax(FR, 0, n + 2), kmax(FR, 1, n + 2), kmax(FE, 0, n + 2), kmax(FE, 1, n + 2))
