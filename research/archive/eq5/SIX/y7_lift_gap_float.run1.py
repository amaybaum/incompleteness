"""EQ4-SIX exploration y7 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  Is Lift(K_A) (closed cone of all local-filter images of K_A's generators and of BS) equal to
its dual Lift(K_A)* = BS* cap (GL^3 W3)* cap (GL^3 kappa')* cap (GL^3 omega)* ?  (T-invariant, so co-self-duality of
Lift(K_A) <=> Lift = Lift*.)  Test, for random directions V (Hermitian, traceless part random):
  gen(V)  = sup over generators G = Ad(k) g / tr(Ad(k) g) and biseparable pure states of tr(V G)   (BFGS over k)
  dual(V) = max tr(V X) over X in Lift*, tr X = 1                                       (cutting planes, LP + pricing)
If Lift = Lift*, the two agree (the max of a linear functional over Lift cap {tr = 1} is attained at an extreme ray,
i.e. at a normalized generator or a limit of them).  dual(V) > gen(V) + tol is a lead for a gap Lift != Lift*.
Pricing: (i) block positivity across each cut (min over a in C^2 of lambda_min(<a| X |a>)); (ii) for each generator
type g in {W3, kappa', omega} min over k of tr(X Ad(k) g) / tr(Ad(k) g) (BFGS, exact gradient, many starts).
"""
import sys

import numpy as np
from scipy.optimize import linprog, minimize

rng = np.random.default_rng(2026100907)
S = [np.eye(2), np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0])]
PB = [np.kron(np.kron(S[a], S[b]), S[c]) for a in range(4) for b in range(4) for c in range(4)]


def coords(X):
    return np.array([np.real(np.trace(X @ P)) for P in PB])        # x_mu = tr(X sigma_mu); tr(XY) = x.y/8


def from_coords(x):
    return sum(xi * P for xi, P in zip(x, PB)) / 8


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
GTYPES = {"W3": 0.5 * I8 - P[0], "kappa'": 0.5 * I8 - P[0] + P[1], "omega": 0.5 * I8 - P[0] + P[2],
          "omega4": 0.5 * I8 - P[0] + P[4], "omega6": 0.5 * I8 - P[0] + P[6]}


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


def ratio_and_grad(p, g, M):
    """f(k) = tr(M Ad(k) g) / tr(Ad(k) g) and gradient."""
    k = kmat(p)
    Y = k @ g @ k.conj().T
    num = np.real(np.trace(M @ Y))
    den = np.real(np.trace(Y))
    gn = grad_k(p, g, M)
    gd = grad_k(p, g, I8)
    return num / den, gn / den - num * gd / den ** 2


def opt_over_k(g, M, sign, starts):
    best = (np.inf, None)
    for _ in range(starts):
        r = minimize(lambda p: tuple(sign * t for t in ratio_and_grad(p, g, M)), rng.normal(size=24), jac=True,
                     method="BFGS", options={"maxiter": 3000, "gtol": 1e-10})
        if r.fun < best[0]:
            best = (r.fun, r.x)
    return sign * best[0], best[1]


def bisep_extreme(M, sign):
    """sign = +1: max over biseparable pure states of <phi|M|phi>; sign = -1: min.  Returns value and state."""
    best = (-np.inf, None)
    for cut in range(3):
        for _ in range(6):
            def f(q):
                a = q[0:2] + 1j * q[2:4]
                a = a / np.linalg.norm(a)
                t = np.einsum("i,ijklmn,l->jkmn", a.conj(), np.moveaxis(np.moveaxis(M.reshape(2, 2, 2, 2, 2, 2), cut, 0),
                                                                          cut + 3, 3), a).reshape(4, 4)
                w, U = np.linalg.eigh(sign * (t + t.conj().T) / 2)
                return -w[-1]
            r = minimize(f, rng.normal(size=4), method="Nelder-Mead", options={"maxiter": 2000, "xatol": 1e-10,
                                                                               "fatol": 1e-13})
            if -r.fun > best[0]:
                q = r.x
                a = q[0:2] + 1j * q[2:4]
                a = a / np.linalg.norm(a)
                t = np.einsum("i,ijklmn,l->jkmn", a.conj(), np.moveaxis(np.moveaxis(M.reshape(2, 2, 2, 2, 2, 2), cut, 0),
                                                                         cut + 3, 3), a).reshape(4, 4)
                w, U = np.linalg.eigh(sign * (t + t.conj().T) / 2)
                chi = U[:, -1]
                v = np.moveaxis(np.kron(a, chi).reshape(2, 2, 2), 0, cut).reshape(8)
                best = (-r.fun, v)
    return sign * best[0], best[1]


def gen_max(V, starts=6):
    best, _ = bisep_extreme(V, +1)
    for nm, g in GTYPES.items():
        val, _ = opt_over_k(g, V, -1, starts)
        best = max(best, val)
    return best


def dual_max(V, iters=400, tol=1e-7):
    cons = [coords(np.outer(v, v.conj())) for v in np.eye(8)]
    for nm, g in GTYPES.items():
        cons.append(coords(g))
    vc = coords(V)
    for it in range(iters):
        A = -np.array(cons) / 8
        res = linprog(-vc / 8, A_ub=A, b_ub=np.zeros(len(cons)), A_eq=np.eye(64)[[0]], b_eq=[1.0],
                      bounds=[(-40, 40)] * 64, method="highs")
        x = res.x
        X = from_coords(x)
        worst = (0.0, None)
        val, phi = bisep_extreme(X, -1)
        if val < worst[0]:
            worst = (val, coords(np.outer(phi, phi.conj())))
        for nm, g in GTYPES.items():
            val, p = opt_over_k(g, X, +1, 4)
            if val < worst[0]:
                k = kmat(p)
                worst = (val, coords(k @ g @ k.conj().T / np.real(np.trace(k @ g @ k.conj().T))))
        if worst[0] > -tol:
            return -res.fun, it, X
        cons.append(worst[1])
    return -res.fun, iters, X


for trial in range(int(sys.argv[1]) if len(sys.argv) > 1 else 8):
    H = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))
    V = (H + H.conj().T) / 2
    V = V - np.trace(V) / 8 * I8
    g = gen_max(V)
    d, its, X = dual_max(V)
    print("trial %d: gen(V) = %.6f  dual(V) = %.6f  gap = %.2e  (cutting-plane iterations %d)" % (trial, g, d, d - g, its),
          flush=True)
print("done", file=sys.stderr)
