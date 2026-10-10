#!/usr/bin/env python3
"""Thread D exploration e3 [E] -- lead only. The 4x4 determinant of cnot(prodState x y) as a polynomial."""
import sympy as sp
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}
def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in NEG else 1) * w[PC[m][n], PT[m][n]])
x = sp.symbols('x0:3', real=True); y = sp.symbols('y0:3', real=True)
hx = sp.Matrix([1] + list(x)); hy = sp.Matrix([1] + list(y))
D = sp.factor(cnot(hx * hy.T).det())
print('det cnot(prodState x y) =', D)
X2 = x[0]**2 + x[1]**2 + x[2]**2; Y2 = y[0]**2 + y[1]**2 + y[2]**2
cand = -(x[0]**2 + x[1]**2)**2 * (y[1]**2 + y[2]**2)**2
print('difference to -(x0^2+x1^2)^2 (y1^2+y2^2)^2 at unit x,y (substituting x2^2, y0^2):',
      sp.factor(sp.expand(D - cand).subs({x[2]**2: 1 - x[0]**2 - x[1]**2, y[0]**2: 1 - y[1]**2 - y[2]**2})))
