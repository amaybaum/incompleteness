#!/usr/bin/env python3
"""control_plane_lint.py - a control plane must not confuse D with B.

AGENTS.md A.37 gives a control plane three commit names: D, the drafting
snapshot; B, the mandated execution base, which has no SHA until the artifact's
certified merge exists; and M, a candidate merge. The Act 21 freeze gave D's SHA
to B and asked, at B, for the absence of a token its own text carried. This lint
rejects both shapes before they merge. It reads the file and its
`control-plane-preconditions` block (the format is documented in
`tools/control_plane_base_check.py`, whose parser it shares) and fails on:

  D==B      one literal 40-hex SHA assigned to both D and B, in prose
            (`D = `<sha>``, `` `D` = `<sha>` ``, `D is `<sha>``) or in the
            block's `d:` / `b:` headers, or across the two;
  B-literal a literal SHA assigned to B in a file whose block does not declare
            `merged: true` - before the merge B has no SHA to give;
  scope     a precondition row without a scope of D, B or D->B, or otherwise
            malformed;
  grep-B    a B-scoped row `git grep -- '<token>' ...` expecting empty output
            when `<token>` already occurs in a control-plane file of the same
            round directory - the frozen artifacts will be in the tree at B, so
            the row can never hold there.

Scope of the lint: control-plane files (`preregistration.md`,
`amendments/amendment-*.md` under `verification/`) that carry the block, plus
any such file added or modified in `git diff --name-only origin/main...HEAD`
when that range resolves. Artifacts merged before the block existed carry no
block and are never rewritten or linted; they are grandfathered.

Usage:
    python3 tools/control_plane_lint.py            # lint, exit 1 on any finding
    python3 tools/control_plane_lint.py --self-test
"""
import glob
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from control_plane_base_check import (  # noqa: E402
    CP_PATH, FENCE, HEX40, parse_block, row_problems)

# `D = `<sha>``, `` `D` = `<sha>` ``, `D is `<sha>``; the name must stand alone.
ASSIGN = re.compile(
    r"(?<![A-Za-z0-9_`])`?([DB])`?\s*(?:=|:=|\bis\b)\s*`?([0-9a-f]{40})(?![0-9a-f])")
# `git grep [opts] -- '<token>' ...`; the token may be quoted either way or bare.
GREP_TOKEN = re.compile(
    r"\bgit\s+grep\b[^|;&]*?\s--\s+(?:'([^']*)'|\"([^\"]*)\"|(\S+))")


def round_dir(path):
    """The round directory a control-plane file belongs to."""
    d = os.path.dirname(path)
    if os.path.basename(d) == "amendments":
        d = os.path.dirname(d)
    return d


def round_files(path, root):
    """Every control-plane file of the same round, on disk, including `path`."""
    rd = os.path.join(root, round_dir(path))
    out = [os.path.join(rd, "preregistration.md")]
    out += sorted(glob.glob(os.path.join(rd, "amendments", "amendment-*.md")))
    return [p for p in out if os.path.isfile(p)]


def prose_assignments(text):
    """{'D': {sha,...}, 'B': {sha,...}} from prose assignment forms."""
    found = {"D": set(), "B": set()}
    for m in ASSIGN.finditer(text):
        found[m.group(1)].add(m.group(2))
    return found


def lint_text(path, text, sibling_texts):
    """Findings for one file. `sibling_texts` are the contents of the round's
    control-plane files (the file itself included) for the grep-B check."""
    findings = []
    blk = parse_block(text)
    for e in blk.errors:
        findings.append("block: " + e)
    assigned = prose_assignments(text)
    if blk.d:
        assigned["D"].add(blk.d)
    if blk.b:
        assigned["B"].add(blk.b)

    both = assigned["D"] & assigned["B"]
    for sha in sorted(both):
        findings.append("D==B: %s is assigned to both D and B; the drafting "
                        "snapshot is never the mandated execution base" % sha[:12])
    if assigned["B"] and not blk.merged:
        for sha in sorted(assigned["B"] - both):
            findings.append("B-literal: B = %s in an artifact not marked "
                            "`merged: true`; before its certified merge B has "
                            "no SHA" % sha[:12])

    for row in blk.rows:
        ident = "row %s (line %d)" % (row.get("id", "?"), row["_line"])
        probs = row_problems(row)
        if probs:
            findings.append("scope: %s: %s" % (ident, "; ".join(probs)))
            continue
        if row["scope"] != "B" or row["expect"] != "empty":
            continue
        m = GREP_TOKEN.search(row["check"])
        if not m:
            continue
        token = next(g for g in m.groups() if g is not None)
        if not token:
            continue
        carriers = [os.path.relpath(p, os.path.dirname(os.path.dirname(path)))
                    for p, t in sibling_texts if token in t]
        if carriers:
            findings.append("grep-B: %s expects `git grep -- %r` empty at B, but "
                            "the token occurs in this round's control-plane "
                            "file(s) (%s), which are in the tree at B; state "
                            "the absence of execution objects instead, or scope "
                            "the freedom check at D" % (ident, token, ", ".join(carriers)))
    return findings


def lint_file(path, root):
    abs_path = os.path.join(root, path)
    text = open(abs_path, encoding="utf-8").read()
    sibs = [(p, open(p, encoding="utf-8").read()) for p in round_files(path, root)]
    if abs_path not in [p for p, _ in sibs]:
        sibs.append((abs_path, text))
    return lint_text(abs_path, text, sibs)


def changed_control_planes(root):
    """Control-plane files added or modified against origin/main, or None when
    the range does not resolve (shallow clone, no remote)."""
    r = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AM",
                        "origin/main...HEAD"], cwd=root, capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return sorted(p for p in r.stdout.splitlines()
                  if CP_PATH.match(p) and os.path.isfile(os.path.join(root, p)))


def block_bearing(root):
    out = []
    for dirpath, _, names in os.walk(os.path.join(root, "verification")):
        for n in names:
            p = os.path.relpath(os.path.join(dirpath, n), root)
            if not CP_PATH.match(p):
                continue
            try:
                if "```" + FENCE in open(os.path.join(root, p), encoding="utf-8").read():
                    out.append(p)
            except (OSError, UnicodeDecodeError):
                continue
    return sorted(out)


def targets(root):
    files = set(block_bearing(root))
    changed = changed_control_planes(root)
    if changed is not None:
        files |= set(changed)
    return sorted(files), changed is not None


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------

D_SHA = "63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed"
B_SHA = "aeb0b91d20b4e307c293c06afda9db64fe2a3b09"


def _fixture(prose, headers, rows):
    return "\n".join(["# Round", "", prose, "", "```" + FENCE] + headers + rows
                     + ["```", ""])


def _good(merged):
    return _fixture(
        "The stem is `RXQ`. `D` = `%s` is the drafting snapshot." % D_SHA,
        ["d: " + D_SHA] + (["b: " + B_SHA, "merged: true"] if merged else []),
        ['{"id": "no-module", "scope": "B", "check": "git ls-tree -r --name-only '
         '$REF | grep -x lean/RXQ.lean", "expect": "empty"}',
         '{"id": "free-at-D", "scope": "D", "check": "git grep -- RXQ $D", '
         '"expect": "empty"}',
         '{"id": "ancestry", "scope": "D->B", "check": "git merge-base --is-ancestor '
         '$D $REF", "expect": "exit0"}'])


def self_test():
    """Positive fixtures pass and each negative fixture is caught by the
    finding named for it; a lint that cannot fail is not a control."""
    cases = [
        ("good-unmerged", _good(False), None),
        ("good-merged", _good(True), None),
        ("d-equals-b-prose",
         _fixture("`D` = `%s`; the base `B` = `%s`." % (D_SHA, D_SHA),
                  ["d: " + D_SHA, "merged: true"], []), "D==B"),
        ("d-equals-b-headers",
         _fixture("", ["d: " + D_SHA, "b: " + D_SHA, "merged: true"], []), "D==B"),
        ("b-literal-unmerged",
         _fixture("B = `%s` is the base." % B_SHA, ["d: " + D_SHA], []), "B-literal"),
        ("b-header-unmerged",
         _fixture("", ["d: " + D_SHA, "b: " + B_SHA, "merged: false"], []), "B-literal"),
        ("row-without-scope",
         _fixture("", ["d: " + D_SHA],
                  ['{"id": "x", "check": "true", "expect": "exit0"}']), "scope"),
        ("row-bad-scope",
         _fixture("", ["d: " + D_SHA],
                  ['{"id": "x", "scope": "M", "check": "true", "expect": "exit0"}']),
         "scope"),
        ("grep-token-carried",
         _fixture("The stem is `RXQ`.", ["d: " + D_SHA],
                  ['{"id": "stem-absent", "scope": "B", "check": "git grep -l -- '
                   '\'RXQ\' $REF", "expect": "empty"}']), "grep-B"),
        ("grep-token-at-D-is-fine",
         _fixture("The stem is `RXQ`.", ["d: " + D_SHA],
                  ['{"id": "stem-free", "scope": "D", "check": "git grep -l -- '
                   '\'RXQ\' $D", "expect": "empty"}']), None),
        ("unknown-header",
         _fixture("", ["d: " + D_SHA, "scope: B"], []), "block"),
    ]
    with tempfile.TemporaryDirectory() as tmp:
        for name, text, want in cases:
            rel = "verification/programmes/self-test/%s/preregistration.md" % name
            p = os.path.join(tmp, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(text)
            findings = lint_file(rel, tmp)
            if want is None and findings:
                return False, "%s: expected clean, got %s" % (name, findings)
            if want is not None and not any(f.startswith(want + ":") for f in findings):
                return False, "%s: expected a %r finding, got %s" % (name, want, findings)

        # an amendment sees the preregistration of its round: the token the
        # preregistration carries fails a B-scoped grep in the amendment
        rd = "verification/programmes/self-test/round-amend"
        os.makedirs(os.path.join(tmp, rd, "amendments"))
        with open(os.path.join(tmp, rd, "preregistration.md"), "w") as fh:
            fh.write("# Round\n\nThe stem is `ZQX`.\n")
        rel = rd + "/amendments/amendment-1.md"
        with open(os.path.join(tmp, rel), "w") as fh:
            fh.write(_fixture("", ["d: " + D_SHA],
                              ['{"id": "t", "scope": "B", "check": "git grep -- ZQX '
                               '$REF", "expect": "empty"}']))
        findings = lint_file(rel, tmp)
        if not any(f.startswith("grep-B:") and "preregistration.md" in f for f in findings):
            return False, "amendment did not see its preregistration: %s" % findings
    return True, ""


# --------------------------------------------------------------------------

def main(argv):
    if "--self-test" in argv:
        ok, why = self_test()
        print("control_plane_lint: self-test " + ("OK" if ok else "FAILED: " + why))
        return 0 if ok else 1

    ok, why = self_test()
    if not ok:
        print("control_plane_lint: FAIL (self-test: %s)" % why)
        return 1

    files, ranged = targets(ROOT)
    total = 0
    for path in files:
        findings = lint_file(path, ROOT)
        for f in findings:
            print("  FAIL  %s: %s" % (path, f))
        total += len(findings)
    how = "block-bearing files plus origin/main...HEAD additions" if ranged \
        else "block-bearing files only; origin/main...HEAD did not resolve"
    if total:
        print("control_plane_lint: FAILED (%d finding(s) over %d file(s); %s)"
              % (total, len(files), how))
        return 1
    print("control_plane_lint: OK (%d control-plane file(s) linted; %s; self-test passed)"
          % (len(files), how))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
