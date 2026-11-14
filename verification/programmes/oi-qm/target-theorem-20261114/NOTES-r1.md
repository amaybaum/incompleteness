# Notes for TARGET-THEOREM-r1

Read-only unit. Commands used: `ls`, `find`, `wc`, `sed -n`, `awk`, `grep`, `cut`, `git log -1`, and a Python text replacement on the two files in this folder. No interpreter was run on any OI model, no Lean build, no probe. GitHub was read, not written: the bodies of Issues #914, #1217, #868, #1236, #866 and #1169 (no comments).

Pin: `wt-mainread` at `c3b5f37a354bb26437e2e0165c576a347a63c153` (2026-11-13). Off `main`: `wt-bellplan` at `a0fa2502`, `wt-tune1plan` at `ea9bff9c`.

## 1. What was read

**Manuscripts on `main`.**
- `papers/Main.md`: :20, :36 (first 1500 characters), :42–:60, :66–:84 in full, :356, :360, :362–:389 (theorem and proof lines), :412–:416, :427, :431, :534–:604 in full except :574–:578 skimmed, :716–:724 in full, the status table :728–:738 (rows cut at 1200 characters), :740–:756 (cut).
- `papers/Substratum.md`: :123–:133, :171, :173, :193, :195.
- `papers/GR.md`: :226, :240, :256–:260, :262–:288 (cut at 700 to 2600 characters per line).
- Level III wording located by search in `book/ch01-observation.md`:165 and `book/ch19-open-problems.md`:126; these mirrors were not compared line by line with M:588.

**Kernel sources, statements read (not rebuilt).** `Equivalence.lean`, `GeneralCarrier.lean`, `CarrierGeneralOIPlus.lean`, `CompletedOI.lean` (:545–:556), `MinimalRepertoire.lean` (:410–:590), `StructuralClosure.lean` (header, :320–:450), `SubstratumSource.lean` (:55–:100), `JordanClassification.lean` (:1095–:1135), `OIRealization.lean` (:180–:260), `LevelOneSeam.lean`, `KrausSoundness.lean`, `AncillaClosure.lean` (definitions), `RouteB.lean` (:129–:170, :385–:405), `SubstratumInterfaceAudit.lean` (:613–:662, :776–:790, :828), `FrozenSourcing.lean` (:62–:75, :314–:332), `DiscreteCompletion.lean` (:31–:68), `DenseInstrumentBridge.lean` (:492–:506), `PairFlowEquivalence.lean` (:195–:203), `FlowEndpoint.lean` (:145–:160), `LiftAudit.lean` (:112–:120, :190–:204), `ExecSource.lean` (:115–:140), `LiftSource.lean` (:150–:170), `DerivedQ3.lean` (:214–:232), `TypedCompletion.lean` (:835–:870, :940–:948), `TypedPositive.lean` (:25–:50), `QuasilocalAlgebra.lean` (:700–:720, :870–:890), `QuasilocalCharacterization.lean` (:338–:362 and declaration lines), `InstrumentAvailability.lean` (:331–:350), `RankGapTheory.lean` (:698–:716), `RootedClassificationAllTime.lean` (:186–:196), `QuantumRepresentationT3.lean` (:205–:216). A token search for `sorry`, `axiom` declarations and `native_decide` in nine of these files returned nothing.

**Records on `main`.** `verification/README.md` :300–:520; `verification/programmes/oi-qm/PROGRAMME.md` headings, :1–:95, :187–:221, :489–:570, :632–:638 (cut); `verification/ROADMAP.md` :975–:1050; `reconstruction/oi-qm-ext-1/endpoints.md` :1–:125; `oa-1-20261112/STATUS.md` in full; the "What the record establishes" sections of the OA-2, OA-3 and W1-1 status notes; `drafts/tune-1-20261111/TUNE-1-STEP1.md` :1–:60 and `TUNE-1-STEP2-SESSION4.md` :423–:470; one entry of `verification/coverage/LEDGER.json`.

**Records off `main`.** `bell-landing-20261114/STATUS-LADDER.md` :1–:140; the "supports", "Hypotheses" and "Limitations" sections of `STATUS-BS.md` and `STATUS-SB-L3.md`; `LANDING-PLAN.md` :1–:40 and searches. `tune1-landing-20261114/STATUS-STEP3A.md` and `STATUS-SOURCING.md`, the same three sections; `LANDING-PLAN.md` :236–:280.

## 2. Kernel statements as read

| Identifier | File:line | Carrier | What the statement says, with its hypotheses |
|---|---|---|---|
| `finite_horizon_equivalence` | Equivalence.lean:462 | any `Fintype V`, any K | for `P : Traj V K → ℝ`: `Stochastic P ↔ RevRealizable P`, `RevRealizable P ↔ QfbRealizable P`, `QfbRealizable P ↔ Stochastic P`; `RevReal` is a bijection of `V × Hid` with an initial law on the product, not required to factor |
| `exactAll_iff_physical_general` | GeneralCarrier.lean:100 | every nonempty finite `A` | `ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T` for every `T : FiniteOperationalTheory A`; no further hypothesis; the theory's operations are linear maps on complex matrices |
| `main_result` | GeneralCarrier.lean:188 | as above; witnesses on `Fin 2` | the characterization, joint satisfiability, the five independence witnesses (each also realizing the sealed core), and a core-realizing theory that is not QM |
| `carrier_general_oiPlus` | CarrierGeneralOIPlus.lean:213 | every nonempty finite `A` | `OIPlus T ↔ ExactAllFiniteEndomorphicQuantumOps T`, with `OIPlus T := WellFormed T ∧ ObservationalIndependence T ∧ ReversibleRichness T ∧ ObserverRecursion T` (:185); no OI-core conjunct |
| `oiPlus_independence` | CarrierGeneralOIPlus.lean:230; CompletedOI.lean:506 | `Fin 2` | three theories, each well-formed with two of the principles and failing the third; in the `CompletedOI` form each also carries the sealed core |
| `oiPlusMin_iff_qm` | MinimalRepertoire.lean:569 | every nonempty finite `A` | `OIPlusMin T ↔ ExactAll…`, with `OIPlusMin T := ImplementationLocality T ∧ PhaseFreeRichness T ∧ EmbeddedObservation T` (:544); `PhaseFreeRichness` (:423): at every level with two or more states one pair is driven at every real time and every exchange is available |
| `substratum_plus_control_qm` | StructuralClosure.lean:414 | every nonempty finite `A` | for an implementation class `𝓘` with `ExtendsSubstratum 𝓘`, `StructurallyClosed 𝓘` and `DrivesElementary 𝓘`: `ExactAll… (genTheory 𝓘 _ A)`; the first hypothesis is unused in the proof term; `DrivesElementary` (SubstratumSource.lean:77) asks for the transition flows at every real time, the exchanges and the quarter phases on every carrier |
| `qm_generated_by_substratum_extension` | StructuralClosure.lean:423 | every nonempty finite `A` | if `T` is exact QM then some class extends the substratum class, is structurally closed, drives the elementary transitions and generates `T`; the witness is `fullClass`, the class of all operators |
| `substratumGen_not_control` | StructuralClosure.lean:348 | `Fin 2` | `¬ HasCompositeUnitaryControl (genTheory substratumClass _ (Fin 2))`; `substratumClass` is the predicate `IsMonomial` (:180); the proof uses the rotation `rot` at level one and diagonal preservation |
| `sameData_unitary_or_transpose` | JordanClassification.lean:1109 | `n × n` complex matrices | hypotheses: two Hermitian menus `G₁`, `G₂` each spanning the matrix space and equal to 1 at a common index; two positive-semidefinite families `σ₁`, `σ₂`, each separating and each generating the positive cone with nonnegative coefficients; equal traces `tr(G₁ᵢ σ₁ₖ) = tr(G₂ᵢ σ₂ₖ)`. Conclusion: a linear `Φ` with `Φ(G₁ᵢ) = G₂ᵢ` and a `W` with `Wᴴ W = 1` such that `Φ` is `X ↦ W X Wᴴ` or `X ↦ W Xᵀ Wᴴ` |
| `sourcedOI_qm_iff_phaseFree`, `obs_sourcedOI` | SubstratumInterfaceAudit.lean:654, :828 | every nonempty finite `A`; every `Substratum 𝒮` | `SourcedOI T → (ExactAll… T ↔ PhaseFreeRichness T)`; `SourcedOI (obsTheory 𝒮)` |
| `frozen_sourcing_verdict` | FrozenSourcing.lean:318 | `Fin 2` | `permTheory (Fin 2)` has no `PhasesAvailable`, no `DenseUnitaryControl` and not `DerivedOI` |
| `derivedOI_qm_iff_layerFlowExecutable'` | DerivedQ3.lean:222 | every nonempty finite `S` | under `DerivedOI T` and an involution `σ` with a moved point: `ExactAll… T ↔ LayerFlowExecutable T σ` |
| `obs_not_layerFlowExecutable` | ExecSource.lean:129 | every `Substratum 𝒮` | no layer flow of a permutation with a moved configuration is executable in `obsTheory 𝒮` |
| `typed_determined_iff` | TypedCompletion.lean:850 | all nonempty finite carriers | the shadow is quantum on every nonempty carrier exactly when typed availability coincides with the typed Kraus instruments |
| `canonEquiv`, `canon_unique` | QuasilocalCharacterization.lean:350, :359 | site type `ι`, alphabet `Q` | a star-algebra isomorphism from the region completion to any `QuasilocalSystem`, agreeing with the stages; any continuous map agreeing with the stages is that map |
| `krausDense_of_fixedGate` | DenseInstrumentBridge.lean:502 | `Fin 2` | `DerivedOI T`, `α/π` irrational and `FixedGateSourced α T` give `KrausDense T` |

## 3. What could not be checked, or was not traced

1. No statement was rebuilt or re-derived. Research-record statuses are transcribed from their status notes; their mathematics was not checked.
2. The Bell records themselves (`BELL-LADDER-r3.md`, `BELL-SCOPE-UNIT1.md`, `SB-L3.md`, #1274's `NEW-RESULTS.md` where N4 is stated) and the TUNE-1 reports in `wt-3a/` and `wt-tune1src/` (`TUNE-1-STEP3A-r3.md`, `TUNE-1-SOURCING-r2.md`) were read only through the status notes and landing plans. The owner decisions those notes quote were not read at source.
3. "OICORE-1": no file or text of that name was found under `verification/` on `main` at the pin. "MATH-CON-1": the only record of that name on `main` is `reconstruction/mathcon1-polc-20261108/DESIGN.md`, not read. The "dependency matrix" was read as the body of Issue #914; no file of that name is on `main`. The apparatus records (`apparatus-1-20261107/DESIGN.md` and related) and the `physical-realization` rounds other than the W1-1 status note were not read.
4. Strictness of the all-time inclusion at `Fin 2`: `qStar_pdFamily` was located; the theorem that its family is not `PPer` was not located (marked "not traced" in T1∞). PG:197–206 is the source used.
5. F1's statement that conditions (i), (ii), (iii), (v) follow for the generated theories is a composition of lemma names read in the proof term of `qm_of_oiPlusMin`; the lemmas' own statements were not opened.
6. No Issue was found for: the finite-precision bound of the gluing theorem, a kernel statement of the ε-theorems, the unitary/transpose orientation, a converse to the Level III theorem. #1217 concerns the complex structure on the six-link carrier of the SM gauge decomposition, not the complex matrix kinematics of the operational characterization; the latter is tracked by #914 rows 3–7 and the frozen ROADMAP row "P1 — K".
7. Issues #1147, #1274, #1283, #1007 and #1143 were not read; #1147 and #866 are cited for O-RDY on the authority of `TL/LANDING-PLAN.md`:243–:252.
8. `papers/SM.md`, `papers/Structure.md`, `papers/Introduction.md`, `papers/Methodology.md`, Main §2 and §3.1–§3.2, and the book chapters were not read; a statement of "full equivalence" in those texts, if any, is not reflected here.
9. For `finiteSupport_iff_kraus`, `iterate_dependsOnlyOn_ball`, `oiSystem`, `systemEquiv_unique`, `pushforward_identity`, `qStar_pdFamily` and `permTheory_phase_ceiling` only the declaration line was read; their descriptions in the main document follow `verification/README.md`, `PROGRAMME.md` or the manuscript.
10. Whether Main's ε-realization of a Bell experiment lies inside or outside the screened class of the Bell-scope record is not classified by any source read.

## 4. Points where the brief and the sources differ

- The brief gives CHSH ≤ 2 "for the linear nearest-neighbour rule under measurement independence". The Corollary at M:414 carries further conditions: setting interventions at one step on disjoint wing regions, each reading and writing only its own, and each wing's ±1 outcome, recorded in every run, read outside the other wing's graph cone.
- The brief places the finite-carrier obstruction at M:562 and M:600 item 3. Both lines restate it; the Proposition and its proof are at M:558.
- The brief names the OI⁺ principles as characterizing QM "on a carrier and its composites". In the kernel the general-carrier `OIPlus` has no OI-core clause, so the left side of that equivalence is a list of operational principles (recorded under T3).
