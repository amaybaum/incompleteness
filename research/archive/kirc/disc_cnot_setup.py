"""Disc-composite existence problem -- setup and constraint algebra (read-only, exploratory).

Local system: the normalized base of the Lorentz cone L_n in R^n with coordinates (t, v), v in R^{n-1}:
  n = 3: the disc (rebit), v = (x, z);   n = 4: the Bloch ball (control), v = (x, y, z).
Pairing <e, s> = e . s (L_n is self-dual). Pure states s(v) = (1, v), |v| = 1; extremal effects e(w) = (1, w)/2.
Composite: V = R^n (x) R^n (local tomography built in: the joint space is spanned by products); a vector is an n x n
matrix W; product s (x) s' <-> outer(s, s').
Max tensor cone test: W in L_n (x)_max L_n iff for every effect direction f, W f lies in L_n, i.e.
  (W f)_0 >= |(W f)_{1:}|  for all f = (1, w), |w| = 1.
Classical frame: |0> = (1, 0.., 1), |1> = (1, 0.., -1) on the last coordinate (z).
Native generators on the frame: NOT = reflection z -> -z (a symmetry of L_n); SWAP of tensor factors.
G: any linear map on V with
  (F) G c_ab = c_{a, a xor b} on the four classical products,
  (U) normalization: (u (x) u)^T G = (u (x) u)^T, u = (1, 0, ..),
  (I) G^2 = I (globally),
  native-faithful (N): (I (x) NOT) G (I (x) NOT) = G;  (NOT (x) I) G (NOT (x) I) = (I (x) NOT) G;  S = G (S G S) G.
"""
import numpy as np
from numpy.linalg import matrix_rank, svd

np.set_printoptions(precision=4, suppress=True, linewidth=160)


def setup(n, notmode='refl'):
    d = n * n
    u = np.zeros(n); u[0] = 1
    k0 = np.zeros(n); k0[0] = 1; k0[-1] = 1
    k1 = np.zeros(n); k1[0] = 1; k1[-1] = -1
    ket = [k0, k1]
    c = {(a, b): np.kron(ket[a], ket[b]) for a in (0, 1) for b in (0, 1)}
    NOT = np.eye(n)
    if notmode == 'refl':          # z -> -z (real QM's X on the disc; an improper map)
        NOT[-1, -1] = -1
    else:                          # rotation by pi through the first transverse axis: v -> (v1, -v2, .., -vz)
        NOT[2:, 2:] *= -1
        if n == 3: NOT[1, 1] = -1  # disc: rotation by pi of the (x, z) plane
    I = np.eye(n)
    S = np.zeros((d, d))
    for i in range(n):
        for j in range(n):
            S[j * n + i, i * n + j] = 1
    XI, IX = np.kron(NOT, I), np.kron(I, NOT)
    u2 = np.kron(u, u)
    return dict(n=n, d=d, u2=u2, c=c, XI=XI, IX=IX, S=S)


def linear_constraints(env, native):
    """rows of A with A vec(G) = b; vec(G) row-major (G[i,j] -> i*d + j)"""
    d = env['d']; rows, rhs = [], []

    def add(Mcoef, val):
        rows.append(Mcoef.reshape(-1)); rhs.append(val)
    for (a, b), v in env['c'].items():                      # (F)  G v = w
        w = env['c'][(a, a ^ b)]
        for i in range(d):
            M = np.zeros((d, d)); M[i, :] = v; add(M, w[i])
    for j in range(d):                                        # (U)  sum_i u2_i G_ij = u2_j
        M = np.zeros((d, d)); M[:, j] = env['u2']; add(M, env['u2'][j])
    if native:
        IX, XI = env['IX'], env['XI']
        for i in range(d):                                    # IX G IX - G = 0  and  XI G XI - IX G = 0
            for j in range(d):
                M1 = np.outer(IX[i, :], IX[:, j]); M1[i, j] -= 1; add(M1, 0.0)
                M2 = np.outer(XI[i, :], XI[:, j]) - np.outer(IX[i, :], np.eye(d)[:, j]); add(M2, 0.0)
    A = np.array(rows); b = np.array(rhs)
    return A, b


def affine_space(env, native):
    A, b = linear_constraints(env, native)
    g0, *_ = np.linalg.lstsq(A, b, rcond=None)
    assert np.allclose(A @ g0, b), 'linear constraints inconsistent'
    U, s, Vt = svd(A)
    r = int((s > 1e-9).sum())
    basis = Vt[r:]                                            # nullspace basis
    return g0, basis


if __name__ == '__main__':
    for n in (3, 4):
        for mode in ('refl', 'rot'):
            env = setup(n, mode)
            for native in (False, True):
                g0, basis = affine_space(env, native)
                print('n=%d NOT=%s native=%s: affine family dimension %d' % (n, mode, native, len(basis)))
