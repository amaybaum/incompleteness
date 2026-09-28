"""Post-run analysis of the orbit table (state_full/state.bin): controls C1-C3 (table part), C6(c), C7 (independent
canonical form on a sample), C10 (every canonical representative and first-found solution is a straight line), and
the distributions. Writes analysis.json."""
import json, random, sys, collections, time
from lib41 import *
t0 = time.time()
path = sys.argv[1] if len(sys.argv) > 1 else 'state_full/state.bin'
hdr, R = load_table(path)
res = {}; bad = []
def chk(name, got, want):
    ok = got == want; print('  %s  %-66s %s' % ('PASS' if ok else 'FAIL', name, got if ok else '%s (expected %s)' % (got, want)), flush=True)
    res[name] = {'ok': ok, 'got': str(got), 'want': str(want)}
    if not ok: bad.append(name)
print('header', hdr)
N = len(R)
chk('run complete (next branch = end)', hdr['next_branch'] == hdr['b_end'] == 1327, True)
chk('C6c: sum of n_sol over orbits = D-solutions (count mode)', int(R['n_sol'].sum()), 171552256)
chk('sum of n_gauge over orbits = gauge classes (count mode)', int(R['n_gauge'].sum()), 30594431)
chk('sum of n_hrep over orbits = H_dom representatives', int(R['n_hrep'].sum()), hdr['hrep'])
chk('built-in: relaxed-membership mismatches', hdr['ctrl_relax_mismatch'], 0)
chk('built-in: canonical-form idempotence failures (2 per orbit)', (hdr['ctrl_canon_not_idemp'], hdr['ctrl_canon_checked']), (0, N))
C = decode_keys(R['key'])
chk('decoded keys distinct', len(set(map(bytes, C.reshape(N, 256)))), N)
# ---- C10: straightness of every canonical representative and every first-found solution (exact integer tables) ----
VT = {}
for i in range(16):
    for i2 in range(i + 1, 16): VT[(i, i2)] = vanishing_table(i, i2).astype(bool)
POW = (1 << np.arange(16)).astype(np.int64)
def straight_batch(X):
    """X (n,16,16) integer: boolean per matrix, every level set of every row-pair difference vanishes"""
    ok = np.ones(len(X), dtype=bool)
    for (i, i2), V in VT.items():
        D = X[:, i, :].astype(np.int64) - X[:, i2, :].astype(np.int64)
        for v in range(-4, 5):
            m = ((D == v).astype(np.int64) * POW).sum(axis=1)
            ok &= V[m] | (m == 0)
    return ok
okC = straight_batch(C)
chk('C10: every canonical representative is a straight line', int((~okC).sum()), 0)
F = np.zeros((N, 16, 16), dtype=np.int8)
for i in range(1, 16): F[:, i, :] = ((R['first'][:, i][:, None].astype(np.int64) >> np.arange(16)) & 1)
okF = straight_batch(F)
chk('C10: every first-found solution is a straight line', int((~okF).sum()), 0)
chk('C10: first-found solutions are in the domain (row 0 = 0, no all-ones row)', bool((F[:, 0, :] == 0).all() and not (F[:, 1:, :].min(axis=2) == 1).any()), True)
# control of the batch checker itself: a non-straight matrix is rejected
Xbad = np.zeros((1, 16, 16), dtype=np.int8); Xbad[0, 1, 0] = 1
chk('C10 countercontrol: a single-entry matrix is rejected', bool(straight_batch(Xbad)[0]), False)
# ---- C7: independent canonical form (numpy lexsort over all 2048 images) on a sample ------------------------
random.seed(4141)
nonrel = np.flatnonzero(R['relmask_canon'] == 0)
sample = sorted(set(random.sample(range(N), 2000)) | set(nonrel[:2000].tolist()))
mism = 0
for x in sample:
    if canon_np(F[x]) != tuple(int(v) for v in C[x].reshape(256)): mism += 1
chk('C7: numpy canonical form of the first-found solution = C key (%d orbits)' % len(sample), mism, 0)
# second representative: a random group image plus a random gauge of the first-found solution
mism = 0
for x in sample[:500]:
    g = random.randrange(2048); E = act(GROUP[g], F[x].tolist())
    r = [random.randint(-3, 3) for _ in range(16)]; c = [random.randint(-3, 3) for _ in range(16)]
    E = [[E[i][j] + r[i] + c[j] for j in range(16)] for i in range(16)]
    if canon_np(E) != tuple(int(v) for v in C[x].reshape(256)): mism += 1
chk('C7: canonical form invariant under a random group element and gauge (500 orbits)', mism, 0)
# ---- C1-C3 table lookups ------------------------------------------------------------------------------------
keyidx = {bytes(C[x].reshape(256).astype(np.int8)): x for x in range(N)}
Mf = lambda f: [[f(i, j) for j in range(16)] for i in range(16)]
A, B, Cm = Mf(EA), Mf(EB), Mf(EC)
add = lambda *Xs: [[sum(X[i][j] for X in Xs) for j in range(16)] for i in range(16)]
objs = {'A': A, 'B': B, 'C': Cm, 'A+B': add(A, B), 'A+C': add(A, Cm), 'B+C': add(B, Cm), 'A+B+C': add(A, B, Cm), 'zero': Mf(lambda i, j: 0)}
found = {}
for k, E in objs.items():
    kk = bytes(np.array(canon_np(E), dtype=np.int8))
    chk('C1-C3: orbit of %s is in the table' % k, kk in keyidx, True)
    if kk in keyidx: found[k] = int(keyidx[kk])
w = found.get('A+B+C')
if w is not None:
    rw = R[w]
    chk('C1: witness orbit: sorted-matching relaxed mask of canon rep', int(rw['relmask_canon']), 0)
    chk('C1: witness orbit: strictly-member D-solutions (sorted matching)', int(rw['n_strict']), 0)
    chk('C1: witness orbit: distinct gauge-normal images', int(rw['orbit_gauge']), 512)
    print('  witness orbit record: n_sol %d n_gauge %d min_dsupp %d canon_nnz %d min_gn_nnz %d' % (rw['n_sol'], rw['n_gauge'], rw['min_dsupp'], rw['canon_nnz'], rw['min_gn_nnz']))
json.dump({'header': hdr, 'controls': res, 'failed': bad, 'object_orbits': found}, open('analysis_controls.json', 'w'), indent=1)
np.save('canon_reps.npy', C); np.save('first_solutions.npy', F)
print('FAILED' if bad else 'ALL GREEN', bad, '%.0fs' % (time.time() - t0))
