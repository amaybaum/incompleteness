#!/usr/bin/env python3
"""EQ-D, node N5 (QD3): the qubit data of Theorem A inside the corpus class MixC (StateMixingCoupling.lean:56).

MixC contains, at Fin 2 (after relabelling Fin 2 x Fin 1 ~ Fin 2 with MixR.relabel):
  phaseGate 0 = D = diag(i, 1)                        (MixR.phase 1 (0,0))
  rot t = [[cos t, -sin t], [sin t, cos t]]           (MixR.mix 1 t, the sourced datum at every angle)
and is closed under mul and smul (|a| <= 1).  Checked exactly here:
  (1) rot t = exp(-i t Y)                                       (closed form, sympy matrix exponential)
  (2) D * rot t * D^3 = flow (transition 0 1) t = exp(-i t X)   (D^3 = D^dagger, by mul)
  (3) flow (transition 0 1)(pi/4) * rot t * flow (transition 0 1)(-pi/4) = exp(-i t Z)
  (4) exp(-i t) * exp(-i t Z) = diag(exp(-2 i t), 1) = flow (transition 0 0) t   (smul by a unit scalar)
So MixC contains the three qubit families Theorem A consumes; with mixC_arch, mixC_contextStable and
mixR_labelInvariant (kernel), Theorem A gives DrivesElementary MixC, and with mixC_daggerStable a
QuantumArchitecture, hence exact finite operational QM of mixTheory A at every nonempty carrier A
(genTheory_qm_of_quantumArchitecture), where the kernel states it at Fin 2 only (mixTheory_qm, :511).
"""
import sys

import sympy as sp

I = sp.I
t = sp.symbols('t', real=True)
FAILS = []


def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok:
        FAILS.append(name)


def zero(M):
    return all(sp.simplify(sp.expand_complex(sp.expand(sp.simplify(v)))) == 0 for v in M)


X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
D = sp.diag(I, 1)
rot = sp.Matrix([[sp.cos(t), -sp.sin(t)], [sp.sin(t), sp.cos(t)]])
expX = lambda s: sp.Matrix([[sp.cos(s), -I * sp.sin(s)], [-I * sp.sin(s), sp.cos(s)]])

check('(0) D^3 = D^dagger and D^4 = 1 (so D^3 is in MixC by mul)', D**3 == D.H and D**4 == sp.eye(2))
check('(1) rot t = exp(-i t Y)', zero((-I * t * Y).exp() - rot))
check('(1b) closed form exp(-i s X) used for flow (transition 0 1) s', zero((-I * t * X).exp() - expX(t)))
check('(2) D * rot t * D^3 = exp(-i t X) = flow (transition 0 1) t', zero(D * rot * D**3 - expX(t)))
check('(3) flow(pi/4) * rot t * flow(-pi/4) = exp(-i t Z)',
      zero(expX(sp.pi / 4) * rot * expX(-sp.pi / 4) - (-I * t * Z).exp()))
check('(4) exp(-i t) * exp(-i t Z) = diag(exp(-2 i t), 1) = flow (transition 0 0) t, and |exp(-i t)| = 1',
      zero(sp.exp(-I * t) * (-I * t * Z).exp() - sp.diag(sp.exp(-2 * I * t), 1))
      and sp.simplify(sp.Abs(sp.exp(-I * t)) - 1) == 0)
check('(4b) closed form: exp(-i t (2 E00)) = diag(exp(-2 i t), 1)',
      zero((-I * t * sp.diag(2, 0)).exp() - sp.diag(sp.exp(-2 * I * t), 1)))
# countercontrol: without the phase gate D the real rotations alone stay real (no exp(-i t X) at generic t)
check('countercontrol: rot t is real for real t, while exp(-i t X) has the non-real entry -i sin t',
      all(sp.im(v) == 0 for v in rot) and sp.simplify(sp.im(expX(t)[0, 1]) + sp.sin(t)) == 0)
print()
if FAILS:
    print('VERDICT  VOID — failed:', FAILS)
    sys.exit(1)
print('VERDICT  MixC contains phaseGate 0, flow (transition 0 1) t and flow (transition 0 0) t at Fin 2 for every t')
