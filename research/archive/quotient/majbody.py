"""Geometry of the majority rule's W-invariant passive quotient (effects <= 6): the image of the pasts <= 8 under
the four non-unit coordinates. Is it a classical simplex (all points nonnegative combinations of 4 vertices)?"""
import sys
from fractions import Fraction as Fr
from itertools import product
sys.path.insert(0, '.'); sys.path.insert(0, '../rank')
from lattice_rank import record_counts
from oistage_helpers import rank
rule, n = 'majority', 8
arr = record_counts(n, rule).reshape([2] * (2 * n))
def val(h, f):
    sl = [slice(None)] * (2 * n)
    for i, b in enumerate(h): sl[n - len(h) + i] = b
    for i, b in enumerate(f): sl[n + i] = b
    return int(arr[tuple(sl)].sum())
pasts = [h for l in range(n + 1) for h in product((0, 1), repeat=l) if val(h, ()) > 0]
def p(h, f): return Fr(val(h, f), val(h, ()))
# coordinates: q1 = [001000]-[00100] (= -[001001]... ), q2 = [010010], q3 = [100100], q4 = sum_k [1^k 0], k=0..5
def q(h):
    return (p(h, (0,0,1,0,0,0)) - p(h, (0,0,1,0,0)), p(h, (0,1,0,0,1,0)), p(h, (1,0,0,1,0,0)),
            sum((p(h, tuple([1]*k + [0])) for k in range(6)), Fr(0)))
pts = {q(h) for h in pasts}
print('MAJBODY distinct points:', len(pts), ' affine dim:', rank([[1] + list(x) for x in pts]) - 1)
# the three frozen phases and the all-ones frozen pattern as candidate vertices; also "unfrozen" 
# check: are all points in the convex hull of the extreme candidates? use exact LP-free test: express each point
# as a combination of the vertices found by brute force among points (vertex = not a convex combination of others)
import itertools
P = sorted(pts)
print('MAJBODY sample points (q1,q2,q3,q4):', [tuple(str(c) for c in x) for x in P[:6]], '...')
print('MAJBODY coordinate ranges:', [(str(min(x[i] for x in P)), str(max(x[i] for x in P))) for i in range(4)])
# extreme points (float LP, evidence level): a point is extreme iff it is not a convex combination of the others
import numpy as np
from scipy.optimize import linprog
Pf = np.array([[float(c) for c in x] for x in P])
ext = []
for i in range(len(Pf)):
    others = np.delete(Pf, i, axis=0)
    A_eq = np.vstack([others.T, np.ones(len(others))])
    b_eq = np.append(Pf[i], 1.0)
    res = linprog(np.zeros(len(others)), A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='highs')
    if res.status != 0:
        ext.append(P[i])
print('MAJBODY extreme points (float LP):', len(ext))
for x in ext:
    print('   ', tuple(str(c) for c in x))
