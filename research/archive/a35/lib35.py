"""Act 35 pre-freeze library: the landed objects of acts 24-34 in numpy, plus the off-locus tools.

Conventions (from the landed Lean):
  U        : 4x4 (single carrier) or 16x16 (product) unitary with |entries| = 1/2 resp. 1/4
  tuple    : G i j k = conj(U[i,j]) U[i,k]       (FibreGram at ancilla Fin 1)
  feature  : mixedTriple G ((i1,i2,i3),(j1,j2,j3)) = G i1 j1 j2 * G i2 j2 j3 * G i3 j3 j1
  inner    : <fv G, fv G'> = tr(A^3),  A_jk = sum_i conj(G i j k) G' i j k = sum_i W_ij conj(W_ik),
             W = U * conj(U')  (entrywise)    -- exact consequence of the definition, checked in probe1
  F4(z)    : (1/2) [[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]
  circle r : tup r z i = (FibreGram 0 (F4(z)/2) (pi_r i)).submatrix tau_r tau_r, i.e.
             U_r(z)[i, j] = F4(z)[pi_r i, tau_r j]
  product  : (X ⊠ Y) i j k = X i.1 j.1 k.1 * Y i.2 j.2 k.2, index (a,b) of Fin 4 x Fin 4 -> 4a+b
"""
import numpy as np, itertools

# ---- single carrier -------------------------------------------------------------------------
def F4(z):
    return 0.5 * np.array([[1, 1, 1, 1], [1, z, -1, -z], [1, -1, 1, -1], [1, -z, -1, z]], dtype=complex)

def swap(a, b):
    p = list(range(4)); p[a], p[b] = p[b], p[a]; return tuple(p)
ID4 = (0, 1, 2, 3)
# the frozen table R of act 33 / 34: (pi, tau) per circle
R = [(ID4, ID4), (ID4, swap(2, 3)), (ID4, swap(1, 2)), (swap(2, 3), ID4), (swap(2, 3), swap(2, 3)),
     (swap(2, 3), swap(1, 2)), (swap(1, 2), ID4), (swap(1, 2), swap(2, 3)), (swap(1, 2), swap(1, 2))]
V1 = [0, 2, 4, 2, 0, 3, 4, 5, 0]
V2 = [1, 3, 5, 5, 4, 1, 3, 1, 2]

def U_circle(r, z):
    """the 4x4 unitary whose fibre-Gram tuple is tup r z."""
    pi, tau = R[r]
    F = F4(z)
    return np.array([[F[pi[i], tau[j]] for j in range(4)] for i in range(4)])

def tuple_of_U(U):
    """G[i, j, k] = conj(U[i,j]) U[i,k]"""
    return np.conj(U)[:, :, None] * U[:, None, :]

def mixed_triple(G):
    """the full feature vector as an array indexed [i1,i2,i3,j1,j2,j3] (single carrier only: 4^6)."""
    n = G.shape[0]
    M = np.zeros((n,) * 6, dtype=complex)
    for i1, i2, i3, j1, j2, j3 in itertools.product(range(n), repeat=6):
        M[i1, i2, i3, j1, j2, j3] = G[i1, j1, j2] * G[i2, j2, j3] * G[i3, j3, j1]
    return M

def inner_U(U, Up):
    """<fv(G_U), fv(G_U')> = tr(A^3), A = W^T conj(W), W = U * conj(U')."""
    W = U * np.conj(Up)
    A = W.T @ np.conj(W)
    return np.trace(A @ A @ A)

def dist2_U(U, Up):
    return (inner_U(U, U) + inner_U(Up, Up) - 2 * inner_U(U, Up).real).real

# ---- product configuration -------------------------------------------------------------------
def kron(X, Y):
    """U_{(a,b),(c,d)} = X[a,c] Y[b,d]; index (a,b) -> 4a+b (the frozen pairing)."""
    return np.kron(X, Y)

def dephase(H):
    """the unique phase-equivalent matrix with positive real first row and column (entries nonzero)."""
    H = H.copy()
    H = H / (H[:, :1] / np.abs(H[:, :1]))          # row phases: first column positive
    H = H / (H[:1, :] / np.abs(H[:1, :]))          # column phases: first row positive
    return H

def sigma_residual(H):
    """max |D[(a,b),(c,d)] - D[(a,0),(c,0)] D[(0,b),(0,d)] / D[0,0]| over the dephased D:
    zero iff the class of H is phase-equivalent to a Kronecker product with the frozen pairing."""
    D = dephase(H)
    n = int(round(np.sqrt(H.shape[0])))
    D4 = D.reshape(n, n, n, n)  # [a,b,c,d]
    X = D4[:, 0, :, 0]; Y = D4[0, :, 0, :]
    P = np.einsum('ac,bd->abcd', X, Y) / D[0, 0]
    return np.max(np.abs(D4 - P))

def is_unitary(U, tol=1e-9):
    return np.max(np.abs(U @ np.conj(U).T - np.eye(U.shape[0]))) < tol

def is_flat(U, tol=1e-9):
    n = U.shape[0]
    return np.max(np.abs(np.abs(U) - 1 / np.sqrt(n))) < tol

def dita(X, Ys, D):
    """the Diţă matrix H_{(a,b),(c,d)} = X[a,c] * D[c,b] * Ys[c][b,d]: for each column block c a
    4x4 unitary Ys[c] (all flat) and a phase row D[c,:]. Realizable whenever X and all Ys are."""
    n = X.shape[0]; m = Ys[0].shape[0]
    H = np.zeros((n * m, n * m), dtype=complex)
    for a in range(n):
        for c in range(n):
            H[a * m:(a + 1) * m, c * m:(c + 1) * m] = X[a, c] * (D[c][:, None] * Ys[c])
    return H

def dita_T(X, Ys, E):
    """the transposed construction H_{(a,b),(c,d)} = X[a,c] * E[a,d] * Ys[a][b,d] (row blocks)."""
    n = X.shape[0]; m = Ys[0].shape[0]
    H = np.zeros((n * m, n * m), dtype=complex)
    for a in range(n):
        for c in range(n):
            H[a * m:(a + 1) * m, c * m:(c + 1) * m] = X[a, c] * (Ys[a] * E[a][None, :])
    return H

# ---- defect ---------------------------------------------------------------------------------
def defect_system(H):
    """real linear system for R (real n x n): d/dt of H∘e^{iR} unitary at t=0:
    sum_k (R_ik - R_jk) H_ik conj(H_jk) = 0 for i<j (complex) -> 2 real rows each.
    unknowns R flattened (n*n)."""
    n = H.shape[0]
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            c = H[i] * np.conj(H[j])            # coefficients of R_ik - R_jk
            row = np.zeros(n * n, dtype=complex)
            row[i * n:(i + 1) * n] += c
            row[j * n:(j + 1) * n] -= c
            rows.append(row.real); rows.append(row.imag)
    return np.array(rows)

def defect_numeric(H, tol=1e-8):
    """dim of the solution space minus the trivial 2n-1."""
    n = H.shape[0]
    M = defect_system(H)
    s = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(s > tol * s[0]))
    return n * n - rank - (2 * n - 1), s

def tangent_rank(vectors, n, tol=1e-8):
    """rank of a set of real n*n tangent vectors modulo the trivial phase directions a_i + b_k."""
    triv = []
    for i in range(n):
        v = np.zeros((n, n)); v[i, :] = 1; triv.append(v.ravel())
    for k in range(n):
        v = np.zeros((n, n)); v[:, k] = 1; triv.append(v.ravel())
    T = np.array(triv)
    A = np.array([v.ravel() for v in vectors])
    r_all = np.linalg.matrix_rank(np.vstack([T, A]), tol=tol)
    r_triv = np.linalg.matrix_rank(T, tol=tol)
    return r_all - r_triv

# ---- invariants ------------------------------------------------------------------------------
def profile(H):
    """multiset of |sum_k H_ak conj(H_bk) H_ck conj(H_dk)| over 4-subsets a<b<c<d of rows
    (equivalence invariant under row/column permutations and phases), rounded."""
    n = H.shape[0]
    Hn = H / np.abs(H)
    vals = []
    for a, b, c, d in itertools.combinations(range(n), 4):
        vals.append(round(abs(np.sum(Hn[a] * np.conj(Hn[b]) * Hn[c] * np.conj(Hn[d]))), 6))
    return tuple(sorted(vals))

def haagerup_set(H, digits=6):
    """the set of dephased-invariant cross ratios H_ij H_kl conj(H_il H_kj), rounded."""
    n = H.shape[0]
    Hn = H / np.abs(H)
    s = set()
    for i, k in itertools.combinations(range(n), 2):
        for j, l in itertools.combinations(range(n), 2):
            v = Hn[i, j] * Hn[k, l] * np.conj(Hn[i, l] * Hn[k, j])
            s.add((round(v.real, digits), round(v.imag, digits)))
    return frozenset(s)
