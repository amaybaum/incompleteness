"""A34 pre-freeze probe 1: the feature map at act 29's product configuration.
(1) fv(X ⊠ Y) = fv(X) ⊗ fv(Y) up to the index pairing, hence <fv(X⊠Y), fv(X'⊠Y')> = <fv X, fv X'><fv Y, fv Y'>.
(2) the product realizable set (rank-1 tuples on Fin 4 x Fin 4 with diagonal 1/16, summing to 1) contains
    F16-type points whose feature vector is not of tensor-product form."""
import numpy as np, itertools
rng = np.random.default_rng(1)
def hadamard4(z):
    return 0.5 * np.array([[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]], dtype=complex)
def gram_tuple(U):
    # single ancilla: G i = (row-block)^H (row-block) with block = U[i, :] as a 1-row? Use the repo's FibreGram with A = one element:
    # FibreGram a0 U i = (U.submatrix (a -> (i,a)) (j -> (j,a0)))^H * (...) : G i j k = conj(U[i,j]) * U[i,k]
    n = U.shape[0]
    G = np.zeros((n, n, n), dtype=complex)
    for i in range(n):
        G[i] = np.outer(np.conj(U[i]), U[i])
    return G
def realizable(G, tol=1e-9):
    n = G.shape[0]
    ok = np.allclose(sum(G[i] for i in range(n)), np.eye(n), atol=tol)
    diag = np.allclose(np.array([[G[i][j][j] for j in range(n)] for i in range(n)]), 1.0 / n, atol=tol)
    ranks = all(np.linalg.matrix_rank(G[i], tol=1e-8) <= 1 for i in range(n))
    return ok and diag and ranks
def mixed_triple(G):
    n = G.shape[0]
    # p = ((a,b,c),(d,e,f)) -> G a d e * G b e f * G c f d  (repo: G p.1.1 p.2.1 p.2.2.1 * G p.1.2.1 p.2.2.1 p.2.2.2 * G p.1.2.2 p.2.2.2 p.2.1)
    T = np.einsum('ade,bef,cfd->abcdef', G, G, G)
    return T.reshape(-1)
# ---- (1) tensor factorization
z, w = np.exp(1j*0.7), np.exp(1j*2.1)
X, Y = gram_tuple(hadamard4(z)), gram_tuple(hadamard4(w))
assert realizable(X) and realizable(Y)
# product tuple on V = Fin4 x Fin4 with index (i1,i2) -> 4*i1+i2
P = np.zeros((16,16,16), dtype=complex)
for i1,i2,j1,j2,k1,k2 in itertools.product(range(4), repeat=6):
    P[4*i1+i2, 4*j1+j2, 4*k1+k2] = X[i1,j1,k1] * Y[i2,j2,k2]
assert realizable(P)
fP = mixed_triple(P)                    # 16^6 entries
fX, fY = mixed_triple(X), mixed_triple(Y)   # 4^6 each
# reorder fP to (a1 b1 c1 d1 e1 f1)(a2 b2 c2 d2 e2 f2)
T = fP.reshape([4,4]*6)                # axes: a1,a2,b1,b2,c1,c2,d1,d2,e1,e2,f1,f2
T = T.transpose(0,2,4,6,8,10, 1,3,5,7,9,11).reshape(4096, 4096)
print('(1) fv(X⊠Y) == fv(X) ⊗ fv(Y):', np.allclose(T, np.outer(fX, fY)))
X2, Y2 = gram_tuple(hadamard4(np.exp(1j*1.3))), gram_tuple(hadamard4(np.exp(1j*-0.4)))
P2 = np.zeros((16,16,16), dtype=complex)
for i1,i2,j1,j2,k1,k2 in itertools.product(range(4), repeat=6):
    P2[4*i1+i2, 4*j1+j2, 4*k1+k2] = X2[i1,j1,k1] * Y2[i2,j2,k2]
fP2 = mixed_triple(P2)
lhs = np.vdot(fP, fP2); rhs = np.vdot(fX, mixed_triple(X2)) * np.vdot(fY, mixed_triple(Y2))
print('    inner products multiply:', np.allclose(lhs, rhs), '| norms', abs(np.linalg.norm(fP)), abs(np.linalg.norm(fX)*np.linalg.norm(fY)))
# ---- (2) a non-product realizable point: the Fourier matrix of order 16 (scaled to entries of modulus 1/4)
F16 = np.array([[np.exp(2j*np.pi*j*k/16) for k in range(16)] for j in range(16)]) / 4.0
Q = gram_tuple(F16)
print('(2) F16 tuple realizable at the product configuration:', realizable(Q))
fQ = mixed_triple(Q).reshape([4,4]*6).transpose(0,2,4,6,8,10, 1,3,5,7,9,11).reshape(4096, 4096)
s = np.linalg.svd(fQ, compute_uv=False)
print('    singular values of the factor-paired feature matrix (top 6):', np.round(s[:6], 6), '| tensor rank 1?', s[1] < 1e-9)
# for comparison the product point
s1 = np.linalg.svd(T, compute_uv=False); print('    product point top-2 singular values:', np.round(s1[:2], 6))
# also: F4 ⊗ F4 with a mixed phase pattern? (Z4 x Z4 character table vs Z16): distance of fQ from the nearest product point is not computed here.
