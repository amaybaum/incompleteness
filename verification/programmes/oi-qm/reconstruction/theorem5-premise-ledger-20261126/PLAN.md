# T5-LEDGER-1: the premise ledger of SM Theorem 5 (unit A; #1049, #1217). Plan

**WIP / UNVERIFIED. Model-written research plan, paper-only. Nothing here is adopted, proposed for
the manuscripts or authorized beyond the unit's scope. This file fixes the questions, conventions,
evidence labels, decision rule, controls, productivity test and stopping rule. It is committed
alone, before any report, and contains no result.**

**Chronology disclosure.** Before this file was written the writer read the sources named in §1
(SM:126–140, SM:222–242, SM:290–300, SM:310–396, SM:474, SM:486–509, SM:609–613, SM:809; Sub:102,
Sub:159, Sub:163, Sub:189–195; the lane 1 and lane 2 records; the consolidated synthesis). No ledger
classification, no Q2 or Q3 outcome and no new counterexample was derived. The decision rule below
is fixed as a rule, not as an expected result. This file is a research plan committed before its
report. It is not a frozen preregistration under §A.39 or §A.50 item 5, and it freezes nothing.

- **Accountable Issues:** #1049 and #1217; programme #1169. Related: #1029, which received lane 1's
  routing of the SM:130 / SM:493 variance.
- **Authorization:** owner decision in #1169 comment 7189139613 (account amaybaum, comment created
  2026-11-26T10:16:17Z; the comment states that the owner decision was received 2026-11-26T10:16Z),
  item 2, lane 1 of the new wave: "Theorem 5 premise ledger (#1049, #1217) | Establish exactly which
  symmetry and additional premises the proof requires." Acceptance criteria: "Lane 1: Produce a
  complete premise ledger distinguishing stated assumptions, derived conditions and unsupported
  steps. Determine whether the full dynamical symmetry is necessary or whether kinetic symmetry
  suffices." The same decision also says: "Use separate writers and independent reviewers, with
  distinct research artifacts for lanes 1 and 3 to avoid conflicting work."; "The previous results
  should be described as reviewed paper derivations, not independently verified theorems."; and
  "Do not authorize computation or adopt additional premises through the new research units." The
  recorded designation in that comment reads: "Unit A (lane 1, Theorem 5 premise ledger, #1049 and
  #1217): `writer-t5-ledger`; branch `research/t5-premise-ledger-20261126`." In this file, "lane 1"
  and "lane 2" without qualification mean the landed records of #1049 and #1217 (§1). They do not
  mean the lanes of the new wave.
- **Goal link (§A.47).** It serves #1049 (tier Foundational) and #1217 (tier Foundational).
  - **For #1049**, the unit decides whether SM Theorem 5's proof, as stated, consumes U(6) as a
    symmetry of the full dynamics (R-dyn). That settles whether lane 1's D3/D16 dependence on
    b = 0, which lane 1 places only under R-dyn, is a dependence of the proof or only of one reading
    stated elsewhere.
  - **For #1217**, the unit decides whether Theorem 5's use of a complex structure rests on one
    bridge premise or on several, and whether any of them (the full two-point condensate clause, or
    H-PF) follows from a stated premise.
  - It decides neither the outcome expected nor which reading the manuscript should adopt (Q4b as
    an owner or referee reading). It does not decide H-ZM or the SM:811 energy (unit C), A5, Q-α or
    Q-γ.
- **Pinned main commit [P]:** `353a066f18766837fed8c7f58507e09ff549b1a4`.
- **Writer:** `writer-t5-ledger`; branch `research/t5-premise-ledger-20261126`. The writer makes no
  GitHub writes and no dispatch. Commits and pushes are made by the coordinator.

## 0. Line conventions

- `SM:n`, `Sub:n`, `Main:n` are line n of `papers/SM.md`, `papers/Substratum.md` and
  `papers/Main.md` at [P]. `ch05:n` and `FULL:n` are line n of `book/ch05-gauge-structure.md` and
  `book/The-Incompleteness-of-Observation-FULL.md` at [P].
- Lanes 1 and 2 cite lines at `b6c6b80bbd4a878452e54759cc85f16c9ffb72da`, an ancestor of [P].
  Between that commit and [P]:
  - `papers/SM.md` changes only by in-place edits at SM:1394 and SM:1472;
  - `papers/Substratum.md` changes only at Sub:463;
  - `papers/Main.md` changes only at Main:692, :716, :720 and :724;
  - no line is inserted or removed in these three files.
  Their SM, Sub and Main citations therefore carry over to [P] unchanged.
- Kernel statements are read at [P]. Nothing is built.

## 1. Inputs and evidence labels

| Label | Meaning |
| --- | --- |
| [K] | Kernel theorem on `main`, statement read at [P]: `theorem_7`, `sum_proj`, `finrank_PT`, `char_c4_odd` (`OIBridge/LinkDecomposition.lean`); the scope statements at `OIBridge/A6Instantiation.lean`:66 and :405, which exclude the condensate stabilizer from the kernel |
| [P] | Manuscript statement at [P] |
| [L1] | Lane 1 result, a reviewed paper derivation, partially verified: `verification/programmes/substratum/a5-linear-affine-20261104/qbeta-trace-20261126/REPORT-r2.md` (§2.7, rows D3 and D16, §6, §7). [L1-Q4] marks results of `A5-Q4-STAGE2D.md` in the parent directory |
| [L2] | Lane 2 result, a reviewed paper derivation, partially verified, with its recorded nits: `verification/programmes/oi-qm/reconstruction/complex-carrier-20261126/REPORT-r2.md` and `PRESERVATION.md` (§4: Propositions 7, 8 and 11, Counterexamples 9 and 10, H-PF, the two-point H-cust clause, same-dynamics stationarity; §5; §6) |
| [A] | Exact hand algebra in this record, unreviewed |
| [W] | Reasoning in this record, unreviewed |

Rules for inputs:
- [L1] and [L2] results are used only as labelled conditional inputs. A ledger verdict, Q2 outcome
  or Q3 outcome that rests on one is stated conditional on it, unless the result is re-derived here
  at [A].
- Counterexamples 9 and 10 and Propositions 7 and 8 are re-derived here as controls (§5).
- Content not on `main` is provenance only. Every off-`main` reference in the report is traced
  under §A.42 item 8.
- The consolidated synthesis (#1169 comment 7189143747) is provenance and fixes no result.

## 2. Questions

### Q1. The complete premise ledger

List every premise that SM Theorem 5's statement and proof (SM:340–342) consume, directly or through
the passages they cite. Classify each item as exactly one of:
- **S (stated assumption):** the content the proof uses is stated at a named location in the corpus
  at [P]. An item counts as S only when the text at that location states the content used, not a
  weaker one. When the location is outside Theorem 5's own hypothesis list, the item is tagged
  *stated elsewhere*.
- **Dv (derived condition):** the content follows from stated assumptions by a named derivation. The
  record gives the derivation's location and evidence layer ([K], [P] proof, [L1], [L2] or [A]) and
  every hypothesis it carries.
- **U (unsupported step):** the proof uses the content, and within the search scope of §4 it is
  neither stated nor derived. U is a finding about support. It is not a disproof (§A.19), and it is
  never presented as one.

Each item also records:
- its **layer**: M, the mathematical statement that the stabilizer in U(6) of a block-scalar Σ is
  U(3)×U(2)×U(1); or Φ, the physical reading that this is the unbroken subgroup of the state;
- its **carrier and regime**: T or Z (lane 2 §3); abs(αμ) < 1/d or αμ = 1/d;
- the named hypotheses it carries: LIN, LIFT, b = 0, abs(αμ) ≤ 1/d, H-top, H-blind and H-ZM, where
  they apply.

**Seed list (fixed now; items found while tracing are added and marked as found):**

| Id | Item | Source at [P] |
| --- | --- | --- |
| H1 | H-link with one carrier copy, m = 1 | SM:340; SM:360–364 |
| H2 | H-cust kinetic clause: the kinetic structure is custodially scalar before the state is chosen | SM:340; SM:374 |
| H2a | Its supply at M = μI_6 by Proposition 4b, with Proposition 4b's own hypotheses (an identical, independent component rule; the selected counting measure; a component-complete site observer; H-blind for extensions) | SM:334–338 |
| H3 | O-equivariance of Σ, the condensate clause of H-cust | SM:340; SM:136; SM:374 |
| H4 | Σ = ⟨φφ†⟩: what φ is (C^6-valued; its relation to the real observer-level field of SM:312) and what ⟨·⟩ is (which law; stationary under which map) | SM:340; SM:312–316; SM:505 |
| H5 | Distinct block values | SM:340 |
| H6 | The ambient U(6): a complex structure and Hermitian form on the carrier, and which complex structure (H-link's abstract ⊗C, or the dynamics' J_F) | SM:362; SM:505; SM:809 |
| P1 | "Under H-cust the pre-condensate observer-level kinetic term is invariant under the custodial unitary action on the physical link carrier." | SM:342 |
| P2 | "The unbroken subgroup of a state with condensate Σ is its unitary stabilizer." | SM:342 |
| P3 | The decomposition 6 = T_1 + E + A_1, multiplicity-free and irreducible after complexification | SM:374–376; [K] `theorem_7` |
| P4 | Schur's lemma gives Σ = aP_T1 + bP_E + cP_A1 with real a, b, c | SM:340; SM:342; SM:376 |
| P5 | Distinct a, b, c give the stabilizer U(3)×U(2)×U(1) | SM:342 |
| L-HPF | H-PF: SM's φ is the J-linear positive-frequency field of the real lift | [L2] §6 |
| L-SDS | The state is stationary under the same custodially scalar linear map | [L2] Counterexample 10 |
| L-TPC | H-cust's condensate clause on the full two-point function | [L2] §4.2, Counterexample 9 |
| L-NZM | A non-zero-mode condensate at αμ = 1/d | [L2] Proposition 11 (depends on H-ZM: unit C) |

**Readings and restatements** checked for consistency with the ledger (these are not proof items):
SM:130, SM:338, SM:344, SM:474, SM:493, SM:613; Sub:102, Sub:163, Sub:189, Sub:193; ch05:120 and
its FULL:1435 mirror. Where a restatement states stronger premises or a stronger conclusion than
the ledger supports, that is a finding for routing. It is listed, not edited.

### Q2. Ambient symmetry per item

For each ledger item, find the weakest reading under which the item holds, together with every
other stated premise (§3). The readings are fixed as follows:
- **R-coup:** U(6) lies in the commutant of the coupling M on the complexified carrier (Sub:102).
- **R-kin:** U(6) leaves invariant the observer-level kinetic (quadratic) structure of the bare
  linear real lift. Other terms (an offset, the threshold, interactions) may break it explicitly
  (SM:130, SM:340, SM:342, Sub:163, Sub:193).
- **R-kin-st:** R-kin for the possibly dressed linear map under which the condensate state is
  stationary ([L2] §4.4; SM:338). This is an intermediate classification category, not a premise
  proposal.
- **R-dyn:** U(6) is a symmetry of the full pre-condensate dynamics, including every term it
  carries (SM:493). Where no U(6) can act on the object (the Z/q alphabet, [L1] §2.7), R-dyn is
  recorded as not meaningful at that level.

R-coup and R-kin are the weak readings that the acceptance criterion groups as "kinetic symmetry".
Where they differ for an item, both are recorded. Each Q2 entry also records which complex
structure the U(6) is taken with.

### Q3. Do the two-point clause or H-PF follow from a stated premise?

Targets:
- **TPC:** C = Σ_b C_b ⊗ P_b for the full second moment ([L2] §4.2).
- **H-PF** ([L2] §6).

For each target the outcome is one of:
- **derived:** a written derivation from listed stated premises, with its evidence label;
- **independent of the stated premises:** a model meeting every stated premise (§3) in which the
  target fails;
- **not found within scope:** neither of the above, within the search of §4. The target is then
  open. This outcome never reads "cannot be derived".

## 3. What counts as "every stated premise"

A model offered as a counterexample, or as an independence witness, must meet all of the
following:
- (i) Theorem 5's hypothesis list at SM:340;
- (ii) the premises stated at the sites the proof cites: SM:360–364 (H-link), SM:374 (H-cust,
  including "does not introduce extra copy-mixing custodial structure"), SM:334–338
  (Proposition 4b) and SM:136 (the condensate clause);
- (iii) the branch premises of SM §4.1 and §4.4 (SM:232, SM:312–316).

Where a stated premise admits more than one reading, the model is checked against each reading,
and the verdict is recorded per reading. A model that meets only (i) defeats an item only "under
the narrow reading" and is recorded as such.

## 4. Search scope (fixed now)

The S/Dv/U classification and Q3 read every passage in the following scope. The search is fixed in
advance and is not keyword-only:
- SM:10–34 (abstract and tiers), SM:110–140 (§3.1), SM:216–620 (§4.1–§4.12) and SM:805–815 (read
  only for SM:809's real-to-complex step; the SM:811 energy is unit C's);
- Sub:80–110 (A1–A6) and Sub:140–200 (Stages 1–3, Theorem 23);
- Main:736–750 (posit ledger). Main §3's complex kinematics is read only to check for an explicit
  formal map to H-PF; sharing the word "complex" is not an identification;
- ch05 (whole chapter) and its FULL mirror;
- the statements, at [P], of the kernel modules `LinkDecomposition`, `A6Instantiation` and
  `BackgroundIndependence`;
- a supplementary sweep over `papers/*.md`, `book/*.md` and `verification/` for the terms:
  condensate; Σ; ⟨φφ; two-point; positive-frequency; complex structure; ⊗ℂ / \otimes\mathbb C;
  H-cust; custodial; stationary; U(6); unbroken. Every hit is read in context.

## 5. Controls and countercontrols

A verdict printed over a failed or vacuous control is void (Code Review Rules, "Exactness and
controls").
- **CC1 (Counterexample 9).** Re-derive [L2] Counterexample 9 at [A], within its stated range (T:
  abs(αμ) < 1/d or V_rest; Z: abs(αμ) < 1/d, with the bump-support condition of PRESERVATION.md §2
  stated). The ledger must mark P2, under the on-site reading of H3, as defeated by it. CC1 also
  records, per reading of SM:374, whether the model meets §3 (ii).
- **CC2 (Counterexample 10).** Re-derive [L2] Counterexample 10 at [A]. The ledger must mark the
  item(s) it defeats (P1 and/or P2) when the kinetic clause holds for the bare map only and the
  state is stationary under a block-dressed map. The stabilizer in the bare U(6) must come out as
  O(3)×O(2)×O(1).
- **CC3 (positive control).** Under lane 2's stated positive class (Propositions 7–8 re-derived at
  [A], with L-TPC, L-HPF and L-SDS), the ledger's premises must reproduce the stabilizer exactly
  U(3)×U(2)×U(1). Failure means the ledger is incomplete.
- **CC4 (real-carrier control).** Without a complex structure, a cubic-equivariant real symmetric Σ
  with distinct values has stabilizer O(3)×O(2)×O(1) in O(6), of dimension 4 against 14. The ledger
  must carry H6 as an item.
- **CC5 (degeneracy control).** If two block values coincide, the stabilizer is strictly larger.
  The ledger must carry H5.
- **CC6 (kernel control).** P3 must be classified as Dv at [K] (`theorem_7`), never as an
  assumption.
- **CC7 (non-vacuity of Q2).** Exhibit a dynamics that meets R-kin and not R-dyn within the branch,
  for example the threshold breaking of SM:130 or a uniform A_1 offset ([L1] §2.7). Without one,
  the R-kin/R-dyn distinction is vacuous for the class, and Q2 is reported as vacuous rather than
  decided.
- **CC8 (witness check).** Every counterexample or independence witness offered for Q2 or Q3
  carries an itemized check that it meets the weaker reading and each premise of §3. A missing line
  voids the witness.
- **CC9 (pin control).** Every quoted line is re-read at [P].

## 6. Decision rule for Q2 (fixed before any result)

**Per item.** Let m(i) be the weakest reading, in the order none, R-coup/R-kin, R-kin-st, R-dyn,
under which item i is proved with every other stated premise held.
- A **counterexample under reading R** is a model meeting R and §3 in which item i fails.
- An item for which no reading is proved and no counterexample is found is **undetermined between**
  the strongest reading refuted and the weakest reading not refuted.
- An item that fails even under R-dyn with every stated premise held is classified U for Q1 and
  recorded as "fails under every reading".

**Verdict, generated from the table, separately for layer M and layer Φ:**
- "Kinetic symmetry suffices" iff every item of that layer is proved under R-coup or R-kin.
- "Kinetic symmetry does not suffice" iff some item of that layer has a counterexample under R-kin.
- "Full dynamical symmetry is necessary" iff some item has a counterexample under R-kin-st, and
  that item is proved under R-dyn.
- "Kinetic symmetry suffices only at the stationary dynamics" iff no item needs R-dyn, some item
  has a counterexample under R-kin, and every such item is proved under R-kin-st.
- Otherwise "not determined", with each undetermined item named and the strongest partial result
  stated.

The verdict sentences are printed only if CC1–CC9 are green.

**Consequence for #1049, stated with its conditions:**
- If layer Φ obtains "kinetic symmetry suffices", the D3/D16 placement that Theorem 5's proof
  consumes is lane 1's R-kin placement.
- If layer Φ needs R-dyn, lane 1's R-dyn placement (conditional on Q4c, H-b and SM:232) is
  consumed.
- Neither branch decides the owner reading Q4b.

**Consequence for #1217:**
- the number of distinct premises among L-HPF, L-TPC, L-SDS and L-NZM that Theorem 5 needs after Q1
  and Q3;
- which of them, if any, are derived.

## 7. Productivity test (fixed before work, §A.31)

The unit is a **gem** iff it yields at least one of:
- (G1) a proof that R-kin (or R-coup) suffices, for the whole proof or for a named step that lane 1
  or lane 2 left Q4b-dependent or open;
- (G2) an explicit step that fails under R-kin, with a witness meeting R-kin and §3;
- (G3) a derivation of TPC or of H-PF from stated premises;
- (G4) a state meeting every stated premise of §3 that defeats a step, beyond the reproduction of
  Counterexamples 9 and 10. Their reproduction is a control, not a gem.

**Non-gems:** restating the SM:130 / SM:493 variance; relabelling; listing premises already named
by lanes 1 and 2 without a new classification. The complete ledger is the acceptance deliverable
whether or not the test is met.

Findings are classified NEW / POSITIVE / ELABORATING / CONFIRMING / BORDERLINE. A branch whose
outcome favours the framework (G1 or G3) is pressure-tested against CC1, CC2, the null sector and
dressing before it is accepted.

## 8. Stopping rule

Stop when all of the following hold:
- every ledger item has an S/Dv/U classification and a Q2 entry (proved reading, counterexample, or
  a precise "undetermined between" node);
- each Q3 target has reached derived, independent, or not-found-within-scope, with every passage of
  §4 read;
- or, alternatively to the first two conditions, 3–4 consecutive depth-first passes yield no NEW
  finding.

**Halt** (the report records the halt and prints no verdict):
- a control of §5 fails;
- a provenance anomaly (§A.26);
- a step would need computation or a Lean build: it is listed as a post-hold control and not run;
- a step would need adopting, weakening or changing a premise.

**Questions reaching H-ZM or the SM:811 energy** are recorded as dependencies on unit C and not
pursued.

## 9. Exclusions

- No manuscript, ledger, census or registry edit.
- No adoption, weakening or change of any premise: H-PF, TPC, R-dyn, H-ZM and A5 included.
- No computation, enumeration or Lean build.
- No GitHub writes by the writer.
- No decision of Q4b's manuscript reading, Q-α, Q-γ, H-ZM or the SM:811 energy.
- No claim for the Z/q level or the nonlinear case beyond naming H-PF-int.
- No editing of unit C's record.

## 10. Review requirement

The report is reviewed, before any acceptance, by an independent non-author reviewer: a separate
agent, not the writer, at an exact pushed commit. The reviewer checks:
- each control;
- the claim/evidence boundary;
- every displayed equivalence, one direction at a time (§A.34);
- the generation of the verdict from the table;
- the §A.42 item 8 tracing.

A model review is evidence of review, not independent mathematical verification (§A.46). Results
remain reviewed paper derivations until an independent non-model verification is recorded.

## 11. Deliverables

This PLAN.md, as the first commit. Then REPORT.md in this directory, containing:
- the ledger table (Q1);
- the Q2 table and the verdict generated by §6;
- Q3;
- the controls;
- the productivity verdict;
- open nodes, including dependencies on unit C;
- findings for routing, listed and not edited;
- off-`main` reference tracing (§A.42 item 8);
- a verification-status and remediation table (§A.46 item 4).
