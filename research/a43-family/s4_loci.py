"""Stage 4: exact Dita loci of the essential atom family of every orbit (min-support member), with per-orbit checkpoints.
Also: the one-parameter classifier on the witness line itself (K7's independent method)."""
import time, pickle, sys
from splitters import *
t0 = time.time()
d = pickle.load(open(os.path.join(HERE, 'orbits.pkl'), 'rb')); Es, recs = d['Es'], d['recs']
AT = pickle.load(open(os.path.join(HERE, 'atoms.pkl'), 'rb'))
CK = os.path.join(HERE, 'loci.pkl')
try: done = pickle.load(open(CK, 'rb'))
except Exception: done = {}
which = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else range(len(recs))
def is_gauge_atom(cells):
    rows = set(r for r, k in cells); cols = set(k for r, k in cells)
    return (len(rows) == 1 and len(cols) == 16) or (len(cols) == 1 and len(rows) == 16)
def shape(cells): return (len(set(r for r, k in cells)), len(set(k for r, k in cells)))
for t in which:
    if t in done: continue
    r = recs[t]
    # the member with the fewest atoms whose atom family is jointly realizable
    mem = min((i for i in r['members'] if AT[i]['joint'][1] == 0), key=lambda i: (len(AT[i]['atoms']), Es[i]))
    at = AT[mem]['atoms']
    ess = [a for a in at if not is_gauge_atom(a)]
    Ms = [cells_to_mat(a) for a in ess]
    t1 = time.time()
    S = summarize(Ms)
    Eess = madd_(*Ms)
    S1 = summarize([Eess])
    rec = {'orbit': t, 'member': mem, 'natoms': len(at), 'ngauge': len(at) - len(ess), 'atoms': ess, 'shapes': [shape(a) for a in ess],
           'hulls': [census_hulls([M]) for M in Ms],
           'loo_hulls': [census_hulls([M for j, M in enumerate(Ms) if j != k]) for k in range(len(Ms))],
           'ncand': S['ncand'], 'n_nonempty': S['n_nonempty'], 'strict_eq_relaxed': S['strict_eq_relaxed'], 'all_coordinate': S['all_coordinate'],
           'maximal': [F.B for F in S['maximal']], 'maximal_show': [F.show() for F in S['maximal']], 'covered': S['covered'],
           'maximal_relaxed_show': [F.show() for F in S['maximal_relaxed']],
           'loci': {k: (v[0].B if v[0] is not None else None, v[1].B if v[1] is not None else None) for k, v in S['loci'].items()},
           'line': {'ncand': S1['ncand'], 'maximal_show': [F.show() for F in S1['maximal']], 'strict_eq_relaxed': S1['strict_eq_relaxed']},
           'secs': time.time() - t1}
    done[t] = rec
    pickle.dump(done, open(CK, 'wb'))
    print('orbit %2d member %3d d=%d (gauge %d) shapes %s cand %d nonempty %d s=r %s coord %s faces %s | line %s  %.0fs' % (
        t, mem, len(ess), rec['ngauge'], rec['shapes'], rec['ncand'], rec['n_nonempty'], rec['strict_eq_relaxed'], rec['all_coordinate'],
        rec['maximal_show'], rec['line']['maximal_show'], rec['secs']), flush=True)
print('total %.0fs' % (time.time() - t0))
