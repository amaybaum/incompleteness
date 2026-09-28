"""Stage 5: alignment-free (general index map) Dita loci of the essential atom family of every orbit, strict and relaxed, with the
sorted-alignment (frozen act-40 notion) loci alongside; per-orbit checkpoints. Also the one-parameter witness line (K7)."""
import time, pickle, sys
from splitters import *
from align import *
t0 = time.time()
d = pickle.load(open(os.path.join(HERE, 'orbits.pkl'), 'rb')); Es, recs = d['Es'], d['recs']
AT = pickle.load(open(os.path.join(HERE, 'atoms.pkl'), 'rb'))
CK = os.path.join(HERE, 'loci_af.pkl')
try: done = pickle.load(open(CK, 'rb'))
except Exception: done = {}
which = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else range(len(recs))
def is_gauge_atom(cells):
    rows = set(r for r, k in cells); cols = set(k for r, k in cells)
    return (len(rows) == 1 and len(cols) == 16) or (len(cols) == 1 and len(rows) == 16)
def shape(cells): return (len(set(r for r, k in cells)), len(set(k for r, k in cells)))
def Bs(U): return sorted(F.B for F in U)
for t in which:
    if t in done: continue
    r = recs[t]
    mem = min((i for i in r['members'] if AT[i]['joint'][1] == 0), key=lambda i: (len(AT[i]['atoms']), Es[i]))
    at = AT[mem]['atoms']
    ess = [a for a in at if not is_gauge_atom(a)]
    Ms = [cells_to_mat(a) for a in ess]
    t1 = time.time()
    S = summarize_alignfree(Ms)
    Eess = madd_(*Ms)
    S1 = summarize_alignfree([Eess])
    rec = {'orbit': t, 'member': mem, 'natoms': len(at), 'ngauge': len(at) - len(ess), 'atoms': ess, 'shapes': [shape(a) for a in ess],
           'hulls': [census_hulls([M]) for M in Ms],
           'loo_hulls': [census_hulls([M for j, M in enumerate(Ms) if j != k]) for k in range(len(Ms))],
           'ncand': S['ncand'], 'n_nonempty_strict': S['n_nonempty_strict'], 'n_nonempty_relaxed': S['n_nonempty_relaxed'], 'n_nonempty_sorted': S['n_nonempty_sorted'],
           'U_strict': Bs(S['union_strict']), 'U_relaxed': Bs(S['union_relaxed']), 'U_sorted': Bs(S['union_sorted_strict']), 'U_sorted_relaxed': Bs(S['union_sorted_relaxed']),
           'show_strict': show_union(S['union_strict']), 'show_relaxed': show_union(S['union_relaxed']), 'show_sorted': show_union(S['union_sorted_strict']),
           'show_sorted_relaxed': show_union(S['union_sorted_relaxed']),
           'loci': {k: ([F.B for F in v[0]], [F.B for F in v[1]], None if v[2] is None else v[2].B, None if v[3] is None else v[3].B) for k, v in S['loci'].items()},
           'line': {'show_strict': show_union(S1['union_strict']), 'show_relaxed': show_union(S1['union_relaxed']), 'show_sorted': show_union(S1['union_sorted_strict'])},
           'secs': time.time() - t1}
    done[t] = rec
    pickle.dump(done, open(CK, 'wb'))
    print('orbit %2d m%3d d=%d g%d %s cand %d ne(s/r/sorted) %d/%d/%d\n   strict  %s\n   relaxed %s\n   sorted  %s | sorted-relaxed %s\n   line strict %s relaxed %s sorted %s  %.0fs' % (
        t, mem, len(ess), rec['ngauge'], rec['shapes'], rec['ncand'], rec['n_nonempty_strict'], rec['n_nonempty_relaxed'], rec['n_nonempty_sorted'],
        rec['show_strict'], rec['show_relaxed'], rec['show_sorted'], rec['show_sorted_relaxed'], rec['line']['show_strict'], rec['line']['show_relaxed'], rec['line']['show_sorted'], rec['secs']), flush=True)
print('total %.0fs' % (time.time() - t0))
