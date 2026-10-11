#!/usr/bin/env python3
"""
o11_token.py -- O11: the stage-crossing datum from the stated access, levels one and two, exactly.

Thread research/origin, round 4, node O11. S0 predictions: NOTES-O11.md (2026-10-11T03:18:03Z), written before
this script's first run. Exact arithmetic only: every number lives in Q(zeta16) (zeta = e^{i pi/8}), stored as
eight Fractions (coefficients of 1, zeta, ..., zeta^7, with zeta^8 = -1); sympy is used only for minimal
polynomials. Floating point appears in one sanity line (the embedding of the constants), never in a decision.

Kernel objects mirrored (L = 9f9f8257): the configuration states |s><s|; the substratum class (monomial operators,
StructuralClosure.lean:180) and its sourced subclass permClass (scaled partial permutations,
SubstratumInterfaceAudit.lean:236); InstAvail's constructors (ImplementationLocality.lean:268): one isometric step,
the native readout of a register with its projectors, coarse-graining, feed-forward, the discard of a uniformly
attached ancilla; the fixed-gate class MixR {alpha} at level one (rot(alpha), the exchange, the quarter phases,
StateMixingCoupling.lean:56, LieRankSource.lean:209). Carriers: level one = 2 configurations, level two = 4.

Items (decided by the rule below):
  E1  substratum class, levels one and two: every normalized branch of every enumerated InstAvail family applied to a
      configuration state is configuration-diagonal with nonnegative rational entries summing to one, and every
      point mass is reached;
  E2  every enumerated available unitary datum maps each configuration state to a configuration state; its period
      on them divides 2 (level one) or 12 (level two), and after the period it fixes every reached state;
  E3  the frame phase diag(1, z), z = (3+4i)/5, fixes every reached state of E1 (level one; at level two the frame
      phase at configuration 3); on |+><+| its orbit has 201 distinct members for 200 steps; z has minimal polynomial
      5x^2 - 6x + 5 over Q, not monic over Z;
  E4  substratum class plus rot(pi/4) at level one: a reached state is coherent (|+><+|) and the frame phase's orbit
      of it has 201 distinct members; over the two families {stated access, extension}, "coherent body" and
      "frame phase of infinite orbit on the body" agree;
  E5  fixedGateTheory(pi/4), level one: the generated group has 192 elements and 24 channels; its reached states are
      the six octahedral pure states (coherent ones included); every channel has finite order (orders in {1,2,3,4});
      the frame phase diag(1, z) is not among the 24 channels;
  E6  fixedGateTheory(pi/8), level one: W = rot(pi/8) S rot(pi/8) S^dagger has trace 1 + sqrt2/2, minimal polynomial
      2x^2 - 4x + 1 (not monic), and W's orbit of the coherent reached state rot(pi/8)|0><0|rot(pi/8)^dagger has
      201 distinct members;
  E7  stage crossing: the infinite-order data of E3 (ambient), E4, E6 return to no orbit point within 200 steps;
      every E2 datum carries the finite set of configuration states into itself;
  E8  every enumerated deterministic family, restricted to the configuration states, is a column-stochastic
      matrix; it has a nonnegative inverse exactly when it is a permutation matrix.
Countercontrols (each must be False):
  CC1 "every reached state is diagonal" on the extension of E4;
  CC2 "a period <= 200 exists" for the frame phase on |+><+|;
  CC3 "the minimal polynomial of the trace is not monic over Z" for the level-one word at pi/4;
  CC4 "the frame phase fixes every reached state" on the extension of E4;
  CC5 "maps every configuration state to a configuration state" for rot(pi/4).

DECISION RULE (fixed before run 1):
  VERDICT O11-FINITE-ON-STATED-ACCESS+ORDINF-IFF-COHERENT if E1 ... E8 all hold and CC1 ... CC5 are all False;
  VERDICT VOID if any countercontrol is True; otherwise VERDICT UNDECIDED, naming the items that failed.
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

import sympy as sp

# ---------------------------------------------------------------- Q(zeta16), exact

N8 = 8


class K:
    __slots__ = ("c",)

    def __init__(self, c):
        self.c = tuple(Fr(v) for v in c)

    @staticmethod
    def of(q):
        return K([q] + [0] * 7)

    def __add__(self, o):
        return K([a + b for a, b in zip(self.c, o.c)])

    def __sub__(self, o):
        return K([a - b for a, b in zip(self.c, o.c)])

    def __neg__(self):
        return K([-a for a in self.c])

    def __mul__(self, o):
        r = [Fr(0)] * 16
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(o.c):
                    if b:
                        r[i + j] += a * b
        return K([r[k] - r[k + 8] for k in range(8)])

    def conj(self):
        r = [Fr(0)] * 8
        r[0] = self.c[0]
        for k in range(1, 8):
            r[8 - k] -= self.c[k]
        return K(r)

    def iszero(self):
        return not any(self.c)

    def __eq__(self, o):
        return self.c == o.c

    def __hash__(self):
        return hash(self.c)

    def approx(self):
        import cmath
        z = cmath.exp(1j * cmath.pi / 8)
        return sum(float(a) * z ** k for k, a in enumerate(self.c))


def zk(k):
    k %= 16
    c = [0] * 8
    if k < 8:
        c[k] = 1
    else:
        c[k - 8] = -1
    return K(c)


ZERO, ONE = K.of(0), K.of(1)
I = zk(4)
SQ2 = zk(2) - zk(6)                     # 2 cos(pi/4)
HALF = K.of(Fr(1, 2))
Z = K.of(Fr(3, 5)) + K.of(Fr(4, 5)) * I  # (3+4i)/5
ZB = Z.conj()
C8 = (zk(1) - zk(7)) * HALF             # cos(pi/8)
S8 = (zk(3) - zk(5)) * HALF             # sin(pi/8)
C4 = SQ2 * HALF                         # cos(pi/4) = sin(pi/4)

# ---------------------------------------------------------------- matrices (lists of lists of K)


def mzero(n):
    return [[ZERO] * n for _ in range(n)]


def eye(n):
    m = mzero(n)
    for i in range(n):
        m[i][i] = ONE
    return m


def mmul(A, B):
    n, p, q = len(A), len(B), len(B[0])
    R = [[ZERO] * q for _ in range(n)]
    for i in range(n):
        for k in range(p):
            a = A[i][k]
            if a.iszero():
                continue
            Bk = B[k]
            for j in range(q):
                b = Bk[j]
                if not b.iszero():
                    R[i][j] = R[i][j] + a * b
    return R


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def conjm(U, X):
    return mmul(mmul(U, X), dag(U))


def madd(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mscale(c, A):
    return [[c * a for a in r] for r in A]


def key(A):
    return tuple(tuple(a.c for a in r) for r in A)


def trace(A):
    t = ZERO
    for i in range(len(A)):
        t = t + A[i][i]
    return t


def cfg(n, s):
    m = mzero(n)
    m[s][s] = ONE
    return m


def is_diag(A):
    return all(A[i][j].iszero() for i in range(len(A)) for j in range(len(A)) if i != j)


def is_rational_prob(A):
    """diagonal entries rational (only the constant coefficient), nonnegative, summing to one."""
    tot = Fr(0)
    for i in range(len(A)):
        c = A[i][i].c
        if any(c[1:]) or c[0] < 0:
            return False
        tot += c[0]
    return tot == 1


def is_coherent(A):
    return not is_diag(A)


def kinv(a):
    """inverse in Q(zeta16) by the norm trick is not needed: only rational traces are inverted here."""
    c = a.c
    assert not any(c[1:]) and c[0] != 0, "only rational, nonzero traces are normalized"
    return K.of(1 / c[0])


def normalize(A):
    return mscale(kinv(trace(A)), A)


def monomial(perm, phases):
    n = len(perm)
    m = mzero(n)
    for j in range(n):
        m[perm[j]][j] = phases[j]
    return m


def perm_of(U):
    """the configuration map of U, if U maps every configuration state to a configuration state; else None."""
    n = len(U)
    sigma = []
    for s in range(n):
        img = conjm(U, cfg(n, s))
        hit = [t for t in range(n) if key(img) == key(cfg(n, t))]
        if len(hit) != 1:
            return None
        sigma.append(hit[0])
    return sigma


def perm_order(sigma):
    p, k = list(range(len(sigma))), 0
    cur = list(sigma)
    k = 1
    while cur != p:
        cur = [sigma[c] for c in cur]
        k += 1
    return k


def mpow(U, k):
    R = eye(len(U))
    for _ in range(k):
        R = mmul(R, U)
    return R


# ---------------------------------------------------------------- InstAvail families on a carrier of n states
# A family is a list of branches; a branch is a linear map given as a Python function on matrices.


def fam_op(U):
    return [lambda X, U=U: conjm(U, X)]


def fam_readout(n, m):
    """native readout of the register T = T' x Fin m (configuration index = t' * m + k): branch k projects."""
    out = []
    for k in range(m):
        P = mzero(n)
        for i in range(n):
            if i % m == k:
                P[i][i] = ONE
        out.append(lambda X, P=P: mmul(mmul(P, X), P))
    return out


def fam_bind(F, Gs):
    return [lambda X, f=f, g=g: g(f(X)) for f, G in zip(F, Gs) for g in G]


def fam_coarse(F):
    def br(X, F=F):
        acc = None
        for f in F:
            y = f(X)
            acc = y if acc is None else madd(acc, y)
        return acc
    return [br]


def attach_uniform(X, m):
    """X on n states -> X (x) I/m on n*m states, index i*m + a."""
    n = len(X)
    R = mzero(n * m)
    w = K.of(Fr(1, m))
    for i in range(n):
        for j in range(n):
            if not X[i][j].iszero():
                for a in range(m):
                    R[i * m + a][j * m + a] = X[i][j] * w
    return R


def ptrace(Y, m):
    n = len(Y) // m
    R = mzero(n)
    for i in range(n):
        for j in range(n):
            t = ZERO
            for a in range(m):
                t = t + Y[i * m + a][j * m + a]
            R[i][j] = t
    return R


def fam_discard(Fbig, m):
    return [lambda X, f=f: ptrace(f(attach_uniform(X, m)), m) for f in Fbig]


def reached(families, n):
    """normalized branches of nonzero weight applied to every configuration state."""
    out = {}
    for F in families:
        for f in F:
            for s in range(n):
                Y = f(cfg(n, s))
                if trace(Y).iszero():
                    continue
                Yn = normalize(Y)
                out[key(Yn)] = Yn
    return out


def stochastic(f, n):
    """the configuration-state restriction of a deterministic family's branch: M[t][s] = (f(E_s))[t][t]."""
    M = [[None] * n for _ in range(n)]
    for s in range(n):
        Y = f(cfg(n, s))
        if not is_diag(Y):
            return None
        for t in range(n):
            c = Y[t][t].c
            if any(c[1:]):
                return None
            M[t][s] = c[0]
    return M


def frac_inverse(M):
    n = len(M)
    A = [list(r) + [Fr(int(i == j)) for j in range(n)] for i, r in enumerate(M)]
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] != 0), None)
        if piv is None:
            return None
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [v / pv for v in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                fac = A[r][col]
                A[r] = [a - fac * b for a, b in zip(A[r], A[col])]
    return [row[n:] for row in A]


def is_perm_matrix(M):
    """a 0/1 matrix with exactly one 1 in every column and in every row (run 1 checked columns only, so a
    non-injective deterministic map such as a reset passed as a permutation)."""
    n = len(M)
    cols = all(sum(1 for t in range(n) if M[t][s] == 1) == 1 and
               all(M[t][s] in (0, 1) for t in range(n)) for s in range(n))
    rows = all(sum(1 for s in range(n) if M[t][s] == 1) == 1 for t in range(n))
    return cols and rows


def orbit_distinct(U, X, steps):
    seen, cur = {key(X)}, X
    for _ in range(steps):
        cur = conjm(U, cur)
        k = key(cur)
        if k in seen:
            return False, len(seen)
        seen.add(k)
    return True, len(seen)


def period_within(U, X, steps):
    cur = X
    for k in range(1, steps + 1):
        cur = conjm(U, cur)
        if key(cur) == key(X):
            return True
    return False


x = sp.symbols("x")


def to_sympy(a):
    """the exact element of Q(zeta16) as a sympy algebraic number (sum of rational multiples of exp(i pi k/8))."""
    return sum((sp.Rational(c.numerator, c.denominator) * sp.exp(sp.I * sp.pi * k / 8)
                for k, c in enumerate(a.c) if c), sp.Integer(0))


def minpoly_not_monic_over_Z(expr):
    mp = sp.Poly(sp.minimal_polynomial(expr, x), x)
    coeffs = mp.all_coeffs()
    lead = coeffs[0]
    monic_int = all(sp.Rational(c / lead).q == 1 for c in coeffs)
    return (not monic_int), sp.factor(sp.minimal_polynomial(expr, x))


# ---------------------------------------------------------------- the stated access: enumerated families

PHASES_L1 = [ONE, -ONE, I, -I, Z, ZB]
PHASES_SMALL = [ONE, Z]
rng = random.Random(20261011)


def substratum_families(n, with_mixer=None):
    fams, ops = [], []
    phases = PHASES_L1 if n == 2 else PHASES_SMALL
    for perm in itertools.permutations(range(n)):
        for ph in itertools.product(phases, repeat=n):
            U = monomial(list(perm), list(ph))
            ops.append(U)
    if with_mixer is not None:
        ops.append(with_mixer)
    for U in ops:
        fams.append(fam_op(U))
    regs = [1, 2] if n == 2 else [1, 2, 4]
    corr = [eye(n), monomial([(i + 1) % n for i in range(n)], [ONE] * n)]
    if with_mixer is not None:
        corr.append(with_mixer)
    for m in regs:
        R = fam_readout(n, m)
        fams.append(R)
        for choice in itertools.product(range(len(corr)), repeat=m):
            Gs = [fam_op(corr[c]) for c in choice]
            B = fam_bind(R, Gs)
            fams.append(B)
            fams.append(fam_coarse(B))
    # discard of a uniformly attached ancilla of size 2: composite step on 2n states, then forget
    big = 2 * n
    perms = list(itertools.permutations(range(big)))
    if len(perms) > 400:
        perms = rng.sample(perms, 400)
    for perm in perms:
        for ph in ([ONE] * big, [Z] + [ONE] * (big - 1)):
            Ub = monomial(list(perm), ph)
            fams.append(fam_discard(fam_op(Ub), 2))
            Rb = fam_readout(big, 2)
            fams.append(fam_discard(fam_bind(fam_op(Ub), [Rb]), 2))
    if with_mixer is not None:
        Mx = mzero(big)
        for i in range(n):
            for j in range(n):
                for a in range(2):
                    Mx[i * 2 + a][j * 2 + a] = with_mixer[i][j]
        fams.append(fam_discard(fam_op(Mx), 2))
    return fams, ops


def frame_phase(n, t, ph):
    d = [ONE] * n
    d[t] = ph
    return monomial(list(range(n)), d)


def rot(c, s):
    return [[c, -s], [s, c]]


results, ccs = {}, {}
out = []

# sanity of the constants (floating point, not a decision)
out.append("sanity: cos(pi/8) ~ %.12f, sin(pi/8) ~ %.12f, sqrt2 ~ %.12f" % (
    C8.approx().real, S8.approx().real, SQ2.approx().real))
assert (C8 * C8 + S8 * S8) == ONE and (C4 * C4 + C4 * C4) == ONE and (Z * ZB) == ONE

# ---------------------------------------------------------------- E1, E2, E3, E8: the stated access

e1, e2, e3, e8 = True, True, True, True
level_reached, level_ops = {}, {}
for n, lab in ((2, "level one"), (4, "level two")):
    fams, ops = substratum_families(n)
    R = reached(fams, n)
    level_reached[n], level_ops[n] = R, ops
    diag_ok = all(is_diag(Y) and is_rational_prob(Y) for Y in R.values())
    pm_ok = all(key(cfg(n, s)) in R for s in range(n))
    e1 = e1 and diag_ok and pm_ok
    out.append("E1 %s: %d families, %d distinct reached states, all diagonal probability vectors: %s, "
               "every point mass reached: %s" % (lab, len(fams), len(R), diag_ok, pm_ok))
    orders, fix_ok, map_ok = set(), True, True
    for U in ops:
        sigma = perm_of(U)
        if sigma is None:
            map_ok = False
            continue
        k = perm_order(sigma)
        orders.add(k)
        Uk = mpow(U, k)
        if not all(key(conjm(Uk, Y)) == key(Y) for Y in R.values()):
            fix_ok = False
    bound = 2 if n == 2 else 12
    div_ok = all(bound % k == 0 for k in orders)
    e2 = e2 and map_ok and fix_ok and div_ok
    out.append("E2 %s: %d unitary data; configuration states to configuration states: %s; periods %s "
               "(divide %d: %s); the period fixes every reached state: %s" % (
                   lab, len(ops), map_ok, sorted(orders), bound, div_ok, fix_ok))
    Fp = frame_phase(n, n - 1, Z)
    triv = all(key(conjm(Fp, Y)) == key(Y) for Y in R.values())
    e3 = e3 and triv
    out.append("E3 %s: the frame phase (z at configuration %d) fixes every reached state: %s" % (lab, n - 1, triv))
    nst, nperm, ninv = 0, 0, 0
    for F in fams:
        if len(F) != 1:
            continue
        M = stochastic(F[0], n)
        if M is None:
            e8 = False
            continue
        nst += 1
        colsum = all(sum(M[t][s] for t in range(n)) == 1 and all(M[t][s] >= 0 for t in range(n))
                     for s in range(n))
        Minv = frac_inverse(M)
        nonneg_inv = Minv is not None and all(v >= 0 for r in Minv for v in r)
        perm = is_perm_matrix(M)
        if not colsum or nonneg_inv != perm:
            e8 = False
        nperm += perm
        ninv += nonneg_inv
    out.append("E8 %s: %d deterministic families, all column-stochastic on the configuration states; "
               "nonnegative inverse in %d, permutation matrix in %d" % (lab, nst, ninv, nperm))

plus = [[HALF, HALF], [HALF, HALF]]
Fp1 = frame_phase(2, 1, Z)
d3, n3 = orbit_distinct(Fp1, plus, 200)
cert_z, mp_z = minpoly_not_monic_over_Z(to_sympy(Z))
e3 = e3 and d3 and cert_z
out.append("E3 frame phase on |+><+|: 200 steps, %d distinct members (no return: %s); minimal polynomial of z: %s, "
           "not monic over Z: %s" % (n3, d3, mp_z, cert_z))
results["E1"], results["E2"], results["E3"], results["E8"] = e1, e2, e3, e8

# ---------------------------------------------------------------- E4: the extension by one balanced mixer

R4 = rot(C4, C4)
fams4, ops4 = substratum_families(2, with_mixer=R4)
Rx = reached(fams4, 2)
coh = [Y for Y in Rx.values() if is_coherent(Y)]
plus_in = key(plus) in Rx
d4, n4 = orbit_distinct(Fp1, plus, 200)
# the two families: coherent body and frame-phase infinite orbit on the body agree
stated_coh = any(is_coherent(Y) for Y in level_reached[2].values())
stated_inf = any(orbit_distinct(Fp1, Y, 200)[0] for Y in level_reached[2].values())
ext_coh = len(coh) > 0
ext_inf = any(orbit_distinct(Fp1, Y, 200)[0] for Y in coh[:20])
agree = (stated_coh == stated_inf) and (ext_coh == ext_inf)
results["E4"] = plus_in and d4 and agree and ext_coh
out.append("E4 extension (substratum + rot(pi/4), level one): %d reached states, %d coherent, |+><+| reached: %s; "
           "frame phase orbit of |+><+|: %d distinct; coherent/infinite-orbit: stated access %s/%s, extension %s/%s, "
           "agree: %s" % (len(Rx), len(coh), plus_in, n4, stated_coh, stated_inf, ext_coh, ext_inf, agree))

# ---------------------------------------------------------------- E5: fixedGateTheory(pi/4), level one

S0 = monomial([0, 1], [I, ONE])
S1 = monomial([0, 1], [ONE, I])
X2 = monomial([1, 0], [ONE, ONE])
gens = [R4, X2, S0, S1]
grp = {key(eye(2)): eye(2)}
frontier = [eye(2)]
while frontier:
    nxt = []
    for g in frontier:
        for h in gens:
            p = mmul(g, h)
            k = key(p)
            if k not in grp:
                grp[k] = p
                nxt.append(p)
    frontier = nxt
paulis = [eye(2), X2, monomial([1, 0], [I, -I]), monomial([0, 1], [ONE, -ONE])]


def channel_key(U):
    return tuple(key(conjm(U, P)) for P in paulis)


chans = {}
for U in grp.values():
    chans.setdefault(channel_key(U), U)
orders5 = set()
for U in chans.values():
    ck = channel_key(eye(2))
    cur, k = U, 1
    while channel_key(cur) != ck and k <= 12:
        cur = mmul(cur, U)
        k += 1
    orders5.add(k)
R5 = {}
for U in grp.values():
    for s in range(2):
        Y = conjm(U, cfg(2, s))
        R5[key(Y)] = Y
coh5 = sum(1 for Y in R5.values() if is_coherent(Y))
fp_in = channel_key(Fp1) in chans
results["E5"] = (len(grp) == 192 and len(chans) == 24 and orders5 <= {1, 2, 3, 4} and len(R5) == 6
                 and coh5 == 4 and not fp_in)
out.append("E5 fixedGateTheory(pi/4) level one: group %d elements, %d channels, channel orders %s; reached states %d "
           "(%d coherent); frame phase among the channels: %s" % (len(grp), len(chans), sorted(orders5), len(R5), coh5,
                                                                    fp_in))

# ---------------------------------------------------------------- E6: fixedGateTheory(pi/8), level one

R8 = rot(C8, S8)
W = mmul(mmul(R8, S1), mmul(R8, dag(S1)))
trW = trace(W)
tr_target = ONE + SQ2 * HALF
cert_w, mp_w = minpoly_not_monic_over_Z(to_sympy(trW))
Y6 = conjm(R8, cfg(2, 0))
d6, n6 = orbit_distinct(W, Y6, 200)
results["E6"] = (trW == tr_target) and cert_w and d6 and is_coherent(Y6)
out.append("E6 fixedGateTheory(pi/8) level one: tr W = 1 + sqrt2/2: %s; minimal polynomial %s, not monic over Z: %s; "
           "orbit of rot(pi/8)|0><0|rot(pi/8)^dagger (coherent: %s): %d distinct" % (
               trW == tr_target, mp_w, cert_w, is_coherent(Y6), n6))

# ---------------------------------------------------------------- E7: stage crossing

e7_inf = d3 and d4 and d6
cfg_set = {key(cfg(2, s)) for s in range(2)}
cfg_set4 = {key(cfg(4, s)) for s in range(4)}
pres1 = all({key(conjm(U, cfg(2, s))) for s in range(2)} <= cfg_set for U in level_ops[2])
pres2 = all({key(conjm(U, cfg(4, s))) for s in range(4)} <= cfg_set4 for U in level_ops[4])
results["E7"] = e7_inf and pres1 and pres2
out.append("E7 infinite-order data return within 200 steps: none (%s); every E2 datum preserves the configuration "
           "states: level one %s, level two %s" % (e7_inf, pres1, pres2))

# ---------------------------------------------------------------- countercontrols

ccs["CC1"] = all(is_diag(Y) for Y in Rx.values())
ccs["CC2"] = period_within(Fp1, plus, 200)
W4 = mmul(mmul(R4, S1), mmul(R4, dag(S1)))
tr_w4 = trace(W4)
cert_w4, mp_w4 = minpoly_not_monic_over_Z(to_sympy(tr_w4))
ccs["CC3"] = cert_w4
ccs["CC4"] = all(key(conjm(Fp1, Y)) == key(Y) for Y in Rx.values())
ccs["CC5"] = perm_of(R4) is not None
out.append("countercontrols: CC1 %s, CC2 %s, CC3 %s (tr of the level-one word at pi/4 = 1: %s, minimal polynomial %s), "
           "CC4 %s, CC5 %s" % (ccs["CC1"], ccs["CC2"], ccs["CC3"], tr_w4 == ONE, mp_w4, ccs["CC4"], ccs["CC5"]))

for k in sorted(results):
    out.append("%s %s" % (k, results[k]))
if any(ccs.values()):
    verdict = "VOID"
elif all(results.values()):
    verdict = "O11-FINITE-ON-STATED-ACCESS+ORDINF-IFF-COHERENT"
else:
    verdict = "UNDECIDED (" + ", ".join(k for k in sorted(results) if not results[k]) + ")"
out.append("VERDICT " + verdict)
print("\n".join(out))
print("exit 0", file=sys.stderr)
