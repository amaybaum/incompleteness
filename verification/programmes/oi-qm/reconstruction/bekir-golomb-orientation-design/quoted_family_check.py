"""Exact coefficient checks of the recorded two-parameter family, not completeness.

Compare the two printed factorizations with the family definitions, then check
all gaps for both ruler orders and independent reflections as identities in
the parameters. No sampling and no appeal to the general classification.
"""
import ast
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[5]
bridge = (root / 'verification/lean-mathlib/OIBridge/PiccardBridge.lean').read_text()
homometric = (root / 'verification/lean-mathlib/OIBridge/HomometricSix.lean').read_text()


def plus(x, y):
    return tuple(a+b for a, b in zip(x, y))


def minus(x, y):
    return tuple(a-b for a, b in zip(x, y))


def expression(node):
    if isinstance(node, ast.Name):
        return {'p1': (1, 0), 'p2': (0, 1)}[node.id]
    if isinstance(node, ast.Constant):
        assert node.value == 0
        return (0, 0)
    assert isinstance(node, ast.BinOp)
    if isinstance(node.op, ast.Add):
        return plus(expression(node.left), expression(node.right))
    if isinstance(node.op, ast.Sub):
        return minus(expression(node.left), expression(node.right))
    assert isinstance(node.op, ast.Mult) and isinstance(node.left, ast.Constant)
    return tuple(node.left.value*v for v in expression(node.right))


def family(name):
    body = bridge.split('def '+name+' ', 1)[1].split('\n\n', 1)[0]
    items = re.findall(r'\|\s*([0-5])\s*=>\s*([^|\n]+)', body)
    assert [int(i) for i, _ in items] == list(range(6))
    return tuple(expression(ast.parse(s.strip(), mode='eval').body) for _, s in items)


def product(first, second):
    result = Counter()
    for x, cx in first.items():
        for y, cy in second.items():
            result[plus(x, y)] += cx*cy
    return {x: c for x, c in result.items() if c}


x, y = family('piccardX'), family('piccardY')
# Independent transcription of the primary factorization recorded in the
# baseline source audit: exponent vectors use (p1, p2) = (a, b).
phi1 = {(0, 0): 1, (1, 0): 1, (0, 1): 1}
phi2 = {(0, 0): 1, (-2, 1): 1, (-1, 1): -1, (-1, 2): 1}
phi2_reverse = {(0, 0): 1, (0, 1): -1, (1, 1): 1, (-1, 2): 1}
factorizations_match = (product(phi1, phi2) == dict(Counter(x))
                        and product(phi1, phi2_reverse) == dict(Counter(y)))
assert factorizations_match
mu_body = homometric.split('def mu :', 1)[1].split('def muInv :', 1)[0]
mu = {(int(a), int(b)): (int(c), int(d)) for a, b, c, d in
      re.findall(r'\|\s*(\d)\s*,\s*(\d)\s*=>\s*\((\d)\s*,\s*(\d)\)', mu_body)}
pairs = tuple(combinations(range(6), 2))
assert set(mu) == set(pairs)
perms = tuple(permutations(range(6)))


def counts(source, target):
    fingerprints = Counter(tuple(minus(target[t[mu[a, b][1]]], target[t[mu[a, b][0]]])
                                 for a, b in pairs) for t in perms)
    totals = [0, 0]
    for s in perms:
        gaps = tuple(minus(source[s[b]], source[s[a]]) for a, b in pairs)
        totals[0] += fingerprints[gaps]
        totals[1] += fingerprints[tuple(tuple(-v for v in gap) for gap in gaps)]
    return totals


span = (-1, 3)
rows = []
for swapped in (False, True):
    for source_reflected in (False, True):
        for target_reflected in (False, True):
            source, target = (y, x) if swapped else (x, y)
            source = tuple(minus(span, v) for v in source) if source_reflected else source
            target = tuple(minus(span, v) for v in target) if target_reflected else target
            actual = counts(source, target)
            assert actual == ([0, 3] if source_reflected != target_reflected else [3, 0])
            rows.append({'swapped': swapped, 'source_reflected': source_reflected,
                         'target_reflected': target_reflected, 'identity_counts': actual})

# Countercontrols: the same count must come out empty off the quoted correspondence.
broken_mu = dict(mu)
broken_mu[0, 2], broken_mu[0, 3] = broken_mu[0, 3], broken_mu[0, 2]
countercontrols = {
    'translated_family': counts(x, tuple(plus(v, (1, 0)) for v in x)),
    'reflection_congruent_family': counts(x, tuple(minus(span, v) for v in x)),
}
mu_saved = dict(mu)
mu.update(broken_mu)
countercontrols['corrupted_correspondence'] = counts(x, y)
mu.update(mu_saved)
assert counts(x, y) == [3, 0]
assert all(v == [0, 0] for v in countercontrols.values())

print(json.dumps({'factorizations_match': factorizations_match, 'orientation_table': rows,
                  'countercontrols': countercontrols,
                  'arithmetic': 'integer coefficient vectors; polynomial identities',
                  'scope': 'recorded quoted family and its orientation/order variants; '
                           'no statement that every exceptional pair belongs to it'},
                 indent=2, sort_keys=True))
