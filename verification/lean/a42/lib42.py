"""A42 support-minimality research toolkit (read-only research; not a certificate).
Loads the head (objects, stabilizer, monomial calculus) of the landed act-37 probe
verification/lean/dita_arc_exclusivity_probe.py without running its sections, and adds:
exact column-subset vanishing tables for every row pair of SIG, the straight-line test, the
18 census membership subspaces (strict and relaxed), and the stabilizer action on exponent matrices."""
import os, sys, itertools
import numpy as np
from fractions import Fraction as Fr
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
_src = open(os.path.join(REPO, 'verification', 'lean', 'dita_arc_exclusivity_probe.py')).read()
_cut = _src.index("print('== 1. the census")
NS = {'__name__': 'probe37head'}
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src[:_cut], 'probe37head', 'exec'), NS)
for _k, _v in NS.items():
    if not _k.startswith('__'): globals()[_k] = _v
assert not fails

FULL = (1 << 16) - 1
# pair products SIG_ik conj(SIG_i'k), scaled by 16*65/16: exact Gaussian integers after scaling by 65
def gint65(g):
    a, b = g.a * 65, g.b * 65
    assert a.denominator == 1 and b.denominator == 1
    return int(a), int(b)
CRE = np.zeros((16, 16, 16), dtype=np.int64); CIM = np.zeros((16, 16, 16), dtype=np.int64)
for _i in range(16):
    for _i2 in range(16):
        for _k in range(16):
            CRE[_i, _i2, _k], CIM[_i, _i2, _k] = gint65(SIG[_i][_k] * SIG[_i2][_k].conj())

def subset_sums(cre, cim):
    re = np.zeros(1 << 16, dtype=np.int64); im = np.zeros(1 << 16, dtype=np.int64)
    for b in range(16):
        lo, hi = 1 << b, 1 << (b + 1)
        re[lo:hi] = re[:lo] + cre[b]; im[lo:hi] = im[:lo] + cim[b]
    return re, im

VAN = {}
def vanishing(i, i2):
    """bool array over the 2^16 column masks: the subset sums to zero in SIG_i o conj(SIG_i2)"""
    key = (min(i, i2), max(i, i2))
    if key not in VAN:
        re, im = subset_sums(CRE[key[0], key[1]], CIM[key[0], key[1]]); VAN[key] = (re == 0) & (im == 0)
    return VAN[key]

def level_masks(vec):
    out = {}
    for k, v in enumerate(vec): out[v] = out.get(v, 0) | (1 << k)
    return out

def straight(E):
    """SIG o u^E is complex Hadamard for every unit u (Laurent identity), via the exact subset tables"""
    for i in range(16):
        for i2 in range(i + 1, 16):
            V = vanishing(i, i2)
            for m in level_masks([E[i][k] - E[i2][k] for k in range(16)]).values():
                if not V[m]: return False
    return True

def straight_direct(E):
    """independent control: the Laurent identity with exact Gaussian rationals, no tables"""
    for i in range(16):
        for i2 in range(i + 1, 16):
            acc = {}
            for k in range(16):
                d = E[i][k] - E[i2][k]; acc[d] = acc.get(d, ZERO) + SIG[i][k] * SIG[i2][k].conj()
            if any(v != ZERO for v in acc.values()): return False
    return True

def support(E): return sum(1 for r in E for x in r if x)

# ---- census structures and the linear membership conditions (as in the a38 toolkit) -----------------
CENSUS9 = []
for (m, n) in SHAPES:
    for cp, rows, ok, X, Y in dita_orientations(SIG, m, n):
        if ok: CENSUS9.append(((m, n), tuple(cp), tuple(rows)))
assert len(CENSUS9) == 9
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

STRUCTS = [(NAMES9[s], tr, s) for s in CENSUS9 for tr in (False, True)]   # 18 = 9 column + 9 row forms
SMAT = {(nm, tr, rel): np.array(struct_eqs(s[0], s[1], s[2], rel, tr), dtype=np.int64) for nm, tr, s in STRUCTS for rel in (False, True)}

def memberships(E, relaxed):
    """the census structures (name, form) whose linear conditions E satisfies (strict or relaxed form)"""
    v = np.array(E, dtype=np.int64).reshape(256)
    return [(nm, 'row' if tr else 'col') for nm, tr, s in STRUCTS if not (SMAT[(nm, tr, relaxed)] @ v).any()]
def is_dita(E):
    """in some census subspace, strict or relaxed (strict is contained in relaxed; both tested)"""
    return bool(memberships(E, False)) or bool(memberships(E, True))

# ---- stabilizer on exponent matrices ------------------------------------------------------------
def stab_apply(e, E):
    p, s_ = e; out = [[None] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            i2, j2 = divmod(p[i * 16 + j], 16); out[i2][j2] = s_ * E[i][j]
    return out

def mat(f): return [[f(i, j) for j in range(16)] for i in range(16)]
def EA(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if (a % 2 == 1 and b == 3 and c % 2 == 1) else 0
def EB(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if (a == 2 and d == 1) else 0
def EC(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if ((a + b) % 2 == 1 and (c, d) in ((0, 2), (2, 0))) else 0
A38, B38, C38 = mat(EA), mat(EB), mat(EC)
WIT38 = [[A38[i][j] + B38[i][j] + C38[i][j] for j in range(16)] for i in range(16)]
WMAT = [[W[i * 16 + j] for j in range(16)] for i in range(16)]
