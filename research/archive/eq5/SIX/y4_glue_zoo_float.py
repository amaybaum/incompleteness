"""EQ4-SIX exploration y4 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  Is the crossing-split glue network N(x, y, e, f) (NOTES N1, (A4)) ever negative when all four
nodes are block-positive across every cut (x, y, e, f in BS*)?  If never, (A4) would be a consequence of (A1) and the
six-token wall would reduce to (A1)-(A3) alone.  Zoo of BS* elements: PSD rank-one (GHZ class, W, random),
projector witnesses lambda(psi) I - |psi><psi| (lambda = largest squared Schmidt coefficient over the three cuts, so
the witness is tight on BS), kappa = 1/2 + |000><111| + h.c., nu = I - 2 GHZ+ + 4 GHZ-; every node with its own local
filter Ad(k), k in GL(2,C)^3, optimized by BFGS with the exact gradient (as in y3).
Also the theta network (three Bell links between two triples) on the same zoo, as a calibration: it is known to go
negative (GHZ against W3: -1/16).
"""
import sys

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(2026100904)
I8 = np.eye(8)


def t6(M):
    return M.reshape(2, 2, 2, 2, 2, 2)


def m8(T):
    return T.reshape(8, 8)


def net(x, y, e, f):
    return 0.25 * np.real(np.einsum("abcdef,aghdij,keilbg,kfjlch->", t6(e), t6(f), t6(x), t6(y)))


def envs(x, y, e, f):
    ex = 0.25 * np.einsum("abcdef,aghdij,kfjlch->keilbg", t6(e), t6(f), t6(y))
    ey = 0.25 * np.einsum("abcdef,aghdij,keilbg->kfjlch", t6(e), t6(f), t6(x))
    ee = 0.25 * np.einsum("aghdij,keilbg,kfjlch->abcdef", t6(f), t6(x), t6(y))
    ef = 0.25 * np.einsum("abcdef,keilbg,kfjlch->aghdij", t6(e), t6(x), t6(y))
    return [m8(ex).T, m8(ey).T, m8(ee).T, m8(ef).T]


def gl2(p):
    return (p[0:4] + 1j * p[4:8]).reshape(2, 2)


def mats(p):
    return gl2(p[0:8]), gl2(p[8:16]), gl2(p[16:24])


def kmat(p):
    A, B, C = mats(p)
    return np.kron(np.kron(A, B), C)


def grad_k(p, g, M):
    A, B, C = mats(p)
    k = np.kron(np.kron(A, B), C)
    G = g @ k.conj().T @ M
    G6 = G.T.reshape(2, 2, 2, 2, 2, 2)
    gA = np.einsum("abcxyz,by,cz->ax", G6, B, C)
    gB = np.einsum("abcxyz,ax,cz->by", G6, A, C)
    gC = np.einsum("abcxyz,ax,by->cz", G6, A, B)
    out = []
    for gm in (gA, gB, gC):
        out += list((2 * gm.real).reshape(4)) + list((-2 * gm.imag).reshape(4))
    return np.array(out)


def fval(p, gs):
    ks = [kmat(p[24 * i:24 * i + 24]) for i in range(4)]
    nodes = [ks[i] @ gs[i] @ ks[i].conj().T for i in range(4)]
    N = net(*nodes)
    nr = [np.linalg.norm(X) for X in nodes]
    D = np.prod(nr)
    Ms = envs(*nodes)
    grad = np.zeros(96)
    for i in range(4):
        pi = p[24 * i:24 * i + 24]
        grad[24 * i:24 * i + 24] = grad_k(pi, gs[i], Ms[i]) / D - (N / D) * grad_k(pi, gs[i], nodes[i]) / nr[i] ** 2
    return N / D, grad


def schmidt_max(psi):
    t = psi.reshape(2, 2, 2)
    best = 0
    for ax in range(3):
        M = np.moveaxis(t, ax, 0).reshape(2, 4)
        best = max(best, np.linalg.svd(M, compute_uv=False)[0] ** 2)
    return best


def witness(psi):
    psi = psi / np.linalg.norm(psi)
    return schmidt_max(psi) * I8 - np.outer(psi, psi.conj())


ghz = np.zeros(8)
ghz[0] = ghz[7] = 1 / np.sqrt(2)
wst = np.zeros(8)
wst[1] = wst[2] = wst[4] = 1 / np.sqrt(3)
G0 = np.outer(ghz, ghz)
Gm = np.zeros((8, 8))
Gm[0, 0] = Gm[7, 7] = 0.5
Gm[0, 7] = Gm[7, 0] = -0.5
zoo = {"GHZ": G0, "W": np.outer(wst, wst), "W3": witness(ghz), "Wwit": witness(wst),
       "kappa": 0.5 * I8 + (np.eye(8)[:, [0]] @ np.eye(8)[[7], :]) + (np.eye(8)[:, [7]] @ np.eye(8)[[0], :]),
       "nu": I8 - 2 * G0 + 4 * Gm}
for i in range(4):
    v = rng.normal(size=8) + 1j * rng.normal(size=8)
    zoo["wit%d" % i] = witness(v)
    zoo["psd%d" % i] = np.outer(v, v.conj()) / np.vdot(v, v).real
names = sorted(zoo)
# membership sanity: every zoo element is >= 0 on random biproducts
worst_bp = np.inf
for nm in names:
    X = zoo[nm]
    for _ in range(300):
        a = rng.normal(size=2) + 1j * rng.normal(size=2)
        b = rng.normal(size=4) + 1j * rng.normal(size=4)
        for ax in range(3):
            v = np.kron(a, b).reshape(2, 2, 2)
            v = np.moveaxis(v, 0, ax).reshape(8)
            worst_bp = min(worst_bp, np.real(np.vdot(v, X @ v)) / np.vdot(v, v).real)
print("zoo: %s; min value on random biproducts %.3e (BS* membership sanity)" % (names, worst_bp), flush=True)

worst = (np.inf, None)
for trial in range(240):
    nm = [names[i] for i in rng.integers(len(names), size=4)]
    gs = [zoo[nm[0]], zoo[nm[1]], zoo[nm[2]].T, zoo[nm[3]].T]
    best = np.inf
    for _s in range(2):
        r = minimize(fval, rng.normal(size=96), args=(gs,), jac=True, method="BFGS",
                     options={"maxiter": 5000, "gtol": 1e-11})
        best = min(best, r.fun)
    if best < worst[0]:
        worst = (best, tuple(nm))
    if trial % 40 == 39:
        print("after %d trials: worst normalized glue-network min %.4e at %s" % (trial + 1, worst[0], worst[1]), flush=True)
print("done", file=sys.stderr)
