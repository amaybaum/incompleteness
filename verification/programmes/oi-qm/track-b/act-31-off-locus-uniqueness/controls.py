"""Track B act 31 -- the round's own static controls, frozen with the control plane.

Written before F; its blob is frozen in the preregistration beside it, and the execution adds it
with that exact blob. It reads nothing but the repository at D and at the commit under check, and
it certifies nothing on its own: the Lean kernel, the axiom audit and the release gate establish
the mathematics, and the V3 verifier the protocol. What it checks is that the execution carries
the frozen statements, the frozen outcome grammar and the frozen surface edits, and nothing else.

    python3 controls.py --self-test     the duality of the two verdict propositions, the mutation
                                        controls on synthetic inputs, and the agreement of the
                                        constants below with the preregistration beside this file
    python3 controls.py check <commit>  every control against the tree at <commit>, read from git

Exit 1 on any failure.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

D = 'd61c6c5409db201e3c25abbf3ec0ecce1f530684'
RDIR = 'verification/programmes/oi-qm/track-b/act-31-off-locus-uniqueness/'
MODULE = 'verification/lean-mathlib/OIBridge/ProductOffLocusUniqueness.lean'
ROOT = 'verification/lean-mathlib/OIBridge.lean'
GUARD = 'verification/lean/edge_rigidity_probe.py'
CENSUS = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
ROADMAP_BLOB_D = 'e6779380f858bcb905fc9877ed2f11bf5de75c95'
GUARD_BLOB_D = '0475fe3d8c5724a7bf918bf3fd75ae06370cef26'

IMPORT = 'import OIBridge.ProductStrictLift\n'
WIRE_AFTER = 'import OIBridge.ProductStrictLift\n'
WIRE = 'import OIBridge.ProductOffLocusUniqueness\n'
OPEN = "open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection\n  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted OrbitLawGaps\n  OrbitGeometryIsometries StrictNaturalLift ProductLocusFreedom ProductAdmission ProductStrictLift\n"

# ---- the frozen propositions, verbatim
PROPS = {
 "P_N": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),\n    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →\n  ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3) →\n    f₂ = (fun G => G) →\n  ∃ Φ Φ' : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n    (ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))\n      ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))\n      ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ\n      ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ\n      ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ t = Φh)\n      ∧ Reversible (Fin 1 × Fin 1) Γ Φ\n      ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n          GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))\n      ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,\n          (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))\n          ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))\n          ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)\n      ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n          (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ\n      ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n          GramPhaseEquiv (Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2)))\n    ∧ (ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))\n      ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))\n      ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ'\n      ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ'\n      ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ' t = Φh)\n      ∧ Reversible (Fin 1 × Fin 1) Γ Φ'\n      ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n          GramPhaseEquiv G G' → GramPhaseEquiv (Φ' t G) (Φ' t G'))\n      ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,\n          (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ' t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))\n          ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))\n          ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)\n      ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n          (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ'\n      ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n          GramPhaseEquiv (Φ' t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2)))\n    ∧ ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G\n      ∧ (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →\n      ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n        X i.1 j.1 k.1 * Y i.2 j.2 k.2) G)\n      ∧ ¬ GramPhaseEquiv (Φ 0 G) (Φ' 0 G)",
 "P_U": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),\n    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →\n  ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3) →\n    f₂ = (fun G => G) →\n  ∀ Φ Φ' : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n    (ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))\n      ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))\n      ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ\n      ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ\n      ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ t = Φh)\n      ∧ Reversible (Fin 1 × Fin 1) Γ Φ\n      ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n          GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))\n      ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,\n          (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))\n          ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))\n          ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)\n      ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n          (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ\n      ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n          GramPhaseEquiv (Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))) →\n    (ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))\n      ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))\n      ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ'\n      ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ'\n      ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ' t = Φh)\n      ∧ Reversible (Fin 1 × Fin 1) Γ Φ'\n      ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n          GramPhaseEquiv G G' → GramPhaseEquiv (Φ' t G) (Φ' t G'))\n      ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,\n          (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ' t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))\n          ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))\n          ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)\n      ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n          (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ'\n      ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n          GramPhaseEquiv (Φ' t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))) →\n    ∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G →\n      (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →\n      ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n        X i.1 j.1 k.1 * Y i.2 j.2 k.2) G) →\n      GramPhaseEquiv (Φ 0 G) (Φ' 0 G)",
 "S_W": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),\n    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →\n  ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, X = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) →\n    Y = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;\n        1, -Complex.I, -1, Complex.I] p.1 q.1)) →\n  ∀ W W₂ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,\n    W = RelabelTransition (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)))\n      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) →\n    W₂ = RelabelTransition (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)))\n      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n        X i.1 j.1 k.1 * RelabelTransition (Equiv.swap (2 : Fin 4) 3) Y i.2 j.2 k.2) →\n    RealizableGram (Fin 1 × Fin 1) (Γ 0) W ∧ RealizableGram (Fin 1 × Fin 1) (Γ 0) W₂\n    ∧ (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →\n      ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n        X i.1 j.1 k.1 * Y i.2 j.2 k.2) W)\n    ∧ (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →\n      ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n        X i.1 j.1 k.1 * Y i.2 j.2 k.2) W₂)\n    ∧ ¬ GramPhaseEquiv W W₂",
 "S_TAU": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),\n    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →\n  ∀ W W₂ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) W → RealizableGram (Fin 1 × Fin 1) (Γ 0) W₂ →\n    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →\n      ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n        X i.1 j.1 k.1 * Y i.2 j.2 k.2) W) →\n    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →\n      ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n        X i.1 j.1 k.1 * Y i.2 j.2 k.2) W₂) →\n    ¬ GramPhaseEquiv W W₂ →\n  ∃ τ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n    (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → RealizableGram (Fin 1 × Fin 1) (Γ 0) (τ G))\n    ∧ (∀ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, GramPhaseEquiv G G' → GramPhaseEquiv (τ G) (τ G'))\n    ∧ (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, GramPhaseEquiv (τ (τ G)) G)\n    ∧ (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧\n      GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n        X i.1 j.1 k.1 * Y i.2 j.2 k.2) G) → τ G = G)\n    ∧ GramPhaseEquiv (τ W) W₂",
 "S_PRE": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),\n    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →\n  ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3) →\n    f₂ = (fun G => G) →\n  ∀ Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n    (EvolvesTotally (Fin 1 × Fin 1) Γ Φ\n      ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ\n      ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ t = Φh)\n      ∧ Reversible (Fin 1 × Fin 1) Γ Φ\n      ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n          GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))\n      ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n          (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ\n      ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n          GramPhaseEquiv (Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))) →\n  ∀ τ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n    (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → RealizableGram (Fin 1 × Fin 1) (Γ 0) (τ G)) →\n    (∀ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, GramPhaseEquiv G G' → GramPhaseEquiv (τ G) (τ G')) →\n    (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, GramPhaseEquiv (τ (τ G)) G) →\n    (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧\n      GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n        X i.1 j.1 k.1 * Y i.2 j.2 k.2) G) → τ G = G) →\n    (EvolvesTotally (Fin 1 × Fin 1) Γ (fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G))\n      ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ (fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G))\n      ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, (fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G)) t = Φh)\n      ∧ Reversible (Fin 1 × Fin 1) Γ (fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G))\n      ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n          GramPhaseEquiv G G' → GramPhaseEquiv ((fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G)) t G) ((fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G)) t G'))\n      ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n          (fun _ => Γ₀) (fun _ => Γ₀) Γ (fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G))\n      ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n          GramPhaseEquiv ((fun (t : ℕ) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) => Φ t (τ G)) t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2)))"
}
# ---- the components the two verdict propositions are built from
COMPONENTS = {
 "HEAD": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),\n    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →\n  ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3) →\n    f₂ = (fun G => G) →\n",
 "A_PHI": "ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))\n      ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))\n      ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ\n      ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ\n      ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ t = Φh)\n      ∧ Reversible (Fin 1 × Fin 1) Γ Φ\n      ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n          GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))\n      ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,\n          (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))\n          ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))\n          ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)\n      ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n          (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ\n      ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n          GramPhaseEquiv (Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))",
 "A_PHI2": "ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))\n      ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ\n        (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ' t (𝔾 t)))\n      ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ'\n      ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ'\n      ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ' t = Φh)\n      ∧ Reversible (Fin 1 × Fin 1) Γ Φ'\n      ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n          GramPhaseEquiv G G' → GramPhaseEquiv (Φ' t G) (Φ' t G'))\n      ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,\n          (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ' t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))\n          ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n            AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))\n          ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)\n      ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n          (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ'\n      ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n          GramPhaseEquiv (Φ' t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))",
 "RPG": "RealizableGram (Fin 1 × Fin 1) (Γ 0) G",
 "OFFG": "(∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →\n      ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n        X i.1 j.1 k.1 * Y i.2 j.2 k.2) G)",
 "EQ": "GramPhaseEquiv (Φ 0 G) (Φ' 0 G)",
 "TP": "Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ"
}

# ---- the label theorems: (label, theorem name, proposition)
LABELS = (('A31-1-NONUNIQUE', 'a31_nonunique', 'P_N'), ('A31-1-UNIQUE', 'a31_unique', 'P_U'))
UNDECIDED = 'A31-1-UNDECIDED'
ROWS = ('A31-1-NONUNIQUE', 'A31-1-UNIQUE', 'A31-1-UNDECIDED')
# ---- the corollary, required in every case
COROLLARY = ('a31_c_exclusive', ('P_N',), 'P_U')
# ---- the shared statements required under A31-1-NONUNIQUE
REQUIRED_NONUNIQUE = (('a31_shared_witnesses', 'S_W'), ('a31_shared_transposition', 'S_TAU'),
                      ('a31_shared_precompose', 'S_PRE'))
SHARED = re.compile(r'a31_shared_[A-Za-z0-9_]+\Z')
OUTCOME_RE = re.compile(r'\*\*Outcome:\*\* `(A31-1-[A-Z]+)`')
LABEL_RE = re.compile(r'A31-1-(?:NONUNIQUE|UNIQUE|UNDECIDED)')

SENTENCES = {
 "A31-1-NONUNIQUE": "At the frozen product configuration, for the pair of local class bijections act 28 fixed in advance, two exhibited transition families each satisfy all eight prefix conjuncts and factorization with factor families realizing that pair, and take `GramPhaseEquiv`-inequivalent values at time zero on an exhibited tuple realizable at the product visible family whose class lies outside the product locus, at evidence level 2. This is a nonuniqueness statement about two exhibited laws at that pair and that time. It does not say that factorization is empty, has no content, or fails to restrict anything, and it reports nothing about any other pair or configuration.",
 "A31-1-UNIQUE": "At the frozen product configuration, for the pair of local class bijections act 28 fixed in advance, any two transition families satisfying all eight prefix conjuncts and factorization with factor families realizing that pair take `GramPhaseEquiv`-equivalent values at time zero on every tuple realizable at the product visible family whose class lies outside the product locus, at evidence level 2. The agreement asserted is agreement up to `GramPhaseEquiv` at time zero, not equality of families, and it is asserted for that pair alone.",
 "A31-1-UNDECIDED": "Neither the nonuniqueness nor the uniqueness was obtained. The step at which the proof stopped is named, with what would settle it."
}
# the clause's body; its heading names the artifact carrying it
CLAUSE = "Act 31 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts\nnone. A law that survives every condition this freeze names is a law that survives **those**\nconditions, at the configuration frozen for it, and it is **not** a finding that it obtains in\nnature, **not** a finding that the programme requires it, and **not** an adoption of it as the\nphysical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about\nthe frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence\nto add one more condition, or to widen one more equivalence, until a plurality becomes a point.\n**No law gains physical status by surviving, no carrier and no principle is adopted as the physical\none, and nothing here derives, recognises or approaches quantum evolution.**"
MENTION = 'THE CLAUSE, carried at this mention'

P0_STANDING = "`P0`'s threading part is untouched, no carrier is adopted as the physical one, no surviving law is adopted as the physical one, and nothing here names, endorses or excludes a selection principle."
P0_ADMITS = "At the product configuration, the ladder's conditions through factorization admit every pair of local class bijections: each such pair is the class action of the factor families of a single law carrying all of them, so those conditions do not select among local behaviours."
P0_CASE = {
 "A31-1-NONUNIQUE": "For the local pair fixed in advance, two such laws can disagree on a class away from the product inputs, so those conditions do not fix a law's action there from its action on product inputs.",
 "A31-1-UNIQUE": "For the local pair fixed in advance, two such laws take equivalent values on every realizable input away from the product inputs, so for that pair those conditions fix the law's action there up to the gauge equivalence."
}

CENSUS_MODULES = ['ProductOffLocusUniqueness']

_BAD_CMD = re.compile(
    r'(?m)^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?(?:(?:private|protected|noncomputable|partial|unsafe)'
    r'[ \t]+)*(?:def|abbrev|structure|class|instance|axiom|opaque|inductive|variable|include|omit|'
    r'export|notation|infix|infixl|infixr|prefix|postfix|macro|macro_rules|syntax|elab|elab_rules|'
    r'attribute|universe|mutual|local|scoped|import|#check|#eval|#reduce|#exit|#guard)\b')
_BAD_TOKEN = re.compile(r'\b(?:sorry|admit|native_decide)\b')


# ------------------------------------------------------------------------------------------------
def norm(t):
    t = ' '.join(t.split())
    t = re.sub(r'\( ', '(', t)
    return re.sub(r' \)', ')', t)


def qnorm(t):
    return ' '.join(re.sub(r'(?m)^[ \t]*>[ \t]?', '', t).split())


def prime(t):
    """The second law's copy of a text: every standalone `Φ` becomes `Φ'`."""
    return re.sub(r"(?<![\w'])Φ(?![\w'])", "Φ'", t)


def dual_texts(c):
    """The two verdict propositions, rebuilt from their shared components."""
    n = (c['HEAD'] + "  ∃ Φ Φ' : ℕ → (" + c['TP'] + ') → (' + c['TP'] + '),\n'
         + '    (' + c['A_PHI'] + ')\n    ∧ (' + c['A_PHI2'] + ')\n'
         + '    ∧ ∃ G : ' + c['TP'] + ', ' + c['RPG'] + '\n      ∧ ' + c['OFFG']
         + '\n      ∧ ¬ ' + c['EQ'])
    u = (c['HEAD'] + "  ∀ Φ Φ' : ℕ → (" + c['TP'] + ') → (' + c['TP'] + '),\n'
         + '    (' + c['A_PHI'] + ') →\n    (' + c['A_PHI2'] + ') →\n'
         + '    ∀ G : ' + c['TP'] + ', ' + c['RPG'] + ' →\n      ' + c['OFFG']
         + ' →\n      ' + c['EQ'])
    return n, u


def duality_ok(props, comps):
    """P_N is `∃ Φ Φ', A ∧ A' ∧ ∃ G, R ∧ O ∧ ¬ E` and P_U is `∀ Φ Φ', A → A' → ∀ G, R → O → E`,
    over one head, one admission body A (with A' its primed copy), one realizability clause R,
    one off-locus clause O and one time-zero comparison E -- so each is the other's negation."""
    f = []
    n, u = dual_texts(comps)
    if norm(props['P_N']) != norm(n):
        f.append('duality:P_N-is-not-the-frozen-existential-form')
    if norm(props['P_U']) != norm(u):
        f.append('duality:P_U-is-not-the-frozen-universal-form')
    if norm(prime(comps['A_PHI'])) != norm(comps['A_PHI2']):
        f.append("duality:the-second-law's-admission-is-not-the-first's-copy")
    if norm(comps['EQ']) != norm("GramPhaseEquiv (Φ 0 G) (Φ' 0 G)"):
        f.append('duality:the-comparison-is-not-at-time-zero')
    return f


def strip_comments(src):
    out, i, depth, n = [], 0, 0, len(src)
    while i < n:
        if src.startswith('/-', i):
            depth += 1
            i += 2
        elif depth and src.startswith('-/', i):
            depth -= 1
            i += 2
        elif depth:
            out.append('\n' if src[i] == '\n' else ' ')
            i += 1
        elif src.startswith('--', i):
            j = src.find('\n', i)
            i = n if j < 0 else j
        else:
            out.append(src[i])
            i += 1
    return ''.join(out)


_THM = re.compile(r'(?m)^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?(?:private[ \t]+|protected[ \t]+)?'
                  r'(?:theorem|lemma)[ \t]+(\S+)')


def theorems(code):
    out = {}
    for m in _THM.finditer(code):
        nm = m.group(1)
        rest = code[m.end():]
        j = rest.find(':=')
        out[nm] = None if nm in out else (rest if j < 0 else rest[:j])
    return out


def statement(key):
    return norm(': ' + PROPS[key])


def corollary_statement():
    nm, prem, concl = COROLLARY
    return norm(': ' + ' → '.join('(' + PROPS[p] + ')' for p in prem) + ' → ¬ (' + PROPS[concl] + ')')


# ---- the module -------------------------------------------------------------------------------
def module_label(src):
    f = []
    if not src.startswith(IMPORT):
        f.append('module:first-line-is-not-the-frozen-import')
    code = strip_comments(src)
    body = code[len(IMPORT):] if code.startswith(IMPORT) else code
    if _BAD_CMD.search(body):
        f.append('module:forbidden-command:' + _BAD_CMD.search(body).group(0).strip())
    if _BAD_TOKEN.search(code):
        f.append('module:forbidden-token:' + _BAD_TOKEN.search(code).group(0))
    opens = [m.start() for m in re.finditer(r'(?m)^[ \t]*open\b', code)]
    if len(opens) != 1 or not code[opens[0]:].startswith(OPEN):
        f.append('module:open-is-not-exactly-the-frozen-one')
    if 'namespace OIBridge\nnamespace ProductOffLocusUniqueness\n' not in code or \
            not code.rstrip().endswith('end ProductOffLocusUniqueness\nend OIBridge'):
        f.append('module:namespace')
    th = theorems(code)
    if any(v is None for v in th.values()):
        f.append('module:theorem-declared-twice')
    if opens and th and min(m.start() for m in _THM.finditer(code)) < opens[0]:
        f.append('module:theorem-before-open')
    printed = re.findall(r'(?m)^[ \t]*#print[ \t]+axioms[ \t]+(\S+)[ \t]*$', code)
    if sorted(printed) != sorted(set(printed)):
        f.append('module:axioms-printed-twice')
    for nm in th:
        if nm not in printed:
            f.append('module:no-print-axioms:' + nm)
    for nm in printed:
        if nm not in th:
            f.append('module:print-axioms-of-no-theorem:' + nm)
    names = {x[1] for x in LABELS} | {COROLLARY[0]}
    for nm in th:
        if nm not in names and not SHARED.match(nm):
            f.append('module:theorem-name-outside-the-frozen-set:' + nm)
    earned = []
    for lab, nm, key in LABELS:
        if nm in th and th[nm] is not None:
            if norm(th[nm]) != statement(key):
                f.append('module:statement-not-frozen:' + nm)
            earned.append(lab)
    if len(earned) > 1:
        f.append('module:both-labels')
        return None, f
    label = earned[0] if earned else UNDECIDED
    if COROLLARY[0] not in th:
        f.append('module:required-corollary-absent:' + COROLLARY[0])
    elif th[COROLLARY[0]] is not None and norm(th[COROLLARY[0]]) != corollary_statement():
        f.append('module:statement-not-frozen:' + COROLLARY[0])
    for nm, key in REQUIRED_NONUNIQUE:
        if nm in th and th[nm] is not None and norm(th[nm]) != statement(key):
            f.append('module:statement-not-frozen:' + nm)
        if label == 'A31-1-NONUNIQUE' and nm not in th:
            f.append('module:required-shared-statement-absent:' + nm)
    return label, f


# ---- the result note ---------------------------------------------------------------------------
def note_ok(note, label):
    f = []
    found = OUTCOME_RE.findall(note)
    if found != [label]:
        f.append('note:outcome-line:%s' % found)
    q = qnorm(note)
    if q.count(qnorm(SENTENCES[label])) != 1:
        f.append('note:frozen-sentence:' + label)
    for lab in SENTENCES:
        if lab != label and qnorm(SENTENCES[lab]) in q:
            f.append('note:sentence-of-a-label-not-earned:' + lab)
    body = qnorm(CLAUSE)
    if note.count(MENTION) != 1 or q.count(body) != 1 or \
            not 0 <= q.index(body) - q.index(MENTION) <= 80:
        f.append('note:the-clause')
    if label == 'A31-1-NONUNIQUE':
        for nm, _ in REQUIRED_NONUNIQUE:
            if '`%s`' % nm not in note:
                f.append('note:required-shared-statement-not-named:' + nm)
    return f


# ---- the surfaces ------------------------------------------------------------------------------
def expected_roadmap(road_d, label):
    if label == UNDECIDED:
        return road_d
    old = ' ' + P0_ADMITS + ' ' + P0_STANDING + ' |'
    if road_d.count(old) != 1:
        return None
    return road_d.replace(old, ' ' + P0_ADMITS + ' ' + P0_STANDING + ' ' + P0_CASE[label]
                          + ' ' + P0_STANDING + ' |', 1)


def census_ok(cen_d, cen_e, label):
    f = []
    try:
        d, e = json.loads(cen_d), json.loads(cen_e)
    except ValueError:
        return ['census:not-json']
    if cen_e != json.dumps(e, indent=2, ensure_ascii=False) + '\n':
        f.append('census:not-in-the-registry-format')
    fams = e.get('families', [])
    mine = [x for x in fams if 'ProductOffLocusUniqueness' in x.get('modules', [])]
    if len(mine) != 1 or fams[-1:] != mine:
        return f + ['census:family-count-or-place']
    m = mine[0]
    if m.get('modules') != CENSUS_MODULES or m.get('status') != 'kernel-only' or \
            m.get('manuscript') != []:
        f.append('census:family-disposition')
    if LABEL_RE.findall(m.get('note', '')) != [label]:
        f.append('census:outcome')
    if dict(e, families=fams[:-1]) != d:
        f.append('census:another-entry-changed')
    return f


def wire_ok(root_d, root_e):
    if root_d.count(WIRE_AFTER) != 1:
        return ['wire:anchor']
    return [] if root_e == root_d.replace(WIRE_AFTER, WIRE_AFTER + WIRE, 1) else ['wire:root']


def expected_paths(label):
    p = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
         MODULE: 'A', ROOT: 'M', CENSUS: 'M'}
    if label != UNDECIDED:
        p[ROADMAP] = 'M'
    return p


def check_all(files_d, files_e, delta):
    f = duality_ok(PROPS, COMPONENTS)
    label, g = module_label(files_e.get(MODULE, ''))
    f += g
    if label is None:
        return f
    f += note_ok(files_e.get(RDIR + 'result.md', ''), label)
    road = expected_roadmap(files_d[ROADMAP], label)
    if road is None or files_e.get(ROADMAP) != road:
        f.append('roadmap:not-as-frozen-for-the-case')
    if files_e.get(GUARD) != files_d[GUARD]:
        f.append('guard:changed')
    f += census_ok(files_d[CENSUS], files_e.get(CENSUS, ''), label)
    f += wire_ok(files_d[ROOT], files_e.get(ROOT, ''))
    if delta != expected_paths(label):
        f.append('paths:delta-is-not-the-frozen-set')
    return f


# ---- git ---------------------------------------------------------------------------------------
def git(*a):
    return subprocess.run(('git',) + a, capture_output=True, check=True).stdout


def blob_id(text):
    b = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def cmd_check(commit):
    paths = (MODULE, ROOT, GUARD, CENSUS, ROADMAP, RDIR + 'result.md')
    fd, fe = {}, {}
    for p in paths:
        for ref, dst in ((D, fd), (commit, fe)):
            try:
                dst[p] = git('show', '%s:%s' % (ref, p)).decode('utf-8')
            except subprocess.CalledProcessError:
                pass
    f = []
    if blob_id(fd[ROADMAP]) != ROADMAP_BLOB_D or blob_id(fd[GUARD]) != GUARD_BLOB_D:
        f.append('base:D-is-not-the-frozen-base')
    delta = {}
    for ln in git('diff', '--no-renames', '--name-status', D, commit).decode().splitlines():
        st, p = ln.split('\t', 1)
        delta[p] = st
    f += check_all(fd, fe, delta)
    label, _ = module_label(fe.get(MODULE, ''))
    print('controls: label read off the module:', label)
    print('controls: %d path(s) changed from D' % len(delta))
    return f


# ---- the self-test -----------------------------------------------------------------------------
def _module(label, extra='', drop=(), stmt=None):
    parts = [IMPORT, '/-! synthetic -/\n', 'namespace OIBridge\nnamespace ProductOffLocusUniqueness\n\n',
             OPEN, '\n']
    def th(nm, s):
        parts.append('theorem %s :\n    %s := by\n  exact test\n#print axioms %s\n\n' % (nm, s, nm))
    th('a31_shared_x', 'True')
    if label == 'A31-1-NONUNIQUE':
        for nm, key in REQUIRED_NONUNIQUE:
            if nm not in drop:
                th(nm, (stmt or {}).get(nm, PROPS[key]))
    for lab, nm, key in LABELS:
        if lab == label and nm not in drop:
            th(nm, (stmt or {}).get(nm, PROPS[key]))
    if COROLLARY[0] not in drop:
        th(COROLLARY[0], (stmt or {}).get(COROLLARY[0], corollary_statement()[2:]))
    parts.append(extra)
    parts.append('end ProductOffLocusUniqueness\nend OIBridge\n')
    return ''.join(parts)


def _note(label):
    parts = ['# result\n\n**Outcome:** `%s`\n\n' % label, '> ' + SENTENCES[label] + '\n\n']
    parts.append('> **' + MENTION + ' — the result note.**\n'
                 + '\n'.join('> ' + l for l in CLAUSE.split('\n')) + '\n\n')
    if label == 'A31-1-NONUNIQUE':
        parts.append(' '.join('`%s`' % nm for nm, _ in REQUIRED_NONUNIQUE) + '\n')
    return ''.join(parts)


def _synthetic_d():
    road = '| **P0** | q | x | a. ' + P0_ADMITS + ' ' + P0_STANDING + ' | y |\n'
    cen = json.dumps({'families': [{'name': 'x', 'modules': ['X'], 'status': 'kernel-only',
                                    'manuscript': [], 'note': 'n'}]},
                     indent=2, ensure_ascii=False) + '\n'
    return {ROADMAP: road, CENSUS: cen, ROOT: 'import A\n' + WIRE_AFTER + 'import B\n',
            GUARD: '# guard\n'}


def _synthetic_e(fd, label):
    fe = {MODULE: _module(label), RDIR + 'result.md': _note(label),
          ROADMAP: expected_roadmap(fd[ROADMAP], label), GUARD: fd[GUARD]}
    c = json.loads(fd[CENSUS])
    c['families'].append({'name': 'act 31', 'modules': ['ProductOffLocusUniqueness'],
                          'status': 'kernel-only', 'manuscript': [],
                          'note': 'Outcome: ' + label + '.'})
    fe[CENSUS] = json.dumps(c, indent=2, ensure_ascii=False) + '\n'
    fe[ROOT] = fd[ROOT].replace(WIRE_AFTER, WIRE_AFTER + WIRE, 1)
    return fe, expected_paths(label)


def self_test():
    bad = []
    here = os.path.dirname(os.path.abspath(__file__))
    pre = os.path.join(here, 'preregistration.md')
    if not os.path.exists(pre):
        bad.append('agreement: preregistration.md not beside controls.py')
    else:
        text = open(pre, encoding='utf-8').read()
        q, n = qnorm(text), norm(text)
        for k, v in PROPS.items():
            if norm(v) not in n:
                bad.append('agreement: proposition %s not in the preregistration' % k)
        for k, v in list(SENTENCES.items()) + [('clause', CLAUSE), ('standing', P0_STANDING),
                                               ('admits', P0_ADMITS)] + list(P0_CASE.items()):
            if qnorm(v) not in q:
                bad.append('agreement: %s not in the preregistration' % k)
        for b in (ROADMAP_BLOB_D, GUARD_BLOB_D, D):
            if b not in text:
                bad.append('agreement: %s not in the preregistration' % b)
    for a, x in SENTENCES.items():
        for b, y in SENTENCES.items():
            if a != b and qnorm(x) in qnorm(y):
                bad.append('distinctness: the sentence of %s lies inside that of %s' % (a, b))
    # the duality holds of the frozen texts, and fails when either is altered
    if duality_ok(PROPS, COMPONENTS):
        bad.append('duality: the frozen propositions are not duals: %s' % duality_ok(PROPS, COMPONENTS))
    dmuts = 0
    for nm, key, old, new in (
            ('P_U-at-time-one', 'P_U', "(Φ' 0 G)", "(Φ' 1 G)"),
            ('P_N-comparison-unnegated', 'P_N', "∧ ¬ GramPhaseEquiv", "∧ GramPhaseEquiv"),
            ('P_U-off-locus-dropped', 'P_U', 'X i.1 j.1 k.1 * Y i.2 j.2 k.2) G) →', 'X i.1 j.1 k.1 * Y i.2 j.2 k.2) G) ∨ True →'),
            ('P_N-second-law-properness-about-the-first', 'P_N', "(Φ' t (𝔾 t))", '(Φ t (𝔾 t))'),
            ('P_U-one-law-for-both', 'P_U', "(Φ' 0 G)", "(Φ 0 G)")):
        props = dict(PROPS)
        if props[key].count(old) < 1:
            bad.append('duality mutation %s: pattern absent' % nm)
            continue
        props[key] = props[key].replace(old, new, 1)
        dmuts += 1
        if not duality_ok(props, COMPONENTS):
            bad.append('duality mutation %s: accepted' % nm)
    comps = dict(COMPONENTS, A_PHI2=COMPONENTS['A_PHI2'].replace("Φ' t (𝔾 t)", 'Φ t (𝔾 t)', 1))
    dmuts += 1
    if not duality_ok(PROPS, comps):
        bad.append('duality mutation component-drift: accepted')

    fd = _synthetic_d()
    for label in ROWS:
        fe, delta = _synthetic_e(fd, label)
        r = check_all(fd, fe, delta)
        if r:
            bad.append('positive %s: %s' % (label, r))
    N, U, X = ROWS
    muts = []

    def mut(name, label, fn, want):
        fe, delta = _synthetic_e(fd, label)
        fe, delta = fn(dict(fe), dict(delta))
        r = check_all(fd, fe, delta)
        muts.append(name)
        if not any(x.startswith(want) for x in r):
            bad.append('mutation %s: expected %s, got %s' % (name, want, r))

    def modstmt(label, nm, s):
        return lambda fe, dl: (dict(fe, **{MODULE: _module(label, stmt={nm: s})}), dl)
    mut('definition-added', N, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'end ProductOffLocusUniqueness', 'noncomputable def zz := 1\nend ProductOffLocusUniqueness')}), dl),
        'module:forbidden-command')
    mut('variable-added', N, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a31_shared_x', '\nvariable (h : False)\ntheorem a31_shared_x')}), dl),
        'module:forbidden-command')
    mut('include-added', N, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a31_shared_x', '\ninclude h\ntheorem a31_shared_x')}), dl), 'module:forbidden-command')
    mut('second-open', N, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a31_shared_x', '\nopen Foo in\ntheorem a31_shared_x')}), dl), 'module:open')
    mut('second-import', N, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '/-! synthetic -/', 'import Mathlib\n/-! synthetic -/')}), dl), 'module:forbidden-command')
    mut('sorry', N, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('exact test', 'sorry', 1)}), dl),
        'module:forbidden-token')
    mut('print-axioms-dropped', N, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '#print axioms a31_nonunique\n', '')}), dl), 'module:no-print-axioms')
    mut('stray-theorem-name', N, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'end ProductOffLocusUniqueness', 'theorem a31_n : True := trivial\n#print axioms a31_n\n'
        'end ProductOffLocusUniqueness')}), dl), 'module:theorem-name-outside')
    mut('nonunique-at-time-one', N, modstmt(N, 'a31_nonunique', PROPS['P_N'].replace("(Φ' 0 G)", "(Φ' 1 G)")),
        'module:statement-not-frozen:a31_nonunique')
    mut('unique-off-locus-dropped', U, modstmt(U, 'a31_unique', PROPS['P_U'].replace(
        'X i.1 j.1 k.1 * Y i.2 j.2 k.2) G) →', 'X i.1 j.1 k.1 * Y i.2 j.2 k.2) G) ∨ True →')),
        'module:statement-not-frozen:a31_unique')
    mut('witnesses-altered', N, modstmt(N, 'a31_shared_witnesses', PROPS['S_W'].replace(
        '∧ ¬ GramPhaseEquiv W W₂', '∧ True')), 'module:statement-not-frozen:a31_shared_witnesses')
    mut('transposition-locus-dropped', N, modstmt(N, 'a31_shared_transposition', PROPS['S_TAU'].replace(
        '→ τ G = G)', '→ True)')), 'module:statement-not-frozen:a31_shared_transposition')
    mut('precompose-altered', N, modstmt(N, 'a31_shared_precompose', PROPS['S_PRE'].replace(
        'Φ t (τ G)', 'Φ t G', 1)), 'module:statement-not-frozen:a31_shared_precompose')
    for nm, _ in REQUIRED_NONUNIQUE:
        mut('required-absent:' + nm, N, lambda fe, dl, nm=nm: (dict(fe, **{MODULE: _module(N, drop=(nm,))}), dl),
            'module:required-shared-statement-absent:' + nm)
    mut('corollary-absent', X, lambda fe, dl: (dict(fe, **{MODULE: _module(X, drop=('a31_c_exclusive',))}), dl),
        'module:required-corollary-absent')
    mut('corollary-altered', X, lambda fe, dl: (dict(fe, **{MODULE: _module(
        X, stmt={'a31_c_exclusive': corollary_statement()[2:].replace('→ ¬ (', '→ (', 1)})}), dl),
        'module:statement-not-frozen:a31_c_exclusive')
    mut('both-labels', N, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'end ProductOffLocusUniqueness', 'theorem a31_unique :\n    ' + PROPS['P_U'] + ' := by\n  exact test\n'
        '#print axioms a31_unique\nend ProductOffLocusUniqueness')}), dl), 'module:both-labels')
    mut('note-outcome-mismatch', N, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '**Outcome:** `A31-1-NONUNIQUE`', '**Outcome:** `A31-1-UNIQUE`')}), dl), 'note:outcome-line')
    mut('note-second-outcome', N, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n**Outcome:** `A31-1-NONUNIQUE`\n'}), dl), 'note:outcome-line')
    mut('note-sentence-altered', U, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        'evidence level 2', 'evidence level 3', 1)}), dl), 'note:frozen-sentence')
    mut('note-unearned-sentence', X, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + SENTENCES['A31-1-UNIQUE'] + '\n'}), dl), 'note:sentence-of-a-label-not-earned')
    mut('note-clause-twice', N, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + CLAUSE + '\n'}), dl), 'note:the-clause')
    mut('note-clause-detached', N, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        ' — the result note.**\n', ' — the result note.**\n' + 'x ' * 60 + '\n', 1)}), dl), 'note:the-clause')
    mut('note-witness-unnamed', N, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a31_shared_witnesses`', 'x')}), dl), 'note:required-shared-statement-not-named')
    mut('roadmap-wrong-case', N, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(fd[ROADMAP], U)}), dl),
        'roadmap:')
    mut('roadmap-standing-dropped', U, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        P0_CASE[U] + ' ' + P0_STANDING, P0_CASE[U])}), dl), 'roadmap:')
    mut('roadmap-touched-when-undecided', X, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(fd[ROADMAP], N)}),
        dict(dl, **{ROADMAP: 'M'})), 'roadmap:')
    mut('roadmap-admits-sentence-removed', N, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        P0_ADMITS + ' ', '', 1)}), dl), 'roadmap:')
    mut('guard-touched', N, lambda fe, dl: (dict(fe, **{GUARD: fe[GUARD] + ' '}), dict(dl, **{GUARD: 'M'})), 'guard:')
    mut('census-status-promoted', N, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"status": "kernel-only",\n      "manuscript": [],\n      "note": "Outcome',
        '"status": "manuscript-cited",\n      "manuscript": [],\n      "note": "Outcome')}), dl),
        'census:family-disposition')
    mut('census-other-entry-changed', N, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"note": "n"', '"note": "m"')}), dl), 'census:another-entry-changed')
    mut('census-outcome-wrong', N, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        'A31-1-NONUNIQUE.', 'A31-1-UNIQUE.')}), dl), 'census:outcome')
    mut('census-entry-absent', N, lambda fe, dl: (dict(fe, **{CENSUS: fd[CENSUS]}), dl), 'census:family-count-or-place')
    mut('wire-absent', N, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT]}), dl), 'wire:')
    mut('wire-misplaced', N, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT] + WIRE}), dl), 'wire:')
    mut('path-extra', N, lambda fe, dl: (fe, dict(dl, **{'papers/SM.md': 'M'})), 'paths:')
    mut('path-missing-note', N, lambda fe, dl: (fe, dict((k, v) for k, v in dl.items()
                                                        if k != RDIR + 'result.md')), 'paths:')
    return bad, len(ROWS), dmuts, len(muts)


def main():
    if sys.argv[1:] == ['--self-test']:
        bad, rows, dmuts, muts = self_test()
        for b in bad:
            print('  FAIL', b)
        if bad:
            print('controls: self-test FAILED')
            return 1
        print('controls: the two verdict propositions are duals; %d duality mutations fail as required'
              % dmuts)
        print('controls: %d rows hold as frozen, %d mutation controls fail as required' % (rows, muts))
        print('controls: self-test OK')
        return 0
    if len(sys.argv) == 3 and sys.argv[1] == 'check':
        f = cmd_check(sys.argv[2])
        for x in f:
            print('  FAIL', x)
        print('controls: check %s' % ('FAILED' if f else 'OK'))
        return 1 if f else 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main())
