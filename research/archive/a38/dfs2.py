"""DFS over the {0,1} straight-line CSP with batch classification: strict and relaxed membership in the 18 census
subspaces, a histogram of membership masks, storage of every non-member, and one representative per partition
signature (the straight lattice L(Pi_E) depends on the signature alone)."""
import sys, time, pickle; sys.path.insert(0, 'a38')
from lib38b import *
t0 = time.time()
adm, C = pickle.load(open('a38/stage1_tables.pkl', 'rb'))
print('tables loaded %.0fs' % (time.time() - t0), flush=True)
AS, BS = membership_matrix(False); AR, BR = membership_matrix(True)
print('membership rows strict', AS.shape, 'relaxed', AR.shape, '%.0fs' % (time.time() - t0), flush=True)
ROWS = list(range(1, 16))
def ctab(i, i2): return C[(i, i2)] if i < i2 else C[(i2, i)].T
BATCH = 65536
buf = np.zeros((BATCH, 16), dtype=np.uint16); nb = 0
count = 0; nodes = 0
hist = {}; nonstrict = []; nonrelaxed = []; sigs = {}
PI = [(i, i2) for i in range(16) for i2 in range(i + 1, 16)]
PI_I = np.array([p[0] for p in PI]); PI_J = np.array([p[1] for p in PI])
BITS = (np.arange(16)[None, :] if True else None)
def flush():
    global nb, count
    if nb == 0: return
    M = buf[:nb].astype(np.int64)                                   # (B,16) masks per row
    E = ((M[:, :, None] >> np.arange(16)[None, None, :]) & 1)       # (B,16,16) exponent matrices
    X = E.reshape(nb, 256).astype(np.float64)
    for A, blocks, tag in ((AS, BS, 'strict'), (AR, BR, 'relaxed')):
        R = X @ A.T
        masks = np.zeros(nb, dtype=np.int64)
        for k, (nm, form, lo, hi) in enumerate(blocks):
            ok = ~np.abs(R[:, lo:hi]).max(axis=1).astype(bool)
            masks |= ok.astype(np.int64) << k
        if tag == 'strict': ms = masks
        else: mr = masks
    for a, b in zip(ms.tolist(), mr.tolist()):
        hist[(a, b)] = hist.get((a, b), 0) + 1
    for idx in np.flatnonzero(ms == 0).tolist():
        (nonrelaxed if mr[idx] == 0 else nonstrict).append(buf[idx].copy())
    # partition signatures: per pair the masks of the d=1 and d=-1 parts
    S1 = M[:, PI_I] & ~M[:, PI_J] & 0xFFFF; S2 = M[:, PI_J] & ~M[:, PI_I] & 0xFFFF
    SG = np.concatenate([S1, S2], axis=1).astype(np.uint16)
    for idx in range(nb):
        key = SG[idx].tobytes()
        if key not in sigs: sigs[key] = buf[idx].copy()
    count += nb; nb = 0
cur = np.zeros(16, dtype=np.uint16)
def emit():
    global nb
    buf[nb] = cur; nb += 1
    if nb == BATCH:
        flush()
        print('sols', count, 'nodes', nodes, 'sigs', len(sigs), 'nonstrict', len(nonstrict), 'nonrelaxed', len(nonrelaxed), '%.0fs' % (time.time() - t0), flush=True)
def rec(dom, chosen):
    global nodes
    nodes += 1
    free = [i for i in ROWS if i not in chosen]
    i = min(free, key=lambda r: int(dom[r].sum()))
    cand = np.flatnonzero(dom[i]); rest = [r for r in free if r != i]
    if not rest:
        for n in cand:
            cur[i] = adm[i][n]; emit()
        return
    for n in cand:
        newdom = {}; ok = True
        for r in rest:
            d = dom[r] & ctab(i, r)[n]
            if not d.any(): ok = False; break
            newdom[r] = d
        if not ok: continue
        cur[i] = adm[i][n]; chosen.add(i); rec(newdom, chosen); chosen.discard(i)
rec({i: np.ones(len(adm[i]), dtype=bool) for i in ROWS}, set())
flush()
print('DONE solutions', count, 'nodes', nodes, 'signatures', len(sigs), 'nonstrict', len(nonstrict), 'nonrelaxed', len(nonrelaxed), '%.0fs' % (time.time() - t0), flush=True)
pickle.dump({'count': count, 'hist': hist, 'nonstrict': nonstrict, 'nonrelaxed': nonrelaxed, 'sigs': sigs, 'BS': BS, 'BR': BR}, open('a38/dfs2_out.pkl', 'wb'))
print('saved', flush=True)
