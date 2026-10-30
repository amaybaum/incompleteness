#!/usr/bin/env python3
"""SUBSTATE-1 exact bounded countercontrol: reversible gauge-covariant link/pointer.

This is a Z/8 subgroup/grid of an explicitly ADDED U(1) link-pointer model,
NOT the native OI wave rule, an actual quantum instrument, or Yang-Mills.
Every verdict is computed only after exhaustive exact controls; no floats.
"""
import itertools
import json
from collections import Counter

N = 8
HALF = N // 2
VERTICES = 4
EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
SETTINGS = (0, N // 4)


def loop(u):
    return sum(u) % N


def mark(k, setting):
    return int((k - setting) % N < HALF)


def transform(state, setting, kick=True):
    u, pointer = state
    new_pointer = pointer ^ mark(loop(u), setting)
    shift = HALF * new_pointer if kick else 0
    return ((u[0] + shift) % N, *u[1:]), new_pointer


def inverse(state, setting, kick=True):
    u, pointer = state
    shift = HALF * pointer if kick else 0
    old_u = ((u[0] - shift) % N, *u[1:])
    return old_u, pointer ^ mark(loop(old_u), setting)


def gauge(state, g):
    u, pointer = state
    return (tuple((u[i] + g[start] - g[end]) % N
                  for i, (start, end) in enumerate(EDGES)), pointer)


def main():
    states = tuple((u, bit) for u in itertools.product(range(N), repeat=4)
                   for bit in (0, 1))
    checks = {}
    for s in SETTINGS:
        checks[f'inverse_{s}'] = all(inverse(transform(x, s), s) == x
                                    and transform(inverse(x, s), s) == x
                                    for x in states)
        checks[f'no_kick_inverse_{s}'] = all(
            inverse(transform(x, s, False), s, False) == x for x in states)
        # Unit vertex generators generate the finite local gauge group.
        for j in range(VERTICES):
            g = tuple(int(k == j) for k in range(VERTICES))
            checks[f'gauge_equivariant_{s}_{j}'] = all(
                transform(gauge(x, g), s) == gauge(transform(x, s), g)
                for x in states)
            checks[f'loop_gauge_invariant_{j}'] = all(
                loop(x[0]) == loop(gauge(x, g)[0]) for x in states)
    checks['no_kick_settings_commute'] = all(
        transform(transform(x, SETTINGS[0], False), SETTINGS[1], False) ==
        transform(transform(x, SETTINGS[1], False), SETTINGS[0], False)
        for x in states)
    witness = next((x for x in states
                    if transform(transform(x, SETTINGS[0]), SETTINGS[1]) !=
                    transform(transform(x, SETTINGS[1]), SETTINGS[0])), None)
    checks['kick_settings_noncommuting'] = witness is not None

    # Haar links with pointer explicitly PREPARED as zero are not the
    # invariant full-state Haar x fair-bit ensemble.
    raw_counts = {}
    for s in SETTINGS:
        initial = ((u, 0) for u in itertools.product(range(N), repeat=4))
        rows = Counter()
        for x in initial:
            y = transform(x, s)
            rows[(loop(x[0]), y[1], loop(y[0]))] += 1
        raw_counts[str(s)] = rows
        checks[f'initial_loop_uniform_{s}'] = all(
            sum(v for (k, b, l), v in rows.items() if k == j) == N**3
            for j in range(N))
        checks[f'pointer_counts_{s}'] = sum(
            v for (_, b, _), v in rows.items() if b == 1) == N**4 // 2
        checks[f'nontrivial_link_back_action_{s}'] = any(
            k != l and v for (k, b, l), v in rows.items())
        checks[f'full_record_deterministic_{s}'] = all(
            b == mark(k, s) and l == (k + HALF*b) % N
            for (k, b, l) in rows)
        checks[f'unchanged_loop_without_kick_{s}'] = all(
            loop(transform(x, s, False)[0]) == loop(x[0])
            for x in states)
        checks[f'unconditional_Haar_no_pointer_prep_{s}'] = all(
            sum(1 for x in states if loop(transform(x, s)[0]) == j)
            == N**4 * 2 // N for j in range(N))

    if not all(checks.values()):
        raise AssertionError([k for k, v in checks.items() if not v])

    print(json.dumps({
        'verdict': 'PASS_EXACT_GRID_TOY_NOT_NATIVE_OI',
        'carrier': 'Z/8 on four oriented U(1) link grid points and one pointer bit',
        'states_exhausted': len(states),
        'controls': checks,
        'source_preparation': 'uniform link grid, pointer initially 0 (not invariant full-state prior)',
        'setting_witness': {
            'initial': witness,
            'A_then_B': transform(transform(witness, SETTINGS[0]), SETTINGS[1]),
            'B_then_A': transform(transform(witness, SETTINGS[1]), SETTINGS[0])},
        'per_setting_full_joint_counts': {
            s: [{'initial_loop': k, 'public_pointer': b,
                 'outgoing_loop': l, 'count': v}
                for (k, b, l), v in sorted(rows.items())]
            for s, rows in raw_counts.items()},
        'native_OI_update': False,
        'continuous_U1_analogue': 'Measurable phase-threshold toggle and central (-1)^pointer link kick',
        'gauge_action_selected': False,
        'quantum_interference_derived': False,
        'operational_QM_derived': False
    }, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
