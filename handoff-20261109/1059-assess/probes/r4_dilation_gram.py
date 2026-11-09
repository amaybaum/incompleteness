"""ASSESS-1059 r4: exact generic checks replacing r3's E2(a), plus the N1 scope checks (WIP / UNVERIFIED).

Label: X (exact computation on generic matrices and vectors). No OI mechanism is computed.
Imports no earlier script (none of p1_*, p2_*, r2_*, r3_*, rv_*, rv2_*, rv3_*).
Run: python3 -I r4_dilation_gram.py

r3's E2(a) compared two encodings of one predicate and was vacuous. D1 below computes what E2(a)
did not: the Gram matrix of every candidate dilation, and the monomial shape of every Kraus block.

Arithmetic: Gaussian rationals as pairs of fractions.Fraction (exact). Monomial shape is the kernel's
IsMonomial (SubstratumInterface.lean:75): K = permMatrix(sigma) * diagonal(d), zeros in d allowed,
decided by searching sigma in S_n for K[i][j] = 0 whenever i != sigma(j).

D0  Self-tests of the two deciders. Monomial: [[1,1],[0,0]] no (columns single-entry, rows not);
    the Hadamard pattern no; P_sigma diag(d) with a zero in d yes; [[0,0],[0,0]] yes. Gram:
    the instrument {|0><+|, |1><->|} stacked has Gram = 1; [[1],[1]] has Gram = 2.
D1  Dilation lemma, computed. n <= 3 inputs, m <= 3 Kraus blocks of size n x n. For every assignment
    of one nonzero entry to each of the n dilation columns (position (block, row)), and every choice
    of entry values from W = {1, i, (3+4i)/5, 1/2}, build V (mn x n), COMPUTE Gram = V^dag V, and
    decide IsMonomial of each block. Claim: Gram = 1 implies every block monomial.
    Countercontrol (a): some single-entry patterns with Gram != 1 have a non-monomial block, so the
    Gram condition (completeness) carries the claim; dropping it makes the claim fail.
    Countercontrol (b): with a value of modulus != 1 in W, single-entry columns at distinct positions
    give Gram != 1, so the Gram test is not decided by positions alone.
D2  Hypothesis "single-entry" is load-bearing: exact complete families with non-monomial blocks exist
    ({|0><+|,|1><->|}, {|0><+|,|0><->|}, and {R/sqrt2, 1/sqrt2} with R the 3-4-5 rotation), and in
    each some dilation column has >= 2 nonzero entries (the lemma's contrapositive, instances).
H1  Reachable-state readout without interference. DS = [[1/3,2/3],[2/3,1/3]] (non-monomial, entries
    >= 0) acting linearly on real amplitudes: DS^k e_1 = ((1+(-1/3)^k)/2, (1-(-1/3)^k)/2) for
    symbolic k (checked by induction, exact), entries >= 0 and summing to 1, so sum |amp|^1 = 1 on
    every state reachable from e_1 (and from e_2 by symmetry); sum |amp|^2 != 1 on DS e_1. So linear
    dynamics with the readout required only on reachable states can fix p = 1, not 2.
H2  Reachable-state readout with interference (instance). M_p = 2^(-1/p) [[1,-1],[1,1]]: both
    columns have sum |.|^p = 1 for every p > 0; M_p^2 e_1 = 2^(1-2/p) e_2, whose sum |.|^p = 2^(p-2),
    equal to 1 only at p = 2. At p = 2, M_2 is orthogonal.
H3  p = 2 on every vector gives unitarity (polarization). For a generic complex 2 x 2 matrix A
    (eight real symbols), the four norm defects ||Av||^2 - ||v||^2 at v = e1, e2, e1+e2, e1+i e2
    determine every entry of A^dag A - 1 linearly (explicit inverse formulas checked symbolically),
    so norm preservation on every vector gives A^dag A = 1.
"""
import itertools
from fractions import Fraction as Fr

import sympy as sp


# ---------------------------------------------------------------- Gaussian rationals
def g(a, b=0):
    return (Fr(a), Fr(b))


ZERO, ONE = g(0), g(1)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def conj(x):
    return (x[0], -x[1])


def gram(V):
    """V: list of rows (each a list of Gaussian rationals); returns V^dag V as an n x n list."""
    n = len(V[0])
    G = [[ZERO] * n for _ in range(n)]
    for row in V:
        for j in range(n):
            if row[j] == ZERO:
                continue
            cj = conj(row[j])
            for jj in range(n):
                if row[jj] != ZERO:
                    G[j][jj] = add(G[j][jj], mul(cj, row[jj]))
    return G


def is_identity(G):
    n = len(G)
    return all(G[i][j] == (ONE if i == j else ZERO) for i in range(n) for j in range(n))


def is_monomial(K):
    """Kernel shape: exists sigma with K[i][j] = 0 for i != sigma(j) (d may vanish)."""
    n = len(K)
    for s in itertools.permutations(range(n)):
        if all(K[i][j] == ZERO for j in range(n) for i in range(n) if i != s[j]):
            return True
    return False


def blocks_of(V, m, n):
    return [V[r * n:(r + 1) * n] for r in range(m)]


res = {}

# ---------------------------------------------------------------- D0
d0 = True
d0 &= not is_monomial([[ONE, ONE], [ZERO, ZERO]])
d0 &= not is_monomial([[ONE, ONE], [ONE, g(-1)]])
d0 &= is_monomial([[ZERO, g(0, 1)], [ZERO, ZERO]])            # P_swap diag(0, i)
d0 &= is_monomial([[ZERO, ZERO], [ZERO, ZERO]])
d0 &= is_monomial([[ZERO, g(2)], [g(3), ZERO]])
# Gram self-tests with rational entries: 3-4-5 column pair is orthonormal; [[1],[1]] has Gram 2
V345 = [[(Fr(3, 5), Fr(0)), (Fr(-4, 5), Fr(0))],
        [(Fr(4, 5), Fr(0)), (Fr(3, 5), Fr(0))]]
d0 &= is_identity(gram(V345))
d0 &= gram([[ONE], [ONE]]) == [[g(2)]]
d0 &= not is_identity(gram([[ONE, ONE], [ZERO, ZERO]]))
res['D0'] = d0

# ---------------------------------------------------------------- D1
W = [g(1), g(0, 1), (Fr(3, 5), Fr(4, 5)), g(Fr(1, 2))]
claim = True
counter_a = 0          # Gram != 1 and some block non-monomial
counter_b = 0          # distinct positions but Gram != 1 (a non-unit value)
n_gram_one = 0
n_cases = 0
for n in (1, 2, 3):
    for m in (1, 2, 3):
        positions = [(r, i) for r in range(m) for i in range(n)]
        for assign in itertools.product(positions, repeat=n):
            distinct = len(set(assign)) == n
            for vals in itertools.product(W, repeat=n):
                n_cases += 1
                V = [[ZERO] * n for _ in range(m * n)]
                for j, ((r, i), v) in enumerate(zip(assign, vals)):
                    V[r * n + i][j] = v
                G = gram(V)
                mono = all(is_monomial(B) for B in blocks_of(V, m, n))
                if is_identity(G):
                    n_gram_one += 1
                    claim &= mono
                else:
                    if not mono:
                        counter_a += 1
                    if distinct:
                        counter_b += 1
res['D1'] = claim and counter_a > 0 and counter_b > 0 and n_gram_one > 0

# ---------------------------------------------------------------- D2 (sympy, exact surds)
s2 = sp.sqrt(2)
ket0, ket1 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
plus, minus = sp.Matrix([[1, 1]]) / s2, sp.Matrix([[1, -1]]) / s2


def sp_monomial(K):
    n = K.shape[0]
    return any(all(K[i, j] == 0 for j in range(n) for i in range(n) if i != s[j])
               for s in itertools.permutations(range(n)))


fams = [[ket0 * plus, ket1 * minus], [ket0 * plus, ket0 * minus]]
# {R/sqrt2, 1/sqrt2}: complete since R^T R = 1; the block R/sqrt2 is non-monomial
R = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]])
fams.append([R / s2, sp.eye(2) / s2])
d2 = True
for Ks in fams:
    n = Ks[0].shape[0]
    d2 &= sp.simplify(sum((K.H * K for K in Ks), sp.zeros(n, n)) - sp.eye(n)) == sp.zeros(n, n)
    d2 &= any(not sp_monomial(K) for K in Ks)
    V = sp.Matrix.vstack(*Ks)
    d2 &= any(sum(1 for x in V.col(j) if x != 0) >= 2 for j in range(n))
res['D2'] = d2

# ---------------------------------------------------------------- H1
k = sp.symbols('k', integer=True, nonnegative=True)
DS = sp.Matrix([[sp.Rational(1, 3), sp.Rational(2, 3)], [sp.Rational(2, 3), sp.Rational(1, 3)]])
r = sp.Rational(-1, 3) ** k
vk = sp.Matrix([(1 + r) / 2, (1 - r) / 2])
h1 = vk.subs(k, 0) == sp.Matrix([1, 0])
h1 &= sp.simplify(DS * vk - vk.subs(k, k + 1)) == sp.zeros(2, 1)       # induction step
h1 &= sp.simplify(sum(vk) - 1) == 0                                     # sum of entries = 1
# entries >= 0: (1 +- r)/2 >= 0 iff |r| <= 1, and |r| = 3^(-k) <= 1 for k >= 0
h1 &= sp.simplify(sp.Abs(r) - sp.Rational(1, 3) ** k) == 0
h1 &= (sp.Integer(3) ** k - 1).is_nonnegative is True       # 3^k >= 1, so 3^(-k) <= 1
h1 &= any(sum(1 for x in DS.row(i) if x != 0) > 1 for i in range(2))   # non-monomial
v1 = DS * sp.Matrix([1, 0])
h1 &= sum(x ** 2 for x in v1) != 1                                      # fails at p = 2
res['H1'] = h1

# ---------------------------------------------------------------- H2
p = sp.symbols('p', positive=True)
Mp = 2 ** (-1 / p) * sp.Matrix([[1, -1], [1, 1]])
h2 = all(sp.simplify(sum(sp.Abs(x) ** p for x in Mp.col(j)) - 1) == 0 for j in range(2))
w = sp.simplify(Mp * Mp * sp.Matrix([1, 0]))
h2 &= sp.simplify(w - sp.Matrix([0, 2 ** (1 - 2 / p)])) == sp.zeros(2, 1)
s_w = sp.powsimp(sp.expand_power_base(sum(sp.Abs(x) ** p for x in w), force=True), force=True)
h2 &= sp.simplify(s_w - 2 ** (p - 2)) == 0
h2 &= sp.solve(sp.Eq(2 ** (p - 2), 1), p) == [2]
M2 = Mp.subs(p, 2)
h2 &= sp.simplify(M2.T * M2 - sp.eye(2)) == sp.zeros(2, 2)
res['H2'] = h2

# ---------------------------------------------------------------- H3
a = sp.symbols('a0:8', real=True)
A = sp.Matrix([[a[0] + sp.I * a[1], a[2] + sp.I * a[3]], [a[4] + sp.I * a[5], a[6] + sp.I * a[7]]])
G = sp.expand(A.H * A)


def defect(v):
    return sp.expand((v.H * G * v)[0, 0] - (v.H * v)[0, 0])


e1v, e2v = sp.Matrix([1, 0]), sp.Matrix([0, 1])
D = [defect(e1v), defect(e2v), defect(e1v + e2v), defect(e1v + sp.I * e2v)]
# G - 1 recovered from the four defects (polarization), exactly:
G11 = D[0]
G22 = D[1]
reG12 = (D[2] - D[0] - D[1]) / 2
imG12 = (D[0] + D[1] - D[3]) / 2   # v = e1 + i e2: v^dag G v = G11 + G22 - 2 Im G12
h3 = sp.simplify(G[0, 0] - 1 - G11) == 0
h3 &= sp.simplify(G[1, 1] - 1 - G22) == 0
h3 &= sp.simplify(sp.re(G[0, 1]) - reG12) == 0
h3 &= sp.simplify(sp.im(G[0, 1]) - imG12) == 0
res['H3'] = h3

for key, v in res.items():
    print(key, 'PASS' if v else 'FAIL')
print('D1 cases:', n_cases, '| Gram = 1:', n_gram_one,
      '| countercontrol (a) non-monomial with Gram != 1:', counter_a,
      '| countercontrol (b) distinct positions, Gram != 1:', counter_b)
print('ALL PASS' if all(res.values()) else 'SOME FAIL')
raise SystemExit(0 if all(res.values()) else 1)
