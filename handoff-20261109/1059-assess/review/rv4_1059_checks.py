"""REVIEW-1059-r4: the reviewer's own exact generic checks (WIP / UNVERIFIED).

Label X: exact computation on generic matrices and vectors only. No OI mechanism is computed.
Imports no earlier script (none of p1_*, p2_*, r2_*, r3_*, r4_*, rv_*, rv2_*, rv3_*).
Run: python3 -I rv4_1059_checks.py

G1  Column lemma. For columns normalised in l^q (q = 1, 2, 3) with >= 2 entries of modulus in (0,1),
    sum |u|^p = 1 holds at p = q and at no other sampled p (exact), and every term is strictly
    decreasing in p (derivative u^p log u < 0), so q is the only root.
G2  Dilation lemma, on a class wider than single-entry dilations. Every V (stacked Kraus family,
    m blocks of size n x n) whose columns are taken from all vectors over the scaled value set
    S5 = {0, 5, 5i, 3, 4, -4} (i.e. {0, 1, i, 3/5, 4/5, -4/5} times 5) of squared norm 25, with
    pairwise inner product 0 (Gram = 1, exact Gaussian integers), for (n, m) in {(2,2), (2,3), (3,2)}.
    Claim checked: some block non-monomial => some column has >= 2 nonzero entries; and all columns
    single-entry => every block monomial. Non-vacuity: complete families with a non-monomial block
    occur (count > 0), and single-entry V with Gram != 1 and a non-monomial block occur.
G3  Scope of the "every amplitude vector" (Aaronson) form outside square maps. The Kraus family
    K1 = 2^(-1/p) [[1,0],[1,0]], K2 = [[0,1],[0,0]] has a non-monomial block and, for every p > 0,
    outcome-table sum |.|^p = |x1|^p + |x2|^p on every input (symbolic p, moduli and phases); it is
    complete only at p = 2. So without completeness (the quadratic Kraus normalisation), H-RF_p on
    every amplitude vector does not force p = 2 for a non-square (dilation) operation.
G4  Reachable-state readout. (a) The nonnegative, non-monomial, singular map
    N_q = [[0,0,0],[a,1,0],[a,0,1]], a = 2^(-1/q): the reachable set from the basis states closes on
    {e1, e2, e3, (0,a,a)}, and H-RF_p holds on all of it iff p = q, for q = 2 and q = 3. No sign and no
    cancellation occur, so p = 2 is forced without interference, any q can be forced the same way,
    and the map forcing p = 2 is not unitary. (b) The signed, non-monomial map
    S = [[0,1,-1],[1/2,0,0],[-1/2,0,0]]: its reachable set from the basis states closes on
    {+-e1, +-(0,1/2,-1/2), e2, e3} and H-RF_p holds on it iff p = 1. (c) Instance recomputed:
    M_p = 2^(-1/p)[[1,-1],[1,1]], sum |M_p^2 e1|^p = 2^(p-2). (d) Control of the method: a signed
    permutation's reachable set satisfies H-RF_p for every p.
"""
import itertools

import sympy as sp

res = {}
p = sp.symbols('p', positive=True)


# ---------------------------------------------------------------- G1
def g1_column(col, q):
    col = [sp.nsimplify(c) for c in col if c != 0]
    ok = len(col) >= 2 and all(0 < abs(c) < 1 for c in col)
    ok &= sp.simplify(sum(abs(c) ** q for c in col) - 1) == 0
    for other in (sp.Rational(1, 2), 1, sp.Rational(3, 2), 2, 3, 4):
        if other != q:
            ok &= sp.simplify(sum(abs(c) ** other for c in col) - 1) != 0
    ok &= all(sp.log(abs(c)) < 0 for c in col)         # each term u^p strictly decreasing
    return ok


s2 = sp.sqrt(2)
res['G1'] = (g1_column([sp.Rational(3, 5), sp.Rational(4, 5)], 2)
             and g1_column([1 / s2, -1 / s2], 2)
             and g1_column([sp.Rational(1, 3), sp.Rational(2, 3)], 1)
             and g1_column([2 ** sp.Rational(-1, 3), 2 ** sp.Rational(-1, 3)], 3))


# ---------------------------------------------------------------- G2 (Gaussian integers as pairs)
S5 = [(0, 0), (5, 0), (0, 5), (3, 0), (4, 0), (-4, 0)]


def ip(u, v):  # <u, v> = sum conj(u) v
    re = im = 0
    for (a, b), (c, d) in zip(u, v):
        re += a * c + b * d
        im += a * d - b * c
    return (re, im)


def nnz(v):
    return sum(1 for x in v if x != (0, 0))


def monomial(K):
    n = len(K)
    return any(all(K[i][j] == (0, 0) for j in range(n) for i in range(n) if i != s[j])
               for s in itertools.permutations(range(n)))


g2 = True
nonmono_complete = 0
single_complete = 0
for n, m in ((2, 2), (2, 3), (3, 2)):
    cols = [c for c in itertools.product(S5, repeat=m * n) if ip(c, c) == (25, 0)]
    for V in itertools.permutations(cols, n):
        if any(ip(V[a], V[b]) != (0, 0) for a in range(n) for b in range(a + 1, n)):
            continue
        blocks = [[[V[j][r * n + i] for j in range(n)] for i in range(n)] for r in range(m)]
        all_mono = all(monomial(B) for B in blocks)
        multi = any(nnz(c) >= 2 for c in V)
        if not all_mono:
            nonmono_complete += 1
            g2 &= multi                                     # the lemma
        if not multi:
            single_complete += 1
            g2 &= all_mono                                  # contrapositive
# countercontrol: single-entry, Gram != 1, non-monomial block (two columns at one position)
cc = [[(5, 0), (5, 0)], [(0, 0), (0, 0)], [(0, 0), (0, 0)], [(0, 0), (0, 0)]]   # V rows, n = 2, m = 2
Vc = [[cc[r][j] for r in range(4)] for j in range(2)]
cc_ok = ip(Vc[0], Vc[1]) != (0, 0) and not monomial([cc[0], cc[1]]) and all(nnz(c) == 1 for c in Vc)
res['G2'] = g2 and nonmono_complete > 0 and single_complete > 0 and cc_ok

# ---------------------------------------------------------------- G3
x1, x2 = sp.symbols('x1 x2', positive=True)
t1, t2 = sp.symbols('t1 t2', real=True)
c = 2 ** (-1 / p)
K1 = sp.Matrix([[c, 0], [c, 0]])
K2 = sp.Matrix([[0, 1], [0, 0]])
x = sp.Matrix([x1 * sp.exp(sp.I * t1), x2 * sp.exp(sp.I * t2)])
table = list(K1 * x) + list(K2 * x)
tot = sum(sp.Abs(e) ** p for e in table)
tot = sp.simplify(sp.powsimp(sp.expand_power_base(tot, force=True), force=True))
g3 = sp.simplify(tot - (x1 ** p + x2 ** p)) == 0
g3 &= not monomial([[(1, 0), (0, 0)], [(1, 0), (0, 0)]])           # K1's pattern
comp = sp.simplify(K1.H * K1 + K2.H * K2 - sp.eye(2))
g3 &= sp.solve(sp.Eq(comp[0, 0], 0), p) == [2] and comp[1, 1] == 0 and comp[0, 1] == 0
res['G3'] = g3


# ---------------------------------------------------------------- G4
def reach(M, cap=50):
    n = M.shape[0]
    seen, frontier = [], [sp.eye(n).col(j) for j in range(n)]
    while frontier and len(seen) < cap:
        v = frontier.pop()
        if any(v == w for w in seen):
            continue
        seen.append(v)
        frontier.append(sp.simplify(M * v))
    return seen if not frontier else None


def admissible_p(states):
    """Exponents p > 0 with sum |v|^p = 1 on every state: 'all' or the solution list."""
    eqs = [sp.powsimp(sum(sp.Abs(e) ** p for e in v if e != 0), force=True) - 1 for v in states]
    eqs = [sp.simplify(e) for e in eqs if sp.simplify(e) != 0]
    if not eqs:
        return 'all'
    sols = set(sp.solve(eqs[0], p))
    return sorted(s for s in sols if all(sp.simplify(e.subs(p, s)) == 0 for e in eqs))


g4 = True
for q in (2, 3):
    a = 2 ** sp.Rational(-1, q)
    N = sp.Matrix([[0, 0, 0], [a, 1, 0], [a, 0, 1]])
    R = reach(N)
    g4 &= R is not None and len(R) == 4
    g4 &= admissible_p(R) == [q]
    g4 &= all(e >= 0 for e in N) and not monomial([[(0 if e == 0 else 1, 0) for e in N.row(i)] for i in range(3)])
    g4 &= N.det() == 0                                              # not unitary
S = sp.Matrix([[0, 1, -1], [sp.Rational(1, 2), 0, 0], [-sp.Rational(1, 2), 0, 0]])
RS = reach(S)
g4 &= RS is not None and len(RS) == 6 and admissible_p(RS) == [1]
g4 &= any(e < 0 for v in RS for e in v)                             # signed reachable states
Mp = 2 ** (-1 / p) * sp.Matrix([[1, -1], [1, 1]])
w = sp.simplify(Mp * Mp * sp.Matrix([1, 0]))
sw = sp.simplify(sp.powsimp(sp.expand_power_base(sum(sp.Abs(e) ** p for e in w), force=True), force=True))
g4 &= sp.simplify(sw - 2 ** (p - 2)) == 0
P = sp.Matrix([[0, -1, 0], [0, 0, 1], [1, 0, 0]])                  # signed permutation: control
RP = reach(P)
g4 &= RP is not None and admissible_p(RP) == 'all'
res['G4'] = g4

for k, v in res.items():
    print(k, 'PASS' if v else 'FAIL')
print('G2 complete families with a non-monomial block:', nonmono_complete,
      '| with single-entry columns:', single_complete)
print('ALL PASS' if all(res.values()) else 'SOME FAIL')
raise SystemExit(0 if all(res.values()) else 1)
