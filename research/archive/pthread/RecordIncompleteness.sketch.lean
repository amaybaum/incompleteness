/-
  UNCOMPILED SKETCH (Thread P, read-only research). Not kernel-checked. No toolchain was run.
  Stated over the landed types of KInfFoundations / OrbitGeneration / TransitiveBody / EffectSpace /
  SharpTests / K2Guard at base 06b6f94e. Names are illustrative. Proof bodies are plans (`sorry`).

  Candidate premise P (best ranked): RECORD INCOMPLETENESS — no single readout's record, followed by
  re-preparation from the record, returns every state of the body.  Field-neutral, no ball, no
  Hilbert space, no matrix, no dimension.  Its instrument-level strengthening is passive
  incompleteness (`PassivelyIncompleteBody`), the field-neutral form of PassiveObservation's
  `no_complete_passive_observation`.
-/
import OIBridge.SharpTests
import OIBridge.K2Guard

namespace OIBridge
namespace PThread

open Set KInfFoundations OrbitGeneration TransitiveBody EffectSpace SharpTests K1Bridge

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {d : ℕ}

/-! ### Definitions (observer vocabulary only) -/

/-- A readout with re-preparation that reconstructs: outcome effects `e i` (available, effects on
`Ω`, summing to one on `Ω`) and re-prepared states `y i ∈ Ω`, such that re-preparing from the record
returns every state on average. -/
def ReconstructingRecord (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∃ (k : ℕ) (e : Fin k → V →ᵃ[ℝ] ℝ) (y : Fin k → V),
    (∀ i, e i ∈ avail) ∧ (∀ i, IsEffectOn Ω (e i)) ∧ (∀ i, y i ∈ Ω) ∧
    (∀ x ∈ Ω, ∑ i, e i x = 1) ∧ (∀ x ∈ Ω, ∑ i, e i x • y i = x)

/-- **P (record incompleteness).** No available readout's record reconstructs the state. -/
def RecordIncomplete (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ¬ ReconstructingRecord Ω avail

/-- A finite readout with unnormalised branches `b i` (the homogeneous pair `(e i, b i)`): each branch
lands in the cone over `Ω`; the branches sum to the identity on `Ω` (passive: observe-and-forget is
idle). -/
structure PassiveReadout (Ω : Set V) (k : ℕ) where
  e : Fin k → V →ᵃ[ℝ] ℝ
  b : Fin k → V →ᵃ[ℝ] V
  eff : ∀ i, IsEffectOn Ω (e i)
  total : ∀ x ∈ Ω, ∑ i, e i x = 1
  branch : ∀ i, ∀ x ∈ Ω, ∃ y ∈ Ω, b i x = e i x • y
  passive : ∀ x ∈ Ω, ∑ i, b i x = x

def PassiveReadout.Separates {Ω : Set V} {k : ℕ} (R : PassiveReadout Ω k) : Prop :=
  ∀ x ∈ Ω, ∀ x' ∈ Ω, (∀ i, R.e i x = R.e i x') → x = x'

/-- **PI, passive incompleteness of a body**: no passive readout separates its states. -/
def PassivelyIncompleteBody (Ω : Set V) : Prop :=
  ∀ (k : ℕ) (R : PassiveReadout Ω k), ¬ R.Separates

/-- **NIWD**: every passive readout is uninformative (each outcome law constant on `Ω`). -/
def NoInfoWithoutDisturbance (Ω : Set V) : Prop :=
  ∀ (k : ℕ) (R : PassiveReadout Ω k) (i : Fin k), ∃ c : ℝ, ∀ x ∈ Ω, R.e i x = c

/-! ### General-body relations (proof plans) -/

/-- A reconstructing record is a passive separating readout (measure-and-prepare branches
`b i x = e i x • y i`).  Hence PI → record incompleteness, on every body. -/
theorem recordIncomplete_of_passivelyIncomplete {Ω : Set V} (h : PassivelyIncompleteBody Ω) :
    RecordIncomplete Ω (fullEffects Ω) := by
  -- from ⟨k, e, y, -, he, hy, hsum, hrec⟩ build R with b i := (e i).smulRight-like affine map x ↦ e i x • y i;
  -- R.passive is hrec; R.Separates: x = ∑ e i x • y i = ∑ e i x' • y i = x'.
  sorry

/-- NIWD with two distinct states gives PI. -/
theorem passivelyIncomplete_of_niwd {Ω : Set V} (h : NoInfoWithoutDisturbance Ω)
    (h2 : ∃ x ∈ Ω, ∃ x' ∈ Ω, x ≠ x') : PassivelyIncompleteBody Ω := by
  -- the outcome laws are constant, so the two distinct states have equal laws.
  sorry

/-! ### On `eball d` -/

/-- Strict convexity at the sphere, the one geometric lemma: a convex combination of ball points equal
to a unit vector has every positively weighted point equal to it. -/
theorem eq_of_combo_sphere {k : ℕ} {w : Fin k → ℝ} {y : Fin k → Fin d → ℝ} {u : Fin d → ℝ}
    (hu : ∑ j, u j ^ 2 = 1) (hy : ∀ i, y i ∈ eball d) (hw : ∀ i, 0 ≤ w i) (hw1 : ∑ i, w i = 1)
    (hc : ∑ i, w i • y i = u) : ∀ i, 0 < w i → y i = u := by
  -- ⟨u, ∑ w i y i⟩ = 1 and ⟨u, y i⟩ ≤ (|u|² + |y i|²)/2 ≤ 1, so ⟨u, y i⟩ = 1 when w i > 0;
  -- then ∑ (y i j - u j)² = |y i|² - 2 + 1 ≤ 0.
  sorry

/-- d = 0: the unit readout with the single state reconstructs. -/
theorem reconstructingRecord_zero : ReconstructingRecord (eball 0) (fullEffects (eball 0)) := by
  -- k = 1, e 0 = const 1, y 0 = 0; every x : Fin 0 → ℝ is 0 (Subsingleton).
  sorry

/-- d = 1: the sharp test along z1 and its complement, with re-preparation of ±z1, reconstruct. -/
theorem reconstructingRecord_one :
    ReconstructingRecord (eball 1) {sharpEff z1, sharpEff (-z1)} := by
  -- e = ![sharpEff z1, sharpEff (-z1)], y = ![z1, -z1]; sums by sharpEff_neg_apply;
  -- (1/2 + x0/2) • z1 + (1/2 - x0/2) • (-z1) = x (Fin.sum_univ_one, funext).
  sorry

/-- d ≥ 2: no readout of the ball reconstructs.  Witness points ±e₀, ±e₁ only. -/
theorem not_reconstructingRecord_of_two_le (hd : 2 ≤ d) :
    ¬ ReconstructingRecord (eball d) (fullEffects (eball d)) := by
  -- u = Pi.single 0 1, v = Pi.single 1 1. By eq_of_combo_sphere at u, v, -v (weights e i ·):
  -- e i u > 0 → y i = u ≠ ±v → e i v = e i (-v) = 0 → e i 0 = 0 (affine_combo, midpoint)
  -- → e i (-u) = - e i u < 0, contradicting IsEffectOn.  So e i u = 0 for all i, contradicting ∑ = 1.
  sorry

/-- **The ball classification** (two directions, separate witnesses, §A.34):
(→) `reconstructingRecord_zero`, `reconstructingRecord_one` (monotone in `avail`);
(←) `not_reconstructingRecord_of_two_le`. -/
theorem recordIncomplete_eball_iff :
    RecordIncomplete (eball d) (fullEffects (eball d)) ↔ 2 ≤ d := by
  sorry

theorem hasTwoSharpTests_of_recordIncomplete
    (h : RecordIncomplete (eball d) (fullEffects (eball d))) : HasTwoSharpTests (eball d) :=
  hasTwoSharpTests_iff.2 (recordIncomplete_eball_iff.1 h)

/-- **Relative form, with the selector's landed hypotheses**: only the seed and its transports need be
available.  d = 0: `not_sharpSeed_zero`.  d = 1: the seed is `sharpEff (±z1)`; boundary transitivity
moves its certain state u to -u; the transported seed is available (V4), is a sharp seed
(`sharpSeed_seedTransport`), is certain at -u, hence by `eq_or_compl_one` equals `1 - r` on the
states; `![r, f]` with `![u, -u]` reconstructs, contradicting `h`. -/
theorem two_le_of_recordIncomplete {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}
    {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}
    (hE : EffectsOn (eball d) avail) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    (h : RecordIncomplete (eball d) avail) : 2 ≤ d := by
  sorry

/-- Composition with K2-GUARD-1: record incompleteness in place of `2 ≤ d` selects three. -/
theorem three_of_recordIncomplete {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}
    {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}
    (hE : EffectsOn (eball d) avail) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : CompositeDimension.W d ≃ₗ[ℝ] _}
    (hN : CompositeDimension.IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T)
    (h : RecordIncomplete (eball d) avail) : d = 3 :=
  K2Guard.three_of_nativeGateOf_of_two_le (two_le_of_recordIncomplete hE hG hP1 hK hV4 h)
    hE hG hP1 hK hV4 hN hT

/-! ### Controls -/

/-- The d = 1 relative countermodel of `two_le_load_bearing_relative` violates P. -/
theorem not_recordIncomplete_one : ¬ RecordIncomplete (eball 1) (fullEffects (eball 1)) := by
  sorry -- reconstructingRecord_one, monotone in avail (both sharp effects are effects)

/-- Non-relabeling witness: on the classical trit `simplex 3` (KInfFoundations:889) two sharp tests
distinct modulo complementation exist, and the barycentric record reconstructs. So
`HasTwoSharpTests` does not imply P on a general body. -/
theorem trit_separates :
    HasTwoSharpTests (simplex 3) ∧ ReconstructingRecord (simplex 3) (fullEffects (simplex 3)) := by
  -- HTST: e = coordinate 2, f = coordinate 1 (affine projections, sharp seeds on the simplex);
  -- at x = Pi.single 2 1: f = 0 ≠ 1 = e; at x = Pi.single 0 1: f = 0 ≠ 1 = 1 - e  (exact P1 witness).
  -- (d=1 step of two_le_of_recordIncomplete uses seedTransport_apply_apply: f (g u) = r u = 1 with g u = -u.)
  -- Record: e i x = x i, y i = Pi.single i 1; ∑ x i = 1 and ∑ x i • Pi.single i 1 = x on the simplex.
  sorry

/-! ### NIWD on the ball (needs the seed to exclude d = 0) -/

theorem niwd_eball_of_two_le (hd : 2 ≤ d) : NoInfoWithoutDisturbance (eball d) := by
  -- at a unit x, eq_of_combo_sphere on ∑ b i x = x gives b i x = e i x • x.  With ±e_j:
  -- b i 0 = (e i e_j - e i (-e_j))/2 • e_j for every j; two different axes force e i e_j = e i (-e_j);
  -- so the linear part of e i vanishes on every axis: e i is constant.
  sorry

theorem not_niwd_one : ¬ NoInfoWithoutDisturbance (eball 1) := by
  sorry -- the measure-and-prepare readout along sharpEff z1 is passive and informative

end PThread
end OIBridge
