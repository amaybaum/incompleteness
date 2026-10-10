"""Thread P helper library: exact rational linear algebra (Fraction only, no floats)."""
from fractions import Fraction as F
from itertools import combinations


def fr(x):
    return x if isinstance(x, F) else F(x)


def rank(rows):
    """Exact rank of a list of row vectors (Fractions)."""
    m = [[fr(a) for a in r] for r in rows]
    if not m:
        return 0
    ncol = len(m[0])
    r = 0
    for c in range(ncol):
        piv = None
        for i in range(r, len(m)):
            if m[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [a / pv for a in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        r += 1
        if r == len(m):
            break
    return r


def nullspace(rows, ncol):
    """Exact basis of {v : rows v = 0}."""
    m = [[fr(a) for a in r] for r in rows]
    pivcols = []
    r = 0
    for c in range(ncol):
        piv = None
        for i in range(r, len(m)):
            if m[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [a / pv for a in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        pivcols.append(c)
        r += 1
        if r == len(m):
            break
    free = [c for c in range(ncol) if c not in pivcols]
    basis = []
    for fc in free:
        v = [F(0)] * ncol
        v[fc] = F(1)
        for i, pc in enumerate(pivcols):
            v[pc] = -m[i][fc]
        basis.append(v)
    return basis


def affine_dim(points):
    if not points:
        return -1
    p0 = points[0]
    return rank([[fr(a) - fr(b) for a, b in zip(p, p0)] for p in points[1:]]) if len(points) > 1 else 0


def solve(A, b):
    """Solve square-or-overdetermined consistent system A x = b exactly; returns one solution or None."""
    n = len(A[0])
    m = [[fr(a) for a in row] + [fr(bb)] for row, bb in zip(A, b)]
    pivcols = []
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, len(m)):
            if m[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [a / pv for a in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * bb for a, bb in zip(m[i], m[r])]
        pivcols.append(c)
        r += 1
    for i in range(r, len(m)):
        if m[i][n] != 0:
            return None
    x = [F(0)] * n
    for i, pc in enumerate(pivcols):
        x[pc] = m[i][n]
    return x


def barycentric(verts, p):
    """Barycentric coordinates of p w.r.t. affinely independent verts (None if not in affine span)."""
    k = len(verts)
    dim = len(p)
    A = [[fr(verts[j][i]) for j in range(k)] for i in range(dim)] + [[F(1)] * k]
    b = [fr(a) for a in p] + [F(1)]
    return solve(A, b)


def is_simplex_hull(points):
    """Is conv(points) a simplex?  Exhaustive: a simplex hull has its vertices among the points;
    search all (affdim+1)-subsets that are affinely independent and contain every point
    with nonnegative barycentric coordinates.  Returns (bool, vertex subset or None)."""
    pts = []
    for p in points:
        t = tuple(fr(a) for a in p)
        if t not in pts:
            pts.append(t)
    k = affine_dim(pts)
    for sub in combinations(range(len(pts)), k + 1):
        vs = [pts[i] for i in sub]
        if affine_dim(vs) != k:
            continue
        ok = True
        for p in pts:
            bc = barycentric(vs, p)
            if bc is None or any(c < 0 for c in bc):
                ok = False
                break
        if ok:
            return True, vs
    return False, None


def eig_blocks(rays):
    """Linear maps M on R^n having every given vector as an eigenvector: solve M r_k = lam_k r_k,
    linear in the unknowns (M entries, lam_k).  Returns (dimension of solution space, blocks), where
    rays i, j share a block iff lam_i = lam_j on every solution."""
    n = len(rays[0])
    K = len(rays)
    nv = n * n + K
    rows = []
    for k, r in enumerate(rays):
        for i in range(n):
            row = [F(0)] * nv
            for j in range(n):
                row[i * n + j] = fr(r[j])
            row[n * n + k] = -fr(r[i])
            rows.append(row)
    ns = nullspace(rows, nv)
    blocks = []
    for k in range(K):
        sig = tuple(v[n * n + k] for v in ns)
        for b in blocks:
            if b[0] == sig:
                b[1].append(k)
                break
        else:
            blocks.append((sig, [k]))
    return len(ns), [b[1] for b in blocks]


def hom(x):
    return [F(1)] + [fr(a) for a in x]
