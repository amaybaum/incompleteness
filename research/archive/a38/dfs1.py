"""DFS with forward checking over the {0,1} straight-line CSP (row 0 = 0). Writes solutions as 15 masks each."""
import sys, time, pickle; sys.path.insert(0, 'a38')
import numpy as np
adm, C = pickle.load(open('a38/stage1_tables.pkl', 'rb'))
ROWS = list(range(1, 16))
idx = {i: {int(v): n for n, v in enumerate(adm[i])} for i in ROWS}
def ctab(i, i2):
    return C[(i, i2)] if i < i2 else C[(i2, i)].T
t0 = time.time(); sols = []; nodes = 0
def rec(dom, chosen):
    global nodes
    nodes += 1
    if len(chosen) == 15:
        sols.append(dict(chosen)); return
    free = [i for i in ROWS if i not in chosen]
    i = min(free, key=lambda r: int(dom[r].sum()))
    cand = np.flatnonzero(dom[i])
    if len(cand) == 0: return
    for n in cand:
        newdom = {}
        ok = True
        for r in free:
            if r == i: continue
            d = dom[r] & ctab(i, r)[n]
            if not d.any(): ok = False; break
            newdom[r] = d
        if not ok: continue
        chosen[i] = int(adm[i][n])
        rec(newdom, chosen)
        del chosen[i]
        if len(sols) % 100000 == 0 and len(sols) and time.time() - t0 > 0:
            pass
    if nodes % 200000 == 0: print('nodes', nodes, 'sols', len(sols), '%.0fs' % (time.time() - t0), flush=True)
dom0 = {i: np.ones(len(adm[i]), dtype=bool) for i in ROWS}
rec(dom0, {})
print('DONE nodes', nodes, 'solutions', len(sols), '%.0fs' % (time.time() - t0), flush=True)
pickle.dump(sols, open('a38/stage1_sols.pkl', 'wb'))
