"""EQ4-SIX exploration y15 (= y14, then an extensive re-verification of the final separating Y) -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  Is the W witness Wwit = (2/3) I - |W><W| (in Z, hence in Lift(K_A)*, s2) in Lift(K_A)?
Sector6 = operators invariant under token permutations S_3 and the phases diag(1, e^{i theta})^{(x)3}: block diagonal
in the Hamming weight, S_3-symmetric: coordinates (d0, aW1, b1, aW2, b2, d3) with
X = d0 |000><000| + aW1 |W><W| + b1 (Pi_1 - |W><W|) + aW2 |Wb><Wb| + b2 (Pi_2 - |Wb><Wb|) + d3 |111><111|.
Tw6 (the average over S_3 and the phases) is a self-adjoint average of symmetries of Lift(K_A), so
Wwit in Lift(K_A)  <=>  no Y in sector6 with <Y, Wwit> < 0 and <Y, Ad(k) g> >= 0 for all filters k and generators g.
Cutting planes in 6 dimensions: LP over Y (box |Y_coords| <= 1), pricing = min over k of <Y, Ad(k) g>/tr(Ad(k) g)
for g in {W3, kappa', omega(3 fibres)} and min over biseparable pure states (many starts).  Converged pricing with
LP value < 0 is a lead for Wwit not in Lift(K_A) (a gap); LP value -> 0 is a lead for membership.
"""
import sys

import numpy as np
from scipy.optimize import linprog, minimize

rng = np.random.default_rng(2026100914)
I8 = np.eye(8)
W = np.array([bin(a).count("1") for a in range(8)])
wv = np.zeros(8)
wv[[1, 2, 4]] = 1 / np.sqrt(3)
wbv = np.zeros(8)
wbv[[3, 5, 6]] = 1 / np.sqrt(3)
PW = np.outer(wv, wv)
PWb = np.outer(wbv, wbv)
Pi = [np.diag((W == w).astype(float)) for w in range(4)]
BASIS = [Pi[0], PW, Pi[1] - PW, PWb, Pi[2] - PWb, Pi[3]]
NORMS = [np.real(np.trace(B @ B)) for B in BASIS]


def coords6(X):
    return np.array([np.real(np.trace(X @ B)) / n for B, n in zip(BASIS, NORMS)])


def op6(y):
    return sum(c * B for c, B in zip(y, BASIS))


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
GT = [0.5 * I8 - P[0]]
Wwit = (2.0 / 3) * I8 - PW


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


def ratio(p, g, M):
    k = kmat(p)
    Y = k @ g @ k.conj().T
    num = np.real(np.trace(M @ Y))
    den = np.real(np.trace(Y))
    return num / den, grad_k(p, g, M) / den - num * grad_k(p, g, I8) / den ** 2


def bisep_min(M):
    best = (np.inf, None)
    M6 = M.reshape(2, 2, 2, 2, 2, 2)
    for cut in range(3):
        Mc = np.moveaxis(np.moveaxis(M6, cut, 0), cut + 3, 3)
        for _ in range(6):
            def f(q):
                a = q[0:2] + 1j * q[2:4]
                a = a / np.linalg.norm(a)
                t = np.einsum("i,ijklmn,l->jkmn", a.conj(), Mc, a).reshape(4, 4)
                return np.linalg.eigvalsh((t + t.conj().T) / 2)[0]
            r = minimize(f, rng.normal(size=4), method="Nelder-Mead", options={"maxiter": 2000, "xatol": 1e-11,
                                                                               "fatol": 1e-14})
            if r.fun < best[0]:
                q = r.x
                a = q[0:2] + 1j * q[2:4]
                a = a / np.linalg.norm(a)
                t = np.einsum("i,ijklmn,l->jkmn", a.conj(), Mc, a).reshape(4, 4)
                w, U = np.linalg.eigh((t + t.conj().T) / 2)
                v = np.moveaxis(np.kron(a, U[:, 0]).reshape(2, 2, 2), 0, cut).reshape(8)
                best = (r.fun, np.outer(v, v.conj()))
    return best


target = coords6(Wwit)
print("Wwit sector6 coordinates:", np.round(target, 6), flush=True)
cols = [coords6(np.outer(v, v)) for v in np.eye(8)] + [coords6(g) for g in GT]
for _ in range(200):
    k = kmat(rng.normal(size=24))
    g = GT[rng.integers(len(GT))]
    Y = k @ g @ k.conj().T
    cols.append(coords6(Y / np.real(np.trace(Y))))
gram = np.array([np.real(np.trace(B1 @ B2)) for B1 in BASIS for B2 in BASIS]).reshape(6, 6)
for it in range(400):
    A = np.array(cols) @ gram            # <Y, G> = y . gram . g  (Y = op6(y), G in sector6 coordinates)
    res = linprog(target @ gram, A_ub=-A, b_ub=np.zeros(len(cols)), bounds=[(-1, 1)] * 6, method="highs")
    y = res.x
    Ym = op6(y)
    worst = (0.0, None)
    b, st = bisep_min(Ym)
    if b < worst[0]:
        worst = (b, st)
    for g in GT:
        for _s in range(6):
            r = minimize(lambda p: ratio(p, g, Ym), rng.normal(size=24), jac=True, method="BFGS",
                         options={"maxiter": 3000, "gtol": 1e-11})
            if r.fun < worst[0]:
                k = kmat(r.x)
                Yg = k @ g @ k.conj().T
                worst = (r.fun, Yg / np.real(np.trace(Yg)))
    if it % 20 == 0 or worst[0] > -1e-9:
        print("round %d: LP value <Y, Wwit> = %.6e ; pricing min %.3e" % (it, res.fun, worst[0]), flush=True)
    if worst[0] > -1e-9:
        print("converged: Y coords", np.round(y, 6), flush=True)
        break
    cols.append(coords6(worst[1]))
# extensive re-verification of the final Y: 400 BFGS starts for the W3 orbit, 40 bisep starts per cut
Yf = op6(y)
yn = float(np.real(np.trace(Yf)))
print("final Y coords (full precision):", [float("%.15g" % c) for c in y], " tr Y = %.12g" % yn, flush=True)
print("<Y, Wwit> / tr Y = %.6e" % (float(np.real(np.trace(Yf @ Wwit))) / yn), flush=True)
best = np.inf
for _s in range(400):
    r = minimize(lambda p: ratio(p, GT[0], Yf), rng.normal(size=24), jac=True, method="BFGS",
                 options={"maxiter": 5000, "gtol": 1e-13})
    best = min(best, r.fun)
print("re-verification: min over 400 starts of <Y, Ad(k) W3>/tr(Ad(k) W3) = %.6e" % best, flush=True)
bb = min(bisep_min(Yf)[0] for _ in range(6))
print("re-verification: min over biseparable pure states of <phi|Y|phi> = %.6e" % bb, flush=True)
print("eigenvalues of Y:", np.round(np.linalg.eigvalsh(Yf), 6), flush=True)
print("done", file=sys.stderr)
