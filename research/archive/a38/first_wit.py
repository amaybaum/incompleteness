"""Collect the first N {0,1} straight lines in no census subspace (strict or relaxed), then verify them exactly."""
import sys, time, pickle; sys.path.insert(0, 'a38')
from lib38b import *
t0 = time.time()
NWANT = int(sys.argv[1]) if len(sys.argv) > 1 else 200
adm, C = pickle.load(open('a38/stage1_tables.pkl', 'rb'))
AS, BS = membership_matrix(False); AR, BR = membership_matrix(True)
ROWS = list(range(1, 16))
def ctab(i, i2): return C[(i, i2)] if i < i2 else C[(i2, i)].T
BATCH = 8192; buf = np.zeros((BATCH, 16), dtype=np.uint16); nb = 0; found = []; count = 0
class Done(Exception): pass
def flush():
    global nb, count
    if nb == 0: return
    M = buf[:nb].astype(np.int64); E = ((M[:, :, None] >> np.arange(16)[None, None, :]) & 1)
    X = E.reshape(nb, 256).astype(np.float64)
    RS = X @ AS.T; RR = X @ AR.T
    okS = np.zeros(nb, dtype=bool); okR = np.zeros(nb, dtype=bool)
    for nm, form, lo, hi in BS: okS |= ~np.abs(RS[:, lo:hi]).max(axis=1).astype(bool)
    for nm, form, lo, hi in BR: okR |= ~np.abs(RR[:, lo:hi]).max(axis=1).astype(bool)
    for idx in np.flatnonzero(~okS & ~okR).tolist(): found.append(E[idx].copy())
    count += nb; nb = 0
    if len(found) >= NWANT: raise Done
cur = np.zeros(16, dtype=np.uint16)
def emit():
    global nb
    buf[nb] = cur; nb += 1
    if nb == BATCH: flush()
def rec(dom, chosen):
    free = [i for i in ROWS if i not in chosen]
    i = min(free, key=lambda r: int(dom[r].sum()))
    cand = np.flatnonzero(dom[i]); rest = [r for r in free if r != i]
    if not rest:
        for n in cand: cur[i] = adm[i][n]; emit()
        return
    for n in cand:
        newdom = {}; ok = True
        for r in rest:
            d = dom[r] & ctab(i, r)[n]
            if not d.any(): ok = False; break
            newdom[r] = d
        if not ok: continue
        cur[i] = adm[i][n]; chosen.add(i); rec(newdom, chosen); chosen.discard(i)
try: rec({i: np.ones(len(adm[i]), dtype=bool) for i in ROWS}, set())
except Done: pass
print('scanned', count, 'found', len(found), '%.0fs' % (time.time() - t0), flush=True)
pickle.dump(found, open('a38/first_wit.pkl', 'wb'))
