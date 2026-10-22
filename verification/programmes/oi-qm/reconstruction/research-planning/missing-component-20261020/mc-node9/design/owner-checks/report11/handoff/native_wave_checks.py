#!/usr/bin/env python3
"""Exact checks for the bounded native-wave resource lemma (v1).

Python 3.9+; standard library only. No file writes, network, random sampling,
quantum probabilities, or repository imports. See REPORT.md for the theorem
and its scope. Failed checks raise even when Python is run with -O.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(a, b, p, coefficient=1):
    out = dict(a)
    for key, value in b.items():
        out[key] = (out.get(key, 0) + coefficient * value) % p
        if not out[key]:
            del out[key]
    return out


def scale(a, coefficient, p):
    return {key: value * coefficient % p for key, value in a.items()
            if value * coefficient % p}


def neighbours(site, length):
    for axis in range(3):
        for sign in (-1, 1):
            other = list(site)
            other[axis] = (other[axis] + sign) % length
            yield tuple(other)


def origin_forms(length, p, alpha, ticks):
    """Sparse linear forms of u_origin(-1), ..., u_origin(ticks).

    Keys are (initial_slice, site), with slice 0=past and 1=current.
    This propagates linear forms on the whole finite torus, including wrap.
    """
    sites = list(product(range(length), repeat=3))
    origin = (0, 0, 0)
    past = {site: {(0, site): 1} for site in sites}
    current = {site: {(1, site): 1} for site in sites}
    outputs = [past[origin], current[origin]]
    for _ in range(ticks):
        following = {}
        for site in sites:
            row = scale(past[site], -1, p)
            for other in neighbours(site, length):
                row = add(row, current[other], p, alpha)
            following[site] = row
        past, current = current, following
        outputs.append(current[origin])
    return outputs


def rank(rows, p):
    """Sparse Gaussian elimination over the prime field F_p."""
    basis = {}
    for original in rows:
        row = dict(original)
        while row:
            pivot = min(row)
            if pivot in basis:
                row = add(row, basis[pivot], p, -row[pivot])
            else:
                basis[pivot] = scale(row, pow(row[pivot], -1, p), p)
                break
    return len(basis)


def numeric_step(past, current, length, p, alpha):
    """Independent numeric phase update; does not use sparse-form routines."""
    following = {
        site: (alpha * sum(current[other] for other in neighbours(site, length))
               - past[site]) % p
        for site in current
    }
    return current, following


def numeric_inverse(current, following, length, p, alpha):
    past = {
        site: (alpha * sum(current[other] for other in neighbours(site, length))
               - following[site]) % p
        for site in current
    }
    return past, current


def translate_no_wrap(row, centre):
    """Lift a radius-4 form from L=9, then translate into the L=18 torus."""
    out = {}
    for (slice_, site), value in row.items():
        displacement = tuple(x if x <= 4 else x - 9 for x in site)
        target = tuple((centre[j] + displacement[j]) % 18 for j in range(3))
        key = (slice_, target)
        require(key not in out, 'translation identified distinct initial variables')
        out[key] = value
    return out


def first_success(sequence, start, window):
    for offset in range(window):
        herald, mark = sequence[start + offset]
        if herald != 0:
            return ('S', offset + 1, mark), start + offset + 1
    return ('F', window), start + window


def single_call_law(window, p=3):
    law = {('F', window): F(1, p ** window)}
    for wait in range(1, window + 1):
        for mark in range(p):
            law[('S', wait, mark)] = F(p - 1, p ** (wait + 1))
    require(sum(law.values()) == 1, 'single-call law not normalized')
    return law


def run():
    print('OI native-wave bounded resource checks v1')
    print('Arithmetic: integers modulo 3 and exact rational fractions; no sampling')

    # Positive source: L=9 is enough for four ticks at one port.
    rows = origin_forms(9, 3, 1, 4)
    initial = rows[:2]
    require(rank(initial, 3) == 2, 'initial port rank')
    increments = [rank(rows[:t + 2], 3) - 2 for t in range(1, 5)]
    require(increments == [1, 2, 3, 4], 'conditional output rank')
    for t in range(1, 5):
        pivot = (1, (t, 0, 0))
        require(rows[t + 1].get(pivot) == 1, 'fresh frontier coefficient')
        require(all(row.get(pivot, 0) == 0 for row in rows[:t + 1]),
                'frontier variable appeared prematurely')
    print('P1 PASS: L=9, four fresh pivots; conditional ranks [1, 2, 3, 4]')

    # Eight stations in ONE lattice; two field components are added by direct sum.
    centres = list(product((0, 9), repeat=3))
    ports = [[translate_no_wrap(row, centre) for row in rows] for centre in centres]
    ready = [row for port in ports for row in port[:2]]
    future = [row for port in ports for row in port[2:]]
    supports = [set().union(*(set(row) for row in port)) for port in ports]
    require(all(supports[i].isdisjoint(supports[j])
                for i in range(8) for j in range(i)), 'station supports overlap')
    require(rank(ready, 3) == 16, 'eight-port readiness rank')
    require(rank(ready + future, 3) == 48, 'eight-port joint rank')
    print('P2 PASS: L=18, eight ports; per-component ranks ready=16, joint=48')
    print('P2 COROLLARY: two components give 64 independent future trits given all 32 initial port trits')

    # Enumerate all four-tick histories of a two-component source.
    # First call has window 2; second starts immediately after success/timeout.
    # Check both fixed and history-dependent second window lengths.
    fixed = Counter()
    adaptive = Counter()
    for flat in product(range(3), repeat=8):
        sequence = list(zip(flat[::2], flat[1::2]))
        first, end = first_success(sequence, 0, 2)
        second, finish = first_success(sequence, end, 2)
        require(finish <= 4, 'fixed call exceeded horizon')
        fixed[(first, second)] += 1
        window = 1 if first[0] == 'S' and first[2] == 0 else 2
        second, finish = first_success(sequence, end, window)
        require(finish <= 4, 'adaptive call exceeded horizon')
        adaptive[(first, window, second)] += 1
    one = single_call_law(2)
    require(len(fixed) == 49, 'fixed joint record count')
    for a, pa in one.items():
        for b, pb in one.items():
            require(F(fixed[(a, b)], 3 ** 8) == pa * pb, 'fixed joint law')
        window = 1 if a[0] == 'S' and a[2] == 0 else 2
        for b, pb in single_call_law(window).items():
            require(F(adaptive[(a, window, b)], 3 ** 8) == pa * pb,
                    'adaptive-window conditional law')
    require(sum(fixed.values()) == 3 ** 8, 'fixed record mass')
    require(sum(adaptive.values()) == 3 ** 8, 'adaptive record mass')
    print('P3 PASS: all 6561 histories; all 49 fixed-window joint records factor exactly')
    print('P4 PASS: adaptive second window and start obey the conditional call law')
    print('CALL LAW: failure=1/9; each mark at wait 1=2/9; each mark at wait 2=2/27')

    # Separate enumeration: choose the second port using the first mark.
    # Two ports x two ticks x two components = eight trits.
    station_records = Counter()
    for flat in product(range(3), repeat=8):
        port0 = [(flat[0], flat[1]), (flat[2], flat[3])]
        port1 = [(flat[4], flat[5]), (flat[6], flat[7])]
        a, _ = first_success(port0, 0, 1)
        station = a[2] % 2 if a[0] == 'S' else 1
        b, _ = first_success((port0, port1)[station], 1, 1)
        station_records[(a, station, b)] += 1
    one_tick = single_call_law(1)
    for a, pa in one_tick.items():
        station = a[2] % 2 if a[0] == 'S' else 1
        for b, pb in one_tick.items():
            require(F(station_records[(a, station, b)], 3 ** 8) == pa * pb,
                    'adaptive station law')
    require(len(station_records) == 16, 'adaptive station record count')
    print('P5 PASS: all 6561 two-port histories; adaptive station choice, 16 records')

    # Correlated initial preparation: impose the linear constraint u_2=u_1.
    shared = add(rows[3], rows[2], 3, -1)
    require(rank(initial + [shared], 3) == 3, 'shared constraint rank')
    require(rank(initial + [shared, rows[2]], 3) == 4, 'first marginal lost uniformity')
    require(rank(initial + [shared, rows[3]], 3) == 4, 'second marginal lost uniformity')
    require(rank(initial + [shared, rows[2], rows[3]], 3) == 4,
            'shared constraint did not correlate outputs')
    correlated_pairs = [(a, b) for a, b in product(range(3), repeat=2) if a == b]
    correlated_sf = F(sum(a != 0 and b == 0 for a, b in correlated_pairs), len(correlated_pairs))
    independent_sf = F(sum(a != 0 and b == 0 for a, b in product(range(3), repeat=2)), 9)
    require(correlated_sf == 0 and independent_sf == F(2, 9), 'shared-preparation witness')
    print('N1 DETECTED: shared preparation keeps uniform marginals; success/failure=0 versus 2/9')

    # If spatial coupling vanishes, no unknown external variable can arrive.
    zero = origin_forms(9, 3, 0, 4)
    require(rank(zero, 3) - rank(zero[:2], 3) == 0, 'zero-coupling control')
    print('N2 DETECTED: alpha=0 gives zero conditional output rank')

    # Access to neighbours discloses the linear combination determining u_1.
    probes = [{(1, other): 1} for other in neighbours((0, 0, 0), 9)]
    probe_rank = rank(initial + probes, 3)
    require(rank(initial + probes + [rows[2]], 3) == probe_rank,
            'expanded access failed to predict first output')
    print('N3 DETECTED: six initial-neighbour probes determine the next herald')

    # Exact finite return on L=3. This is outside the positive nonwrap condition.
    small = origin_forms(3, 3, 1, 6)
    require(small[6] == {(0, (0, 0, 0)): 2}, 'u_5 != -u_-1')
    require(small[7] == {(1, (0, 0, 0)): 2}, 'u_6 != -u_0')
    small_ranks = [rank(small[:t + 2], 3) - 2 for t in range(1, 7)]
    require(small_ranks == [1, 2, 3, 4, 4, 4], 'finite-return ranks')

    # Independent numeric implementation on every phase-space basis vector.
    # Both algorithms are linear, so basis agreement proves agreement on all states.
    sites = list(product(range(3), repeat=3))
    for slice_, source in product((0, 1), sites):
        past = {site: int(slice_ == 0 and site == source) for site in sites}
        current = {site: int(slice_ == 1 and site == source) for site in sites}
        original = (dict(past), dict(current))
        after = numeric_step(past, current, 3, 3, 1)
        require(numeric_inverse(*after, 3, 3, 1) == original, 'numeric inverse')
        for t in range(1, 7):
            past, current = numeric_step(past, current, 3, 3, 1)
            require(current[(0, 0, 0)] == small[t + 1].get((slice_, source), 0),
                    'numeric/symbolic disagreement')
        require(past == {site: -value % 3 for site, value in original[0].items()},
                'six-step past return')
        require(current == {site: -value % 3 for site, value in original[1].items()},
                'six-step current return')
    print('N4 DETECTED: L=3 ranks [1, 2, 3, 4, 4, 4]; u_5=-u_-1, u_6=-u_0')
    print('P6 PASS: inverse and six-step return checked on all 54 phase-space basis vectors')
    print('PASS: bounded resource lemma checks and all four countercontrols')
    print('NOT CLAIMED: angular flux law, physical emission/reset apparatus, access closure, or OI-QM equivalence')


if __name__ == '__main__':
    run()
