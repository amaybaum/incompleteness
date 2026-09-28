"""Stage 6: an out-of-collection test of K10'. Random families of 2-4 straight atoms from the atom library (and their images
under a few stabilizer elements, to leave the collector's row-0 = 0 domain), jointly realizable, disjoint OR overlapping supports,
witnesses and non-witnesses alike. Exact alignment-free loci vs the K10' prediction. Seed fixed."""
import pickle, random, sys, time
from align import *
from splitters import cells_to_mat
import t_k10 as K
t0 = time.time()
WIT = len(sys.argv) > 2 and sys.argv[2] == 'witness'
rng = random.Random(4344 if WIT else 4343)
lib = [r for r in pickle.load(open(os.path.join(HERE, 'atomlib.pkl'), 'rb')) if r['straight'] and not (len(set(a[0] for a in r['atom'])) == 1)]
atoms = [cells_to_mat(r['atom']) for r in lib]
def stab_apply(e, M):
    p, s_ = e; out = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            i2, j2 = divmod(p[i * 16 + j], 16); out[i2][j2] = M[i][j]
    return out
N = int(sys.argv[1]) if len(sys.argv) > 1 else 24
fams = []; tries = 0
while len(fams) < N and tries < 20000:
    tries += 1
    d = rng.choice([3, 4, 4, 5]) if WIT else rng.choice([2, 3, 3, 4])
    Ms = [atoms[i] for i in rng.sample(range(len(atoms)), d)]
    overlap = any(Ms[a][i][j] and Ms[b][i][j] for a in range(d) for b in range(a + 1, d) for i in range(16) for j in range(16))
    if overlap and rng.random() < 0.6: continue
    if rng.random() < 0.5:
        e = elems[rng.randrange(len(elems))]; Ms = [stab_apply(e, M) for M in Ms]
    if joint_realizable(Ms)[1] != 0: continue
    if WIT and K.identically_Dita([madd_(*Ms)], relaxed=True) is not None: continue
    fams.append((Ms, overlap))
print('families', len(fams), 'from', tries, 'draws', flush=True)
ok = okS = 0; out = []
for idx, (Ms, overlap) in enumerate(fams):
    d = len(Ms)
    S = summarize_alignfree(Ms)
    PS = sorted(F.B for F in K.predict(Ms, False)); PR = sorted(F.B for F in K.predict(Ms, True))
    gs = sorted(F.B for F in S['union_strict']) == PS; gr = sorted(F.B for F in S['union_relaxed']) == PR
    okS += gs; ok += gr
    witness = not any(F.rank() == 0 for F in S['union_relaxed'])
    out.append({'Ms': Ms, 'strict': show_union(S['union_strict']), 'relaxed': show_union(S['union_relaxed']), 'gs': gs, 'gr': gr})
    print('%2d d=%d overlap=%s witness=%s  strict %s  relaxed %s  K10\'-strict %s relaxed %s%s  %.0fs' % (idx, d, overlap, witness,
          show_union(S['union_strict']), show_union(S['union_relaxed']), gs, gr,
          '' if gs and gr else ' PRED %s / %s' % ([FlatD.of(d, B).show() for B in PS], [FlatD.of(d, B).show() for B in PR]), time.time() - t0), flush=True)
print("K10' on random library families: strict %d of %d, relaxed %d of %d" % (okS, len(fams), ok, len(fams)))
pickle.dump(out, open(os.path.join(HERE, 'random_families%s.pkl' % ('_wit' if WIT else '')), 'wb'))
