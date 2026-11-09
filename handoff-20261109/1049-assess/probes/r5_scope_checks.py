"""ASSESS-1049 r5: exact generic checks for R4-B1 (F7 extended) and nits M1, M5.

WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).

Label: EXACT GENERIC CHECK. Exact integer arithmetic on finite sets: permutations of Z/q,
generic functions on (Z/q)^n, and the one-step second-order wave update on a 3-site ring,
conjugated once. It iterates no dynamics, computes no observable and instantiates no OI
mechanism. It imports nothing from probes/ or review/; every object is coded here from its
definition. Run with `python3 -I`.

S1 (F7)    Every permutation of Z/q is tested for affinity directly (p affine iff
           p(x) = p(0) + (p(1) - p(0)) x for all x, with p(1) - p(0) a unit). The affine ones number
           q * phi(q), and they are all of S_q exactly when q <= 3, for q = 2..8.
S2 (R4-B1) Slice lemma. For a permutation s of Z/q with inverse t, and units u, v, the two-slot
           map S(a, b) = s(u t(a) + v t(b)) is affine on (Z/q)^2 iff s is affine. Exhaustive over
           every permutation and every pair of units, q = 2..7. (Paper proof: S(a, s0) and S(s0, b)
           affine give s(u z) and s(v z) affine in s(z); then s(x + y) - s(0) is additive.)
           Consequence: conjugating a linear rule with two unit-coefficient read slots by a
           non-affine relabelling gives a non-affine rule; at q <= 3 no such relabelling exists.
S3 (R4-B1) Whole-update check. The d = 1 second-order wave update on a ring of 3 sites,
           (p, x) -> (x, x_{i-1} + x_{i+1} - p_i) on (Z/q)^6, conjugated site-wise by s, is affine
           iff s is affine, for every permutation s at q = 2, 3, 4, 5.
S4 (M5)    x -> l x + c (l a unit) preserves '+' iff c = 0; every such map preserves x - y + z.
           Exhaustive, q = 2..9.
S5 (M1)    q = 2, n = 6: every affine a.x + b satisfies the kappa-general uniform form
           (F(x + 1) - F(x) independent of x); it satisfies the kappa = 2 form (F(x + 1) = F(x)) iff
           sum(a) is even; the affine rule x_1 fails the kappa = 2 form.
Mutation   A one-slot slice s(u t(a)) does not detect every non-affine s: at q = 8 some
           non-affine s give an affine one-slot slice for every unit u, so S2's second slot is
           load-bearing. A tester that drops the unit condition admits non-bijective maps at q = 4.
"""
import itertools
import math
import sys

FAIL = []


def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        FAIL.append(msg)


def phi(n):
    r, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r = r // p * (p - 1)
        p += 1
    if m > 1:
        r = r // m * (m - 1)
    return r


def units(q):
    return [a for a in range(1, q) if math.gcd(a, q) == 1] if q > 1 else []


def perm_affine(p, q, require_unit=True):
    a = (p[1] - p[0]) % q
    if require_unit and math.gcd(a, q) != 1:
        return False
    return all(p[x] == (p[0] + a * x) % q for x in range(q))


def fn_affine(F, n, q):
    z = (0,) * n
    f0 = F(z) % q
    co = [(F(tuple(1 if j == i else 0 for j in range(n))) - f0) % q for i in range(n)]
    return all(F(x) % q == (f0 + sum(c * v for c, v in zip(co, x))) % q
               for x in itertools.product(range(q), repeat=n))


def inverse(p):
    t = [0] * len(p)
    for i, v in enumerate(p):
        t[v] = i
    return t


# ---- S1 ----
for q in range(2, 9):
    perms = list(itertools.permutations(range(q)))
    naff = sum(1 for p in perms if perm_affine(p, q))
    check(naff == q * phi(q), f"S1 q={q}: {naff} affine permutations (tested) = q*phi(q)")
    check((naff == math.factorial(q)) == (q <= 3),
          f"S1 q={q}: every permutation affine is {naff == math.factorial(q)} (expected {q <= 3})")
check(perm_affine((1, 0, 2, 3), 4) is False, "S1 control q=4: the transposition (0 1) is not affine")
check(perm_affine(tuple((3 * x + 1) % 4 for x in range(4)), 4), "S1 control q=4: 3x+1 is affine")

# ---- S2 ----
for q in range(2, 8):
    ok = True
    n_nonaff = 0
    for p in itertools.permutations(range(q)):
        t = inverse(p)
        aff = perm_affine(p, q)
        n_nonaff += (not aff)
        for u in units(q):
            for v in units(q):
                S = lambda x, p=p, t=t, u=u, v=v: p[(u * t[x[0]] + v * t[x[1]]) % q]
                if fn_affine(S, 2, q) != aff:
                    ok = False
    check(ok, f"S2 q={q}: s(u t(a) + v t(b)) affine iff s affine, every s and units u, v "
              f"({n_nonaff} non-affine s)")


# ---- S3 ----
def wave_conj(p, t, q):
    def F(state):  # state = (p0, p1, p2, x0, x1, x2), conjugated: s o Phi o s^-1
        P = [t[v] for v in state[:3]]
        X = [t[v] for v in state[3:]]
        new = [(X[(i - 1) % 3] + X[(i + 1) % 3] - P[i]) % q for i in range(3)]
        return tuple(p[v] for v in X) + tuple(p[v] for v in new)
    return F


for q in (2, 3, 4, 5):
    ok = True
    for p in itertools.permutations(range(q)):
        t = inverse(p)
        G = wave_conj(p, t, q)
        aff_all = all(fn_affine(lambda s, k=k: G(s)[k], 6, q) for k in range(3, 6))
        if aff_all != perm_affine(p, q):
            ok = False
    check(ok, f"S3 q={q}: the conjugated 3-site wave update is affine iff s is affine (every s)")
# control: identity conjugation gives the linear rule itself
check(all(fn_affine(lambda s, k=k: wave_conj(tuple(range(5)), list(range(5)), 5)(s)[k], 6, 5)
          for k in range(6)), "S3 control q=5: unconjugated wave update is affine")

# ---- S4 ----
ok_hom, ok_tern = True, True
for q in range(2, 10):
    for l in units(q):
        for c in range(q):
            m = lambda x, l=l, c=c, q=q: (l * x + c) % q
            hom = all(m((x + y) % q) == (m(x) + m(y)) % q for x in range(q) for y in range(q))
            ok_hom &= (hom == (c == 0))
            ok_tern &= all(m((x - y + z) % q) == (m(x) - m(y) + m(z)) % q
                           for x in range(q) for y in range(q) for z in range(q))
check(ok_hom, "S4 q=2..9: x -> l x + c preserves '+' iff c = 0")
check(ok_tern, "S4 q=2..9: every x -> l x + c preserves x - y + z")

# ---- S5 ----
n = 6
ok_gen, ok_k2 = True, True
for a in itertools.product(range(2), repeat=n):
    for b in range(2):
        F = lambda x, a=a, b=b: (sum(i * v for i, v in zip(a, x)) + b) % 2
        diffs = {(F(tuple((v + 1) % 2 for v in x)) - F(x)) % 2 for x in itertools.product(range(2), repeat=n)}
        ok_gen &= (len(diffs) == 1)
        ok_k2 &= ((diffs == {0}) == (sum(a) % 2 == 0))
check(ok_gen, "S5 q=2, n=6: every affine a.x + b satisfies the kappa-general uniform form")
check(ok_k2, "S5 q=2, n=6: a.x + b satisfies the kappa = 2 form iff sum(a) is even")
check(not all(((x[0] + 1) % 2) == x[0] for x in itertools.product(range(2), repeat=n)),
      "S5 q=2: the affine rule x_1 fails the kappa = 2 form")

# ---- Mutations ----
q = 8
missed = 0
for p in itertools.permutations(range(q)):
    if perm_affine(p, q):
        continue
    t = inverse(p)
    if all(fn_affine(lambda x, p=p, t=t, u=u: p[(u * t[x[0]]) % q], 1, q) for u in units(q)):
        missed += 1
check(missed > 0, f"Mutation q=8: a one-slot slice misses {missed} non-affine s (second slot load-bearing)")
nonperm = [m for m in itertools.product(range(4), repeat=4)
           if perm_affine(m, 4, require_unit=False) and len(set(m)) < 4]
check(len(nonperm) > 0, f"Mutation q=4: dropping the unit condition admits {len(nonperm)} non-bijective maps")

print("ALL PASS" if not FAIL else f"{len(FAIL)} FAILURES")
sys.exit(1 if FAIL else 0)
