#!/usr/bin/env python3
"""release_gate.py - one entry point for every pre-release check.

The checks accumulated over the correction rounds, none of which subsumes
another. Each exists because a real defect shipped past the others:

  toolchain_check      build.sh went missing and the duplicate unicode-fix
                       headers came back. All six other checks passed green on
                       a tree that could not be rebuilt at all.
  staleness_check      a .md was edited and its .tex/.pdf were not rebuilt.
                       bundle_check, mirror and citation audits all passed.
  mirror_check         a book CHAPTER was edited; chapters have no individual
                       .tex, so staleness_check stays green.
  baseline_label_check one handover doc named a superseded baseline archive
                       while its sibling was current. Strict --label pins the
                       expected number, since a tree where EVERY doc names the
                       same stale baseline passes the relative test.
  voice_check          correction rounds reintroduced revision narration that
                       AGENTS.md forbids, faster than review removed it.
  claims_check         a withdrawn result stayed asserted in a later sentence;
                       a file-level scope note does not rescue it.
  duplicate_check      a scope note pasted at the head of every file put 16
                       identical copies inside the assembled book, and an
                       entire 8.6 section was duplicated in one paper.
  lean_axiom_check     a round shipped six results carrying sorryAx while a grep
                       over the build output reported the file clean: lake prints
                       the severity before the filename, so a pattern anchored on
                       FILE:LINE:COL matched nothing and silence read as success.
                       This check reads `#print axioms` -- the kernel's own report
                       -- and fails on the literal token sorryAx regardless of how
                       the surrounding diagnostics are laid out.
  coverage_check       theorems accumulated in the papers with no executable or
                       kernel coverage and nothing noticed, because every other
                       check compares artifacts to sources and none of them asks
                       whether a source statement is checked at all.
  control_plane_lint   a control plane named its drafting snapshot as the
                       mandated execution base and required, at that base, the
                       absence of a token its own text carried; two of its
                       preconditions could not hold at the commit its chronology
                       control named, and owner review caught it after the
                       merge. Applies to control planes carrying a preconditions
                       block or changed in the diff under check.
  certificate_verifier the V2 round-certificate verifier, authoritative: a
                       historical round is data -- a certificate and an attestation
                       record -- verified by one generic tool, after six manifestations
                       of one defect in two repair rounds showed that a historical
                       round expressed as executable code running at every later head
                       invites an assertion against the wrong tree at every extension
                       point. The standalone workflow job runs it in shadow and gates
                       nothing; this step is where V2 can reject a build.
  v3-receipts          the V3 verdict, from round V3-11: every receipt in the
                       tree, verified by tools/v3_verifier.py --receipts from
                       the commit that last wrote it. A receipt is data no other
                       check reads, so this step is where a native round whose
                       receipt does not hold can reject a build. V1 and V2 keep
                       running beside it and can still fail the gate; they do
                       not decide whether a native round is protocol-valid.

Post-packaging, verify the DECLARED checksum against the shipped archive:
    python3 tools/baseline_label_check.py --verify-archive PATH --root TRANSFER

Usage:
    python3 tools/release_gate.py [--label bNNN] [--transfer DIR]

Exit 1 if any check fails. Run from the repository root.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def run(name, argv, cwd=ROOT):
    try:
        r = subprocess.run(argv, cwd=cwd, capture_output=True, text=True,
                           timeout=1800)
    except Exception as e:                     # noqa: BLE001
        return name, False, f"could not run: {e}"
    tail = [l for l in (r.stdout + r.stderr).strip().splitlines() if l.strip()]
    return name, r.returncode == 0, (tail[-1] if tail else "")

def main():
    label = None
    if '--label' in sys.argv:
        label = sys.argv[sys.argv.index('--label') + 1]
    # the commit under check, located here because tools/v3_verifier.py reads no ref: the gate
    # names the commit, and a failed lookup leaves an empty argument, which the verifier refuses
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
                          text=True).stdout.strip()
    checks = [
        # toolchain FIRST: every other check compares artifacts to sources, so
        # they all pass on a tree that has lost its build entry point and can
        # no longer be regenerated at all.
        ("toolchain", [sys.executable, "tools/toolchain_check.py"]),
        ("staleness", [sys.executable, "tools/staleness_check.py"]),
        ("voice",     [sys.executable, "tools/voice_check.py"]),
        # Controls on the gate itself. voice-scope keeps voice_check pointed at
        # the manuscript and only the manuscript; ci-gate-presence keeps this
        # gate wired into CI. Both are mutation-tested: each fails if the thing
        # it guards is removed.
        ("voice-scope", [sys.executable, "tools/voice_scope_test.py"]),
        ("ci-gate-presence", [sys.executable, "tools/ci_gate_presence_test.py"]),
        # artifact-placement: new audits and preregistrations stay out of the
        # verification/ root. One-directional against the migration manifest as
        # a grandfather list, so it survives the mechanical migration unchanged.
        ("artifact-placement",
                      [sys.executable, "tools/artifact_placement_check.py"]),
        # manifest-drift: the two forms of the migration manifest are rendered
        # from one mapping, and --check re-renders and compares rather than
        # trusting that nobody hand-edited a generated file. Needs no
        # particular layout, so it holds across the migration too.
        ("manifest-drift",
                      [sys.executable, "tools/build_migration_manifest.py", "--check"]),
        # control-plane-lint: a control plane must not give its drafting
        # snapshot's SHA to the mandated execution base, and no B-scoped
        # precondition may ask for the absence of a token the frozen artifact
        # itself carries. Applies to block-bearing and newly changed control
        # planes only; merged artifacts without a block are grandfathered.
        ("control-plane-lint",
                      [sys.executable, "tools/control_plane_lint.py"]),
        ("claims",    [sys.executable, "tools/claims_check.py"]),
        ("duplicate", [sys.executable, "tools/duplicate_check.py"]),
        ("mirror",    [sys.executable, "papers/oi_lattice_code/mirror_check.py"]),
        ("citation",  [sys.executable, "papers/oi_lattice_code/citation_check.py"]),
        ("architecture",
                      [sys.executable, "papers/oi_lattice_code/architecture_check.py"]),
        # dependency-label guard: a "(derived)"/Tier-label paragraph that cites
        # a section carrying a named condition. Strict: any hit fails the gate
        # (the check also runs its own self-test every time).
        ("dependency-label",
                      [sys.executable, "tools/dependency_label_check.py", "--strict"]),
        # coverage: every canonical theorem/lemma has a ledger entry, every entry's
        # fingerprint still matches the manuscript statement it certifies, every
        # named checker exists, and no level claims more than its checkers deliver.
        # This is the check against a proof that ships without ever being wired to
        # anything -- which no other check here can see.
        ("coverage",  [sys.executable, "tools/coverage_check.py"]),
        # lean-axioms: proof health read from `#print axioms`, the kernel's own
        # report, plus a hard fail on the literal token `sorryAx` anywhere in the
        # captured build output. This exists because a grep anchored on Lean's
        # diagnostic layout reported a file clean while six of its results
        # carried sorryAx -- lake prints the severity BEFORE the filename, so the
        # pattern matched nothing and silence read as success. Diagnostic
        # formatting is not a contract; the axiom report is.
        # --require-lake: without it a missing toolchain prints SKIPPED and exits 0,
        # which this runner would score as PASS. The gate must not report a
        # kernel-health check it never ran.
        ("lean-axioms",
                      [sys.executable, "tools/lean_axiom_check.py", "--require-lake"]),
        # lean-manuscript: the manuscripts against the whole kernel. Every cited
        # identifier resolves, no paragraph cites a superseded theorem without its
        # successor, every OIBridge module has a registry disposition, and every
        # anchor a current family names is present. This is the check against a
        # kernel strengthening that reaches the verification notes and guards and
        # never reaches the papers -- which no other check here can see.
        ("lean-manuscript",
                      [sys.executable, "tools/lean_manuscript_census.py"]),
        # certificate-verifier: the V2 round-certificate verifier in AUTHORITATIVE mode -- every
        # certificate, attestation record, relocation, live-policy clause and conformance vector,
        # the corpus executed as an exact set. This is the cutover wiring edit of certificate
        # round CV-1: the repository's ruleset requires only three status contexts, none of them
        # the standalone shadow job, so a red standalone job would not by itself block a merge;
        # this step, run by the required Mathlib bridge check, is what lets V2 reject a build.
        # V1's guard gates beside it and is not retired here.
        ("certificate-verifier",
                      [sys.executable, "tools/certificate_verifier.py", "--mode", "authoritative"]),
        # v3-receipts: the V3 verdict (round V3-11). Every receipt under verification/receipts/,
        # verified from the commit that last wrote it; a receipt that does not hold, or a
        # repository too shallow to decide, fails the gate. It needs full history, so the
        # workflow's Mathlib bridge job checks out with fetch-depth: 0.
        ("v3-receipts",
                      [sys.executable, "tools/v3_verifier.py", "--receipts", head]),
    ]
    # baselines are named in the TRANSFER's docs, not the manuscript tree, so
    # point the label check there when a transfer path is supplied
    lab = [sys.executable, os.path.join(HERE, "baseline_label_check.py")]
    if '--transfer' in sys.argv:
        lab += ["--root", sys.argv[sys.argv.index('--transfer') + 1]]
    if label:
        lab += ["--label", label]
    checks.insert(2, ("baseline-label", lab))

    print("release gate")
    print("=" * 68)
    failed = []
    for name, argv in checks:
        n, ok, tail = run(name, argv)
        print(f"  {'PASS' if ok else 'FAIL'}  {n:16s} {tail[:60]}")
        if not ok:
            failed.append(n)
    print("=" * 68)
    if failed:
        print("release gate: FAILED -> " + ", ".join(failed))
        print("(rerun the individual check for file/line detail)")
        return 1
    if not label:
        print("release gate: PASS  (note: --label bNNN not given, so the "
              "baseline check ran in relative mode only)")
    else:
        print("release gate: PASS")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
