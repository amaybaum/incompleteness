#!/usr/bin/env python3
"""Targeted G/N source screening with complete earlier records and local output."""
import argparse
import ast
from collections import Counter
from functools import lru_cache
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def load(path, name, digest):
    need(hashlib.sha256(path.read_bytes()).hexdigest() == digest, 'source pin '+path.name)
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


KNOWN = tuple(itertools.product(range(2), repeat=5))
UNKNOWN = (0, 1)
TRIPLES = tuple(itertools.product(range(8), repeat=3))


def run(root, synthesis_path, asymmetric_path):
    need(len(KNOWN) == 32 and len(set(KNOWN)) == 32 and UNKNOWN == (0, 1) and len(TRIPLES) == 512,
         'complete known/unknown/source domains')
    need(sum(k[3:] == (0, 1) for k in KNOWN) == 8, 'terminal protocol coverage')
    a = load(asymmetric_path, 'accepted_asymmetric',
             '680496938b5df4758754615030770ca9f2daadde7565a4fcbc44559da04b4e1d')
    s = load(synthesis_path, 'accepted_synthesis',
             '15971d7abcacd075f86e17f79b812d5365bed6c4bb38980a8c9987f1c0efaea3')
    engine = a.pinned(root/'native_route_v13/checks.py',
                      '8c1bbc37f47b6ff7ad7ee67d719f058067e2e15e9a6a967adfb78ef57d1ed856')
    qt = json.loads((root/'native_route_v13/result.json').read_text())['q10_table_hex']
    pt = json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    need(hashlib.sha256(qt.encode()).hexdigest() ==
         'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc', 'Q table pin')
    need(hashlib.sha256(pt.encode()).hexdigest() ==
         'dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf', 'q9 table pin')
    tree = ast.parse(engine)
    node = next(n.value for n in tree.body if isinstance(n, ast.Assign) and
                any(isinstance(t, ast.Name) and t.id == 'SOURCES' for t in n.targets))
    functions = {ast.literal_eval(k): eval(compile(ast.Expression(v.args[0]), '<pinned sources>', 'eval'),
                                         {'TR': tuple(itertools.product(range(2), repeat=3)), '__builtins__': {}})
                 for k, v in zip(node.keys, node.values)}
    # Primary physical positions are read as declarations, not inferred from
    # the collapsed upper-strip coordinates used by the evaluator.
    geometry = a.pinned(root/'native_vread_v15/checks.py',
                        '93b4161f32e02874769d57d8a670d1a460d26fa2c953d517db5c6564fb649824')
    source_fn = next(n for n in ast.parse(geometry).body if isinstance(n, ast.FunctionDef) and n.name == 'local_sources')
    T = 185
    P = 12*840**185
    S = P+T
    R = S+68
    L = R+9
    positions = eval(compile(ast.Expression(source_fn.body[0].value), '<pinned positions>', 'eval'),
                     {'S': S, 'T': T, 'P': P, 'R': R, 'L': L, '__builtins__': {}})
    q8 = (0, S, 76)
    deadline = R+8
    distance = lambda v: sum(abs(x-y) for x, y in zip(v, q8))
    slack = {name: distance(positions[name])-deadline for name in ('G', 'J', 'Kplus', 'Kminus', 'N', 'E')}
    need(slack['G'] == 0 and all(slack[name] > 0 for name in slack if name != 'G'),
         'only G reaches q8 among the adjustable sources')
    need(sum(x != y for x, y in zip(positions['G'], q8)) == 1 and
         len({a.h(v) for v in range(8)}) == 8, 'unique axial first arrival with bijective h')
    q9 = (0, S, 77)
    need(all(sum(abs(x-y) for x, y in zip(positions[name], q9)) > L for name in ('N', 'E')),
         'N and E cannot change old q9 at its deadline')

    def target_q(bits, e=None):
        my = bits[2]
        return int(qt[a.index(bits+(7-2*my if e is None else e, 4*my+2+(1 ^ my)), (2,)*6+(8, 8))], 16)

    def old_q(bits, values=None):
        if values is None:
            return int(pt[a.index(bits+(4, 5, 7), (2,)*6+(8,)*3)], 16)
        x, u, my, mr, aa, b = bits
        c = values[0, 0, -18] ^ a.enc(u ^ 1, 1, u ^ 1)
        return int(pt[a.index((x, u, my, mr, 1, 0, c, values[1, 0, -17], values[-1, 0, -17]),
                              (2,)*6+(8,)*3)], 16)

    class NSource:
        enc = staticmethod(a.enc)
        index = staticmethod(a.index)

        @staticmethod
        def payloads(fn, bits, packed, r, reference=False):
            p, j, n = packed & 7, (packed >> 3) & 7, packed >> 6
            need(0 <= n < 8, 'three-bit N source')
            values, original_n = a.payloads(fn, bits, p, r, reference)
            if not reference:
                values[0, 0, -18] ^= j
                values[0, 0, -20] = n
            return values, original_n if reference else n

    v0, n0 = NSource.payloads(functions, (0,)*6, 0, 0)
    v4, n4 = NSource.payloads(functions, (0,)*6, 256, 0)
    need((n0, n4) == (0, 4) and v0[0, 0, -20] ^ v4[0, 0, -20] == 4 and
         all(v0[key] == v4[key] for key in v0 if key != (0, 0, -20)),
         'one real N source change without modifying other sources')

    def g_response(worlds, baseline=False):
        # Same retained base/strip and native collision. Changed-G earlier
        # records are measured constraints, not assumed preserved by a guard.
        spec = importlib.util.spec_from_file_location('G_screen_route', root/'native_route_v13/checks.py')
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        data = []
        payloads = []
        for x, g, reference in worlds:
            values, n = a.payloads(functions, (x, 0, 0, 0, 0, 0), 0, 0, reference)
            if not reference:
                values[0, 0, -16] = g
            data.append((x, 0, 0, 0, 0, 0, 7, n))
            payloads.append(values)
        count = len(worlds)
        m.ROWS = tuple(data)
        m.UR = tuple(range(count))
        m.FULL = m.UF = (1 << count)-1
        m.XM, m.UM, m.MY, m.MR = tuple(sum(row[j] << i for i, row in enumerate(data)) for j in range(4))
        m.SOURCES = {key: tuple(sum(((row[key] >> (2-f)) & 1) << i for i, row in enumerate(payloads))
                                for f in range(3)) for key in m.SOURCES}
        m.expand_upper = lambda q: q
        m.CONTROLS = [((0, -m.S, -68), m.XM), ((0, m.S, -68), m.MY ^ m.MR),
                      ((m.T, m.P, -68), m.MY), ((-m.T, m.P, -68), m.MR)]
        direct = 0
        for ell, xx, yy in ((18, 0, 0), (18, -1, 1), (18, 1, 1), (20, 0, 0)):
            for n in (0, 1):
                need(m.upper_strip()[ell, xx, yy][n] == m.direct_upper(n+ell, xx, yy, n),
                     'G strip versus direct native recursion')
                direct += count
        end = (0, 0, 10)
        previous = {v: m.base(m.R-2, v) for v in m.ball(10, end)}
        current = {v: m.base(m.R-1, v) for v in m.ball(11, end)}
        records = {}
        for tau in range(11):
            future = {}
            for v in m.ball(10-tau, end):
                neighbors = [current[tuple(v[j]+(sign if j == axis else 0) for j in range(3))]
                             for axis in range(3) for sign in (-1, 1)]
                future[v] = m.xx(previous[v], m.h(m.xx(*neighbors)))
            records[tau] = future
            previous, current = current, future
        if baseline:
            expected, expected_records = m.native_compute()
            need(records == expected_records and current[end] == expected,
                 'complete collision replay equals untouched baseline engine')
        coordinates = ((0, (0, 0, 0)), (7, (0, 0, 7)), (8, (0, 0, 8)),
                       (9, (0, 0, 9)), (10, end))
        return [[m.code(m.lane(records[tau][pos], i)) for tau, pos in coordinates]
                for i in range(count)], direct

    reference, direct = g_response([(x, 3, True) for x in UNKNOWN], baseline=True)
    need([row[-1] for row in reference] == [target_q((x, 0, 0, 0, 0, 0)) for x in UNKNOWN]
         and [row[-2] for row in reference] == [old_q((x, 0, 0, 0, 0, 0)) for x in UNKNOWN],
         'G reference full Q/q9 tables')
    g_values, d = g_response([(x, g, False) for g in range(8) for x in UNKNOWN])
    direct += d
    g_rows = [{'G_code': g, 'q8_x0_x1': [g_values[2*g+x][2] for x in UNKNOWN],
               'prefix_preserved': all(g_values[2*g+x][:3] == reference[x][:3] for x in UNKNOWN)}
              for g in range(8)]
    need(all(len({row['q8_x0_x1'][x] for row in g_rows}) == 8 for x in UNKNOWN),
         'G first-arrival whole-q8 permutations')
    original_G = a.payloads(functions, (0,)*6, 0, 0)[0][0, 0, -16]
    allowed_G = [row['G_code'] for row in g_rows if row['prefix_preserved']]
    need(all(g_rows[g]['q8_x0_x1'] == [reference[x][2] for x in UNKNOWN] for g in allowed_G),
         'every allowed G retains the complete earlier q8 record')
    need(original_G in allowed_G, 'original G preserves the old prefix')
    nontrivial_G = [g for g in allowed_G if g != original_G]

    inv = {a.h(v): v for v in range(8)}

    @lru_cache(None)
    def local_values(u, aa, b, mr, j, p, r):
        values, _ = NSource.payloads(functions, (0, u, 0, mr, aa, b), p+8*j, r)
        c, g = values[0, 0, -18], values[0, 0, -16]
        kp, km = values[1, 0, -17], values[-1, 0, -17]
        target = a.enc(1 ^ aa ^ b ^ mr, 1 ^ (aa & mr), mr ^ u ^ (u & aa) ^ (u & aa & mr))
        fixed = a.h(c ^ kp) ^ a.h(c ^ km) ^ a.h(c ^ g ^ kp ^ km)
        n = c ^ inv[inv[c ^ target] ^ fixed]
        responses = [c ^ a.h(fixed ^ a.h(c ^ z)) for z in range(8)]
        need(len(set(responses)) == 8 and [z for z, value in enumerate(responses) if value == target] == [n],
             'unique full-local-output N determined without dropping fields')
        values[0, 0, -20] = n
        physical = {(v[0], v[1], -(v[2]+18)): z for v, z in values.items()}

        @lru_cache(None)
        def at(t, v):
            if t < 0:
                return 0
            if t == 0:
                return physical.get(v, 0)
            return at(t-2, v) ^ a.h(a.xor(at(t-1, a.add(v, direction)) for direction in a.D))

        need(at(1, (0, 0, 0)) == 0 and at(2, (0, 0, 0)) == target,
             'complete local current/previous native recursion')
        return n

    baseline = [(bits, 0, 0, e, True) for bits in a.BITS for e in range(8)]
    base, old, d = s.native_response(root, NSource, functions, baseline, pt)
    direct += d
    need(base == [target_q(bits, e) for bits, p, r, e, ref in baseline] and
         old == [old_q(bits) for bits, p, r, e, ref in baseline], '512 original E/N0/reference worlds')
    rows = []
    failed = None
    candidate_worlds = 0
    permutations = 0
    for k in KNOWN:
        u, my, mr, aa, b = k
        controls = []
        for j, p, r in TRIPLES:
            n = local_values(u, aa, b, mr, j, p, r)
            values, _ = NSource.payloads(functions, (0,)+k, p+8*j+64*n, r)
            need(values == NSource.payloads(functions, (1,)+k, p+8*j+64*n, r)[0],
                 'N/J/K sources independent of unknown x')
            if all(old_q((x,)+k, values) == old_q((x,)+k) for x in UNKNOWN):
                controls.append((n, j, p, r))
        worlds = [((x,)+k, p+8*j+64*n, r, e, False)
                  for n, j, p, r in controls for e in range(8) for x in UNKNOWN]
        need(worlds, 'nonvacuous N old-record domain')
        outputs = []
        for start in range(0, len(worlds), 512):
            out, _, d = s.native_response(root, NSource, functions, worlds[start:start+512], pt)
            outputs += out
            direct += d
        candidate_worlds += len(worlds)
        allowed = []
        certificate = []
        histogram = Counter()
        for i, (n, j, p, r) in enumerate(controls):
            masks = []
            for x in UNKNOWN:
                values = outputs[16*i+x:16*i+16:2]
                need(len(set(values)) == 8, 'N-screen whole-triple E permutations')
                permutations += 1
                masks.append(sum(1 << e for e, value in enumerate(values) if value == target_q((x,)+k)))
            common = masks[0] & masks[1]
            e0, e1 = (mask.bit_length()-1 for mask in masks)
            histogram[e0, e1] += 1
            for e in range(8):
                if (common >> e) & 1:
                    need(all(outputs[16*i+2*e+x] == target_q((x,)+k) for x in UNKNOWN),
                         'same E satisfies both actual native outputs')
                    allowed.append((n, j, p, r, e))
            certificate.append((n, j, p, r, e0, e1))
        row = {'known': k, 'terminal': k[3:] == (0, 1), 'local_quadruples': len(TRIPLES),
               'old_q9_quadruples': len(controls), 'allowed': allowed,
               'required_E_pair_histogram': [[e0, e1, count] for (e0, e1), count in sorted(histogram.items())]}
        rows.append(row)
        if not allowed and not row['terminal']:
            failed = {'known': k, 'Q_targets': [target_q((x,)+k) for x in UNKNOWN],
                      'q9_targets': [old_q((x,)+k) for x in UNKNOWN], 'source_certificate': certificate}
            break
        # The first context is the targeted screen; no later context is
        # evaluated unless this necessary gate admits a common control.
        if k == (0,)*5 and not allowed:
            break
    initial_survived = bool(rows[0]['allowed'])
    if failed is not None:
        need(not any(e0 == e1 for e0, e1, count in rows[-1]['required_E_pair_histogram']),
             'empty continuing N domain has no common-E diagonal')
    verdict = ('G_PREFIX_FIXED_N_CONTINUING_DOMAIN_UNSAT' if not nontrivial_G and failed is not None else
               'FURTHER_SOURCE_SYNTHESIS_REQUIRED')
    return {'schema': 'oi.native-GN-screen.v1', 'status': 'PASS', 'verdict': verdict,
            'G': {'geometry_q8_slacks': slack, 'unique_axis_first_arrival': True,
                  'prefix_rows': g_rows, 'allowed_values': allowed_G, 'nontrivial_values': nontrivial_G},
            'N': {'affine_coefficient_bits': 90, 'initial_screen_survived': initial_survived,
                  'contexts_tested': len(rows), 'contexts_required': len(KNOWN), 'rows': rows,
                  'continuing_counterexample': failed, 'global_coefficient_search': 'NOT_NEEDED' if failed else 'OPEN'},
            'candidate_N_worlds': candidate_worlds, 'baseline_worlds': 512,
            'G_worlds_with_reference': 18, 'local_inverse_cases': local_values.cache_info().currsize,
            'E_permutation_controls': permutations, 'upper_direct_scalar_lanes': direct,
            'full_42bit_carrier': 'NOT_ESTABLISHED', 'measurement_output_tests': 0,
            'physical_selection_or_reuse': 'NOT_ESTABLISHED'}


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
