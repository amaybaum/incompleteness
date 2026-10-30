#!/usr/bin/env python3
"""OI observer-relative finiteness: exact finite regression controls.

The all-observer and infinite-parameter conclusions have analytic proofs
in OBSERVER-RELATIVE-FINITENESS.md; finite tests cannot prove them.
No physical horizon assumption or quantum/YM completion is derived.
"""
from fractions import Fraction as F
import json


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def main():
    width = 12
    states = range(1 << width)
    observers = []
    for n in range(1, width + 1):
        prefixes = {x % (1 << n) for x in states}
        require(len(prefixes) == 1 << n, "prefix quotient")
        observers.append({"resolved_bits": n, "distinct_records": len(prefixes)})
    # A finite outcome alphabet can support arbitrarily many EXACT response
    # probabilities across different preparations. Here each θ=k/N is
    # represented by a binary Bernoulli distribution, not a new outcome.
    preparations = []
    for denominator in (1, 2, 3, 4, 8, 16, 32, 64):
        distributions = {(F(k, denominator), 1 - F(k, denominator))
                         for k in range(denominator + 1)}
        require(len(distributions) == denominator + 1, "Bernoulli cardinality")
        require(all(a + b == 1 for a, b in distributions), "normalization")
        preparations.append({"denominator": denominator,
                             "binary_outcome_count": 2,
                             "distinct_exact_laws": len(distributions)})
    # Finite full-record classes under K+1 deterministic bit reads.
    history_classes = []
    for k in range(0, 9):
        words = {tuple((x >> j) & 1 for j in range(k + 1)) for x in states}
        require(len(words) == 1 << (k + 1), "history quotient")
        history_classes.append({"time_horizon": k,
                                "record_classes": len(words)})
    # Equal CURRENT readout need not induce equal NEXT readout, so the
    # finite record quotient is not automatically autonomous dynamics.
    q = 1 << width
    read = lambda x: (x >> 3) & 1
    first, second = 0, 7
    require(read(first) == read(second) == 0, "same present")
    require(read((first + 1) % q) == 0 and
            read((second + 1) % q) == 1, "different next")
    out = {
        "status": "PASS_OBSERVER_RELATIVE_FINITE_RECORD_CONTROLS",
        "whole_state_count_in_regression": q,
        "finite_observer_partitions": observers,
        "two_outcome_distinct_response_laws": preparations,
        "finite_history_quotients": history_classes,
        "nonclosure_witness": {"states": [first, second],
                               "same_present_bit": 0,
                               "different_next_bits": [0, 1]},
        "unbounded_observer_family_proved_by_finite_enumeration": False,
        "continuous_preparation_family_proved_by_finite_enumeration": False,
        "all_embedded_observers_have_finite_horizons": False,
        "finite_operational_state_space_derived": False,
        "ontic_state_cardinality_derived": False,
        "quantum_or_Yang_Mills_derived": False,
    }
    print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
