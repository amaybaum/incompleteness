# Hardening design for `tools/lean_axiom_check.py` (#1162)

**Status: design only, for independent review.** This document specifies a hardened axiom
checker and how it would be validated. It changes no file under `tools/`, no release-gate
step and no proof grade. It implements nothing. Implementation, any run against a real build
log, and replacement of the production checker each need their own owner authorization.

**Authority.** Owner ruling, amaybaum, 2026-11-06 (#1031 comment 6682459524, posted
2026-11-06T10:13:52Z):

> For #1167, only the evidence record is approved. The production axiom checker remains unchanged.
> The independently reviewed hardening design must establish correct full-identity matching,
> Unicode handling, fail-closed behavior and non-vacuous controls before implementation is
> separately authorized.

**Supporting files** (in `hardening-design/`):

- `fixtures/`: 34 synthetic fixtures, P01–P10 positive and F01–F24 negative, in the layout of
  the demonstration in this directory.
- `fixtures/expected.json`: for each fixture, the hardened outcome and the current checker's
  predicted outcome, plus the mutant kill matrix M01–M19. All are hand-derived.
- `run_fixtures.py`: mechanical checks of those fixtures. It does not implement the design.
- `results.json`: the output of `run_fixtures.py`.
- `source_facts.py`: a census of the `#print axioms` lines in the sources.

## 1. What the design answers

The demonstration in [`README.md`](README.md) confirmed two classes of false PASS in the checker
(blob `8dec29c7b2c63fc083536a8f62c9056930c30d65`):

- **Short-name masking** (N1, N1n). Prints and reports are compared as sets of final name
  components.
- **ASCII-only identifiers** (N2, N3). A non-ASCII print is never collected and a non-ASCII report
  is never parsed.

`run_fixtures.py` runs the unmodified checker on this design's fixtures. It exits 0 on 15
fixtures the design fails and nonzero on none the design passes (§7.3). Among the 15 are three
latent gaps the demonstration did not cover:

- the same constant printed in two modules (F03);
- an indented print (F10);
- a print whose name is on the next line (F15).

No print on `main` currently takes the last two forms (§1.1).

### 1.1 Source facts on `main`

`python3 -I hardening-design/source_facts.py` reads only the sources. It runs no Lean, reads no
log and imports nothing from `tools/`. At this record's base `9f4e653b` it prints:

```
{"col0": 6212, "current_pattern_miss": 15, "escaped_names": 0, "indented": 0, "name_on_next_line": 0, "non_ascii_names": 15, "print_lines": 6212, "short_names_multi_module": 26, "trailing_text": 0, "written_names_multi_module": 19}
```

Read as follows:

- There are 6212 `#print axioms` lines under `verification/lean-mathlib/`. All start at column 0.
  None is followed by trailing text, none has its name on the next line, and none uses `«»`.
- 15 have a non-ASCII name. These are exactly the 15 the current pattern misses.
- 26 final name components occur in more than one module. This is the count the Issue gives.
- 19 written names occur verbatim in more than one module.
- 4429 of the 6212 lines do not begin with `OIBridge.`, so most prints are written relative to an
  open namespace. The 4429 is counted with
  `grep -rh '^#print axioms' verification/lean-mathlib --include=*.lean | awk '{print $3}' | grep -vc '^OIBridge\.'`
  at `9f4e653b`: 6193 prints in `OIBridge/`, 1783 of them beginning `OIBridge.`, plus 19 in
  `OIBridge.lean`, none of which begin `OIBridge.`.

The census counts every line that begins with `#print axioms`, including any inside a comment.

## 2. Lean facts the design rests on

The toolchain is pinned in `verification/lean-mathlib/lean-toolchain` at
`leanprover/lean4:v4.33.0`. The following was read from the Lean sources at tag `v4.33.0`. Rows
marked *to confirm* are first checked in the dry run (§8).

| # | Fact | Source at `v4.33.0` | Consequence |
| --- | --- | --- | --- |
| L1 | `#print%$tk axioms $id` elaborates with `withRef tk`, then `realizeGlobalConstWithInfos id`, then `cs.forM printAxiomsOf` | `src/Lean/Elab/Print.lean` | Every report is positioned at the `#print` token. One print can resolve to several constants, which gives several reports at one position. |
| L2 | The message is `'{constName}' does not depend on any axioms` or `'{constName}' depends on axioms: {… MessageData.ofConstName …}` | same | The quoted name is the resolved constant, printed with `MessageData.ofName`, that is, `Name.toString` with escaping. |
| L3 | `Name.toString`: an identifier component is printed bare; a non-identifier component is printed as `«…»`; a numeric component is printed as digits. Components containing `»`, inaccessible names and macro-scoped names are not escaped. | `src/Init/Meta/Defs.lean` | §4 gives the grammar. Non-round-trippable names fail closed. |
| L4 | Identifier characters: `isIdFirst` is ASCII alpha, `_` or `isLetterLike`. `isIdRest` is ASCII alnum, `_ ' ! ?`, `isLetterLike` or `isSubScriptAlnum`. `isLetterLike` covers Greek U+03B1–03C9 except λ; U+0391–03A9 except Π and Σ; U+03CA–03FB; U+1F00–1FFE; U+2100–214F; U+1D49C–1D59F; U+00C0–00FF except × and ÷; U+0100–017F. `isSubScriptAlnum` covers U+2080–2089, U+2090–209C, U+1D62–1D6A and U+2C7C. | `src/Init/Meta/Defs.lean` | §4 transcribes these ranges exactly. |
| L5 | The axiom list is `MessageData.ofList`, which is `sbracket (joinSep xs ("," ++ Format.line))`. It is either one line `[a, b]` or broken after each comma. | `src/Lean/Message.lean` | Reports may wrap (§4.3). The model uses a one-space continuation indent, as the existing round controls on `main` do (`round-ktrans-sep-2-omega4/controls.py`). Any whitespace is accepted. |
| L6 | Axiom names use `MessageData.ofConstName` with `fullNames := false`, so they follow the user's `pp.fullNames` and may be abbreviated relative to open namespaces. | `src/Lean/Message.lean` | Listed axiom names are not guaranteed to be fully qualified (§5, D-AX). |
| L7 | Lake prints `info: <path>:<line>:<col>: <message>`. Lines are 1-based and columns 0-based. | `…/round-ktoken-maxcone-1/evidence/e-run/cells.json` on `main` (`:223:0:` for a column-0 print) | Gives the report key (§3). *To confirm:* the path form, and whether messages of up-to-date modules are replayed. |

## 3. Identity

**Print key.** A print is identified by `(M, L)`, with its column `C` recorded beside it:

- `M` is the source path relative to `verification/lean-mathlib/`, for example `OIBridge/A.lean`;
- `L` is the 1-based line of the `#print` token;
- `C` is the 0-based column of that token.

**Report key.** A report is keyed by the `(M', L')` lake prints before it, with its column `C'`
beside it. `M'` is normalized by removing leading `./` segments and must then be a relative
`.lean` path without `..`. An absolute path is accepted only when it equals
`<root>/verification/lean-mathlib/` + `M`; any other path makes the report UNPARSED.

**Matching.** A report attaches to the print with the same `(M, L)` and to no other. With
`k = (M, L)`:

- no report at `k` gives MISSING;
- two or more identical reports at `k` give DUPLICATE;
- two or more distinct reports at `k` give AMBIGUOUS;
- a single report must have `C' = C` (otherwise POSITION) and a name that agrees with the written
  name (otherwise MISMATCH);
- a report at a key with no parsed print gives ORPHAN, once per key.

**Name agreement.** Let `w` be the written name's components after removing one leading `_root_`
component, and `f` the reported name's components, both parsed by §4. They agree if and only if
`f = w`, or `f` ends with `w` component-wise. This covers:

- fully qualified prints (P01, P02);
- namespace-relative prints (P03);
- `open X` and `open X (a)` (P04);
- `_root_` (P09).

Some prints resolve to a name that does not end with the written one. They fail as MISMATCH:

- `open X renaming a → b` (F23);
- `export`;
- any resolution whose result does not end with the written name.

Such a print has to be written fully qualified. That is a source change, outside this design.

**Why the key is the position, not a name.** Lean resolves the written name (L1) and reports the
constant it resolved to (L2), so the checker does not reimplement name resolution, namespaces or
`open`. The verified identity is `(module M, the fully qualified name Lean reports at M:L)`.

- A key is unique per print line, so a report cannot satisfy any other print. This closes the
  26-short-name masking class: F01 and F02.
- Keying by the reported fully qualified name alone is not enough. When the same constant is
  printed in two modules (P04, F03), one report would satisfy both prints, and the 19 written
  names that recur across modules on `main` are candidates for this.
- The name check does not establish identity. It guards against a report attached to the wrong
  print (F12).

**Ambiguous resolution.** When one print resolves to several constants (L1), Lean emits several
distinct reports at one key. The result is AMBIGUOUS (F22), even if each report passes on its own:
the print does not name a single declaration.

## 4. Name parsing

### 4.1 Name grammar

| Element | Definition |
| --- | --- |
| `name` | `component ("." component)*`, parsed left to right: a `.` inside `«…»` belongs to the component |
| `component` | `plain`, `escaped` or `numeric` |
| `plain` | `idFirst idRest*`, with the character classes of L4 |
| `escaped` | `«`, then any characters other than `»` (spaces, dots and quotes included), then `»` |
| `numeric` | `[0-9]+`. Accepted only in reported names, where Lean prints numeric components such as those of private names (§10). |

Anything else is not a name. That includes a component containing `»`, an inaccessible or
macro-scoped name, and an empty component. A line that needs a name and holds none of these is
UNPARSED. Examples: P05 (`G₀_apply`, a subscript in `isSubScriptAlnum`) and P06 (`«a b»`, an
escaped component with a space).

### 4.2 Print lines

A line is a *print candidate* when it matches `^[ \t]*#print[ \t]+axioms(?=[ \t]|$)`. It is a
*print* when the rest of the line is `[ \t]+ name [ \t]*`, optionally followed by `--` and anything
to end of line (P10). Every other candidate is UNPARSED at `M:L`, which covers:

- a name on the next line (F15);
- a second command on the line (F16);
- trailing text that is not a line comment;
- a block comment opened after the name.

Leading whitespace is allowed (P08), and `C` is its length.

There is deliberately no comment lexer. A candidate line inside a block comment or docstring is
treated as a print, gets no report, and so fails as MISSING. That is a false FAIL, the safe
direction. A lexer that mistook code for comment would hide prints, the unsafe direction. A
`#print axioms` command that does not start its line is not a candidate. Its report then has no
print and fails as ORPHAN.

### 4.3 Report records

A record starts on a physical line of the form

`info: ` PATH `:` LINE `:` COL `: '` NAME `' ` TAIL

where TAIL is `does not depend on any axioms`, followed by optional spaces and the end of the
line, or `depends on axioms: [` LIST `]`, followed by optional spaces and the end of the line.

- LIST is `name ("," ws* name)*`, and `ws` includes newlines.
- A wrapped list continues on later physical lines, each consisting of whitespace and list items,
  until the `]` that closes it (P07, F09).
- The `]` is found by the grammar, not by `[^\]]*`, so an escaped axiom name may contain `]`.
- A record that has not closed within 64 physical lines is UNPARSED at its first line.
- Severities other than `info:` are not accepted.

**Extracting the name.** Find each position in the line where `' does not depend on any axioms`
or `' depends on axioms: [` begins. The name is the text from the opening quote to such a
position, and a position counts only if that text is a `name`. Exactly one position can count:

- Both phrases contain a space.
- A space may occur in a `name` only inside `«…»`.
- A position inside an open escape leaves the component unclosed, so it does not count.
- If two positions counted, the longer candidate would contain the shorter one's phrase outside
  any escape, space included, so it would not count either.

The implementation still asserts uniqueness and reports UNPARSED if it fails.

**Unparsed reports.** A physical line that contains `depends on axioms` or
`does not depend on any axioms` and is not the first line of a parsed record is UNPARSED at
`log:N` (F14). Continuation lines of a parsed record are part of that record.

**The sorryAx scan.** Any physical line containing `sorryAx` gives SORRY at `log:N`, whether or
not it belongs to a record (F19, F20). The rule is unchanged except that it now records a location.

## 5. Rules

The checker exits 1 if any finding is produced; findings are sorted. Every rule is fail-closed:
input it cannot classify is a failure, never skipped.

| Kind | Location | Fires when |
| --- | --- | --- |
| BUILD | `log` | lake exited nonzero (unchanged) |
| SORRY | `log:N` | the physical line contains `sorryAx` (unchanged rule) |
| UNPARSED | `M:L` or `log:N` | a print candidate is not a print (§4.2); a report-like line is not a parsed record, or a record does not close (§4.3); a report path cannot be normalized (§3) |
| AXIOM | the report's `M:L` | a parsed report lists an axiom not in `{propext, Classical.choice, Quot.sound}`, compared verbatim |
| MISSING | `M:L` | a print has no report |
| DUPLICATE | `M:L` | a print has two or more identical reports |
| AMBIGUOUS | `M:L` | a print has two or more distinct reports |
| POSITION | `M:L` | the single report's column differs from the print's column |
| MISMATCH | `M:L` | the single report's name does not agree with the written name (§3) |
| ORPHAN | `M:L` | a report key has no parsed print |
| EMPTY | `log` | no parsed report at all (unchanged rule) |

Several rules can fire on one input. F16 gives UNPARSED and ORPHAN. F18 gives EMPTY and two
MISSING. F20 gives SORRY and AXIOM.

The CLI keeps `--log`, `--root` and `--require-lake`. It adds `--json FILE`, which writes the
sorted finding list and the matched `(M, L, C, fully qualified name, axioms)` table in a stated
schema (§A.44). The exit status is the verdict.

**D-AX, a permitted-name collision (open; needs a decision).**

- **The risk.** Because of L6, a listed axiom is displayed with `pp.fullNames` false. A
  non-permitted user axiom whose abbreviated display equals `propext`, `Classical.choice` or
  `Quot.sound` would pass the verbatim check. Matching names verbatim is still the correct rule.
- **The safe side.** A permitted axiom displayed in abbreviated form, for example `choice` under
  `open Classical`, fails. That is a false FAIL, the safe direction.
- **Evidence.** Ten modules on `main` contain an `open … Classical` line, and the current checker,
  which also compares verbatim, is green in CI. That is consistent with no abbreviation occurring for these
  names, but it does not establish it.
- **What the dry run checks** (§8 criterion e): every listed axiom name in a real build, verbatim.
- **Closing the collision.** It needs one of the following, each a decision outside this design:
  - setting `pp.fullNames = true` in the build's Lean options, a build-configuration change;
  - a comment-aware source lint forbidding `axiom` declarations whose final component is `propext`,
    `choice` or `sound`.

**Rules unchanged from the current checker.**

- the sorryAx token scan;
- the nonzero-exit rule;
- the three permitted axioms;
- the EMPTY rule;
- `--require-lake`;
- a self-test at every invocation.

The current checker's only other rule is SILENT. SILENT fires when no report whose name the
current pattern can parse has the print's final name component. On such an input the design fires
MISSING, MISMATCH, UNPARSED or POSITION, with one exception. The report at the print's position may
carry a fully qualified name the current pattern cannot parse, for example a namespace component
with a non-ASCII letter or with `?`. Then the design passes, and the current FAIL is a false FAIL.
The design is therefore not a superset of the current checker on every input. On the 34 fixtures,
the design never passes an input the current checker fails (§7.3).

## 6. Self-test

The hardened checker's self-test runs the 34 fixtures at every invocation, as the current
self-test runs its synthetic logs. Each fixture must give exactly its `hardened` verdict and
finding list from `fixtures/expected.json`.

The five existing self-test cases are kept, re-expressed with a source tree and lake position
prefixes: clean, sorryAx, forbidden axiom, dropped print, nonzero exit. The nonzero-exit case is
the only BUILD case, because `--log` fixes the exit status at 0 and the fixtures here run through
the CLI.

The expectations were written by hand from this design before anything ran on the fixtures; the
commit `76b8c675` on this record's pull request is provenance for that order. They are checked by
independent review, because no implementation exists. An implementation that disagrees with a
fixture is resolved by re-deriving the outcome from this design, never by editing the expectation
to match.

**Both directions, for both failure modes.** In each pair the negative fixture is its positive
parent with one log mutation, which `run_fixtures.py` verifies.

| Mode | Positive (must PASS) | Negative (must FAIL) |
| --- | --- | --- |
| Short name shared across modules | P02, P03 | F01, F02 (MISSING) |
| Same constant printed in two modules | P04 | F03 (MISSING) |
| Subscript identifier | P05 | F04 (AXIOM), F05 (MISSING), F20 (SORRY and AXIOM) |
| `«»` name with a space | P06 | F08 (AXIOM) |
| Wrapped report | P07 | F09 (AXIOM) |
| Indented print | P08 | F10 (MISSING) |
| ASCII baseline | P01 | F06 (AXIOM), F07 (MISSING), F11 (DUPLICATE), F13 (ORPHAN), F14 (UNPARSED), F17 (POSITION), F18 (EMPTY and MISSING), F19 (SORRY), F21 (AXIOM) |
| Misattributed report | P02 | F12 (MISMATCH) |

Some negatives have no passing counterpart. They are the deliberate fail-closed boundaries:

- F15, name on the next line (UNPARSED);
- F16, two prints on one line (UNPARSED and ORPHAN);
- F22, ambiguous resolution (AMBIGUOUS);
- F23, `open … renaming` (MISMATCH);
- F24, an empty tree and an empty log (EMPTY).

P09 and P10 pin the `_root_` and trailing-comment allowances.

## 7. Countercontrols

### 7.1 Every rule decides at least one fixture

Every rule except BUILD is the only kind of finding on at least one negative fixture:

| Rule | Sole fixture |
| --- | --- |
| SORRY | F19 |
| AXIOM | F04 |
| MISSING | F01 |
| DUPLICATE | F11 |
| AMBIGUOUS | F22 |
| MISMATCH | F12 |
| POSITION | F17 |
| ORPHAN | F13 |
| UNPARSED | F14 (log), F15 (print) |
| EMPTY | F24 |

So no rule is redundant on the fixture set. `run_fixtures.py` checks this.

### 7.2 Mutant kill matrix

Each mutant changes one rule of the design. The implementation's CI must run every mutant through a
test-only switch, never in the production path. Each mutant must change the verdict of the listed
fixtures, which `run_fixtures.py` checks against the hand-derived verdicts in `expected.json`.

| Mutant | Change | Killed by (mutant's verdict) |
| --- | --- | --- |
| M01 | match by final name component (current key) | F01, F02 (PASS) |
| M02 | match by fully qualified name, ignoring position | F03 (PASS) |
| M03 | ASCII-only grammar, fail-closed kept | P05, P06 (FAIL) |
| M04 | ignore unparsed report-like lines | F14 (PASS) |
| M05 | ignore unparsed print candidates | F15 (PASS) |
| M06 | collect prints at column 0 only | F10 (PASS), P08 (FAIL) |
| M07 | drop ORPHAN | F13 (PASS) |
| M08 | keep the first of identical reports | F11 (PASS) |
| M09 | keep the first of distinct reports | F22 (PASS) |
| M10 | drop the name check | F12, F23 (PASS) |
| M11 | drop the column check | F17 (PASS) |
| M12 | parse reports from one physical line | P07 (FAIL) |
| M13 | keep a leading `_root_` | P09 (FAIL) |
| M14 | reject a trailing line comment | P10 (FAIL) |
| M15 | drop EMPTY | F24 (PASS) |
| M16 | drop the sorryAx scan | F19 (PASS) |
| M17 | permit `Lean.ofReduceBool` | F06 (PASS) |
| M18 | require the reported name to equal the written name | P03, P04 (FAIL) |
| M19 | key by line without module | P02 (FAIL) |

Mutants killed by positive fixtures, namely M03, M06, M12, M13, M14, M18 and M19, show that the
positives guard against a design that is too strict. The others show that the negatives guard
against one that is too weak.

### 7.3 The current checker as a baseline

`run_fixtures.py` runs the unmodified checker on all 34 fixtures, and every exit status, tag set
and count matched its hand prediction. It exits 0 on 15 fixtures the design fails:

- F01–F05, F08, F10–F17 and F22.

It exits nonzero on none of the fixtures the design passes. The fixtures therefore separate the
two checkers in one direction only.

### 7.4 Controls of `run_fixtures.py` itself

The controls are:

- the tool blob pin;
- every P fixture passes with no findings, and every F fixture fails with findings;
- findings are sorted and of known kinds;
- every rule has a fixture on which it fires alone;
- every mutant flips its killers;
- the tool's self-test passed on every run;
- mutations are verified;
- every current-checker prediction matched.

All are green. Two runs give byte-identical `results.json`.

Countercontrols were run on a scratch copy before this record landed. That is provenance, and it
is reproducible by repeating the edits. Each of the following turned the matching control red and
suppressed the verdict:

- flipping one mutant's expected outcome;
- deleting F24;
- changing one prediction;
- unsorting one finding list;
- giving a P fixture a finding;
- appending a byte to the tool;
- appending a line to a fixture log.

## 8. Migration: dry-run comparison

This section specifies the comparison; it does not authorize running it. The dry run reads a real
build log, and the ruling commissioning this design does not authorize that. It needs separate
owner authorization, as does implementing the candidate. During the dry run the candidate lives
outside `tools/`, and the production checker stays unchanged.

**Procedure.** One CI job, dispatched on an exact commit `X` of `main`:

1. Check out `X` with full history. Record the toolchain and lake versions.
2. Run `lake build` in `verification/lean-mathlib/`. Capture stdout and stderr to `LOG` and the exit
   status to `RC`.
3. Run the current checker: `python3 -I tools/lean_axiom_check.py --log LOG`, recording its exit
   and output.
4. Run the candidate: `--root . --log LOG --json C1.json`.
5. Run `source_facts.py` at `X`.
6. Run `lake build` again with the warm cache to get `LOG2`, then run the candidate on it, giving
   `C2.json`. Repeat step 4 on the same `LOG`, giving `C1b.json`.
7. Run the candidate's self-test and the mutant matrix of §7.2.

**Acceptance.** Every criterion is read from exit statuses and the JSON files (§A.44):

| | Criterion |
| --- | --- |
| a | `RC = 0` and the current checker exits 0. Otherwise the baseline is red and the dry run is void. |
| b | The candidate's parsed prints equal `source_facts.py`'s `print_lines`. Every print has exactly one report: MISSING, DUPLICATE and AMBIGUOUS are all 0. |
| c | UNPARSED, ORPHAN, MISMATCH, POSITION, AXIOM and SORRY are all 0, and there is no EMPTY. |
| d | Every short name the current checker counts as reported is the final component of a matched name. The prints with non-ASCII names, 15 at `9f4e653b` (count recomputed at `X`), are matched and axiom-checked. |
| e | D-AX: every listed axiom name is one of the three permitted names verbatim. The multiset of axiom lists is recorded. |
| f | `C1.json` and `C1b.json` are byte-identical. `C2.json` has the same matched `(M, L, fully qualified name)` set as `C1.json`, which tests message replay for up-to-date modules. |
| g | The self-test and every mutant kill pass. |

**Disposition of findings.**

- Every finding is triaged individually.
- A real defect in the corpus gets its own Issue and is never suppressed.
- A design defect sends the design back for revision and fresh review. Examples are a lake path
  form not covered by §3, or a Lean message form not covered by §4.
- No rule is relaxed, and no allowlist or exemption is added, to make the dry run pass.
- A print that fails only by MISMATCH or UNPARSED, such as a renamed `open` or a print inside a
  comment, is corrected in the source under its own authorization, not exempted in the checker.

**Replacement.** Replacement is authorized separately, only after a clean dry run and independent
review. It keeps the release-gate invocation (`--require-lake`) and the CLI, and it repeats the
comparison at the replacement commit.

## 9. Out of scope

- Any edit to `tools/lean_axiom_check.py`, the release gate or its workflow, and any
  implementation of this design.
- Any Lean build, and any run against a real build log on `main`, including the dry run of §8.
- Proof grades and scientific status, which this changes in neither direction.
- Source changes to prints, such as rewriting a renamed `open` fully qualified, or adding
  `pp.fullNames`.
- Coverage: whether every theorem that should have a `#print axioms` has one. The checker checks
  only the prints that exist.
- Reports from dependency packages. They have no print in the scanned tree and would fail as
  ORPHAN; the dry run shows whether any appear.
- The overstated gate wording recorded in #1162 item 3, which has its own authorization path.

## 10. Open points for the reviewer

1. **L1–L7.** The facts were read from the pinned sources, not observed in a build. Criteria b, c
   and f confirm them. If the lake path form, the column units or the replay behaviour differ, the
   design changes before implementation.
2. **D-AX** (§5) needs an owner decision on how the collision is closed.
3. **Private declarations.** Lean names private constants `_private.<module>.<n>.<name>`. Whether
   the report prints that form under L2 is not established. Until it is, a printed private
   declaration fails as MISMATCH. If the dry run shows such names, a reviewed rule can strip exactly
   `_private.<M as dotted name>.<digits>.` before the agreement check.
4. **Prints inside comments** (§4.2) fail as MISSING. The census cannot tell whether any of the
   6212 lines is inside a comment, but the dry run will show it.
5. **Severity.** Only `info:` starts a record. If a build option turns infos into another
   severity, the records become UNPARSED. That is safe, but it would need a design change.

## Reproduce

From the repository root:

```sh
python3 -I verification/audits/infrastructure/axiom-checker-integrity-20261106/hardening-design/source_facts.py
OUT="$(mktemp)"
python3 -I verification/audits/infrastructure/axiom-checker-integrity-20261106/hardening-design/run_fixtures.py --out "$OUT"
cmp "$OUT" verification/audits/infrastructure/axiom-checker-integrity-20261106/hardening-design/results.json
```

Commit: the commit at which this record lands on `main`. Any later commit with the same record
directory and the same checker blob `8dec29c7…` gives the same result. `source_facts.py`'s figures
depend on the sources at that commit.

Expected output:

- `source_facts.py` prints the JSON line of §1.1, provided the sources are unchanged.
- `run_fixtures.py` exits 0 with the line `run_fixtures: the production checker exits 0 on 15
  fixture(s) the design fails: F01, F02, F03, F04, F05, F08, F10, F11, F12, F13, F14, F15, F16,
  F17, F22; it exits nonzero on 0 fixture(s) the design passes: none.`
- `cmp` reports no difference.

`results.json` uses the schema `oi-axiom-checker-hardening-fixtures`, version 1. It records:

- the tool blob and sha256;
- the sha256 of `expected.json`;
- every control and `controls_green`;
- the fixtures covered by sole-kind checks;
- the two disagreement lists;
- one row per fixture: input digest, mutation check, the design's verdict and findings, the
  current checker's exit, stdout, stderr, tags and count, whether the prediction matched, and
  `current_vs_design`.
