"""RANK investigation: exact passive Hankel ranks of the visible process of 1-D second-order (leap)
substrata, to larger horizons.

Rule: v^{t+1}_i = F(v^t)_i + v^{t-1}_i (mod 2), the leap (u,v) -> (v, F(v) + u) of
SecondOrderCircuit.  It is time-symmetric: v^{t-1} = F(v^t) + v^{t+1}.  The uniform product measure
is invariant (bijective CA), so the pair (v^0, v^1) on [-rho, rho] is uniform, and it determines
v^t_0 for t in [-rho, rho+1]: 2*rho + 2 = 2n consecutive visible values with rho = n - 1.  This is
exact for the infinite lattice (causal cone, RegionTower.iterate_dependsOnlyOn_ball).

H_n: rows = pasts of length <= n (ending at time 0), columns = futures of length <= n (starting at
time 1), entries = joint probabilities (integer counts / 2^(2W)).  rank over Q >= rank over F_p for
every prime p (exact lower bound); for small n the rank over Q is computed exactly with fractions.
"""
import sys
from fractions import Fraction as Fr
from itertools import product
import numpy as np

P1, P2 = 2147483647, 2147483629       # two primes for the modular ranks


def rank_mod(M, p):
    A = np.array([[int(x) % p for x in row] for row in M], dtype=np.int64)
    r, c = 0, 0
    nr, nc = A.shape
    while r < nr and c < nc:
        piv = np.nonzero(A[r:, c])[0]
        if len(piv) == 0:
            c += 1
            continue
        k = r + piv[0]
        A[[r, k]] = A[[k, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        col = A[:, c].copy()
        col[r] = 0
        nz = np.nonzero(col)[0]
        for i in nz:                       # row ops, int64 safe: values < p < 2^31
            A[i] = (A[i] - col[i] * A[r]) % p
        r += 1
        c += 1
    return r


def rank_Q(M):
    A = [[Fr(x) for x in row] for row in M]
    r, c = 0, 0
    nr, nc = len(A), len(A[0])
    while r < nr and c < nc:
        k = next((i for i in range(r, nr) if A[i][c] != 0), None)
        if k is None:
            c += 1
            continue
        A[r], A[k] = A[k], A[r]
        for i in range(nr):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
        c += 1
    return r


def F(v, m, rule):
    left, right = (v << np.uint32(1)) & m, v >> np.uint32(1)
    if rule == 'linear':
        return left ^ right
    if rule == 'nonlinear':
        return (left & right) ^ v
    if rule == 'majority':
        return (left & right) | (left & v) | (right & v)
    raise ValueError(rule)


def record_counts(n, rule):
    """Integer counts of the 2n-bit visible record (times -rho..rho+1), rho = n-1."""
    rho = n - 1
    W = 2 * rho + 1
    m = np.uint32((1 << W) - 1)
    c = np.uint32(rho)
    counts = np.zeros(1 << (2 * n), dtype=np.int64)
    b_all = np.arange(1 << W, dtype=np.uint32)
    for a0 in range(1 << W):
        a = np.full(1 << W, a0, dtype=np.uint32)       # v^0
        b = b_all.copy()                                # v^1
        fwd = []
        prev, cur = a, b
        for _ in range(rho):                            # v^2 .. v^{rho+1}
            nxt = (F(cur, m, rule) ^ prev) & m
            fwd.append((nxt >> c) & np.uint32(1))
            prev, cur = cur, nxt
        bwd = []
        nxt, cur = b, a
        for _ in range(rho):                            # v^-1 .. v^-rho
            prv = (F(cur, m, rule) ^ nxt) & m
            bwd.append((prv >> c) & np.uint32(1))
            nxt, cur = cur, prv
        bits = list(reversed(bwd)) + [(a >> c) & np.uint32(1), (b >> c) & np.uint32(1)] + fwd
        rec = np.zeros(1 << W, dtype=np.int64)
        for bt in bits:                                 # times -rho .. rho+1, earliest first
            rec = (rec << 1) | bt.astype(np.int64)
        counts += np.bincount(rec, minlength=1 << (2 * n))
    return counts


def hankel(counts, n, L):
    """Joint-probability Hankel matrix (integer counts) with pasts/futures of length <= L <= n."""
    T = 2 * n
    arr = counts.reshape([2] * T)                       # axis k = time -rho + k

    def joint(past, fut):
        sl = []
        for k in range(T):
            if n - len(past) <= k < n:
                sl.append(past[k - (n - len(past))])
            elif n <= k < n + len(fut):
                sl.append(fut[k - n])
            else:
                sl.append(slice(None))
        return int(arr[tuple(sl)].sum())
    strings = [s for l in range(L + 1) for s in product((0, 1), repeat=l)]
    return [[joint(h, f) for f in strings] for h in strings]


if __name__ == '__main__':
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    rules = sys.argv[2].split(',') if len(sys.argv) > 2 else ['linear', 'nonlinear']
    for rule in rules:
        counts = record_counts(NMAX, rule)
        out = []
        for L in range(1, NMAX + 1):
            H = hankel(counts, NMAX, L)
            r1, r2 = rank_mod(H, P1), rank_mod(H, P2)
            rq = rank_Q(H) if L <= 4 else None
            out.append((L, r1, r2, rq))
            print(f'RANK {rule} n={L}: rank_Fp={r1},{r2}' + (f' rank_Q={rq}' if rq is not None else ''),
                  flush=True)
        # scalar sequence s_m = count of the all-zero record of length m (ending anywhere: stationary)
        T = 2 * NMAX
        arr = counts.reshape([2] * T)
        s = []
        for mlen in range(T + 1):
            sl = tuple([0] * mlen + [slice(None)] * (T - mlen))
            s.append(int(arr[sl].sum()))
        K = NMAX
        Hs = [[s[i + j] for j in range(K + 1)] for i in range(K + 1)]
        print(f'SCALAR {rule} P(0^m)*2^(2W), m=0..{T}:', s)
        print(f'SCALAR {rule} Hankel rank of (s_(i+j)), i,j<={K}: Fp={rank_mod(Hs, P1)} Q={rank_Q(Hs)}',
              flush=True)
