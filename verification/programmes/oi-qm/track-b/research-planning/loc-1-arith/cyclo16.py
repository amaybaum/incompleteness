"""Exact arithmetic in Q(zeta_16), for the LOC-1 S16 layer (research development, synthetic inputs only).

Q(zeta_16) = Q[x] / (x^8 + 1), Phi_16 = x^8 + 1 irreducible over Q.  An element is held as its unique normal form,
the 8 rational coordinates on the power basis 1, zeta, ..., zeta^7 (condition E1 of S16-completeness.md).

    Q16          the field element; +, -, *, /, ** (integer exponent), ==, hash, bool and a total order on normal
                 forms (lexicographic on the coordinates; E3).  Mixed arithmetic with int and Fraction.
    zeta(k)      zeta^k.
    galois(x, k) the automorphism zeta -> zeta^k, k odd; conj = galois(., 15).
    norm, trace  N and Tr from Q(zeta_16) to Q, as the product and the sum of the 8 conjugates.
    Place        a prime p = 1 (mod 16) with a primitive 16th root of unity w mod p: the ring homomorphism
                 rho: Z[zeta]_P -> F_p, zeta -> w (E2).  It is an int subclass equal to p, so the frozen engine's
                 'x % PR' and 'pow(., PR - 2, PR)' compute rho and arithmetic mod p when PR is bound to it.
    PLACE        the place the layer uses: p the least prime = 1 (mod 16) above 2^61, w = a^((p-1)/16) for the least
                 a >= 2 with w^8 = -1 (mod p).

Inverse: x^-1 = (product of the 7 other conjugates) / N(x).  The replay's arithmetic (replay_cyclo16.py) is written
separately and uses other methods; this module imports only the standard library.

Run:  python3 -I -B cyclo16.py --self-test [--full]      field controls (fast by default; --full for CI)
      python3 -I -B cyclo16.py --emit-vectors FILE      seeded cross-check vectors for replay_cyclo16.py
"""
import json
import sys
from fractions import Fraction

DEG = 8
ODD = (1, 3, 5, 7, 9, 11, 13, 15)


def _frac(x):
    if isinstance(x, Fraction):
        return x
    if isinstance(x, int) and not isinstance(x, bool):
        return Fraction(x)
    raise TypeError("not an exact rational: %r" % (x,))


class Q16:
    __slots__ = ("c",)

    def __init__(self, coeffs=()):
        c = [_frac(x) for x in coeffs]
        if len(c) > DEG:
            raise ValueError("more than 8 coordinates; use from_poly")
        self.c = tuple(c + [Fraction(0)] * (DEG - len(c)))

    # --------------------------------------------------------------- construction and coercion
    @classmethod
    def from_poly(cls, coeffs):
        """Reduce a polynomial of any degree modulo x^8 + 1."""
        out = [Fraction(0)] * DEG
        for i, x in enumerate(coeffs):
            q, r = divmod(i, DEG)
            out[r] += -_frac(x) if q % 2 else _frac(x)
        return cls(out)

    @classmethod
    def coerce(cls, x):
        if isinstance(x, cls):
            return x
        return cls((x,))

    def is_rational(self):
        return not any(self.c[1:])

    # --------------------------------------------------------------- ring operations
    def _other(self, o):
        if isinstance(o, Q16):
            return o
        if isinstance(o, (int, Fraction)) and not isinstance(o, bool):
            return Q16((o,))
        return None

    def __add__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        return Q16(tuple(a + b for a, b in zip(self.c, o.c)))

    __radd__ = __add__

    def __neg__(self):
        return Q16(tuple(-a for a in self.c))

    def __sub__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        return Q16(tuple(a - b for a, b in zip(self.c, o.c)))

    def __rsub__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        return o - self

    def _mulpoly(self, o):
        out = [Fraction(0)] * DEG
        a, b = self.c, o.c
        for i in range(DEG):
            ai = a[i]
            if not ai:
                continue
            for j in range(DEG):
                bj = b[j]
                if not bj:
                    continue
                k = i + j
                if k < DEG:
                    out[k] += ai * bj
                else:
                    out[k - DEG] -= ai * bj        # zeta^8 = -1
        return out

    def __mul__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        return Q16(self._mulpoly(o))

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError("zero in Q(zeta_16)")
        num = Q16((1,))
        for k in ODD[1:]:
            num = num * galois(self, k)
        n = (num * self).c
        assert not any(n[1:]), "norm not rational"
        return num * Q16((1 / n[0],))

    def __truediv__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        return self * o.inverse()

    def __rtruediv__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        return o * self.inverse()

    def __pow__(self, e):
        if not isinstance(e, int):
            return NotImplemented
        base = self if e >= 0 else self.inverse()
        e = abs(e)
        out = Q16((1,))
        while e:
            if e & 1:
                out = out * base
            base = base * base
            e >>= 1
        return out

    # --------------------------------------------------------------- reduction at a place
    def __mod__(self, o):
        if isinstance(o, Place):
            return o.rho(self)
        return NotImplemented

    # --------------------------------------------------------------- comparison (normal form) and hashing
    def __eq__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        return self.c == o.c

    def __hash__(self):
        if self.is_rational():
            return hash(self.c[0])
        return hash(self.c)

    def __bool__(self):
        return any(self.c)

    def __lt__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        return self.c < o.c

    def __le__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        return self.c <= o.c

    def __gt__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        return self.c > o.c

    def __ge__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        return self.c >= o.c

    def __repr__(self):
        return "Q16(%s)" % ",".join(str(x) for x in self.c)

    def to_json(self):
        return [str(x) for x in self.c]


def zeta(k=1):
    k %= 2 * DEG
    c = [0] * DEG
    if k < DEG:
        c[k] = 1
    else:
        c[k - DEG] = -1
    return Q16(c)


def galois(x, k):
    """The automorphism zeta -> zeta^k (k odd) applied to x."""
    if k % 2 == 0:
        raise ValueError("zeta -> zeta^k is an automorphism only for odd k")
    out = Q16()
    for i, ci in enumerate(x.c):
        if ci:
            out = out + zeta(i * k) * Q16((ci,))
    return out


def conj(x):
    return galois(x, 15)


def norm(x):
    out = Q16((1,))
    for k in ODD:
        out = out * galois(x, k)
    assert out.is_rational()
    return out.c[0]


def trace(x):
    out = Q16()
    for k in ODD:
        out = out + galois(x, k)
    assert out.is_rational()
    return out.c[0]


# ------------------------------------------------------------------- the place (E2)

MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)     # deterministic below 3.18e23


def is_prime(n):
    if n < 2:
        return False
    for b in MR_BASES:
        if n % b == 0:
            return n == b
    if n >= 318665857834031151167461:
        raise ValueError("Miller-Rabin with these bases is not deterministic above 3.18e23")
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for b in MR_BASES:
        x = pow(b, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


class Place(int):
    """p = 1 (mod 16) prime with w of order 16 mod p; equal to p as an int."""

    def __new__(cls, p, w):
        obj = int.__new__(cls, p)
        obj.w = w % p
        obj.wpow = [pow(obj.w, i, p) for i in range(DEG)]
        return obj

    @property
    def p(self):
        return int(self)

    def valid(self):
        p, w = int(self), self.w
        return is_prime(p) and p % 16 == 1 and pow(w, 8, p) == p - 1

    def rho(self, x):
        """rho(x) in F_p, as a plain int; refuses an element with a denominator divisible by p."""
        p = int(self)
        if not isinstance(x, Q16):
            x = Q16.coerce(x)
        acc = 0
        for ci, wi in zip(x.c, self.wpow):
            if ci:
                if ci.denominator % p == 0:
                    raise ValueError("a denominator is divisible by p: rho is undefined")
                acc += ci.numerator * pow(ci.denominator, p - 2, p) * wi
        return acc % p

    def omega_int(self):
        return self.w


def least_place(lo=(1 << 61)):
    p = lo + 1
    while not (p % 16 == 1 and is_prime(p)):
        p += 1
    a = 2
    while pow(pow(a, (p - 1) // 16, p), 8, p) != p - 1:
        a += 1
    return Place(p, pow(a, (p - 1) // 16, p))


PLACE = least_place()


# ------------------------------------------------------------------- controls

class SM64:
    """SplitMix64, as in the frozen engine (integer only, deterministic)."""

    def __init__(self, seed):
        self.s = seed & ((1 << 64) - 1)

    def next(self):
        M = (1 << 64) - 1
        self.s = (self.s + 0x9E3779B97F4A7C15) & M
        z = self.s
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & M
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & M
        return z ^ (z >> 31)

    def below(self, k):
        lim = (1 << 64) - ((1 << 64) % k)
        while True:
            x = self.next()
            if x < lim:
                return x % k


def rand_elem(rng, F=None, span=5, dens=8, denoms=(1, 2, 3, 4)):
    F = F or Q16
    c = [0] * DEG
    for _ in range(dens):
        c[rng.below(DEG)] = Fraction(rng.below(2 * span + 1) - span, denoms[rng.below(len(denoms))])
    return F(c)


def field_checks(F, rng, n):
    """Field identities on n seeded triples, with F the element class (a mutant may be passed).  Returns failures."""
    bad = []
    one, z = F((1,)), F((0, 1))
    zp = one
    for _ in range(8):
        zp = zp * z
    if zp != F((-1,)):
        bad.append("zeta^8 != -1")
    zq = one
    order = None
    for k in range(1, 17):
        zq = zq * z
        if zq == one:
            order = k
            break
    if order != 16:
        bad.append("zeta has order %s, not 16" % order)
    for t in range(n):
        a, b, c = rand_elem(rng, F), rand_elem(rng, F), rand_elem(rng, F)
        if (a * b) * c != a * (b * c):
            bad.append("associativity %d" % t)
        if a * b != b * a:
            bad.append("commutativity %d" % t)
        if a * (b + c) != a * b + a * c:
            bad.append("distributivity %d" % t)
        if a + F() != a or a * one != a or a - a != F():
            bad.append("identities %d" % t)
        if a:
            try:
                if a * a.inverse() != one:
                    bad.append("inverse %d" % t)
            except (ZeroDivisionError, AssertionError) as e:
                bad.append("inverse %d: %s" % (t, e))
    return bad


def galois_checks(rng, n, gal=None):
    gal = gal or galois
    bad = []
    for t in range(n):
        a, b = rand_elem(rng), rand_elem(rng)
        for k in ODD:
            if gal(a * b, k) != gal(a, k) * gal(b, k) or gal(a + b, k) != gal(a, k) + gal(b, k):
                bad.append("sigma_%d not a ring homomorphism (%d)" % (k, t))
            for l in (3, 5):
                if gal(gal(a, k), l) != gal(a, k * l % 16):
                    bad.append("sigma_%d o sigma_%d != sigma_%d (%d)" % (l, k, k * l % 16, t))
        if conj(conj(a)) != a:
            bad.append("conj o conj != id (%d)" % t)
        if norm(a * b) != norm(a) * norm(b):
            bad.append("norm not multiplicative (%d)" % t)
        if trace(a) != 8 * a.c[0]:
            bad.append("Tr(x) != 8 c_0 (%d)" % t)
        if a and norm(a) <= 0:
            bad.append("N(x) not positive for x != 0 (%d)" % t)       # N = product of |sigma(x)|^2 over 4 pairs
        r = a * conj(a)
        if conj(r) != r:
            bad.append("x conj(x) not real (%d)" % t)
    return bad


def unit_checks():
    """Known elements: zeta, i, sqrt 2, cyclotomic units, 1 - zeta."""
    bad = []
    z, one = zeta(1), Q16((1,))
    i, s2 = zeta(4), zeta(2) - zeta(6)
    if i * i != -one:
        bad.append("i^2 != -1")
    if s2 * s2 != Q16((2,)):
        bad.append("sqrt2^2 != 2")
    if norm(z) != 1:
        bad.append("N(zeta) != 1")
    if norm(one - z) != 2:
        bad.append("N(1 - zeta) != Phi_16(1) = 2")
    for a in (3, 5, 7):
        u = (one - zeta(a)) / (one - z)
        if norm(u) != 1:
            bad.append("N((1-zeta^%d)/(1-zeta)) != 1" % a)
    if norm(one + s2) != 1:
        bad.append("N(1 + sqrt2) != 1")
    if galois(s2, 3) != -s2 or galois(s2, 7) != s2:
        bad.append("Galois action on sqrt2")
    if zeta(-1) * z != one or z ** -1 != zeta(15):
        bad.append("zeta^-1")
    if Q16.from_poly([0] * 8 + [1]) != Q16((-1,)):
        bad.append("from_poly does not reduce x^8 to -1")
    return bad


def place_checks(P, rng, n):
    bad = []
    p = int(P)
    if not P.valid():
        bad.append("place invalid: p prime, p = 1 (mod 16), w^8 = -1")
    if P.rho(zeta(1)) != P.w:
        bad.append("rho(zeta) != w")
    if pow(P.rho(zeta(1)), 8, p) != p - 1:
        bad.append("rho(zeta)^8 != -1")
    for t in range(n):
        a, b = rand_elem(rng), rand_elem(rng)
        if P.rho(a + b) != (P.rho(a) + P.rho(b)) % p or P.rho(a * b) != P.rho(a) * P.rho(b) % p:
            bad.append("rho not a ring homomorphism (%d)" % t)
        if (a % P) != P.rho(a):
            bad.append("x %% PR != rho(x) (%d)" % t)
    k = zeta(1) - Q16((P.w,))
    if not k or P.rho(k) != 0:
        bad.append("zeta - w is not a nonzero element of ker rho")
    try:
        P.rho(Q16((Fraction(1, p),)))
        bad.append("rho accepted a denominator divisible by p")
    except ValueError:
        pass
    return bad


# ------------------------------------------------------------------- negative controls (mutant arithmetic)

class MutPlusOne(Q16):
    """Mutant: reduces with zeta^8 = +1 (the ring Q[x]/(x^8 - 1), not a field)."""
    __slots__ = ()

    def __mul__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        out = [Fraction(0)] * DEG
        for i in range(DEG):
            for j in range(DEG):
                out[(i + j) % DEG] += self.c[i] * o.c[j]
        return MutPlusOne(out)

    __rmul__ = __mul__

    def _other(self, o):
        if isinstance(o, Q16):
            return o
        if isinstance(o, (int, Fraction)):
            return MutPlusOne((o,))
        return None

    def __add__(self, o):
        r = Q16.__add__(self, o)
        return MutPlusOne(r.c)

    __radd__ = __add__

    def __sub__(self, o):
        return MutPlusOne(Q16.__sub__(self, o).c)


class MutNoReduce(Q16):
    """Mutant: drops the terms of degree >= 8 instead of reducing them."""
    __slots__ = ()

    def __mul__(self, o):
        o = self._other(o)
        if o is None:
            return NotImplemented
        out = [Fraction(0)] * DEG
        for i in range(DEG):
            for j in range(DEG - i):
                out[i + j] += self.c[i] * o.c[j]
        return MutNoReduce(out)

    __rmul__ = __mul__

    def __add__(self, o):
        return MutNoReduce(Q16.__add__(self, o).c)

    __radd__ = __add__

    def __sub__(self, o):
        return MutNoReduce(Q16.__sub__(self, o).c)


def mut_galois_even(x, k):
    """Mutant Galois map zeta -> zeta^(k+1): an even exponent, not an automorphism."""
    out = Q16()
    for i, ci in enumerate(x.c):
        if ci:
            out = out + zeta(i * (k + 1)) * Q16((ci,))
    return out


def self_test(full=False):
    n = 400 if full else 40
    lines, ok = [], True

    def rep(name, bad, expect_fail=False):
        nonlocal ok
        passed = (bool(bad) if expect_fail else not bad)
        ok &= passed
        lines.append("%-4s %-44s %s" % ("PASS" if passed else "FAIL", name,
                                        ("detected, %d failing checks, first: %s" % (len(bad), bad[0]))
                                        if expect_fail and bad else
                                        ("; ".join(bad[:3]) if bad else "0 failures")))

    rep("field identities, %d seeded triples" % n, field_checks(Q16, SM64(0x51160001), n))
    ng = n if full else n // 4
    rep("Galois action, norm and trace, %d pairs" % ng, galois_checks(SM64(0x51160002), ng))
    rep("known elements and units", unit_checks())
    rep("place: p = %d, w = %d" % (int(PLACE), PLACE.w), place_checks(PLACE, SM64(0x51160003), n))
    lines.append("--   negative controls (each must fail)")
    rep("NEG mutant zeta^8 = +1", field_checks(MutPlusOne, SM64(0x51160004), 10), expect_fail=True)
    rep("NEG mutant without reduction", field_checks(MutNoReduce, SM64(0x51160005), 10), expect_fail=True)
    rep("NEG mutant Galois map zeta -> zeta^(k+1)", galois_checks(SM64(0x51160006), 3, gal=mut_galois_even),
        expect_fail=True)
    bad_w = Place(int(PLACE), PLACE.w * PLACE.w)          # w^2 has order 8, so w'^8 = 1
    rep("NEG place with w of order 8", place_checks(bad_w, SM64(0x51160007), 5), expect_fail=True)
    bad_p = Place(int(PLACE) + 16, PLACE.w)               # p + 16 = 1 (mod 16) but w is not a root there
    rep("NEG place with w not a 16th root mod p", place_checks(bad_p, SM64(0x51160008), 5), expect_fail=True)
    npos = sum(1 for l in lines if l.startswith(("PASS", "FAIL")) and "NEG" not in l)
    nneg = sum(1 for l in lines if "NEG" in l)
    lines.append("cyclo16 self-test (%s): %d positive controls, %d negative controls: %s"
                 % ("full" if full else "fast", npos, nneg, "ALL PASS" if ok else "FAILURE"))
    return ok, lines


def emit_vectors(path, n=60):
    """Seeded elements and this module's results, for replay_cyclo16.py --check-vectors."""
    rng = SM64(0x51160010)
    rows = []
    for _ in range(n):
        a, b = rand_elem(rng), rand_elem(rng)
        row = {"a": a.to_json(), "b": b.to_json(), "sum": (a + b).to_json(), "prod": (a * b).to_json(),
               "norm_a": str(norm(a)), "sigma3_a": galois(a, 3).to_json(), "rho_a": a % PLACE}
        if a:
            row["inv_a"] = a.inverse().to_json()
        rows.append(row)
    doc = {"schema": "loc1-cyclo16-vectors", "version": 1, "p": int(PLACE), "w": PLACE.w, "rows": rows}
    with open(path, "w", encoding="ascii") as fh:
        json.dump(doc, fh, sort_keys=True, separators=(",", ":"))
        fh.write("\n")
    return len(rows)


def main(argv):
    if argv[:1] == ["--self-test"]:
        ok, lines = self_test(full="--full" in argv[1:])
        print("\n".join(lines))
        return 0 if ok else 1
    if argv[:1] == ["--emit-vectors"] and len(argv) == 2:
        print("wrote %d vectors" % emit_vectors(argv[1]))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
