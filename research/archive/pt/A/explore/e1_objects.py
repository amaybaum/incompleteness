#!/usr/bin/env python3
"""EXPLORATION [E] (not certified): compute the objects thread A will certify later.

Leads only. Nothing printed here is evidence; the certified scripts re-derive every value under
decision rules stated before their first run.
"""
from itertools import product

import sympy as sp

Q = sp.Rational
R4 = range(4)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def sgn(m, n):
    return -1 if (m, n) in NEG else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = R
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def prodState(x, y):
    return hom(x) * hom(y).T


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in R4 for n in R4)


def fourVal(X, Y, E, F):
    return sum(X[a, b] * Y[c, d] * E[a, c] * F[b, d] for a, b, c, d in product(R4, repeat=4))


phiW = sp.diag(1, 1, -1, 1)
E00 = sp.zeros(4, 4)
E00[0, 0] = 1
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
Tpsi = actT(RH, phiW)
print('Tpsi', Tpsi.tolist())
print('cnot Tpsi', cnot(Tpsi).tolist())
F = E00 / 2 - Tpsi / 4
E = Tpsi / 4
print('fourVal(phiW, phiW, E, F) =', fourVal(phiW, phiW, E, F))
print('ipW(F, Tpsi) =', ipW(F, Tpsi))
xs = sp.symbols('x1 x2 x3', real=True)
ys = sp.symbols('y1 y2 y3', real=True)
print('ipW(Tpsi, x(x)y) =', sp.expand(ipW(Tpsi, prodState(xs, ys))))
print('ipW(Tpsi, cnot x(x)y) =', sp.expand(ipW(Tpsi, cnot(prodState(xs, ys)))))
print('ipW(cnot Tpsi, x(x)y) =', sp.expand(ipW(cnot(Tpsi), prodState(xs, ys))))
Wsym = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'w{i}{j}', real=True))
Asym = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'a{i}{j}', real=True))
print('cnot self-adjoint for ipW:', sp.expand(ipW(Asym, cnot(Wsym)) - ipW(cnot(Asym), Wsym)) == 0)
Dm = sp.diag(1, 1, -1, 1)
print('phiW F phiW^T == Tfull F:', phiW * F * phiW.T == Dm * F * Dm)
print('Tfull Tpsi == Tpsi:', Dm * Tpsi * Dm == Tpsi)
# rotations to probe IE1 of K_E = dual(K_gen): F_rot = actT R F, look for a cnot-product with negative pairing
R0 = sp.Matrix([[Q(3, 5), Q(-4, 5), 0], [Q(4, 5), Q(3, 5), 0], [0, 0, 1]])
R1 = sp.Matrix([[1, 0, 0], [0, Q(3, 5), Q(-4, 5)], [0, Q(4, 5), Q(3, 5)]])
R2 = sp.Matrix([[Q(3, 5), 0, Q(-4, 5)], [0, 1, 0], [Q(4, 5), 0, Q(3, 5)]])
pts = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1],
       [Q(3, 5), Q(4, 5), 0], [Q(3, 5), 0, Q(4, 5)], [0, Q(3, 5), Q(4, 5)], [Q(2, 3), Q(2, 3), Q(1, 3)],
       [Q(-2, 3), Q(2, 3), Q(1, 3)], [Q(2, 3), Q(-2, 3), Q(1, 3)], [Q(2, 3), Q(2, 3), Q(-1, 3)]]
best = None
for name, R in (('R0', R0), ('R1', R1), ('R2', R2), ('R1R2', R1 * R2), ('R0R1', R0 * R1)):
    G = actT(R, F)
    for x in pts:
        for y in pts:
            v = ipW(G, cnot(prodState(x, y)))
            if best is None or v < best[0]:
                best = (v, name, x, y)
print('min ipW(actT R F, cnot(x(x)y)) over samples:', best)
