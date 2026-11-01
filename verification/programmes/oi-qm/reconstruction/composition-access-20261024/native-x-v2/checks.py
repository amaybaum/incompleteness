#!/usr/bin/env python3
"""Exact finite-kernel audit of retained native-X source fragments."""
import ast
from collections import defaultdict
from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def load_source():
    src = json.loads((ROOT / 'SOURCE-EXCERPTS.json').read_text())
    env = {}
    for item in src['candidate.py']['fragments']:
        tree = ast.parse(item['text'])
        need(len(tree.body) == 1 and isinstance(tree.body[0], ast.FunctionDef),
             'retained candidate function')
        exec(compile(tree, '<retained-native-source>', 'exec'), env)
    for item in src['checks.py']['fragments']:
        node = ast.parse(item['text']).body[0]
        need(isinstance(node, ast.Assign) and len(node.targets) == 1,
             'retained calibration literal')
        env[node.targets[0].id] = ast.literal_eval(node.value)
    return env


def tv(p, q):
    return sum((abs(p.get(k, 0) - q.get(k, 0)) for k in p.keys() | q.keys()), F(0))/2


def marginal(p, f):
    d = defaultdict(F)
    for k, v in p.items():
        d[f(k)] += v
    return dict(d)


def bloch(mu):
    # Unnormalized coordinates: trace, X, Y, Z.
    return (sum(mu.values(), F(0)),) + tuple(
        sum((w * (1-2*j[i]) for j, w in mu.items()), F(0)) for i in (0, 1, 3))


def report():
    src = load_source()
    accept, output, pulse = (src[k] for k in ('accept', 'output', 'pulse'))
    T = 185
    P = 12 * 840**T
    S, d = T + P, 68
    need((S+d) % 12 == 1 and S & d == 0, 'actual source phase')
    for x in range(2):
        for u in range(2):
            a, b, c = pulse(S, d, u)
            b ^= x
            native = (b, c, a ^ (b & c))
            need(native == output(S, x, u), 'independent collision algebra')
    planes, weights, indices = (src[k] for k in ('planes', 'weights', 'indices'))
    preps = {}
    for axis, index in indices.items():
        for sign in range(2):
            preps[axis, sign] = {(*p, z): F(1, 6) if axis == 'Z' else F(weights[axis][i], 20)
                                for i, p in enumerate(planes) for z in range(2)
                                if (*p, z)[index] == sign}
    reference_axes = {'X': (F(1), F(0), F(0)), 'Y': (F(0), F(1), F(0)),
                      'R': (F(4, 5), F(3, 5), F(0)), 'Z': (F(0), F(0), F(1))}
    for (axis, sign), mu in preps.items():
        need(bloch(mu) == (F(1),) + tuple((1-2*sign)*v for v in reference_axes[axis]),
             'fixed decoder on supplied preparation')
    success_branches = failure_branches = 0
    for label, prep in preps.items():
        actual = defaultdict(F)
        for j, w in prep.items():
            x, y, r, oldz = j
            for pads in range(8):
                public = (x, y ^ (pads & 1), r ^ ((pads >> 1) & 1), oldz ^ (pads >> 2))
                for seed in range(64):
                    u, v, k, z = seed & 1, (seed >> 1) & 1, (seed >> 2) & 7, seed >> 5
                    g = int(accept(u, v, k))
                    raw_y, raw_r, raw_z = output(S, x, u), output(S, x, v), (0, 0, z)
                    need(raw_y[0] == raw_r[0] == x and raw_y[1] == raw_r[1] == 1,
                         'fixed raw encoding')
                    offered = (raw_y[0], raw_y[2], raw_r[2], raw_z[2]) if g else None
                    actual[public, g, offered] += w / 512
        need(sum(actual.values()) == 1, 'all branches normalized')
        axis, sign = label
        quantum_x_mean = (1-2*sign) * reference_axes[axis][0]
        for x in range(2):
            read_mass = (1 + (1-2*x) * quantum_x_mean)/2
            for pads in range(8):
                public = (x, pads & 1, (pads >> 1) & 1, pads >> 2)
                carrier = {j: w for (rec, g, j), w in actual.items() if rec == public and g == 1}
                scale = F(5, 128) * read_mass
                # P_x rho P_x has Bloch coordinates (read, +/-read,0,0).
                need(bloch(carrier) == (scale, (1-2*x)*scale, 0, 0),
                     'success branch quantum intertwining')
                target = {j: scale*w for j, w in preps['X', x].items()}
                need(tv(carrier, target) == 0, 'stronger full offered-carrier kernel')
                need(actual.get((public, 0, None), F(0)) == F(11, 128)*read_mass,
                     'terminal failure record with no-carrier')
                success_branches += 1
                failure_branches += 1
    fail_counts = defaultdict(int)
    for u in range(2):
        for v in range(2):
            for k in range(8):
                if not accept(u, v, k):
                    fail_counts[u, v] += 1
    need(dict(fail_counts) == {(0, 0): 3, (0, 1): 8, (1, 0): 4, (1, 1): 7},
         'hidden physical failure field distribution retained')

    # Explicit proposed non-native extension: expose raw X port's Y metadata,
    # then reuse the same sample for a decoded Y read without reset.
    extensions = []
    for x in range(2):
        mu = preps['X', x]
        for y_metadata in range(2):
            posterior = {j: 2*w for j, w in mu.items() if j[1] == y_metadata}
            t, bx, by, bz = bloch(posterior)
            determinant = (t*t - bx*bx - by*by - bz*bz)/4
            need((t, bx, by, bz) == (1, 1-2*x, 1-2*y_metadata, 0),
                 'conditional unchanged carrier decoder')
            need(determinant == F(-1, 4),
                 'unchanged-carrier decoder leaves positive cone')
        unchanged = marginal(mu, lambda j: (j[1], j[1]))
        fresh = defaultdict(F)
        for j, w in mu.items():
            for jp, wp in mu.items():
                fresh[j[1], jp[1]] += w*wp
        need(marginal(unchanged, lambda rs: rs[0]) == marginal(fresh, lambda rs: rs[0]),
             'first terminal metadata marginal')
        need(marginal(unchanged, lambda rs: rs[1]) == marginal(fresh, lambda rs: rs[1]),
             'second Y marginal')
        need(tv(unchanged, dict(fresh)) == F(1, 2), 'no-reset extension joint failure')
        # Same fresh sample logic but explicit independent fair metadata bit.
        control = {(a, b): F(1, 4) for a in range(2) for b in range(2)}
        need(dict(fresh) == control, 'fresh reset positive control')
        extensions.append({'x': x, 'conditional_success_tv': '1/2',
                           'including_same_terminal_failure_tv': '5/32',
                           'posterior_decoder_determinant': '-1/4'})
    good_weights = {(0, 0): F(5, 10), (1, 0): F(4, 10), (1, 1): F(1, 10)}
    bad_weights = {(0, 0): F(4, 10), (1, 0): F(5, 10), (1, 1): F(1, 10)}
    need(tv(good_weights, bad_weights) == F(1, 10), 'swapped herald weights rejected')
    a, b, c = pulse(S, d, 0)
    c = 0
    b ^= 1
    wrong_raw = (b, c, a ^ (b & c))
    need(wrong_raw != output(S, 1, 0), 'removed collision constant rejected')
    return {
        'schema': 'oi-native-x-contract-audit-v1',
        'scope': 'exact native-source finite kernel and conditional proof application; not a new lattice transport proof',
        'preparation_cone_generators': len(preps),
        'success_intertwining_branches': success_branches,
        'terminal_failure_record_branches': failure_branches,
        'success_mass': '5/16', 'terminal_failure_mass': '11/16',
        'physical_failure_uv_counts': {'00': 3, '01': 8, '10': 4, '11': 7},
        'proposed_unchanged_sample_extension': extensions,
        'swapped_herald_count_control_tv': '1/10',
        'missing_constant_collision_control_detected': True,
        'full_public_noise_independence': 'INHERITED_NOT_REPROVED',
        'native_next_stage_boundary_closure': 'NOT_SUPPLIED',
        'post_failure_qubit_carrier_law': 'NOT_SUPPLIED',
        'controls_passed': True,
        'verdict': 'CONDITIONAL_ONE_STAGE_SUCCESS_CONTRACT; TERMINAL_FAILURE_ACCOUNTED; REUSABLE_CLOSURE_OPEN'
    }


if __name__ == '__main__':
    encoded = json.dumps(report(), indent=2, sort_keys=True) + '\n'
    target = ROOT / 'RESULT.json'
    if target.exists():
        need(target.read_text() == encoded, 'retained result mismatch')
    else:
        target.write_text(encoded)
    print(encoded, end='')
