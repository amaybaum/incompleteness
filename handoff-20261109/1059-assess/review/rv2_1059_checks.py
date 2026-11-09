"""REVIEW-1059-r2: reviewer's exact generic checks (WIP / UNVERIFIED).

Generic matrices and columns only; no OI mechanism is computed. Imports no earlier
script (neither the writer's probes nor rv_1059_checks.py). Run: python3 -I rv2_1059_checks.py

Readout convention (unrenormalised H-RF_p): a column / Kraus family is p-admissible iff the
unrenormalised values |amp|^p summed over all outcomes equal 1.

D1  Exponent = normalisation exponent of the column.  For a column c with >= 2 nonzero entries,
    all |c_i| in (0,1), h(p) = sum |c_i|^p is strictly decreasing, so h(p) = 1 has exactly one
    root, and that root is the q with sum |c_i|^q = 1.  Checked exactly for an l^2 column
    (unitary column -> p = 2), an l^1 (stochastic) column -> p = 1, and an l^3 column -> p = 3.
    A doubly stochastic non-monomial matrix read under H-RF_p is admissible only at p = 1.
D2  Stinespring: the weighted monomial Kraus family {2^{-k/2} P_s} (k = 1, 2), stacked, is an
    isometry V (V^dag V = I exactly) whose columns are non-monomial unit vectors; the family's
    |.|^p table sum equals the column sum of V, 2^{k(1-p/2)}.  So the Kraus forcing at p = 2 is
    the column lemma applied to a dilation, not a separate mechanism.
D3  Non-monomial Kraus operator inside a complete instrument: K0 = |0><+|, K1 = |1><-| are
    non-monomial, sum K^dag K = I, and the outcome table under |.|^p sums to 2^{1-p/2} on each
    input: admissible only at p = 2.  The unscaled K = [[1,1],[0,0]] (non-monomial, monomial
    columns, fits every p) has K^dag K with eigenvalue 2, so it is not a Kraus operator of any
    instrument (not a contraction).
D4  Square-root insertion: amplitudes 2^{-k/2} defined from counting weights 2^{-k}: the H-RF_p
    law (2^{-k/2})^p equals the counting law 2^{-k} iff p = 2 (k = 1..6): normalisation at p = 2
    returns the inserted counting weights.
"""
import sympy as sp

p = sp.symbols('p', positive=True)
res = {}


def unique_root_at(col, q):
    """All |c| in (0,1) and >= 2 entries: h strictly decreasing; return True iff h(q) == 1."""
    a = [sp.nsimplify(abs(c)) for c in col]
    ok = len(a) >= 2 and all(0 < x < 1 for x in a)
    h_q = sp.nsimplify(sp.simplify(sum(x ** q for x in a)))
    # strict decrease: derivative sum x^p log x < 0 termwise for x in (0,1)
    return ok and h_q == 1


# D1
l2 = [sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3)]
l1 = [sp.Rational(1, 2), sp.Rational(1, 2)]
l3 = [2 ** sp.Rational(-1, 3), 2 ** sp.Rational(-1, 3)]
d1 = unique_root_at(l2, 2) and unique_root_at(l1, 1) and unique_root_at(l3, 3)
# non-vacuity: the same columns are not admissible at a different exponent
d1 &= sum(x ** 2 for x in l1) != 1 and sum(x ** 1 for x in l2) != 1 and sp.simplify(sum(x ** 2 for x in l3)) != 1
DS = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [sp.Rational(1, 2), sp.Rational(1, 2)]])
nonmono = any(sum(1 for x in DS.row(i) if x != 0) > 1 for i in range(2))
d1 &= nonmono and all(unique_root_at(list(DS.col(j)), 1) for j in range(2))
res['D1'] = d1


# D2
def P(perm):
    n = len(perm)
    M = sp.zeros(n, n)
    for j, i in enumerate(perm):
        M[i, j] = 1
    return M


d2 = True
fams = {1: [(0, 1, 2), (1, 0, 2)], 2: [(0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1)]}
for k, perms in fams.items():
    w = sp.sqrt(sp.Rational(1, 2 ** k))
    Ks = [w * P(s) for s in perms]
    V = sp.Matrix.vstack(*Ks)                     # Stinespring isometry
    d2 &= sp.simplify(V.H * V - sp.eye(3)) == sp.zeros(3, 3)
    for j in range(3):
        col = list(V.col(j))
        nz = [x for x in col if x != 0]
        d2 &= len(nz) == 2 ** k                   # non-monomial unit column
        tab = sum(sp.Abs(x) ** p for x in nz)
        d2 &= sp.simplify(tab - 2 ** (k * (1 - p / 2))) == 0
        d2 &= unique_root_at(nz, 2)
res['D2'] = d2

# D3
s2 = sp.sqrt(2)
K0 = sp.Matrix([[1, 1], [0, 0]]) / s2         # |0><+|
K1 = sp.Matrix([[0, 0], [1, -1]]) / s2        # |1><-|
d3 = sp.simplify(K0.H * K0 + K1.H * K1 - sp.eye(2)) == sp.zeros(2, 2)
d3 &= all(any(sum(1 for x in Kk.row(i) if x != 0) > 1 for i in range(2)) for Kk in (K0, K1))
for j in range(2):
    nz = [x for Kk in (K0, K1) for x in Kk.col(j) if x != 0]
    d3 &= sp.simplify(sum(sp.Abs(x) ** p for x in nz) - 2 ** (1 - p / 2)) == 0
    d3 &= unique_root_at(nz, 2)
Kraw = sp.Matrix([[1, 1], [0, 0]])
eig = (Kraw.H * Kraw).eigenvals()
d3 &= sp.Integer(2) in eig                     # not a contraction
d3 &= all(sum(sp.Abs(x) ** q for x in Kraw.col(j)) == 1 for j in range(2) for q in (sp.Rational(1, 2), 1, 2, 5))
res['D3'] = d3

# D4
d4 = True
for k in range(1, 7):
    amp = 2 ** sp.Rational(-k, 2)
    d4 &= sp.solve(sp.Eq(amp ** p, sp.Rational(1, 2 ** k)), p) == [2]
res['D4'] = d4

for key, v in res.items():
    print(key, 'PASS' if v else 'FAIL')
print('ALL PASS' if all(res.values()) else 'SOME FAIL')
raise SystemExit(0 if all(res.values()) else 1)
