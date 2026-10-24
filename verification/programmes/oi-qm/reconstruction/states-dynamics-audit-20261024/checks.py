#!/usr/bin/env python3
"""Exact bounded controls for PROBE-SPEC.md; no native dynamics imported."""

from collections import Counter
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import argparse
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    return x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def scale(c, x):
    return c * x[0], c * x[1]


def sign(x):
    a, b = x
    if not b:
        return (a > 0) - (a < 0)
    if not a:
        return (b > 0) - (b < 0)
    if a * b > 0:
        return (a > 0) - (a < 0)
    d = a * a - 2 * b * b
    return ((d > 0) - (d < 0)) * ((a > 0) - (a < 0))


def text_fraction(x):
    return str(x)


def run():
    weights = (5, 5, 3, 3, 2, 2)
    labels = ((0, 0, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1))
    target = {outcome: F(w, 20) for outcome, w in zip(labels, weights)}

    def law(counts):
        total = sum(counts.values())
        return {key: F(value, total) for key, value in counts.items()} if total else {}

    # Check counts directly rather than calling a divisibility oracle.
    benchmarks = []
    for b in range(17):
        atoms = 2 ** b
        proposed_success = F(5 * atoms, 16)
        possible = proposed_success.denominator == 1 and all(
            (proposed_success * prob).denominator == 1 for prob in target.values()
        )
        require(possible == (b >= 6), "success benchmark differs from proved bound")
        always = all((atoms * prob).denominator == 1 for prob in target.values())
        require(not always, "dyadic always-success law incorrectly accepted")
        # All candidate nonzero success counts for this bounded bank.
        for success in range(1, atoms + 1):
            feasible = all((success * prob).denominator == 1 for prob in target.values())
            require(feasible == (success % 20 == 0), "integer feasibility mismatch")
        benchmarks.append({"fair_bits": b, "success_5_over_16_feasible": possible})

    # Seed-preserving XOR into a three-bit register; register value0 is failure.
    assignment = [code for code, count in enumerate(weights, 1) for _ in range(count)] + [0] * 44
    require(len(assignment) == 64, "seed space size")
    permutation = {(s, r): (s, r ^ assignment[s]) for s in range(64) for r in range(8)}
    require(len(set(permutation.values())) == 512, "sampler not bijective")
    require(all(permutation[permutation[state]] == state for state in permutation), "not involutive")
    successful = Counter(labels[assignment[s] - 1] for s in range(64) if assignment[s])
    require(law(successful) == target, "wrong full successful law")
    failures = sum(code == 0 for code in assignment)
    require(F(64 - failures, 64) == F(5, 16), "wrong success law")
    carrier_cases = []
    for y in (0, 1):
        actual = Counter((y ^ a, y, y ^ b, z) for (a, b, z), count in successful.items() for _ in range(count))
        expected = {(y ^ a, y, y ^ b, z): p for (a, b, z), p in target.items()}
        require(law(actual) == expected, "carrier law mismatch")
        carrier_cases.append({"y": y, "joint_law_matched": True})

    wrong_ratio = Counter(dict(zip(labels, (5, 5, 2, 2, 3, 3))))
    require(law(wrong_ratio) != target, "wrong calibration control vacuous")
    fixed_z = Counter({(0, 0, 0): 10, (1, 0, 0): 6, (1, 1, 0): 4})
    require(law(fixed_z) != target, "bad z accepted")
    marginal = Counter()
    for (a, b, z), count in fixed_z.items():
        marginal[a, b] += count
    require(law(marginal) == {(0, 0): F(1, 2), (1, 0): F(3, 10), (1, 1): F(1, 5)}, "marginal control")

    p = (F(1, 2), F(1, 4))
    polynomial = add(add(scale(8, mul(p, p)), scale(-8, p)), (F(1), F(0)))
    require(polynomial == (0, 0), "irrational target polynomial")
    require(sign(p) > 0 and sign(add((F(1), F(0)), scale(-1, p))) > 0, "invalid prior")
    require(sign((F(1), F(-1))) < 0 and sign((F(3, 2), F(-1))) > 0, "ordering controls")
    comparisons = 0
    for m in range(1, 65):
        for n in range(m + 1):
            delta = add((F(n, m), F(0)), scale(-1, p))
            require(sign(delta) != 0, "rational falsely equal to p")
            absolute = scale(sign(delta), delta)
            require(sign(add(absolute, (F(-1, 8 * m * m), F(0)))) > 0, "finite budget bound")
            require(8 * n * n - 8 * n * m + m * m != 0, "integer witness vanished")
            comparisons += 1

    brackets = []
    previous_width = F(1)
    for b in range(1, 17):
        atoms = 2 ** b
        k = atoms // 2 + isqrt(2 * atoms * atoms) // 4
        lo, hi = F(k, atoms), F(k + 1, atoms)
        require(sign(add(p, (-lo, F(0)))) > 0 and sign(add((hi, F(0)), scale(-1, p))) > 0, "bad bracket")
        require(hi - lo == F(1, atoms) and hi - lo < previous_width, "bracket width")
        previous_width = hi - lo
        brackets.append({"fair_bits": b, "lower": text_fraction(lo), "upper": text_fraction(hi)})

    # Two-state identity model, with p placed in the prior, reproduces p exactly.
    prior = (p, add((F(1), F(0)), scale(-1, p)))
    require(add(*prior) == (1, 0) and prior[0] == p, "irrational prior countercontrol")
    return {
        "schema": "oi-states-dynamics-finite-resource-v1",
        "verdict": "PASS",
        "scope": "abstract finite-resource diagnostic; not native implementation or full QM equivalence",
        "benchmark": benchmarks,
        "sampler": {"random_bits": 6, "blank_label_bits": 3, "states": 512,
                    "successful_atoms": 20, "failure_atoms": failures,
                    "success_probability": "5/16", "conditional_counts": list(weights),
                    "bijective": True, "involutive": True, "carrier_checks": carrier_cases},
        "negative_controls": {"wrong_5_2_3_ratio_rejected": True, "fixed_z_rejected_despite_correct_ab_marginal": True},
        "irrational_target": {"symbolic": "(2+sqrt(2))/4", "polynomial": [8, -8, 1],
                              "rational_comparisons": comparisons, "strict_bound": "1/(8*M^2)",
                              "brackets": brackets, "irrational_prior_countercontrol_exact": True},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    else:
        print(encoded, end="")
