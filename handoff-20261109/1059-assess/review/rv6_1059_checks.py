"""Reviewer checks for ASSESS-1059 r6 (REVIEW-1059-r6). WIP / UNVERIFIED.

Exact arithmetic only (fractions.Fraction, integer roots, sympy) on generic numbers, vectors and
matrices. No OI mechanism, carrier or lift is computed. Imports no earlier script.
Run: python3 -I rv6_1059_checks.py [MUTANT]   (MUTANT in m1..m6; each must turn its check to FAIL)

Notation. For complex a, b and p > 0, D_p(a,b) = |a+b|^p + |a-b|^p - 2(|a|^p + |b|^p).
s = |a|^2, t = |b|^2, w = Re(a conj b), u = |a+b|^2 = s+t+2w, v = |a-b|^2 = s+t-2w, w^2 <= st.

V1  Parallelogram identity for complex a, b (symbolic real and imaginary parts): u + v = 2(s+t),
    u - v = 4w, and w^2 <= st (Lagrange identity st - w^2 = (Im a conj b)^2).
V2  Even exponents, symbolic in s, t, w: D_4, D_6, D_8 are polynomials whose every monomial has
    a nonnegative coefficient and contains st or w^2; so D_p >= 0, and D_p = 0 forces st = 0
    (since w^2 <= st). Control: D_2 = 0 identically.
V3  Non-even exponents, rigorous: p in {1/2, 1, 3/2, 5/2, 3, 7/2} over a Gaussian-rational alphabet
    (all ordered pairs). Each |z|^p = (|z|^2)^(p/2) is enclosed in a rational interval by integer
    k-th roots; for ab != 0 the enclosure of D_p must lie strictly below 0 (p < 2) or above 0
    (p > 2); for ab = 0, D_p = 0 exactly (u = v = s + t with st = 0).
V4  The row-sum step, exhaustive at p = 4 (exact, since |z|^4 is rational for Gaussian rationals):
    all pairs of 4-entry p-unit columns over {0, +-1, +-i, (+-1+-i)/2}. Passers of H-RF_4 on
    e1, e2, (e1 +- e2) normalised: all have disjoint supports; every disjoint pair passes;
    overlapping unit pairs exist (non-vacuity). Countercontrol: the same at p = 2 over
    {0, +-1, +-i, (+-1+-i)/2} has overlapping passers.
V5  Polarization needs complex probes: v1 = (1,0,0,0), v2 = (i,0,0,0) passes H-RF_2 on the four
    real probes, overlaps, and has V^dag V != 1; it fails on e1 + i e2. (ASSESS's "on every
    amplitude vector" includes complex vectors, which is what the V^dag V = 1 step uses.)
V6  The overlapping instance: {cH, cH} complete iff c = 1/2, i.e. {H/2, H/2}; {H/sqrt2, H/sqrt2}
    gives sum K^dag K = 2.
V7  Square maps: every 0/1 support pattern on n x n (n = 2, 3) with nonzero, pairwise disjoint
    columns is a permutation pattern.

Mutants: m1 expects D_{3/2} >= 0 (V3); m2 drops the probe e1 - e2 (V4); m3 sets c = 1/sqrt2 as
the complete scale (V6); m4 breaks the parallelogram (a + 2b) (V1); m5 drops the w^2 term
check (V2 accepts a monomial without st or w^2: injects s^2); m6 lets one column be zero (V7).
"""
import itertools
import sys
from fractions import Fraction as Fr
from math import isqrt

import sympy as sp

MUT = sys.argv[1] if len(sys.argv) > 1 else ''
res = {}

# ---------------------------------------------------------------- V1
x1, y1, x2, y2 = sp.symbols('x1 y1 x2 y2', real=True)
a = x1 + sp.I * y1
b = x2 + sp.I * y2
bb = 2 * b if MUT == 'm4' else b
m2 = lambda z: sp.expand(z * sp.conjugate(z))
s_, t_ = m2(a), m2(b)
u_, v_ = m2(a + bb), m2(a - bb)
w_ = sp.expand(sp.re(sp.expand(a * sp.conjugate(b))))
im_ = sp.expand(sp.im(sp.expand(a * sp.conjugate(b))))
v1 = sp.expand(u_ + v_ - 2 * (s_ + t_)) == 0
v1 &= sp.expand(u_ - v_ - 4 * w_) == 0
v1 &= sp.expand(s_ * t_ - w_ ** 2 - im_ ** 2) == 0
res['V1'] = v1

# ---------------------------------------------------------------- V2
s, t, w = sp.symbols('s t w', nonnegative=True)
v2 = True
for p in (2, 4, 6, 8):
    h = p // 2
    D = sp.expand((s + t + 2 * w) ** h + (s + t - 2 * w) ** h - 2 * (s ** h + t ** h))
    if MUT == 'm5' and p == 6:
        D = D + s ** 3
    if p == 2:
        v2 &= D == 0
        continue
    poly = sp.Poly(D, s, t, w)
    for mon, coef in poly.terms():
        es, et, ew = mon
        v2 &= coef > 0 and ew % 2 == 0 and ((es >= 1 and et >= 1) or ew >= 2)
res['V2'] = v2


# ---------------------------------------------------------------- V3 (rigorous enclosures)
def kroot_bounds(x, k, digits=40):
    """Rational lo <= x^(1/k) <= hi for rational x >= 0."""
    if x == 0:
        return Fr(0), Fr(0)
    scale = 10 ** digits
    n = x.numerator * scale ** k
    d = x.denominator
    q = n // d
    # integer k-th root by Newton/bisection
    lo, hi = 0, 1
    while hi ** k <= q:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** k <= q:
            lo = mid
        else:
            hi = mid
    # lo^k <= floor(n/d) <= n/d, (lo+1)^k > floor(n/d) => (lo+1)^k >= floor(n/d)+1 > n/d
    return Fr(lo, scale), Fr(lo + 1, scale)


def pow_bounds(r2, p):
    """Enclose (r2)^(p/2), r2 = |z|^2 rational, p = m/n rational."""
    e = Fr(p) / 2
    m, n = e.numerator, e.denominator
    return kroot_bounds(r2 ** m, n)


def mod2(z):
    return z[0] * z[0] + z[1] * z[1]


GA = [(Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(-1, 2), Fr(1, 3)), (Fr(3, 5), Fr(-4, 5)),
      (Fr(2), Fr(1)), (Fr(1, 7), Fr(0)), (Fr(-3, 2), Fr(-5, 4)), (Fr(1, 2), Fr(1, 2)), (Fr(0), Fr(-2, 3))]
v3 = True
for p in (Fr(1, 2), Fr(1), Fr(3, 2), Fr(5, 2), Fr(3), Fr(7, 2)):
    sign = -1 if p < 2 else 1
    if MUT == 'm1' and p == Fr(3, 2):
        sign = 1
    for za, zb in itertools.product(GA, repeat=2):
        sa, sb = mod2(za), mod2(zb)
        su = mod2((za[0] + zb[0], za[1] + zb[1]))
        sv = mod2((za[0] - zb[0], za[1] - zb[1]))
        if sa * sb == 0:
            v3 &= su == sv == sa + sb            # D_p = 0 exactly
            continue
        bu, bv, ba, bb_ = (pow_bounds(x, p) for x in (su, sv, sa, sb))
        lo = bu[0] + bv[0] - 2 * (ba[1] + bb_[1])
        hi = bu[1] + bv[1] - 2 * (ba[0] + bb_[0])
        v3 &= (hi < 0) if sign < 0 else (lo > 0)
res['V3'] = v3

# ---------------------------------------------------------------- V4
ALPH = [(Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(-1), Fr(0)), (Fr(0), Fr(1)), (Fr(0), Fr(-1))] + \
       [(Fr(e1, 2), Fr(e2, 2)) for e1 in (1, -1) for e2 in (1, -1)]


def cadd(z1, z2, sg):
    return (z1[0] + sg * z2[0], z1[1] + sg * z2[1])


def psum(col, p):
    return sum(mod2(z) ** (p // 2) for z in col)


def supp(col):
    return frozenset(i for i, z in enumerate(col) if z != (0, 0))


def run_v4(p, signs):
    units = [c for c in itertools.product(ALPH, repeat=4) if psum(c, p) == 1]
    passers = overl = disj_fail = overl_pairs = 0
    for c0, c1 in itertools.product(units, repeat=2):
        dj = not (supp(c0) & supp(c1))
        if not dj:
            overl_pairs += 1
        ok = all(psum([cadd(x, y, sg) for x, y in zip(c0, c1)], p) == 2 for sg in signs)
        if ok:
            passers += 1
            overl += (not dj)
        elif dj:
            disj_fail += 1
    return len(units), passers, overl, disj_fail, overl_pairs


signs4 = (1,) if MUT == 'm2' else (1, -1)
c4 = run_v4(4, signs4)
c2 = run_v4(2, (1, -1))
res['V4'] = c4[1] > 0 and c4[2] == 0 and c4[3] == 0 and c4[4] > 0 and c2[2] > 0

# ---------------------------------------------------------------- V5
col1 = [(Fr(1), Fr(0))] + [(Fr(0), Fr(0))] * 3
col2 = [(Fr(0), Fr(1))] + [(Fr(0), Fr(0))] * 3
v5 = psum(col1, 2) == 1 and psum(col2, 2) == 1
v5 &= all(psum([cadd(x, y, sg) for x, y in zip(col1, col2)], 2) == 2 for sg in (1, -1))
v5 &= bool(supp(col1) & supp(col2))
ip = (col1[0][0] * col2[0][0] + col1[0][1] * col2[0][1], col1[0][0] * col2[0][1] - col1[0][1] * col2[0][0])
v5 &= ip != (0, 0)                                           # v1^dag v2 = i
icol2 = [(-z[1], z[0]) for z in col2]                        # i * v2
v5 &= psum([cadd(x, y, 1) for x, y in zip(col1, icol2)], 2) != 2
res['V5'] = v5

# ---------------------------------------------------------------- V6
H = sp.Matrix([[1, 1], [1, -1]])
good = sp.Rational(1, 2) if MUT != 'm3' else 1 / sp.sqrt(2)
tot = lambda c: sp.simplify(2 * (c * H).H * (c * H))
v6 = tot(good) == sp.eye(2) and tot(1 / sp.sqrt(2)) == 2 * sp.eye(2)
cc = sp.symbols('c', positive=True)
v6 &= sp.solve(sp.Eq(tot(cc)[0, 0], 1), cc) == [sp.Rational(1, 2)]
res['V6'] = v6

# ---------------------------------------------------------------- V7
v7 = True
for n in (2, 3):
    for bits in itertools.product((0, 1), repeat=n * n):
        cols = [[bits[i * n + j] for i in range(n)] for j in range(n)]
        nonzero = all(any(c) for c in cols) if MUT != 'm6' else True
        disj = all(not any(x and y for x, y in zip(cols[i], cols[j]))
                   for i, j in itertools.combinations(range(n), 2))
        if nonzero and disj:
            v7 &= all(sum(c) == 1 for c in cols) and sorted(c.index(1) for c in cols) == list(range(n))
res['V7'] = v7

for k, v in res.items():
    print(k, 'PASS' if v else 'FAIL')
print('V4 p=4 (units, passers, overlapping passers, failing disjoint pairs, overlapping unit pairs):', c4)
print('V4 p=2 countercontrol (same tuple):', c2)
print('ALL PASS' if all(res.values()) else 'SOME FAIL')
raise SystemExit(0 if all(res.values()) else 1)
