"""PE-05 design-only arithmetic: footprints under the accounting models U, R, E of PLAN.md §2.
Pure formula evaluation; no generator or observer is simulated."""
from math import ceil, log2, factorial

def c(K): return ceil(log2(K + 1))
def gamma(x): return 2 * (x.bit_length() - 1) + 1
def FU(m, K): return m + c(K) + 1
def TR(m, K): return 2 * m * 2**m + 2**m + 2**(m + 1) + c(K)
def TE(m, K):
    L = ceil(log2(factorial(2**m))) if m > 0 else 0
    return gamma(m + 1) + 2 * L + 2 * 2**m + gamma(K + 1)

print("PE-01 witness m=2 K=7: FU", FU(2, 7), "TR", TR(2, 7), "FR", FU(2, 7) + TR(2, 7), "TE", TE(2, 7), "FE", FU(2, 7) + TE(2, 7))
print("m | K | c | FU | TR | FR | TE | FE")
for m in range(0, 5):
    for K in (4, 7, 8, 15, 16, 31):
        print(m, K, c(K), FU(m, K), TR(m, K), FU(m, K) + TR(m, K), TE(m, K), FU(m, K) + TE(m, K))
print("least n with n+1 >= F at K = Kmin (lower bound, Z ignored: Kmin=4)")
for m in range(0, 5):
    for Kmin in (4, 8, 12, 16):
        print(m, Kmin, "U:", FU(m, Kmin) - 1, "R:", FU(m, Kmin) + TR(m, Kmin) - 1, "E:", FU(m, Kmin) + TE(m, Kmin) - 1)
print("largest K admissible at theta=n+1 (window floor ignored), n=3..24")
for model in ("U", "R", "E"):
    for m in (0, 1, 2):
        row = []
        for n in range(3, 25):
            best = None
            for K in range(1, 2**20):
                F = FU(m, K) + {"U": 0, "R": TR(m, K), "E": TE(m, K)}[model]
                if F <= n + 1: best = K
                elif c(K) > n + 2: break
            row.append(best)
        print(model, "m=%d" % m, row)
