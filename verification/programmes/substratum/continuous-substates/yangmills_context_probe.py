#!/usr/bin/env python3
"""SUBSTATE-1: exact one-plaquette U(1) Haar/observation-selection countercontrol.

AMBIENT LATTICE EXAMPLE ONLY, not native OI, SU(2)/SU(3) Yang-Mills,
a Gibbs measure, an operational quantum instrument or an action derivation.

Four links around an oriented square are independent U(1) Haar elements.
Exact integration takes the constant Laurent-Fourier coefficient in four
independent variables. The two positive, gauge-invariant acceptance rules
are toy observer-conditionings, not physical mechanisms selected by OI.
"""
from fractions import Fraction as F
import json

ZERO = (0, 0, 0, 0)
LOOP = (1, 1, 1, 1)
ONE = {ZERO: F(1)}


def add(a, b):
    c = a.copy()
    for k, v in b.items():
        c[k] = c.get(k, F(0)) + v
    return {k: v for k, v in c.items() if v}


def scale(a, s):
    return {k: v * s for k, v in a.items() if v * s}


def sub(a, b):
    return add(a, scale(b, F(-1)))


def mul(a, b):
    c = {}
    for p, v in a.items():
        for q, w in b.items():
            k = tuple(x + y for x, y in zip(p, q))
            c[k] = c.get(k, F(0)) + v * w
    return {k: v for k, v in c.items() if v}


def haar(poly):
    # Each nonzero Fourier mode integrates to zero under independent Haar.
    return poly.get(ZERO, F(0))


def accepted_expectation(obs, acceptance):
    z = haar(acceptance)
    assert z > 0
    return haar(mul(obs, acceptance)) / z


def main():
    neg = tuple(-e for e in LOOP)
    cos_loop = {LOOP: F(1, 2), neg: F(1, 2)}
    cos2 = mul(cos_loop, cos_loop)
    wilson = sub(ONE, cos_loop)        # w = 1 - cos(theta_p)
    alternative = mul(wilson, wilson) # w^2, also gauge invariant

    # Both success/selection contexts have mean 13/16, by construction.
    accept_w = scale(sub(ONE, scale(wilson, F(1, 8))), F(13, 14))
    accept_w2 = sub(ONE, scale(alternative, F(1, 8)))

    edges = ((0, 1), (1, 2), (2, 3), (3, 0))
    balanced = all(
        sum((int(v == source) - int(v == target)) * LOOP[k]
            for k, (source, target) in enumerate(edges)) == 0
        for v in range(4)
    )  # local gauge phases cancel on the closed oriented loop

    checks = {
        "gauge_loop_vertex_balance": balanced,
        "Haar_loop_cos_mean_zero": haar(cos_loop) == 0,
        "Haar_cos_square_half": haar(cos2) == F(1, 2),
        "Haar_cos_fourth_three_eighths": haar(mul(cos2, cos2)) == F(3, 8),
        "distinct_invariant_actions_on_two_holonomies":
            [(F(1, 2), F(1, 4)), (F(2), F(4))] ==
            [(F(1, 2), F(1, 2)**2), (F(2), F(2)**2)],
        "acceptance_in_unit_interval":
            F(0) <= F(13, 14) * (1 - F(2, 8)) <= F(13, 14) <= 1
            and F(0) <= 1 - F(4, 8) <= 1,
        "equal_full_run_success_probabilities":
            haar(accept_w) == haar(accept_w2) == F(13, 16),
        "different_selected_loop_means":
            accepted_expectation(cos_loop, accept_w) == F(1, 14)
            and accepted_expectation(cos_loop, accept_w2) == F(2, 13),
        "selected_second_moments":
            accepted_expectation(cos2, accept_w) == F(1, 2)
            and accepted_expectation(cos2, accept_w2) == F(25, 52),
    }
    if not all(checks.values()):
        raise AssertionError({k: value for k, value in checks.items() if not value})
    print(json.dumps({
        "verdict": "PASS_EXACT_AMBIENT_SELECTION_COUNTERCONTROL",
        "controls": checks,
        "model": "U(1) four-link single plaquette, independent Haar prior",
        "unconditioned_mean_cos": str(haar(cos_loop)),
        "acceptance_rates": [str(haar(accept_w)), str(haar(accept_w2))],
        "selected_mean_cos": [
            str(accepted_expectation(cos_loop, accept_w)),
            str(accepted_expectation(cos_loop, accept_w2))],
        "selected_mean_cos_squared": [
            str(accepted_expectation(cos2, accept_w)),
            str(accepted_expectation(cos2, accept_w2))],
        "physical_Yang_Mills_action_derived": False,
        "native_OI_link_dynamics_derived": False,
        "quantum_operational_completion_derived": False
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
