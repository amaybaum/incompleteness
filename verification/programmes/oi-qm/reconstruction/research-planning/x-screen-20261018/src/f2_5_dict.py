#!/usr/bin/env python3
"""f2_5_dict.py -- F2-5: OI's operational primitives through E1's phase-point dictionary (exact, q = 3).

Cells and controls are those of RULES.md as corrected by amendments/amendment-1.md and amendment-2.md. Arithmetic is exact in Q(w),
w = exp(2 pi i / 3), stored as a + b w with Fraction coefficients (w^2 = -1 - w). Standard library only.
"""
import sys
from fractions import Fraction
from itertools import combinations, permutations, product

q = 3
INV2 = 2  # 2^{-1} mod 3

results = []


def check(name, ok, detail=''):
    results.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ('  ' + detail if detail else ''))
    return bool(ok)


# ---------------------------------------------------------------- Q(w)
class K:
    __slots__ = ('a', 'b')

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, o):
        o = o if isinstance(o, K) else K(o)
        return K(self.a + o.a, self.b + o.b)
    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, K) else K(o)
        return K(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return K(o) - self

    def __neg__(self):
        return K(-self.a, -self.b)

    def __mul__(self, o):
        if not isinstance(o, K):
            o = K(o)
        a, b, c, d = self.a, self.b, o.a, o.b
        return K(a * c - b * d, a * d + b * c - b * d)
    __rmul__ = __mul__

    def conj(self):
        return K(self.a - self.b, -self.b)

    def norm(self):
        return self.a * self.a - self.a * self.b + self.b * self.b

    def __truediv__(self, o):
        if not isinstance(o, K):
            o = K(o)
        n = o.norm()
        c = self * o.conj()
        return K(c.a / n, c.b / n)

    def __eq__(self, o):
        o = o if isinstance(o, K) else K(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def is_real(self):
        return self.b == 0

    def iszero(self):
        return self.a == 0 and self.b == 0


ZERO, ONE = K(0), K(1)
W = K(0, 1)


def wpow(k):
    k %= 3
    return ONE if k == 0 else (W if k == 1 else K(-1, -1))


# ---------------------------------------------------------------- matrices
def zeros(n, m=None):
    return [[ZERO] * (m if m is not None else n) for _ in range(n)]


def eye(n):
    M = zeros(n)
    for i in range(n):
        M[i][i] = ONE
    return M


def mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = zeros(n, p)
    for i in range(n):
        Ai = A[i]
        row = out[i]
        for k in range(m):
            a = Ai[k]
            if a.iszero():
                continue
            Bk = B[k]
            for j in range(p):
                if not Bk[j].iszero():
                    row[j] = row[j] + a * Bk[j]
    return out


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def kron(A, B):
    n, m = len(A), len(B)
    out = zeros(n * m)
    for i in range(n):
        for j in range(n):
            if A[i][j].iszero():
                continue
            for k in range(m):
                for l in range(m):
                    out[i * m + k][j * m + l] = A[i][j] * B[k][l]
    return out


def tr(A):
    s = ZERO
    for i in range(len(A)):
        s = s + A[i][i]
    return s


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def scal(c, A):
    return [[c * x for x in row] for row in A]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def hermitian(A):
    return meq(A, dag(A))


def ptrace2(A, d1, d2):
    """tr over the second factor of a (d1 d2) x (d1 d2) matrix."""
    out = zeros(d1)
    for i in range(d1):
        for j in range(d1):
            s = ZERO
            for k in range(d2):
                s = s + A[i * d2 + k][j * d2 + k]
            out[i][j] = s
    return out


# ---------------------------------------------------------------- PSD tests
def psd_ldl(A):
    n = len(A)
    M = [row[:] for row in A]
    for k in range(n):
        d = M[k][k]
        if not d.is_real():
            return False
        if d.a < 0:
            return False
        if d.a == 0:
            if any(not M[k][j].iszero() for j in range(k + 1, n)):
                return False
            continue
        for i in range(k + 1, n):
            if M[i][k].iszero():
                continue
            f = M[i][k] / d
            for j in range(k + 1, n):
                M[i][j] = M[i][j] - f * M[k][j]
    return True


def charpoly(A):
    """Faddeev-LeVerrier: coefficients c[0..n] of det(tI - A) = sum c_i t^i."""
    n = len(A)
    c = [ZERO] * (n + 1)
    c[n] = ONE
    Mk = zeros(n)
    I = eye(n)
    for k in range(1, n + 1):
        Mk = add(mm(A, Mk), scal(c[n - k + 1], I))
        c[n - k] = -(tr(mm(A, Mk)) / K(k))
    return c


def psd_charpoly(A):
    n = len(A)
    c = charpoly(A)
    for k in range(n + 1):
        e = c[n - k] * K((-1) ** k)
        if not e.is_real() or e.a < 0:
            return False
    return True


psd_disagree = [0]


def psd(A):
    a, b = psd_ldl(A), psd_charpoly(A)
    if a != b:
        psd_disagree[0] += 1
    return a


# ---------------------------------------------------------------- Weyl and phase-point operators
def digits(y, n):
    """Site 1 is the most significant digit, matching the Kronecker order (amendment 2)."""
    return [(y // q ** (n - 1 - i)) % q for i in range(n)]


def undig(v):
    n = len(v)
    return sum(vi * q ** (n - 1 - i) for i, vi in enumerate(v))


def D(xs, xis):
    """N-site Weyl operator D(x, xi) = w^{-2^{-1} x.xi} Z^xi X^x on (C^3)^{tensor N}."""
    n = len(xs)
    d = q ** n
    M = zeros(d)
    ph = (-INV2 * sum(a * b for a, b in zip(xs, xis))) % q
    for y in range(d):
        yv = digits(y, n)
        tv = [(yi + xi) % q for yi, xi in zip(yv, xs)]       # X^x |y> = |y + x>
        z = sum(b * t for b, t in zip(xis, tv)) % q            # Z^xi |t> = w^{xi.t} |t>
        M[undig(tv)][y] = wpow(ph + z)
    return M


def Par(n):
    d = q ** n
    M = zeros(d)
    for y in range(d):
        M[undig([(-v) % q for v in digits(y, n)])][y] = ONE
    return M


def A_op(xs, xis):
    Dz = D(xs, xis)
    return mm(mm(Dz, Par(len(xs))), dag(Dz))


PTS1 = [(x, xi) for x in range(q) for xi in range(q)]          # one-site phase space, index 3x + xi
A1 = {z: A_op([z[0]], [z[1]]) for z in PTS1}
D1 = {z: D([z[0]], [z[1]]) for z in PTS1}


def symp(z, w):
    return (z[0] * w[1] - z[1] * w[0]) % q


# ---------------------------------------------------------------- K-weyl
kw = all(meq(mm(D1[z], dag(D1[z])), eye(3)) for z in PTS1)
kw &= all(tr(D1[z]) == (K(3) if z == (0, 0) else ZERO) for z in PTS1)
for z in PTS1:
    for w_ in PTS1:
        s = ((z[0] + w_[0]) % q, (z[1] + w_[1]) % q)
        kw &= meq(mm(D1[z], D1[w_]), scal(wpow(-INV2 * symp(z, w_)), D1[s]))
check('K-weyl', kw, 'D unitary, tr D(z) = 3 delta, D(z)D(w) = w^{-2^{-1}<z,w>} D(z+w) for all 81 pairs')

# ---------------------------------------------------------------- K-pp
kp = all(hermitian(A1[z]) and tr(A1[z]) == ONE for z in PTS1)
kp &= all(tr(mm(A1[z], A1[w_])) == (K(3) if z == w_ else ZERO) for z in PTS1 for w_ in PTS1)
S = zeros(3)
for z in PTS1:
    S = add(S, A1[z])
kp &= meq(S, scal(K(3), eye(3)))
check('K-pp', kp, 'A(z) Hermitian, tr 1, tr A(z)A(w) = 3 delta, sum A(z) = 3I')

# ---------------------------------------------------------------- K-psd
proj = [[K(Fraction(1, 2)), K(Fraction(1, 2)), ZERO], [K(Fraction(1, 2)), K(Fraction(1, 2)), ZERO], [ZERO, ZERO, ZERO]]
dm = [[ONE, ZERO], [ZERO, K(-1)]]
kpsd = psd_ldl(eye(3)) and psd_charpoly(eye(3)) and psd_ldl(proj) and psd_charpoly(proj)
kpsd &= not psd_ldl(dm) and not psd_charpoly(dm) and not psd_ldl(A1[(0, 0)]) and not psd_charpoly(A1[(0, 0)])
check('K-psd', kpsd, 'both PSD tests accept I and a projector, reject diag(1,-1) and A(0)')


# ---------------------------------------------------------------- superoperators and Choi
def E(i, j, d=3):
    M = zeros(d)
    M[i][j] = ONE
    return M


def wig(rho, z):
    return tr(mm(A1[z], rho)) / K(3)


def phi_from_T(T):
    """T: dict z -> list of (z', weight). Returns Phi as a function on 3x3 matrices."""
    def phi(rho):
        out = zeros(3)
        for z in PTS1:
            wz = wig(rho, z)
            if wz.iszero():
                continue
            for z2, wt in T.get(z, []):
                out = add(out, scal(wz * K(wt), A1[z2]))
        return out
    return phi


def choi(phi, d=3, transpose_input=False):
    C = zeros(d * d)
    for i in range(d):
        for j in range(d):
            img = phi(E(j, i, d) if transpose_input else E(i, j, d))
            for k in range(d):
                for l in range(d):
                    C[i * d + k][j * d + l] = img[k][l]
    return C


kc = psd(choi(lambda r: r)) and not psd(choi(lambda r: [[r[j][i] for j in range(3)] for i in range(3)]))
deph = lambda r: [[r[i][j] if i == j else ZERO for j in range(3)] for i in range(3)]
kc &= psd(choi(deph))
Cid = choi(lambda r: r)
kc &= meq(mm(Cid, Cid), scal(K(3), Cid))  # rank one: C^2 = 3 C
check('K-choi', kc, 'Choi of identity PSD rank one, of transpose not PSD, of dephasing PSD')

# ---------------------------------------------------------------- OD-SUB
LINES = set()
for z0 in PTS1:
    for dvec in [(0, 1), (1, 0), (1, 1), (1, 2)]:
        LINES.add(frozenset(((z0[0] + t * dvec[0]) % q, (z0[1] + t * dvec[1]) % q) for t in range(q)))
sub_ok = len(LINES) == 12 and all(not psd(A1[z]) for z in PTS1)
SUBPSD = {}
for Sset in combinations(PTS1, 3):
    M = zeros(3)
    for z in Sset:
        M = add(M, A1[z])
    M = scal(K(Fraction(1, 3)), M)
    ok = psd(M)
    SUBPSD[frozenset(Sset)] = ok
    sub_ok &= ok == (frozenset(Sset) in LINES)
od_sub = check('OD-SUB', sub_ok, 'every A(z) indefinite; of the 84 three-subsets exactly the 12 lines give a PSD operator')

# ---------------------------------------------------------------- OD-REV
idx = {z: i for i, z in enumerate(PTS1)}
line_list = [sorted(idx[z] for z in l) for l in LINES]
lineset_idx = {frozenset(l) for l in line_list}
lp = []
n_perm = 0
nonline_witness_ok = True
for perm in permutations(range(9)):
    n_perm += 1
    good = True
    for l in line_list:
        if frozenset(perm[i] for i in l) not in lineset_idx:
            good = False
            img = frozenset(PTS1[perm[i]] for i in l)
            nonline_witness_ok &= not SUBPSD[img]
            break
    if good:
        lp.append(perm)
# independent enumeration of AGL and ASL
agl, asl = set(), set()
for a, b, c, d in product(range(q), repeat=4):
    det = (a * d - b * c) % q
    if det == 0:
        continue
    for t0, t1 in PTS1:
        perm = tuple(idx[((a * x + b * xi + t0) % q, (c * x + d * xi + t1) % q)] for x, xi in PTS1)
        agl.add(perm)
        if det == 1:
            asl.add(perm)
cp_set, pos_noncp = set(), set()
for perm in lp:
    T = {PTS1[i]: [(PTS1[perm[i]], 1)] for i in range(9)}
    ph = phi_from_T(T)
    if psd(choi(ph)):
        cp_set.add(perm)
    elif psd(choi(ph, transpose_input=True)):
        pos_noncp.add(perm)
check('K-AGL', len(agl) == 432 and len(asl) == 216 and set(lp) == agl and cp_set == asl,
      'independent AGL(2,3) (432) and ASL(2,3) (216) equal the line-preserving and CP sets of the sweep')
od_rev = check('OD-REV', n_perm == 362880 and set(lp) == agl and cp_set == asl and pos_noncp == agl - asl
               and nonline_witness_ok,
               '%d permutations: %d line-preserving, %d CP, %d positive and not CP (Phi o transpose CP), %d with a '
               'stabilizer state sent to a non-PSD operator' % (n_perm, len(lp), len(cp_set), len(pos_noncp),
                                                                n_perm - len(lp)))

# ---------------------------------------------------------------- OD-PREP
priors = [(a, b, 6 - a - b) for a in range(7) for b in range(7 - a)]
prep_ok = len(priors) == 28 and all(not psd(A1[z]) for z in PTS1)
n_psd = 0
for a in range(q):
    for nu in priors:
        M = zeros(3)
        for xi in range(q):
            M = add(M, scal(K(Fraction(nu[xi], 6)), A1[(a, xi)]))
        ok = psd(M)
        n_psd += ok
        prep_ok &= ok == (nu == (2, 2, 2))
Cnt = zeros(3)
for z in PTS1:
    Cnt = add(Cnt, scal(K(Fraction(1, 9)), A1[z]))
prep_ok &= meq(Cnt, scal(K(Fraction(1, 3)), eye(3)))
# K-psd-neg: a non-uniform registered prior rejected and the uniform accepted, by both tests
Mnu = add(scal(K(Fraction(1, 2)), A1[(0, 0)]), scal(K(Fraction(1, 2)), A1[(0, 1)]))
Mun = zeros(3)
for xi in range(q):
    Mun = add(Mun, scal(K(Fraction(1, 3)), A1[(0, xi)]))
check('K-psd-neg', not psd_ldl(Mnu) and not psd_charpoly(Mnu) and psd_ldl(Mun) and psd_charpoly(Mun),
      'non-uniform registered prior rejected, uniform accepted, by both tests')
od_prep = check('OD-PREP', prep_ok, 'point laws map to non-states; %d of 84 registered priors give a state (the '
                'uniform one at each value); counting measure maps to I/3' % n_psd)

# ---------------------------------------------------------------- OD-READ
read_ok = True
for k in range(q):
    Tk = {z: [(z, 1)] for z in PTS1 if z[0] == k}
    Tpk = {z: [((k, xi2), Fraction(1, 3)) for xi2 in range(q)] for z in PTS1 if z[0] == k}
    pk, ppk = phi_from_T(Tk), phi_from_T(Tpk)
    read_ok &= not psd(choi(pk))
    Pk = E(k, k)
    for i in range(3):
        for j in range(3):
            read_ok &= meq(ppk(E(i, j)), mm(mm(Pk, E(i, j)), Pk))
    for a in range(3):
        read_ok &= meq(pk(E(a, a)), ppk(E(a, a)))
od_read = check('OD-READ', read_ok, 'non-disturbing readout not CP; re-randomizing readout equals Lueders; the two '
                'agree on diagonal states; k = 0, 1, 2')

# ---------------------------------------------------------------- N = 2 operators
PTS2 = [((x1, xi1), (x2, xi2)) for (x1, xi1) in PTS1 for (x2, xi2) in PTS1]
A2 = {z: A_op([z[0][0], z[1][0]], [z[0][1], z[1][1]]) for z in PTS2}

# ---------------------------------------------------------------- K-order (amendment 2)
check('K-order', all(meq(D([a[0], b[0]], [a[1], b[1]]), kron(D1[a], D1[b])) for a, b in PTS2),
      'D((x1,x2),(xi1,xi2)) = D(x1,xi1) x D(x2,xi2) for all 81 pairs')

# ---------------------------------------------------------------- OD-AD
ad_ok = all(meq(A2[(z1, z2)], kron(A1[z1], A1[z2])) for z1, z2 in PTS2)
for z1 in PTS1:
    M = zeros(9)
    for z2 in PTS1:
        M = add(M, scal(K(Fraction(1, 9)), A2[(z1, z2)]))
    ad_ok &= meq(M, kron(A1[z1], scal(K(Fraction(1, 3)), eye(3))))
ad_ok &= all(meq(ptrace2(A2[(z1, z2)], 3, 3), A1[z1]) for z1, z2 in PTS2)
od_ad = check('OD-AD', ad_ok, 'A(z1,z2) = A(z1) x A(z2) for all 81 z; counting attach gives rho x I/3; '
              'marginalizing site 2 gives tr_2')


# ---------------------------------------------------------------- OD-COMP
def symp2(z, w):
    return (symp(z[0], w[0]) + symp(z[1], w[1])) % q


def addv(z, w, s=1):
    return (((z[0][0] + s * w[0][0]) % q, (z[0][1] + s * w[0][1]) % q),
            ((z[1][0] + s * w[1][0]) % q, (z[1][1] + s * w[1][1]) % q))


zero2 = ((0, 0), (0, 0))
lagr = set()
nz = [z for z in PTS2 if z != zero2]
for u in nz:
    for v in nz:
        if symp2(u, v) != 0:
            continue
        span = frozenset(addv(addv(zero2, u, a), v, b) for a in range(q) for b in range(q))
        if len(span) == 9:
            lagr.add(span)
comp_ok = len(lagr) == 40
n_ent = n_prod = 0
for L in sorted(lagr, key=lambda s: sorted(s)):
    rho = zeros(9)
    for z in L:
        rho = add(rho, scal(K(Fraction(1, 9)), A2[z]))
    pure = hermitian(rho) and tr(rho) == ONE and meq(mm(rho, rho), rho)
    red = ptrace2(rho, 3, 3)
    maxmix = meq(red, scal(K(Fraction(1, 3)), eye(3)))
    redpure = meq(mm(red, red), red)
    in1 = sum(1 for z in L if z[1] == (0, 0))
    in2 = sum(1 for z in L if z[0] == (0, 0))
    is_prod = in1 == 3 and in2 == 3
    comp_ok &= pure and ((is_prod and redpure and not maxmix) or (not is_prod and maxmix))
    n_prod += is_prod
    n_ent += (not is_prod) and maxmix
od_comp = check('OD-COMP', comp_ok, '%d Lagrangian subspaces, each mapping to a rank-one projector: %d products of '
                'lines give product states, %d others give maximally entangled states' % (len(lagr), n_prod, n_ent))

# ---------------------------------------------------------------- OD-HOLD and K-cov-neg
def jmap(z):
    return ((-z[1]) % q, z[0])


V = zeros(3)
for z in PTS1:
    V = add(V, mm(D1[jmap(z)], dag(D1[z])))
VV = mm(V, dag(V))
lam = VV[0][0]
hold_ok = not lam.iszero() and lam.is_real() and lam.a > 0 and meq(VV, scal(lam, eye(3)))
hold_ok &= all(meq(mm(mm(V, A1[z]), dag(V)), scal(lam, A1[jmap(z)])) for z in PTS1)
V2 = mm(V, V)
V4 = mm(V2, V2)
hold_ok &= meq(V4, scal(V4[0][0], eye(3))) and not V4[0][0].iszero()
Pi = Par(1)
ratio = None
for i in range(3):
    for j in range(3):
        if not Pi[i][j].iszero():
            ratio = V2[i][j] / Pi[i][j]
            break
    if ratio is not None:
        break
hold_ok &= meq(V2, scal(ratio, Pi))
for k in range(q):
    Pk = E(k, k)
    ppk = phi_from_T({z: [((k, xi2), Fraction(1, 3)) for xi2 in range(q)] for z in PTS1 if z[0] == k})
    for i in range(3):
        for j in range(3):
            hold_ok &= meq(ppk(ppk(E(i, j))), ppk(E(i, j)))
    one = mm(mm(V, Pk), dag(V))
    hold_ok &= (one[k][k] / lam) != ONE
    four = mm(mm(V4, Pk), dag(V4))
    hold_ok &= (four[k][k] / (lam * lam * lam * lam)) == ONE
wrong = all(meq(mm(mm(V, A1[z]), dag(V)), scal(lam, A1[((jmap(z)[0] + 1) % q, jmap(z)[1])])) for z in PTS1)
check('K-cov-neg', not wrong, 'covariance against the shifted target A(Jz + (1,0)) fails')
od_hold = check('OD-HOLD', hold_ok, 'free-leap covariance unitary: U A(z) U^dag = A(Jz), U^4 ~ I, U^2 ~ parity; '
                'Lueders registration idempotent; one free tick loses the registered value, four restore it')

# ---------------------------------------------------------------- tokens
check('K-psd-agree', psd_disagree[0] == 0, 'the LDL and characteristic-polynomial tests agreed on every matrix '
      '(%d disagreements)' % psd_disagree[0])
controls = all(ok for name, ok in results if name.startswith('K-'))
cells = [('OD-SUB', od_sub, 'OD-SUB-LINES'), ('OD-REV', od_rev, 'OD-REV-CLIFFORD'),
         ('OD-PREP', od_prep, 'OD-PREP-REGISTERED-UNIFORM'), ('OD-READ', od_read, 'OD-READ-BACKACTION'),
         ('OD-AD', od_ad, 'OD-AD-TRANSFER'), ('OD-COMP', od_comp, 'OD-COMP-STABILIZER'),
         ('OD-HOLD', od_hold, 'OD-HOLD-STROBOSCOPIC')]
if not controls:
    print('VERDICT VOID (a control failed)')
    sys.exit(1)
for _, ok, tok in cells:
    if ok:
        print('TOKEN ' + tok)
print('VERDICT ' + ('OD-READ' if all(ok for _, ok, _ in cells) else 'OD-NOT-READ'))
fails = sum(1 for _, ok in results if not ok)
print('checks: %d, failures: %d' % (len(results), fails))
sys.exit(0)
