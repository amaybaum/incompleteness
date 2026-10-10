#!/usr/bin/env python3
"""Thread D exploration e2 [E] -- a lead only, nothing here is certified.

Zero-set lemma exploration. For M1 = homMap(R1) with R1 orthogonal and R1 z3 = -z3, find the space of 4x4 matrices A
whose bilinear form b^T A Y vanishes on
  Z1 = {((1, n), (1, -n)) : |n| = 1}           (<b, Y> = 0)
  Z2 = {((1, n), (1, -R1^T n)) : |n| = 1}      (<b, M1 Y> = 0).
Criterion used: f(n) = f0 + f1(n) + f2(n) (degrees 0, 1, 2 in n) vanishes on the unit sphere iff f1 == 0 and
f2(n) + f0 |n|^2 == 0 as polynomials (odd/even split, then homogenization of the even part).
Cases: R1 = nflip (proper), R1 = diag(1, 1, -1), R1 = diag(R_psi, -1) for a rational rotation, R1 = -I.
"""
import sympy as sp

n = sp.symbols('n1:4', real=True)
Asym = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'a{i}{j}', real=True))
avars = list(Asym)


def conds_on_sphere(f):
    f = sp.expand(f)
    P = sp.Poly(f, *n)
    f0 = sum((c for (mon, c) in zip(P.monoms(), P.coeffs()) if sum(mon) == 0), sp.Integer(0))
    f1 = sum((c * sp.prod([n[i] ** mon[i] for i in range(3)]) for (mon, c) in zip(P.monoms(), P.coeffs()) if sum(mon) == 1), sp.Integer(0))
    f2 = sum((c * sp.prod([n[i] ** mon[i] for i in range(3)]) for (mon, c) in zip(P.monoms(), P.coeffs()) if sum(mon) == 2), sp.Integer(0))
    assert sp.expand(f0 + f1 + f2 - f) == 0
    eqs = []
    for g in (f1, sp.expand(f2 + f0 * (n[0] ** 2 + n[1] ** 2 + n[2] ** 2))):
        if g != 0:
            eqs += sp.Poly(g, *n).coeffs()
    return eqs


def solve_space(R1):
    R1 = sp.Matrix(R1)
    b = sp.Matrix([1] + list(n))
    Y1 = sp.Matrix([1] + [-v for v in n])
    m2 = -(R1.T * sp.Matrix(n))
    Y2 = sp.Matrix([1] + list(m2))
    eqs = conds_on_sphere((b.T * Asym * Y1)[0, 0]) + conds_on_sphere((b.T * Asym * Y2)[0, 0])
    Msys = sp.Matrix([[sp.diff(e, v) for v in avars] for e in eqs])
    ns = Msys.nullspace()
    return [sp.Matrix(4, 4, list(v)) for v in ns]


cases = {
    'nflip (proper)': sp.diag(1, -1, -1),
    'diag(1,1,-1) (improper)': sp.diag(1, 1, -1),
    'diag(R(3/5,4/5), -1) (improper)': sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5), 0], [sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, -1]]),
    '-I (improper)': -sp.eye(3),
    'rotation pi about (3/5,4/5,0) (proper)': None,
}
w = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5), 0])
cases['rotation pi about (3/5,4/5,0) (proper)'] = 2 * w * w.T - sp.eye(3)
for name, R1 in cases.items():
    assert sp.simplify(R1.T * R1 - sp.eye(3)) == sp.zeros(3, 3)
    assert R1 * sp.Matrix([0, 0, 1]) == sp.Matrix([0, 0, -1])
    sp_ = solve_space(R1)
    print(f'{name}: det R1 = {R1.det()}, dim of form space = {len(sp_)}')
    for B in sp_:
        print('   ', list(B))
    col0 = all(B[i, 0] == 0 for B in sp_ for i in range(4))
    col3 = all(B[i, 3] == 0 for B in sp_ for i in range(4))
    print(f'    every form kills Y0: {col0}; every form kills Y3: {col3}')
