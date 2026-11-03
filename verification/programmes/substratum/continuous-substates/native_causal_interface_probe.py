#!/usr/bin/env python3
"""Exact source/record cones and a conditional late-entry interface window."""
import argparse
from functools import lru_cache
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def pinned(path, digest):
    raw = path.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == digest, 'source pin '+path.name)
    return raw.decode()


def run(root, contract_path):
    path = root/'native_vread_v15/checks.py'
    pinned(path, '93b4161f32e02874769d57d8a670d1a460d26fa2c953d517db5c6564fb649824')
    contract = pinned(contract_path, '1a0b34ebb0c7115dd5faae11d2ab20c25ecf8a6f091ea292eb184e4311be7633')
    need('torus side 256L+64T+1' in contract, 'inherited torus declaration')
    raw_inventory = pinned(root/'parallel_v3/history_control/SOURCE-GEOMETRY.json',
                           '2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d')
    rows = json.loads(raw_inventory)['sources']
    need(len(rows) == 1479, 'complete compiled-source catalogue')
    inventory = {tuple(row['position']) for row in rows}
    spec = importlib.util.spec_from_file_location('source_geometry', path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    sources = m.local_sources()
    inherited, balls = m.ready_balls()
    need(len(sources) == 17 and len(inherited) == 24 and len(balls) == 25,
         'complete named-source and preparation declarations')
    q = m.Q10
    tau = m.L+3
    side = 256*m.L+64*m.T+1
    footprint = [q]+[m.add(q, d) for d in m.STEPS]

    def affine(value):
        coefficient, offset = divmod(value, m.P)
        if offset > m.P//2:
            coefficient += 1
            offset -= m.P
        need(coefficient*m.P+offset == value, 'exact compact integer representation')
        return {'P_coefficient': coefficient, 'offset': offset}

    events = [('qY', (0, m.S, 68), m.R), ('q7', (0, m.S, 75), m.R+7),
              ('q8', (0, m.S, 76), m.R+8), ('q9', m.Q9, m.L), ('Q_private', q, m.L+1)]
    public_ports = [('port%d' % i, center, deadline) for i, (center, direction, deadline) in enumerate(m.PORTS)]
    controls = {'G', 'J', 'Kplus', 'Kminus', 'N', 'E'}
    earlier = {'Q', 'C'}
    matrix = []
    for name, pos in sources.items():
        role = ('previously_tested_candidate_source_laws' if name in controls else
                'existing_earlier_exception_fixed_law' if name in earlier else
                'original_input_or_resource_fixed_by_contract')
        matrix.append({'source': name, 'role': role,
                       'record_cones': {event: {'within': m.dist(pos, center) <= deadline,
                                               'slack': affine(m.dist(pos, center)-deadline)}
                                        for event, center, deadline in events+public_ports}})

    locks = []
    for name, event, later in (
            ('Q', 'qY', ('C', 'G', 'J', 'Kplus', 'Kminus', 'N', 'E')),
            ('C', 'q7', ('G', 'J', 'Kplus', 'Kminus', 'N', 'E')),
            ('G', 'q8', ('J', 'Kplus', 'Kminus', 'N', 'E'))):
        _, center, deadline = next(v for v in events if v[0] == event)
        need(m.dist(sources[name], center) == deadline and
             sum(x != y for x, y in zip(sources[name], center)) == 1,
             'unique axial first arrival '+name)
        slacks = {other: m.dist(sources[other], center)-deadline for other in later}
        need(all(value > 0 for value in slacks.values()), 'later adjustable sources cannot compensate '+name)
        locks.append({'source': name, 'first_record': event, 'later_source_slacks': slacks,
                      'conclusion': 'fixed_by_whole_record_given_earlier_locks_and_fixed_background'})

    containment = []
    for k in range(10):
        center, deadline = (0, m.S, 68+k), m.R+k
        current = m.dist(center, q)+deadline
        previous = m.dist(center, q)+deadline-1
        need(current <= m.L+1 and previous <= m.L,
             'entire earlier cone lies in original current/previous ready balls')
        containment.append({'chain_index': k, 'current_margin': m.L+1-current,
                            'previous_margin': m.L-previous})

    rays = []
    for direction in m.STEPS:
        pos = m.add(q, direction, m.L+5)
        boundary = m.add(q, direction)
        current_slack = min(m.dist(pos, v)-tau for v in footprint)
        previous_slack = min(m.dist(pos, v)-(tau-1) for v in footprint)
        future_slack = m.dist(pos, boundary)-(tau+1)
        need(current_slack > 0 and previous_slack > 0 and future_slack == 0,
             'late source excluded from both incoming packet slices')
        rays.append({'direction': m.STEP_NAMES[direction],
                     'current_class': list(m.classify(pos, inventory, balls)),
                     'previous_class': list(m.classify_previous(pos, balls)),
                     'minimum_ready_margin': min(m.dist(pos, center)-radius for center, radius in balls),
                     'input_current_slack': current_slack, 'input_previous_slack': previous_slack,
                     'next_boundary_arrival_slack': future_slack})

    p = (0, m.S, m.S+160)
    direction = (0, 0, 1)
    boundary = m.add(q, direction)
    need(p == m.add(q, direction, m.L+5), 'selected late axial coordinate')
    chosen = next(row for row in rays if row['direction'] == '+z')
    route = [{'ticks_from_p': t, 'initial_cell_class': list(m.classify(m.add(p, direction, -t), inventory, balls))}
             for t in range(5)]
    need(m.dist(sources['J'], sources['N']) == 2 and m.dist(p, sources['N']) == 4
         and 2+m.dist(sources['J'], sources['N']) == 4,
         'computed J2 and hypothetical p0 cones can meet at N4')
    need(m.dist(p, sources['J']) == 6 and
         all(m.dist(p, sources['J']) > t+(t-2) for t in (2, 3)),
         'no earlier overlap of J2 and p0 cones')
    need(m.dist(p, boundary) == tau+1 and 4+m.dist(sources['N'], boundary) == tau+1,
         'known-computation meeting can reach next packet boundary')

    # Treat every compiled source and every nonlocal named source as possibly
    # x-bearing. Only the explicitly known-seed local cluster is excluded.
    known_cluster = {'Q', 'C', 'G', 'J', 'Kplus', 'Kminus', 'N'}
    potential_input_sources = inventory | {pos for name, pos in sources.items() if name not in known_cluster}
    need(inventory <= potential_input_sources, 'entire compiled catalogue included in the conservative x-cone audit')
    min_input_distance = min(m.dist(p, pos) for pos in potential_input_sources)
    need(min_input_distance >= 2*tau, 'no x-source/control-cone overlap before the incoming cut')
    old_port_margin = min(m.dist(p, center)-tau for center, direction, deadline in m.PORTS)
    need(old_port_margin > 0, 'late coordinate cannot affect any old public-port history through the cut')
    unknown_contact = m.add(q, direction, 2)
    need(m.dist(p, unknown_contact) == tau and m.dist(sources['O'], unknown_contact) == tau,
         'first possible original-input contact at the cut outside the seven-site packet')

    all_positions = list(inventory)+list(sources.values())+[pos for name, pos, time in events+public_ports]+[p]
    need(all(max(v[j] for v in all_positions)-min(v[j] for v in all_positions) < side//2
             for j in range(3)), 'no torus wrap in any mapped separation')

    # Independent bounded dependency-graph controls for the two-slice stencil.
    # These propagate possible dependencies, not native field values.
    steps = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
    add = lambda a, b: tuple(x+y for x, y in zip(a, b))
    norm = lambda v: sum(abs(x) for x in v)

    @lru_cache(None)
    def dependencies(t, pos):
        if t == 0:
            return frozenset([pos]), frozenset()
        if t == -1:
            return frozenset(), frozenset([pos])
        before = [dependencies(t-2, pos)]+[dependencies(t-1, add(pos, d)) for d in steps]
        return tuple(frozenset().union(*(value[i] for value in before)) for i in (0, 1))

    small_checks = 0
    for time in range(1, 5):
        sites = [(0,0,0)]+list(steps)
        data = [dependencies(t, v) for t in (time, time-1) for v in sites]
        current = set().union(*(value[0] for value in data))
        previous = set().union(*(value[1] for value in data))
        ball = lambda radius: {v for v in itertools.product(range(-radius, radius+1), repeat=3) if norm(v) <= radius}
        need(current == ball(time+1) and previous == ball(time), 'independent two-slice dependency radii')
        for d in steps:
            outside = tuple((time+2)*x for x in d)
            inside = tuple((time+1)*x for x in d)
            future = dependencies(time+1, d)[0]
            need(outside not in current and outside not in previous and outside in future,
                 'late-entry graph positive control')
            need(inside in current, 'one-tick-earlier source fails input-independence control')
            small_checks += 1
    # Whole incoming packet preservation fails if p is moved one tick inward.
    inward = m.add(q, direction, m.L+4)
    need(min(m.dist(inward, v)-tau for v in footprint) == 0,
         'actual-scale inward-placement countercontrol')
    passed = chosen['current_class'] == ['FREE', 'complement'] and chosen['previous_class'] == ['FREE', 'complement']
    return {'schema': 'oi.native-causal-interface.v1', 'status': 'PASS',
            'verdict': 'LATE_CAUSAL_WINDOW_PHYSICAL_CONTROL_SOURCE_OPEN' if passed else 'PREPARATION_GATE_BLOCKED',
            'source_count': len(sources), 'compiled_source_rows': len(rows), 'current_ready_balls': len(balls),
            'dependency_map': matrix, 'triangular_record_locks': locks, 'prepared_cone_containment': containment,
            'six_late_rays': rays, 'selected_late_ray': '+z', 'initial_route_classes': route,
            'first_known_computation_overlap': {'source': 'J', 'source_tick': 2, 'meeting': 'N', 'tick': 4},
            'input_independence': {'current_margin': chosen['input_current_slack'],
                                   'previous_margin': chosen['input_previous_slack'],
                                   'conservative_x_cone_distance_margin': min_input_distance-2*tau,
                                   'old_public_history_horizon': 'L+3',
                                   'earliest_old_port_distance_beyond_cut': old_port_margin,
                                   'first_possible_x_contact_tick': 'L+3', 'contact_site': 'q10+2z'},
            'next_boundary_tick': 'L+4', 'earliest_center_tick': 'L+5',
            'bounded_dependency_graph_checks': small_checks,
            'physical_setting_preparation': 'NOT_ESTABLISHED', 'public_setting_access': 'NOT_ESTABLISHED',
            'original_carrier_compatibility_of_J2_candidate': 'NOT_ESTABLISHED',
            'native_field_simulations': 0, 'measurement_output_tests': 0,
            'outgoing_kernel_and_reuse': 'NOT_ESTABLISHED', 'operational_quotient': 'NOT_ADOPTED'}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parents[2] /
                    'oi-qm/reconstruction/native-y-continuation-20261024')
    ap.add_argument('--contract', type=Path)
    args = ap.parse_args()
    try:
        result = run(args.source_root, args.contract or args.source_root/'shared_v12/INTERFACE-CONTRACT.md')
    except (RuntimeError, ValueError, KeyError, OSError, StopIteration, TypeError) as exc:
        print(json.dumps({'status': 'VOID', 'reason': str(exc)}, sort_keys=True))
        raise SystemExit(2)
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))
