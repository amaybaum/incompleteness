"""Monte Carlo (evidence only, not exact): tails of the visible run-length distributions.

Second-order rule on a ring of N sites (N >> 2T, so the ring is exact for T steps by the causal cone),
uniform initial (u, v); every site is a visible observer (identically distributed processes).
For each site, record the length of the zero run starting at time 0 (capped at T), conditioned on
x_0 = 1 (a run that starts fresh).  Report the survival function S(m) = P(run >= m | start), and
its frozen-run limit.  A finite-rank process has |S(m) - S(inf)| <= C rho^m (exponential); a power
law here is the signature of infinite rank (criterion R2).
"""
import sys
import numpy as np


def step(u, v, rule):
    l, r = np.roll(v, 1), np.roll(v, -1)
    if rule == 'majority':
        F = (l & r) | (l & v) | (r & v)
    elif rule == 'nonlinear':
        F = (l & r) ^ v
    else:
        F = l ^ r
    return v, F ^ u


def run(rule, N, T, seed):
    rng = np.random.default_rng(seed)
    u = rng.integers(0, 2, N, dtype=np.uint8)
    v = rng.integers(0, 2, N, dtype=np.uint8)
    rec = np.zeros((T + 1, N), dtype=np.uint8)
    rec[0] = v
    for t in range(1, T + 1):
        u, v = step(u, v, rule)
        rec[t] = v
    return rec


if __name__ == '__main__':
    rule = sys.argv[1]
    T = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    N = 200000
    reps = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    surv = np.zeros(T + 1)
    tot = 0
    for s in range(reps):
        rec = run(rule, N, T, 1000 + s)
        # runs of zeros starting at t = 1 after a 1 at t = 0, at sites spaced 2T+... apart are independent;
        # all sites are used (correlated but identically distributed)
        start = rec[0] == 1
        z = rec[1:] == 0
        alive = start.copy()
        tot += start.sum()
        surv[0] += start.sum()
        for m in range(1, T + 1):
            alive &= z[m - 1]
            surv[m] += alive.sum()
    S = surv / tot
    for m in (4, 6, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 80, 100, 120, 150):
        if m <= T:
            print(f'MC {rule} S({m}) = {S[m]:.6f}   S(m)-S({T}) = {S[m]-S[T]:.6f}')
