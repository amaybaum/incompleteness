"""Preflight: sizes of the identification spaces, before any classification (design evidence only)."""
from math import factorial
from fractions import Fraction
def set_classes(n, m, k):
    """Set-level identifications of an n-set with Fin m x Fin k, up to S_m x S_k (and the swap when m == k)."""
    assert m * k == n
    g = factorial(m) * factorial(k) * (2 if m == k else 1)
    assert factorial(n) % g == 0
    return factorial(n) // g
def gl(n, q):
    r = 1
    for i in range(n):
        r *= q**n - q**i
    return r
def lin_decomps(n, q):
    """Unordered sets of n independent functionals on F_q^n, each up to a nonzero scalar."""
    num, den = gl(n, q), (q - 1)**n * factorial(n)
    assert num % den == 0
    return num // den
CAP_EXH, CAP_SAMPLE = 50_000, 2_000
rows = [
    ('leg T', 'CCT4 / CT4 x CT4', 'V=4 as 2x2, A=4 as 2x2', set_classes(4, 2, 2) * set_classes(4, 2, 2)),
    ('leg T', 'CCC', 'V=4 as 2x2, A=4 as 2x2', set_classes(4, 2, 2) * set_classes(4, 2, 2)),
    ('leg T', 'CENT (countercontrol)', 'V=4 as 2x2, A=1', set_classes(4, 2, 2)),
    ('leg T', 'C21', 'V=16 as 4x4, A=1', set_classes(16, 4, 4)),
    ('leg T', 'K-search engine control', 'Fin 8 as 2x4', set_classes(8, 2, 4)),
    ('leg S', 'one coupled edge / U-free(3)', 'F_3^4, linear', lin_decomps(4, 3)),
    ('leg S', 'four-site ring, q=3 (counterexample)', 'F_3^8, linear', lin_decomps(8, 3)),
    ('leg S', 'four-site ring, q=5', 'F_5^8, linear', lin_decomps(8, 5)),
    ('leg S', 'two coupled edges U-edge(3)', 'F_3^8, linear', lin_decomps(8, 3)),
]
print('%-6s %-38s %-26s %28s  %s' % ('leg', 'case', 'space', 'classes (I0)', 'budget'))
for leg, case, space, n in rows:
    mode = 'exhaustive' if n <= CAP_EXH else 'over cap: sample %d or complete pruned search' % CAP_SAMPLE
    print('%-6s %-38s %-26s %28d  %s' % (leg, case, space, n, mode))
# controls on the formulas
assert set_classes(4, 2, 2) == 3 and set_classes(4, 4, 1) == 1 and set_classes(8, 2, 4) == 840
assert lin_decomps(2, 2) == 3   # F_2^2: 3 projective points, 3 unordered pairs
assert lin_decomps(4, 3) == 63180
print('formula controls: OK')
