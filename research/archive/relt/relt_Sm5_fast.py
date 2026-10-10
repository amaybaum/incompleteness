"""REL-T node N6.2 (fast variant of relt_Sm_numeric.py with analytic Jacobian). FLOATING-POINT EVIDENCE ONLY.
Same question and controls: m = 3 must stay away from 0, m = 4 must reach ~0; question m = 5."""
import numpy as np, itertools, sys
from scipy.optimize import least_squares
def basis(m):
    B = []
    for k, j in itertools.combinations(range(m), 2):
        E = np.zeros((m, m)); E[k, j] = 1; E[j, k] = -1
        for a, b in itertools.combinations(range(m), 2):
            A = np.zeros((m, m)); A[a, b] = 1; A[b, a] = -1
            B.append(np.kron(E, A))
    return np.array(B)
def run(m, starts, seed=3):
    B = basis(m); nb = len(B); I = np.eye(m * m); rng = np.random.default_rng(seed); best = np.inf
    for s in range(starts):
        def res(x):
            return (np.tensordot(x[:nb], B, 1) @ np.tensordot(x[nb:], B, 1) - I).ravel()
        def jac(x):
            M1 = np.tensordot(x[:nb], B, 1); M2 = np.tensordot(x[nb:], B, 1)
            J1 = np.einsum('iab,bc->iac', B, M2).reshape(nb, -1).T
            J2 = np.einsum('ab,ibc->iac', M1, B).reshape(nb, -1).T
            return np.hstack([J1, J2])
        r = least_squares(res, rng.normal(size=2 * nb), jac=jac, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
        best = min(best, np.sqrt(2 * r.cost))
        print(f"  m={m} start {s}: residual {np.sqrt(2*r.cost):.3e}"); sys.stdout.flush()
    return best
for m, starts in [(3, 6), (4, 3), (5, 12)]:
    print(f"m={m}: best {run(m, starts):.3e}"); sys.stdout.flush()
