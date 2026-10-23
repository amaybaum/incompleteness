#!/usr/bin/env python3
"""Scoped exploratory checks; no file/network I/O or random sampling.

These are not an apparatus acceptance test or a proof that OI cannot work.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def fourth_relation_by_axis():
    # Independent integer-coordinate construction of review13's alternative
    # frames, with velocities scaled by 25. Negative stations invert velocity.
    n = 15
    weights = [(2*i-n, comb(n, i)) for i in range(n+1)]
    result = {}
    for axis in 'XYZR':
        laws = {s: Counter() for s in 'XYR'}
        herald = Counter()
        for x, wx in weights:
            if x <= 0:
                continue
            plus = dict.fromkeys('XYR', 0)
            for y, wy in weights:
                for z, wz in weights:
                    velocities = {
                        'X': (25*x, 25*y, 25*z),
                        'Y': (25*z, 25*x, 25*y),
                        'R': (20*x-9*y+12*z, 15*x+12*y-16*z, 20*y+15*z),
                    }
                    for station, v in velocities.items():
                        projection = {'X': v[0], 'Y': v[1], 'Z': v[2],
                                      'R': 4*v[0]+3*v[1]}[axis]
                        require(projection != 0, 'unexpected read tie')
                        plus[station] += wy*wz*(projection > 0)
            for depth in range(1, 5*x+1):
                time = F(depth, 5*x)
                herald[time] += wx*4**n
                for station in 'XYR':
                    laws[station][time] += wx*plus[station]
        bad = sum(10*laws['R'][t]-8*laws['X'][t]-6*laws['Y'][t]+2*h != 0
                  for t, h in herald.items())
        result[axis] = (bad, len(herald))
    require(result == {'X': (245, 245), 'Y': (245, 245),
                       'Z': (0, 245), 'R': (245, 245)}, 'axis results differ')
    print('R1 fourth relation, alternative frames, n=15: nonzero positive-read atoms / timestamps')
    for axis, (bad, total) in result.items():
        print('  %s: %d / %d' % (axis, bad, total))


def frame_uniform_witness():
    # T=1/(5n) forces S_x=n and D=1. Check independently by every depth.
    for n in (7, 15, 63):
        pairs = [(x, d) for x in range(1, n+1, 2)
                 for d in range(1, 5*x+1) if F(d, 5*x) == F(1, 5*n)]
        require(pairs == [(n, 1)], 'timestamp does not isolate frontier')
        gap_bound = F(4*n-27, 4*(16*n+9))
        require(gap_bound > 0, 'conditional uniform-frame bound not positive')
        # Sample controls for the analytical all-frame inequality, not a
        # substitute for its proof. b^2+c^2=9/25 in each transverse frame.
        for cosine, sine in ((F(1), F(0)), (F(0), F(1)),
                             (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))):
            b, c = -F(3, 5)*cosine, F(3, 5)*sine
            require(b*b+c*c == F(9, 25), 'bad transverse norm')
            counts = Counter()
            for j in range(n+1):
                y = 2*j-n
                for k in range(n+1):
                    z = 2*k-n
                    v = F(4*n, 5)+b*y+c*z
                    sign = (v > 0)-(v < 0)
                    counts[sign] += comb(n, j)*comb(n, k)
            actual_gap = (F(13, 16)*F(counts[1], 4**n)
                          +F(3, 16)*F(counts[-1], 4**n)-F(3, 4))
            require(actual_gap >= gap_bound, 'Cantelli frame bound fails')
    n, m = 63, 256
    norm = sum(5*x*comb(n, (x+n)//2) for x in range(1, n+1, 2))
    require(norm == 5*n*comb(n-1, (n-1)//2), 'normal count identity')
    depth_size = 1 << (9*n-1).bit_length()
    p = F(norm, depth_size*2**n)
    completion = 1-(1-p)**m
    bound = completion*F(4*n-27, 4*(16*n+9)*norm)
    require(bound > 0, 'no complete-record witness')
    print('R2 all-frame analytical witness: conditional gap bound at n=63 = %s' % F(4*n-27, 4*(16*n+9)))
    print('  Complete-record lower bound, n=63 m=256: %.12e' % float(bound))
    print('  Timestamp isolation and 12 rational-frame controls PASS; asymptotic error floor NOT claimed')


def affine_and_gate_checks():
    inputs = list(product((0, 1), repeat=2))
    target = []
    for a, b in inputs:
        normal, depth = 5*(2*a-1), 1+8*b
        hit = int(0 < depth <= normal)
        require(hit == a*(1-b), 'crossing slice is not AND-NOT')
        target.append(hit)
    require(sum(target) % 2 == 1, 'target rectangle parity')
    agreements = []
    for offset, ca, cb in product((0, 1), repeat=3):
        outputs = [(offset+ca*a+cb*b) % 2 for a, b in inputs]
        require(sum(outputs) % 2 == 0, 'affine rectangle parity')
        agreements.append(sum(x == y for x, y in zip(outputs, target)))
    require(max(agreements) == 3, 'affine gate obstruction absent')
    # Nonlinear readout of an unchanged two-bit register evades the narrow
    # raw-bit restriction. It is NOT implemented by this identity update.
    require([int((a, b) == (1, 0)) for a, b in inputs] == target, 'macro-decoder control')
    print('R3 crossing slice %s; all 8 affine Boolean outputs fail; best agreement 3/4' % target)
    print('  Nonlinear macro-decoder countercontrol PASS; general observation maps NOT ruled out')


def force(current):
    a, b, detector = current
    return (0, 0, a*b)


def step(state):
    previous, current = state[:3], state[3:]
    following = tuple(a ^ b for a, b in zip(previous, force(current)))
    return current+following


def inverse(state):
    current, following = state[:3], state[3:]
    previous = tuple(a ^ b for a, b in zip(following, force(current)))
    return previous+current


def nonlinear_controls():
    states = list(product((0, 1), repeat=6))
    require(len({step(s) for s in states}) == 64, 'nonlinear phase map not bijective')
    require(all(inverse(step(s)) == s and step(inverse(s)) == s for s in states), 'inverse fails')
    for a, b in product((0, 1), repeat=2):
        current = (a, 1-b, 0)
        state = current+current
        require(step(state)[-1] == a*(1-b), 'nonlinear write fails')
        # These ready control values remain constant, but the detector does
        # not latch forever: record returns to zero at tick 3.
        for _ in range(3):
            state = step(state)
        require(state[-1] == 0, 'unexpected latch behavior')
    quadratic, linear = Counter(), Counter()
    for bits in product((0, 1), repeat=6):
        value = sum(bits[i]*bits[j] for i in range(6) for j in range(i+1, 6)) % 2
        quadratic[value] += 1
        linear[sum(bits) % 2] += 1
    independent_count = sum(comb(6, k) for k in range(7) if (k*(k-1)//2) % 2)
    require(quadratic[1] == independent_count == 36 and linear[1] == 32, 'source-law countercontrol')
    print('R4 nonlinear second-order gate: full inverse and bijection 64/64; write 4/4; no persistent latch')
    print('  Cubic-symmetric quadratic force, ready old port=0: P(next=1)=9/16; linear control=1/2')


def majority_force(bits):
    px, py, pz = (bits[2*j] ^ bits[2*j+1] for j in range(3))
    return (px*py) ^ (py*pz) ^ (pz*px)


def balanced_nonlinear_control():
    words = list(product((0, 1), repeat=6))
    for shift in words:
        require(sum(majority_force(tuple(a ^ b for a, b in zip(word, shift)))
                    for word in words) == 32, 'shifted balance failed')
    for a, b in product((0, 1), repeat=2):
        require(majority_force((a, 0, 1-b, 0, 0, 0)) == a*(1-b), 'majority write failed')
    # Actual cubic update for an isolated pulse, not a circuit surrogate.
    side = 5
    sites = list(product(range(side), repeat=3))
    neighbors = {}
    for site in sites:
        row = []
        for axis in range(3):
            for direction in (-1, 1):
                v = list(site)
                v[axis] = (v[axis]+direction) % side
                row.append(tuple(v))
        neighbors[site] = row
    previous = {site: 0 for site in sites}
    pulse = {site: int(site == (0, 0, 0)) for site in sites}
    def advance(old, current, force_rule):
        return {site: old[site] ^ force_rule(tuple(current[v] for v in neighbors[site]))
                for site in sites}
    current = pulse
    populations = []
    for _ in range(4):
        following = advance(previous, current, majority_force)
        populations.append(sum(following.values()))
        previous, current = current, following
    require(populations == [0, 1, 0, 1], 'isolated pulse behavior changed')
    linear_next = advance({site: 0 for site in sites}, pulse, lambda bits: sum(bits) % 2)
    require(sum(linear_next.values()) == 6, 'linear propagation control failed')
    print('R5 pair-parity majority rule: balanced for all 64 shifts; crossing-bit write 4/4')
    print('  Two-tick freshness follows analytically from balance and independent old-neighbor values')
    print('  Actual 5^3 torus isolated-pulse populations at ticks 1..4: [0, 1, 0, 1]; linear tick 1: 6')


def main():
    print('Detector-boundary diagnostic v1: exact scoped checks; NOT apparatus acceptance')
    fourth_relation_by_axis()
    frame_uniform_witness()
    affine_and_gate_checks()
    nonlinear_controls()
    balanced_nonlinear_control()
    print('PASS: review corrections, all-frame witness controls, and specified detector boundaries')


if __name__ == '__main__':
    main()
