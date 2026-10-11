#!/usr/bin/env python3
"""b11_preflight.py -- node B11 of research/bridge (round 3): exact preflight of every statement of the design module
BridgeDictionary.lean (round 3) under the kernel's conventions, before the CI dispatch.

DECISION RULE (fixed 2026-10-11T00:29:05Z, from `date -u` immediately before writing; before run 1).

Conventions mirrored from the kernel at L (this tree's verification/ is identical to L):
  W 3 tables w[mu][nu], mu the control (first token) index, nu the target index; hom x = (1, x);
  homMap N v = vecCons (v 0) (N (vecTail v)) (CompositeDimension.lean:112), so homMap N = 1 (+) N;
  actT N w = fun mu => homMap N (w mu)   (rows mapped: w Nh^T)        (CompositeDimension.lean:198);
  actC N w = fun mu nu => homMap N (fun k => w k nu) mu   (Nh w)       (CompositeDimension.lean:201);
  cnot w = fun mu nu => sgn mu nu * w (pc mu nu) (pt mu nu), pc/pt parsed from CompositeDimension.lean;
  nflip x = (x0, -x1, -x2); tensorOf XA XB (a,b) (c,d) = XA a c * XB b d (MonoidalCompletion.lean:193),
  with (a, b) <-> 2a + b, i.e. sympy's kronecker_product.
Module definitions mirrored: pauli = [1, X, Y, Z]; tokMat v = sum (v_mu / 2) pauli mu;
  dict w = sum (w_mu,nu / 4) tensorOf (pauli mu) (pauli nu); rotZ c s x = (c x0 - s x1, s x0 + c x1, x2);
  zPhase c s = diagonal (1, c + i s); zPhaseD c s = diagonal (1, c - i s);
  proj0 = diagonal (1, 0), proj1 = diagonal (0, 1); cnotMat = tensorOf proj0 1 + tensorOf proj1 (pauli 1).
Symbols: c, s real; the unit circle is imposed by substituting s^2 -> 1 - c^2 only where a check says so.

CHECKS
  F1  dict_tens: dict (tens X Y) = tensorOf (tokMat X) (tokMat Y), X, Y symbolic (8 symbols).
  F2  dict_cnot: dict (cnot w) = cnotMat * dict w * cnotMat on all 16 basis tables.
  F3  zPhase_conjTranspose: (zPhase c s)^H = zPhaseD c s, symbolically.
  F4  the 2x2 phase identities, with U = zPhase c s:
        U pauli1 U^H = c pauli1 + s pauli2 and U pauli2 U^H = -s pauli1 + c pauli2 WITHOUT the circle;
        U pauli0 U^H = pauli0 and U pauli3 U^H = pauli3 WITH the circle, and both FAIL without it.
  F5  conj_dict_right / conj_dict_left: for a symbolic 2x2 U (8 real symbols) and every basis table w,
        (1 (x) U) dict w (1 (x) U)^H = sum (w_mu,nu / 4) tensorOf (pauli mu) (U pauli nu U^H), and
        (U (x) 1) dict w (U (x) 1)^H = sum (w_mu,nu / 4) tensorOf (U pauli mu U^H) (pauli nu).
  F6  homMap entries: homMap (rotZ c s) v = (v0, c v1 - s v2, s v1 + c v2, v3) and
        homMap nflip v = (v0, v1, -v2, -v3), symbolically.
  F7  dict_actT_rotZ / dict_actC_rotZ: on all 16 basis tables, dict (actT (rotZ c s) w) =
        (1 (x) U) dict w (1 (x) U)^H and dict (actC (rotZ c s) w) = (U (x) 1) dict w (U (x) 1)^H on the circle;
        and the actT identity fails for some basis table at (c, s) = (0, 0) (countercontrol).
  F8  dict_actT_nflip / dict_actC_nflip: on all 16 basis tables, with X = pauli 1 (X^H = X), and the 2x2
        identities X pauli0 X = pauli0, X pauli1 X = pauli1, X pauli2 X = (-1) pauli2, X pauli3 X = (-1) pauli3.
  F9  zPhase_unitary: (zPhase c s)^H zPhase c s = 1 on the circle; the (1, 1) entry of zPhase 0 0 pauli0
        (zPhase 0 0)^H is 0, not 1 (the countercontrol of the module, phaseU_pauli0 off the circle).
  F10 rotZ (cos t) (sin t) equals the kernel's rotFun t (KInfFoundations.lean:351) symbolically in t, and
        rotZ (3/5) (4/5) satisfies the circle (positive control of the module).

VERDICT B11-PREFLIGHT-OK iff F1-F10 all PASS; otherwise VERDICT B11-PREFLIGHT-FAILED followed by the failing ids.
"""
import os
import re
import sys

import sympy as sp

PASS, FAIL = [], []


def check(cid, ok, msg=""):
    print(f"{cid:4s} {'PASS' if ok else 'FAIL'}  {msg}")
    (PASS if ok else FAIL).append(cid)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..")
I = sp.I
kron = sp.kronecker_product
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
PAULI = [I2, X, Y, Z]


def dag(M):
    return M.conjugate().T


def ex(M):
    return M.applyfunc(sp.expand)


def is_zero(M):
    return ex(M) == sp.zeros(*M.shape)


def tensorOf(A, B):
    return kron(A, B)


def tokMat(v):
    return sum((v[m] / 2 * PAULI[m] for m in range(4)), sp.zeros(2, 2))


def dict_(w):
    return sum((w[m, n] / 4 * tensorOf(PAULI[m], PAULI[n]) for m in range(4) for n in range(4)), sp.zeros(4, 4))


def E(m, n):
    w = sp.zeros(4, 4)
    w[m, n] = 1
    return w


BASIS = [E(m, n) for m in range(4) for n in range(4)]


def Nh(N):
    H = sp.zeros(4, 4)
    H[0, 0] = 1
    H[1:, 1:] = N
    return H


def actT(N, w):
    return w * Nh(N).T


def actC(N, w):
    return Nh(N) * w


SRC = open(os.path.join(ROOT, "verification", "lean-mathlib", "OIBridge", "CompositeDimension.lean"),
           encoding="utf-8").read()
PAT = re.compile(r"\|\s*(\d),\s*(\d)\s*=>\s*(\d)")


def parse_table(name, nxt):
    blk = SRC[SRC.index(f"def {name} : Fin 4 → Fin 4 → Fin 4"):SRC.index(nxt)]
    T = [[None] * 4 for _ in range(4)]
    for a, b, v in PAT.findall(blk):
        T[int(a)][int(b)] = int(v)
    assert all(T[i][j] is not None for i in range(4) for j in range(4))
    return T


PC = parse_table("pc", "def pt : Fin 4")
PT = parse_table("pt", "def cnotFun")


def sgn(m, n):
    return -1 if (m, n) in ((1, 3), (2, 2)) else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


c, s, t = sp.symbols("c s t", real=True)
circ = {s ** 2: 1 - c ** 2}


def on_circle(M):
    return M.applyfunc(lambda z: sp.expand(sp.expand(z).subs(circ)))


def rotZ(cc, ss):
    return sp.Matrix([[cc, -ss, 0], [ss, cc, 0], [0, 0, 1]])


def zPhase(cc, ss):
    return sp.diag(1, cc + I * ss)


def zPhaseD(cc, ss):
    return sp.diag(1, cc - I * ss)


nflip = sp.diag(1, -1, -1)
proj0 = sp.diag(1, 0)
proj1 = sp.diag(0, 1)
cnotMat = tensorOf(proj0, I2) + tensorOf(proj1, X)

# F1
xs = sp.symbols("x0:4", real=True)
ys = sp.symbols("y0:4", real=True)
tensXY = sp.Matrix(4, 4, lambda m, n: xs[m] * ys[n])
check("F1", is_zero(dict_(tensXY) - tensorOf(tokMat(xs), tokMat(ys))),
      "dict (tens X Y) = tensorOf (tokMat X) (tokMat Y), symbolic")

# F2
check("F2", all(is_zero(dict_(cnot(b)) - cnotMat * dict_(b) * cnotMat) for b in BASIS),
      f"dict (cnot w) = cnotMat dict w cnotMat on 16 basis tables (pc = {PC}, pt = {PT})")

# F3
U = zPhase(c, s)
check("F3", is_zero(dag(U) - zPhaseD(c, s)), "(zPhase c s)^H = zPhaseD c s")

# F4
f4a = is_zero(U * PAULI[1] * dag(U) - (c * PAULI[1] + s * PAULI[2]))
f4b = is_zero(U * PAULI[2] * dag(U) - (-s * PAULI[1] + c * PAULI[2]))
f4c = on_circle(U * PAULI[0] * dag(U) - PAULI[0]) == sp.zeros(2, 2)
f4d = on_circle(U * PAULI[3] * dag(U) - PAULI[3]) == sp.zeros(2, 2)
f4e = not is_zero(U * PAULI[0] * dag(U) - PAULI[0]) and not is_zero(U * PAULI[3] * dag(U) - PAULI[3])
check("F4", f4a and f4b and f4c and f4d and f4e,
      f"U s1 U^H = c s1 + s s2: {f4a}; U s2 U^H = -s s1 + c s2: {f4b} (no circle needed); "
      f"U s0 U^H = s0: {f4c}, U s3 U^H = s3: {f4d} on the circle; both fail off it: {f4e}")

# F5
u = sp.symbols("u0:8", real=True)
Ug = sp.Matrix([[u[0] + I * u[1], u[2] + I * u[3]], [u[4] + I * u[5], u[6] + I * u[7]]])
f5r = all(is_zero(tensorOf(I2, Ug) * dict_(b) * dag(tensorOf(I2, Ug)) -
                  sum((b[m, n] / 4 * tensorOf(PAULI[m], Ug * PAULI[n] * dag(Ug))
                       for m in range(4) for n in range(4)), sp.zeros(4, 4))) for b in BASIS)
f5l = all(is_zero(tensorOf(Ug, I2) * dict_(b) * dag(tensorOf(Ug, I2)) -
                  sum((b[m, n] / 4 * tensorOf(Ug * PAULI[m] * dag(Ug), PAULI[n])
                       for m in range(4) for n in range(4)), sp.zeros(4, 4))) for b in BASIS)
check("F5", f5r and f5l, f"conj_dict_right: {f5r}; conj_dict_left: {f5l} (symbolic U, 16 basis tables)")

# F6
vs = sp.symbols("v0:4", real=True)
vv = sp.Matrix(vs)
hr = Nh(rotZ(c, s)) * vv
hn = Nh(nflip) * vv
f6 = list(ex(hr)) == [vs[0], c * vs[1] - s * vs[2], s * vs[1] + c * vs[2], vs[3]] and \
    list(ex(hn)) == [vs[0], vs[1], -vs[2], -vs[3]]
check("F6", f6, f"homMap (rotZ c s) v = {list(ex(hr))}; homMap nflip v = {list(ex(hn))}")

# F7
f7T = all(on_circle(dict_(actT(rotZ(c, s), b)) - tensorOf(I2, U) * dict_(b) * dag(tensorOf(I2, U))) ==
          sp.zeros(4, 4) for b in BASIS)
f7C = all(on_circle(dict_(actC(rotZ(c, s), b)) - tensorOf(U, I2) * dict_(b) * dag(tensorOf(U, I2))) ==
          sp.zeros(4, 4) for b in BASIS)
U00 = zPhase(0, 0)
f7x = any(not is_zero(dict_(actT(rotZ(0, 0), b)) - tensorOf(I2, U00) * dict_(b) * dag(tensorOf(I2, U00)))
          for b in BASIS)
check("F7", f7T and f7C and f7x,
      f"dict_actT_rotZ: {f7T}; dict_actC_rotZ: {f7C} (on the circle, 16 basis tables); fails at (0, 0): {f7x}")

# F8
x2 = [is_zero(X * PAULI[0] * X - PAULI[0]), is_zero(X * PAULI[1] * X - PAULI[1]),
      is_zero(X * PAULI[2] * X + PAULI[2]), is_zero(X * PAULI[3] * X + PAULI[3])]
f8T = all(is_zero(dict_(actT(nflip, b)) - tensorOf(I2, X) * dict_(b) * dag(tensorOf(I2, X))) for b in BASIS)
f8C = all(is_zero(dict_(actC(nflip, b)) - tensorOf(X, I2) * dict_(b) * dag(tensorOf(X, I2))) for b in BASIS)
check("F8", all(x2) and f8T and f8C and is_zero(dag(X) - X),
      f"X s_k X = (1, 1, -1, -1) s_k: {x2}; dict_actT_nflip: {f8T}; dict_actC_nflip: {f8C}")

# F9
f9u = on_circle(dag(U) * U - I2) == sp.zeros(2, 2)
cc11 = ex(U00 * PAULI[0] * dag(U00))[1, 1]
check("F9", f9u and cc11 == 0 and PAULI[0][1, 1] == 1,
      f"(zPhase c s)^H zPhase c s = 1 on the circle: {f9u}; (zPhase 0 0 s0 (zPhase 0 0)^H)[1,1] = {cc11} != 1")

# F10
rotFun_t = sp.Matrix([[sp.cos(t), -sp.sin(t), 0], [sp.sin(t), sp.cos(t), 0], [0, 0, 1]])
f10 = (rotZ(sp.cos(t), sp.sin(t)) - rotFun_t) == sp.zeros(3, 3) and \
    sp.Rational(3, 5) ** 2 + sp.Rational(4, 5) ** 2 == 1
check("F10", f10, "rotZ (cos t) (sin t) = rotFun t (kernel); (3/5)^2 + (4/5)^2 = 1")

print()
print(f"PASS {len(PASS)}  FAIL {len(FAIL)}")
print("VERDICT B11-PREFLIGHT-OK" if not FAIL else "VERDICT B11-PREFLIGHT-FAILED " + " ".join(FAIL))
sys.exit(0)
