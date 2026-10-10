"""EQ4-SIX exploration y22 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  Can the C_A boundary point X_t (Xi, d = (1,1,2,2), c = 2 sqrt 2, rho = 4; outside Lift(K_A) by
y16) or the y16 dual element Y_t (Xi, moduli (1/3, 1/6, 1/2), rho ~ 5.6e-3; in Lift(K_A)* \ Lift(K_A) by y16/y19)
belong to a K_A-lift satisfying (A4)?  Glue network (crossing split, Bell links; code of y3, analytic gradients),
nodes Ad(k) g with g from {non-PSD K_A generators} and the candidate (T(X_t) = X_t, T(Y_t) = Y_t: both are real).
Runs: (a) the candidate in all four positions; (b) the candidate in one random position, K_A generators elsewhere;
(c) the candidate as both states, K_A generators as effects; control: PSD nodes (>= 0 expected);
countercontrol: X_t and Y_t as the two states with the biseparable effects (1/2) 1_s (x) Phi+_{r1 u1} and
(1/2) 1_t (x) Phi+_{r2 u2} (filters free), where the unfiltered network is (1/32) tr(x T(y)) (s3 B) and
<X_t, Y_t> < 0: must be negative.
DECISION RULE (fixed before the first run; lead only): a candidate is "excluded by (A4) (lead)" iff some run gives a
normalized minimum < -1e-6 with the countercontrol negative and the control >= -1e-9; "not excluded (lead)" iff every
run's minimum is >= -1e-9.
"""
import sys

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(2026100922)


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


WT = np.array([bin(a).count("1") for a in range(8)])
BIN = np.array([1, 3, 3, 1])
d_t = np.array([1.0, 1.0, 2.0, 2.0])
X_t = np.diag(d_t[WT]).astype(complex)
X_t[0, 7] = X_t[7, 0] = 2 * np.sqrt(2)
yd = np.array([0.35628263794720455, 1.2133877116503091, 0.20603472212519652, 0.31186223417779774])
Y_t = np.diag((yd / BIN)[WT]).astype(complex)
Y_t[0, 7] = Y_t[7, 0] = -0.5
print("<X_t, Y_t> = %.6f" % np.real(np.trace(X_t @ Y_t)), flush=True)


PHI = np.zeros((4, 4))
PHI[0, 0] = PHI[0, 3] = PHI[3, 0] = PHI[3, 3] = 0.5
BELL_EFF = np.kron(0.5 * np.eye(2), PHI)


def pick_all(C, nm):
    return lambda: ([C, C, C.T, C.T], (nm,) * 4)


def pick_one(C, nm):
    def f():
        ii = rng.integers(len(NEG), size=4)
        gs = [NEG[ii[0]], NEG[ii[1]], NEG[ii[2]].T, NEG[ii[3]].T]
        names = [NEGNAME[i] for i in ii]
        pos = rng.integers(4)
        gs[pos] = C if pos < 2 else C.T
        names[pos] = nm
        return gs, tuple(names)
    return f


def pick_states(C, nm):
    def f():
        ii = rng.integers(len(NEG), size=2)
        return [C, C, NEG[ii[0]].T, NEG[ii[1]].T], (nm, nm, NEGNAME[ii[0]], NEGNAME[ii[1]])
    return f


def pick_counter():
    return [X_t, Y_t, BELL_EFF, BELL_EFF], ("X_t", "Y_t", "1/2 (x) Phi+", "1/2 (x) Phi+")


def pick_psd():
    vs = [rng.normal(size=8) + 1j * rng.normal(size=8) for _ in range(4)]
    return [np.outer(v, v.conj()) for v in vs], ("psd",) * 4


run("control PSD nodes", pick_psd, 10)
run("countercontrol X_t, Y_t states with (1/2) (x) Phi+ effects", pick_counter, 10)
for C, nm in ((X_t, "X_t"), (Y_t, "Y_t")):
    run("(a) %s in all four positions" % nm, pick_all(C, nm), 20)
    run("(b) %s in one position, K_A generators elsewhere" % nm, pick_one(C, nm), 60)
    run("(c) %s as both states, K_A generator effects" % nm, pick_states(C, nm), 40)
print("done", file=sys.stderr)
