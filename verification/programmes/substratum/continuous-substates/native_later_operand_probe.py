#!/usr/bin/env python3
"""Later original-preparation operand algebra and conditional controller timing.

Reads the retained native response table; performs no native field simulation.
"""
import argparse
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
    need(hashlib.sha256(raw).hexdigest() == digest, 'source pin '+str(path))
    return raw


def parity(value):
    return value.bit_count() & 1


def target(bits):
    x, u, my, mr, a, b = bits
    return 1 ^ (a & mr)


def feature(bits):
    return 1 | sum(v << (j+1) for j, v in enumerate(bits[1:]))


def affine_solutions(equations):
    """Six-variable Gaussian elimination, then enumerate its free variables."""
    pivots = {}
    for mask, rhs in equations:
        for bit in range(5, -1, -1):
            if not mask & (1 << bit):
                continue
            if bit in pivots:
                mask ^= pivots[bit][0]
                rhs ^= pivots[bit][1]
            else:
                pivots[bit] = (mask, rhs)
                break
        else:
            if rhs:
                return []
    free = [bit for bit in range(6) if bit not in pivots]
    answers = []
    for values in itertools.product((0, 1), repeat=len(free)):
        answer = sum(v << bit for bit, v in zip(free, values))
        for bit in sorted(pivots):
            mask, rhs = pivots[bit]
            answer |= (rhs ^ parity(mask & answer)) << bit
        need(all(parity(mask & answer) == rhs for mask, rhs in equations),
             'Gaussian solution direct substitution')
        answers.append(answer)
    return sorted(answers)


def solve(rows):
    gaussian = []
    for raw_mask in range(1, 8):
        equations = [(feature(bits), target(bits) ^ parity(raw & raw_mask))
                     for bits, raw in rows]
        gaussian.extend((raw_mask, c) for c in affine_solutions(equations))
    brute = [(q, c) for q in range(1, 8) for c in range(64)
             if all(parity(raw & q) ^ parity(feature(bits) & c) == target(bits)
                    for bits, raw in rows)]
    need(gaussian == brute, 'Gaussian and direct 448-law enumeration agree')
    return gaussian


def anf(values):
    coefficients = list(values)
    for bit in range(6):
        for index in range(64):
            if index & (1 << bit):
                coefficients[index] ^= coefficients[index ^ (1 << bit)]
    terms = [i for i, coefficient in enumerate(coefficients) if coefficient]
    need(all(sum(1 for term in terms if term & index == term) % 2 == value
             for index, value in enumerate(values)), 'ANF independent evaluation')
    names = ('b', 'a', 'mR', 'mY', 'u', 'x')
    return ['*'.join(names[j] for j in range(6) if term & (1 << j)) or '1'
            for term in terms]


def run(root, contract):
    raw = pinned(root/'native_route_v13/result.json',
                 '762b9799db7448c4eecf2c994c8c68ff94e1be83a7f6884b4a36385505df5a02')
    retained = json.loads(raw)
    table = retained['q10_table_hex']
    need(len(table) == 4096 and hashlib.sha256(table.encode()).hexdigest() ==
         'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc',
         'complete retained response table')
    need(retained['table_order'].startswith('x,u,mY,mR,a,b,Ecode,Ncode'), 'table order')
    preparation_path = root/'native_vread_v15/checks.py'
    pinned(preparation_path, '93b4161f32e02874769d57d8a670d1a460d26fa2c953d517db5c6564fb649824')
    pinned(contract, '1a0b34ebb0c7115dd5faae11d2ab20c25ecf8a6f091ea292eb184e4311be7633')
    spec = importlib.util.spec_from_file_location('retained_preparation', preparation_path)
    v = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v)
    law = (1, 5, 1, 4, 1, 5)
    need(law == v.FEWEST_LAW, 'original reference law')
    rows = []
    for bits in itertools.product((0, 1), repeat=6):
        x, u, my, mr, a, b = bits
        e, n = v.law_codes(law, bits[1:])
        need(v.fields(e) == (1, 1 ^ my, 1) and
             v.fields(n) == (my, 1, 1 ^ my), 'reference source payloads unchanged')
        index = 0
        for value, size in zip(bits+(e, n), (2,)*6+(8, 8)):
            index = index*size+value
        need(index == v.q10_index(*bits, e, n), 'independent row address')
        rows.append((bits, int(table[index], 16)))
    continuing = [(bits, q) for bits, q in rows if bits[4:6] != (0, 1)]
    terminal = [(bits, q) for bits, q in rows if bits[4:6] == (0, 1)]
    need(len(continuing) == 48 and len(terminal) == 16, 'retain all source contexts')
    normal_forms = {label: anf([(q >> bit) & 1 for bits, q in rows])
                    for label, bit in (('A', 2), ('B', 1), ('D', 0))}

    # A separately written compact identity on the continuing domain.
    for bits, raw in continuing:
        x, u, my, mr, a, b = bits
        c = a ^ b
        expected = (x ^ u ^ a,
                    1 ^ a ^ b ^ (c & mr) ^ (b & my & (1 ^ u)) ^ (u & x),
                    1 ^ b ^ (c & mr) ^ ((1 ^ c) & (my ^ u)) ^ (c & x) ^
                    (c & mr & x) ^ (b & my & x & (1 ^ u)))
        need(v.fields(raw) == expected, 'compact original-field identities')
    lookup = dict(continuing)
    pairs = []
    for x, u, my, a, b in itertools.product((0, 1), repeat=5):
        if (a, b) == (0, 1):
            continue
        left, right = (x, u, my, 0, a, b), (x, u, my, 1, a, b)
        q0, q1 = lookup[left], lookup[right]
        need(((q0 >> 1) ^ (q1 >> 1)) & 1 == (a ^ b), 'native B mR derivative')
        need(target(left) == 1 and target(right) == (1 ^ a), 'target branch specification')
        pairs.append({'x': x, 'u': u, 'mY': my, 'a': a, 'b': b,
                      'Q_codes': [q0, q1], 'target_bits': [target(left), target(right)]})
    collisions = [p for p in pairs if p['Q_codes'][0] == p['Q_codes'][1]
                  and p['target_bits'][0] != p['target_bits'][1]]
    solutions = solve(continuing)
    full_solutions = solve(rows)
    # Solver controls use changed tables, explicitly outside the native claim.
    planted = [(bits, (q & 5) | ((target(bits) ^ bits[1] ^ bits[2]) << 1))
               for bits, q in continuing]
    planted_solutions = solve(planted)
    need((2, 6) in planted_solutions, 'planted B plus affine u/mY mask is detected')
    erased = [(bits, lookup[bits[:3]+(0,)+bits[4:]]) for bits, q in continuing]
    erased_solutions = solve(erased)
    need(not erased_solutions, 'mR-erased nonlinear-target countercontrol')
    # Nonlinear ANF control independent of the native table.
    fixture = [x ^ (u & mr) ^ (my & a & b)
               for x, u, my, mr, a, b in itertools.product((0, 1), repeat=6)]
    need(set(anf(fixture)) == {'x', 'mR*u', 'b*a*mY'}, 'nonlinear ANF fixture')

    tau = v.L+3
    register = v.PORTS[5][0]
    setting_tick = v.S+4
    footprint = [v.Q10]+[v.add(v.Q10, d) for d in v.STEPS]
    minimum_distance = min(v.dist(register, site) for site in footprint)
    first_contact = setting_tick+minimum_distance
    need(register == (0, v.S, 0) and minimum_distance == 77, 'old public port 5 geometry')
    need(first_contact > tau and first_contact == v.L+4, 'post-preparation first packet contact')
    need(setting_tick+v.dist(register, v.Q10) == v.L+5, 'later center contact')
    need(setting_tick-1+minimum_distance == tau, 'one-tick-earlier input-contact countercontrol')
    late_decision_contact = tau+minimum_distance
    need(late_decision_contact == v.L+80, 'decision at input cut cannot use L+4 window')
    # Conditional first-front maps retain arbitrary old-local/background triples.
    # This is a mathematical control assuming a supplied perturbation at S+4,
    # not a compiled actuator or a native field replay.
    maps = list(range(8))
    for step in range(minimum_distance):
        background, old_local = (3*step+1) % 8, (5*step+2) % 8
        maps = [old_local ^ v.h(q ^ background) for q in maps]
        need(len(set(maps)) == 8, 'conditional axial map remains bijective')
    uniform_counts = [maps.count(q) for q in range(8)]
    shifted = [maps[q ^ 4] for q in range(8)]
    need(all(maps[q] != shifted[q] for q in range(8)) and
         sorted(maps) == sorted(shifted), 'distinct conditional actions can have identical uniform marginals')
    return {'schema': 'oi.native-later-operand-controller.v1', 'status': 'PASS',
            'verdict': 'LATER_INTERNAL_MR_DEPENDENCE_PUBLIC_ACTUATOR_NOT_COMPILED',
            'parent': '488ee2b90fdd847582d8c7817ea9846fae663310',
            'original_contexts': {'continuing': len(continuing), 'terminal_diagnostics_only': len(terminal)},
            'original_q10_all_context_ANF_terms_XOR': normal_forms,
            'continuing_mR_pairs': len(pairs),
            'native_Q_mR_sensitive_pairs': sum(p['Q_codes'][0] != p['Q_codes'][1] for p in pairs),
            'target_sensitive_equal_Q_pairs': collisions,
            'target_linear_Q_parity_plus_affine_known_seed_solutions': solutions,
            'all_context_diagnostic_solutions': full_solutions,
            'solver_controls': {'planted_solutions': planted_solutions,
                                'erased_mR_solutions': erased_solutions,
                                'ANF_fixture': 'PASS'},
            'conditional_public_register': {'site': 'old port 5=(0,S,0)',
                'hypothetical_current_slice_setting_tick': 'S+4',
                'first_packet_contact': 'L+4', 'first_center_contact': 'L+5',
                'incoming_current_slack': first_contact-tau,
                'incoming_previous_slack': first_contact-(tau-1),
                'earliest_contact_if_decided_at_input_cut': 'L+80',
                'supplied_first_front_permutation': maps,
                'uniform_output_counts': uniform_counts,
                'actuator_under_original_passive_contract': 'NOT_COMPILED',
                'public_setting_record_joint_law': 'NOT_ESTABLISHED',
                'full_outgoing_joint_kernel_and_reuse': 'NOT_ESTABLISHED'},
            'native_field_simulations': 0, 'writes_performed': 0,
            'new_access_or_preparation_adopted': False, 'operational_quotient_applied': False,
            'terminal_new_reads_or_offers': 0}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parents[2] /
                        'oi-qm/reconstruction/native-y-continuation-20261024')
    parser.add_argument('--contract', type=Path)
    args = parser.parse_args()
    try:
        result = run(args.source_root, args.contract or args.source_root/'shared_v12/INTERFACE-CONTRACT.md')
    except (RuntimeError, ValueError, KeyError, OSError, TypeError) as exc:
        print(json.dumps({'status': 'VOID', 'reason': str(exc)}, sort_keys=True))
        raise SystemExit(2)
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))
