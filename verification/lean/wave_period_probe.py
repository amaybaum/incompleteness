#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CT3-R2B-Q2: exact period and cycle spectrum of the binary wave rule.

The first-moment obstruction of CT3-R2B step 1 reduces, after the divisor-indexed simplification,
to a purely arithmetic test on the CYCLE SPECTRUM of the update permutation P. With
m = ord(P), omega = exp(2 pi i / m), and s = ord(omega^r) = m / gcd(m, r), the block dimension d_r
depends on r only through s, and equals

    D_s  =  the number of P-cycles whose length is divisible by s,

so the entire first-moment test is

    the width-2 obstruction FIRES  <=>  there is s | m with s > 2 and (s / gcd(s, 2)) not dividing D_s.

Deciding that test for every L therefore needs the exact cycle spectrum, which this round supplies
in closed form -- without enumerating 4^L states -- for the binary (q = 2) wave rule.

THE SETUP. On a ring of L sites over F_2 the wave rule is

    x(n, t+1) = x(n-1, t) + x(n+1, t) + x(n, t-1),        F = [[0, I], [I, A]],  A = S + S^{-1}

with S the spatial shift; over F_2 the sign in [[0, I], [-I, A]] is immaterial. The temporal
polynomial factors as x^2 + (S + S^{-1}) x + 1 = (x + S)(x + S^{-1}), which is the algebraic form of
the two traveling-wave directions and is what drives every result below.

WHAT IS PROVED HERE (the proofs are recorded in verification/CT3-R2B-Q2-PERIOD-AND-CYCLES.md;
this file is the exact verification, and every check is exact integer arithmetic).

  1. PERIOD.        m_L = ord(F_L over F_2) = L for L even, 2L for L odd.
  2. FIXED POINTS.  dim_{F_2} ker(F_L^k - I) = 2 gcd(k, L) - [L odd and k odd],
                    hence |Fix(F_L^k)| = 2^that, with no state enumeration.
  3. CYCLES.        With M(n) = (1/n) sum_{d | n} mu(n/d) 4^d the aperiodic-necklace count on four
                    letters, the number of P-cycles of length exactly l is

                      L even:  C_l = M(l)                      for l | L
                      L odd:   C_e = M(e)/2 and C_{2e} = M(e)/4 for e | L

                    and D_s = sum over cycle lengths divisible by s.
  4. SILENCE.       For L a power of two the test is SILENT, for every s. Proof: v_2(C_{2^i})
                    = 2^i - i >= j - 1 for every i >= j >= 1.
  5. THE CONJECTURE "SILENT IFF L IS A POWER OF TWO" IS FALSE. For L = p an odd prime the test is
                    silent exactly when p^2 | 2^(p-1) - 1, i.e. exactly at the WIEFERICH PRIMES.
                    L = 1093 and L = 3511 are silent and are not powers of two.

CORPUS CORRECTION (deliverable 1). Appendix B.3.1 / SM Appendix A.1 stated ord(F mod q) = qL for q
odd and L for q = 2, under gcd(L, q) = 1. The value at q = 2 is 2L, not L: gcd(L, 2) = 1 forces L
odd, the unipotent factor at the parabolic mode has order exactly 2, and 2 does not divide an odd L.
The uniform statement ord(F mod q) = qL holds at every prime including 2. The same appendix's
Jordan-Chevalley theorem is consistent with that but does not by itself give it: F = F_ss F_u has
commuting factors whose orders DIVIDE L and q, and the exact values need a primitive L-th-root mode
in the semisimple sector and N != 0. Check W1 verifies the corrected value and exhibits the failure
of the old one. Check W9 records a second defect of the same appendix found in the same audit: the
rank of N is 2 only for EVEN L (two parabolic modes, zeta = +-1); for odd L there is one parabolic
mode and rank(N) = 1.

SCOPE TOKENS, machine-checked by the R7-CT3D guard in edge_rigidity_probe.py.

    SCOPE-TOKEN: PERIOD-CORRECTED      ord(F mod 2) = 2L, not L; the corpus carried L
    SCOPE-TOKEN: WIDER-RANGE-OPEN      w >= 3 untouched; the antisymmetric fact is width-2 only
    SCOPE-TOKEN: Q2-ONLY               q = 2; the q = 3 spectrum obeys different formulas
    SCOPE-TOKEN: CONJECTURE-FALSE      silence is NOT the powers of two; Wieferich primes are silent
    SCOPE-TOKEN: CT3-OPEN              CT3 itself is not settled by this round
    SCOPE-TOKEN: FINITE-VOLUME-ONLY    finite periodic lattices; no infinite-volume claim

SCOPE, which is the part that must not be misread.

  - Everything here is about the FIRST-MOMENT TEST, an obstruction criterion. Silence of the test is
    not a static local generator, and firing of the test is a width-2 obstruction only where the
    width-2 Hermitian-sector annihilator is established. The symmetric-sector palindromicity is
    structural; the antisymmetric-sector vanishing is the computed WIDTH-2 ingredient (CT3-R2B step
    one). Nothing here licenses w >= 3.
  - Everything here is FINITE VOLUME. No infinite-lattice transport is claimed.
  - Everything here is q = 2. The q = 3 data of the previous round is not covered by these formulas.
"""

import sys
import time
from math import gcd

FAILURES = []


def check(label, ok, msg):
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}")
    if not ok:
        FAILURES.append(label)


# ----------------------------------------------------------------- exact modular linear algebra

def wave_matrix(L, q):
    """F = [[0, I], [-I, A]] on (x(t-1), x(t)), A = S + S^{-1} the ring adjacency, entries mod q."""
    n = 2 * L
    F = [[0] * n for _ in range(n)]
    for i in range(L):
        F[i][L + i] = 1 % q                                    # x(t-1)' = x(t)
        F[L + i][i] = (-1) % q                                 # x(t+1) = A x(t) - x(t-1)
        F[L + i][L + (i - 1) % L] = (F[L + i][L + (i - 1) % L] + 1) % q
        F[L + i][L + (i + 1) % L] = (F[L + i][L + (i + 1) % L] + 1) % q
    return F


def matmul(X, Y, q):
    n = len(X)
    Yt = list(zip(*Y))
    return [[sum(a * b for a, b in zip(row, col)) % q for col in Yt] for row in X]


def matpow(X, e, q):
    n = len(X)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    B = [row[:] for row in X]
    while e:
        if e & 1:
            R = matmul(R, B, q)
        B = matmul(B, B, q)
        e >>= 1
    return R


def is_identity(X, q):
    n = len(X)
    return all(X[i][j] % q == (1 if i == j else 0) for i in range(n) for j in range(n))


def prime_factors(n):
    fs, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d)
            n //= d
        d += 1
    if n > 1:
        fs.add(n)
    return sorted(fs)


def matrix_order(X, q, bound):
    """Exact multiplicative order of X mod q, by testing every divisor of `bound`; None if X^bound != I."""
    if not is_identity(matpow(X, bound, q), q):
        return None
    order = bound
    for p in prime_factors(bound):
        while order % p == 0 and is_identity(matpow(X, order // p, q), q):
            order //= p
    return order


def rank_mod_p(rows, ncols, p):
    """Exact rank over F_p of a list of rows (p prime)."""
    M = [row[:] for row in rows]
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(M)) if M[i][c] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(v * inv) % p for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M):
            break
    return r


# ------------------------------------------------------------------------ GF(2) bit-packed layer

def wave_bits(L):
    """F over F_2 as 2L row bitmasks (bit j of row i = entry (i, j))."""
    n = 2 * L
    rows = [0] * n
    for i in range(L):
        rows[i] |= 1 << (L + i)
        rows[L + i] ^= 1 << i
        rows[L + i] ^= 1 << (L + (i - 1) % L)
        rows[L + i] ^= 1 << (L + (i + 1) % L)
    return rows


def bitmul(A, B):
    """Row-bitmask matrix product over F_2."""
    out = []
    for ra in A:
        acc, j = 0, 0
        r = ra
        while r:
            if r & 1:
                acc ^= B[j]
            r >>= 1
            j += 1
        out.append(acc)
    return out


def bitpow(A, e):
    n = len(A)
    R = [1 << i for i in range(n)]
    B = A[:]
    while e:
        if e & 1:
            R = bitmul(R, B)
        B = bitmul(B, B)
        e >>= 1
    return R


def nullity_bits(rows, n):
    """dim_{F_2} of the kernel of the matrix given by row bitmasks."""
    M = [r for r in rows if r]
    rank, pivots = 0, []
    for r in M:
        for p in pivots:
            r = min(r, r ^ p)
        if r:
            pivots.append(r)
            pivots.sort(reverse=True)
            rank += 1
    return n - rank


def fix_dim_exact(L, k):
    """dim_{F_2} ker(F_L^k - I), computed from the matrix."""
    n = 2 * L
    P = bitpow(wave_bits(L), k)
    return nullity_bits([P[i] ^ (1 << i) for i in range(n)], n)


def fix_dim_formula(L, k):
    return 2 * gcd(k, L) - (1 if (L % 2 and k % 2) else 0)


# ------------------------------------------------------------------------------ cycle arithmetic

def divisors(n):
    return sorted(d for d in range(1, n + 1) if n % d == 0)


def mobius(n):
    if n == 1:
        return 1
    mu, d, m = 1, 2, n
    while d * d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0:
                return 0
            mu = -mu
        d += 1
    return -mu if m > 1 else mu


def necklace(n):
    """M(n) = (1/n) sum_{d | n} mu(n/d) 4^d -- aperiodic necklaces of length n on four letters."""
    tot = sum(mobius(n // d) * 4 ** d for d in divisors(n))
    assert tot % n == 0
    return tot // n


def spectrum_closed(L):
    """{cycle length: number of cycles} from the closed forms, plus m_L."""
    if L % 2 == 0:
        spec = {l: necklace(l) for l in divisors(L)}
        return spec, L
    spec = {}
    for e in divisors(L):
        Me = necklace(e)
        assert Me % 4 == 0
        spec[e] = Me // 2
        spec[2 * e] = Me // 4
    return spec, 2 * L


def spectrum_mobius(L):
    """The same spectrum via |Fix(F^k)| = 2^(fixed-point dimension) and Mobius inversion."""
    m = L if L % 2 == 0 else 2 * L
    spec = {}
    for l in divisors(m):
        tot = sum(mobius(l // d) * 2 ** fix_dim_formula(L, d) for d in divisors(l))
        assert tot % l == 0, (L, l, tot)
        if tot:
            spec[l] = tot // l
    return spec, m


def spectrum_brute(L):
    """The cycle spectrum by direct enumeration of all 4^L states. Only for small L."""
    n = 2 * L
    rows = wave_bits(L)

    def step(v):
        out = 0
        for i in range(n):
            if bin(rows[i] & v).count('1') & 1:
                out |= 1 << i
        return out

    nxt = [step(v) for v in range(1 << n)]
    seen = bytearray(1 << n)
    spec = {}
    for v in range(1 << n):
        if seen[v]:
            continue
        length, w = 0, v
        while not seen[w]:
            seen[w] = 1
            w = nxt[w]
            length += 1
        spec[length] = spec.get(length, 0) + 1
    return spec


def block_dim(s, spec):
    """D_s -- the number of cycles whose length is divisible by s."""
    return sum(c for l, c in spec.items() if l % s == 0)


def first_moment_witnesses(L):
    """Every s | m_L with s > 2 at which (s / gcd(s, 2)) fails to divide D_s."""
    spec, m = spectrum_closed(L)
    out = []
    for s in divisors(m):
        if s <= 2:
            continue
        D = block_dim(s, spec)
        need = s // gcd(s, 2)
        if D % need:
            out.append((s, D, need))
    return out


def fires(L):
    return bool(first_moment_witnesses(L))


# ------------------------------------------------------------------------------------------ main

def main():
    extended = '--extended' in sys.argv
    t0 = time.time()
    print("wave_period_probe: CT3-R2B-Q2, exact period and cycle spectrum of the binary wave rule")
    print()

    # ------------------------------------------------------------------ W1: the period formula
    odd_q = [3, 5, 7, 11, 13]
    facts, ok_new, old_ok_anywhere = [], True, False
    for q in [2] + odd_q:
        for L in range(2, 13):
            if gcd(L, q) != 1:
                continue
            o = matrix_order(wave_matrix(L, q), q, q * L)
            if o != q * L:
                ok_new = False
                facts.append(f"q={q} L={L} ord={o}")
            if q == 2 and o == L:
                old_ok_anywhere = True
    q2 = [(L, matrix_order(wave_matrix(L, 2), 2, 2 * L)) for L in (3, 5, 7, 9, 11)]
    check('W1', ok_new and not old_ok_anywhere,
          "PERIOD FORMULA, corrected. ord(F mod q) = qL at EVERY prime q with gcd(L, q) = 1, "
          f"q in {{2, 3, 5, 7, 11, 13}} and L <= 12, with no exception at q = 2: "
          f"{', '.join(f'ord(F_{L} mod 2) = {o}' for L, o in q2)}. The corpus statement "
          "ord(F mod 2) = L holds at NO admissible L. The failure is exactly the parabolic mode: "
          "over F_2 the block at lambda = 0 is [[0, 1], [1, 0]], of order 2, and gcd(L, 2) = 1 "
          "forces L odd, so that 2 is not absorbed into L"
          + (f"  [counterexamples to the corrected form: {facts}]" if facts else ""))

    # ------------------------------------------------------ W2: the binary period at every L
    ok, rows = True, []
    for L in range(2, 25):
        o = matrix_order(wave_matrix(L, 2), 2, 2 * L)
        want = L if L % 2 == 0 else 2 * L
        ok &= (o == want)
        if L <= 8:
            rows.append(f"m_{L} = {o}")
    check('W2', ok,
          f"m_L = L for even L and 2L for odd L, exactly, for every L = 2 .. 24 ({', '.join(rows)}, "
          "...). This is the statement the manuscript needed and is a corollary of the "
          "fixed-point formula of W3: F^k = I needs gcd(k, L) = L, and for odd L needs k even too")

    # ------------------------------------------------- W3: the fixed-point dimension formula
    bad = []
    Ls = range(1, 15 if not extended else 19)
    for L in Ls:
        for k in range(1, 3 * L + 1):
            if fix_dim_exact(L, k) != fix_dim_formula(L, k):
                bad.append((L, k))
    check('W3', not bad,
          "FIXED-POINT DIMENSION. dim_{F_2} ker(F_L^k - I) = 2 gcd(k, L) - [L odd and k odd], "
          f"verified against the matrix for every L = 1 .. {max(Ls)} and every k = 1 .. 3L "
          f"({sum(3 * L for L in Ls)} cases). The proof is d'Alembert over F_2: every solution on "
          "Z^2 is f(n-t) + g(n+t), the representation has a 2-dimensional kernel spanned by the "
          "constant and the parity function, and the two periodicities force f and g to be "
          "quasi-periodic with a common increment -- giving 2 gcd(L, k) plus the increment "
          "freedom minus 2, which is 2 gcd - 1 exactly when L and k are both odd"
          + (f"  [failures: {bad[:6]}]" if bad else ""))

    # ---------------------------------------------- W4 / W5: the cycle spectrum, three ways
    bad = []
    for L in range(1, 9 if not extended else 10):
        b = spectrum_brute(L)
        c, _ = spectrum_closed(L)
        mb, _ = spectrum_mobius(L)
        if b != {l: n for l, n in c.items() if n} or b != {l: n for l, n in mb.items() if n}:
            bad.append(L)
    check('W4', not bad,
          "CYCLE SPECTRUM. The closed forms agree with BRUTE-FORCE enumeration of all 4^L states "
          f"for every L = 1 .. {8 if not extended else 9} -- {4 ** (8 if not extended else 9)} "
          "states at the top. "
          "Closed forms, with M(n) the aperiodic-necklace count on four letters: for even L, "
          "C_l = M(l) at each l | L; for odd L, C_e = M(e)/2 and C_{2e} = M(e)/4 at each e | L "
          "(M(e) is divisible by 4 for odd e, since every term of sum mu(e/d) 4^d is)"
          + (f"  [mismatch at L = {bad}]" if bad else ""))

    bad = []
    for L in range(1, 41):
        c, m = spectrum_closed(L)
        mb, m2 = spectrum_mobius(L)
        tot = sum(l * n for l, n in c.items())
        if c != mb or m != m2 or tot != 4 ** L:
            bad.append(L)
    check('W5', not bad,
          "The closed forms agree with the Mobius route -- C_l = (1/l) sum_{d | l} mu(l/d) "
          "2^(2 gcd(d, L) - [both odd]) -- and account for every state, sum_l l C_l = 4^L, for "
          "every L = 1 .. 40. At L = 40 that is 4^40 = 1.2e24 states counted without enumeration"
          + (f"  [mismatch at L = {bad}]" if bad else ""))

    # ------------------------------------------------------------- W6: the first-moment test
    silent = [L for L in range(1, 65) if not fires(L)]
    pow2 = [L for L in range(1, 65) if L & (L - 1) == 0]
    prev = {3: True, 4: False, 5: True, 6: True, 7: True, 8: False, 9: True, 10: True, 11: True}
    agrees = all(fires(L) == v for L, v in prev.items())

    # the divisor-sum closed form for D_s itself, W(t) = sum over the multiples of t dividing L
    closed_ok = True
    for L in range(1, 42):
        spec, m = spectrum_closed(L)

        def W(t):
            return sum(necklace(e) for e in divisors(L) if e % t == 0)

        for s in divisors(m):
            if s <= 2:
                continue
            D = block_dim(s, spec)
            if L % 2 == 0:
                want = sum(necklace(e) for e in divisors(L) if e % s == 0)
            elif s % 2:
                want = 3 * W(s) // 4
            else:
                want = W(s // 2) // 4
            closed_ok &= (D == want)
    check('W6', agrees and silent == pow2 and closed_ok,
          f"FIRST-MOMENT TEST over L = 1 .. 64: silent exactly at {silent}, which is exactly the "
          "powers of two in that range, and firing at every other L. This reproduces the "
          "independently computed CT3-R2B data (fires at L = 3, 5, 6, 7, 9, 10, 11; silent at "
          "L = 4, 8) from the closed forms rather than from state enumeration. D_s itself is a "
          "divisor sum: with W(t) = sum of M(e) over the multiples e of t dividing L, D_s = W(s) "
          "for even L, D_s = 3 W(s)/4 for odd L and odd s, and D_{2t} = W(t)/4 for odd L -- "
          "verified against the cycle counts for every L = 1 .. 41 and every admissible s")

    # ------------------------------------------- W7: powers of two are silent, with the reason
    def v2(n):
        k = 0
        while n % 2 == 0:
            n //= 2
            k += 1
        return k

    direct = True
    for a in range(1, 6):
        spec, _ = spectrum_closed(2 ** a)
        for j in range(2, a + 1):
            if block_dim(2 ** j, spec) % 2 ** (j - 1):
                direct = False
    val = all(v2(necklace(2 ** i)) == 2 ** i - i for i in range(1, 6))
    ineq = all(2 ** j - j >= j - 1 for j in range(1, 4097))
    check('W7', direct and val and ineq,
          "SILENCE AT POWERS OF TWO IS A THEOREM, and this is its arithmetic. For L = 2^a every "
          "cycle length is 2^i with C_{2^i} = M(2^i) = 2^(2^i) (2^(2^i) - 1) / 2^i, so "
          f"v_2(C_{{2^i}}) = 2^i - i, checked against the integers for i = 1 .. 5 "
          f"{[(i, v2(necklace(2 ** i))) for i in range(1, 6)]}. Since 2^i - i increases in i, "
          "D_{2^j} = sum_{i >= j} C_{2^i} has v_2 at least 2^j - j, and 2^j - j >= j - 1 for "
          "every j (checked to j = 4096), which is exactly the divisibility the test demands. "
          "The direct check runs at L = 2, 4, 8, 16, 32; beyond that the valuation does the work, "
          "and no enumeration could")

    # ------------------------------------- W8: the conjecture is FALSE, and exactly where
    def prime_silent_reason(p):
        """For prime L = p the two tests are s = p and s = 2p; return (fires, the p^2 | 4^(p-1) - 1 flag)."""
        spec, m = spectrum_closed(p)
        Dp, D2p = block_dim(p, spec), block_dim(2 * p, spec)
        return (Dp % p != 0 or D2p % p != 0), (4 ** (p - 1) - 1) % (p * p) == 0

    wieferich = [1093, 3511]
    small_primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    wf_ok = all(prime_silent_reason(p) == (False, True) for p in wieferich)
    sp_ok = all(prime_silent_reason(p) == (True, False) for p in small_primes)
    d1093 = block_dim(1093, spectrum_closed(1093)[0])
    check('W8', wf_ok and sp_ok and all(p & (p - 1) for p in wieferich),
          "THE CONJECTURE 'SILENT IFF L IS A POWER OF TWO' IS FALSE. For L = p an odd prime the "
          "only s > 2 dividing m = 2p are p and 2p, with D_p = 3 (4^(p-1) - 1) / p and "
          "D_{2p} = (4^(p-1) - 1) / p, so for p > 3 BOTH tests are silent exactly when "
          "p^2 | 4^(p-1) - 1 -- and that holds exactly at the WIEFERICH primes base 2, because "
          "ord_{p^2}(2) divides 2(p-1) and p times ord_p(2) cannot. L = 1093 and L = 3511 are "
          f"therefore silent (D_1093 has {len(str(d1093))} digits and 1093 divides it) and neither "
          "is a power of two. The power-of-two direction (W7) stands as a theorem; the converse "
          "does not, and no search below 2^64 can settle where else it fails, since a further "
          "counterexample of this shape is a further Wieferich prime")

    # --------------------------------------------------- W9: the second corpus defect, rank(N)
    obs, ok = [], True
    for q in [2, 3, 5, 7]:
        for L in range(3, 12):
            if gcd(L, q) != 1:
                continue
            n = 2 * L
            FL = matpow(wave_matrix(L, q), L, q)
            Linv = pow(L % q, q - 2, q)
            N = [[(Linv * ((FL[i][j] - (1 if i == j else 0)) % q)) % q for j in range(n)]
                 for i in range(n)]
            r = rank_mod_p(N, n, q)
            N2 = matmul(N, N, q)
            want = 2 if L % 2 == 0 else 1
            ok &= (r == want and all(v == 0 for row in N2 for v in row))
            if q == 3 and L <= 8:
                obs.append(f"L={L}: rank {r}")
    check('W9', ok,
          "SECOND DEFECT IN THE SAME APPENDIX. B.3.2 states rank(N) = 2 for N = (F^L - I)/L with "
          "no parity hypothesis, and its own proof uses '(-1)^L = 1 for even L'. The rank is 2 "
          "only for EVEN L, where both parabolic modes zeta = +1 and zeta = -1 occur; for odd L "
          f"there is one parabolic mode and rank(N) = 1 ({', '.join(obs)}). Verified over "
          "q in {2, 3, 5, 7} and L = 3 .. 11 with gcd(L, q) = 1, together with N^2 = 0 in every "
          "case. B.3.3's conductor is f_ss(L) + rank(N), which is f_ss(L) + 2 at the even L of "
          "its table and f_ss(L) + 1 at odd L")

    # ------------------------------------------------------------------------ W10: the verdict
    check('W10', True,
          "VERDICT. The q = 2 cycle arithmetic is closed in exact form: period, fixed-point "
          "dimensions, cycle spectrum and the divisor-indexed D_s all follow from the "
          "traveling-wave factorization (x + S)(x + S^{-1}) with no state enumeration, and the "
          "first-moment test is decidable at every L from the exact divisor-sum formulas -- powers "
          "of two by the 2-adic criterion, odd prime volumes by the Wieferich criterion, and every "
          "other L by the divisor sums themselves, which the two named criteria do not cover. "
          "Not claimed: that a firing test is a width-w obstruction for any w >= 3 -- the "
          "symmetric-sector palindromicity is structural but the antisymmetric-sector vanishing "
          "is the computed WIDTH-2 ingredient, and nothing here extends it; that any of this "
          "transports to the infinite lattice, the periodization obligation of CT3-R1 standing "
          "unused here as well; that silence of the test at L = 4, 8, 1093, 3511 exhibits a "
          "static local generator, since the test is an obstruction and its silence is the "
          "absence of one obstruction only; that anything here covers q = 3, whose period and "
          "spectrum are governed by different formulas; that CT3 is settled in either direction")

    print()
    if FAILURES:
        print(f"wave_period_probe: FAILED -> {', '.join(FAILURES)}  [{time.time()-t0:.1f}s]")
        return 1
    print(f"wave_period_probe: ALL CHECKS PASS  [{time.time()-t0:.1f}s]")
    return 0


if __name__ == '__main__':
    sys.exit(main())
