# Status note: the option-(c) carried results of INTERVENE-1 and SUBSTATE-BRIDGE-1

This note gives the standing of the records in this directory. It does not change `NEW-RESULTS.md`,
`DEPENDENCIES.md`, `PROVENANCE.md`, `CHANGES.md` or any file in `review/`; their texts at
`d015131d6aad4ab09f80a7a78eb123384430186d` are the accepted texts.

## Accepted record and reviews

- **Record.**

  | File | Blob | SHA-256 | Lines |
  |---|---|---|---|
  | `NEW-RESULTS.md` | `1859e8c5cbb4d4d7af8f211df2e7e2b922ddc849` | `7985076d429b6fea8801b42783f006aa581705ee646589f54f9c6b81fc799828` | 627 |
  | `DEPENDENCIES.md` | `6c127b0af1823f8f73614728755d79e05a64a65b` | `5213023f49a1b06ad71090b6cb4b2685c56e3e81edac531c82d4238ea16ca25a` | 75 |
  | `PROVENANCE.md` | `3277a372eb680c89c2594dae4ee196d93bb876a8` | `e6bb9b65d63991cca8f0a66531354f2668458a242d632039f73efef30baa78a4` | 102 |
  | `CHANGES.md` | `8cc99cdf32bc380650f461ced4a1356ac82e2c21` | `b8aab7e040114dee00610c0ff743795d5c4d2809cbf426075caee4d3e5f761ca` | 70 |

  The four files were last changed at `4b40dcdcb448815a7eb3aaee1c77a2317284f850` and are unchanged
  at `d015131d`. The record pins `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`.
- **Review trail of this package (PR #1274).**
  - `review/REVIEW-r1.md` (blob `67e455ec`, committed at `3f56d543a0f15778c206e76cf82d1281ed02ef1f`):
    exact-head review of `1ef60d92d3484ae030bd186424066b579fd6a67c`, ACCEPT WITH CHANGES; findings
    1–12, finding 1 blocking, and nits 1–13.
  - `review/RESPONSE-r1.md` (blob `7be0bbdc`, committed at `4b40dcdc`): one disposition per finding
    and nit, applied in the same commit.
  - `review/CONFIRM-r2.md` (blob `223af48d`, committed at `d015131d`): focused confirmation of
    `4b40dcdc`, ACCEPT, with one optional nit (`DEPENDENCIES.md`:18), which is not applied.
  - ChatGPT review 5895564670 (posted under `amaybaum`, 2026-11-13T17:44:35Z) at the exact head
    `d015131d`: "ACCEPT as a scoped research-evidence package, with separate integration gates."
  - The reviews of the drafts and of the reconciliation (#1271) are listed in `PROVENANCE.md` §2–§3.
- **Nature of the reviews.** All are model-written. REVIEW-r1 and CONFIRM-r2 are exact-head reviews
  separate from the writer pass; review 5895564670 is a model review posted under the owner's
  account. None is a human review, a GitHub approval or an owner decision, and none is verification
  (§A.46 item 7).

## Owner records

- **Option (c).** #1169 comment 6854728636 (`amaybaum`, 2026-11-13T13:45:13Z): "INTERVENE-1 (#1230)
  and SUBSTATE-BRIDGE-1 (#1232): "Adopt (c) (Recommended)" (amaybaum, 2026-11-13)." Step 3: "A
  minimal landing package containing only the results not already on `main`." Step 5: "A current
  owner decision to replace the 2026-11-11 approvals cited in both PR bodies, which could not be
  located." Also: "Results already on `main` are referenced, not duplicated. … Merging is a
  separate decision."
- **Carried set.** #1169 comment 6855167580 (`amaybaum`, 2026-11-13T14:02:39Z): "Corrected set
  (Recommended)". "It replaces the landing list in c.6854728636". The package carries "INTERVENE-1
  T5 part (c) only", "SUBSTATE-BRIDGE-1 G1/E2, and E1's generality", "L1/L4 for infinite site
  groups", "The A/B/C Bell-route classification, with SLL kept as an open obligation" and "(NS_A),
  with its countercontrol S7"; T7(b) is excluded. "Merging is a separate owner decision. AW-OA2-1
  stays stopped, and priorities are unchanged."
- **Assessment.** #1169 comment 6863414487 (`amaybaum`, 2026-11-13T19:58:05Z), item 1: "It
  prepares the smallest landing changes, starting with #1274 and the REC-1 housekeeping. … It
  grants no merge authority: each landing remains a separate owner decision."
- **Scope.** #1274 comment 6863419164 (`amaybaum`, 2026-11-13T19:58:18Z): "The accepted option-(c)
  package stays narrowly scoped. It is T5 part (c) only, as #1169 c.6855167580 fixes it." "Whether
  to carry the short proofs of T5(a), (b) and (d), and so close gap A1, will be assessed
  separately. That assessment will not delay this package's preservation."
- **This note.** #1169 comment 6865177667 (`amaybaum`, 2026-11-13T21:19:31Z), OQ-1: "Prepare a
  `STATUS.md` for #1274, and only that. The reviewed files stay unchanged. It then gets a focused
  check and a ChatGPT exact-head review. No merge." OQ-10: "Write a short paper-only note on how
  the #1265 landing practice relates to §A.46 items 1, 2 and 4, for an owner ruling." And: "None of
  these decisions authorizes a merge, adopts a premise, or changes a priority or the board."

Emphasis is removed from the owner quotations above.

## What the record supports, and at what strength

The record states its results as "research records, not established claims (§A.46 items 1 and 3)"
(`NEW-RESULTS.md`:3–15). Each is a paper argument [A], not kernel-checked, conditional on the
hypotheses stated with it. Its evidence tags (`NEW-RESULTS.md`:33–36) are the strengths used here.

| § | Result | Strength in the record |
|---|---|---|
| 1 | T5(c): given (T5b), `InstAvail CM ↔ InstAvail substratumClass`; given (T5a) and (T5b), `genTheory CM = substratumTheory` | [A], conditional on (T5a), (T5b), open on `main`; the FI-1 headline also needs (T5d) and is not asserted |
| 2 | E1: the induced sub-Markov kernel, with no measure invariance, no finiteness of the hidden carrier, adaptive stopping and a ⊥ outcome | [A]; measurability step hand-checked from Dynkin's π–λ theorem [L]; an upper bound, no operation exhibited |
| 3.1 | G1: on route E_f, under T3's spanning hypothesis the frame matrix is unique and the class is fixed by the map; without spanning the test need not separate: on the octahedral and Husimi frames non-diagonal-preserving unitaries have nonnegative frame representatives, and on the Husimi frame every unitary does | [A]; each [X] number hand-checked in the record |
| 3.2 | E2: under one linear encoding of every density matrix shared by all procedures, native procedures are jointly measurable, and sharp ones commute | [A]; scope as stated (no context-dependent, non-linear or restricted-domain encoding); an upper bound |
| 4.1 | L1: tower locality for a finite site set with arbitrary site alphabets | [A] on Main:362 [P] |
| 4.2 | L4: the dependency relation of an affine update on abelian site groups is the same for every non-empty state set | [A], one line of algebra |
| 5 | Routes A/B/C under measurement independence; requirements N1–N4; SLL | [A] classification; N1–N4 not supplied; SLL open; N2 conditional on L3; SLL's exclusion consequence conditional on L2 and Theorem N |
| 6 | (NS_A); (PAD) ⇒ (NS_A) for the triple; countercontrol S7 | definition; [A]; S7 hand-checked; no OI hypothesis used |

The record also states: "None supplies an operation that is physically reachable under the
currently demonstrated OI premises (REC-1 Q2-F or Q2-P); the constructive items are definable or
representable (Q2-A), and the remainder are upper bounds, classifications, a definition with a
countercontrol, and an open obligation" (`NEW-RESULTS.md`:11–15).

**Claim supported by this record:** "For the option-(c) results of INTERVENE-1 and
SUBSTATE-BRIDGE-1, each under the hypotheses stated with it: given (T5b),
`InstAvail CM ↔ InstAvail substratumClass`, and given (T5a) and (T5b),
`genTheory CM = substratumTheory`; for a procedure kernel independent of the input law (H-IND) on a
measurable hidden carrier, the law of (output, outcome) is given by a sub-Markov kernel, without
measure invariance or finiteness and with adaptive stopping and a ⊥ outcome; on route E_f the
nonnegative-frame test has a unique frame matrix under spanning and need not separate without it
(octahedral and Husimi frames), and under one full-domain linear encoding shared by all procedures
the native procedures are jointly measurable; L1 and L4 hold for arbitrary
site alphabets and abelian site groups at their stencil and affine scope; with measurement
independence kept, routes A, B and C classify how parameter dependence can be carried, with N1–N4
not supplied and SLL an open obligation; and (PAD) gives (NS_A) for the law and triple it is
verified for, while S7 shows that invariance of the unconditional law does not (paper arguments
[A], hand-checked and model-reviewed, not kernel-checked or independently verified; [X] numbers
hand-checked in the record, the probe being provenance; Dynkin's π–λ theorem and Bell's theorem
for a measurable λ imported [L]; no physically reachable operation; no manuscript claim affected)."

**Not established.** T5's unconditional headline "FI-1 is not theory-invariant" (gap A1); N2's
necessity (gap D2); SLL's exclusion-branch consequence (gaps D3, E2); any physical operation, Bell
mechanism or OI↔QM result; the #1230 and #1232 drafts themselves.

## Verification status (§A.46 item 4)

No result in the record is independently verified. No carried statement is known to be invalid at
the scope of its witnesses; see the scope line on `NEW-RESULTS.md`:332–335 and `CHANGES.md` Δ30.
`review/REVIEW-r1.md` and `review/CONFIRM-r2.md` report no mathematical error in a carried statement
or proof. N1–N4 and SLL are open.
Whether hand checks in model-written reviews make a result partially verified in §A.46 item 4's
sense is not decided here; it is part of the question before the owner (OQ-10). [A] items are paper
arguments, hand-checked and model-reviewed, not independently verified; [L] items are imported
standard mathematics; [K] items are Lean statements on `main`, read and not rebuilt.

| § | Result | Status | Checks recorded (model-written, not verification) | Verification route |
|---|---|---|---|---|
| 1 | T5(c) | not independently verified; conditional on (T5a), (T5b) (gap A1) | RV:47–62; `review/REVIEW-r1.md` against the Lean source | kernel target (I:294) or independent non-model review |
| 2 | E1 | not independently verified | hand check in `NEW-RESULTS.md`:215–224; CONFIRM-r2 §3 | kernel target (S:347) or independent non-model review |
| 3.1 | G1 | not independently verified | RV:66–67; hand checks in `NEW-RESULTS.md`:298–316 | independent non-model review |
| 3.2 | E2 | not independently verified | item 4: RV:64–65; S3 and Husimi bound: `NEW-RESULTS.md`:358–365 | item 4 a kernel target (S:347); independent non-model review |
| 4.1 | L1 | not independently verified | RV:70–71 | kernel target (S:347) or independent non-model review |
| 4.2 | L4 | not independently verified | RV:70–71 | independent non-model review |
| 5 | A/B/C, N1–N4, SLL | classification not independently verified; N1–N4 and SLL open; N2 and SLL's exclusion consequence conditional (gaps D2, D3, E2) | S4 arithmetic: `NEW-RESULTS.md`:497–500; consistency with Main:362, :412, :414 (R3:68) | independent non-model review; the gaps below |
| 6 | (NS_A), (PAD), S7 | not independently verified | S7 arithmetic: `NEW-RESULTS.md`:591–595 | independent non-model review |

"I:n", "S:n", "R3:n" and "RV:n" are the line conventions of `NEW-RESULTS.md` ("Pins"). RV is the
reconciliation's `REVIEW-r1.md` at `703ae20e` (#1271), off `main`; it is provenance
(`DEPENDENCIES.md` row I).

**Scope of `NEW-RESULTS.md`:332–335.** The sentence states that without spanning the test need not
separate, as on the octahedral and Husimi frames (S2c, S2). Non-separation does not hold for every
non-spanning frame: the tetrahedral frame extended by a point of probability zero is non-spanning,
and every frame representative of the Hadamard on it has the entry −1/2 (`CHANGES.md` Δ30; owner
decision #1274 c.6865575359). The copied Finding and Argument of §3.1 carry the same scope, stated
in the scope line at `NEW-RESULTS.md`:302–310 (`CHANGES.md` Δ31; owner decision 2026-11-14, #1169
c.6872005186).

**Remediation, one line per gap** (`DEPENDENCIES.md` rows A1, D2, D3, E2):

| Gap | What is missing | Remediation | Accountable Issue |
|---|---|---|---|
| A1 | (T5a), (T5b), (T5d), argued in APPROX r4a C1–C3 (#1221) and INTERVENE I:159–168, I:179, off `main` | the separate assessment of T5(a), (b) and (d) (#1274 c.6863419164): carry the short proofs in a follow-on package, or land #1221 through its own gates; either closes A1 for the research record only | #1169 |
| D2 | L3 (S:167–171), on which N2's necessity rests | land #1232 L3 through its own gates (#1169 c.6865177667, OQ-2/OQ-3) | #1169 |
| D3 | L2 (S:153) and class (a)3 (S:263), on which SLL's exclusion consequence rests | land #1232 L2 with class (a)3 through its own gates, together with Theorem N (gap E2) | #1169 |
| E2 | Bell-scope r2 Theorem N and 𝒞_sep (#1231) | land #1231 through its own gates (#1169 c.6865177667, OQ-2/OQ-3) | #868 |

Issue assignments are the drafts' own: #1232's PR body names #1169 (gaps D2, D3), #1231's names #868
(gap E2), and the record names #1169 (gap A1, `NEW-RESULTS.md`:9).

c.6865177667 records OQ-2/OQ-3 as "a planning record only; nothing starts from it". It names #1231
and #1232 L3; it does not name #1232 L2.

## Dependencies

`DEPENDENCIES.md` traces every off-`main` reference of `NEW-RESULTS.md` (rows A1–L) under §A.42
item 8. The references this note adds:

| Reference | Classification |
| --- | --- |
| Commits `bac44eeb8562afe12142124c2df6a5192c3c5c67`, `1ef60d92`, `3f56d543`, `4b40dcdc` and `d015131d` on this PR's branch, named in the reviews and in review 5895564670 | Support on `main` once this PR lands by merge commit, which keeps them ancestors of `main`. |
| #1169 comments 6854728636, 6855167580, 6863414487, 6865177667; #1274 comment 6863419164; #1265 comment 6846206075 | Governance provenance, quoted above and under "Landing". |
| ChatGPT review 5895564670 | Provenance: its integration requirements are quoted below; no claim rests on it. |
| Integration assessment r2, `verification/audits/integration/integration-assess-20261113/INTEGRATION-ASSESS-r2.md` on `research/integration-assess-20261113` at `c7ce4f2852cb90883b7a7c8ed645ba09db19f7ca` (#1279), with its `REVIEW-r1.md` and `CONFIRM-r2.md` | Provenance: it specifies the contents of this note; no claim rests on it. |
| #1221, #1231, #1232 in the remediation table | Provenance: remediation routes; no claim rests on them. |

## Source drift from `c3b5f37a` to `main` (`c3b5f37a`)

None: the record's pin is the `main` commit against which this note is measured.

## Superseded lines in the accepted text

- `DEPENDENCIES.md`:31 (row H), "the branch head is `cd38655c` at this writing, three later
  commits, P0 r1 to r3 with their review and confirmation records", and `PROVENANCE.md`:17, "that
  branch's head is `cd38655c` at writing": the head of `research/rec-1-1169-20261113` (#1268)
  measured for this note is `3a3aa1465244565b9645e234e300d6ec191717a0`. `REC-1-r7.md` is blob
  `f1ffac0e4a254536930acf2afd56e40c32597c51` at `9f7d2612`, `cd38655c` and `3a3aa146`, so row H's
  statement that `REC-1-r7.md` is unchanged to the branch head holds at `3a3aa146`.

The PR states recorded in `PROVENANCE.md` §1 and in rows A1, C, D1, E1 and I (#1221, #1230, #1231,
#1232 and #1271 are open drafts), and the branch heads of `PROVENANCE.md` §1 (`ea12fde1`,
`86a413c8`, `703ae20e`), hold as measured for this note.

## Integration requirements (review 5895564670)

Quoted from the review:

> 1. An ACCEPT by a model is not independent mathematical verification (§A.46). The [A]/[X] and [L] support labels must remain on any resulting main record. External Dynkin's π–λ theorem is used as a standard imported mathematics fact, not a claim of Lean formalization.
> 2. Confirm the actual merge-time dependency/CI/mergeability checks and the **current owner integration decision** separately. The original draft approval records for #1230/#1232 were not recovered; the current option-(c) writer authorization is not a retrospective authorization of those drafts nor permission to merge them.
> 3. Avoid upgrades of the Q2-A/upper-bound classifications to an OI physical mechanism, Bell escape or OI↔QM result. Keep AW-OA2-1 stopped and the Bell-first priorities unchanged.

How each is met:

1. The [A], [X] and [L] labels are in `NEW-RESULTS.md` (standing paragraph, evidence tags and each
   *Support layer* paragraph), which is unchanged. This note describes the support in the same
   labels and adds none. Dynkin's π–λ theorem is recorded as [L] in `DEPENDENCIES.md` row L(i).
2. The merge-time checks (CI at the final head, mergeability with `main`, and the head of row H)
   are made at the final head, separately from this note. No owner integration decision is
   recorded: c.6865177667 reads "No merge." The 2026-11-11 approvals cited in the #1230 and #1232
   PR bodies were not recovered (`PROVENANCE.md` §4), and no owner record on #1169 up to
   c.6865177667 replaces them. Neither this note nor a landing supplies them, and c.6855167580
   authorizes the writer pass, not those drafts or a merge.
3. This note keeps the record's Q2-A and upper-bound classifications as stated and adds no
   mechanism, Bell escape or OI↔QM result. AW-OA2-1 stays stopped and priorities are unchanged
   (c.6855167580; c.6865177667).

## Landing

- **Mode.** Merge commit (neither squash nor rebase), so that the commits the reviews name and the
  reviewed head `d015131d` remain ancestors of `main`. The reviews cite those commits by id, and a
  squash or rebase would leave them off `main` (§A.42 items 2 and 3). The branch commits carry
  "(WIP)" in their messages; those were labels on the working checkpoints.
- **Basis.** The proposed landing basis, pending the owner's ruling under OQ-10 (c.6865177667), is
  the owner practice of #1265: #1265 comment 6846206075
  (`amaybaum`, 2026-11-13T06:44:20Z), "one status note per unit … naming the claim it supports",
  applied in `oa-1-20261112/STATUS.md`, "Landing". Under that practice a record lands as the
  evidence for the scoped claim it states, at the strength stated; here that is the claim above,
  and option (c) was chosen as "a minimal landing package" (c.6854728636). The practice is not
  §A.46 item 2's literal text. Under the literal text (evidence an established claim needs, or
  evidence needed for reproducibility or to support records already on `main`) the record does not
  qualify: it states its results as research records, not established claims, and no record on
  `main` has an item 8 gap that it closes. How the #1265 practice relates to §A.46 items 1, 2 and 4
  is before the owner for a ruling (c.6865177667, OQ-10); this note does not decide it.
- **Accountable Issue.** #1169. T5(a), (b) and (d) are assessed separately (#1274 c.6863419164).
- **Owner record.** No merge decision is recorded. Merging is a separate owner decision
  (c.6854728636; c.6855167580; c.6863414487; c.6865177667).
