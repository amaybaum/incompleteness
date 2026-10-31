#!/usr/bin/env python3
"""Bounded native previous-shell apparatus test; no late write is authorized."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path


def need(ok, why):
    if not ok:
        raise RuntimeError(why)


D = tuple(tuple(s if j == a else 0 for j in range(3))
          for a in range(3) for s in (-1, 1))
Z = (0, 0, 0)
BALL = (Z,) + D


def add(a, b): return tuple(x+y for x, y in zip(a, b))
def scale(n, v): return tuple(n*x for x in v)
def dist(a, b): return sum(abs(x-y) for x, y in zip(a, b))


def xor(values):
    out = 0
    for v in values:
        out ^= v
    return out


def h(v):
    a, b, d = v >> 2, (v >> 1) & 1, v & 1
    return 4*b + 2*d + (a ^ (b & d))


def world(seed, register, payload):
    cache = {}

    def value(t, v):
        if (t, v) not in cache:
            x, y, z = v
            if t == 0:
                out = (x*y + 3*z + 5*seed + y) % 8
            elif t == -1:
                out = (y*z + 5*x + 3*seed + z) % 8
                if v == register:
                    out ^= payload
            elif t > 0:
                out = value(t-2, v) ^ h(xor(value(t-1, add(v, d)) for d in D))
            else:
                out = value(t+2, v) ^ h(xor(value(t+1, add(v, d)) for d in D))
            cache[t, v] = out
        return cache[t, v]
    return value


def packet(v, t):
    return tuple(v(u, p) for u in (t, t-1) for p in BALL)


def run(root):
    raw = (root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_bytes()
    need(hashlib.sha256(raw).hexdigest() ==
         '2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d',
         'original source inventory pin')
    sources = {tuple(s['position']) for s in json.loads(raw)['sources']}
    need(len(sources) == 1479, 'original source inventory size')
    need([h(v) for v in range(8)] == [0, 2, 4, 7, 1, 3, 5, 6], 'native rule')
    need(len({h(v) for v in range(8)}) == 8, 'native h is bijective')
    need(all(h(v ^ 4) ^ h(v) == 1 for v in range(8)), 'clean A-to-D response')
    T = 185
    P = 12*840**185
    S = P+T
    L = S+77
    tau = L+3
    q = (0, S, 78)
    extra = {(0, -78, 78), (0, S, S+156), (4*T, P+S, 0), (0, S, -S-136)}
    ports = [(0, T, 0), (0, 0, -8*T), (T, P, 0), (-T, P, 0),
             (4*T, P, 0), (0, S, 0), (12*(S+68), 0, 0), (48*L, 0, 0)]
    banks = [(0, -1, 0), (0, 0, -1), (0, 1, 0), (0, 1, 0),
             (0, 1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]
    need(all(dist(s, q) >= L+1 for s in sources), 'inherited q10 source exclusions')
    geometry = []
    for direction in D:
        register = add(q, scale(2, direction))
        witness = add(register, scale(-(tau-1), direction))
        need(witness == add(q, scale(-L, direction)), 'backward axial first arrival')
        need(dist(witness, q) == L and dist(witness, q) < L+1,
             'forced original change is strictly inside q10 readiness')
        need(witness not in sources | extra, 'forced cell is no source exception')
        for port, axis in zip(ports, banks):
            j = next(i for i, a in enumerate(axis) if a)
            need(any(witness[i] != port[i] for i in range(3) if i != j),
                 'forced cell is outside every public bank line')
        side = 256*L+64*T+1
        need(2*(tau+2) < side, 'no torus wrap on the tested axial front')
        geometry.append({'direction': direction, 'ready_margin': -1,
                         'source_exception': False})
    # Full native recursion on dirty two-slice worlds, not a hand-coded packet flip.
    patch = [p for p in itertools.product(range(-4, 5), repeat=3) if dist(p, Z) <= 4]
    forward_worlds = backward_worlds = 0
    for direction in D:
        register = scale(2, direction)
        for seed in range(3):
            left, right = world(seed, register, 0), world(seed, register, 4)
            need(packet(left, 0) == packet(right, 0), 'same complete incoming 42 bits')
            need(packet(left, 1) == packet(right, 1), 'same first outgoing packet')
            expected = list(packet(left, 2))
            expected[1+D.index(direction)] ^= 1
            need(packet(right, 2) == tuple(expected), 'second outgoing packet has one D flip')
            for v in (left, right):
                for t, p in itertools.product((0, -1), BALL + (register,)):
                    need(v(t, p) == v(t-2, p) ^ h(xor(v(t-1, add(p, d)) for d in D)),
                         'backward reconstructed fields obey the forward native rule')
            for p in patch:
                need(left(1, p) ^ right(1, p) == (4 if p == register else 0),
                     'complete first-step support')
                need(left(2, p) ^ right(2, p) == (1 if dist(p, register) == 1 else 0),
                     'complete second-step support; all residual neighbors retained')
            forward_worlds += 2
        for seed, depth in itertools.product(range(2), (4, 5, 6)):
            witness = add(register, scale(-(depth-1), direction))
            values = [world(seed, register, v)(-depth, witness) for v in range(8)]
            need(sorted(values) == list(range(8)), 'backward first-arrival permutation')
            need(all(values[v] != values[v ^ 4] for v in range(8)),
                 'clean program pair necessarily changes forced original cell')
            backward_worlds += 8
    # Independently index the full finite periodic update to check backward
    # recursion against forward evolution from its reconstructed two slices.
    sites = list(itertools.product(range(5), repeat=3))
    neighbors = {v: [tuple((v[j]+d[j]) % 5 for j in range(3)) for d in D]
                 for v in sites}
    roundtrips = 0
    for seed in range(3):
        now = {v: (v[0]*v[1]+v[2]+seed) % 8 for v in sites}
        old = {v: (v[1]*v[2]+3*v[0]+seed) % 8 for v in sites}
        original = now, old
        for _ in range(3):
            now, old = old, {v: now[v] ^ h(xor(old[w] for w in neighbors[v])) for v in sites}
        for _ in range(3):
            now, old = {v: old[v] ^ h(xor(now[w] for w in neighbors[v])) for v in sites}, now
        need((now, old) == original, 'native two-slice inverse roundtrip')
        roundtrips += 1
    # Exact native h with all eight dirty summed-neighbor values. Fair packet
    # marginals do not make the two joint output/mask actions identical.
    marginals = [Counter(), Counter()]
    joints = [Counter(), Counter()]
    for setting, p, sigma in itertools.product(range(2), range(8), range(8)):
        out = p ^ h(sigma ^ (4*setting))
        marginals[setting][out] += 1
        joints[setting][(p, sigma, out)] += 1
    need(marginals[0] == marginals[1] == Counter({v: 8 for v in range(8)}),
         'uniform raw output does not identify a setting')
    support = set(joints[0]) | set(joints[1])
    tv = sum(abs(Fraction(joints[0][x], 64)-Fraction(joints[1][x], 64))
             for x in support)/2
    need(tv == 1, 'joint native countercontrol retains the dirty mask')
    # Physical access/terminal guard: the private register is never a new read.
    def offered(terminal, v):
        if terminal:
            return None, None
        return (), packet(v, 2)  # No new local public read; full private packet.
    class Forbidden:
        def __call__(self, *args):
            raise RuntimeError('terminal branch attempted an internal field read')
    need(offered(True, Forbidden()) == (None, None), 'terminal no-read/no-offer')
    need(offered(False, world(0, (0, 2, 0), 0))[0] == (), 'no private register read granted')
    need(forward_worlds == 36 and backward_worlds == 288 and len(geometry) == 6,
         'nonvacuous controls')
    return {'status': 'PASS', 'verdict': 'CLEAN_REGISTER_PAIR_VIOLATES_PREPARATION',
            'incoming_packet_bits': 42, 'native_forward_worlds': forward_worlds,
            'native_backward_worlds': backward_worlds, 'directions_checked': 6,
            'periodic_inverse_roundtrips': roundtrips,
            'outgoing_packet_D_flips': 1, 'outgoing_current_environment_D_flips': 5,
            'outgoing_previous_environment_A_flips': 1,
            'local_countercontrol_joint_TV': str(tv), 'local_countercontrol_marginal_TV': '0',
            'new_sources': 0, 'new_reads': 0, 'new_resets': 0,
            'selectable_native_apparatus': 'NOT_ESTABLISHED', 'geometry': geometry}


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
