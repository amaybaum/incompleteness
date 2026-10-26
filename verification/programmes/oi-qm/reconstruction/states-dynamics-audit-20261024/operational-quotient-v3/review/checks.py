#!/usr/bin/env python3
"""Independent exact review controls. No author imports or data evaluation."""
from fractions import Fraction as Q
from itertools import product, permutations
import json

S = tuple(product((-1, 1), repeat=3))
POS = {s: i for i, s in enumerate(S)}
UNIFORM = (Q(1, 8),) * 8


def check(condition, label):
    if not condition:
        raise RuntimeError(label)


def moment(p):
    return (sum(p, Q()), *(sum((p[i] * s[a] for i, s in enumerate(S)), Q())
                           for a in range(3)))


def mult(p, c):
    return tuple(c * v for v in p)


def distribution(axis, sign):
    return tuple(Q(int(s[axis] == sign), 4) for s in S)


def measure_reset(p, axis, sign):
    probability = sum((p[i] for i, s in enumerate(S) if s[axis] == sign), Q())
    return mult(distribution(axis, sign), probability)


def matrix_apply(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def transform(p, matrix):
    out = [Q()] * 8
    for i, s in enumerate(S):
        out[POS[matrix_apply(matrix, s)]] += p[i]
    return tuple(out)


H = ((0, 0, 1), (0, -1, 0), (1, 0, 0))
PHASE = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
ROT = ((Q(3, 5), Q(-4, 5), 0), (Q(4, 5), Q(3, 5), 0), (0, 0, 1))


def target_measure(vector, axis, sign):
    probability = (vector[0] + sign * vector[axis + 1]) / 2
    return (probability, *(sign * probability if a == axis else Q() for a in range(3)))


def tv(p, q):
    return sum((abs(a - b) for a, b in zip(p, q)), Q()) / 2


def det_density(v):
    return (v[0] ** 2 - sum(x * x for x in v[1:])) / 4


def main():
    eigenstates = [distribution(axis, sign) for axis in range(3) for sign in (-1, 1)]
    correlated = [tuple(Q(int(s[0] * s[1] == sign), 4) for s in S) for sign in (-1, 1)]
    nu = [tuple(Q(1, 12) + Q(int(i == j), 3) for i in range(8)) for j in range(8)]
    preparations = eigenstates + [UNIFORM] + correlated + nu
    # Reviewer checks 17 priors; two xyz-parity author controls are unnecessary
    # for this independent set because Walsh-nullspace controls cover them.
    local = 0
    for p in preparations:
        m = moment(p)
        check(m[0] == 1 and sum(abs(x) for x in m[1:]) <= 1, "input cone")
        for axis, sign in product(range(3), (-1, 1)):
            out = measure_reset(p, axis, sign)
            check(moment(out) == target_measure(m, axis, sign), "projector law")
            check(det_density(moment(out)) >= 0, "branch positivity")
            local += 1

    # Independent enumeration of all proper signed-coordinate permutations.
    rotations = []
    for order in permutations(range(3)):
        parity = (-1) ** sum(order[i] > order[j] for i in range(3) for j in range(i + 1, 3))
        for signs in product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] == 1:
                rotations.append(tuple(tuple(signs[i] if j == order[i] else 0 for j in range(3))
                                       for i in range(3)))
    check(len(rotations) == 24 and H in rotations and PHASE in rotations, "rotation class")
    null_cases = 0
    walsh = []
    for mask in range(8):
        vector = tuple(Q(1) for _ in S)
        for a in range(3):
            if mask & (1 << a):
                vector = tuple(v * s[a] for v, s in zip(vector, S))
        walsh.append(vector)
    for i in range(8):
        for j in range(8):
            check(sum(a * b for a, b in zip(walsh[i], walsh[j])) == (8 if i == j else 0),
                  "Walsh basis independence")
    for mask in (3, 5, 6, 7):
        vector = walsh[mask]
        check(moment(vector) == (0, 0, 0, 0), "nullspace basis")
        for matrix in rotations:
            check(moment(transform(vector, matrix)) == (0, 0, 0, 0), "gate congruence")
            null_cases += 1
        for axis, sign in product(range(3), (-1, 1)):
            check(measure_reset(vector, axis, sign) == (0,) * 8, "reset congruence")
            null_cases += 1

    adaptive_leaves = zero_leaves = 0
    for p in preparations:
        for first, after_minus, after_plus in product(range(3), repeat=3):
            gate = H if (first + after_minus + after_plus) % 2 else PHASE
            pp = transform(p, gate)
            target = (Q(1), *matrix_apply(gate, moment(p)[1:]))
            branches = []
            for s in (-1, 1):
                hp = measure_reset(pp, first, s)
                qp = target_measure(target, first, s)
                next_gate = H if s == -1 else PHASE
                hp = transform(hp, next_gate)
                qp = (qp[0], *matrix_apply(next_gate, qp[1:]))
                second = after_minus if s == -1 else after_plus
                for t in (-1, 1):
                    out = measure_reset(hp, second, t)
                    target_out = target_measure(qp, second, t)
                    check(moment(out) == target_out, "adaptive full branch")
                    record = ((1, first, 1, s), (2, second, 1, t))
                    branches.append((record, out))
                    adaptive_leaves += 1
                    zero_leaves += int(target_out[0] == 0)
            check(len(branches) == 4 and sum(moment(out)[0] for _, out in branches) == 1,
                  "full record normalization")

    # Reset bijection checked by explicit reverse lookup, not author's inverse.
    dilation = 0
    for axis in range(3):
        images = {}
        for source, blank, seed, record in product(range(8), range(8), range(4), range(2)):
            signs = list(S[source])
            other = [a for a in range(3) if a != axis]
            signs[other[0]] = 2 * (seed % 2) - 1
            signs[other[1]] = 2 * (seed // 2) - 1
            label = POS[tuple(signs)]
            image = ((blank + label) % 8, source, seed, record ^ (S[source][axis] == -1))
            check(image not in images, "reset dilation injectivity")
            images[image] = (source, blank, seed, record)
            dilation += 1
        check(len(images) == 512, "global reset dilation onto")

    noreset = []
    for p in correlated:
        noreset.append(tuple(sum(p[i] for i, s in enumerate(S) if (s[0], s[1]) == (x, y))
                             for x, y in product((-1, 1), repeat=2)))
    check(tv(*noreset) == 1, "no-reset hidden correlations leak")
    for p in correlated:
        for x in (-1, 1):
            selected = tuple(2 * p[i] if s[0] == x else 0 for i, s in enumerate(S))
            check(det_density(moment(selected)) == Q(-1, 4), "no-reset positive cone")
    for state in S:
        check(det_density((Q(1), *state)) == Q(-1, 2), "seed exposure positive cone")

    hadamard = moment(transform(distribution(2, -1), H))
    check(hadamard == (1, -1, 0, 0) and det_density(hadamard) == 0, "positive Hadamard")
    # rho_01=(r_x-i r_y)/2, so this is exactly -1/2.
    check(hadamard[1] / 2 == Q(-1, 2), "negative off-diagonal is permitted by new map")

    # Affine span: eight admissible nu reconstruct all forbidden point vectors.
    average = tuple(sum(p[i] for p in nu) / 8 for i in range(8))
    check(average == UNIFORM, "nu average")
    for j, p in enumerate(nu):
        check(tuple(3 * p[i] - 2 * UNIFORM[i] for i in range(8))
              == tuple(int(i == j) for i in range(8)), "affine point reconstruction")
    vertex = (1, -1, 1)
    check(matrix_apply(ROT, vertex)[0] == Q(7, 5), "cube-preserving obstruction")
    # Independent Gaussian-integer conjugation control for diag(2-i,2+i).
    check(2 * 2 + 1 == 5 and (2 * 2 - 1, -2 * 2) == (3, -4), "unitary phase")
    for i in range(3):
        for j in range(3):
            check(sum(ROT[i][k] * ROT[j][k] for k in range(3)) == int(i == j),
                  "proper rotation orthogonality")
    check(ROT[0][0] * ROT[1][1] - ROT[0][1] * ROT[1][0] == 1, "rotation determinant")

    pplus = nu[POS[vertex]]
    pminus = nu[POS[tuple(-x for x in vertex)]]
    source_tv = tv(pplus, pminus)
    targets = []
    for p in (pplus, pminus):
        rx = matrix_apply(ROT, moment(p)[1:])[0]
        targets.append(((1 + rx) / 2, (1 - rx) / 2))
    check(targets == [(Q(11, 15), Q(4, 15)), (Q(4, 15), Q(11, 15))], "rotated X records")
    floor = (tv(*targets) - source_tv) / 2
    check(source_tv == Q(1, 3) and floor == Q(1, 15), "data-processing pair floor")
    largest = Q()
    smallest_error = Q(1)
    optimal_count = 0
    for response in product((0, 1), repeat=8):
        probability = [sum(p[i] * response[i] for i in range(8)) for p in (pplus, pminus)]
        distance = abs(probability[0] - probability[1])
        check(distance <= source_tv, "all deterministic responses contract TV")
        largest = max(largest, distance)
        error = max(abs(probability[i] - targets[i][0]) for i in range(2))
        if error < smallest_error:
            smallest_error, optimal_count = error, 1
        elif error == smallest_error:
            optimal_count += 1
    check(largest == source_tv and smallest_error == floor, "tight pair error")

    target = (Q(3, 5), Q(4, 5), Q())
    max_support = max(moment(p)[1] + moment(p)[2] for p in eigenstates)
    coverage = (target[0] + target[1] - max_support) / 4
    check(coverage == Q(1, 10), "octahedral supporting-facet lower bound")
    closest = (Q(2, 5), Q(3, 5), Q())
    check(sum(closest) == 1 and max(abs(a - b) / 2 for a, b in zip(target, closest)) == coverage,
          "state-coverage bound attained")
    prior = tuple(Q(1, 8) * (1 + target[0] * s[0]) * (1 + target[1] * s[1])
                  * (1 + target[2] * s[2]) for s in S)
    check(min(prior) >= 0 and moment(prior) == (1, *target), "enlarged ball state coverage")

    print(json.dumps({
        "schema": "oi-operational-quotient-v3-review-1",
        "author_commit": "fb0f799d94b621cdb82a8e06183f07afc070f14c",
        "verdict": "ACCEPT_WITHIN_SCOPE",
        "blockers": [],
        "independent_priors": len(preparations),
        "independent_projector_branches": local,
        "proper_signed_permutations": len(rotations),
        "kernel_congruence_checks": null_cases,
        "all_depth_two_axis_policies_per_prior": 27,
        "adaptive_full_record_leaves": adaptive_leaves,
        "zero_mass_adaptive_leaves_retained": zero_leaves,
        "global_dilation_cases": dilation,
        "no_reset_full_record_tv": "1",
        "hadamard_offdiagonal": "-1/2",
        "nonclifford_cube_coordinate": "7/5",
        "pair_error_floor": str(floor),
        "deterministic_binary_responses": 256,
        "optimal_deterministic_pair_responses": optimal_count,
        "separate_state_coverage_error": str(coverage),
        "all_controls_pass": True,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
