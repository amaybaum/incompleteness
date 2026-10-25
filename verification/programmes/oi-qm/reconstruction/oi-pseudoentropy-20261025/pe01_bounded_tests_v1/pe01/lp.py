"""Randomized K0 worst case for P^emb(m <= 2) by exact rational LP (PLAN.md §3).

For a sign pattern s on the family F (modulo a global flip), the dual form is
    min_{pi in Delta(F)} max_{(rho, a)} sum_{(v, x)} ( sum_phi pi_phi s_phi Delta_phi(v, x) )_+ ,
the inner maximum over F being the sum of positive parts. It is solved exactly by cutting planes:
the master problem is the matrix game min_pi max_{cuts j} (G pi)_j over the tests generated so far,
solved by an exact simplex (Fractions, Bland's rule); pricing evaluates the inner maximum exactly at
the master's pi and adds the maximising test (rho, a, F*) until it does not exceed the master value.
The final value carries both certificates: pi (an upper bound by pricing) and the mixed test w over
the cuts (a lower bound, max_w min_phi s_phi sum_D w_D Delta_phi(D)).
"""
from fractions import Fraction

import numpy as np


def simplex_max(A, b, c):
    """max c.y s.t. A y <= b, y >= 0, with b >= 0 (exact). Returns (value, y, u) where u are the
    optimal dual values of the constraints (min b.u s.t. A^T u >= c, u >= 0)."""
    m = len(A)
    n = len(c)
    # tableau: rows 0..m-1 constraints [A | I | b], last row objective [-c | 0 | 0]
    T = [[Fraction(A[i][j]) for j in range(n)] + [Fraction(int(i == k)) for k in range(m)] + [Fraction(b[i])]
         for i in range(m)]
    T.append([-Fraction(cj) for cj in c] + [Fraction(0)] * m + [Fraction(0)])
    basis = [n + i for i in range(m)]
    while True:
        obj = T[-1]
        ent = next((j for j in range(n + m) if obj[j] < 0), None)
        if ent is None:
            break
        best, lv = None, None
        for i in range(m):
            a = T[i][ent]
            if a > 0:
                r = T[i][-1] / a
                if best is None or r < best or (r == best and basis[i] < basis[lv]):
                    best, lv = r, i
        if lv is None:
            raise ValueError("unbounded")
        piv = T[lv][ent]
        T[lv] = [v / piv for v in T[lv]]
        for i in range(m + 1):
            if i != lv and T[i][ent] != 0:
                f = T[i][ent]
                T[i] = [vi - f * vl for vi, vl in zip(T[i], T[lv])]
        basis[lv] = ent
    y = [Fraction(0)] * n
    for i, bv in enumerate(basis):
        if bv < n:
            y[bv] = T[i][-1]
    u = [T[-1][n + i] for i in range(m)]
    return T[-1][-1], y, u


def solve_game(G):
    """value, pi (minimiser over columns), w (maximiser over rows) of min_pi max_j (G pi)_j."""
    rows = len(G)
    cols = len(G[0])
    mn = min(min(r) for r in G)
    kappa = Fraction(1) - mn if mn <= 0 else Fraction(0)
    Gp = [[g + kappa for g in r] for r in G]
    # column player: u = pi / v' maximises sum u s.t. Gp u <= 1, u >= 0 (value 1/v'); the row
    # player's y = w / v' are the optimal dual values of the row constraints.
    val, u, y = simplex_max(Gp, [1] * rows, [1] * cols)
    vprime = 1 / val
    su = sum(u)
    pi = [ui / su for ui in u]
    sy = sum(y)
    w = [yi / sy for yi in y]
    v = vprime - kappa
    # certificates: max_j (G pi)_j = v = min_f (w^T G)_f
    up = max(sum(G[j][f] * pi[f] for f in range(cols)) for j in range(rows))
    lo = min(sum(w[j] * G[j][f] for j in range(rows)) for f in range(cols))
    assert up == v == lo, (up, v, lo)
    return v, pi, w


class Pricer:
    """Exact inner maximum over the m <= 2 observers at one K, for a family's tables.

    Cell data per observer: C[o, cell, phi] (counts) and Z[o, cell] = Q_K(v) M; with den = 2^(K+1),
    Delta_phi(cell) = (C den - Z) / (M den). Observers with identical sorted cell multisets are
    merged (the inner maximum depends only on that multiset)."""

    def __init__(self, Cstack, Zcells, den, M, obs_ids):
        # Cstack: (n_obs, cells, F) int64; Zcells: (n_obs, cells) object
        n, cells, F = Cstack.shape
        self.F = F
        self.den = den
        self.M = M
        keys = {}
        rep = []
        self.cellidx = []
        for o in range(n):
            orig = [(tuple(int(x) for x in Cstack[o, c]), int(Zcells[o, c])) for c in range(cells)]
            order = sorted(range(cells), key=lambda c: orig[c])
            items = tuple(orig[c] for c in order)
            if items not in keys:
                keys[items] = len(rep)
                rep.append((o, items))
                self.cellidx.append(order)
        self.rep = rep
        self.obs_ids = obs_ids
        self.cells = cells
        # per representative, the integer numerators N_phi(cell) = C den - Z
        self.num = [[[c[0][f] * den - c[1] for f in range(F)] for c in items] for _, items in rep]

    def price(self, coef):
        """max_o sum_cells (sum_phi coef_phi Delta_phi(cell))_+ for rational coef (s_phi pi_phi).
        Returns (value, global observer id, F* cell bitmask)."""
        D = 1
        for c in coef:
            D = _lcm(D, c.denominator)
        ci = [int(c * D) for c in coef]
        best, arg, Fbest = None, None, None
        for r, rows in enumerate(self.num):
            tot = 0
            Fm = 0
            for k, row in enumerate(rows):
                v = 0
                for f in range(self.F):
                    if ci[f]:
                        v += ci[f] * row[f]
                if v > 0:
                    tot += v
                    Fm |= 1 << self.cellidx[r][k]
            if best is None or tot > best:
                best, arg, Fbest = tot, r, Fm
        val = Fraction(best, D * self.M * self.den)
        return val, int(self.obs_ids[self.rep[arg][0]]), Fbest

    def cut_vector(self, o_global, Fmask, s, Cfull, Zfull):
        """s_phi Delta_phi(F) for observer o (exact), from the full tables."""
        F = self.F
        out = []
        for f in range(F):
            tot = Fraction(0)
            for c in range(self.cells):
                if (Fmask >> c) & 1:
                    tot += Fraction(int(Cfull[o_global, c, f]) * self.den - int(Zfull[o_global, c]), self.M * self.den)
            out.append(s[f] * tot)
        return out


def _lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)


def randomized_k0(Cfull, Zfull, den, M, s, obs_ids=None, max_iter=500):
    """Exact value of the dual LP for sign pattern s. Cfull: (n_obs, cells, F); Zfull: (n_obs, cells).
    Returns dict with value, pi, the mixed test (cuts with weights) and iteration count."""
    n, cells, F = Cfull.shape
    if obs_ids is None:
        obs_ids = np.arange(n)
    pr = Pricer(Cfull, Zfull, den, M, np.arange(n))
    cuts = []
    G = []
    for f in range(F):
        e = [Fraction(int(i == f)) * s[i] for i in range(F)]
        _, o, Fm = pr.price(e)
        if (o, Fm) not in cuts:
            cuts.append((o, Fm))
            G.append(pr.cut_vector(o, Fm, s, Cfull, Zfull))
    it = 0
    while True:
        it += 1
        v, pi, w = solve_game(G)
        coef = [s[f] * pi[f] for f in range(F)]
        g, o, Fm = pr.price(coef)
        if g <= v:
            assert g == v or g >= v  # g >= v always (the master is a relaxation)
            break
        if (o, Fm) in cuts or it > max_iter:
            raise RuntimeError("cutting plane did not converge")
        cuts.append((o, Fm))
        G.append(pr.cut_vector(o, Fm, s, Cfull, Zfull))
    assert g == v, (g, v)
    mixed = [(int(obs_ids[cuts[j][0]]), cuts[j][1], w[j]) for j in range(len(cuts)) if w[j] != 0]
    return {"value": v, "pi": pi, "mixed": mixed, "iterations": it, "cuts": len(cuts)}


def sign_patterns(F):
    """All s in {+1,-1}^F modulo a global flip (s_0 = +1), the all-positive pattern first."""
    out = []
    for k in range(1 << (F - 1)):
        out.append([1] + [(-1 if (k >> (i - 1)) & 1 else 1) for i in range(1, F)])
    return out
