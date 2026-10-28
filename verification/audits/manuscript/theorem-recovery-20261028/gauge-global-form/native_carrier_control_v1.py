#!/usr/bin/env python3
"""Exact noncentral finite control for native_carrier_barrier_v1.txt."""
import itertools
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def monomials(n, modulus):
    for permutation in itertools.permutations(range(n)):
        for phases in itertools.product(range(modulus), repeat=n):
            yield permutation, phases


def scalar(n, phase):
    return tuple(range(n)), (phase,) * n


def native_six(C, D, t):
    p, a = C
    q, b = D
    return p + tuple(3 + x for x in q) + (5,), a + b + (t,)


def conjugation_on_unit(g, i, j, modulus):
    # g E_ij g^-1 = root^(a_i-a_j) E_(p_i,p_j), exactly.
    permutation, phases = g
    return permutation[i], permutation[j], (phases[i] - phases[j]) % modulus


def fixes_entire_End(g, modulus):
    return all(conjugation_on_unit(g, i, j, modulus) == (i, j, 0)
               for i in range(6) for j in range(6))


def main():
    modulus = 6
    color = tuple(monomials(3, modulus))
    weak = tuple(monomials(2, modulus))
    actual = set()
    checked = 0
    for C, D, t in itertools.product(color, weak, range(modulus)):
        checked += 1
        if fixes_entire_End(native_six(C, D, t), modulus):
            actual.add((C, D, t))
    expected = {(scalar(3, c), scalar(2, c), c) for c in range(modulus)}
    require(actual == expected, "full End conjugation kernel differs from common phase")

    K = {(scalar(3, c), scalar(2, d), (2 * c - d) % modulus)
         for c in range(modulus) for d in range(modulus)}
    K_fixing_End = {x for x in K if fixes_entire_End(native_six(*x), modulus)}
    require(K_fixing_End == expected, "K intersection End kernel differs from common phase")
    extra_circle = []
    for u in range(modulus):
        g = native_six(scalar(3, 0), scalar(2, u), -u % modulus)
        phase32 = conjugation_on_unit(g, 0, 3, modulus)[2]
        phase31 = conjugation_on_unit(g, 0, 5, modulus)[2]
        phase21 = conjugation_on_unit(g, 3, 5, modulus)[2]
        require((phase32, phase31, phase21) ==
                ((-u) % modulus, u, (2 * u) % modulus), "cross-Hom charge mismatch")
        require(fixes_entire_End(g, modulus) == (u == 0), "extra K circle acts trivially")
        extra_circle.append({"u_phase": u, "cross_Hom_phases": [phase32, phase31, phase21]})

    print(json.dumps({
        "schema": "oi-native-End-kernel-control-v1",
        "status": "finite_controls_hold",
        "arithmetic": "exact integers modulo six",
        "color_monomial_group_order": len(color),
        "weak_monomial_group_order": len(weak),
        "G0_elements_checked": checked,
        "full_End_kernel_order": len(actual),
        "full_End_kernel_is_common_phase": True,
        "K_elements_on_grid": len(K),
        "K_elements_fixing_full_End": len(K_fixing_End),
        "extra_K_circle": extra_circle,
        "scope": "Exact finite controls; general matrix-unit proof and physical limits are separate."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
