"""Exact verification of a candidate witness exponent matrix E."""
from lib38b import *
U5 = G(Fr(3, 5), Fr(4, 5))

def conditions_E(E, m, n, cp, rows, transpose=False):
    """every monomial condition of the structure on SIG o u^E (column form; row form on the transpose)"""
    ent0 = entry_fn(E)
    ent = (lambda i, j: ent0(j, i)) if transpose else ent0
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    out = []
    for c in range(m):
        for b in range(n):
            for a in range(m):
                for d in range(1, n):
                    i, i2, j, j0 = row[(a, b)], row[(0, b)], col[(c, d)], col[(c, 0)]
                    out.append(('prop', (i, i2, j, j0), gen_div(gen_div(ent(i, j), ent(i2, j)), gen_div(ent(i, j0), ent(i2, j0)))))
    lam = {(a, b, c): gen_div(ent(row[(a, b)], col[(c, 0)]), ent(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
    for a in range(m):
        for b in range(n):
            for c in range(m):
                out.append(('rank1', (a, b, c), gen_div(lam[(a, b, c)], gen_mul(lam[(a, 0, c)], lam[(0, b, c)]))))
    return out

def exceptional_points(E, s, transpose=False):
    """the unit points at which the census structure s is admitted by SIG o u^E: 'all', or a frozenset of canonical points"""
    (m, n), cp, rows = s
    pts = None
    for kind, idx, mm in conditions_E(E, m, n, cp, rows, transpose):
        sol = solutions(mm)
        if sol == 'all': continue
        if sol == 'none': return frozenset()
        pts = sol if pts is None else pts & sol
        if not pts: return frozenset()
    return 'all' if pts is None else pts

def obstruction_summary(E):
    """per census structure and form: 'identical' or the exceptional point set and the exponent set of its non-identity conditions"""
    out = {}
    for s in CENSUS9:
        for tr in (False, True):
            (m, n), cp, rows = s
            conds = conditions_E(E, m, n, cp, rows, tr)
            ks = sorted(set(x[2][0] for x in conds if x[2] != GEN_ONE))
            pts = exceptional_points(E, s, tr)
            out[(NAMES9[s], 'row' if tr else 'column')] = ('identical' if pts == 'all' else sorted(show_pt(p) for p in pts), ks)
    return out

def generic_counts(E):
    """(candidates, exact) by shape for the column form and the row form at a generic u"""
    ET = [list(c) for c in zip(*E)]
    return {('column', mn): tuple(len(x) for x in search_generic(E, *mn)) for mn in SHAPES} | {('row', mn): tuple(len(x) for x in search_generic(ET, *mn)) for mn in SHAPES}

def H_at(E, u): return [[SIG[i][j] * gpow(u, E[i][j]) for j in range(16)] for i in range(16)]
def numeric_counts(E, u):
    H = H_at(E, u); HT = [list(c) for c in zip(*H)]
    assert is_unitary16(H)
    return {(form, mn): (len(o), sum(1 for x in o if x[2])) for form, M in (('column', H), ('row', HT)) for mn in SHAPES for o in [dita_orientations(M, *mn)]}

def as_list(E): return [[int(E[i][j]) for j in range(16)] for i in range(16)]
def show(E): return '\n'.join(' '.join('%2d' % E[i][j] for j in range(16)) for i in range(16))
