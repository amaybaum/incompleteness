"""P4 — kernel-cheap numbers for proposals T5 and T8 (exact).

T5 (reflection no-go): the chain prodState xplus z3 -> cnot -> actT reflY -> cnot, read by the product effect
  prodEffVal (sharpEff (-e1)) (sharpEff (-e3)), is negative.  sharpEff b = affOf (1/2, b/2) (EffectSpace.lean:57-65).
T8 (a composite is never elementary in the singleton-face sense): the product effect sharpEff z3 (x) unit is proper
  and certain on two distinct product states.
Countercontrol for T5: the same chain with nflip (a rotation) in place of reflY is nonnegative on that effect pair and
  on the whole P3 effect family (P3.d').
"""
import sys
import sympy as sp
from k2lib import *

LEAN = sys.argv[1]
K = kernel_cnot_matrix(LEAN)
reflY = sp.diag(1, -1, 1)


def sharpVec(b):
    return sp.Matrix([sp.Rational(1, 2)] + [sp.Rational(bi, 2) for bi in b])


a = sharpVec([-1, 0, 0])
b = sharpVec([0, 0, -1])
w0 = prod_W([1, 0, 0], [0, 0, 1])
w1 = unvec(K * vec(w0))
w2 = unvec(actT_matrix(reflY) * vec(w1))
w3 = unvec(K * vec(w2))
v = pairval(a, b, w3)
check('P4.T5 chain value prodEffVal (sharpEff -e1) (sharpEff -e3) (cnot (actT reflY (cnot (prodState xplus z3)))) = -1/2',
      v == sp.Rational(-1, 2), (w1, w2, w3))
w2c = unvec(actT_matrix(sp.diag(1, -1, -1)) * vec(w1))
w3c = unvec(K * vec(w2c))
check('P4.T5\' countercontrol (nflip instead of reflY): same effect pair gives >= 0', pairval(a, b, w3c) >= 0,
      pairval(a, b, w3c))
check('P4.T5\'\' the intermediate actT reflY (phiW) is the identity array (W(SWAP/2))', w2 == sp.eye(4))
# T8
E = sharpVec([0, 0, 1])
U = sp.Matrix([1, 0, 0, 0])
vals = [pairval(E, U, prod_W(x, y)) for (x, y) in [([0, 0, 1], [0, 0, 1]), ([0, 0, 1], [0, 0, -1]), ([0, 0, -1], [0, 0, 1])]]
check('P4.T8 sharpEff z3 (x) unit: values 1, 1 on prodState z3 z3 != prodState z3 (-z3), and 0 on prodState (-z3) z3',
      vals == [1, 1, 0] and prod_W([0, 0, 1], [0, 0, 1]) != prod_W([0, 0, 1], [0, 0, -1]), vals)
sys.exit(summary())
