/-
  OIBridge/SpectatorBridge.lean — the bridge between `H_comp` (the act/corr world of round
  twenty-four) and the availability world of `FiniteOperationalTheory`: what spectator
  compositionality DETERMINES and what it does not SUPPLY.

  ROUND THIRTY-SEVEN. Round thirty-six proved that system Kraus soundness, full composite
  unitary control and parallel reference extension force composite Kraus soundness (the
  antecedent is weakened to `KrausSound` in this round's opening cleanup, in
  `ReferenceSufficiency.lean`). The question left open was whether parallel reference
  extension is itself an OI-style consequence — in particular whether `H_comp`, the
  compositional hypothesis already in the file, delivers it. This file answers it in two
  halves, each proved, and names the condition that is missing.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  FORM (proved).  `hComp_spectator_form`: under `H_comp`, the coherent map of  │
      │    every spectator-extended relabelling `id_R × g` IS `id_R ⊗ (coherent map   │
      │    of g)` — `correlationExtension (spectatorExt g) (C _) = amplRefL R (…)`.   │
      │    `isSpectatorExtension_iff`: a map acting as `id_R ⊗ Φ` on every reindexed  │
      │    product input IS `withSpectator R e Φ` (locality fixes the form uniquely). │
      │  EXISTENCE (not supplied).  `hcompRealized_not_implies_parallelReferenceExtension`: │
      │    a theory in which `H_comp` holds AND every coherent map it names is         │
      │    available, with full composite unitary control, need not have               │
      │    `HasParallelReferenceExtension` — the round-34 countermodel is one.          │
      │  THE MISSING CONDITION.  `InertSpectatorCompositionality`, in physical words:   │
      │    an intervention performable on a system remains performable when an          │
      │    independent finite spectator is adjoined, and acts identically on that       │
      │    spectator.  `inertSpectator_iff_parallelReferenceExtension`: it is exactly   │
      │    parallel reference extension.                                                │
      └──────────────────────────────────────────────────────────────────────────────┘

  WHY THE SPLIT IS THE RIGHT ONE. `H_comp` is a statement about the coherent maps assigned
  to RELABELLINGS: functoriality on implementations, and `id_A × g ↦ id_A ⊗ (map of g)` on
  product inputs. Its spectator clause therefore constrains the FORM of a spectator
  extension wherever the completion assigns one (`spectatorIndependent_iff_mapLevel`, round
  twenty-four, plus this file's `mapSpectatorIndependent_iff_amplRef`: agreement on product
  inputs is agreement everywhere, since composite matrix units are products). It never
  asserts that an available NON-reversible intervention — a general `availExt` family —
  has any spectator extension available at all. That is a separate existence principle,
  and the round-34 countermodel shows it is independent: there the relabellings are all
  available (it has every composite unitary), `H_comp` holds for the trivial-correlation
  completion, and the spectator extension of the available branch `Φ₂` is not available.

  THE REALIZATION PREDICATE. `HCompRealized T e act corr CB C` says: `H_comp` holds for the
  completion, AND each coherent map the completion names — each letter on the composite
  `R × (Fin 2 × Fin n)`, transported along the explicit reindexing `e` into the theory's
  carrier `Fin 2 × Fin m`; each `B`-side map at level `n`; each spectator-extended map at
  level `m` — is an available one-outcome intervention. Transport is the reindexing
  conjugation `transport e Φ = reindex e e ∘ Φ ∘ reindex e.symm e.symm`, and
  `withSpectator R e Φ = transport e (amplRefL R Φ)` definitionally. In a realized `H_comp`
  the spectator-extended coherent map of every relabelling is available AND has the
  `withSpectator` form (`hCompRealized_spectator_available`): parallel reference extension
  holds ON THE REVERSIBLE SECTOR named by the completion. The non-implication is that it
  need not hold on the rest.

  WHAT IS AND IS NOT CLAIMED. Proved: the form theorems; the trivial-correlation completion
  satisfies `H_comp` for every alphabet (`hComp_ones`) and is realized by any theory with
  composite unitary control (`hCompRealized_ones_of_control`), in particular by the
  countermodel and by the full quantum theory; the countermodel refutes parallel reference
  extension, so `H_comp` realized does not give it; inert-spectator compositionality is
  equivalent to parallel reference extension, so with system soundness, control and
  boundary item 2 it gives composite soundness (`krausSoundExt_of_sound_control_inert`),
  the countermodel lacks it, the full theory has it. NOT claimed: that OI or `H_comp`
  implies inert-spectator compositionality — the non-implication says the opposite for the
  realized form. NOT claimed: composite COMPLETENESS (that every Kraus family on every
  composite is available): `prepAvail` starts from the visible system only, and a
  product-preparation principle is a separate question, round thirty-eight's (ANSWERED IN
  ROUND THIRTY-EIGHT, `AncillaClosure.lean` / `ClosureObstruction.lean`: the missing rule is
  iterated ancilla closure — fresh-ancilla attach and discard relative to a composite base —
  it is independent of everything above, and with it composite completeness follows). NOT claimed:
  OI + conditions ⟺ full operational QM. No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.ReferenceSufficiency

namespace OIBridge
namespace SpectatorBridge

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalCountermodel ReferenceExtension ReferenceSufficiency BoundaryAudit

/-! ### Section A — spectator independence is reference amplification -/

section Form

variable {R S : Type*} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]

/-- The reference block of a product matrix is a scalar multiple of the system factor. -/
theorem refBlockR_tensorOf (XR : Matrix R R ℂ) (X : Matrix S S ℂ) (i j : R) :
    refBlockR (tensorOf XR X) i j = XR i j • X := by
  ext k l
  rw [Matrix.smul_apply, smul_eq_mul]
  rfl

/-- **REFERENCE AMPLIFICATION ON PRODUCTS** is `id_R ⊗ Φ`. -/
theorem amplRef_tensorOf (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (XR : Matrix R R ℂ)
    (X : Matrix S S ℂ) :
    amplRef R Φ (tensorOf XR X) = tensorOf XR (Φ X) := by
  ext ⟨i, k⟩ ⟨j, l⟩
  show Φ (refBlockR (tensorOf XR X) i j) k l = XR i j * Φ X k l
  rw [refBlockR_tensorOf, map_smul, Matrix.smul_apply, smul_eq_mul]

/-- **MAP-LEVEL SPECTATOR INDEPENDENCE IS REFERENCE AMPLIFICATION.** A composite map that
acts as `id_R ⊗ Φ` on every product input is `amplRefL R Φ` — composite matrix units are
products, so agreement on products is agreement everywhere. -/
theorem mapSpectatorIndependent_iff_amplRef (ΦB : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (ΦRS : Matrix (R × S) (R × S) ℂ →ₗ[ℂ] Matrix (R × S) (R × S) ℂ) :
    MapSpectatorIndependent ΦB ΦRS ↔ ΦRS = amplRefL R ΦB := by
  constructor
  · intro h
    refine eq_of_agree_on_single ΦRS (amplRefL R ΦB) fun p q => ?_
    obtain ⟨r, s⟩ := p
    obtain ⟨r', s'⟩ := q
    rw [← tensorOf_single r r' s s', h, amplRefL_apply, amplRef_tensorOf]
  · rintro rfl XR X
    exact amplRef_tensorOf ΦB XR X

/-- **THE SPECTATOR CLAUSE FIXES THE FORM.** Under spectator independence, the coherent
map assigned to `id_R × g` is exactly `id_R ⊗ (coherent map of g)`. -/
theorem spectatorIndependent_form (CB : Equiv.Perm S → Matrix S S ℂ)
    (C : Equiv.Perm (R × S) → Matrix (R × S) (R × S) ℂ) (h : SpectatorIndependent CB C)
    (g : Equiv.Perm S) :
    correlationExtension (spectatorExt g) (C (spectatorExt g))
      = amplRefL R (correlationExtension g (CB g)) :=
  (mapSpectatorIndependent_iff_amplRef _ _).mp
    (((spectatorIndependent_iff_mapLevel CB C).mp h) g)

/-- **`H_comp` SUPPLIES THE FORM OF EVERY SPECTATOR EXTENSION IT NAMES** — the reversible
specialization of parallel reference extension, with `id_R ⊗ Φ` read off explicitly. -/
theorem hComp_spectator_form {ι : Type*} (act : ι → Equiv.Perm (R × S))
    (corr : ι → Matrix (R × S) (R × S) ℂ) (CB : Equiv.Perm S → Matrix S S ℂ)
    (C : Equiv.Perm (R × S) → Matrix (R × S) (R × S) ℂ) (h : HComp act corr CB C)
    (g : Equiv.Perm S) :
    correlationExtension (spectatorExt g) (C (spectatorExt g))
      = amplRefL R (correlationExtension g (CB g)) :=
  spectatorIndependent_form CB C h.2 g

end Form

/-! ### Section B — locality (form) versus existence, in the availability world -/

section Locality

variable {A : Type*} [Fintype A] [DecidableEq A] {R : Type*} [Fintype R] [DecidableEq R]

/-- Two endomorphisms of the extended carrier agreeing on every reindexed matrix unit are
equal. -/
theorem ext_of_agree_on_reindexed_single {n m : ℕ} (e : R × (A × Fin n) ≃ A × Fin m)
    (G G' : Matrix (A × Fin m) (A × Fin m) ℂ →ₗ[ℂ] Matrix (A × Fin m) (A × Fin m) ℂ)
    (h : ∀ p q : R × (A × Fin n),
      G (Matrix.reindex e e (Matrix.single p q 1)) = G' (Matrix.reindex e e (Matrix.single p q 1))) :
    G = G' := by
  have hL : ∀ Y : Matrix (R × (A × Fin n)) (R × (A × Fin n)) ℂ,
      G (Matrix.reindex e e Y) = G' (Matrix.reindex e e Y) := by
    intro Y
    have h1 : G (Matrix.reindex e e Y)
        = (G ∘ₗ (Matrix.reindexLinearEquiv ℂ ℂ e e).toLinearMap) Y := rfl
    have h2 : G' (Matrix.reindex e e Y)
        = (G' ∘ₗ (Matrix.reindexLinearEquiv ℂ ℂ e e).toLinearMap) Y := rfl
    rw [h1, h2]
    conv_lhs => rw [Matrix.matrix_eq_sum_single Y]
    conv_rhs => rw [Matrix.matrix_eq_sum_single Y]
    rw [map_sum, map_sum]
    refine Finset.sum_congr rfl fun p _ => ?_
    rw [map_sum, map_sum]
    refine Finset.sum_congr rfl fun q _ => ?_
    rw [single_eq_smul, map_smul, map_smul]
    congr 1
    exact h p q
  refine LinearMap.ext fun N => ?_
  have := hL (Matrix.reindex e.symm e.symm N)
  rwa [← Matrix.reindex_symm, Equiv.apply_symm_apply] at this

/-- **A SPECTATOR EXTENSION, BY ITS ACTION.** `G` on the extended carrier is a spectator
extension of `Φ` along `e` when, on every reindexed product input `X_R ⊗ X`, it acts as
`X_R ⊗ Φ X`: it does what `Φ` does and leaves the spectator untouched. This is the
LOCALITY of an extension — its form — stated without presupposing existence. -/
def IsSpectatorExtension {n m : ℕ} (e : R × (A × Fin n) ≃ A × Fin m)
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (G : Matrix (A × Fin m) (A × Fin m) ℂ →ₗ[ℂ] Matrix (A × Fin m) (A × Fin m) ℂ) : Prop :=
  ∀ (XR : Matrix R R ℂ) (X : Matrix (A × Fin n) (A × Fin n) ℂ),
    G (Matrix.reindex e e (tensorOf XR X)) = Matrix.reindex e e (tensorOf XR (Φ X))

/-- **LOCALITY FIXES THE FORM UNIQUELY.** A spectator extension of `Φ` along `e` is
`withSpectator R e Φ`, and nothing else. -/
theorem isSpectatorExtension_iff {n m : ℕ} (e : R × (A × Fin n) ≃ A × Fin m)
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (G : Matrix (A × Fin m) (A × Fin m) ℂ →ₗ[ℂ] Matrix (A × Fin m) (A × Fin m) ℂ) :
    IsSpectatorExtension e Φ G ↔ G = withSpectator R e Φ := by
  constructor
  · intro h
    refine ext_of_agree_on_reindexed_single e G _ fun p q => ?_
    obtain ⟨r, x⟩ := p
    obtain ⟨r', x'⟩ := q
    rw [← tensorOf_single r r' x x', h, withSpectator_reindex, amplRef_tensorOf]
  · rintro rfl XR X
    rw [withSpectator_reindex, amplRef_tensorOf]

/-- Two spectator extensions of the same map along the same reindexing coincide. -/
theorem spectatorExtension_unique {n m : ℕ} (e : R × (A × Fin n) ≃ A × Fin m)
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    {G G' : Matrix (A × Fin m) (A × Fin m) ℂ →ₗ[ℂ] Matrix (A × Fin m) (A × Fin m) ℂ}
    (hG : IsSpectatorExtension e Φ G) (hG' : IsSpectatorExtension e Φ G') : G = G' := by
  rw [(isSpectatorExtension_iff e Φ G).mp hG, (isSpectatorExtension_iff e Φ G').mp hG']

end Locality

/-! ### Section C — inert-spectator compositionality -/

section Inert

variable {A : Type*} [Fintype A] [DecidableEq A]

/-- **INERT-SPECTATOR COMPOSITIONALITY**, in physical words: an intervention performable on
a system remains performable when an independent finite spectator is adjoined, and acts
identically on that spectator. Formally: every available family at level `n` has, for
every finite spectator `R` and every relabelling `e` of the joint carrier into the
theory's carrier at level `m`, an AVAILABLE family at level `m` whose branches are
spectator extensions (in the sense of `IsSpectatorExtension`) of the original branches.
The definition asserts EXISTENCE of an available extension; its FORM is then forced. -/
def InertSpectatorCompositionality (T : FiniteOperationalTheory A) : Prop :=
  ∀ (R : Type) [Fintype R] [DecidableEq R] (n m : ℕ) (e : R × (A × Fin n) ≃ A × Fin m)
    (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n O F →
      ∃ G : O → Matrix (A × Fin m) (A × Fin m) ℂ →ₗ[ℂ] Matrix (A × Fin m) (A × Fin m) ℂ,
        T.availExt m O G ∧ ∀ a, IsSpectatorExtension e (F a) (G a)

/-- **INERT-SPECTATOR COMPOSITIONALITY IS PARALLEL REFERENCE EXTENSION.** The existence
clause, once the form is forced, is exactly round thirty-five's property. -/
theorem inertSpectator_iff_parallelReferenceExtension (T : FiniteOperationalTheory A) :
    InertSpectatorCompositionality T ↔ HasParallelReferenceExtension T := by
  constructor
  · intro h R _ _ n m e O _ _ F hF
    obtain ⟨G, hG, hspec⟩ := h R n m e O F hF
    have hform : G = fun a => withSpectator R e (F a) :=
      funext fun a => (isSpectatorExtension_iff e (F a) (G a)).mp (hspec a)
    rwa [hform] at hG
  · intro h R _ _ n m e O _ _ F hF
    exact ⟨fun a => withSpectator R e (F a), h R n m e O F hF,
      fun a => (isSpectatorExtension_iff e (F a) _).mpr rfl⟩

end Inert

/-- **COMPOSITE SOUNDNESS FROM INERT-SPECTATOR COMPOSITIONALITY**, with system soundness,
full composite unitary control and boundary item 2. -/
theorem krausSoundExt_of_sound_control_inert (T : FiniteOperationalTheory (Fin 2))
    (hext : FiniteIsometryExtensionSF Unit) (hsound : KrausSound T)
    (hctrl : HasCompositeUnitaryControl T) (hin : InertSpectatorCompositionality T) :
    KrausSoundExt T :=
  krausSoundExt_of_sound_control_refext T hext hsound hctrl
    ((inertSpectator_iff_parallelReferenceExtension T).mp hin)

/-- The round-34 countermodel lacks inert-spectator compositionality. -/
theorem countermodel_not_inert : ¬ InertSpectatorCompositionality countermodel :=
  fun h => countermodel_not_parallelReferenceExtension
    ((inertSpectator_iff_parallelReferenceExtension _).mp h)

/-- The full quantum theory has it. -/
theorem fullQuantum_inert : InertSpectatorCompositionality fullQuantum :=
  (inertSpectator_iff_parallelReferenceExtension _).mpr fullQuantum_parallelReferenceExtension

/-! ### Section D — the trivial-correlation completion satisfies `H_comp` -/

section Ones

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- The trivial (all-ones) correlation. -/
def onesCorr (S : Type*) : Matrix S S ℂ := Matrix.of fun _ _ => 1

/-- Correlation extension with the trivial correlation is relabelling by `g`. -/
theorem correlationExtension_ones (g : Equiv.Perm S) (X : Matrix S S ℂ) :
    correlationExtension g (onesCorr S) X = Matrix.of fun a b => X (g.symm a) (g.symm b) := by
  ext a b
  show onesCorr S (g.symm a) (g.symm b) * X (g.symm a) (g.symm b) = X (g.symm a) (g.symm b)
  rw [show onesCorr S (g.symm a) (g.symm b) = 1 from rfl, one_mul]

/-- Relabelling by `g` is conjugation by the permutation unitary. -/
theorem correlationExtension_ones_eq_conjChannel (g : Equiv.Perm S) :
    correlationExtension g (onesCorr S) = conjChannel (permMatrix g) := by
  refine LinearMap.ext fun X => ?_
  ext a b
  rw [correlationExtension_ones]
  show X (g.symm a) (g.symm b) = (permMatrix g * X * (permMatrix g)ᴴ) a b
  rw [permMatrix_conj_apply]

/-- Relabellings compose as the permutations do. -/
theorem correlationExtension_ones_comp (g h : Equiv.Perm S) :
    (correlationExtension g (onesCorr S)).comp (correlationExtension h (onesCorr S))
      = correlationExtension (g * h) (onesCorr S) := by
  refine LinearMap.ext fun X => ?_
  ext a b
  rw [LinearMap.comp_apply, correlationExtension_ones, correlationExtension_ones,
    correlationExtension_ones]
  rfl

/-- The word map of the trivial-correlation completion is relabelling by the word's
permutation. -/
theorem wordMap_ones {ι : Type*} (act : ι → Equiv.Perm S) (w : List ι) :
    wordMap act (fun _ => onesCorr S) w = correlationExtension (wordPerm act w) (onesCorr S) := by
  induction w with
  | nil =>
    refine LinearMap.ext fun X => ?_
    ext a b
    rw [wordMap_nil, wordPerm_nil, correlationExtension_ones]
    rfl
  | cons i w ih =>
    show (correlationExtension (act i) (onesCorr S)).comp (wordMap act (fun _ => onesCorr S) w)
      = correlationExtension (act i * wordPerm act w) (onesCorr S)
    rw [ih, correlationExtension_ones_comp]

/-- The trivial-correlation completion is implementation-extensional for every alphabet. -/
theorem implementationExtensionality_ones {ι : Type*} (act : ι → Equiv.Perm S) :
    ImplementationExtensionality act (fun _ => onesCorr S) := by
  intro u v huv
  rw [wordMap_ones, wordMap_ones, huv]

end Ones

section OnesComposite

variable {A B : Type*} [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B]

/-- The trivial-correlation completion is spectator independent. -/
theorem spectatorIndependent_ones :
    SpectatorIndependent (fun _ : Equiv.Perm B => onesCorr B)
      (fun _ : Equiv.Perm (A × B) => onesCorr (A × B)) :=
  (spectatorIndependent_iff _ _).mpr fun _ _ _ => rfl

/-- **`H_comp` HOLDS FOR THE TRIVIAL-CORRELATION COMPLETION**, for every alphabet. -/
theorem hComp_ones {ι : Type*} (act : ι → Equiv.Perm (A × B)) :
    HComp act (fun _ => onesCorr (A × B)) (fun _ : Equiv.Perm B => onesCorr B)
      (fun _ : Equiv.Perm (A × B) => onesCorr (A × B)) :=
  ⟨implementationExtensionality_ones act, spectatorIndependent_ones⟩

end OnesComposite

/-! ### Section E — transport along a reindexing -/

section Transport

variable {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l] [DecidableEq l']

/-- Transport of an endomorphism along a reindexing of the carrier. -/
def transport (e : l ≃ l') (Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ) :
    Matrix l' l' ℂ →ₗ[ℂ] Matrix l' l' ℂ :=
  (Matrix.reindexLinearEquiv ℂ ℂ e e).toLinearMap ∘ₗ Φ
    ∘ₗ (Matrix.reindexLinearEquiv ℂ ℂ e.symm e.symm).toLinearMap

theorem transport_apply (e : l ≃ l') (Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ) (N : Matrix l' l' ℂ) :
    transport e Φ N = Matrix.reindex e e (Φ (Matrix.reindex e.symm e.symm N)) := rfl

/-- Transport of a conjugation is conjugation by the reindexed matrix. -/
theorem transport_conjChannel (e : l ≃ l') (V : Matrix l l ℂ) :
    transport e (conjChannel V) = conjChannel (Matrix.reindex e e V) := by
  refine LinearMap.ext fun N => ?_
  rw [transport_apply]
  show Matrix.reindex e e (V * Matrix.reindex e.symm e.symm N * Vᴴ)
    = Matrix.reindex e e V * N * (Matrix.reindex e e V)ᴴ
  rw [reindex_mul, reindex_mul, Matrix.conjTranspose_reindex, ← Matrix.reindex_symm,
    Equiv.apply_symm_apply]

/-- Reindexing preserves the isometry equation. -/
theorem reindex_isometry (e : l ≃ l') (V : Matrix l l ℂ) (hV : Vᴴ * V = 1) :
    (Matrix.reindex e e V)ᴴ * Matrix.reindex e e V = 1 := by
  rw [Matrix.conjTranspose_reindex, ← reindex_mul, hV, Matrix.reindex_apply,
    Matrix.submatrix_one_equiv]

/-- The permutation lift satisfies the isometry equation in the other order too. -/
theorem permMatrix_isometry (g : Equiv.Perm l) : (permMatrix g)ᴴ * permMatrix g = 1 := by
  rw [permMatrix_conjTranspose]
  have h := permMatrix_unitary g.symm
  rwa [permMatrix_conjTranspose, Equiv.symm_symm] at h

end Transport

/-- `withSpectator` is transport of reference amplification. -/
theorem withSpectator_eq_transport {A : Type*} [Fintype A] [DecidableEq A] (R : Type*)
    [Fintype R] [DecidableEq R] {n m : ℕ} (e : R × (A × Fin n) ≃ A × Fin m)
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    withSpectator R e Φ = transport e (amplRefL R Φ) := rfl

/-! ### Section F — `H_comp` realized in a theory, and the non-implication -/

section Realized

variable {R : Type*} [Fintype R] [DecidableEq R] {ι : Type*} {n m : ℕ}

/-- **`H_comp` REALIZED IN A THEORY.** The completion satisfies `H_comp`, and every coherent
map it names is an available one-outcome intervention: each letter on the composite
`R × (Fin 2 × Fin n)`, transported along `e` into the carrier at level `m`; each `B`-side
map at level `n`; each spectator-extended map at level `m`. -/
def HCompRealized (T : FiniteOperationalTheory (Fin 2)) (e : R × (Fin 2 × Fin n) ≃ Fin 2 × Fin m)
    (act : ι → Equiv.Perm (R × (Fin 2 × Fin n)))
    (corr : ι → Matrix (R × (Fin 2 × Fin n)) (R × (Fin 2 × Fin n)) ℂ)
    (CB : Equiv.Perm (Fin 2 × Fin n) → Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ)
    (C : Equiv.Perm (R × (Fin 2 × Fin n)) → Matrix (R × (Fin 2 × Fin n)) (R × (Fin 2 × Fin n)) ℂ) :
    Prop :=
  HComp act corr CB C
    ∧ (∀ i, T.availExt m Unit (fun _ => transport e (correlationExtension (act i) (corr i))))
    ∧ (∀ g, T.availExt n Unit (fun _ => correlationExtension g (CB g)))
    ∧ (∀ g, T.availExt m Unit
        (fun _ => transport e (correlationExtension (spectatorExt g) (C (spectatorExt g)))))

/-- **PARALLEL REFERENCE EXTENSION ON THE REVERSIBLE SECTOR.** In a realized `H_comp`, the
spectator extension of every relabelling's coherent map is available, and it is exactly
`withSpectator R e` of that map. -/
theorem hCompRealized_spectator_available (T : FiniteOperationalTheory (Fin 2))
    (e : R × (Fin 2 × Fin n) ≃ Fin 2 × Fin m) (act : ι → Equiv.Perm (R × (Fin 2 × Fin n)))
    (corr : ι → Matrix (R × (Fin 2 × Fin n)) (R × (Fin 2 × Fin n)) ℂ)
    (CB : Equiv.Perm (Fin 2 × Fin n) → Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ)
    (C : Equiv.Perm (R × (Fin 2 × Fin n)) → Matrix (R × (Fin 2 × Fin n)) (R × (Fin 2 × Fin n)) ℂ)
    (h : HCompRealized T e act corr CB C) (g : Equiv.Perm (Fin 2 × Fin n)) :
    T.availExt m Unit (fun _ => withSpectator R e (correlationExtension g (CB g))) := by
  have hav := h.2.2.2 g
  rw [hComp_spectator_form act corr CB C h.1 g] at hav
  exact hav

/-- **CONTROL REALIZES THE TRIVIAL-CORRELATION COMPLETION**, for every spectator, reindexing
and alphabet: every relabelling is a permutation conjugation, hence a composite unitary. -/
theorem hCompRealized_ones_of_control (T : FiniteOperationalTheory (Fin 2))
    (hctrl : HasCompositeUnitaryControl T) (e : R × (Fin 2 × Fin n) ≃ Fin 2 × Fin m)
    (act : ι → Equiv.Perm (R × (Fin 2 × Fin n))) :
    HCompRealized T e act (fun _ => onesCorr _) (fun _ => onesCorr _) (fun _ => onesCorr _) := by
  refine ⟨hComp_ones act, fun i => ?_, fun g => ?_, fun g => ?_⟩
  · rw [correlationExtension_ones_eq_conjChannel, transport_conjChannel]
    exact hctrl m _ (reindex_isometry e _ (permMatrix_isometry _))
  · rw [correlationExtension_ones_eq_conjChannel]
    exact hctrl n _ (permMatrix_isometry _)
  · rw [correlationExtension_ones_eq_conjChannel, transport_conjChannel]
    exact hctrl m _ (reindex_isometry e _ (permMatrix_isometry _))

end Realized

/-- The countermodel realizes the trivial-correlation completion for every spectator,
reindexing and alphabet. -/
theorem countermodel_hCompRealized_ones {R : Type*} [Fintype R] [DecidableEq R] {ι : Type*}
    {n m : ℕ} (e : R × (Fin 2 × Fin n) ≃ Fin 2 × Fin m)
    (act : ι → Equiv.Perm (R × (Fin 2 × Fin n))) :
    HCompRealized countermodel e act (fun _ => onesCorr _) (fun _ => onesCorr _)
      (fun _ => onesCorr _) :=
  hCompRealized_ones_of_control countermodel countermodel_control e act

/-- So does the full quantum theory. -/
theorem fullQuantum_hCompRealized_ones {R : Type*} [Fintype R] [DecidableEq R] {ι : Type*}
    {n m : ℕ} (e : R × (Fin 2 × Fin n) ≃ Fin 2 × Fin m)
    (act : ι → Equiv.Perm (R × (Fin 2 × Fin n))) :
    HCompRealized fullQuantum e act (fun _ => onesCorr _) (fun _ => onesCorr _)
      (fun _ => onesCorr _) :=
  hCompRealized_ones_of_control fullQuantum fullQuantum_control e act

/-- **`H_comp` REALIZED DOES NOT GIVE PARALLEL REFERENCE EXTENSION.** At the qutrit
spectator and the explicit reindexing of round thirty-five, with the full alphabet of
composite relabellings: `H_comp` holds, every coherent map it names is available, full
composite unitary control holds — and the theory refutes parallel reference extension,
hence inert-spectator compositionality. -/
theorem hcompRealized_not_implies_parallelReferenceExtension :
    ∃ T : FiniteOperationalTheory (Fin 2),
      HCompRealized T qutritIdx (id : Equiv.Perm (Fin 3 × (Fin 2 × Fin 2)) → _)
          (fun _ => onesCorr _) (fun _ => onesCorr _) (fun _ => onesCorr _)
        ∧ HasCompositeUnitaryControl T
        ∧ ¬ HasParallelReferenceExtension T ∧ ¬ InertSpectatorCompositionality T :=
  ⟨countermodel, countermodel_hCompRealized_ones qutritIdx id, countermodel_control,
    countermodel_not_parallelReferenceExtension, countermodel_not_inert⟩

/-- **THE SAME REALIZATION IS CONSISTENT WITH THE EXTENSION.** The full theory realizes the
same completion and has parallel reference extension: the realization decides neither way,
which is what "existence is an independent condition" means. -/
theorem hcompRealized_consistent_with_parallelReferenceExtension :
    ∃ T : FiniteOperationalTheory (Fin 2),
      HCompRealized T qutritIdx (id : Equiv.Perm (Fin 3 × (Fin 2 × Fin 2)) → _)
          (fun _ => onesCorr _) (fun _ => onesCorr _) (fun _ => onesCorr _)
        ∧ HasParallelReferenceExtension T ∧ InertSpectatorCompositionality T :=
  ⟨fullQuantum, fullQuantum_hCompRealized_ones qutritIdx id,
    fullQuantum_parallelReferenceExtension, fullQuantum_inert⟩

#print axioms refBlockR_tensorOf
#print axioms amplRef_tensorOf
#print axioms mapSpectatorIndependent_iff_amplRef
#print axioms spectatorIndependent_form
#print axioms hComp_spectator_form
#print axioms ext_of_agree_on_reindexed_single
#print axioms isSpectatorExtension_iff
#print axioms spectatorExtension_unique
#print axioms inertSpectator_iff_parallelReferenceExtension
#print axioms krausSoundExt_of_sound_control_inert
#print axioms countermodel_not_inert
#print axioms fullQuantum_inert
#print axioms correlationExtension_ones
#print axioms correlationExtension_ones_eq_conjChannel
#print axioms correlationExtension_ones_comp
#print axioms wordMap_ones
#print axioms implementationExtensionality_ones
#print axioms spectatorIndependent_ones
#print axioms hComp_ones
#print axioms transport_apply
#print axioms transport_conjChannel
#print axioms reindex_isometry
#print axioms permMatrix_isometry
#print axioms withSpectator_eq_transport
#print axioms hCompRealized_spectator_available
#print axioms hCompRealized_ones_of_control
#print axioms countermodel_hCompRealized_ones
#print axioms fullQuantum_hCompRealized_ones
#print axioms hcompRealized_not_implies_parallelReferenceExtension
#print axioms hcompRealized_consistent_with_parallelReferenceExtension

end SpectatorBridge
end OIBridge
