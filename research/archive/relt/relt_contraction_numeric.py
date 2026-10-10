"""REL-T node N6.3: FLOATING-POINT EVIDENCE ONLY.  Necessary condition extracted from M, M^{-1} in S_m (contract the
identity M M^{-1} = I with a unit control vector v on both sides):  -I_m = sum_{r=1}^{m-1} P_r R_r with P_r, R_r
antisymmetric m x m.  For m = 3 this is impossible by the written trace/rank argument.  Is it solvable for m = 5?
Controls: m = 2, 4 must reach ~0 (J (x) J and J (x) K give solutions); m = 3 must stay away from 0."""
import numpy as np, itertools
from scipy.optimize import least_squares
def asym(m, x):
    A = np.zeros((m, m)); iu = np.triu_indices(m, 1); A[iu] = x; return A - A.T
for m, starts in [(2, 5), (3, 20), (4, 10), (5, 40)]:
    na = m * (m - 1) // 2; k = m - 1
    rng = np.random.default_rng(1); best = np.inf
    for s in range(starts):
        def res(x):
            S = np.zeros((m, m))
            for r in range(k):
                S += asym(m, x[(2*r)*na:(2*r+1)*na]) @ asym(m, x[(2*r+1)*na:(2*r+2)*na])
            return (S + np.eye(m)).ravel()
        r = least_squares(res, rng.normal(size=2 * k * na), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=5000)
        best = min(best, np.sqrt(2 * r.cost))
    print(f"m={m}: best residual {best:.3e}")
