"""Independent exact arithmetic in Q(zeta_16) for the LOC-1 replay (decision (j)); research development.

Written separately from cyclo16.py and importing nothing from it, from s16_layer.py or from the engine: only the
standard library.  The methods differ on purpose:

    representation  an integer vector of 8 numerators over one positive common denominator, in lowest terms
                    (cyclo16.py holds 8 Fractions);
    product         negacyclic convolution of integer vectors (x^8 = -1), one division by the gcd at the end;
    inverse         solving L(a) y = e_0 by Gaussian elimination over Q, where L(a) is the 8 x 8 matrix of
                    multiplication by a (cyclo16.py multiplies the other seven conjugates and divides by the norm);
    norm            det L(a), by fraction-free Bareiss elimination (cyclo16.py: the product of the conjugates);
    rho             sum of a_k w^k mod p, with w checked to satisfy w^8 = -1 mod p, and p checked prime by trial
                    division to its 4th root and strong-probable-prime tests to the thirteen prime bases 2 to 41,
                    deterministic below 3.3e24 (cyclo16.py: the twelve bases 2 to 37).

The cross-check reads the seeded vectors cyclo16.py writes and recomputes every result here.

Run:  python3 -I -B replay_cyclo16.py --self-test [--full]
      python3 -I -B replay_cyclo16.py --check-vectors FILE
"""
import ast
import json
import math
import os
import sys
from fractions import Fraction

N8 = 8
ALLOWED_IMPORTS = {"ast", "json", "math", "os", "sys", "fractions"}


class Cyc:
    __slots__ = ("num", "den")

    def __init__(self, num, den=1):
        num = [int(v) for v in num]
        if len(num) != N8:
            raise ValueError("need 8 numerators")
        if den == 0:
            raise ZeroDivisionError
        if den < 0:
            num, den = [-v for v in num], -den
        g = den
        for v in num:
            g = math.gcd(g, v)
        self.num = tuple(v // g for v in num)
        self.den = den // g

    @staticmethod
    def of(q):
        q = Fraction(q)
        return Cyc([q.numerator] + [0] * 7, q.denominator)

    @staticmethod
    def from_strings(xs):
        fs = [Fraction(s) for s in xs]
        d = 1
        for f in fs:
            d = d * f.denominator // math.gcd(d, f.denominator)
        return Cyc([f.numerator * (d // f.denominator) for f in fs], d)

    def coords(self):
        return [Fraction(v, self.den) for v in self.num]

    def __eq__(self, o):
        return isinstance(o, Cyc) and self.num == o.num and self.den == o.den

    def __hash__(self):
        return hash((self.num, self.den))

    def is_zero(self):
        return not any(self.num)

    def add(self, o):
        return Cyc([a * o.den + b * self.den for a, b in zip(self.num, o.num)], self.den * o.den)

    def neg(self):
        return Cyc([-a for a in self.num], self.den)

    def sub(self, o):
        return self.add(o.neg())

    def mul(self, o):
        acc = [0] * (2 * N8 - 1)
        for i, a in enumerate(self.num):
            if a:
                for j, b in enumerate(o.num):
                    acc[i + j] += a * b
        red = [acc[k] - (acc[k + N8] if k + N8 < len(acc) else 0) for k in range(N8)]
        return Cyc(red, self.den * o.den)

    def mulmatrix(self):
        """L(a): column j is a * zeta^j, as rational coordinates."""
        cols = []
        for j in range(N8):
            e = [0] * N8
            e[j] = 1
            cols.append(self.mul(Cyc(e)).coords())
        return [[cols[j][i] for j in range(N8)] for i in range(N8)]

    def inv(self):
        A = self.mulmatrix()
        rhs = [Fraction(1)] + [Fraction(0)] * 7
        M = [row[:] + [r] for row, r in zip(A, rhs)]
        for c in range(N8):
            piv = next((r for r in range(c, N8) if M[r][c] != 0), None)
            if piv is None:
                raise ZeroDivisionError("singular multiplication matrix")
            M[c], M[piv] = M[piv], M[c]
            pv = M[c][c]
            M[c] = [x / pv for x in M[c]]
            for r in range(N8):
                if r != c and M[r][c] != 0:
                    f = M[r][c]
                    M[r] = [x - f * y for x, y in zip(M[r], M[c])]
        sol = [M[r][N8] for r in range(N8)]
        d = 1
        for f in sol:
            d = d * f.denominator // math.gcd(d, f.denominator)
        return Cyc([f.numerator * (d // f.denominator) for f in sol], d)

    def norm(self):
        """det L(a) by Bareiss on the integer matrix L(num), divided by den^8."""
        B = Cyc(self.num).mulmatrix()
        A = [[int(x) for x in row] for row in B]
        sign, prev = 1, 1
        n = N8
        for k in range(n - 1):
            if A[k][k] == 0:
                sw = next((r for r in range(k + 1, n) if A[r][k] != 0), None)
                if sw is None:
                    return Fraction(0)
                A[k], A[sw] = A[sw], A[k]
                sign = -sign
            for i in range(k + 1, n):
                for j in range(k + 1, n):
                    A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
            prev = A[k][k]
        return Fraction(sign * A[n - 1][n - 1], self.den ** n)

    def sigma(self, k):
        out = [0] * N8
        for i, a in enumerate(self.num):
            e = (i * k) % 16
            if e < N8:
                out[e] += a
            else:
                out[e - N8] -= a
        return Cyc(out, self.den)


def zeta_pow(k):
    e = [0] * N8
    k %= 16
    if k < N8:
        e[k] = 1
    else:
        e[k - N8] = -1
    return Cyc(e)


def probable_prime(n):
    if n < 2:
        return False
    r = 2
    while r ** 4 <= n and r < 100000:
        if n % r == 0:
            return n == r
        r += 1
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def rho(x, p, w):
    if pow(w, 8, p) != p - 1:
        raise ValueError("w^8 != -1 mod p")
    if x.den % p == 0:
        raise ValueError("denominator divisible by p")
    s = 0
    wk = 1
    for a in x.num:
        s = (s + a * wk) % p
        wk = wk * w % p
    return s * pow(x.den, -1, p) % p


# ------------------------------------------------------------------- self-test

class Rng:
    """xorshift64*, deterministic (deliberately not the generator cyclo16.py uses)."""

    def __init__(self, seed):
        self.s = seed or 1

    def next(self):
        x = self.s
        x ^= (x >> 12) & ((1 << 64) - 1)
        x ^= (x << 25) & ((1 << 64) - 1)
        x ^= (x >> 27) & ((1 << 64) - 1)
        self.s = x & ((1 << 64) - 1)
        return (self.s * 0x2545F4914F6CDD1D) & ((1 << 64) - 1)

    def elem(self):
        num = [(self.next() % 9) - 4 for _ in range(N8)]
        return Cyc(num, 1 + self.next() % 4)


def imports_ok():
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            names.add((node.module or "").split(".")[0])
    return names <= ALLOWED_IMPORTS, sorted(names)


def axioms(rng, n, mul=None):
    mul = mul or (lambda a, b: a.mul(b))
    bad = []
    one = Cyc([1] + [0] * 7)
    z = zeta_pow(1)
    p = one
    for _ in range(8):
        p = mul(p, z)
    if p != Cyc([-1] + [0] * 7):
        bad.append("zeta^8 != -1")
    if mul(Cyc([1, -1, 0, 0, 0, 0, 0, 0]), Cyc([1] * 8)) != Cyc.of(2):
        bad.append("(1 - zeta)(1 + zeta + ... + zeta^7) != 1 - zeta^8 = 2")
    for t in range(n):
        a, b, c = rng.elem(), rng.elem(), rng.elem()
        if mul(mul(a, b), c) != mul(a, mul(b, c)) or mul(a, b) != mul(b, a):
            bad.append("assoc/comm %d" % t)
        if mul(a, b.add(c)) != mul(a, b).add(mul(a, c)):
            bad.append("distributivity %d" % t)
        if not a.is_zero():
            if a.mul(a.inv()) != one:
                bad.append("inverse %d" % t)
            if a.norm() == 0:
                bad.append("zero norm of a nonzero element %d" % t)
        if a.mul(b).norm() != a.norm() * b.norm():
            bad.append("norm not multiplicative %d" % t)
        for k in (3, 5, 7, 15):
            if a.mul(b).sigma(k) != a.sigma(k).mul(b.sigma(k)):
                bad.append("sigma_%d not multiplicative %d" % (k, t))
        prod = one
        for k in (1, 3, 5, 7, 9, 11, 13, 15):
            prod = prod.mul(a.sigma(k))
        if prod != Cyc.of(a.norm()):
            bad.append("det L(a) != product of conjugates %d" % t)
    return bad


def units():
    bad = []
    one = Cyc([1] + [0] * 7)
    z = zeta_pow(1)
    if one.sub(z).norm() != 2:
        bad.append("N(1 - zeta) != 2")
    for a in (3, 5, 7):
        u = one.sub(zeta_pow(a)).mul(one.sub(z).inv())
        if u.norm() != 1:
            bad.append("cyclotomic unit %d" % a)
    s2 = zeta_pow(2).sub(zeta_pow(6))
    if s2.mul(s2) != Cyc.of(2) or one.add(s2).norm() != 1:
        bad.append("sqrt2")
    if zeta_pow(4).mul(zeta_pow(4)) != Cyc.of(-1):
        bad.append("i^2")
    return bad


def check_vectors(path, corrupt=False):
    with open(path, encoding="ascii") as fh:
        doc = json.load(fh)
    p, w = doc["p"], doc["w"]
    bad = []
    if not probable_prime(p) or p % 16 != 1 or pow(w, 8, p) != p - 1:
        bad.append("place")
    rows = doc["rows"]
    if corrupt:
        rows = [dict(r) for r in rows]
        rows[0]["prod"] = list(rows[0]["prod"])
        rows[0]["prod"][3] = str(Fraction(rows[0]["prod"][3]) + 1)
    for t, r in enumerate(rows):
        a, b = Cyc.from_strings(r["a"]), Cyc.from_strings(r["b"])
        if a.add(b) != Cyc.from_strings(r["sum"]):
            bad.append("sum %d" % t)
        if a.mul(b) != Cyc.from_strings(r["prod"]):
            bad.append("prod %d" % t)
        if a.norm() != Fraction(r["norm_a"]):
            bad.append("norm %d" % t)
        if a.sigma(3) != Cyc.from_strings(r["sigma3_a"]):
            bad.append("sigma3 %d" % t)
        if rho(a, p, w) != r["rho_a"]:
            bad.append("rho %d" % t)
        if "inv_a" in r and a.inv() != Cyc.from_strings(r["inv_a"]):
            bad.append("inv %d" % t)
    return bad, len(rows)


def self_test(full=False):
    n = 300 if full else 30
    out, ok = [], True

    def rep(name, bad, neg=False):
        nonlocal ok
        passed = bool(bad) if neg else not bad
        ok &= passed
        out.append("%s %s%-46s %s" % ("PASS" if passed else "FAIL", "NEG " if neg else "", name,
                                      ("detected, %d failing checks" % len(bad)) if neg and bad else
                                      "; ".join(bad[:3]) or "0 failures"))

    good, names = imports_ok()
    rep("imports only %s" % ",".join(sorted(ALLOWED_IMPORTS)), [] if good else ["imports %s" % names])
    rep("field identities, norm = det = product, %d triples" % n, axioms(Rng(0x5EED0001), n))
    rep("known elements and units", units())

    def mul_plus_one(a, b):                      # mutant: x^8 = +1
        acc = [0] * N8
        for i, x in enumerate(a.num):
            for j, y in enumerate(b.num):
                acc[(i + j) % N8] += x * y
        return Cyc(acc, a.den * b.den)
    rep("mutant product with zeta^8 = +1", axioms(Rng(0x5EED0002), 5, mul=mul_plus_one), neg=True)
    zero_div = Cyc([1, -1, 0, 0, 0, 0, 0, 0])        # 1 - zeta: invertible in the field
    try:
        zero_div.inv()
        sing = []
    except ZeroDivisionError:
        sing = ["1 - zeta reported singular"]
    rep("1 - zeta is invertible (norm 2)", sing)
    bad_p = ["w^8 = 1 accepted"]
    try:
        rho(zeta_pow(1), 17, 2)                          # 2 has order 8 mod 17: 2^8 = 1
    except ValueError:
        bad_p = []
    rep("rho refuses w with w^8 != -1", bad_p)
    nneg = sum(1 for l in out if " NEG " in l)
    out.append("replay_cyclo16 self-test (%s): %d positive controls, %d negative controls: %s"
               % ("full" if full else "fast", len(out) - nneg, nneg, "ALL PASS" if ok else "FAILURE"))
    return ok, out


def main(argv):
    if argv[:1] == ["--self-test"]:
        ok, lines = self_test(full="--full" in argv[1:])
        print("\n".join(lines))
        return 0 if ok else 1
    if argv[:1] == ["--check-vectors"] and len(argv) == 2:
        bad, n = check_vectors(argv[1])
        badc, _ = check_vectors(argv[1], corrupt=True)
        print("cross-check of %d cyclo16 vectors: %s" % (n, "; ".join(bad[:5]) or "0 mismatches"))
        print("NEG a corrupted product coordinate: %s" % ("detected" if badc else "NOT detected"))
        return 0 if not bad and badc else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
