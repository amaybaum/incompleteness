"""Knuth's estimator for the size of the {0,1} DFS solution set (same MRV order as dfs2)."""
import sys, time, pickle, random; sys.path.insert(0, 'a38')
import numpy as np
adm, C = pickle.load(open('a38/stage1_tables.pkl', 'rb'))
ROWS = list(range(1, 16))
def ctab(i, i2): return C[(i, i2)] if i < i2 else C[(i2, i)].T
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
def probe():
    dom = {i: np.ones(len(adm[i]), dtype=bool) for i in ROWS}; chosen = set(); weight = 1
    while True:
        free = [i for i in ROWS if i not in chosen]
        i = min(free, key=lambda r: int(dom[r].sum()))
        cand = np.flatnonzero(dom[i]); rest = [r for r in free if r != i]
        if not rest: return weight * len(cand)
        # children that survive forward checking
        good = []
        for n in cand:
            newdom = {}; ok = True
            for r in rest:
                d = dom[r] & ctab(i, r)[n]
                if not d.any(): ok = False; break
                newdom[r] = d
            if ok: good.append((n, newdom))
        if not good: return 0
        weight *= len(good)
        n, dom = random.choice(good); chosen.add(i)
t0 = time.time(); ests = []
for k in range(int(sys.argv[2]) if len(sys.argv) > 2 else 40):
    ests.append(probe())
    if (k + 1) % 10 == 0: print('probes', k + 1, 'mean estimate %.3g' % (sum(ests) / len(ests)), 'min %.3g max %.3g' % (min(ests), max(ests)), '%.0fs' % (time.time() - t0), flush=True)
print('ESTIMATE', sum(ests) / len(ests))
