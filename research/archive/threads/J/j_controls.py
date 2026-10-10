#!/usr/bin/env python3
"""Thread J controls: the sharp-seed completion question.  Exact arithmetic only (Fraction, Q(sqrt3)).

Sections
  T   positive towers: classical simplex tower; an illustrative consistent disk tower (surrogate, not OI-sourced)
  C1a stage consistency fails  -> the carried 1/0 values are lost (finite affine dimension)
  C1b limit of stage seeds in the countable-simplex completion loses sharpness; the escape state; a fixed-stage
      seed survives (infinite affine dimension)
  C2  SIC realization of the Bloch ball over Q(sqrt3)
  C3  classical finite simplex (passes trivially)
  M   matrix-regime analogue (region inclusion X -> X (x) 1); imported field, not field-neutral
Written steps are printed as NOTE lines and are not counted as checks.
"""
from fractions import Fraction as F
from itertools import combinations
import sys

CHECKS = 0
NOTES = 0


def check(cond, label):
    global CHECKS
    if not cond:
        print("FAIL", label)
        sys.exit(1)
    CHECKS += 1
    print("ok  ", label)


def note(text):
    global NOTES
    NOTES += 1
    print("NOTE", text)


def rank(rows):
    m = [list(map(F, r)) for r in rows]
    rk, col = 0, 0
    ncols = len(m[0]) if m else 0
    while rk < len(m) and col < ncols:
        piv = next((i for i in range(rk, len(m)) if m[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        m[rk], m[piv] = m[piv], m[rk]
        for i in range(len(m)):
            if i != rk and m[i][col] != 0:
                f = m[i][col] / m[rk][col]
                m[i] = [a - f * b for a, b in zip(m[i], m[rk])]
        rk += 1
        col += 1
    return rk


# ---------------------------------------------------------------- T: positive towers
print("== T1 classical simplex tower  Delta_0 < Delta_1 < ... (forward maps = inclusions)")


def simplex_stage(n):
    # preparations delta_0..delta_n and the uniform mixture; readbacks: unit, pi_0..pi_n
    P = {("d", j): {("pi", i): F(int(i == j)) for i in range(n + 1)} for j in range(n + 1)}
    P[("mix", n)] = {("pi", i): F(1, n + 1) for i in range(n + 1)}
    for x in P:
        P[x]["unit"] = F(1)
    return P


N = 8
for n in range(1, N):
    S, T_ = simplex_stage(n), simplex_stage(n + 1)
    cons = all(T_[x][e] == S[x][e] for x in S if x[0] == "d" for e in S[x])
    check(cons, f"T1 stage {n}->{n+1}: carried point masses keep every carried table entry (SC)")
    check(all(0 <= v <= 1 for x in T_ for v in T_[x].values()), f"T1 stage {n+1}: table in [0,1]")
    check(T_[("d", 0)][("pi", 0)] == 1 and T_[("d", 1)][("pi", 0)] == 0,
          f"T1 stage {n+1}: seed pi_0 is 1 on delta_0 and 0 on delta_1")
    check(all(sum(T_[x][("pi", i)] for i in range(n + 2)) == T_[x]["unit"] for x in T_),
          f"T1 stage {n+1}: visible partition sums to the unit on every preparation")

print("== T2 consistent disk tower (illustrative surrogate: rational unit vectors, effects (1+u.r)/2)")


def pyth(k):
    a, b = k + 1, 1  # (a^2-b^2, 2ab)/(a^2+b^2), rational unit vectors
    return (F(a * a - b * b, a * a + b * b), F(2 * a * b, a * a + b * b))


dirs = [(F(1), F(0)), (F(0), F(1))] + [pyth(k) for k in range(1, 7)]
for u in dirs:
    check(u[0] ** 2 + u[1] ** 2 == 1, f"T2 direction {u} is a rational unit vector")


def eff(u, r):
    return (1 + u[0] * r[0] + u[1] * r[1]) / 2


for n in range(2, len(dirs) + 1):
    preps = [d for d in dirs[:n]] + [(-d[0], -d[1]) for d in dirs[:n]]
    tab = {(u, r): eff(u, r) for u in dirs[:n] for r in preps}
    check(all(0 <= v <= 1 for v in tab.values()), f"T2 stage {n}: table in [0,1]")
    check(tab[(dirs[0], dirs[0])] == 1 and tab[(dirs[0], (-dirs[0][0], -dirs[0][1]))] == 0,
          f"T2 stage {n}: seed (1+x.r)/2 is 1 on +x and 0 on -x")
note("T2 consistency is by construction (one formula for every stage); the tower is a surrogate for the "
     "completion's shape, not an OI construction.")

# ---------------------------------------------------------------- C1a: SC fails
print("== C1a two-stage tower violating stage consistency")
sigma = {"x": {"u": F(1), "e": F(1)}, "y": {"u": F(1), "e": F(0)}}
tau = {"x": {"u": F(1), "e": F(1, 2)}, "y": {"u": F(1), "e": F(0)}}  # same carried objects, new entry at (e,x)
check(all(0 <= v <= 1 for s in (sigma, tau) for x in s for v in s[x].values()), "C1a both tables valid stages")
check(sigma["x"]["e"] == 1 and sigma["y"]["e"] == 0, "C1a seed sharp at stage sigma")
check(tau["x"]["e"] != sigma["x"]["e"], "C1a SC fails at (e, x)")
check(tau["x"]["e"] < 1, "C1a with the later stage's value the seed is not certain at x_v: sharpness lost")
check(rank([[tau["y"][k] - tau["x"][k] for k in ("u", "e")]]) <= 1, "C1a affine dimension <= 1 (finite rank)")
note("C1a: without SC the carried value p(e_v|x_v) is not a well-defined function on the colimit; any choice "
     "rule other than 'the first stage' loses the 1.")

# ---------------------------------------------------------------- C1b: countable simplex completion
print("== C1b countable-simplex completion in [0,1]^{E_inf}, product topology")


def delta(n, M):  # coordinates (unit, pi_0..pi_{M-1})
    return [F(1)] + [F(int(i == n)) for i in range(M)]


ZERO = lambda M: [F(1)] + [F(0)] * M  # the escape state: unit 1, every visible coordinate 0
for M in range(1, 11):
    check(all(delta(n, M) == ZERO(M) for n in range(M, 25)),
          f"C1b delta_n agrees with the escape state on the first {M} visible coordinates for all n>={M}")
note("C1b: hence delta_n -> 0̸ (escape state) in the product topology; 0̸ lies in the closed hull Omega_inf.")
for M in range(1, 11):
    check(sum(ZERO(M)[1:]) == 0 and ZERO(M)[0] == 1,
          f"C1b escape state: sum of the first {M} visible coordinates is 0 while the unit is 1")
note("C1b: the infinite visible partition is not a test on Omega_inf (the escape state has no visible value); "
     "a finite stage partition still is, being a closed linear condition on finitely many coordinates.")
# limit of stage seeds e_n = pi_n, each sharp at its stage on (delta_n, delta_0)
for n in range(1, 12):
    check(delta(n, 12)[1 + n] == 1 and delta(0, 12)[1 + n] == 0, f"C1b stage seed pi_{n} sharp on (delta_{n}, delta_0)")
mixes = [[F(1, 2), F(1, 3), F(1, 6)], [F(1, 4)] * 4, [F(1)]]
for w in mixes:
    K = len(w)
    z = [F(1)] + [w[i] if i < K else F(0) for i in range(30)]
    check(all(z[1 + n] == 0 for n in range(K, 30)), f"C1b pi_n -> 0 on the mixture {w} (n >= {K})")
check(all(ZERO(30)[1 + n] == 0 for n in range(30)), "C1b pi_n = 0 on the escape state for every n")
check(all(delta(n, 30)[1 + n] == 1 for n in range(30)) and ZERO(30)[1:] == [0] * 30,
      "C1b lim e_n(delta_n) = 1 but (lim e_n)(lim delta_n) = 0: the limit of stage seeds is never certain")
# fixed-stage seed survives
check(delta(0, 30)[1] == 1 and delta(1, 30)[1] == 0 and 0 <= ZERO(30)[1] <= 1,
      "C1b fixed-stage seed pi_0: 1 on delta_0, 0 on delta_1, in [0,1] at the escape state")
for K in range(1, 9):
    rows = [[a - b for a, b in zip(delta(j, K + 1), delta(0, K + 1))] for j in range(1, K + 1)]
    check(rank(rows) == K, f"C1b delta_0..delta_{K} affinely independent: affine dimension >= {K} (rank unbounded)")

# ---------------------------------------------------------------- C2: SIC ball over Q(sqrt3)
print("== C2 SIC realization of the Bloch ball, exact in Q(sqrt3)")


class Q3:
    def __init__(s, a, b=0):
        s.a, s.b = F(a), F(b)

    def __add__(s, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return Q3(s.a + o.a, s.b + o.b)

    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return Q3(s.a - o.a, s.b - o.b)

    def __mul__(s, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return Q3(s.a * o.a + 3 * s.b * o.b, s.a * o.b + s.b * o.a)

    __rmul__ = __mul__

    def __eq__(s, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return s.a == o.a and s.b == o.b

    def pos(s):  # a + b sqrt3 > 0, exactly
        a, b = s.a, s.b
        if a >= 0 and b >= 0:
            return a > 0 or b > 0
        if a <= 0 and b <= 0:
            return False
        return (a * a > 3 * b * b) if a > 0 else (3 * b * b > a * a)

    def __repr__(s):
        return f"({s.a} + {s.b}√3)"


INV_SQRT3 = Q3(0, F(1, 3))
check((not Q3(1, -1).pos()) and Q3(-1, 1).pos() and not Q3(2, -1).pos() is False, "C2 mutation: exact sign test (1-√3<0, -1+√3>0, 2-√3>0)")
B = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]  # a_i = b_i / sqrt3
dot = lambda u, v: sum(x * y for x, y in zip(u, v))
check(all(dot(B[i], B[j]) == (3 if i == j else -1) for i in range(4) for j in range(4)), "C2 tetrahedral Gram")
check(all(sum(b[k] for b in B) == 0 for k in range(3)), "C2 sum a_i = 0")
check(all(sum(b[k] * b[l] for b in B) == (4 if k == l else 0) for k in range(3) for l in range(3)),
      "C2 sum b_i b_i^T = 4 I")
# (i) the sharp operational coordinate (1+z)/2 as a response c.p, p_i(r) = (1 + a_i.r)/4
c = [Q3(F(1, 2), F(b[2], 2)) for b in B]  # c_i = 1/2 + (3/2) a_iz = 1/2 + (sqrt3/2) b_iz
const = sum(c, Q3(0)) * Q3(F(1, 4))
check(const == Q3(F(1, 2)), "C2(i) constant term of c.p(r) is 1/2")
for k in range(3):
    lin = sum((ci * b[k] for ci, b in zip(c, B)), Q3(0)) * INV_SQRT3 * Q3(F(1, 4))
    check(lin == Q3(F(int(k == 2), 2)), f"C2(i) coefficient of r_{k} of c.p(r) is {F(int(k==2),2)}")
check(rank([[F(b[k]) for k in range(3)] for b in B]) == 3,
      "C2(i) the ball image spans aff(Delta_3), so the response vector c is unique")
check(max(c, key=lambda q: (q.b, q.a)) == Q3(F(1, 2), F(1, 2)) and (Q3(F(1, 2), F(1, 2)) - 1).pos(),
      "C2(i) c_max = 1/2 + √3/2 > 1: the sharp coordinate is an effect on the ball, not a response effect (Main.md:540)")
# (ii) no visible-partition indicator 1_T is sharp on the ball
for size in range(0, 5):
    for T in combinations(range(4), size):
        s = [sum(B[i][k] for i in T) for k in range(3)]
        s2 = dot(s, s)
        # max = |T|/4 + |s|/(4 sqrt3), min = |T|/4 - |s|/(4 sqrt3); sharp iff |T| = 2 and |s|^2 = 12
        sharp = (size == 2 and s2 == 12)
        maxone = (3 * (4 - size) ** 2 == s2)
        minzero = (3 * size ** 2 == s2)
        check(not sharp and not (maxone and minzero and 0 < size < 4),
              f"C2(ii) T={T}: |T|={size}, |s_T|^2={s2}; certain somewhere={maxone}, zero somewhere={minzero}; not sharp")
# (iii) conditioning on a visible cell leaves the ball image
for i in range(4):
    for j in range(4):
        if i != j:  # p_i(-a_j) = (1 - a_i.a_j)/4 = (1 + 1/3)/4
            check(F(1, 4) * (1 - F(dot(B[i], B[j]), 3)) == F(1, 3), f"C2(iii) p_{i}(-a_{j}) = 1/3")
note("C2(iii): p_i(r) = 0 iff a_i.r = -1 with |r|<=1, iff r = -a_i (Cauchy-Schwarz equality); with the 1/3 checks, "
     "no ball state has two zero coordinates, so a state conditioned on a cell of size <= 2 is not in the ball image, "
     "and p_i(r) = 1 needs a_i.r = 3 > |r|. Closing the body under visible conditioning adds the vertices of "
     "Delta_3, so the closed body is Delta_3 and the ball geometry is gone.")

# ---------------------------------------------------------------- C3: classical finite simplex
print("== C3 classical finite simplex Delta_3, constant tower")
S3 = simplex_stage(3)
check(all(S3[x][e] == simplex_stage(3)[x][e] for x in S3 for e in S3[x]), "C3 constant tower is consistent")
check(S3[("d", 2)][("pi", 2)] == 1 and S3[("d", 0)][("pi", 2)] == 0, "C3 seed pi_2 sharp on (delta_2, delta_0)")
check(all(sum(S3[x][("pi", i)] for i in range(4)) == 1 for x in S3), "C3 partition of unity on every preparation")

# ---------------------------------------------------------------- M: matrix-regime analogue
print("== M region inclusion X -> X (x) 1 (matrix regime, imported field; RL:102, RL:116, RL:125)")


def kron(A, Bm):
    n, m = len(A), len(Bm)
    return [[A[i // m][j // m] * Bm[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def mm(A, Bm):
    return [[sum(A[i][k] * Bm[k][j] for k in range(len(Bm))) for j in range(len(Bm[0]))] for i in range(len(A))]


tr = lambda A: sum(A[i][i] for i in range(len(A)))
I2 = [[F(1), F(0)], [F(0), F(1)]]
X = [[F(1), F(0)], [F(0), F(0)]]
XI = kron(X, I2)
check(mm(XI, XI) == XI, "M (X (x) 1)^2 = X (x) 1: the included projector stays sharp")
rho = [[F(3, 10), F(1, 10), F(0), F(1, 20)], [F(1, 10), F(1, 5), F(1, 30), F(0)],
       [F(0), F(1, 30), F(1, 4), F(1, 40)], [F(1, 20), F(0), F(1, 40), F(1, 4)]]
ptr = [[rho[2 * a][2 * b] + rho[2 * a + 1][2 * b + 1] for b in range(2)] for a in range(2)]
check(tr(mm(XI, rho)) == tr(mm(X, ptr)), "M duality tr((X(x)1) rho) = tr(X restrict(rho)) (exact instance)")
sig = [[F(2, 3), F(1, 5)], [F(1, 5), F(1, 3)]]
check(tr(mm(XI, kron(X, sig))) == 1 and tr(mm(XI, kron([[F(0), F(0)], [F(0), F(1)]], sig))) == 0,
      "M the pair |0><0| (x) s, |1><1| (x) s keeps the values 1/0")

print(f"OK -- {CHECKS} checks, {NOTES} written notes")
