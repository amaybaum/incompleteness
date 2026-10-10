"""Hidden-assumption audit: the theorem uses ONE involution N on both factors.  Countercontrol with N_A != N_B at d = 5.
Basis per factor: 0 u, 1 x, 2 y, 3 w1, 4 w2, 5 z.  Corners u +- z.
 N_B (target) = rotation fixing x, flipping y, w1, w2, z   (p_B = 1, q_B = 3)
 N_A (control) = reflection fixing x, w1, flipping y, w2, z (p_A = 2, q_A = 2)
 G: controlled-N_B on the classical control part; c (x) t -> c (x) S t on E+(N_B) = {u, x} (u <-> x);
    c (x) t -> J c (x) K t on V-(N_B) = {y, w1, w2, z}, with J an orthogonal complex structure on T_A anticommuting
    with N_A (x <-> y, w1 <-> w2) and K an orthogonal complex structure on V-(N_B).
Relations checked exactly (integer matrices); positivity is exact by the J/K reduction lemma (BALL5-FINITE.md sec. 1:
the value depends on (a.s, a.Js) and (b.t, b.Kt) through discs of the Bloch radii for ANY orthogonal complex structures
J, K), and cross-checked by block-coordinate minimization."""
import numpy as np
n = 6; D = n * n; u, x, y, w1, w2, z = range(6); e = np.eye(n)
NA = np.diag([1, 1, -1, 1, -1, -1.]); NB = np.diag([1, 1, -1, -1, -1, -1.])
J = np.zeros((n, n)); J[y, x] = 1; J[x, y] = -1; J[w2, w1] = 1; J[w1, w2] = -1          # J x = y, J y = -x, J w1 = w2, J w2 = -w1
K = np.zeros((n, n)); K[z, y] = 1; K[y, z] = -1; K[w2, w1] = 1; K[w1, w2] = -1          # K y = z, K z = -y, K w1 = w2, K w2 = -w1
S = np.zeros((n, n)); S[x, u] = 1; S[u, x] = 1
TA = [x, y, w1, w2]; Ep = [u, x]; Vm = [y, w1, w2, z]
k0, k1 = e[u] + e[z], e[u] - e[z]
G = np.zeros((D, D))
for j in range(n):
    G[:, u * n + j] = (np.kron(k0, e[j]) + np.kron(k1, NB @ e[j])) / 2
    G[:, z * n + j] = (np.kron(k0, e[j]) - np.kron(k1, NB @ e[j])) / 2
for c in TA:
    for j in Ep: G[:, c * n + j] = np.kron(e[c], S @ e[j])
    for j in Vm: G[:, c * n + j] = np.kron(J @ e[c], K @ e[j])
I = np.eye(D); ks = [k0, k1]
print('frame', all(np.allclose(G @ np.kron(ks[a], ks[b]), np.kron(ks[a], ks[a ^ b])) for a in (0, 1) for b in (0, 1)))
print('invertible (G^2 = I)', np.allclose(G @ G, I))
print('J, K orthogonal complex structures on T_A, V-:', np.allclose(J[np.ix_(TA, TA)] @ J[np.ix_(TA, TA)], -np.eye(4)),
      np.allclose(K[np.ix_(Vm, Vm)] @ K[np.ix_(Vm, Vm)], -np.eye(4)))
print('J anticommutes with N_A on T_A:', np.allclose(NA @ J @ NA, -J))
print('Rt with N_B: (I(x)N_B) G (I(x)N_B) = G:', np.allclose(np.kron(e, NB) @ G @ np.kron(e, NB), G))
print('Rc with N_A on control, N_B on target: (N_A(x)I) G (N_A(x)I) = (I(x)N_B) G:',
      np.allclose(np.kron(NA, e) @ G @ np.kron(NA, e), np.kron(e, NB) @ G))
print('Rc with the SAME N (N_B on both):', np.allclose(np.kron(NB, e) @ G @ np.kron(NB, e), np.kron(e, NB) @ G))
rng = np.random.default_rng(1)
def minval(M, starts=200, iters=60):
    T = M.reshape(n, n, n, n); best = np.inf; subs = 'ijkl'
    for _ in range(starts):
        v = [rng.normal(size=n - 1) for _ in range(4)]; v = [w / np.linalg.norm(w) for w in v]
        for _ in range(iters):
            for blk in range(4):
                vec = [np.concatenate([[1.], w]) for w in v]
                ex = 'ijkl,' + ','.join(s for b, s in enumerate(subs) if b != blk) + '->' + subs[blk]
                cc = np.einsum(ex, T, *[vec[b] for b in range(4) if b != blk])[1:]
                if np.linalg.norm(cc) > 1e-15: v[blk] = -cc / np.linalg.norm(cc)
        vec = [np.concatenate([[1.], w]) for w in v]; best = min(best, np.einsum('ijkl,i,j,k,l->', T, *vec))
    return best
print('positivity cross-check: min over unit s,t,f,g of (f(x)g)(G(s(x)t)) ~ %+.2e (and for G^-1 = G)' % minval(G))
