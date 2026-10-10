"""A33 research: exact points of the nine circles at roots of unity, and exact metric data.
A point is its feature vector: a tuple over IDX of Gaussian rationals (re, im) scaled by 64."""
from fractions import Fraction
from circles import C, N

def ipow(k):          # i^k as (re, im)
    return [(1, 0), (0, 1), (-1, 0), (0, -1)][k % 4]

def point(r, k, n=4):
    """f_r(w) at w = exp(2 pi i k/n), n = 4 only (Gaussian integers), times 64."""
    assert n == 4
    out = []
    for s, e in C[r]:
        re, im = ipow(k * e)
        out.append((s * re, s * im))
    return tuple(out)

def reip(x, y):
    """Re <x, y> for vectors scaled by 64: returns the exact rational Re <x, y>."""
    t = 0
    for (a, b), (c, d) in zip(x, y):
        t += a * c + b * d       # Re(conj(a+ib)(c+id))
    return Fraction(t, 4096)

def d2(x, y):
    return reip(x, x) + reip(y, y) - 2 * reip(x, y)

def on_circle(x, s):
    """the unit parameters w with f_s(w) = x (x scaled by 64), exactly: returns a set of k in Z/4 or
    'other' if x lies on circle s at a parameter outside the fourth roots (it cannot: a coordinate with
    exponent +-1 fixes w as a Gaussian unit)."""
    ks = set(range(4))
    for (sg, e), v in zip(C[s], x):
        ks = {k for k in ks if (sg * ipow(k * e)[0], sg * ipow(k * e)[1]) == v}
    return ks
