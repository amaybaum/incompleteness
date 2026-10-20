"""A10: candidate repair, joint sequential linear programming (SLP) with a trust region, on eball3 (design probe).

Instead of alternating G and H, each step solves ONE LP in (lamG, lamH):
  min |G_k H_k - 1 + dG H_k + G_k dH|_1   s.t.  G, H pool-A positive (constraint generation),  |d| <= rho,
accepts the step if the true residual max|G H - 1| decreases (rho grows), else shrinks rho.
mode basin <eps> <trials>: start at (R, R^-1 + eps*xi)   -> does SLP return to an exact gate?
mode random <starts> <budget>: the generator's own random vertex starts (seeds 1000+s) -> residual reached.
Float only; any converged point would still go to the exact verifier.  Nothing here is a verdict."""
import json
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog

PRE, WORK, mode = sys.argv[1:4]
sys.path.insert(0, PRE)
import controls_gen as cg   # noqa: E402

control = os.environ.get('A10_CONTROL', 'eball3')
pool = json.load(open(os.path.join(WORK, 'pool-%s.json' % control)))
prob = cg.Problem(pool)
lam = json.load(open(os.path.join(WORK, 'lam-%s.json' % control)))
lamR = np.array([float(Fr(v)) for v in lam['lamR']])
lamRi = np.array([float(Fr(v)) for v in lam['lamRi']])
nv, nn = prob.nv, prob.n * prob.n
I = np.eye(nn)
res_of = lambda a, b: float(np.abs(prob.G(a) @ prob.G(b) - I).max())


def slp(lg, lh, cutsG, cutsH, deadline, iters=60, rho=0.5, tag=''):
    for it in range(iters):
        G, H = prob.G(lg), prob.G(lh)
        r0 = (G @ H - I).reshape(-1)
        JG = np.einsum('kij,jl->kil', prob.Bm, H).reshape(nv, -1).T      # d(GH)/d lamG
        JH = np.einsum('ij,kjl->kil', G, prob.Bm).reshape(nv, -1).T      # d(GH)/d lamH
        J = sp.csr_matrix(np.hstack([JG, JH]))
        m = J.shape[0]
        Im = sp.identity(m, format='csr')
        while True:
            # variables: dG, dH (nv each), t (m) ; min sum t ; -t <= r0 + J d <= t ; posFwd rows for G, H
            c = np.concatenate([np.zeros(2 * nv), np.ones(m)])
            AG = sp.hstack([sp.csr_matrix(-cutsG.R), sp.csr_matrix((len(cutsG.C), nv + m))])
            AH = sp.hstack([sp.csr_matrix((len(cutsH.C), nv)), sp.csr_matrix(-cutsH.R), sp.csr_matrix((len(cutsH.C), m))])
            A = sp.vstack([sp.hstack([J, -Im]), sp.hstack([-J, -Im]), AG, AH], format='csr')
            b = np.concatenate([-r0, r0, cutsG.C + cutsG.R @ lg, cutsH.C + cutsH.R @ lh])
            bounds = ([(max(-rho, -cg.BOX - v), min(rho, cg.BOX - v)) for v in lg]
                      + [(max(-rho, -cg.BOX - v), min(rho, cg.BOX - v)) for v in lh] + [(0, None)] * m)
            left = deadline - time.monotonic()
            if left < 3:
                return lg, lh
            out = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs', options={'time_limit': left - 1})
            if out.status != 0:
                return lg, lh
            ng, nh = lg + out.x[:nv], lh + out.x[nv:2 * nv]
            more = cutsG.separate(ng)
            more = cutsH.separate(nh) or more
            if not more:
                break
        r_old, r_new = res_of(lg, lh), res_of(ng, nh)
        if r_new < r_old:
            lg, lh = ng, nh
            rho = min(2 * rho, 4.0)
        else:
            rho /= 4
        print('%s it %d: residual %.3e (rho %.2e), |G-R| %.3e' % (tag, it, res_of(lg, lh), rho,
                                                                np.abs(lg - lamR).max()), flush=True)
        if res_of(lg, lh) < 1e-12 or rho < 1e-12:
            break
    return lg, lh


if mode == 'basin':
    eps, trials = float(sys.argv[4]), int(sys.argv[5])
    for t in range(trials):
        rng = np.random.RandomState(7000 + t)
        cG, cH = cg.Cuts(prob, rng), cg.Cuts(prob, rng)
        xi = rng.randn(nv)
        lh = lamRi + eps * xi / np.abs(xi).max()
        xi2 = rng.randn(nv)
        lg = lamR + (eps * xi2 / np.abs(xi2).max() if os.environ.get('A10_BOTH') else 0)
        print('trial %d eps %g: initial residual %.3e' % (t, eps, res_of(lg, lh)))
        slp(lg, lh, cG, cH, time.monotonic() + 120, tag='b%d' % t)
elif mode == 'random':
    starts, budget = int(sys.argv[4]), float(sys.argv[5])
    only = os.environ.get('A10_ONLY')
    for s in ([int(only)] if only else range(starts)):
        rng = np.random.RandomState(1000 + s)
        cuts = cg.Cuts(prob, rng)
        cobj = rng.randn(nv)
        dl = time.monotonic() + budget
        lg = cg.vertex(prob, cuts, cobj, dl)
        lh = cg.vertex(prob, cuts, -cobj, dl)
        cH = cg.Cuts(prob, np.random.RandomState(5000 + s))
        print('start %d: vertex residual %.3e' % (s, res_of(lg, lh)))
        lg, lh = slp(lg, lh, cuts, cH, dl, iters=200, tag='s%d' % s)
        print('start %d END residual %.3e, |G-R| %.3e' % (s, res_of(lg, lh), np.abs(lg - lamR).max()), flush=True)
        if res_of(lg, lh) < cg.ACCEPT:
            G = cg.exactify(prob, lg)
            outp = os.path.join(WORK, 'slp-candidate-%s-s%d.json' % (control, s))
            json.dump({'control': control, 'status': 'candidate' if G else 'exactify-failed',
                       'G': None if G is None else [[str(v) for v in r] for r in G]}, open(outp, 'w'))
            print('start %d: exactified %s -> %s' % (s, G is not None, outp), flush=True)
