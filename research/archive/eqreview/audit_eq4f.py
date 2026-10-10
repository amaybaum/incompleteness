"""Independent exact audit of EQ4-F's formalization package (coordinator; research only, base bcbc516f).

Imports nothing from scratchpad/eq4/F.  Kernel cnot typed in by hand (as audit_eq3_n1.py); operator dictionary mine.
Usage: python3 -I -B audit_eq4f.py

DECISION RULES (fixed before the first run):
  S  cnot' = actT reflY . cnot . actT reflY is an involution and Euclidean-symmetric (so its dual action on effect tables
     is itself), as the aligned form (Theorem B) and Lemma P require.
  P  Lemma P witnesses, family (i): X = g01(prodState xplus z3), Y = g23(prodState xplus z3),
     E = g02(tens(sharpVec xplus, sharpVec z3)), F = g13(tens(sharpVec(-xplus), sharpVec(-z3))), with g_p = cnot or
     cnot' by the twist bit; the value <X, E.Y.F^T> is negative at every odd pattern and nonnegative at every even one
     (16 patterns).  Membership control: X, Y are tables of states of the corresponding cones (pure states of Q3 or Tw
     per twist bit, by my dictionary: projector test or PT-projector test).
  O  orientation rule (Theorem C2): for exact rational O(3) post-locals (A, B), the Bell table H_R, R = A reflY B^T, is a
     pure state of Q3 (projector) iff det A det B = 1, and a pure state of Tw (PT_2 projector) iff det A det B = -1;
     8 random exact (A, B) covering all four determinant-sign classes.
VERDICT `AUDIT-EQ4F-EXACT` iff every check passes.
"""
import itertools
import random
import sys
from functools import reduce

import sympy as sp
from sympy import I, Matrix, Rational as R, eye, zeros

checks = []


def check(name, cond):
    checks.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


def kron(*Ms):
    return reduce(sp.kronecker_product, Ms)


def sgn(m, n):
    return -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnot(T):
    return Matrix(4, 4, lambda m, n: sgn(m, n) * T[PC[m][n], PT[m][n]])


def H(A):
    M = eye(4)
    M[1:, 1:] = A
    return M


REFLY = sp.diag(1, -1, 1)


def actT(A, T):
    return T * H(A).T


def actC(A, T):
    return H(A) * T


def cnot_tw(T):
    return actT(REFLY, cnot(actT(REFLY, T)))


def tab_matrix(f):
    M = zeros(16, 16)
    for k in range(16):
        E = zeros(4, 4)
        E[k // 4, k % 4] = 1
        img = f(E)
        for j in range(16):
            M[j, k] = img[j // 4, j % 4]
    return M


CT = tab_matrix(cnot_tw)
check("S cnot' is an involution and symmetric as a 16 x 16 table map", CT * CT == eye(16) and CT.T == CT)


def hom(x):
    return Matrix([1] + list(x))


def sharp(x):
    return Matrix([R(1, 2)] + [sp.S(c) / 2 for c in x])


XP, Z3 = [1, 0, 0], [0, 0, 1]
MXP, MZ3 = [-1, 0, 0], [0, 0, -1]
s0, sx = eye(2), Matrix([[0, 1], [1, 0]])
sy, sz = Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])
SIG = [s0, sx, sy, sz]


def pauli(T):
    out = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            out += T[m, n] * kron(SIG[m], SIG[n])
    return out / 4


def PT2(M):
    out = zeros(4, 4)
    for i0, i1, j0, j1 in itertools.product(range(2), repeat=4):
        out[2 * i0 + i1, 2 * j0 + j1] = M[2 * i0 + j1, 2 * j0 + i1]
    return out


def is_proj(P):
    return (P * P - P).applyfunc(sp.expand).is_zero_matrix and sp.expand(P.trace()) == 1


ok_p, rows, ok_mem = True, [], True
for tau in itertools.product(range(2), repeat=4):          # order (01, 23, 02, 13)
    g = {p: (cnot_tw if t else cnot) for p, t in zip(["01", "23", "02", "13"], tau)}
    X = g["01"](hom(XP) * hom(Z3).T)
    Y = g["23"](hom(XP) * hom(Z3).T)
    E = g["02"](sharp(XP) * sharp(Z3).T)
    F = g["13"](sharp(MXP) * sharp(MZ3).T)
    val = sp.expand(sum((X[m, n] * (E * Y * F.T)[m, n]) for m in range(4) for n in range(4)))
    odd = (tau[0] + tau[3] + tau[1] + tau[2]) % 2 == 1
    rows.append("%s:%s" % ("".join(map(str, tau)), val))
    ok_p &= (val < 0) if odd else (val >= 0)
    for T, t in ((X, tau[0]), (Y, tau[1])):
        P = pauli(T)
        ok_mem &= is_proj(PT2(P)) if t else is_proj(P)
check("P Lemma P witnesses: family (i) value negative exactly at the odd patterns  [" + " ".join(rows) + "]", ok_p)
check("P membership control: X and Y are pure states of Q3 (twist 0) or of Tw (twist 1) in my dictionary", ok_mem)

rng = random.Random(4242)


def rat_rot():
    a, b, c = (R(rng.randint(-5, 5), rng.randint(1, 4)) for _ in range(3))
    S = Matrix([[0, -a, -b], [a, 0, -c], [b, c, 0]])
    return ((eye(3) - S) * (eye(3) + S).inv()).applyfunc(sp.expand)


ok_o, classes = True, set()
for k in range(8):
    A = rat_rot() * (REFLY if k % 2 else eye(3))
    B = rat_rot() * (REFLY if (k // 2) % 2 else eye(3))
    Rm = A * REFLY * B.T
    bell = actC(A, actT(B, cnot(hom(XP) * hom(Z3).T)))
    P = pauli(bell)
    dprod = A.det() * B.det()
    classes.add((A.det(), B.det()))
    q3, tw = is_proj(P), is_proj(PT2(P))
    ok_o &= (bell == H(Rm)) and ((q3 and not tw) if dprod == 1 else (tw and not q3))
check("O orientation rule: the Bell table H_R (R = A reflY B^T) is a pure state of Q3 iff det A det B = 1 and of Tw "
      "iff det A det B = -1 (8 exact random post-locals, determinant classes %s)" % sorted(classes),
      ok_o and len(classes) == 4)
print("--- audit_eq4f: %d/%d" % (sum(checks), len(checks)))
print("VERDICT AUDIT-EQ4F-EXACT" if all(checks) else "VERDICT NOT RENDERED")
