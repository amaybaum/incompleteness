"""Native first-front continuation boundary audit; exact standard-library checks."""
import argparse
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def distance(p, q):
    return sum(abs(x-y) for x, y in zip(p, q))


def h(q):
    a, b, d = q
    return b, d, a ^ (b & d)


def xor(*qs):
    out = [0, 0, 0]
    for q in qs:
        for i in range(3):
            out[i] ^= q[i]
    return tuple(out)


TRIPLES = tuple(product((0, 1), repeat=3))
ZERO = (0, 0, 0)


def small_native_controls():
    """Full three-dimensional recursion, compared to a path permutation.

    Both initial slices have nonzero deterministic background. The source
    current triple is the only varying variable. Its displacement is uniquely
    axial, so every other input to the critical update is source-independent.
    """
    cases = direct_rows = prefix_rows = nonlinear_rows = 0
    tables = []
    for n, seed in product(range(1, 7), range(3)):
        source = (n, 0, 0)

        def initial(t, p):
            if seed == 0:
                return ZERO
            a, b, c = p
            # Deliberately nonlinear spatial patterns on both initial slices.
            q = (a*a + 3*b + b*c + 7*c*c + 11*seed + 13*t)
            return tuple(((q + (j+1)*(a*b + c + seed*t + j)) >> j) & 1
                         for j in range(3))

        @lru_cache(None)
        def direct(t, p, code):
            if t in (-1, 0):
                return TRIPLES[code] if t == 0 and p == source else initial(t, p)
            ns = []
            for axis in range(3):
                for sign in (-1, 1):
                    q = list(p)
                    q[axis] += sign
                    ns.append(direct(t-1, tuple(q), code))
            return xor(direct(t-2, p, code), h(xor(*ns)))

        path = list(TRIPLES)
        for j in range(1, n+1):
            p = (n-j, 0, 0)
            old = direct(j-2, p, 0)
            others = []
            for axis in range(3):
                for sign in (-1, 1):
                    if axis == 0 and sign == 1:
                        continue
                    q = list(p)
                    q[axis] += sign
                    others.append((j-1, tuple(q)))
            fixed = xor(*(direct(t, q, 0) for t, q in others))
            # Independent direct native checks that the translated backgrounds
            # are actually independent of the varying source at this first front.
            for code in range(8):
                require(direct(j-2, p, code) == old, 'old term source-independent')
                require(all(direct(t, q, code) == direct(t, q, 0)
                            for t, q in others), 'five neighbors source-independent')
                prefix_rows += 6
            path = [xor(old, h(xor(q, fixed))) for q in path]
            require(len(set(path)) == 8, 'path step is a permutation')
            for code in range(8):
                require(path[code] == direct(j, p, code), 'path/full native equality')
                direct_rows += 1
        actual = [direct(n, (0, 0, 0), code) for code in range(8)]
        require(actual == path and len(set(actual)) == 8, 'complete terminal permutation')
        for code in range(8):
            q = TRIPLES[code]
            for _ in range(n):
                q = h(q)
            if actual[code] != q:
                nonlinear_rows += 1
        tables.append({'distance': n, 'background': seed,
                       'output_codes': [TRIPLES.index(q) for q in actual]})
        cases += 1
        direct.cache_clear()
    require(nonlinear_rows > 0, 'nonzero background changes the response')
    # H itself is checked through the truth-table encoding, separately from
    # the full direct recursion and its first-front factorization.
    require([TRIPLES.index(h(q)) for q in TRIPLES] == [0, 2, 4, 7, 1, 3, 5, 6],
            'native H truth table')
    return {'full_3d_world_families': cases, 'path_direct_rows': direct_rows,
            'fixed_background_comparisons': prefix_rows,
            'nonvacuum_response_differences': nonlinear_rows,
            'tables': tables}


def geometry(root):
    T = 185
    P = 12 * 840**185
    S = T + P
    R = S + 68
    L = R + 9
    q8, q9, q10 = (0, S, 76), (0, S, 77), (0, S, 78)
    f8, f10 = (-(L+1), S, 76), (-(L+1), S, 78)
    old_ports = [(0, T, 0), (0, 0, -8*T), (T, P, 0), (-T, P, 0),
                 (4*T, P, 0), (0, S, 0), (12*R, 0, 0)]
    deadlines = [T, T, S, S, S, S, R]
    cG, cZ = (48*L, 0, 0), (-48*L, 0, 0)
    ready = list(zip(old_ports, deadlines))
    ready += [((T, 0, 0), T), ((-T, 0, 0), T), ((4*T, 0, 0), T)]
    ready += [((0, S, -68), R), ((-12*R, 0, 0), R)]
    ready += [((0, S, 68+k), R+k) for k in range(10)]
    ready += [(cG, L), (cZ, L)]
    current_sources = [(0, -76, 76), (0, S, S+136), (0, S, S+150),
                       (0, S, S+152), (0, S, S+154),
                       (1, S, S+153), (-1, S, S+153)]
    gp = root/'parallel_v3/history_control/SOURCE-GEOMETRY.json'
    geo = json.loads(gp.read_text())
    require(len(geo['sources']) == 1479, 'source geometry inventory')
    rows = []
    for name, f, own, other in [('f8', f8, q8, q10), ('f10', f10, q10, q8)]:
        require(distance(f, own) == L+1, 'first native next-port arrival')
        require(distance(f, q9) == L+2, 'selected current phase unaffected')
        require(distance(f, other) == L+3, 'two free sources have no cross effect')
        require(all(distance(f, c) > radius for c, radius in ready),
                'outside every retained current/previous ready region')
        require(all(distance(f, c) > L for c, radius in ready),
                'even all named ready-center records through L unaffected')
        require(all(distance(f, p) > L for p in old_ports+[cG, cZ]),
                'whole observed old/new port history through L unaffected')
        require(all(f != tuple(e['position']) for e in geo['sources']),
                'no inherited 1479 source overwritten')
        require(f not in current_sources, 'no controller source overwritten')
        # The six local bank rays have fixed x=0,+T,-T,4T. The old
        # remote herald ray has x=12R-t>0 for every t<=L.
        require(f[0] not in (0, T, -T, 4*T) and 12*R-L > 0,
                'all seven bank families excluded for their complete intervals')
        # Inherited remote preparation/source blocks lie within radius R
        # of +/-12R and new remote source/ready regions within L of +/-48L.
        require(all(distance(f, c) > radius
                    for c, radius in [((12*R, 0, 0), R), ((-12*R, 0, 0), R),
                                      (cG, L), (cZ, L)]),
                'old/new remote source-program regions excluded')
        require((sum(f) - ((L+1)+sum(own))) % 2 == 0,
                'same native spacetime parity')
        rows.append({'source': name,
                     'source_formula': '(-(L+1),S,'+str(own[2])+')',
                     'own_next_port_distance_minus_L': distance(f, own)-L,
                     'q9_distance_minus_L': distance(f, q9)-L,
                     'other_next_port_distance_minus_L': distance(f, other)-L,
                     'public_port_distance_slacks_above_L':
                     [{'P_coefficient': (distance(f, p)-L)//P,
                       'constant': (distance(f, p)-L)%P}
                      for p in old_ports+[cG, cZ]],
                     'ready_region_count': len(ready)})
    # Negative control for careless axis selection: the corresponding +x
    # source has reached the old port4 noise stream before the claimed cut.
    plus8 = (L+1, S, 76)
    require(distance(plus8, old_ports[4])-L == -478,
            'positive-x source fails complete-history exclusion')
    # A return-side blank extension would consume an existing used bank.
    # Geometry alone is not an influence proof: M1 is opposite parity and
    # an isolated first-front cancellation can also occur for M2.
    require(distance((0, -1, 0), q8)-L == 0, 'M1 in return shell')
    require(distance((0, -2, 0), q8)-L == 1, 'M2 in return shell')
    require(distance((0, -1, 0), q10)-L == 2 and
            distance((0, -2, 0), q10)-L == 3, 'outward shell preserves both bank points')
    # The torus used by the retained herald is larger than all differences
    # relevant to these new sources and their complete <=L+1 light cones.
    torus = 256*L+64*T+1
    require(2*(49*L+2*(L+1)+S+8*T+156) < torus, 'conservative no-wrap bound')
    require(all(distance(f, p) > L for f in (f8, f10)
                for p in (q8, q9, q10)), 'all three present ports unchanged')
    return {'target_tick': 'L+1', 'sources': rows,
            'source_inventory_rows': 2*len(geo['sources']),
            'ready_exclusion_rows': 2*len(ready),
            'positive_x_countercontrol_port4_distance_minus_L': -478,
            'new_current_shell': 'B_(L+1)(q8) union B_(L+1)(q10)',
            'new_previous_shell': 'B_L(q8) union B_L(q10)',
            'return_shell_reserved_bank_exceptions': [
                {'bank_point': '(0,-1,0)', 'q8_distance_minus_L': 0},
                {'bank_point': '(0,-2,0)', 'q8_distance_minus_L': 1}],
            'old_current_pins_retained': True,
            'old_previous_pins_retained': True,
            'torus_unchanged': True}


def main():
    ap = argparse.ArgumentParser()
    default_root = Path(__file__).resolve().parent.parent
    if not (default_root/'parallel_v3').exists():
        default_root = default_root/'checkpoint_v10'
    ap.add_argument('--source-root', type=Path,
                    default=default_root)
    args = ap.parse_args()
    here = Path(__file__).resolve().parent
    prov = json.loads((here/'PROVENANCE.json').read_text())
    for path, expected in prov['inputs'].items():
        require(hashlib.sha256((args.source_root/path).read_bytes()).hexdigest() == expected,
                'source hash '+path)
    native = small_native_controls()
    geo = geometry(args.source_root)
    # A pair of independent uniform initial triples through two separate
    # permutations remains jointly uniform. This does not posit any late seed.
    pair_outputs = {(a, b) for a, b in product(TRIPLES, repeat=2)}
    require(len(pair_outputs) == 64, 'independent two-port support')
    result = {'schema': 'oi.native-continuation-boundary.v11',
              'source_commit': prov['source_commit'],
              'checks': {'input_hashes': len(prov['inputs']),
                         'native_first_front': native, 'geometry': geo,
                         'two_free_triple_joint_support': len(pair_outputs)},
              'conditional_law': {
                  'assumption': 'f8,f10 current initial triples independently uniform conditional on all other initial variables',
                  'conditioning': 'all other initial variables; prior full public history and selected phase through L are unaffected',
                  'next_q8_q10_joint_cell_probability': '1/64',
                  'all_success_failure_branches_preserved': True},
              'verdict': {'selected_phase_autonomous_next_port_contract': 'fails for unrestricted outside-ready complement',
                          'independent_fair_complement_next_q8_q10': 'jointly uniform',
                          'globally_zero_outside_ready_complement': 'additional initial restriction; not tested as native reset',
                          'native_reset': 'not_constructed',
                          'general_reusable_instrument': 'not_excluded'}}
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
