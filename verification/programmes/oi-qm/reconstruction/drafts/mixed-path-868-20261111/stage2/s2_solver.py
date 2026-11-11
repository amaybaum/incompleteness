"""MIXED-PATH-1 Stage 2: locality decision with certificate, and exact maximum of |CHSH|.

Exact phase-1 simplex with integer-preserving pivots on a reduced form of the local-decomposition
linear program (see _phase1).  Integers and Fractions only.  The certificate it returns is
checked by the separate verifier (s2_verify.py); only a verified certificate counts.
"""
import time
from fractions import Fraction

import numpy as np

SAFE = 1 << 50


class Budget:
    def __init__(self, each_ns, total_ns):
        self.each = each_ns
        self.total = total_ns
        self.used = 0
        self.exhausted = False
        self.solved = 0


def decide_locality(N, H, budget):
    """N[a][b][x][y] integer counts, total H per (a,b).  Returns a certificate dict or None
    (None only when a time bound of section 7 is reached)."""
    start = time.monotonic_ns()
    if budget.used >= budget.total:
        budget.exhausted = True
        return None
    deadline = start + min(budget.each, budget.total - budget.used)
    try:
        res = _phase1(N, H, deadline)
    finally:
        budget.used += time.monotonic_ns() - start
        budget.solved += 1
    if res is None:
        budget.exhausted = True
    return res


def _simplex(b, S, sgn, deadline):
    """Exact phase-1 simplex, integer-preserving pivots.  Columns: column j has entries sgn[j][i]
    at rows S[j][i].  Minimises the sum of artificials of  A w + s = b, w, s >= 0  (b >= 0).
    Returns ("feasible", {j: Fraction}) or ("infeasible", y, d) with y A_j <= 0 for all j and
    y b > 0, or None when the deadline passes."""
    m = len(b)
    ns = len(S)
    width = S.shape[1] if ns else 0
    Binv = np.eye(m, dtype=np.int64)
    d = 1
    xB = list(b)
    basis = list(range(m))                         # ids < m artificial; m + j column j
    big = False
    stall = 0
    bland = False
    prev_obj = None
    while True:
        if time.monotonic_ns() > deadline:
            return None
        art = [r for r in range(m) if basis[r] < m]
        obj_num = sum(xB[r] for r in art)
        if obj_num == 0:
            sol = {}
            for r in range(m):
                if basis[r] >= m and xB[r] != 0:
                    if xB[r] < 0:
                        raise ArithmeticError("negative basic value")
                    sol[basis[r] - m] = Fraction(xB[r], d)
            return ("feasible", sol)
        y = Binv[art].sum(axis=0)
        j = None
        if ns:
            vals = y[S[:, 0]] * sgn[:, 0]
            for i in range(1, width):
                vals = vals + y[S[:, i]] * sgn[:, i]
            if big:
                vl = vals.tolist()
                if bland:
                    for jj, vv in enumerate(vl):
                        if vv > 0:
                            j = jj
                            break
                else:
                    mx = max(vl)
                    if mx > 0:
                        j = vl.index(mx)
            else:
                if bland:
                    nz = np.flatnonzero(vals > 0)
                    if len(nz):
                        j = int(nz[0])
                else:
                    jj = int(np.argmax(vals))
                    if int(vals[jj]) > 0:
                        j = jj
        if j is None:
            return ("infeasible", [int(v) for v in y.tolist()], d)
        obj = Fraction(obj_num, d)
        if prev_obj is not None and obj < prev_obj:
            stall = 0
            bland = False
        else:
            stall += 1
            if stall >= 30:
                bland = True
        prev_obj = obj
        alpha = Binv[:, S[j, 0]] * int(sgn[j, 0])
        for i in range(1, width):
            alpha = alpha + Binv[:, S[j, i]] * int(sgn[j, i])
        al = [int(v) for v in alpha.tolist()]
        r = None
        for i in range(m):
            if al[i] > 0:
                if r is None:
                    r = i
                else:
                    lhs = xB[i] * al[r]
                    rhs = xB[r] * al[i]
                    if lhs < rhs or (lhs == rhs and basis[i] < basis[r]):
                        r = i
        if r is None:
            raise ArithmeticError("phase-1 ratio test found no pivot row")
        p = al[r]
        rowr = Binv[r].copy()
        done = False
        if not big:
            maxB = int(np.abs(Binv).max())
            maxal = max(abs(v) for v in al)
            bound = (maxB * (p + maxal)) // d + 1
            e = (d & -d).bit_length() - 1
            if bound < (1 << (62 - e)) and bound < SAFE and maxB < SAFE:
                # integer-preserving pivot in wrapping 64-bit arithmetic: the exact quotient
                # (Binv*p - alpha x row)/d is an integer of magnitude at most bound, recovered
                # from its value modulo 2^64 (odd part of d inverted, power of two shifted out)
                num = Binv * np.int64(p) - np.multiply.outer(alpha, rowr)
                if d != 1:
                    inv = pow(d >> e, -1, 1 << 64)
                    num = (num.view(np.uint64) * np.uint64(inv)).view(np.int64) >> np.int64(e)
                new = num
                done = True
            else:
                Binv = Binv.astype(object)
                alpha = alpha.astype(object)
                rowr = Binv[r].copy()
                big = True
        if not done:
            new = Binv * p - np.multiply.outer(alpha, rowr)
            if d != 1:
                new //= d
            mx = max(abs(v) for v in new.ravel().tolist()) if new.size else 0
            if mx < SAFE:
                new = new.astype(np.int64)
                rowr = rowr.astype(np.int64)
                big = False
        new[r] = rowr
        xr = xB[r]
        nx = []
        for i in range(m):
            num = xB[i] * p - al[i] * xr
            if num % d:
                raise ArithmeticError("inexact integer pivot")
            nx.append(num // d)
        nx[r] = xr
        xB = nx
        Binv = new
        d = p
        basis[r] = m + j

def _phase1(N, H, deadline):
    """Local decomposition of a no-signalling-or-not table.  Variables f[i,x1,y0], g[i,x1,y1]
    (x0 = i): sum_x1 f = N00[i,y0]; sum_i f = N10[x1,y0]; sum_x1 g = N01[i,y1]; sum_i g = N11[x1,y1];
    sum_y0 f = sum_y1 g for every (i,x1).  A solution gives the strategy weights
    w(i,x1,y0,y1) = f g / r with r = sum_y0 f; a Farkas vector gives a Bell functional."""
    Na = np.array(N, dtype=np.int64)
    nA, nB = Na.shape[2], Na.shape[3]
    sup = Na > 0
    R = np.full(Na.shape, -1, dtype=np.int64)
    nsup = int(sup.sum())
    R[sup] = np.arange(nsup)
    b = [int(v) for v in Na[sup]]
    fv = np.argwhere(sup[0, 0][:, None, :] & sup[1, 0][None, :, :])      # i, x1, y0
    gv = np.argwhere(sup[0, 1][:, None, :] & sup[1, 1][None, :, :])      # i, x1, y1
    pairs = sorted(set((int(v[0]), int(v[1])) for v in fv) | set((int(v[0]), int(v[1])) for v in gv))
    prow = {pr: nsup + k for k, pr in enumerate(pairs)}
    b = b + [0] * len(pairs)
    S = []
    sg = []
    for v in fv:
        S.append([int(R[0, 0, v[0], v[2]]), int(R[1, 0, v[1], v[2]]), prow[(int(v[0]), int(v[1]))]])
        sg.append([1, 1, 1])
    for v in gv:
        S.append([int(R[0, 1, v[0], v[2]]), int(R[1, 1, v[1], v[2]]), prow[(int(v[0]), int(v[1]))]])
        sg.append([1, 1, -1])
    S = np.array(S, dtype=np.int64).reshape(-1, 3)
    sg = np.array(sg, dtype=np.int64).reshape(-1, 3)
    res = _simplex(b, S, sg, deadline)
    if res is None:
        return None
    if res[0] == "feasible":
        sol = res[1]
        nf = len(fv)
        f = {}
        g = {}
        r = {}
        for j, val in sol.items():
            if j < nf:
                i, x1, y0 = (int(t) for t in fv[j])
                f.setdefault((i, x1), []).append((y0, val))
                r[(i, x1)] = r.get((i, x1), Fraction(0)) + val
            else:
                i, x1, y1 = (int(t) for t in gv[j - nf])
                g.setdefault((i, x1), []).append((y1, val))
        weights = []
        for key in sorted(f):
            for y0, fval in sorted(f[key]):
                for y1, gval in sorted(g.get(key, [])):
                    weights.append([key[0], key[1], y0, y1, str(fval * gval * Fraction(r[key].denominator, r[key].numerator * H))])
        return {"type": "LOCAL", "weights": weights}
    yl = res[1]
    mabs = max(abs(v) for v in yl[:nsup])
    pen = -4 * mabs - 1
    beta = [[[[str(Fraction(yl[int(R[a, bb, x, yy])])) if sup[a, bb, x, yy] else str(Fraction(pen))
               for yy in range(nB)] for x in range(nA)] for bb in (0, 1)] for a in (0, 1)]
    return {"type": "NONLOCAL", "beta": beta}


def chsh_max(N, H):
    """Exact maximum of |CHSH| over all pairs of +-1 maps of the histories (maps may depend on the
    own setting) and the four placements of the minus sign.  Fraction, or None above 9 letters."""
    Na = np.array(N, dtype=np.int64)
    useA = [x for x in range(Na.shape[2]) if int(Na[:, :, x, :].sum()) > 0]
    useB = [y for y in range(Na.shape[3]) if int(Na[:, :, :, y].sum()) > 0]
    if len(useA) > 9 or len(useB) > 9:
        return None
    Na = Na[:, :, useA, :][:, :, :, useB]
    nA = len(useA)
    codes = np.arange(1 << nA, dtype=np.int64)
    maps = 1 - 2 * ((codes[:, None] >> np.arange(nA, dtype=np.int64)[None, :]) & 1)
    G = [[maps @ Na[a, b] for b in (0, 1)] for a in (0, 1)]
    best = 0
    for i in (0, 1):
        for j in (0, 1):
            tot = np.zeros((1 << nA, 1 << nA), dtype=np.int64)
            for b in (0, 1):
                s0 = -1 if (0, b) == (i, j) else 1
                s1 = -1 if (1, b) == (i, j) else 1
                tot += np.abs(s0 * G[0][b][:, None, :] + s1 * G[1][b][None, :, :]).sum(axis=2)
            best = max(best, int(tot.max()))
    return Fraction(best, H)
