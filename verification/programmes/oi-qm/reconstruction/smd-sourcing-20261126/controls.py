"""SMD-SRC-1 local controls (paper-only investigation; see PLAN.md section 4).

Part E (CC-E): exact rational arithmetic. Certifies the identities the witnesses of REPORT.md rest on.
Part X (CC-X): floating point. Illustration only; certifies nothing.
Run: python3 -I controls.py   (python >= 3.8, numpy for part X only). Exit status 0 iff every
exact check passes.
"""
from fractions import Fraction as Fr
from itertools import permutations, product
import sys

FAIL = []


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAIL.append(name)


def zeros(n, m=None):
    m = n if m is None else m
    return [[Fr(0)] * m for _ in range(n)]


def eye(n):
    z = zeros(n)
    for i in range(n):
        z[i][i] = Fr(1)
    return z


def mul(a, b):
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(r, c)) for c in bt] for r in a]


def tr(a):
    return [list(r) for r in zip(*a)]


def add(a, b, s=1):
    return [[x + s * y for x, y in zip(r, q)] for r, q in zip(a, b)]


def scal(k, a):
    return [[k * x for x in r] for r in a]


def block(a, b, c, d):
    return [ra + rb for ra, rb in zip(a, b)] + [rc + rd for rc, rd in zip(c, d)]


def is_pos_def(a):
    """Exact LDL^T: True iff every pivot is > 0."""
    n = len(a)
    m = [row[:] for row in a]
    for k in range(n):
        if m[k][k] <= 0:
            return False
        for i in range(k + 1, n):
            f = m[i][k] / m[k][k]
            if f:
                for j in range(k, n):
                    m[i][j] -= f * m[k][j]
    return True


# ---------- spatial part on a torus (Z/L)^d ----------

def sites(d, L):
    return list(product(range(L), repeat=d))


def hop(d, L, mu):
    S = sites(d, L)
    idx = {s: i for i, s in enumerate(S)}
    n = len(S)
    A = zeros(n)
    for s in S:
        for j in range(d):
            for e in (1, -1):
                t = list(s)
                t[j] = (t[j] + e) % L
                A[idx[s]][idx[tuple(t)]] += Fr(mu) / d
    return A, S, idx


def spatial_checks(d, L, mu):
    A, S, idx = hop(d, L, mu)
    n = len(S)
    I, Z = eye(n), zeros(n)
    F = block(Z, I, scal(-1, I), A)                      # F_s(u, v) = (v, A v - u)
    c = block(I, scal(Fr(1, 2), A), scal(Fr(1, 2), A), I)  # c = [[1, A/2], [A/2, 1]]
    D = block(scal(Fr(-1, 2), A), I, scal(-1, I), scal(Fr(1, 2), A))  # D_s = F_s - A/2
    A2 = mul(A, A)
    s2 = add(I, scal(Fr(1, 4), A2), -1)                 # 1 - A^2/4
    s2b = block(s2, Z, Z, s2)
    tag = f"d={d} L={L} mu={mu}"
    check(f"[E1] F c F^T = c ({tag})", mul(mul(F, c), tr(F)) == c)
    check(f"[E2] D c D^T = (1 - A^2/4) c, i.e. J c J^T = c ({tag})", mul(mul(D, c), tr(D)) == mul(s2b, c))
    check(f"[E3] c positive definite ({tag})", is_pos_def(c))
    # negative control: the identity covariance is not F-invariant
    I2 = eye(2 * n)
    check(f"[E4-neg] I_2n is NOT F-invariant (non-vacuity of E1) ({tag})", mul(mul(F, I2), tr(F)) != I2)
    cp = block(I, scal(Fr(1, 3), A), scal(Fr(1, 3), A), I)  # perturbed off-diagonal weight A/3
    check(f"[N1-neg] [[1, A/3], [A/3, 1]] fails E1 and E2 ({tag})",
          mul(mul(F, cp), tr(F)) != cp and mul(mul(D, cp), tr(D)) != mul(s2b, cp))
    c3 = block(I, scal(Fr(3), A), scal(Fr(3), A), I)       # eigenvalue 1 - 6 abs(mu) < 0 at k = 0
    check(f"[N2-neg] [[1, 3A], [3A, 1]] is NOT positive definite (non-vacuity of E3) ({tag})", not is_pos_def(c3))
    # cubic invariance: axis permutations and reflections act by site permutations
    ok = True
    for perm in permutations(range(d)):
        for signs in product((1, -1), repeat=d):
            P = zeros(n)
            for s in S:
                t = tuple((signs[k] * s[perm[k]]) % L for k in range(d))
                P[idx[t]][idx[s]] = Fr(1)
            PP = block(P, zeros(n), zeros(n), P)
            if mul(mul(PP, c), tr(PP)) != c or mul(mul(PP, F), tr(PP)) != F:
                ok = False
    check(f"[E5] c and F invariant under the hyperoctahedral site action ({tag})", ok)
    # translation invariance
    T = zeros(n)
    for s in S:
        t = list(s)
        t[0] = (t[0] + 1) % L
        T[idx[tuple(t)]][idx[s]] = Fr(1)
    TT = block(T, zeros(n), zeros(n), T)
    check(f"[E6] c translation invariant ({tag})", mul(mul(TT, c), tr(TT)) == c)
    # finite range: c(n, m) = 0 for graph distance > 1
    def dist(a, b):
        return sum(min((x - y) % L, (y - x) % L) for x, y in zip(a, b))
    ok = all(c[i + p * n][j + q * n] == 0
             for p in (0, 1) for q in (0, 1)
             for i, a in enumerate(S) for j, b in enumerate(S) if dist(a, b) > 1)
    check(f"[E7] c has range 1 ({tag})", ok)
    # negative controls for E5-E7
    cb = [row[:] for row in c]
    s1 = [0] * d
    s1[0] = 1
    cb[idx[tuple(s1)]][idx[tuple(s1)]] += 1                # bump at one site off the origin
    def perm_inv(Pm, M):
        return mul(mul(Pm, M), tr(Pm)) == M
    refl = zeros(n)
    for s_ in S:
        t = tuple((-x) % L for x in s_)
        refl[idx[t]][idx[s_]] = Fr(1)
    RR = block(refl, zeros(n), zeros(n), refl)
    check(f"[N3-neg] a one-site bump fails the reflection (E5) and translation (E6) checks ({tag})",
          not perm_inv(RR, cb) and not perm_inv(TT, cb))
    c2 = block(I, A2, A2, I)
    ok2 = all(c2[i + p * n][j + q * n] == 0
              for p in (0, 1) for q in (0, 1)
              for i, a in enumerate(S) for j, b in enumerate(S) if dist(a, b) > 1)
    check(f"[N4-neg] [[1, A^2], [A^2, 1]] fails the range-1 check (non-vacuity of E7) ({tag})", not ok2)


# ---------- internal part: the six signed links and the cubic rotation group O ----------

def rotation_group():
    G = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = signs[i]
            det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                   - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                   + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
            if det == 1:
                G.append(M)
    return G


LINKS = [(j, s) for j in range(3) for s in (1, -1)]  # link +e_j / -e_j


def link_rep(M):
    R = zeros(6)
    for a, (j, s) in enumerate(LINKS):
        v = [0, 0, 0]
        v[j] = s
        w = [sum(M[i][k] * v[k] for k in range(3)) for i in range(3)]
        jj = next(i for i in range(3) if w[i] != 0)
        b = LINKS.index((jj, w[jj]))
        R[b][a] = Fr(1)
    return R


def vec(entries):
    v = [Fr(0)] * 6
    for (j, s), x in entries.items():
        v[LINKS.index((j, s))] = Fr(x)
    return v


def outer(u, v):
    return [[x * y for y in v] for x in u]


def internal_checks():
    G = rotation_group()
    check("[E8] |O| = 24", len(G) == 24)
    reps = [link_rep(M) for M in G]
    o = [vec({(j, 1): 1, (j, -1): -1}) for j in range(3)]    # odd combinations: T_1 (unnormalized)
    s = [vec({(j, 1): 1, (j, -1): 1}) for j in range(3)]     # even combinations: A_1 + E
    P_T1 = scal(Fr(1, 2), add(add(outer(o[0], o[0]), outer(o[1], o[1])), outer(o[2], o[2])))
    P_ev = scal(Fr(1, 2), add(add(outer(s[0], s[0]), outer(s[1], s[1])), outer(s[2], s[2])))
    one = [Fr(1)] * 6
    P_A1 = scal(Fr(1, 6), outer(one, one))
    P_E = add(P_ev, P_A1, -1)
    I6 = eye(6)
    check("[E9] P_T1 + P_E + P_A1 = I and the projections are idempotent with traces 3, 2, 1",
          add(add(P_T1, P_E), P_A1) == I6 and all(mul(P, P) == P for P in (P_T1, P_E, P_A1))
          and [sum(P[i][i] for i in range(6)) for P in (P_T1, P_E, P_A1)] == [3, 2, 1])
    check("[E10] the projections commute with every rho(g)",
          all(mul(R, P) == mul(P, R) for R in reps for P in (P_T1, P_E, P_A1)))
    t = o[0]
    e = add([s[0]], [s[1]], -1)[0]                          # s_1 - s_2 lies in E
    check("[E11] t in T_1 and e in E", mul(P_T1, [[x] for x in t]) == [[x] for x in t]
          and mul(P_E, [[x] for x in e]) == [[x] for x in e])
    B = add(outer(t, e), outer(e, t))
    avg = zeros(6)
    for R in reps:
        avg = add(avg, mul(mul(R, B), tr(R)))
    check("[E12] sum over O of rho(h) B rho(h)^T = 0 (second moment of the CC-K mixture is block-scalar)",
          avg == zeros(6))
    check("[E13] [P_T1, B] != 0 (the T_1 phase circle does not fix S = sum kappa_b P_b + eps B)",
          mul(P_T1, B) != mul(B, P_T1))
    distinct = {tuple(map(tuple, mul(mul(R, B), tr(R)))) for R in reps}
    print(f"     number of distinct rho(h) B rho(h)^T over O: {len(distinct)}")
    check("[E14] exactly 12 distinct mixture components rho(h) B rho(h)^T", len(distinct) == 12)
    # positivity of S = sum kappa_b P_b + eps B for kappa = (1, 2, 3), eps = 1/10
    S = add(add(add(scal(Fr(1), P_T1), scal(Fr(2), P_E)), scal(Fr(3), P_A1)), scal(Fr(1, 10), B))
    check("[E15] S = P_T1 + 2 P_E + 3 P_A1 + B/10 positive definite", is_pos_def(S))
    Sbig = add(add(add(scal(Fr(1), P_T1), scal(Fr(2), P_E)), scal(Fr(3), P_A1)), scal(Fr(10), B))
    check("[N5-neg] with eps = 10 the matrix is NOT positive definite (non-vacuity of E15)", not is_pos_def(Sbig))
    # mu = 0 witness: single-site supports
    eps = [add([s[j]], [scal(Fr(1, 3), [add(add([s[0]], [s[1]]), [s[2]])[0]])[0]], -1)[0] for j in range(3)]
    check("[E16] the three E-vectors lie in E", all(mul(P_E, [[x] for x in v]) == [[x] for x in v] for v in eps))
    frameT = add(add(outer(o[0], o[0]), outer(o[1], o[1])), outer(o[2], o[2]))
    frameE = add(add(outer(eps[0], eps[0]), outer(eps[1], eps[1])), outer(eps[2], eps[2]))
    check("[E17] frame identities: sum o_j o_j^T = 2 P_T1, sum eps_j eps_j^T = 2 P_E",
          frameT == scal(Fr(2), P_T1) and frameE == scal(Fr(2), P_E))
    def setof(vs):
        out = set()
        for v in vs:
            for sg in (1, -1):
                out.add(tuple(sg * x for x in v))
        return out
    supT, supE = setof(o), setof(eps)   # rho(g) is real, so {i^K v_j} is rho(g)-invariant iff {+-v_j} is
    ok = all(setof([[sum(R[a][b] * v[b] for b in range(6)) for a in range(6)] for v in o]) == supT and
             setof([[sum(R[a][b] * v[b] for b in range(6)) for a in range(6)] for v in eps]) == supE
             for R in reps)
    check("[E18] the mu = 0 witness supports {i^K o_j}, {i^K eps_j} are invariant under every rho(g)", ok)


def illustration():
    try:
        import numpy as np
    except ImportError:
        print("numpy absent: part X skipped")
        return
    print("\n[X] illustration only (floating point): spreading of f_t = (F^T)^t f, f = delta at the origin in the u-slot")
    for d, Tmax in ((1, 400), (2, 120)):
        for mu in (0.5, 0.9, 0.0):
            N = 2 * Tmax + 9
            shape = (N,) * d
            u = np.zeros(shape); v = np.zeros(shape)
            u[(N // 2,) * d] = 1.0
            rows = []
            for t in range(Tmax + 1):
                if t in (0, 1, 2, 3, Tmax // 8, Tmax // 4, Tmax // 2, Tmax):
                    w = np.concatenate([u.ravel(), v.ravel()])
                    rows.append((t, np.abs(w).max(), (w ** 4).sum() ** 0.25, (w ** 2).sum() ** 0.5))
                # F^T(u, v) = (-v, u + A v) for F(u, v) = (v, A v - u), A symmetric
                Av = sum(np.roll(v, 1, j) + np.roll(v, -1, j) for j in range(d)) * (mu / d)
                u, v = -v, u + Av
            print(f"  d={d} mu={mu}: t, sup|f_t|, ||f_t||_4, ||f_t||_2")
            for r in rows:
                print("    %4d  %.4e  %.4e  %.4e" % r)


if __name__ == "__main__":
    for (d, L, mu) in ((1, 5, Fr(1, 3)), (1, 6, Fr(-3, 5)), (2, 4, Fr(1, 3)), (3, 3, Fr(1, 2))):
        spatial_checks(d, L, mu)
    internal_checks()
    illustration()
    print("\nEXACT CHECKS:", "ALL PASS" if not FAIL else f"{len(FAIL)} FAILED: {FAIL}")
    sys.exit(1 if FAIL else 0)
