"""A34 probe 4: a kernel-friendly non-product realizable point (entries in {±1, ±i}/4).
Dita twist of F4 ⊗ F4: H[(i,a),(j,b)] = F4(i)[i,j] * D_j[a,b] with D_j = F4(z_j), z = (i, -i, i, -i).
A row-tuple of a 16x16 complex Hadamard (entries of modulus 1/4) is realizable at the product configuration.
Measure: realizable? paired feature matrix tensor rank 1? and the same for the untwisted product (control)."""
import numpy as np, itertools
def hadamard4(z):
    return 0.5 * np.array([[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]], dtype=complex)
def gram_tuple(U):
    n = U.shape[0]; G = np.zeros((n,n,n), dtype=complex)
    for i in range(n): G[i] = np.outer(np.conj(U[i]), U[i])
    return G
def realizable(G, tol=1e-9):
    n = G.shape[0]
    return (np.allclose(sum(G[i] for i in range(n)), np.eye(n), atol=tol)
            and np.allclose(np.array([[G[i][j][j] for j in range(n)] for i in range(n)]), 1.0/n, atol=tol)
            and all(np.linalg.matrix_rank(G[i], tol=1e-8) <= 1 for i in range(n)))
def paired_fv(G):
    f = np.einsum('ade,bef,cfd->abcdef', G, G, G).reshape([4,4]*6)
    return f.transpose(0,2,4,6,8,10, 1,3,5,7,9,11).reshape(4096, 4096)
def rank1_residual(M):
    # exact criterion: M has rank 1 iff every row is proportional to the row of largest norm
    k = np.argmax(np.linalg.norm(M, axis=1)); v = M[k]
    c = (M @ v.conj()) / np.vdot(v, v)
    return float(np.linalg.norm(M - np.outer(c, v)))
def dita(zs, outer=1j):
    F = hadamard4(outer); H = np.zeros((16,16), dtype=complex)
    for i, a, j, b in itertools.product(range(4), repeat=4):
        H[4*i+a, 4*j+b] = F[i, j] * hadamard4(zs[j])[a, b]
    return H
for name, zs in [('control: untwisted F4(i) ⊗ F4(i)', [1j]*4), ('twist z = (i,-i,i,-i)', [1j,-1j,1j,-1j]), ('twist z = (i,i,i,-i)', [1j,1j,1j,-1j])]:
    H = dita(zs)
    entries_ok = np.allclose(np.abs(H), 0.25) and np.allclose((4*H)**4, 1)      # entries in {±1,±i}/4
    G = gram_tuple(H)
    res = rank1_residual(paired_fv(G))
    print('%-36s unitary: %s | entries 4th roots/4: %s | realizable: %s | rank-1 residual (Frobenius) = %.4f | tensor rank 1: %s' %
          (name, np.allclose(H.conj().T @ H, np.eye(16)), entries_ok, realizable(G), res, res < 1e-9))
# is the twisted point equivalent to a product point by a relabelling of V? (necessary condition: paired rank 1 under some
# permutation of the 16 indices applied to rows and columns) -- sample the 2 coordinate-preserving swaps and 200 random perms
rng = np.random.default_rng(3); H = dita([1j,-1j,1j,-1j]); G = gram_tuple(H)
best = 1e9
for k in range(30):
    p = rng.permutation(16); Gp = np.zeros_like(G)
    for i in range(16): Gp[i] = G[p[i]][np.ix_(p, p)]
    best = min(best, rank1_residual(paired_fv(Gp)))
print('twisted point: min rank-1 residual over 30 random relabellings: %.4f (rank 1 would be 0)' % best)
