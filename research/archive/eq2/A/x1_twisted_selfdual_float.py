"""EQ2-A exploration x1 -- FLOATING POINT, EXPLORATION ONLY, CERTIFIES NOTHING.

Question (A4.5): does the six-copy kinematic test also exclude the ALL-TWISTED pairwise hull B_tw (three copies, every
pair composite Tw, twist on the second copy of each pair)?  The test requires B_tw* to be self-positive.  The
natural candidate in B_tw* is W = 1/2 - |GHZ><GHZ| (Schmidt bound).  W is GHZ-diagonal and the GHZ-stabilizer
twirl (local Pauli conjugations, which preserve B_tw) projects B_tw onto GHZ-diagonal operators, so
  W in B_tw  <=>  d(W) in cone{ d(g) : g a generator },  d(X)_m = <G_m|X|G_m>, G_m the 8 GHZ basis vectors.
This script searches with an LP over a finite generator family: either a decomposition (suggesting W in B_tw) or
a separating vector y with y.d(g) >= 0 on the family and y.d(W) < 0 (a candidate GHZ-diagonal element of B_tw*
that pairs negatively with W).  Any candidate must then be verified EXACTLY elsewhere.
"""
import itertools
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(7)
I2 = np.eye(2)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]])
Z = np.diag([1.0, -1.0]).astype(complex)


def ket(bits):
    v = np.zeros(8, dtype=complex)
    v[int(bits, 2)] = 1
    return v


G = []
for x in ("00", "01", "10", "11"):
    xb = "".join("1" if c == "0" else "0" for c in x)
    for s in (1, -1):
        G.append((ket("0" + x) + s * ket("1" + xb)) / np.sqrt(2))
G = np.array(G)


def pt(M, which):
    T = M.reshape(2, 2, 2, 2, 2, 2)
    axes = list(range(6))
    axes[which], axes[which + 3] = axes[which + 3], axes[which]
    return T.transpose(axes).reshape(8, 8)


def place(sig4, pair, rho2):
    """operator sigma on `pair` (sigma index order = pair order) times rho on the remaining copy."""
    i, j = pair
    k = [c for c in range(3) if c not in pair][0]
    T = np.einsum("abcd,ef->abecdf", sig4.reshape(2, 2, 2, 2), rho2)   # axes (i, j, k | i, j, k)
    order = [None] * 3
    order[i], order[j], order[k] = 0, 1, 2
    perm = [order[0], order[1], order[2], 3 + order[0], 3 + order[1], 3 + order[2]]
    return T.transpose(perm).reshape(8, 8)


def gen(sig4, pair, rho2):
    """twisted generator: partial transpose on the SECOND copy of the pair."""
    return pt(place(sig4, pair, rho2), pair[1])


def dvec(M):
    return np.real(np.array([g.conj() @ M @ g for g in G]))


def rand_pure(n):
    v = rng.normal(size=n) + 1j * rng.normal(size=n)
    return v / np.linalg.norm(v)


pairs = [(0, 1), (0, 2), (1, 2)]
singles = [np.outer(v, v.conj()) for v in
           [np.array([1, 0]), np.array([0, 1]), np.array([1, 1]) / np.sqrt(2), np.array([1, -1]) / np.sqrt(2),
            np.array([1, 1j]) / np.sqrt(2), np.array([1, -1j]) / np.sqrt(2)]]
bells = [np.array([1, 0, 0, 1]) / np.sqrt(2), np.array([1, 0, 0, -1]) / np.sqrt(2),
         np.array([0, 1, 1, 0]) / np.sqrt(2), np.array([0, 1, -1, 0]) / np.sqrt(2)]
pures = bells + [np.kron(a, b) for a in [np.array([1, 0]), np.array([0, 1]), np.array([1, 1]) / np.sqrt(2)]
                 for b in [np.array([1, 0]), np.array([0, 1]), np.array([1, 1]) / np.sqrt(2)]]
pures += [rand_pure(4) for _ in range(200)]
singles += [np.outer(v, v.conj()) for v in [rand_pure(2) for _ in range(60)]]
D = []
for pair in pairs:
    for p in pures:
        sig = np.outer(p, p.conj())
        for r in singles:
            D.append(dvec(gen(sig, pair, r)))
D = np.array(D)
ghz = (ket("000") + ket("111")) / np.sqrt(2)
W = np.eye(8) / 2 - np.outer(ghz, ghz.conj())
w = dvec(W)
print("d(W) =", np.round(w, 6))
print("min over family of d(g)[GHZ+] =", D[:, 0].min())
res = linprog(np.zeros(len(D)), A_eq=D.T, b_eq=w, bounds=(0, None), method="highs")
print("decomposition LP status:", res.status, res.message)
# separating vector: minimize y.w subject to y.d >= 0 on the family, -1 <= y <= 1
res2 = linprog(w, A_ub=-D, b_ub=np.zeros(len(D)), bounds=[(-1, 1)] * 8, method="highs")
print("separation LP:", res2.status, "min y.d(W) =", res2.fun)
y = res2.x
print("y =", np.round(y, 6))


# check y against many random generators (continuous family)
def worst(y, trials=20000):
    m = 1e9
    for _ in range(trials):
        pair = pairs[rng.integers(3)]
        p = rand_pure(4)
        r = rand_pure(2)
        m = min(m, y @ dvec(gen(np.outer(p, p.conj()), pair, np.outer(r, r.conj()))))
    return m


print("worst y.d(g) over 20000 random generators:", worst(y))
