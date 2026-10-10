"""FLOATING POINT, EXPLORATION ONLY, CERTIFIES NOTHING.
EQ3-P exploration x1 -- self-pairing of SLOCC orbits of candidate three-copy elements.  Research only.

Question explored: N2 derived (p5) that a KT(6)-coherent three-copy cone is invariant under local filters
Ad(C0 (x) C1 (x) C2), C_k in GL(2, C) (SLOCC), and co-self-dual.  A candidate element x can lie in such a cone only if
its whole SLOCC orbit is self-positive: pair(x, Ad(C) x) >= 0 for every C.  EQ2-A's c = 1 candidate x_t = F + t 1
(t = 1/10) passes this test for local UNITARIES (orbit bound 9/50, a4d).  Here: does it pass for SLOCC?
  c = 1 (all pair marginals twins): pairing tr(X Y) (Euclidean self-duality, twin links).
  c = 0 (all pair marginals Q3): pairing tr(X Y^T); for real symmetric W this is tr(W Ad(conj C) W), and conj C ranges
  over GL(2)^3 with C, so the test is again min over C of tr(W Ad(C) W).
Method: minimize phi(C) = tr(x C x C^H) / ||C||_F^2 over C = C0 (x) C1 (x) C2 (24 real parameters), BFGS from
deterministic random starts.  A negative minimum is only a LEAD; it must be certified by an exact rational C in a
separate exact probe (p6).  A nonnegative minimum is NOT evidence of self-positivity (EQ2-A's x3 lesson).
Usage: python3 -I -B x1_slocc_orbit_float.py
"""
import numpy as np
from scipy.optimize import minimize

np.set_printoptions(precision=6, suppress=True)
k000 = np.zeros(8); k000[0] = 1
k111 = np.zeros(8); k111[7] = 1
P6 = np.eye(8) - np.outer(k000, k000) - np.outer(k111, k111)
Xc = np.outer(k000, k111) + np.outer(k111, k000)
F = P6 / 2 + Xc
ghz = (k000 + k111) / np.sqrt(2)
Gam = np.outer(ghz, ghz)


def build(p):
    Cs = []
    for k in range(3):
        q = p[8 * k: 8 * k + 8]
        Cs.append((q[:4] + 1j * q[4:]).reshape(2, 2))
    return np.kron(np.kron(Cs[0], Cs[1]), Cs[2])


def phi(p, x):
    C = build(p)
    n = np.real(np.trace(C @ C.conj().T))
    return np.real(np.trace(x @ C @ x @ C.conj().T)) / n


def explore(x, label, starts=60, seed=1):
    rng = np.random.default_rng(seed)
    best = (np.inf, None)
    for s in range(starts):
        p0 = rng.normal(size=24)
        r = minimize(phi, p0, args=(x,), method="BFGS", options={"maxiter": 4000, "gtol": 1e-12})
        if r.fun < best[0]:
            best = (r.fun, r.x)
    print(f"{label}: min phi over {starts} starts = {best[0]:.6e}")
    return best


res = {}
for t in (0.1, 0.15, 0.2, 0.3):
    res[("F", t)] = explore(F + t * np.eye(8), f"c=1  x = F + {t} 1")
for c in (1.5, 1.9, 2.0):
    res[("W", c)] = explore(np.eye(8) - c * Gam, f"c=0  W = 1 - {c} GHZ")
fbest = res[("F", 0.1)]
if fbest[0] < 0:
    C = build(fbest[1])
    blocks = [fbest[1][8 * k: 8 * k + 8] for k in range(3)]
    for k, q in enumerate(blocks):
        Ck = (q[:4] + 1j * q[4:]).reshape(2, 2)
        Ck = Ck / Ck[np.unravel_index(np.argmax(np.abs(Ck)), Ck.shape)]
        print(f"  lead C{k} (normalized by its largest entry):\n{Ck}")
print("x1 done (exploration only)")
