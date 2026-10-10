"""EQ4-SIX exploration y20 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  Can C_A be the Xi-section of a K_A-lift off rho = 1?  Necessary, for the boundary point
X_t = (d_t, phi_A(u(d_t))) of C_A at a target with rho != 1:
  (i)  X_t in Lift(K_A)*:  min over filters k of <X_t, Ad(k) g>/tr(Ad(k) g) >= 0 for g in {W3, kappa, omega}, and
       <phi|X_t|phi> >= 0 on biseparable pure states;
  (ii) the filter orbit of X_t is self-positive:  min over k of <X_t, Ad(k) X_t>/tr(Ad(k) X_t) >= 0.
Same search code as y19 (dense matrices, k_j = expm(H_j), random search + Nelder-Mead, S_3-symmetric filters).
DECISION RULE (fixed before the first run; for the lead only): "C_A section survives at d_t" iff every minimum is
>= -1e-7; "C_A section excluded at d_t" iff some minimum is < -1e-5 (then the minimizing filter is printed);
otherwise inconclusive.  Countercontrol: X_t with the coherence scaled by 1.05 (outside C_A) must give a negative
minimum in (i).
"""

import sys

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

TARGETS = {"t1": (4.0, 1.0, 1.0, 1.0), "t3": (1.0, 1.0, 2.0, 2.0), "t5": (1.0, 2.0, 1.0, 1.0)}
name = sys.argv[1]
rng = np.random.default_rng(2026100920 + sum(map(ord, name)))
I8 = np.eye(8)
WT = np.array([bin(a).count("1") for a in range(8)])
BIN = np.array([1, 3, 3, 1])


def ghz_proj(b, t):
    b1, b2 = b >> 1, b & 1
    v = np.zeros(8)
    v[2 * b1 + b2] = 1
    v[4 + 2 * (1 - b1) + (1 - b2)] = 1 if t == 0 else -1
    return np.outer(v, v) / 2


P0p, P0m, P1p = ghz_proj(0, 0), ghz_proj(0, 1), ghz_proj(1, 0)
GENS = {"W3": 0.5 * I8 - P0p, "kappa": 0.5 * I8 + P0p - P0m, "omega": 0.5 * I8 - P0p + P1p}


def make_Y(y, cscale=1.0):
    Y = np.diag([y[WT[a]] / BIN[WT[a]] for a in range(8)]).astype(complex)
    Y[0, 7] = Y[7, 0] = -0.5 * cscale
    return Y


def filt(q):
    ks = []
    for j in range(3):
        H = (q[8 * j:8 * j + 4] + 1j * q[8 * j + 4:8 * j + 8]).reshape(2, 2)
        ks.append(expm(H))
    return np.kron(np.kron(ks[0], ks[1]), ks[2])


def ratio(Y, g, k):
    X = k @ g @ k.conj().T
    return np.real(np.trace(Y @ X)) / np.real(np.trace(X))


def min_orbit(Y, g):
    best = []
    for _ in range(20000):
        q = rng.normal(size=24) * rng.choice([0.3, 1.0, 2.0])
        best.append((ratio(Y, g, filt(q)), q))
    best.sort(key=lambda t: t[0])
    out = best[0][0]
    for val, q in best[:30]:
        r = minimize(lambda z: ratio(Y, g, filt(z)), q, method="Nelder-Mead",
                     options={"maxiter": 20000, "maxfev": 20000, "xatol": 1e-10, "fatol": 1e-14})
        out = min(out, r.fun)
    # S_3-symmetric filters k (x) k (x) k
    for _ in range(40):
        q0 = rng.normal(size=8)
        f = lambda z: ratio(Y, g, filt(np.concatenate([z, z, z])))
        r = minimize(f, q0, method="Nelder-Mead", options={"maxiter": 20000, "xatol": 1e-11, "fatol": 1e-15})
        out = min(out, r.fun)
    return out


def min_bisep(Y):
    out = np.inf
    for cut in range(3):
        def f(z):
            a = z[0:2] + 1j * z[2:4]
            b = z[4:8] + 1j * z[8:12]
            a = a / np.linalg.norm(a)
            b = b / np.linalg.norm(b)
            v = np.moveaxis(np.kron(a, b).reshape(2, 2, 2), 0, cut).reshape(8)
            return np.real(v.conj() @ Y @ v)
        vals = [(f(z), z) for z in rng.normal(size=(3000, 12))]
        vals.sort(key=lambda t: t[0])
        for val, z in vals[:10]:
            r = minimize(f, z, method="Nelder-Mead", options={"maxiter": 20000, "xatol": 1e-11, "fatol": 1e-15})
            out = min(out, r.fun)
    return out


d_t = np.array(TARGETS[name])
ut0, ut1 = np.sqrt(d_t[0] * d_t[3]), np.sqrt(d_t[1] * d_t[2])
phit = min(ut0 + ut1, 3 * ut1, (ut0 + 3 * ut1) / 2)


def make_X(cscale=1.0):
    X = np.diag([d_t[WT[a]] for a in range(8)]).astype(complex)
    X[0, 7] = X[7, 0] = phit * cscale
    return X


Xt = make_X()
print("target %s: X_t = (d = %s, c = %.10f), rho = %.4f" % (name, d_t, phit,
      d_t[0] * d_t[2] ** 3 / (d_t[3] * d_t[1] ** 3)), flush=True)
for gname, g in GENS.items():
    print("  (i)  min over filters of <X_t, Ad(k) %s>/tr = %.3e" % (gname, min_orbit(Xt, g)), flush=True)
print("  (i)  min over biseparable pure states of <phi|X_t|phi> = %.3e" % min_bisep(Xt), flush=True)
print("  (ii) min over filters of <X_t, Ad(k) X_t>/tr = %.3e" % min_orbit(Xt, Xt), flush=True)
Xc = make_X(1.05)
cc = min(min_orbit(Xc, g) for g in GENS.values())
print("  countercontrol (coherence x 1.05): min over the generator orbits = %.3e" % cc, flush=True)
print("done", file=sys.stderr)
