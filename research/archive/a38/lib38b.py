"""A38 lattice machinery. Straight lines come in lattices L(Pi) fixed by the level-set partitions of every row pair;
identically-Dita lines for a census structure S form a linear subspace L_S (strict form, and the diagonal-equivalence
relaxed form). A straight lattice lies in the union of the L_S iff it lies in one of them (a Q-space is not a finite
union of proper subspaces), so a witness exists iff some straight lattice lies in no single L_S."""
from lib38 import *
import sympy

# ---- the nine column-form exact structures at SIG (row forms = the same index sets on the transpose) -----------
CENSUS9 = []
for (m, n) in SHAPES:
    for cp, rows, ok, X, Y in dita_orientations(SIG, m, n):
        if ok: CENSUS9.append(((m, n), tuple(cp), tuple(rows)))
assert len(CENSUS9) == 9 and [s[0] for s in CENSUS9].count((4, 4)) == 4
NAMES9 = {}
for s in CENSUS9:
    if s[0] == (2, 8) and s[1] == FROZEN_BLOCKS: NAMES9[s] = 't1'
_others = sorted([s for s in CENSUS9 if s not in NAMES9], key=lambda x: (SHAPES.index(x[0]), x[1]))
for s, nm in zip(_others, ('k1', 'k2', 'k3', 'k4', 'e1', 'e2', 't2', 't3')): NAMES9[s] = nm

def var(i, j): return i * 16 + j
def unit(*terms):
    v = [0] * 256
    for coef, i, j in terms: v[var(i, j)] += coef
    return v
def struct_eqs(mn, cp, rows, relaxed=False, transpose=False):
    """the linear conditions on E for SIG o u^E to admit the structure identically (column form); with transpose=True the
    conditions of the row form (the structure on E^T)."""
    m, n = mn
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    T = (lambda i, j: (j, i)) if transpose else (lambda i, j: (i, j))
    eqs = []
    for c in range(m):
        for b in range(n):
            for a in range(1, m):
                for d in range(1, n):
                    i, i2, j, j0 = row[(a, b)], row[(0, b)], col[(c, d)], col[(c, 0)]
                    eqs.append(unit((1,) + T(i, j), (-1,) + T(i2, j), (-1,) + T(i, j0), (1,) + T(i2, j0)))
    def lam(a, b, c):   # exponent of lambda(a,b,c) as a linear form
        return [(1,) + T(row[(a, b)], col[(c, 0)]), (-1,) + T(row[(0, b)], col[(c, 0)])]
    for a in range(1, m):
        for b in range(1, n):
            for c in range(m):
                if not relaxed:
                    eqs.append(unit(*(lam(a, b, c) + [(-k, i, j) for k, i, j in lam(a, 0, c)])))
                elif c > 0:
                    eqs.append(unit(*(lam(a, b, c) + [(-k, i, j) for k, i, j in lam(a, 0, c)] + [(-k, i, j) for k, i, j in lam(a, b, 0)] + lam(a, 0, 0))))
    return eqs
def gauge_eqs():
    eqs = []
    for j in range(16): eqs.append(unit((1, 0, j)))
    for i in range(1, 16): eqs.append(unit((1, i, 0)))
    return eqs

def partition_eqs(E):
    """E_i - E_i' constant on each level set of the pair difference, for every pair"""
    eqs = []
    for i in range(16):
        for i2 in range(i + 1, 16):
            for m in level_masks([E[i][k] - E[i2][k] for k in range(16)]).values():
                ks = [k for k in range(16) if (m >> k) & 1]
                for k in ks[1:]:
                    eqs.append(unit((1, i, ks[0]), (-1, i2, ks[0]), (-1, i, k), (1, i2, k)))
    return eqs

def nullspace(eqs):
    """exact rational nullspace basis (list of integer vectors) of the equation list, in the 256 variables"""
    M = sympy.Matrix(eqs)
    basis = M.nullspace()
    out = []
    for v in basis:
        den = 1
        for x in v: den = sympy.ilcm(den, sympy.Rational(x).q)
        out.append([int(x * den) for x in v])
    return out

def straight_lattice(E):
    """a basis of L(Pi_E) with the gauge fixed (row 0 = 0, column 0 = 0); every point is a straight line"""
    return nullspace(partition_eqs(E) + gauge_eqs())

STRUCT_EQS = {}
def struct_matrix(s, relaxed, transpose):
    key = (s, relaxed, transpose)
    if key not in STRUCT_EQS: STRUCT_EQS[key] = np.array(struct_eqs(s[0], s[1], s[2], relaxed, transpose), dtype=np.int64)
    return STRUCT_EQS[key]
def in_structure(vecs, s, relaxed=False, transpose=False):
    """every vector of vecs satisfies the structure's linear conditions"""
    A = struct_matrix(s, relaxed, transpose); V = np.array(vecs, dtype=np.int64)
    return not (A @ V.T).any()
def lattice_classes(basis, relaxed=False):
    """the census structures (name, form) whose L_S contains the whole lattice"""
    out = []
    for s in CENSUS9:
        for tr in (False, True):
            if in_structure(basis, s, relaxed, tr): out.append((NAMES9[s], 'row' if tr else 'column'))
    return out

def row_basis(rows):
    """fraction-free elimination: a list of integer rows spanning the same row space, linearly independent"""
    M = [r[:] for r in rows if any(r)]; m = len(M)
    if not m: return []
    n = len(M[0]); r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if M[i][c] != 0: p = i; break
        if p is None: continue
        M[r], M[p] = M[p], M[r]; piv = M[r][c]
        for i in range(r + 1, m):
            if M[i][c] != 0:
                f = M[i][c]; M[i] = [piv * x - f * y for x, y in zip(M[i], M[r])]
                g = 0
                for x in M[i]:
                    if x: g = gcd(g, x)
                if g > 1: M[i] = [x // g for x in M[i]]
        r += 1
        if r == m: break
    return M[:r]

def membership_matrix(relaxed):
    """stacked reduced equation rows of the 18 structures (9 column, 9 row) and the block offsets"""
    blocks = []; rows = []
    for s in CENSUS9:
        for tr in (False, True):
            B = row_basis(struct_eqs(s[0], s[1], s[2], relaxed, tr))
            blocks.append((NAMES9[s], 'row' if tr else 'column', len(rows), len(rows) + len(B))); rows += B
    A = np.array(rows, dtype=np.float64)
    assert np.abs(A).max() < 2 ** 40
    return A, blocks
