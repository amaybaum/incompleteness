#!/usr/bin/env python3
"""One additional existing J source: complete local computation and input gates."""
import argparse
import ast
from functools import lru_cache
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
    out = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


KNOWN = tuple(itertools.product(range(2), repeat=5))
UNKNOWN = (0, 1)
SOURCE_VALUES = tuple(itertools.product(range(8), repeat=3))


def run(root, synthesis_path, asymmetric_path):
    need(len(KNOWN) == 32 and len(set(KNOWN)) == 32 and UNKNOWN == (0, 1)
         and len(SOURCE_VALUES) == 512, 'complete known/unknown/J-K domains')
    need(sum(k[3:] == (0, 1) for k in KNOWN) == 8, 'terminal context coverage')
    a = module(asymmetric_path, 'accepted_asymmetric',
               '680496938b5df4758754615030770ca9f2daadde7565a4fcbc44559da04b4e1d')
    s = module(synthesis_path, 'accepted_synthesis',
               '15971d7abcacd075f86e17f79b812d5365bed6c4bb38980a8c9987f1c0efaea3')
    engine = a.pinned(root/'native_route_v13/checks.py',
                      '8c1bbc37f47b6ff7ad7ee67d719f058067e2e15e9a6a967adfb78ef57d1ed856')
    pt = json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    qt = json.loads((root/'native_route_v13/result.json').read_text())['q10_table_hex']
    need(hashlib.sha256(pt.encode()).hexdigest() ==
         'dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf', 'old-q9 table pin')
    need(hashlib.sha256(qt.encode()).hexdigest() ==
         'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc', 'Q table pin')
    node = next(n.value for n in ast.parse(engine).body if isinstance(n, ast.Assign) and
                any(isinstance(t, ast.Name) and t.id == 'SOURCES' for t in n.targets))
    functions = {ast.literal_eval(k): eval(compile(ast.Expression(v.args[0]), '<pinned sources>', 'eval'),
                                         {'TR': tuple(itertools.product(range(2), repeat=3)), '__builtins__': {}})
                 for k, v in zip(node.keys, node.values)}

    class Sources:
        enc = staticmethod(a.enc)
        index = staticmethod(a.index)

        @staticmethod
        def payloads(fn, bits, packed, r, reference=False):
            # Packed is evaluator metadata, not an extra physical source field.
            p, j = packed & 7, packed >> 3
            need(0 <= j < 8 and 0 <= r < 8, 'three-bit source values')
            values, n = a.payloads(fn, bits, p, r, reference)
            if not reference:
                values[0, 0, -18] ^= j
            return values, n

    check0, n0 = Sources.payloads(functions, (0,)*6, 0, 0)
    check3, n3 = Sources.payloads(functions, (0,)*6, 24, 0)
    need(n0 == n3 and check0[0, 0, -18] ^ check3[0, 0, -18] == 3 and
         all(check0[key] == check3[key] for key in check0 if key != (0, 0, -18)),
         'one additional physical J source and no other source change')

    def target_q(bits, e=None):
        my = bits[2]
        return int(qt[a.index(bits+(7-2*my if e is None else e, 4*my+2+(1 ^ my)),
                              (2,)*6+(8, 8))], 16)

    def old_q(bits, values=None):
        if values is None:
            return int(pt[a.index(bits+(4, 5, 7), (2,)*6+(8,)*3)], 16)
        x, u, my, mr, aa, b = bits
        c = values[0, 0, -18] ^ a.enc(u ^ 1, 1, u ^ 1)
        return int(pt[a.index((x, u, my, mr, 1, 0, c,
                               values[1, 0, -17], values[-1, 0, -17]), (2,)*6+(8,)*3)], 16)

    @lru_cache(None)
    def local(u, aa, b, mr, j, p, r):
        values, n = Sources.payloads(functions, (0, u, 0, mr, aa, b), p+8*j, r)
        c, g = values[0, 0, -18], values[0, 0, -16]
        kp, km = values[1, 0, -17], values[-1, 0, -17]
        formula = c ^ a.h(a.h(c ^ kp) ^ a.h(c ^ km) ^ a.h(c ^ n) ^ a.h(c ^ g ^ kp ^ km))
        physical = {(v[0], v[1], -(v[2]+18)): value for v, value in values.items()}

        @lru_cache(None)
        def at(time, site):
            if time < 0:
                return 0
            if time == 0:
                return physical.get(site, 0)
            return at(time-2, site) ^ a.h(a.xor(at(time-1, a.add(site, d)) for d in a.D))

        need(at(1, (0, 0, 0)) == 0, 'complete previous J slice')
        need(at(2, (0, 0, 0)) == formula, 'full local native recursion versus cone formula')
        return formula

    baseline = [(bits, 0, 0, e, True) for bits in a.BITS for e in range(8)]
    base, old, direct = s.native_response(root, Sources, functions, baseline, pt)
    need(base == [target_q(bits, e) for bits, p, r, e, ref in baseline], '512 original source/E responses')
    need(old == [old_q(bits) for bits, p, r, e, ref in baseline], 'original whole q9 baseline')
    rows = []
    worlds = []
    for k in KNOWN:
        u, my, mr, aa, b = k
        target = a.enc(1 ^ aa ^ b ^ mr, 1 ^ (aa & mr),
                       mr ^ u ^ (u & aa) ^ (u & aa & mr))
        local_count = 0
        compatible = []
        for j, p, r in SOURCE_VALUES:
            if local(u, aa, b, mr, j, p, r) != target:
                continue
            local_count += 1
            values, _ = Sources.payloads(functions, (0,) + k, p+8*j, r)
            if all(old_q((x,) + k, values) == old_q((x,) + k) for x in UNKNOWN):
                compatible.append((j, p, r))
        rows.append({'known': k, 'complete_local_choices': local_count,
                     'whole_q9_choices': len(compatible), 'allowed_J_K_E': [], 'zero_J_values': []})
        for j, p, r in compatible:
            for e in range(8):
                for x in UNKNOWN:
                    worlds.append(((x,) + k, p+8*j, r, e, False))
    outputs = []
    for start in range(0, len(worlds), 512):
        out, _, count = s.native_response(root, Sources, functions, worlds[start:start+512], pt)
        outputs += out
        direct += count
    need(outputs and len(outputs) == len(worlds), 'nonvacuous complete actual-scale source comparison')
    certificate = []
    relaxed = [[] for k in KNOWN]
    permutations = 0
    for start in range(0, len(worlds), 16):
        block = worlds[start:start+16]
        bits, packed, r, _, _ = block[0]
        k, p, j = bits[1:], packed & 7, packed >> 3
        need(len(block) == 16 and all(w[0][1:] == k and w[1:3] == (packed, r) for w in block)
             and [w[0][0] for w in block] == list(UNKNOWN)*8
             and [w[3] for w in block] == [e for e in range(8) for x in UNKNOWN],
             'same physical J/K/E controls for both unknown inputs')
        values0, _ = Sources.payloads(functions, (0,)+k, packed, r)
        values1, _ = Sources.payloads(functions, (1,)+k, packed, r)
        need(values0 == values1, 'apparatus source payloads independent of unknown x')
        masks = []
        for x in UNKNOWN:
            values = outputs[start+x:start+16:2]
            need(len(set(values)) == 8, 'whole-triple E permutation')
            permutations += 1
            masks.append(sum(1 << e for e, value in enumerate(values) if value == target_q((x,)+k)))
        common = masks[0] & masks[1]
        if masks[0] and masks[1]:
            relaxed[KNOWN.index(k)].append((j, p, r))
        for e in range(8):
            if (common >> e) & 1:
                need(all(outputs[start+2*e+x] == target_q((x,)+k) for x in UNKNOWN),
                     'one identical E matches both actual outputs')
                rows[KNOWN.index(k)]['allowed_J_K_E'].append((j, p, r, e))
                if j == 0:
                    rows[KNOWN.index(k)]['zero_J_values'].append((p, r, e))
        if k == (0,)*5:
            certificate.append({'J_offset': j, 'plus_offset': p, 'minus_offset': r,
                                'E_mask_x0': masks[0], 'E_mask_x1': masks[1], 'intersection': common})
    zero_J = s.solve_domains([row['zero_J_values'] for row in rows])
    result = s.solve_domains([row['allowed_J_K_E'] for row in rows])
    need(s.solve_domains(relaxed)['status'] == 'COEFFICIENT_SOLVING_REQUIRED',
         'private-x-dependent E diagnostic removes pointwise obstruction')
    # Recovery and enlargement controls: the old certificate remains at j=0,
    # and genuine nonzero-J choices pass local/record gates before input testing.
    old_certificate = [v for v in certificate if v['J_offset'] == 0]
    new_certificate = [v for v in certificate if v['J_offset'] != 0]
    need(old_certificate and new_certificate, 'J extension genuinely enlarges the old-record domain')
    for v in old_certificate:
        p, r = v['plus_offset'], v['minus_offset']
        expected = (6, 3) if p == r else ((0, 3) if (p, r) in ((1, 5), (5, 1)) else (7, 6))
        need((v['E_mask_x0'], v['E_mask_x1']) == tuple(1 << e for e in expected),
             'accepted zero-J certificate recovered')
    continuing = [row for row in rows if row['known'][3:] != (0, 1)]
    return {'schema': 'oi.native-J-coordination.v1', 'status': 'PASS',
            'verdict': 'UNSAT_WITH_EXISTING_J_COORDINATION' if result['status'] == 'UNSAT'
                       else 'COEFFICIENT_AND_FULL_INPUT_SOLVING_REQUIRED',
            'known_order': ['u', 'mY', 'mR', 'a', 'b'], 'affine_coefficient_bits': 72,
            'pointwise_J_K_context_cases': len(KNOWN)*len(SOURCE_VALUES),
            'distinct_local_recursions': local.cache_info().currsize,
            'baseline_worlds': len(baseline), 'candidate_worlds': len(worlds),
            'upper_direct_scalar_lanes': direct, 'E_permutation_controls': permutations,
            'pointwise_result': result, 'zero_J_result': zero_J,
            'continuing_empty_domains': sum(not row['allowed_J_K_E'] for row in continuing),
            'certificate_known': (0,)*5, 'certificate': certificate,
            'witness_target_Q': [target_q((x,)+(0,)*5) for x in UNKNOWN],
            'witness_old_q9': [old_q((x,)+(0,)*5) for x in UNKNOWN],
            'rows': rows, 'measurement_output_tests': 0,
            'full_carrier': 'NOT_ESTABLISHED', 'physical_selection_or_reuse': 'NOT_ESTABLISHED'}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parents[2] /
                    'oi-qm/reconstruction/native-y-continuation-20261024')
    ap.add_argument('--synthesis', type=Path, default=Path(__file__).with_name('native_affine_delivery_synthesis.py'))
    ap.add_argument('--asymmetric', type=Path, default=Path(__file__).with_name('native_asymmetric_delivery_probe.py'))
    args = ap.parse_args()
    try:
        result = run(args.source_root, args.synthesis, args.asymmetric)
    except (RuntimeError, ValueError, KeyError, OSError, StopIteration, TypeError) as exc:
        print(json.dumps({'status': 'VOID', 'reason': str(exc)}, sort_keys=True))
        raise SystemExit(2)
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))
