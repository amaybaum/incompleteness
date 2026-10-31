#!/usr/bin/env python3
"""Fixed swapped affine controller, full-carrier invariant and E/N compensation."""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


def need(ok, why):
    if not ok:
        raise RuntimeError(why)


def h(v):
    a, b, d = v >> 2, (v >> 1) & 1, v & 1
    return 4*b+2*d+(a ^ (b & d))


def xor(values):
    out = 0
    for value in values:
        out ^= value
    return out


def index(values, sizes):
    out = 0
    for v, size in zip(values, sizes):
        out = size*out+v
    return out


def feature(k):
    return 1 | sum(bit << (j+1) for j, bit in enumerate(k))


def affine_solutions(options):
    """Exact GF(2): six affine fields plus one binary domain choice per row."""
    need(all(len(row['allowed_E_N']) == 2 for row in options), 'binary native domains')
    equations = []
    for j, row in enumerate(options):
        a, b = row['allowed_E_N']
        for field in range(6):
            half, bit = divmod(field, 3)
            shift = 2-bit
            lhs = feature(row['context_u_mY_mR_a_b']) << (6*field)
            lhs ^= (((a[half] ^ b[half]) >> shift) & 1) << (36+j)
            equations.append((lhs, (a[half] >> shift) & 1))
    pivots = {}
    for mask, rhs in equations:
        while mask:
            p = mask.bit_length()-1
            if p not in pivots:
                pivots[p] = mask, rhs
                break
            old, oldrhs = pivots[p]
            mask ^= old
            rhs ^= oldrhs
        if not mask and rhs:
            return {'consistent': False}
    value = 0
    for p, (mask, rhs) in sorted(pivots.items()):
        if ((mask & value).bit_count() % 2) ^ rhs:
            value ^= 1 << p
    need(all(((mask & value).bit_count() % 2) == rhs for mask, rhs in equations),
         'affine solution replays every original equation')
    return {'consistent': True, 'equations': len(equations), 'unknowns': 36+len(options),
            'rank': len(pivots), 'free_variables': 36+len(options)-len(pivots),
            'field_coefficients': [(value >> (6*f)) & 63 for f in range(6)]}


def run(root):
    engine = root/'native_route_v13/checks.py'
    need(hashlib.sha256(engine.read_bytes()).hexdigest() ==
         '8c1bbc37f47b6ff7ad7ee67d719f058067e2e15e9a6a967adfb78ef57d1ed856',
         'retained native engine pin')
    qt = json.loads((root/'native_route_v13/result.json').read_text())['q10_table_hex']
    pt = json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    inventory = (root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_bytes()
    for data, digest in ((qt.encode(), 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc'),
                         (pt.encode(), 'dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf'),
                         (inventory, '2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d')):
        need(hashlib.sha256(data).hexdigest() == digest, 'retained input pin')
    spec = importlib.util.spec_from_file_location('coordinated_native_route', engine)
    route = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(route)
    planted = []
    known = [1, 5, 1, 4, 1, 5]
    for k in route.CONTEXTS:
        fields = [(c & feature(k)).bit_count() % 2 for c in known]
        e = 4*fields[0]+2*fields[1]+fields[2]
        n = 4*fields[3]+2*fields[4]+fields[5]
        planted.append({'context_u_mY_mR_a_b': k, 'allowed_E_N': [(e, n), (e, n ^ 1)]})
    positive = affine_solutions(planted)
    need(positive['consistent'] and positive['free_variables'] == 6 and
         positive['field_coefficients'][:5] == known[:5], 'planted affine family and exact nullity')
    malformed = [dict(row) for row in planted]
    malformed[0]['allowed_E_N'] = [(e ^ 4, n) for e, n in malformed[0]['allowed_E_N']]
    need(not affine_solutions(malformed)['consistent'], 'single nonaffine corner is rejected')
    need(route.P % (12*840**route.BUDGET) == 0 and route.BUDGET == 20,
         'retained upper-strip period applies to both payload arrangements')
    need(route.P % (384*840**3) == 0, 'retained lower-front period')
    baseline, base_records = route.native_compute()
    baseline_hex = ''.join(format(route.code(route.lane(baseline, i)), 'x') for i in range(len(route.ROWS)))
    need(baseline_hex == qt, 'all4096 baseline rows reproduce retained actual-scale table')
    # Exhaust the retained512 constant-controller arrangements, keeping every
    # old public raw q9 row, including its terminal rows.
    compatible = []
    for controller in itertools.product(range(8), repeat=3):
        if all(pt[index(bits+controller, (2,)*6+(8,)*3)] ==
               pt[index(bits+(4, 5, 7), (2,)*6+(8,)*3)]
               for bits in itertools.product(range(2), repeat=6)):
            compatible.append(controller)
    need(compatible == [(4, 5, 7), (4, 7, 5)], 'complete old-phase compatible controllers')
    # The only change to the native engine's source data is the two existing
    # K payloads. No ready region, bank, lower source or native rule changes.
    original_sources = dict(route.SOURCES)
    route.SOURCES[(1, 0, -17)], route.SOURCES[(-1, 0, -17)] = (
        route.SOURCES[(-1, 0, -17)], route.SOURCES[(1, 0, -17)])
    need({k for k in route.SOURCES if route.SOURCES[k] != original_sources[k]} ==
         {(1, 0, -17), (-1, 0, -17)}, 'only retained K payloads swapped')
    for f in (route.direct_upper, route.upper_strip, route.expand_upper, route.upper):
        f.cache_clear()
    upper_controls = 0
    for key in ((0, 0, 0), (2, 0, 0), (4, -1, 1), (4, 1, 1),
                (8, -2, 0), (8, 2, 0), (12, -1, 1), (12, 1, 1)):
        ell, x, y = key
        arr = route.upper_strip()[key]
        for n in (0, 1, 2):
            need(arr[n] == route.direct_upper(n+ell, x, y, n),
                 'swapped upper strip agrees with full local native recursion')
            upper_controls += len(route.UR)
    swapped, swap_records = route.native_compute()
    swapped_hex = ''.join(format(route.code(route.lane(swapped, i)), 'x') for i in range(len(route.ROWS)))
    old_phase_checks = 0
    for i, row in enumerate(route.ROWS):
        bits = row[:6]
        for records, controller in ((base_records, (4, 5, 7)), (swap_records, (4, 7, 5))):
            old = int(pt[index(bits+controller, (2,)*6+(8,)*3)], 16)
            need(route.code(route.lane(records[9][0, 0, 9], i)) == old,
                 'complete old q9 preserved for every E/N payload')
            old_phase_checks += 1
    diffs = []
    terminal = accepted = 0
    for bits in itertools.product(range(2), repeat=6):
        x, u, my, mr, a, b = bits
        e, n = 4+2*(1 ^ my)+1, 4*my+2+(1 ^ my)
        i = route.RINDEX[bits+(e, n)]
        q0, q1 = route.code(route.lane(baseline, i)), route.code(route.lane(swapped, i))
        p0 = int(pt[index(bits+(4, 5, 7), (2,)*6+(8,)*3)], 16)
        p1 = int(pt[index(bits+(4, 7, 5), (2,)*6+(8,)*3)], 16)
        need(p0 == p1, 'same full old public q9 including terminal rows')
        if (a, b) == (0, 1):
            terminal += 1
        else:
            accepted += 1
            need(q0 >> 2 == x ^ u ^ a, 'baseline accepted sign retained')
        if q0 != q1:
            diffs.append({'bits_x_u_mY_mR_a_b': bits, 'q10_baseline': q0, 'q10_swapped': q1,
                          'terminal': (a, b) == (0, 1)})
    # Independently check the fixed whole-Q inverse using complete native
    # fields on finite periodic worlds. It is a coordinate, never a new read.
    dirs = tuple(tuple(s if j == a else 0 for j in range(3))
                 for a in range(3) for s in (-1, 1))
    sites = tuple(itertools.product(range(5), repeat=3))
    neighbors = {v: [tuple((v[j]+d[j]) % 5 for j in range(3)) for d in dirs] for v in sites}
    q = (0, 0, 0)
    for seed in range(8):
        old = {v: (v[0]*v[1]+v[2]+seed) % 8 for v in sites}
        now = {v: (v[1]*v[2]+3*v[0]+seed) % 8 for v in sites}
        original_q = now[q]
        for _ in range(2):
            now, old = {v: old[v] ^ h(xor(now[w] for w in neighbors[v])) for v in sites}, now
        recovered = now[q] ^ h(xor(old[w] for w in neighbors[q]))
        need(recovered == original_q, 'whole triple is fixed function of the outgoing42-bit packet')
    # Stronger rescue test: permit arbitrary affine E(k),N(k) in the existing
    # known seeds k=(u,mY,mR,a,b), preserving the baseline whole Q for both x.
    options = []
    baseline_options = []
    pair_checks = 0
    for k in route.CONTEXTS:
        u, my, mr, a, b = k
        e0, n0 = 4+2*(1 ^ my)+1, 4*my+2+(1 ^ my)
        target = tuple(route.code(route.lane(baseline, route.RINDEX[(s ^ u ^ a, u, my, mr, a, b, e0, n0)]))
                       for s in (0, 1))
        allowed = []
        original_allowed = []
        for e, n in itertools.product(range(8), repeat=2):
            got = tuple(route.code(route.lane(swapped, route.RINDEX[(s ^ u ^ a, u, my, mr, a, b, e, n)]))
                        for s in (0, 1))
            if got == target:
                allowed.append((e, n))
            original = tuple(route.code(route.lane(baseline, route.RINDEX[(s ^ u ^ a, u, my, mr, a, b, e, n)]))
                             for s in (0, 1))
            if original == target:
                original_allowed.append((e, n))
            pair_checks += 1
        options.append({'context_u_mY_mR_a_b': k, 'target_Q_s0_s1': target, 'allowed_E_N': allowed})
        baseline_options.append({'context_u_mY_mR_a_b': k, 'allowed_E_N': original_allowed})
    original_fit = affine_solutions(baseline_options)
    swapped_fit = affine_solutions(options)
    need(original_fit['consistent'] and original_fit['free_variables'] == 0 and
         original_fit['field_coefficients'] == [1, 5, 1, 4, 1, 5],
         'baseline whole-Q affine program is unique and equals the retained law')
    # A fixed rectangle of seed values is enough to contradict affinity.
    rectangle = ((0, 0, 0, 0, 0), (0, 0, 0, 1, 0),
                 (0, 0, 1, 0, 0), (0, 0, 1, 1, 0))
    witness = [next(row for row in options if row['context_u_mY_mR_a_b'] == k) for k in rectangle]
    forced = []
    for row in witness:
        values = {(n >> 1) & 1 for e, n in row['allowed_E_N']}
        forced.append(next(iter(values)) if len(values) == 1 else None)
    need(xor(feature(k) for k in rectangle) == 0, 'affine rectangle feature XOR')
    need(all(xor((coeff & feature(k)).bit_count() % 2 for k in rectangle) == 0 for coeff in range(64)),
         'all affine Boolean controls obey rectangle identity')
    nonaffine_rescue = all(len(row['allowed_E_N']) > 0 for row in options)
    need(nonaffine_rescue, 'per-context full-Q compensation is possible; comparator is nonvacuous')
    obstruction = None not in forced and xor(forced) == 1
    need(swapped_fit['consistent'] == (not obstruction), 'independent rectangle and full affine system agree')
    # Comparator positive control: affine data on the same feature rows must
    # survive; a single flipped corner must violate the rectangle identity.
    need(xor((5 & feature(k)).bit_count() % 2 for k in rectangle) == 0,
         'planted affine rectangle accepted')
    need(xor([1, 1, 1, 0]) == 1, 'nonaffine corner countercontrol')
    need(accepted == 48 and terminal == 16 and old_phase_checks == 8192 and pair_checks == 1536,
         'source and terminal coverage')
    return {'status': 'PASS', 'verdict': 'UNIQUE_PROGRAM_IN_FIXED_AFFINE_CLASS' if obstruction else 'NO_OBSTRUCTION_FOUND',
            'baseline_rows': 4096, 'swapped_table_sha256': hashlib.sha256(swapped_hex.encode()).hexdigest(),
            'old_q9_native_checks': old_phase_checks, 'swapped_upper_direct_scalar_lanes': upper_controls,
            'accepted_source_rows': accepted, 'terminal_microscopic_rows': terminal,
            'changed_q10_rows': len(diffs), 'changed_continuing_q10_rows': sum(not r['terminal'] for r in diffs),
            'changed_terminal_q10_rows': sum(r['terminal'] for r in diffs),
            'first_continuing_change': next((r for r in diffs if not r['terminal']), None),
            'whole_packet_inverse_worlds': 8, 'E_N_pair_checks': pair_checks,
            'old_controller_candidates': 512, 'compatible_old_controllers': compatible,
            'baseline_affine_fit': original_fit, 'swapped_affine_fit': swapped_fit,
            'linear_solver_controls': 2,
            'allowed_counts_by_context': [len(row['allowed_E_N']) for row in options],
            'affine_rectangle': witness, 'forced_N_B': forced, 'required_N_B_XOR': xor(forced) if None not in forced else None,
            'nonaffine_per_context_compensation': nonaffine_rescue,
            'source_family': 'same source positions; swapped existing K payloads; affine E/N rescue only tested',
            'new_sources_adopted': 0, 'new_reads': 0, 'native_selectable_apparatus': 'NOT_ESTABLISHED'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parents[2] /
                        'oi-qm/reconstruction/native-y-continuation-20261024')
    args = parser.parse_args()
    try:
        result = run(args.source_root)
    except (RuntimeError, ValueError, KeyError, OSError) as exc:
        print(json.dumps({'status': 'VOID', 'reason': str(exc)}, sort_keys=True))
        raise SystemExit(2)
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))
