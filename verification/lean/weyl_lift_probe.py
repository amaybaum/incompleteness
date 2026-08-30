#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/WeylLift.lean.

LAYERS 3 AND 4 of [Main] Theorem (separability threshold), which end in

    G isotropic  ==>  ( EntanglementBreaking(Phi_G)  iff  |G| = 2^s ).

This probe exists because the obvious construction is WRONG, and the record of why it is wrong is
worth as much as the repair. The self-adjoint involutions H(u) = i^{b.a} W(u) look like they carry
a representation of an isotropic subspace -- they commute, they square to 1 -- so the character
projectors

    P_chi = |G|^{-1} sum_{g in G} chi(g) H(g)

look like projectors. They are not. H is a PROJECTIVE representation: H(u)H(v) = +-H(u+v), and the
sign is -1 on commuting pairs, so P_chi is not idempotent. Its trace still comes out 1 -- the trace
prediction is right, which is exactly what makes the error easy to miss -- but its rank is 2^s.

The repair is a choice of spanning tuple. With g_1,...,g_t a basis of G, the ordered product

    lift(c) = prod_{i : c_i = 1} H(g_i)

IS a homomorphism (F_2^t, +) -> matrices, because the factors commute and square to 1, and every
property of the projectors follows from ordinary character theory of an elementary abelian 2-group.
The lift depends on the tuple and not only on the subspace; that dependence is the content of the
obstruction, not an artefact of the formalization.

Everything below is exact: entries live in Z[i], the projectors are used in their scaled form
Q_e = 2^t P_e so that no division is needed, and ranks are computed by exact Gaussian elimination
over Q(i). No floating point anywhere.

  L1  the product law  H(u)H(v) = beta(u,v) H(u+v)  with beta in {+1,-1},  every pair at s = 1, 2.
  L2  OBSTRUCTION. beta = -1 occurs on COMMUTING pairs -- exhibited on a Lagrangian subspace at
      s = 2, matching the countercontrol WeylTwirl.H_not_multiplicative proves in the kernel.
  L3  COUNTERCONTROL. The naive P_chi built from H on that Lagrangian is not idempotent, and has
      rank 2^s = 4 rather than 1, even though its trace is 1.
  L4  COUNTERCONTROL for the phase normalization: dropping the i^{b.a} factor and using W directly
      makes the generator non-Hermitian on an XZ-type generator, so the self-adjoint projector
      argument does not even start.
  L5  the repaired lift is a homomorphism, self-adjoint, and a unit multiple of a single Weyl
      operator -- exhaustively, over every basis and every coefficient vector at s = 1, 2.
  L6  the character projectors: idempotent, Hermitian, mutually orthogonal, summing to 1, and --
      at t = s with independent generators -- of trace 1 and rank 1.
  L7  COUNTERCONTROL for maximality: at t < s some joint projector has rank > 1, so the
      "complete dephasing" conclusion genuinely needs t = s and not merely commutativity.
  L9  the dephasing identity  sum_chi P_chi rho P_chi = Phi_G(rho)  on a generic complex rho.
  L10 the separable Choi matrix: rank one used as an entrywise factorization, and the Choi matrix
      of the twirl as a sum of pure product projectors -- entanglement breaking, exhibited.
  L11 COUNTERCONTROL for the Choi index convention, on genuinely complex vectors.
  L12 the non-maximal direction: trace 2^(s-t) >= 2, a nonzero 2x2 minor, a plane the twirl fixes
      pointwise, and the antisymmetric witness making the partially transposed Choi form negative.
  L13 THE CONJUGATION GATE for that witness, on a genuinely complex plane.
  L8  lint.

Usage:  python3 weyl_lift_probe.py
"""
import itertools
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.abspath(os.path.join(HERE, '..', 'lean-mathlib'))

CHECKS = []


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


# ---------------------------------------------------------------- exact Q(i) arithmetic
# A scalar is a pair (re, im) of Fractions. Everything the probe forms stays in this field, so
# every equality below is decided exactly and no tolerance is ever consulted.

ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))
I = (Fraction(0), Fraction(1))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def conj(a):
    return (a[0], -a[1])


def inv(a):
    n = a[0] * a[0] + a[1] * a[1]
    return (a[0] / n, -a[1] / n)


def scal_c(k, a):
    return (Fraction(k) * a[0], Fraction(k) * a[1])


def mat_mul(A, B):
    n = len(A)
    return [[
        # sum_k A[i][k] B[k][j]
        _sum(mul(A[i][k], B[k][j]) for k in range(n))
        for j in range(n)] for i in range(n)]


def _sum(terms):
    acc = ZERO
    for t in terms:
        acc = add(acc, t)
    return acc


def mat_add(A, B):
    return [[add(A[i][j], B[i][j]) for j in range(len(A))] for i in range(len(A))]


def mat_smul(k, A):
    return [[scal_c(k, A[i][j]) for j in range(len(A))] for i in range(len(A))]


def mat_scale(a, A):
    return [[mul(a, A[i][j]) for j in range(len(A))] for i in range(len(A))]


def dagger(A):
    n = len(A)
    return [[conj(A[j][i]) for j in range(n)] for i in range(n)]


def eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def zeros(n):
    return [[ZERO for _ in range(n)] for _ in range(n)]


def eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))


def trace(A):
    return _sum(A[i][i] for i in range(len(A)))


def rank(A):
    """Exact rank over Q(i) by Gaussian elimination."""
    M = [row[:] for row in A]
    n = len(M)
    r = 0
    for col in range(n):
        piv = None
        for row in range(r, n):
            if M[row][col] != ZERO:
                piv = row
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        p = inv(M[r][col])
        M[r] = [mul(p, x) for x in M[r]]
        for row in range(n):
            if row != r and M[row][col] != ZERO:
                f = M[row][col]
                M[row] = [sub(M[row][k], mul(f, M[r][k])) for k in range(n)]
        r += 1
    return r


# ---------------------------------------------------------------- the Weyl operators
def basis(s):
    return list(itertools.product((0, 1), repeat=s))


def phase_space(s):
    return list(itertools.product((0, 1), repeat=2 * s))


def split(u, s):
    return u[:s], u[s:]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b)) % 2


def omega(u, v, s):
    ua, ub = split(u, s)
    va, vb = split(v, s)
    return (dot(ub, va) + dot(vb, ua)) % 2


def addv(u, v):
    return tuple((x + y) % 2 for x, y in zip(u, v))


def W(u, s):
    """W(a,b)|y> = (-1)^{b.y} |y+a>."""
    B = basis(s)
    n = len(B)
    ua, ub = split(u, s)
    M = zeros(n)
    for j, y in enumerate(B):
        x = tuple((y[k] + ua[k]) % 2 for k in range(s))
        M[B.index(x)][j] = ONE if dot(ub, y) == 0 else scal_c(-1, ONE)
    return M


def H(u, s):
    ua, ub = split(u, s)
    ph = ONE if dot(ub, ua) == 0 else I
    return mat_scale(ph, W(u, s))


# ---------------------------------------------------------------- L1  the product law
ok1 = True
signs_seen = set()
units_seen = set()
pairs1 = 0
for s in (1, 2):
    for u in phase_space(s):
        for v in phase_space(s):
            pairs1 += 1
            lhs = mat_mul(H(u, s), H(v, s))
            base = H(addv(u, v), s)
            found = None
            for name, unit in (('+1', ONE), ('-1', scal_c(-1, ONE)),
                               ('+i', I), ('-i', scal_c(-1, I))):
                if eq(lhs, mat_scale(unit, base)):
                    found = name
            if found is None:
                ok1 = False
                continue
            units_seen.add(found)
            if omega(u, v, s) == 0:
                if found in ('+i', '-i'):
                    ok1 = False                              # commuting pairs must give a SIGN
                signs_seen.add(found)
ok1 &= signs_seen == {'+1', '-1'}
ok1 &= units_seen == {'+1', '-1', '+i', '-i'}
check("L1", ok1,
      f"the product law H(u)H(v) = beta(u,v) H(u+v) holds with beta a fourth root of unity for "
      f"every one of the {pairs1} phase-space pairs at s = 1, 2. On COMMUTING pairs beta is a sign, "
      f"and both signs occur -- so H is a projective representation and not a representation, even "
      f"restricted to an isotropic subspace. (On anticommuting pairs beta is +-i, since the parity "
      f"of d shifts by omega; that case never enters the projectors, which only ever multiply "
      f"commuting generators)")

# ---------------------------------------------------------------- L2  the obstruction
# The Lagrangian G = <(0,1|0,1), (1,0|1,0)> at s = 2: isotropic, order 4 = 2^s, so maximal.
s = 2
gens = [(0, 1, 0, 1), (1, 0, 1, 0)]
G = [(0, 0, 0, 0), gens[0], gens[1], addv(gens[0], gens[1])]
ok2 = len(set(G)) == 4
ok2 &= all(addv(x, y) in G for x in G for y in G)            # a subspace
ok2 &= all(omega(x, y, s) == 0 for x in G for y in G)        # isotropic
ok2 &= len(G) == 2 ** s                                      # maximal: |G| = 2^s
bad = [(u, v) for u in G for v in G
       if not eq(mat_mul(H(u, s), H(v, s)), H(addv(u, v), s))]
ok2 &= len(bad) == 6
ok2 &= all(eq(mat_mul(H(u, s), H(v, s)), mat_smul(-1, H(addv(u, v), s))) for u, v in bad)
ok2 &= ((0, 1, 0, 1), (1, 0, 1, 0)) in bad                   # the pair the Lean countercontrol uses
check("L2", ok2,
      "OBSTRUCTION. On the Lagrangian G = <(0,1|0,1),(1,0|1,0)> at s = 2 -- isotropic, of the "
      "maximal order 2^s -- six of the sixteen pairs have H(u)H(v) = -H(u+v), among them the pair "
      "WeylTwirl.H_not_multiplicative exhibits in the kernel. The sign survives commutativity: "
      "d(u+v) = d(u)+d(v)+omega(u,v) holds in ZMod 2, but the exponents of i add in Z")

# ---------------------------------------------------------------- L3  the naive projectors fail
def naive_P(G, e_index, s):
    """|G|^{-1} sum_{g in G} chi_e(g) H(g), scaled by |G| to stay in Z[i]."""
    acc = zeros(2 ** s)
    for k, g in enumerate(G):
        sgn = 1 if e_index[k] == 0 else -1
        acc = mat_add(acc, mat_smul(sgn, H(g, s)))
    return acc                                              # = |G| * P


# The four characters of G = Z/2 x Z/2, written as their sign patterns on (0, g1, g2, g1+g2).
CHARS = [(0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1), (0, 1, 1, 0)]
ok3 = True
for pat in CHARS:
    Q = naive_P(G, pat, s)                                   # Q = 4 P
    # idempotence of P is  Q*Q = 4 Q
    ok3 &= not eq(mat_mul(Q, Q), mat_smul(len(G), Q))
    # the trace prediction is nevertheless right: tr P = 1, i.e. tr Q = 4
    ok3 &= trace(Q) == scal_c(len(G), ONE)
    ok3 &= rank(Q) == 2 ** s                                 # rank 4, not 1
check("L3", ok3,
      "COUNTERCONTROL. Every one of the four naive P_chi on that Lagrangian has trace exactly 1 -- "
      "the prediction the printed argument makes -- and yet none is idempotent and every one has "
      "rank 2^s = 4. Trace alone does not certify rank; that is precisely why the projective phase "
      "has to be dealt with rather than assumed away")

# ---------------------------------------------------------------- L4  the phase is needed
# Dropping i^{b.a} and using W directly: on an XZ-type generator W is anti-Hermitian in the sense
# that W^dagger = -W, so no character combination of Ws is a self-adjoint projector.
s1 = 1
XZ = (1, 1)
ok4 = eq(dagger(W(XZ, s1)), mat_smul(-1, W(XZ, s1)))
ok4 &= not eq(dagger(W(XZ, s1)), W(XZ, s1))
ok4 &= eq(dagger(H(XZ, s1)), H(XZ, s1))                      # the normalized version IS Hermitian
ok4 &= eq(mat_mul(W(XZ, s1), W(XZ, s1)), mat_smul(-1, eye(2)))
ok4 &= eq(mat_mul(H(XZ, s1), H(XZ, s1)), eye(2))
check("L4", ok4,
      "COUNTERCONTROL for the phase normalization. On the XZ-type generator (1|1) the bare Weyl "
      "operator has W^dagger = -W and W^2 = -1, so the self-adjoint projector argument cannot even "
      "be started from W; the normalized H(u) = i^{b.a} W(u) is Hermitian and squares to 1. The "
      "phase is doing real work -- which is why it cannot simply be dropped to dodge L2")

# ---------------------------------------------------------------- L5  the repaired lift
def lift(gens, c, s):
    """The ordered product prod_{i : c_i = 1} H(g_i)."""
    M = eye(2 ** s)
    for gi, ci in zip(gens, c):
        if ci:
            M = mat_mul(M, H(gi, s))
    return M


def span(gens, s):
    out = []
    for c in itertools.product((0, 1), repeat=len(gens)):
        v = tuple([0] * (2 * s))
        for gi, ci in zip(gens, c):
            if ci:
                v = addv(v, gi)
        out.append(v)
    return out


def isotropic_tuples(s, t):
    """All t-tuples of phase-space vectors that are independent and pairwise commuting."""
    out = []
    for gens in itertools.product(phase_space(s), repeat=t):
        if any(omega(u, v, s) for u in gens for v in gens):
            continue
        sp = span(gens, s)
        if len(set(sp)) != 2 ** t:                           # independence
            continue
        out.append(gens)
    return out


ok5 = True
cases5 = 0
for s in (1, 2):
    for t in range(0, s + 1):
        for gens in isotropic_tuples(s, t):
            cases5 += 1
            for c in itertools.product((0, 1), repeat=t):
                Lc = lift(gens, c, s)
                # self-adjoint
                ok5 &= eq(dagger(Lc), Lc)
                # a unit multiple of the Weyl operator at the F_2 combination
                v = tuple([0] * (2 * s))
                for gi, ci in zip(gens, c):
                    if ci:
                        v = addv(v, gi)
                ok5 &= (eq(Lc, W(v, s)) or eq(Lc, mat_smul(-1, W(v, s)))
                        or eq(Lc, mat_scale(I, W(v, s)))
                        or eq(Lc, mat_scale(scal_c(-1, I), W(v, s))))
                for c2 in itertools.product((0, 1), repeat=t):
                    csum = tuple((a + b) % 2 for a, b in zip(c, c2))
                    ok5 &= eq(mat_mul(Lc, lift(gens, c2, s)), lift(gens, csum, s))
ok5 &= cases5 > 0
check("L5", ok5,
      f"the repaired lift, over all {cases5} independent commuting tuples at s = 1, 2 and every "
      f"coefficient vector: lift(c) lift(c') = lift(c+c') EXACTLY -- a homomorphism, no sign left "
      f"-- each lift is self-adjoint, and each is a unit multiple of the single Weyl operator at "
      f"the F_2 combination its coefficients name")

# ---------------------------------------------------------------- L6  the character projectors
def proj(gens, e, s):
    """2^t P_e = sum_c (-1)^{e.c} lift(c), kept scaled so entries stay in Z[i]."""
    t = len(gens)
    acc = zeros(2 ** s)
    for c in itertools.product((0, 1), repeat=t):
        sgn = 1 if dot(e, c) == 0 else -1
        acc = mat_add(acc, mat_smul(sgn, lift(gens, c, s)))
    return acc


ok6 = True
cases6 = 0
for s in (1, 2):
    for gens in isotropic_tuples(s, s):                      # the MAXIMAL case t = s
        cases6 += 1
        N = 2 ** s
        chars = list(itertools.product((0, 1), repeat=s))
        Qs = {e: proj(gens, e, s) for e in chars}
        tot = zeros(2 ** s)
        for e in chars:
            Q = Qs[e]
            ok6 &= eq(mat_mul(Q, Q), mat_smul(N, Q))         # P idempotent
            ok6 &= eq(dagger(Q), Q)                          # P Hermitian
            ok6 &= trace(Q) == scal_c(N, ONE)                # tr P = 1
            ok6 &= rank(Q) == 1                              # RANK ONE
            tot = mat_add(tot, Q)
            for e2 in chars:
                if e2 != e:
                    ok6 &= eq(mat_mul(Q, Qs[e2]), zeros(2 ** s))
        ok6 &= eq(tot, mat_smul(N, eye(2 ** s)))             # sum_e P_e = 1
ok6 &= cases6 > 0
check("L6", ok6,
      f"the character projectors built from the lift, over all {cases6} Lagrangian tuples at "
      f"s = 1, 2: idempotent, Hermitian, mutually orthogonal, summing to the identity, of trace 1 "
      f"and -- the gate the maximal case actually needs -- of RANK 1. The joint eigenspaces are "
      f"lines, kernel-proved rather than read off 'maximal abelian'")

# ---------------------------------------------------------------- L7  maximality is needed
ok7 = True
cases7 = 0
for s in (2,):
    for t in range(0, s):                                    # NON-maximal: t < s
        for gens in isotropic_tuples(s, t):
            cases7 += 1
            chars = list(itertools.product((0, 1), repeat=t))
            ranks = [rank(proj(gens, e, s)) for e in chars]
            ok7 &= all(r == 2 ** (s - t) for r in ranks)
            ok7 &= any(r > 1 for r in ranks)
ok7 &= cases7 > 0
check("L7", ok7,
      f"COUNTERCONTROL for maximality, over all {cases7} non-maximal independent commuting tuples "
      f"at s = 2: every joint projector has rank 2^{{s-t}} > 1, so the joint eigenspaces are not "
      f"lines and no complete dephasing follows. The conclusion needs |G| = 2^s and not merely "
      f"that G is isotropic")

# ---------------------------------------------------------------- L9  the dephasing identity
def Pproj(gens, e, s):
    """The actual projector 2^{-t} sum_c chi(e.c) lift(c)."""
    t = len(gens)
    return mat_scale((Fraction(1, 2 ** t), Fraction(0)), proj(gens, e, s))


def twirl(G, rho, s):
    acc = zeros(2 ** s)
    for g in G:
        Wg = W(g, s)
        acc = mat_add(acc, mat_mul(mat_mul(Wg, rho), dagger(Wg)))
    return mat_scale((Fraction(1, len(G)), Fraction(0)), acc)


def generic_rho(s):
    """A deliberately non-Hermitian, genuinely complex matrix: the identity is claimed for ALL rho,
    so testing it on a state would be a weaker test than testing it on this."""
    n = 2 ** s
    return [[(Fraction(1 + a + 2 * b), Fraction(1 + a * b - b)) for b in range(n)]
            for a in range(n)]


ok9 = True
cases9 = 0
for s in (1, 2):
    rho = generic_rho(s)
    for gens in isotropic_tuples(s, s):
        cases9 += 1
        G = span(gens, s)
        acc = zeros(2 ** s)
        for e in itertools.product((0, 1), repeat=s):
            Pe = Pproj(gens, e, s)
            acc = mat_add(acc, mat_mul(mat_mul(Pe, rho), dagger(Pe)))
        ok9 &= eq(acc, twirl(G, rho, s))
ok9 &= cases9 > 0
check("L9", ok9,
      f"THE DEPHASING IDENTITY sum_chi P_chi rho P_chi = Phi_G(rho), over all {cases9} Lagrangian "
      f"tuples at s = 1, 2 and a non-Hermitian generically complex rho. The projectors are built "
      f"from a chosen tuple and the twirl is not; they agree, which is what makes a "
      f"tuple-dependent construction legitimate for a tuple-independent theorem")

# ---------------------------------------------------------------- L10  the separable Choi matrix
def single_mat(p1, q1, n):
    M = zeros(n)
    M[p1][q1] = ONE
    return M


def choi(Phi, s, dim=None):
    """J(Phi)[(p1,p2)][(q1,q2)] = Phi(E_{p1 q1})[p2][q2], ancilla index FIRST -- the convention
    OIBridge/Separability.lean fixes."""
    n = dim if dim is not None else 2 ** s
    J = [[ZERO] * (n * n) for _ in range(n * n)]
    for p1 in range(n):
        for q1 in range(n):
            out = Phi(single_mat(p1, q1, n))
            for p2 in range(n):
                for q2 in range(n):
                    J[p1 * n + p2][q1 * n + q2] = out[p2][q2]
    return J


def prodProj(u, v, n):
    """|u (x) v><u (x) v| at ((p1,p2),(q1,q2)) = u[p1] v[p2] conj(u[q1] v[q2])."""
    J = [[ZERO] * (n * n) for _ in range(n * n)]
    for p1 in range(n):
        for p2 in range(n):
            for q1 in range(n):
                for q2 in range(n):
                    J[p1 * n + p2][q1 * n + q2] = mul(mul(u[p1], v[p2]),
                                                      conj(mul(u[q1], v[q2])))
    return J


def rank_one_factor(M):
    """M[a][i] = x[a] * y[i]; returns (x, y). Requires M of rank one."""
    n = len(M)
    j0 = next(j for j in range(n) if any(M[a][j] != ZERO for a in range(n)))
    a0 = next(a for a in range(n) if M[a][j0] != ZERO)
    x = [M[a][j0] for a in range(n)]
    y = [mul(M[a0][i], inv(M[a0][j0])) for i in range(n)]
    return x, y


ok10 = True
cases10 = 0
for s in (1, 2):
    n = 2 ** s
    for gens in isotropic_tuples(s, s):
        cases10 += 1
        G = span(gens, s)
        J = choi(lambda r: twirl(G, r, s), s)
        acc = [[ZERO] * (n * n) for _ in range(n * n)]
        for e in itertools.product((0, 1), repeat=s):
            Pe = Pproj(gens, e, s)
            # the factorization rank one supplies, with no eigenvector anywhere
            x, y = rank_one_factor(Pe)
            for a in range(n):
                for i in range(n):
                    ok10 &= Pe[a][i] == mul(x[a], y[i])
            term = prodProj(y, x, n)
            ok10 &= eq(choi(lambda r: mat_mul(mat_mul(Pe, r), dagger(Pe)), s), term)
            acc = [[add(acc[i][j], term[i][j]) for j in range(n * n)] for i in range(n * n)]
        ok10 &= eq(J, acc)
ok10 &= cases10 > 0
check("L10", ok10,
      f"THE SEPARABLE CHOI MATRIX, over all {cases10} Lagrangian tuples at s = 1, 2. Each P_chi "
      f"factors entrywise as P[a][i] = x[a] y[i] -- rank one used with no eigenvector, no "
      f"orthonormal basis and no square root -- the Choi matrix of rho |-> P rho P^dagger is "
      f"exactly the pure product projector prodProj(y, x) with the ancilla index taking y, and the "
      f"Choi matrix of the twirl is their sum. That is entanglement breaking, exhibited")

# ---------------------------------------------------------------- L11  the index convention
# prodProj(y, x) and prodProj(x, y) are genuinely different objects; the Lean proof commits to the
# first, and a real complex example is needed to see the difference at all.
ok11 = False
for s in (1, 2):
    n = 2 ** s
    for gens in isotropic_tuples(s, s):
        for e in itertools.product((0, 1), repeat=s):
            x, y = rank_one_factor(Pproj(gens, e, s))
            if not eq(prodProj(y, x, n), prodProj(x, y, n)):
                ok11 = True
check("L11", ok11,
      "COUNTERCONTROL for the Choi index convention. prodProj(y, x) and prodProj(x, y) genuinely "
      "differ on these projectors, so the order in `choi_conj_of_factor` is a real commitment and "
      "not a harmless relabelling -- the same discipline the Kraus transpose guard applies")

# ---------------------------------------------------------------- L12  the non-maximal direction
def ptranspose(J, n):
    T = [[ZERO] * (n * n) for _ in range(n * n)]
    for p1 in range(n):
        for p2 in range(n):
            for q1 in range(n):
                for q2 in range(n):
                    T[p1 * n + p2][q1 * n + q2] = J[p1 * n + q2][q1 * n + p2]
    return T


def qform(M, w):
    acc = ZERO
    for p in range(len(M)):
        for q in range(len(M)):
            acc = add(acc, mul(mul(conj(w[p]), M[p][q]), w[q]))
    return acc


def minor_pair(M):
    """(a, b, i, j) with a non-vanishing 2x2 minor, or None."""
    n = len(M)
    for a in range(n):
        for b in range(n):
            for i in range(n):
                for j in range(n):
                    if mul(M[a][i], M[b][j]) != mul(M[a][j], M[b][i]):
                        return a, b, i, j
    return None


def witness(x, y, n):
    """w(i,a) = conj(x_i) conj(y_a) - conj(y_i) conj(x_a), ancilla index first."""
    return [sub(mul(conj(x[p // n]), conj(y[p % n])), mul(conj(y[p // n]), conj(x[p % n])))
            for p in range(n * n)]


ok12 = True
cases12 = 0
for s in (1, 2):
    n = 2 ** s
    for t in range(0, s):
        for gens in isotropic_tuples(s, t):
            cases12 += 1
            G = span(gens, s)
            Phi = lambda r, G=G, s=s: twirl(G, r, s)
            T = ptranspose(choi(Phi, s), n)
            Pe = Pproj(gens, (0,) * t, s)
            # the trace is 2^{s-t} >= 2, so no rank-one factorization can exist
            ok12 &= trace(Pe) == (Fraction(2 ** (s - t)), Fraction(0))
            mp = minor_pair(Pe)
            ok12 &= mp is not None
            a0, b0, i, j = mp
            x = [Pe[k][i] for k in range(n)]
            y = [Pe[k][j] for k in range(n)]
            # the twirl fixes the plane pointwise, on every combination
            for (al, be, ga, de) in itertools.product((ONE, I, scal_c(-1, ONE)), repeat=4):
                u = [add(mul(al, x[k]), mul(be, y[k])) for k in range(n)]
                v = [add(mul(ga, x[k]), mul(de, y[k])) for k in range(n)]
                op = [[mul(u[k], conj(v[l])) for l in range(n)] for k in range(n)]
                ok12 &= eq(Phi(op), op)
            # and the witness is negative, at exactly the predicted value
            q = qform(T, witness(x, y, n))
            pred = ZERO
            for a in range(n):
                for b in range(n):
                    z = sub(mul(y[a], x[b]), mul(x[a], y[b]))
                    pred = sub(pred, mul(z, conj(z)))
            ok12 &= q == pred
            ok12 &= q[0] < 0
ok12 &= cases12 > 0
check("L12", ok12,
      f"THE NON-MAXIMAL DIRECTION, over all {cases12} non-maximal isotropic subspaces at s = 1, 2. "
      f"Each character projector has trace exactly 2^(s-t) >= 2, so no rank-one factorization "
      f"exists and some 2x2 minor is nonzero; the two columns it names span a plane the twirl fixes "
      f"pointwise on all 81 coefficient combinations tried; and the antisymmetric witness makes the "
      f"partially transposed Choi form equal -sum_(a,b) |y_a x_b - x_a y_b|^2, hence negative. That "
      f"is the route `not_entanglementBreaking_twirl` takes, with no anticommuting pair anywhere")

# ---------------------------------------------------------------- L13  the conjugation gate
# The witness is  conj(x) (x) conj(y) - conj(y) (x) conj(x).  On REAL vectors every variant below
# coincides with it, so the guard needs a genuinely complex plane. Phi(rho) = P rho P for P the
# orthogonal projector onto span{x,y} fixes the plane and is linear, which is all
# `not_eb_of_fixed_plane` asks of it.
def ip(u, v):
    return _sum(mul(conj(u[k]), v[k]) for k in range(len(u)))


n13 = 3
x13 = [(Fraction(1), Fraction(-1)), (Fraction(1), Fraction(1)), (Fraction(0), Fraction(2))]
y13 = [(Fraction(1, 4), Fraction(1, 4)), (Fraction(-1, 4), Fraction(1, 4)),
       (Fraction(1, 2), Fraction(0))]
ok13 = ip(x13, y13) == ZERO                      # orthogonal
ok13 &= any(z[1] != 0 for z in x13) and any(z[1] != 0 for z in y13)   # genuinely complex
P13 = mat_add(
    mat_scale(inv(ip(x13, x13)), [[mul(x13[a], conj(x13[b])) for b in range(n13)]
                                  for a in range(n13)]),
    mat_scale(inv(ip(y13, y13)), [[mul(y13[a], conj(y13[b])) for b in range(n13)]
                                  for a in range(n13)]))
Phi13 = lambda r: mat_mul(mat_mul(P13, r), dagger(P13))
T13 = ptranspose(choi(Phi13, None, n13), n13)
pred13 = scal_c(-2, mul(ip(x13, x13), ip(y13, y13)))
q_right = qform(T13, witness(x13, y13, n13))
ok13 &= q_right == pred13
VARIANTS = {
    'no conjugation at all': lambda i, a: sub(mul(x13[i], y13[a]), mul(y13[i], x13[a])),
    'conjugated on the ancilla slot only':
        lambda i, a: sub(mul(conj(x13[i]), y13[a]), mul(conj(y13[i]), x13[a])),
    'conjugated on the output slot only':
        lambda i, a: sub(mul(x13[i], conj(y13[a])), mul(y13[i], conj(x13[a]))),
    'symmetric instead of antisymmetric':
        lambda i, a: add(mul(conj(x13[i]), conj(y13[a])), mul(conj(y13[i]), conj(x13[a]))),
}
wrong_ok = 0
for name, f in VARIANTS.items():
    qv = qform(T13, [f(p // n13, p % n13) for p in range(n13 * n13)])
    ok13 &= qv != pred13                              # every variant gets the value wrong
    if qv[0] >= 0:
        wrong_ok += 1
ok13 &= wrong_ok >= 3                                 # and at least three refute nothing at all
check("L13", ok13,
      f"THE CONJUGATION GATE. On a genuinely complex orthogonal plane the witness gives exactly "
      f"-2|x|^2|y|^2 = {pred13[0]}, and all four obvious variants get the value wrong -- {wrong_ok} "
      f"of them come out NON-NEGATIVE and so would refute nothing. On real vectors all five "
      f"coincide, which is why the guard has to be complex; the same discipline as the Kraus "
      f"transpose and the Choi index order")

# ---------------------------------------------------------------- L8  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'WeylLift.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
body = src[src.index('namespace OIBridge'):]

NAMES = ('fac_mul', 'lift_mul', 'lift_conjTranspose', 'lift_eq_smul_W', 'P_conjTranspose',
         'P_mul_self', 'P_mul_of_ne', 'sum_P', 'trace_P', 'trace_P_eq_one',
         'lift_conj', 'exists_lagrangian_tuple', 'sum_P_conj', 'sum_P_conj_eq_twirl',
         'exists_factor_of_finrank_range_eq_one', 'finrank_range_P',
         'entanglementBreaking_twirl', 'exists_minor_ne_of_idem_trace', 'trace_P_nonmaximal',
         'twirl_fixes_plane', 'not_entanglementBreaking_twirl', 'entanglementBreaking_iff',
         'entanglementBreaking_iff_dim')
ok8 = 'import OIBridge.WeylLift' in root
ok8 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
ok8 &= re.search(r'(?m)^axiom ', body) is None
ok8 &= all(f'theorem {n}' in src for n in NAMES)
ok8 &= all(f'#print axioms {n}' in src for n in NAMES)
ok8 &= 'native_decide' not in body
# the homomorphism property must be the stated conclusion, not an assumption
lm = src[src.index('theorem lift_mul'):]
ok8 &= 'lift t g c * lift t g c\' = lift t g (c + c\')' in lm[:lm.index(':= by')]
# rank one must be a finrank statement, not a trace statement wearing its name
ok8 &= 'Module.finrank ℂ (LinearMap.range (Matrix.toLin\' (P s g e))) = 1' in src
# the obstruction must be recorded in the kernel, in WeylTwirl, and referred to here
twirl_src = open(os.path.join(BRIDGE, 'OIBridge', 'WeylTwirl.lean'), encoding='utf-8').read()
ok8 &= 'theorem H_not_multiplicative' in twirl_src
ok8 &= '#print axioms H_not_multiplicative' in twirl_src
ok8 &= 'H_not_multiplicative' in src
# THE WRAPPER'S HYPOTHESES MUST BE ON G, NOT ON A TUPLE. This is the gate that keeps the
# tuple-dependent construction from leaking into the manuscript-facing statement.
wr = src[src.index('theorem entanglementBreaking_twirl'):]
sig = wr[:wr.index(':= by')]
ok8 &= 'G : Submodule (ZMod 2) (PS s)' in sig
ok8 &= 'hiso : Isotropic G' in sig
ok8 &= "hcard : (gset G).card = 2 ^ s" in sig
ok8 &= 'Separability.EntanglementBreaking (twirl G)' in sig
for banned in ('Fin s → PS s', 'Indep', 'spanF', 'lift', 'P s g'):
    ok8 &= banned not in sig                     # no tuple, no lift, no projector in the statement
# and the tuple it does use has to be produced from G, not assumed
ok8 &= 'exists_lagrangian_tuple G hiso hcard' in wr
# THE TERMINAL WRAPPER, likewise: an iff, with hypotheses naming only G
iw = src[src.index('theorem entanglementBreaking_iff '):]
isig = iw[:iw.index(':= by')]
ok8 &= 'hiso : Isotropic G' in isig
ok8 &= "EntanglementBreaking (twirl G) ↔ (gset G).card = 2 ^ s" in isig
for banned in ('Fin s → PS s', 'Indep', 'spanF', 'lift', 'P s g', 'perp'):
    ok8 &= banned not in isig
# the converse must NOT go through an anticommuting pair: it is the block-rank route
nb = src[src.index('theorem not_entanglementBreaking_twirl'):]
nbody = nb[:nb.index('/-! ###')]
for banned in ('perp', 'anticommut', 'W_conj'):
    ok8 &= banned not in nbody
ok8 &= 'not_eb_of_fixed_plane' in nbody
ok8 &= 'exists_minor_ne_of_idem_trace' in nbody
check("L8", ok8,
      f"LINT. The file is imported by OIBridge.lean so CI builds it; no `sorry`, no `axiom`, no "
      f"`native_decide`; all {len(NAMES)} named results print their axiom dependencies. "
      f"`lift_mul` states the homomorphism property as its conclusion, rank one is a `finrank` "
      f"statement and not a trace statement wearing its name, and the obstruction that motivates "
      f"the whole file is itself kernel-proved as `WeylTwirl.H_not_multiplicative`")

print()
print('     [scope] [Main] Theorem (separability threshold) is settled in Lean, both directions,')
print('     as entanglementBreaking_iff: for isotropic G, Phi_G is entanglement breaking exactly')
print('     when |G| = 2^s, with hypotheses naming only G. The maximal direction runs through the')
print('     rank-one character projectors and an explicit separable Choi matrix; the non-maximal')
print('     one through a projector of trace 2^(s-t) >= 2, a fixed two-dimensional sector, and')
print('     one antisymmetric witness. Neither uses an eigenvector, a spectral theorem, a Witt')
print('     extension, or the Clifford group.')
print()
print("weyl_lift_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
