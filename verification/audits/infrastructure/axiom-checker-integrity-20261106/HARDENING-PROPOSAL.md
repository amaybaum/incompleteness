# Hardening proposal for `tools/lean_axiom_check.py` (#1162): for separate review

**Status: design only, for separate review.** This proposal makes no edit to the production checker
or the release gate, and none is authorized by the ruling it answers (#1031 comment 6681413802,
item 6). Any implementation needs its own owner authorization and an independent review before the
edit.

**Trigger.** The synthetic demonstration in this directory ([`README.md`](README.md)) confirms false
PASS for short-name masking (fixtures N1, N1n) and for non-ASCII identifiers (N2, N3).

## Constraint from the sources on `main`

Most prints are written relative to an open namespace: of the 6193 `#print axioms` lines in
`verification/lean-mathlib/OIBridge/` (the checker scans all of `verification/lean-mathlib/`, which
adds 19 prints in `OIBridge.lean`), 1783 begin with `OIBridge.` (counted with
`grep -rh '^#print axioms' verification/lean-mathlib/OIBridge | awk '{print $3}' | grep -c '^OIBridge\.'`
at `63671259`). So the name as written is not a qualified identity, and qualifying it from the source
would need Lean's namespace and `open` resolution. The report, however, carries both the fully
qualified name and the position of the command that produced it. The position is the identity source
proposed below.

## Proposed changes

1. **Qualified identities.** Key each declared print by `(module path, line)` of its `#print axioms`
   command, relative to `verification/lean-mathlib`. Key each report by the `FILE:LINE` lake prints
   before it, normalized by stripping any leading `./`. Then:
   - every declared print has exactly one report at its position (MISSING / DUPLICATE);
   - the reported fully qualified name equals the written name or ends with `.` + the written name
     (MISMATCH);
   - a report at a position with no declared print is a failure (ORPHAN).

   The checked identity is then `(module, fully qualified name)`. Messages name it in full.
2. **Unicode-aware parsing.**
   - Accept any non-whitespace name in the print pattern, `^#print axioms[ \t]+(\S+)[ \t]*$`. This
     covers `«»`-escaped names that contain no whitespace. An escaped name with a space, such as
     `«a b»`, does not match and falls to the fail-closed rule of item 3, which is safe but would
     need a dedicated pattern if such names are ever printed.
   - Parse the report name as the text between the quote after the position prefix and the last
     `' depends on axioms: [` or `' does not depend on any axioms` on that line.
   - Keep the existing `[^\]]*` axiom-list capture, which already spans wrapped lines and any
     characters. A wrapped report is parsed from its first line: the position prefix, the quoted
     name and `depends on axioms: [` sit on that line, and the capture runs on to the closing `]`
     on a later line. The fail-closed rule of item 3 applies to that first line; continuation lines
     carry neither trigger phrase.
3. **Fail closed on unparsed input.**
   - Any log line that contains `depends on axioms` or `does not depend on any axioms` and does not
     parse is a failure.
   - Any source line that begins with `#print axioms` and does not match the print pattern is a
     failure.
   - This turns a future layout or character-class drift into a red check rather than a silent skip.
4. **Self-test coverage.** Add to `self_test()` synthetic cases for both failure modes and their clean
   counterparts:
   - a duplicated short name with one report dropped, and the same pair with both reported;
   - a non-ASCII declaration reported with `Lean.ofReduceBool`, and with permitted axioms;
   - a non-ASCII declaration with no report;
   - an unparsable report line.

   Each case is asserted in the direction it must go, so a refactor that loses either detection fails
   the self-test. The fixtures C0–N7 of this record can be reused for the same purpose.
5. **No weakening.** The existing rules stay as they are: the `sorryAx` token scan, the nonzero-exit
   rule, the permitted-axiom set, EMPTY and `--require-lake`. Every input that fails today still fails.

## Open points for the reviewer

- **Coverage of the current tree.** Before adoption, the hardened checker must pass on a real
  `lake build` log of `main`. A failure there (for example a print inside a comment, or a cached
  module whose messages lake does not replay) is a finding to resolve, not a reason to relax the rule.
- **Prints not at column 0.** Indented prints and prints inside block comments are invisible to both
  the current and the proposed print pattern. Whether to lint for them is a separate decision.
- **Position format across lake versions.** The `FILE:LINE:COL` prefix and the replay of messages
  for up-to-date modules should be confirmed on the pinned toolchain.
