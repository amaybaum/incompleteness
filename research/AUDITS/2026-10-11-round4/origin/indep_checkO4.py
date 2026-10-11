#!/usr/bin/env python3
"""indep_checkO4.py — the coordinator's independent check of research/origin, round 4 (O11, O12, O13).

Own code; reads nothing from the thread (no import of its scripts, no parsing of its outputs). Exact arithmetic
throughout: an own class for Q(zeta_16) over Fractions (X2, X3a, X5, CC2, CC5) and sympy exact radicals /
minimal polynomials (X1, X3b, X4, X6, X8).

DECISION RULE (fixed before run 1):
  X1  O12-T1  on every reduced angle alpha = pi*p/q, q <= 24, 0 <= p < 2q: conjugation by rot(alpha) carries Z
              and X into the 16-element Pauli set exactly when 4p/q is an integer (q | 4); on the grid the Clifford
              angles number exactly 8.  Direct matrix test (sympy, q <= 12) and closed form (q <= 24) must agree.
  X2  O12-T3  the level-one group <rot(k*pi/4), S, X> modulo scalars has 8 classes for k even and 24 for k odd
              (k = 0..7), by BFS on the pair (G X G^dag, G Z G^dag) in Q(zeta_16).
  X3  O12-T4/T5  (a) W = rot(pi/8) * S rot(pi/8) S^dag has det 1, trace 1 + sqrt2/2, and W^k is not a scalar for
              1 <= k <= 96 (exact in Q(zeta_16)); the Chebyshev sequence p of the trace has p_k != 0 for
              1 <= k <= 400 (exact in Q(sqrt2)); (b) trace(W(alpha)) = 2 cos^2 alpha symbolically; (c) on the grid
              q <= 24 the number 1 + cos(2 alpha) is an algebraic integer (monic primitive minimal polynomial)
              exactly at the Clifford angles.
  X4  O11-T4/E3  z = (3+4i)/5 has minimal polynomial 5x^2 - 6x + 5 (not monic): not a root of unity.
  X5  O11-T6/E5  the group <rot(pi/4), S, X> with scalars has 192 elements and 24 channels (classes modulo
              scalars); every channel has order in {1, 2, 3, 4} in PU(2).
  X6  O13-T1/T2  for the axes z, -z, x, y, (4/5,0,3/5), (3/5,4/5,0), (2/3,1/3,2/3): Pi_n = (1 + n.sigma)/2 is
              submonomial exactly for +-z; the Choi matrix of F(X) = tr(Pi X) Pi has rank 1 and equals
              vec(Pi) vec(Pi)^dag up to the standard ordering; the single Kraus operator is proportional to Pi;
              the Lueders selectors on the configuration basis are F^z_+-.
  X7  O11-S2  the class counts 16 + 5 + 21 + 4 + 8 + 12 + 2 equal 68.
  X8  O11-T1  for monomial unitaries U = P D on Fin 4 (phases in {1, i, (3+4i)/5}), U E_ss U^dag is a configuration
              projector E_tt (exact, sympy), so the induced map on configuration states is a permutation.
  Countercontrols, each expected False:
  CC1 the Pauli test accepts rot(pi/8);  CC2 some p_k = 0 for 1 <= k <= 400;  CC3 the Choi matrix of F_+ + F_- has
  rank 1;  CC4 Pi_x is submonomial;  CC5 the BFS at pi/8 closes within 200 classes.
VERDICT INDEP-O4-FIXED iff X1-X8 all CONFIRMED and CC1-CC5 all False; VOID if any countercontrol is True;
UNDECIDED otherwise.
RUN HISTORY: run 1 2026-10-11T05:10:57Z (41 s): 8/8 CONFIRMED, CC1-CC5 all False, VERDICT INDEP-O4-FIXED; replay
(run 2, same file) byte-identical on stdout and stderr. This docstring line was appended after run 2; nothing else
in the file changed, and the replay below the record was re-run from the appended file.
"""
from fractions import Fraction as Fr
from math import gcd
import sys
import sympy as sp

# ---------------------------------------------------------------- Q(zeta_16): 8-tuples, zeta^8 = -1
N = 8


class Cyc:
    __slots__ = ('c',)

    def __init__(self, c):
        self.c = tuple(Fr(x) for x in c)

    @staticmethod
    def const(a):
        return Cyc((Fr(a),) + (Fr(0),) * (N - 1))

    @staticmethod
    def zeta(k):
        k %= 2 * N
        s = 1
        if k >= N:
            k -= N
            s = -1
        c = [Fr(0)] * N
        c[k] = Fr(s)
        return Cyc(c)

    def __add__(s, o):
        return Cyc([a + b for a, b in zip(s.c, o.c)])

    def __sub__(s, o):
        return Cyc([a - b for a, b in zip(s.c, o.c)])

    def __neg__(s):
        return Cyc([-a for a in s.c])

    def __mul__(s, o):
        if not isinstance(o, Cyc):
            o = Cyc.const(o)
        r = [Fr(0)] * N
        for i, a in enumerate(s.c):
            if a == 0:
                continue
            for j, b in enumerate(o.c):
                if b == 0:
                    continue
                k = i + j
                if k >= N:
                    r[k - N] -= a * b
                else:
                    r[k] += a * b
        return Cyc(r)

    __rmul__ = __mul__

    def conj(s):
        r = [Fr(0)] * N
        for k, a in enumerate(s.c):
            if a == 0:
                continue
            m = (-k) % (2 * N)
            sgn = 1
            if m >= N:
                m -= N
                sgn = -1
            r[m] += sgn * a
        return Cyc(r)

    def iszero(s):
        return all(a == 0 for a in s.c)

    def __eq__(s, o):
        return s.c == o.c

    def __hash__(s):
        return hash(s.c)


ZERO, ONE = Cyc.const(0), Cyc.const(1)
HALF = Cyc.const(Fr(1, 2))


def cos8(k):  # cos(k*pi/8) = (zeta^k + zeta^-k)/2
    return (Cyc.zeta(k) + Cyc.zeta(-k)) * HALF


def sin8(k):  # sin(k*pi/8) = (zeta^k - zeta^-k) * (-zeta^4) / 2
    return (Cyc.zeta(k) - Cyc.zeta(-k)) * (-Cyc.zeta(4)) * HALF


def mmul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def mdag(A):
    return ((A[0][0].conj(), A[1][0].conj()), (A[0][1].conj(), A[1][1].conj()))


def mkey(A):
    return (A[0][0].c, A[0][1].c, A[1][0].c, A[1][1].c)


def meq(A, B):
    return mkey(A) == mkey(B)


def rot8(k):  # rot(k*pi/8) = [[c, -s], [s, c]]
    c, s = cos8(k), sin8(k)
    return ((c, -s), (s, c))


I2 = ((ONE, ZERO), (ZERO, ONE))
XM = ((ZERO, ONE), (ONE, ZERO))
ZM = ((ONE, ZERO), (ZERO, -ONE))
SM = ((ONE, ZERO), (ZERO, Cyc.zeta(4)))  # diag(1, i)


def is_scalar(A):
    return A[0][1].iszero() and A[1][0].iszero() and A[0][0] == A[1][1]


def class_key(G):
    Gd = mdag(G)
    return (mkey(mmul(mmul(G, XM), Gd)), mkey(mmul(mmul(G, ZM), Gd)))


def bfs_classes(gens, limit):
    """BFS of the group generated by gens modulo scalars; returns (reps dict, closed)."""
    start = I2
    seen = {class_key(start): start}
    frontier = [start]
    while frontier:
        nxt = []
        for G in frontier:
            for g in gens:
                H = mmul(g, G)
                k = class_key(H)
                if k not in seen:
                    seen[k] = H
                    nxt.append(H)
                    if len(seen) > limit:
                        return seen, False
        frontier = nxt
    return seen, True


def bfs_group(gens, limit):
    seen = {mkey(I2): I2}
    frontier = [I2]
    while frontier:
        nxt = []
        for G in frontier:
            for g in gens:
                H = mmul(g, G)
                k = mkey(H)
                if k not in seen:
                    seen[k] = H
                    nxt.append(H)
                    if len(seen) > limit:
                        return seen, False
        frontier = nxt
    return seen, True


results = {}
cc = {}


def record(name, ok, detail):
    results[name] = ok
    print(f"{name}: {'CONFIRMED' if ok else 'FAILED'} -- {detail}")


# ---------------------------------------------------------------- X1
def reduced_angles(qmax):
    out = []
    for q in range(1, qmax + 1):
        for p in range(0, 2 * q):
            if gcd(p, q) == 1 or (p == 0 and q == 1):
                out.append((p, q))
    return out


PAULI16 = []
for j, P in enumerate([sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]),
                       sp.Matrix([[1, 0], [0, -1]])]):
    for k in range(4):
        PAULI16.append(sp.I ** k * P)


def in_pauli(M):
    for P in PAULI16:
        if all(sp.simplify(M[i, j] - P[i, j]) == 0 for i in range(2) for j in range(2)):
            return True
    return False


def rot_sym(a):
    return sp.Matrix([[sp.cos(a), -sp.sin(a)], [sp.sin(a), sp.cos(a)]])


x1_ok = True
cliff_direct = []
for (p, q) in reduced_angles(12):
    a = sp.pi * sp.Rational(p, q)
    R = rot_sym(a)
    MZ = sp.simplify(R * sp.Matrix([[1, 0], [0, -1]]) * R.T)
    MX = sp.simplify(R * sp.Matrix([[0, 1], [1, 0]]) * R.T)
    direct = in_pauli(MZ) and in_pauli(MX)
    closed = (4 * p) % q == 0
    if direct != closed:
        x1_ok = False
    if direct:
        cliff_direct.append((p, q))
cliff_closed24 = [(p, q) for (p, q) in reduced_angles(24) if (4 * p) % q == 0]
n24 = len(reduced_angles(24))
record('X1', x1_ok and len(cliff_direct) == 8 and len(cliff_closed24) == 8,
       f"direct test q<=12 agrees with closed form at every angle: {x1_ok}; Clifford angles (q<=12 direct) "
       f"{len(cliff_direct)}, (q<=24 closed form) {len(cliff_closed24)} of {n24} grid angles; "
       f"Clifford set {sorted(cliff_closed24)}")
cc['CC1'] = in_pauli(sp.simplify(rot_sym(sp.pi / 8) * sp.Matrix([[1, 0], [0, -1]]) * rot_sym(sp.pi / 8).T)) and \
    in_pauli(sp.simplify(rot_sym(sp.pi / 8) * sp.Matrix([[0, 1], [1, 0]]) * rot_sym(sp.pi / 8).T))

# ---------------------------------------------------------------- X2
x2_counts = {}
x2_ok = True
for k in range(8):
    reps, closed = bfs_classes([rot8(2 * k), SM, XM], 1000)  # rot(k*pi/4) = rot8(2k)
    x2_counts[k] = (len(reps), closed)
    expect = 8 if k % 2 == 0 else 24
    if not closed or len(reps) != expect:
        x2_ok = False
record('X2', x2_ok, f"classes modulo scalars at k*pi/4: {x2_counts}")

# ---------------------------------------------------------------- X3
R8 = rot8(1)
Sd = mdag(SM)
W = mmul(R8, mmul(SM, mmul(R8, Sd)))
detW = W[0][0] * W[1][1] - W[0][1] * W[1][0]
trW = W[0][0] + W[1][1]
sqrt2 = Cyc.zeta(2) + Cyc.zeta(-2)
t_expect = ONE + sqrt2 * HALF
x3a_ok = (detW == ONE) and (trW == t_expect) and (not W[0][1].iszero())
Wk = W
nonscalar = True
for k in range(1, 97):
    if is_scalar(Wk):
        nonscalar = False
        break
    Wk = mmul(Wk, W)
# Chebyshev sequence in Q(sqrt2): elements (a, b) = a + b sqrt2
t = (Fr(1), Fr(1, 2))


def q2mul(u, v):
    return (u[0] * v[0] + 2 * u[1] * v[1], u[0] * v[1] + u[1] * v[0])


p_prev, p_cur = (Fr(0), Fr(0)), (Fr(1), Fr(0))
zero_hit = False
for k in range(2, 401):
    p_next = (q2mul(t, p_cur)[0] - p_prev[0], q2mul(t, p_cur)[1] - p_prev[1])
    p_prev, p_cur = p_cur, p_next
    if p_cur == (Fr(0), Fr(0)):
        zero_hit = True
        break
cc['CC2'] = zero_hit
x3a_ok = x3a_ok and nonscalar and not zero_hit
# symbolic trace identity
al = sp.symbols('alpha', real=True)
Ssym = sp.diag(1, sp.I)
Wsym = rot_sym(al) * Ssym * rot_sym(al) * Ssym.H
x3b_ok = sp.simplify(Wsym.trace() - 2 * sp.cos(al) ** 2) == 0 and sp.simplify(Wsym.det() - 1) == 0
# integrality of 1 + cos 2alpha on the grid q <= 24
x = sp.symbols('x')
x3c_ok = True
nonint = 0
for (p, q) in reduced_angles(24):
    val = 1 + sp.cos(2 * sp.pi * sp.Rational(p, q))
    mp = sp.minimal_polynomial(val, x)
    poly = sp.Poly(mp, x)
    monic = (abs(poly.LC()) == 1)  # minimal_polynomial returns a primitive integer polynomial
    clifford = (4 * p) % q == 0
    if monic != clifford:
        x3c_ok = False
    if not monic:
        nonint += 1
record('X3', x3a_ok and x3b_ok and x3c_ok,
       f"det(W)=1 {detW == ONE}, tr(W)=1+sqrt2/2 {trW == t_expect}, W^k non-scalar k<=96 {nonscalar}, "
       f"p_k != 0 k<=400 {not zero_hit}; tr W(alpha)=2cos^2 alpha and det 1 symbolic {x3b_ok}; "
       f"1+cos 2alpha algebraic integer exactly at Clifford angles on q<=24 {x3c_ok} ({nonint} non-integral of {n24})")

# ---------------------------------------------------------------- X4
z = sp.Rational(3, 5) + sp.I * sp.Rational(4, 5)
mpz = sp.Poly(sp.minimal_polynomial(z, x), x)
record('X4', mpz.as_expr() == 5 * x ** 2 - 6 * x + 5 or mpz.as_expr() == -(5 * x ** 2 - 6 * x + 5),
       f"minimal polynomial of (3+4i)/5: {mpz.as_expr()}, leading coefficient {mpz.LC()}")

# ---------------------------------------------------------------- X5
grp, closed = bfs_group([rot8(2), SM, XM], 2000)
classes, closed2 = bfs_classes([rot8(2), SM, XM], 1000)
orders = {}
for key, G in classes.items():
    P = G
    m = 1
    while not is_scalar(P):
        P = mmul(P, G)
        m += 1
        if m > 50:
            break
    orders[m] = orders.get(m, 0) + 1
record('X5', closed and len(grp) == 192 and closed2 and len(classes) == 24 and set(orders) <= {1, 2, 3, 4},
       f"group with scalars {len(grp)} (closed {closed}); channels {len(classes)}; channel orders {orders}")
reps8, closed8 = bfs_classes([rot8(1), SM, XM], 200)
cc['CC5'] = closed8

# ---------------------------------------------------------------- X6
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
axes = {'z': (0, 0, 1), '-z': (0, 0, -1), 'x': (1, 0, 0), 'y': (0, 1, 0),
        '(4/5,0,3/5)': (sp.Rational(4, 5), 0, sp.Rational(3, 5)),
        '(3/5,4/5,0)': (sp.Rational(3, 5), sp.Rational(4, 5), 0),
        '(2/3,1/3,2/3)': (sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(2, 3))}


def proj(n, sgn=1):
    return (sp.eye(2) + sgn * (n[0] * sig[0] + n[1] * sig[1] + n[2] * sig[2])) / 2


def submonomial(M):
    for i in range(2):
        if sum(1 for j in range(2) if sp.simplify(M[i, j]) != 0) > 1:
            return False
    for j in range(2):
        if sum(1 for i in range(2) if sp.simplify(M[i, j]) != 0) > 1:
            return False
    return True


def choi(F):
    # Choi matrix J = sum_{ij} E_ij (x) F(E_ij)
    J = sp.zeros(4, 4)
    for i in range(2):
        for j in range(2):
            E = sp.zeros(2, 2)
            E[i, j] = 1
            J += sp.kronecker_product(E, F(E))
    return J


x6_ok = True
sub_axes = []
for name, n in axes.items():
    Pp, Pm = proj(n, 1), proj(n, -1)
    if submonomial(Pp):
        sub_axes.append(name)
    Fp = lambda X, Pp=Pp: (Pp * X).trace() * Pp
    Fm = lambda X, Pm=Pm: (Pm * X).trace() * Pm
    J = choi(Fp)
    if J.rank(simplify=True) != 1:
        x6_ok = False
    vecP = sp.Matrix([Pp[0, 0], Pp[1, 0], Pp[0, 1], Pp[1, 1]])  # column-stacking
    # J should equal vec(Pp) vec(Pp)^dag up to a fixed permutation of the ordering; test rank-one factor agreement
    # through the trace pairing: J = sum_ij E_ij (x) Pp_ij-weighted; check J == kron(Pp^T, Pp) exactly.
    if sp.simplify(J - sp.kronecker_product(Pp.T, Pp)) != sp.zeros(4, 4):
        x6_ok = False
    if name == '(3/5,4/5,0)':
        # single Kraus operator: the Choi eigenvector of the nonzero eigenvalue reshaped is proportional to Pp
        evs = J.eigenvects()
        nz = [(lam, vs) for lam, mult, vs in evs if sp.simplify(lam) != 0]
        if len(nz) != 1 or len(nz[0][1]) != 1:
            x6_ok = False
        else:
            v = nz[0][1][0]
            K = sp.Matrix([[v[0], v[2]], [v[1], v[3]]])  # unvec (column-stacking of kron(P^T, P) rows)
            # K proportional to Pp: rank of [vec K | vec Pp] is 1
            if sp.Matrix.hstack(K.reshape(4, 1), Pp.reshape(4, 1)).rank(simplify=True) != 1:
                x6_ok = False
    Jsum = choi(lambda X, Fp=Fp, Fm=Fm: Fp(X) + Fm(X))
    if name == 'x':
        cc['CC3'] = (Jsum.rank(simplify=True) == 1)
        cc['CC4'] = submonomial(Pp)
# Lueders selectors on the configuration basis
E00, E11 = sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 0], [0, 1]])
lue_ok = True
for Xm in [sp.Matrix([[1, 2], [3, 4]]), sp.Matrix([[sp.I, 1], [0, 2]])]:
    if sp.simplify(E00 * Xm * E00 - (proj((0, 0, 1)) * Xm).trace() * proj((0, 0, 1))) != sp.zeros(2, 2):
        lue_ok = False
    if sp.simplify(E11 * Xm * E11 - (proj((0, 0, 1), -1) * Xm).trace() * proj((0, 0, 1), -1)) != sp.zeros(2, 2):
        lue_ok = False
record('X6', x6_ok and sorted(sub_axes) == ['-z', 'z'] and lue_ok,
       f"submonomial axes {sub_axes}; Choi rank one and = kron(Pi^T, Pi) at all axes {x6_ok}; Lueders = F^z {lue_ok}")

# ---------------------------------------------------------------- X7
record('X7', 16 + 5 + 21 + 4 + 8 + 12 + 2 == 68, f"16+5+21+4+8+12+2 = {16 + 5 + 21 + 4 + 8 + 12 + 2}")

# ---------------------------------------------------------------- X8
import itertools
phases = [1, sp.I, sp.Rational(3, 5) + sp.I * sp.Rational(4, 5)]
x8_ok = True
perms = [(1, 0, 3, 2), (2, 3, 0, 1), (3, 0, 1, 2)]
for perm in perms:
    for ph in [(phases[0], phases[1], phases[2], phases[1]), (phases[2], phases[2], phases[0], phases[1])]:
        U = sp.zeros(4, 4)
        for s in range(4):
            U[perm[s], s] = ph[s]
        if sp.simplify(U.H * U - sp.eye(4)) != sp.zeros(4, 4):
            x8_ok = False
        for s in range(4):
            E = sp.zeros(4, 4)
            E[s, s] = 1
            M = sp.simplify(U * E * U.H)
            Et = sp.zeros(4, 4)
            Et[perm[s], perm[s]] = 1
            if M != Et:
                x8_ok = False
record('X8', x8_ok, "monomial U carries E_ss to E_{pi(s) pi(s)} for 3 permutations x 2 phase patterns (exact)")

# ---------------------------------------------------------------- verdict
print("COUNTERCONTROLS (expected False):", {k: cc[k] for k in sorted(cc)})
allx = all(results.values())
anycc = any(cc.values())
if anycc:
    print("VERDICT VOID")
elif allx:
    print("VERDICT INDEP-O4-FIXED")
else:
    print("VERDICT UNDECIDED")
print(f"SUMMARY {sum(results.values())}/{len(results)} confirmed")
