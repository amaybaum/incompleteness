"""Coordinator audit 2: which partition structures hold at (1,1,1) and (-1,-1,-1) under all labellings; and act 37's W-arc."""
import itertools, time, sys
exec(open('audit.py', encoding='utf-8').read().split("res = {}")[0])
res = {k: (all_loci(k, False), all_loci(k, True)) for k in CANDS}
def show(k): return '%s %s blocks=%s classes=%s' % (k[0], k[1], k[2], k[3])
for nm, u in (('(1,1,1)', (ONE, ONE, ONE)), ('(-1,-1,-1)', (G(-1), G(-1), G(-1)))):
    for idx, lab in ((0, 'strict'), (1, 'relaxed')):
        hit = [k for k in CANDS if any(on_flat(F, u) for F in res[k][idx][0])]
        print(nm, lab, len(hit))
        if nm != '(1,1,1)' and idx == 0:
            for k in hit: print('   ', show(k))
by = {}
for k in CANDS:
    if k[0] == 'column' and res[k][0][0] and any(on_flat(F, (ONE, ONE, ONE)) for F in res[k][0][0]): by.setdefault(k[1], 0); by[k[1]] += 1
print('column-form partition structures at (1,1,1) by shape', by)
print('per-candidate strict union == relaxed union:', all(res[k][0][0] == res[k][1][0] for k in CANDS))
# act 37's W-arc: H(u) = SIG o u^W as the u1-line of the torus machinery
t2 = time.time()
Z = [[0] * 16 for _ in range(16)]
WM = [[W[i * 16 + j] for j in range(16)] for i in range(16)]
OR, CANDS, STATS, _ = (lambda o: (o, *enumerate_candidates(o), None))(orientations(WM, Z, Z))
print('W-arc partition candidates', len(CANDS))
resW = {k: (all_loci(k, False), all_loci(k, True)) for k in CANDS}
LINE = Flat([((0, 1, 0), V0), ((0, 0, 1), V0)])
for idx, lab in ((0, 'strict'), (1, 'relaxed')):
    fl = set(G_ for k in CANDS for F in resW[k][idx][0] for G_ in [meet_or_none(F, LINE)] if G_ is not None)
    whole = [k for k in CANDS if any(F.contains(LINE) for F in resW[k][idx][0])]
    pts = sorted(G_.show() for G_ in fl if G_.dim() == 0)
    print('W-arc', lab, ': identically on the arc', [(k[0], k[1]) for k in whole], ' isolated points', pts)
    for pstr in pts:
        pass
for nm, u in (('u=1', (ONE, ONE, ONE)), ('u=-1', (G(-1), ONE, ONE))):
    for idx, lab in ((0, 'strict'), (1, 'relaxed')):
        print('W-arc', nm, lab, sum(1 for k in CANDS if any(on_flat(F, u) for F in resW[k][idx][0])))
print('W-arc time %.0fs' % (time.time() - t2))
