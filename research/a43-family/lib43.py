"""a43 research library (disposable, not a certificate).

Loads the frozen act-40 probe (verification/lean/dita_torus_locus_probe.py, blob 4b718e79) as a library: its head (act 36/37/38
objects, SIG, SIGE, the monomial calculus, the 3-dim flat calculus) and its definition block (CLASSES, M_COL, M_ROW, the
3-parameter classifier), without running its numbered sections. Adds a d-parameter generalization of the flat calculus and of the
classifier, for families SIG o prod_k u_k^{P_k} with any number d of pieces, and for a general base matrix given by its exponent
table in G = <i, z, w> (so that faces u_k = -1 can be re-based at SIG o (-1)^{P_k}).

Everything asserted is exact: characters in Z^d, values in G = Z/4 x Z^2 (z, w multiplicatively independent modulo roots of
unity, so G embeds in the unit circle).
"""
import os, sys, io, contextlib, itertools
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = open(os.path.join(HERE, 'probe40_frozen_copy.py'), encoding='utf-8').read()
_NS = {'__name__': 'probe40lib'}
_head = _SRC[:_SRC.index("print('== 1. the flat calculus")]
_defs = _SRC[_SRC.index("# ---- act 37's census of SIG's Dita structures"):_SRC.index("print('== 2. completeness")]
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_head, 'probe40head', 'exec'), _NS)
    exec(compile(_defs, 'probe40defs', 'exec'), _NS)
for _k, _v in _NS.items():
    if not _k.startswith('__'): globals()[_k] = _v
P40 = _NS   # the frozen namespace (3-dim Flat, classify, ...)

# ---- d-dimensional flat calculus (the frozen calculus with range(3) -> range(d)) --------------------------------------
V0 = (0, 0, 0)
def vadd(a, b): return ((a[0] + b[0]) % 4, a[1] + b[1], a[2] + b[2])
def vsub(a, b): return ((a[0] - b[0]) % 4, a[1] - b[1], a[2] - b[2])
def vmul(n, a): return ((n * a[0]) % 4, n * a[1], n * a[2])
class EmptyD(Exception):
    pass
def hnf_d(rows, d):
    R = [[list(k), v] for k, v in rows]
    basis = []
    for col in range(d):
        while True:
            idx = [t for t in range(len(R)) if R[t][0][col] != 0]
            if len(idx) <= 1: break
            idx.sort(key=lambda t: abs(R[t][0][col]))
            pk, pv = R[idx[0]]
            for t in idx[1:]:
                f = R[t][0][col] // pk[col]
                R[t] = [[a - f * b for a, b in zip(R[t][0], pk)], vsub(R[t][1], vmul(f, pv))]
        idx = [t for t in range(len(R)) if R[t][0][col] != 0]
        if idx:
            k, v = R.pop(idx[0])
            if k[col] < 0: k = [-a for a in k]; v = vmul(-1, v)
            basis.append([k, v])
    for k, v in R:
        if any(k): raise AssertionError('reduction incomplete')
        if v != V0: raise EmptyD()
    piv = [next(c for c in range(d) if k[c] != 0) for k, v in basis]
    for a in range(len(basis)):
        pc = piv[a]; h = basis[a][0][pc]
        for b in range(a):
            f = basis[b][0][pc] // h
            if f:
                basis[b] = [[x - f * y for x, y in zip(basis[b][0], basis[a][0])], vsub(basis[b][1], vmul(f, basis[a][1]))]
    return tuple((tuple(k), v) for k, v in basis)
class FlatD:
    __slots__ = ('B', 'd')
    def __init__(self, d, rows=()): self.d = d; self.B = hnf_d(list(rows), d)
    @staticmethod
    def of(d, B):
        f = FlatD.__new__(FlatD); f.d = d; f.B = B; return f
    def __eq__(self, o): return isinstance(o, FlatD) and self.d == o.d and self.B == o.B
    def __hash__(self): return hash((self.d, self.B))
    def rank(self): return len(self.B)
    def dim(self): return self.d - len(self.B)
    def meet(self, other): return FlatD.of(self.d, hnf_d(list(self.B) + list(other.B), self.d))
    def add(self, k, v): return FlatD.of(self.d, hnf_d(list(self.B) + [(tuple(k), v)], self.d))
    def reduce(self, k, v):
        k = list(k)
        for bk, bv in self.B:
            pc = next(c for c in range(self.d) if bk[c] != 0)
            f = k[pc] // bk[pc]
            if f: k = [a - f * b for a, b in zip(k, bk)]; v = vsub(v, vmul(f, bv))
        return (tuple(k), v)
    def holds(self, k, v):
        rk, rv = self.reduce(k, v)
        return not any(rk) and rv == V0
    def contains(self, other): return all(other.holds(k, v) for k, v in self.B)
    def show(self, names=None):
        nm = names or tuple('u%d' % (t + 1) for t in range(self.d))
        def val(v):
            p, q, r = v; s = {0: '1', 1: 'i', 2: '-1', 3: '-i'}[p]
            return s + ('' if not q else ' z^%d' % q) + ('' if not r else ' w^%d' % r)
        return ', '.join('%s = %s' % ('*'.join(('%s^%d' % (nm[t], k[t]) if k[t] != 1 else nm[t]) for t in range(self.d) if k[t]), val(v)) for k, v in self.B) or 'T^%d' % self.d
    def is_coordinate(self):
        """cut out by coordinate characters u_k = +-1 alone"""
        return all(sorted(map(abs, k)) == [0] * (self.d - 1) + [1] and v in (V0, (2, 0, 0)) for k, v in self.B)
    def coord_dict(self):
        """for a coordinate flat: {k: +1 or -1}"""
        out = {}
        for k, v in self.B:
            t = next(c for c in range(self.d) if k[c]); out[t] = 1 if v == V0 else -1
        return out
def torus(d): return FlatD(d)
def meet_or_none_d(F, G):
    try: return F.meet(G)
    except EmptyD: return None

# ---- d-parameter classifier (the frozen classify with K entries in Z^d and a general base-constant table) ---------------
def ksub(a, b): return tuple(x - y for x, y in zip(a, b))
def kadd(a, b): return tuple(x + y for x, y in zip(a, b))
PAIRS2 = list(itertools.combinations(range(16), 2))
SHAPES3 = ((4, 4), (8, 2), (2, 8))
def orientations_d(pieces, base=None):
    """pieces: list of d integer 16x16 matrices; base: 16x16 table of G-values (default SIGE, i.e. SIG)"""
    Cb = base if base is not None else [[SIGE[i][j] for j in range(16)] for i in range(16)]
    K = [[tuple(P[i][j] for P in pieces) for j in range(16)] for i in range(16)]
    return {'column': (K, Cb), 'row': ([list(c) for c in zip(*K)], [list(c) for c in zip(*Cb)])}
def enumerate_candidates_d(OR, d):
    TOR = torus(d)
    cache = {}
    def pbf(vals):
        if vals in cache: return cache[vals]
        d0, e0 = vals[0]
        try:
            F = TOR
            for dd, e in vals[1:]: F = F.add(ksub(dd, d0), vsub(e0, e))
            r = F
        except EmptyD: r = None
        cache[vals] = r; return r
    cands = {}; stats = {}
    for form, (Km, Cm) in OR.items():
        de = {p: [(ksub(Km[p[0]][j], Km[p[1]][j]), vsub(Cm[p[0]][j], Cm[p[1]][j])) for j in range(16)] for p in PAIRS2}
        for m, n in SHAPES3:
            good = {}
            for Sb in itertools.combinations(range(16), n):
                loc = {}
                for p in PAIRS2:
                    F = pbf(tuple(sorted(set(de[p][j] for j in Sb))))
                    if F is not None: loc[p] = F
                def rec(rem, classes, F):
                    if not rem: good.setdefault(tuple(classes), []).append((Sb, F)); return
                    i = min(rem)
                    nb = sorted(j for j in rem if j != i and (i, j) in loc)
                    for rest in itertools.combinations(nb, m - 1):
                        cl = (i,) + rest; Gf = F
                        for a, b in itertools.combinations(cl, 2):
                            Gf = meet_or_none_d(Gf, loc[(a, b)])
                            if Gf is None: break
                        if Gf is None: continue
                        rec(rem - set(cl), classes + [cl], Gf)
                rec(frozenset(range(16)), [], TOR)
            nb0 = len(cands)
            for P, blocks in good.items():
                def cover(rem, chosen, F):
                    if not rem: cands[(form, (m, n), tuple(sorted(chosen)), P)] = F; return
                    first = min(rem)
                    for Sb, Gf in blocks:
                        if Sb[0] == first and set(Sb) <= rem:
                            Hf = meet_or_none_d(F, Gf)
                            if Hf is not None: cover(rem - set(Sb), chosen + [Sb], Hf)
                cover(frozenset(range(16)), [], TOR)
            stats[(form, (m, n))] = len(cands) - nb0
    return cands, stats
def conditions_d(OR, form, mn, cp, rows, relaxed):
    Km, Cm = OR[form]; m, n = mn
    col = {(c, dd): cp[c][dd] for c in range(m) for dd in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    def ent(i, j): return (Km[i][j], Cm[i][j])
    def div(x, y): return (ksub(x[0], y[0]), vsub(x[1], y[1]))
    def mul(x, y): return (kadd(x[0], y[0]), vadd(x[1], y[1]))
    out = []
    for c in range(m):
        for b in range(n):
            for a in range(m):
                for dd in range(1, n):
                    i, i2, j, j0 = row[(a, b)], row[(0, b)], col[(c, dd)], col[(c, 0)]
                    out.append(div(div(ent(i, j), ent(i2, j)), div(ent(i, j0), ent(i2, j0))))
    lam = {(a, b, c): div(ent(row[(a, b)], col[(c, 0)]), ent(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
    for a in range(m):
        for b in range(n):
            for c in range(m):
                if not relaxed: out.append(div(lam[(a, b, c)], mul(lam[(a, 0, c)], lam[(0, b, c)])))
                elif c > 0: out.append(div(div(lam[(a, b, c)], lam[(a, 0, c)]), div(lam[(a, b, 0)], lam[(a, 0, 0)])))
    return out
def solve_d(conds, d):
    try:
        F = torus(d)
        for k, c in conds:
            if not any(k):
                if c != V0: return None
                continue
            F = F.add(k, vsub(V0, c))
        return F
    except EmptyD:
        return None
def classify_d(pieces, base=None):
    d = len(pieces)
    OR = orientations_d(pieces, base)
    cands, stats = enumerate_candidates_d(OR, d)
    loci = {}
    for key in cands:
        form, mn, cp, rows = key
        loci[key] = (solve_d(conditions_d(OR, form, mn, cp, rows, False), d), solve_d(conditions_d(OR, form, mn, cp, rows, True), d))
    return OR, cands, stats, loci
def union_faces_d(loci_strict):
    ne = set(F for F in loci_strict.values() if F is not None)
    maximal = sorted((F for F in ne if not any(M2 != F and M2.contains(F) for M2 in ne)), key=lambda F: F.B)
    return maximal, all(any(M.contains(F) for M in maximal) for F in ne)
def summarize(pieces, base=None):
    """the whole pipeline: counts and the maximal loci, strict and relaxed separately"""
    OR, cands, stats, loci = classify_d(pieces, base)
    strict = {k: v[0] for k, v in loci.items()}; relax = {k: v[1] for k, v in loci.items()}
    mx, cov = union_faces_d(strict)
    mxr, covr = union_faces_d(relax)
    return {'d': len(pieces), 'ncand': len(cands), 'stats': stats, 'n_nonempty': sum(1 for v in strict.values() if v is not None),
            'n_nonempty_relaxed': sum(1 for v in relax.values() if v is not None),
            'strict_eq_relaxed': all(strict[k] == relax[k] for k in loci),
            'all_coordinate': all(F.is_coordinate() for F in strict.values() if F is not None),
            'maximal': mx, 'covered': cov, 'maximal_relaxed': mxr, 'covered_relaxed': covr,
            'loci': loci, 'OR': OR}

# ---- realizability ---------------------------------------------------------------------------------------------------
def base_value(base, i, j): return gval(base[i][j]) if base is not None else SIG[i][j]
def joint_realizable(pieces, base=None):
    """SIG o prod u_k^{P_k} unitary on the whole torus: every joint level set of every row-pair difference has vanishing pair sum
    (exact Gaussian rationals). Returns (n_level_sets, n_bad)."""
    bad = 0; nsets = 0
    for r in range(16):
        for s in range(r + 1, 16):
            groups = {}
            for j in range(16): groups.setdefault(tuple(M[r][j] - M[s][j] for M in pieces), []).append(j)
            for t, js in groups.items():
                nsets += 1
                tot = ZERO
                for j in js: tot = tot + base_value(base, r, j) * base_value(base, s, j).conj()
                if tot != ZERO: bad += 1
    return nsets, bad
def straight(P, base=None): return joint_realizable([P], base)[1] == 0

# ---- identical membership in a structure (the monomial conditions hold identically in u) -------------------------------
def identically_in(pieces, form, mn, cp, rows, relaxed=False, base=None):
    """the structure holds for every u: every condition has zero character and trivial value"""
    OR = orientations_d(pieces, base)
    return all(not any(k) and c == V0 for k, c in conditions_d(OR, form, mn, cp, rows, relaxed))
NAMED20 = [(nm, f, (m, n), tuple(map(tuple, cp)), tuple(map(tuple, rows))) for nm, m, n, cp, rows in CLASSES for f in ('column', 'row')]
def census_hulls(pieces, relaxed=False, base=None):
    """names (class, form) of the eighteen census structures of SIG in which the lattice spanned by the pieces lies identically"""
    return [(nm, f) for nm, f, mn, cp, rows in NAMED20 if identically_in(pieces, f, mn, cp, rows, relaxed, base)]

# ---- base re-basing at a sign point -------------------------------------------------------------------------------------
def rebase(pieces, signs, base=None):
    """substitute u_k = signs[k] (in {1, -1, None}) and return (remaining pieces, new base table)"""
    Cb = [row[:] for row in (base if base is not None else [[SIGE[i][j] for j in range(16)] for i in range(16)])]
    rem = []
    for P, s in zip(pieces, signs):
        if s is None: rem.append(P); continue
        if s == -1:
            for i in range(16):
                for j in range(16):
                    if P[i][j] % 2: Cb[i][j] = vadd(Cb[i][j], (2, 0, 0))
    return rem, Cb
def all_structures_of_base(base):
    """every Dita structure (form, shape, blocks, classes) of the constant matrix given by the G-table base, exactly
    (the d = 0 classifier: a structure is a candidate with a nonempty = full locus)"""
    OR = orientations_d([], base)
    cands, stats = enumerate_candidates_d(OR, 0)
    out = []
    for key in cands:
        form, mn, cp, rows = key
        if solve_d(conditions_d(OR, form, mn, cp, rows, False), 0) is not None: out.append(key)
    return out

def mat(f): return [[f(i, j) for j in range(16)] for i in range(16)]
def madd_(*Ms): return [[sum(M[i][j] for M in Ms) for j in range(16)] for i in range(16)]
