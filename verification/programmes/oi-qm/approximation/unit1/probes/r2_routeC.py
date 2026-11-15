#!/usr/bin/env python3
"""r2 labelled exact generic checks for #1216 unit 1, route C and the outcome table (findings B1,
B3, N4).  Imports nothing from earlier probes.  Generic symbolic matrices only; no OI mechanism.

CM  the column-monomial class: matrices with at most one nonzero entry in each column.
C1  CM is closed under the five fields of the kernel's `Architecture` (ImplementationLocality.lean:
    506-515): identity, product, scalar multiple, ancilla projectors diag(r.2 = k), and ancilla
    blocks ancBlock K f e (s, t) = K((s, f), (t, e)) (AncillaClosure.lean:457).  Symbolic, on every
    zero pattern: 3x3 products (64^2 pattern pairs), 4x4 = S x Fin 2 blocks (625 patterns).
C2  every CM conjugation K diag(w) K^dag of a symbolic diagonal is diagonal (64 patterns, n = 3);
    countercontrol: the Hadamard is not CM and its conjugation of |0><0| is not diagonal.
C3  K = |0>(<0| + <1|)/sqrt2 is CM, not monomial (row 0 has two nonzeros; `IsMonomial` =
    permMatrix * diagonal, SubstratumInterface.lean:75), with K^dag K <= I; a CM matrix with
    K^dag K = I has a permutation pattern (n = 2, 3), so CM's isometries are monomial.
C4  gate flow at t = 1/2 for the swap of two configurations: entries (1+i)/2 and (1-i)/2
    (the statement of `gateFlow_half_entries`), unitary, and conj(|0><0|) has off-diagonal i/2.
C5  law-level witness (N4): for every stochastic map T on two configurations, used for "H",
    max(TV on (|0>, H, Z-read), TV on (|0>, H, H, Z-read)) >= g = (sqrt2 - 1)/2; attained at
    T(0|0) = 1/sqrt2, T(0|1) = 1; countercontrol: the coherent Hadamard gives 1/2 and 1 (gap 0).
C6  coverage witness (B1): for x+ (x) z+ and y+ (x) z+, tr((rho - D) W) = 1 for every diagonal D
    (W = X(x)Z, Y(x)Z, ||W||_op = 1), so TD >= 1/2; attained at D = diag(rho).  Compatibility
    control: a diagonal unit-trace D with nonnegative entries is a quantum state.
C7  QP node 10 values: Y(x)Y = -(X(x)X)(Z(x)Z); the joint +1 eigenspace of XX and ZZ is spanned by
    Phi+, so every state with <XX> = <ZZ> = 1 has <YY> = -1.
Run: python3 -I -B r2_routeC.py   (exit 0 iff every check passes)
"""
import itertools
import sys

import sympy as sp

FAILS = []


def check(label, cond):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        FAILS.append(label)


def is_zero(M):
    return all(sp.expand(x) == 0 for x in M)


def is_cm(M):
    return all(sum(1 for i in range(M.rows) if sp.expand(M[i, j]) != 0) <= 1 for j in range(M.cols))


def cm_patterns(n):
    """Every column-monomial zero pattern of an n x n matrix: per column, a row index or None."""
    return list(itertools.product([None] + list(range(n)), repeat=n))


def cm_matrix(pattern, n, tag):
    return sp.Matrix(n, n, lambda i, j: sp.Symbol(f"{tag}{i}{j}", nonzero=True) if pattern[j] == i else 0)


# C1 -------------------------------------------------------------------------------------------
n = 3
pats3 = cm_patterns(n)
check("C1 identity is CM; scalar multiple of a CM matrix is CM",
      is_cm(sp.eye(n)) and all(is_cm(sp.Symbol('a') * cm_matrix(p, n, 'k')) for p in pats3))
ok = all(is_cm(cm_matrix(p, n, 'k') * cm_matrix(q, n, 'l')) for p in pats3 for q in pats3)
check(f"C1 product of two symbolic CM matrices is CM ({len(pats3)}^2 pattern pairs, n = 3)", ok)
# ancilla projectors on S x Fin m, S = Fin 2, m = 2: diagonal 0/1
m = 2
idx = [(s, r) for s in range(2) for r in range(m)]
projs = [sp.diag(*[1 if r == k else 0 for (_, r) in idx]) for k in range(m)]
check("C1 ancilla projectors diag(r.2 = k) on S x Fin 2 are CM", all(is_cm(P) for P in projs))
pats4 = cm_patterns(4)
ok = True
for p in pats4:
    K = cm_matrix(p, 4, 'k')
    for f in range(m):
        for e in range(m):
            B = sp.Matrix(2, 2, lambda s, t: K[idx.index((s, f)), idx.index((t, e))])
            if not is_cm(B):
                ok = False
check(f"C1 every ancilla block (f, e) of every symbolic CM matrix on S x Fin 2 is CM ({len(pats4)} patterns)", ok)

# C2 -------------------------------------------------------------------------------------------
w = sp.symbols('w0:3')
Dw = sp.diag(*w)


def offdiag_zero(M):
    return all(sp.expand(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols) if i != j)


ok = all(offdiag_zero(cm_matrix(p, n, 'k') * Dw * cm_matrix(p, n, 'k').H) for p in pats3)
check("C2 conjugation by every symbolic 3x3 CM matrix maps a symbolic diagonal to a diagonal", ok)
Hd = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
check("C2 countercontrol: the Hadamard is not CM and H|0><0|H is not diagonal",
      (not is_cm(Hd)) and not offdiag_zero(Hd * sp.diag(1, 0) * Hd.H))

# C3 -------------------------------------------------------------------------------------------
K = sp.Matrix([[1, 1], [0, 0]]) / sp.sqrt(2)


def is_monomial_pattern(M):
    rows_ok = all(sum(1 for j in range(M.cols) if sp.expand(M[i, j]) != 0) <= 1 for i in range(M.rows))
    return rows_ok and is_cm(M)


KdK = sp.simplify(K.H * K)
check("C3 K = |0>(<0|+<1|)/sqrt2 is CM and not monomial; K^dag K has eigenvalues {0, 1}",
      is_cm(K) and not is_monomial_pattern(K) and sorted(KdK.eigenvals().keys()) == [0, 1])
ok = True
for nn in (2, 3):
    for p in cm_patterns(nn):
        M = cm_matrix(p, nn, 'u')
        G = (M.H * M)
        # orthonormal columns need every column nonzero and every off-diagonal Gram entry zero
        cols_nonzero = all(r is not None for r in p)
        offd = [sp.expand(G[i, j]) for i in range(nn) for j in range(nn) if i != j]
        can_be_isometry = cols_nonzero and all(x == 0 for x in offd)
        if can_be_isometry and not is_monomial_pattern(M):
            ok = False
check("C3 a CM matrix with K^dag K = I has a permutation pattern (n = 2, 3): CM isometries are monomial", ok)

# C4 -------------------------------------------------------------------------------------------
Psw = sp.Matrix([[0, 1], [1, 0]])
Ghalf = (1 + sp.I) / 2 * sp.eye(2) + (1 - sp.I) / 2 * Psw
check("C4 gate flow at t = 1/2 (swap): unitary, entries (1+i)/2 diagonal and (1-i)/2 off-diagonal",
      is_zero(sp.simplify(Ghalf.H * Ghalf) - sp.eye(2)) and sp.simplify(Ghalf[0, 0] - (1 + sp.I) / 2) == 0)
img = sp.simplify(Ghalf * sp.diag(1, 0) * Ghalf.H)
check("C4 its conjugation of |0><0| has off-diagonal entry i/2 (does not preserve diagonals)",
      sp.simplify(img[0, 1] - sp.I / 2) == 0)

# C5 -------------------------------------------------------------------------------------------
p, q = sp.symbols('p q', real=True)
g = (sp.sqrt(2) - 1) / 2
P1 = p                       # P(0) after one application, start 0
P2 = p * p + q * (1 - p)     # P(0) after two applications
TV2 = 1 - P2                 # target P(0) = 1 (H H = I)
check("C5 TV2 - p(1-p) = (1-q)(1-p) >= 0 on [0,1]^2", sp.expand(TV2 - p * (1 - p) - (1 - q) * (1 - p)) == 0)
check("C5 g solves g = 1/4 - g^2, so p(1-p) >= g whenever |p - 1/2| <= g",
      sp.simplify(sp.Rational(1, 4) - g ** 2 - g) == 0)
check("C5 attained: p = 1/sqrt2, q = 1 gives TV1 = TV2 = g",
      sp.simplify(sp.Abs(P1 - sp.Rational(1, 2)).subs(p, 1 / sp.sqrt(2)) - g) == 0
      and sp.simplify(TV2.subs({p: 1 / sp.sqrt(2), q: 1}) - g) == 0)
# exhaustive rational grid as an independent countercheck of the minimax value
grid = [sp.Rational(i, 40) for i in range(41)]
best = min(max(abs(a - sp.Rational(1, 2)), 1 - a * a - b * (1 - a)) for a in grid for b in grid)
check("C5 rational-grid control: no grid map beats g (minimum of the max over a 41x41 grid >= g)",
      sp.simplify(best - g) >= 0)
v0 = sp.Matrix([1, 0])
out1 = Hd * v0
out2 = Hd * Hd * v0
check("C5 countercontrol: the coherent Hadamard gives P(0) = 1/2 and 1 exactly (gap 0)",
      sp.simplify(abs(out1[0]) ** 2) == sp.Rational(1, 2) and sp.simplify(abs(out2[0]) ** 2) == 1)

# C6 -------------------------------------------------------------------------------------------
kp = sp.kronecker_product
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Zm = sp.diag(1, -1); I2 = sp.eye(2)
xp = sp.Matrix([1, 1]) / sp.sqrt(2); yp = sp.Matrix([1, sp.I]) / sp.sqrt(2); zp = sp.Matrix([1, 0])
d = sp.symbols('d0:4')
Dsym = sp.diag(*d)
for name, a, W in (("x+ (x) z+", xp, kp(X, Zm)), ("y+ (x) z+", yp, kp(Y, Zm))):
    psi = kp(a, zp)
    rho = psi * psi.H
    val = sp.expand(((rho - Dsym) * W).trace())
    opn = max(abs(e) for e in W.eigenvals())
    check(f"C6 {name}: tr((rho - D) W) = 1 for every symbolic diagonal D, ||W||_op = 1, so TD >= 1/2",
          sp.simplify(val - 1) == 0 and opn == 1)
    diffm = rho - sp.diag(*[rho[i, i] for i in range(4)])
    tn = sum(abs(sp.simplify(e)) * mult for e, mult in diffm.eigenvals().items())
    check(f"C6 {name}: attained, ||rho - diag(rho)||_1 = 1 (TD = 1/2)", sp.simplify(tn - 1) == 0)
check("C6 compatibility control: a diagonal unit-trace matrix with nonnegative entries is PSD (a quantum state)",
      all(e >= 0 for e in sp.diag(sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6), 0).eigenvals()))

# C7 -------------------------------------------------------------------------------------------
XX, YY, ZZ = kp(X, X), kp(Y, Y), kp(Zm, Zm)
check("C7 operator identity Y(x)Y = -(X(x)X)(Z(x)Z)", is_zero(YY + XX * ZZ))
Pj = (sp.eye(4) + XX) * (sp.eye(4) + ZZ) / 4
phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
check("C7 the joint +1 eigenprojector of XX and ZZ is |Phi+><Phi+| (rank one)",
      is_zero(sp.simplify(Pj - phi * phi.H)))
check("C7 hence <YY> = -1 on every state with <XX> = <ZZ> = 1; a table with <YY> = 0 has no quantum completion",
      sp.simplify((phi * phi.H * YY).trace()) == -1)
check("C7 countercontrol: Phi- = (|00> - |11>)/sqrt2 has <XX> = -1 (excluded by <XX> = 1)",
      sp.simplify((lambda v: (v * v.H * XX).trace())(sp.Matrix([1, 0, 0, -1]) / sp.sqrt(2))) == -1)

print("RESULT " + ("ALL PASS" if not FAILS else f"{len(FAILS)} FAIL"))
sys.exit(1 if FAILS else 0)
