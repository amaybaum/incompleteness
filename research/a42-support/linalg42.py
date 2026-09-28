"""Exact rational linear algebra (Fractions) for small systems: rref, nullspace, rank."""
from fractions import Fraction as Fr
def rref(rows, ncols):
    M = [[Fr(x) for x in r] for r in rows]; piv = []; r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]; pv = M[r][c]
        if pv != 1: M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]; Mr = M[r]; M[i] = [x - f * y for x, y in zip(M[i], Mr)]
        piv.append(c); r += 1
        if r == len(M): break
    return M[:r], piv
def nullspace(rows, ncols):
    R, piv = rref(rows, ncols); free = [c for c in range(ncols) if c not in set(piv)]
    out = []
    for f in free:
        v = [Fr(0)] * ncols; v[f] = Fr(1)
        for r, c in zip(R, piv): v[c] = -r[f]
        out.append(v)
    return out
def rank(rows, ncols): return len(rref(rows, ncols)[1])
