"""Thread I exact checks (Fractions only; no floats).

Mirrors landed definitions at 6d0abf6b:
  ClassicalBranchDomain (DomainGlue.lean:134): shell / evolve w -> w o phi / branch i
  BranchDomainK (ObservabilityQuotient.lean:108): graded by evolution steps
  itiRelK / itiRelInf (ObservabilityQuotient.lean:79,83)
  ball3, rot3, cyc3, ball3Drive, ballEffect (KInfFoundations.lean:311,411,425,449,1026)
Each check prints PASS/FAIL; script exits nonzero on any FAIL.
"""
from fractions import Fraction as F
from itertools import product
import sys

fails = 0
count = 0


def check(name, cond):
    global fails, count
    count += 1
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails += 1


# ---------------------------------------------------------------- (a) passive
def perm_pow(phi, k):
    n = len(phi)
    out = list(range(n))
    for _ in range(k):
        out = [phi[x] for x in out]
    return out


def order(phi):
    k = 1
    while perm_pow(phi, k) != list(range(len(phi))):
        k += 1
    return k


def inv(phi):
    out = [0] * len(phi)
    for s, t in enumerate(phi):
        out[t] = s
    return out


def comp_fn(w, g):  # (w o g)(s) = w(g s)
    return tuple(w[g[s]] for s in range(len(g)))


def shell(n):
    return tuple(F(1) for _ in range(n))


def evolve(w, phi):  # ClassicalBranchDomain.evolve: s -> w (phi s)
    return comp_fn(w, phi)


def branch(w, vis, i):  # ClassicalBranchDomain.branch i
    return tuple(w[s] if vis[s] == i else F(0) for s in range(len(w)))


def iti_rel_K(phi, vis, K, s, t):
    return all(vis[perm_pow(phi, k)[s]] == vis[perm_pow(phi, k)[t]] for k in range(K))


def invariant_K(f, phi, vis, K):
    n = len(phi)
    return all(f[s] == f[t] for s in range(n) for t in range(n) if iti_rel_K(phi, vis, K, s, t))


def pair(f, mu):
    return sum(a * b for a, b in zip(f, mu))


def pushforward(mu, g):  # (g_* mu)(t) = sum_{s: g s = t} mu(s)
    out = [F(0)] * len(mu)
    for s, m in enumerate(mu):
        out[g[s]] += m
    return tuple(out)


# A1: S = Z/5, phi = +1, vis = [s == 0]; separating cycle.
n = 5
phi = [(s + 1) % n for s in range(n)]
vis = [s == 0 for s in range(n)]
r = branch(shell(n), vis, True)  # the visible readout (indicator of vis = true)
L = order(phi)
check("A1.order(phi)=5", L == 5)
w = r
for _ in range(L - 1):
    w = evolve(w, phi)  # constructor term evolve^(L-1) (branch true shell)
check("A1.evolve^(ord-1)(branch shell) == r o phi^-1", w == comp_fn(r, inv(phi)))
check("A1.r o phi^-1 is [s==1]", comp_fn(r, inv(phi)) == tuple(F(int(s == 1)) for s in range(n)))
# every element of <phi> transports r into the constructor closure
ok = True
for m in range(L):
    g = perm_pow(phi, m)
    target = comp_fn(r, inv(g))  # r o g^-1
    ww = r
    for _ in range((L - m) % L):
        ww = evolve(ww, phi)
    ok &= (ww == target)
check("A1.forall g in <phi>: r o g^-1 = evolve^((L-m) mod L)(r)", ok)
# Schroedinger/Heisenberg convention control: <r, g_* mu> = <r o g, mu>; direction matters
mu = (F(1, 2), F(1, 3), F(1, 12), F(1, 24), F(1, 24))
check("A1.mu is a law", sum(mu) == 1)
check("A1.<r, phi_* mu> == <r o phi, mu>", pair(r, pushforward(mu, phi)) == pair(comp_fn(r, phi), mu))
check("A1.direction control: <r o phi, mu> != <r o phi^-1, mu>",
      pair(comp_fn(r, phi), mu) != pair(comp_fn(r, inv(phi)), mu))

# A2: horizon caveat. r o phi^-1 = r o phi^4 needs BranchDomainK horizon 5 = ord(phi).
rinv = comp_fn(r, inv(phi))
inv_by_K = {K: invariant_K(rinv, phi, vis, K) for K in range(1, 7)}
print("   A2 r o phi^-1 ~_K-invariant by K:", inv_by_K)
check("A2.not ~_2-invariant (so not in span BranchDomainK 2, by branchDomainK_invariant)", not inv_by_K[2])
# Run 1 asserted the minimal horizon equals orderOf phi = 5; measured 4. Corrected: the span
# horizon is the least K with ~_K-invariance (OQ:270), which can be below the horizon of the
# direct constructor term evolve^(ord-1)(branch shell), which is ord = 5 in BranchDomainK.
Kmin = min(K for K, v in inv_by_K.items() if v)
print("   A2 least K with r o phi^-1 in span BranchDomainK K:", Kmin, "; constructor-term horizon:", L)
check("A2.span horizon (4) < constructor-term horizon (5) and > 2", Kmin == 4 and L == 5)
# the class of s=1 at K=4 is a singleton (itinerary 0000), so r o phi^-1 is its class indicator
check("A2.[s==1] is the ~_4 class indicator of 1",
      tuple(F(int(iti_rel_K(phi, vis, 4, t, 1))) for t in range(n)) == rinv)
check("A2.forward r o phi (horizon 2) is ~_2-invariant", invariant_K(comp_fn(r, phi), phi, vis, 2))

# A3: restriction control. Label-symmetric 4-cycle (probe F25/F30 shape): vis = s mod 2.
n4 = 4
phi4 = [(s + 1) % n4 for s in range(n4)]
vis4 = [s % 2 for s in range(n4)]
r4 = branch(shell(n4), vis4, 0)
ord4 = order(phi4)
check("A3.orderOf phi4 = 4", ord4 == 4)
okp = all(invariant_K(comp_fn(r4, inv(perm_pow(phi4, m))), phi4, vis4, ord4) for m in range(ord4))
check("A3.every r4 o g^-1, g in <phi4>, is ~inf-invariant", okp)
swap01 = [1, 0, 2, 3]
r4s = comp_fn(r4, swap01)
check("A3.r4 o swap(0,1) = [0,1,1,0]", r4s == (F(0), F(1), F(1), F(0)))
check("A3.r4 o swap(0,1) NOT ~inf-invariant (outside span ClassicalBranchDomain, OQ:316)",
      not invariant_K(r4s, phi4, vis4, ord4))
check("A3.swap(0,1) not in <phi4>", swap01 not in [perm_pow(phi4, m) for m in range(ord4)])

# A4: passive transport stays diagonal: monomial conjugation of a diagonal projector is diagonal
def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def T(a):
    return [list(x) for x in zip(*a)]


for name, P in (("id", [[1, 0], [0, 1]]), ("X", [[0, 1], [1, 0]])):
    for d in ((1, 1), (1, -1)):
        M = [[F(P[i][j] * d[j]) for j in range(2)] for i in range(2)]  # perm * diag(+-1), real monomial
        proj = [[F(1), F(0)], [F(0), F(0)]]
        C = matmul(matmul(M, proj), T(M))
        check(f"A4.monomial {name}{d} conj of |0><0| is diagonal", C[0][1] == 0 and C[1][0] == 0)

# ---------------------------------------------------------------- (b) drive
def apply(Mx, v):
    return tuple(sum(Mx[i][j] * v[j] for j in range(3)) for i in range(3))


def ball_effect(u):  # v -> 1/2 + u.v/2  (KF:1026)
    return lambda v: F(1, 2) + sum(a * b for a, b in zip(u, v)) / 2


ROT90 = [[F(0), F(-1), F(0)], [F(1), F(0), F(0)], [F(0), F(0), F(1)]]  # rot3(pi/2): cos=0, sin=1
ROTm90 = T(ROT90)  # rot3(-pi/2)
CYC = [[F(0), F(0), F(1)], [F(1), F(0), F(0)], [F(0), F(1), F(0)]]  # cyc3 v = (v2, v0, v1)
CYCinv = T(CYC)  # cyc3.symm v = (v1, v2, v0)
check("B0.cyc3 orthogonal", matmul(CYC, CYCinv) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
check("B0.rot3(pi/2) orthogonal", matmul(ROT90, ROTm90) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
e0, e1, e2 = (F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))
m2 = (F(0), F(0), F(-1))
grid = [tuple(F(x, 2) for x in t) for t in product(range(-2, 3), repeat=3)]
ball_pts = [v for v in grid if sum(x * x for x in v) <= 1]


def same_on(f, g):
    return all(f(v) == g(v) for v in ball_pts)


# seed on the flow axis e2: flow fixes it, J moves it
r_ = ball_effect(e2)
check("B1.r o rot3(pi/2)^-1 == r (flow fixes the e2 seed)", same_on(lambda v: r_(apply(ROTm90, v)), r_))
check("B1.r o J^-1 == ballEffect(e0)", same_on(lambda v: r_(apply(CYCinv, v)), ball_effect(e0)))
check("B1.r o J^-2 == ballEffect(e1)",
      same_on(lambda v: r_(apply(CYCinv, apply(CYCinv, v))), ball_effect(e1)))
# seed e0 (moved by the NOT): flow moves it
s_ = ball_effect(e0)
check("B1.ballEffect(e0) o rot3(pi/2)^-1 == ballEffect(e1)",
      same_on(lambda v: s_(apply(ROTm90, v)), ball_effect(e1)))

# B2: countermodel. avail0 = {ballEffect e2, ballEffect(-e2)}: a PD pair at the poles.
a, b = ball_effect(e2), ball_effect(m2)
check("B2.pair are effects on grid ball points", all(0 <= a(v) <= 1 and 0 <= b(v) <= 1 for v in ball_pts))
check("B2.pair sums to 1", all(a(v) + b(v) == 1 for v in ball_pts))
check("B2.pair certain at poles", a(e2) == 1 and b(m2) == 1)
x = e0  # isBoundaryState_ball3 ![1,0,0] (KF:1080)
check("B2.(r o J^-1)(1,0,0) = 1", r_(apply(CYCinv, x)) == 1)
check("B2.members of avail0 give 1/2 at (1,0,0) -> r o J^-1 not in avail0",
      a(x) == F(1, 2) and b(x) == F(1, 2))

# B3: generator-on-seed is strictly weaker than orbit. avail2 = {r o g^-1 : g in flow U {J}} = {be(e2), be(e0)}
# (flow fixes e2). The word J.J gives be(e1), which differs from both at e1.
check("B3.be(e1)(e1)=1 while be(e2)(e1)=be(e0)(e1)=1/2",
      ball_effect(e1)(e1) == 1 and ball_effect(e2)(e1) == F(1, 2) and ball_effect(e0)(e1) == F(1, 2))
check("B3.J has order 3 (J^-1 = J^2 is a monoid word)",
      matmul(CYC, matmul(CYC, CYC)) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

print(f"{'OK' if fails == 0 else 'FAILED'} -- {count} checks, {fails} failures")
sys.exit(1 if fails else 0)
