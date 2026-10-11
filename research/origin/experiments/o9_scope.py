#!/usr/bin/env python3
"""
o9_scope.py -- scope of O9-S: is the level-one obstruction specific to the balanced angle?

Thread research/origin, round 3, node O9 (fixed-point pass 2). Exact arithmetic (sympy algebraic numbers).
The level-one class at angle alpha contains rot(alpha) = mixImage 1 alpha (StateMixingCoupling.lean:50) and the
quarter phase S = phaseGate (1,0) = diag(1, i) (LieRankSource.lean:209). The word W(alpha) = rot(alpha) S rot(alpha) S^dagger
is a level-one member.

DECISION RULE (fixed before run 1):
  S1  at alpha = pi/8: det W = 1, trace W = 1 + sqrt2/2 exactly, its minimal polynomial over Q is not monic over Z
      (so W has infinite order), and rot(pi/8)^2 = rot(pi/4) exactly;
  S2  at alpha = pi/4: trace W is an algebraic integer and W^k = 1 for some k <= 48 (finite order);
  CC  the infinite-order test (minimal polynomial of the trace not monic over Z) fires at alpha = pi/4 (must be False).
  VERDICT SCOPE-ANGLE-SPECIFIC if S1 and S2 hold and CC is False; VERDICT VOID if CC is True; otherwise
  VERDICT UNDECIDED.
"""
import sys
import sympy as sp

x = sp.symbols('x')


def rot(a):
    return sp.Matrix([[sp.cos(a), -sp.sin(a)], [sp.sin(a), sp.cos(a)]])


S = sp.diag(1, sp.I)


def word(a):
    R = rot(a)
    return sp.simplify(R * S * R * S.H)


def integral_trace(t):
    mp = sp.minimal_polynomial(t, x)
    poly = sp.Poly(mp, x)
    lc = poly.LC()
    monic_int = all(sp.Rational(c / lc).q == 1 for c in poly.all_coeffs())
    return mp, monic_int


print('== o9_scope ==')
W8 = word(sp.pi / 8)
d8 = sp.simplify(W8.det())
t8 = sp.nsimplify(sp.simplify(W8.trace()))
mp8, int8 = integral_trace(t8)
sq = sp.simplify(rot(sp.pi / 8) ** 2 - rot(sp.pi / 4))
sq_zero = bool(sq.is_zero_matrix)
s1 = (sp.simplify(d8 - 1) == 0) and sp.simplify(t8 - (1 + sp.sqrt(2) / 2)) == 0 and (not int8) and sq_zero
print('S1  alpha = pi/8: det W = %s; trace W = %s; minimal polynomial %s (monic over Z: %s); rot(pi/8)^2 = rot(pi/4): %s'
      '  -> %s' % (d8, t8, mp8, int8, sq_zero, s1))
W4 = word(sp.pi / 4)
t4 = sp.nsimplify(sp.simplify(W4.trace()))
mp4, int4 = integral_trace(t4)
P = sp.eye(2)
order4 = None
for k in range(1, 49):
    P = sp.simplify(P * W4)
    if sp.simplify(P - sp.eye(2)).is_zero_matrix:
        order4 = k
        break
s2 = int4 and order4 is not None
print('S2  alpha = pi/4: trace W = %s; minimal polynomial %s (monic over Z: %s); order %s  -> %s'
      % (t4, mp4, int4, order4, s2))
cc = not int4
print('CC  infinite-order test fires at alpha = pi/4: %s  -> %s' % (cc, 'CC-OK (False as required)' if not cc
                                                                   else 'CC-FAILED (True)'))
if cc:
    print('VERDICT VOID')
elif s1 and s2:
    print('VERDICT SCOPE-ANGLE-SPECIFIC: at alpha = pi/8 (alpha/pi rational) the level-one group is infinite and '
          'contains the level-one group at pi/4; the level-one obstruction of O9-L1 belongs to the balanced angle')
else:
    print('VERDICT UNDECIDED')
sys.stderr.write('exit 0\n')
