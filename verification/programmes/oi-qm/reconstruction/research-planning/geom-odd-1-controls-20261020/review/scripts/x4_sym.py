"""Symmetry-ansatz check over the whole local orbit (32 sign-twist gates of x2), not just R."""
import sys, itertools, json
import numpy as np
from fractions import Fraction as Fr
from math import lcm
sys.path.insert(0, sys.argv[1]); import controls_verify as cv
body = cv.Body('eball3')
R = np.array([[int(c) for c in r] for r in body.reference], dtype=np.int64)
H = np.array([[int(c) for c in r] for r in body.H]); T = np.kron(np.eye(4, dtype=np.int64), H); C = np.kron(H, np.eye(4, dtype=np.int64))
cor = {0: [1, 0, 0, 1], 1: [1, 0, 0, -1]}
def inF(M):
    return (np.array_equal(T @ M @ T, M) and np.array_equal(C @ M @ C, T @ M)
            and all(np.array_equal(M @ np.kron(cor[a], cor[b]), np.kron(cor[a], cor[(a + b) % 2])) for a in (0, 1) for b in (0, 1)))
def scal(v):
    L = 1
    for c in v: L = lcm(L, Fr(c).denominator)
    return [int(Fr(c) * L) for c in v]
st = [s for p in 'AB' for s in body.pools[p]['states']]; ef = [e for p in 'AB' for e in body.pools[p]['effects']]
S = np.array([scal(cv.hom(x)) for x in st], dtype=np.int64); E = np.array([scal(e) for e in ef], dtype=np.int64)
def minval(M):
    W = np.einsum('mnkl,xk,yl->xymn', M.reshape(4, 4, 4, 4), S, S)
    return np.einsum('am,xymn,bn->xyab', E, W, E).min()
# the 32 gates: R o diag(s); first filter in F (cheap), then positivity
gates = []
for bits in itertools.product((1, -1), repeat=16):
    M = R @ np.diag(bits)
    if inF(M) and minval(M) >= 0 and minval(np.diag(bits) @ R) >= 0: gates.append(M)
print('gates:', len(gates))
G4 = [np.diag([1] + list(g)) for g in [(1, 1, 1), (1, -1, 1), (-1, 1, 1), (-1, -1, 1)]]
I4 = np.eye(4, dtype=np.int64)
def comm(M, X): return np.array_equal(M @ X, X @ M)
best = {}
for k, M in enumerate(gates):
    gg = sum(comm(M, np.kron(g, g)) for g in G4); g1 = sum(comm(M, np.kron(g, I4)) for g in G4); og = sum(comm(M, np.kron(I4, g)) for g in G4)
    best.setdefault((g1, og, gg), 0); best[(g1, og, gg)] += 1
print('counts of (g(x)1, 1(x)g, g(x)g commuting, out of 4 each) over the orbit:', best)
print('R itself:', sum(comm(R, np.kron(g, I4)) for g in G4), sum(comm(R, np.kron(I4, g)) for g in G4), sum(comm(R, np.kron(g, g)) for g in G4))
