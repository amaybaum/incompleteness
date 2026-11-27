# Phase 1 post-A1 obstruction reassessment: preservation record

Mutable record under §A.46 items 4 and 8. It cites the reports and does not change them. It is a
draft prepared for the owner's preservation decision, and it records no decision.

- **Evidence layers.** The report is mathematical derivation and source reading on paper. Its
  labels are:
  - K for kernel theorems on `main`, cited and not rebuilt;
  - X for exact algebra in cited records;
  - P for paper arguments in cited records;
  - P-here for arguments written in the report, among them the coherent-control transfers, the
    vacuum-revival argument (§3.1) and the equivariance remark (§3.3).

  No computation was run and no Lean was built.
- **Inputs.** Records on `main`, cited at `13c05b4fe`, an ancestor of `main`:
  - the kernel modules, Main, A1-FCLASS, NR-1, SUBSTATE-1/2, F2-1, MECH-1, MR-1, MEAS-Q, UNIV-1 and
    OBS-EMERGE;
  - SMD-CL-1, FSLICE-PS-1 and UN-1, preserved on `main` by the merges recorded in §4.

  Three records not on `main` (BIDUAL-DIO, OPRES, I3-SOURCE) enter only through claims stated as
  conditional on them (§4).

## 1. The record preserved

**Authoritative report:** `REPORT-r3.md` at the landing head of
`research/phase1-post-a1-obstructions-20261127`. The landing corrections are made in place on it at
`e56149db` and recorded in `CHANGES-r3.md`. The earlier reports and change records are kept
unchanged in the directory:
- `REPORT.md` (r1), committed at `79e1b3d2`, count corrected at `c6c9d02b`, moved into this
  directory at `ccafee2a`;
- `REPORT-r2.md` and `CHANGES-r2.md` (r2) at `aa7e8ce3`;
- `REPORT-r3.md` and `CHANGES-r3.md` (r3) at `95d7c225`.

**Plan.** `PLAN.md` was committed alone at `569940b5`, before any analysis. Its blob is unchanged
through the move at `ccafee2a`, which the r1 review checked. It fixes the questions, the inventory
method, the classification rule, the ranking and rejection criteria, the stopping conditions and the
Goal link. Its stopping condition said "committed locally; no push and no GitHub writes". The
branch was published by the coordinating session under the owner's publication rule (§A.43), as
`CHANGES-r2.md` records.

**Writers.**
- r1 and r2: the Claude coordinating session's designated Phase 1 writer.
- r3: Codex. The commit `95d7c225` carries the repository account; the report header names Codex.
- Landing corrections and this file: the Claude coordinating session, after its takeover under
  §A.52 (#1169 comment 7212372089).

**Status in the header.** `REPORT-r3.md`'s header records the r3 acceptance and the in-place
landing corrections. The review status of those corrections is recorded below.

**Accountable Issues:** #1169, with #914; #1217 for the SMD rows. Guiding pull request: #1625.

**Owner decisions.** Each is a #1169 comment posted from the account `amaybaum`, quoting the
owner:
- **Comment 7209026471** (created 2026-11-27T03:29:13Z): "Approved: Phase 1 post-A1 obstruction
  reassessment as scoped above, paper-only under WP-2, accountable to #1169 with #914." "No premise
  adoption, scientific computation or Phase 2–4 execution is authorized by this decision."
- **Comment 7209325168** (created 2026-11-27T03:51:22Z) routes the SMD findings: "feed these
  findings into the authorized post-A1 obstruction reassessment, specifically examining whether the
  obstruction survives A1 retirement." The UN-1 and F-slice rows were added within the writer's
  scope and under comment 7209354605's "continue the work as outlined under the existing
  authorizations".
- **Comment 7209354605** (created 2026-11-27T03:53:38Z), quoted in part: "For C-ENV and C-SEL,
  distinguish four possibilities"; "Only the first two should advance as physical sourcing
  candidates, provided their underlying principles are independently justified."; "For each
  surviving candidate, identify its potential contribution to SMD, complex structure, native
  quantum operations, observer emergence and gravitational coupling."
- **Comment 7212372089** (created 2026-11-27T07:20:10Z), item 4, quoted from the approved list:
  "Accept the Phase 1 scientific assessment at r3. Correct the two nonblocking wording nits and
  resolve its outstanding preservation and source-tracing requirements before landing."
- **Preservation decision: pending.** No owner decision under §A.46 item 8 authorizing this
  record's merge has been recorded. This file does not authorize a merge (§A.50 item 1).

**Independent non-author reviews.** These are model reviews by reviewer agents, recorded on PR #1625
as reviewer text: evidence of review, not independent mathematical verification.
- **Comment 7209339803, review of r1 at `ccafee2a`: REVISE.** Four major, four medium and three minor
  findings, and three nits. It checked the rule-90 arithmetic exactly over t ≤ 600 and the plan timing.
- **Comment 7210001008, review of r2 at `aa7e8ce3`: REVISE.** Four corrections. It checked the
  vacuum Dickson/Frobenius argument on paper in its stated cases.
- **Comment 7210078621, review of r3 at `95d7c225`: ACCEPT,** with two nonblocking wording nits.
  These are fixed at `e56149db`.
- **Comment 7212555489, focused review of the landing corrections and this file at `9a258779`:
  REVISE,** with four required text corrections and seven nits. These are applied in the following
  commit.
- **Not yet confirmed:** that commit. A focused confirmation is required before landing.

## 2. Substantive result and its precise scope

**Question.** Which established impossibility and ceiling results bearing on native preparation,
observation and coherent control survive the retirement of A1 (total finiteness)? Which are
reopened? Does any candidate mechanism generate or select the required states without assuming
them? The analysis is conditional on A1's retirement, keeping local finiteness (finite alphabet,
finite reading sets, Lemma 1, finite horizons), A5 and the second-order form.

**Results, with their exact limitations.**
- **Inventory.** There are 42 rows. Of the original 30: 23 survive within their stated scopes, five
  are reopened (two escaped by cited counterexamples: P1-15 by NR-1 row 12, P1-18 by infinite-XOR;
  three unproved) and two are unclear (P1-07, P1-17). P1-05, P1-06 and P1-08 are S conditional on
  OPRES, BIDUAL-DIO and I3-SOURCE respectively, records not on `main`.
- **Coherent control.** The kernel forms of the representational ceilings are A1-scoped, because
  the kernel applies `permTheory` globally to `𝒮.Conf`. They survive only within the proposed
  P-here transfer's scope: a countable carrier with a diagonal hidden state and discrete append, or,
  for the detection result, OPRES's measurable conditions, which are conditional on that unlanded
  record. The general entrywise and diagonal-preservation transfers are open. The results are
  representational (KIN; R-READ as a named hypothesis) and are not an operational no-go.
- **A5, not A1.** Setting selection, non-Clifford operations and universality obstructions depend
  on A5. Their windowed transfer is P-here.
- **What A1 retirement reopens.** The global-finiteness layer only: exact return, global record
  erasure, all-time `PPer`, the all-precision fixed carrier, and the counting-measure and
  eventual-image steps.
- **New rows.** SMD-CL-1's Q1 negative holds for infinite-volume product Haar under (B) and (H).
  S-2′ and S-3 are reopened. The K0 witness needs an infinite lattice. K1 is open. FSLICE-PS-1's
  finite-torus results keep their parity and label-sector scopes, and their ℤ^d transfer is open.
  UN-1 is unaffected.
- **Vacuum revival (P-here; checked on paper by the r2 review).** For the native linear rule over
  F_p on ℤ^d from a single current-slice excitation, the origin's value at t = p^k is a·c^k (odd p),
  and site e_1 recovers a at every t = 2^k (q = 2). The vacuum variant of C-ENV fails all-time
  terminality for q = 2 (every α ≠ 0 and d), and for odd p wherever c ≠ 0.
- **Candidates.** None of C-ENV, C-ENV×MON, C-NL, C-ONT or C-SEL generates or selects, from
  independently justified principles, any of: the condensate state with distinct block values,
  SMD, a native complex structure, or native non-Clifford operations. The inventory establishes no
  common sourcing mechanism after A1's removal. §4 of the report states the missing principle as a
  common test setting 𝒞 and proposes P2-MIN, bounded to submitted specifications.

**What the record does not show.** That any mechanism exists or is impossible. That the coherent-
control transfers hold beyond their stated scopes. That the conditional rows hold independently of
their unlanded records. No premise is adopted, nothing is proposed for the manuscripts, and no
Phase 2 work is authorized by this record.

## 3. Verification status and remediation (§A.46 items 4 and 8)

The remediation plans authorize no work (§A.45 rule 3).

| Claim | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| 42-row classification | report §2 | partially verified: model-reviewed (r1–r3) | independent non-model review | #1169, #914 | a recorded independent review |
| Coherent-control transfers (P1-01 to P1-04) | report §2.1 | P-here, model-reviewed; kernel forms A1-scoped | a written proof in the stated regime; the general measurable extensions | #914 | a reviewed proof, optionally Lean over a measurable carrier |
| Rows conditional on BIDUAL-DIO, OPRES, I3-SOURCE | report §2.1, §3, §4, §6 | conditional on records not on `main`; not established here | landing those records under their own preservation decisions, or independent re-derivation | #1509, #1507 | either |
| R-READ, KIN | report §0, §2.1 | named hypotheses | a sourced READ statement | #1501 | QOPS status |
| P1-31 to P1-42 | report §2.6 | as recorded in the landed SMD-CL-1, FSLICE-PS-1 and UN-1 preservation records | as recorded there | #1217, #1216 | as recorded there |
| Vacuum revival | report §3.1 | P-here; checked on paper in review 7210001008 | independent non-model check | #1169 | a recorded check |
| Equivariance remark; class 𝒞 synthesis | report §3.3, §4 | P-here, model-reviewed | review; P2-MIN | #1169, #914 | Phase 2 under its own authorization |
| P1-07, P1-17 (unclear) | report §2.1, §2.3 | open | a proof or a counterexample | #914, #866 | either |
| Candidate premises (E1)–(E3), M1, (x1)–(x4) | report §3, §4 | candidates, not adopted | §A.29 tests | #1169 | owner decisions |
| Landing corrections at `e56149db`; this file | `REPORT-r3.md`, `CHANGES-r3.md`, here | unreviewed | focused exact-head check | #1169 | a recorded check |
| Preregistration order | `PLAN.md` | commit order: `569940b5` at 03:30:06Z precedes `79e1b3d2` at 03:41:23Z (2026-11-27) | none available from commit order alone | #1169 | none; the limitation stands |

## 4. Off-`main` references (§A.42 item 8)

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7209026471, 7209325168, 7209354605, 7212372089 | report header; §1 here | provenance: authority records quoted with author and time |
| PR #1625 comments 7209339803, 7210001008, 7210078621 | §1 here; `CHANGES-r2.md`, `CHANGES-r3.md` | provenance: evidence of review |
| BIDUAL-DIO `e8976f11` (#1509) | report §0 item 5, P1-02, P1-06, P1-20, J-2, AW-P1-4 | support off `main`, closed by **narrowing**: each claim is stated as conditional on the unlanded record |
| OPRES `24702c1d` (#1511) | report §0 item 1, P1-04, P1-05, P1-07, §3.1 NC, §4 NC | support off `main`, closed by **narrowing**, as above |
| I3-SOURCE `df520f3b` (#1508) | report P1-08, J-2, J-3 | support off `main`, closed by **narrowing**, as above; J-3 stands on F2-1 C10 without it |
| QOPS (#1501) | R-READ | provenance: R-READ is a named hypothesis; no QOPS result is used |
| SMD-CL-1 `b7e29ea7`; FSLICE-PS-1 `2706ae17`; UN-1 `4e84b2f2` | report §2.6 | support on `main`: merges `210294b2`, `69786da2`, `9c59074d`. Report texts identical, except one UN-1 verification-table row (Prop I (iii)) that no Phase 1 row uses |
| Pin `13c05b4fe` and the records cited there | throughout | support on `main`: an ancestor of `main`, the cited files unchanged |
| Branch commits `569940b5`, `79e1b3d2`, `c6c9d02b`, `ccafee2a`, `aa7e8ce3`, `95d7c225`, `e56149db`, and the commits adding and completing this file (through the landing head) | §1, §3 here | support off `main` (gap), closed by the merge commit of §5. `569940b5` and `79e1b3d2` carry the preregistration order. The others carry the reports and change records |
| Pivato–Yassawi; Christol; Lucas's theorem; Dickson-polynomial identities | report §2.6, §3.1 | external literature or textbook results, cited by name; Pivato–Yassawi's applicability is stated as unestablished |

**Scope of the tracing.** The tracing is report §6 together with this section. Report §6 classifies
the remaining references: the Issue bodies of #914, #866, #1461, #1062, #1210, #1507 and #1509,
#1169 comment 7079945577, #885 at each use, and #1498, #1503, #1504 and #1216. Once §5's merge
lands, every reference is classified and no gap remains.

## 5. Landing condition

The record is preserved only through a **merge commit, not a squash**. The merge keeps reachable
from `main` every branch commit of §4, including the commits adding and completing this file
(through the landing head), so that `PLAN.md`'s commit precedes every report commit. The
merge needs the owner's separate approval (§A.50 item 1), which this file does not give.

## 6. Preservation rationale

The record answers the owner-authorized Phase 1 question with a plan committed before analysis and
three review rounds. Its results are substantive and nonredundant with A1-FCLASS, the A1-09 census
and the mechanism records, because it applies the A1-dependence classification to the mechanism-side
obstructions. Its findings narrow the search for a physical mechanism:
- the coherent-control bottleneck is set by interface premises and A5, not by A1, within the stated
  scopes;
- A1 retirement reopens only the global-finiteness layer;
- the vacuum sink fails in the stated cases;
- no assessed candidate generates or selects the required states.

This is the owner's stated priority (#1169 comment 7209325168; Goal link #914). The reviews are
recorded in §1, the §A.42 item 8 tracing is complete (§4), the accountable Issues are #1169, #914
and #1217, and each open gap carries a remediation plan (§3).

## 7. Standing of this record

Preservation establishes no claim (§A.46 item 1). The model reviews are evidence of review, not
independent mathematical verification. Landing the record does not change any result's evidence
layer. No premise is adopted, no Phase 2 work is authorized, and nothing is proposed for the
manuscripts.
