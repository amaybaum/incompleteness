#!/usr/bin/env python3
"""EXPLORATION [E] (not certified): extract an explicit famI violation for uniform
K_E = dualW(SEP + cnot SEP), with X = Fw, Y = actC R1 phiW (lead from e2). Fractions only."""
from fractions import Fraction as Fr
from itertools import product

R4 = range(4)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def mat(rows):
    return [[Fr(v) for v in r] for r in rows]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in R4) for j in R4] for i in R4]


def T(A):
    return [[A[j][i] for j in R4] for i in R4]


def cnot(w):
    return [[(-1 if (m, n) in NEG else 1) * w[PC[m][n]][PT[m][n]] for n in R4] for m in R4]


def hom(x):
    return [Fr(1)] + [Fr(v) for v in x]


def homMap(R):
    M = [[Fr(0)] * 4 for _ in R4]
    M[0][0] = Fr(1)
    for i in range(3):
        for j in range(3):
            M[i + 1][j + 1] = Fr(R[i][j])
    return M


def actC(R, w):
    return mul(homMap(R), w)


def actT(R, w):
    return mul(w, T(homMap(R)))


def prodState(x, y):
    a, b = hom(x), hom(y)
    return [[a[i] * b[j] for j in R4] for i in R4]


def ipW(E, X):
    return sum(E[m][n] * X[m][n] for m in R4 for n in R4)


def lin(c1, A, c2, B):
    return [[c1 * A[i][j] + c2 * B[i][j] for j in R4] for i in R4]


phiW = mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
E00 = mat([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
RH = [[0, 0, 1], [0, -1, 0], [1, 0, 0]]
Tpsi = actT(RH, phiW)
Fw = lin(Fr(1, 2), E00, Fr(-1, 4), Tpsi)
R1 = [[1, 0, 0], [0, Fr(3, 5), Fr(-4, 5)], [0, Fr(4, 5), Fr(3, 5)]]
Y = actC(R1, phiW)
Q = Fr
pts = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1],
       [Q(3, 5), Q(4, 5), 0], [Q(3, 5), 0, Q(4, 5)], [0, Q(3, 5), Q(4, 5)], [Q(-3, 5), Q(4, 5), 0],
       [Q(2, 3), Q(2, 3), Q(1, 3)], [Q(-2, 3), Q(2, 3), Q(1, 3)], [Q(2, 3), Q(-2, 3), Q(1, 3)],
       [Q(2, 3), Q(2, 3), Q(-1, 3)], [Q(-2, 3), Q(-2, 3), Q(1, 3)]]
gens = []
for x in pts:
    for y in pts:
        gens.append(('P', x, y, prodState(x, y)))
        gens.append(('C', x, y, cnot(prodState(x, y))))
best = None
for gF in gens:
    M = mul(mul(Fw, gF[3]), T(Y))
    for gE in gens:
        v = ipW(gE[3], M)
        if best is None or v < best[0]:
            best = (v, gE[:3], gF[:3])
print('best famI value', best[0])
print('E generator', best[1])
print('F generator', best[2])
# simpler: Y = phiW and the same search
best2 = None
for gF in gens:
    M = mul(mul(Fw, gF[3]), T(phiW))
    for gE in gens:
        v = ipW(gE[3], M)
        if best2 is None or v < best2[0]:
            best2 = (v, gE[:3], gF[:3])
print('with Y = phiW:', best2)
