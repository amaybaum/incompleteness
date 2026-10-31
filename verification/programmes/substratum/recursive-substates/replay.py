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

SOURCE_SHA256 = "6beb25044fc6966a954adc186d1a136f42fedd78c938c2683983316b886af666"
RESULT_SHA256 = "8b949aa7cbd688f7c41fa079f761424afea98700e387db42c2b15320174e2b64"


def require(cond, description):
    if not cond:
        raise RuntimeError(description)


def main():
    directory = Path(__file__).resolve().parent
    script = directory / "recursive_controls.py"
    expected_path = directory / "RESULTS.json"
    expected = expected_path.read_bytes()
    require(sha256(script.read_bytes()).hexdigest() == SOURCE_SHA256, "source digest changed")
    require(sha256(expected).hexdigest() == RESULT_SHA256, "expected result digest changed")
    baseline = json.loads(expected)
    require(baseline["status"] == "PASS_EXACT_FINITE_CONTROLS", "not PASS")
    require(baseline["A"]["status"] == "PASS_NEGATIVE_CONTROL", "A status")
    require(baseline["B1"]["status"] == "PASS_FEEDBACK_ROOTED_INDIVISIBLE", "B1 status")
    require(baseline["B2"]["status"] == "PASS_SHIFT_CONVEYOR", "B2 status")
    require(baseline["C"]["status"] == "PASS_KINEMATICS_ACTION_NOT_SELECTED", "C status")
    for key in ("operational_QM_derived", "YM_action_derived", "log_periodic_signal_derived"):
        require(baseline[key] is False, "overclaim in recorded result: " + key)

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
        "script_sha256": SOURCE_SHA256,
        "results_sha256": RESULT_SHA256,
        "runs": results,
        "proof_scope": "finite enumerations only; infinite-limit theorems written separately",
        "native_OI_dynamics_derived": False,
        "quantum_operational_completion_derived": False,
        "Yang_Mills_action_derived": False,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
