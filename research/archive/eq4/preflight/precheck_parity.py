"""Exact pre-check of the statements the preflight's sorry-free module proves (research only, base bcbc516f).

Kernel tables typed from CompositeDimension.lean (sgn 739, pc 742, pt 749, cnotFun 755), K2Guard.lean (reflY 46,
idW 101) and EffectSpace.lean (sharpVec 57).  Every statement below is checked symbolically (sympy), not sampled.
Usage: python3 -I -B precheck_parity.py
DECISION RULE: VERDICT `PREFLIGHT-PRECHECK-EXACT` iff every check passes.
"""
import itertools
import sys

import sympy as sp

checks = []


def check(name, cond):
    checks.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


R4 = range(4)
# kernel tables, verbatim from CompositeDimension.lean
PC = {(0, 0): 0, (0, 1): 0, (0, 2): 3, (0, 3): 3, (1, 0): 1, (1, 1): 1, (1, 2): 2, (1, 3): 2,
      (2, 0): 2, (2, 1): 2, (2, 2): 1, (2, 3): 1, (3, 0): 3, (3, 1): 3, (3, 2): 0, (3, 3): 0}
PT = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (1, 0): 1, (1, 1): 0, (1, 2): 3, (1, 3): 2,
      (2, 0): 1, (2, 1): 0, (2, 2): 3, (2, 3): 2, (3, 0): 0, (3, 1): 1, (3, 2): 2, (3, 3): 3}


def sgn(m, n):
    return -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1


def cnot(w):
    return {(m, n): sgn(m, n) * w[PC[(m, n)], PT[(m, n)]] for m in R4 for n in R4}


def hom(x):
    return [sp.Integer(1)] + list(x)


def homMap(N, v):          # N: 3x3 sympy matrix acting on the tail
    tail = sp.Matrix(v[1:])
    return [v[0]] + list(N * tail)


def actT(N, w):            # (actT N w) mu = homMap N (w mu)
    out = {}
    for m in R4:
        row = homMap(N, [w[m, n] for n in R4])
        for n in R4:
            out[m, n] = row[n]
    return out


def actC(N, w):            # (actC N w) mu nu = homMap N (fun k => w k nu) mu
    out = {}
    for n in R4:
        col = homMap(N, [w[k, n] for k in R4])
        for m in R4:
            out[m, n] = col[m]
    return out


REFLY = sp.diag(1, -1, 1)


def cnotTw(w):
    return actT(REFLY, cnot(actT(REFLY, w)))


def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return {(m, n): hx[m] * hy[n] for m in R4 for n in R4}


def sharpVec(b):
    return [sp.Rational(1, 2)] + [sp.S(c) / 2 for c in b]


def tens(X, Y):
    return {(m, n): X[m] * Y[n] for m in R4 for n in R4}


def tabMul(A, B):
    return {(m, n): sum(A[m, k] * B[k, n] for k in R4) for m in R4 for n in R4}


def tabT(A):
    return {(m, n): A[n, m] for m in R4 for n in R4}


def ipW(E, X):
    return sp.expand(sum(E[m, n] * X[m, n] for m in R4 for n in R4))


def dg(p, q, r, s):
    d = [p, q, r, s]
    return {(m, n): (d[m] if m == n else 0) for m in R4 for n in R4}


def smul(k, A):
    return {key: k * v for key, v in A.items()}


def eq(A, B):
    return all(sp.simplify(A[k] - B[k]) == 0 for k in A)


SGNY = [1, 1, -1, 1]


def transposeW(w):
    return {(m, n): SGNY[m] * SGNY[n] * w[m, n] for m in R4 for n in R4}


phiW = {(m, n): ((-1 if m == 2 else 1) if m == n else 0) for m in R4 for n in R4}
idW = dg(1, 1, 1, 1)
xplus, z3 = [1, 0, 0], [0, 0, 1]
mxplus, mz3 = [-1, 0, 0], [0, 0, -1]

E = {(m, n): sp.Symbol("E%d%d" % (m, n)) for m in R4 for n in R4}
X = {(m, n): sp.Symbol("X%d%d" % (m, n)) for m in R4 for n in R4}
b = sp.symbols("b0:3")
c = sp.symbols("c0:3")
p, q, r, s, k, kk = sp.symbols("p q r s k kk")

check("T0 cnot (prodState xplus z3) = phiW (base lemma, control)", eq(cnot(prodState(xplus, z3)), phiW))
check("T1 phiW = dg 1 1 (-1) 1", eq(phiW, dg(1, 1, -1, 1)))
check("T2 actT reflY phiW = idW (base lemma, control)", eq(actT(REFLY, phiW), idW))
check("T3 reflY z3 = z3", list(REFLY * sp.Matrix(z3)) == z3)
check("T4 cnotTw (prodState xplus z3) = idW", eq(cnotTw(prodState(xplus, z3)), idW))
check("T5 cnot (prodState (-xplus) (-z3)) = dg 1 (-1) (-1) (-1)",
      eq(cnot(prodState(mxplus, mz3)), dg(1, -1, -1, -1)))
check("T6 actT reflY (dg p q r s) = dg p q (-r) s", eq(actT(REFLY, dg(p, q, r, s)), dg(p, q, -r, s)))
check("T7 cnotTw (prodState (-xplus) (-z3)) = dg 1 (-1) 1 (-1)",
      eq(cnotTw(prodState(mxplus, mz3)), dg(1, -1, 1, -1)))
check("T8 tens (sharpVec b) (sharpVec c) = (1/4) prodState b c",
      eq(tens(sharpVec(b), sharpVec(c)), smul(sp.Rational(1, 4), prodState(b, c))))
check("T9 k * dg p q r s = dg (k p) (k q) (k r) (k s)", eq(smul(k, dg(p, q, r, s)), dg(k * p, k * q, k * r, k * s)))
a_ = sp.symbols("a0:4")
b_ = sp.symbols("bb0:4")
c_ = sp.symbols("cc0:4")
f_ = sp.symbols("f0:4")
lhs = ipW(dg(*a_), tabMul(tabMul(dg(*b_), dg(*c_)), tabT(dg(*f_))))
rhs = sum(a_[i] * b_[i] * c_[i] * f_[i] for i in range(4))
check("T10 ipW_dg: diagonal contraction formula", sp.expand(lhs - rhs) == 0)
check("T11 ipW (cnot E) X = ipW E (cnot X)", sp.expand(ipW(cnot(E), X) - ipW(E, cnot(X))) == 0)
check("T12 ipW (actT reflY E) X = ipW E (actT reflY X)",
      sp.expand(ipW(actT(REFLY, E), X) - ipW(E, actT(REFLY, X))) == 0)
check("T13 ipW (cnotTw E) X = ipW E (cnotTw X)", sp.expand(ipW(cnotTw(E), X) - ipW(E, cnotTw(X))) == 0)
check("T14 ipW (tens a b) w = pairVal a b w (definitional reordering)",
      sp.expand(ipW(tens(list(a_), list(b_)), X) - sum(a_[m] * X[m, n] * b_[n] for m in R4 for n in R4)) == 0)
check("T15 phiW . f . phiW^T = transposeW f", eq(tabMul(tabMul(phiW, E), tabT(phiW)), transposeW(E)))
check("T16 transposeW is an involution", eq(transposeW(transposeW(E)), E))
check("T17 ipW (transposeW E) X = ipW E (transposeW X)",
      sp.expand(ipW(transposeW(E), X) - ipW(E, transposeW(X))) == 0)
check("T18 ipW (tabT E) (tabT X) = ipW E X", sp.expand(ipW(tabT(E), tabT(X)) - ipW(E, X)) == 0)
check("T19 actT reflY is an involution and actT reflY . cnot . actT reflY is an involution",
      eq(actT(REFLY, actT(REFLY, E)), E) and eq(cnotTw(cnotTw(E)), E))

# Lemma P: the family-(i) value at every pattern, in the exact form the Lean proof reaches
sg = {False: -1, True: 1}
ok, rows = True, []
for t01, t23, t02, t13 in itertools.product([False, True], repeat=4):
    g = {False: cnot, True: cnotTw}
    Xs = g[t01](prodState(xplus, z3))
    Ys = g[t23](prodState(xplus, z3))
    Es = g[t02](tens(sharpVec(xplus), sharpVec(z3)))
    Fs = g[t13](tens(sharpVec(mxplus), sharpVec(mz3)))
    val = ipW(Xs, tabMul(tabMul(Es, Ys), tabT(Fs)))
    closed = sp.Rational(1, 16) * (1 * 1 * 1 * 1 + 1 * 1 * 1 * (-1) + sg[t01] * sg[t02] * sg[t23] * sg[t13]
                                   + 1 * 1 * 1 * (-1))
    even = (int(t01) + int(t23) + int(t02) + int(t13)) % 2 == 0
    ok &= (val == closed) and ((val >= 0) == even)
    rows.append("%d%d%d%d:%s" % (t01, t23, t02, t13, val))
check("P  family-(i) value = (1/16)(s01 s02 s23 s13 - 1), nonnegative exactly at the even patterns  ["
      + " ".join(rows) + "]", ok)
# countercontrol: with the effect F built from (xplus, z3) instead of (-xplus, -z3) the parity is NOT detected
ok_cc = True
for t01, t23, t02, t13 in itertools.product([False, True], repeat=4):
    g = {False: cnot, True: cnotTw}
    val = ipW(g[t01](prodState(xplus, z3)), tabMul(tabMul(g[t02](tens(sharpVec(xplus), sharpVec(z3))),
                                                          g[t23](prodState(xplus, z3))),
                                                   tabT(g[t13](tens(sharpVec(xplus), sharpVec(z3))))))
    ok_cc &= val >= 0
check("PC countercontrol: with F from (xplus, z3) every pattern gives a nonnegative value (witness choice load-bearing)",
      ok_cc)
print("--- precheck_parity: %d/%d" % (sum(checks), len(checks)))
print("VERDICT PREFLIGHT-PRECHECK-EXACT" if all(checks) else "VERDICT NOT RENDERED")
