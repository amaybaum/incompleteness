"""Diagnostic: shape of the linear rule's Level-2 operational state space (rank 3 => affine dim 2) for one
interface, exact. States = normalized preparation columns, in coordinates of two effects completing the unit."""
import sys
from fractions import Fraction as Fr
from record_fast import run_all
from record_analysis2 import protocols
from rankbasis import reduce_basis

def hull(pts):
    pts = sorted(set(pts))
    def cross(o, a, b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0: lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0: up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]

def states(rule, kappa, L):
    pps, pes = protocols('oifs', L), protocols('oimfs', L)
    J = run_all([a + b for a in pps for b in pes], rule, kappa)
    effs = [(pe, re) for pe in pes for re in range(1 << pe.count('o'))]
    cols = []
    for pp in pps:
        base, tot = J[pp]
        k = pp.count('o')
        for r in range(1 << k):
            if base[r] == 0: continue
            pr = Fr(base[r], tot)
            col = []
            for (pe, re) in effs:
                c, t = J[pp + pe]
                col.append(Fr(c[(r << pe.count('o')) | re], t) / pr)
            cols.append((pp, r, col))
    # effect rows restricted to states; pick a row basis containing the unit
    rows = [[c[2][i] for c in cols] for i in range(len(effs))]
    basis, chosen = [], []
    for i, row in enumerate(rows):
        if len(reduce_basis(basis + [row])) > len(basis):
            basis.append(row); chosen.append(effs[i])
    return cols, chosen, basis

if __name__ == '__main__':
    kappa = eval(sys.argv[1]); L = int(sys.argv[2])
    cols, chosen, basis = states('linear', kappa, L)
    print('rank', len(chosen), 'basis effects', chosen)
    assert len(chosen) == 3 and chosen[0] == ('', 0)
    pts = [(basis[1][j], basis[2][j]) for j in range(len(cols))]
    H = hull(pts)
    print('states', len(cols), 'distinct points', len(set(pts)), 'hull vertices', len(H))
    for v in H:
        ex = next(c for j, c in enumerate(cols) if pts[j] == v)
        print('  ', v, 'e.g. prep', repr(ex[0]), 'record', ex[1])
