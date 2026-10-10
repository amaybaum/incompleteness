"""rank / nullspace helpers copied from oistage_checks (no side effects on import)."""
from fractions import Fraction as Fr


def rank(rows):
    M = [list(r) for r in rows]
    rk, col = 0, 0
    ncol = len(M[0]) if M else 0
    while rk < len(M) and col < ncol:
        piv = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][col] != 0:
                f = M[i][col] / M[rk][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[rk])]
        rk += 1
        col += 1
    return rk


def nullspace(cols):
    """Basis of {c : sum_j c_j cols[j] = 0}."""
    m, n = len(cols[0]), len(cols)
    A = [[cols[j][i] for j in range(n)] for i in range(m)]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fcol in free:
        v = [Fr(0)] * n
        v[fcol] = Fr(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fcol]
        basis.append(v)
    return basis
