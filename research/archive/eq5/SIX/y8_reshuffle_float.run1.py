"""EQ4-SIX exploration y8 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.

tr(g' Ad(A (x) B (x) C) g) = <v| H |v> with v = vec(A) (x) vec(B) (x) vec(C) in (C^4)^3 and
H = sum over the tensor structure of g' (x) g^T reshuffled per token (per token: X (x) Y^T on (row, col) of A).
If H is PSD, the orbit pairing is >= 0 for every k (sufficient, not necessary).  Print min eigenvalue of H for the
orbit pairs (kappa', kappa'), (kappa', omega), (omega, kappa'), (omega, omega), and W3 pairs as calibration.
H is built numerically by evaluating the bilinear form on a basis (exact structure: linear in v v^dag).
"""
import itertools

import numpy as np


def idx(x, y, z):
    return 4 * x + 2 * y + z


P = []
for b in range(4):
    b1, b2 = b >> 1, b & 1
    for t in range(2):
        v = np.zeros(8)
        v[idx(0, b1, b2)] = 1
        v[idx(1, 1 - b1, 1 - b2)] = 1 if t == 0 else -1
        P.append(np.outer(v, v) / 2)
I8 = np.eye(8)
G = {"W3": 0.5 * I8 - P[0], "kappa'": 0.5 * I8 - P[0] + P[1], "omega": 0.5 * I8 - P[0] + P[2]}


def Hmat(gp, g):
    # E(k) = tr(gp k g k^dag) = sum gp[i,j] k[j,l] g[l,m] conj(k[i,m]); k[(j1j2j3),(l1l2l3)] = prod A_t[j_t, l_t]
    # v index per token = (row, col) = (j, l); E = sum conj(v_I) H[I, J] v_J
    g6 = gp.reshape(2, 2, 2, 2, 2, 2)      # gp[i1 i2 i3, j1 j2 j3]
    h6 = g.reshape(2, 2, 2, 2, 2, 2)       # g[l1 l2 l3, m1 m2 m3]
    # E = sum gp[i, j] g[l, m] k[j, l] conj(k[i, m]) ; v_J = k[j, l] (J = (j,l) per token), conj(v_I) = conj(k[i, m])
    H = np.einsum("abcdef,ghiklm->akbldmcl", g6, h6)  # placeholder, rebuilt below
    H = np.zeros((64, 64), dtype=complex)
    for i in itertools.product(range(2), repeat=3):
        for j in itertools.product(range(2), repeat=3):
            gij = gp[idx(*i), idx(*j)]
            if gij == 0:
                continue
            for l in itertools.product(range(2), repeat=3):
                for m in itertools.product(range(2), repeat=3):
                    glm = g[idx(*l), idx(*m)]
                    if glm == 0:
                        continue
                    I = sum((4 * i[t] + 2 * 0 + m[t]) * 0 for t in range(3))
                    rowI = 0
                    colJ = 0
                    for t in range(3):
                        rowI = rowI * 4 + (2 * i[t] + m[t])
                        colJ = colJ * 4 + (2 * j[t] + l[t])
                    H[rowI, colJ] += gij * glm
    return H


rng = np.random.default_rng(1)
for (n1, g1), (n2, g2) in itertools.product(G.items(), G.items()):
    H = Hmat(g2, g1)
    # sanity: compare with direct evaluation on a random product filter
    A = [rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)) for _ in range(3)]
    k = np.kron(np.kron(A[0], A[1]), A[2])
    direct = np.trace(g2 @ k @ g1 @ k.conj().T)
    v = np.kron(np.kron(A[0].reshape(4), A[1].reshape(4)), A[2].reshape(4))
    via = np.vdot(v, H @ v)
    ev = np.linalg.eigvalsh((H + H.conj().T) / 2)
    print("pair (g = %s, g' = %s): check |direct - via H| = %.1e; Hermitian %s; min eig %.4f; #neg %d"
          % (n1, n2, abs(direct - via), np.allclose(H, H.conj().T), ev[0], int(np.sum(ev < -1e-12))))
