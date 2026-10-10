"""Depth 1, both directions, no local group, no involution: G and G^-1 both map min into max (evidence only).
Ball d = 3 control: the complex CNOT (in the n = 4 weak family) attains slack 0 in both directions."""
import sys, numpy as np
from scipy.optimize import minimize
from disc_cnot_setup import setup, affine_space
from disc_cnot_search import sphere_points, complex_cnot
rng = np.random.default_rng(3)
def slack(vecs, F, n):
    W = vecs.reshape(-1, n, n); Wf = np.einsum('kij,fj->kfi', W, F)
    return (Wf[..., 0] - np.linalg.norm(Wf[..., 1:], axis=-1)).ravel()
def samp(n, k, m):
    if n == 3:
        a = 2 * np.pi * np.arange(k) / k; b = 2 * np.pi * (np.arange(m) + .5) / m
        S = np.stack([np.ones(k), np.sin(a), np.cos(a)], 1); F = np.stack([np.ones(m), np.sin(b), np.cos(b)], 1)
    else:
        S = np.hstack([np.ones((k, 1)), sphere_points(k)]); F = np.hstack([np.ones((m, 1)), sphere_points(m)])
    return np.array([np.kron(s, t) for s in S for t in S]), F
n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
env = setup(n, 'rot'); g0, B = affine_space(env, False); d = n * n
P, F = samp(n, 10 if n == 3 else 14, 20 if n == 3 else 30); VP, VF = samp(n, 40 if n == 3 else 30, 80 if n == 3 else 60)
def both(G, P, F):
    return min(slack(P @ G.T, F, n).min(), slack(P @ np.linalg.inv(G).T, F, n).min())
if n == 4:
    GC = complex_cnot(); print('control complex CNOT both-direction slack %+.2e' % both(GC, VP, VF))
def obj(lam):
    G = (g0 + lam @ B).reshape(d, d)
    try: Gi = np.linalg.inv(G)
    except np.linalg.LinAlgError: return 1e3
    s = np.concatenate([slack(P @ G.T, F, n), slack(P @ Gi.T, F, n)])
    return -(s.min() - 0.02 * np.log(np.mean(np.exp(-(s - s.min()) / 0.02))))
res_all = []
for r in range(12 if n == 3 else 6):
    res = minimize(obj, rng.normal(scale=0.5, size=len(B)), method='L-BFGS-B', options={'maxiter': 300})
    G = (g0 + res.x @ B).reshape(d, d); res_all.append((both(G, VP, VF), np.linalg.cond(G)))
res_all.sort(key=lambda x: -x[0])
print('n=%d best both-direction slack (slack, cond):' % n, [('%+.3f' % a, '%.1e' % c) for a, c in res_all[:5]], flush=True)
