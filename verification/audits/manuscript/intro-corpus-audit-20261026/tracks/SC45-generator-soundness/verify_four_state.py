#!/usr/bin/env python3
"""SC-45: exact four-state controls for Substratum Theorem 24(i).

Pure finite exhaustive arithmetic, no floating point, no source-file writes.
These are controlled counterexamples for the *fixed* observer interface, not
a verdict about the all-partitions gauge group or the graph family (iv).
"""
from fractions import Fraction
from itertools import permutations

STATES = tuple((v, h) for v in range(2) for h in range(2))
HALF = Fraction(1, 2)


def inverse(p):
    assert set(p) == set(STATES) == set(p.values())
    return {b: a for a, b in p.items()}


def compose(f, g):
    return {s: f[g[s]] for s in STATES}


def conjugate(phi, p):
    return compose(compose(p, phi), inverse(p))


def power(phi, n):
    result = {s: s for s in STATES}
    for _ in range(n):
        result = compose(phi, result)
    return result


def kernel(phi, n=1, pi=None):
    # pi transports BOTH the readout and the uniformly prepared hidden fibre.
    if pi is None:
        pi = {s: s for s in STATES}
    inv = inverse(pi)
    pn = power(phi, n)
    return tuple(tuple(
        Fraction(sum(inv[pn[pi[(v, h)]]][0] == w for h in range(2)), 2)
        for w in range(2)
    ) for v in range(2))


def test():
    phi = {(v, h): (h, v) for v, h in STATES}
    pi = {s: s for s in STATES}
    pi[(0, 0)], pi[(1, 0)] = pi[(1, 0)], pi[(0, 0)]
    phi_prime = conjugate(phi, pi)

    uniform = ((HALF, HALF), (HALF, HALF))
    ident = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    assert kernel(phi) == uniform, kernel(phi)
    assert kernel(phi_prime) == ident, kernel(phi_prime)
    assert kernel(phi) != kernel(phi_prime)
    # Distinct fixed-interface laws, SAME coordinates simultaneously renamed.
    for n in range(5):
        assert kernel(phi_prime, n, pi) == kernel(phi, n), n

    # Positive control: a hidden-factor relabeling preserves the uniform-prior
    # law even with the original visible partition held fixed.
    relabel_hidden = {(v, h): (v, 1-h) for v, h in STATES}
    hidden_prime = conjugate(phi, relabel_hidden)
    for n in range(5):
        assert kernel(hidden_prime, n) == kernel(phi, n), n

    # Broader diagnostic: count relabelings preserving the fixed-interface
    # ONE-STEP matrix; no inferential claim about all-time observable carriers.
    preserving = 0
    violating = 0
    for arrangement in permutations(STATES):
        q = dict(zip(STATES, arrangement))
        if kernel(conjugate(phi, q)) == kernel(phi):
            preserving += 1
        else:
            violating += 1
    assert preserving + violating == 24
    assert violating > 0
    return preserving, violating


if __name__ == "__main__":
    good, bad = test()
    print(f"SC45 COUNTEREXAMPLE CONFIRMED; 24 relabelings: {good} fixed-interface one-step-preserving, {bad} violating; positive controls PASS")
