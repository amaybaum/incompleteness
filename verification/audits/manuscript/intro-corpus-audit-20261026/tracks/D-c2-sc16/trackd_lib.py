"""Track D shared library: exact rational LP feasibility, bijective process laws, gaps, rooted families.

All arithmetic is Fraction/int. No floating point.
"""
from fractions import Fraction as Fr
from itertools import product
from collections import defaultdict

# ---------------------------------------------------------------- exact LP

def lp_feasible(A, b):
    """Decide feasibility of A x = b, x >= 0 exactly (Phase-I simplex, Bland's rule).

    Returns ('feasible', x) with x verified, or ('infeasible', w) with a Farkas certificate w:
    A^T w >= 0 and b^T w < 0 (verified)."""
    m = len(A)
    n = len(A[0]) if m else 0
    A = [[Fr(v) for v in row] for row in A]
    b = [Fr(v) for v in b]
    sign = [1] * m
    for i in range(m):
        if b[i] < 0:
            sign[i] = -1
            A[i] = [-v for v in A[i]]
            b[i] = -b[i]
    # tableau columns: n originals, m artificials, rhs
    T = [A[i] + [Fr(1) if j == i else Fr(0) for j in range(m)] + [b[i]] for i in range(m)]
    basis = [n + i for i in range(m)]
    cost = [Fr(0)] * n + [Fr(1)] * m
    N = n + m
    while True:
        # reduced costs r_j = c_j - c_B B^-1 A_j
        cb = [cost[k] for k in basis]
        enter = None
        for j in range(N):
            if j in basis:
                continue
            r = cost[j] - sum(cb[i] * T[i][j] for i in range(m))
            if r < 0:
                enter = j
                break  # Bland: smallest index
        if enter is None:
            break
        # ratio test, Bland tie-break on basis index
        best = None
        for i in range(m):
            if T[i][enter] > 0:
                ratio = T[i][N] / T[i][enter]
                if best is None or ratio < best[0] or (ratio == best[0] and basis[i] < basis[best[1]]):
                    best = (ratio, i)
        if best is None:
            raise RuntimeError('unbounded phase I (impossible)')
        p = best[1]
        piv = T[p][enter]
        T[p] = [v / piv for v in T[p]]
        for i in range(m):
            if i != p and T[i][enter] != 0:
                f = T[i][enter]
                T[i] = [vi - f * vp for vi, vp in zip(T[i], T[p])]
        basis[p] = enter
    obj = sum(cost[basis[i]] * T[i][N] for i in range(m))
    if obj == 0:
        x = [Fr(0)] * n
        for i in range(m):
            if basis[i] < n:
                x[basis[i]] = T[i][N]
        # verify against the ORIGINAL system
        for i in range(m):
            lhs = sum(A[i][j] * x[j] for j in range(n))
            assert lhs == b[i], 'feasible point fails verification'
        assert all(v >= 0 for v in x)
        return 'feasible', x
    # duals y = c_B B^{-1}; B^{-1} sits in the artificial columns
    cb = [cost[k] for k in basis]
    y = [sum(cb[i] * T[i][n + k] for i in range(m)) for k in range(m)]
    w = [-y[k] for k in range(m)]  # certificate for the sign-flipped system
    for j in range(n):
        assert sum(A[i][j] * w[i] for i in range(m)) >= 0, 'Farkas certificate fails A^T w >= 0'
    assert sum(b[i] * w[i] for i in range(m)) < 0, 'Farkas certificate fails b^T w < 0'
    w_orig = [w[i] * sign[i] for i in range(m)]
    return 'infeasible', w_orig


def divisor(Gs, Gt):
    """Exact: is there a row-stochastic Lambda with Gs Lambda = Gt?  Returns (bool, Lambda or cert)."""
    d = len(Gs)
    # variables Lambda[k][j], index k*d+j
    A, b = [], []
    for i in range(d):
        for j in range(d):
            row = [Fr(0)] * (d * d)
            for k in range(d):
                row[k * d + j] = Fr(Gs[i][k])
            A.append(row)
            b.append(Fr(Gt[i][j]))
    for k in range(d):
        row = [Fr(0)] * (d * d)
        for j in range(d):
            row[k * d + j] = Fr(1)
        A.append(row)
        b.append(Fr(1))
    status, sol = lp_feasible(A, b)
    if status == 'feasible':
        L = [[sol[k * d + j] for j in range(d)] for k in range(d)]
        # independent re-verification
        assert all(v >= 0 for r in L for v in r)
        assert all(sum(r) == 1 for r in L)
        assert matmul(Gs, L) == [[Fr(v) for v in r] for r in Gt]
        return True, L
    return False, sol


def divisible_2x2_closed_form(Gs, Gt):
    """Independent closed-form test for 2x2 stochastic matrices."""
    a, b_ = Fr(Gs[0][0]), Fr(Gs[0][1])
    c, d = Fr(Gs[1][0]), Fr(Gs[1][1])
    det = a * d - b_ * c
    if det != 0:
        inv = [[d / det, -b_ / det], [-c / det, a / det]]
        L = matmul(inv, Gt)
        return all(v >= 0 for r in L for v in r)
    # singular stochastic 2x2: identical rows (rank one); Gs Lambda has identical rows r Lambda,
    # and r Lambda can be any distribution (Lambda = 1 q). So divisible iff Gt has identical rows.
    return list(Gt[0]) == list(Gt[1])


def matmul(X, Y):
    return [[sum(Fr(X[i][k]) * Fr(Y[k][j]) for k in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def p_divisible_window(Gammas, n, closed_form_check=False, stats=None):
    """P-divisible on {0..n}: all 0<=s<t<=n. Gammas[t] for t=0..n. Returns (bool, failing pair or None)."""
    for t in range(1, n + 1):
        for s in range(0, t):
            ok, _ = divisor(Gammas[s], Gammas[t])
            if closed_form_check and len(Gammas[s]) == 2:
                cf = divisible_2x2_closed_form(Gammas[s], Gammas[t])
                if stats is not None:
                    stats['cf_checked'] += 1
                if cf != ok:
                    if stats is not None:
                        stats['cf_disagree'] += 1
                    raise AssertionError('closed form disagrees with LP')
            if not ok:
                return False, (s, t)
    return True, None


def n_div(Gammas, nmax, closed_form_check=False, stats=None):
    """Largest n <= nmax such that the rooted family is P-divisible on {0..n} (>= 1 always)."""
    n = 1
    for t in range(2, nmax + 1):
        for s in range(0, t):
            ok, _ = divisor(Gammas[s], Gammas[t])
            if closed_form_check and len(Gammas[s]) == 2:
                cf = divisible_2x2_closed_form(Gammas[s], Gammas[t])
                if stats is not None:
                    stats['cf_checked'] += 1
                if cf != ok:
                    raise AssertionError('closed form disagrees with LP')
            if not ok:
                return n, (s, t)
        n = t
    return n, None

# ---------------------------------------------------------------- bijections

def perm_order(perm):
    seen = [False] * len(perm)
    from math import gcd
    L = 1
    for i in range(len(perm)):
        if not seen[i]:
            c, j = 0, i
            while not seen[j]:
                seen[j] = True
                j = perm[j]
                c += 1
            L = L * c // gcd(L, c)
    return L


def state_index(x, h, nH):
    return x * nH + h


def trajectories(perm, nV, nH, horizon):
    """All trajectories from the uniform initial law on V x H. Returns list of (x-tuple, z0)."""
    out = []
    for z0 in range(nV * nH):
        z = z0
        xs = [z // nH]
        for _ in range(horizon):
            z = perm[z]
            xs.append(z // nH)
        out.append((tuple(xs), z0))
    return out


def rooted_family(perm, nV, nH, tmax):
    """Gamma_t(a, j) under uniform mu_H, every root a, t = 0..tmax."""
    G = []
    for t in range(tmax + 1):
        M = [[Fr(0)] * nV for _ in range(nV)]
        for a in range(nV):
            for h in range(nH):
                z = a * nH + h
                for _ in range(t):
                    z = perm[z]
                M[a][z // nH] += Fr(1, nH)
        G.append(M)
    return G


def law_from_trajs(trajs, weights=None):
    """Exact law on visible strings: dict string -> Fraction."""
    P = defaultdict(Fr)
    tot = len(trajs) if weights is None else None
    for idx, (xs, _) in enumerate(trajs):
        w = Fr(1, tot) if weights is None else weights[idx]
        P[xs] += w
    return dict(P)


def marginal(P, length):
    Q = defaultdict(Fr)
    for s, w in P.items():
        Q[s[:length]] += w
    return Q


def gap_at(P, k, nV):
    """Gap at order k: distinct positive-prob histories (x_0..x_k) with common x_k and different
    next-step laws. Returns (bool, max TV gap, witness)."""
    Pk1 = marginal(P, k + 2)
    Pk = marginal(P, k + 1)
    by_end = defaultdict(list)
    for hist, w in Pk.items():
        if w > 0:
            nxt = tuple(Pk1.get(hist + (y,), Fr(0)) / w for y in range(nV))
            by_end[hist[-1]].append((hist, nxt))
    best = Fr(0)
    wit = None
    for x, lst in by_end.items():
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                tv = sum(abs(a - b) for a, b in zip(lst[i][1], lst[j][1])) / 2
                if tv > best:
                    best = tv
                    wit = (lst[i], lst[j])
    return best > 0, best, wit


def all_perms(N):
    from itertools import permutations
    return permutations(range(N))
