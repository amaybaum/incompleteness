#!/usr/bin/env python3
"""EXPLORATION [E/F] (not certified): look for a direct famI/famII violation for uniform
K_E = dualW(SEP + cnot SEP). Exact rationals for the values; the candidate lists are ad hoc.

famI for uniform K:  for X, Y in K and E, F in K*:  ipW(E, X F Y^T) >= 0.
K_E* = cl(K_gen) = K_gen = cone(products u cnot products), so E, F range over generators.
Membership X in K_E is tested here only against a finite sample of generators (a lead, not proof).
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


phiW = sp.diag(1, 1, -1, 1)
E00 = sp.zeros(4, 4)
E00[0, 0] = 1
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
Tpsi = actT(RH, phiW)
Fw = E00 / 2 - Tpsi / 4
pts = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1],
       [Q(3, 5), Q(4, 5), 0], [Q(3, 5), 0, Q(4, 5)], [0, Q(3, 5), Q(4, 5)], [Q(-3, 5), Q(4, 5), 0],
       [Q(2, 3), Q(2, 3), Q(1, 3)], [Q(-2, 3), Q(2, 3), Q(1, 3)], [Q(2, 3), Q(-2, 3), Q(1, 3)],
       [Q(2, 3), Q(2, 3), Q(-1, 3)], [Q(-2, 3), Q(-2, 3), Q(1, 3)]]
gens = []
for x in pts:
    for y in pts:
        gens.append(prodState(x, y))
        gens.append(cnot(prodState(x, y)))


def in_KE_sample(X):
    return min(ipW(X, g) for g in gens) >= 0


R0 = sp.Matrix([[Q(3, 5), Q(-4, 5), 0], [Q(4, 5), Q(3, 5), 0], [0, 0, 1]])
R1 = sp.Matrix([[1, 0, 0], [0, Q(3, 5), Q(-4, 5)], [0, Q(4, 5), Q(3, 5)]])
cands = {'Fw': Fw, 'cnotFw': cnot(Fw), 'phiW': phiW, 'E00': E00,
         'TfullFw': sp.diag(1, 1, -1, 1) * Fw * sp.diag(1, 1, -1, 1)}
for nm in list(cands):
    for rn, R in (('R0', R0), ('R1', R1)):
        for side, act in (('C', actC), ('T', actT)):
            cands[f'{side}{rn}({nm})'] = act(R, cands[nm])
Xs = {k: v for k, v in cands.items() if in_KE_sample(v)}
print('candidates in K_E (sample test):', sorted(Xs))
best = None
gsmall = gens[::3]
for (nx, X), (ny, Y) in product(Xs.items(), repeat=2):
    for F in gsmall:
        M = X * F * Y.T
        v = min(ipW(E, M) for E in gsmall)
        if best is None or v < best[0]:
            best = (v, nx, ny)
print('min famI value found:', best)
