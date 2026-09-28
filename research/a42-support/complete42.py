"""Complete Dita membership (all label matchings; the 18 census structures and the fifth 4x4 structure in both forms =
20 structures). matchlib41.py and fifth41.json are verbatim copies from the parallel census thread (a41-census);
the valid relaxed matchings are recomputed here at SIG with exact Gaussian arithmetic."""
import json, os
from lib42 import *
import matchlib41 as ML
HERE = os.path.dirname(os.path.abspath(__file__))
def H(i, j): return SIG[i][j]
def div(x, y): return x * y.conj()          # SIG entries are unimodular
STRUCT20 = []
for nm, tr, s in STRUCTS:
    (m, n), cp, rows = s
    STRUCT20.append({'name': nm, 'transpose': tr, 'blocks': [list(b) for b in cp], 'groups': [list(g) for g in rows]})
for f in json.load(open(os.path.join(HERE, 'fifth41.json'))):
    STRUCT20.append({'name': 'k5', 'transpose': f['form'] == 'row', 'blocks': f['blocks'], 'groups': f['groups']})
import pickle
_cache = os.path.join(HERE, 'struct20_cache.pkl')
if os.path.exists(_cache):
    STRUCT20 = pickle.load(open(_cache, 'rb'))
else:
    for st in STRUCT20:
        st['relaxed'] = ML.valid_per_group(H, st['blocks'], st['groups'], True, div)
        st['strict'] = ML.valid_per_group(H, st['blocks'], st['groups'], False, div)
        assert all(len(v) >= 1 for v in st['relaxed'][1:]), st['name']
    pickle.dump(STRUCT20, open(_cache, 'wb'))
def complete_members(flat):
    flat = [int(x) for x in flat]
    return [(st['name'], 'row' if st['transpose'] else 'col') for st in STRUCT20 if ML.member_complete(flat, st, True)]
if __name__ == '__main__':
    print('structures', len(STRUCT20), 'relaxed matchings per structure:', [(st['name'], st['transpose'], ML.n_matchings(st['relaxed'])) for st in STRUCT20])
    for nm, E in (('A', A38), ('B', B38), ('C', C38), ('act-38 witness', WIT38)):
        print(nm, complete_members([x for r in E for x in r]))
