"""u5_level2_N.py -- thread U, level (ii): [N, numerical] exploration only; certifies nothing.

Question: is the orbit surgery K_Z = (Q3 ∩ Z*) + cone(Z), Z = {a E00 + s1 E13 + s2 E22 : s1, s2 = ±1}, self-dual?
Equivalently: is K_Z* = (Q3 + cone Z) ∩ Z* self-positive?  We minimise <y, h> over y, h ∈ K_Z* (trace-normalised
parametrisation y = q + sum sigma_s z_s, q = M M^H / tr, sigma >= 0, Z*-constraints by penalty) from fixed seeds.
Decision rule (fixed before the first run): this script prints only rounded minima per value of a.  A minimum
below -1e-6 at a feasible pair is a LEAD for an exact certificate (not a result); a minimum >= -1e-6 over all
starts is reported as "no violation found [N]" and is never quoted as evidence of self-duality.
Output is rounded to 4 decimals; seeds are fixed so the replay is byte-identical on this machine.
"""
import numpy as np
from scipy.optimize import minimize

X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
XZ, YY = np.kron(X, Z), np.kron(Y, Y)
I4 = np.eye(4, dtype=complex)


def ip(A, B):
    return 4.0 * np.real(np.trace(A @ B))


def zs(a):
    return [(a * I4 + s1 * XZ + s2 * YY) / 4.0 for s1 in (1, -1) for s2 in (1, -1)]


def unpack(p, k):
    M = (p[0:16] + 1j * p[16:32]).reshape(4, 4)
    q = M @ M.conj().T
    q = q / np.real(np.trace(q))
    sig = p[32:36] ** 2
    return q + sum(sig[i] * k[i] for i in range(4))


def objective(p, k):
    y = unpack(p[0:36], k)
    h = unpack(p[36:72], k)
    pen = 0.0
    for w in (y, h):
        for zz in k:
            v = ip(w, zz)
            if v < 0:
                pen += 1e3 * v * v
    ny = np.sqrt(ip(y, y))
    nh = np.sqrt(ip(h, h))
    return ip(y, h) / (ny * nh) + pen


def run(a, nstart):
    k = zs(a)
    rng = np.random.default_rng(12345)
    best = None
    for _ in range(nstart):
        p0 = rng.normal(size=72)
        r = minimize(objective, p0, args=(k,), method="BFGS", options={"maxiter": 1500, "gtol": 1e-10})
        y = unpack(r.x[0:36], k)
        h = unpack(r.x[36:72], k)
        feas = min(min(ip(y, zz) for zz in k), min(ip(h, zz) for zz in k))
        val = ip(y, h) / np.sqrt(ip(y, y) * ip(h, h))
        if feas >= -1e-7 and (best is None or val < best):
            best = val
    return best


print("[N] level-(ii) orbit surgery: min normalised <y, h> over y, h in K_Z* (feasible starts only)")
for a in (1.0, 1.25, 1.5, 1.75):
    b = run(a, 8)
    tag = "none feasible" if b is None else "%.4f" % b
    print("[N] a = %.2f: Gram min a^2 - 2 = %.4f; min <y,h>/|y||h| = %s" % (a, a * a - 2, tag))
print("[N] end of exploration (no VERDICT: numerical leads only)")
