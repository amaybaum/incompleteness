import sys
from fractions import Fraction as Fr
sys.path.insert(0, sys.argv[1]); import controls_gen as cg
D = 7
N = [[Fr(0)] * D for _ in range(D)]
for i, h in enumerate([1, 1, -1, -1, -1, -1, 1]): N[i][i] = Fr(h)      # (X1..X6, S)
z = [Fr(int(i == 2)) for i in range(D)]
r = cg.build_F(D, z, N)
print('eball 7, family pair: frame consistent', r is not None, '; free entries', len(r[0]) if r else None, '; dim F', len(r[2]) if r else None)
# Omega_h pair for comparison
Nh = [[Fr(0)] * D for _ in range(D)]
for i, h in enumerate([1, 1, -1, -1, 1, -1, -1]): Nh[i][i] = Fr(h)
zh = [Fr(int(i == 3)) for i in range(D)]
r2 = cg.build_F(D, zh, Nh); print('omegah pair: dim F', len(r2[2]))
