from lib41 import *
import json, itertools
gens = json.load(open('ctrl_objects.json'))['generators']
def perm_pair(e):
    p, s_ = e
    rp = [p[i * 16] // 16 for i in range(16)]; cq = [p[j] % 16 for j in range(16)]
    if all(p[i * 16 + j] == rp[i] * 16 + cq[j] for i in range(16) for j in range(16)): return 'product', rp, cq
    psi = [p[i * 16] % 16 for i in range(16)]; phi = [p[j] // 16 for j in range(16)]
    return 'transposed', psi, phi
g = GROUP[1133]
form, f1, f2 = perm_pair(g)
print(form, f1, f2, g[1])
for s in CENSUS9:
    (m, n), cp, rows = s
    if form == 'product':
        ncp = [sorted(f2[j] for j in b) for b in cp]; nrows = [[f1[i] for i in r] for r in rows]
    else:
        continue
    # find census structure with these index sets
    tgt = [t for t in CENSUS9 if t[0] == (m, n) and sorted(map(tuple, map(sorted, t[1]))) == sorted(map(tuple, ncp)) and sorted(map(tuple, map(sorted, t[2]))) == sorted(tuple(sorted(r)) for r in nrows)]
    print(NAMES9[s], '->', [NAMES9[t] for t in tgt])
    if tgt:
        t = tgt[0]
        # matching: image rows groups as ordered lists vs target sorted groups
        print('   image groups (ordered by source label a):', nrows)
        print('   target groups (sorted)            :', [list(r) for r in t[2]])
        print('   image blocks (ordered by source d):', [[f2[j] for j in b] for b in cp])
        print('   target blocks                     :', [list(b) for b in t[1]])
