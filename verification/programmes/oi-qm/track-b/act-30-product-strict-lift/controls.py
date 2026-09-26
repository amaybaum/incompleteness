"""Track B act 30 -- the round's own static controls, frozen with the control plane.

Written before F; its blob is frozen in the preregistration beside it, and the execution adds it
with that exact blob. It reads nothing but the repository at D and at the commit under check, and
it certifies nothing on its own: the Lean kernel, the axiom audit and the release gate establish
the mathematics, and the V3 verifier the protocol. What it checks is that the execution carries
the frozen statements, the frozen outcome grammar and the frozen surface edits, and nothing else.

    python3 controls.py --self-test     the mutation controls, on synthetic inputs, and the
                                        agreement of the constants below with the preregistration
    python3 controls.py check <commit>  every control against the tree at <commit>, read from git

Exit 1 on any failure.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

D = '48450428f528fe489d454458e21c9394aef6a02f'
RDIR = 'verification/programmes/oi-qm/track-b/act-30-product-strict-lift/'
MODULE = 'verification/lean-mathlib/OIBridge/ProductStrictLift.lean'
ROOT = 'verification/lean-mathlib/OIBridge.lean'
GUARD = 'verification/lean/edge_rigidity_probe.py'
CENSUS = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
RECEIPT = 'verification/receipts/A30.json'
GUARD_BLOB_D = '8dad60d0aac870fced7deeec44c0dbdfcb3d45de'
GUARD_BLOB_RETIRED = '0475fe3d8c5724a7bf918bf3fd75ae06370cef26'
ROADMAP_BLOB_D = 'f26f7c1c8d275539bccb21d6faa2e882abc6dcf8'

IMPORT = 'import OIBridge.ProductAdmission\n'
WIRE_AFTER = 'import OIBridge.ProductAdmission\n'
WIRE = 'import OIBridge.ProductStrictLift\n'
OPEN = "open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection\n  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted OrbitLawGaps\n  OrbitGeometryIsometries StrictNaturalLift ProductLocusFreedom ProductAdmission\n"

# ---- the four frozen propositions, verbatim
PROPS = {
 "P_S": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),\n    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →\n  ∀ (Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)),\n    (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → RealizableGram (Fin 1 × Fin 1) (Γ 0) (Φ₀ G)) →\n    (∀ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → RealizableGram (Fin 1 × Fin 1) (Γ 0) G' →\n      GramPhaseEquiv G G' → GramPhaseEquiv (Φ₀ G) (Φ₀ G')) →\n    ∃ (Φ₁ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)) (Ψ : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ),\n      (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → GramPhaseEquiv (Φ₁ G) (Φ₀ G))\n      ∧ (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ¬ RealizableGram (Fin 1 × Fin 1) (Γ 0) G → Φ₁ G = Φ₀ G)\n      ∧ (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → RealizableGram (Fin 1 × Fin 1) (Γ 0) (Φ₁ G))\n      ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ 0) ((0 : Fin 1), (0 : Fin 1)) U →\n          FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ₁ (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))\n      ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ 0) ((0 : Fin 1), (0 : Fin 1)) U →\n          AdmissibleDilationAt (Γ 0) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))\n      ∧ StrictNatural ((0 : Fin 1), (0 : Fin 1)) Ψ",
 "P_T": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),\n    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →\n  ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)),\n    (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (f₁ G)) →\n    (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (f₂ G)) →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv G G' → GramPhaseEquiv (f₁ G) (f₁ G')) →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv G G' → GramPhaseEquiv (f₂ G) (f₂ G')) →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv (f₁ G) (f₁ G') → GramPhaseEquiv G G') →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv (f₂ G) (f₂ G') → GramPhaseEquiv G G') →\n    (∀ G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G' →\n      ∃ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (f₁ G) G') →\n    (∀ G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G' →\n      ∃ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (f₂ G) G') →\n  ∀ (Φ₀ Φ₁ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)),\n    (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Γ 0) G → GramPhaseEquiv (Φ₁ G) (Φ₀ G)) →\n    (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ¬ RealizableGram (Fin 1 × Fin 1) (Γ 0) G → Φ₁ G = Φ₀ G) →\n    (EvolvesTotally (Fin 1 × Fin 1) Γ (fun _ : ℕ => Φ₀)\n      ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ (fun _ : ℕ => Φ₀)\n      ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, (fun _ : ℕ => Φ₀) t = Φh)\n      ∧ Reversible (Fin 1 × Fin 1) Γ (fun _ : ℕ => Φ₀)\n      ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n          GramPhaseEquiv G G' → GramPhaseEquiv ((fun _ : ℕ => Φ₀) t G) ((fun _ : ℕ => Φ₀) t G'))\n      ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n          (fun _ => Γ₀) (fun _ => Γ₀) Γ (fun _ : ℕ => Φ₀)\n      ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n          GramPhaseEquiv ((fun _ : ℕ => Φ₀) t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))) →\n    (EvolvesTotally (Fin 1 × Fin 1) Γ (fun _ : ℕ => Φ₁)\n      ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ (fun _ : ℕ => Φ₁)\n      ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, (fun _ : ℕ => Φ₁) t = Φh)\n      ∧ Reversible (Fin 1 × Fin 1) Γ (fun _ : ℕ => Φ₁)\n      ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n          GramPhaseEquiv G G' → GramPhaseEquiv ((fun _ : ℕ => Φ₁) t G) ((fun _ : ℕ => Φ₁) t G'))\n      ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n          (fun _ => Γ₀) (fun _ => Γ₀) Γ (fun _ : ℕ => Φ₁)\n      ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n          GramPhaseEquiv ((fun _ : ℕ => Φ₁) t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2)))",
 "P_N": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),\n    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →\n  ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)),\n    (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (f₁ G)) →\n    (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (f₂ G)) →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv G G' → GramPhaseEquiv (f₁ G) (f₁ G')) →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv G G' → GramPhaseEquiv (f₂ G) (f₂ G')) →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv (f₁ G) (f₁ G') → GramPhaseEquiv G G') →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv (f₂ G) (f₂ G') → GramPhaseEquiv G G') →\n    (∀ G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G' →\n      ∃ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (f₁ G) G') →\n    (∀ G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G' →\n      ∃ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (f₂ G) G') →\n  ∃ Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n    EvolvesTotally (Fin 1 × Fin 1) Γ Φ\n    ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ\n    ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ t = Φh)\n    ∧ Reversible (Fin 1 × Fin 1) Γ Φ\n    ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n        GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))\n    ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n        (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ\n    ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n        GramPhaseEquiv (Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))\n    ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,\n        (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n          FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))\n        ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n          AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))\n        ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)",
 "P_0": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),\n    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →\n  ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)),\n    (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (f₁ G)) →\n    (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (f₂ G)) →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv G G' → GramPhaseEquiv (f₁ G) (f₁ G')) →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv G G' → GramPhaseEquiv (f₂ G) (f₂ G')) →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv (f₁ G) (f₁ G') → GramPhaseEquiv G G') →\n    (∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →\n      GramPhaseEquiv (f₂ G) (f₂ G') → GramPhaseEquiv G G') →\n    (∀ G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G' →\n      ∃ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (f₁ G) G') →\n    (∀ G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G' →\n      ∃ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (f₂ G) G') →\n  ∃ Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n    ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ\n      (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))\n    ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ\n      (fun 𝔾 : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ =>\n        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))\n    ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ\n    ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ\n    ∧ (∃ Φh : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t : ℕ, Φ t = Φh)\n    ∧ Reversible (Fin 1 × Fin 1) Γ Φ\n    ∧ (∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),\n        GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))\n    ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,\n        (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n          FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))\n        ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →\n          AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))\n        ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)\n    ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n        (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ\n    ∧ (∀ (t : ℕ) (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₁ → RealizableGram (Fin 1) Γ₀ G₂ →\n        GramPhaseEquiv (Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))\n          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2))"
}

# ---- the label theorems: (target, label, theorem name, statement form)
LABELS = (
    ('A30-S', 'A30-S-HOLD', 'a30_s_strictify', 'P_S', '+'),
    ('A30-S', 'A30-S-FAILS', 'a30_s_fails', 'P_S', '-'),
    ('A30-T', 'A30-T-HOLD', 'a30_t_transfer', 'P_T', '+'),
    ('A30-T', 'A30-T-FAILS', 'a30_t_fails', 'P_T', '-'),
    ('A30-N', 'A30-N-LIFTS', 'a30_n_lifts', 'P_N', '+'),
    ('A30-N', 'A30-N-NO-LIFT', 'a30_n_no_lift', 'P_N', '-'),
    ('A30-0', 'A30-0-ADMITS', 'a30_0_admits', 'P_0', '+'),
    ('A30-0', 'A30-0-RESTRICTS', 'a30_0_restricts', 'P_0', '-'),
)
UNDECIDED = {'A30-S': 'A30-S-UNDECIDED', 'A30-T': 'A30-T-UNDECIDED',
             'A30-N': 'A30-N-UNDECIDED', 'A30-0': 'A30-0-UNDECIDED'}
# ---- the corollary theorems: name -> (premises, conclusion)
COROLLARIES = {
    'a30_c_lift': (('P_S', 'P_T'), 'P_N'),
    'a30_c_admit': (('P_N',), 'P_0'),
    'a30_c_restrict': (('P_0',), 'P_N'),
}
SHARED = re.compile(r'a30_shared_[A-Za-z0-9_]+\Z')

# ---- the twenty-five rows of the frozen outcome-vector table
_S = ('A30-S-HOLD', 'A30-S-FAILS', 'A30-S-UNDECIDED')
_T = ('A30-T-HOLD', 'A30-T-FAILS', 'A30-T-UNDECIDED')
_N = ('A30-N-LIFTS', 'A30-N-NO-LIFT', 'A30-N-UNDECIDED')
_ZERO = {'A30-N-LIFTS': 'A30-0-ADMITS', 'A30-N-NO-LIFT': 'A30-0-RESTRICTS',
         'A30-N-UNDECIDED': 'A30-0-UNDECIDED'}
ROWS = tuple((s, t, n, _ZERO[n]) for s in _S for t in _T for n in _N
             if not (s == 'A30-S-HOLD' and t == 'A30-T-HOLD' and n != 'A30-N-LIFTS'))
assert len(ROWS) == 25


def row_text(v):
    return ' · '.join('`%s`' % x for x in v)


VECTOR_RE = re.compile(r'A30-S-(?:HOLD|FAILS|UNDECIDED)`? · `?A30-T-(?:HOLD|FAILS|UNDECIDED)`? · '
                       r'`?A30-N-(?:LIFTS|NO-LIFT|UNDECIDED)`? · `?A30-0-(?:ADMITS|RESTRICTS|UNDECIDED)')

# ---- the frozen post-round sentences, one per label
SENTENCES = {
 "A30-S-HOLD": "At the frozen product configuration, every map preserving realizability and descending on\nrealizable tuples is pointwise `GramPhaseEquiv`-equivalent, and equal off realizable tuples, to a\nmap with a strictly natural representative-level lift, at evidence level 2. This is a statement at\nthe exact configuration and says nothing about any other.",
 "A30-S-FAILS": "At the frozen product configuration, an exhibited map preserving realizability and descending on\nrealizable tuples has no pointwise-equivalent replacement with a strictly natural lift, at evidence\nlevel 2. This refutes the strictification and nothing more; it says nothing about twisted lifts.",
 "A30-S-UNDECIDED": "Neither the strictification nor a counterexample was obtained. The step at which the proof stopped\nis named, with what would settle it.",
 "A30-T-HOLD": "At the frozen product configuration, replacing a family by one pointwise `GramPhaseEquiv`-equivalent\non realizable tuples and equal off them keeps every conjunct of eligibility for the same prescribed\npair, at evidence level 2.",
 "A30-T-FAILS": "At the frozen product configuration, an exhibited replacement of that kind loses the named conjunct\nof eligibility, at evidence level 2.",
 "A30-T-UNDECIDED": "Neither the transfer nor a counterexample was obtained. The conjunct at which the proof stopped is\nnamed.",
 "A30-N-LIFTS": "At the frozen product configuration, for every prescribed pair of bijections of the single-carrier\nrealizable class spaces there is a transition family satisfying conjuncts 3 to 7 and factorization\nwith factor families realizing that pair which also satisfies representative-level gauge\nnaturality at act 20's certified strength, at the product carrier, at evidence level 2. **This is\nan existence statement about some such family. It does not disturb act 23's verdict about its own\nformula**, which is a statement that one exact formula admits no lift.",
 "A30-N-NO-LIFT": "At the frozen product configuration, for an exhibited pair of bijections of the single-carrier\nrealizable class spaces, no transition family satisfying conjuncts 3 to 7 and factorization with\nfactor families realizing that pair satisfies representative-level gauge naturality at act 20's\ncertified strength at the product carrier, for any lift and any induced maps, at evidence level 2.\nThis is a statement about that exhibited pair, and it does not say that any other pair is so\nrestricted.",
 "A30-N-UNDECIDED": "Neither a lifting family nor the universal negative was obtained. The obstruction is named, with\nthe family or families tried and what would settle it. A family found to admit no lift is recorded\nas that and is not reported as the universal negative, and the absence of a strict lift is not\nreported as the absence of a twisted one.",
 "A30-0-ADMITS": "At the frozen product configuration, for the ordered decomposition named, every pair of bijections\nof the single-carrier realizable class spaces is the class action of the factor families of a\nsingle transition family satisfying all eight prefix conjuncts and factorization as act 21 froze\nit, at evidence level 2. This is a statement about the exact declarations at the exact\nconfiguration. It does not say that any particular formula carries those conjuncts, does not\ndisturb act 23's verdict about its own formula, and reports nothing about any other configuration\nor decomposition.",
 "A30-0-RESTRICTS": "At the frozen product configuration, for the ordered decomposition named, an exhibited pair of\nbijections of the single-carrier realizable class spaces is the class action of the factor\nfamilies of no transition family satisfying all eight prefix conjuncts and factorization as act 21\nfroze it, at evidence level 2. This is a statement about that exhibited pair, and it does not say\nthat any other pair is restricted.",
 "A30-0-UNDECIDED": "Neither the universal nor a counterexample was obtained. The conjunct that is missing is named,\nwith the step at which the proof stopped and what would settle it."
}

# the clause's body; its heading names the artifact carrying it
CLAUSE = "Act 30 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts\nnone. A law that survives every condition this freeze names is a law that survives **those**\nconditions, at the configuration frozen for it, and it is **not** a finding that it obtains in\nnature, **not** a finding that the programme requires it, and **not** an adoption of it as the\nphysical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about\nthe frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence\nto add one more condition, or to widen one more equivalence, until a plurality becomes a point.\n**No law gains physical status by surviving, no carrier and no principle is adopted as the physical\none, and nothing here derives, recognises or approaches quantum evolution.**"
MENTION = 'THE CLAUSE, carried at this mention'
WATCH = "Conjunct 8 places no constraint on `αL` and `αR` beyond act 20's closure conjuncts. With\n`αL = αR = fun _ => 1` it asks for a lift `Ψ` constant along gauge orbits. By the freeze's reading\n(hand reasoning, not a result), a family that factors exactly through `GramPhaseEquiv` classes on\ndilatable tuples and preserves realizability has such a lift, and every descending family is\npointwise equivalent to one that does. If so, conjunct 8 read with constant maps adds nothing, up to\nlaw equivalence, to conjuncts 4 and 7. **This round establishes none of that**, rests no verdict on\nit, and changes no declaration. It is recorded so that a later round reading conjunct 8 as a\nrestriction knows the reading exists."

# ---- the P0 cell
P0_PFR = "At the product configuration, whether factorization restricts which pair of local class bijections can occur is undecided, with the obstruction named."
P0_PRA = "At the product configuration, whether the ladder's conditions through factorization admit every pair of local class bijections is undecided, with the conjunct that is missing named."
P0_STANDING = "`P0`'s threading part is untouched, no carrier is adopted as the physical one, no surviving law is adopted as the physical one, and nothing here names, endorses or excludes a selection principle."
P0_ADMITS = "At the product configuration, the ladder's conditions through factorization admit every pair of local class bijections: each such pair is the class action of the factor families of a single law carrying all of them, so those conditions do not select among local behaviours."
P0_RESTRICTS = "At the product configuration, the ladder's conditions through factorization do not admit every pair of local class bijections: for an exhibited pair, no law carrying all of them has factor families realizing it, the obstruction being representative-level gauge naturality at the product carrier."

# ---- the guard-retirement ledger: exact splices of the guard at D, applied on a decided A30-0
LEDGER = [
 {
  "id": "pfr-road-standing",
  "old_sha256": "03e8d3b67661e06f9118b34feef2f9aee7a83a16a6d8bfa32f54cff7c49f4f2d",
  "old": "_PFR_ROAD_STANDING = \"`P0`'s threading part is untouched, no carrier is adopted as the physical one, no surviving law is adopted as the physical one, and nothing here names, endorses or excludes a selection principle.\"\n",
  "new": "",
  "new_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "reason": "R7-PFR's ROADMAP standing-clause constant, read only by its ROADMAP leg"
 },
 {
  "id": "pfr-p0",
  "old_sha256": "9d310604c24ec728b826debf548a7417c3e6032f1067de77e1c0dca9910a4719",
  "old": "_PFR_P0 = 'At the product configuration, whether factorization restricts which pair of local class bijections can occur is undecided, with the obstruction named.'\n",
  "new": "",
  "new_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "reason": "R7-PFR's frozen P0 sentence constant, read only by its ROADMAP leg"
 },
 {
  "id": "pfr-p0-cell-and-road-ok",
  "old_sha256": "168273af4647dfc1eb88fc1e30503e1ef0e8fc838f937e9676a4aef926a4fac1",
  "old": "def _pfr_p0_cell(road):\n    \"\"\"The ACTUAL P0 status cell -- the fourth field of the one row whose first field is P0.\n\n    Content is checked inside this cell, never against the document, so a frozen sentence moved\n    out of P0 into an appendix is not accepted for sitting somewhere in the file.\n    \"\"\"\n    rows = [l for l in road.split('\\n') if l.strip().startswith('| **P0** |')]\n    if len(rows) != 1:\n        return None\n    cells = rows[0].strip().split('|')[1:-1]\n    return cells[3] if len(cells) == 5 else None\n\n\ndef _pfr_road_ok(road):\n    \"\"\"THE PREDICATE THAT GATES act 28's ROADMAP entry, read as a BOUNDED ENTRY.\n\n    Act 28's entry is its unique frozen sentence, inside the ACTUAL P0 cell, after act 27's anchor,\n    with the complete standing clause following it. The predicate validates that entry and counts\n    nothing beyond it: a successor round's entry, which necessarily reuses the standing clause, is\n    outside the bound and is neither counted nor accepted in its place.\n    \"\"\"\n    cell = _pfr_p0_cell(road)\n    if cell is None:\n        return False\n    c = _pfr_n(cell)\n    p0 = _pfr_n(_PFR_P0)\n    if c.count(p0) != 1:\n        return False\n    anchor = _pfr_n('with its selecting power left open.')\n    if anchor not in c or c.index(p0) < c.index(anchor):\n        return False\n    # this round's standing clause is not merely present: it follows the frozen sentence it scopes.\n    if not c[c.index(p0) + len(p0):].lstrip().startswith(_pfr_n(_PFR_ROAD_STANDING)):\n        return False\n    n = _pfr_n(road)\n    return n.count(p0) == 1\n\n\n",
  "new": "",
  "new_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "reason": "the P0-cell reader (read only by R7-PFR's and R7-PRA's ROADMAP legs) and R7-PFR's ROADMAP gating predicate"
 },
 {
  "id": "pfr-road-read",
  "old_sha256": "259a9c3b5c444b37900d69162460b2c938bf93887f6b7cb9b888221f287aa479",
  "old": "_PFRROAD = _bb_read('ROADMAP.md').decode('utf-8')\n",
  "new": "",
  "new_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "reason": "R7-PFR's read of verification/ROADMAP.md"
 },
 {
  "id": "pfr-road-leg",
  "old_sha256": "784284350863547227b87cd0bb2c4539717a69b221ff90b745190710d13970e7",
  "old": "_pfr_checks['roadmap'] = _pfr_road_ok(_PFRROAD)\nfor _nm, _fn in (\n        ('p0-deleted', lambda r: r.replace(_PFR_P0, '', 1)),\n        ('p0-duplicated', lambda r: r + '\\n' + _PFR_P0 + '\\n'),\n        ('standing-clause-removed', lambda r: r.replace(_PFR_ROAD_STANDING, '', 1)),\n        ('standing-clause-detached',\n         lambda r: r.replace(_PFR_P0 + ' ' + _PFR_ROAD_STANDING,\n                             _PFR_P0 + ' Something else entirely. ' + _PFR_ROAD_STANDING, 1)),\n        ('p0-before-act27',\n         lambda r: _PFR_P0 + ' ' + _PFR_ROAD_STANDING + '\\n'\n                   + r.replace(_PFR_P0 + ' ' + _PFR_ROAD_STANDING, '', 1)),\n        ('p0-block-moved-out-of-the-cell',\n         lambda r: r.replace(' ' + _PFR_P0 + ' ' + _PFR_ROAD_STANDING, '', 1)\n                   + '\\n\\n## Appendix\\n\\n' + _PFR_P0 + ' ' + _PFR_ROAD_STANDING + '\\n'),\n        ('p0-row-removed',\n         lambda r: '\\n'.join(l for l in r.split('\\n')\n                             if not l.strip().startswith('| **P0** |')))):\n    _pfr_checks['road-mut:' + _nm] = not _pfr_road_ok(_fn(_PFRROAD))\n    _pfr_mutations += 1\n\n",
  "new": "",
  "new_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "reason": "R7-PFR's ROADMAP check entry and its seven road-mut mutation controls"
 },
 {
  "id": "pfr-description",
  "old_sha256": "95d909f415335263827d2f80bd4c4800088dc8db6e3cdfa9d7ea6428744f4e2c",
  "old": "check('R7-PFR', not _pfr_bad,\n      'Act 28: the DECODED census entry and the ROADMAP cell each read through ONE gating '\n      'predicate that every mutation is passed through. Each frozen requirement is pinned to its '\n      'COMPLETE content, not a heading: ten census records and the census clause in full. '\n      'Mutations: a module that gains a definition, each record deleted, the census clause '\n      'truncated or duplicated, the census note re-escaped or its entry removed, and the ROADMAP '\n      'standing clause removed or detached. PLACEMENT AND COUNT, not only presence: exactly one '\n      'mention of the census clause with that mention opening the COMPLETE clause, and the frozen '\n      'sentence read out of the ACTUAL P0 cell rather than the document -- with the census clause '\n      'duplicated or given an incomplete second copy, and the P0 block moved to an appendix or its '\n      'row removed, all failing closed. Twelve pinned statements each mutation-tested, the frozen '\n      'configuration and act 21 predicate verbatim.')\n",
  "new": "check('R7-PFR', not _pfr_bad,\n      'Act 28: the DECODED census entry read through ONE gating predicate that every '\n      'mutation is passed through. Each frozen requirement is pinned to its COMPLETE content, '\n      'not a heading: ten census records and the census clause in full. Mutations: a module '\n      'that gains a definition, each record deleted, the census clause truncated or '\n      'duplicated, and the census note re-escaped or its entry removed. PLACEMENT AND COUNT, '\n      'not only presence: exactly one mention of the census clause with that mention opening '\n      'the COMPLETE clause, with the census clause duplicated or given an incomplete second '\n      'copy failing closed. Twelve pinned statements each mutation-tested, the frozen '\n      'configuration and act 21 predicate verbatim.')\n",
  "new_sha256": "d37022ced1c9c5f47a997bfd31250c20bf2a5ef8818cfc6e5f57d3d20c583c83",
  "reason": "R7-PFR's check description, less its statements that the ROADMAP cell is read"
 },
 {
  "id": "pra-road-constants",
  "old_sha256": "677dc5e71329bdc5431f0d0d910bc8ed6c4d8e6782ee543fc513712d033af964",
  "old": "_PRA_P0 = \"At the product configuration, whether the ladder's conditions through factorization admit every pair of local class bijections is undecided, with the conjunct that is missing named.\"\n_PRA_ROAD_STANDING = \"`P0`'s threading part is untouched, no carrier is adopted as the physical one, no surviving law is adopted as the physical one, and nothing here names, endorses or excludes a selection principle.\"\n_PRA_ROAD_ANCHOR = 'with the obstruction named.'\n",
  "new": "",
  "new_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "reason": "R7-PRA's frozen P0 sentence, standing-clause and anchor constants, read only by its ROADMAP leg"
 },
 {
  "id": "pra-road-ok",
  "old_sha256": "6ae97784f6c16ae28550c80868207be7a7dc2c27e7ff76efa9be0fb8e037f301",
  "old": "def _pra_road_ok(road):\n    \"\"\"THE PREDICATE THAT GATES act 29's ROADMAP entry, read as a BOUNDED ENTRY out of the ACTUAL cell.\"\"\"\n    cell = _pfr_p0_cell(road)\n    if cell is None:\n        return False\n    c = _pra_n(cell)\n    p0 = _pra_n(_PRA_P0)\n    if c.count(p0) != 1:\n        return False\n    anchor = _pra_n(_PRA_ROAD_ANCHOR)\n    if anchor not in c or c.index(p0) < c.index(anchor):\n        return False\n    # THE BOUNDED ENTRY: the standing clause attached immediately and complete, once. Nothing\n    # beyond the entry is counted, so a successor's entry -- which reuses the clause -- is\n    # outside what this contract reads, and act 28's document-wide count is not repeated here.\n    if c.count(p0 + ' ' + _pra_n(_PRA_ROAD_STANDING)) != 1:\n        return False\n    return _pra_n(road).count(p0) == 1\n\n\n",
  "new": "",
  "new_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "reason": "R7-PRA's ROADMAP gating predicate"
 },
 {
  "id": "pra-road-read",
  "old_sha256": "531b9485cfe1b7d0f15bd31805b12e2aa771b8a797799f2e88b67f09c4484d26",
  "old": "_PRAROAD = _bb_read('ROADMAP.md').decode('utf-8')\n",
  "new": "",
  "new_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "reason": "R7-PRA's read of verification/ROADMAP.md"
 },
 {
  "id": "pra-road-leg",
  "old_sha256": "60f9fe69fd72f5b2f36805da80e3091761a29841293655ed359f3b009ef23725",
  "old": "_pra_checks['roadmap'] = _pra_road_ok(_PRAROAD)\nfor _nm, _fn in (\n        ('p0-deleted', lambda r: r.replace(_PRA_P0, '', 1)),\n        ('p0-duplicated', lambda r: r + '\\n' + _PRA_P0 + '\\n'),\n        ('standing-clause-removed', lambda r: r.replace(\n            _PRA_P0 + ' ' + _PRA_ROAD_STANDING, _PRA_P0, 1)),\n        ('standing-clause-detached',\n         lambda r: r.replace(_PRA_P0 + ' ' + _PRA_ROAD_STANDING,\n                             _PRA_P0 + ' Something else entirely. ' + _PRA_ROAD_STANDING, 1)),\n        ('p0-before-act28',\n         lambda r: r.replace(' ' + _PRA_P0 + ' ' + _PRA_ROAD_STANDING, '', 1).replace(\n             _PRA_ROAD_ANCHOR, _PRA_P0 + ' ' + _PRA_ROAD_STANDING + ' ' + _PRA_ROAD_ANCHOR, 1)),\n        ('p0-block-moved-out-of-the-cell',\n         lambda r: r.replace(' ' + _PRA_P0 + ' ' + _PRA_ROAD_STANDING, '', 1)\n                   + '\\n\\n## Appendix\\n\\n' + _PRA_P0 + ' ' + _PRA_ROAD_STANDING + '\\n'),\n        ('standing-clause-truncated', lambda r: r.replace(\n            _PRA_P0 + ' ' + _PRA_ROAD_STANDING, _PRA_P0 + ' ' + _PRA_ROAD_STANDING[:60], 1)),\n        ('p0-duplicated-in-cell', lambda r: r.replace(\n            _PRA_P0 + ' ' + _PRA_ROAD_STANDING,\n            _PRA_P0 + ' ' + _PRA_ROAD_STANDING + ' ' + _PRA_P0 + ' ' + _PRA_ROAD_STANDING, 1)),\n        ('p0-row-removed',\n         lambda r: '\\n'.join(l for l in r.split('\\n')\n                             if not l.strip().startswith('| **P0** |')))):\n    _pra_checks['road-mut:' + _nm] = not _pra_road_ok(_fn(_PRAROAD))\n    _pra_mutations += 1\n# POSITIVE CONTROL: a successor round's entry after this one, reusing the standing clause, is\n# tolerated -- the defect RD2 records in act 28's contract is not repeated in this one.\n_pra_checks['road-successor-tolerated'] = _pra_road_ok(_PRAROAD.replace(\n    _PRA_P0 + ' ' + _PRA_ROAD_STANDING,\n    _PRA_P0 + ' ' + _PRA_ROAD_STANDING + ' A successor sentence. ' + _PRA_ROAD_STANDING, 1))\n_pra_mutations += 1\n\n",
  "new": "",
  "new_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "reason": "R7-PRA's ROADMAP check entry, its nine road-mut mutation controls and its road-successor-tolerated positive control"
 },
 {
  "id": "pra-description",
  "old_sha256": "18985af9c22a7632dd230828bc781737903532e9a99b359d5a4d548667079b0d",
  "old": "check('R7-PRA', not _pra_bad,\n      'Act 29: the DECODED census entry and the ROADMAP cell each read through ONE gating '\n      'predicate that every mutation is passed through. Each frozen requirement is pinned to its '\n      'COMPLETE content, the census prose pinned WHOLE and not as fragments. EVERY complete '\n      'outcome-vector occurrence is counted, valid or not, before membership and the corollaries '\n      'are asked, so an impossible vector appended beside the correct one, or the correct one '\n      \"duplicated, fails in the census. The ROADMAP contract reads this round's BOUNDED ENTRY and \"\n      'tolerates a successor, with a positive control proving it. Each frozen requirement is '\n      'pinned to its COMPLETE content, not a heading: twelve census records, plus the census '\n      \"clause in full. THE GATES AND THE TWO ASSEMBLY COROLLARIES ARE READ OFF THE ARTIFACT'S BARE \"\n      'OUTCOME VECTOR: the vector must be one of the eleven admissible rows, A29-0-ADMITS must '\n      'accompany A29-P-HOLD with A29-N-LIFTS and no other combination, and A29-N-NO-LIFT must '\n      'carry A29-0-RESTRICTS -- so an off-table row and a corollary-contradicting row both fail '\n      'closed. A29-P is checked for ITS SHAPE AND SCOPE: the five hypothesis conjuncts and the two '\n      'conclusions present, and no FactorizesOnProduct hypothesis and no prescribed pair in the '\n      'statement. The UNDECIDED and NOT-EXECUTED labels forbid a theorem named for their targets. '\n      'Mutations: a module that gains a definition or a gated name, each record deleted, the '\n      'census clause truncated or duplicated or given an incomplete second copy, the census note '\n      're-escaped or its entry removed, and the ROADMAP standing clause removed or detached. '\n      'PLACEMENT AND COUNT, not only presence: exactly one mention of the census clause with that '\n      'mention opening the COMPLETE clause, and the frozen sentence read out of the ACTUAL P0 cell '\n      \"after act 28's. Six pinned statements each mutation-tested.\")\n",
  "new": "check('R7-PRA', not _pra_bad,\n      'Act 29: the DECODED census entry read through ONE gating '\n      'predicate that every mutation is passed through. Each frozen requirement is pinned to its '\n      'COMPLETE content, the census prose pinned WHOLE and not as fragments. EVERY complete '\n      'outcome-vector occurrence is counted, valid or not, before membership and the corollaries '\n      'are asked, so an impossible vector appended beside the correct one, or the correct one '\n      'duplicated, fails in the census. Each frozen requirement is '\n      'pinned to its COMPLETE content, not a heading: twelve census records, plus the census '\n      \"clause in full. THE GATES AND THE TWO ASSEMBLY COROLLARIES ARE READ OFF THE ARTIFACT'S BARE \"\n      'OUTCOME VECTOR: the vector must be one of the eleven admissible rows, A29-0-ADMITS must '\n      'accompany A29-P-HOLD with A29-N-LIFTS and no other combination, and A29-N-NO-LIFT must '\n      'carry A29-0-RESTRICTS -- so an off-table row and a corollary-contradicting row both fail '\n      'closed. A29-P is checked for ITS SHAPE AND SCOPE: the five hypothesis conjuncts and the two '\n      'conclusions present, and no FactorizesOnProduct hypothesis and no prescribed pair in the '\n      'statement. The UNDECIDED and NOT-EXECUTED labels forbid a theorem named for their targets. '\n      'Mutations: a module that gains a definition or a gated name, each record deleted, the '\n      'census clause truncated or duplicated or given an incomplete second copy, the census note '\n      're-escaped or its entry removed. '\n      'PLACEMENT AND COUNT, not only presence: exactly one mention of the census clause with that '\n      'mention opening the COMPLETE clause. Six pinned statements each mutation-tested.')\n",
  "new_sha256": "88214942affb2f072410e1a73aaeb0250a4616b1cdd1cae4a6d3187045d32be8",
  "reason": "R7-PRA's check description, less its statements that the ROADMAP cell is read"
 }
]

CENSUS_MODULES = ['ProductStrictLift']

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
    """Normalization for prose that may sit in a blockquote."""
    return ' '.join(re.sub(r'(?m)^[ \t]*>[ \t]?', '', t).split())


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


def theorems(code):
    """name -> statement text (between the name and the first ':='), from comment-free source."""
    out = {}
    for m in re.finditer(r'(?m)^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?(?:private[ \t]+|protected[ \t]+)?'
                         r'(?:theorem|lemma)[ \t]+(\S+)', code):
        nm = m.group(1)
        rest = code[m.end():]
        j = rest.find(':=')
        st = rest if j < 0 else rest[:j]
        if nm in out:
            out[nm] = None
        else:
            out[nm] = st
    return out


def target_statement(key, sign):
    return norm(': ' + (PROPS[key] if sign == '+' else '¬ (' + PROPS[key] + ')'))


def corollary_statement(name):
    prem, concl = COROLLARIES[name]
    return norm(': ' + ' → '.join('(' + PROPS[p] + ')' for p in prem + (concl,)))


# ---- the module -------------------------------------------------------------------------------
def module_labels(src):
    """Check the module and read the labels it earns. Returns (vector or None, failures)."""
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
    if 'namespace OIBridge\nnamespace ProductStrictLift\n' not in code or \
            not code.rstrip().endswith('end ProductStrictLift\nend OIBridge'):
        f.append('module:namespace')
    th = theorems(code)
    if any(v is None for v in th.values()):
        f.append('module:theorem-declared-twice')
    if opens and th:
        first = min(m.start() for m in re.finditer(r'(?m)^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?'
                                                   r'(?:private[ \t]+|protected[ \t]+)?'
                                                   r'(?:theorem|lemma)\b', code))
        if first < opens[0]:
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
    names = {x[2] for x in LABELS} | set(COROLLARIES)
    for nm in th:
        if nm not in names and not SHARED.match(nm):
            f.append('module:theorem-name-outside-the-frozen-set:' + nm)
    earned = {}
    for tgt, lab, nm, key, sign in LABELS:
        if nm in th and th[nm] is not None:
            if norm(th[nm]) != target_statement(key, sign):
                f.append('module:statement-not-frozen:' + nm)
            earned.setdefault(tgt, []).append(lab)
    vec = []
    for tgt in ('A30-S', 'A30-T', 'A30-N', 'A30-0'):
        ls = earned.get(tgt, [])
        if len(ls) > 1:
            f.append('module:both-labels:' + tgt)
            return None, f
        vec.append(ls[0] if ls else UNDECIDED[tgt])
    vec = tuple(vec)
    for nm in COROLLARIES:
        if nm in th and th[nm] is not None and norm(th[nm]) != corollary_statement(nm):
            f.append('module:statement-not-frozen:' + nm)
    for nm in ('a30_c_admit', 'a30_c_restrict'):
        if nm not in th:
            f.append('module:required-corollary-absent:' + nm)
    if vec[0] == 'A30-S-HOLD' and vec[1] == 'A30-T-HOLD' and 'a30_c_lift' not in th:
        f.append('module:required-corollary-absent:a30_c_lift')
    if vec not in ROWS:
        f.append('module:vector-off-table:' + ' · '.join(vec))
    return vec, f


# ---- the result note ---------------------------------------------------------------------------
def note_ok(note, vec):
    f = []
    found = VECTOR_RE.findall(note)
    if len(found) != 1:
        f.append('note:vector-occurrences:%d' % len(found))
    if note.count(row_text(vec)) != 1:
        f.append('note:vector-row-not-carried-once')
    q = qnorm(note)
    for lab in vec:
        if q.count(qnorm(SENTENCES[lab])) != 1:
            f.append('note:frozen-sentence:' + lab)
    for lab in SENTENCES:
        if lab not in vec and qnorm(SENTENCES[lab]) in q:
            f.append('note:sentence-of-a-label-not-earned:' + lab)
    body = qnorm(CLAUSE)
    if note.count(MENTION) != 1 or q.count(body) != 1 or \
            not 0 <= q.index(body) - q.index(MENTION) <= 80:
        f.append('note:the-clause')
    if q.count(qnorm(WATCH)) != 1:
        f.append('note:assumption-watch')
    if vec[3] != 'A30-0-UNDECIDED':
        for e in LEDGER:
            if '`%s`' % e['id'] not in note:
                f.append('note:replaced-leg-not-listed:' + e['id'])
    return f


# ---- the surfaces ------------------------------------------------------------------------------
def expected_roadmap(road_d, vec):
    if vec[3] == 'A30-0-UNDECIDED':
        return road_d
    old = ' ' + P0_PFR + ' ' + P0_STANDING + ' ' + P0_PRA + ' ' + P0_STANDING + ' |'
    new = ' ' + (P0_ADMITS if vec[3] == 'A30-0-ADMITS' else P0_RESTRICTS) + ' ' + P0_STANDING + ' |'
    if road_d.count(old) != 1:
        return None
    return road_d.replace(old, new, 1)


def retired_guard(guard_d):
    out = guard_d
    for e in LEDGER:
        if hashlib.sha256(e['old'].encode()).hexdigest() != e['old_sha256'] or \
                hashlib.sha256(e['new'].encode()).hexdigest() != e['new_sha256'] or \
                guard_d.count(e['old']) != 1 or out.count(e['old']) != 1:
            return None
        out = out.replace(e['old'], e['new'], 1)
    return out


def expected_guard(guard_d, vec):
    return guard_d if vec[3] == 'A30-0-UNDECIDED' else retired_guard(guard_d)


def census_ok(cen_d, cen_e, vec):
    f = []
    try:
        d, e = json.loads(cen_d), json.loads(cen_e)
    except ValueError:
        return ['census:not-json']
    if cen_e != json.dumps(e, indent=2, ensure_ascii=False) + '\n':
        f.append('census:not-in-the-registry-format')
    fams = e.get('families', [])
    mine = [x for x in fams if 'ProductStrictLift' in x.get('modules', [])]
    if len(mine) != 1 or fams[-1:] != mine:
        return f + ['census:family-count-or-place']
    m = mine[0]
    if m.get('modules') != CENSUS_MODULES or m.get('status') != 'kernel-only' or \
            m.get('manuscript') != []:
        f.append('census:family-disposition')
    note = m.get('note', '')
    bare = ' · '.join(vec)
    if note.count(bare) != 1 or len(VECTOR_RE.findall(note)) != 1:
        f.append('census:vector')
    rest = dict(e, families=fams[:-1])
    if rest != d:
        f.append('census:another-entry-changed')
    return f


def wire_ok(root_d, root_e):
    if root_d.count(WIRE_AFTER) != 1:
        return ['wire:anchor']
    return [] if root_e == root_d.replace(WIRE_AFTER, WIRE_AFTER + WIRE, 1) else ['wire:root']


def expected_paths(vec):
    p = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
         MODULE: 'A', ROOT: 'M', CENSUS: 'M'}
    if vec[3] != 'A30-0-UNDECIDED':
        p[GUARD] = 'M'
        p[ROADMAP] = 'M'
    return p


def check_all(files_d, files_e, delta, vec_expected=None):
    """files_*: path -> text. delta: path -> status letter, D to the commit under check."""
    vec, f = module_labels(files_e.get(MODULE, ''))
    if vec is None:
        return f
    f += note_ok(files_e.get(RDIR + 'result.md', ''), vec)
    road = expected_roadmap(files_d[ROADMAP], vec)
    if road is None or files_e.get(ROADMAP) != road:
        f.append('roadmap:not-as-frozen-for-the-case')
    g = expected_guard(files_d[GUARD], vec)
    if g is None or files_e.get(GUARD) != g:
        f.append('guard:not-as-frozen-for-the-case')
    f += census_ok(files_d[CENSUS], files_e.get(CENSUS, ''), vec)
    f += wire_ok(files_d[ROOT], files_e.get(ROOT, ''))
    if delta != expected_paths(vec):
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
        try:
            fd[p] = git('show', '%s:%s' % (D, p)).decode('utf-8')
        except subprocess.CalledProcessError:
            pass
        try:
            fe[p] = git('show', '%s:%s' % (commit, p)).decode('utf-8')
        except subprocess.CalledProcessError:
            pass
    f = []
    if blob_id(fd[GUARD]) != GUARD_BLOB_D or blob_id(fd[ROADMAP]) != ROADMAP_BLOB_D:
        f.append('base:D-is-not-the-frozen-base')
    rg = retired_guard(fd[GUARD])
    if rg is None or blob_id(rg) != GUARD_BLOB_RETIRED:
        f.append('ledger:does-not-reproduce-the-frozen-retired-guard')
    delta = {}
    for ln in git('diff', '--no-renames', '--name-status', D, commit).decode().splitlines():
        st, p = ln.split('\t', 1)
        delta[p] = st
    f += check_all(fd, fe, delta)
    vec, _ = module_labels(fe.get(MODULE, ''))
    print('controls: vector read off the module:', ' · '.join(vec) if vec else '(none)')
    print('controls: %d path(s) changed from D' % len(delta))
    return f


# ---- the self-test -----------------------------------------------------------------------------
def _module(vec, extra='', drop=(), stmt=None):
    lines = [IMPORT, '/-! synthetic -/\n', 'namespace OIBridge\nnamespace ProductStrictLift\n\n',
             OPEN, '\n', 'theorem a30_shared_x : True := trivial\n#print axioms a30_shared_x\n\n']
    for tgt, lab, nm, key, sign in LABELS:
        if lab in vec and nm not in drop:
            s = (stmt or {}).get(nm, PROPS[key] if sign == '+' else '¬ (' + PROPS[key] + ')')
            lines.append('theorem %s :\n    %s := by\n  exact test\n#print axioms %s\n\n' % (nm, s, nm))
    for nm, (prem, concl) in COROLLARIES.items():
        if nm in drop:
            continue
        s = ' → '.join('(' + PROPS[p] + ')' for p in prem + (concl,))
        lines.append('theorem %s :\n    %s := by\n  exact test\n#print axioms %s\n\n' % (nm, s, nm))
    lines.append(extra)
    lines.append('end ProductStrictLift\nend OIBridge\n')
    return ''.join(lines)


def _note(vec):
    parts = ['# result\n\n| vector |\n|---|\n| ' + row_text(vec) + ' |\n\n']
    for lab in vec:
        parts.append('### `%s`\n\n> %s\n\n' % (lab, SENTENCES[lab]))
    parts.append('> **' + MENTION + ' — the result note.**\n' + '\n'.join('> ' + l for l in CLAUSE.split('\n')) + '\n\n' + WATCH + '\n\n')
    if vec[3] != 'A30-0-UNDECIDED':
        parts.append(' '.join('`%s`' % e['id'] for e in LEDGER) + '\n')
    return ''.join(parts)


def _synthetic_d():
    guard = '# guard\n' + ''.join('\n#%d\n%s\n' % (i, e['old']) for i, e in enumerate(LEDGER))
    road = ('| **P0** | q | x | a sentence. ' + P0_PFR + ' ' + P0_STANDING + ' ' + P0_PRA + ' '
            + P0_STANDING + ' | y |\n')
    cen = json.dumps({'families': [{'name': 'x', 'modules': ['X'], 'status': 'kernel-only',
                                    'manuscript': [], 'note': 'n'}]},
                     indent=2, ensure_ascii=False) + '\n'
    root = 'import A\n' + WIRE_AFTER + 'import B\n'
    return {GUARD: guard, ROADMAP: road, CENSUS: cen, ROOT: root}


def _synthetic_e(fd, vec):
    fe = {MODULE: _module(vec), RDIR + 'result.md': _note(vec)}
    fe[ROADMAP] = expected_roadmap(fd[ROADMAP], vec)
    fe[GUARD] = expected_guard(fd[GUARD], vec)
    c = json.loads(fd[CENSUS])
    c['families'].append({'name': 'act 30', 'modules': ['ProductStrictLift'],
                          'status': 'kernel-only', 'manuscript': [],
                          'note': 'Outcome vector: ' + ' · '.join(vec) + '.'})
    fe[CENSUS] = json.dumps(c, indent=2, ensure_ascii=False) + '\n'
    fe[ROOT] = fd[ROOT].replace(WIRE_AFTER, WIRE_AFTER + WIRE, 1)
    return fe, expected_paths(vec)


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
            if n.count(norm(v)) < 1:
                bad.append('agreement: proposition %s not in the preregistration' % k)
        for k, v in SENTENCES.items():
            if qnorm(v) not in q:
                bad.append('agreement: sentence %s not in the preregistration' % k)
        for k, v in (('clause', CLAUSE), ('watch', WATCH), ('admits', P0_ADMITS),
                     ('restricts', P0_RESTRICTS), ('pfr', P0_PFR), ('pra', P0_PRA),
                     ('standing', P0_STANDING)):
            if qnorm(v) not in q:
                bad.append('agreement: %s not in the preregistration' % k)
        for e in LEDGER:
            if '`%s`' % e['id'] not in text or e['old_sha256'] not in text or \
                    e['new_sha256'] not in text:
                bad.append('agreement: ledger entry %s not in the preregistration' % e['id'])
        for b in (GUARD_BLOB_RETIRED, GUARD_BLOB_D, ROADMAP_BLOB_D):
            if b not in text:
                bad.append('agreement: blob %s not in the preregistration' % b)

    for a, x in SENTENCES.items():
        for b, y in SENTENCES.items():
            if a != b and qnorm(x) in qnorm(y):
                bad.append('distinctness: the sentence of %s lies inside that of %s' % (a, b))
    fd = _synthetic_d()
    # every row holds when the execution is as frozen
    for vec in ROWS:
        fe, delta = _synthetic_e(fd, vec)
        r = check_all(fd, fe, delta)
        if r:
            bad.append('positive %s: %s' % (' · '.join(vec), r))
    base = ('A30-S-HOLD', 'A30-T-HOLD', 'A30-N-LIFTS', 'A30-0-ADMITS')
    und = ('A30-S-UNDECIDED', 'A30-T-UNDECIDED', 'A30-N-UNDECIDED', 'A30-0-UNDECIDED')
    neg = ('A30-S-HOLD', 'A30-T-FAILS', 'A30-N-NO-LIFT', 'A30-0-RESTRICTS')
    muts = []

    def mut(name, vec, fn, want):
        fe, delta = _synthetic_e(fd, vec)
        fe, delta = fn(dict(fe), dict(delta))
        r = check_all(fd, fe, delta)
        muts.append(name)
        if not any(x.startswith(want) for x in r):
            bad.append('mutation %s: expected %s, got %s' % (name, want, r))

    P = PROPS
    def modstmt(nm, s):
        return lambda fe, dl: (dict(fe, **{MODULE: _module(base, stmt={nm: s})}), dl)
    mut('definition-added', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'end ProductStrictLift', 'def zz := 1\nend ProductStrictLift')}), dl), 'module:forbidden-command')
    mut('private-noncomputable-def', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'end ProductStrictLift', 'private noncomputable def zz := 1\nend ProductStrictLift')}), dl),
        'module:forbidden-command')
    mut('variable-added', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a30_shared_x', '\nvariable (h : False)\ntheorem a30_shared_x')}), dl),
        'module:forbidden-command')
    mut('include-added', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a30_shared_x', '\ninclude h\ntheorem a30_shared_x')}), dl),
        'module:forbidden-command')
    mut('second-open', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a30_shared_x', '\nopen Foo\ntheorem a30_shared_x')}), dl), 'module:open')
    mut('open-in', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a30_n_lifts', '\nopen Foo in\ntheorem a30_n_lifts')}), dl), 'module:open')
    mut('open-altered', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'ProductAdmission\n\n', 'ProductAdmission Foo\n\n', 1)}), dl), 'module:open')
    mut('second-import', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '/-! synthetic -/', 'import Mathlib\n/-! synthetic -/')}), dl), 'module:forbidden-command')
    mut('sorry', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'exact test', 'sorry', 1)}), dl), 'module:forbidden-token')
    mut('print-axioms-dropped', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '#print axioms a30_n_lifts\n', '')}), dl), 'module:no-print-axioms')
    mut('stray-theorem-name', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'end ProductStrictLift', 'theorem a30_n_lifts_strict : True := trivial\n'
        '#print axioms a30_n_lifts_strict\nend ProductStrictLift')}), dl),
        'module:theorem-name-outside')
    mut('n-strict-instead-of-twisted', base,
        modstmt('a30_n_lifts', P['P_N'].replace('TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ',
                                                'StrictNatural ((0 : Fin 1), (0 : Fin 1)) Ψ')),
        'module:statement-not-frozen:a30_n_lifts')
    mut('0-two-existentials', base,
        modstmt('a30_0_admits', P['P_0'].replace('    ∧ (∀ t : ℕ, ∃ Ψ', '    ∧ (∃ Φ\' : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), True) ∧ (∀ t : ℕ, ∃ Ψ', 1)),
        'module:statement-not-frozen:a30_0_admits')
    mut('s-off-realizable-clause-dropped', base,
        modstmt('a30_s_strictify', P['P_S'].replace(
            '(∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ¬ RealizableGram (Fin 1 × Fin 1) (Γ 0) G → Φ₁ G = Φ₀ G)',
            'True')), 'module:statement-not-frozen:a30_s_strictify')
    mut('s-binder-added', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'theorem a30_s_strictify :', 'theorem a30_s_strictify (h : False) :')}), dl),
        'module:statement-not-frozen:a30_s_strictify')
    mut('t-configuration-changed', base,
        modstmt('a30_t_transfer', P['P_T'].replace('(1 / 4 : ℝ)', '(1 / 2 : ℝ)')),
        'module:statement-not-frozen:a30_t_transfer')
    mut('negative-not-negated', neg, lambda fe, dl: (dict(fe, **{MODULE: _module(
        neg, stmt={'a30_n_no_lift': P['P_N']})}), dl), 'module:statement-not-frozen:a30_n_no_lift')
    mut('both-labels', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'end ProductStrictLift', 'theorem a30_n_no_lift :\n    ¬ (' + P['P_N'] + ') := by\n  exact test\n'
        '#print axioms a30_n_no_lift\nend ProductStrictLift')}), dl), 'module:both-labels')
    mut('corollary-admit-absent', und, lambda fe, dl: (dict(fe, **{MODULE: _module(
        und, drop=('a30_c_admit',))}), dl), 'module:required-corollary-absent:a30_c_admit')
    mut('corollary-restrict-absent', und, lambda fe, dl: (dict(fe, **{MODULE: _module(
        und, drop=('a30_c_restrict',))}), dl), 'module:required-corollary-absent:a30_c_restrict')
    mut('corollary-lift-absent-when-reached', base, lambda fe, dl: (dict(fe, **{MODULE: _module(
        base, drop=('a30_c_lift',))}), dl), 'module:required-corollary-absent:a30_c_lift')
    mut('corollary-lift-altered', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'theorem a30_c_lift :\n    (', 'theorem a30_c_lift :\n    (True) → (', 1)}), dl),
        'module:statement-not-frozen:a30_c_lift')
    mut('gate-s-t-hold-n-undecided', base, lambda fe, dl: (dict(fe, **{MODULE: _module(
        base, drop=('a30_n_lifts', 'a30_0_admits'))}), dl), 'module:vector-off-table')
    mut('gate-n-lifts-0-undecided', base, lambda fe, dl: (dict(fe, **{MODULE: _module(
        base, drop=('a30_0_admits',))}), dl), 'module:vector-off-table')
    mut('note-vector-mismatch', base, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': _note(
        ('A30-S-HOLD', 'A30-T-HOLD', 'A30-N-LIFTS', 'A30-0-ADMITS')).replace(
        '`A30-S-HOLD` · `A30-T-HOLD`', '`A30-S-HOLD` · `A30-T-UNDECIDED`')}), dl),
        'note:vector-row-not-carried-once')
    mut('note-second-vector', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'] + '\n' + row_text(und) + '\n'}), dl),
        'note:vector-occurrences')
    mut('note-sentence-altered', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'].replace('at evidence level 2', 'at evidence level 3', 1)}), dl),
        'note:frozen-sentence')
    mut('note-unearned-sentence', und, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'] + '\n' + SENTENCES['A30-N-LIFTS'] + '\n'}), dl),
        'note:sentence-of-a-label-not-earned')
    mut('note-clause-twice', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'] + '\n' + CLAUSE + '\n'}), dl), 'note:the-clause')
    mut('note-mention-twice', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'] + '\n' + MENTION + '\n'}), dl), 'note:the-clause')
    mut('note-clause-detached', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'].replace(' — the result note.**\n', ' — the result note.**\n' + 'x ' * 60 + '\n', 1)}), dl),
        'note:the-clause')
    mut('note-clause-truncated', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'].replace(CLAUSE.split('\n')[-1], '')}), dl),
        'note:the-clause')
    mut('note-watch-dropped', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'].replace(WATCH, '')}), dl), 'note:assumption-watch')
    mut('note-legs-unlisted', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'].replace('`pra-road-leg`', 'x')}), dl),
        'note:replaced-leg-not-listed:pra-road-leg')
    mut('roadmap-stale-pfr-kept', base, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        P0_ADMITS, P0_PFR + ' ' + P0_STANDING + ' ' + P0_ADMITS)}), dl), 'roadmap:')
    mut('roadmap-wrong-case', base, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        P0_ADMITS, P0_RESTRICTS)}), dl), 'roadmap:')
    mut('roadmap-standing-dropped', neg, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        ' ' + P0_STANDING + ' |', ' |')}), dl), 'roadmap:')
    mut('roadmap-touched-when-undecided', und, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(
        fd[ROADMAP], base)}), dict(dl, **{ROADMAP: 'M'})), 'roadmap:')
    mut('guard-one-byte', base, lambda fe, dl: (dict(fe, **{GUARD: fe[GUARD] + ' '}), dl), 'guard:')
    mut('guard-untouched-when-decided', base, lambda fe, dl: (dict(fe, **{GUARD: fd[GUARD]}),
        dict((k, v) for k, v in dl.items() if k != GUARD)), 'guard:')
    mut('guard-retired-when-undecided', und, lambda fe, dl: (dict(fe, **{GUARD: retired_guard(
        fd[GUARD])}), dict(dl, **{GUARD: 'M'})), 'guard:')
    mut('guard-one-leg-restored', base, lambda fe, dl: (dict(fe, **{GUARD: fe[GUARD].replace(
        '#9\n', '#9\n' + LEDGER[9]['old'])}), dl), 'guard:')
    mut('census-status-promoted', base, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"status": "kernel-only",\n      "manuscript": [],\n      "note": "Outcome',
        '"status": "manuscript-cited",\n      "manuscript": [],\n      "note": "Outcome')}), dl),
        'census:family-disposition')
    mut('census-other-entry-changed', base, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"note": "n"', '"note": "m"')}), dl), 'census:another-entry-changed')
    mut('census-vector-wrong', base, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        'A30-0-ADMITS.', 'A30-0-UNDECIDED.')}), dl), 'census:vector')
    mut('census-entry-absent', base, lambda fe, dl: (dict(fe, **{CENSUS: fd[CENSUS]}), dl),
        'census:family-count-or-place')
    mut('wire-absent', base, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT]}), dl), 'wire:')
    mut('wire-misplaced', base, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT] + WIRE}), dl), 'wire:')
    mut('path-extra', base, lambda fe, dl: (fe, dict(dl, **{'papers/SM.md': 'M'})), 'paths:')
    mut('path-missing-note', base, lambda fe, dl: (fe, dict((k, v) for k, v in dl.items()
                                                           if k != RDIR + 'result.md')), 'paths:')
    # the retired guard reproduces its frozen ledger, and a tampered ledger entry does not apply
    t = [dict(e) for e in LEDGER]
    t[0]['old'] = t[0]['old'] + 'x'
    saved = list(LEDGER)
    LEDGER[:] = t
    if retired_guard(fd[GUARD]) is not None:
        bad.append('mutation ledger-tampered: the tampered ledger still applied')
    LEDGER[:] = saved
    muts.append('ledger-tampered')
    return bad, len(ROWS), len(muts)


def main():
    if sys.argv[1:] == ['--self-test']:
        bad, rows, muts = self_test()
        for b in bad:
            print('  FAIL', b)
        if bad:
            print('controls: self-test FAILED')
            return 1
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
