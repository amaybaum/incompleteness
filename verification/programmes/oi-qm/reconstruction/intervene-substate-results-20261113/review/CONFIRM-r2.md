# Focused confirmation of PR #1274 after review r1

**Verdict: ACCEPT.** Every finding of REVIEW-r1 is resolved as `review/RESPONSE-r1.md` states. Each
item applied in a different form is correct, and in findings 6 and 10 it corrects an error in my
own proposed fix. The π–λ hand check is sound. The diff from `3f56d543` contains only the stated
changes. No change alters a carried statement's mathematics, and none introduces an overclaim. One
optional nit is listed at the end. Merging remains a separate owner decision.

## Object

- Branch `research/optc-1230-1232-20261113`, fetched by name with full history and checked out in a
  detached worktree in the working area. HEAD is exactly
  `4b40dcdcb448815a7eb3aaee1c77a2317284f850`.
- The parent is `3f56d543`, whose parent is `1ef60d92`.
- `3f56d543` adds only `review/REVIEW-r1.md`, and that file is byte-identical to the review r1 I
  wrote.
- `3f56d543..4b40dcdc` changes only the four package files and adds `review/RESPONSE-r1.md`. No path
  outside the package directory changes.
- Checks at the head: `claims_check`, `staleness_check`, `voice_check`, `artifact_placement_check`
  and `legacy_records_check 4b40dcdc…`. All are OK. Nothing else was run.

## 1. Each finding against its disposition

- **1 (blocking).** Resolved.
  - The hand check is at `NEW-RESULTS.md`:215–224, and the support layer is updated at :254–255.
  - Row L(i) at `DEPENDENCIES.md`:36 is reclassified and closed. The former gap 3 is deleted.
  - The closing line now reads "No reference other than those of gaps 1–2 is a gap."
  - Nothing in the package is "owed before landing" any more.
- **2.** Resolved at :441–444. The sentence now keeps (vii) apart from the weaker affine restriction,
  as Main:724 does. Δ10's cells are updated at `CHANGES.md`:30.
- **3.** Resolved at :502–505. The sentence cites all three §A.29 requirements, which agrees with
  S:303 and S:309. Δ15 is updated.
- **4.** Resolved: the heading is at :129 and the "Draft statement … carried only in the conditional
  form" label at :131–132. The heading's form is discussed in §2.
- **5.** Resolved.
  - The opening statement's support is at :541–543, naming Main:366–381 and :401–404 (both checked
    at `c3b5f37a`).
  - Row L(iii)'s reference, claim and classification cells now agree with each other.
  - The Main row of the content table adds both ranges.
- **6.** Resolved at :309–313 (see §2).
- **7.** Resolved at :119–122. Every symbol of (Sep) is now defined, and the definitions agree with
  Bell-scope (Gen) and (Rec) at `e1534b08`:142–149.
- **8.** Resolved.
  - The NX-1 bullet at :100–101 copies I:123's defining clause verbatim.
  - The §3.1 *Hypotheses* text at :319–320 points to it.
  - Row A2 names it.
  - Δ28 records the two departures from I:123: the E_f clause is replaced by the spanning class
    (INC-1) and the route-C clause is dropped. No carried result uses route C's class.
- **9.** Resolved at :247 ("analogous to H-IND (the exact relation is not audited; I:299, R3:83)").
  Δ8 is updated.
- **10.** Resolved by deletion at :382–383 (see §2). Δ9 is updated.
- **11.** Resolved at :6–11.
  - The kernel targets match I:294 (T5(c)) and S:347 (E1, E2 item 4, L1).
  - The new sentence says the hand-checked steps "are cited at each result". The writer made this
    true by citing RV:70–71 at L1 (:424–425) and L4 (:463). RV:70–71 does check both against
    Main:362.
  - With those citations every review hand check of a carried result is cited at it:
    - T5: RV:48–60;
    - E2 item 4: RV:64–65;
    - G1/S2c: RV:66–67;
    - L1 and L4: RV:70–71.
  - E1 and (PAD)/S7 are not claimed as hand-checked in a review, and indeed were not.
- **12.** Resolved.
  - Each inserted or replaced phrase inside the SLL quotation is bracketed (:529–535).
  - The two table headers read "from S:…, with the changes of …" (:476, :490).
  - The convention sentence at :44–45 exempts only Δ1's re-pinned Main lines and Δ2's SM anchor. I
    found no other unbracketed in-quote change. The table cells are not quotations.
- **Nits 1–13.** All applied as listed. For nit 1, the (T5a) range I:159–166 is the right range for
  part (a): I:168 is part (b). The scope question stays with the owner.

## 2. The items applied in a different form

- **Finding 4 (heading).** The heading now reads "part (c), given (T5a) and (T5b): `InstAvail CM ↔
  InstAvail substratumClass` and `genTheory CM = substratumTheory`". It attaches both hypotheses to
  both statements, whereas the ↔ needs only (T5b). That makes the heading weaker than the carried
  form, never stronger, and the "Carried form" paragraph gives the exact split. The writer is right
  that my wording could be read as making the ↔ unconditional. Leaving "Carried form" where it is
  remains acceptable, because the new label already says the copied block is not the record's
  statement.
- **Finding 6 (factor 1/4).** The writer is right, and my proposed middle expression was wrong.
  - p_k(Rr) = (1 + r_k·Rr)/4 = 1/4 + (1/4) r_k·R(4 Σ_j p_j r_j).
  - Since Σ_j p_j = 1, which the check now states, this equals Σ_j p_j (1/4 + r_k·(R r_j)).
  - Uniqueness, now stated as "the vectors p(r) span ℝ⁴", is correct. p(r) is (1,1,1,1)/4 plus a
    vector of the three-dimensional space {(r_k·r)_k}. That space is orthogonal to (1,1,1,1), since
    Σ_k r_k = 0, and is injectively parametrized, since the r_k span ℝ³.
  - The minimum of −2/5 is unchanged.
- **Finding 10 (deletion option).** The writer is right that the row I proposed would have carried an
  unverified anchor. On `c3b5f37a`, `git grep "QP/U′"` over `verification/` finds nothing. My earlier
  pattern matched "U′" alone, so locating QP/U′ in the `bsel-2-*` records was wrong. Deleting the
  examples removes the references and changes no claim: the sentence restates E2's own full-domain
  hypothesis.
- **Finding 12 (convention sentence).** Correct, and its exemptions are complete.
- **Nit 10 (bracket option).** "§3.4 [§6 here]" at :494 now matches Δ19's convention, and Δ14 is
  updated.

## 3. The hand check of the measurability step

The hand check is sound. Write E_s for the section of E at s.

1. **Definition of 𝒟.** 𝒟 is the class of E ∈ 𝒮 ⊗ ℛ with every section E_s in ℛ and s ↦ κ(s, E_s)
   measurable. The writer's added clause, every E_s ∈ ℛ, makes the integrand defined before
   measurability is asked. That repairs an omission in my proposed text.
2. **Rectangles.** A rectangle A × B has section B for s ∈ A and ∅ otherwise, so it gives
   1_A(s)·κ(s, B), which is measurable. Hence Ω_S × R ∈ 𝒟.
3. **Proper differences.** For F ⊆ E, F_s ⊆ E_s and (E ∖ F)_s = E_s ∖ F_s ∈ ℛ. Then
   κ(s, E_s ∖ F_s) = κ(s, E_s) − κ(s, F_s), a difference of finite measurable functions.
4. **Increasing unions.** Sections commute with unions, and continuity from below of the measure
   κ(s, ·) gives a pointwise limit of measurable functions.
5. **Conclusion.** So 𝒟 is a λ-system. Rectangles form a π-system that contains Ω_S × R and generates
   𝒮 ⊗ ℛ. Dynkin's π–λ theorem gives 𝒮 ⊗ ℛ ⊆ 𝒟, and 𝒟 ⊆ 𝒮 ⊗ ℛ holds by definition.

The only external input is Dynkin's theorem, recorded as [L] in row L(i).

## 4. The diff from `3f56d543` contains nothing else

Every hunk of the four package files maps to a finding, a nit, or one of the two changes that
RESPONSE-r1 lists outside them:

- **The `CHANGES.md` header.** It adds "review r1" as a cited reason source.
- **Row C's dangling "(row M)".** Row C now points to the MECH-2 row of the content table. "(row M)"
  was already dangling at `1ef60d92`: no row M exists. The fix is correct.

The remaining `CHANGES.md` edits are the reason cells of Δ8, Δ9, Δ10, Δ14, Δ15, Δ16 and Δ20, all
corrected in place, plus the new rows Δ28 and Δ29. The `PROVENANCE.md` edits are nits 11–13. Every
fact they state checks:

- `703ae20e` has the single parent `1d3c4599`, whose parent is `b36bba60`.
- `cd38655c` is three commits after `9f7d2612`, adding P0 r1–r3 with their review, response and
  confirmation records, and `REC-1-r7.md` is unchanged between them.
- No #1169 comment between c.6854728636 and c.6855167580 records the decision c.6854728636 step 5
  asks for. The only other comment in that span is c.6854774010, the safeguards record.

## 5. Mathematics and overclaim

No carried statement or proof changed: T5(c), E1, E2, L4, (PAD), G1's argument and the A/B/C
classification are all as before.

The new text adds two things:

- a hand check (§3 above);
- definitions copied from their sources, for NX-1 and the symbols of (Sep).

It also narrows or re-attributes wording in a number of places: the heading, the label, the status
labels, the standing paragraph, the Δ8, Δ10 and Δ15 sentences, and the S4 wing direction. None of
these makes a statement stronger than before.

The (T5d) qualifier "(for |S| ≥ 2)" makes explicit a condition the witness already needed. The L4
*Hypotheses* line now matches L4's statement, which never used a finite V. Neither is an overclaim.

The register of the added `NEW-RESULTS.md` text is neutral throughout. It contains no self-narration,
no revision-history voice and none of the §A.32/§A.33 phrase families.

## Nit (optional)

- `DEPENDENCIES.md`:18 (row A1, closure cell) still describes the hypotheses' status as "argued in two
  drafts off `main`, hand-checked in RV:47–62". This is consistent with, but worded differently from,
  the labels at `NEW-RESULTS.md`:144–153. For uniformity it could read: "open on `main`; paper proofs
  off `main`; hand-checked in RV:47–62".
