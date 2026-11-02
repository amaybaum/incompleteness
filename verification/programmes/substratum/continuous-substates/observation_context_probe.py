#!/usr/bin/env python3
"""Exact reference controls for an ideal two-path/two-port observation experiment.

All probabilities are rational. This is not an OI dynamics model: benchmark
amplitudes are supplied as EXTERNAL quantum/classical-wave reference physics.
Controls distinguish fixed-path classical additivity, classical coherent
wave interference, unobserved path tagging, and conditional erasure.
"""
from fractions import Fraction as Q
import json


def signs(port):
    return (1, 1) if port == 0 else (1, -1)


def one_open(open_path):
    # Incident state has amplitude 1/sqrt(2) in each arm; recombiner adds
    # 1/sqrt(2), so the one-path screen amplitude is +/- 1/2.
    return tuple(Q(signs(port)[open_path] ** 2, 4) for port in (0, 1))


def both_coherent():
    return tuple(Q(sum(signs(port)) ** 2, 4) for port in (0, 1))


def which_way_joint():
    # (screen, recorded path) joint probabilities: 1/4 in each cell.
    return {(port, path): Q(signs(port)[path] ** 2, 4)
            for port in (0, 1) for path in (0, 1)}


def eraser_joint():
    # Two balanced analyzers: amplitude is sum of +/- path contributions,
    # divided by 2 sqrt(2); joint probability is square / 8.
    return {(port, tag): Q(sum(signs(port)[path] * signs(tag)[path]
                              for path in (0, 1)) ** 2, 8)
            for port in (0, 1) for tag in (0, 1)}


def marginal(joint):
    return tuple(sum((v for (port, _), v in joint.items() if port == i),
                     Q(0)) for i in (0, 1))


def vector_json(vector):
    return [str(v) for v in vector]


def main():
    left, right = one_open(0), one_open(1)
    both = both_coherent()
    path = which_way_joint()
    erase = eraser_joint()
    additive = tuple(left[i] + right[i] for i in (0, 1))
    contrast = tuple(both[i] - additive[i] for i in (0, 1))
    uniform = (Q(1, 2), Q(1, 2))
    checks = {
        "same_incident_source_left_unconditional": left == (Q(1, 4), Q(1, 4)),
        "same_incident_source_right_unconditional": right == (Q(1, 4), Q(1, 4)),
        "loss_left_1_over_2": sum(left) == Q(1, 2),
        "loss_right_1_over_2": sum(right) == Q(1, 2),
        "both_coherent_reference": both == (Q(1), Q(0)),
        "classical_fixed_path_additive_countercontrol": additive == uniform,
        # Same supplied amplitude benchmark, not a second independent wave model.
        "classical_wave_reference_matches_coherent_intensity": both == (Q(1), Q(0)),
        "contrast_not_proof_of_unique_quantumness": contrast == (Q(1, 2), Q(-1, 2)),
        "which_path_full_joint": all(p == Q(1, 4) for p in path.values()),
        "unread_marker_screen_uniform": marginal(path) == uniform,
        "complementary_eraser_joint": erase == {(0, 0): Q(1, 2),
                                                (0, 1): Q(0),
                                                (1, 0): Q(0),
                                                (1, 1): Q(1, 2)},
        "eraser_unsorted_screen_uniform": marginal(erase) == uniform,
        "eraser_conditioned_opposite_ports": erase[(0, 0)] == erase[(1, 1)] == Q(1, 2),
        "both_tag_settings_normalized": sum(path.values()) == sum(erase.values()) == 1,
    }
    if not all(checks.values()):
        raise AssertionError({k: v for k, v in checks.items() if not v})
    print(json.dumps({
        "status": "REFERENCE_ONLY_PASS",
        "reference": "ideal externally supplied two-path Born/classical-wave benchmark",
        "controls": checks,
        "both_screen": vector_json(both),
        "left_screen_subnormalized": vector_json(left),
        "right_screen_subnormalized": vector_json(right),
        "fixed_path_additive": vector_json(additive),
        "interference_contrast": vector_json(contrast),
        "which_path_screen": vector_json(marginal(path)),
        "eraser_screen_unsorted": vector_json(marginal(erase)),
        "eraser_joint": {f"{port}{tag}": str(prob)
                         for (port, tag), prob in erase.items()},
        "native_oi_dynamics_proved": False,
        "quantum_uniqueness_proved": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
