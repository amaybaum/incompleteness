/-
  OIBridge/StinespringAssembly.lean — the generic Kraus assembly: from composite unitary
  control to all finite endomorphic instruments.

  PHASE THREE, THE KRAUS ROUND. Round 25b/25c built the operational closure structure and
  removed the last hidden pure-seed assumption. What remains is mechanical, and this file
  does it — with the one external fact isolated as an explicit hypothesis rather than a
  prose citation.

  §A — THE SYSTEM-FIRST MIRRORS. Round twenty's dilation algebra is ANCILLA-FIRST
  (`Matrix (ι × S) S`), while the operational development is SYSTEM-FIRST
  (`Matrix (A × Fin n) A`). Rather than rewrite either, this file adds the mirrored
  `Vsf`/`Esf` and PINS them to round twenty's definitions pointwise
  (`Vsf_eq_dilationIsometry`, `Esf_eq_seedEmbed`), so the two cannot drift apart.

  §B — THE THREE EXACT IDENTITIES.

      `vsf_gram`   :  (V_K)† V_K = ∑ₖ Kₖ† Kₖ,  so normalization ⟺ isometry
      `esf_conj`   :  E_{k₀} ρ E_{k₀}† = ρ ⊗ |k₀⟩⟨k₀|
      `vsf_block`  :  blockₖ(V_K ρ V_K†) = Kₖ ρ Kₖ†

  §C — THE BOUNDARY, ISOLATED. `FiniteIsometryExtensionSF` states EXACTLY what the
  assembly consumes: every system-first isometry extends to a unitary agreeing with it on
  the seed. It is a hypothesis of the capstone, not an axiom hidden in the file, so the
  dependency is visible in the theorem statement itself.

  §D — THE FINE BRANCH. `stinespringCircuit_branch`: with `U E_{k₀} = V_K`, the circuit
  branch of round 25b is exactly `ρ ↦ Kₖ ρ Kₖ†`. Kept standalone so the algebra is
  independently auditable, separately from the availability bookkeeping.

  §E — THE CAPSTONE.

      ┌────────────────────────────────────────────────────────────────────┐
      │  `fullInstruments_of_control`:                                      │
      │      FiniteIsometryExtensionSF ∧ HasCompositeUnitaryControl T       │
      │          ⟹ HasFullFiniteEndomorphicInstruments T.                   │
      └────────────────────────────────────────────────────────────────────┘

  WHAT IS DERIVED RATHER THAN ASSUMED INSIDE THIS CHAIN. The Lüders readout SHAPE
  (`readout_is_localLuders`, from map-level spectator independence) and the PURE ANCILLA
  (`pureSeedPrep_available`, from the uniform attachment plus readout plus reversible
  feed-forward). Neither is a hypothesis anywhere.

  SCOPE, in the predicate's own name. The Kraus operators are square, so this is ALL
  FINITE ENDOMORPHIC INSTRUMENTS ON A FIXED SYSTEM `A` — not "all finite quantum
  instruments" unqualified, which needs rectangular Kraus maps or a dimension-changing
  encoding. The Kraus index is `Fin (n+1)`: the circuit needs a level `k₀` to seed, and on
  a nonempty system a normalized empty Kraus family is impossible anyway.

  BOUNDARY FOR THIS THEOREM: finite isometry extension ALONE. Purification and Uhlmann
  uniqueness are not used. The project's global boundary remains the four-item ledger.
  [HISTORICAL, SUPERSEDED BY THE ROUND-35 BOUNDARY AUDIT: PSD square-root/factorization was discharged internally in round thirty-four (`psdFactorization_of_spectral`), so the current unresolved boundary is three items — see `BoundaryAudit.lean`.]

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.OperationalAssembly

namespace OIBridge
namespace StinespringAssembly

open Complex Matrix CoherentExtension InstrumentDilation MonoidalCompletion
open OperationalAssembly

local notation "conj'" => (starRingEnd ℂ)

variable {A : Type*} [Fintype A] [DecidableEq A]

/-! ### Section A — the system-first mirrors -/

/-- The Stinespring isometry, SYSTEM-FIRST: `V (s', k) s = Kₖ(s', s)`. -/
def Vsf {n : ℕ} (K : Fin n → Matrix A A ℂ) : Matrix (A × Fin n) A ℂ :=
  Matrix.of fun p s => K p.2 p.1 s

/-- The pure-seed embedding, SYSTEM-FIRST: `|ψ⟩ ↦ |ψ⟩ ⊗ |k₀⟩`. -/
def Esf {n : ℕ} (k₀ : Fin n) : Matrix (A × Fin n) A ℂ :=
  Matrix.of fun p s => if p.2 = k₀ then (if p.1 = s then 1 else 0) else 0

omit [Fintype A] [DecidableEq A] in
/-- **PINNED TO ROUND TWENTY, POINTWISE.** The system-first isometry is round twenty's
ancilla-first one with the factors swapped — so the two developments cannot drift. -/
theorem Vsf_eq_dilationIsometry {n : ℕ} (K : Fin n → Matrix A A ℂ) (s' : A) (k : Fin n)
    (s : A) : Vsf K (s', k) s = dilationIsometry K (k, s') s := rfl

omit [Fintype A] in
/-- **PINNED TO ROUND TWENTY, POINTWISE.** Likewise for the seed embedding. -/
theorem Esf_eq_seedEmbed {n : ℕ} (k₀ : Fin n) (s' : A) (k : Fin n) (s : A) :
    Esf k₀ (s', k) s = seedEmbed k₀ (k, s') s := rfl

/-! ### Section B — the three exact identities -/

omit [DecidableEq A] in
/-- **NORMALIZATION IS ISOMETRY.** `(V_K)† V_K = ∑ₖ Kₖ† Kₖ`. -/
theorem vsf_gram {n : ℕ} (K : Fin n → Matrix A A ℂ) :
    (Vsf K)ᴴ * Vsf K = ∑ k, (K k)ᴴ * K k := by
  ext s t
  rw [Matrix.mul_apply, Matrix.sum_apply, Fintype.sum_prod_type, Finset.sum_comm]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Matrix.mul_apply]
  exact Finset.sum_congr rfl fun s' _ => by
    rw [Matrix.conjTranspose_apply, Matrix.conjTranspose_apply]
    rfl

/-- **THE SEED EMBEDDING PREPARES THE PURE PRODUCT.** `E_{k₀} ρ E_{k₀}† = ρ ⊗ |k₀⟩⟨k₀|`. -/
theorem esf_conj {n : ℕ} (k₀ : Fin n) (ρ : Matrix A A ℂ) :
    Esf k₀ * ρ * (Esf (A := A) k₀)ᴴ = pureAttach n k₀ ρ := by
  ext p q
  rw [pureAttach_apply, tensorOf_apply, single_entry, Matrix.mul_apply,
    Finset.sum_eq_single q.1]
  · rw [Matrix.mul_apply, Finset.sum_eq_single p.1]
    · rw [Matrix.conjTranspose_apply]
      show (if p.2 = k₀ then (if p.1 = p.1 then (1 : ℂ) else 0) else 0) * ρ p.1 q.1
          * conj' (if q.2 = k₀ then (if q.1 = q.1 then (1 : ℂ) else 0) else 0) = _
      rw [if_pos rfl, if_pos rfl]
      by_cases h : k₀ = p.2 ∧ k₀ = q.2
      · rw [if_pos h, if_pos h.1.symm, if_pos h.2.symm]
        simp
      · rw [if_neg h]
        rcases (not_and_or.mp h) with h1 | h1
        · rw [if_neg (show ¬(p.2 = k₀) from fun hh => h1 hh.symm), zero_mul, zero_mul,
            mul_zero]
        · rw [if_neg (show ¬(q.2 = k₀) from fun hh => h1 hh.symm), map_zero, mul_zero,
            mul_zero]
    · intro s _ hs
      show (if p.2 = k₀ then (if p.1 = s then (1 : ℂ) else 0) else 0) * ρ s q.1 = 0
      rw [if_neg (show ¬(p.1 = s) from fun hh => hs hh.symm), ite_self, zero_mul]
    · intro hc
      exact absurd (Finset.mem_univ _) hc
  · intro t _ ht
    rw [Matrix.conjTranspose_apply]
    show (Esf k₀ * ρ : Matrix (A × Fin n) A ℂ) p t
        * conj' (if q.2 = k₀ then (if q.1 = t then (1 : ℂ) else 0) else 0) = 0
    rw [if_neg (show ¬(q.1 = t) from fun hh => ht hh.symm), ite_self, map_zero,
      mul_zero]
  · intro hc
    exact absurd (Finset.mem_univ _) hc

omit [DecidableEq A] in
/-- **THE ANCILLA BLOCK IS THE KRAUS BRANCH.** `blockₖ(V_K ρ V_K†) = Kₖ ρ Kₖ†`. -/
theorem vsf_block {n : ℕ} (K : Fin n → Matrix A A ℂ) (k : Fin n) (ρ : Matrix A A ℂ)
    (s t : A) : (Vsf K * ρ * (Vsf K)ᴴ) (s, k) (t, k) = (K k * ρ * (K k)ᴴ) s t := by
  rw [Matrix.mul_apply, Matrix.mul_apply]
  refine Finset.sum_congr rfl fun v _ => ?_
  rw [Matrix.conjTranspose_apply, Matrix.conjTranspose_apply, Matrix.mul_apply,
    Matrix.mul_apply]
  rfl

/-! ### Section C — the boundary, isolated -/

/-- **THE ONLY EXTERNAL FACT THIS ASSEMBLY CONSUMES**, stated in exactly the form it is
used: every system-first isometry extends to a unitary agreeing with it on the seed. It is
a HYPOTHESIS of the capstone, not an axiom hidden in the file, so the dependency is visible
in the theorem statement. -/
def FiniteIsometryExtensionSF (A : Type*) [Fintype A] [DecidableEq A] : Prop :=
  ∀ (n : ℕ) (k₀ : Fin (n + 1)) (V : Matrix (A × Fin (n + 1)) A ℂ), Vᴴ * V = 1 →
    ∃ U : Matrix (A × Fin (n + 1)) (A × Fin (n + 1)) ℂ, Uᴴ * U = 1 ∧ U * Esf k₀ = V

/-! ### Section D — the fine branch -/

/-- **THE FINE BRANCH IS THE KRAUS BRANCH.** With `U E_{k₀} = V_K`, the round-25b circuit
branch is exactly `ρ ↦ Kₖ ρ Kₖ†`. Kept standalone from the availability bookkeeping so the
algebra is independently auditable. -/
theorem stinespringCircuit_branch {n : ℕ} (K : Fin (n + 1) → Matrix A A ℂ)
    (k₀ k : Fin (n + 1)) (U : Matrix (A × Fin (n + 1)) (A × Fin (n + 1)) ℂ)
    (hUE : U * Esf k₀ = Vsf K) (ρ : Matrix A A ℂ) :
    discardMap (n + 1) k₀ ((localLuders k).comp (conjChannel U)) ρ
      = conjChannel (K k) ρ := by
  rw [circuit_branch]
  ext s t
  show (U * tensorOf ρ (Matrix.single k₀ k₀ 1) * Uᴴ) (s, k) (t, k) = _
  have hE : tensorOf ρ (Matrix.single k₀ k₀ 1) = Esf k₀ * ρ * (Esf (A := A) k₀)ᴴ := by
    rw [esf_conj, pureAttach_apply]
  have hassoc : U * (Esf k₀ * ρ * (Esf (A := A) k₀)ᴴ) * Uᴴ = Vsf K * ρ * (Vsf K)ᴴ := by
    rw [← hUE, Matrix.conjTranspose_mul]
    simp only [Matrix.mul_assoc]
  rw [hE, hassoc, vsf_block]
  rfl

/-! ### Section E — the capstone -/

/-- **ALL FINITE ENDOMORPHIC INSTRUMENTS ON A FIXED SYSTEM `A`**, as a property of the
operational theory itself. The Kraus operators are square — this is NOT "all finite quantum
instruments" unqualified. The index is `Fin (n+1)`: the circuit needs a level to seed, and
on a nonempty system a normalized empty Kraus family is impossible anyway. -/
def HasFullFiniteEndomorphicInstruments (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n m : ℕ) (K : Fin (n + 1) → Matrix A A ℂ) (out : Fin (n + 1) → Fin m),
    (∑ k, (K k)ᴴ * K k = 1) → T.avail (Fin m) (instrumentBranch K out)

/-- **THE CAPSTONE.** Composite-dimension unitary control, plus finite isometry extension
as an explicit hypothesis, delivers every finite endomorphic instrument on the system.

The Lüders readout SHAPE and the PURE ANCILLA are derived inside the chain, not assumed:
the readout form comes from `readout_is_localLuders` (map-level spectator independence) and
the seed from `pureSeedPrep_available` (uniform attachment + readout + reversible
feed-forward). No `H-readout` and no `H-pure-seed` hypothesis appears anywhere. -/
theorem fullInstruments_of_control (T : FiniteOperationalTheory A)
    (hext : FiniteIsometryExtensionSF A) (hctrl : HasCompositeUnitaryControl T) :
    HasFullFiniteEndomorphicInstruments T := by
  intro n m K out hnorm
  obtain ⟨U, hU, hUE⟩ := hext n 0 (Vsf K) (by rw [vsf_gram]; exact hnorm)
  have havail := circuit_available_pureSeed T hctrl n 0 U hU
  rw [show (fun k => discardMap (n + 1) (0 : Fin (n + 1))
        ((localLuders k).comp (conjChannel U)))
      = fun k => conjChannel (K k) from by
    funext k
    exact LinearMap.ext fun ρ => stinespringCircuit_branch K 0 k U hUE ρ] at havail
  exact T.avail_coarse (Fin (n + 1)) (Fin m) _ out havail

#print axioms Vsf_eq_dilationIsometry
#print axioms Esf_eq_seedEmbed
#print axioms vsf_gram
#print axioms esf_conj
#print axioms vsf_block
#print axioms stinespringCircuit_branch
#print axioms fullInstruments_of_control

end StinespringAssembly
end OIBridge
