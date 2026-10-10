"""EQ4-SIX probe s7 -- the S10 slice of K_tw (c = 1).  Research only.

Usage:  python3 -I -B s7_s10_slice_c1.py <base>/verification/lean-mathlib/OIBridge
Imports the copied library eq4_lib.py (sha256 cc2c6aca94007ac8); sympy for the symbolic restriction only.

c = 1 analogue of s6 (whose part C, the diagonal-filter action on S10, does not depend on c and is not repeated).
GD cap S10 has GHZ eigenvalues (P0 + C, P0 - C, P1, P1, P2, P2, P3, P3).  K_tw (36 generators, self-dual for the
Euclidean pairing; EQ4-P p13, rebuilt as in s5 D from the G-orbits of p0 = e_{0+} + e_{0-},
t = (1,1,1,1,1,-1,1,-1) and k = (-1,3,1,1,1,1,1,1)).
Written claim (NOTES N4): K_tw cap GD cap S10 = H_tw := {P >= 0, |C| <= phi_tw(P)},
phi_tw(P) = min((P0 + P1 + P2 + P3)/2, P1 + P2, P1 + P3, P2 + P3), self-dual for sum_j P_j P'_j + C C'.

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `S7-S10-SLICE-C1-EXACT` iff all:
  K  transcription control.
  A  restricting the 36 generators of K_tw (= its inequalities) to the slice: the C-bounds not dominated
     coefficientwise by another are exactly the four forms of phi_tw; every C-free inequality has nonnegative
     coefficients.
  B  self-duality of H_tw: F F^T >= 0 entrywise on its 12 inequality rows and its extreme rays pair >= 0 with each
     other.  Countercontrol: without (P0 + P1 + P2 + P3)/2 the ray pairing has a negative entry.
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import sympy as sp  # noqa: E402

import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("s7_s10_slice_c1")
rng = random.Random(2026100971)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])
X3 = (0, 1, 2)


# ------------------------------------------------------------------------------------------------ A the slice
def KT_gens():
    p0 = (1, 1, 0, 0, 0, 0, 0, 0)
    t0 = (1, 1, 1, 1, 1, -1, 1, -1)
    k0 = (-1, 3, 1, 1, 1, 1, 1, 1)
    gens7 = [(1, 0, 3, 2, 5, 4, 7, 6), (6, 7, 4, 5, 2, 3, 0, 1), (4, 5, 6, 7, 0, 1, 2, 3), (2, 3, 0, 1, 6, 7, 4, 5),
             (1, 0, 3, 2, 4, 5, 6, 7), (0, 1, 2, 3, 6, 7, 4, 5), (0, 1, 4, 5, 2, 3, 6, 7)]
    group = {tuple(range(8))}
    frontier = [tuple(range(8))]
    while frontier:
        nf = []
        for g in frontier:
            for h in gens7:
                cc_ = tuple(g[h[i]] for i in range(8))
                if cc_ not in group:
                    group.add(cc_)
                    nf.append(cc_)
        frontier = nf
    return sorted({tuple(v[g[i]] for i in range(8)) for v in (p0, t0, k0) for g in group})


Ps = sp.symbols("P0:4", real=True)
Cs = sp.Symbol("C", real=True)
lam = [Ps[0] + Cs, Ps[0] - Cs, Ps[1], Ps[1], Ps[2], Ps[2], Ps[3], Ps[3]]
bounds, cfree = set(), set()
gens = KT_gens()
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
expect = {(0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1), (h, h, h, h)}
expect = {tuple(sp.Rational(c) for c in e) for e in expect}
rep.check("A the 36 K_tw inequalities restricted to GD cap S10: the undominated C-bounds are exactly the four forms "
          "of phi_tw (%d generators, %d distinct C-bounds, %d C-free forms, all with nonnegative coefficients)"
          % (len(gens), len(bounds), len(cfree)),
          len(gens) == 36 and minimal == expect and all(all(c >= 0 for c in co) for co in cfree))


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
rep.check("B H_tw is self-dual: F F^T >= 0 entrywise (12 rows) and its %d extreme rays pair >= 0; countercontrol: "
          "without (P0 + P1 + P2 + P3)/2 the extreme rays pair to %s < 0" % (len(rays), min_cc),
          ok_ff and ok_rr and len(rays) > 0 and min_cc < 0)


rep.verdict("S7-S10-SLICE-C1-EXACT")
