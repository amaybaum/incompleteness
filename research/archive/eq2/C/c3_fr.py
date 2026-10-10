"""EQ2-C, C3 target 2: FiniteRank.

Written theorem under test (Theorem FR-R, RESULT.md): for a stage tower D with SC-inf, with body = body D in
l^inf(Label D) and the operational metric = the l^inf norm (sup over stage effects):
  FiniteRank(body)  <=>  UFR  and  (N),
  UFR  : for every eps > 0 there is a stage i with ||x - y|| <= d_i(x, y) + eps on body x body
         (d_i = sup over stage-i effects); equivalently (Dini / total boundedness) body is compact;
  (N)  : body - body contains a ball {v in span(body - body) : ||v|| <= kappa}, kappa > 0 (uniform norming).
  (<=) Riesz: the kappa-ball is closed in the compact body - body, so the span is finite-dimensional.
  (=>) finite dimension: closed bounded => compact (=> UFR by Dini); relative interior => (N).

DECISION RULE (fixed before the first run). The verdict prints only if all checks pass:
  RT  the renewal tower (passive protocol tower of the shift on a stationary renewal process with gap law
      f(k) = 4/(k(k+1)(k+2)), an invariant measure, a bijective dynamics and a binary readout):
      RT.1 f is a probability law with mean 2 (exact closed forms on partial sums);
      RT.2 the Hankel submatrix [P(1 0^(i+j) 1)] of the stage tables is nonsingular for n = 1..12 (rank >= n);
      RT.3 controls: the geometric gap law (i.i.d. bits) gives Hankel rank 1, a two-geometric mixture rank 2;
      RT.4 survival S(a) = 2/((a+1)(a+2)) (exact) and P(renewal within m | age a) decreasing in a;
      RT.5 the age states a_k = 16^k, k = 0..8, are pairwise >= 1/3 apart in the operational metric (one stage
           effect separates each pair): the body is not totally bounded, so UFR fails; with RT.2, not FiniteRank.
  EL  the ellipsoid tower of EQ-A (semi-axes 1/k): (N) fails at every kappa = 1/m (exact witness 2/m e_(m+1)),
      UFR holds (written tail bound; printed as a note, not a check).
  L2  the l2 tower of EQ-A: (N) holds with kappa = 1 (written note), UFR fails (EQ-A's exact 7/10 separation,
      re-derived here for one pair).
Exact arithmetic only (Fraction).
"""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c_common import Checks  # noqa: E402

C = Checks("c3_fr")


def det(M):
    A = [list(r) for r in M]
    n = len(A)
    d = Fr(1)
    for c in range(n):
        p = next((i for i in range(c, n) if A[i][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        for i in range(c + 1, n):
            if A[i][c] != 0:
                f = A[i][c] / A[c][c]
                A[i] = [A[i][k] - f * A[c][k] for k in range(n)]
    return d


def rank(M):
    A = [list(r) for r in M]
    rows, cols = len(A), len(A[0])
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [A[i][k] - f * A[r][k] for k in range(cols)]
        r += 1
        if r == rows:
            break
    return r


# ----------------------------------------------------------------------------- RT: the renewal tower

print("== RT the stationary renewal process with gap law f(k) = 4/(k(k+1)(k+2))")
f = lambda k: Fr(4, k * (k + 1) * (k + 2))  # noqa: E731
okA = all(sum(f(k) for k in range(1, N + 1)) == 1 - Fr(2, (N + 1) * (N + 2)) and
          sum(k * f(k) for k in range(1, N + 1)) == 2 - Fr(4, N + 2) for N in range(1, 60))
C.check("RT.1 partial sums: sum_(k<=N) f = 1 - 2/((N+1)(N+2)) -> 1 and sum_(k<=N) k f = 2 - 4/(N+2) -> 2 "
        "(N = 1..59): a gap law with mean 2, so the stationary renewal process exists with P(1) = 1/2", okA)
P1 = Fr(1, 2)
hank_ok = True
dets = []
for n in range(1, 13):
    H = [[P1 * f(i + j + 1) for j in range(n)] for i in range(n)]
    dd = det(H)
    dets.append(dd != 0)
    hank_ok &= dd != 0
C.check("RT.2 the joint table entries P(1 0^(i+j) 1) = P(1) f(i+j+1) (pasts 1 0^i, futures 0^j 1) form a nonsingular "
        f"n x n Hankel matrix for n = 1..12 ({sum(dets)}/12): stage ranks are unbounded (rank-thread R0: not FiniteRank)",
        hank_ok)
g = lambda k: Fr(1, 2 ** k)  # noqa: E731
mix = lambda k: Fr(1, 2) * Fr(1, 2 ** k) + Fr(1, 2) * Fr(2, 3 ** k)  # noqa: E731
C.check("RT.3 controls: geometric gaps (i.i.d. fair bits) give Hankel rank 1; a mixture of two geometrics gives rank 2 "
        "(the rank test is not vacuous)",
        rank([[g(i + j + 1) for j in range(8)] for i in range(8)]) == 1 and
        rank([[mix(i + j + 1) for j in range(8)] for i in range(8)]) == 2 and
        abs(sum(mix(k) for k in range(1, 200)) - 1) < Fr(1, 10 ** 30))
S = lambda a: Fr(2, (a + 1) * (a + 2))  # noqa: E731
C.check("RT.4a survival S(a) = P(gap > a) = 2/((a+1)(a+2)) equals 1 - sum_(k<=a) f(k) (a = 0..80)",
        all(S(a) == 1 - sum(f(k) for k in range(1, a + 1)) for a in range(0, 81)))
ren = lambda m, a: 1 - S(a + m) / S(a)  # noqa: E731  P(renewal within m steps | age a)
C.check("RT.4b P(renewal within m | age a) = 1 - (a+1)(a+2)/((a+m+1)(a+m+2)) is strictly decreasing in the age a "
        "(m = 1..30, a = 0..60)", all(ren(m, a) > ren(m, a + 1) for m in range(1, 31) for a in range(0, 60)))
ages = [16 ** k for k in range(9)]
sep = min(abs(ren(ages[k], ages[k]) - ren(ages[k], ages[l])) for k in range(9) for l in range(k + 1, 9))
C.check(f"RT.5 the age states a_k = 16^k (k = 0..8) are pairwise separated by the stage effect 'renewal within a_k "
        f"steps': minimum separation {sep} >= 1/3; written for all k: ren(a,a) >= 1/2 and ren(a, b) <= 33/289 for "
        "b >= 16a, so the body is not totally bounded: UFR fails", sep >= Fr(1, 3) and
        all(ren(a, a) >= Fr(1, 2) and ren(a, 16 * a) <= Fr(33, 289) for a in range(1, 400)))

# ----------------------------------------------------------------------------- EL: the ellipsoid tower (EQ-A)

print("== EL the compact ellipsoid tower E = {sum_k k^2 x_k^2 <= 1} (EQ-A C2)")
in2E = lambda v: sum((k + 1) ** 2 * v[k] ** 2 for k in range(len(v))) <= 4  # noqa: E731  v in E - E = 2E
okN = True
for m in range(1, 40):
    v = [Fr(0)] * (m + 1) + [Fr(2, m)]          # 2/m e_(m+2) in 0-based index m+1 -> semi-axis 1/(m+2)
    opnorm = Fr(1, 2) * Fr(2, m)                # sup over unit u of |<u, v>|/2 = |v|_2 / 2 = 1/m
    okN &= (opnorm == Fr(1, m)) and not in2E(v)
C.check("EL.1 (N) fails: for every kappa = 1/m (m = 1..39) the vector 2/m e_(m+2) has operational norm kappa and lies "
        "outside E - E = 2E", okN)
C.note("EL.2 (written, not a check) UFR holds: every x in E has tail |x_(>n)|_2 <= 1/(n+1) (since "
       "sum_(k>n) x_k^2 <= (n+1)^-2 sum_(k>n) k^2 x_k^2), so stage n fixes every effect value to within 2/(n+1) "
       "uniformly on E; E is compact (EQ-A C2)")

# ----------------------------------------------------------------------------- L2: the l2 tower (EQ-A)

print("== L2 the l2 tower (EQ-A A, C)")
u = (Fr(3, 5), Fr(-4, 5))
ej, ek = (Fr(1), Fr(0)), (Fr(0), Fr(1))
e_u = lambda x: (1 + u[0] * x[0] + u[1] * x[1]) / 2  # noqa: E731
C.check("L2.1 UFR fails: the stage effect along (3/5) e_j - (4/5) e_k separates e_j and e_k by 7/10, for every pair "
        "j != k (EQ-A's witness, re-derived)", e_u(ej) - e_u(ek) == Fr(7, 10))
C.note("L2.2 (written, not a check) (N) holds with kappa = 1: the operational norm of v is |v|_2 / 2 (rational "
       "unit directions are dense) and body - body = 2B contains {|v|_2 / 2 <= 1}")

sys.exit(C.finish("FR-UFR-N: the renewal tower is an exact OI-shaped passive protocol tower with SC-inf, unbounded "
                  "rank and no uniform finite resolution; the ellipsoid tower separates UFR from (N), the l2 tower (N) "
                  "from UFR; with the written Theorem FR-R (Riesz both ways) FiniteRank <=> UFR and (N)"))
