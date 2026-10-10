"""EQ4-P exploration x7 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead-finding only).  If a GHZ-diagonal y lies in K3, then (five-token filters) Ad(k) y lies in K3 for every
local k, and co-self-duality (K3 = T(K3*), T(y) = y for real symmetric y) requires
    tr( y Ad(m) y ) >= 0   for every local m = A (x) B (x) C
(m = k^dag conj(k'), arbitrary).  This is stronger than self-positivity of the G-orbit in the sector.  For the
H_0-invariant negative elements rho(beta, z) = -GHZ_{+,00} + beta GHZ_{-,00} + z (1 - GHZ_{+,00} - GHZ_{-,00}) (kappa is
rho(3, 1) up to G; W3 is rho(1, 1)), find the minimum of tr(y Ad(m) y) / (||y|| ||Ad(m) y||) over m.
Method: random starts + scipy BFGS over complex A, B, C.  A clearly negative minimum is a lead only (must be certified
exactly with a rational m before anything is claimed).
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(2026100907)
gp = np.zeros(8); gp[0] = gp[7] = 1 / np.sqrt(2)
gm = np.zeros(8); gm[0] = 1 / np.sqrt(2); gm[7] = -1 / np.sqrt(2)
Pp, Pm = np.outer(gp, gp), np.outer(gm, gm)


def rho(beta, z):
    return -Pp + beta * Pm + z * (np.eye(8) - Pp - Pm)


def gl2(p):
    return (p[0:4] + 1j * p[4:8]).reshape(2, 2)


def val(p, y):
    m = np.kron(np.kron(gl2(p[0:8]), gl2(p[8:16])), gl2(p[16:24]))
    Y = m @ y @ m.conj().T
    nrm = np.linalg.norm(y) * np.linalg.norm(Y)
    return np.real(np.trace(y @ Y)) / max(nrm, 1e-300)


for beta, z in [(1, 1), (2, 1), (3, 1), (2.9, 1), (3, 1.2), (5, 1.5), (6.75, 1.5), (7, 5 / 3), (12, 2), (1, 2)]:
    y = rho(beta, z)
    best = np.inf
    for s in range(24):
        p0 = rng.normal(size=24)
        r = minimize(val, p0, args=(y,), method="BFGS", options={"maxiter": 3000, "gtol": 1e-11})
        best = min(best, r.fun)
    print("rho(beta=%-5s z=%-6s) [sector self-positive iff beta <= 3 z^2 = %6.3f]  min normalized tr(y Ad(m) y) = %.6e"
          % (beta, round(z, 4), 3 * z * z, best), flush=True)
