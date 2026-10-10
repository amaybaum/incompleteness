import OIBridge.DitaTorus

/-!
# Act 40 — the Diţă locus of the three-parameter family: the kernel layer

Act 39 proved the family `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point
`SIG = F₄(z) ⊗ F₄(w)`, `z = (3+4i)/5`, `w = (5+12i)/13`, realizable at every point of the three-torus. This
module states the kernel layer of act 40's classification of the points of the torus at which `H3` admits a
Diţă structure. On each of the five coordinate faces `u₁ = 1`, `u₁ = −1`, `u₂ = 1`, `u₃ = 1`, `u₃ = −1`, and at
every point of the face, `H3` (or its transpose) is an explicit strict Diţă product `dita X Y D` of a named shape
and index map, with `X` and every `Y c` flat unitary and `‖D c b‖ = 1`. For each of twenty named index maps — act
37's nine classes in both orientations and act 38's two maps `M_COL` and `M_ROW` — a strict Diţă form of `H3` at
that map forces the named coordinate equations. The module does not state that the five faces exhaust the
points admitting a Diţă structure: that converse, over every shape, index map and orientation and up to
diagonal equivalence, is certified by the round's exact-computation probe, not by the kernel.

The module carries no definition. Every theorem prints its axioms.
-/

namespace OIBridge
namespace DitaTorusLocus

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity OrbitIsometryGroup ProductStratum DitaHull DitaHierarchy DitaArcExclusivity DitaLocalEscape DitaTorus

-- A40-LOCUS-CLASSIFIED, `a40_locus_kernel`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 1 u₂ u₃ = ditat2 X Y D)
  ∧ (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 (-1) u₂ u₃ = ditamc X Y D)
  ∧ (∀ u₁ u₃ : ℂ, star u₁ * u₁ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ 1 u₃ = dita28 X Y D)
  ∧ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ 1 = (dita28 X Y D)ᵀ)
  ∧ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ (-1) = (ditamr X Y D)ᵀ)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak1 X Y D)ᵀ) → u₁ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak2 X Y D) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak2 X Y D)ᵀ) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak3 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak3 X Y D)ᵀ) → u₁ = 1 ∧ u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak4 X Y D) → u₁ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak4 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae1 X Y D)ᵀ) → u₁ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae2 X Y D) → u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae2 X Y D)ᵀ) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = dita28 X Y D) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (dita28 X Y D)ᵀ) → u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat2 X Y D) → u₁ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat2 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat3 X Y D) → u₁ = 1 ∧ u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat3 X Y D)ᵀ) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditamc X Y D) → u₁ = -1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditamr X Y D)ᵀ) → u₃ = -1))

-- A40-LOCUS-FAILS, `a40_not_locus_kernel`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ¬ (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 1 u₂ u₃ = ditat2 X Y D)
  ∨ ¬ (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 (-1) u₂ u₃ = ditamc X Y D)
  ∨ ¬ (∀ u₁ u₃ : ℂ, star u₁ * u₁ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ 1 u₃ = dita28 X Y D)
  ∨ ¬ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ 1 = (dita28 X Y D)ᵀ)
  ∨ ¬ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ (-1) = (ditamr X Y D)ᵀ)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak1 X Y D)ᵀ) → u₁ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak2 X Y D) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak2 X Y D)ᵀ) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak3 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak3 X Y D)ᵀ) → u₁ = 1 ∧ u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak4 X Y D) → u₁ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak4 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae1 X Y D)ᵀ) → u₁ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae2 X Y D) → u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae2 X Y D)ᵀ) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = dita28 X Y D) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (dita28 X Y D)ᵀ) → u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat2 X Y D) → u₁ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat2 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat3 X Y D) → u₁ = 1 ∧ u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat3 X Y D)ᵀ) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditamc X Y D) → u₁ = -1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditamr X Y D)ᵀ) → u₃ = -1))

-- A40-1, `a40_shared_face_1p`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 1 u₂ u₃ = ditat2 X Y D)

-- A40-1, `a40_shared_face_1m`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 (-1) u₂ u₃ = ditamc X Y D)

-- A40-1, `a40_shared_face_2p`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₃ : ℂ, star u₁ * u₁ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ 1 u₃ = dita28 X Y D)

-- A40-1, `a40_shared_face_3p`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ 1 = (dita28 X Y D)ᵀ)

-- A40-1, `a40_shared_face_3m`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ (-1) = (ditamr X Y D)ᵀ)

-- A40-2, `a40_shared_excl_k1_c`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak1 X Y D) → u₂ = 1 ∧ u₃ = 1)

-- A40-2, `a40_shared_excl_k1_r`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak1 X Y D)ᵀ) → u₁ = 1 ∧ u₃ = 1)

-- A40-2, `a40_shared_excl_k2_c`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak2 X Y D) → u₂ = 1)

-- A40-2, `a40_shared_excl_k2_r`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak2 X Y D)ᵀ) → u₂ = 1)

-- A40-2, `a40_shared_excl_k3_c`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak3 X Y D) → u₂ = 1 ∧ u₃ = 1)

-- A40-2, `a40_shared_excl_k3_r`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak3 X Y D)ᵀ) → u₁ = 1 ∧ u₂ = 1 ∧ u₃ = 1)

-- A40-2, `a40_shared_excl_k4_c`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak4 X Y D) → u₁ = 1 ∧ u₃ = 1)

-- A40-2, `a40_shared_excl_k4_r`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak4 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)

-- A40-2, `a40_shared_excl_e1_c`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae1 X Y D) → u₂ = 1 ∧ u₃ = 1)

-- A40-2, `a40_shared_excl_e1_r`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae1 X Y D)ᵀ) → u₁ = 1)

-- A40-2, `a40_shared_excl_e2_c`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae2 X Y D) → u₃ = 1)

-- A40-2, `a40_shared_excl_e2_r`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae2 X Y D)ᵀ) → u₂ = 1)

-- A40-2, `a40_shared_excl_t1_c`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = dita28 X Y D) → u₂ = 1)

-- A40-2, `a40_shared_excl_t1_r`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (dita28 X Y D)ᵀ) → u₃ = 1)

-- A40-2, `a40_shared_excl_t2_c`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat2 X Y D) → u₁ = 1)

-- A40-2, `a40_shared_excl_t2_r`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat2 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)

-- A40-2, `a40_shared_excl_t3_c`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat3 X Y D) → u₁ = 1 ∧ u₂ = 1)

-- A40-2, `a40_shared_excl_t3_r`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat3 X Y D)ᵀ) → u₂ = 1)

-- A40-2, `a40_shared_excl_mc_c`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditamc X Y D) → u₁ = -1)

-- A40-2, `a40_shared_excl_mr_r`
#check (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditamr X Y D)ᵀ) → u₃ = -1)

-- corollary
#check ((∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ¬ (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 1 u₂ u₃ = ditat2 X Y D)
  ∨ ¬ (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 (-1) u₂ u₃ = ditamc X Y D)
  ∨ ¬ (∀ u₁ u₃ : ℂ, star u₁ * u₁ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ 1 u₃ = dita28 X Y D)
  ∨ ¬ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ 1 = (dita28 X Y D)ᵀ)
  ∨ ¬ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ (-1) = (ditamr X Y D)ᵀ)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak1 X Y D)ᵀ) → u₁ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak2 X Y D) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak2 X Y D)ᵀ) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak3 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak3 X Y D)ᵀ) → u₁ = 1 ∧ u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak4 X Y D) → u₁ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak4 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae1 X Y D)ᵀ) → u₁ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae2 X Y D) → u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae2 X Y D)ᵀ) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = dita28 X Y D) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (dita28 X Y D)ᵀ) → u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat2 X Y D) → u₁ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat2 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat3 X Y D) → u₁ = 1 ∧ u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat3 X Y D)ᵀ) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditamc X Y D) → u₁ = -1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditamr X Y D)ᵀ) → u₃ = -1)) → ¬ (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 1 u₂ u₃ = ditat2 X Y D)
  ∧ (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 (-1) u₂ u₃ = ditamc X Y D)
  ∧ (∀ u₁ u₃ : ℂ, star u₁ * u₁ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ 1 u₃ = dita28 X Y D)
  ∧ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ 1 = (dita28 X Y D)ᵀ)
  ∧ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ (-1) = (ditamr X Y D)ᵀ)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak1 X Y D)ᵀ) → u₁ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak2 X Y D) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak2 X Y D)ᵀ) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak3 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak3 X Y D)ᵀ) → u₁ = 1 ∧ u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak4 X Y D) → u₁ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak4 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae1 X Y D)ᵀ) → u₁ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae2 X Y D) → u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae2 X Y D)ᵀ) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = dita28 X Y D) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (dita28 X Y D)ᵀ) → u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat2 X Y D) → u₁ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat2 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat3 X Y D) → u₁ = 1 ∧ u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat3 X Y D)ᵀ) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditamc X Y D) → u₁ = -1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditamr X Y D)ᵀ) → u₃ = -1)))

end DitaTorusLocus
end OIBridge
