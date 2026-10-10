"""EQ4-SIX exploration y18 (c = 1 analogue of y16) -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  c = 1, sector Xi.  On rho = 1 the twirl of Lift(K_tw) is C_tw = {|c| <= phi_tw(u0, u1)},
phi_tw = min(2 u1, (u0 + 3 u1)/2) (s5 D; written: diagonal filters).  Off rho = 1: is Tw_Xi(Lift(K_tw)) = C_tw?
For fixed d, f_low(d) := max{c : (d, c) in Tw_Xi(Lift(K_tw))} by column generation:
  columns: Tw_Xi(Ad(k) g)/tr for g in {t0a = 1 - 2P_{0+} - 2P_{1+}, t0b = 1 - 2P_{0+} - 2P_{1-}, k0 = 1 - 2P_{0+} + 2P_{0-}}
  (representatives of the generator types of K_tw other than the separable pair sums) and k in GL(2,C)^3; Tw_Xi of the
  pure twin-hull elements |a><a|_k (x) PT_j(|chi><chi|) (all k, j), which contain the separable states;
  LP and duals as in y16.  Bracket: LP value <= f_low(d) <= y.d + eps tr(d).
DECISION RULE (fixed before the first run; for the lead only):
  control  : the full set reaches phi_tw at the rho = 1 control point d = (1, 1, 1, 1); the twin-only column set at t1
             is reported against the written value (3/2) u1 of Tw_Xi(B_tw) (s5 header (iv); a check of that claim);
  lead     : at each target rho != 1, report LP value, upper bracket after a verification re-pricing with 10x starts,
             phi_tw(u(d)) and psi_tw(d) (diagonal-filter upper bound, from the S10 slice of K_tw:
             |C| <= min((P0 + P1 + P2 + P3)/2, P1 + P2 + P3 - max_b P_b), written from the 36 inequalities).
  "gap lead" iff upper bracket < phi_tw - 1e-4 after verification; "no-gap lead" iff LP value > phi_tw - 1e-6.
  Stopping threshold eps < 1e-8, at most 200 rounds (as y16 run 2).
"""
import sys

import numpy as np
from scipy.optimize import linprog, minimize

TARGETS = {"ctrl": (1.0, 1.0, 1.0, 1.0), "t1": (4.0, 1.0, 1.0, 1.0), "t2": (1.0, 1.0, 1.0, 4.0),
           "t3": (1.0, 1.0, 2.0, 2.0), "t4": (2.0, 1.0, 1.0, 1.0), "t5": (1.0, 2.0, 1.0, 1.0),
           "t6": (16.0, 1.0, 1.0, 1.0)}
name = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "full"
rng = np.random.default_rng(2026100918 + sum(map(ord, name + mode)))
I8 = np.eye(8)
WT = np.array([bin(a).count("1") for a in range(8)])
BIN = np.array([1, 3, 3, 1])


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
GENS = {"t0a": I8 - 2 * P[0] - 2 * P[2], "t0b": I8 - 2 * P[0] - 2 * P[3], "k0": I8 - 2 * P[0] + 2 * P[1]}
C07 = np.zeros((8, 8))
C07[0, 7] = C07[7, 0] = 0.5


def column(X):
    X = X / np.real(np.trace(X))
    dg = np.real(np.diag(X))
    d = np.array([dg[WT == w].sum() / BIN[w] for w in range(4)])
    return d, abs(X[0, 7])


def gl2(p):
    return (p[0:4] + 1j * p[4:8]).reshape(2, 2)


def kmat(p):
    return np.kron(np.kron(gl2(p[0:8]), gl2(p[8:16])), gl2(p[16:24]))


def grad_k(p, g, M):
    A, B, C = gl2(p[0:8]), gl2(p[8:16]), gl2(p[16:24])
    k = np.kron(np.kron(A, B), C)
    G6 = (g @ k.conj().T @ M).T.reshape(2, 2, 2, 2, 2, 2)
    gA = np.einsum("abcxyz,by,cz->ax", G6, B, C)
    gB = np.einsum("abcxyz,ax,cz->by", G6, A, C)
    gC = np.einsum("abcxyz,ax,by->cz", G6, A, B)
    out = []
    for gm in (gA, gB, gC):
        out += list((2 * gm.real).reshape(4)) + list((-2 * gm.imag).reshape(4))
    return np.array(out)


def neg_ratio(p, g, M):
    k = kmat(p)
    Y = k @ g @ k.conj().T
    num = np.real(np.trace(M @ Y))
    den = np.real(np.trace(Y))
    return -num / den, -(grad_k(p, g, M) / den - num * grad_k(p, g, I8) / den ** 2)


def pt_pair(t, which):
    t4 = t.reshape(2, 2, 2, 2)
    return (t4.transpose(2, 1, 0, 3) if which == 0 else t4.transpose(0, 3, 2, 1)).reshape(4, 4)


def twin_max(M, starts):
    """max of <M, |a><a|_k (x) PT_j(|chi><chi|)> over pure twin-hull elements (single token k = cut, j in the pair)."""
    best = (-np.inf, None)
    M6 = M.reshape(2, 2, 2, 2, 2, 2)
    for cut in range(3):
        Mc = np.moveaxis(np.moveaxis(M6, cut, 0), cut + 3, 3)
        for which in (0, 1):
            for _ in range(starts):
                def f(q):
                    a = q[0:2] + 1j * q[2:4]
                    a = a / np.linalg.norm(a)
                    t = np.einsum("i,ijklmn,l->jkmn", a.conj(), Mc, a).reshape(4, 4)
                    t = pt_pair((t + t.conj().T) / 2, which)
                    return -np.linalg.eigvalsh((t + t.conj().T) / 2)[-1]
                r = minimize(f, rng.normal(size=4), method="Nelder-Mead",
                             options={"maxiter": 3000, "xatol": 1e-12, "fatol": 1e-15})
                if -r.fun > best[0]:
                    q = r.x
                    a = q[0:2] + 1j * q[2:4]
                    a = a / np.linalg.norm(a)
                    t = np.einsum("i,ijklmn,l->jkmn", a.conj(), Mc, a).reshape(4, 4)
                    t = pt_pair((t + t.conj().T) / 2, which)
                    w, U = np.linalg.eigh((t + t.conj().T) / 2)
                    B = pt_pair(np.outer(U[:, -1], U[:, -1].conj()), which)
                    T6 = np.einsum("ab,cdef->acdbef", np.outer(a, a.conj()), B.reshape(2, 2, 2, 2))
                    T6 = np.moveaxis(np.moveaxis(T6, 0, cut), 3, cut + 3)
                    best = (-r.fun, T6.reshape(8, 8))
    return best


def price(M, gens, starts, pool):
    """largest reduced cost over the generator orbits (BFGS from random and pooled starts) and twin-hull pure elements."""
    best = twin_max(M, max(2, starts // 5))
    for gname in gens:
        g = GENS[gname]
        inits = [rng.normal(size=24) for _ in range(starts)] + [p for (gn, p) in pool if gn == gname][-starts:]
        for p0 in inits:
            r = minimize(neg_ratio, p0, args=(g, M), jac=True, method="BFGS", options={"maxiter": 4000, "gtol": 1e-12})
            if -r.fun > best[0]:
                k = kmat(r.x)
                best = (-r.fun, k @ g @ k.conj().T)
                pool.append((gname, r.x))
    return best


def phi_A(d):
    u0, u1 = np.sqrt(d[0] * d[3]), np.sqrt(d[1] * d[2])
    return min(2 * u1, (u0 + 3 * u1) / 2), 1.5 * u1


def psi_diag(d):
    """inf over diagonal filters of phi_tw^{S10}(arithmetic pair means)/sqrt(mu1 mu2 mu3) (upper bound on Lift* cap Xi)."""
    x = np.array([d[WT[a]] for a in range(8)])
    best = np.inf
    for _ in range(40):
        def f(lm):
            mu = np.exp(lm)
            m = np.array([np.prod([mu[q] if (a >> (2 - q)) & 1 else 1.0 for q in range(3)]) for a in range(8)])
            y = x * m
            s = np.sqrt(np.prod(mu))
            P0 = (y[0] + y[7]) / 2 / s
            Pb = [(y[1] + y[6]) / 2 / s, (y[2] + y[5]) / 2 / s, (y[4] + y[3]) / 2 / s]
            return min((P0 + sum(Pb)) / 2, sum(Pb) - max(Pb))
        r = minimize(f, rng.normal(size=3), method="Nelder-Mead", options={"maxiter": 4000, "xatol": 1e-12,
                                                                           "fatol": 1e-15})
        best = min(best, r.fun)
    return best


d_t = np.array(TARGETS[name])
gens = [] if mode == "twin" else ["t0a", "t0b", "k0"]
cols = []
for w in range(4):
    e = np.zeros(4)
    e[w] = 1.0 / BIN[w]
    cols.append((e, 0.0))
for gname in gens:
    cols.append(column(GENS[gname]))
pool = []
phiA, twbs = phi_A(d_t)
rho = d_t[0] * d_t[2] ** 3 / (d_t[3] * d_t[1] ** 3)
print("c = 1 target %s mode %s: d = %s, rho = %.4f, phi_tw = %.6f, (3/2) u1 = %.6f" % (name, mode, d_t, rho, phiA, twbs),
      flush=True)
STARTS = 12
for it in range(200):
    A_eq = np.array([c[0] for c in cols]).T
    obj = -np.array([c[1] for c in cols])
    res = linprog(obj, A_eq=A_eq, b_eq=d_t, bounds=[(0, None)] * len(cols), method="highs")
    val = -res.fun
    y = -res.eqlin.marginals
    M = C07 - np.diag([y[WT[a]] / BIN[WT[a]] for a in range(8)])
    eps, X = price(M, gens, STARTS, pool)
    upper = y @ d_t + max(eps, 0.0) * float(BIN @ d_t)
    if it % 10 == 0 or eps < 1e-8:
        print("  round %d: LP value %.8f, upper bracket %.8f (eps %.2e)" % (it, val, upper, eps), flush=True)
    if eps < 1e-8:
        break
    cols.append(column(X))
# verification re-pricing with 10x starts
eps_v, Xv = price(M, gens, 10 * STARTS, pool)
upper_v = y @ d_t + max(eps_v, 0.0) * float(BIN @ d_t)
print("  final: LP value %.8f, verified upper bracket %.8f (eps %.2e), phi_tw %.8f, psi_tw %.8f"
      % (val, upper_v, eps_v, phiA, psi_diag(d_t)), flush=True)
used = [(round(lam, 6), np.round(cols[i][0], 4).tolist(), round(cols[i][1], 6)) for i, lam in enumerate(res.x)
        if lam > 1e-9]
print("  support:", used, flush=True)
print("  duals y (full precision):", [float(v) for v in y], flush=True)
if mode == "full":
    print("  reading: %s" % ("gap lead" if upper_v < phiA - 1e-4 else
                             ("no-gap lead" if val > phiA - 1e-6 else "inconclusive")), flush=True)
else:
    print("  control reading: twin-only LP %.8f vs (3/2) u1 %.8f" % (val, twbs), flush=True)
print("done", file=sys.stderr)
