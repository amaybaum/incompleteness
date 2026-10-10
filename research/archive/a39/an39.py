import pickle, collections
from flats import Flat, TORUS
d = pickle.load(open('locus39.pkl','rb'))
res = d['res']; print({k:v for k,v in d.items() if k!='res'})
def desc(B):
    if B is None: return 'EMPTY'
    F = Flat.of(B); return 'dim %d comps %d : %s' % (F.dim(), F.components(), F.describe())
cnt = collections.Counter()
for cand, Bs, Br in res:
    form, mn, cp, rows = cand
    cnt[(form, mn, None if Bs is None else Flat.of(Bs).dim(), None if Br is None else Flat.of(Br).dim())] += 1
for k,v in sorted(cnt.items(), key=str): print(k, v)
print()
for cand, Bs, Br in res:
    form, mn, cp, rows = cand
    print(form, mn, '| strict', desc(Bs), '| relaxed', desc(Br))
