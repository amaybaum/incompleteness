# Independent review: RO-3 inventory r4 (PR #1303), and its use of OBL-RO3-2

**Verdict: ACCEPT WITH CHANGES.** No label in r4 is refuted at its stated scope. Several labels and
cross-references are stale, though, and r4's map of A1-dependent results is complete only for the
recurrence family that RO-3's Q5 scope names. It is not a corpus-wide map of A1's consumers. The
required changes (R1 to R5) should be made in an authorized r5 before r4 serves as the base for the
next #1055 unit.

## Object, base and limits

- **Reviewed.** `RO3-INVENTORY-r4.md` at PR head `78089e5e7540f116f69933efca898a8b86d5f36d`
  (blob `999cf29a`, SHA-256 `6b96e295…2eed`, matching the README), together with how it uses
  `OBL-RO3-2-r2.md` (SHA-256 `bad122a2…1876`). The OBL-RO3-2 r2 direct mixing proof is not
  re-reviewed. The owner accepted it at its stated scope (#914 c.6883931412 item 2; #1055
  c.6883932722).
- **Authority.** #1169 c.6893456888 (owner, 2026-11-15).
- **Base.** r4 cites `main` `dfeec843`. Between `dfeec843` and `main` `7ac74a4b` the only changes
  under `papers/`, `book/`, `verification/lean*` and `verification/programmes/substratum/` are in
  `book/ch10`, `ch18`, `ch19`, `appendix-a`, FULL and `papers/Complexity.*`. r4 cites none of these
  files, so every `path:line` citation in r4 points to the same text at `7ac74a4b`.
- **Checks made.**
  - Read r4 in full, OBL-RO3-2 r2, the two independent reviews of r2, and ChatGPT reviews
    5906337933 and 5906973051.
  - Looked up every Lean identifier cited in §1 at its stated line, and census families 34, 40, 114
    and 120 with their status.
  - Read the cited Main, GR, SM and Substratum lines.
  - Grepped `papers/`, `book/` and the verification records for A1 and total-finiteness uses.
  - Checked the (ii-b) diagonal calculation against `QuasilocalAlgebra.lean` by hand.
  - No build and no computation.

## 1. Labels (check 1)

Supported at the stated scope:

- **1.1 to 1.4, class F.** The cited theorems exist at the cited lines:
  - `iterate_return_at_order` and `rootedMap_at_order` (`RootedRecurrenceBridge.lean:47`, :55);
  - `rootedMap_periodic` (`RootedClassification.lean:135`);
  - `pIndivisible_of_rooted_identity_return_of_overlap` and
    `pIndivisible_of_identity_return_of_overlap` (`RecurrenceHorizon.lean:148`, :119);
  - `pIndivisible_of_visible_identity_return_nonperm` (`ObservableFactorRecurrence.lean:68`);
  - `measuredGamma_eq_one_iff` (`ObservableMeasureReturn.lean:83`);
  - `finiteRootedRealizable_iff_pper` (`RootedClassificationAllTime.lean:192`).

  The census statuses are as r4 states them. The 1.4 biconditional satisfies §A.34 because each
  direction has its own witness: `pper_of_finiteRootedRealizable` (`RootedClassification.lean:339`)
  and `pper_has_responseRealization` (`RootedClassificationAllTime.lean:162`). r4 cites the
  forward direction through the docstring at AllTime:182 rather than the theorem at
  RootedClassification:339, which Main:638 names. Cite the theorem.
- **1.3 I-meas.** Conditional on exact return. This matches the hypotheses of the two matrix-level
  theorems, which need only row stochasticity, `Γ_n = 1`, and an earlier overlap or non-permutation
  step. The prior serves only to define `Γ`.
- **1.5.** H-scramble fails at aligned bipartitions, so the theorem has no instance (GR:805, :813,
  :823). r4 states this as a failure of the hypothesis, not as a refutation of the theorem. That is
  correct.
- **1.7 I-qloc.** The completion is stated as a uniqueness given stages and dynamics, not as an
  equivalence (§A.34). Correct.

Findings:

- **F1 (minor), r4:252, 1.7 F.** "Refuted within one fixed finite realization" rests on an imported
  half: the unbounded nonnegative rank is taken from [55] (Main:558; Main:600 item (3)). r4's own
  definition of "refuted within" requires "a result on `main`" (r4:79–80). The cell should read
  "refuted within F, conditional on the imported unboundedness theorem [55] (external, cited
  input)".
- **F2 (minor), r4:440, 2.7.** "Poincaré recurrence needs a finite invariant measure" states a
  sufficient condition as a necessary one: conservative infinite-measure systems recur. This is
  addendum n4 (`REVIEW-OBL-r2-ADDENDUM.md`) and is unapplied. Use "is not available without a finite
  invariant measure or conservativity".
- **F3 (minor), r4:418–419, 2.6.** Main:155 is attached to "1.1 and 1.2", but it supports only the
  failure of exact common visible return (1.2). This is addendum n3 and is unapplied.
- **F4 (minor), r4:149.** SM:296's order theorem needs `L ≥ 2` and `p ∤ L`. r4 omits `L ≥ 2`.
  SM:1606 (Theorem A.1) concerns the circulant wave equation with unit coefficients, not general `α`.

## 2. How r4 uses OBL-RO3-2 (stale against the accepted result)

r4 predates the acceptance and does not use OBL-RO3-2's results. That is correct under OBL §7
("Moving any cell needs its own authorized revision", OBL-RO3-2-r2.md:394). Several passages are now
stale, however:

- **F5 (required, R1).** The following passages are stale:
  - r4:459–499 calls OBL-RO3-2 "proposed", "from the review and is unverified", with a "proposed"
    decision rule.
  - r4:483–484 still routes (c) through the Halmos criterion and Rokhlin's theorem.
  - r4:487–489 makes the primary-source check a precondition.

  The owner accepted the direct proofs in place of that check (#1055 c.6883932722), and OBL Step 4
  avoids both criteria (OBL-RO3-2-r2.md:145–158, :205–207). The first branch of r4's own decision
  rule (r4:492–496) has now fired.
- **F6 (required, R1).** These cells and passages should move in r5, at the OBL class only (this
  rule, prime `p`, `α ≠ 0`, uniform Haar `μ`), and not across I-meas or I-qloc as a whole:
  - **1.1 I-qloc and I-meas (r4:153–154).** Exact microscopic return `φ^L = id` is refuted within
    the class: `F` has infinite order (OBL 3.2). μ-almost-everywhere Poincaré recurrence holds, and
    the row should state both. For I-qloc, `heisQ^n ≠ id` follows by hand. On diagonal stage
    elements `heisQ^n` acts as `f ↦ f ∘ F^n`, and cylinder functions separate points.
  - **1.2 I-qloc and I-meas (r4:170–171).** Refuted within the class in the cell-conditioned
    convention. In Main's root-shared convention the refutation covers restriction readouts only
    (OBL-RO3-2-r2.md:221–228).
  - **1.3 (r4:196–197).** The recurrence route is unavailable in the class. P-indivisibility itself
    stays open (OBL 3.3).
  - **2.3 G-fact (r4:352–355).** The `[IR] If the reviewer's mixing reading holds` reading becomes
    OBL 3.4: there is no nontrivial finite dynamical factor.
  - **2.5 first missing step, Q6, and the first secondary candidate (r4:397–409, :565–569,
    :537).** Diagonal invariance (ii-a) and (ii-b) is proved on paper. Only (ii-c), off-diagonal
    invariance, and (iii) remain open (OBL §5).
- **F7 (required, R2): evidence layer of the moves.** OBL-RO3-2 r2 is a paper proof on a PR branch,
  not on `main`. r4's labels "established (P)" and "refuted within" are defined as resting on
  `main` (r4:74–81). Owner acceptance does not make a claim established (§A.46 item 1). r5 must
  therefore do one of two things:
  - cite OBL-RO3-2 r2 at its exact SHA as support off `main`, with the gap stated (§A.42 item 8),
    and label the moved cells accordingly;
  - land OBL-RO3-2 r2 on `main` first.

  It must not record the moved cells as established on `main`.

## 3. Completeness of r4's map of A1-dependent results (check 2)

**Covered.** The recurrence family is covered:
- §2.3: Main:113–129, :135–139, :141–143, :155;
- the all-time periodicity Main:638 and its kernel classification;
- the fixed-finite obstruction Main:558, with Main:496 and :556 under Q12;
- GR:138, :585, :587; A.8 and A.9 (GR:797–839);
- Substratum:255, :257–268; SM:296, :1606;
- the book mirrors `ch01:95–109` and `appendix-b:92`, :413;
- Lean: RootedRecurrenceBridge, RootedClassification(AllTime), RecurrenceHorizon,
  ObservableMeasureReturn and ObservableFactorRecurrence.

**Missed.** Main:60 lists these consumers of the finite representative itself, and r4 has no row
for them:

- **F8 (required, R3).**
  - (a) The **eventual-image and surjectivity steps of the bijectivity argument** (Main:60; "On a
    finite set, injectivity implies surjectivity"; Methodology:158, :166, :253, :261). Every I-class
    in r4 assumes "a measurable bijection" (r4:124) without recording that the corpus derives
    bijectivity from A1.
  - (b) **Lemma 3's counting measure, and the uniform hidden prior that defines the baseline
    matrices** (Main:56, :129, :266; `CanonicalMeasure.lean:54`, `[Fintype S]`). These appear only
    as owner question Q6.
  - (c) The **§3.2 setup's finite hidden space** (Main:266) and the results resting on it:
    - permutation unitarity (:268);
    - the channel with `ρ_H = I_m/m` (:280);
    - the Born-form representation theorem (:286);
    - diagonal preservation (:326);
    - CP-indivisibility (:330), which r4 names only in the 1.3 header (r4:186) and gives no
      per-class row.
  - (d) The **§3.1 corner-occupancy claim**, "conditional on the total-finiteness posit"
    (Main:216).
  - (e) The **§3.3 coupling-graph causal cone**, `S = ∏_{i∈V} S_i` with `V` finite (Main:362), and
    the Bell results built on it.
  - (f) **§4.6** (Main:758). This is acknowledged as out of scope (Q9).

  Also not cited:
  - Main:486, the no-uniform-finite-realization proposition, a second fixed-finite obstruction;
  - Main:718, the falsifiability claim "a finite set with a deterministic bijection".
- **F9 (required, R3): companions and records.**
  - Substratum Theorem 23, the reconstruction within the A1–A6 class (Substratum:104, :199;
    Structure:47). Theorem 24 beyond (iii) is also unmapped.
  - Computation:118 (an `S → ∞` characterization set against total finiteness).
  - The proof-dependency matrix of the merged observer-relative finiteness audit
    (`verification/audits/manuscript/observer-relative-finiteness-20261030/DEPENDENCY-AUDIT.md:277–291`)
    has rows for Theorem 23 and gauge uniqueness, Lemma 3's orbit measure, and finite boundary
    entropy and the ħ gap. r4 cites only its H-product row (:290).
  - Structure's A1–A6 comparisons (e.g. :80, :1032–1038) classify other programmes. They are not
    consumers.
- **F10 (required, R3): the scope statement.** r4 should state that its map covers the Q5 family
  and is not an inventory of A1's consumers. Q9 (r4:581–582) repeats the #1055 body's "second
  consumer" framing. The body says "Main names exactly two consumers", but Main:724 names two
  ("consumed here by the recurrence step of §2.3 and by §4.6") and defers "the remaining uses" to
  the §1.2 Remark, which lists the items above.
- **F11 (required, R3): the "main equivalence" reading.** The authority comment (#1169
  c.6893456888) cites "the per-horizon equivalence's finite hidden configuration space
  (Main.md:111, :266)" and says "the main equivalence stays conditional on that posit".
  - Main:111 and :266 are the setups of §2.3 and §3.2, not of the §3.4 equivalence (Main:546).
  - Main:60 states that the §3.4 equivalence uses only Lemma 1, "in which a finite hidden space is
    constructed, not assumed". r4:237 follows that.
  - The source governs (§A.45 rule 1). The difference is a finding for the owner, and r5 should
    state it so that the next unit does not inherit the conflation. What does consume A1 is the
    family in F8 (c): the Born-form representation, the channel and CP-indivisibility.

## 4. Stale cross-references (check 3)

- **F12 (required, R4), r4:337–338.** "Whether such a stage counts … under Gate A answers 3 and 4 is
  an owner question (§4, Q10)" is stale on two counts:
  - Q10 is decided: r4:590–592 itself quotes the adoption.
  - Answer 4 is quoted verbatim at r4:50–52 and r4:588–589. If D-CQ amends answer 4, as the brief
    states, all three sites are stale.

  I could not locate the D-CQ record in the comments of #1169, #914, #1055, #1294, #1303 or #945,
  or on the RO-1 (`e4ffa3b5`) and Gate A amendment branches. r5 should cite it by comment id and
  quote the amended answer.
- **F13 (required, R4), r4:551–554 Q2, and r4:338–339.** "Does stating it fall under RO-1's
  specification of sector C, or is it separate?" is answered. The RO-1 split (#1169 c.6883250792,
  2026-11-14T19:48:20Z) assigns to RO-1 "sector-C membership, physical confinement grounds (S-J),
  closure … (S-A)". It was adopted in the same minute as Q10–Q12, which r3 recorded, so r3 and r4
  missed it. Q2's remaining part is whether a support-level finiteness posit is admissible. That
  part now belongs to RO-1 and S-J.
- **F14 (required, R4), r4:58–66 and r4:640–641.** The ledger statements are stale:
  - "The ledger is not on `main`" and "A draft r9 … pending review" no longer hold.
    `LEDGER-r8.md` is on `main` at `7ac74a4b`, byte-identical to `9ff3b8d9`, and the accepted r9 is
    on `main` through #1304 (#1169 c.6891337868).
  - r4's provenance-only classification of the ledger in §6 can become support on `main`.
  - The r8→r9 diff on the cited identifiers adds rows only; no cited row changes. I checked this on
    `main`.
- **F15 (minor).** The status lines disagree:
  - r4:3 and :8 say "UNREVIEWED … r4 has not been reviewed", while the README lists r4 as
    "reviewed (ACCEPT)" (`REVIEW-OBL-r2.md`).
  - r4:351 still says "so r2 does not recommend it".
  - The Base line names `dfeec843` (r4:57); `7ac74a4b` is equivalent for every cited file (see
    "Object, base and limits").

## 5. ChatGPT review 5906973051 nits (check 4): confirmed unapplied

Both nits concern `OBL-RO3-2-r2.md:352`, row (ii-b). The independent confirmation raised the same
two points (`REVIEW-OBL-r2.md`, nits n1 and n2), and neither is applied at the head.

- **F16 (R5), the `patch_glob` lemma.** The row still says that `patch Λ s (glob Λ s) = s` is "the
  one identity assumed here and not looked up". This is the kernel theorem `patch_glob`
  (`QuasilocalAlgebra.lean:136`). Cite it and drop the caveat.
- **F17 (R5), the explicit diagonal identification.** Step (3) passes from the operator identity
  `heis Φ D_f = D_{f∘φ}` to the value of `heisQ_stage` (:1274) without identifying the matrix.
  The missing clause, checked here by hand:
  - `heis_emb` (:1127) gives `heis Φ (emb Λ X) = emb (hat Φ Λ) (transported Φ Λ X)`.
  - For `X = diag g`, the sum defining `transported` (:1109) is nonzero only at
    `f₀ = glob Λ (φ (ext h))`. By `patch_glob` and `glob_ext` (:1071),
    `target Φ Λ (ext h) f₀ = glob (hat Φ Λ) (ext h) = h`.
  - Hence `transported Φ Λ (diag g) = diag (h ↦ g (glob Λ (φ (ext h))))` on `Conf (hat Φ Λ)`.
  - The value does not depend on the choice of extension, by `glob_map_of_glob_eq` (:1073).
  - Only then does `referenceState_stage` (:904) give the uniform average.

  `emb_injective` (:353, `[Nonempty Q]`) or `kern_patch` (:178) gives the same identification at
  the operator level. The calculation holds as stated.

## 6. The next bounded #1055 unit (check 5)

**Prerequisite.** An r5 of the inventory applying R1 to R4. It is editorial with a status
propagation and needs its own authorization (OBL §7). It should not be bundled with new
mathematics.

**Recommended first recovery target:** recurrence-scale P-indivisibility (Main:113–143) and the
rooted classification's necessity half (Main:638), with an infinite normalized deep factor that the
dynamics does not couple.

- **Statement.**
  - The carrier is `S = (C_V × C_H) × Ω`, where `(Ω, ν)` is a standard probability space,
    `ν(Ω) = 1`, and `ψ` is a measurable bijection of `Ω`.
  - The dynamics is `φ̃ = φ × ψ`, with the root-shared prior `μ_H ⊗ ν`.
  - Claim: `Γ̃_t = Γ_t` for every `t`. Then the identity return, recurrence-scale
    P-indivisibility and `Γ̃ ∈ P_per(V)` all transfer, while `φ̃` itself need not have finite order.
- **Why this target.** It is the infinite form of Theorem 24(iii) (Substratum:257–262), restricted
  to rooted laws. r4 names it as the first missing step for decoupled I-deep (r4:370–375). Main:60
  explicitly leaves an infinite hidden sector outside its enlargement statement, so the result is
  not already on record. It separates microscopic recurrence, which fails, from exact common
  visible return, which holds. That locates A1's actual role in the §2.3 route: finiteness is
  needed only on the coupled factor.
- **Skepticism, stated in advance.**
  - The proof is near Fubini and nearly definitional, the same weakness that withdrew
    OBL-RO3-1.
  - Its value is a scoped recovery under #1055 acceptance criterion 2. It replaces A1 by "the
    dynamically coupled part is finite".
  - It is not a Layer-0 replacement of A1 and supplies no independent prediction under §A.29.
  - It must not be presented as removing the posit: the coupled part stays finite by assumption.
- **Controls, set in advance.**
  - With `Ω` a single point, every F cell of 1.1 to 1.5 is reproduced unchanged.
  - Finite Theorem 24(iii), the readback lemma, `S ⇔ D ⇔ Q_fb`, and GR:138's scope are unchanged.
- **Countercontrols that must fail at a named step.**
  - (i) A coupled infinite sector: the OBL-RO3-2 linear rule under Haar measure has no exact return,
    so an argument that transfers to it is wrong.
  - (ii) I-nonorm: counting measure with the shift on `Z` gives no rooted law. The proof must use
    `ν(Ω) = 1` at a named step.
  - (iii) The RR nonperiodic families on coupled infinite hidden carriers
    (`continuous-substates/infinite-xor-counterexample.md`). These are context only, not premises.
- **Decision rule, preregistered as a rule.**
  - **Recovery:** a complete paper proof of the stated transfer, with every hypothesis labelled.
  - **Negative:** a named hypothesis without which the transfer fails, such as standardness,
    measurability of `ψ`, or H-product under the product prior, shown by an explicit
    counterexample in the stated class.
  - **Anything else:** open, with the remaining gap stated.
  - No expected outcome is set in advance.

**Second candidate:** the bijectivity step of F8 (a), which r4 does not map.

- **Statement.** On a probability space, an injective measurable map that preserves a normalized
  measure, with measurable image, is onto up to a null set, because `μ(T X) ≥ μ(T⁻¹ T X) = 1`.
- **Effect.** This replaces A1 in Main:60's surjectivity step by the normalized-measure premise that
  r4 already needs for rooted laws.
- **Countercontrols.**
  - `n ↦ n+1` on `N`: injective, not onto, with no normalized invariant measure.
  - The one-sided shift: measure-preserving, but not injective.

**Not recommended first:** recurrence-scale P-indivisibility on a coupled infinite sector by a
non-recurrence route. On the OBL class it is open, and no bounded mechanism is in view (OBL 3.3).

## Required changes (summary)

- **R1.** Update r4:153–154, :170–171, :196–197, :352–355, :397–409, :459–499, :537 and :565–569 to
  the accepted OBL-RO3-2 r2, at its class only (F5, F6).
- **R2.** Label the moved cells as support off `main` at the exact SHA, or land OBL-RO3-2 r2 first
  (F7).
- **R3.** State the map's scope, add rows or an explicit out-of-scope list for F8 and F9, and record
  F11 (F8 to F11).
- **R4.** Repair the stale Q10 and Gate A answer 4 references, the Q2 and RO-1 reference, and the
  ledger references (F12 to F14).
- **R5.** Apply F16 and F17 in an OBL-RO3-2 r3, and F1 to F4 and F15 in the inventory r5.

No finding requires withdrawing a result. Every finite-carrier result keeps its scope.
