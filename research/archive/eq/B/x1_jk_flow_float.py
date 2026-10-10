"""EXPLORATION ONLY (floating point; certifies nothing).

The J/K one-parameter family G_t on W d, transcribed from the QT controlled-U(1) group through CNOT:
  classical sector: G_t(hom z (x) Y) = hom z (x) Y,  G_t(hom(-z) (x) Y) = hom(-z) (x) R_t Y,
                    R_t = P+ + cos t P- + sin t K P-;
  tangent sector:   G_t(c (x) Y) = c (x) A_t Y + Jc (x) B_t Y,
                    A_t = (1+cos t)/2 I + (1-cos t)/2 X P+ + (sin t/2) K P-,
                    B_t = (sin t/2)(P+ - X P+) + (sin t/2) P- + (1-cos t)/2 K P-.
At t = pi this is the J/K gate (gC5 at d = 5, cnot at d = 3).
Question explored: is G_t two-sided positive on product states (images in maxCone) for every t, at d = 5, 7?
Method: minimise pairVal(e, f, G_t(hom x (x) hom y)) over unit x, y and extreme effects e = (1, a), f = (1, b),
|a| = |b| = 1, by random restarts + local search.
"""
import numpy as np
import sys

rng = np.random.default_rng(12345)


def jk_data(d):
    """Return (n, E+ indices, X, K, J) for the J/K structure at odd d = 2m+1.

    Homogeneous indices: 0 = u, 1 = x, d = z, tangent T = 1..d-1.
    E+ = {u, x}; E- = {2..d}. X swaps u <-> x. K pairs (2,d) as y->z->-y and the rest (3,4),(5,6),... .
    J pairs tangent (1,2), (3,4), ... as a -> b -> -a.
    For d = 5 this reproduces gC5's (y, w1, w2, z) = (2, 3, 4, 5) structure.
    """
    n = d + 1
    X = np.zeros((n, n)); X[0, 1] = X[1, 0] = 1.0
    K = np.zeros((n, n))
    # y = 2 -> z = d -> -y
    K[d, 2] = 1.0; K[2, d] = -1.0
    for a in range(3, d - 1, 2):
        K[a + 1, a] = 1.0; K[a, a + 1] = -1.0
    J = np.zeros((n, n))
    for a in range(1, d - 1, 2):
        J[a + 1, a] = 1.0; J[a, a + 1] = -1.0
    Pp = np.zeros((n, n)); Pp[0, 0] = Pp[1, 1] = 1.0
    Pm = np.eye(n) - Pp
    return n, X, K, J, Pp, Pm


def gate(d, t):
    n, X, K, J, Pp, Pm = jk_data(d)
    c, s = np.cos(t), np.sin(t)
    R = Pp + c * Pm + s * K @ Pm
    A = (1 + c) / 2 * np.eye(n) + (1 - c) / 2 * X @ Pp + s / 2 * K @ Pm
    B = s / 2 * (Pp - X @ Pp) + s / 2 * Pm + (1 - c) / 2 * K @ Pm
    G = np.zeros((n * n, n * n))
    hz = np.zeros(n); hz[0] = 1; hz[d] = 1
    hmz = np.zeros(n); hmz[0] = 1; hmz[d] = -1
    # control basis: hz, hmz, tangent e_1..e_{d-1}
    Cb = [hz, hmz] + [np.eye(n)[k] for k in range(1, d)]
    Bm = np.array(Cb).T
    Binv = np.linalg.inv(Bm)
    for mu in range(n):
        coeff = Binv[:, mu]
        for nu in range(n):
            Y = np.eye(n)[nu]
            out = np.zeros((n, n))
            for k, ck in enumerate(coeff):
                if abs(ck) < 1e-15:
                    continue
                if k == 0:
                    img = np.outer(hz, Y)
                elif k == 1:
                    img = np.outer(hmz, R @ Y)
                else:
                    cvec = Cb[k]
                    img = np.outer(cvec, A @ Y) + np.outer(J @ cvec, B @ Y)
                out += ck * img
            G[:, mu * n + nu] = out.reshape(-1)
    return G


def value(G, n, x, y, a, b):
    hx = np.concatenate([[1.0], x]); hy = np.concatenate([[1.0], y])
    w = (G @ np.outer(hx, hy).reshape(-1)).reshape(n, n)
    e = np.concatenate([[1.0], a]); f = np.concatenate([[1.0], b])
    return e @ w @ f


def unit(v):
    return v / np.linalg.norm(v)


def minimise(G, d, iters=3000, restarts=60):
    n = d + 1
    best = (np.inf, None)
    for r in range(restarts):
        x, y, a, b = (unit(rng.normal(size=d)) for _ in range(4))
        cur = value(G, n, x, y, a, b)
        step = 0.5
        for it in range(iters):
            cand = [unit(v + step * rng.normal(size=d)) for v in (x, y, a, b)]
            val = value(G, n, *cand)
            if val < cur:
                x, y, a, b = cand
                cur = val
            else:
                step *= 0.995
            if step < 1e-6:
                break
        if cur < best[0]:
            best = (cur, (x, y, a, b))
    return best


if __name__ == "__main__":
    for d in (3, 5, 7):
        for t in (np.pi / 2, 2 * np.pi / 3, 1.0, np.pi, 2.5, 4.0):
            G = gate(d, t)
            Gi = np.linalg.inv(G)
            m1, _ = minimise(G, d, iters=1500, restarts=25)
            m2, _ = minimise(Gi, d, iters=1500, restarts=25)
            print(f"d={d} t={t:.4f}  min posFwd value {m1:+.3e}   min posInv value {m2:+.3e}")
        sys.stdout.flush()
