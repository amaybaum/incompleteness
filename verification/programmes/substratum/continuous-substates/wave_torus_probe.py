#!/usr/bin/env python3
"""SUBSTATE-1 (#1007) probe: visible recurrence of the lattice wave map lifted to a torus.

The 1-D lattice wave map on a ring of L sites acts on x = (u_t, u_{t-1}) by
    u_{t+1}(n) = u_t(n+1) + u_t(n-1) - u_{t-1}(n).
Its integer matrix F is the map whose reduction mod q is the substratum wave map
(SM Theorem A.1). Here the same F acts on the torus (R/Z)^{2L}: every site value
is a real number mod 1 instead of an element of Z/qZ. The hidden prior is Haar
measure on the torus.

A visible observable is an integer linear form v, read through the two-cell
partition {v.x mod 1 in [0, 1/2)}, {v.x mod 1 in [1/2, 1)}. Facts used:

  (H) If v and w are integer forms of rank 2, then (v.x, w.x) mod 1 is Haar on
      T^2 when x is Haar on T^n (pushforward of Haar measure under a surjective
      homomorphism of compact groups). So the rooted visible map from time 0 to
      a time t with w = v F^t of rank 2 with v is Gamma_t = [[1/2, 1/2], [1/2, 1/2]].
  (R) If v M = 0 with M = F^L - I and M^2 = 0, then v F^{mL} = v (I + mM) = v,
      so the visible cell returns exactly at every t = mL: Gamma_{mL} = I.

Everything below is exact integer or rational arithmetic. Controls run first;
verdicts are printed only if every control passes.
"""
import json
import sys
from fractions import Fraction


def wave_matrix(L):
    n = 2 * L
    A = [[0] * n for _ in range(n)]
    for i in range(L):
        A[i][(i + 1) % L] += 1
        A[i][(i - 1) % L] += 1
        A[i][L + i] -= 1
        A[L + i][i] = 1
    return A


def mat_mul(A, B, mod=None):
    n, k, m = len(A), len(B), len(B[0])
    C = [[sum(A[i][j] * B[j][l] for j in range(k)) for l in range(m)] for i in range(n)]
    if mod is not None:
        C = [[x % mod for x in row] for row in C]
    return C


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mat_pow(A, e):
    R, B = identity(len(A)), A
    while e:
        if e & 1:
            R = mat_mul(R, B)
        B = mat_mul(B, B)
        e >>= 1
    return R


def row_mul(v, A):
    return [sum(v[k] * A[k][j] for k in range(len(v))) for j in range(len(A[0]))]


def order_mod(A, q, bound):
    n, P = len(A), [row[:] for row in A]
    I = identity(n)
    for t in range(1, bound + 1):
        if [[x % q for x in row] for row in P] == I:
            return t
        P = mat_mul(P, A, q)
    return None


def proportional_times(v, F, M, L):
    """Exactly decide every t = mL + r (m >= 0, 0 <= r < L, t >= 1) with v F^t = c v.

    v F^{mL+r} = a + m b with a = v F^r, b = a M (M^2 = 0, F and M commute).
    Returns a list of (r, m or 'all m', c); the empty list means never proportional.
    """
    hits = []
    for r in range(L):
        a = row_mul(v, mat_pow(F, r))
        b = row_mul(a, M)
        if not any(b):  # m drops out: need a = c v
            c = ratio(a, v)
            if c is not None:
                hits.append((r, "all m" if r else "all m >= 1", str(c)))
            continue
        # solve a_j + m b_j = c v_j for rationals (m, c)
        sol = solve_two(a, b, v)
        if sol is not None:
            m, c = sol
            if m.denominator == 1 and m >= 0 and not (r == 0 and m == 0):
                hits.append((r, int(m), str(c)))
    return hits


def ratio(a, v):
    c = None
    for x, y in zip(a, v):
        if y == 0:
            if x != 0:
                return None
        else:
            q = Fraction(x, y)
            if c is None:
                c = q
            elif q != c:
                return None
    return c


def solve_two(a, b, v):
    rows = [(Fraction(b[j]), Fraction(-v[j]), Fraction(-a[j])) for j in range(len(v))]
    for i in range(len(rows)):
        for k in range(i + 1, len(rows)):
            (p1, q1, s1), (p2, q2, s2) = rows[i], rows[k]
            det = p1 * q2 - q1 * p2
            if det != 0:
                m = (s1 * q2 - q1 * s2) / det
                c = (p1 * s2 - s1 * p2) / det
                if all(p * m + q * c == s for p, q, s in rows):
                    return m, c
                return None
    raise AssertionError("degenerate system: b and v parallel; not expected here")


def grid_gamma(L, N, v, t, cell=None):
    """Exact rooted visible map on the finite subgroup (Z/N)^{2L} of the torus (N even).

    F preserves this subgroup, and its uniform measure is the finite substratum with
    alphabet Z/NZ. The visible cell of x is [v.x mod N < N/2]. Returns Gamma_t as
    a 2x2 matrix of Fractions (rows: initial cell, columns: cell at time t).
    """
    import itertools
    if cell is None:
        cell = lambda y: int(y % N >= N // 2)  # most significant digit: real-type coarse cell
    n = 2 * L
    w = row_mul(v, mat_pow(wave_matrix(L), t))
    counts = [[0, 0], [0, 0]]
    for x in itertools.product(range(N), repeat=n):
        a = cell(sum(c * y for c, y in zip(v, x)))
        b = cell(sum(c * y for c, y in zip(w, x)))
        counts[a][b] += 1
    return [[Fraction(c, sum(row)) for c in row] for row in counts]


def unit(n, i):
    return [int(k == i) for k in range(n)]


def main():
    controls, findings, ok = [], {}, True

    # Control 1: F mod q has order qL for prime q not dividing L (SM Theorem A.1).
    for L in (3, 4, 5):
        for q in (3, 5, 7):
            if L % q == 0:
                continue
            got = order_mod(wave_matrix(L), q, q * L + 1)
            passed = got == q * L
            ok &= passed
            controls.append({"control": "order F mod q == qL", "L": L, "q": q, "order": got, "pass": passed})

    # Control 3 (independent of (H) and (R)): exact counts on the finite subgroup (Z/8)^6, L = 3.
    half = Fraction(1, 2)
    uniform = [[half, half], [half, half]]
    eye = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    L, N = 3, 8
    site, diff = unit(6, 0), [1, -1, 0, 0, 0, 0]
    checks = [
        ("u0 Gamma_1 uniform", grid_gamma(L, N, site, 1) == uniform),
        ("u0-u1 Gamma_1 uniform", grid_gamma(L, N, diff, 1) == uniform),
        ("u0-u1 Gamma_L == I", grid_gamma(L, N, diff, L) == eye),
        ("u0 Gamma_L != I", grid_gamma(L, N, site, L) != eye),
    ]
    for name, passed in checks:
        ok &= passed
        controls.append({"control": f"grid (Z/{N})^6: {name}", "L": L, "pass": passed})
    # Recurrence time of the single-site observable on the alphabet Z/N grows with N,
    # while the difference observable returns at L for every N (consequence of (R)).
    orders = {str(N): order_mod(wave_matrix(3), N, 3 * N * N) for N in (2, 4, 8, 16)}
    findings["grid_orders_L3"] = orders
    # Least significant digit as the visible cell (p-adic-type coarse cell, p = 2): the
    # higher digits never feed the lowest one, so the cell returns at ord(F mod 2) = 6
    # on every grid Z/2^k, while the most significant digit returns only at ord(F mod 2^k).
    low = lambda y: y % 2
    t2 = order_mod(wave_matrix(3), 2, 100)
    findings["low_digit_L3_N8"] = {
        "ord_F_mod_2": t2,
        "u0_Gamma_1_low_digit": [[str(x) for x in r] for r in grid_gamma(3, 8, site, 1, low)],
        "u0_Gamma_ordmod2_low_digit_is_I": grid_gamma(3, 8, site, t2, low) == eye,
        "u0_Gamma_ordmod2_high_digit_is_I": grid_gamma(3, 8, site, t2) == eye,
    }

    for L in range(3, 11):
        n = 2 * L
        F = wave_matrix(L)
        M = [[x - int(i == j) for j, x in enumerate(row)] for i, row in enumerate(mat_pow(F, L))]
        # Control 2: M = F^L - I is nonzero and squares to zero over Z (SM Theorem A.2 over Z).
        m_nonzero = any(any(r) for r in M)
        m_sq_zero = not any(any(r) for r in mat_mul(M, M))
        passed = m_nonzero and m_sq_zero
        ok &= passed
        controls.append({"control": "M != 0 and M^2 == 0", "L": L, "pass": passed})

        site = unit(n, 0)
        nn_diff = [p - q for p, q in zip(unit(n, 0), unit(n, 1))]
        nnn_diff = [p - q for p, q in zip(unit(n, 0), unit(n, 2))]
        entry = {}
        for name, v in (("u0", site), ("u0-u1", nn_diff), ("u0-u2", nnn_diff)):
            vm_zero = not any(row_mul(v, M))
            entry[name] = {
                "vM_zero": vm_zero,
                "proportional_times": proportional_times(v, F, M, L),
            }
        findings[str(L)] = entry

    if not ok:
        print(json.dumps({"controls": controls, "verdict": "VOID: a control failed"}, indent=1))
        return 1

    # Verdicts generated from the measurements.
    verdict = {}
    for L, e in findings.items():
        if not L.isdigit():
            continue
        v = {}
        s = e["u0"]
        v["u0"] = ("never proportional for t >= 1: Gamma_t = uniform for every t >= 1 (H); "
                   "Gamma_t = Gamma_s Pi with Pi uniform, so P-divisible; no visible recurrence"
                   if not s["proportional_times"] else f"proportional at {s['proportional_times']}")
        for name in ("u0-u1", "u0-u2"):
            s = e[name]
            if s["vM_zero"]:
                inner = [h for h in s["proportional_times"] if h[0] != 0]
                v[name] = ("vM = 0: exact visible return at every t = mL (R); "
                           + ("Gamma_s uniform for 0 < s < L (H), so P-indivisible on {0..L} by the stochastic-inverse lemma"
                              if not inner else f"exceptions within the cycle at (r, m, c) = {inner}; Gamma_1 uniform (H)"))
            else:
                v[name] = "vM != 0: the parabolic-mode drift reaches this observable; no exact return at t = mL"
        verdict[L] = v

    print(json.dumps({"controls": controls, "findings": findings, "verdict": verdict}, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
