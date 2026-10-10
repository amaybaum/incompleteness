"""Minimal exact linear algebra over Fractions (rref, rank, nullspace)."""
from fractions import Fraction as Fr
def rref(M):
    M = [[Fr(x) for x in row] for row in M]
    rows, cols = len(M), (len(M[0]) if M else 0)
    piv = []; r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]; M[r] = [x / pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f*b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == rows: break
    return M, piv
def rank(M): return len(rref(M)[1]) if M else 0
def nullspace(M, ncols=None):
    if not M: return [[Fr(int(i == j)) for j in range(ncols)] for i in range(ncols)]
    R_, piv = rref(M); n = len(M[0]); free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [Fr(0)]*n; v[f] = Fr(1)
        for i, pc in enumerate(piv): v[pc] = -R_[i][f]
        basis.append(v)
    return basis
def matmul(A, B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def T(A): return [list(r) for r in zip(*A)]
