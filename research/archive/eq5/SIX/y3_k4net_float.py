"""EQ4-SIX exploration y3 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Successor of y2 (stopped by hand: numerical gradients too slow).  Same question with analytic gradients.
Glue network, crossing split (NOTES N1):
  N = 1/4 sum e[s r1 u1; s' r1' u1'] f[s r2 u2; s' r2' u2'] x[p' r1' r2'; p r1 r2] y[p' u1' u2'; p u1 u2],
nodes x = Ad(k_x) g_x, y = Ad(k_y) g_y (states), e = Ad(k_e) g_e^T, f = Ad(k_f) g_f^T (effects; T(Ad(k) g) = Ad(conj k) g^T),
k in GL(2,C)^3.  Minimize N / (|x||y||e||f|) by BFGS with the exact gradient.
Runs: (1) all four nodes from the non-PSD generators of K_A (Lift(K_A)); (2) countercontrol: states filtered GHZ (PSD,
GHZ class), effects from Lift(K_A) — tests whether the network can detect the GHZ / K_A conflict at all; (3) control:
all nodes PSD (rank one, random), expected >= 0.
"""
import sys

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(2026100903)


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
NEG = [I8 - 2 * P[j] for j in range(8)] + [I8 - 2 * P[j] + 2 * P[p] for j in range(8) for p in range(8) if p != j]
NEGNAME = ["m%d" % j for j in range(8)] + ["n%d%d" % (j, p) for j in range(8) for p in range(8) if p != j]


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
    return [m8(ex).T, m8(ey).T, m8(ee).T, m8(ef).T]   # N = tr(M X) for each node X


def gl2(p):
    return (p[0:4] + 1j * p[4:8]).reshape(2, 2)


def mats(p):
    return gl2(p[0:8]), gl2(p[8:16]), gl2(p[16:24])


def kmat(p):
    A, B, C = mats(p)
    return np.kron(np.kron(A, B), C)


def grad_k(p, g, M):
    """gradient over the 24 real parameters of k of tr(M k g k^dag) (M, g Hermitian)."""
    A, B, C = mats(p)
    k = np.kron(np.kron(A, B), C)
    G = g @ k.conj().T @ M                      # dN = 2 Re tr(G dk)
    G6 = G.T.reshape(2, 2, 2, 2, 2, 2)          # G6[a, b, c, a', b', c'] = G[(a'b'c'), (abc)]
    gA = np.einsum("abcxyz,by,cz->ax", G6, B, C)
    gB = np.einsum("abcxyz,ax,cz->by", G6, A, C)
    gC = np.einsum("abcxyz,ax,by->cz", G6, A, B)
    out = []
    for gm in (gA, gB, gC):
        out += list((2 * gm.real).reshape(4)) + list((-2 * gm.imag).reshape(4))
    return np.array(out)


def fval(p, gs):
    nodes = [kmat(p[24 * i:24 * i + 24]) @ gs[i] @ kmat(p[24 * i:24 * i + 24]).conj().T for i in range(4)]
    N = net(*nodes)
    nr = [np.linalg.norm(X) for X in nodes]
    D = np.prod(nr)
    Ms = envs(*nodes)
    grad = np.zeros(96)
    for i in range(4):
        pi = p[24 * i:24 * i + 24]
        dN = grad_k(pi, gs[i], Ms[i])
        dlog = grad_k(pi, gs[i], nodes[i]) / (nr[i] ** 2)   # d log|X| = tr(X dX)/|X|^2
        grad[24 * i:24 * i + 24] = dN / D - (N / D) * dlog
    return N / D, grad


def run(label, pick, trials):
    worst = (np.inf, None)
    for _ in range(trials):
        gs, names = pick()
        best = np.inf
        for _s in range(2):
            r = minimize(fval, rng.normal(size=96), args=(gs,), jac=True, method="BFGS",
                         options={"maxiter": 5000, "gtol": 1e-11})
            best = min(best, r.fun)
        if best < worst[0]:
            worst = (best, names)
    print("%s: %d trials; worst normalized min %.4e at %s" % (label, trials, worst[0], worst[1]), flush=True)


# gradient sanity check (finite differences)
gs0 = [NEG[0], NEG[9], NEG[3].T, NEG[20].T]
p0 = rng.normal(size=96)
v0, g0 = fval(p0, gs0)
h = 1e-6
fd = np.array([(fval(p0 + h * np.eye(96)[i], gs0)[0] - fval(p0 - h * np.eye(96)[i], gs0)[0]) / (2 * h) for i in range(96)])
print("gradient check: max |analytic - finite difference| = %.2e" % np.max(np.abs(fd - g0)), flush=True)


def pick_lift():
    ii = rng.integers(len(NEG), size=4)
    return [NEG[ii[0]], NEG[ii[1]], NEG[ii[2]].T, NEG[ii[3]].T], tuple(NEGNAME[i] for i in ii)


def pick_counter():
    ii = rng.integers(len(NEG), size=2)
    return [P[0], P[0], NEG[ii[0]].T, NEG[ii[1]].T], ("GHZ", "GHZ", NEGNAME[ii[0]], NEGNAME[ii[1]])


def pick_counter2():
    ii = rng.integers(len(NEG), size=2)
    return [P[0], NEG[ii[0]], P[0].T, NEG[ii[1]].T], ("GHZ", NEGNAME[ii[0]], "GHZ", NEGNAME[ii[1]])


def pick_psd():
    vs = [rng.normal(size=8) + 1j * rng.normal(size=8) for _ in range(4)]
    return [np.outer(v, v.conj()) for v in vs], ("psd",) * 4


run("control PSD nodes", pick_psd, 20)
run("countercontrol: GHZ states, Lift(K_A) effects", pick_counter, 40)
run("countercontrol: GHZ and Lift(K_A) mixed", pick_counter2, 40)
run("Lift(K_A) nodes (states and effects)", pick_lift, 300)
print("done", file=sys.stderr)
