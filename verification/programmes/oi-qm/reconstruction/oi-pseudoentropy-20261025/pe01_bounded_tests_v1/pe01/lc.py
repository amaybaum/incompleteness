"""Linear complexity: Berlekamp-Massey (Massey 1969), the length-count closed form, and its checks.

IM1: BM against brute-force minimal-LFSR search on all sequences of length <= 12.
IM2: the closed form N_N(0) = 1, N_N(L) = 2^min(2L-1, 2N-2L) against enumeration of {0,1}^N for
N <= 20, and against an independent DP on the BM length process for every N used; the DP's
Markov premise is itself checked by enumeration for N <= 20.
"""
import numpy as np


def bm_profile(bits):
    """LC of every prefix: out[i] = LC(bits[0..i]). bits: sequence of 0/1."""
    C, B, L, m, R = 1, 1, 0, 1, 0
    out = []
    for i, s in enumerate(bits):
        R = (R << 1) | int(s)
        d = bin(C & R).count("1") & 1
        if d:
            T = C
            C ^= B << m
            if 2 * L <= i:
                L = i + 1 - L
                B = T
                m = 1
            else:
                m += 1
        else:
            m += 1
        out.append(L)
    return out


def lc(bits):
    p = bm_profile(bits)
    return p[-1] if p else 0


def count_closed(N, L):
    """Gustavson 1976 / Rueppel 1986: number of length-N binary sequences of linear complexity L."""
    if L == 0:
        return 1
    if 1 <= L <= N:
        return 1 << min(2 * L - 1, 2 * N - 2 * L)
    return 0


def count_dp(Nmax):
    """Independent DP on the BM length process under fair bits; returns dists[N] = {L: count}."""
    dist = {0: 1}
    dists = {0: dict(dist)}
    for i in range(Nmax):
        nd = {}
        for L, w in dist.items():
            nd[L] = nd.get(L, 0) + w                       # discrepancy 0
            L1 = i + 1 - L if 2 * L <= i else L            # discrepancy 1
            nd[L1] = nd.get(L1, 0) + w
        dist = nd
        dists[i + 1] = dict(dist)
    return dists


def enumerate_bm_levels(Nmax):
    """Vectorized BM over all of {0,1}^N, level by level, for N <= Nmax (Nmax <= 20).

    Returns (counts[N] = {L: count}, markov_ok, details): markov_ok certifies, at every prefix,
    that its two one-symbol extensions have discrepancies 0 and 1 (one each): the discrepancy is a
    fair bit independent of the past, the Markov premise of the DP. That BM's length update is the
    linear complexity is IM1's check against brute force.
    """
    assert Nmax <= 20
    C = np.array([1], dtype=np.int64)
    B = np.array([1], dtype=np.int64)
    L = np.array([0], dtype=np.int64)
    m = np.array([1], dtype=np.int64)
    R = np.array([0], dtype=np.int64)
    PAR = parity_table(22)
    counts = {0: {0: 1}}
    ok = True
    bad = []
    for i in range(Nmax):
        n = len(C)
        C2 = np.repeat(C, 2); B2 = np.repeat(B, 2); L2 = np.repeat(L, 2)
        m2 = np.repeat(m, 2)
        s = np.tile(np.array([0, 1], dtype=np.int64), n)
        R2 = (np.repeat(R, 2) << 1) | s
        d = PAR[(C2 & R2) & ((1 << 22) - 1)]
        # Markov premise: siblings have different discrepancies
        dd = d.reshape(n, 2)
        if not np.all(dd[:, 0] ^ dd[:, 1] == 1):
            ok = False
            bad.append(("sibling-discrepancy", i))
        T = C2.copy()
        upd = d == 1
        Cn = np.where(upd, C2 ^ (B2 << m2), C2)
        grow = upd & (2 * L2 <= i)
        Ln = np.where(grow, i + 1 - L2, L2)
        Bn = np.where(grow, T, B2)
        mn = np.where(grow, 1, m2 + 1)
        C, B, L, m, R = Cn, Bn, Ln, mn, R2
        vals, cnts = np.unique(L, return_counts=True)
        counts[i + 1] = {int(a): int(b) for a, b in zip(vals, cnts)}
    return counts, ok, bad


def parity_table(bits):
    t = np.zeros(1 << bits, dtype=np.int64)
    for k in range(bits):
        t[1 << k: 1 << (k + 1)] = 1 - t[: 1 << k]
    return t


def brute_min_lfsr(N):
    """Minimal LFSR length of every sequence in {0,1}^N by exhaustive search over connection
    polynomials (no BM). Sequence int seq has bit t = s_t. Returns an int64 array indexed by seq."""
    PAR = parity_table(max(N, 1))
    seqs = np.arange(1 << N, dtype=np.int64)
    res = np.full(1 << N, -1, dtype=np.int64)
    unresolved = seqs
    for L in range(0, N + 1):
        if unresolved.size == 0:
            break
        found = np.zeros(unresolved.size, dtype=bool)
        for cmask in range(1 << L):
            ok = np.ones(unresolved.size, dtype=bool)
            for i in range(L, N):
                window = (unresolved >> (i - L)) & ((1 << L) - 1) if L else np.zeros_like(unresolved)
                pred = PAR[window & cmask] if L else np.zeros_like(unresolved)
                si = (unresolved >> i) & 1
                ok &= pred == si
            found |= ok
        res[unresolved[found]] = L
        unresolved = unresolved[~found]
    return res


def im1(Nmax=12):
    """IM1: BM equals brute-force minimal-LFSR length on all sequences of length 1..Nmax."""
    mism = []
    total = 0
    for N in range(1, Nmax + 1):
        brute = brute_min_lfsr(N)
        for seq in range(1 << N):
            bits = [(seq >> t) & 1 for t in range(N)]
            if lc(bits) != int(brute[seq]):
                mism.append((N, seq))
            total += 1
    return {"pass": not mism, "sequences": total, "mismatches": mism[:10]}


def im2(Nused, Nenum=20):
    """IM2: closed form vs enumeration (N <= Nenum) and vs the DP (every N <= Nused)."""
    counts, markov_ok, bad = enumerate_bm_levels(Nenum)
    enum_mism = []
    for N in range(1, Nenum + 1):
        for L in range(0, N + 1):
            if counts[N].get(L, 0) != count_closed(N, L):
                enum_mism.append((N, L))
        if sum(counts[N].values()) != 1 << N:
            enum_mism.append((N, "total"))
    dists = count_dp(Nused)
    dp_mism = []
    for N in range(1, Nused + 1):
        for L in range(0, N + 1):
            if dists[N].get(L, 0) != count_closed(N, L):
                dp_mism.append((N, L))
    # the DP must also agree with enumeration where both exist (its premise checked above)
    for N in range(1, Nenum + 1):
        if any(dists[N].get(L, 0) != counts[N].get(L, 0) for L in range(N + 1)):
            dp_mism.append((N, "enum"))
    return {"pass": (not enum_mism) and (not dp_mism) and markov_ok,
            "N_enumerated": Nenum, "N_dp": Nused, "markov_premise": markov_ok,
            "enum_mismatches": enum_mism[:10], "dp_mismatches": dp_mism[:10], "premise_failures": bad[:10]}


def prq_le(N, lam):
    """Pr_Q[LC(X_{0:N-1}) <= lam] as (numerator, 2^N)."""
    return sum(count_closed(N, L) for L in range(0, min(lam, N) + 1)), 1 << N


def bm_profile_np(X):
    """Vectorized Berlekamp-Massey over the rows of X (seeds x N, N <= 60): LC of every prefix."""
    S, N = X.shape
    assert N <= 60
    C = np.ones(S, dtype=np.int64)
    B = np.ones(S, dtype=np.int64)
    L = np.zeros(S, dtype=np.int64)
    m = np.ones(S, dtype=np.int64)
    R = np.zeros(S, dtype=np.int64)
    PAR = parity_table(16)
    out = np.zeros((S, N), dtype=np.int64)
    for i in range(N):
        R = (R << 1) | X[:, i].astype(np.int64)
        t = C & R
        d = np.zeros(S, dtype=np.int64)
        while True:
            nz = t != 0
            if not nz.any():
                break
            d ^= PAR[t & 0xFFFF]
            t >>= 16
        upd = d == 1
        grow = upd & (2 * L <= i)
        T = C
        C = np.where(upd, C ^ (B << m), C)
        B = np.where(grow, T, B)
        L = np.where(grow, i + 1 - L, L)
        m = np.where(grow, 1, m + 1)
        out[:, i] = L
    return out
