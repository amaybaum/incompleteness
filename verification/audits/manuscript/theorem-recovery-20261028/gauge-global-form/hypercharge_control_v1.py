#!/usr/bin/env python3
"""Exact coefficient and finite controls for the charge-recovery supplement.

Python standard library only. Polynomial coefficients are checked exactly;
finite enumeration is separately labelled. No floats and no assert.
"""
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(*polys):
    result = {}
    for poly in polys:
        for powers, coefficient in poly.items():
            result[powers] = result.get(powers, 0) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(poly, factor):
    return {m: factor * c for m, c in poly.items() if factor * c}


def mul(left, right):
    result = {}
    for p, a in left.items():
        for q, b in right.items():
            powers = tuple(x + y for x, y in zip(p, q))
            result[powers] = result.get(powers, 0) + a * b
    return {m: c for m, c in result.items() if c}


def cube(poly):
    return mul(mul(poly, poly), poly)


def polynomial_anomalies(a, u, d, l, e):
    return (
        add(scale(a, 2), scale(u, -1), scale(d, -1)),
        add(scale(a, 3), l),
        add(scale(a, 6), scale(u, -3), scale(d, -3), scale(l, 2), scale(e, -1)),
        add(scale(cube(a), 6), scale(cube(u), -3), scale(cube(d), -3),
            scale(cube(l), 2), scale(cube(e), -1)),
    )


def anomalies(a, u, d, l, e, neutrino=None):
    G = 6 * a - 3 * u - 3 * d + 2 * l - e
    A = 6 * a ** 3 - 3 * u ** 3 - 3 * d ** 3 + 2 * l ** 3 - e ** 3
    if neutrino is not None:
        G -= neutrino
        A -= neutrino ** 3
    return 2 * a - u - d, 3 * a + l, G, A


def as_json(poly, variable_names):
    return [{"powers": dict(zip(variable_names, powers)), "coefficient": coefficient}
            for powers, coefficient in sorted(poly.items())]


def polynomial_controls():
    # Linear certificates in independent variables a,u,d,l,e.
    variables = tuple({tuple(int(j == i) for j in range(5)): 1} for i in range(5))
    a, u, d, l, e = variables
    C, W, G, _ = polynomial_anomalies(*variables)
    require(add(d, scale(a, -2), u) == scale(C, -1), "d linear certificate failed")
    require(add(l, scale(a, 3)) == W, "l linear certificate failed")
    require(add(e, scale(a, 6)) == add(scale(C, 3), scale(W, 2), scale(G, -1)),
            "e linear certificate failed")

    # Restricted solution plane: independent polynomial variables a,u.
    a = {(1, 0): 1}
    u = {(0, 1): 1}
    d, l, e = add(scale(a, 2), scale(u, -1)), scale(a, -3), scale(a, -6)
    C, W, G, A = polynomial_anomalies(a, u, d, l, e)
    require(C == W == G == {}, "linear solution plane does not solve linear anomalies")
    factor1 = scale(mul(a, add(scale(mul(a, a), 8), mul(u, d))), 18)
    factor2 = scale(mul(a, mul(add(u, scale(a, -4)), add(u, scale(a, 2)))), -18)
    require(A == factor1 == factor2, "anomaly factorization coefficient identity failed")
    require(A == {(3, 0): 144, (2, 1): 36, (1, 2): -18}, "unexpected expanded cubic")

    # Yukawa plane: independent polynomial variables a,h; weak condition l=-3a.
    h = {(0, 1): 1}
    u, d, l = add(a, h), add(a, scale(h, -1)), scale(a, -3)
    e = add(l, scale(h, -1))
    C2, W2, G2, A2 = polynomial_anomalies(a, u, d, l, e)
    n = add(h, scale(a, -3))
    require(C2 == W2 == {}, "Yukawa weak plane not color/weak anomaly free")
    require(G2 == n and A2 == cube(n), "Yukawa gravitational/cubic identities failed")
    require(add(G2, scale(n, -1)) == {} and add(A2, scale(cube(n), -1)) == {},
            "charged neutrino cancellation identity failed")
    return {
        "linear_certificates": ["d-2a+u=-C", "l+3a=W", "e+6a=3C+2W-G"],
        "classification_cubic_coefficients": as_json(A, ("a", "u")),
        "classification_factorizations": ["18a(8a^2+ud)", "-18a(u-4a)(u+2a)"],
        "Yukawa_gravitational_coefficients": as_json(G2, ("a", "h")),
        "Yukawa_cubic_coefficients": as_json(A2, ("a", "h")),
        "Yukawa_factorization": "(h-3a)^3",
        "charged_neutrino_polynomial_cancellation": True,
    }


def finite_classification_control(bound=6):
    solutions = []
    checked = 0
    for a, u, d, l, e in product(range(-bound, bound + 1), repeat=5):
        checked += 1
        actual = anomalies(a, u, d, l, e) == (0, 0, 0, 0)
        expected = ((a == 0 and d == -u and l == 0 and e == 0) or
                    (a != 0 and l == -3 * a and e == -6 * a and
                     ((u, d) == (4 * a, -2 * a) or (u, d) == (-2 * a, 4 * a))))
        require(actual == expected, "finite classification differs from original equations")
        if actual:
            solutions.append((a, u, d, l, e))
    require(len(solutions) == 17, "unexpected finite solution count")
    return {"all_five_charges_bound": bound, "assignments_checked": checked,
            "solutions_found": len(solutions), "solutions": solutions}


def negative_controls():
    exceptional = (0, 1, -1, 0, 0)
    require(anomalies(*exceptional) == (0, 0, 0, 0), "exceptional branch failed")
    # Nonzero h=1 would be required by u=a+h and violates e=l-h.
    require(exceptional[1] == exceptional[0] + 1 and exceptional[4] != exceptional[3] - 1,
            "exceptional branch unexpectedly admits all h=1 Yukawas")
    with_neutrino = (1, 2, 0, -3, -4)
    require(anomalies(*with_neutrino, neutrino=-2) == (0, 0, 0, 0),
            "charged neutrino counterexample failed")
    require(with_neutrino != (1, 4, -2, -3, -6), "charged neutrino example is standard")
    families = ((1, 4, -2, -2, -5), (1, 4, -2, -4, -7), (1, 4, -2, -3, -6))
    total = tuple(sum(anomalies(*f)[j] for f in families) for j in range(4))
    require(total == (0, 0, 0, 0), "nonuniversal family counterexample failed")
    require(all(u == a + 3 and d == a - 3 and e == l - 3
                for a, u, d, l, e in families), "diagonal Yukawas failed")
    require(len({f[3] for f in families}) == 3, "families unexpectedly universal")
    return {"exceptional_neutral_Q_branch": list(exceptional),
            "charged_neutrino_counterexample": {"family": list(with_neutrino), "n": -2, "h": 1},
            "nonuniversal_three_family_counterexample": families,
            "nonuniversal_total_anomalies": list(total)}


def main():
    print(json.dumps({
        "schema": "oi-hypercharge-recovery-controls-v1",
        "status": "exact_coefficient_identities_and_finite_controls_hold",
        "arithmetic": "exact integer polynomial coefficients and integer enumeration",
        "polynomial_controls": polynomial_controls(),
        "finite_control": finite_classification_control(),
        "negative_controls": negative_controls(),
        "scope": "The general all-real classification uses the written zero-product proof; no OI physical selector or Lean proof is claimed."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
