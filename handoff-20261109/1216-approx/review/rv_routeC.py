#!/usr/bin/env python3
"""Reviewer's exact generic checks for #1216 unit 1 (route C, NX-1 vs FI-1).  Imports nothing earlier.

C1  Shuffle-only reachability on a configuration carrier: for every permutation of a 3-set and
    symbolic phases, conjugation by the monomial operator maps a symbolic diagonal matrix to a
    diagonal one; partial trace over a diagonal ancilla keeps diagonals (symbolic, 2x2 system x 2
    ancilla).  Countercontrol: Hadamard conjugation of |0><0| is not diagonal.
C2  Distance: for rho in {x+ (x) z+, y+ (x) z+} and a symbolic diagonal D (complex entries allowed),
    tr((rho - D) W) = 1 with W = X(x)Z resp. Y(x)Z, ||W||_op = 1, so trace distance >= 1/2; the
    bound is attained at D = diag(rho) (exact eigenvalues of rho - diag(rho) are +-1/2, 0, 0).
    Countercontrol: with W = Z(x)Z the same expression depends on D (no bound).
C3  Non-real operation: for symbolic real symmetric R, tr(R Y) = 0; real Kraus operators keep real
    symmetric inputs real symmetric (symbolic 2x2).
C4  FI-1 does not imply NX-1 at the level of THEORIES: the class CM of "column-monomial" matrices
    (at most one nonzero entry in every column) is closed under the Architecture operations of
    OIBridge/ImplementationLocality.lean (identity, product, contraction by |a| <= 1, ancilla
    projectors, ancilla blocks), contains the non-monomial K = |0>(<0| + <1|)/sqrt2, and every
    conjugation by a CM matrix preserves diagonal states, so every branch of the theory it generates
    (finite sums of admissible conjugations, realized_of_instAvail) preserves diagonals.  Checked
    symbolically: product of two generic CM patterns (all 3x3 patterns), blocks of generic 4x4 CM
    patterns on S x Fin 2, conjugation of a symbolic diagonal by every 3x3 CM pattern.  Also: a
    unitary in CM is monomial (all 2x2 and 3x3 patterns with orthonormal columns).
    Countercontrol: the Hadamard matrix is not CM and does not preserve diagonals.
C5  Law-level gap (route C, two configurations, no memory outside the carrier, one fixed classical
    stochastic map reused for each "H"): on the protocols (|0>, H, Z) and (|0>, H, H, Z) the larger
    TV error is >= (sqrt2 - 1)/2, attained.  Countercontrol: the coherent Hadamard has gap 0.
Run: python3 -I -B rv_routeC.py   (exit 0 iff all pass)
"""
import itertools
import sys

import sympy as sp

FAIL = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)


def is_diag(M):
    return all(sp.expand(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols) if i != j)


kp = sp.kronecker_product
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.diag(1, -1); I2 = sp.eye(2)

# C1 ------------------------------------------------------------------------
w = sp.symbols('w0:3')
ph = sp.symbols('f0:3')
Dw = sp.diag(*w)
ok = True
for p in itertools.permutations(range(3)):
    P = sp.zeros(3)
    for j in range(3):
        P[p[j], j] = 1
    Kmon = P * sp.diag(*ph)
    ok &= is_diag(Kmon * Dw * Kmon.conjugate().T)
check("C1 every monomial conjugation (all 6 permutations x symbolic phases) maps symbolic diagonals to diagonals", ok)
u = sp.symbols('u0:4')
Dsa = sp.diag(*u)              # system (x) ancilla, ordering (s, a)
red = sp.Matrix(2, 2, lambda i, j: sum(Dsa[2 * i + a, 2 * j + a] for a in range(2)))
check("C1 partial trace of a symbolic diagonal over the ancilla is diagonal", is_diag(red))
Hd = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
check("C1 countercontrol: H|0><0|H is not diagonal", not is_diag(Hd * sp.diag(1, 0) * Hd.T))

# C2 ------------------------------------------------------------------------
xp = sp.Matrix([1, 1]) / sp.sqrt(2); yp = sp.Matrix([1, sp.I]) / sp.sqrt(2); zp = sp.Matrix([1, 0])
d = sp.symbols('d0:4')
Dg = sp.diag(*d)
for nm, st, W in (("x+ (x) z+", kp(xp, zp), kp(X, Z)), ("y+ (x) z+", kp(yp, zp), kp(Y, Z))):
    rho = st * st.H
    val = sp.expand(((rho - Dg) * W).trace())
    opn = max(abs(e) for e in W.eigenvals())
    dd = sp.diag(*[rho[i, i] for i in range(4)])
    evs = (rho - dd).eigenvals()
    tn = sum(abs(e) * m for e, m in evs.items())
    check(f"C2 {nm}: tr((rho - D)W) = 1 for symbolic diagonal D, ||W||_op = 1, so TD >= 1/2", val == 1 and opn == 1)
    check(f"C2 {nm}: attained, ||rho - diag(rho)||_1 = 1 exactly (TD = 1/2)", sp.simplify(tn) == 1)
rho = kp(xp, zp) * kp(xp, zp).H
check("C2 countercontrol: with W = Z(x)Z the expression depends on D",
      sp.expand(((rho - Dg) * kp(Z, Z)).trace()).free_symbols != set())

# C3 ------------------------------------------------------------------------
a, b, c = sp.symbols('a b c', real=True)
R = sp.Matrix([[a, b], [b, c]])
check("C3 tr(R Y) = 0 for every real symmetric R", sp.expand((R * Y).trace()) == 0)
k = sp.symbols('k0:4', real=True)
Kr = sp.Matrix(2, 2, k)
out = Kr * R * Kr.T
check("C3 a real Kraus operator maps real symmetric to real symmetric",
      all(sp.im(sp.expand(e)) == 0 for e in out) and sp.expand(out - out.T) == sp.zeros(2))
plusi = sp.Matrix([[1, -sp.I], [sp.I, 1]]) / 2
check("C3 hence tr((|+i><+i| - R) Y) = 1 for every real symmetric R",
      sp.expand(((plusi - R) * Y).trace()) == 1)


# C4 ------------------------------------------------------------------------
def cm_patterns(n):
    """All column patterns: each column has its nonzero (if any) in one row, or is zero."""
    return list(itertools.product(list(range(n)) + [None], repeat=n))


def cm_matrix(pattern, sym):
    n = len(pattern)
    M = sp.zeros(n)
    for j, r in enumerate(pattern):
        if r is not None:
            M[r, j] = sym[j]
    return M


def is_cm(M):
    return all(sum(1 for i in range(M.rows) if sp.expand(M[i, j]) != 0) <= 1 for j in range(M.cols))


def is_monomial(M):
    n = M.rows
    return all(sum(1 for j in range(n) if sp.expand(M[i, j]) != 0) == 1 for i in range(n)) and \
        all(sum(1 for i in range(n) if sp.expand(M[i, j]) != 0) == 1 for j in range(n))


al = sp.symbols('al0:3'); be = sp.symbols('be0:3')
pats3 = cm_patterns(3)
ok_mul = all(is_cm(cm_matrix(p, al) * cm_matrix(q, be)) for p in pats3 for q in pats3)
check(f"C4 product of two symbolic CM matrices is CM (all {len(pats3)}^2 3x3 pattern pairs)", ok_mul)
ok_conj = all(is_diag(cm_matrix(p, al) * Dw * cm_matrix(p, al).conjugate().T) for p in pats3)
check("C4 conjugation by every symbolic 3x3 CM matrix maps symbolic diagonals to diagonals", ok_conj)
check("C4 identity and ancilla projectors diag(r.2 = k) are CM; a scalar multiple of a CM matrix is CM",
      is_cm(sp.eye(4)) and all(is_cm(sp.diag(*[1 if (r % 2) == kk else 0 for r in range(4)])) for kk in range(2))
      and is_cm(sp.Symbol('t') * cm_matrix(pats3[5], al)))
ga = sp.symbols('ga0:4')
ok_blk = True
for p in cm_patterns(4):          # S = Fin 2, ancilla Fin 2, index 2*s + a
    M = cm_matrix(p, ga)
    for f in range(2):
        for e in range(2):
            blk = sp.Matrix(2, 2, lambda i, j: M[2 * i + f, 2 * j + e])
            ok_blk &= is_cm(blk)
check("C4 every ancilla block (f,e) of every symbolic 4x4 CM matrix on S x Fin 2 is CM (625 patterns)", ok_blk)
Kw = sp.Matrix([[1, 1], [0, 0]]) / sp.sqrt(2)
check("C4 K = |0>(<0|+<1|)/sqrt2 is CM, not monomial, and K^dag K <= I (eigenvalues 0, 1)",
      is_cm(Kw) and not is_monomial(Kw) and set((Kw.H * Kw).eigenvals()) == {0, 1})
ok_uni = True
for n in (2, 3):
    for p in cm_patterns(n):
        if None in p or len(set(p)) < n:
            continue   # a CM matrix with orthonormal columns has nonzero, distinct-row columns
        ok_uni &= is_monomial(cm_matrix(p, sp.symbols(f'h0:{n}')))
check("C4 every CM matrix with orthonormal columns has the monomial pattern (n = 2, 3)", ok_uni)
check("C4 countercontrol: Hadamard is not CM", not is_cm(Hd))

# C5 ------------------------------------------------------------------------
# Operational (law-level) gap on a two-configuration carrier with no memory outside it: every
# classical stochastic map M = [[p, q], [1-p, 1-q]] used for "H" gives, on the protocols
# (|0>, H, read Z) and (|0>, H, H, read Z), TVs |p - 1/2| and 1 - p^2 - q(1-p) >= p(1-p) (q <= 1);
# max(|p - 1/2|, p(1-p)) >= (sqrt2 - 1)/2 on [0, 1], with equality at p = 1/sqrt2, q = 1.
p_, q_ = sp.symbols('p q', real=True)
g = (sp.sqrt(2) - 1) / 2
tv2 = 1 - p_ ** 2 - q_ * (1 - p_)
check("C5 1 - p^2 - q(1-p) - p(1-p) = (1-q)(1-p) >= 0 on [0,1]^2",
      sp.expand(tv2 - p_ * (1 - p_) - (1 - q_) * (1 - p_)) == 0)
# on |p - 1/2| < g, p(1-p) = 1/4 - (p-1/2)^2 > 1/4 - g^2 = g  (exact identity 1/4 - g^2 = g)
check("C5 1/4 - g^2 = g for g = (sqrt2-1)/2, so the two TVs cannot both be < g", sp.simplify(sp.Rational(1, 4) - g ** 2 - g) == 0)
check("C5 attained: p = 1/sqrt2, q = 1 gives both TVs equal to g",
      sp.simplify(sp.Abs(1 / sp.sqrt(2) - sp.Rational(1, 2)) - g) == 0
      and sp.simplify(tv2.subs({p_: 1 / sp.sqrt(2), q_: 1}) - g) == 0)
Hc = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
r1 = Hc * sp.diag(1, 0) * Hc.T
r2 = Hc * r1 * Hc.T
check("C5 countercontrol: the coherent Hadamard gives exactly 1/2 and 1 (gap 0)",
      sp.simplify(r1[0, 0]) == sp.Rational(1, 2) and sp.simplify(r2[0, 0]) == 1)

print("RESULT", "ALL PASS" if not FAIL else "FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
