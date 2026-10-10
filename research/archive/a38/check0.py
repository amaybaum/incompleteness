import sys, time; sys.path.insert(0, 'a38')
from lib38 import *
t0 = time.time()
Wm = W_matrix()
print('W straight (tables / direct):', straight_line(Wm), straight_line_direct(Wm))
print('W gauge normal values:', sorted(set(x for r in gauge_normal(Wm) for x in r)))
print('zero E straight:', straight_line([[0]*16 for _ in range(16)]))
# a random non-straight control
import random; random.seed(1)
Er = [[random.randint(0, 1) for _ in range(16)] for _ in range(16)]
print('random E straight (tables / direct):', straight_line(Er), straight_line_direct(Er))
# vanishing-subset counts per pair, and the naive per-monomial lemma comparison
tot = 0; viol = 0; viol_pairs = 0
for i in range(16):
    for i2 in range(i + 1, 16):
        V = vanishing(i, i2); n = int(V.sum()); tot += n
        # naive lemma: signed count per monomial class (monomial = (q, r) exponent of z, w from SIGE)
        cls = {}
        for k in range(16):
            a1, q1, r1 = SIGE[i][k]; a2, q2, r2 = SIGE[i2][k]
            mono = (q1 - q2, r1 - r2); sgn = 1 if (a1 - a2) % 4 == 0 else -1
            assert (a1 - a2) % 2 == 0
            cls.setdefault(mono, []).append((k, sgn))
        # per-mask signed counts via numpy
        masks = np.arange(1 << 16)
        naive = np.ones(1 << 16, dtype=bool)
        for mono, lst in cls.items():
            s = np.zeros(1 << 16, dtype=np.int64)
            for k, sg in lst: s += sg * ((masks >> k) & 1)
            naive &= (s == 0)
        d = int((V & ~naive).sum())
        assert not (naive & ~V).any()
        if d: viol_pairs += 1; viol += d
print('pairs 120; total vanishing subsets', tot, '; subsets vanishing but not per-monomial balanced:', viol, 'over', viol_pairs, 'pairs')
print('%.1fs' % (time.time() - t0))
