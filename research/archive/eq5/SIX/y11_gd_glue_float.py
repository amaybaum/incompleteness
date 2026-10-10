"""EQ4-SIX exploration y11 -- integer/float scan, EXPLORATION ONLY (used to choose a countercontrol for s4).
Glue network on GHZ-diagonal nodes (unfiltered): which node sets give negative values?  Sets: K_A generators,
nu-orbit (nu = (-1, 5, 1^6)), GHZ projectors e_j, W3 types m_j, S* = cone{e_j, m_j}."""
import itertools
import numpy as np


def idx(x, y, z):
    return 4 * x + 2 * y + z


VEC = []
for b in range(4):
    b1, b2 = b >> 1, b & 1
    for t in range(2):
        v = [0] * 8
        v[idx(0, b1, b2)] = 1
        v[idx(1, 1 - b1, 1 - b2)] = 1 if t == 0 else -1
        VEC.append(v)
P2 = [np.outer(np.array(v), np.array(v)).astype(np.int64) for v in VEC]
B2 = np.zeros((2, 2, 2, 2), dtype=np.int64)
for a in range(2):
    for b in range(2):
        B2[a, a, b, b] = 1


def t6(M):
    return M.reshape(2, 2, 2, 2, 2, 2)


def glue(x, y, e, f):
    gs = np.einsum("pqPQ,PabpAB,QcdqCD->abcdABCD", B2, t6(x), t6(y))
    ge = np.einsum("stST,SacsAC,TbdtBD->abcdABCD", B2, t6(e), t6(f))
    return int(np.einsum("abcdABCD,ABCDabcd->", ge, gs))


tau = np.zeros((8, 8, 8, 8), dtype=np.int64)
for i, j, k, l in itertools.product(range(8), repeat=4):
    tau[i, j, k, l] = glue(P2[i], P2[j], P2[k], P2[l])
print("tau nonzero entries:", int((tau != 0).sum()), "values:", sorted(set(tau.flatten().tolist())))
E = np.eye(8, dtype=np.int64)
M = np.array([[1 - 2 * (i == j) for i in range(8)] for j in range(8)], dtype=np.int64)
nu = np.array([[-1 if i == j else (5 if i == (j ^ 1) else 1) for i in range(8)] for j in range(8)], dtype=np.int64)


def mn(A, Bm, C, D):
    v = np.einsum("ijkl,ai,bj,ck,dl->abcd", tau, A, Bm, C, D)
    w = np.unravel_index(np.argmin(v), v.shape)
    return int(v.min()), w


SS = np.vstack([E, M])
print("S* x S* x S* x S*:", mn(SS, SS, SS, SS))
print("e,e,m,m:", mn(E, E, M, M), " m,m,e,e:", mn(M, M, E, E), " e,m,e,m:", mn(E, M, E, M))
print("nu orbit (same-fibre partner) all four:", mn(nu, nu, nu, nu))
print("nu states, S* effects:", mn(nu, nu, SS, SS))
# structure of the support: label j = 2b + t (fibre b in Z_2^2, sign t); test linear relations over Z_2^3
sup = [tuple(int(v) for v in q) for q in np.argwhere(tau != 0)]
print("support size", len(sup))
def bits(j):
    return ((j >> 2) & 1, (j >> 1) & 1, j & 1)
rels = []
for coeffs in itertools.product(range(2), repeat=12):
    ok = True
    for q in sup:
        s = 0
        for n, j in enumerate(q):
            bj = bits(j)
            s ^= (coeffs[3 * n] & bj[0]) ^ (coeffs[3 * n + 1] & bj[1]) ^ (coeffs[3 * n + 2] & bj[2])
        if s:
            ok = False
            break
    if ok and any(coeffs):
        rels.append(coeffs)
print("number of Z_2-linear relations satisfied on the support:", len(rels))
print("first relations:", rels[:12])
