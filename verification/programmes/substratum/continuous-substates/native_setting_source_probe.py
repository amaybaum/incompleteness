#!/usr/bin/env python3
"""Source/permission feasibility for the late coordinate; no native field replay."""
import argparse
import ast
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def module(path, name, digest):
    need(hashlib.sha256(path.read_bytes()).hexdigest() == digest, 'source pin '+path.name)
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def run(root, contract, geometry_probe):
    g = module(geometry_probe, 'accepted_causal_geometry',
               'b608bee76763d6a874b219ec605d9781d24ce2602e586b7428a3cc743d6dbac9')
    geometry = g.run(root, contract)
    need(geometry['status'] == 'PASS' and geometry['native_field_simulations'] == 0,
         'accepted geometry baseline')
    v = module(root/'native_vread_v15/checks.py', 'primary_preparation',
               '93b4161f32e02874769d57d8a670d1a460d26fa2c953d517db5c6564fb649824')
    engine_raw = (root/'native_route_v13/checks.py').read_bytes()
    need(hashlib.sha256(engine_raw).hexdigest() ==
         '8c1bbc37f47b6ff7ad7ee67d719f058067e2e15e9a6a967adfb78ef57d1ed856', 'native source-law pin')
    raw_inventory = (root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_bytes()
    need(hashlib.sha256(raw_inventory).hexdigest() ==
         '2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d', 'source inventory pin')
    inventory = {tuple(row['position']) for row in json.loads(raw_inventory)['sources']}
    named = v.local_sources()
    _, balls = v.ready_balls()
    p = (0, v.S, v.S+160)
    interaction = v.L+4
    first_port = min(v.dist(p, pos) for pos, direction, deadline in v.PORTS)
    need(first_port > interaction, 'old public ports cannot reveal p by interaction')
    need(v.dist(p, v.Q9) > v.L+2,
         'neither old q9 read nor supplied whole-V read contains p')

    # Exact policy controls. H can be correlated with unknown X, but is
    # independent of the private uniform triple B; Z is a declared independent
    # controller seed in this mathematical relaxation, not a native resource.
    h_weights = ((1, 2, 3, 4), (4, 3, 2, 1))
    z_weights = (1, 2)
    denominator = sum(sum(weights) for weights in h_weights)*sum(z_weights)*8
    bit_policies = 0
    for truth in range(1 << 8):
        matched = 0
        for x, h, z, b in itertools.product(range(2), range(4), range(2), range(8)):
            setting = (truth >> (2*h+z)) & 1
            matched += h_weights[x][h]*z_weights[z]*int(setting == ((b >> 2) & 1))
        need(Fraction(matched, denominator) == Fraction(1, 2), 'all public bit-policy nonsteering controls')
        bit_policies += 1
    triple_policies = 0
    for aa, bb, cc in itertools.product(range(8), repeat=3):
        matched = 0
        for x, h, z, b in itertools.product(range(2), range(4), range(2), range(8)):
            setting = (aa*h+bb*z+cc) % 8
            matched += h_weights[x][h]*z_weights[z]*int(setting == b)
        need(Fraction(matched, denominator) == Fraction(1, 8), 'whole-triple nonsteering controls')
        triple_policies += 1
    # An excluded correlated prior defeats the independence hypothesis.
    # This conditioning is a mathematical countercontrol, not an allowed herald.
    correlated_total = correlated_match = 0
    for x, h, z, b in itertools.product(range(2), range(4), range(2), range(8)):
        if ((b >> 2) & 1) == (h & 1):
            weight = h_weights[x][h]*z_weights[z]
            correlated_total += weight
            correlated_match += weight*int((h & 1) == ((b >> 2) & 1))
    need(Fraction(correlated_match, correlated_total) == 1 and correlated_total < denominator,
         'correlated-prior countercontrol violates the product-law hypothesis')

    tree = ast.parse(engine_raw.decode())
    node = next(n.value for n in tree.body if isinstance(n, ast.Assign) and
                any(isinstance(t, ast.Name) and t.id == 'SOURCES' for t in n.targets))
    functions = {ast.literal_eval(k): eval(compile(ast.Expression(val.args[0]), '<pinned source laws>', 'eval'),
                                         {'TR': tuple(itertools.product(range(2), repeat=3)), '__builtins__': {}})
                 for k, val in zip(node.keys, node.values)}
    need(v.FEWEST_LAW == (1, 5, 1, 4, 1, 5), 'retained reference affine law')
    need(all(not (mask & 8) for mask in v.FEWEST_LAW), 'reference E/N fields contain no mR coefficient')

    def source_profile(u, my, mr, aa, b, inserted_mr=False):
        n = (u ^ aa ^ mr) if inserted_mr else (4*my+2+(1 ^ my))
        return {key: fn(u, aa, b, n) for key, fn in functions.items()}

    insensitive_pairs = 0
    differing_targets = 0
    supplied_mr_pairs = 0
    for u, my, aa, b in itertools.product(range(2), repeat=4):
        values0 = source_profile(u, my, 0, aa, b)
        values1 = source_profile(u, my, 1, aa, b)
        need(values0 == values1, 'original local source profile independent of mR')
        insensitive_pairs += 1
        differing_targets += (1 ^ (aa & 0)) != (1 ^ (aa & 1))
        supplied_mr_pairs += source_profile(u, my, 0, aa, b, True) != source_profile(u, my, 1, aa, b, True)
    need(differing_targets > 0 and supplied_mr_pairs > 0, 'MR-sensitive target and source-change countercontrol')

    known_local = {'J', 'G', 'Kplus', 'Kminus', 'N'}
    cones = []
    for label, center, current_radius in (('J2', named['J'], 2), ('N4', named['N'], 4)):
        current = [v.add(center, offset) for offset in v.small_ball(current_radius)]
        previous = [v.add(center, offset) for offset in v.small_ball(current_radius-1)]
        current_counts = Counter()
        previous_counts = Counter()
        seen_sources = set()
        for cell in current:
            state, reason = v.classify(cell, inventory, balls)
            current_counts[state] += 1
            need(cell not in inventory and state != 'BANK', 'no undeclared local source/bank dependence')
            if reason.startswith('source '):
                name = reason[7:]
                need(name in known_local, 'only original known-seed MR-free source in early cone')
                seen_sources.add(name)
        for cell in previous:
            state, reason = v.classify_previous(cell, balls)
            previous_counts[state] += 1
        need(all(v.dist(named[name], center) > current_radius for name in ('selector_y', 'selector_minus')),
             'declared MR selectors cannot reach the early computation')
        cones.append({'event': label, 'current_radius': current_radius, 'previous_radius': current_radius-1,
                      'current_cells': len(current), 'previous_cells': len(previous),
                      'current_classes': dict(current_counts), 'previous_classes': dict(previous_counts),
                      'named_sources': sorted(seen_sources),
                      'MR_dependence_under_original_product_preparation': False})

    return {'schema': 'oi.native-setting-source-feasibility.v1', 'status': 'PASS',
            'verdict': 'BLOCKED_FOR_DECLARED_PASSIVE_SOURCE_INTERFACE',
            'scope': 'late p0 coordinate with unchanged reference preparation and declared public-read/stop interface',
            'setting_preparation': {'physical_p_actuator': 'NOT_SUPPLIED_BY_THE_AUDITED_CONTRACT',
                                    'read_only_label_selection': 'CANNOT_STEER_PRIVATE_UNIFORM_P',
                                    'uniform_bit_match': '1/2', 'uniform_triple_match': '1/8',
                                    'all_binary_public_policies_tested': bit_policies,
                                    'whole_triple_policy_controls': triple_policies,
                                    'excluded_correlated_prior_bit_match': '1'},
            'compatible_early_computation': {'original_MR_insensitive_source_pairs': insensitive_pairs,
                                             'pairs_with_different_required_product_bit': differing_targets,
                                             'inserted_MR_source_countercontrol_pairs': supplied_mr_pairs,
                                             'local_cones': cones,
                                             'J2_and_N4_required_MR_sensitive_bit': 'NOT_AVAILABLE_UNDER_ORIGINAL_LOCAL_PREPARATION',
                                             'later_computation': 'OPEN'},
            'public_access': {'interaction_tick': 'L+4', 'earliest_possible_old_port_tick': 'L+83',
                              'old_port_delay_after_interaction': first_port-interaction,
                              'new_setting_or_outcome_read': 'NOT_ADOPTED',
                              'complete_outgoing_kernel_flags_timing_and_reuse': 'NOT_CONSTRUCTED'},
            'native_field_simulations': 0, 'private_writes_performed': 0,
            'preparation_or_access_change': False, 'operational_quotient_applied': False}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parents[2] /
                    'oi-qm/reconstruction/native-y-continuation-20261024')
    ap.add_argument('--contract', type=Path)
    ap.add_argument('--geometry-probe', type=Path, default=Path(__file__).with_name('native_causal_interface_probe.py'))
    args = ap.parse_args()
    try:
        result = run(args.source_root, args.contract or args.source_root/'shared_v12/INTERFACE-CONTRACT.md', args.geometry_probe)
    except (RuntimeError, ValueError, KeyError, OSError, StopIteration, TypeError) as exc:
        print(json.dumps({'status': 'VOID', 'reason': str(exc)}, sort_keys=True))
        raise SystemExit(2)
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))
