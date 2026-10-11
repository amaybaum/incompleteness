"""E16 probe a -- the pair level on the chart-4 tokens Omega_4, Omega_star, Omega_cs: the pair carrier, the candidate
cones, the replacement of cnot (a native gate of the token), and product-form self-duality.  (exact: integers and
Fractions; no floating point)

S0 (written 2026-10-11T03:31Z by `date -u`, before run 1): NOTES-E16 S0 (A1), (A4) and the predictions there.

SETTING (kernel vocabulary at L).  A token body Omega in R^d; the pair carrier W d = tables w[mu][nu] over the
homogenized index 0..d (CompositeDimension.lean:97); actC N, actT N apply H = homMap N = 1 (+) N to the control and the
target index (:201, :198).  A replacement of cnot for the token is a native gate NativeGate Omega z N G (:218, defined for
every Omega), N a NOT of Omega (IsNot, :210).  The candidate cones of the pair: K_min = the cone of products, K_max =
maxCone Omega (:186), and, under product-form self-duality, K = K^{*(M (x) M)}.  The three tokens (chart dimension 4):
Omega_4 = {(x, s) : |x|^4 + s^4 <= 1} (NOTES-E2, EqvOmega4), Omega_star = {(X, S) : |X|^3 <= (1 + S)(1 - S)^2} and
Omega_cs = {(X, S) : |X| <= F(1 + S, 1 - S)} (NOTES-E13).  Each body's membership depends on its point only through
|x|^2 (resp. |X|^2) and the last coordinate.  Each token's drive (EqvOmega4's omega4Drive; E13's extension of
ball3Drive by S -> S) has the NOT N = flow(pi) = diag(-1, -1, 1, 1) and the corner axis z = e_0.

CHECKS.
 Gate -- the control relation relC (NOTES-E16 (A1)):
  G1  the tokens' NOT: N = diag(-1, -1, 1, 1) is the flow at t = pi of rotFun4 (parsed from research/equivalence/lean/
      EqvOmega4.lean, the lines of rotFun4_apply); N is an involution, N z = -z for the unit z = e_0, and N preserves
      |x|^2 and the last coordinate (N^T diag(1,1,1,0) N = diag(1,1,1,0), N e_3 = e_3): IsNot for each of the three
      bodies.
  G2  on W 4, the 25 x 25 matrices of actC N and actT N are built entry by entry from the definitions; tr(actC N) = 5,
      tr(actC N o actT N) = 1 = (tr H)^2 with tr H = 1; since 5 != 1 the two maps are not similar, so no invertible G
      satisfies relC with this N: none of the three tokens carries a native gate with its drive's NOT.
  G3  every NOT of chart dimension 4: for the 15 non-identity diagonal sign involutions of R^4 (every linear involution
      is diagonalizable with eigenvalues +-1 and the count reads only the trace), 5 tr H != (tr H)^2 on the built
      matrices: no body of chart dimension 4, eball 4 included, carries an invertible gate with relC.
  G4  for d = 1 .. 6 and every number m = 1 .. d of eigenvalues -1 of a diagonal NOT, the identity (d + 1) tr H =
      (tr H)^2 holds on the built matrices exactly when m = (d + 1)/2, which requires d odd.
  C1  positive control d = 3: the parsed kernel cnot with nflip satisfies relC and relT on all 16 basis tables; tr H = 0.
  C2  positive controls d = 1 and d = 5: the kernel's cnot1 (cnot1Fun w mu nu = w (mu + nu) nu, with neg1) and
      ODD-CHAR-1's gRev 2 (sgate (oddK 2) Fin.rev, with nK 2 = diagSign (cK 2)), their definitions parsed, satisfy relC
      on all basis tables; tr H = 0 for both.
  C3  negative control d = 3: refl3 = diag(1, 1, -1) and negId3 = -1 (ParityNot.lean:307, :310) have tr H = 2 and -2,
      so the identity fails (in agreement with the landed not_gateRel_refl3, not_gateRel_negId3).
 Product-form self-duality (NOTES-E16 (A4)):
  S1  Omega_4: y = (5/6, 0, 0, 5/6) lies in Omega_4 (|y|_4^4 = 1250/1296) and y . y = 25/18 > 1, so the cone points
      (1, y) and (1, -y) pair 1 - 25/18 < 0 for the Euclidean form: C(Omega_4) is not self-positive for I.  Axis data:
      the support of Omega_4 in the directions e_0 and e_3 is 1, attained at (1, 0, 0, 0) and (0, 0, 0, 1), and its
      sections by the two axes are [-1, 1]; so (written step) a self-dualizing form diag(a, b I, c) must have b = c = a,
      and a I fails by the witness.  Flat directions (the written step that Aut(C(Omega_4)) is compact modulo scalars,
      so that any self-dualizing form is Aut-invariant): with F = (x.x)^2 + s^4, the second derivative of F along e_3 is
      0 at (e_0, 0) and along e_0 is 0 at (0, 1), while the Hessian of F at (1/2, 1/2, 0, 1/2) is positive definite.
  S2  control: eball 4 (the Euclidean unit 4-ball) is self-positive for I on the same test -- for every pair of the
      sample points of S1 scaled into the ball the pairing 1 + p.q... is nonnegative (Cauchy-Schwarz instance).
  S3  Omega_star (M = diag(1/3, 2/3, 1, 1, 1) in (u, v, X), u = T + S, v = T - S; E13): (i) self-positivity on a grid of
      exact cone points ((X.X)^3 <= (u v^2)^2, u, v >= 0): every pairing <z, w>_M >= 0; (ii) R : X -> -X preserves the
      cone (it fixes u, v and |X|); (iii) omega_Phi = M^-1 (the table sum_i b_i (x) b_i over an M-orthonormal basis)
      satisfies <omega_Phi, (M a) (x) (M b)> = <a, b>_M identically (so omega_Phi is in K_max = maxCone, effects being
      M C by E13's self-duality), and the bilinear form phi(x, y) = x^T M R y, nonnegative on the products, gives
      phi(omega_Phi) = tr R = -1 < 0: omega_Phi is in K_max and not in K_min.
  S4  Omega_cs (M = diag(4/5, 1/5, 1, 1, 1) in (u, v, X); E13): (ii) and (iii) as in S3 (self-positivity is E13b's
      [X] + [W] and is not re-run here).
COUNTERCONTROLS (each must fail as stated).
  XG1  "relT alone excludes chart dimension 4": G = id satisfies relT with the tokens' N on all 25 basis tables.
  XG2  "G = id satisfies relC with the tokens' N" -- fails on a basis table.
  XS1  "C(Omega_4) is self-positive for I" -- fails by S1's witness pair.
  XS2  "omega_Phi of Omega_star lies in the product cone K_min" -- fails: the form phi, nonnegative on products, pairs -1.
DECISION RULE (fixed before run 1).  VERDICT E16A-CHART4-PAIR-LEVEL-SEPARATED iff G1-G4, C1-C3 and S1-S4 print PASS, no
FAIL is printed, XG1, XG2, XS1 and XS2 each print "COUNTER ... fails as stated", and the last line before the verdict is
"checks: 11, failures: 0".  Otherwise "VERDICT NOT RENDERED" with the failing items.  The verdict says: no native gate
exists on any body of chart dimension 4 (relC alone excludes it), and product-form pair self-duality with the products
and the K2 bound excludes Omega_4 and not Omega_star or Omega_cs (whose cones K_min and K_max differ).  It says nothing
about odd chart dimension >= 5, about positivity of gates, or about invariance of a self-dual composite under a drive.
"""
import itertools
import re
import sys
from fractions import Fraction as Fr

KERNEL = '../../../verification/lean-mathlib/OIBridge/'
OMEGA4 = '../lean/EqvOmega4.lean'
RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''), flush=True)


def src(f):
    return open(f, encoding='utf-8').read()


# ------------------------------------------------------------------ W d tables and the two actions
def basis(d, p, q):
    return [[Fr(1) if (a, b) == (p, q) else Fr(0) for b in range(d + 1)] for a in range(d + 1)]


def homH(N):
    """homMap N = 1 (+) N as a (d+1) x (d+1) matrix"""
    d = len(N)
    return [[Fr(1) if (i, j) == (0, 0) else Fr(0) for j in range(d + 1)] if i == 0 else
            [Fr(0)] + [Fr(N[i - 1][j - 1]) for j in range(1, d + 1)] for i in range(d + 1)]


def actC(H, w):
    n = len(w)
    return [[sum(H[m][k] * w[k][v] for k in range(n)) for v in range(n)] for m in range(n)]


def actT(H, w):
    n = len(w)
    return [[sum(H[v][k] * w[m][k] for k in range(n)) for v in range(n)] for m in range(n)]


def matrix_of(f, d):
    """the (d+1)^2 x (d+1)^2 matrix of a linear map f of W d, column (p, q) = f(basis p q)"""
    n = d + 1
    cols = {}
    for p in range(n):
        for q in range(n):
            cols[(p, q)] = f(basis(d, p, q))
    return [[cols[(p, q)][m][v] for p in range(n) for q in range(n)] for m in range(n) for v in range(n)]


def tr(A):
    return sum(A[i][i] for i in range(len(A)))


def diag_sign(signs):
    d = len(signs)
    return [[Fr(signs[i]) if i == j else Fr(0) for j in range(d)] for i in range(d)]


def trace_pair(N):
    d = len(N)
    H = homH(N)
    tC = tr(matrix_of(lambda w: actC(H, w), d))
    tCT = tr(matrix_of(lambda w: actC(H, actT(H, w)), d))
    return tC, tCT, tr(H)


# ------------------------------------------------------------------ G1: the tokens' NOT, parsed from EqvOmega4
s4 = src(OMEGA4)
rot_ok = all(t in s4 for t in ('rotFun4 t v 0 = Real.cos t * v 0 - Real.sin t * v 1 ∧',
                               'rotFun4 t v 1 = Real.sin t * v 0 + Real.cos t * v 1 ∧ rotFun4 t v 2 = v 2 ∧',
                               'rotFun4 t v 3 = v 3'))
c_pi, s_pi = -1, 0                                   # cos pi, sin pi
N4 = [[c_pi, -s_pi, 0, 0], [s_pi, c_pi, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
N4 = [[Fr(x) for x in row] for row in N4]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def tp(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


I4 = [[Fr(1) if i == j else Fr(0) for j in range(4)] for i in range(4)]
Q = [[Fr(1) if (i == j and i < 3) else Fr(0) for j in range(4)] for i in range(4)]
z0 = [Fr(1), Fr(0), Fr(0), Fr(0)]
e3 = [Fr(0), Fr(0), Fr(0), Fr(1)]
Nz = [sum(N4[i][j] * z0[j] for j in range(4)) for i in range(4)]
Ne3 = [sum(N4[i][j] * e3[j] for j in range(4)) for i in range(4)]
ok_g1 = (rot_ok and mm(N4, N4) == I4 and Nz == [-x for x in z0] and sum(x * x for x in z0) == 1
         and mm(mm(tp(N4), Q), N4) == Q and Ne3 == e3)
check('G1', ok_g1, 'rotFun4_apply parsed: %s; N = flow(pi) = diag(-1, -1, 1, 1): involution, flips the unit e_0, preserves '
      '|x|^2 and the last coordinate (IsNot for Omega_4, Omega_star, Omega_cs)' % rot_ok)

tC, tCT, tH = trace_pair(N4)
check('G2', tC == 5 and tCT == 1 and tH == 1 and 5 * tH != tH * tH,
      'on W 4: tr(actC N) = %s = 5 tr H, tr(actC N o actT N) = %s = (tr H)^2, tr H = %s; not similar, no invertible G with '
      'relC' % (tC, tCT, tH))

ok_g3 = True
n_inv = 0
for signs in itertools.product([1, -1], repeat=4):
    if all(s == 1 for s in signs):
        continue
    n_inv += 1
    a, b, h = trace_pair(diag_sign(signs))
    if not (a == 5 * h and b == h * h and a != b):
        ok_g3 = False
check('G3', ok_g3 and n_inv == 15, 'all %d non-identity diagonal involutions of R^4: (d+1) tr H != (tr H)^2' % n_inv)

table = []
ok_g4 = True
for d in range(1, 7):
    for m in range(1, d + 1):
        a, b, h = trace_pair(diag_sign([1] * (d - m) + [-1] * m))
        holds = (a == b)
        table.append((d, m, h, holds))
        if holds != (2 * m == d + 1) or a != (d + 1) * h or b != h * h:
            ok_g4 = False
odd_only = all((not t[3]) or (t[0] % 2 == 1) for t in table)
check('G4', ok_g4 and odd_only,
      'd = 1..6: the identity holds exactly for %s' % [(t[0], t[1]) for t in table if t[3]])


# ------------------------------------------------------------------ C1-C3: kernel controls
def parse_table(text, name):
    mt = re.search(r'def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n)+)' % name, text)
    entries = re.findall(r'(\d), (\d) => (\d)', mt.group(1))
    return {(int(a), int(b)): int(c) for a, b, c in entries}


def parse_sgn(text):
    mt = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1', text)
    neg = {(int(mt.group(1)), int(mt.group(2))), (int(mt.group(3)), int(mt.group(4)))}
    return {(a, b): (-1 if (a, b) in neg else 1) for a in range(4) for b in range(4)}


cd = src(KERNEL + 'CompositeDimension.lean')
PC, PT, SGN = parse_table(cd, 'pc'), parse_table(cd, 'pt'), parse_sgn(cd)
cnot3 = lambda w: [[SGN[(m, n)] * w[PC[(m, n)]][PT[(m, n)]] for n in range(4)] for m in range(4)]
nflip = diag_sign([1, -1, -1])


def rel_ok(G, N, d, which):
    H = homH(N)
    for p in range(d + 1):
        for q in range(d + 1):
            w = basis(d, p, q)
            if which == 'C' and actC(H, G(actC(H, w))) != actT(H, G(w)):
                return False
            if which == 'T' and actT(H, G(actT(H, w))) != G(w):
                return False
    return True


ok_c1 = rel_ok(cnot3, nflip, 3, 'C') and rel_ok(cnot3, nflip, 3, 'T') and trace_pair(nflip)[2] == 0
check('C1', ok_c1, 'd = 3: kernel cnot with nflip satisfies relC and relT on 16 basis tables; tr H = 0')

cnot1_ok = 'def cnot1Fun (ω : W 1) : W 1 := fun μ ν => ω (μ + ν) ν' in cd and \
    'def neg1 : (Fin 1 → ℝ) →ₗ[ℝ] (Fin 1 → ℝ) := -LinearMap.id' in cd
cnot1 = lambda w: [[w[(m + n) % 2][n] for n in range(2)] for m in range(2)]
neg1 = diag_sign([-1])
oc = src(KERNEL + 'OddChar.lean')
pn = src(KERNEL + 'ParityNot.lean')
grev_ok = all(t in oc for t in ('def oddK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) : Bool := decide (k < (μ : ℕ))',
                                'def cK (k : ℕ) (j : Fin (2 * k + 1)) : ℝ := if oddK k j.succ then -1 else 1',
                                'def nK (k : ℕ) : (Fin (2 * k + 1) → ℝ) →ₗ[ℝ] (Fin (2 * k + 1) → ℝ) := diagSign (cK k)',
                                'def gRev (k : ℕ) : W (2 * k + 1) ≃ₗ[ℝ] W (2 * k + 1) := sgateEquiv (oddK k) Fin.rev Fin.rev_rev')) \
    and 'fun μ ν => if odd ν then ω (p μ) ν else ω μ ν' in pn
k = 2
oddK = lambda mu: k < mu
nK2 = diag_sign([-1 if oddK(j + 1) else 1 for j in range(2 * k + 1)])
gRev2 = lambda w: [[w[(2 * k + 1) - m][n] if oddK(n) else w[m][n] for n in range(2 * k + 2)] for m in range(2 * k + 2)]
ok_c2 = (cnot1_ok and grev_ok and rel_ok(cnot1, neg1, 1, 'C') and trace_pair(neg1)[2] == 0
         and rel_ok(gRev2, nK2, 5, 'C') and rel_ok(gRev2, nK2, 5, 'T') and trace_pair(nK2)[2] == 0)
check('C2', ok_c2, 'd = 1: cnot1 with neg1 satisfies relC; d = 5: gRev 2 with nK 2 = diag%s satisfies relC and relT; '
      'tr H = 0 for both (definitions parsed: %s, %s)' % ([int(nK2[i][i]) for i in range(5)], cnot1_ok, grev_ok))

refl3 = diag_sign([1, 1, -1])
negId3 = diag_sign([-1, -1, -1])
r1, r2, r3 = trace_pair(refl3)
n1, n2, n3 = trace_pair(negId3)
ok_c3 = ('def refl3 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) := diagSign ![1, 1, -1]' in pn
         and 'def negId3 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) := diagSign ![-1, -1, -1]' in pn
         and r3 == 2 and n3 == -2 and r1 != r2 and n1 != n2)
check('C3', ok_c3, 'd = 3: refl3 tr H = %s (%s vs %s), negId3 tr H = %s (%s vs %s): no invertible G with relC'
      % (r3, r1, r2, n3, n1, n2))


# ------------------------------------------------------------------ S1, S2: Omega_4 is not self-positive for I; the ball is
def omega4_mem(p):
    x2 = p[0] ** 2 + p[1] ** 2 + p[2] ** 2
    return x2 * x2 + p[3] ** 4 <= 1


y = [Fr(5, 6), Fr(0), Fr(0), Fr(5, 6)]
yy = sum(t * t for t in y)
pair_neg = 1 - yy                                    # <(1, y), (1, -y)> for the Euclidean form
supp_ok = omega4_mem([Fr(1), 0, 0, 0]) and omega4_mem([0, 0, 0, Fr(1)]) and \
    not omega4_mem([Fr(1) + Fr(1, 1000), 0, 0, 0]) and not omega4_mem([0, 0, 0, Fr(1) + Fr(1, 1000)])
# second derivatives of F = (x.x)^2 + s^4: d2F/ds2 = 12 s^2; d2F/dxi dxj = 4 (x.x) delta_ij + 8 x_i x_j
d2s_at_e0 = 12 * Fr(0) ** 2
d2x0_at_s1 = 4 * Fr(0) + 8 * Fr(0) * Fr(0)
xp = [Fr(1, 2), Fr(1, 2), Fr(0)]
sp_ = Fr(1, 2)
Hx = [[4 * sum(t * t for t in xp) * (1 if i == j else 0) + 8 * xp[i] * xp[j] for j in range(3)] for i in range(3)]
Hs = 12 * sp_ ** 2
minors = [Hx[0][0], Hx[0][0] * Hx[1][1] - Hx[0][1] * Hx[1][0],
          Hx[0][0] * (Hx[1][1] * Hx[2][2] - Hx[1][2] * Hx[2][1]) - Hx[0][1] * (Hx[1][0] * Hx[2][2] - Hx[1][2] * Hx[2][0])
          + Hx[0][2] * (Hx[1][0] * Hx[2][1] - Hx[1][1] * Hx[2][0])]
hess_pd = all(mi > 0 for mi in minors) and Hs > 0
ok_s1 = omega4_mem(y) and yy == Fr(25, 18) and pair_neg < 0 and supp_ok and d2s_at_e0 == 0 and d2x0_at_s1 == 0 and hess_pd
check('S1', ok_s1, 'y = (5/6, 0, 0, 5/6) in Omega_4, y.y = %s, <(1, y), (1, -y)> = %s < 0; axis support 1; flat directions '
      'at (e_0, 0) and (0, 1); Hessian positive definite at (1/2, 1/2, 0, 1/2)' % (yy, pair_neg))

samples = [[Fr(1), 0, 0, 0], [0, 0, 0, Fr(1)], [Fr(5, 6), 0, 0, Fr(5, 6)], [Fr(-5, 6), 0, 0, Fr(-5, 6)],
           [Fr(3, 5), Fr(4, 5), 0, 0], [Fr(1, 2), Fr(-1, 2), Fr(1, 2), Fr(1, 2)], [0, Fr(-3, 5), 0, Fr(4, 5)]]
ball_pts = []
for p in samples:
    n2 = sum(Fr(t) ** 2 for t in p)
    c = Fr(1) if n2 <= 1 else Fr(1, 2)
    while c * c * n2 > 1:
        c = c / 2
    ball_pts.append([c * Fr(t) for t in p])
ball_selfpos = all(1 + sum(p[i] * q[i] for i in range(4)) >= 0 for p in ball_pts for q in ball_pts) and \
    all(sum(t * t for t in p) <= 1 for p in ball_pts)
check('S2', ball_selfpos, 'eball 4: every pairing 1 + p.q of %d sample points scaled into the ball is >= 0' % len(ball_pts))


# ------------------------------------------------------------------ S3, S4: Omega_star and Omega_cs, K_min != K_max
def pc_mem(z):                                   # power cone in (u, v, X): u, v >= 0, (X.X)^3 <= (u v^2)^2
    u, v, X = z[0], z[1], z[2:]
    xx = sum(t * t for t in X)
    return u >= 0 and v >= 0 and xx ** 3 <= (u * v * v) ** 2


def form(M, a, b):
    return sum(M[i] * a[i] * b[i] for i in range(5))


Mstar = [Fr(1, 3), Fr(2, 3), Fr(1), Fr(1), Fr(1)]
grid = []
for u in (Fr(1), Fr(2), Fr(1, 2), Fr(0)):
    for v in (Fr(1), Fr(3), Fr(1, 3), Fr(0)):
        for X in ([0, 0, 0], [Fr(1, 2), 0, 0], [0, Fr(-1, 3), Fr(1, 4)], [Fr(-1), Fr(1), 0], [Fr(1, 5), Fr(1, 5), Fr(-1, 5)]):
            z = [u, v] + [Fr(t) for t in X]
            if pc_mem(z):
                grid.append(z)
selfpos_star = all(form(Mstar, a, b) >= 0 for a in grid for b in grid)
R = [Fr(1), Fr(1), Fr(-1), Fr(-1), Fr(-1)]
R_pres = all(pc_mem([R[i] * z[i] for i in range(5)]) for z in grid)


def kmin_kmax_witness(M):
    """omega_Phi = M^-1 (diagonal); <omega_Phi, (M a) (x) (M b)> = sum_i a_i M_i b_i; phi = M R; phi(omega_Phi) = tr R"""
    import random
    rng = random.Random(16)
    ok_ident = True
    for _ in range(20):
        a = [Fr(rng.randint(-9, 9), rng.randint(1, 9)) for _ in range(5)]
        b = [Fr(rng.randint(-9, 9), rng.randint(1, 9)) for _ in range(5)]
        omega = [[(1 / M[i]) if i == j else Fr(0) for j in range(5)] for i in range(5)]
        lhs = sum(omega[i][j] * (M[i] * a[i]) * (M[j] * b[j]) for i in range(5) for j in range(5))
        if lhs != form(M, a, b):
            ok_ident = False
    phi_omega = sum((1 / M[i]) * M[i] * R[i] for i in range(5))
    return ok_ident, phi_omega


id_star, phi_star = kmin_kmax_witness(Mstar)
check('S3', len(grid) >= 30 and selfpos_star and R_pres and id_star and phi_star == -1,
      'Omega_star: %d exact cone points pairwise >= 0 for M; R preserves the cone; <omega_Phi, Ma (x) Mb> = <a, b>_M; '
      'phi(omega_Phi) = tr R = %s' % (len(grid), phi_star))
Mcs = [Fr(4, 5), Fr(1, 5), Fr(1), Fr(1), Fr(1)]
id_cs, phi_cs = kmin_kmax_witness(Mcs)
check('S4', id_cs and phi_cs == -1, 'Omega_cs: <omega_Phi, Ma (x) Mb> = <a, b>_M; phi(omega_Phi) = tr R = %s; R fixes u, v '
      'and |X|, so it preserves the cone' % phi_cs)

# ------------------------------------------------------------------ countercontrols
counters = []
Gid = lambda w: [row[:] for row in w]
counters.append(('XG1', rel_ok(Gid, N4, 4, 'T'), 'G = id satisfies relT with the tokens\' N on all 25 basis tables'))
counters.append(('XG2', not rel_ok(Gid, N4, 4, 'C'), 'G = id fails relC with the tokens\' N'))
counters.append(('XS1', pair_neg < 0, 'two points of C(Omega_4) pair %s for the Euclidean form' % pair_neg))
counters.append(('XS2', phi_star < 0, 'a form nonnegative on the products of Omega_star pairs %s with omega_Phi' % phi_star))
for name, failed, detail in counters:
    print(('COUNTER %s fails as stated' % name) if failed else ('COUNTER %s DID NOT FAIL' % name), '--', detail, flush=True)

nfail = sum(1 for _, ok in RESULTS if not ok)
print('checks: %d, failures: %d' % (len(RESULTS), nfail), flush=True)
if nfail == 0 and len(RESULTS) == 11 and all(c[1] for c in counters):
    print('VERDICT E16A-CHART4-PAIR-LEVEL-SEPARATED')
else:
    print('VERDICT NOT RENDERED -- failing: %s' % ([n for n, ok in RESULTS if not ok] + [c[0] for c in counters if not c[1]]))
sys.exit(0)
