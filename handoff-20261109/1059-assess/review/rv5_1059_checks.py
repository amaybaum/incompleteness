"""REVIEW-1059-r5: reviewer's exact checks on ASSESS-1059 r5's B1 passages (WIP / UNVERIFIED).

Label X: exact computation (fractions.Fraction and sympy) on generic matrices and vectors only.
No OI mechanism, carrier, lift or substratum object is computed. Imports no earlier script
(no p1_*, p2_*, r2_*..r5_*, rv_*..rv4_*). Run: python3 -I rv5_1059_checks.py [MUTANT]
An optional MUTANT argument (m1..m7) applies one single-line mutation; each must turn its
check to FAIL (mutation test).

Readout: unrenormalised H-RF_p. For a linear map V (a square operation, or the stacked dilation
of a Kraus family, whose output entries are the outcome table), H-RF_p "on every vector" means
sum_i |(Vx)_i|^p = sum_j |x_j|^p for all x.

T1  Every-vector form, exhaustive over a finite alphabet (necessary conditions on e_i and e_i +- e_j,
    homogeneity used). Alphabet {0, +-1/2, +-1}. Square 2x2 and 3x3: every map passing at p = 1 is
    monomial. Non-square 4x2: every map passing at p = 1 has dilation columns with disjoint supports
    (Lamperti/Clarkson equality case), and some passing map has a non-monomial 2x2 block; at p = 2
    every passing map has V^T V = 1, and some passing map has columns with overlapping supports.
    Countercontrol: with the e_i - e_j test dropped (nonnegative probes only, as on a reachable set),
    overlapping-support maps pass at p = 1.
T2  B1(a) dilation case, overlapping supports. Kraus family {c H, c H}, H = [[1,1],[1,-1]], free c > 0,
    symbolic p. H-RF_p on e1 and on e1 + e2 has the unique solution p = 2, c = 1/2; completeness
    sum K^dag K = 1 then follows (it is not posited), and H-RF_2 holds on every complex vector
    (symbolic moduli and phases). This is a non-square operation (4 x 2 dilation) for which the 2
    does not come "only from completeness".
T3  B1(a) the text's examples are the disjoint-support case. K1 = 2^(-1/p)[[1,0],[1,0]], K2 = [[0,1],[0,0]]:
    dilation columns disjointly supported, table sum |x1|^p + |x2|^p (symbolic), complete iff p = 2.
    {w^(1/q) P_s} over 2^k permutations of 3 points (w = 2^-k): dilation columns disjoint,
    2^k nonzero entries each.
T4  B1(b) reachable-state route. N_q (symbolic q): reachable set {e1, e2, e3, (0,a,a)}, admissible
    p = q only; N_2 fails H-RF_1 (so "a non-monomial nonnegative map satisfies H-RF_1" holds only
    as an instance). S: admissible p = 1. M_p = 2^(-1/p)[[1,-1],[1,1]] (r4 H2's map): its first
    reachable state is p-normalised at every p, and the cancelled state M_p^2 e1 forces p = 2.
    R = 2^(-1/2)[[1,-1],[1,1]]: its first reachable state, before any cancellation, already forces
    p = 2.
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

MUT = sys.argv[1] if len(sys.argv) > 1 else ''
res = {}
ALPH = [Fr(0), Fr(1, 2), Fr(-1, 2), Fr(1), Fr(-1)]
if MUT == 'm7':
    ALPH = [Fr(0), Fr(1, 2), Fr(1), Fr(-1)]


def psum(v, p):
    return sum(abs(e) ** p for e in v)


def apply(cols, x):
    m = len(cols[0])
    return [sum(cols[j][i] * x[j] for j in range(len(cols))) for i in range(m)]


def passes(cols, p, signed=True):
    n = len(cols)
    for i in range(n):
        if psum(cols[i], p) != 1:
            return False
    for i, j in itertools.combinations(range(n), 2):
        signs = (1, -1) if signed else (1,)
        if MUT == 'm1':
            signs = (1,)
        for s in signs:
            x = [Fr(0)] * n
            x[i], x[j] = Fr(1), Fr(s)
            if psum(apply(cols, x), p) != 2:
                return False
    return True


def monomial_square(cols):
    n = len(cols)
    return all(sum(1 for e in c if e != 0) == 1 for c in cols) and \
        len({next(i for i, e in enumerate(c) if e != 0) for c in cols}) == n


def supports(cols):
    return [frozenset(i for i, e in enumerate(c) if e != 0) for c in cols]


def disjoint(cols):
    if MUT == 'm6':
        return True
    s = supports(cols)
    return all(not (s[i] & s[j]) for i, j in itertools.combinations(range(len(s)), 2))


def gram_is_one(cols):
    n = len(cols)
    return all(sum(cols[a][i] * cols[b][i] for i in range(len(cols[a]))) == (1 if a == b else 0)
               for a in range(n) for b in range(n))


# ---------------------------------------------------------------- T1
t1 = True
for n in (2, 3):
    colset = list(itertools.product(ALPH, repeat=n))
    unit1 = [c for c in colset if psum(c, 1) == 1]          # necessary for p = 1
    cnt = 0
    for cols in itertools.product(unit1, repeat=n):
        if passes(list(cols), 1):
            cnt += 1
            t1 &= monomial_square(list(cols))
    t1 &= cnt > 0
cols4 = list(itertools.product(ALPH, repeat=4))
u1 = [c for c in cols4 if psum(c, 1) == 1]
u2 = [c for c in cols4 if psum(c, 2) == 1]
p1_pass = [cs for cs in itertools.product(u1, repeat=2) if passes(list(cs), 1)]
t1 &= len(p1_pass) > 0 and all(disjoint(list(cs)) for cs in p1_pass)
# some p=1 passer has a non-monomial 2x2 block (rows 0-1 or rows 2-3)
blk_nonmono = 0
for cs in p1_pass:
    for rows in ((0, 1), (2, 3)):
        blk = [[c[r] for r in rows] for c in cs]
        if any(e != 0 for c in blk for e in c) and not monomial_square(blk):
            blk_nonmono += 1
            break
t1 &= blk_nonmono > 0
p2_pass = [cs for cs in itertools.product(u2, repeat=2) if passes(list(cs), 2)]
t1 &= len(p2_pass) > 0 and all(gram_is_one(list(cs)) for cs in p2_pass)
overlap2 = sum(1 for cs in p2_pass if not disjoint(list(cs)))
t1 &= overlap2 > 0
# countercontrol: nonnegative probes only admit overlapping supports at p = 1
cc = [cs for cs in itertools.product(u1, repeat=2) if passes(list(cs), 1, signed=False)]
t1 &= any(not disjoint(list(cs)) for cs in cc)
res['T1'] = t1
T1_COUNTS = (len(p1_pass), blk_nonmono, len(p2_pass), overlap2,
             sum(1 for cs in cc if not disjoint(list(cs))))

# ---------------------------------------------------------------- T2
p, c = sp.symbols('p c', positive=True)
Hm = sp.Matrix([[1, 1], [1, -1]])
K = c * Hm
fam = [K, K] if MUT != 'm2' else [K, c * sp.Matrix([[1, 0], [0, 1]])]
V = sp.Matrix.vstack(*fam)
e1v, s12 = sp.Matrix([1, 0]), sp.Matrix([1, 1])
eqA = sp.Eq(sum(sp.Abs(e) ** p for e in V * e1v), 1)
eqB = sp.Eq(sum(sp.Abs(e) ** p for e in V * s12), 2)
# eqA: 4 c^p = 1 ; eqB: 2 (2c)^p = 2  =>  c^p = 2^-p  =>  c = 1/2, then 4 * 2^-p = 1  =>  p = 2
cp = sp.symbols('cp', positive=True)                      # cp = c^p
A_ = sp.simplify(sp.expand_power_base(eqA.lhs, force=True).subs(c ** p, cp))
B_ = sp.simplify(sp.expand_power_base(eqB.lhs, force=True).subs(c ** p, cp))
sol_cp = sp.solve(sp.Eq(A_, 1), cp)
t2 = len(sol_cp) == 1
if t2:
    rem = sp.simplify(B_.subs(cp, sol_cp[0]) - 2)          # must vanish => equation in p
    psol = sp.solve(sp.Eq(rem, 0), p)
    t2 &= psol == [2]
    csol = sp.solve(sp.Eq(c ** 2, sol_cp[0].subs(p, 2)), c)
    t2 &= csol == [sp.Rational(1, 2)]
    Kc = [F.subs(c, sp.Rational(1, 2)) for F in fam]
    comp = sp.simplify(sum((F.H * F for F in Kc), sp.zeros(2)) - sp.eye(2))
    t2 &= comp == sp.zeros(2)
    r1, r2 = sp.symbols('r1 r2', positive=True)
    a1, a2 = sp.symbols('a1 a2', real=True)
    xv = sp.Matrix([r1 * sp.exp(sp.I * a1), r2 * sp.exp(sp.I * a2)])
    tot = sum(sp.expand(e * sp.conjugate(e)) for F in Kc for e in F * xv)
    t2 &= sp.simplify(tot - r1 ** 2 - r2 ** 2) == 0
    t2 &= not (Kc[0][0, 1] == 0 or Kc[0][1, 0] == 0)       # K non-monomial
    Vc = sp.Matrix.vstack(*Kc)
    t2 &= Vc.rows == 4 and Vc.cols == 2 and \
        bool(supports([list(Vc.col(0)), list(Vc.col(1))])[0] & supports([list(Vc.col(0)), list(Vc.col(1))])[1])
res['T2'] = t2

# ---------------------------------------------------------------- T3
t3 = True
K1 = 2 ** (-1 / p) * sp.Matrix([[1, 0], [1, 0]])
K2 = sp.Matrix([[0, 1], [0, 0]]) if MUT != 'm3' else sp.Matrix([[0, 1], [0, 1]])
V = sp.Matrix.vstack(K1, K2)
t3 &= disjoint([list(V.col(0)), list(V.col(1))])
r1, r2 = sp.symbols('r1 r2', positive=True)
a1, a2 = sp.symbols('a1 a2', real=True)
xv = sp.Matrix([r1 * sp.exp(sp.I * a1), r2 * sp.exp(sp.I * a2)])
tot = sum(sp.Abs(e) ** p for e in V * xv)
t3 &= sp.simplify(sp.powsimp(sp.expand_power_base(tot, force=True), force=True) - r1 ** p - r2 ** p) == 0
G = sp.simplify(K1.H * K1 + K2.H * K2)
t3 &= G[0, 1] == 0 and G[1, 0] == 0 and G[1, 1] == 1 and sp.solve(sp.Eq(G[0, 0], 1), p) == [2]
perms = list(itertools.permutations(range(3)))
for k in (1, 2):
    Ps = []
    for s in perms[: 2 ** k]:
        M = sp.zeros(3, 3)
        for j, i in enumerate(s):
            M[i, j] = 1
        Ps.append(M)
    Vk = sp.Matrix.vstack(*Ps)
    colsk = [list(Vk.col(j)) for j in range(3)]
    t3 &= disjoint(colsk) and all(sum(1 for e in cl if e != 0) == 2 ** k for cl in colsk)
res['T3'] = t3

# ---------------------------------------------------------------- T4
t4 = True
q = sp.symbols('q', positive=True)


def reach(M, n):
    seen, todo = [], [sp.eye(n).col(j) for j in range(n)]
    while todo:
        v = sp.simplify(todo.pop())
        if any(sp.simplify(v - w) == sp.zeros(n, 1) for w in seen):
            continue
        seen.append(v)
        if len(seen) > 40:
            return None
        todo.append(M * v)
    return seen


a = 2 ** (-1 / q)
N = sp.Matrix([[0, 0, 0], [a, 1, 0], [a, 0, 1]])
if MUT == 'm4':
    N = sp.Matrix([[0, 0, 0], [0, 1, 0], [a, 0, 1]])
st = reach(N, 3)
t4 &= st is not None and len(st) == 4
conds = [sp.simplify(sp.powsimp(sp.expand_power_base(sum(sp.Abs(e) ** p for e in v), force=True), force=True) - 1)
         for v in st]
nontriv = [cnd for cnd in conds if cnd != 0]
t4 &= len(nontriv) == 1 and sp.solve(sp.Eq(nontriv[0], 0), p) == [q]
N2 = N.subs(q, 2)
st2 = reach(N2, 3)
t4 &= any(sum(abs(e) for e in v) != 1 for v in st2)        # N_2 fails H-RF_1
t4 &= all(e >= 0 for e in N2) and N2.det() == 0
S = sp.Matrix([[0, 1, -1], [sp.Rational(1, 2), 0, 0], [-sp.Rational(1, 2), 0, 0]])
stS = reach(S, 3)
condS = {sp.simplify(sum(sp.Abs(e) ** p for e in v) - 1) for v in stS} - {0}
t4 &= len(condS) == 1 and sp.solve(sp.Eq(condS.pop(), 0), p) == [1]
scale = 2 ** (-1 / p) if MUT != 'm5' else 2 ** sp.Rational(-1, 2)
Mp = scale * sp.Matrix([[1, -1], [1, 1]])
s1 = Mp * sp.Matrix([1, 0])
t4 &= sp.simplify(sp.powsimp(sp.expand_power_base(sum(sp.Abs(e) ** p for e in s1), force=True), force=True)) == 1
s2 = sp.simplify(Mp * s1)
t4 &= s2[0] == 0                                           # cancellation
f2 = sp.simplify(sp.powsimp(sp.expand_power_base(sum(sp.Abs(e) ** p for e in s2), force=True), force=True))
t4 &= sp.solve(sp.Eq(f2, 1), p) == [2]
R = 2 ** sp.Rational(-1, 2) * sp.Matrix([[1, -1], [1, 1]])
r_first = R * sp.Matrix([1, 0])
t4 &= all(e != 0 for e in r_first)                         # no cancellation in the first state
f1 = sum(sp.Abs(e) ** p for e in r_first)
t4 &= sp.solve(sp.Eq(sp.simplify(f1), 1), p) == [2]
res['T4'] = t4

for k_, v_ in res.items():
    print(k_, 'PASS' if v_ else 'FAIL')
print('T1 counts (p1 passers 4x2, with non-monomial block, p2 passers, p2 overlapping, '
      'p1 overlapping under nonneg probes):', T1_COUNTS)
print('ALL PASS' if all(res.values()) else 'SOME FAIL')
raise SystemExit(0 if all(res.values()) else 1)
