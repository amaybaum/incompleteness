#!/usr/bin/env python3
"""Independent exact review controls; imports no author implementation."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
import json


def require(condition, name):
    if not condition:
        raise RuntimeError(name)


def distance(left, right):
    return sum((abs(left.get(k, 0)-right.get(k, 0))
                for k in set(left) | set(right)), Q()) / 2


def project(law, f):
    out = defaultdict(Q)
    for key, mass in law.items():
        out[f(key)] += mass
    return dict(out)


RECORDS = ((0, -1), (1, 0), (1, 1))


def circuit(q, g, setting, atom):
    # Sixteen equiprobable atoms, four failure and twelve success atoms.
    if atom < 4:
        return (0, -1), q, 1-g
    coin = (atom-4)//3
    output = (q, 1-q, coin & 1)[setting]
    return (1, output), output, g ^ q ^ (setting & 1) ^ (coin >> 1)


def ideal_edges(q, setting):
    # Independent classical transition matrix on the diagonal qubit sector.
    yield (0, -1), q, Q(1, 4)
    weights = ((1-q, q), (q, 1-q), (Q(1, 2), Q(1, 2)))[setting]
    for output, prob in enumerate(weights):
        if prob:
            yield (1, output), output, Q(3, 4)*prob


def run():
    local = 0
    for q, g, setting in product(range(2), range(2), range(3)):
        actual = Counter()
        for atom in range(16):
            record, output, _ = circuit(q, g, setting, atom)
            actual[(record, output)] += 1
        actual = {key: Q(count, 16) for key, count in actual.items()}
        ideal = {(record, output): mass for record, output, mass in ideal_edges(q, setting)}
        require(actual == ideal, "independent local matrix")
        local += 1
    cases = 0
    for initial_q, initial_g in product(range(2), repeat=2):
        for policy in product(range(3), repeat=4):
            actual = Counter()
            for atom1, atom2 in product(range(16), repeat=2):
                r1, q1, g1 = circuit(initial_q, initial_g, policy[0], atom1)
                a2 = policy[1+RECORDS.index(r1)]
                r2, q2, _ = circuit(q1, g1, a2, atom2)
                actual[(r1, r2, q2)] += 1
            actual = {key: Q(count, 256) for key, count in actual.items()}
            ideal = defaultdict(Q)
            for r1, q1, mass1 in ideal_edges(initial_q, policy[0]):
                for r2, q2, mass2 in ideal_edges(q1, policy[1+RECORDS.index(r1)]):
                    ideal[(r1, r2, q2)] += mass1*mass2
            require(actual == dict(ideal), "full adaptive branch table")
            cases += 1

    # Compute each comparison from raw equiprobable atoms, not expected TVs.
    fair2 = {(a, b): Q(1, 4) for a, b in product(range(2), repeat=2)}
    diagonal = {(0, 0): Q(1, 2), (1, 1): Q(1, 2)}
    require(project(fair2, lambda p: p[0]) == project(diagonal, lambda p: p[0]), "first marginal")
    require(project(fair2, lambda p: p[1]) == project(diagonal, lambda p: p[1]), "second marginal")
    joint_tv = distance(fair2, diagonal)
    require(joint_tv == Q(1, 2), "joint correlation control")
    xor_tv = distance(project(diagonal, lambda p: p[0]^p[1]), {0: Q(1, 2), 1: Q(1, 2)})
    require(xor_tv == Q(1, 2), "herald-conditioned hidden correlation")
    calibration = []
    for y in range(2):
        laws = []
        for population in ([(0,0)]*5+[(1,0)]*3+[(1,1)]*2,
                           [(0,0)]*5+[(1,0)]*2+[(1,1)]*3):
            counts = Counter((y^a, y, y^b, z) for a, b in population for z in range(2))
            laws.append({key: Q(count, 20) for key, count in counts.items()})
        x_tv = distance(*(project(law, lambda c:c[0]) for law in laws))
        r_tv = distance(*(project(law, lambda c:c[2]) for law in laws))
        carrier_tv = distance(*laws)
        require((x_tv, r_tv, carrier_tv) == (0, Q(1,10), Q(1,10)), "calibration diagnostics")
        calibration.append([str(x_tv), str(r_tv), str(carrier_tv)])
    failure_tv = distance({0: Q(1,2), 1: Q(1,2)}, {0: Q(1,4), 1: Q(3,4)})
    require(failure_tv == Q(1,4), "failure mass")
    access_tv = distance({0: Q(1)}, {1: Q(1)})
    require(access_tv == 1, "access extension")

    # Controller settings have the same marginal, but correlation with q changes
    # which input ensemble each setting acts on. This necessitates the qualifier.
    correlated_controller = {(q, q ^ q): Q(1,2) for q in range(2)}
    independent_controller = {(a, q ^ a): Q(1,4) for q, a in product(range(2), repeat=2)}
    controller_tv = distance(correlated_controller, independent_controller)
    require(controller_tv == Q(1,2), "controller conditional independence")
    return {
        "schema": "oi-composition-separate-author-review-v1",
        "imports_author_code": False,
        "local_matrix_cases": local,
        "complete_two_stage_policy_cases": cases,
        "physical_seed_pairs_per_case": 256,
        "joint_marginal_tv": str(joint_tv),
        "herald_hidden_correlation_tv": str(xor_tv),
        "calibration_x_r_carrier_tv_by_y": calibration,
        "failure_mass_tv": str(failure_tv),
        "expanded_access_tv": str(access_tv),
        "correlated_controller_tv": str(controller_tv),
        "controls_passed": True,
        "scope": "exact toy diagnostics; written theorem reviewed separately",
    }


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True, indent=2))
