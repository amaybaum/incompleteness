#!/usr/bin/env python3
"""Independent exact finite controls for SM3 recovery; not a universal proof.

All calculations use Python integers. Characteristic two is handled by an
explicit reduction mod 2. The controls deliberately leave the proposed theorem's
class, and must exhibit failure of the corresponding overbroad conclusion.
"""

from itertools import product
import json
from pathlib import Path


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mul(a, b):
    return [[sum(x * y for x, y in zip(ar, bc)) for bc in zip(*b)] for ar in a]


def scale(k, a):
    return [[k * x for x in ar] for ar in a]


def diag(xs):
    return [[x if i == j else 0 for j in range(len(xs))] for i, x in enumerate(xs)]


def zero(a):
    return all(x == 0 for ar in a for x in ar)


def anticomm(a, e):
    return add(mul(a, e), mul(e, a))


def commutes(a, e):
    return mul(a, e) == mul(e, a)


def odd_support(a, signs):
    return all(x == 0 for i, ar in enumerate(a) for j, x in enumerate(ar)
               if signs[i] == signs[j])


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def main():
    signs = [1, -1]
    e = diag(signs)
    ident = diag([1, 1])
    positive = []
    controls = []

    count = 0
    for a, b, c, d in product(range(-2, 3), repeat=4):
        matrix = [[a, b], [c, d]]
        require(zero(anticomm(matrix, e)) == odd_support(matrix, signs),
                "entry classification")
        count += 1
    positive.append({"name": "matrix chirality iff opposite-parity support",
                     "cases": count, "arithmetic": "integer", "pass": True})

    count = 0
    for b, c, a, d in product(range(-2, 3), repeat=4):
        hopping = [[0, b], [c, 0]]
        even = diag([a, d])
        require(zero(anticomm(hopping, e)) and commutes(even, e),
                "independent hypothesis calculation")
        require(zero(anticomm(add(hopping, even), e)) == zero(even),
                "general even perturbation equivalence")
        count += 1
    positive.append({"name": "fixed odd hopping plus arbitrary even perturbation",
                     "cases": count, "arithmetic": "integer", "pass": True})

    count = 0
    for b, c in product(range(-2, 3), repeat=2):
        hopping = [[0, b], [c, 0]]
        for m, p in product(range(-3, 4), repeat=2):
            center = add(scale(m, e), scale(p, ident))
            require(zero(anticomm(add(hopping, center), e)) == (m == 0 and p == 0),
                    "uniform coefficient uniqueness")
            count += 1
    positive.append({"name": "both-sector uniform coefficient equivalence",
                     "cases": count, "arithmetic": "integer", "pass": True})

    # Dropping evenness admits a nonzero additional odd hopping term.
    additional_odd = [[0, 1], [0, 0]]
    require(not zero(additional_odd) and not commutes(additional_odd, e)
            and zero(anticomm(additional_odd, e)), "dropped evenness control")
    controls.append({"name": "drop perturbation-evenness", "perturbation": additional_odd,
                     "total_chiral": True, "perturbation_nonzero": True,
                     "overbroad_claim_refuted": True})

    # An even term may cancel an even component of unfixed/non-odd D.
    d = ident
    even = scale(-1, ident)
    require(commutes(even, e) and not zero(anticomm(d, e)) and not zero(even)
            and zero(anticomm(add(d, even), e)), "dropped odd baseline control")
    controls.append({"name": "drop fixed odd hopping", "D": d, "C": even,
                     "total_chiral": True, "C_nonzero": True,
                     "overbroad_claim_refuted": True})

    # In characteristic 2, 2Cε=0 need not imply C=0.
    mod2 = [[x % 2 for x in ar] for ar in anticomm(ident, ident)]
    require(zero(mod2) and not zero(ident), "characteristic-two control")
    controls.append({"name": "drop no-two-torsion", "modulus": 2,
                     "C": ident, "epsilon": ident, "anticommutator_mod2": mod2,
                     "overbroad_claim_refuted": True})

    # One parity sector cannot identify two uniform coefficients.
    one_sector_e = diag([1])
    center = add(scale(1, one_sector_e), scale(-1, diag([1])))
    require(zero(center), "missing parity-sector control")
    controls.append({"name": "drop negative parity sector", "m": 1, "p": -1,
                     "epsilon": one_sector_e, "center": center,
                     "overbroad_claim_refuted": True})

    # Arbitrary commuting OPERATOR coefficients m,p need not be independent.
    op_m = ident
    op_p = scale(-1, e)
    center = add(mul(op_m, e), op_p)
    require(commutes(op_m, e) and commutes(op_p, e)
            and not zero(op_m) and not zero(op_p) and zero(center),
            "operator coefficient cancellation control")
    controls.append({"name": "replace uniform scalar coefficients by commuting operators",
                     "operator_m": op_m, "operator_p": op_p, "center": center,
                     "overbroad_claim_refuted": True})

    # No onsite terms alone does not rule out same-parity offsite hopping.
    e3 = diag([1, -1, 1])
    a3 = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
    require(all(a3[i][i] == 0 for i in range(3)) and not zero(anticomm(a3, e3)),
            "zero diagonal insufficient control")
    controls.append({"name": "replace opposite-parity support by zero diagonal",
                     "epsilon": e3, "A": a3, "anticommutator": anticomm(a3, e3),
                     "overbroad_claim_refuted": True})

    # A chiral first-order operator can have a nonzero diagonal after squaring.
    a = [[0, 1], [-1, 0]]
    a2 = mul(a, a)
    require(zero(anticomm(a, e)) and any(a2[i][i] != 0 for i in range(2)),
            "first/second-order distinction control")
    controls.append({"name": "identify second-order diagonal with first-order mass",
                     "D": a, "D_squared": a2,
                     "D_chiral": True, "D_squared_diagonal_nonzero": True,
                     "overbroad_claim_refuted": True})

    report = {"status": "PASS", "scope": "exact finite controls, not universal proof",
              "positive_total": sum(x["cases"] for x in positive),
              "positive_checks": positive, "negative_controls": controls}
    output = Path(__file__).with_name("controls-results.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "positive_total": report["positive_total"],
                      "negative_controls": len(controls), "output": str(output)}))


if __name__ == "__main__":
    main()
