import json, collections
from hull_linear import states, hull
R = json.load(open('fast_stageA_L2.json'))
ks = [tuple(map(tuple, r['kappa'])) for r in R if r['rule'] == 'linear' and r['verdict'] == 'FAIL(dimC=3)']
out = collections.Counter()
for k in ks:
    cols, chosen, basis = states('linear', k, 3)
    assert len(chosen) == 3 and chosen[0] == ('', 0)
    pts = [(basis[1][j], basis[2][j]) for j in range(len(cols))]
    H = hull(pts)
    out[(tuple(chosen[1:]), tuple(sorted(H)))] += 1
    print(k, chosen[1:], sorted((float(a), float(b)) for a, b in H), flush=True)
print('SUMMARY')
for key, n in out.items():
    print(n, key[0], [(str(a), str(b)) for a, b in key[1]])
