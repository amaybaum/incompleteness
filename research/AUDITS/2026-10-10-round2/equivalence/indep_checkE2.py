#!/usr/bin/env python3
"""Coordinator's independent check of the research/equivalence thread's round-2 exact claims (branch head 5d266133;
NOTES-E9, NOTES-E10).  Own code; reads nothing.  Run: python3 -I -B indep_checkE2.py
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH per line; INDEP-E2-FIXED iff all CONFIRMED.
Run 2 (run 1 kept as indep_checkE2.run1.*): run 1 crashed in X4 inside my own harness -- W_for(n) returned the unitary with
W sigma_x W^* = n.sigma, the transpose of the thread's convention W^* sigma_x W = n.sigma, so [W|0>, X W|1>] was singular on
the first instance before any X4 verdict was printed.  Run 2 returns its adjoint.  X1-X3 were CONFIRMED in run 1.
Conventions: tables 4x4 (control index first), pauliW(w) = (1/4) sum w_mn sigma_m (x) sigma_n, ipW the entrywise sum,
cnot = Ad(P0 (x) 1 + P1 (x) X) with the control the first token, actT R = w . hom(R)^T.  Signed-permutation closure
machinery as in indep_checkC.py (round 1), reused as my own code.
 X1 (E10 L2) actT cyc3 = Ad(1 (x) U_J) with U_J = (1/sqrt 2) [[-i, -1], [-i, 1]]: U_J is unitary, Ad(U_J) sends
    sigma_x -> sigma_y -> sigma_z -> sigma_x (e_x -> e_y -> e_z), and the table action of Ad(1 (x) U_J) equals actT J
    on all 16 basis tables.  Also actT R_z(t) = Ad(1 (x) exp(-i t sigma_z / 2)) at cos t = 3/5 (exact).
 X2 (E10 F1) the group <cnot, actT R_z(pi/2), actT cyc3> acting on W 3 by signed permutations of the 16 entries has
    order 384; phi0 = (1, 2, 3i, -1+i)/4 (unit) has a table that no element of the group carries to a rank-one table
    (a pure state's table is rank one iff the state is a product); control: the Bell state (|00> + |11>)/sqrt 2 is
    carried to a product table (by cnot); every product state has a rank-one table (symbolic in the Bloch vectors).
 X3 (E10 section 3) cos theta0 = 3/5: theta0/pi is irrational.  Exact argument: (3 + 4i)/5 = ((2 + i)/(2 - i)); if
    ((3+4i)/5)^n = 1 then (2+i)^n = (2-i)^n in Z[i], impossible since 2+i and 2-i are non-associate Gaussian primes
    (norm 5; (2+i)/(2-i) = (3+4i)/5 is not a unit of Z[i]).  Checked: (2+i)^2 = 3+4i; N(2+-i) = 5 (prime, so both are
    Gaussian primes); (2+i)/(2-i) not in Z[i]; no power R_z(theta0)^n, n <= 3000, is the identity (exact rationals).
 X4 (E10 L4) the reachability word: for pure psi = |0> x + |1> y (x, y in C^2, |x|^2 + |y|^2 = 1), a = |x|, b = |y|,
    with kappa = <x^|y^>, n = (Re kappa, -Im kappa, sqrt(1 - |kappa|^2)), W unitary with W^* sigma_x W = n . sigma,
    W' = [x^ y^] [W|0>, X W|1>]^-1: g = (1 (x) W') CNOT (1 (x) W) CNOT maps (a|0> + b|1>) (x) |0> to psi up to phase.
    Checked on my own three Gaussian-rational states (not the thread's instances), exactly: the output density matrix
    equals |psi><psi|, W' is unitary, and the identity CNOT (1 (x) W) CNOT = P0 (x) W + P1 (x) X W X holds symbolically.
 X5 (E10 L5) the cone step on an exact instance: a PSD 4x4 Gaussian-rational matrix is a sum of rank-one terms (Gram
    decomposition by exact LDL), and for an omega in Q3 and every vector v, v^* rho(omega) v = (1/4) ipW(omega, table(vv^*)).
 X6 (E9 M1-M3) exhaustive monomial instance at N = 4 over fourth-root phases (24 permutations x 256 diagonals = 6144
    unitaries): conjugation maps every matrix unit to a matrix unit iff the diagonal is scalar (96 unitaries), giving
    exactly 24 distinct maps (the permutation conjugations); the Householder reflection H = 1 - 2 v v^T/25, v = (1,2,2,4),
    is orthogonal and conjugates every one of the 16 matrix units to a non-matrix-unit.
 X7 (E9 P1, P2, K1) the single-site stage map E_01 -> i E_01 (phase) and E_01 -> -E_01 (conjugation by Z) are not
    produced by any permutation transport of E_01 (x) 1 (entries in {0, 1}; 24 permutations of the four configurations);
    [E_01, E_10] = diag(1, -1) != 0 (no commutative member); Jordan-Wigner two-site copies anticommute (a0 a1 = -a1 a0)
    while their even parts commute.
"""
import itertools
from fractions import Fraction as Fr
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, expand, simplify, conjugate, kronecker_product as kron, symbols
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""), flush=True)
I2 = eye(2); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
SG = [I2, SX, SY, SZ]; KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4
def tab(M):
    out = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            e = expand((KR[(m, n)] * M).trace())
            if not e.is_Rational: e = sp.nsimplify(simplify(e))
            out[m, n] = e
    return out
def ipW(a, b): return expand(sum(a[i, j] * b[i, j] for i in range(4) for j in range(4)))
def E(m, n): B = zeros(4, 4); B[m, n] = 1; return B
def homMap(Rm):
    M = eye(4)
    for i in range(3):
        for j in range(3): M[i + 1, j + 1] = Rm[i, j]
    return M
def actT(Rm, w): return w * homMap(Rm).T
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])      # P0 (x) 1 + P1 (x) X, control first
def cnotW(w): return tab(CNOT * pauliW(w) * CNOT.H)
def adT(U, w): return tab(kron(I2, U) * pauliW(w) * kron(I2, U).H)
cyc3 = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])                              # e_x -> e_y -> e_z -> e_x
def Rz_cs(c, s): return Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])
BASIS = [E(m, n) for m in range(4) for n in range(4)]

print("== X1 the token generators as unitary conjugations")
UJ = Matrix([[-I, -1], [-I, 1]]) / sqrt(2)
unit = simplify(UJ * UJ.H - I2) == zeros(2, 2)
perm = simplify(UJ * SX * UJ.H - SY) == zeros(2, 2) and simplify(UJ * SY * UJ.H - SZ) == zeros(2, 2) and simplify(UJ * SZ * UJ.H - SX) == zeros(2, 2)
cycJ = all(adT(UJ, B) == actT(cyc3, B) for B in BASIS)
c0, s0 = Q(3, 5), Q(4, 5)
# exp(-i t sigma_z/2) = diag(e^{-it/2}, e^{it/2}); with cos t = 3/5: e^{it/2} = ((1+c)/2)^{1/2} + i ((1-c)/2)^{1/2} = (2 + i)/sqrt 5
eh = (2 + I) / sqrt(5)
Uz = Matrix.diag(conjugate(eh), eh)
flow = all(simplify(adT(Uz, B) - actT(Rz_cs(c0, s0), B)) == zeros(4, 4) for B in BASIS) and simplify(eh ** 2 - (c0 + I * s0)) == 0
rec('X1', unit and perm and cycJ and flow,
    'U_J unitary; Ad(U_J): sigma_x -> sigma_y -> sigma_z -> sigma_x; Ad(1 x U_J) = actT cyc3 on all 16 basis tables; Ad(1 x exp(-i t sigma_z/2)) = actT R_z(t) at cos t = 3/5')

print("== X2 the finite clause: order 384, phi0 unreachable")
def elem_from_fun(f):
    src = [None] * 16; sgn = [None] * 16
    for m in range(4):
        for n in range(4):
            img = f(E(m, n)); nz = [(i, j) for i in range(4) for j in range(4) if img[i, j] != 0]
            assert len(nz) == 1 and abs(img[nz[0]]) == 1, 'not a signed permutation of entries'
            i, j = nz[0]; src[4 * i + j] = 4 * m + n; sgn[4 * i + j] = int(img[i, j])
    return (tuple(src), tuple(sgn))
def apply_elem(g, t): return tuple(g[1][k] * t[g[0][k]] for k in range(16))
def compose(g, h): return (tuple(h[0][g[0][k]] for k in range(16)), tuple(g[1][k] * h[1][g[0][k]] for k in range(16)))
IDe = (tuple(range(16)), tuple([1] * 16))
def closure(gens):
    seen = {IDe}; frontier = [IDe]
    while frontier:
        nxt = []
        for a in frontier:
            for g in gens:
                b = compose(g, a)
                if b not in seen: seen.add(b); nxt.append(b)
        frontier = nxt
    return seen
G = closure([elem_from_fun(cnotW), elem_from_fun(lambda w: actT(Rz_cs(0, 1), w)), elem_from_fun(lambda w: actT(cyc3, w))])
def vec(M): return tuple(M[i, j] for i in range(4) for j in range(4))
def state_table(psi):
    psi = Matrix(psi); return tab(psi * psi.H / expand((psi.H * psi)[0]))
def rank1_tuple(t):
    M = [t[4 * m:4 * m + 4] for m in range(4)]
    return all(expand(M[i][k] * M[j][l] - M[i][l] * M[j][k]) == 0 for i in range(4) for j in range(4) for k in range(4) for l in range(4))
phi0 = [1, 2, 3 * I, -1 + I]
n_phi0 = expand(sum(c * conjugate(c) for c in phi0))
w0 = vec(state_table(phi0))
reach = sum(1 for g in G if rank1_tuple(apply_elem(g, w0)))
bell = vec(state_table([1, 0, 0, 1]))
bell_reach = sum(1 for g in G if rank1_tuple(apply_elem(g, bell)))
# every product state has a rank-one table (symbolic): table(rho_x (x) rho_y) = (1, x) (1, y)^T
a1, a2, a3, b1, b2, b3 = symbols('a1 a2 a3 b1 b2 b3', real=True)
rho_x = (I2 + a1 * SX + a2 * SY + a3 * SZ) / 2; rho_y = (I2 + b1 * SX + b2 * SY + b3 * SZ) / 2
tp = Matrix(4, 4, lambda m, n: expand((KR[(m, n)] * kron(rho_x, rho_y)).trace()))
prod_rank1 = tp == Matrix([1, a1, a2, a3]) * Matrix([1, b1, b2, b3]).T
rec('X2', len(G) == 384 and n_phi0 == 16 and reach == 0 and bell_reach > 0 and prod_rank1 and not rank1_tuple(w0),
    '|<cnot, actT R_z(pi/2), actT cyc3>| = 384; phi0 (|phi0|^2 = 16, table not rank one) is carried to a rank-one table by no element; the Bell state by some; product tables are rank one',
    'order %d, phi0 reachable by %d elements, Bell by %d' % (len(G), reach, bell_reach))

print("== X3 theta0/pi irrational, cos theta0 = 3/5")
z = 2 + I
sq = expand(z ** 2) == 3 + 4 * I
nrm = expand(z * conjugate(z)) == 5 and sp.isprime(5)
ratio = expand(z / conjugate(z)); ratio_unit = ratio in (1, -1, I, -I); ratio_gauss = all(x.is_integer for x in (sp.re(ratio), sp.im(ratio)))
Mz = Rz_cs(Fr(3, 5), Fr(4, 5)); P = [[Fr(int(Mz[i, j] == 1)) for j in range(3)] for i in range(3)]
Mf = [[Fr(3, 5), Fr(-4, 5), Fr(0)], [Fr(4, 5), Fr(3, 5), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
def mul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
Id = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
cur = Id; hit = None
for n in range(1, 3001):
    cur = mul(cur, Mf)
    if cur == Id: hit = n; break
rec('X3', sq and nrm and (not ratio_unit) and (not ratio_gauss) and hit is None,
    '(2+i)^2 = 3+4i, N(2+i) = 5 prime, (2+i)/(2-i) = (3+4i)/5 is neither a unit nor a Gaussian integer, so ((3+4i)/5)^n != 1 for all n >= 1; no R_z(theta0)^n = 1 for n <= 3000',
    'ratio %s' % ratio)

print("== X4 the reachability word on my own instances")
P0 = Matrix([[1, 0], [0, 0]]); P1 = Matrix([[0, 0], [0, 1]])
w11, w12, w21, w22 = symbols('w11 w12 w21 w22')
Wsym = Matrix([[w11, w12], [w21, w22]])
ident = expand(CNOT * kron(I2, Wsym) * CNOT - (kron(P0, Wsym) + kron(P1, SX * Wsym * SX))) == zeros(4, 4)
def unit_vec(v): return v / sqrt(expand((v.H * v)[0]))
def W_for(n):
    """unitary W with W^* sigma_x W = n . sigma: columns = eigenvectors of n . sigma for +1 and -1 (then W sigma_x W^* ... ):
    take W = [u+, u-] where (n.sigma) u+- = +- u+-; then W^* (n.sigma) W = sigma_z; we need W^* sigma_x W = n.sigma, i.e.
    W = V H' with (n.sigma) = W sigma_x W^*: choose W = [ (u+ + u-)/sqrt2, (u+ - u-)/sqrt2 ]"""
    ns = n[0] * SX + n[1] * SY + n[2] * SZ
    ev = ns.eigenvects()
    up = [v for val, mult, vs in ev if simplify(val - 1) == 0 for v in vs][0]
    um = [v for val, mult, vs in ev if simplify(val + 1) == 0 for v in vs][0]
    up, um = unit_vec(up), unit_vec(um)
    Wm = Matrix.hstack((up + um) / sqrt(2), (up - um) / sqrt(2))     # Wm sigma_x Wm^* = n.sigma
    return Wm.H                                                      # W^* sigma_x W = n.sigma
def word_check(x, y):
    x, y = Matrix(x), Matrix(y)
    psi = Matrix.vstack(x, y)
    nrm = expand((psi.H * psi)[0])
    a = sqrt(expand((x.H * x)[0])); b = sqrt(expand((y.H * y)[0]))
    xh, yh = x / a, y / b
    kappa = expand((xh.H * yh)[0])
    n = (sp.re(kappa), -sp.im(kappa), sqrt(expand(1 - kappa * conjugate(kappa))))
    W = W_for(n)
    okW = simplify(W.H * SX * W - (n[0] * SX + n[1] * SY + n[2] * SZ)) == zeros(2, 2) and simplify(W.H * W - I2) == zeros(2, 2)
    u = W * Matrix([1, 0]); v = SX * W * Matrix([0, 1])
    Wp = (Matrix.hstack(xh, yh) * Matrix.hstack(u, v).inv()).applyfunc(simplify)
    okWp = simplify(Wp.H * Wp - I2) == zeros(2, 2)
    g = kron(I2, Wp) * CNOT * kron(I2, W) * CNOT
    inp = kron(Matrix([a, b]), Matrix([1, 0]))
    out = (g * inp).applyfunc(simplify)
    rho_out = (out * out.H).applyfunc(simplify); rho_psi = (psi * psi.H / nrm).applyfunc(simplify)
    return okW and okWp and simplify(rho_out - rho_psi) == zeros(4, 4) and expand(nrm) == 1, kappa
inst = [([Q(1, 2), Q(1, 2)], [Q(1, 2), I / 2]),                       # kappa = (1 + i)/2... real data
        ([Q(3, 5), 0], [0, Q(4, 5) * I]),                             # kappa = 0 (x perp y)
        ([Q(2, 3), Q(1, 3) * I], [Q(2, 3) * I, 0])]                   # |x|^2 = 5/9, |y|^2 = 4/9
res = [word_check(x, y) for x, y in inst]
rec('X4', ident and all(ok for ok, k in res),
    'CNOT (1 x W) CNOT = P0 x W + P1 x X W X symbolically; on three Gaussian-rational states the word (1 x W\') CNOT (1 x W) CNOT carries (a|0> + b|1>) x |0> to psi exactly, W and W\' unitary',
    'kappas %s' % [str(k) for ok, k in res])

print("== X5 the cone step on an instance")
Mg = Matrix([[2, 1 + I, 0, 1], [1 - I, 3, I, 0], [0, -I, 2, 1 - I], [1, 0, 1 + I, 3]])
herm = Mg.H == Mg
Lm, Dm = Mg.LDLdecomposition(hermitian=True)
gram = simplify(Lm * Dm * Lm.H - Mg) == zeros(4, 4) and all(simplify(Dm[k, k]) > 0 for k in range(4))
rank1_sum = sum((Dm[k, k] * Lm[:, k] * Lm[:, k].H for k in range(4)), zeros(4, 4))
sum_ok = simplify(rank1_sum - Mg) == zeros(4, 4)
om = tab(Mg)
vv = Matrix([1, I, 2, -1 + I])
lhs = expand((vv.H * pauliW(om) * vv)[0]); rhs = ipW(om, tab(vv * vv.H)) / 4
rec('X5', herm and gram and sum_ok and expand(lhs - rhs) == 0 and simplify(pauliW(om) - Mg) == zeros(4, 4),
    'a PSD Gaussian-rational 4x4 matrix is an exact sum of four rank-one terms (LDL), and v^* rho(omega) v = ipW(omega, table(vv^*))/4 on an instance',
    'pivots %s, v^* rho v = %s' % ([str(Dm[k, k]) for k in range(4)], lhs))

print("== X6 H-DYN on the monomial instance N = 4")
N = 4
phases = [1, I, -1, -I]
units = {(i, j): E(i, j) for i in range(N) for j in range(N)}
def is_unit(M):
    nz = [(i, j) for i in range(N) for j in range(N) if M[i, j] != 0]
    return len(nz) == 1 and M[nz[0]] == 1
cnt_unit = 0; maps = set()
for perm in itertools.permutations(range(N)):
    Pm = zeros(N, N)
    for i in range(N): Pm[perm[i], i] = 1
    for d in itertools.product(phases, repeat=N):
        U = Pm * Matrix.diag(*d)
        imgs = [expand(U * units[(i, j)] * U.H) for i in range(N) for j in range(N)]
        if all(is_unit(M) for M in imgs):
            cnt_unit += 1
            scalar = all(x == d[0] for x in d)
            assert scalar
            maps.add(tuple(vec_ := tuple(M[i, j] for M in imgs for i in range(N) for j in range(N))))
vh = Matrix([1, 2, 2, 4]); H = eye(4) - 2 * vh * vh.T / 25
orth = H * H.T == eye(4)
bad = sum(1 for i in range(N) for j in range(N) if not is_unit(expand(H * units[(i, j)] * H)))
rec('X6', cnt_unit == 96 and len(maps) == 24 and orth and bad == 16,
    '6144 monomial unitaries: H-DYN holds for exactly 96 (scalar diagonal), giving 24 distinct maps; Householder H = 1 - 2vv^T/25 orthogonal and violates H-DYN on all 16 units',
    'unitaries %d, maps %d, bad units %d' % (cnt_unit, len(maps), bad))

print("== X7 E9 P1, P2, K1 finite instances")
E01 = Matrix([[0, 1], [0, 0]]); E10 = E01.T
Zm = Matrix.diag(1, -1)
sign_img = Zm * E01 * Zm; phase_img = Matrix.diag(I, 1) * E01 * Matrix.diag(I, 1).H
X01 = kron(E01, I2)
entries = set()
for perm in itertools.permutations(range(4)):
    Pm = zeros(4, 4)
    for i in range(4): Pm[perm[i], i] = 1
    M = Pm * X01 * Pm.T
    entries |= set(M)
comm = E01 * E10 - E10 * E01
# Jordan-Wigner: a0 = sigma^- (x) 1, a1 = Z (x) sigma^-
sm = Matrix([[0, 0], [1, 0]])
a0 = kron(sm, I2); a1 = kron(Zm, sm)
anti = expand(a0 * a1 + a1 * a0) == zeros(4, 4)
even0 = [a0.H * a0, a0 * a0.H]; even1 = [a1.H * a1, a1 * a1.H]
even_comm = all(expand(p * q - q * p) == zeros(4, 4) for p in even0 for q in even1)
rec('X7', sign_img == -E01 and phase_img == I * E01 and entries == {0, 1} and comm == Zm and anti and even_comm,
    'Z E_01 Z = -E_01, phase map gives i E_01; permutation transports of E_01 x 1 have entries in {0, 1}; [E_01, E_10] = diag(1, -1); JW copies anticommute, even parts commute',
    'transport entries %s' % sorted(entries, key=str))

print("SUMMARY %d/%d CONFIRMED" % (sum(R), len(R)))
print("INDEP-E2-FIXED" if all(R) else "INDEP-E2-MISMATCH")
