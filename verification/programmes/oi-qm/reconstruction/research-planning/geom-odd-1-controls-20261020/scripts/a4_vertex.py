"""A4: is the reference gate a vertex of the generator's posFwd polytope P_A = {lam : G(lam) pool-A positive}?

Reports, for the G-side tight rows only (each linear in lam): float rank; exact rank modulo two primes on the exact
rows (rank_p <= rank_Q, so rank_p == dim F certifies the vertex property exactly); and, for eball3, how often the
generator's own vertex step (random Gaussian objective, box +-8, full pool-A constraint set) returns R, and the normal
cone test: is a symmetric-group-invariant objective enough?"""
import json
import os
import sys
from fractions import Fraction as Fr
from math import gcd

import numpy as np
from scipy.optimize import linprog

PRE, WORK, control = sys.argv[1:4]
TRIALS = int(sys.argv[4]) if len(sys.argv) > 4 else 0
sys.path.insert(0, PRE)
import controls_gen as cg       # noqa: E402
import controls_verify as cv    # noqa: E402

body = cv.Body(control)
pool = json.load(open(os.path.join(WORK, 'pool-%s.json' % control)))
prob = cg.Problem(pool)
R = body.reference
Rf = np.array([[float(v) for v in r] for r in R])
vals = prob.values(Rf)
tG = [tuple(int(v) for v in q) for q in np.argwhere(np.abs(vals) < 1e-12)]
rows, consts = prob.rows(tG)
key = {}
for r, c0 in zip(rows, consts):
    m = np.abs(r).max()
    if m < 1e-12:
        continue
    key.setdefault(tuple(np.round(r / m, 9)), (r, c0))
U = np.array([v[0] for v in key.values()])
sv = np.linalg.svd(U, compute_uv=False)
print('== %s: dim F %d; G-side tight quadruples %d; distinct rows %d; float rank %d'
      % (control, prob.nv, len(tG), len(U), int((sv > 1e-9 * sv.max()).sum())))

statesX = body.pools['A']['states']
effX = body.pools['A']['effects']
homx = [[Fr(1)] + list(x) for x in statesX]
nn = prob.n * prob.n
fpl, fql = list(prob.fp), list(prob.fq)
# exact rows on a subset chosen by float pivoting (enough to certify rank), to keep Fraction work bounded
Q, Rr, piv = None, None, None
import scipy.linalg as sla
_, _, P = sla.qr(U.T, pivoting=True, mode='economic')
sel_keys = list(key.keys())
chosen = [tG[[i for i, (r, c0) in enumerate(zip(rows, consts))
              if np.abs(r).max() > 1e-12 and tuple(np.round(r / np.abs(r).max(), 9)) == sel_keys[j]][0]]
          for j in P[:prob.nv]]


def exrow(x, y, a, b):
    ef = [p * q for p in effX[a] for q in effX[b]]
    w = [p * q for p in homx[x] for q in homx[y]]
    d = [ef[p] * w[q] for p, q in zip(fpl, fql)]
    return [sum((di * bk[i] for i, di in enumerate(d) if di and bk[i]), Fr(0)) for bk in prob.basis_exact]


def rank_mod(rows, p):
    M = [[v % p for v in r] for r in rows]
    rk = 0
    for c in range(len(M[0])):
        pv = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if pv is None:
            continue
        M[rk], M[pv] = M[pv], M[rk]
        inv = pow(M[rk][c], p - 2, p)
        M[rk] = [v * inv % p for v in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]:
                f = M[i][c]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk


ER = [exrow(*q) for q in chosen]
IR = []
for r in ER:
    L = 1
    for f in r:
        L = L * f.denominator // gcd(L, f.denominator)
    IR.append([int(f * L) for f in r])
for p in (2147483647, 1000000007):
    print('exact rank mod %d of %d selected tight rows: %d (dim F %d)' % (p, len(IR), rank_mod(IR, p), prob.nv))

if TRIALS:
    allq = [tuple(int(v) for v in np.unravel_index(i, vals.shape)) for i in range(vals.size)]
    Ar, Ac = prob.rows(allq)
    lamR = np.array([float(Fr(v)) for v in json.load(open(os.path.join(WORK, 'lam-%s.json' % control)))['lamR']])
    hits = 0
    dists = []
    for s in range(TRIALS):
        rng = np.random.RandomState(1000 + s)
        rng.choice(vals.size, size=min(cg.INIT, vals.size), replace=False)    # same draw order as Cuts
        cobj = rng.randn(prob.nv)
        res = linprog(cobj, A_ub=-Ar, b_ub=Ac, bounds=[(-cg.BOX, cg.BOX)] * prob.nv, method='highs')
        d = np.abs(res.x - lamR).max()
        dists.append(d)
        hits += d < 1e-7
    print('random-objective vertices of the full pool-A polytope (box %g): %d of %d equal R; distance min %.3f median %.3f'
          % (cg.BOX, hits, TRIALS, min(dists), float(np.median(dists))))
    # normal-cone objective: minus the sum of R's tight rows (a strictly interior normal); returns R?
    cR = U.sum(axis=0)
    res = linprog(cR, A_ub=-Ar, b_ub=Ac, bounds=[(-cg.BOX, cg.BOX)] * prob.nv, method='highs')
    print('objective = sum of R tight rows (minimised): vertex distance to R %.3e' % np.abs(res.x - lamR).max())
