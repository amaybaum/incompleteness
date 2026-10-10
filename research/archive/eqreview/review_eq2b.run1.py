"""Independent check of EQ2-B's N-CLASS (coordinator review; research only, base bcbc516f).

Written without importing eq2b_lib or any EQ2-B script. Conventions are read from the kernel:
  W 3 tables om[mu][nu] (mu control, nu target, index 0 = unit); prodState x y = hom x (x) hom y;
  actC N om = Nh . om, actT N om = om . Nh^T (Nh = 1 (+) N); pairVal a b om = a^T om b;
  maxCone(eball 3) = {om : u^T om v >= 0 for all u, v in the Lorentz cone};
  kernel cnot: cnotFun om mu nu = sgn mu nu * om (pc mu nu) (pt mu nu)  (CompositeDimension.lean:741-781, typed in here).
Normalized setting (EQ2-B's reduction, re-derived by hand in the review): z = z3, N = nflip, Mfwd = id, so
  Gt(C+ (x) Y) = C+ (x) Y,  Gt(C- (x) Y) = C- (x) Nh Y  (C+- = hom(+-z3)),  and the tangent block Gt(lift e_c (x) Y) is unknown.

Decision rules, fixed before the run (rules, not expected numbers):
  K   the typed-in kernel cnot is an involution and equals the hand-derived closed form F(1, 1, -1, 1).
  N1  with the 128 tangent-block entries unknown, the exact rank of C1 (relC) + C2 (corner orthogonality) + C3/C4
      (first-order tightness at x = +-z3 for 24 rational unit y) equals 124, and the 4-dim null space equals the
      span of the closed-form directions dF/da, dF/da', dF/db, dF/db'.
  N2  the closed form satisfies C1, C2 exactly and C3, C4 as polynomial identities modulo |y|^2 = 1.
  N3  countercontrols: dropping C3 + C4 leaves a strictly larger null space, and so does dropping C1.
  P1  F's inverse is F(1/a, 1/a', -1/b', -1/b) exactly (symbolic).
  P2  each of a, a', b, b' at 3/2 (others at their cnot values) violates posFwd at an exact point.
  P3  of the 16 sign patterns, those with a b + a' b' != 0 have an exact posFwd violation; those with a b + a' b' = 0
      are each an exact product actC D1 . actT D2 . cnot . actC D3 . actT D4 with Di diagonal sign matrices.
  V   the review verdict prints only if every check passes.
"""
import sys
import itertools
from fractions import Fraction as Fr
import sympy as sp

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


# ---------- the kernel cnot, typed in from CompositeDimension.lean:741-781 ----------
def sgn(m, n):
    return -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def idx(m, n):
    return 4 * m + n


CNOT = sp.zeros(16, 16)
for m in range(4):
    for n in range(4):
        CNOT[idx(m, n), idx(PC[m][n], PT[m][n])] = sgn(m, n)

# ---------- linear maps on W 3 as 16 x 16 matrices on vec(om) ----------


def hommat(A):
    H = sp.eye(4)
    H[1:, 1:] = sp.Matrix(A)
    return H


def actC(A):
    Hm = hommat(A)
    M = sp.zeros(16, 16)
    for m in range(4):
        for n in range(4):
            for k in range(4):
                M[idx(m, n), idx(k, n)] += Hm[m, k]
    return M


def actT(A):
    Hm = hommat(A)
    M = sp.zeros(16, 16)
    for m in range(4):
        for n in range(4):
            for k in range(4):
                M[idx(m, n), idx(m, k)] += Hm[n, k]
    return M


def tens(X, Y):
    return sp.Matrix([X[m] * Y[n] for m in range(4) for n in range(4)])


def hom(x):
    return sp.Matrix([1] + list(x))


NFLIP = sp.diag(1, -1, -1)
Nh = hommat(NFLIP)
Cp, Cm = sp.Matrix([1, 0, 0, 1]), sp.Matrix([1, 0, 0, -1])
ex, ey = sp.Matrix([0, 1, 0, 0]), sp.Matrix([0, 0, 1, 0])
E = [sp.Matrix([1 if i == l else 0 for i in range(4)]) for l in range(4)]
S = sp.zeros(4, 4)
S[0, 1] = S[1, 0] = 1
J = sp.zeros(4, 4)
J[2, 3], J[3, 2] = 1, -1


def from_slices(f):
    """Assemble the 16 x 16 matrix of the linear map whose value on control basis vector c (x) e_l is f(c, l).
    Control basis: C+, C-, ex, ey (a basis of HVec 3); inputs are re-expressed in it."""
    basis = [Cp, Cm, ex, ey]
    Bc = sp.Matrix.hstack(*basis)            # columns = control basis
    cols = []
    images = {}
    for ci in range(4):
        for l in range(4):
            images[(ci, l)] = f(ci, l)
    Binv = Bc.inv()
    M = sp.zeros(16, 16)
    for m in range(4):                        # standard control basis vector e_m = sum_ci Binv[ci, m] basis[ci]
        for l in range(4):
            col = sp.zeros(16, 1)
            for ci in range(4):
                if Binv[ci, m] != 0:
                    col += Binv[ci, m] * images[(ci, l)]
            M[:, idx(m, l)] = col
    return M


def F_closed(a, a2, b, b2):
    def f(ci, l):
        Y = E[l]
        if ci == 0:
            return tens(Cp, Y)
        if ci == 1:
            return tens(Cm, Nh * Y)
        if ci == 2:
            return tens(ex, a * S * Y) + tens(ey, b * J * Y)
        return tens(ex, b2 * J * Y) + tens(ey, a2 * S * Y)
    return from_slices(f)


a, a2, b, b2 = sp.symbols("a a2 b b2")
Fsym = F_closed(a, a2, b, b2)

# K: kernel control
check("K kernel cnot (typed in) is an involution", CNOT * CNOT == sp.eye(16))
check("K kernel cnot == closed form F(1, 1, -1, 1)", F_closed(1, 1, -1, 1) == CNOT)

# ---------- N1: independent null-space computation over 128 unknowns ----------
U = sp.symbols("u0:128")                      # tangent block: (c in {x, y}) x (l in 0..3) x (16 outputs)


def G_unknown():
    def f(ci, l):
        Y = E[l]
        if ci == 0:
            return tens(Cp, Y)
        if ci == 1:
            return tens(Cm, Nh * Y)
        c = ci - 2
        return sp.Matrix([U[(c * 4 + l) * 16 + k] for k in range(16)])
    return from_slices(f)


Gu = G_unknown()
AC, AT = actC(NFLIP), actT(NFLIP)
rows_C1 = list(AC * Gu * AC - AT * Gu)          # relC as 256 linear forms (many trivial)
rows_C2 = []
for c, cv in ((0, ex), (1, ey)):
    for l in range(4):
        out = Gu * tens(cv, E[l])
        for Cv in (Cp, Cm):
            for n in range(4):
                rows_C2.append(sum(Cv[m] * out[idx(m, n)] for m in range(4)))


def sphere_pt(s, t):
    q = s * s + t * t + 1
    return [Fr(2 * s, 1) / q, Fr(2 * t, 1) / q, Fr(s * s + t * t - 1, 1) / q]


targets = [(Fr(p), Fr(q)) for p, q in [(0, 0), (1, 0), (0, 1), (2, 0), (0, 3), (1, 1), (Fr(1, 2), 2), (3, -1),
                                        (-1, 2), (Fr(2, 3), Fr(-1, 4)), (5, 1), (-2, -3), (Fr(1, 3), Fr(1, 5)),
                                        (4, -2), (-1, -1), (Fr(3, 2), Fr(5, 2)), (7, 0), (0, -5), (Fr(-1, 7), 3),
                                        (2, 2), (-3, 1), (Fr(5, 3), Fr(-2, 3)), (1, 4), (-4, Fr(1, 2))]]
rows_C34 = []
for (s, t) in targets:
    y = sphere_pt(s, t)
    yv = sp.Matrix([sp.Rational(v.numerator, v.denominator) for v in y])
    Y = hom(yv)
    for c, cv in ((0, ex), (1, ey)):
        out = Gu * tens(cv, Y)
        for w in (hom(-yv), hom(-(NFLIP * yv))):
            for m in range(4):
                rows_C34.append(sum(out[idx(m, n)] * w[n] for n in range(4)))


def to_matrix(forms):
    rows = []
    for e in forms:
        e = sp.expand(e)
        if e == 0:
            continue
        coeffs = [Fr(0)] * 128
        const = e.subs({u: 0 for u in U})
        for i, u in enumerate(U):
            cf = e.coeff(u)
            if cf != 0:
                coeffs[i] = Fr(int(sp.fraction(cf)[0]), int(sp.fraction(cf)[1]))
        rows.append((coeffs, const))
    return rows


def rank_and_null(rows, ncols=128):
    """Exact Gaussian elimination over Q on homogeneous rows; returns rank and a null-space basis."""
    M = [list(r) for r in rows]
    piv_cols = []
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = 1 / M[r][c]
        M[r] = [v * inv for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [vi - f * vr for vi, vr in zip(M[i], M[r])]
        piv_cols.append(c)
        r += 1
        if r == len(M):
            break
    free = [c for c in range(ncols) if c not in piv_cols]
    null = []
    for fc in free:
        v = [Fr(0)] * ncols
        v[fc] = Fr(1)
        for i, pc in enumerate(piv_cols):
            v[pc] = -M[i][fc]
        null.append(v)
    return r, null


R1, R2, R34 = to_matrix(rows_C1), to_matrix(rows_C2), to_matrix(rows_C34)
check("N1 all constraint rows are homogeneous in the unknowns (corner slices consistent)",
      all(c == 0 for _, c in R1 + R2 + R34))
full = [r for r, _ in R1 + R2 + R34]
rk, null = rank_and_null(full)
check(f"N1 exact rank of C1 + C2 + C3/C4 (24 sphere points) = {rk} = 124 (null dim {len(null)})", rk == 124 and len(null) == 4)


def tangent_vec(Gm):
    v = []
    for c, cv in ((0, ex), (1, ey)):
        for l in range(4):
            out = Gm * tens(cv, E[l])
            v.extend(out[k] for k in range(16))
    return v


dirs = []
for sym in (a, a2, b, b2):
    Gd = Fsym.diff(sym)
    dv = tangent_vec(Gd)
    dirs.append([Fr(int(sp.fraction(x)[0]), int(sp.fraction(x)[1])) for x in dv])
# null-space membership and equality of spans
in_null = all(sum(rw[i] * d[i] for i in range(128)) == 0 for d in dirs for rw in full)
rk_dirs, _ = rank_and_null(dirs)
rk_both, _ = rank_and_null(dirs + null)
check("N1 the closed-form directions dF/da, dF/da', dF/db, dF/db' lie in the null space", in_null)
check(f"N1 they span it: rank(dirs) = {rk_dirs}, rank(dirs + null) = {rk_both}", rk_dirs == 4 and rk_both == 4)
check("N1 the closed form is affine in (a, a', b, b'): F = F(0) + a dF/da + ...",
      sp.expand(Fsym - F_closed(0, 0, 0, 0) - sum(sym * Fsym.diff(sym) for sym in (a, a2, b, b2))) == sp.zeros(16, 16))

# ---------- N2: the closed form satisfies the constraints exactly, C3/C4 for all unit y ----------
check("N2 closed form satisfies relC exactly (symbolic)", sp.expand(AC * Fsym * AC - AT * Fsym) == sp.zeros(16, 16))
ok_c2 = True
for cv in (ex, ey):
    for l in range(4):
        out = Fsym * tens(cv, E[l])
        for Cv in (Cp, Cm):
            for n in range(4):
                if sp.expand(sum(Cv[m] * out[idx(m, n)] for m in range(4))) != 0:
                    ok_c2 = False
check("N2 closed form: tangent control output orthogonal to both corners (symbolic)", ok_c2)
y1, y2, y3 = sp.symbols("y1 y2 y3")
yv = sp.Matrix([y1, y2, y3])
ok_c34 = True
for cv in (ex, ey):
    out = Fsym * tens(cv, hom(yv))
    for w in (hom(-yv), hom(-(NFLIP * yv))):
        for m in range(4):
            poly = sp.expand(sum(out[idx(m, n)] * w[n] for n in range(4)))
            red = sp.expand(poly.subs(y3**2, 1 - y1**2 - y2**2))
            if red != 0:
                ok_c34 = False
check("N2 closed form: C3 and C4 hold as polynomial identities modulo |y|^2 = 1", ok_c34)
ok_corner = (Fsym * tens(Cp, hom(yv)) == tens(Cp, hom(yv))) and \
    (sp.expand(Fsym * tens(Cm, hom(yv)) - tens(Cm, Nh * hom(yv))) == sp.zeros(16, 1))
check("N2 closed form: corner slices are the identity and I (x) N (frame: z3 (x) +-z3 fixed / flipped)", ok_corner)
check("N2 closed form preserves u = om_00 (row 0 of the matrix is e_0)", Fsym[0, :] == sp.Matrix([[1] + [0] * 15]))

# ---------- N3: countercontrols ----------
rk_no34, null_no34 = rank_and_null([r for r, _ in R1 + R2])
rk_noC1, null_noC1 = rank_and_null([r for r, _ in R2 + R34])
check(f"N3 countercontrol: without C3 + C4 the null space has dim {len(null_no34)} > 4", len(null_no34) > 4)
check(f"N3 countercontrol: without C1 the null space has dim {len(null_noC1)} > 4", len(null_noC1) > 4)

# ---------- P: positivity ----------
Finv_claim = F_closed(1 / a, 1 / a2, -1 / b2, -1 / b)
check("P1 F(a, a', b, b')^-1 == F(1/a, 1/a', -1/b', -1/b) (symbolic)",
      sp.simplify(Fsym * Finv_claim - sp.eye(16)) == sp.zeros(16, 16))


def val(G, x, y, al, be):
    om = G * tens(hom(sp.Matrix(x)), hom(sp.Matrix(y)))
    return sum(hom(sp.Matrix(al))[m] * om[idx(m, n)] * hom(sp.Matrix(be))[n] for m in range(4) for n in range(4))


h = sp.Rational(3, 2)
witnesses = {
    "a": (F_closed(h, 1, -1, 1), [1, 0, 0], [0, 0, 0], [-1, 0, 0], [1, 0, 0]),
    "a'": (F_closed(1, h, -1, 1), [0, 1, 0], [0, 0, 0], [0, -1, 0], [1, 0, 0]),
    "b": (F_closed(1, 1, h, 1), [1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]),
    "b'": (F_closed(1, 1, -1, h), [0, 1, 0], [0, 1, 0], [-1, 0, 0], [0, 0, 1]),
}
for nm, (G, x, y, al, be) in witnesses.items():
    v = val(G, x, y, al, be)
    check(f"P2 {nm} = 3/2: posFwd value {v} < 0 at x = {x}, y = {y}, effects {al}, {be}", v < 0)

# P3: the 16 sign patterns
signs = list(itertools.product((1, -1), repeat=4))
diags = [sp.diag(*d) for d in itertools.product((1, -1), repeat=3)]
local_cache = {}
for D1, D2 in itertools.product(range(8), repeat=2):
    local_cache[(D1, D2)] = actC(diags[D1]) * actT(diags[D2])
products = {}
for i, j in itertools.product(range(64), repeat=2):
    L1 = local_cache[divmod(i, 8)]
    L2 = local_cache[divmod(j, 8)]
    M = L1 * CNOT * L2
    key = tuple(M)
    if key not in products:
        products[key] = (divmod(i, 8), divmod(j, 8))


def search_witness(G):
    """Exact grid search for a posFwd violation: x, y, alpha, beta from a fixed rational grid inside the unit ball."""
    grid = [sp.Rational(p, 5) for p in (-4, -3, 0, 3, 4)]
    pts = []
    for v in itertools.product(grid, repeat=3):
        if sum(c * c for c in v) <= 1:
            pts.append(list(v))
    unit_like = [p for p in pts if sum(c * c for c in p) == 1] + [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]
    best = None
    for x in unit_like:
        for y in unit_like:
            om = G * tens(hom(sp.Matrix(x)), hom(sp.Matrix(y)))
            Om = sp.Matrix(4, 4, lambda m, n: om[idx(m, n)])
            for al in unit_like:
                row = hom(sp.Matrix(al)).T * Om
                for be in unit_like:
                    v = (row * hom(sp.Matrix(be)))[0, 0]
                    if v < 0 and (best is None or v < best[0]):
                        best = (v, x, y, al, be)
            if best is not None:
                return best
    return best


n_good, n_bad = 0, 0
for s in signs:
    G = F_closed(*s)
    cross = s[0] * s[2] + s[1] * s[3]
    if cross == 0:
        hit = products.get(tuple(G))
        ok = hit is not None
        n_good += ok
        check(f"P3 pattern {s} (a b + a' b' = 0) == actC D{hit[0][0] if hit else '?'} actT D{hit[0][1] if hit else '?'}"
              f" cnot actC D{hit[1][0] if hit else '?'} actT D{hit[1][1] if hit else '?'} (exact)", ok)
    else:
        w = search_witness(G)
        ok = w is not None and w[0] < 0
        n_bad += ok
        check(f"P3 pattern {s} (a b + a' b' = {cross}) violates posFwd: value {w[0] if w else None} at "
              f"x = {w[1] if w else None}, y = {w[2] if w else None}", ok)
check(f"P3 split: {n_good} patterns are local.cnot.local, {n_bad} violate posFwd", n_good == 8 and n_bad == 8)

npass = sum(1 for _, c in checks if c)
print(f"review_eq2b: {npass}/{len(checks)} checks pass")
if npass == len(checks):
    print("VERDICT N-CLASS-CONFIRMED: the normalized tangent block is the 4-parameter family; posFwd/posInv force"
          " +-1 with a b + a' b' = 0; the 8 survivors are sign-diagonal local . cnot . local")
else:
    print("VERDICT NOT RENDERED")
sys.exit(0 if npass == len(checks) else 1)
