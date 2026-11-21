# OIQM-LEAN P2: formalization dependencies and numbered proof obligations

**Standing.** WIP / UNVERIFIED. This is a preparation-level record for #1169 (P1), authorized at
#1169 c.7066630306. It turns the reviewed designs of #1506 (`DESIGN.md` at `66d1b8e9`, CONFIRMED WITH
NITS, nits applied) into a dependency graph and a list of numbered proof obligations, ordered by
what each one unblocks. Execution and implementation are not authorized by this record.
- No `.lean` file is added, nothing is built, and no theorem is proved here.
- No E, no sector condition C, no new physical assumption and no status is adopted.
- Every Lean block below is a *statement to be proved*.

Base: `origin/main` at `df6da1c6`, which is the base of #1506. Kernel paths are under
`verification/lean-mathlib/OIBridge/`. Mathlib is pinned at `v4.33.0` (`db584cd6`). Every Mathlib name
cited was checked at that tag; names that are *absent* are marked as such.

**Reviewed inputs integrated** (portfolio addendum, #1169):
- OPRES #1511 at `7669e511`: Lemma C, Theorems A′, B and C, Proposition D, Remark D′. All (I) except
  Lemma C, which is (N) as algebra.
- I3-SOURCE #1508 at `df520f3b`: Lemma S1 and Proposition S2, both (I).
- P-ST: the T1/T2 record at `c45b82cf` (#1510). This covers Lemma TC and Proposition P-ST.
- Proposition U, #1504 at `31594967`.

GATE-A r5 #1503 (D5 and D6 decided) and BQ1 #1498 are cross-references only.

**Standing constraints.**
- **R-READ is UNRESOLVED.** R-READ is the question whether native readout effects lie in the
  configuration algebra; READOUT-ALG is checking it. No obligation assumes either answer. A native
  readout appears only as a member of the operation set it belongs to, with its coherence class
  undetermined.
- **O1 is two separate obligations, non-MIO and non-DIO** (#1169 c.7066541026). The obligations keep
  them separate: no obligation infers one from the other.

**Labels: one convention, applied to the Lean statement of each obligation.**
- **(N)** The statement's premises are native, or it has no premise at all. This includes pure
  mathematics about a *definition*, such as lemmas about the comparator `qLaw`, because a definition
  is not an assumption.
- **(I)** The statement equates or constrains a native quantity using an imported quantum or
  operational assumption. Each import is named, with the Lean hypothesis or structure field that
  carries it.
- **Where the comparator counts as an import.** It does so only where a statement identifies native
  behaviour with `qLaw`: in `InclusionAt`, PO-10, PO-16 and PO-18. It does not when a statement is
  about `qLaw` alone.
- **Relation to the #1506 design labels.** This refines them. Those labelled each design by the OI
  claim it serves, and they stand at design level. E/A/M is the owner's Established / Assumed / Missing triple. "Established" here means
established in the cited paper or kernel record, never in Lean by this record.

**Cost.** Every Lean build, kernel and Mathlib alike, runs in CI (§A.40). Difficulty is an estimate:
- S: hours, repackaging.
- M: days, standard finite linear algebra.
- H: weeks, new library-level arguments.
- R: research-grade, needing a Mathlib theory that is absent.

## 0. Dependency graph

```text
Roots (no dependency on another obligation; can start in parallel): PO-01, PO-03, PO-04, PO-05, PO-11.

PO-01 vocabulary ──► PO-02 NativeModel + schema ──► PO-14 D-I.4b
   │                    ├──► PO-08 LawBridge + RecordRetention ◄── PO-03, PO-05
   │                    ├──► PO-09 P-ST ◄── PO-05
   │                    ├──► PO-15 O2-b (via the CoherentTower type)
   │                    ├──► PO-16 D-W ◄── PO-09 (FE_ADM control)
   │                    └──► PO-17 O2-c S-∞ (statement only)
   └──► PO-13 O2-a encoding
PO-03 NativeSource/toTheory ──► PO-07 plug points A/B, controls ◄── PO-06 (part e)
PO-03, PO-02, PO-08 ──► PO-10 inclusion_of_source
PO-04 DIO-type + missing closure lemmas ──► PO-06 Theorem C exact ──► PO-07e O1 split
PO-04 ──► PO-19 Theorem C approximate; D; D′
PO-11 S1 (finite H) ──► PO-12 S2
PO-10, PO-13, PO-15, PO-17 ──► PO-18 O2-d assembly
```

These edges are absent: PO-01 → PO-05, PO-02 → PO-03 and PO-03 → PO-04. Lemma TC uses Mathlib only,
`NativeSource` does not use `NativeModel`, and the DIO predicate uses only kernel definitions.

**Unblocking count**, the number of obligations depending on each, directly or transitively:

| PO | 01 | 02 | 05 | 03 | 04 | 08 | 06 | 09 | 10 | 11 | 13 | 15 | 17 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| obligations it unblocks | 10 | 8 | 5 | 4 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

**Recommended order**, by what each obligation unblocks:
PO-01, PO-02, PO-05, PO-03, PO-04, PO-08, then the rest. The roots PO-01, PO-03, PO-04, PO-05 and PO-11
can start in parallel. The PO numbers are identifiers, not ordinals (§A.30), so they are kept as
first assigned.

## 1. The obligations

### PO-01 Vocabulary of `J_exact(A)` and the comparator law. Difficulty M. Unblocks 10.

- **Lean statement.** These are definitions from DESIGN §4.1, with the setting node required by
  schema clause (c), plus three lemmas:

```lean
abbrev Car (A : Type) (k : ℕ) := A × Fin (k + 1)
structure DensLabel (S) [Fintype S] [DecidableEq S] where
  ρ : Matrix S S ℂ; psd : ρ.PosSemidef; tr : ρ.trace = 1
structure InstrLabel (A) [Fintype A] [DecidableEq A] (k m : ℕ) where
  r : ℕ; K : Fin (r+1) → Matrix (Car A k) (Car A k) ℂ; out : Fin (r+1) → Fin m
  norm : ∑ i, (K i)ᴴ * K i = 1
inductive Prot (A) [Fintype A] [DecidableEq A] : ℕ → Type
  | stop | inst (m) (L : InstrLabel A k m) (next : Fin m → Prot A k)
  | setting (s : ℕ) (next : Fin (s+1) → Prot A k)            -- fresh randomized setting (EP:81)
  | attach (m) (σ : DensLabel (Fin (m+1))) (next : Prot A (joinLevel k m))
  | discard (m) (h : k = joinLevel k' m) (next : Prot A k')
noncomputable def qLaw : Matrix (Car A k) (Car A k) ℂ → (π : Prot A k) → Hist π → ℝ

theorem qLaw_nonneg (p : DensLabel (Car A k)) (π) (h) : 0 ≤ qLaw p.ρ π h
theorem qLaw_sum (p : DensLabel (Car A k)) (π) : ∑ h, qLaw p.ρ π h = 1      -- Fintype (Hist π)
theorem qLaw_prefix … -- the law of a prefix is the marginal of the law of every extension
```

  A setting node carries a declared setting law, uniform on `Fin (s+1)`, so that `qLaw` stays one
  law per protocol.
- **Kernel identifiers it builds on.**
  - `instrumentBranch` (MonoidalCompletion.lean:731), `conjChannel` (:360).
  - `ptraceAnc` (OperationalAssembly.lean:453), `uniformAttach` (:492).
  - The level indexing of `ExactCompositeQuantumOps` (AncillaClosure.lean:364).
  - The Kraus normal form `IsFiniteEndomorphicKrausInstrument` (KrausSoundness.lean:112).
- **Mathlib dependencies.**
  - `Matrix.PosSemidef` (LinearAlgebra/Matrix/PosDef.lean:59), `Matrix.PosSemidef.trace_nonneg`
    (:349), `Matrix.PosSemidef.conjTranspose_mul_mul_same` (:313).
  - `Matrix.trace` (LinearAlgebra/Matrix/Trace.lean:45), `Matrix.trace_mul_comm` (:158).
  - `Matrix.kroneckerMap` (LinearAlgebra/Matrix/Kronecker.lean:55), `Matrix.trace_kronecker` (:398).
  - `Matrix.reindex` (LinearAlgebra/Matrix/Defs.lean:526).
- **Hardest step.** `qLaw_sum`. Completeness `∑ Kᴴ K = 1` has to be pushed through each `inst`
  node, combined with the partial-trace identity at `discard`.
- **Label.** (N), under the convention above: the definitions and the three lemmas are pure
  mathematics about the comparator `qLaw` (EP:110), with no premise. The comparator becomes an import
  (I) only in the obligations that equate native behaviour with `qLaw`.
- **E/A/M.**
  - E: the definitions are fixed by EP:33–41 and EP:110, and reviewed in #1506.
  - A: none for these lemmas. The comparator is a definition here.
  - M: the Lean text.
- **§A.35.** New module `OIQMTarget`, in a new `kernel-only` family with `manuscript: []`. No
  supersession.

### PO-02 Native model, measurability, admissibility schema and the target clauses. Difficulty M–H. Unblocks 8.

- **Lean statement.** This is DESIGN §4.1–4.2 with the confirmed nits applied:

```lean
structure NativeModel (A) [Fintype A] [DecidableEq A] where
  Ω : Type u; [mΩ : MeasurableSpace Ω]; Φ : Ω ≃ᵐ Ω
  Λs : Type u; [mΛ : MeasurableSpace Λs]
  μ : DensLabel (Car A k) → MeasureTheory.Measure Λs; [prob : ∀ p, IsProbabilityMeasure (μ p)]
  ι : DensLabel (Car A k) → Prot A k → Λs → Ω
  R : (π : Prot A k) → (ℕ → Ω) → Hist π
  ι_meas : ∀ p π, Measurable (ι p π)
  R_meas : ∀ π h, MeasurableSet {x | R π x = h}
noncomputable def NativeModel.law (M) (p) (π) (h) : ℝ :=
  ((M.μ p) {λ | M.R π (fun t => (⇑M.Φ)^[t] (M.ι p π λ)) = h}).toReal
def SchemaAdmissible (M) : Prop := UComplete M ∧ Isolation M ∧ FreshSettings M ∧ CausalPrefix M ∧ CompositionalLoading M
def InclusionAt (E) (A) : Prop := ∃ M, E M ∧ SchemaAdmissible M ∧ ∀ k p π h, M.law p π h = qLaw p.ρ π h

theorem law_sum (M) (hM : SchemaAdmissible M) (p π) : ∑ h, M.law p π h = 1      -- sanity: additivity
structure NaturalLoading (Ω) where                                   -- D-I.2 (BORDERLINE)
  load : ∀ 𝔐 : LabelSig.Model, 𝔐.State → ProtOver 𝔐 → Λs → Ω
  natural : ∀ {𝔐 𝔐'} (f : LabelSig.Hom 𝔐 𝔐') s π, load 𝔐' (f.state s) (π.map f) = load 𝔐 s π
```

- **Kernel identifiers.** None directly. `RevReal` (Equivalence.lean:157) is the finite-horizon
  precedent for a reversible model with a pushforward law.
- **Mathlib dependencies.**
  - `MeasurableEquiv` (MeasureTheory/MeasurableSpace/Embedding.lean:179).
  - `MeasureTheory.Measure.map` (Measure/Map.lean:91), `Measure.map_apply` (:161).
  - `MeasureTheory.IsProbabilityMeasure` (Measure/Typeclasses/Probability.lean:64).
  - `ProbabilityTheory.IndepFun` (Probability/Independence/Basic.lean:144), used in `FreshSettings`.
  - `measurable_pi_iff` (MeasurableSpace/Constructions.lean:580), for `R_meas` on `ℕ → Ω`.
- **Hardest step.** `law_sum`. The history events have to be shown to partition the seed space
  measurably. That is the obligation `R_meas` creates.
- **Nonvacuity control.** The witness of PO-16 must satisfy `SchemaAdmissible`. Without it the schema
  could be empty, the failure KERNEL-VAC-1 found for another predicate.
- **Label.** (I). E is a predicate parameter. Unsourced clauses become named hypotheses of any
  inclusion theorem. The choice of `LabelSig` in `NaturalLoading` is E-content.
- **E/A/M.**
  - E: the schema is EP:73–102.
  - A: E.
  - M: a physically justified E, which is I-3.
- **Cardinality neutrality.** The statement is neutral. Every witness has infinite `Ω`.
- **§A.35.** Module `OIQMTarget`, kernel-only.

### PO-03 `NativeSource` and `toTheory`: the O3 obligations. Difficulty M–H. Unblocks 4.

- **Lean statement.** This is DESIGN §2.1 and §3, with R1 and R4 applied:

```lean
structure NativeSource (S) [Fintype S] [DecidableEq S] where
  Proc : ℕ → Type; Out : Proc n → Type; [fOut …] [dOut …]
  branch : (P : Proc n) → Out P → (Matrix (S × Fin n) (S × Fin n) ℂ →ₗ[ℂ] Matrix (S × Fin n) (S × Fin n) ℂ)
  sysProc : Type; sysOut : sysProc → Type; sysBranch : …
structure O3Fields (src : NativeSource S) where
  idP; coarse; bind; prep; prep_uniform; readoutP; readout_out; readout_local; discard; sysAvail
  swaps : ∀ n (k k₀ : Fin (n+1)), ∃ P : src.Proc (n+1), … branch P () =
    conjChannel (CoherentLift.permMatrix (ancSwap (n+1) k k₀))
noncomputable def NativeSource.toTheory (src) (O3 : O3Fields src) : FiniteOperationalTheory S

theorem toTheory_availExt_iff (src O3) n O F :
  (src.toTheory O3).availExt n O F ↔ ∃ (P : src.Proc n) (e : src.Out P ≃ O), F = src.branch P ∘ e.symm
theorem toTheory_pureSeed (src O3) n k₀ : (src.toTheory O3).prepAvail (n+1) (pureAttach (n+1) k₀)
  -- := pureSeedPrep_available_of_swap _ n k₀ (O3.swaps …)
```

  A **negative-control instance** is also stated: `substratumSource : NativeSource S`, built from
  `bijectiveOperator` and `phaseOperator`, with
  `toTheory_substratumSource_le : (substratumSource.toTheory _).availExt n O F → (substratumTheory S).availExt n O F`.
- **Kernel identifiers.**
  - `FiniteOperationalTheory` (OperationalAssembly.lean:594), `readout_is_localLuders` (:658),
    `pureSeedPrep_available_of_swap` (:675).
  - `MapSpectatorIndependent` (:151), `discardWith` (:515), `ancSwap` (:528).
  - `SystemToLevelOne` (LevelOneSeam.lean:117).
  - `bijectiveOperator` and `phaseOperator` (SubstratumInterface.lean:55, :58), `substratumTheory`
    (RouteB.lean:286), `genTheory` (ImplementationLocality.lean:852).
- **Mathlib dependencies.** `Equiv` and `Equiv.sigmaEquivProd` (Logic/Equiv/Defs.lean:722), for the
  dependent outcome type of `bind`; `Finset.sum_congr`; `LinearMap.comp`. No new Mathlib theory is needed.
- **Hardest step.** `availExt_bind`. The bound procedure's outcome type is a Σ-type over the first
  procedure's outcomes, and it must be identified with `O × O'` through the equivalence in
  `RealizedExt`.
- **R-READ.** `readoutP` is a field. Nothing about whether its branches lie in the configuration
  algebra is assumed. `readout_is_localLuders` fixes its channel *form* given spectator independence,
  which is itself the import (ii).
- **Label.** (I). The imports are:
  - Coh-1, as the codomain of `branch`;
  - (i) `prep_uniform`;
  - (ii) `readout_local`;
  - (iii) record retention, inside `bind`;
  - (iv) `discard`;
  - (vi) `swaps`;
  - `sysAvail`.
- **E/A/M.**
  - E: the kernel derives the readout form and pure seeds from these fields.
  - A: every field.
  - M: native procedures for each field. That is physical.
- **§A.35.** New module `OIQMInterface`, kernel-only. It imports DerivedQ3, MinimalRepertoire,
  SubstratumInterface and RouteB, and edits none of them. RouteB, SubstratumSource and FrozenSourcing
  docstrings are named in #1477's frozen, not yet executed plan and stay untouched.

### PO-04 The DIO-type predicate and the missing half of OPRES Lemma C. Difficulty M. Unblocks 3.

**The MIO-type half is already in the kernel; it is cited, not restated.** `PreservesDiag`
(DiagonalTheory.lean:68) is OPRES's MIO-type predicate. Its closure lemmas exist:
- `preservesDiag_comp` (:94), composition;
- `preservesDiag_sum` (:84);
- `preservesDiag_transport` (:106);
- `preservesDiag_amplRef` (:132) and `preservesDiag_withSpectator` (:151), for ⊗ id and spectators;
- `preservesDiag_localLuders` (:158);
- `preservesDiag_relabel` (:184);
- `preservesDiag_discardWith` (:229), for discard;
- `preservesDiag_conj_of_monomial` (SubstratumInterface.lean:101).

PO-04 covers only what is missing.

- **Lean statement.**

```lean
def diagPart (X : Matrix S S ℂ) : Matrix S S ℂ := Matrix.diagonal (Matrix.diag X)
/-- DIO-type (new). -/
def NoDetect (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) : Prop := ∀ X, diagPart (Φ X) = diagPart (Φ (diagPart X))
theorem noDetect_comp, noDetect_sum, noDetect_transport, noDetect_amplRef, noDetect_withSpectator,
  noDetect_discardWith, noDetect_relabel                  -- the DIO counterparts of the kernel's MIO lemmas
theorem noDetect_conj_of_monomial (h : IsMonomial K) : NoDetect (conjChannel K)
theorem noDetect_append (ω : Matrix H H ℂ) : NoDetect (appendState ω)         -- any ω
-- the two MIO-side cases not located in the kernel:
theorem preservesDiag_feedforward, noDetect_feedforward  -- Σ_r |r⟩⟨r| ⊗ K_r on configuration records
theorem preservesDiag_append_iff (ω) : PreservesDiag (appendState ω) ↔ ω = diagPart ω
```

- **Kernel identifiers.** The lemmas cited above, together with `IsMonomial` (SubstratumInterface.lean:50),
  `conjChannel`, `ptraceAnc`, `discardWith` and `permMatrix`.
- **Mathlib dependencies.** `Matrix.diagonal`, `Matrix.diag`, `Matrix.kroneckerMap`,
  `Matrix.posSemidef_diagonal_iff` (LinearAlgebra/Matrix/PosDef.lean:71), `Matrix.trace_kronecker`.
- **Hardest step.** `noDetect_discardWith` and the two feedforward lemmas, under the kernel's
  `A × Fin n` indexing.
- **Label.** (N), as pure algebra, matching OPRES's Lemma C label. It makes no claim about OI's
  operations: which operations are native is R-READ and PO-06's business.
- **E/A/M.**
  - E: Lemma C, layer X, reviewed in #1511. Its MIO half is in the kernel already (K).
  - A: none.
  - M: the DIO half and the two MIO-side cases, in Lean.
- **§A.35.** New module `CoherenceResource`, kernel-only. It imports DiagonalTheory and does not
  edit it, so the `current` family "completion classification and the primitive-source chain" is
  untouched.

### PO-05 Lemma TC (tomographic completeness). Difficulty S–M. Unblocks 5.

- **Lean statement.**

```lean
theorem tomographic_ext {n : Type} [Fintype n] [DecidableEq n]
    (L L' : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (h : ∀ ρ E : Matrix n n ℂ, ρ.PosSemidef → ρ.trace = 1 → E.PosSemidef → (1 - E).PosSemidef →
      (E * L ρ).trace = (E * L' ρ).trace) : L = L'
```

- **Kernel identifiers.** None.
- **Mathlib dependencies.**
  - `Matrix.ext_iff_trace_mul_left` (LinearAlgebra/Matrix/Trace.lean:274).
  - `Matrix.posSemidef_iff_eq_sum_vecMulVec` (Analysis/InnerProductSpace/Positive.lean:557) and
    `Matrix.IsHermitian` (LinearAlgebra/Matrix/Hermitian.lean:44), for the spanning of Hermitian
    matrices by effects.
  - `LinearMap.ext_on_range` (LinearAlgebra/Span/Basic.lean:845), over a spanning family.
- **Hardest step.** Effects span `Matrix n n ℂ` over ℂ. One route takes `single i j` combinations
  `(eᵢ ± eⱼ)(eᵢ ± eⱼ)ᴴ/2` and `(eᵢ ± i·eⱼ)(…)ᴴ/2`, each an effect, and reaches every `single i j`.
- **Label.** (N), pure mathematics. The P-ST record calls it "mathematical/definitional, no OI
  assumption".
- **E/A/M.**
  - E: layer X in #1510.
  - A: none.
  - M: the Lean text.
- **§A.35.** It could go in `OIQMTarget`. Kernel-only.

### PO-06 OPRES Theorem C, exact form: the two necessity conjuncts (statement). Difficulty M. Unblocks 1.

- **Lean statement.** This is Theorem C(d) on finite carriers. Its two conclusions are kept as
  separate theorems, following the restatement of O1 as two obligations:

```lean
/-- The closure of a set 𝒪 of operation families under Lemma C's rules (composition, ⊗ id,
partial trace, feedforward on configuration records, sub-instrument). -/
inductive GenBy (𝒪 : ∀ S [Fintype S] [DecidableEq S], Set (Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)) : … → Prop
theorem thmC_creator {V} [Fintype V] [DecidableEq V] (𝒪) {Φ} (hΦ : GenBy 𝒪 Φ)
    {W : Matrix V V ℂ} (hW : W ∈ Matrix.unitaryGroup V ℂ) (hnm : ¬ IsMonomial W)
    {p : ℝ} (hp : 0 < p) (hbr : Φ = (p : ℂ) • conjChannel W) :
    ∃ S _ _ (O ∈ 𝒪 S), ¬ PreservesDiag O                      -- non-MIO element
theorem thmC_detector … : ∃ S _ _ (O ∈ 𝒪 S), ¬ NoDetect O      -- non-DIO element
```

  The hypotheses are identical; the conclusions are separate. No theorem derives one conclusion from
  the other. The two elements may coincide, but proving one does not discharge the other.
- **Proof decomposition.**
  - **Detector.** By contraposition, PO-04 closure gives `NoDetect Φ`. Then the OPRES B(i) argument
    applies: `p·Wᴴ|i⟩⟨i|W` is diagonal and rank one, so it is a basis projector, so row i of W has a
    single entry, so W is monomial.
  - **Creator.** By contraposition, `PreservesDiag Φ`. Then `p·W|x⟩⟨x|Wᴴ` is diagonal and rank one,
    so column x has a single entry, so W is monomial.
  - The shared step is the lemma `unitary_monomial_of_rows` / `_of_cols`. A unitary whose rows, or
    whose columns, each have one nonzero entry is monomial. This step is new, and is the hardest
    part.
- **Kernel identifiers.**
  - `IsMonomial` (SubstratumInterface.lean:50), `permMatrix`, `PreservesDiag`, and PO-04.
  - Related, not duplicated: `ExecSource.exists_nonMonomial_of_layerFlowExecutable`, which yields one
    non-monomial admissible operator. Theorem C is sharper. Non-monomial is not identical to non-MIO
    plus non-DIO; for example, a non-monomial Kraus operator inside MIO exists by MIO ⊋ IO (Chitambar
    and Gour 2016).
  - `hadamard_not_monomial` (C5Discovery.lean:162), as the positive instance.
- **Mathlib dependencies.**
  - `Matrix.unitaryGroup` (LinearAlgebra/UnitaryGroup.lean:60) and `Matrix.mem_unitaryGroup_iff`
    (:72).
  - `Matrix.posSemidef_diagonal_iff`. For the rank-one step, `Matrix.rank_vecMulVec_le`
    (LinearAlgebra/Matrix/Rank.lean:199) gives the upper bound for `W|x⟩⟨x|Wᴴ`. The step "a diagonal
    rank-one PSD matrix is a multiple of one basis projector" is a direct entrywise argument, since
    Mathlib has no lemma for it. (`Matrix.rank_one`, Rank.lean:155, is the rank of the identity
    matrix and does not apply here.)
  - `Matrix.vecMulVec` (Data/Matrix/Mul.lean:616).
- **R-READ.** Native readouts enter `𝒪` as whatever operations they are. If R-READ holds they are
  MIO and DIO, and the theorem then says the creator and the detector are not readouts. If R-READ
  fails, a readout may be the detector. Both readings are covered, and neither is assumed.
- **Label.** (N), under the stated convention. The statement is pure mathematics about an abstract set
  `𝒪` of complex channels, and it has no native premise.
  - It is restricted to finite carriers, a narrower scope than OPRES's countable carriers, stated as
    such.
  - The approximate forms (a) and (b) are PO-19.
  - OPRES's label (I) on KIN belongs to the *reading* of `𝒪` as OI's native operations. In this record
    that reading is made in PO-07e, which is (I), where the native branches are typed as complex
    channels through `NativeSource.branch`.
- **E/A/M.**
  - E: Theorem C, layer X, in #1511, reviewed.
  - A: none in the statement. KIN enters at PO-07e.
  - M: which native operations, if any, are the non-MIO and non-DIO elements. That is physical.
- **§A.35.** Module `CoherenceResource`, kernel-only.

### PO-07 O1 plug points, controls and the O1 split. Difficulty S (A, B, C+), M (C−, e). Unblocks 0.

- **Lean statement.** This is DESIGN §2.2–2.3 with R2 applied:

```lean
structure CoherentSourceA (src) (O3) (σ : Equiv.Perm S) : Prop where
  closure : RouteB.DerivedOI (src.toTheory O3); invol : ∀ x, σ (σ x) = x
  moved : ∃ x, σ x ≠ x; flow : LiftAudit.LayerFlowExecutable (src.toTheory O3) σ
structure CoherentSourceB (src) (O3) : Prop where
  locality : ImplementationLocality (src.toTheory O3)
  observation : EmbeddedObservation (src.toTheory O3)
  rich : MinimalRepertoire.PhaseFreeRichness (src.toTheory O3)
theorem qm_of_coherentSourceA [Nonempty S] (h : ∃ σ, CoherentSourceA src O3 σ) : ExactAllFiniteEndomorphicQuantumOps (src.toTheory O3)
theorem qm_of_coherentSourceB [Nonempty S] (h : CoherentSourceB src O3) : ExactAllFiniteEndomorphicQuantumOps (src.toTheory O3)
theorem coherentSourceB_of_qm … : ∃ src O3, CoherentSourceB src O3                         -- C+ nonvacuity
theorem not_coherentSource_substratum : ¬ ∃ σ, CoherentSourceA substratumSource _ σ          -- C−
-- (e) the O1 split, two separate theorems, via PO-06 applied to the flow's non-monomial unitary:
theorem coherentSourceA_needs_creator (h : CoherentSourceA src O3 σ) (hx …) : ∃ n P a, ¬ PreservesDiag (src.branch P a)
theorem coherentSourceA_needs_detector (h : CoherentSourceA src O3 σ) (hx …) : ∃ n P a, ¬ NoDetect (src.branch P a)
```

- **Kernel identifiers.**
  - `qm_of_derivedOI_layerFlowExecutable` (DerivedQ3.lean:214), `qm_of_oiPlusMin`, `oiPlusMin_of_qm`
    (MinimalRepertoire.lean), `PhaseFreeRichness` (:423).
  - `LayerFlowExecutable` (LiftAudit.lean:112), `gateFlow` (:47), `levelPerm` (:51),
    `substratumTheory_not_layerFlowExecutable` (:200).
  - `DerivedOI` (RouteB.lean:148), `ReversibleImplementationLocality` (MicroscopicReversibility.lean:223).
- **Mathlib dependencies.** None beyond PO-03 and PO-06.
- **Hardest step (e).** Showing that `gateFlow (levelPerm σ n) t` is non-monomial for some t. At
  `t = 1/2` the flow mixes the moved pair. `exp_pi_I_half` (LiftAudit.lean) and the transition closed
  form are the kernel inputs. That the generated closure `GenBy` of the native branches contains the
  flow is `toTheory_availExt_iff`.
- **Label.** (I). The imports are those of PO-03, plus `PhasesAvailable` inside `DerivedOI` for plug
  point A, plus `ImplementationGenerated` for both A and B (AW-LEAN-1).
- **E/A/M.**
  - E: the kernel iffs and the reviewed interface design.
  - A: as listed.
  - M: a native procedure realizing the flow, with separate non-MIO and non-DIO elements. That is
    physical.
- **§A.35.** Module `OIQMInterface`, kernel-only.

### PO-08 Law bridge and record retention. Difficulty M. Unblocks 2.

- **Lean statement.**

```lean
structure LawBridge (src : NativeSource S) where
  nativeProb : Matrix (S × Fin n) (S × Fin n) ℂ → (P : src.Proc n) → src.Out P → ℝ
  trace_rule : ∀ ρ P a, ρ.PosSemidef → ρ.trace = 1 → nativeProb ρ P a = (Matrix.trace (src.branch P a ρ)).re
theorem branch_unique_of_lawBridge (B B' : LawBridge src) … -- via PO-05: two native channels with equal laws are equal
def RecordRetention (M : NativeModel A) : Prop :=      -- D-I.R1: R on a prefix is invariant under later steps
  ∀ π π' (hpre : IsPrefix π π') x, restrictHist hpre (M.R π' x) = M.R π (truncate x)
```

- **Kernel identifiers.** PO-03 and PO-05.
- **Mathlib dependencies.** `Matrix.trace`, `Complex.re`.
- **Label.** (I). The import is the trace law (Meas-1), carried in `trace_rule`. Its derivation is
  O6 and is not attempted.
- **E/A/M.**
  - E: none.
  - A: the trace law and record retention.
  - M: a native persistent record (MQ AW-MQ-2; M5 not passed). That is physical.
- **§A.35.** Module `OIQMInterface`.

### PO-09 Proposition P-ST (statement). Difficulty M, given PO-01, PO-02 and PO-05. Unblocks 1.

- **Lean statement.** Two theorems, items 1 and 2 of P-ST. Directions: ⇒ only, which is the witness
  direction of §A.34.

```lean
/-- FE-ADM: free evolution with setting s_Λ loaded is the label interpretation of "prepare ρ,
apply Λ_t", and {E, 1−E} is that of the readout. A hypothesis, not a derived fact. -/
def FE_ADM (M : NativeModel A) (s : Setting) (Λ : ℕ → Channel A) : Prop := …
def opChannelSpec (M) (s) (t) (L : Channel A) : Prop :=
  ∀ ρ E, IsDensity ρ → IsEffect E → opProb M s ρ t E = (Matrix.trace (E * L ρ)).re
theorem p_st_op (M) (hI : ∀ k p π h, M.law p π h = qLaw p.ρ π h) (hFE : FE_ADM M s Λ) :
    ∀ t, opChannelSpec M s t (Λ t) ∧ ∀ L, opChannelSpec M s t L → L = Λ t        -- I★_st-coh^op, via PO-05
theorem p_st_pop (…) : ∀ t i j, opProb M s (single i i 1) t (single j j 1) = ((Λ t) (single i i 1) j j).re
/-- BF: Born-form agreement (KIN applied to M*). A hypothesis. -/
theorem p_st_born (…) (hBF : ∀ t ρ E, (Matrix.trace (E * bornFamily M s t ρ)).re = opProb M s ρ t E) :
    ∀ t, bornFamily M s t = Λ t                                                     -- I★_st-coh
```

- **Kernel identifiers.**
  - `familyAt` (SemigroupTransfer.lean:93) is the uniform-prior Born family. `bornFamily` generalizes
    it to a fixed prior ω_H plus the controller configuration `c_{s_Λ}` (typing (b) of #1510).
  - PO-01, PO-02, PO-05.
- **Mathlib dependencies.** PO-05's dependencies, plus `Matrix.single`.
- **Hardest step.** Stating PROT inside `Prot`. The protocol `π(ρ, Λ_t, E)` uses a one-outcome
  instrument `{Λ_t}`, which requires `Λ_t` in Kraus normal form. The Kraus decomposition of
  `Tr_K[W^t(ρ ⊗ σ_K)W^{−t}]` is the kernel's `familyAt` Kraus form, generalized.
- **Label.** (I). The imports are:
  - FE-ADM, hypothesis `hFE`;
  - BF, hypothesis `hBF`, for item 2 only;
  - J-coh, the quantification over coherent ρ and arbitrary E in `opChannelSpec`; the population
    variant drops it;
  - the I★ witness property, hypothesis `hI`.
- **E/A/M.**
  - E: P-ST and Lemma TC, layer X on paper (#1510).
  - A: FE-ADM, BF and J-coh.
  - M: a physical source for FE-ADM, which is a form of O1, and for BF.
  
  FE-ADM does not exclude D-W (#1510 §3). The PO-16 witness is a nonvacuity control for `hFE`.
- **§A.35.** New module `SingleTime`, kernel-only. It imports SemigroupTransfer, whose family is
  kernel-only, and does not edit it.

### PO-10 `inclusion_of_source` (DESIGN §4.4). Difficulty H. Unblocks 1.

- **Lean statement.**

```lean
theorem inclusion_of_source [Nonempty A] (M : NativeModel A) (src : ∀ k, NativeSource (Car A k))
    (O3 : ∀ k, O3Fields (src k)) (hqm : ∀ k, ExactAllFiniteEndomorphicQuantumOps ((src k).toTheory (O3 k)))
    (hsem : RealizedSemantics M src) (hlaw : ∀ k, LawBridge (src k)) (hret : RecordRetention M) :
    ∀ k p π h, M.law p π h = qLaw p.ρ π h
```

- **Kernel identifiers.** `ExactCompositeQuantumOps` (AncillaClosure.lean:364): only its completeness
  half ⇐ is used. Also PO-02, PO-03 and PO-08.
- **Mathlib dependencies.** `MeasureTheory.Measure.map_apply`, and conditional measures on cylinder
  sets, via `Measure.restrict` and `measure_union` over the finitely many histories.
- **Hardest step.** `hsem`, the coherent use of the same procedure for the same label across the
  whole tree, combined with the step-by-step factorization of `M.law` into native conditionals.
- **Label.** (I). The imports are kinematics, `LawBridge`, `O3Fields` and `RecordRetention`.
- **E/A/M.**
  - E: none.
  - A: as listed.
  - M: every premise is physical.
- **§A.35.** Module `OIQMInterface`.

### PO-11 Lemma S1, finite hidden carrier (statement). Difficulty H. Unblocks 1.

- **Lean statement.** Finite H is a narrower scope than #1508's countable H, and is stated as such.

```lean
/-- The Born-form lift with a fixed hidden state ω, assumption (b): the family is DEFINED this way. -/
noncomputable def bornLift (φ : Equiv.Perm (V × H)) (ω : Matrix H H ℂ) (t : ℕ) (ρ : Matrix V V ℂ) :
    Matrix V V ℂ := ptraceH (permMatrix (φ ^ t) * Matrix.kroneckerMap (· * ·) ρ ω * (permMatrix (φ ^ t))ᴴ)
theorem s1_monomial [Fintype V] [DecidableEq V] [Fintype H] [DecidableEq H]
    (φ : Equiv.Perm (V × H)) (ω : Matrix H H ℂ) (hω : ω.PosSemidef) (hω1 : ω.trace = 1)  -- (c): one ω for all ρ
    {t : ℕ} (ht : 1 ≤ t) {W : Matrix V V ℂ} (hW : W ∈ Matrix.unitaryGroup V ℂ)
    (hU : ∀ ρ, bornLift φ ω t ρ = W * ρ * Wᴴ) :                                           -- (d): all ρ
    IsMonomial W                                                                             -- (a): fixed basis
theorem s1'_hadamard (φ) (ω) (hω hω1) : ¬ ∀ ρ, bornLift φ ω 1 ρ = hadamard * ρ * hadamardᴴ   -- S1′ via hadamard_not_monomial
```

- **Proof decomposition.**
  1. The spectral decomposition of ω:
     `Matrix.IsHermitian.spectral_theorem` (Analysis/Matrix/Spectrum.lean:141), or
     `Matrix.posSemidef_iff_eq_sum_vecMulVec` (Analysis/InnerProductSpace/Positive.lean:557).
  2. **Purity splitting.** This replaces Choi's extremality theorem. Mathlib has general extreme-point
     theory (`Set.extremePoints`, Analysis/Convex/Extreme.lean:68) and completely positive maps
     (`CompletelyPositiveMap`, Analysis/CStarAlgebra/CompletelyPositiveMap.lean:50, on C*-algebras,
     which covers `Matrix n n ℂ` under the scoped `Matrix.instCStarAlgebra`). It does not have the
     theorem that unitary channels are extreme, nor a Stinespring dilation theorem. Those two are the
     real gaps. The route here avoids both. A rank-one PSD matrix that is a sum
     of PSD matrices has each summand a nonnegative multiple of it. Apply this to the pure outputs
     `W|v⟩⟨v|Wᴴ` and `W|v+v′⟩⟨v+v′|Wᴴ`. This gives, for each eigenvector χ of ω, an equation
     `P(|v⟩ ⊗ |χ⟩) = W|v⟩ ⊗ |e⟩` with one e for all v. This is the hardest step.
  3. **Support disjointness.** Injectivity of `φ^t` makes the sets `supp(W|v⟩)` pairwise disjoint.
     Each is nonempty, and there are |V| of them, so each is a singleton:
     `Finset.card_le_card_of_injOn` (Data/Finset/Card.lean:427) and `Finset.card_biUnion`
     (Algebra/BigOperators/Group/Finset/Basic.lean:973).
  4. A unitary with single-entry columns is monomial. This is shared with PO-06.
- **Kernel identifiers.** `IsMonomial` (SubstratumInterface.lean:50), `permMatrix`, `hadamard` and
  `hadamard_not_monomial` (C5Discovery.lean:162), `familyAt` (SemigroupTransfer.lean:93), which is
  the uniform-ω special case.
- **Mathlib dependencies.** As in the proof decomposition, plus `Matrix.kroneckerMap` and
  `Matrix.unitaryGroup`.
- **Label.** (I). The imports, from #1508's table, are:
  - (b) the Born-form lift, as the *definition* `bornLift`, the corpus representation (KIN);
  - (c) preparation independence: ω is a fixed argument, not a function of ρ;
  - (d) a unitary target on every ρ, coherent ρ included: the quantifier `∀ ρ` in `hU`;
  - (a) the fixed configuration basis: the conclusion is in the configuration basis;
  - (e) finite H, here a hypothesis of scope.
- **E/A/M.**
  - E: S1 and S1′, layer X (#1508).
  - A: (b), (c), (d).
  - M: an operational counterpart for an embedded observer, not established (#1508). That is
    mathematics plus R-READ.
- **§A.35.** Module `SingleTime`, kernel-only.

### PO-12 Proposition S2, spectral form (statement). Difficulty H. Unblocks 0.

- **Lean statement.** This is S2 with a same-basis whole-space encoding U, so the hypotheses are
  "(b)–(e), not (a)". The conclusion is in a finite-order form, which implies the root-of-unity
  eigenvalue form.

```lean
theorem s2_finiteOrder (φ ω hω hω1) {U W : Matrix V V ℂ} (hU : U ∈ Matrix.unitaryGroup V ℂ)
    (hW : W ∈ Matrix.unitaryGroup V ℂ)
    (h : ∀ ρ, Uᴴ * bornLift φ ω 1 (U * ρ * Uᴴ) * U = W * ρ * Wᴴ) :
    ∃ d : ℂ, ‖d‖ = 1 ∧ ∃ N : ℕ, 0 < N ∧ (d⁻¹ • W) ^ N = 1
```

- **Proof decomposition.**
  1. Apply PO-11 to `UWUᴴ`, which gives a monomial `d_v|σ v⟩`.
  2. Amplitude multisets: `{χ_h} = d_v·{e_h′}`. The finite set of maximal-modulus amplitudes is
     invariant under each ratio `d_v/d_v′`, so each ratio has finite order:
     `isOfFinOrder_iff_pow_eq_one` (GroupTheory/OrderOfElement.lean:73).
  3. A power of `D′P_σ` is diagonal of roots of unity: `Equiv.Perm` order and `orderOf_dvd`.
- **Kernel identifiers.** PO-11.
- **Mathlib dependencies.** `IsOfFinOrder` (GroupTheory/OrderOfElement.lean:63),
  `isOfFinOrder_iff_pow_eq_one` (:73), `IsPrimitiveRoot` (RingTheory/RootsOfUnity/PrimitiveRoots.lean:63),
  `Matrix.unitaryGroup`.
- **Scope.** The encoding scope is the proved one only. Subspace and fixed-ancilla encodings
  (Conjecture S2-sub, open) are not obligations. CM-5 is the countercontrol for (d): `T = ⅓I + ⅔P₄`
  is not unitary.
- **Label.** (I), on (b)–(d), exactly as for PO-11.
- **E/A/M.**
  - E: S2, layer X (#1508).
  - A: (b), (c), (d).
  - M: S2-sub, which is mathematics.
- **§A.35.** Module `SingleTime`.

### PO-13 O2-a, the corner encoding lemma. Difficulty M. Unblocks 1.

- **Lean statement.**

```lean
/-- The level-k encoding: V on the system factor, identity on the ancilla factor of `Car _ k`. -/
def encLevel (V : Matrix B A ℂ) (k : ℕ) : Matrix (Car B k) (Car A k) ℂ :=
  Matrix.kroneckerMap (· * ·) V (1 : Matrix (Fin (k+1)) (Fin (k+1)) ℂ)
theorem encLevel_iso (hV : Vᴴ * V = 1) (k) : (encLevel V k)ᴴ * encLevel V k = 1
theorem encLevel_join (k m) :                 -- compatible with the fixed join reindexing of EP:33
  reindex (joinEquiv B k m) (joinEquiv A k m) (kroneckerMap (· * ·) (encLevel V k) 1) = encLevel V (joinLevel k m)
def encInstr (V : Matrix B A ℂ) (hV : Vᴴ * V = 1) {k m} (L : InstrLabel A k m) (c : Fin (L.r+1) → ℂ)
    (hc : ∑ i, ‖c i‖^2 = 1) : InstrLabel B k m
  -- K_i ↦ Vₖ K_i Vₖᴴ + c_i (1 − Vₖ Vₖᴴ), with Vₖ := encLevel V k; both sides live on Car B k
theorem encInstr_norm : ∑ i, ((encInstr V hV L c hc).K i)ᴴ * (encInstr V hV L c hc).K i = 1
  -- cross terms vanish: Vₖᴴ (1 − Vₖ Vₖᴴ) = 0 by encLevel_iso
def encProt (V hV) : Prot A k → Prot B k     -- encInstr at inst; σ unchanged at attach; levels preserved
theorem qLaw_enc (V hV) {k} (p : DensLabel (Car A k)) (π : Prot A k) (h : Hist π) :
    qLaw (encLevel V k * p.ρ * (encLevel V k)ᴴ) (encProt V hV π) (encHist h) = qLaw p.ρ π h
```

- **Kernel identifiers.** PO-01, `inclObs` (RegionTower.lean:123), and `Conf` (:86) for the region
  carriers.
- **Mathlib dependencies.** `Matrix.trace_mul_comm`, `Matrix.mul_assoc`, `Matrix.conjTranspose_mul`,
  `Matrix.PosSemidef.conjTranspose_mul_mul_same`, `Matrix.kroneckerMap` and `Matrix.mul_kronecker_mul` (:382)
  (LinearAlgebra/Matrix/Kronecker.lean), and `Matrix.reindex`.
- **Hardest step.** `encLevel_join`, the commutation of the encoding with the join reindexing at
  `attach` and `discard`. That is what fixes the level-k typing error of the previous statement.
- **Label.** (N), under the same convention as PO-01: pure mathematics about the comparator, with no
  premise. It has no native content: #1506 called it
  "the one part of D-O2 that is a statement of mathematics". It agrees with #1504's corner lemma at
  `31594967`.
- **E/A/M.**
  - E: the paper argument (#1504, #1506).
  - A: none.
  - M: the Lean text.
- **§A.35.** Module `CoherentTower`, kernel-only.

### PO-14 D-I.4b, finite Ω exclusion under isolation. Difficulty R. Unblocks 0.

- **Lean statement.**

```lean
/-- The imported mathematics of Main [55], as a hypothesis: no finite nonnegative factorization
of all qubit prepare-and-measure behaviours. -/
def QubitUnboundedNonnegRank : Prop := ∀ N : ℕ, ∃ (finite qubit prepare–measure family), ¬ FactorsThrough N …
theorem finite_Ω_excluded (h55 : QubitUnboundedNonnegRank) :
    ∀ (M : NativeModel A), (∀ k p π h, M.law p π h = qLaw p.ρ π h) → ¬ (Finite M.Ω ∧ Isolation M)
```

- **Kernel identifiers.** PO-02 (`Isolation`).
- **Mathlib.** Nonnegative rank is **absent** at `v4.33.0`, under `nonnegRank` or any synonym. It is
  therefore carried as the hypothesis `h55`. Proving it would be research-grade.
- **Label.** (I). The imports are [55] (`h55`) and isolation (`Isolation M`).
- **E/A/M.**
  - E: the factorization half (Main:568, P).
  - A: [55] and isolation.
  - M: [55] in Lean, which is mathematics.
- Relation: this is the finite-Ω counterpart of #1504's Proposition U, which is (I), at `31594967`.
- **§A.35.** Module `OIQMTarget`.

### PO-15 O2-b, stage compatibility (operational). Difficulty H. Unblocks 1.

- **Lean statement.**

```lean
theorem stage_compat (C : CoherentTower ι Q) {Λ Λ'} (h : Λ ⊆ Λ') :
    ∀ O F, (genTheory C.𝓘 C.qa.arch (Conf Λ Q)).availExt n O F →
      (genTheory C.𝓘 C.qa.arch (Conf Λ' Q)).availExt n O (fun o => liftStage h (F o))
```

- **Kernel identifiers.** `ContextStable` (ImplementationLocality.lean:359), `LabelInvariant` (:364),
  `genTheory` (:852), `stage_inclObs` (QuasilocalAlgebra.lean:700), `confRestrict`
  (RegionTower.lean:89).
- **Mathlib dependencies.** `Equiv.piEquivPiSubtypeProd` (Logic/Equiv/Prod.lean:468), for the
  reindexing `Conf Λ' Q ≃ Conf Λ Q × Conf (Λ' \ Λ) Q`. No kernel lemma for this reindexing was
  located.
- **Label.** (I), as D-O2: `QuantumArchitecture 𝓘` is a field.
- **E/A/M.**
  - E: none.
  - A: `qa`.
  - M: the reindexing lemma, which is mathematics.
- **§A.35.** Module `CoherentTower`.

### PO-16 D-W, the stepwise ψ-complete witness with split tapes (countercontrol). Difficulty H–R. Unblocks 0.

- **Lean statement.**

```lean
def psiCompleteModel (A) : NativeModel A   -- Ω := Tape × STape × Reg × Prog × Rec × Hist × Clock; Φ one Bennett step
theorem psiComplete_admissible : SchemaAdmissible (psiCompleteModel A)
theorem psiComplete_law : ∀ k p π h, (psiCompleteModel A).law p π h = qLaw p.ρ π h
theorem psiComplete_feAdm : FE_ADM (psiCompleteModel A) s Λ    -- control for PO-09's hFE
```

- **Proof decomposition.**
  1. The two-sided reversible embedding of an injective step on an infinite type.
  2. Measurability of the sampler.
  3. U-completeness and isolation, from loading that writes no outcome.
  4. `IndepFun` of U, the outcome tape, and S, the setting tape: the setting seeds come from `STape`,
     not from the U tape.
  5. Telescoping of conditional laws.
- **Mathlib dependencies.**
  - `MeasureTheory.Measure.infinitePi` (Probability/ProductMeasure.lean:358), its
    `IsProbabilityMeasure` instance (:381), `infinitePi_map_restrict` (:377).
  - The `MeasureSpace unitInterval` instance (MeasureTheory/Constructions/UnitInterval.lean:26).
  - `measurable_pi_lambda` (MeasurableSpace/Constructions.lean:597).
  - `ProbabilityTheory.IndepFun`.
  - `MeasureTheory.Measure.prod`, for the two tapes.
- **Label.** (I). The comparator's matrices are data in the simulator; that is the point of the
  countercontrol. The conclusion holds conditional on the simulator meeting `SchemaAdmissible` as
  finally written.
- **E/A/M.**
  - E: the design, CONFIRMED in #1506.
  - A: the comparator, as data.
  - M: the Lean text, and a candidate E with `¬ E psiCompleteModel` (D-W.C), which is physical.
- **Cardinality neutrality.** Needed: Ω is uncountable.
- **§A.35.** New module `PsiComplete`, kernel-only.

### PO-17 O2-c, S-∞ in operational form (statement only; blocked). Unblocks 1.

- **Lean statement.**

```lean
def SpectatorInert (M) : Prop := ∀ {Λ Λ'} (h : Λ ⊆ Λ') (π : Prot_stage Λ) (p p' : DensLabel (Conf Λ' Q)),
  RegionTower.restrict h p.ρ = RegionTower.restrict h p'.ρ → M.law p (inclProt h π) = M.law p' (inclProt h π)
```

  `RegionTower.restrict` is at RegionTower.lean:128.
- **Status.** A field of `CoherentTower`, not a theorem to prove now.
  - It is strictly stronger than Theorem 24(iii), which covers only the decoupled case (GR:138).
  - It relates to #1477's frozen, not yet executed plan (P* `55544cc3`, rows D362–D373).
  - It waits.
- **Label.** (I). S-∞ is the field `spectator`.
- **E/A/M.**
  - E: none.
  - A: S-∞.
  - M: S-∞, which is physical (coupled remainder).
- **§A.35.** Module `CoherentTower`.

### PO-18 O2-d, single-model assembly. Difficulty H. Unblocks 0.

- **Lean statement.**

```lean
theorem single_model_inclusion (C : CoherentTower ι Q) [Infinite ι] (hlaw : …) :
    ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (k p π h),
      C.model.law (encodeP C A p) (encodeProt C A π) (encodeHist h) = qLaw p.ρ π h
```

  The quantifier order, `∃ C` before `∀ A`, is the scalability requirement: one model and not one per
  size. `cone` is a field that is not bounded, consistent with #1504's Proposition U and AW-U2. A
  bounded cone is not imposed.
- **Kernel identifiers.** `genTheory_qm_of_quantumArchitecture` (SubstratumSource.lean:136), plus
  PO-10, PO-13, PO-15 and PO-17.
- **Label.** (I). The imports are `qa` (O1), `opSem`, `LawBridge` and S-∞.
- **E/A/M.**
  - E: the design (#1506).
  - A: as listed.
  - M: O1, O3 and S-∞, all physical.
- **Cardinality neutrality.** Needed.
- **§A.35.** Module `CoherentTower`.

### PO-19 Theorem C, approximate forms (a) and (b); Proposition D; Remark D′. Difficulty R. Unblocks 0.

- **Lean statement.**

```lean
theorem thmC_approx_creator … (hd : diamondDist Φ (conjChannel W) < 2 * kappaCol W) : ∃ O ∈ 𝒪, ¬ PreservesDiag O
theorem thmC_approx_detector … (hd : diamondDist Φ (conjChannel W) < 2 * kappaRow W) : ∃ O ∈ 𝒪, ¬ NoDetect O
```

  Proposition D and Remark D′ concern measurable carriers in the Heisenberg form. They are listed as
  statements to be typed later, in von Neumann algebra form.
- **Mathlib dependencies.**
  - **Present.**
    - The l2 operator norm on matrices: `Matrix.instCStarAlgebra` (Analysis/CStarAlgebra/Matrix.lean:294,
      scoped in `Matrix.Norms.L2Operator` at :297), `Matrix.l2_opNorm_def` (:185) and
      `l2_opNorm_conjTranspose_mul_self` (:199).
    - `Matrix.frobeniusNorm` and `Matrix.linftyOpNorm` (Analysis/Matrix/Normed.lean).
    - For Proposition D: `VonNeumannAlgebra` (Analysis/VonNeumannAlgebra/Basic.lean:67) and
      `WStarAlgebra` (:45).
  - The operator-norm variant is not part of PO-19. It is an unreviewed proposal, set apart in §4.
  - **Real gaps, carried as hypotheses only.** The trace norm and the diamond norm, which (a) and (b)
    as stated need, are absent at `v4.33.0`.
  - **Not located in this check.** Normal states and the von Neumann tensor product with its normal
    slice maps. Their presence is to be checked at implementation. Remark D′, for finite visible
    carriers, needs neither, and is typable with `CStarAlgebra` and finite-dimensional linear algebra.
- **Label.** (I). The imports are KIN, for (a) and (b). For D they are KIN, nonsingularity and
  normality.
- **E/A/M.**
  - E: layer X (#1511).
  - A: as listed.
  - M: Mathlib theory, which is mathematics.
- **§A.35.** Module `CoherenceResource`.

## 2. Summary for the three questions

- **Established.** Nothing in Lean by this record. The obligations restate results that are
  established at their own layers:
  - kernel iffs (K);
  - OPRES Lemma C and Theorems A′–C, S1, S2, Lemma TC and P-ST (X, paper, reviewed);
  - Proposition U (P, (I));
  - the #1506 designs, CONFIRMED.
- **Assumed.** Each obligation names its imports as hypotheses or fields:
  - KIN, as the channel types and `bornLift`;
  - preparation independence;
  - the unitary target on all ρ;
  - FE-ADM and BF;
  - J-coh;
  - the trace law;
  - the O3 fields and record retention;
  - `PhasesAvailable` and `ImplementationGenerated`;
  - `QuantumArchitecture`;
  - S-∞;
  - [55].
- **Missing.**
  - The earliest unsupported step is still the realization map from native procedures to complex
    channels (PO-03's `branch`), which is physical. It is followed by the native law bridge and
    records (PO-08), and then by O1's two separate elements, non-MIO and non-DIO (PO-06, PO-07e).
  - The mathematical gaps, carried as hypotheses only, are the trace and diamond norms, nonnegative
    rank, Stinespring dilation and channel extremality, all absent at `v4.33.0`.
  - Mathlib does supply the l2 operator norm, general extreme-point theory, CP maps on C*-algebras
    and von Neumann algebras. These are used in PO-11 and PO-19. The operator-norm proposal of §4 is
    unreviewed and is not counted here.
  - Other open mathematics: the reindexing lemma (PO-15) and S2-sub.
- **The (N) obligations are PO-01's lemmas, PO-04, PO-05, PO-06 and PO-13**, all pure mathematics
  under the stated convention. Every other obligation is (I).
- **Cardinality neutrality** is needed by PO-16 and PO-18. It is neutral or not needed for the rest.

## 3. Cross-references, not overlapped

- The BQP Lean ladder, `research/bqp-p2-20261121`.
- The Theorem 24 Lean sketch, `research/thm24-def-20261121`. It is relevant to PO-17's decoupled
  case only.
- READOUT-ALG, which carries R-READ.

None is used as a premise.

## 4. Unreviewed proposal, outside the obligation list

**UNREVIEWED PROPOSAL; not a reviewed obligation.** This item is a new claim: it is not part of
OPRES #1511, and no review has checked it. It has no PO number and enters no count, graph edge or
order above.

- **Proposal P-19a, the operator-norm form of Theorem A′'s bound.** For every diagonal σ,
  `‖ψψᴴ − σ‖ ≥ sup_{i≠j} |ψ_i ψ_j|` in the l2 operator norm (`Matrix.l2_opNorm_def`,
  Analysis/CStarAlgebra/Matrix.lean:185).
- **Proposed consequence.** The operator-norm counterparts of Theorem C (a) and (b), with constant κ in
  place of 2κ.
- **Status.** Conjectured by analogy with the trace-norm argument, and unproved. It needs independent
  review before it could become an obligation.
