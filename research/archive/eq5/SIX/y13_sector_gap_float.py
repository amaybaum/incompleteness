"""EQ4-SIX exploration y13 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  Is Lift(K_A) self-dual?  Necessary: for every twirl sector Sigma (fixed space of a compact group
of symmetries of Lift(K_A)), Tw(Lift) = Lift cap Sigma equals Lift* cap Sigma = (Tw Lift)^{*Sigma}.
Test in sectors (X16: X-shaped operators, diagonal + anti-diagonal, the twirl over <ZZI, IZZ>, 16 dims; S10: zero-sum phase torus only, 10 dims; Z3: phases diag(1, w)^3 with w^3 = 1 only, 22 dims): sector6 (S_3 x phases diag(1, e^{i theta})^3; 6 dims) and Omega3 (S_3 x Z_3 phases diag(1, w)^3, w^3 = 1: weight
blocks + the |000><111| coherence; 8 dims), for random directions V in the sector:
  gen(V)  = sup over filtered generators G (normalized by trace) and biseparable pure states of <V, G>  (BFGS)
  dual(V) = max <V, Y> over Y in Sigma cap Lift*, tr Y = 1   (cutting planes; pricing as in y12)
dual(V) - gen(V) > 0 after converged pricing is a lead for a gap (Lift != Lift*).
"""
import sys

import numpy as np
from scipy.optimize import linprog, minimize

rng = np.random.default_rng(2026100913)
I8 = np.eye(8)
Wt = np.array([bin(a).count("1") for a in range(8)])
wv = np.zeros(8)
wv[[1, 2, 4]] = 1 / np.sqrt(3)
wbv = np.zeros(8)
wbv[[3, 5, 6]] = 1 / np.sqrt(3)
PW = np.outer(wv, wv)
PWb = np.outer(wbv, wbv)
Pi = [np.diag((Wt == w).astype(float)) for w in range(4)]
C07 = np.zeros((8, 8))
C07[0, 7] = C07[7, 0] = 1.0
C07i = np.zeros((8, 8), dtype=complex)
C07i[0, 7] = 1j
C07i[7, 0] = -1j
def unit_h(a, b):
    M = np.zeros((8, 8), dtype=complex)
    if a == b:
        M[a, a] = 1
        return [M]
    M1 = M.copy()
    M1[a, b] = M1[b, a] = 1
    M2 = M.copy()
    M2[a, b] = 1j
    M2[b, a] = -1j
    return [M1, M2]


S10B = [unit_h(a, a)[0] for a in range(8)] + unit_h(0, 7)
Z3B = []
for w in range(4):
    st = [a for a in range(8) if Wt[a] == w]
    for i, a in enumerate(st):
        for b in st[i:]:
            Z3B += unit_h(a, b)
Z3B += unit_h(0, 7)
X16 = [unit_h(a, a)[0] for a in range(8)] + unit_h(0, 7) + unit_h(1, 6) + unit_h(2, 5) + unit_h(3, 4)
SECTORS = {"X16": X16, "sector6": [Pi[0], PW, Pi[1] - PW, PWb, Pi[2] - PWb, Pi[3]], "S10": S10B, "Z3": Z3B,
           "Omega3": [Pi[0], PW, Pi[1] - PW, PWb, Pi[2] - PWb, Pi[3], C07, C07i]}


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
GT = [0.5 * I8 - P[0], 0.5 * I8 - P[0] + P[1], 0.5 * I8 - P[0] + P[2], 0.5 * I8 - P[0] + P[4], 0.5 * I8 - P[0] + P[6]]


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


def ratio(p, g, M, sign):
    k = kmat(p)
    Y = k @ g @ k.conj().T
    num = np.real(np.trace(M @ Y))
    den = np.real(np.trace(Y))
    return sign * num / den, sign * (grad_k(p, g, M) / den - num * grad_k(p, g, I8) / den ** 2)


def bisep_ext(M, sign):
    """sign = -1: min over biseparable pure states of <phi|M|phi>; sign = +1: max."""
    best = (np.inf, None)
    M6 = M.reshape(2, 2, 2, 2, 2, 2)
    for cut in range(3):
        Mc = np.moveaxis(np.moveaxis(M6, cut, 0), cut + 3, 3)
        for _ in range(6):
            def f(q):
                a = q[0:2] + 1j * q[2:4]
                a = a / np.linalg.norm(a)
                t = np.einsum("i,ijklmn,l->jkmn", a.conj(), Mc, a).reshape(4, 4)
                ev = np.linalg.eigvalsh((t + t.conj().T) / 2)
                return ev[0] if sign < 0 else -ev[-1]
            r = minimize(f, rng.normal(size=4), method="Nelder-Mead", options={"maxiter": 2000, "xatol": 1e-11,
                                                                               "fatol": 1e-14})
            if r.fun < best[0]:
                q = r.x
                a = q[0:2] + 1j * q[2:4]
                a = a / np.linalg.norm(a)
                t = np.einsum("i,ijklmn,l->jkmn", a.conj(), Mc, a).reshape(4, 4)
                w, U = np.linalg.eigh((t + t.conj().T) / 2)
                u = U[:, 0] if sign < 0 else U[:, -1]
                v = np.moveaxis(np.kron(a, u).reshape(2, 2, 2), 0, cut).reshape(8)
                best = (r.fun, np.outer(v, v.conj()))
    return (best[0] if sign < 0 else -best[0]), best[1]


def run_sector(name, BASIS, ntrials):
    nb = len(BASIS)
    gram = np.array([np.real(np.trace(B1 @ B2)) for B1 in BASIS for B2 in BASIS]).reshape(nb, nb)
    ginv = np.linalg.inv(gram)

    def coords(X):
        return ginv @ np.array([np.real(np.trace(X @ B)) for B in BASIS])

    def op(y):
        return sum(c * B for c, B in zip(y, BASIS))

    trI = np.array([np.real(np.trace(B)) for B in BASIS])
    for trial in range(ntrials):
        v = rng.normal(size=nb)
        V = op(v)
        V = (V + V.conj().T) / 2
        # gen(V)
        gen = bisep_ext(V, +1)[0]
        for g in GT:
            for _s in range(8):
                r = minimize(lambda p: ratio(p, g, V, -1.0), rng.normal(size=24), jac=True, method="BFGS",
                             options={"maxiter": 3000, "gtol": 1e-11})
                gen = max(gen, -r.fun)
        # dual(V): max <V, Y> over Y in sector, tr Y = 1, <Y, G> >= 0 for priced G
        cons = [coords(np.outer(e, e)) for e in np.eye(8)] + [coords(g) for g in GT]
        for it in range(300):
            A = np.array(cons) @ gram
            res = linprog(-(v @ gram), A_ub=-A, b_ub=np.zeros(len(cons)), A_eq=[trI], b_eq=[1.0],
                          bounds=[(-30, 30)] * nb, method="highs")
            y = res.x
            Ym = op(y)
            Ym = (Ym + Ym.conj().T) / 2
            worst = (0.0, None)
            b, st = bisep_ext(Ym, -1)
            if b < worst[0]:
                worst = (b, st)
            for g in GT:
                for _s in range(6):
                    r = minimize(lambda p: ratio(p, g, Ym, 1.0), rng.normal(size=24), jac=True, method="BFGS",
                                 options={"maxiter": 3000, "gtol": 1e-11})
                    if r.fun < worst[0]:
                        k = kmat(r.x)
                        Yg = k @ g @ k.conj().T
                        worst = (r.fun, Yg / np.real(np.trace(Yg)))
            if worst[0] > -1e-9:
                break
            cons.append(coords(worst[1]))
        dual = -res.fun
        print("%s trial %d: gen(V) = %.8f  dual(V) = %.8f  gap = %.2e  (rounds %d, last pricing %.1e)"
              % (name, trial, gen, dual, dual - gen, it, worst[0]), flush=True)


which = sys.argv[1] if len(sys.argv) > 1 else "sector6"
run_sector(which, SECTORS[which], int(sys.argv[2]) if len(sys.argv) > 2 else 6)
print("done", file=sys.stderr)
