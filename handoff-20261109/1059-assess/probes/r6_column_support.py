"""ASSESS-1059 r6: the non-square every-vector form splits by the supports of the dilation columns
(WIP / UNVERIFIED).

Label X: exact computation (fractions.Fraction and sympy) on generic matrices and vectors only.
No OI mechanism, carrier, lift or substratum object is computed. Imports no earlier script (no
p1_*, p2_*, r2_*..r5_*, rv*_*). Run: python3 -I r6_column_support.py [MUTANT]
An optional MUTANT argument (n1..n6) applies one single-line mutation; each must turn the check it
names to FAIL (mutation test).

Readout: unrenormalised H-RF_p. A Kraus family {K_r} (each K_r of size n x n) is read through its
stacked dilation V = (K_1; ...; K_m), whose output entries are the outcome table, so H-RF_p on
every vector means sum_i |(V x)_i|^p = sum_j |x_j|^p for every x. A square map is the case m = 1.

Q1  Pointwise equality case (the step of the paper proof). For p != 2,
    D_p(a, b) = |a+b|^p + |a-b|^p - 2(|a|^p + |b|^p) is <= 0 for p < 2 and >= 0 for p > 2, and is 0
    iff ab = 0. Exact over an alphabet: real entries at p = 1 and p = 3; Gaussian-rational entries at
    p = 4. Control: D_2 = 0 on every pair (parallelogram law).
Q2  Exhaustive 4 x 2 maps (two dilation columns of length 4), one exact alphabet per exponent chosen
    so that non-trivial p-unit columns exist: p = 1 {0, +-1/3, +-1/2, +-2/3, +-1};
    p = 3 {0, +-1/2, +-2/3, +-5/6, +-1} (27 + 64 + 125 = 216); p = 2 {0, +-1/2, +-3/5, +-4/5, +-1}.
    Probes e_1, e_2, e_1 + e_2, e_1 - e_2.
    (a) p in {1, 3}: every passer has disjoint column supports; every pair of disjointly supported
        p-unit columns passes; some passer has a non-monomial 2 x 2 block (non-square, non-monomial
        K, H-RF_p with p != 2).
    (b) p = 2: every passer has V^T V = 1 (completeness follows), and some passer has overlapping
        supports (so the overlapping case is non-empty, and there p = 2).
    (c) Countercontrol: with the probe e_1 - e_2 dropped (nonnegative probes only), overlapping
        passers appear at p = 1.
Q3  Disjoint case, symbolic: V with column 1 supported on rows {1, 2} (entries u1, u2) and column 2
    on rows {3, 4} (entries w1, w2), complex entries and input with symbolic moduli and phases,
    symbolic p: sum |V x|^p = |x1|^p (|u1|^p + |u2|^p) + |x2|^p (|w1|^p + |w2|^p), and
    V^dag V = diag(|u1|^2 + |u2|^2, |w1|^2 + |w2|^2). So H-RF_p on every vector holds iff every
    column is p-normalised, and completeness holds iff every column is 2-normalised.
Q4  Overlapping case, the counterexample {c H, c H}, H = [[1,1],[1,-1]], free scale c > 0, symbolic p:
    H-RF_p on e_1 and on e_1 + e_2 has the unique solution p = 2, c = 1/2 (by sympy's solve, and by
    hand: e_1 gives c^p = 1/4, then e_1 + e_2 gives 2^p / 4 = 1); the dilation columns overlap;
    completeness then holds (derived, not posited); H-RF_2 holds on every complex vector (symbolic
    moduli and phases); K is non-monomial.
Q5  The disjoint families named in the text: K1 = 2^(-1/p) [[1,0],[1,0]], K2 = [[0,1],[0,0]]
    (disjoint; table sum |x1|^p + |x2|^p for symbolic p; complete iff p = 2);
    {2^(-k/q) P_s} over 2^k permutations of 3 points, k = 1, 2, q = 2, 3, 4 (disjoint; each column
    has 2^k nonzero entries; columns q-normalised, hence H-RF_p on every vector iff p = q by Q3 and
    the column lemma; complete iff q = 2), which at q = 2 is {2^(-k/2) P_s}.

Mutants: n1 drops the probe e_1 - e_2 (Q2); n2 makes the disjointness decider constant (Q2);
n3 replaces the second Kraus operator by c 1 (Q4); n4 makes K2's support overlap K1's (Q5);
n5 flips the expected sign of D_1 (Q1); n6 removes the entries that give overlapping p = 2 passers
(Q2's non-vacuity guard).
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

MUT = sys.argv[1] if len(sys.argv) > 1 else ''
res = {}


# ------------------------------------------------------------------ helpers (exact rationals)
def psum(v, p):
    return sum(abs(e) ** p for e in v)


def image(cols, x):
    return [sum(cols[j][i] * x[j] for j in range(len(cols))) for i in range(len(cols[0]))]


def probes_ok(cols, p, signed=True):
    if any(psum(c, p) != 1 for c in cols):
        return False
    signs = (1, -1) if signed else (1,)
    if MUT == 'n1':
        signs = (1,)
    for s in signs:
        if psum(image(cols, [Fr(1), Fr(s)]), p) != 2:
            return False
    return True


def supp(c):
    return frozenset(i for i, e in enumerate(c) if e != 0)


def disjoint2(c0, c1):
    if MUT == 'n2':
        return True
    return not (supp(c0) & supp(c1))


def block_monomial(blk):
    nz = [[e != 0 for e in col] for col in blk]          # blk given by columns
    if not any(any(r) for r in nz):
        return True
    rows = [i for col in nz for i, b in enumerate(col) if b]
    return all(sum(col) <= 1 for col in nz) and len(rows) == len(set(rows))


# ------------------------------------------------------------------ Q1
def D_real(a, b, p):
    return abs(a + b) ** p + abs(a - b) ** p - 2 * (abs(a) ** p + abs(b) ** p)


def mod2(z):
    return z[0] * z[0] + z[1] * z[1]


def D_cplx4(a, b):
    s = (a[0] + b[0], a[1] + b[1])
    d = (a[0] - b[0], a[1] - b[1])
    return mod2(s) ** 2 + mod2(d) ** 2 - 2 * (mod2(a) ** 2 + mod2(b) ** 2)


q1 = True
RA = [Fr(0), Fr(1, 3), Fr(-1, 2), Fr(2, 3), Fr(1), Fr(-5, 4), Fr(7, 3)]
for a, b in itertools.product(RA, repeat=2):
    for p, sgn in ((1, -1), (3, 1)):
        d = D_real(a, b, p)
        if MUT == 'n5' and p == 1:
            sgn = 1
        q1 &= (d * sgn >= 0) and ((d == 0) == (a * b == 0))
    q1 &= D_real(a, b, 2) == 0
CA = [(Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(3, 5), Fr(4, 5)), (Fr(1, 2), Fr(-1, 2)),
      (Fr(-2), Fr(1, 3))]
for a, b in itertools.product(CA, repeat=2):
    d = D_cplx4(a, b)
    q1 &= d >= 0 and ((d == 0) == (mod2(a) * mod2(b) == 0))
res['Q1'] = q1

# ------------------------------------------------------------------ Q2
ALPH = {
    1: [Fr(0), Fr(1, 3), Fr(-1, 3), Fr(1, 2), Fr(-1, 2), Fr(2, 3), Fr(-2, 3), Fr(1), Fr(-1)],
    3: [Fr(0), Fr(1, 2), Fr(-1, 2), Fr(2, 3), Fr(-2, 3), Fr(5, 6), Fr(-5, 6), Fr(1), Fr(-1)],
    2: [Fr(0), Fr(1, 2), Fr(-1, 2), Fr(3, 5), Fr(-3, 5), Fr(4, 5), Fr(-4, 5), Fr(1), Fr(-1)],
}
if MUT == 'n6':
    ALPH[2] = [Fr(0), Fr(1), Fr(-1), Fr(3, 5), Fr(4, 5)]
q2 = True
counts = {}
for p in (1, 3, 2):
    units = [c for c in itertools.product(ALPH[p], repeat=4) if psum(c, p) == 1]
    passers, overl, nonmono, disj_fail = 0, 0, 0, 0
    gram_ok = True
    for c0, c1 in itertools.product(units, repeat=2):
        ok = probes_ok([c0, c1], p)
        dj = disjoint2(c0, c1)
        if dj and not ok:
            disj_fail += 1
        if ok:
            passers += 1
            if not dj:
                overl += 1
            if p == 2:
                gram_ok &= sum(x * y for x, y in zip(c0, c1)) == 0
            for rows in ((0, 1), (2, 3)):
                if not block_monomial([[c0[r] for r in rows], [c1[r] for r in rows]]):
                    nonmono += 1
                    break
    counts[p] = (len(units), passers, overl, nonmono)
    if p in (1, 3):
        q2 &= passers > 0 and overl == 0 and disj_fail == 0 and nonmono > 0
    else:
        q2 &= passers > 0 and gram_ok and overl > 0
units1 = [c for c in itertools.product(ALPH[1], repeat=4) if psum(c, 1) == 1]
cc = sum(1 for c0, c1 in itertools.product(units1, repeat=2)
         if probes_ok([c0, c1], 1, signed=False) and not disjoint2(c0, c1))
q2 &= cc > 0
res['Q2'] = q2

# ------------------------------------------------------------------ Q3
p = sp.symbols('p', positive=True)
r = sp.symbols('ru1 ru2 rw1 rw2 rx1 rx2', positive=True)
t = sp.symbols('tu1 tu2 tw1 tw2 tx1 tx2', real=True)
u1, u2, w1, w2, x1, x2 = [r[i] * sp.exp(sp.I * t[i]) for i in range(6)]
Vd = sp.Matrix([[u1, 0], [u2, 0], [0, w1], [0, w2]])
xv = sp.Matrix([x1, x2])


def abs_p_sum(vec, pp):
    return sp.powsimp(sp.expand_power_base(sum(sp.Abs(e) ** pp for e in vec), force=True), force=True)


lhs = abs_p_sum(Vd * xv, p)
rhs = r[4] ** p * (r[0] ** p + r[1] ** p) + r[5] ** p * (r[2] ** p + r[3] ** p)
q3 = sp.simplify(sp.expand(lhs - rhs)) == 0
G = sp.simplify(Vd.H * Vd)
q3 &= G[0, 1] == 0 and G[1, 0] == 0
q3 &= sp.simplify(G[0, 0] - r[0] ** 2 - r[1] ** 2) == 0 and sp.simplify(G[1, 1] - r[2] ** 2 - r[3] ** 2) == 0
res['Q3'] = q3

# ------------------------------------------------------------------ Q4
c = sp.symbols('c', positive=True)
Hm = sp.Matrix([[1, 1], [1, -1]])
fam = [c * Hm, c * Hm] if MUT != 'n3' else [c * Hm, c * sp.eye(2)]
V4 = sp.Matrix.vstack(*fam)
cols4 = [list(V4.col(0)), list(V4.col(1))]
q4 = bool(supp(cols4[0]) & supp(cols4[1]))                   # overlapping supports
eq1 = abs_p_sum(V4 * sp.Matrix([1, 0]), p) - 1               # 4 c^p - 1
eq2 = abs_p_sum(V4 * sp.Matrix([1, 1]), p) - 2               # 2 (2c)^p - 2
sol = sp.solve([eq1, eq2], [c, p], dict=True)
q4 &= sol == [{c: sp.Rational(1, 2), p: 2}]
# uniqueness by hand: eq1 gives c^p = 1/4; eq2 is then 2^p / 4 = 1, whose only real root is p = 2
cp = sp.symbols('cp', positive=True)
q4 &= sp.solve(sp.Eq(eq1.subs(c ** p, cp), 0), cp) == [sp.Rational(1, 4)]
q4 &= sp.solve(sp.Eq(sp.expand_power_base(eq2, force=True).subs(c ** p, sp.Rational(1, 4)), 0), p) == [2]
if q4:
    Kh = [F.subs(c, sp.Rational(1, 2)) for F in fam]
    q4 &= sp.simplify(sum((F.H * F for F in Kh), sp.zeros(2)) - sp.eye(2)) == sp.zeros(2)
    y = sp.Matrix([r[4] * sp.exp(sp.I * t[4]), r[5] * sp.exp(sp.I * t[5])])
    tot = sum(sp.expand(e * sp.conjugate(e)) for F in Kh for e in F * y)
    q4 &= sp.simplify(tot - r[4] ** 2 - r[5] ** 2) == 0
    q4 &= not block_monomial([list(Kh[0].col(0)), list(Kh[0].col(1))])
res['Q4'] = q4

# ------------------------------------------------------------------ Q5
q5 = True
K1 = 2 ** (-1 / p) * sp.Matrix([[1, 0], [1, 0]])
K2 = sp.Matrix([[0, 1], [0, 0]]) if MUT != 'n4' else sp.Matrix([[1, 1], [0, 0]])
V5 = sp.Matrix.vstack(K1, K2)
q5 &= not (supp(list(V5.col(0))) & supp(list(V5.col(1))))
q5 &= sp.simplify(sp.expand(abs_p_sum(V5 * xv, p) - r[4] ** p - r[5] ** p)) == 0
G5 = sp.simplify(K1.H * K1 + K2.H * K2)
q5 &= G5[0, 1] == 0 and G5[1, 1] == 1 and sp.solve(sp.Eq(G5[0, 0], 1), p) == [2]
q = sp.symbols('q', positive=True)
perms = list(itertools.permutations(range(3)))
for k in (1, 2):
    Ps = []
    for s in perms[: 2 ** k]:
        M = sp.zeros(3, 3)
        for j, i in enumerate(s):
            M[i, j] = 1
        Ps.append(M)
    for qq in (2, 3, 4):
        Vk = sp.Matrix.vstack(*[sp.Integer(2) ** sp.Rational(-k, qq) * M for M in Ps])
        cl = [list(Vk.col(j)) for j in range(3)]
        q5 &= all(not (supp(cl[i]) & supp(cl[j])) for i, j in itertools.combinations(range(3), 2))
        q5 &= all(len(supp(col)) == 2 ** k for col in cl)
        colsum = sp.simplify(sum(sp.Abs(e) ** p for e in cl[0]))
        q5 &= sp.solve(sp.Eq(colsum, 1), p) == [qq]           # columns q-normalised only
        comp = sp.simplify(Vk.T * Vk - sp.eye(3)) == sp.zeros(3)
        q5 &= comp == (qq == 2)
res['Q5'] = q5

for k_, v_ in res.items():
    print(k_, 'PASS' if v_ else 'FAIL')
print('Q2 counts p -> (unit columns, passers, overlapping passers, passers with non-monomial block):',
      {k_: counts[k_] for k_ in sorted(counts)})
print('Q2 countercontrol (overlapping passers at p = 1, nonnegative probes only):', cc)
print('ALL PASS' if all(res.values()) else 'SOME FAIL')
raise SystemExit(0 if all(res.values()) else 1)
