"""q=2, leaps only: do Clifford images of the leapfrogs (symmetric couplings on N=2 sites) exist that
reproduce the classical marginal of cur (prev uniform) on all words?  Images solved from
U W(z) = s_z W(Lz) U over every sign pattern s (the q=2 Weyl relations carry signs)."""
import itertools, numpy as np
q, N = 2, 2
d = 4
pts = list(itertools.product(range(2), repeat=N)); idx = {p: i for i, p in enumerate(pts)}
def X(a):
    U = np.zeros((d, d), complex)
    for p in pts: U[idx[tuple((np.array(p) + a) % 2)], idx[p]] = 1
    return U
def Z(b): return np.diag([(-1) ** (int(np.dot(b, p)) % 2) for p in pts]).astype(complex)
def W(x, xi): return (1j) ** (int(np.dot(x, xi)) % 4) * (Z(np.array(xi)) @ X(np.array(x)))
def leap(M):
    L = np.zeros((4, 4), int); L[:2, :2] = M; L[:2, 2:] = np.eye(2, dtype=int); L[2:, :2] = np.eye(2, dtype=int)
    return L % 2
def images(L):
    out = []
    gens = [np.eye(4, dtype=int)[k] for k in range(4)]
    for signs in itertools.product((1, -1), repeat=4):
        rows = []
        for s, z in zip(signs, gens):
            Lz = (L @ z) % 2
            A = W(z[:2], z[2:]); B = s * W(Lz[:2], Lz[2:])
            rows.append(np.kron(A.T, np.eye(d)) - np.kron(np.eye(d), B))
        sv, vh = np.linalg.svd(np.vstack(rows))[1:]
        if np.sum(sv < 1e-8) == 1:
            U = vh[-1].conj().reshape(d, d, order='F'); U /= np.sqrt(np.real(np.trace(U.conj().T @ U)) / d)
            if np.allclose(U.conj().T @ U, np.eye(d), atol=1e-8): out.append(U)
    return out
Ms = [np.array([[a, c], [c, b]]) for a in range(2) for b in range(2) for c in range(2)]
def cl_marg(word, x0):
    dist = np.zeros(d)
    for xi in pts:
        x, p = np.array(x0), np.array(xi)
        for M in word: x, p = (M @ x + p) % 2, x       # -p = p mod 2
        dist[idx[tuple(x)]] += 1 / 4
    return dist
def qu_marg(word, x0, U_of):
    v = np.zeros(d, complex); v[idx[x0]] = 1
    for k in word: v = U_of[k] @ v
    return np.abs(v) ** 2
cands = [images(leap(M)) for M in Ms]
print("candidate images per coupling:", [len(c) for c in cands])
# single-leap consistency (powers), per coupling
single_ok = []
for i, M in enumerate(Ms):
    ok = [U for U in cands[i] if all(np.allclose(qu_marg([0] * k, x0, {0: U}), cl_marg([M] * k, x0)) for k in range(1, 13) for x0 in pts)]
    single_ok.append(ok)
print("images consistent under powers alone:", [len(o) for o in single_ok])
# joint consistency for two couplings (zero coupling and the nearest-neighbour coupling)
pairs = [(0, 1), (0, 6), (1, 6), (3, 5)]
for (i, j) in pairs:
    found = 0
    for Ui in single_ok[i]:
        for Uj in single_ok[j]:
            U_of = {0: Ui, 1: Uj}; Mm = {0: Ms[i], 1: Ms[j]}
            if all(np.allclose(qu_marg(w, x0, U_of), cl_marg([Mm[k] for k in w], x0))
                   for L in range(1, 7) for w in itertools.product((0, 1), repeat=L) for x0 in pts):
                found += 1
    print(f"couplings {Ms[i].tolist()} & {Ms[j].tolist()}: consistent image pairs = {found}")
