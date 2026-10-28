#!/usr/bin/env python3
"""Distinguish no additive 2-torsion from merely characteristic != 2."""

import json
from pathlib import Path

from verify_sm3 import add, anticomm, diag, scale, zero


def reduce_mod(a, q):
    return [[x % q for x in row] for row in a]


def main():
    q = 6
    epsilon = diag([1, -1])
    perturbation = scale(3, diag([1, 1]))
    reduced = reduce_mod(anticomm(perturbation, epsilon), q)
    assert not zero(reduce_mod(perturbation, q)) and zero(reduced)
    nonunique_center = reduce_mod(add(scale(3, epsilon), scale(3, diag([1, 1]))), q)
    assert zero(nonunique_center)
    # Composite odd modulus is allowed: primeness or an integral domain is unnecessary.
    q_odd = 9
    for x in range(q_odd):
        assert ((2 * x) % q_odd == 0) == (x == 0)
    for m in range(q_odd):
        for p in range(q_odd):
            vanished = (m + p) % q_odd == 0 and (-m + p) % q_odd == 0
            assert vanished == (m == 0 and p == 0)
    report = {
        "status": "PASS",
        "modulus6_control": {
            "characteristic": 6,
            "has_additive_2_torsion": True,
            "C": perturbation,
            "epsilon": epsilon,
            "anticommutator_mod6": reduced,
            "uniform_m": 3,
            "uniform_p": 3,
            "center_mod6": nonunique_center,
            "characteristic_not_2_alone_insufficient": True,
        },
        "modulus9_positive": {"no_two_torsion_cases": 9,
                               "uniform_coefficient_cases": 81,
                               "primality_unnecessary": True},
        "scope": "exact finite controls, not universal proof",
    }
    out = Path(__file__).with_name("modular-scope-results.json")
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "positive_cases": 90,
                      "negative_controls": 1, "output": str(out)}))


if __name__ == "__main__":
    main()
