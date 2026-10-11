#!/usr/bin/env python3
"""indep_checkO5.py -- coordinator's independent check of research/origin, round 5, node O14 (head 44c06d46).

Reads nothing the thread wrote.  Objects rebuilt from the definitions, as read at L and in the thread's notes as
statements: the drive D = diag(1, w), w = (3 + 4i)/5 = e^{i theta0}, cos theta0 = 3/5; the quarter phase S = diag(1, i);
the balanced mixer B = rot(pi/4) = [[1, -1], [1, 1]]/sqrt2 (H = B Z); T = diag(1, zeta8); the kernel's InstAvail
constructors at L (ImplementationLocality.lean:268): op (an admissible isometry), readout (Lueders readout of a
register, its projectors admissible), coarse, bind (outcome-dependent continuation), discard (of a UNIFORMLY attached
ancilla).  Exact arithmetic in Q(zeta8) (own class: Q-coefficients on 1, z, z^2, z^3 with z^4 = -1; i = z^2,
sqrt2 = z - z^3).

Decision rule (fixed before run 1): VERDICT INDEP-O5-FIXED iff Z1-Z6 all PASS and CC1-CC6 all evaluate False;
otherwise VERDICT INDEP-O5-FAILED <items>.

Z1 the stated access's reversible groups (exhaustive, exact): on N configurations, <all transpositions> has N!
   elements modulo scalars and <transpositions, diag(i, 1, ..., 1)> has N! 4^(N-1), at N = 2 and 4 (= (2n)! and
   (2n)! 4^(2n-1) at n = 1, 2); every element of the second is a unit multiple of a mu4-monomial; both are finite, so
   each is its own closure.
Z2 the coefficient square (T9/X10): for 400 random exact lattice protocols on the data qubit (a uniformly attached
   ancilla of size 2 or 4, mu4-monomial isometries on the joint carrier, a computational-basis readout of the ancilla
   with outcome-dependent mu4-monomial continuations, coarse-graining, discard) the coefficient
   c(Phi) = <0|Phi(|0><1|)|1> satisfies |Re c| + |Im c| <= 1; the drive's coefficient is conj w with |Re| + |Im| = 7/5.
   The sample is a spot check of the written argument [W]: every Kraus operator of a channel composed from these
   constructors is a positive multiple p^(1/2) of a partial monomial matrix with mu4 entries, so
   c = sum_K p_K K_00 conj(K_11) is a combination of mu4 units with total weight <= sum_K p_K |K_00|^2 <= 1; the square
   is closed, so the drive is not a limit of these channels.
Z3 the repeat-until-success protocol (O14-N1, T9), exactly: (a) gates: H = B Z, the Toffoli a permutation matrix, S
   monomial; (b) a pure ancilla |00> from the uniform attachment by readout and conditional flips (coarse-grained);
   (c) one round U = (H_a H_b) Toff S_d Toff S_d^+ (H_a H_b) on (data, a, b) with ancilla |00>: the Kraus operators of
   the readout are K00 = (3I + iZ)/4, K01 = K10 = (I - iZ)/4, K11 = (-I + iZ)/4, with K00^+K00 = 5/8, the others 1/8, each
   failure equal to S times a scalar and the success to V = diag(1, (4 - 3i)/5) times a scalar; (d) with the correction
   S^+ after a failure and stop on success, the k-round channel is (1 - (3/8)^k) Ad(V) + (3/8)^k id exactly on the four
   matrix units, k = 1, 2, 3; (e) S V = D, so Ad(S) o Phi_k -> Ad(D) with distance (3/8)^k.
Z4 the balanced mixer's level-one reversible group: <B, S, X> modulo phase has 24 elements (the Clifford channels) and
   contains neither V nor D: the limit in Z3 exceeds the closure of the reversible group (AW-14a).
Z5 rational angles (O14-N3's valuation step): w = (2 + i)/(2 - i), so its (2 - i)-adic valuation is -1 and w lies in
   no ring Z[i][1/2]; every entry of every element of <B, S, X> lies in Z[zeta8][1/2] [W: 5 is unramified in Q(zeta8),
   so the valuation stays -1 there].
Z6 finite-order non-Clifford phase (X7): <T, S, X> has 16 elements modulo scalars, all monomial; H T is not monomial
   and (H T)^n is not scalar for n <= 200.
Countercontrols (each must evaluate False):
CC1 the round with CC(Z) in place of CC(iZ) has a success branch proportional to a unitary.
CC2 the drive's coefficient lies in the square.
CC3 V or D lies in <B, S, X> modulo phase.
CC4 w has nonnegative (2 - i)-adic valuation.
CC5 some tested lattice protocol leaves the square.
CC6 H T lies in <T, S, X> modulo phase.

Run from this directory:  python3 -I -B indep_checkO5.py > indep_checkO5.out 2> indep_checkO5.err
"""
import math
import random
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


W = q(F(3, 5), F(4, 5))
Dm = [[ONE, ZERO], [ZERO, W]]
Sm = [[ONE, ZERO], [ZERO, I_]]
Xm = [[ZERO, ONE], [ONE, ZERO]]
Zm = [[ONE, ZERO], [ZERO, -ONE]]
Bm = [[HALF_SQ2, -HALF_SQ2], [HALF_SQ2, HALF_SQ2]]
Hm = [[HALF_SQ2, HALF_SQ2], [HALF_SQ2, -HALF_SQ2]]
Tm = [[ONE, ZERO], [ZERO, Z]]
Vm = [[ONE, ZERO], [ZERO, q(F(4, 5), F(-3, 5))]]

# ---------------------------------------------------------------- Z1
z1, m1 = True, []
for N in (2, 4):
    def transp(a, b):
        M = eye(N)
        M[a][a], M[b][b], M[a][b], M[b][a] = ZERO, ZERO, ONE, ONE
        return M
    ts = [transp(a, a + 1) for a in range(N - 1)]
    ph = eye(N)
    ph[0][0] = I_
    gp, f1 = closure(ts)
    gl, f2 = closure(ts + [ph])
    mono = all(is_monomial([list(r) for r in g]) and all(x.zero() or x in (ONE, -ONE, I_, -I_) for r in g for x in r)
               for g in gl)
    ok = f1 and f2 and len(gp) == math.factorial(N) and len(gl) == math.factorial(N) * 4 ** (N - 1) and mono
    z1 &= ok
    m1.append(f'N = {N}: <transpositions> {len(gp)}, <transpositions, quarter phase> {len(gl)} (N! 4^(N-1) = '
              f'{math.factorial(N) * 4 ** (N - 1)}), all mu4-monomial up to scalar {mono}')
check('Z1', z1, '; '.join(m1))


# ---------------------------------------------------------------- Z2 coefficient square
def rand_mono(n, rng):
    perm = list(range(n))
    rng.shuffle(perm)
    M = [[ZERO] * n for _ in range(n)]
    for j in range(n):
        M[perm[j]][j] = [ONE, -ONE, I_, -I_][rng.randrange(4)]
    return M


def channel_apply(kraus_list, X):
    out = None
    for K in kraus_list:
        t = mm(mm(K, X), dg(K))
        out = t if out is None else add(out, t)
    return out


def lattice_protocol_kraus(m, rng):
    """Kraus operators (data <- data) of: uniform ancilla of size m attached (Kraus sqrt(1/m) |a>), U1 (mu4-monomial on
    data x ancilla), readout of the ancilla in the computational basis, continuation U2[k] (mu4-monomial, outcome
    dependent), coarse-graining, discard of the ancilla (trace)"""
    n = 2 * m
    U1 = rand_mono(n, rng)
    U2 = [rand_mono(n, rng) for _ in range(m)]
    ks = []
    # Kraus: <e| U2[k] P_k U1 |a> / sqrt(m), with data index d, ancilla index a: joint index d*m + a
    sq = None
    for a in range(m):
        for k in range(m):
            for e in range(m):
                K = [[ZERO, ZERO], [ZERO, ZERO]]
                for d_out in range(2):
                    for d_in in range(2):
                        # (<d_out, e| U2[k] |.,k><.,k| U1 |d_in, a>)
                        s = ZERO
                        for d_mid in range(2):
                            s = s + U2[k][d_out * m + e][d_mid * m + k] * U1[d_mid * m + k][d_in * m + a]
                        K[d_out][d_in] = s
                ks.append((K, m))
    return ks


def coeff(kraus_scaled):
    X01 = [[ZERO, ONE], [ZERO, ZERO]]
    tot = ZERO
    for K, m in kraus_scaled:
        t = mm(mm(K, X01), dg(K))
        tot = tot + t[0][1] * F(1, m)
    return tot


def sq_norm1(x):
    (ra, rb), (ia, ib) = x.re_im()
    assert rb == 0 and ib == 0, 'coefficient outside Q(i)'
    return abs(ra) + abs(ia)


rng = random.Random(20261011)
z2, worst = True, F(0)
for trial in range(400):
    m = 2 if trial % 2 == 0 else 4
    ks = lattice_protocol_kraus(m, rng)
    # trace preservation check
    tp = None
    for K, mm_ in ks:
        t = scal(F(1, mm_), mm(dg(K), K))
        tp = t if tp is None else add(tp, t)
    c = coeff(ks)
    v = sq_norm1(c)
    worst = max(worst, v)
    z2 &= eq(tp, eye(2)) and v <= 1
cD = coeff([(Dm, 1)])
vD = sq_norm1(cD)
check('Z2', z2 and cD == W.conj() and vD == F(7, 5),
      f'400 lattice protocols trace preserving with |Re c| + |Im c| <= 1: {z2} (largest {worst}); drive coefficient = '
      f'conj w {cD == W.conj()}, |Re| + |Im| = {vD}')
cc('CC2', vD <= 1, 'the drive coefficient lies in the square')
cc('CC5', not z2, 'a tested lattice protocol leaves the square')

# ---------------------------------------------------------------- Z3 repeat-until-success
I2 = eye(2)
z3a = eq(Hm, mm(Bm, Zm)) and eq(mm(Sm, Sm), Zm)


def op3(U_d, U_a, U_b):
    return kron(kron(U_d, U_a), U_b)  # index d*4 + a*2 + b


Toff = eye(8)
for a_, b_ in [(1, 1)]:
    for d_ in range(2):
        i_ = d_ * 4 + a_ * 2 + b_
        j_ = (1 - d_) * 4 + a_ * 2 + b_
        Toff[i_][i_] = ZERO
        Toff[i_][j_] = ONE
z3a &= all(sum(1 for x in r if x == ONE) == 1 and sum(1 for x in r if x.zero()) == 7 for r in Toff)
Sd, Sdh = op3(Sm, I2, I2), op3(dg(Sm), I2, I2)
HH = op3(I2, Hm, Hm)
CCiZ = mm(mm(mm(Toff, Sd), Toff), Sdh)
Uround = mm(mm(HH, CCiZ), HH)
# (b) pure ancilla from the uniform attachment: readout of (a, b) and conditional flips, coarse-grained
prep = None
for x in range(2):
    for y in range(2):
        flip = kron(Xm if x else I2, Xm if y else I2)
        proj = [[ONE if (i == j == 2 * x + y) else ZERO for j in range(4)] for i in range(4)]
        t = mm(mm(flip, proj), dg(flip))
        prep = t if prep is None else add(prep, t)
prep = scal(F(1, 4), prep)  # uniform attachment I/4 then readout + flips: sum_xy flip P_xy (I/4) P_xy flip^+
P00 = [[ONE if (i == j == 0) else ZERO for j in range(4)] for i in range(4)]
z3b = eq(prep, P00)


def kraus_outcome(U, c, d):
    """data operator <c d| U |0 0> (data <- data)"""
    K = [[ZERO, ZERO], [ZERO, ZERO]]
    for do in range(2):
        for di in range(2):
            K[do][di] = U[do * 4 + c * 2 + d][di * 4 + 0]
    return K


Ks = {(c, d): kraus_outcome(Uround, c, d) for c in range(2) for d in range(2)}
iZ = [[I_, ZERO], [ZERO, -I_]]
exp = {(0, 0): scal(F(1, 4), add(scal(3, I2), iZ)), (0, 1): scal(F(1, 4), add(I2, scal(-1, iZ))),
       (1, 0): scal(F(1, 4), add(I2, scal(-1, iZ))), (1, 1): scal(F(1, 4), add(scal(-1, I2), iZ))}
z3c = all(eq(Ks[k], exp[k]) for k in Ks)
z3c &= eq(mm(dg(Ks[(0, 0)]), Ks[(0, 0)]), scal(F(5, 8), I2))
z3c &= all(eq(mm(dg(Ks[k]), Ks[k]), scal(F(1, 8), I2)) for k in [(0, 1), (1, 0), (1, 1)])


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


z3c &= prop(Ks[(0, 0)], Vm) and all(prop(Ks[k], Sm) for k in [(0, 1), (1, 0), (1, 1)])
# (d) k-round channel with correction S^+ after failure and stop on success
units = [[[ONE if (i == r and j == s) else ZERO for j in range(2)] for i in range(2)] for r in range(2) for s in range(2)]


def round_channel(X, k):
    """apply up to k rounds: the output of the protocol (stop on success; after a failure, correct by S^+ and continue
    on the unnormalized post-failure data operator)"""
    if k == 0:
        return X
    succ = mm(mm(Ks[(0, 0)], X), dg(Ks[(0, 0)]))
    fail = None
    for key in [(0, 1), (1, 0), (1, 1)]:
        Kc = mm(dg(Sm), Ks[key])  # correction S^+
        t = mm(mm(Kc, X), dg(Kc))
        fail = t if fail is None else add(fail, t)
    return add(succ, round_channel(fail, k - 1))


z3d = True
for k in (1, 2, 3):
    eps = F(3, 8) ** k
    for X in units:
        out = round_channel(X, k)
        target = add(scal(1 - eps, mm(mm(Vm, X), dg(Vm))), scal(eps, X))
        z3d &= eq(out, target)
z3e = eq(mm(Sm, Vm), Dm)
check('Z3', z3a and z3b and z3c and z3d and z3e,
      f'gates H = B Z, S^2 = Z, Toffoli a permutation: {z3a}; pure ancilla from uniform attachment by readout and flips '
      f'{z3b}; Kraus operators (3I+iZ)/4, (I-iZ)/4 x2, (-I+iZ)/4 with K^+K = 5/8, 1/8, 1/8, 1/8, failures prop. S, success '
      f'prop. V = diag(1, (4-3i)/5): {z3c}; k-round channel = (1-(3/8)^k) Ad(V) + (3/8)^k id on the matrix units, k = 1, 2, 3: '
      f'{z3d}; S V = D: {z3e}')
# CC1: CC(Z) in place of CC(iZ)
Hd = op3(Hm, I2, I2)
CCZ = mm(mm(Hd, Toff), Hd)
U2r = mm(mm(HH, CCZ), HH)
K00z = kraus_outcome(U2r, 0, 0)
KK = mm(dg(K00z), K00z)
cc('CC1', KK[0][1].zero() and KK[1][0].zero() and KK[0][0] == KK[1][1],
   f'with CC(Z) the success branch is proportional to a unitary (K^+K = diag({KK[0][0].c[0]}, {KK[1][1].c[0]}))')

# ---------------------------------------------------------------- Z4 the level-one reversible group of the balanced mixer
g24, fin24 = closure([Bm, Sm, Xm])
hasV = normalize(Vm) in g24
hasD = normalize(Dm) in g24
check('Z4', fin24 and len(g24) == 24 and not hasV and not hasD,
      f'<B, S, X> modulo phase: {len(g24)} elements; contains V: {hasV}; contains D: {hasD}')
cc('CC3', hasV or hasD, 'V or D in <B, S, X> modulo phase')


# ---------------------------------------------------------------- Z5 valuation
def gauss_div(a, b):  # exact division in Z[i] if possible: returns quotient or None
    ar, ai = a
    br, bi = b
    n = br * br + bi * bi
    qr, qi = ar * br + ai * bi, ai * br - ar * bi
    if qr % n == 0 and qi % n == 0:
        return (qr // n, qi // n)
    return None


def val(num, den, p):
    """p-adic valuation (p a Gaussian prime) of num/den, num, den in Z[i]"""
    def v(x):
        k = 0
        while True:
            y = gauss_div(x, p)
            if y is None:
                return k
            x = y
            k += 1
    return v(num) - v(den)


# w = (3 + 4i)/5; 5 = (2 + i)(2 - i); (2 + i)^2 = 3 + 4i
v_minus = val((3, 4), (5, 0), (2, -1))
v_plus = val((3, 4), (5, 0), (2, 1))
fac = (2 * 2 - 1 * 1, 2 * 1 + 1 * 2) == (3, 4) and (2 * 2 + 1, 0) == (5, 0)
# entries of <B, S, X> in Z[zeta8][1/2]: coefficients have power-of-two denominators
den_ok = all(all((x.denominator & (x.denominator - 1)) == 0 for x in e.c) for g in g24 for r in g for e in r)
check('Z5', fac and v_minus == -1 and v_plus == 1 and den_ok,
      f'(2+i)^2 = 3+4i and (2+i)(2-i) = 5: {fac}; (2-i)-adic valuation of w = {v_minus}, (2+i)-adic = {v_plus}; entries of '
      f'<B, S, X> (normalized) have power-of-two denominators: {den_ok}')
cc('CC4', v_minus >= 0, 'w has nonnegative (2 - i)-adic valuation')

# ---------------------------------------------------------------- Z6 finite-order non-Clifford phase
g16, fin16 = closure([Tm, Sm, Xm])
mono16 = all(is_monomial([list(r) for r in g]) for g in g16)
HT = mm(Hm, Tm)
inG = normalize(HT) in g16
P = eye(2)
scalar_power = None
for n in range(1, 201):
    P = mm(P, HT)
    if P[0][1].zero() and P[1][0].zero() and P[0][0] == P[1][1]:
        scalar_power = n
        break
check('Z6', fin16 and len(g16) == 16 and mono16 and not is_monomial(HT) and scalar_power is None,
      f'<T, S, X> modulo scalars: {len(g16)} elements, all monomial {mono16}; H T monomial: {is_monomial(HT)}; (H T)^n '
      f'scalar for some n <= 200: {scalar_power is not None}')
cc('CC6', inG, 'H T in <T, S, X> modulo phase')

fails = [k for k, ok in RESULTS.items() if not ok] + [k for k, v in CCS.items() if v]
print()
print(f'PASS {sum(RESULTS.values())}/{len(RESULTS)}; countercontrols False {sum(1 for v in CCS.values() if not v)}/{len(CCS)}')
print('VERDICT INDEP-O5-FIXED' if not fails else 'VERDICT INDEP-O5-FAILED ' + ' '.join(fails))
