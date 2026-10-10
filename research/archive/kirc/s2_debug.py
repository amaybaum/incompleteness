import itertools, sympy as sp, random
random.seed(3)
def rand_sphere(dim):
    tt = [random.randint(-6, 6) for _ in range(dim - 1)]
    s2 = sum(x * x for x in tt)
    return [sp.Rational(2 * x, s2 + 1) for x in tt] + [sp.Rational(s2 - 1, s2 + 1)]
for d, p in [(4, 0), (4, 2), (5, 2), (5, 1)]:
    n = d + 1; Tn = d - 1; q = Tn - p
    Nd = [1] + [1] * p + [-1] * q + [-1]
    ph = sp.symbols('f0:%d' % (n * n)); Phi = sp.Matrix(n, n, ph)
    for K in (12 + 4 * d, 60):
        rows = []
        pts = [rand_sphere(d) for _ in range(K)]
        for tp in pts:
            t = sp.Matrix([1] + tp); w = Phi * t
            g0 = sp.Matrix([1] + [-x for x in tp]); g1 = sp.Matrix([1] + [-Nd[i + 1] * tp[i] for i in range(d)])
            rows += [(g0.T * w)[0], (g1.T * w)[0]]
        A = sp.Matrix([[sp.diff(r_, v) for v in ph] for r_ in rows])
        print(d, p, 'K=%d random pts: nullity %d' % (K, n * n - A.rank()), flush=True)
