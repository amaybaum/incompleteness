"""P1 (generic exact check; not an OI mechanism). #1059 re-assessment, ASSESS-1059.md §3.

Claims checked, on generic finite objects only:
 (a) For every permutation matrix on n <= 4 points, |U|^p = |U|^2 entrywise for p in a set of
     rational exponents, so a fixed-basis permutation table is the same for every p > 0
     (the Main:556 / BORN-SRC-1 C2 observation, re-checked).
 (b) Column lemma: a unit vector u (sum |u_j|^2 = 1) has sum |u_j|^p = 1 for some p != 2 iff
     exactly one |u_j| = 1.  Checked exactly on a rational grid of the simplex of |u|^2-profiles
     (n = 3, step 1/6) at p = 1 and p = 4 (BORN-SRC-1 L2 in fixed-basis form).
 (c) An exact non-monomial unitary (Cayley transform of a rational skew-Hermitian matrix) has
     columns normalised at p = 2 and not at p = 4 (control that (b) is not vacuous).
Every check is exact (sympy rationals / algebraic numbers). Exit status 0 iff all pass.
"""
import itertools, sys
import sympy as sp

fails = []
def need(cond, msg):
    if not cond:
        fails.append(msg)

# (a) permutation tables are p-independent
ps = [sp.Rational(1, 2), 1, 2, 3, 7]
for n in range(1, 5):
    for perm in itertools.permutations(range(n)):
        U = sp.zeros(n, n)
        for i, j in enumerate(perm):
            U[j, i] = 1
        for p in ps:
            Tp = U.applyfunc(lambda x: sp.Abs(x) ** p)
            need(Tp == U.applyfunc(lambda x: sp.Abs(x) ** 2), f"(a) perm {perm} p={p}")
print("(a) permutation |U|^p tables identical for p in", ps, "n<=4:", not fails)

# (b) column lemma on a rational grid of profiles x_j = |u_j|^2, n = 3, step 1/6
N = 6
grid = [(sp.Rational(a, N), sp.Rational(b, N), sp.Rational(N - a - b, N))
        for a in range(N + 1) for b in range(N + 1 - a)]
nb = 0
for x in grid:
    vertex = sum(1 for xi in x if xi == 1) == 1
    s4 = sum(xi ** 2 for xi in x)                       # sum |u|^4
    s1 = sp.nsimplify(sum(sp.sqrt(xi) for xi in x))      # sum |u|^1
    need((s4 == 1) == vertex, f"(b) p=4 at {x}")
    need(sp.simplify(s1 - 1) == 0 if vertex else sp.simplify(s1 - 1) != 0, f"(b) p=1 at {x}")
    nb += 1
print(f"(b) column lemma at p=1,4 on {nb} grid profiles (n=3, step 1/{N}):", not fails)

# (c) exact non-monomial unitary via Cayley transform U = (I - A)(I + A)^{-1}, A skew-Hermitian
I = sp.I
A = sp.Matrix([[I, 1 + 2 * I, -1], [-1 + 2 * I, 0, 2], [1, -2, -3 * I]])
need(A.H == -A, "(c) A skew-Hermitian")
Id = sp.eye(3)
U = sp.simplify((Id - A) * (Id + A).inv())
need(sp.simplify(U.H * U - Id) == sp.zeros(3, 3), "(c) U unitary")
mods2 = U.applyfunc(lambda z: sp.nsimplify(sp.simplify(z * sp.conjugate(z))))
nonmono = any(0 < mods2[j, i] < 1 for i in range(3) for j in range(3))
need(nonmono, "(c) U non-monomial")
for i in range(3):
    need(sum(mods2[j, i] for j in range(3)) == 1, f"(c) column {i} p=2")
p4 = [sum(mods2[j, i] ** 2 for j in range(3)) for i in range(3)]
need(all(v != 1 for v in p4), "(c) every column fails p=4")
print("(c) Cayley unitary: |U|^2 column sums = 1; |U|^4 column sums =", p4, ":", not fails)

if fails:
    print("FAIL:", fails)
    sys.exit(1)
print("ALL P1 CHECKS PASS")
