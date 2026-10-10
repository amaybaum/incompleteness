"""EQ4-F premise probe (research only, exact arithmetic; no repo file is read or written).

Conventions transcribed from the Lean sources (CompositeDimension, K2Guard, FourCopyDefs):
  tables W 3 = 4x4, index 0 = unit, 1..3 = coordinates; hom x = (1, x);
  homMap R v = (v0, R v[1:]); actC R acts on the first index, actT R on the second;
  cnot w (m, n) = sgn(m, n) * w(pc(m, n), pt(m, n)); phiW = diag(1, 1, -1, 1); idW = I;
  pairVal a b w = a^T w b;  pauliW(w) = (1/4) sum w[m, n] s_m (x) s_n with s = (I, X, Y, Z).

Checks (decision rule fixed before the first run: PASS iff every check below holds, including
the countercontrols, which must come out as stated):
 K1  the target-side rotation R_H = [[0,0,1],[0,-1,0],[1,0,0]] is in SO(3), and
     actT R_H phiW is the table T_psi of psi = (|00>+|01>+|10>-|11>)/2 (pauliW(T_psi) = |psi><psi|).
 K2  phiW = cnot(prodState xplus z3), so phiW is a cnot image of a product.
 K3  pauliW(T_psi) is Hermitian of rank one and trace one (a pure state: not interior to Q3);
     T_psi has table rank 4 and cnot(T_psi) has table rank >= 2, so T_psi is neither a positive
     multiple of a pure product nor of a cnot image of one.
 K4  countercontrol: for R0 = rotation about the third axis by (3/5, 4/5), cnot(actC R0 phiW) has
     table rank exactly 1 (it is prodState (R0 xplus) z3), so the K3 test does detect cnot images.
 M1  cnot idW = chainW and pairVal at the sharp pair u = (-1,0,0), w = (0,0,-1) is -1/2, while
     idW takes (1 + u.w)/4 = 1/4 there (idW in maxCone by Cauchy-Schwarz, written).
 M2  famI factorizes on product effect tables: ipW X ((alpha(x)gamma) Y (beta(x)delta)^T) =
     (alpha^T X beta)(gamma^T Y delta), exactly, on random rational data (3 instances).
 M3  countercontrol: with the entangled effects E = F = phiW the famI value at X = idW,
     Y = diag(1,-1,-1,-1) (both in maxCone) is negative, so the product structure of the duals
     is load-bearing in the maxCone computation.
 M4  maxCone rotation covariance: pairVal a b (actC R w) = pairVal (homMap R^T a) b w and
     pairVal a b (actT R w) = pairVal a (homMap R^T b) w, exactly, for a rational Cayley rotation.
 O1  mixed orientation: actT reflY (cnot idW) = chainW and actC reflY (cnot idW) = chainW, and
     actT reflY phiW = idW = actC reflY phiW.
 O2  rank(phiW) = 4 while every prodState has table rank 1 (an N-CLASS gate is not the identity).
"""
import random
import sympy as sp
from sympy import Rational as Q, Matrix, I as iu

random.seed(20261009)

def hom(x): return [Q(1)] + list(x)
def homMap(R, v):
    t = R * Matrix(v[1:])
    return [v[0]] + list(t)
def actC(R, w):
    out = sp.zeros(4, 4)
    for n in range(4):
        col = homMap(R, [w[m, n] for m in range(4)])
        for m in range(4): out[m, n] = col[m]
    return out
def actT(R, w):
    out = sp.zeros(4, 4)
    for m in range(4):
        row = homMap(R, [w[m, n] for n in range(4)])
        for n in range(4): out[m, n] = row[n]
    return out
PC = [[0,0,3,3],[1,1,2,2],[2,2,1,1],[3,3,0,0]]
PT = [[0,1,2,3],[1,0,3,2],[1,0,3,2],[0,1,2,3]]
def sgn(m, n): return -1 if (m, n) in ((1, 3), (2, 2)) else 1
def cnot(w): return Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])
def prodState(x, y): return Matrix(4, 1, hom(x)) * Matrix(1, 4, hom(y))
phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
chainW = Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
reflY = sp.diag(1, -1, 1)
xplus, z3 = [Q(1), Q(0), Q(0)], [Q(0), Q(0), Q(1)]
sig = [sp.eye(2), Matrix([[0, 1], [1, 0]]), Matrix([[0, -iu], [iu, 0]]), Matrix([[1, 0], [0, -1]])]
def kron(A, B): return sp.kronecker_product(A, B)
def pauliW(w):
    out = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            if w[m, n] != 0: out += w[m, n] * kron(sig[m], sig[n])
    return (out / 4).applyfunc(sp.nsimplify)
def pairVal(a, b, w): return (Matrix(1, 4, a) * w * Matrix(4, 1, b))[0, 0]
def tabMul(A, B): return A * B
def ipW(E, X): return sum(E[m, n] * X[m, n] for m in range(4) for n in range(4))
def isRot(R): return sp.simplify(R.T * R - sp.eye(3)) == sp.zeros(3, 3) and R.det() == 1
def rq(): return Q(random.randint(-9, 9), random.randint(1, 7))

results = []
def check(name, ok, note=""):
    results.append((name, bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {note}")

# K1
RH = Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
Tpsi = actT(RH, phiW)
psi = Matrix([1, 1, 1, -1]) / 2
check("K1 R_H in SO(3)", isRot(RH))
check("K1 actT R_H phiW = T_psi with pauliW(T_psi) = |psi><psi|",
      sp.simplify(pauliW(Tpsi) - psi * psi.T) == sp.zeros(4, 4), f"T_psi={Tpsi.tolist()}")
# K2
check("K2 phiW = cnot(prodState xplus z3)", cnot(prodState(xplus, z3)) == phiW)
# K3
P = pauliW(Tpsi)
check("K3 pauliW(T_psi) Hermitian, rank 1, trace 1",
      P == P.H and P.rank() == 1 and sp.simplify(P.trace()) == 1)
check("K3 table rank T_psi = 4, table rank cnot(T_psi) >= 2",
      Tpsi.rank() == 4 and cnot(Tpsi).rank() >= 2, f"ranks {Tpsi.rank()}, {cnot(Tpsi).rank()}")
# K4 countercontrol
R0 = Matrix([[Q(3, 5), Q(-4, 5), 0], [Q(4, 5), Q(3, 5), 0], [0, 0, 1]])
w0 = actC(R0, phiW)
c0 = cnot(w0)
check("K4 countercontrol: R0 in SO(3) and cnot(actC R0 phiW) has table rank 1 = prodState (R0 xplus) z3",
      isRot(R0) and c0.rank() == 1 and c0 == prodState(list(R0 * Matrix(xplus)), z3))
# M1
check("M1 cnot idW = chainW", cnot(idW) == chainW)
a = [Q(1, 2)] + [Q(-1, 2), 0, 0]
b = [Q(1, 2)] + [0, 0, Q(-1, 2)]
v_chain, v_id = pairVal(a, b, chainW), pairVal(a, b, idW)
check("M1 chainW = -1/2 and idW = 1/4 at the sharp pair", v_chain == Q(-1, 2) and v_id == Q(1, 4),
      f"({v_chain}, {v_id})")
# M2
ok = True
for _ in range(3):
    al, be, ga, de = ([rq() for _ in range(4)] for _ in range(4))
    X = Matrix(4, 4, lambda m, n: rq()); Y = Matrix(4, 4, lambda m, n: rq())
    E = Matrix(4, 1, al) * Matrix(1, 4, ga); F = Matrix(4, 1, be) * Matrix(1, 4, de)
    lhs = ipW(X, tabMul(tabMul(E, Y), F.T))
    rhs = pairVal(al, be, X) * pairVal(ga, de, Y)
    ok &= sp.simplify(lhs - rhs) == 0
check("M2 famI factorizes on product effect tables (3 random rational instances)", ok)
# M3 countercontrol
Ysing = sp.diag(1, -1, -1, -1)
v = ipW(idW, tabMul(tabMul(phiW, Ysing), phiW.T))
# both in maxCone: idW by M1's Cauchy-Schwarz; Ysing is a quantum state (singlet), pauliW PSD
check("M3 countercontrol: entangled effects give famI value < 0 on maxCone tables",
      v < 0 and all(ev >= 0 for ev in pauliW(Ysing).eigenvals()), f"value {v}")
# M4
S = Matrix([[0, rq(), rq()], [0, 0, rq()], [0, 0, 0]]); S = S - S.T
Rg = (sp.eye(3) - S) * (sp.eye(3) + S).inv()
w = Matrix(4, 4, lambda m, n: rq()); a = [rq() for _ in range(4)]; b = [rq() for _ in range(4)]
ok4 = isRot(Rg)
ok4 &= sp.simplify(pairVal(a, b, actC(Rg, w)) - pairVal(homMap(Rg.T, a), b, w)) == 0
ok4 &= sp.simplify(pairVal(a, b, actT(Rg, w)) - pairVal(a, homMap(Rg.T, b), w)) == 0
check("M4 maxCone rotation covariance (Cayley rotation, exact)", ok4)
# O1
check("O1 actT reflY (cnot idW) = chainW = actC reflY (cnot idW)",
      actT(reflY, cnot(idW)) == chainW and actC(reflY, cnot(idW)) == chainW)
check("O1 actT reflY phiW = idW = actC reflY phiW",
      actT(reflY, phiW) == idW and actC(reflY, phiW) == idW)
# O2
check("O2 rank phiW = 4; prodState has rank 1", phiW.rank() == 4 and prodState(xplus, z3).rank() == 1)

n_ok = sum(ok for _, ok in results)
print(f"{n_ok}/{len(results)}")
print("VERDICT", "PREMISE-PROBE-PASS" if n_ok == len(results) else "PREMISE-PROBE-FAIL")
