"""REVIEW-1049-r3: independent exact generic checks of the link-sum recovery (ASSESS-1049 r3 sec. 2.4).

WIP / UNVERIFIED; model-written (Claude Code reviewer subagent, 2026-11-09).
Exact integer arithmetic over Z/q only: generic local functions and one-step identities.
No OI mechanism, no observable, no dynamics iterated. Imports nothing from probes/ or review/.
Run: python3 -I rv3_link_affinity.py

Method (different from the writer's K2, which enumerates tables). The condition
    (S)  sum_j [m_j(x_j + c) - m_j(x_j)]  is independent of x, for every c,
is LINEAR in the unknown tables (m_1(.), ..., m_n(.)). Write it as the joint system
    sum_j [m_j(x_j+c) - m_j(x_j)] - sum_j [m_j(c) - m_j(0)] = 0   for all x in (Z/q)^n, c in Z/q
(no slot-wise reduction is used to build it). The affine tuples m_j(v) = a_j v + b_j solve it and
number q^(2n). So the solution set equals the affine set iff it has exactly q^(2n) elements:
  prime q:     rank over GF(q) must be n*q - 2n;
  composite q: |ker A mod q| = q^(cols - r) * prod_i gcd(d_i, q) from the Smith normal form.

V1  link sum + uniform shifts => affine, every slot count n in {1,2,4,6} (d = 1, 2, 3 neighbour
    counts) at primes q in {2,3,5,7} (n = 6 up to q = 7; n = 4 up to q = 11; n = 2 up to q = 13)
    and composite q in {4,6,8,9} (n = 2, 3 where small). Also affine-subset membership check.
V2  internal index K = 2 (alphabet V = (Z/q)^2, slot maps V -> V): shifts by every c in V force
    affinity (q = 2, 3); shifts by the diagonal c(1,1) only do NOT at q = 3 (non-affine solutions
    exist). At q = 2 the diagonal shifts happen to suffice (printed as a NOTE).
V3  separability is load-bearing: general (non-separable) F on n slots with (S) has more solutions
    than the affine ones (q = 3, 5, n = 2).
V4  checker mutation control: dropping the x-dependence of (S) (only x = 0 rows) must be detected
    as a failure (solution set != affine).
V5  P1 constructions re-coded with a different slot order (+x,+y,+z,-x,-y,-z / E,N,W,S): each has
    a nonzero mixed second difference between two neighbour slots (not a link sum); their
    single-slot response is invariant under uniform shifts of the background (all x, c) and
    depends on the background (witness); uniform covariance kappa = 2 (all x, c, units lambda).
V6  F1 scope: at q = 2, d = 3, every centre-free isotropic affine rule a*sum + b satisfies the
    kappa = 2 uniform form; at odd q, a*sum + b with b != 0 fails it via lambda = -1.
"""
import itertools
import math
import sys

import numpy as np
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

FAIL = []


def report(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        FAIL.append(msg)


def is_prime(q):
    return q >= 2 and all(q % p for p in range(2, int(q ** 0.5) + 1))


# ---------------------------------------------------------------- linear-system builders
def rows_linksum(q, n, K=1, shifts='all', only_x0=False):
    """Rows of the joint system (S) for slot maps m_j : (Z/q)^K -> (Z/q)^K.
    Unknown index: (j, v, k) -> j*(q^K*K) + vidx(v)*K + k. One row per (x, c, output comp k)."""
    V = list(itertools.product(range(q), repeat=K))
    vid = {v: i for i, v in enumerate(V)}
    per = len(V) * K
    cols = n * per
    if shifts == 'all':
        C = V
    else:  # diagonal shifts c*(1,...,1)
        C = [tuple([c] * K) for c in range(q)]
    zero = tuple([0] * K)
    X = [tuple([zero] * n)] if only_x0 else list(itertools.product(V, repeat=n))
    add = lambda a, b: tuple((s + t) % q for s, t in zip(a, b))
    rows = []
    for x in X:
        for c in C:
            for k in range(K):
                r = [0] * cols
                for j in range(n):
                    r[j * per + vid[add(x[j], c)] * K + k] += 1
                    r[j * per + vid[x[j]] * K + k] -= 1
                    r[j * per + vid[c] * K + k] -= 1
                    r[j * per + vid[zero] * K + k] += 1
                rows.append(r)
    return rows, cols


def np_rows_k1(q, n):
    """Same joint system (S) as rows_linksum at K = 1, built with numpy (unknown j*q + v)."""
    X = np.array(list(itertools.product(range(q), repeat=n)), dtype=np.int64)  # (q^n, n)
    blocks = []
    for c in range(q):
        A = np.zeros((X.shape[0], n * q), dtype=np.int64)
        for j in range(n):
            base = j * q
            np.add.at(A, (np.arange(X.shape[0]), base + (X[:, j] + c) % q), 1)
            np.add.at(A, (np.arange(X.shape[0]), base + X[:, j]), -1)
            A[:, base + c] -= 1
            A[:, base + 0] += 1
        blocks.append(A)
    return np.vstack(blocks), n * q


def rank_mod_p(rows, p):
    A = np.array(rows, dtype=np.int64) % p
    m, n = A.shape
    r = 0
    for col in range(n):
        piv = None
        nz = np.nonzero(A[r:, col])[0]
        if len(nz):
            piv = r + nz[0]
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        A[r] = (A[r] * pow(int(A[r, col]), -1, p)) % p
        f = A[:, col].copy()
        f[r] = 0
        nzr = np.nonzero(f)[0]
        if len(nzr):
            A[nzr] = (A[nzr] - np.outer(f[nzr], A[r])) % p
        r += 1
        if r == m:
            break
    return r


def kernel_size_mod_q(rows, cols, q):
    """|{u in (Z/q)^cols : A u = 0 mod q}| via Smith normal form over Z."""
    # deduplicate rows to keep SNF small
    uniq = sorted({tuple(r) for r in rows if any(r)})
    if not uniq:
        return q ** cols
    S = smith_normal_form(Matrix(uniq), domain=ZZ)
    diag = [abs(int(S[i, i])) for i in range(min(S.shape)) if S[i, i] != 0]
    size = q ** (cols - len(diag))
    for d in diag:
        size *= math.gcd(d, q)
    return size


def solution_count(rows, cols, q):
    if is_prime(q):
        return q ** (cols - rank_mod_p(rows, q))
    return kernel_size_mod_q(rows, cols, q)


# ---------------------------------------------------------------- V1
def v1():
    cases = [(q, 1) for q in (2, 3, 4, 5, 6, 7, 8, 9)]
    cases += [(q, 2) for q in (2, 3, 4, 5, 6, 7, 8, 9, 11, 13)]
    cases += [(q, 3) for q in (2, 3, 4, 5)]
    cases += [(q, 4) for q in (2, 3, 5, 7, 11)]
    cases += [(q, 6) for q in (2, 3, 5, 7)]
    for q, n in cases:
        if is_prime(q):
            A, cols = np_rows_k1(q, n)
            got = q ** (cols - rank_mod_p(A, q))
        else:
            rows, cols = rows_linksum(q, n)
            got = solution_count(rows, cols, q)
        exp = q ** (2 * n)
        report(got == exp, f"V1 link sum, n={n} slots, q={q}: |solutions| = {got}, affine = {exp}")
    # affine subset membership (the solutions counted above contain every affine tuple)
    for q, n in [(5, 2), (4, 2), (7, 4)]:
        A, cols = np_rows_k1(q, n)
        ok = True
        for j in range(n):
            for kind in ('a', 'b'):
                u = np.zeros(cols, dtype=np.int64)
                for v in range(q):
                    u[j * q + v] = v if kind == 'a' else 1
                ok &= not np.any((A @ u) % q)
        report(ok, f"V1 affine generators solve (S), n={n}, q={q}")


# ---------------------------------------------------------------- V2
def v2():
    for q, n in [(2, 2), (3, 2), (2, 3), (3, 3)]:
        K = 2
        rows, cols = rows_linksum(q, n, K=K, shifts='all')
        got = solution_count(rows, cols, q)
        exp = q ** (n * (K * K + K))  # affine maps V->V: K*K matrix + K offset, per slot
        report(got == exp, f"V2 K=2, shifts by all c in V, n={n}, q={q}: {got} solutions = affine {exp}")
        rows, cols = rows_linksum(q, n, K=K, shifts='diag')
        got = solution_count(rows, cols, q)
        if q == 2:
            # over F_2^2 the only non-affine monomial is x1*x2, whose diagonal-shift difference
            # depends on x, so diagonal shifts already suffice; recorded, not a pass condition
            print(f"NOTE V2 K=2, diagonal shifts only, n={n}, q=2: {got} solutions (affine {exp})")
        else:
            report(got > exp, f"V2 K=2, diagonal shifts only, n={n}, q={q}: {got} solutions > affine {exp} "
                              f"(non-affine admitted)")


# ---------------------------------------------------------------- V3
def v3():
    for q in (3, 5):
        n = 2
        X = list(itertools.product(range(q), repeat=n))
        idx = {x: i for i, x in enumerate(X)}
        rows = []
        for x in X:
            for c in range(q):
                r = [0] * len(X)
                xc = tuple((t + c) % q for t in x)
                cc = tuple([c] * n)
                r[idx[xc]] += 1
                r[idx[x]] -= 1
                r[idx[cc]] -= 1
                r[idx[tuple([0] * n)]] += 1
                rows.append(r)
        got = solution_count(rows, len(X), q)
        aff = q ** (n + 1)
        report(got > aff, f"V3 general F on {n} slots, q={q}: {got} uniformly covariant > affine {aff} "
                          f"(separability load-bearing)")


# ---------------------------------------------------------------- V4
def v4():
    for q, n in [(5, 2), (4, 2)]:
        rows, cols = rows_linksum(q, n, only_x0=True)
        got = solution_count(rows, cols, q)
        report(got != q ** (2 * n), f"V4 mutation (x = 0 rows only) detected, n={n}, q={q}: {got} != {q ** (2 * n)}")


# ---------------------------------------------------------------- V5
def p1_d3(q):
    """slots (+x,+y,+z,-x,-y,-z)."""
    t = pow(3, -1, q)

    def f(v):
        px, py, pz = v[0] + v[3], v[1] + v[4], v[2] + v[5]
        A = (2 * px - py - pz) % q
        B = (2 * py - pz - px) % q
        Cc = (2 * pz - px - py) % q
        P = (A * A + B * B + Cc * Cc) % q
        return (t * sum(v) + A * B * Cc * pow(P, q - 2, q)) % q
    return f


def p1_d3_q2(v):
    return (sum(v) + (1 if min(v) == max(v) else 0)) % 2


def p1_d2_q7(v):
    E, N, W, S = v
    q = 7
    y1, y2, y3 = (E - W) % q, (N - S) % q, (E + W - N - S) % q
    a = (y1 * y1 - y2 * y2) % q
    chi = 0 if a == 0 else (1 if pow(a, 3, q) == 1 else -1)
    return (4 * sum(v) + y3 * chi) % q  # 1/2 = 4 mod 7


def mixed_witness(f, q, n):
    for x in itertools.product(range(q), repeat=n):
        for j, k in itertools.combinations(range(n), 2):
            for a in range(1, q):
                for b in range(1, q):
                    xj = list(x); xj[j] = (xj[j] + a) % q
                    xk = list(x); xk[k] = (xk[k] + b) % q
                    xjk = list(xj); xjk[k] = (xjk[k] + b) % q
                    if (f(tuple(xjk)) - f(tuple(xj)) - f(tuple(xk)) + f(x)) % q:
                        return (x, j, k, a, b)
    return None


def v5():
    cons = [("d=3 q=5", p1_d3(5), 5, 6), ("d=3 q=7", p1_d3(7), 7, 6),
            ("d=3 q=2", p1_d3_q2, 2, 6), ("d=2 q=7", p1_d2_q7, 7, 4)]
    for name, f, q, n in cons:
        w = mixed_witness(f, q, n)
        report(w is not None, f"V5 P1 {name} not a link sum (mixed difference witness {w})")
    lin = lambda v: (4 * sum(v)) % 7
    report(mixed_witness(lin, 7, 4) is None, "V5 control: linear d=2 q=7 is a link sum (no witness)")
    sq = lambda v: sum(t * t for t in v) % 5
    report(mixed_witness(sq, 5, 3) is None, "V5 control: sum x_j^2 (q=5, 3 slots) is a link sum")
    # uniform covariance (kappa = 2), all units, exhaustive, d=2 q=7 and d=3 q=5
    for name, f, q, n in [("d=2 q=7", p1_d2_q7, 7, 4), ("d=3 q=5", p1_d3(5), 5, 6)]:
        ok = True
        for x in itertools.product(range(q), repeat=n):
            fx = f(x)
            for lam in range(1, q):
                for c in range(q):
                    y = tuple((lam * t + c) % q for t in x)
                    if f(y) != (lam * fx + 2 * c) % q:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        report(ok, f"V5 P1 {name}: f(lam x + c1) = lam f(x) + 2c for all x, units lam, c")
    # response invariant under uniform shifts; depends on background (d=2, q=7 exhaustive)
    f, q, n = p1_d2_q7, 7, 4
    inv_ok, dep = True, None
    for x in itertools.product(range(q), repeat=n):
        for j in range(n):
            for dl in range(1, q):
                xd = list(x); xd[j] = (xd[j] + dl) % q
                r0 = (f(tuple(xd)) - f(x)) % q
                for c in range(1, q):
                    xc = tuple((t + c) % q for t in x)
                    xdc = tuple((t + c) % q for t in xd)
                    if (f(xdc) - f(xc)) % q != r0:
                        inv_ok = False
                if dep is None:
                    z = (0,) * n
                    zd = list(z); zd[j] = dl
                    if (f(tuple(zd)) - f(z)) % q != r0:
                        dep = (x, j, dl)
    report(inv_ok, "V5 P1 d=2 q=7: every single-slot response is invariant under uniform shifts")
    report(dep is not None, f"V5 P1 d=2 q=7: response depends on the background (witness {dep})")


# ---------------------------------------------------------------- V6
def v6():
    q = 2
    ok = True
    for a in range(q):
        for b in range(q):
            f = lambda v, a=a, b=b: (a * sum(v) + b) % q
            for x in itertools.product(range(q), repeat=6):
                for c in range(q):
                    if f(tuple((t + c) % q for t in x)) != (f(x) + 2 * c) % q:
                        ok = False
    report(ok, "V6 q=2, d=3: every isotropic centre-free affine a*sum+b satisfies the kappa=2 uniform form")
    for q in (3, 5, 7):
        ok = True
        for b in range(1, q):
            f = lambda v, b=b: (sum(v) + b) % q
            x = (0,) * 6
            y = tuple((-t) % q for t in x)
            if f(y) == (-f(x)) % q:  # lambda = -1, c = 0
                ok = False
        report(ok, f"V6 q={q}: a*sum + b with b != 0 fails lambda = -1 (input not implied by affinity)")


if __name__ == "__main__":
    v1(); v2(); v3(); v4(); v5(); v6()
    print("ALL PASS" if not FAIL else f"{len(FAIL)} FAIL")
    sys.exit(1 if FAIL else 0)
