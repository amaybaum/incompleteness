"""Count-only DFS (forward checking, MRV) over the {0,1} straight-line CSP; stores solutions compactly as uint16 rows."""
import sys, time, pickle; sys.path.insert(0, 'a38')
import numpy as np
adm, C = pickle.load(open('a38/stage1_tables.pkl', 'rb'))
ROWS = list(range(1, 16))
def ctab(i, i2): return C[(i, i2)] if i < i2 else C[(i2, i)].T
t0 = time.time(); count = 0; nodes = 0
STORE = int(sys.argv[1]) if len(sys.argv) > 1 else 0
buf = np.zeros((STORE, 16), dtype=np.uint16) if STORE else None
cur = np.zeros(16, dtype=np.uint16)
def rec(dom, chosen_n):
    global nodes, count
    nodes += 1
    free = [i for i in ROWS if i not in chosen_n]
    if not free:
        if STORE and count < STORE: buf[count] = cur
        count += 1
        if count % 1000000 == 0: print('sols', count, 'nodes', nodes, '%.0fs' % (time.time() - t0), flush=True)
        return
    i = min(free, key=lambda r: int(dom[r].sum()))
    cand = np.flatnonzero(dom[i])
    rest = [r for r in free if r != i]
    if not rest:
        # leaf level: every candidate is a solution
        for n in cand:
            cur[i] = adm[i][n]
            if STORE and count < STORE: buf[count] = cur
            count += 1
            if count % 1000000 == 0: print('sols', count, 'nodes', nodes, '%.0fs' % (time.time() - t0), flush=True)
        return
    for n in cand:
        newdom = {}; ok = True
        for r in rest:
            d = dom[r] & ctab(i, r)[n]
            if not d.any(): ok = False; break
            newdom[r] = d
        if not ok: continue
        cur[i] = adm[i][n]; chosen_n.add(i)
        rec(newdom, chosen_n)
        chosen_n.discard(i)
dom0 = {i: np.ones(len(adm[i]), dtype=bool) for i in ROWS}
rec(dom0, set())
print('DONE solutions', count, 'nodes', nodes, '%.0fs' % (time.time() - t0), flush=True)
if STORE: np.save('a38/stage1_sols.npy', buf[:min(count, STORE)])
