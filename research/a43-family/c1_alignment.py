"""Control/test 1: the alignment question.
(a) sorted-alignment agreement: for H3, the alignment-free code restricted to sigma = sorted reproduces the frozen loci (built in).
(b) positive control: SIG with rows 7, 15 swapped is a row permutation of SIG; the correct structure count is 18. The sorted notion
    finds 12; the alignment-free notion must find 18 (and 18 at SIG).
(c) the decisive test: H3's 46 candidates, alignment-free strict and relaxed loci; is the union still the five faces?"""
import time
from align import *
t0 = time.time()
fails = []
def chk(name, got, want):
    ok = got == want; print('  %s  %-90s %s' % ('PASS' if ok else 'FAIL', name, got if ok else '%s (expected %s)' % (got, want)), flush=True)
    if not ok: fails.append(name)
def count_structures_d0(base):
    OR = orientations_d([], base); cands, _ = enumerate_candidates_d(OR, 0)
    nS = sum(1 for (f, mn, cp, rows) in cands if locus_alignfree(OR, f, mn, cp, rows, False, 0))
    nR = sum(1 for (f, mn, cp, rows) in cands if locus_alignfree(OR, f, mn, cp, rows, True, 0))
    nsort = sum(1 for (f, mn, cp, rows) in cands if solve_d(conditions_d(OR, f, mn, cp, rows, False), 0) is not None)
    return len(cands), nS, nR, nsort
S0 = [[SIGE[i][j] for j in range(16)] for i in range(16)]
sw = [S0[15] if i == 7 else S0[7] if i == 15 else S0[i] for i in range(16)]
chk('SIG: (candidates, alignment-free strict, relaxed, sorted strict)', count_structures_d0(S0)[1:], (18, 18, 18))
chk('SIG rows 7<->15: alignment-free strict and relaxed 18; sorted 12', count_structures_d0(sw)[1:], (18, 18, 12))
print('  (%.0fs)' % (time.time() - t0), flush=True)
S = summarize_alignfree([PA, PB, PC])
chk('H3: candidates', S['ncand'], 46)
chk('H3: sorted-alignment union (frozen notion) = five faces', show_union(S['union_sorted_strict']), ['u1 = -1', 'u1 = 1', 'u2 = 1', 'u3 = -1', 'u3 = 1'])
print('  H3 alignment-free strict union :', show_union(S['union_strict']))
print('  H3 alignment-free relaxed union:', show_union(S['union_relaxed']))
print('  nonempty: alignment-free strict %d, relaxed %d, sorted %d' % (S['n_nonempty_strict'], S['n_nonempty_relaxed'], S['n_nonempty_sorted']))
diff = [(k, [F.show() for F in v[0]], None if v[2] is None else v[2].show()) for k, v in S['loci'].items() if minimal_union(v[0]) != minimal_union([v[2]] if v[2] is not None else [])]
print('  candidates whose alignment-free strict locus differs from the sorted one:', len(diff))
for k, a, s in diff: print('    ', k[0], k[1], 'free:', a, ' sorted:', s)
print('  (%.0fs)' % (time.time() - t0))
print('c1:', 'FAILED %s' % fails if fails else 'OK')
