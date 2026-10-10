"""EQ4-SIX exploration y10 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  Projector witnesses W_psi = lam(psi) I - |psi><psi| (lam = largest squared Schmidt
coefficient of psi over the three cuts) lie in Z (PT_j W_psi = lam I - PT_j(psi psi^dag) >= 0, since the largest
eigenvalue of PT_j of a pure state is its largest squared Schmidt coefficient), hence in Lift(K_A)* (s2, exact).
Is W_psi in Lift(K_A)?  Column generation / Farkas: minimize <Y, W_psi> over Y with <Y, G> >= 0 for the current
generator set G and |Y_coords| <= 1; pricing adds the filtered generator (or biseparable pure state) with the most
negative <Y, G>/tr(G).  Stop when pricing finds nothing below -tol: then Y is (approximately) in Lift(K_A)* and
<Y, W_psi> < 0 is a lead that W_psi is not in Lift(K_A), i.e. Lift(K_A) != Lift(K_A)* (a gap); an LP optimum 0 means
W_psi is (approximately) in the current cone.
"""
import sys
from multiprocessing import Pool

import numpy as np
from scipy.optimize import linprog, minimize

S = [np.eye(2), np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0])]
PB = [np.kron(np.kron(S[a], S[b]), S[c]) for a in range(4) for b in range(4) for c in range(4)]
I8 = np.eye(8)


def coords(X):
    return np.array([np.real(np.trace(X @ P)) for P in PB])


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


def ratio(p, g, M):
    k = kmat(p)
    Y = k @ g @ k.conj().T
    num = np.real(np.trace(M @ Y))
    den = np.real(np.trace(Y))
    return num / den, grad_k(p, g, M) / den - num * grad_k(p, g, I8) / den ** 2


def bisep_min(M, rng):
    best = (np.inf, None)
    M6 = M.reshape(2, 2, 2, 2, 2, 2)
    for cut in range(3):
        Mc = np.moveaxis(np.moveaxis(M6, cut, 0), cut + 3, 3)
        for _ in range(5):
            def f(q):
                a = q[0:2] + 1j * q[2:4]
                a = a / np.linalg.norm(a)
                t = np.einsum("i,ijklmn,l->jkmn", a.conj(), Mc, a).reshape(4, 4)
                return np.linalg.eigvalsh((t + t.conj().T) / 2)[0]
            r = minimize(f, rng.normal(size=4), method="Nelder-Mead", options={"maxiter": 1500, "xatol": 1e-10,
                                                                               "fatol": 1e-13})
            if r.fun < best[0]:
                q = r.x
                a = q[0:2] + 1j * q[2:4]
                a = a / np.linalg.norm(a)
                t = np.einsum("i,ijklmn,l->jkmn", a.conj(), Mc, a).reshape(4, 4)
                w, U = np.linalg.eigh((t + t.conj().T) / 2)
                v = np.moveaxis(np.kron(a, U[:, 0]).reshape(2, 2, 2), 0, cut).reshape(8)
                best = (r.fun, np.outer(v, v.conj()))
    return best


def witness(psi):
    psi = psi / np.linalg.norm(psi)
    t = psi.reshape(2, 2, 2)
    lam = 0
    for ax in range(3):
        lam = max(lam, np.linalg.svd(np.moveaxis(t, ax, 0).reshape(2, 4), compute_uv=False)[0] ** 2)
    return lam * I8 - np.outer(psi, psi.conj())


def test(seed):
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=8) + 1j * rng.normal(size=8)
    X = witness(psi)
    xc = coords(X)
    cols = [coords(np.outer(v, v)) for v in np.eye(8)] + [coords(g) for g in GT]
    for _ in range(40):
        k = kmat(rng.normal(size=24))
        g = GT[rng.integers(len(GT))]
        Y = k @ g @ k.conj().T
        cols.append(coords(Y / np.real(np.trace(Y))))
    hist = []
    for it in range(300):
        A = np.array(cols)
        res = linprog(xc, A_ub=-A, b_ub=np.zeros(len(cols)), bounds=[(-1, 1)] * 64, method="highs")
        yc = res.x
        val = res.fun
        Ym = from_coords(yc) * 8      # <Y, G> = yc . coords(G) / 8 ... use the matrix with tr(Ym G) = yc . coords(G)
        worst = (0.0, None)
        b, st = bisep_min(Ym, rng)
        if b < worst[0]:
            worst = (b, st)
        for g in GT:
            for _s in range(3):
                r = minimize(lambda p: ratio(p, g, Ym), rng.normal(size=24), jac=True, method="BFGS",
                             options={"maxiter": 2000, "gtol": 1e-10})
                if r.fun < worst[0]:
                    k = kmat(r.x)
                    Y = k @ g @ k.conj().T
                    worst = (r.fun, Y / np.real(np.trace(Y)))
        hist.append((val, worst[0]))
        if worst[0] > -1e-7:
            return seed, val, it, worst[0]
        cols.append(coords(worst[1]))
    return seed, val, 300, worst[0]


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    with Pool(3) as pool:
        for seed, val, it, pr in pool.imap_unordered(test, range(2026101000, 2026101000 + n)):
            print("psi seed %d: min <Y, W_psi> over (approx.) Lift(K_A)* with |Y| <= 1 = %.3e after %d pricing rounds "
                  "(last pricing min %.1e)" % (seed, val, it, pr), flush=True)
    print("done", file=sys.stderr)
