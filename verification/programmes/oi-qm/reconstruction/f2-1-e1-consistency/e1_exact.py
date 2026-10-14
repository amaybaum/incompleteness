#!/usr/bin/env python3
"""F2-1: exact computations for candidate E1, as frozen in RULES.md and amendment 1 (2026-10-14).

Run:  python3 -I e1_exact.py > e1-exact-output.txt
Standard library only. Every decisive measurement is exact: rationals and the cyclotomic fields
Q(zeta_n), implemented here as integer polynomials modulo the n-th cyclotomic polynomial.
Lines tagged [N] are floating-point and decide nothing. Lines tagged [L] cite literature.
The output is deterministic (no randomness, no timing, no hash-order dependence).
"""
import itertools
import sys
from fractions import Fraction
from math import gcd

# ============================================================================ exact arithmetic


def _poly_divmod_int(num, den):
    """Exact division of integer polynomials (low-to-high), den monic. Returns quotient."""
    num = list(num)
    dq = len(den) - 1
    out = [0] * (len(num) - dq)
    for k in range(len(num) - 1, dq - 1, -1):
        c = num[k]
        if c:
            out[k - dq] = c
            for j, dj in enumerate(den):
                num[k - dq + j] -= c * dj
    assert all(v == 0 for v in num[:dq]), "non-exact cyclotomic division"
    return out


_PHI_CACHE = {}


def cyclotomic_poly(n):
    if n in _PHI_CACHE:
        return _PHI_CACHE[n]
    p = [-1] + [0] * (n - 1) + [1]          # x^n - 1
    for d in range(1, n):
        if n % d == 0:
            p = _poly_divmod_int(p, cyclotomic_poly(d))
    _PHI_CACHE[n] = p
    return p


class Cyc:
    """The cyclotomic field Q(zeta_n), zeta_n = exp(2 pi i / n) under the fixed embedding.

    An element is (c, d): c a tuple of ints (coefficients of 1, zeta, ..., zeta^(phi-1)),
    d a positive int denominator, normalized so that gcd(d, c_0, ..., c_{phi-1}) = 1.
    """

    def __init__(self, n):
        self.n = n
        self.Phi = cyclotomic_poly(n)
        self.deg = len(self.Phi) - 1
        D = self.deg
        self.low = [(j, c) for j, c in enumerate(self.Phi[:D]) if c]   # x^D = -sum c_j x^j
        self.zero = ((0,) * D, 1)
        self.one = ((1,) + (0,) * (D - 1), 1)
        pw = []
        for k in range(n):
            v = [0] * (max(D, k + 1))
            v[k] = 1
            pw.append(self._reduce_list(v))
        self.pw = pw                                   # zeta^k as int tuples
        self.units = [t for t in range(1, n) if gcd(t, n) == 1]
        self._gal = {}

    def _reduce_list(self, v):
        D = self.deg
        v = list(v)
        for k in range(len(v) - 1, D - 1, -1):
            c = v[k]
            if c:
                v[k] = 0
                base = k - D
                for j, cj in self.low:
                    v[base + j] -= c * cj
        v = v[:D] + [0] * (D - len(v[:D]))
        return tuple(v)

    # -- construction
    def norm(self, c, d):
        if d < 0:
            c = tuple(-x for x in c)
            d = -d
        g = gcd(d, *c)
        if g == 0:
            return self.zero
        if g > 1:
            c = tuple(x // g for x in c)
            d //= g
        if not any(c):
            return self.zero
        return (c, d)

    def frac(self, f):
        f = Fraction(f)
        return self.norm((f.numerator,) + (0,) * (self.deg - 1), f.denominator)

    def zeta(self, k):
        return (self.pw[k % self.n], 1)

    def root(self, m, k):
        """zeta_m^k, for m dividing n, or for m dividing 2n with n odd (zeta_2n = -zeta_n^((n+1)/2))."""
        if self.n % m == 0:
            return self.zeta((self.n // m) * k)
        assert self.n % 2 == 1 and (2 * self.n) % m == 0
        e = ((2 * self.n) // m) * k % (2 * self.n)
        z = self.zeta(e * ((self.n + 1) // 2))
        return self.neg(z) if e % 2 else z

    # -- arithmetic
    def add(self, a, b):
        (ac, ad), (bc, bd) = a, b
        if ad == bd:
            return self.norm(tuple(x + y for x, y in zip(ac, bc)), ad)
        return self.norm(tuple(x * bd + y * ad for x, y in zip(ac, bc)), ad * bd)

    def neg(self, a):
        return (tuple(-x for x in a[0]), a[1])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.deg >= 16:
            return self.kmul(a, b)
        return self.smul(a, b)

    def kmul(self, a, b):
        """Kronecker substitution: pack, one big-integer product, unpack signed digits."""
        ac, ad = a
        bc, bd = b
        D = self.deg
        ma = max(abs(x) for x in ac)
        mb = max(abs(x) for x in bc)
        if ma == 0 or mb == 0:
            return self.zero
        k = (ma * mb * D).bit_length() + 2
        A = 0
        for x in reversed(ac):
            A = (A << k) + x
        B = 0
        for x in reversed(bc):
            B = (B << k) + x
        Cn = A * B
        half = 1 << (k - 1)
        mask = (1 << k) - 1
        full = 1 << k
        prod = []
        for _ in range(2 * D - 1):
            c = Cn & mask
            if c >= half:
                c -= full
            prod.append(c)
            Cn = (Cn - c) >> k
        for kk in range(2 * D - 2, D - 1, -1):
            c = prod[kk]
            if c:
                base = kk - D
                for j, cj in self.low:
                    prod[base + j] -= c * cj
        return self.norm(tuple(prod[:D]), ad * bd)

    def smul(self, a, b):
        ac, ad = a
        bc, bd = b
        D = self.deg
        prod = [0] * (2 * D - 1)
        for i, x in enumerate(ac):
            if x:
                for j, y in enumerate(bc):
                    if y:
                        prod[i + j] += x * y
        for k in range(2 * D - 2, D - 1, -1):
            c = prod[k]
            if c:
                base = k - D
                for j, cj in self.low:
                    prod[base + j] -= c * cj
        return self.norm(tuple(prod[:D]), ad * bd)

    def scal(self, f, a):
        f = Fraction(f)
        return self.norm(tuple(x * f.numerator for x in a[0]), a[1] * f.denominator)

    def galois(self, a, t):
        """zeta -> zeta^t."""
        t %= self.n
        if t not in self._gal:
            self._gal[t] = [self.pw[(t * k) % self.n] for k in range(self.deg)]
        rows = self._gal[t]
        out = [0] * self.deg
        for k, x in enumerate(a[0]):
            if x:
                for j, y in enumerate(rows[k]):
                    if y:
                        out[j] += x * y
        return self.norm(tuple(out), a[1])

    def conj(self, a):
        return self.galois(a, -1)

    def inv(self, a):
        assert not self.is_zero(a), "inverse of zero"
        num = self.one
        for t in self.units:
            if t != 1:
                num = self.mul(num, self.galois(a, t))
        nrm = self.mul(a, num)
        assert self.is_rational(nrm)
        return self.scal(1 / self.to_frac(nrm), num)

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def pow(self, a, k):
        r = self.one
        for _ in range(k):
            r = self.mul(r, a)
        return r

    # -- predicates
    def is_zero(self, a):
        return not any(a[0])

    def is_rational(self, a):
        return not any(a[0][1:])

    def to_frac(self, a):
        assert self.is_rational(a)
        return Fraction(a[0][0], a[1])

    def is_real(self, a):
        return self.conj(a) == a

    def is_alg_integer(self, a):
        # Z[zeta_n] is the ring of integers of Q(zeta_n) and the power basis is integral.
        return a[1] == 1

    def embed(self, a, small):
        """Element of the subfield Q(zeta_m) (m | n) -> Q(zeta_n)."""
        m = small.n
        assert self.n % m == 0
        s = self.n // m
        out = [0] * self.deg
        for k, x in enumerate(a[0]):
            if x:
                for j, y in enumerate(self.pw[(s * k) % self.n]):
                    if y:
                        out[j] += x * y
        return self.norm(tuple(out), a[1])

    # -- numerics, for [N] lines only
    def to_complex(self, a):
        import cmath
        z = cmath.exp(2j * cmath.pi / self.n)
        return sum(x * z ** k for k, x in enumerate(a[0])) / a[1]

    def show(self, a):
        if self.is_rational(a):
            return str(self.to_frac(a))
        terms = []
        for k, x in enumerate(a[0]):
            if x:
                terms.append(("%d" % x) + ("" if k == 0 else "*z^%d" % k))
        s = "+".join(terms).replace("+-", "-")
        return ("(%s)/%d" % (s, a[1])) if a[1] != 1 else "(%s)" % s


# ---------------------------------------------------------------- rigorous signs of real elements
# A real element x = sum_k c_k zeta^k equals sum_k c_k cos(2 pi k / n) under the fixed embedding.
# Each cosine is enclosed in a rational interval (Machin's formula for pi, Taylor series with the
# alternating-series remainder); the sign is certified when the enclosure excludes 0.

def _atan_inv_bounds(m, terms):
    x = Fraction(1, m)
    s = Fraction(0)
    for j in range(terms):
        s += (-1) ** j * x ** (2 * j + 1) / (2 * j + 1)
    nxt = x ** (2 * terms + 1) / (2 * terms + 1)
    return s - nxt, s + nxt


def _pi_bounds(terms=40):
    a_lo, a_hi = _atan_inv_bounds(5, terms)
    b_lo, b_hi = _atan_inv_bounds(239, terms)
    return 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo


_PI = _pi_bounds()


def _cos_point_bounds(t, terms=40):
    """cos(t) for a rational t in [0, 4] via Taylor; remainder bounded by the next term."""
    s = Fraction(0)
    term = Fraction(1)
    for j in range(terms):
        if j > 0:
            term = term * (-1) * t * t / ((2 * j - 1) * (2 * j))
        s += term
    nxt = abs(term * t * t / ((2 * terms - 1) * (2 * terms)))
    return s - nxt, s + nxt


_COS_CACHE = {}


def cos_bounds(n, k):
    """Rational enclosure of cos(2 pi k / n)."""
    k %= n
    if 2 * k > n:
        k = n - k
    key = (n, k)
    if key not in _COS_CACHE:
        if k == 0:
            _COS_CACHE[key] = (Fraction(1), Fraction(1))
        else:
            t_lo = 2 * _PI[0] * k / n
            t_hi = 2 * _PI[1] * k / n           # theta in [0, pi]: cos decreasing
            lo, _ = _cos_point_bounds(t_hi)
            _, hi = _cos_point_bounds(t_lo)
            _COS_CACHE[key] = (max(lo, Fraction(-1)), min(hi, Fraction(1)))
    return _COS_CACHE[key]


def real_sign(F, a):
    """Exact sign (-1, 0, +1) of a real element, certified by rational interval enclosure."""
    assert F.is_real(a)
    if F.is_zero(a):
        return 0
    if F.is_rational(a):
        return 1 if F.to_frac(a) > 0 else -1
    lo = Fraction(0)
    hi = Fraction(0)
    for k, x in enumerate(a[0]):
        if x:
            cl, ch = cos_bounds(F.n, k)
            if x > 0:
                lo += x * cl
                hi += x * ch
            else:
                lo += x * ch
                hi += x * cl
    if lo > 0:
        return 1
    if hi < 0:
        return -1
    raise RuntimeError("sign not certified at this precision")


# ---------------------------------------------------------------- matrices over a field

def eye(F, d):
    return [[F.one if i == j else F.zero for j in range(d)] for i in range(d)]


def zeros(F, d):
    return [[F.zero] * d for _ in range(d)]


def mat_mul(F, A, B):
    d = len(A)
    e = len(B[0])
    out = [[F.zero] * e for _ in range(d)]
    Bnz = [[(j, x) for j, x in enumerate(row) if any(x[0])] for row in B]
    for i in range(d):
        acc = {}
        for k, a in enumerate(A[i]):
            if any(a[0]):
                for j, b in Bnz[k]:
                    m = F.mul(a, b)
                    acc[j] = F.add(acc[j], m) if j in acc else m
        row = out[i]
        for j, v in acc.items():
            row[j] = v
    return out


def mat_vec(F, A, v):
    out = []
    nz = [(k, x) for k, x in enumerate(v) if any(x[0])]
    for i in range(len(A)):
        s = F.zero
        Ai = A[i]
        for k, x in nz:
            a = Ai[k]
            if any(a[0]):
                s = F.add(s, F.mul(a, x))
        out.append(s)
    return out


def adjoint(F, A):
    d = len(A)
    return [[F.conj(A[j][i]) for j in range(d)] for i in range(len(A[0]))]


def mat_add(F, A, B):
    return [[F.add(x, y) for x, y in zip(ra, rb)] for ra, rb in zip(A, B)]


def mat_sub(F, A, B):
    return [[F.sub(x, y) for x, y in zip(ra, rb)] for ra, rb in zip(A, B)]


def mat_scale(F, c, A):
    return [[F.mul(c, x) for x in row] for row in A]


def mat_eq(A, B):
    return all(x == y for ra, rb in zip(A, B) for x, y in zip(ra, rb))


def is_zero_mat(F, A):
    return all(F.is_zero(x) for row in A for x in row)


def mat_embed(Fbig, A, Fsmall):
    if Fbig.n == Fsmall.n:
        return A
    return [[Fbig.embed(x, Fsmall) for x in row] for row in A]


def vec_embed(Fbig, v, Fsmall):
    if Fbig.n == Fsmall.n:
        return v
    return [Fbig.embed(x, Fsmall) for x in v]


def proportional_scalar(F, A, B):
    """Return c with A = c B (B nonzero), or None."""
    c = None
    for ra, rb in zip(A, B):
        for x, y in zip(ra, rb):
            if not F.is_zero(y):
                c = F.div(x, y)
                break
        if c is not None:
            break
    if c is None:
        return None
    return c if mat_eq(A, mat_scale(F, c, B)) else None


def unitary_check(F, U):
    return mat_eq(mat_mul(F, U, adjoint(F, U)), eye(F, len(U)))


def mat_pow(F, A, k):
    R = eye(F, len(A))
    for _ in range(k):
        R = mat_mul(F, R, A)
    return R


# ============================================================================ classical layer (mod q)

def cmat_mul(A, B, q):
    n, m, r = len(A), len(B), len(B[0])
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(m)) % q for j in range(r)) for i in range(n))


def cmat_vec(A, v, q):
    return tuple(sum(a * x for a, x in zip(row, v)) % q for row in A)


def cmat_eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def cmat_T(A):
    return tuple(zip(*A))


def cmat_inv(A, q):
    n = len(A)
    M = [list(A[i]) + [int(i == j) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] % q)
        M[c], M[p] = M[p], M[c]
        iv = pow(M[c][c], -1, q)
        M[c] = [(x * iv) % q for x in M[c]]
        for r in range(n):
            if r != c and M[r][c]:
                f = M[r][c]
                M[r] = [(x - f * y) % q for x, y in zip(M[r], M[c])]
    return tuple(tuple(row[n:]) for row in M)


def cmat_det(A, q):
    n = len(A)
    M = [list(r) for r in A]
    det = 1
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] % q), None)
        if p is None:
            return 0
        if p != c:
            M[c], M[p] = M[p], M[c]
            det = -det
        det = det * M[c][c] % q
        iv = pow(M[c][c], -1, q)
        for r in range(c + 1, n):
            f = M[r][c] * iv % q
            M[r] = [(x - f * y) % q for x, y in zip(M[r], M[c])]
    return det % q


def symp_J(N, q):
    J = [[0] * (2 * N) for _ in range(2 * N)]
    for i in range(N):
        J[i][N + i] = 1
        J[N + i][i] = q - 1
    return tuple(tuple(r) for r in J)


def is_symplectic(g, N, q):
    J = symp_J(N, q)
    return cmat_mul(cmat_mul(cmat_T(g), J, q), g, q) == J


def leap_matrix(M, q):
    """z = (x, xi) = (current, previous):  x' = M x - xi,  xi' = x  (SM 3.1 leapfrog)."""
    N = len(M)
    L = [[0] * (2 * N) for _ in range(2 * N)]
    for i in range(N):
        for j in range(N):
            L[i][j] = M[i][j] % q
        L[i][N + i] = (-1) % q
        L[N + i][i] = 1
    return tuple(tuple(r) for r in L)


def cmat_order(g, q, bound=10000):
    I = cmat_eye(len(g))
    P = g
    for k in range(1, bound):
        if P == I:
            return k
        P = cmat_mul(P, g, q)
    raise RuntimeError("order bound")


def symmetric_couplings(q, N):
    out = []
    for e in itertools.product(range(q), repeat=N * (N + 1) // 2):
        M = [[0] * N for _ in range(N)]
        it = iter(e)
        for i in range(N):
            for j in range(i, N):
                v = next(it)
                M[i][j] = v
                M[j][i] = v
        out.append(tuple(tuple(r) for r in M))
    return out


def all_couplings(q, N):
    return [tuple(tuple(e[i * N:(i + 1) * N]) for i in range(N)) for e in itertools.product(range(q), repeat=N * N)]


def sp_order(N, q):
    o = q ** (N * N)
    for i in range(1, N + 1):
        o *= q ** (2 * i) - 1
    return o


def group_closure(gens, q, cap=None):
    I = cmat_eye(len(gens[0]))
    seen = {I}
    frontier = [I]
    order = [I]
    while frontier:
        new = []
        for g in frontier:
            for s in gens:
                h = cmat_mul(g, s, q)
                if h not in seen:
                    seen.add(h)
                    new.append(h)
                    order.append(h)
        frontier = new
        if cap and len(seen) > cap:
            break
    return order


def nullspace_mod(rows, nvars, q):
    """Basis of the nullspace mod q of a list of equations (lists of coefficients)."""
    M = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(nvars):
        p = next((i for i in range(r, len(M)) if M[i][c] % q), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        iv = pow(M[r][c], -1, q)
        M[r] = [(x * iv) % q for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % q:
                f = M[i][c]
                M[i] = [(x - f * y) % q for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(nvars) if c not in piv]
    basis = []
    for f in free:
        v = [0] * nvars
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-M[i][f]) % q
        basis.append(v)
    return basis


def find_commutator(g, group_list, N, q):
    """a, b in Sp(2N, q) with a b a^-1 b^-1 = g, searching a in a fixed order (deterministic)."""
    n = 2 * N
    for a in group_list:
        ai = cmat_inv(a, q)
        A2 = cmat_mul(ai, g, q)
        # unknown b (n x n, row-major): b ai - A2 b = 0
        rows = []
        for i in range(n):
            for j in range(n):
                row = [0] * (n * n)
                for k in range(n):
                    row[i * n + k] += ai[k][j]
                    row[k * n + j] -= A2[i][k]
                rows.append([x % q for x in row])
        basis = nullspace_mod(rows, n * n, q)
        for coeffs in itertools.product(range(q), repeat=len(basis)):
            if not any(coeffs):
                continue
            v = [sum(c * b[t] for c, b in zip(coeffs, basis)) % q for t in range(n * n)]
            b = tuple(tuple(v[i * n:(i + 1) * n]) for i in range(n))
            if cmat_det(b, q) and is_symplectic(b, N, q):
                comm = cmat_mul(cmat_mul(cmat_mul(a, b, q), cmat_inv(a, q), q), cmat_inv(b, q), q)
                assert comm == g
                return a, b
    return None


# ============================================================================ the quantum carrier


class Carrier:
    """C^{V^N}, V = Z/q, with the symmetric Weyl operators W(x, xi) = w^{-xi.x/2} Z^xi X^x."""

    def __init__(self, q, N, F):
        assert F.n % q == 0
        self.q, self.N, self.F = q, N, F
        self.d = q ** N
        self.pts = list(itertools.product(range(q), repeat=N))
        self.idx = {p: i for i, p in enumerate(self.pts)}
        self.h = pow(2, -1, q)
        self.om = [F.root(q, k) for k in range(q)]

    def padd(self, p, a):
        return tuple((x + y) % self.q for x, y in zip(p, a))

    def dot(self, a, b):
        return sum(x * y for x, y in zip(a, b)) % self.q

    def weyl_mono(self, x, xi):
        """W(x, xi)|p> = w^{xi.p + xi.x/2} |p + x>, as (target index, exponent) per column p."""
        q = self.q
        out = []
        for p in self.pts:
            e = (self.dot(xi, p) + self.h * self.dot(xi, x)) % q
            out.append((self.idx[self.padd(p, x)], e))
        return out

    def mono_matrix(self, mono):
        F = self.F
        A = zeros(F, self.d)
        for col, (t, e) in enumerate(mono):
            A[t][col] = self.om[e]
        return A

    def weyl(self, z):
        N = self.N
        return self.mono_matrix(self.weyl_mono(tuple(z[:N]), tuple(z[N:])))

    def unit_vectors(self):
        n = 2 * self.N
        return [tuple(int(i == j) for i in range(n)) for j in range(n)]

    def X(self, k):
        e = tuple(int(i == k) for i in range(self.N))
        return self.weyl(e + (0,) * self.N)

    def Z(self, k):
        e = tuple(int(i == k) for i in range(self.N))
        return self.weyl((0,) * self.N + e)

    def parity(self):
        F = self.F
        P = zeros(F, self.d)
        for p in self.pts:
            P[self.idx[tuple((-x) % self.q for x in p)]][self.idx[p]] = F.one
        return P

    def F0(self):
        F = self.F
        return [[self.om[self.dot(x, y)] for y in self.pts] for x in self.pts]

    def chirp(self, B):
        """diag(w^{y.B y / 2}): the image of the lower shear (x, xi) -> (x, xi + B x)."""
        F = self.F
        q = self.q
        D = zeros(F, self.d)
        for i, y in enumerate(self.pts):
            e = self.h * sum(B[a][b] * y[a] * y[b] for a in range(self.N) for b in range(self.N)) % q
            D[i][i] = self.om[e]
        return D

    def basis_vec(self, p):
        F = self.F
        v = [F.zero] * self.d
        v[self.idx[tuple(p)]] = F.one
        return v

    # ---- exact intertwiner space of a linear map g of V^{2N} (sparse elimination)
    def intertwiners(self, g):
        """All U with U W(e_j) = W(g e_j) U for the 2N unit vectors e_j; returns a basis."""
        F = self.F
        q, N, d = self.q, self.N, self.d
        eqs = []
        for z in self.unit_vectors():
            gz = cmat_vec(g, z, q)
            Wm = self.weyl_mono(tuple(z[:N]), tuple(z[N:]))
            Wp = self.weyl_mono(tuple(gz[:N]), tuple(gz[N:]))
            inv_t = [None] * d
            for c, (t, e) in enumerate(Wp):
                inv_t[t] = (c, e)
            for a in range(d):
                c, e2 = inv_t[a]
                for b in range(d):
                    t, e1 = Wm[b]
                    # w^{e1} U[a][t] - w^{e2} U[c][b] = 0
                    eqs.append(((a * d + t, e1), (c * d + b, e2)))
        return self._solve_monomial_system(eqs, d * d)

    def _solve_monomial_system(self, eqs, nvars):
        F = self.F
        # piv[var] = (free var or None, coeff): var = coeff * free  (None: var = 0)
        piv = {}
        refs = {}

        def resolve(v):
            if v in piv:
                return piv[v]
            return (v, F.one)

        for (v1, e1), (v2, e2) in eqs:
            f1, c1 = resolve(v1)
            f2, c2 = resolve(v2)
            a1 = F.mul(self.om[e1], c1) if f1 is not None else F.zero
            a2 = F.neg(F.mul(self.om[e2], c2)) if f2 is not None else F.zero
            terms = {}
            for f, a in ((f1, a1), (f2, a2)):
                if f is not None and not F.is_zero(a):
                    terms[f] = F.add(terms[f], a) if f in terms else a
            terms = {f: a for f, a in terms.items() if not F.is_zero(a)}
            if not terms:
                continue
            keys = sorted(terms)
            if len(keys) == 1:
                p, target = keys[0], (None, F.zero)
            else:
                p, o = keys[1], keys[0]
                target = (o, F.neg(F.div(terms[o], terms[p])))
            # p becomes a pivot: p = target ; substitute into pivots referencing p
            piv[p] = target
            if target[0] is not None:
                refs.setdefault(target[0], set()).add(p)
            for r in sorted(refs.pop(p, ())):
                fr, cr = piv[r]
                assert fr == p
                if target[0] is None:
                    piv[r] = (None, F.zero)
                else:
                    piv[r] = (target[0], F.mul(cr, target[1]))
                    refs.setdefault(target[0], set()).add(r)
        free = [v for v in range(nvars) if v not in piv]
        d = self.d
        basis = []
        for f in free:
            U = zeros(F, d)
            U[f // d][f % d] = F.one
            for v, (fv, c) in piv.items():
                if fv == f:
                    U[v // d][v % d] = c
            basis.append(U)
        return basis

    def apply_mono_vec(self, mono, v):
        F = self.F
        out = [F.zero] * self.d
        for col, (t, e) in enumerate(mono):
            if not F.is_zero(v[col]):
                out[t] = F.mul(self.om[e], v[col])
        return out


def canonical_weil(C):
    """The canonical Weil representation on the leaps.

    rho(lower shear (x, xi) -> (x, xi + B x)) = diag(w^{y.By/2})          (the chirp, no character)
    rho(J'),  J' = [[0, -I], [I, 0]]: forced by J' = up(-1) low(1) up(-1) with up(b) = J' low(-b) J'^-1,
    rho(L_M) = rho(J') rho(low(-M))  since  L_M = J' low(-M).
    Returns (rho_J, sign s, Gauss sum G) with rho_J = s^N G^-N F0.
    """
    F = C.F
    q = C.q
    C1 = Carrier(q, 1, F)
    G = F.zero
    for x in range(q):
        G = F.add(G, C1.om[(x * x) % q])
    F0 = C1.F0()
    F0inv = mat_scale(F, F.frac(Fraction(1, q)), adjoint(F, F0))

    def up(b):
        # rho(up(b)) = rho(J') rho(low(-b)) rho(J')^-1, independent of the normalization of rho(J')
        return mat_mul(F, mat_mul(F, F0, C1.chirp((((-b) % q,),))), F0inv)
    R = mat_mul(F, mat_mul(F, up(-1), C1.chirp(((1,),))), up(-1))
    c = proportional_scalar(F, R, F0)
    s = F.mul(c, G)
    assert s in (F.one, F.neg(F.one)), "J' normalization not +-1/G"
    sN = F.one if (C.N % 2 == 0 or s == F.one) else F.neg(F.one)
    GN = F.pow(G, C.N)
    rho_J = mat_scale(F, F.mul(sN, F.inv(GN)), C.F0())
    # classical identities used above
    J1 = ((0, q - 1), (1, 0))
    upm1 = ((1, q - 1), (0, 1))
    low1 = ((1, 0), (1, 1))
    assert cmat_mul(cmat_mul(upm1, low1, q), upm1, q) == J1
    return rho_J, s, G


def rho_leap(C, rho_J, M):
    q = C.q
    negM = tuple(tuple((-x) % q for x in row) for row in M)
    return mat_mul(C.F, rho_J, C.chirp(negM))


# ============================================================================ spectral calculus


def spectral(F, U, order):
    """Exact spectral projectors of U with U^order = I. Eigenvalues zeta_order^j.

    Distinct eigenvalues are found from the cyclic-group projectors (1/order) sum_k l^-k U^k;
    the projectors are then computed by Lagrange interpolation and checked equal to those, and
    checked to be a resolution of the identity by orthogonal projectors with U P = l P.
    """
    d = len(U)
    I = eye(F, d)
    pw = [I]
    for _ in range(1, order):
        pw.append(mat_mul(F, pw[-1], U))
    assert mat_eq(mat_mul(F, pw[-1], U), I), "U^order != I"
    four = {}
    for j in range(order):
        P = zeros(F, d)
        for k in range(order):
            P = mat_add(F, P, mat_scale(F, F.root(order, -j * k), pw[k]))
        P = mat_scale(F, F.frac(Fraction(1, order)), P)
        if not is_zero_mat(F, P):
            four[j] = P
    js = sorted(four)
    lam = {j: F.root(order, j) for j in js}
    out = []
    for j in js:
        P = I
        for l in js:
            if l != j:
                fac = mat_scale(F, F.inv(F.sub(lam[j], lam[l])), mat_sub(F, U, mat_scale(F, lam[l], I)))
                P = mat_mul(F, P, fac)
        assert mat_eq(P, four[j]), "Lagrange projector != cyclic projector"
        assert mat_eq(mat_mul(F, P, P), P)
        assert mat_eq(adjoint(F, P), P)
        assert mat_eq(mat_mul(F, U, P), mat_scale(F, lam[j], P))
        out.append((j, P))
    S = zeros(F, d)
    for _, P in out:
        S = mat_add(F, S, P)
    assert mat_eq(S, I)
    return out


def principal_theta(j, order):
    """Principal eigenphase / 2 pi of zeta_order^j, in (-1/2, 1/2]."""
    t = Fraction(j, order)
    return t if 2 * t <= 1 else t - 1


def cut_patterns(spec, order):
    """theta lists for each branch-cut position: c = 0..m-1 wraps the c largest eigenphases."""
    th = [principal_theta(j, order) for j, _ in spec]
    ordr = sorted(range(len(th)), key=lambda i: -th[i])
    pats = []
    for c in range(len(th)):
        t2 = list(th)
        for i in ordr[:c]:
            t2[i] -= 1
        pats.append(t2)
    return pats


def generator_from_thetas(F, spec, thetas):
    d = len(spec[0][1])
    G = zeros(F, d)
    for (j, P), t in zip(spec, thetas):
        if t != 0:
            G = mat_add(F, G, mat_scale(F, F.frac(t), P))
    return G


def sqrt_from(F, spec, order, thetas, signs):
    """sum_k s_k exp(i pi theta_k) P_k; exp(i pi theta) = zeta_(2 order)^(order theta)."""
    d = len(spec[0][1])
    V = zeros(F, d)
    for (j, P), t, s in zip(spec, thetas, signs):
        e = t * order
        assert e.denominator == 1
        c = F.root(2 * order, int(e))
        if s < 0:
            c = F.neg(c)
        V = mat_add(F, V, mat_scale(F, c, P))
    return V


# ============================================================================ exact Lie closure


def lie_closure_dim(F, gens, add_identity=True, stop_at=None):
    """K-dimension of the K-span of all iterated brackets of gens (and I if add_identity).

    K = Q(zeta_n); K-rank equals C-rank, so this is the complex dimension of the complex Lie
    algebra generated. Each generator is a list of square blocks (a block-diagonal matrix); the
    caller supplies the blocks, so the coordinates are the block entries only.
    """
    shapes = [len(b) for b in gens[0]]
    gl = list(gens)
    if add_identity:
        gl = gl + [[eye(F, s) for s in shapes]]
    basis = []

    def flat(X):
        return [x for blk in X for row in blk for x in row]

    def reduce(v):
        for p, row in basis:
            c = v[p]
            if not F.is_zero(c):
                v = [x if F.is_zero(y) else F.sub(x, F.mul(c, y)) for x, y in zip(v, row)]
        return v

    def bracket(A, B):
        return [mat_sub(F, mat_mul(F, a, b), mat_mul(F, b, a)) for a, b in zip(A, B)]

    queue = [("g", X) for X in gl]
    qi = 0
    while qi < len(queue):
        kind, item = queue[qi]
        qi += 1
        X = item if kind == "g" else bracket(item[0], item[1])
        v = reduce(flat(X))
        p = next((k for k, x in enumerate(v) if not F.is_zero(x)), None)
        if p is None:
            continue
        iv = F.inv(v[p])
        v = [F.mul(iv, x) if not F.is_zero(x) else x for x in v]
        basis.append((p, v))
        if stop_at is not None and len(basis) >= stop_at:
            break
        for g in gens:
            queue.append(("b", (g, X)))
    return len(basis)


# ============================================================================ helpers for the cells


def lcm(*xs):
    r = 1
    for x in xs:
        r = r * x // gcd(r, x)
    return r


_FIELDS = {}


def field(n):
    if n % 4 == 2:
        n //= 2
    if n not in _FIELDS:
        _FIELDS[n] = Cyc(n)
    return _FIELDS[n]


def out(*a):
    print(*a)


def header(t):
    out("")
    out("=" * 100)
    out(t)
    out("=" * 100)


def token(cell, size, tok):
    out("TOKEN %-34s %-12s %s" % (cell, size, tok))


def fmtM(M):
    return "[" + ";".join(",".join(str(x) for x in row) for row in M) + "]"


def fmt_pt(p):
    return "(" + ",".join(str(x) for x in p) + ")"


def ray_key(F, v):
    k = next(i for i, x in enumerate(v) if not F.is_zero(x))
    iv = F.inv(v[k])
    return tuple(F.mul(iv, x) for x in v)


def weyl_multiple(C, A):
    """(x, xi) if A is proportional to W(x, xi), else None (exact)."""
    F = C.F
    col0 = [i for i in range(C.d) if not F.is_zero(A[i][0])]
    if len(col0) != 1:
        return None
    x = C.pts[col0[0]]
    for xi in C.pts:
        W = C.mono_matrix(C.weyl_mono(x, xi))
        if proportional_scalar(F, A, W) is not None:
            return (x, xi)
    return None


def normalizer_failures(C, V):
    """Generators W(e_j) whose conjugate V W V^dagger is proportional to no Weyl operator."""
    F = C.F
    Vd = adjoint(F, V)
    fails = []
    for k in range(C.N):
        for name, Wm in (("X_%d" % (k + 1), C.X(k)), ("Z_%d" % (k + 1), C.Z(k))):
            A = mat_mul(F, mat_mul(F, V, Wm), Vd)
            if weyl_multiple(C, A) is None:
                fails.append(name)
    return fails


def parity_basis(C):
    """Columns |0>, |p>+|-p>, |p>-|-p> (rational); returns S, S^-1, n_even."""
    F = C.F
    d = C.d
    reps = []
    seen = set()
    for p in C.pts:
        if p in seen:
            continue
        m = tuple((-x) % C.q for x in p)
        seen.add(p)
        seen.add(m)
        if p != m:
            reps.append((p, m))
    cols = [[F.one if i == C.idx[(0,) * C.N] else F.zero for i in range(d)]]
    plus, minus = [], []
    for p, m in reps:
        v = [F.zero] * d
        v[C.idx[p]] = F.one
        v[C.idx[m]] = F.one
        plus.append(v)
        w = [F.zero] * d
        w[C.idx[p]] = F.one
        w[C.idx[m]] = F.neg(F.one)
        minus.append(w)
    cols = cols + plus + minus
    S = [[cols[j][i] for j in range(d)] for i in range(d)]
    Sinv = [[F.mul(cols[i][j], F.frac(Fraction(1, 1 if i == 0 else 2))) for j in range(d)] for i in range(d)]
    assert mat_eq(mat_mul(F, Sinv, S), eye(F, d))
    return S, Sinv, 1 + len(plus)


def to_blocks(F, S, Sinv, ne, G):
    H = mat_mul(F, mat_mul(F, Sinv, G), S)
    d = len(H)
    for i in range(d):
        for j in range(d):
            if (i < ne) != (j < ne):
                assert F.is_zero(H[i][j]), "generator does not commute with the parity"
    return [[row[:ne] for row in H[:ne]], [row[ne:] for row in H[ne:]]]


def mono_compose(C, m2, m1):
    return [(m2[t1][0], (e1 + m2[t1][1]) % C.q) for (t1, e1) in m1]


def wigner(C, v):
    """W(z) = q^-N <v|A(z)|v> / <v|v>, A(z) = W(z) Par W(z)^dagger (Gross's odd-q Wigner function)."""
    F = C.F
    N = C.N
    par = [(C.idx[tuple((-x) % C.q for x in p)], 0) for p in C.pts]
    nrm = F.zero
    for x in v:
        if not F.is_zero(x):
            nrm = F.add(nrm, F.mul(x, F.conj(x)))
    scale = F.inv(F.mul(nrm, F.frac(C.q ** N)))
    vc = [F.conj(x) for x in v]
    W = {}
    for z in itertools.product(range(C.q), repeat=2 * N):
        x, xi = z[:N], z[N:]
        Wp = C.weyl_mono(x, xi)
        Wm = C.weyl_mono(tuple((-a) % C.q for a in x), tuple((-a) % C.q for a in xi))
        A = mono_compose(C, Wp, mono_compose(C, par, Wm))
        s = F.zero
        for col, (t, e) in enumerate(A):
            if not F.is_zero(v[col]) and not F.is_zero(vc[t]):
                s = F.add(s, F.mul(vc[t], F.mul(C.om[e], v[col])))
        W[z] = F.mul(s, scale)
    return W


def born(F, v):
    return [F.mul(x, F.conj(x)) for x in v]


# ============================================================================ C1, C2: words, Born law, two-time law


def classical_marginal(C, A, b, x0):
    """Rooted law of the current component: x0 registered, previous component uniform (Lemma 3)."""
    q, N = C.q, C.N
    cnt = {}
    for xi in C.pts:
        z = tuple(x0) + tuple(xi)
        z2 = tuple((s + t) % q for s, t in zip(cmat_vec(A, z, q), b))
        x = z2[:N]
        cnt[x] = cnt.get(x, 0) + 1
    return [Fraction(cnt.get(p, 0), q ** N) for p in C.pts]


def c1_words(C, U, L, maxlen=6, early=False, collect=None, sums=None):
    """Every word of length <= maxlen over {L} u {tau_1..tau_N}, from every registered x0.

    Returns (ok, first counterexample, counts per length)."""
    F = C.F
    q, N = C.q, C.N
    n2 = 2 * N
    letters = [("L", U, L, (0,) * n2)]
    for k in range(N):
        e = tuple(int(i == k) for i in range(N)) + (0,) * N
        letters.append(("t%d" % (k + 1), C.X(k), cmat_eye(n2), e))
    I2 = cmat_eye(n2)
    starts = [C.basis_vec(p) for p in C.pts]
    level = [((), I2, (0,) * n2, starts)]
    counts = [1]
    first = None
    ok = True

    def check(word, A, b, states):
        nonlocal ok, first
        for x0, v in zip(C.pts, states):
            pb = born(F, v)
            if sums is not None:
                s = F.zero
                for x in pb:
                    s = F.add(s, x)
                sums.append(s == F.one)
            pc = classical_marginal(C, A, b, x0)
            if any(x != F.frac(y) for x, y in zip(pb, pc)):
                ok = False
                if first is None:
                    first = (word, x0, [F.show(x) for x in pb], [str(y) for y in pc])
                if early:
                    return False
            if collect is not None:
                collect.setdefault(ray_key(F, v), v)
        return True

    check((), I2, (0,) * n2, starts)
    for ln in range(1, maxlen + 1):
        new = []
        for (word, A, b, states) in level:
            for name, Um, Lm, tv in letters:
                A2 = cmat_mul(Lm, A, q)
                b2 = tuple((s + t) % q for s, t in zip(cmat_vec(Lm, b, q), tv))
                st2 = [mat_vec(F, Um, v) for v in states]
                w2 = word + (name,)
                if not check(w2, A2, b2, st2) and early:
                    return ok, first, counts
                new.append((w2, A2, b2, st2))
        counts.append(len(new))
        level = new
    return ok, first, counts


def intertwines(C, U, L):
    F = C.F
    Ud = adjoint(F, U)
    for z in C.unit_vectors():
        if not mat_eq(mat_mul(F, mat_mul(F, U, C.weyl(z)), Ud), C.weyl(cmat_vec(L, z, C.q))):
            return False
    return True


def two_time(Cs, U_sys, L_sys, k, x0):
    """System N sites + one meter site (index N). Protocol: leap, meter coupling, register meter,
    leap, register the system's current component. Meter: x_m += x_k, xi_k -= xi_m (symplectic).
    Returns (classical joint law, Born joint law, post-registration meter-conjugate marginals)."""
    F = Cs.F
    q, N = Cs.q, Cs.N - 1
    n = N + 1
    # classical maps on z = (x_1..x_N, x_m, xi_1..xi_N, xi_m)
    Lb = [[0] * (2 * n) for _ in range(2 * n)]
    for i in range(N):
        for j in range(N):
            Lb[i][j] = L_sys[i][j]
            Lb[i][n + j] = L_sys[i][N + j]
            Lb[n + i][j] = L_sys[N + i][j]
            Lb[n + i][n + j] = L_sys[N + i][N + j]
    Lb[N][N] = 1
    Lb[n + N][n + N] = 1
    Lb = tuple(tuple(r) for r in Lb)
    Cm = [[int(i == j) for j in range(2 * n)] for i in range(2 * n)]
    Cm[N][k] = 1                       # x_m += x_k
    Cm[n + k][n + N] = q - 1            # xi_k -= xi_m
    Cm = tuple(tuple(r) for r in Cm)
    assert is_symplectic(Cm, n, q) and is_symplectic(Lb, n, q)
    Jc = {}
    for xis in itertools.product(range(q), repeat=N):
        for xim in range(q):
            z = tuple(x0) + (0,) + tuple(xis) + (xim,)
            z = cmat_vec(Lb, z, q)
            z = cmat_vec(Cm, z, q)
            rec = z[N]
            z = cmat_vec(Lb, z, q)
            key = (rec, tuple(z[:N]))
            Jc[key] = Jc.get(key, 0) + Fraction(1, q ** n)
    # quantum: U_sys (x) I_meter ; meter coupling image |x, m> -> |x, m + x_k>
    d = Cs.d
    dm = q ** N

    def apply_sys(v):
        outv = [F.zero] * d
        for m in range(q):
            sl = [v[Cs.idx[p + (m,)]] for p in itertools.product(range(q), repeat=N)]
            r = mat_vec(F, U_sys, sl)
            for i, p in enumerate(itertools.product(range(q), repeat=N)):
                outv[Cs.idx[p + (m,)]] = r[i]
        return outv
    Uc = zeros(F, d)
    for p in Cs.pts:
        p2 = p[:N] + ((p[N] + p[k]) % q,)
        Uc[Cs.idx[p2]][Cs.idx[p]] = F.one
    sols = Cs.intertwiners(Cm)
    assert len(sols) == 1 and proportional_scalar(F, Uc, sols[0]) is not None
    v = Cs.basis_vec(tuple(x0) + (0,))
    v = apply_sys(v)
    v = mat_vec(F, Uc, v)
    Jq = {}
    post = []
    for rec in range(q):
        proj = [v[i] if Cs.pts[i][N] == rec else F.zero for i in range(d)]
        if all(F.is_zero(x) for x in proj):
            continue
        post.append((rec, proj))
        w = apply_sys(proj)
        for i, p in enumerate(Cs.pts):
            key = (rec, p[:N])
            Jq[key] = F.add(Jq.get(key, F.zero), F.mul(w[i], F.conj(w[i])))
    return Jc, Jq, post, Uc


# ============================================================================ the run for one size


def summary_tag(flags):
    if all(flags):
        return "ALL"
    if not any(flags):
        return "NONE"
    return "SOME"


def run_size(q, N, R):
    size = "q=%d,N=%d" % (q, N)
    res = R.setdefault(size, {})
    Fq = field(q)
    C = Carrier(q, N, Fq)
    d = C.d
    Ms = symmetric_couplings(q, N)
    Ls = {M: leap_matrix(M, q) for M in Ms}
    ords = {M: cmat_order(Ls[M], q) for M in Ms}

    # ------------------------------------------------------------------ W0: the canonical images
    header("[%s] W0  canonical Weil images of the leaps (amendment A1)" % size)
    rho_J, s, G = canonical_weil(C)
    out("Gauss sum G = sum_x w^(x^2) = %s, G^2 = %s; sign of rho(J') at one site s = %s" %
        (Fq.show(G), Fq.show(Fq.mul(G, G)), Fq.show(s)))
    U = {M: rho_leap(C, rho_J, M) for M in Ms}
    w0_ok = True
    for M in Ms:
        un = unitary_check(Fq, U[M])
        it = intertwines(C, U[M], Ls[M])
        po = mat_eq(mat_pow(Fq, U[M], ords[M]), eye(Fq, d))
        w0_ok &= un and it and po
    out("every symmetric coupling (%d): image unitary, U W(z) U^+ = W(L z) exactly, U^ord(L) = I: %s"
        % (len(Ms), w0_ok))
    out("orders of L_M: " + " ".join("%s:%d" % (fmtM(M), ords[M]) for M in Ms))
    perfect = not (N == 1 and q == 3)
    gen_ok = True
    if N == 1:
        def key(A):
            return tuple(x for r in A for x in r)
        I = eye(Fq, d)
        seen = {key(I)}
        fr = [I]
        gens = [U[M] for M in Ms]
        while fr:
            nw = []
            for A in fr:
                for g in gens:
                    B = mat_mul(Fq, A, g)
                    kk = key(B)
                    if kk not in seen:
                        seen.add(kk)
                        nw.append(B)
            fr = nw
        out("matrix group generated by the images: order %d; |SL(2,%d)| = %d" % (len(seen), q, sp_order(1, q)))
        gen_ok &= len(seen) == sp_order(1, q)
    grp = group_closure([Ls[M] for M in Ms], q)
    if perfect:
        def uinv(Ux):
            c = mat_mul(Fq, Ux, adjoint(Fq, Ux))[0][0]
            return mat_scale(Fq, Fq.inv(c), adjoint(Fq, Ux))
        nc = 0
        for M in Ms:
            a, b = find_commutator(Ls[M], grp, N, q)
            Ua = C.intertwiners(a)[0]
            Ub = C.intertwiners(b)[0]
            Cm = mat_mul(Fq, mat_mul(Fq, mat_mul(Fq, Ua, Ub), uinv(Ua)), uinv(Ub))
            nc += mat_eq(Cm, U[M])
        out("Sp(%d,%d) is perfect: the genuine lift is unique and equals [U_a,U_b] for any a,b with "
            "[a,b] = L_M, for any phases of U_a, U_b." % (2 * N, q))
        out("commutator certificates: image equals the commutator lift for %d of %d couplings" % (nc, len(Ms)))
        gen_ok &= nc == len(Ms)
    else:
        out("Sp(2,3) = SL(2,3) is not perfect (abelianization Z/3): three genuine lifts exist; the "
            "canonical one is fixed by the explicit chirp formula rho(low(b)) = diag(w^(b y^2/2)).")
    out("canonical images form a genuine representation (exact): %s" % gen_ok)
    res["W0"] = w0_ok and gen_ok

    # ------------------------------------------------------------------ C1
    header("[%s] C1  consistency: intertwiner spaces, Born law = rooted visible law, two-time law" % size)
    dims = {M: len(C.intertwiners(Ls[M])) for M in Ms}
    c1a = all(v == 1 for v in dims.values())
    out("(i) intertwiner-space dimension per symmetric coupling: " +
        " ".join("%s:%d" % (fmtM(M), dims[M]) for M in Ms))
    sums = []
    rays = {}
    c1b = True
    first = None
    counts = None
    out("(ii) alphabet per coupling M: {L_M} u {tau_1..tau_%d}, tau_k: x_k -> x_k + 1 (image X_k); "
        "initial states: every registered x0 in V^%d (%d); previous component uniform" % (N, N, d))
    for M in Ms:
        ok, fst, cnts = c1_words(C, U[M], Ls[M], collect=rays, sums=sums)
        counts = cnts
        c1b &= ok
        if fst and first is None:
            first = (M, fst)
        out("    M=%s alphabet size %d: words per length 0..6 = %s, total %d, Born = classical on all: %s"
            % (fmtM(M), N + 1, cnts, sum(cnts), ok))
    if first:
        out("    first counterexample:", first)
    out("    words checked over all couplings: %d (x %d initial states)" % (len(Ms) * sum(counts), d))
    # two-time law
    Cs = Carrier(q, N + 1, Fq)
    c1c = True
    post_meter = []
    out("(iii) symplectic meter: one meter site m, x_m := x_m + x_k, xi_k := xi_k - xi_m (image: the "
        "permutation |x, x_m> -> |x, x_m + x_k>); protocol leap, meter, register x_m, leap, register x")
    tt_sums = []
    for M in Ms:
        for k in range(N):
            for x0 in C.pts:
                Jc, Jq, post, _ = two_time(Cs, U[M], Ls[M], k, x0)
                keys = set(Jc) | set(Jq)
                eq = all(Jq.get(kk, Fq.zero) == Fq.frac(Jc.get(kk, 0)) for kk in sorted(keys))
                c1c &= eq
                tot = Fq.zero
                for kk in sorted(Jq):
                    tot = Fq.add(tot, Jq[kk])
                tt_sums.append(tot == Fq.one)
                post_meter.extend(post)
    out("    two-time joint law (record, final x) equal as exact rationals for every M, every meter "
        "site k, every x0: %s (%d protocols)" % (c1c, len(Ms) * N * d))
    c1 = c1a and c1b and c1c
    res["C1"] = c1
    token("C1", size, "E1-CONSISTENT" if c1 else "E1-INCONSISTENT")

    # ------------------------------------------------------------------ C2
    header("[%s] C2  normalization and back-action" % size)
    s_ok = all(sums) and all(tt_sums)
    out("registration probabilities sum to 1 exactly: %d of %d word states, %d of %d two-time laws"
        % (sum(sums), len(sums), sum(tt_sums), len(tt_sums)))
    ba_ok = True
    nchk = 0
    for key_, v in sorted(rays.items()):
        for k in range(N):
            for xval in range(q):
                proj = [v[i] if C.pts[i][k] == xval else Fq.zero for i in range(d)]
                if all(Fq.is_zero(x) for x in proj):
                    continue
                W = wigner(C, proj)
                marg = {}
                for z, w in W.items():
                    marg[z[N + k]] = Fq.add(marg.get(z[N + k], Fq.zero), w)
                ba_ok &= all(marg[t] == Fq.frac(Fraction(1, q)) for t in range(q))
                nchk += 1
    out("distinct tested rays: %d; post-registration states checked: %d; conjugate-component "
        "(previous) marginal of the Wigner function = counting measure 1/%d: %s" % (len(rays), nchk, q, ba_ok))
    Cs_meter_ok = True
    for rec, proj in post_meter:
        W = wigner(Cs, proj)
        marg = {}
        for z, w in W.items():
            marg[z[2 * (N + 1) - 1]] = Fq.add(marg.get(z[2 * (N + 1) - 1], Fq.zero), w)
        Cs_meter_ok &= all(marg[t] == Fq.frac(Fraction(1, q)) for t in range(q))
    out("meter registrations in the two-time protocols: %d; meter conjugate marginal = 1/%d: %s"
        % (len(post_meter), q, Cs_meter_ok))
    c2 = s_ok and ba_ok and Cs_meter_ok
    res["C2"] = c2
    token("C2", size, "E1-NORMALIZED-BACKACTING" if c2 else "E1-NOT-NORMALIZED-BACKACTING")

    # ------------------------------------------------------------------ spectral data
    def spec_of(Uop, order, Fbig):
        return spectral(Fbig, mat_embed(Fbig, Uop, Fq), order)

    full = d * d

    # ------------------------------------------------------------------ C3(a)
    header("[%s] C3(a)  all durations: Lie algebra of the principal-logarithm generators (A1, A3)" % size)
    out("convention: leaps by the canonical Weil representation (A1); position translations by the symmetric "
        "Weyl operators X_k = W(e_k, 0) (order q, det 1); principal branch, eigenphases in (-pi, pi]")
    if N == 1:
        S_leaps = [((0,),)]
    else:
        S_leaps = [((0, 1), (1, 0))]
    S_name = "{L_%s, tau_1}" % fmtM(S_leaps[0])
    Fa = field(lcm(q, *[ords[M] for M in S_leaps]))
    out("generating subset S = %s of the C3(a) repertoire; field Q(zeta_%d), degree %d" % (S_name, Fa.n, Fa.deg))
    out("  (the repertoire's algebra contains the algebra of any subset; a full dimension on S is the "
        "repertoire's dimension, and the derived algebra does not change under central shifts, so a full "
        "result for every convention of S holds for every convention of every repertoire element)")
    specL = {M: spec_of(U[M], ords[M], Fa) for M in S_leaps}
    specX = spectral(Fa, mat_embed(Fa, C.X(0), Fq), q)
    patsL = [cut_patterns(specL[M], ords[M]) for M in S_leaps]
    patsX = cut_patterns(specX, q)
    flags = []
    flagsA1 = []
    dim_can = None
    for combo in itertools.product(*([range(len(p)) for p in patsL] + [range(len(patsX))])):
        gens = [generator_from_thetas(Fa, specL[M], patsL[i][c]) for i, (M, c) in enumerate(zip(S_leaps, combo))]
        gens.append(generator_from_thetas(Fa, specX, patsX[combo[-1]]))
        dm = lie_closure_dim(Fa, [[g] for g in gens], stop_at=full)
        flags.append(dm == full)
        if combo[-1] == 0:
            flagsA1.append(dm == full)
        if not any(combo):
            dim_can = dm
        out("  S with branch-cut positions (leap %s, tau_1 %d): dim modulo identity %d"
            % (",".join(str(c) for c in combo[:-1]), combo[-1], dm - 1))
    out("canonical convention (cut positions all 0): dim(L + C I) = %d, dimension modulo the identity = %d; "
        "q^{2N} - 1 = %d" % (dim_can, dim_can - 1, full - 1))
    full_can = dim_can == full
    res["C3a"] = full_can
    tagA1 = summary_tag(flagsA1)
    tag = summary_tag(flags)
    out("A1 scan (every global phase of the leap, translation canonical): %s [%d of %d full]"
        % (tagA1, sum(flagsA1), len(flagsA1)))
    out("extended scan (every global phase of the leap and of the translation, jointly): %s [%d of %d full]"
        % (tag, sum(flags), len(flags)))
    res["C3a_scan"] = tagA1
    res["C3a_scan_ext"] = tag
    token("C3(a)", size, ("E1-FULL-ALGEBRA" if full_can else "E1-NOT-FULL-ALGEBRA") +
          " [canonical; A1 scan %s; extended scan %s]" % (tagA1, tag))
    if N == 1:
        Fall = field(lcm(q, *[ords[M] for M in Ms]))
        gens = []
        for M in Ms:
            spm = spec_of(U[M], ords[M], Fall)
            gens.append(generator_from_thetas(Fall, spm, [principal_theta(j, ords[M]) for j, _ in spm]))
        spx = spectral(Fall, mat_embed(Fall, C.X(0), Fq), q)
        gens.append(generator_from_thetas(Fall, spx, [principal_theta(j, q) for j, _ in spx]))
        dm = lie_closure_dim(Fall, [[g] for g in gens], stop_at=full)
        out("supporting: canonical convention on {L_M for every M, tau_1} (field Q(zeta_%d)): dim modulo identity %d"
            % (Fall.n, dm - 1))
    if N == 2:
        # supporting: the zero-coupling leap of two uncoupled sites against the local-sum control
        M0 = ((0, 0), (0, 0))
        Fz = field(lcm(q, 4))
        C1q = Carrier(q, 1, Fq)
        U1 = rho_leap(C1q, canonical_weil(C1q)[0], ((0,),))
        out("supporting: U_[0,0;0,0] = rho(J') (x) rho(J') exactly: %s" % mat_eq(U[M0], kron(Fq, U1, U1)))
        sp2 = spec_of(U[M0], 4, Fz)
        sp1 = spectral(Fz, mat_embed(Fz, U1, Fq), 4)
        I3 = eye(Fz, q)
        Id = eye(Fz, d)
        loc_any = False
        for t2 in cut_patterns(sp2, 4):
            G2 = generator_from_thetas(Fz, sp2, t2)
            for ta in cut_patterns(sp1, 4):
                for tb in cut_patterns(sp1, 4):
                    ga = generator_from_thetas(Fz, sp1, ta)
                    gb = generator_from_thetas(Fz, sp1, tb)
                    diff = mat_sub(Fz, G2, mat_add(Fz, kron(Fz, ga, I3), kron(Fz, I3, gb)))
                    if is_zero_mat(Fz, diff) or proportional_scalar(Fz, diff, Id) is not None:
                        loc_any = True
        out("supporting: for some global phase of the two-site uncoupled leap and some global phases of the "
            "one-site leaps, its principal log is a local sum g_a (x) I + I (x) g_b + cI: %s" % loc_any)
        spx2 = [spectral(Fz, mat_embed(Fz, C.X(k), Fq), q) for k in range(N)]
        GX2 = [generator_from_thetas(Fz, p_, [principal_theta(j, q) for j, _ in p_]) for p_ in spx2]
        g1 = generator_from_thetas(Fz, sp1, [principal_theta(j, 4) for j, _ in sp1])
        G0 = generator_from_thetas(Fz, sp2, [principal_theta(j, 4) for j, _ in sp2])
        dm_loc = lie_closure_dim(Fz, [[g] for g in [kron(Fz, g1, I3), kron(Fz, I3, g1)] + GX2], stop_at=full)
        dm_0 = lie_closure_dim(Fz, [[g] for g in [G0] + GX2], stop_at=full)
        out("supporting: dim modulo identity of {g (x) I, I (x) g, tau_1, tau_2} = %d; of {principal log of "
            "L_[0,0;0,0], tau_1, tau_2} = %d" % (dm_loc - 1, dm_0 - 1))
        res["N2_uncoupled_log_local_any"] = loc_any
        res["N2_uncoupled_dims"] = (dm_loc - 1, dm_0 - 1)

    # ------------------------------------------------------------------ C3(b) and K6(b)
    header("[%s] C3(b)  leaps alone: parity superselection; K6(b) dropped-generator mutation" % size)
    Par = C.parity()
    comm = all(mat_eq(mat_mul(Fq, U[M], Par), mat_mul(Fq, Par, U[M])) for M in Ms)
    S, Sinv, ne = parity_basis(C)
    no = d - ne
    out("every leap image commutes with the parity x -> -x exactly: %s; spectral projectors and every "
        "principal logarithm are polynomials in the image, so the generated algebra commutes with it" % comm)
    out("parity blocks: even %d, odd %d; exact upper bound dim <= %d^2 + %d^2 = %d (modulo identity %d) < %d"
        % (ne, no, ne, no, ne * ne + no * no, ne * ne + no * no - 1, full - 1))
    Fb = field(lcm(q, *[ords[M] for M in Ms]))
    out("leaps-only repertoire (every symmetric coupling, no translation, no source term), field "
        "Q(zeta_%d) degree %d" % (Fb.n, Fb.deg))
    gens_b = []
    for M in Ms:
        Fm = field(lcm(q, ords[M]))
        spm = spectral(Fm, mat_embed(Fm, U[M], Fq), ords[M])
        Gm = generator_from_thetas(Fm, spm, [principal_theta(j, ords[M]) for j, _ in spm])
        Gm = mat_embed(Fb, Gm, Fm)
        Cb = Carrier(q, N, Fb)
        Sb, Sbinv, _ = parity_basis(Cb)
        gens_b.append(to_blocks(Fb, Sb, Sbinv, ne, Gm))
    dim_b = lie_closure_dim(Fb, gens_b)
    out("exact dimension of the leaps-only algebra (C3(a)'s computation on the mutated repertoire): "
        "dim(L + C I) = %d, modulo identity %d" % (dim_b, dim_b - 1))
    c3b = comm and dim_b <= ne * ne + no * no
    res["C3b"] = c3b
    token("C3(b)", size, "E1-PARITY-SUPERSELECTED" if c3b else "E1-NOT-SUPERSELECTED")
    k6b = (dim_b - 1) < full - 1
    res["K6b"] = k6b
    token("K6(b) dropped generators", size, "DETECTED" if k6b else "NOT-DETECTED (control fails)")

    # ------------------------------------------------------------------ (c1)
    header("[%s] C3(c1)  Clifford generation, exact" % size)
    out("Sp(2N,q) order formula: %d; group generated by the %d leap matrices: %d"
        % (sp_order(N, q), len(Ms), len(grp)))
    span_rows = []
    for g in grp:
        for k in range(N):
            span_rows.append(cmat_vec(g, tuple(int(i == k) for i in range(N)) + (0,) * N, q))
    span_rows = sorted(set(span_rows))
    rank = 2 * N - len(nullspace_mod([list(r) for r in span_rows], 2 * N, q))
    out("span of the orbit of the position translations under the generated group: rank %d of %d" % (rank, 2 * N))
    irr = len(C.intertwiners(cmat_eye(2 * N))) == 1
    out("commutant of the Weyl operators is the scalars (exact, Schur): %s" % irr)
    c1_ok = len(grp) == sp_order(N, q) and rank == 2 * N and irr
    out("group generated modulo phases has order q^{2N} |Sp(2N,q)| = %d: %s" % (q ** (2 * N) * sp_order(N, q), c1_ok))
    if N == 2:
        diag = [Ls[M] for M in Ms if M[0][1] == 0]
        out("countercontrol: diagonal couplings only (no cross-site coupling) generate order %d"
            % len(group_closure(diag, q)))
    if N == 1:
        def pkey(A):
            return ray_key(Fq, [x for r in A for x in r])
        I = eye(Fq, d)
        seen = {pkey(I)}
        fr = [I]
        gens = [U[M] for M in Ms] + [C.X(0)]
        while fr:
            nw = []
            for A in fr:
                for g in gens:
                    B = mat_mul(Fq, A, g)
                    kk = pkey(B)
                    if kk not in seen:
                        seen.add(kk)
                        nw.append(B)
            fr = nw
        out("direct cross-check: matrix group generated by the images and tau, modulo phases: order %d" % len(seen))
        c1_ok &= len(seen) == q ** 2 * sp_order(1, q)
    res["c1"] = c1_ok
    token("C3(c1)", size, "CLIFFORD-GENERATED" if c1_ok else "NOT-CLIFFORD-GENERATED")

    # ------------------------------------------------------------------ (c2)
    header("[%s] C3(c2)  named non-Clifford gate: the zero-coupling leap at t = 1/2" % size)
    M0 = Ms[0]
    assert all(x == 0 for r in M0 for x in r)
    o0 = ords[M0]
    Fc = field(lcm(q, 2 * o0))
    Cc = Carrier(q, N, Fc)
    sp0 = spec_of(U[M0], o0, Fc)
    th0 = [principal_theta(j, o0) for j, _ in sp0]
    out("U_0 = canonical image of L_0 (M = 0), order %d; field Q(zeta_%d); eigenphases/2pi %s"
        % (o0, Fc.n, [str(t) for t in th0]))
    V0 = sqrt_from(Fc, sp0, o0, th0, [1] * len(sp0))
    assert unitary_check(Fc, V0) and mat_eq(mat_mul(Fc, V0, V0), mat_embed(Fc, U[M0], Fq))
    ctrl = all(not normalizer_failures(Cc, mat_embed(Fc, U[M], Fq)) for M in Ms) and \
        not normalizer_failures(Cc, Cc.X(0))
    out("positive control: every integer-time image and tau_1 normalize the Weyl group: %s" % ctrl)
    nf = normalizer_failures(Cc, V0)
    out("canonical principal square root V (V^2 = U_0, unitary): V W V^+ proportional to no Weyl operator for %s"
        % (nf if nf else "none"))
    c2 = bool(nf) and ctrl
    res["c2"] = c2
    # scans
    cutf = []
    for t in cut_patterns(sp0, o0):
        cutf.append(bool(normalizer_failures(Cc, sqrt_from(Fc, sp0, o0, t, [1] * len(sp0)))))
    sgnf = []
    for sg in itertools.product((1, -1), repeat=len(sp0) - 1):
        sgnf.append(bool(normalizer_failures(Cc, sqrt_from(Fc, sp0, o0, th0, (1,) + sg))))
    out("scan, every global phase (branch-cut positions %d): non-Clifford %s" % (len(cutf), cutf))
    out("scan, every square root modulo global phase (%d sign patterns): non-Clifford %s" % (len(sgnf), sgnf))
    res["c2_scan"] = (summary_tag(cutf), summary_tag(sgnf))
    token("C3(c2)", size, ("E1-ONE-DURATION-NONCLIFFORD" if c2 else "E1-HALF-PERIOD-CLIFFORD") +
          " [canonical; global-phase scan %s; square-root scan %s]" % res["c2_scan"])
    # supporting: every coupling's half-leap (canonical)
    per = []
    for M in Ms:
        Fm = field(lcm(q, 2 * ords[M]))
        Cm_ = Carrier(q, N, Fm)
        spm = spectral(Fm, mat_embed(Fm, U[M], Fq), ords[M])
        Vm = sqrt_from(Fm, spm, ords[M], [principal_theta(j, ords[M]) for j, _ in spm], [1] * len(spm))
        per.append((M, bool(normalizer_failures(Cm_, Vm))))
    out("supporting: canonical half-leap non-Clifford per coupling: " +
        " ".join("%s:%s" % (fmtM(M), "Y" if f else "n") for M, f in per))
    res["c2_percoupling"] = summary_tag([f for _, f in per])
    if not c2:
        res["need_other_durations"] = True
    if N == 2:
        U1 = rho_leap(Carrier(q, 1, Fq), canonical_weil(Carrier(q, 1, Fq))[0], ((0,),))
        sp1 = spectral(Fc, mat_embed(Fc, U1, Fq), 4)
        V1 = sqrt_from(Fc, sp1, 4, [principal_theta(j, 4) for j, _ in sp1], [1] * len(sp1))
        prodV = kron(Fc, V1, V1)
        out("supporting: two-site canonical half-leap equals the product of one-site half-leaps up to "
            "phase: %s; operator-Schmidt rank of V across the two sites: %d"
            % (proportional_scalar(Fc, V0, prodV) is not None, schmidt_rank(Fc, V0, q)))
        ranks = [schmidt_rank(Fc, sqrt_from(Fc, sp0, o0, th0, (1,) + sg), q)
                 for sg in itertools.product((1, -1), repeat=len(sp0) - 1)]
        out("supporting: operator-Schmidt rank of every square root of U_[0,0;0,0] modulo global phase: %s "
            "(rank 1 = product of one-site gates)" % ranks)
        res["N2_halfleap_ranks"] = ranks

    # ------------------------------------------------------------------ (c3)
    header("[%s] C3(c3)  density by literature [L]" % size)
    out("[L] statement used, as quoted in amendment 1 (A2): Campbell, Anwar, Browne, Phys. Rev. X 2, 041021 "
        "(2012), Appendix D: for odd prime dimension, the Clifford group together with any non-Clifford "
        "gate is dense. The source text was not retrievable in this environment (no network route).")
    hyp = [("q odd prime", q % 2 == 1 and all(q % p for p in range(2, q))),
           ("full Clifford group on N qudits (c1)", c1_ok),
           ("a non-Clifford gate (c2)", c2)]
    for n_, v in hyp:
        out("  hypothesis %-40s %s" % (n_, v))
    out("  Hilbert-space dimension q^N = %d is %s" % (d, "prime" if N == 1 else "not prime: the quoted statement "
        "applies only if 'dimension' means the qudit dimension q; not checked against the source"))
    c3 = all(v for _, v in hyp)
    res["c3"] = c3
    res["c3_scope_N"] = (N == 1)
    # supporting: exact infinite-order certificate within the generated group
    cand = []
    Xs = [Cc.X(k) for k in range(N)]
    Zs = [Cc.Z(k) for k in range(N)]
    others = [("X_1", Xs[0]), ("Z_1", Zs[0])] + [("U_%s" % fmtM(M), mat_embed(Fc, U[M], Fq)) for M in Ms[1:3]]
    found = None
    for name, Y in others:
        g = mat_mul(Fc, V0, Y)
        tr = Fc.zero
        for i in range(d):
            tr = Fc.add(tr, g[i][i])
        a2 = Fc.mul(tr, Fc.conj(tr))
        integral = Fc.is_alg_integer(a2)
        cand.append((name, Fc.show(a2), integral))
        if not integral and found is None:
            found = name
    for name, a2, integ in cand:
        out("  supporting: g = V %s: |tr g|^2 = %s, algebraic integer: %s" % (name, a2, integ))
    out("  supporting (decides nothing, A2): an element g of the generated group with |tr g|^2 not an "
        "algebraic integer has infinite order modulo scalars (exact): %s" % (found if found else "none found"))
    e1v = tuple(int(i == 0) for i in range(2 * N))
    orbit = set(cmat_vec(g, e1v, q) for g in grp)
    trans = len(orbit) == q ** (2 * N) - 1
    out("  supporting: orbit of e_1 under the generated symplectic group has %d of %d nonzero vectors "
        "(transitive: %s); in the Weyl basis {W(u)} the Clifford adjoint action is then irreducible on "
        "sl(q^N) [W]" % (len(orbit), q ** (2 * N) - 1, trans))
    out("  supporting argument [X]+[W], decides nothing: an Ad-irreducible Clifford group and an element of "
        "infinite order modulo scalars force the closure to contain SU(q^N): %s" % (trans and found is not None))
    res["c3_support"] = trans and found is not None
    token("C3(c3)", size, ("E1-DENSE [L]" if c3 else "E1-DENSITY-NOT-ESTABLISHED") +
          ("" if N == 1 else " [scope at N=2 conditional on the quoted statement covering N qudits]"))

    # ------------------------------------------------------------------ C4
    header("[%s] C4  escape from the known obstructions" % size)
    e1 = (1,) + (0,) * (N - 1)
    v = mat_vec(Fq, U[M0], C.basis_vec(e1))
    wit = None
    for i in range(d):
        for j in range(d):
            ent = Fq.mul(v[i], Fq.conj(v[j]))
            if not Fq.is_real(ent) or real_sign(Fq, ent) < 0:
                wit = (C.pts[i], C.pts[j], Fq.show(ent))
                break
        if wit:
            break
    out("(a) input |%s><%s| (entrywise nonnegative), operation U_0 (integer-time image): output entry %s is %s, "
        "not a nonnegative real" % (fmt_pt(e1), fmt_pt(e1), (wit[0], wit[1]) if wit else None, wit[2] if wit else None))
    c4a = wit is not None
    res["C4a"] = c4a
    token("C4(a)", size, "E1-NOT-NONNEG-BOUNDED" if c4a else "E1-NONNEG-BOUNDED")
    st = mat_vec(Fc, V0, Cc.basis_vec((0,) * N))
    W = wigner(Cc, st)
    tot = Fc.zero
    for z in sorted(W):
        tot = Fc.add(tot, W[z])
    out("(b) Wigner function of V|0>: real at every point %s; sum over phase space = %s"
        % (all(Fc.is_real(x) for x in W.values()), Fc.show(tot)))
    res["wigner_norm"] = tot == Fc.one
    negs = []
    for z in sorted(W):
        assert Fc.is_real(W[z])
        if real_sign(Fc, W[z]) < 0:
            negs.append(z)
    out("(b) state V|0> (V the canonical half-leap of L_0): Wigner values certified negative at %d of %d "
        "points (exact sign, rational interval enclosure)" % (len(negs), len(W)))
    if negs:
        z = negs[0]
        out("    e.g. W%s = %s  [N] ~ %.6f" % (fmt_pt(z), Fc.show(W[z]), Fc.to_complex(W[z]).real))
    ctrl_neg = True
    for key_, vv in sorted(rays.items()):
        Wv = wigner(C, vv)
        if any(real_sign(Fq, x) < 0 for x in Wv.values()):
            ctrl_neg = False
    out("    countercontrol: Wigner function nonnegative on every integer-time tested ray (%d): %s"
        % (len(rays), ctrl_neg))
    negscan = []
    for sg in itertools.product((1, -1), repeat=len(sp0) - 1):
        Vs = sqrt_from(Fc, sp0, o0, th0, (1,) + sg)
        Ws = wigner(Cc, mat_vec(Fc, Vs, Cc.basis_vec((0,) * N)))
        negscan.append(any(real_sign(Fc, x) < 0 for x in Ws.values()))
    out("    scan over every square root modulo global phase: negativity %s" % negscan)
    c4b = bool(negs)
    res["C4b"] = c4b
    res["C4b_ctrl"] = ctrl_neg
    token("C4(b)", size, "E1-WIGNER-NEGATIVE" if c4b else "E1-WIGNER-NONNEGATIVE")
    ngen = len(Ms) + N + 1
    out("(c) generating set for (c1)+(c2): %d leap images + %d translations + 1 half-leap = %d elements; the "
        "generated group is finitely generated, hence countable; a countable group is not all of PU(%d) "
        "(uncountable), so the exact target is not met by it [W]; consistent with fixedGateTheory_denseFiniteQM "
        "and fixedGateTheory_not_qm (DenseInstrumentBridge.lean:521, DiscreteCompletion.lean:1948) and "
        "countable_not_pairFlowSourced (PairFlowEquivalence.lean:218) [K, cited]" % (len(Ms), N, ngen, d))
    token("C4(c)", size, "COUNTABLE-GENERATING-SET (%d)" % ngen)

    # ------------------------------------------------------------------ controls K2-K6(a)
    header("[%s] Controls K2-K6(a)" % size)
    if N == 1:
        out("K2 not applicable at N = 1: every 1x1 coupling is symmetric")
        res["K2"] = None
    else:
        ns = [M for M in all_couplings(q, N) if M not in set(Ms)]
        dd = [len(C.intertwiners(leap_matrix(M, q))) for M in ns]
        k2 = all(x == 0 for x in dd) and not any(is_symplectic(leap_matrix(M, q), N, q) for M in ns)
        out("K2 non-symmetric couplings: %d; leap symplectic for none; intertwiner dimension 0 for all: %s" % (len(ns), k2))
        res["K2"] = k2
        token("K2", size, "PASS" if k2 else "FAIL")
    k3 = True
    for M in Ms:
        # point prior xi = 0, x0 = 0, one leap: classical x' = M 0 - 0 = 0 deterministic
        pc = [Fraction(1) if p == (0,) * N else Fraction(0) for p in C.pts]
        pb = born(Fq, mat_vec(Fq, U[M], C.basis_vec((0,) * N)))
        k3 &= any(x != Fq.frac(y) for x, y in zip(pb, pc))
    out("K3 point prior on the previous component (xi = 0), one leap from x0 = 0: classical law (deterministic) "
        "differs from the Born law for every coupling: %s; Born law for M = 0: %s"
        % (k3, [Fq.show(x) for x in born(Fq, mat_vec(Fq, U[M0], C.basis_vec((0,) * N)))]))
    res["K3"] = k3
    token("K3", size, "PASS" if k3 else "FAIL")
    k4 = True
    for k in range(N):
        n = N + 1
        A = [[int(i == j) for j in range(2 * n)] for i in range(2 * n)]
        A[N][k] = 1
        bare = tuple(tuple(r) for r in A)
        db = len(Cs.intertwiners(bare))
        A[n + k][n + N] = q - 1
        sym = tuple(tuple(r) for r in A)
        ds = len(Cs.intertwiners(sym))
        k4 &= db == 0 and ds == 1 and not is_symplectic(bare, n, q)
        out("K4 meter on site %d: bare read-write copy x_m += x_k (previous untouched): intertwiner dimension %d; "
            "symplectic meter: %d" % (k + 1, db, ds))
    res["K4"] = k4
    token("K4", size, "PASS" if k4 else "FAIL")
    k5 = k5_config_carrier(q, N, Ms)
    res["K5"] = k5
    token("K5", size, "PASS" if k5 else "FAIL")
    # K6(a)
    k6a = True
    p1 = C.idx[e1]
    Dm = eye(Fq, d)
    Dm[p1][p1] = Fq.neg(Fq.one)
    for M in Ms:
        Um = mat_mul(Fq, U[M], Dm)
        ok, fst, _ = c1_words(C, Um, Ls[M], early=True)
        itw = intertwines(C, Um, Ls[M])
        det = (not ok)
        k6a &= det
        if M == M0:
            out("K6(a) column-sign mutation U_M diag(..,-1 at %s,..), M = %s: C1 Born-law check rejects: %s "
                "(first counterexample word %s, x0 %s); intertwining check rejects: %s"
                % (fmt_pt(e1), fmtM(M), det, fst[0] if fst else None, fst[1] if fst else None, not itw))
    out("K6(a) column-sign mutation rejected by the C1 Born-law check for every coupling: %s" % k6a)
    chirp_ok = True
    for M in Ms:
        if M == M0:
            continue
        Uc = mat_mul(Fq, rho_J, C.chirp(M))
        ok, fst, _ = c1_words(C, Uc, Ls[M], early=True)
        chirp_ok &= not ok
    out("K6(a) chirp-sign mutation rho(J') diag(w^(+y.My/2)) rejected for every nonzero coupling: %s" % chirp_ok)
    okg, _, _ = c1_words(C, mat_scale(Fq, Fq.neg(Fq.one), U[M0]), Ls[M0])
    out("K6(a) non-mutation: the global sign -U_0 is accepted (a phase): %s" % okg)
    k6a = k6a and chirp_ok and okg
    res["K6a"] = k6a
    token("K6(a) sign mutation", size, "DETECTED" if k6a else "NOT-DETECTED (control fails)")
    supplementary_centre_free(C, Ms, Ls, ords, U, size, res)
    return res


def supplementary_centre_free(C, Ms, Ls, ords, U, size, res):
    """Outside the frozen cells; decides nothing. SM 3.1's rule is centre-free: x_i(t+1) depends on the
    neighbours of i, not on x_i, so a coupling with a nonzero diagonal entry is a self-coupling that the
    substratum rule does not contain. RULES.md quantifies over every symmetric coupling."""
    q, N, d = C.q, C.N, C.d
    Fq = C.F
    header("[%s] SUPPLEMENTARY (not a cell; decides nothing): centre-free couplings only" % size)
    cf = [M for M in Ms if all(M[i][i] == 0 for i in range(N))]
    out("centre-free symmetric couplings (zero diagonal): %s" % " ".join(fmtM(M) for M in cf))
    grp = group_closure([Ls[M] for M in cf], q)
    out("group generated by their leap matrices: order %d; |Sp(%d,%d)| = %d" % (len(grp), 2 * N, q, sp_order(N, q)))
    rows = sorted(set(cmat_vec(g, tuple(int(i == k) for i in range(N)) + (0,) * N, q) for g in grp for k in range(N)))
    rank = 2 * N - len(nullspace_mod([list(r) for r in rows], 2 * N, q))
    out("with the position translations: translation subgroup of rank %d; group modulo phases of order %d "
        "(full Clifford group: %d)" % (rank, q ** rank * len(grp), q ** (2 * N) * sp_order(N, q)))
    Mx = cf[-1]
    Fa = field(lcm(q, ords[Mx]))
    spm = spectral(Fa, mat_embed(Fa, U[Mx], Fq), ords[Mx])
    spx = spectral(Fa, mat_embed(Fa, C.X(0), Fq), q)
    gens = [generator_from_thetas(Fa, spm, [principal_theta(j, ords[Mx]) for j, _ in spm]),
            generator_from_thetas(Fa, spx, [principal_theta(j, q) for j, _ in spx])]
    dm = lie_closure_dim(Fa, [[g] for g in gens], stop_at=d * d)
    out("all-duration algebra of {L_%s, tau_1}, canonical: dim modulo identity %d of %d" % (fmtM(Mx), dm - 1, d * d - 1))
    res["centre_free"] = (len(grp), rank, dm - 1)


def ords_single(q):
    return cmat_order(leap_matrix(((0,),), q), q)


def kron(F, A, B):
    da, db = len(A), len(B)
    return [[F.mul(A[i // db][j // db], B[i % db][j % db]) for j in range(da * db)] for i in range(da * db)]


def schmidt_rank(F, V, q):
    """Operator-Schmidt rank of V on C^q (x) C^q: rank of the realigned matrix (exact)."""
    rows = []
    for a in range(q):
        for b in range(q):
            rows.append([V[a * q + c][b * q + e] for c in range(q) for e in range(q)])
    return mat_rank(F, rows)


def mat_rank(F, rows):
    rows = [list(r) for r in rows]
    r = 0
    ncol = len(rows[0])
    for c in range(ncol):
        p = next((i for i in range(r, len(rows)) if not F.is_zero(rows[i][c])), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        iv = F.inv(rows[r][c])
        rows[r] = [F.mul(iv, x) for x in rows[r]]
        for i in range(len(rows)):
            if i != r and not F.is_zero(rows[i][c]):
                f = rows[i][c]
                rows[i] = [F.sub(x, F.mul(f, y)) for x, y in zip(rows[i], rows[r])]
        r += 1
    return r


def k5_config_carrier(q, N, Ms):
    """K5: configuration carrier C^{V^2N}, (prev, cur) per site; shear (prev,cur) -> (M cur - prev, cur),
    swap, and leap = swap o shear, for every symmetric coupling. Every spectral projector of each
    permutation has the all-ones vector as an eigenvector (checked cycle by cycle, exactly), so every
    principal logarithm (any global phase) maps 1 to a multiple of 1, brackets of such maps annihilate 1,
    and every flow fixes the all-ones ray."""
    pts = list(itertools.product(range(q), repeat=2 * N))
    idx = {p: i for i, p in enumerate(pts)}
    perms = []
    for M in Ms:
        sh = []
        sw = []
        for p in pts:
            prev, cur = p[:N], p[N:]
            new_prev = tuple((sum(M[i][j] * cur[j] for j in range(N)) - prev[i]) % q for i in range(N))
            sh.append(idx[new_prev + cur])
            sw.append(idx[cur + prev])
        lp = [sw[sh[i]] for i in range(len(pts))]
        perms += [sh, sw, lp]
    ok = True
    lengths = set()
    for pm in perms:
        seen = [False] * len(pts)
        for s0 in range(len(pts)):
            if seen[s0]:
                continue
            cyc = []
            t = s0
            while not seen[t]:
                seen[t] = True
                cyc.append(t)
                t = pm[t]
            ell = len(cyc)
            lengths.add(ell)
            Fl = field(ell if ell > 2 else 4)
            for j in range(ell):
                # (P_j 1)_s = (1/ell) sum_t zeta_ell^{j(t-s)} on the cycle; must be delta_{j0}
                for s_ in range(ell):
                    acc = Fl.zero
                    for t_ in range(ell):
                        acc = Fl.add(acc, Fl.root(ell, j * (t_ - s_)))
                    acc = Fl.scal(Fraction(1, ell), acc)
                    ok &= acc == (Fl.one if j == 0 else Fl.zero)
    out("K5 configuration carrier C^%d: %d permutations (shear, swap, leap per coupling); cycle lengths %s; "
        "all-ones vector an eigenvector of every spectral projector (exact): %s"
        % (len(pts), len(perms), sorted(lengths), ok))
    F4 = field(4)
    ph = [F4.root(4, 1)] + [F4.one] * (len(pts) - 1)
    moved = not all(x == ph[0] for x in ph)
    out("    quarter phase on one configuration moves the all-ones ray (exact): %s "
        "[K: onesTheory_not_phasesAvailable, FlowEndpoint.lean:177]" % moved)
    return ok and moved


# ============================================================================ K1 (q = 2) and the driver


def run_K1(R):
    header("K1  q = 2: the kernel's two-layer images against the visible law")
    F = field(8)
    i_ = F.root(4, 1)
    hc = F.scal(Fraction(1, 2), F.add(F.zeta(1), F.zeta(7)))           # 1/sqrt 2
    assert F.mul(F.mul(hc, hc), F.frac(2)) == F.one
    shear_img = [[F.one, F.zero], [F.zero, i_]]                          # siteShearImage: diag(1, I)
    swap_img = [[hc, hc], [hc, F.neg(hc)]]                               # siteSwapImage: hadamard
    out("images (C5Discovery.lean:156-198): shear -> diag(1, i); swap -> (1/sqrt2)[[1,1],[1,-1]]; "
        "unitary: %s, %s" % (unitary_check(F, shear_img), unitary_check(F, swap_img)))
    out("classical layers on (prev, cur) in Z_2^2: shear (a, b) -> (F(b) - a, b) with F(b) = b; swap (a, b) -> (b, a); "
        "cur registered, prev uniform")

    def cl(word, x0):
        cnt = [Fraction(0), Fraction(0)]
        for p in range(2):
            a, b = p, x0
            for g in word:
                a, b = ((b - a) % 2, b) if g == "s" else (b, a)
            cnt[b] += Fraction(1, 2)
        return cnt
    mism = 0
    total = 0
    first = None
    for ln in range(1, 7):
        for word in itertools.product("sw", repeat=ln):
            for x0 in range(2):
                v = [F.one if i == x0 else F.zero for i in range(2)]
                for g in word:
                    v = mat_vec(F, shear_img if g == "s" else swap_img, v)
                pb = born(F, v)
                pc = cl(word, x0)
                total += 1
                if any(x != F.frac(y) for x, y in zip(pb, pc)):
                    mism += 1
                    if first is None:
                        first = ("".join(word), x0, [F.show(x) for x in pb], [str(y) for y in pc])
    out("words of length 1..6 over {s, w}, both x0: %d cases, %d contradict the classical visible law" % (total, mism))
    out("first contradiction (word applied left to right, x0, Born, classical): %s" % (first,))
    S2 = mat_mul(F, shear_img, shear_img)
    out("shear is an involution classically; its image squared is diag(1, -1), not a scalar: %s"
        % (proportional_scalar(F, S2, eye(F, 2)) is None))
    k1 = mism > 0
    R["K1"] = k1
    token("K1", "q=2,N=1", "PASS (kernel images contradict the visible law)" if k1 else "FAIL")


def self_tests():
    header("Implementation self-tests (exact)")
    ok = True
    for n in (24, 60, 120):
        F = field(n)
        a = F.norm(tuple((7 * i + 3) % 23 - 11 for i in range(F.deg)), 6)
        b = F.norm(tuple((5 * i + 1) % 19 - 9 for i in range(F.deg)), 35)
        ok &= F.kmul(a, b) == F.smul(a, b)
        ok &= F.mul(a, F.inv(a)) == F.one
        ok &= F.conj(F.conj(a)) == a
    out("Kronecker product = schoolbook product, a * a^-1 = 1, conj o conj = id: %s" % ok)
    F = field(12)
    s3 = F.add(F.zeta(1), F.zeta(11))
    sg = (real_sign(F, F.sub(s3, F.frac(Fraction(17320, 10000)))), real_sign(F, F.sub(s3, F.frac(Fraction(17321, 10000)))))
    out("certified signs: sqrt3 - 1.7320 -> %d, sqrt3 - 1.7321 -> %d" % sg)
    ok &= sg == (1, -1)
    for q in (3, 5):
        Fq = field(q)
        G = Fq.zero
        for x in range(q):
            G = Fq.add(G, Fq.root(q, x * x))
        leg = 1 if q % 4 == 1 else -1
        ok &= Fq.mul(G, G) == Fq.frac(leg * q)
    out("Gauss sums G^2 = (-1/q) q at q = 3, 5: %s" % ok)
    return ok


def main(sizes):
    R = {}
    out("F2-1 exact run: RULES.md @ 6481ead7 with amendment 1 @ 9d996159 (2026-10-14)")
    out("Labels: [X] exact (all lines unless tagged), [N] floating point (decides nothing), [L] literature, "
        "[K] kernel theorem cited, [W] written argument.")
    st = self_tests()
    R["selftest"] = st
    run_K1(R)
    for q, N in sizes:
        run_size(q, N, R)
    verdict(R, sizes)


def verdict(R, sizes):
    header("Summary and verdict")
    ctrl = [("selftest", R["selftest"]), ("K1", R["K1"])]
    for q, N in sizes:
        r = R["q=%d,N=%d" % (q, N)]
        sz = "q=%d,N=%d" % (q, N)
        for k in ("W0", "K2", "K3", "K4", "K5", "K6a", "K6b", "C4b_ctrl", "wigner_norm"):
            if r.get(k) is not None:
                ctrl.append((k + "@" + sz, r[k]))
    for name, v in ctrl:
        out("control %-26s %s" % (name, "PASS" if v else "FAIL"))
    controls_ok = all(v for _, v in ctrl)
    rows = []
    for q, N in sizes:
        sz = "q=%d,N=%d" % (q, N)
        r = R[sz]
        out("%s: C1 %s | C2 %s | C3(a) %s (A1 scan %s) | C3(b) %s | c1 %s | c2 %s (scans %s) | c3 %s | C4(a) %s | C4(b) %s"
            % (sz, r["C1"], r["C2"], r["C3a"], r["C3a_scan"], r["C3b"], r["c1"], r["c2"], "/".join(r["c2_scan"]),
               r["c3"], r["C4a"], r["C4b"]))
        rows.append((sz, r))
    if not controls_ok:
        out("VERDICT VOID")
        return
    if not all(r["C1"] and r["C2"] for _, r in rows):
        bad = [sz for sz, r in rows if not (r["C1"] and r["C2"])]
        out("VERDICT E1-INCONSISTENT (%s)" % ",".join(bad))
        return
    dense = [sz for sz, r in rows if r["c1"] and r["c2"] and r["c3"] and r["C4a"] and r["C4b"]]
    if len(dense) == len(rows):
        out("outcome rule: C1, C2 hold at every tested size; C3(c) = (c1) [X] and (c2) [X] and (c3) [L] holds with "
            "C4(a), C4(b) at every tested size")
        out("qualifier: (c3) is the amendment's quoted literature statement [L]; at N >= 2 it is used for an "
            "N-qudit Clifford group, a scope not checked against the source here")
        out("VERDICT E1-CONSISTENT-AND-DENSE")
        return
    toks = []
    for sz, r in rows:
        toks.append("%s:%s,%s" % (sz, "E1-FULL-ALGEBRA" if r["C3a"] else "E1-NOT-FULL-ALGEBRA",
                                  "E1-ONE-DURATION-NONCLIFFORD" if r["c2"] else "E1-HALF-PERIOD-CLIFFORD"))
    out("VERDICT E1-CONSISTENT; repertoires: " + " ".join(toks))


if __name__ == "__main__":
    SIZES = [(3, 1), (3, 2), (5, 1)]
    if len(sys.argv) > 1:
        SIZES = [tuple(int(x) for x in a.split(",")) for a in sys.argv[1:]]
    main(SIZES)
