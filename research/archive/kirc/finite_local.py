"""Finite local symmetry, disc (d = 2): countermodel search (floating point; evidence only). Read-only.
Local group Gamma = C_m (rotations by 2 pi k/m; m even, so NOT = rotation by pi is inside) or D_m (adds z -> -z).
Seek G in the weak family (CNOT on the four corners, normalization) with G^2 = I, maximizing the min max-cone slack
over words G, G L G, G L1 G L2 G (L in Gamma x Gamma) applied to pure products (dense sample) and tested on
product effects. Words beginning or ending in a local map are covered, since local maps preserve min and max."""
import sys, itertools, time
import numpy as np
from scipy.optimize import minimize
from disc_cnot_setup import setup, affine_space
rng = np.random.default_rng(11)

def rotm(c):
    R = np.eye(3); R[1:, 1:] = [[np.cos(c), -np.sin(c)], [np.sin(c), np.cos(c)]]; return R

def group(m, dihedral):
    g = [rotm(2 * np.pi * k / m) for k in range(m)]
    if dihedral:
        F = np.diag([1., 1., -1.]); g += [F @ R for R in g]
    return g

def pts(k, off=0.0):
    a = 2 * np.pi * (np.arange(k) + off) / k
    return np.stack([np.ones(k), np.sin(a), np.cos(a)], 1)

def slack(vecs, F):
    W = vecs.reshape(-1, 3, 3); Wf = np.einsum('kij,fj->kfi', W, F)
    return (Wf[..., 0] - np.linalg.norm(Wf[..., 1:], axis=-1)).ravel()

def words(G, Ls, depth):
    out = [G]
    if depth >= 2: out += [G @ L @ G for L in Ls]
    if depth >= 3: out += [G @ L1 @ G @ L2 @ G for L1 in Ls for L2 in Ls]
    return out

def score(G, Ls, depth, S, F):
    prods = np.array([np.kron(s, t) for s in S for t in S])
    return min(slack(prods @ W.T, F).min() for W in words(G, Ls, depth))

def search(m, dihedral, depth, restarts=12, iters=150):
    env = setup(3, 'rot'); g0, B = affine_space(env, False); I = np.eye(9)
    gam = group(m, dihedral); Ls = [np.kron(a, b) for a in gam for b in gam]
    S, F = pts(8), pts(16, 0.5)
    prods = np.array([np.kron(s, t) for s in S for t in S])
    Wd = lambda G: words(G, Ls, depth)
    def obj(lam):
        G = (g0 + lam @ B).reshape(9, 9)
        s = np.concatenate([slack(prods @ W.T, F) for W in Wd(G)])
        sm = s.min() - 0.02 * np.log(np.mean(np.exp(-(s - s.min()) / 0.02)))
        return -sm + 200 * np.sum((G @ G - I) ** 2)
    best = None
    for r in range(restarts):
        res = minimize(obj, rng.normal(scale=0.5, size=len(B)), method='L-BFGS-B', options={'maxiter': iters})
        G = (g0 + res.x @ B).reshape(9, 9); rr = np.abs(G @ G - I).max()
        sv = score(G, Ls, depth, pts(24), pts(48, 0.5))
        if best is None or (rr < 1e-3 and sv > best[0]): best = (sv, rr, G)
    return best

if __name__ == '__main__':
    t0 = time.time()
    for m, dih, depth in [(2, False, 3), (2, True, 3), (4, False, 3), (4, True, 3), (6, False, 3), (8, False, 2), (12, False, 2)]:
        sv, rr, G = search(m, dih, depth)
        print('%s_%d depth %d: best validated slack %+.4e, involution residual %.1e (%.0fs)' % (
            'D' if dih else 'C', m, depth, sv, rr, time.time() - t0), flush=True)
        np.save('finite_best_%s%d.npy' % ('D' if dih else 'C', m), G)
