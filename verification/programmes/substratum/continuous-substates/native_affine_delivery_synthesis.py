#!/usr/bin/env python3
"""Exact known-seed K/E source constraints, with an explicit empty-domain proof."""
import argparse
import ast
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


KNOWN = tuple(itertools.product(range(2), repeat=5))
UNKNOWN = (0, 1)
PAIRS = tuple(itertools.product(range(8), repeat=2))


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def native_response(root, helper, functions, worlds, old_table):
    # Credited retained engine: only source payloads and lane packing change.
    # Unlike the predecessor, E is an explicit original-time source coordinate.
    m = load_module(root / 'native_route_v13/checks.py', 'affine_delivery_route')
    data = []
    sources = []
    for bits, p, r, e, reference in worlds:
        payload, n = helper.payloads(functions, bits, p, r, reference)
        data.append(bits + (e, n))
        sources.append(payload)
    count = len(worlds)
    need(0 < count <= 512, 'bounded nonempty native batch')
    m.ROWS = tuple(data)
    m.UR = tuple(range(count))
    m.FULL = m.UF = (1 << count) - 1
    m.XM, m.UM, m.MY, m.MR = tuple(
        sum(row[j] << i for i, row in enumerate(data)) for j in range(4))
    keys = set(m.SOURCES)
    need(all(set(v) == keys for v in sources), 'same upper source sites')
    m.SOURCES = {key: tuple(sum(((row[key] >> (2-f)) & 1) << i
                               for i, row in enumerate(sources))
                           for f in range(3)) for key in keys}
    m.expand_upper = lambda q: q
    m.CONTROLS = [((0, -m.S, -68), m.XM),
                  ((0, m.S, -68), m.MY ^ m.MR),
                  ((m.T, m.P, -68), m.MY), ((-m.T, m.P, -68), m.MR)]
    need(m.BUDGET == 20 and m.P % (12*840**20) == 0 and
         m.P % (384*840**3) == 0, 'inherited native period coverage')
    direct = 0
    for ell, x, y in ((18, 0, 0), (18, -1, 1), (18, 1, 1), (20, 0, 0)):
        for n in (0, 1):
            need(m.upper_strip()[ell, x, y][n] == m.direct_upper(n+ell, x, y, n),
                 'independent direct-upper recursion control')
            direct += count
    output, records = m.native_compute()
    out = [m.code(m.lane(output, i)) for i in range(count)]
    old = [m.code(m.lane(records[9][0, 0, 9], i)) for i in range(count)]
    for i, ((bits, p, r, e, reference), payload) in enumerate(zip(worlds, sources)):
        x, u, my, mr, aa, b = bits
        c = payload[0, 0, -18] ^ helper.enc(u ^ 1, 1, u ^ 1)
        address = (x, u, my, mr, 1, 0, c, payload[1, 0, -17], payload[-1, 0, -17])
        need(old[i] == int(old_table[helper.index(address, (2,)*6+(8,)*3)], 16),
             'whole old-q9 independent table addressing')
    return out, old, direct


def solve_domains(domains):
    # Exact finite Boolean CSP elimination: each context is a disjunction of
    # admissible source values. An empty disjunction is FALSE, even before
    # imposing the cross-context affine-coefficient equations.
    empty = [i for i, values in enumerate(domains) if not values]
    return {'status': 'UNSAT' if empty else 'COEFFICIENT_SOLVING_REQUIRED',
            'empty_context_indices': empty}


def run(root, predecessor):
    need(len(KNOWN) == 32 and len(set(KNOWN)) == 32 and UNKNOWN == (0, 1)
         and len(PAIRS) == 64, 'complete known/unknown/source domains')
    need(sum(k[3:] == (0, 1) for k in KNOWN) == 8,
         'all terminal known contexts retained')
    need(hashlib.sha256(predecessor.read_bytes()).hexdigest() ==
         '680496938b5df4758754615030770ca9f2daadde7565a4fcbc44559da04b4e1d',
         'accepted predecessor source pin')
    helper = load_module(predecessor, 'accepted_asymmetric_delivery')
    source = helper.pinned(root / 'native_route_v13/checks.py',
                          '8c1bbc37f47b6ff7ad7ee67d719f058067e2e15e9a6a967adfb78ef57d1ed856')
    qt = json.loads((root / 'native_route_v13/result.json').read_text())['q10_table_hex']
    pt = json.loads((root / 'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    need(hashlib.sha256(qt.encode()).hexdigest() ==
         'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc', 'Q table pin')
    need(hashlib.sha256(pt.encode()).hexdigest() ==
         'dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf', 'q9 table pin')
    tree = ast.parse(source)
    node = next(n.value for n in tree.body if isinstance(n, ast.Assign) and
                any(isinstance(t, ast.Name) and t.id == 'SOURCES' for t in n.targets))
    functions = {ast.literal_eval(k): eval(compile(ast.Expression(v.args[0]), '<pinned sources>', 'eval'),
                                         {'TR': tuple(itertools.product(range(2), repeat=3)), '__builtins__': {}})
                 for k, v in zip(node.keys, node.values)}

    def target_q(bits, e=None):
        my = bits[2]
        return int(qt[helper.index(bits + (7-2*my if e is None else e, 4*my+2+(1 ^ my)),
                                   (2,)*6+(8, 8))], 16)

    def old_q(bits, p=None, r=None):
        if p is None:
            return int(pt[helper.index(bits + (4, 5, 7), (2,)*6+(8,)*3)], 16)
        x, u, my, mr, aa, b = bits
        payload, _ = helper.payloads(functions, bits, p, r)
        c = payload[0, 0, -18] ^ helper.enc(u ^ 1, 1, u ^ 1)
        return int(pt[helper.index((x, u, my, mr, 1, 0, c,
                                   payload[1, 0, -17], payload[-1, 0, -17]), (2,)*6+(8,)*3)], 16)

    # Independent baseline control exercises every E value with original N0/K.
    baseline = [(bits, 0, 0, e, True) for bits in helper.BITS for e in range(8)]
    base, old, direct = native_response(root, helper, functions, baseline, pt)
    need(base == [target_q(bits, e) for bits, p, r, e, ref in baseline],
         'all 512 retained original-K/N0/E responses reproduced')
    need(old == [old_q(bits) for bits, p, r, e, ref in baseline], 'full baseline q9')

    rows = []
    worlds = []
    local_checks = 0
    for k in KNOWN:
        u, my, mr, aa, b = k
        target = helper.enc(1 ^ aa ^ b ^ mr, 1 ^ (aa & mr),
                            mr ^ u ^ (u & aa) ^ (u & aa & mr))
        local = []
        old_pairs = []
        formula_preserving = 0
        for p, r in PAIRS:
            got = helper.local_output(functions, u, aa, b, mr, p, r)
            local_checks += 1
            # Check actual pointwise full fields; the uniform constant-offset
            # classification is deliberately not imposed on this larger family.
            pa, pb, pd = helper.decode(p)
            ra, rb, rd = helper.decode(r)
            delta = aa ^ b
            change = ((1 ^ u) & (pd ^ rd)) ^ (delta & rd) ^ ((1 ^ delta) & (pb ^ rb)) ^ (pb & rd) ^ (rb & pd)
            need((((got ^ target) >> 1) & 1) == change, 'pointwise J.B difference control')
            need((got == target) == (change == 0), 'pointwise complete-J classification')
            formula_preserving += change == 0
            if got != target:
                continue
            local.append((p, r))
            if all(old_q((x,) + k, p, r) == old_q((x,) + k) for x in UNKNOWN):
                old_pairs.append((p, r))
        need(len(local) == formula_preserving, 'no pointwise local choices omitted')
        rows.append({'known': k, 'local_pairs': len(local), 'old_q9_pairs': len(old_pairs),
                     'K_only_values': [], 'K_E_values': [], 'witness_E_masks': []})
        for p, r in old_pairs:
            for e in range(8):
                for x in UNKNOWN:
                    worlds.append(((x,) + k, p, r, e, False))
    outputs = []
    for start in range(0, len(worlds), 512):
        out, _, d = native_response(root, helper, functions, worlds[start:start+512], pt)
        outputs += out
        direct += d
    need(len(outputs) == len(worlds) and len(worlds) > 0, 'complete nonvacuous native source worlds')
    permutations = 0
    relaxed_domains = [[] for k in KNOWN]
    for start in range(0, len(worlds), 16):
        block = worlds[start:start+16]
        need(len(block) == 16 and all(w[0][1:] == block[0][0][1:] and w[1:3] == block[0][1:3]
                                     for w in block), 'same known controls across unknown branches')
        need([w[0][0] for w in block] == list(UNKNOWN)*8 and
             [w[3] for w in block] == [e for e in range(8) for _ in UNKNOWN], 'complete E/unknown pairing')
        k = block[0][0][1:]
        p, r = block[0][1:3]
        row = rows[KNOWN.index(k)]
        masks = [0, 0]
        for x in UNKNOWN:
            values = outputs[start+x:start+16:2]
            need(len(set(values)) == 8, 'native first-arrival E permutation positive control')
            permutations += 1
            masks[x] = sum(1 << e for e, value in enumerate(values) if value == target_q((x,) + k))
        common = masks[0] & masks[1]
        if masks[0] and masks[1]:
            relaxed_domains[KNOWN.index(k)].append((p, r, masks[0], masks[1]))
        for e in range(8):
            if (common >> e) & 1:
                need(all(outputs[start+2*e+x] == target_q((x,) + k) for x in UNKNOWN),
                     'one identical E must match both actual unknown outputs')
                row['K_E_values'].append((p, r, e))
                if e == 7-2*k[1]: row['K_only_values'].append((p, r))
        if k == (0,)*5:
            row['witness_E_masks'].append({'p': p, 'r': r, 'E_mask_x0': masks[0],
                                           'E_mask_x1': masks[1], 'intersection': common})
    k_only = solve_domains([r['K_only_values'] for r in rows])
    coordinated = solve_domains([r['K_E_values'] for r in rows])
    # Nonempty domain is never SAT for the affine problem or full carrier:
    # coefficient coupling and complete packet/correlations remain unchecked.
    relaxed = solve_domains(relaxed_domains)
    need(relaxed['status'] == 'COEFFICIENT_SOLVING_REQUIRED',
         'relaxing unknown-dependent E removes the pointwise obstruction')
    continuing = [i for i, k in enumerate(KNOWN) if k[3:] != (0, 1)]
    independent_x_choices = all(v['E_mask_x0'] and v['E_mask_x1'] for v in rows[0]['witness_E_masks'])
    need(rows[0]['witness_E_masks'] and independent_x_choices,
         'each unknown branch individually has an E compensation')
    return {'schema': 'oi.native-affine-delivery-synthesis.v1', 'status': 'PASS',
            'verdict': 'UNSAT_K_AND_EXISTING_E_EXTENSION' if k_only['status'] == coordinated['status'] == 'UNSAT'
                       else 'FURTHER_SOLVING_REQUIRED',
            'known_order': ['u', 'mY', 'mR', 'a', 'b'], 'unknown': list(UNKNOWN),
            'affine_coefficient_bits_K': 36, 'affine_coefficient_bits_K_E': 54,
            'local_context_pair_checks': local_checks, 'baseline_E_worlds': len(baseline),
            'candidate_native_worlds': len(worlds), 'upper_direct_scalar_lanes': direct,
            'E_permutation_controls': permutations, 'K_only': k_only, 'K_E': coordinated,
            'unauthorized_x_dependent_E_pointwise': relaxed,
            'witness_target_Q_x0_x1': [target_q((x,) + (0,)*5) for x in UNKNOWN],
            'witness_old_q9_x0_x1': [old_q((x,) + (0,)*5) for x in UNKNOWN],
            'continuing_empty_domains_K': sum(not rows[i]['K_only_values'] for i in continuing),
            'continuing_empty_domains_K_E': sum(not rows[i]['K_E_values'] for i in continuing),
            'rows': rows, 'first_empty_domain_known': next((r['known'] for r in rows if not r['K_E_values']), None),
            'full_42bit_gate': 'NOT_REACHED', 'measurement_output_tests': 0,
            'physical_selection': 'NOT_ESTABLISHED', 'terminal_rows_are_private_diagnostics': True}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parents[2] /
                    'oi-qm/reconstruction/native-y-continuation-20261024')
    ap.add_argument('--predecessor', type=Path, default=Path(__file__).with_name('native_asymmetric_delivery_probe.py'))
    args = ap.parse_args()
    try:
        result = run(args.source_root, args.predecessor)
    except (RuntimeError, ValueError, KeyError, OSError, StopIteration, TypeError) as exc:
        print(json.dumps({'status': 'VOID', 'reason': str(exc)}, sort_keys=True))
        raise SystemExit(2)
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))
