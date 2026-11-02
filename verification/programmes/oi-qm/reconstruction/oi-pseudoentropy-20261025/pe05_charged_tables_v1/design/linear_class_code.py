"""PE-05 design-only arithmetic (revision 3, for owner decision O3): a class-specific code for the passive
linear-filter observers plin_m (PLAN.md §2.2), and the K ranges it would admit.

Code: selector (1 bit) | gamma(m+1) | index of A in GL(m,2) (ceil(log2 |GL(m,2)|) bits) | b (m bits) |
c (m bits) | e (1 bit) | gamma(K+1), for rho_x(v) = A v + x b and the linear prediction chi(v) = c.v + e.
Footprint F_lin = F_U + |code| with F_U = m + ceil(log2(K+1)) + 1. |GL(m,2)| is counted by enumerating all m x m
matrices over F_2 and testing invertibility, and compared with prod_i (2^m - 2^i). Pure arithmetic; no generator or
observer is simulated."""
from math import ceil, log2

def c(K): return ceil(log2(K + 1))
def gamma(x): return 2 * (x.bit_length() - 1) + 1
def FU(m, K): return m + c(K) + 1

def rank_f2(rows, m):
    rows, r = list(rows), 0
    for col in range(m):
        piv = next((i for i in range(r, m) if rows[i] >> col & 1), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(m):
            if i != r and rows[i] >> col & 1: rows[i] ^= rows[r]
        r += 1
    return r

def gl_count(m):
    n = 0
    for M in range(1 << (m * m)):
        rows = [(M >> (m * i)) & ((1 << m) - 1) for i in range(m)]
        n += rank_f2(rows, m) == m
    return n

GL = {}
for m in range(1, 5):
    GL[m] = gl_count(m)
    prod = 1
    for i in range(m): prod *= (2**m - 2**i)
    print("m=%d |GL(m,2)| enumerated=%d formula=%d match=%s index bits=%d" % (m, GL[m], prod, GL[m] == prod, ceil(log2(GL[m])) if GL[m] > 1 else 0))

def code_len(m, K):
    gl_bits = ceil(log2(GL[m])) if GL[m] > 1 else 0
    return 1 + gamma(m + 1) + gl_bits + m + m + 1 + gamma(K + 1)

def F(m, K): return FU(m, K) + code_len(m, K)

print("F_lin(m, K) for K = 4..8:")
for m in range(1, 5):
    print("  m=%d" % m, [(K, F(m, K)) for K in range(4, 9)])
for d in (1, 2):
    print("theta = n+%d: search range [4, Kmax] per n where non-empty (window floor K >= 4)" % d)
    for m in range(1, 5):
        rng = []
        for n in range(3, 25):
            best, K = None, 1
            while F(m, K) <= n + d:
                best = K; K += 1
            if best is not None and best >= 4:
                rng.append((n, best))
        print("  plin_m%d:" % m, rng if rng else "empty for n <= 24")
