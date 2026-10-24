#!/usr/bin/env python3
"""Bounded exact controls for the stopping-time candidate in REPORT.md."""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import argparse
import json


def require(test, label):
    if not test:
        raise RuntimeError(label)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    return a[0] * b[0] + 2 * a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def scale(r, a):
    return r * a[0], r * a[1]


def div(a, b):
    denominator = b[0] * b[0] - 2 * b[1] * b[1]
    require(denominator != 0, "division by zero")
    return scale(1 / denominator, mul(a, (b[0], -b[1])))


def sign(a):
    x, y = a
    if not x:
        return (y > 0) - (y < 0)
    if not y or x * y > 0:
        return (x > 0) - (x < 0)
    d = x * x - 2 * y * y
    return ((d > 0) - (d < 0)) * ((x > 0) - (x < 0))


def pair(a):
    return [str(a[0]), str(a[1])]


def floor_p(depth):
    n = 2 ** depth
    return 0 if depth == 0 else n // 2 + isqrt(2 * n * n) // 4


def bits(seed, depth):
    return tuple((seed >> j) & 1 for j in range(depth - 1, -1, -1))


def sampler(random_bits, target_bits, flip=False):
    for t, (u, p) in enumerate(zip(random_bits, target_bits), 1):
        if u != p:
            return t, p ^ flip
    return "timeout", "timeout"


def interval_classification(random_bits, p):
    """Independent branch test: compare the whole dyadic interval with p."""
    prefix = 0
    for depth, bit in enumerate(random_bits, 1):
        prefix = 2 * prefix + bit
        lo, hi = F(prefix, 2 ** depth), F(prefix + 1, 2 ** depth)
        if sign(add(p, (-hi, F(0)))) > 0:
            return depth, 1
        if sign(add((lo, F(0)), scale(-1, p))) > 0:
            return depth, 0
    return "timeout", "timeout"


def tv(counts_a, counts_b, denominator):
    return sum(abs(counts_a[k] - counts_b[k]) for k in counts_a.keys() | counts_b.keys()) / F(2 * denominator)


def matmul(a, b):
    return tuple(sum(a[2 * i + k] * b[2 * k + j] for k in range(2)) for i in range(2) for j in range(2))


def transpose(a):
    return a[0], a[2], a[1], a[3]


def run():
    p = (F(1, 2), F(1, 4))
    q = (F(1, 2), F(-1, 4))
    require(add(p, q) == (1, 0), "complement control")
    require(sign((F(1), F(-1))) < 0 and sign((F(3, 2), F(-1))) > 0, "Q(sqrt2) sign control")
    require(mul(p, div((F(1), F(0)), p)) == (1, 0), "Q(sqrt2) quotient control")
    depths = []
    compared = 0
    for depth in range(1, 13):
        n = 2 ** depth
        p_bits = tuple(floor_p(t) - 2 * floor_p(t - 1) for t in range(1, depth + 1))
        q_bits = tuple(1 - bit for bit in p_bits)
        law_p, law_q = Counter(), Counter()
        mutant_rejections = 0
        for seed in range(n):
            random_bits = bits(seed, depth)
            a, b = sampler(random_bits, p_bits), sampler(random_bits, q_bits)
            expected_a = interval_classification(random_bits, p)
            expected_b = interval_classification(random_bits, q)
            require(a == expected_a and b == expected_b, "digit/interval methods disagree")
            law_p[a] += 1
            law_q[b] += 1
            compared += 2
            mutant_rejections += sampler(random_bits, p_bits, flip=True) != expected_a
        require(mutant_rejections == n - 1, "flipped-output mutant not rejected on every halt")
        require(law_p["timeout", "timeout"] == law_q["timeout", "timeout"] == 1, "tail count")
        t_p, t_q, y_p, y_q = Counter(), Counter(), Counter(), Counter()
        for law, times, outcomes in ((law_p, t_p, y_p), (law_q, t_q, y_q)):
            for (t, y), count in law.items():
                times[t] += count
                outcomes[y] += count
        require(t_p == t_q, "timing marginals differ")
        for t in range(1, depth + 1):
            require(t_p[t] == 2 ** (depth - t), "geometric stopping mass")
            require(law_p[t, p_bits[t - 1]] == t_p[t], "joint p law")
            require(law_q[t, q_bits[t - 1]] == t_q[t], "joint q law")
        distance = tv(law_p, law_q, n)
        require(distance == 1 - F(1, n), "joint total variation")
        require(tv(t_p, t_q, n) == 0, "time total variation")
        require(y_p[1] == floor_p(depth), "success prefix mass")
        require(sign(add(p, (-F(y_p[1], n), F(0)))) > 0, "truncated p below target")
        require(sign(add((F(y_p[1] + 1, n), F(0)), scale(-1, p))) > 0, "truncated error bound")
        # Timeout replaced by0: an actual bounded-output approximation.
        clipped_expected_queries = sum(F(t * count, n) for t, count in t_p.items() if t != "timeout") + F(depth, n)
        require(clipped_expected_queries == 2 - F(2, n), "truncated expected query cost")
        depths.append({"cutoff": depth, "prefixes_per_threshold": n,
                       "timeout_probability": str(F(1, n)),
                       "joint_TY_total_variation": str(distance),
                       "time_marginal_total_variation": "0",
                       "p_truncated_output1_probability": str(F(y_p[1], n)),
                       "expected_min_T_cutoff": str(clipped_expected_queries)})

    # For public T=1,Y=1, p's threshold gives1/2; q's gives0.
    kappa_p = div((F(1, 2), F(0)), p)
    kappa_q = (F(0), F(0))
    require(sign(kappa_p) > 0 and kappa_p != kappa_q, "state-independent refinement mutant accepted")
    # Positive countercontrol: an abstract independently generated T has the same factor1/2.
    independent_p = div(scale(F(1, 2), p), p)
    independent_q = div(scale(F(1, 2), q), q)
    require(independent_p == independent_q == (F(1, 2), F(0)), "refinement positive control")

    partial_permutations = []
    for entries in product((0, 1), repeat=4):
        a, b, c, d = entries
        if a + b <= 1 and c + d <= 1 and a + c <= 1 and b + d <= 1:
            partial_permutations.append(entries)
    require(len(partial_permutations) == 7, "qubit partial-permutation census including zero")
    images = []
    for a, b, c, d in partial_permutations:
        # P |1><1| P^T = outer product of second column.
        image = (b * b, b * d, b * d, d * d)
        require(image == matmul(matmul((a, b, c, d), (0, 0, 0, 1)), transpose((a, b, c, d))), "column/product cross-check")
        require(image[1] == image[2] == 0 and all(v >= 0 for v in image), "cone witness escaped")
        images.append(image)
    # Hadamard positive control: (1/sqrt2)*[[1,1],[1,-1]].
    h_numerator = (1, 1, 1, -1)
    require(matmul(h_numerator, transpose(h_numerator)) == (2, 0, 0, 2), "Hadamard unitary normalization")
    h_input_image = tuple(F(v, 2) for v in matmul(matmul(h_numerator, (0, 0, 0, 1)), transpose(h_numerator)))
    require(h_input_image[1] < 0 and sum((h_input_image[0], h_input_image[3])) == 1, "non-native positive control")
    # The input matrix has norm1; every cone image differs by at least1/2 in this entry.
    require(all(abs(image[1] - h_input_image[1]) >= F(1, 2) for image in images), "entry separation")
    return {
        "schema": "oi-stopping-candidate-v2",
        "verdict": "PASS",
        "scope": "abstract almost-sure sampler and fixed-identification controls; not native implementation",
        "exact_parameters": {"p": pair(p), "complement": pair(q), "coefficient_basis": ["1", "sqrt(2)"]},
        "prefix_comparisons": compared,
        "cutoffs": depths,
        "written_limit_claims": {"eventual_output1_probability": "(2+sqrt(2))/4",
                                 "expected_coin_queries": "2", "zero_probability_nontermination": True,
                                 "joint_TY_total_variation": "1", "output_Y_total_variation": "sqrt(2)/2",
                                 "time_T_total_variation": "0", "finite_enumeration_is_not_limit_proof": True},
        "refinement_controls": {"candidate_kappa_Y1_T1_at_p": pair(kappa_p),
                                "candidate_kappa_Y1_T1_at_complement": pair(kappa_q),
                                "common_kappa_rejected": True, "independent_time_positive_control": pair(independent_p)},
        "fixed_G3_cone_controls": {"partial_permutations_including_zero": len(partial_permutations),
                                   "all_offdiagonal_entries_zero": True,
                                   "Hadamard_negative_entry": "-1/2", "operator_norm_gap_lower_bound": "1/2"},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    data = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(data)
    else:
        print(data, end="")
