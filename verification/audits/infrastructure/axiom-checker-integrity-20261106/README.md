# Axiom-checker integrity: controlled synthetic demonstration (#1162)

This record tests `tools/lean_axiom_check.py`, the release gate's `lean-axioms` step, on synthetic
source trees and synthetic Lean-output logs. It asks whether the checker's short-name matching and
its ASCII-only identifier pattern can produce a false PASS. The production checker is run
unmodified. No manuscript evidence, Lean module or captured build log from `main` is used as input.
The record changes no proof grade or scientific status.

## Authority

Owner ruling, amaybaum, 2026-11-06 (#1031 comment 6681413802, posted 2026-11-06T09:14:23Z, item 6;
restated on #1162, comment 6681420259, 2026-11-06T09:14:45Z):

> Authorize one narrowly scoped verification-infrastructure investigation under Issue #1162.
>
> Test only synthetic source trees and synthetic Lean-output logs:
>
> * Whether two distinct fully qualified declarations sharing a short name allow one report to mask another missing report.
> * Whether a non-ASCII identifier can hide a forbidden axiom from the current parser.
> * Whether the controls detect the injected defects and pass correctly constructed clean cases.
>
> Require an independently checked expected outcome for every positive and negative fixture. Record actual exit statuses and enough inputs to reproduce the demonstration.
>
> If a false PASS is confirmed, prepare a separately reviewed hardening proposal using qualified identities and Unicode-aware parsing.
>
> Not authorized: editing the production checker, changing proof grades, rerunning unrelated studies, or weakening the current release gate.

**Placement (§A.36).** No existing audit family covers verification tooling:

- `foundations/`, `operational/` and `physical-realization/` hold audits of the framework's physics
  and its foundations;
- `manuscript/` holds corpus audits;
- `evidence-pruning/` holds the evidence-pruning ledger;
- `provenance-errata/` holds record provenance.

`verification/infrastructure/` holds the records of verification-infrastructure *rounds* (the V3,
SI, CV, GR and GH rounds and the legacy-records manifest), and parts of it are closed namespaces. This
record is an audit, not a round, so it goes under `verification/audits/` and opens the family
`verification/audits/infrastructure/`.

## Object under test

`tools/lean_axiom_check.py`, git blob `8dec29c7b2c63fc083536a8f62c9056930c30d65` (the same blob at
`374b2ef3`, the commit the Issue cites, and at `63671259`, this record's base). `run_demo.py` checks
the blob before it uses the file. The relevant code:

- `declared_prints(root)` collects every line `^#print axioms NAME\s*$` under
  `ROOT/verification/lean-mathlib/`, with `NAME` in `[A-Za-z0-9_.']+`, and keeps only
  `NAME.split('.')[-1]`.
- `analyse` parses report lines with `AXIOM_LINE` and `NO_AXIOM_LINE` (same character class), again
  keeps the final component, flags any axiom outside `{propext, Classical.choice, Quot.sound}`, flags
  `sorryAx` anywhere in the log, and compares the declared and reported short-name **sets** (SILENT).
- `main` accepts `--root DIR` and `--log FILE`, and with `--log` it sets the build exit code to 0.

## Method

1. **Fixtures** (`fixtures/<ID>/`): synthetic sources `lean-mathlib/OIBridge/*.lean.in`, holding only
   `namespace`/`end` lines and `#print axioms` lines, and a synthetic `build.log` in lake's layout
   (`info: OIBridge/X.lean:LINE:0: 'NAME' depends on axioms: [...]`). The sources carry `.in` so that
   no tool or search that walks the repository for `.lean` files picks them up.
2. **Expectations** (`fixtures/expected.json`) were written by hand from reading the code and committed
   before any checker was run on the fixtures. For each fixture they record the correct outcome
   (`correct`, `correct_findings`), the predicted outcome of the production checker (`tool_predicted`:
   exit status, problem tags, reported count) and the reasoning.
3. **Production checker.** `run_demo.py` copies each fixture into a temporary directory as
   `<tmp>/<ID>/tree/verification/lean-mathlib/OIBridge/*.lean` and `<tmp>/<ID>/build.log`. It then
   runs `python3 -I tools/lean_axiom_check.py --root <tmp>/<ID>/tree --log <tmp>/<ID>/build.log` as a
   subprocess, with `LC_ALL=C.UTF-8`. No wrapper and no import are used: the CLI already takes a root
   and a log.
4. **Independent check of the expectations.** `reference_checker.py` is a separate evaluator that
   imports nothing from `tools/`. It identifies a print by its source file and line, attaches a report by
   the position lake prints before it, requires the reported fully qualified name to extend the
   written name on a `.` boundary, accepts any non-whitespace identifier, and fails closed on unparsed
   report lines. Its verdict and findings must equal `correct` and `correct_findings` for every fixture.
   It is a reference for this demonstration only, not a hardening proposal, and it reads only the
   single-line report layout the fixtures use.
5. **Mutations in both directions.** Each defect fixture is its clean parent with one stated mutation of
   the log, and `run_demo.py` checks that by applying the mutation to the parent. Each clean fixture must
   PASS under both checkers, and each defect fixture must FAIL under the reference.

## Fixtures and outcomes

"Correct" is the reference evaluator's verdict, which equals the hand-written expectation in every row.
"Predicted" and "actual" are exit statuses of the production checker.

| ID | Parent → mutation | Question | Correct | Predicted | Actual | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| C0 | none | clean, unique ASCII names | PASS | 0 | 0 | matches |
| C1 | none | clean, `OIBridge.A.foo` and `OIBridge.B.foo` both reported | PASS | 0 | 0 | matches |
| C1n | none | as C1, prints written namespace-relative (`#print axioms foo`) | PASS | 0 | 0 | matches |
| C2 | none | clean, ASCII and non-ASCII (`OIBridge.R.G₀_apply`) both reported | PASS | 0 | 0 | matches |
| N1 | C1, drop the `B.foo` report | short-name masking | FAIL (MISSING B:3) | 0 | 0 | **false PASS** |
| N1n | C1n, drop the `B.foo` report | masking, namespace-relative prints | FAIL (MISSING B:3) | 0 | 0 | **false PASS** |
| N2 | C2, R axioms → `[propext, Lean.ofReduceBool]` | non-ASCII name hides a forbidden axiom | FAIL (AXIOM R:3) | 0 | 0 | **false PASS** |
| N2e | N2, drop the A report | N2 with no parsable report in the log | FAIL (AXIOM R:3, MISSING A:3) | 1 (EMPTY) | 1 (EMPTY) | matches |
| N3 | C2, drop the R report | non-ASCII print with no report | FAIL (MISSING R:3) | 0 | 0 | **false PASS** |
| N4 | C0, foo axioms → `[propext, Lean.ofReduceBool]` | control: ASCII forbidden axiom | FAIL (AXIOM A:3) | 1 (AXIOM) | 1 (AXIOM) | matches |
| N5 | C0, drop the `bar` report | control: unique ASCII print with no report | FAIL (MISSING A:4) | 1 (SILENT) | 1 (SILENT) | matches |
| N6 | C2, R axioms → `[propext, sorryAx]` | control: `sorryAx` on a non-ASCII report | FAIL (SORRY, AXIOM R:3) | 1 (SORRY) | 1 (SORRY) | matches |
| N7 | C0, foo axioms → `[propext, OIBridge.A.ax₀]` | control: non-ASCII forbidden axiom on an ASCII declaration | FAIL (AXIOM A:3) | 1 (AXIOM) | 1 (AXIOM) | matches |

The production checker's exact output for every fixture is in `results.json`. In each of the four
false-PASS rows it prints `lean_axiom_check: OK (1 named result(s) reported, …; self-test passed)`.

## Verdict

All controls of `run_demo.py` are green. The production checker's built-in self-test passed on every
run, every prediction of exit status, problem tags and reported count matched, every mutation was
verified, and the reference reproduced every hand-written expectation. Over those controls:

- **Short-name masking: false PASS confirmed** (N1, N1n). A report for `OIBridge.A.foo` satisfies the
  SILENT check for a printed `OIBridge.B.foo` that produced no report. N5 shows that the SILENT rule
  does detect a missing report whose short name is unique.
- **Non-ASCII identifiers: false PASS confirmed** (N2, N3). A report for `OIBridge.R.G₀_apply` that
  depends on `Lean.ofReduceBool` is not parsed, so its axioms are not inspected (N2). A non-ASCII
  print is not collected as declared, so its missing report is not detected (N3). N4 shows that the
  forbidden-axiom rule works for an ASCII declaration. N7 shows that the gap is in the identifier
  pattern for declaration names, not in the axiom-list parsing. N6 shows that the `sorryAx` token
  rule is independent of identifiers. N2e fails only through the EMPTY rule, because no report in its
  log parses. A log with at least one parsable (ASCII-named) report takes N2's path instead; this
  record does not measure which path any real build log takes.
- **Clean cases** C0, C1, C1n and C2 pass under both checkers. C2's PASS is vacuous for the production
  checker: it reports one named result where two were printed, and the non-ASCII print is seen by
  neither its declared nor its reported set.

A hardening proposal, for separate review, is in [`HARDENING-PROPOSAL.md`](HARDENING-PROPOSAL.md).

## Limits

- The inputs are synthetic. Nothing here measures whether `main` is exposed. Issue #1162 records that a
  review held off `main` found no current exposure. This record neither re-checks nor relies on that
  finding.
- No Lean toolchain or lake build is run. The log layout follows lake's `info: FILE:LINE:COL:` form, as
  in captured logs on `main` such as
  `verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/evidence/e-run/cells.json`.
  Wrapped multi-line reports and `«»`-escaped names are not exercised.
- With `--log` the checker fixes the build exit code at 0, so its BUILD rule is not exercised here.
- `reference_checker.py` fixes the expected outcomes for these fixtures only. It is not a candidate
  replacement for the production checker.
- No production file is changed (`git diff origin/main -- tools/` is empty), and the release gate is
  unchanged.

## Reproduce

Commit: the commit at which this record lands on `main`. Any later commit with the same record
directory and the same blob of `tools/lean_axiom_check.py` (`8dec29c7…`) gives the same result.
From the repository root, with Python 3 (3.13 was used):

```sh
OUT="$(mktemp)"
python3 -I verification/audits/infrastructure/axiom-checker-integrity-20261106/run_demo.py \
  --out "$OUT"
cmp "$OUT" verification/audits/infrastructure/axiom-checker-integrity-20261106/results.json
```

Expected: exit 0, the verdict line
`run_demo: verdict: the production checker exits 0 on 4 fixture(s) whose correct outcome is FAIL: N1, N1n, N2, N3.`,
and `cmp` reporting no difference. Running without `--out` rewrites `results.json` in place, with
identical bytes.

One fixture by hand, for example N2:

```sh
F=verification/audits/infrastructure/axiom-checker-integrity-20261106/fixtures/N2
R=$(mktemp -d); mkdir -p "$R/verification/lean-mathlib/OIBridge"
for f in "$F"/lean-mathlib/OIBridge/*.lean.in; do
  cp "$f" "$R/verification/lean-mathlib/OIBridge/$(basename "$f" .in)"; done
python3 -I tools/lean_axiom_check.py --root "$R" --log "$F/build.log"; echo "exit=$?"   # exit=0
```

`results.json` (schema `oi-axiom-checker-demo-results`, version 1) contains:

- `tool`: path, git blob and sha256;
- `reference_checker_sha256` and `expected_sha256`;
- `controls`: each control and a boolean, plus `controls_green`;
- `false_pass` and `false_fail`: fixture ids;
- `fixtures`: one row per fixture, with the input digest, `mutation_verified`, the production
  checker's exit status, stdout, stderr, tags and reported count, the reference's verdict and
  findings, the per-fixture checks, and `tool_vs_correct`.

The verdict is computed from exit statuses and the reference's JSON output. The printed tags serve
only as a diagnostic check of the predictions.
