import numpy as np, collections, sys
from dfs42 import VT, PC
ALL = (1 << 16) - 1
def cv_table(i, Z):
    V = np.ones(1 << 16, dtype=bool)
    for r in range(16):
        if (Z >> r) & 1: V &= VT[i, r]
    return V
def minimal_sets(V):
    ms = np.flatnonzero(V)[1:]
    ms = sorted(ms.tolist(), key=lambda x: PC[x])
    mins = []
    for m in ms:
        if not any((mm & m) == mm for mm in mins): mins.append(m)
    return mins
if __name__ == '__main__':
    surv = np.load('survR.npy')
    rng = np.random.default_rng(0)
    stats = collections.Counter()
    for R, lb in surv[rng.choice(len(surv), 60, replace=False)]:
        R = int(R); Z = ALL ^ R
        desc = []
        for i in range(16):
            if not (R >> i) & 1: continue
            mins = minimal_sets(cv_table(i, Z))
            disjoint = all((a & b) == 0 for x, a in enumerate(mins) for b in mins[x+1:])
            cover = 0
            for a in mins: cover |= a
            desc.append((len(mins), sorted(collections.Counter(PC[a] for a in mins).items()), disjoint, PC[cover]))
            stats[disjoint] += 1
        print(bin(R).count('1'), lb, desc[:4])
    print(stats)
