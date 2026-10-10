"""Thread G3, probe P1 -- single-system side: the two-level systems H_2(F) over the Hurwitz algebras,
their NOTs, and the split census of DIM-1's two numeric constraints.

Read-only research against base 06b6f94e479bc19a28979c72316823cbdd0fb62b. Exact arithmetic only (Fraction).

DECISION RULES (written before the first run; the verdict text is generated from the measurements):
  A  Cayley-Dickson controls: R, C, H associative; O not associative but alternative; norm multiplicative
     on every basis pair and on two non-basis pairs.  A failure voids every F-row below.
  B  For F in {R, C, H, O}: H_2(F) with the Jordan product (AB+BA)/2 is the spin factor V_{1+k}
     (traceless orthonormal basis u_i with u_i o u_j = delta_ij I), and the level exchange
     theta(A) = X A X is a Jordan automorphism, involutive, flipping z = diag(1,-1).
     Record the homogenized split (+1, -1) of theta, its tangent split, det on the tangent space,
     the equatorial (off-diagonal) split (dim Re F, dim Im F), balance, block (p_tan <= 1).
  C  The i-map: for each imaginary unit u of F, Phi_u(A) = Z o A + u * [A, Z]/2 sends the
     commutant {I, X} of theta into Herm; Phi_u is a bijection commutant -> anticommutant iff k = 2.
     Over R there is no u and [X, Z]/2 is antisymmetric (not in Herm).
  D  The Wigner table over C: the four z-flipping NOTs Ad X, Ad Y (unitary) and A -> X A^T X,
     A -> Y A^T Y (antiunitary): automorphism vs antiautomorphism of the associative product,
     Jordan automorphism (all four), Bloch det, homogenized split.  Rule: balanced <=> unitary.
  E  Census over the whole spin-factor family V_d, d = 1..13, all orthogonal involutions N of the
     tangent space with N z = -z (diagonal representatives (p_tan, m_tan), m_tan >= 1; every orthogonal
     involution is orthogonally diagonalizable, [W]):
        PAR   = { d : some N balanced }            BLK = { d : some N with p_tan <= 1 }
        PAR+  = { d : some N balanced, det N = +1 } JOINT = { d : some N balanced and p_tan <= 1 }
     and their intersections with the Hurwitz dimensions {1, 2, 3, 5, 9}.

Run:  python3 -I g3_p1_hurwitz.py
"""
from fractions import Fraction as Fr
import itertools

CHECKS = []


def check(name, cond, detail=""):
    cond = bool(cond)
    CHECKS.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))


# ---------------------------------------------------------------- Cayley-Dickson algebras over Q
def cd_mul(x, y):
    n = len(x)
    if n == 1:
        return (x[0] * y[0],)
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    # (a,b)(c,d) = (ac - conj(d) b, d a + b conj(c))
    left = tuple(p - q for p, q in zip(cd_mul(a, c), cd_mul(cd_conj(d), b)))
    right = tuple(p + q for p, q in zip(cd_mul(d, a), cd_mul(b, cd_conj(c))))
    return left + right


def cd_conj(x):
    n = len(x)
    if n == 1:
        return x
    h = n // 2
    return cd_conj(x[:h]) + tuple(-t for t in x[h:])


def cd_add(x, y):
    return tuple(p + q for p, q in zip(x, y))


def cd_scale(c, x):
    return tuple(c * t for t in x)


def cd_norm2(x):
    return sum(t * t for t in x)


def unit(n, i):
    return tuple(Fr(1) if j == i else Fr(0) for j in range(n))


FIELDS = [(1, "R"), (2, "C"), (4, "H"), (8, "O")]

for k, nm in FIELDS:
    basis = [unit(k, i) for i in range(k)]
    assoc = all(cd_mul(cd_mul(a, b), c) == cd_mul(a, cd_mul(b, c)) for a in basis for b in basis for c in basis)
    alt = all(cd_mul(cd_mul(a, a), b) == cd_mul(a, cd_mul(a, b)) and cd_mul(cd_mul(b, a), a) == cd_mul(b, cd_mul(a, a))
              for a in basis for b in basis)
    x1 = tuple(Fr(i + 1, 3) for i in range(k))
    x2 = tuple(Fr((-1) ** i * (2 * i + 1), 5) for i in range(k))
    normmult = all(cd_norm2(cd_mul(a, b)) == cd_norm2(a) * cd_norm2(b) for a in basis + [x1] for b in basis + [x2])
    expect_assoc = k <= 4
    check("A %s: associative=%s (expected %s), alternative, norm multiplicative" % (nm, assoc, expect_assoc),
          assoc == expect_assoc and alt and normmult)


# ---------------------------------------------------------------- 2x2 matrices over F
def m_mul(A, B):
    return [[cd_add(cd_mul(A[i][0], B[0][j]), cd_mul(A[i][1], B[1][j])) for j in range(2)] for i in range(2)]


def m_add(A, B):
    return [[cd_add(A[i][j], B[i][j]) for j in range(2)] for i in range(2)]


def m_scale(c, A):
    return [[cd_scale(c, A[i][j]) for j in range(2)] for i in range(2)]


def m_sub(A, B):
    return m_add(A, m_scale(Fr(-1), B))


def jordan(A, B):
    return m_scale(Fr(1, 2), m_add(m_mul(A, B), m_mul(B, A)))


def herm(k, a, b, q):
    """[[a, q], [conj q, b]] with a, b real."""
    r = lambda t: (Fr(t),) + tuple(Fr(0) for _ in range(k - 1))
    return [[r(a), tuple(q)], [cd_conj(tuple(q)), r(b)]]


def is_herm(A):
    k = len(A[0][0])
    realpart = lambda x: all(t == 0 for t in x[1:])
    return realpart(A[0][0]) and realpart(A[1][1]) and A[1][0] == cd_conj(A[0][1])


def coords(A):
    """real coordinates (s, zc, q...) with A = s I + zc Z + offdiag(q): s=(a+b)/2, zc=(a-b)/2."""
    a, b = A[0][0][0], A[1][1][0]
    return [(a + b) / 2, (a - b) / 2] + list(A[0][1])


def from_coords(k, v):
    s, zc, q = v[0], v[1], v[2:]
    return herm(k, s + zc, s - zc, q)


def nullity(M, rows, cols):
    """rank-nullity over Q for a rows x cols Fraction matrix (list of lists)."""
    M = [list(r) for r in M]
    rank, c = 0, 0
    for c in range(cols):
        piv = next((r for r in range(rank, rows) if M[r][c] != 0), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pv = M[rank][c]
        M[rank] = [t / pv for t in M[rank]]
        for r in range(rows):
            if r != rank and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[rank])]
        rank += 1
    return cols - rank, rank


def det(M):
    n = len(M)
    M = [list(map(Fr, r)) for r in M]
    s = Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            s = -s
        s *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return s


def linmap_matrix(f, k):
    """matrix of a real-linear map H_2(F) -> H_2(F) in coords (columns = images of coordinate basis)."""
    n = 2 + k
    cols = []
    for j in range(n):
        v = [Fr(0)] * n
        v[j] = Fr(1)
        cols.append(coords(f(from_coords(k, v))))
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def split(M):
    n = len(M)
    I = [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
    plus = nullity([[M[i][j] - I[i][j] for j in range(n)] for i in range(n)], n, n)[0]
    minus = nullity([[M[i][j] + I[i][j] for j in range(n)] for i in range(n)], n, n)[0]
    return plus, minus


ROWS = {}
Xm = lambda k: herm(k, 0, 0, unit(k, 0))
Zm = lambda k: herm(k, 1, -1, [Fr(0)] * k)
Im = lambda k: herm(k, 1, 1, [Fr(0)] * k)

for k, nm in FIELDS:
    d = 1 + k
    n = 2 + k
    # traceless orthonormal basis: Z and offdiag(e_j)
    tl = [Zm(k)] + [herm(k, 0, 0, unit(k, j)) for j in range(k)]
    I = Im(k)
    zero = m_scale(Fr(0), I)
    spin = all(jordan(tl[i], tl[j]) == (I if i == j else zero) for i in range(len(tl)) for j in range(len(tl)))
    check("B %s: H_2(%s) is the spin factor V_%d (u_i o u_j = delta_ij I on %d traceless units)" % (nm, nm, d, len(tl)),
          spin and len(tl) == d)
    X = Xm(k)
    theta = lambda A, X=X: m_mul(m_mul(X, A), X)
    # all coordinate basis elements and a few sums for the Jordan-automorphism check
    cb = [from_coords(k, [Fr(int(i == j)) for i in range(n)]) for j in range(n)]
    extra = [from_coords(k, [Fr(1, 2), Fr(1, 3)] + [Fr(j + 1, 7) for j in range(k)])]
    jaut = all(theta(jordan(A, B)) == jordan(theta(A), theta(B)) for A in cb + extra for B in cb + extra)
    herm_ok = all(is_herm(theta(A)) for A in cb)
    M = linmap_matrix(theta, k)
    inv = all(sum(M[i][l] * M[l][j] for l in range(n)) == Fr(int(i == j)) for i in range(n) for j in range(n))
    flips = coords(theta(Zm(k))) == coords(m_scale(Fr(-1), Zm(k)))
    check("B %s: level exchange theta(A) = XAX is an involutive Jordan automorphism of H_2(%s) flipping z" % (nm, nm),
          jaut and herm_ok and inv and flips)
    p_hom, m_hom = split(M)
    T = [row[1:] for row in M[1:]]            # tangent block (coords zc, q...)
    p_tan, m_tan = split(T)
    detT = det(T)
    E = [row[2:] for row in M[2:]]            # equatorial = off-diagonal block
    re_dim, im_dim = split(E)
    ROWS[nm] = dict(d=d, k=k, p_hom=p_hom, m_hom=m_hom, p_tan=p_tan, m_tan=m_tan, det=detT, re=re_dim, im=im_dim)
    check("B %s: splits homogenized (%d,%d) tangent (%d,%d) equatorial (Re,Im)=(%d,%d), det_tan=%s"
          % (nm, p_hom, m_hom, p_tan, m_tan, re_dim, im_dim, detT),
          p_hom == 2 and m_hom == k and p_tan == 1 and m_tan == k and re_dim == 1 and im_dim == k - 1)

# classical bit: diagonal algebra R+R, coordinates (s, zc); LE = swap of the two levels
M0 = [[Fr(1), Fr(0)], [Fr(0), Fr(-1)]]
ROWS["cl"] = dict(d=1, k=0, p_hom=1, m_hom=1, p_tan=0, m_tan=1, det=Fr(-1), re=0, im=0)
check("B cl: classical bit, swap of levels, homogenized split (1,1), tangent (0,1)", split(M0) == (1, 1))

# ---------------------------------------------------------------- C: the i-map
for k, nm in FIELDS:
    Z, X, I = Zm(k), Xm(k), Im(k)
    comm = [I, X]
    # anticommutant of theta inside Herm: {A : XAX = -A}
    n = 2 + k
    theta = lambda A, X=X: m_mul(m_mul(X, A), X)
    M = linmap_matrix(theta, k)
    anti_dim = split(M)[1]
    br = m_scale(Fr(1, 2), m_sub(m_mul(X, Z), m_mul(Z, X)))     # [X, Z]/2
    if k == 1:
        check("C R: [X,Z]/2 is antisymmetric, not in H_2(R); no imaginary unit; anticommutant dim %d < 2 = dim commutant"
              % anti_dim, (not is_herm(br)) and anti_dim == 1)
        continue
    imag_units = [unit(k, j) for j in range(1, k)]
    surj = []
    for u in imag_units:
        def Phi(A, u=u):
            b = m_scale(Fr(1, 2), m_sub(m_mul(A, Z), m_mul(Z, A)))
            ub = [[cd_mul(u, b[i][j]) for j in range(2)] for i in range(2)]
            return m_add(jordan(Z, A), ub)
        imgs = [Phi(A) for A in comm]
        allherm = all(is_herm(B) for B in imgs)
        anti = all(theta(B) == m_scale(Fr(-1), B) for B in imgs)
        rank = nullity([coords(B) for B in imgs], 2, 2 + k)[1]
        surj.append(allherm and anti and rank == 2 and anti_dim == 2)
        if not (allherm and anti and rank == 2):
            surj[-1] = None
    ok_maps = all(s is not None for s in surj)
    check("C %s: each of the %d imaginary units u gives Phi_u: commutant -> anticommutant (Hermitian, rank 2); "
          "anticommutant dim %d; Phi_u bijective: %s" % (nm, len(imag_units), anti_dim, any(surj)),
          ok_maps and (any(surj) == (k == 2)))

# ---------------------------------------------------------------- D: the Wigner table over C
k = 2
Xc, Zc, Ic = Xm(2), Zm(2), Im(2)
Yc = herm(2, 0, 0, (Fr(0), Fr(-1)))   # [[0,-i],[i,0]]


def m_T(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]


def full_basis():
    """real basis of M_2(C) (8 elements) for the associative-product tests."""
    out = []
    for i, j in itertools.product(range(2), range(2)):
        for c in (unit(2, 0), unit(2, 1)):
            A = [[(Fr(0), Fr(0)), (Fr(0), Fr(0))], [(Fr(0), Fr(0)), (Fr(0), Fr(0))]]
            A[i][j] = c
            out.append(A)
    return out


NOTS = {
    "Ad X (unitary)": lambda A: m_mul(m_mul(Xc, A), Xc),
    "Ad Y (unitary)": lambda A: m_mul(m_mul(Yc, A), Yc),
    "X A^T X (antiunitary)": lambda A: m_mul(m_mul(Xc, m_T(A)), Xc),
    "Y A^T Y (antiunitary, universal NOT)": lambda A: m_mul(m_mul(Yc, m_T(A)), Yc),
}
FB = full_basis()
wig = {}
for nm, f in NOTS.items():
    hom = all(f(m_mul(A, B)) == m_mul(f(A), f(B)) for A in FB for B in FB)
    antihom = all(f(m_mul(A, B)) == m_mul(f(B), f(A)) for A in FB for B in FB)
    cb = [from_coords(2, [Fr(int(i == j)) for i in range(4)]) for j in range(4)]
    jaut = all(f(jordan(A, B)) == jordan(f(A), f(B)) for A in cb for B in cb)
    M = linmap_matrix(f, 2)
    T = [row[1:] for row in M[1:]]
    flips = coords(f(Zc)) == coords(m_scale(Fr(-1), Zc))
    sp = split(M)
    wig[nm] = (hom, antihom, sp, det(T))
    print("     %-38s automorphism=%s antiautomorphism=%s Jordan-aut=%s flips z=%s det_Bloch=%s split=%s"
          % (nm, hom, antihom, jaut, flips, det(T), sp))
    check("D %s: Jordan automorphism, flips z, exactly one of aut/antiaut" % nm, jaut and flips and (hom != antihom))
check("D rule: over C a z-flipping NOT is balanced iff it is unitary (automorphism) iff det_Bloch = +1",
      all((v[2][0] == v[2][1]) == v[0] == (v[3] == 1) for v in wig.values()))

# ---------------------------------------------------------------- E: census over the spin-factor family
HURWITZ = {1: "cl", 2: "R", 3: "C", 5: "H", 9: "O"}
PAR, PARP, BLK, JOINT = set(), set(), set(), set()
for d in range(1, 14):
    for p in range(0, d):
        m = d - p                      # m_tan >= 1 (z flipped)
        bal = (1 + p == m)
        blk = p <= 1
        dt = (-1) ** m
        if bal:
            PAR.add(d)
            if dt == 1:
                PARP.add(d)
        if blk:
            BLK.add(d)
        if bal and blk:
            JOINT.add(d)
print("     PAR   =", sorted(PAR))
print("     PAR+  =", sorted(PARP))
print("     BLK   =", sorted(BLK))
print("     JOINT =", sorted(JOINT))
check("E PAR = odd d (parity alone is not field-selecting: it admits d = 5 (H), 9 (O), 7)",
      PAR == {d for d in range(1, 14) if d % 2 == 1})
check("E PAR+ = d = 3 mod 4 (parity with an orientation-preserving NOT)", PARP == {d for d in range(1, 14) if d % 4 == 3})
check("E BLK = every d (block bound alone selects no dimension, only the NOT type p_tan <= 1)", BLK == set(range(1, 14)))
check("E JOINT = {1, 3} (DIM-1's count, same N)", JOINT == {1, 3})
check("E Hurwitz: PAR meets {1,2,3,5,9} in {1,3,5,9}; PAR+ in {3}; JOINT in {1,3}; level-exchange balance in {1,3}",
      PAR & set(HURWITZ) == {1, 3, 5, 9} and PARP & set(HURWITZ) == {3} and JOINT & set(HURWITZ) == {1, 3}
      and {ROWS[HURWITZ[d]]["d"] for d in HURWITZ if ROWS[HURWITZ[d]]["p_hom"] == ROWS[HURWITZ[d]]["m_hom"]} == {1, 3})
# which constraint fails, per Hurwitz algebra, per NOT class
print("     per-field failure locus (tangent split (p_tan, m_tan): parity / block):")
for d, nm in sorted(HURWITZ.items()):
    cells = []
    for p in range(0, d):
        m = d - p
        cells.append("(%d,%d):%s/%s%s" % (p, m, "P" if 1 + p == m else "-", "B" if p <= 1 else "-",
                                          "+" if (-1) ** m == 1 else ""))
    le = ROWS[nm]
    print("       %-2s d=%d  LE=(%d,%d)  %s" % (nm, d, le["p_tan"], le["m_tan"], " ".join(cells)))

fails = [nm for nm, c in CHECKS if not c]
print("SUMMARY %d checks, %d failed" % (len(CHECKS), len(fails)))
if fails:
    print("VERDICT NOT RENDERED (a control failed)")
else:
    bal = sorted(nm for nm in ROWS if ROWS[nm]["p_hom"] == ROWS[nm]["m_hom"])
    print("VERDICT RENDERED: level-exchange NOT balanced exactly for %s; equatorial split (Re,Im) = (1,k-1) so "
          "balance <=> dim Im F = 1; over C balance <=> unitary NOT; parity alone admits %s, with det+1 %s; "
          "block alone admits every d; jointly %s"
          % (bal, sorted(PAR), sorted(PARP), sorted(JOINT)))
