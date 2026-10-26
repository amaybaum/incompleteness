"""Independent check (author of TAGS-r2): exact K_zero of passive statistics that are linear
in the record, on G_lin(p) from PLAN.md section 1 definitions only. No repository imports.

Seed space F_2^{n+1}: bits 0..n-1 = h_0 coordinates, bit n = x_0. Uniform mu.
Advantage of every test on a linear statistic S = M X_{0:K} is 0 iff law_P(S) = law_Q(S)
iff rank(seed forms of S's components) == rank(record forms). Otherwise some nonzero parity of S
is constant under P and the optimal test has advantage >= 1/2 (so K_delta = K_zero + 1 for delta <= 1/2).
"""
import itertools, sys, json

def rank(vs):
    basis = {}
    r = 0
    for v in vs:
        while v:
            hb = v.bit_length() - 1
            if hb in basis:
                v ^= basis[hb]
            else:
                basis[hb] = v; r += 1; break
    return r

def poly_mod_order(p, n):
    # order of z modulo p (p as int bitmask incl. z^n), None if not coprime/irreducible check separately
    x = 1; 
    for k in range(1, 2**n):
        x <<= 1
        if x >> n & 1: x ^= p
        if x == 1: return k
    return None

def is_irreducible(p, n):
    # trial division by all polys of degree 1..n//2
    def pmod(a, b):
        db = b.bit_length() - 1
        while a and a.bit_length() - 1 >= db:
            a ^= b << (a.bit_length() - 1 - db)
        return a
    for d in range(1, n // 2 + 1):
        for q in range(1 << d, 1 << (d + 1)):
            if pmod(p, q) == 0: return False
    return True

def primitive_polys(n):
    out = []
    for low in range(1 << n):
        p = (1 << n) | low
        if p & 1 and is_irreducible(p, n) and poly_mod_order(p, n) == 2**n - 1:
            out.append(p)
    return out

def record_seed_forms(p, n, K):
    """seed forms of X_0..X_K for G_lin(p): h <- L_p h (Fibonacci companion,
    (h0..h_{n-1}) -> (h1..h_{n-1}, sum c_i h_i), c_i = coefficient of z^i in p), then x <- x xor h_0."""
    c = [(p >> i) & 1 for i in range(n)]
    h = [1 << i for i in range(n)]          # forms of current h coordinates
    x = 1 << n
    X = [x]
    for t in range(K):
        new = 0
        for i in range(n):
            if c[i]: new ^= h[i]
        h = h[1:] + [new]
        x ^= h[0]
        X.append(x)
    return X

def stat_ok(rec_forms, X):
    # rec_forms: list of record forms (bitmask over record indices); X: seed forms per index
    seeds = []
    for r in rec_forms:
        s = 0; i = 0; rr = r
        while rr:
            if rr & 1: s ^= X[i]
            rr >>= 1; i += 1
        seeds.append(s)
    return rank(seeds) == rank(rec_forms)

def kzero(p, n, Kmax, stats_at_K):
    X = record_seed_forms(p, n, Kmax)
    for K in range(Kmax + 1):
        for st in stats_at_K(K):
            if not stat_ok(st, X):
                return K - 1
    return None   # no firing within Kmax

def b3k(K):
    idx = range(K + 1)
    for k in (1, 2, 3):
        for S in itertools.combinations(idx, k):
            yield [1 << a for a in S]

def b3k_pairs_only(K):   # odd-size subsets contain x_0 an odd number of times: exactly unbiased
    for a, b in itertools.combinations(range(K + 1), 2):
        yield [(1 << a) | (1 << b)]

def b3w(K):
    for w in range(1, 17):
        for a in range(0, K + 2 - w):
            yield [1 << (a + j) for j in range(w)]

def gl(m):
    for cols in itertools.product(range(1, 1 << m), repeat=m):
        if rank(list(cols)) == m:
            yield cols   # column j = A e_j

def apply(A, v, m):
    out = 0
    for j in range(m):
        if v >> j & 1: out ^= A[j]
    return out

def plin_stats(m):
    filters = [(A, b) for A in gl(m) for b in range(1 << m)]
    def at_K(K):
        for A, b in filters:
            # v_{t+1} = A v_t xor X_t b ; component j of v as record form
            comps = [0] * m
            for t in range(K):
                # new comps: (A v)_j xor X_t b_j
                # comps[j] = record form of coordinate j of v_t; coordinate i of A v = xor_j A[j]_i v_j
                newc = [0] * m
                for i in range(m):
                    f = 0
                    for j in range(m):
                        if A[j] >> i & 1: f ^= comps[j]
                    if b >> i & 1: f ^= 1 << t
                    newc[i] = f
                comps = newc
            yield [cf for cf in comps] + [1 << K]
    return at_K

if __name__ == "__main__":
    res = {}
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    for n in range(3, nmax + 1):
        fam = primitive_polys(n)
        res[n] = {"family_size": len(fam)}
        cap = 4 * (2**n - 1)
        # B3k K1 on each family member (pairs suffice; full check for n <= 5)
        kb = {p: kzero(p, n, min(cap, 2**n + 2), b3k if n <= 5 else b3k_pairs_only) for p in fam}
        res[n]["B3k_K1_set"] = sorted(set(kb.values()))
        kw = {p: kzero(p, n, min(cap, 20), b3w) for p in fam}
        res[n]["B3w_K1_set"] = sorted(set(kw.values()))
        for m in (1, 2, 3, 4):
            if m == 4 and n > 6: break   # m = 4 checked for n <= 6 only (run time)
            st = plin_stats(m)
            kp = {p: kzero(p, n, min(cap, 2**(n+1)), st) for p in fam}
            res[n]["plin_m%d_K1" % m] = {format(p, 'b'): k for p, k in kp.items()}
            res[n]["plin_m%d_K0avg_kzero" % m] = min(kp.values())
        print(n, json.dumps(res[n]), flush=True)
