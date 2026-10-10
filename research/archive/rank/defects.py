"""Defect kinematics census (Monte Carlo, evidence): where does a defect at (i, t) have a defect at t+1?
Defect: majority -> site value differs from both neighbours; nonlinear -> both neighbours equal 1.
Also the space-time autocorrelation along the light-cone diagonals over k steps."""
import sys
import numpy as np
from runs_mc import step
rule, N, T = sys.argv[1], 400000, 60
rng = np.random.default_rng(11)
u = rng.integers(0, 2, N, dtype=np.uint8); v = rng.integers(0, 2, N, dtype=np.uint8)
D = []
for t in range(T):
    l, r = np.roll(v, 1), np.roll(v, -1)
    d = ((v != l) & (v != r)) if rule == 'majority' else ((l == 1) & (r == 1))
    D.append(d.astype(np.float64))
    u, v = step(u, v, rule)
D = np.array(D)
rho = D.mean()
print(f'DEFECT {rule}: density {rho:.4f}')
for k in (1, 2, 4, 8, 16, 32):
    row = []
    for dx in range(-k - 1, k + 2):
        c = (D[:-k] * np.roll(D[k:], -dx, axis=1)).mean() / rho
        row.append(f'{c:.3f}')
    print(f'DEFECT {rule} k={k}: P(defect at (i+dx, t+k) | defect at (i,t)), dx=-{k+1}..{k+1}:', ' '.join(row))
