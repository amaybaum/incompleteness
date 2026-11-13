# Exact-head review of PR #1274 (option-(c) landing package), r1

**Verdict: ACCEPT WITH CHANGES.**

No mathematical error was found in any carried statement or proof, and every proof marked "copied"
(T5(c), E1, E2, L4, (PAD)) matches its source steps. One item is blocking because the package itself
records it as owed before landing (finding 1). Ten should-fix items are wording or dependency-record
defects. Each one makes a statement stronger than its support, misdescribes a `main` anchor or
leaves an off-`main` dependency unlisted. All of them close by the text replacements given below,
and none needs a new derivation. The nits are optional. Merging remains a separate owner decision.

## Object and method

- PR #1274, branch `research/optc-1230-1232-20261113`. It was fetched by name and checked out in a
  detached worktree in the working area. HEAD is exactly `1ef60d92d3484ae030bd186424066b579fd6a67c`
  (parent `bac44eeb`). The diff against `origin/main` touches only the four files of
  `verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/`.
- `origin/main` is `c3b5f37a354bb26437e2e0165c576a347a63c153`, the package's pin.
- Sources read at their pins:
  - INTERVENE-UNIT1.md at `ea12fde1` (blob `06f148e0…`, sha256 `5edb4ad3…`);
  - SUBSTATE-BRIDGE-UNIT1.md at `86a413c8` (blob `9ff0f077…`, sha256 `662b9cba…`);
  - the probe `generic_substate_checks.py` (sha256 `d269224f…bbb99`);
  - RECONCILE-r3, REVIEW-r1 and CONFIRM-r2 at `703ae20e`;
  - Bell-scope r2 at `e1534b08`, APPROX r4a at `e41cf613`, BRIDGE-UNIT1 at `820519cf`, REC-1 r7 at
    `9f7d2612`.

  All hashes match `PROVENANCE.md`. Every branch head named in `PROVENANCE.md` §1 is still the live
  head, except `research/rec-1-1169-20261113`, which is now at `cd38655c`; `REC-1-r7.md` is unchanged
  from `9f7d2612` to `cd38655c`.
- The owner comments #1169 c.6854728636 and c.6855167580, and reviews 5857985732, 5859960068 and
  5892291246, were read through the REST API. Every quotation of them in the package is accurate.
- Lean anchors were read at `c3b5f37a`. `InstAvail` is at :268 and its `op` constructor requires a
  square K with Kᴴ K = 1 (:270–272). The other anchors are at the cited lines: `instAvail_mono` :305,
  `LabelInvariant` :364, `Architecture` :506–516, `realized_of_instAvail` :530 and `genTheory` :852
  (ImplementationLocality); `substratumClass` :180, `substratumClass_arch` :231 and
  `substratumClass_labelInvariant` :275 (StructuralClosure); `substratumTheory` (RouteB:284);
  `IsMonomial` :75 and `preservesDiag_conj_of_monomial` :126 (SubstratumInterface); `PreservesDiag`
  (DiagonalTheory:68); `ColMonomial` :651 and `preservesDiag_conjChannel_of_colMonomial` :654
  (SubstantiveCensus); `exists_nonMonomial_of_layerFlowExecutable` (ExecSource:52); `waveStep` :32 and
  `project_waveStep` :56 (NativePadicReduction); `nonnegClass_nonnegBounded` (F2CoherenceControls:173).
- Every `Main:n` anchor carries the stated text: 42, 48, 58, 360, 362, 412, 414, 416, 423, 558, 562,
  590, 718 and 724. Main:362's linear-update clause, Main:414's window
  Δt/√3 < d ≤ Δt/‖n̂‖₁ and Main:724's items (vii), (viii), (x) and (xiv) were all checked. So were
  GR:266, Substratum:131–133, SM:112 (and SM:112 at `cac5d264`), and every `verification/` file:line
  anchor in `DEPENDENCIES.md`.
- The uniform −2 line shift after line 4 of `papers/Main.md` was confirmed by comparing
  `cac5d264` with `c3b5f37a`. The RS/, CS/, MECH-2 and `oi-qm-ext-1` files cited are unchanged
  between those commits.
- Checks run at the head: `claims_check`, `staleness_check`, `voice_check`,
  `artifact_placement_check` and `legacy_records_check 1ef60d92…`. All are OK. Nothing else was run.
  Every [X] number was re-derived by hand: S2, S2b (minimum −2/5 at σ_k = (1,−1,−1), σ_j = (1,1,1)),
  S2c, S3 (|v|² = 1/16), the Husimi bound 1/4, S4 (CHSH = 4) and S7 (1 and 3/4; the control gives 1/2).
  So were T5(c) against the Lean source, E1, E2 items 1–4, L4 and (PAD).

## Findings

### 1. The kernel-measurability step of E1 is acknowledged as owed before landing (blocking)

**Where:** `DEPENDENCIES.md`:36 (row L(i)), :74 (gap 3); `NEW-RESULTS.md`:195–196, :228–229.

**Evidence.** Row L(i) reads: "A citation to a standard measure-theory text for the measurability of
s ↦ κ(s, E_s) on product-measurable E is owed before landing; no text change is made here." The
package therefore records that it is not yet landable. Under the Code Review Rules, an external
input is permissible only when its role, status and independent support are explicit. E1 is a
carried result, and this step is one of its links.

**Fix.** Close it in the package. The cheapest closure is a hand check, consistent with the
package's other hand checks, so that no unread citation is needed. Insert after `NEW-RESULTS.md`:198:

> *Hand check of the measurability step (this record).* Let 𝒟 be the class of E ∈ 𝒮 ⊗ ℛ for which
> s ↦ κ(s, E_s) is 𝒮-measurable. A rectangle A × B gives 1_A(s)·κ(s, B), which is measurable because
> κ is a kernel. 𝒟 is closed under proper differences, since κ(s, ·) is finite and additive, and
> under increasing unions, by countable additivity and monotone limits. Rectangles form a π-system
> generating 𝒮 ⊗ ℛ, so 𝒟 = 𝒮 ⊗ ℛ by Dynkin's π–λ theorem.

Then make two changes:

- In `DEPENDENCIES.md`:36, replace the closure cell for (i) with: "(i) Closed by the hand check
  after the E1 proof (π–λ argument); Dynkin's π–λ theorem is standard [L]."
- Delete gap 3 at :74, and change "No other reference is a gap." to follow from gaps 1–2 only.

If a citation is preferred instead, it must be read first-hand before it is cited, since [L] means
"recalled, not read first-hand".

### 2. Δ10 misdescribes ledger item (vii) (should-fix)

**Where:** `NEW-RESULTS.md`:413–415; `CHANGES.md`:29 (Δ10).

**Evidence.** Main:724 reads: "(vii) linearity of the substratum update (A5), stronger than the
affine restriction that amplitude-scale gauge invariance yields in the form that every first
difference of the update is independent of its base point". The first-difference form is that of
the weaker affine restriction.

- The draft (S:157) kept the two apart: "with the affine form glossed as …".
- The package reads: "Item (vii) is "linearity of the substratum update (A5)", in the form that
  "every first difference …"". This makes (vii) itself the first-difference (affine) condition.

Δ10 does not record this change of meaning, and `CHANGES.md`:62–67 states that no change alters a
statement. No carried conclusion changes, because linear updates are affine and L4 covers affine
updates. The description of a `main` premise is nonetheless wrong.

**Fix.** Replace `NEW-RESULTS.md`:413–415 from "Item (vii) is" with:

> Item (vii) is "linearity of the substratum update (A5)", which Main:724 states as stronger than the
> affine restriction "that every first difference of the update is independent of its base point";
> L4 needs only the affine form.

Update the package-text cell of Δ10 to match.

### 3. Δ15 attributes N1–N4's failure to the wrong §A.29 clause and cites S:309 for it (should-fix)

**Where:** `NEW-RESULTS.md`:473–475; `CHANGES.md`:34 (Δ15).

**Evidence.** The package says: "No one of them meets §A.29's demand for an independent prediction
and independent controls (S:309)." The draft says otherwise:

- S:309 reads: "No row meets all three §A.29 requirements. N3 is the only one with an independent
  reason and an own consequence".
- S:303 records N3's *I* column as "yes, one: signalling for an observer of finer resolution, or for
  non-Haar preparations of the unresolved digits". N3 fails on *V*, adjustability.

The package sentence therefore contradicts the source it cites for N3.

**Fix.** Replace the second sentence at :473–475 with:

> No one of them meets all three §A.29 requirements (controls preserved, an independent prediction,
> not adjustable to fit any outcome; S:309), and none supplies the independent controls a Bell or
> quantum mechanism would need.

Amend Δ15's package-text cell to match.

### 4. §1 displays T5's unconditional headline and equality as its statement (should-fix)

**Where:** `NEW-RESULTS.md`:118, :120–126; `DEPENDENCIES.md`:18 (row A1).

**Evidence.** The section heading asserts `genTheory CM = substratumTheory`. The "Statement
(copied)" block opens with "**T5 (FI-1 is not theory-invariant).**" and ends with "So `genTheory CM`
= `substratumTheory` … on every carrier". Both need (T5a) and (T5b), and the headline also needs
(T5d), none of which the package carries (row A1). Row A1 says: "The unconditional headline "FI-1 is
not theory-invariant" is not asserted by the package." As laid out, the block reads as the record's
statement, and the conditional "Carried form" follows it (assert-then-qualify).

**Fix.**

- Heading at :118: "## 1. INTERVENE-1 T5, part (c): `InstAvail CM ↔ InstAvail substratumClass`, and
  `genTheory CM = substratumTheory` given (T5a), (T5b)".
- Label at :120: "**Draft statement (copied; I:157, I:170, I:177); the record carries it only in the
  conditional form below.**"
- Optionally, move "Carried form" (:140–144) directly under the heading.

### 5. §5's opening statement uses Bell's theorem, which no dependency row lists (should-fix)

**Where:** `NEW-RESULTS.md`:442–445, :511–516; `DEPENDENCIES.md`:36 (row L(iii)), :58.

**Evidence.** "With measurement independence kept, a deterministic completion exceeds the Bell bound
only through parameter dependence" is Bell's theorem under determinism and MI.

- For finite Ω it is on `main` at Main:366–381 (the theorem) and Main:401–404 ("gives up at least
  one of two remaining hypotheses …").
- For the measurable λ of a substate carrier it is the [L] input.

Row L(iii) says Bell's theorem is "carried only inside the conditional of rows D3/E2". That is
incorrect, because the A/B/C classification itself uses it. The `main` content table at :58 omits
Main:366–381 and :401–404.

**Fix.**

- Add to `NEW-RESULTS.md`'s §5 *Hypotheses carried* (:511): "The opening statement is Bell's theorem
  under determinism and MI: Main:366–381, :401–404 [P] for finite Ω; for a measurable λ it is the
  standard extension [L] (`DEPENDENCIES.md` row L(iii))."
- In row L(iii), change "(iii) carried only inside the conditional of rows D3/E2" to "(iii) used by
  §5's opening statement for a measurable λ (on `main` for finite Ω, Main:366–381, :401–404) and
  inside the conditional of rows D3/E2".
- Add ":366–381, :401–404" to the Main row at :58.

### 6. The S2b hand check takes its frame-matrix formula from the off-`main` probe (should-fix)

**Where:** `NEW-RESULTS.md`:283–288; `DEPENDENCIES.md`:35 (row X).

**Evidence.** The S2b hand check reads: "the frame matrix is F_kj = 1/4 + r_k·(R r_j) (probe lines
137–142)". That formula is derived only in the probe's comments, at `86a413c8`, off `main`. The
frame (p_k(r) = (1 + r_k·r)/4, E_k = (1 + r_k·σ)/4) is first stated in the S3 hand check further
down. The S2b number therefore rests on content that row X classifies as provenance. The formula
itself is correct. Σ_j r_j r_jᵀ = I for the four even-sign vectors (±1/2)³, so r = 4 Σ_j p_j r_j
and p_k(Rr) = Σ_j p_j (1/4 + r_k·R r_j). The minimum −2/5 was re-derived by hand.

**Fix.** Replace "With r_k = σ_k/2, σ_k ∈ {±1}³ of even sign product, the frame matrix is
F_kj = 1/4 + r_k·(R r_j) (probe lines 137–142)." with:

> The tetrahedral frame is p_k(r) = (1 + r_k·r)/4, that is E_k = (1 + r_k·σ)/4, with r_k = σ_k/2 and
> σ_k ∈ {±1}³ of even sign product. Then Σ_k r_k r_kᵀ = I and Σ_k r_k = 0, so Σ_k p_k r_k = r/4 and
> p_k(Rr) = 1/4 + r_k·R(4 Σ_j p_j r_j) = Σ_j p_j (1/4 + r_k·(R r_j)): the frame matrix is
> F_kj = 1/4 + r_k·(R r_j), unique because the four frame points span.

### 7. (Sep) is quoted without its symbols, so row E1's self-contained closure is incomplete (should-fix)

**Where:** `NEW-RESULTS.md`:109–111; `DEPENDENCIES.md`:25 (row E1).

**Evidence.** `G_B`, `R_A^t`, `t_s`, `T_A` and `d_{G_φ}` are not defined anywhere in the package.
Bell-scope defines them in (Gen) and (Rec), at `BELL-SCOPE-UNIT1.md`:142–149 at `e1534b08`.

**Fix.** Append to the (Sep) bullet:

> Here `G_A, G_B ⊂ V` are the disjoint generator regions whose content at the setting time `t_s`
> fixes the settings, `R_A^t` is the region from which wing A's complete record reads at time
> `t ∈ [t_s, T_A]`, and `d_{G_φ}` is graph distance in Main's coupling graph (Main:362) (Bell-scope
> r2 (Gen), (Rec), [D]).

### 8. NX-1 is used but not stated, so row A2's closure does not cover it (should-fix)

**Where:** `NEW-RESULTS.md`:94, :242–243, :290–292; `DEPENDENCIES.md`:19 (row A2).

**Evidence.** §3.1 *Hypotheses* says: "The verdict they qualify, NX-1 on route E_f, is the one of
§0.3". §0.3 states the E_f class and T3, but neither NX-1 nor an NX-1 verdict. Row A2 says "§0.3
states the E_f classical class in full … No carried result uses any other part of NX-1's
definition". G1's marker and §3.1 do use NX-1, at least as the verdict being qualified.

**Fix.** Add a bullet to §0.3, from I:123, which is copied and so provenance:

> **NX-1** (I:123): "some valid native procedure induces a transformation at an ε-independent positive
> distance from the route's classical class"; on E_f the class is the one above.

At :290–292, replace "is the one of §0.3" with "is NX-1 on route E_f as defined in §0.3".

### 9. "A fixed lift in the role of H-IND" asserts an unaudited identification (should-fix)

**Where:** `NEW-RESULTS.md`:220–222 (Δ8); `CHANGES.md`:27.

**Evidence.**

- REVIEW-r1 finding F (RV:154–155) flags "H-IND plays the role of a fixed lift" as an identification
  that INTERVENE leaves unaudited (I:299).
- The reconciliation accordingly says "analogous to a fixed lift … the exact relation is not
  audited" (R3:83).
- The package's own §0.1 row also says "Analogous … the exact relation is not audited".

Δ8 uses the stronger wording. Under the Code Review Rules (Bridge and no-go scope), no
identification may be made without a formal map.

**Fix.** Replace "with a fixed lift in the role of H-IND" with "with a fixed lift, analogous to H-IND
(the exact relation is not audited; I:299, R3:83)".

### 10. Δ9 names off-`main` and on-`main` records that `DEPENDENCIES.md` does not list (should-fix)

**Where:** `NEW-RESULTS.md`:354–357; `DEPENDENCIES.md` (no row).

**Evidence.** The added sentence attributes restricted-domain encodings to "MECH-1, QP/U′ and
Q-868-H". These are references not traced under §A.42 item 8:

- Q-868-H r3 is off `main`, at `research/q868h-868-20261113` @ `ffc9cda4` (R3:24).
- MECH-1 (`mechanism-1-20261107/`) and QP/U′ (`bsel-2-*` records) are on `main`, but are not in the
  `main` content table.

The scope claim itself does not depend on them, since it restates E2's own hypothesis. The
references are provenance, but item 8 requires each reference to be classified.

**Fix.** Either delete "such as the epistricted and stabilizer-type encodings used by MECH-1, QP/U′
and Q-868-H", or add a row:

> | M | Q-868-H r3 (`research/q868h-868-20261113` @ `ffc9cda4`, off `main`); MECH-1
> (`verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/`) and QP/U′ (on `main`) |
> §3.2 E2 scope sentence (Δ9) | **provenance**: the sentence restates E2's full-domain hypothesis;
> the named encodings are examples taken from R3:60, and E2's scope does not use their content |
> No gap. |

### 11. The standing paragraph overstates review coverage and omits §A.46 item 4's accountable Issue and plan (should-fix)

**Where:** `NEW-RESULTS.md`:5–7.

**Evidence.** "Each is a paper argument [A]: hand-checked in the drafts' reviews and in the
reconciliation". The record does not support that for every result:

- REVIEW-r1 hand-checks T5, E2 item 4, G1/S2c and L1/L4 (RV:47–73).
- RECONCILE marks "hand-checked" only for T5, saturation, G1 and E2.
- E1 is compared with A★2 (RV:80) but not hand-checked.
- (NS_A)/(PAD)/S7 and the A/B/C classification are reviewed ("Yes", R3:67–68) but not marked as
  hand-checked.
- The ChatGPT reviews assess scope rather than hand-check each step.

Separately, §A.46 item 4 requires an unverified claim on `main` to carry an accountable Issue and a
remediation plan. The package gives status and the off-`main` gaps, but no plan for the [A]
verification gap itself.

**Fix.** Replace from "Each is a paper argument [A]" to "stated with it." with:

> Each is a paper argument [A], not kernel-checked, and conditional on the hypotheses stated with it.
> Model-written reviews read every result (`PROVENANCE.md` §2–3); the steps hand-checked there, and
> those hand-checked in this record, are cited at each result. None of these reviews is verification
> (§A.46 item 7). The accountable Issue is #1169. The open gaps are listed in `DEPENDENCIES.md`, and
> verification would be an independent non-model review or a kernel formalization; T5(c), E1, E2
> item 4 and L1 are named kernel targets (I:294, S:347).

### 12. Altered text sits inside quotation marks in "copied" passages (should-fix)

**Where:** `NEW-RESULTS.md`:498–505 (SLL, Δ16); :447–451 and :461–466 (table cells marked "copied
from S:177–181" and "copied from S:187–190").

**Evidence.**

- Inside the SLL quotation, the package inserts "to `G_φ^ref`, Main:724", "the window of Main:414;",
  "(measurement independence, ledger item (xiv), Main:724)" and "of the same kind as the scoping of
  (x) that Main:724 states (Bell-scope's finding F1)". None of these is bracketed. The last replaces
  the draft's "parallel to Bell-scope's finding F1 on (x)".
- In the table cells, text from Δ12 and Δ13 replaces draft text under a "copied" label.

The Text conventions (:34–39) say a change is marked at the place it occurs. In the SLL paragraph
the marks are only paragraph-level. A reader cannot tell the draft's words from the package's
inside the quotation.

**Fix.**

- In the SLL quotation, put each inserted or replaced phrase in square brackets, for example
  "route B (an update outside (vii), with (x) scoped [to `G_φ^ref`, Main:724])" and "an owner
  question, [of the same kind as the scoping of (x) that Main:724 states (Bell-scope's finding
  F1)]".
- Relabel the two table headers "(from S:177–181, with the changes of Δ1 and Δ12)" and "(from
  S:187–190, with the changes of Δ1, Δ13, Δ14 and Δ20)".

### 13. Nits

1. **Status labels of the T5 hypotheses** (`NEW-RESULTS.md`:132–138). The Code Review Rules label
   named hypotheses as *justified*, *posited* or *open*. Write "Status: open on `main`; paper proof
   off `main` (I:159–168 [D]; APPROX r4a C1 [D]); hand-checked RV:48–49", and likewise for (T5b) and
   (T5d). Separately: these proofs are short and are in the copied source, so if the owner widened
   the scope, gap A1 would close by carrying I:159–168 and I:179. This is an owner question, not a
   defect.
2. **"(b)" in the copied `op` case** (`NEW-RESULTS.md`:149) refers to the draft's (b). Add "[(b) is
   (T5b) above]".
3. **The FI-1 witness needs |S| ≥ 2** (`NEW-RESULTS.md`:136). Add "(for |S| ≥ 2)".
4. **L4 Hypotheses** (`NEW-RESULTS.md`:431) add "a finite site set V", which L4's statement does not
   use. Write "Product of abelian groups over a site set V (finite in Main's `G_φ^K`)".
5. **Δ27 has no [Δ27] marker** at the heading (`NEW-RESULTS.md`:399), contrary to the convention at
   :34–35. Append " [Δ27]". The reworded heading has the same meaning: both assert that ∼_K, hence
   `G_φ^K`, is the same for every non-empty state class. The statement and proof are unchanged
   (`git show 1ef60d92` changes one heading line and adds one `CHANGES.md` row).
6. **Δ20's source line** (`CHANGES.md`:39). The gloss "a shared factor that both wings read and no
   setting writes is a common cause" is S:26's wording. S:167's title is "a shared factor is
   harmless unless a setting writes it". Cite S:26.
7. **The S4 hand check** (`NEW-RESULTS.md`:468–471) puts the channel at wing B (B outputs p ⊕ ab).
   The probe puts it at A (h_A = d ⊕ ab, probe line 213). The result is symmetric. To match the
   source, write "wing B outputs p and wing A outputs p ⊕ ab, the channel carrying b to A".
8. **H-LIFT's line range** (`NEW-RESULTS.md`:61): H-LIFT is at `DESIGN.md`:319–321, not :318–321.
9. **The Q1-D typing of H1–H2** (`NEW-RESULTS.md`:62) is unattributed. Add "(RV:153)".
10. **Δ14 and Δ19 handle cross-references differently.** Δ14 replaces "§3.4" inline with "§6", while
    Δ19 says that copied sentences keep their wording and a bracket gives the target. Either bracket
    "[§6 here]" after an unchanged "§3.4", or reword Δ19 and :38–39 to allow inline replacement.
11. **`PROVENANCE.md`:9** lists "parents `1d3c4599` (r3), `b36bba60` (r1, review, r2)". `703ae20e`
    has the single parent `1d3c4599`, and `b36bba60` is its grandparent. Write "parent `1d3c4599`
    (r3); ancestor `b36bba60` (r1, review, r2)".
12. **`PROVENANCE.md`:78–81.** State that c.6854728636 step 5, a current owner decision to replace the
    2026-11-11 approvals cited in the #1230 and #1232 PR bodies, has no recorded decision on #1169 up
    to c.6855167580. c.6855167580 authorizes this writer pass, not those drafts.
13. **`DEPENDENCIES.md`:31 (row H).** Replace "whether `7f465d56` changes it was not checked here"
    with "`REC-1-r7.md` is unchanged from `9f7d2612` to the branch head".

## Check-by-check summary

1. **Faithful copying.**
   - T5(c) matches I:170–177; E1 matches S:82–92 and S:72; E2 matches S:110–121; L4 matches S:155;
     (PAD) matches S:206; (NS_A) matches S:196–202; S7 matches S:208–211.
   - The G1 argument matches S:102–108, and L1 matches S:143–147 apart from Δ1.
   - Δ1–Δ26 were each checked against the source lines they cite. They are accurate, except that
     Δ10 changes the meaning of the (vii) gloss (finding 2) and Δ15 misreports S:309 (finding 3).
   - Unmarked in-quote changes are finding 12. The Δ27 heading change preserves meaning (nit 5).
   - No listed change alters a carried statement's mathematics.
2. **Claim/evidence boundary.**
   - T5(c)'s logic is correct against the Lean source. `op` is square with Kᴴ K = 1, so (T5b)'s
     "square" is accurate. The CM→substratumClass direction needs (T5b) only, and the theory
     equality needs (T5a). Both directions of the ↔ are proved separately (§A.34).
   - Findings 4, 5, 8 and 9 are boundary defects.
   - The negative results are scoped: E2 to one full-domain linear encoding, L1 and L4 to additive
     or stencil rules, and SLL is an open obligation.
3. **§A.42 item 8.**
   - Rows A1, D2, D3 and E2 are narrowed correctly by conditional statement, and rows B, E3, E4 and F
     are support on `main`, as stated.
   - Rows C, D1, G, H, I, J and K are provenance. Row X is provenance once finding 6 is fixed.
   - The remaining defects are findings 1, 5, 7, 8 and 10.
   - Every cited `main` anchor exists at `c3b5f37a` (= current `origin/main`) with the stated content.
4. **§A.46.** Status labels are accurate apart from finding 11. Nothing is presented as established.
5. **Register.** No §A.32/§A.33 phrase family, capitals emphasis or revision-history voice appears in
   the added text of `NEW-RESULTS.md`. Process wording in `PROVENANCE.md` §5 and `CHANGES.md` is
   provenance, as intended.
6. **Δ27.** The meaning is preserved (nit 5).
