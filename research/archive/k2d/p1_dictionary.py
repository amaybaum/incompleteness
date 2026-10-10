"""P1 — the W 3 dictionary, exact.

Question (preregistered decision rule): is DIM-1's carrier W 3 with prodState / prodEffVal / cnot / actT nflip /
actC nflip exactly the Pauli-coordinate image of the two-qubit Hermitian carrier with rho(x) (x) rho(y), Tr((E(x)F) .),
Ad(CNOT), Ad(I(x)X), Ad(X(x)I)?  PASS on every identity => the kernel's d = 3 witness is the Pauli transfer of the
quantum CNOT (a model of the DIM-1 hypotheses; this is a dictionary instance, NOT a derivation of the carrier).
The kernel tables pc, pt, sgn are parsed from CompositeDimension.lean, not transcribed.
Countercontrol: the transposed-target CNOT variant (Ad(CNOT) followed by a target y-reflection) must NOT equal the
kernel cnot.
"""
import sys
import sympy as sp
from k2lib import *

LEAN = sys.argv[1]

# product states and effects, symbolic
x = sp.symbols('x1:4', real=True)
y = sp.symbols('y1:4', real=True)
rx = (I2 + x[0] * SX + x[1] * SY + x[2] * SZ) / 2
ry = (I2 + y[0] * SX + y[1] * SY + y[2] * SZ) / 2
Wp = W_of(kron(rx, ry))
check('P1.1 Phi(rho(x)(x)rho(y)) = prodState x y (symbolic)', sp.simplify(Wp - prod_W(x, y)) == sp.zeros(4, 4))

a = sp.symbols('a0:4', real=True)
b = sp.symbols('b0:4', real=True)
E = a[0] * I2 + a[1] * SX + a[2] * SY + a[3] * SZ
F = b[0] * I2 + b[1] * SX + b[2] * SY + b[3] * SZ
# Tr(E rho(x)) = a0 + a.x : the homogenized coefficients ehom e = (a0, a1, a2, a3)
check('P1.2 Tr(E rho(x)) = a . hom x', sp.expand((E * rx).trace() - (sp.Matrix(a).T * hom(x))[0, 0]) == 0)
om = sp.Matrix(4, 4, lambda m, v: sp.Symbol('w%d%d' % (m, v), real=True))
rho = rho_of_W(om)
check('P1.3 Tr((E(x)F) rho_of_W(omega)) = pairVal a b omega (symbolic)',
      sp.expand((kron(E, F) * rho).trace() - pairval(sp.Matrix(a), sp.Matrix(b), om)) == 0)
check('P1.4 W_of(rho_of_W(omega)) = omega (the Pauli map is a bijection Herm(4) <-> W 3)',
      sp.simplify(W_of(rho) - om) == sp.zeros(4, 4))

CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
K = kernel_cnot_matrix(LEAN)
P = ptm(CNOT)
check('P1.5 kernel cnot (parsed pc/pt/sgn) = Pauli transfer matrix of Ad(CNOT)', K == P)
nflip = sp.diag(1, -1, -1)
check('P1.6 actT nflip = Pauli transfer of Ad(I (x) X)', actT_matrix(nflip) == ptm(kron(I2, SX)))
check('P1.7 actC nflip = Pauli transfer of Ad(X (x) I)', actC_matrix(nflip) == ptm(kron(SX, I2)))
# corners: z3 = (0,0,1) is |0><0|, -z3 is |1><1|
# countercontrol: reflected-target variant
Ry = actT_matrix(sp.diag(1, -1, 1))
check('P1.8 countercontrol: (I(x)R_y) cnot != cnot', Ry * K != K)
# the entangling witness image
phiW = sp.diag(1, 1, -1, 1)
inp = prod_W([1, 0, 0], [0, 0, 1])
check('P1.9 cnot(prodState xplus z3) = phiW (kernel :1222) and phiW = W(Phi+)',
      unvec(K * vec(inp)) == phiW and W_of(sp.Matrix([[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]) / 2) == phiW)
sys.exit(summary())
