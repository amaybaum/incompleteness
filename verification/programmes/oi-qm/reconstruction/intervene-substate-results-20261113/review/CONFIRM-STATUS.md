# Focused check of `STATUS.md` for PR #1274

**Verdict: ACCEPT WITH CHANGES.** The commit changes no reviewed file. Every quotation is verbatim,
and every id and time resolves. The three integration requirements are quoted word for word, and the
account of how each is met does not overclaim.

There is one blocking item, finding 1. `STATUS.md` restates, in its "claim supported by this record"
and in its results table, a sentence of the accepted record that generalizes from two witnesses to
every non-spanning frame. That generalization is false: a counterexample is given below. My
REVIEW-r1 and CONFIRM-r2 accepted the sentence and should not have. Findings 2 and 3 are should-fix.
The rest are nits. Every fix is confined to `STATUS.md` and the drafting log, so the reviewed files
stay unchanged.

## Object and method

- **Head.** Branch `research/optc-1230-1232-20261113`, fetched by name with no `--depth` and checked
  out in a detached worktree in the working area. HEAD is exactly
  `f4c300bc59ead434b7ad5e93cd5f9bcff58145db`, with parent `d015131d`.
- **Parent commit.** `d015131d` adds only `review/CONFIRM-r2.md`. That file is byte-identical to my
  CONFIRM-r2.
- **`main`.** `origin/main` is `c3b5f37a`.
- **Owner comments.** Read through the REST API: #1169 c.6854728636, c.6855167580, c.6863414487 and
  c.6865177667; #1274 c.6863419164; #1265 c.6846206075.
- **Other GitHub sources.**
  - Review 5895564670 was read through the API as well.
  - The #1169 comments since 14:00Z were searched for any record that replaces the #1230/#1232
    approvals.
  - Live heads and PR states were checked for #1274, #1230, #1232, #1271, #1221, #1231, #1268 and
    #1279.
  - The `Accountable Issue` lines of the #1231 and #1232 PR bodies were read.
- **Integration assessment.** At `c7ce4f28`, I read its review F7, F8, F9 and F11 and its §4 step 1.
- **Checks at the head.** The five cheap check scripts all report OK. Nothing else was run.

## 1. The commit changes no reviewed file

Confirmed. `d015131d..f4c300bc` adds only `STATUS.md` (214 lines) and `review/NOTES-STATUS.md`. A diff
of the reviewed files between `d015131d` and `f4c300bc` is empty: `NEW-RESULTS.md`,
`DEPENDENCIES.md`, `PROVENANCE.md`, `CHANGES.md`, and `review/REVIEW-r1.md`, `RESPONSE-r1.md` and
`CONFIRM-r2.md`.

## 2. Quotations, ids and times

All are verified.

- **Blob ids, SHA-256 values and line counts** of the four record files at `d015131d` match the table
  at `STATUS.md`:13–16:

  | File | Blob | SHA-256 | Lines |
  |---|---|---|---|
  | `NEW-RESULTS.md` | `1859e8c5…` | `7985076d…` | 627 |
  | `DEPENDENCIES.md` | `6c127b0a…` | `5213023f…` | 75 |
  | `PROVENANCE.md` | `3277a372…` | `e6bb9b65…` | 102 |
  | `CHANGES.md` | `8cc99cdf…` | `b8aab7e0…` | 70 |

  Each file was last changed at `4b40dcdc`.
- **Review files.** `REVIEW-r1` is blob `67e455ec`, added at `3f56d543`. `RESPONSE-r1` is `7be0bbdc`,
  added at `4b40dcdc`. `CONFIRM-r2` is `223af48d`, added at `d015131d`.
- **Commit ids.** `bac44eeb8562afe12142124c2df6a5192c3c5c67` resolves. The other commit ids in the
  table expand to the stated full SHAs.
- **Owner comments.** Authors (`amaybaum`), issues and creation times all match.
  - c.6854728636: 13:45:13Z, on #1169.
  - c.6855167580: 14:02:39Z, on #1169.
  - c.6863414487: 19:58:05Z, on #1169.
  - c.6865177667: 21:19:31Z, on #1169.
  - c.6863419164: 19:58:18Z, on #1274.
  - c.6846206075: 06:44:20Z, on #1265.

  Every quotation is verbatim apart from removed bold, which `STATUS.md`:63 declares. Each ellipsis
  replaces only intervening text.
- **Review 5895564670.** Author `amaybaum`, submitted 2026-11-13T17:44:35Z, commit `d015131d`. The
  verdict quotation at :29 is verbatim with the bold removed.
- **Line references into `NEW-RESULTS.md`.** :3–15, :11–15, :33–36, :215–224, :298–316, :358–365,
  :497–500 and :591–595 each point at the content `STATUS.md` names. The quotation at :82–85 is
  verbatim.

## 3. The integration requirements

The three items at `STATUS.md`:177–179 each match a line of review 5895564670 exactly, bold markup
included.

The account of how each is met does not overclaim:

- **Requirement 1.** The [A], [X] and [L] labels are in the unchanged `NEW-RESULTS.md`. Dynkin's
  theorem is recorded as [L] in row L(i).
- **Requirement 2.** The account says that no owner integration decision is recorded, and quotes
  "No merge." from c.6865177667. That is true.
  - It says the 2026-11-11 approvals were not recovered and that no #1169 record up to c.6865177667
    replaces them. That is also true: none of the eleven #1169 comments from c.6855167580 to
    c.6865237489 does so.
  - It says that neither the note nor a landing supplies those approvals.
  - It says that c.6855167580 authorizes the writer pass only.
  - It defers the merge-time checks to the final head and does not claim them. The drafting log
    records a mergeability probe and the CI state at `d015131d` but keeps both out of `STATUS.md`,
    which is correct.
- **Requirement 3.** No upgrade is made. AW-OA2-1 and the priorities are cited correctly to
  c.6855167580 and c.6865177667.

## 4. §A.46 and §A.27/§A.30

- **What the record supports.** Accurate except for row 3.1 and the matching clause of the claim
  sentence (finding 1). Each of the other rows uses the record's own labels and hypotheses. The
  claim sentence carries "each under the hypotheses stated with it" and the support layers, and the
  "Not established" list is complete.
- **Verification statuses.** Accurate. No result is independently verified. The decision whether
  model-written hand checks count as "partially verified" is left to OQ-10, and c.6865177667's OQ-10
  does cover §A.46 item 4. "None is known to be invalid" needs the scope note of finding 1.
- **Remediation lines.** One line per gap, each with a route and an accountable Issue. Sources for
  the Issue assignments are finding 3.
- **Landing basis.** Its later sentences state correctly that the #1265 practice is not §A.46 item
  2's literal text and that the question is before the owner (OQ-10). Its first sentence states the
  basis as settled (finding 2).
- **Register.** Neutral. There is no self-narration and no revision-history voice. The only hit for
  "currently" is inside the verbatim quotation of `NEW-RESULTS.md`:11–15. None of the barred path
  strings or the session-storage word appears in `STATUS.md` or `NOTES-STATUS.md`.

## 5. The superseded-lines list

The list is exact.

- **Stale lines.** Only row H (`DEPENDENCIES.md`:31) and `PROVENANCE.md`:17 are stale. Each names
  `cd38655c` as the REC-1 head "at (this) writing". The live head of `research/rec-1-1169-20261113`
  (#1268) is `3a3aa1465244565b9645e234e300d6ec191717a0`.
- **What still holds at the live head.** `REC-1-r7.md` is blob `f1ffac0e4a25…` at `9f7d2612`,
  `cd38655c` and `3a3aa146`, so row H's "unchanged to the branch head" holds.
- **Lines correctly not listed.**
  - The "open, draft" states: #1221, #1230, #1231, #1232 and #1271 are all open drafts.
  - The heads in `PROVENANCE.md` §1: `ea12fde1`, `86a413c8` and `703ae20e` are all live.
  - `PROVENANCE.md`:100, which assessment F8 judged accurate.
- **Matches the assessment.** Reducing the list to the time-indexed lines follows assessment F8.
  Adding `PROVENANCE.md`:17 is correct, because it carries the same fact as row H.

## 6. The writer's flags

1. **D3 also needs #1232 L2, which no planning record names.** Correctly handled at
   `STATUS.md`:137 and :140–141. The note states that OQ-2/OQ-3 names #1231 and #1232 L3 but not L2,
   and claims no authority for L2.
2. **Accountable Issues A1/D2/D3 → #1169, E2 → #868.** The assignments are right. Each is a sourced
   fact rather than a new planning decision:
   - the #1232 PR body reads "Accountable Issue: #1169";
   - the #1231 PR body reads "Accountable Issue: #868";
   - the record's standing paragraph names #1169.

   `STATUS.md` does not cite these sources (finding 3).
3. **`PROVENANCE.md`:17 added to the superseded lines.** Correct (§5 above).
4. **`d015131d` added to the own-branch commits.** Correct. It is the reviewed head, and review
   5895564670 and this note cite it.
5. **"Partially verified" left to OQ-10.** Acceptable and transparent (§4 above).
6. **"Ten should-fix" against eleven listed.** The writer is right: my REVIEW-r1 says "Ten
   should-fix items" but lists findings 2–12, which is eleven. Leaving the reviewed file unchanged is
   correct. `STATUS.md`:22–23 states the findings by number ("findings 1–12, finding 1 blocking, and
   nits 1–13"), not by count, which is accurate.

## Findings

### 1. G1 is restated as a universal over non-spanning frames, which is false (blocking)

**Where:** `STATUS.md`:75 (row 3.1), :92–93 (claim sentence) and :109 ("None is known to be
invalid"). The source sentence is `NEW-RESULTS.md`:322–323.

**Evidence.**

- `NEW-RESULTS.md`:322–323 reads: "The E_f verdict separates only on spanning frames (T3); on
  non-spanning frames the nonnegativity test does not separate (R3:59)".
- `STATUS.md` restates it in two places:
  - row 3.1: "on route E_f the nonnegative-frame test separates only on spanning frames";
  - the claim sentence: "on route E_f the nonnegative-frame test separates only on spanning frames".
- The support (S:278, R3:59) is two witnesses. On the octahedral frame (S2c) and the Husimi frame
  (S2), non-diagonal-preserving unitaries have nonnegative frame representatives. That supports
  "need not separate" and "the class is frame-relative". It does not support "does not separate on
  non-spanning frames", which is witness → universal.

**The universal is false.** Take the tetrahedral frame and add a fifth point that every state gives
probability zero:

- L(ρ)(k) = tr(ρ E_k) for k ≤ 4, with E_k = (1 + r_k·σ)/4, and L(ρ)(5) = 0.
- L is linear, injective and valued in probability measures.
- It does not span ℝ⁵, because the fifth coordinate is always zero.
- The image of L spans {x : x₅ = 0}. So every T with L∘E = T∘L has its first four columns fixed: they
  are the tetrahedral frame matrix of E, with a zero fifth row.
- For the Hadamard, take σ_j = (1,1,1) and σ_k = (−1,1,−1). Then σ_k·Hσ_j = −3, so
  F_kj = 1/4 − 3/4 = −1/2.
- Every frame representative of the Hadamard therefore has a negative entry, while the identity has a
  nonnegative one. On this non-spanning frame the test separates.

The copied draft sentence at `NEW-RESULTS.md`:290–292 ("without spanning … does not separate") is
correct only on its "need not separate" reading. It follows the two counter-structures, so that
reading is the natural one.

This defect is in the accepted text. My REVIEW-r1 and CONFIRM-r2 did not catch it.

**Fix (in `STATUS.md` only; the reviewed files stay unchanged).**

- **Row 3.1.** Replace the result cell with: "G1: on route E_f the nonnegative-frame test is
  separating under T3's spanning hypothesis; without spanning it need not separate: on the octahedral
  and Husimi frames, non-diagonal-preserving unitaries have nonnegative frame representatives, so the
  E_f classical class is frame-relative".
- **Claim sentence.** Replace "on route E_f the nonnegative-frame test separates only on spanning
  frames" with "on route E_f the nonnegative-frame test is separating under spanning and need not
  separate without it (octahedral and Husimi frames)".
- **Verification status.** Add a line to the verification-status section, which is the status
  artifact §A.30 and §A.46 item 4 provide for this:

  > **Scope of `NEW-RESULTS.md`:322–323.** "On non-spanning frames the nonnegativity test does not
  > separate" is shown for the octahedral and Husimi frames (S2c, S2). It does not hold for every
  > non-spanning frame. The tetrahedral frame extended by a point of probability zero is
  > non-spanning, and every frame representative of the Hadamard on it has the entry −1/2. The
  > supported statement is that without spanning the test need not separate.
- **":109".** Change it to read "No carried statement is known to be invalid at the scope of its
  witnesses; see the scope line on `NEW-RESULTS.md`:322–323."

Whether to correct `NEW-RESULTS.md`:322–323 itself is an owner question, since OQ-1 keeps the
reviewed files unchanged. It should be listed among the open owner points in the drafting log.

### 2. The landing basis is first stated as settled (should-fix)

**Where:** `STATUS.md`:202.

**Evidence.** The basis paragraph opens "The landing basis is the owner practice of #1265". Its own
:207–211 then say that the practice is not §A.46 item 2's literal text and that the relation is
before the owner (OQ-10). The opening sentence asserts what the rest leaves open.

**Fix.** Replace "The landing basis is the owner practice of #1265:" with "The proposed landing
basis, pending the owner's ruling under OQ-10 (c.6865177667), is the owner practice of #1265:".

### 3. The accountable-Issue assignments carry no source (should-fix)

**Where:** `STATUS.md`:133–138.

**Evidence.** The assignments are right, but the owner has not confirmed them. Under §A.45 rule 3's
maintenance clause, such entries may record "a sourced fact". The sources exist:

- the #1232 PR body: "Accountable Issue: #1169";
- the #1231 PR body: "Accountable Issue: #868";
- `NEW-RESULTS.md`:9: "The accountable Issue is #1169".

**Fix.** Add under the table: "Issue assignments are the drafts' own: #1232's PR body names #1169
(gaps D2, D3), #1231's names #868 (gap E2), and the record names #1169 (gap A1, `NEW-RESULTS.md`:9)."

### 4. Nits

1. **`STATUS.md`:169–171 reads ambiguously** ("The PR states in … hold"). Write instead: "The PR
   states recorded in `PROVENANCE.md` §1 and in rows A1, C, D1, E1 and I (#1221, #1230, #1231, #1232
   and #1271 are open drafts), and the branch heads of `PROVENANCE.md` §1 (`ea12fde1`, `86a413c8`,
   `703ae20e`), hold as measured for this note."
2. **"REVIEW-r1" is ambiguous in two places.** At `STATUS.md`:118 the T5(c) checks cell reads "RV:47–62;
   REVIEW-r1 against the Lean source", where RV is the reconciliation's review. At :110, "REVIEW-r1
   and CONFIRM-r2 report no mathematical error" means this package's reviews. Write
   `review/REVIEW-r1.md` in both places.
3. **`review/NOTES-STATUS.md`:5** says "Nothing committed, pushed or posted", which describes the
   drafting pass and not the committed state. If the log lands, mark it as drafting-time ("At
   drafting, nothing was committed …"). Separately, whether a drafting log is needed on `main` at all
   is a §A.28 question for the landing step.

## Summary against the six checks

1. **No reviewed file changed.** Confirmed.
2. **Quotations, ids and times.** All verified.
3. **Integration requirements.** Verbatim, with no overclaim. Requirement 2 states that no
   integration decision is recorded and that the approvals were not recovered.
4. **§A.46 and §A.27/§A.30.** Accurate apart from finding 1 (G1 scope) and finding 2 (basis stated
   as settled).
5. **Superseded lines.** Exact.
6. **Writer's flags.** All handled correctly. Flag 2 needs its sources cited (finding 3).

The register is neutral and no barred string appears.
