"""Stage 2: splitters and atoms for all 416 witnesses; exact controls; per orbit the atom families."""
import time, pickle, random
from splitters import *
t0 = time.time()
d = pickle.load(open(os.path.join(HERE, 'orbits.pkl'), 'rb')); Es, recs = d['Es'], d['recs']
rng = random.Random(43)
out = {}
bad_split = bad_nonsplit = nchecked_non = 0
for idx, E in enumerate(Es):
    sols = splitters(E)
    at = atoms(E, sols)
    Ms = [cells_to_mat(a) for a in at]
    jr = joint_realizable(Ms)
    # every union of atoms a splitter iff #splitters == 2^#atoms (splitters are unions of atoms by construction)
    out[idx] = {'nsplit': len(sols), 'atoms': at, 'joint': jr}
    if idx % 8 == 0:
        # independent exact control on a sample: each enumerated splitter is jointly realizable with its complement (Gaussian
        # rationals, no tables); random sub-supports not enumerated are not
        for P in sols[:6]:
            Pm = mask_to_mat(P); Q = [[E[i][j] - Pm[i][j] for j in range(16)] for i in range(16)]
            bad_split += joint_realizable([Pm, Q])[1] != 0
        S = set(sols); cells = [(r, k) for r in range(16) for k in range(16) if E[r][k]]
        for _ in range(4):
            sub = [c for c in cells if rng.random() < 0.5]
            Pm = cells_to_mat(sub); key = tuple(row_mask(Pm[r]) for r in range(16))
            if key in S: continue
            Q = [[E[i][j] - Pm[i][j] for j in range(16)] for i in range(16)]
            nchecked_non += 1; bad_nonsplit += joint_realizable([Pm, Q])[1] == 0
print('exact controls: enumerated splitters failing the direct check', bad_split, '; random non-enumerated sub-supports passing it', bad_nonsplit, 'of', nchecked_non)
print('%.0fs' % (time.time() - t0))
print('orbit  members: (#splitters, #atoms, atom sizes, atoms jointly realizable)')
for t, r in enumerate(recs):
    row = []
    for i in r['members']:
        o = out[i]; row.append((o['nsplit'], len(o['atoms']), tuple(sorted(len(a) for a in o['atoms'])), o['joint'][1] == 0))
    print('%3d' % t, sorted(set(row)))
print('every member: #splitters == 2^#atoms:', all(out[i]['nsplit'] == 2 ** len(out[i]['atoms']) for i in out))
print('every member: atom family jointly realizable:', all(out[i]['joint'][1] == 0 for i in out))
pickle.dump(out, open(os.path.join(HERE, 'atoms.pkl'), 'wb'))
print('%.0fs' % (time.time() - t0))
