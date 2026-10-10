#!/usr/bin/env python3
"""Exact check of the owner's note 6 (stage 4): CNOT = (I(x)P+ + iZ(x)P-) . (I(x)P+ - i I(x)P-); the first factor is in
the connected group {U(x)P+ + V(x)P- : U, V in SU(2)}; the discrete factor is not (sector determinants 1 and -1), acts as
a target X-rotation up to global phase, and its square I(x)X is in the connected group (V = -I); so the quotient of the
generated group by the connected part has order 2.  DECISION RULE: all lines CONFIRMED => NOTE6-CONFIRMED."""
import sympy as sp, sys
I2 = sp.eye(2); SX = sp.Matrix([[0,1],[1,0]]); SZ = sp.Matrix([[1,0],[0,-1]]); kron = sp.kronecker_product
Pp = (I2 + SX)/2; Pm = (I2 - SX)/2
CNOT = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
A = kron(I2, Pp) + kron(sp.I*SZ, Pm); D = kron(I2, Pp) - sp.I*kron(I2, Pm)
R = []
def rec(cid, ok, text): ok = bool(ok); R.append(ok); print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}")
rec("N6-1", (A*D - CNOT).applyfunc(sp.expand).is_zero_matrix, "CNOT = (I(x)P+ + iZ(x)P-)(I(x)P+ - iI(x)P-)")
rec("N6-2", sp.expand((sp.I*SZ).det()) == 1 and (A.H*A - sp.eye(4)).applyfunc(sp.expand).is_zero_matrix, "the first factor has U = I, V = iZ in SU(2): it lies in the connected group")
rec("N6-3", sp.expand(((-sp.I)*I2).det()) == -1, "the discrete factor's sector blocks I and -iI have determinants 1 and -1: not in the connected group under any global phase")
rec("N6-4", (D - kron(I2, (1-sp.I)/2*(I2 + sp.I*SX))).applyfunc(sp.expand).is_zero_matrix, "the discrete factor is e^{-i pi/4} . (I + iX)/sqrt2 on the target, a target X-rotation up to a global phase")
rec("N6-5", (D*D - kron(I2, SX)).applyfunc(sp.expand).is_zero_matrix and (kron(I2, SX) - (kron(I2, Pp) + kron(-I2, Pm))).applyfunc(sp.expand).is_zero_matrix and sp.expand((-I2).det()) == 1,
    "its square is I(x)X = I(x)P+ + (-I)(x)P-, which is in the connected group (V = -I in SU(2)): the quotient has order 2")
n = sum(R); print(f"checks: {len(R)}, confirmed: {n}"); print("VERDICT", "NOTE6-CONFIRMED" if n == len(R) else "NOTE6-MISMATCH"); sys.exit(0 if n == len(R) else 1)
