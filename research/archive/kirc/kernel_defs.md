# Kernel definitions audit: ambient kinematics (K) and completion principles

Worktree: `scratchpad/wt-L42`, commit `fdebc6e39498367e15a8352fe0f01f8f75ab3671`.
All paths are relative to `verification/lean-mathlib/OIBridge/`. Lean text is quoted verbatim.
This was a read-only audit. Nothing was built. The results below come from reading the source,
not from running `lake build` or `#print axioms`.

***

## (A) Ambient kinematics K of the operational layer

### A.1 `structure FiniteOperationalTheory`, OperationalAssembly.lean:594–652

```lean
structure FiniteOperationalTheory (A : Type*) [Fintype A] [DecidableEq A] where
  /-- Available finite outcome families of operations on the SYSTEM. -/
  avail : ∀ (O : Type) [Fintype O] [DecidableEq O],
    (O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) → Prop
  /-- Available finite outcome families on the system extended by an `n`-level ANCILLA. -/
  availExt : ∀ (n : ℕ) (O : Type) [Fintype O] [DecidableEq O],
    (O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) → Prop
  /-- Doing nothing is available. -/
  avail_id : avail Unit (fun _ => LinearMap.id)
  /-- CLASSICAL COARSE-GRAINING of the outcome label, on the system. -/
  avail_coarse : ∀ (O O' : Type) [Fintype O] [DecidableEq O] [Fintype O'] [DecidableEq O']
      (F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) (f : O → O'), avail O F →
    avail O' (fun a => ∑ j ∈ Finset.univ.filter (fun j => f j = a), F j)
  /-- CLASSICAL COARSE-GRAINING on the extended carrier. -/
  availExt_coarse : ∀ (n : ℕ) (O O' : Type) [Fintype O] [DecidableEq O] [Fintype O']
      [DecidableEq O']
      (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
      (f : O → O'), availExt n O F →
    availExt n O' (fun a => ∑ j ∈ Finset.univ.filter (fun j => f j = a), F j)
  /-- GENERAL INSTRUMENT COMPOSITION (feed-forward) ... -/
  availExt_bind : ∀ (n : ℕ) (O O' : Type) [Fintype O] [DecidableEq O] [Fintype O']
      [DecidableEq O']
      (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
      (G : O → O' → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ]
        Matrix (A × Fin n) (A × Fin n) ℂ),
    availExt n O F → (∀ a, availExt n O' (G a)) →
      availExt n (O × O') (fun c => (G c.1 c.2).comp (F c.1))
  /-- Which cross-carrier PREPARATIONS are available. ... -/
  prepAvail : ∀ n : ℕ,
    (Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) → Prop
  /-- The only preparation ASSUMED: attaching a MAXIMALLY MIXED ancilla. ... -/
  prepAvail_uniform : ∀ n : ℕ, prepAvail (n + 1) (uniformAttach (n + 1))
  /-- An available composite deterministic operation may be POST-COMPOSED onto an
  available preparation. -/
  prepAvail_post : ∀ (n : ℕ)
      (P : Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
      (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    prepAvail n P → availExt n Unit (fun _ => Φ) → prepAvail n (Φ.comp P)
  /-- NATIVE FINITE BASIS READOUT of the ancilla: ... Its FORM is not
  postulated — see `readout_is_localLuders`. -/
  readout : ∀ n : ℕ, Fin n →
    Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ
  readout_avail : ∀ n : ℕ, availExt n (Fin n) (readout n)
  readout_local : ∀ (n : ℕ) (k : Fin n),
    MapSpectatorIndependent (ludersLift k) (readout n k)
  /-- ANCILLA DISCARD. ... -/
  prepAvail_discard : ∀ (n : ℕ)
      (P : Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
      (O : Type) [Fintype O] [DecidableEq O]
      (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    prepAvail n P → availExt n O F → avail O (fun a => discardWith n P (F a))
```

The docstrings are shortened above. The field types are exact.

Auxiliary definitions the fields use (verbatim):

- `tensorOf`, MonoidalCompletion.lean:193
  ```lean
  def tensorOf (XA : Matrix A A ℂ) (XB : Matrix B B ℂ) : Matrix (A × B) (A × B) ℂ :=
    Matrix.of fun p q => XA p.1 q.1 * XB p.2 q.2
  ```
- `uniformAttach`, OperationalAssembly.lean:492
  ```lean
  noncomputable def uniformAttach (n : ℕ) :
      Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ where
    toFun ρ := tensorOf ρ ((n : ℂ)⁻¹ • (1 : Matrix (Fin n) (Fin n) ℂ))
  ```
- `ptraceAnc`, OperationalAssembly.lean:453
  ```lean
  def ptraceAnc (n : ℕ) (M : Matrix (A × Fin n) (A × Fin n) ℂ) : Matrix A A ℂ :=
    Matrix.of fun s t => ∑ e : Fin n, M (s, e) (t, e)
  ```
- `discardWith`, OperationalAssembly.lean:515
  ```lean
  def discardWith (n : ℕ) (P : Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
      (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
      Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ :=
    (ptraceAncL n).comp (Φ.comp P)
  ```
- `ludersLift`, BranchSelector.lean:64: `toFun X := X k k • Matrix.single k k 1`
- `MapSpectatorIndependent`, OperationalAssembly.lean:151
  ```lean
  def MapSpectatorIndependent
      (ΦB : Matrix B B ℂ →ₗ[ℂ] Matrix B B ℂ)
      (ΦAB : Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ) : Prop :=
    ∀ (XA : Matrix A A ℂ) (XB : Matrix B B ℂ),
      ΦAB (tensorOf XA XB) = tensorOf XA (ΦB XB)
  ```
- `localLuders`, OperationalAssembly.lean:191:
  `toFun X := Matrix.of fun p q => if p.2 = k ∧ q.2 = k then X (p.1, k) (q.1, k) else 0`
- `readout_is_localLuders`, OperationalAssembly.lean:658:
  `T.readout n k = localLuders k`. The readout's form is derived from `readout_local`.
- `conjChannel`, MonoidalCompletion.lean:360: `toFun X := V * X * Vᴴ`
- `HasCompositeUnitaryControl`, OperationalAssembly.lean:665
  ```lean
  def HasCompositeUnitaryControl (T : FiniteOperationalTheory A) : Prop :=
    ∀ (n : ℕ) (U : Matrix (A × Fin n) (A × Fin n) ℂ), Uᴴ * U = 1 →
      T.availExt n Unit (fun _ => conjChannel U)
  ```

What each ingredient assumes:

| Ingredient | What the kernel fixes |
|---|---|
| Scalar field | Always `ℂ`. Every carrier is `Matrix _ _ ℂ` and every map is `→ₗ[ℂ]`. The structure has no field or scalar parameter. |
| Carrier | `Matrix A A ℂ` for a `Fintype`, `DecidableEq` index `A` (so `M_{|A|}(ℂ)`). Composites are `Matrix (A × Fin n) (A × Fin n) ℂ`. |
| Composition of systems | Index product `A × Fin n`, with the ancilla always a `Fin n`. Product states are `tensorOf`, the entrywise Kronecker product. Spectators are adjoined by `withSpectator` (reindexed `amplRef`, ReferenceExtension.lean:422). Levels are regrouped by `shiftIdx : (A × Fin n) × Fin m ≃ A × Fin (n * m)` (AncillaClosure.lean:142). This is the complex tensor product of matrix algebras. No other composition rule exists. |
| Operation / instrument | An outcome family `O → (Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)`: a ℂ-linear superoperator for each finite outcome. Availability is a `Prop` on the whole family. The structure puts no positivity, CP or trace condition on these maps. |
| States | There is no state type. States appear only implicitly, as the arguments `ρ : Matrix A A ℂ` of maps and preparations (`prepAvail`). PSD enters only through `CompositeOperationalValidity` (`PosSemidef`, under `open scoped ComplexOrder`, OperationalValidity.lean:75). The structure has no density-matrix predicate. |
| Normalization | Not in the structure. It enters through `CompositeOperationalValidity`'s `∑ a, ((F a) X).trace = X.trace` (aggregate trace preservation). |
| Readout | The only readout is `readout n k`, a map on `Matrix (A × Fin n) ...`, derived to be `localLuders k` (fixed-basis Lüders projection on the ancilla). There is no probability or Born functional. The outcome weight is the trace of the branch output, and it appears only implicitly through the validity trace clause. I found no `prob`, `born` or `density` definition in OperationalAssembly, OperationalValidity, CompositeSoundness, GeneralCarrier or PhysicalCharacterization. |
| Preparation | Only `uniformAttach` (maximally mixed ancilla) is assumed. The pure seed is derived (`pureSeedPrep_available_of_swap`, OperationalAssembly.lean:675ff) using ancilla-swap permutation matrices. |
| Quantum target (endpoint) | `IsFiniteEndomorphicKrausInstrument` (KrausSoundness.lean:112), `IsKrausFamily` (CompositeSoundness.lean:94), `IsCompletelyPositive := (choiMatrix Φ).PosSemidef` (CoherentExtension.lean:260), `IsCPTP` (CoherentExtension.lean:268). All of these are over `ℂ`. |

Endpoint predicates (verbatim):

```lean
-- KrausSoundness.lean:112
def IsFiniteEndomorphicKrausInstrument {m : ℕ}
    (F : Fin m → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) : Prop :=
  ∃ (n : ℕ) (K : Fin (n + 1) → Matrix A A ℂ) (out : Fin (n + 1) → Fin m),
    (∑ k, (K k)ᴴ * K k = 1) ∧ F = instrumentBranch K out
-- KrausSoundness.lean:134
def ExactFiniteEndomorphicQuantumOps (T : FiniteOperationalTheory A) : Prop :=
  ∀ (m : ℕ) (F : Fin m → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ),
    T.avail (Fin m) F ↔ IsFiniteEndomorphicKrausInstrument F
-- AncillaClosure.lean:364
def ExactCompositeQuantumOps (T : FiniteOperationalTheory A) : Prop :=
  ∀ (k m : ℕ) (F : Fin m → Matrix (A × Fin (k + 1)) (A × Fin (k + 1)) ℂ →ₗ[ℂ]
      Matrix (A × Fin (k + 1)) (A × Fin (k + 1)) ℂ),
    T.availExt (k + 1) (Fin m) F ↔ IsFiniteEndomorphicKrausInstrument F
-- LevelOneSeam.lean:186
def ExactAllFiniteEndomorphicQuantumOps (T : FiniteOperationalTheory A) : Prop :=
  ExactFiniteEndomorphicQuantumOps T ∧ ExactCompositeQuantumOps T
```

**Consequence for any reading of the characterization theorems.** The theory is a family of
availability predicates on subsets of complex matrix superoperators on complex tensor-product
carriers. So "OI⁺ ⟺ QM" is a selection within the ℂ-linear maps on `M_D(ℂ) ⊗ M_n(ℂ)`. It is not
a reconstruction of the complex field, the matrix carrier or the tensor product. K is fixed
ambiently: complex scalars, full complex matrix algebras, Kronecker composition, and ℂ-linear
operations.

### A.2 Is anything in the operational layer formulated abstractly?

No. Every definition in the operational and completion layer is written over `Matrix _ _ ℂ` and
`→ₗ[ℂ]`. That covers FiniteOperationalTheory, the completion principles, the census theories and
OIPlus in both versions. Grep results over `OIBridge/*.lean`:

| Pattern | Hits | Relevance to the operational layer |
|---|---|---|
| `IsROrC` | 0 | none |
| `RCLike` | 31 hits in 17 files | Almost all are rewrite lemmas `RCLike.star_def` or `RCLike.inner_apply` applied at `ℂ`. The only generic use is FactorUniqueness.lean:47, `variable {𝕜 E F H : Type*} [RCLike 𝕜]`, an infrastructure lemma for Kraus/Stinespring uniqueness (two factorizations with equal `X X*` differ by a unitary). It is generic over ℝ/ℂ but is consumed at ℂ. It is not part of the operational layer's kinematics. |
| `[Field` | 5 (Averaging:32, EdgeRigidity:618, HomometricSix:100, IdempotentTrace:50, Irreducibility:49) | None of these is operational: they cover counting averaging, K4 edge rigidity, homometric sets, trace of an idempotent, and representation irreducibility. |
| `Quaternion`, `ℍ` | 0 | none |
| `ConvexCone` | 0 | none |
| `Convex` (case-insensitive) | 27 hits in 6 files | Convex hulls of readout columns (CoherentLift), row-stochastic convexity (ContinuousExtension), the cycle-fibre hull, and a convex admissible state space in RegionTower:340. None is an abstract convex or GPT state space for the operational layer. |
| `GPT` | 0 | none |
| `Jordan` | 38 hits in 4 files | JordanClassification / OperationalRigidity: the Kadison order-isomorphism ⟹ Jordan ∗-isomorphism argument, then `matrixJordan_unitary_or_transpose` for Jordan maps **of `M_D(ℂ)`**. These are Jordan automorphisms of complex matrices, not Jordan-algebra (GPT or spin-factor) state spaces. |
| `Matrix … ℝ` | many | Stochastic and transition matrices of the classical or Markov layer (Equivalence, RootedClassification, ContinuousExtension, …), and `RealPairFlow.PairFlow.A : ℝ → Matrix (Fin 2) (Fin 2) ℝ`, which is immediately cast into `ℂ` by `transport`. |

The operational layer is concretely complex matrices throughout.

### A.3 The fixed-basis representation and the S ⇔ D ⇔ Q_fb equivalence

**Classes, Equivalence.lean**

```lean
-- :147
def Stochastic {K : ℕ} (P : Traj V K → ℝ) : Prop :=
  (∀ τ, 0 ≤ P τ) ∧ ∑ τ, P τ = 1
-- :157
structure RevReal (V : Type u) (K : ℕ) : Type (u + 1) where
  Hid : Type u
  fH : Fintype Hid
  dH : DecidableEq Hid
  step : (V × Hid) ≃ (V × Hid)
  init : V × Hid → ℝ
-- :182
def RevRealizable {K : ℕ} (P : Traj V K → ℝ) : Prop :=
  ∃ R : RevReal V K, R.IsLaw ∧ R.law = P
-- :190
structure QfbReal (V : Type u) (K : ℕ) : Type (u + 1) where
  Bas : Type u
  fB : Fintype Bas
  dB : DecidableEq Bas
  U : Matrix Bas Bas ℂ
  init : Bas → ℝ
  read : Bas → V
-- :201
def QfbReal.IsLaw {K : ℕ} (Q : QfbReal V K) : Prop :=
  Q.U ∈ Matrix.unitaryGroup Q.Bas ℂ ∧ (∀ b, 0 ≤ Q.init b) ∧ ∑ b, Q.init b = 1
-- :205
noncomputable def QfbReal.born {K : ℕ} (Q : QfbReal V K) (b b' : Q.Bas) : ℝ := ‖Q.U b' b‖ ^ 2
-- :209
noncomputable def QfbReal.chain {K : ℕ} (Q : QfbReal V K) (σ : Fin (K + 1) → Q.Bas) : ℝ :=
  Q.init (σ 0) * ∏ k : Fin K, Q.born (σ k.castSucc) (σ k.succ)
-- :216
def QfbRealizable {K : ℕ} (P : Traj V K → ℝ) : Prop :=
  ∃ Q : QfbReal V K, Q.IsLaw ∧ Q.law = P
```

**D is a permutation of a finite set.** Yes. `step : (V × Hid) ≃ (V × Hid)` is a bijection of the
finite type `V × Hid` (`Fintype Hid`). The initial law `init` is a general probability vector on
the product; it is not required to factor.

**Q_fb as defined.** `U : Matrix Bas Bas ℂ` is unitary (`Matrix.unitaryGroup Bas ℂ`). The readout
is a projective fixed-basis measurement at every step, with collapse: `chain` multiplies one-step
Born weights `‖U b' b‖²`. The law of a Q_fb datum therefore depends on `U` only through the
unistochastic matrix `|U_{b'b}|²`. Phases of `U` cannot affect any Q_fb law.

**`QfbData`, QuantumRepresentation.lean:60**, is the same datum without the horizon index:

```lean
structure QfbData (V : Type u) : Type (u + 1) where
  Bas : Type u
  fB : Fintype Bas
  dB : DecidableEq Bas
  U : Matrix Bas Bas ℂ
  init : Bas → ℝ
  read : Bas → V
```

It adds `IsLaw` (:71, same as above), `born` (:75), `chainW` (:79), `rootMass` and
`PositiveRootMass` (:88, :93), `rootTraj` (:109), and `QStar` (:165). `QStar` is
`∃ Q : QfbData V, Q.IsLaw ∧ Q.PositiveRootMass ∧ ∀ a t j, Γ t a j = Q.rooted t a j`.

**`Qfb_imp_S`, Equivalence.lean:245.** It uses only nonnegativity of `‖·‖²` and the unit-column
property of a unitary (`QfbReal.sum_born`, :227). It holds for every unitary, so it also holds for
any restricted class of unitaries (real orthogonal or permutation).

**`D_imp_Qfb`, Equivalence.lean:294. This is the realizing-unitary construction:**

```lean
theorem D_imp_Qfb {K : ℕ} (P : Traj V K → ℝ) (h : RevRealizable P) : QfbRealizable P := by
  classical
  obtain ⟨R, ⟨hn, ht⟩, rfl⟩ := h
  let Q : QfbReal V K :=
    { Bas := V × R.Hid, fB := inferInstance, dB := inferInstance,
      U := Equiv.Perm.permMatrix ℂ R.step.symm, init := R.init, read := Prod.fst }
  -- the Born weights of a permutation matrix are the indicator of the deterministic step:
  ...
  refine ⟨Q, ⟨EquivalenceChain.permMatrix_mem_unitaryGroup _, hn, ht⟩, ?_⟩
```

The unitarity certificate is EquivalenceChain.lean:178, `permMatrix_mem_unitaryGroup`:
`φ.permMatrix ℂ ∈ Matrix.unitaryGroup (V × H) ℂ`.

**`S_imp_D`, Equivalence.lean:419.** It builds a clock-and-record carrier
`Hid V K := Fin (K + 1) × Traj V K` (:362) with advance map `adv` (:369). It pads `adv` to a
global permutation with `exists_perm_extending` (:60). It uses no matrices and no scalars beyond ℝ.

**`finite_horizon_equivalence`, Equivalence.lean:459**

```lean
theorem finite_horizon_equivalence {K : ℕ} (P : Traj V K → ℝ) :
    (Stochastic P ↔ RevRealizable P) ∧
    (RevRealizable P ↔ QfbRealizable P) ∧
    (QfbRealizable P ↔ Stochastic P) :=
```

**Answer to the key question.** The realizing unitary in S ⇒ D ⇒ Q_fb is
`Equiv.Perm.permMatrix ℂ R.step.symm`, a 0/1 permutation matrix. It uses no complex phases, no
`Complex.I`, no exponential and no Hermitian generator. The file header, Equivalence.lean:28–34,
states that the manuscript's `U = e^{-iĤ}` remark is deliberately not formalized. So the complex
field does no work in this direction.

The equivalence would hold verbatim if `QfbReal.U` were restricted to real orthogonal matrices, or
to permutation matrices:
- S ⇒ Q_fb (through D) only ever produces permutation matrices.
- Q_fb ⇒ S holds for any unitary, and so for any subclass.

This is a reading of the proof, not a kernel theorem. No real or permutation variant of
`finite_horizon_equivalence` is formalized.

Related data points:
- **QuantumRepresentationT3.lean:74–80 (`permData`).** The C_OI ⊆ Q* inclusion also uses
  `U := Equiv.Perm.permMatrix ℂ (show Equiv.Perm (V × H) from R.step.symm)`, again a permutation
  matrix.
- **QuantumRepresentationT2.lean:69 (`hadU`).** The witness refuting Q* ⊆ C_OI is the Hadamard
  `!![hadAmp, hadAmp; hadAmp, -hadAmp]` with `hadAmp` a real `(√2)⁻¹` (conjugation is trivial, :74).
  It is a real orthogonal matrix. The file header says rational rotations would serve as well.
- **DilationChoice.lean:231–242.** Every 2×2 doubly stochastic matrix is the modulus-squared of a
  real orthogonal matrix (`isUnistochastic_two_of_symmetric`).

So in the whole Q_fb / Q* layer, every constructed unitary is a permutation matrix or real
orthogonal. Complex phases never enter.

***

## (B) Completion principles, verbatim

**`CompositeOperationalValidity`, OperationalValidity.lean:88**
```lean
def CompositeOperationalValidity (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n O F →
      (∀ a (X : Matrix (A × Fin n) (A × Fin n) ℂ), X.PosSemidef → ((F a) X).PosSemidef)
        ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace
```
Branchwise positivity plus aggregate trace preservation, at every ancilla level.

**`SystemToLevelOne`, LevelOneSeam.lean:117**
```lean
def SystemToLevelOne (T : FiniteOperationalTheory A) : Prop :=
  ∀ (O : Type) [Fintype O] [DecidableEq O] (F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ),
    T.avail O F → T.availExt 1 O (fun a => transport (levelOneIdx A).symm (F a))
```
`transport`, SpectatorBridge.lean:348, conjugates by `Matrix.reindexLinearEquiv`.

**`WellFormed`, GeneralCarrier.lean:125**
```lean
def WellFormed (T : FiniteOperationalTheory A) : Prop :=
  CompositeOperationalValidity T ∧ SystemToLevelOne T
```

**`InertSpectatorCompositionality`, SpectatorBridge.lean:223.** The file is SpectatorBridge, not
CompletedOI.
```lean
def InertSpectatorCompositionality (T : FiniteOperationalTheory A) : Prop :=
  ∀ (R : Type) [Fintype R] [DecidableEq R] (n m : ℕ) (e : R × (A × Fin n) ≃ A × Fin m)
    (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n O F →
      ∃ G : O → Matrix (A × Fin m) (A × Fin m) ℂ →ₗ[ℂ] Matrix (A × Fin m) (A × Fin m) ℂ,
        T.availExt m O G ∧ ∀ a, IsSpectatorExtension e (F a) (G a)
```
with SpectatorBridge.lean:180:
```lean
def IsSpectatorExtension {n m : ℕ} (e : R × (A × Fin n) ≃ A × Fin m)
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (G : Matrix (A × Fin m) (A × Fin m) ℂ →ₗ[ℂ] Matrix (A × Fin m) (A × Fin m) ℂ) : Prop :=
  ∀ (XR : Matrix R R ℂ) (X : Matrix (A × Fin n) (A × Fin n) ℂ),
    G (Matrix.reindex e e (tensorOf XR X)) = Matrix.reindex e e (tensorOf XR (Φ X))
```

**`ObservationalIndependence`** is defined twice:
- the qubit version, CompletedOI.lean:129,
  `def ObservationalIndependence : Prop := HasParallelReferenceExtension T` with
  `T : FiniteOperationalTheory (Fin 2)`;
- the carrier-general version, CarrierGeneralOIPlus.lean:73, with the same body for
  `T : FiniteOperationalTheory A`.

The body is `HasParallelReferenceExtension`, ReferenceExtension.lean:447:
```lean
def HasParallelReferenceExtension (T : FiniteOperationalTheory A) : Prop :=
  ∀ (R : Type) [Fintype R] [DecidableEq R] (n m : ℕ) (e : R × (A × Fin n) ≃ A × Fin m)
    (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n O F → T.availExt m O (fun a => withSpectator R e (F a))
```
`withSpectator R e Φ` (ReferenceExtension.lean:422) is the reindexed `amplRefL R Φ`, that is
`id_R ⊗ Φ`. Equivalence with inert spectators is `inertSpectator_iff_parallelReferenceExtension`
(SpectatorBridge.lean, below :223), restated as `observationalIndependence_iff_inert`
(CompletedOI.lean:131, CarrierGeneralOIPlus.lean:75).

**`HasCompositeUnitaryControl`, OperationalAssembly.lean:665.** Quoted in A.1. For every `n` and
every `U` with `Uᴴ * U = 1`, `conjChannel U` (`X ↦ U X Uᴴ`) is available at level `n`.

**`ReversibleRichness`** (qubit version CompletedOI.lean:171; the carrier-general version
CarrierGeneralOIPlus.lean:110 is identical with `Fin 2` replaced by `A`):
```lean
def ReversibleRichness : Prop :=
  (∀ (n : ℕ) (V : Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n Unit (fun _ => conjChannel V) → T.availExt n Unit (fun _ => conjChannel Vᴴ))
  ∧ ∀ n : ℕ, ∃ (G : Type) (H : Matrix (A × Fin n) (A × Fin n) ℂ)
      (U : G → Matrix (A × Fin n) (A × Fin n) ℂ),
      Hᴴ = H ∧ (∀ g, (U g)ᴴ * U g = 1) ∧ HControl H U
        ∧ (∀ t : ℝ, T.availExt n Unit (fun _ => conjChannel (flow H t)))
        ∧ (∀ g, T.availExt n Unit (fun _ => conjChannel (U g)))
```

- **"Every reversible transformation can be undone"** is the first conjunct. A "reversible
  transformation" is formally any available single-outcome conjugation channel
  `conjChannel V : X ↦ V X Vᴴ` for an arbitrary complex matrix `V`, with no unitarity hypothesis.
  "Undone" means `conjChannel Vᴴ` is available. Unitarity of `V` is derived only under
  `WellFormed`: in `reversibleRichness_of_control` (CompletedOI.lean:278;
  CarrierGeneralOIPlus.lean:148), trace preservation plus `sum_conjTranspose_mul_eq_one_of_trace`
  (DimensionalCountermodel.lean:456) gives `Vᴴ * V = 1`.
- **How su(D) enters.** It enters through the drift/control certificate `HControl H U`:
  - MonoidalCompletion.lean:344: `def IsSpecialSkew (A : Matrix S S ℂ) : Prop := Aᴴ = -A ∧ A.trace = 0`
  - MonoidalCompletion.lean:349:
    ```lean
    def HControl {G : Type*} (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) : Prop :=
      ∀ A : Matrix S S ℂ, IsSpecialSkew A → A ∈ controlLie H U
    ```
  - ControlLie.lean:83 and :89:
    ```lean
    def controlGenerators (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) :
        Set (Matrix S S ℂ) :=
      {A | ∃ g : G, A = (-Complex.I) • (U g * H * (U g)ᴴ)}
    noncomputable def controlLie (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) :
        LieSubalgebra ℝ (Matrix S S ℂ) :=
      LieSubalgebra.lieSpan ℝ (Matrix S S ℂ) (controlGenerators H U)
    ```
  - ReachabilitySeam.lean:95:
    `noncomputable def flow (H : Matrix S S ℂ) (t : ℝ) : Matrix S S ℂ := NormedSpace.exp ((-(t : ℂ) * Complex.I) • H)`

  So `su(D)` is the traceless skew-Hermitian complex matrices, and the control Lie algebra is the
  real Lie span of `-i U_g H U_g†`. `Complex.I` is built into both the generators and the passive
  flow `e^{-itH}`. `control_of_reversibleRichness` (CompletedOI.lean:200;
  CarrierGeneralOIPlus.lean:127) uses `universalReachability_of_lieRank_unconditional`
  (OrbitReachability.lean:631) to reach every unitary. The converse direction takes the rank-one
  drift `Matrix.single i₀ i₀ 1` with all unitaries as controls (`hControl_single_all`,
  CompletedOI.lean:257, whose proof uses `Complex.I • A` and the Hermitian spectral decomposition).

**`IteratedAncillaClosure`, AncillaClosure.lean:247**
```lean
def IteratedAncillaClosure (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n m : ℕ) (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix ((A × Fin n) × Fin (m + 1)) ((A × Fin n) × Fin (m + 1)) ℂ →ₗ[ℂ]
      Matrix ((A × Fin n) × Fin (m + 1)) ((A × Fin n) × Fin (m + 1)) ℂ),
    T.availExt (n * (m + 1)) O (fun a => transport (shiftIdx A n (m + 1)) (F a)) →
      T.availExt n O
        (fun a => discardWith (A := A × Fin n) (m + 1) (uniformAttach (m + 1)) (F a))
```

**`IsShiftedTheory`, CompletedOI.lean:315**
```lean
def IsShiftedTheory (T : FiniteOperationalTheory A) (n : ℕ)
    (T' : FiniteOperationalTheory (A × Fin n)) : Prop :=
  (∀ (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    T'.avail O F ↔ T.availExt n O F)
  ∧ ∀ (m : ℕ) (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix ((A × Fin n) × Fin m) ((A × Fin n) × Fin m) ℂ →ₗ[ℂ]
      Matrix ((A × Fin n) × Fin m) ((A × Fin n) × Fin m) ℂ),
    T'.availExt m O F ↔ T.availExt (n * m) O (fun a => transport (shiftIdx A n m) (F a))
```

**`ObserverRecursion`, CompletedOI.lean:327**
```lean
def ObserverRecursion (T : FiniteOperationalTheory A) : Prop :=
  ∀ n : ℕ, ∃ T' : FiniteOperationalTheory (A × Fin n), IsShiftedTheory T n T'
```
This is carrier-general already; CarrierGeneralOIPlus reuses it.

**`PhysicalCompletionConditions`, PhysicalCharacterization.lean:295**
```lean
def PhysicalCompletionConditions (T : FiniteOperationalTheory A) : Prop :=
  CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
    ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T
```
`SubstantiveCompletion`, GeneralCarrier.lean:130:
`InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T`.

**`OIPlus`, qubit version, CompletedOI.lean:418**
```lean
def OIPlus : Prop :=
  OICore T ∧ WellFormed T ∧ ObservationalIndependence T ∧ ReversibleRichness T
    ∧ ObserverRecursion T
```
with `def OICore (T : FiniteOperationalTheory (Fin 2)) : Prop := RealizesSealedOICore T`
(CompletedOI.lean:96).

**`OIPlus`, carrier-general version, CarrierGeneralOIPlus.lean:185**
```lean
def OIPlus : Prop :=
  WellFormed T ∧ ObservationalIndependence T ∧ ReversibleRichness T ∧ ObserverRecursion T
```
It has no OI-core conjunct. `oiPlus_qubit_iff` (:224) identifies the two versions on `Fin 2`.

**`RealizesSealedOICore`, OIRealization.lean:234**
```lean
def RealizesSealedOICore (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  CoreC1C4
    ∧ T.availExt 4 Unit (fun _ => transport coreIdx (correlationExtension sigmaPerm (onesCorr Core)))
    ∧ T.availExt 4 Unit (fun _ => transport coreIdx (correlationExtension tauPerm (onesCorr Core)))
    ∧ (∀ r : Bool × Bool, transport coreIdx (readVisible r) = T.readout 4 (visIdx r))
    ∧ T.availExt 4 (Bool × Bool) (fun r => transport coreIdx (readVisible r))
    ∧ ∀ (steps : List VStep) (w : Core → ℂ),
        realizedFold steps (Matrix.reindex coreIdx coreIdx (Matrix.diagonal w))
          = Matrix.reindex coreIdx coreIdx (Matrix.diagonal (visWeightFold steps w))
```
The supporting definitions are in IndependenceCensus.lean:
- `Core := VH × Bool` (:94), an 8-state classical core;
- `sigmaPerm` (swap v,h) at :113 and `tauPerm` (flip b) at :116, which are permutations;
- `CoreC1C4` at :187, decidable combinatorial predicates on the core.

`correlationExtension g (onesCorr Core)` is a permutation conjugation (CoherentExtension.lean:278;
`correlationExtension_ones_eq_conjChannel`), and `readVisible` (OIRealization.lean:115) is a
block-Lüders projector. The whole OI core is classical and permutation-based.

### Statements

- **`exactAll_iff_physical_general`**, GeneralCarrier.lean:100, under the section variables
  `{A : Type} [Fintype A] [DecidableEq A] [Nonempty A]` (:74):
  ```lean
  theorem exactAll_iff_physical_general (T : FiniteOperationalTheory A) :
      ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T :=
    ⟨physical_of_exactAll T, exactAll_of_physical_general T⟩
  ```
- **`oiPlus_iff_qm`, carrier-general**, CarrierGeneralOIPlus.lean:207, with `[Nonempty A]` (:188):
  ```lean
  theorem oiPlus_iff_qm : OIPlus T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
    ⟨qm_of_oiPlus T, oiPlus_of_qm T⟩
  ```
  and `carrier_general_oiPlus` (:213) quantifies it over every `(A : Type) [Fintype A] [DecidableEq A] [Nonempty A]`.
  The qubit version is CompletedOI.lean:440, with the same statement for `T : FiniteOperationalTheory (Fin 2)`.
- **`oi_alone_not_qm`**, GeneralCarrier.lean:160:
  ```lean
  theorem oi_alone_not_qm :
      ∃ T : FiniteOperationalTheory (Fin 2),
        RealizesSealedOICore T ∧ ¬ ExactAllFiniteEndomorphicQuantumOps T :=
    ⟨diagTheory, diag_realizesSealedOICore, diag_not_exactAll⟩
  ```
- **`substantive_census`**, SubstantiveCensus.lean:986:
  ```lean
  theorem substantive_census (gI gC gK : Bool) :
      ∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ RealizesSealedOICore T
        ∧ (InertSpectatorCompositionality T ↔ gI = true)
        ∧ (HasCompositeUnitaryControl T ↔ gC = true)
        ∧ (IteratedAncillaClosure T ↔ gK = true)
  ```
- **`krausSoundExt_of_validity_inert`**, OperationalValidity.lean:124:
  ```lean
  theorem krausSoundExt_of_validity_inert [Nonempty A] (T : FiniteOperationalTheory A)
      (hval : CompositeOperationalValidity T) (hin : InertSpectatorCompositionality T) :
      KrausSoundExt T
  ```
  `KrausSoundExt` (CompositeSoundness.lean:123) says every available family at every level `n+1`
  satisfies `IsKrausFamily`. The proof (`cp_of_valid_inert`, :105) adjoins a copy of the composite
  as reference and evaluates at the maximally entangled dyad to get a PSD Choi matrix. This is the
  complex Choi–Kraus route.
- **`realizesSealedOICore_of_control`**, OIRealization.lean:252:
  ```lean
  theorem realizesSealedOICore_of_control (T : FiniteOperationalTheory (Fin 2))
      (hctrl : HasCompositeUnitaryControl T) : RealizesSealedOICore T
  ```
  Only permutation unitaries are used (`relabel_available`, :245, via
  `permMatrix_isometry g`). Consequently `completedOI_iff_physical` (CompletedOI.lean:110) shows
  that the OI-core conjunct is redundant given control.

### The eight census cells, SubstantiveCensus.lean:927–984

All are qubit (`Fin 2`), well-formed, and realize the sealed OI core. The witnesses come from
`classTheory` (:301), whose composite availability is
`(∀ a, C.P N (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace` and whose system availability is
`IsKrausFamily F ∧ ∀ a, C.Q (F a)`. Otherwise they are the named theories below.

| Cell (failing principles) | Lemma | Theory | Composite maps |
|---|---|---|---|
| ∅ (QM) | `cell_none` :927 | `fullQuantum` (ReferenceSufficiency.lean:681), via `main_result.2.1` | `IsCPInstrument`: CP branches, aggregate trace preserved |
| {inert} | `cell_I` :935 | `countermodel` (DimensionalCountermodel.lean:621) | `IsTwoPositiveInstrument`: 2-positive branches, aggregate trace. Exactly Kraus on the system. |
| {control} | `cell_C` :943 | `diagTheory` (DiagonalTheory.lean:246) | `IsCPInstrument F ∧ ∀ a, PreservesDiag (F a)`: CP and computational-basis diagonal-preserving |
| {closure} | `cell_K` :950 | `gapTheory` (RankGapTheory.lean:273) | `IsGapInstrument`: Kraus sums of rank-gap-admissible operators (`Gap N`), aggregate trace |
| {inert, control} | `cell_IC` :957 | `diagTwoPosTheory = classTheory icData` (:585) | `icP`: `IsTwoPositive Φ ∧ PreservesDiag Φ` |
| {inert, closure} | `cell_IK` :964 | `cappedTheory = classTheory ikData` (:587) | `ikP`: `IsTwoPositive Φ ∧ (N ≤ 3 → IsCompletelyPositive Φ)` (2-positive, CP capped at levels ≤ 3) |
| {control, closure} | `cell_CK` :971 | `diagGapTheory = classTheory ckData` (:583) | `ckP`: `IsCompletelyPositive Φ ∧ PreservesDiag Φ ∧ (N ≤ 3 → Gap N Φ)` |
| {inert, control, closure} | `cell_ICK` :978 | `cappedDiagTheory = classTheory ickData` (:589) | `ickP`: `IsTwoPositive Φ ∧ PreservesDiag Φ ∧ (N ≤ 3 → IsCompletelyPositive Φ)` |

`IsTwoPositive` (DimensionalObstruction.lean:374) means `id₂ ⊗ Φ` is positive with a qubit
reference. `PreservesDiag` (DiagonalTheory.lean:68) means diagonal matrices map to diagonal
matrices. Every cell is a sub-class of ℂ-linear maps on `M_2(ℂ) ⊗ M_N(ℂ)`. None is a
non-matrix GPT, a real or quaternionic theory, or an abstract classical simplex theory. The
diagonal-preserving cells are the closest to "classical", and they are still complex-matrix
theories.

***

## (C) Comparisons to real or quaternionic QM, or to non-matrix GPTs

**None found.** No kernel file defines, or compares against, any of the following:
- real-Hilbert-space QM or quaternionic QM (0 hits for `Quaternion` or `ℍ`, and no real-QM operational theory);
- boxworld, PR boxes, Tsirelson or CHSH (0 hits);
- spin factors or Jordan-algebra state spaces (the `Jordan` hits are Jordan automorphisms of `M_D(ℂ)`);
- the classical simplex as an operational theory;
- any GPT abstraction (0 hits for `GPT`, `ConvexCone`, or "generalized probabilistic").

`FiniteOperationalTheory` cannot express these theories at all, because its carrier is
hard-coded to `Matrix _ _ ℂ`.

Three nearby items are not such comparisons. They are recorded so they are not mistaken for one.

1. **MinimalRepertoire.lean**, header :1–37 and :250, `colourAlg`. The "bipartite obstruction"
   shows that bichromatic drives plus colour-compatible permutations lie in a Lie algebra that the
   colour phase `diag(i, 1)` conjugates into real antisymmetric matrices. That algebra cannot reach
   population differences (`popDiff_notMem_controlLie` :337, `not_hControl_two` :362). This is a
   statement about control Lie algebras inside complex `M_D(ℂ)`, not a comparison with real QM.
   `PhaseFreeRichness` (:423) still uses `flow (transition a b) t = exp(-it(E_ab+E_ba))`, which is
   a genuinely complex unitary. `ElementaryTransitionRichness` (LieRankSource.lean:436) includes
   `phaseGate a := diagonal (if a = p then Complex.I else 1)` (LieRankSource.lean:209).
2. **RealPairFlow.lean**, `PairFlow` at :41, with `A : ℝ → Matrix (Fin 2) (Fin 2) ℝ`, orthogonal.
   A real orthogonal one-parameter pair flow is cast into ℂ by `transport` (:51). QM is recovered
   only together with complex phase gates (`qm_of_pairFlowSourced` :429, hypothesis `hph` on
   `phaseGate`). The complex phase is an explicit extra input there. The kernel does not compare
   real and complex theories.
3. **InstrumentDilation.lean:434**, `local_tomography_physical`. Local tomography is proved for
   complex matrices by "complex polarization twice". That is the property that singles out complex
   over real QM in reconstruction programmes, but the kernel proves it only as a fact about
   `Matrix (A × B) (A × B) ℂ`. It does not use it to exclude a real alternative.

***

## Bottom line

- **The operational layer K.** It is fixed ambient kinematics: `ℂ` scalars, full matrix algebras
  `M_{|A|·n}(ℂ)`, Kronecker/`tensorOf` composition with `Fin n` ancillas, and ℂ-linear
  superoperators as operations. The only readout is fixed-basis Lüders, and there is no explicit
  Born functional. PSD and trace enter only through `CompositeOperationalValidity`.
- **What the characterization theorems select.** `exactAll_iff_physical_general`,
  `oiPlus_iff_qm` and `substantive_census` select among subsets of these complex maps. They do not
  derive ℂ, the matrix carrier or the tensor product.
- **The S ⇔ D ⇔ Q_fb equivalence** never uses complex phases:
  - D is a bijection of a finite set;
  - D ⇒ Q_fb realizes it by a 0/1 permutation matrix;
  - Q_fb laws depend only on `|U_{b'b}|²`.

  The same proof would go through with `U` restricted to real orthogonal or permutation matrices.
  This is an observation about the proof, not a formalized theorem.
- **Where `Complex.I` enters** the completion layer:
  - the control Lie generators `-i U H U†` and the flow `e^{-itH}` in `ReversibleRichness`;
  - `HasCompositeUnitaryControl` over complex unitaries;
  - the phase gates of the elementary and pair-flow repertoires;
  - the complex Choi/Kraus endpoint.
