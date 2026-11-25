# Ledger coverage tool, consolidated design r6: decision package (for owner decision, not adopted)

Status: prepared under the owner's authorization of 2026-11-25 (#1169 comment 7159270333), before the r6
text is drafted. It adopts nothing, changes no design, implementation, control expectation or exception,
and grants no exception. Every recommendation below is a proposal; nothing is decided until the owner
records a decision.

Goal link (sec. A.47): A1-EXIT (#1169). The package decides how the verification tool's specification is
consolidated; it decides no scientific question.

## 0. Basis

- Sources, read from exact blobs (git blob / sha256 prefix):
  - v1 `DESIGN.md` (1e3332ed / 447d23f3)
  - `DESIGN-v2.md` (a501e7c1 / 7bd79464)
  - `review-v2.md` (ca180164 / 1a86e3fb)
  - v6.0e `DESIGN-v6.0e.md` (4c18f715 / 4024a31c)
  - amendment r5 (1b4d7694 / 11a9077c)

  The first three exist only on `records/a1-retirement-preservation-20261124` under
  `verification/audits/foundations/a1-retirement-records-20261124/copies/coord2-ledgertool-design/`.
  v6.0e is held on the same branch. r5 is held on `reconcile/a1-amendment-20261125` at `99c51e6a`.
  r4 differs from r5 only at O9-10 and r5's section J.
- Tool commit: `a37992449b452021001277c06c524a30c92dfb87`. CI evidence: run 45569710442.
- `INVENTORY.json` (beside this file) holds 1148 items, 1067 of them normative. Each item gives a source
  line range, the verbatim text extracted mechanically from the source blob, and the source's git blob
  and sha256. Every substantive line of the five sources is covered; table headers and bold labels are
  the only lines not in an item. One exception: `review-v2.md` lines 259-269 (addendum 2's role tests
  and verdict) are outside the addenda v6.0e references. The mapping will record them as not
  referenced.
- `EXPECTATION-SOURCES.json` (beside this file) has one row for each of the 382 controls known to any
  source: the design expectation, the `controls.json` row, the runner predicate (`file:line`), whether
  they agree, and the status the CI run recorded.
- The inventories were made by five read-only agents. The coordinating session verified the findings
  marked "verified" below against the code at the tool commit.

**Correction of an earlier record.** Comment 7158801838 said `a1_controls.py` "never reads
`controls.json`". That is too broad. The engine loads `controls.json` through the configuration's
`controls` reference. It reads each row's `operations` and `direction` (engine/config.py:430-439, the
CONFIG_NO_CONTROLS check) and the file's `control_inputs` (engine/cli.py:622; a1_controls.py:303-306,
RT-DR3W). No code reads a row's `expect`, `reference`, `case` or `by` (verified). The finding that
matters stands: **the expected results in `controls.json` are not enforced**, so a wrong `expect`
cannot fail any run.

## 1. Categories

| Category | Treatment | Section |
|---|---|---|
| Owner decision | Two adopted or incorporated rules conflict, or a requirement is ambiguous or has no defined translation. One option must be chosen. | 2 |
| Mechanical correction | Restores agreement with an unambiguous requirement already approved; cites it. Confirmation only. | 3 |
| Verification defect | The implementation or a control does not enforce an approved requirement. Needs a design correction and a control that detects it. | 4 |
| Identifier migration | Every identifier collision, classified as the same control stated twice or different controls sharing a name. | 5 |
| Missing evidence | A claim whose support is not on `main`. Classified as historical provenance or as evidence a current requirement needs. | 6 |

## 2. Owner decisions

The decisions are numbered OD-1 to OD-31 (OD-31, the identifier migration, is in section 5). "Depends on" lists the decisions whose answer constrains this
one; "Affects" lists those that follow from it. OD-1 is the root: it fixes how every expectation below
is enforced.

### Group A: architecture (root)

**OD-1. Authoritative expectation architecture.** Affects: OD-2, OD-17 to OD-22, and every row of
section 3 that corrects an expectation.
- Problem: three independent statements of each expectation (design text, `controls.json`, runner
  predicate). Only the runner decides. Of 382 controls:
  - 124 agree in all three;
  - 5 conflict (RT-H0, RT-T0, RT-L2, RT-C, SW2);
  - 13 runner predicates are weaker than their stated expectation;
  - 1 preregistered control (S11-7) is not implemented;
  - 42 rest on v1 and v2 expectations that no adopted text translates.
- Options:
  - (a) Every runner reads its expectation from the file and evaluates it. This needs a generic
    evaluator in every runner: a large change to reviewed code, and one evaluator bug would fail
    silently across all controls.
  - (b) An independent gate. Each runner keeps its predicate, but writes a structured record of the
    control id, `actual` (every asserted quantity: outcome, exit, classes, counts, sites) and its
    status. A separate CI step, in the §A.44 manner, reads the expectation file and the records and
    fails when:
    - an id in the file is not recorded, or a recorded id is not in the file;
    - a status is not allowed;
    - any declarative field of `expect` differs from `actual`.

    The gate re-evaluates `expect` against `actual` itself, so a weak runner predicate cannot pass a
    wrong result. Controls that cannot be declared (relational, two-run, process or host, external
    oracle, purity lint: about 60, listed in `EXPECTATION-SOURCES.json`) declare their outcome and
    class, and name a procedural predicate whose result the gate checks.
  - (c) A design-to-file correspondence check only. It catches documentation drift but not runner
    drift.
- **Recommendation: (b) together with (c).** The expectation file is authoritative for expected
  results. The gate makes it decisive. The correspondence check ties each row to the requirement in
  r6 that it tests (requirement id, statement and the normalized expected text). A `NOT RUN` status is
  allowed only with a stated reason and release condition (today RT-T, TR5 and G-A1).
- Consequences:
  - It requires a tool revision: runner output fields, the gate, and the expectation schema
    `oi-control-expectations/1` replacing the `expect` fields of `controls.json`. That revision is a
    later, separately authorized implementation.
  - Mutation evidence must be re-established for the changed code.
  - Reference figures move to a separate informational field, so that a figure cannot pass as the rule.

**OD-2. Where the expected results are stated.** Depends on: OD-1.
- Options:
  - (a) The design tables are authoritative, and the file is generated from them.
  - (b) The file is authoritative, and the design tables are generated from it or checked against it.
- **Recommendation: (b).** The r6 text states each requirement in prose, and gives its control ids and
  a requirement id. The expectation file states the expected results, and the correspondence check
  verifies agreement both ways. Consequence: r6 carries no expected-result tables of its own, which
  removes the drift source behind RT-H0.

**OD-3. Form of r6.**
- Options:
  - (a) An amendment r6 that again amends v6.0e.
  - (b) A complete, self-contained design that supersedes v6.0e, r4 and r5.
- **Recommendation: (b)**, with the mapping table as a separate file. Consequence: after adoption,
  v6.0e, r4 and r5 are historical. Nothing is incorporated by reference.

### Group B: specification conflicts named by the owner

**OD-4. Error class for a pinned input whose blob differs or is missing.**
- The same kind of defect has four classes:
  - ERROR `SOURCE_CHANGED`: D:2895-2896, D:3084, Y10, r5 I2-3;
  - ERROR `CONFIG_UNREVIEWED`: D:1357, TR2;
  - ERROR `CONFIG_INVALID`: D:2983-2984 (an adapter module);
  - FAIL `record-invalid`: D:1319-1320, "except the configuration's own reference".
- **Recommendation: one rule by role.**
  - `CONFIG_UNREVIEWED`: the configuration itself is not admitted from `F`'s pin table.
  - `SOURCE_CHANGED`: any input the admitted configuration pins (adapter, record, rule file, profile
    source) is missing or differs from its pin.
  - `CONFIG_INVALID`: the configuration is malformed or inconsistent.
  - FAIL `record-invalid`: a record whose blob matches its pin but whose content fails its lint or its
    review.

  This needs a conformance check of what the code raises today (not yet done). Any difference becomes
  a verification defect.

**OD-5. Placement of the authority constant** (r5 A.3, the `record_authority.py` file outside the
engine).
- The conflict: D:3007-3009 says every A1 constant moves to the configuration or a pinned adapter, and
  the layout at D:2419-2421 agrees. The owner accepted the placement in r4, because a configuration
  cannot admit its own record directory.
- Options:
  - (a) Keep the constant in the tool file. r6 states a named exception class ("constants that bound
    what a configuration may claim") and amends 16.4 and 12.1 to match.
  - (b) Move the constant into the configuration. This defeats its purpose: it would be
    self-authorizing.
- **Recommendation: (a).**

**OD-6. Wording of "authority" and "authorized"** (r5 A.3, A.4, A.8) against D:477-481, which bars any
output implying authorization, and D:1376-1377, under which the owner, not the tool, confirms a
record directory.
- **Recommendation:** use a neutral term, "admitted record directories". Rename the result field
  "authority match" to "admission match" and the ERROR reason "(authority)" to "(directory not
  admitted)". This is a wording change only, with no change to behaviour. It is one of the identifier
  migrations in section 5.

**OD-7. Paths the tool's landing may touch.**
- D:2441-2442 allows paths only under `tools/` and the audit directory. The tool's pinned workflow,
  `.github/workflows/ledger-coverage.yml`, is outside both and is changed by r5. The class record pins
  it, "owner decision on sec. 12.3", but that decision has no record.
- **Recommendation:** r6 sec. 12.3 lists the pinned workflow path explicitly as the one path outside
  `tools/` and the audit directory.

**OD-8. Rules marked "not adopted" or "for review"** (DR-1a to DR-5, W1/W2, `resid`; D:1613-1620, 1738),
while S13 (D:3020, 3037-3039) requires their outcomes.
- Options:
  - (a) r6 adopts them as tool requirements.
  - (b) The rules are plan records, adopted with the amended plan at `F`. The tool's requirement is the
    rule mechanism; the controls use the current rule files as pinned control inputs, and S13
    acceptance is about the mechanism's behaviour on those inputs.
- **Recommendation: (b).** It keeps the A1 content out of the tool specification (sec. 16 generality),
  and the ESC-1 gap stays where it is: it concerns the W1/W2 record, not the tool.

### Group C: inherited specification conflicts (v1, v2 against v6.0e)

**OD-9. Paths changed identically on both sides at landing.**
- v2:580-582 composes a path that `X` and `M` changed to the same blob as that blob. v6.0e D:2490-2496,
  which takes its wording from v2 addendum 2, counts every path changed on both sides as a conflict.
- This matters for r5: the plan's record directory can be on `M` and on `C` with equal bytes.
- **Recommendation:** v2's rule (equal blobs compose without conflict). Consequence: a conformance check
  of `execution.py:392-442` is needed.

**OD-10. The landing diff equation.**
- v2:585-587 compares `M..L` with `H..X` on the paths `M` did not change. v6.0e D:2498-2499 compares
  path by path "after translation", without that restriction, and "translation" is undefined.
- **Recommendation:** v2's restriction, with "translation" defined as the ledger splices at their
  `M`-translated offsets.

**OD-11. Derived artifacts changed on both sides.**
- v2 allows regeneration or a reconciliation record; v6.0e allows regeneration only, and is
  REVIEW_REQUIRED until regenerated.
- **Recommendation:** v6.0e's rule.

**OD-12. Role of a reconciliation record.**
- v2:583-584 lets a record name the landing blob. In v6.0e (D:2490-2496, 2574-2580) the composition is
  always computed, and a record may only predict it.
- **Recommendation:** v6.0e's rule.

**OD-13. A corpus file changed on `M`.**
- v2 treats it as authorized and checks it by op B under `MAIN`. v6.0e (D:2473-2474) makes it
  `base-drift`, which FAILs unless reconciled.
- **Recommendation:** v6.0e's rule, with v2's op B on `L` retired explicitly. Op B is not implemented.

**OD-14. The set of obligation values.**
- v6.0e never lists them. The code emits HP, RET, MAIN, RECORD, TERMS and DELEGATED (verified).
- **Recommendation:** enumerate exactly those six, with a definition of each.

**OD-15. The class `stale-adjudication`.**
- It is listed as a FAIL class (D, sec. 9), but no v6.0e rule produces it. It is in the code's class
  list (outcome.py:28), and only the inherited U15 expects it.
- Options:
  - (a) Define its condition, from v1 4.6 and v2 3.3.
  - (b) Retire it.
- **Recommendation:** decide together with OD-20. If U14 and U15 are retired, retire the class.

**OD-16. The `read` route and "held".**
- v1 4.2 and 4.7 define `new_site_rules[*].read` entries and the hold rules. v6.0e's sec. 8.1 gives
  hits no `read` route, yet D:2990 still lists `read_entries` (loaded by the code and never used).
  Control U13 depends on the route.
- **Recommendation:** withdraw the `read` route explicitly, define "held" as held by a tracked site,
  and drop `read_entries` from the adapter interface. Depends on: OD-20.

### Group D: inherited controls without a translation

These depend on OD-1 and OD-2.

**OD-17. R1-R14, RT-X, RT-L and RT-L2: restated expectations in v6.0e vocabulary.**
- v2's expectations use `unrelated-authorized` and obligation `MAIN`, which v6.0e no longer defines.
- **Recommendation:** approve one translation:
  - "`unrelated-authorized`" becomes "classified by a side-change class record, or `record-directory`";
  - `MAIN` is kept as an obligation (OD-14).
- With a restated expectation for each control:
  - R1 and R13: the class-pin reading the runner implements;
  - R2: v2's countercontrol (the old-style comparison of `X` against `M`), which is not implemented
    today;
  - R7: its landing expectation under the computed composition (OD-12);
  - R8: PASS asserted, not only the absence of three classes;
  - R14: "at S12" restated as the tool-landing check, together with where that check runs (OD-26).

**OD-18. RT-L2: when it runs, and what "no `base-drift`" means.** Depends on: OD-1 and OD-12.
- v2 runs RT-L2 after the tool lands. v6.0e (D:2592) runs it before landing, on a predicted `M`.
  `controls.json` expects FAIL `base-drift`, the observation recorded at Stage 1.
- The runner passes only with a drafted, unreviewed reconciliation record for `AGENTS.md`, under
  harness admission.
- Options for the safeguard:
  - (a) `base-drift` reconciled by a reviewed record counts as "no `base-drift`".
  - (b) Only the absence of `base-drift` counts.
- **Recommendation:** run it before landing, as v6.0e says, and take (a). Until a reviewed record
  exists, RT-L2 is NOT RUN, with the release condition "reviewed reconciliation record present". It is
  not PASS on a draft. Consequence: the RT-L2 PASS recorded by CI run 45569710442 does not establish
  the safeguard. That is stated in r6's evidence section.

**OD-19. U1-U15 and M1-M11.** They are defined in v1 sec. 8.1-8.2, partly amended by v2 9.1, and
"stand, with v4 classes and exit codes" (D:2096), with no translation table.
- **Recommendation:** restate each in v6.0e classes and exit codes, as the runner implements them,
  except where a sub-decision applies:
  - (a) U13: retire, with the `read` route (OD-16).
  - (b) U14 and U15: retire, or restate under provenance adjudications. Recommendation: retire, with
    OD-15.
  - (c) M7 and M8: restate as an integrity ERROR 65 with the named replay equality false, which the
    runner does. Name the equalities (`build`, `render`) in the replay interface.
  - (d) M11: assert exit 65, not the raised exception.
  - (e) U2 and U10: assert `line_delta` and the per-splice hashes (also listed in section 4).
  - (f) The preflight set: name it. Recommendation: the set the code runs, U1, U4, U10, M1, K1, O9
    and O1, as a stated list. v1's U1-U4 is superseded.

**OD-20. C1-C3, RT-H, and v2's implementation steps S4b-S12.** They are neither restated nor listed as
retired.
- **Recommendation:** retire them formally, in r6's retired-identifier list.

**OD-21. RT-C's expectation.**
- `controls.json` says PASS unconditionally. The design (D:2211) says PASS only with contract evidence.
  The runner gives REVIEW_REQUIRED without evidence.
- **Recommendation:** the design's rule. Without contract evidence the expected result is
  REVIEW_REQUIRED `delegated-evidence-missing`.

**OD-22. Extensions beyond the design that `controls.json` and the runner agree on.**
- GV4 adds an HP-merge case. EI6 adds a third case and the `json.py`/`importlib.py` shadow files. EI5
  and EI7 add countercontrol clauses.
- **Recommendation:** adopt them into r6. They strengthen controls.

### Group E: definitions missing from v6.0e

**OD-23. Sentence splitter version 2.**
- v6.0e cites "splitter version 2 (sec. 6.1)" at D:1065, 1240, 1265, 1673, 1760, 2690 and 2916. v6.0e
  sec. 6.1 does not define it.
- The definition was in v5.1 (line 770) and v5.2 (line 845) as "Sentence splitter, version 2
  (versioned with the schema; O6)". It was dropped in v5.3 and later, while the references remained.
  The code implements one (engine/util.py:168, `sentences_of`, version 2).
- **Recommendation:** restate the v5.2 text verbatim in r6, and add a conformance check against
  `util.py`. Any difference becomes a decision or a defect.

**OD-24. Result schema `/5`.**
- Its field set is defined through v5.5.9, v3, v2 and v1 (D:945-947). The schema file
  `engine/schemas/oi-ledger-coverage-5.schema.json` defines it in fact; it does not require `inputs`,
  and the code never emits it.
- **Recommendation:** r6 states the complete field list from the schema file, with `inputs` withdrawn,
  and the schema file becomes the machine form that the correspondence check covers.

**OD-25. v1 and v2 rules that v6.0e uses but neither restates nor retires.** Recommendation for each:
- the `--out` guard (empty or nonexistent, outside every worktree): restate, after a conformance check;
- `--prior` and `pre_existing`: restate how the endpoint is fixed, or withdraw;
- segment chain and contiguity (v1 3.3), the default single unledgered segment, and "broken segment
  chain" as an ERROR: restate;
- the pin check (guard-pin splice, PIN_OK, updated pin present): restate;
- PIN_MISMATCH's structured fields, and the rule that it comes before any frozen code runs: restate;
- `pin-anchor` findings at op A: give them a class, or withdraw;
- `whitespace_only`: keep it as a diagnostic, defined with its normalization (NFC is not applied by the
  code today), or drop it from U9;
- `anchors.json`: withdraw; only `anchors_sha256` is emitted;
- the rule lint's 8-character minimum literal and its zero-fingerprint check: restate or withdraw;
- the v1 sec. 11 rollback (no workflow trigger; outputs never tracked) and v1 sec. 12 (landing after
  retirement): retire, as superseded by the pinned workflow and sec. 12;
- `self-test --real-trees` and where HP is tracked: retire or restate.

### Group F: wider consistency

**OD-26. Where the tool-landing head is checked against `H`** (v2 S12, used by R14).
- **Recommendation:** in the landing check of the tool's own pull request, stated in sec. 12.

**OD-27. Configuration validation timing.**
- 16.6 says validation runs before any subject. r5's CONFIG_INCONSISTENT checks (directory admission,
  D2-D5) run only in the `M` role.
- **Recommendation:** state the r5 checks as role-dependent validation and amend 16.6 to match. This
  documents the code's behaviour.

**OD-28. TR1's scope** (D:2266: every run without `--freeze` is an ERROR), against allowed harness runs
(D:1548-1550; r5 A.4, A.7 and O9-14).
- **Recommendation:** TR1 applies to chain admission only.

**OD-29. Shape of `config.admission`.**
- It is a string at D:1372, 1549, 2243 and 3100, and an object with `mode` at D:890 and in TR45. The
  code uses an object with `mode` and `snapshot` (cli.py:329, checker.py:83).
- **Recommendation:** the object form, as implemented.

**OD-30. Plan-amendment requirements carried in the tool design** (preserve_check gaps 1-8, cited by
number only, D:1911; gap 6 is dropped silently).
- **Recommendation:** move the gap texts verbatim into the plan amendment's requirements, not the tool
  design, and decide gap 6 there. r6 keeps only a pointer.

## 3. Mechanical corrections

Each restores agreement with an approved requirement.

| # | Correction | Approved requirement it restores |
|---|---|---|
| MC-1 | `controls.json` RT-H0: 3 becomes 7 HP `context-structure-changed` | v6.0e D:2208, D:274, D:376-379 (the design's 7; Stage 1 correction D3, carried from v5.2 on) |
| MC-2 | `controls.json` RT-T0 "3 structure REVIEWs" becomes 7; the runner's `expected` string (a1_controls.py:262) becomes "113/7/7" | D:2209; sec. 10.4 (the `expected` string is the stated expectation, verbatim) |
| MC-3 | The runner's stale RT-H0 `reference_difference` is removed | D:2208 |
| MC-4 | `controls.json` RT-L2 and RT-O9 contradict each other (FAIL against "RT-L2 still PASS"); the row is restated | D:2592-2594 and r5 RT-O9; the exact form follows OD-18 |
| MC-5 | SW2's `controls.json` text ("exactly one FAIL naming that site") becomes D:2218's (one new RET FAIL per site, `H` items unchanged, 584) | D:2218 |
| MC-6 | v6.0e's stale status statements ("paper-only", "v5.5.9 authoritative", gates already passed) become a single current status | r5:3-5; owner adoption, comment 7130449822 |
| MC-7 | "The v2 controls U1-U15 and M1-M11" becomes "v1 controls, amended by v2 9.1" | DESIGN.md sec. 8.1-8.2 |
| MC-8 | D:249 cites "v1 Q5", which does not exist; v1 cites "sec. 7.1" for the preflight, which is sec. 8.1 | v1 text |
| MC-9 | Z9h is defined twice (D:2291 and D:2886); one row remains (the text is chosen in section 5) | the identifier rule (sec. A.30) |
| MC-10 | The LN10 row is malformed (four cells in a three-column table) | table form |
| MC-11 | Section 15's numbering jumps from 6 to 10; item 10's "v6.0d against v6.0c" | document form |
| MC-12 | r5 C's file list omits `adapters/record_directory_controls.py` | the r4/r5 implementation as reviewed (comment 7155870110) |
| MC-13 | 16.8 S13's acceptance list omits r5's O9-1 to O9-25, O9-12b, RT-O9 and I2-1 to I2-8 | r5 A.9 and A.10, as adopted |
| MC-14 | The sec. 9 description of `side-change-unclassified` ("outside every declared class") also covers r5 A.5's directory-completeness case | r5 A.5 and O9-21 |
| MC-15 | `record-dir`'s "additions only as enumerated under `execution/`": `execution/` is undefined (D:1924); it is defined or the clause restated | D:1920-1930 |
| MC-16 | The `ci` class job list (D:1927) lacks `coverage_check`, which sec. 11 item 4 requires (D:2344) | D:2344 |
| MC-17 | FAIL expectations without a class (G3, G5, the countercontrols of sec. 11 items 4, 6 and 13) name their sec. 9 class | D:2083-2084 |
| MC-18 | 12.2's replacement text for a sentence v6.0e does not contain is moved to history | D:2429-2437 |
| MC-19 | Overlap "meets" in v1 is strict, as D:1000-1009 states; v2's residual test, which deletes the literal, is superseded by D:1275 ("No rule ever deletes text") | D:1000-1009, D:1275 |
| MC-20 | The scope-record widening rule (D:2950 against 2958): adding a scope path to a deny profile is not widening, and any other change is | D:2950 as the specific rule |

## 4. Verification defects

The implementation or a control does not enforce an approved requirement. Each needs a design
correction and a distinguishing control. "Verified" means the coordinating session confirmed it at the
tool commit.

| # | Defect | Requirement | Proposed correction and control |
|---|---|---|---|
| VD-1 | Expected results in `controls.json` are not enforced (verified) | the preregistered expectations (sec. 10) | OD-1 (b)+(c): the gate and the correspondence check; a control that plants a wrong `expect` and must fail the gate |
| VD-2 | In a ledgered segment, adjudicated HP sites in a non-conforming file, or a file with an unledgered change, are excluded by `not st.hp` (pipeline.py:342-344, 371-374): no 4.4 search and no site-level item (verified; fails closed) | v1 4.3 point 1, 4.4; D:639 | Search those sites too. Control: an adjudicated HP site in a ledgered segment whose file is non-conforming must yield its site-level item |
| VD-3 | Translation of a pin-duplicated line (`count > 1`, segments.py:158-161) accepts any occurrence at the translated line, with no count, context or ordinal check (verified) | v1 4.3 point 2, 4.4; D:680 | Apply the 4.4 duplicate rule. Controls: a duplicated site whose count changes must be `duplicated`; one with a context mismatch must be `ambiguous` |
| VD-4 | R7's landing run `e7l` is computed and never asserted (controls_engine.py:538-539, verified) | v2 13.4 R7 (OD-17) | Assert its landing expectation |
| VD-5 | R2 does not run the old-style comparison of `X` against `M` | v2 13.4 R2 (OD-17) | Implement it as v2 specifies, or retire R2 under OD-17 |
| VD-6 | S11-7 is preregistered (D:2347, `controls.json`) and implemented by no runner (verified) | D:2347 | Implement it: a literal and a DR-5 match must FAIL both |
| VD-7 | Unreachable code: a1_controls.py:758-765 follows `return` at 757. It holds the only check of A9r's own negative example and of A11r's clean-lint baseline (verified) | D:2171, D:2173 | Make the checks reachable, and assert A9r's negative-example half |
| VD-8 | SW1 computes `bad_delta` (exactly one new FAIL against the unmutated tree) and never asserts it (verified) | D:2217 | Assert it |
| VD-9 | Z9f's adapter half lints an empty source map, so it cannot fail (synthetic_fixture.py:573, verified) | D:2884 | Lint the real adapter sources |
| VD-10 | Weak predicates: O1-O3, O5 and O7 check lint problems, not an emitted FAIL `record-invalid`; O6 asserts no ERROR; RT-I7 does not assert the per-literal split; S11-14 does not assert its landing half; item11-T1p does not assert the 176-line count; R8, R12, U2 and U10 are weak | the rows cited in `EXPECTATION-SOURCES.json` | Under OD-1 the gate re-evaluates the declared `expect` against `actual`; each runner must emit the asserted quantities |
| VD-11 | The runner's RT-T0 `expected` string disagrees with its own predicate | sec. 10.4 | MC-2, and the gate makes such a disagreement impossible |
| VD-12 | `read_entries` are loaded and unused (a1exit_sitemap.py:25-30) | OD-16 | Remove them with the `read` route, or reinstate the route |

The corrections in VD-2 to VD-9 and VD-12 are code changes, made in a later tool revision with its own
authorization. r6 specifies them; it does not make them.

## 5. Identifier migration (sec. A.48 item 3)

Historical records stay unchanged. The mapping index below lists the successor of every renamed
identifier; no identifier is reused. Recommended scheme (an owner decision, OD-31):

| Collision | Classification | Proposed new identifiers |
|---|---|---|
| R1-R14 (v2 four-tree controls) and R1-R13 (record conditions) | different controls, one shared name | four-tree controls become `TT1`-`TT14`; record conditions become `RC1`-`RC13` |
| Finding labels R5, R8, R9 and "v3 R11" | not controls | review-finding labels are not identifiers in r6; cited as "v3 review finding R11" |
| r5 directory conditions D2-D5 and owner-decision labels D1-D8 | different things | directory conditions become `RD2`-`RD5`; owner-decision labels are quoted, not used as identifiers |
| N4 (control) and N4 (finding at D:2585) | different | the control keeps N4; the finding is cited in prose |
| B1-B6, V5 and O9 as both control ids and finding labels; O9 against r5's O9-1 to O9-25 | different | control ids unchanged; r5's controls become `RDIR-1` to `RDIR-25` and `RDIR-12b` |
| Z9h at D:2291 and D:2886 | the same control stated twice, with different text | one `Z9h`; the owner chooses the expected text (the two differ only in wording; the D:2886 form is recommended, as the later and fuller statement) |
| "authority" names (r5 A.3, A.4, A.8) | wording | OD-6 |
| C3 (control) and C3 (decision label) | different | the control is retired (OD-20); the label is quoted |

The migration needs owner approval in advance and an independent non-author review (sec. A.48 item 3).
It changes the code's recorded ids, so it is applied in the same tool revision as OD-1.

## 6. Missing evidence

| # | Claim | Its support | Classification | Proposed resolution |
|---|---|---|---|---|
| ME-1 | The register and infinity engine semantics equal P's `static_new`; selection, counting and splitting equal P's (TRACE 39 to 40) | P's `edits_check.py` (off `main`) | needed by a current requirement | (a) recast as a plan-amendment obligation, verified at `F` against P's checker as frozen with the plan (recommended); (b) land P's checker as evidence; (c) owner exception |
| ME-2 | The parity measurements: 2822/2822, 16905/16905, 273; 4000 cases; 401/399 (TRACE 41 to 43) | scripts lost (`work-v53/`, `work-v54/`, `work-v55/`) | needed by ME-1 | recompute with a retained script under ME-1 (a); otherwise narrow to "measured during design, not retained" |
| ME-3 | Figures measured at `T1'` or from P, which sec. 0.3 makes acceptance references (about 25 rows) | `T1'`, P and lost scripts | historical in r6 | r6 sec. 0.3 makes only figures reproduced by controls on `main` acceptance references; the rest are historical measurements, kept as provenance |
| ME-4 | "Every guarantee of v5.5.9 is kept" | v5.5.9, INVENTORY, reviews (off `main`) | historical | withdrawn as a claim; r6 states its own requirements |
| ME-5 | Owner decisions without a record: the v6.0e status quotes at lines 17, 31, 54, 75 and 95; labels S1, R-D and A-D; the r4/r5 authorization quote at line 7 | none on GitHub | governance | r6 relies on no unrecorded decision; its own adoption is the authority. The quotes stay as history. The owner may record any decision still needed in their own words |
| ME-6 | D1-D4 and V5-D1/V5-D2 recorded only in paraphrase (comment 7099655517) | paraphrase | governance | as ME-5 |
| ME-7 | Review files v6.0b, v6.0c and v6.0d: stated hashes against redacted copies | the records-branch manifest mapping | historical | record the mapping in r6's provenance file; no further action |
| ME-8 | ESC-1, ESC-2 and ESC-4 at design level | `T1'` and P | partly identical to the ESCs | an extension may cover only the identical parts: row 39's parameter-equality clause (ESC-2), row 53's fingerprinted W1/W2 sentences (ESC-1) and row 55's line content (ESC-4). Everything else falls under ME-1 to ME-3 |
| ME-9 | The Stage A V2 basis of r5 change 1 | the reconcile branch and P | historical rationale | provenance; if V2 were false, change 1 would be unnecessary but not unsafe |

## 7. v1 and v2 provenance

They are not landed automatically. If OD-3 (b) is adopted, r6 is self-contained, and v1 and v2 become
historical sources of the mapping. Two ways to make their authority checkable:
- (a) Land them byte for byte as historical records, with a sec. A.42 item 8 trace of their own. This
  is about 20 to 30 further references to classify, many depending on `T1'` and P.
- (b) Keep them on the records branch, and record their git blob and sha256 in r6's mapping. A blob id
  verifies itself only if the object is reachable, so this is verifiable from `main` only if the
  records branch's content lands.

**Recommendation: (a)**, as provenance only, under the same item 8 discipline. The mapping's
verbatim-text check then runs against objects on `main`.

## 8. Dependency summary

- OD-1 → OD-2, OD-17 to OD-22, MC-1 to MC-5, VD-1, VD-10, VD-11
- OD-3 → OD-23 to OD-25 (restated, not incorporated), section 7
- OD-12 → OD-17 (R7), OD-18
- OD-14 → OD-17
- OD-15 ↔ OD-19 (U14/U15) ↔ OD-16 (U13, `read`) → VD-12
- OD-18 → MC-4
- OD-26 → OD-17 (R14)
- OD-31 (migration) → section 5; applied with OD-1's tool revision
- ME-1 → ME-2, ME-8

The decisions in Group B (OD-4 to OD-8), Group C (OD-9 to OD-16) and OD-23 to OD-30 are independent of
one another, apart from the edges listed.
