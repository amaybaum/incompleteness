"""Exact Gaussian-rational / rational matrix helpers for EQ-D (sympy DomainMatrix over QQ_I or QQ).

Every operation is exact field arithmetic; there is no simplification step and no floating point.
"""
import random

from sympy import Rational, sympify
from sympy.polys.domains import QQ, QQ_I
from sympy.polys.matrices import DomainMatrix


class Ctx:
    def __init__(self, real, seed):
        self.real = real
        self.K = QQ if real else QQ_I
        self.rng = random.Random(seed)

    # ---- scalars ----
    def s(self, re, im=0):
        if self.real:
            return QQ.from_sympy(sympify(re))
        return QQ_I(re, im)

    def conj(self, a):
        return a if self.real else QQ_I(a.x, -a.y)

    def re(self, a):
        return a if self.real else a.x

    def im(self, a):
        return QQ(0) if self.real else a.y

    def grat(self):
        return Rational(self.rng.randint(-4, 4), self.rng.randint(1, 3))

    def rand_scalar(self):
        return self.s(self.grat(), 0 if self.real else self.grat())

    # ---- matrices ----
    def mat(self, rows):
        n, m = len(rows), len(rows[0])
        return DomainMatrix([[self.K.convert(v) if not isinstance(v, type(self.K.one)) else v for v in r]
                             for r in rows], (n, m), self.K)

    def zeros(self, n, m=None):
        return DomainMatrix.zeros((n, m if m is not None else n), self.K)

    def eye(self, n):
        return DomainMatrix.eye(n, self.K)

    def H(self, M):
        n, m = M.shape
        return DomainMatrix([[self.conj(M[i, j].element) for i in range(n)] for j in range(m)], (m, n), self.K)

    def kron(self, A, B):
        (a1, a2), (b1, b2) = A.shape, B.shape
        rows = [[A[i // b1, j // b2].element * B[i % b1, j % b2].element for j in range(a2 * b2)]
                for i in range(a1 * b1)]
        return DomainMatrix(rows, (a1 * b1, a2 * b2), self.K)

    def col(self, M, j):
        return M.extract(list(range(M.shape[0])), [j])

    def cols(self, M, js):
        return M.extract(list(range(M.shape[0])), list(js))

    def rows(self, M, iss):
        return M.extract(list(iss), list(range(M.shape[1])))

    def trace(self, M):
        t = self.K.zero
        for i in range(M.shape[0]):
            t += M[i, i].element
        return t

    def is_zero(self, M):
        return all(M[i, j].element == self.K.zero for i in range(M.shape[0]) for j in range(M.shape[1]))

    def eq(self, A, B):
        return self.is_zero(A - B)

    def scal(self, c, M):
        return M * self.K.convert(c) if not isinstance(c, type(self.K.one)) else M * c

    # ---- random exact objects ----
    def rand_skew(self, n):
        rows = [[self.K.zero] * n for _ in range(n)]
        for i in range(n):
            rows[i][i] = self.K.zero if self.real else self.s(0, self.grat())
            for j in range(i + 1, n):
                z = self.rand_scalar()
                rows[i][j] = z
                rows[j][i] = -self.conj(z)
        return DomainMatrix(rows, (n, n), self.K)

    def cayley(self, S):
        n = S.shape[0]
        E = self.eye(n)
        return (E - S) * (E + S).inv()

    def rand_state(self, k):
        B = DomainMatrix([[self.rand_scalar() for _ in range(k)] for _ in range(k)], (k, k), self.K)
        M = B * self.H(B) + self.eye(k)
        return M * (self.K.one / self.trace(M))

    def rand_effect(self, k):
        B = DomainMatrix([[self.rand_scalar() for _ in range(k)] for _ in range(k)], (k, k), self.K)
        M = B * self.H(B)
        lam = QQ(1)
        for i in range(k):
            for j in range(k):
                e = M[i, j].element
                lam += abs(self.re(e)) + abs(self.im(e))   # >= sum |M_ij| >= operator norm
        return M * self.K.convert(1 / lam) if self.real else M * QQ_I(1 / lam, 0)


def real_rank(vectors):
    """rank over QQ of a list of rational vectors"""
    if not vectors:
        return 0
    return DomainMatrix([[QQ(v) for v in vec] for vec in vectors], (len(vectors), len(vectors[0])), QQ).rank()
