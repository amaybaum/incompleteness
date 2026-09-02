/-
  OIBridge/BoundaryAudit.lean — the external boundary, audited after round thirty-four.

  ROUND THIRTY-FIVE, PART ONE. Through round thirty-four the project's global external
  boundary was stated as exactly four items:

      (1) compact Lie integration / reachability;
      (2) finite isometry extension;
      (3) PSD square-root / factorization;
      (4) finite Uhlmann / Schmidt / right-unitary uniqueness.

  Round thirty-four proved `psdFactorization_of_spectral`: for every finite carrier, every
  positive semidefinite matrix factorizes as `B Bᴴ`, inside Lean, from the rank-one spectral
  resolution (Mathlib's spectral theorem, treated as kernel-internal since the Kadison round)
  and the real square root of the eigenvalues, with no new axiom dependency. Under the
  conventions the project already uses, continuing to count PSD factorization as an
  unresolved external fact would be inconsistent. THIS FILE RECLASSIFIES IT.

  THE CURRENT UNRESOLVED EXTERNAL BOUNDARY: THREE ITEMS.

      1. compact Lie integration / reachability;
      2. finite isometry extension;
      3. finite Uhlmann / Schmidt / right-unitary uniqueness.

  DISCHARGED INTERNALLY (round thirty-four): PSD square-root / factorization, by
  `psdFactorization_of_spectral`, re-exported here as `psdFactorization_discharged`. The
  dependency did not disappear — it remains a mathematical dependency of purification and of
  the CP ⟹ Kraus step — it ceased to be an external one.

  PROVENANCE IS PRESERVED, NOT REWRITTEN. The four-item statements in
  `MonoidalCompletion.lean`, `OperationalAssembly.lean`, `StinespringAssembly.lean`, the
  finite-instruments milestone note and the older probe texts are left in place and labelled
  HISTORICAL, SUPERSEDED BY THE ROUND-35 BOUNDARY AUDIT: they were true when written.
  `Purification.lean` keeps its conditional theorem `purification_of_factorization`, whose
  hypothesis is now dischargeable, and cross-references the discharge;
  `purification_unconditional` below is the discharged form.

  WHAT THIS FILE DOES NOT DO. It proves nothing new. It does not touch the three remaining
  items, and it does not claim any of them is dischargeable.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.DimensionalCountermodel
import OIBridge.Purification

namespace OIBridge
namespace BoundaryAudit

open Matrix DimensionalCountermodel Purification

open scoped ComplexOrder

/-- **PSD FACTORIZATION IS KERNEL-INTERNAL**: the former boundary item 3, discharged. -/
theorem psdFactorization_discharged (R : Type*) [Fintype R] [DecidableEq R] :
    ∀ ρ : Matrix R R ℂ, ρ.PosSemidef → ∃ B : Matrix R R ℂ, ρ = B * Bᴴ :=
  psdFactorization_of_spectral R

/-- **PURIFICATION, UNCONDITIONAL**: every positive semidefinite state on `S` has a pure
purification on `S × S` — `purification_of_factorization` with its hypothesis discharged. -/
theorem purification_unconditional {S : Type*} [Fintype S] [DecidableEq S]
    (ρ : Matrix S S ℂ) (hρ : ρ.PosSemidef) :
    ∃ A : Matrix S S ℂ, ptraceB (Matrix.vecMulVec (purifVec A) (star (purifVec A))) = ρ := by
  obtain ⟨B, hB⟩ := psdFactorization_discharged S ρ hρ
  exact ⟨B, purification_of_factorization B ρ hB⟩

#print axioms psdFactorization_discharged
#print axioms purification_unconditional

end BoundaryAudit
end OIBridge
