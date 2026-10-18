"""Independent check of every arithmetic claim the LOC-1 arithmetic controls certify (research development).

Imports only the standard library and nothing from this directory: not cyclo16.py, s16_layer.py, replay_cyclo16.py,
the engine or emit_claims.py.  It reads the claims file emit_claims.py writes and decides each claim by methods the
round's code does not use:

    field       Q(zeta_16) as the tower Q < Q(i) < Q(i)(u) < Q(i)(u)(t), with u^2 = i and t^2 = u, so t is a root of
                x^8 + 1 (t^8 = u^4 = i^2 = -1).  Power-basis coordinate k = k0 + 2 k1 + 4 k2 maps to t^k0 u^k1 i^k2.
                Products by the quadratic-extension rule, inverses as conjugate over relative norm, the norm as the
                composite of the three relative norms, the trace as 8 c_0 by the composite of relative traces,
                Galois images by evaluating x at t^k with tower products, rho as the composite of the three
                place maps i -> w^4, u -> w^2, t -> w.  (cyclo16.py: power-basis convolution, conjugates;
                replay_cyclo16.py: integer vectors, elimination and a Bareiss determinant.)
    irreducible x^8 + 1 by Eisenstein at 2 after x -> x + 1.
    place       p prime by a Lucas certificate on the full factorization of p - 1, its factors proved prime by trial
                division; every q = 1 (mod 16) in (2^61, p) composite by an explicit factor or Fermat witness; w as
                a^((p - 1)/16) for the least a >= 2 with w^8 = -1, every smaller a checked.
    classes     classes of identifications Fin N -> Fin m x Fin n as pairs of transversal partitions (rows into m
                blocks of n, columns into n blocks of m), up to the factor swap when m = n; counts checked against
                N!/(m! n!) (halved when m = n).  The product test factors the reshuffle as an outer product through
                one inverse; the canonical representative and the greedy static order are written here from the
                engine's documented definitions, not from its code.
    W-CYC-16    the cycle types of all 576 permutations pi_1 x pi_2 of Fin 4 x Fin 4, against a transposition.

Every claim is reported case by case.  Countercontrols, each of which must be detected: mutant tower arithmetic,
a mutant coordinate map, a composite modulus, a w of order 8, corrupted claimed class sets, a corrupted order and
a corrupted witness; and an image-only product test, which must wrongly accept the collision instance.

Run:  python3 -I -B indep_arith_check.py --self-test
      python3 -I -B indep_arith_check.py --check CLAIMS.json
"""
import ast
import itertools
import json
import math
import os
import sys
from fractions import Fraction

ALLOWED_IMPORTS = {"ast", "itertools", "json", "math", "os", "sys", "fractions"}
F0, F1 = Fraction(0), Fraction(1)


# =================================================================== the tower Q(i)(u)(t)

class Tower:
    """Arithmetic in Q(i)(u)(t), u^2 = i, t^2 = u.  An element is ((K1, K1), (K1, K1)) pairs: x = A + B t with
    A, B in Q(i)(u), each C + D u with C, D in Q(i) = (e, f) meaning e + f i.  isq is i^2 (-1; +1 in a mutant)."""

    def __init__(self, isq=-1):
        self.isq = Fraction(isq)

    # ---- Q(i)
    def k1mul(self, x, y):
        return (x[0] * y[0] + self.isq * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def k1inv(self, x):
        n = x[0] * x[0] - self.isq * x[1] * x[1]
        if n == 0:
            raise ZeroDivisionError("zero divisor in Q(i)")
        return (x[0] / n, -x[1] / n)

    @staticmethod
    def k1add(x, y):
        return (x[0] + y[0], x[1] + y[1])

    @staticmethod
    def k1neg(x):
        return (-x[0], -x[1])

    @staticmethod
    def k1zero(x):
        return x[0] == 0 and x[1] == 0

    def k1times_i(self, x):
        return (self.isq * x[1], x[0])

    # ---- Q(i)(u), u^2 = i
    def k2mul(self, x, y):
        cc = self.k1mul(x[0], y[0])
        dd = self.k1times_i(self.k1mul(x[1], y[1]))
        return (self.k1add(cc, dd), self.k1add(self.k1mul(x[0], y[1]), self.k1mul(x[1], y[0])))

    def k2add(self, x, y):
        return (self.k1add(x[0], y[0]), self.k1add(x[1], y[1]))

    def k2neg(self, x):
        return (self.k1neg(x[0]), self.k1neg(x[1]))

    def k2zero(self, x):
        return self.k1zero(x[0]) and self.k1zero(x[1])

    def k2times_u(self, x):
        return (self.k1times_i(x[1]), x[0])

    def k2norm(self, x):
        """N_{K2/K1}(C + D u) = C^2 - D^2 i."""
        return self.k1add(self.k1mul(x[0], x[0]), self.k1neg(self.k1times_i(self.k1mul(x[1], x[1]))))

    def k2inv(self, x):
        n = self.k2norm(x)
        ni = self.k1inv(n)
        return (self.k1mul(x[0], ni), self.k1neg(self.k1mul(x[1], ni)))

    # ---- Q(i)(u)(t), t^2 = u
    def mul(self, x, y):
        aa = self.k2mul(x[0], y[0])
        bb = self.k2times_u(self.k2mul(x[1], y[1]))
        return (self.k2add(aa, bb), self.k2add(self.k2mul(x[0], y[1]), self.k2mul(x[1], y[0])))

    def add(self, x, y):
        return (self.k2add(x[0], y[0]), self.k2add(x[1], y[1]))

    def neg(self, x):
        return (self.k2neg(x[0]), self.k2neg(x[1]))

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def is_zero(self, x):
        return self.k2zero(x[0]) and self.k2zero(x[1])

    def rel_norm3(self, x):
        """N_{K3/K2}(A + B t) = A^2 - B^2 u."""
        return self.k2add(self.k2mul(x[0], x[0]), self.k2neg(self.k2times_u(self.k2mul(x[1], x[1]))))

    def inv(self, x):
        n = self.rel_norm3(x)
        ni = self.k2inv(n)
        return (self.k2mul(x[0], ni), self.k2neg(self.k2mul(x[1], ni)))

    def norm(self, x):
        """N_{K3/Q} = N_{K1/Q} o N_{K2/K1} o N_{K3/K2}."""
        c = self.k2norm(self.rel_norm3(x))
        return c[0] * c[0] - self.isq * c[1] * c[1]

    @staticmethod
    def trace(x):
        """Tr_{K3/Q} = Tr_{K1/Q} o Tr_{K2/K1} o Tr_{K3/K2}: 2 * 2 * 2 times the rational part."""
        return 8 * x[0][0][0]

    def one(self):
        return (((F1, F0), (F0, F0)), ((F0, F0), (F0, F0)))

    def zero(self):
        return (((F0, F0), (F0, F0)), ((F0, F0), (F0, F0)))

    def t(self):
        return (((F0, F0), (F0, F0)), ((F1, F0), (F0, F0)))

    def scalar(self, q):
        return (((Fraction(q), F0), (F0, F0)), ((F0, F0), (F0, F0)))

    def power(self, x, e):
        out = self.one()
        for _ in range(e):
            out = self.mul(out, x)
        return out

    # ---- coordinates: power basis zeta^k, k = k0 + 2 k1 + 4 k2  <->  t^k0 u^k1 i^k2
    @staticmethod
    def from_coords(c):
        c = [Fraction(v) for v in c]
        assert len(c) == 8
        return (((c[0], c[4]), (c[2], c[6])), ((c[1], c[5]), (c[3], c[7])))

    @staticmethod
    def to_coords(x):
        (((c0, c4), (c2, c6)), ((c1, c5), (c3, c7))) = x
        return (c0, c1, c2, c3, c4, c5, c6, c7)

    def galois(self, x, k):
        """x(t^k): evaluate the power-basis polynomial of x at t^k with tower products (Horner)."""
        c = self.to_coords(x)
        tk = self.power(self.t(), k % 16)
        out = self.zero()
        for ck in reversed(c):
            out = self.add(self.mul(out, tk), self.scalar(ck))
        return out

    def rho(self, x, p, w):
        """The place i -> w^4, u -> w^2, t -> w, composed through the tower."""
        def q(v):
            if v.denominator % p == 0:
                raise ValueError("denominator divisible by p")
            return v.numerator * pow(v.denominator, -1, p) % p
        w2, w4 = w * w % p, pow(w, 4, p)

        def r1(e):
            return (q(e[0]) + q(e[1]) * w4) % p

        def r2(e):
            return (r1(e[0]) + r1(e[1]) * w2) % p
        return (r2(x[0]) + r2(x[1]) * w) % p


class TowerBadMap(Tower):
    """Mutant coordinate map: zeta^4 read as -i (an isomorphic field, the wrong identification of coordinates)."""

    @staticmethod
    def from_coords(c):
        c = [Fraction(v) for v in c]
        return (((c[0], -c[4]), (c[2], -c[6])), ((c[1], -c[5]), (c[3], -c[7])))

    @staticmethod
    def to_coords(x):
        (((c0, c4), (c2, c6)), ((c1, c5), (c3, c7))) = x
        return (c0, c1, c2, c3, -c4, -c5, -c6, -c7)


T = Tower()


def parse_entry(v):
    """A claims-file entry (8 coordinate strings) as (tower element, normal-form key)."""
    c = tuple(Fraction(s) for s in v)
    return T.from_coords(c), c


# =================================================================== irreducibility and the place

def eisenstein_phi16():
    """Phi_16(x + 1) = (x + 1)^8 + 1: monic, every other coefficient even, constant 2 not divisible by 4."""
    coeffs = [math.comb(8, k) for k in range(9)]       # coefficient of x^k
    coeffs[0] += 1
    return coeffs[8] == 1 and all(c % 2 == 0 for c in coeffs[:8]) and coeffs[0] % 4 != 0, coeffs


def trial_prime(n):
    if n < 2:
        return False
    r = 2
    while r * r <= n:
        if n % r == 0:
            return False
        r += 1
    return True


def factor_small(n, bound=10 ** 7):
    f, d = {}, 2
    while d * d <= n and d <= bound:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    return f, n


def lucas_certificate(p):
    """(proved, detail): p prime iff some a has a^(p-1) = 1 and a^((p-1)/q) != 1 for every prime q | p - 1."""
    f, rest = factor_small(p - 1)
    if rest != 1:
        if rest > 10 ** 14 or not trial_prime(rest):
            return False, "cofactor %d of p - 1 not proved prime" % rest
        f[rest] = f.get(rest, 0) + 1
    prod = 1
    for q, e in f.items():
        if not trial_prime(q):
            return False, "factor %d not prime" % q
        prod *= q ** e
    if prod != p - 1:
        return False, "factorization does not multiply to p - 1"
    for a in range(2, 1000):
        if pow(a, p - 1, p) != 1:
            return False, "Fermat witness %d: p composite" % a
        if all(pow(a, (p - 1) // q, p) != 1 for q in f):
            return True, "p - 1 = %s, witness a = %d" % (" * ".join("%d^%d" % (q, e) if e > 1 else str(q)
                                                                    for q, e in sorted(f.items())), a)
    return False, "no Lucas witness below 1000"


def composite_witness(q):
    f, _ = factor_small(q, bound=10 ** 5)
    if f:
        return "factor %d" % min(f)
    for a in (2, 3, 5, 7):
        if pow(a, q - 1, q) != 1:
            return "Fermat witness %d" % a
    return None


def check_place(pl):
    out = []
    p, w, lo = pl["p"], pl["w"], pl["lo"]
    ok, det = lucas_certificate(p)
    out.append(("place: p = %d prime (Lucas certificate)" % p, ok, det))
    out.append(("place: p = 1 (mod 16)", p % 16 == 1, "p mod 16 = %d" % (p % 16)))
    cands = [q for q in range(lo + 1, p) if q % 16 == 1]
    wits = [(q, composite_witness(q)) for q in cands]
    out.append(("place: least such prime above 2^61", p > lo and all(wt for _, wt in wits),
                "%d smaller candidates, each composite: %s" % (len(cands), "; ".join("%d %s" % x for x in wits))))
    a = next((a for a in range(2, 10000) if pow(pow(a, (p - 1) // 16, p), 8, p) == p - 1), None)
    w_ref = pow(a, (p - 1) // 16, p) if a else None
    out.append(("place: w = a^((p-1)/16), least a >= 2 with w^8 = -1", a is not None and w == w_ref,
                "a = %s, w = %s" % (a, w_ref)))
    order = next((k for k in range(1, 17) if pow(w, k, p) == 1), None)
    out.append(("place: w has order exactly 16", order == 16, "order %s" % order))
    return out


# =================================================================== classes of identifications

def set_partitions_equal(items, k, size):
    """Unordered partitions of items into k blocks of the given size."""
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for comb in itertools.combinations(rest, size - 1):
        block = (first,) + comb
        remaining = [x for x in rest if x not in comb]
        for tail in set_partitions_equal(remaining, k - 1, size):
            yield [block] + tail


_CLASSES = {}


def classes(m, n):
    if (m, n) not in _CLASSES:
        _CLASSES[(m, n)] = _classes(m, n)
    return _CLASSES[(m, n)]


def _classes(m, n):
    """One representative sigma (tuple, sigma[i] = a n + b) per class of Fin N -> Fin m x Fin n modulo
    S_m x S_n and, when m = n, the factor swap."""
    N = m * n
    rows = list(set_partitions_equal(range(N), m, n))
    cols = list(set_partitions_equal(range(N), n, m))
    seen, out = set(), []
    for R in rows:
        rlab = {i: a for a, blk in enumerate(R) for i in blk}
        for C in cols:
            if any(len(set(rb) & set(cb)) != 1 for rb in R for cb in C):
                continue
            key = (tuple(sorted(R)), tuple(sorted(C)))
            if m == n:
                key = min(key, (key[1], key[0]))
            if key in seen:
                continue
            seen.add(key)
            clab = {i: b for b, blk in enumerate(C) for i in blk}
            out.append(tuple(rlab[i] * n + clab[i] for i in range(N)))
    return out


def class_count(m, n):
    c = math.factorial(m * n) // (math.factorial(m) * math.factorial(n))
    return c // 2 if m == n and m > 1 else c


def reshuffle(M, sig, m, n):
    N = m * n
    inv = [0] * N
    for i, g in enumerate(sig):
        inv[g] = i
    return [[M[inv[a * n + b]][inv[a2 * n + b2]] for b in range(n) for b2 in range(n)]
            for a in range(m) for a2 in range(m)]


def is_product(M, sig, m, n, F=T):
    """M^sigma = A (x) B iff the reshuffle R is an outer product: R = col (x) (row / pivot)."""
    R = reshuffle(M, sig, m, n)
    piv = next(((r, c) for r in range(len(R)) for c in range(len(R[0])) if not F.is_zero(R[r][c])), None)
    if piv is None:
        return True
    r0, c0 = piv
    ip = F.inv(R[r0][c0])
    for r in range(len(R)):
        f = F.mul(R[r][c0], ip)
        for c in range(len(R[0])):
            if F.sub(R[r][c], F.mul(f, R[r0][c])) != F.zero():
                return False
    return True


def is_product_mod(Mimg, sig, m, n, p):
    R = reshuffle(Mimg, sig, m, n)
    piv = next(((r, c) for r in range(len(R)) for c in range(len(R[0])) if R[r][c] % p), None)
    if piv is None:
        return True
    r0, c0 = piv
    ip = pow(R[r0][c0], -1, p)
    return all((R[r][c] - R[r][c0] * ip * R[r0][c]) % p == 0 for r in range(len(R)) for c in range(len(R[0])))


def canonical(sig, m, n, order):
    """The engine's documented class representative: both coordinate sequences along the static order are
    restricted-growth strings, and for m = n the first precedes the second lexicographically."""
    def rgs(seq):
        lab, out = {}, []
        for x in seq:
            lab.setdefault(x, len(lab))
            out.append(lab[x])
        return out
    s1 = rgs([sig[i] // n for i in order])
    s2 = rgs([sig[i] % n for i in order])
    if m == n and s2 < s1:
        s1, s2 = s2, s1
    res = [0] * len(sig)
    for d, i in enumerate(order):
        res[i] = s1[d] * n + s2[d]
    return tuple(res)


def is_canonical(sig, m, n, order):
    return canonical(sig, m, n, order) == tuple(sig)


def greedy_order(keys, N):
    """The documented greedy static order: the rarest index first, then repeatedly the index with the most nonzero
    links to the indices already ordered; ties by rarity, then index.  keys[k][i][j] is the normal-form key of
    target k's entry (i, j); the signature of index i is, per target, (its sorted row, its sorted column, its
    diagonal entry), sorted by the lexicographic order of normal forms."""
    sig = []
    for i in range(N):
        sig.append(tuple((tuple(sorted(K[i])), tuple(sorted(K[j][i] for j in range(N))), K[i][i]) for K in keys))
    freq = {}
    for s in sig:
        freq[s] = freq.get(s, 0) + 1
    nz = [[any(any(x != 0 for x in K[i][j]) or any(x != 0 for x in K[j][i]) for K in keys) and i != j
           for j in range(N)] for i in range(N)]
    order = [min(range(N), key=lambda i: (freq[sig[i]], i))]
    rest = set(range(N)) - set(order)
    while rest:
        nxt = min(rest, key=lambda i: (-sum(1 for j in order if nz[i][j]), freq[sig[i]], i))
        order.append(nxt)
        rest.discard(nxt)
    return order


def cycle_type(perm):
    seen, out = set(), []
    for s in range(len(perm)):
        if s in seen:
            continue
        L, x = 0, s
        while x not in seen:
            seen.add(x)
            x = perm[x]
            L += 1
        out.append(L)
    return tuple(sorted(out))


def wcyc16_types():
    types = set()
    for p1 in itertools.permutations(range(4)):
        for p2 in itertools.permutations(range(4)):
            types.add(cycle_type([p1[g // 4] * 4 + p2[g % 4] for g in range(16)]))
    return types


# =================================================================== the claims

class Mats:
    """Target matrices from the claims file: tower elements and normal-form keys."""

    def __init__(self, enc):
        self.enc = enc
        self.el, self.keys = [], []
        for M in enc:
            e, k = zip(*[zip(*[parse_entry(v) for v in row]) for row in M]) if M else ((), ())
            self.el.append([list(r) for r in e])
            self.keys.append([list(r) for r in k])


def truth_classes(mats, m, n, cache):
    key = json.dumps([mats.enc, m, n])
    if key not in cache:
        reps = classes(m, n)
        cache[key] = [r for r in reps if all(is_product(M, r, m, n) for M in mats.el)]
    return cache[key]


def check_layer(L, place, results, cache):
    p, w = place["p"], place["w"]
    planted = {json.dumps(x["matrix"]): x for x in L["planted"]}
    agree = {}

    def rep(case, ok, detail=""):
        results.append((case, ok, detail))

    for eng in L["engines"]:
        if eng["tag"] in ("plain", "layered"):
            rep("engine load %s: frozen source digest" % eng["tag"], eng["sha256"] == place["engine_sha256"],
                eng["sha256"][:16])
    for idx, r in enumerate(L["runs"]):
        mats, m, n, N = Mats(r["mats"]), r["m"], r["n"], r["m"] * r["n"]
        case = "run %02d %s %dx%d %s rules=%s arith=%s mut=%s" % (idx, r["engine"], m, n, r["mode"], r["rules"],
                                                                 r["arith"], r["mut"])
        order = greedy_order(mats.keys, N)
        order_ok = order == r["order"]
        found = [tuple(f) for f in r["found"]]
        if r["engine"].startswith("layered-place"):
            # the non-homomorphic reduction: the claim is only that it can change the class set
            truth = sorted(canonical(s, m, n, r["order"]) for s in truth_classes(mats, m, n, cache))
            agree.setdefault("badplace", []).append((idx, r["arith"], sorted(found) != truth))
            if r["arith"] == "exact":
                rep(case + " [exact N2 is unaffected by the place: equals the partition enumeration]",
                    sorted(found) == truth)
            rep(case + " [order]", order_ok)
            continue
        if r["mut"] is not None:
            truth = sorted(canonical(s, m, n, r["order"]) for s in truth_classes(mats, m, n, cache)) \
                if N <= 9 else None
            wrong = any(not all(is_product(M, f, m, n) for M in mats.el) for f in found)
            detected = r["status"] != "ALL" or wrong or (truth is not None and sorted(found) != truth)
            agree.setdefault("mut:" + r["mut"], []).append(detected)
            rep(case + " [order]", order_ok)
            continue
        if N <= 9:
            truth = sorted(canonical(s, m, n, order) for s in truth_classes(mats, m, n, cache))
            if r["mode"] == "all":
                ok = r["status"] == "ALL" and sorted(found) == truth
                det = "status %s, %d classes claimed, %d by partitions" % (r["status"], len(found), len(truth))
            else:
                ok = (r["status"] == "FOUND" and len(found) >= 1 and all(f in truth for f in found)) or \
                     (r["status"] == "NONE" and not truth and not found)
                det = "status %s, truth %d classes" % (r["status"], len(truth))
        else:
            if r["status"] == "FOUND":
                ok = all(is_canonical(f, m, n, order) and all(is_product(M, f, m, n) for M in mats.el)
                         for f in found) and len(found) >= 1
                det = "witness canonical and a product of every target"
            elif r["status"] == "NONE":
                perm = None
                M0 = mats.el[0]
                if len(mats.el) == 1 and all(sum(1 for x in row if not T.is_zero(x)) == 1 for row in M0):
                    perm = [next(j for j, x in enumerate(row) if not T.is_zero(x)) for row in M0]
                    ones = all(M0[i][perm[i]] == T.one() for i in range(N))
                ct = cycle_type(perm) if perm else None
                ok = bool(perm) and ones and sorted(perm) == list(range(N)) and ct not in wcyc16_types()
                det = "permutation matrix of cycle type %s; product permutations on 4x4 have %d cycle types, " \
                      "this one not among them (W-CYC)" % (ct, len(wcyc16_types()))
            elif r["status"] == "ALL" and r["rules"] == "R" and not found:
                ok, det = True, "status ALL with no class; decided below by the collision clauses only"
            else:
                ok, det = False, "status %s on a shape too large for partitions" % r["status"]
        rep(case, ok and order_ok, det + ("" if order_ok else "; static order differs"))
        pk = planted.get(json.dumps(r["mats"][0])) if len(r["mats"]) == 1 else None
        if pk is not None:
            sig = tuple(pk["sigma"])
            hit = all(is_product(M, sig, m, n) for M in mats.el)
            rep(case + " [planted sigma is a product]", hit)
            if r["mode"] == "all" and r["status"] == "ALL":
                rep(case + " [planted class recovered]", canonical(sig, m, n, order) in found)
        if r["rules"] == "R" and r["mut"] is None and r["mode"] == "all":
            # the collision instance: equal images to a planted product, no exact class
            imgs = [[T.rho(x, p, w) for x in row] for row in mats.el[0]]
            base = next((x for x in L["planted"] if x["m"] == m and x["n"] == n and
                         [[T.rho(parse_entry(v)[0], p, w) for v in row] for row in x["matrix"]] == imgs
                         and x["matrix"] != r["mats"][0]), None)
            if base is not None:
                sig = tuple(base["sigma"])
                Bm = [[parse_entry(v)[0] for v in row] for row in base["matrix"]]
                diff = [(i, j) for i in range(N) for j in range(N) if Bm[i][j] != mats.el[0][i][j]]
                zw = T.sub(T.t(), T.scalar(w))
                d_ok = len(diff) == 1 and T.sub(mats.el[0][diff[0][0]][diff[0][1]], Bm[diff[0][0]][diff[0][1]]) == zw
                rep(case + " [collision: differs from a planted product by zeta - w at one entry]", d_ok,
                    "entry %s" % (diff,))
                rep(case + " [collision: zeta - w != 0 and rho(zeta - w) = 0]",
                    not T.is_zero(zw) and T.rho(zw, p, w) == 0)
                rep(case + " [collision: images are a product under the planted sigma, mod p]",
                    is_product_mod(imgs, sig, m, n, p))
                rep(case + " [collision: the planted leaf is rejected exactly]",
                    not is_product(mats.el[0], sig, m, n))
                if N <= 9:
                    rep(case + " [collision: no class is an exact product]", not truth_classes(mats, m, n, cache))
                    agree["collision"] = (mats, imgs, sig, m, n)
                else:
                    agree["collision16"] = (imgs, sig, m, n)
                    results.append((case + " [collision: the engine's claim that no class of 16 points is an exact "
                                    "product]", None, "beyond partition enumeration; the control's clause is the "
                                    "planted leaf, checked above"))
    for idx, b in enumerate(L["brute"]):
        mats, m, n = Mats(b["mats"]), b["m"], b["n"]
        truth = sorted(canonical(s, m, n, b["order"]) for s in truth_classes(mats, m, n, cache))
        rep("brute %02d %s %dx%d: the control's brute force equals the partition enumeration" % (idx, b["engine"], m, n),
            sorted(tuple(c) for c in b["classes"]) == truth, "%d classes" % len(truth))
    bp = agree.get("badplace", [])
    nmod = sum(1 for _, a, _ in bp if a == "modp")
    rep("E2 load-bearing: w of order 8 gives a class set other than the exact one on some instance",
        any(d for _, a, d in bp if a == "modp") and pow(w * w % p, 8, p) == 1,
        "%d of %d completed instances differ on images; (w^2)^8 = 1 mod p; instances that raised the engine's "
        "assertion leave no run record" % (sum(1 for _, a, d in bp if a == "modp" and d), nmod))
    # the integer-equivalence claim: each plain run is followed by the layered run on the same instance
    runs = L["runs"]
    pairs = [(i, i + 1) for i in range(len(runs) - 1) if runs[i]["engine"] == "plain" and
             runs[i + 1]["engine"] == "layered" and runs[i]["mats"] == runs[i + 1]["mats"]]
    same = [i for i, j in pairs if (runs[i]["status"], runs[i]["found"], runs[i]["order"]) ==
            (runs[j]["status"], runs[j]["found"], runs[j]["order"])]
    if pairs:
        rep("E1/E3/E4: the layer equals the integer engine in status, classes and static order", len(same) == len(pairs),
            "%d of %d integer instances" % (len(same), len(pairs)))
    for k, v in sorted(agree.items()):
        if k.startswith("mut:"):
            rep("engine mutation %s: some run differs from the exact class set" % k[4:], any(v),
                "%d of %d runs" % (sum(v), len(v)))
    return agree


def check_field(doc, results, F=T):
    p, w = doc["place"]["p"], doc["place"]["w"]

    def el(v):
        return F.from_coords([Fraction(s) for s in v])

    def same(x, v):
        return tuple(F.to_coords(x)) == tuple(Fraction(s) for s in v)
    bad = {"cyclo16": [], "replay": []}
    for t, r in enumerate(doc["field"]):
        a, b = el(r["a"]), el(r["b"])
        for who in ("cyclo16", "replay"):
            c = r[who]
            if not same(F.add(a, b), c["sum"]):
                bad[who].append("sum %d" % t)
            if not same(F.mul(a, b), c["prod"]):
                bad[who].append("prod %d" % t)
            if F.norm(a) != Fraction(c["norm"]):
                bad[who].append("norm %d" % t)
            if "trace" in c and F.trace(a) != Fraction(c["trace"]):
                bad[who].append("trace %d" % t)
            for k, v in c["sigma"].items():
                if not same(F.galois(a, int(k)), v):
                    bad[who].append("sigma_%s %d" % (k, t))
            if F.rho(a, p, w) != c["rho"]:
                bad[who].append("rho %d" % t)
            if "inv" in c and not same(F.inv(a), c["inv"]):
                bad[who].append("inv %d" % t)
    n = len(doc["field"])
    results.append(("field: cyclo16 sums, products, norms, traces, all 8 Galois images, rho, inverses on %d seeded "
                    "pairs" % n, not bad["cyclo16"], "; ".join(bad["cyclo16"][:4]) or "0 mismatches"))
    results.append(("field: replay_cyclo16 sums, products, norms, 4 Galois images, rho, inverses on %d seeded pairs" % n,
                    not bad["replay"], "; ".join(bad["replay"][:4]) or "0 mismatches"))
    return bad


def check_known(doc, results):
    k = doc["known"]
    one = T.one()
    z = T.t()
    results.append(("known: zeta has coordinates e_1", tuple(T.to_coords(z)) == tuple(Fraction(s) for s in k["zeta"])))
    results.append(("known: N(1 - zeta) = 2", T.norm(T.sub(one, z)) == 2 == Fraction(k["one_minus_zeta_norm"])))
    s2 = T.sub(T.power(z, 2), T.power(z, 6))
    results.append(("known: zeta^2 - zeta^6 squares to 2 and has the claimed coordinates",
                    T.mul(s2, s2) == T.scalar(2) and tuple(T.to_coords(s2)) == tuple(Fraction(s) for s in k["sqrt2"])))
    results.append(("known: N(1 + sqrt 2) = 1", T.norm(T.add(one, s2)) == 1 == Fraction(k["one_plus_sqrt2_norm"])))
    ok = all(T.norm(T.mul(T.sub(one, T.power(z, a)), T.inv(T.sub(one, z)))) == 1 == Fraction(k["cyclotomic_unit_norms"]
                                                                                           [str(a)]) for a in (3, 5, 7))
    results.append(("known: N((1 - zeta^a)/(1 - zeta)) = 1 for a = 3, 5, 7", ok))
    results.append(("known: sigma_3(sqrt 2) = -sqrt 2, sigma_7(sqrt 2) = sqrt 2",
                    T.galois(s2, 3) == T.neg(s2) and T.galois(s2, 7) == s2))
    e_ok, co = eisenstein_phi16()
    results.append(("x^8 + 1 irreducible over Q (Eisenstein at 2 on Phi_16(x + 1))", e_ok, "coefficients %s" % co))
    results.append(("tower: t^8 = -1 and t has order 16", T.power(z, 8) == T.neg(one) and
                    next(e for e in range(1, 17) if T.power(z, e) == one) == 16))


# =================================================================== self-test and countercontrols

class LCG:
    """A 64-bit linear congruential generator (Knuth's MMIX constants), unlike either module's generator."""

    def __init__(self, seed):
        self.s = seed

    def next(self):
        self.s = (6364136223846793005 * self.s + 1442695040888963407) % (1 << 64)
        return self.s >> 33

    def elem(self, F=T):
        return F.from_coords([Fraction(int(self.next() % 11) - 5, 1 + self.next() % 5) for _ in range(8)])


def axioms(F, rng, n):
    bad = []
    one, z = F.one(), F.t()
    if F.power(z, 8) != F.neg(one):
        bad.append("t^8 != -1")
    for k in range(n):
        a, b, c = rng.elem(F), rng.elem(F), rng.elem(F)
        if F.mul(F.mul(a, b), c) != F.mul(a, F.mul(b, c)) or F.mul(a, b) != F.mul(b, a):
            bad.append("assoc/comm %d" % k)
        if F.mul(a, F.add(b, c)) != F.add(F.mul(a, b), F.mul(a, c)):
            bad.append("distributivity %d" % k)
        try:
            if F.mul(a, F.inv(a)) != one:
                bad.append("inverse %d" % k)
        except ZeroDivisionError:
            bad.append("zero divisor %d" % k)
        if F.norm(F.mul(a, b)) != F.norm(a) * F.norm(b):
            bad.append("norm %d" % k)
        if F.from_coords(F.to_coords(a)) != a:
            bad.append("coordinate round trip %d" % k)
        for kk in (3, 5, 7):
            if F.galois(F.mul(a, b), kk) != F.mul(F.galois(a, kk), F.galois(b, kk)):
                bad.append("sigma_%d %d" % (kk, k))
    # (1 + i)(1 - i) = 2 in the field, 0 when i^2 = +1
    ip = F.power(z, 4)
    if F.is_zero(F.mul(F.add(one, ip), F.sub(one, ip))):
        bad.append("(1 + i)(1 - i) = 0")
    return bad


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


def self_test():
    res = []
    good, names = imports_ok()
    res.append(("imports only %s" % ",".join(sorted(ALLOWED_IMPORTS)), good, ",".join(names)))
    b = axioms(T, LCG(0x10C1), 40)
    res.append(("tower field identities, norm, Galois, round trip, 40 seeded triples", not b, "; ".join(b[:3])))
    counts = {(m, n): (len(classes(m, n)), class_count(m, n)) for (m, n) in ((2, 2), (2, 3), (3, 2), (2, 4), (3, 3))}
    res.append(("class enumeration counts equal N!/(m! n!) (halved when m = n)",
                all(a == b for a, b in counts.values()), str({"%dx%d" % k: v[0] for k, v in counts.items()})))
    res.append(("W-CYC-16: no product permutation of 4x4 is a transposition", (2,) + (1,) * 14 not in
                {tuple(sorted(t, reverse=True)) for t in wcyc16_types()}, "%d cycle types" % len(wcyc16_types())))
    e_ok, _ = eisenstein_phi16()
    res.append(("x^8 + 1 Eisenstein at 2 after x -> x + 1", e_ok))
    neg = []
    Tm = Tower(isq=+1)
    neg.append(("NEG tower with i^2 = +1", bool(axioms(Tm, LCG(0x10C2), 5))))
    # a planted product of tower elements, then one corrupted coordinate
    rng = LCG(0x10C3)
    A = [[rng.elem() for _ in range(2)] for _ in range(2)]
    B = [[rng.elem() for _ in range(3)] for _ in range(3)]
    K = [[T.mul(A[a][a2], B[b][b2]) for a2 in range(2) for b2 in range(3)] for a in range(2) for b in range(3)]
    ident = tuple(range(6))
    res.append(("a planted 2x3 product passes the product test", is_product(K, ident, 2, 3)))
    K2 = [row[:] for row in K]
    K2[1][4] = T.add(K2[1][4], T.scalar(Fraction(1, 7)))
    neg.append(("NEG one corrupted entry fails the product test", not is_product(K2, ident, 2, 3)))
    neg.append(("NEG composite modulus refused by the Lucas certificate",
                not lucas_certificate(2305843009213694017 + 16)[0]))
    for name, detected in neg:
        res.append((name, detected, "detected" if detected else "NOT detected"))
    return res


def countercontrols(doc, agree):
    """Corrupted claims and mutant arithmetic, each of which the check must detect."""
    res = []
    # mutant coordinate map on the field rows
    r = []
    check_field({"place": doc["place"], "field": doc["field"][:5]}, r, F=TowerBadMap())
    res.append(("NEG mutant coordinate map (zeta^4 read as -i) on the field rows", any(not ok for _, ok, _ in r)))
    # w of order 8
    bad_place = dict(doc["place"])
    bad_place["w"] = doc["place"]["w"] ** 2 % doc["place"]["p"]
    res.append(("NEG w of order 8 refused", not all(ok for _, ok, _ in check_place(bad_place))))
    # composite p
    bp = dict(doc["place"])
    bp["p"] = doc["place"]["p"] + 16
    res.append(("NEG p + 16 refused as the place", not all(ok for _, ok, _ in check_place(bp))))
    # corrupted class sets, order and witness
    L = doc["layer"]
    alls = [x for x in L["runs"] if x["mode"] == "all" and x["mut"] is None and x["engine"] == "layered" and x["found"]]
    if alls:
        x = json.loads(json.dumps(alls[0]))
        x["found"] = x["found"][1:]
        res.append(("NEG a claimed class set with one class removed", not _one_run_ok(x, doc)))
        y = json.loads(json.dumps(alls[0]))
        m, n = y["m"], y["n"]
        extra = next(canonical(s, m, n, y["order"]) for s in classes(m, n)
                     if list(canonical(s, m, n, y["order"])) not in y["found"])
        y["found"] = sorted(y["found"] + [list(extra)])
        res.append(("NEG a claimed class set with a non-solution added", not _one_run_ok(y, doc)))
        z = json.loads(json.dumps(alls[0]))
        z["order"] = z["order"][1:2] + z["order"][:1] + z["order"][2:]
        res.append(("NEG a claimed static order with its first two indices swapped", not _one_run_ok(z, doc)))
    ex = [x for x in L["runs"] if x["status"] == "FOUND" and x["m"] * x["n"] == 16 and x["mut"] is None]
    if ex:
        x = json.loads(json.dumps(ex[0]))
        e = x["mats"][0][0][0]
        x["mats"][0][0][0] = [str(Fraction(e[0]) + 1)] + e[1:]
        res.append(("NEG a 4x4 witness whose target has one corrupted coordinate", not _one_run_ok(x, doc)))
    if "collision" in agree:
        mats, imgs, sig, m, n = agree["collision"]
        p = doc["place"]["p"]
        img_classes = [s for s in classes(m, n) if is_product_mod(imgs, s, m, n, p)]
        res.append(("NEG an image-only product test accepts the collision instance (so the exact leaf decides)",
                    bool(img_classes), "%d classes accepted on images" % len(img_classes)))
    if "collision16" in agree:
        imgs, sig, m, n = agree["collision16"]
        res.append(("NEG an image-only product test accepts the 4x4 collision at its planted leaf (so the exact leaf "
                    "decides)", is_product_mod(imgs, sig, m, n, doc["place"]["p"])))
    return [(name, ok, "detected" if ok else "NOT detected") for name, ok, *_ in res]


def _one_run_ok(r, doc):
    sub = {"engines": [], "planted": [], "runs": [r], "brute": []}
    out = []
    check_layer(sub, dict(doc["place"], engine_sha256=doc["engine_sha256"]), out, {})
    return all(ok for _, ok, _ in out)


def check(path):
    with open(path, encoding="ascii") as fh:
        doc = json.load(fh)
    if doc.get("schema") != "loc1-arith-claims" or doc.get("version") != 1:
        raise SystemExit("not a loc1-arith-claims v1 file")
    results = []
    results += check_place(doc["place"])
    results.append(("place: the claimed validity flag", doc["place"]["valid"] is True))
    results.append(("E4 claim: rebound names are exactly Fraction, PR, int",
                    sorted(doc["rebound"]) == ["Fraction", "PR", "int"]))
    check_known(doc, results)
    check_field(doc, results)
    cache = {}
    agree = check_layer(doc["layer"], dict(doc["place"], engine_sha256=doc["engine_sha256"]), results, cache)
    results.append(("the controls' own verdict in the claims file", doc["layer"]["self_test_ok"] is True))
    cc = countercontrols(doc, agree)
    return results, cc


def emit(results, title):
    """A case is AGREE, DISAGREE or UNDECIDED (passed None: not decided independently, and not counted as agreeing)."""
    ok, und = True, 0
    for row in results:
        name, passed = row[0], row[1]
        det = row[2] if len(row) > 2 else ""
        if passed is None:
            und += 1
            label = "UNDECIDED"
        else:
            ok &= bool(passed)
            label = "AGREE    " if passed else "DISAGREE "
        print("%s %s%s" % (label, name, ("  -- " + det) if det else ""))
    print("%s: %d cases, %d decided, %d undecided: %s" % (title, len(results), len(results) - und, und,
                                                          "ALL DECIDED CASES AGREE" if ok else "DISAGREEMENT"))
    return ok


def main(argv):
    if argv[:1] == ["--self-test"]:
        return 0 if emit(self_test(), "indep_arith_check self-test") else 1
    if argv[:1] == ["--check"] and len(argv) == 2:
        results, cc = check(argv[1])
        ok = emit(results, "independent check of %s" % os.path.basename(argv[1]))
        ok2 = emit(cc, "countercontrols (each must be detected)")
        return 0 if ok and ok2 else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
