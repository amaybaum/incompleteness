"""Coordinator's independent check of EQ-C's foundation (exact; written without EQ-C's code).

V1 := { X in End(W 3) : X preserves the normalization omega_00 (row 0 of X is zero), and for every unit x, y in R^3,
        (1,-x)^T X(hom x hom y^T) = 0  and  X(hom x hom y^T) (1,-y) = 0 }.
Derivation: if exp(tX) preserves an admissible cone K (products in K, K inside maxCone), then t -> pairVal e f
(exp(tX) P) >= 0 vanishes at t = 0 whenever e = (1,-x) or f = (1,-y) for the pure product P = hom x hom y^T, so its
derivative vanishes; the Lorentz cone spans R^4.
Checks:
  V1a  upper bound: exact constraints at N rational sphere points give rank r; dim V1 <= 240 - r (= 33 claimed);
  V1b  lower bound: a basis of the sampled null space satisfies the constraints identically on the sphere
       (symbolic stereographic parameters), so dim V1 = 33 exactly;
  V1c  the su(4) image (15) and its R_B conjugate lie in V1; together they span 24 (they share the local 6);
  V1d  the 9 extra directions are not skew for the Euclidean pairing (symmetric part nonzero), as EQ-C's N;
  CX   R_B . SWAP . R_B = T . SWAP with T = R_A R_B the global transpose; SWAP is Ad of a unitary (Choi rank 1);
       T . SWAP has Choi rank 16, so it is not Ad of a unitary.
"""
import sys, random
from sympy import Matrix, Rational as R, I, eye, zeros, symbols, cancel, together, expand, simplify

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


def hom(x):
    return Matrix([1] + list(x))


def sphere_point(a, b):
    s = a * a + b * b
    return [2 * a / (1 + s), 2 * b / (1 + s), (s - 1) / (1 + s)]


def constraint_rows(x, y):
    """rows (over the 240 unknowns X[r, c], r = 1..15, c = 0..15) of the 8 linear constraints at (x, y)"""
    P = hom(x) * hom(y).T
    p = [P[m, n] for m in range(4) for n in range(4)]
    ex = [1] + [-v for v in x]
    fy = [1] + [-v for v in y]
    rows = []
    # (X P)[m, n] = sum_c X[4m+n, c] p[c]; row 0 of X is zero (m = n = 0 term contributes nothing).
    # A: sum_m ex[m] (XP)[m, n] = 0 for each n
    for n in range(4):
        row = [0] * 240
        for m in range(4):
            r = 4 * m + n
            if r == 0:
                continue
            for c in range(16):
                row[(r - 1) * 16 + c] += ex[m] * p[c]
        rows.append(row)
    # B: sum_n (XP)[m, n] fy[n] = 0 for each m
    for m in range(4):
        row = [0] * 240
        for n in range(4):
            r = 4 * m + n
            if r == 0:
                continue
            for c in range(16):
                row[(r - 1) * 16 + c] += fy[n] * p[c]
        rows.append(row)
    return rows


rng = random.Random(20261008)
pts = []
rows = []
rank = 0
for k in range(60):
    a = R(rng.randint(-7, 7), rng.randint(1, 7))
    b = R(rng.randint(-7, 7), rng.randint(1, 7))
    c = R(rng.randint(-7, 7), rng.randint(1, 7))
    d = R(rng.randint(-7, 7), rng.randint(1, 7))
    rows += constraint_rows(sphere_point(a, b), sphere_point(c, d))
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
M = Matrix(rows)
DM = DomainMatrix.from_Matrix(M).convert_to(QQ)
rank = DM.rank()
check(f"V1a upper bound: rank of exact constraints at 60 rational sphere pairs = {rank}; dim V1 <= {240 - rank}",
      240 - rank == 33)
ns = [Matrix(v) for v in DM.nullspace().to_Matrix().tolist()]
ns = [Matrix(len(v), 1, v) for v in [list(r) for r in ns]]
check(f"V1a sampled null space has dim {len(ns)}", len(ns) == 33)


def X_of(v):
    X = zeros(16, 16)
    for r in range(1, 16):
        for c in range(16):
            X[r, c] = v[(r - 1) * 16 + c]
    return X


aa, bb, cc, dd = symbols("aa bb cc dd")
xs, ys = sphere_point(aa, bb), sphere_point(cc, dd)
symrows = constraint_rows(xs, ys)
ok = True
den = (1 + aa**2 + bb**2) ** 2 * (1 + cc**2 + dd**2) ** 2
symrows_p = [[expand(cancel(r * den)) for r in row] for row in symrows]
for v in ns:
    for row in symrows_p:
        e = expand(sum(row[i] * v[i] for i in range(240) if v[i] != 0))
        if e != 0:
            ok = False
            break
    if not ok:
        break
check("V1b every sampled null vector satisfies the constraints identically on the sphere: dim V1 = 33 exactly", ok)

# su(4) image in Pauli coordinates
S0 = Matrix([[1, 0], [0, 1]]); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
PAU = [S0, SX, SY, SZ]


def kron(A, B):
    out = zeros(A.shape[0] * B.shape[0], A.shape[1] * B.shape[1])
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            out[i * B.shape[0]:(i + 1) * B.shape[0], j * B.shape[1]:(j + 1) * B.shape[1]] = A[i, j] * B
    return out


SIG = [[kron(PAU[m], PAU[n]) for n in range(4)] for m in range(4)]


def generator(H):
    """X with omega' = X omega for d rho/dt = i[H, rho], rho = (1/4) sum omega_ab s_a (x) s_b"""
    X = zeros(16, 16)
    for a in range(4):
        for b in range(4):
            dr = I * (H * SIG[a][b] - SIG[a][b] * H) / 4
            for m in range(4):
                for n in range(4):
                    X[4 * m + n, 4 * a + b] = expand((dr * SIG[m][n]).trace())
    return X


gens = [generator(SIG[a][b]) for a in range(4) for b in range(4) if (a, b) != (0, 0)]
check("V1c su(4) generators are real", all(all(v.is_real for v in X) for X in gens))
RB = zeros(16, 16)
reflY = [1, 1, -1, 1]
for m in range(4):
    for n in range(4):
        RB[4 * m + n, 4 * m + n] = reflY[n]
twisted = [RB * X * RB for X in gens]


def vec240(X):
    return Matrix([X[r, c] for r in range(1, 16) for c in range(16)])


def in_V1(X):
    if not X[0, :].is_zero_matrix:
        return False
    return (M * vec240(X)).is_zero_matrix


check("V1c the 15 su(4) generators and their R_B conjugates satisfy the sampled constraints and fix omega_00",
      all(in_V1(X) for X in gens + twisted))
span = Matrix.hstack(*[vec240(X) for X in gens + twisted])
check(f"V1c span(su(4) image + R_B conjugate) has dim {span.rank()} (= 15 + 15 - 6 local)", span.rank() == 24)
NS = Matrix.hstack(*ns)
full = Matrix.hstack(span, NS)
check(f"V1c su(4) image + conjugate lie inside the 33-dim V1 (rank of union {full.rank()})", full.rank() == 33)
# the extra directions: complement of the 24 inside V1 contains a non-skew element
extra_nonskew = False
for v in ns:
    X = X_of(v)
    if Matrix.hstack(span, vec240(X)).rank() > 24 and not (X + X.T).is_zero_matrix:
        extra_nonskew = True
        break
check("V1d a direction of V1 outside the 24 is not Euclidean-skew (compactness must remove it)", extra_nonskew)

# CX
SW = zeros(16, 16)
for m in range(4):
    for n in range(4):
        SW[4 * n + m, 4 * m + n] = 1
RA = zeros(16, 16)
for m in range(4):
    for n in range(4):
        RA[4 * m + n, 4 * m + n] = reflY[m]
T = RA * RB
check("CX R_B SWAP R_B == T SWAP (T = R_A R_B, the global transpose in Pauli coordinates)", (RB * SW * RB - T * SW).is_zero_matrix)


def choi_rank(apply_map, dim):
    C = zeros(dim * dim, dim * dim)
    for i in range(dim):
        for j in range(dim):
            Eij = zeros(dim, dim)
            Eij[i, j] = 1
            C += kron(Eij, apply_map(Eij))
    return C.rank()


SWAPU = zeros(4, 4)
for i in range(2):
    for j in range(2):
        SWAPU[2 * j + i, 2 * i + j] = 1
r_swap = choi_rank(lambda A: SWAPU * A * SWAPU.H, 4)
r_tswap = choi_rank(lambda A: (SWAPU * A * SWAPU.H).T, 4)
check(f"CX Choi rank: Ad(SWAP) = {r_swap} (unitary), transpose . Ad(SWAP) = {r_tswap}", r_swap == 1 and r_tswap == 16)

npass = sum(1 for _, c in checks if c)
print(f"review_eqC_fast: {npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)
