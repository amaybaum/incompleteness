"""Exact rational LP feasibility (Phase I simplex, Bland's rule), Fractions only.
feasible(cols, b): find lam >= 0 with sum_j lam_j * cols[j] = b (b >= 0). Returns lam list or None."""
from fractions import Fraction as F

def feasible(cols, b):
    m, n = len(b), len(cols)
    if n == 0:
        return [] if all(x == 0 for x in b) else None
    # tableau rows: n structural + m artificial + rhs
    T = []
    for i in range(m):
        row = [F(cols[j][i]) for j in range(n)] + [F(1) if k == i else F(0) for k in range(m)] + [F(b[i])]
        T.append(row)
    basis = [n + i for i in range(m)]
    W = n + m
    # objective: minimise sum of artificials; reduced costs c_j = -sum_i T[i][j] for structural
    def obj_row():
        r = [F(0)] * (W + 1)
        for j in range(n + m):
            cj = F(1) if j >= n else F(0)
            s = cj - sum(T[i][j] * (F(1) if basis[i] >= n else F(0)) for i in range(m))
            r[j] = s
        r[W] = -sum(T[i][W] for i in range(m) if basis[i] >= n)
        return r
    z = obj_row()
    while True:
        enter = next((j for j in range(W) if z[j] < 0), None)   # Bland: smallest index with negative reduced cost
        if enter is None:
            break
        best, leave = None, None
        for i in range(m):
            if T[i][enter] > 0:
                ratio = T[i][W] / T[i][enter]
                if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                    best, leave = ratio, i
        if leave is None:
            raise RuntimeError("unbounded phase I (impossible)")
        piv = T[leave][enter]
        T[leave] = [x / piv for x in T[leave]]
        for i in range(m):
            if i != leave and T[i][enter] != 0:
                f = T[i][enter]; T[i] = [a - f * c for a, c in zip(T[i], T[leave])]
        f = z[enter]; z = [a - f * c for a, c in zip(z, T[leave])]
        basis[leave] = enter
    val = sum(T[i][W] for i in range(m) if basis[i] >= n)
    if val != 0:
        return None
    lam = [F(0)] * n
    for i in range(m):
        if basis[i] < n:
            lam[basis[i]] = T[i][W]
    # exact verification
    for i in range(m):
        assert sum(lam[j] * cols[j][i] for j in range(n)) == b[i]
    assert all(x >= 0 for x in lam)
    return lam

if __name__ == "__main__":
    # self-test: (1/2,1/2) in hull of (1,0),(0,1): feasible; (1,0) not in hull of (1/2,1/2),(0,1)
    assert feasible([[1, 0], [0, 1]], [F(1, 2), F(1, 2)]) == [F(1, 2), F(1, 2)]
    assert feasible([[F(1, 2), F(1, 2)], [0, 1]], [1, 0]) is None
    assert feasible([[F(1,3),F(2,3)],[F(2,3),F(1,3)],[1,0]], [F(1,2),F(1,2)]) is not None
    print("exactlp self-test PASS")
