"""r2 EXACT CHECKS OF PAPER CLAIMS ON GENERIC MATHEMATICAL OBJECTS (BRIDGE-UNIT1 r2).

Run under the owner's permission recorded in #1211 c.6739843458 ("Allow generic checks
(as #1210)"). Labelled checks of algebraic statements used in the r2 text; they are
controls on that algebra, not evidence for any new physical result. No OI mechanism is
simulated. This script imports no earlier script (neither the r1 writer's nor the
reviewer's probes) and uses exact sympy arithmetic only.

C1  Cubic rotation group O (24 elements) on the six signed axis vectors of R^3:
    (a) the real commutant has dimension 3, so the three isotypic components are
        multiplicity-free and of real type (End = R for each);
    (b) a generic O-equivariant symmetric Sigma has eigenvalue multiplicities (1,2,3);
    (c) its stabilizer Lie algebra has dimension 4 in so(6) and 14 in u(6).
C2  One oscillator mode f_a = [[0,1],[-1,a]] (det 1), tensored with I_6:
    (a) a = 2cos(w) with 0 < w < pi: J = (f - cos w)/sin w satisfies J^2 = -1, [J,f] = 0,
        det J = 1 (symplectic in 2D);
    (b) the commutant of f_a (x) I_6 in sp(12,R) has dimension 36 and every element
        commutes with J (x) I_6, so it is u(6);
    (d) a stationary product covariance C = K (x) Sigma on that mode has stabilizer
        dimension 14 inside the u(6) commutant and 4 inside diagonal o(6);
    (c) a = 2 (unipotent f): no real 2x2 J with J^2 = -1 commutes with f_2;
        countercontrol: the same solve finds real J for a = 1.
C3  Ring of N sites, eps = diag((-1)^x), symbolic mu:
    D' = (T - T^-1)/2 + mu (T^3 - T^-3)/2 anticommutes with eps identically in mu;
    on the even scalar sublattice the second-order operator -4 D'^2 has a
    same-sublattice (scalar hop 2) coupling equal to -2 mu, nonzero iff mu != 0.
    Control: adding an eps-even term directly to the first-order operator breaks
    the anticommutator.
"""
import itertools
import sympy as sp

ok = True
def check(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

# ---------------- C1 ----------------
axes = []
for j in range(3):
    for s in (1, -1):
        v = [0, 0, 0]; v[j] = s; axes.append(tuple(v))
group = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        R = sp.zeros(3, 3)
        for i in range(3):
            R[perm[i], i] = signs[i]
        if R.det() == 1:
            P = sp.zeros(6, 6)
            for a, v in enumerate(axes):
                w = tuple(R * sp.Matrix(v))
                P[axes.index(w), a] = 1
            group.append(P)
check("C1 |O| = 24", len(group) == 24)
gens = group  # use all elements
X = sp.Matrix(6, 6, sp.symbols('x0:36'))
eqs = []
for P in gens:
    eqs += list(P * X - X * P)
A, _ = sp.linear_eq_to_matrix(eqs, list(X))
comm_basis = [sp.Matrix(6, 6, list(v)) for v in A.nullspace()]
check("C1(a) real commutant dimension = 3 (multiplicity-free, real type)", len(comm_basis) == 3)
# generic symmetric equivariant Sigma: symmetric part of a generic commutant element
coeffs = [sp.Rational(2), sp.Rational(-5, 3), sp.Rational(7, 11)]
Sig = sum((c * B for c, B in zip(coeffs, comm_basis)), sp.zeros(6, 6))
Sig = (Sig + Sig.T) / 2
mult = sorted(Sig.eigenvals().values())
check("C1(b) multiplicities (1,2,3): got %s" % mult, mult == [1, 2, 3])
Y = sp.Matrix(6, 6, sp.symbols('y0:36'))
eqs = list(Y + Y.T) + list(Y * Sig - Sig * Y)
A, _ = sp.linear_eq_to_matrix(eqs, list(Y))
dim_so = 36 - A.rank()
Aa = sp.Matrix(6, 6, sp.symbols('p0:36')); Bb = sp.Matrix(6, 6, sp.symbols('q0:36'))
eqs = list(Aa + Aa.T) + list(Bb - Bb.T) + list(Aa * Sig - Sig * Aa) + list(Bb * Sig - Sig * Bb)
A, _ = sp.linear_eq_to_matrix(eqs, list(Aa) + list(Bb))
dim_u = 72 - A.rank()
check("C1(c) stabilizer dim so(6) = 4: got %d" % dim_so, dim_so == 4)
check("C1(c) stabilizer dim u(6) = 14: got %d" % dim_u, dim_u == 14)

# ---------------- C2 ----------------
w = sp.pi / 3            # a = 2cos(pi/3) = 1, a generic non-null value
a = 2 * sp.cos(w)
f = sp.Matrix([[0, 1], [-1, a]])
J2 = (f - sp.cos(w) * sp.eye(2)) / sp.sin(w)
check("C2(a) J^2 = -1", sp.simplify(J2 * J2 + sp.eye(2)) == sp.zeros(2, 2))
check("C2(a) [J,f] = 0", sp.simplify(J2 * f - f * J2) == sp.zeros(2, 2))
check("C2(a) det J = 1", sp.simplify(J2.det() - 1) == 0)
n = 6
F = sp.Matrix(sp.kronecker_product(f, sp.eye(n)))
J = sp.Matrix(sp.kronecker_product(J2, sp.eye(n)))
Om = sp.Matrix(sp.kronecker_product(sp.Matrix([[0, 1], [-1, 0]]), sp.eye(n)))
check("C2 F symplectic", sp.simplify(F.T * Om * F - Om) == sp.zeros(2 * n, 2 * n))
Z = sp.Matrix(2 * n, 2 * n, sp.symbols('z0:%d' % (4 * n * n)))
eqs = list(Z * F - F * Z) + list(Z.T * Om + Om * Z)
A, _ = sp.linear_eq_to_matrix([sp.nsimplify(sp.simplify(e)) for e in eqs], list(Z))
basis = [sp.Matrix(2 * n, 2 * n, list(v)) for v in A.nullspace()]
check("C2(b) dim commutant in sp(12) = 36: got %d" % len(basis), len(basis) == 36)
check("C2(b) every commutant element commutes with J (x) I6",
      all(sp.simplify(B * J - J * B) == sp.zeros(2 * n, 2 * n) for B in basis))
# C2(d): stationary product covariance C = K (x) Sig on this mode; stabilizer {X : X C + C X^T = 0}
k11, k12, k22 = sp.symbols('k11 k12 k22')
Kc = sp.Matrix([[k11, k12], [k12, k22]])
solK = sp.solve(list(f * Kc * f.T - Kc), [k12, k22], dict=True)[0]
Kc = Kc.subs(solK).subs(k11, 1)
check("C2(d) K positive definite", Kc[0, 0] > 0 and sp.simplify(Kc.det()) > 0)
C = sp.Matrix(sp.kronecker_product(Kc, Sig))
check("C2(d) C stationary under F", sp.simplify(F * C * F.T - C) == sp.zeros(2 * n, 2 * n))
cs = sp.symbols('c0:%d' % len(basis))
Xc = sum((c * B for c, B in zip(cs, basis)), sp.zeros(2 * n, 2 * n))
A, _ = sp.linear_eq_to_matrix([sp.simplify(e) for e in (Xc * C + C * Xc.T)], list(cs))
st = len(basis) - A.rank()
check("C2(d) stabilizer of C inside the u(6) commutant = 14: got %d" % st, st == 14)
Xo = sp.Matrix(n, n, sp.symbols('o0:%d' % (n * n)))
Xb = sp.Matrix(sp.kronecker_product(sp.eye(2), Xo))
A, _ = sp.linear_eq_to_matrix(list(Xo + Xo.T) + [sp.simplify(e) for e in (Xb * C + C * Xb.T)], list(Xo))
st_o = n * n - A.rank()
check("C2(d) same, configuration-space o(6) acting diagonally = 4: got %d" % st_o, st_o == 4)
f2 = sp.Matrix([[0, 1], [-1, 2]])
p, q, r, t = sp.symbols('p q r t', real=True)
K = sp.Matrix([[p, q], [r, t]])
sols = sp.solve(list(K * f2 - f2 * K) + list(K * K + sp.eye(2)), [p, q, r, t], dict=True)
real_sols = [s for s in sols if all(v.is_real for v in s.values())]
check("C2(c) no real J with J^2=-1 commuting with f_2: %d real solutions" % len(real_sols),
      len(real_sols) == 0)
f1 = sp.Matrix([[0, 1], [-1, 1]])  # countercontrol: the same solve finds real J at a non-null mode
sols1 = sp.solve(list(K * f1 - f1 * K) + list(K * K + sp.eye(2)), [p, q, r, t], dict=True)
check("C2(c) countercontrol: real J found for f_1: %d real solutions" % len([s for s in sols1 if all(v.is_real for v in s.values())]),
      len([s for s in sols1 if all(v.is_real for v in s.values())]) > 0)

# ---------------- C3 ----------------
N = 12
mu = sp.symbols('mu')
def T(k):
    M = sp.zeros(N, N)
    for x in range(N):
        M[(x + k) % N, x] = 1
    return M
eps = sp.diag(*[(-1) ** x for x in range(N)])
Dp = (T(1) - T(-1)) / 2 + mu * (T(3) - T(-3)) / 2
check("C3 {D', eps} = 0 identically in mu", sp.expand(Dp * eps + eps * Dp) == sp.zeros(N, N))
Box = sp.expand(-4 * Dp * Dp)
ev = list(range(0, N, 2))
Bs = Box.extract(ev, ev)       # scalar operator on the even sublattice; scalar hop 1 = fermion hop 2
same_hop = sp.expand(Bs[0, 2])  # scalar hop 2 (same scalar sublattice)
check("C3 same-sublattice coupling on scalar lattice = -2 mu: got %s" % same_hop,
      sp.simplify(same_hop + 2 * mu) == 0)
h = (T(2) + T(-2)) / 10
D0 = (T(1) - T(-1)) / 2
check("C3 control: {D0 + h, eps} != 0", (D0 + h) * eps + eps * (D0 + h) != sp.zeros(N, N))

print("ALL PASS" if ok else "SOME CHECK FAILED")
