"""A38 read-only discovery toolkit. Loads the landed A37 probe's head (objects, stabilizer, monomial calculus)
without running its sections, then adds the straight-line (realizability) machinery for general exponent
matrices E: SIG o u^E unitary for every unit u."""
import os, sys, itertools
import numpy as np
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(HERE, 'probe37_landed.py')).read()
_cut = _src.index("print('== 1. the census")
NS = {'__name__': 'probe37head'}
exec(compile(_src[:_cut], 'probe37head', 'exec'), NS)
for _k, _v in NS.items():
    if not _k.startswith('__'): globals()[_k] = _v

# ---- exact pair products as Gaussian integers (scaled by 65) ---------------------------------
def gint65(g):
    a, b = g.a * 65, g.b * 65
    assert a.denominator == 1 and b.denominator == 1
    return int(a), int(b)
CRE = np.zeros((16, 16, 16), dtype=np.int64); CIM = np.zeros((16, 16, 16), dtype=np.int64)
for i in range(16):
    for i2 in range(16):
        for k in range(16):
            CRE[i, i2, k], CIM[i, i2, k] = gint65(SIG[i][k] * SIG[i2][k].conj())

def subset_sums(cre, cim):
    """re[mask], im[mask] for all 2^16 column subsets"""
    re = np.zeros(1 << 16, dtype=np.int64); im = np.zeros(1 << 16, dtype=np.int64)
    for b in range(16):
        lo, hi = 1 << b, 1 << (b + 1)
        re[lo:hi] = re[:lo] + cre[b]; im[lo:hi] = im[:lo] + cim[b]
    return re, im

VAN = {}
def vanishing(i, i2):
    """boolean array over masks: the column subset sums to zero in SIG_i conj(SIG_i2)"""
    key = (i, i2)
    if key not in VAN:
        re, im = subset_sums(CRE[i, i2], CIM[i, i2]); VAN[key] = (re == 0) & (im == 0)
    return VAN[key]

def level_masks(row):
    """the level-set masks of an integer row vector, as {value: mask}"""
    out = {}
    for k, v in enumerate(row): out[v] = out.get(v, 0) | (1 << k)
    return out

def straight_line(E):
    """SIG o u^E unitary for every unit u: every level set of every pair difference has vanishing pair sum"""
    for i in range(16):
        for i2 in range(i + 1, 16):
            V = vanishing(i, i2)
            for m in level_masks([E[i][k] - E[i2][k] for k in range(16)]).values():
                if not V[m]: return False
    return True

def straight_line_direct(E):
    """control: the Laurent-polynomial identity computed with exact Gaussian rationals, no subset tables"""
    for i in range(16):
        for i2 in range(i + 1, 16):
            acc = {}
            for k in range(16):
                d = E[i][k] - E[i2][k]; acc[d] = acc.get(d, ZERO) + SIG[i][k] * SIG[i2][k].conj()
            if any(v != ZERO for v in acc.values()): return False
    return True

def gauge_normal(E):
    return [[E[i][j] - E[i][0] - E[0][j] + E[0][0] for j in range(16)] for i in range(16)]
def is_gauge_trivial(E):
    return all(x == 0 for r in gauge_normal(E) for x in r)

def W_matrix(): return [[W[i * 16 + j] for j in range(16)] for i in range(16)]

# ---- monomial calculus for a general exponent matrix ------------------------------------------
def entry_fn(E):
    def ent(i, j):
        p, q, r = SIGE[i][j]; return (E[i][j], p, q, r)
    return ent
def search_generic(E, m, n):
    ent = entry_fn(E)
    ratio = [[[gen_div(ent(i, s), ent(i, s0)) for s in range(16)] for s0 in range(16)] for i in range(16)]
    return structures(ent, gen_div, gen_mul, lambda x: x == GEN_ONE, m, n, ratio)
def search_point(E, pt, m, n):
    ent0 = entry_fn(E)
    ent = [[at_point(ent0(i, j), pt) for j in range(16)] for i in range(16)]
    def div3(a, b): return ((a[0] - b[0]) % 1, a[1] - b[1], a[2] - b[2])
    def mul3(a, b): return ((a[0] + b[0]) % 1, a[1] + b[1], a[2] + b[2])
    ratio = [[[div3(ent[i][s], ent[i][s0]) for s in range(16)] for s0 in range(16)] for i in range(16)]
    return structures(lambda i, j: ent[i][j], div3, mul3, lambda x: x == PT_ONE, m, n, ratio)

def stab_apply_E(e, E):
    """transport an exponent matrix by a stabilizer element (index permutation with sign)"""
    p, s_ = e; out = [[None] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            i2, j2 = divmod(p[i * 16 + j], 16); out[i2][j2] = s_ * E[i][j]
    return out
