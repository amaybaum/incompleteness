"""Small exact Q(i) matrix arithmetic for the independently written design controls."""
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache


@dataclass(frozen=True)
class G:
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __post_init__(self):
        object.__setattr__(self, 're', Fraction(self.re))
        object.__setattr__(self, 'im', Fraction(self.im))

    @staticmethod
    def of(value):
        return value if isinstance(value, G) else G(value)

    def __add__(self, other):
        other = G.of(other)
        return G(self.re + other.re, self.im + other.im)
    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + -G.of(other)

    def __rsub__(self, other):
        return G.of(other) + -self

    def __mul__(self, other):
        other = G.of(other)
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)
    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def __truediv__(self, other):
        other = G.of(other)
        norm = other.re ** 2 + other.im ** 2
        if norm == 0:
            raise ZeroDivisionError
        return self * G(other.re / norm, -other.im / norm)

    def __eq__(self, other):
        other = G.of(other)
        return (self.re, self.im) == (other.re, other.im)

    def nonnegative(self):
        return self.im == 0 and self.re >= 0


I = G(0, 1)
Z = G()


def matrix(rows):
    return tuple(tuple(G.of(x) for x in row) for row in rows)


def eye(n):
    return matrix([[int(j == k) for k in range(n)] for j in range(n)])


def diag(*values):
    return matrix([[v if j == k else 0 for k in range(len(values))]
                   for j, v in enumerate(values)])


def add(A, B):
    return tuple(tuple(a + b for a, b in zip(ra, rb)) for ra, rb in zip(A, B))


def scale(c, A):
    return tuple(tuple(G.of(c) * a for a in row) for row in A)


def mul(A, B):
    return tuple(tuple(sum((A[j][k] * B[k][l] for k in range(len(B))), Z)
                       for l in range(len(B[0]))) for j in range(len(A)))


def adj(A):
    return tuple(tuple(A[k][j].conj() for k in range(len(A))) for j in range(len(A[0])))


def tensor(A, B):
    return tuple(tuple(A[j][k] * B[l][m] for k in range(len(A[0])) for m in range(len(B[0])))
                 for j in range(len(A)) for l in range(len(B)))


def trace(A):
    return sum((A[j][j] for j in range(len(A))), Z)


def extract(A, ix):
    return tuple(tuple(A[j][k] for k in ix) for j in ix)


@lru_cache(maxsize=None)
def det(A):
    n = len(A)
    if n == 0:
        return G(1)
    if n == 1:
        return A[0][0]
    return sum(((-1) ** k * A[0][k] * det(tuple(tuple(row[l] for l in range(n) if l != k)
                  for row in A[1:])) for k in range(n)), Z)


def rank(A):
    rows = [list(row) for row in A]
    pivot = 0
    for col in range(len(A[0])):
        found = next((j for j in range(pivot, len(A)) if rows[j][col] != 0), None)
        if found is None:
            continue
        rows[pivot], rows[found] = rows[found], rows[pivot]
        div = rows[pivot][col]
        rows[pivot] = [a / div for a in rows[pivot]]
        for j in range(len(A)):
            if j != pivot:
                fac = rows[j][col]
                rows[j] = [a - fac * b for a, b in zip(rows[j], rows[pivot])]
        pivot += 1
        if pivot == len(A):
            break
    return pivot
