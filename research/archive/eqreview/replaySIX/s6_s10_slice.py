"""EQ4-SIX probe s6 -- the S10 slice of K_A and the diagonal-filter action on S10.  Research only.

Usage:  python3 -I -B s6_s10_slice.py <base>/verification/lean-mathlib/OIBridge
Imports the copied library eq4_lib.py (sha256 cc2c6aca94007ac8); sympy for the symbolic restriction only.

S10 = {X = diag(x_0..x_7) + c|000><111| + conj(c)|111><000|}.  GD cap S10 has GHZ eigenvalues
(P0 + C, P0 - C, P1, P1, P2, P2, P3, P3) (fibre b of the strings b, b xor 111; C real).
Written claims (NOTES N2.6 (vi), (vii)):
 (vi)  K_A cap GD cap S10 = H := {P >= 0, |C| <= phi(P)}, phi(P) = min(P0 + P1, P0 + P2, P0 + P3, P1 + P2 + P3,
       (P0 + P1 + P2 + P3)/2), and H is self-dual for sum_j P_j P'_j + C C' (proportional to the trace pairing).
 (vii) a diagonal filter (x)_j diag(1, t_j) maps x_a to x_a prod_j mu_j^{a_j} and c to c prod_j conj(t_j)
       (mu_j = |t_j|^2), so it keeps S10 and keeps rho = x_0 x_3 x_5 x_6 / (x_7 x_1 x_2 x_4).

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `S6-S10-SLICE-EXACT` iff all:
  K  transcription control.
  A  restricting the 92 generators of K_A (= its inequalities, K_A self-dual) to the slice: every inequality with a
     C-term gives a bound |C| <= f(P); the bounds not dominated coefficientwise by another bound are exactly the five
     forms of phi; every inequality without a C-term has nonnegative coefficients.
  B  self-duality of H: with F the 14 inequality rows of H ((e_j, 0) and (l_i, +-1)), F F^T >= 0 entrywise (so
     H* <= H), and the extreme rays of H (exact enumeration over 4-subsets of rows) pair >= 0 with each other (so
     H <= H*).  Countercontrol: without the form (P0 + P1 + P2 + P3)/2 the ray pairing has a negative entry.
  C  for t = (2, 3, 1/2) and for t = (1, i, 1 + i) (exact Gaussian), Ad(D) of all 10 S10 basis elements equals the
     predicted scaling; rho is unchanged on 3 random exact S10 elements; countercontrol: the filter
     (x) [[1, 1], [0, 1]] maps |000><111| outside S10.
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import sympy as sp  # noqa: E402

import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("s6_s10_slice")
rng = random.Random(2026100961)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])
X3 = (0, 1, 2)


# ------------------------------------------------------------------------------------------------ A the slice
def KA_gens():
    G = []
    for j, k in itertools.combinations(range(8), 2):
        G.append([1 if i in (j, k) else 0 for i in range(8)])
    for j in range(8):
        G.append([1 - 2 * (i == j) for i in range(8)])
    for j in range(8):
        for p in range(8):
            if p != j:
                G.append([1 - 2 * (i == j) + 2 * (i == p) for i in range(8)])
    return G


Ps = sp.symbols("P0:4", real=True)
Cs = sp.Symbol("C", real=True)
lam = [Ps[0] + Cs, Ps[0] - Cs, Ps[1], Ps[1], Ps[2], Ps[2], Ps[3], Ps[3]]
bounds, cfree = set(), set()
gens = KA_gens()
for g in gens:
    f = sp.expand(sum(gi * li for gi, li in zip(g, lam)))
    e_ = f.coeff(Cs)
    co = tuple(sp.Rational(f.coeff(P)) for P in Ps)
    if e_ == 0:
        cfree.add(co)
    else:
        bounds.add(tuple(c / abs(e_) for c in co))
minimal = {b for b in bounds if not any(all(o[i] <= b[i] for i in range(4)) and o != b for o in bounds)}
h = sp.Rational(1, 2)
expect = {(1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 1), (h, h, h, h)}
expect = {tuple(sp.Rational(c) for c in e) for e in expect}
rep.check("A the 92 K_A inequalities restricted to GD cap S10: the undominated C-bounds are exactly the five forms of "
          "phi (%d generators, %d distinct C-bounds, %d C-free forms, all with nonnegative coefficients)"
          % (len(gens), len(bounds), len(cfree)),
          len(gens) == 92 and minimal == expect and all(all(c >= 0 for c in co) for co in cfree))


# ------------------------------------------------------------------------------------------------ B self-duality of H
def rows_of(forms):
    R = [tuple([Fr(int(j == i)) for j in range(4)] + [Fr(0)]) for i in range(4)]
    for fm in forms:
        for s in (1, -1):
            R.append(tuple([Fr(fm[i].p, fm[i].q) for i in range(4)] + [Fr(s)]))
    return R


def nullvec(M):
    """one generator of the null space of a 4 x 5 rational matrix of rank 4 (None otherwise)."""
    A = [list(r) for r in M]
    n = 5
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = 1 / A[r][c]
        A[r] = [v * inv for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    if r != 4:
        return None
    free = [c for c in range(n) if c not in piv][0]
    v = [Fr(0)] * n
    v[free] = Fr(1)
    for i, c in enumerate(piv):
        v[c] = -A[i][free]
    return tuple(v)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def extreme_rays(R):
    rays = set()
    for sub in itertools.combinations(R, 4):
        v = nullvec(sub)
        if v is None:
            continue
        for s in (1, -1):
            w = tuple(s * x for x in v)
            if all(dot(r, w) >= 0 for r in R):
                m = max(abs(x) for x in w)
                rays.add(tuple(x / m for x in w))
    return rays


R_full = rows_of(sorted(expect))
ok_ff = all(dot(a, b) >= 0 for a in R_full for b in R_full)
rays = extreme_rays(R_full)
ok_rr = all(dot(a, b) >= 0 for a in rays for b in rays)
R_cc = rows_of(sorted(e for e in expect if e != (h, h, h, h)))
rays_cc = extreme_rays(R_cc)
min_cc = min(dot(a, b) for a in rays_cc for b in rays_cc)
rep.check("B H is self-dual: F F^T >= 0 entrywise (14 rows) and its %d extreme rays pair >= 0; countercontrol: "
          "without (P0 + P1 + P2 + P3)/2 the extreme rays pair to %s < 0" % (len(rays), min_cc),
          ok_ff and ok_rr and len(rays) > 0 and min_cc < 0)


# ------------------------------------------------------------------------------------------------ C diagonal filters
def s10_basis():
    B = [L.unit(X3, a, a) for a in range(8)]
    B.append(L.Op(X3, {(0, 7): L.ONE, (7, 0): L.ONE}))
    B.append(L.Op(X3, {(0, 7): L.I_, (7, 0): -L.I_}))
    return B


def diag_filter(t):
    return L.tensor(*[L.Op((q,), {(0, 0): L.ONE, (1, 1): L.G.of(t[q])}) for q in range(3)])


def predicted(X, t):
    out = {}
    mu = [L.G.of(tq).abs2() for tq in t]
    for a in range(8):
        v = X.get(a, a)
        if not v.is_zero():
            m = Fr(1)
            for q in range(3):
                if (a >> (2 - q)) & 1:
                    m *= mu[q]
            out[(a, a)] = v * L.G(m)
    ct = L.ONE
    for tq in t:
        ct = ct * L.G.of(tq).conj()
    c = X.get(0, 7)
    if not c.is_zero():
        out[(0, 7)] = c * ct
        out[(7, 0)] = (c * ct).conj()
    return L.Op(X3, out)


def rho(X):
    x = [X.get(a, a).re for a in range(8)]
    return x[0] * x[3] * x[5] * x[6] / (x[7] * x[1] * x[2] * x[4])


ok_c = True
for t in [(L.G(2), L.G(3), L.G(Fr(1, 2))), (L.G(1), L.G(0, 1), L.G(1, 1))]:
    D = diag_filter(t)
    for X in s10_basis():
        ok_c &= L.ad(D, X) == predicted(X, t)
    for _ in range(3):
        x = [Fr(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(8)]
        c = L.G(Fr(rng.randint(-5, 5), 3), Fr(rng.randint(-5, 5), 2))
        d = {(a, a): L.G(x[a]) for a in range(8)}
        d[(0, 7)] = c
        d[(7, 0)] = c.conj()
        X = L.Op(X3, d)
        Y = L.ad(D, X)
        ok_c &= rho(Y) == rho(X) and Y == predicted(X, t)
K = L.tensor(*[L.Op((q,), {(0, 0): L.ONE, (0, 1): L.ONE, (1, 1): L.ONE}) for q in range(3)])
Yk = L.ad(K, L.Op(X3, {(0, 7): L.ONE}))
off = [(r, c) for (r, c), v in Yk.d.items() if not v.is_zero() and r != c and (r, c) not in ((0, 7), (7, 0))]
rep.check("C diagonal filters act on S10 by the predicted scaling (10 basis elements, 2 exact filters) and keep rho "
          "(6 random exact elements); countercontrol: an upper-triangular filter maps |000><111| outside S10 "
          "(%d off-S10 entries)" % len(off), ok_c and len(off) > 0)
rep.verdict("S6-S10-SLICE-EXACT")
