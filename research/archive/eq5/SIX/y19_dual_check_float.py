"""EQ4-SIX exploration y19 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  Independent re-check of the y16 run-2 duals.  For a target d_t, y16's LP duals y define
  Y = sum_a (y_wt(a) / C(3, wt(a))) |a><a| - (1/2)(|000><111| + |111><000|)   (an element of Xi),
with <Y, X> = y.d(X) - Re c(X) on Xi.  y16 claims (float) Y in Lift(K_A)* up to eps ~ 1e-8 and <Y, X_t> < 0 for
X_t = (d_t, phi_A(u(d_t))) in C_A.  Here, with code independent of y16's pricing (dense 8 x 8 matrices; filters
parametrized as k_j = expm(H_j), H_j complex 2 x 2; random search over 20000 filters with log-normal scales, then
Nelder-Mead from the 30 best; S_3-symmetric filters k (x) k (x) k separately; biseparable pure states by random
sampling plus Nelder-Mead):
  report min over (k, g) of <Y, Ad(k) g>/tr(Ad(k) g), g in {W3, kappa, omega}, and min over biseparable pure states,
  and the moduli (u0, u1, |c|) and rho of Y.
DECISION RULE (fixed before the first run; for the lead only): the y16 lead "Y in Lift(K_A)*" survives iff every
reported minimum is >= -1e-7; otherwise it is withdrawn.
Countercontrol: the same search applied to Y' = Y with the coherence scaled by 1.05 must find a negative value
(a search that cannot see a slightly larger coherence is not testing anything).
"""
import sys

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

DUALS = {"t3": [0.35628263794720455, 1.2133877116503091, 0.20603472212519652, 0.31186223417779774],
         "t5": [0.4498730958227585, 0.2327999168148535, 1.0738835378126472, 0.24698321636537313]}
TARGETS = {"t3": (1.0, 1.0, 2.0, 2.0), "t5": (1.0, 2.0, 1.0, 1.0)}
name = sys.argv[1]
rng = np.random.default_rng(2026100919 + sum(map(ord, name)))
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


y = DUALS[name]
d_t = np.array(TARGETS[name])
Y = make_Y(y)
dY = np.array([y[w] / BIN[w] for w in range(4)])
u0, u1 = np.sqrt(dY[0] * dY[3]), np.sqrt(dY[1] * dY[2])
rhoY = dY[0] * dY[2] ** 3 / (dY[3] * dY[1] ** 3)
ut0, ut1 = np.sqrt(d_t[0] * d_t[3]), np.sqrt(d_t[1] * d_t[2])
phit = min(ut0 + ut1, 3 * ut1, (ut0 + 3 * ut1) / 2)
print("target %s: Y has u0 = %.10f, u1 = %.10f, |c| = 0.5, rho = %.6e; phi_A(u_Y) = %.10f" %
      (name, u0, u1, rhoY, min(u0 + u1, 3 * u1, (u0 + 3 * u1) / 2)), flush=True)
print("  <Y, X_t> = y.d_t - phi_A(u(d_t)) = %.10f" % (np.dot(y, d_t) - phit), flush=True)
for gname, g in GENS.items():
    print("  min over filters of <Y, Ad(k) %s>/tr = %.3e" % (gname, min_orbit(Y, g)), flush=True)
print("  min over biseparable pure states of <phi|Y|phi> = %.3e" % min_bisep(Y), flush=True)
Yc = make_Y(y, 1.05)
cc = min(min_orbit(Yc, g) for g in GENS.values())
print("  countercontrol (coherence x 1.05): min over the generator orbits = %.3e" % cc, flush=True)
print("done", file=sys.stderr)
