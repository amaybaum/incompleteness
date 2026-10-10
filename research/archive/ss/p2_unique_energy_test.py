"""Thread SS, probe P2 -- the candidate single-system selector UE (unique conserved sharp test).

Read-only research against base 68b6df0651f14b2c8ab082635b8d2051918617a2. Exact arithmetic only.

Candidate (NOT adopted; a named proposal):
  UE_full(d): every nontrivial continuous flow of body automorphisms of eball d conserves exactly one sharp
  binary test up to complementation, i.e. there is a unit u with sharpEff u o flow t = sharpEff u for all t,
  and any conserved sharp test is sharpEff u or its complement sharpEff (-u).
For a flow exp(tX), X in so(d), the conserved sharp tests are sharpEff u with u a unit vector of ker X^T = ker X.
So UE_full(d)  <=>  every nonzero X in so(d) has a one-dimensional kernel.

Sections
  K  kernel dimensions of the single-plane generator J01 for d = 2..9 (decides the exclusions)
  L  flow-level conservation of sharpEff e_j (j >= 2) under the plane rotation (symbolic t), and the
     separation of two conserved tests modulo complementation (d >= 4); d = 2: no conserved test
  M  d = 3: every nonzero hat(w) has rank 2 (sum of squared 2x2 minors = |w|^4) and kernel span(w)
  P  load-bearing check for "all flows" (FNR): d = 5 conjugation-closed family of a generic flow passes the
     uniqueness clause flow by flow, but a commuting product of two members is a single-plane flow
  O  orientation: improper symmetries of a flow send its conserved test to the complement (test level),
     while at Lie level g hat(v) g^T = det(g) hat(g v) (the sign that breaks full-group equivariance)
  S  stabilizer algebra of a pure state: abelian exactly for d <= 3 (FNR variant)

Run (from scratchpad/ss):  python3 -I p2_unique_energy_test.py
"""
import itertools
import sympy as sp
from sympy import Rational as R, Matrix, eye, zeros, cos, sin, sqrt, symbols

CHECKS = []


def check(name, cond):
    cond = bool(cond)
    CHECKS.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


def note(msg):
    print("NOTE " + msg)


def iszero(M):
    return all(sp.simplify(sp.expand_trig(sp.expand(z))) == 0 for z in M)


def e(d, i):
    v = zeros(d, 1)
    v[i] = 1
    return v


def Jgen(d, i, k):
    X = zeros(d, d)
    X[i, k], X[k, i] = -1, 1
    return X


def sharp(b, x):
    return R(1, 2) + (b.T * x)[0] / 2


t, s = symbols("t s", real=True)

# ---- K
print("=== K")
kd = {}
for d in range(2, 10):
    X = Jgen(d, 0, 1)
    kd[d] = len(X.nullspace())
    print("K d=%d dim ker J01 = %d" % (d, kd[d]))
check("K1 dim ker J01 = d - 2 for d = 2..9", all(kd[d] == d - 2 for d in kd))
check("K2 one-dimensional kernel for the single-plane generator exactly at d = 3 (d = 2..9)",
      [d for d in kd if kd[d] == 1] == [3])

# ---- L
print("=== L")
for d in [2, 3, 4, 5, 7]:
    xs = Matrix(symbols("x0:%d" % d, real=True))
    Rot = eye(d)
    Rot[0, 0], Rot[0, 1], Rot[1, 0], Rot[1, 1] = cos(t), -sin(t), sin(t), cos(t)
    if d == 2:
        # a conserved sharp test needs Rot(t)^T u = u for all t; at t = pi/2: (u1, -u0) = (u0, u1) -> u = 0
        u0, u1 = symbols("u0 u1", real=True)
        sol = sp.solve([u1 - u0, -u0 - u1], [u0, u1], dict=True)
        check("L1 d=2 no nonzero u with Rot(pi/2)^T u = u (solution %s): no conserved sharp test" % sol,
              sol == [{u0: 0, u1: 0}])
        continue
    for j in range(2, d):
        ej = e(d, j)
        ok = iszero(Matrix([sharp(ej, Rot * xs) - sharp(ej, xs)]))
        check("L2 d=%d sharpEff e%d conserved by the plane-(0,1) rotation flow (symbolic t)" % (d, j), ok)
    if d >= 4:
        e2, e3 = e(d, 2), e(d, 3)
        a, b = sharp(e2, e2), sharp(e3, e2)
        check("L3 d=%d conserved tests e2, e3 separated mod complement at x = e2: (%s, %s, %s)"
              % (d, a, b, 1 - a), a == 1 and b == R(1, 2) and b != a and b != 1 - a)

# ---- M
print("=== M")
w = Matrix(symbols("w0:3", real=True))
hat = Matrix([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])
check("M1 hat(w) w = 0", hat * w == zeros(3, 1))
minors = [hat.extract(list(r), list(c)).det() for r in itertools.combinations(range(3), 2)
          for c in itertools.combinations(range(3), 2)]
ssq = sp.factor(sp.expand(sum(m ** 2 for m in minors)))
check("M2 sum of squared 2x2 minors of hat(w) = (w.w)^2 (%s): rank 2 iff w != 0" % ssq,
      sp.expand(ssq - (w.T * w)[0] ** 2) == 0)
check("M3 every X in so(3) is hat(w) (3 free entries) -- parametrization",
      all(hat[i, j] == -hat[j, i] for i in range(3) for j in range(3)))
note("M: so for every nonzero X in so(3) the conserved sharp tests are exactly sharpEff(+-w/|w|): UE_full(3) "
     "at generator level; the flow-level statement (every nontrivial continuous flow of SO(3) is exp(t hat w)) "
     "is written, not computed")

# ---- P
print("=== P")
d = 5
X1 = Jgen(d, 0, 1) + sqrt(2) * Jgen(d, 2, 3)
g = sp.diag(1, 1, 1, -1, -1)
X2 = g * X1 * g.inv()
check("P1 g = diag(1,1,1,-1,-1) orthogonal with det +1", g.T * g == eye(d) and g.det() == 1)
check("P2 dim ker X1 = 1 and dim ker X2 = 1 (generic flows: one conserved test each)",
      len(X1.nullspace()) == 1 and len(X2.nullspace()) == 1)
check("P3 X2 = J01 - sqrt2 J23 and [X1, X2] = 0", X2 == Jgen(d, 0, 1) - sqrt(2) * Jgen(d, 2, 3)
      and X1 * X2 - X2 * X1 == zeros(d, d))
check("P4 the commuting product flow exp(t X1) exp(t X2) = exp(t (X1 + X2)) has generator 2 J01 with "
      "dim ker 3", X1 + X2 == 2 * Jgen(d, 0, 1) and len((X1 + X2).nullspace()) == 3)
note("P: the conjugation class of exp(t X1) under SO(5) generates a dense (normal) subgroup of the simple group "
     "SO(5), so its closure is transitive on S^4 (written). UE stated only for an available family closed under "
     "conjugation passes at d = 5; closure under commuting products, or all flows (FNR), is load-bearing.")

# ---- O
print("=== O")
xs = Matrix(symbols("x0:3", real=True))
Rz = Matrix([[cos(t), -sin(t), 0], [sin(t), cos(t), 0], [0, 0, 1]])
sig = sp.diag(1, 1, -1)
mI = -eye(3)
e2 = e(3, 2)
for name, gg in [("sigma = diag(1,1,-1)", sig), ("-I", mI)]:
    comm = iszero(gg * Rz - Rz * gg)
    # transport of the conserved test along gg: x |-> sharpEff e2 (gg^-1 x)
    tr = sp.expand(sharp(e2, gg.inv() * xs) - (1 - sharp(e2, xs)))
    check("O1 %s: det %s, commutes with the flow about e2, and carries sharpEff e2 to its complement"
          % (name, gg.det()), comm and gg.det() == -1 and tr == 0)
v = Matrix(symbols("v0:3", real=True))


def hatv(u):
    return Matrix([[0, -u[2], u[1]], [u[2], 0, -u[0]], [-u[1], u[0], 0]])


c1, s1 = R(3, 5), R(4, 5)
Rot_test = Matrix([[c1, -s1, 0], [s1, c1, 0], [0, 0, 1]])
for name, gg in [("proper rotation (3/5,4/5) about e2", Rot_test), ("sigma", sig), ("-I", mI),
                 ("reflY = diag(1,-1,1)", sp.diag(1, -1, 1))]:
    ok = sp.expand(gg * hatv(v) * gg.T - gg.det() * hatv(gg * v)) == zeros(3, 3)
    check("O2 %s: g hat(v) g^T = det(g) hat(g v)" % name, ok)

# ---- S
print("=== S")
for d in range(2, 8):
    gens = [Jgen(d, i, k) for i in range(1, d) for k in range(i + 1, d)]   # so(d-1) fixing e0
    ab = all(A * B - B * A == zeros(d, d) for A in gens for B in gens)
    print("S d=%d stabilizer algebra of e0: dim %d, abelian %s" % (d, len(gens), ab))
check("S1 stabilizer algebra so(d-1) of a pure state is nonzero and abelian exactly at d = 3 (d = 2..7)",
      [d for d in range(2, 8) if (lambda G: len(G) > 0 and all(A * B - B * A == zeros(d, d)
                                                                 for A in G for B in G))(
          [Jgen(d, i, k) for i in range(1, d) for k in range(i + 1, d)])] == [3])

fails = [n for n, c in CHECKS if not c]
print("SUMMARY %d checks, %d failed" % (len(CHECKS), len(fails)))
print("VERDICT " + ("RENDERED: at generator level UE_full holds at d = 3 and fails at d = 2 and d = 4..9; "
                    "FNR load-bearing (P); improper symmetries act on conserved tests by complementation (O)"
                    if not fails else "NOT RENDERED (a control failed)"))
