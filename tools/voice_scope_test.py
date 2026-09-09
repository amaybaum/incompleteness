#!/usr/bin/env python3
"""voice_scope_test.py - does voice_check scan the manuscript, and only it?

This exists because of a real defect, not a hypothetical one. `voice_check.py`
described itself as a manuscript-voice check while walking every Markdown file
under the repository root. It therefore flagged the phrase "It now reads:" in a
frozen control-plane amendment under `verification/` - a document whose whole
job is to record what changed. The fix was to scope the checker positively to
publication manuscript Markdown. This test is what stops the repository-wide
scan from coming back.

The test is a mutation in both directions, which is the point: a checker that
never fires is as broken as one that fires everywhere.

  - a synthetic file under `verification/` carrying the trigger phrase must
    PASS, because it is outside the manuscript;
  - the same phrase in a synthetic `papers/*.md` must FAIL;
  - the same phrase in a synthetic book manuscript chapter must FAIL.

Usage:  python3 tools/voice_scope_test.py
Exit 1 if the scope has drifted in either direction.
"""
import os
import shutil
import subprocess
import sys
import tempfile

TRIGGER = "The section was corrected. It now reads: the bound is exact.\n"

CASES = [
    # (relative path, expect_failure, why this case exists)
    ("verification/SYNTHETIC-SCOPE-PROBE.md", False,
     "control-plane and audit records are outside the manuscript"),
    ("papers/SyntheticScopeProbe.md", True,
     "papers are manuscript and must be scanned"),
    ("book/ch99-synthetic-scope-probe.md", True,
     "book chapters are manuscript and must be scanned"),
    ("book/README.md", False,
     "directory documentation beside the book is not manuscript prose"),
]


def run_case(repo_root, rel, expect_failure):
    """Build a minimal tree with one synthetic file and run voice_check on it."""
    with tempfile.TemporaryDirectory() as tmp:
        # A tree only counts as the manuscript tree if papers/ exists.
        for d in ("papers", "book", "verification"):
            os.makedirs(os.path.join(tmp, d), exist_ok=True)
        target = os.path.join(tmp, rel)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as fh:
            fh.write(TRIGGER)
        checker = os.path.join(repo_root, "tools", "voice_check.py")
        proc = subprocess.run(
            [sys.executable, checker, "--root", tmp],
            capture_output=True, text=True)
        failed = proc.returncode != 0
        return failed, proc.stdout


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bad = 0
    for rel, expect_failure, why in CASES:
        failed, out = run_case(repo_root, rel, expect_failure)
        ok = (failed == expect_failure)
        verb = "flags" if expect_failure else "ignores"
        status = "OK  " if ok else "FAIL"
        print(f"  {status} voice_check {verb} {rel}  ({why})")
        if not ok:
            bad += 1
            print("       checker said:")
            for line in out.strip().splitlines():
                print(f"       | {line}")
    if bad:
        print(f"\nvoice_scope_test: FAILED ({bad} scope case(s) wrong)")
        return 1
    print(f"\nvoice_scope_test: OK ({len(CASES)} scope case(s); the checker "
          f"scans the manuscript and only the manuscript)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
