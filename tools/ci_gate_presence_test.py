#!/usr/bin/env python3
"""ci_gate_presence_test.py - does CI actually run the release gate?

The release gate exists because individually green subsystems have let defects
through before. That argument only holds if CI runs the gate. For a long time it
did not: the workflow had a Lean kernel job, a Mathlib bridge job and a probes
job, and none of them invoked `tools/release_gate.py`. "All checks green"
therefore said nothing about voice, claims, coverage, staleness or the
manuscript census - and a voice_check scope defect reached main underneath three
green checks.

This is the control for that. It asserts the workflow invokes the real gate, by
its real path, and it is written so that DELETING the gate step from verify.yml
makes this test fail. A presence check that cannot fail when the thing is absent
is not a control.

It deliberately does not accept a re-implementation: the step must call
`tools/release_gate.py`, not a hand-rolled subset of its checks, because a
second partial implementation drifts from the gate it stands in for.

Usage:  python3 tools/ci_gate_presence_test.py
Exit 1 if CI does not invoke the release gate.
"""
import os
import sys

WORKFLOW = os.path.join(".github", "workflows", "verify.yml")
NEEDLE = "tools/release_gate.py"


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(root, WORKFLOW)
    if not os.path.exists(path):
        print(f"  FAIL {WORKFLOW} is missing entirely")
        print("\nci_gate_presence_test: FAILED (no workflow to check)")
        return 1
    text = open(path, encoding="utf-8").read()

    problems = []
    if NEEDLE not in text:
        problems.append(
            f"{WORKFLOW} never invokes {NEEDLE}; CI green would then say "
            f"nothing about the gate checks")
    else:
        # The invocation must be a real run step, not a mention in a comment.
        live = [ln for ln in text.splitlines()
                if NEEDLE in ln and not ln.strip().startswith("#")]
        if not live:
            problems.append(
                f"{NEEDLE} appears in {WORKFLOW} only inside comments; a "
                f"commented-out gate is not a gate")

    gate = os.path.join(root, "tools", "release_gate.py")
    if not os.path.exists(gate):
        problems.append("tools/release_gate.py does not exist to be run")

    for p in problems:
        print(f"  FAIL {p}")
    if problems:
        print(f"\nci_gate_presence_test: FAILED ({len(problems)} problem(s))")
        return 1
    print("  OK   .github/workflows/verify.yml invokes tools/release_gate.py "
          "as a live step")
    print("\nci_gate_presence_test: OK (CI runs the real release gate)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
