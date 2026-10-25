"""Reviewer spot-checks for PE-01 PLAN.md (aa667c13). Exact integer/Fraction arithmetic only."""
from fractions import Fraction as Fr
from itertools import product, permutations
from collections import Counter
from math import gcd

P = {3: [1, 3], 4: [1, 4], 5: [2, 5], 6: [1, 6], 7: [1, 7], 8: [2, 3, 4, 8]}  # exponents besides 0
PR = {3: [2, 3], 4: [3, 4], 5: [3, 5], 6: [5, 6], 7: [6, 7], 8: [4, 5, 6, 8]}


def poly_int(exps):
    v = 1
    for e in exps:
        v |= 1 << e
    return v


def mulmod(a, b, m, deg):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a >> deg & 1:
            a ^= m
    return r


def order_of_z(m, deg):
    x, k = 2, 1
    while x != 1:
        x = mulmod(x, 2, m, deg)
        k += 1
        if k > 1 << deg:
            return None
    return k


def recip(exps, n):
    return sorted(set([n - e for e in exps if e != n] + [n]) - {0} | ({n} if True else set()))


print("== EX4 primitivity and reciprocal table")
for n in P:
    m, mr = poly_int(P[n]), poly_int(PR[n])
    rc = poly_int(sorted({n - e for e in P[n]} | {n}) )  # reciprocal: z^n p(1/z); constant term 1 -> z^n, z^n -> 1
    # build reciprocal properly
    coeffs = [0] * (n + 1)
    for e in [0] + P[n]:
        coeffs[n - e] = 1
    rc = sum(c << i for i, c in enumerate(coeffs))
    print(n, "ord(p)=", order_of_z(m, n), "ord(p')=", order_of_z(mr, n), "want", 2 ** n - 1, "p' is reciprocal:", rc == mr)


def nprim(n):
    cnt = 0
    for m in range((1 << n) + 1, 1 << (n + 1), 2):
        if order_of_z(m, n) == 2 ** n - 1:
            cnt += 1
    return cnt


print("primitive counts:", {n: nprim(n) for n in range(3, 9)})


def make_L(n, exps):
    c = [0] * n
    for e in [0] + exps:
        if e < n:
            c[e] = 1

    def L(h):  # h tuple (h0..h_{n-1})
        return h[1:] + (sum(ci & hi for ci, hi in zip(c, h)) & 1,)
    return L


def gen(name, n, exps):
    L = make_L(n, exps)
    ell = lambda h: h[0]
    g = lambda h: h[0] ^ (h[1] & h[2])
    if name == "lin":
        s0 = s1 = L; f = ell
    elif name == "filt":
        s0 = s1 = L; f = g
    elif name == "clk":
        s0 = L; s1 = lambda h: L(L(h)); f = ell
    elif name == "dec":
        s0 = s1 = L; f = lambda h: 0

    def phi(state):
        x, h = state
        h2 = s1(h) if x else s0(h)
        return (x ^ f(h2), h2)
    return phi


def states(n):
    return [(x, h) for x in (0, 1) for h in product((0, 1), repeat=n)]


def record(phi, s, K):
    out = [s[0]]
    for _ in range(K):
        s = phi(s)
        out.append(s[0])
    return tuple(out)


print("== EX1 bijection by image count, orbit structure, K_cx, K_max vs 2*Lmax")
for name in ["lin", "filt", "clk", "dec"]:
    for n in range(3, 9):
        phi = gen(name, n, P[n])
        S = states(n)
        img = {phi(s) for s in S}
        assert len(img) == len(S)
        # orbit lengths
        seen, lens = {}, []
        for s in S:
            if s in seen:
                lens.append(seen[s]); continue
            orb = [s]; t = phi(s)
            while t != s:
                orb.append(t); t = phi(t)
            for o in orb:
                seen[o] = len(orb)
            lens.append(len(orb))
        lens.sort()
        N = len(lens)
        med = lens[(N - 1) // 2], lens[N // 2]
        Lmax = max(lens)
        Kmax = 4 * (2 ** n - 1)
        print(f"{name} n={n} bij ok; Lmax={Lmax} median={med} Kcx={med[0]//2}..{med[1]//2} Kmax={Kmax} 2Lmax-2={2*Lmax-2} ok={Kmax >= 2*Lmax-2}")


def lc(seq):  # Berlekamp-Massey over GF(2)
    N = len(seq); C = [1] + [0] * N; B = [1] + [0] * N; L = 0; m = 1
    for i in range(N):
        d = seq[i]
        for j in range(1, L + 1):
            d ^= C[j] & seq[i - j]
        if d == 0:
            m += 1
        elif 2 * L <= i:
            T = C[:]
            for j in range(m, N + 1):
                C[j] ^= B[j - m]
            L = i + 1 - L; B = T; m = 1
        else:
            for j in range(m, N + 1):
                C[j] ^= B[j - m]
            m += 1
    return L


def count_formula(N, L):
    return 1 if L == 0 else 2 ** min(2 * L - 1, 2 * N - 2 * L)


print("== IM2-style: LC count formula vs enumeration, N<=14")
for N in range(1, 15):
    c = Counter(lc(s) for s in product((0, 1), repeat=N))
    assert all(c[L] == count_formula(N, L) for L in range(N + 1)), N
    assert sum(count_formula(N, L) for L in range(N + 1)) == 2 ** N
print("formula matches enumeration for N=1..14")


# independent DP: LC profile Markov chain for fair bits (discrepancy fair & independent)
def lc_dist_dp(N):
    dist = {0: 1}  # counts over 2^i sequences
    for i in range(N):
        nd = Counter()
        for L, w in dist.items():
            nd[L] += w  # discrepancy 0
            nd[i + 1 - L if 2 * L <= i else L] += w  # discrepancy 1
        dist = nd
    return dist


ok = all(lc_dist_dp(N)[L] == count_formula(N, L) for N in range(1, 1100) for L in range(N + 1) if L in lc_dist_dp(N) or count_formula(N, L) == 0) if False else None
bad = []
for N in list(range(1, 60)) + [255, 256, 1021]:
    d = lc_dist_dp(N)
    if any(d.get(L, 0) != count_formula(N, L) for L in range(N + 1)):
        bad.append(N)
print("DP vs closed form mismatches:", bad)

print("== PC zero, NC-1, NC-2 on G_lin; NC-2 separation on G_filt")
for n in range(3, 7):
    for exps in (P[n], PR[n]):
        phi = gen("lin", n, exps)
        S = states(n)
        for K in range(0, 3 * n + 4):
            recs = Counter(record(phi, s, K) for s in S)
            Nn = K + 1
            tv = Fr(sum(abs(Fr(c, len(S)) - Fr(1, 2 ** Nn)) for c in recs.values()) + Fr(2 ** Nn - len(recs), 2 ** Nn), 2)
            want = max(Fr(0), 1 - Fr(2 ** n, 2 ** K))
            assert tv == want, (n, K, tv, want)
            pP = Fr(sum(c for r, c in recs.items() if lc(r) <= n + 1), len(S))
            pQ = Fr(sum(count_formula(Nn, L) for L in range(min(n + 1, Nn) + 1)), 2 ** Nn)
            assert pP == 1
print("NC-1 TV = max(0,1-2^(n-K)) and LC<=n+1 surely: verified n=3..6, both siblings, K<=3n+3")

for n in range(4, 8):
    phi = gen("filt", n, P[n]); S = states(n)
    rows = []
    for K in [2 * n + 2, 2 * n + 6, 4 * n]:
        recs = Counter(record(phi, s, K) for s in S)
        pP = Fr(sum(c for r, c in recs.items() if lc(r) <= n + 1), len(S))
        pQ = Fr(sum(count_formula(K + 1, L) for L in range(n + 2)), 2 ** (K + 1))
        lin = 1 - pQ
        rows.append((K, len(recs), str(pP), float(abs(pP - pQ)), float(lin)))
    print("G_filt n=%d" % n, rows)

print("== PC firing on G_dec at K=1")
for n in (3, 4):
    phi = gen("dec", n, P[n]); S = states(n)
    recs = Counter(record(phi, s, 1) for s in S)
    print(n, dict(recs))

print("== P_emb counts")
m1 = len(list(permutations(range(2)))) ** 2 * 2 ** 2
m2 = len(list(permutations(range(4)))) ** 2 * 2 ** 4
print("m=1:", m1, "m=2:", m2, "F count m=2:", 2 ** (2 ** 3))

print("== B4 trivial-annihilator horizon by monomial counting vs 2^(n+1) support")
from math import comb
for n in range(3, 9):
    S = 2 ** (n + 1)
    for d in (1, 2, 3):
        K = 0
        while sum(comb(K + 1, i) for i in range(d + 1)) <= S:
            K += 1
        print(f"n={n} d={d}: annihilator guaranteed by counting at K={K}")
