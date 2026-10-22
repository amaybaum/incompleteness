#!/usr/bin/env python3
"""Exact exploratory checks for REPORT.md. Python 3.9+, standard library only.

No file writes, network, random sampling, or repository imports. This is a
kinematic candidate diagnostic, not a new C-SPH-1 acceptance experiment.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def depth_count(n):
    return 1 << (9 * n - 1).bit_length()


def counts(n, station, bins=16):
    """Integrate out S_z; the checked records depend only on S_x,S_y.

    Native +/-1 bit strings have binomial multiplicities. The integer normal
    speed in scaled coordinates is P=5*S_x or 4*S_x+3*S_y. Depth D ranges
    uniformly over 1..M, with M >= 9*n > all positive P.
    """
    require(n > 0 and n % 2 == 1, 'use a positive odd block length')
    require(station in ('X', 'R'), 'unknown station')
    result = Counter()
    clock = [0] * bins
    for k in range(n + 1):
        x = 2 * k - n
        for ell in range(n + 1):
            y = 2 * ell - n
            multiplicity = comb(n, k) * comb(n, ell)
            p = 5 * x if station == 'X' else 4 * x + 3 * y
            if p <= 0:
                continue
            require(p <= depth_count(n), 'speed exceeds depth range')
            result['success'] += multiplicity * p
            coprime_part = p
            while coprime_part % 5 == 0:
                coprime_part //= 5
            # D/P has denominator divisible by 5 unless D is divisible by
            # the entire power of 5 dividing P: exactly p-coprime_part depths.
            result['denominator_event'] += multiplicity * (p - coprime_part)
            read_sign = 4 * x + 3 * y if station == 'X' else x
            require(read_sign != 0, 'unexpected readout tie')
            result['read_plus'] += multiplicity * p * int(read_sign > 0)
            for j in range(1, bins + 1):
                clock[j - 1] += multiplicity * ((j * p) // bins - ((j - 1) * p) // bins)
    require(sum(clock) == result['success'], 'clock bins do not partition success')
    return result, clock, depth_count(n) * 2 ** (2 * n)


def direct_counts(n, station):
    """Separate path: enumerate bit strings and every depth; reduce each time."""
    out = Counter()
    for bits in product((-1, 1), repeat=2 * n):
        x, y = sum(bits[:n]), sum(bits[n:])
        p = 5 * x if station == 'X' else 4 * x + 3 * y
        for depth in range(1, depth_count(n) + 1):
            if 0 < depth <= p:
                timestamp = F(depth, p)
                out['success'] += 1
                out['denominator_event'] += int(timestamp.denominator % 5 == 0)
                out['read_plus'] += int((4 * x + 3 * y if station == 'X' else x) > 0)
    return out


def retry_clock_tv(xbins, rbins, denominator, attempts):
    """Exact TV on first-success attempt, clock bin, and the all-fail record."""
    fx = denominator - sum(xbins)
    fr = denominator - sum(rbins)
    common_denominator = denominator ** attempts
    total = abs(fx ** attempts - fr ** attempts)
    xpower = rpower = 1
    remaining = denominator ** (attempts - 1)
    for attempt in range(1, attempts + 1):
        total += remaining * sum(abs(xpower * x - rpower * r) for x, r in zip(xbins, rbins))
        xpower *= fx
        rpower *= fr
        if attempt < attempts:
            remaining //= denominator
    return F(total, 2 * common_denominator)


def main():
    print('OI emission-map diagnostic v1: exact counts; exploratory, no acceptance threshold')
    for n in (1, 3):
        for station in ('X', 'R'):
            closed, _, _ = counts(n, station)
            require(closed == direct_counts(n, station), 'direct/counting mismatch')
    print('Independent microstate/depth enumeration: n=1,3; X,R: PASS')
    print('n | X->R plus | R->X plus | E given success, X | E given success, R')
    for n in (1, 3, 7, 15, 31, 63, 127):
        x, _, _ = counts(n, 'X')
        r, _, _ = counts(n, 'R')
        values = (F(x['read_plus'], x['success']), F(r['read_plus'], r['success']),
                  F(x['denominator_event'], x['success']), F(r['denominator_event'], r['success']))
        print(str(n) + ' | ' + ' | '.join(format(float(v), '.9f') for v in values))
    print('Angular reference for these two reads: 9/10; comparison only, not a sampling input')

    n, attempts, bins = 63, 256, 16
    x, xb, denominator = counts(n, 'X', bins)
    r, rb, denominator_r = counts(n, 'R', bins)
    require(denominator == denominator_r, 'different base sample spaces')
    px, pr = F(x['success'], denominator), F(r['success'], denominator)
    cx, cr = 1 - (1 - px) ** attempts, 1 - (1 - pr) ** attempts
    ex = cx * F(x['denominator_event'], x['success'])
    er = cr * F(r['denominator_event'], r['success'])
    gap = ex - er
    require(gap > F(1, 2), 'exact-time witness missing')
    coarse = retry_clock_tv(xb, rb, denominator, attempts)
    require(F(0) <= coarse <= F(1), 'invalid coarse-record TV')
    require(coarse < gap, 'coarsening control did not reduce distinction')
    # The denominator event cannot be a function of the 16-bin clock:
    # 1/5 and 2/9 occur for available velocities, share a bin, but disagree on E.
    require((16 * 1 + 5 - 1) // 5 == (16 * 2 + 9 - 1) // 9, 'bin counterexample')
    require(F(1, 5).denominator % 5 == 0 and F(2, 9).denominator % 5 != 0,
            'denominator counterexample')
    print('Witness: n=63; M=1024; at most 256 fresh trials')
    print('Completion X,R: %.12f %.12f' % (float(cx), float(cr)))
    print('Full-record event probabilities X,R: %.12f %.12f' % (float(ex), float(er)))
    print('Full-record TV lower bound: %.12f; exact comparison > 1/2: PASS' % float(gap))
    print('16-bin herald-record TV: %.12f' % float(coarse))
    print('Timing coarsening countercontrol: PASS; does not establish physical access closure')
    print('PASS: exact diagnostic identities and witness; candidate NOT accepted as an OI instrument')


if __name__ == '__main__':
    main()
