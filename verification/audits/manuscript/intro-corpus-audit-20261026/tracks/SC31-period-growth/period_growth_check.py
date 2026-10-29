#!/usr/bin/env python3
"""SC-31 check: three growth rates for the order of a permutation of n points.

(1) universal bound: ord(sigma) divides lcm(1..n); ln lcm(1..n) = psi(n) ~ n.
(2) maximum order: Landau's g(n), ln g(n) ~ sqrt(n ln n).
(3) typical order of a uniform random permutation: ln ord ~ (ln n)^2 / 2,
    asymptotically normal with variance (ln n)^3 / 3 (Erdos-Turan).
(4) rule-specific: an invertible linear map of (Z/q)^D has order <= q^D - 1
    for every q >= 2; the wave rule on a ring of L sites has order qL
    (q prime, gcd(L,q)=1, book Theorem B.3.1); the 3D torus rule's order
    divides 2q(q^(2m)-1), m = ord_L(q) (probe, not a corpus claim).

Exact integer arithmetic for (1) and (2); exact cycle-type enumeration plus a
seeded sampler for (3). Deterministic: fixed seed, fixed output precision.
Run: python3 -I period_growth_check.py
"""
import itertools
import math
import random
import sys
from fractions import Fraction
from functools import reduce

try:
    import mpmath
    mpmath.mp.dps = 40
except ImportError:  # pragma: no cover
    mpmath = None

FAIL = []


def check(name, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        FAIL.append(name)


def lcm(a, b):
    return a // math.gcd(a, b) * b


def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    return [i for i in range(n + 1) if sieve[i]]


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield []
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield [k] + rest


def landau_dp(nmax):
    """g(n) for n <= nmax: knapsack over primes, one prime power per prime.
    best[s] = max product of prime powers with distinct primes and sum <= s."""
    best = [1] * (nmax + 1)
    for p in primes_upto(nmax):
        new = best[:]
        q = p
        while q <= nmax:
            for s in range(q, nmax + 1):
                cand = best[s - q] * q
                if cand > new[s]:
                    new[s] = cand
            q *= p
        best = new
    return best


def landau_brute(n):
    return max(reduce(lcm, part, 1) for part in partitions(n))


def lnint(x):
    if mpmath is not None:
        return float(mpmath.log(mpmath.mpf(x)))
    return math.log(x)


def main():
    print("SC-31 period-growth check")
    print(f"python {sys.version.split()[0]}; mpmath {getattr(mpmath, '__version__', 'absent')}")

    # ---- (1) universal bound -------------------------------------------
    print("\n(1) Every permutation order divides lcm(1..n)  [exhaustive, n <= 22]")
    ok = True
    for n in range(1, 23):
        L = reduce(lcm, range(1, n + 1), 1)
        for part in partitions(n):
            if L % reduce(lcm, part, 1):
                ok = False
    check("ord | lcm(1..n) for every cycle type, n = 1..22", ok)

    print("\n    psi(n) = ln lcm(1..n), exact integer lcm")
    L, lcms = 1, [1]
    NMAX = 200000
    pmax_ratio, x_at = 0.0, 0
    for n in range(1, NMAX + 1):
        L = lcm(L, n)
        if n in (10, 100, 1000, 10000, 100000, 200000):
            psi = lnint(L)
            print(f"    n={n:>6}  psi(n)={psi:14.4f}  psi(n)/n={psi / n:.6f}")
        if n <= 2000:
            r = lnint(L) / n
            if r > pmax_ratio:
                pmax_ratio, x_at = r, n
    print(f"    max psi(n)/n over n<=2000: {pmax_ratio:.6f} at n={x_at}  (observation only)")
    # independent psi via von Mangoldt sum, as a control on the lcm route
    n = 100000
    psi_vm = 0.0  # exact floor(log_p n) by repeated multiplication
    for p in primes_upto(n):
        k, q = 0, p
        while q <= n:
            k += 1
            q *= p
        psi_vm += k * math.log(p)
    L = reduce(lcm, range(1, n + 1), 1)
    check("von Mangoldt psi(1e5) equals ln lcm(1..1e5) to 1e-6", abs(psi_vm - lnint(L)) < 1e-6)

    # ---- (2) Landau's function -------------------------------------------
    print("\n(2) Landau g(n): partition DP vs brute force")
    g = landau_dp(2000)
    check("DP equals brute force max lcm over partitions, n = 1..40",
          all(g[n] == landau_brute(n) for n in range(1, 41)))
    print("    g(1..20) =", [g[n] for n in range(1, 21)])
    for n in (10, 20, 50, 100, 500, 1000, 2000):
        lg = lnint(g[n])
        L = reduce(lcm, range(1, n + 1), 1)
        print(f"    n={n:>4}  g(n)={g[n] if n <= 100 else '...'}  ln g={lg:9.4f}  "
              f"ln g/sqrt(n ln n)={lg / math.sqrt(n * math.log(n)):.4f}  ln lcm(1..n)={lnint(L):10.4f}")
    print(f"    g(100) = {g[100]}")
    ok, L = True, 1
    for n in range(1, 2001):
        L = lcm(L, n)
        ok = ok and L % g[n] == 0
    check("g(n) divides lcm(1..n), n = 1..2000", ok)
    check("ln g(n) / ln lcm(1..n) < 0.25 at n = 2000 (g far below the universal bound)",
          lnint(g[2000]) / lnint(reduce(lcm, range(1, 2001), 1)) < 0.25)

    # ---- (3) typical order ----------------------------------------------
    print("\n(3) Typical order of a uniform random permutation")
    # exact E[ln ord] by cycle-type enumeration: P(type) = prod 1/(k^m_k m_k!)
    def exact_moments(n):
        m1, m2 = 0.0, 0.0
        tot = Fraction(0)
        for part in partitions(n):
            cnt = {}
            for k in part:
                cnt[k] = cnt.get(k, 0) + 1
            pr = Fraction(1)
            for k, m in cnt.items():
                pr /= Fraction(k ** m * math.factorial(m))
            tot += pr
            lo = math.log(reduce(lcm, part, 1))
            m1 += float(pr) * lo
            m2 += float(pr) * lo * lo
        return tot, m1, m2 - m1 * m1

    rng = random.Random(20261027)

    def sample_ln_order(n):
        # cycle containing a fixed point of the remaining set has length uniform on 1..m
        m, o = n, 1
        while m:
            k = rng.randint(1, m)
            o = lcm(o, k)
            m -= k
        return lnint(o)

    def shuffle_ln_order(n):
        perm = list(range(n))
        rng.shuffle(perm)
        seen, o = [False] * n, 1
        for i in range(n):
            if not seen[i]:
                j, c = i, 0
                while not seen[j]:
                    seen[j] = True
                    j = perm[j]
                    c += 1
                o = lcm(o, c)
        return lnint(o)

    tot, mu30, var30 = exact_moments(30)
    check("cycle-type probabilities sum to exactly 1 at n = 30", tot == 1)
    S = 20000
    a = [sample_ln_order(30) for _ in range(S)]
    b = [shuffle_ln_order(30) for _ in range(S)]
    ma, mb = sum(a) / S, sum(b) / S
    se = math.sqrt(var30 / S)
    print(f"    n=30 exact E[ln ord]={mu30:.4f}  cycle sampler={ma:.4f}  shuffle sampler={mb:.4f}  (se {se:.4f})")
    check("both samplers within 4 se of the exact mean at n = 30",
          abs(ma - mu30) < 4 * se and abs(mb - mu30) < 4 * se)

    print("    n        mean ln ord   (ln n)^2/2   ratio   var ln ord   (ln n)^3/3   ratio")
    for n, S in ((10 ** 3, 4000), (10 ** 5, 2000), (10 ** 7, 1000), (10 ** 9, 1000)):
        xs = [sample_ln_order(n) for _ in range(S)]
        mu = sum(xs) / S
        var = sum((x - mu) ** 2 for x in xs) / (S - 1)
        ln = math.log(n)
        print(f"    1e{round(math.log10(n))}  {mu:12.3f}  {ln * ln / 2:11.3f}  {mu / (ln * ln / 2):.3f}"
              f"  {var:11.3f}  {ln ** 3 / 3:11.3f}  {var / (ln ** 3 / 3):.3f}")
    print("    (sanity check only: both ratios rise toward 1 slowly, lower-order terms dominate at these n)")


    # ---- (4) the framework's linear rule ---------------------------------
    print("\n(4) Linear rule over Z/q: order <= q^D - 1; wave-rule periods")
    import numpy as np
    from sympy import factorint

    def matorder(M, q, cap):
        P = np.eye(M.shape[0], dtype=np.int64)
        Mq = M % q
        for k in range(1, cap + 1):
            P = (P @ Mq) % q
            if np.array_equal(P, np.eye(M.shape[0], dtype=np.int64)):
                return k
        return None

    def mpow(M, e, q):
        R = np.eye(M.shape[0], dtype=np.int64)
        B = M % q
        while e:
            if e & 1:
                R = (R @ B) % q
            B = (B @ B) % q
            e >>= 1
        return R

    def isid(M):
        return np.array_equal(M, np.eye(M.shape[0], dtype=np.int64))

    def wave_F(A):
        V = A.shape[0]
        I = np.eye(V, dtype=np.int64)
        Z = np.zeros((V, V), dtype=np.int64)
        return np.block([[Z, I], [-I, A]])

    def ring_A(L):
        A = np.zeros((L, L), dtype=np.int64)
        for i in range(L):
            A[i, (i + 1) % L] += 1
            A[i, (i - 1) % L] += 1
        return A

    def torus_A(L):
        A = np.zeros((L ** 3, L ** 3), dtype=np.int64)
        ix = lambda a, b, c: (a % L) * L * L + (b % L) * L + (c % L)
        for a, b, c in itertools.product(range(L), repeat=3):
            for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                A[ix(a, b, c), ix(a + d[0], b + d[1], c + d[2])] += 1
        return A

    ok = True
    for q in (2, 3, 4, 5, 6, 8, 9, 10, 12):
        mx = 0
        for a, b, c, d in itertools.product(range(q), repeat=4):
            if math.gcd((a * d - b * c) % q, q) == 1:
                mx = max(mx, matorder(np.array([[a, b], [c, d]]), q, q * q))
        ok = ok and mx <= q * q - 1
        print(f"    D=2, q={q:>2}: max order over GL(2,Z/q) = {mx:>3}  (q^2-1 = {q * q - 1})")
    check("every invertible 2x2 matrix over Z/q has order <= q^2-1, q = 2..12 sample", ok)
    ok = True
    for q in (2, 3, 5, 7):
        for L in range(3, 10):
            if math.gcd(L, q) == 1:
                ok = ok and matorder(wave_F(ring_A(L)), q, 10 ** 5) == q * L
    check("ring wave rule: order = qL for q in {2,3,5,7}, L = 3..9, gcd(L,q)=1 (Theorem B.3.1)", ok)
    for q, L in ((4, 3), (6, 3), (4, 5), (6, 5), (9, 4), (8, 3)):
        o = matorder(wave_F(ring_A(L)), q, q ** (2 * L))
        print(f"    ring, composite q={q} L={L}: order {o}  (q^D-1 = {q ** (2 * L) - 1})")
    ok = True
    for L, q in ((2, 3), (2, 5), (3, 2), (3, 5), (4, 3), (4, 5), (5, 2), (5, 3)):
        m = 1
        while pow(q, m, L) != 1:
            m += 1
        F = wave_F(torus_A(L))
        M = 2 * q * (q ** (2 * m) - 1)
        div = isid(mpow(F, M, q))
        o = M
        for p, k in factorint(M).items():
            for _ in range(k):
                if isid(mpow(F, o // p, q)):
                    o //= p
                else:
                    break
        ok = ok and div
        print(f"    3D torus L={L} q={q} D={2 * L ** 3}: order {o}; ln order / ln|S| = {math.log(o) / (2 * L ** 3 * math.log(q)):.4f}")
    check("3D torus wave rule: order divides 2q(q^(2m)-1) on the tested (L, q)", ok)

    # ---- leading orders at |S| ~ e^{10^122} ------------------------------
    print("\nLeading-order expressions at n = e^(10^122)  [asymptotic]")
    if mpmath is not None:
        lnn = mpmath.mpf(10) ** 122
        log10e = mpmath.log10(mpmath.e)
        # (1) ln lcm ~ n  -> log10(ln lcm) = 10^122 log10 e
        print(f"    (1) ln lcm(1..n) ~ n = e^(10^122);  log10(ln lcm) ~ {mpmath.nstr(lnn * log10e, 8)}")
        # (2) ln g ~ sqrt(n ln n) = 10^61 e^(5e121)
        l2 = 61 + lnn / 2 * log10e
        print(f"    (2) ln g(n) ~ sqrt(n ln n) = 10^61 e^(5e121);  log10(ln g) ~ {mpmath.nstr(l2, 8)}")
        print(f"        ln g / ln lcm ~ sqrt(ln n / n) = 10^61 e^(-5e121)")
        # (3) ln ord ~ (ln n)^2/2, sd sqrt((ln n)^3/3)
        print(f"    (3) ln ord ~ (ln n)^2/2 = {mpmath.nstr(lnn ** 2 / 2, 6)};  "
              f"sd ~ sqrt((ln n)^3/3) = {mpmath.nstr(mpmath.sqrt(lnn ** 3 / 3), 6)}")
        # Planck-time conversion is negligible in the exponent
        print(f"    t_Pl ~ 5.39e-44 s shifts ln(time in s) by {mpmath.nstr(mpmath.log(mpmath.mpf('5.39e-44')), 6)}")

    print("\nRESULT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
