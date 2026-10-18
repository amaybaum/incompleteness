#!/usr/bin/env python3
"""KTOKEN-MAXCONE-1 exact layer at k = 3, in Q(i), standard library only.

Finite exact witnesses, not a kernel proof and not a universal statement. Nothing is imported
from the Lean kernel or from any landed checker. Tokens are ordered with token 0 the most
significant bit of a basis index a in 0..7.

Positive checks: DICT3, PRODUCT3, REACH3, DEMUX3, ADJOINT3, QUANTUM3.
Countercontrols, each a literal witness that the named hypothesis fails for a cone meeting the
others (the family arguments are written in the preregistration): ZERO3 (hH1), SCALE3 (hsmul),
ADD3 (hadd), SHIFT3 (hmax), SEP3 (hH2), ORBIT3 (hA), CUT3 (connectivity), SLICE3 (route (c)).

  python3 -I -B ktoken_maxcone1_probe.py              # the checks; final line VERDICT KTOKEN-K3-EXACT
  python3 -I -B ktoken_maxcone1_probe.py --self-test  # the checks, then five mutations, each rejected
"""
import argparse
import sys
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product


class G:
    """A Gaussian rational re + i*im."""
    __slots__ = ('re', 'im')

    def __init__(self, re=0, im=0):
        self.re, self.im = F(re), F(im)

    @staticmethod
    def of(x):
        return x if isinstance(x, G) else G(x)

    def __add__(self, o):
        o = G.of(o); return G(self.re + o.re, self.im + o.im)
    __radd__ = __add__

    def __sub__(self, o):
        o = G.of(o); return G(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return G.of(o) - self

    def __neg__(self):
        return G(-self.re, -self.im)

    def __mul__(self, o):
        o = G.of(o); return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def norm2(self):
        return self.re * self.re + self.im * self.im

    def __truediv__(self, o):
        o = G.of(o); n = o.norm2()
        if n == 0:
            raise ZeroDivisionError
        p = self * o.conj(); return G(p.re / n, p.im / n)

    def __eq__(self, o):
        o = G.of(o); return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __bool__(self):
        return self.re != 0 or self.im != 0

    def __repr__(self):
        return f'G({self.re},{self.im})'


I = G(0, 1)


def mat(rows):
    return [[G.of(x) for x in r] for r in rows]


def zeros(n, m=None):
    return [[G() for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    return [[G(1 if i == j else 0) for j in range(n)] for i in range(n)]


def diag(*xs):
    m = zeros(len(xs))
    for i, x in enumerate(xs):
        m[i][i] = G.of(x)
    return m


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), G()) for j in range(len(b[0]))]
            for i in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(c, a):
    return [[G.of(c) * x for x in r] for r in a]


def adj(a):
    return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]


def transpose(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), G())


def kron(a, b):
    return [[a[i][j] * b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def tensor(*xs):
    out = [[G(1)]]
    for x in xs:
        out = kron(out, x)
    return out


def col(v):
    return [[G.of(x)] for x in v]


def outer(v):
    return mul(v, adj(v))


def conj_by(u, a):
    return mul(mul(u, a), adj(u))


def extract(a, idx):
    return [[a[i][j] for j in idx] for i in idx]


def det(a):
    a = [r[:] for r in a]; n = len(a); d = G(1)
    for c in range(n):
        p = next((r for r in range(c, n) if a[r][c]), None)
        if p is None:
            return G()
        if p != c:
            a[c], a[p] = a[p], a[c]; d = -d
        d = d * a[c][c]
        for r in range(c + 1, n):
            f = a[r][c] / a[c][c]
            if f:
                a[r] = [x - f * y for x, y in zip(a[r], a[c])]
    return d


def rank(a):
    a = [r[:] for r in a]; rk = 0; rows, cols = len(a), len(a[0])
    for c in range(cols):
        p = next((r for r in range(rk, rows) if a[r][c]), None)
        if p is None:
            continue
        a[rk], a[p] = a[p], a[rk]
        for r in range(rows):
            if r != rk and a[r][c]:
                f = a[r][c] / a[rk][c]
                a[r] = [x - f * y for x, y in zip(a[r], a[rk])]
        rk += 1
    return rk


def hermitian(a):
    return a == adj(a)


def psd(a):
    """Exact: Hermitian and every principal minor nonnegative."""
    if not hermitian(a):
        return False
    n = len(a)
    for r in range(1, n + 1):
        for idx in combinations(range(n), r):
            m = det(extract(a, idx))
            if m.im != 0 or m.re < 0:
                return False
    return True


def ket(n, a):
    return col([1 if i == a else 0 for i in range(n)])


def cnot(i, j, k=3):
    out = zeros(2 ** k)
    for a in range(2 ** k):
        b = a ^ (1 << (k - 1 - j)) if (a >> (k - 1 - i)) & 1 else a
        out[b][a] = G(1)
    return out


def local(g, j, k=3):
    return tensor(*(g if t == j else eye(2) for t in range(k)))


def ptran(a, token, k=3):
    out = zeros(2 ** k); bit = 1 << (k - 1 - token)
    for i, j in product(range(2 ** k), repeat=2):
        ii, jj = (i ^ bit, j ^ bit) if bool(i & bit) != bool(j & bit) else (i, j)
        out[ii][jj] = a[i][j]
    return out


def is_pure_product(v):
    """Every one-token matricization of the 8-vector v has rank 1."""
    for j in range(3):
        m = [[v[a] for a in range(8) if ((a >> (2 - j)) & 1) == b] for b in (0, 1)]
        if rank(m) != 1:
            return False
    return True


def fsqrt(x):
    """Exact square root of a nonnegative rational square, else an assertion."""
    x = F(x); roots = []
    for part in (x.numerator, x.denominator):
        r = int(part ** 0.5)
        while r * r > part:
            r -= 1
        while (r + 1) * (r + 1) <= part:
            r += 1
        assert r * r == part, x
        roots.append(r)
    return F(roots[0], roots[1])


PAULI = [eye(2), mat([[0, 1], [1, 0]]), mat([[0, -I], [I, 0]]), diag(1, -1)]
# Rational points on the unit circle, and the cyclic matrix of the landed EqvK2Converse.cycMat.
CIRCLES = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17)), (F(7, 25), F(24, 25))]
CYC = mat([[G(F(1, 2), F(-1, 2)), G(F(-1, 2), F(-1, 2))], [G(F(1, 2), F(-1, 2)), G(F(1, 2), F(1, 2))]])
HALF = mat([[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]])        # |+><+|
P0, P1 = diag(1, 0), diag(0, 1)


def phase(c, s):
    return diag(1, G(c, s))                                   # the third-axis flow, det cis t


def su_of(p, q, r):
    return scale(G(1) / G(r), mat([[p, -q.conj()], [q, p.conj()]]))


def mux(blocks):
    """Block-diagonal family on the last token, controlled by the earlier tokens."""
    n = 2 * len(blocks); out = zeros(n)
    for b, m in enumerate(blocks):
        for i in range(2):
            for j in range(2):
                out[2 * b + i][2 * b + j] = m[i][j]
    return out


def run(mutation=None):
    count = Counter()

    def check(code, ok):
        if not ok:
            raise AssertionError(code)
        count[code] += 1

    # DICT3: the k-fold Pauli dictionary inverts Pauli coordinates, with the factor 2^k = 8.
    paulis = [tensor(*(PAULI[t] for t in mu)) for mu in product(range(4), repeat=3)]
    v = col([1, G(2, 1), G(0, -1), 3, G(1, -1), 2, -1, I])
    a = add(outer(v), scale(-2, outer(ket(8, 3))))
    coeff = [trace(mul(a, p)) for p in paulis]
    factor = 4 if mutation == 'trace-factor' else 8
    rec = zeros(8)
    for c, p in zip(coeff, paulis):
        rec = add(rec, scale(c / factor, p))
    check('DICT3', rec == a)
    check('DICT3', all(c.im == 0 for c in coeff))
    for p in paulis:
        check('DICT3', hermitian(p) and mul(p, p) == eye(8))
    for p, q in combinations(paulis, 2):
        check('DICT3', trace(mul(p, q)) == 0)

    # PRODUCT3: products of one-token PSD factors are PSD of rank 1, 2, 4, 8.
    for ranks in ((1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)):
        p = tensor(*(diag(1, r - 1) for r in ranks))
        check('PRODUCT3', psd(p) and rank(p) == ranks[0] * ranks[1] * ranks[2])

    # DEMUX3: two-axis multiplexors from target rotations and CNOTs (Gray order) equal the
    # branchwise signed products; ADJOINT3: the circuit is unitary.
    gray = [0, 1, 3, 2]
    for axis in ('y', 'z'):
        rots = [mat([[c, -s], [s, c]]) if axis == 'y' else diag(G(c, s), G(c, -s)) for c, s in CIRCLES]
        u = eye(8)
        for j, r in enumerate(rots):
            u = mul(local(r, 2), u)
            changed = gray[j] ^ gray[(j + 1) % 4]
            u = mul(cnot(1 if changed == 1 else 0, 2), u)
        blocks = []
        for b in range(4):
            blk = eye(2)
            for gcode, r in zip(gray, rots):
                blk = mul(adj(r) if bin(b & gcode).count('1') % 2 else r, blk)
            blocks.append(blk)
        check('DEMUX3', u == mux(blocks))
        dag = transpose(u) if mutation == 'adjoint' else adj(u)
        check('ADJOINT3', mul(dag, u) == eye(8))

    # REACH3: the recursion rebuilds x x^dagger from a first-token vector with |0> on the others,
    # by multiplexed SU(2) blocks on the last token, then on the middle token; zero blocks use 1.
    def reach(x):
        level, words = x, []
        for depth in (2, 1):
            blocks, norms = [], []
            for b in range(len(level) // 2):
                p, q = level[2 * b][0], level[2 * b + 1][0]
                r = fsqrt(p.norm2() + q.norm2())
                su = eye(2) if r == 0 else su_of(p, q, r)
                check('REACH3', mul(adj(su), su) == eye(2) and det(su) == 1)
                blocks.append(su); norms.append(r)
            words.append((depth, mux(blocks)))
            level = col(norms)
        u = eye(8)
        for depth, m in reversed(words):
            u = mul(kron(m, eye(2)) if depth == 1 else m, u)
        start = tensor(level, ket(2, 0), ket(2, 0))
        check('REACH3', all(t[0].im == 0 and t[0].re >= 0 for t in level))
        check('REACH3', mul(u, start) == x and outer(mul(u, start)) == outer(x))

    def blk(n, c, s, ph):
        return [G(n) * G(c), G(n) * G(s) * ph]
    w = [F(9, 5), F(12, 5), F(20, 13), F(48, 13)]           # block norms; pairs of norm 3, 4; top (3, 4)
    x1 = col(blk(w[0], F(3, 5), F(4, 5), I) + blk(w[1], F(5, 13), F(12, 13), -1)
             + blk(w[2], F(8, 17), F(15, 17), G(F(3, 5), F(4, 5))) + blk(w[3], F(7, 25), F(24, 25), -I))
    x2 = col(blk(3, F(3, 5), F(4, 5), I) + [0, 0] + blk(4, F(5, 13), F(12, 13), 1) + [0, 0])
    x3 = col([0] * 8)
    for x in (x1, x2, x3, ket(8, 0), ket(8, 7)):
        reach(x)

    # QUANTUM3: the PSD cone meets every hypothesis on exact samples: products of ball states,
    # sums, nonnegative scaling, nonnegativity on product effects, CNOT into later tokens and the
    # flow and cyclic map off token 0.
    ball = [diag(1, 0), diag(F(1, 2), F(1, 2)), HALF,
            mat([[F(1, 2), G(F(3, 10), F(-2, 5))], [G(F(3, 10), F(2, 5)), F(1, 2)]])]
    ghz = outer(add(ket(8, 0), ket(8, 7)))
    samples = [tensor(ball[0], ball[2], ball[3]), tensor(ball[1], ball[3], ball[2]), ghz,
               add(outer(v), ghz)]
    for s in samples:
        check('QUANTUM3', psd(s))
    check('QUANTUM3', psd(add(samples[0], samples[2])) and psd(scale(F(5, 3), samples[3])))
    effects = [diag(0, 0), eye(2), P0, P1, HALF, diag(F(1, 3), F(2, 3))]
    for s in samples:
        for e in product(effects, repeat=3):
            val = trace(mul(s, tensor(*e)))
            check('QUANTUM3', val.im == 0 and val.re >= 0)
    gens = [cnot(i, j) for i in range(3) for j in range(3) if i < j]
    gens += [local(phase(c, s), j) for j in (1, 2) for c, s in CIRCLES[:2]] + [local(CYC, j) for j in (1, 2)]
    for gate in gens:
        check('QUANTUM3', mul(adj(gate), gate) == eye(8))
        for s in samples:
            check('QUANTUM3', psd(conj_by(gate, s)))

    # Countercontrols.
    check('ZERO3', tensor(ball[0], ball[0], ball[0]) != zeros(8))               # hH1 fails for {0}
    prod_state = tensor(ball[0], ball[2], ball[3])
    check('SCALE3', trace(prod_state) == 1 and trace(scale(F(1, 2), prod_state)).re < 1)
    a2, a1 = diag(1, 1, 0, 0, 0, 0, 0, 0), outer(ket(8, 2))
    check('ADD3', rank(a2) == 2 and rank(a1) == 1 and rank(add(a1, a2)) == 3)
    sign = 2 if mutation == 'shift-sign' else -2
    shift = add(eye(8), scale(sign, outer(ket(8, 0))))
    check('SHIFT3', psd(add(shift, scale(trace(shift) / 6, eye(8)))))
    check('SHIFT3', trace(mul(shift, tensor(P0, P0, P0))) == -1)
    ent = conj_by(cnot(0, 1), tensor(HALF, P0, P0))
    check('SEP3', psd(ent) and det(extract(ptran(ent, 0), (2, 4))) == F(-1, 4))
    bell = scale(F(1, 2), outer(add(ket(8, 0), ket(8, 6))))
    cut = cnot(2, 1) if mutation == 'cut-direction' else cnot(1, 2)
    g3 = conj_by(cut, bell)
    check('CUT3', psd(g3) and det(extract(ptran(g3, 2), (1, 6))) == F(-1, 4))
    maps = []
    for cols in permutations(range(1, 8), 3):
        perm = [0] * 8
        for t in range(8):
            for j in range(3):
                if (t >> j) & 1:
                    perm[t] ^= cols[j]
        if len(set(perm)) == 8:
            maps.append(perm)
    if mutation == 'group-below-168':
        maps = maps[:-1]
    check('ORBIT3', len(maps) == 168 and len({tuple(p) for p in maps}) == 168)
    src = mul(cnot(1, 2), mul(cnot(0, 1), tensor(col([3, 4]), col([5, 12]), col([1, 2]))))
    for token in (1, 2):
        dest = [r[0] for r in mul(local(CYC, token), src)]
        check('ORBIT3', all(not is_pure_product([dest[p[t]] for t in range(8)]) for p in maps))
    gv = add(ket(8, 0), ket(8, 7))
    wit = add(eye(8), scale(F(-3, 4), outer(gv)))
    check('SLICE3', mul(adj(gv), mul(wit, gv))[0][0] == -1)
    units = [col([1, 0]), col([0, 1]), col([F(3, 5), F(4, 5)]), col([F(3, 5), G(0, F(4, 5))]),
             col([F(5, 13), F(-12, 13)])]
    for t in range(3):
        for u in units:
            iso = tensor(*(u if s == t else eye(2) for s in range(3)))   # |u> on token t
            contr = mul(mul(adj(iso), wit), iso)
            check('SLICE3', psd(contr))
    for q in product(units, repeat=3):
        qv = tensor(*q)
        val = mul(adj(qv), mul(wit, qv))[0][0]
        check('SLICE3', val.im == 0 and val.re >= F(1, 4))
    drive = mul(cnot(0, 2), cnot(0, 1))
    check('SLICE3', trace(mul(tensor(HALF, P0, P0), conj_by(drive, wit))) == F(-1, 2))
    return count


CODES = ['DICT3', 'PRODUCT3', 'REACH3', 'DEMUX3', 'ADJOINT3', 'QUANTUM3',
         'ZERO3', 'SCALE3', 'ADD3', 'SHIFT3', 'SEP3', 'ORBIT3', 'CUT3', 'SLICE3']
MUTATIONS = [('trace-factor', 'DICT3'), ('adjoint', 'ADJOINT3'), ('shift-sign', 'SHIFT3'),
             ('group-below-168', 'ORBIT3'), ('cut-direction', 'CUT3')]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--self-test', action='store_true')
    args = ap.parse_args()
    count = run()
    assert set(count) == set(CODES), sorted(count)
    for code in CODES:
        print(f'PASS {code} ({count[code]})')
    print(f'checks: {sum(count.values())}, failures: 0')
    if args.self_test:
        for mutation, code in MUTATIONS:
            try:
                run(mutation)
            except AssertionError as exc:
                if str(exc) != code:
                    print(f'FAIL mutation {mutation}: expected {code}, got {exc}')
                    sys.exit(1)
                print(f'REJECTED {mutation}: {code}')
            else:
                print(f'FAIL mutation {mutation} accepted')
                sys.exit(1)
        print('mutations: 5 rejected, 0 accepted')
    print('VERDICT KTOKEN-K3-EXACT')


if __name__ == '__main__':
    main()
