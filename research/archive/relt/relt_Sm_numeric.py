"""REL-T node N6.2: FLOATING-POINT EVIDENCE ONLY (not a certificate).
Is there an invertible M in S_m with M^{-1} in S_m?  Least squares on the residual M M' - I over M, M' in S_m.
Controls: m = 2, 4 (solutions exist: residual must reach ~0); m = 3 (exactly excluded by relt_S_exact: residual must
stay bounded away from 0).  Question: m = 5."""
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

def run(m, starts, seed=0):
    B = basis(m); nb = len(B); I = np.eye(m * m)
    rng = np.random.default_rng(seed)
    best = np.inf
    for s in range(starts):
        x0 = rng.normal(size=2 * nb)
        def res(x):
            M = np.tensordot(x[:nb], B, 1); Mp = np.tensordot(x[nb:], B, 1)
            return (M @ Mp - I).ravel()
        r = least_squares(res, x0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        best = min(best, np.sqrt(2 * r.cost))
    return best

for m, starts in [(2, 5), (3, 20), (4, 10), (5, 30)]:
    b = run(m, starts)
    print(f"m={m}: dim S_m={len(basis(m))}, best ||M M' - I||_F over {starts} starts = {b:.3e}")
    sys.stdout.flush()
