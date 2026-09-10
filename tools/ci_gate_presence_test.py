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

It also does not accept a mere MENTION of the path. An earlier version of this
test passed on any uncommented line containing `tools/release_gate.py`, so
`echo tools/release_gate.py` inside a `run:` block would have satisfied it while
CI ran no gate at all - a control that cannot fail when the thing is absent. The
test now extracts the `run:` content of the workflow and requires a command line
that actually invokes the gate through an interpreter.

Usage:  python3 tools/ci_gate_presence_test.py
Exit 1 if CI does not invoke the release gate.
"""
import os
import re
import sys

WORKFLOW = os.path.join(".github", "workflows", "verify.yml")
GATE = "tools/release_gate.py"
# A real invocation: an interpreter, then the gate path, at the start of a
# command. `echo tools/release_gate.py` does not match; `python3
# tools/release_gate.py` and `python tools/release_gate.py` do.
INVOCATION = re.compile(r"^(?:python3?|py)\s+" + re.escape(GATE) + r"(?:\s|$)")


def run_commands(text):
    """Every shell command line inside a `run:` key of the workflow.

    Handles both `run: <command>` and the block form `run: |` followed by an
    indented script. Comment lines inside a script are dropped: a commented-out
    gate is not a gate.
    """
    cmds = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("#"):
            i += 1
            continue
        m = re.match(r"^(\s*)-?\s*run:\s*(.*)$", line)
        if not m:
            i += 1
            continue
        indent, rest = m.group(1), m.group(2).strip()
        if rest and rest not in ("|", ">", "|-", ">-"):
            cmds.append(rest)
            i += 1
            continue
        # Block scalar: consume the more-indented lines that follow.
        base = len(indent)
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if not nxt.strip():
                i += 1
                continue
            if len(nxt) - len(nxt.lstrip()) <= base:
                break
            body = nxt.strip()
            if not body.startswith("#"):
                cmds.append(body)
            i += 1
    return cmds


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(root, WORKFLOW)
    if not os.path.exists(path):
        print(f"  FAIL {WORKFLOW} is missing entirely")
        print("\nci_gate_presence_test: FAILED (no workflow to check)")
        return 1
    text = open(path, encoding="utf-8").read()

    problems = []
    cmds = run_commands(text)
    invocations = [c for c in cmds if INVOCATION.match(c)]
    if not invocations:
        mentions = [c for c in cmds if GATE in c]
        if mentions:
            problems.append(
                f"{WORKFLOW} mentions {GATE} in a run: command but never "
                f"invokes it through an interpreter; mentioning a path is not "
                f"running it (saw: {mentions[0]!r})")
        else:
            problems.append(
                f"{WORKFLOW} never invokes {GATE} in any run: command; CI green "
                f"would then say nothing about the gate checks")

    gate = os.path.join(root, "tools", "release_gate.py")
    if not os.path.exists(gate):
        problems.append("tools/release_gate.py does not exist to be run")

    for p in problems:
        print(f"  FAIL {p}")
    if problems:
        print(f"\nci_gate_presence_test: FAILED ({len(problems)} problem(s))")
        return 1
    print(f"  OK   {WORKFLOW} invokes {GATE} through an interpreter in a "
          f"live run: command ({invocations[0]!r})")
    print("\nci_gate_presence_test: OK (CI runs the real release gate)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
