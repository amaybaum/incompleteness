#!/usr/bin/env python3
"""SUBSTATE-1 exact algebra regression for the all-L proof.

This finite range is a sanity check, NOT a proof of the universal L statement
in observable-recurrence.md. It reuses the integer wave matrix from the pinned
free-map probe, and prints PASS only if every positive and countercontrol passes.
"""
import json
import sys
from pathlib import Path

# Python -I omits the script directory from sys.path; import this pinned sibling explicitly.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from wave_torus_probe import mat_mul, mat_pow, row_mul, unit, wave_matrix


def require(condition, reason):
    if not condition:  # Unlike bare assert, survives Python -O.
        raise AssertionError(reason)


def checked():
    counts = {"ring_sizes": 0, "odd_difference_controls": 0,
              "even_difference_countercontrols": 0}
    for L in range(3, 21):
        n = 2 * L
        F = wave_matrix(L)
        M = [[v - int(i == j) for j, v in enumerate(row)]
             for i, row in enumerate(mat_pow(F, L))]
        site = unit(n, 0)
        d1 = [a - b for a, b in zip(site, unit(n, 1))]
        d2 = [a - b for a, b in zip(site, unit(n, 2))]

        # Structural controls and an observable that fails to annihilate M.
        require(any(any(row) for row in M), ("zero M", L))
        require(not any(any(row) for row in mat_mul(M, M)), ("M^2", L))
        require(any(row_mul(site, M)), ("site countercontrol", L))

        # Proposed recurrent observables annihilate both parabolic modes.
        require(not any(row_mul(d2, M)), ("distance-two return", L))
        require(row_mul(d2, F)[L:] == [-x for x in d2[:L]], ("time-one", L))
        if L % 2:
            require(not any(row_mul(d1, M)), ("odd nearest return", L))
            counts["odd_difference_controls"] += 1
        else:
            require(any(row_mul(d1, M)), ("even nearest countercontrol", L))
            counts["even_difference_countercontrols"] += 1
        counts["ring_sizes"] += 1

    # No verdict is printed when an assertion has failed.
    return {"controls": counts, "status": "PASS", "scope": "exact finite L=3..20 only"}


if __name__ == "__main__":
    print(json.dumps(checked(), indent=2, sort_keys=True))
