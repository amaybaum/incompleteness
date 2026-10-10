"""POS-SEP core: exact (Fraction) model of DIM-1's carrier W d, mirroring the Lean definitions at L.

Lean references (wt-L/verification/lean-mathlib/OIBridge/CompositeDimension.lean):
  hom (l.100), homMap (l.112), prodState (l.161), pairVal (l.164), actT (l.198), actC (l.201),
  corner (l.205), IsNot (l.210), NativeGate (l.218), Lor (l.869), cornerMap (l.1797).
EffectSpace.lean: sharpVec (l.57).  ParityNot.lean: diagSign (l.292), sgate (l.428), odd5/perm5/n5/z5/x5/w5.
OddChar.lean: oddK (l.37), nK (l.56), zK (l.59).

A joint vector omega in W d is a (d+1)x(d+1) list of Fractions, omega[mu][nu]
(mu = control index, nu = target index), exactly as `W d := Fin (d+1) -> Fin (d+1) -> R`.
"""
from fractions import Fraction as Fr
import itertools

ZERO, ONE = Fr(0), Fr(1)


def zeros(n):
    return [[ZERO] * n for _ in range(n)]


def hom(x):
    return [ONE] + [Fr(v) for v in x]


def prod_state(x, y):
    hx, hy = hom(x), hom(y)
    return [[a * b for b in hy] for a in hx]


def tens(X, Y):
    return [[a * b for b in Y] for a in X]


def pair_val(a, b, om):
    return sum(a[m] * om[m][n] * b[n] for m in range(len(a)) for n in range(len(b)))


def sharp_vec(b):
    return [Fr(1, 2)] + [Fr(v) / 2 for v in b]


def corner(z, a):
    return list(z) if a == 0 else [-v for v in z]


# ---- a diagonal NOT (diagSign), its homogenized action as a sign vector on Fin (d+1) ----

def hom_signs(c):
    """homMap (diagSign c) v mu = vecCons 1 c mu * v mu (ParityNot.homMap_diagSign)."""
    return [ONE] + [Fr(v) for v in c]


def actT(s, om):
    """actT N om mu = homMap N (om mu): N on the target index."""
    n = len(s)
    return [[s[nu] * om[mu][nu] for nu in range(n)] for mu in range(n)]


def actC(s, om):
    """actC N om mu nu = homMap N (fun k => om k nu) mu: N on the control index."""
    n = len(s)
    return [[s[mu] * om[mu][nu] for nu in range(n)] for mu in range(n)]


def eq(om1, om2):
    return all(om1[i][j] == om2[i][j] for i in range(len(om1)) for j in range(len(om1)))


def basis(n):
    for m, v in itertools.product(range(n), range(n)):
        om = zeros(n)
        om[m][v] = ONE
        yield om


# ---- linear maps of W d as matrices on the flattened index (mu, nu) -> mu*n + nu ----

def to_vec(om):
    return [om[m][v] for m in range(len(om)) for v in range(len(om))]


def from_vec(vec, n):
    return [[vec[m * n + v] for v in range(n)] for m in range(n)]


def matrix_of(f, n):
    cols = [to_vec(f(om)) for om in basis(n)]
    N = n * n
    return [[cols[j][i] for j in range(N)] for i in range(N)]


def mat_apply(M, om):
    n = len(om)
    v = to_vec(om)
    return from_vec([sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(v))], n)


def mat_inverse(M):
    """Exact Gauss-Jordan inverse; raises if singular."""
    N = len(M)
    A = [list(row) + [ONE if i == j else ZERO for j in range(N)] for i, row in enumerate(M)]
    for col in range(N):
        piv = next((r for r in range(col, N) if A[r][col] != 0), None)
        if piv is None:
            raise ValueError("singular")
        A[col], A[piv] = A[piv], A[col]
        p = A[col][col]
        A[col] = [v / p for v in A[col]]
        for r in range(N):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [vr - f * vc for vr, vc in zip(A[r], A[col])]
    return [row[N:] for row in A]


def rank(M):
    A = [list(r) for r in M]
    rows, cols = len(A), len(A[0])
    rk = 0
    for c in range(cols):
        piv = next((r for r in range(rk, rows) if A[r][c] != 0), None)
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        for r in range(rows):
            if r != rk and A[r][c] != 0:
                f = A[r][c] / A[rk][c]
                A[r] = [vr - f * vc for vr, vc in zip(A[r], A[rk])]
        rk += 1
    return rk


# ---- exact PSD test (symmetric elimination with positive pivots) ----

def is_psd(Q):
    A = [list(r) for r in Q]
    n = len(A)
    idx = list(range(n))
    while idx:
        diag = [(A[i][i], i) for i in idx]
        if any(v < 0 for v, _ in diag):
            return False
        pos = [i for v, i in diag if v > 0]
        if not pos:
            return all(A[i][j] == 0 for i in idx for j in idx)
        p = pos[0]
        for i in idx:
            if i == p:
                continue
            f = A[i][p] / A[p][p]
            if f != 0:
                for j in idx:
                    A[i][j] -= f * A[p][j]
        idx.remove(p)
    return True


def in_lor_exact(v):
    """Lor v :  0 <= v 0  and  sum tail^2 <= v0^2."""
    return v[0] >= 0 and sum(t * t for t in v[1:]) <= v[0] * v[0]


def maxcone_certificate(om, mu):
    """Sufficient certificate that om in maxCone(eball d):
    for a = (1, alpha), |alpha| <= 1, the vector L = om^T a must lie in Lor.
    (i)  L_0 is affine in alpha with L_0(0) = om[0][0]... min over the ball >= 0, checked exactly
         as  L0(0) >= 0  and  L0(0)^2 >= |grad L0|^2;
    (ii) f(alpha) = L^T J L = h^T (om J om^T) h with h = (1, alpha) is >= 0 on the ball, certified by
         the S-lemma multiplier mu >= 0:  om J om^T - mu J  PSD  (then f(h) >= mu h^T J h >= 0).
    Every effect has ehom in Lor (lor_ehom), so (i)+(ii) give om in maxCone."""
    n = len(om)
    L00 = om[0][0]
    grad = [om[m][0] for m in range(1, n)]
    ok_i = L00 >= 0 and L00 * L00 >= sum(g * g for g in grad)
    J = [ONE] + [-ONE] * (n - 1)
    Q = [[sum(om[i][k] * J[k] * om[j][k] for k in range(n)) - (mu * J[i] if i == j else ZERO)
          for j in range(n)] for i in range(n)]
    return ok_i and mu >= 0 and is_psd(Q)


# ---- rational points on the unit sphere (inverse stereographic projection) ----

def sphere_point(u):
    """u in Q^(d-1) -> unit vector in Q^d."""
    s = sum(Fr(t) ** 2 for t in u)
    return [2 * Fr(t) / (1 + s) for t in u] + [(s - 1) / (1 + s)]


def maxcone_certificate_algebraic(om):
    """Exact certificate at tight points, where the S-lemma multiplier is an algebraic number.

    Condition (i) as in maxcone_certificate.  For (ii): the multipliers mu with  Q - mu J  PSD
    (Q = om J om^T) form an interval; when no rational mu works, a feasible mu* is a real root of
    det(Q - mu J).  For each nonnegative real root mu* of each irreducible factor f of that
    determinant, every principal minor m_S(mu) of Q - mu J is tested at mu* exactly: if f | m_S the
    minor vanishes at mu*; otherwise f and m_S share no root, the rational isolating interval of mu*
    is refined until m_S has no root in it, and the sign of m_S at mu* is read at the interval's
    midpoint.  PSD <=> every principal minor >= 0.  All arithmetic is exact (sympy over Q)."""
    import sympy as sp
    from itertools import combinations
    n = len(om)
    L00 = om[0][0]
    grad = [om[m][0] for m in range(1, n)]
    if not (L00 >= 0 and L00 * L00 >= sum(g * g for g in grad)):
        return False
    R = lambda f: sp.Rational(f.numerator, f.denominator)
    J = [1] + [-1] * (n - 1)
    mu = sp.Symbol("mu")
    Qm = sp.Matrix(n, n, lambda i, j: sum(R(om[i][k]) * J[k] * R(om[j][k]) for k in range(n))
                   - (mu * J[i] if i == j else 0))
    minors = []
    for r in range(1, n + 1):
        for S in combinations(range(n), r):
            minors.append(sp.Poly(sp.expand(Qm.extract(list(S), list(S)).det()), mu, domain="QQ"))
    det = minors[-1]
    if det.is_zero:
        return False
    _, facs = sp.factor_list(det.as_expr(), mu)
    for f, _m in facs:
        fp = sp.Poly(f, mu, domain="QQ")
        if fp.degree() < 1:
            continue
        for (a, b), _mult in fp.intervals():
            a, b = sp.Rational(a), sp.Rational(b)
            if b < 0:
                continue
            # the isolated root mu* must be >= 0
            if a < 0 and fp.eval(0) != 0 and fp.count_roots(a, 0) > 0:
                continue
            ok = True
            for m in minors:
                if m.is_zero:
                    continue
                rem = m.rem(fp)
                if rem.is_zero:
                    continue
                lo, hi = a, b
                while rem.count_roots(lo, hi) > 0:
                    lo, hi = fp.refine_root(lo, hi, eps=(hi - lo) / 16)
                    lo, hi = sp.Rational(lo), sp.Rational(hi)
                if rem.eval((lo + hi) / 2) < 0:
                    ok = False
                    break
            if ok:
                return True
    return False
