#!/usr/bin/env python3
"""Independent Fourier-diagonalization and binary-record review controls."""
from fractions import Fraction as F
from itertools import product
import json


POINTS = tuple(product((-1, 1), repeat=3))


def require(value, message):
    if not value:
        raise RuntimeError(message)


def probability(r):
    result = []
    for point in POINTS:
        value = F(1)
        for mean, sign in zip(r, point):
            value *= (1 + mean * sign) / 2
        result.append(value)
    return tuple(result)


def expectation(p, mask):
    value = F()
    for weight, point in zip(p, POINTS):
        term = weight
        for axis in range(3):
            if mask & (1 << axis):
                term *= point[axis]
        value += term
    return value


def mm(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(row, column))
                       for column in zip(*b)) for row in a)


def transpose(a):
    return tuple(zip(*a))


def tv(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) / 2


def rotate(r):
    return (F(3, 5) * r[0] - F(4, 5) * r[1],
            F(4, 5) * r[0] + F(3, 5) * r[1], F(r[2]))


def main():
    parameter = F(1, 3)
    source_vectors = tuple(tuple(parameter * sign for sign in point) for point in POINTS)
    source = tuple(probability(r) for r in source_vectors)
    for r, p in zip(source_vectors, source):
        require(min(p) == F(1, 27) and sum(p) == 1, "spanning positivity")
        require(sum(v * v for v in r) == F(1, 3), "spanning Bloch norm")
        for axis in range(3):
            require(expectation(p, 1 << axis) == r[axis], "spanning first moments")
    matrix = transpose(source)
    walsh = []
    for mask in range(8):
        row = []
        for point in POINTS:
            value = 1
            for axis in range(3):
                if mask & (1 << axis):
                    value *= point[axis]
            row.append(F(value))
        walsh.append(tuple(row))
    walsh = tuple(walsh)
    require(mm(walsh, transpose(walsh)) == tuple(tuple(F(8 * (i == j)) for j in range(8))
                                                for i in range(8)), "Walsh invertibility")
    spectral = mm(mm(walsh, matrix), transpose(walsh))
    eigenvalues = tuple(parameter ** mask.bit_count() for mask in range(8))
    for i in range(8):
        for j in range(8):
            require(spectral[i][j] == (8 * eigenvalues[i] if i == j else 0),
                    "independent product-spectrum certificate")
    determinant = F(1)
    for eigenvalue in eigenvalues:
        determinant *= eigenvalue
    require(determinant == F(1, 531441), "product determinant")
    diagonal_inverse = tuple(tuple((1 / eigenvalues[i]) if i == j else F()
                                   for j in range(8)) for i in range(8))
    inverse = tuple(tuple(value / 8 for value in row)
                    for row in mm(mm(transpose(walsh), diagonal_inverse), walsh))
    require(mm(matrix, inverse) == tuple(tuple(F(i == j) for j in range(8)) for i in range(8)),
            "explicit inverse reconstructs point vectors")
    require(all(sum(column) == 1 for column in zip(*inverse)), "interpolation affine totals")
    require(min(value for row in inverse for value in row) < 0, "not physical convex mixing")

    # Derive the unique binary response needed for the finite spanning inputs.
    target_probabilities = tuple((1 + rotate(r)[0]) / 2 for r in source_vectors)
    forced = tuple(sum(target_probabilities[j] * inverse[j][i] for j in range(8))
                   for i in range(8))
    require(forced == tuple((1 + rotate(point)[0]) / 2 for point in POINTS),
            "unique forced binary response")
    require(min(forced) == F(-1, 5) and max(forced) == F(6, 5),
            "no positive binary response for all spanning preparations")

    pair_vectors = ((F(2, 3), F(-2, 3), F()), (F(-2, 3), F(2, 3), F()))
    pair = tuple(probability(r) for r in pair_vectors)
    require(pair[0] == tuple(F(x, 72) for x in (5, 5, 1, 1, 25, 25, 5, 5)),
            "explicit pair source plus")
    require(pair[1] == tuple(F(x, 72) for x in (5, 5, 25, 25, 1, 1, 5, 5)),
            "explicit pair source minus")
    for r, p in zip(pair_vectors, pair):
        require(sum(v * v for v in r) == F(8, 9) and sum(map(abs, r)) == F(4, 3),
                "new pair valid ball and outside old octahedron")
        require(min(p) == F(1, 72) and sum(p) == 1, "new pair source positivity")
    target_records = tuple(((1 + rotate(r)[0]) / 2, (1 - rotate(r)[0]) / 2) for r in pair_vectors)
    require(target_records == ((F(29, 30), F(1, 30)), (F(1, 30), F(29, 30))),
            "new pair target records")
    source_tv, target_tv = tv(*pair), tv(*target_records)
    floor = (target_tv - source_tv) / 2
    require(source_tv == F(2, 3) and target_tv == F(14, 15) and floor == F(2, 15),
            "pair contraction bound")
    best, count = F(1), 0
    for response in product((0, 1), repeat=8):
        yes = tuple(sum(p[i] * response[i] for i in range(8)) for p in pair)
        require(abs(yes[0] - yes[1]) <= source_tv, "all deterministic response contractions")
        error = max(abs(yes[i] - target_records[i][0]) for i in range(2))
        if error < best:
            best, count = error, 1
        elif error == best:
            count += 1
    x_records = tuple(((1 + r[0]) / 2, (1 - r[0]) / 2) for r in pair_vectors)
    require(best == floor and max(tv(a, b) for a, b in zip(x_records, target_records)) == floor,
            "tight pair bound and explicit X read")

    mixed = tuple((a + b) / 2 for a, b in zip(*pair))
    uniform = probability((F(), F(), F()))
    require(all(expectation(mixed, 1 << axis) == 0 for axis in range(3)), "mixture moments")
    require(expectation(mixed, 3) == F(-4, 9) and expectation(uniform, 3) == 0,
            "product section nonconvexity")
    require(mixed != uniform, "same means do not select hidden mixed prior")
    closure_controls = 0
    for r in source_vectors + pair_vectors:
        for action in (lambda p: (p[2], -p[1], p[0]), lambda p: (-p[1], p[0], p[2])):
            outgoing = {action(s): weight for s, weight in zip(POINTS, probability(r))}
            require(tuple(outgoing[s] for s in POINTS) == probability(action(r)), "Clifford product closure")
            closure_controls += 1

    # Gaussian-integer phase multiplier of diag(2-i,2+i)/sqrt(5).
    require((2 * 2 - 1, -2 * 2) == (3, -4), "unitary conjugation phase")
    require(3 * 3 + 4 * 4 == 5 * 5, "unitary phase modulus")
    for r in source_vectors + pair_vectors:
        x, y, z = r
        actual_real = (3 * x - 4 * y) / 10
        actual_imag = (-4 * x - 3 * y) / 10
        rx, ry, rz = rotate(r)
        require((actual_real, actual_imag, z) == (rx / 2, -ry / 2, rz),
                "density-matrix off-diagonal rotation")
    labels = ((F(29, 30), F(1, 30)), (F(1, 30), F(29, 30)))
    for label, accepted in enumerate((29, 1)):
        sampled = sum(int(seed < accepted) for seed in range(30))
        require((F(sampled, 30), F(30 - sampled, 30)) == labels[label],
                "supplied preparation label controller")
    tagged_plus = tuple(weight if label == 0 else F() for label in (0, 1) for weight in pair[0])
    tagged_minus = tuple(weight if label == 1 else F() for label in (0, 1) for weight in pair[1])
    require(tv(tagged_plus, tagged_minus) == 1, "label changes complete-input distinguishability")

    print(json.dumps({
        "schema": "oi-product-section-v4-review-1",
        "author_commit": "d6966ce055f6f1d872080328023fc37d68d17533",
        "verdict": "ACCEPT_WITHIN_SCOPE",
        "blockers": [],
        "spanning_product_priors": 8,
        "independent_spectral_matrix_controls": 64,
        "rank_certificate": 8,
        "determinant": str(determinant),
        "forced_binary_response_range": [str(min(forced)), str(max(forced))],
        "source_pair_tv": str(source_tv),
        "target_pair_tv": str(target_tv),
        "tight_pair_error_floor": str(floor),
        "all_binary_response_controls": 256,
        "optimal_deterministic_responses": count,
        "mixture_xy_correlation": "-4/9",
        "Clifford_product_closure_controls": closure_controls,
        "prep_label_input_tv": "1",
        "all_controls_pass": True,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
