#!/usr/bin/env python3
"""Strict byte-level replay for SUBSTATE-2 NATIVE-PADIC-1.

Recompute exact finite regression in normal and -O Python; check pinned
Git blobs and exact structured output, never infer an infinite theorem
from finite enumeration.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

SOURCE_BLOB = "03499afca26c46be1f0d84952f7aee4c8be8f9ce"
RESULT_BLOB = "e19da95e2a2b2a757ac8cab732774fcd85101daa"


def require(ok, label):
    if not ok:
        raise RuntimeError(label)


def blob_hash(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def main():
    here=Path(__file__).resolve().parent
    script=here/"native_padic_probe.py"
    result=here/"RESULTS.json"
    source=script.read_bytes()
    expected=result.read_bytes()
    require(blob_hash(source)==SOURCE_BLOB, "source changed")
    require(blob_hash(expected)==RESULT_BLOB, "expected results changed")
    data=json.loads(expected)
    require(data["status"]=="PASS_NATIVE_CONGRUENCE_NO_BACKFLOW", "not verified")
    require(data["controls"]==9344, "control count")
    require(len(data["stages"])==6, "stage count")
    require(data["native_deeper_digit_can_change_low_bit"] is False, "scope mismatch")
    require(data["non_native_positive_control"]=="fixed bit1-to-bit0 reversible source-site kick", "positive control missing")
    for flag in ["general_nonlinear_padic_readouts_excluded",
                 "native_Y_or_intervention_sourcing_derived",
                 "quantum_operational_completion_derived",
                 "Yang_Mills_action_derived"]:
        require(data[flag] is False, "overclaim "+flag)
    for optimized in (False, True):
        cmd=[sys.executable,"-I","-B"]+ (["-O"] if optimized else []) + [str(script)]
        x=subprocess.run(cmd,capture_output=True,check=False)
        require(x.returncode==0 and not x.stderr and x.stdout==expected,
                "native-padic replay failed for optimized="+str(optimized))
    print(json.dumps({
        "status":"PASS_NATIVE_PADIC_REPLAY",
        "normal_and_optimized":"BYTE_IDENTICAL",
        "source_git_blob":SOURCE_BLOB,
        "results_git_blob":RESULT_BLOB,
        "finite_checks":data["controls"],
        "all_state_algebraic_proof_from_replay":False,
        "physical_OI_padic_premise_derived":False
    },indent=2,sort_keys=True))


if __name__=="__main__": main()
