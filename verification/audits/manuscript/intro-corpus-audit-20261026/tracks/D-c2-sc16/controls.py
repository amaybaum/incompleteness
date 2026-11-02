"""Track D controls (PREREG §4): C-LP+, C-LP+x, C-LP-, C-gap. C-2x2 and C-rec run inside sc16_search.py,
C-bij inside c2_bijective_checks.py."""
import importlib.util, sys, os
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('trackd_lib', os.path.join(HERE, 'trackd_lib.py'))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)

results = {}

# C-LP+ : Markov semigroup T^t, T non-permutation (2x2 and 3x3)
for T in ([[Fr(2, 3), Fr(1, 3)], [Fr(1, 4), Fr(3, 4)]],
          [[Fr(1, 2), Fr(1, 4), Fr(1, 4)], [Fr(0), Fr(1, 3), Fr(2, 3)], [Fr(1, 5), Fr(0), Fr(4, 5)]]):
    G = [[[Fr(int(i == j)) for j in range(len(T))] for i in range(len(T))]]
    for t in range(1, 6):
        G.append(L.matmul(G[-1], T))
    ok, bad = L.p_divisible_window(G, 5)
    results.setdefault('C-LP+', []).append(ok)

# C-LP+x : XOR law. X0 uniform, X1 uniform indep, X2 = X0 xor X1.
P = {}
for x0 in (0, 1):
    for x1 in (0, 1):
        P[(x0, x1, x0 ^ x1)] = Fr(1, 4)
G = [[[Fr(1), Fr(0)], [Fr(0), Fr(1)]]]
for t in (1, 2):
    M = [[Fr(0)] * 2 for _ in range(2)]
    for s, w in P.items():
        M[s[0]][s[t]] += w * 2  # condition on root (prob 1/2)
    G.append(M)
okx, _ = L.p_divisible_window(G, 2)
lam_ok, lam = L.divisor(G[1], G[2])
gx, dx, _ = L.gap_at(P, 1, 2)
results['C-LP+x'] = [okx and gx and dx == 1, G[1] == G[2]]

# C-LP- : §2.4 minimal model family Gamma_1 = [[2/3,1/3],[1/3,2/3]], Gamma_2 = I
G1 = [[Fr(2, 3), Fr(1, 3)], [Fr(1, 3), Fr(2, 3)]]
I2 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
ok, cert = L.divisor(G1, I2)
results['C-LP-'] = [not ok and cert is not None, not L.divisible_2x2_closed_form(G1, I2)]

# C-gap: build the §2.4 minimal model permutation exactly.  x in {0,1}, h in {1..6} -> index h-1
nV, nH = 2, 6
def idx(x, h): return x * nH + (h - 1)
perm = list(range(12))
for (a, b) in [((0, 1), (1, 1)), ((0, 2), (1, 2)), ((0, 3), (0, 4)), ((0, 5), (0, 6)), ((1, 3), (1, 4)), ((1, 5), (1, 6))]:
    i, j = idx(*a), idx(*b)
    perm[i], perm[j] = j, i
Gm = L.rooted_family(perm, nV, nH, 2)
trajs = L.trajectories(perm, nV, nH, 3)
Pm = L.law_from_trajs(trajs)
g1, d1, w1 = L.gap_at(Pm, 1, 2)
# exact paper values: P(x2=0 | x1=1, x0=0) = 1, P(x2=0 | x1=1) = 1/3
M2 = L.marginal(Pm, 3); M1 = L.marginal(Pm, 2)
cond_full = M2[(0, 1, 0)] / M1[(0, 1)]
cond_x1 = sum(w for s, w in M2.items() if s[1] == 1 and s[2] == 0) / sum(w for s, w in M1.items() if s[1] == 1)
okm, badm = L.p_divisible_window(Gm, 2)
results['C-gap'] = [g1, cond_full == 1, cond_x1 == Fr(1, 3), Gm[1] == G1, Gm[2] == I2, not okm]

# decoupled bijection: phi(x,h) = (1-x, (h+x+1) mod 3) on (2,3): T permutation, no gap at any order
nV, nH = 2, 3
perm = [0] * 6
for x in range(2):
    for h in range(3):
        perm[x * 3 + h] = (1 - x) * 3 + (h + x + 1) % 3
assert sorted(perm) == list(range(6))
Lord = L.perm_order(perm)
Pd = L.law_from_trajs(L.trajectories(perm, nV, nH, Lord + 2))
results['C-gap'].append(not any(L.gap_at(Pd, k, 2)[0] for k in range(1, Lord + 1)))

allgreen = all(all(v) for v in results.values())
for k, v in results.items():
    print(f'{k:8s} {"GREEN" if all(v) else "RED"}  {v}')
print('CONTROLS', 'ALL GREEN' if allgreen else 'FAILED')
sys.exit(0 if allgreen else 1)
