"""Track B act 34 -- the round's own static controls, frozen with the control plane.

Written before F; its blob is frozen in the preregistration beside it, and the execution adds it
with that exact blob. It reads nothing but the repository at D and at the commit under check, and
it certifies nothing on its own: the Lean kernel, the axiom audit and the release gate establish
the mathematics, and the V3 verifier the protocol. What it checks is that the execution carries
the frozen statements, the frozen outcome grammar and the frozen surface edits, and nothing else.

    python3 controls.py --self-test     the duality of the two verdict propositions, the single
                                        source of every shared text, the mutation controls on
                                        synthetic inputs, and the agreement of the constants
                                        below with the preregistration beside this file
    python3 controls.py check <commit>  every control against the tree at <commit>, read from git

Exit 1 on any failure.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

D = 'a2f3d8209dba3133424f2609b2763a49a73c2174'
RDIR = 'verification/programmes/oi-qm/track-b/act-34-product-stratum/'
MODULE = 'verification/lean-mathlib/OIBridge/ProductStratum.lean'
ROOT = 'verification/lean-mathlib/OIBridge.lean'
GUARD = 'verification/lean/edge_rigidity_probe.py'
CENSUS = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
ROADMAP_BLOB_D = '32b4886983ce2e9026e3ec2afdc9f827f9d96801'
GUARD_BLOB_D = 'd28e9b3cf2093984a1c453892204b9932a685b2e'

IMPORT = 'import OIBridge.OrbitIsometryGroup\n'
WIRE_AFTER = 'import OIBridge.OrbitIsometryGroup\n'
WIRE = 'import OIBridge.ProductStratum\n'
OPEN = "open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection\n  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted\n  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries\n  OrbitGeometryRigidity OrbitIsometryGroup\n"
NAMESPACE = 'ProductStratum'

# ---- act 33's frozen normal-form text, which the corollary carries verbatim (with `f`, and with `g`)
A33_NF_UNIQ = "(∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if νε.2 r then z else star z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if νε.2 r then z else star z)))"

# ---- the frozen propositions, verbatim
PROPS = {
 "P_R": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ((S = ⋃ (r : Fin 9) (s : Fin 9), tor r s)\n  ∧ (∀ r r' s s' : Fin 9, adj r r' → adj s s' →\n    tor r s ∩ tor r' s' = {featureVec (prod (tup r (μ r r')) (tup s (μ s s')))})\n  ∧ (∀ r s s' : Fin 9, adj s s' →\n    tor r s ∩ tor r s' = {x | ∃ z : ℂ, star z * z = 1 ∧ x = featureVec (prod (tup r z) (tup s (μ s s')))})\n  ∧ (∀ r r' s : Fin 9, adj r r' →\n    tor r s ∩ tor r' s = {x | ∃ w : ℂ, star w * w = 1 ∧ x = featureVec (prod (tup r (μ r r')) (tup s w))})\n  ∧ (∀ r r' s s' : Fin 9, (r ≠ r' ∧ ¬ adj r r') ∨ (s ≠ s' ∧ ¬ adj s s') →\n    tor r s ∩ tor r' s' = ∅))\n  ∧ ((∀ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) g →\n    ∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧\n      ∀ X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ X' → RealizableGram (Fin 1) Γ₀ Y' →\n        f (featureVec X) = featureVec X' → g (featureVec Y) = featureVec Y' → F (featureVec (prod X Y)) = featureVec (prod X' Y'))\n  ∧ (∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧\n    ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → F (featureVec (prod X Y)) = featureVec (prod Y X)))\n  ∧ (∀ (F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) (Φ₁ Φ₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), IsSurjIsometryOn S F →\n    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ (Φ₁ X) ∧ RealizableGram (Fin 1) Γ₀ (Φ₂ Y) ∧ F (featureVec (prod X Y)) = featureVec (prod (Φ₁ X) (Φ₂ Y))) →\n    ∃ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧\n      ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y))",
 "P_N": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ¬ ((S = ⋃ (r : Fin 9) (s : Fin 9), tor r s)\n  ∧ (∀ r r' s s' : Fin 9, adj r r' → adj s s' →\n    tor r s ∩ tor r' s' = {featureVec (prod (tup r (μ r r')) (tup s (μ s s')))})\n  ∧ (∀ r s s' : Fin 9, adj s s' →\n    tor r s ∩ tor r s' = {x | ∃ z : ℂ, star z * z = 1 ∧ x = featureVec (prod (tup r z) (tup s (μ s s')))})\n  ∧ (∀ r r' s : Fin 9, adj r r' →\n    tor r s ∩ tor r' s = {x | ∃ w : ℂ, star w * w = 1 ∧ x = featureVec (prod (tup r (μ r r')) (tup s w))})\n  ∧ (∀ r r' s s' : Fin 9, (r ≠ r' ∧ ¬ adj r r') ∨ (s ≠ s' ∧ ¬ adj s s') →\n    tor r s ∩ tor r' s' = ∅))\n  ∨ ¬ ((∀ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) g →\n    ∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧\n      ∀ X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ X' → RealizableGram (Fin 1) Γ₀ Y' →\n        f (featureVec X) = featureVec X' → g (featureVec Y) = featureVec Y' → F (featureVec (prod X Y)) = featureVec (prod X' Y'))\n  ∧ (∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧\n    ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → F (featureVec (prod X Y)) = featureVec (prod Y X)))\n  ∨ ¬ (∀ (F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) (Φ₁ Φ₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), IsSurjIsometryOn S F →\n    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ (Φ₁ X) ∧ RealizableGram (Fin 1) Γ₀ (Φ₂ Y) ∧ F (featureVec (prod X Y)) = featureVec (prod (Φ₁ X) (Φ₂ Y))) →\n    ∃ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧\n      ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y))",
 "FACT": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∀ (X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (p : ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))),\n    mixedTriple (prod X Y) p = mixedTriple X ((p.1.1.1, p.1.2.1.1, p.1.2.2.1), (p.2.1.1, p.2.2.1.1, p.2.2.2.1)) * mixedTriple Y ((p.1.1.2, p.1.2.1.2, p.1.2.2.2), (p.2.1.2, p.2.2.1.2, p.2.2.2.2))",
 "INNER": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∀ (X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),\n    inner ℂ (featureVec (prod X Y)) (featureVec (prod X' Y')) = inner ℂ (featureVec X) (featureVec X') * inner ℂ (featureVec Y) (featureVec Y')",
 "FIBRE": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∀ (X X' Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ Y →\n    dist (featureVec (prod X Y)) (featureVec (prod X' Y)) = dist (featureVec X) (featureVec X')\n    ∧ dist (featureVec (prod Y X)) (featureVec (prod Y X')) = dist (featureVec X) (featureVec X')",
 "PAIR": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∀ (X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ X' → RealizableGram (Fin 1) Γ₀ Y' →\n    featureVec (prod X Y) = featureVec (prod X' Y') → featureVec X = featureVec X' ∧ featureVec Y = featureVec Y'",
 "COVER": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  S = ⋃ (r : Fin 9) (s : Fin 9), tor r s",
 "POINT": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∀ r r' s s' : Fin 9, adj r r' → adj s s' →\n    tor r s ∩ tor r' s' = {featureVec (prod (tup r (μ r r')) (tup s (μ s s')))}",
 "CIRC_L": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∀ r s s' : Fin 9, adj s s' →\n    tor r s ∩ tor r s' = {x | ∃ z : ℂ, star z * z = 1 ∧ x = featureVec (prod (tup r z) (tup s (μ s s')))}",
 "CIRC_R": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∀ r r' s : Fin 9, adj r r' →\n    tor r s ∩ tor r' s = {x | ∃ w : ℂ, star w * w = 1 ∧ x = featureVec (prod (tup r (μ r r')) (tup s w))}",
 "APART": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∀ r r' s s' : Fin 9, (r ≠ r' ∧ ¬ adj r r') ∨ (s ≠ s' ∧ ¬ adj s s') →\n    tor r s ∩ tor r' s' = ∅",
 "COUNT": "  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  (Finset.univ.filter (fun q : (Fin 9 × Fin 9) × (Fin 9 × Fin 9) => (q.1.1 ≠ q.2.1 ∧ (v₁ q.1.1 = v₁ q.2.1 ∨ v₁ q.1.1 = v₂ q.2.1 ∨ v₂ q.1.1 = v₁ q.2.1 ∨ v₂ q.1.1 = v₂ q.2.1)) ∧ (q.1.2 ≠ q.2.2 ∧ (v₁ q.1.2 = v₁ q.2.2 ∨ v₁ q.1.2 = v₂ q.2.2 ∨ v₂ q.1.2 = v₁ q.2.2 ∨ v₂ q.1.2 = v₂ q.2.2)))).card = 1296\n  ∧ (Finset.univ.filter (fun q : (Fin 9 × Fin 9) × (Fin 9 × Fin 9) => (q.1.1 = q.2.1 ∧ (q.1.2 ≠ q.2.2 ∧ (v₁ q.1.2 = v₁ q.2.2 ∨ v₁ q.1.2 = v₂ q.2.2 ∨ v₂ q.1.2 = v₁ q.2.2 ∨ v₂ q.1.2 = v₂ q.2.2))) ∨ (q.1.2 = q.2.2 ∧ (q.1.1 ≠ q.2.1 ∧ (v₁ q.1.1 = v₁ q.2.1 ∨ v₁ q.1.1 = v₂ q.2.1 ∨ v₂ q.1.1 = v₁ q.2.1 ∨ v₂ q.1.1 = v₂ q.2.1))))).card = 648",
 "TENSOR": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∀ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) g →\n    ∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧\n      ∀ X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ X' → RealizableGram (Fin 1) Γ₀ Y' →\n        f (featureVec X) = featureVec X' → g (featureVec Y) = featureVec Y' → F (featureVec (prod X Y)) = featureVec (prod X' Y')",
 "SWAP": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧\n    ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → F (featureVec (prod X Y)) = featureVec (prod Y X)",
 "LOCAL": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∀ (F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) (Φ₁ Φ₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), IsSurjIsometryOn S F →\n    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ (Φ₁ X) ∧ RealizableGram (Fin 1) Γ₀ (Φ₂ Y) ∧ F (featureVec (prod X Y)) = featureVec (prod (Φ₁ X) (Φ₂ Y))) →\n    ∃ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧\n      ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y)",
 "NFORM": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  ∀ (F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) (Φ₁ Φ₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), IsSurjIsometryOn S F →\n    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ (Φ₁ X) ∧ RealizableGram (Fin 1) Γ₀ (Φ₂ Y) ∧ F (featureVec (prod X Y)) = featureVec (prod (Φ₁ X) (Φ₂ Y))) →\n    ∃ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧\n      (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y))\n      ∧ (∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),\n    (∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if νε.2 r then z else star z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if νε.2 r then z else star z))))\n      ∧ (∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),\n    (∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        g (pt r z) = pt s (if νε.2 r then z else star z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        g (pt r z) = pt s (-(if νε.2 r then z else star z))))",
 "PROPER": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  let H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2\n  RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (H i j) * H i k)\n  ∧ ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, featureVec (prod X Y) ≠ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (H i j) * H i k)",
 "PRODUCT": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  let H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.2 j.2\n  ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (H i j) * H i k)",
 "BITS": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  featureVec (prod (tup 0 1) (tup 3 Complex.I)) = featureVec (prod (tup 4 1) (tup 3 Complex.I))\n  ∧ featureVec (prod (tup 0 1) (tup 3 Complex.I)) ≠ featureVec (prod (tup 0 1) (tup 3 (star Complex.I)))",
 "SQUARE": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n  dist (featureVec (prod (tup 0 (Complex.I * Complex.I)) (tup 3 Complex.I))) (featureVec (prod (tup 0 1) (tup 3 Complex.I)))\n    ≠ dist (featureVec (prod (tup 0 Complex.I) (tup 3 Complex.I))) (featureVec (prod (tup 0 1) (tup 3 Complex.I)))"
}

# ---- the shared components the propositions are built from
COMPONENTS = {
 "HEAD": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}\n  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')\n  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1\n",
 "FIN": "  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n",
 "INC": "(S = ⋃ (r : Fin 9) (s : Fin 9), tor r s)\n  ∧ (∀ r r' s s' : Fin 9, adj r r' → adj s s' →\n    tor r s ∩ tor r' s' = {featureVec (prod (tup r (μ r r')) (tup s (μ s s')))})\n  ∧ (∀ r s s' : Fin 9, adj s s' →\n    tor r s ∩ tor r s' = {x | ∃ z : ℂ, star z * z = 1 ∧ x = featureVec (prod (tup r z) (tup s (μ s s')))})\n  ∧ (∀ r r' s : Fin 9, adj r r' →\n    tor r s ∩ tor r' s = {x | ∃ w : ℂ, star w * w = 1 ∧ x = featureVec (prod (tup r (μ r r')) (tup s w))})\n  ∧ (∀ r r' s s' : Fin 9, (r ≠ r' ∧ ¬ adj r r') ∨ (s ≠ s' ∧ ¬ adj s s') →\n    tor r s ∩ tor r' s' = ∅)",
 "ACT": "(∀ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) g →\n    ∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧\n      ∀ X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ X' → RealizableGram (Fin 1) Γ₀ Y' →\n        f (featureVec X) = featureVec X' → g (featureVec Y) = featureVec Y' → F (featureVec (prod X Y)) = featureVec (prod X' Y'))\n  ∧ (∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧\n    ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → F (featureVec (prod X Y)) = featureVec (prod Y X))",
 "LOCAL": "∀ (F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) (Φ₁ Φ₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), IsSurjIsometryOn S F →\n    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ (Φ₁ X) ∧ RealizableGram (Fin 1) Γ₀ (Φ₂ Y) ∧ F (featureVec (prod X Y)) = featureVec (prod (Φ₁ X) (Φ₂ Y))) →\n    ∃ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧\n      ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y)",
 "COVER": "S = ⋃ (r : Fin 9) (s : Fin 9), tor r s",
 "POINT": "∀ r r' s s' : Fin 9, adj r r' → adj s s' →\n    tor r s ∩ tor r' s' = {featureVec (prod (tup r (μ r r')) (tup s (μ s s')))}",
 "CIRC_L": "∀ r s s' : Fin 9, adj s s' →\n    tor r s ∩ tor r s' = {x | ∃ z : ℂ, star z * z = 1 ∧ x = featureVec (prod (tup r z) (tup s (μ s s')))}",
 "CIRC_R": "∀ r r' s : Fin 9, adj r r' →\n    tor r s ∩ tor r' s = {x | ∃ w : ℂ, star w * w = 1 ∧ x = featureVec (prod (tup r (μ r r')) (tup s w))}",
 "APART": "∀ r r' s s' : Fin 9, (r ≠ r' ∧ ¬ adj r r') ∨ (s ≠ s' ∧ ¬ adj s s') →\n    tor r s ∩ tor r' s' = ∅",
 "TENSOR": "∀ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) g →\n    ∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧\n      ∀ X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ X' → RealizableGram (Fin 1) Γ₀ Y' →\n        f (featureVec X) = featureVec X' → g (featureVec Y) = featureVec Y' → F (featureVec (prod X Y)) = featureVec (prod X' Y')",
 "SWAP": "∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧\n    ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → F (featureVec (prod X Y)) = featureVec (prod Y X)",
 "LOCAL_HYP": "∀ (F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) (Φ₁ Φ₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), IsSurjIsometryOn S F →\n    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ (Φ₁ X) ∧ RealizableGram (Fin 1) Γ₀ (Φ₂ Y) ∧ F (featureVec (prod X Y)) = featureVec (prod (Φ₁ X) (Φ₂ Y))) →\n",
 "LOCAL_CONCL": "∃ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧\n      ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y)",
 "NF_F": "(∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if νε.2 r then z else star z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if νε.2 r then z else star z)))",
 "NF_G": "(∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        g (pt r z) = pt s (if νε.2 r then z else star z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        g (pt r z) = pt s (-(if νε.2 r then z else star z)))",
 "GDEF": "fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (H i j) * H i k",
 "F4I": "!![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I]",
 "F4T": "!![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)]",
 "ADJ": "(q.1.1 ≠ q.2.1 ∧ (v₁ q.1.1 = v₁ q.2.1 ∨ v₁ q.1.1 = v₂ q.2.1 ∨ v₂ q.1.1 = v₁ q.2.1 ∨ v₂ q.1.1 = v₂ q.2.1))",
 "ADJ2": "(q.1.2 ≠ q.2.2 ∧ (v₁ q.1.2 = v₁ q.2.2 ∨ v₁ q.1.2 = v₂ q.2.2 ∨ v₂ q.1.2 = v₁ q.2.2 ∨ v₂ q.1.2 = v₂ q.2.2))"
}

# ---- the theorems: (role, name, proposition key)
THEOREMS = [
 [
  "A34-STRATIFIED",
  "a34_stratified",
  "P_R"
 ],
 [
  "A34-NOT-STRATIFIED",
  "a34_not_stratified",
  "P_N"
 ],
 [
  "A34-1",
  "a34_shared_factor",
  "FACT"
 ],
 [
  "A34-1",
  "a34_shared_inner",
  "INNER"
 ],
 [
  "A34-2",
  "a34_shared_cover",
  "COVER"
 ],
 [
  "A34-2",
  "a34_shared_point",
  "POINT"
 ],
 [
  "A34-2",
  "a34_shared_circle_left",
  "CIRC_L"
 ],
 [
  "A34-2",
  "a34_shared_circle_right",
  "CIRC_R"
 ],
 [
  "A34-2",
  "a34_shared_apart",
  "APART"
 ],
 [
  "A34-2",
  "a34_shared_count",
  "COUNT"
 ],
 [
  "A34-3",
  "a34_shared_tensor",
  "TENSOR"
 ],
 [
  "A34-3",
  "a34_shared_swap",
  "SWAP"
 ],
 [
  "A34-5",
  "a34_shared_fibre",
  "FIBRE"
 ],
 [
  "A34-5",
  "a34_shared_pairing",
  "PAIR"
 ],
 [
  "A34-5",
  "a34_shared_local",
  "LOCAL"
 ],
 [
  "A34-5 corollary",
  "a34_c_normal_form",
  "NFORM"
 ],
 [
  "A34-4",
  "a34_control_proper",
  "PROPER"
 ],
 [
  "control",
  "a34_control_product",
  "PRODUCT"
 ],
 [
  "control",
  "a34_control_bits",
  "BITS"
 ],
 [
  "control",
  "a34_control_square",
  "SQUARE"
 ]
]
LABELS = [(role, nm, key) for role, nm, key in THEOREMS if role.startswith('A34-') and role[4:5].isalpha()]
COROLLARY = ('a34_c_exclusive', ['P_N'], 'P_R')
SHARED = re.compile(r'^a34_shared_[A-Za-z0-9_]+$')
UNDECIDED = 'A34-UNDECIDED'
STRATIFIED, NOT_STRATIFIED = 'A34-STRATIFIED', 'A34-NOT-STRATIFIED'
ROWS = (STRATIFIED, NOT_STRATIFIED, UNDECIDED)
STRUCTURAL = [(nm, key) for role, nm, key in THEOREMS if role in ('A34-2', 'A34-3', 'A34-5', 'A34-5 corollary')]
ALWAYS = [(nm, key) for role, nm, key in THEOREMS if role in ('A34-1', 'A34-4', 'control')]
REQUIRED = {STRATIFIED: STRUCTURAL + ALWAYS, NOT_STRATIFIED: ALWAYS, UNDECIDED: []}
OUTCOME_RE = re.compile(r'\*\*Outcome:\*\* `(A34-[A-Z-]+)`')
LABEL_RE = re.compile(r'A34-(?:NOT-STRATIFIED|STRATIFIED|UNDECIDED)')

SENTENCES = {
 "A34-STRATIFIED": "At the frozen product configuration, the five-part product-stratum package holds, at evidence level 2: the feature map of a product tuple is the coordinatewise product of the factors' feature maps under the index pairing, so inner products of product feature vectors multiply; the product-embedded stratum is the union of the eighty-one tori, the products of pairs of act 26's nine relabelled Fourier circles, two tori meeting in a single point when both index pairs are adjacent in the incidence graph `K₃,₃`, in a shared circle when one index agrees and the other pair is adjacent, and not at all otherwise; act 33's group acts on the stratum factorwise by surjective isometries, and the factor exchange is a surjective isometry; the stratum is a proper subset of the product normalized set, by an exhibited realizable class with entries in the fourth roots of unity; and every surjective isometry of the stratum that factorizes through two single-carrier maps has both factors surjective isometries of the single-carrier normalized space, hence in act 33's group with unique normal forms. This is a statement about the frozen mathematical object; it adopts no isometry as a symmetry, a principle or a law, and it does not classify the isometries of the stratum or of the product normalized set.",
 "A34-NOT-STRATIFIED": "At the frozen product configuration, the five-part product-stratum package fails, at evidence level 2: the incidence census of the eighty-one tori, the factorwise action of act 33's group with the factor exchange, or the restriction of factorized surjective isometries of the stratum to act 33's group is false, and the witness is exhibited in the kernel; the exact factorization of the feature map and the properness of the stratum hold. This is a statement about the frozen mathematical object; it adopts no isometry as a symmetry, a principle or a law.",
 "A34-UNDECIDED": "Neither the package nor its negation was obtained. The step at which the proof stopped is named, with what would settle it."
}
CLAUSE = "Act 34 proves five statements about the product-embedded stratum of act 29's product configuration, the\nfeature vectors of the products of two realizable single-carrier tuples, and adopts none of them as\nanything but mathematics. The stratum is a mathematical object, a finite union of tori in a Euclidean\nspace; its incidence structure, the action on it and the restriction it places on factorized\nsurjective isometries are facts about that object and about nothing else. A `STRATIFIED` verdict\nsettles the frozen five-part package, and a `NOT-STRATIFIED` verdict exhibits the failure of a named\npart; both leave the full product normalized set, which the round proves strictly larger than the\nstratum, unclassified. Neither verdict establishes that any admissible transition law is covariant\nunder the stratum's isometries, selects a physical law or closes `P0`. No isometry, carrier, family,\ngroup or principle gains physical status by appearing here, and nothing here derives, recognises or\napproaches quantum evolution."
MENTION = 'THE CLAUSE, carried at this mention'

# ---- the `P0` cell: the end of the cell at D, and the sentence appended per decided case
P0_END_D = "At the single-carrier configuration, the surjective isometries of the normalized space are classified: each permutes the nine relabelled Fourier circles by an automorphism of their incidence graph `K₃,₃` and conjugates the parameter on an arbitrary subset of the circles, 36864 in all, and act 25's four-shape family is a subgroup of index 16. `P0`'s threading part is untouched, no isometry of the normalized space is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle."
P0_CASE = {
 "A34-STRATIFIED": "At the product configuration, the feature map factorizes exactly on product tuples, the product-embedded stratum is the union of eighty-one tori whose incidence is the product of the two `K₃,₃` incidences, act 33's group acts on it factorwise together with the factor exchange, the stratum is a proper subset of the product normalized set by an exhibited realizable class, and every surjective isometry of the stratum that factorizes through two single-carrier maps has both factors in act 33's group: a finite geometric restriction conditional on stratum-isometry covariance.",
 "A34-NOT-STRATIFIED": "At the product configuration, the five-part product-stratum package fails at a named part, by a witness exhibited in the kernel, while the feature map factorizes exactly on product tuples and the stratum is a proper subset of the product normalized set by an exhibited realizable class."
}
P0_STANDING_34 = "Nothing here establishes that any admissible law is covariant under the stratum's isometries or reaches the classes outside the stratum, `P0`'s threading part is untouched, no isometry of the stratum is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle."

CENSUS_MODULES = ['ProductStratum']

_BAD_CMD = re.compile(r'(?m)^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?(?:private[ \t]+|protected[ \t]+|noncomputable[ \t]+|'
                      r'unsafe[ \t]+|partial[ \t]+)*(?:def|abbrev|structure|class|instance|inductive|axiom|opaque|'
                      r'example|variable|include|omit|section|macro|syntax|elab|notation|infix|prefix|postfix|'
                      r'set_option|import|attribute|local|scoped|universe|initialize|deriving|mutual|declare_syntax_cat)\b')
_BAD_TOKEN = re.compile(r'\b(?:sorry|native_decide|admit|unsafe|implemented_by|extern)\b')


def norm(t):
    t = ' '.join(t.split())
    t = re.sub(r'\( ', '(', t)
    return re.sub(r' \)', ')', t)


def qnorm(t):
    return ' '.join(re.sub(r'(?m)^[ \t]*>[ \t]?', '', t).split())


def sha(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()


def dual_texts(c):
    """The two verdict propositions, rebuilt from their shared components."""
    r = c['HEAD'] + '  (' + c['INC'] + ')\n  ∧ (' + c['ACT'] + ')\n  ∧ (' + c['LOCAL'] + ')'
    n = c['HEAD'] + '  ¬ (' + c['INC'] + ')\n  ∨ ¬ (' + c['ACT'] + ')\n  ∨ ¬ (' + c['LOCAL'] + ')'
    return r, n


SOURCE_TABLE = (
    ('FACT', 'HEAD', 1), ('INNER', 'HEAD', 1), ('FIBRE', 'HEAD', 1), ('PAIR', 'HEAD', 1), ('COVER', 'HEAD', 1),
    ('POINT', 'HEAD', 1), ('CIRC_L', 'HEAD', 1), ('CIRC_R', 'HEAD', 1), ('APART', 'HEAD', 1), ('TENSOR', 'HEAD', 1),
    ('SWAP', 'HEAD', 1), ('LOCAL', 'HEAD', 1), ('NFORM', 'HEAD', 1), ('PROPER', 'HEAD', 1), ('PRODUCT', 'HEAD', 1),
    ('BITS', 'HEAD', 1), ('SQUARE', 'HEAD', 1), ('P_R', 'HEAD', 1), ('P_N', 'HEAD', 1),
    ('COUNT', 'FIN', 1), ('COUNT', 'ADJ', 2), ('COUNT', 'ADJ2', 2),
    ('COVER', 'COVER', 1), ('POINT', 'POINT', 1), ('CIRC_L', 'CIRC_L', 1), ('CIRC_R', 'CIRC_R', 1), ('APART', 'APART', 1),
    ('TENSOR', 'TENSOR', 1), ('SWAP', 'SWAP', 1), ('LOCAL', 'LOCAL', 1), ('LOCAL', 'LOCAL_HYP', 1), ('LOCAL', 'LOCAL_CONCL', 1),
    ('NFORM', 'LOCAL_HYP', 1), ('NFORM', 'NF_F', 1), ('NFORM', 'NF_G', 1), ('NFORM', 'LOCAL_CONCL', 0),
    ('P_R', 'INC', 1), ('P_R', 'ACT', 1), ('P_R', 'LOCAL', 1), ('P_N', 'INC', 1), ('P_N', 'ACT', 1), ('P_N', 'LOCAL', 1),
    ('P_R', 'COVER', 1), ('P_R', 'POINT', 1), ('P_R', 'CIRC_L', 1), ('P_R', 'CIRC_R', 1), ('P_R', 'APART', 1),
    ('P_R', 'TENSOR', 1), ('P_R', 'SWAP', 1),
    ('PROPER', 'GDEF', 2), ('PROPER', 'F4I', 1), ('PROPER', 'F4T', 1), ('PRODUCT', 'GDEF', 1), ('PRODUCT', 'F4I', 2),
    ('PRODUCT', 'F4T', 0),
)


def duality_ok(props, comps):
    """P_R is `INC ∧ ACT ∧ LOCAL` and P_N is `¬ INC ∨ ¬ ACT ∨ ¬ LOCAL` over one head, so each verdict is
    the other's negation; INC is the conjunction of the five incidence statements, ACT of the two
    action statements, LOCAL the factorized-isometry statement; every other statement carries the
    one head, and the corollary carries act 33's normal-form text verbatim."""
    f = []
    r, n = dual_texts(comps)
    if norm(props['P_R']) != norm(r):
        f.append('duality:P_R-is-not-the-frozen-conjunction')
    if norm(props['P_N']) != norm(n):
        f.append('duality:P_N-is-not-the-frozen-disjunction')
    inc = '(' + comps['COVER'] + ')\n  ∧ (' + comps['POINT'] + ')\n  ∧ (' + comps['CIRC_L'] + ')\n  ∧ (' + comps['CIRC_R'] + ')\n  ∧ (' + comps['APART'] + ')'
    if norm(comps['INC']) != norm(inc):
        f.append('duality:INC-is-not-the-conjunction-of-the-five')
    if norm(comps['ACT']) != norm('(' + comps['TENSOR'] + ')\n  ∧ (' + comps['SWAP'] + ')'):
        f.append('duality:ACT-is-not-the-conjunction-of-the-two')
    if norm(comps['LOCAL']) != norm(comps['LOCAL_HYP'] + '    ' + comps['LOCAL_CONCL']):
        f.append('duality:LOCAL-is-not-hypothesis-then-conclusion')
    if comps['NF_F'] != A33_NF_UNIQ or comps['NF_G'] != A33_NF_UNIQ.replace('f (pt r z)', 'g (pt r z)'):
        f.append('source:corollary-normal-form-is-not-act-33s')
    for key, comp, k in SOURCE_TABLE:
        if norm(props[key]).count(norm(comps[comp])) != k:
            f.append('source:%s-does-not-carry-%s-%d-times' % (key, comp, k))
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


_END = re.compile(r':=[ \t]*(?:by\b|\n)')


def theorems(code):
    """name -> the text between the name and the `:=` that opens the proof: the first `:=` followed
    by `by` or by the end of its line, so that a `let x := v` inside a statement does not end it."""
    out = {}
    for m in _THM.finditer(code):
        nm = m.group(1)
        rest = code[m.end():]
        e = _END.search(rest)
        out[nm] = None if nm in out else (rest if e is None else rest[:e.start()])
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
    if 'namespace OIBridge\nnamespace %s\n' % NAMESPACE not in code or \
            not code.rstrip().endswith('end %s\nend OIBridge' % NAMESPACE):
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
    names = {x[1] for x in LABELS} | {COROLLARY[0]} | {x[0] for x in STRUCTURAL + ALWAYS}
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
    for nm, key in STRUCTURAL + ALWAYS:
        if nm in th and th[nm] is not None and norm(th[nm]) != statement(key):
            f.append('module:statement-not-frozen:' + nm)
    for nm, key in REQUIRED[label]:
        if nm not in th:
            f.append('module:required-statement-absent:' + nm)
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
    for nm, _ in REQUIRED[label]:
        if '`%s`' % nm not in note:
            f.append('note:required-statement-not-named:' + nm)
    return f


# ---- the surfaces ------------------------------------------------------------------------------
def expected_roadmap(road_d, label):
    if label == UNDECIDED:
        return road_d
    old = ' ' + P0_END_D + ' |'
    if road_d.count(old) != 1:
        return None
    return road_d.replace(old, ' ' + P0_END_D + ' ' + P0_CASE[label] + ' ' + P0_STANDING_34 + ' |', 1)


def census_ok(cen_d, cen_e, label):
    f = []
    try:
        d, e = json.loads(cen_d), json.loads(cen_e)
    except ValueError:
        return ['census:not-json']
    if cen_e != json.dumps(e, indent=2, ensure_ascii=False) + '\n':
        f.append('census:not-in-the-registry-format')
    fams = e.get('families', [])
    mine = [x for x in fams if CENSUS_MODULES[0] in x.get('modules', [])]
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
        f.append('guard:not-byte-identical-to-D')
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
    parts = [IMPORT, '/-! synthetic -/\n', 'namespace OIBridge\nnamespace %s\n\n' % NAMESPACE,
             OPEN, '\n']

    def th(nm, s):
        parts.append('theorem %s :\n    %s := by\n  exact test\n#print axioms %s\n\n' % (nm, s, nm))
    th('a34_shared_x', 'True')
    for nm, key in REQUIRED[label]:
        if nm not in drop:
            th(nm, (stmt or {}).get(nm, PROPS[key]))
    for lab, nm, key in LABELS:
        if lab == label and nm not in drop:
            th(nm, (stmt or {}).get(nm, PROPS[key]))
    if COROLLARY[0] not in drop:
        th(COROLLARY[0], (stmt or {}).get(COROLLARY[0], corollary_statement()[2:]))
    parts.append(extra)
    parts.append('end %s\nend OIBridge\n' % NAMESPACE)
    return ''.join(parts)


def _note(label):
    parts = ['# result\n\n**Outcome:** `%s`\n\n' % label, '> ' + SENTENCES[label] + '\n\n']
    parts.append('> **' + MENTION + ' — the result note.**\n'
                 + '\n'.join('> ' + l for l in CLAUSE.split('\n')) + '\n\n')
    parts.append(' '.join('`%s`' % nm for nm, _ in REQUIRED[label]) + '\n')
    return ''.join(parts)


def _synthetic_d():
    road = '| **P0** | q | x | Act 25 a. Act 33 b. ' + P0_END_D + ' | y |\n'
    cen = json.dumps({'families': [{'name': 'x', 'modules': ['X'], 'status': 'kernel-only',
                                    'manuscript': [], 'note': 'n'}]},
                     indent=2, ensure_ascii=False) + '\n'
    return {ROADMAP: road, CENSUS: cen, ROOT: 'import A\n' + WIRE_AFTER + 'import B\n', GUARD: '# guard\n'}


def _synthetic_e(fd, label):
    fe = {MODULE: _module(label), RDIR + 'result.md': _note(label),
          ROADMAP: expected_roadmap(fd[ROADMAP], label), GUARD: fd[GUARD]}
    c = json.loads(fd[CENSUS])
    c['families'].append({'name': 'act 34', 'modules': CENSUS_MODULES,
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
        for k, v in list(SENTENCES.items()) + [('clause', CLAUSE), ('end-of-cell', P0_END_D),
                                               ('standing-34', P0_STANDING_34)] + list(P0_CASE.items()):
            if qnorm(v) not in q:
                bad.append('agreement: %s not in the preregistration' % k)
        for b in (ROADMAP_BLOB_D, GUARD_BLOB_D, D):
            if b not in text:
                bad.append('agreement: %s not in the preregistration' % b)
        for role, nm, key in THEOREMS:
            if '`%s`' % nm not in text:
                bad.append('agreement: theorem %s not in the preregistration' % nm)
    for a, x in SENTENCES.items():
        for b, y in SENTENCES.items():
            if a != b and qnorm(x) in qnorm(y):
                bad.append('distinctness: the sentence of %s lies inside that of %s' % (a, b))
    # the duality and the single source hold of the frozen texts, and fail when either is altered
    if duality_ok(PROPS, COMPONENTS):
        bad.append('duality: the frozen texts fail: %s' % duality_ok(PROPS, COMPONENTS))
    dmuts = 0
    for nm, key, old, new in (
            ('P_R-disjunction', 'P_R', '\n  ∧ (' + COMPONENTS['LOCAL'] + ')', '\n  ∨ (' + COMPONENTS['LOCAL'] + ')'),
            ('P_R-part-dropped', 'P_R', '\n  ∧ (' + COMPONENTS['ACT'] + ')', ''),
            ('P_N-negation-dropped', 'P_N', '\n  ∨ ¬ (' + COMPONENTS['LOCAL'] + ')', '\n  ∨ (' + COMPONENTS['LOCAL'] + ')'),
            ('P_N-conjunction', 'P_N', '\n  ∨ ¬ (' + COMPONENTS['ACT'] + ')', '\n  ∧ ¬ (' + COMPONENTS['ACT'] + ')'),
            ('cover-drift', 'COVER', 'S = ⋃', 'S ⊆ ⋃'),
            ('proper-twist-dropped', 'PROPER', COMPONENTS['F4T'], COMPONENTS['F4I']),
            ('corollary-normal-form-drift', 'NFORM', 'if νε.2 r then z else star z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        g', 'if νε.2 r then z else z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        g')):
        props = dict(PROPS)
        if props[key].count(old) < 1:
            bad.append('duality mutation %s: pattern absent' % nm)
            continue
        props[key] = props[key].replace(old, new, 1)
        dmuts += 1
        if not duality_ok(props, COMPONENTS):
            bad.append('duality mutation %s: accepted' % nm)
    comps = dict(COMPONENTS, NF_G=COMPONENTS['NF_G'].replace('-(if νε.2 r', '(if νε.2 r', 1))
    dmuts += 1
    if not duality_ok(PROPS, comps):
        bad.append('duality mutation component-drift: accepted')

    fd = _synthetic_d()
    for label in ROWS:
        fe, delta = _synthetic_e(fd, label)
        r = check_all(fd, fe, delta)
        if r:
            bad.append('positive %s: %s' % (label, r))
    ST, NS, X = ROWS
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
    E_ = 'end ' + NAMESPACE
    mut('definition-added', ST, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'noncomputable def zz := 1\n' + E_)}), dl), 'module:forbidden-command')
    mut('variable-added', ST, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a34_shared_x', '\nvariable (h : False)\ntheorem a34_shared_x')}), dl),
        'module:forbidden-command')
    mut('second-open', ST, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a34_shared_x', '\nopen Classical in\ntheorem a34_shared_x')}), dl), 'module:open')
    mut('second-import', ST, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '/-! synthetic -/', 'import Mathlib.GroupTheory.SemidirectProduct\n/-! synthetic -/')}), dl),
        'module:forbidden-command')
    mut('sorry', ST, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('exact test', 'sorry', 1)}), dl),
        'module:forbidden-token')
    mut('native-decide', ST, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('exact test', 'native_decide', 1)}), dl),
        'module:forbidden-token')
    mut('print-axioms-dropped', ST, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '#print axioms a34_stratified\n', '')}), dl), 'module:no-print-axioms')
    mut('stray-theorem-name', ST, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'theorem a34_n : True := trivial\n#print axioms a34_n\n' + E_)}), dl),
        'module:theorem-name-outside')
    mut('stratified-weakened', ST, modstmt(ST, 'a34_stratified', PROPS['P_R'].replace(
        '\n  ∧ (' + COMPONENTS['LOCAL'] + ')', '', 1)), 'module:statement-not-frozen:a34_stratified')
    mut('not-stratified-weakened', NS, modstmt(NS, 'a34_not_stratified', PROPS['P_N'].replace(
        '¬ (' + COMPONENTS['INC'] + ')', '(' + COMPONENTS['INC'] + ')', 1)), 'module:statement-not-frozen:a34_not_stratified')
    mut('cover-into-not-onto', ST, modstmt(ST, 'a34_shared_cover', PROPS['COVER'].replace(
        'S = ⋃', 'S ⊆ ⋃', 1)), 'module:statement-not-frozen:a34_shared_cover')
    mut('point-weakened', ST, modstmt(ST, 'a34_shared_point', PROPS['POINT'].replace(
        "tor r s ∩ tor r' s' = {", "tor r s ∩ tor r' s' ⊆ {", 1)), 'module:statement-not-frozen:a34_shared_point')
    mut('apart-weakened', ST, modstmt(ST, 'a34_shared_apart', PROPS['APART'].replace(
        "= ∅", "≠ ∅", 1)), 'module:statement-not-frozen:a34_shared_apart')
    mut('count-altered', ST, modstmt(ST, 'a34_shared_count', PROPS['COUNT'].replace('= 648', '= 324', 1)),
        'module:statement-not-frozen:a34_shared_count')
    mut('tensor-isometry-dropped', ST, modstmt(ST, 'a34_shared_tensor', PROPS['TENSOR'].replace(
        'IsSurjIsometryOn S F ∧', 'True ∧', 1)), 'module:statement-not-frozen:a34_shared_tensor')
    mut('fibre-weakened', ST, modstmt(ST, 'a34_shared_fibre', PROPS['FIBRE'].replace(
        '= dist (featureVec X) (featureVec X\')\n    ∧', '≤ dist (featureVec X) (featureVec X\')\n    ∧', 1)),
        'module:statement-not-frozen:a34_shared_fibre')
    mut('local-surjectivity-dropped', ST, modstmt(ST, 'a34_shared_local', PROPS['LOCAL'].replace(
        'IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧', 'IsSurjIsometryOn (normalizedSet Γ₀) f ∧', 1)),
        'module:statement-not-frozen:a34_shared_local')
    mut('local-hypothesis-weakened', ST, modstmt(ST, 'a34_shared_local', PROPS['LOCAL'].replace(
        'IsSurjIsometryOn S F →', 'True →', 1)), 'module:statement-not-frozen:a34_shared_local')
    mut('proper-trivialized', NS, modstmt(NS, 'a34_control_proper', PROPS['PROPER'].replace(
        'featureVec (prod X Y) ≠ featureVec', 'featureVec (prod X Y) = featureVec', 1)), 'module:statement-not-frozen:a34_control_proper')
    mut('proper-realizability-dropped', NS, modstmt(NS, 'a34_control_proper', PROPS['PROPER'].replace(
        'RealizableGram (Fin 1 × Fin 1)', 'RealizableGram (Fin 1)', 1)), 'module:statement-not-frozen:a34_control_proper')
    mut('product-control-twisted', NS, modstmt(NS, 'a34_control_product', PROPS['PRODUCT'].replace(
        COMPONENTS['F4I'] + ' i.2 j.2', COMPONENTS['F4T'] + ' i.2 j.2', 1)), 'module:statement-not-frozen:a34_control_product')
    mut('bits-trivialized', NS, modstmt(NS, 'a34_control_bits', PROPS['BITS'].replace('≠', '=', 1)),
        'module:statement-not-frozen:a34_control_bits')
    mut('square-trivialized', NS, modstmt(NS, 'a34_control_square', PROPS['SQUARE'].replace('≠', '=', 1)),
        'module:statement-not-frozen:a34_control_square')
    mut('factor-index-drift', NS, modstmt(NS, 'a34_shared_factor', PROPS['FACT'].replace(
        '(p.2.1.1, p.2.2.1.1, p.2.2.2.1)', '(p.2.1.1, p.2.2.1.1, p.2.2.2.2)', 1)), 'module:statement-not-frozen:a34_shared_factor')
    for nm, _ in REQUIRED[ST]:
        mut('required-absent:' + nm, ST, lambda fe, dl, nm=nm: (dict(fe, **{MODULE: _module(ST, drop=(nm,))}), dl),
            'module:required-statement-absent:' + nm)
    for nm, _ in REQUIRED[NS]:
        mut('required-absent-not-stratified:' + nm, NS, lambda fe, dl, nm=nm: (dict(fe, **{MODULE: _module(NS, drop=(nm,))}), dl),
            'module:required-statement-absent:' + nm)
    mut('corollary-absent', X, lambda fe, dl: (dict(fe, **{MODULE: _module(X, drop=('a34_c_exclusive',))}), dl),
        'module:required-corollary-absent')
    mut('corollary-altered', X, lambda fe, dl: (dict(fe, **{MODULE: _module(
        X, stmt={'a34_c_exclusive': corollary_statement()[2:].replace('→ ¬ (', '→ (', 1)})}), dl),
        'module:statement-not-frozen:a34_c_exclusive')
    mut('both-labels', ST, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'theorem a34_not_stratified :\n    ' + PROPS['P_N'] + ' := by\n  exact test\n'
        '#print axioms a34_not_stratified\n' + E_)}), dl), 'module:both-labels')
    mut('note-outcome-mismatch', ST, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '**Outcome:** `A34-STRATIFIED`', '**Outcome:** `A34-NOT-STRATIFIED`')}), dl), 'note:outcome-line')
    mut('note-second-outcome', ST, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n**Outcome:** `A34-STRATIFIED`\n'}), dl), 'note:outcome-line')
    mut('note-sentence-altered', ST, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        'evidence level 2', 'evidence level 3', 1)}), dl), 'note:frozen-sentence')
    mut('note-unearned-sentence', X, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + SENTENCES[ST] + '\n'}), dl), 'note:sentence-of-a-label-not-earned')
    mut('note-clause-twice', ST, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + CLAUSE + '\n'}), dl), 'note:the-clause')
    mut('note-clause-detached', ST, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        ' — the result note.**\n', ' — the result note.**\n' + 'x ' * 60 + '\n', 1)}), dl), 'note:the-clause')
    mut('note-control-unnamed', ST, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a34_control_square`', 'x')}), dl), 'note:required-statement-not-named')
    mut('note-structural-unnamed', ST, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a34_shared_local`', 'x')}), dl), 'note:required-statement-not-named')
    mut('roadmap-wrong-case', ST, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(fd[ROADMAP], NS)}), dl),
        'roadmap:')
    mut('roadmap-standing-dropped', ST, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        P0_CASE[ST] + ' ' + P0_STANDING_34, P0_CASE[ST])}), dl), 'roadmap:')
    mut('roadmap-sentence-misplaced', ST, lambda fe, dl: (dict(fe, **{ROADMAP: fd[ROADMAP].replace(
        ' Act 25 a.', ' Act 25 a. ' + P0_CASE[ST] + ' ' + P0_STANDING_34, 1)}), dl), 'roadmap:')
    mut('roadmap-touched-when-undecided', X, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(fd[ROADMAP], ST)}),
        dict(dl, **{ROADMAP: 'M'})), 'roadmap:')
    mut('guard-one-byte', ST, lambda fe, dl: (dict(fe, **{GUARD: fe[GUARD] + ' '}), dict(dl, **{GUARD: 'M'})), 'guard:')
    mut('census-status-promoted', ST, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"status": "kernel-only",\n      "manuscript": [],\n      "note": "Outcome',
        '"status": "manuscript-cited",\n      "manuscript": [],\n      "note": "Outcome')}), dl),
        'census:family-disposition')
    mut('census-other-entry-changed', ST, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"note": "n"', '"note": "m"')}), dl), 'census:another-entry-changed')
    mut('census-outcome-wrong', ST, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        'A34-STRATIFIED.', 'A34-NOT-STRATIFIED.')}), dl), 'census:outcome')
    mut('census-entry-absent', ST, lambda fe, dl: (dict(fe, **{CENSUS: fd[CENSUS]}), dl), 'census:family-count-or-place')
    mut('wire-absent', ST, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT]}), dl), 'wire:')
    mut('wire-misplaced', ST, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT] + WIRE}), dl), 'wire:')
    mut('path-extra', ST, lambda fe, dl: (fe, dict(dl, **{'papers/SM.md': 'M'})), 'paths:')
    mut('path-missing-note', ST, lambda fe, dl: (fe, dict((k, v) for k, v in dl.items()
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
        print('controls: the two verdict propositions are duals and every shared text has one source; '
              '%d duality mutations fail as required' % dmuts)
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
