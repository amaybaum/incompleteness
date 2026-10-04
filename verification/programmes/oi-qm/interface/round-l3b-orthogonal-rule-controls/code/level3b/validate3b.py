"""Validation gates V2-V5 of preregistration section 7.3 (run at C1, before any result run), and the brute-force
cone reference used by V5 and V11.

  V2  rule census equals the frozen table (rules3b.census)
  V3  record3_fast == record3_sim on LS, NL, R5: 180 random protocols (seed 3), four kappa
  V4  hsim3b on H0 == record3_sim on 150 random protocols over the six rules (seed 3), and == record3_fast on the
      full Stage-A set for kappa ((0,1),(0,1)), ((1,3),(0,2)), ((2,0),(3,1)) under linear and R5
  V5  hsim3b on H0, H1, H2 == brute force on 54 random protocols with <= 3 leaps (seed 3), rules linear, R5, NL

usage: validate3b.py [V2|V3|V4|V5]   (default: all four, in order; each prints a final 'GATE Vn OK|FAILED' line)
"""
import os
import sys
import time
import random
from fractions import Fraction as Fr
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
for sub in ('record', 'level3', 'quotient', 'level3b'):
    p = os.path.join(HERE, '..', sub)
    if p not in sys.path:
        sys.path.insert(0, p)
import rules3b                                    # noqa: E402  installs F3B
import hsim3b                                     # noqa: E402
import record3_sim                                # noqa: E402
import record3_fast                               # noqa: E402

PALPH, EALPH = 'oifsc', 'oimfsc'
KAPPAS = [((0, 1), (0, 1)), ((1, 3), (0, 2)), ((2, 0), (3, 1)), ((0, 2), (1, 3))]


def norm(counts, mass):
    return tuple(Fr(c, mass) for c in counts)


def brute(protocol, rule, kappa, H):
    """Independent brute force: enumerate the initial (u, v) on |i| <= R = T + 1 with the measure's weights and
    step the automaton explicitly; sites at |i| = R are frozen to 0 after the first leap (they cannot reach site 0
    within T leaps)."""
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
        else:
            raise ValueError(H)
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
                            nv[i] = 0
                    u, v = v, nv
            counts[rec] = counts.get(rec, 0) + wv
            mass += wv
    no = protocol.count('o')
    return norm([counts.get(r, 0) for r in range(1 << no)], mass)


def protocols(alph, L):
    return [''.join(p) for l in range(L + 1) for p in product(alph, repeat=l)]


def rand_protocol(rng, lp_max=3, le_max=3):
    lp, le = rng.randint(0, lp_max), rng.randint(0, le_max)
    return ''.join(rng.choice(PALPH) for _ in range(lp)) + ''.join(rng.choice(EALPH) for _ in range(le))


def gate_V2():
    rows, aff, ok = rules3b.census()
    for rule in rules3b.RULES:
        a, c, p = rows[rule]
        print(f'V2 {rule:10s} affine {str(a):5s} uses-centre {str(c):5s} permutive-in {sorted(p)}')
    print(f'V2 two-variable functions permutive in some argument: {aff}, all affine')
    print('GATE V2', 'OK' if ok else 'FAILED')
    return ok


def gate_V3():
    rng = random.Random(3)
    bad = 0
    n = 0
    for rule in ('LS', 'NL', 'R5'):
        prs = [rand_protocol(rng) for _ in range(60)]
        k = rng.choice(KAPPAS)
        J = record3_fast.run_all3(prs, rule, k)
        for pr in prs:
            n += 1
            bad += (norm(*J[pr]) != norm(*record3_sim.run3(pr, rule, k)))
    print(f'V3 record3_fast == record3_sim on LS/NL/R5: {n} protocols, mismatches {bad}')
    print('GATE V3', 'OK' if bad == 0 and n == 180 else 'FAILED')
    return bad == 0 and n == 180


def gate_V4():
    rng = random.Random(3)
    bad = 0
    n = 0
    for rule in rules3b.RULES:
        for _ in range(25):
            pr = rand_protocol(rng)
            k = rng.choice(KAPPAS)
            n += 1
            bad += (norm(*hsim3b.run_H(pr, rule, k, 'H0')) != norm(*record3_sim.run3(pr, rule, k)))
    print(f'V4 hsim3b(H0) == record3_sim on random protocols: {n}, mismatches {bad}')
    pps, pes = protocols(PALPH, 3), protocols(EALPH, 3)
    allp = [a + b for a in pps for b in pes]
    ok = bad == 0 and n == 150
    for rule in ('linear', 'R5'):
        for k in KAPPAS[:3]:
            t = time.time()
            J1 = record3_fast.run_all3(allp, rule, k)
            t1 = time.time() - t
            t = time.time()
            J2 = hsim3b.run_all_H(allp, rule, k, 'H0')
            t2 = time.time() - t
            m = sum(1 for p in allp if norm(*J1[p]) != norm(*J2[p]))
            ok &= (m == 0)
            print(f'V4 full Stage-A set {rule} {k}: {len(allp)} protocols, window {t1:.0f}s, enumerator {t2:.0f}s, mismatches {m}')
    print('GATE V4', 'OK' if ok else 'FAILED')
    return ok


def gate_V5():
    rng = random.Random(3)
    bad = 0
    n = 0
    for H in ('H0', 'H1', 'H2'):
        for rule in ('linear', 'R5', 'NL'):
            for _ in range(6):
                pr = rand_protocol(rng, 2, 2)
                if sum(1 for s in pr if s in 'oimp') > 3:
                    continue
                k = rng.choice(KAPPAS)
                n += 1
                bad += (norm(*hsim3b.run_H(pr, rule, k, H)) != brute(pr, rule, k, H))
    print(f'V5 hsim3b vs brute force on H0/H1/H2 (<= 3 leaps): {n} protocols, mismatches {bad}')
    print('GATE V5', 'OK' if bad == 0 and n == 54 else 'FAILED')
    return bad == 0 and n == 54


if __name__ == '__main__':
    which = sys.argv[1:] or ['V2', 'V3', 'V4', 'V5']
    ok = True
    for g in which:
        ok &= {'V2': gate_V2, 'V3': gate_V3, 'V4': gate_V4, 'V5': gate_V5}[g]()
    sys.exit(0 if ok else 1)
