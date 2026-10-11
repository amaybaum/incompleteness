#!/usr/bin/env python3
"""indep_checkO5b.py -- coordinator's supplementary check of research/origin, round 5, node O14 (head 44c06d46): the
thread's own repeat-until-success circuit (O14-T9, NOTES-O14 S0 addendum W2) and the identity it cites for J.

Reads nothing the thread wrote.  The objects are rebuilt from their statements: uJ = [[(1-i)/2, (-1-i)/2],
[(1-i)/2, (1+i)/2]] (BridgeAvail.lean:80-81 at dev-origin/drive 86358785, carried verbatim from research/bridge @
a34d20b5); zPh = diag(1, w), w = (3 + 4i)/5; H = rot(pi/4) Z; S = diag(1, i); Tof the doubly controlled exchange of the
token's two values, controlled by two ancilla qubits; the circuit U = (1 (x) H (x) H) Tof (S (x) 1 (x) 1) Tof (1 (x) H (x) H)
on (token, a, b), the ancillas prepared in |00>.  Exact arithmetic in Q(zeta8), the same class as indep_checkO5.py
(copied, not imported).

Decision rule (fixed before run 1): VERDICT INDEP-O5B-FIXED iff Y1-Y4 all PASS and DD1-DD3 all evaluate False;
otherwise VERDICT INDEP-O5B-FAILED <items>.

Y1 the J datum is a Clifford element: uJ = e^{-i pi/4} H S^3 exactly; uJ has four nonzero entries (not monomial); uJ lies
   in <rot(pi/4), S, X> modulo phase (24 elements) and H lies in <uJ, S, X> modulo phase, which also has 24 elements.
Y2 the blocks of U at the ancilla outcome (c, d): K_00 = ((3 + i)/4) zPh, and K_01, K_10, K_11 are multiples of Z, with
   K^+K = 5/8, 1/8, 1/8, 1/8 times the identity.
Y3 with the correction Z after a failure and stop on success, the k-round channel equals
   (1 - (3/8)^k) Ad(zPh) + (3/8)^k id on the four matrix units, k = 1, 2, 3, 4.
Y4 with a spectator qubit (level two), the same protocol on the token gives (1 - (3/8)^k) Ad(zPh (x) 1) + (3/8)^k id on
   the sixteen matrix units, k = 1, 2.
Countercontrols (each must evaluate False):
DD1 without the correction after a failure, the 2-round channel equals (1 - (3/8)^2) Ad(zPh) + (3/8)^2 id.
DD2 uJ is a nonzero multiple of a monomial matrix.
DD3 with the token's S applied unconditionally (no Toffoli pair), the success block K_00 is a multiple of zPh.

Run from this directory:  python3 -I -B indep_checkO5b.py > indep_checkO5b.out 2> indep_checkO5b.err
"""
from fractions import Fraction as F


# ---------------------------------------------------------------- Q(zeta8)
class Q8:
    __slots__ = ('c',)

    def __init__(self, c=(0, 0, 0, 0)):
        self.c = tuple(F(x) for x in c)

    @staticmethod
    def of(x):
        if isinstance(x, Q8):
            return x
        return Q8((x, 0, 0, 0))

    def __add__(self, o):
        o = Q8.of(o)
        return Q8(tuple(a + b for a, b in zip(self.c, o.c)))

    __radd__ = __add__

    def __neg__(self):
        return Q8(tuple(-a for a in self.c))

    def __sub__(self, o):
        return self + (-Q8.of(o))

    def __rsub__(self, o):
        return Q8.of(o) - self

    def __mul__(self, o):
        o = Q8.of(o)
        r = [F(0)] * 4
        for i, a in enumerate(self.c):
            if a == 0:
                continue
            for j, b in enumerate(o.c):
                if b == 0:
                    continue
                k = i + j
                if k < 4:
                    r[k] += a * b
                else:
                    r[k - 4] -= a * b
        return Q8(r)

    __rmul__ = __mul__

    def conj(self):  # z -> z^-1 = -z^3, z^2 -> -z^2, z^3 -> -z
        a0, a1, a2, a3 = self.c
        return Q8((a0, -a3, -a2, -a1))

    def zero(self):
        return all(a == 0 for a in self.c)

    def __eq__(self, o):
        return self.c == Q8.of(o).c

    def __hash__(self):
        return hash(self.c)

    def inv(self):
        # solve self * x = 1 by linear algebra over Q (multiplication matrix)
        M = []
        for j in range(4):
            e = [0, 0, 0, 0]
            e[j] = 1
            M.append((self * Q8(e)).c)  # column j
        A = [[M[j][i] for j in range(4)] + [F(1) if i == 0 else F(0)] for i in range(4)]
        for col in range(4):
            piv = next(r for r in range(col, 4) if A[r][col] != 0)
            A[col], A[piv] = A[piv], A[col]
            p = A[col][col]
            A[col] = [x / p for x in A[col]]
            for r in range(4):
                if r != col and A[r][col] != 0:
                    f = A[r][col]
                    A[r] = [x - f * y for x, y in zip(A[r], A[col])]
        return Q8([A[i][4] for i in range(4)])

    def __truediv__(self, o):
        return self * Q8.of(o).inv()

    def re_im(self):
        """real and imaginary parts as (rational, rational-multiple-of-sqrt2) pairs: x = a + b z + c z^2 + d z^3,
        z = (1 + i)/sqrt2: Re = a + (b - d)/sqrt2, Im = c + (b + d)/sqrt2"""
        a, b, c, d = self.c
        return (a, (b - d) / 2), (c, (b + d) / 2)  # value = r + s*sqrt2

    def __repr__(self):
        return 'Q8' + str(tuple(str(x) for x in self.c))


Z = Q8((0, 1, 0, 0))
I_ = Q8((0, 0, 1, 0))
SQ2 = Q8((0, 1, 0, -1))
ONE, ZERO = Q8.of(1), Q8.of(0)
HALF_SQ2 = SQ2 * F(1, 2)  # 1/sqrt2


def q(x, y=0):  # x + i y, rational
    return Q8((x, 0, y, 0))


def mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(k)), ZERO) for j in range(m)] for i in range(n)]


def dg(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def scal(z, A):
    return [[Q8.of(z) * x for x in r] for r in A]


def add(A, B):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(A, B)]


def eq(A, B):
    return all(x == y for ra, rb in zip(A, B) for x, y in zip(ra, rb))


def kron(A, B):
    return [[A[i // len(B)][j // len(B[0])] * B[i % len(B)][j % len(B[0])] for j in range(len(A[0]) * len(B[0]))]
            for i in range(len(A) * len(B))]


def normalize(M):
    for r in M:
        for x in r:
            if not x.zero():
                inv = x.inv()
                return tuple(tuple(y * inv for y in row) for row in M)


def closure(gens, cap=20000):
    s = normalize(eye(len(gens[0])))
    seen, frontier = {s}, [s]
    while frontier:
        nxt = []
        for a in frontier:
            A = [list(r) for r in a]
            for G in gens:
                b = normalize(mm(A, G))
                if b not in seen:
                    seen.add(b)
                    nxt.append(b)
                    if len(seen) > cap:
                        return seen, False
        frontier = nxt
    return seen, True


def is_monomial(M):
    return all(sum(1 for x in r if not x.zero()) == 1 for r in M) and \
        all(sum(1 for r in M if not r[j].zero()) == 1 for j in range(len(M[0])))


RESULTS, CCS = {}, {}


def check(name, ok, msg):
    RESULTS[name] = bool(ok)
    print(f'[{"PASS" if ok else "FAIL"}] {name}: {msg}', flush=True)


def cc(name, val, msg):
    CCS[name] = bool(val)
    print(f'[CC] {name} = {bool(val)}: {msg}', flush=True)



def prop(A, B):
    z = None
    for ra, rb in zip(A, B):
        for x, y in zip(ra, rb):
            if y.zero():
                if not x.zero():
                    return False
                continue
            r = x / y
            if z is None:
                z = r
            elif not (r == z):
                return False
    return z is not None



W = q(F(3, 5), F(4, 5))
zPh = [[ONE, ZERO], [ZERO, W]]
Sm = [[ONE, ZERO], [ZERO, I_]]
Xm = [[ZERO, ONE], [ONE, ZERO]]
Zm = [[ONE, ZERO], [ZERO, -ONE]]
Bm = [[HALF_SQ2, -HALF_SQ2], [HALF_SQ2, HALF_SQ2]]
Hm = mm(Bm, Zm)
I2 = eye(2)
uJ = [[q(F(1, 2), F(-1, 2)), q(F(-1, 2), F(-1, 2))], [q(F(1, 2), F(-1, 2)), q(F(1, 2), F(1, 2))]]
E_m = (ONE - I_) * HALF_SQ2  # e^{-i pi/4} = (1 - i)/sqrt2

# ---------------------------------------------------------------- Y1
S3 = mm(mm(Sm, Sm), Sm)
y1a = eq(uJ, scal(E_m, mm(Hm, S3)))
y1b = sum(1 for r in uJ for x in r if not x.zero()) == 4
gB, finB = closure([Bm, Sm, Xm])
gJ, finJ = closure([uJ, Sm, Xm])
y1c = normalize(uJ) in gB
y1d = normalize(Hm) in gJ
check('Y1', y1a and y1b and finB and finJ and len(gB) == 24 and len(gJ) == 24 and y1c and y1d,
      f'uJ = e^(-i pi/4) H S^3: {y1a}; four nonzero entries: {y1b}; |<rot(pi/4), S, X>| = {len(gB)}, |<uJ, S, X>| = '
      f'{len(gJ)} modulo phase; uJ in the first: {y1c}; H in the second: {y1d}')
cc('DD2', is_monomial(uJ), 'uJ is a multiple of a monomial matrix')


# ---------------------------------------------------------------- Y2
def op3(Ud, Ua, Ub):
    return kron(kron(Ud, Ua), Ub)  # index d*4 + a*2 + b


Tof = eye(8)
for d_ in range(2):
    i_ = d_ * 4 + 3
    Tof[i_][i_] = ZERO
    Tof[i_][(1 - d_) * 4 + 3] = ONE
HH = op3(I2, Hm, Hm)
U = mm(mm(mm(mm(HH, Tof), op3(Sm, I2, I2)), Tof), HH)


def block(Um, c, d):
    return [[Um[do * 4 + c * 2 + d][di * 4] for di in range(2)] for do in range(2)]


K = {(c, d): block(U, c, d) for c in range(2) for d in range(2)}
y2 = eq(K[(0, 0)], scal(q(F(3, 4), F(1, 4)), zPh))
y2 &= all(prop(K[k], Zm) for k in [(0, 1), (1, 0), (1, 1)])
y2 &= eq(mm(dg(K[(0, 0)]), K[(0, 0)]), scal(F(5, 8), I2))
y2 &= all(eq(mm(dg(K[k]), K[k]), scal(F(1, 8), I2)) for k in [(0, 1), (1, 0), (1, 1)])
check('Y2', y2, f'K_00 = ((3+i)/4) zPh, K_01, K_10, K_11 multiples of Z, K^+K = 5/8, 1/8, 1/8, 1/8: {y2}')


# ---------------------------------------------------------------- Y3, Y4
def rounds(X, k, Ks, corr, spect):
    """k rounds with stop on success; corr is the correction after a failure (None: no correction); spect: level"""
    if k == 0:
        return X
    lift = (lambda A: kron(A, eye(2))) if spect else (lambda A: A)
    succ = mm(mm(lift(Ks[(0, 0)]), X), dg(lift(Ks[(0, 0)])))
    fail = None
    for key in [(0, 1), (1, 0), (1, 1)]:
        Kc = lift(Ks[key]) if corr is None else mm(lift(corr), lift(Ks[key]))
        t = mm(mm(Kc, X), dg(Kc))
        fail = t if fail is None else add(fail, t)
    return add(succ, rounds(fail, k - 1, Ks, corr, spect))


def units(n):
    return [[[ONE if (i == r and j == s) else ZERO for j in range(n)] for i in range(n)] for r in range(n) for s in range(n)]


y3 = True
for k in (1, 2, 3, 4):
    e = F(3, 8) ** k
    for X in units(2):
        y3 &= eq(rounds(X, k, K, Zm, False), add(scal(1 - e, mm(mm(zPh, X), dg(zPh))), scal(e, X)))
check('Y3', y3, f'k-round channel with the correction Z = (1-(3/8)^k) Ad(zPh) + (3/8)^k id on the matrix units, k = 1..4: {y3}')
zP2 = kron(zPh, eye(2))
y4 = True
for k in (1, 2):
    e = F(3, 8) ** k
    for X in units(4):
        y4 &= eq(rounds(X, k, K, Zm, True), add(scal(1 - e, mm(mm(zP2, X), dg(zP2))), scal(e, X)))
check('Y4', y4, f'with a spectator qubit: (1-(3/8)^k) Ad(zPh (x) 1) + (3/8)^k id on the 16 matrix units, k = 1, 2: {y4}')
e2 = F(3, 8) ** 2
dd1 = all(eq(rounds(X, 2, K, None, False), add(scal(1 - e2, mm(mm(zPh, X), dg(zPh))), scal(e2, X))) for X in units(2))
cc('DD1', dd1, 'without the correction the 2-round channel equals (1-(3/8)^2) Ad(zPh) + (3/8)^2 id')
U3 = mm(mm(HH, op3(Sm, I2, I2)), HH)
dd3 = prop(block(U3, 0, 0), zPh)
cc('DD3', dd3, 'with S unconditional the success block is a multiple of zPh')

fails = [k for k, ok in RESULTS.items() if not ok] + [k for k, v in CCS.items() if v]
print()
print(f'PASS {sum(RESULTS.values())}/{len(RESULTS)}; countercontrols False {sum(1 for v in CCS.values() if not v)}/{len(CCS)}')
print('VERDICT INDEP-O5B-FIXED' if not fails else 'VERDICT INDEP-O5B-FAILED ' + ' '.join(fails))
