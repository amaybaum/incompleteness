"""Valid label matchings at SIG for the 18 census index structures (exact monomial arithmetic, factorized by group),
every per-group verdict cross-checked with Gaussian-rational arithmetic. Writes matchings.json."""
import itertools, json
from lib41 import *
from matchlib import *


def mdiv(x, y): return ((x[0] - y[0]) % 4, x[1] - y[1], x[2] - y[2])


def gdiv(x, y):
    n2 = y.norm2(); q = x * y.conj(); return G(q.a / n2, q.b / n2)


assert all(val(*SIGE[i][j]) == SIG[i][j] for i in range(16) for j in range(16))
out = {}
for s in CENSUS9:
    (m, n), blocks, groups = s
    for tr in (False, True):
        H = (lambda i, j: SIGE[j][i]) if tr else (lambda i, j: SIGE[i][j])
        Hg = (lambda i, j: SIG[j][i]) if tr else (lambda i, j: SIG[i][j])
        vs = valid_per_group(H, blocks, groups, False, mdiv); vr = valid_per_group(H, blocks, groups, True, mdiv)
        for rel, V in ((False, vs), (True, vr)):
            for b in range(1, n):
                for sb in itertools.permutations(range(m)):
                    assert group_valid(Hg, blocks, groups, b, sb, rel, gdiv) == (sb in V[b]), (NAMES9[s], b, sb)
        key = '%s-%s' % (NAMES9[s], 'row' if tr else 'column')
        out[key] = {'name': NAMES9[s], 'form': 'row' if tr else 'column', 'shape': [m, n], 'blocks': blocks, 'groups': groups,
                    'transpose': tr, 'strict': vs, 'relaxed': vr}
        print('%-10s per-group valid strict %s -> %5d matchings; relaxed %s -> %5d; identity valid %s' % (
            key, [len(x) for x in vs[1:]], n_matchings(vs), [len(x) for x in vr[1:]], n_matchings(vr),
            all(tuple(range(m)) in x for x in vs[1:])), flush=True)
json.dump(out, open('matchings.json', 'w'))
print('written matchings.json')
