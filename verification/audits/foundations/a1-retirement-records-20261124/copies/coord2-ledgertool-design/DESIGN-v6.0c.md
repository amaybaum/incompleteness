# Commit-independent ledger and terminology verification tool: design v6.0c

## Status and authority

This is a paper-only design. Nothing is implemented, committed, pushed or published under it.

- **v6.0c is a bounded correction of the draft v6.0b** (`DESIGN-v6.0b.md`, sha256
  f87dd8bee2c0a9d20beaf462351245f4735eaf056ad0485616fe391dacceb452), applying the independent review
  `review-v6.0b/review.md` (sha256 0c41ec5aa395e7971665b156275fbffdb3fee05a283459d11a4bcf0b4a3445aa,
  verdict ACCEPT-WITH-NITS; finding Q-1, owner question O-1, nits N-a to N-h) under the owner
  decision of 2026-11-24 (owner `amaybaum`, in session, relayed by the coordinating session; no
  comment id held by this writer), quoted:
  > "Approve O-1 option (b): restore the v5.5.9 pre-run pin check in the workflow.
  > Authorize the bounded v6.0c design correction, including the identified reviewer nits.
  > Preserve the following:
  > - Verify executable dependencies before the verification tool runs.
  > - Retain the independent consumer checks.
  > - Preserve all scientific and technical guarantees.
  > - Do not reintroduce automated owner-authorization verification.
  > Obtain a focused independent review of the corrected version before adoption."

  > "Checking the tool's integrity before execution is preferable to discovering afterward that the
  > wrong code ran. This is technical verification, not authorization machinery."

  v6.0c is authoritative only after a focused independent review returns ACCEPT and the owner
  adopts it; until then the authoritative design is v5.5.9. `CHANGES-v6.0c.md` maps every change
  to its finding; `INVENTORY-v6.0c.md` lists every removed, retained and modified section, control
  row and implementation module against v5.5.9, and `CHANGES-v6.0c-from-v5.5.9.diff` is the exact
  difference.
- **v6.0b is a bounded correction of the draft v6.0a** (`DESIGN-v6.0a.md`, sha256
  105db5efe8803876107e525f868051593227f0cc20f0bd2fb7600ea312113585), applying the independent review
  `review-v6.0a/review.md` (sha256 f5f4f57b6c028f0b995984be74be0c1a799e9cd3875dc4c82097a9a0167e9f2a,
  verdict REJECT on R-1, with the demonstrated counterexample CX-3 and the design-level CX-4, and
  nits N1-N6) under the owner decision of 2026-11-24 (owner `amaybaum`, in session, relayed by the
  coordinating session; no comment id held by this writer), quoted:
  > "Approve the bounded v6.0b correction.
  > - Restore the requirement that the tool commit belongs to main's first-parent history.
  > - Require the workflow's executable dependencies and the tool's import environment to be
  >   covered by the integrity checks.
  > - Add the proposed hashlib.py negative control. An unverified file must not execute, even
  >   before the tool performs its own integrity checks.
  > - Apply all six reviewer nits.
  > - Preserve the removal of automated owner-authorization verification.
  > - Obtain fresh independent review against v6.0a and v5.5.9.
  > Keep the implementation as simple as possible. Do not introduce unnecessary security
  > infrastructure."

  > "The reviewer found a genuine weakness: verifying individual files is insufficient if other,
  > unverified files can influence what actually runs."

  `CHANGES-v6.0b.md` maps its changes to their findings.
- **v6.0a is a bounded correction of the draft v6.0** (`DESIGN-v6.0.md`, sha256
  5d4ddf784164c496d98b3194030524b20353cfcd5695fbf102eae68ced85e145), applying the independent review
  `review-v6.0/review.md` (sha256 43cfe728198588eb4f01a38dd817f4d207e50494bb98c5bb20c895df4fddb0ec,
  verdict REJECT on B-1 to B-4, with nits N-1 to N-7) under the owner decision of 2026-11-24 (owner
  `amaybaum`, in session, relayed by the coordinating session; no comment id held by this writer),
  quoted:
  > "Approve the bounded v6.0a correction. 1. Apply B-1, B-2 and B-3 as proposed, including the
  > restored and new negative controls. 2. For B-4, use the fixed meaning table and ensure
  > human-readable results use accurate technical terminology. Do not introduce automated text-lint
  > machinery unless independent review demonstrates a concrete need. 3. Apply the reviewer nits,
  > including explicit failure handling for git ls-remote and negative tests for mismatched plan and
  > pin-table identities. 4. Record the additional requirement for the later A1 plan amendment.
  > 5. Preserve the removal of all automated owner-authorization verification. 6. Obtain fresh
  > independent review against both v6.0 and v5.5.9. ... Keep the scope bounded. Do not introduce
  > additional infrastructure or replacement authorization mechanisms."

  > "The correct distinction is between verifying who approved the work and verifying what actually
  > ran. We removed the former from the tool, but the latter remains essential."

  `CHANGES-v6.0a.md` maps its changes to their findings.
- **v6.0 is a reduced design derived from the adopted v5.5.9** (`DESIGN-v5.5.9.md`, sha256
  cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9, verified before this
  revision). This document is complete in itself; it is not a diff.
- **Owner decisions of 2026-11-24** (owner `amaybaum`, in session, relayed by the coordinating
  session; this writer holds no comment id for them; the record that quotes them with author, time
  and comment id is still to be cited, sec. A.42 item 7 and sec. 15 item 1), quoted:
  > "No, let's remove automated historical authorization verification entirely while retaining
  > explicit owner authorization as a procedural requirement."

  > "One distinction must be preserved: removing automated approval verification does not mean
  > removing verification that the exact approved plan was executed."

  > "Authorize drafting the reduced design and obtaining independent design review. Requirements:
  > 1. Remove automated owner-authorization verification, including authority records, freeze
  > ledgers, comment history and GraphQL dependencies. 2. Preserve all scientific and technical
  > verification guarantees, including exact-commit binding, hash integrity, edit completeness,
  > unrelated-change detection, corpus consistency, controls and mathematical verification. 3. Keep
  > explicit owner authorization as a procedural requirement under the applicable governance
  > rules. 4. Provide a complete inventory of removed, retained and modified design sections, test
  > rows and implementation modules. 5. Independently confirm that no scientific or technical
  > verification guarantee is weakened. 6. Confirm that AGENTS.md requires no amendment under the
  > reduced design. 7. Preserve previous designs and reviews unchanged as historical evidence. Keep
  > ESC-6 and the outstanding A1 evidence gaps under their existing dispositions. The reduced design
  > should be as simple as possible. Do not introduce replacement authorization machinery."

  > "The objective is now much clearer: verify the work, not reconstruct the owner's decision
  > history."

  > "the tool verifies which exact plan was executed; the owner confirms that it was the approved
  > plan. The tool itself makes no claim about authorization."
- **What the tool verifies.** The tool verifies which exact plan was executed and what actually
  ran: every result identifies, and the run verifies against the git object store and the pins of
  the configuration at `F`, the plan commit `F`, the pin table and configuration blobs, the tool
  commit `T` with every tool file and the workflow, the repository and event of the producing CI
  run, and the evaluated commits; the landing record that commits the result is the result commit
  (sec. 5, 6.3). The owner confirms, procedurally and outside the tool, that this was the approved
  plan. The tool makes no claim about authorization (sec. 1); the output's class names carry a
  fixed technical meaning (sec. 5, "Class meanings").
- **What v6.0 removes.** All automated verification of owner authorization: the tool authority
  record `A` (schema `oi-tool-authority/2`); the versioned comment forms `oi-freeze/1`,
  `oi-authority/1` and `oi-freeze-ledger/1`; "Owner at creation"; the freeze ledger; the reading of
  any comment thread, comment edit history, hidden state or deletion event; the authority-change and
  ledger-append procedures; the owner-authorization record `oi-owner-authorization/1` and its lint;
  and every read of the host's GraphQL API and of its comment, Issue, pull-request, branch,
  repository-history and file-content APIs. Nothing takes their place.
- **What v6.0 keeps.** Every scientific and technical verification guarantee of v5.5.9:
  exact-commit binding (sec. 5, 6.3); the hash integrity of every object read (sec. 6.3, "Object
  integrity", which now covers every git read); edit completeness and the edit/splice
  correspondence (sec. 6.1); unrelated-change detection (sec. 7.1, 13.1); the four tree roles and
  the landing composition (sec. 13); corpus and mirror consistency (sec. 11); the profiles, rules,
  records and their independent reviews (sec. 3, 4, 6, 8); the controls and countercontrols
  (sec. 10, 11, 16); native delegated execution with exact-head evidence, including the Lean kernel
  and Mathlib CI evidence (sec. 7); the offline replay (sec. 5); and the fail-closed outcomes
  (sec. 5, 9, 16.6).
- **Owner authorization is procedural.** The approvals AGENTS.md requires (sec. A.50: freezing and
  designating the plan, dispatching its trials, executing it, merging into `main`; sec. A.45 rule 3
  and A.51 for work) are given by the owner and quoted with author and time in the record that
  relies on them (sec. A.42 item 7). The tool neither reads nor checks them.
- **Host reads.** Only the host's REST records of GitHub Actions runs, jobs and artifacts are read
  (sec. 6.3, "Host reads"). Every repository object is read from a local git object store and
  verified against its id.
- Earlier designs and reviews stay as written: `DESIGN.md` (v1) to `DESIGN-v5.5.9.md`, the
  unadopted drafts `DESIGN-v5.5.10.md` and `DESIGN-v5.5.10a.md`, and every review file. The
  history of decisions and reviews up to v5.5.9 is in the "Status and authority" section of
  `DESIGN-v5.5.9.md`, and the decision labels used here (for example D1-D4, V5-D1, V5-D2, S1-D1 to
  S1-D3, R-D1, R-D3, R-D5, A-D5, DI-2, C3, C4) keep the meanings it gives them.
- Identifiers: retained controls, sections and items keep their ids and meaning. Removed control
  ids, the removed sec. 15 item 0a and the retired schema ids are never reused (sec. 10, "Retired
  identifiers"). v6.0 adds the controls GV1-GV7 and sec. 15 items 10-12; v6.0a adds EI1-EI5 and
  restores TR15 and TR50 with their v5.5.9 meaning (the pins are held by the configuration at `F`);
  v6.0b adds EI6 and EI7 and restores TR29's first case with its v5.5.9 meaning; v6.0c adds
  EI8-EI14. None uses any of the
  identifiers the unadopted drafts v5.5.10 and v5.5.10a introduced (TR71-TR87, HV1-HV12, HS-1 to
  HS-7, sec. 10.5, sec. 15 items 7-9).
- Authority for the route: owner decision #1169 c.7093128173 (amaybaum, 2026-11-23T06:13:50Z). It
  approves in principle the exception-free verification route. That route has four steps: the tool
  lands first through its own review and merge decision; `PREREG.md` is amended and frozen again so
  that every mandatory check of sec. 11 passes as written; the trials are rerun; the retirement is
  executed. That decision holds implementation, push, pull request, merge, the plan edit and
  execution. Nothing in this design changes those gates.
- The Q10 disposition (owner decisions of 2026-11-24, `coord2-q10/OWNER-DECISION-20261124.md`) is
  unchanged: ESC-1 to ESC-4 stay unresolved A1 evidence gaps, ESC-5 administrative, and ESC-6 the
  required correction of the S1 classifications and README (sec. 15 item 11).
- Owner standing instructions that bind this revision: correct the design and its expected
  outcomes to match independently verifiable behaviour; never weaken a check to turn a real-tree
  failure green; no retrospective weakening; the generality conditions stay mandatory, within
  their scope.
- The v4 review recounted every v4 figure. The figures v5 introduces or changes carry the label
  WN (sec. 0.3) until an independent reviewer recounts them against this document.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This design
decides how the tool verifies each mandatory check of the amended plan and which exact commits a
run checked. It decides no scientific question, no row disposition and no owner approval.

## Notation

| Symbol | Meaning |
|---|---|
| `E` | e837e3dbaa605efc867a213f3345cee14c36d8f5, the ledger pin. `E` has no other meaning in this document |
| `H` | 53c6601a10419b6b333cc992474272501ab542af, the scientific base |
| `T1'` | 14ac71b4b0a0c0aa2d7068d6799a73f474097060 |
| `P` | 4c79be642ca631573f06b444903be75ec4f5e2b6, the frozen plan |
| `W` | 413b0bb88f39cad901befcf4684355c7ee39480b, `main` at the time of v3 |
| `F` | the future freeze of the amended plan: a commit id given to every run as an explicit input (sec. 6.3) |
| `T` | the tool commit: the commit whose tool files a run executes; the `head_sha` of the producing CI run (sec. 6.3) |
| `X` | the candidate (execution) commit |
| `C` | the certified execution head (sec. A.39 calls it `E`; renamed here, R9) |
| `M` | `main` at check time |
| `L` | the landing merge |

Every commit a run reads or records is a full 40-hex id; no ref name stands for one (sec. 6.3, "Object
integrity").

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
| 8. Review lint for rules, PIN_OK reasons, reconciliation records and other records. The authorization lint of v5.5.9 is removed by the owner decision of 2026-11-24 (item 1); owner approval is procedural and outside the tool (sec. 6.3) | sec. 6.3 |
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
points O1-O7. Rows whose only answer was the automated authorization machinery that v6.0 removes are not
listed here; `DESIGN-v5.5.9.md` sec. 0.2 keeps them, and `INVENTORY-v6.0c.md` table 1 maps them.

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
| v3 R11: ownership chain | sec. 6.3; O1-O3, O5-O9 |
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
| Stage 1 B3: configuration admission from `F`'s pin table | sec. 6.3; TR1-TR3, TR5 |
| Stage 1 B4: commits of `C` classified path by path; widening reviews with coverage | sec. 13.1, 6.3; R16, R17, A12r |
| Stage 1 B5: engine purity over adapter companions; guard pins in the adapter | sec. 16.1, 16.3; Z9g, Z9h |
| Stage 1 B6: control reporting with PASS, FAIL, SKIP and NOT RUN; predicates equal expectations | sec. 10.4; RT-T, RT-D |
| Drift findings S2-S7 (reconciliation, landing composition, class pins, supersedes, one class per id) | sec. 6.3, 13.1, 13.2, 13.3, 16.6; N2-N11, R18, Z11, S4a |
| v5.2 review V1: register and infinity on P's per-edit unit; P's splitter; correspondence check | sec. 6.1, 11 rows 5-6; S11-56, S11-57a-d |
| v5.2 review V3: tool-landing class bound to exact blobs | sec. 13.1; R19 |
| v5.2 review V4: a control for every reconciliation condition | sec. 13.2, 13.3; N12-N18 |
| v5.2 review V5: context hash, location, deterministic grant | sec. 6.2; WB9, WB13, WB14 |
| v5.2 review V6: SW2 reference, 14 sites | sec. 10.3 SW2 |
| v5.2 review V7: native execution at `C` as well as `X` | sec. 7.2; G9 |
| v5.2 review V8: N10 pinned to the S6 probe | sec. 13.2 N10, N11 |
| v5.2 review O1: case-insensitive negative literals | sec. 6.2; WB15 |
| v5.3 review W1: P's edit variants selected as P selects; correspondence | sec. 6.1; S11-57a-c, S11-58a-h |
| owner decision A-D5 and v5.3 review O3: durable evidence on `main` | sec. 5 |
| v5.3 review O2: a sentence's byte offset | sec. 6.2 |
| v5.4 review V1: P's count; offsets back to `H`; chained edits; overlap control | sec. 6.1; S11-58i-k |
| v5.4 review V2 and R-D3: the run's commit; evaluated commits as inputs | sec. 5, 6.3 (execution identity); TR29, TR30 |
| v5.4 review V3 and R-D3: the executed code and workflow bound to the configuration's `tool` pins at `T` | sec. 5, 6.3 (execution identity); TR15, TR28, TR48, TR50-TR52, EI1, EI2 |
| v5.4 addendum C3 and R-D5: admission snapshot, compressed result, offline replay | sec. 5, 6.3 (snapshot); TR45, TR46 |
| v5.4 addendum C4 and R-D1: the stricter refusals stated | sec. 6.1 |
| v5.4 review: residual-trust list | sec. 6.3 |
| owner decisions of 2026-11-24 on the authorization model | Status and authority; sec. 1, 5, 6.3, 7.2, 10, 15, 16.7; GV1-GV7 |
| v6.0 review B-1 to B-4, N-1 to N-6 (v6.0a) | sec. 1, 5, 6.2, 6.3, 7.2, 11, 13.4, 15, 16.2, 16.4, 16.7; TR2, TR5, TR13-TR15, TR28, TR48, TR50, TR52, X10, WB rows, EI1-EI5 |
| v6.0a review R-1, N1-N6 (v6.0b) | sec. 5, 6.3 (configuration admission; execution identity points 4-6; residual trust), 13.4, 15; TR29, EI6, EI7 |
| v6.0b review Q-1, O-1 (b), N-a to N-h (v6.0c) | sec. 5, 6.3 (execution identity points 5-6), 10; TR29, EI6, EI8-EI14 |

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
- The tool checks that role fields differ. It cannot check who wrote a record (sec. 6.3).
- **Approval is outside the tool.** The tool verifies which exact plan, configuration, tool and
  evaluated commits a run checked, and identifies them in its result. Whether that plan is the one
  the owner approved is confirmed by the owner, procedurally (sec. 6.3). No output, outcome, field
  or control of the tool states or implies that a plan, a record, a run or a result was approved
  or authorized.

## 2. Pipeline and subject kinds

### 2.1 Pipeline stages

Every run executes the same stages in a fixed order. A stage that fails stops all later stages.

1. **Usage.** Arguments are parsed and the `--out` guard is applied.
2. **Integrity.** Objects (each verified against its id, sec. 6.3), the tool's own files against
   `T`, pins, record hashes, ledger hashes, the configuration and the adapter module blobs are
   checked.
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
the tool's package, which it loads by location after the isolation check of sec. 6.3 (execution
identity point 5); the isolation check precedes every import of a module not already loaded at
interpreter start (N-g). The wrapper catches `BaseException` (including `SystemExit` raised by frozen
code and `KeyboardInterrupt`) and maps it to INTERNAL, exit 71, with a `result.json`. A failure
before the wrapper is installed exits with the interpreter's own code.

**Acceptance predicate (sec. A.44).** A consumer (a workflow step, the plan's checker or a
reviewer) accepts a run only if all of the following hold:

- the exit status is 0;
- `result.json` exists in `--out` and validates against schema `oi-ledger-coverage/5`;
- its `outcome` is PASS, and the independent outcome checker (S7) recomputes PASS from its
  `preflight`, `record_checks` and `items`;
- its recorded tool commit `T` and tool blobs equal the blobs the consumer reads itself at `T` from
  its own verified object store, and these equal the `tool` pins of the configuration at `F`
  (sec. 6.3); its adapter module blobs equal the configuration's pins; and its configuration
  `{path, blob_sha256}` equals the frozen one;
- `config.admission` is `"chain"` and names the same `F` and the same pin table
  `{path, blob_sha256}` as the landing record (control EI3).
- The result was produced in a host CI run that the consumer verifies itself, by repeating
  execution identity (sec. 6.3, points 1-3, the `uses:` check of point 5, and point 6):
  - the host's REST API reports the run, by its run id, with `repository.id` and
    `head_repository.id` both equal to the configuration's `repository_id`, and with event `push`
    or `workflow_dispatch`;
  - its `head_sha` is the `T` the result records, and `T`'s tree, read from the consumer's own
    verified store, holds the configuration's `tool.files` exactly and the pinned workflow blob at
    `tool.workflow.path`, which is the run's workflow path;
  - the evaluated commits equal the landing record's;
  - `T` is on the first-parent chain of `M`, resolved as sec. 13.4 states (TR29);
  - the result file is that run's uploaded artifact, by sha256.

  A result produced anywhere else, or by other code or another workflow, is never acceptable.
- **Durable evidence (A-D5, C3, R-D5).** Acceptance is recorded only by landing it on `main` in a
  landing record, the result commit. The landing merges only with the owner's approval (sec. A.50
  item 1), which the record quotes with author and time (sec. A.42 item 7); the tool does not read
  or check that quotation. The record commits:
  - **The result, compressed deterministically.** `result.json.gz`: gzip of the exact result bytes,
    with a modification time of 0, no file name, compression level 9 and the operating-system
    field 255. The sha256 of the uncompressed bytes decides; the compressed bytes' sha256 is
    recorded as well.
  - **The admission snapshot** of sec. 6.3, and its sha256.
  - **The reproducibility recipe:** the commits, including `F` and `T`; the configuration, pin
    table, engine, adapter and workflow blob hashes; the exact command; and the tool version.

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
- an unresolvable object: missing from the store, or not hashing to its id (sec. 6.3, "Object
  integrity");
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

**Output form.** Schema `oi-ledger-coverage/5`. It is v5.5.9's `/4` (which extends v3's `/3`) with
the admission snapshot of sec. 6.3 in place of v5.5.9's; a result of another schema id is never
acceptable under this design. Its fields:

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

**Class meanings (B-4).** The schema carries a fixed table `class_meaning`, identical in every
result:

| Class identifier | Meaning |
|---|---|
| `authorized-replacement` | a site replaced by a splice of the frozen ledger |
| `authorized-removal` | a site removed by a splice of the frozen ledger |
| `unauthorized-edit` | a ledgered file whose bytes differ from `H` with the frozen ledger's splices applied |
| `unauthorized-change` | a change that no splice of the frozen ledger and no declared class specifies |

These identifiers are kept from v1 (sec. A.48 item 3). They state nothing about owner approval.
The explanation of every item or site state in one of these classes quotes its meaning from the
table, and every human-readable text the tool writes (explanations, reasons, `resolution_needed`,
messages on stderr) uses the technical terms of this design ("specified by the frozen ledger",
"pinned", "recorded"), never approval vocabulary. This is a requirement on the tool's own strings,
checked in review; no text-lint control is added.

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
   - the sentence's sha256 equals the fingerprint's `sentence_sha256` (the exact fingerprinted text);
   - the context sha256 equals the fingerprint's `context_sha256` (the fingerprinted location: the same
     neighbouring sentences), whether or not the rule sets `context_required`;
   - that fingerprint has not already granted its allowance to another sentence in this tree.

   If, for any negative literal, the sentence has more matches than the allowance grants, the
   result is FAIL `rule-negative-match`. The allowance is bound to one fingerprint, that is, one
   fingerprinted sentence at one fingerprinted location. It is never a global count, and it cannot be used
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
neighbours to another part of the same file, since the fingerprinted text and its fingerprinted neighbours
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

### 6.3 Records, review records and lint (R11, D4); admission, execution identity and object integrity

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

**Owner approval (procedural).** In this design the ownership chain (R11) is the writer, the
independent reviewer and the frozen configuration's reference at `F`. The owner's approval of a
record, of the configuration, of `F` and of a landing is given under AGENTS.md (sec. A.45 rule 3,
A.50, A.51) and quoted with author and time in the record that relies on it (sec. A.42 item 7).
The tool neither reads nor checks it, and no record kind, field, comment or host read stands in
for it.

**Frozen configuration.** `retirement-config.json` at `F` references every record and review
record by `{path, blob_sha256}` (sec. 16.2). A record added after `F` is
admissible only under sec. 13.3's reconciliation rule and never for a decision on `X`.

**What the tool checks.** A record fails, with FAIL `record-invalid`, on any of these:

- a referenced blob that does not exist at `F` at its path, or whose hash differs (this is ERROR
  `SOURCE_CHANGED` when the blob is the configuration's own reference);
- a schema or field error, or a missing field;
- no review record naming exactly this record's blob, or a review record naming another blob;
- `reviewer` equal to `author`;
- a review whose `verdicts` do not cover every item id of the record, or any item not `accept`;
- a `reviewer` value that points to a tool run, a CI run, a check run or an Issue (a URL or run id
  rather than a person);
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
    and, where it widens the record it supersedes, its widening review);
  - a cycle in a `supersedes` chain;
  - ambiguous ancestry: two records superseding the same predecessor, among the records in the
    audit directory and the plan's record directory at `F` and the records the run reads; or a
    lineage with two heads used in one run, a head being a record of the lineage that no other
    record the run reads (the records the configuration references and every record their chains
    name) supersedes;
- a record not read from the git object store.

The tool never infers a role or a review from a passing tool result.

**Configuration admission (O5, B3).** The run names the plan commit `F` (`--freeze F`) and the
configuration (`--config F:<path>`) as explicit inputs. Neither is inferred, and both are recorded.
Any step below that fails, or cannot be completed, refuses with ERROR `CONFIG_UNREVIEWED`:

1. **`F` and the configuration.** `F` is a full commit id, read through the verified reader below.
   The configuration is read only from `F`'s tree at the named path, never from a file the caller
   supplies or from another commit.
2. **The pin table (B-3).** The pin table is derived, not chosen: it is read from the file
   `PREREG.md` in the same directory of `F`'s tree as the configuration, as a regular file. Within
   that file it is the last subsection whose heading matches `^### \d+\.\d+ Record pins\b`; its
   rows are `` | `<file>` | `<sha256>` | ``, each naming a file of that directory. This is the plan's
   own rule ("The pins in force are always the last `Record pins` subsection", P's PREREG). The
   configuration and its review record are admitted only if listed there with their sha256. Files
   beside the configuration that the table does not list are never admitted. A missing `PREREG.md`,
   no such subsection, or a malformed table row refuses. The run takes no pin-table argument.
3. **Local runs and replay.** A run outside a host CI job, or one whose run record cannot be read
   (execution identity, point 1), cannot reach `"chain"`. The offline replay of sec. 5 writes
   `"admission": "replay"` and is never acceptable as a new run.

The record directory of the plan is thereby identified by the configuration's path, which the
result records; the landing record names it with `F`.
Whether `F` and the configuration path are the plan commit and record directory the owner
designated is confirmed procedurally (sec. A.50 items 2 and 5), not by the tool (N2).

**Execution identity (R-D3, B-1, B-2, R-1).** An acceptable result is computed by the tool files and
run by the workflow that the configuration at `F` pins, in the repository it names:

1. **The run record.** The tool reads its own run record by the run id the host assigns, from the
   host's REST API in the repository the job runs in: the repository id, the head repository id,
   the event, the workflow path and the run's `head_sha`. `T`, the tool commit, is that `head_sha`.
   The run's `repository.id` and `head_repository.id` must both equal the configuration's
   `repository_id`, and its `event` must be `push` or `workflow_dispatch`, the events for which the
   workflow that runs is the one at `head_sha`.
2. **The tool's files and the workflow.** `T`'s tree is read through the verified reader. Under
   `tools/ledger_coverage/`, together with the entry point `tools/ledger_coverage.py`, it must hold
   exactly the files of the configuration's `tool.files`, each a regular file whose blob sha256
   equals its pin; a further file, a missing file, a differing blob, or a symlink, submodule or
   other non-regular entry refuses (K7). The run record's workflow path must equal
   `tool.workflow.path`, and the blob at that path in `T` must equal `tool.workflow.blob_sha256`.
   The workflow runs the tool with `python3 -I -B` from a checkout of `T`. Before evaluating
   anything, the tool compares the entry point and every file under `tools/ledger_coverage/` in
   that checkout with `T`'s tree: the same set of paths, each byte-identical. Any difference,
   including a file on disk that `T` does not hold (for example a compiled-bytecode file), refuses.
3. **Evaluated commits are inputs.** The commits evaluated (`X`, `C`, `L`, `M`, and `H` and `E`)
   are explicit full ids, read through the verified reader and recorded. They are never the run's
   `head_sha`, because `X` (`H` plus the ledger) does not contain the tool.
4. **The consumer repeats it.** The consumer repeats points 1-3 and the `uses:` check of point 5
   for the producing run itself (sec. 5),
   from the host's REST API and from its own verified object store, against the configuration at
   `F` that the landing record names. A run whose repository, head repository or event fails
   point 1, a `head_sha` other than the `T` the result records, or a tool or workflow blob that
   differs from the configuration's pins is non-acceptance.

5. **Nothing unpinned executes (R-1, O-1).** In every run of the pinned workflow, no file outside
   `tool.files`, the pinned workflow, the actions it names by commit id and the interpreter's own
   standard library executes in the job, before or after the tool's own checks. The delegated
   checker runs of sec. 7, which execute `F`'s checker blobs and, for `coverage-ledger`, `X`'s own
   `tools/proof_census.py` in clones under `--out` with `-I -B`, are outside this rule and governed
   by sec. 7 as in v5.5.9 (N-h). The rule rests on three parts:
   - **The pre-run pin check (O-1 (b); v5.5.9's "verify the tool blobs ... before executing").**
     The first step after the checkout, before the entry point or any file of the checkout runs,
     is one fixed inline step of the pinned workflow: a short program given in the workflow text
     itself and run as `python3 -I -S -B -c '<program>'`, so that it executes no file of the
     checkout. The workflow fetches `F` by its full id. The step reads the configuration blob at
     `F` with `git cat-file blob`, at the path the run passes to the tool as `--config`, and takes
     `tool.files`. It then examines the entry point `tools/ledger_coverage.py` and the directory
     `tools/ledger_coverage/` on disk with `os.lstat`, never following a link: every entry must be a
     regular file or a directory; the set of regular-file paths must equal the paths of
     `tool.files` exactly, so a `__pycache__` directory's files, a bytecode file, an extension
     module or any other extra file fails; and each file's sha256 must equal its pin. Any failure,
     a missing `F` or configuration, or an unreadable `tool.files` fails the step, and the job ends
     before any tool code runs (EI8-EI13). The step's program is part of the pinned workflow blob
     (TR15, TR50), so it adds no trust root. The tool's own comparison of the checkout with `T`
     (point 2) and the consumer's repetition of point 2 from its own store (point 4) are kept; the
     entry point adds no second package scan.
   - **The import path.** The workflow invokes `python3 -I -B tools/ledger_coverage.py`. Isolated
     mode puts neither the script's directory, the working directory nor any environment-named
     path on `sys.path`. The entry point does not insert any directory of the checkout into
     `sys.path`; it loads the package `tools/ledger_coverage/` by its location. Given the pre-run
     check, the only files of the checkout that can be imported are the pinned files under that
     directory. Before any import of a module not already loaded at interpreter start (only `sys`
     and `os` precede it; N-g), the entry point refuses (ERROR, exit 65) unless the interpreter runs
     in isolated mode and no `sys.path` entry lies inside the checkout. A file such as
     `tools/hashlib.py`, outside the package, is therefore never imported (EI6).
   - **The workflow's executable dependencies.** The pinned workflow executes only the pre-run
     check, the entry point above, fixed `git` commands and the actions it names by commit id (N-b).
     Every occurrence of a `uses` key in the workflow blob must match
     `^\s*(- )?uses: <owner>/<repo>[/<path>]@<40 lowercase hex>\s*$` on its own line, with literal
     `<owner>` and `<repo>` names; any other form refuses, including `./` (a local action or a
     reusable workflow of the same repository), a branch or tag, a quoted key, a flow mapping, a
     block scalar or an alias (EI7). The tool and the consumer check this on the workflow blob at
     `T`. The rest of the workflow's content is checked against the list below when the
     configuration's review covers `tool.workflow`, and the pin then fixes it (TR15, TR50):
     - its triggers and inputs: the run receives `F` and the configuration path as inputs, and a
       run without them fails the pre-run check;
     - `permissions` read-only except artifact upload;
     - a GitHub-hosted `runs-on`; no `container:` and no `services:`;
     - no `env`, `GITHUB_ENV` or `GITHUB_PATH` change of `PATH`, `LD_*`, `GIT_*` or `PYTHON*`;
     - no `shell:` override;
     - the named actions only: no `setup-*` action, and no composite or docker action that installs
       or downloads executables or refers to other actions by tag;
     - the exact run lines: the fetch of `F`, the pre-run check, and the entry point's command.
6. **The tool commit is on `main`.** The tool refuses (ERROR `CONFIG_UNREVIEWED`, before any
   evaluation) unless the run record's `head_branch` is `main`, a field of the run record point 1
   already reads (N-c). The consumer requires `T` to lie on the first-parent chain of `M`, the
   `main` resolved by `git ls-remote` as sec. 13.4 states, walked by the verified reader (TR29).
   This keeps `T` reachable from `main` (sec. A.42 items 1, 3), and bounds every file of `T`,
   pinned or not, to code merged on `main`.

No command-line option, environment value or other configuration field sets `tool` or
`repository_id`; they are read only from the configuration at `F` (N3).

**Object integrity (the verified reader).** Every read of a commit, tree or blob, in a run, by the
consumer and in the offline replay, goes through one reader over a local git object store:

- **Each object verified.** Every object is requested by its full id, and its id is recomputed from
  its type, length and content. An object that is missing, or does not hash to its id, is an
  unresolvable object (ERROR, sec. 5), or refuses admission. A commit's parents and tree, and a
  tree's entries and their modes, are parsed from the verified content.
- **Nothing but verified content.** Refs, reflogs and packed refs are never consulted for a role
  commit: every role commit is an explicit full id (Notation), apart from the re-resolution of `M`
  before landing (sec. 13.4), whose result is then read through this reader. Replace refs and
  grafts are never applied. No parent or ancestry is taken from a traversal command, a graft, the
  store's `shallow` file or a commit-graph file: first-parent chains and ancestry (`H` on `M`'s
  first-parent chain, the commits of E..H and of `X`..`C`, the merges of sec. 3.1, a rule's
  `recorded_at` in sec. 6.2) are computed from parsed parents only.
- **Bounded walks, no fetch.** Every walk runs between explicit commits. A parent the walk needs and
  the store lacks is an error; no object is fetched on demand. What decides is that every object
  the run needs is present and verified. (The native clones of sec. 7.2 stay full clones.)
- **Entries.** Records, rule files, the configuration, the pin table, the delegation contract and the
  tool's files are read only from regular-file entries (mode 100644 or 100755); any other entry at
  such a path refuses.

**Host reads.** The tool and the consumer read from the host only GitHub Actions records, through its
REST API, each with a `GET`:

- the producing run's record (execution identity, point 1), and its artifact list with each
  artifact's sha256 digest (sec. 5);
- for the host-run classes `pdf` and `ci` (sec. 7.2, 7.3): the runs on the evaluated commit, their
  jobs and conclusions, and the `pdf` artifact's digest.

A failed or incomplete read is never a fallback to another source: admission refuses, and a
host-run class whose records cannot be read is REVIEW_REQUIRED `delegated-evidence-missing`, never
PASS (GV7). No comment, Issue, pull request, branch, commit listing, tree or file content is read
through the host's API, and its GraphQL API is not used. Re-resolving `M` before landing
(sec. 13.4) uses `git ls-remote`, which reads one ref id over the git protocol.

**The admission snapshot (C3).** `result.json` records `config.admission`. Its mode is `"chain"`
only when configuration admission and execution identity held, and it carries the snapshot:

- the run record fields read: run id, repository id, head repository id, event, workflow path and
  `head_sha` (`T`); the workflow file's blob sha256 at `T`; the tool blob hashes at `T`;
- the evaluated commits `E`, `H`, `X`, `C`, `L` and `M`;
- `F`, the pin table's `{path, blob_sha256}`, and the configuration's and its review record's
  `{path, blob_sha256}`;
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

- **The host's REST records of Actions runs:** a run's repository and head repository, event,
  workflow path and `head_sha`; its jobs, their names and conclusions; and an artifact's sha256
  digest.
- **The host runner:** that it executes the workflow at `head_sha` faithfully, with the
  interpreter and standard library of its image. Given execution identity point 5, the code that
  ran is then the code whose blobs were read and compared (N6).
- **Git object ids.** Every object is bound to its id by recomputation. That binding rests on
  SHA-1's second-preimage resistance against the objects in the store, and on git's refusal of
  objects that collision-detecting SHA-1 flags. The local store itself is not trusted.
- **At acceptance time, the authenticity of the host records in the admission snapshot.** They are
  host-attested and are not reproducible offline (sec. 5).

The owner's approvals are not among these: they are procedural and outside the tool. If any of
these fails, the tool's checks can be deceived. None of them is a value the caller can
choose.

**Corrections.** A correction is a new record with `supersedes` and a new review. Nothing is edited
in place, and an id is never reused.

**Residual limit.** The tool can check that the role fields differ, not who actually wrote the
records. Identity rests on the writer's and the reviewer's own recorded statements.

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
between the two (each changed field, added file, fingerprint or allowance), and every verdict is
`accept`. A widening review that covers only some items, or names other blobs, is invalid.
Widening without a valid widening review is FAIL `record-invalid`.

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
  no alternates; `X`'s commit and tree ids are checked in the clone), and, when `C` differs from `X`,
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
  tool from the host's REST API inside the job (sec. 6.3, "Host reads"; sec. A.44), never a file
  supplied by a caller. The tool
  checks `head_sha = X`, the named workflow and jobs, and their conclusions, and that the run's
  event is `push` or `workflow_dispatch` and its repository and head repository ids equal the
  configuration's `repository_id` (sec. 6.3). For `pdf` it also
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
| any profile hit in a ledgered replacement image, inside or outside a site region (`new-pattern-in-replacement` when the pattern is absent from the FROM region) | REVIEW_REQUIRED | a hit classification record or an allow rule |
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

**Retired identifiers.** The controls O4, TR4, TR6-TR12, TR16-TR27, TR31-TR44, TR47, TR49,
TR53-TR70, LN9, LN11 and LN12 tested the automated authorization machinery that this design
removes. Their ids are retired and never reused. `INVENTORY-v6.0c.md` table 2 states, for each,
whether it tested authorization only, and which retained control covers any technical guarantee it
also touched. The controls GV1-GV7 and EI1-EI14 (sec. 10.4) are new; TR15 and TR50 keep their
v5.5.9 meaning, with the pins held by the configuration at `F`.

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
| O5 | a `reviewer` field holding a CI run URL | FAIL `record-invalid` | no role inferred from a tool result |
| O6 | a record edited in place after `F` (blob differs from the configuration's reference) | ERROR `SOURCE_CHANGED` | sec. 6.3, 16.2 |
| O7 | a superseding record with no new review | FAIL `record-invalid` | corrections |
| O8 | a record added after `F` and used for a decision on `X` | FAIL `record-invalid` | sec. 13.3 |
| O9 | a complete chain (record, review, configuration reference) | the record is admitted | positive control |
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
| X10 | exit 0 with a `result.json` whose outcome was edited to FAIL; exit 0 with an engine blob hash differing from the configuration's `tool` pin | non-acceptance in both | acceptance predicate |

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
| WB3 | the fingerprinted sentence copied, unchanged, to another paragraph of a file in W1-c's scope | FAIL `rule-negative-match` at the copy (its context differs, so no allowance); the original still PASS | step 3: no reuse in other locations |
| WB4 | the fingerprinted sentence copied to a file outside every W1 rule's scope | REVIEW_REQUIRED `unclassified` (no rule applies; step 1) | scope |
| WB5 | the fingerprinted sentence moved (cut and pasted) to another paragraph of the same file | FAIL `rule-negative-match` at the new location; REVIEW_REQUIRED `rule-stale` for the fingerprint | step 3; `rule-stale` |
| WB6 | a near-copy at the fingerprinted location with one other word changed, keeping one `finit` word | FAIL `rule-negative-match` (sentence sha differs, so no allowance) | step 3: tied to the exact text |
| WB7 | the fingerprinted sentence with its one `finit` word removed | REVIEW_REQUIRED `rule-fingerprint-mismatch` (no negative match; step 4) | step 4 |
| WB8 | the fingerprinted sentence and its neighbours shifted by 40 lines (as L1) | PASS | context-bound, not line-bound |
| WB9 | two fingerprints' sentences made identical in one file, so that one allowance is claimed twice | the claim at the larger byte offset gets no allowance: FAIL `rule-negative-match` | one grant per fingerprint |
| WB10 | lint: a W1-c rule whose allowance is 2, or 0, or names `axiom` (absent from the sentence) | FAIL `record-invalid` | sec. 6.3 (allowance equals the exact count) |
| WB11 | lint: a rule whose fingerprinted sentence fails its own rule (v5.1's W1-c, with no allowance) | FAIL `record-invalid` | sec. 6.3 self-PASS clause |
| WB12 | V7a on the W1-c sentence ("..., one of which is total finiteness,") | FAIL `rule-negative-match` | step 3 |
| WB13 | the fingerprinted sentence moved together with both of its neighbours (the three sentences, unchanged) to another section of the same file | PASS: the context, which defines the location, is unchanged | sec. 6.2, V5 |
| WB14 | the fingerprinted sentence with both neighbours duplicated in the same file, so that two copies satisfy step 3 | the copy at the smaller byte offset PASSes; the later copy FAILs `rule-negative-match`, on every run | sec. 6.2, V5 |
| WB15 | "Finiteness" (capitalized) added to a W1 sentence at its fingerprinted location | FAIL `rule-negative-match` (case-insensitive negatives) | sec. 6.2, O1 |
| X11 | a control-harness PASS result of RT-E, presented with the pinned engine and configuration hashes | non-acceptance (`admission` is not `"chain"`); the harness never writes `result.json` | sec. 5 (B1) |
| TR1 | a run without `--freeze` | ERROR `CONFIG_UNREVIEWED`, exit 65 | sec. 6.3 |
| TR2 | a configuration whose sha256 is not in the pin table of the `PREREG.md` beside it | ERROR `CONFIG_UNREVIEWED` | sec. 6.3, configuration admission point 2 |
| TR3 | a review record placed beside the configuration, naming its blob, but not in `F`'s pin table | ERROR `CONFIG_UNREVIEWED` | configuration admission point 2 |
| TR5 | a complete run: `--freeze F` and `--config F:<path>` given; the `PREREG.md` beside the configuration, whose last `Record pins` subsection lists the configuration and its review; the run record read in a host CI job, with event `workflow_dispatch` and repository and head repository ids equal to `repository_id`; `T`'s tool files and workflow equal to the configuration's `tool` pins and to the checkout | `config.admission: "chain"` with every snapshot field of sec. 6.3 recorded (`F`, the pin table, the configuration, the run with its repository, head repository and event, `T` with its tool and workflow blobs, the evaluated commits) | positive control (CI only) |
| TR13 | a local run, all inputs otherwise valid | no `"chain"` admission; never acceptable | configuration admission point 3 |
| TR14 | the same workflow and tool run in a fork, or in another repository; separately, a `pull_request` run from a fork, executed and listed in the canonical repository (its `head_repository.id` is the fork's); separately, the same results presented to a consumer that runs in a fork | ERROR at the tool wherever it runs with the configuration at `F` (repository or head repository id differs from `repository_id`); non-acceptance at the consumer in every case | execution identity points 1, 4; sec. 5 (B-2) |
| TR15 | a run of a workflow whose blob at `T` differs from `tool.workflow.blob_sha256` (a forged result written by a changed workflow step, review counterexample CX-2); separately, a same-named workflow at a path other than `tool.workflow.path` | ERROR at the tool; non-acceptance at the consumer | execution identity points 2, 4 (B-1) |
| TR28 | a `T` whose tool blobs differ from the configuration's `tool.files` pins (an engine module changed, review counterexample CX-1), or that carries an extra file under `tools/ledger_coverage/` | ERROR at the tool; non-acceptance at the consumer, which reads the blobs itself | sec. 6.3 execution identity point 2 (V3, B-1) |
| TR29 | a run whose `head_sha` is not on `main`'s first-parent chain (a branch); separately, a run whose `head_sha` is the evaluated commit `X`; separately, a result whose recorded `T` differs from the producing run's `head_sha` | ERROR / non-acceptance in each case: the first is ERROR at the tool (the run record's `head_branch` is not `main`) and non-acceptance at the consumer (`T` not on the first-parent chain of `M` resolved as sec. 13.4 states) | execution identity points 3, 4, 6 (V2; R-1; N-c) |
| TR30 | a result whose evaluated commits differ from the landing record's | non-acceptance | sec. 5 (V2) |
| TR45 | the offline replay of an accepted result from its committed snapshot: an op-B result; and an op-C result whose delegated classes (`tex`, `pdf`, `record-dir`, `sc42`, `coverage-ledger`, `ci`) are taken from the snapshot's delegated evidence, with no host call, clone, PDF build or checker run | output equal to the committed result except `config.admission.mode = "replay"`, for both; never acceptable as a new run; a snapshot whose recorded result file does not hash to its recorded sha256, or lacks the evidence for a class the result decided, makes the replay refuse | sec. 5 (C3, F2) |
| TR46 | a committed compressed result whose uncompressed sha256 differs from the recorded one | refused at landing | sec. 5 (C3) |
| TR48 | a valid `T` whose `tools/ledger_coverage/` and entry point hold exactly the configuration's `tool.files`, each a regular file with its pinned blob, and whose workflow blob equals the pin; the checkout equal to `T`'s tree | accepted: execution identity holds, and `T` with every tool and workflow blob is recorded (positive control) | sec. 6.3 execution identity point 2 (K7) |
| TR50 | the workflow at `tool.workflow.path` at `T` modified (one byte changed) | ERROR (its blob differs from `tool.workflow.blob_sha256`); non-acceptance | execution identity point 2 (B-1) |
| TR51 | a symlink, separately a submodule entry, under `tools/ledger_coverage/` in `T`'s tree | ERROR in each case; non-acceptance | K7 |
| TR52 | an additional file under `tools/ledger_coverage/` at `T` that the configuration's `tool.files` does not name | ERROR; non-acceptance | K7 |
| G4 | `sc42` with a supplied result file claiming `verbose_equal: true`, while the clone's re-execution differs | FAIL `delegated-evidence-invalid`; the supplied file is not read as evidence | sec. 7.2 (B2) |
| G5 | `coverage-ledger` with a supplied census JSON; one STALE value at `X` differs from the census the tool runs | FAIL | sec. 7.2 |
| G6 | `tex` with a supplied preserve_check result reporting `pass`, while a TeX stamp at `X` is wrong | FAIL `delegated-evidence-invalid` | own re-derivation |
| G7 | `pdf` evidence whose `candidate_tree` differs from `X`'s, or whose artifact hash differs | FAIL `delegated-evidence-invalid` | sec. 7.2 |
| G9 | `C` = `X` plus one commit that changes the SC-42 result file; the class run at `X` alone would PASS | FAIL for `sc42` from the clone at `C` (V7) | sec. 7.2 |
| G8 | delegated evidence with `plan: null` and no `F` | never PASS: REVIEW_REQUIRED `delegated-evidence-missing` for the class, and the field FAIL `delegated-evidence-invalid` | T4 |
| R16 | `C` = `X` plus one commit that changes an unledgered, undeclared path | FAIL `unauthorized-change` naming that commit | sec. 13.1 (B4) |
| R17 | `C` = `X` plus one commit that changes only a record path the plan admits after `F` | PASS for that commit | sec. 13.1 |
| A12r | a widening review whose verdicts omit one changed item; separately, one naming another superseded blob | FAIL `record-invalid` each | sec. 6.3 (B4) |
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
| GV1 | a replace ref (`refs/replace/`) that substitutes a commit of the E..H chain, and separately one that substitutes the configuration's blob at `F`; separately, a role commit given as a ref name (`main`, a tag) | the replace refs are ignored: the result equals that from the same store without them; the ref name is an unresolvable object (ERROR), refs not being consulted | sec. 6.3, object integrity |
| GV2 | a graft file that makes a commit of the E..H chain parentless | ignored: the result equals that without the graft file | object integrity |
| GV3 | a commit-graph file recording false parents for a commit between `H` and `M`, and for a rule's `recorded_at` | ignored: `H` on `M`'s first-parent chain and the `rule-stale` scoping equal those of the clean store | object integrity |
| GV4 | a loose object whose stored content does not hash to its id, each case separately: the configuration's blob at `F`, the pin table's blob, a tree of `X`, a commit of E..H, a tool blob at `T` | ERROR in each case (`CONFIG_UNREVIEWED` for an admission or identity read, the unresolvable-object error otherwise), although `git cat-file -p` prints the content | object integrity |
| GV5 | a store lacking a parent that a bounded walk needs (a shallow store whose boundary lies inside E..H; separately, a partial store lacking a needed blob); and the positive direction: a shallow store that holds every object the run needs | ERROR in the first two, with no object fetched; the third proceeds as in a full store | object integrity, bounded walks |
| GV6 | a symlink entry at the configuration's path in `F`; separately at the pin table's path; separately at a record's path | refused in each case (ERROR `CONFIG_UNREVIEWED` for the first two; the record `record-invalid`) | object integrity, entries |
| GV7 | the host's REST API failing or incomplete, each case separately: the run record; the consumer's artifact list; the run and job records of a host-run class | no `"chain"` (ERROR `CONFIG_UNREVIEWED`); non-acceptance at the consumer; REVIEW_REQUIRED `delegated-evidence-missing` for the class, never PASS; no fallback source in any case | sec. 6.3, host reads |
| EI1 | the tool run directly, without the pre-run check, on a checkout of `T` in which one tool file differs from `T`'s blob (an engine module patched after checkout), or holds a file `T` does not (a compiled-bytecode file under `tools/ledger_coverage/`) | ERROR at the tool; in the pinned workflow the pre-run check fails first (EI9, EI13), and the consumer's repetition of point 2 (TR28, TR52) is the binding refusal | execution identity point 2 |
| EI2 | a run whose event is `pull_request` (head in the canonical repository); separately `schedule`; separately `workflow_run` | ERROR at the tool; non-acceptance at the consumer | execution identity point 1 (B-1) |
| EI3 | a result whose `F` differs from the landing record's; separately, whose pin table `{path, blob_sha256}` differs; separately, whose configuration path differs | non-acceptance in each case | sec. 5 (review N-1) |
| EI4 | `F` holds the plan directory with its `PREREG.md` and a second directory whose `PREREG.md` lists another configuration: (a) that other configuration placed in the plan directory, listed only by the second `PREREG.md`; (b) a caller argument naming the second `PREREG.md` as pin table; (c) the plan's `PREREG.md` whose last `Record pins` subsection omits the configuration while an earlier one lists it; (d) no `PREREG.md` beside the configuration; separately, a malformed row in its last `Record pins` subsection | (a), (c), (d): ERROR `CONFIG_UNREVIEWED`; (b): USAGE, exit 64 (the run takes no pin-table argument) | configuration admission point 2 (B-3) |
| EI5 | before landing, `git ls-remote` failing; separately, returning no `refs/heads/main` line or more than one; separately, an id that is not a full 40-hex id, or that the verified reader cannot read; separately, an id other than `L`'s first parent | the landing is refused in each case | sec. 13.4 (review N-2) |
| EI6 | the checkout of a `T` holding, besides the pinned files, an unpinned `tools/hashlib.py` (separately `tools/re.py`, `tools/subprocess.py`) whose module body writes a marker, the probe `review-v6.0a/cx3/hashlib_probe.py`; separately, the entry point run without `-I`, or with a checkout directory on `sys.path` | the first: the marker is never written, every imported module's file lies in `tool.files` or the interpreter's standard library, and the run's items equal those of the same run without the file; at the consumer a `T` that is not on `main`'s first-parent chain is non-acceptance (TR29). The second: ERROR at the entry point, exit 65, before any import of a module not already loaded at interpreter start | execution identity point 5 (R-1; N-g) |
| EI7 | a pinned workflow blob with `uses: ./.github/actions/x`; separately `uses: ./.github/workflows/w.yml`; separately `uses: owner/action@v4` (a tag); separately `uses: owner/action@main` | ERROR at the tool; non-acceptance at the consumer | execution identity point 5 (R-1, N5) |
| EI8 | the pre-run check on a clean checkout of a `T` equal to the configuration's `tool.files` | the step passes and the entry point runs (positive control) | execution identity point 5 (O-1) |
| EI9 | the pre-run check on a checkout holding `tools/ledger_coverage/engine/__pycache__/util.cpython-313.pyc`, an unchecked-hash bytecode file whose code writes a marker (review v6.0b probe P4) | the step fails; the job ends before the entry point runs; the marker is never written | point 5 (O-1) |
| EI10 | the pre-run check on a checkout holding an extension module `tools/ledger_coverage/engine/util.so` beside the pinned `util.py` (probe P7) | the step fails before the entry point runs; the module's init never runs | point 5 (O-1) |
| EI11 | the pre-run check on a checkout in which the pinned path `tools/ledger_coverage/engine/util.py` is a symlink to a payload outside the package (probe P9) | the step fails before the entry point runs; the payload never runs | point 5 (O-1) |
| EI12 | the pre-run check on a checkout in which the entry point `tools/ledger_coverage.py` is a symlink to `tools/evil.py` (probe P10) | the step fails before the entry point runs; `evil.py` never runs | point 5 (O-1) |
| EI13 | the pre-run check, each case separately: a pinned file changed by one byte; a pinned file missing; an extra `.py` file under `tools/ledger_coverage/`; a directory entry that is neither a regular file nor a directory; `F` not fetched; the configuration path absent at `F`; a configuration without `tool.files` | the step fails in each case before the entry point runs | point 5 (O-1) |
| EI14 | the review v6.0a CX-3 tree: a branch `T'` holding the pinned files and an unpinned `tools/hashlib.py` | the pre-run check passes (the file lies outside the pinned paths and the step does not examine it); the file never executes (EI6); the tool refuses with ERROR before any evaluation (`head_branch` is not `main`, TR29); at the consumer, non-acceptance (TR29). The same file at an on-`main` `T`: never executed, the run unaffected | points 5, 6 (O-1; N-c) |

***

## 11. Mapping of the mandatory sec. 11 checks (P's PREREG sec. 11) to the tool

Every command adds `--freeze F` (sec. 6.3),
`--config F:<record dir>/retirement-config.json` and `--out DIR`, and reads
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
  records, HP, context and hit classification records, review records, reconciliation records,
  and the tool's landing record with its commands and counts.
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
| LN4 | a predecessor of the same lineage that fails the lint itself (no review record; separately, a verdict not `accept`; separately, a predecessor that widens its own predecessor without a valid widening review) | FAIL `record-invalid` for the superseding record in each case (DI-2) |
| LN5 | a `supersedes` cycle of two records, and a self-supersession, in a synthetic in-memory store that resolves each named `{path, blob_sha256}` to the given record without rehashing (a hash cycle cannot be built from real objects) | FAIL `record-invalid` in both; the chain walk terminates (DI-2) |
| LN6 | two records of one lineage superseding the same predecessor, both in the audit directory at `F`, only one referenced by the configuration | FAIL `record-invalid` (ambiguous ancestry) (DI-2) |
| LN7 | two records with one `record_id` and kind, each with `supersedes: null` (separately, two chains from one first record that diverge), both read in one run | FAIL `record-invalid` (two heads) (DI-2) |
| LN8 | a three-record chain whose middle record has another `record_id` (separately, another schema of the same kind) | FAIL `record-invalid` (unrelated chain) (DI-2) |
| LN10 | (positive) a record with `supersedes: null` and no `record_id`, named by no `supersedes` | no `record-invalid` | DI-2 |

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

Immediately before landing, `M` is re-resolved from `main` of the repository that
`repository_id` names (`git ls-remote`, read-only; N4)
and checked to equal `L`'s first parent. The landing record quotes the resolved id and the command.
A failed `git ls-remote`, an output without exactly one `refs/heads/main` line, an id that is not a
full 40-hex id or that the verified reader cannot read, or an id other than `L`'s first parent
refuses the landing (control EI5). The consumer then requires `T` on `M`'s first-parent chain
(sec. 6.3, execution identity point 6; TR29).

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

0. **RT-L2 at current `main` (Stage 1 review B7).** At `main`, `AGENTS.md` is `base-drift` and
   `.claude/settings.json` is an unclassified side change, so the sequencing safeguard of
   sec. 13.4 does not hold. Resolving it needs reviewed records (a reconciliation record for
   `AGENTS.md` under sec. 13.3, side-change class records) and the owner's decision; under the
   current implementation the reconciliation cannot pass op C (drift finding S2), which v5.2
   specifies away (sec. 13.3).
1. **Decision records.** The owner decisions D1-D4, V5-D1, V5-D2 and S1-D1 to S1-D3 of 2026-11-23, and the
   owner decisions of 2026-11-24 quoted in "Status and authority", reached this
   writer only through the coordinating session. The design should cite them with author, time and
   comment id once the record exists (sec. A.42 item 7).
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
6. **Item 7.** The amendment text itself is outside this design (sec. 11 note 1).
10. **Focused independent review of v6.0c.** The owner's requirement 5: an independent reviewer confirms that
    no scientific or technical verification guarantee of v5.5.9 is weakened (`INVENTORY-v6.0c.md`
    table 4), and the AGENTS.md conclusion (table 5).
11. **ESC-6 and the A1 evidence gaps.** Unchanged under the accepted Q10 disposition: ESC-1 to ESC-4
    stay unresolved A1 evidence gaps; ESC-5 is administrative; ESC-6 (the correction of the S1
    classifications and the landing README) stays open until its separately reviewed change. None
    of them blocks the tool's landing, and this design resolves none of them.
12. **The plan amendment.** The later, separately authorized amendment of the A1 plan does not
    refer to an authority record, a freeze ledger, comment forms or an automated authorization
    check (`INVENTORY-v6.0c.md` table 6). Its frozen configuration carries the `tool` pins (tool
    files and workflow) and the `repository_id` (sec. 16.2), and lies beside the `PREREG.md` whose
    last `Record pins` subsection lists it (sec. 6.3). Its pinned workflow meets execution
    identity point 5 of sec. 6.3, including the pre-run pin check.

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
- the engine's own schema ids: `oi-ledger-coverage/5`, `oi-retirement-config/1`,
  `oi-term-rules/2`, `oi-delegation/1`, `oi-hp-adjudication/1`, `oi-context-adjudication/1`,
  `oi-hit-classification/1`, `oi-scope/1`, `oi-side-change-classes/1`, `oi-reconciliation/1`,
  `oi-review-record/1`;
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
| `retirement` | name and accountable Issue |
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
| `records` | every record and review record the run may use: `[{kind, path, blob_sha256}]`. A kind this design does not define, such as the retired `oi-owner-authorization/1`, is ERROR `CONFIG_INVALID` |
| `tool` | `{files: [{path, blob_sha256}], workflow: {path, blob_sha256}}`: every file of the tool (the entry point and every file under `tools/ledger_coverage/`) and the workflow whose runs may produce an acceptable result (sec. 6.3, execution identity) |
| `repository_id` | the numeric host id of the repository whose runs may produce an acceptable result (sec. 6.3) |
| `operations` | the supported subset of `record`, `coverage`, `execution` and `terms` |
| `controls` | `{path, blob_sha256}`: the retirement's preregistered control set (sec. 10, 11) with expected outcome rules |
| `author` | the configuration's writer; its review is a record under sec. 6.3 |

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
  operation;
- `tool.files` names the entry point and only paths under `tools/ledger_coverage/`, each once, and
  `repository_id` is a positive integer.

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
- any change to `tool` or `repository_id`;
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
| the tool's file and workflow pins; the repository id 1156244443 | `tool`, `repository_id` |
| W's workflow, the tool's landing paths | `roles.side_change_classes` |
| every HP, context, hit classification and review record | `records` |
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
  `"chain"`, the snapshot fields sec. 6.3 lists (the producing run, `T` and its tool blobs, `F`,
  the pin table and the evaluated commits);
- each adapter's interface, name, version, module blob hash and input blob hashes;
- each profile's name, source commit, path, blob and `pattern_sha256`;
- every rule file's path and blob, and the id of every rule applied (in each explanation);
- every record and review record used, by path and blob;
- the delegation record hash and each class adapter version;
- the HP obligation's pinned merges;
- the tool commit `T`, the run's repository, head repository and event, and the engine blob hash
  (the entry point and every engine module), each tool blob equal to its `tool` pin.

Two runs with equal inputs produce byte-identical output (sec. 5). That is checked in CI by running
twice and comparing.

### 16.8 Implementation step

| Step | Work | Acceptance |
|---|---|---|
| S13 | Configuration loader and validator, adapter admission by blob, the A1 configuration, the synthetic configuration | Z1-Z8, Z9a-Z9h, Z10, Z11 and Y1-Y10 behave; N2-N18, R18, R19, S4a, LN1-LN8, LN10, S11-57a-d, S11-58a-k, G9, TR1-TR3, TR5, TR13-TR15, TR28-TR30, TR45, TR46, TR48, TR50-TR52, GV1-GV7, EI1-EI14, WB13-WB15, X11, G4-G8, R16, R17, A12r, WB1-WB12, S11-56 and K10 behave; every A1 control has the same outcome as specified in sec. 10-11 of this document; no engine source contains an A1 constant (Z9) |
