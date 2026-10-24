"""Independent review of mc1 node 1b (exact SymPy). Tensor order (ancilla, data), opposite to the node's probes."""
import sys
import sympy as sp
from sympy import Matrix, I, sqrt, eye, zeros, Rational, symbols
R = []
def chk(n, ok): R.append((n, bool(ok))); print(('PASS ' if ok else 'FAIL ') + n)
def kr(A, B): return Matrix(sp.kronecker_product(A, B))
def z(M): return all(sp.simplify(sp.expand(x)) == 0 for x in M)
X = Matrix([[0, 1], [1, 0]]); Z = Matrix([[1, 0], [0, -1]]); I2 = eye(2)
k0, k1 = Matrix([1, 0]), Matrix([0, 1]); pl, mi = Matrix([1, 1]) / sqrt(2), Matrix([1, -1]) / sqrt(2)
Pr = lambda v: v * v.H
one = Matrix([1, 1]); u = one / sqrt(2)
rho = Matrix(2, 2, symbols('a b c d'))
def ch(Ks, r): return sum((K * r * K.H for K in Ks), zeros(2, 2))
def span_has_one(Ks):
    M = Matrix.hstack(*[K.H * one for K in Ks]); return Matrix.hstack(M, one).rank() == M.rank()
# (i) heralded Z: ancilla |0>, X-test on ancilla, outcome '-' -> CNOT(anc target, data control), discard
CN = kr(I2, Pr(k0)) * 0 + kr(Pr(k0), I2) * 0  # (unused guard)
CN = Matrix(4, 4, lambda i, j: 0)
for d in (0, 1):
    for a in (0, 1):
        CN[2 * (a ^ d) + d, 2 * a + d] = 1      # index = 2*anc + data ; data controls, ancilla target
att = kr(k0, I2)
Ks_s = [kr(cv.H, I2) * CN * kr(Pr(mi), I2) * att for cv in (k0, k1)]
Ks_f = [kr(cv.H, I2) * kr(Pr(pl), I2) * att for cv in (k0, k1)]
chk('i1 success branch = 1/2 Z rho Z, each success Kraus prop. Z', z(ch(Ks_s, rho) - Z * rho * Z / 2)
    and all(z(K - K[0, 0] * Z) for K in Ks_s))
chk('i2 failure branch = 1/2 rho', z(ch(Ks_f, rho) - rho / 2))
chk('i3 complete, and sum K^H 1 over the whole instrument = 1 (OnesNormal, this very list)',
    z(sum((K.H * K for K in Ks_s + Ks_f), zeros(2, 2)) - I2) and z(sum((K.H * one for K in Ks_s + Ks_f), zeros(2, 1)) - one))
chk('i4 success branch alone: 1 not in span{K^H 1} (no decomposition of it is OnesNormal)', not span_has_one(Ks_s))
chk('i5 coarse-graining the herald gives dephasing (rho+ZrhoZ)/2, not Ad Z', z(ch(Ks_s + Ks_f, rho) - (rho + Z * rho * Z) / 2))
# (ii) RUS truncated at depth n: recursion Phi_0 = id ; Phi_n = S + F o Phi_{n-1}
def Phi(n, r):
    if n == 0: return r
    return ch(Ks_s, r) + Phi(n - 1, ch(Ks_f, r))
for n in range(1, 6):
    p = Rational(1, 2 ** n)
    assert z(Phi(n, rho) - ((1 - p) * Z * rho * Z + p * rho)), n
chk('ii1 Phi_n = (1-2^-n) Ad Z + 2^-n id, n=1..5, from the protocol recursion', True)
nn = symbols('n', positive=True, integer=True)
dist = sp.simplify(((1 - 2 ** -nn) * 0 + 2 ** -nn))  # Choi: Phi_n - AdZ = 2^-n (id - AdZ); ||id-AdZ||_Choi-trace/2 = 1
J = lambda f: sum((kr(Matrix(2, 2, lambda i, j: 1 if (i, j) == (a, b) else 0), f(Matrix(2, 2, lambda i, j: 1 if (i, j) == (a, b) else 0))) for a in (0, 1) for b in (0, 1)), zeros(4, 4)) / 2
D = J(lambda r: r) - J(lambda r: Z * r * Z)
ev = D.eigenvals(); tn = sum(abs(k) * m for k, m in ev.items())
chk('ii2 normalized-Choi trace norm of (id - AdZ) is %s, so ||Phi_n - AdZ||_1(Choi) = 2^-n * %s' % (tn, tn), tn == 2)
# OnesNormal decompositions
for n in range(1, 7):
    p = Rational(1, 2 ** n)
    Ks = [p * I2] * (2 ** n) + [sqrt((1 - p) / 2) * Z, -sqrt((1 - p) / 2) * Z]
    assert z(ch(Ks, rho) - ((1 - p) * Z * rho * Z + p * rho)) and z(sum((K.H * K for K in Ks), zeros(2, 2)) - I2) \
        and z(sum((K.H * one for K in Ks), zeros(2, 1)) - one), n
chk('ii3 2^n copies of 2^-n I + pair +-sqrt((1-2^-n)/2) Z: channel Phi_n, complete, sum K^H 1 = 1 (n=1..6)', True)
p = Rational(1, 4)
Ko = [sqrt(p) * I2, sqrt((1 - p) / 2) * Z, -sqrt((1 - p) / 2) * Z]
chk('ii4 owner sketch {sqrt p I, +-sqrt((1-p)/2) Z}: channel right, sum K^H 1 = sqrt(p) 1 != 1',
    z(ch(Ko, rho) - ((1 - p) * Z * rho * Z + p * rho)) and z(sum((K.H * one for K in Ko), zeros(2, 1)) - sqrt(p) * one) and sqrt(p) != 1)
# minimality: superoperators rho->A rho B^H, A,B in {I,Z}, are linearly independent, so a Kraus list sum_j (a_j I + b_j Z)
# reproduces Phi_n iff sum|a|^2 = 2^-n, sum|b|^2 = 1-2^-n, sum a conj(b) = 0 ; sum K^H 1 = 1 iff sum conj(a)=1, sum conj(b)=0.
vecs = [Matrix(kr(A, B.conjugate())).reshape(16, 1) for A in (I2, Z) for B in (I2, Z)]
chk('ii5 {I(x)I, I(x)Z, Z(x)I, Z(x)Z} superoperators independent (rank 4) => Kraus coefficients determined as stated',
    Matrix.hstack(*vecs).rank() == 4)
# Cauchy-Schwarz: |sum a_j| <= sqrt(m) sqrt(sum|a|^2) = sqrt(m 2^-n) ; =1 needs m >= 2^n (+ the Z part needs >= 1 more
# operator with b != 0 ... check whether 2^n total suffices: equality in C-S forces all a_j = 2^-n, then sum a conj(b)=0
# gives 2^-n sum conj(b) = 0 -- consistent; sum|b|^2 = 1-2^-n with sum b = 0 and b_j paired on the same operators.)
nn2 = 2
m = 2 ** nn2; p = Rational(1, m); s_ = sp.symbols('t0:%d' % m)
# try exactly m = 2^n operators: a_j = p (forced by C-S equality), b = (t0..t_{m-1}) real, sum b = 0, sum b^2 = 1-p
sol = sp.solve([sum(s_), sum(t ** 2 for t in s_) - (1 - p), s_[2], s_[3]], s_, dict=True)
Ks = [p * I2 + sol[0][s_[0]] * Z, p * I2 + sol[0][s_[1]] * Z, p * I2, p * I2]
chk('ii6 the bound 2^n is attained by exactly 2^n operators (n=2: a_j = 1/4, b = (+-sqrt(3/8),0,0)): node list of 2^n+2 is not minimal',
    z(ch(Ks, rho) - ((1 - p) * Z * rho * Z + p * rho)) and z(sum((K.H * one for K in Ks), zeros(2, 1)) - one) and len(Ks) == m)
chk('ii7 limit Ad Z: Kraus prop. Z, 1 not in span{Z^H 1} -> not OnesNormal', not span_has_one([Z]))
# invariant 2: fixing the uniform state
Pu = u * u.H
for n in (1, 2, 3):
    pp = Rational(1, 2 ** n)
    assert z(Phi(n, Pu) - ((1 - pp) * mi * mi.H + pp * Pu))
chk('u1 Phi_n(|u><u|) = (1-2^-n)|-><-| + 2^-n |u><u|, n=1..3 (fails to fix u)', True)
readout = [Pr(k0), Pr(k1)]
chk('u2 NATIVE configuration readout (coarse-grained) does not fix |u><u| (gives I/2): the uniform-state condition is not an invariant of the native theory',
    z(ch(readout, Pu) - I2 / 2))
chk('u3 ...while native readout is OnesNormal (sum P^H 1 = 1)', z(sum((P.H * one for P in readout), zeros(2, 1)) - one))
# implication: fixing |u><u| => 1 in span{K^H 1}: instance with a non-unitary channel fixing u (dephasing in X basis)
dX = [Pr(pl), Pr(mi)]
chk('u4 X-basis dephasing fixes |u><u| and is OnesNormal (implication instance)', z(ch(dX, Pu) - Pu) and span_has_one(dX))
# invariant 3: nonnegativity
Jm = Matrix([[1, 1], [1, 1]])
chk('n1 Phi_2([[1,1],[1,1]]) = [[1,-1/2],[-1/2,1]]', z(Phi(2, Jm) - Matrix([[1, -Rational(1, 2)], [-Rational(1, 2), 1]])))
chk('n2 Phi_1 keeps [[1,1],[1,1]] nonnegative (off-diagonal 0)', z(Phi(1, Jm) - I2))
# d1: ||Z - cV|| for ones-fixing V: (Z - cV)u = |-> - c z u, norm sqrt(2) (|cz|=1), so ||Z-cV|| >= sqrt 2 (node: >= 1)
cz = symbols('cz')
w = Z * u - cz * u
chk('d1 ||(Z - cV)u||^2 = 1 + |cz|^2 = 2 for any ones-fixing V, |c|=1: bound is sqrt(2), node states >= 1 (true, not sharp)',
    sp.simplify(sp.expand((w.H * w)[0].subs(sp.conjugate(cz), 1 / cz))) == 2)
fails = [n for n, ok in R if not ok]
print('SUMMARY', len(R) - len(fails), 'PASS', len(fails), 'FAIL'); sys.exit(1 if fails else 0)
