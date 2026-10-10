import pickle, time
from math import gcd
from fractions import Fraction as Fr
hulls, DF, GAUGE, C_SIG, Tc, Tr, K = pickle.load(open('p4/state4.pkl', 'rb'))
src = open('wt-probe4/verification/lean/dita_hierarchy_probe.py').read(); exec(src[src.index('def rank_int'):src.index('def defect_rows')])

def rank_ff(rows):
    """fraction-free integer elimination: rows are distinct primitive integer vectors; forward elimination with
    cross-multiplication and gcd normalization; rank = number of pivots"""
    seen = set(); M = []
    for r in rows:
        t = tuple(r)
        if t in seen: continue
        seen.add(t); M.append(list(r))
    return rank_int(M) if M else 0

allv = [v for _, _, vecs in hulls for v in vecs]
print('rows', len(GAUGE + allv), 'distinct', len(set(tuple(v) for v in GAUGE + allv)))
t = time.time(); r = rank_int(GAUGE + allv); print('rank_int big', r - 31, '%.1fs' % (time.time() - t))
t = time.time(); r = rank_ff(GAUGE + allv); print('rank_ff big (dedupe)', r - 31, '%.1fs' % (time.time() - t))
t = time.time(); rs = sorted(set(rank_int(GAUGE + v) - 31 for _, _, v in hulls)); print('492 rank_int', rs, '%.1fs' % (time.time() - t))
t = time.time(); rs = sorted(set(rank_ff(GAUGE + v) - 31 for _, _, v in hulls)); print('492 rank_ff', rs, '%.1fs' % (time.time() - t))
t = time.time(); r = rank_int(DF); print('rank_int DF', r, '%.1fs' % (time.time() - t))
t = time.time(); print('T ranks', rank_int(GAUGE + Tc) - 31, rank_int(GAUGE + Tr) - 31, rank_int(GAUGE + Tc + Tr) - 31, '%.1fs' % (time.time() - t))
