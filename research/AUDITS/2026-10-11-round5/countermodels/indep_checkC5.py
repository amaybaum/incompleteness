#!/usr/bin/env python3
"""indep_checkC5.py -- coordinator's independent check of research/countermodels, round 5, node C23 (head c9ac75bd).

Reads nothing the thread wrote: no import from and no file read under research/countermodels.  Every object is rebuilt
from the definitions.  Basis |00>, |01>, |10>, |11> (control first; indices 0..3); CNOT = the permutation (2 3);
X_B = 1 (x) X = (0 1)(2 3); R_B(t) = diag(1, e^{it}, 1, e^{it}); D(u, v) = diag(1, uv, u, v) (|u| = |v| = 1);
G_n = <CNOT, X_B, R_B(2 pi / 2^n)>, G_T = closure of the union.  Defects d_h = I - c P_h, P_h = h h^+ / |h|^2;
balanced defects I - c P_h - (2 - c) P_k (k orthogonal to h).  The engine's local condition is taken from the statement
of `selfDual_of_local` (research/countermodels/lean/CmSprime.lean:705, read as a statement at the thread's round-4 head
644bf0a1): for j, k with k = j or pr(d_k, d_j) > 0, every u with u^+ d_j u < 0 and every x != 0 with u^+ x = 0 give
x^+ d_k x > 0.  H1 for a G_T-invariant defect set (products lie in K, K = K*): every defect pairs >= 0 with every
product, i.e. for d = I - c P_h on the whole orbit, 1 - 4 D <= (2/c - 1)^2 with D = |det Psi|^2/|h|^4, Psi = [[h0, h1],
[h2, h3]].

Exact arithmetic: Fractions (Gaussian rationals, own class) and sympy for identities.  Floats only in Z3(e), labelled
[N] (numerical; not a certification).

Decision rule (fixed before run 1): VERDICT INDEP-C5-FIXED iff Z1-Z5 all PASS and CC1-CC5 all evaluate False;
otherwise VERDICT INDEP-C5-FAILED <items>.

Z1 group.  (a) R_B(t) = D(1, w), CNOT D(u, v) CNOT = D(v, u), X_B D(u, v) X_B = uv D(1/u, 1/v), symbolically.
   (b) G_1 and G_2 enumerated exactly modulo phase: orders 16 and 64; every element monomial, permutation in
   V4 = {e, (23), (01)(23), (01)}, phases with phi0 phi1 = phi2 phi3; the diagonal part is {D(u, v) : u, v in mu_{2^n}}.
Z2 Lemma C23-1.  (a) <h|D(u, v) X_B h> = beta + uv conj(beta) + u alpha + v conj(alpha), alpha = conj(h2) h3,
   beta = conj(h0) h1, in real coordinates; (b) |beta + u alpha|^2 - |conj(alpha) + u conj(beta)|^2 =
   (|u|^2 - 1)(|alpha|^2 - |beta|^2) in real coordinates; (c) exhaustive: every nonzero h with components in
   {-1, 0, 1} + i{-1, 0, 1} (6560 vectors) gets a unimodular Gaussian-rational (u, v) with <h|D(u, v) X_B h> = 0 from
   the five-class formulas, and the rank r of the orthogonalizing family {D(u, v) X_B h} (eight solutions) is 3 on every
   class-(i) vector, 2 on every class-(ii) vector and on every class-(iii)/(iv) vector with exactly one zero coordinate;
   (d) own seeds, one per class.
Z3 the c = 2 corner for G_T.  (a) det Psi(D(u, v)h) = v(h0h3 - u^2 h1h2) and det Psi(CNOT D(u, v)h) = u(h0h2 - v^2 h1h3),
   symbolically; for (h0, 0, 0, h3) and (0, h1, h2, 0) the CNOT image has det Psi = 0.  (b) the four sum-of-squares
   identities for S/2 -+ x, S/2 -+ y (S = sum a_i^2, x = a0a3 - a1a2, y = a0a2 - a1a3, moduli a_i >= 0), and
   {|x| = S/2, |y| = S/2, a >= 0} has the single solution a = 0: no G_T-orbit is maximally entangled throughout.
   (c) every state of C1' = {|00> + w|11>}, C2' = {|01> + w|10>} (w at ten rational points) is maximally entangled, its
   CNOT image is a product, and the c = 2 defect of that image pairs -1 with it: the Bell circles are not H1-admissible
   G_T-orbits at c = 2.  (d) x + y = (a0 - a1)(a2 + a3), x - y = (a0 + a1)(a3 - a2) symbolically, hence
   min(|x|, |y|) <= S/(2 sqrt 2) and D_min <= 1/8 [W]; attained exactly at a = (sqrt2/2, 0, 1/2, 1/2); H1 on a
   G_T-orbit then forces c <= 2/(1 + 1/sqrt 2) = 4 - 2 sqrt 2 (exact).  (e) [N] 200000 random unit moduli vectors:
   max D_min <= 1/8 + 1e-12.
Z4 Theorem C23-2(a), the rank-one witness.  (a) <y, d_k> = (c* - c_k)(1 + lam) + c_k s'(1 + lam c*) + c_k r identically
   (lam = (c* - 1)/(4 - 2c*), s = |<h^|k^>|^2, s' = |<gh^|k^>|^2, r = 1 - s - s'); (b) <d_k, d_h> - (4 - 2c*) =
   (c* - c_k) + c_k c* s identically; (c) own instance: class-(i) seed h = (1, 2i, 3, 1), D_min = 1/225, c* = 1001/1000
   with H1; g = D(u, v) X_B with gh orthogonal to h; y = P_h + lam d_gh: <y, d_h> = 0, (gh)^+ y (gh) < 0, and on 200
   orbit samples (the c* orbit and the orbit of (2, 1, 1, 3) at c = 2001/2000; 25 torus points x 4 cosets each):
   <y, d> >= 0 and equal to (a), <d, d_h> > 0, H1 at every sample.
Z5 Theorem C23-3, the balanced route.  (a) <d, g d g^+> = c^2|<h^|gh^>|^2 + c(2 - c)(|<h^|gk^>|^2 + |<k^|gh^>|^2) +
   (2 - c)^2 |<k^|gk^>|^2 on exact instances; (b) with gh orthogonal to h and pr(d, gdg^+) > 0 the local condition fails at
   u = h, x = gh (x^+ (g d g^+) x = h^+ d h < 0), exact instance; (c) own seeds (i) (1, 2i, 3, 1): {k : k orthogonal to
   the eight partners and to h} = {0}; (ii) (1, 2, 2, 1), (iii) (1, 1+i, 0, 2), (iv) (2, 0, 1, i): that space is a line
   spanned by k0; (d) for each r = 2 seed at c = 3/2: <d, g d g^+> = 0 on the eight orthogonalizing g, and an exact
   tightness instance found by a fixed search: U in T^2 near 1, u = h + b k0 with u^+ d u < 0, x = k0 - (<u|k0>/<u|u>) u
   with x^+ d x > 0, pr(d, U d U^+) > 0 and x^+ (U d U^+) x < 0 (the local condition fails at (d, U d U^+)).
Countercontrols (each must evaluate False):
CC1 1 (x) [[3/5, -4/5], [4/5, 3/5]] passes the G_T membership test.
CC2 for the class-(i) seed (1, 2i, 3, 1), (u, v) = (1, 1) is orthogonalizing.
CC3 under T^2 x| <X_B> alone (no CNOT) some sampled orbit point of |00> + |11> is not maximally entangled.
CC4 the witness built at c2 = 2001/2000 < c* pairs >= 0 with the c* copy of d_h.
CC5 for each r = 2 seed, a vector k orthogonal to h and not proportional to k0 has zero pairing on the orthogonalizing family.

Run from this directory:  python3 -I -B indep_checkC5.py > indep_checkC5.out 2> indep_checkC5.err
"""
import itertools
import random
from fractions import Fraction as F

import sympy as sp


# ---------------------------------------------------------------- Gaussian rationals
class GQ:
    __slots__ = ('re', 'im')

    def __init__(self, re=0, im=0):
        self.re = F(re)
        self.im = F(im)

    def __add__(self, o):
        o = gq(o)
        return GQ(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = gq(o)
        return GQ(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        o = gq(o)
        return GQ(o.re - self.re, o.im - self.im)

    def __mul__(self, o):
        o = gq(o)
        return GQ(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __neg__(self):
        return GQ(-self.re, -self.im)

    def conj(self):
        return GQ(self.re, -self.im)

    def n2(self):
        return self.re * self.re + self.im * self.im

    def __truediv__(self, o):
        o = gq(o)
        d = o.n2()
        return self * GQ(o.re / d, -o.im / d)

    def __eq__(self, o):
        o = gq(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def zero(self):
        return self.re == 0 and self.im == 0

    def __repr__(self):
        if self.im == 0:
            return str(self.re)
        if self.re == 0:
            return f'{self.im}i'
        return f'({self.re}{"+" if self.im > 0 else "-"}{abs(self.im)}i)'


def gq(x):
    return x if isinstance(x, GQ) else GQ(x, 0)


ZERO, ONE, I1 = GQ(0), GQ(1), GQ(0, 1)


def vec(*xs):
    return [gq(x) for x in xs]


def inner(a, b):
    s = GQ(0)
    for x, y in zip(a, b):
        s = s + x.conj() * y
    return s


def n2v(a):
    return sum((x.n2() for x in a), F(0))


def matvec(M, v):
    return [sum((M[i][j] * v[j] for j in range(4)), GQ(0)) for i in range(4)]


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(4)), GQ(0)) for j in range(4)] for i in range(4)]


def dag(A):
    return [[A[j][i].conj() for j in range(4)] for i in range(4)]


def eye():
    return [[ONE if i == j else ZERO for j in range(4)] for i in range(4)]


def proj(h):
    n = n2v(h)
    return [[h[i] * h[j].conj() / n for j in range(4)] for i in range(4)]


def lin(*terms):  # sum of coeff * matrix
    out = [[GQ(0) for _ in range(4)] for _ in range(4)]
    for c, M in terms:
        for i in range(4):
            for j in range(4):
                out[i][j] = out[i][j] + gq(c) * M[i][j]
    return out


def defect(c, h):
    return lin((1, eye()), (-c, proj(h)))


def defect2(c, h, k):
    return lin((1, eye()), (-c, proj(h)), (-(2 - F(c)), proj(k)))


def pr(A, B):  # Re tr(A B)
    t = GQ(0)
    for i in range(4):
        for k in range(4):
            t = t + A[i][k] * B[k][i]
    return t.re


def qf(A, x):
    return inner(x, matvec(A, x)).re


def perm(p):  # matrix sending e_j to e_{p[j]}
    M = [[ZERO for _ in range(4)] for _ in range(4)]
    for j in range(4):
        M[p[j]][j] = ONE
    return M


CNOT = perm([0, 1, 3, 2])
XB = perm([1, 0, 3, 2])


def Dm(u, v):
    u, v = gq(u), gq(v)
    M = [[ZERO for _ in range(4)] for _ in range(4)]
    for i, x in enumerate([ONE, u * v, u, v]):
        M[i][i] = x
    return M


def conjugate_by(g, A):
    return matmul(matmul(g, A), dag(g))


def det2(h):
    return h[0] * h[3] - h[1] * h[2]


def rp(t):  # rational point on the unit circle; t = None gives -1
    if t is None:
        return GQ(-1)
    t = F(t)
    return GQ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


U_LIST = [rp(0), rp(None), rp(1), rp(-1), rp(F(1, 2)), rp(2), rp(F(1, 3)), rp(F(-1, 2)), rp(3), rp(F(-1, 3)),
          rp(F(2, 3)), rp(F(-3, 2))]


def rank(rows):
    M = [list(r) for r in rows]
    rk, col, nr = 0, 0, len(M)
    while rk < nr and col < 4:
        piv = next((i for i in range(rk, nr) if not M[i][col].zero()), None)
        if piv is None:
            col += 1
            continue
        M[rk], M[piv] = M[piv], M[rk]
        p = M[rk][col]
        M[rk] = [x / p for x in M[rk]]
        for i in range(nr):
            if i != rk and not M[i][col].zero():
                f = M[i][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[rk])]
        rk += 1
        col += 1
    return rk


def nullspace(rows):
    """basis of {k in C^4 : sum_j rows[i][j] k_j = 0 for all i}"""
    M = [list(r) for r in rows]
    pivcols, rk, nr = [], 0, len(M)
    for col in range(4):
        piv = next((i for i in range(rk, nr) if not M[i][col].zero()), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        p = M[rk][col]
        M[rk] = [x / p for x in M[rk]]
        for i in range(nr):
            if i != rk and not M[i][col].zero():
                f = M[i][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[rk])]
        pivcols.append(col)
        rk += 1
    free = [c for c in range(4) if c not in pivcols]
    basis = []
    for fc in free:
        k = [GQ(0) for _ in range(4)]
        k[fc] = ONE
        for r, pc in enumerate(pivcols):
            k[pc] = -M[r][fc]
        basis.append(k)
    return basis


def orth_rows(vs):  # rows expressing <v|k> = 0
    return [[x.conj() for x in v] for v in vs]


RESULTS = {}


def check(name, ok, msg):
    RESULTS[name] = bool(ok)
    print(f'[{"PASS" if ok else "FAIL"}] {name}: {msg}', flush=True)


CCS = {}


def cc(name, val, msg):
    CCS[name] = bool(val)
    print(f'[CC] {name} = {bool(val)}: {msg}', flush=True)


# ---------------------------------------------------------------- Z1
u_, v_, w_ = sp.symbols('u v w', nonzero=True)


def sD(u, v):
    return sp.diag(1, u * v, u, v)


sC = sp.Matrix(4, 4, lambda i, j: 1 if [0, 1, 3, 2][j] == i else 0)
sX = sp.Matrix(4, 4, lambda i, j: 1 if [1, 0, 3, 2][j] == i else 0)
z1a = (sp.diag(1, w_, 1, w_) - sD(1, w_)).is_zero_matrix
z1a &= sp.simplify(sC * sD(u_, v_) * sC - sD(v_, u_)).is_zero_matrix
z1a &= sp.simplify(sX * sD(u_, v_) * sX - u_ * v_ * sD(1 / u_, 1 / v_)).is_zero_matrix


def membership(g):
    """G_T modulo phase: unitary, monomial with permutation in V4, phases phi0 phi1 = phi2 phi3"""
    if not all(x.zero() for x in [a - b for ra, rb in zip(matmul(g, dag(g)), eye()) for a, b in zip(ra, rb)]):
        return False
    sig = []
    for i in range(4):
        nz = [j for j in range(4) if not g[i][j].zero()]
        if len(nz) != 1:
            return False
        sig.append(nz[0])
    if tuple(sig) not in {(0, 1, 2, 3), (0, 1, 3, 2), (1, 0, 3, 2), (1, 0, 2, 3)}:
        return False
    ph = [g[i][sig[i]] for i in range(4)]
    return ph[0] * ph[1] == ph[2] * ph[3]


def normalize(g):
    j = next(j for j in range(4) if not g[0][j].zero())
    z = g[0][j]
    zc = z.conj() / z.n2()
    return tuple(tuple(x * zc for x in row) for row in g)


def enumerate_group(gens):
    start = normalize(eye())
    seen = {start}
    frontier = [start]
    while frontier:
        nxt = []
        for a in frontier:
            A = [list(r) for r in a]
            for G in gens:
                b = normalize(matmul(A, G))
                if b not in seen:
                    seen.add(b)
                    nxt.append(b)
        frontier = nxt
    return seen


z1b = True
msgs = []
for n, om in [(1, GQ(-1)), (2, I1)]:
    grp = enumerate_group([CNOT, XB, Dm(1, om)])
    allmem = all(membership([list(r) for r in g]) for g in grp)
    diag = [g for g in grp if all(g[i][j].zero() for i in range(4) for j in range(4) if i != j)]
    roots = {ONE, om} if n == 1 else {ONE, I1, GQ(-1), GQ(0, -1)}
    want = {normalize(Dm(a, b)) for a in roots for b in roots}
    ok = len(grp) == 4 ** (n + 1) and allmem and set(diag) == want and len(diag) == 4 ** n
    z1b &= ok
    msgs.append(f'G_{n}: order {len(grp)} mod phase, all pass membership {allmem}, diagonal part = D(mu_{2 ** n}^2) '
                f'({len(diag)}) {set(diag) == want}')
check('Z1', z1a and z1b, f'conjugation relations symbolic {z1a}; ' + '; '.join(msgs))
R345 = [[ONE, ZERO, ZERO, ZERO], [ZERO, ONE, ZERO, ZERO], [ZERO, ZERO, ONE, ZERO], [ZERO, ZERO, ZERO, ONE]]
r = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
for a in range(2):
    for b in range(2):
        for c in range(2):
            R345[2 * a + b][2 * a + c] = gq(r[b][c])
cc('CC1', membership(R345), '1 (x) R_345 accepted as an element of G_T')

# ---------------------------------------------------------------- Z2
xs = sp.symbols('x0:4', real=True)
ys = sp.symbols('y0:4', real=True)
ur, ui, vr, vi = sp.symbols('ur ui vr vi', real=True)
H = [xs[i] + sp.I * ys[i] for i in range(4)]
U, V = ur + sp.I * ui, vr + sp.I * vi
al, be = sp.conjugate(H[2]) * H[3], sp.conjugate(H[0]) * H[1]
gh_s = sD(U, V) * sX * sp.Matrix(H)
lhs = sum(sp.conjugate(H[i]) * gh_s[i] for i in range(4))
rhs = be + U * V * sp.conjugate(be) + U * al + V * sp.conjugate(al)
z2a = sp.expand(lhs - rhs) == 0
a1, a2, b1, b2 = sp.symbols('a1 a2 b1 b2', real=True)
A_, B_ = a1 + sp.I * a2, b1 + sp.I * b2
m1 = sp.expand((B_ + U * A_) * sp.conjugate(B_ + U * A_) - (sp.conjugate(A_) + U * sp.conjugate(B_)) * sp.conjugate(sp.conjugate(A_) + U * sp.conjugate(B_)))
m2 = sp.expand((U * sp.conjugate(U) - 1) * (A_ * sp.conjugate(A_) - B_ * sp.conjugate(B_)))
z2b = sp.expand(m1 - m2) == 0


def klass(h):
    alpha, beta = h[2].conj() * h[3], h[0].conj() * h[1]
    if not alpha.zero() and not beta.zero():
        return ('i' if alpha.n2() != beta.n2() else 'ii'), alpha, beta
    if alpha.zero() and not beta.zero():
        return 'iii', alpha, beta
    if beta.zero() and not alpha.zero():
        return 'iv', alpha, beta
    return 'v', alpha, beta


def solutions(h, want=8):
    """orthogonalizing (u, v) from the five-class formulas, at up to `want` values of u"""
    cl, alpha, beta = klass(h)
    out = []
    for u in U_LIST:
        if cl in ('i', 'ii'):
            den = alpha.conj() + u * beta.conj()
            if den.zero():
                continue
            v = -(beta + u * alpha) / den
        elif cl == 'iii':
            v = (-beta / beta.conj()) / u
        elif cl == 'iv':
            v = -(u * alpha) / alpha.conj()
        else:
            v = u
        out.append((u, v))
        if len(out) == want:
            break
    return cl, out


def gx(u, v):
    return matmul(Dm(u, v), XB)


comps = [GQ(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
counts, bad, rank_tab = {}, [], {}
for h in itertools.product(comps, repeat=4):
    h = list(h)
    if all(x.zero() for x in h):
        continue
    cl, sols = solutions(h)
    counts[cl] = counts.get(cl, 0) + 1
    good = len(sols) >= 1
    imgs = []
    for u, v in sols:
        g = gx(u, v)
        x = matvec(g, h)
        if not (u.n2() == 1 and v.n2() == 1 and inner(h, x).zero() and membership(g)):
            good = False
        imgs.append(x)
    if not good:
        bad.append(h)
    nz = sum(1 for x in h if x.zero())
    key = (cl, nz, rank(imgs))
    rank_tab[key] = rank_tab.get(key, 0) + 1
z2c_orth = not bad
z2c_rank = all(k[2] == 3 for k in rank_tab if k[0] == 'i') and all(k[2] == 2 for k in rank_tab if k[0] == 'ii') \
    and all(k[2] == 2 for k in rank_tab if k[0] in ('iii', 'iv') and k[1] == 1)
z2c_rank &= any(k[0] == 'i' for k in rank_tab) and any(k[0] == 'ii' for k in rank_tab)
tab = ', '.join(f'{k[0]}/{k[1]}z/r{k[2]}: {n}' for k, n in sorted(rank_tab.items()))
seeds = {'i': vec(1, GQ(0, 2), 3, 1), 'ii': vec(1, 2, 2, 1), 'iii': vec(1, GQ(1, 1), 0, 2), 'iv': vec(2, 0, 1, I1),
         'v': vec(1, 0, 0, 3)}
z2d, sd = True, []
for nm, h in seeds.items():
    cl, sols = solutions(h, 1)
    u, v = sols[0]
    ok = cl == nm and u.n2() == 1 and v.n2() == 1 and inner(h, matvec(gx(u, v), h)).zero()
    z2d &= ok
    sd.append(f'{nm}: (u, v) = ({u}, {v}) {ok}')
check('Z2', z2a and z2b and z2c_orth and z2c_rank and z2d,
      f'identity (real coordinates) {z2a}; modulus identity {z2b}; grid {sum(counts.values())} vectors, classes {dict(sorted(counts.items()))}, '
      f'orthogonalizing (u, v) found and verified for all: {z2c_orth}; rank table (class/zero coords/r: count) {tab}; '
      f'rank pattern as claimed {z2c_rank}; own seeds: ' + '; '.join(sd))
cc('CC2', inner(seeds['i'], matvec(gx(ONE, ONE), seeds['i'])).zero(), 'class-(i) seed orthogonalized by (u, v) = (1, 1)')

# ---------------------------------------------------------------- Z3
h0, h1, h2, h3 = sp.symbols('h0 h1 h2 h3')
hv = sp.Matrix([h0, h1, h2, h3])


def sdet(x):
    return x[0] * x[3] - x[1] * x[2]


z3a = sp.expand(sdet(sD(u_, v_) * hv) - v_ * (h0 * h3 - u_ ** 2 * h1 * h2)) == 0
z3a &= sp.expand(sdet(sC * sD(u_, v_) * hv) - u_ * (h0 * h2 - v_ ** 2 * h1 * h3)) == 0
z3a &= sp.expand(sdet(sC * sp.Matrix([h0, 0, 0, h3]))) == 0 and sp.expand(sdet(sC * sp.Matrix([0, h1, h2, 0]))) == 0
a = sp.symbols('a0:4', nonnegative=True)
S = sum(t ** 2 for t in a)
x_, y_ = a[0] * a[3] - a[1] * a[2], a[0] * a[2] - a[1] * a[3]
sos = [S / 2 - x_ - ((a[0] - a[3]) ** 2 + (a[1] + a[2]) ** 2) / 2, S / 2 + x_ - ((a[0] + a[3]) ** 2 + (a[1] - a[2]) ** 2) / 2,
       S / 2 - y_ - ((a[0] - a[2]) ** 2 + (a[1] + a[3]) ** 2) / 2, S / 2 + y_ - ((a[0] + a[2]) ** 2 + (a[1] - a[3]) ** 2) / 2]
z3b = all(sp.expand(e) == 0 for e in sos)
# |x| = S/2 with a >= 0: (a0 = a3, a1 = a2 = 0) or (a0 = a3 = 0, a1 = a2); |y| = S/2: (a0 = a2, a1 = a3 = 0) or
# (a0 = a2 = 0, a1 = a3).  Intersect the four combinations as linear systems.
X_cases = [[a[0] - a[3], a[1], a[2]], [a[0], a[3], a[1] - a[2]]]
Y_cases = [[a[0] - a[2], a[1], a[3]], [a[0], a[2], a[1] - a[3]]]
only_zero = True
for xc in X_cases:
    for yc in Y_cases:
        sol = sp.linsolve(xc + yc, list(a))
        only_zero &= sol == sp.FiniteSet((0, 0, 0, 0))
z3b &= only_zero
z3c, cmsg = True, []
ws = [rp(0), rp(None), rp(1), rp(-1), rp(F(1, 2)), rp(2), rp(F(1, 3)), rp(F(-1, 2)), rp(3), rp(F(2, 3))]
for w in ws:
    for b in (vec(1, 0, 0, w), vec(0, 1, w, 0)):
        maxent = 4 * det2(b).n2() == n2v(b) ** 2
        p = matvec(CNOT, b)
        product = det2(p).zero()
        pairing = qf(defect(2, p), p) / n2v(p)
        z3c &= maxent and product and pairing == -1
cmsg = f'20 Bell states (w at ten rational points): maximally entangled, CNOT image a product, c = 2 defect of the image pairs -1 with it: {z3c}'
z3d = sp.expand((x_ + y_) - (a[0] - a[1]) * (a[2] + a[3])) == 0 and sp.expand((x_ - y_) - (a[0] + a[1]) * (a[3] - a[2])) == 0
astar = (sp.sqrt(2) / 2, 0, sp.Rational(1, 2), sp.Rational(1, 2))
sub = dict(zip(a, astar))
Sst, xst, yst = [sp.nsimplify(sp.simplify(e.subs(sub))) for e in (S, x_, y_)]
dmin_star = sp.simplify(sp.Min(xst ** 2, yst ** 2) / Sst ** 2)
z3d &= Sst == 1 and sp.simplify(dmin_star - sp.Rational(1, 8)) == 0
cmax = sp.simplify(2 / (1 + sp.sqrt(1 - 4 * sp.Rational(1, 8))))
z3d &= sp.simplify(cmax - (4 - 2 * sp.sqrt(2))) == 0
rng = random.Random(20261011)
best = 0.0
for _ in range(200000):
    t = [abs(rng.gauss(0, 1)) for _ in range(4)]
    s = sum(q * q for q in t) ** 0.5
    t = [q / s for q in t]
    d = min((t[0] * t[3] - t[1] * t[2]) ** 2, (t[0] * t[2] - t[1] * t[3]) ** 2)
    best = max(best, d)
z3e = best <= 0.125 + 1e-12
check('Z3', z3a and z3b and z3c and z3d and z3e,
      f'determinant identities and two-zero CNOT products {z3a}; SOS identities and only a = 0 {z3b}; {cmsg}; '
      f'x +- y factorizations, D_min = 1/8 exactly at a* = (sqrt2/2, 0, 1/2, 1/2), c_max = 2/(1 + 1/sqrt2) = '
      f'4 - 2 sqrt2 = {sp.N(cmax, 8)} {z3d}; [N] random max D_min = {best:.10f} <= 1/8 {z3e}')
# CC3: T^2 x| <X_B> without CNOT keeps |00> + |11> maximally entangled
notmax = False
b = vec(1, 0, 0, 1)
for u in U_LIST[:6]:
    for v in U_LIST[:6]:
        for g in (Dm(u, v), matmul(Dm(u, v), XB)):
            p = matvec(g, b)
            if 4 * det2(p).n2() != n2v(p) ** 2:
                notmax = True
cc('CC3', notmax, 'under T^2 x| <X_B> (72 sampled points) some orbit point of |00> + |11> is not maximally entangled')

# ---------------------------------------------------------------- Z4
cs, ck, s_, sp_ = sp.symbols('cs ck s sp')
lam = (cs - 1) / (4 - 2 * cs)
pairing = 1 - ck * s + lam * (4 - cs - ck + cs * ck * sp_)
decomp = (cs - ck) * (1 + lam) + ck * sp_ * (1 + lam * cs) + ck * (1 - s - sp_)
z4a = sp.simplify(pairing - decomp) == 0
z4b = sp.expand((4 - ck - cs + ck * cs * s) - (4 - 2 * cs) - ((cs - ck) + ck * cs * s)) == 0


def dmin_exact(h):
    """min over the G_T-orbit of |det|^2/|h|^4 = min((|h0h3| - |h1h2|)^2, (|h0h2| - |h1h3|)^2)/|h|^4 for seeds whose
    moduli are rational (checked); the formula is the triangle inequality on det Psi(D(u,v)h) = v(h0h3 - u^2 h1h2) and
    its CNOT branch (Z3(a)) plus X_B's invariance of |det|"""
    mods = []
    for x in h:
        r2 = x.n2()
        r = F(int(r2.numerator ** 0.5 + 0.5), int(r2.denominator ** 0.5 + 0.5))
        assert r * r == r2, 'irrational modulus'
        mods.append(r)
    n2 = n2v(h)
    return min((mods[0] * mods[3] - mods[1] * mods[2]) ** 2, (mods[0] * mods[2] - mods[1] * mods[3]) ** 2) / n2 ** 2


def h1_ok(c, D):
    return 1 - 4 * D <= (F(2) / c - 1) ** 2


hs = seeds['i']
cstar = F(1001, 1000)
lamv = (cstar - 1) / (4 - 2 * cstar)
Dh = dmin_exact(hs)
cl, sols = solutions(hs, 1)
gu, gv = sols[0]
g0 = gx(gu, gv)
ghs = matvec(g0, hs)
yW = lin((1, proj(hs)), (lamv, defect(cstar, ghs)))
dh = defect(cstar, hs)
z4c = Dh == F(1, 225) and h1_ok(cstar, Dh) and pr(yW, dh) == 0 and qf(yW, ghs) < 0
h2s = vec(2, 1, 1, 3)
c2 = F(2001, 2000)
D2 = dmin_exact(h2s)
z4c &= h1_ok(c2, D2)
cosets = [eye(), CNOT, XB, matmul(XB, CNOT)]
tor = [rp(0), rp(F(1, 2)), rp(2), rp(F(-1, 3)), rp(None)]
nsamp, minpair, samp_ok = 0, None, True
for seed, cval in ((hs, cstar), (h2s, c2)):
    for u in tor:
        for v in tor:
            for sg in cosets:
                k = matvec(matmul(Dm(u, v), sg), seed)
                dk = defect(cval, k)
                pv = pr(yW, dk)
                sv = inner(hs, k).n2() / (n2v(hs) * n2v(k))
                spv = inner(ghs, k).n2() / (n2v(ghs) * n2v(k))
                formula = (cstar - cval) * (1 + lamv) + cval * spv * (1 + lamv * cstar) + cval * (1 - sv - spv)
                Dk = det2(k).n2() / n2v(k) ** 2
                samp_ok &= pv >= 0 and pv == formula and pr(dk, dh) > 0 and h1_ok(cval, Dk)
                minpair = pv if minpair is None else min(minpair, pv)
                nsamp += 1
z4c &= samp_ok and nsamp == 200
check('Z4', z4a and z4b and z4c,
      f'witness decomposition identity {z4a}; <d_k, d_h> bound identity {z4b}; seed (1, 2i, 3, 1): D_min = {Dh}, '
      f'c* = {cstar} with H1, g = D({gu}, {gv}) X_B, lam = {lamv}, <y, d_h> = {pr(yW, dh)}, (gh)^+ y (gh)/|gh|^2 = '
      f'{qf(yW, ghs) / n2v(ghs)}; second seed (2, 1, 1, 3): D_min = {D2}, c = {c2} with H1; {nsamp} samples: pairing >= 0 '
      f'and = decomposition, <d, d_h> > 0, H1: {samp_ok}; min sample pairing {minpair}')
lam2 = (c2 - 1) / (4 - 2 * c2)
y2 = lin((1, proj(hs)), (lam2, defect(c2, ghs)))
cc('CC4', pr(y2, dh) >= 0, f'witness at c2 = {c2} pairs {pr(y2, dh)} with the c* copy of d_h')

# ---------------------------------------------------------------- Z5
c32 = F(3, 2)


def pair_formula(c, h, k, g):
    gh_, gk_ = matvec(g, h), matvec(g, k)
    nh, nk = n2v(h), n2v(k)

    def ov(a_, b_, na, nb):
        return inner(a_, b_).n2() / (na * nb)

    return (c * c * ov(h, gh_, nh, nh) + c * (2 - c) * (ov(h, gk_, nh, nk) + ov(k, gh_, nk, nh))
            + (2 - c) ** 2 * ov(k, gk_, nk, nk))


z5a, z5b = True, True
inst_h, inst_k = seeds['i'], None
kperp = nullspace(orth_rows([inst_h]))[0]
for (u, v) in [(rp(F(1, 2)), rp(2)), (rp(3), rp(F(-1, 3)))]:
    for sg in cosets:
        g = matmul(Dm(u, v), sg)
        d = defect2(c32, inst_h, kperp)
        z5a &= pr(d, conjugate_by(g, d)) == pair_formula(c32, inst_h, kperp, g)
# (b): the generic partner kperp with an orthogonalizing g: positive pairing and the local condition fails at u = h, x = gh
cl, sols = solutions(inst_h, 1)
g = gx(*sols[0])
d = defect2(c32, inst_h, kperp)
gd = conjugate_by(g, d)
z5b = pr(d, gd) > 0 and qf(d, inst_h) < 0 and inner(inst_h, matvec(g, inst_h)).zero() and qf(gd, matvec(g, inst_h)) < 0
rmsg, z5c, z5d, cc5 = [], True, True, False
k0s = {}
for nm in ('i', 'ii', 'iii', 'iv'):
    h = seeds[nm]
    cl, sols = solutions(h, 8)
    partners = [matvec(gx(u, v), h) for u, v in sols]
    ns = nullspace(orth_rows(partners + [h]))
    rr = rank(partners)
    if nm == 'i':
        z5c &= rr == 3 and len(ns) == 0
    else:
        z5c &= rr == 2 and len(ns) == 1
        if len(ns) == 1:
            k0s[nm] = ns[0]
    rmsg.append(f'{nm}: rank {rr}, partner space dim {len(ns)}' + (f', k0 = {ns[0]}' if len(ns) == 1 else ''))
tight = []
for nm, k0 in k0s.items():
    h = seeds[nm]
    cl, sols = solutions(h, 8)
    d = defect2(c32, h, k0)
    zp = all(pr(d, conjugate_by(gx(u, v), d)) == 0 for u, v in sols)
    # CC5: a vector orthogonal to h, not proportional to k0
    others = [b_ for b_ in nullspace(orth_rows([h])) if rank([b_, k0]) == 2]
    kk = others[0]
    dd = defect2(c32, h, kk)
    cc5 |= all(pr(dd, conjugate_by(gx(u, v), dd)) == 0 for u, v in sols)
    # tightness search (fixed order): U in T^2 near 1; u = h + b k0 inside the cap near its boundary
    ratio = n2v(h) / n2v(k0)  # cap: |b|^2 < ratio
    found = None
    us = [rp(F(1, 10)), rp(F(-1, 10)), rp(F(1, 20)), rp(F(-1, 20)), rp(F(1, 50)), rp(F(-1, 50))]
    Us = []
    for e in us:
        Us += [('D(e,1)', Dm(e, 1)), ('D(1,e)', Dm(1, e)), ('D(e,e)', Dm(e, e)), ('D(e,1/e)', Dm(e, ONE / e))]
    phases = [rp(0), rp(None), rp(1), rp(-1), rp(F(1, 2)), rp(2), rp(F(-1, 2)), rp(-2), rp(F(1, 3)), rp(3),
              rp(F(-1, 3)), rp(-3)]
    for shrink in (F(99, 100), F(999, 1000), F(9, 10)):
        target = ratio * shrink * shrink  # |b|^2 = target < ratio
        # |b| = rho with rho^2 = target need not be a square; use rho = a rational just below sqrt(target)
        num, den = target.numerator, target.denominator
        rho = F(int((num * 10 ** 12 // den) ** 0.5), 10 ** 6)
        for ph in phases:
            bb = ph * rho
            uu = [x + bb * y for x, y in zip(h, k0)]
            if not qf(d, uu) < 0:
                continue
            coef = inner(uu, k0) / gq(n2v(uu))
            xx = [y - coef * x for x, y in zip(uu, k0)]
            for nmU, Um in Us:
                Ud = conjugate_by(Um, d)
                if qf(d, xx) > 0 and pr(d, Ud) > 0 and qf(Ud, xx) < 0 and inner(uu, xx).zero():
                    found = (nmU, shrink, ph, rho, qf(Ud, xx) / n2v(xx))
                    break
            if found:
                break
        if found:
            break
    z5d &= zp and found is not None
    tight.append(f'{nm}: zero pairing on 8 g {zp}; tightness ' +
                 (f'{found[0]} (shrink {found[1]}, phase {found[2]}, |b| = {found[3]}), x^+ (U d U^+) x/|x|^2 = '
                  f'{float(found[4]):.3e}' if found else 'NOT FOUND'))
check('Z5', z5a and z5b and z5c and z5d,
      f'pairing formula on 8 instances {z5a}; local condition fails at u = h, x = gh for a generic partner with an '
      f'orthogonalizing g {z5b}; ' + '; '.join(rmsg) + '; ' + '; '.join(tight))
cc('CC5', cc5, 'a partner orthogonal to h and not proportional to k0 has zero pairing on the orthogonalizing family')

fails = [k for k, ok in RESULTS.items() if not ok] + [k for k, v in CCS.items() if v]
print()
print(f'PASS {sum(RESULTS.values())}/{len(RESULTS)}; countercontrols False {sum(1 for v in CCS.values() if not v)}/{len(CCS)}')
print('VERDICT INDEP-C5-FIXED' if not fails else 'VERDICT INDEP-C5-FAILED ' + ' '.join(fails))
