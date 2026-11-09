"""REVIEW-1049-r4: reviewer's independent exact checks for ASSESS-1049 r4.

WIP / UNVERIFIED. Model-written (Claude Code reviewer subagent, 2026-11-09).

Label: EXACT GENERIC CHECK. Exact integer arithmetic on finite sets: permutations of Z/q,
generic local functions, one-step identities. It iterates no dynamics, computes no observable
and instantiates no OI mechanism. It imports nothing from probes/ or review/; every object is
coded here from its definition. Run with `python3 -I`.

W1 (F7)   Affine permutations of Z/q are found by TESTING every permutation (not by generating
          the family): p is affine iff p(x) = p(0) + (p(1) - p(0)) x for all x, with p(1) - p(0)
          a unit. Their count equals q * phi(q), phi from the prime factorisation (not gcd
          counting), and equals q! exactly when q <= 3, for q = 2..8. Integer comparison
          q * phi(q) < q! for 4 <= q <= 200. Controls: a transposition at q = 4 is rejected; 3x + 1
          at q = 4 is accepted. Mutation: a tester that drops the unit condition admits
          non-permutations, so the bijection filter is load-bearing.
W2 (F7)   Kernel carrier (Z/q)^6: |{x -> l x + c}| = q^6 phi(q), and |AGL(6, q)| (prime q, exact
          |GL|) or the bound q^6 * q^36 (composite q) is < (q^6)!, q = 2..7. Note: at (Z/2)^2,
          AGL(2, 2) has 24 = 4! elements, so properness on a K-component carrier needs K's value.
W3 (V1')  x -> l x + c is an automorphism of (Z/q, +) iff c = 0; every such map preserves the
          ternary operation x - y + z. Exhaustive, q = 2..9.
W4 (F6)   F6's witnesses, re-coded: d = 2, q = 7, f = 4*sum + y3 * chi(y1^2 - y2^2) (4 = 1/2);
          d = 3, q = 5, f = 2*sum + C * P^(q-2) (2 = 1/3); d = 3, q = 2, f = sum + [all equal].
          Each satisfies f(l x + c1) = l f(x) + 2c for every unit l, every c and every x, and is
          not affine. Countercontrol: the affine rule 4*sum + 1 at q = 7 fails l = -1.
W5 (F1)   q = 2, n = 6: the affine rule x_1 fails the kappa = 2 uniform form; a.x + b satisfies
          kappa = 2 iff sum(a) is even. So at q = 2 the comparative holds in the kappa-general
          form for every affine rule, and in the kappa = 2 form only for sum(a) even.
W6 (N4/G1) The single-slot map x -> x^2 is affine on Z/q iff q = 2, q = 2..16.
"""
import itertools
import math
import sys

FAIL = []


def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        FAIL.append(msg)


def prime_factors(n):
    f, p = set(), 2
    while p * p <= n:
        while n % p == 0:
            f.add(p)
            n //= p
        p += 1
    if n > 1:
        f.add(n)
    return f


def phi(n):
    r = n
    for p in prime_factors(n):
        r = r // p * (p - 1)
    return r


def is_unit(a, q):
    return math.gcd(a % q, q) == 1


def perm_is_affine(p, q, require_unit=True):
    a = (p[1] - p[0]) % q if q > 1 else 0
    if require_unit and not is_unit(a, q):
        return False
    return all(p[x] == (p[0] + a * x) % q for x in range(q))


# ---- W1 (F7) ----
for q in range(2, 9):
    perms = list(itertools.permutations(range(q)))
    naff = sum(1 for p in perms if perm_is_affine(p, q))
    check(naff == q * phi(q), f"W1 q={q}: {naff} affine permutations (tested) = q*phi(q) = {q * phi(q)}")
    check((naff == math.factorial(q)) == (q <= 3),
          f"W1 q={q}: affine permutations {'=' if naff == math.factorial(q) else '<'} q! = {math.factorial(q)}")
check(all(q * phi(q) < math.factorial(q) for q in range(4, 201)),
      "W1 integer: q*phi(q) < q! for every 4 <= q <= 200")
check(all(q * phi(q) == math.factorial(q) for q in (2, 3)), "W1 integer: q*phi(q) = q! at q = 2, 3")
check(not perm_is_affine((1, 0, 2, 3), 4), "W1 control q=4: the transposition (0 1) is not affine")
check(perm_is_affine(tuple((3 * x + 1) % 4 for x in range(4)), 4), "W1 control q=4: 3x+1 is affine")
# mutation: without the unit condition the tester accepts maps that are not permutations
nonperm = [m for m in itertools.product(range(4), repeat=4)
           if perm_is_affine(m, 4, require_unit=False) and len(set(m)) < 4]
check(len(nonperm) > 0, f"W1 mutation q=4: dropping the unit condition admits {len(nonperm)} non-bijective maps")


# ---- W2 (kernel carrier (Z/q)^6) ----
def gl_order_prime(K, p):
    r = 1
    for i in range(K):
        r *= p ** K - p ** i
    return r


for q in range(2, 8):
    N = q ** 6
    scalar = N * phi(q)
    full = N * (gl_order_prime(6, q) if len(prime_factors(q)) == 1 and q in prime_factors(q) else q ** 36)
    fact = math.factorial(N)
    check(scalar < fact and full < fact, f"W2 q={q}: |x->lx+c| and |AGL(6)| (or bound) < ({N})!")
check(4 * gl_order_prime(2, 2) == math.factorial(4), "W2 note: |AGL(2,2)| = 24 = 4! (K = 2, q = 2 is not proper)")

# ---- W3 (V1': shifts are not additive automorphisms) ----
ok_hom, ok_tern = True, True
for q in range(2, 10):
    for l in range(1, q):
        if not is_unit(l, q):
            continue
        for c in range(q):
            m = lambda x: (l * x + c) % q
            hom = all(m((x + y) % q) == (m(x) + m(y)) % q for x in range(q) for y in range(q))
            if hom != (c == 0):
                ok_hom = False
            if not all(m((x - y + z) % q) == (m(x) - m(y) + m(z)) % q
                       for x in range(q) for y in range(q) for z in range(q)):
                ok_tern = False
check(ok_hom, "W3 q=2..9: x -> lx + c preserves '+' iff c = 0")
check(ok_tern, "W3 q=2..9: every x -> lx + c preserves x - y + z")


# ---- W4 (F6 witnesses) ----
def is_affine_fn(F, n, q):
    z = (0,) * n
    f0 = F(z)
    co = [(F(tuple(1 if j == i else 0 for j in range(n))) - f0) % q for i in range(n)]
    return all(F(x) % q == (f0 + sum(a * v for a, v in zip(co, x))) % q
               for x in itertools.product(range(q), repeat=n))


def uniform_k2(F, n, q):
    for l in range(1, q):
        if not is_unit(l, q):
            continue
        for c in range(q):
            for x in itertools.product(range(q), repeat=n):
                if F(tuple((l * v + c) % q for v in x)) % q != (l * F(x) + 2 * c) % q:
                    return False
    return True


def legendre7(a):
    a %= 7
    if a == 0:
        return 0
    return 1 if a in {1, 2, 4} else 6  # 6 = -1 mod 7


def f_d2(x):  # slots (E, W, N, S)
    E, W, N, S = x
    y1, y2, y3 = E - W, N - S, E + W - N - S
    return (4 * (E + W + N + S) + y3 * legendre7(y1 * y1 - y2 * y2)) % 7


def f_d3q5(x):  # slots (+x, -x, +y, -y, +z, -z)
    q = 5
    px, py, pz = x[0] + x[1], x[2] + x[3], x[4] + x[5]
    a, b, c = 2 * px - py - pz, 2 * py - pz - px, 2 * pz - px - py
    C, P = a * b * c, a * a + b * b + c * c
    return (2 * sum(x) + C * pow(P % q, q - 2, q)) % q


def f_d3q2(x):
    return (sum(x) + (1 if len(set(x)) == 1 else 0)) % 2


for name, F, n, q in (("d=2 q=7", f_d2, 4, 7), ("d=3 q=5", f_d3q5, 6, 5), ("d=3 q=2", f_d3q2, 6, 2)):
    check(uniform_k2(F, n, q), f"W4 {name}: every uniform x -> lx + c1 is an exact symmetry (kappa = 2)")
    check(not is_affine_fn(F, n, q), f"W4 {name}: not affine")
check(not uniform_k2(lambda x: (4 * sum(x) + 1) % 7, 4, 7),
      "W4 countercontrol d=2 q=7: affine 4*sum + 1 fails the uniform form (b != 0)")
check(uniform_k2(lambda x: (4 * sum(x)) % 7, 4, 7), "W4 control d=2 q=7: 4*sum satisfies the uniform form")

# ---- W5 (F1 at q = 2) ----
n = 6
x1_fails = not all(((x[0] + 1) % 2) == x[0] for x in itertools.product(range(2), repeat=n))
check(x1_fails, "W5 q=2: the affine rule x_1 fails the kappa=2 uniform form")
ok = True
for a in itertools.product(range(2), repeat=n):
    for b in range(2):
        F = lambda x: (sum(i * v for i, v in zip(a, x)) + b) % 2
        k2 = all(F(tuple((v + 1) % 2 for v in x)) == F(x) for x in itertools.product(range(2), repeat=n))
        if k2 != (sum(a) % 2 == 0):
            ok = False
check(ok, "W5 q=2, n=6: a.x + b satisfies the kappa=2 form iff sum(a) is even")

# ---- W6 (N4/G1) ----
check(all(is_affine_fn(lambda x, q=q: (x[0] * x[0]) % q, 1, q) == (q == 2) for q in range(2, 17)),
      "W6 q=2..16: x -> x^2 is affine on Z/q iff q = 2")

print("ALL PASS" if not FAIL else f"{len(FAIL)} FAILURES")
sys.exit(1 if FAIL else 0)
