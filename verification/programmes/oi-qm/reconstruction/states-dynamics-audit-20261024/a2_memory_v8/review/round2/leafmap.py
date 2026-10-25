"""Reviewer leaf mapping between result.json at 200fcd9f (old) and fb05dea8 (new).

Usage: python3 -I -B leafmap.py <old result.json> <new result.json>
Own mapping rules for moved keys; every old leaf must map to an identical new value, else it is listed as changed.
"""
import json
import re
import sys


def leaves(x, p=()):
    if isinstance(x, dict):
        if not x:
            yield p, {}
        for k, v in x.items():
            yield from leaves(v, p + (k,))
    elif isinstance(x, list):
        if not x:
            yield p, []
        for i, v in enumerate(x):
            yield from leaves(v, p + (i,))
    else:
        yield p, x


MOVED_POST = {'power_rule_T_above_half_for_h_at_least', 'power_rule_T_at_most_half_for_h_at_most',
              'quantum_mass_of_source_null_records', 'mass_of_records_ending_in_r_disagreements'}
RENAME = {'certified_fails_before_memoryless_reset': 'certified_fails_before_ceiling_rounded_reset',
          'certified_outlasts_memoryless_reset': 'certified_outlasts_ceiling_rounded_reset'}


def mapped(p):
    if len(p) >= 3 and p[0] == 'family_RS':
        m = re.fullmatch(r'B(\d)_memoryless_reset', p[1])
        if m:
            return ('family_RS', f'B{m.group(1)}_memoryless_comparators_post_plan', 'ceiling_rounded_reset_RS_B_1') + p[2:]
        if p[2] in MOVED_POST:
            return p[:2] + ('post_plan',) + p[2:]
        if p[2] in RENAME:
            return p[:2] + ('post_plan', RENAME[p[2]]) + p[3:]
    return p


def main():
    old = json.load(open(sys.argv[1]))
    new = json.load(open(sys.argv[2]))
    O = dict(leaves(old))
    N = dict(leaves(new))
    same, moved_same, changed, missing = 0, 0, [], []
    hit = set()
    for p, v in O.items():
        q = mapped(p)
        if q in N:
            hit.add(q)
            if N[q] == v:
                if q == p:
                    same += 1
                else:
                    moved_same += 1
            else:
                changed.append((p, q))
        else:
            missing.append(p)
    added = [q for q in N if q not in hit]
    print('old leaves', len(O), 'new leaves', len(N))
    print('unchanged in place', same, 'moved and identical', moved_same, 'changed', len(changed),
          'unmapped old', len(missing), 'new-only', len(added))
    for p, q in changed:
        a, b = str(O[p]), str(N[q])
        print('CHANGED', '/'.join(map(str, p)), '|', a[:90], '->', b[:90])
    for p in missing:
        print('UNMAPPED', '/'.join(map(str, p)))
    kinds = {}
    for q in added:
        key = '/'.join(str(x) for x in q if not re.fullmatch(r'B\d_k\d+|\d+|B\d_m\d|B\d', str(x)))
        kinds[key] = kinds.get(key, 0) + 1
    for k in sorted(kinds):
        print('ADDED', kinds[k], k)


if __name__ == '__main__':
    main()
