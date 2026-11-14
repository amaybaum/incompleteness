# Response to REVIEW-r1 (TARGET-THEOREM-r1 → r2)

Each finding was checked at the sources it cites before a disposition was taken. "r2 §n" is a section of `TARGET-THEOREM-r2.md`. Sources: `wt-mainread` at `c3b5f37a`; `OB/` = `verification/lean-mathlib/OIBridge/`; `M:` = `papers/Main.md`; `PG:` = `verification/programmes/oi-qm/PROGRAMME.md`. GitHub was read, not written: bodies of #875, #1216, #1060, #899 in addition to r1's six; titles of #945, #1059, #872, #1007, #1055, #1143, #1061, #1032, #913, #1188, #1147 through the REST API. No Lean build and no computation on an OI model.

## Blocking

| # | Disposition | Where applied | Check made; reason if modified |
|---|---|---|---|
| B1 | Applied | r2 §2 T3: (d) removed from the biconditional statement and stated as (d⇒), (d⇐) on their own predicates; §4 Summary; §4 "Documents that differ" D2 (GR:258, GR:274, M:588) | Confirmed: `ImplementationGenerated` (OB/ImplementationLocality.lean:352) quantifies over `0 < N` only; `generated_of_qm` (:1004) uses `h.2` only; `genTheory` (:852–855) defines both `avail` and `availExt` by `InstAvail`; `substratum_plus_control_qm` (OB/StructuralClosure.lean:414) binds `ExtendsSubstratum` to `_`; `levelOne_independent` (OB/LevelOneSeam.lean:353) and `systemLoose_not_exact` (:328); `exactComposite_of_validity_general` (OB/GeneralCarrier.lean:79) is unconditional; `krausFamily_of_exactComposite`, `availExt_of_krausFamily` (OB/PhysicalCharacterization.lean:179, :188) take `ExactCompositeQuantumOps` only. The `systemLoose` countermodel is carried as a reading, not a kernel statement. The displays are recorded as a finding and not repeated (§A.34). |
| B2 | Applied in a modified form | r2 §2 T2 (⇒) and T4b (⇒); §4 O3 split into (a), (b), (c); §4 Summary; §7 question 9 | Confirmed: M:598's object is behaviour sets ("non-quantum operational theories"), with a stated reason and no exhibited witness; M:360's PR table is non-quantum relative to the wing structure. Modification: the review's "Law by law the inclusion holds exactly ([K], `D_imp_Qfb`)" is kept as inclusion in Q_fb, in a dimension the statement does not bound; `D_imp_Qfb` (OB/Equivalence.lean:294) concludes `QfbRealizable`, not membership in Q^(d,m)_K. |
| B3 | Applied; mapping modified | r2 §1.3 (new); §3 "What is already decided" (new, R1–R9); §7 questions 1, 4, 6, 8, 10 rephrased as keep, narrow or supersede; r1's F3 removed and its content stated in R2; findings renamed D1–D4 | Confirmed: PG:21–36, :44–64, :515–545, :634; M:774; M:431; #875 body ("Owner decisions (2026-10-17)", (a)–(d), "These decisions fix the screening criteria only"); #1216 body (Levels A and B, "Level B is the main target", "distinct from #1169's exact question"); #914 §1; the #914 phrase is in its body, not its title. Modification to proposed change 1: T2 is not placed under PG's notion B as sourced; it is described as an ε-form by a constructed realization, with PG:216 ("represented" is a disqualified ground for a sourcing claim). Additions beyond the review: #1169's owner clarification and accepted Gate A contract (R5), #1236's owner decision (R6), Main's adopted Bell branch (R7), the #1273 decisions as quoted in BL/STATUS-LADDER.md (R8), #899's recorded owner decision (R9). The Level B sentence is recorded as Issue text; an owner comment for it was not traced. |

## Should-fix

| # | Disposition | Where applied | Check made; reason if modified |
|---|---|---|---|
| S1 | Applied | r2 §2 T0 (new, before T1); §4 Summary; §5 rows for T0 | Confirmed: M:536–542, M:628 ("neither is formalized in the kernel"), M:632, M:526–528, M:600 (2), M:608, M:696, `unavoidable_hidden_predictive_memory` (OB/HiddenMemory.lean:185). Added: T0's two sides are both non-quantum; (i) enters in one direction; rational-kernel hypothesis of M:516 with M:731's response-table extension. |
| S2 | Applied | r2 §1.1 OI-L row; §2 T1 (⇐); §5 O-RDY evidence cell and the (Obs, μ) row; §7 question 3 | Confirmed: M:516 (rational kernels; "Rationality tracks the prior"), M:522, M:58, M:600, OB/Equivalence.lean:150–156, TL/STATUS-SOURCING.md:43, TL/LANDING-PLAN.md:136. The rationality step is cited to M:516 instead of being carried as hand reasoning; the conclusion for ledger (iv) stays marked as a reading. |
| S3 | Applied | r2 §4 O1 (narrowed), O5 (M:638 added), O7, O8, O9 (new); Summary | Confirmed: M:480, M:486, M:492, M:496, M:600, M:638, M:644, `verification/ROADMAP.md`:73. |
| S4 | Applied; one entry by title only | r2 §5 Issue column | Confirmed by body: #899, #1060, #875, #1216. Confirmed by title: #945, #1059, #872, #1007, #1055, #1143, #1061, #1032, #913, #1147. #1143 is entered beside #1169 for the T2 selection principle and marked "title only", as the review itself calls it unconfirmed. |
| S5 | Applied | r2 §2 T1∞; §4 O5 | Confirmed: `qStar_not_subset_finiteRootedRealizable` (OB/QuantumRepresentationT2.lean:163), `qStar_not_subset_pper` (:169), `pdFamily_not_finiteRootedRealizable` (OB/RootedClassificationAllTime.lean:239), `pdFamily_not_periodicFamily` (:220). |
| S6 | Applied | r2 §2 T4a (⇒), Statement, Status, Witness and Hypotheses cells | Confirmed: `QuasilocalSystem` (OB/QuasilocalCharacterization.lean:168) and `oiSystem` (:187, `[Nonempty Q]`) carry no OI_Q predicate; `OISystem` :463, `oiDynamical` :471, `canon_dyn` :487, `systemEquiv_dyn` :497; header :51–53. |
| S7 | Applied | r2 §2 header sentence on ε-forms; T2 and T4b rows labelled completeness and soundness; T5c split into interface-level completeness, interface-level soundness and native-model level; T3 (e) | Confirmed: `krausDense_of_fixedGate` (OB/DenseInstrumentBridge.lean:502) concludes `KrausDense`, the inclusion QM ⊆_ε OI side, which r1 had labelled (⇒); `KrausSoundExt` is a hypothesis of `denseFiniteQM_of_denseControl` (:496); `shadowQuantum_of_typed` (OB/TypedCompletion.lean:838) concludes `ShadowQuantum`. |
| S8 | Applied | r2 §2 clause B, adopted branch; §4 Summary ("Posited"); §5 | Confirmed: Sub:133, Sub:193, M:414, M:427, #1060 body. |
| S9 | Applied | r2 §5: rows for Kochen–Specker, Born statistics across settings, (Obs, μ), physical C4, the native instrument, records and reuse, run repetition and H-μ, the relating evolution, the successor problems | Confirmed: M:582, M:570, `papers/Methodology.md`:399; #914 rows 14, 15, 17c, 20 in its body; `ensemble_underdetermined` (OB/StochasticInterface.lean:118); #1169 body ("#1032 and #913 (O-REUSE)"); TL/STATUS-STEP3A.md:88, :94; TL/STATUS-SOURCING.md:84; M:496. |
| S10 | Applied in a modified form | r2 §1.1: fourth bullet, OI-I row, "Extensions" sentence | Confirmed: `obsTheory` (OB/SubstratumInterfaceAudit.lean:770) on `𝒮.Conf`, "under the finiteness A1 supplies" (:769); header :35; `Conf` :78; GR:240, GR:260, GR:284; M:356, M:360. Modification: M:562 is not cited for the phrase, because "bare" does not occur on that line (occurrences: M:66, :214, :352, :354, :356, :360, :554, :582, :588, :774). |
| S11 | Applied | r2 §4 D1 (surfaces M:214, M:352, Sub:373 and RD:320–322 added; the qualification on generated formal theories added); D3 (reconciliation at PG:86 stated) | Confirmed: M:214, M:352, Sub:373; the four lemma statements at OB/ImplementationLocality.lean:957, :971 and OB/EmbeddedObservation.lean:211, :223; EP:25. |
| S12 | Applied in a modified form | r2 §2 T2 (⇐) Bell cell; §6 item 2 | Confirmed: M:572 (4) in full. Modification: the consequence is stated from M:381 alone, as "a realization whose CHSH value exceeds 2 cannot satisfy hypotheses (ii)–(iv) of M:366–373 jointly". The review's version singles out hypothesis (ii) and adds an accuracy statement for no-signalling; M:381 does not say which of (ii)–(iv) fails, and the accuracy statement is not in a source. |

## Nits

| # | Disposition | Where applied | Note |
|---|---|---|---|
| N1 | Applied | r2 §2 T5a (⇒) Witness; §4 O2 Scope | `permTheory_phase_ceiling` (OB/FrozenSourcing.lean:106) has `[Nonempty A]`. |
| N2 | Applied | r2 §2 T5a (⇒) Witness | — |
| N3 | Applied | r2 §2 T2 (⇐) Status | Ledger note confirmed. |
| N4 | Applied | r2 §1.2 Q_fb row; §2 T1 (⇒) Status | `QfbReal.chain` :209, `QfbReal.law` :213. |
| N5 | Applied | r2 §1.1 OI-L row | Confirmed at M:36: Axiom 2 is that "there is more than one moment for the dynamics to act across". |
| N6 | Applied | r2 §1.1 OI-S row | A1–A2 at Sub:123, A3–A6 at Sub:145. |
| N7 | Applied | r2 §2 T3, "Two-state exact form" | `qm_iff_derivedOI_pairFlowSourced` (OB/PairFlowEquivalence.lean:199). |
| N8 | Applied | r2 §2 T4c | M:356 quoted. |
| N9 | Applied | r2 §6 item 5 | S4:3 header confirmed. |
| N10 | Applied | r2 §1.3 first bullet | `papers/Methodology.md`:399 confirmed. |
| N11 | Applied | r2 §4 D4 | #1188 read by title only; stated so. |
| N12 | Applied | r2 §2 clause B, reference rule, Hypotheses | — |
| N13 | Declined, not applicable | — | r1 and r2 cite no Main line taken from #914; every Main line in the document was read at `c3b5f37a`. |
| N14 | Applied | r2 §5 title; §7 question 14 | — |

## Review §4, point 7 (owner questions)

Applied in r2 §7: the initial law (question 3), the realization quantifier (5), the endpoint type (1), the carrier scope (6), the readback sector (11), the Gate A admissibility contract (10), complete-history against selected-read no-signalling and the physical cone (12). r1's questions 1 and 10 are kept as two questions (1 and 14): #899 is a separate accountable Issue for the Level III converse.

## Not changed

- No candidate is recommended and no assessment of OI is made.
- `TARGET-THEOREM-r1.md` and `NOTES-r1.md` are untouched. The limits recorded in `NOTES-r1.md` §3 still hold, except item 4 (closed by S5) and item 5 (lemma statements opened, S11). Additional limits for r2: #875's decision memo, #1216's unit-1 drafts and the comments of every Issue were not read; Issues #945, #1059, #872, #1007, #1055, #1143, #1061, #1032, #913, #1188, #1147 by title only; Main §2 and §3.1–§3.2 remain unread beyond the lines cited.

## Confirmation review (CONFIRM-r2.md)

Each change was checked at its source before it was applied in `TARGET-THEOREM-r3.md`; `TARGET-THEOREM-r2.md` is untouched.

| # | Disposition | Where applied in r3 | Check made; reason if modified |
|---|---|---|---|
| C1 | Applied as given | §2 T1 (⇐) Hypotheses; §2 T0 (ii) ⇒ (iii) Hypotheses | Confirmed at M:518: "The rationality restriction is a property of the uniform-tape presentation, not of realizability"; the response-table form has a product prior independent of $X_0$ and "reproduces the full multi-time joint for arbitrary real kernels"; "The characterization below therefore quantifies over general finite-horizon laws". M:520: the constructive proof's prior is uniform on the tape. r2 understated the paper result. |
| C2 | Applied as given | §2 T2 header, second sentence | Confirmed in the #1216 body: "Can one mechanism derived from OI approximate …", "independently justified observer access", Unit 1 question 1, "A preloaded table of quantum predictions could satisfy Level A without explaining anything"; M:580 for R. |
| C3 | Applied; one pointer modified | §3 R5 and R6 ("What it fixes", "Bears on"); §7 first line; questions 2, 7, 9, 13 | Confirmed verbatim in the #1236 and #1169 bodies. R5's quotation was extended to carry "account for every operation the proposed physical OI interface admits", which question 9 cites. Modification, question 13: the pointer reads "R5: #1169's candidate requirement Meas-1 asks for Born frequencies derived from the extension. R6: Born probabilities and Kochen–Specker contextuality are separate obligations for TUNE-1." The #1169 body does not mention Kochen–Specker (searched), so the proposed joint wording would attribute it to #1169. In question 2, "#1007 and #1055" is marked "titles read". |
| C4 | Applied as given | §2 T5c, soundness at interface level, Status | Confirmed: `krausSoundExt_of_implementationGenerated` (OB/ImplementationLocality.lean:963, nonempty carrier); `ReversibleImplementationLocality` (OB/MicroscopicReversibility.lean:223) is `∃ 𝓘, ImplementationGenerated T 𝓘 ∧ …`; `KrausSoundExt` (OB/CompositeSoundness.lean:123) quantifies over levels `n + 1`. Kept as a reading. |
| C5 | Applied as given | §4 D1 | Confirmed: M:588 says "structural architecture"; RD:320–322 "all of the structural requirements". |
| C6 | Applied as given | §4 D2, last sentence | Confirmed: GR:274–276 cite `typed_determined_iff`, `typed_determined_of_oiPlusMin`, `typed_determined_of_oiPlusPos`. |
