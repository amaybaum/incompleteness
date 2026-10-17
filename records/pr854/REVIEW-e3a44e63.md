# PR #854: independent repair review at e3a44e63

Reviewed commit: `e3a44e63ebec41fccd109cf1ca945b3b8a200553`.
Prior tested checkpoint: `6bf56dc4500770b6c32bc584b32d2198a1916215`.
Intermediate fix: `915ca926ee7d5b17a35001362ca6800c938d3789`.

**Verdict: APPROVE-FOR-PR-UPDATE. CI and real Lean reproductions remain required before acceptance.**

Reviewer: Codex, continuing in a fresh environment; the reviewer did not author the two fix commits.
The source review covered the two fix commits and the six-file scope against the PR base `66a981d5`.
No source change was needed. This is working review material, not a native-round attestation or retained
scientific evidence under AGENTS section A.42.

## Counterexamples replayed independently

`counterexamples.py` imports the exact files from the named git commits. Run:

```sh
python3 -I counterexamples.py /absolute/path/to/a/full-history/clone
```

It exercises the real archive-history checks on copied archive bytes. It runs the real reproduction entry
point and writes its actual verdict.json, with explicit stand-ins for toolchain commands, extraction and
comparison. The latter checks argument handling, negative-control conditions and exit handling only.
It does not establish real Lean reproducibility.

All 28 assertions passed, including 68 split/joined parser pairs:

- The old `6bf56dc4` accepts a CI bridge result relabelled as a design diagnostic after the manifest's size
  and digest follow it. The corrected history check rejects it under R8 and R11, with no unrelated failure.
- The old checkpoint also accepts the same relabel of BG-3's E-tail result. The corrected check rejects it
  under R11 rather than listing an attested run as outside scope.
- Dropping the sole result of another required run fails attested-versus-checked run-set equality.
- The unmodified archive checks 97 results from 96 attested runs, 165 module records, with exactly three
  explicitly excluded results.
- The old checkpoint silently drops a joined unmatched `--expect-failure=TEXT` and accepts the mocked
  negative control. The corrected code rejects unmatched text in either form and accepts matching text.
- `915ca926` gives different verdicts for flag-shaped values in the two forms. `e3a44e63` rejects both
  forms identically, and all four valued flags agree across 17 representative values each.
- Unknown, missing, empty, repeated and malformed arguments write a false verdict. A comparator exception
  writes a false verdict with the exception type and message.

## Local validation at the exact reviewed commit

- Evidence-retention history gate: HOLDS, zero failures; 104 checker self-test cases pass.
- Comparator self-test: passes against four expected-result fixtures.
- V3 verifier self-test: passes; all 48 receipts hold.
- Legacy checker self-test: passes; all 303 records in 75 closed namespaces are intact.
- Artifact placement, voice, Python compilation and diff whitespace checks pass.
- The manifest changes only reproduce.py's pinned size and digest. Historical expected results are unchanged.
- A clean merge-tree simulation against main `ea3155fd` yields `18d4d6ccdabef55f721f9f67d918c95fdf947d08`.
  Its patch over main is byte-identical to the repair's patch over `66a981d5`; all 58 provenance-errata
  additions are preserved, and there are no other differences.

Machine-readable replay results and concise local-check outputs accompany this note.

## Remaining acceptance work

The owner already authorized pushing an independently reviewed SHA, followed by exact-head verification
and the affected positive and negative reproductions. The PR branch was advanced, by a checked fast-forward,
from `6bf56dc4` to exactly `e3a44e63`; the old checkpoint and intermediate fix remain in history.

The pull-request run is an integration check. It does not replace a `workflow_dispatch` run on exactly
`e3a44e63`, or the real positive and negative reproductions with the verifier at that SHA.
The connected GitHub tools expose no workflow-dispatch operation. Browser fallback requires approval
under the session's browser instructions. No workflow workaround or change to the workflow is introduced.
The PR remains a draft. No merge is authorized by this review.
