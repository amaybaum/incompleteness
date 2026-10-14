"""Separate exact diagnostic: directed gaps force the target relabelling."""
from itertools import permutations
from pathlib import Path
import json
import re

directory = Path(__file__).resolve().parents[5] / 'verification/lean-mathlib/OIBridge'
text = (directory / 'HomometricSix.lean').read_text()
blocks = re.split(r'\ndef (r1|r2|mu|muInv)\s*:', text)
objects = {blocks[i]: blocks[i+1] for i in range(1, len(blocks), 2)}


def parse_marks(name):
    found = {}
    for match in re.finditer(r'\| ([0-5]) => (-?[0-9]+)', objects[name]):
        found[int(match[1])] = int(match[2])
    assert sorted(found) == list(range(6))
    return [found[i] for i in range(6)]


first, second = parse_marks('r1'), parse_marks('r2')
edges = []
for match in re.finditer(r'\| ([0-5]), ([0-5]) => \(([0-5]),([0-5])\)', objects['mu']):
    edges.append(tuple(map(int, match.groups())))
assert len(edges) == 15


def reversed_marks(values):
    return [max(values)-values[5-i] for i in range(6)]


def permitted(values, other):
    distances = [{values[b]-values[a] for a in range(6) for b in range(a+1, 6)},
                 {other[b]-other[a] for a in range(6) for b in range(a+1, 6)}]
    return (all(values[a] < values[a+1] and other[a] < other[a+1] for a in range(5))
            and len(distances[0]) == len(distances[1]) == 15 and distances[0] == distances[1]
            and any(other[i]-values[i] != other[0]-values[0] for i in range(1, 6))
            and any(other[i]+values[5-i] != other[0]+values[5] for i in range(1, 6)))


def forced_counts(values, other, correspondence):
    target_by_gap = {other[j]-other[i]: (i, j)
                     for i in range(6) for j in range(6) if i != j}
    assert len(target_by_gap) == 30
    total = [0, 0]
    for s in permutations(range(6)):
        for slot, sign in enumerate((1, -1)):
            assignment = {}
            for a, b, c, d in correspondence:
                target_pair = target_by_gap.get(sign*(values[s[b]]-values[s[a]]))
                if target_pair is None:
                    break
                conflict = False
                for target_label, native_label in zip((c, d), target_pair):
                    if target_label in assignment and assignment[target_label] != native_label:
                        conflict = True
                        break
                    assignment[target_label] = native_label
                if conflict:
                    break
            else:
                assert len(assignment) == 6 and len(set(assignment.values())) == 6
                total[slot] += 1
    return total


rows = []
for swapped in (False, True):
    for source_reflected in (False, True):
        for target_reflected in (False, True):
            values, other = (second, first) if swapped else (first, second)
            values = reversed_marks(values) if source_reflected else values
            other = reversed_marks(other) if target_reflected else other
            assert permitted(values, other)
            count = forced_counts(values, other, edges)
            assert count == ([0, 3] if source_reflected != target_reflected else [3, 0])
            rows.append({'swapped': swapped, 'source_reflected': source_reflected,
                         'target_reflected': target_reflected, 'counts': count})
assert not permitted(first, [x+3 for x in first])
assert not permitted(first, reversed_marks(first))
corrupted = list(edges)
lookup = {(a, b): index for index, (a, b, _, _) in enumerate(corrupted)}
i, j = lookup[0, 2], lookup[0, 3]
a, b, c, d = corrupted[i]
e, f, g, h = corrupted[j]
corrupted[i], corrupted[j] = (a, b, g, h), (e, f, c, d)
assert forced_counts(first, second, corrupted) == [0, 0]
print(json.dumps({'orientation_table': rows, 'countercontrols_rejected': 3,
                  'scope': 'separate exact directed-gap implementation; no classification theorem'},
                 indent=2, sort_keys=True))
