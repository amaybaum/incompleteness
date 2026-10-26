"""PE-05 design-only arithmetic (revision 3): admissible K ranges per n under PLAN.md §2.

For theta = n + d (d = 1, 2), charge scope full (PLAN §2.1) or TA (transition-and-action component sums, PLAN §2.1
and O10), models R and E, memory m = 0..4 and n = 3..24, it prints the largest K >= 1 with F <= theta (window floor
ignored), the search range [4, Kmax] when Kmax >= 4, the least n whose range is non-empty, and the per-n values the
pe02-parameters block carries. Pure formula evaluation; no generator or observer is simulated."""
import json
from math import ceil, log2, factorial

def c(K): return ceil(log2(K + 1))
def gamma(x): return 2 * (x.bit_length() - 1) + 1
def lehmer_bits(m): return ceil(log2(factorial(2**m))) if m > 0 else 0
def FU(m, K): return m + c(K) + 1

def charge(model, scope, m, K):
    N = 2**m
    if model == "R":
        rho, act, rd, trig = 2 * m * N, N, 2 * N, c(K)
        pre = 0
    else:
        rho, act, rd, trig = 2 * lehmer_bits(m), N, N, gamma(K + 1)
        pre = gamma(m + 1)
    if scope == "full":
        return pre + rho + act + rd + trig
    # TA: component sum of rho_0, rho_1 and a only (PLAN §2.1; not a code length under E)
    return rho + act

def F(model, scope, m, K): return FU(m, K) + charge(model, scope, m, K)

def kmax(model, scope, m, theta):
    """F is non-decreasing in K (c and gamma are), so the scan stops at the first K with F > theta."""
    best, K = None, 1
    while F(model, scope, m, K) <= theta:
        best = K
        K += 1
    return best

NS = range(3, 25)
out = {}
for d in (1, 2):
    for scope in ("full", "TA"):
        for model in ("R", "E"):
            for m in range(0, 5):
                key = "theta=n+%d %s %s m=%d" % (d, scope, model, m)
                row = {n: kmax(model, scope, m, n + d) for n in NS}
                out[key] = row
                least = next((n for n in NS if row[n] is not None and row[n] >= 4), None)
                print(key, "| least n with K>=4:", least)
                print("   Kmax by n=3..24:", [row[n] for n in NS])
print()
print("PARAMETER VALUES (largest K, m = 1, full charge, R and E; null if no K >= 1)")
for d in (1, 2):
    for model in ("R", "E"):
        key = "theta=n+%d full %s m=1" % (d, model)
        print(json.dumps({"theta": "n+%d" % d, "model": model, "m": 1,
                          "by_n": {str(n): out[key][n] for n in range(9, 25)}}, sort_keys=True))
print()
print("CELLS AT n <= 8 WITH A NON-EMPTY SEARCH RANGE [4, Kmax] (any model, scope, m)")
for key, row in out.items():
    for n in range(3, 9):
        if row[n] is not None and row[n] >= 4:
            print(key, "n=%d" % n, "K in [4, %d]" % row[n])
