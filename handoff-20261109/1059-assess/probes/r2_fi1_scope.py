"""ASSESS-1059 r2: exact generic checks (WIP / UNVERIFIED).

Generic mathematical objects only (small matrices, columns, a real function).
No OI mechanism is computed. Imports no earlier probe. Run: python3 -I r2_fi1_scope.py

K1  A non-monomial operator can have only monomial columns (K = [[1,1],[0,0]]):
    column readout |K e_j|^p sums to 1 for every p.  (FI-1's predicate is not R3-C's antecedent.)
K2  Weighted monomial Kraus families {2^{-k/2} P_s}: complete (sum K^dag K = I, exact) and
    sum_K sum_i |K e_j|_i^p = 2^{k(1-p/2)}, = 1 iff p = 2.  Control: phased permutation fits every p.
K3  Invertible matrices: every column with exactly one nonzero entry => monomial (exhaustive
    over support patterns, n <= 4).  So for unitaries "non-monomial" = "some column has >= 2 nonzeros".
K4  (review B2(i)) column (1/3,2/3,2/3): unrenormalised |.|^p sums to 1 only at p = 2;
    renormalised readout is a law for every p and the laws differ.
K5  (review B2(ii), B3) column (2^{-1/2}, 2^{-1/2}): sum |a|^p = 2^{1-p/2}, = 1 iff p = 2.
K6  (review nit 4) g(u) = u^2 (1 + sin^2(pi log2 u^2)) equals u^2 at u = 2^{-k/2}, k <= 40 (exact),
    and g(cos pi/8) + g(sin pi/8) != 1 (mpmath interval arithmetic, rigorous enclosure).
"""
import itertools
import sympy as sp
import mpmath

ok = {}
p = sp.symbols('p', positive=True)

# K1
K = sp.Matrix([[1, 1], [0, 0]])
nonmono = any(sum(1 for x in K.row(i) if x != 0) > 1 for i in range(2))
cols_mono = all(sum(1 for x in K.col(j) if x != 0) == 1 for j in range(2))
fits = all(sp.simplify(sum(sp.Abs(x) ** q for x in K.col(j)) - 1) == 0
           for j in range(2) for q in [sp.Rational(1, 2), 1, 2, 3, 7])
ok['K1'] = nonmono and cols_mono and fits

# K2
def perm_matrix(s):
    n = len(s)
    M = sp.zeros(n, n)
    for j, i in enumerate(s):
        M[i, j] = 1
    return M

k2 = True
for k in (1, 2, 3):
    perms = list(itertools.permutations(range(3)))[: 2 ** k] if 2 ** k <= 6 else None
    if perms is None:  # k = 3: use 8 permutations of 4 points
        perms = list(itertools.permutations(range(4)))[:8]
    n = len(perms[0])
    fam = [sp.sqrt(sp.Rational(1, 2 ** k)) * perm_matrix(s) for s in perms]
    comp = sum((A.H * A for A in fam), sp.zeros(n, n))
    k2 &= comp == sp.eye(n)
    tot = sum(sp.Abs(A[i, 0]) ** p for A in fam for i in range(n))
    sols = sp.solve(sp.Eq(sp.simplify(tot), 1), p)
    k2 &= sols == [2]
# control: phased permutation (unimodular monomial) fits every p
P = perm_matrix((1, 2, 0)) * sp.diag(sp.I, -1, 1)
k2 &= all(sp.simplify(sum(sp.Abs(P[i, j]) ** q for i in range(3)) - 1) == 0
          for j in range(3) for q in [sp.Rational(1, 2), 1, 3, 7])
ok['K2'] = k2

# K3: column map c -> row; nonsingular iff the map is a bijection; then monomial
k3 = True
for n in (2, 3, 4):
    for rows in itertools.product(range(n), repeat=n):
        # generic nonzero entries: distinct symbols
        M = sp.zeros(n, n)
        for j, i in enumerate(rows):
            M[i, j] = sp.Symbol(f'a{j}')
        nonsing = sp.expand(M.det()) != 0
        mono = len(set(rows)) == n
        k3 &= (nonsing == mono)
ok['K3'] = k3

# K4
col = [sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3)]
# h(p) = sum c^p with every c in (0,1): a positive sum of strictly decreasing exponentials,
# hence strictly decreasing in p; h(2) = 1 exactly, so p = 2 is the unique root of h(p) = 1.
s = sum(c ** p for c in col)
k4 = all(0 < c < 1 for c in col) and s.subs(p, 2) == 1
k4 &= s.subs(p, 1) != 1 and s.subs(p, 3) != 1  # non-vacuity at the sampled exponents
laws = {}
for q in (1, 2, 3):
    w = [c ** q for c in col]
    laws[q] = tuple(sp.nsimplify(x / sum(w)) for x in w)
k4 &= all(sum(v) == 1 for v in laws.values()) and len(set(laws.values())) == 3
k4 &= laws[1] == (sp.Rational(1, 5), sp.Rational(2, 5), sp.Rational(2, 5))
ok['K4'] = k4

# K5
a = 1 / sp.sqrt(2)
s5 = sp.simplify(2 * a ** p)
ok['K5'] = sp.simplify(s5 - 2 ** (1 - p / 2)) == 0 and sp.solve(sp.Eq(s5, 1), p) == [2]

# K6
u = sp.symbols('u', positive=True)
g = u ** 2 * (1 + sp.sin(sp.pi * sp.log(u ** 2, 2)) ** 2)
k6 = all(sp.simplify(g.subs(u, 2 ** sp.Rational(-k, 2)) - 2 ** (-k)) == 0 for k in range(0, 41))
mpmath.iv.dps = 40
c, sn = mpmath.iv.cos(mpmath.iv.pi / 8), mpmath.iv.sin(mpmath.iv.pi / 8)
def giv(x):
    return x ** 2 * (1 + mpmath.iv.sin(mpmath.iv.pi * mpmath.iv.log(x ** 2) / mpmath.iv.log(2)) ** 2)
tot = giv(c) + giv(sn)
k6 &= not (1 in tot) and tot.a > 1
ok['K6'] = k6

for key, v in ok.items():
    print(key, 'PASS' if v else 'FAIL')
print('K4 renormalised laws:', {q: [str(x) for x in v] for q, v in laws.items()})
print('K6 g(cos pi/8)+g(sin pi/8) enclosure:', tot)
print('ALL PASS' if all(ok.values()) else 'SOME FAIL')
raise SystemExit(0 if all(ok.values()) else 1)
