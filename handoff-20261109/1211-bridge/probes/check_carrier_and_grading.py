"""SANITY CHECKS ONLY (BRIDGE-UNIT1). Not evidence for any new result.
Check A: stabilizer Lie-algebra dimension of a generic O-equivariant condensate
  Sigma = a P_T1 + b P_E + c P_A1 on the six signed cubic links,
  (i) inside so(6) (real carrier), (ii) inside u(6) (complexified carrier).
  Expected by Schur: so(3)+so(2)+so(1) = 4 ; u(3)+u(2)+u(1) = 14.
Check B: on a bipartite ring, opposite-parity hopping anticommutes with the
  sublattice grading eps; adding same-parity (next-nearest) hopping does not.
"""
import itertools, numpy as np
# six signed links e_{+1},e_{-1},...,e_{+3},e_{-3} as vectors in R^3
links = []
for j in range(3):
    for s in (+1, -1):
        v = np.zeros(3); v[j] = s; links.append(v)
links = np.array(links)
def perm_of(R):
    P = np.zeros((6, 6))
    for i, v in enumerate(links):
        w = R @ v
        k = [n for n, u in enumerate(links) if np.allclose(u, w)][0]
        P[k, i] = 1
    return P
# rotation group O (det +1 signed permutation matrices of R^3)
G = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i, p in enumerate(perm): R[p, i] = signs[i]
        if np.isclose(np.linalg.det(R), 1): G.append(perm_of(R))
assert len(G) == 24
chi = [np.trace(P) for P in G]
# isotypic projectors via characters of O on the 6-dim link rep
# build projector onto equivariant-commutant blocks by diagonalising a generic equivariant operator
rng = np.random.default_rng(0)
X = rng.normal(size=(6, 6)); X = X + X.T
Sig = sum(P @ X @ P.T for P in G) / len(G)  # generic O-equivariant symmetric operator
w, V = np.linalg.eigh(Sig)
mult = np.unique(np.round(w, 8), return_counts=True)[1]
print("eigenvalue multiplicities of generic equivariant Sigma:", sorted(mult))
def stab_dim(basis):
    M = np.array([(B @ Sig - Sig @ B).ravel() for B in basis]).T
    return len(basis) - np.linalg.matrix_rank(M, tol=1e-9)
so6 = []
for i in range(6):
    for j in range(i + 1, 6):
        E = np.zeros((6, 6)); E[i, j] = 1; E[j, i] = -1; so6.append(E)
u6 = list(so6)  # real antisymmetric
for i in range(6):
    for j in range(i, 6):
        E = np.zeros((6, 6), complex); E[i, j] = 1j; E[j, i] = 1j; u6.append(E)  # i*symmetric
print("dim stabilizer in so(6) (real carrier):", stab_dim(so6))
print("dim stabilizer in u(6)  (complex carrier):", stab_dim(u6))
# Check B
L = 8
eps = np.diag([(-1) ** i for i in range(L)])
D1 = np.zeros((L, L)); D2 = np.zeros((L, L))
for i in range(L):
    D1[i, (i + 1) % L] = D1[(i + 1) % L, i] = 1
    D2[i, (i + 2) % L] = D2[(i + 2) % L, i] = 1
print("|| {D_nn, eps} || =", np.linalg.norm(D1 @ eps + eps @ D1))
print("|| {D_nn + 0.1 D_same, eps} || =", np.linalg.norm((D1 + 0.1 * D2) @ eps + eps @ (D1 + 0.1 * D2)))
