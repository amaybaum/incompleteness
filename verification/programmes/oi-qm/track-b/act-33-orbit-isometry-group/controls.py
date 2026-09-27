"""Track B act 33 -- the round's own static controls, frozen with the control plane.

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

D = 'db82376dfc0e2ae561ec541fd0d3a915f082beda'
RDIR = 'verification/programmes/oi-qm/track-b/act-33-orbit-isometry-group/'
MODULE = 'verification/lean-mathlib/OIBridge/OrbitIsometryGroup.lean'
ROOT = 'verification/lean-mathlib/OIBridge.lean'
GUARD = 'verification/lean/edge_rigidity_probe.py'
CENSUS = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
ROADMAP_BLOB_D = 'b1f6f9f728d07c0361302ed1994d43e848522372'
GUARD_BLOB_D = 'd28e9b3cf2093984a1c453892204b9932a685b2e'

IMPORT = 'import OIBridge.OrbitGeometryRigidity\n'
WIRE_AFTER = 'import OIBridge.OrbitIsometryClassification\n'
WIRE = 'import OIBridge.OrbitIsometryGroup\n'
OPEN = "open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection\n  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted\n  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries\n  OrbitGeometryRigidity\n"
NAMESPACE = 'OrbitIsometryGroup'

# ---- the frozen propositions, verbatim
PROPS = {
 "P_R": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  (∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f →\n      ∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),\n    (∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if νε.2 r then z else star z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if νε.2 r then z else star z))))\n  ∧ (∀ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool),\n      (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)) →\n      ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧\n    (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if ε r then z else star z))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if ε r then z else star z))))",
 "P_N": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  (∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧\n      ¬ ∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),\n    (∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if νε.2 r then z else star z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if νε.2 r then z else star z))))\n  ∨ (∃ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool),\n      (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)) ∧\n      ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f →\n    ¬ ((∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if ε r then z else star z))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if ε r then z else star z)))))",
 "B1": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f →\n    ∀ r : Fin 9, ∃ s : Fin 9, f '' (pt r '' {z : ℂ | star z * z = 1}) = pt s '' {z : ℂ | star z * z = 1}",
 "B2": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → ∀ r s : Fin 9, f '' (pt r '' {z : ℂ | star z * z = 1}) = pt s '' {z : ℂ | star z * z = 1} →\n    ∃ (l : ℂ) (ε : Bool), star l * l = 1 ∧ ∀ z : ℂ, star z * z = 1 → f (pt r z) = pt s (l * (if ε then z else star z))",
 "B3": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → ∀ (σ : Fin 9 → Fin 9) (l : Fin 9 → ℂ) (ε : Fin 9 → Bool),\n    (∀ r, star (l r) * l r = 1) → (∀ r, ∀ z : ℂ, star z * z = 1 → f (pt r z) = pt (σ r) (l r * (if ε r then z else star z))) →\n    ∀ r, l r = 1 ∨ l r = -1",
 "COMP": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ∀ (ν ν' : Equiv.Perm (Fin 6)) (ε ε' : Fin 9 → Bool) (f f' : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) f' →\n    (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if ε r then z else star z))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if ε r then z else star z))) →\n    (∀ r : Fin 9, ∃ s : Fin 9, (ν' (v₁ r) = v₁ s ∧ ν' (v₂ r) = v₂ s) ∨ (ν' (v₁ r) = v₂ s ∧ ν' (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, ν' (v₁ r) = v₁ s → ν' (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f' (pt r z) = pt s (if ε' r then z else star z))\n    ∧ (∀ r s : Fin 9, ν' (v₁ r) = v₂ s → ν' (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f' (pt r z) = pt s (-(if ε' r then z else star z))) →\n    ∀ ε'' : Fin 9 → Bool, (∀ r s : Fin 9, (ν' (v₁ r) = v₁ s ∧ ν' (v₂ r) = v₂ s) ∨ (ν' (v₁ r) = v₂ s ∧ ν' (v₂ r) = v₁ s) →\n        ε'' r = decide (ε' r = ε s)) →\n    (∀ r : Fin 9, ∃ s : Fin 9, ((ν * ν') (v₁ r) = v₁ s ∧ (ν * ν') (v₂ r) = v₂ s) ∨ ((ν * ν') (v₁ r) = v₂ s ∧ (ν * ν') (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, (ν * ν') (v₁ r) = v₁ s → (ν * ν') (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        (f ∘ f') (pt r z) = pt s (if ε'' r then z else star z))\n    ∧ (∀ r s : Fin 9, (ν * ν') (v₁ r) = v₂ s → (ν * ν') (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        (f ∘ f') (pt r z) = pt s (-(if ε'' r then z else star z)))",
 "C_ID": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  (∀ r : Fin 9, ∃ s : Fin 9, ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s) ∨ ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        (id : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) (pt r z) = pt s (if (fun _ => true) r then z else star z))\n    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        (id : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) (pt r z) = pt s (-(if (fun _ => true) r then z else star z)))",
 "ORDER": "  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  (Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))).card = 72",
 "TRANS_C": "  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ∀ r s : Fin 9, ∃ ν ∈ (Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))), (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)",
 "STAB_C": "  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ((Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))).filter (fun ν => (ν (v₁ 0) = v₁ 0 ∧ ν (v₂ 0) = v₂ 0) ∨ (ν (v₁ 0) = v₂ 0 ∧ ν (v₂ 0) = v₁ 0))).card = 8",
 "TRANS_V": "  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ∀ v w : Fin 6, ∃ ν ∈ (Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))), ν v = w",
 "STAB_V": "  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ((Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))).filter (fun ν => ν 0 = 0)).card = 12",
 "FAM_K": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → ∀ ε : Fin 9 → Bool,\n    (∀ r : Fin 9, ∃ s : Fin 9, ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s) ∨ ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if ε r then z else star z))\n    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if ε r then z else star z))) →\n    ((∃ π τ : Equiv.Perm (Fin 4),\n      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →\n          f (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => Matrix.of fun j k =>\n            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) ↔ ∀ v w : Fin 6, ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = v ∨ v₂ r = v) ∧ ε r = false)).card % 2) = ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = w ∨ v₂ r = w) ∧ ε r = false)).card % 2))",
 "FAM_COUNT": "  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  (Finset.univ.filter (fun ε : Fin 9 → Bool => ∀ v w : Fin 6, ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = v ∨ v₂ r = v) ∧ ε r = false)).card % 2) = ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = w ∨ v₂ r = w) ∧ ε r = false)).card % 2))).card = 32",
 "FAM_COSET": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ∀ (ν : Equiv.Perm (Fin 6)) (ε ε' : Fin 9 → Bool) (f f' : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) f' →\n    (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if ε r then z else star z))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if ε r then z else star z))) →\n    (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f' (pt r z) = pt s (if ε' r then z else star z))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f' (pt r z) = pt s (-(if ε' r then z else star z))) →\n    (∃ π τ : Equiv.Perm (Fin 4),\n      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →\n          f (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => Matrix.of fun j k =>\n            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) →\n    ((∃ π τ : Equiv.Perm (Fin 4),\n      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f' (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →\n          f' (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f' (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f' (featureVec G) = featureVec (fun i => Matrix.of fun j k =>\n            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) ↔ ∀ v w : Fin 6, ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = v ∨ v₂ r = v) ∧ (fun r => decide (ε r = ε' r)) r = false)).card % 2) = ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = w ∨ v₂ r = w) ∧ (fun r => decide (ε r = ε' r)) r = false)).card % 2))",
 "FAM_ONTO": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ∀ ν : Equiv.Perm (Fin 6), (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)) → ∃ (ε : Fin 9 → Bool) (f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ (∃ π τ : Equiv.Perm (Fin 4),\n      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →\n          f (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => Matrix.of fun j k =>\n            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) ∧\n    (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if ε r then z else star z))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if ε r then z else star z)))",
 "C_CONJ": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧\n    (∀ r : Fin 9, ∃ s : Fin 9, ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s) ∨ ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if (fun _ => false) r then z else star z))\n    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if (fun _ => false) r then z else star z)))",
 "C_A32": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ ¬ (∃ π τ : Equiv.Perm (Fin 4),\n      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →\n          f (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => Matrix.of fun j k =>\n            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))) ∧\n    (∀ r : Fin 9, ∃ s : Fin 9, ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s) ∨ ((1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s ∧ (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₁ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if (fun r => decide (r ≠ 0)) r then z else star z))\n    ∧ (∀ r s : Fin 9, (1 : Equiv.Perm (Fin 6)) (v₁ r) = v₂ s → (1 : Equiv.Perm (Fin 6)) (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if (fun r => decide (r ≠ 0)) r then z else star z)))",
 "C_PHASE": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  dist (pt 0 (Complex.I * Complex.I)) (pt 4 Complex.I) ≠ dist (pt 0 Complex.I) (pt 4 Complex.I)",
 "C_INCID": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n  (∀ z w : ℂ, star z * z = 1 → star w * w = 1 → 1 ≤ dist (pt 0 z) (pt 3 w))\n  ∧ pt 1 1 = pt 3 1\n  ∧ ¬ ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ f '' (pt 0 '' {z : ℂ | star z * z = 1}) = pt 1 '' {z : ℂ | star z * z = 1}\n      ∧ f '' (pt 3 '' {z : ℂ | star z * z = 1}) = pt 3 '' {z : ℂ | star z * z = 1}"
}

# ---- the shared components the propositions are built from
COMPONENTS = {
 "HEAD": "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]\n  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (fun i =>\n    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2)\n  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n",
 "FIN": "  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n",
 "UNIQ": "(∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f →\n      ∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),\n    (∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if νε.2 r then z else star z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if νε.2 r then z else star z))))",
 "REAL": "(∀ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool),\n      (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)) →\n      ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧\n    (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if ε r then z else star z))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if ε r then z else star z))))",
 "NUNIQ": "(∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧\n      ¬ ∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),\n    (∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if νε.2 r then z else star z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if νε.2 r then z else star z))))",
 "NREAL": "(∃ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool),\n      (∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)) ∧\n      ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f →\n    ¬ ((∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if ε r then z else star z))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if ε r then z else star z)))))",
 "NF_UNIQ": "(∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if νε.2 r then z else star z))\n    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if νε.2 r then z else star z)))",
 "NF_REAL": "(∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₁ s → ν (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (if ε r then z else star z))\n    ∧ (∀ r s : Fin 9, ν (v₁ r) = v₂ s → ν (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n        f (pt r z) = pt s (-(if ε r then z else star z)))",
 "EDGE": "(∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))",
 "AUT": "(Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)))",
 "FAM": "(∃ π τ : Equiv.Perm (Fin 4),\n      (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →\n          f (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))\n      ∨ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => Matrix.of fun j k =>\n            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))))",
 "PARITY": "∀ v w : Fin 6, ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = v ∨ v₂ r = v) ∧ ε r = false)).card % 2) = ((Finset.univ.filter (fun r : Fin 9 => (v₁ r = w ∨ v₂ r = w) ∧ ε r = false)).card % 2)",
 "SURJ": "IsSurjIsometryOn (normalizedSet Γ₀) f",
 "CIRC": "{z : ℂ | star z * z = 1}"
}

# ---- the theorems: (role, name, proposition key)
THEOREMS = [
 [
  "A33-CLASSIFIED",
  "a33_classified",
  "P_R"
 ],
 [
  "A33-NOT-CLASSIFIED",
  "a33_not_classified",
  "P_N"
 ],
 [
  "corollary",
  "a33_c_exclusive",
  None
 ],
 [
  "A33-1",
  "a33_shared_circles",
  "B1"
 ],
 [
  "A33-2",
  "a33_shared_form",
  "B2"
 ],
 [
  "A33-2",
  "a33_shared_signs",
  "B3"
 ],
 [
  "A33-3",
  "a33_shared_composition",
  "COMP"
 ],
 [
  "A33-3",
  "a33_shared_identity",
  "C_ID"
 ],
 [
  "A33-3",
  "a33_shared_order",
  "ORDER"
 ],
 [
  "A33-3 corollary",
  "a33_c_transitive_circles",
  "TRANS_C"
 ],
 [
  "A33-3 corollary",
  "a33_c_stabilizer_circle",
  "STAB_C"
 ],
 [
  "A33-3 corollary",
  "a33_c_transitive_points",
  "TRANS_V"
 ],
 [
  "A33-3 corollary",
  "a33_c_stabilizer_point",
  "STAB_V"
 ],
 [
  "A33-4",
  "a33_shared_family_kernel",
  "FAM_K"
 ],
 [
  "A33-4",
  "a33_shared_family_count",
  "FAM_COUNT"
 ],
 [
  "A33-4",
  "a33_shared_family_coset",
  "FAM_COSET"
 ],
 [
  "A33-4",
  "a33_shared_family_onto",
  "FAM_ONTO"
 ],
 [
  "control",
  "a33_control_conjugation",
  "C_CONJ"
 ],
 [
  "control",
  "a33_control_a32",
  "C_A32"
 ],
 [
  "control",
  "a33_control_phase",
  "C_PHASE"
 ],
 [
  "control",
  "a33_control_incidence",
  "C_INCID"
 ]
]
LABELS = [(role, nm, key) for role, nm, key in THEOREMS if role.startswith('A33-') and role[4:5].isalpha()]
COROLLARY = ('a33_c_exclusive', ['P_N'], 'P_R')
SHARED = re.compile(r'^a33_shared_[A-Za-z0-9_]+$')
UNDECIDED = 'A33-UNDECIDED'
CLASSIFIED, NOT_CLASSIFIED = 'A33-CLASSIFIED', 'A33-NOT-CLASSIFIED'
ROWS = (CLASSIFIED, NOT_CLASSIFIED, UNDECIDED)
STRUCTURAL = [(nm, key) for role, nm, key in THEOREMS if role in ('A33-1', 'A33-2', 'A33-3', 'A33-4', 'A33-3 corollary')]
CONTROLS = [(nm, key) for role, nm, key in THEOREMS if role == 'control']
REQUIRED = {CLASSIFIED: STRUCTURAL + CONTROLS, NOT_CLASSIFIED: CONTROLS, UNDECIDED: []}
OUTCOME_RE = re.compile(r'\*\*Outcome:\*\* `(A33-[A-Z-]+)`')
LABEL_RE = re.compile(r'A33-(?:NOT-CLASSIFIED|CLASSIFIED|UNDECIDED)')

SENTENCES = {
 "A33-CLASSIFIED": "At the frozen single-carrier configuration, the surjective isometries of the normalized space are classified, at evidence level 2: every such map carries each of act 26's nine relabelled Fourier circles onto one of them, acts on each circle by `w ↦ λ w` or `w ↦ λ w̄` with `λ ∈ {1, −1}` fixed by its action on the two shared points of that circle, and is determined by the automorphism it induces on the incidence graph `K₃,₃` of the six shared points together with nine independent conjugation bits; every such pair is realized, the composition law is `ε''ᵣ = ε'ᵣ · ε_{σ'(r)}`, and there are exactly `72 · 2⁹ = 36864` surjective isometries. Act 25's four-shape family is a subgroup of index 16, meeting the kernel of the incidence action exactly in the conjugation patterns whose degree parities at the six shared points are uniform. This is a classification of the isometries of the frozen mathematical object; it adopts no isometry as a symmetry, a principle or a law.",
 "A33-NOT-CLASSIFIED": "At the frozen single-carrier configuration, the classification proposition for the surjective isometries of the normalized space is false, at evidence level 2: either some surjective isometry admits no normal form over the incidence graph `K₃,₃` and nine conjugation bits or admits two, or some automorphism of the incidence graph together with some choice of conjugation bits is the normal form of no surjective isometry. The witness is exhibited in the kernel. This is a statement about the frozen space; it adopts no isometry as a symmetry, a principle or a law.",
 "A33-UNDECIDED": "Neither the classification nor its negation was obtained. The step at which the proof stopped is named, with what would settle it."
}
CLAUSE = "Act 33 classifies the surjective isometries of the frozen normalized single-carrier space, and adopts\nnone. The group obtained is the isometry group of a mathematical object, a finite union of circles\nin a Euclidean space; its elements are not thereby physical symmetries, transformation laws,\ndynamics, time reversals, antiunitary operations or principles of nature, and its order and\nstructure are facts about that object and about nothing else. A `CLASSIFIED` verdict settles that\nfrozen isometry problem, and a `NOT-CLASSIFIED` verdict exhibits its failure. Neither verdict\nselects a physical law or closes `P0`. No isometry, carrier, family, group or principle gains\nphysical status by appearing in this classification, and nothing here derives, recognises or\napproaches quantum evolution."
MENTION = 'THE CLAUSE, carried at this mention'

# ---- the `P0` cell: the end of the cell at D, and the sentence appended per decided case
P0_END_D = "At the single-carrier configuration, the positive classification proposition posed as act 25's `ISO3` is false: the map that conjugates the Fourier parameter on the Fourier circle and fixes the class of every point of the other eight relabelled Fourier circles preserves realizability, is surjective on classes and preserves the distance, and for no pair of relabellings does it satisfy any of the four shapes of act 25's family. `P0`'s threading part is untouched, no isometry of the normalized space is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle."
P0_CASE = {
 "A33-CLASSIFIED": "At the single-carrier configuration, the surjective isometries of the normalized space are classified: each permutes the nine relabelled Fourier circles by an automorphism of their incidence graph `K₃,₃` and conjugates the parameter on an arbitrary subset of the circles, 36864 in all, and act 25's four-shape family is a subgroup of index 16.",
 "A33-NOT-CLASSIFIED": "At the single-carrier configuration, the classification of the surjective isometries of the normalized space by the automorphisms of the circles' incidence graph `K₃,₃` and nine conjugation bits fails, by a witness exhibited in the kernel."
}
P0_STANDING_33 = "`P0`'s threading part is untouched, no isometry of the normalized space is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle."

CENSUS_MODULES = ['OrbitIsometryGroup']

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
    r = c['HEAD'] + '  ' + c['UNIQ'] + '\n  ∧ ' + c['REAL']
    n = c['HEAD'] + '  ' + c['NUNIQ'] + '\n  ∨ ' + c['NREAL']
    return r, n


def duality_ok(props, comps):
    """P_R is `UNIQ ∧ REAL` and P_N is `NUNIQ ∨ NREAL` over one head, where NUNIQ negates UNIQ
    (∀ f, S f → ∃! ...  against  ∃ f, S f ∧ ¬ ∃! ...) and NREAL negates REAL (∀ ν ε, E → ∃ f, S f ∧ NF
    against  ∃ ν ε, E ∧ ∀ f, S f → ¬ NF), so each verdict is the other's negation; every other
    statement carries the same normal-form, incidence, family and parity strings, verbatim."""
    f = []
    r, n = dual_texts(comps)
    if norm(props['P_R']) != norm(r):
        f.append('duality:P_R-is-not-the-frozen-conjunction')
    if norm(props['P_N']) != norm(n):
        f.append('duality:P_N-is-not-the-frozen-disjunction')
    U, NU, R, NR = (norm(comps[k]) for k in ('UNIQ', 'NUNIQ', 'REAL', 'NREAL'))
    if not (U.startswith('(∀ f :') and NU.startswith('(∃ f :') and U.count(norm(comps['NF_UNIQ'])) == 1
            and NU.count(norm(comps['NF_UNIQ'])) == 1 and '→ ∃! νε' in U and '∧ ¬ ∃! νε' in NU
            and U.replace('(∀ f :', '', 1).replace('→ ∃! νε', '', 1) == NU.replace('(∃ f :', '', 1).replace('∧ ¬ ∃! νε', '', 1)):
        f.append('duality:NUNIQ-is-not-the-negation-of-UNIQ')
    if not (R.startswith('(∀ (ν :') and NR.startswith('(∃ (ν :') and R.count(norm(comps['NF_REAL'])) == 1
            and NR.count(norm(comps['NF_REAL'])) == 1 and R.count(norm(comps['EDGE']) + ' → ∃ f :') == 1
            and NR.count(norm(comps['EDGE']) + ' ∧ ∀ f :') == 1
            and R.endswith(norm(comps['SURJ']) + ' ∧ ' + norm(comps['NF_REAL']) + ')')
            and NR.endswith(norm(comps['SURJ']) + ' → ¬ (' + norm(comps['NF_REAL']) + '))')):
        f.append('duality:NREAL-is-not-the-negation-of-REAL')
    for key, comp, k in (('B1', 'HEAD', 1), ('B2', 'HEAD', 1), ('B3', 'HEAD', 1), ('COMP', 'HEAD', 1),
                         ('C_ID', 'HEAD', 1), ('FAM_K', 'HEAD', 1), ('FAM_COSET', 'HEAD', 1), ('FAM_ONTO', 'HEAD', 1),
                         ('C_CONJ', 'HEAD', 1), ('C_A32', 'HEAD', 1), ('C_PHASE', 'HEAD', 1), ('C_INCID', 'HEAD', 1),
                         ('ORDER', 'FIN', 1), ('TRANS_C', 'FIN', 1), ('STAB_C', 'FIN', 1), ('TRANS_V', 'FIN', 1),
                         ('STAB_V', 'FIN', 1), ('FAM_COUNT', 'FIN', 1),
                         ('COMP', 'NF_REAL', 1), ('FAM_COSET', 'NF_REAL', 1), ('FAM_ONTO', 'NF_REAL', 1),
                         ('FAM_ONTO', 'EDGE', 2), ('ORDER', 'AUT', 1), ('TRANS_C', 'AUT', 1), ('STAB_C', 'AUT', 1),
                         ('TRANS_V', 'AUT', 1), ('STAB_V', 'AUT', 1),
                         ('FAM_K', 'FAM', 1), ('FAM_COSET', 'FAM', 1), ('FAM_ONTO', 'FAM', 1), ('C_A32', 'FAM', 1),
                         ('FAM_K', 'PARITY', 1), ('FAM_COUNT', 'PARITY', 1),
                         ('B1', 'CIRC', 2), ('B2', 'CIRC', 2), ('C_INCID', 'CIRC', 4),
                         ('B1', 'SURJ', 1), ('B2', 'SURJ', 1), ('B3', 'SURJ', 1), ('FAM_K', 'SURJ', 1),
                         ('C_CONJ', 'SURJ', 1), ('C_A32', 'SURJ', 1), ('C_INCID', 'SURJ', 1), ('FAM_ONTO', 'SURJ', 1)):
        if norm(props[key]).count(norm(comps[comp])) != k:
            f.append('source:%s-does-not-carry-%s' % (key, comp))
    if norm(comps['AUT']) != '(Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ' + norm(comps['EDGE'])[1:-1] + '))':
        f.append('source:AUT-is-not-the-incidence-condition')
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
    names = {x[1] for x in LABELS} | {COROLLARY[0]} | {x[0] for x in STRUCTURAL + CONTROLS}
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
    for nm, key in STRUCTURAL + CONTROLS:
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
    return road_d.replace(old, ' ' + P0_END_D + ' ' + P0_CASE[label] + ' ' + P0_STANDING_33 + ' |', 1)


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
    th('a33_shared_x', 'True')
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
    road = '| **P0** | q | x | Act 25 a. Act 32 b. ' + P0_END_D + ' | y |\n'
    cen = json.dumps({'families': [{'name': 'x', 'modules': ['X'], 'status': 'kernel-only',
                                    'manuscript': [], 'note': 'n'}]},
                     indent=2, ensure_ascii=False) + '\n'
    return {ROADMAP: road, CENSUS: cen, ROOT: 'import A\n' + WIRE_AFTER + 'import B\n', GUARD: '# guard\n'}


def _synthetic_e(fd, label):
    fe = {MODULE: _module(label), RDIR + 'result.md': _note(label),
          ROADMAP: expected_roadmap(fd[ROADMAP], label), GUARD: fd[GUARD]}
    c = json.loads(fd[CENSUS])
    c['families'].append({'name': 'act 33', 'modules': CENSUS_MODULES,
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
                                               ('standing-33', P0_STANDING_33)] + list(P0_CASE.items()):
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
            ('P_R-uniqueness-weakened', 'P_R', '∃! νε', '∃ νε'),
            ('P_R-realization-dropped', 'P_R', '\n  ∧ (∀ (ν : Equiv.Perm (Fin 6))', '\n  ∧ True ∧ (∀ (ν : Equiv.Perm (Fin 6))'),
            ('P_N-negation-dropped', 'P_N', '¬ ∃! νε', '∃! νε'),
            ('P_N-conjunction', 'P_N', '\n  ∨ (∃ (ν :', '\n  ∧ (∃ (ν :'),
            ('P_N-realization-negation-dropped', 'P_N', '→\n    ¬ (' + COMPONENTS['NF_REAL'] + '))', '→\n    (' + COMPONENTS['NF_REAL'] + '))'),
            ('FAM_K-parity-drift', 'FAM_K', '∧ ε r = false)).card % 2)', '∧ ε r = true)).card % 2)')):
        props = dict(PROPS)
        if props[key].count(old) < 1:
            bad.append('duality mutation %s: pattern absent' % nm)
            continue
        props[key] = props[key].replace(old, new, 1)
        dmuts += 1
        if not duality_ok(props, COMPONENTS):
            bad.append('duality mutation %s: accepted' % nm)
    comps = dict(COMPONENTS, EDGE=COMPONENTS['EDGE'].replace('ν (v₂ r) = v₂ s', 'ν (v₂ r) = v₁ s', 1))
    dmuts += 1
    if not duality_ok(PROPS, comps):
        bad.append('duality mutation component-drift: accepted')

    fd = _synthetic_d()
    for label in ROWS:
        fe, delta = _synthetic_e(fd, label)
        r = check_all(fd, fe, delta)
        if r:
            bad.append('positive %s: %s' % (label, r))
    CL, NC, X = ROWS
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
    mut('definition-added', CL, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'noncomputable def zz := 1\n' + E_)}), dl), 'module:forbidden-command')
    mut('variable-added', CL, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a33_shared_x', '\nvariable (h : False)\ntheorem a33_shared_x')}), dl),
        'module:forbidden-command')
    mut('second-open', CL, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a33_shared_x', '\nopen Classical in\ntheorem a33_shared_x')}), dl), 'module:open')
    mut('second-import', CL, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '/-! synthetic -/', 'import Mathlib.GroupTheory.SemidirectProduct\n/-! synthetic -/')}), dl),
        'module:forbidden-command')
    mut('sorry', CL, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('exact test', 'sorry', 1)}), dl),
        'module:forbidden-token')
    mut('native-decide', CL, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('exact test', 'native_decide', 1)}), dl),
        'module:forbidden-token')
    mut('print-axioms-dropped', CL, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '#print axioms a33_classified\n', '')}), dl), 'module:no-print-axioms')
    mut('stray-theorem-name', CL, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'theorem a33_n : True := trivial\n#print axioms a33_n\n' + E_)}), dl),
        'module:theorem-name-outside')
    mut('classified-uniqueness-weakened', CL, modstmt(CL, 'a33_classified', PROPS['P_R'].replace(
        '∃! νε', '∃ νε', 1)), 'module:statement-not-frozen:a33_classified')
    mut('not-classified-weakened', NC, modstmt(NC, 'a33_not_classified', PROPS['P_N'].replace(
        '¬ ∃! νε', '∃! νε', 1)), 'module:statement-not-frozen:a33_not_classified')
    mut('circles-into-not-onto', CL, modstmt(CL, 'a33_shared_circles', PROPS['B1'].replace(
        "= pt s '' {z : ℂ | star z * z = 1}", "⊆ pt s '' {z : ℂ | star z * z = 1}", 1)),
        'module:statement-not-frozen:a33_shared_circles')
    mut('signs-weakened', CL, modstmt(CL, 'a33_shared_signs', PROPS['B3'].replace(
        'l r = 1 ∨ l r = -1', 'star (l r) * l r = 1', 1)), 'module:statement-not-frozen:a33_shared_signs')
    mut('a32-witness-inside-family', CL, modstmt(CL, 'a33_control_a32', PROPS['C_A32'].replace(
        '∧ ¬ (∃ π τ', '∧ (∃ π τ', 1)), 'module:statement-not-frozen:a33_control_a32')
    mut('composition-law-drift', CL, modstmt(CL, 'a33_shared_composition', PROPS['COMP'].replace(
        "ε'' r = decide (ε' r = ε s)", "ε'' r = decide (ε' r = ε r)", 1)), 'module:statement-not-frozen:a33_shared_composition')
    mut('order-altered', CL, modstmt(CL, 'a33_shared_order', PROPS['ORDER'].replace('= 72', '= 36', 1)),
        'module:statement-not-frozen:a33_shared_order')
    mut('family-count-altered', CL, modstmt(CL, 'a33_shared_family_count', PROPS['FAM_COUNT'].replace('= 32', '= 64', 1)),
        'module:statement-not-frozen:a33_shared_family_count')
    mut('phase-control-trivialized', NC, modstmt(NC, 'a33_control_phase', PROPS['C_PHASE'].replace('≠', '=', 1)),
        'module:statement-not-frozen:a33_control_phase')
    mut('incidence-bound-weakened', NC, modstmt(NC, 'a33_control_incidence', PROPS['C_INCID'].replace(
        '1 ≤ dist', '0 ≤ dist', 1)), 'module:statement-not-frozen:a33_control_incidence')
    for nm, _ in REQUIRED[CL]:
        mut('required-absent:' + nm, CL, lambda fe, dl, nm=nm: (dict(fe, **{MODULE: _module(CL, drop=(nm,))}), dl),
            'module:required-statement-absent:' + nm)
    for nm, _ in REQUIRED[NC]:
        mut('required-absent-not-classified:' + nm, NC, lambda fe, dl, nm=nm: (dict(fe, **{MODULE: _module(NC, drop=(nm,))}), dl),
            'module:required-statement-absent:' + nm)
    mut('corollary-absent', X, lambda fe, dl: (dict(fe, **{MODULE: _module(X, drop=('a33_c_exclusive',))}), dl),
        'module:required-corollary-absent')
    mut('corollary-altered', X, lambda fe, dl: (dict(fe, **{MODULE: _module(
        X, stmt={'a33_c_exclusive': corollary_statement()[2:].replace('→ ¬ (', '→ (', 1)})}), dl),
        'module:statement-not-frozen:a33_c_exclusive')
    mut('both-labels', CL, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'theorem a33_not_classified :\n    ' + PROPS['P_N'] + ' := by\n  exact test\n'
        '#print axioms a33_not_classified\n' + E_)}), dl), 'module:both-labels')
    mut('note-outcome-mismatch', CL, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '**Outcome:** `A33-CLASSIFIED`', '**Outcome:** `A33-NOT-CLASSIFIED`')}), dl), 'note:outcome-line')
    mut('note-second-outcome', CL, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n**Outcome:** `A33-CLASSIFIED`\n'}), dl), 'note:outcome-line')
    mut('note-sentence-altered', CL, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        'evidence level 2', 'evidence level 3', 1)}), dl), 'note:frozen-sentence')
    mut('note-unearned-sentence', X, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + SENTENCES[CL] + '\n'}), dl), 'note:sentence-of-a-label-not-earned')
    mut('note-clause-twice', CL, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + CLAUSE + '\n'}), dl), 'note:the-clause')
    mut('note-clause-detached', CL, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        ' — the result note.**\n', ' — the result note.**\n' + 'x ' * 60 + '\n', 1)}), dl), 'note:the-clause')
    mut('note-control-unnamed', CL, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a33_control_phase`', 'x')}), dl), 'note:required-statement-not-named')
    mut('note-structural-unnamed', CL, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a33_shared_circles`', 'x')}), dl), 'note:required-statement-not-named')
    mut('roadmap-wrong-case', CL, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(fd[ROADMAP], NC)}), dl),
        'roadmap:')
    mut('roadmap-standing-dropped', CL, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        P0_CASE[CL] + ' ' + P0_STANDING_33, P0_CASE[CL])}), dl), 'roadmap:')
    mut('roadmap-sentence-misplaced', CL, lambda fe, dl: (dict(fe, **{ROADMAP: fd[ROADMAP].replace(
        ' Act 25 a.', ' Act 25 a. ' + P0_CASE[CL] + ' ' + P0_STANDING_33, 1)}), dl), 'roadmap:')
    mut('roadmap-touched-when-undecided', X, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(fd[ROADMAP], CL)}),
        dict(dl, **{ROADMAP: 'M'})), 'roadmap:')
    mut('guard-one-byte', CL, lambda fe, dl: (dict(fe, **{GUARD: fe[GUARD] + ' '}), dict(dl, **{GUARD: 'M'})), 'guard:')
    mut('census-status-promoted', CL, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"status": "kernel-only",\n      "manuscript": [],\n      "note": "Outcome',
        '"status": "manuscript-cited",\n      "manuscript": [],\n      "note": "Outcome')}), dl),
        'census:family-disposition')
    mut('census-other-entry-changed', CL, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"note": "n"', '"note": "m"')}), dl), 'census:another-entry-changed')
    mut('census-outcome-wrong', CL, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        'A33-CLASSIFIED.', 'A33-NOT-CLASSIFIED.')}), dl), 'census:outcome')
    mut('census-entry-absent', CL, lambda fe, dl: (dict(fe, **{CENSUS: fd[CENSUS]}), dl), 'census:family-count-or-place')
    mut('wire-absent', CL, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT]}), dl), 'wire:')
    mut('wire-misplaced', CL, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT] + WIRE}), dl), 'wire:')
    mut('path-extra', CL, lambda fe, dl: (fe, dict(dl, **{'papers/SM.md': 'M'})), 'paths:')
    mut('path-missing-note', CL, lambda fe, dl: (fe, dict((k, v) for k, v in dl.items()
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
