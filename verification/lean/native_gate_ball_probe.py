"""Round NB-1 -- the exact-computation layer of the finite native-gate ball no-go.

Python integers and fractions only; no floating point, no randomness, no modular arithmetic: every rank is computed by
exact Gaussian elimination over Q, and every point at which an identity is tested is fixed in this file.  Every
assertion is exact; the script exits 1 on the first mismatch.  These statements are exact arithmetic replayed in CI;
they are not kernel-certified.

Conventions.  Each local space is R^n, n = d + 1, basis index 0 = u, 1 .. d-1 = the transverse space T, d = z.
Corners k_a = u + (-1)^a z; they are also the effects <a|.  N = diag(u: 1; p transverse +1; q transverse -1; z: -1).
A vector of R^n (x) R^n is an n x n array X[i][j] (control index i, target index j).

Sections.
 1. S1, the controlled form: for d = 2..7 and a = 0, 1 the linear conditions of the corner and equator arguments cut
    Z_a(t) = G(k_a (x) t), t in T, down to exactly span{k_a} (x) T.
 2. S2, the block structure: for d = 2..7 and every split p + q = d - 1 the exact solution space of
      (1, -t') . Phi(u + t') = 0  and  (1, -N t') . Phi(u + t') = 0  for every unit t'
    (read off the polynomial in t' on the sphere: odd part zero, even part a multiple of |t'|^2) equals the family
      alpha_r at (r, u) AND at (u, r)  +  so(V+)  +  so(V-),
    of dimension p + p(p-1)/2 + q(q+1)/2; the transposed form (u, r) = -(r, u) is not a solution.
 3. S3 replay: for p = 1..8 the averaging identity
      sum_{i, s = +-1} [(1 + s g_i)^2 - |g + s(e_i + K e_i)|^2] = -2 [(p - 1)|g|^2 + ||K||^2]
    as an identity of polynomials in g and the entries K_ij (i < j): both sides have degree <= 2, so agreement on the
    fixed determining set {0, e_v, 2 e_v, e_v + e_w} of the variables proves it (kernel: averaging_bound); the
    same set rejects the identity with (p - 1) replaced by p.
 4. S4, the value identity: for the S2 family with generic block entries (every basis matrix), d = 5 (p = 2) and
    d = 7 (p = 3), (f (x) g)(G(s (x) t)) = (1, b)(I + Gamma_ac)(1, t) on the multi-affine grid, which determines it.
 5. Controls.
    C3  d = 3 complex CNOT (Pauli coordinates, Gaussian-integer arithmetic): frame, S1 form, both native relations,
        S2 structure with p = q = 1, and the reduction formula below (its value is the quantum value).
    C5  d = 5 J/K map: frame, G^2 = I, S1 form, S2 structure with p = 1, q = 3, target relation; the control relation
        FAILS; J, K orthogonal complex structures; the reduction formula
          value = (1 + s_z a_z)(1 + b_x t_x) + (s_z + a_z)(b-.t-) + (a.s)(t_x + b_x) + (a.Js)(b-.K t-)
        holds exactly (multi-affine grid).  Positivity then follows by the hand reduction to C3.
    C2N the same map with N_A (p = q = 2) on the control and N_B on the target satisfies BOTH relations.
    C7  d = 7 algebraic candidate: frame, G^2 = I, S1 and S2 structure (p = q = 3), both relations; for the pure
        product state s (x) t = (u + x) (x) (u + v3) and the control effect f = u + x the target covector is
        w = (1; 1, 1, 1, 0, 0, 0, 0), so the minimum over target effects u + b, |b| <= 1, is 1 - |w_T| = 1 - sqrt(3);
        a rational effect on that segment gives the value -2/3.
    C2  d = 2: p + q = 1 admits no p = q.
"""
import sys
from fractions import Fraction as Fr

CHECKS = []


def check(name, ok, detail=''):
    if not ok:
        print('native_gate_ball_probe: FAILED ' + name + ((' -- ' + detail) if detail else ''))
        sys.exit(1)
    CHECKS.append(name)
    print('PASS ' + name + (('  ' + detail) if detail else ''), flush=True)


# ---------------------------------------------------------------- exact linear algebra ----------------------------
def rank(rows, ncols):
    M = [[Fr(x) for x in r] for r in rows]
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M):
            break
    return r


def zeros(n, m=None):
    return [[Fr(0)] * (n if m is None else m) for _ in range(n)]


def matvec(G, v):
    return [sum(G[i][j] * v[j] for j in range(len(v)) if v[j] != 0) for i in range(len(G))]


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    Bt = list(zip(*B))
    return [[sum(A[i][l] * Bt[j][l] for l in range(k) if A[i][l] != 0) for j in range(m)] for i in range(n)]


def kron(a, b):
    return [x * y for x in a for y in b]


def kronM(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def diag(v):
    return [[Fr(v[i]) if i == j else Fr(0) for j in range(len(v))] for i in range(len(v))]


# ---------------------------------------------------------------- 1. S1 --------------------------------------------
for d in range(2, 8):
    n = d + 1
    for a in (0, 1):
        s = 1 - 2 * a
        kb = [Fr(0)] * n; kb[0] = Fr(1); kb[d] = Fr(-s)            # k_abar
        k0 = [Fr(0)] * n; k0[0] = Fr(1); k0[d] = Fr(1)
        k1 = [Fr(0)] * n; k1[0] = Fr(1); k1[d] = Fr(-1)
        rows = []
        idx = lambda i, j: i * n + j
        for j in range(n):                                         # (k_abar^T (x) I) Z = 0
            r = [0] * (n * n)
            for i in range(n): r[idx(i, j)] = kb[i]
            rows.append(r)
        for kk in (k0, k1):                                        # (I (x) k_b^T) Z = 0
            for i in range(n):
                r = [0] * (n * n)
                for j in range(n): r[idx(i, j)] = kk[j]
                rows.append(r)
        for i in range(1, d):                                      # the equator effect curve kills the T (x) R^n rows
            for j in range(n):
                r = [0] * (n * n); r[idx(i, j)] = 1; rows.append(r)
        nullity = n * n - rank(rows, n * n)
        # the family k_a (x) e_m, m in T, satisfies every row
        fam = []
        for m in range(1, d):
            v = [Fr(0)] * (n * n)
            for i in range(n):
                ka_i = Fr(1) if i == 0 else (Fr(s) if i == d else Fr(0))
                v[idx(i, m)] = ka_i
            fam.append(v)
        ok_members = all(sum(Fr(x) * y for x, y in zip(r, v)) == 0 for r in rows for v in fam)
        check('S1 d=%d a=%d: solution space = span{k_a} (x) T (dim %d)' % (d, a, d - 1),
              nullity == d - 1 and ok_members and rank(fam, n * n) == d - 1)


# ---------------------------------------------------------------- 2. S2 --------------------------------------------
def s2_rows(d, nu):
    """exact linear conditions on Phi (n x n, Phi[i][j] = component i of Phi(e_j)) for
       (1,-t).Phi(1,t) = 0 and (1,-Nt).Phi(1,t) = 0 on the unit sphere; nu = eigenvalues of N on 1..d"""
    n = d + 1
    idx = lambda i, j: i * n + j
    rows = []
    for nv in ([1] * d, nu):
        # polynomial: Phi00 + sum_j (Phi0j - nv_j Phij0) t_j - sum_ij nv_i Phi_ij t_i t_j
        for j in range(1, n):                                      # odd part
            r = [0] * (n * n); r[idx(0, j)] = 1; r[idx(j, 0)] = -nv[j - 1]; rows.append(r)
        for i in range(1, n):                                      # even part = c |t|^2: sym(nv_i Phi_ij) = Phi00 delta
            for j in range(i, n):
                r = [0] * (n * n)
                r[idx(i, j)] += -nv[i - 1]; r[idx(j, i)] += -nv[j - 1]
                if i == j:
                    r[idx(i, j)] = -2 * nv[i - 1]; r[idx(0, 0)] = 2
                rows.append(r)
    return rows


for d in range(2, 8):
    n = d + 1
    for p in range(0, d):
        q = d - 1 - p
        nu = [1] * p + [-1] * q + [-1]
        Vp = [i for i in range(1, d) if nu[i - 1] == 1]
        Vm = [i for i in range(1, n) if nu[i - 1] == -1]
        rows = s2_rows(d, nu)
        idx = lambda i, j: i * n + j
        fam = []
        for r_ in Vp:
            v = [Fr(0)] * (n * n); v[idx(r_, 0)] = 1; v[idx(0, r_)] = 1; fam.append(v)
        for blk in (Vp, Vm):
            for i in range(len(blk)):
                for j in range(i + 1, len(blk)):
                    v = [Fr(0)] * (n * n); v[idx(blk[i], blk[j])] = 1; v[idx(blk[j], blk[i])] = -1; fam.append(v)
        nullity = n * n - rank(rows, n * n)
        members = all(sum(Fr(x) * y for x, y in zip(r, v)) == 0 for r in rows for v in fam)
        dim = p + p * (p - 1) // 2 + q * (q + 1) // 2
        ok = nullity == dim and members and len(fam) == dim and rank(fam, n * n) == dim
        bad = None
        if Vp:
            v = [Fr(0)] * (n * n); v[idx(Vp[0], 0)] = 1; v[idx(0, Vp[0])] = -1
            bad = any(sum(Fr(x) * y for x, y in zip(r, v)) != 0 for r in rows)
        check('S2 d=%d p=%d q=%d: solution space = alpha at (r,u) and (u,r) + so(V+) + so(V-) (dim %d)%s'
              % (d, p, q, dim, '; transposed form excluded' if Vp else ''), ok and (bad is None or bad))

# ---------------------------------------------------------------- 3. S3 replay -------------------------------------
def s3_defect(p, g, K):
    tot = Fr(0)
    for i in range(p):
        for s in (1, -1):
            v = [g[j] + s * ((1 if j == i else 0) + K[j][i]) for j in range(p)]
            tot += (1 + s * g[i]) ** 2 - sum(x * x for x in v)
    return tot + 2 * ((p - 1) * sum(x * x for x in g) + sum(K[i][j] ** 2 for i in range(p) for j in range(p)))


npts = 0
for p in range(1, 9):
    var = [('g', j) for j in range(p)] + [('K', i, j) for i in range(p) for j in range(i + 1, p)]
    pts = [{}] + [{v: c} for v in var for c in (1, 2)] \
        + [{v: 1, w: 1} for a, v in enumerate(var) for w in var[a + 1:]]
    for pt in pts:
        g = [Fr(pt.get(('g', j), 0)) for j in range(p)]
        K = [[Fr(0)] * p for _ in range(p)]
        for i in range(p):
            for j in range(i + 1, p):
                K[i][j] = Fr(pt.get(('K', i, j), 0)); K[j][i] = -K[i][j]
        if s3_defect(p, g, K) != 0:
            check('S3 replay p=%d at %s' % (p, sorted(pt.items())), False)
        npts += 1
check('S3 replay: the averaging identity as a polynomial identity, p = 1..8 (%d determining points)' % npts, True)
# countercontrol: the same determining set rejects the identity with (p - 1) replaced by p
bad = [p for p in range(1, 9) if s3_defect(p, [Fr(1)] + [Fr(0)] * (p - 1), [[Fr(0)] * p for _ in range(p)])
       + 2 * sum(x * x for x in [Fr(1)] + [Fr(0)] * (p - 1)) == 0]
check('S3 countercontrol: the identity with (p - 1) replaced by p fails at the point g = e_1 for every p = 1..8',
      bad == [])


# ---------------------------------------------------------------- 4. S4 value identity -----------------------------
def s4_identity(d, p):
    n = d + 1; m = d - 1
    TA = list(range(1, d)); Vp = list(range(1, p + 1))
    ok = True
    # every basis instance of the block entries: one nonzero entry of one A_r, or of one B_rs (with B_sr = -B_rs)
    instances = []
    for r_ in Vp:
        for k in range(m):
            for l in range(m):
                instances.append(('A', r_, None, k, l))
    for i_ in range(len(Vp)):
        for j_ in range(i_ + 1, len(Vp)):
            for k in range(m):
                for l in range(m):
                    instances.append(('B', Vp[i_], Vp[j_], k, l))
    for inst in instances:
        A = {r_: [[0] * m for _ in range(m)] for r_ in Vp}
        B = {(r_, s_): [[0] * m for _ in range(m)] for r_ in Vp for s_ in Vp}
        if inst[0] == 'A':
            A[inst[1]][inst[3]][inst[4]] = 1
        else:
            B[(inst[1], inst[2])][inst[3]][inst[4]] = 1; B[(inst[2], inst[1])][inst[3]][inst[4]] = -1

        def Gt(ci, tj):
            """G~(e_ci (x) e_tj) as dict {(i, j): value}, ci in T_A, tj in E+ (0 or V+)"""
            out = {}
            col = ci - 1
            if tj == 0:
                for r_ in Vp:
                    for k in range(m):
                        if A[r_][k][col]: out[(k + 1, r_)] = out.get((k + 1, r_), 0) + A[r_][k][col]
            else:
                for k in range(m):
                    if A[tj][k][col]: out[(k + 1, 0)] = out.get((k + 1, 0), 0) + A[tj][k][col]
                for r_ in Vp:
                    if r_ != tj:
                        for k in range(m):
                            if B[(r_, tj)][k][col]: out[(k + 1, r_)] = out.get((k + 1, r_), 0) + B[(r_, tj)][k][col]
            return out
        # multi-affine grid: a, c in basis of T_A (linear); b, t in {0} + basis of V+ (affine)
        for ai in TA:
            for ci in TA:
                gam = [A[r_][ai - 1][ci - 1] for r_ in Vp]
                Km = [[B[(r_, s_)][ai - 1][ci - 1] for s_ in Vp] for r_ in Vp]
                for bi in [None] + Vp:
                    for ti in [None] + Vp:
                        bvec = [1 if (bi == r_) else 0 for r_ in Vp]; tvec = [1 if (ti == r_) else 0 for r_ in Vp]
                        # left side: g.t (from G(u (x) t) = u (x) t, M_0 = I) + (f (x) g)(G~(c (x) t))
                        lhs = 1 + sum(x * y for x, y in zip(bvec, tvec))
                        tcomp = [(0, 1)] + ([(ti, 1)] if ti is not None else [])
                        for tj, tw in tcomp:
                            for (i, j), val in Gt(ci, tj).items():
                                if i == ai:
                                    gj = 1 if j == 0 else (1 if j == bi else 0)
                                    lhs += val * tw * gj
                        rhs = 1 + sum(x * y for x, y in zip(bvec, tvec)) + sum(x * y for x, y in zip(gam, bvec)) \
                            + sum(x * y for x, y in zip(gam, tvec)) \
                            + sum(bvec[r_] * Km[r_][s_] * tvec[s_] for r_ in range(p) for s_ in range(p))
                        if lhs != rhs:
                            ok = False
    return ok


for (d, p) in ((5, 2), (7, 3)):
    check('S4 d=%d p=%d: value = (1,b)(I + Gamma_ac)(1,t) for every basis block entry, on the multi-affine grid'
          % (d, p), s4_identity(d, p))


# ---------------------------------------------------------------- 5. controls --------------------------------------
def corners(n):
    k0 = [Fr(0)] * n; k0[0] = Fr(1); k0[n - 1] = Fr(1)
    k1 = [Fr(0)] * n; k1[0] = Fr(1); k1[n - 1] = Fr(-1)
    return [k0, k1]


def frame_ok(G, n):
    k = corners(n)
    return all(matvec(G, kron(k[a], k[b])) == kron(k[a], k[a ^ b]) for a in (0, 1) for b in (0, 1))


def relations(G, n, NA, NB):
    I = eye(n)
    rt = matmul(matmul(kronM(I, NB), G), kronM(I, NB)) == G
    rc = matmul(matmul(kronM(NA, I), G), kronM(NA, I)) == matmul(kronM(I, NB), G)
    return rt, rc


def s1_s2_structure(G, n, nu):
    """S1 form (M_0 = I read off, isometric on T) and S2 structure of G~ = G (I (x) M_0^-1), M_0 a signed permutation"""
    d = n - 1; k = corners(n); e = eye(n)
    M = []
    for a in (0, 1):
        Ma = zeros(n)
        for j in range(n):
            img = matvec(G, kron(k[a], e[j]))
            row_u = img[0:n]
            if [img[i * n + jj] for i in range(n) for jj in range(n)] != [k[a][i] * row_u[jj] for i in range(n) for jj in range(n)]:
                return False
            for i in range(n): Ma[i][j] = row_u[i]
        M.append(Ma)
    iso = all(matmul([list(r) for r in zip(*Ma)], Ma) == eye(n) for Ma in M)
    Nm = diag([1] + nu)
    if matmul(Nm, M[0]) != M[1]:
        return False
    M0inv = [list(r) for r in zip(*M[0])]                          # orthogonal
    Gt = matmul(G, kronM(eye(n), M0inv))
    Vp = [i for i in range(1, d) if nu[i - 1] == 1]; Vm = [i for i in range(1, n) if nu[i - 1] == -1]
    ok = True
    col = lambda ci, tj: [Gt[r][ci * n + tj] for r in range(n * n)]
    for c in range(1, d):
        cu = col(c, 0)
        ok &= all(cu[i * n + j] == 0 for i in range(n) for j in [0] + Vm)
        ok &= all(cu[i * n + j] == 0 for i in [0, d] for j in range(n))
        for r_ in Vp:
            cr = col(c, r_)
            ok &= all(cr[i * n + 0] == cu[i * n + r_] for i in range(n))                 # same A_r twice
            ok &= all(cr[i * n + j] == 0 for i in range(n) for j in Vm)
            for s_ in Vp:
                cs = col(c, s_)
                ok &= all(cr[i * n + s_] == -cs[i * n + r_] for i in range(n))           # B antisymmetric
        for j_ in Vm:
            cj = col(c, j_)
            ok &= all(cj[i * n + jj] == 0 for i in range(n) for jj in [0] + Vp)
            for l_ in Vm:
                cl = col(c, l_)
                ok &= all(cj[i * n + l_] == -cl[i * n + j_] for i in range(n))            # V- block antisymmetric
    return iso and ok


# Gaussian-integer 2x2 arithmetic for the complex CNOT
def gmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def gadd(a, b): return (a[0] + b[0], a[1] + b[1])
def mm(A, B):
    n = len(A)
    return [[(lambda acc: acc)(sum_g([gmul(A[i][l], B[l][j]) for l in range(n)])) for j in range(n)] for i in range(n)]
def sum_g(xs):
    acc = (0, 0)
    for x in xs: acc = gadd(acc, x)
    return acc
def gkron(A, B):
    n, m = len(A), len(B)
    return [[gmul(A[i // m][j // m], B[i % m][j % m]) for j in range(n * m)] for i in range(n * m)]
def dag(A):
    return [[(A[j][i][0], -A[j][i][1]) for j in range(len(A))] for i in range(len(A))]


ONE, ZER, IM = (1, 0), (0, 0), (0, 1)
PAULI = [[[ONE, ZER], [ZER, ONE]], [[ZER, ONE], [ONE, ZER]], [[ZER, (0, -1)], [IM, ZER]], [[ONE, ZER], [ZER, (-1, 0)]]]
CN = [[ONE if (i == j and i < 2) or (i, j) in ((2, 3), (3, 2)) else ZER for j in range(4)] for i in range(4)]
basis16 = [gkron(PAULI[a], PAULI[b]) for a in range(4) for b in range(4)]
G3 = zeros(16)
for jj, Bj in enumerate(basis16):
    img = mm(mm(CN, Bj), dag(CN))
    for ii, Bi in enumerate(basis16):
        tr = sum_g([mm(img, Bi)[k][k] for k in range(4)])
        assert tr[1] == 0 and tr[0] % 4 == 0
        G3[ii][jj] = Fr(tr[0], 4)
nu3 = [1, -1, -1]
rt3, rc3 = relations(G3, 4, diag([1] + nu3), diag([1] + nu3))
check('C3 d=3 complex CNOT: frame, G^2 = I, S1/S2 structure (p = q = 1), both native relations',
      frame_ok(G3, 4) and matmul(G3, G3) == eye(16) and s1_s2_structure(G3, 4, nu3) and rt3 and rc3)


def jk_map():
    """d = 5, basis u, x, y, w1, w2, z; N = diag(1, 1, -1, -1, -1, -1)"""
    n = 6; U, X, Y, W1, W2, Z = range(6)
    Nd = [1, 1, -1, -1, -1, -1]
    J = {X: (1, Y), Y: (-1, X), W1: (1, W2), W2: (-1, W1)}
    K = {Y: (1, Z), Z: (-1, Y), W1: (1, W2), W2: (-1, W1)}
    S = {U: (1, X), X: (1, U)}
    G = zeros(36)
    e = eye(n); k = corners(n)
    for j in range(n):
        Pp = [e[j][i] * (1 if Nd[i] == 1 else 0) for i in range(n)]
        Pm = [e[j][i] * (1 if Nd[i] == -1 else 0) for i in range(n)]
        col_u = [a + b for a, b in zip(kron(e[U], Pp), kron(e[Z], Pm))]
        col_z = [a + b for a, b in zip(kron(e[Z], Pp), kron(e[U], Pm))]
        for r in range(36): G[r][U * n + j] = col_u[r]; G[r][Z * n + j] = col_z[r]
    for c in (X, Y, W1, W2):
        for j in (U, X):
            s, l = S[j]; G[c * n + l][c * n + j] = Fr(s)
        for j in (Y, W1, W2, Z):
            s1, kk = J[c]; s2, l = K[j]; G[kk * n + l][c * n + j] = Fr(s1 * s2)
    Jm = zeros(n); Km = zeros(n)
    for a, (s, b) in J.items(): Jm[b][a] = Fr(s)
    for a, (s, b) in K.items(): Km[b][a] = Fr(s)
    return G, Nd, Jm, Km


G5, Nd5, J5, K5 = jk_map()
N5 = diag(Nd5)
rt5, rc5 = relations(G5, 6, N5, N5)
TA5 = [1, 2, 3, 4]; Vm5 = [2, 3, 4, 5]
Jsub = [[J5[i][j] for j in TA5] for i in TA5]; Ksub = [[K5[i][j] for j in Vm5] for i in Vm5]
cs_ok = (matmul(Jsub, Jsub) == [[-x for x in r] for r in eye(4)] and [list(r) for r in zip(*Jsub)] == [[-x for x in r] for r in Jsub]
         and matmul(Ksub, Ksub) == [[-x for x in r] for r in eye(4)] and [list(r) for r in zip(*Ksub)] == [[-x for x in r] for r in Ksub])


def reduction_ok(G, n, J, K, Nd):
    """multi-affine grid: value(s', t', a, b) == the reduction formula, for s', t', a, b in {0} + basis of R^d"""
    d = n - 1; e = eye(n); z = d
    Vm = [i for i in range(1, n) if Nd[i] == -1]; xidx = [i for i in range(1, d) if Nd[i] == 1]
    pts = [None] + list(range(1, n))
    def vec(i):
        v = [Fr(0)] * n; v[0] = Fr(1)
        if i is not None: v[i] += 1
        return v
    for si in pts:
        s = vec(si); sp_ = [s[i] for i in range(n)]
        Gs = [matvec(G, kron(s, e[j])) for j in range(n)]          # columns G(s (x) e_j)
        for ti in pts:
            t = vec(ti)
            W = [sum(Gs[j][r] * t[j] for j in range(n)) for r in range(n * n)]
            for ai in pts:
                f = vec(ai)
                for bi in pts:
                    g = vec(bi)
                    val = sum(f[i] * g[j] * W[i * n + j] for i in range(n) for j in range(n))
                    sT = [s[i] if 1 <= i < d else 0 for i in range(n)]; aT = [f[i] if 1 <= i < d else 0 for i in range(n)]
                    Js = matvec(J, sT)
                    tm = [t[i] if i in Vm else 0 for i in range(n)]; bm = [g[i] if i in Vm else 0 for i in range(n)]
                    Kt = matvec(K, tm)
                    tx = sum(t[i] for i in xidx); bx = sum(g[i] for i in xidx)
                    rhs = (1 + s[z] * f[z]) * (1 + bx * tx) + (s[z] + f[z]) * sum(x * y for x, y in zip(bm, tm)) \
                        + sum(x * y for x, y in zip(aT, sT)) * (tx + bx) + sum(x * y for x, y in zip(aT, Js)) * sum(x * y for x, y in zip(bm, Kt))
                    if val != rhs:
                        return False
    return True


check('C5 d=5 J/K map: frame, G^2 = I, S1/S2 structure (p = 1, q = 3), target relation; control relation FAILS',
      frame_ok(G5, 6) and matmul(G5, G5) == eye(36) and s1_s2_structure(G5, 6, Nd5[1:]) and rt5 and not rc5)
check('C5 J, K orthogonal complex structures; the reduction formula holds exactly on the multi-affine grid',
      cs_ok and reduction_ok(G5, 6, J5, K5, Nd5))
J3 = zeros(4); J3[2][1] = Fr(1); J3[1][2] = Fr(-1)                # x -> y, y -> -x
K3 = zeros(4); K3[3][2] = Fr(1); K3[2][3] = Fr(-1)                # y -> z, z -> -y
check('C3 the same reduction formula holds for the complex CNOT (it is the d = 3 case)',
      reduction_ok(G3, 4, J3, K3, [1, 1, -1, -1]))
NA = diag([1, 1, -1, 1, -1, -1])
rtA, rcA = relations(G5, 6, NA, N5)
check('C2N d=5: the J/K map with N_A (p = q = 2) on the control and N_B on the target meets BOTH relations',
      rtA and rcA and not rc5)


def d7_map():
    n = 8; U, X, V2, V3, Y1, Y2, Y3, Z = range(8)
    Nd = [1, 1, 1, 1, -1, -1, -1, -1]
    M0 = diag([1, 1, -1, 1, 1, 1, 1, 1]); Nm = diag(Nd); M1 = matmul(Nm, M0)
    J = {X: (1, Y1), Y1: (-1, X), V2: (1, Y2), Y2: (-1, V2), V3: (1, Y3), Y3: (-1, V3)}
    K = {Y1: (1, Z), Z: (-1, Y1), Y2: (1, Y3), Y3: (-1, Y2)}
    Ep = {U: (1, X), X: (1, U), V2: (1, V3), V3: (1, V2)}
    G = zeros(64); e = eye(n); k = corners(n)
    for j in range(n):
        m0 = [M0[i][j] for i in range(n)]; m1 = [M1[i][j] for i in range(n)]
        cu = [(a + b) / 2 for a, b in zip(kron(k[0], m0), kron(k[1], m1))]
        cz = [(a - b) / 2 for a, b in zip(kron(k[0], m0), kron(k[1], m1))]
        for r in range(64): G[r][U * n + j] = cu[r]; G[r][Z * n + j] = cz[r]
    for c in (X, V2, V3, Y1, Y2, Y3):
        for j in (U, X, V2, V3):
            s, l = Ep[j]; G[c * n + l][c * n + j] = Fr(s)
        for j in (Y1, Y2, Y3, Z):
            s1, kk = J[c]; s2, l = K[j]; G[kk * n + l][c * n + j] = Fr(s1 * s2)
    return G, Nd


G7, Nd7 = d7_map()
N7 = diag(Nd7)
rt7, rc7 = relations(G7, 8, N7, N7)
# exact rational witness: s = f = u + x, t = u + v3, g = (1, b) with b a rational unit vector (0, b1, b2, b3, 0, ..)
e8 = eye(8)
s7 = [a + b for a, b in zip(e8[0], e8[1])]; t7 = [a + b for a, b in zip(e8[0], e8[3])]
W7 = matvec(G7, kron(s7, t7)); fvec = s7
w = [sum(fvec[i] * W7[i * 8 + j] for i in range(8)) for j in range(8)]      # target covector image: value = w . g
# a rational point on the unit sphere of span{x, v2, v3}: (-2/3, -2/3, -1/3)
bvec = [Fr(0), Fr(-2, 3), Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(0), Fr(0), Fr(0)]
gvec = [Fr(1)] + bvec[1:]
val7 = sum(x * y for x, y in zip(w, gvec))
check('C7 d=7 candidate: frame, G^2 = I, S1/S2 structure (p = q = 3), both native relations',
      frame_ok(G7, 8) and matmul(G7, G7) == eye(64) and s1_s2_structure(G7, 8, Nd7[1:]) and rt7 and rc7)
check('C7 max-cone violation: w = (1; 1, 1, 1, 0, 0, 0, 0), minimum over target effects 1 - sqrt(3) < 0; '
      'rational effect value %s' % val7,
      w == [Fr(1), Fr(1), Fr(1), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)] and sum(x * x for x in w[1:]) == 3 > w[0] ** 2
      and sum(x * x for x in bvec) == 1 and val7 == Fr(-2, 3))
check('C2 d=2: p + q = 1 admits no p = q', all(p != 1 - p for p in (0, 1)))

print('native_gate_ball_probe: OK -- %d checks: S1 d=2..7, S2 d=2..7 all p, S3 replay, S4 identity, controls C3 C5 C2N C7 C2'
      % len(CHECKS))
