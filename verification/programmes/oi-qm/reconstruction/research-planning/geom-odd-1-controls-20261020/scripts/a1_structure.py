"""A1: exact structure of the preflight's search space at e8ac54b5 (read-only analysis, design note).

For each control: dim F; exact coordinates lam* of the reference gate R and of R^-1 in the generator's
parametrisation G = G0 + sum lam_k B_k; whether R^-1 lies in F; R^2 == 1; max |lam*| against BOX; exact
posFwd/posInv of R on pool A only (generator's view)."""
import json
import os
import sys
from fractions import Fraction as Fr

PRE = sys.argv[1]
WORK = sys.argv[2]
sys.path.insert(0, PRE)
import controls_gen as cg      # noqa: E402
import controls_verify as cv   # noqa: E402


def coords(prob, M):
    """exact lam with G0 + sum lam_k B_k == M on the free pattern, or None; and whether M vanishes off the pattern"""
    nn = prob.n * prob.n
    pos = {pq: i for i, pq in enumerate(prob.free)}
    off = all(M[p][q] == 0 for p in range(nn) for q in range(nn) if (p, q) not in pos)
    g = [M[p][q] for (p, q) in prob.free]
    # basis vectors are unit on their free column fc; lam_k = g[fc_k] - part[fc_k]
    lam = []
    for b in prob.basis_exact:
        fc = next(i for i, v in enumerate(b) if v == 1 and all(
            bb[i] == 0 for bb in prob.basis_exact if bb is not b))
        lam.append(g[fc] - prob.part_exact[fc])
    rec = [prob.part_exact[i] + sum(l * b[i] for l, b in zip(lam, prob.basis_exact) if l) for i in range(len(g))]
    return (lam if rec == g and off else None), off


for control in ('eball3', 'omegah'):
    pool = json.load(open(os.path.join(WORK, 'pool-%s.json' % control)))
    prob = cg.Problem(pool)
    body = cv.Body(control)
    R = body.reference
    Ri = cv.inverse(R)
    n2 = body.n * body.n
    lamR, offR = coords(prob, R)
    lamRi, offRi = coords(prob, Ri)
    sq = cv.mat_mul(R, R) == cv.eye(n2)
    print('== %s: D %d, dim F %d, free entries %d of %d' % (control, body.D, prob.nv, len(prob.free), n2 * n2))
    print('  R in F (exact coords found): %s; R^-1 in F: %s; R^2 == 1: %s' % (lamR is not None, lamRi is not None, sq))
    if lamR is not None:
        print('  max|lam*(R)| = %s (BOX %s); nonzero coords %d; distinct values %s'
              % (max(abs(v) for v in lamR), cg.BOX, sum(1 for v in lamR if v), sorted(set(map(str, lamR)))[:12]))
    mf, nf = cv.positivity(body, R, pools=('A',))
    mi, ni = cv.positivity(body, Ri, pools=('A',))
    print('  pool A exact: posFwd min %s (neg %d), posInv min %s (neg %d)' % (mf, nf, mi, ni))
    # how many pool-A quadruples are tight (value 0) for R: degeneracy of the reference vertex
    import numpy as np
    vals = prob.values(np.array([[float(v) for v in r] for r in R]))
    print('  pool-A quadruples %d; tight (|v|<1e-12) for R: %d; for R^-1: %d'
          % (vals.size, int((abs(vals) < 1e-12).sum()),
             int((abs(prob.values(np.array([[float(v) for v in r] for r in Ri]))) < 1e-12).sum())))
    json.dump({'lamR': [str(v) for v in lamR] if lamR else None,
               'lamRi': [str(v) for v in lamRi] if lamRi else None},
              open(os.path.join(WORK, 'lam-%s.json' % control), 'w'))
