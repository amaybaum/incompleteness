"""EQ-B exact two-qubit library over the Gaussian rationals Q(i).

Complex numbers are Python complex-free pairs: class Q with Fraction real and imaginary parts.
Channels Ad(U): rho -> U rho U^dagger are represented on the real carrier W 3 of CompositeDimension:
  omega_{mu nu} = tr(rho sigma_mu (x) sigma_nu),  sigma_0 = I, sigma_1 = X, sigma_2 = Y, sigma_3 = Z,
so that a product state rho = rho_x (x) rho_y has omega = hom x hom y^T (Bloch vectors x, y), the carrier
convention of the kernel (hom index 0 = unit, indices 1..3 = x, y, z).
"""
from fractions import Fraction as Fr


class Q:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        o = o if isinstance(o, Q) else Q(o)
        return Q(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Q) else Q(o)
        return Q(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return Q(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, Q) else Q(o)
        return Q(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __neg__(self):
        return Q(-self.re, -self.im)

    def conj(self):
        return Q(self.re, -self.im)

    def __eq__(self, o):
        o = o if isinstance(o, Q) else Q(o)
        return self.re == o.re and self.im == o.im

    def __repr__(self):
        return f"({self.re}+{self.im}i)"


I_ = Q(0, 1)


def cz(n, m):
    return [[Q() for _ in range(m)] for _ in range(n)]


def cmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = cz(n, m)
    for i in range(n):
        for t in range(k):
            a = A[i][t]
            if a.re == 0 and a.im == 0:
                continue
            for j in range(m):
                b = B[t][j]
                if b.re == 0 and b.im == 0:
                    continue
                out[i][j] = out[i][j] + a * b
    return out


def cdag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def ckron(A, B):
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    out = cz(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            for k in range(rb):
                for l in range(cb):
                    out[i * rb + k][j * cb + l] = A[i][j] * B[k][l]
    return out


def ctrace(A):
    s = Q()
    for i in range(len(A)):
        s = s + A[i][i]
    return s


def cadd(A, B, s=1):
    return [[A[i][j] + B[i][j] * s for j in range(len(A[0]))] for i in range(len(A))]


def cscale(c, A):
    c = c if isinstance(c, Q) else Q(c)
    return [[c * x for x in r] for r in A]


def ceye(n):
    m = cz(n, n)
    for i in range(n):
        m[i][i] = Q(1)
    return m


PI = [[Q(1), Q()], [Q(), Q(1)]]
PX = [[Q(), Q(1)], [Q(1), Q()]]
PY = [[Q(), Q(0, -1)], [Q(0, 1), Q()]]
PZ = [[Q(1), Q()], [Q(), Q(-1)]]
PAULI = [PI, PX, PY, PZ]
P0 = [[Q(1), Q()], [Q(), Q()]]    # |0><0|  (Bloch +z)
P1 = [[Q(), Q()], [Q(), Q(1)]]    # |1><1|  (Bloch -z)


def channel_W(U):
    """Real 16 x 16 matrix of Ad(U) on the carrier W 3 (index mu*4+nu)."""
    Ud = cdag(U)
    basis = [ckron(PAULI[a], PAULI[b]) for a in range(4) for b in range(4)]
    M = [[Fr(0)] * 16 for _ in range(16)]
    for col in range(16):
        img = cmul(U, cmul(basis[col], Ud))
        for row in range(16):
            t = ctrace(cmul(img, basis[row]))
            # omega' = (1/4) sum omega tr(U s_col U^dag s_row)
            assert t.im == 0, "non-real trace"
            M[row][col] = t.re / 4
    return M


def local_W(V):
    """Real 4 x 4 matrix of Ad(V) on one copy's homogenized space (index 0 = unit)."""
    Vd = cdag(V)
    M = [[Fr(0)] * 4 for _ in range(4)]
    for col in range(4):
        img = cmul(V, cmul(PAULI[col], Vd))
        for row in range(4):
            t = ctrace(cmul(img, PAULI[row]))
            assert t.im == 0
            M[row][col] = t.re / 2
    return M


def controlled(L0, L1):
    """|0><0| (x) L0 + |1><1| (x) L1."""
    return cadd(ckron(P0, L0), ckron(P1, L1))
