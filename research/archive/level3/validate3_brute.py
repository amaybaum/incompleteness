"""PREREG-3A section 6 item 2: record3_sim.run3 == brute-force full-cone enumeration (validate_brute.py, sealed,
extended with the letter c) on 40 random (interface, protocol) pairs per rule; all three rules exercise the
rule-generic code; outputs are validation samples, not results."""
import random
from fractions import Fraction as Fr
import numpy as np
from record3_sim import run3, F_bits


def brute(protocol, rule, kappa):
    T = sum(1 for s in protocol if s in 'oimp')
    R = max(T, 1)
    n = 2 * R + 1
    W = 1 << (2 * n)
    idx = np.arange(W, dtype=np.int64)
    u = np.stack([(idx >> (2 * k)) & 1 for k in range(n)])
    v = np.stack([(idx >> (2 * k + 1)) & 1 for k in range(n)])
    ctr = R
    rec = np.zeros(W, dtype=np.int64)
    for s in protocol:
        if s in 'om':
            b = v[ctr].copy()
            newp = np.zeros(W, dtype=np.int64)
            for uu in (0, 1):
                for bb in (0, 1):
                    newp[(u[ctr] == uu) & (b == bb)] = kappa[bb][uu]
            u[ctr], v[ctr] = newp & 1, newp >> 1
            if s == 'o':
                rec = (rec << 1) | b
        if s == 'f':
            v[ctr] ^= 1
        if s == 's':
            u[ctr], v[ctr] = v[ctr].copy(), u[ctr].copy()
        if s == 'c':
            u[ctr] = u[ctr] ^ v[ctr]
        if s in 'oim':
            l = np.roll(v, 1, axis=0)
            r = np.roll(v, -1, axis=0)
            nv = F_bits(l, v, r, rule) ^ u
            u, v = v, nv          # boundary sites wrong; they never reach the centre within T leaps
    k = protocol.count('o')
    cnt = np.bincount(rec, minlength=1 << k)
    return [Fr(int(x), W) for x in cnt]


random.seed(31)
inj = [(a, b) for a in range(4) for b in range(4) if a != b]
ok = True
for rule in ('linear', 'nonlinear', 'majority'):
    bad = n = 0
    while n < 40:
        kappa = (random.choice(inj), random.choice(inj))
        pr = ''.join(random.choice('oimfsc') for _ in range(random.randint(1, 7)))
        if sum(1 for s in pr if s in 'oim') > 4 or 'c' not in pr:
            continue
        c, tot = run3(pr, rule, kappa)
        n += 1
        if [Fr(x, tot) for x in c] != brute(pr, rule, kappa):
            bad += 1
    print(f"V1' {rule}: {n} random (interface, protocol) pairs containing c, mismatches {bad}")
    ok = ok and bad == 0
print("V1'", 'OK' if ok else 'FAILED')
