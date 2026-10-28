#!/usr/bin/env python3
"""Bounded controls for exact whole-trace entropy; not a universal proof."""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import lcm, log2
import json
import sys


def advance(p, q, n):
    for _ in range(n):
        q = p[q]
    return q


def order(p):
    seen, period = set(), 1
    for q in range(len(p)):
        if q in seen:
            continue
        s, length = q, 0
        while s not in seen:
            seen.add(s)
            length += 1
            s = p[s]
        period = lcm(period, length)
    return period


def entropy(weights, variables):
    law = defaultdict(Fraction)
    for q, w in enumerate(weights):
        law[tuple(v[q] for v in variables)] += w
    return -sum(float(w) * log2(float(w)) for w in law.values() if w)


def cmi(weights, past, now, other):
    return (entropy(weights, [past, now]) + entropy(weights, [now, other])
            - entropy(weights, [now]) - entropy(weights, [past, now, other]))


def variables(p, visible, t):
    period = order(p)
    past = [tuple(visible(advance(p, q, j)) for j in range(t)) for q in range(len(p))]
    current = [advance(p, q, t) for q in range(len(p))]
    now = [visible(s) for s in current]
    # Periodicity makes each entire sequence exactly this finite cyclic word.
    whole = [tuple(visible(advance(p, s, j + 1)) for j in range(period)) for s in current]
    return past, now, whole, current


counts = {'exact_coordinate': 0, 'exact_countercontrol': 0, 'numerical_entropy': 0}


def require(condition, kind, message):
    """Execute checks under normal and optimized Python alike."""
    counts[kind] += 1
    if not condition:
        raise RuntimeError(message)


if '--failure-control' in sys.argv:
    require(False, 'exact_countercontrol', 'deliberately failed guard')

for p in permutations(range(4)):
    for weights in ([Fraction(1, 4)] * 4,
                    [Fraction(x, 10) for x in (1, 2, 3, 4)],
                    [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]):
        for t in range(2 * order(p) + 1):
            past, now, whole, current = variables(p, lambda s: s // 2, t)
            hidden = [s % 2 for s in current]
            iwhole, ihidden = cmi(weights, past, now, whole), cmi(weights, past, now, hidden)
            require(-1e-12 <= iwhole <= ihidden + 1e-12 <= 1 + 2e-12,
                    'numerical_entropy', 'whole-future information bound')
            for q in range(4):
                for j in range(2 * order(p) + 1):
                    require(whole[q][j % order(p)] == advance(p, q, t + j + 1) // 2,
                            'exact_coordinate', 'actual future coordinate')

# Identity retains hidden degeneracy in the whole trace: not an injective state code.
p = tuple(range(4))
_, _, whole, _ = variables(p, lambda s: s // 2, 0)
require(whole[0] == whole[1] and whole[2] == whole[3] and whole[0] != whole[2],
        'exact_countercontrol', 'identity keeps hidden degeneracy')

saturation = []
for bits in range(2, 6):
    count = 2 ** bits
    p = tuple(((s << 1) % count) + (s >> (bits - 1)) for s in range(count))
    past, now, whole, _ = variables(p, lambda s: s >> (bits - 1), bits - 1)
    info = cmi([Fraction(1, count)] * count, past, now, whole)
    require(abs(info - (bits - 1)) < 1e-12,
            'numerical_entropy', 'cyclic-register capacity saturation')
    saturation.append({'hidden_bits': bits - 1, 'whole_future_cmi_bits': info})
    if bits == 3:
        # A one-step prefix need not encode the entire future.
        require(any(a[0] == b[0] and a != b for a in whole for b in whole),
                'exact_countercontrol', 'one-step prefix can lose whole-future distinctions')

print(json.dumps({'status': 'pass', 'checks': sum(counts.values()),
                  'check_kinds': counts,
                  'permutations': 24, 'initial_laws': 3,
                  'saturation': saturation}, indent=2))
