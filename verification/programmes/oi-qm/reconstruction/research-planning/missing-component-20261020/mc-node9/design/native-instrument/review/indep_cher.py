"""Reviewer: C-HER recomputation, w-dependent herald (acceptance halved for +-R), own code."""
import importlib.util, sys
from fractions import Fraction as Fr
sys.path.insert(0, '.')
import indep_register as R  # reviewer's own module (prints its results on import)
def her(q):
    return {1: q, 2: (1 - q) * q, 'f': (1 - q) ** 2}
def single_h(st, a):
    q = Fr(625, 4096) * (Fr(1, 2) if st[1] == 'R' else 1)
    H1, H2 = her(q), R.HER
    K = {('F',): H1['f']}; ia = R.NAMES.index(a)
    for j in (1, 2):
        for lam, pl in R.LAM[st].items():
            for j2 in (1, 2, 'f'):
                k = (j, lam[ia], j2); K[k] = K.get(k, 0) + H1[j] * pl * H2[j2]
    return K
res = {a: (R.ids_hold({s: single_h(s, a) for s in R.STATIONS}), R.tv({s: single_h(s, a) for s in R.STATIONS})) for a in R.NAMES}
print('C-HER per setting (identities hold?, TV):', {a: (h, str(t)) for a, (h, t) in res.items()})
print('max TV', max(t for _, t in res.values()), '== 9068125/2^26:', max(t for _, t in res.values()) == Fr(9068125, 2 ** 26))
