#!/usr/bin/env python3
"""Coordinator's independent check of the research/origin thread's load-bearing exact claims (branch head 4cec62c9).
Own code; reads nothing.  Run: python3 -I -B indep_checkO.py
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH per line; INDEP-O-FIXED iff all CONFIRMED.
 X1 (O1-T1) for 2x2 and 3x3 unitaries U, Ad U commutes with the computational-basis dephasing D iff U is monomial;
    tested on a basis of matrices for 14 instances (identity, Paulis, S, phase diagonals, permutations with phases:
    monomial; H, sqrt X, R_y(theta), the 3x3 Fourier matrix, a 3x3 real rotation: non-monomial).
 X2 (O1-T2) qubit sandwich: with rho0 = P = |0><0|, V = tr P (Ad U^dag . Ad U rho0) - tr P (Ad U^dag . D . Ad U rho0)
    equals 2|a|^2|b|^2 for U = [[a, b], [-conj b, conj a]] (symbolic, a = cos(th) e^{i al}, b = sin(th) e^{i be});
    at the balanced angle the two probabilities are 1 and 1/2 (the owner's witness (1, 1/2)).
 X3 (O4-I1) cyc3 = R_z(pi/2) R_x(pi/2) and cyc3 R_z(t) cyc3^-1 = R_x(t), symbolically in t.
 X4 (O3-T2) the flow through the native NOT, R_x(pi t), sends the frame state e_z at t = 1/2 to a state with zero
    z-component (balanced for the frame readout), and R_x(pi) = nflip = diag(1, -1, -1).
 X5 (O3-T7) Hadamard on the states {0, 1} and Hadamard on {1, 2} (two balanced mixers on overlapping pairs of three
    states) generate an element of infinite order: for the product, an orthogonal 3x3 matrix of determinant 1,
    2 cos(theta) = trace - 1 = -3/2 is not an integer, so e^{i theta} is not a root of unity (a root of unity's
    2 cos is an algebraic integer, and a rational algebraic integer is an integer).  Control at level two: H S has
    finite order ((H S)^24 = 1).
"""
import itertools
import sympy as sp
from sympy import Matrix, I, eye, zeros, sqrt, simplify, expand, exp, cos, sin, pi, symbols, Rational as Q
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
def deph(M): return Matrix(M.rows, M.cols, lambda i, j: M[i, j] if i == j else 0)
def monomial(U): return all(sum(1 for j in range(U.cols) if simplify(U[i, j]) != 0) == 1 for i in range(U.rows)) and all(sum(1 for i in range(U.rows) if simplify(U[i, j]) != 0) == 1 for j in range(U.cols))
def commutes_with_deph(U):
    d = U.rows
    for i in range(d):
        for j in range(d):
            E = zeros(d, d); E[i, j] = 1
            if simplify(U * deph(E) * U.H - deph(U * E * U.H)) != zeros(d, d): return False
    return True
print("== X1 dephasing covariance <-> monomial")
H2 = Matrix([[1, 1], [1, -1]]) / sqrt(2); S2 = Matrix.diag(1, I); X2 = Matrix([[0, 1], [1, 0]]); Z2 = Matrix.diag(1, -1)
sqrtX = Matrix([[1 + I, 1 - I], [1 - I, 1 + I]]) / 2
th = symbols('th', real=True)
Ry = Matrix([[cos(th / 2), -sin(th / 2)], [sin(th / 2), cos(th / 2)]]).subs(th, pi / 3)
ph = Matrix.diag(exp(I * pi / 7), exp(-I * pi / 5))
w = exp(2 * pi * I / 3); F3 = Matrix(3, 3, lambda i, j: w ** (i * j)) / sqrt(3)
P3 = Matrix([[0, 0, exp(I * pi / 3)], [1, 0, 0], [0, exp(-I * pi / 9), 0]])
Rz3 = Matrix([[cos(pi / 3), -sin(pi / 3), 0], [sin(pi / 3), cos(pi / 3), 0], [0, 0, 1]])
inst = [('I2', eye(2)), ('X', X2), ('Z', Z2), ('S', S2), ('phases', ph), ('XS', X2 * S2), ('I3', eye(3)), ('P3', P3), ('cyc', Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])),
        ('H', H2), ('sqrtX', sqrtX), ('Ry', Ry), ('F3', F3), ('Rz3', Rz3)]
res1 = {nm: (monomial(U), commutes_with_deph(U)) for nm, U in inst}
unitary = all(simplify(U.H * U - eye(U.rows)) == zeros(U.rows, U.rows) for _, U in inst)
rec('X1', unitary and all(m == c for m, c in res1.values()) and sum(m for m, _ in res1.values()) == 9 and len(inst) == 14,
    'Ad U commutes with dephasing iff U is monomial, on all 14 unitary instances (9 monomial, 5 not)', str({k: v for k, v in res1.items()}))
print("== X2 qubit sandwich visibility")
al, be = symbols('al be', real=True)
a = cos(th) * exp(I * al); b = sin(th) * exp(I * be)
U = Matrix([[a, b], [-sp.conjugate(b), sp.conjugate(a)]])
rho0 = Matrix.diag(1, 0); P = rho0
rho1 = U * rho0 * U.H
p_coh = simplify((P * (U.H * rho1 * U)).trace()); p_deph = simplify((P * (U.H * deph(rho1) * U)).trace())
V = simplify(p_coh - p_deph)
rec('X2', simplify(p_coh - 1) == 0 and simplify(V - 2 * cos(th) ** 2 * sin(th) ** 2) == 0 and simplify(p_deph.subs(th, pi / 4)) == Q(1, 2),
    'V = 2|a|^2|b|^2 symbolically; at the balanced angle the probabilities are 1 (coherent) and 1/2 (dephased)', 'V = %s' % V)
print("== X3 cyc3 and the rotations")
t = symbols('t', real=True)
def Rz(u): return Matrix([[cos(u), -sin(u), 0], [sin(u), cos(u), 0], [0, 0, 1]])
def Rx(u): return Matrix([[1, 0, 0], [0, cos(u), -sin(u)], [0, sin(u), cos(u)]])
cyc3 = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
ok3 = simplify(Rz(pi / 2) * Rx(pi / 2) - cyc3) == zeros(3, 3) and simplify(cyc3 * Rz(t) * cyc3.T - Rx(t)) == zeros(3, 3) and cyc3 ** 3 == eye(3)
rec('X3', ok3, 'cyc3 = R_z(pi/2) R_x(pi/2), cyc3 R_z(t) cyc3^-1 = R_x(t), cyc3^3 = 1')
print("== X4 the NOT flow at t = 1/2")
ez = Matrix([0, 0, 1]); half = Rx(pi * Q(1, 2)) * ez
rec('X4', simplify(half[2]) == 0 and simplify(half.T * half)[0] == 1 and simplify(Rx(pi) - Matrix.diag(1, -1, -1)) == zeros(3, 3),
    'R_x(pi/2) e_z has zero z-component (balanced, pure); R_x(pi) = nflip', 'R_x(pi/2) e_z = %s' % list(half))
print("== X5 infinite order from two overlapping balanced mixers")
B1 = Matrix([[1, 1, 0], [1, -1, 0], [0, 0, sqrt(2)]]) / sqrt(2); B2 = Matrix([[sqrt(2), 0, 0], [0, 1, 1], [0, 1, -1]]) / sqrt(2)
M = simplify(B1 * B2); tr = simplify(M.trace()); det = simplify(M.det())
two_cos = simplify(tr - 1)
HS = H2 * S2; HS24 = simplify(HS ** 24)
rec('X5', simplify(M.T * M - eye(3)) == zeros(3, 3) and det == 1 and two_cos == Q(-3, 2) and not two_cos.is_integer and HS24 == eye(2),
    'B1 B2 is orthogonal with det 1 and 2 cos(theta) = -3/2 (not an integer): infinite order; control (H S)^24 = 1', 'trace %s' % tr)
print("SUMMARY %d/%d CONFIRMED" % (sum(R), len(R)))
print("INDEP-O-FIXED" if all(R) else "INDEP-O-MISMATCH")
