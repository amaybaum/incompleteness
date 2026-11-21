# OIQM-LEAN P3: proof obligations for claims accepted since #1517

**Standing.** WIP / UNVERIFIED. This is a round-4 design unit for #1169 (c.7067281228), stacked on #1517 at
`81888955`. The plan is `PLAN.md` in this directory, committed first.

This record writes Lean statements to be proved:
- no `.lean` file, no build and no computation;
- no manuscript edit, no adopted premise, and no imported operation counted as native.

**Conventions.**
- **Pins.** Base `origin/main` is `df6da1c6`. Kernel paths are under `verification/lean-mathlib/OIBridge/`.
  Mathlib is `v4.33.0` (`db584cd6`), and every Mathlib name was checked there.
- **Labels.** They follow #1517's convention:
  - **(N):** the statement's premises are native, or it has none, which covers pure mathematics about a
    definition.
  - **(I):** the statement equates or constrains a native quantity using imports, each written as a
    hypothesis or field.
- **Obligation IDs** continue #1517's sequence from PO-20. IDs are identifiers, not ordinals.
- **Layer tags** follow the round-4 layer rule. Each obligation names its layer and stays at it:
  - Eff / In / Acc: effect, instrument or accessible algebra;
  - Ont / Born: ontic or Born-form;
  - Typ / Snd / Op: typing, soundness or operational.

## 0. Acceptance check (PLAN step 1)

| Input | Confirmed pin (verdict) | Head used | Delta pin → head | Used |
|---|---|---|---|---|
| OPRES #1511 | `5a6b2a80` (CONFIRMED WITH NITS, c.7066452685) | `7669e511` | one commit, NOTE §0 summary only | Proposition D, Remark D′ |
| READOUT-ALG #1513 | `24982679` (CONFIRMED WITH NITS, c.7066859754) | `4554dd63` | one commit, NOTE §0 wording | RA-1′ for items 2, 3, 5–10 |
| GATE-A r5.8 #1503 | `109b9590` (CONFIRMED, c.7067277470) | `109b9590` | none | P-ST as integrated, and its failure list |
| OIQM-UNBOUNDED P2 #1516 | `1195f2c2` (CONFIRMED WITH NITS, c.7066822325) | `e1715cdd` | nit commit: the C-T ancilla clause and the In label | Lemma P, Corollary P, C-T |
| BQ1 #1498 | CONFIRMED WITH NITS (c.7064968130); nits at `3269772a` | — | — | **excluded**: its Lean form belongs to the BQP ladder (#1498, #1514) |

**Covered by #1517 and not restated:**
- Theorem C, exact form: PO-06, (N).
- Lemma TC: PO-05.
- P-ST items 1 and 2: PO-09.
- S1 and S2: PO-11 and PO-12.

**Excluded:**
- PO-19a, an unreviewed proposal.
- The r5.8 failure item "without FE-ADM … (sketch)", which is marked as a sketch in its source.

**Caution on deltas.** The heads used differ from their confirmed pins by nit commits, which have not
been re-reviewed. The obligations below use only content present at the confirmed pins.

## 1. Obligations

### PO-20 Remark D′: finite visible carriers and any hidden state, in Heisenberg form. Layers: In, Born (algebraic lift), Typ. Difficulty M–H.

- **Lean statement.**

```lean
/-- The hidden algebra is any unital C*-algebra 𝒜_H containing an abstract commutative
"configuration" subalgebra 𝒞_H; a state is a positive unital functional. Finite visible carrier V. -/
structure HiddenSide where
  B : Type; [inst : CStarAlgebra B]
  C : StarSubalgebra ℂ B                          -- the hidden configuration algebra (abstract L^∞)
  comm : ∀ x ∈ C, ∀ y ∈ C, x * y = y * x
/-- The Heisenberg dual of appending ω on the hidden side, read on the visible configuration algebra. -/
def appendDual (ω : hs.B →L[ℂ] ℂ) : (V → hs.B) → (V → ℂ) := fun f v => ω (f v)
theorem appendDual_config (ω) (hω : IsState ω) (f : V → hs.B) (hf : ∀ v, f v ∈ hs.C) :
    ∃ g : V → ℂ, appendDual ω f = g                -- lands in ℓ^∞(V) = (V → ℂ): no normality used
theorem dualDIO_closed : -- Koopman (finite-support bijection) conjugation, readouts with projections
    -- in V → hs.C, feedforward, discard, postselection each map (V → hs.C) into (V → hs.C) or (V → ℂ)
    …
theorem remarkD'_B_i (Φ) (hΦ : GenByDual Φ) {W : Matrix V V ℂ} (hW : W ∈ Matrix.unitaryGroup V ℂ)
    (hnm : ¬ IsMonomial W) {p : ℝ} (hp : 0 < p) : ¬ (∀ i, Φdual (single i i 1) = (p : ℂ) • (Wᴴ * single i i 1 * W))
```

- **Kernel identifiers.** `IsMonomial` (SubstratumInterface.lean:50), `IsState` (QuasilocalCharacterization.lean:196), and #1517's PO-04 (`NoDetect`)
  for the finite case.
- **Mathlib.**
  - `CStarAlgebra` (Analysis/CStarAlgebra/Classes.lean:38).
  - `StarSubalgebra` (Algebra/Star/Subalgebra.lean:26).
  - `Matrix.unitaryGroup` (LinearAlgebra/UnitaryGroup.lean:60).
  - `Matrix.instCStarAlgebra`, scoped L2Operator (Analysis/CStarAlgebra/Matrix.lean:294, :297).
- **Hardest step.** Stating the Heisenberg dual of a protocol without Kraus forms. OPRES uses none.
- **Label.** (I). The algebraic lift is a hypothesis: the protocol is given by its dual on
  `V → hs.B`. Normality is not needed, which is D′'s point.
- **E/A/M.**
  - E: Remark D′, layer X (#1511).
  - A: the algebraic lift (KIN).
  - M: the Lean text.
- **§A.35.** New module `CoherenceResourceDual`, kernel-only.

### PO-21 Proposition D: measurable carriers, the detection half (exact part). Layers: In, Born, Typ. Difficulty R.

- **Lean statement.**

```lean
variable {V : Type} [Fintype V] [DecidableEq V] {H : Type} [MeasurableSpace H] (ν : Measure H)
/-- Nonsingular measurable bijection of V × H (counting × ν). -/
structure NonsingularBij where
  T : (V × H) ≃ᵐ (V × H)
  qmp : MeasureTheory.Measure.QuasiMeasurePreserving T (count.prod ν) (count.prod ν)
  qmp_symm : MeasureTheory.Measure.QuasiMeasurePreserving T.symm (count.prod ν) (count.prod ν)
/-- Koopman unitary on L²(V × H) with the Radon–Nikodym factor. -/
noncomputable def koopman (T : NonsingularBij ν) : MeasureTheory.Lp ℂ 2 (count.prod ν) →L[ℂ] MeasureTheory.Lp ℂ 2 (count.prod ν)
theorem koopman_unitary (T) : (ContinuousLinearMap.adjoint (koopman T)) * koopman T = 1
theorem koopman_conj_mul (T) (g) : koopman T * mulOp g * ContinuousLinearMap.adjoint (koopman T) = mulOp (g ∘ T.symm)
/-- The normal slice map is carried as a FIELD (Mathlib theory not located in this check). -/
structure NormalSlice (ω) where
  slice : (V × H → ℂ) →ₗ[ℂ] (V → ℂ)
  slice_mul : … ; slice_unit : …
theorem propD_dual_preserves (Φ) (hΦ : GenByMeasurable ν Φ) (σ : NormalSlice ω) :
    ∀ i : V, ∃ f : V → ℂ, Φdual (indicator i) = mulOp f        -- Φ*(|i⟩⟨i|) ∈ ℓ^∞(V)
theorem propD_B_i … : ¬ (Φ = p • conjChannel W) for non-monomial W         -- B(i), V finite
```

- **Kernel identifiers.** None directly. `ReversibleDynamics` (QuasilocalAlgebra.lean:956) is the
  finite-range analogue.
- **Mathlib.**
  - `MeasurableEquiv` (MeasureTheory/MeasurableSpace/Embedding.lean:179).
  - `MeasureTheory.Measure.QuasiMeasurePreserving` (MeasureTheory/Measure/QuasiMeasurePreserving.lean:43).
  - `MeasureTheory.Measure.rnDeriv` (MeasureTheory/Measure/Decomposition/Lebesgue.lean).
  - `MeasureTheory.Lp` (MeasureTheory/Function/LpSpace/Basic.lean:89).
  - `ContinuousLinearMap.adjoint` (Analysis/InnerProductSpace/Adjoint.lean:114).
  - `VonNeumannAlgebra` (Analysis/VonNeumannAlgebra/Basic.lean:67), for 𝒜 as a double commutant if
    used.
  - The Koopman unitary with a Radon–Nikodym factor on `Lp 2` was **not located**, and is part of the
    obligation.
- **Not included.**
  - Proposition D's approximate part (ii), and Theorem C(b) in measurable form. Both need the trace
    or diamond norm, which is a real gap. Each would be a separate obligation with that norm as a
    hypothesis.
  - The continuous-PVM Lüders instrument, which OPRES excludes.
- **Label.** (I). Imported:
  - KIN, the Born-form lift on L²;
  - nonsingularity, in the field `qmp`;
  - normality, through the `NormalSlice` field.
- **E/A/M.**
  - E: Proposition D, layer X (#1511).
  - A: KIN, nonsingularity and normality.
  - M: the Koopman construction and the slice theory in Mathlib, both mathematics.
- **§A.35.** Module `CoherenceResourceDual`, kernel-only.

### PO-22 RA-1′: instrument-level DIO for the corpus readouts, items 2, 3 and 5–10. Layers: In (complete instruments with state update), Born. Not Eff, not Acc. Difficulty M.

- **Lean statements.** They use #1517's `NoDetect`, which is PO-04, together with one general lemma.

```lean
/-- General (N): every branch of a Kraus family with row-monomial operators is DIO-type. -/
theorem noDetect_of_rowMonomial {K : Fin n → Matrix S S ℂ} (h : ∀ k, IsRowMonomial (K k)) :
    NoDetect (∑ k, conjChannel (K k))
-- item 2: the permutation channel of the visible history (EquivalenceChain.lean:242, `Phi`)
theorem noDetect_Phi (φ : Equiv.Perm (V × H)) (μ : H → ℂ) (t : ℕ) : NoDetect (Phi φ μ t)   -- (MIO side: `isDiag_Phi`, :253)
-- item 3, finite form only (H finite): K_C = Σ_{x∈C} |A_t(x,h)⟩⟨x| row-monomial
theorem noDetect_historyReadout_fin … : NoDetect (historyInstr A_t C)
-- item 5: classical intervention dilation = conjugation by a permutation: PO-04 `noDetect_conj_of_monomial`
-- item 6: the native ancilla readout field
theorem noDetect_readout (T : FiniteOperationalTheory A) (n) (k : Fin n) : NoDetect (T.readout n k)
  -- via `readout_is_localLuders` (OperationalAssembly.lean:658) and `localLuders` (:191)
-- item 7: `InstAvail.readout` (ImplementationLocality.lean:268): conjugation by a diagonal projector
--          `readProj` (:256) is monomial ⇒ PO-04
-- item 8: the recorder
theorem noDetect_recordInstr (a : A) : NoDetect (recordInstr a)       -- InternalObserver.lean:249, :252
-- item 9: block-passive and passive instruments
theorem noDetect_of_blockPassive (hF : IsBlockPassiveInstrument F) (a) : NoDetect (F a)
  -- via `central_classification` (CentralObservation.lean:433), `branch_scalar_on_block` (:392)
theorem noDetect_of_passive (hF : IsPassiveInstrument F) (a) : NoDetect (F a)   -- PassiveObservation.lean:203, :215
-- item 10: composites of the above: PO-04's closure lemmas
```

- **Layer discipline.**
  - These are **instrument**-level statements: they constrain the full branch maps, including state
    updates. They are not effect-level statements, which READOUT-ALG's RA-1 already covers, and they
    say nothing about the **accessible algebra**, which is Open (Str:742, Str:788, Main:722, GR:366).
  - Items 1, 4, 11, 12 and 22 have no obligation here. RA-1′ leaves them Open for DIO.
  - R-READ stays UNRESOLVED.
- **Mathlib.**
  - `Matrix.diagonal` and `Matrix.diag`.
  - `Matrix.single` (Data/Matrix/Basis.lean:34), with `Matrix.ext_iff_trace_mul_left`
    (LinearAlgebra/Matrix/Trace.lean:274) available for the extensional steps.
- **Hardest step.** Item 9: extracting a diagonal Kraus form for each branch from
  `central_classification`.
- **Labels.**
  - `noDetect_of_rowMonomial` is (N), pure algebra.
  - The item instances are (I). KIN enters as the Born-form typing of each corpus readout as a complex
    channel.
  - Item 6 adds READ: the native interpretation of the `readout` field, an open obligation (EP:25).
  - Item 3 is stated only for finite H. The measurable form is PO-21's setting.
- **E/A/M.**
  - E: RA-1′, layer X from K (#1513).
  - A: KIN, plus READ for item 6.
  - M: whether all native instruments are DIO, which is Open and physical.
- **§A.35.** Module `CoherenceResource`, kernel-only. It imports EquivalenceChain, CentralObservation,
  InternalObserver and PassiveObservation, which are in `current` families, and edits none of them.

### PO-23 P-ST as integrated: the BF / I-4 incompatibility on non-monomial targets. Layers: Born, Op. Difficulty M, given PO-09 and PO-11.

- **Lean statement.**

```lean
theorem bf_i4_incompatible [Fintype H] (M : NativeModel A) (φ : Equiv.Perm (V × H)) (ω : Matrix H H ℂ)
    (hω : ω.PosSemidef ∧ ω.trace = 1)
    (hborn : ∀ t ρ, bornFamily M s t ρ = bornLift φ ω t ρ)          -- the model's Born family is a bijection lift
    (hI : ∀ k p π h, M.law p π h = qLaw p.ρ π h) (hFE : FE_ADM M s Λ) (hBF : BF M s)
    {W} (hW : W ∈ Matrix.unitaryGroup V ℂ) (hΛ : Λ 1 = conjChannel W) (hnm : ¬ IsMonomial W) : False
-- proof: PO-09 `p_st_born` gives bornFamily M s 1 = conjChannel W; `hborn` and PO-11 `s1_monomial`
-- give IsMonomial W; contradiction.
theorem t2_indexing_needed (Φ : ℕ → Channel A) {Λ Λ'} (hne : Λ 1 ≠ Λ' 1) : ¬ (Φ = Λ ∧ Φ = Λ')
-- (N), typing: an A-indexed sector carries one autonomous family (#1510 T2)
```

- **Kernel identifiers.** #1517's PO-09 and PO-11. `familyAt` (SemigroupTransfer.lean:93) is the
  uniform special case of `bornLift`.
- **Mathlib.** As for PO-11.
- **Labels.**
  - `bf_i4_incompatible` is (I). Its imports are hypotheses: FE-ADM (`hFE`), BF (`hBF`), and S1's
    (b)–(d) through `hborn`, a fixed ω, and the unitary target on all ρ.
  - `t2_indexing_needed` is (N) and trivial, a typing fact.
- **Scope.** Finite H only. #1508's S1 is on countable H.
- **E/A/M.**
  - E: r5.8 §2.4, CONFIRMED.
  - A: FE-ADM, BF, (b)–(d).
  - M: a physical source for FE-ADM and BF.
- **§A.35.** Module `SingleTime`, kernel-only.

### PO-24 Lemma P: compatibility of the coherence pair along stages. Layers: In, Born. Difficulty M.

- **Lean statement.** Every iff below has both directions as separate named lemmas (§A.34).

```lean
-- (i) inert-spectator extension, both predicates
theorem preservesDiag_inclObsMap_iff (h : Λ ⊆ Λ') (Φ) : PreservesDiag (inclObsMap h Φ) ↔ PreservesDiag Φ
theorem noDetect_inclObsMap_iff (h : Λ ⊆ Λ') (Φ) : NoDetect (inclObsMap h Φ) ↔ NoDetect Φ
--   (→) via Φ = Tr_{Λ'∖Λ} ∘ inclObsMap h Φ ∘ (· ⊗ |x₀⟩⟨x₀|), append and discard being MIO and DIO
--   (←) via PO-04 closure (⊗ id)
-- (ii) conjugation by a monomial unitary, both predicates
theorem preservesDiag_conjMono_iff (hM : IsMonomial M) (hMu : M ∈ unitaryGroup _ ℂ) (Φ) :
    PreservesDiag (conjChannel M ∘ₗ Φ ∘ₗ conjChannel Mᴴ) ↔ PreservesDiag Φ
theorem noDetect_conjMono_iff … : NoDetect (…) ↔ NoDetect Φ
-- (iii) Heisenberg: the substratum automorphism maps the configuration subalgebra onto itself
theorem heisQ_configAlg (Φ : ReversibleDynamics ι Q) : heisQ Φ '' configAlg ι Q = configAlg ι Q
-- Corollary P, two directions stated separately
theorem pair_of_stage_sub (h : Λ₀ ⊆ Λ) : HasPair 𝓘 Λ₀ → HasPair 𝓘 Λ       -- needs 𝓘 closed under inclObsMap
theorem pair_of_stage_sub_rev (h : Λ₀ ⊆ Λ) : HasPair 𝓘 Λ → HasPair 𝓘 Λ₀   -- the (←) direction, as stated in #1516
```

- **Caution on the (←) direction.** #1516 calls it trivial. Read literally, it requires `𝓘` to be
  closed under restriction, which #1516's Corollary P assumes: "those stages carry a pair" implies
  "Λ₀ does". The design keeps it as a separate obligation, with that closure as an explicit
  hypothesis (`hrestr`), and does not call it trivial in Lean.
- **Kernel identifiers.**
  - `inclObs` (RegionTower.lean:123), `inclObs_trans` (:152).
  - `heisQ` (QuasilocalAlgebra.lean:1264), `heis_iterate_emb` (:1330), `stage_inclObs` (:700).
  - `preservesDiag_amplRef` (DiagonalTheory.lean:132), `preservesDiag_withSpectator` (:151),
    `preservesDiag_discardWith` (:229), `preservesDiag_comp` (:94).
  - `preservesDiag_conj_of_monomial` (SubstratumInterface.lean:101).
  - `InertSpectatorCompositionality` (SpectatorBridge.lean:223).
- **Mathlib.** `Matrix.kroneckerMap`, `Matrix.reindex`, `Equiv.piEquivPiSubtypeProd`
  (Logic/Equiv/Prod.lean:468), `StarSubalgebra`.
- **Label.** (N): pure algebra on definitions under #1517's convention. KIN gives "coherence" its
  physical reading only when the maps are read as native operations, and that reading is not in
  these statements.
- **E/A/M.**
  - E: Lemma P and Corollary P, X (#1516).
  - A: none in the statements. `hrestr` is a hypothesis of the (←) corollary.
  - M: the Lean text.
- **§A.35.** Module `CoherentTower`, kernel-only.

### PO-25 C-T at the typing layer: generated availability equals the Kraus instruments. Layers: In, Born, **Typ only**. Not Snd of a physical realization, not Op. Difficulty H.

- **Lean statement.**

```lean
/-- C-T's generated availability on stage Λ (|Q| = 2): an inductive closure whose generators are
the IMPORTS (fields of the generating data) and whose rules are composition, inert-spectator
extension, transport, feedforward, coarse-graining and fresh-ancilla append/discard. -/
inductive CTAvail (ι : Type) [DecidableEq ι] : (Λ : Finset ι) → (m : ℕ) →
    (Fin m → Channel (Conf Λ (Fin 2))) → Prop
  | perm  (σ : finite-support bijection) : CTAvail Λ 1 (fun _ => conjChannel (permMatrix σ))
  | phase (d) : CTAvail Λ 1 (fun _ => conjChannel (phaseOperator d))       -- `phaseOperator_supplied`
  | readout (i ∈ Λ) : CTAvail Λ 2 (configReadout i)
  | plus  (CR) : … append |+⟩ on a fresh site, discarded within the family   -- import CR
  | det   (DET) : … the destructive ⟨±| detector on one site, re-appended      -- import DET
  | comp … | ext (h : Λ ⊆ Λ') … (IS) | transport … | ff … | coarse …
theorem ct_sound (Λ m F) : CTAvail ι Λ m F → IsFiniteEndomorphicKrausInstrument F      -- typing-level soundness
theorem ct_complete (Λ) (hΛ : Λ.Nonempty) (m F) : IsFiniteEndomorphicKrausInstrument F → CTAvail ι Λ m F
theorem ct_exact … : CTAvail ι Λ m F ↔ IsFiniteEndomorphicKrausInstrument F
```

- **Proof decomposition.**
  - **`ct_sound`.** By induction. Every generator is given in Kraus form, and every rule preserves
    Kraus form. So, unlike #1516's paper proof, no appeal to Choi's theorem is needed. That is a
    simplification at the Lean layer, not a change of claim.
  - **`ct_complete`.** Five steps:
    1. W(ii): `H` on both branches from `|+⟩`, `⟨±|`, the diagonal phases, readout and Pauli
       feedforward, which is CC-1.
    2. The ZXZ Euler form gives every single-qubit unitary. The form `R_z H R_z H R_z` is
       elementary 2×2 algebra; no Mathlib Euler-angle lemma was located.
    3. Two-level special unitaries generate SU: `su_mem_closure_twoLevel`
       (DiscreteCompletion.lean:1372), `su_mem_closure_of_suppOn` (:1232), `twoLevel` (:960).
    4. Each two-level unitary comes from single-qubit unitaries and finite-support permutations. This
       needs controlled-U from single-qubit unitaries plus CNOT, the Barenco et al. 1995 lemma, which
       is in neither the kernel nor Mathlib. **This is the hardest step.**
    5. Instruments come from unitaries plus readout: `fullInstruments_of_control`
       (StinespringAssembly.lean:197) and `finiteInstrument_of_ancillaControl`
       (InstrumentDilation.lean:139).
- **Kernel identifiers.**
  - `IsFiniteEndomorphicKrausInstrument` (KrausSoundness.lean:112), `instrumentBranch`, `permMatrix`.
  - `phaseOperator` (SubstratumInterface.lean:58), `phaseOperator_supplied` (StructuralClosure.lean:315).
  - `Conf` (RegionTower.lean:86).
  - The compatibility clauses T1 to T4 of #1516: `inclObs_trans` (RegionTower.lean:152),
    `heis_iterate_emb` (QuasilocalAlgebra.lean:1330, in cone form) and `quasiState_unique` (:879).
- **Mathlib.** `Matrix.unitaryGroup`, `Matrix.det`, `Submonoid.closure`, `Matrix.kroneckerMap`.
- **Label.** (I). The imports are carried as follows:
  - **KIN:** the channel types.
  - **CR:** constructor `plus`, which is not MIO.
  - **DET:** constructor `det`, which is not DIO.
  - **IS:** constructor `ext`, which is `InertSpectatorCompositionality` at the stage level.
  - **INF:** a hypothesis `[Infinite ι]`, only where the tower is used. `ct_exact` itself holds for each
    finite Λ.
- **Layer discipline.**
  - `ct_exact` is a **typing-layer** statement about an availability family.
  - It does not state that any generator is physically implementable. That would be soundness of a
    realization, which is not shown.
  - It does not state any operational law equality. #1504 Node 2(ii) shows there is no ontic
    realization with law equality.
  - It does not meet I-2 or I-3.
- **E/A/M.**
  - E: C-T, X/P, at the typing layer (#1516).
  - A: KIN, CR, DET, IS and INF.
  - M: the Barenco step in Lean, which is mathematics. Physical implementability of CR and DET is
    physical.
- **§A.35.** Module `CoherentTower`, kernel-only. It imports DiscreteCompletion and
  StinespringAssembly and edits neither.

## 2. Productivity verdict (PLAN)

**Criterion 1 holds.** PO-20 to PO-25 are new obligations for accepted claims. None of them is stated
in #1517.

**Criterion 2 holds.** Four obligations had to be placed at a layer below the naive one:
1. **PO-22 is instrument-level, not effect- or algebra-level.** RA-1′ is typed on the full branch maps.
   The Lean statements leave the accessible algebra, Open, and items 1, 4, 11, 12 and 22, which are
   effect-level only, untouched.
2. **PO-25 is typing-layer only.** `ct_sound` is soundness *of the typing*, the fact that generated
   families are Kraus. It is not soundness of a physical realization, and the obligation names that
   distinction.
3. **PO-20 and PO-21 are Heisenberg-dual and Born-form.** They state DIO as `Φ*(𝒜) ⊆ 𝒜` without Kraus
   forms. A Schrödinger-form typing would need a conditional expectation that does not exist on a
   diffuse MASA.
4. **PO-24 exposes an implicit hypothesis.** The (←) direction of Corollary P needs closure under
   restriction, which becomes an explicit hypothesis.

**Outcome: PRODUCTIVE.** This is pending review. Every obligation is a design and nothing is proved.

## 3. Three questions

- **Established.** Nothing in Lean. Each obligation restates a confirmed result at its own layer:
  - Proposition D and Remark D′: X.
  - RA-1′: X from K.
  - P-ST and the S1 combination: X.
  - Lemma P: X.
  - C-T: X/P at the typing layer.
- **Assumed.** All written as hypotheses or fields:
  - KIN;
  - nonsingularity and normality (PO-21);
  - the algebraic lift (PO-20);
  - READ (PO-22, item 6);
  - FE-ADM, BF and S1's (b)–(d) (PO-23);
  - CR, DET, IS and INF (PO-25);
  - restriction closure (PO-24, the (←) direction).
- **Missing.**
  - Mathematics:
    - the Koopman unitary with a Radon–Nikodym factor, and normal slices (PO-21);
    - the Barenco controlled-U lemma (PO-25);
    - the trace and diamond norms, for the approximate parts, which are excluded here.
  - Physical:
    - whether all native instruments are DIO;
    - the operational meaning of the declared observable algebra;
    - the physical implementability of CR and DET.
  - R-READ stays UNRESOLVED.

## 4. Cross-references, not overlapped

- **BQ1 and its Lean designs.** These belong to the BQP ladder (#1498, #1514).
- **The Theorem 24 Lean sketch.** `research/thm24-def-20261121`.
