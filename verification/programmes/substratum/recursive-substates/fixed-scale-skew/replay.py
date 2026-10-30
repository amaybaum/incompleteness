#!/usr/bin/env python3
"""Byte-exact, normal/optimized replay of SUBSTATE-2 FIXED-SCALE-1."""
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

SOURCE_SHA256 = "524c599e89282f7d1d9e95f60f1a36d4cff630afdac464cbea3057276bf39f8c"
RESULT_SHA256 = "48e54a1be614627424bc18286d2889dcf366bbbb1f20df91cf7205362d48af7b"


def require(cond, description):
    if not cond:
        raise RuntimeError(description)


def main():
    root = Path(__file__).resolve().parent
    script = root / "fixed_scale_probe.py"
    expected = root / "RESULTS.json"
    source_bytes = script.read_bytes()
    data = expected.read_bytes()
    require(sha256(source_bytes).hexdigest() == SOURCE_SHA256, "source digest changed")
    require(sha256(data).hexdigest() == RESULT_SHA256, "expected result digest changed")
    parsed = json.loads(data)
    require(parsed["status"] == "PASS_FIXED_RULE_CLASSICAL_MEMORY_CONTROL", "not PASS")
    require(len(parsed["finite_stages"]) == 7, "stage count")
    require(all(x["predictive_conditional_memory_bits"] == 1 and
                x["no_feedback_conditional_memory_bits"] == 0
                for x in parsed["finite_stages"]), "memory controls")
    require(parsed["infinite_mathematical_prediction"]["P_divisible"] is True,
            "unexpected rooted scope")
    for key in ("native_OI_update_derived", "quantum_interference_derived",
                "Yang_Mills_action_derived", "physical_log_periodicity_derived",
                "finite_boundary_entropy_derived"):
        require(parsed[key] is False, "overclaim in recorded result: " + key)
    for optimized in (False, True):
        cmd = [sys.executable, "-I", "-B"] + (["-O"] if optimized else []) + [str(script)]
        result = subprocess.run(cmd, capture_output=True, check=False)
        require(result.returncode == 0 and not result.stderr and result.stdout == data,
                "replay failed in optimized="+str(optimized))
    print(json.dumps({"status": "PASS_FIXED_SCALE_EXACT_REPLAY",
                      "normal_and_optimized": "BYTE_IDENTICAL",
                      "finite_full_state_sizes": [x["full_states"] for x in parsed["finite_stages"]],
                      "source_sha256": SOURCE_SHA256,
                      "result_sha256": RESULT_SHA256,
                      "topological_and_physical_theorems_inferred_from_execution": False},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
