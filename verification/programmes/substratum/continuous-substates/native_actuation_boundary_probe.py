#!/usr/bin/env python3
"""Exact local-rule diagnostics; not a native actuator or later-cut replay."""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path

TABLE_PIN = 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc'
OLD_PIN = 'dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf'


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def fields(c):
    return c >> 2, (c >> 1) & 1, c & 1


def h(c):
    a, b, d = fields(c)
    return 4*b + 2*d + (a ^ (b & d))


def step(old, sigma):
    return old ^ h(sigma)


def pullback_controls():
    """Small whole-native-world check of a fixed transported phase coordinate."""
    sites = tuple(itertools.product(range(5), repeat=3))
    origin, q8, q10 = (0, 0, 0), (0, 0, 4), (0, 0, 1)
    def neighbors(v):
        for axis in range(3):
            for delta in (-1, 1):
                w = list(v)
                w[axis] = (w[axis] + delta) % 5
                yield tuple(w)
    def kick(field):
        result = {}
        for v in sites:
            sigma = 0
            for w in neighbors(v):
                sigma ^= field[w]
            result[v] = h(sigma)
        return result
    def advance(cut):
        current, previous = cut
        noise = kick(current)
        return ({v: previous[v] ^ noise[v] for v in sites}, current)
    def inverse(cut):
        current, previous = cut
        noise = kick(previous)
        return (previous, {v: current[v] ^ noise[v] for v in sites})
    def phase(cut):
        current, previous = cut
        sigma = 0
        for w in neighbors(origin):
            sigma ^= previous[w]
        return current[origin] ^ h(sigma), previous[q8], previous[q10]
    count = 0
    changed_by_omission = 0
    for seed in range(7):
        original = ({v: (v[0]*v[1] + 3*v[2] + seed + v[0]*seed) % 8 for v in sites},
                    {v: (v[1]*v[2] + 5*v[0] + 3*seed + v[2]*seed) % 8 for v in sites})
        cut1 = advance(original)
        target = original[0][origin], cut1[0][q8], cut1[0][q10]
        cut = advance(cut1)
        changed_by_omission += phase(cut)[0] != cut[0][origin]
        for horizon in range(2, 7):
            recovered = cut
            for _ in range(horizon - 2):
                recovered = inverse(recovered)
            need(phase(recovered) == target, 'fixed transported raw phase')
            need(inverse(advance(cut)) == cut, 'complete native two-slice inverse')
            count += 1
            cut = advance(cut)
    need(changed_by_omission > 0, 'nonvacuous seven-site inverse control')
    return count


def index(values, sizes):
    i = 0
    for v, size in zip(values, sizes):
        i = size*i + v
    return i


def phase_pair(k, route, old):
    u, my, mr, a, b = k
    need((a, b) != (0, 1), 'terminal mask has no attempted phase analysis')
    e, n = 4 + 2*(1 ^ my) + 1, 4*my + 2 + (1 ^ my)
    pairs = []
    for s in (0, 1):
        x = s ^ u ^ a
        prefix = (x, u, my, mr, a, b)
        q = int(route[index(prefix + (e, n), (2,)*6 + (8, 8))], 16)
        p = int(old[index(prefix + (4, 5, 7), (2,)*6 + (8,)*3)], 16)
        need(q >> 2 == s, 'actual q10 A field is s')
        need(p == 2*s + (s ^ a ^ b), 'actual old q9 fields')
        pairs.append((p, q))
    return pairs


def run(root):
    route_data = json.loads((root/'native_route_v13/result.json').read_text())
    old_data = json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())
    route, old = route_data['q10_table_hex'], old_data['q9_table_hex']
    need(len(route) == 4096 and len(old) == 32768, 'input table sizes')
    need(route_data['table_order'].startswith('x,u,mY,mR,a,b,Ecode,Ncode'), 'input table order')
    need(hashlib.sha256(route.encode()).hexdigest() == TABLE_PIN, 'native q10 table pin')
    need(hashlib.sha256(old.encode()).hexdigest() == OLD_PIN, 'native old-q9 table pin')
    need(set(route + old) <= set('01234567'), 'raw triple alphabet')
    pullback_worlds = pullback_controls()

    # Independently invert the complete three-bit map.
    need(len({h(c) for c in range(8)}) == 8, 'native H permutation')
    for c in range(8):
        a, b, d = fields(h(c))
        need(4*(d ^ (a & b)) + 2*a + b == c, 'H inverse')

    translation_rows = 0
    for p, sigma, s in itertools.product(range(8), range(8), range(2)):
        a, b, d = fields(sigma)
        baseline = step(p, sigma)
        need(step(p, sigma ^ (4*s)) ^ baseline == s, 'A input: clean D translation')
        need(step(p, sigma ^ (2*s)) ^ baseline == 4*s + s*d, 'B input: residual D dependence')
        need(step(p, sigma ^ s) ^ baseline == 2*s + s*b, 'D input: residual B dependence')
        # The full old-local term is retained, including nonzero A on failures.
        need(step(p ^ s, sigma) ^ baseline == s, 'old-local contribution')
        translation_rows += 1

    counts = Counter()
    background_rows = 0
    terminal_patterns = 0
    for k in itertools.product(range(2), repeat=5):
        if k[3:] == (0, 1):
            # Deliberate invalid continuation must be rejected before a table read.
            class NoRead:
                def __getitem__(self, key):
                    raise AssertionError('attempted terminal table read')
            try:
                phase_pair(k, NoRead(), NoRead())
            except RuntimeError as exc:
                need(str(exc) == 'terminal mask has no attempted phase analysis', 'terminal rejection reason')
            else:
                raise RuntimeError('terminal phase accepted')
            terminal_patterns += 1
            continue
        (p0, q0), (p1, q1) = phase_pair(k, route, old)
        # Formal local-coordinate comparison: hold the other five-neighbor XOR
        # eta equal. This is NOT the physical counterfactual eta_0 vs eta_1.
        deltas = {step(p0, q0 ^ eta) ^ step(p1, q1 ^ eta) for eta in range(8)}
        counts[(q0 ^ q1, tuple(sorted(deltas)))] += 1
        background_rows += 8
        for eta in range(8):
            b0, d0 = fields(q0 ^ eta)[1:]
            b1, d1 = fields(q1 ^ eta)[1:]
            need((step(p0, q0 ^ eta) ^ step(p1, q1 ^ eta)) & 1
                 == (b0 & d0) ^ (b1 & d1), 'actual old-D/sign-A cancellation')

    need(terminal_patterns == 8 and background_rows == 192, 'nonvacuous branch coverage')
    need(sum(counts.values()) == 24, 'accepted context coverage')
    # Decision computed from actual rows, without fixing the expected histogram.
    dirty = sum(n for (dq, ds), n in counts.items() if dq & 3)
    clean = sum(n for (dq, ds), n in counts.items() if not (dq & 3))
    return {
        'status': 'PASS',
        'scope': 'local algebra and retained L+1 phase table; no H-cut actuator or reuse certification',
        'translation_control_rows': translation_rows,
        'small_world_transported_phase_controls': pullback_worlds,
        'accepted_contexts': sum(counts.values()),
        'terminal_patterns_rejected_before_read': terminal_patterns,
        'formal_background_rows': background_rows,
        'pure_A_input_difference_contexts': clean,
        'residual_B_or_D_difference_contexts': dirty,
        'formal_delta_histogram': [
            {'q10_xor': dq, 'output_xors': list(ds), 'contexts': n}
            for (dq, ds), n in sorted(counts.items())],
        'two_setting_instrument': 'NOT_SUPPLIED',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    default = Path(__file__).resolve().parents[2]/'oi-qm/reconstruction/native-y-continuation-20261024'
    parser.add_argument('--source-root', type=Path, default=default)
    args = parser.parse_args()
    try:
        result = run(args.source_root)
    except (RuntimeError, ValueError, KeyError, OSError) as exc:
        print(json.dumps({'status': 'VOID', 'reason': str(exc)}, sort_keys=True))
        raise SystemExit(2)
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))
