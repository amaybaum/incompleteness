"""EQ2-A exploration x2 -- FLOATING POINT, EXPLORATION ONLY, CERTIFIES NOTHING.

Cutting-plane refinement of x1.  Work in stabilizer coordinates: for a GHZ-diagonal comparison only the 7
expectations t_s(g) = tr(g s), s in S \\ {1} = (ZZI, IZZ, ZIZ, XXX, -YYX, -XYY, -YXY), of a normalized generator
g = PT_j(sigma_ij) (x) rho_k matter.  W = 1/2 - |GHZ><GHZ| has the normalized vector (-1/3)(1,...,1).
  W in B_tw  <=>  (-1/3)1 in conv{ t(g) }.
Loop: LP for a separating y (y . t(g) >= 0 on the current family, y . (-1/3)1 minimized, |y| <= 1); then minimize
y . t(g) over the continuous family by random restarts + Nelder-Mead; add the minimizers; repeat.
"""
import numpy as np
from scipy.optimize import linprog, minimize

rng = np.random.default_rng(11)
P = {"I": np.eye(2), "X": np.array([[0, 1], [1, 0]], dtype=complex),
     "Y": np.array([[0, -1j], [1j, 0]]), "Z": np.diag([1.0, -1.0]).astype(complex)}
STAB = [(1, "ZZI"), (1, "IZZ"), (1, "ZIZ"), (1, "XXX"), (-1, "YYX"), (-1, "XYY"), (-1, "YXY")]


def op3(lbl):
    return np.kron(np.kron(P[lbl[0]], P[lbl[1]]), P[lbl[2]])


SOPS = [sg * op3(l) for sg, l in STAB]


def pt(M, which):
    T = M.reshape(2, 2, 2, 2, 2, 2)
    axes = list(range(6))
    axes[which], axes[which + 3] = axes[which + 3], axes[which]
    return T.transpose(axes).reshape(8, 8)


def place(sig4, pair, rho2):
    i, j = pair
    k = [c for c in range(3) if c not in pair][0]
    T = np.einsum("abcd,ef->abecdf", sig4.reshape(2, 2, 2, 2), rho2)
    order = [None] * 3
    order[i], order[j], order[k] = 0, 1, 2
    perm = [order[0], order[1], order[2], 3 + order[0], 3 + order[1], 3 + order[2]]
    return T.transpose(perm).reshape(8, 8)


PAIRS = [(0, 1), (0, 2), (1, 2)]


def tvec(pair, psi4, r2):
    sig = np.outer(psi4, psi4.conj())
    rho = np.outer(r2, r2.conj())
    g = pt(place(sig, pair, rho), pair[1])
    return np.real(np.array([np.trace(g @ s) for s in SOPS]))


def unpack(x):
    psi = x[0:4] + 1j * x[4:8]
    r = x[8:10] + 1j * x[10:12]
    return psi / np.linalg.norm(psi), r / np.linalg.norm(r)


def rand_x():
    return rng.normal(size=12)


family = []
for pair in PAIRS:
    for _ in range(300):
        family.append(tvec(pair, *unpack(rand_x())))
target = -np.ones(7) / 3
for it in range(25):
    D = np.array(family)
    res = linprog(target, A_ub=-D, b_ub=np.zeros(len(D)), bounds=[(-1, 1)] * 7, method="highs")
    y = res.x
    val = res.fun
    worst, worst_pts = 0.0, []
    for pair in PAIRS:
        for _ in range(40):
            f = lambda x: y @ tvec(pair, *unpack(x))  # noqa: E731
            r = minimize(f, rand_x(), method="Nelder-Mead", options={"maxiter": 4000, "xatol": 1e-10, "fatol": 1e-12})
            if r.fun < -1e-9:
                worst_pts.append(tvec(pair, *unpack(r.x)))
            worst = min(worst, r.fun)
    print(f"iter {it}: LP min y.target = {val:.6g}; continuous worst y.t(g) = {worst:.3g}; added {len(worst_pts)}")
    if not worst_pts:
        print("separating y stable:", np.round(y, 6))
        break
    family += worst_pts
res = linprog(np.zeros(len(family)), A_eq=np.vstack([np.array(family).T, np.ones(len(family))]),
              b_eq=np.concatenate([target, [1.0]]), bounds=(0, None), method="highs")
print("final convex-combination LP status:", res.status, res.message)
