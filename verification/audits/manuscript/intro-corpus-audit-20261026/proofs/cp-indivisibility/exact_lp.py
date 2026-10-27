"""Exact rational LP feasibility with verified certificates.

feasible(A, b): decide whether {x >= 0 : A x = b} is nonempty.
Returns ('feasible', x) with A x == b, x >= 0 checked exactly, or
('infeasible', y) with y^T A >= 0 and y^T b < 0 checked exactly (Farkas).
The simplex below is only a search procedure: every verdict is re-checked
exactly against its certificate before it is returned.
"""
from fractions import Fraction as F


def _verify_primal(A, b, x):
    if any(v < 0 for v in x):
        return False
    return all(sum(A[i][j] * x[j] for j in range(len(x))) == b[i] for i in range(len(A)))


def _verify_farkas(A, b, y):
    m, n = len(A), len(A[0])
    for j in range(n):
        if sum(y[i] * A[i][j] for i in range(m)) < 0:
            return False
    return sum(y[i] * b[i] for i in range(m)) < 0


def feasible(A, b):
    m, n = len(A), len(A[0])
    A = [[F(v) for v in row] for row in A]
    b = [F(v) for v in b]
    # make b >= 0
    sign = [1] * m
    for i in range(m):
        if b[i] < 0:
            sign[i] = -1
            A[i] = [-v for v in A[i]]
            b[i] = -b[i]
    # phase-1 tableau: variables x (n) + artificials (m)
    N = n + m
    T = [A[i] + [F(1) if k == i else F(0) for k in range(m)] + [b[i]] for i in range(m)]
    basis = [n + i for i in range(m)]
    # objective: minimize sum of artificials -> reduced costs
    cost = [F(0)] * n + [F(1)] * m

    def reduced():
        r = []
        for j in range(N):
            r.append(cost[j] - sum(cost[basis[i]] * T[i][j] for i in range(m)))
        return r

    it = 0
    while True:
        it += 1
        if it > 10000:
            raise RuntimeError("simplex did not terminate")
        r = reduced()
        enter = next((j for j in range(N) if r[j] < 0), None)  # Bland
        if enter is None:
            break
        rows = [(T[i][-1] / T[i][enter], basis[i], i) for i in range(m) if T[i][enter] > 0]
        if not rows:
            raise RuntimeError("unbounded phase 1 (impossible)")
        mn = min(rw[0] for rw in rows)
        _, _, piv = min((rw for rw in rows if rw[0] == mn), key=lambda rw: rw[1])
        pv = T[piv][enter]
        T[piv] = [v / pv for v in T[piv]]
        for i in range(m):
            if i != piv and T[i][enter] != 0:
                f = T[i][enter]
                T[i] = [T[i][k] - f * T[piv][k] for k in range(N + 1)]
        basis[piv] = enter
    obj = sum(cost[basis[i]] * T[i][-1] for i in range(m))
    if obj == 0:
        x = [F(0)] * n
        for i in range(m):
            if basis[i] < n:
                x[basis[i]] = T[i][-1]
        A0 = [[F(v) * sign[i] for v in A[i]] for i in range(m)]
        b0 = [b[i] * sign[i] for i in range(m)]
        assert _verify_primal(A0, b0, x)
        return "feasible", x
    # dual of phase 1: y_i = cost_B B^{-1}; the artificial columns of the tableau hold B^{-1}
    y = []
    for i in range(m):
        col = n + i
        y.append(sum(cost[basis[k]] * T[k][col] for k in range(m)))
    # Phase-1 optimality: c_j - y^T A_j >= 0 for x columns (c_j = 0) => -y^T A >= 0
    # and objective y^T b > 0.  Farkas vector is -y (in the sign-flipped system).
    yf = [-y[i] * sign[i] for i in range(m)]
    A0 = [[F(v) * sign[i] for v in A[i]] for i in range(m)]
    b0 = [b[i] * sign[i] for i in range(m)]
    assert _verify_farkas(A0, b0, yf), "Farkas certificate failed verification"
    return "infeasible", yf


def stochastic_divisor(T1, T2):
    """Exact: is there a row-stochastic M with T1 M = T2?  Returns (bool, certificate)."""
    n = len(T1)
    # variables M[k][j] -> index k*n + j
    A, b = [], []
    for i in range(n):
        for j in range(n):
            row = [F(0)] * (n * n)
            for k in range(n):
                row[k * n + j] = F(T1[i][k])
            A.append(row)
            b.append(F(T2[i][j]))
    for k in range(n):
        row = [F(0)] * (n * n)
        for j in range(n):
            row[k * n + j] = F(1)
        A.append(row)
        b.append(F(1))
    verdict, cert = feasible(A, b)
    return verdict == "feasible", cert


if __name__ == "__main__":
    # self-test: controls with known answers
    I2 = [[1, 0], [0, 1]]
    J2 = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
    assert stochastic_divisor(I2, J2)[0] is True      # J = I * J
    assert stochastic_divisor(J2, I2)[0] is False     # equal rows obstruction
    assert stochastic_divisor(J2, J2)[0] is True
    # invertible T1 whose unique divisor has a negative entry
    T1 = [[F(3, 4), F(1, 4)], [F(1, 4), F(3, 4)]]
    T2 = [[F(1), F(0)], [F(0), F(1)]]
    assert stochastic_divisor(T1, T2)[0] is False
    T2b = [[F(5, 8), F(3, 8)], [F(3, 8), F(5, 8)]]    # = T1 * T1 -> divisible
    assert stochastic_divisor(T1, T2b)[0] is True
    print("exact_lp self-test: PASS")
