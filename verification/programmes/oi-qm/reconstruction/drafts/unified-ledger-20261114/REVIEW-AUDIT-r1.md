ACCEPT WITH CHANGES

# Independent review of COVERAGE-AUDIT-r1

This review is read-only, paper-only and non-author. Papers and book chapters were read from `main` at
`dfeec843`. The file reviewed is `COVERAGE-AUDIT-r1.md`, identical to the copy on PR #1292 at `edc50055`
(SHA-256 `a029fc76…c1489`, matching the README entry in that commit). No file other than this review was
written, no computation was run and nothing was posted.

References of the form "A:n" are lines of `COVERAGE-AUDIT-r1.md`. Paper and book references are physical
lines at `dfeec843`.

## Summary

The audit is careful, and most of it is right. In particular:
- Its counts reconcile exactly with its tables.
- Structure's absence from the ledger is real.
- Most entries checked at source are accurately located and paraphrased.

Five of its ten highlighted findings need correction. Four were read without the passage that qualifies or
resolves them (§A.19):
- finding 9: the Lemma 1 status;
- finding 5: Σm_ν;
- finding 4: the prediction counts;
- finding 2, in part: the use of Theorem 22.

Finding 6 miscodes the PMNS rows as uncovered.

Several proposed rows give the DM class to results tied to the SM branch's lattice model or to one
displayed update. This conflicts with r3's DM definition and with condition 4. One displayed bidirectional
correspondence that falls under §A.34 is not recorded.

All of these are local corrections, and none needs the audit to be redone.

## Should-fix

**S1. Finding 9 and M-29: the corpus resolves the Lemma 1 status (§A.19).** (A:110–114, :154, :433)

The audit sets Main:700 against GR:90 and SM:46 and records a mismatch. GR states the reconciliation itself.
- GR:585: "Lemma 1 (independent in Part I; consequence of geometry in Part II)".
- GR:565: Lemma 1 is "motivated by the classical fact that finite-area boundaries admit finitely many modes".
- Main:700 calls holographic bounds "downstream physical results" and says only that invoking them "at the
  foundational layer" would be circular. Its own last sentence calls them "compatible with the finiteness
  assumed here".
- GR:90 and SM:46 are downstream realization statements, where that input is admissible.

The statements apply at different layers and do not conflict. Withdraw the CM code and the proposed §11
question.

One point can stay, as a nit: GR:90's "Lemma 1 is a consequence of partition geometry" is looser than GR:585.

**S2. Finding 5 and G-15: the anchor is wrong.** (A:88–93, :209, :437)

The audit sets GR:410 and :524 against SM:1468 ("absolute scale … solution-specific"). But the Σm_ν ≈ 0.059 eV
statement comes from SM's own genericity heuristic: SM:1464, item (iv), "The framework naturally produces
Σm_ν near the minimum allowed by the mass splittings". Appendix A classes the same value L, at Layer 3:
- `book/appendix-a-prediction-status.md`:87 (row 18);
- :112 (G12);
- :130 (N4).

What the record shows:
- GR's word "predictions" promotes a heuristic (ledger B-SM-NU-2, PE) to a prediction. That supports the
  O flag, against B-SM-NU-2, not B-SM-NU-3.
- GR:410's coupling sentence ("both follow from the same lattice structure") has no derivation behind it.
  That part of the finding is right.
- The real internal tension is inside SM: SM:1464 (a near-minimal sum) against SM:1468 (an absolute scale
  that is solution-specific). Appendix A's L class sits on the same line.

Restate the finding and the §11 question in these terms.

**S3. Finding 4 and S-21: the prediction counts are partly a counting convention.** (A:83–87, :184, :435)

The counts use different units:
- Substratum's Class B counts 13 *predictions*.
- SM's table counts 22 *observables*.
- Substratum:199 quotes SM's observable count and attributes it to [SM §7.6].

So :199 and :525 do not contradict each other.

Substratum states one exclusion rule. Inheritors are not counted separately: sin²θ₁₃ is "class C in [SM §7.6];
not counted separately in Class B" (:506). This accounts for part of the C gap, |V_cb| being likewise an
inheritor.

The residue is genuine and should be stated as the finding:
- Koide Q (C in SM) is not listed in Class B.
- λ(M_Pl) = 0 is S in SM. In Substratum it appears only inside the B-M entry for m_H (:514).
- Class B-L swaps m_b via Q_down for a₀.
- Substratum explains none of these differences.

The point about λ(M_Pl) = 0's S class (SM:1314, against the composite-Higgs hypothesis, SM:1116, and
Theorem 11's input status, SM:468) is correct as stated.

**S4. Finding 2, T-5 and SM-38: Theorem 22 is misapplied; the core finding stands.** (A:66–73, :271, :289, :422–423)

The finding stands for C1:
- Structure:733 says random permutations "typically lack the coupled-dynamics … features".
- Structure:717 defines that feature as non-factorization of φ.
- Main:147–151 shows that the factorizing class is a vanishing fraction.

Theorem 22, however, does not bear on random permutations. Its hypothesis is "the wave equation (or any
energy-conserving dynamics) on a connected bounded-degree coupling graph" (SM:1376). It is not "every
connected bounded-degree partition" (A:71).

Remove Theorem 22 from the finding, from SM-38's "Bears on T-5", and from C-STR-1's "contradicted in part by
… B-SM-15" (A:422–423).

Add the book mirror. `book/ch03-structural-realism.md`:26 and its FULL mirror (`FULL.md`:891) carry the same
claim, with a separate coupling argument ("too uniform or too sparse") that Main:147–151 also bears on. This
lies outside chapters 18–19, but a §11 question about Structure:733 needs it under §A.25.

**S5. SM-37 and finding 6: the PMNS values are covered; their forward-test status is not.** (A:94–98, :270)

Ledger C-PRED-1 covers appendix-a rows 12–14 and 19, and N1–N3 and N6 (`book/appendix-a-prediction-status.md`:81–83, :88, :127–129, :132): the three angles and the sum rule. Only the forward-test commitments are absent:
- the octant;
- the 0.005-level sum-rule measurement;
- continued sin²θ₁₃ tightening.

Code SM-37 as CB, keep the O flag, and narrow "untracked" to the forward-test status. The O reading itself is
correct:
- SM:1353 and SM:1360 say "forces" and "forced … no free parameter";
- SM:1314–1316 and footnote ᶠ class the sum rule and θ₂₃ L, pending Cond 2.

**S6. SM-34: the paraphrase inverts the direction.** (A:267)

SM:1118 reads "The observed m_H = 125.10 ± 0.14 GeV is 4–7 GeV below", so the prediction lies above the
observed value. Ledger C-PRED-2 and REVIEW-r3 state it that way. Fix the paraphrase.

The recorded tension among SM:1118, :1126 and the table is mild but real:
- the range is 129–132 GeV at :1118 and 128–132 GeV at :1126;
- :1126 says "~2–3σ", while :1118 says "within the current m_t uncertainty".

Keep it as a question.

**S7. Proposed rows give DM to results specific to the SM lattice model or to one update.** (A:353–355, :393, :396–401)

r3 (r3:54–58) uses DM only for a result that holds for every model of the bare finite class. It explicitly
does not take the SM branch's lattice model as the common model (condition 4). REVIEW-r3 S1 further limits
DM to finite common models. The following proposals use DM outside that scope:

- **B-SM-13.** Theorem 1a and Cor 1a are results on the cubic lattice. Use CD[cubic reference lattice].
- **B-SM-15.** Theorem 22 holds for wave-equation or energy-conserving dynamics on a connected
  bounded-degree graph (SM:1376). Use CD[that dynamics class].
- **B-SM-16.** Appendix A concerns the linear rule on the lattice (SM:1596–1654). Use CD[A5 linear rule, lattice].
- **B-QM-20.** "DM within the stated update". A result for one displayed update at q = 2 is CD[that update].
- **B-BH-8.** "DM within their stated hypotheses" is CD by r3's own definition.
- **B-QM-17.** The persistence form is proved "in the coupling-step model of the physical-memory theorem"
  (Main:736). Scope it to that model.

Inclusion implies no derivation. A proposal's class still has to be honest under the ledger's own
definitions.

**S8. Some proposed rows carry no evidence class.** (A:402–406, :416–417, :428)

Condition 3 requires a class for every entry, and REVIEW-r3 S2 flagged the same pattern in r3. These rows
have none:
- **B-SM-FLAV-6:** "L or C per row at source". These are labels from the S/C/L scheme.
- **B-SM-FLAV-8:** "A retrodiction counted as one test".
- **C-STR-5:** "Scope limit".
- **C-PRED-10 and C-PRED-11:** NEG only. r3 itself uses NEG-only cells, so this item can follow whatever is
  decided for r3.

Give each row a class from {DM, CD, EF, PE, UO}, with the S/C/L label mapped as REVIEW-r3 S2 proposes.

**S9. A displayed bidirectional correspondence that falls under §A.34 is not recorded.** (Substratum:231–233)

Substratum displays "Observed local lattice/gauge data (E1–E7) + Structural assumptions (A1–A6) ⟷
[(S,φ)]_loc/𝒢_sub", introduced as "a bidirectional correspondence". The reverse direction is Theorem 23, which
is a uniqueness or reconstruction theorem. §A.34 says such a theorem is not a converse. Ledger §1 itself calls
Theorem 23 "a uniqueness statement … not a forward derivation". The forward direction would rest on the
conditional SM chain.

The audit applies §A.34 nowhere. Record this display under S-7 (or as its own entry), with each direction's
witness and status. State whether the five papers were searched for other displayed equivalences.

**S10. The O flag is noted but not applied.** (A:198, :219)

- **G-4.** GR:48 marks C2 "**Satisfied**" from τ_B ≳ 1/H, which GR:456 says "is not derived from the
  substratum dynamics". The audit's note says so, but the row is coded C with no O flag.
- **G-25.** GR:536 says "Each follows from partition geometry … no predictions are fit". The table directly
  below records "factor imported", "partly definitional (1 − Ω_B)" and two "in tension" rows. The audit's note
  says so, but the row is coded C with no O flag.

Code both as CM, O and update the summary counts.

## Nits

- **N1. Substratum Stage 2 (finding 3, S-7, S-8).** Add Substratum:201, which lists "the generation count
  exactly three, one Higgs doublet" as residue the theorem returns, and :203, which lists "the generation count"
  among the invariants "forced by representation theory given the lattice". These are stronger than :199,
  where the Higgs is "taken as input". Also note that :161 carries the H-spin′ qualification for physical
  generations, so the Stage 2 text omits the conditions at :151–152 and :165, not throughout.
- **N2. SM-44.** Add SM:847 ("All predictions follow from the cubic-lattice geometry") as a further location.
- **N3. T-6.** The conflict over the dark-sector level is Structure:179 (G3 × D) against Structure:192 and
  GR:30, both of which place the GR results, and the dark-sector phenomenology, at D × G1–G2. The note's
  "GR:30 and 611–679 place the partition-geometry results at the universality level" concerns GR's Tier 1, not
  the items listed at :179.
- **N4. T-4.** Structure:453 conditions the A/4 statement "under the conditions of the horizon calibration
  stated below". The O flag stands, because a bound on "any horizon entropy" is stronger than the calibration.
  Quote the conditional clause, and soften C-STR-3's "unsupported" to "not established beyond the calibration's
  conditions".
- **N5. S-10.** Substratum:239 states that the weak ER=EPR form is recovered "as a structural consequence" of
  a "holographic dictionary" the corpus does not supply (Structure:443–510: no full AdS/CFT). Add the O flag.
- **N6. Missed claims found by sampling.** Add rows for these, or state that they are covered:
  - Structure:703, "OI's substratum produces SU(3) × SU(2) × U(1) uniquely". This omits H-link, H-cust and the
    lattice's selection by the observed group. Flag O.
  - GR:551. A DESI detection of |ν| ~ 10⁻⁴ would require correlated Lorentz violation. This is a cross-sector
    test claim, partly covered by ledger §7.3 and §7.5 (GR:400).
  - GR:587. P-indivisibility carries over to a finite representative of the constraint surface.
- **N7. Appendix-a mapping.** Note in K-table's incidental line (A:334–336) that
  `book/appendix-a-prediction-status.md`:133 itself calls N5 "a heuristic consequence … rather than a
  theorem". The mismatch is the C label alone.
- **N8. Header (A:4–6).** "no repository file was edited" is true of the manuscripts. Commit `edc50055` does
  edit the drafts README, so write "no manuscript or record file".
- **N9. §A.42 item 8.** The audit cites #914 comments 6877871344 and 6877908458 and has no off-`main` reference
  section. Add a one-line classification: provenance, authorization only. Also say that the quoted "Level C
  coverage audit, cross-referenced to GR §6.2" is the recording text of comment 6877908458. It is not the
  owner's verbatim words, which are only "Yes, I approve adding the QCD group to r3".

## Answers to the six checks

**1. Spot-checks at source.** Thirty-three entries were read at source, across all five papers and both
chapters.

Correct as stated:
- M-6, M-33;
- S-8, S-9;
- G-17, G-21, G-23, G-24;
- SM-19, SM-21, SM-25, SM-30, SM-35, SM-36, SM-40;
- T-1, T-3, T-14;
- K-1, K-2, K-3, K-4, K-6, K-9.

Correct but incomplete or mis-coded:
- S-7 (N1);
- SM-37 (S5);
- SM-44 (N2);
- T-4 (N4);
- T-6 (N3);
- S-10 (N5);
- G-4 and G-25 (S10).

Mis-stated:
- M-29 (S1);
- G-15 (S2);
- S-21 (S3);
- SM-34 (S6);
- the Theorem 22 part of T-5 and SM-38 (S4).

The five items named in the brief:
- **Structure:733 against Main:147–151:** right for C1. Theorem 22 is misapplied (S4).
- **Substratum Stage 2 against SM:** right, with locations to add (N1).
- **The prediction counts:** partly a convention (S3).
- **Σm_ν:** mis-anchored (S2).
- **PMNS:** right about the forward tests, miscoded as uncovered (S5).

**2. Completeness.** Sampled gaps were checked: Main §2.1–§2.2, §4.2–§4.5; Substratum §1.1, §2, the
dependency list and §6.1; GR §7.4 and §8.1–§8.7; SM §2.5–§2.6, §4.12 and §7 opening; Structure §3–§5 and §9.5–§9.7.

What the sample found:
- one §A.34 display (S9);
- three missed claims (N6);
- missing locations (N1, N2).

Most sampled material is exposition, or is covered by the audit's grouped rows. The coverage is good but not
exhaustive.

**3. Classification.**
- Evidence classes in the audit's own notes mostly match the sources.
- The exceptions are the O flags in S10 and N5, and the proposed classes in S7 and S8.
- The "CB" codes checked are justified: M-3, M-12, S-5, G-9, G-20, SM-11, SM-13, SM-39, T-13. SM-37 should
  join them (S5).

**4. Counts.** A tabulation of the five tables reproduces every cell of A:50–57: 150 claims found, 55 C + 27
CB, 17 CM, 51 U, 28 O and 13 T. Each column sums correctly. S1, S5 and S10 will change some cells.

**5. Scope.**
- **Appendix A.** Condition 6 names five papers and chapters 18–19. Appendix A's B1–B14 and F-rows are outside
  it, so the audit's reading is fair. But r3 (r3:332–334) and REVIEW-r3 S6's replacement text assign their
  classification to the coverage audit, so the item now belongs to neither document. The audit's §5 records
  this honestly. It should also list it as a missing-entry finding against the ledger, since Level C coverage
  falls under condition 2. It can also note that F6–F8 are already mapped and that F13's content is SM:130,
  which is in scope (SM-5).
- **SM §7.** Checking §7 at the level of stated results is a defensible reading, because the sub-derivations
  are proof bodies and the claims are their stated results. However, A:50–57 does not say that the §7 counts,
  and those of the other sections read at reduced depth (A:449–451), are lower bounds. Say so in §1. The
  sample found one missed §7 location (N2).

**6. Inclusion never implies derivation.**
- The header (A:7–8, :21–22) and §4's preamble (A:340–341) make the proposals non-adopting.
- No proposal asserts a derivation the sources lack.
- The status defects are the DM scoping (S7) and the rows without a class (S8).
- The Main-independence observation (A:302–309) is recorded, not traced. That suits the mandate and is
  correctly labelled.

## Checked by the reviewer

- **Mandate.** #914 comments 6877871344 and 6877908458, read through the API.
- **Records.**
  - `COVERAGE-AUDIT-r1.md`, in full.
  - `LEDGER-r3.md`: header and registry (:1–334), §1, §4.5–§4.7, §7 and §11–§13.
  - `REVIEW-r3.md`, in full.
  - PR #1292 at `edc50055`: files and digest.
- **`papers/Main.md`.** 46, 76, 101–107, 145–151, 258, 486, 590–592, 620, 662, 694–700, 704, 714–738.
- **`papers/Substratum.md`.** 28–44, 106–119, 143–203, 225–243, 389, 421–423, 431–459, 468–527.
- **`papers/SM.md`.** 14, 46, 76–86, 456–470, 541–567, 615–617, 815–817, 847, 1114–1128, 1206, 1265–1390,
  1448–1468.
- **`papers/GR.md`.** 12, 24, 30, 44–52, 90, 104, 410, 454–458, 512, 524–551, 557–587.
- **`papers/Structure.md`.** 13, 179, 192, 204–254, 351, 369, 403, 417, 429, 453, 700–746, 950, 1096.
- **Book.**
  - `book/ch19-open-problems.md`: 46, 104–118, 194–196, 226–248, 356, 362.
  - `book/ch18-beyond.md`: 104, 144–152.
  - `book/ch03-structural-realism.md`: 26.
  - `book/appendix-a-prediction-status.md`: 66–200.
- **Searches.**
  - Corpus-wide: "random permutation" and "random bijection".
  - The five papers: "non-renormaliz", "bidirectional", "⟷" and "is equivalent to".
  - The ledger: genericity, Lorentz, Theorem 22 and 24, PMNS sum rule, CMB and Tully–Fisher.
- **Not done.**
  - No Lean or census check.
  - No script run.
  - No line-by-line read of SM §7.1–§7.5 or of the long proof bodies.
