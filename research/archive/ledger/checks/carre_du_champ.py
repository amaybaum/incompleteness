"""Exact check: for the normalized nearest-neighbour Markov kernel T = A/(2d) on Z^3, the carre du champ
Gamma(f,f)(x) = 1/2 [T(f^2) - 2 f T f](x) on linear functions f = k.x equals |k|_2^2 / (2d): isotropic (ell_2) in k,
the same quadratic form as the propagation metric.  Contrast: the hop metric is ell_1 (T-A6-2) and the edge boundary
is int ||n||_1 dA (T-A3-2)."""
from fractions import Fraction as Fr
import itertools
d = 3
nbrs = [tuple((1 if j == i else 0) * s for j in range(d)) for i in range(d) for s in (1, -1)]
def T(f, x):
    return sum(Fr(f(tuple(a + b for a, b in zip(x, e)))) for e in nbrs) / (2 * d)
ok = True
for k in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, -1, 3), (0, 5, -2)]:
    f = lambda x, k=k: sum(a * b for a, b in zip(k, x))
    x0 = (0, 0, 0)
    gamma = (T(lambda x: f(x) ** 2, x0) - 2 * f(x0) * T(f, x0)) / 2
    pred = Fr(sum(a * a for a in k), 2 * d)
    ok &= gamma == pred
    print(k, 'Gamma =', gamma, ' |k|^2/(2d) =', pred, ' ell1^2/(2d) =', Fr(sum(map(abs, k)) ** 2, 2 * d))
print('ISOTROPIC' if ok else 'FAIL')
