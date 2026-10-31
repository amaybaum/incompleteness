"""Exact GF(2) arithmetic: polynomials as Python ints, linear algebra on packed integer arrays.

Polynomials over GF(2) are ints, bit i the coefficient of z^i. Vectors over GF(2) are ints or
packed uint64 numpy arrays. Nothing here uses floating point.
"""
import numpy as np

# PLAN.md §1, polynomial table: exponents present in p_n and p'_n.
P_EXPS = {3: (3, 1, 0), 4: (4, 1, 0), 5: (5, 2, 0), 6: (6, 1, 0), 7: (7, 1, 0), 8: (8, 4, 3, 2, 0)}
PR_EXPS = {3: (3, 2, 0), 4: (4, 3, 0), 5: (5, 3, 0), 6: (6, 5, 0), 7: (7, 6, 0), 8: (8, 6, 5, 4, 0)}


def poly(exps):
    v = 0
    for e in exps:
        v |= 1 << e
    return v


def deg(p):
    return p.bit_length() - 1


def pmulmod(a, b, m):
    """a*b mod m over GF(2)."""
    d = deg(m)
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if (a >> d) & 1:
            a ^= m
    return r


def order_of_z(p):
    """Multiplicative order of z modulo p (degree >= 2, p(0) = 1), or None if z is not a unit."""
    d = deg(p)
    if d < 2 or not p & 1:
        return None
    x, k = 2, 1
    while x != 1:
        x = pmulmod(x, 2, p)
        k += 1
        if k > (1 << d):
            return None
    return k


def is_primitive(p):
    return order_of_z(p) == (1 << deg(p)) - 1


def reciprocal(p):
    d = deg(p)
    r = 0
    for i in range(d + 1):
        if (p >> i) & 1:
            r |= 1 << (d - i)
    return r


def primitive_polys(n):
    """All primitive polynomials of degree n, ascending by integer encoding."""
    return [p for p in range((1 << n) | 1, 1 << (n + 1), 2) if is_primitive(p)]


def euler_phi(k):
    r, m, q = k, k, 2
    while q * q <= m:
        if m % q == 0:
            while m % q == 0:
                m //= q
            r -= r // q
        q += 1
    if m > 1:
        r -= r // m
    return r


def parity(v):
    return bin(v).count("1") & 1


def poly_str(p):
    terms = []
    for i in range(deg(p), -1, -1):
        if (p >> i) & 1:
            terms.append("1" if i == 0 else ("z" if i == 1 else "z^%d" % i))
    return "+".join(terms)


# ---------- dense GF(2) linear algebra on Python-int rows ----------

def rank_int_rows(rows):
    """Rank of a list of int bit-rows, by elimination with a pivot dictionary."""
    piv = {}
    r = 0
    for v in rows:
        while v:
            h = v.bit_length() - 1
            if h in piv:
                v ^= piv[h]
            else:
                piv[h] = v
                r += 1
                break
    return r


def matrix_rank_cols(cols, n):
    """Rank of an n-row matrix given as a list of column bitmasks."""
    return rank_int_rows(cols)


# ---------- packed numpy GF(2) elimination ----------

def pack_rows(bits):
    """bits: (rows, cols) uint8 0/1 array -> (rows, words) uint64, column j at word j//64 bit j%64."""
    rows, cols = bits.shape
    words = (cols + 63) // 64
    pad = words * 64 - cols
    if pad:
        bits = np.concatenate([bits, np.zeros((rows, pad), dtype=np.uint8)], axis=1)
    b = bits.reshape(rows, words, 64).astype(np.uint64)
    shifts = np.arange(64, dtype=np.uint64)
    return np.bitwise_or.reduce(b << shifts, axis=2)


def rref_packed(A, ncols, max_rank=None):
    """Reduced row echelon form over GF(2) of a packed matrix (rows, words), in place on a copy.

    Returns (R, pivots) where R holds the rank nonzero rows in RREF order and pivots[i] is the
    pivot column of row i. If max_rank is given and the rank reaches it, elimination stops early
    (the returned rank is then exactly max_rank, and R is in RREF on the pivot columns found).
    """
    A = A.copy()
    rows = A.shape[0]
    pivots = []
    r = 0
    one = np.uint64(1)
    for c in range(ncols):
        if r == rows:
            break
        w, b = divmod(c, 64)
        mask = one << np.uint64(b)
        col = (A[r:, w] & mask) != 0
        idx = np.flatnonzero(col)
        if idx.size == 0:
            continue
        p = r + int(idx[0])
        if p != r:
            A[[r, p]] = A[[p, r]]
        hit = (A[:, w] & mask) != 0
        hit[r] = False
        if hit.any():
            A[hit] ^= A[r]
        pivots.append(c)
        r += 1
        if max_rank is not None and r >= max_rank:
            break
    return A[:r], pivots


def nullspace_from_rref(R, pivots, ncols):
    """Basis of {c : M c = 0} as a list of Python ints (bit j = coefficient of column j)."""
    pivset = set(pivots)
    free = [j for j in range(ncols) if j not in pivset]
    rows_int = [packed_row_to_int(R[i]) for i in range(len(pivots))]
    basis = []
    for j in free:
        v = 1 << j
        for i, pc in enumerate(pivots):
            if (rows_int[i] >> j) & 1:
                v |= 1 << pc
        basis.append(v)
    return basis


def packed_row_to_int(row):
    v = 0
    for k, w in enumerate(row.tolist()):
        v |= int(w) << (64 * k)
    return v


def int_to_bits(v, n):
    return [(v >> i) & 1 for i in range(n)]
