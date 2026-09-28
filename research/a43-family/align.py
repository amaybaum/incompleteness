"""Alignment-free Dita loci.

A Dita structure of shape m x n (column form) is an index map: rows <-> (a, b), columns <-> (c, d), with
H[(a,b),(c,d)] = X[a][c] D[c][b] Y_c[b][d]. Given the column blocks cp and the row classes P (the pair the probe enumerates), the
index map still carries, for every class b, the bijection sigma_b: {0..m-1} -> class b (which member plays X-row a). Ordering of d
within a block, of blocks c and of classes b is free (absorbed by Y_c, by relabelling X's columns, by D and Y's rows); a global
relabelling of a is free, so sigma_0 may be fixed (sorted). sigma_b for b >= 1 is NOT free for m >= 3 in general.

The frozen probe's `conditions` uses sigma_b = sorted order for every b. Here:
  mu_b(r, c) = H[r, col(c,0)] / H[rep_b, col(c,0)]            (rep_b = min member; valid where the proportionality holds)
  strict  : for all b >= 1 there is sigma_b with  mu_b(sigma_b(a), c) / mu_b(sigma_b(0), c) = mu_0(sigma_0(a), c)  for all a >= 1, c
  relaxed : R_b(a, c) = mu_b(sigma_b(a), c) / mu_0(sigma_0(a), c) has rank one:  R(a,c) R(0,0) = R(a,0) R(0,c)  for all a, c >= 1
Both conditions for a given b couple sigma_b(0) and sigma_b(a) only, so the locus is
  L = Prop  meet  intersection_b  union_{sigma_b} L_b(sigma_b),
computed exactly as a finite union of flats (DFS over sigma_b with pruning on empty meets)."""
import itertools
from lib43 import *

def _mono(Km, Cm, i, j): return (Km[i][j], Cm[i][j])
def _div(x, y): return (ksub(x[0], y[0]), vsub(x[1], y[1]))
def _mul(x, y): return (kadd(x[0], y[0]), vadd(x[1], y[1]))

def minimal_union(flats):
    """remove duplicates and flats contained in another"""
    fs = list(set(f for f in flats if f is not None))
    return [f for f in fs if not any(g != f and g.contains(f) for g in fs)]

def meet_unions(U, V):
    out = []
    for f in U:
        for g in V:
            h = meet_or_none_d(f, g)
            if h is not None: out.append(h)
    return minimal_union(out)

def locus_alignfree(OR, form, mn, cp, rows, relaxed, d, return_alignments=False):
    Km, Cm = OR[form]; m, n = mn
    col0 = [cp[c][0] for c in range(m)]
    # proportionality (alignment-free): every member vs the representative on every block, every d >= 1
    prop = []
    for b in range(n):
        rep = rows[b][0]
        for r in rows[b][1:]:
            for c in range(m):
                for dd in range(1, n):
                    j, j0 = cp[c][dd], cp[c][0]
                    prop.append(_div(_div(_mono(Km, Cm, r, j), _mono(Km, Cm, rep, j)), _div(_mono(Km, Cm, r, j0), _mono(Km, Cm, rep, j0))))
    F = solve_d(prop, d)
    if F is None: return []
    def mu(b, r, c): return _div(_mono(Km, Cm, r, col0[c]), _mono(Km, Cm, rows[b][0], col0[c]))
    s0 = list(rows[0])   # sigma_0 sorted
    U = [F]
    for b in range(1, n):
        members = list(rows[b])
        # pair condition flats: cond(r0, a, r) for sigma_b(0) = r0, sigma_b(a) = r
        cache = {}
        def cond(r0, a, r):
            key = (r0, a, r)
            if key in cache: return cache[key]
            eqs = []
            if not relaxed:
                for c in range(m):
                    # mu_b(r,c) / mu_b(r0,c) = mu_0(s0[a],c)   (mu_0(s0[0], c) = 1)
                    eqs.append(_div(_div(mu(b, r, c), mu(b, r0, c)), mu(0, s0[a], c)))
            else:
                def R(rr, aa, c): return _div(mu(b, rr, c), mu(0, s0[aa], c))
                for c in range(1, m):
                    eqs.append(_div(_mul(R(r, a, c), R(r0, 0, 0)), _mul(R(r, a, 0), R(r0, 0, c))))
            res = solve_d(eqs, d); cache[key] = res; return res
        Ub = []
        def dfs(a, used, r0, Fl):
            if a == m: Ub.append(Fl); return
            for r in members:
                if r in used: continue
                c_ = cond(r0, a, r)
                if c_ is None: continue
                G_ = meet_or_none_d(Fl, c_)
                if G_ is None: continue
                dfs(a + 1, used | {r}, r0, G_)
        for r0 in members:
            dfs(1, {r0}, r0, torus(d))
        Ub = minimal_union(Ub)
        U = meet_unions(U, Ub)
        if not U: return []
    return U

def sorted_alignment_locus(OR, form, mn, cp, rows, relaxed, d):
    """the frozen probe's notion (sorted alignment), for comparison"""
    return solve_d(conditions_d(OR, form, mn, cp, rows, relaxed), d)

def classify_alignfree(pieces, base=None):
    d = len(pieces)
    OR = orientations_d(pieces, base)
    cands, stats = enumerate_candidates_d(OR, d)
    loci = {}
    for key in cands:
        form, mn, cp, rows = key
        loci[key] = (locus_alignfree(OR, form, mn, cp, rows, False, d), locus_alignfree(OR, form, mn, cp, rows, True, d),
                     sorted_alignment_locus(OR, form, mn, cp, rows, False, d), sorted_alignment_locus(OR, form, mn, cp, rows, True, d))
    return OR, cands, stats, loci

def summarize_alignfree(pieces, base=None):
    OR, cands, stats, loci = classify_alignfree(pieces, base)
    allS = minimal_union([f for v in loci.values() for f in v[0]])
    allR = minimal_union([f for v in loci.values() for f in v[1]])
    sortS = minimal_union([v[2] for v in loci.values()])
    sortR = minimal_union([v[3] for v in loci.values()])
    return {'d': len(pieces), 'ncand': len(cands), 'loci': loci, 'OR': OR,
            'union_strict': sorted(allS, key=lambda F: F.B), 'union_relaxed': sorted(allR, key=lambda F: F.B),
            'union_sorted_strict': sorted(sortS, key=lambda F: F.B), 'union_sorted_relaxed': sorted(sortR, key=lambda F: F.B),
            'n_nonempty_strict': sum(1 for v in loci.values() if v[0]), 'n_nonempty_relaxed': sum(1 for v in loci.values() if v[1]),
            'n_nonempty_sorted': sum(1 for v in loci.values() if v[2] is not None),
            'all_coordinate': all(F.is_coordinate() for F in allS + allR)}
def show_union(U, names=None): return sorted(F.show(names) for F in U)
