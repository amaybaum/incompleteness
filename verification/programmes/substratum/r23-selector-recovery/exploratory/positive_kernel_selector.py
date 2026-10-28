#!/usr/bin/env python3
"""R23-A exploratory control for a conditional spatial-kernel selector.

This is NOT a derivation of positivity, a lattice speed, or their physical
necessity from OI. It checks an exact elementary theorem for *real* finite
cubic-invariant nonnegative normalized spatial kernels with NO self-loop.
The theorem is proved algebraically in the accompanying README. This script
only exhausts an explicitly bounded four-orbit mixture grid and tests
hypothesis-removal countercontrols, with Fraction arithmetic.
"""
from fractions import Fraction as F
from itertools import permutations, product
import json

def orbit(v):
    return tuple(sorted({tuple(sign[i]*v[perm[i]] for i in range(3))
                          for perm in permutations(range(3))
                          for sign in product((-1, 1), repeat=3)}))

O = {
    "unit_axis": orbit((1, 0, 0)),
    "double_axis": orbit((2, 0, 0)),
    "face_diagonal": orbit((1, 1, 0)),
    "body_diagonal": orbit((1, 1, 1)),
}
assert {k: len(v) for k,v in O.items()} == {
    "unit_axis": 6, "double_axis": 6,
    "face_diagonal": 12, "body_diagonal": 8}

def covariance(weights):
    c = [[F(0) for _ in range(3)] for _ in range(3)]
    for name, w in weights.items():
        for d in O[name]:
            for i in range(3):
                for j in range(3):
                    c[i][j] += w * d[i] * d[j] / len(O[name])
    return c

def csquared(weights):
    c = covariance(weights)
    assert all(c[i][j] == (c[0][0] if i == j else 0)
               for i in range(3) for j in range(3))
    return c[0][0]

def compositions4(n):
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                yield a,b,c,n-a-b-c

def run():
    grid = 0
    equality = 0
    names = tuple(O)
    # All convex mixtures on a denominator-6 grid over the four fixed orbits.
    for parts in compositions4(6):
        weights = {name:F(v,6) for name,v in zip(names,parts)}
        assert sum(weights.values()) == 1
        x = csquared(weights)
        assert x >= F(1,3)
        if x == F(1,3):
            equality += 1
            assert weights["unit_axis"] == 1
        grid += 1
    assert equality == 1
    # No-self condition matters: adding the origin with 3/4 and a radius-2
    # orbit with 1/4 gives the same variance and hence same infrared speed.
    with_self = {"origin":F(3,4), "double_axis":F(1,4)}
    assert with_self["origin"]*0+with_self["double_axis"]*4 == 1
    # Nonnegativity matters: a signed nontrivial three-shell measure can
    # reproduce the same two moments 1 and 1, without being nearest-only.
    signed = {"unit_axis": F(5,4), "double_axis": -F(2,5),
              "triple_axis": F(3,20)}
    assert sum(signed.values()) == 1
    assert (signed["unit_axis"] + 4*signed["double_axis"] +
            9*signed["triple_axis"]) == 1
    return {"scope":"bounded four-orbit mixtures only, general theorem is algebraic",
            "grid_cases":grid, "equality_cases":equality,
            "minimum_c_squared":"1/3",
            "uniqueness_under_positivity_and_no_self":"PASS",
            "self_loop_countercontrol":"PASS",
            "signed_weight_countercontrol":"PASS"}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
