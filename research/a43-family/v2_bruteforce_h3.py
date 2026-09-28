"""Verification 2: brute force over every within-class alignment for H3's 46 candidates, using ONLY the frozen probe's own functions
(P40['classify'] for the candidates, P40['conditions'] + P40['solve'] + the frozen 3-dim Flat). An alignment is realized by
passing the class tuples in permuted member order (the frozen code reads rows[b][a] as the member playing X-row a). sigma_0 is
kept sorted (global relabelling of a is free). Shares no code with align.py or FlatD."""
import itertools, time, pickle, os
from lib43 import P40, HERE
t0 = time.time()
classify, conditions, solve, Flat = P40['classify'], P40['conditions'], P40['solve'], P40['Flat']
OR, CANDS, STATS, LOCI = classify(P40['PA'], P40['PB'], P40['PC'])
res = {}
for idx, key in enumerate(sorted(CANDS, key=lambda k: (k[0], k[1], k[2], k[3]))):
    form, mn, cp, rows = key
    m, n = mn
    locS = set(); locR = set(); nal = 0
    for perms in itertools.product(*[list(itertools.permutations(cl)) for cl in rows[1:]]):
        rw = (rows[0],) + perms
        nal += 1
        a = solve(conditions(OR, form, mn, cp, rw, False)); b = solve(conditions(OR, form, mn, cp, rw, True))
        if a is not None: locS.add(a)
        if b is not None: locR.add(b)
    res[key] = (locS, locR, nal)
    print('%2d %-6s %s alignments %6d  strict %s  relaxed %s  %.0fs' % (idx, form, mn, nal, sorted(F.show() for F in locS), sorted(F.show() for F in locR), time.time() - t0), flush=True)
def maximal(fs):
    fs = set(fs); return sorted(F.show() for F in fs if not any(G_ != F and G_.contains(F) for G_ in fs))
allS = set().union(*[v[0] for v in res.values()]); allR = set().union(*[v[1] for v in res.values()])
print('union strict  (maximal):', maximal(allS))
print('union relaxed (maximal):', maximal(allR))
print('nonempty candidates strict %d relaxed %d' % (sum(1 for v in res.values() if v[0]), sum(1 for v in res.values() if v[1])))
print('non-coordinate flats among all per-alignment loci:', sorted(set(F.show() for F in allS | allR if not all(sorted(map(abs, k)) == [0, 0, 1] and v in ((0, 0, 0), (2, 0, 0)) for k, v in F.B))))
pickle.dump({k: ([F.B for F in v[0]], [F.B for F in v[1]], v[2]) for k, v in res.items()}, open(os.path.join(HERE, 'v2_bruteforce_h3.pkl'), 'wb'))
print('%.0fs' % (time.time() - t0))
