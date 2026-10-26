import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from indep import companion, order_of_z
from search import observers, counts, chi_hits, windows
n = 5; N = 64
prims = []
for low in range(1 << n):
    if not low & 1: continue
    taps = {i for i in range(n) if (low >> i) & 1}
    if order_of_z(n, taps) == 2 ** n - 1: prims.append(taps)
print('primitive degree-5 polys (tap sets):', [sorted(t) for t in prims])
obs = observers(2)
allab = None
for taps in prims:
    L = np.array(companion(n, taps)); L2 = L[L]; f = np.arange(32) & 1
    out = counts(2, obs, L, L2, f, n, 7)
    H, chis = chi_hits(out, 2)
    ab, sg = windows(H, N, 7)
    w = H[4:8, 2361, 0]
    signs = np.sign(8 * H[4:8] - 4 * N)
    mixed = (ab & ~((signs > 0).all(0) | (signs < 0).all(0))).sum()
    print(sorted(taps), 'witness Pr-1/2 at 4..7:', [f'{int(2*x-N)}/{2*N}' for x in w],
          'abs pairs', int(ab.sum()), 'signed', int(sg.sum()), 'mixed-sign abs', int(mixed))
    allab = ab if allab is None else (allab & ab)
print('family-wide abs pairs at K=7:', int(allab.sum()))
