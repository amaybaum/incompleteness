"""Post-freeze descriptive diagnostic (not a criterion; cf. RECORD RESULT.md section 7): the reachable operational
states of the linear rule under I3 for one kappa, in the three fiducial coordinates predicted by LEMMA-3A,
    x = P(read v0 = 1) = effect 'o'(1),  y = P(u0 = 1) = 's o'(1),  z = P(u0 XOR v0 = 1) = 'c s o'(1),
each normalized by the preparation's record weight. Exact over Q. Reports the distinct points, whether every
point lies in the octahedron |x-1/2|+|y-1/2|+|z-1/2| <= 1/2 (the six 'one register function known' states as
vertices), and which of the six vertices are reached.

usage: geometry3.py "((0,1),(0,1))" Lp
"""
import sys
from fractions import Fraction as Fr
from analysis3 import protocols, PALPH
from record3_fast import run_all3

kappa = eval(sys.argv[1])
Lp = int(sys.argv[2])
EFF = ['o', 'so', 'cso']
pps = protocols(PALPH, Lp)
J = run_all3([a + b for a in pps for b in [''] + EFF], 'linear', kappa)
pts = {}
for pp in pps:
    base, tot = J[pp]
    k = pp.count('o')
    for r in range(1 << k):
        if base[r] == 0:
            continue
        w = Fr(base[r], tot)
        coord = []
        for e in EFF:
            c, t = J[pp + e]
            coord.append(Fr(c[(r << 1) | 1], t) / w)
        pts.setdefault(tuple(coord), (pp, r))
half = Fr(1, 2)
inside = all(sum(abs(c - half) for c in p) <= half for p in pts)
verts = {tuple(half + (d if i == j else 0) for i in range(3)) for j in range(3) for d in (half, -half)}
reached = sorted(v for v in verts if v in pts)
print(f'GEOMETRY3 {kappa} Lp={Lp}: states {sum(1 for pp in pps for r in range(1 << pp.count("o")) if J[pp][0][r])}, '
      f'distinct points {len(pts)}, all inside octahedron {inside}, vertices reached {len(reached)}/6')
for p in sorted(pts):
    print('  ', tuple(str(c) for c in p), 'e.g.', repr(pts[p][0]), 'record', pts[p][1])
