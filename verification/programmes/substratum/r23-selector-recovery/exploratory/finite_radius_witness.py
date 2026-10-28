#!/usr/bin/env python3
"""Exploratory R23-A diagnostic, not a frozen research execution.

Exact finite arithmetic on a cubic L=7 torus over F_7. This ONLY tests whether
bounded support, translation/cubic symmetry, linearity and omission of an
on-site current-field term uniquely select the nearest-neighbor update.

It is NOT a countermodel to ALL E1-E7/A1-A6 simultaneously, not a verified
model of QM or SM representations, and not a proof about the physical world.
The two rules need not share the physical dispersion or propagation speed.
Do not promote this probe to a theorem or grade without a governed round.
"""
from itertools import product, permutations
import json

Q, L = 7, 7
SITES = tuple(product(range(L), repeat=3))
ZERO = {s: 0 for s in SITES}
IMPULSE = {s: int(s == (0, 0, 0)) for s in SITES}

# Both are reversible *second-order* updates with coefficient -1 on x_(t-1).
# Since 6*(1/3) = 2 and 12*(1/6) = 2 in F_7, both have a massless constant
# mode at the algebraic level. Coupling A has radius 1, B radius 2.
RULES = {
    "A-nearest": {1: pow(3, -1, Q)},
    "B-two-shell": {1: pow(6, -1, Q), 2: pow(6, -1, Q)},
}

def shifted(s, axis, displacement):
    return tuple((s[i] + (displacement if i == axis else 0)) % L
                 for i in range(3))

def neighbor_sum(values, site, radius):
    return sum(values[shifted(site, axis, sign * radius)]
               for axis in range(3) for sign in (-1, +1))

def forward(now, before, rule):
    after = {
        s: (sum(c * neighbor_sum(now, s, radius)
                for radius, c in rule.items()) - before[s]) % Q
        for s in SITES
    }
    return after, now

def backward(after, now, rule):
    before = {
        s: (sum(c * neighbor_sum(now, s, radius)
                for radius, c in rule.items()) - after[s]) % Q
        for s in SITES
    }
    return now, before

def symmetry(values, axis_order, signs):
    return {
        tuple(signs[i] * s[axis_order[i]] % L for i in range(3)): value
        for s, value in values.items()
    }

def translation(values, shift):
    return {
        tuple((s[i] + shift[i]) % L for i in range(3)): value
        for s, value in values.items()
    }

def diagnostic():
    outputs = {}
    for name, rule in RULES.items():
        after, old = forward(IMPULSE, ZERO, rule)
        # Inversion is an exact identity for every configuration: from
        # after = F(now) - before, recover before = F(now) - after.
        assert backward(after, old, rule) == (IMPULSE, ZERO)
        assert sum(rule.values()) * 6 % Q == 2   # constant mode
        for order in permutations(range(3)):
            for signs in product((-1, +1), repeat=3):
                tr = symmetry(IMPULSE, order, signs)
                z = symmetry(ZERO, order, signs)
                assert forward(tr, z, rule)[0] == symmetry(after, order, signs)
        shift = (2, 3, 1)
        assert forward(translation(IMPULSE, shift),
                       translation(ZERO, shift), rule)[0] == translation(after, shift)
        outputs[name] = {
            "coupling_shells": sorted(rule),
            "coefficients_mod_7": {str(k): v for k, v in rule.items()},
            "nonzero_one_step_impulse_sites": sum(v != 0 for v in after.values()),
            "inverse_control": "PASS",
            "48_signed_axis_symmetries": "PASS",
            "translation_control": "PASS",
        }
    assert outputs["A-nearest"]["nonzero_one_step_impulse_sites"] == 6
    assert outputs["B-two-shell"]["nonzero_one_step_impulse_sites"] == 12
    assert outputs["A-nearest"]["nonzero_one_step_impulse_sites"] != outputs["B-two-shell"]["nonzero_one_step_impulse_sites"]
    return {"verdict": "TWO DISTINCT RULES under tested local premises",
            "scope": "A3 bounded support + A4 no self-term/translation + A5 linear + cubic symmetry, not full E1-E7",
            "lattice": "Z/7Z cubed", "field": "F_7", "cases": outputs}

if __name__ == "__main__":
    print(json.dumps(diagnostic(), sort_keys=True, indent=2))
