"""Disc-composite existence problem -- numerical obstruction search (read-only, exploratory; floating point).

For a candidate G in the affine family (frame action, normalization, optionally native relations), score
  slack(G) = min over sampled words W in {G, local rotations} of depth <= 2 applied to sampled product pure states,
             and over sampled effect directions f, of  (Wv f)_0 - |(Wv f)_{1:}|        (>= 0 iff inside the max cone)
together with the residuals |G^2 - I| and (native) |S - G S G S G|. Maximize slack subject to the residuals vanishing
(penalty method, many random restarts). Calibration: the complex CNOT on the Bloch-ball composite (n = 4) must lie in
the family and have slack ~ 0.

A negative best slack over many restarts is EVIDENCE of an obstruction, not a proof; an obstruction is established only
by an exact certificate (a separate step).
"""
import sys, time
import numpy as np
from scipy.optimize import minimize
from disc_cnot_setup import setup, affine_space

rng = np.random.default_rng(42)


def sphere_points(k):
    i = np.arange(k) + 0.5
    phi = np.arccos(1 - 2 * i / k); th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], 1)


def samples(n, m_state, m_eff, m_rot):
    if n == 3:
        a = 2 * np.pi * np.arange(m_state) / m_state
        V = np.stack([np.sin(a), np.cos(a)], 1)
        b = 2 * np.pi * (np.arange(m_eff) + 0.5) / m_eff
        Fd = np.stack([np.sin(b), np.cos(b)], 1)
        rots = []
        for c in 2 * np.pi * np.arange(m_rot) / m_rot:
            R = np.eye(3); R[1:, 1:] = [[np.cos(c), np.sin(c)], [-np.sin(c), np.cos(c)]]; rots.append(R)
    else:
        V = np.vstack([sphere_points(m_state), np.eye(3), -np.eye(3)])
        Fd = sphere_points(m_eff)
        rots = [np.eye(4)]
        for _ in range(m_rot - 1):
            Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
            if np.linalg.det(Q) < 0: Q[:, 0] *= -1
            R = np.eye(4); R[1:, 1:] = Q; rots.append(R)
    S = np.hstack([np.ones((len(V), 1)), V])
    F = np.hstack([np.ones((len(Fd), 1)), Fd])
    prods = np.array([np.kron(s, t) for s in S for t in S])
    Ls = [np.kron(A, B) for A in rots for B in rots]
    return prods, F, Ls


def slacks(vecs, F, n):
    W = vecs.reshape(-1, n, n)
    Wf = np.einsum('kij,fj->kfi', W, F)
    return (Wf[..., 0] - np.linalg.norm(Wf[..., 1:], axis=-1)).reshape(-1)


def all_slacks(G, prods, F, Ls, n, depth2=True):
    v1 = prods @ G.T
    out = [slacks(v1, F, n)]
    if depth2:
        for L in Ls:
            M = G @ L @ G
            out.append(slacks(prods @ M.T, F, n))
    return np.concatenate(out)


def complex_cnot():
    X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex)
    P = [np.eye(2), X, Y, Z]
    C = np.eye(4, dtype=complex)[[0, 1, 3, 2]]
    G = np.zeros((16, 16))
    for i in range(4):
        for j in range(4):
            img = C @ np.kron(P[i], P[j]) @ C.conj().T
            for k in range(4):
                for l in range(4):
                    G[k * 4 + l, i * 4 + j] = np.real(np.trace(img @ np.kron(P[k], P[l]))) / 4
    return G


def run(n, native, restarts, notmode='rot', mu=200.0, tau=0.02, maxiter=200):
    env = setup(n, notmode); d = env['d']; S = env['S']
    g0, B = affine_space(env, native)
    k = len(B)
    ms, me, mr = (8, 16, 4) if n == 3 else (8, 20, 3)
    prods, F, Ls = samples(n, ms, me, mr)
    vprods, vF, vLs = samples(n, 24, 48, 12) if n == 3 else samples(n, 30, 60, 6)
    I = np.eye(d)

    def G_of(lam): return (g0 + lam @ B).reshape(d, d)

    def resid(G):
        r = np.sum((G @ G - I) ** 2)
        if native: r += np.sum((S - G @ S @ G @ S @ G) ** 2)
        return r

    def obj(lam):
        G = G_of(lam)
        s = all_slacks(G, prods, F, Ls, n)
        softmin = -tau * np.log(np.mean(np.exp(-(s - s.min()) / tau))) + s.min()
        return -softmin + mu * resid(G)

    best = None
    for r in range(restarts):
        lam0 = rng.normal(scale=0.5, size=k)
        res = minimize(obj, lam0, method='L-BFGS-B', options={'maxiter': maxiter})
        G = G_of(res.x)
        s = all_slacks(G, vprods, vF, vLs, n).min(); rr = resid(G)   # validated on a denser grid
        rec = (s, rr, res.x)
        if best is None or (rr < 1e-6 and s > best[0]) or (best[1] >= 1e-6 and rr < best[1]):
            best = rec
        print('  restart %2d: min slack %+.4e  residual %.2e' % (r, s, rr), flush=True)
    return best, (g0, B, env, prods, F, Ls)


if __name__ == '__main__':
    t0 = time.time()
    # calibration
    env4 = setup(4); GC = complex_cnot()
    env4 = setup(4, 'rot'); g0, B = affine_space(env4, True)
    lam, *_ = np.linalg.lstsq(B.T, GC.reshape(-1) - g0, rcond=None)
    in_family = np.allclose(g0 + lam @ B, GC.reshape(-1), atol=1e-9)
    prods, F, Ls = samples(4, 14, 30, 5)
    sC = all_slacks(GC, prods, F, Ls, 4).min()
    invC = np.abs(GC @ GC - np.eye(16)).max()
    natC = np.abs(env4['S'] - GC @ env4['S'] @ GC @ env4['S'] @ GC).max()
    print('CALIBRATION complex CNOT on Bloch-ball composite: in native family %s, involution resid %.1e, '
          'S-relation resid %.1e, min slack %+.2e' % (in_family, invC, natC, sC))
    which = sys.argv[1:] or ['4w', '4n-rot', '3w', '3n-refl', '3n-rot']
    for tag in which:
        n = int(tag[0]); native = tag[1] == 'n'; mode = tag.split('-')[1] if '-' in tag else 'rot'
        print('SEARCH n=%d native=%s NOT=%s' % (n, native, mode), flush=True)
        best, _ = run(n, native, restarts=int(8 if n == 4 else 16), notmode=mode)
        print('BEST n=%d native=%s NOT=%s: min slack %+.4e residual %.2e (%.0fs)' % (
            n, native, mode, best[0], best[1], time.time() - t0), flush=True)
        np.save('best_%s.npy' % tag, best[2])
