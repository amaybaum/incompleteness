# Design r6: residual owner decisions (before the r6 text is drafted)

Status: prepared under the owner's authorization of 2026-11-25 (#1169 comment 7160281751), steps 1, 2 and
4. It decides nothing. Each item gives options and a recommendation; nothing is settled until the owner
records a decision.

## Basis and completeness

- `MAPPING.json` holds 1149 rows: one for each of the 1148 inventory items, plus `review-v2.md`
  lines 259-269. Every row has exactly one disposition, a valid r6 section code, the stated
  underlying disposition where it is superseded or retired, the translation where translated, and the
  partner where merged. The check is mechanical (`MAPPING-CHECK.txt`).
  - retained 550, translated 295, superseded 101, historical 82, transferred 38, merged 32,
    retired 28, unresolved 23.
- `EXPECTATIONS-draft.json` (`oi-control-expectations/1`, draft) covers all 382 control ids exactly
  once: 379 live rows plus U13, U14 and U15 retired, with no duplicates (mechanical). It adds 20
  controls of the gate itself (GATE-1 to GATE-20). Of its 399 rows, 34 have `expect: null`; they are
  listed in RD-24 and RD-25.
- `GATE-draft.md` is the draft of r6 section 16: the expectation schema, the runner evidence contract,
  independent extraction, the verdict rules, the correspondence check, the gate's own controls, CI
  under sec. A.44, and the NOT RUN rule with RT-L2 three-valued (Q1, Q2).
- The mappings were made by seven read-only agents. The coordinating session corrected two points
  before this list:
  - **E-1072:** the withdrawal of `stale-adjudication` had been recorded inside a "translated" row. It
    is reclassified as unresolved (RD-9).
  - **The draft's U14 claim:** it says U14 is "preserved-at Z10 and K10". That is wrong. K10 is a
    context adjudication, not a provenance adjudication; the H-series (H1, H2, H6) has only negative
    cases; and no Z10 row concerns adjudication. The claim is withdrawn and the question is RD-9.

The decisions below are numbered RD-1 to RD-35. They are grouped, and each lists its dependencies.
Rows of `MAPPING.json` left unresolved are cited by item id.

## Group 1: verification architecture (depend on OD-1 and Q1)

**RD-1. Mutation evidence and the gate.** The 107 mutants are outside the 382 controls, so as drafted
the gate does not check mutation results.
- (a) Each mutant gets a row in its own namespace of the expectation file, with its killing controls
  as evidence, and the gate checks it.
- (b) Mutation evidence stays outside the gate, under REPRO.

**Recommendation: (a).** It follows from Q1. Mutant ids are part of RD-5.

**RD-2. The double run of sec. 16.7.** It has no control, so the correspondence check would fail on that
requirement.
- (a) Add a control that runs a result twice and compares the bytes.
- (b) Move it to sec. 32 as an outstanding obligation.

**Recommendation: (a).** Determinism is a stated requirement.

**RD-3. Reference figures that the runner asserts today**: RT-H0 113/7/7, RT-A and RT-E 697, the RT-DR
counts at `H`, the RT-T0 site and region counts, the RT-I7 split at `H`, RT-I7A and RT-C.
- (a) They are informational (`reference-difference`), as drafted.
- (b) They are promoted to `expect.counts`.

**Recommendation: (b)** for every figure reproducible from inputs on `main`. Demoting a figure a runner
asserts today would weaken a safeguard, which Q4 forbids. Figures that need `T1'` follow RD-23.

**RD-4. Runner sub-ids** (GV7-tool and GV7-consumer, TR28-tool and TR28-consumer, TR29-tool,
EI2-consumer, EI7-tool, GV6-disk, RT-D-gr58, V27-glossary, TR45-opB). Under the gate an id the file does
not list fails.
- (a) Make them control ids in their own right, with migration-index entries.
- (b) Have the runner aggregate them under the parent id.

**Recommendation: (a)**, with the parent kept as a `composed_of` row, as drafted for EI7, GV7 and S11-2.

**RD-5. Identifiers outside OD-31.** O9-m1 to O9-m17, RT-O9, R15-R19, the runner-only R-prefixed ids,
and v1's RT-T (no records, FAIL) against v6.0e's RT-T (all records, NOT RUN).
- O9-mN becomes `RDIR-mN`.
- RT-O9 keeps its id.
- R15-R19 keep their ids: after the record conditions become RC1-RC13 they collide with nothing.
- v1's RT-T is recorded in the migration index as succeeded by RT-T0.
- Runner-only R ids are handled under RD-24.

**Recommendation: as listed.** Each rename is a sec. A.48 item 3 migration (owner approval and
independent review).

**RD-6. RT-O9's clause "RT-L2 still PASS".**
- (a) `depends_on` RT-L2: RT-O9 is NOT RUN until RT-L2 is released (the draft).
- (b) Drop the clause.
- (c) RT-O9 asserts no `base-drift` itself.

**Recommendation: (a).**

**RD-7. The SKIP status** (v6.0e defines it; OD-1 names only NOT RUN).
- (a) Allowed only with a reason.
- (b) Folded into NOT RUN, with a release condition.

**Recommendation: (b).** One non-run status, always with a release condition.

**RD-8. Both directions for every sec. 10 control** (D:2083).
- (a) Require a restored case on every row.
- (b) Only where the source states one (the draft).

**Recommendation: (b)** in r6. Adding restored cases where none is stated would be new work, outside
consolidation. Listed as a known limit.

## Group 2: safeguards whose retirement or withdrawal needs a decision (Q3, Q4)

**RD-9. `stale-adjudication`, U14 and U15** (E-1072, V2-029, V2-072, V1-099; OD-15, OD-19(b)).
- The purpose traces find two gaps:
  - Retiring U14 removes the only synthetic positive case: a matching adjudication holds, with status
    `adjudicated`. Only RT-T, which is NOT RUN, covers it.
  - Retiring the class leaves a record that matches no subject (an orphan) unreported. A wrong region
    hash still FAILs, through `unauthorized-change`.
- Options:
  - (a) Keep U14, restated as a positive HP adjudication case. Report orphan records under record lint
    as `record-invalid`, with a control planting an orphan. Retire only the class name.
  - (b) Keep `stale-adjudication`, with v2 3.3's condition and U15 restated.
  - (c) Retire all three, accepting both gaps.

**Recommendation: (a).** No safeguard is lost, and the class list stays minimal.

**RD-10. Result fields** (E-106, V1-074, V2-064, V2-065; OD-24, Q3).
- The schema file at the tool commit does not list fields the code emits and controls assert:
  - `line_delta`, the per-splice ids and hashes, `whitespace_only`, `held_by` and `pre_existing`;
  - `new_region_sha256`, `record_checks.anchors_sha256` and `record_checks.pin_findings`.
- `inputs` (v1 and v2: the CLI-supplied object ids and paths) and `pins` (passing pin resolutions) are
  emitted nowhere.
- Options:
  - (a) r6's field list is the schema file extended with the emitted fields above. `inputs` and `pins`
    are restated, each member as a named field unless a conformance check shows it is already bound
    elsewhere.
  - (b) Withdraw `inputs` and `pins`.

**Recommendation: (a).** The conformance check precedes any withdrawal.

**RD-11. v1 and v2 mechanisms that OD-25 left open:**

| Item | Recommendation |
|---|---|
| `--prior` and `pre_existing` (V2-045, V1-024) | restate: the prior endpoint is the last segment's FROM, as `cli.py:872` does |
| the rule lint's 8-character minimum literal (V2-054) | restate |
| the zero-fingerprint lint for allow rules (V2-055) | restate: nothing else forbids an allow rule with no fingerprint |
| `self-test --real-trees` (V2-107, V1-070) | retire, provided the gate never accepts a non-run status without a release condition (RD-7) |
| where HP is tracked (V2-119) | retire as tool text: sec. A.45 rule 6 covers it |
| `whitespace_only` (V1-041) | define it as the code computes it (whitespace collapse and trim, no NFC), as a diagnostic |
| sitemap `relocation` (V1-045) | withdraw: the replay's build equality verifies the whole sitemap |
| `anchor_survives` (V1-051) | withdraw: a review aid, not a verdict input, and never implemented |
| real-object demonstrations RT-M and demos 1, 2 and 4 (V1-120, V1-122, V1-123, V1-124, V1-126) | restate RT-M (M1 on real trees: exactly one added `unauthorized-edit`) and demo 2 (a shift-only mutant of E passes) as real-tree controls; demo 1's 168 moved sites becomes an asserted RT-T0 quantity (RD-3) |
| no writes outside `--out`, and the clone left clean (V1-127, V1-131) | restate, with a control |
| anchor determinism across two Python versions (V1-133) | restate under REPRO, with a control |
| no resolution by line proximity or similarity score (V1-135) | retire as an inspection criterion: preserved by U5-U7 and VD-3's controls |

**RD-12. A symlink or submodule side change outside the record directory** (A-140). It reaches
`classify_side`'s byte read and is refused there.
- (a) Record it as a residual limit.
- (b) Treat it as a verification defect: check the entry type before any read, for every side change,
  with a control.

**Recommendation: (b).**

**RD-13. Retired v6.0e identifiers** (O4, TR4, TR6-TR12, TR16-TR27, TR31-TR44, TR47, TR49, TR53-TR70,
LN9, LN11, LN12). Their per-id dispositions are recorded only in INVENTORY-v6.0e table 2, which is not
on `main`.
- (a) r6's RET restates each id's disposition, from table 2 on the records branch.
- (b) Land table 2 as provenance.

**Recommendation: (a)**, as Q4 requires r6 to state them.

**RD-14. The V4 reversal.** V4 goes from FAIL to PASS, an accepted residual after DR-2 was dropped
(V2-080). It rests on owner decision V5-D1, which is recorded only in paraphrase (ME-6).
- (a) Confirm it knowingly as part of r6's adoption.
- (b) Restore V4's FAIL expectation.

**Recommendation: (a)**, stated explicitly in r6.

**RD-15. Safeguards from v1 retained, which v6.0e does not state**:
- `--repo` (V1-017);
- the tool never writes tracked files or changes git state (V1-027);
- every hit is listed, with no truncation (V1-067);
- synthetic cases use the same object reader (V1-113);
- the release-gate wiring needs its own review (V1-144).

**Recommendation:** retain them, as "safeguards preserved". This adds them to r6 on top of v6.0e's
text; confirm.

**RD-16. MC-18's scope.** Recommendation: the 12.2 replacement text moves to history, but its substance
is kept in r6's status and placement sections: no check is waived, and each later step keeps its own
owner gate.

**RD-17. C1 and the addendum-2 role tests.**
- The draft says C1 is "preserved-at TT1 and TT13". It needs a check that the catalogue holds a
  synthetic op C PASS case.
- Three role tests have no confirmed control:
  - an unclassified change on `M` gives REVIEW;
  - a first parent other than the recorded `M` fails;
  - an unclassified path in `C` fails.

**Recommendation:** confirm by mapping them to existing controls during drafting. If any lacks one, add a
control row (not a retirement).

## Group 3: specification conflicts not settled by the package

**RD-18. OD-4 extended by role.** The cases outside its four roles:
- a record passed with `--classify` that the configuration does not reference: `record-invalid`, as r5
  I2-4 says;
- an execution-identity failure, such as a head branch that is not `main`;
- an unknown ledger schema id with a matching blob;
- ledger integrity failures, M3-M5: the runner raises ERROR 65 `LEDGER_INTEGRITY` or
  `SCIENTIFIC_BASE_MISMATCH`.

**Recommendation:** add two roles, "execution identity (ERROR `CONFIG_UNREVIEWED`)" and "pinned input
whose content fails its integrity rules (ERROR with the named class, as raised)", after the OD-4
conformance check.

**RD-19. The isolation-check refusal.** `tools/ledger_coverage.py:28-31` exits 65 with only a stderr
message: no class and no `result.json`. That contradicts "only USAGE writes no result" (E-104).
- (a) Name an ERROR class and state this as a second documented case without `result.json`, since it
  fires before any import.
- (b) Require a fixed-bytes `result.json`.

**Recommendation: (a).**

**RD-20. Literals r5 added to the engine**: the reserved class id `record-directory`, reason strings and
`.github/`. They are against the purity rule.
- (a) Declare them engine enumerations and the reserved class, which the allowlist admits.
- (b) Move them out of the engine.

**Recommendation: (a)**, after a conformance check against Z9's actual allowlist.

**RD-21. RC10 and RC11** ("as the record states"; r5 A.7 extends RC11). Recommendation: define both
independently in r6, and record any difference from the code as a verification defect.

**RD-22. Z1-Z8 and Z6b.** The design gives a group, of seven defect rows for eight ids. The runner assigns
each id and adds Z6b. Recommendation: adopt the runner's assignment with Z6b, as OD-22 did. It
strengthens the controls.

**RD-23. Figures from controls that run on `T1'`** (N10, N11, RT-I7, RT-T0, item11-T1p).
- (a) They are acceptance references only if `T1'` is reachable from `main`; otherwise historical.
- (b) Land `T1'`'s needed objects.

**Recommendation: (a)**, with the controls' expectations stated over their pinned inputs. The figures
stay acceptance references for the run that has those inputs; their status as evidence follows sec.
A.42.

**RD-24. Runner-only controls with no design expectation.** These 31 rows have `expect: null`:
A5r-generic, ACCEPT-SCHEMA, ADM-CONFIG-AT-F, B4-MEANING, CHAIN-REFUSAL, CONFIG-LINT, E-A1r, E-A2r,
E-A3r, E-A6r, E-A8r, E-L1, E-L3, E-S1r, E-S2r, GV-CACHE, GV-CACHE-AFTER-READ, GV-CACHE-IMMUTABLE,
GV-CACHE-KEY, K1-GRAPH, O3-FILTER, R3-F2, R4-B3, R4-B3-DUP, R5-N6, R6-G6, RL, S7-schema-and-checker,
V3-countercontrol, Z6b, lint-ok, rule-negative.

**Recommendation:** adopt each runner predicate as a restated expectation tied to a named requirement.
This keeps every safeguard. The E-* analogues are recorded as preserved-at their v6.0e controls, unless
the review finds them identical (then merged).

**RD-25. Other null expectations.**
- G-A1: state it from the sec. 7.2 rules; it stays NOT RUN.
- TT12: v2 says FAIL with no class. Recommendation: `landing-extra-change`.
- The purity job's single record id `outcome`: give it the id Z9-STAGED.
- RT-L's outcome: REVIEW_REQUIRED exit 10, as `controls.json` and the runner have it.
- TT7's landing class: `landing-conflict-unresolved`, under the computed composition (OD-12).

**RD-26. Halves not runnable or not recorded.**
- TR45's op-C half: a NOT RUN row, with the release condition "delegated evidence recorded by native
  runs at `X` and `C`".
- EI14: split, with the branch-dispatch half NOT RUN.
- EI7-consumer and the consumer non-acceptance of TR15, TR50, TR51 and TR52: rows, implemented in the
  tool revision.

**Recommendation: as listed.**

**RD-27. Op A record-check failure** (E-1077: listed as FAIL with no class) and `pin-anchor` (V1-080).
Recommendation: `record_checks.pin_findings`, failing with FAIL `record-invalid`. This needs a check of
what the code emits.

**RD-28. Notation.** r5 reuses `P` (configuration path), `D` (its directory), and `E_F` and `E_M`.
Recommendation: `P_cfg`, `D_rec`, `F-entries` and `M-entries`, recorded in NOTE and the migration index.

**RD-29. Module name `record_authority.py`.** Recommendation: keep it. OD-6 is a wording change, and a
rename would re-pin `tool.files` and the class record. r6 notes the historical name.

**RD-30. `record_id` on records** (r5 B.3). Recommendation: keep r5's narrow scope, empty item-2 records
only; LN10 is unaffected.

**RD-31. Z9h's text** (MC-9). Recommendation: the D:2886 form, plus D:2291's "with the adapter
companions in the value set". The combined form is the stronger one.

**RD-32. Where `operations` is stated.** Recommendation: the expectation file carries `operations` for
every row, and `controls.json` is reduced to `control_inputs`. One source.

**RD-33. How `C` is supplied.** Recommendation: state the flag from the code, after a conformance check.
This is mechanical unless the code and the design intent differ.

**RD-34. v1's implementation steps S0-S10.** OD-20 named only v2's S4b-S12. Recommendation: the row
dispositions in `MAPPING.json` (merged, translated, retained or superseded), with V1-131, V1-133 and
V1-135 under RD-11.

**RD-35. Findings the package does not cover.** Each is to be added as a verification defect or a
mechanical correction:
- A2r's runner literal (`six structural`) differs from the design's `(A1)`;
- A5r's expected deny FAIL names no rule alternative (D:2084);
- K4 checks only the K1 half;
- EI7's consumer half is not implemented;
- RT-D's 45 count is omitted from `controls.json`;
- `EXPECTATION-SOURCES.json` cites Z1-Z8 one line off (D:3080-3086), to be corrected before the
  correspondence check;
- E-060's "op B (and L)" needs a check against OD-13's retirement.

**Recommendation:** confirm them as such.

## Notes

- **CI run 45569710442, step 6, exited 1 with verdict PASS.** That is the preregistered rule, not an
  anomaly. RT-T was NOT RUN, so the failed list was non-empty and the exit was 1, as the decision rule
  requires. The gate draft reads structured records, not exit codes (sec. A.44).
- **Conformance checks before the r6 text is final** (reading only, no execution): OD-4, OD-9
  (`execution.py:392-442`), OD-23 (splitter version 2 against `util.py`), OD-25 (`--out` guard,
  PIN_MISMATCH), OD-27, RD-10, RD-18, RD-20, RD-27, RD-33. Each difference found becomes a verification
  defect or a residual decision. None is assumed.

## Dependencies

- RD-1, RD-2, RD-3, RD-4, RD-7, RD-24, RD-25 and RD-26 depend on OD-1 and Q1.
- RD-6 depends on OD-18 and Q2.
- RD-5 depends on OD-31.
- RD-9 depends on OD-15, OD-16 and OD-19.
- RD-10 depends on OD-24.
- RD-11 depends on OD-25.
- RD-18 depends on OD-4.
- RD-23 depends on ME-3.

The rest are independent.
