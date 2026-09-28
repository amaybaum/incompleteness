"""Stage 3: the library of atoms across the 416 witnesses: distinct atoms, rectangle form, straightness, census hulls."""
import time, pickle
from splitters import *
t0 = time.time()
d = pickle.load(open(os.path.join(HERE, 'orbits.pkl'), 'rb')); Es, recs = d['Es'], d['recs']
AT = pickle.load(open(os.path.join(HERE, 'atoms.pkl'), 'rb'))
lib = {}
for idx in AT:
    for a in AT[idx]['atoms']:
        lib.setdefault(tuple(sorted(a)), []).append(idx)
print('distinct atoms', len(lib))
def rect(cells):
    R = sorted(set(r for r, k in cells)); K = sorted(set(k for r, k in cells))
    return (R, K) if len(R) * len(K) == len(cells) else None
def rc(i): return (i // 4, i % 4)
rows_out = []
for t, (a, users) in enumerate(sorted(lib.items(), key=lambda kv: -len(kv[1]))):
    M = cells_to_mat(a); rr = rect(a)
    st = straight(M)
    hs = census_hulls([M]); hr = census_hulls([M], relaxed=True)
    rows_out.append({'atom': a, 'users': users, 'rect': rr, 'straight': st, 'hulls': hs, 'hulls_relaxed': hr})
    print('%2d used by %3d  rect %-58s straight %s  hulls %s%s' % (t, len(users), (('R=%s K=%s' % ([rc(i) for i in rr[0]], [rc(i) for i in rr[1]])) if rr else 'NOT A RECTANGLE (%d cells)' % len(a)), st, hs, '' if hs == hr else ' relaxed %s' % hr))
pickle.dump(rows_out, open(os.path.join(HERE, 'atomlib.pkl'), 'wb'))
print('%.0fs' % (time.time() - t0))
