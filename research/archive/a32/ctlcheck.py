"""Exploration only: the overlaps of the designated circle with the other eight, over roots of unity,
and the exponent-level argument that forces them."""
import cmath
from circles import coord_data, R, COORDS
C0 = coord_data(*R[0])
N = 48
roots = [cmath.exp(2j*cmath.pi*k/N) for k in range(N)]
for idx, r in enumerate(R[1:], 1):
    Cr = coord_data(*r)
    # symbolic: coordinates where both exponents are 0 must agree in sign
    const_clash = any(C0[p][1] == 0 and Cr[p][1] == 0 and C0[p][0] != Cr[p][0] for p in COORDS)
    hits = []
    for a, z in enumerate(roots):
        for b, w in enumerate(roots):
            if all(abs(C0[p][0]*z**C0[p][1] - Cr[p][0]*w**Cr[p][1]) < 1e-9 for p in COORDS[::7]):
                if all(abs(C0[p][0]*z**C0[p][1] - Cr[p][0]*w**Cr[p][1]) < 1e-9 for p in COORDS):
                    hits.append((a, b))
    print(idx, r, 'const-sign clash' if const_clash else '', 'overlaps (z k/48, w k/48):', hits)
