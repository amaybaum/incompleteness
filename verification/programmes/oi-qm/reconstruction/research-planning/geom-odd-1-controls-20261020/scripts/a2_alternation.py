"""A2: behaviour of the preflight generator's alternating L1 coupling on eball3 (read-only analysis).

mode replay <seed>: reproduce one start of controls_gen.main exactly (same RandomState, same Cuts, same vertex,
  same couple) and print the residual per round, continuing past the STALL rule up to <rounds>.
mode basin <eps> <trials>: start the alternation at H = G(lam*(R^-1) + eps*xi) (xi seeded Gaussian, projected
  pool-feasible by the same separation), and report the residual sequence: does it return to a gate?
mode fixed: H fixed at R^-1 exactly; one couple step; residual of the result.
"""
import json
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

PRE, WORK, control, mode = sys.argv[1:5]
sys.path.insert(0, PRE)
import controls_gen as cg   # noqa: E402

pool = json.load(open(os.path.join(WORK, 'pool-%s.json' % control)))
prob = cg.Problem(pool)
lam = json.load(open(os.path.join(WORK, 'lam-%s.json' % control)))
lamR = np.array([float(Fr(v)) for v in lam['lamR']])
lamRi = np.array([float(Fr(v)) for v in lam['lamRi']])
I = np.eye(prob.n * prob.n)
resid = lambda a, b: float(np.abs(prob.G(a) @ prob.G(b) - I).max())
dist = lambda a: float(min(np.abs(a - lamR).max(), np.inf))
deadline = time.monotonic() + float(os.environ.get('A2_BUDGET', '500'))


def alternate(lg, lh, cuts, rounds, tag):
    seq = []
    for it in range(rounds):
        lg2 = cg.couple(prob, cuts, prob.G(lh), True, deadline)
        if lg2 is None:
            break
        lh2 = cg.couple(prob, cuts, prob.G(lg2), False, deadline)
        if lh2 is None:
            break
        lg, lh = lg2, lh2
        r = resid(lg, lh)
        seq.append(r)
        print('%s round %d: residual %.3e, |G-R|_max %.3e, |G-G^T...| cuts %d' % (tag, it + 1, r, dist(lg),
                                                                                len(cuts.quads)), flush=True)
        if r < cg.ACCEPT:
            break
    return lg, lh, seq


if mode == 'replay':
    s, rounds = int(sys.argv[5]), int(sys.argv[6])
    rng = np.random.RandomState(1000 + s)
    cuts = cg.Cuts(prob, rng)
    cobj = rng.randn(prob.nv)
    lg = cg.vertex(prob, cuts, cobj, deadline)
    lh = cg.vertex(prob, cuts, -cobj, deadline)
    print('start %d vertices: residual %.3e' % (s, resid(lg, lh)))
    lg, lh, seq = alternate(lg, lh, cuts, rounds, 's%d' % s)
    G = prob.G(lg)
    # is the stalled point a gate in disguise? report singular values and the pool-A minimum of G and of G^-1
    sv = np.linalg.svd(G, compute_uv=False)
    print('stalled G: sigma_min %.3e sigma_max %.3e; pool-A min of G %.3e; pool-A min of G^-1 %.3e'
          % (sv.min(), sv.max(), prob.values(G).min(), prob.values(np.linalg.inv(G)).min()))
elif mode == 'basin':
    eps, trials = float(sys.argv[5]), int(sys.argv[6])
    for t in range(trials):
        rng = np.random.RandomState(7000 + t)
        cuts = cg.Cuts(prob, rng)
        xi = rng.randn(prob.nv)
        lh = lamRi + eps * xi / np.abs(xi).max()
        lg = lamR.copy()
        print('trial %d eps %g: initial residual %.3e' % (t, eps, resid(lg, lh)))
        alternate(lg, lh, cuts, int(os.environ.get('A2_ROUNDS', '30')), 'b%d' % t)
elif mode == 'fixed':
    rng = np.random.RandomState(1)
    cuts = cg.Cuts(prob, rng)
    lg = cg.couple(prob, cuts, prob.G(lamRi), True, deadline)
    print('H = R^-1 fixed: residual of argmin G: %.3e; |G - R|_max %.3e' % (resid(lg, lamRi), dist(lg)))
