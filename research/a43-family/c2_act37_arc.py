"""Check of act 37's arc Pu(u) = SIG o u^W under the alignment-free notion: which structures, where."""
from align import *
Wm = [[W[i * 16 + j] for j in range(16)] for i in range(16)]
S = summarize_alignfree([Wm])
print('candidates', S['ncand'])
for k, v in sorted(S['loci'].items()):
    fs, fr, ss, sr = v
    if fs or fr or ss is not None:
        print(k[0], k[1], 'strict', [F.show() for F in fs], 'relaxed', [F.show() for F in fr], 'sorted', None if ss is None else ss.show())
print('union strict', show_union(S['union_strict']), 'relaxed', show_union(S['union_relaxed']), 'sorted', show_union(S['union_sorted_strict']))
