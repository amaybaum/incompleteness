#!/usr/bin/env python3
"""Exact controls for a naive pure-gradient U(1) link extraction from the
existing 3-D finite mod-q wave rule. Rejects only THIS LINK DEFINITION.
Not a no-go for H-link, OI gauge fields, or other native extensions.
"""
import json

L = 3
Q = 5
SITES = tuple((x, y, z) for x in range(L) for y in range(L) for z in range(L))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(a, b):
    return tuple((a[i] + b[i]) % L for i in range(3))


def neg(a):
    return tuple((-a[i]) % L for i in range(3))


def make(seed):
    return {p: (seed + 2*p[0] + 3*p[1] + p[2]**2) % Q for p in SITES}


def wave(cur, prev):
    return {p: (sum(cur[add(p, d)] + cur[add(p, neg(d))]
                    for d in AXES) - prev[p]) % Q for p in SITES}


def step(cur, prev):
    return wave(cur, prev), cur.copy()


def inv(nxt, cur):
    return cur.copy(), wave(cur, nxt)


def edge(cur, p, d):
    return (cur[add(p, d)] - cur[p]) % Q


def plaquette(cur, p, d, e):
    return (edge(cur, p, d) + edge(cur, add(p, d), e)
            - edge(cur, add(p, e), d) - edge(cur, p, e)) % Q


def main():
    fields = [{p: 0 for p in SITES}, make(0), make(2),
              {p: (p[0]*p[1] + 2*p[1]*p[2] + p[0]**2) % Q for p in SITES}]
    checks = {}
    checks['inverse_both_directions'] = all(
        inv(*step(a, b)) == (a, b) and step(*inv(a, b)) == (a, b)
        for a in fields for b in fields)
    checks['closed_plaquettes_are_flat'] = all(
        plaquette(cur, p, d, e) == 0 for cur in fields
        for p in SITES for i, d in enumerate(AXES) for e in AXES[i+1:])
    checks['evolved_plaquettes_still_flat'] = all(
        plaquette(wave(a, b), p, d, e) == 0 for a in fields for b in fields
        for p in SITES for i, d in enumerate(AXES) for e in AXES[i+1:])
    checks['nontrivial_open_link_countercontrol'] = any(
        edge(x, p, d) != 0 for x in fields for p in SITES for d in AXES)

    delta = {p: int(p == (0, 0, 0)) for p in SITES}
    zero = fields[0]
    shifted_cur = {p: (zero[p] + delta[p]) % Q for p in SITES}
    shifted_prev = shifted_cur.copy()
    lhs = step(shifted_cur, shifted_prev)[0]
    rhs = {p: (step(zero, zero)[0][p] + delta[p]) % Q for p in SITES}
    checks['native_update_not_covariant_under_local_site_shift'] = lhs != rhs
    checks['specific_source_site_witness'] = (
        lhs[(0, 0, 0)], rhs[(0, 0, 0)]) == (Q-1, 1)

    if not all(checks.values()):
        raise AssertionError({k: v for k, v in checks.items() if not v})
    print(json.dumps({
        'verdict': 'PASS_NARROW_NATIVE_GRADIENT_NO_GO',
        'native_rule': 'f_next = sum six nearest present neighbors - prior slice mod q',
        'L': L, 'q': Q, 'test_field_count': len(fields),
        'controls': checks,
        'local_shift_witness': {'native_next_origin': lhs[(0, 0, 0)],
                                'required_covariant_origin': rhs[(0, 0, 0)]},
        'mathematical_scope': 'Pure-gradient links flat for every field and time; arbitrary local site shifts do not commute with the tested native update',
        'H_link_other_constructions_ruled_out': False,
        'YM_action_derived': False
    }, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
