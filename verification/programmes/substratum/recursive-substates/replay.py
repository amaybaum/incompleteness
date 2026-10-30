#!/usr/bin/env python3
"""Reproduce SUBSTATE-2 exact JSON with ordinary and optimized Python.

Local deterministic evidence only; no GitHub CI claim, Lean certificate,
physical OI model or independent scientific review is inferred.
"""
from pathlib import Path
from hashlib import sha256
import json
import subprocess
import sys


def main():
    directory = Path(__file__).resolve().parent
    script = directory / "recursive_controls.py"
    expected_path = directory / "RESULTS.json"
    expected = expected_path.read_bytes()
    baseline = json.loads(expected)
    assert baseline["status"] == "PASS_EXACT_FINITE_CONTROLS"
    assert baseline["A"]["status"] == "PASS_NEGATIVE_CONTROL"
    assert baseline["B1"]["status"] == "PASS_FEEDBACK_ROOTED_INDIVISIBLE"
    assert baseline["B2"]["status"] == "PASS_SHIFT_CONVEYOR"
    assert baseline["C"]["status"] == "PASS_KINEMATICS_ACTION_NOT_SELECTED"
    assert not baseline["operational_QM_derived"]
    assert not baseline["YM_action_derived"]
    assert not baseline["log_periodic_signal_derived"]

    results = []
    for optimized in (False, True):
        cmd = [sys.executable, "-I", "-B"]
        if optimized:
            cmd.append("-O")
        cmd.append(str(script))
        run = subprocess.run(cmd, check=False, capture_output=True)
        if run.returncode or run.stderr or run.stdout != expected:
            raise RuntimeError(
                f"SUBSTATE-2 replay failure, optimized={optimized}, "
                f"returncode={run.returncode}, stderr={run.stderr[:1000]!r}, "
                f"exact_match={run.stdout == expected}")
        results.append({"optimized": optimized, "exit_code": run.returncode,
                        "exact_output_match": True})

    print(json.dumps({
        "status": "PASS_EXACT_REPLAY",
        "script_sha256": sha256(script.read_bytes()).hexdigest(),
        "results_sha256": sha256(expected).hexdigest(),
        "runs": results,
        "proof_scope": "finite enumerations only; infinite-limit theorems written separately",
        "native_OI_dynamics_derived": False,
        "quantum_operational_completion_derived": False,
        "Yang_Mills_action_derived": False,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
