"""Exact diagnostic using complete gap fingerprints of all permutation pairs."""
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[5]
source = (root / 'verification/lean-mathlib/OIBridge/HomometricSix.lean').read_text()


def ruler(name, following):
    body = source.split('def ' + name + ' :', 1)[1].split('def ' + following + ' :', 1)[0]
    values = re.findall(r'\|\s*(\d)\s*=>\s*(-?\d+)', body)
    assert [int(i) for i, _ in values] == list(range(6))
    return tuple(int(v) for _, v in values)


r1, r2 = ruler('r1', 'r2'), ruler('r2', 'mu')
mu_body = source.split('def mu :', 1)[1].split('def muInv :', 1)[0]
mu = {(int(a), int(b)): (int(c), int(d)) for a, b, c, d in
      re.findall(r'\|\s*(\d)\s*,\s*(\d)\s*=>\s*\((\d)\s*,\s*(\d)\)', mu_body)}
pairs = tuple(combinations(range(6), 2))
perms = tuple(permutations(range(6)))
assert len(perms) == 720 and set(mu) == set(pairs)
assert all(r2[mu[a, b][1]] - r2[mu[a, b][0]] == r1[b] - r1[a] for a, b in pairs)


def reflect(x):
    return tuple(x[-1] - v for v in reversed(x))


def eligible(x, y):
    gx = [x[b] - x[a] for a, b in pairs]
    gy = [y[b] - y[a] for a, b in pairs]
    return (all(x[a] < x[b] and y[a] < y[b] for a, b in pairs)
            and len(set(gx)) == len(set(gy)) == 15 and set(gx) == set(gy)
            and len({y[i] - x[i] for i in range(6)}) > 1
            and len({y[i] + x[5-i] for i in range(6)}) > 1)


def counts(x, y, correspondence):
    target = Counter(tuple(y[t[correspondence[a, b][1]]] - y[t[correspondence[a, b][0]]]
                           for a, b in pairs) for t in perms)
    result = [0, 0]
    for s in perms:
        v = tuple(x[s[b]] - x[s[a]] for a, b in pairs)
        result[0] += target[v]
        result[1] += target[tuple(-z for z in v)]
    return result


rows = []
for swapped in (False, True):
    for source_reflected in (False, True):
        for target_reflected in (False, True):
            x, y = (r2, r1) if swapped else (r1, r2)
            if source_reflected:
                x = reflect(x)
            if target_reflected:
                y = reflect(y)
            assert eligible(x, y)
            actual = counts(x, y, mu)
            expected = [0, 3] if source_reflected != target_reflected else [3, 0]
            assert actual == expected
            rows.append({'swapped': swapped, 'source_reflected': source_reflected,
                         'target_reflected': target_reflected, 'counts': actual})

# Independent positive and negative inputs exercise every nontriviality gate.
assert not eligible(r1, tuple(v + 3 for v in r1))
assert not eligible(r1, reflect(r1))
broken_mu = dict(mu)
broken_mu[0, 2], broken_mu[0, 3] = broken_mu[0, 3], broken_mu[0, 2]
assert counts(r1, r2, broken_mu) == [0, 0]

# Check the small algebraic reduction used by the Lean diagnostic.
survivors = []
for s in perms:
    x = [r1[i] for i in s]
    if (x[5] + 2*x[0] == x[1] + x[2] + x[4]
            and 2*x[1] + x[3] == 2*x[0] + x[4]
            and x[1] + 2*x[3] == x[0] + x[2] + x[5]):
        survivors.append(s)
        differences = (x[1] - x[0], x[5] - x[0])
        assert differences in ((1, 17), (-6, -9), (5, -8))
        y = reflect(r2)
        assert not any((y[j]-y[i], y[k]-y[i]) == differences
                       for i in range(6) for j in range(6) for k in range(6))
assert len(survivors) == 3
print(json.dumps({'orientation_table': rows, 'source_reduction_survivors': 3,
                  'countercontrols_rejected': 3,
                  'scope': 'exact finite diagnostic of the formal premise; no classification theorem'},
                 indent=2, sort_keys=True))
