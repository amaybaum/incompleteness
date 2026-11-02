"""Does the corpus probe's instance set discriminate the stated constant from a false one?
Re-evaluates the probe's Q1, Q2, Q5 instances (rebuilt here independently) in interval
arithmetic against c * p0 delta^2 (nats) for c = 1 (stated), 2 (false in general), 4 (l1 reading).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from cmi_iv import *

q1 = {((x0,), x1, (x0,)): F(1, 4) for x0 in (0, 1) for x1 in (0, 1)}
phiR = {(0, 0): (0, 0), (0, 1): (0, 1), (1, 0): (1, 0), (1, 1): (2, 0), (2, 0): (1, 1), (2, 1): (2, 1)}
q2 = {}
for s in phiR:
    s1 = phiR[s]; s2 = phiR[s1]
    k = ((s[0],), s1[0], (s2[0],)); q2[k] = q2.get(k, F(0)) + F(1, 6)
q5 = {}
for x0 in (0, 1):
    sh = F(1, 8) if x0 == 0 else F(-1, 8)
    for x1 in (0, 1):
        for x2 in (0, 1):
            q5[((x0,), x1, (x2,))] = F(1, 4) * ((F(1, 2) + sh) if x2 == 0 else (F(1, 2) - sh))
# tightness-family instance a near-tight probe would need
qt = {}
for a, sg in ((0, 1), (1, -1)):
    d = F(1, 10)
    qt[(a, 1, 0)] = F(1, 2) * (1 + sg * d) / 2
    qt[(a, 1, 1)] = F(1, 2) * (1 - sg * d) / 2
for name, t in (('Q1', q1), ('Q2', q2), ('Q5', q5), ('tight d=1/10', qt)):
    I = cmi_nats(t)
    best = max(h['p0'] * h['delta'] ** 2 for h in hypothesis_pairs(t))
    res = {c: decide(I, c * best) for c in (1, 2, 4)}
    print(f'{name:>13}: c=1 {res[1]:<9} c=2 {res[2]:<9} c=4 {res[4]}')
