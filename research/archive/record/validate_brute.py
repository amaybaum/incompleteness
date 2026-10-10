"""V1: window simulator == brute-force enumeration of the full cone for invasive (non-injective) interfaces."""
import random
from fractions import Fraction as Fr
from itertools import product
import numpy as np
from record_sim import run, F_bits

def brute(protocol, rule, kappa):
    T = sum(1 for s in protocol if s in 'oimp')
    R = max(T, 1)
    n = 2 * R + 1
    W = 1 << (2 * n)
    idx = np.arange(W, dtype=np.int64)
    u = np.stack([(idx >> (2 * k)) & 1 for k in range(n)])
    v = np.stack([(idx >> (2 * k + 1)) & 1 for k in range(n)])
    c = R
    rec = np.zeros(W, dtype=np.int64)
    for s in protocol:
        if s in 'om':
            b = v[c].copy()
            p = u[c] + 2 * b
            newp = np.zeros(W, dtype=np.int64)
            for uu in (0, 1):
                for bb in (0, 1):
                    newp[(u[c] == uu) & (b == bb)] = kappa[bb][uu]
            u[c], v[c] = newp & 1, newp >> 1
            if s == 'o':
                rec = (rec << 1) | b
        if s == 'f':
            v[c] ^= 1
        if s == 's':
            u[c], v[c] = v[c].copy(), u[c].copy()
        if s in 'oim':
            l = np.roll(v, 1, axis=0); r = np.roll(v, -1, axis=0)
            nv = F_bits(l, v, r, rule) ^ u
            u, v = v, nv          # boundary sites wrong; they never reach the centre within T leaps
    k = protocol.count('o')
    cnt = np.bincount(rec, minlength=1 << k)
    return [Fr(int(x), W) for x in cnt]

random.seed(11)
inj = [(a, b) for a in range(4) for b in range(4) if a != b]
ok = True
for rule in ('linear', 'nonlinear', 'majority'):
    bad = n = 0
    for trial in range(40):
        kappa = (random.choice(inj), random.choice(inj))
        pr = ''.join(random.choice('oimfs') for _ in range(random.randint(1, 6)))
        if sum(1 for s in pr if s in 'oim') > 4:
            continue
        c, tot = run(pr, rule, kappa)
        n += 1
        if [Fr(x, tot) for x in c] != brute(pr, rule, kappa):
            bad += 1
    print(f'V1 {rule}: {n} random (interface, protocol) pairs, mismatches {bad}')
    ok = ok and bad == 0
print('V1', 'OK' if ok else 'FAILED')
