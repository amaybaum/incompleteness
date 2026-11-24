# Commit-independent ledger and terminology verification tool: design v5.5.10a

## Status and authority

This is a paper-only design. Nothing is implemented, committed, pushed or published under it.

- It supersedes v5.4 where they differ. `DESIGN.md` (v1), `DESIGN-v2.md` to `DESIGN-v5.md` and
  `DESIGN-v5.1.md` to `DESIGN-v5.4.md` stay as written. This document is complete in itself; it is
  not a diff. It is intended as the final design version.
- **v5.5.10a is the bounded correction of the v5.5.10 draft that the owner approved on 2026-11-24**
  after its independent review (`review-v5.5.10/review.md`, sha256
  78dc33d3a99405cbb7150de77ad1550495643f4f3121f51795bd0312fc897a8c, verdict REJECT on B1 and B2).
  It supersedes the v5.5.10 draft (sha256
  fae222cd5caab23cec5a80bfa9d0db083efad8311e3985cd7b553bec87748e0c) and, like it, amends the adopted
  v5.5.9, which stays authoritative until an independent exact-version review returns ACCEPT and the
  owner adopts v5.5.10a. It makes only these corrections: B1, the v5.5.9 deletion rule restored,
  with the thread's deletion events read through GraphQL under fail-closed handling (admission
  point 3, "Deletion events"; TR35 restored; TR85; new TR86, TR87, HV11, HV12); B2, an owner comment
  known to be edited whose earlier text is unavailable refuses (TR79, HV5); the review's nits N1
  (object-id wording), N2 (revisions above 100), N4 (the anchor fetched before admission), N5
  (regular-file entries) and N7 (the label of sec. 15 item 6), N8 being HV12; and F4 stated as an
  unresolved feasibility risk that stops and escalates. Nits N3 and N6 are observations and change
  nothing. Implementation, the validation stage and every test write stay separately authorized.
  `CHANGES-v5.5.10a.md` lists every changed passage.
- **v5.5.10 amends the adopted v5.5.9 for the owner decisions HS-1 to HS-7 of 2026-11-24 only:**
  the sources from which the tool reads the host. It is authoritative only after an independent
  review returns ACCEPT and the owner adopts it; until then the authoritative design is v5.5.9
  (sha256 cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9). It changes sec. 5 (the
  consumer's verification, integrity errors), sec. 6.3 (trust root, authority changes, the freeze
  ledger's residual, admission points 2, 3 and 9, the admission snapshot, residual trust), sec. 7.2
  (clones and host-run records), sec. 10.4 (TR25, TR35; new controls TR71-TR85), the new sec. 10.5
  (real-host validation, HV1-HV10), sec. 15 (items 1, 7-9) and S13. No other rule changes, and no
  control expectation is relaxed. Implementation is not authorized by it. `CHANGES-v5.5.10.md`
  lists every changed passage. The decisions (owner amaybaum, 2026-11-24), as they reached this
  writer through the coordinating session, with no comment id held (sec. 15 item 1):
  - **HS-1.** Hash-verified local git for repository history; the host's REST API for its metadata.
  - **HS-2.** Option G: the existing comment edit-history requirements are kept, and GraphQL is
    restricted to information unavailable through REST.
  - **HS-3.** Fail closed whenever required edit history is missing, unreadable, incomplete or
    unverifiable; an unreadable revision is never silently skipped.
  - **HS-4.** Shallow and partial clones are rejected unless their completeness for all required
    objects can be independently established; replace and graft mechanisms are ignored.
  - **HS-5.** `updated_at` is not relied on as proof that a comment has never been edited.
  - **HS-6.** Deleted comments are investigated separately, distinguishing what the host exposes
    from what cannot be reconstructed; complete historical coverage is not claimed without evidence.
  - **HS-7.** The API budget is measured, and the remaining GraphQL behaviour verified, in a
    separately authorized CI validation stage.
- **v5.5.9 amends the adopted v5.5.8 for owner decision D-1 of 2026-11-24 only.** It is
  authoritative only after an independent check returns ACCEPT and the owner adopts it; until then
  the authoritative design is v5.5.8 (sha256
  f531948147b3638c5ad567f5ccf0eedfd04650a30be9fd0a9f2084aa13a77ad2). It changes one sentence of
  sec. 15, item 0a, on when the empty freeze ledger lands. Nothing else changes.
- **v5.5.8 is a draft amendment of the frozen v5.5.3.** It is authoritative only after an
  independent review returns ACCEPT and the owner adopts it; until then the frozen design is v5.5.3
  (sha256 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379). It supersedes the
  v5.5.7 draft. It implements only
  two owner decisions of 2026-11-23 on the design issues of the fourth Stage 1 review
  (`review-stage1-r4/review.md`, sec. 7): DI-1, option B, the owner identity of a comment (sec. 6.3,
  "Owner at creation"; controls TR54-TR62, TR64-TR70); and DI-2, option A in its narrow form, the
  lineage of a superseding record (sec. 6.3, record lint and the field `supersedes` of `A`;
  controls LN1-LN12 and TR63). Nothing else changes. `CHANGES-v5.5.8.md` lists every changed
  passage.
- **v5.5.3 reopens the frozen v5.5.2 for K7 only.** By owner decision of 2026-11-23, the frozen
  design v5.5.2 (sha256 835ff356200349db7689ea41ce936349015fb70f47b35a508945d681a8604323) is
  narrowly reopened for K7, and v5.5.3 changes nothing else. K7 concerns the execution-identity rule
  (sec. 6.3, trust root point 3). The authority record at `tools/ledger_coverage/authority.json` and
  the workflow at its separately pinned path `A.workflow.path` are explicitly permitted, each still
  subject to exact content-hash verification. Every other file under `tools/ledger_coverage/` not
  named by `A.engine_pins` stays prohibited. This is an explicit allowance for these two required,
  independently pinned components only, not a general exception, and it weakens no identity,
  admission or authorization safeguard. If either of them is modified, substituted or duplicated,
  the run is refused (controls TR48-TR53). `CHANGES-v5.5.3.md` lists every changed passage.
- **v5.5.2 is the frozen design.** By owner decision of 2026-11-23, design v5.5.1 (sha256
  8befd35c74b8e4dfa241e360d891de3222b3f878ca2aaf23ceaae1d00fbed649) is accepted, and v5.5.2 adds
  only N3 of the final bounded review. Every acceptance-time append to the freeze ledger requires its
  own owner approval comment, verified like a designation (sec. 6.3, "The freeze ledger"; control
  TR47). After v5.5.2 the design is frozen. `CHANGES-v5.5.2.md` lists every changed passage.
- **The owner's final decisions of 2026-11-23:**
  - **D1.** The residual is accepted that a withdrawal created and deleted before any check observes
    it may be undetectable (sec. 6.3, residual trust assumptions). This is a stated trust
    limitation, not a claim of complete protection.
  - **D2.** The three stricter refusal classes of sec. 6.1 are accepted, with the evidence that
    valid frozen-plan operations are not rejected: (i) a splice for the unselected variant, (ii) one
    splice covering two edits, (iii) chained edits.
  - **D3.** The append-only freeze ledger is adopted, with N3.
  - **D4.** The authority record at `tools/ledger_coverage/authority.json`, the versioned comment
    forms, authority changes that are independently reviewed and owner-approved, and numeric owner
    id 7273571 are adopted.
- v5.5.1 differs from `DESIGN-v5.5.md` (sha256
  74db584a5bdb861519f9703e3b5d102ba07a60dfd0e8f89ea183bd89a80b52a4) only by the corrections F2
  (delegated evidence in the admission snapshot; replay of op-C results), F1 (control S11-58k
  completed) and N1 (wording of chained edits) of the final bounded review,
  `review-v5.5/review-v5.5.md` (sha256
  8c77254a7291e75fe8caff01185e3f9896ace2a18a881497241fc4c51cc5f9ac, verdict ACCEPT WITH REQUIRED
  CORRECTIONS). `CHANGES-v5.5.1.md` lists every changed passage.
- v5.5 applies exactly the independent review of v5.4, `review-v5.4/review-v5.4.md` (sha256
  bc0921e37a1d941f3845b200dd90e744dcf0fdd635f8cac7fb2b6ca9d67af854, verdict REVISE: V1-V5), its
  addendum `review-v5.4/review-v5.4-addendum.md` (sha256
  8559e4336e293a5b879a5154c928fcad209be8e1a1aa37d15ddab459b1059ef3: C1-C4), and the residual-trust
  list, under the owner decisions of 2026-11-23 on that review, called R-D1 to R-D5 here (stricter
  refusals, withdrawal integrity, execution identity, the authority configuration, durable
  evidence). `DESIGN-v5.4.md` (sha256
  a980251709485e7c1b26c91c32a18d8fdf412adb6f6d8058c382892bc29b9cb3) and both review files were
  verified before this revision. `CHANGES-v5.5.md` lists every changed passage. The owner's stopping
  rule applies to later reviews: a finding blocks only if it is demonstrated or supported by a
  reproducible counterexample and violates an existing requirement or an agreed pass condition.
- v5.4 applies the independent review of v5.3, `review-v5.3/review-v5.3.md` (sha256
  20f2c0c3e867cecdbc161dee88df12973f64101acbb15ae1d8a31b6ba1b88b66, verdict REVISE): W1 (P's
  edit variants, sec. 6.1), W2-W4 (repository, run and designation binding, sec. 5 and 6.3), and
  the optional O2 (sec. 6.2) and O3 (sec. 5). It also applies the owner decisions of 2026-11-23 on
  the authority values, called A-D1 to A-D5 here (owner id, edited designations, supersession and
  withdrawal, repository and workflow, durable evidence), and the owner's addendum on the trust
  root of the authority record (sec. 6.3). `DESIGN-v5.3.md` (sha256
  3b24ac8e5e651a5a5651ace69d36112d29e1afe9388696f056631f1c59e7773d) and the review were verified
  before this revision. `CHANGES-v5.4.md` lists every changed passage.
- v5.3 applies the independent review of v5.2, `review-v5.2/review-v5.2.md` (sha256
  15260f0957ba81bb555c413a7e73db201a828f059a073a601fbe471da2c34fd0, verdict REVISE): required
  corrections V1-V8 and optional point O1. Its two blocking points are the register and infinity
  parity with P's per-edit check (V1; sec. 6.1) and the authority for `F`'s designation (V2;
  sec. 6.3). `DESIGN-v5.2.md` (sha256
  195d1e288b1d6750c333b4707332868d351926793ad2b2a555d64e3bd78f4aeb) and the review were verified
  before this revision. `CHANGES-v5.3.md` lists every changed passage. (In this list, V1-V8 name the
  v5.2 review's corrections; elsewhere in this document V1-V27 are adversarial controls.)
- v5.2 applies the independent Stage 1 review, `review-stage1/review-stage1.md` (sha256
  007d4ada8c19cb3103073d80f75c9721d57c908f7cd8813a7b52c568449d4b6a, verdict REVISE), of the Stage 1
  implementation (local commit 8c1e628a08272ad9414929fa8e003020e1cc2234; report
  `impl-stage1/REPORT.md`, sha256 9093f93a002fcc2dfa5574468ed15bf37044a6434c59b2f2d81d3eecde7cad9f):
  its design corrections D1-D8, and a specification against which the implementation fixes its
  blocking defects B1-B6. `DESIGN-v5.1.md` (sha256
  0c4ff0e60331d0e9604ece0c997dec472b3f977bf24384676d74f850bff4a3fe) and the two review inputs were
  verified before this revision. `CHANGES-v5.2.md` lists every changed passage.
- Owner decisions on the Stage 1 review (2026-11-23), called S1-D1 to S1-D3 here: S1-D1, the W1
  self-match is resolved by option B (sec. 6.2 step 3); S1-D2, apply D1-D8; S1-D3, specify
  configuration admission, native delegated execution, the classification of `C`, widening reviews,
  engine purity over the adapter companions, and control reporting (B1-B6). B7 (RT-L2 at current
  `main`) is an owner decision outside this design (sec. 15).
- Authority: owner decision #1169 c.7093128173 (amaybaum, 2026-11-23T06:13:50Z). It approves in
  principle the exception-free verification route. That route has four steps: the tool lands first
  through its own review and merge decision; `PREREG.md` is amended and frozen again so that every
  mandatory check of sec. 11 passes as written; the trials are rerun; the retirement is executed.
- That decision holds implementation, push, pull request, merge, the plan edit and execution.
- Review inputs: `review-v2.md` (sha256 1a86e3fb...eb9, addenda 1-4) and `review-v3.md` (sha256
  5041232c6c2c0fe3b7ec939564dd669dd4f3f4f82d8ce79d365c28e7a6d2e4ff), verdict REVISE, required
  corrections R1-R11. `DESIGN-v3.md` has sha256
  855e3da00341a0c3cb7234ba7473870115164d809adeb698dd80752bf3d29d9d.
- `review-v4/review-v4.md` (sha256 113d1c129ad761114a4b529c5ec90d6d79a224d468bffa0cbe7b3cfd922cca6f),
  the independent bounded delta review of `DESIGN-v4.md` (sha256
  3cde34d2209dbcd6c5f03f991fb27385c2e709b9bd1557b60d965f9aa219c625) and `CHANGES-v4.md` (sha256
  c3214f10ea57879e7771bcacd2ea9a446b3fcc27c7464ad0d41cf665c145fdca): verdict ACCEPT WITH REQUIRED
  CORRECTIONS, required corrections V1-V8, optional points O1-O7. All three hashes were verified
  before this revision.
- Owner decisions of 2026-11-23 on v3's open points 1-4 (D1-D4 below): adopt the v3 review's
  recommendations.
- Owner decisions of 2026-11-23 on the v4 review (called V5-D1 and V5-D2 here, to keep them apart
  from D1-D4): V5-D1, drop DR-1d and DR-2 from the active deny set with a recorded history, and
  keep DR-3 with its real witness in `AGENTS.md` at `H` (sec. 6.4, 6.4.1); V5-D2, widen `resid` as
  the v4 review's V8 proposes (sec. 6.6).
- All of these decisions, S1-D1 to S1-D3 included, reached this writer through the coordinating session
  (session_013T6pfKuv5mi3MXtKjH2tZb). This writer holds no comment id for them; the record that
  quotes them with author, time and comment id (sec. A.42 item 7) is still to be cited (sec. 15).
- Owner standing instructions that bind this revision: correct the design and its expected
  outcomes to match independently verifiable behaviour; never weaken a check to turn a real-tree
  failure green; no retrospective weakening; the generality conditions stay mandatory, within
  their scope.
- The v4 review recounted every v4 figure. The figures v5 introduces or changes carry the label
  WN (sec. 0.3) until an independent reviewer recounts them against this document.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This design
decides how the tool verifies each mandatory check of the amended plan. It decides no scientific
question and no row disposition.

## Notation

| Symbol | Meaning |
|---|---|
| `E` | e837e3dbaa605efc867a213f3345cee14c36d8f5, the ledger pin. `E` has no other meaning in this document |
| `H` | 53c6601a10419b6b333cc992474272501ab542af, the scientific base |
| `T1'` | 14ac71b4b0a0c0aa2d7068d6799a73f474097060 |
| `P` | 4c79be642ca631573f06b444903be75ec4f5e2b6, the frozen plan |
| `W` | 413b0bb88f39cad901befcf4684355c7ee39480b, `main` at the time of v3 |
| `F` | the future freeze of the amended plan |
| `X` | the candidate (execution) commit |
| `C` | the certified execution head (sec. A.39 calls it `E`; renamed here, R9) |
| `M` | `main` at check time |
| `L` | the landing merge |

`R` is the frozen ledger record directory. It has tree b05efdca935a42b9c94ef1748c964696bf58fcd9 at
9882df8f, H, T1' and W.

Paths in this document: FULL is `book/The-Incompleteness-of-Observation-FULL.md`; chNN is the book
chapter file with that number.

***

## 0. Traceability

### 0.1 Owner acceptance conditions

| Condition | Answered in |
|---|---|
| 1. Distinct exit codes, including parser errors and `--help`; with a control | sec. 5; controls X1-X10 |
| 2. A frozen, reviewed `delegation.json` with exact-head evidence; missing evidence is never PASS | sec. 7 |
| 3. Deny-pattern coverage; adversarial FAILs, each traced to a named rule or sec. 9 condition | sec. 6.4-6.6, 9, 10.2 |
| 4. A preregistered s3-to-context mapping; the T1' cases resolved transparently | sec. 4 |
| 5. Every replacement-text and unclassified hit classified, with the review load stated | sec. 8 |
| 6. Deterministic HP regions; full merge ids; HP/RET overlap visible in both | sec. 3 |
| 7. Each mandatory sec. 11 check mapped to an operation, flags, expected outcome and countercontrol | sec. 11 |
| 8. Review and authorization lint for rules, PIN_OK reasons, reconciliation records and other records | sec. 6.3 |
| 9. Generality with strict scope limits | sec. 16 |
| 9.1. A core that does not depend on any retirement | sec. 16.1; control Z9 |
| 9.2. A frozen per-retirement configuration `oi-retirement-config/1`: schema, adapters, location, pinning and lint | sec. 16.2, 16.3 |
| 9.3. A1 as the first configuration, with every A1-specific constant relocated and no check weakened | sec. 16.4 |
| 9.4. A structurally different synthetic configuration with positive and adversarial controls | sec. 16.5 |
| 9.5. Fail-closed configuration validation, with exit codes and classes | sec. 16.6 |
| 9.6. Reproducibility record | sec. 16.7 |

### 0.2 Review changes

The v1 and v2 review items are answered as in v3 and keep their places below. `CHANGES-v4.md`
maps each v3 review correction and owner decision to the sections it changed; `CHANGES-v5.md` does
the same for the v4 review's corrections V1-V8, the decisions V5-D1 and V5-D2, and the optional
points O1-O7.

| Review item | Answered in |
|---|---|
| v1 Q1: HP class kept out of RET; attribution; tracking resumes after adjudication; unresolved sites touched later reported | sec. 3 |
| v1 Q2: new-pattern-in-replacement; per-hit classification records | sec. 8 |
| v1 Q3: preregistered context rule; BOF/EOF sentinel | sec. 4 |
| v1 Q4: placement | sec. 12 |
| v1 Q5: schema, fingerprints, output form, boundary cases | sec. 5, 10.1 |
| v2 addenda 1-4 | as mapped in v3 sec. 0.2; role model now H/M/X/C/L (sec. 13) |
| v3 R1: FAIL exit code; acceptance predicate; X7 | sec. 5; X7-X10 |
| v3 R2: DR-4 against V5 and the retired (A1) entries; a countercontrol at H for every DR; V7 precondition | sec. 6.4, 10.2, 10.3 |
| v3 R3: deny set strengthened; residual limit | sec. 6.4, 6.6, 1 |
| v3 R4: sec. 11 note 1; `item7-literal` | sec. 11, 6.1, 10.3 |
| v3 R5: sec. 8.2 profile sets and disjointness | sec. 8.2 |
| v3 R6: region mergers; both overlap counts; per-line classification; H7 | sec. 3.2, 3.3, 3.4; H7 |
| v3 R7: sec. 5 against `--final` | sec. 5, 11 note 2; X9 |
| v3 R8: adapters outside the purity scope; Z9 allowlist and synthetic controls; widening list | sec. 16.1-16.3; Z9a-Z9g |
| v3 R9: the two meanings of `E` | Notation; sec. 13 |
| v3 R10: S0 indicators | sec. 4.2-4.4; K5-K9 |
| v3 R11: ownership chain | sec. 6.3; O1-O9 |
| v4 V1: nine merger groups of 22 sites | sec. 3.2, 3.3; RT-T0 |
| v4 V2: `ptr` has 5 hits at T1' | sec. 6.5, 11 row 1 |
| v4 V3: the item-7 amendment check fails hard where the original does | sec. 5, 11 note 1, 16.2 (`checks`); V23-V26; RT-I7A |
| v4 V4: repo-scan split 96 / 31 / 14 / 35 | sec. 0.3, 8.2 |
| v4 V5: HP obligations and merges are widening | sec. 16.2; Z10 |
| v4 V6 and V5-D1: DR-1d and DR-2 dropped; DR-3's real witness | sec. 6.4, 6.4.1, 15; RT-DR, RT-DR3W |
| v4 V7: figure labels; source of v3's 86 | sec. 0.3, 8.2, 14 |
| v4 V8 and V5-D2: `resid` widened | sec. 1, 6.6, 8.2; V26 |
| v4 O2-O7 (adopted) | sec. 2.3 (O2), RT-DR (O3), 4.1 (O4), 6.3 (O5), 6.1 (O6), 11 note 1 (O7) |
| v5 review W1, W2, O8 (v5.1) | sec. 1, 6.4.1, 0.3, 10.2 V27, 14 |
| Stage 1 D1 and S1-D1: W1 self-match, option B; self-PASS lint | sec. 6.2 step 3, 6.3, 6.5; WB1-WB12 |
| Stage 1 D2: SW2 expectation | sec. 10.3 SW2 |
| Stage 1 D3: 7 HP structure REVIEWs | sec. 0.3, 4.4, 8.2; RT-H0, RT-T0 |
| Stage 1 D4: 215 region lines, LF-inclusive span | sec. 0.3, 5, 14; RT-T0 |
| Stage 1 D5: RT-D 45 `resid` lines | sec. 0.3; RT-D |
| Stage 1 D6: register and infinity semantics; parameters in a rule file | sec. 6.1, 11 rows 5-6; S11-56 |
| Stage 1 D7: `rule-stale` scoping | sec. 6.2 |
| Stage 1 D8: source-byte literals | sec. 6.2, 6.5 |
| Stage 1 B1: acceptance reads admission; harness results never acceptable | sec. 5, 6.3, 10.4, 16.7; X11 |
| Stage 1 B2: native delegated execution in a clone at `X`; independent verification | sec. 7.2; G4-G8 |
| Stage 1 B3: configuration admission from `F`'s designation and pin table | sec. 6.3; TR1-TR5 |
| Stage 1 B4: commits of `C` classified path by path; widening reviews with coverage and authorization | sec. 13.1, 6.3; R16, R17, A12r |
| Stage 1 B5: engine purity over adapter companions; guard pins in the adapter | sec. 16.1, 16.3; Z9g, Z9h |
| Stage 1 B6: control reporting with PASS, FAIL, SKIP and NOT RUN; predicates equal expectations | sec. 10.4; RT-T, RT-D |
| Drift findings S2-S7 (reconciliation, landing composition, class pins, supersedes, one class per id) | sec. 6.3, 13.1, 13.2, 13.3, 16.6; N2-N11, R18, Z11, S4a |
| v5.2 review V1: register and infinity on P's per-edit unit; P's splitter; correspondence check | sec. 6.1, 11 rows 5-6; S11-56, S11-57a-d |
| v5.2 review V2: `F`'s designation from the host, outside the caller and outside `F` | sec. 5, 6.3, 16.7; TR1-TR13 |
| v5.2 review V3: tool-landing class bound to exact blobs | sec. 13.1; R19 |
| v5.2 review V4: a control for every reconciliation condition | sec. 13.2, 13.3; N12-N18 |
| v5.2 review V5: context hash, location, deterministic grant | sec. 6.2; WB9, WB13, WB14 |
| v5.2 review V6: SW2 reference, 14 sites | sec. 10.3 SW2 |
| v5.2 review V7: native execution at `C` as well as `X` | sec. 7.2; G9 |
| v5.2 review V8: N10 pinned to the S6 probe | sec. 13.2 N10, N11 |
| v5.2 review O1: case-insensitive negative literals | sec. 6.2; WB15 |
| v5.3 review W1: P's edit variants selected as P selects; correspondence | sec. 6.1; S11-57a-c, S11-58a-h |
| v5.3 review W2-W4 and owner decisions A-D1 to A-D4: authority record, repository, workflow, forms, thread, edits, supersession | sec. 6.3; TR1-TR27 |
| owner decision A-D5 and v5.3 review O3: durable evidence on `main` | sec. 5 |
| owner addendum: the trust root of the authority record, bootstrap, changes after `F`, residual trust | sec. 6.3; TR24-TR27 |
| v5.3 review O2: a sentence's byte offset | sec. 6.2 |
| v5.4 review V1: P's count; offsets back to `H`; chained edits; overlap control | sec. 6.1; S11-58i-k |
| v5.4 review V2 and R-D3: the run's commit; evaluated commits as inputs | sec. 5, 6.3 (trust root point 3); TR29, TR30 |
| v5.4 review V3 and R-D3: the executed code bound by the host | sec. 5, 6.3 (`engine_pins`, point 3); TR28 |
| v5.4 review V4 and R-D2: every owner comment's edits; the freeze ledger | sec. 6.3 (admission point 3, freeze ledger); TR31-TR36 |
| v5.4 review V5 and R-D4: the first line | sec. 6.3 (forms); TR37, TR38 |
| v5.4 addendum C1 and R-D4: authority changes by an owner approval comment | sec. 6.3 (authority changes); TR40-TR44 |
| v5.4 addendum C2 and R-D4: versioned forms | sec. 6.3 (forms); TR39 |
| v5.4 addendum C3 and R-D5: admission snapshot, compressed result, offline replay | sec. 5, 6.3 (snapshot); TR45, TR46 |
| v5.4 addendum C4 and R-D1: the stricter refusals stated | sec. 6.1 |
| v5.4 review: residual-trust list | sec. 6.3 |
| owner decisions HS-1 to HS-7 (2026-11-24): host sources, edit history, local stores, deleted comments, real-host validation | sec. 5, 6.3 (trust root points 1-3, authority changes, freeze ledger, admission points 2, 3 and 9, snapshot, residual trust), 7.2, 10.5, 15; TR25, TR35, TR71-TR85, HV1-HV10 |
| review of v5.5.10, B1 and B2, nits N1, N2, N4, N5, N7, N8, and F4 (owner decision of 2026-11-24 on v5.5.10a) | sec. 6.3 (trust root point 2, freeze ledger, admission point 3, snapshot, residual trust), 15; TR79, TR85, TR86, TR87, HV5, HV11, HV12 |

### 0.3 Figures

Every figure below was measured read-only from git objects (sec. 14). The implementation reports
its own counts under the fixed definitions. The counts are references, never fitted. A difference
between an implementation's count and a reference here is a finding that blocks acceptance of the
implementation step until it is explained.

**Labels.** Each figure carries one label, used identically in this document and in
`CHANGES-v5.md`:

- **IR**: independently recounted by the v4 review with its own scripts (`review-v4/rv_*.py`). Most
  of these were also reproduced earlier by the v3 review or by the v4 writer.
- **IR+WR**: as IR, and recounted again by this writer for v5 with new scripts (`work-v5/`).
- **WN**: introduced or changed in v5 and measured by this writer only; pending an independent
  recount.
- **S1**: measured by the Stage 1 implementation and reproduced by the Stage 1 review, and
  re-derived by this writer for v5.2 from git objects (`work-v52/`).

**Sites, regions and provenance.**

- 697 sites; s3 categories 346 / 136 / 109 / 106. IR.
- 113 E..H site changes, attributed #1475 48, #1474 23, #1470 15, #1473 15, #1472 12. IR+WR.
- Multi-step HP provenance: 3 sites (papers/Main.md:224, papers/Main.md:732,
  papers/Substratum.md:92), each changed by #1473 and then #1474. IR+WR.
- Region mergers (sec. 3.2): **9 groups covering 22 sites**, each formed at one E..H step. 8 groups
  at #1475 (7f28886f): FULL 4897/4899/4901/4903, FULL 4921/4923, FULL 4973/4975, ch18
  166/168/170/172, ch18 190/192, ch18 242/244, papers/Methodology.md 146/148 and 367/369; 1 group at
  #1474 (a1f38284): papers/Substratum.md 266/268. IR+WR.
- HP sites also overlapped by H..T1' splices: 19 sites and 31 distinct splices, region-attributed;
  18 sites and 31 splices, line-attributed (myers and histogram agree). The difference is
  papers/Substratum.md:266, whose region-attributed splice D029 (an empty image) lies in :268's line.
  Of the 9 merger groups, only Substratum.md 266/268 is overlapped by an H..T1' splice. IR.
- 383 unchanged, 197 replaced and 4 removed sites. IR. **215 region lines** (D4), with the site
  span as v1 sec. 4.3 defines it, the line's bytes plus its LF (sec. 5). S1. The v4 figure of 203
  used a span without the LF; the 12 extra lines come from 3 sites (papers/Main.md:44 at E with
  D259, ch01:28 with D310, FULL:361 with D311) whose second splice starts at the site line's LF and
  inserts a paragraph. The site counts and the 84 hit lines are the same under both spans.

**Hit lines and review load at T1'.**

- Hit lines in the 197 site replacement regions: 84 under the profile set p0-core, p0-para,
  ledger-ext. Adding `count-grep` gives 86; the 2 extra lines are W1 lines (ch19:212, FULL:5284).
  IR.
- 200 unheld p0+ext lines; all 84 region hit lines among them; 116 outside them, of which 93 equal
  an unheld line at H; the other 23 split 16 (in splices over hit lines of HP site regions) and 7
  (new, on non-site lines: D237, D238, D241, D242, D246, D247, D388). IR.
- `resid` as in v4, on added text: 287 splice-image lines, 28 hits, 13 hit by no other review
  profile. IR+WR.
- `resid` as widened in v5 (sec. 6.6): 45 hits on the 287 lines, 17 hit by no other review profile;
  the 4 lines added by the widening are FULL:6265, appendix-c-objections.md:108,
  papers/Complexity.md:206 and papers/Structure.md:1010. WN. The v4 review's design target was the
  same 4 lines; this count agrees with it. In RT-D, whose profile set (item 7's) evaluates no p0
  profile, all 45 `resid` hits are REVIEW items; 17 of them are hit by no other review profile (D5;
  S1).
- Distinct corpus lines needing a classification record or rule under all review profiles: 226
  (200 p0+ext, 5 W1 lines that are not p0+ext hits, 4 W2 lines, 17 `resid`-only). WN (the v4 total
  of 222 was IR; the difference is the 4 `resid` lines).
- `ptr` at T1': 5 lines, the 4 W2 lines and papers/GR.md:58. IR+WR.
- The `repo` profile at T1', by the class P's `classify()` returns: 176 active lines explained by
  entries sec. 6.3 does not admit: 96 path-wide "unrelated label", 31 path-wide "guard pins", 14
  substring entries (9 unrelated label, 1 historical record label, 1 registry identifier, 3
  preserved historical evidence) and 35 "kernel identifier" (IDENT); 0 unexplained; 5486 lines in
  historical records, 2 in generated artifacts. IR+WR.
- Meaning-context failures under the adopted mapping: 12 (7 in E..H, 5 in H..T1'); for reference
  only, 8 if `per unit` were false. 52 unchanged sites with a context change (27 / 22 / 3). IR.
- S0 indicators under v4's definitions: ANAPH 23, LIST 49, TABLE 6, PARTIAL 521 of 697; among the 52
  changes 0, 3, 1, 39; no ANAPH failure. IR. Indicator items: **7 HP** (D3; S1) and 3 RET (IR).
  The 7 HP items are FULL:706, FULL:708, ch02:76, ch02:78, papers/Substratum.md:94, :253 (LIST) and
  papers/Main.md:741 (TABLE): the sites unchanged at H whose context or structure context changed in
  E..H. v4's figure of 3 was taken over sites also unique at T1', a condition the rule does not have;
  only 3 of the 7 are unique at T1'.

**Item 7 and the deny rules.**

- Literal item-7 greps over papers/*.md and book/*.md: at T1' "six structural" 7, "Fourteen" 0,
  "sixth of" 0, `\bA1\b` 4; at H 11, 1, 2 and 179. IR.
- The v5 deny set (DR-1a/b/c, DR-3, DR-4, DR-5; sec. 6.4) with the v5 splitter: at T1' 0 lines and
  0 sentences. At H: DR-1 61 lines (a 6, b 2, c 55), DR-3 0, DR-4 28, DR-5 1; 86 distinct lines.
  At E: 95 distinct lines. Per sentence (v5 splitter): at H DR-1a 6, DR-1b 2, DR-1c 65, DR-4 28,
  DR-5 1, as in v4; at E DR-1c 70, the others as per line. IR+WR for H and T1' (the splitter
  change of O6 changed no count there); WN for the per-sentence counts at E.
- DR-3 on `AGENTS.md`: one sentence at H (lines 37-39, blob sha256 d87acac5...e27), none at T1'
  (blob sha256 59b68984...ce2). IR+WR.
- DR-1d, DR-2 and DR-3 over history (sec. 6.4.1): no match of any of the three, at line or
  sentence level, in any of the 4677 distinct blobs that occur at a top-level `papers/*.md` or
  `book/*.md` path in some commit reachable from the 794 local refs; and no match of DR-1d or DR-2
  in any text file at H, W or T1'. Measured by the v5 review and by this writer. The 4677 is the
  union of two walks that each miss blobs:
  the path-limited walk (4657) and the unrestricted walk (4671), sec. 6.4.1.
- Retired lines at H that carry `\bA1\b` or a `count-grep` literal, are absent at T1', and match no
  deny rule: 95, all of them `ptr` or `count-grep` hits. IR+WR.
- The proposed item-7 amendment check (sec. 11 note 1) with no records: at H, 86 deny lines and
  123 `final-unclassified` lines, 209 FAIL lines in all, the 95 among the 123; at T1', 0 deny lines
  and 12 `final-unclassified` lines (the 7 W1 lines, the 4 W2 lines and papers/GR.md:58). WN.
  The 86 and 209 count line-level deny matches only (O8). If every line of a multi-line sentence
  that a deny rule matches is also counted as a deny line, H has 93 deny lines and 216 FAIL lines;
  the 123 does not change. These two figures were measured by the v5 review and by this writer.

**Withdrawn.**

- The v2 review's 24 sites / 24 splices and its 2 two-step sites.
- v3's figure of 86 hit lines in the 197 regions under the stated profiles. Under the stated
  profiles the figure is 84. v3's script (`work/measure10.py`) reached 86 by one deviation, a
  touching-overlap test (`start <= site_end and end >= site_start`): with only that test made
  strict, the same script gives 84. It skips empty replacement images. Counting the removed sites'
  offset lines under the strict test is an equivalent variant that also gives 86 with the same two
  extra lines (FULL:710, ch02:78), but it is not what v3's script did.
- v4's statement that there is one region merger (corrected to 9 groups, V1), v4's `ptr` count of 4
  (corrected to 5, V2), and v4's repo split 37 / 12 (corrected to 14 / 35, V4). v4's split counted
  each line by the first `EXPLAINED` entry for its path, not by the class `classify()` returns.
- The frozen tool's error counts (32 and 154): used by no expected outcome and recounted by no one.

***

## 1. Purpose, non-goals and residual limits

**Purpose.** One evaluation pipeline verifies, for named commits:

- that the frozen record `R` is correct at its pin;
- that every ledger site and every terminology subject at a candidate is accounted for;
- that a candidate is exactly `H` plus the ledger;
- that a landing merge composes `main` with the candidate exactly.

Each mandatory check of the amended plan is one configuration of this pipeline (sec. 11).

**Non-goals.**

- **Scientific correctness.** A PASS establishes coverage and provenance only. It does not show
  that a replacement keeps its finite-only, conditional or open qualification. It does not show
  that a classification rule's reading is right. It does not show that the frozen map's 16 fuzzy
  and 83 anchor relocations chose the right line at the pin. Those questions stay with:
  - the classification records' reviewers;
  - the plan's independent non-author review of the exact head;
  - the owner's decisions.
- **Row dispositions.** The tool reclassifies no row. Row, code and owner are carried from the
  frozen map, and no record may change them.

**Residual limits.**

- Coverage is defined by the sites, the profiles and the rules. A removed qualifying sentence is
  not detected if it matches no profile and sits next to no context-required site.
- The context mapping and the S0 indicators are preregistered heuristics.
- A rule fingerprint recognizes only identical text. Any edited legitimate use returns to
  REVIEW_REQUIRED or FAIL.
- **Lexically unanchored paraphrases.** The deny rules close only forms with a fixed lexical anchor
  (a count or ordinal of posits, a label range, the (A1) label, a posit-ledger count, and in a
  sentence a posit noun with a connector and a finiteness word). A paraphrase without such an
  anchor cannot be closed by a regular expression. The guarantee of at least REVIEW_REQUIRED is
  implemented, on added text, only for the classes that `resid` (sec. 6.6) or another review profile
  matches:
  - a finiteness word together with a posit noun (posit, premise, axiom, assumption, hypothesis)
    within a 60-character window of one sentence;
  - a state-space noun (configuration, state or phase space) followed by "is finite" or a similar
    copula;
  - "finite set", with at most one word between;
  - "substratum", "universe" or "world" followed within 40 characters by "is", "be", "being" or
    "are", an optional article and at most one word, and "finite";
  - "finite number" or "finite count" of states, configurations, elements, points or sites.

  A paraphrase outside these classes stays outside the tool, and its detection rests on the plan's
  independent review of the exact head. Constructed examples outside them, which PASS when added:
  "the framework's sixth structural property, finiteness of the bijection" and "The framework's
  sixth structural property is finiteness of the substratum" (both no longer denied once DR-2 is
  dropped, V5-D1), "the six posits of the substratum", "six assumptions about the substratum",
  "The posit ledger lists fourteen.", "the fourteen-item posit ledger" and "$A_1$–$A_6$". The
  original literal item 7 misses each of these too.
- Delegated checks stay outside the tool's semantics, even when their evidence is bound to `X`.
- The tool checks that role fields differ and that a quoted authorization exists. It cannot check
  who wrote a record (sec. 6.3).

## 2. Pipeline and subject kinds

### 2.1 Pipeline stages

Every run executes the same stages in a fixed order. A stage that fails stops all later stages.

1. **Usage.** Arguments are parsed and the `--out` guard is applied.
2. **Integrity.** Objects, pins, record hashes, ledger hashes, the configuration and the adapter
   module blobs are checked.
3. **Controls.** The in-memory preflight controls run.
4. **Identity.** Every subject is located.
5. **Provenance.** Ledger splices, HP adjudications and reconciliations are applied.
6. **Classification.** Profiles, rules and records are applied.
7. **Outcome.** The overall result is computed.

### 2.2 Subject kinds

Each subject kind has its own anchor and context rule.

| Kind | Anchor | Context | Source |
|---|---|---|---|
| `site` | exact pin line bytes, `pin_count`, `ordinal` | sec. 4 | frozen `sitemap.json` |
| `splice` | id, span, `old_sha256`, `new_sha256` at `H` | the image's offset in `X` | `ledger.json` at `F` |
| `hit` | file, segment, `line_sha256` (unique in its tree) | the sentence and its neighbours | profiles (sec. 6.1) |
| `pin` | check file, exact literal, target file, occurrence counts at `H` and at `X` | none | Python literals of tracked checks, by `ast` |
| `mirror` | edit id pair (`mirror_of`) | none | `edits.json` at `F` |
| `path` | path and blob id in each role | none | the role trees (sec. 13) |
| `delegated` | delegation entry id | none | `delegation.json` at `F` (sec. 7) |

### 2.3 Operations

| Op | Subcommand | Roles used |
|---|---|---|
| A | `record` | `E`, plus the record commit |
| B | `coverage` | `E`, `H`, `X` (and `L`) |
| C | `execution` | `H`, `X`, `M`, `L` |
| D | `terms` | one commit; with `--base B --ledger F:ledger.json`, also the added text of `B..commit` |

All four operations share the code paths of the pipeline stages.

**Where deny profiles run (O2).** Deny profiles (sec. 6.1) are evaluated on every tree a run
evaluates except `E` and `H`, the two trees named in the configuration as retired-form trees
(`roles.pin` and `roles.scientific_base`), where the retired forms are expected. In op D they are
evaluated on the named commit whatever it is, so that their countercontrols at `H` run through op D
(RT-DR). `result.json` lists the profiles evaluated on each tree.

**Added text.** Profiles with `applies_to: added-text` (`register`, `infinity`, `resid`) are
evaluated on the splice images of a ledgered segment. In op D they run only with `--base` and
`--ledger`.

### 2.4 Ledger fields

The ledger adapter (sec. 16.3) reads the ledger. The rules below are the A1 adapter's.

- `retained_unchanged` (D032, D039): each id must exist in `edits.json`, must have no splice, and
  must have its site text byte-identical at `H` and at `X`. Otherwise the result is FAIL
  `retained-changed`.
- Every other unread ledger field is reported under `ignored_fields`. An unknown schema id is
  ERROR `SOURCE_CHANGED`.

***

## 3. Historical provenance obligation `HP` (segment E..H)

### 3.1 Pinned merges

The A1 configuration record (sec. 16.4) pins the merges by full commit id. The engine contains
no merge ids. The tool cross-checks each pinned merge against the PR number in its subject, and
never resolves a merge from subject text.

| PR | Merge commit | First parent | Sites first changed |
|---|---|---|---|
| #1470 | 0cd5d5bfb4f6641c8b08706c4eb636ee730ebbf0 | 1c7eedc402eafd2bac654484fa790874a33f444d | 15 |
| #1473 | a1f38284d21338b66119c870a551a670c73e3fa7 | f1c8c6b18b245c2faaa68abb464d70ab332b7bec | 15 (plus 3 second steps of #1474) |
| #1474 | 0ba358ccf05eb461c3a5bd686062f65115c293fc | a1f38284d21338b66119c870a551a670c73e3fa7 | 23 |
| #1472 | 4de2eabd6c7c88dc214db70a813ec44b8641b630 | 0adc410c4ad8c3ff51fc77ebb2e055506d758fc8 | 12 |
| #1475 | 7f28886f4cc96fbfa7407af1fdc37de2f0e562e5 | 4de2eabd6c7c88dc214db70a813ec44b8641b630 | 48 |
| #1494 | 53c6601a10419b6b333cc992474272501ab542af (= `H`) | fd9f99cc8866bd4f4244298f819fa99d5c707fba | 0 |

The first-parent chain from E to H has 14 commits. Six of them change the corpus.

### 3.2 Region definition (independent of any diff algorithm)

For a site, the region is a block of whole lines. For each first-parent commit `c` with parent `p`
in E..H, in order, the region is updated as follows.

1. **Carried.** If the region occurs exactly once as a whole-line block in both `p` and `c`, it is
   carried unchanged.
2. **Not unique at the parent.** If it does not occur exactly once in `p`, the site is FAIL
   `provenance-ambiguous`.
3. **Changed at this commit.** Otherwise the site is changed at `c`:
   - The upper anchor is the nearest line above the block in `p` that occurs exactly once in `p`
     and exactly once in `c`. If there is none, the sentinel `BOF` is used. The lower anchor is
     chosen the same way below the block, with the sentinel `EOF`.
   - The anchors must keep their order in `c`. If they do not, the site is FAIL
     `provenance-ambiguous`.
   - The pre-region is the lines of `p` strictly between the anchors. The post-region is the lines
     of `c` strictly between the anchors. Both are trimmed of leading and trailing blank lines.
   - The step `{commit c, parent p, position k, pre_sha256, post_sha256}` is recorded. The
     post-region becomes the region.

These rules depend only on the two texts. An empty post-region means the site was removed in that
step. A step at a commit that is not in sec. 3.1 is FAIL `provenance-foreign`.

**Region mergers (R6, V1).** Two sites whose walks produce the same post-region at the same step
share that region from then on. The tool reports each such site with `region_shared_with`: the
sorted list of the other site ids, the step at which the regions merged, and the shared region's
hash. A merger is never silent. On the chain E..H there are 9 merger groups covering 22 sites, each
formed at a single step:

| Step | Groups (sites at the pin) |
|---|---|
| #1475 (7f28886f) | FULL 4897/4899/4901/4903; FULL 4921/4923; FULL 4973/4975; ch18 166/168/170/172; ch18 190/192; ch18 242/244; papers/Methodology.md 146/148; papers/Methodology.md 367/369 |
| #1474 (a1f38284) | papers/Substratum.md 266/268 |

The sites of a group sit two lines apart, separated by blank lines. Blank lines are never unique,
so the anchors of the walks fall outside all sites of the group, and their pre-regions become one
block. Of the 9 groups, only Substratum.md 266/268 is overlapped by an H..T1' splice (D029).

### 3.3 HP adjudication record (schema `oi-hp-adjudication/1`)

The record is an immutable file in the audit directory, under the ownership chain of sec. 6.3. It
lists each `site_id` with the following:

- `steps`: each step's commit (full id), parent, position, `pre_sha256` and `post_sha256`;
- the carried `row`, `code` and `owner`, which must equal the frozen values; otherwise FAIL
  `adjudication-row-changed`;
- `own_lines`: for a site with `region_shared_with`, the lines of the shared final region at `H`
  that carry this site's text, by `line_sha256`. It is required for every one of the 22 merged
  sites of sec. 3.2, whether or not a splice overlaps the region. For an unshared site it is the
  whole final region;
- `semantic_classification`: which qualification is visible on the site's own lines, with the
  reason. For a shared region each site is classified on its own lines, never only on the block;
- `splice_attribution`: for each H..X splice that overlaps the final region, the site ids whose own
  lines it intersects;
- `hit_classifications` for every profile hit in the final region (sec. 8), bound by
  `line_sha256`;
- `context`: the pin and H context hashes plus a semantic statement, required when sec. 4 marks
  the site and its context changed in E..H;
- `author`.

The tool recomputes the walk of sec. 3.2 and compares it with the record. The result is:

- `provenance-adjudicated` only if every step matches exactly;
- FAIL `provenance-mismatch` if a commit or hash differs;
- FAIL `provenance-gap` if a step is missing or extra;
- FAIL `provenance-foreign` or `provenance-ambiguous` as in sec. 3.2;
- FAIL `hp-unadjudicated` if no record names the site;
- FAIL `record-invalid` if a site with `region_shared_with` has no `own_lines`, if the own lines of
  the sites sharing a region leave a non-blank region line unassigned, or if a splice overlapping
  the region is attributed to no site.

### 3.4 Resumed tracking and HP/RET overlap

- An adjudicated site resumes tracking in H..X from its final region at H, under the ledgered
  rules of v1 sec. 4.3. It then becomes `authorized-replacement`, `authorized-removal`,
  `unchanged`, `moved` or a RET FAIL.
- An HP site whose H region is touched by any H..X splice keeps two independent entries:
  - in `HP`: its provenance status;
  - in `RET`: its H..X status, with `hp_overlap: true` and the splice ids.

  Neither entry is counted in the other obligation's totals. An E..H edit is never reported as a
  retirement edit, and a retirement splice is never reported as historical.
- Without an adjudication, an HP site stays unresolved. Its RET entry is then
  `untracked-hp-overlap`, a FAIL listing the overlapping splices. This makes the retirement's
  rewrites of historical sites visible before any adjudication exists.
- **Two overlap counts (R6).** Each RET entry carries `region_splices` (splices overlapping the
  site's final region, the decision basis) and `line_splices` (a diagnostic: splices intersecting
  the site's own line, tracked through each step by `git diff -U0 --no-renames` with the myers
  algorithm, carrying the site's line range through the hunks). The FAIL class and the totals use
  `region_splices`. Once an adjudication exists, `line_splices` is replaced by the record's
  `splice_attribution`, which the tool checks as in sec. 3.3.
- At T1': 19 HP sites, overlapped by 31 distinct splices, region-attributed; 18 sites and 31
  splices line-attributed. The one difference is Substratum.md:266, whose region-attributed splice
  D029 lies in :268's line.

### 3.5 Context changes in E..H

Every item is assigned to the segment in which its change occurred. A context change on a
meaning-required site (sec. 4) that occurred in E..H is an `HP` item. It is resolved only by the
`context` field of that site's HP adjudication, or of a context adjudication for an unchanged site.
Indicator items of sec. 4.3 that arise in E..H are also `HP` items.

***

## 4. Preregistered context rule

Decided at S0, before any implementation output. The rule is stated per frozen s3 value and per
indicator. The mapping and the indicator definitions were adopted on their principle by the owner
decisions of 2026-11-23 (D2). Their counts at T1' are reported, not tuned.

**Context definition.** The ordered pair of the nearest non-blank line above and the nearest
non-blank line below, with sentinels `BOF` and `EOF`. Its hash is
`sha256(above + 0x00 + below)`, taken at the pin and at every tree.

**Identity.** Context is required for identity when `pin_count > 1`, or when the current text is
not unique (v1 sec. 4.4). A context change then makes the site FAIL `ambiguous`. All 697 pin lines
are unique at E.

**Meaning.** The principle: context is required exactly when the frozen record does not establish
that the qualification is visible on the site's own line. `per unit` stays on the required side: a
per-unit status means the qualification was established by a unit's correction, which may sit in
a neighbouring sentence.

| Frozen s3 value | Sites | `meaning_context` |
|---|---|---|
| visible (names the hypothesis); rewritten at deletion | 194 | false |
| visible (P0/P1/P2 disposition) | 144 | false |
| visible (applied splice) | 5 | false |
| visible (none: the (NR) corollary ...) | 3 | false |
| n/a | 136 | false |
| not determined: Q3 census | 81 | true |
| not determined | 28 | true |
| per unit regression audit (#1468) | 45 | true |
| per unit Q1 corrections (Step 2) | 28 | true |
| per unit Step-2 phase | 15 | true |
| per unit R6 corrections (Step 2) | 9 | true |
| per unit R1/R2 scoping | 8 | true |
| per unit Q2 | 1 | true |

The indicator ANAPH (sec. 4.2) also sets `meaning_context` to true. A reviewed context adjudication
may set it to true for a further site. Nothing can set it to false for a site the table or ANAPH
marks.

### 4.1 Decision

| Condition | Result |
|---|---|
| `meaning_context` true, context changed, no context adjudication matching both hashes | FAIL `context-meaning-unverified` |
| `meaning_context` true, context changed, matching adjudication | PASS |
| LIST or TABLE site, its structure context or its context changed, no adjudication matching both context hashes and both structure hashes (sec. 4.3) | REVIEW_REQUIRED `context-structure-changed` |
| `meaning_context` false, context changed, not covered by the row above | PASS with `context_changed: true`; requires verified identity and identical site bytes |

FAIL takes precedence: a LIST or TABLE site whose `meaning_context` is true and whose context
changed is FAIL `context-meaning-unverified`.

A context adjudication (schema `oi-context-adjudication/1`) records `site_id`, `segment`,
`from_context_sha256`, `to_context_sha256`, for LIST and TABLE sites also
`from_structure_sha256` and `to_structure_sha256`, and a semantic statement that the
qualification is still visible or still stated. It carries `author` and is under the ownership
chain of sec. 6.3.

### 4.2 S0 indicators: exact definitions (R10)

All four indicators are computed on the site's pin line at `E`. They are preregistered at S0 with
the definitions below, which are part of the A1 configuration (sec. 16.4). A change to any of them
is a configuration change and is widening (sec. 16.2).

- `strip(line)`: remove leading whitespace, then any run of blockquote markers `>` with their
  following whitespace, then one heading marker `#{1,6}` with its whitespace, then one list marker
  (`-`, `*`, `+`, or digits followed by `.` or `)`) with its whitespace, then any run of `*` and `_`.
- **ANAPH**: `strip(pin line)` matches, case-sensitively,
  `^(This|These|Such|Hence|Thus|It|Under this)\b`.
- **LIST**: the pin line matches either
  - `^\s*(>\s*)*([-*+]|\d+[.)])\s+` (a list item), or
  - `^\s*(>\s*)*(([-*+]|\d+[.)])\s+)?[*_]{0,2}\(\s*([A-Z]{1,3}\d{1,2}[a-z]?|[ivx]{1,4})\s*\)` (a
    labelled item, such as `*(A2) Determinism.*` or `(C1)`).
- **TABLE**: the pin line matches `^\s*\|`.
- **PARTIAL**: the site has a Phase-0 entry, and its `quote`, whitespace-normalized, differs from
  the whitespace-normalized pin line.

### 4.3 Indicator effects

| Indicator | Effect |
|---|---|
| ANAPH | sets `meaning_context` true. An anaphoric line takes its referent from the line above, so a changed context changes what the line asserts. FAIL `context-meaning-unverified` until adjudicated |
| LIST | REVIEW_REQUIRED `context-structure-changed` when the site's context (sec. 4) or its list context changed, unless adjudicated |
| TABLE | REVIEW_REQUIRED `context-structure-changed` when the site's context (sec. 4) or its table context changed, unless adjudicated |
| PARTIAL | informational only: the site carries `partial_quote: true`. No effect on any outcome |

**List context.** Walking up from the site over blank lines and list-item lines (as LIST defines
them), the first other non-blank line is the lead-in (`BOF` if none). Walking down the same way,
the first other non-blank line is the trailer (`EOF` if none). The siblings are the non-blank item
lines between them, other than the site. The list context is `(lead-in, siblings, trailer)`, and
its structure hash is the SHA-256 of its canonical JSON.

**Table context.** The table block is the maximal run of lines matching `^\s*\|` that contains the
site. The table context is `(header, caption above, caption below)`: the block's first line; the
nearest non-blank line above the block (`BOF` if none); and the first non-blank line after the
block if it starts with `Table:` or `: `, else the empty string. Its structure hash is defined as
for lists.

**Conservative reading.** The review recommended REVIEW when a list's lead-in or a sibling changed,
and the table context redefined as header plus caption. v4 keeps the neighbour-pair context of
sec. 4 for these sites as well, and adds the trailer to the list context. This is a strict
superset: it removes no v3 outcome, keeps the review's own TABLE true positive
(papers/Main.md:741, whose neighbour row changed) visible, and catches its LIST true positive
(papers/Substratum.md:127, whose following paragraph changed from "derived from E1-E3, A1-A2" to
"derived from E1-E3 and A2").

**Reference rates.** These are references for the preregistration. They are not tuned values.

| Indicator | v3 review's definitions: sites / of 52 changes | v4 definitions: sites / of 52 changes |
|---|---|---|
| ANAPH | 31 / 0 | 23 / 0 |
| LIST | 20 / 1, plus 2 false negatives (FULL:708, ch02:78) | 49 / 3 (FULL:708, ch02:78, Substratum.md:127) |
| TABLE | 6 / 1 (Main.md:741) | 6 / 1 (Main.md:741) |
| PARTIAL | 342 / 23 | 521 / 39 |

The review's definitions were its own and are not given exactly in its text; the v4 definitions
above are the preregistered ones. The differences in ANAPH, LIST and PARTIAL come from the
definitions (v4's LIST includes labelled items and ordered lists; v4's PARTIAL counts any
difference between quote and line). Only the v4 column is a reference for the implementation.

### 4.4 The real-tree cases at T1'

There are 52 unchanged sites whose context differs from the pin:

- 27 changed in E..H;
- 22 changed in H..T1';
- 3 changed in both segments.

Of these, the table of sec. 4 marks 12. ANAPH marks none of the 52.

| Origin | Cases | Result under the rule | Resolved by |
|---|---|---|---|
| E..H | 6 `not determined`, 1 `per unit` | HP FAIL `context-meaning-unverified` | the HP or context adjudication of sec. 3.5 |
| H..T1' | 2 `not determined`, 3 `per unit` | RET FAIL `context-meaning-unverified` | a context adjudication reviewed against the retirement's edits |

The 12 sites: E..H: FULL:4895, 4905, 4919; ch18:164, 174, 188; papers/Main.md:332. H..T1':
FULL:1340; ch05:25; papers/Computation.md:122; papers/GR.md:90; papers/Main.md:588.

Indicator items (none of these sites is marked by the s3 table). The E..H row counts every site
unchanged at H whose context or structure context changed in E..H; it has no condition at T1' (D3).
FULL:706, ch02:76 and Substratum.md:94 and :253 are rewritten in H..T1', so they are not among the
52 unchanged sites of sec. 4.4's first table, but their E..H items stand:

| Origin | Sites | Result |
|---|---|---|
| E..H | LIST FULL:706, FULL:708, ch02:76, ch02:78 (sibling items changed), papers/Substratum.md:94, papers/Substratum.md:253; TABLE papers/Main.md:741 (neighbour row changed) | 7 HP REVIEW_REQUIRED `context-structure-changed` |
| H..T1' | LIST FULL:708, ch02:78 (lead-in, sibling items and trailer changed); papers/Substratum.md:127 (the paragraph after the list changed) | 3 RET REVIEW_REQUIRED `context-structure-changed` |

The two contradictory cases named in v2 addendum 3 are the 2 `not determined` H..T1' cases. Under
this rule they are RET FAILs. RT-T (sec. 10.3) states this. It does not claim "no RET FAIL".

***

## 5. Outcomes, exit codes and output

| Outcome | Exit | Emitted when |
|---|---|---|
| PASS | 0 | every check holds and every control is green |
| REVIEW_REQUIRED | 10 | no FAIL item, at least one REVIEW item |
| FAIL | 20 | at least one FAIL item |
| USAGE | 64 | an argument error, `--help`, or a refused `--out` |
| ERROR | 65 | an integrity error (list below) |
| VOID | 70 | a preflight or self-test control failed |
| INTERNAL | 71 | any exception caught by the tool's wrapper |

**Why FAIL is 20 (R1).** CPython itself exits 1 on an uncaught exception, including one raised
before the tool's wrapper is installed (an import or syntax error in the tool's own package), and 2
when it cannot open the script; it exits 120 when flushing standard streams fails at shutdown. None
of the codes in the table is one of these. The parser overrides `ArgumentParser.error` and the
`-h`/`--help` action so that both exit 64; exit 2 is therefore excluded only for the parser's
paths, and the interpreter can still return it.

**The wrapper.** The entry point `tools/ledger_coverage.py` installs the wrapper before it imports
the tool's package. The wrapper catches `BaseException` (including `SystemExit` raised by frozen
code and `KeyboardInterrupt`) and maps it to INTERNAL, exit 71, with a `result.json`. A failure
before the wrapper is installed exits with the interpreter's own code.

**Acceptance predicate (sec. A.44).** A consumer (a workflow step, the plan's checker or a
reviewer) accepts a run only if all of the following hold:

- the exit status is 0;
- `result.json` exists in `--out` and validates against schema `oi-ledger-coverage/4`;
- its `outcome` is PASS, and the independent outcome checker (S7) recomputes PASS from its
  `preflight`, `record_checks` and `items`;
- its recorded engine blob and adapter module blobs equal the pinned ones (sec. 16.7), and its
  configuration `{path, blob_sha256}` equals the frozen one;
- `config.admission` is `"chain"` and names the same `F` as the consumer's own, with the same
  designation, the same pin table and the same `A` blob. The consumer reads `A` itself from the
  canonical repository's `main` (sec. 6.3).
- The result was produced in a host CI run that the consumer verifies itself, from the host's REST
  API and its own full local object store read as trust-root point 2 of sec. 6.3 states (HS-1), by
  repeating trust-root points 1-3 of sec. 6.3:
  - the repository id equals `A.repository.id`, and the repository is not a fork;
  - `head_sha` is on `main`'s first-parent chain and contains `A`, the pinned workflow and the
    pinned tool blobs;
  - the workflow content hash and the tool blobs are read at that `head_sha` and equal their pins;
  - the evaluated commits equal the landing record's;
  - the result file is that run's uploaded artifact, by sha256.

  A result produced anywhere else, or by other code, is never acceptable.
- **Durable evidence (A-D5, C3, R-D5).** Acceptance is recorded only by landing it on `main` in the
  authorized landing record. The record commits:
  - **The result, compressed deterministically.** `result.json.gz`: gzip of the exact result bytes,
    with a modification time of 0, no file name, compression level 9 and the operating-system
    field 255. The sha256 of the uncompressed bytes decides; the compressed bytes' sha256 is
    recorded as well.
  - **The admission snapshot** of sec. 6.3, and its sha256.
  - **The reproducibility recipe:** the commits; the configuration, `A`, engine, adapter and
    workflow blob hashes; the exact command; and the tool version.
  - **The events the admission observed,** appended to the freeze ledger only with the append's own
    owner approval comment (sec. 6.3, N3).

  CI run ids, job ids and log references are recorded as provenance only (sec. A.42 item 2).
  Committing a result preserves it; it never makes an invalid run acceptable. The predicate above
  is re-checked from the committed data before the landing merges.
- **Offline replay (C3, F2).** `replay --snapshot <path> --out DIR` recomputes the result from git
  objects and the committed snapshot alone. Admission is taken from the snapshot and written as
  `"admission": {"mode": "replay", ...}`.

  For op C, every delegated and native class is decided from the snapshot's delegated evidence
  (sec. 6.3). Replay does not call the host, clone the repository, build PDFs or rerun any checker.
  It re-applies the tool's own verification rules of sec. 7.2 and 7.3 to the recorded host records,
  hashes and checker outputs and to the git objects, for example:
  - the TeX stamps and path set;
  - LEDGER.json against `H` plus its splices and the recorded census values;
  - SC-42's committed file against the recorded `--verbose` output;
  - the recorded `pdf` and `ci` records against `X`'s ids and the artifact hash.

  Every recorded result file must also hash to the sha256 recorded beside it.

  Apart from the admission field, the replay's output must equal the committed result byte for
  byte (canonical JSON, sec. 5), for op B and op D results as well as for op C results. An independent verifier can therefore
  reproduce and validate an accepted result from preserved inputs, without any temporary CI
  artifact. A replay is never acceptable as a new run. One thing remains host-attested and cannot
  be reproduced offline: that the snapshot was genuine when it was taken.
- The schema makes `config.admission` required. A result with a mode other than `"chain"`, or with
  a top-level `"harness"` field, is never acceptable, whatever its outcome (control X11).

Any exit status not in the table (for example 1, 2, 120, 126, 127 or a signal) is non-acceptance,
whatever `result.json` says. An exit status in the table that disagrees with `result.json` is
non-acceptance.

**Integrity errors.** These produce ERROR:

- `PIN_MISMATCH`, `RECORD_TREE_MISMATCH`, `SCIENTIFIC_BASE_MISMATCH`, `MAIN_NOT_DESCENDANT`;
- `SOURCE_CHANGED`;
- a ledger hash, span, overlap or base mismatch;
- `edits_sha256` mismatch;
- an encoding error (not UTF-8, or CR present);
- an unresolvable object, or one that does not hash to its id (sec. 6.3, trust root point 2);
- the configuration classes of sec. 16.6.

Evaluation order fixes precedence: USAGE, INTERNAL (at any stage), ERROR, VOID, FAIL,
REVIEW_REQUIRED, PASS. Only exit 0 with the acceptance predicate is acceptance.

**Flags and REVIEW_REQUIRED (R7, V3).** No flag converts REVIEW_REQUIRED to PASS. A run of op D
names the plan check it implements with `--check ID`; the configuration's `checks` table (sec. 16.2)
gives each check its profiles and its `final_profiles`. `--final` converts the REVIEW items of the
selected check's `final_profiles` to FAIL `final-unclassified`, and changes nothing else. For A1,
item 7 lists `ptr` and `count-grep`, and item 11 lists `repo`. `--final` without `--check`, or with a
check that has no `final_profiles`, is USAGE. Controls X9 and V23-V25 show both directions.

**When no `result.json` is written.** In the USAGE case nothing is written to `--out`. One JSON
object with the same schema id, `outcome: "USAGE"` and the parser message goes to stderr. This is
the only case of the table without a `result.json`. A run that ends with an interpreter code
outside the table writes none either, and is non-acceptance.

**Frozen code.** Every call into frozen code in op A is wrapped. An exception becomes a structured
INTERNAL or ERROR with its class and message. The frozen `main()` is never called, so its line-523
`TypeError` cannot be reached.

**Output form.** Schema `oi-ledger-coverage/4`, which extends v3's `/3`:

- `site_counts`, `finding_counts` and `hit_counts` are separate;
- items carry `file` and `line` where applicable, and are sorted by
  `(obligation, class, subject, segment, fingerprint)`;
- the fingerprint is the SHA-256 of canonical JSON (sorted keys, no whitespace, UTF-8, null as
  `null`) over fields that do not depend on any diagnostic algorithm. For `unauthorized-edit` that
  is the expected and actual file hashes and the segment; difflib ranges are diagnostics only;
- every hit carries a `segment`, its profile and the tree it was scanned in. `pre_existing` is
  computed by the same scan at the prior endpoint;
- `repo_head` is removed;
- the output is written with sorted keys, indent 1, `ensure_ascii` true and a final LF;
- site fields: `pin_count`, `ordinal`, `pin_context_sha256`, `current_context_sha256`,
  `context_required`, `meaning_context`, `indicators` (`anaph`, `list`, `table`, `partial_quote`),
  `structure_context_sha256` (LIST and TABLE sites), `provenance` (record id or null),
  `region_shared_with`, `hp_overlap`, `region_splices` and `line_splices`;
- `profiles_evaluated`: per tree, the profiles run on it (sec. 2.3);
- `covered_paths` lists exactly the paths the run's verdict covers. A PASS states nothing about
  any other path;
- an adjudication naming a segment outside the chain is `out-of-scope`, which is reported but is
  not a finding.

**Explanation.** Every subject carries an explanation with:

- the subject id and kind;
- the anchor and its hashes;
- the provenance chain (segment, splice ids, HP steps, reconciliation id);
- the rule id and rule blob hash, or null;
- each matcher's result;
- the resulting state;
- for REVIEW_REQUIRED, `resolution_needed`: the record kind and the fields a reviewer must supply.

The explanation is part of the JSON Schema. The outcome is a pure function of `preflight`,
`record_checks` and `items`. An independent checker of about 30 lines recomputes it (S7).

**Boundary cases.**

- A splice overlaps a site if `start < site_end` and `end > site_start`. A zero-length splice at an
  interior offset also overlaps. A splice that only touches a site's boundary does not.
- A hit line is "in a splice image" if it contains the splice's offset in `X`. Empty images are
  included, for example D029 at Substratum.md:268.
- A removed site (empty image) has no replacement region; the line holding its offset is reported
  with the removal, not counted as a region line.
- A last line without LF is a line. Its span ends at end of file.
- A site's span is its line's bytes plus its terminating LF (v1 sec. 4.3; D4). A splice that starts
  at the site line's LF therefore overlaps the site, and the replacement region includes the lines
  it inserts.

***

## 6. Profiles, rules and record lint

### 6.1 Scan profiles

Profiles are extracted from their source blobs by `ast` or JSON, never retyped, except the rule
patterns of sec. 6.4 and 6.6, which live in reviewed rule files. Each profile records its source
blob and the SHA-256 of its patterns.

**Review profiles.** A hit is REVIEW_REQUIRED unless held or classified.

| Profile | Source | Applies to |
|---|---|---|
| `p0-core`, `p0-para` | Phase-0 `sites.json` | tree |
| `ledger-ext` | `EXTENDED_PATTERNS` in `R/ledger_check.py` | tree |
| `ptr` | `PTR` in P's `edits_check.py` | tree |
| `repo` | `REPO_PAT` in P's `edits_check.py`; scope "active files", sec. 11 item 11 | tree |
| `count-grep` | the literal list of sec. 11 item 7: "Fourteen", "six structural", "sixth of" | tree |
| `resid` | sec. 6.6 (v4, widened in v5; rule file) | added text |

**Deny profiles.** Any match is FAIL. They are evaluated on every line and on every sentence of
every in-scope file of the trees named in sec. 2.3, not only on hits of other profiles.

| Profile | Source and scope |
|---|---|
| `DR-1`, `DR-3`, `DR-4`, `DR-5` | sec. 6.4 (DR-1d and DR-2 are retired, sec. 6.4.1) |
| `register`, `register-caps` | `REG`, and `CAPS` less `CAPS_OK`, in P's `edits_check.py`; added text only, net of the replaced text (below) |
| `infinity` | `INF` less the `NEUTRAL` disclaimer, in P's `edits_check.py`; added text only |

**Semantics of `register` and `infinity` (D6, V1).** These profiles implement items 5 and 6 of P's
plan exactly as P's frozen checker defines them: per edit and per step of the edit list, not per
splice. The reference is P's `edits_check.py` (blob sha256 2856e58c...d98c), function `static_new`
(lines 351-380), with `inf_key` (lines 345-349) and `sentences` (lines 227-228). No approximation is
admitted.

- **Unit.** For every entry `e` of the edit list frozen at `F` (`edits.json`, read through the
  ledger adapter's companion and bound by `edits_sha256`), the pairs evaluated are `(e.old, e.new)`
  and, if `e` has them, `(e.old_step2, e.new_step2)`. Each pair is evaluated separately, as P's
  `static_new` does, whichever of them P applies. Edits that the ledger lists as retained (A1:
  D032, D039) are evaluated as P does (`old` against `new`).
- **What `old_step2` is (W1).** In P, `(old_step2, new_step2)` is not a second edit applied after
  the first. It is an alternative version of the same edit, for a later state of the file. P's
  `variant(e, text)` (lines 214-224) takes the candidates `(old, new)` and then
  `(old_step2, new_step2)`, and selects the first whose `old` text occurs exactly once in `text`.
  If neither does, it selects none. P's `check` and `apply_edits` apply only the selected pair.
- **`register`** (REG): a FAIL for each lowercased REG token in `new` that is not among the
  lowercased REG tokens of `old` (set difference per pair).
- **`register-caps`** (CAPS less CAPS_OK): a FAIL for each CAPS token in `new` that is not in `old`
  and not in CAPS_OK, only when the edit's own `kind` is one of the kinds named in the rule file
  (A1: `ptr`, `consistency`, `handoff`).
- **`infinity`** (INF less NEUTRAL): each of `new` and `old` is split by **P's splitter**,
  `re.split(r'(?<=[.;:?])\s+', text)`: a sentence ends after `.`, `;`, `:` or `?` followed by
  whitespace. This is not splitter version 2 of sec. 6.1, which does not split at `;` or `:` and so
  would change which NEUTRAL spans exempt a match. In each sentence, every INF match not contained
  in a NEUTRAL span is an assertion. `old` is first rewritten as P rewrites it (A1:
  `\bA1\b(?: \(finiteness\))?` becomes "finiteness"). Each assertion is normalized to a key as P's
  `inf_key` does (lowercase; runs of whitespace, `*` and `_` collapsed to one space; a key matching
  `finiteness\b.*\bfails` becomes "finiteness fails"). A FAIL is emitted for each assertion of `new`
  whose key count in `new` exceeds its count in the rewritten `old` (multiset difference, in P's
  order).
- **Both units, fail-closed.** The per-splice evaluation (each splice's image against the `H` bytes
  it replaces, same rules) also runs, and a FAIL from either unit is a FAIL. In addition, the
  integrity stage checks that the splices are exactly P's application of the edit list at `H`,
  selecting as P selects (W1):
  - **Counting (V1).** "Occurs exactly once" means P's count: non-overlapping occurrences found
    left to right (Python `str.count` on the file's text decoded as UTF-8). A byte-level count of
    the UTF-8 encoding gives the same number. Under this count, `old = "aa"` occurs once in
    `"xaaay"` and is selected, as P selects it.
  - **Uniqueness at `H`.** P's selection is applied to the file's text at `H` for every edit, in
    edit-list order, retained edits included. It must select a pair. If neither `old` nor
    `old_step2` occurs exactly once, P's check fails, and the tool refuses with ERROR
    `SOURCE_CHANGED`, naming the edit and both counts.
  - **Application in order.** The edits are then applied in edit-list order to a running copy of
    each file, as P's `check` and `apply_edits` do. Each edit selects its pair against the running
    copy, by the same rule, and replaces the first occurrence of the selected `old` (Python
    `str.replace` with count 1). If no pair is selected at that point, P reports the edit lost, and
    the tool refuses.
  - **Offsets back to `H` (V1).** The running copy is kept as an ordered list of segments. Each
    segment is either a run of `H`'s original text, carrying its start offset in `H`, or an image
    an earlier edit inserted. The occurrence an edit replaces, `[p, p + len(old))` in the running
    copy, must lie entirely inside one original-text segment. Its `H` span is then that segment's
    `H` start plus `p` minus the segment's start in the running copy. Character offsets are
    converted to byte offsets by the UTF-8 length of the `H` text before them. The segment is
    split around the occurrence, and the image is inserted as a new segment.
  - **Binding to the splices.** For each applied edit, the `H` byte span must equal its splice's
    `start` and `end`; the splice's replaced bytes must equal the selected `old`, and its image the
    selected `new`. A retained edit must have `old` equal to `new` and no splice. Every splice must
    belong to exactly one applied edit.
  - Any other relation is ERROR `SOURCE_CHANGED`, with the edit and splice ids.

  **Where the tool is stricter than P (C4, R-D1).** The tool computes and records P's per-edit result
  for items 5 and 6 in every case, including a refusal, so no item-5 or item-6 verdict differs from
  P's. It refuses three kinds of input that P, which has no splices, would not refuse. Each is
  accepted as a stricter refusal only because it prevents an invalid or ambiguous input:
  - **(i) A splice for the variant P does not select** (S11-58g). The ledger would write bytes P's
    application does not write, so the frozen ledger misrepresents the frozen edit list. This is
    invalid input.
  - **(ii) One splice covering two edits** (S11-57c). The frozen ledger schema gives each splice
    exactly one edit `id`, so such a splice is malformed under the plan's own schema. This holds
    even where its bytes equal P's combined application.
  - **(iii) Chained edits** (S11-58j, S11-58k). A later edit's selected occurrence lies wholly or
    partly inside an image an earlier edit inserted, or spans the point where an earlier edit's
    image, possibly empty (a deletion), was inserted; in the segment model it then crosses more than
    one segment. P applies such edits, but no set of disjoint splices
    at `H` can express that application. A frozen plan containing one has, of necessity, a ledger
    inconsistent with its edit list; it is invalid as a frozen plan, though P alone would apply its
    edit list.

  Measured with P's own code (sec. 14), every edit list that P applies and that disjoint splices at
  `H` can represent is accepted, with splices that reproduce P's resulting text: 2822 of 2822
  random cases, and A1's 401 edits. Every list P refuses is refused: 16905 of 16905. The only
  additional refusals among lists P applies are the 273 chained cases. No valid, unambiguous
  frozen-plan operation was rejected. This is not a claim of complete behavioural equivalence with
  P: P has no ledger, and the three kinds above are where the tool's input model differs from P's.
- **Extraction.** REG, CAPS, CAPS_OK, INF and NEUTRAL are extracted from P's blob by
  `python-ast-assign`. P's sentence regex is extracted from the `sentences` function by the
  extractor `python-ast-call-arg` (sec. 16.2), and its `pattern_sha256` is recorded. The edit kinds,
  the key rule and the rewrite are not extractable assignments, so they live in the reviewed rule
  file `register-infinity-params` under sec. 6.3, with positive and negative examples, and a lint
  that each equals the corresponding literal in P's `static_new` and `inf_key` source.
- **Measured on A1** (sec. 14). There are 401 edits and 399 splices. Applying all 401 edits in
  list order with P's selection binds every splice: 399 select `(old, new)` at the splice's exact
  offsets, with replaced bytes equal to `old` and the image equal to `new`. The two retained edits,
  D032 and D039, have `old` equal to `new` and no splice. No edit has `old_step2`. P's `static_new`
  gives 0 / 0 / 0 (register, caps, infinity), and so does the per-splice unit.
- **Controls (V1).** S11-56 requires the tool's result at T1' to equal P's `static_new` result on
  P's `edits.json` (0 findings each) and the mutants of sec. 11 rows 5 and 6 to FAIL. S11-57a-c are
  constructed cases on which a per-splice check alone would pass. Each is expected FAIL; the
  outcomes below were checked with P's own functions (sec. 14):
  - (a) a two-variant edit whose selected variant `(old, new)` leaves the text unchanged and whose
    unapplied variant `(old_step2, new_step2)` adds "now". P's `static_new` scans both pairs and
    gives register 1, so the tool gives FAIL `deny-match`. The per-splice unit, which sees only
    the selected variant, gives 0;
  - (b) the same with "no longer" in the unapplied variant: P register 1; the tool FAIL; the
    per-splice unit 0. The same edit at an `H` holding `old_step2` selects that variant, and the
    tool's result again equals P's;
  - (c) one splice covering two edits, one deleting "now" and the other adding it elsewhere. P's
    per-edit check gives register 1, which the tool reproduces (FAIL `deny-match`, recorded). The
    correspondence check refuses the ledger with ERROR `SOURCE_CHANGED`, because P has no splice
    that covers two edits. P checks no splices at all, so this refusal is the tool's fail-closed
    binding, and it adds no acceptance.
  - Regression controls S11-58a-f, on one two-variant edit:
    - (a) `H` holds `old` once: `(old, new)` selected;
    - (b) `H` holds `old_step2` only: `(old_step2, new_step2)` selected;
    - (c) both absent: refused, as P's check fails;
    - (d) both present once: `(old, new)` selected, as P selects the first unique;
    - (e) `old` twice and `old_step2` once: `(old_step2, new_step2)` selected;
    - (f) both ambiguous: refused, as P's check fails.

    In every case the selection, the refusal and the items 5 and 6 result equal P's. S11-58g covers
    a splice built for the variant P did not select: refused. S11-58h covers an earlier edit that
    destroys a later edit's `old`: refused, as P reports the edit lost.
  S11-57d: the `infinity` evaluation splits "The bound holds; the lattice is infinite." into two
  sentences, as P's splitter does (splitter v2 gives one), and its result equals P's `static_new`
  on the same pair.
- The landing record lists every line-level match of these profiles in the T1' splice images (the
  Stage 1 implementation reported 30) with the `old` match that cancels it.

### 6.2 Rule schema `oi-term-rules/2`

A rule file is an immutable record under the ownership chain of sec. 6.3: a change is a new file,
which carries `supersedes: {path, blob_sha256}`.

**Allow rule.** Its fields:

- `id` (never reused);
- `profiles` it addresses;
- `scope.files`: exact paths; mirrors are named explicitly;
- `matcher.literal`, which must contain the trigger, defined as the profile match span of each
  fingerprinted sentence at `recorded_at`;
- `matcher.context`: required co-occurring literals in the sentence or its neighbouring
  sentences, for example the enumerated list;
- `matcher.negative`: literals or regexes that must not match;
- `context_required`;
- `max_instances`, equal to the number of fingerprints;
- `fingerprints`: `{file, sentence_sha256, context_sha256, negative_allowance}`, where the optional
  `negative_allowance` maps a negative literal to the number of its matches in that exact
  fingerprinted sentence (S1-D1, sec. 6.2 step 3);
- `recorded_at`;
- `positive_examples` and `negative_examples`, at least one of each. These become controls;
- `reason`;
- `author`.

**Deny rule.** Its fields:

- `id`;
- `pattern`: a reviewed regex, or a two-part sentence test as for DR-3;
- `scope`: `all-corpus` or exact paths;
- `positive_examples`, at least one, which the rule must match;
- `negative_examples`, at least one, which the rule must not match, for example the W1 and W2
  sentences;
- `countercontrol`: a real line or sentence at a named commit that the rule matches, in a scanned
  file or in a control-only input named by the controls file (sec. 6.4). No constructed text
  serves as a deny rule's countercontrol;
- `reason`;
- `author`.

Fingerprints and `max_instances` do not apply to deny rules.

**Applying an allow rule.** For a hit, the steps run in this order:

1. If no allow rule has the hit's file in scope, with a literal covering the trigger and a context
   matcher that holds, the hit stays REVIEW_REQUIRED `unclassified`.
2. If any deny profile matches the sentence, the result is FAIL `deny-match`.
3. The rule's negative matcher is applied to the whole sentence, with every negative literal
   counted (owner decision S1-D1, option B). The allowance for the sentence is the
   `negative_allowance` of a fingerprint only if all of the following hold, and is zero otherwise:
   - the hit's file is the fingerprint's `file`;
   - the sentence's sha256 equals the fingerprint's `sentence_sha256` (the exact approved text);
   - the context sha256 equals the fingerprint's `context_sha256` (the approved location: the same
     neighbouring sentences), whether or not the rule sets `context_required`;
   - that fingerprint has not already granted its allowance to another sentence in this tree.

   If, for any negative literal, the sentence has more matches than the allowance grants, the
   result is FAIL `rule-negative-match`. The allowance is bound to one fingerprint, that is, one
   approved sentence at one approved location. It is never a global count, and it cannot be used
   by any other sentence, file or location.
4. If the sentence or, when required, the context differs from every fingerprint, the result is
   REVIEW_REQUIRED `rule-fingerprint-mismatch`.
5. If the rule has already been applied `max_instances` times in the tree, the result is FAIL
   `rule-overreach`.
6. Otherwise the hit is classified by the rule.

A fingerprint with no `negative_allowance` grants none. A literal's matches are counted as
non-overlapping matches of the literal (or regex) in the sentence's source bytes.

**The fingerprint's context and location (V5).** The sentence list of a file is every sentence of
every paragraph, in file order, under splitter version 2 (sec. 6.1); neighbours may lie in adjacent
paragraphs. For the sentence at index `k`, `prev` is the sentence at `k-1`, or the four bytes `BOF`
if `k` is the first; `next` is the sentence at `k+1`, or `EOF` if `k` is the last. Each sentence is
taken as the splitter yields it (lines stripped and joined with one space) and encoded as UTF-8.
`context_sha256 = sha256(prev || 0x00 || next)`. "Location" in step 3 means exactly this pair of
neighbours in the named file. It is not a line number or byte offset: a shift of the whole region
(control WB8) keeps the allowance, and so does a move of the sentence together with both of its
neighbours to another part of the same file, since the approved text and its approved neighbours
travel together (control WB13, expected PASS). A move of the sentence without both neighbours
changes the context and loses the allowance (WB5).

**One grant, deterministically (V5).** When several sentences in one file satisfy the conditions of
step 3 for the same fingerprint (identical text with identical neighbours), the grant goes to the
one with the smallest byte offset in the file; every later one gets no allowance (control WB14). A
sentence's byte offset is the byte offset, in the file as committed, of the first byte of its first
non-whitespace character (O2).

**Case (O1).** Literal entries of an allow rule's negative matcher are matched case-insensitively,
for W1, W2 and every other allow rule; a regex entry keeps its own flags. Allowances count
case-insensitive matches. Measured at T1': no W1 or W2 sentence gains a match (W1-c keeps exactly
one `finit` match), so no outcome on the real tree changes, while a capitalized edit such as an
added "Finiteness" becomes FAIL `rule-negative-match` (control WB15).

**Matching on source bytes (D8).** Every literal of an allow or deny rule (trigger, context,
negative, fingerprinted sentence) is matched against the source bytes of the file as committed,
after the splitter's whitespace normalization (sec. 6.1), never against rendered text. For example,
W2-b's context literal is `\mathrm{SU}(3)`, which is what its source line contains, not "SU(3)".

**`rule-stale` scoping (D7).** REVIEW_REQUIRED `rule-stale` (a fingerprinted sentence no longer
present) is evaluated on every tree except those that are proper ancestors of the rule's
`recorded_at`, where the fingerprinted text has not yet been written. A candidate `X`, `C`, `L` or
`M`, and `recorded_at` itself, are always evaluated. `result.json` lists, per tree, the rules not
evaluated for staleness and why. At `recorded_at` a missing fingerprint is a lint failure of the
rule (sec. 6.3), not a `rule-stale` item.

No rule ever deletes text from the line before testing.

### 6.3 Records, review records, owner authorization and lint (R11, D4)

The chain below applies to every reviewed record kind: HP adjudications, context adjudications,
hit classifications, allow and deny rule files, scope records, side-change class records,
reconciliation records, PIN_OK entries outside `F`'s pin table, and the configuration itself. One
record is one immutable file in the audit directory of sec. 12.1, or in the amended plan's record
directory for records frozen with the plan.

**Writer (author).** Prepares the record and its evidence: the exact git object ids, the subject's
`line_sha256` or region hashes, the tool's REVIEW-mode explanation for that subject, and the
semantic statement (which qualification is visible, and why). The evidence may include tool
output, but the record states its classification in its own words. Its `author` field names the
writer. A writer may not review a record they wrote.

**Independent reviewer.** A non-author re-derives each record from the git object store, not from
the writer's output. For an HP record that means recomputing the walk, checking each step's commit
and hashes, and reading the pre and post text. For a classification or context record it means
reading the sentence and its context at the stated tree and judging the semantic statement. The
reviewer writes a separate immutable review record, schema `oi-review-record/1`, with:

- `reviewer`;
- `reviewed`: `{path, blob_sha256}` of exactly one record;
- `method`: how each item was re-derived, naming the object ids read;
- `verdicts`: one entry per item id of the reviewed record (`accept`, `reject` or `dissent`, with
  the reason);
- `dissent`, if any.

A review that cites only a passing tool run is invalid.

**Owner authorization.** The owner authorizes exact content. An authorization record, schema
`oi-owner-authorization/1`, quotes the owner's comment with `owner`, `time` and `comment_id` (sec.
A.42 item 7) and lists `authorizes: [{record: {path, blob_sha256}, review: {path, blob_sha256}}]`.
A batch may be authorized by one authorization record that lists every member. An authorization
that names a path without a hash authorizes nothing.

**Frozen configuration.** `retirement-config.json` at `F` references every record, review record
and authorization record by `{path, blob_sha256}` (sec. 16.2). A record added after `F` is
admissible only under sec. 13.3's reconciliation rule and never for a decision on `X`.

**What the tool checks.** A record fails, with FAIL `record-invalid`, on any of these:

- a referenced blob that does not exist at `F` at its path, or whose hash differs (this is ERROR
  `SOURCE_CHANGED` when the blob is the configuration's own reference);
- a schema or field error, or a missing field;
- no review record naming exactly this record's blob, or a review record naming another blob;
- `reviewer` equal to `author`;
- a review whose `verdicts` do not cover every item id of the record, or any item not `accept`;
- no authorization record listing both this record's blob and its review's blob;
- an authorization whose `owner` differs from the configuration's owner, or with no `comment_id`;
- a `reviewer`, `owner` or `comment_id` value that points to a tool run, a CI run, a check run or
  an Issue (a URL or run id rather than a person and a comment);
- a broken `supersedes` chain, or a reused id, for every record kind (S4): each `supersedes` must
  name a `{path, blob_sha256}` that exists in the object store at or before `F` and is a record of
  the same kind, schema and lineage; a chain naming an id or blob that never existed as a record
  (for example an off-repository draft) is FAIL `record-invalid`. A first record has
  `supersedes: null`;
- **lineage (DI-2)**, for every record kind that carries `supersedes`. A record's lineage is its
  `record_id`, a non-empty string at the record's top level; for the configuration it is its
  `config_id` (sec. 16.2). `record_id` is immutable within a lineage: a superseding record has the
  same kind, schema and `record_id` as the record it names. Sharing a `record_id` within one lineage
  is not reuse of an id; a `record_id` carried by two records that do not lie on one `supersedes`
  chain is. Each of the following is FAIL `record-invalid`:
  - a record without a valid `record_id` (missing, empty or not a string) that supersedes another
    record or is named by a `supersedes`;
  - a `supersedes` naming a record whose kind, schema or `record_id` differs (an unrelated chain),
    at any step of the chain;
  - a `supersedes` naming a predecessor that does not itself pass this lint, read from the object
    store at or before `F` and verified independently of the superseding record (its own review
    and authorization, each authorization its lint requires, a widening review's included,
    checked as "Owner at creation" states for a predecessor,
    in place of the comparison with the configuration's owner);
  - a cycle in a `supersedes` chain;
  - ambiguous ancestry: two records superseding the same predecessor, among the records in the
    audit directory and the plan's record directory at `F` and the records the run reads; or a
    lineage with two heads used in one run, a head being a record of the lineage that no other
    record the run reads (the records the configuration references and every record their chains
    name) supersedes;
- a record not read from the git object store.

The tool never infers a role, a review or an authorization from a passing tool result.

**Configuration admission and the root of trust (O5, B3, V2; owner decisions D1-D5 of
2026-11-23, called A-D1 to A-D5 here, and of the v5.4 review, called R-D1 to R-D5).** Neither the
caller nor `F` can establish who designated `F`, in which repository, by which workflow, or with
which code. These authority values come from one reviewed record, the **tool authority record**
`A`, which the caller cannot override and a frozen plan can never redefine.

**The authority record `A`** (schema `oi-tool-authority/2`). `A` lives at the fixed path
`tools/ledger_coverage/authority.json` (R-D4). This is a generic location of the tool's own data,
not a retirement record, and lies outside the engine's purity scope. `A` lands on `main` before any
freeze, through the authority-change procedure below. Its fields are:

- `owner`: `{id, login}`. The numeric user id decides identity; for A1 it is 7273571. The login
  (`amaybaum`) is informational and is never used to match (A-D1, R-D4).
- `repository`: `{id, full_name, fork: false}`. For A1, id 1156244443, `amaybaum/incompleteness`,
  not a fork (A-D4).
- `workflow`: `{path, content_sha256}` of the one workflow whose runs may produce an acceptable
  result (A-D4). The workflow's reviewed content must check out exactly the run's `head_sha`, verify
  the tool blobs against `engine_pins` before executing, and run the tool only from that tree (V3).
- `engine_pins`: `{path: blob_sha256}` for every file of `tools/ledger_coverage.py` and
  `tools/ledger_coverage/` that the run executes (engine and adapters) (V3, R-D3).
- `plans`: one entry per plan, with:
  - `plan_id`;
  - the authorized thread (`repository_id`, issue number);
  - the allowed `round` ids;
  - `pin_table_path`, the path of the PREREG pin table in `F`.

  A *plan id* names one retirement plan and its thread. A *round* names one freeze cycle of that
  plan; at most one `F` is valid per plan and round. Both are defined here and never in `F` (A-D3).
- `authority_thread`: `{repository_id, issue}`, where authority changes are approved (C1).
- `freeze_ledger_path`: the path, on `main`, of the freeze ledger (below).
- `forms`: the exact versioned forms below, with `version: 1`, and the first-line rule (C2, V5).
- `supersedes`: `{path, blob_sha256}` of the `A` it replaces, or null for the first. `A` carries no
  `record_id`: its lineage is its fixed path. `supersedes` must name the version of `A` that
  precedes it on `main`'s first-parent chain, at the same path; otherwise admission refuses (DI-2).

The owner identity is never derived from the repository owner, the caller, the environment or the
frozen plan (A-D1).

**The forms (C2, R-D4).** The first line of a host comment is its body's bytes up to the first LF,
with at most one trailing CR removed, and with no other normalization (V5). A comment carries a form
only if its first line is exactly one of the following, with single spaces, lowercase 40-hex commit
ids and lowercase 64-hex sha256 values:

- `oi-freeze/1 designate plan=<plan_id> round=<round_id> commit=<F>`
- `oi-freeze/1 withdraw plan=<plan_id> round=<round_id> commit=<F>`
- `oi-freeze/1 supersede plan=<plan_id> round=<round_id> commit=<F> by=<F2>`
- `oi-authority/1 approve from=<sha256 of the A replaced, or "none"> to=<sha256 of the new A>`

An owner comment whose first line begins with `oi-freeze/` or `oi-authority/`, but does not match
one of these exactly, refuses. This covers an unknown version (`oi-freeze/2 ...`), a wrong key
order, a trailing space, and a plan or round that `A` does not list. A comment written for another
purpose cannot match.

**Owner at creation (DI-1, owner decision of 2026-11-23).** A comment never acquires authority
merely because its author becomes the owner later, or becomes the owner again.

- **Definitions.** The version of `A` *in force* at a time `t` is the latest version of `A` whose
  landing merge on `main`'s first-parent chain has a host merge time strictly before `t`. An *owner
  comment* is a comment whose author numeric id equals the `owner.id` of the version in force at the
  comment's creation time; a comment created when no version was in force is not one. An *owner
  change* is the merge on `main` of a version of `A` whose `owner.id` differs from that of the
  version it replaces.
- **Withdrawals and revocations.** A withdrawal, and the revoking half of a supersession (the
  withdrawal of `F`), counts if it is an owner comment. It stays effective after any later owner
  change.
- **Designations.** A designation, and the designating half of a supersession (the designation of
  `F2`), counts only if it is an owner comment, its author numeric id equals the `owner.id` of the
  authority record governing the admission, and no owner change merged between its creation and the
  admission. After an owner change, the round is designated again by the owner in force. A
  supersession recorded in the freeze ledger or in a committed snapshot only revokes; it never
  designates (sec. 6.3, "The freeze ledger").
- **Approvals.** An `oi-authority/1 approve` comment and an `oi-freeze-ledger/1 append` comment
  count only if each is an owner comment, its author numeric id equals the `owner.id` of the
  authority record governing the evaluation, and no owner change merged between its creation and
  the merge it authorizes. An owner change away and back does not restore an earlier approval. The
  authority record governing the evaluation is, for an authority change, the version it replaces;
  for a freeze-ledger change, the version in force at its merge, or `main`'s current `A` for an
  append not yet merged.
- **Owner authorizations.** An `oi-owner-authorization/1` record counts for a record the run uses
  only if the version of `A` in force at its `time` has `owner.id` equal to its `owner`, its `owner`
  equals the `owner.id` of the authority record governing the admission, and no owner change merged
  between its `time` and the admission. Each authorization of a predecessor named by a
  `supersedes`, a widening review's included, is a completed action: it counts if the version of
  `A` in force at its `time` has `owner.id` equal to its `owner`.
- **The first `A` and an owner-id change.** The approval of the first `A`, and the new id's approval
  of an owner-id change, are by the id the new `A` pins, which is not yet the owner. Each is
  authenticated as that id (sec. 6.3, "Authority changes"), not as an owner comment. It must still
  be created before the merge it authorizes, with no owner change merged between its creation and
  that merge. The previous id's approval of an owner-id change is an approval under the rule above.
- **Completed actions.** An authority change or a freeze-ledger change merged on `main`'s
  first-parent chain is completed. It stays valid if its approvals counted under these rules at its
  merge, and a later owner change never invalidates it. An acceptance landing merged on `main` is
  completed; the admission its snapshot records stands, and the events it appended bind under
  reconciliation. A designation is not completed for a later admission: each admission evaluates it
  under the rule above against the authority record governing that admission. A withdrawal, and the
  revoking half of a supersession, bind from their creation.

**The trust root, without circularity.** `A` is data. It cannot authenticate itself, and the owner
id inside it cannot be what authenticates it. Its authority rests on things outside `A`, the caller
and `F`, all read by the tool and, separately, by the consumer from the host, never from a run's
own output: from the host's REST API, and from a local git object store each of whose objects is
bound by its hash to an id the host reported (point 2; HS-1):

1. **The host's attestation of the run.** The tool and the consumer each read the run record,
   from the host's REST API, by the run id the host assigns. It gives:
   - the repository's numeric id and fork status;
   - the workflow path;
   - the run's `head_sha`.
2. **That repository's `main`.** `A` is read only from `main` of the attested repository, at the
   head the host reports. It is never read from the caller's checkout, another ref, another
   repository, a file the caller supplies, or `F`'s tree. `A.repository` must equal the attested
   repository id. This is a consistency check of `A` against the attestation, not a source of
   trust.

   **Repository history from a verified local object store (HS-1, HS-4).** The commit id of `main`
   is read once per admission from the host's REST record of the attested repository's `main`; that
   one id anchors every read from `main` in the admission. It and the run's `head_sha` (point 1)
   are the anchors. The first-parent chain, every version of `A` and of the freeze ledger, and every
   commit, tree, tree entry and file that the trust root, the authority-change procedure and the
   freeze ledger read come from a full local git object store, read by object id only; commits named
   otherwise (`F` and `F2` in owner comments, the evaluated commits) are read the same way:
   - **Each object verified.** Every object is requested by its id, and its id is recomputed from
     its type, length and content. An object that is missing, or does not hash to its id, refuses. A
     commit's parents and tree, and a tree's entries, are parsed from the verified content. The
     store's refs, reflogs and packed refs are never consulted.
   - **Replace and graft mechanisms ignored.** Replace refs (`refs/replace/`) and graft files are
     never applied, and no commit-graph file is trusted: every object is read with replacement
     disabled, and no parent is taken from a traversal command, a graft, the store's `shallow` file
     or a commit-graph.
   - **The chain reaches a root.** The first-parent chain from `main`'s anchor is followed to a
     commit with no parent; a parent missing from the store refuses. `head_sha` must lie on that
     chain. Ancestry, such as `F`'s descent from a `main` commit that contains `A`, is computed from
     the same parsed parents.
   - **Shallow and partial stores refused.** A store that is shallow (it holds a `shallow` file) or
     partial (a promisor remote, a partial-clone filter or `extensions.partialClone` configured, or
     a promisor pack present) refuses, whatever objects it holds. No object is fetched on demand.
     This design states no other means of establishing such a store's completeness. The
     completeness it relies on is that every object the admission needs is present and verified, and
     that the chain reaches a root.
   - **Anchors absent.** If `main`'s anchor or `head_sha` is not in the store, the admission refuses.
     The workflow therefore fetches the exact anchor id, by its full id, into the full store before
     admission (no depth, no filter); the objects fetched are verified like any other, and the tool
     itself fetches nothing (N4).
   - **Entries.** `A`, every version of the freeze ledger, review records and committed admission
     snapshots are read only from regular-file entries (mode 100644 or 100755); a symlink, a
     submodule or any other entry at such a path refuses (N5). Non-regular entries under
     `tools/ledger_coverage/` refuse as point 3 states.
   - **Other reads.** The same reader, with the same store checks, serves every other read the
     tool makes from a git object store, in a run or in the offline replay of sec. 5; outside
     admission, a refusal there is the integrity error of sec. 5 (HS-4).

   The host's own commits, trees and contents are addressed by the same ids, so the bytes read are
   those the host holds under the ids it reported, under the assumption on object ids stated under
   "Residual trust assumptions".
3. **Execution identity (V2, V3, R-D3).** The run's `head_sha` must be a commit on `main`'s
   first-parent chain of the attested repository that contains `A`, the reviewed tool and the
   pinned workflow. The following are read at that `head_sha` from the verified store of point 2:
   - the content of the file at `A.workflow.path`, whose sha256 must equal `A.workflow.content_sha256`;
   - every blob that `A.engine_pins` names, whose sha256 must equal its pin;
   - **the files permitted under `tools/ledger_coverage/` (K7).** Besides the files `A.engine_pins`
     names, exactly two files are permitted there, each only at its own path and as a regular file:
     - the authority record at `tools/ledger_coverage/authority.json`, whose blob sha256 must equal
       that of the `A` admitted for the run (read from `main` and verified by the authority rules of
       this section);
     - the workflow at `A.workflow.path`, if that path lies under the directory, whose content
       sha256 must equal `A.workflow.content_sha256`.

     Every other file under `tools/ledger_coverage/` at `head_sha` refuses the run, whatever its
     content; that includes a second copy of the authority record or of the workflow at another
     path. A permitted path whose content differs from its pin, or which holds a symlink, a
     submodule or another non-regular entry, also refuses. These two allowances are explicit and
     limited to these two independently pinned components. They are not a general exception, and
     no other identity, admission or authorization check is relaxed by them.

   The commits evaluated (`X`, `C`, `L`, `M`, and `H` and `E`) are explicit inputs, resolved from
   the object store and recorded. They are never the run's `head_sha`, because `X` (`H` plus the
   ledger) does not contain the tool.
4. **Acceptance in the canonical repository.** A result is accepted only by its landing on `main`
   of the repository in which the owner lands it (A-D5). The landing check run there reads `A` from
   that `main` itself, repeats points 1-3 for the producing run, and compares the evaluated commits
   with the landing record's. So a run in a fork, or one that ran other code, is never accepted.

**Authority changes (C1, R-D4).** An authority record takes effect only if all of the following
hold:

- **An owner approval comment.** It is in `A.authority_thread`, with the first line `oi-authority/1
  approve from=<sha256 of the previous A> to=<sha256 of the new A>`. Its author numeric id is the
  previous `A`'s `owner.id`. It is verified like a designation: never edited, not hidden, the
  thread read completely, and no conflicting approval. Its creation time precedes the merge that
  lands the new `A`. The merge alone authorizes nothing. It must also count as an approval under
  "Owner at creation" above.
- **An owner-id change** also needs the same approval from the new id, in a separate comment. That
  approval is authenticated as "Owner at creation" states for the new id.
- **An independent review record** (sec. 6.3) names both blobs.
- **The merge is a pull request into `main`.** The merge record is the host's REST pull-request
  record whose merge commit id equals the commit that lands the new version on `main`'s first-parent
  chain, merged into `main` of the attested repository; none, or more than one, refuses (HS-1). Its
  merge time is the host merge time that "Owner at creation" uses. The merge is recorded as
  provenance. Its merged-by id must equal the previous owner id, but that is a provenance check and
  not the authorization.
- **The first `A`** carries `supersedes: null` and an approval `from=none`, by the id it pins, with
  its review record. That check is consistent, but circular: nothing in the tool can authenticate
  the first `A` from its own content. It stays a residual trust assumption (below).
- **Every change to `A` on `main`** between its first version and the version in use must satisfy
  this procedure. Otherwise admission refuses. An unrecoverable loss of the owner account cannot be
  repaired inside the tool, and the result is fail-closed.

**Changes between `F` and execution.** `F` must descend from a `main` commit that contains `A`. If
`main`'s current `A` equals `F`'s copy, it governs. If they differ, the run is refused unless every
change between them passed the authority-change procedure, in which case the current `A` governs
and both blobs are recorded. `F`'s copy never governs on its own, so a frozen plan can never
redefine the authority rules.

**The caller cannot override.** No command-line option, environment value, configuration field or
record in `F` can set or override any of these: `owner`, `repository`, `workflow`, `engine_pins`,
`plans`, `authority_thread`, `freeze_ledger_path` or `forms`. The retirement configuration (sec.
16.2) cannot contain these fields; an unknown field there is ERROR `CONFIG_INVALID`. A configuration
supplied as a file or path is never read as `A`.

**The freeze ledger (withdrawal integrity, R-D2).** A thread listing cannot show that a comment
once existed. So withdrawals and supersessions, once observed, are made durable on `main`:

- **The ledger.** It is a record `oi-freeze-ledger/1` at `A.freeze_ledger_path` on `main`. It is an
  append-only list of observed events per plan and round. Each event is a designation, withdrawal
  or supersession, with its commit ids, comment id, author numeric id, creation time, edit status
  as read, first line, and body sha256.
- **How it changes.** Every change lands through the authority-change procedure, with an
  `oi-authority/1 approve` comment quoting the old and new ledger blob hashes. Every acceptance
  landing (sec. 5) also appends the events its admission observed.
- **Approval of each acceptance-time append (N3).** No append takes effect, including the append an
  acceptance landing makes, without its own explicit owner approval comment. The comment must:
  - be in the plan's authorized thread;
  - have the first line
    `oi-freeze-ledger/1 append plan=<plan_id> round=<round_id> from=<sha256 of the ledger before> to=<sha256 of the ledger after>`,
    with single spaces and lowercase 64-hex values, the first line as defined for the forms above;
  - be an owner comment that counts as an approval under "Owner at creation" above (for A1, numeric
    owner id 7273571);
  - be created before the merge that lands the append.

  It is verified exactly like a designation, by host means: the thread is read completely; the
  comment is matched by its immutable id, author numeric id, creation time and edit status; it is
  never edited, has no edit history, and is not hidden. An owner comment whose first line begins
  with `oi-freeze-ledger/` but does not match this form exactly refuses, and so does an unknown
  version. Without such a comment, quoting exactly the ledger blob hashes before and after the
  append, the append is refused: the acceptance landing does not merge. A ledger on `main` whose
  append lacks a verified approval comment is unverifiable, and every later admission refuses
  (TR36).
- **Reconciliation.** Every admission reconciles the thread with the ledger and with every
  admission snapshot already committed on `main` (sec. 5):
  - a withdrawal or supersession in the ledger or in a committed snapshot binds, even if its
    comment is now deleted, hidden or edited, so it can never silently reactivate an earlier
    freeze;
  - a designation must be present and verifiable in the thread now; a ledger entry alone never
    designates;
  - a ledger or snapshot event that conflicts with the thread refuses, as does a missing ledger or
    one that cannot be verified.
- **The residual.** A withdrawal or supersession that is posted and then deleted before any
  admission observes it, and before it reaches the ledger, cannot be detected, unless the host
  exposes deletion events for the thread. If it does, any deletion of an owner comment refuses. This
  is a residual of the host model, stated below.

  **What the host exposes (HS-6).** The host's REST listing holds only the comments that exist when
  it is read, and the issue's comment count counts only those; a deletion lowers both alike, so the
  completeness check of admission point 2 cannot reveal it. No REST issue-event or timeline type
  records a comment's deletion. The host's GraphQL schema documents a `CommentDeletedEvent`; whether
  it is emitted for every deletion, and whether it identifies the deleted comment's author by
  numeric id, is not established. The host does expose these events for a thread, so the rule
  above applies: the tool reads them and refuses on any deletion of an owner comment, or of a
  comment whose author cannot be shown not to be an owner (admission point 3, "Deletion events";
  B1). Neither API returns a deleted comment's id, body or first line, so the form a deleted comment
  carried cannot be reconstructed from the host. The absence of reported deletion events establishes
  nothing: it is never taken as proof that no comment was deleted, the residual stands, and no
  complete historical coverage of a thread is claimed. Whether the events are complete is an open
  investigation (sec. 15 item 9).

**Admission.** The tool performs the following inside a host CI job. Any step that fails or cannot
be completed refuses admission with ERROR `CONFIG_UNREVIEWED`:

1. **Run and execution identity.** Points 1-3 of the trust root.
2. **The thread, read completely.** Every comment of the plan's authorized thread is read from the
   host's REST listing, page by page, until the host reports no further page, and the count must
   equal the comment count of the host's REST record of the issue; comment ids must be unique. Each
   comment gives its id, node id, author numeric id and login, creation time, `updated_at`, body and
   `minimized` field. A mismatch, a repeated id, a page error or an unavailable API refuses (no
   fallback).
3. **Every owner comment's edit status (V4, R-D2).** For every comment whose author numeric id is
   `A.owner.id`, and every owner comment as "Owner at creation" defines it (in this point and point
   4, each of them is meant by "an owner comment"), relevant or not, the tool reads the version of
   `A` in force at its creation, its edit status and its hidden state, as stated below. The
   admission refuses if any of the following holds:
   - an owner comment carrying a form has any recorded edit (a designation edited and restored stays
     invalid, A-D2);
   - an owner comment's edit history ever contained a first line beginning with `oi-freeze/` or
     `oi-authority/`;
   - an owner comment is hidden or minimized;
   - an owner comment's edit status cannot be read.

   **Edit history (HS-2, HS-3).** The edit history and the deletion events of the threads the
   admission reads are the only facts the tool reads through the host's GraphQL API; REST provides
   neither. For every owner comment, whatever its `updated_at`, the tool reads
   `lastEditedAt` and `userContentEdits` (`totalCount`, and each revision's `diff`, `editedAt` and
   `deletedAt`), by the node ids of the REST listing, in batched queries of at most 100 node ids
   (HV3). `userContentEdits` is read with its first 100 revisions and is not paginated, so a
   comment with more than 100 revisions refuses under the `totalCount` rule below (N2). The content
   of a revision is its `diff`, and its first line is defined as for the forms. The edit status
   cannot be read, and the admission refuses, if any of the following holds; no revision is ever
   skipped:
   - a request fails, or its response carries an error, a rate-limit response or a partial result;
   - a requested node is missing or null, is returned twice, carries another node id, or is not an
     issue comment;
   - `lastEditedAt` or `userContentEdits` is absent;
   - fewer revisions are returned than `totalCount` states;
   - a revision's `diff` is null or absent, or its `deletedAt` is set;
   - the comment is edited in the sense below while its earlier text is unavailable: no revision is
     returned (`totalCount` 0). Whether the revisions returned hold the text of every earlier
     version is the feasibility question below (B2).

   **Required earlier text (F4).** The edit-history rules need the full text of every earlier
   version of a comment. That GraphQL `diff` carries it is not established: the schema describes
   `diff` as "A summary of the changes for this edit". HV4 and HV8 test it. If the host does not
   expose the full earlier text, the stage fails and the design returns to the owner; no rule of
   this section is relaxed and no other source is substituted.

   **Deletion events (B1; "The freeze ledger", "The residual"; HS-2, HS-6).** For every thread the admission
   reads (the plan's authorized thread and `A.authority_thread`), the tool reads the issue's
   timeline items of type `CommentDeletedEvent` through GraphQL, page by page in pages of at most
   100 until the host reports no further page, in batched queries (a page may share a request with
   an edit-history batch). For each event it reads its id, creation time and
   `deletedCommentAuthor`, whose numeric id is read through a `User` fragment. The admission
   refuses if any of the following holds:
   - any failure of the edit-history list above applies to the read (request failure, error,
     rate-limit response, partial result, absent field), or the events returned differ in number
     from the `totalCount` the host states, or an event id repeats;
   - an event's `deletedCommentAuthor` is absent, null or not a `User`, or its numeric id is absent;
   - an event's author numeric id equals the `owner.id` of any version of `A` on `main`'s
     first-parent chain (the deleted comment's creation time is not exposed, so it cannot be shown
     not to have been an owner comment).

   An event whose author's numeric id differs from the `owner.id` of every version of `A` does not
   refuse. The absence of events establishes nothing (sec. 6.3, "The freeze ledger").

   **Edited (HS-5).** A comment is unedited only if GraphQL reports `lastEditedAt` null and
   `totalCount` 0, and REST reports `updated_at` equal to `created_at`. Any one of the three signals
   makes it edited; "any recorded edit" above means edited in this sense. `updated_at` can add an
   edit signal; its equality to `created_at` never removes one and is never proof that a comment was
   not edited.

   **Hidden state (HS-2).** It is read from the REST field `minimized`. Only `null` reads as not
   hidden, and a non-null object reads as hidden. An absent field, or any other value, cannot be
   read, and the admission refuses.

   A comment whose author has the owner's login but another numeric id is not the owner's. It is
   reported, never matched.
4. **Forms.** The owner comments of point 3 whose first line begins with `oi-freeze/` are parsed
   by the forms
   above. A malformed or unknown-version line refuses.
5. **Deterministic state.** The forms for this plan and round, together with the bound events of the
   freeze ledger and committed snapshots, are processed in order of creation time, then comment id.
   A form, or half of a supersession, that does not count under "Owner at creation" is not processed:
   - a designation of `F` makes `F` designated;
   - a withdrawal of `F` makes it withdrawn;
   - a supersession of `F` by `F2` withdraws `F` and designates `F2` (a supersession recorded in the
     freeze ledger or in a committed snapshot only revokes: "Owner at creation", "Designations").

   The run's `F` is admitted only if, at the end, it is the one designated commit of the round. Any
   of the following refuses: two live designations; a withdrawal or supersession naming a commit
   never designated (for this test, a designation that was an owner comment at its creation has
   designated its commit, even if it is not processed); a designation of a withdrawn commit; any
   other conflict.
6. **The pin table.** `F`'s PREREG pin table is read from `F`'s tree, at `pin_table_path`. Its
   content is authenticated by the owner's designation of exactly `F`. The retirement configuration
   and its review record and owner authorization are admitted only if listed there with their
   sha256. Files beside the configuration are never admitted.
7. **The owner field.** `retirement.owner` must equal `A.owner.id`, and so must the owner of the
   configuration's authorization record. Every authorization record the run uses must also count
   under "Owner at creation" above; otherwise FAIL `record-invalid`, or ERROR `CONFIG_UNREVIEWED`
   for the configuration's own.
8. **Optional equality.** `--config-sha256`, if given, must equal the admitted configuration's
   sha256. It is an extra check and never a substitute.
9. **Local runs and replay.** A run outside a host CI job, or one that cannot reach the host's REST
   or GraphQL API or has no full local object store (point 2), cannot reach `"chain"`. The offline
   replay of sec. 5 writes `"admission": "replay"` and is never acceptable as a new run.

**The admission snapshot (C3).** `result.json` records `config.admission`. Its mode is `"chain"`
only when points 1-7 held, and it carries the snapshot:

- `A`'s blob sha256, the chain of approval comments, and the merge commits;
- the run record fields read: run id, repository id and fork status, workflow path and content
  sha256, `head_sha`, and the engine and adapter blob hashes at `head_sha`;
- `main`'s commit id as the host reported it, which anchored every read from `main` (point 2);
- the evaluated commits `E`, `H`, `X`, `C`, `L` and `M`;
- the thread's complete comment-id list and count;
- for every comment of admission point 3: id, author numeric id, creation time, the blob sha256 of
  the version of `A` in force at its creation, edit status (GraphQL `lastEditedAt` and `totalCount`,
  the sha256 of each revision's content, REST `updated_at`, and the resulting edited flag), hidden
  state (the REST `minimized` value as read), full first line and body sha256;
- for every thread read, the deletion events read (event id, creation time, author numeric id) and
  their count (B1);
- the freeze-ledger blob, and the committed snapshots it was reconciled with;
- `F` and the pin table's `{path, blob_sha256}`;
- **the delegated evidence (F2)**, for every delegated and native class of sec. 7.3, at `X` and, where
  `C` differs, at `C`:
  - the host records the tool read for the class, as the host returned them (run and job records
    with their ids, `head_sha`, workflow path, names and conclusions; for `pdf`, the artifact
    record), in canonical JSON;
  - the sha256 of every artifact and result file the class used;
  - the outputs of every checker the tool ran natively: for each run, the checker blob sha256, the
    exact command line, the working directory, the exit status, and the complete bytes of each
    result file it wrote and of each output the class compares (for example SC-42's `--verbose`
    and `--self-test` outputs, `proof_census.py --json`, and preserve_check's result files for
    `tex` and `pdf`);
  - the class's own recorded re-derivations (sec. 7.2);
- the sha256 of the canonical JSON of the snapshot itself.

Only `"chain"` is acceptable (sec. 5). The control harness (sec. 10.4) may admit a draft
configuration without its chain. Its results carry `"admission": "control-harness"` and are never
written as an acceptable result.

**Residual trust assumptions, stated.** The tool and the consumer trust:

- **The host's APIs and their attestations.** The REST API: the run record (repository id, fork
  status, workflow path, `head_sha`); `main`'s head commit id; a pull request's merge commit,
  merged-by id and merge time; and a comment's immutable id, numeric author id, creation time,
  `updated_at`, body, hidden state, and the completeness of a thread's listing of the comments that
  exist when it is read. The GraphQL API: a comment's edit history, that is, each recorded revision,
  its content, and their count; and a thread's deletion events and their authors (HS-2, B1).
- **Git object ids.** The content of files at a commit and `main`'s history are read from a local
  object store and bound to the ids the host reported by recomputing each object's id (trust root
  point 2). That binding rests on SHA-1's second-preimage resistance against the objects the host
  holds, and on the host's and git's refusal of objects that collision-detecting SHA-1 flags (N1).
  The local store itself is not trusted.
- **The host runner:** that it executes the pinned workflow at `head_sha` faithfully, so that the
  code that ran is the code whose blobs were read.
- **The host's access control on the canonical repository's `main`.**
- **Who can delete, hide or edit comments in the authorized threads:** the owner, and accounts the
  host grants moderation rights in the repository. Edits and hiding are detected (admission point
  3). A deletion is detected only for events already in the freeze ledger or in a committed
  snapshot, or if the host reports deletions (admission point 3, "Deletion events"). A withdrawal
  deleted before any admission observed it, and not reported by the host, remains a residual, and so
  does any form a deleted comment carried.
- **The integrity of the first reviewed and owner-approved landing of `A`,** which nothing in the
  tool can verify from `A`'s content.
- **The owner's own account.**
- **At acceptance time, the authenticity of the admission snapshot** (that its comments and run
  record were genuine). This is host-attested and is not reproducible offline (sec. 5).

If any of these fails, the tool's checks can be deceived. None of them is a value the caller can
choose.

**Corrections.** A correction is a new record with `supersedes`, a new review and a new owner
authorization. Nothing is edited in place, and an id is never reused.

**Residual limit.** The tool can check that the role fields differ and that the quoted
authorization exists, not who actually wrote them. Identity rests on the reviewer's and the
owner's own recorded statements.

**Widening of an allow rule.** Any of the following, compared with the superseded version, is
widening:

- added files;
- a changed or shorter literal;
- fewer context or negative literals;
- **any change to the fingerprint set**, including a swap with the count unchanged (control A3r);
- a larger `max_instances`;
- `context_required` turned off;
- a new allow rule without `supersedes`;
- any `negative_allowance` added, raised or moved to another fingerprint.

**Widening of a deny rule.** A changed pattern, a narrower scope, removed examples, or a removed or
changed countercontrol.

Widening needs a `widening_review` record by a non-author reviewer other than the record's own
reviewer, under the same chain as any review (B4): the widening review names the superseding
record's blob and the superseded record's blob, its `verdicts` cover every item that differs
between the two (each changed field, added file, fingerprint or allowance), every verdict is
`accept`, and an owner authorization lists the widening review's blob. A widening review that
covers only some items, has no authorization, or names other blobs is invalid. Widening without a
valid widening review is FAIL `record-invalid`.

**Examples and fingerprints.** Each fingerprint must be reproduced by a sentence of its named file
at `recorded_at`. Each example and countercontrol must behave as stated. Every fingerprinted
sentence, read at `recorded_at` in its named file, must be classified PASS by its own rule through
steps 1-6 of sec. 6.2, with its own allowance (D1). Every `negative_allowance` must equal, literal
by literal, the number of matches of that negative literal in its fingerprinted sentence, and may
name only literals of the rule's negative matcher. A rule's positive examples include each
fingerprinted sentence in full, not a fragment of it. Otherwise the record fails the lint.

**Kind-specific rules.**

- **PIN_OK.** An entry is valid only if listed in `F`'s pin table, or in a reviewed record that the
  configuration at `F` references. An entry dated after `F` is FAIL `pin-broken`.
- **Reconciliation.** A record written after `F` is valid only for a side change on `M`, and it
  never changes a decision of op C on `X` (sec. 13.3).

### 6.4 Deny rules DR-1, DR-3, DR-4, DR-5 (for independent review; measured in sec. 14)

These strengthen v3's seed rules as review-v3 required (R2, R3), less the two candidates the owner
dropped (V5-D1; sec. 6.4.1). They are a proposal for the independent review that the plan amendment
needs (sec. 11 note 1); they are not adopted. All are case-insensitive. Each must match none of the
W1 and W2 sentences at T1' and none of the replacement "Thirteen items" sentence
(papers/Main.md:738 at T1'); measured, none does. The identifiers DR-1d and DR-2 are retired and
are never reused.

Below, `N` is `(?:assumptions?|axioms?|posits?|premises?|conditions?)`, `CNT` is
`(?:six|seven|sixth|seventh)`, `LBL(k)` is `(?:\(\s*Ak\s*\)|\bAk\b)`, and `SEP` is
`(?:\s*(?:-{1,3}|–|—|\bthrough\b|\bto\b|\$?\\(?:text)?(?:endash|emdash)\$?)\s*|\s*,\s*(?:\.{3}|…|\$?\\l?dots\$?|\$?\\cdots\$?)\s*,?\s*)`.

- **DR-1** (a count or ordinal of the structural posits, or the A1-A6 range). One of:
  - a: `(?i)\bCNT\b[^.;]{0,40}\b(?:structural|substratum(?:'s|’s)?)\s+N`
  - b: `(?i)\bCNT\b[^.;]{0,40}\bstructural\s+propert(?:y|ies)\s+of\s+the\s+substratum\b`
  - c: `(?i)` followed by `LBL(1)`, `SEP` and `LBL(6)` in sequence (hyphen, double or triple hyphen,
    en dash, em dash, "through", "to", TeX dash macros, and the bare ellipsis list "A1, ..., A6",
    each with bare or parenthesized labels; a list with intermediate items, such as
    "A1, A2, \ldots, A6", is not matched)
- **DR-3.** A sentence (sec. 6.1) that matches both
  - the count part `(?i)structural\s+propert|structural\s+assumption|structural\s+axiom|structural\s+posit|\bposits?\b|\bpremises?\b|\baxioms?\b`, and
  - the tail `(?i)(?:one of which|one of its|one of the|among|includ\w*|the first being|first of which|namely)[^.;]{0,60}?(?:total[- ]finiteness|finite in total|totally finite|finiteness of (?:\$?\\?(?:mathcal\{)?S\}?\$?|the (?:configuration|state) space)|finiteness\b)`.
- **DR-4** (the retired posit entry; crosses the label's own period):
  `(?i)(?:\(\s*A1\s*\)|\bposit\s+A1\b|\bA1\b\s*(?:\(|:))[^.;]{0,60}(?:\.[^.;]{0,80})?\b(?:finit\w*|configuration\s+space|substratum)`
- **DR-5** (the posit-ledger count): `(?i)\b(?:fourteen|14)\b[^.;]{0,40}\b(?:items|posits|entries|premises|assumptions)\b`

DR-1, DR-4 and DR-5 are evaluated on each line and on each sentence; DR-3 on each sentence.

DR-1's ordinal alternatives also match current, legitimate references to A6 as "the sixth structural
assumption" in active files outside the corpus (for example `verification/README.md:2320` and
`A6Instantiation.lean:15` at T1'). In the corpus that usage was retired. The ordinal alternatives
therefore encode a corpus terminology decision, which the amendment states (sec. 11 note 1).

**Measured (sec. 14).** Each countercontrol asserts the target rule id on the named line or
sentence, not only the run's outcome (O3).

| Rule | T1' lines / sentences | H lines | Real-tree countercontrol at H |
|---|---|---|---|
| DR-1 | 0 / 0 | 61 (a 6, b 2, c 55) | a: FULL:6504 and book/glossary.md:13 ("The sixth of the framework's structural assumptions A1–A6"); b: ch09:104; c: FULL:718 |
| DR-3 | 0 / 0 | 0 in the corpus | `AGENTS.md` at H, the sentence of lines 37-39, by a control-only scan (below) |
| DR-4 | 0 / 0 | 28, including papers/Substratum.md:92 ("(A1) **Finiteness.** The configuration space $S$ is finite.") | papers/Substratum.md:92 |
| DR-5 | 0 / 0 | 1: papers/Main.md:736 ("Fourteen items, of unequal weight, and not fourteen independent physical assumptions") | papers/Main.md:736 |

**DR-3's witness (V5-D1).** No corpus blob in the repository's history matches DR-3. Its real
witness is the sentence of `AGENTS.md` at `H`, lines 37-39: "Every posit of the substratum model —
the posit ledger of `papers/Main.md`, including total finiteness (A1), linearity (A5), the lattice
and its coupling range, the form of the update and the measure selection — is a hypothesis that may
be false, not a fixed part of the framework." DR-3's count part matches "posit" and its tail matches
"including total finiteness". Ledger splice D296 (`AGENTS.md`, bytes 2332-2382 at `H`, lines 37-38)
rewrites it to "including linearity (A5)". `AGENTS.md` at T1' has no deny match at line or sentence
level.

- `AGENTS.md` is a ledgered file but lies outside the corpus that the deny profiles scan in
  production (`papers/*.md` and `book/*.md`). The production scan is not widened: other ledgered
  non-corpus files match deny rules at T1' with legitimate text (the A6 references above, Lean
  docstrings, guard pins), so a wider production scope would need its own allow rules and review.
- The control RT-DR3W exercises the witness by a **control-only scan**. The controls file names the
  input `{commit: H, path: AGENTS.md, blob: 12a9281fb88c14395b6715a3bf4b4f6b030f433c, sha256:
  d87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27}`. The control reads that blob
  from the object store, splits it with the configured splitter (sec. 6.1), and applies DR-3 alone.
  It requires exactly one matching sentence, whose span starts on line 37 and includes lines 37-38.
  Its countercontrol reads `AGENTS.md` at T1' (sha256
  59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2) the same way and requires 0
  matches.
- A control-only input is read only by the control that names it. It changes no profile's scope
  and no production result. Adding or changing a control-only input changes the controls file and
  is reviewed with it (sec. 16.2).
- No historical text is constructed for this purpose.

### 6.4.1 Rejected candidates DR-1d and DR-2 (history)

These two rules were proposed in v4 and dropped from the active set by owner decision V5-D1. They
are recorded here so that their purpose and patterns are not lost.

| Id | Purpose | Exact pattern (v4) | Forms it covered |
|---|---|---|---|
| DR-1d | a reversed ordinal: "structural" or "substratum" before "sixth/seventh" and a posit noun | `(?i)\b(?:structural\|substratum(?:'s\|’s)?)\s+(?:sixth\|seventh)\s+(?:assumption\|axiom\|posit\|premise\|condition\|property)\b` | "the substratum's sixth axiom, finiteness" (v4 V15) |
| DR-2 | an ordinal structural property, assumption or posit followed by finiteness | `(?i)\b(?:sixth\|seventh)\b[^.;]{0,40}\bstructural\s+(?:property\|assumption\|axiom\|posit\|premise\|condition)\b[^.;]{0,80}\bfinit` | "the framework's sixth structural property, finiteness of the bijection" (v4 V4) |

(The `\|` above is a table escape for `|`.)

**Why they were dropped.** Neither has a real-tree countercontrol. Neither pattern matches, at line
or sentence level, any blob of the history search below, nor any text file at `H`, `W` or T1'.
Their v4 countercontrols were single-line mutants of H lines, which are not evidence of a real
form. The absence of any match in history supports their removal. It does not prove that such a
form can never be written.

**The history search (W2).** The searched set is defined by commit trees, not by how a walk names
blobs: every blob that occurs at a top-level `papers/<name>.md` or `book/<name>.md` path in the tree
of any commit reachable from any local ref. With the 794 local refs (7857 commits) this set has
4677 distinct blobs. DR-1d, DR-2 and DR-3 match none of them, at line or sentence level. Two
cheaper walks each miss part of the set, which is why v5 and the v4 review reported different
counts; the difference is method, not refs:

- `git rev-list --all --objects -- papers book` (path-limited, 4657 blobs) omits 20 blobs. History
  simplification under a pathspec drops commits that make no corpus change relative to the parent
  it follows, so blobs that exist only in side-branch commits are never listed.
- `git rev-list --all --objects` (unrestricted, 4671 blobs, v5's figure) omits 6 blobs. It names
  each blob by the first path it meets, and these 6 are first met under a non-corpus path (for
  example `repo/papers/Main.md` or `README.md`), so a filter on the path name drops them.

The union of the two walks equals the tree-defined set exactly (4677 blobs).

**What removing them costs (measured).**

- Known retired material: there is no line or sentence in any tree or historical corpus blob that
  either rule matches, so no known retired A1 line loses a FAIL. At `E`, `H` and `W` the active
  deny set gives the same distinct line counts with or without them (95, 86, 86).
- Constructed forms: "the substratum's sixth axiom, finiteness" is REVIEW_REQUIRED through `resid`
  (a posit noun with a finiteness word). "the framework's sixth structural property, finiteness of
  the bijection" now PASSes when added: no deny rule, review profile or `resid` alternative matches
  it. The original literal item 7 does not catch it either ("sixth structural" contains neither
  "six structural" nor "sixth of"). It is listed as a residual in sec. 1 and kept as control V4
  with expected PASS, so that a change in its outcome is visible.
- The text of v4's DR-2 countercontrol (the former mutant M-DR2), "The framework's sixth
  structural property is finiteness of the substratum", now PASSes when added, alone or inside the
  glossary.md:13 line at H that the mutant edited: no deny rule, no review profile and no `resid`
  alternative matches it, and the original literal item 7 misses it too. It is listed as a residual
  in sec. 1 and kept as control V27 with expected PASS.
- The former mutant M-DR1d line (glossary.md:11 at H, edited to "The substratum's sixth axiom,")
  stays FAIL: DR-4 matches the same line.
- In sum, coverage was lost only for constructed strings: V4 and the M-DR2 text went from FAIL to
  PASS, and V15 from FAIL to REVIEW. No known retired real-tree material is affected.

### 6.5 Seed allow rules W1 and W2 (for review; not adopted)

**W1: "six structural properties" counting the bijection's properties.** At T1' the profile
`count-grep` matches 7 lines:

- `papers/SM.md:1394`
- `book/ch09-universality.md:137`
- `book/ch19-open-problems.md:198` and `:212`
- FULL lines 2554, 5270 and 5284

There is one rule per distinct sentence. The context matcher requires part of the enumerated list
or "of the bijection". For W1-b the context literal is "isotropy, sublattice structure, link
content", not the full six-item list (D8): with the whole list as one literal, a sentence with one
list word changed would stop at step 1 (REVIEW `unclassified`) instead of reaching step 4 (REVIEW
`rule-fingerprint-mismatch`, control V7c). Both outcomes are REVIEW. SM.md:1394's sentence
carries neither, so its rule sets `context_required: true` and cites SM's own definition of the six
properties. The negative matcher is: `A1`, `A1-A6`, `finit`, `assumption`, `axiom`, `of the
substratum`, for every W1 rule, unchanged.

**W1-c and its allowance (S1-D1, D1).** W1-c fingerprints the sentence of ch19:198 and its mirror
FULL:5270 at T1': "On a finite periodic quotient of $\mathbb{Z}^3$, a qualified case of A4
(Chapter 2), the notion of ... (one of the framework's six structural properties of the bijection),
isotropy is built in ..." (one sentence under splitter version 2, 404 characters). It contains
exactly one match of the negative literal `finit` ("finite periodic quotient", which describes the
lattice, the qualified A4 case, not a finiteness posit) and no match of the other five. Under v5.1
both lines were FAIL `rule-negative-match`, which contradicted the stated outcomes of RT-D, RT-I7A,
sec. 8.2 and sec. 11 note 1. The negative list is not narrowed: each of W1-c's two fingerprints
carries `negative_allowance: {"finit": 1}`, so only that exact sentence at that exact location may
contain one `finit` match, and any further match, any other text, or any other location FAILs
(controls WB1-WB12). The other W1 sentences contain no negative literal and carry no allowance.

**W2: the anomaly condition "(A1)".** The profiles `ptr` and `repo` match it at
`book/appendix-b-derivations.md:235` and `:246`, and at FULL lines 5914 and 5925. These four lines
are unchanged site lines (held for `p0-core`). The context matcher requires the source-byte literal
`\mathrm{SU}(3)` or `anomaly` (D8: the source line reads `$\mathrm{SU}(3)$`; the rendered
"SU(3)" does not occur in it).
The negative matcher is: `Finiteness`, `finit`, `posit`, `substratum`, `configuration space`. These
rules replace the first two `RESIDUAL_ALLOW` entries, the corresponding `EXPLAINED` substring
entries and the blanket `(A1)` strip.

**The fifth `ptr` hit (V2).** `ptr` matches 5 lines at T1': the 4 W2 lines and papers/GR.md:58
("For a finite total system, restrict it to a conserved energy shell ..."), which matches PTR's
`finite total system`. P explains it by its third `RESIDUAL_ALLOW` entry ("finite-scope wording of
ledger X-70") and the strip `.replace('For a finite total system', '')`. W1 and W2 do not replace
that entry, and no allow rule does. GR.md:58 is one of the 84 replacement-region hit lines, so it
is resolved by its hit classification record (sec. 8), which names the `ptr` hit as well.

### 6.6 Residual review profile `resid` (widened in v5; for independent review)

`resid` is a review profile on added text. It exists so that a lexically unanchored paraphrase of
the retired posit, which no deny rule can close, is at least REVIEW_REQUIRED when it is added. v5
widens it as the v4 review's V8 proposed (owner decision V5-D2), and adds one alternative of its own.
Its pattern is the disjunction of three parts:

- **resid-a (v4)**:
  `(?i)\b(?:configuration|state|phase)\s+spaces?\b[^.;]{0,40}\b(?:is|be|being|are|remains?)\s+(?:\w+\s+)?finite\b|\b(?:posits?|premises?|axioms?|assumptions?|hypothes[ie]s)\b[^.;]{0,60}\bfinit\w*|\bfinit\w*[^.;]{0,60}\b(?:posits?|premises?|axioms?|assumptions?|hypothes[ie]s)\b`
- **resid-b (V8, as the v4 review proposed it)**:
  `(?i)\bfinite\s+(?:\w+\s+)?set\b|\b(?:substratum|universe|world)\b[^.;]{0,40}\b(?:is|be|being|are)\s+(?:a\s+)?(?:\w+\s+)?finite\b`
- **resid-c (v5)**: `(?i)\bfinite\s+(?:number|count)\s+of\s+(?:\w+\s+)?(?:states|configurations|elements|points|sites)\b`.
  The v4 review listed "The substratum is assumed to have a finite number of states." among the
  escapes its extension catches; measured, resid-b does not match it ("is assumed to have a" puts
  more than one word between "is" and "finite"). resid-c closes it.

**Forms it is meant to catch.** Measured, `resid` matches each of: "one of the posits is that the
configuration space is finite"; "a finite set with a deterministic bijection on it"; "uses a finite
set with a deterministic bijection"; "the substratum is a finite set with a bijection on it"; "We
take the substratum to be finite."; "the universe is assumed finite"; "The substratum is assumed to
have a finite number of states."; "the substratum's sixth axiom, finiteness". The first is the v3
review's example, which `p0-core` P4 and `ptr` do not match; the next three are real H sentences
with their "under A1" qualifier deleted (ch02:212, SM.md:30, ch02:136 at H).

**Every additional match, by tree.** `resid` is evaluated only on added text (sec. 2.3), so only
added-text lines receive an outcome from it. The whole-corpus counts below are given so that the
widening's reach is visible; outside added text they produce no item.

| Tree | Whole-corpus lines matched by resid-a | Lines matched by resid-b or resid-c only | Of those, hit by no other review profile | Outcome |
|---|---|---|---|---|
| E | 141 | 75 | 41 | none: `resid` is not evaluated on `E` |
| H | 138 | 79 | 42 | none: `resid` is not evaluated on `H` |
| T1' (whole corpus) | 98 | 88 | 46 | none outside added text |
| T1', added text (287 splice-image lines) | 28 | 17 | 4 | REVIEW_REQUIRED `unclassified` for the 4 lines below |

resid-c alone matches no line at E, H or T1', and none of the 287 added-text lines.

**The 4 newly matched lines at T1' (added text, no other review profile, no deny match).** Each
receives REVIEW_REQUIRED `unclassified` until a hit classification record or allow rule resolves
it. None receives FAIL, because no deny rule matches it, and none receives PASS without a record.

| Line | Text near the match | Reading (the writer's, for the reviewer) |
|---|---|---|
| FULL:6265 | "A referee who denies that the universe as a whole is finite does not thereby reject ..." | legitimate: the universe's finiteness is denied as a premise |
| book/appendix-c-objections.md:108 | the same sentence (mirror of FULL:6265) | legitimate |
| papers/Complexity.md:206 | "uniform relabelling of a finite set of hidden configurations ..." | legitimate scope wording |
| papers/Structure.md:1010 | "... takes the substratum to be a locally finite partially-ordered set ..." (causal-set literature) | legitimate: a description of another programme |

The 13 lines that resid-a alone already matched (sec. 0.3) keep REVIEW_REQUIRED as in v4. The
other 13 of the 17 added-text lines that resid-b matches are also hit by another review profile, so
the widening adds no item for them. `resid` therefore adds 17 REVIEW lines at T1' in all, 4 more
than v4. The v4 review's design target was 4 additional lines, and this count is the same 4 lines.

Adding or widening a review profile only adds REVIEW items, so it weakens nothing. resid-b and
resid-c need the same independent review as the deny set.

***

## 7. Delegation contract `delegation.json` (schema `oi-delegation/1`)

### 7.1 Location and pinning

- The contract is one structured record in the amended plan's record directory, beside
  `ledger.json` and `edits.json`. It is frozen with the plan at `F`, and its SHA-256 is listed in
  `F`'s PREREG pin table (the sec. 26.4 mechanism) and referenced by the configuration.
- The tool reads it only as `--delegation F:path`. A hash that differs from the pin is ERROR
  `SOURCE_CHANGED`.
- It enumerates exact paths, with no globs.
- The path set must equal what the ledger implies: `tex_sources(ledger)` for TeX, and the fixed
  paths of the other classes. A changed path at `X` outside the ledger and the contract is FAIL
  `unauthorized-change`.
- Evidence not named by the frozen contract is never accepted, however and whenever it is
  supplied.

### 7.2 Rules common to every class

- **Native execution (B2).** Every delegated or native-re-execution class is executed by the tool
  itself against every tree whose delegated paths are evaluated (V7). In the integrity stage the
  tool creates a disposable full clone of the repository at exact `X` under `--out` (no `--depth`,
  no `--filter`, no alternates; the clone is refused if shallow or partial, as sec. 6.3 trust root
  point 2 states; `X`'s commit and tree ids are checked in the clone), and, when `C` differs from `X`,
  a second disposable full clone at exact `C`, checked the same way. Every class is executed and
  recorded in each clone separately, with the same independent re-derivation; a class PASSes for
  the run only if it PASSes at `X` and at `C`. Checkers run only from `F`'s blobs, written into a
  directory under `--out`, never from the clone's own copy and never in the user's repository or a
  worktree of it. This contains preserve_check's `git worktree add` (gap 6).
- The tool records, for each run, the checker's blob sha256, its exact command line, its working
  directory, its exit status, and the sha256 of each result file it wrote. It then reads the
  result file it produced itself; a result file supplied from outside the run is never evidence
  for a class that the tool can execute.
- **Independent verification of results.** The tool does not take a checker's verdict on trust. For
  each class it re-derives what it can from the clone: `sc42` compares the re-executed output bytes
  with the committed file itself; `coverage-ledger` compares each of the seven values with the
  census output it produced; `tex` checks the `% source-sha256` stamps and the path set itself, in
  addition to reading preserve_check's result. A checker result that disagrees with the tool's own
  re-derivation is FAIL `delegated-evidence-invalid`.
- **Host-run classes** (`pdf`, `ci`). The evidence is the host's run and job records, read by the
  tool from the host's REST API inside the job (sec. A.44), never a file supplied by a caller. The tool
  checks `head_sha = X`, the named workflow and jobs, and their conclusions. For `pdf` it also
  checks that the PDF comparison result names `candidate_commit` and `candidate_tree` equal to
  `X`, that it was produced by preserve_check run by this tool from `F`'s blob on PDFs built in the
  clone at `X`, and that the uploaded artifact's sha256 equals the result's.
- **No freeze, no PASS (T4).** Without `F`, every delegated class is REVIEW_REQUIRED
  `delegated-evidence-missing` and can never be PASS; a `plan` field that is null or absent is
  FAIL `delegated-evidence-invalid`.
- Where the environment cannot run the clone (a local run, sec. A.40), the class is
  REVIEW_REQUIRED `delegated-evidence-missing`. The code path and its controls (G4-G8) run in CI.
- **Evidence absent** (a run not made, or no result file): REVIEW_REQUIRED
  `delegated-evidence-missing`.
- **Evidence defective**: FAIL `delegated-evidence-invalid`. That is any of:
  - a schema other than `a1exit-checker-result-v1`;
  - `checker` other than `preserve_check.py`;
  - `plan` other than `F`;
  - `ledger_base` or `base` other than `H`;
  - `ledger_sha256` other than `F`'s ledger;
  - `candidate` other than `X`'s full 40-hex id;
  - a nonzero exit;
  - `verdict` other than `pass`;
  - a required check missing, not `pass`, or with non-empty discrepancies;
  - a checker blob that differs from `F`'s copy;
  - a result file the tool did not produce in this run, for a class it executes;
  - a disagreement between a checker's result and the tool's own re-derivation.
- A class PASSes only if every required item holds.

**preserve_check.py gaps (v2 addendum 4).** The amended plan must close gaps 1, 2, 5 and 7: record
the resolved candidate commit and tree and the checker blob, write a result on a usage error or
crash, and fail on a missing STALE id. Until it does, the contract's binding cannot hold, and the
affected classes are REVIEW_REQUIRED (missing) or FAIL (inconsistent). Gap 3 is met by the PDF
class below. Gap 4 is met by reading only the named checks' `status` and `discrepancies`
emptiness, never their text. Gap 8, the stale docstring, is corrected in the amendment.

### 7.3 Classes

| Class | Paths | How the tool verifies it |
|---|---|---|
| `tex` | the 9 TeX files of `tex_sources(ledger)`: Complexity, Computation, GR, Main, Methodology, SM, Structure, Substratum and FULL | delegated: `preserve_check.py --commit X --plan F --result-json OUT` in the clone, with the commit-mode checks "candidate against base, ledger, regenerated artifacts and plan record" and "scope assertions of amendment sec. 31" both `pass`. Native as well: each file's last line is `% source-sha256: <sha256 of X's .md>`, and the path set equals `tex_sources` |
| `pdf` | the 9 PDFs | delegated: `preserve_check.py --tree ... --pdf-compare BUILT --pdf-out OUT --plan F --result-json OUT` in the exact-head CI run on `X`. Required: `candidate_commit` and `candidate_tree` equal to `X`; a host run record (API) with `head_sha = X`, the named workflow and job, and conclusion success; the result hash equal to the uploaded artifact. Native as well: each PDF blob differs from `H`'s |
| `record-dir` | the plan's record directory | native: equals `F`'s blobs; additions only as enumerated under `execution/` |
| `sc42` | `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json` | native re-execution in the clone at `X`: contains ca3a5bb2...; `--verbose` (plain and `-O`) exits 0 and is byte-identical to the file; `--self-test` (plain and `-O`) is byte-identical to the controls file, which equals `H`'s |
| `coverage-ledger` | `verification/coverage/LEDGER.json` (a ledgered file) | native: `H` plus its splices, except the fingerprint values of the seven STALE ids; each id exactly once; each value equals `tools/proof_census.py --json` (`X`'s blob, run in the clone, exit 0); any other byte FAIL |
| `ci` | the Lean kernel, Mathlib, R7 guard, `bohr_frequency_probe.py` and `guards_check.py --mutants` jobs | delegated: host run and job records (API) for the exact-head run on `X`, each named job concluding success |

Missing evidence is never PASS.

***

## 8. Classification of hits and the review load

### 8.1 Rules

| Hit | State until classified | Resolved by |
|---|---|---|
| any profile hit in an authorized replacement image, inside or outside a site region (`new-pattern-in-replacement` when the pattern is absent from the FROM region) | REVIEW_REQUIRED | a hit classification record or an allow rule |
| a hit on an unchanged site line | PASS | the frozen classification |
| a hit in an HP region | REVIEW_REQUIRED | the HP adjudication's `hit_classifications` |
| any other unheld hit | REVIEW_REQUIRED | a record or rule |
| a deny match on a tree where deny profiles run (sec. 2.3) | FAIL | not resolvable by a record |

A hit classification record (schema `oi-hit-classification/1`) binds:

- `file` and `line_sha256`, which must be unique in the tree;
- the segment;
- the splice id or HP step;
- the profiles and patterns;
- the semantic classification (which qualification is visible, with the reason);
- `author`, under the chain of sec. 6.3.

It states that it classifies meaning, and that the splice provenance is recorded separately. A line
hit by several profiles needs one classification that names every profile hit on it.

### 8.2 Review load before the amended plan can pass as written (R5)

Counted at T1'. Each row states its profile set and carries a label of sec. 0.3. The four rows
marked "p0+ext" are disjoint from each other; the rows under other profiles may share lines with
them, as stated.

| Set | Profile set | Lines | Label |
|---|---|---|---|
| Hit lines in the 197 site replacement regions | p0+ext | 84 | IR |
| Hit lines in splices over hit lines of HP site regions | p0+ext | 16 | IR |
| New hit lines on non-site lines (D237, D238, D241, D242, D246, D247, D388) | p0+ext | 7 | IR |
| Pre-existing unheld lines identical at H | p0+ext | 93 | IR |
| `resid` hits in added text, hit by no other review profile | resid (v5) | 17 (13 by resid-a, 4 added by resid-b) | 13 IR+WR; 4 WN |
| W1 allow rules | count-grep | 7 | IR. 2 lines (FULL:5270, ch19:198) are also p0+ext hits among the 93; 2 (ch19:212, FULL:5284) lie in replacement regions but are not p0+ext hits, so they are outside the 84; 3 are hit only by `count-grep` |
| W2 allow rules | ptr, repo | 4 | IR; unchanged site lines, held for p0-core |
| The fifth `ptr` hit, papers/GR.md:58 | ptr | 1 | IR+WR; one of the 84, resolved by its record |
| HP site adjudications, with `hit_classifications` for their regions and `own_lines` for the 22 merged sites | | 113 sites | IR |
| Meaning-context adjudications (sec. 4.4) | | 12 | IR; 7 HP, 5 RET |
| Indicator adjudications (sec. 4.4) | | 10 | 7 HP (S1, D3), 3 RET (IR) |

**Totals.** Replacement-text hit lines under p0+ext: 84 + 16 + 7 = 107. Unheld or replacement p0+ext
lines in all: 107 + 93 = 200 (IR, also counted directly as 200). Distinct corpus lines that need a
classification record or rule under all review profiles: 200 + 5 (W1 lines that are not p0+ext
hits) + 4 (W2) + 17 (`resid`) = 226 (WN; the v4 total of 222, IR, had 13 `resid` lines).
Convention: 84 is used, with W1's 7 lines counted in their own row; v3's 86 came from a different
overlap test (sec. 0.3).

The `repo` profile (sec. 11 item 11) adds the following. Measured with P's own `classify()` at
T1', there are 0 unexplained lines, but 176 active lines are explained by entries that sec. 6.3
does not admit:

- 96 lines by path-wide "unrelated label" entries;
- 31 lines by path-wide "guard pins" entries;
- 14 lines by substring entries, without fingerprints (9 "unrelated label", 1 "historical record
  label", 1 "registry identifier (kept)", 3 "preserved historical evidence");
- 35 lines as "kernel identifier" (IDENT), without a rule.

The split is by the class `classify()` returns (IR+WR). v4's split (37 / 12) attributed each line by
the first `EXPLAINED` entry for its path, and so counted 23 IDENT lines in files that also carry
substring entries as substring lines.

Each needs an exact-path, fingerprinted rule or record. The 5486 lines in historical records and
the 2 lines in generated artifacts are outside the profile's scope. That scope is a reviewed scope
record (prefix lists are allowed only there), and any change to it is widening (sec. 16.2).

The HP regions' hits are among the 93 + 16. Records may therefore serve two rows of the table, but
each hit line needs exactly one classification.

Until all of the above exist, `coverage` and `terms` at T1' are REVIEW_REQUIRED at best, and FAIL
while any FAIL item of sec. 9 remains.

***

## 9. Complete list of FAIL and REVIEW conditions

### FAIL (exit 20)

Sites:

- `unauthorized-change`, `missing`, `duplicated`, `ambiguous`;
- `context-meaning-unverified`;
- `retained-changed`.

Ledgered files:

- `unauthorized-edit`;
- `unledgered-file-change`.

Historical provenance:

- `hp-unadjudicated`, `untracked-hp-overlap`;
- `provenance-mismatch`, `provenance-gap`, `provenance-foreign`, `provenance-ambiguous`;
- `adjudication-row-changed`.

Hits and rules:

- `deny-match`;
- `item7-literal-match` (the countercontrol profile only);
- `rule-negative-match`, `rule-overreach`;
- `record-invalid`;
- `stale-adjudication`;
- `final-unclassified` (only under `--final`, sec. 5).

Pins and mirrors:

- `pin-broken`, `pin-target-missing`;
- `mirror-mismatch`.

Lean:

- `lean-code-change`.

Delegation:

- `delegated-evidence-invalid`;
- an `unauthorized-change` path outside the ledger and the contract.

Tree roles:

- `candidate-parent`;
- `landing-parents`, `landing-first-parent-not-M`;
- `landing-drops-main-change`, `landing-conflict-unresolved`, `landing-extra-change`;
- `base-drift`.

Record checks:

- op A record checks not all holding.

### REVIEW_REQUIRED (exit 10)

- `unclassified`;
- `new-pattern-in-replacement`;
- `unclassified-in-replacement`;
- `rule-fingerprint-mismatch`;
- `rule-stale`;
- `context-structure-changed`;
- `delegated-evidence-missing`;
- `side-change-unclassified` (a change on `M` outside every declared class).

ERROR, VOID, USAGE and INTERNAL are as in sec. 5.

***

## 10. Test matrix

Each control runs in both directions: the mutant gives the stated outcome, and the restored tree
returns to its control outcome. Each expected FAIL names the sec. 9 class that produces it, and
each expected deny FAIL names the rule alternative that produces it (measured on the control text,
sec. 14).

### 10.1 Unit and mutation controls (synthetic, in memory)

The v2 controls U1-U15 and M1-M11 stand, with v4 classes and exit codes. Added:

| Id | Case | Expected |
|---|---|---|
| K1 | the neighbour line of a meaning-context site is negated | FAIL `context-meaning-unverified` |
| K2 | the same next to a non-required site | PASS, `context_changed: true` |
| K3 | two site paragraphs swapped | per site, as K1 and K2 |
| K4 | a site line moved to a distant section of the same file | as K1 and K2 |
| K5 | an ANAPH site ("This bound ...") whose line above is changed, s3 `visible` | FAIL `context-meaning-unverified` |
| K6 | a labelled item `*(A2) Determinism.*` whose list lead-in is changed | REVIEW_REQUIRED `context-structure-changed` |
| K7 | a table row whose header row is changed; separately, whose neighbour row is changed | REVIEW_REQUIRED `context-structure-changed` in both |
| K8 | a list item whose trailer paragraph is changed (the Substratum.md:127 shape) | REVIEW_REQUIRED `context-structure-changed` |
| K9 | a PARTIAL site, nothing else changed | PASS; `partial_quote: true`; outcome unchanged when the flag is toggled |
| B1 | an empty-image splice on a site line | `authorized-removal`; a hit at its offset is "in image" |
| B2 | a multi-line splice (33 exist in P) | `authorized-replacement` with a line range |
| B3 | a zero-length insertion at a line boundary | the overlap rule of sec. 5 |
| B4 | a last line without LF | located and spanned to end of file |
| B5 | a splice making a replacement region non-unique in `X` | FAIL `duplicated` at the next search |
| B6 | a splice touching a site's end offset only | no overlap: site `unchanged` |
| H1 | HP adjudication naming #1473 where the walk gives #1474 | FAIL `provenance-mismatch` |
| H2 | one step listed where the walk gives two | FAIL `provenance-gap` |
| H3 | a change at an unpinned commit | FAIL `provenance-foreign` |
| H4 | an adjudicated site later rewritten outside every splice | FAIL `unauthorized-change` (RET) |
| H5 | an HP site overlapped by a splice, with no adjudication | FAIL `untracked-hp-overlap`, visible in HP and RET |
| H6 | an adjudication changing a site's row | FAIL `adjudication-row-changed` |
| H7 | two adjacent sites, separated by one blank line, both changed at one E..H step, and an H..X splice inside the second only | both sites reported as HP; each carries `region_shared_with` naming the other; `region_splices` lists the splice for both; `line_splices` lists it for the second only. With an adjudication whose `own_lines` leave a line unassigned, or attribute the splice to no site: FAIL `record-invalid` |

### 10.2 Adversarial controls (each tied to its rule)

The V controls are splices adding the stated text to the stated file (added text), unless stated
otherwise.

| Id | Case | Expected | By |
|---|---|---|---|
| L1 | the W1 sentence shifted by 40 lines | PASS | W1 rule |
| L2 | the W2 lines moved | PASS | W2 rule |
| L3 | a W1 sentence copied inside scope | FAIL `rule-overreach` | `max_instances` |
| L4 | a W1 sentence copied outside scope | REVIEW_REQUIRED `unclassified` | scope |
| V1 | "The six structural properties of the substratum are listed in Chapter 2." | FAIL `deny-match` | DR-1b |
| V2 | the W1 sentence of ch19:212 edited to "six structural properties, one of which is total finiteness," (a synthetic edit; DR-3's real witness is RT-DR3W) | FAIL `deny-match` | DR-3 |
| V3 | "(A1) the substratum is finite in total" in appendix B | FAIL `deny-match` | DR-4 |
| V4 | "the framework's sixth structural property, finiteness of the bijection" | PASS (no hit) | accepted residual after DR-2 was dropped (V5-D1, sec. 6.4.1); the original item 7 misses it too. Kept so that a change in its outcome is visible |
| V27 | "The framework's sixth structural property is finiteness of the substratum" (the text of v4's former DR-2 countercontrol), added alone and as the edited glossary.md:13 line | PASS (no hit) in both | accepted residual after DR-2 was dropped (V5-D1, sec. 6.4.1); the original item 7 misses it too. Kept so that a change in its outcome is visible |
| V5 | "**(A1) Finiteness.** The configuration space is finite." in appendix B | FAIL `deny-match` | DR-4 (case-insensitive; matched within the label) |
| V6 | "the six structural properties of the substratum, including finiteness" | FAIL `deny-match` | DR-1b and DR-3 |
| V7a | V2 with DR-3 removed from the profile set. Precondition: the text is an edit of a sentence fingerprinted by a W1 rule, inside that rule's scope | FAIL `rule-negative-match` | W1's negative matcher (`finit`): shows DR-3 is the operative deny rule |
| V7b | V2's text placed in a file outside every W1 rule's scope, DR-3 removed | REVIEW_REQUIRED `unclassified` | p0-core and `count-grep` hits with no rule |
| V7c | a W1 sentence edited with no negative literal (one word of the enumerated list changed) | REVIEW_REQUIRED `rule-fingerprint-mismatch` | sec. 6.2 step 4 |
| V9 | "Six structural assumptions define the substratum." | FAIL `deny-match` | DR-1a |
| V10 | "the six structural conditions on the substratum" | FAIL `deny-match` | DR-1a |
| V11 | "six structural premises of the framework" | FAIL `deny-match` | DR-1a |
| V12 | "the six substratum posits" | FAIL `deny-match` | DR-1a |
| V13 | "the structural assumptions A1 through A6" | FAIL `deny-match` | DR-1c |
| V14 | "A1--A6"; "A1—A6"; "(A1)–(A6)"; "A1, ..., A6" (four cases) | FAIL `deny-match` each | DR-1c |
| V15 | "the substratum's sixth axiom, finiteness" | REVIEW_REQUIRED `unclassified` | `resid` (resid-a), after DR-1d was dropped (V5-D1) |
| V16 | "posit A1 (finiteness) holds" | FAIL `deny-match` | DR-4 |
| V17 | "A1 (Finiteness): the configuration space is finite" | FAIL `deny-match` | DR-4 |
| V18 | "(A1) Finiteness. The configuration space S is finite." | FAIL `deny-match` | DR-4 |
| V19 | "The posit ledger has 14 items." | FAIL `deny-match` | DR-5 |
| V20 | "the six structural properties of the bijection, the first being finiteness of S" | FAIL `deny-match` | DR-3 |
| V21 | "one of the posits is that the configuration space is finite" | REVIEW_REQUIRED `unclassified` | `resid` only; residual limit (sec. 1): no deny rule |
| V22 | papers/Main.md:736's H sentence ("Fourteen items, ...") reinstated at a T1'-style `X` | FAIL `deny-match` | DR-5 (the original item 7 fails it too) |
| N-W | every W1 and W2 line at T1', and papers/Main.md:738 ("Thirteen items") | no deny match | negative examples |
| V23 | ch02-substratum.md:136 at H ("... the substratum is a set (finite under A1) with a bijection ...") reinstated at a T1'-style `X`; run as item 7 (`terms --check item7 --final`) | FAIL `final-unclassified` (`ptr` hit; no deny rule matches) | sec. 5, 11 note 1 (V3) |
| V24 | "six structural hypotheses" added; run as item 7 with `--final` | FAIL `final-unclassified` (`count-grep` hit; no deny rule matches) | V3 |
| V25 | the other direction: V23 and V24 without `--final` give REVIEW_REQUIRED `unclassified`; a W2 line with its rule under item 7 with `--final` gives PASS; a `resid`-only hit (V21) under item 7 with `--final` stays REVIEW_REQUIRED, since `resid` is not in item 7's `final_profiles` | as stated | sec. 5 |
| V26 | added, one at a time: "a finite set with a deterministic bijection on it"; "the substratum is a finite set with a bijection on it"; "We take the substratum to be finite."; "the universe is assumed finite"; "The substratum is assumed to have a finite number of states." | REVIEW_REQUIRED `unclassified` each | `resid` (resid-b, resid-b, resid-b, resid-b, resid-c) |
| A1r | rule scope widened to `book/` | FAIL `record-invalid` | sec. 6.3 |
| A2r | literal shortened to `(A1)` | FAIL `record-invalid` | widening |
| A3r | fingerprint swapped, count unchanged, no widening review | FAIL `record-invalid` | widening: any fingerprint change |
| A4r | widening review signed by the rule's author | FAIL `record-invalid` | reviewer is not the author |
| A5r | allow rule fingerprinting a sentence that a deny rule matches | FAIL `deny-match` | deny precedence (sec. 6.2 step 2) |
| A6r | literal not covering the trigger | FAIL `record-invalid` | trigger definition |
| A7r | reused rule id | FAIL `record-invalid` | id rule |
| A8r | allow rule with no negative example | FAIL `record-invalid` | examples |
| A9r | rule widened by one alternation | FAIL `record-invalid`, and caught by its own negative example | widening and examples |
| A10r | deny rule narrowed in scope | FAIL `record-invalid` | deny widening |
| A11r | deny rule whose countercontrol no longer matches | FAIL `record-invalid` | sec. 6.3 examples and countercontrols |
| S1r | a fingerprinted sentence edited | REVIEW_REQUIRED `rule-fingerprint-mismatch` | sec. 6.2 |
| S2r | a fingerprinted sentence deleted | REVIEW_REQUIRED `rule-stale` | |
| N1 | a PIN_OK entry dated after `F` | FAIL `pin-broken` | sec. 6.3 |
| N2 | a reconciliation record that changes a decision on `X` | FAIL `record-invalid` | sec. 13.3 |
| O1 | a record whose review record has `reviewer` equal to its `author` | FAIL `record-invalid` | sec. 6.3 |
| O2 | a review record naming another blob of the same path | FAIL `record-invalid` | binding to the reviewed blob |
| O3 | a review whose `verdicts` omit one item id | FAIL `record-invalid` | coverage of every item |
| O4 | an owner authorization naming the record's path without a hash | FAIL `record-invalid` | hash binding |
| O5 | a `reviewer` field holding a CI run URL; separately, an `owner` comment id pointing to an Issue | FAIL `record-invalid` | no role inferred from a tool result |
| O6 | a record edited in place after `F` (blob differs from the configuration's reference) | ERROR `SOURCE_CHANGED` | sec. 6.3, 16.2 |
| O7 | a superseding record with no new review or authorization | FAIL `record-invalid` | corrections |
| O8 | a record added after `F` and used for a decision on `X` | FAIL `record-invalid` | sec. 13.3 |
| O9 | a complete chain (record, review, authorization, configuration reference) | the record is admitted | positive control |
| G1 | delegated result whose `candidate` is an abbreviation | FAIL `delegated-evidence-invalid` | sec. 7.2 |
| G2 | no delegated result supplied | REVIEW_REQUIRED `delegated-evidence-missing` | sec. 7.2 |
| G3 | LEDGER.json with one STALE id removed | FAIL | sec. 7.3 |
| X1 | `record --pin H` | ERROR `PIN_MISMATCH`, exit 65 | sec. 5 |
| X2 | an exception injected in classification | INTERNAL, exit 71 | sec. 5 |
| X3 | an unknown flag | exit 64, stderr JSON, nothing written | sec. 5 |
| X4 | `--help` | exit 64 | sec. 5 |
| X5 | a missing required argument | exit 64, never 2 | sec. 5 |
| X6 | a run whose outcome is REVIEW_REQUIRED | exit 10, distinct from X3-X5 and from FAIL | sec. 5 |
| X7 | the tool run with a deliberately broken import in its package (a module raising `ImportError` at import time, before the wrapper's own imports complete) | a nonzero exit distinct from 20 (the interpreter's 1, or 71 if the wrapper caught it); no `result.json` with outcome PASS; the consumer's acceptance predicate reports non-acceptance | sec. 5 |
| X8 | the interpreter pointed at a missing script path | exit 2 from the interpreter; non-acceptance | sec. 5, unlisted codes |
| X9 | an unexplained `repo` hit run as item 11: without `--final`; with `--final`; a REVIEW item of a profile outside item 11's `final_profiles` with `--final`; and `--final` without `--check` | REVIEW exit 10; FAIL `final-unclassified` exit 20; that other item stays REVIEW; USAGE exit 64 | sec. 5 |
| X10 | exit 0 with a `result.json` whose outcome was edited to FAIL; exit 0 with an engine blob hash differing from the pin | non-acceptance in both | acceptance predicate |

### 10.3 Real-tree controls (CI)

The rules are preregistered. The counts are references (sec. 0.3).

| Id | Run | Rule | Reference |
|---|---|---|---|
| RT-A | `record --pin E --record H` | PASS | frozen replay: 0 errors; 697 anchors |
| RT-E | `coverage --commit E` | PASS (deny profiles not evaluated on `E`, sec. 2.3) | 697 unchanged |
| RT-H0 | `coverage --commit H`, no HP records | FAIL; every FAIL and indicator item has obligation HP | 113 `hp-unadjudicated`; 7 HP `context-meaning-unverified`; 7 HP `context-structure-changed` (FULL:706, FULL:708, ch02:76, ch02:78, Substratum.md:94, :253, Main.md:741) |
| RT-T0 | `coverage` at `X = T1'`, no records | FAIL. HP: 113 `hp-unadjudicated`, 7 context FAILs, 7 structure REVIEWs (as RT-H0). RET: 19 `untracked-hp-overlap` (region-attributed; 18 line-attributed), 5 `context-meaning-unverified`, 3 `context-structure-changed`. Deny: 0. REVIEW: sec. 8.2 | 383 unchanged (168 moved), 197 replaced, 4 removed; 215 region lines; 9 region-merger groups covering 22 sites, each site carrying `region_shared_with`; only Substratum.md 266/268 overlapped by a splice (D029) |
| RT-T | RT-T0 with all reviewed records of sec. 8.2 | PASS only when every record verifies under sec. 6.3; any missing record leaves REVIEW_REQUIRED or FAIL. Reported `NOT RUN` while no reviewed record exists (sec. 10.4) | |
| RT-C | `execution` at `X = T1'` with `F` = the amended freeze | candidate checks as sec. 11; PASS only with contract evidence | 399 splices verified at H; 23 corpus and 21 other ledgered files conform, except LEDGER.json under the `coverage-ledger` class |
| RT-D | `terms --commit T1' --base H --ledger F:ledger.json` | 0 deny matches; all 7 W1 lines (W1-c with its allowance) and the 4 W2 lines PASS with their rules, else REVIEW; GR.md:58 PASS with its record, else REVIEW; 45 `resid` lines REVIEW until classified, 17 of them hit by no other review profile (D5) | |
| RT-DR | `terms --commit H --profile DR-1,DR-3,DR-4,DR-5` | FAIL `deny-match`; the item for each named countercontrol line of sec. 6.4 carries the target rule id (DR-1a on FULL:6504 and glossary.md:13, DR-1b on ch09:104, DR-1c on FULL:718, DR-4 on Substratum.md:92, DR-5 on Main.md:736), checked by id, not by the run's outcome (O3); the same profiles at T1' match 0 lines and 0 sentences | at H: DR-1 61 lines (a 6, b 2, c 55), DR-3 0, DR-4 28, DR-5 1, 86 distinct lines; at E: 95 |
| RT-DR3W | control-only scan of `AGENTS.md` at H (blob 12a9281f..., sha256 d87acac5...) with DR-3 alone (sec. 6.4); countercontrol: `AGENTS.md` at T1' (sha256 59b68984...) | exactly one DR-3 sentence at H, starting on line 37 and including lines 37-38 (the lines splice D296 rewrites); 0 at T1' | |
| RT-I7 | `terms --commit T1' --profile item7-literal`; the same at H | FAIL `item7-literal-match` at both | T1': exactly 7 "six structural" lines (SM.md:1394, ch09:137, ch19:198 and 212, FULL:2554, 5270 and 5284), 0 "Fourteen", 0 "sixth of"; `\bA1\b` 4 (the W2 lines). H: 11 / 1 / 2; `\bA1\b` 179 |
| RT-I7A | the proposed item-7 amendment check (sec. 11 note 1) at H and at T1', no records | FAIL at both. Every one of the 95 retired lines of sec. 0.3 is FAIL (`final-unclassified`), none only REVIEW | H: 86 `deny-match` lines and 123 `final-unclassified` lines (209 FAIL lines), counting line-level deny matches only; with every line of a matching multi-line sentence counted, 93 and 216, the 123 unchanged (O8). T1': 0 deny lines; 12 `final-unclassified` lines (the 7 W1 lines, the 4 W2 lines, GR.md:58), which become PASS once W1 (with W1-c's allowance), W2 and GR.md:58's record exist |
| SW1 | per-site sweep at E: each of the 697 sites, one token deleted | exactly one FAIL naming that site, and exactly one new FAIL against the unmutated tree | |
| SW2 | per-site sweep at H: each of the 584 sites, one token deleted (segments E..H `hp`, H..X unledgered) | for each site, exactly one new FAIL naming it, of obligation RET, class `unauthorized-change`, segment H..X; the items naming it at the unmutated H (all of obligation HP, segment E..H) unchanged; items compared by `(obligation, class, segment, fingerprint)` (D2). Holds for 584 of 584. Once the 7 E..H context adjudications exist, "exactly one FAIL naming that site" holds as well; the 7 structure REVIEWs are REVIEW items and do not affect it | 14 sites carry HP items at the unmutated H (V6): the 7 E..H meaning-context FAILs of sec. 4.4 (FULL:4895, 4905, 4919; ch18:164, 174, 188; Main.md:332) and the 7 E..H structure REVIEWs (FULL:706, 708; ch02:76, 78; Main.md:741; Substratum.md:94, 253). The v5.2 review ran SW2 with the Stage 1 engine under the tuple predicate: 584 of 584 |

***

### 10.4 Control reporting and new controls (B1-B6, S1-D1)

**Reporting (B6).** Every control run writes one record per control with `id`, `expected` (the
stated expectation of this document, verbatim), `predicate` (a machine-checkable form of exactly
that expectation), `actual`, and `status`, one of:

- `PASS`: the control ran and its predicate held;
- `FAIL`: the control ran and its predicate did not hold;
- `SKIP`: the control was deliberately not run in this environment, with the reason (for example a
  clone-at-`X` class outside CI, sec. A.40);
- `NOT RUN`: the control could not run because an input does not exist (for example RT-T, which
  needs reviewed records).

A summary counts each status separately and never reports `SKIP` or `NOT RUN` as met. A control's
predicate must test its whole stated expectation: every outcome, class and count it names, in every
direction it names. A predicate weaker than its expectation is a defect of the control. In
particular: RT-T is `NOT RUN` until reviewed records exist; RT-D tests the states of all 7 W1 lines,
the 4 W2 lines and GR.md:58 and the `resid` count; A1r-A11r run the mutated rule through the
pipeline and require an emitted FAIL `record-invalid` (not a truthy lint result); the sweeps compare
items by `(obligation, class, segment, fingerprint)`; each control that this document states in
both directions asserts both. A control-harness result is a control artefact. It is written as
`control-result.json` with a top-level `"harness": true` and `config.admission:
"control-harness"`, never as `result.json`, and the acceptance predicate rejects it (X11).

**New and changed controls.**

| Id | Case | Expected | By |
|---|---|---|---|
| WB1 | the W1-c sentence at T1' in ch19:198 and FULL:5270, with the W1-c fingerprints and `negative_allowance: {finit: 1}` | PASS, both lines | sec. 6.2 step 3 (S1-D1) |
| WB2 | the same sentence at the same location with one more word containing `finit` (for example a second "finite" inserted elsewhere in the sentence) | FAIL `rule-negative-match` (2 matches, allowance 1) | step 3 |
| WB3 | the approved sentence copied, unchanged, to another paragraph of a file in W1-c's scope | FAIL `rule-negative-match` at the copy (its context differs, so no allowance); the original still PASS | step 3: no reuse in other locations |
| WB4 | the approved sentence copied to a file outside every W1 rule's scope | REVIEW_REQUIRED `unclassified` (no rule applies; step 1) | scope |
| WB5 | the approved sentence moved (cut and pasted) to another paragraph of the same file | FAIL `rule-negative-match` at the new location; REVIEW_REQUIRED `rule-stale` for the fingerprint | step 3; `rule-stale` |
| WB6 | a near-copy at the approved location with one other word changed, keeping one `finit` word | FAIL `rule-negative-match` (sentence sha differs, so no allowance) | step 3: tied to the exact text |
| WB7 | the approved sentence with its one `finit` word removed | REVIEW_REQUIRED `rule-fingerprint-mismatch` (no negative match; step 4) | step 4 |
| WB8 | the approved sentence and its neighbours shifted by 40 lines (as L1) | PASS | context-bound, not line-bound |
| WB9 | two fingerprints' sentences made identical in one file, so that one allowance is claimed twice | the claim at the larger byte offset gets no allowance: FAIL `rule-negative-match` | one grant per fingerprint |
| WB10 | lint: a W1-c rule whose allowance is 2, or 0, or names `axiom` (absent from the sentence) | FAIL `record-invalid` | sec. 6.3 (allowance equals the exact count) |
| WB11 | lint: a rule whose fingerprinted sentence fails its own rule (v5.1's W1-c, with no allowance) | FAIL `record-invalid` | sec. 6.3 self-PASS clause |
| WB12 | V7a on the W1-c sentence ("..., one of which is total finiteness,") | FAIL `rule-negative-match` | step 3 |
| WB13 | the approved sentence moved together with both of its neighbours (the three sentences, unchanged) to another section of the same file | PASS: the context, which defines the location, is unchanged | sec. 6.2, V5 |
| WB14 | the approved sentence with both neighbours duplicated in the same file, so that two copies satisfy step 3 | the copy at the smaller byte offset PASSes; the later copy FAILs `rule-negative-match`, on every run | sec. 6.2, V5 |
| WB15 | "Finiteness" (capitalized) added to a W1 sentence at its approved location | FAIL `rule-negative-match` (case-insensitive negatives) | sec. 6.2, O1 |
| X11 | a control-harness PASS result of RT-E, presented with the pinned engine and configuration hashes | non-acceptance (`admission` is not `"chain"`); the harness never writes `result.json` | sec. 5 (B1) |
| TR1 | a run without `--freeze` | ERROR `CONFIG_UNREVIEWED`, exit 65 | sec. 6.3 |
| TR2 | a configuration whose sha256 is not in `F`'s pin table, with a matching `--config-sha256` | ERROR `CONFIG_UNREVIEWED` | point 6 |
| TR3 | a review record and authorization placed beside the configuration, naming its blob, but not in `F`'s pin table | ERROR `CONFIG_UNREVIEWED` | point 6 |
| TR4 | `retirement.owner` differing from `A.owner.id` | ERROR `CONFIG_UNREVIEWED` | point 7 |
| TR5 | a complete chain: `A` admitted; the pinned workflow in repository 1156244443; one unedited owner designation of `F` in the authorized thread; `F`'s pin table listing the configuration, its review and authorization | `config.admission: "chain"` with every field of sec. 6.3 recorded | positive control (CI only) |
| TR6 | a designation record inside `F`'s tree, with no designation comment on the host | ERROR (missing designation) | point 5 |
| TR7 | a designation comment by another account | ERROR (not the owner's id) | point 3 |
| TR8 | an owner designation comment naming a different commit | ERROR (`F` not designated) | point 5 |
| TR9 | caller-supplied overrides, one at a time: of the owner id, the repository id, the designation forms, the thread, the workflow path, the workflow hash (each by a command-line option, an environment value, a retirement-configuration field and a record in `F`) | each ignored or refused; never `"chain"` on the overridden value; an unknown configuration field is ERROR `CONFIG_INVALID` | sec. 6.3 |
| TR10 | a caller-built `F` whose pin table lists its own configuration and review files, with no owner designation | ERROR | points 5, 6 |
| TR11 | the owner's designation comment edited after creation; separately, edited and then restored to the original text | ERROR in both, permanently: a new designation comment is needed (A-D2) | point 3 |
| TR12 | a later owner supersession of `F` by another commit, placed on the first page of the thread; separately, beyond the first page | ERROR for `F` in both; the thread is read to its end | points 2, 5 |
| TR13 | a local run with a complete chain on paper | no `"chain"` admission; never acceptable | point 9 |
| TR14 | the same workflow and tool run in a fork, or in another repository, with a designation there by that repository's owner | ERROR (repository id differs, or fork) at the tool; non-acceptance at the consumer | point 1; sec. 5 |
| TR15 | a run from a workflow at `A.workflow.path` whose content differs from the pinned hash; separately, a same-named workflow at another path | ERROR at the tool; non-acceptance at the consumer | point 1; sec. 5 |
| TR16 | an owner designation in a thread other than the plan's authorized thread | ERROR (no designation in the authorized thread) | point 2 |
| TR17 | an owner comment quoting `F` in another wording (for example "do not merge <F>"); separately, a near form (`oi-freeze/1 designate plan=<id> commit=<F>`, without the round) | the first does not count, so ERROR for a missing designation; the second refuses as ambiguous | point 3 |
| TR18 | an explicit owner withdrawal of `F` after its designation | ERROR (`F` withdrawn) | point 5 |
| TR19 | the designation comment deleted; separately, hidden or minimized | ERROR in both (deleted: missing; hidden: unverifiable) | points 3, 5 |
| TR20 | a designation by an account with the owner's login but another numeric id (for example after a rename) | ERROR (wrong author id) | point 3 |
| TR21 | the host API unavailable, a page request failing, or a comment count mismatch | ERROR, never a fallback | points 2, 9 |
| TR22 | two live designations of different commits for one round | ERROR (conflict) | point 5 |
| TR23 | `F`'s tree carrying a copy of `A` that differs from the admitted `A`; separately, a change to `A` on `main` merged by an account other than the owner | ERROR in both | sec. 6.3 (`A`) |
| TR24 | a caller-supplied authority configuration (a file, a path argument, an environment value naming one) | never read as `A`; `A` is read from `main` of the attested repository only; a run that cannot do so is ERROR | sec. 6.3, trust root |
| TR25 | `A` taken from another ref (a branch, a tag, `F`'s tree) or another repository | refused: only `main` of the attested repository, at the head id the host's REST API reports, read from the verified store of point 2 | trust root point 2 (HS-1) |
| TR26 | `A` on `main` changed after the commit `F` descends from, by a merge without its review record and owner authorization; separately, the same change with them | the first: ERROR; the second: admitted under `main`'s `A`, with both blobs and the merges recorded | changes between `F` and execution |
| TR27 | `F` based on a `main` commit that does not yet contain `A` | ERROR | bootstrap order |
| TR28 | the pinned workflow at a `head_sha` whose tool blobs differ from `A.engine_pins` (or carry an extra file under `tools/ledger_coverage/`) | ERROR at the tool; non-acceptance at the consumer, which reads the blobs itself | sec. 6.3 trust root point 3 (V3) |
| TR29 | a run whose `head_sha` is not on `main`'s first-parent chain (a branch); separately, a run whose `head_sha` is the evaluated commit `X` | ERROR / non-acceptance in both | point 3 (V2) |
| TR30 | a result whose evaluated commits differ from the landing record's | non-acceptance | sec. 5 (V2) |
| TR31 | a withdrawal of `F` committed in the freeze ledger, whose comment is later deleted; separately, hidden; separately, edited | `F` stays withdrawn in all three, and the edited case also refuses under point 3; never reactivated | freeze ledger (V4, R-D2) |
| TR32 | a supersession committed in an earlier acceptance snapshot, whose comment is later deleted | the supersession binds; the earlier `F` stays superseded | freeze ledger |
| TR33 | a withdrawal edited into a comment without a form | ERROR (an owner comment's edit history contained a form) | point 3 (V4) |
| TR34 | an old owner comment edited into a designation | ERROR (an owner comment carrying a form has an edit) | point 3 (V4) |
| TR35 | a withdrawal posted and deleted before any admission observed it, on a host that reports no deletion events | not detected: the stated residual (sec. 6.3); the control documents the residual and does not claim a refusal. On a host that reports deletions: ERROR | residual |
| TR36 | the freeze ledger missing, unverifiable, or conflicting with the thread | ERROR | freeze ledger |
| TR37 | a designation whose first line ends in CRLF | recognized (one trailing CR removed) | forms (V5) |
| TR38 | a designation whose first line has a trailing space, or a doubled space, or an uppercase hex id | ERROR (malformed form) | forms (V5, C2) |
| TR39 | `oi-freeze/2 designate ...` (unknown version); separately, keys in another order | ERROR | forms (C2) |
| TR40 | an `A` change merged by the owner's account with no approval comment | ERROR (C1) | authority changes |
| TR41 | an approval comment quoting another blob hash, or created after the merge | ERROR | authority changes |
| TR42 | an approval comment edited | ERROR | authority changes |
| TR43 | an approval by another numeric id | ERROR | authority changes |
| TR44 | an owner-id change approved only by the old id | ERROR (the new id must approve too) | authority changes |
| TR45 | the offline replay of an accepted result from its committed snapshot: an op-B result; and an op-C result whose delegated classes (`tex`, `pdf`, `record-dir`, `sc42`, `coverage-ledger`, `ci`) are taken from the snapshot's delegated evidence, with no host call, clone, PDF build or checker run | output equal to the committed result except `config.admission.mode = "replay"`, for both; never acceptable as a new run; a snapshot whose recorded result file does not hash to its recorded sha256, or lacks the evidence for a class the result decided, makes the replay refuse | sec. 5 (C3, F2) |
| TR46 | a committed compressed result whose uncompressed sha256 differs from the recorded one | refused at landing | sec. 5 (C3) |
| TR47 | an acceptance landing that appends observed events to the freeze ledger, each case separately: with no `oi-freeze-ledger/1 append` comment; with one quoting other ledger hashes; one by another numeric id (even with the owner's login); one edited, or hidden; one outside the plan's thread; one created after the merge; a malformed or unknown-version `oi-freeze-ledger/` line | the append is refused and the landing does not merge, in every case; a ledger on `main` carrying such an append makes later admissions refuse | sec. 6.3, freeze ledger (N3) |
| TR48 | a valid `head_sha` whose `tools/ledger_coverage/` holds exactly the files of `A.engine_pins`, the approved authority record at `tools/ledger_coverage/authority.json` (blob equal to the admitted `A`) and, if `A.workflow.path` lies there, the approved workflow | accepted: execution identity holds (positive control) | sec. 6.3 point 3 (K7) |
| TR49 | the authority record at `head_sha` modified (one byte changed) | ERROR at the tool; non-acceptance at the consumer | K7 |
| TR50 | the workflow at `A.workflow.path` at `head_sha` modified (one byte changed) | ERROR (content hash differs from `A.workflow.content_sha256`); non-acceptance | K7 |
| TR51 | a substituted file at either permitted path: different content; separately, a symlink or a submodule entry at that path | ERROR in each case; non-acceptance | K7 |
| TR52 | an additional file under `tools/ledger_coverage/` that `A.engine_pins` does not name and that is neither permitted file | ERROR; non-acceptance | K7 |
| TR53 | a second, byte-identical copy of the authority record at another path in `tools/ledger_coverage/` (for example `tools/ledger_coverage/authority-copy.json`) | ERROR; non-acceptance | K7 |
| TR54 | (review probe D1) owner 4242 designates `F`; an owner change 4242 -> 5555 merges; no later designation. Separately, 5555 then designates `F` | the first: ERROR (missing designation; the former owner's designation does not count); the second: `F` is the one designated commit at point 5 (control harness); in a full chain, ERROR `CONFIG_UNREVIEWED` at point 7, since `F`'s configuration authorization predates the owner change and `F` must be re-frozen | Owner at creation (DI-1) |
| TR55 | (D2) 4242 designates and then withdraws `F`, the withdrawal not in the freeze ledger; 4242 -> 5555; 5555 designates `F` | ERROR (designation of a withdrawn commit: the withdrawal, an owner comment at its creation, binds after the owner change) | DI-1 |
| TR56 | (D3) 5555 designates `F` while 4242 is the owner; then 4242 -> 5555; no later designation | ERROR (missing designation: the comment is not an owner comment) | DI-1 |
| TR57 | (L5) a freeze-ledger change whose `oi-authority/1 approve` and `oi-freeze-ledger/1 append` comments 4242 created before 4242 -> 5555 -> 4242, merged after the change back; each ledger route separately | the change is refused (an owner change merged between the approvals' creation and the merge): an acceptance landing carrying it does not merge, and a ledger on `main` carrying it makes every later admission refuse | DI-1 |
| TR58 | (L6) 5555 creates both approval comments of a freeze-ledger change while 4242 is the owner; 4242 -> 5555; the change merged under 5555; each ledger route separately | refused as in TR57 (the approvals are not owner comments) | DI-1 |
| TR59 | 4242 designates `F`; 4242 -> 5555 -> 4242; no later designation | ERROR (missing designation: an owner change merged between the designation's creation and the admission) | DI-1 |
| TR60 | (positive) a freeze-ledger append approved by 4242 and merged while 4242 is the owner; later an owner change 4242 -> 5555 approved by both ids; 5555 designates an `F` whose configuration authorization 5555 made after the change | the earlier append and the authority chain verify (completed actions); `F` admitted | DI-1 |
| TR61 | 4242 designates `F` and then supersedes it by `F2` in the thread, not in the ledger; 4242 -> 5555. Separately, 5555 then designates `F2` | admission of `F`: ERROR (`F` withdrawn) in both; admission of `F2`: ERROR (missing designation) in the first; in the second, `F2` is the one designated commit at point 5 (control harness), and in a full chain ERROR `CONFIG_UNREVIEWED` at point 7 as in TR54 | DI-1 |
| TR62 | an owner-id change 4242 -> 5555 approved by 4242 and by 5555, both created before the merge; separately, 5555's approval created after the merge | the first: the change verifies (5555's approval is authenticated as the id the new `A` pins); the second: ERROR | DI-1; authority changes |
| TR63 | an `A` on `main` whose `supersedes` names a blob other than the version of `A` preceding it on `main`'s first-parent chain; separately, names null while a version precedes it | ERROR `CONFIG_UNREVIEWED` in both | DI-2 (`A`) |
| TR64 | (positive) a freeze-ledger change whose approvals 4242 created before a merged change of `A` that keeps `owner.id` 4242 (for example a changed engine pin), merged after it | the approvals count (no owner change); the change verifies | DI-1 |
| TR65 | (authorization analogue of D3 and L5) an authorization record whose `time` falls while 4242 is owner and whose `owner` is 5555; 4242 -> 5555; 5555 designates `F`, whose configuration uses it. Separately, 4242's authorization with `time` before 4242 -> 5555 -> 4242. Separately (positive), 5555's authorization with `time` after 4242 -> 5555 | the first two: ERROR `CONFIG_UNREVIEWED` for the configuration's authorization, FAIL `record-invalid` for any other record's; the third: admitted | DI-1 |
| TR66 | 4242 designates `F`; 5555 posts `oi-freeze/1 withdraw` of `F` while 4242 is the owner; 4242 -> 5555; 5555 designates `F` (control harness). Separately, the withdrawal posted by 4242 before the change | the first: `F` is the one designated commit at point 5 (the withdrawal is not an owner comment and is not processed); the second: ERROR (designation of a withdrawn commit) | DI-1 |
| TR67 | a comment without a form, created by 4242 while owner; 4242 -> 5555; the comment then edited by 4242 into a first line beginning `oi-freeze/`. Separately, the same comment left unedited | the first: ERROR (point 3); the second: no refusal from point 3 or 4 | DI-1, point 3 |
| TR68 | V1 (owner 4242) -> V2 (owner 5555) is an owner change. Each case separately, with every other approval and review in it valid, so that each case isolates one defect: an `A` change V2 -> V3 keeping 5555, whose previous-id approval (`from=<sha256 of V2>`) 5555 created while V1 was in force; an `A` change V3 -> V4 after V2 -> V3 (5555 -> 4242), whose previous-id approval 4242 created while V1 was in force; an owner-id change V2 -> V3 (5555 -> 6666), whose new-id approval 6666 created before V1 -> V2 merged | ERROR in each case: the change does not take effect, and every later admission refuses | DI-1; authority changes |
| TR69 | 5555 designates `F` while 4242 is the owner; 4242 -> 5555; 5555 withdraws `F`; 5555 then designates `F'` | ERROR (a withdrawal naming a commit never designated: the designation was not an owner comment at its creation); admission of `F'`: ERROR | DI-1, point 5 |
| TR70 | 4242 designates `F`; 5555 posts `oi-freeze/1 supersede` of `F` by `F2` while 4242 is the owner; 4242 -> 5555; 5555 designates `F` (control harness) | `F` is the one designated commit at point 5 (the supersession is not an owner comment; neither half is processed) | DI-1, point 5 |
| TR71 | a replace ref (`refs/replace/`) in the store that substitutes, for a commit of `main`'s first-parent chain, a commit without its change to `A`; separately, one that substitutes `A`'s blob at `head_sha` | ignored: the versions of `A`, their bytes and the admission equal those read from the same store without the replace ref, in both directions | trust root point 2 (HS-4) |
| TR72 | a graft file that makes a commit of the chain parentless, so that a traversal command stops before an earlier change to `A` | ignored: the result equals that without the graft file | point 2 (HS-4) |
| TR73 | a commit-graph file recording false parents for a commit of the chain | ignored: the result equals that without the commit-graph file | point 2 (HS-4) |
| TR74 | a shallow store (a clone with `--depth`); separately, a store holding a `shallow` file in which every needed object is present | ERROR `CONFIG_UNREVIEWED` in both (refused by its marker) | point 2 (HS-4) |
| TR75 | a partial store (`--filter=blob:none`, a promisor remote); separately, a partial store in which every needed object has already been fetched | ERROR `CONFIG_UNREVIEWED` in both; no object is fetched on demand | point 2 (HS-4) |
| TR76 | a loose object whose stored content does not hash to its id, each case separately: a blob of `A`, a tree of a chain commit, a commit of the chain, a tool blob at `head_sha` | ERROR `CONFIG_UNREVIEWED` in each case, although `git cat-file -p` prints the content | point 2 (HS-1) |
| TR77 | the chain does not reach a root: the first parent of a chain commit removed from the store, with no `shallow` file; separately, `main`'s anchor absent from the store; separately, `head_sha` absent | ERROR `CONFIG_UNREVIEWED` in each case | point 2 (HS-1, HS-4) |
| TR78 | an owner comment whose GraphQL edit history holds a revision with `diff: null`; separately, with no `diff` field; separately, with `deletedAt` set; in each case with every other revision free of forms, on a comment carrying a form and, separately, on one carrying none | ERROR in every case: the edit status cannot be read; the revision is never skipped | admission point 3 (HS-3) |
| TR79 | an owner comment whose `userContentEdits.totalCount` exceeds the number of revisions returned; separately, more than 100 revisions; separately, on a comment carrying no form, `lastEditedAt` set with `totalCount` 0; separately, `updated_at` different from `created_at` with `totalCount` 0 | ERROR in every case | point 3 (HS-3; B2, N2) |
| TR80 | the GraphQL edit-history read, each case separately: the request fails; an `errors` entry beside the data; a rate-limit response; a requested node null or missing; a node returned twice or carrying another node id; a node that is not an issue comment; `lastEditedAt` or `userContentEdits` absent | ERROR in every case; no fallback to REST | point 3 (HS-3) |
| TR81 | an owner comment whose REST `minimized` is an object; separately, absent; separately, `true`, a string or another non-null value that is not an object | ERROR in each case: hidden in the first, unreadable in the others; only `null` reads as not hidden | point 3 (HS-2) |
| TR82 | an owner designation for which GraphQL reports `lastEditedAt` null and `totalCount` 0 while REST `updated_at` differs from `created_at`; separately, GraphQL reporting an edit while `updated_at` equals `created_at`; separately (positive), all three signals unedited | ERROR (edited) in the first two; the third: no refusal from point 3 | point 3 (HS-5) |
| TR83 | a REST listing that repeats one comment id and omits another, so that its count equals the issue's comment count | ERROR | admission point 2 |
| TR84 | a version of `A` (separately, of the freeze ledger) whose landing commit on `main` has no REST pull-request record with that merge commit, merged into `main` of the attested repository (a direct push); separately, two such records; separately, a pull request merged into another base | ERROR in each case | authority changes (HS-1) |
| TR85 | lint of the host adapter: a GraphQL query other than the edit-history read and the deletion-event read of admission point 3 (for example one reading `isMinimized`, a file, a commit or a pull request) | lint FAIL; the two permitted reads pass | point 3 (HS-2, B1) |
| TR86 | a `CommentDeletedEvent` in the plan's authorized thread (separately, in the authority thread) whose author numeric id is the owner id; separately, the `owner.id` of an earlier version of `A`; separately, an author that is null, absent, not a `User` or without a numeric id; separately (positive), an author whose id differs from every version's `owner.id` | ERROR in the first three; the fourth: no refusal from the deletion events | point 3, "Deletion events" (B1) |
| TR87 | the deletion-event read, each case separately: the request fails; an `errors` entry; a rate-limit response; a partial result; a page missing (events returned fewer than `totalCount`); an event id repeated; a field absent | ERROR in every case; no fallback | point 3, "Deletion events" (B1) |
| G4 | `sc42` with a supplied result file claiming `verbose_equal: true`, while the clone's re-execution differs | FAIL `delegated-evidence-invalid`; the supplied file is not read as evidence | sec. 7.2 (B2) |
| G5 | `coverage-ledger` with a supplied census JSON; one STALE value at `X` differs from the census the tool runs | FAIL | sec. 7.2 |
| G6 | `tex` with a supplied preserve_check result reporting `pass`, while a TeX stamp at `X` is wrong | FAIL `delegated-evidence-invalid` | own re-derivation |
| G7 | `pdf` evidence whose `candidate_tree` differs from `X`'s, or whose artifact hash differs | FAIL `delegated-evidence-invalid` | sec. 7.2 |
| G9 | `C` = `X` plus one commit that changes the SC-42 result file; the class run at `X` alone would PASS | FAIL for `sc42` from the clone at `C` (V7) | sec. 7.2 |
| G8 | delegated evidence with `plan: null` and no `F` | never PASS: REVIEW_REQUIRED `delegated-evidence-missing` for the class, and the field FAIL `delegated-evidence-invalid` | T4 |
| R16 | `C` = `X` plus one commit that changes an unledgered, undeclared path | FAIL `unauthorized-change` naming that commit | sec. 13.1 (B4) |
| R17 | `C` = `X` plus one commit that changes only a record path the plan admits after `F` | PASS for that commit | sec. 13.1 |
| A12r | a widening review whose verdicts omit one changed item; separately, one with no owner authorization | FAIL `record-invalid` each | sec. 6.3 (B4) |
| Z9h | `'guard-pin'` planted in an engine module, with the adapter companions in the value set | lint FAIL | sec. 16.1 (B5) |
| S11-56 | items 5 and 6 at T1': the tool's `register`, `register-caps` and `infinity` results on P's per-edit unit | 0 findings each, equal to P's `static_new` on P's `edits.json`; the mutants of sec. 11 rows 5 and 6 FAIL | sec. 6.1 (D6, V1) |
| S11-57a | a two-variant edit: selected variant unchanged text, unapplied variant adds "now" | FAIL `deny-match` (register), as P's `static_new` (register 1); the per-splice unit alone would PASS | sec. 6.1 (W1) |
| S11-57b | the same with "no longer"; also at an `H` holding `old_step2` | FAIL `deny-match`, as P, at both | W1 |
| S11-57c | one splice covering two edits: one deletes "now", the other adds it elsewhere | ERROR `SOURCE_CHANGED` (edit/splice correspondence); evaluated per edit, FAIL `deny-match` (register), as P | V1 |
| S11-57d | "The bound holds; the lattice is infinite." as an added pair | split into two sentences, as P's splitter does; the result equals P's `static_new` | V1 |
| S11-58a-f | one two-variant edit, with `H` holding: `old` once; `old_step2` only; neither; both once; `old` twice and `old_step2` once; both ambiguous | selection, refusal (ERROR `SOURCE_CHANGED` in c and f) and items 5-6 equal to P's in each case | sec. 6.1 (W1) |
| S11-58g | a splice built for `(old, new)` while P selects `(old_step2, new_step2)` | ERROR `SOURCE_CHANGED` | W1 |
| S11-58h | an earlier edit that destroys a later edit's `old` | ERROR `SOURCE_CHANGED`, as P reports the edit lost | W1 |
| S11-58i | overlap: `old = "aa"` in `"xaaay"` (non-overlapping count 1) | selected at offset 1, as P selects; accepted | sec. 6.1 (V1) |
| S11-58j | chained edits: edit 1 `cat fox` → `fox cat` at `H` `"cat fox."`; edit 2 `cat` → `dog`, whose only occurrence after edit 1 lies inside edit 1's image; the ledger holds edit 1's splice | ERROR `SOURCE_CHANGED` naming edit 2 (chained); P applies the list; P's items 5 and 6 recorded | sec. 6.1 (V1, C4 iii) |
| S11-58k | chained across the image boundary: `H` = `"ab qc"`; edit 1 `{old: "ab q", new: "xy"}`; edit 2 `{old: "qc", new: "Q", old_step2: "yc", new_step2: "Q"}`. Edit 2's `old` occurs once at `H`; after edit 1 the text is `"xyc"`, `qc` no longer occurs, and P selects `yc`, which spans edit 1's image and the original `c`; the ledger holds edit 1's splice | ERROR `SOURCE_CHANGED` naming edit 2 (chained); P applies the list, with result `"xQ"` | V1 (F1) |
| K10 | a meaning-context site with a context change and a matching context adjudication | PASS (sec. 4.1 row 2) | positive direction of K1 |

### 10.5 Real-host validation stage (HS-7)

This stage is not part of this design's adoption or of the implementation step, and runs only under
its own owner authorization. It runs in a host CI job of the attested repository, with the job's own
token, and only reads, except for HV8-HV10 and HV12, which need writes on a dedicated test issue
that the owner authorizes separately. Its decision rules are fixed here; the figures are measured and
recorded, never preset. Until every item has passed on the host, no admission on the real host is
claimed: TR5 and TR48 are reported `NOT RUN` on the real host, and no result is presented for
acceptance under sec. 5. An item that fails returns the design to the owner; no rule of sec. 6.3 is
relaxed to make it pass.

| Id | Measurement or check | Passes when |
|---|---|---|
| HV1 | the job token's REST budget, from the host's rate-limit record inside the job, before and after one complete admission read of the authorized thread, the authority history and the merge records | the REST requests the admission made, counted by the tool, are at most the remaining REST budget measured before it; both figures are recorded |
| HV2 | the job token's GraphQL budget, from the same record, and the point cost of each edit-history query | the points the admission used are at most the remaining GraphQL budget measured before it; both figures are recorded |
| HV3 | the edit-history query over every owner comment of the authorized thread, in batches of the tool's size; and one batch one id larger | each batch of the tool's size returns exactly one issue-comment node per requested id, with the same node id; the larger batch is answered completely or with an error, never truncated without one |
| HV4 | every comment of the thread whose `totalCount` is above 0 | `totalCount` equals the revisions returned; no `diff` is null; the content of the newest revision equals the comment's current REST body, byte for byte |
| HV5 | every comment of the thread | `lastEditedAt` null implies `totalCount` 0, and `lastEditedAt` set implies `totalCount` above 0; the number of comments on which the REST and GraphQL edit signals disagree, and the comments on which an edit signal holds with `totalCount` 0, are recorded |
| HV6 | the edit-history query as the tool frames it | accepted with no `errors`; every field the tool reads, `deletedAt` included, exists in the host's schema |
| HV7 | REST `minimized` on every comment of the thread | each value is `null` or an object |
| HV8 | (write) the owner's account edits a test comment | REST `updated_at` changes; `lastEditedAt` is set; `totalCount` rises; the newest revision's content equals the new body, and an earlier revision's the old body |
| HV9 | (write) a revision of the test comment deleted from its edit history | the history still reports it, in `totalCount` and as a revision with a null `diff` or a set `deletedAt`, so that point 3 refuses |
| HV10 | (write) the test comment minimized | its REST `minimized` is a non-null object |
| HV11 | the deletion-event read of admission point 3 over the plan's authorized thread and the authority thread, every page | accepted with no `errors`; events returned equal `totalCount`; every event's `deletedCommentAuthor` resolves to a `User` with a numeric id; the number of events, and of events whose author is an owner id, are recorded. An event naming an owner id is reported to the owner for separate handling; it changes no rule |
| HV12 | (write) a test comment by the owner's account deleted | a `CommentDeletedEvent` is reported for it, its author's numeric id equal to the owner's id, so that point 3 refuses |

***

## 11. Mapping of the mandatory sec. 11 checks (P's PREREG sec. 11) to the tool

Every command adds `--config F:<record dir>/retirement-config.json` and `--out DIR`, and reads
`F`'s records by object id. Profiles, rules, the delegation contract and the HP obligations come
from the configuration record. Paths given as `F:...` below are resolved through it. `X` is the
execution head. The "Countercontrol" column gives a mutant on which the original check fails; the
tool must also give a non-PASS result on it, and a FAIL wherever the original's failure was a hard
failure.

| # | Original check | Tool command | Expected at a T1'-style `X` | Countercontrol |
|---|---|---|---|---|
| 1 | `edits_check --commit X`: every `new` present; residual pointer scan zero unqualified | `execution --scientific-base H --candidate X --ledger F:ledger.json --edits F:edits.json` (splice postconditions) and `terms --commit X --profile ptr` | splices PASS; `ptr` has 5 hits: the 4 W2 lines PASS with their rules, papers/GR.md:58 with its hit classification record, else REVIEW | one splice reverted in `X`: FAIL `unauthorized-edit`. Original: the `new` string is absent |
| 2 | `ledger_check build` and `check`; CK1-CK8 PASS; extended scan 0 unqualified | `record --pin E --record F` and `coverage --commit X --segment E..H --segment H..X=F:ledger.json --hp F:hp.json --classify F:...` | FAIL or REVIEW (RT-T0) until the records of sec. 8.2 exist; PASS only with them | the frozen self-test's countercontrols at E: unclassified new site gives REVIEW_REQUIRED; dropped Phase-3 site gives FAIL `missing`; J row with S1 Yes gives FAIL (op A `record_checks`) |
| 3 | build; no dropped glyphs; page and median-character counts | `execution ... --delegation F:delegation.json` (classes `tex`, `pdf`, `ci`) | PASS only with bound exact-head evidence | evidence from another `head_sha`, or `build.rc` nonzero: FAIL `delegated-evidence-invalid` |
| 4 | `coverage_check.py`; STALE entries re-affirmed | `execution` class `coverage-ledger`, plus `ci` job `coverage_check` | PASS iff the seven values equal `proof_census` | one STALE value altered, or an id removed: FAIL |
| 5 | register scan of added lines: 0 | `execution` profiles `register` and `register-caps` on P's per-edit and per-step unit, with the per-splice unit and the edit/splice correspondence check as well (sec. 6.1) | PASS (P's `static_new`: 0; controls S11-56, S11-57a-c) | a splice adding "no longer": FAIL `deny-match` |
| 6 | infinity scan of added lines: 0 | `execution` profile `infinity` on P's per-edit and per-step unit with P's splitter, and the per-splice unit (sec. 6.1) | PASS (P's `static_new`: 0; controls S11-56, S11-57d) | a splice adding "is infinite": FAIL |
| 7 | corpus grep: only ledger false positives for `\bA1\b` and related terms; posit counts ("Fourteen", "six structural", "sixth of"): zero | as frozen: `terms --commit X --profile item7-literal` | **FAIL** at T1': 7 "six structural" lines (W1), 0 "Fourteen", 0 "sixth of"; `\bA1\b` 4 lines (W2). Item 7 as frozen does not pass at T1' (RT-I7) | the H-form "Fourteen items" reinstated (V22): FAIL in both the literal check and DR-5. See note 1 for the proposed amendment |
| 8 | mirrors byte-identical | `execution` subject `mirror` | PASS (P's `--static`: 0 findings) | FULL mirror text altered: FAIL `mirror-mismatch` |
| 9 | census registry notes updated in the same commit | `execution` conformance of `verification/lean-manuscript-census.json` (15 splices) | PASS | one registry splice dropped: FAIL `unauthorized-edit` |
| 10 | Lean docstring-only; kernel and Mathlib builds; CI | `execution` subject `lean` (equal outside comments) and class `ci` | PASS with evidence | a Lean definition changed: FAIL `lean-code-change` |
| 11 | `edits_check --repo-scan --final --commit X`: 0 unexplained | `terms --commit X --check item11 --scope F:repo-scope.json --rules F:repo-rules.json --final` | FAIL `final-unclassified` for each of the 176 lines of sec. 8.2 until it has an exact rule (REVIEW without `--final`); then PASS | a new unexplained `A1` line in a new active file: FAIL in the original, FAIL `final-unclassified` here. See note 2 |
| 12 | `edits_check --pins --commit <X's parent>`; guards mutants; R7 and bohr in CI | `execution` subject `pin` (counts at `H` and at `X`) and class `ci` | PASS (the original reported 0 unresolved at its base) | a guard-pin splice dropped: FAIL `pin-broken` |
| 13 | SC-42 regeneration and safeguards | `execution` class `sc42` (native) | PASS iff byte-identical | the result file hand-edited: FAIL |
| 14 | `preserve_check --commit X` (`--base main` when moved) | `execution --scientific-base H --main M --candidate X [--landing L]`, plus the `tex` contract | candidate PASS against `H`; landing per sec. 13 | an extra word in an unledgered file of `X`: FAIL `unauthorized-change`. `L` dropping W's workflow: FAIL `landing-drops-main-change`. Compare the original `--base W`, which failed on `X` only for that workflow file |

**Note 1 (item 7; owner decision D1).** Item 7 as frozen fails at T1': seven lines contain the
legitimate count of the bijection's properties (W1). The tool keeps that literal check as the named
countercontrol `item7-literal`, with the expected FAILs of RT-I7.

- Any restatement of item 7 is a **plan amendment**. It needs its own preregistered text, an
  independent review of the deny set (sec. 6.4), the `resid` profile (sec. 6.6) and the W1 rules,
  and the owner's authorization. It is not "passing as written", and it cannot be used in the
  current frozen trials. Under the exception-free route, the amendment must be adopted before any
  trial can claim item 7.
- The check this design proposes for that amendment: `terms --commit X --base H --ledger
  F:ledger.json --check item7 --final`, where the configuration's `checks.item7` (sec. 16.2) has
  profiles `ptr`, `count-grep`, `resid`, DR-1, DR-3, DR-4 and DR-5 and `final_profiles` `ptr` and
  `count-grep`. It requires zero deny matches; every `ptr` and `count-grep` hit not classified by a
  reviewed rule or record is FAIL `final-unclassified`; every unclassified `resid` hit is
  REVIEW_REQUIRED.
- **Failure behaviour is not weakened (V3).** The original item 7 fails hard on any `\bA1\b` line
  that is not a ledger false positive and on any posit-count literal. In the proposed check every
  such line is a `ptr` or `count-grep` hit, so it is FAIL unless a reviewed record classifies it,
  which is the counterpart of the original's "ledger false positive". At H, 95 retired lines carry
  `\bA1\b` or a `count-grep` literal and match no deny rule; under v4's check they were only
  REVIEW, and under this check all 95 are FAIL (RT-I7A). Counts with no records: at H, 86 deny lines
  (line-level matches; 93 if each line of a matching multi-line sentence is counted) and 123
  `final-unclassified` lines; at T1', 0 deny lines and 12 `final-unclassified` lines (the 7
  W1 lines, the 4 W2 lines and papers/GR.md:58), which pass once their rules and record exist.
  Countercontrols: V23 and V24 FAIL; V25 shows the other direction. `resid` hits stay REVIEW: the
  original check does not fail them at all, so keeping them REVIEW is stricter than the original,
  not weaker.
- **Scope (O7).** Item 7's scope is `papers/*.md` and `book/*.md`. Active files outside it still
  carry "the sixth structural assumption" for A6, whose count includes A1 (for example
  `verification/README.md:2320` and `A6Instantiation.lean:15` at T1'). The amendment's scope
  statement names this, and DR-1's ordinal alternatives are a corpus terminology decision
  (sec. 6.4).
- v3's claim that the restatement "changes the check's text, not its decision on any retired form"
  was false for v3's seed set: the H sentence "Fourteen items, of unequal weight, ..."
  (papers/Main.md:736) escaped DR-1..DR-4. With DR-5 it is a FAIL (RT-DR, V22). The claim is not
  repeated for the v5 set: whether that set preserves the original prohibition on every retired
  form is the independent review's question. The lexically unanchored paraphrases remain a stated
  residual limit (sec. 1), covered at least by REVIEW through `resid` for the classes sec. 1 names.
- The plan's own implementation never ran the literal grep. It checked the retired phrases of
  `identifier_sim()`, P lines 331-335.

**Note 2 (item 11).** The tool is stricter than item 11's original.

- The original passes a premise line in any path-wide-explained file, for example
  `tools/citation_roles_check.py`. The tool fails it.
- Without `--final`, the tool reports an unexplained line as REVIEW_REQUIRED, while the original
  reports it as a failure. The item names `--final`, and under it the REVIEW items of the `repo`
  profile become FAIL `final-unclassified` (sec. 5). No flag turns REVIEW_REQUIRED into PASS.

**Other wording the amendment must correct.** Item 4 says "four entries", but preserve_check's
STALE list has seven (sec. 31, nit 5). Item 12's "execution head's parent" becomes "the ledger base
H".

***

## 12. Placement and governance

### 12.1 Placement

- `tools/ledger_coverage.py` is the entry point. It installs the wrapper (sec. 5) and then imports
  the package.
- `tools/ledger_coverage/engine/` holds the engine (sec. 16.1), its JSON Schemas, the outcome
  checker and the in-memory self-test fixtures. This directory is the purity scope of Z9.
- `tools/ledger_coverage/adapters/` holds the adapter modules: the A1 adapters, the delegation class
  adapters and the synthetic configuration's adapters. It is outside the purity scope; each module
  is pinned by blob in the configuration that uses it (sec. 16.2).
- A new audit directory under `verification/audits/` (sec. A.36) holds the rule files, scope
  records, HP, context and hit classification records, review records, authorization records,
  reconciliation records, and the tool's landing record with its commands and counts.
- The plan's `delegation.json`, `hp.json`, `retirement-config.json` and rule files frozen with the
  plan live in the amended plan's record directory.
- The tool reads every record from git objects, which `export-ignore` does not affect.

### 12.2 Sec. 11 replacement text (v2 addendum 4, point 1)

"The tool is part of the verification route adopted by owner decision c.7093128173 (amaybaum,
2026-11-23T06:13:50Z), which supersedes the execution exception of c.7092885251. Under that route
the retirement plan is amended and frozen again so that each of its mandatory checks names an
operation of this tool and its exact command, and passes as written. No check is waived, replaced
after the freeze, or recorded as a deviation. Landing the tool decides nothing about the
retirement: the plan amendment and its freeze, the repeated trials, the execution and the merge
each keep their own owner gate."

### 12.3 Governance

- The tool's landing may add paths only under `tools/` and its audit directory. It touches no
  ledgered path (control R14).
- Records strengthen no claim (sec. A.22, A.46 item 1).

***

## 13. Four trees

The v2 sec. 13 rules stand, with the corrections below. The certified execution head is `C`
throughout (R9); `E` is only the ledger pin.

### 13.1 Roles and invariants

- **`H`** (`--scientific-base`) must equal `roles.scientific_base` in the frozen configuration
  record (sec. 16.2) and the ledger base. Every `base_sha256` must equal `H`'s blob. `R`'s tree at
  `H` is the pinned tree.
- **`M`** (`--main`) is resolved once and recorded. Its invariants:
  - `H` is on `M`'s first-parent chain;
  - `R`'s tree at `M` is pinned;
  - every path changed between `H` and `M` is a side change, listed with its first-parent commit.

  Side changes are classified by a reviewed side-change class record (schema
  `oi-side-change-classes/1`; for example, the trial workflow file, or the tool's landing paths). A
  class binds each path it covers to its pinned blob (`git_blob` and `blob_sha256`). A path matches a
  class only if its path matches and its blob at `M` equals the pin (S3). This holds for the tool's
  landing class as well (V3): it lists every path the tool's landing commit adds under its prefixes,
  each with its exact blob; a prefix only says where such paths may lie and never classifies a path
  by itself. The one path a class record cannot pin is the class record itself, whose
  `{path, blob_sha256}` the configuration pins. A path under a prefix that is not listed, or whose
  blob differs from its pin, is REVIEW_REQUIRED `side-change-unclassified` (controls R18, R19). A
  class id is defined exactly once across all class records the configuration references; two
  definitions of one id, in one record or several, are ERROR `CONFIG_INCONSISTENT` (S7, control
  Z11). An unclassified side change is REVIEW_REQUIRED `side-change-unclassified`. A side change to
  a ledgered or corpus path is `base-drift`, a FAIL for the landing unless it is reconciled under
  sec. 13.3. Side changes are never retirement edits.
- **`X`** has exactly one parent, `H`. Every path in the diff from `H` to `X` is in exactly one
  class: ledgered, delegated or record. Every other path is byte-identical to `H`. No check of `X`
  reads `M`.
- **`C`**, the certified execution head, descends linearly from `X` when it differs from it (B4).
  Each commit `c` after `X` on that chain, with parent `p`, is classified path by path, exactly as
  `X` is against `H`: every path in the diff from `p` to `c` must be in exactly one class
  (ledgered, delegated or record); a ledgered path must equal `H`'s bytes with the ledger's
  splices applied, as at `X`; a delegated path is checked by its class at `C`; a record path must
  be one the plan's record directory admits after `F`. Any other changed path is FAIL
  `unauthorized-change`, naming the commit. A commit with more than one parent is FAIL
  `candidate-parent`. The tree of `C` is then checked as a whole, as `X` is.
- **`L`** has exactly two parents: the first equals the recorded `M` (FAIL
  `landing-first-parent-not-M` otherwise), and the second equals `C`. Each path is composed as in
  v2 sec. 13.2:
  - A ledgered conflict passes only if `L`'s bytes equal `M`'s bytes with `C`'s splices applied at
    `M`-translated offsets, each `old_sha256` re-verified against `M`. This composition is computed
    and compared for every such path on every landing check, whether or not a reconciliation record
    names the path; no record can stand in for it (sec. 13.3, S6).
  - A generated-artifact conflict is REVIEW_REQUIRED until it is regenerated from `L`'s sources
    under the contract.
  - Any other conflict is FAIL.

  The diff from `M` to `L` must equal the diff from `H` to `C`, path by path, after translation.

### 13.2 Controls

R1-R14, RT-X, RT-L and RT-L2 stand, read with `C` for the certified head. R15 is added: an `L`
whose first parent is a `main` other than the recorded `M` gives FAIL `landing-first-parent-not-M`.
R16 and R17 (the commits of `C`) are in sec. 10.4. N2 (sec. 10.2) stands, now evaluated as sec. 13.3 states (items on `X` with and without the records). Added for the drift findings S2-S7 (the record's own checks R1-R13, named below as "the record's R13" and so on, are not these controls):

| Id | Case | Expected |
|---|---|---|
| N3 | a valid reconciliation record naming a ledgered path that `X` changes (the AGENTS.md shape: D296 at `X`, a later section added on `M`) | the record applies; no `record-invalid`; op C's items on `X` identical with and without it (S2) |
| N4 | the same record with its `ledger_binding` altered by one byte | the record does not apply: `base-drift` FAIL, naming R13 (S5) |
| N5 | `M` with one more first-parent commit changing the path, not in the record's `side_change_commits` | does not apply: `base-drift`, naming R1 (S5) |
| N6 | a protected range at `M` altered by one byte in the composed landing | does not apply: `base-drift`, naming R9 (S5) |
| N7 | the path's blob at `M` differs from the record's `m` | does not apply, naming R2 |
| N8 | a splice's `old` bytes occurring twice at `M` | does not apply, naming R4 |
| N9 | the record's `l` differs from the composed blob | does not apply, naming R7 |
| N10 | the S6 probe, pinned (V8): `M` = 8e9b83341cf5bc7fd9fb260892d0385fc9bfab4d, `X` = T1' (14ac71b4); a landing `L` whose `AGENTS.md` is `X`'s blob 9f4fc3e830707c90ffc105842d26d5b51f01760b (it keeps D296 and drops `M`'s inserted section, bytes 46677-47031); a reconciliation record whose `l` names that same blob. Reference: the composition of `M`'s `AGENTS.md` (6b1280fa) with D296 at offset 2332, blob 86d79863821f3f8cdad86771008b2df89fd1961a | FAIL `landing-conflict-unresolved` for `AGENTS.md`, and `record-invalid` for the record (its `l` differs from the composition, the record's R7); the composition is evaluated regardless of the record (S6) |
| N11 | the same `M`, `X` and reference, with `L`'s `AGENTS.md` equal to blob 86d79863 and the record's `l` equal to it | PASS for the path (positive direction of N10) |
| R18 | a classified side-change path whose blob at `M` differs from its class pin | REVIEW_REQUIRED `side-change-unclassified` (S3) |
| N12 | the record's R3: D296's `old` bytes made to occur twice at `H` in a synthetic copy | does not apply, naming R3 |
| N13 | the record's R5: an insertion on `M` before D296's offset while the record states the identity translation | does not apply, naming R5 |
| N14 | the record's R6: the record's approved text differs from the ledger's `new`, or lines 36-39 of the composition differ from `X`'s | does not apply, naming R6 |
| N15 | the record's R8: the record's `x` differs from the ledger's `expected_sha256` for the path | does not apply, naming R8 |
| N16 | the record's R10: another ledgered file changed on `M` | does not apply, naming R10; that file is `base-drift` |
| N17 | the record's R11: a changed path on `M` not covered by a pinned class, or a corpus path changed | does not apply, naming R11 |
| N18 | the record's R12: `changes_decisions_on_X` non-empty | does not apply, naming R12; the record is `record-invalid` |
| R19 | a path under the tool-landing prefix on `M` that the class does not list, and separately a listed path whose blob differs from its pin | REVIEW_REQUIRED `side-change-unclassified` each (V3) |
| Z11 | two class records (or one record) defining the same class id, for example `trial-workflow` | ERROR `CONFIG_INCONSISTENT` (S7) |
| S4a | a record of each kind (HP, context, hit classification, rule, scope, side-change class, reconciliation, configuration) whose `supersedes` names a `{path, blob_sha256}` that does not exist in the object store, or a blob that is not a record of the same kind | FAIL `record-invalid` for each kind (S4) |
| LN1 | (review probe E6) a record superseding a record of the same kind and schema, present at `F`, with another `record_id`; for each kind of S4a (`config_id` for the configuration) | FAIL `record-invalid` for each kind (DI-2) |
| LN2 | (positive) a record superseding a record of the same kind, schema and `record_id` that itself passes the lint | no `record-invalid`; the run uses the superseding record (DI-2) |
| LN3 | a superseding record whose `record_id` is missing, empty or not a string; separately, a valid superseding record whose predecessor lacks a valid `record_id` | FAIL `record-invalid` in each case (DI-2) |
| LN4 | a predecessor of the same lineage that fails the lint itself (no review record; separately, a verdict not `accept`; separately, no authorization) | FAIL `record-invalid` for the superseding record in each case (DI-2) |
| LN5 | a `supersedes` cycle of two records, and a self-supersession, in a synthetic in-memory store that resolves each named `{path, blob_sha256}` to the given record without rehashing (a hash cycle cannot be built from real objects) | FAIL `record-invalid` in both; the chain walk terminates (DI-2) |
| LN6 | two records of one lineage superseding the same predecessor, both in the audit directory at `F`, only one referenced by the configuration | FAIL `record-invalid` (ambiguous ancestry) (DI-2) |
| LN7 | two records with one `record_id` and kind, each with `supersedes: null` (separately, two chains from one first record that diverge), both read in one run | FAIL `record-invalid` (two heads) (DI-2) |
| LN8 | a three-record chain whose middle record has another `record_id` (separately, another schema of the same kind) | FAIL `record-invalid` (unrelated chain) (DI-2) |
| LN9 | a predecessor R1 authorized by 4242 while owner; 4242 -> 5555; R2 superseding R1, reviewed and authorized by 5555, used by the run. Separately, R1's authorization `time` before 4242 was owner | the first: no `record-invalid`, the run uses R2; the second: FAIL `record-invalid` | DI-1, DI-2 |
| LN10 | (positive) a record with `supersedes: null` and no `record_id`, named by no `supersedes` | no `record-invalid` | DI-2 |
| LN11 | an allow rule R1 widening R0, R1's widening review authorized by 4242 while owner in an authorization record separate from R1's own; 4242 -> 5555; R2 superseding R1, reviewed and authorized by 5555, used by the run; separately, the same for a configuration lineage | no `record-invalid`; the run uses R2, in both | DI-1, DI-2 |
| LN12 | as LN11 for an allow rule, each case separately: R1's widening review listed only by an authorization record with `owner` 5555 whose `time` falls while 4242 is the owner; R1's widening review listed by no authorization record | FAIL `record-invalid` for the superseding record R2 in each case | DI-1, DI-2 |

### 13.3 Reconciliation records (schema `oi-reconciliation/1`)

- A record written after `F` is allowed only for side changes on `M` that the freeze could not
  foresee. It is under the ownership chain of sec. 6.3.
- **What it may and may not do (S2).** A reconciliation record names a ledgered or corpus path that
  both `M` and the retirement change, which is exactly the "both changed" case of v2 sec. 13.2. A
  record that names a path `X` changes is therefore valid. What is forbidden is a record that
  changes a decision of op C on `X` or relabels a failing retirement check. The tool enforces this
  by running op C's candidate checks with and without the reconciliation records and requiring
  identical items on `X`; any difference is FAIL `record-invalid` (control N2). Naming a path that
  `X` changes is never by itself `record-invalid` (control N3).
- **What the tool evaluates (S5).** A reconciliation record applies only if every one of its
  checkable conditions holds at the run's `M` and `L`. The tool evaluates each itself, from git
  objects, and never takes the record's statement that it holds:
  - **ledger binding** (the record's R13): the run's ledger has `base` equal to
    `roles.scientific_base`, and the canonical sha256 (sorted keys, no whitespace, UTF-8) of the
    path's `files` entry, of its splice list and of its edit-list entries equal the record's
    `ledger_binding` values. Checked first;
  - **commit list** (R1): `H` is on `M`'s first-parent chain, and the first-parent commits on
    `H..M` that change the path equal the record's `side_change_commits`, in order;
  - **blob at `M`** (R2): the path's git blob id and sha256 at `M` equal the record's `m` and
    `m_sha256`;
  - **uniqueness and translation** (R3-R5): each splice's `old` bytes occur exactly once at `H` and
    at `M`, and the translation is the one the record states;
  - **protected bytes** (R9): every protected range the record lists occurs once at `M` and once at
    the composed landing blob, with equal bytes and the recorded sha256, and the bytes after the
    last splice are unchanged;
  - **expected blobs** (R6-R8): the composed landing blob's git id and sha256 equal the record's
    `l` and `l_sha256`, and the candidate blob equals `x` and the ledger's `expected_sha256`;
  - **other ledgered files** (R10) and **classified side changes** (R11) as the record states;
  - `changes_decisions_on_X` empty (R12).

  If any condition fails, the record does not apply: the path stays `base-drift` (FAIL), and the
  result names the failed condition. Each condition has its own control: N4 (R13), N5 (R1), N7
  (R2), N12 (R3), N8 (R4), N13 (R5), N14 (R6), N9 (R7), N15 (R8), N6 (R9), N16 (R10), N17 (R11) and
  N18 (R12) (V4).
- **A record never replaces the composition (S6).** At landing, the composition rule of sec. 13.1 is
  always evaluated for every path, with or without a record. A record's `l` is a prediction that
  the tool checks against the composition, never a substitute for it: the landing passes for the
  path only if `L`'s blob equals the composed blob and, where a record exists, the composed blob
  also equals the record's `l`. A record whose `l` names any other blob (for example `X`'s copy,
  which drops `M`'s change) makes the path FAIL `landing-conflict-unresolved` and the record
  `record-invalid` (control N10).

### 13.4 Re-resolving `M`

Immediately before landing, `M` is re-resolved from the remote `main` (`git ls-remote`, read-only)
and checked to equal `L`'s first parent. The landing record quotes the resolved id and the command.

**Sequencing safeguard (c.7093128173).** Before the tool lands, RT-L2 is run against a predicted
`M` that contains the tool's landing paths. It must show every side change classified and no
`base-drift`.

***

## 14. How the figures were measured

All figures were measured read-only, with throwaway scripts reading `git show`, `git ls-tree`,
`git rev-list` and `git cat-file --batch` from the local object store. Their outputs were written
outside the checkout, and the checkout stayed unmodified. Patterns are extracted from their blobs:
Phase-0 `sites.json` at `H`, `EXTENDED_PATTERNS` from `R/ledger_check.py` at `H` by `ast`, and P's
`edits_check.py` (blob sha256 2856e58c...d98c, verified against `P`'s tree). The v5 scripts are in
`work-v5/` beside this file; the v4 scripts in `work-v4/`; the earlier ones in `work/`; the v4
review's in `review-v4/`.

**v5.5 measurements (`work-v55/parity55.py`, sha256 06b6f0515ca07e1cd39f2841468af977d11f1e0bf1062d12a55f7b0a58ffd40d).**
P's `edits_check.py` is imported from its verified blob with `python -I`. The script implements the
rule of sec. 6.1 from its text: the non-overlapping count, the running copy as segments, the mapping
back to `H`, and the refusal of chained edits. It compares the rule with P's own `variant`, with a
`check`-style application and with `static_new`.

- **A1.** All 401 edits are accepted, and the splices reproduce P's application exactly.
- **Crafted cases.**
  - `"aa"` in `"xaaay"`: selected and accepted, as P does.
  - Two chained cases, which P applies: refused as chained.
  - A splice for the unselected variant, and one splice over two edits, both of which P applies:
    refused.
- **Random cases.** 20000 cases over the alphabet "ab ", with one to three edits, 60 % of them with
  two variants:

  | Cases | P | The tool |
  |---|---|---|
  | 2822 | applies; disjoint splices can represent the application | accepts with splices built from P's application, which reproduce P's text |
  | 16905 | refuses | refuses |
  | 273 | applies; the edits are chained | refuses (28 named as chained directly; 245 stop earlier for the edit without a representable splice) |

  No other difference.

**v5.4 measurements (`work-v54/parity.py`).** P's `edits_check.py` is imported from its verified blob with
`python -I`. The script implements, from this document's text and without calling P, the selection
and correspondence rule of sec. 6.1 and the per-edit items 5 and 6. It compares them with P's own
`variant`, `check`-style application and `static_new`:

- **A1.** All 401 edits, in list order with the retained ones: the correspondence holds and binds
  all 399 splices to the `(old, new)` variant at their byte offsets. D032 and D039 have `old` equal
  to `new`. P does not refuse. Items 5 and 6 give 0 / 0 / 0 under both.
- **Regression cases.** Each of these gives selection, refusal and items 5 and 6 equal to P's:
  - `H` holding `old` only, `old_step2` only, neither, both once, `old` twice and `old_step2` once,
    both ambiguous;
  - S11-57a and b, and b at an `H` holding `old_step2`;
  - a progressive loss;
  - a progressive change of the selected variant.
- **Expected differences from P.** A splice for the unselected variant and a splice covering two
  edits are refused (S11-58g, S11-57c). P has no splices, so these are the binding's own refusals.
- **Random enumeration.** 4000 cases of one to three edits, half of them with two variants, over
  texts built from register, caps, infinity and NEUTRAL fragments: 0 differences in items 5 and 6
  from `static_new`, and 0 differences in refusal from P's uniqueness and application. In each
  random case the splices were built from P's own application.

**v5.3 measurements (`work-v53/`).**

- **Edit and splice units (`units.py`).** P's `edits_check.py` imported from its verified blob with
  `python -I`. 401 edits, 399 splices; every splice has an edit of the same id, file, `old` (equal to
  the replaced `H` bytes) and `new` (equal to the image): 399 of 399. The edits without a splice
  are D032 and D039 (retained). No edit has `new_step2`. P's `static_new` on P's `edits.json`: 0
  infinity, 0 register, 0 caps, 0 identifier findings. Cases (a)-(c) through P's own `static_new`:
  register 1 each; the per-splice register rule on the same texts: 0 each.
- **Case-insensitive negatives and the S6 composition (`ci.py`).** On the 7 W1 and 4 W2 sentences
  at T1', case-sensitive and case-insensitive counts of every negative literal are equal (W1-c:
  one `finit`; all others none). `AGENTS.md` at 8e9b8334 is blob 6b1280fa; at T1' 9f4fc3e8; D296's
  `old` bytes are equal at `H` and `M` at offset 2332 and unique at `M`; `M` with D296 applied is
  blob 86d79863821f3f8cdad86771008b2df89fd1961a (sha256 3c334a42cb3d984c...).

**v5.2 measurements (`work-v52/`).**

- **Structure items at H (`struct.py`).** The definitions of sec. 4.2-4.3 (copied from
  `work-v4/ind.py` and `ind2.py`) over every site whose pin line is unique at E and at H: 7 sites
  have a context or structure change in E..H (FULL:706, 708; ch02:76, 78; Substratum.md:94, 253;
  Main.md:741). 3 of them are unique at T1' as well, which is how v4 obtained 3.
- **Region lines (`b3.py` variant).** `work-v4/b3.py` with the site span extended by its LF: 383 /
  197 / 4 sites, 215 region lines, 84 hit lines (86 with `count-grep`); without the LF, 203.
- **RT-D and W1-c (`w1c.py`).** On the 287 added-text lines, 45 carry a `resid` hit, and none of the
  45 is a `ptr` or `count-grep` hit, so under item 7's profile set all 45 are `resid` REVIEW items.
  The W1-c sentence (ch19:198 and FULL:5270 at T1', splitter version 2) has exactly one match of the
  negative literal `finit` and none of the other five; the other five W1 sentences have none.
- **SW2.** Not re-run (about 6 min of sweeps on the implementation). The 7 sites the Stage 1 review
  found with an HP item at the unmutated H are exactly the 7 E..H meaning-context sites of
  sec. 4.4, which carry HP FAILs at H by the rule of sec. 4.1.
- **Register and infinity.** Read from P's verified `edits_check.py`, `static_new` (lines
  351-380) and `inf_key` (lines 345-349).

**v5 measurements (`work-v5/`).**

- **HP walk and mergers (`walk.py`).** A new implementation of sec. 3.2 from its text, over the
  first-parent chain E..H: 113 changed sites, 584 unchanged, 3 two-step sites, first-change
  attribution 48 / 23 / 15 / 15 / 12. Sites whose walks yield the same post-region at the same step
  are grouped: 9 groups, 22 sites (sec. 3.2).
- **Deny rules (`rules5.py`, `dr5.py`).** The v5 rule set and the v5 splitter (sec. 6.1, version 2).
  Line level over every top-level `papers/*.md` and `book/*.md` at E, H, W and T1': 95, 86, 86
  and 0 distinct lines. Per sentence (`sentcount.py`): at H DR-1a 6, DR-1b 2, DR-1c 65, DR-4 28,
  DR-5 1; at E DR-1c 70 and the others as per line; at T1' none. `AGENTS.md` at H
  and W: one DR-3 sentence (lines 37-39); at T1': none.
- **History search (`hist.py`, `hist2.py`).** The searched set is every blob at a top-level
  `papers/<name>.md` or `book/<name>.md` path in the tree of any commit reachable from the 794 local
  refs (7857 commits, `git rev-list --all` then `git ls-tree` per commit): 4677 blobs. It equals
  the union of the path-limited walk (`git rev-list --all --objects -- papers book`, 4657 blobs)
  and the unrestricted walk (`git rev-list --all --objects`, 4671 blobs), which miss 20 and 6 of
  them respectively (sec. 6.4.1). All 4677 were scanned for DR-1d, DR-2 and DR-3 at line and
  sentence level with the v5 splitter: 0 matches. (v5's first pass, `hist.py`, scanned the 4671
  of the unrestricted walk with a "sixth|seventh" prefilter, exact for DR-1d and DR-2: 0 matches.)
  Every
  text file at H (3543 files), W (3543) and T1' (3550): 0 matches of DR-1d or DR-2. DR-3 at H and W
  matches only `AGENTS.md`; at T1' it matches only the frozen record
  `verification/audits/foundations/a1exit-deletion-20261121/edits.json`, which quotes the old
  sentence as an edit's FROM text and is outside every deny scope.
- **Item 7 (`item7.py`).** PTR extracted from P's verified `edits_check.py`; the `count-grep`
  literals; deny lines at line level (`w1o8.py` adds the sentence-attributed variant of O8: 93
  deny lines, 123 unchanged, 216). At H: 198 `ptr` lines, 14 `count-grep` lines, 86 deny lines, 123
  lines that are `ptr` or `count-grep` hits and not deny lines. At T1': 5 `ptr` lines, 7 `count-grep`
  lines, 0 deny lines, 12 lines in all. Retired lines at H (carrying `\bA1\b` or a `count-grep`
  literal, the line text absent from the same file at T1', no deny match): 95, all among the 123.
- **Repo split (`repo.py`).** P's `edits_check.py` imported from its verified blob with `python -I`.
  Each `REPO_PAT` line of every tracked text file at T1' is classified by `classify()`; the
  mechanism (scope, path-wide entry, substring entry, IDENT) is read from the same `EXPLAINED`
  table: 96 / 31 / 14 / 35, with 5486 historical and 2 generated lines.
- **v3's 86 (`m10strict.py`).** `work/measure10.py` with only its overlap test changed from touching
  (`<=`, `>=`) to sec. 5's strict test gives 84. The script skips empty replacement images (`if seg
  and k >= 0`), so the touching test alone produced v3's 86.
- **`resid` (`resid5.py`, `resid5b.py`).** Added text is every T1' line holding a byte of a
  non-empty splice image in a `.md` file (287 lines). Each line is tested against resid-a, resid-b,
  resid-c, the other review profiles (p0-core, p0-para, ledger-ext, `ptr`, `repo`, `count-grep`)
  and the deny rules. Whole-corpus counts at E, H and T1' for the table of sec. 6.6.
- **Escape strings (`esc.py`).** The constructed strings of sec. 1 and 6.4.1 and of the v4 review,
  against the deny rules, `resid`, the other review profiles and the item-7 `final_profiles`.

**Figures carried from v4 and recounted by the v4 review** (`work-v4/` and `review-v4/rv_*.py`):

- **Context and the 12.** Unchanged sites are those whose pin line is unique in its file at E, H
  and T1'. A change is attributed to E..H if the context at H differs from the pin, and to H..T1'
  if the context at T1' differs from H's. 52 changes (27 / 22 / 3); 12 marked by the s3 table
  (7 / 5).
- **Overlap counts.** 19 sites and 31 splices by sec. 3.2's regions; 18 and 31 line-attributed
  (`git diff -U0 --no-renames`, myers and histogram agreeing). D029 (bytes 86149-86197 at H, empty
  image) lies inside :268's H line.
- **Hit lines in replacement regions (`b3.py`, `rv_b3.py`).** Non-HP sites are located at H by
  their unique pin line. A splice overlaps a site by sec. 5's rule. The region at T1' is the union
  of the site span and its overlapping splice spans at H, mapped to T1' offsets and expanded to
  whole lines; removed sites (empty image) have no region. 383 / 197 / 4 sites; 215 region lines
  with the LF-inclusive site span of sec. 5 (203 without the LF, the v4 measurement),
  84 hit lines under p0+ext, 86 with `count-grep`. Variants: the touching test gives 381 / 199
  sites, 217 lines and 86 hit lines (extra: FULL:710, ch02:78); counting the removed sites' offset
  lines under the strict test gives 205 lines and 86, with the same two lines.
- **Unheld lines and the 16 / 7 split (`u116.py`, `rv_u116.py`, `rv_split23.py`).** 200; 84 in
  regions; 116 outside; 93 identical to an unheld H line; 16 in splices over hit lines of HP site
  regions; 7 new on non-site lines.
- **Literal greps (`lit.py`, `rv_lit.py`).** papers/*.md and book/*.md (top level),
  case-sensitive.
- **Indicators (`ind.py`, `ind2.py`, `rv_ctx.py`).** The definitions of sec. 4.2 and 4.3, applied to
  the pin line at E.
- **Merge ids.** `git rev-list --first-parent` over E..H, restricted to `papers` and `book` (v3).

***

## 15. Open points for the owner

0a. **The authority record `A` and the freeze ledger (A-D1 to A-D4, R-D2, R-D4).** `A` must be
   written, independently reviewed, approved by the owner's `oi-authority/1` comment and merged to
   `main` before any freeze. It pins the owner id 7273571, the repository id 1156244443, the workflow
   path and content hash, the engine pins, the plan id with its thread and rounds, the authority
   thread, the freeze-ledger path and the versioned forms. The empty freeze ledger lands in its own merge after it, approved under “Owner at creation”.
   The plan amendment refers to these values. It cannot set them.
0. **RT-L2 at current `main` (Stage 1 review B7).** At `main`, `AGENTS.md` is `base-drift` and
   `.claude/settings.json` is an unclassified side change, so the sequencing safeguard of
   sec. 13.4 does not hold. Resolving it needs reviewed records (a reconciliation record for
   `AGENTS.md` under sec. 13.3, side-change class records) and the owner's decision; under the
   current implementation the reconciliation cannot pass op C (drift finding S2), which v5.2
   specifies away (sec. 13.3).
1. **Decision records.** The owner decisions D1-D4, V5-D1, V5-D2 and S1-D1 to S1-D3 of 2026-11-23,
   and HS-1 to HS-7 of 2026-11-24, reached this writer only through the coordinating session. The
   design should cite them with author, time and comment id once the record exists (sec. A.42
   item 7).
2. **Accepted residuals after V5-D1.** With DR-1d and DR-2 dropped, "the framework's sixth
   structural property, finiteness of the bijection" PASSes when added (control V4), and "the
   substratum's sixth axiom, finiteness" is REVIEW only (V15). The text of v4's former DR-2
   countercontrol, "The framework's sixth structural property is finiteness of the substratum",
   also PASSes (V27). None of these forms occurs in any tree or historical corpus blob.
3. **Residual classes of `resid` (V8).** After widening, the REVIEW guarantee covers the classes of
   sec. 1. Constructed forms outside them PASS: "the six posits of the substratum", "six assumptions
   about the substratum", "The posit ledger lists fourteen.", "the fourteen-item posit ledger" and
   "$A_1$–$A_6$" (the original item 7 misses them too). The owner may accept them as residual or ask
   for further rules. Optional point O1 of the v4 review proposed deny rules for them; v5 does not
   add them, because none has a real-tree match (0 at E, H and T1'), the same ground on which V5-D1
   dropped DR-1d and DR-2.
4. **LIST and TABLE reading.** v4 and v5 keep the neighbour context for list and table sites in
   addition to the review's structure contexts (sec. 4.3). This is stricter than D2's wording; the
   v4 review found it correct.
5. **Independent recount.** The figures labelled WN in sec. 0.3 need an independent recount before
   they are used as references.
6. **The plan's item 7.** The amendment text itself is outside this design (sec. 11 note 1).
7. **Real-host validation (HS-7).** The stage of sec. 10.5 needs its own owner authorization, and
   HV8-HV10 and HV12 need writes on a dedicated test issue, authorized separately. Until every item passes,
   no admission on the real host is claimed.
8. **Host behaviour not yet observed.** Whether every edit changes REST `updated_at` (the tool does
   not rely on it, HS-5); the non-null form of REST `minimized`, which no comment of the repository
   has shown (HV7, HV10); whether a revision deleted from an edit history is still reported (HV9);
   whether a revision's `diff` is its full content (HV4, HV8; an unresolved feasibility risk: if it
   is not, the design returns to the owner, sec. 6.3 "Required earlier text"); whether
   `deletedCommentAuthor` is populated (HV11, HV12); the batch size the host accepts (HV3). The tool's rules refuse wherever the host's answer departs from the expected form. They
   cannot detect a fact the host omits altogether, such as a minimized comment reported with
   `minimized: null` or a deleted revision left out of `totalCount`; HV9 and HV10 test these.
9. **Deleted comments (HS-6).** An investigation, separate from this design and not one of its
   requirements, of completeness only: whether the host's `CommentDeletedEvent` is emitted for every
   deletion, so that the residual of sec. 6.3 could be narrowed, and what cannot be reconstructed (a
   deleted comment's id, body and form). The tool reads the events and refuses on them whatever the
   outcome (admission point 3). Until the investigation gives evidence of completeness, the residual
   stands and no complete historical coverage of a thread is claimed.

***

## 16. Generality: a core independent of any retirement, with frozen per-retirement configuration (condition 9)

### Scope

This section covers design only. It does not include:

- a second real retirement;
- a generic verifier of scientific proofs or semantic correctness;
- any reduction of A1 coverage or preservation obligations;
- any postponement of a review defect.

Only the A1 adapters and one minimal synthetic adapter set are specified. The acceptance gate
remains A1 correctness and fail-closed verification. Generalization is accepted only if every A1
control of sec. 10 and sec. 11 has the same outcome under the configured engine as specified above
(S13).

### 16.1 The engine (`tools/ledger_coverage/engine/`)

The engine is retirement-independent. It contains:

- the pipeline of sec. 2;
- the outcome, exit codes, acceptance checker and output of sec. 5;
- the algorithms: anchors (v1 sec. 4.2-4.4), the overlap and image rules (sec. 5), the region walk
  and merger reporting (sec. 3.2), the context hash, the indicator machinery and structure
  contexts with definitions supplied by the configuration (sec. 4), sentence splitting with the
  abbreviation list supplied by the configuration, rule application and record lint (sec. 6);
- the four role checks (sec. 13);
- the adapter interface definitions (sec. 16.3) and the loader that admits adapter modules by
  pinned blob;
- the configuration loader and validator (sec. 16.6);
- the purity lint Z9.

It contains no commit or tree id, path of a retirement record, terminology, regex pattern, site or
hit count, PR number, delegation class, s3 value, adapter name or checker schema. The adapters,
which must contain their retirement's schema strings (for example "a1exit deletion exact-edit
ledger v2"), are outside the engine, in `tools/ledger_coverage/adapters/` (R8).

**Z9, the purity lint.** It runs over the source blobs of `tools/ledger_coverage/engine/` and the
entry point, parsed by `ast`, and fails on any of the following:

- a hexadecimal literal of 7 or more hex digits standing alone (in a string or as a number),
  including any 40-hex literal;
- a string literal equal to any string value occurring in the A1 configuration, in a record it
  references, in any record its adapters read (the adapter companions: `ledger.json`,
  `edits.json`, `sitemap.json`, `rows.json`, the Phase-0 `sites.json`, and every other file named
  in an adapter's `path` or `companion`), or in the synthetic configuration, unless the value is on
  the allowlist (B5);
- a string literal or identifier matched by any review or deny profile of the A1 configuration.

With the companions in the value set, Z9 catches retirement semantics hard-coded in the engine, for
example the guard-pin handling the Stage 1 engine carried (`engine/execution.py`: the edit kind
`'guard-pin'`, the `pin_note` values `'message'` and `'comment'`, a literal-piece filter, and a read
of `ledger['edits']`, a field outside the ledger interface). Such semantics belong to the ledger
adapter, which returns them through the interface field `guard_pins` (sec. 16.3); the engine reads
nothing from a ledger but the interface's fields. Control Z9h plants `'guard-pin'` in an engine
module and expects a lint FAIL; Z9g, on the real engine with the extended value set, expects no
finding. Allowlisting a value that occurs in a companion (for example a control id that collides
with a row code) requires that the value be an engine enumeration of sec. 16.1, listed by name.

**The allowlist** is fixed in the engine and is itself linted to contain only:

- the interface field names of sec. 16.3 and of the engine's record schemas (for example `id`,
  `file`, `start`, `end`, `new`, `old_sha256`, `new_sha256`, `splices`, `sites`, `base`, `files`,
  `retained`, `mirrors`, `site_id`, `pin_line`, `carried`, `row`, `code`, `owner`, `author`,
  `reviewer`, `reviewed`, `verdicts`, `supersedes`, `path`, `blob_sha256`, `segment`);
- the engine's own schema ids: `oi-ledger-coverage/4`, `oi-retirement-config/1`,
  `oi-term-rules/2`, `oi-delegation/1`, `oi-hp-adjudication/1`, `oi-context-adjudication/1`,
  `oi-hit-classification/1`, `oi-scope/1`, `oi-side-change-classes/1`, `oi-reconciliation/1`,
  `oi-review-record/1`, `oi-owner-authorization/1`;
- the engine's own enumerations: outcome names, sec. 9 class names, ERROR and configuration class
  names, extractor kinds, `review`, `deny`, `tree`, `added-text`, `accept`, `reject`, `dissent`.

Z9's controls are synthetic: they run the lint on an in-memory engine tree (Z9a-Z9f) and on the
real engine tree (Z9g). Z9 runs in CI and in `self-test`; a failure in `self-test` is VOID.

| Id | Case | Expected |
|---|---|---|
| Z9a | a 40-hex commit id planted as a string literal in an engine module | lint FAIL |
| Z9b | a 7-hex abbreviation planted | lint FAIL |
| Z9c | the A1 regex `\bA1\b` planted as a string literal | lint FAIL |
| Z9d | the s3 value "per unit Q2" planted | lint FAIL |
| Z9e | the allowlisted field name `splices` used in an engine module | lint PASS |
| Z9f | an adapter module under `adapters/` containing "a1exit deletion exact-edit ledger v2" | lint PASS (outside the purity scope); the same string moved into the engine: FAIL |
| Z9g | the real engine tree, with the value set extended to the adapter companions | lint PASS |
| Z9h | `'guard-pin'` planted in an engine module | lint FAIL (the value occurs in `edits.json`) |

### 16.2 Configuration record `oi-retirement-config/1`

**Location and pinning.**

- One reviewed, versioned JSON record, `retirement-config.json`, in the retirement plan's record
  directory, frozen with the plan at `F`, under the ownership chain of sec. 6.3.
- Its SHA-256 is listed in `F`'s PREREG pin table, the sec. 26.4 mechanism.
- The tool reads it only as `--config F:path` from the object store. A hash that differs from the
  pin is ERROR `SOURCE_CHANGED`.
- A change after `F` requires a new configuration version and a new freeze.

**Fields.** All fields are required unless marked optional.

| Field | Content |
|---|---|
| `schema` | `oi-retirement-config/1` |
| `config_id`, `version`, `supersedes` | identity; `supersedes` is `{path, blob_sha256}` or null |
| `retirement` | name, accountable Issue and owner login |
| `roles` | `scientific_base` (full id); `pin` and `record_commit` (optional, for replay); `side_change_classes` (`{path, blob_sha256}`) |
| `corpus` | an exact path list, or declared path sets with stated patterns, in a scope record (sec. 6.3) |
| `adapters.ledger` | `{adapter, adapter_version, module: {path, blob_sha256}, path, blob_sha256, companion: [{role, path, blob_sha256}]}` |
| `adapters.sitemap` | as `adapters.ledger`, or null when the retirement has no frozen site map |
| `adapters.replay` | `{adapter, adapter_version, module: {path, blob_sha256}, module_path, record_tree, functions}`, or null (optional) |
| `profiles` | `[{name, kind: review or deny, scope, applies_to: tree or added-text, source: {commit, path, blob_sha256, extractor: {kind, selector}}, pattern_sha256}]` |
| `checks` | one entry per plan check that op D implements: `{id, profiles, final_profiles}`. `final_profiles` lists the review profiles whose REVIEW items `--final` converts for that check (sec. 5). A1: `item7` with `final_profiles` `ptr` and `count-grep`; `item11` with `final_profiles` `repo` |
| `rules` | `[{path, blob_sha256}]`, rule files `oi-term-rules/2` |
| `context_mapping` | `{source_field, values: {value: bool}, default: "invalid"}`. A value outside the table is a configuration error |
| `indicators` | the exact definitions of sec. 4.2 and the effects of sec. 4.3, as data (patterns, word lists, effect per indicator) |
| `sentence` | `{splitter_version, abbreviations}` |
| `hp_obligations` | `[{segment: [from, to], merges: [{pr, commit, first_parent}]}]` |
| `delegation` | `{path, blob_sha256}` (`oi-delegation/1`) with `class_adapters: [{adapter, adapter_version, module: {path, blob_sha256}}]`, or null |
| `records` | every record, review record and authorization record the run may use: `[{kind, path, blob_sha256}]` |
| `operations` | the supported subset of `record`, `coverage`, `execution` and `terms` |
| `controls` | `{path, blob_sha256}`: the retirement's preregistered control set (sec. 10, 11) with expected outcome rules |
| `author` | the configuration's writer; its review and authorization are records under sec. 6.3 |

Supported extractor kinds: `json-pointer`, `python-ast-assign` (a module-level name bound to a
string, a tuple of strings, a dict of strings, or a compiled regex call with a literal pattern),
`python-ast-call-arg` (the literal first argument of a named call, such as `re.split`, inside a
named module-level function; used for P's `sentences`, sec. 6.1), and `literal-list`. The extractor's output must hash to `pattern_sha256`.

**Lint.** The configuration takes the lint of sec. 6.3, with these additions:

- every referenced blob exists at its stated commit (or at `F`) with its stated hash, adapter
  modules included;
- `roles.scientific_base` equals the ledger adapter's reported base;
- the `hp_obligations` segments end at `scientific_base`, and every merge is on its first-parent
  chain with its stated first parent;
- every delegation class has a class adapter;
- no profile name is duplicated, and every `final_profiles` entry of a check is a review profile listed in that check's `profiles`;
- every deny profile has examples in a rule file and a countercontrol named there, the countercontrol being a real line of a scanned file or a control-only input of the controls file;
- the controls file names at least one positive and one adversarial control per configured
  operation.

**Widening (R8, V5).** Every change compared with the superseded configuration is widening, and
needs a `widening_review` under sec. 6.3, unless it is on this non-widening list:

- adding a deny profile, a review profile or a control;
- adding a scope path to a deny profile;
- a context-mapping value changed from false to true;
- adding an entry to a check's `final_profiles`;
- removing an allow rule file.

For definiteness, each of the following is widening (the list is illustrative; the rule above
decides):

- a scope removed or narrowed, and any change to a scope record;
- a deny profile removed or changed; any profile changed;
- a context-mapping value changed from true to false; any change to `indicators`;
- an HP obligation removed;
- an HP obligation added, or a merge added to one (V5). A new merge turns a step that would be FAIL
  `provenance-foreign` into an adjudicable step, and a new obligation for a further segment turns
  changes that would be RET `unauthorized-change` into adjudicable HP sites; both can increase
  acceptance;
- a delegation class added;
- an allow-rule file added, or a new allow rule without `supersedes`;
- a side-change class added or changed;
- an adapter added, or an adapter's module blob or `adapter_version` changed;
- an extractor kind or selector changed;
- a sentence abbreviation added, or `splitter_version` changed (merged sentences change what the
  sentence-level DR-3 sees);
- any change to `operations`;
- an entry removed from a check's `final_profiles`, or a check removed from `checks`;
- a control-only input (sec. 6.4) added, removed or changed;
- a control removed or its expected outcome relaxed.

### 16.3 Adapter interfaces (versioned)

Each adapter is a module under `tools/ledger_coverage/adapters/` that declares an interface name,
an adapter name and an integer version. The engine admits an adapter only if the configuration
names it, its module blob hash equals the configured pin, and its declared interface, name and
version equal the configured ones. Anything else is ERROR `CONFIG_INVALID`. The engine holds no
adapter names.

| Interface | Must return |
|---|---|
| ledger | `base`; `splices [{id, file, start, end, old_sha256, new_sha256, new}]` (byte spans at `base`); `files {path: {base_sha256, expected_sha256}}`; `retained [{id, site_ref}]`; `mirrors [{id, mirror_of}]`; `guard_pins [{id, file, pieces, targets}]` (the updated pin literals the edit list requires, with the retirement's own selection rules applied inside the adapter; B5); `ignored_fields`; plus validation errors (overlap, hash, schema) |
| sitemap | `pin`; `sites [{site_id, file, pin_line, carried: {row, code, owner}, context_field_value, quote}]`; `override_anchors`; `read_entries` |
| replay | `{equalities: [{name, equal}], errors: [str], self_test: bool}`, computed by calling the named functions of a frozen module in a materialization (v1 sec. 3.2), wrapped (sec. 5) |
| delegation | the classes of sec. 7. A class adapter has `verify(evidence, roles) -> PASS, REVIEW or FAIL` and a structured reason |

**The A1 adapters** (all under `adapters/`, each pinned by blob in the A1 configuration):

- `a1exit-exact-edit/2` reads `ledger.json` ("a1exit deletion exact-edit ledger v2") and
  `edits.json` ("a1exit deletion edit list v1").
- `a1exit-sitemap/2` reads the frozen `sitemap.json` ("a1exit site map v2"), `rows.json` and the
  Phase-0 quotes.
- `python-frozen-replay/1` replays `ledger_check.py`'s `manuscript_digest`, `build`, `render`,
  `splice_block`, `check`, `extended_unmapped` and `self_test`.
- The delegation class adapters are `preserve-check-v1` (tex, pdf), `record-dir/1`, `rerun-equal/1`
  (sc42), `fingerprint-regen/1` (coverage-ledger) and `host-run/1` (ci).

### 16.4 A1 as the first configuration: where each A1 constant goes

Every constant of v1-v3 and of this document's sec. 3-13 moves into the A1 configuration
`a1exit-retirement-config`, version 1, into a record it pins, or into an A1 adapter module it pins.
No check changes.

| Constant | Destination |
|---|---|
| `E`, record commit, `R` tree b05efdca | `roles.pin`, `roles.record_commit`, `adapters.replay.record_tree` |
| `H` | `roles.scientific_base` |
| `R` paths and the Phase-0/2 record paths | `adapters.sitemap`, `adapters.replay.module_path` |
| ledger and edits schema ids, `retained_unchanged`, `mirror_of` | the `a1exit-exact-edit/2` module, `adapters.ledger.companion` |
| frozen function names, line-523 handling | the `python-frozen-replay/1` module, `adapters.replay.functions` |
| corpus `papers/*.md`, `book/*.md` | `corpus` |
| profiles p0-core, p0-para, ledger-ext, ptr, repo, count-grep, item7-literal, register, infinity | `profiles` (sources: Phase-0 `sites.json`; `R/ledger_check.py` `EXTENDED_PATTERNS`; `P` `edits_check.py` `PTR`, `REPO_PAT`, `REG`, `CAPS`, `CAPS_OK`, `INF`, `NEUTRAL`; sec. 11 item 7 literals) |
| `resid` (resid-a, resid-b, resid-c), DR-1, DR-3, DR-4, DR-5, W1, W2, the converted `EXPLAINED` entries | rule files under `rules`, profiles naming them |
| item 7 and item 11 profile sets and `final_profiles` (`item7`: `ptr`, `count-grep`; `item11`: `repo`) | `checks` |
| DR-3's control-only witness input (`AGENTS.md` at H) | `controls` |
| repo scope (historical prefixes and files, generated artifacts) | a scope record under `records` |
| s3 mapping (sec. 4) | `context_mapping` (`source_field: s3`) |
| ANAPH, LIST, TABLE, PARTIAL definitions and effects | `indicators` |
| sentence abbreviations | `sentence.abbreviations` |
| the six pinned merges and PR numbers (sec. 3.1) | `hp_obligations[0]` (segment `[E, H]`) |
| tex/pdf/record-dir/sc42/coverage-ledger/ci classes, STALE ids, SC42_BASE ca3a5bb2, `tex_sources` rule, `a1exit-checker-result-v1` | `delegation.json` and the class adapters' parameters in it |
| W's workflow, the tool's landing paths | `roles.side_change_classes` |
| every HP, context, hit classification, review and authorization record | `records` |
| controls RT-*, SW*, the sec. 11 mapping and countercontrols | `controls` |

Counts such as 697, 113 and 19 are not configuration. They are references in the controls file and
in the landing record.

Acceptance criterion S13: the configured engine reproduces every A1 control outcome of sec. 10 and
11 as corrected in this document (control V5 matched by DR-4, V4 and V27 PASS, V15 REVIEW, V7a-V7c,
V23-V26, RT-I7, RT-I7A, RT-DR, RT-DR3W among them), compared item by item with these expectations.

### 16.5 Synthetic second configuration (test only)

`synthetic-retirement-config` is held as in-memory fixture data under `tools/` and is never
committed as a record. Its adapters (`line-patch/1`, `artifact-hash/1`) are modules under
`adapters/`, pinned by blob in the fixture. It is structurally different from A1:

| Aspect | A1 | Synthetic |
|---|---|---|
| Ledger adapter | `a1exit-exact-edit/2` (byte spans, hashes) | `line-patch/1`: edits `{id, file, old_line_sha256, new_lines}`, located by unique whole-line hash |
| Site map | frozen sitemap | none: sites are declared in the configuration as `{site_id, file, line_sha256, carried}` |
| Replay | yes | none; op `record` unsupported |
| Profiles | Phase-0 and the plan's regexes | one review profile `axiom-Z` (`\bAxiom Z\b`), one deny profile `Z-premise` (`\bAxiom Z\b[^.]{0,40}\b(holds|assumed)\b`) |
| HP | one obligation, six merges | one obligation, one synthetic merge |
| Delegation | six classes | one class `artifact-hash/1`: a declared file must hash to a value computed by a declared deterministic recipe |
| Context field | `s3` | `kind`, with values `{definition: true, remark: false}` |
| Indicators | ANAPH, LIST, TABLE, PARTIAL | one: LIST |

**Controls**, run by the same executable with no code change:

| Id | Case | Expected |
|---|---|---|
| Y1 | edits applied exactly; sites moved | PASS |
| Y2 | one edit's new lines changed | FAIL `unauthorized-edit` |
| Y3 | "Axiom Z is assumed" added | FAIL `deny-match` |
| Y4 | a legitimate "Axiom Z" hit with its allow rule | PASS; the same hit with the rule widened without review gives FAIL `record-invalid` |
| Y5 | a site with `kind: definition` and its neighbour changed | FAIL `context-meaning-unverified` |
| Y6 | the artifact hash wrong | FAIL `delegated-evidence-invalid`; evidence absent gives REVIEW_REQUIRED |
| Y7 | `record` requested | ERROR `CONFIG_UNSUPPORTED` |
| Y8 | the A1 configuration and the synthetic one run in one CI job by the same engine blob | identical engine hash recorded in both results |
| Y9 | a list-item site whose lead-in changed | REVIEW_REQUIRED `context-structure-changed` |
| Y10 | the `line-patch/1` module edited by one byte, configuration unchanged | ERROR `SOURCE_CHANGED` |

### 16.6 Fail-closed configuration validation

Validation runs in the integrity stage (sec. 2.1), before any subject is evaluated. No
configuration defect can lead to PASS.

| Defect | Outcome | Exit | Class |
|---|---|---|---|
| unknown `schema`, or unknown or mismatched adapter interface, name or version | ERROR | 65 | `CONFIG_INVALID` |
| missing required field, or unknown field | ERROR | 65 | `CONFIG_INVALID` |
| operation not in `operations` | ERROR | 65 | `CONFIG_UNSUPPORTED` |
| missing or failing review chain (sec. 6.3); reviewer equal to author; widening without review | ERROR | 65 | `CONFIG_UNREVIEWED` |
| hash or pin mismatch of the configuration, an adapter module or any referenced blob | ERROR | 65 | `SOURCE_CHANGED` |
| inconsistency: base differs from the ledger, merge off the chain, context value missing, extractor hash mismatch, duplicate profile, a `final_profiles` entry that is not a review profile, a side-change class id defined more than once (S7) | ERROR | 65 | `CONFIG_INCONSISTENT` |
| configuration controls file absent or empty for an operation | VOID | 70 | `CONFIG_NO_CONTROLS` |

Controls Z1-Z8 each give one of these defects in the synthetic configuration and expect the stated
class. Z9 is the purity lint of sec. 16.1, with its controls Z9a-Z9h.

Z10 (V5): the synthetic configuration superseded by a version that adds a merge to its HP
obligation, with no `widening_review`, so that a step now FAIL `provenance-foreign` would become
adjudicable: ERROR `CONFIG_UNREVIEWED`, exit 65, and the step is not admitted. With a valid
widening review and a matching adjudication, the same step is `provenance-adjudicated`.

### 16.7 Reproducibility

Every `result.json` records:

- `config`: `{config_id, version, path, commit, blob_sha256, admission}`, with, for admission
  `"chain"`, the fields sec. 6.3 lists (the authority record `A`, the attested repository and
  workflow, `F`, every relevant comment with its id, author id, creation time and edit status, and
  the pin table);
- each adapter's interface, name, version, module blob hash and input blob hashes;
- each profile's name, source commit, path, blob and `pattern_sha256`;
- every rule file's path and blob, and the id of every rule applied (in each explanation);
- every record, review record and authorization record used, by path and blob;
- the delegation record hash and each class adapter version;
- the HP obligation's pinned merges;
- the engine blob hash (the entry point and every engine module).

Two runs with equal inputs produce byte-identical output (sec. 5). That is checked in CI by running
twice and comparing.

### 16.8 Implementation step

| Step | Work | Acceptance |
|---|---|---|
| S13 | Configuration loader and validator, adapter admission by blob, the A1 configuration, the synthetic configuration | Z1-Z8, Z9a-Z9h, Z10, Z11 and Y1-Y10 behave; N2-N18, R18, R19, S4a, LN1-LN12, S11-57a-d, S11-58a-k, G9, TR1-TR87, WB13-WB15, X11, TR1-TR5, G4-G8, R16, R17, A12r, WB1-WB12, S11-56 and K10 behave; every A1 control has the same outcome as specified in sec. 10-11 of this document; no engine source contains an A1 constant (Z9); no admission on the real host is claimed before HV1-HV12 pass in the separately authorized stage of sec. 10.5 |
