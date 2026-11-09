"""ASSESS-1059 r5: exact generic checks for REVIEW-1059-r4 B1 (WIP / UNVERIFIED).

Label X: exact sympy computation on generic matrices and vectors only. No OI mechanism, carrier,
lift or substratum object is computed. Imports no earlier script (none of p1_*, p2_*, r2_*, r3_*,
r4_*, rv_*, rv2_*, rv3_*, rv4_*). Run: python3 -I r5_scope_checks.py

Readout (unrenormalised H-RF_p): on one input, the values |amp|^p summed over every outcome and
output entry of the operation's outcome table must equal 1 for every p-normalised input.

S1  B1(a), non-square operations, H-RF_p on EVERY amplitude vector. (i) For each p > 0 the Kraus
    pair K1 = 2^(-1/p) [[1,0],[1,0]], K2 = [[0,1],[0,0]] (stacked: a 4 x 2 map) has outcome-table
    sum |x1|^p + |x2|^p identically (symbolic p, moduli and phases), so it satisfies H-RF_p on
    every vector at every p; K1 is non-monomial; sum K^dag K = 1 iff p = 2. (ii) The family
    {2^(-k/q) P_s} over 2^k permutations of 3 points (k = 1, 2; q = 2, 3, 4): outcome-table sum
    = 2^(k(1 - p/q)) sum |x_i|^p identically, so H-RF_p holds on every vector iff p = q; its
    stacked dilation columns have 2^k nonzero entries; complete iff q = 2.
S2  B1(a), square controls (instances consistent with the endomorphic form; not a proof of it).
    (i) Square non-monomial maps (2^(-1/2)[[1,1],[1,-1]], the 3-4-5 rotation (+) 1, K1 of S1
    alone) each change sum |.|^p on some basis vector at every sampled p != 2. (ii) A phased
    permutation preserves sum |x_i|^p on a symbolic vector for symbolic p. (iii) In S1(i) the
    square block K1 alone fails H-RF_p on e2 at every p: only the non-square stacked map preserves.
S3  B1(b), H-RF_p required only on the states reachable from the basis states under one linear
    map. The admissible exponents are computed two ways: (A) as the intersection, over reachable
    states, of each state's own normalisation exponent (a state with >= 2 nonzero entries of
    modulus in (0,1) has exactly one, by strict decrease of each term; a single entry of modulus 1
    admits every p); (B) by testing H-RF_p exactly at each sampled exponent. Cases:
    N_q = [[0,0,0],[a,1,0],[a,0,1]], a = 2^(-1/q) (nonnegative, non-monomial, singular), q = 2, 3:
    {q}; S = [[0,1,-1],[1/2,0,0],[-1/2,0,0]] (signed, non-monomial): {1}; the rotation
    2^(-1/2)[[1,-1],[1,1]] (cancellation): {2}; control: a signed permutation: every p.
"""
import itertools

import sympy as sp

p = sp.symbols('p', positive=True)
SAMPLE = (sp.Rational(1, 2), 1, sp.Rational(3, 2), 2, 3, 4)
res = {}


def is_monomial(M):
    """Square M is P_sigma diag(d) with zeros allowed: some permutation covers every nonzero."""
    n = M.shape[0]
    return any(all(M[i, j] == 0 for i in range(n) for j in range(n) if i != s[j])
               for s in itertools.permutations(range(n)))


def table_sum(Ks, x, q):
    tot = sum(sp.Abs(e) ** q for K in Ks for e in (K * x))
    return sp.simplify(sp.powsimp(sp.expand_power_base(sp.expand(tot), force=True), force=True))


def complete(Ks):
    return sp.simplify(sum((K.H * K for K in Ks), sp.zeros(Ks[0].shape[1])) - sp.eye(Ks[0].shape[1]))


# ---------------------------------------------------------------- S1
r1, r2, r3 = sp.symbols('r1 r2 r3', positive=True)
t1, t2, t3 = sp.symbols('t1 t2 t3', real=True)
x2v = sp.Matrix([r1 * sp.exp(sp.I * t1), r2 * sp.exp(sp.I * t2)])
x3v = sp.Matrix([r1 * sp.exp(sp.I * t1), r2 * sp.exp(sp.I * t2), r3 * sp.exp(sp.I * t3)])

s1 = True
K1 = 2 ** (-1 / p) * sp.Matrix([[1, 0], [1, 0]])
K2 = sp.Matrix([[0, 1], [0, 0]])
s1 &= sp.simplify(table_sum([K1, K2], x2v, p) - (r1 ** p + r2 ** p)) == 0
s1 &= not is_monomial(K1.subs(p, 3))
C = complete([K1, K2])
s1 &= C[0, 1] == 0 and C[1, 0] == 0 and C[1, 1] == 0
s1 &= sp.solve(sp.Eq(C[0, 0], 0), p) == [2]
s1_ii = True
perms3 = list(itertools.permutations(range(3)))


def P(perm):
    M = sp.zeros(3, 3)
    for j, i in enumerate(perm):
        M[i, j] = 1
    return M


for k in (1, 2):
    for q in (2, 3, 4):
        Ks = [2 ** sp.Rational(-k, q) * P(s) for s in perms3[: 2 ** k]]
        tot = table_sum(Ks, x3v, p)
        want = 2 ** (k * (1 - p / q)) * (r1 ** p + r2 ** p + r3 ** p)
        s1_ii &= sp.simplify(tot - want) == 0
        s1_ii &= sp.simplify(tot.subs(p, q) - (r1 ** q + r2 ** q + r3 ** q)) == 0
        s1_ii &= all(sp.simplify(tot.subs(p, o) - (r1 ** o + r2 ** o + r3 ** o)) != 0
                     for o in SAMPLE if o != q)
        V = sp.Matrix.vstack(*Ks)
        s1_ii &= all(sum(1 for e in V.col(j) if e != 0) == 2 ** k for j in range(3))
        s1_ii &= (complete(Ks) == sp.zeros(3, 3)) == (q == 2)
res['S1'] = s1 and s1_ii

# ---------------------------------------------------------------- S2
s2 = True
had = 2 ** sp.Rational(-1, 2) * sp.Matrix([[1, 1], [1, -1]])
rot = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5), 0], [sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])
for M in (had, rot):
    s2 &= not is_monomial(M) and sp.simplify(M.H * M - sp.eye(M.shape[0])) == sp.zeros(*M.shape)
    for o in SAMPLE:
        bad = any(sp.simplify(sum(sp.Abs(e) ** o for e in M.col(j)) - 1) != 0 for j in range(M.shape[1]))
        s2 &= bad == (o != 2)
Ph = sp.Matrix([[0, 0, -1], [sp.I, 0, 0], [0, sp.exp(sp.I * sp.Rational(2, 7)), 0]])
s2 &= is_monomial(Ph)
s2 &= sp.simplify(table_sum([Ph], x3v, p) - (r1 ** p + r2 ** p + r3 ** p)) == 0
e2 = sp.Matrix([0, 1])
s2 &= all(sp.simplify(sum(sp.Abs(e) ** o for e in (K1.subs(p, o) * e2)) - 1) != 0 for o in SAMPLE)
res['S2'] = s2


# ---------------------------------------------------------------- S3
def reachable(M, cap=60):
    n = M.shape[0]
    seen, todo = [], [sp.eye(n).col(j) for j in range(n)]
    while todo:
        v = todo.pop()
        if any(sp.simplify(v - w) == sp.zeros(n, 1) for w in seen):
            continue
        seen.append(v)
        if len(seen) > cap:
            return None
        todo.append(sp.simplify(M * v))
    return seen


def own_exponents(v):
    """Exponent set of one state: 'all', a one-element set, or None (unclassified)."""
    mods = [sp.nsimplify(sp.Abs(e)) for e in v if sp.simplify(e) != 0]
    if len(mods) == 1:
        return 'all' if mods[0] == 1 else set()
    if len(mods) >= 2 and all(0 < m < 1 for m in mods):
        roots = {o for o in SAMPLE if sp.simplify(sum(m ** o for m in mods) - 1) == 0}
        # strict decrease of each term m^p (log m < 0) gives at most one root
        return roots if len(roots) <= 1 and all(sp.log(m) < 0 for m in mods) else None
    return None


def method_A(states):
    out = 'all'
    for v in states:
        e = own_exponents(v)
        if e is None:
            return None
        if e != 'all':
            out = set(e) if out == 'all' else out & e
    return out


def method_B(states):
    ok = {o for o in SAMPLE
          if all(sp.simplify(sum(sp.Abs(e) ** o for e in v) - 1) == 0 for v in states)}
    return 'all' if ok == set(SAMPLE) else ok


s3 = True
cases = []
for q in (2, 3):
    a = 2 ** sp.Rational(-1, q)
    N = sp.Matrix([[0, 0, 0], [a, 1, 0], [a, 0, 1]])
    cases.append((N, {q}))
    s3 &= all(e >= 0 for e in N) and not is_monomial(N) and N.det() == 0
S = sp.Matrix([[0, 1, -1], [sp.Rational(1, 2), 0, 0], [-sp.Rational(1, 2), 0, 0]])
s3 &= not is_monomial(S)
cases.append((S, {1}))
R = 2 ** sp.Rational(-1, 2) * sp.Matrix([[1, -1], [1, 1]])
cases.append((R, {2}))
Q = sp.Matrix([[0, -1, 0], [0, 0, 1], [1, 0, 0]])
cases.append((Q, 'all'))
for M, want in cases:
    st = reachable(M)
    s3 &= st is not None
    A, B = method_A(st), method_B(st)
    s3 &= A == want and B == want
st_S = reachable(S)
s3 &= any(e < 0 for v in st_S for e in v)                      # signed reachable states
st_R = reachable(R)
s3 &= any(sum(1 for e in v if e != 0) == 1 and v not in [sp.eye(2).col(0), sp.eye(2).col(1)]
          for v in st_R)                                         # cancellation occurs
res['S3'] = s3

for k, v in res.items():
    print(k, 'PASS' if v else 'FAIL')
print('ALL PASS' if all(res.values()) else 'SOME FAIL')
raise SystemExit(0 if all(res.values()) else 1)
