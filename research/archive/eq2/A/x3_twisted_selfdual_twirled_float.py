"""EQ2-A exploration x3 -- FLOATING POINT, EXPLORATION ONLY, CERTIFIES NOTHING.

Is the all-twisted three-copy pairwise hull B_tw self-dual on the GHZ-twirled subspace?  (Necessary for B_tw to pass
the six-copy kinematic test, which requires B_tw* = B_tw.)  In stabilizer coordinates t(g) in R^7 the twirled base
is B8 = conv{ t(g) } and the twirled dual base is B8^ = { f : 1 + f.t >= 0 for all t in B8 }.  Self-duality of the
twirled cone  <=>  B8 = B8^.
Support function h(y) = min_{t in B8} y.t = min over pairs p and r in the unit sphere of lambda_min(A_p(y, r)), with
A_p(y, r) = sum_s y_s <s_k>_r (s_i (x) s_j^T)  (sigma ranges over all two-qubit states; lambda_min concave in r, so
the minimum over the ball is on the sphere).
Test: f on the boundary of B8^ (f = u / (-h(u)), h(f) = -1).  f in B8 iff g(z) = z.f - h(z) >= 0 on the unit ball;
g is convex, so its minimum over the ball is a convex problem; a robustly negative minimum means f is not in B8.
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(3)
P = {"I": np.eye(2), "X": np.array([[0, 1], [1, 0]], dtype=complex),
     "Y": np.array([[0, -1j], [1j, 0]]), "Z": np.diag([1.0, -1.0]).astype(complex)}
STAB = [(1, "ZZI"), (1, "IZZ"), (1, "ZIZ"), (1, "XXX"), (-1, "YYX"), (-1, "XYY"), (-1, "YXY")]
PAIRS = [(0, 1), (0, 2), (1, 2)]
BLOCH = {"I": None, "X": 0, "Y": 1, "Z": 2}
# precompute, per pair, the list of (sign * 2-qubit operator s_i (x) s_j^T, which component of r (or None))
TERMS = []
for (i, j) in PAIRS:
    k = [c for c in range(3) if c not in (i, j)][0]
    lst = []
    for sg, lbl in STAB:
        si, sj, sk = P[lbl[i]], P[lbl[j]], P[lbl[k]]
        lst.append((sg * np.kron(si, sj.T), BLOCH[lbl[k]]))
    TERMS.append(lst)
grid = rng.normal(size=(600, 3))
grid /= np.linalg.norm(grid, axis=1)[:, None]


def lam(y, p, r):
    A = np.zeros((4, 4), dtype=complex)
    for ys, (O, comp) in zip(y, TERMS[p]):
        A += ys * (1.0 if comp is None else r[comp]) * O
    return np.linalg.eigvalsh(A)[0]


def h(y):
    best = np.inf
    for p in range(3):
        vals = [lam(y, p, r) for r in grid]
        i0 = int(np.argmin(vals))
        def f(a):
            r = np.array([np.sin(a[0]) * np.cos(a[1]), np.sin(a[0]) * np.sin(a[1]), np.cos(a[0])])
            return lam(y, p, r)
        r0 = grid[i0]
        a0 = [np.arccos(np.clip(r0[2], -1, 1)), np.arctan2(r0[1], r0[0])]
        res = minimize(f, a0, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 2000})
        best = min(best, res.fun, vals[i0])
    return best


# sanity: h at the target direction of W (all -1/3) should be <= y.(-1/3 1) since W in B8 (exact, a4b)
y_t = np.ones(7) / np.sqrt(7)
print("h(1/sqrt7) =", h(y_t), " vs  y.(-1/3) =", -7 / 3 / np.sqrt(7))
results = []
for trial in range(10):
    u = rng.normal(size=7)
    u /= np.linalg.norm(u)
    hu = h(u)
    if hu >= 0:
        results.append(("h>=0", hu))
        continue
    fvec = u / (-hu)
    g = lambda z: z @ fvec - h(z)  # noqa: E731
    best = 0.0
    for _ in range(3):
        z0 = rng.normal(size=7)
        z0 /= 2 * np.linalg.norm(z0)
        res = minimize(g, z0, method="SLSQP", constraints=[{"type": "ineq", "fun": lambda z: 1 - z @ z}],
                       options={"maxiter": 200, "ftol": 1e-10})
        best = min(best, res.fun)
    results.append((f"|f|={np.linalg.norm(fvec):.4f}", best))
    print(f"trial {trial:2d}: |f| = {np.linalg.norm(fvec):.4f}, min_z (z.f - h(z)) on the ball = {best:.3e}")
neg = [b for _, b in results if isinstance(b, float) and b < -1e-4]
print(f"summary: {len(neg)} of {len(results)} boundary points of the twirled dual base lie robustly outside B8")
