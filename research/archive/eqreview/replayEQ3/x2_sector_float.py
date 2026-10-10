"""FLOATING POINT, EXPLORATION ONLY, CERTIFIES NOTHING.
EQ3-P exploration x2 -- the GHZ-diagonal sector of the natural c = 0 GHZ-free candidate.  Research only.

Candidate (c = 0, pair marginals Q3): K_cand = closed convex hull of BS (biseparable cone) and the SLOCC orbit of
W2 = 1 - 2 GHZ.  A KT(6)-coherent K_3 must be B-self-dual and SLOCC-invariant (p5); its GHZ-diagonal twirl (local Pauli
twirl, B-self-adjoint, idempotent; T fixes every GHZ projector) must then be a self-dual cone in R^8 with the
Euclidean pairing of GHZ eigenvalues.  Necessary-condition test for K_cand:
  (a) self-positivity of the sector generators (all pairwise inner products >= 0);
  (b) is the sector dual contained in the sector cone?  Extreme directions of the dual are probed by LPs (random
      objectives over the dual cut by sum = 1), then membership in the sector cone is tested by an LP.
Sector generators: twirls of random pure biseparable states and of random SLOCC images Ad(C) W2.
A 'dual point outside the cone' only says K_cand is not self-dual in the sector (it could still be extended); a clean
pass would be a LEAD for a GHZ-free countermodel, to be certified exactly and in the full space.  Neither outcome is
evidence.  Usage: python3 -I -B x2_sector_float.py
"""
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(11)
# GHZ basis: index (s, b) -> (|0 b> + s |1 bbar>)/sqrt2, b in {00,01,10,11}
basis = []
for b in range(4):
    for s in (1, -1):
        v = np.zeros(8)
        v[b] = 1                      # |0 b1 b2>
        v[4 + (3 - b)] = s            # |1 bbar>
        basis.append(v / np.sqrt(2))
Bm = np.array(basis)                 # rows: GHZ basis vectors
ghz = basis[0]
W2 = np.eye(8) - 2 * np.outer(ghz, ghz)


def twirl(rho):
    return np.real(np.einsum("ij,jk,ik->i", Bm.conj(), rho, Bm))


def rand_c2():
    return rng.normal(size=2) + 1j * rng.normal(size=2)


def rand_bisep():
    pair = rng.integers(3)
    v2 = rng.normal(size=4) + 1j * rng.normal(size=4)
    v1 = rand_c2()
    if pair == 0:      # (01)|2
        v = np.kron(v2, v1)
    elif pair == 1:    # 0|(12)
        v = np.kron(v1, v2)
    else:              # (02)|1 : v2 on copies 0,2
        v = np.einsum("ac,b->abc", v2.reshape(2, 2), v1).reshape(8)
    v = v / np.linalg.norm(v)
    return np.outer(v, v.conj())


def rand_slocc_w2():
    C = np.kron(np.kron(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)),
                        rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))),
                rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))
    return C @ W2 @ C.conj().T


gens = []
for _ in range(3000):
    t = twirl(rand_bisep())
    gens.append(t / t.sum())
for _ in range(3000):
    t = twirl(rand_slocc_w2())
    gens.append(t / np.abs(t).sum())
G = np.array(gens)
pair_min = (G @ G.T).min()
print(f"(a) min pairwise inner product among {len(G)} sector generators = {pair_min:.3e}")
print(f"    W2 sector vector = {twirl(W2)}")

# (b) probe extreme directions of the dual {y : G y >= 0, sum y = 1}
outside = 0
worst = 0.0
for k in range(200):
    c = rng.normal(size=8)
    r = linprog(c, A_ub=-G, b_ub=np.zeros(len(G)), A_eq=np.ones((1, 8)), b_eq=[1], bounds=[(None, None)] * 8,
                method="highs")
    if r.status != 0:
        continue
    y = r.x
    # membership of y in cone(G): y = G^T lam, lam >= 0
    m = linprog(np.zeros(len(G)), A_eq=G.T, b_eq=y, bounds=[(0, None)] * len(G), method="highs")
    if m.status != 0:
        outside += 1
        # distance proxy: how negative is y against the cone's own generators? (y is in the dual by construction)
        worst = min(worst, float(np.min(y)))
print(f"(b) dual probe points not in the sector cone (LP infeasible): {outside} of 200; most negative eigenvalue "
      f"coordinate among them: {worst:.3e}")
print("x2 done (exploration only)")
