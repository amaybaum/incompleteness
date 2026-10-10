"""EQ3-P probe p3 -- the conditional through a general gate link, and the rotation filters it supplies (exact).
Research only; base bcbc516f.  Usage (from scratchpad/eq3/P):
  python3 -I -B p3_general_links.py <base>/.../OIBridge/CompositeDimension.lean

CLAIMS:
  G1 for |a> = (1, u), |b> = (1, v) (symbolic complex u, v, u', v'), the link L_{a,b} = cnot(coords|a><a| (x)
     coords|b><b|) is the table of |psi_C><psi_C| with coefficient matrix C = diag(1, u) . [[1, v], [v, 1]] (row index
     = first token), and the four-copy conditional through links L_{a,b} on (0,2), L_{a',b'} on (1,3) of an effect f on
     (2,3) is  L_{a,b} . f . L_{a',b'}^T = 4 coordsW(Ad(C (x) C')(pauliW(transposeW f)))   (symbolic f)
  G2 orientation control: with C^T in place of C the identity fails (C is not symmetric for generic u, v)
  G3 rotation filters: for rational t, b = (1 - t^2, 2 i t) (unnormalized cos/sin pair) and u = 1, the coefficient
     C = (1 - t^2) 1 + 2 i t X is (1 + t^2) times a unitary (exact), i.e. the link supplies the X-rotation filter;
     with v = 0, u = (1 + 2 i t - t^2)/(1 + t^2)... (a unit phase) C = diag(1, u) is a Z-phase filter: |u|^2 = 1 exactly
  G4 the induced one-copy maps M_C (M_C[m,k] = (1/2) tr(sigma_m C sigma_k C^dag)) for these unitary C are rotations:
     M_C = homMap(R) with R in SO(3) (exact, two rational t values each); a Z-rotation and an X-rotation that are not
     commensurate-trivial generate (by the Euler decomposition, written) all of SO(3)
DECISION RULE (fixed before the first run): verdict `P3-GENERAL-LINKS-EXACT` iff all checks pass (G2 is a
countercontrol).  Exact arithmetic only.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import I, Matrix, Rational as R, eye, zeros  # noqa: E402

import eq3_lib as L  # noqa: E402

check = L.check
cnot = L.cnot_from(L.parse_cnot(sys.argv[1]))
ur, ui, vr, vi, pr, pi_, qr, qi = sp.symbols("ur ui vr vi pr pi qr qi", real=True)
u, v, up, vp = ur + I * ui, vr + I * vi, pr + I * pi_, qr + I * qi


def proj(x):
    return (x * x.H).applyfunc(sp.expand)


def link(z, w):
    ca, cb = L.coords1(proj(Matrix([1, z]))), L.coords1(proj(Matrix([1, w])))
    return cnot(Matrix(4, 4, lambda m, n: ca[m] * cb[n]))


def coef(z, w):
    return sp.diag(1, z) * Matrix([[1, w], [w, 1]])


f = Matrix(4, 4, lambda m, n: sp.Symbol(f"f{m}{n}", real=True))
Lab, Lab2 = link(u, v), link(up, vp)
C, Cp = coef(u, v), coef(up, vp)
psiC = Matrix([C[0, 0], C[0, 1], C[1, 0], C[1, 1]])
check("G1 L_{a,b} = coordsW(|psi_C><psi_C|) with C = diag(1,u).[[1,v],[v,1]] (row = first token) (symbolic u, v)",
      L.zero(Lab - L.coordsW(proj(psiC))))
lhs = (Lab * f * Lab2.T).applyfunc(sp.expand)
rhs = (4 * L.coordsW(L.ad(L.kron(C, Cp), L.pauliW(L.transposeW(f))))).applyfunc(sp.expand)
check("G1 L_{a,b}.f.L_{a',b'}^T = 4 coordsW(Ad(C (x) C')(pauliW(transposeW f))) (symbolic f, u, v, u', v')",
      L.zero(lhs - rhs))
rhsT = (4 * L.coordsW(L.ad(L.kron(C.T, Cp.T), L.pauliW(L.transposeW(f))))).applyfunc(sp.expand)
check("G2 countercontrol: with C^T, C'^T in place of C, C' the identity fails (C is not symmetric)",
      not L.zero(lhs - rhsT) and not L.zero(C - C.T))
okrot = True
for t in (R(1, 2), R(2, 3)):
    Cx = coef(1, 2 * I * t / (1 - t ** 2)) * (1 - t ** 2)            # (1 - t^2) 1 + 2 i t X
    nrm = 1 + t ** 2
    okrot = okrot and L.zero(Cx.H * Cx - nrm ** 2 * eye(2)) and L.zero(Cx - ((1 - t ** 2) * eye(2) + 2 * I * t * L.SX))
    uz = (1 - t ** 2 + 2 * I * t) / (1 + t ** 2)
    Cz = coef(uz, 0)
    okrot = okrot and sp.expand(uz * sp.conjugate(uz)) == 1 and L.zero(Cz.H * Cz - eye(2))
check("G3 the gate links supply unitary filters: (1 - t^2) 1 + 2 i t X = coefficient of the link with u = 1, "
      "v = 2it/(1 - t^2), times (1 - t^2), and it is (1 + t^2) times a unitary; diag(1, u_z) with |u_z| = 1 is a "
      "Z-phase (t = 1/2, 2/3)", okrot)


def M_of(Cm):
    return Matrix(4, 4, lambda m, k: sp.expand((L.PAULI[m] * Cm * L.PAULI[k] * Cm.H).trace() / 2))


okso3 = True
for t in (R(1, 2), R(2, 3)):
    for Cm in (((1 - t ** 2) * eye(2) + 2 * I * t * L.SX) / (1 + t ** 2),
               sp.diag(1, (1 - t ** 2 + 2 * I * t) / (1 + t ** 2))):
        M = M_of(Cm).applyfunc(sp.simplify)
        Rr = M[1:, 1:]
        okso3 = okso3 and M[0, 0] == 1 and all(M[0, k] == 0 and M[k, 0] == 0 for k in range(1, 4)) \
            and L.zero(Rr.T * Rr - eye(3)) and sp.simplify(Rr.det()) == 1
check("G4 for these unitary coefficients the induced one-copy map M_C is homMap(R) with R in SO(3) (exact): the "
      "links supply X- and Z-rotations, which generate SO(3) by the Euler decomposition (written)", okso3)
ok = L.summary("p3_general_links")
print("VERDICT " + ("P3-GENERAL-LINKS-EXACT" if ok else "NOT RENDERED"))
sys.exit(0 if ok else 1)
