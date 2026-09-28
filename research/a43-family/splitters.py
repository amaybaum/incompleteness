"""Splitters of a {0,1} straight line E: the 0/1 matrices P <= E (sub-supports) with {P, E - P} jointly realizable, i.e.
SIG o u^P v^(E-P) unitary for all (u, v) on the 2-torus. Every piece of a jointly realizable decomposition E = sum_k P_k (disjoint
0/1 supports) is a splitter (specialize all other parameters to one common value), so every such decomposition is a coarsening of
the partition of supp(E) into the atoms of the splitter family (cells equivalent iff every splitter contains both or neither).

Exact: the vanishing tables are exact integer subset sums of 65 * SIG_r conj(SIG_s) (Gaussian integers after scaling)."""
import numpy as np, itertools
from lib43 import *

def gint65(g):
    a, b = g.a * 65, g.b * 65
    assert a.denominator == 1 and b.denominator == 1
    return int(a), int(b)
_VAN = {}
def van(r, s):
    if (r, s) not in _VAN:
        cre = [gint65(SIG[r][k] * SIG[s][k].conj())[0] for k in range(16)]
        cim = [gint65(SIG[r][k] * SIG[s][k].conj())[1] for k in range(16)]
        re = np.zeros(1 << 16, dtype=np.int64); im = np.zeros(1 << 16, dtype=np.int64)
        for b in range(16):
            lo, hi = 1 << b, 1 << (b + 1)
            re[lo:hi] = re[:lo] + cre[b]; im[lo:hi] = im[:lo] + cim[b]
        _VAN[(r, s)] = (re == 0) & (im == 0)
    return _VAN[(r, s)]

def row_mask(row): return sum(1 << k for k, x in enumerate(row) if x)
def submasks(m):
    out = []; s = m
    while True:
        out.append(s)
        if s == 0: break
        s = (s - 1) & m
    return np.array(sorted(out), dtype=np.int64)

def pair_table(E, r, s, opts_r, opts_s, extra=()):
    """bool[len(opts_r), len(opts_s)]: all joint level sets of (P_r - P_s, E_r - E_s, extra pieces' differences) vanish.
    extra: list of fixed 0/1 matrices whose differences also label the level sets (used for refining a known family)."""
    V = van(r, s); FULL = (1 << 16) - 1
    er, es = row_mask(E[r]), row_mask(E[s])
    # E-level masks (E in {0,1}): +1 on er & ~es, -1 on es & ~er, 0 elsewhere
    elev = [er & ~es & FULL, es & ~er & FULL, FULL & ~((er & ~es) | (es & ~er))]
    # refine by extra pieces
    for X in extra:
        xr, xs = row_mask(X[r]), row_mask(X[s])
        xl = [xr & ~xs & FULL, xs & ~xr & FULL, FULL & ~((xr & ~xs) | (xs & ~xr))]
        elev = [a & b for a in elev for b in xl]
    elev = [m for m in elev if m]
    pr = opts_r[:, None]; ps = opts_s[None, :]
    plev = [pr & ~ps, ps & ~pr, FULL & ~((pr & ~ps) | (ps & ~pr))]
    ok = np.ones((len(opts_r), len(opts_s)), dtype=bool)
    for em in elev:
        for pm in plev:
            ok &= V[pm & em]
    return ok

def unary_filter(E, r, opts):
    """necessary unary conditions (E in {0,1}): for every s, p_r restricted to (e_r minus e_s) is a vanishing set of the pair (r, s)
    (the E-level set +1 of (r, s) splits by P into p_r and its complement, both must vanish; the whole vanishes)"""
    er = row_mask(E[r]); keep = np.ones(len(opts), dtype=bool)
    for s in range(16):
        if s == r: continue
        es = row_mask(E[s]); V = van(r, s) if r < s else van(s, r)
        # van(s, r) is the conjugate pair; vanishing is conjugation-invariant, so either table serves
        keep &= V[opts & (er & ~es)]
    return opts[keep]
def splitters(E, extra=(), limit=10 ** 6):
    """all splitters P <= E, as tuples of 16 row masks (arc-consistent backtracking over rows)"""
    opts = [unary_filter(E, r, submasks(row_mask(E[r]))) if not extra else submasks(row_mask(E[r])) for r in range(16)]
    T = {}
    for r in range(16):
        for s in range(r + 1, 16):
            T[(r, s)] = pair_table(E, r, s, opts[r], opts[s], extra)
    def tab(a, b): return T[(a, b)] if a < b else T[(b, a)].T
    sols = []
    cur = [0] * 16
    def rec(dom, free):
        if len(sols) >= limit: return
        if not free:
            sols.append(tuple(cur)); return
        i = min(free, key=lambda r: int(dom[r].sum()))
        rest = [r for r in free if r != i]
        for n in np.flatnonzero(dom[i]):
            newdom = {}; ok = True
            for r in rest:
                dd = dom[r] & tab(i, r)[n]
                if not dd.any(): ok = False; break
                newdom[r] = dd
            if not ok: continue
            cur[i] = int(opts[i][n]); rec(newdom, rest)
    rec({r: np.ones(len(opts[r]), dtype=bool) for r in range(16)}, list(range(16)))
    return sols

def mask_to_mat(masks): return [[(masks[r] >> k) & 1 for k in range(16)] for r in range(16)]
def atoms(E, sols):
    """the partition of supp(E) into atoms of the splitter family"""
    cells = [(r, k) for r in range(16) for k in range(16) if E[r][k]]
    sig = {}
    for c in cells:
        key = tuple((P[c[0]] >> c[1]) & 1 for P in sols)
        sig.setdefault(key, []).append(c)
    return sorted(sig.values())
def cells_to_mat(cells):
    M = [[0] * 16 for _ in range(16)]
    for r, k in cells: M[r][k] = 1
    return M
