"""Exact check: number of nearest-neighbour edges of Z^3 cut by a plane n.x = c, per unit Euclidean area of the
plane, for three normals. A lattice plane with integer normal m has cut-edge density sum_j |m_j| / |m| per unit area
(ell_1 / ell_2 of the normal); computed here by direct counting in a periodic box."""
import itertools, math
from fractions import Fraction
def cut_density(m, L):
    # periodic box of side L (L multiple of all needed periods); count edges (x, x+e_j) with m.x < c <= m.(x+e_j) mod period
    # region: sites with (m.x mod P) < P/2 ; boundary = two parallel planes; area of each plane in the torus = L^3/ (P/|m|) ... use direct count
    P = sum(abs(a) for a in m) * 2 * L  # not used
    cnt = 0
    for x in itertools.product(range(L), repeat=3):
        s = sum(a*b for a, b in zip(m, x))
        inside = (s % L) < L // 2
        for j in range(3):
            y = list(x); y[j] = (y[j] + 1) % L
            t = sum(a*b for a, b in zip(m, y))
            if ((t % L) < L // 2) != inside:
                cnt += 1
    # the region {m.x mod L < L/2} has 2 boundary planes per period; total plane area in the torus = 2 * L^3 * |m| / L
    area = 2 * L**3 * math.sqrt(sum(a*a for a in m)) / L
    return cnt, area, cnt / area
for m in [(1, 0, 0), (1, 1, 0), (1, 1, 1)]:
    c, a, d = cut_density(m, 12)
    print(m, 'cut edges', c, 'plane area', round(a, 3), 'edges per unit area', round(d, 4),
          'predicted ell1/ell2', round(sum(map(abs, m)) / math.sqrt(sum(v*v for v in m)), 4))
