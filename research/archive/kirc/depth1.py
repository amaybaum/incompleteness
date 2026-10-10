"""Depth-1 only, no local group: does any G in the weak disc family satisfy G(min) <= max with G^2 = I? (evidence)
Control: the non-invertible measure-control-and-flip map M satisfies the frame and depth-1 containment (slack >= 0)."""
import numpy as np
from finite_local import pts, slack, rng
from disc_cnot_setup import setup, affine_space
from scipy.optimize import minimize
env = setup(3, 'rot'); g0, B = affine_space(env, False); I = np.eye(9)
S, F = pts(12), pts(24, 0.5); prods = np.array([np.kron(s, t) for s in S for t in S])
# control
k = [np.array([1, 0, 1.]), np.array([1, 0, -1.])]; e = [np.array([1, 0, 1.]) / 2, np.array([1, 0, -1.]) / 2]
NOT = np.diag([1., -1, -1])
M = sum(np.kron(np.outer(k[a], e[a]), np.linalg.matrix_power(NOT, a)) for a in (0, 1))
ok = all(np.allclose(M @ np.kron(k[a], k[b]), np.kron(k[a], k[a ^ b])) for a in (0, 1) for b in (0, 1))
print('control measure-and-flip: frame %s, depth-1 slack %+.3e, rank %d' % (ok, slack(prods @ M.T, F).min(), np.linalg.matrix_rank(M)))
for mu, tag in [(0.0, 'no involution'), (200.0, 'G^2 = I penalty')]:
    def obj(lam):
        G = (g0 + lam @ B).reshape(9, 9); s = slack(prods @ G.T, F)
        return -(s.min() - 0.02 * np.log(np.mean(np.exp(-(s - s.min()) / 0.02)))) + mu * np.sum((G @ G - I) ** 2)
    best = []
    for r in range(16):
        res = minimize(obj, rng.normal(scale=0.5, size=len(B)), method='L-BFGS-B', options={'maxiter': 300})
        G = (g0 + res.x @ B).reshape(9, 9)
        best.append((slack(np.array([np.kron(s, t) for s in pts(40) for t in pts(40)]) @ G.T, pts(80, .5)).min(),
                     np.abs(G @ G - I).max(), abs(np.linalg.det(G))))
    best.sort(key=lambda x: (x[1] > 1e-3, -x[0]))
    print(tag, 'top (slack, inv resid, |det|):', [('%+.3f' % a, '%.1e' % b, '%.2e' % c) for a, b, c in best[:4]], flush=True)
