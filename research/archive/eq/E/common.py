"""EQ-E shared exact helpers (sympy exact arithmetic only; no floating point).

Conventions match the kernel at bcbc516f (verification/lean-mathlib/OIBridge/CompositeDimension.lean):
  * one copy: homogenized index mu in {0,1,2,3}; hom x = (1, x0, x1, x2)            (CD:100)
    quantum identification: x = Bloch vector of rho, i.e. omega_mu = tr(rho sigma_mu),
    sigma = (I, X, Y, Z).
  * joint carrier W 3: 4x4 real matrix omega[mu][nu]; prodState x y [mu][nu] = hom x mu * hom y nu  (CD:161)
    quantum identification: omega[mu][nu] = tr(rho sigma_mu (x) sigma_nu)   (control index mu, target nu).
  * vectorisation index 4*mu + nu.
  * actT N omega = omega * H^T   (H = homMap N = diag(1, N)), i.e. kron(I4, H)      (CD:198)
    actC N omega = H * omega,                         i.e. kron(H, I4)              (CD:201)
  * kernel cnot (CD:741-786): (cnot omega)[mu][nu] = sgn(mu,nu) * omega[pc(mu,nu)][pt(mu,nu)].
"""
import itertools
from sympy import Matrix, I, Rational, eye, zeros, simplify, expand, conjugate, sqrt, nsimplify

R = Rational

# ---------------------------------------------------------------- Pauli algebra
S0 = Matrix([[1, 0], [0, 1]])
SX = Matrix([[0, 1], [1, 0]])
SY = Matrix([[0, -I], [I, 0]])
SZ = Matrix([[1, 0], [0, -1]])
PAULI = [S0, SX, SY, SZ]


def kron(A, B):
    ra, ca = A.shape
    rb, cb = B.shape
    M = zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            for k in range(rb):
                for l in range(cb):
                    M[i * rb + k, j * cb + l] = A[i, j] * B[k, l]
    return M


def dag(U):
    return U.conjugate().T


def tr(M):
    return expand(M.trace())


def ptm1(U):
    """4x4 matrix C acting on expectation coordinates: (C w)_mu = tr(U rho U^dag sigma_mu)."""
    C = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            C[m, n] = simplify(tr(PAULI[m] * U * PAULI[n] * dag(U)) / 2)
    return C


PAULI2 = [kron(PAULI[m], PAULI[n]) for m in range(4) for n in range(4)]


def ptm2(U):
    """16x16 matrix on vec(omega), index 4*mu+nu: (C w)_(mu nu) = tr(U rho U^dag sigma_mu (x) sigma_nu)."""
    C = zeros(16, 16)
    for a in range(16):
        for b in range(16):
            C[a, b] = simplify(tr(PAULI2[a] * U * PAULI2[b] * dag(U)) / 4)
    return C


def rho1(x):
    """qubit density matrix of Bloch vector x."""
    return (S0 + x[0] * SX + x[1] * SY + x[2] * SZ) / 2


def coeffs2(rho):
    """omega[mu][nu] = tr(rho sigma_mu (x) sigma_nu) as a 4x4 Matrix."""
    return Matrix(4, 4, lambda m, n: simplify(tr(rho * PAULI2[4 * m + n])))


def vec(om):
    return Matrix(16, 1, lambda a, _: om[a // 4, a % 4])


def unvec(v):
    return Matrix(4, 4, lambda m, n: v[4 * m + n])


# ---------------------------------------------------------------- kernel objects (transcribed)
_PC = {(0, 0): 0, (0, 1): 0, (0, 2): 3, (0, 3): 3,
       (1, 0): 1, (1, 1): 1, (1, 2): 2, (1, 3): 2,
       (2, 0): 2, (2, 1): 2, (2, 2): 1, (2, 3): 1,
       (3, 0): 3, (3, 1): 3, (3, 2): 0, (3, 3): 0}
_PT = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3,
       (1, 0): 1, (1, 1): 0, (1, 2): 3, (1, 3): 2,
       (2, 0): 1, (2, 1): 0, (2, 2): 3, (2, 3): 2,
       (3, 0): 0, (3, 1): 1, (3, 2): 2, (3, 3): 3}


def _sgn(m, n):
    return -1 if (m, n) in ((1, 3), (2, 2)) else 1


def kernel_cnot16():
    """the kernel's `cnot` (CD:758,775) as a 16x16 matrix on vec(omega)."""
    C = zeros(16, 16)
    for m in range(4):
        for n in range(4):
            C[4 * m + n, 4 * _PC[(m, n)] + _PT[(m, n)]] = _sgn(m, n)
    return C


NFLIP = Matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])     # CD:797
Z3 = Matrix([0, 0, 1])                                     # CD:793
XPLUS = Matrix([1, 0, 0])                                  # CD:1213
PHIW = Matrix(4, 4, lambda m, n: (-1 if m == 2 else 1) if m == n else 0)   # CD:1220
REFLY = Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 1]])        # K2Guard:46


def homMap(N):
    H = zeros(4, 4)
    H[0, 0] = 1
    H[1:, 1:] = N
    return H


def actT16(N):
    return kron(eye(4), homMap(N))


def actC16(N):
    return kron(homMap(N), eye(4))


def hom(x):
    from sympy import sympify
    return Matrix([1, sympify(x[0]), sympify(x[1]), sympify(x[2])])


def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return Matrix(4, 4, lambda m, n: hx[m] * hy[n])


def sharpVec(b):
    """homogenized coefficients of sharpEff b (EffectSpace:57): (1/2, b/2).  Inputs are sympified, so Python ints
    cannot turn b/2 into a float (s7 run 1 failed for that reason)."""
    from sympy import sympify
    b = [sympify(v) for v in b]
    return Matrix([R(1, 2), b[0] / 2, b[1] / 2, b[2] / 2])


def pairVal(a, b, om):
    return expand(sum(a[m] * om[m, n] * b[n] for m in range(4) for n in range(4)))


# ---------------------------------------------------------------- reporting
class Report:
    def __init__(self, name):
        self.name = name
        self.lines = []
        self.fail = 0
        self.n = 0

    def check(self, label, ok, detail=""):
        self.n += 1
        if not ok:
            self.fail += 1
        self.lines.append(("PASS" if ok else "FAIL") + "  " + label + (("  -- " + detail) if detail else ""))

    def note(self, s):
        self.lines.append("NOTE  " + s)

    def out(self):
        for l in self.lines:
            print(l)
        status = "OK" if self.fail == 0 else "FAILED"
        print("%s: %s -- %d checks, %d failed" % (self.name, status, self.n, self.fail))
        return self.fail == 0
