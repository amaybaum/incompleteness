"""Reviewer checks for ASSESS-1059 r3 (WIP / UNVERIFIED; fresh independent review).

Generic mathematical objects only (columns, matrices, Kraus families, Lie algebras). No OI
mechanism is computed. Imports no earlier script. Run: python3 -I rv3_1059_checks.py

F1  Column lemma, existence and uniqueness. For a column with >= 2 nonzero entries, all of modulus
    in (0,1), h(p) = sum |c|^p - 1 changes sign exactly once on (0, oo): h(0+) = (#nonzero) - 1 > 0,
    h -> -1, and h' < 0. Checked exactly on columns normalised in l^1, l^2, l^3, l^(1/2) and on one
    column, (1/2, 1/3), whose exponent is none of 1/2, 1, 2, 3 (root bracketed in (1/2, 1)).
    Mutation-tested (see the review): six single-line mutants each turn one check to FAIL.
F2  Dilation lemma, non-vacuous form. For complete Kraus families (sum K^dag K = 1), m blocks of
    n x n, n <= 3, m <= 2: for every assignment of one nonzero entry per dilation column (generic
    unit phases as values), the Gram matrix is COMPUTED and monomiality of each block is decided by
    brute force over (sigma, d) with K = P_sigma diag(d) (the kernel's IsMonomial shape). Claim
    tested: Gram = 1 implies every block monomial. Countercontrol: the same single-entry patterns
    with Gram != 1 include non-monomial blocks (e.g. K = [[1,1],[0,0]]), so completeness is
    load-bearing. Positive instances: exact rational unitaries (Cayley) cut into Kraus blocks that
    are non-monomial have a dilation column with >= 2 nonzero entries.
F3  The complex drive carries the phase (independent construction). gateFlow(t) is built as the
    kernel defines it, 1 + (e^{i pi t} - 1)(1 - P)/2 with P the transposition matrix.
    e^{-i th X} (from cos/sin, not from a matrix exponential routine) equals
    e^{-i th} gateFlow(2 th / pi) diag(1,1,e^{i th}); the quarter-turn identity; gateFlow fixes the
    all-ones vector at every t while the drive moves it for th not in pi Z; the real rotation moves
    it too and lies in a real Lie algebra of dimension 3 with its permutation conjugates, against 8
    for i X.
F4  Where the 2 sits if unitarity is not posited (Lamperti-type check). M_p = 2^{-1/p}[[1,-1],[1,1]]
    has l^p-normalised columns for every p; requiring sum |amp|^p = 1 also on the reachable state
    M_p^2 e_1 forces p = 2 (interference). The nonnegative analogue N_p = 2^{-1/p}[[1,1],[1,1]] forces
    p = 1. So with linear dynamics and the readout required on every reachable state, the exponent is
    fixed by the amplitude field and interference, unitarity being an output; R3-C's attribution of
    the 2 to posited unitarity is relative to H-LIN.
F5  Root insertion. {2^{-k/2} P_s} over 2^k distinct permutations: outcome table uniform 2^{-k}
    (the counting law) at p = 2, p-admissible only at p = 2, complete.
"""
import itertools

import sympy as sp

p = sp.symbols('p', positive=True)
out = {}


def nz(col):
    return [c for c in col if c != 0]


# ---------- F1
def unique_root_bracket(col, lo, hi):
    a = [sp.Abs(sp.nsimplify(c)) for c in nz(col)]
    assert len(a) >= 2 and all(0 < x < 1 for x in a)
    h = sum(x ** p for x in a) - 1
    hp = sp.diff(h, p)
    ok = all(bool(sp.N(sp.Abs(x)) < 1) for x in a)
    ok &= sp.limit(h, p, 0, '+') == len(a) - 1
    ok &= sp.limit(h, p, sp.oo) == -1
    # derivative is a sum of negative terms x^p log x, x in (0,1)
    ok &= all(bool(sp.log(x) < 0) for x in a)
    ok &= bool(h.subs(p, lo) > 0) and bool(h.subs(p, hi) < 0)
    return ok, h


f1 = True
cases = [([sp.Rational(1, 3), sp.Rational(2, 3)], 1),
         ([sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7)], 2),
         ([2 ** sp.Rational(-1, 3)] * 2, 3),
         ([sp.Rational(1, 4), sp.Rational(1, 4)], sp.Rational(1, 2))]
for col, q in cases:
    ok, h = unique_root_bracket(col, q / 2, 2 * q)
    f1 &= ok and sp.simplify(h.subs(p, q)) == 0
    for other in (sp.Rational(1, 2), 1, 2, 3):
        if other != q:
            f1 &= sp.simplify(h.subs(p, other)) != 0
# a column whose exponent is not 1, 2, 3, 1/2: (1/2, 1/3): root strictly between 1/2 and 1
ok, h = unique_root_bracket([sp.Rational(1, 2), sp.Rational(1, 3)], sp.Rational(1, 2), 1)
f1 &= ok and all(sp.simplify(h.subs(p, q)) != 0 for q in (sp.Rational(1, 2), 1, 2, 3))
out['F1'] = f1


# ---------- F2
def perm_matrix(s):
    n = len(s)
    M = sp.zeros(n, n)
    for j, i in enumerate(s):
        M[i, j] = 1
    return M


def is_monomial(K):
    n = K.shape[0]
    for s in itertools.permutations(range(n)):
        P = perm_matrix(s)
        d = P.T * K          # P is orthogonal: K = P diag(d) iff P^T K is diagonal
        if all(d[i, j] == 0 for i in range(n) for j in range(n) if i != j):
            return True
    return False


phases = [1, sp.I, -1, -sp.I]
f2_claim = True
f2_counter = False
n_patterns = 0
for n in (1, 2, 3):
    for m in (1, 2):
        positions = [(r, i) for r in range(m) for i in range(n)]
        for assign in itertools.product(positions, repeat=n):
            n_patterns += 1
            V = sp.zeros(m * n, n)
            for j, (r, i) in enumerate(assign):
                V[r * n + i, j] = phases[(j + r + i) % 4]
            gram = V.H * V
            blocks = [V[r * n:(r + 1) * n, :] for r in range(m)]
            mono = all(is_monomial(B) for B in blocks)
            if gram == sp.eye(n):
                f2_claim &= mono
            elif not mono:
                f2_counter = True
# positive instances: Cayley rational unitaries, 4x4 = 2 blocks of 2x2 stacked as an isometry 4x2
pos = True
rng_A = [sp.Matrix([[0, 1, 2, 0], [-1, 0, 1, 3], [-2, -1, 0, 1], [0, -3, -1, 0]]),
         sp.Matrix([[0, 2, 0, 1], [-2, 0, 1, 0], [0, -1, 0, 2], [-1, 0, -2, 0]])]
count_nonmono = 0
for A in rng_A:
    I4 = sp.eye(4)
    U = (I4 - A) * (I4 + A).inv()
    pos &= sp.simplify(U.T * U - I4) == sp.zeros(4, 4)
    V = U[:, :2]                       # isometry 4x2 -> two Kraus blocks of size 2x2
    pos &= sp.simplify(V.T * V - sp.eye(2)) == sp.zeros(2, 2)
    blocks = [V[0:2, :], V[2:4, :]]
    if any(not is_monomial(B) for B in blocks):
        count_nonmono += 1
        pos &= any(len(nz(list(V.col(j)))) >= 2 for j in range(2))
pos &= count_nonmono >= 1
out['F2'] = f2_claim and f2_counter and pos


# ---------- F3
th, t = sp.symbols('theta t', real=True)
X = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
P01 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
Pi01 = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]])   # projector on the pair


def gate_flow(tt):
    return sp.eye(3) + (sp.exp(sp.I * sp.pi * tt) - 1) * (sp.eye(3) - P01) / 2


# X^2 = projector on the pair, so e^{-i th X} = (1 - Pi01) + cos th Pi01 - i sin th X
drive = (sp.eye(3) - Pi01) + sp.cos(th) * Pi01 - sp.I * sp.sin(th) * X
lhs_minus_rhs = drive - sp.exp(-sp.I * th) * gate_flow(2 * th / sp.pi) * sp.diag(1, 1, sp.exp(sp.I * th))
f3 = lhs_minus_rhs.applyfunc(lambda z: sp.simplify(sp.expand(z.rewrite(sp.exp)))) == sp.zeros(3, 3)
f3 &= sp.simplify(drive.subs(th, sp.pi / 2) * P01 - (-sp.I) * sp.diag(1, 1, sp.I)) == sp.zeros(3, 3)
f3 &= sp.simplify(X * X - Pi01) == sp.zeros(3, 3)
ones = sp.Matrix([1, 1, 1])
f3 &= sp.simplify(gate_flow(t) * ones - ones) == sp.zeros(3, 1)          # layer flow fixes the ray
moved = sp.simplify(drive * ones)
f3 &= sp.Matrix.hstack(ones, moved.subs(th, sp.pi / 3)).rank() == 2       # drive moves it
f3 &= sp.Matrix.hstack(ones, moved.subs(th, sp.pi / 2)).rank() == 2       # also at the quarter turn
f3 &= sp.Matrix.hstack(ones, moved.subs(th, sp.pi)).rank() == 2           # th = pi: relative sign, ray moved
f3 &= sp.Matrix.hstack(ones, moved.subs(th, 2 * sp.pi)).rank() == 1       # th = 2 pi: identity
Rgen = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
rot = sp.eye(3) - Pi01 + sp.cos(sp.pi / 5) * Pi01 + sp.sin(sp.pi / 5) * Rgen
f3 &= sp.Matrix.hstack(ones, sp.simplify(rot * ones)).rank() == 2


def lie_closure_dim(gens):
    def flat(M):
        return [sp.re(x) for x in M] + [sp.im(x) for x in M]
    mats, rows = [], []
    queue = list(gens)
    while queue:
        M = sp.expand(queue.pop())
        trial = rows + [flat(M)]
        if sp.Matrix(trial).rank() > len(rows):
            rows.append(flat(M))
            for N in mats:
                queue.append(M * N - N * M)
            mats.append(M)
    return len(rows)


perms = [perm_matrix(s) for s in itertools.permutations(range(3))]
f3 &= lie_closure_dim([Q * Rgen * Q.T for Q in perms]) == 3
f3 &= lie_closure_dim([Q * (sp.I * X) * Q.T for Q in perms]) == 8
out['F3'] = f3


# ---------- F4
def lp_sum(v, q):
    return sum(sp.Abs(x) ** q for x in v)


f4 = True
signed = 2 ** (-1 / p) * sp.Matrix([[1, -1], [1, 1]])
nonneg = 2 ** (-1 / p) * sp.Matrix([[1, 1], [1, 1]])
e1 = sp.Matrix([1, 0])
for M, want in ((signed, 2), (nonneg, 1)):
    # columns l^p-normalised for every p
    f4 &= all(sp.simplify(lp_sum(M.col(j), p) - 1) == 0 for j in range(2))
    v2 = sp.simplify(M * M * e1)
    s2 = sp.simplify(sp.powsimp(lp_sum(v2, p), force=True))
    sols = sp.solve(sp.Eq(s2, 1), p)
    f4 &= sols == [want]
# signed case at p = 2 is orthogonal (unitarity as an output), nonneg case at p = 1 is stochastic
S2 = signed.subs(p, 2)
f4 &= sp.simplify(S2.T * S2 - sp.eye(2)) == sp.zeros(2, 2)
N1 = nonneg.subs(p, 1)
f4 &= all(sum(N1.col(j)) == 1 for j in range(2))
# control: at p != 2 the signed column alone is admissible (column test cannot see it)
f4 &= sp.simplify(lp_sum(signed.subs(p, 3).col(0), 3) - 1) == 0
out['F4'] = f4

# ---------- F5
f5 = True
for k in (1, 2):
    ps = list(itertools.permutations(range(3)))[: 2 ** k]
    Ks = [2 ** sp.Rational(-k, 2) * perm_matrix(s) for s in ps]
    f5 &= sp.simplify(sum((K.T * K for K in Ks), sp.zeros(3, 3)) - sp.eye(3)) == sp.zeros(3, 3)
    V = sp.Matrix.vstack(*Ks)
    for j in range(3):
        col = nz(list(V.col(j)))
        f5 &= [sp.simplify(c ** 2) for c in col] == [sp.Rational(1, 2 ** k)] * (2 ** k)
        f5 &= sp.solve(sp.Eq(sp.powsimp(sum(sp.Abs(c) ** p for c in col), force=True), 1), p) == [2]
    f5 &= all(is_monomial(K) for K in Ks)
out['F5'] = f5

for key, v in out.items():
    print(key, 'PASS' if v else 'FAIL')
print('F2 single-entry dilation patterns:', n_patterns)
print('ALL PASS' if all(out.values()) else 'SOME FAIL')
raise SystemExit(0 if all(out.values()) else 1)
