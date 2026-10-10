"""d = 7 candidate built from the algebraic solution pattern, then positivity (block-coordinate descent; evidence).
Local basis: 0 u, 1 x, 2 v2, 3 v3 (T+ = x,v2,v3), 4 y1, 5 y2, 6 y3 (T-), 7 z. Corners u +- z."""
import numpy as np, itertools
n = 8; D = n * n
u, x, v2, v3, y1, y2, y3, z = range(8)
N = np.diag([1, 1, 1, 1, -1, -1, -1, -1.])
M0 = np.diag([1, 1, -1, 1, 1, 1, 1, 1.])            # twist on V+: v2 -> -v2
M1 = N @ M0
TA = [x, v2, v3, y1, y2, y3]
Jm = {x: (1, y1), y1: (-1, x), v2: (1, y2), y2: (-1, v2), v3: (1, y3), y3: (-1, v3)}
Km = {y1: (1, z), z: (-1, y1), y2: (1, y3), y3: (-1, y2)}
Ep = {u: (1, x), x: (1, u), v2: (1, v3), v3: (1, v2)}
e = np.eye(n)
def build(Ep=Ep, Km=Km, Jm=Jm, M0=M0):
    M1 = N @ M0
    G = np.zeros((D, D))
    k0, k1 = e[u] + e[z], e[u] - e[z]
    for j in range(n):
        # G(u(x)e_j) = (|0>(x)M0 e_j + |1>(x)M1 e_j)/2 ; G(z(x)e_j) = (|0>(x)M0 e_j - |1>(x)M1 e_j)/2
        G[:, u * n + j] = (np.kron(k0, M0[:, j]) + np.kron(k1, M1[:, j])) / 2
        G[:, z * n + j] = (np.kron(k0, M0[:, j]) - np.kron(k1, M1[:, j])) / 2
    for c in TA:
        for j in (u, x, v2, v3):
            s, l = Ep[j]; G[c * n + l, c * n + j] = s
        for j in (y1, y2, y3, z):
            s1, k = Jm[c]; s2, l = Km[j]; G[k * n + l, c * n + j] = s1 * s2
    return G
G = build()
ks = [e[u] + e[z], e[u] - e[z]]
I = np.eye(D)
L = lambda A, B: np.kron(A, B)
print('frame', all(np.allclose(G @ np.kron(ks[a], ks[b]), np.kron(ks[a], ks[a ^ b])) for a in (0, 1) for b in (0, 1)),
      '| involution', np.allclose(G @ G, I), '| normalization', np.allclose(G.T[:, 0], I[0]),
      '| target rel', np.allclose(L(e, N) @ G @ L(e, N), G), '| control rel', np.allclose(L(N, e) @ G @ L(N, e), L(e, N) @ G))
rng = np.random.default_rng(7)
def min_value(M, starts=300, iters=80):
    T = M.reshape(n, n, n, n); best = np.inf; arg = None
    subs = 'ijkl'
    for _ in range(starts):
        v = [rng.normal(size=n - 1) for _ in range(4)]; v = [w / np.linalg.norm(w) for w in v]
        for _ in range(iters):
            for blk in range(4):
                vec = [np.concatenate([[1.], w]) for w in v]
                expr = 'ijkl,' + ','.join(s for b, s in enumerate(subs) if b != blk) + '->' + subs[blk]
                c = np.einsum(expr, T, *[vec[b] for b in range(4) if b != blk])[1:]
                if np.linalg.norm(c) > 1e-15: v[blk] = -c / np.linalg.norm(c)
        vec = [np.concatenate([[1.], w]) for w in v]
        val = np.einsum('ijkl,i,j,k,l->', T, *vec)
        if val < best: best, arg = val, v
    return best, arg
if __name__ == '__main__':
    v, arg = min_value(G); print('d=7 candidate: min (f(x)g)(G(s(x)t)) ~ %+.4f' % v)
    np.save('ball7_arg.npy', np.array(arg))
