"""A41 census research toolkit (read-only research; not a probe of any round).

Loads the landed act-38 probe head (verification/lean/dita_local_escape_probe.py at D41, up to its section 1) for the
shared exact objects: SIG = F4(z) (x) F4(w) scaled by 4, the stabilizer `elems` (1024 index permutations with sign),
SIGE monomial exponents, the structure search. Adds: exact vanishing subset tables, the census structures' linear
membership conditions (strict and relaxed; the construction of the a38 discovery toolkit, reimplemented here), and the
reference (Python) canonical form under gauge x stabilizer x sign."""
import os, sys, itertools
import numpy as np
from fractions import Fraction as Fr
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
_src = open(os.path.join(ROOT, 'verification', 'lean', 'dita_local_escape_probe.py')).read()
_cut = _src.index("print('== 1. realizability")
NS = {'__name__': 'probe38head'}
exec(compile(_src[:_cut], 'probe38head', 'exec'), NS)
for _k, _v in NS.items():
    if not _k.startswith('__'): globals()[_k] = _v
assert not fails

# ---- exact pair products as Gaussian integers (SIG scaled by 4 has entries i^p z^q w^r; products scaled by 65) ----
def gint65(g):
    a, b = g.a * 65, g.b * 65
    assert a.denominator == 1 and b.denominator == 1
    return int(a), int(b)
CRE = [[[0] * 16 for _ in range(16)] for _ in range(16)]; CIM = [[[0] * 16 for _ in range(16)] for _ in range(16)]
for i in range(16):
    for i2 in range(16):
        for k in range(16):
            CRE[i][i2][k], CIM[i][i2][k] = gint65(SIG[i][k] * SIG[i2][k].conj())

def vanishing_table(i, i2):
    """bytes over the 2^16 column masks: 1 iff sum_{k in mask} SIG_ik conj(SIG_i2k) == 0 (exact integers)"""
    re = np.zeros(1 << 16, dtype=np.int64); im = np.zeros(1 << 16, dtype=np.int64)
    for b in range(16):
        lo, hi = 1 << b, 1 << (b + 1)
        re[lo:hi] = re[:lo] + CRE[i][i2][b]; im[lo:hi] = im[:lo] + CIM[i][i2][b]
    return ((re == 0) & (im == 0)).astype(np.uint8)

def straight_line_direct(E):
    """SIG o u^E unitary for every unit u, as the Laurent-polynomial identity in exact Gaussian rationals"""
    for i in range(16):
        for i2 in range(i + 1, 16):
            acc = {}
            for k in range(16):
                d = E[i][k] - E[i2][k]; acc[d] = acc.get(d, ZERO) + SIG[i][k] * SIG[i2][k].conj()
            if any(v != ZERO for v in acc.values()): return False
    return True

# ---- census structures and linear membership conditions ----------------------------------------------------
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

def unit(*terms):
    v = [0] * 256
    for coef, i, j in terms: v[i * 16 + j] += coef
    return v
def struct_eqs(mn, cp, rows, relaxed=False, transpose=False):
    """linear conditions on E for SIG o u^E to admit the structure identically in u (column form; transpose=True: the
    row form, i.e. the structure on the transpose)"""
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
    def lam(a, b, c):
        return [(1,) + T(row[(a, b)], col[(c, 0)]), (-1,) + T(row[(0, b)], col[(c, 0)])]
    for a in range(1, m):
        for b in range(1, n):
            for c in range(m):
                if not relaxed:
                    eqs.append(unit(*(lam(a, b, c) + [(-k, i, j) for k, i, j in lam(a, 0, c)])))
                elif c > 0:
                    eqs.append(unit(*(lam(a, b, c) + [(-k, i, j) for k, i, j in lam(a, 0, c)] + [(-k, i, j) for k, i, j in lam(a, b, 0)] + lam(a, 0, 0))))
    return eqs
STRUCTS18 = [(NAMES9[s], 'row' if tr else 'column', s, tr) for s in CENSUS9 for tr in (False, True)]
EQS = {(nm, form, rel): struct_eqs(s[0], s[1], s[2], rel, tr) for nm, form, s, tr in STRUCTS18 for rel in (False, True)}
def members(E, relaxed):
    """the census structures (name, form) whose linear conditions E satisfies (exact integers)"""
    flat = [E[i][j] for i in range(16) for j in range(16)]
    out = []
    for nm, form, s, tr in STRUCTS18:
        if all(sum(c * x for c, x in zip(eq, flat) if c) == 0 for eq in EQS[(nm, form, relaxed)]): out.append((nm, form))
    return out

# ---- the group: gauge x stabilizer x sign ------------------------------------------------------------------
# g = (perm, s) acts on a 16x16 integer matrix by (g.E)[perm[t]] = s * E[t] on flattened positions t = 16 i + j.
def act(g, E):
    p, s = g; out = [0] * 256
    for t in range(256): out[p[t]] = s * E[t // 16][t % 16]
    return [out[16 * i:16 * i + 16] for i in range(16)]
def gnorm(E):
    return [[E[i][j] - E[i][0] - E[0][j] + E[0][0] for j in range(16)] for i in range(16)]
GROUP = [(p, s) for p, s in elems] + [(p, -s) for p, s in elems]
def canon_ref(E):
    """lexicographic minimum (row-major, 256 entries) of the gauge normal forms of the 2048 images eps.g.E"""
    return min(tuple(x for r in gnorm(act(g, E)) for x in r) for g in GROUP)

# ---- numpy canonical form (independent of the C early-exit implementation: full images, lexsort) ------------
PERM_ARR = np.array([p for p, s in GROUP], dtype=np.int64)
SIGN_ARR = np.array([s for p, s in GROUP], dtype=np.int64)
INV_ARR = np.argsort(PERM_ARR, axis=1)          # image[t] = s * E[INV[t]]
def images_gn(E):
    flat = np.asarray(E, dtype=np.int64).reshape(256)
    imgs = (flat[INV_ARR] * SIGN_ARR[:, None]).reshape(-1, 16, 16)
    imgs = imgs - imgs[:, :, :1] - imgs[:, :1, :] + imgs[:, :1, :1]
    return imgs.reshape(-1, 256)
def canon_np(E):
    fl = images_gn(E)
    order = np.lexsort(fl.T[::-1])
    return tuple(int(x) for x in fl[order[0]])

# ---- the orbit table written by census41 (state.bin) ----------------------------------------------------------
REC_DTYPE = np.dtype([('key', '<u8', 11), ('first', '<u2', 16), ('n_sol', '<u8'), ('n_gauge', '<u8'), ('n_strict', '<u8'),
                      ('n_hrep', '<u8'), ('relmask_canon', '<u4'), ('strictmask_union', '<u4'), ('min_dsupp', '<u2'),
                      ('canon_nnz', '<u2'), ('min_gn_nnz', '<u2'), ('orbit_gauge', '<u2'), ('used', 'u1'), ('pad', 'u1', 7)])
assert REC_DTYPE.itemsize == 176
HDR_NAMES = ['magic', 'next_branch', 'b_end', 'n_orbits', 'sol', 'gauge', 'hrep', 'strict', 'relaxonly_sol', 'non_sol',
             'ctrl_relax_mismatch', 'ctrl_canon_not_idemp', 'ctrl_canon_checked', 'nodes', 'x', 'y']
def load_table(path):
    raw = open(path, 'rb').read()
    hdr = dict(zip(HDR_NAMES, np.frombuffer(raw[:128], dtype='<u8').tolist()))
    recs = np.frombuffer(raw[128:], dtype=REC_DTYPE)
    assert len(recs) == hdr['n_orbits']
    return hdr, recs
def decode_keys(keys):
    """(n, 11) uint64 -> (n, 16, 16) int8 canonical gauge normal forms"""
    n = len(keys); out = np.zeros((n, 16, 16), dtype=np.int8)
    k = keys.astype(np.uint64)
    for p in range(225):
        b = 3 * p; w, o = b >> 6, b & 63
        v = (k[:, w] >> np.uint64(o)) & np.uint64(7)
        if o > 61: v = v | ((k[:, w + 1] << np.uint64(64 - o)) & np.uint64(7))
        out[:, 1 + p // 15, 1 + p % 15] = v.astype(np.int8) - 2
    return out
def first_matrix(first):
    return [[(int(first[i]) >> j) & 1 if i > 0 else 0 for j in range(16)] for i in range(16)]
