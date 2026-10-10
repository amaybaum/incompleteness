"""EQ2-C common helpers: a check recorder and exact arithmetic in Q(sqrt 5).

Everything here is exact (fractions.Fraction); nothing uses floating point.
"""
import sys
from fractions import Fraction as Fr


class Checks:
    """Records named boolean checks; prints PASS/FAIL lines; the verdict line prints only if all pass."""

    def __init__(self, name):
        self.name = name
        self.items = []

    def check(self, label, cond):
        ok = bool(cond)
        self.items.append((label, ok))
        print(("PASS " if ok else "FAIL ") + label)
        sys.stdout.flush()
        return ok

    def note(self, text):
        print("     " + text)

    def finish(self, verdict):
        n = len(self.items)
        k = sum(1 for _, ok in self.items if ok)
        print(f"{self.name}: {k}/{n} checks pass")
        if k == n:
            print("VERDICT " + verdict)
            return 0
        print("VERDICT NOT RENDERED (a check failed)")
        return 1


class Q5:
    """a + b*sqrt(5) with rational a, b (exact)."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    @staticmethod
    def lift(x):
        return x if isinstance(x, Q5) else Q5(x, 0)

    def __add__(self, o):
        o = Q5.lift(o)
        return Q5(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-Q5.lift(o))

    def __rsub__(self, o):
        return Q5.lift(o) - self

    def __mul__(self, o):
        o = Q5.lift(o)
        return Q5(self.a * o.a + 5 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def inv(self):
        n = self.a * self.a - 5 * self.b * self.b
        if n == 0:
            raise ZeroDivisionError("Q5 zero")
        return Q5(self.a / n, -self.b / n)

    def __truediv__(self, o):
        return self * Q5.lift(o).inv()

    def __rtruediv__(self, o):
        return Q5.lift(o) * self.inv()

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if (a > 0) == (b > 0):
            return 1 if a > 0 else -1
        # opposite signs: compare a^2 with 5 b^2
        if a * a > 5 * b * b:
            return 1 if a > 0 else -1
        if a * a < 5 * b * b:
            return 1 if b > 0 else -1
        return 0

    def __eq__(self, o):
        o = Q5.lift(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def __lt__(self, o):
        return (self - o).sign() < 0

    def __le__(self, o):
        return (self - o).sign() <= 0

    def __gt__(self, o):
        return (self - o).sign() > 0

    def __ge__(self, o):
        return (self - o).sign() >= 0

    def __repr__(self):
        if self.b == 0:
            return str(self.a)
        return f"({self.a}+{self.b}*r5)"


SQRT5 = Q5(0, 1)
PHI = (1 + SQRT5) / 2          # golden ratio
IPHI = PHI - 1                 # 1/phi


def vadd(u, v):
    return tuple(x + y for x, y in zip(u, v))


def vsub(u, v):
    return tuple(x - y for x, y in zip(u, v))


def vscale(c, u):
    return tuple(c * x for x in u)


def dot(u, v):
    s = 0
    for x, y in zip(u, v):
        s = s + x * y
    return s


def cross2(u, v):
    return u[0] * v[1] - u[1] * v[0]


def mat_vec(M, v):
    return tuple(dot(row, v) for row in M)


def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return tuple(tuple(sum((A[i][k] * B[k][j] for k in range(m)), Q5(0) if isinstance(A[0][0], Q5) else 0)
                       for j in range(p)) for i in range(n))


def transpose(A):
    return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))
