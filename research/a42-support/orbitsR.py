import numpy as np, collections, sys
from lib42 import elems
msize = np.load('msize.npy')
FULL = (1 << 16) - 1
rowperms = set()
for p, s_ in elems:
    rr = [set(divmod(p[i * 16 + j], 16)[0] for j in range(16)) for i in range(16)]
    if all(len(x) == 1 for x in rr): rowperms.add(tuple(x.pop() for x in rr))
rowperms = sorted(rowperms); assert len(rowperms) == 64
def img(R, pm):
    out = 0
    for i in range(16):
        if (R >> i) & 1: out |= 1 << pm[i]
    return out
budget = int(sys.argv[1])
seen = set(); reps = []; cnt = collections.Counter()
for R in range(1, FULL):
    if R in seen: continue
    orb = {img(R, pm) for pm in rowperms}; seen |= orb
    Z = FULL ^ R
    lb = sum(int(msize[i, Z]) for i in range(16) if (R >> i) & 1)
    if lb <= budget:
        reps.append((R, lb, len(orb))); cnt[bin(R).count('1')] += 1
print('orbit reps with LB <=', budget, ':', len(reps), dict(sorted(cnt.items())))
# order by r descending? keep natural; write
reps.sort(key=lambda x: (bin(x[0]).count('1'), x[0]))
open('Rreps_%d.txt' % budget, 'w').write('\n'.join(str(R) for R, lb, o in reps))
