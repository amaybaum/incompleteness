"""ASSESS-1049 r4: exact generic checks for the witnesses r4 states at N2, N3, N4 and F7.

WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).

Label: EXACT GENERIC CHECK. Exact integer arithmetic mod q on generic local functions and
one-step identities. It iterates no dynamics, computes no observable and instantiates no OI
mechanism. It imports nothing from probes/ or review/; every function is coded here from its
definition in ASSESS-1049 r4.

C1 (N4)  q = 2: every map Z/2 -> Z/2 is affine, so sum_j x_j^2 = sum_j x_j on (Z/2)^n.
         q = 3, 5: the centre-free link sum sum_j x_j^2 (n = 4) is not affine, and its uniform-shift
         effect depends on the state. Control: sum_j x_j has a state-independent effect.
C2 (N2)  q = 2, n = 6: every affine rule a.x + b satisfies F(x + c1) = F(x) + kappa c with
         kappa = sum(a); the kappa = 2 (= 0 mod 2) form holds exactly when sum(a) is even, which
         includes every isotropic rule. P1's q = 2, d = 3 rule sum x + [all six equal] satisfies
         the kappa = 2 form and is not affine. Countercontrol (odd q): at q = 3, d = 2 the affine
         rule 2*sum x + 1 fails the lambda = -1 uniform form; 2*sum x satisfies the full form.
C3 (N3)  q = 3, K = 2: m(x1, x2) = ((x1 - x2)^2, 0) is not affine, and m(x + c(1,1)) - m(x) = 0
         for every x and c; under the shift (1, 0) its difference depends on the state.
         Control: an affine map of (Z/3)^2 passes both.
C4 (F7)  For q = 2..7 the permutations of Z/q of the form x -> l x + c (l a unit) number
         q * phi(q); they are all q! permutations exactly when q <= 3.
"""
import itertools
import math
import sys

FAIL = []


def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        FAIL.append(msg)


def units(q):
    return [l for l in range(1, q) if math.gcd(l, q) == 1]


def is_affine(F, n, q):
    """F on (Z/q)^n is affine iff F(x) = F(0) + sum_i (F(e_i) - F(0)) x_i for every x."""
    z = (0,) * n
    f0 = F(z)
    coef = []
    for i in range(n):
        e = [0] * n
        e[i] = 1
        coef.append((F(tuple(e)) - f0) % q)
    for x in itertools.product(range(q), repeat=n):
        if F(x) % q != (f0 + sum(c * xi for c, xi in zip(coef, x))) % q:
            return False
    return True


def shift_effect_state_independent(F, n, q):
    for c in range(q):
        vals = {(F(tuple((xi + c) % q for xi in x)) - F(x)) % q
                for x in itertools.product(range(q), repeat=n)}
        if len(vals) != 1:
            return False
    return True


# ---- C1 (N4) ----
maps = list(itertools.product(range(2), repeat=2))  # all maps Z/2 -> Z/2 as (m(0), m(1))
check(all(is_affine(lambda x, m=m: m[x[0]], 1, 2) for m in maps),
      "C1 q=2: all 4 maps Z/2 -> Z/2 are affine")
for n in (4, 6):
    ok = all(sum(v * v for v in x) % 2 == sum(x) % 2 for x in itertools.product(range(2), repeat=n))
    check(ok, f"C1 q=2, n={n}: sum x_j^2 = sum x_j identically")
for q in (3, 5):
    sq = lambda x, q=q: sum(v * v for v in x) % q
    lin = lambda x, q=q: sum(x) % q
    check(not is_affine(sq, 4, q), f"C1 q={q}, n=4: sum x_j^2 is not affine")
    check(not shift_effect_state_independent(sq, 4, q),
          f"C1 q={q}, n=4: sum x_j^2 has a state-dependent uniform-shift effect (excluded by gauge)")
    check(shift_effect_state_independent(lin, 4, q),
          f"C1 control q={q}, n=4: sum x_j has a state-independent uniform-shift effect")

# ---- C2 (N2) ----
q, n = 2, 6
all_ok, even_ok = True, True
for a in itertools.product(range(2), repeat=n):
    for b in range(2):
        F = lambda x, a=a, b=b: (sum(ai * xi for ai, xi in zip(a, x)) + b) % 2
        kap = sum(a) % 2
        for x in itertools.product(range(2), repeat=n):
            x1 = tuple((v + 1) % 2 for v in x)
            if F(x1) != (F(x) + kap) % 2:
                all_ok = False
            k2 = F(x1) == F(x)  # kappa = 2 = 0 mod 2, c = 1
            if k2 != (kap == 0):
                even_ok = False
check(all_ok, "C2 q=2, n=6: all 128 affine rules satisfy the kappa-general uniform form with kappa = sum(a)")
check(even_ok, "C2 q=2, n=6: an affine rule satisfies the kappa=2 form iff sum(a) is even (isotropic: 6a, even)")
p1q2 = lambda x: (sum(x) + (1 if len(set(x)) == 1 else 0)) % 2
check(all(p1q2(tuple((v + 1) % 2 for v in x)) == p1q2(x) for x in itertools.product(range(2), repeat=6)),
      "C2 q=2, d=3: sum x + [all six equal] satisfies the kappa=2 uniform form")
check(not is_affine(p1q2, 6, 2), "C2 q=2, d=3: sum x + [all six equal] is not affine")


def uniform_form(F, n, q, kappa):
    for l in units(q):
        for c in range(q):
            for x in itertools.product(range(q), repeat=n):
                y = tuple((l * v + c) % q for v in x)
                if F(y) % q != (l * F(x) + kappa * c) % q:
                    return False
    return True


check(not uniform_form(lambda x: (2 * sum(x) + 1) % 3, 4, 3, 2),
      "C2 countercontrol q=3, d=2: 2*sum x + 1 fails the uniform form (lambda = -1)")
check(uniform_form(lambda x: (2 * sum(x)) % 3, 4, 3, 2),
      "C2 control q=3, d=2: 2*sum x satisfies the uniform form, kappa = 2")

# ---- C3 (N3) ----
q = 3
V = list(itertools.product(range(q), repeat=2))


def m3(x):
    return (((x[0] - x[1]) ** 2) % q, 0)


def aff3(x):
    return ((x[0] + 2 * x[1] + 1) % q, (2 * x[0]) % q)


def add(u, v):
    return tuple((a + b) % q for a, b in zip(u, v))


def sub(u, v):
    return tuple((a - b) % q for a, b in zip(u, v))


def is_affine_vec(m):
    m0 = m((0, 0))
    c1, c2 = sub(m((1, 0)), m0), sub(m((0, 1)), m0)
    return all(m(x) == add(m0, add(tuple(x[0] * t % q for t in c1), tuple(x[1] * t % q for t in c2)))
               for x in V)


def diag_ok(m):
    return all(len({sub(m(add(x, (c, c))), m(x)) for x in V}) == 1 for c in range(q))


def axis_dep(m):
    return len({sub(m(add(x, (1, 0))), m(x)) for x in V}) > 1


check(not is_affine_vec(m3), "C3 q=3, K=2: m(x) = ((x1-x2)^2, 0) is not affine")
check(diag_ok(m3), "C3 q=3, K=2: m has a state-independent (zero) effect under every diagonal shift c(1,1)")
check(axis_dep(m3), "C3 q=3, K=2: under the shift (1,0) the effect of m depends on the state")
check(is_affine_vec(aff3) and diag_ok(aff3) and not axis_dep(aff3),
      "C3 control q=3, K=2: an affine map passes the affinity, diagonal and (1,0) tests")

# ---- C4 (F7) ----
for q in range(2, 8):
    perms = list(itertools.permutations(range(q)))
    aff = {tuple((l * x + c) % q for x in range(q)) for l in units(q) for c in range(q)}
    naff = sum(1 for p in perms if p in aff)
    phi = len(units(q))
    check(naff == q * phi, f"C4 q={q}: {naff} affine permutations = q*phi(q) = {q * phi}")
    check((naff == len(perms)) == (q <= 3),
          f"C4 q={q}: affine permutations {'are' if naff == len(perms) else 'are not'} all {len(perms)} permutations")

print("ALL PASS" if not FAIL else f"{len(FAIL)} FAILURES")
sys.exit(1 if FAIL else 0)
