#!/usr/bin/env python3
"""PREP-REGRESS-1 exact controls (paper-only unit; small exact cases, no sweeps).

All information quantities are in bits and are computed exactly. Every
probability used is a rational whose numerator and denominator factor over
{2, 3}, so every entropy is an exact element a + b*log2(3) with rational a, b.
Signs of such elements are decided by integer comparisons (3^q vs 2^p), so no
floating-point value certifies any equality or inequality below.

Run:  python3 -I prep_regress_checks.py      (exit status 0 iff every check holds)
"""
from fractions import Fraction as Fr
from itertools import permutations, product
import sys


# ---------------------------------------------------------------- exact numbers
class L:
    """a + b*log2(3), a and b rational."""

    def __init__(self, a=0, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = o if isinstance(o, L) else L(o)
        return L(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return L(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, L) else L(o)))

    def __rsub__(self, o):
        return L(o) - self

    def scale(self, r):
        r = Fr(r)
        return L(self.a * r, self.b * r)

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        # a + b*l3 > 0  <=>  l3 > -a/b (b>0)  or  l3 < -a/b (b<0)
        r = -a / b
        p, q = r.numerator, r.denominator  # q > 0
        # l3 > p/q  <=>  3^q > 2^p   (for p >= 0; for p < 0 always true)
        if p < 0:
            gt = True
        else:
            lhs, rhs = 3 ** q, 2 ** p
            if lhs == rhs:  # impossible for q >= 1, kept for completeness
                return 0
            gt = lhs > rhs
        return 1 if (gt == (b > 0)) else -1

    def __eq__(self, o):
        o = o if isinstance(o, L) else L(o)
        return self.a == o.a and self.b == o.b

    def __repr__(self):
        if self.b == 0:
            return f"{self.a}"
        return f"{self.a} + {self.b}*log2(3)"


def log2_rational(x):
    x = Fr(x)
    assert x > 0
    out = L()
    for n, s in ((x.numerator, 1), (x.denominator, -1)):
        for prime in (2, 3):
            while n % prime == 0:
                n //= prime
                out = out + (L(s) if prime == 2 else L(0, s))
        assert n == 1, "probability outside the {2,3} field"
    return out


def H(dist):
    """Shannon entropy (bits) of {outcome: Fraction}."""
    tot = L()
    for p in dist.values():
        if p:
            tot = tot - log2_rational(p).scale(p)
    return tot


def marginal(dist, idx):
    out = {}
    for s, p in dist.items():
        k = tuple(s[i] for i in idx)
        out[k] = out.get(k, 0) + p
    return out


def D_unif(dist, nbits):
    """D(p || uniform on {0,1}^nbits)."""
    return L(nbits) - H(dist)


def push(dist, f):
    out = {}
    for s, p in dist.items():
        t = f(s)
        out[t] = out.get(t, 0) + p
    return out


def K(dist, held, n):
    """K(H) = log|H| - H(H | Rest), H given by bit positions `held`."""
    rest = [i for i in range(n) if i not in held]
    return L(len(held)) - (H(marginal(dist, list(held) + rest)) - H(marginal(dist, rest)))


def h2(eps):
    eps = Fr(eps)
    return H({0: eps, 1: 1 - eps})


def bern(p0):
    return {0: Fr(p0), 1: 1 - Fr(p0)}


def product_law(*factors):
    out = {(): Fr(1)}
    for f in factors:
        new = {}
        for s, p in out.items():
            for v, q in f.items():
                if q:
                    new[s + (v,)] = new.get(s + (v,), 0) + p * q
        out = new
    return out


UNIF = bern(Fr(1, 2))
RESULTS = []


def check(name, cond):
    RESULTS.append((name, bool(cond)))
    print(f"CHECK {name}: {'PASS' if cond else 'FAIL'}")


# ---------------------------------------------------------------- gates
def cnot(c, t):
    return lambda s: tuple((s[t] ^ s[c]) if i == t else x for i, x in enumerate(s))


def swap(i, j):
    def f(s):
        s = list(s)
        s[i], s[j] = s[j], s[i]
        return tuple(s)
    return f


# C1  ARROW-1 C.4 reuse example: coarse-grained (marginal) D is not monotone.
p = product_law({0: Fr(1)}, UNIF)  # (v, b), v = 0, b uniform
g = cnot(1, 0)                      # v <- v xor b
D_tot, D_marg, TC = [], [], []
for t in range(3):
    D_tot.append(D_unif(p, 2))
    m = D_unif(marginal(p, [0]), 1) + D_unif(marginal(p, [1]), 1)
    D_marg.append(m)
    TC.append(D_tot[-1] - m)
    p = push(p, g)
check("C1a total D(p_t||u) constant = 1", all(d == L(1) for d in D_tot))
check("C1b sum of marginal D = 1, 0, 1 (rises at t=2)", [str(x) for x in D_marg] == ["1", "0", "1"])
check("C1c total correlation = 0, 1, 0", [str(x) for x in TC] == ["0", "1", "0"])

# C2  swap on its 2-cycle {01,10} under the per-orbit law: budget saturation.
muO = {(0, 1): Fr(1, 2), (1, 0): Fr(1, 2)}
check("C2a D(muO||u) = log2(|S|/l) = 1", D_unif(muO, 2) == L(1))
check("C2b K(V) = 1 and D(p_H||u_H) = 0 (transfer identity 1 = 1 + 0)",
      K(muO, [0], 2) == L(1) and D_unif(marginal(muO, [1]), 1) == L(0))

# C3  swap under the uniform law: K = 0 at every t, yet history memory M_1 = 1 bit.
u2 = product_law(UNIF, UNIF)
sw = swap(0, 1)
ok = True
pt = u2
for _ in range(4):
    ok &= K(pt, [0], 2) == L(0)
    pt = push(pt, sw)
traj = push(u2, lambda s: (s[0], sw(s)[0], sw(sw(s))[0]))  # (X0, X1, X2)
M1 = (H(marginal(traj, [0, 1])) + H(marginal(traj, [1, 2]))
      - H(marginal(traj, [1])) - H(traj))
check("C3a K(V)=0 for t=0..3 under u", ok)
check("C3b M_1 = I(X0;X2|X1) = 1 bit under u (memory is budget-free)", M1 == L(1))


# C4  tight record protocol, N = 2 retained records + re-armed register.
#     bits: 0 c1, 1 c2, 2 r, 3 l1, 4 l2
def run_protocol(p0):
    steps = [cnot(0, 2), swap(2, 3), cnot(1, 2), swap(2, 4)]
    D0 = D_unif(p0, 5)
    held = [2, 3, 4]
    rest = [0, 1]
    ok_cons, ok_transfer = True, True
    p = p0
    for st in [None] + steps:
        if st is not None:
            p = push(p, st)
        ok_cons &= D_unif(p, 5) == D0
        ok_transfer &= (K(p, held, 5) + D_unif(marginal(p, rest), 2)) == D0
    return D0, p, ok_cons, ok_transfer


p0 = product_law(UNIF, UNIF, {0: Fr(1)}, {0: Fr(1)}, {0: Fr(1)})
D0, pT, c_ok, t_ok = run_protocol(p0)
check("C4a perfect blanks: D0 = 3 bits, conserved at every step", D0 == L(3) and c_ok)
check("C4b transfer identity K_t(H) + D(p_Rest||u) = D0 at every step", t_ok)
err1 = sum(q for s, q in pT.items() if s[3] != s[0])
err2 = sum(q for s, q in pT.items() if s[4] != s[1])
errr = sum(q for s, q in pT.items() if s[2] != 0)
check("C4c final: l1=c1, l2=c2, r=0 exactly; K(H)=3 = (N+1)(1-h(0))",
      err1 == 0 and err2 == 0 and errr == 0 and K(pT, [2, 3, 4], 5) == L(3))

q = Fr(3, 4)
p0n = product_law(UNIF, UNIF, bern(q), bern(q), bern(q))
D0n, pTn, c_ok, t_ok = run_protocol(p0n)
bound = (L(1) - h2(Fr(1, 4))).scale(3)
err1 = sum(x for s, x in pTn.items() if s[3] != s[0])
err2 = sum(x for s, x in pTn.items() if s[4] != s[1])
errr = sum(x for s, x in pTn.items() if s[2] != 0)
check("C4d noisy blanks P(0)=3/4: D0 = 3(1-h(1/4)), conserved; transfer identity holds",
      D0n == bound and c_ok and t_ok)
check("C4e final errors 1/4, 1/4, 1/4 and K(H) = D0 = 3(1-h(1/4)): bound attained",
      err1 == err2 == errr == Fr(1, 4) and K(pTn, [2, 3, 4], 5) == bound)

# C5  reversible copy/uncopy cycles: N cycles at fixed budget, nothing retained.
N = 5
n = N + 1  # bits 0..4 carriers, 5 register
p = product_law(*([UNIF] * N + [{0: Fr(1)}]))
D0 = D_unif(p, n)
ok_mid, ok_end = True, True
for k in range(N):
    p = push(p, cnot(k, N))
    ok_mid &= (H(marginal(p, [N])) + H(marginal(p, [k])) - H(marginal(p, [N, k]))) == L(1)
    p = push(p, cnot(k, N))
    ok_end &= sum(x for s, x in p.items() if s[N] != 0) == 0
check("C5a budget D0 = 1 bit for any N; conserved", D0 == L(1) and D_unif(p, n) == L(1))
check("C5b each of N=5 cycles: I(r;c_k)=1 bit mid-cycle, r re-armed exactly", ok_mid and ok_end)

# C6  exchange record under u: faithful to the past value, zero budget.
p = product_law(UNIF, UNIF)  # (c, l)
pT = push(p, swap(0, 1))
joint = push(p, lambda s: (s[0], swap(0, 1)(s)[1]))  # (c at 0, l at 1)
check("C6 exchange: D0 = 0, P(l_1 = c_0) = 1, K(l) = 0",
      D_unif(p, 2) == L(0) and sum(x for s, x in joint.items() if s[0] != s[1]) == 0
      and K(pT, [1], 2) == L(0))

# C7  conditioning cost: D(u(.|E) || u) = log2(|S|/|E|) exactly.
S3 = list(product((0, 1), repeat=3))
for E in ([s for s in S3 if s[0] == 0 and s[1] == 0], [(0, 0, 0), (0, 0, 1), (1, 1, 1)]):
    uE = {s: Fr(1, len(E)) for s in E}
    check(f"C7 |E|={len(E)}: D(u_E||u) = log2(8/|E|)",
          D_unif(uE, 3) == L(3) - log2_rational(len(E)))

# C8  flux balance for every bijection of a 4-set and every event.
def flux_balanced(phi, size):
    """True iff inflow == outflow for every event E of a map phi on range(size)."""
    for mask in range(2 ** size):
        E = {i for i in range(size) if mask >> i & 1}
        inflow = sum(1 for s in range(size) if s not in E and phi[s] in E)
        outflow = sum(1 for s in range(size) if s in E and phi[s] not in E)
        if inflow != outflow:
            return False
    return True


ok = all(flux_balanced(perm, 4) for perm in permutations(range(4)))
check("C8 flux balance |{s notin E: phi s in E}| = |{s in E: phi s notin E}| (24 x 16 cases)", ok)

# C9  readiness ceiling P_t(E) * M * log2 q <= D0 + 1 on the C4d trajectory (E = r,l1,l2 all 0).
p = p0n
ok = True
for st in [None, cnot(0, 2), swap(2, 3), cnot(1, 2), swap(2, 4)]:
    if st is not None:
        p = push(p, st)
    P = sum(x for s, x in p.items() if s[2] == s[3] == s[4] == 0)
    ok &= (D0n + L(1) - L(3 * P)).sign() >= 0
check("C9 readiness ceiling P_t(E) <= (D0+1)/(M log2 q) at every step", ok)


# C10 collision model (2.7). Bits (r, C1, C2); A = r uniform, C_j ~ Bern(3/4) fresh.
#     Step j: CNOT(r -> C_j), which creates I(A; C_j) > 0. F_j = D(a_j) + sum_{i>j} D(C_i).
def Dm(p, i):
    return D_unif(marginal(p, [i]), 1)


def I2(p, i, j):
    return H(marginal(p, [i])) + H(marginal(p, [j])) - H(marginal(p, [i, j]))


p = product_law(UNIF, bern(q), bern(q))
F = [Dm(p, 0) + Dm(p, 1) + Dm(p, 2)]
ok_dec, ok_I = True, True
for j, unused in ((1, [2]), (2, [])):
    p = push(p, cnot(0, j))
    F.append(Dm(p, 0) + sum((Dm(p, i) for i in unused), L()))
    dec = F[-2] - F[-1]
    ok_I &= I2(p, 0, j).sign() > 0
    ok_dec &= dec == I2(p, 0, j) + Dm(p, j)
check("C10a fresh CNOT steps: I(A;C_j) > 0, decrement = I + D(outgoing), F non-increasing",
      ok_I and ok_dec and all((F[k] - F[k + 1]).sign() >= 0 for k in range(2)))
# reuse of C1 by CNOT(C1 -> r) on the same trajectory: F (no unused cells left) = D(a) rises.
F_before = Dm(p, 0)
p = push(p, cnot(1, 0))
check("C10b reuse of a used cell: D(a) rises from 0 to 1-h(1/4)",
      F_before == L(0) and Dm(p, 0) == L(1) - h2(Fr(1, 4)))

# C12 orbit-selection weight for an unstructured bijection: over all permutations of
#     n = 5 points, the cycle through a fixed point has each length 1..n equally often,
#     so P(length <= l) = l/n and the mu-O budget log2(n/l) has weight l/n.
n5 = 5
counts = [0] * (n5 + 1)
for perm in permutations(range(n5)):
    k, x = 1, perm[0]
    while x != 0:
        x, k = perm[x], k + 1
    counts[k] += 1
check("C12 cycle length through a fixed point is uniform on 1..5 (24 each of 120)",
      counts[1:] == [24] * n5)

# C13 moving block under mu-O (1.3 scope). phi(0,b) = (0,1-b), phi(1,b) = (1,b); orbit {00, 01}.
def phi13(s):
    return (0, 1 - s[1]) if s[0] == 0 else s


muO13 = {(0, 0): Fr(1, 2), (0, 1): Fr(1, 2)}
check("C13 mu-O invariant; moving block K: cell1 at t0 = 0 -> cell0 at t1 = 1 <= D(mu-O||u) = 1",
      push(muO13, phi13) == muO13 and K(muO13, [1], 2) == L(0)
      and K(push(muO13, phi13), [0], 2) == L(1) and D_unif(muO13, 2) == L(1))


# C14 2.5 away from equality: every law on 3 bits with p(s) in {0,1,2,3,4,6}/16 whose
#     quantities stay in the {2,3} field; A = bit0, B = (bit1, bit2), g = id (jointly balanced),
#     f in {(a,a), (a,1-a), (a,0), (1-a,a)}. Checks D(p||u) >= 2 - h(eps1) - h(eps2).
def compositions(total, parts, allowed):
    if parts == 1:
        if total in allowed:
            yield (total,)
        return
    for v in allowed:
        if v <= total:
            for rest in compositions(total - v, parts - 1, allowed):
                yield (v,) + rest


def slack_25(law, nbits, pairs):
    """D(p||u) - (N - sum_k h2(eps_k)) for predictor/target pairs (f_k, g_k) on states."""
    eps = [sum(x for s, x in law.items() if f(s) != g(s)) for f, g in pairs]
    return D_unif(law, nbits) - (L(len(pairs)) - sum((h2(e) for e in eps), L())), eps


S3 = list(product((0, 1), repeat=3))
# A = bit0 predicts B = (bit1, bit2) with g = id (jointly balanced, disjoint).
preds = [lambda a: (a, a), lambda a: (a, 1 - a), lambda a: (a, 0), lambda a: (1 - a, a)]
n_checked = n_strict = 0
ok = True
for comp in compositions(16, 8, (0, 1, 2, 3, 4, 6)):
    law = {s: Fr(c, 16) for s, c in zip(S3, comp) if c}
    for f in preds:
        pairs = [(lambda s, f=f: f(s[0])[0], lambda s: s[1]),
                 (lambda s, f=f: f(s[0])[1], lambda s: s[2])]
        try:
            slack, _ = slack_25(law, 3, pairs)
        except AssertionError:  # a probability outside the {2,3} field: skipped, not checked
            continue
        sg = slack.sign()
        ok &= sg >= 0
        n_checked += 1
        n_strict += sg > 0
check(f"C14 2.5 holds on {n_checked} exact (law, predictor) cases, {n_strict} strictly",
      ok and n_checked > 1000 and n_strict > 0)

# C15 countercontrols for 2.5's hypotheses, through C14's slack_25: the inequality must FAIL.
slack_and, eps_and = slack_25(product_law(UNIF, UNIF), 2, [(lambda s: 0, lambda s: s[0] & s[1])])
check("C15a no joint balancedness (g = AND, f = 0): eps = 1/4 and D = 0 < 1 - h(1/4)",
      eps_and == [Fr(1, 4)] and slack_and.sign() < 0)
copy = {(0, 0): Fr(1, 2), (1, 1): Fr(1, 2)}
slack_cp, eps_cp = slack_25(copy, 2, [(lambda s: s[0], lambda s: s[1]), (lambda s: s[1], lambda s: s[0])])
check("C15b no disjointness (x predicts y, y predicts x): N - sum h = 2 > D = 1",
      eps_cp == [0, 0] and slack_cp == L(-1))

# C11 countercontrols: the exact sign test and C8's flux routine can fail.
check("C11a sign test: 1.58 < log2(3) < 1.59 decided by integer powers",
      (L(0, 1) - Fr(158, 100)).sign() > 0 and (L(0, 1) - Fr(159, 100)).sign() < 0)
check("C11b C8's flux routine reports failure on a non-bijection (constant map)",
      flux_balanced((0, 0, 0, 0), 4) is False)

failed = [n for n, ok in RESULTS if not ok]
print(f"{len(RESULTS) - len(failed)}/{len(RESULTS)} checks hold")
sys.exit(1 if failed else 0)
