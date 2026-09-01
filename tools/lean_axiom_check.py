#!/usr/bin/env python3
"""lean_axiom_check.py - proof health from the KERNEL's own report, not from
diagnostic formatting.

WHY THIS EXISTS. A round shipped six results carrying `sorryAx` while a grep
over the build output reported the file clean. The grep was anchored on
`FILE:LINE:COL: (error|warning)`, and lake prints the severity BEFORE the
filename -- `error: OIBridge/X.lean:12:3: ...` -- so the pattern matched
nothing and silence read as success. Parsing diagnostic layout is not a proof
health gate; the layout is not a contract.

What IS a contract is `#print axioms`. This check reads that, plus one
formatting-independent rule:

  1. HARD FAIL on the literal token `sorryAx` anywhere in the captured output,
     whatever surrounds it. A changed diagnostic layout cannot hide a token
     that the axiom report itself must print.
  2. HARD FAIL if lake exits nonzero.
  3. HARD FAIL on any axiom outside the permitted three. `native_decide` shows
     up here as `Lean.ofReduceBool`; the project bans it outright.
  4. HARD FAIL if a `#print axioms NAME` written in a source produced no
     report -- a print that silently stops being elaborated is exactly as bad
     as a bad axiom.

The analysis runs against three synthetic logs on every invocation, so a
refactor that breaks the detection fails the check rather than passing it
quietly. That is the same defect class this file exists to catch.

Usage:
    python3 tools/lean_axiom_check.py [--log FILE] [--root DIR]

With --log, scans a previously captured build log instead of building. Without
it, runs `lake build` in verification/lean-mathlib and scans what comes back.
If lake cannot be found the check reports SKIPPED and exits 0 -- the tree is
still checkable without a Lean toolchain -- but says so loudly, because a
skipped proof-health check is not a passed one.

Exit 1 on any failure.
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

PERMITTED = {'propext', 'Classical.choice', 'Quot.sound'}

AXIOM_LINE = re.compile(r"'([A-Za-z0-9_.']+)' depends on axioms: \[([^\]]*)\]")
NO_AXIOM_LINE = re.compile(r"'([A-Za-z0-9_.']+)' does not depend on any axioms")


def find_lake():
    for cand in (os.environ.get('LAKE'),
                 os.path.expanduser('~/.elan/bin/lake'),
                 '/usr/local/bin/lake'):
        if cand and os.path.isfile(cand) and os.access(cand, os.X_OK):
            return cand
    for d in os.environ.get('PATH', '').split(os.pathsep):
        c = os.path.join(d, 'lake')
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    return None


def declared_prints(root):
    """Every `#print axioms NAME` written in the Lean sources, as short names."""
    out = set()
    src = os.path.join(root, 'verification', 'lean-mathlib')
    for dp, _, fs in os.walk(src):
        if '.lake' in dp.split(os.sep):
            continue
        for f in sorted(fs):
            if f.endswith('.lean'):
                text = open(os.path.join(dp, f), encoding='utf-8',
                            errors='replace').read()
                for m in re.finditer(
                        r'(?m)^#print axioms ([A-Za-z0-9_.\']+)\s*$', text):
                    out.add(m.group(1).split('.')[-1])
    return out


def analyse(log, rc, declared):
    """(problem count, report lines, names reported). Pure: the self-test below
    drives exactly this, so the detection cannot rot behind a live build."""
    msgs, fail = [], 0

    hits = [l.strip() for l in log.splitlines() if 'sorryAx' in l]
    if hits:
        msgs.append(f"  SORRY  {len(hits)} line(s) of Lean output mention "
                    f"`sorryAx`:")
        msgs += [f"         {l[:160]}" for l in hits[:12]]
        fail += len(hits)

    if rc != 0:
        msgs.append(f"  BUILD  lake exited {rc}")
        msgs += [f"         {l[:160]}" for l in log.splitlines()
                 if l.startswith('error:')][:12]
        fail += 1

    reported = set()
    for m in AXIOM_LINE.finditer(log):
        name = m.group(1).split('.')[-1]
        reported.add(name)
        extra = {a.strip() for a in m.group(2).split(',') if a.strip()} \
            - PERMITTED
        if extra:
            msgs.append(f"  AXIOM  {name} depends on {sorted(extra)}")
            fail += 1
    for m in NO_AXIOM_LINE.finditer(log):
        reported.add(m.group(1).split('.')[-1])

    if reported:
        missing = sorted(declared - reported)
        if missing:
            msgs.append(f"  SILENT {len(missing)} declared `#print axioms` "
                        f"produced no report: {missing[:8]}")
            fail += len(missing)
    else:
        msgs.append("  EMPTY  the build produced no axiom report at all; force "
                    "a rebuild or pass --log from a real compile.")
        fail += 1
    return fail, msgs, reported


CLEAN = ("info: X.lean:1:0: 'OIBridge.A.foo' depends on axioms: "
         "[propext, Classical.choice, Quot.sound]\n"
         "info: X.lean:2:0: 'OIBridge.A.bar' does not depend on any axioms\n")


def self_test():
    """Three synthetic logs. Written in lake's real layout, severity first."""
    d = {'foo', 'bar'}
    if analyse(CLEAN, 0, d)[0] != 0:
        return "clean log did not pass"
    dirty = CLEAN.replace("[propext, Classical.choice, Quot.sound]",
                          "[propext, sorryAx, Classical.choice, Quot.sound]")
    if analyse(dirty, 0, d)[0] == 0:
        return "sorryAx in an axiom report was not caught"
    native = CLEAN.replace("[propext, Classical.choice, Quot.sound]",
                           "[propext, Lean.ofReduceBool]")
    if analyse(native, 0, d)[0] == 0:
        return "a forbidden axiom was not caught"
    if analyse(CLEAN, 0, d | {'gone'})[0] == 0:
        return "a dropped `#print axioms` was not caught"
    if analyse("error: X.lean:1:0: boom\n" + CLEAN, 1, d)[0] == 0:
        return "a nonzero lake exit was not caught"
    return None


def main():
    root = ROOT
    if '--root' in sys.argv:
        root = os.path.abspath(sys.argv[sys.argv.index('--root') + 1])

    bad = self_test()
    if bad:
        print(f"lean_axiom_check: FAILED - self-test: {bad}")
        return 1

    if '--log' in sys.argv:
        log = open(sys.argv[sys.argv.index('--log') + 1], encoding='utf-8',
                   errors='replace').read()
        rc = 0
    else:
        lake = find_lake()
        if lake is None:
            print("lean_axiom_check: SKIPPED - no `lake` on PATH or in "
                  "~/.elan/bin, so there is no kernel report to read.")
            print("             A SKIPPED proof-health check is not a passed "
                  "one. Install the toolchain,")
            print("             or pass --log with a captured `lake build` "
                  "output.")
            return 0
        try:
            r = subprocess.run([lake, 'build'],
                               cwd=os.path.join(root, 'verification',
                                                'lean-mathlib'),
                               capture_output=True, text=True, timeout=5400)
        except Exception as e:                                  # noqa: BLE001
            print(f"lean_axiom_check: FAILED - could not run lake: {e}")
            return 1
        log, rc = r.stdout + r.stderr, r.returncode

    fail, msgs, reported = analyse(log, rc, declared_prints(root))
    for m in msgs:
        print(m)
    if fail:
        print(f"\nlean_axiom_check: FAILED ({fail} problem(s))")
        return 1
    print(f"lean_axiom_check: OK ({len(reported)} named result(s) reported, no "
          f"sorryAx, every axiom within "
          f"{{propext, Classical.choice, Quot.sound}}; self-test passed)")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
