#!/usr/bin/env python3
"""Thread D exploration e1 [E] -- a lead only, nothing here is certified.

Sanity checks of the hand derivation for node D1.1 before the certified script is written:
  (a) the four-parameter family G(s1, s2, t1, t2) built from the corner structure (controlled-(id, N) on the control
      diagonal, coherence map e1(x)Y -> e1(x)s1 S Y + e2(x)t2 T Y, e2(x)Y -> e1(x)t1 T Y + e2(x)s2 S Y) equals cnot at
      (1, 1, -1, 1);
  (b) frame, relC (and relT) for symbolic parameters;
  (c) the pairing formula F = 2 p_u p_x <b,Y> + 2 q_u q_x <b,NY> + u'^T Lam x' against direct computation;
  (d) the inverse is the family member (1/s1, 1/s2, -1/t2, -1/t1).
Exact sympy arithmetic. No decision rule: exploration output is read by hand.
"""
import sympy as sp
from itertools import product

R4 = range(4)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in NEG else 1) * w[PC[m][n], PT[m][n]])


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = sp.Matrix(R)
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def hom(x):
    return sp.Matrix([1] + list(x))


def prodState(x, y):
    return hom(x) * hom(y).T


NF = sp.diag(1, -1, -1)          # nflip
HN = homMap(NF)                  # diag(1, 1, -1, -1)
S = sp.zeros(4, 4); S[0, 1] = 1; S[1, 0] = 1          # swap e0 <-> e1 on HVec
T = sp.zeros(4, 4); T[2, 3] = -1; T[3, 2] = 1         # T Y = (0, 0, -Y3, Y2)


def unit(m, n):
    E = sp.zeros(4, 4)
    E[m, n] = 1
    return E


def gate_from(s1, s2, t1, t2):
    """Return the 16x16 matrix (acting on vec(w), row-major) and a function."""
    def G(w):
        out = sp.zeros(4, 4)
        hz = sp.Matrix([1, 0, 0, 1]); hmz = sp.Matrix([1, 0, 0, -1])
        # control-diagonal part: w = sum_mu e_mu (x) w[mu, :]
        for mu in R4:
            row = w[mu, :].T  # target vector for control basis e_mu
            if mu == 0:
                # e0 = (hz + hmz)/2
                out += (hz * row.T + hmz * (HN * row).T) / 2
            elif mu == 3:
                # e3 = (hz - hmz)/2
                out += (hz * row.T - hmz * (HN * row).T) / 2
            elif mu == 1:
                e1 = sp.Matrix([0, 1, 0, 0]); e2 = sp.Matrix([0, 0, 1, 0])
                out += e1 * (s1 * S * row).T + e2 * (t2 * T * row).T
            elif mu == 2:
                e1 = sp.Matrix([0, 1, 0, 0]); e2 = sp.Matrix([0, 0, 1, 0])
                out += e1 * (t1 * T * row).T + e2 * (s2 * S * row).T
        return out
    return G


Wsym = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'w{m}{n}', real=True))
s1, s2, t1, t2 = sp.symbols('s1 s2 t1 t2', nonzero=True)
G = gate_from(s1, s2, t1, t2)
Gc = gate_from(1, 1, -1, 1)
print('(a) G(1,1,-1,1) == cnot on a symbolic table:', sp.simplify(Gc(Wsym) - cnot(Wsym)) == sp.zeros(4, 4))

z3 = [0, 0, 1]
corner = {0: z3, 1: [0, 0, -1]}
ok_frame = all(sp.simplify(G(prodState(corner[a], corner[b])) - prodState(corner[a], corner[(a + b) % 2])) == sp.zeros(4, 4)
               for a in (0, 1) for b in (0, 1))
print('(b) frame (symbolic s,t):', ok_frame)
relC = sp.simplify(actC(NF, G(actC(NF, Wsym))) - actT(NF, G(Wsym)))
print('(b) relC (symbolic s,t):', relC == sp.zeros(4, 4))
relT = sp.simplify(actT(NF, G(actT(NF, Wsym))) - G(Wsym))
print('(b) relT (symbolic s,t):', relT == sp.zeros(4, 4))

# (c) pairing formula
u = sp.symbols('u0:3', real=True); x = sp.symbols('x0:3', real=True)
b = sp.symbols('b0:4', real=True); y = sp.symbols('y0:3', real=True)
Y = hom(y)
bv = sp.Matrix(b)
lhs = (hom(u).T * G(prodState(x, y)) * bv)[0, 0]
pu = (1 + u[2]) / 2; qu = (1 - u[2]) / 2; px = (1 + x[2]) / 2; qx = (1 - x[2]) / 2
sig = (bv.T * S * Y)[0, 0]; tau = (bv.T * T * Y)[0, 0]
Lam = sp.Matrix([[s1 * sig, t1 * tau], [t2 * tau, s2 * sig]])
up = sp.Matrix([u[0], u[1]]); xp = sp.Matrix([x[0], x[1]])
rhs = 2 * pu * px * (bv.T * Y)[0, 0] + 2 * qu * qx * (bv.T * HN * Y)[0, 0] + (up.T * Lam * xp)[0, 0]
print('(c) F formula (pairVal(hom u, b, G prodState x y) = diag + coherence):', sp.expand(lhs - rhs) == 0)

# (d) inverse
Ginv = gate_from(1 / s1, 1 / s2, -1 / t2, -1 / t1)
print('(d) G^-1 = G(1/s1, 1/s2, -1/t2, -1/t1):', sp.simplify(Ginv(G(Wsym)) - Wsym) == sp.zeros(4, 4),
      sp.simplify(G(Ginv(Wsym)) - Wsym) == sp.zeros(4, 4))
