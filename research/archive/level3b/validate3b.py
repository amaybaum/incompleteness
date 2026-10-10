"""Design-time validation of the 3B instrument (no result run): rule census; hsim3b on H0 == record3_sim.run3 and
== record3_fast.run_all3; hsim3b on H1/H2 == an independent brute-force cone enumeration; timing of one kappa's
Stage-A protocol set under the enumerator."""
import os
import sys
import time
import random
from fractions import Fraction as Fr
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
for sub in ('record', 'level3', 'quotient', 'level3b'):
    sys.path.insert(0, os.path.join(HERE, '..', sub))
import rules3b                                    # noqa: E402  installs F3B
import hsim3b                                     # noqa: E402
import record3_sim                                # noqa: E402
import record3_fast                               # noqa: E402
import record_sim                                 # noqa: E402

random.seed(3)
PALPH, EALPH = 'oifsc', 'oimfsc'


def norm(counts, mass):
    return tuple(Fr(c, mass) for c in counts)


def brute(protocol, rule, kappa, H):
    """Independent brute force: enumerate initial (u, v) on |i| <= R (R = T + 1), step the CA explicitly."""
    T = sum(1 for s in protocol if s in 'oimp')
    R = T + 1
    sites = list(range(-R, R + 1))
    n = len(sites)
    counts = {}
    mass = 0
    for vbits in range(1 << n):
        v0 = {i: (vbits >> (i + R)) & 1 for i in sites}
        if H == 'H1':
            wv = 1
            for i in range(-R, R):
                wv *= 3 if v0[i] == v0[i + 1] else 1
            urange = range(1 << n)
        elif H == 'H0':
            wv = 1
            urange = range(1 << n)
        elif H == 'H2':
            wv = 1
            urange = [sum(v0[i] << (i + R) for i in sites)]
        for ubits in urange:
            u = {i: (ubits >> (i + R)) & 1 for i in sites}
            v = dict(v0)
            rec = 0
            for s in protocol:
                if s in 'om':
                    b = v[0]
                    q = kappa[b][u[0]]          # kappa_b maps u to a pair code u' + 2 v'
                    u[0], v[0] = q & 1, q >> 1
                    if s == 'o':
                        rec = 2 * rec + b
                elif s in 'fsc':
                    f = hsim3b.perm_of(s)
                    q = f(u[0] | (v[0] << 1))
                    u[0], v[0] = q & 1, q >> 1
                if s in 'oimp':
                    nv = {}
                    for i in sites:
                        if abs(i) < R:
                            nv[i] = rules3b.F3B(v[i - 1], v[i], v[i + 1], rule) ^ u[i]
                        else:
                            nv[i] = 0   # boundary sites never reach site 0 (cone)
                    u, v = v, nv
            counts[rec] = counts.get(rec, 0) + wv
            mass += wv
    no = protocol.count('o')
    return norm([counts.get(r, 0) for r in range(1 << no)], mass)


def protocols(alph, L):
    return [''.join(p) for l in range(L + 1) for p in product(alph, repeat=l)]


if __name__ == '__main__':
    print('== rule census'); os.system(f'{sys.executable} {os.path.join(HERE, "rules3b.py")}')
    kappas = [((0, 1), (0, 1)), ((1, 3), (0, 2)), ((2, 0), (3, 1)), ((0, 2), (1, 3))]
    # V-H0: hsim3b on H0 == reference window simulator, all six rules, random protocols up to length 6
    bad = 0; n = 0
    for rule in rules3b.RULES:
        for _ in range(25):
            lp, le = random.randint(0, 3), random.randint(0, 3)
            pr = ''.join(random.choice(PALPH) for _ in range(lp)) + ''.join(random.choice(EALPH) for _ in range(le))
            k = random.choice(kappas)
            a = norm(*hsim3b.run_H(pr, rule, k, 'H0'))
            b = norm(*record3_sim.run3(pr, rule, k))
            n += 1; bad += (a != b)
    print(f'V-H0  hsim3b(H0) vs record3_sim.run3: {n} protocols x rules, mismatches {bad}')
    # V-fast: record3_fast (window, int64) == record3_sim for the new rules (the window argument is rule-generic)
    bad = 0; n = 0
    for rule in ('LS', 'NL', 'R5'):
        prs = [''.join(random.choice(PALPH) for _ in range(random.randint(0, 3))) +
               ''.join(random.choice(EALPH) for _ in range(random.randint(0, 3))) for _ in range(60)]
        k = random.choice(kappas)
        J = record3_fast.run_all3(prs, rule, k)
        for pr in prs:
            n += 1; bad += (norm(*J[pr]) != norm(*record3_sim.run3(pr, rule, k)))
    print(f'V-fast record3_fast == record3_sim on LS/NL/R5: {n} protocols, mismatches {bad}')
    # V-brute: hsim3b on H1/H2 (and H0) == independent brute force, small T
    bad = 0; n = 0
    for H in ('H0', 'H1', 'H2'):
        for rule in ('linear', 'R5', 'NL'):
            for _ in range(6):
                lp, le = random.randint(0, 2), random.randint(0, 2)
                pr = ''.join(random.choice(PALPH) for _ in range(lp)) + ''.join(random.choice(EALPH) for _ in range(le))
                if sum(1 for s in pr if s in 'oimp') > 3:
                    continue
                k = random.choice(kappas)
                a = norm(*hsim3b.run_H(pr, rule, k, H))
                b = brute(pr, rule, k, H)
                n += 1; bad += (a != b)
    print(f'V-brute hsim3b vs brute force on H0/H1/H2 (T <= 3): {n} protocols, mismatches {bad}')
    # V-all: whole Stage-A protocol set, one kappa, H0: hsim3b == record3_fast, and the timing (H1 costs the same)
    pps, pes = protocols(PALPH, 3), protocols(EALPH, 3)
    allp = [a + b for a in pps for b in pes]
    k = kappas[0]
    t = time.time(); J1 = record3_fast.run_all3(allp, 'linear', k); t1 = time.time() - t
    t = time.time(); J2 = hsim3b.run_all_H(allp, 'linear', k, 'H0'); t2 = time.time() - t
    mism = sum(1 for pr in allp if norm(*J1[pr]) != norm(*J2[pr]))
    print(f'V-all  Stage-A set ({len(allp)} protocols), kappa {k}: window {t1:.0f}s, enumerator(H0) {t2:.0f}s, mismatches {mism}')
    t = time.time(); J3 = hsim3b.run_all_H(allp, 'linear', k, 'H1'); t3 = time.time() - t
    print(f'TIMING enumerator(H1) Stage-A set one kappa: {t3:.0f}s  (masses: {sorted(set(m for _, m in J3.values()))[:6]} ...)')
