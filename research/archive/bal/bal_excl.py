"""BAL, nodes B2-B4: exclusions under frame + relT + posFwd + posInv for a given NOT N (exact parts).

Written argument (LEDGER B2): with the REL-T normal form (Gt = G (I (x) M0^-1); corner maps I and S = 1 (+) sigma,
sigma orthogonal, sigma z = -z, sigma N = N sigma; tangent blocks L = [[0, a^T], [a, A]] in Lsig(sigma) and commuting
with homMap N), injectivity of the tangent block forces: no common kernel vector of all blocks, p_sigma = 1
(p_sigma >= 2 forces a = 0 by positivity; p_sigma = 0 forces a = 0 since a in Fix sigma), Fix sigma = span(u0) in Fix N.

Exact parts here:
  E0  the so(m) (x) so(3) lemma: block (i,j) of (sum_r P_r (x) E_r)(sum_s Q_s (x) E_s) is P_j Q_i - d_ij sum_r P_r Q_r
      (E_r = [e_r x]); hence no invertible element of so(m) (x) so(3) has its inverse there (written: P_i Q_i = -I/2 and
      P_j Q_i = 0 for i != j).  Groebner confirmation for m = 2, 3; positive controls so(2)(x)so(2), so(4)(x)so(2),
      so(2)(x)so(4), so(4)(x)so(4) contain inverse-closed invertible elements (J (x) J etc.).
  E1  d = 5, N = n5 (PARITY-NOT-1; balanced): every sigma = s+ (+) s- (+) (-1) commuting with n5, s+/s- running over
      I, -I, diag(1,-1), the symbolic reflection F(m) and the symbolic rotation R(m), is excluded: either the blocks
      Lsig(sigma) cap comm(homMap n5) have a common kernel vector, or p_sigma >= 2 and the blocks with a = 0 kill e0.
  E2  the positivity step for p_sigma >= 2: f^T L hom v = (1 - c)(a.v) - s(a.u + u.A v) identically (f = (1, -(c v + s u))).
  E3  the general lemmas at other d: p_N = 2 kills lift u1 (d = 7, (p,q) = (2,4)); a rotoreflection on V = Fix N - u0
      (dim 3) gives A|V = 0 (d = 9, (4,4)); a rotation in F cap z-perp with dim F = 3 gives A z = 0 (d = 7, (4,2));
      at d = 9, (4,4), sigma = 2 u0 u0^T - I: the blocks are a = alpha u0 and A in so(V) (+) so(F), dims 1 + 3 + 10.
  E4  controls: the same computation finds NO common kernel and p_sigma = 1 for (d, N, sigma) where a gate exists:
      (3, nflip, nflip), (5, nC5, nC5), (5, (3,1), 2e1e1^T - I), (7, N7b, 2e1e1^T - I); and for (5, n5, sigma = n5)
      the linear common kernel is 0 while p_sigma = 2 -- the positivity step, not linear algebra, excludes it.
"""
import sys
from sympy import (Matrix, Rational as R, eye, zeros, diag, symbols, expand, linsolve, cancel, together, groebner,
                   simplify, BlockDiagMatrix, sqrt)
from relt_common import homMap
from relt_lsig import Lsig_exact, Lsig_formula_ok, rot2

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


def kron(A, B):
    m, n = A.shape
    p, q = B.shape
    K = zeros(m * p, n * q)
    for i in range(m):
        for j in range(n):
            if A[i, j] != 0:
                K[i * p:(i + 1) * p, j * q:(j + 1) * q] = A[i, j] * B
    return K


def so_generic(m, tag):
    syms = symbols(f"{tag}0:{m * (m - 1) // 2}")
    P = zeros(m, m)
    k = 0
    for i in range(m):
        for j in range(i + 1, m):
            P[i, j] = syms[k]
            P[j, i] = -syms[k]
            k += 1
    return P, list(syms)


def cross(r):
    e = [0, 0, 0]
    e[r] = 1
    a, b, c = e
    return Matrix([[0, -c, b], [c, 0, -a], [-b, a, 0]])


# ------------------------------------------------------------------ E0 the so(m) (x) so(3) lemma
print("== E0 so(m) (x) so(3): no inverse-closed invertible element")
E = [cross(r) for r in range(3)]
ok = all((E[r] * E[s] - (Matrix([[1 if i == s else 0] for i in range(3)]) * Matrix([[1 if j == r else 0 for j in range(3)]])
          - (1 if r == s else 0) * eye(3))).is_zero_matrix for r in range(3) for s in range(3))
check("E0a [e_r x][e_s x] = e_s e_r^T - d_rs I for all r, s", ok)
for m in (2, 4):
    Ps = [so_generic(m, f"p{r}_")[0] for r in range(3)]
    Qs = [so_generic(m, f"q{r}_")[0] for r in range(3)]
    M = sum((kron(Ps[r], E[r]) for r in range(3)), zeros(3 * m, 3 * m))
    Mp = sum((kron(Qs[r], E[r]) for r in range(3)), zeros(3 * m, 3 * m))
    MM = M * Mp
    good = True
    tot = sum((Ps[r] * Qs[r] for r in range(3)), zeros(m, m))
    for i in range(3):
        for j in range(3):
            blk = Matrix(m, m, lambda a, b: MM[a * 3 + i, b * 3 + j])
            target = Qs[i] * 0 + Ps[j] * Qs[i] - (tot if i == j else zeros(m, m))
            good = good and (blk - target).applyfunc(expand).is_zero_matrix
    check(f"E0b m = {m}: block (i,j) of M M' = P_j Q_i - d_ij sum_r P_r Q_r (generic P_r, Q_s in so({m}))", good)
for m in (2, 3):
    Ps, Qs, unk = [], [], []
    for r in range(3):
        P, s1 = so_generic(m, f"p{r}_")
        Q, s2 = so_generic(m, f"q{r}_")
        Ps.append(P)
        Qs.append(Q)
        unk += s1 + s2
    M = sum((kron(Ps[r], E[r]) for r in range(3)), zeros(3 * m, 3 * m))
    Mp = sum((kron(Qs[r], E[r]) for r in range(3)), zeros(3 * m, 3 * m))
    eqs = [e for e in (M * Mp - eye(3 * m)) if e != 0]
    gb = groebner(eqs, *unk, order="grevlex")
    check(f"E0c m = {m}: Groebner basis of M M' = I over so({m}) (x) so(3) is [1] (no solution)", list(gb.exprs) == [1])


def inverse_closed_exists(m, n, A, B):
    """control: A in so(m), B in so(n) invertible with A^-1, B^-1 antisymmetric -> (A (x) B)^-1 in so (x) so"""
    M = kron(A, B)
    Mi = kron(A.inv(), B.inv())
    return (M * Mi - eye(m * n)).is_zero_matrix and (A.inv() + A.inv().T).is_zero_matrix and \
        (B.inv() + B.inv().T).is_zero_matrix


J2 = Matrix([[0, -1], [1, 0]])
K4 = Matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
check("E0d controls: so(2)(x)so(2), so(4)(x)so(2), so(2)(x)so(4), so(4)(x)so(4) contain inverse-closed invertible "
      "elements", inverse_closed_exists(2, 2, J2, J2) and inverse_closed_exists(4, 2, K4, J2)
      and inverse_closed_exists(2, 4, J2, K4) and inverse_closed_exists(4, 4, K4, K4))


# ------------------------------------------------------------------ the block-space machinery

def formula_space(sigma):
    """basis of {[[0,a^T],[a,A]] : sigma a = a, A^T = -A, sigma^T A = A sigma} (Lsig by A1), exact"""
    d = sigma.shape[0]
    av = symbols(f"a0:{d}")
    Av = symbols(f"A0:{d * d}")
    a = Matrix(av)
    A = Matrix(d, d, Av)
    cons = [expand(c) for c in list(sigma * a - a) + list(A + A.T) + list(sigma.T * A - A * sigma)]
    unk = list(av) + list(Av)
    rows = []
    for c in cons:
        num = cancel(together(c))
        rows.append([cancel(num.diff(u)) for u in unk])
    Mx = Matrix(rows) if rows else zeros(0, len(unk))
    ns = Mx.nullspace(iszerofunc=lambda x: cancel(x) == 0, simplify=cancel)
    basis = []
    for v in ns:
        v = v.applyfunc(cancel)
        a_ = Matrix(v[:d])
        A_ = Matrix(d, d, list(v[d:]))
        L = zeros(d + 1, d + 1)
        L[0, 1:] = a_.T
        L[1:, 0] = a_
        L[1:, 1:] = A_
        basis.append(L)
    return basis


def intersect_comm(basis, N):
    """basis of span(basis) cap {L : L homMap N = homMap N L}"""
    if not basis:
        return []
    Nh = homMap(N)
    cs = symbols(f"c0:{len(basis)}")
    M = zeros(*basis[0].shape)
    for c, B in zip(cs, basis):
        M += c * B
    cons = [cancel(together(e)) for e in (M * Nh - Nh * M) if cancel(together(e)) != 0]
    if not cons:
        return list(basis)
    rows = [[cancel(e.diff(c)) for c in cs] for e in cons]
    ns = Matrix(rows).nullspace(iszerofunc=lambda x: cancel(x) == 0, simplify=cancel)
    out = []
    for v in ns:
        L = zeros(*basis[0].shape)
        for c, B in zip(v, basis):
            L += cancel(c) * B
        out.append(L.applyfunc(cancel))
    return out


def common_kernel(basis, n):
    if not basis:
        return [Matrix([1 if i == k else 0 for i in range(n)]) for k in range(n)]
    St = Matrix.vstack(*basis)
    return St.nullspace(iszerofunc=lambda x: cancel(x) == 0, simplify=cancel)


def fix_dim(sigma):
    d = sigma.shape[0]
    return d - (sigma - eye(d)).rank(iszerofunc=lambda x: cancel(x) == 0, simplify=cancel)


def verdict(sigma, N, label, expect_excluded=True, cross_check=False):
    d = sigma.shape[0]
    n = d + 1
    assert (sigma.T * sigma - eye(d)).applyfunc(cancel).is_zero_matrix, label
    z = zeros(d, 1)
    z[d - 1] = 1
    assert (sigma * z + z).is_zero_matrix, label
    assert (sigma * N - N * sigma).applyfunc(cancel).is_zero_matrix, label
    B = formula_space(sigma)
    if cross_check:
        Bx = Lsig_exact(sigma)
        check(f"{label}: Lsig solver dim {len(Bx)} == formula-space dim {len(B)} and solver basis has the formula shape",
              len(Bx) == len(B) and Lsig_formula_ok(sigma, Bx))
    BN = intersect_comm(B, N)
    p = fix_dim(sigma)
    ker = common_kernel(BN, n)
    if p >= 2:
        B0 = [L for L in BN]  # impose a = 0: project out the a-part by solving
        cs = symbols(f"k0:{len(B0)}")
        M = zeros(n, n)
        for c, L in zip(cs, B0):
            M += c * L
        acons = [cancel(e) for e in M[1:, 0] if cancel(e) != 0]
        if acons:
            rows = [[cancel(e.diff(c)) for c in cs] for e in acons]
            ns = Matrix(rows).nullspace(iszerofunc=lambda x: cancel(x) == 0, simplify=cancel)
            B0 = []
            for v in ns:
                L = zeros(n, n)
                for c, Lb in zip(v, BN):
                    L += cancel(c) * Lb
                B0.append(L)
        ker0 = common_kernel(B0, n)
        e0 = Matrix([1] + [0] * d)
        e0_killed = all((L * e0).applyfunc(cancel).is_zero_matrix for L in B0)
        excluded = e0_killed
        how = f"p_sigma = {p} >= 2: positivity forces a = 0; then e0 is killed by every block ({len(ker0)}-dim common kernel)"
        lin = len(ker)
    else:
        excluded = len(ker) > 0
        how = f"p_sigma = {p}: common kernel of Lsig(sigma) cap comm(N) has dim {len(ker)}" + (
            "" if not ker else " (e.g. " + str(list(ker[0].T)) + ")")
        lin = len(ker)
    return excluded, how, lin, len(BN), p


def blk(*bs):
    return Matrix(BlockDiagMatrix(*bs))


m = symbols("m")
cm, sm = (1 - m ** 2) / (1 + m ** 2), 2 * m / (1 + m ** 2)
Fm = Matrix([[cm, sm], [sm, -cm]])
Rm = rot2(m)
types2 = [("I", eye(2)), ("-I", -eye(2)), ("diag(1,-1)", diag(1, -1)), ("F(m)", Fm), ("R(m)", Rm)]

# ------------------------------------------------------------------ E1 d = 5, n5
print("== E1 d = 5, N = n5 = diag(1,1,-1,-1,-1): every admissible sigma is excluded")
n5 = diag(1, 1, -1, -1, -1)
first = True
for nplus, sp in types2:
    for nminus, sq in types2:
        sigma = blk(sp, sq, Matrix([[-1]]))
        ex, how, lin, dimBN, p = verdict(sigma, n5, f"E1 s+={nplus} s-={nminus}", cross_check=first)
        first = False
        check(f"E1 sigma = {nplus} (+) {nminus} (+) (-1): EXCLUDED -- {how}", ex)

# ------------------------------------------------------------------ E2 the positivity step identity
print("== E2 the p_sigma >= 2 step")
d = 5
c, s = symbols("c s")
av = Matrix(symbols(f"a0:{d}"))
Asym, _ = so_generic(d, "w")
vv = Matrix(symbols(f"v0:{d}"))
uu = Matrix(symbols(f"u0:{d}"))
L = zeros(d + 1, d + 1)
L[0, 1:] = av.T
L[1:, 0] = av
L[1:, 1:] = Asym
f = Matrix([1] + list(-(c * vv + s * uu)))
homv = Matrix([1] + list(vv))
lhs = (f.T * L * homv)[0, 0]
rhs = (1 - c) * (av.T * vv)[0, 0] - s * ((av.T * uu)[0, 0] + (uu.T * Asym * vv)[0, 0])
check("E2 f^T L hom v = (1 - c)(a.v) - s (a.u + u.A v) for f = (1, -(c v + s u)), every a, antisymmetric A",
      expand(lhs - rhs) == 0)

# ------------------------------------------------------------------ E3 general lemmas at other d
print("== E3 the general lemmas")
# p_N = 2 at d = 7, (p, q) = (2, 4): sigma = 1 (+) (-1) on Fix N, then -I or a rotation on F cap z-perp
N724 = diag(1, 1, -1, -1, -1, -1, -1)
for name, sF in [("-I4", -eye(4)), ("R(m)(+)-I2", blk(Rm, -eye(2))), ("R(m)(+)R(m)", blk(Rm, Rm))]:
    sigma = blk(diag(1, -1), sF, Matrix([[-1]]))
    BN = intersect_comm(formula_space(sigma), N724)
    l2 = zeros(8, 1)
    l2[2] = 1
    check(f"E3a d = 7, (p,q) = (2,4), sigma on F cap z-perp = {name}: every block kills lift e2 (p_N = 2 lemma)",
          all((Lb * l2).applyfunc(cancel).is_zero_matrix for Lb in BN))
# rotoreflection on V (dim 3) at d = 9, (4,4): A|V = 0
N944 = diag(1, 1, 1, 1, -1, -1, -1, -1, -1)
rr = blk(Rm, Matrix([[-1]]))  # on V = e2, e3, e4: rotation plane (e2, e3) angle theta(m), axis e4 -> -1
sigma = blk(Matrix([[1]]), rr, -eye(5))
BN = intersect_comm(formula_space(sigma), N944)
killV = all(all((Lb * Matrix([1 if i == k else 0 for i in range(10)])).applyfunc(cancel).is_zero_matrix
                for k in (2, 3, 4)) for Lb in BN)
check("E3b d = 9, (4,4), sigma|V = rotoreflection R(m) (+) (-1): every block kills lift V", killV)
# rotation in F cap z-perp with dim F = 3 at d = 7, (4,2): A z = 0, so every block kills lift z
N742 = diag(1, 1, 1, 1, -1, -1, -1)
sigma = blk(Matrix([[1]]), -eye(3), Rm, Matrix([[-1]]))
BN = intersect_comm(formula_space(sigma), N742)
lz = zeros(8, 1)
lz[7] = 1
check("E3c d = 7, (4,2), sigma on F cap z-perp = R(m): every block kills lift z", all((Lb * lz).applyfunc(cancel).is_zero_matrix for Lb in BN))
# d = 9, (4,4), sigma = 2 e1 e1^T - I: block structure a = alpha e1, A in so(V) (+) so(F)
sigma = blk(Matrix([[1]]), -eye(8))
BN = intersect_comm(formula_space(sigma), N944)
shape_ok = True
for Lb in BN:
    a = Lb[1:, 0]
    A = Lb[1:, 1:]
    shape_ok = shape_ok and all(a[i] == 0 for i in range(1, 9)) and A[0, :].is_zero_matrix and \
        A[1:4, 4:].is_zero_matrix and A[4:, 1:4].is_zero_matrix
check(f"E3d d = 9, (4,4), sigma = 2e1e1^T - I: dim = {len(BN)} = 1 + 3 + 10, a in span(e1), A in so(V) (+) so(F)",
      len(BN) == 14 and shape_ok)
# d = 7, (4,2), sigma = 2e1e1^T - I: A in so(V) (+) so(F) with dim V = 3, dim F = 3
sigma = blk(Matrix([[1]]), -eye(6))
BN = intersect_comm(formula_space(sigma), N742)
check(f"E3e d = 7, (4,2), sigma = 2e1e1^T - I: dim = {len(BN)} = 1 + 3 + 3 (so(3) twice: excluded by E0)", len(BN) == 7)

# ------------------------------------------------------------------ E4 controls
print("== E4 controls: no exclusion where a gate exists; the positivity step is load-bearing for sigma = n5")
for label, N, sigma in [
        ("(3, nflip, nflip) [DIM-1 cnot]", diag(1, -1, -1), diag(1, -1, -1)),
        ("(5, nC5, nC5) [landed gC5]", diag(1, -1, -1, -1, -1), diag(1, -1, -1, -1, -1)),
        ("(5, (3,1), 2e1e1^T-I) [P3 gate]", diag(1, 1, 1, -1, -1), diag(1, -1, -1, -1, -1)),
        ("(7, N7b, 2e1e1^T-I) [C7b]", diag(1, 1, 1, -1, -1, -1, -1), diag(1, -1, -1, -1, -1, -1, -1))]:
    ex, how, lin, dimBN, p = verdict(sigma, N, label, cross_check=(label.startswith("(3")))
    check(f"E4 {label}: NOT excluded (p_sigma = {p}, common kernel dim {lin}, block space dim {dimBN})", not ex and p == 1 and lin == 0)
ex, how, lin, dimBN, p = verdict(n5, n5, "E4 (5, n5, n5)")
check(f"E4 (5, n5, sigma = n5): linear common kernel dim {lin} == 0, p_sigma = {p}; excluded only by the positivity "
      f"step ({ex})", lin == 0 and p == 2 and ex)

npass = sum(1 for _, cc in checks if cc)
print(f"bal_excl: {npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)
