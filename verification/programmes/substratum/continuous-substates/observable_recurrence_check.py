#!/usr/bin/env python3
"""SUBSTATE-1 exact algebra regression for the all-L proof.

This finite range is a sanity check, NOT a proof of the universal L statement
in observable-recurrence.md. It reuses the integer wave matrix from the pinned
free-map probe, and prints PASS only if every positive and countercontrol passes.
"""
import json

from wave_torus_probe import mat_mul, mat_pow, row_mul, unit, wave_matrix


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
        assert any(any(row) for row in M), ("zero M", L)
        assert not any(any(row) for row in mat_mul(M, M)), ("M^2", L)
        assert any(row_mul(site, M)), ("site countercontrol", L)

        # Proposed recurrent observables annihilate both parabolic modes.
        assert not any(row_mul(d2, M)), ("distance-two return", L)
        assert row_mul(d2, F)[L:] == [-x for x in d2[:L]], ("time-one", L)
        if L % 2:
            assert not any(row_mul(d1, M)), ("odd nearest return", L)
            counts["odd_difference_controls"] += 1
        else:
            assert any(row_mul(d1, M)), ("even nearest countercontrol", L)
            counts["even_difference_countercontrols"] += 1
        counts["ring_sizes"] += 1

    # No verdict is printed when an assertion has failed.
    return {"controls": counts, "status": "PASS", "scope": "exact finite L=3..20 only"}


if __name__ == "__main__":
    print(json.dumps(checked(), indent=2, sort_keys=True))
