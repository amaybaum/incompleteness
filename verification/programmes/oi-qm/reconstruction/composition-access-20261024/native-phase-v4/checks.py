#!/usr/bin/env python3
"""Exact local native-boundary controls; no original-time reachability claim."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json


H_TABLE = (0, 2, 4, 7, 1, 3, 5, 6)
Q8 = (0, 0, 0)
Q9 = (0, 0, 1)
OTHER_NEIGHBORS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0),
                   (0, -1, 0), (0, 0, -1))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def bits(code):
    return (code >> 2 & 1, code >> 1 & 1, code & 1)


def code(a, b, d):
    return 4 * a + 2 * b + d


def h_boolean(value):
    a, b, d = bits(value)
    return code(b, d, a ^ (b & d))


def native_next(previous, current, site=Q8):
    parity = 0
    for axis in range(3):
        for direction in (-1, 1):
            neighbor = list(site)
            neighbor[axis] += direction
            parity ^= current.get(tuple(neighbor), 0)
    return previous.get(site, 0) ^ H_TABLE[parity]


def formula(y, x, r, c):
    ca, cb, cd = bits(c)
    return code(cb ^ x, y ^ cd ^ r, ca ^ ((cb ^ x) & (cd ^ r)))


def tv(left, right):
    return sum((abs(left.get(k, 0) - right.get(k, 0))
                for k in left.keys() | right.keys()), F()) / 2


def encode_q9(old_x, y, a, b):
    if (a, b) == (0, 1):
        old_u = old_x ^ y
        return code(old_u, y, old_x & (1 ^ old_u))
    return code(0, y ^ a, y ^ b)


def source_laws(y, mode):
    """256 worlds incl duplicated unused control bit, conditioned on old y.

    The boundary completions set only the current five-neighbor XOR C.
    They are not claimed to arise from the old original-time apparatus.
    """
    selected, public, joint, failure = (defaultdict(F) for _ in range(4))
    for old_x, a, b, k0, k1, k2, z, extra in product((0, 1), repeat=8):
        probability = F(1, 256)
        k = k0 + 2 * k1 + 4 * k2
        g = k < {(0, 0): 5, (0, 1): 0, (1, 0): 3, (1, 1): 2}[a, b]
        raw = encode_q9(old_x, y, a, b)
        selected[g, old_x, y, raw, z] += probability
        if not g:
            # Optional whole-q9 failure metadata and physical failed fields
            # are retained. No next observation or qubit carrier is offered.
            key = ("terminal-failure", old_x, y, raw, None)
            public[key] += probability
            joint[key] += probability
            failure[old_x, y, raw, z, None] += probability
            continue
        _, x, r = bits(raw)
        ca = {"zero": 0, "flip-A": 1, "fresh": extra,
              "correlated": z ^ (x & r)}[mode]
        c = code(ca, 0, 0)
        current = {Q9: raw, OTHER_NEIGHBORS[0]: c}
        out = native_next({Q8: code(0, y, 0)}, current)
        record = ("success", old_x, y, raw, out)
        public[record] += probability
        # The old current Z field remains in the next previous slice.
        # This is a joint record/selected-field test, not a new public read.
        joint[record, z] += probability
    return selected, public, joint, failure


def normalized_success(law):
    kept = {key: value for key, value in law.items()
            if (key[0] if isinstance(key[0], str) else key[0][0]) == "success"}
    mass = sum(kept.values(), F())
    require(mass == F(5, 16), "success mass changed")
    return {key: value / mass for key, value in kept.items()}


def sign(bit):
    return 1 - 2 * bit


def moments(law):
    return (sum(law.values(), F()),
            *(sum((weight * sign(point[index]) for point, weight in law.items()), F())
              for index in (0, 1, 3)))


def post_x(x):
    out = defaultdict(F)
    for (a, b), count in (((0, 0), 5), ((1, 0), 4), ((1, 1), 1)):
        for z in (0, 1):
            out[x, x ^ a, x ^ b, z] += F(count, 20)
    return out


def kappa(y, x, r):
    if x == y:
        return F(int(r == y))
    return F(3, 5) if r == y else F(2, 5)


def main():
    for value in range(8):
        require(h_boolean(value) == H_TABLE[value], "H lookup not native")
    local_cases = 0
    omitted_neighbor_mutants = 0
    old_slice_mutants = 0
    distant_controls = 0
    for y, x, r in product((0, 1), repeat=3):
        for c in range(8):
            decompositions = []
            for chosen in range(5):
                decompositions.append(tuple(c if i == chosen else 0 for i in range(5)))
            for split in range(8):
                decompositions.append((split, c ^ split, 0, 0, 0))
            for decomposition in decompositions:
                current = dict(zip(OTHER_NEIGHBORS, decomposition))
                current[Q9] = code(0, x, r)
                previous = {Q8: code(0, y, 0)}
                actual = native_next(previous, current)
                require(actual == formula(y, x, r, c), "response formula mismatch")
                distant = dict(current)
                distant[(3, 0, 0)] = 7
                require(native_next(previous, distant) == actual,
                        "outside one-step cone changed output")
                distant_controls += 1
                omitted_neighbor_mutants += int(actual != formula(y, x, r, 0))
                old_slice_mutants += int(actual != native_next({}, current))
                local_cases += 1
    require(omitted_neighbor_mutants > 0 and old_slice_mutants > 0,
            "negative controls are vacuous")

    bounded = {}
    invariant_controls = 0
    for y in (0, 1):
        laws = {mode: source_laws(y, mode)
                for mode in ("zero", "flip-A", "fresh", "correlated")}
        base_selected, _, _, base_failure = laws["zero"]
        for selected, public, joint, failure in laws.values():
            require(selected == base_selected, "selected preparation changed")
            require(failure == base_failure, "failure physical fields changed")
            require(sum(public.values(), F()) == 1 and sum(joint.values(), F()) == 1,
                    "full law not normalized")
        zero, flip = laws["zero"][1], laws["flip-A"][1]
        require(tv(zero, flip) == F(5, 16), "native complement TV wrong")
        require(tv(normalized_success(zero), normalized_success(flip)) == 1,
                "conditional native complement TV wrong")
        fresh_public, fresh_joint = laws["fresh"][1:3]
        correlated_public, correlated_joint = laws["correlated"][1:3]
        require(fresh_public == correlated_public, "matching next-record control failed")
        require(tv(fresh_joint, correlated_joint) == F(5, 32),
                "joint retained-Z TV wrong")
        require(tv(normalized_success(fresh_joint), normalized_success(correlated_joint)) == F(1, 2),
                "conditional joint retained-Z TV wrong")
        # Different current hidden neighbor decompositions with the same C
        # give the same whole next-q8 record on every successful raw value.
        for a, b in ((0, 0), (1, 0), (1, 1)):
            x, r = y ^ a, y ^ b
            for c in range(8):
                ref = formula(y, x, r, c)
                for g in range(8):
                    current = {Q9: code(0, x, r), OTHER_NEIGHBORS[0]: g,
                               OTHER_NEIGHBORS[1]: g ^ c}
                    require(native_next({Q8: code(0, y, 0)}, current) == ref,
                            "equal relevant parity did not lump")
                    invariant_controls += 1
        bounded[str(y)] = {
            "C_A_flip_success_conditioned_record_tv": "1",
            "C_A_flip_full_record_tv": "5/16",
            "fresh_correlated_next_public_record_tv": "0",
            "fresh_correlated_joint_previous_Z_success_tv": "1/2",
            "fresh_correlated_joint_previous_Z_full_tv": "5/32",
        }

    # Law-level positive control: preserve the actual whole-q9 record and
    # independently sample the calibrated post-X family. This is not native.
    reset_branches = 0
    reset_cells = 0
    post_read_determinants = set()
    for y in (0, 1):
        for (x, r), count in (((y, y), 5), ((y ^ 1, y), 3), ((y ^ 1, y ^ 1), 2)):
            branch_mass = F(count, 10)
            require(branch_mass == F(1, 2) * kappa(y, x, r), "whole-port refinement wrong")
            output = post_x(x)
            require(moments(output) == (F(1), F(sign(x)), F(0), F(0)),
                    "positive reset is not X eigenstate")
            require(sum((w * sign(j[2]) for j, w in output.items()), F()) == F(4, 5) * sign(x),
                    "post-X R calibration wrong")
            require(sum(output.values(), F()) * branch_mass == branch_mass,
                    "reset branch mass changed")
            # Unchanged phase after the whole port fixes X and old Y.
            determinant = (F(1) - sign(x) ** 2 - sign(y) ** 2) / 4
            post_read_determinants.add(determinant)
            require(determinant < 0, "unchanged sample positivity mutant missed")
            reset_branches += 1
            reset_cells += len(output)

    result = {
        "schema": "oi-native-phase-composition-v4-1",
        "scope": "local-native-boundary-controls-and-conditional-contract",
        "original_time_reachability_of_local_completions_claimed": False,
        "native_update_cases": local_cases,
        "distant_field_controls": distant_controls,
        "omitted_neighbor_mutant_mismatches": omitted_neighbor_mutants,
        "dropped_old_slice_mutant_mismatches": old_slice_mutants,
        "equal_parity_unequal_hidden_completion_controls": invariant_controls,
        "per_y": bounded,
        "abstract_fresh_post_X_reset_branches": reset_branches,
        "abstract_fresh_post_X_reset_cells": reset_cells,
        "unchanged_post_read_determinants": sorted(map(str, post_read_determinants)),
        "all_controls_pass": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
