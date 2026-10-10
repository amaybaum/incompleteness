"""E+ block with the positivity constraint (p >= 2): every entry A_r, B_rs antisymmetric (evidence, least squares).
(G D)^2 = I, G = [[0, A_r^T],[A_r, B_rs]], B antisym in (r,s), D = diag(1, mu).  W = one N_A-parity sector, dim p."""
import itertools, numpy as np
from scipy.optimize import least_squares
rng = np.random.default_rng(5)
def so(p, v):
    M = np.zeros((p, p)); iu = np.triu_indices(p, 1); M[iu] = v; return M - M.T
def run(p, mu, restarts=20):
    k = p + 1; na = p * (p - 1) // 2; pairs = [(r, s) for r in range(p) for s in range(r + 1, p)]
    nx = p * na + len(pairs) * na; Dm = np.kron(np.diag([1.] + list(mu)), np.eye(p))
    def build(x):
        G = np.zeros((k * p, k * p))
        for r in range(p):
            A = so(p, x[r * na:(r + 1) * na]); G[(r + 1) * p:(r + 2) * p, :p] = A; G[:p, (r + 1) * p:(r + 2) * p] = A.T
        for i, (r, s) in enumerate(pairs):
            B = so(p, x[p * na + i * na:p * na + (i + 1) * na])
            G[(r + 1) * p:(r + 2) * p, (s + 1) * p:(s + 2) * p] = B; G[(s + 1) * p:(s + 2) * p, (r + 1) * p:(r + 2) * p] = -B
        return G
    f = lambda x: ((build(x) @ Dm) @ (build(x) @ Dm) - np.eye(k * p)).ravel()
    best = np.inf
    for _ in range(restarts):
        r = least_squares(f, rng.normal(size=nx), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=5000)
        best = min(best, np.sqrt(2 * r.cost))
    return best
for p in (2, 3, 4, 5):
    rows = []
    for mu in sorted({tuple(sorted(m)) for m in itertools.product((1., -1.), repeat=p)}):
        rows.append((run(p, mu), mu))
    print('p=%d (d=%d): E+ with antisymmetric entries, residual by twist:' % (p, 2 * p + 1),
          ', '.join('%s:%.2e' % (''.join('+' if m > 0 else '-' for m in mu), r) for r, mu in rows), flush=True)
