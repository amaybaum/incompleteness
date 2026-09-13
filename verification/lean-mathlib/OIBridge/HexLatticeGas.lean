import OIBridge.HydroSourceAudit

/-!
# Hydrodynamics round H-B — a reversible streaming-and-collision substratum

Executed under the frozen control plane
`verification/programmes/hydrodynamics/round-h-b-reversible-fluid-substratum/preregistration.md`,
blob `37cc9dae301ee10d55adb73b296aa2fc7d0578e3`, from `main` at
`8de0478ef31fe4cabcf89fc5787f80f38376a957` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base.

## The candidate

One candidate, frozen: a lattice gas on the `L × L` periodic lattice `Fin 2 → ZMod L`, read in the
hexagonal basis, with six channels per site and Boolean occupation `Fin 6 → ZMod 2`. The six
lattice directions are `hexDir`, with `c_{k+3} = −c_k`; the on-site collision `hexCollide` is a
permutation of the 64 local states moving exactly five — the head-on pairs `{0, 3} ↦ {1, 4} ↦
{2, 5} ↦ {0, 3}` and the three-body pair `{0, 2, 4} ↔ {1, 3, 5}` — written as a product of three
transpositions, so its inverse is explicit; `hexStream` moves the particle of channel `k` one step
along `c_k`; the gas is `hexGas := hexStream ∘ (sitewise hexCollide)`, collide then stream. The
kernel's `Substratum` interface is consumed **unmodified**: `hexSubstratum L` is the second-order
rule `F c := hexGas c + hexGas.symm c` with neighbourhood `{i + c_k}`, whose phase-space map
`leap F : (p, c) ↦ (c, F c − p)` is a bijection by the interface's own theorem. On the **graph
sector** `Γ := {x | prevOf x = hexGas.symm (curOf x)}` the map carries `Γ` to `Γ` and acts as
`hexGas`; **every conservation statement below is a statement on `Γ`**, and off `Γ` the map
conserves nothing this round names (`hexSubstratum_mass_not_conserved_off_sector`).

`hexSum A w c := Σ_{i ∈ A} Σ_k (c i k).val · w k` is the channel-weighted total; mass is
`hexSum univ 1`, momentum in lattice coordinates is `hexSum univ (k ↦ hexDir k j)`, block charges
are `hexSum β w` over the blocks of the partition into `b × b` squares. `hexMoment4` is the fourth
moment of the six embedded unit vectors `u_k = (c_k)₁ a₁ + (c_k)₂ a₂`, `a₁ = (1, 0)`,
`a₂ = (1/2, √3/2)`. `hexRot` is the `60°` lattice rotation `ρ (a, b) = (−b, a + b)` acting on
configurations, `(ρ·c) (ρ i) (k + 1) = c i k`.

## The targets, and what each is read as

* **`HB0` — the A-profile, and the sector** (Sections B, D). `hexSubstratum L` satisfies `A1`,
  `A2`, `A3 6` and `A4Exact` (`hexSubstratum_A1`, `hexSubstratum_A2`, `hexSubstratum_A3`,
  `hexSubstratum_A4Exact`, with `hexSubstratum_A4` the gauge form `A4 ⊥`), and **fails `A5` by
  construction**: for the witness `c` = one particle in channel `0` at the origin, `c'` = one in
  channel `3` at the origin, `F (c + c')` has a particle in channel `1` at the site `c₁` and
  `F c + F c'` does not (`hexSubstratum_A5_witness`, `hexSubstratum_not_A5`), for every `L ≥ 1`. The
  sector `Γ` is invariant and the sector dynamics is exactly the gas (`hexSubstratum_sector`);
  off `Γ` mass is not conserved (`hexSubstratum_mass_not_conserved_off_sector`). **Reported
  status for the advection obligation: HO for the candidate** — H-A's linearity gate has `A5` as
  its hypothesis and does not apply here, which lifts H-A's `H0` obstruction for this candidate
  and establishes nothing positive: non-additivity is necessary for an advective term and not
  sufficient, and no coarse description carrying one is exhibited or claimed.
* **`HB1` — exact conservation, and the invariance principle** (Section C). Streaming preserves
  every channel-weighted total (`hexSum_hexStream`); the collision preserves the total with weight
  `w` on every local state **iff** `w₀ + w₃ = w₁ + w₄`, `w₁ + w₄ = w₂ + w₅` and
  `w₀ + w₂ + w₄ = w₁ + w₃ + w₅` (`hexCollide_conserved_iff`, `hexSum_collide_iff`), and those
  conditions hold **iff** `w = a·1 + b₁·d₁ + b₂·d₂` for integers `a, b₁, b₂`, `d_j` the coordinate
  rows of `hexDir` (`hexCollide_conditions_iff_span`). Consequently mass and both momentum
  components are exactly conserved by the gas on every configuration for every `L`
  (`hexSum_hexGas`, `hexSum_mass_hexGas`, `hexSum_momentum_hexGas`) and along every trajectory in
  `Γ` (`hexSum_leap_sector`), and within the class of site-independent channel-weighted totals
  **they are the only conserved quantities** (`hexSum_hexGas_iff`, `hexSum_hexGas_iff_span`).
  The conserved fields are translation-invariant (`hexSum_shiftBy`) and covariant under the
  lattice's `60°` rotation, which commutes with the gas (`hexGas_hexRot`, `hexRot_charges`).
  H-A's `q`-gauge test has no analogue here: the alphabet is Boolean occupation by construction
  and carries no free parameter, and none is manufactured. **Reported status for H1: HD for mass
  and momentum, for the candidate, on the sector** — with the uniqueness within the frozen class
  stated and the outside of the class HO. Staggered, site-dependent or time-dependent invariants
  are outside the class and are not adjudicated.
* **`HB2` — the lowest-order stencil tensors** (Section E). The second moment of the embedded
  stencil is `3 δ_{ab}` (`hexMoment2_eq`); the fourth moment is
  `(3/4)(δ_{ab}δ_{ce} + δ_{ac}δ_{be} + δ_{ae}δ_{bc})` on all sixteen entries (`hexMoment4_eq`), its
  quartic form is `(9/4)(Σ_i k_i²)²` (`hexMoment4_quartic`) and is a function of `|k|²`
  (`hexMoment4_isotropic`); H-A's `axisMoment4 2 = 2·[a = b = c = e]` has quartic form
  `2(k₁⁴ + k₂⁴)`, equal to `2` at `(1, 0)` and `1` at `(1/√2, 1/√2)`, two vectors of the same
  length on which the hexagonal form agrees (`axisMoment4_two_not_isotropic`); the sixth moment
  is not isotropic, `Σ_k (u_k)₁⁶ = 33/16` against `Σ_k (u_k)₁⁴ (u_k)₂² = 3/16`, ratio `11` where an
  isotropic rank-6 tensor has `5` (`hexMoment6_not_isotropic`). **Reported status for H2: HD for
  the stencil tensor; for the hydrodynamic stress, HC conditional on H5's closure consuming this
  tensor, otherwise HO.** Fourth order is what the stress expansion needs; isotropy already fails
  at sixth order, and **no claim is made about higher orders**.
* **`HB3` — exact closure of a coarse variable, and the sector measure** (Section F). At `L = 4`,
  `b = 2`, two configurations pinned by equation — `c`: channel `0` at `(0, 0)` and channel `3`
  at `(0, 1)`; `c'`: the head-on pair `{0, 3}` at `(0, 0)` — have equal block charges for every
  block and every weight at `t` and at `t − 1`, and different momentum on block `(0, 0)` at
  `t + 1` (`hb3a_block_state_not_closed`), so no coarse rule closes on the block-charge two-time
  state (`hb3a_no_closure`). The charge sectors are invariant: `hexGas` maps each
  `{c | M c = m ∧ (P₁ c, P₂ c) = p}` bijectively onto itself (`hexGas_bijOn_sector`), the exact
  statement beneath any local-equilibrium hypothesis and all the round says in that direction.
  **Reported status for H3: HO.** No timescale is asserted and no local-equilibrium or mixing
  statement is made in either direction.

## The post-round status, under the frozen rule

The candidate is finite, deterministic, reversible, translation-covariant and of bounded degree,
inside the kernel's `Substratum` interface, with exact mass and momentum conservation on every
configuration for every lattice size and fourth-order stencil isotropy, proved and not assumed:
**a rigorous reversible fluid witness in the A1–A4, ¬A5 class**. It lies in the class obtained by
dropping A5's amplitude-scale gauge principle; **whether that class is admissible as an OI
substratum is an owner decision this round does not make**, and it is recorded as open. Round H-B
is therefore **not** reported closed by this module, and no label here is a label "for OI": every
HD, HC, HI or HO reading above is a reading for the candidate, in the class it lies in.

## What none of this licenses

**Nothing here bears on the OI → QM chain, on Track B, on Bell, or on gravity.** **Nothing here
says OI yields Navier–Stokes**: a lattice gas with the right conservation laws and stencil is not
a hydrodynamic limit, and the candidate is not shown to be selected by OI. **Nothing here is a
continuum statement**: no PDE limit is asserted and no scaling map is fixed beyond the field lift.
**No timescale separation is asserted.** **Nothing here changes A1–A6 or their status**; H-A's
findings stand as stated for the wave representative, and the candidate's A5 failure is not a
criticism of the manuscripts' linear rule. **Nothing about `d = 3`.** No manuscript is edited.
-/

namespace OIBridge
namespace HexLatticeGas

open Finset
open OIBridge.SecondOrderCircuit (leap curOf prevOf)
open OIBridge.SubstratumInterfaceAudit (Substratum shiftBy)
open OIBridge.HydroSourceAudit (curOf_leap axisMoment4 axisMoment4_eq axisMoment4_quartic)

/-! ### Section A — the stencil and the collision -/

section Stencil

/-- **THE SIX LATTICE DIRECTIONS** (budget slot 1) — `c_k` in lattice coordinates, as integers:
`c₀ = (1, 0)`, `c₁ = (0, 1)`, `c₂ = (−1, 1)`, `c₃ = (−1, 0)`, `c₄ = (0, −1)`, `c₅ = (1, −1)`, cast to
`ZMod L` wherever a site is formed. In the hexagonal basis `a₁ = (1, 0)`, `a₂ = (1/2, √3/2)` their
images are the six unit vectors at angles `kπ/3`. -/
def hexDir : Fin 6 → Fin 2 → ℤ := ![![1, 0], ![0, 1], ![-1, 1], ![-1, 0], ![0, -1], ![1, -1]]

/-- `c_{k+3} = −c_k`. -/
theorem hexDir_add_three (k : Fin 6) (j : Fin 2) : hexDir (k + 3) j = -hexDir k j := by
  revert k j; decide

/-- `c_{k+3} = −c_k`, cast to `ZMod L`. -/
theorem hexDir_cast_add_three (L : ℕ) (k : Fin 6) :
    (fun j => (hexDir (k + 3) j : ZMod L)) = -(fun j => (hexDir k j : ZMod L)) := by
  funext j
  rw [Pi.neg_apply, hexDir_add_three, Int.cast_neg]

/-- The `60°` rotation `ρ (a, b) = (−b, a + b)` carries `c_k` to `c_{k+1}`. -/
theorem hexDir_add_one (k : Fin 6) :
    hexDir (k + 1) 0 = -hexDir k 1 ∧ hexDir (k + 1) 1 = hexDir k 0 + hexDir k 1 := by
  revert k; decide

/-- Its inverse `ρ⁻¹ (a, b) = (a + b, −a)` carries `c_k` to `c_{k−1}`. -/
theorem hexDir_sub_one (k : Fin 6) :
    hexDir (k - 1) 0 = hexDir k 0 + hexDir k 1 ∧ hexDir (k - 1) 1 = -hexDir k 0 := by
  revert k; decide

/-- Each coordinate row of `hexDir` satisfies the three collision-invariance conditions of
`HB1-b`. -/
theorem hexDir_conditions (j : Fin 2) :
    hexDir 0 j + hexDir 3 j = hexDir 1 j + hexDir 4 j
      ∧ hexDir 1 j + hexDir 4 j = hexDir 2 j + hexDir 5 j
      ∧ hexDir 0 j + hexDir 2 j + hexDir 4 j = hexDir 1 j + hexDir 3 j + hexDir 5 j := by
  revert j; decide

/-- **THE ON-SITE COLLISION** (budget slot 2) — a permutation of the 64 local states
`Fin 6 → ZMod 2`, the identity on 59 of them and on the five remaining ones the 3-cycle of the
head-on pairs `{0, 3} ↦ {1, 4} ↦ {2, 5} ↦ {0, 3}` composed with the transposition of the three-body
states `{0, 2, 4} ↔ {1, 3, 5}`, written as a product of transpositions so that the inverse is
explicit. Every moved state has mass `2` or `3` and momentum `0`. -/
def hexCollide : Equiv.Perm (Fin 6 → ZMod 2) :=
  Equiv.swap ![1, 0, 0, 1, 0, 0] ![0, 1, 0, 0, 1, 0]
    * Equiv.swap ![0, 1, 0, 0, 1, 0] ![0, 0, 1, 0, 0, 1]
    * Equiv.swap ![1, 0, 1, 0, 1, 0] ![0, 1, 0, 1, 0, 1]

theorem hexCollide_apply (s : Fin 6 → ZMod 2) :
    hexCollide s = Equiv.swap ![1, 0, 0, 1, 0, 0] ![0, 1, 0, 0, 1, 0]
      (Equiv.swap ![0, 1, 0, 0, 1, 0] ![0, 0, 1, 0, 0, 1]
        (Equiv.swap ![1, 0, 1, 0, 1, 0] ![0, 1, 0, 1, 0, 1] s)) := rfl

/-- **THE FIVE MOVED STATES**: `{0, 3} ↦ {1, 4} ↦ {2, 5} ↦ {0, 3}` and `{0, 2, 4} ↔ {1, 3, 5}`. -/
theorem hexCollide_moved :
    hexCollide ![1, 0, 0, 1, 0, 0] = ![0, 1, 0, 0, 1, 0]
    ∧ hexCollide ![0, 1, 0, 0, 1, 0] = ![0, 0, 1, 0, 0, 1]
    ∧ hexCollide ![0, 0, 1, 0, 0, 1] = ![1, 0, 0, 1, 0, 0]
    ∧ hexCollide ![1, 0, 1, 0, 1, 0] = ![0, 1, 0, 1, 0, 1]
    ∧ hexCollide ![0, 1, 0, 1, 0, 1] = ![1, 0, 1, 0, 1, 0] := by
  decide

/-- **THE 59 FIXED STATES**: every state other than the five moved ones is fixed. -/
theorem hexCollide_of_ne {s : Fin 6 → ZMod 2} (hA : s ≠ ![1, 0, 0, 1, 0, 0])
    (hB : s ≠ ![0, 1, 0, 0, 1, 0]) (hC : s ≠ ![0, 0, 1, 0, 0, 1]) (hD : s ≠ ![1, 0, 1, 0, 1, 0])
    (hE : s ≠ ![0, 1, 0, 1, 0, 1]) : hexCollide s = s := by
  rw [hexCollide_apply, Equiv.swap_apply_of_ne_of_ne hD hE, Equiv.swap_apply_of_ne_of_ne hB hC,
    Equiv.swap_apply_of_ne_of_ne hA hB]

theorem hexCollide_symm_of_ne {s : Fin 6 → ZMod 2} (hA : s ≠ ![1, 0, 0, 1, 0, 0])
    (hB : s ≠ ![0, 1, 0, 0, 1, 0]) (hC : s ≠ ![0, 0, 1, 0, 0, 1]) (hD : s ≠ ![1, 0, 1, 0, 1, 0])
    (hE : s ≠ ![0, 1, 0, 1, 0, 1]) : hexCollide.symm s = s :=
  (Equiv.symm_apply_eq hexCollide).mpr (hexCollide_of_ne hA hB hC hD hE).symm

/-- Every moved state occupies a channel other than any given one. -/
theorem hexCollide_moved_support (k₀ : Fin 6) :
    (∃ k, k ≠ k₀ ∧ (![1, 0, 0, 1, 0, 0] : Fin 6 → ZMod 2) k ≠ 0)
    ∧ (∃ k, k ≠ k₀ ∧ (![0, 1, 0, 0, 1, 0] : Fin 6 → ZMod 2) k ≠ 0)
    ∧ (∃ k, k ≠ k₀ ∧ (![0, 0, 1, 0, 0, 1] : Fin 6 → ZMod 2) k ≠ 0)
    ∧ (∃ k, k ≠ k₀ ∧ (![1, 0, 1, 0, 1, 0] : Fin 6 → ZMod 2) k ≠ 0)
    ∧ (∃ k, k ≠ k₀ ∧ (![0, 1, 0, 1, 0, 1] : Fin 6 → ZMod 2) k ≠ 0) := by
  revert k₀; decide

/-- **SINGLE PARTICLES DO NOT COLLIDE**: a state occupying at most one channel is fixed. -/
theorem hexCollide_of_single (s : Fin 6 → ZMod 2) (k₀ : Fin 6) (h : ∀ k, k ≠ k₀ → s k = 0) :
    hexCollide s = s := by
  have key : ∀ X : Fin 6 → ZMod 2, (∃ k, k ≠ k₀ ∧ X k ≠ 0) → s ≠ X := by
    rintro X ⟨k, hk, hX⟩ rfl
    exact hX (h k hk)
  obtain ⟨hA, hB, hC, hD, hE⟩ := hexCollide_moved_support k₀
  exact hexCollide_of_ne (key _ hA) (key _ hB) (key _ hC) (key _ hD) (key _ hE)

theorem hexCollide_symm_of_single (s : Fin 6 → ZMod 2) (k₀ : Fin 6) (h : ∀ k, k ≠ k₀ → s k = 0) :
    hexCollide.symm s = s :=
  (Equiv.symm_apply_eq hexCollide).mpr (hexCollide_of_single s k₀ h).symm

theorem hexCollide_zero : hexCollide 0 = 0 := hexCollide_of_single 0 0 fun _ _ => rfl

/-- **THE COLLISION COMMUTES WITH THE CHANNEL ROTATION** `k ↦ k + 1`, on all 64 states. -/
theorem hexCollide_channel_rot (s : Fin 6 → ZMod 2) :
    hexCollide (fun k => s (k - 1)) = fun k => hexCollide s (k - 1) := by
  revert s
  simp only [Fin.forall_fin_succ_pi, Fin.forall_fin_zero_pi]
  decide

/-- **THE COLLISION IS CHIRAL**: it does not commute with the channel reflection `k ↦ −k` — on the
head-on pair `{0, 3}`, which the reflection fixes, the collision gives `{1, 4}` while the
reflected image of `{1, 4}` is `{2, 5}`. This is a property of the class, recorded as such; no
parity statement is made. -/
theorem hexCollide_not_reflection :
    hexCollide (fun k => (![1, 0, 0, 1, 0, 0] : Fin 6 → ZMod 2) (-k))
      ≠ fun k => hexCollide ![1, 0, 0, 1, 0, 0] (-k) := by
  decide

end Stencil

/-! ### Section B — streaming, the gas, and the substratum instance -/

section Gas

variable (L : ℕ)

/-- **STREAMING** (budget slot 3) — the particle of channel `k` moves one lattice step along
`c_k`: `(stream c) i k = c (i − c_k) k`, with inverse `(unstream c) i k = c (i + c_k) k`. It is the
permutation `(i, k) ↦ (i + c_k, k)` of site–channel pairs, and changes no channel index. -/
def hexStream : Equiv.Perm ((Fin 2 → ZMod L) → Fin 6 → ZMod 2) where
  toFun c i k := c (i - fun j => (hexDir k j : ZMod L)) k
  invFun c i k := c (i + fun j => (hexDir k j : ZMod L)) k
  left_inv c := by funext i k; simp only [add_sub_cancel_right]
  right_inv c := by funext i k; simp only [sub_add_cancel]

theorem hexStream_apply (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) (i : Fin 2 → ZMod L) (k : Fin 6) :
    hexStream L c i k = c (i - fun j => (hexDir k j : ZMod L)) k := rfl

/-- **THE GAS** (budget slot 4) — `Φ := hexStream ∘ (sitewise hexCollide)`: collide, then stream.
A bijection because both factors are; `Φ⁻¹ = (sitewise hexCollide⁻¹) ∘ unstream`. -/
def hexGas : Equiv.Perm ((Fin 2 → ZMod L) → Fin 6 → ZMod 2) :=
  (Equiv.piCongrRight fun _ => hexCollide).trans (hexStream L)

theorem hexGas_eq (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) :
    hexGas L c = hexStream L fun i => hexCollide (c i) := rfl

theorem hexGas_apply (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) (i : Fin 2 → ZMod L) (k : Fin 6) :
    hexGas L c i k = hexCollide (c (i - fun j => (hexDir k j : ZMod L))) k := rfl

theorem hexGas_symm_apply (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) (i : Fin 2 → ZMod L) :
    (hexGas L).symm c i = hexCollide.symm fun k => c (i + fun j => (hexDir k j : ZMod L)) k := rfl

/-- **THE SUBSTRATUM INSTANCE** (budget slot 5) — the kernel's `Substratum`, consumed
unmodified: sites `Fin 2 → ZMod L`, alphabet `Fin 6 → ZMod 2`, and the second-order rule
`F c := Φ c + Φ⁻¹ c` (channel-wise exclusive or) with neighbourhood `N i := {i + c_k}`, built
inline. The phase-space map is `leap F : (p, c) ↦ (c, F c − p)`; on the graph sector
`prevOf x = Φ⁻¹ (curOf x)` it acts as `Φ` (`hexSubstratum_sector`). -/
def hexSubstratum [NeZero L] : Substratum where
  ι := Fin 2 → ZMod L
  V := Fin 6 → ZMod 2
  R :=
    { F := fun c => hexGas L c + (hexGas L).symm c
      N := fun i => Finset.univ.image fun k : Fin 6 => i + fun j => (hexDir k j : ZMod L)
      infl := fun i => Finset.univ.image fun k : Fin 6 => i + fun j => (hexDir k j : ZMod L)
      dep := fun i c c' h => by
        have h1 : ∀ k : Fin 6, c (i + fun j => (hexDir k j : ZMod L))
            = c' (i + fun j => (hexDir k j : ZMod L)) :=
          fun k => h _ (Finset.mem_image.mpr ⟨k, Finset.mem_univ _, rfl⟩)
        have h2 : ∀ k : Fin 6, c (i - fun j => (hexDir k j : ZMod L))
            = c' (i - fun j => (hexDir k j : ZMod L)) := by
          intro k
          rw [sub_eq_add_neg, ← hexDir_cast_add_three]
          exact h1 (k + 3)
        show hexGas L c i + (hexGas L).symm c i = hexGas L c' i + (hexGas L).symm c' i
        rw [hexGas_symm_apply, hexGas_symm_apply]
        congr 1
        · funext k
          rw [hexGas_apply, hexGas_apply, h2]
        · congr 1
          funext k
          rw [h1]
      mem_infl := fun i j hj => by
        obtain ⟨k, -, rfl⟩ := Finset.mem_image.mp hj
        refine Finset.mem_image.mpr ⟨k + 3, Finset.mem_univ _, ?_⟩
        rw [hexDir_cast_add_three]
        abel }

variable [NeZero L]

theorem hexSubstratum_F :
    (hexSubstratum L).R.F = fun c => hexGas L c + (hexGas L).symm c := rfl

theorem hexSubstratum_N (i : Fin 2 → ZMod L) :
    (hexSubstratum L).R.N i = Finset.univ.image fun k : Fin 6 => i + fun j => (hexDir k j : ZMod L) :=
  rfl

/-- **`HB0-a` — A1**: the configuration space is finite. -/
theorem hexSubstratum_A1 : (hexSubstratum L).A1 := by
  show Finite ((Fin 2 → ZMod L) → (Fin 6 → ZMod 2) × (Fin 6 → ZMod 2))
  infer_instance

/-- **`HB0-a` — A2**: the phase-space map is a bijection, by the interface's own theorem. -/
theorem hexSubstratum_A2 : (hexSubstratum L).A2 := Substratum.a2_every_substratum _

/-- **`HB0-a` — A3 WITH DEGREE `6`**: `N i` is the image of `Fin 6`. -/
theorem hexSubstratum_A3 : (hexSubstratum L).A3 6 := by
  intro (i : Fin 2 → ZMod L)
  show (Finset.univ.image fun k : Fin 6 => i + fun j => (hexDir k j : ZMod L)).card ≤ 6
  exact Finset.card_image_le.trans (by simp)

/-- **`HB0-a` — A4, EXACT FORM**: streaming and the sitewise collision each commute with every
translation, hence so do `Φ`, `Φ⁻¹` and their sum. -/
theorem hexSubstratum_A4Exact : (hexSubstratum L).A4Exact := by
  intro (v : Fin 2 → ZMod L) (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2)
  funext (i : Fin 2 → ZMod L)
  show hexGas L (shiftBy v c) i + (hexGas L).symm (shiftBy v c) i
    = hexGas L c (i - v) + (hexGas L).symm c (i - v)
  rw [hexGas_symm_apply, hexGas_symm_apply]
  congr 1
  · funext k
    rw [hexGas_apply, hexGas_apply]
    show hexCollide (c (i - (fun j => (hexDir k j : ZMod L)) - v)) k = _
    rw [sub_right_comm]
  · congr 1
    funext k
    show c (i + (fun j => (hexDir k j : ZMod L)) - v) k = _
    rw [add_sub_right_comm]

/-- **`HB0-a` — A4 WITH TRIVIAL GAUGE**, through `a4_of_exact`. -/
theorem hexSubstratum_A4 : (hexSubstratum L).A4 ⊥ :=
  Substratum.a4_of_exact _ (hexSubstratum_A4Exact L)

end Gas

/-! ### Section C — `HB1`: the channel-weighted totals and their conservation -/

section Totals

/-- **THE CHANNEL-WEIGHTED TOTAL** (budget slot 6) — `hexSum A w c := Σ_{i ∈ A} Σ_k (c i k).val · w k`,
the integer lift of the Boolean occupations, weighted by `w` per channel and summed over a finite
set of sites. Mass is `hexSum univ 1`, momentum in lattice coordinates is
`hexSum univ (k ↦ hexDir k j)`, and block charges are `hexSum β w`. -/
def hexSum {ι : Type} (A : Finset ι) (w : Fin 6 → ℤ) (c : ι → Fin 6 → ZMod 2) : ℤ :=
  ∑ i ∈ A, ∑ k, ((c i k).val : ℤ) * w k

theorem hexSum_apply {ι : Type} (A : Finset ι) (w : Fin 6 → ℤ) (c : ι → Fin 6 → ZMod 2) :
    hexSum A w c = ∑ i ∈ A, ∑ k, ((c i k).val : ℤ) * w k := rfl

/-- A configuration occupying one site. -/
theorem hexSum_single {ι : Type} [Fintype ι] [DecidableEq ι] (w : Fin 6 → ℤ) (x : ι)
    (s : Fin 6 → ZMod 2) :
    hexSum univ w (Pi.single x s) = ∑ k, ((s k).val : ℤ) * w k := by
  unfold hexSum
  rw [Finset.sum_eq_single x]
  · rw [Pi.single_eq_same]
  · intro y _ hy
    rw [Pi.single_eq_of_ne hy]
    simp
  · intro h
    exact absurd (Finset.mem_univ x) h

/-- A configuration occupying one site, over any finite set of sites. -/
theorem hexSum_single_site {ι : Type} [DecidableEq ι] (A : Finset ι) (w : Fin 6 → ℤ) (x : ι)
    (s : Fin 6 → ZMod 2) :
    hexSum A w (fun i => if i = x then s else 0)
      = if x ∈ A then ∑ k, ((s k).val : ℤ) * w k else 0 := by
  unfold hexSum
  rw [← Finset.sum_ite_eq' A x fun _ => ∑ k, ((s k).val : ℤ) * w k]
  refine Finset.sum_congr rfl fun i _ => ?_
  by_cases h : i = x
  · subst h
    simp
  · simp [h]

/-- A configuration occupying two distinct sites, over any finite set of sites. -/
theorem hexSum_two_sites {ι : Type} [DecidableEq ι] (A : Finset ι) (w : Fin 6 → ℤ) (x y : ι)
    (hxy : x ≠ y) (s s' : Fin 6 → ZMod 2) :
    hexSum A w (fun i => if i = x then s else if i = y then s' else 0)
      = (if x ∈ A then ∑ k, ((s k).val : ℤ) * w k else 0)
        + (if y ∈ A then ∑ k, ((s' k).val : ℤ) * w k else 0) := by
  unfold hexSum
  rw [← Finset.sum_ite_eq' A x fun _ => ∑ k, ((s k).val : ℤ) * w k,
    ← Finset.sum_ite_eq' A y fun _ => ∑ k, ((s' k).val : ℤ) * w k, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun i _ => ?_
  by_cases hx : i = x
  · subst hx
    simp [hxy]
  · by_cases hy : i = y
    · subst hy
      simp [hx]
    · simp [hx, hy]

theorem hexSum_neg_weight {ι : Type} (A : Finset ι) (w : Fin 6 → ℤ) (c : ι → Fin 6 → ZMod 2) :
    hexSum A (fun k => -w k) c = -hexSum A w c := by
  unfold hexSum
  simp [mul_neg, Finset.sum_neg_distrib]

theorem hexSum_add_weight {ι : Type} (A : Finset ι) (w w' : Fin 6 → ℤ) (c : ι → Fin 6 → ZMod 2) :
    hexSum A (fun k => w k + w' k) c = hexSum A w c + hexSum A w' c := by
  unfold hexSum
  simp [mul_add, Finset.sum_add_distrib]

/-- The total, read in `ZMod 2`: the parity of the weighted occupation count. -/
theorem hexSum_intCast_two {ι : Type} (A : Finset ι) (w : Fin 6 → ℤ) (c : ι → Fin 6 → ZMod 2) :
    ((hexSum A w c : ℤ) : ZMod 2) = ∑ i ∈ A, ∑ k, c i k * (w k : ZMod 2) := by
  unfold hexSum
  push_cast
  simp

/-- Read in `ZMod 2`, the total is additive in the configuration. -/
theorem hexSum_add_intCast_two {ι : Type} (A : Finset ι) (w : Fin 6 → ℤ)
    (c c' : ι → Fin 6 → ZMod 2) :
    ((hexSum A w (c + c') : ℤ) : ZMod 2) = (hexSum A w c : ZMod 2) + (hexSum A w c' : ZMod 2) := by
  rw [hexSum_intCast_two, hexSum_intCast_two, hexSum_intCast_two, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Pi.add_apply, Pi.add_apply, add_mul]

variable (L : ℕ) [NeZero L]

/-- **`HB1-a` — STREAMING PRESERVES EVERY CHANNEL-WEIGHTED TOTAL**: it permutes site–channel
pairs and preserves the channel index, so each channel's site sum is reindexed by a translation. -/
theorem hexSum_hexStream (w : Fin 6 → ℤ) (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) :
    hexSum univ w (hexStream L c) = hexSum univ w c := by
  unfold hexSum
  simp only [hexStream_apply]
  rw [Finset.sum_comm]
  conv_rhs => rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun k _ => ?_
  exact Equiv.sum_comp (Equiv.subRight fun j => (hexDir k j : ZMod L))
    fun i => ((c i k).val : ℤ) * w k

/-- **`HB1-b`, ON-SITE — THE COLLISION INVARIANTS**: the collision preserves the weighted count
`Σ_k w_k n_k` on every one of the 64 local states **iff** `w₀ + w₃ = w₁ + w₄`,
`w₁ + w₄ = w₂ + w₅` and `w₀ + w₂ + w₄ = w₁ + w₃ + w₅`. Forward: the three states `{0, 3}`,
`{1, 4}`, `{0, 2, 4}`. Backward: the five moved states by the conditions, the 59 others
trivially. -/
theorem hexCollide_conserved_iff (w : Fin 6 → ℤ) :
    (∀ s : Fin 6 → ZMod 2, ∑ k, ((hexCollide s k).val : ℤ) * w k = ∑ k, ((s k).val : ℤ) * w k)
      ↔ (w 0 + w 3 = w 1 + w 4 ∧ w 1 + w 4 = w 2 + w 5
          ∧ w 0 + w 2 + w 4 = w 1 + w 3 + w 5) := by
  obtain ⟨hA, hB, hC, hD, hE⟩ := hexCollide_moved
  constructor
  · intro h
    have h1 := h ![1, 0, 0, 1, 0, 0]
    have h2 := h ![0, 1, 0, 0, 1, 0]
    have h3 := h ![1, 0, 1, 0, 1, 0]
    rw [hA] at h1
    rw [hB] at h2
    rw [hD] at h3
    simp [Fin.sum_univ_six, -ZMod.natCast_val, ZMod.val_one_eq_one_mod] at h1 h2 h3
    exact ⟨by linarith, by linarith, by linarith⟩
  · rintro ⟨h1, h2, h3⟩ s
    by_cases sA : s = ![1, 0, 0, 1, 0, 0]
    · rw [sA, hA]
      simp [Fin.sum_univ_six, -ZMod.natCast_val, ZMod.val_one_eq_one_mod]
      linarith
    by_cases sB : s = ![0, 1, 0, 0, 1, 0]
    · rw [sB, hB]
      simp [Fin.sum_univ_six, -ZMod.natCast_val, ZMod.val_one_eq_one_mod]
      linarith
    by_cases sC : s = ![0, 0, 1, 0, 0, 1]
    · rw [sC, hC]
      simp [Fin.sum_univ_six, -ZMod.natCast_val, ZMod.val_one_eq_one_mod]
      linarith
    by_cases sD : s = ![1, 0, 1, 0, 1, 0]
    · rw [sD, hD]
      simp [Fin.sum_univ_six, -ZMod.natCast_val, ZMod.val_one_eq_one_mod]
      linarith
    by_cases sE : s = ![0, 1, 0, 1, 0, 1]
    · rw [sE, hE]
      simp [Fin.sum_univ_six, -ZMod.natCast_val, ZMod.val_one_eq_one_mod]
      linarith
    rw [hexCollide_of_ne sA sB sC sD sE]

/-- The sitewise collision on a one-site configuration is the one-site configuration of the
collided state. -/
theorem collide_single {ι : Type} [DecidableEq ι] (x : ι) (s : Fin 6 → ZMod 2) :
    (fun i => hexCollide ((Pi.single x s : ι → Fin 6 → ZMod 2) i)) = Pi.single x (hexCollide s) := by
  funext i
  by_cases h : i = x
  · subst h
    rw [Pi.single_eq_same, Pi.single_eq_same]
  · rw [Pi.single_eq_of_ne h, Pi.single_eq_of_ne h, hexCollide_zero]

/-- **`HB1-b` — THE SITEWISE COLLISION PRESERVES THE TOTAL WITH WEIGHT `w` ON EVERY
CONFIGURATION IFF THE THREE CONDITIONS HOLD.** Forward: the three one-site configurations at the
origin. Backward: the identity holds at each site. -/
theorem hexSum_collide_iff (w : Fin 6 → ℤ) :
    (∀ c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2,
        hexSum univ w (fun i => hexCollide (c i)) = hexSum univ w c)
      ↔ (w 0 + w 3 = w 1 + w 4 ∧ w 1 + w 4 = w 2 + w 5
          ∧ w 0 + w 2 + w 4 = w 1 + w 3 + w 5) := by
  rw [← hexCollide_conserved_iff]
  constructor
  · intro h s
    have := h (Pi.single 0 s)
    rwa [collide_single, hexSum_single, hexSum_single] at this
  · intro h c
    unfold hexSum
    exact Finset.sum_congr rfl fun i _ => h (c i)

/-- **`HB1-b′` — THE THREE CONDITIONS HOLD IFF `w` LIES IN THE `ℤ`-SPAN OF MASS AND THE TWO
MOMENTUM ROWS**: `w = a·1 + b₁·d₁ + b₂·d₂` with `d_j k = hexDir k j`; the solution lattice has
rank `3` and the basis is unimodular, the witnesses being `a = w₀ − w₁ + w₂`, `b₁ = w₁ − w₂`,
`b₂ = 2w₁ − w₀ − w₂`. -/
theorem hexCollide_conditions_iff_span (w : Fin 6 → ℤ) :
    (w 0 + w 3 = w 1 + w 4 ∧ w 1 + w 4 = w 2 + w 5 ∧ w 0 + w 2 + w 4 = w 1 + w 3 + w 5)
      ↔ ∃ a b₁ b₂ : ℤ, w = fun k => a + b₁ * hexDir k 0 + b₂ * hexDir k 1 := by
  constructor
  · rintro ⟨h1, h2, h3⟩
    refine ⟨w 0 - w 1 + w 2, w 1 - w 2, 2 * w 1 - w 0 - w 2, ?_⟩
    funext k
    fin_cases k <;> simp [hexDir] <;> linarith
  · rintro ⟨a, b₁, b₂, rfl⟩
    simp [hexDir]
    refine ⟨?_, ?_, ?_⟩ <;> ring

/-- **`HB1-c` — THE GAS PRESERVES EVERY TOTAL WHOSE WEIGHT SATISFIES THE THREE CONDITIONS**, on
every configuration, for every `L`. -/
theorem hexSum_hexGas (w : Fin 6 → ℤ)
    (hw : w 0 + w 3 = w 1 + w 4 ∧ w 1 + w 4 = w 2 + w 5 ∧ w 0 + w 2 + w 4 = w 1 + w 3 + w 5)
    (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) :
    hexSum univ w (hexGas L c) = hexSum univ w c := by
  rw [hexGas_eq, hexSum_hexStream, (hexSum_collide_iff L w).mpr hw]

/-- **`HB1-c`, THE CLASSIFICATION**: the gas preserves the total with weight `w` on every
configuration **iff** the three conditions hold — so within the class of site-independent
channel-weighted totals, mass and momentum are the only conserved quantities. -/
theorem hexSum_hexGas_iff (w : Fin 6 → ℤ) :
    (∀ c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2, hexSum univ w (hexGas L c) = hexSum univ w c)
      ↔ (w 0 + w 3 = w 1 + w 4 ∧ w 1 + w 4 = w 2 + w 5
          ∧ w 0 + w 2 + w 4 = w 1 + w 3 + w 5) := by
  constructor
  · intro h
    refine (hexSum_collide_iff L w).mp fun c => ?_
    have := h c
    rwa [hexGas_eq, hexSum_hexStream] at this
  · intro hw c
    exact hexSum_hexGas L w hw c

/-- **`HB1-c`, THE CLASSIFICATION IN SPAN FORM**: conserved by the gas on every configuration
**iff** `w ∈ span_ℤ {1, d₁, d₂}`. -/
theorem hexSum_hexGas_iff_span (w : Fin 6 → ℤ) :
    (∀ c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2, hexSum univ w (hexGas L c) = hexSum univ w c)
      ↔ ∃ a b₁ b₂ : ℤ, w = fun k => a + b₁ * hexDir k 0 + b₂ * hexDir k 1 := by
  rw [hexSum_hexGas_iff, hexCollide_conditions_iff_span]

/-- **`HB1-c` — MASS IS EXACTLY CONSERVED BY THE GAS**, on every configuration, for every `L`. -/
theorem hexSum_mass_hexGas (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) :
    hexSum univ 1 (hexGas L c) = hexSum univ 1 c :=
  hexSum_hexGas L 1 (by simp) c

/-- **`HB1-c` — BOTH MOMENTUM COMPONENTS ARE EXACTLY CONSERVED BY THE GAS**, on every
configuration, for every `L`. -/
theorem hexSum_momentum_hexGas (j : Fin 2) (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) :
    hexSum univ (fun k => hexDir k j) (hexGas L c) = hexSum univ (fun k => hexDir k j) c :=
  hexSum_hexGas L _ (hexDir_conditions j) c

/-- **`HB1-d` — TRANSLATION INVARIANCE**: every channel-weighted total is invariant under every
lattice translation, a reindexing of the site sum. -/
theorem hexSum_shiftBy (v : Fin 2 → ZMod L) (w : Fin 6 → ℤ)
    (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) :
    hexSum univ w (shiftBy v c) = hexSum univ w c := by
  unfold hexSum shiftBy
  exact Equiv.sum_comp (Equiv.subRight v) fun i => ∑ k, ((c i k).val : ℤ) * w k

end Totals

/-! ### Section D — `HB0-b`, `HB0-c`: non-additivity, the sector, and the off-sector control -/

section Sector

variable (L : ℕ)

theorem single_channel_zero {ι : Type} [DecidableEq ι] (x i : ι) (s : Fin 6 → ZMod 2) (k : Fin 6)
    (hk : s k = 0) : (Pi.single x s : ι → Fin 6 → ZMod 2) i k = 0 := by
  rw [Pi.single_apply]
  split_ifs
  · exact hk
  · rfl

/-- The gas on a one-particle configuration has no particle in any other channel. -/
theorem hexGas_single_channel (x : Fin 2 → ZMod L) (s : Fin 6 → ZMod 2) (k₀ : Fin 6)
    (hs : ∀ k, k ≠ k₀ → s k = 0) (i : Fin 2 → ZMod L) (k : Fin 6) (hk : k ≠ k₀) :
    hexGas L (Pi.single x s) i k = 0 := by
  rw [hexGas_apply, hexCollide_of_single _ k₀ ?_]
  · exact single_channel_zero _ _ _ _ (hs k hk)
  · intro k' hk'
    exact single_channel_zero _ _ _ _ (hs k' hk')

/-- The inverse gas on a one-particle configuration has no particle in any other channel. -/
theorem hexGas_symm_single_channel (x : Fin 2 → ZMod L) (s : Fin 6 → ZMod 2) (k₀ : Fin 6)
    (hs : ∀ k, k ≠ k₀ → s k = 0) (i : Fin 2 → ZMod L) (k : Fin 6) (hk : k ≠ k₀) :
    (hexGas L).symm (Pi.single x s) i k = 0 := by
  rw [hexGas_symm_apply, hexCollide_symm_of_single _ k₀ ?_]
  · exact single_channel_zero _ _ _ _ (hs k hk)
  · intro k' hk'
    exact single_channel_zero _ _ _ _ (hs k' hk')

/-- A state empty in channels `1`, `2`, `4`, `5` is carried by the inverse collision to a state
empty in channel `1`: it is `{0, 3}`, which goes to `{2, 5}`, or it is fixed. -/
theorem hexCollide_symm_channel_one (s : Fin 6 → ZMod 2) (h1 : s 1 = 0) (h2 : s 2 = 0)
    (h4 : s 4 = 0) (h5 : s 5 = 0) : hexCollide.symm s 1 = 0 := by
  obtain ⟨-, -, hC, -, -⟩ := hexCollide_moved
  by_cases hA : s = ![1, 0, 0, 1, 0, 0]
  · rw [hA, (Equiv.symm_apply_eq hexCollide).mpr hC.symm]
    decide
  · have hne : ∀ X : Fin 6 → ZMod 2, (X 1 ≠ 0 ∨ X 2 ≠ 0 ∨ X 4 ≠ 0 ∨ X 5 ≠ 0) → s ≠ X := by
      rintro X hX rfl
      rcases hX with hX | hX | hX | hX
      · exact hX h1
      · exact hX h2
      · exact hX h4
      · exact hX h5
    rw [hexCollide_symm_of_ne hA (hne _ (by decide)) (hne _ (by decide)) (hne _ (by decide))
      (hne _ (by decide))]
    exact h1

/-- **`HB0-b` — A5 FAILS, THE WITNESS**: `c` = one particle in channel `0` at the origin, `c'` =
one in channel `3` at the origin, pinned by equation, for the rule `F c = Φ c + Φ⁻¹ c` — which is
`(hexSubstratum L).R.F` by `hexSubstratum_F`. `F (c + c')` has a particle in channel `1` at the
site `c₁` — the head-on pair collides to `{1, 4}` and streams — and `F c + F c'` has none there:
single particles do not collide, and channels `0`, `3` are all that occur. Valid for every
`L ≥ 1`. -/
theorem hexSubstratum_A5_witness :
    ∃ c c' : (Fin 2 → ZMod L) → Fin 6 → ZMod 2,
      c = Pi.single 0 ![1, 0, 0, 0, 0, 0] ∧ c' = Pi.single 0 ![0, 0, 0, 1, 0, 0]
      ∧ (hexGas L (c + c') + (hexGas L).symm (c + c')) (fun j => (hexDir 1 j : ZMod L)) 1 = 1
      ∧ ((hexGas L c + (hexGas L).symm c) + (hexGas L c' + (hexGas L).symm c'))
          (fun j => (hexDir 1 j : ZMod L)) 1 = 0
      ∧ hexGas L (c + c') + (hexGas L).symm (c + c')
          ≠ (hexGas L c + (hexGas L).symm c) + (hexGas L c' + (hexGas L).symm c') := by
  obtain ⟨hA, -, -, -, -⟩ := hexCollide_moved
  have hsum : (![1, 0, 0, 0, 0, 0] : Fin 6 → ZMod 2) + ![0, 0, 0, 1, 0, 0] = ![1, 0, 0, 1, 0, 0] := by
    decide
  have he0 : ∀ k : Fin 6, k ≠ 0 → (![1, 0, 0, 0, 0, 0] : Fin 6 → ZMod 2) k = 0 := by decide
  have he3 : ∀ k : Fin 6, k ≠ 3 → (![0, 0, 0, 1, 0, 0] : Fin 6 → ZMod 2) k = 0 := by decide
  have v1 : (hexGas L ((Pi.single 0 ![1, 0, 0, 0, 0, 0] : (Fin 2 → ZMod L) → Fin 6 → ZMod 2)
        + Pi.single 0 ![0, 0, 0, 1, 0, 0])
      + (hexGas L).symm ((Pi.single 0 ![1, 0, 0, 0, 0, 0] : (Fin 2 → ZMod L) → Fin 6 → ZMod 2)
        + Pi.single 0 ![0, 0, 0, 1, 0, 0]))
      (fun j => (hexDir 1 j : ZMod L)) 1 = 1 := by
    rw [← Pi.single_add, hsum, Pi.add_apply, Pi.add_apply, hexGas_apply, sub_self,
      Pi.single_eq_same, hA, hexGas_symm_apply, hexCollide_symm_channel_one]
    · simp
    all_goals exact single_channel_zero _ _ _ _ (by decide)
  have v2 : ((hexGas L (Pi.single 0 ![1, 0, 0, 0, 0, 0] : (Fin 2 → ZMod L) → Fin 6 → ZMod 2)
        + (hexGas L).symm (Pi.single 0 ![1, 0, 0, 0, 0, 0]))
      + (hexGas L (Pi.single 0 ![0, 0, 0, 1, 0, 0])
        + (hexGas L).symm (Pi.single 0 ![0, 0, 0, 1, 0, 0])))
      (fun j => (hexDir 1 j : ZMod L)) 1 = 0 := by
    simp only [Pi.add_apply]
    rw [hexGas_single_channel L _ _ 0 he0 _ 1 (by decide),
      hexGas_symm_single_channel L _ _ 0 he0 _ 1 (by decide),
      hexGas_single_channel L _ _ 3 he3 _ 1 (by decide),
      hexGas_symm_single_channel L _ _ 3 he3 _ 1 (by decide)]
    simp
  refine ⟨_, _, rfl, rfl, v1, v2, fun h => ?_⟩
  have := congrFun (congrFun h (fun j => (hexDir 1 j : ZMod L))) 1
  rw [v1, v2] at this
  exact absurd this (by decide)

variable [NeZero L]

/-- **`HB0-b` — THE CANDIDATE FAILS A5**: `F (c + c') ≠ F c + F c'` for the witness, `F` being the
substratum's own rule. The candidate lies in the class obtained by dropping the amplitude-scale
gauge principle; whether that class is admissible as an OI substratum is an owner decision this
round does not make. -/
theorem hexSubstratum_not_A5 : ¬ (hexSubstratum L).A5 := by
  intro h
  obtain ⟨c, c', -, -, -, -, hne⟩ := hexSubstratum_A5_witness L
  exact hne (h c c')

/-- **`HB0-c` — THE SECTOR IS INVARIANT AND CARRIES THE GAS**: for every phase-space configuration
with `prevOf x = Φ⁻¹ (curOf x)`, the image under `leap F` satisfies the same relation and its
current slice is `Φ (curOf x)`, since `F (curOf x) − prevOf x = Φ c + Φ⁻¹ c − Φ⁻¹ c = Φ c`. -/
theorem hexSubstratum_sector (x : (hexSubstratum L).Conf)
    (hx : prevOf x = (hexGas L).symm (curOf x :)) :
    prevOf (leap (hexSubstratum L).R.F x)
        = (hexGas L).symm (curOf (leap (hexSubstratum L).R.F x) :)
      ∧ curOf (leap (hexSubstratum L).R.F x) = hexGas L (curOf x :) := by
  have hcur : curOf (leap (hexSubstratum L).R.F x) = hexGas L (curOf x :) := by
    rw [curOf_leap, hx, hexSubstratum_F]
    exact add_sub_cancel_right _ _
  refine ⟨?_, hcur⟩
  rw [hcur]
  exact ((hexGas L).symm_apply_apply _).symm

/-- **`HB1-c` ON TRAJECTORIES — EVERY TOTAL WITH AN ADMISSIBLE WEIGHT IS CONSERVED ALONG EVERY
TRAJECTORY IN `Γ`**; in particular mass and both momentum components. -/
theorem hexSum_leap_sector (w : Fin 6 → ℤ)
    (hw : w 0 + w 3 = w 1 + w 4 ∧ w 1 + w 4 = w 2 + w 5 ∧ w 0 + w 2 + w 4 = w 1 + w 3 + w 5)
    (x : (hexSubstratum L).Conf) (hx : prevOf x = (hexGas L).symm (curOf x :)) :
    hexSum (univ : Finset (Fin 2 → ZMod L)) w (curOf (leap (hexSubstratum L).R.F x) :)
      = hexSum (univ : Finset (Fin 2 → ZMod L)) w (curOf x :) := by
  rw [(hexSubstratum_sector L x hx).2]
  exact hexSum_hexGas L w hw _

/-- **`HB0-c`, THE COUNTERCONTROL — MASS IS NOT CONSERVED OFF THE SECTOR**: with `prevOf x = 0` and
`curOf x` a single particle in channel `0` at the origin, the mass after one step is not `1`, for
every `L ≥ 1`. The proof is by parity: `F c = Φ c + Φ⁻¹ c` in `ZMod 2`, and each summand has mass
`1` by `HB1-c`, so the mass of the sum is even. (The value is `0` for `L ∈ {1, 2}` and `2` for
`L ≥ 3`; the statement is the inequality.) -/
theorem hexSubstratum_mass_not_conserved_off_sector :
    ∃ x : (hexSubstratum L).Conf,
      prevOf x = 0
      ∧ curOf x = (Pi.single 0 ![1, 0, 0, 0, 0, 0] : (Fin 2 → ZMod L) → Fin 6 → ZMod 2)
      ∧ hexSum (univ : Finset (Fin 2 → ZMod L)) 1 (curOf x :) = 1
      ∧ hexSum (univ : Finset (Fin 2 → ZMod L)) 1 (curOf (leap (hexSubstratum L).R.F x) :)
          ≠ hexSum (univ : Finset (Fin 2 → ZMod L)) 1 (curOf x :) := by
  have hmass : hexSum univ 1 (Pi.single 0 ![1, 0, 0, 0, 0, 0] : (Fin 2 → ZMod L) → Fin 6 → ZMod 2)
      = 1 := by
    rw [hexSum_single]
    simp [Fin.sum_univ_six, -ZMod.natCast_val, ZMod.val_one_eq_one_mod]
  refine ⟨fun i => (0, (Pi.single 0 ![1, 0, 0, 0, 0, 0] : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) i),
    rfl, rfl, hmass, fun h => ?_⟩
  have hc : curOf (leap (hexSubstratum L).R.F
      (fun i => (0, (Pi.single 0 ![1, 0, 0, 0, 0, 0] : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) i)
        : (hexSubstratum L).Conf))
      = hexGas L (Pi.single 0 ![1, 0, 0, 0, 0, 0])
        + (hexGas L).symm (Pi.single 0 ![1, 0, 0, 0, 0, 0]) := by
    rw [curOf_leap, hexSubstratum_F]
    exact sub_zero _
  have h1 : hexSum univ 1 (hexGas L (Pi.single 0 ![1, 0, 0, 0, 0, 0])) = 1 := by
    rw [hexSum_mass_hexGas, hmass]
  have h2 : hexSum univ 1 ((hexGas L).symm (Pi.single 0 ![1, 0, 0, 0, 0, 0])) = 1 := by
    rw [← hexSum_mass_hexGas L ((hexGas L).symm _), Equiv.apply_symm_apply, hmass]
  have hpar := congrArg (Int.cast : ℤ → ZMod 2) (h.trans hmass)
  rw [hc, hexSum_add_intCast_two, h1, h2] at hpar
  push_cast at hpar
  exact absurd hpar (by decide)

end Sector

/-! ### Section E — `HB2`: the lowest-order stencil tensors -/

section Moments

/-- **`HB2-a` — THE SECOND MOMENT OF THE EMBEDDED STENCIL IS `3 δ_{ab}`**, stated inline over the
six unit vectors `u_k = (c_k)₁ a₁ + (c_k)₂ a₂`. This is the order Corollary 1a's
`quadratic_isotropic` speaks to for the cubic case, consumed for comparison only. -/
theorem hexMoment2_eq (a b : Fin 2) :
    (∑ k : Fin 6,
        (![(hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2, (hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)]
          : Fin 2 → ℝ) a
        * (![(hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2, (hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)]
          : Fin 2 → ℝ) b)
      = 3 * if a = b then 1 else 0 := by
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  fin_cases a <;> fin_cases b <;> simp [Fin.sum_univ_six, hexDir] <;> nlinarith [h3]

/-- **THE FOURTH MOMENT OF THE HEXAGONAL STENCIL** (budget slot 7) —
`T_{abce} = Σ_k (u_k)_a (u_k)_b (u_k)_c (u_k)_e` over the six embedded unit vectors
`u_k = (c_k)₁ a₁ + (c_k)₂ a₂ = ((c_k)₁ + (c_k)₂/2, (c_k)₂ √3/2)`, the embedding written inline. -/
noncomputable def hexMoment4 (a b c e : Fin 2) : ℝ :=
  ∑ k : Fin 6,
    (![(hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2, (hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)]
      : Fin 2 → ℝ) a
    * (![(hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2, (hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)]
      : Fin 2 → ℝ) b
    * (![(hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2, (hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)]
      : Fin 2 → ℝ) c
    * (![(hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2, (hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)]
      : Fin 2 → ℝ) e

/-- **`HB2-b` — THE FOURTH MOMENT IS `(3/4)(δ_{ab}δ_{ce} + δ_{ac}δ_{be} + δ_{ae}δ_{bc})`**, on all
sixteen entries: `T₁₁₁₁ = T₂₂₂₂ = 9/4`, `T₁₁₂₂ = 3/4`, the odd entries `0`. -/
theorem hexMoment4_eq (a b c e : Fin 2) :
    hexMoment4 a b c e
      = 3 / 4 * ((if a = b then (1 : ℝ) else 0) * (if c = e then 1 else 0)
          + (if a = c then 1 else 0) * (if b = e then 1 else 0)
          + (if a = e then 1 else 0) * (if b = c then 1 else 0)) := by
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have h4 : Real.sqrt 3 ^ 4 = 9 := by
    rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, h3]
    norm_num
  unfold hexMoment4
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases e <;>
    simp [Fin.sum_univ_six, hexDir] <;> nlinarith [h3, h4]

/-- **`HB2-b` — THE QUARTIC FORM OF THE HEXAGONAL MOMENT IS `(9/4)(Σ_i k_i²)²`.** -/
theorem hexMoment4_quartic (k : Fin 2 → ℝ) :
    (∑ a, ∑ b, ∑ c, ∑ e, hexMoment4 a b c e * (k a * k b * k c * k e))
      = 9 / 4 * (∑ i, k i ^ 2) ^ 2 := by
  simp only [hexMoment4_eq, Fin.sum_univ_two]
  simp
  ring

/-- **`HB2-b` — THE HEXAGONAL QUARTIC FORM IS A FUNCTION OF `|k|²`**: two vectors of the same
length give it the same value — the notion `IsotropicQuartic` uses, stated inline for `Fin 2`.
**Reported status for H2: HD for the stencil tensor; HC for the hydrodynamic stress conditional
on H5's closure consuming this tensor, otherwise HO.** -/
theorem hexMoment4_isotropic (k k' : Fin 2 → ℝ) (h : (∑ i, k i ^ 2) = ∑ i, k' i ^ 2) :
    (∑ a, ∑ b, ∑ c, ∑ e, hexMoment4 a b c e * (k a * k b * k c * k e))
      = ∑ a, ∑ b, ∑ c, ∑ e, hexMoment4 a b c e * (k' a * k' b * k' c * k' e) := by
  rw [hexMoment4_quartic, hexMoment4_quartic, h]

/-- **`HB2-c` — THE COMPARISON**: H-A's `axisMoment4 2 = 2·[a = b = c = e]` (`axisMoment4_eq`) has
quartic form `2(k₁⁴ + k₂⁴)` (`axisMoment4_quartic`), which takes the value `2` at `(1, 0)` and `1`
at `(1/√2, 1/√2)`, two vectors of equal length; the hexagonal form agrees on them. So the square
four-velocity stencil is **not** fourth-order isotropic where the hexagonal six-velocity stencil
**is**. H-A's `quartic_not_isotropic` and `axisMoment4_not_isotropic` are the `d = 3` statement
of the same failure and are cited, not re-proved. -/
theorem axisMoment4_two_not_isotropic :
    ∃ k k' : Fin 2 → ℝ, k = ![1, 0] ∧ k' = ![1 / Real.sqrt 2, 1 / Real.sqrt 2]
      ∧ (∑ i, k i ^ 2) = (∑ i, k' i ^ 2)
      ∧ (∀ a b c e : Fin 2, axisMoment4 2 a b c e = if a = b ∧ b = c ∧ c = e then 2 else 0)
      ∧ (∑ a, ∑ b, ∑ c, ∑ e, axisMoment4 2 a b c e * (k a * k b * k c * k e)) = 2
      ∧ (∑ a, ∑ b, ∑ c, ∑ e, axisMoment4 2 a b c e * (k' a * k' b * k' c * k' e)) = 1
      ∧ (∑ a, ∑ b, ∑ c, ∑ e, hexMoment4 a b c e * (k a * k b * k c * k e))
          = ∑ a, ∑ b, ∑ c, ∑ e, hexMoment4 a b c e * (k' a * k' b * k' c * k' e) := by
  have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hk : (1 / Real.sqrt 2) ^ 2 = 1 / 2 := by rw [div_pow, one_pow, h2]
  have hlen : (∑ i, (![1, 0] : Fin 2 → ℝ) i ^ 2)
      = ∑ i, (![1 / Real.sqrt 2, 1 / Real.sqrt 2] : Fin 2 → ℝ) i ^ 2 := by
    simp [Fin.sum_univ_two]
    norm_num
  refine ⟨_, _, rfl, rfl, hlen, axisMoment4_eq 2, ?_, ?_, hexMoment4_isotropic _ _ hlen⟩
  · rw [axisMoment4_quartic]
    simp [Fin.sum_univ_two]
  · rw [axisMoment4_quartic]
    simp only [Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one]
    rw [show (1 / Real.sqrt 2) ^ 4 = ((1 / Real.sqrt 2) ^ 2) ^ 2 by ring, hk]
    norm_num

/-- **`HB2-d` — THE BOUND: THE SIXTH MOMENT IS NOT ISOTROPIC.** `Σ_k (u_k)₁⁶ = 33/16` and
`Σ_k (u_k)₁⁴ (u_k)₂² = 3/16`, ratio `11`, whereas a rotation-isotropic fully symmetric rank-6
tensor has `T₁₁₁₁₁₁ = 5 T₁₁₁₁₂₂`. Fourth-order isotropy holds and isotropy already fails at sixth
order; **no claim is made about higher orders**. -/
theorem hexMoment6_not_isotropic :
    (∑ k : Fin 6, ((hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2) ^ 6) = 33 / 16
    ∧ (∑ k : Fin 6, ((hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2) ^ 4
        * ((hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)) ^ 2) = 3 / 16
    ∧ (∑ k : Fin 6, ((hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2) ^ 6)
        ≠ 5 * ∑ k : Fin 6, ((hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2) ^ 4
          * ((hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)) ^ 2 := by
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have e6 : (∑ k : Fin 6, ((hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2) ^ 6) = 33 / 16 := by
    simp [Fin.sum_univ_six, hexDir]
    norm_num
  have e42 : (∑ k : Fin 6, ((hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2) ^ 4
      * ((hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)) ^ 2) = 3 / 16 := by
    simp [Fin.sum_univ_six, hexDir]
    nlinarith [h3]
  refine ⟨e6, e42, ?_⟩
  rw [e6, e42]
  norm_num

end Moments

/-! ### Section F — `HB3`: exact closure of a block variable, and the sector measure -/

section Block

set_option maxRecDepth 8000 in
/-- **`HB3-a` — THE WITNESS, EVALUATED**: the gas and its inverse on the two configurations of
recorded item 7 at `L = 4`, every site decided. `c`: channel `0` at `(0, 0)`, channel `3` at
`(0, 1)`; `c'`: the head-on pair `{0, 3}` at `(0, 0)`. -/
theorem hb3a_gas_values :
    hexGas 4 (fun i => if i = ![0, 0] then ![1, 0, 0, 0, 0, 0]
        else if i = ![0, 1] then ![0, 0, 0, 1, 0, 0] else 0)
      = (fun i => if i = ![1, 0] then ![1, 0, 0, 0, 0, 0]
        else if i = ![3, 1] then ![0, 0, 0, 1, 0, 0] else 0)
    ∧ (hexGas 4).symm (fun i => if i = ![0, 0] then ![1, 0, 0, 0, 0, 0]
        else if i = ![0, 1] then ![0, 0, 0, 1, 0, 0] else 0)
      = (fun i => if i = ![1, 1] then ![0, 0, 0, 1, 0, 0]
        else if i = ![3, 0] then ![1, 0, 0, 0, 0, 0] else 0)
    ∧ hexGas 4 (fun i => if i = ![0, 0] then ![1, 0, 0, 1, 0, 0] else 0)
      = (fun i => if i = ![0, 1] then ![0, 1, 0, 0, 0, 0]
        else if i = ![0, 3] then ![0, 0, 0, 0, 1, 0] else 0)
    ∧ (hexGas 4).symm (fun i => if i = ![0, 0] then ![1, 0, 0, 1, 0, 0] else 0)
      = (fun i => if i = ![1, 0] then ![0, 0, 0, 1, 0, 0]
        else if i = ![3, 0] then ![1, 0, 0, 0, 0, 0] else 0) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> funext i <;> revert i <;>
    simp only [Fin.forall_fin_succ_pi, Fin.forall_fin_zero_pi] <;> decide

/-- **THE BLOCKS OF THE WITNESS SITES**, `k ↦ ⌊(i k).val / 2⌋` at `L = 4`, `b = 2`: membership
of each site named in the witness in the block `β` of the partition into `2 × 2` squares. -/
theorem hb3a_mem (β : Fin 2 → ℕ) :
    ((![0, 0] : Fin 2 → ZMod 4)
        ∈ (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
      ↔ (![0, 0] : Fin 2 → ℕ) = β)
    ∧ ((![0, 1] : Fin 2 → ZMod 4)
        ∈ (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
      ↔ (![0, 0] : Fin 2 → ℕ) = β)
    ∧ ((![1, 0] : Fin 2 → ZMod 4)
        ∈ (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
      ↔ (![0, 0] : Fin 2 → ℕ) = β)
    ∧ ((![1, 1] : Fin 2 → ZMod 4)
        ∈ (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
      ↔ (![0, 0] : Fin 2 → ℕ) = β)
    ∧ ((![3, 0] : Fin 2 → ZMod 4)
        ∈ (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
      ↔ (![1, 0] : Fin 2 → ℕ) = β)
    ∧ ((![3, 1] : Fin 2 → ZMod 4)
        ∈ (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
      ↔ (![1, 0] : Fin 2 → ℕ) = β)
    ∧ ((![0, 3] : Fin 2 → ZMod 4)
        ∈ (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
      ↔ (![0, 1] : Fin 2 → ℕ) = β) := by
  have b00 : (fun j => ((![0, 0] : Fin 2 → ZMod 4) j).val / 2) = ![0, 0] := by
    funext j; fin_cases j <;> rfl
  have b01 : (fun j => ((![0, 1] : Fin 2 → ZMod 4) j).val / 2) = ![0, 0] := by
    funext j; fin_cases j <;> rfl
  have b10 : (fun j => ((![1, 0] : Fin 2 → ZMod 4) j).val / 2) = ![0, 0] := by
    funext j; fin_cases j <;> rfl
  have b11 : (fun j => ((![1, 1] : Fin 2 → ZMod 4) j).val / 2) = ![0, 0] := by
    funext j; fin_cases j <;> rfl
  have b30 : (fun j => ((![3, 0] : Fin 2 → ZMod 4) j).val / 2) = ![1, 0] := by
    funext j; fin_cases j <;> rfl
  have b31 : (fun j => ((![3, 1] : Fin 2 → ZMod 4) j).val / 2) = ![1, 0] := by
    funext j; fin_cases j <;> rfl
  have b03 : (fun j => ((![0, 3] : Fin 2 → ZMod 4) j).val / 2) = ![0, 1] := by
    funext j; fin_cases j <;> rfl
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  rw [b00, b01, b10, b11, b30, b31, b03]
  exact ⟨Iff.rfl, Iff.rfl, Iff.rfl, Iff.rfl, Iff.rfl, Iff.rfl, Iff.rfl⟩

/-- **`HB3-a` — THE BLOCK-CHARGE TWO-TIME STATE DOES NOT CLOSE ON THE SECTOR**, at `L = 4`,
`b = 2`, the two configurations pinned by equation: `c` = channel `0` at `(0, 0)` and channel `3`
at `(0, 1)`; `c'` = the head-on pair `{0, 3}` at `(0, 0)`. For every block `β` of the partition
into `2 × 2` squares and **every** channel weight `w` — in particular for mass and both momentum
components — the block charges agree at `t` and at `t − 1` (`t − 1` being `Φ⁻¹` of each, as the
sector dictates), while at `t + 1` the momentum component `P₁` on block `(0, 0)` is `1` for `c`
and `0` for `c'`. -/
theorem hb3a_block_state_not_closed :
    ∃ c c' : (Fin 2 → ZMod 4) → Fin 6 → ZMod 2,
      c = (fun i => if i = ![0, 0] then ![1, 0, 0, 0, 0, 0]
        else if i = ![0, 1] then ![0, 0, 0, 1, 0, 0] else 0)
      ∧ c' = (fun i => if i = ![0, 0] then ![1, 0, 0, 1, 0, 0] else 0)
      ∧ (∀ (β : Fin 2 → ℕ) (w : Fin 6 → ℤ),
          hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β) w c
            = hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β) w c')
      ∧ (∀ (β : Fin 2 → ℕ) (w : Fin 6 → ℤ),
          hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β) w
              ((hexGas 4).symm c)
            = hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β) w
              ((hexGas 4).symm c'))
      ∧ hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = ![0, 0])
          (fun k => hexDir k 0) (hexGas 4 c) = 1
      ∧ hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = ![0, 0])
          (fun k => hexDir k 0) (hexGas 4 c') = 0 := by
  obtain ⟨g1, g2, g3, g4⟩ := hb3a_gas_values
  refine ⟨_, _, rfl, rfl, fun β w => ?_, fun β w => ?_, ?_, ?_⟩
  · obtain ⟨m00, m01, -, -, -, -, -⟩ := hb3a_mem β
    rw [hexSum_two_sites _ _ _ _ (by decide), hexSum_single_site]
    simp only [m00, m01]
    by_cases hβ : (![0, 0] : Fin 2 → ℕ) = β
    · rw [if_pos hβ, if_pos hβ, if_pos hβ]
      simp [Fin.sum_univ_six, -ZMod.natCast_val, ZMod.val_one_eq_one_mod]
    · rw [if_neg hβ, if_neg hβ, if_neg hβ]
      simp
  · obtain ⟨-, -, m10, m11, m30, -, -⟩ := hb3a_mem β
    rw [g2, g4, hexSum_two_sites _ _ _ _ (by decide), hexSum_two_sites _ _ _ _ (by decide)]
    simp only [m10, m11, m30]
  · obtain ⟨-, -, m10, -, -, m31, -⟩ := hb3a_mem ![0, 0]
    rw [g1, hexSum_two_sites _ _ _ _ (by decide)]
    simp only [m10, m31, if_true]
    rw [if_neg (show (![1, 0] : Fin 2 → ℕ) ≠ ![0, 0] by decide)]
    simp [Fin.sum_univ_six, hexDir, -ZMod.natCast_val, ZMod.val_one_eq_one_mod]
  · obtain ⟨-, m01, -, -, -, -, m03⟩ := hb3a_mem ![0, 0]
    rw [g3, hexSum_two_sites _ _ _ _ (by decide)]
    simp only [m01, m03, if_true]
    rw [if_neg (show (![0, 1] : Fin 2 → ℕ) ≠ ![0, 0] by decide)]
    simp [Fin.sum_univ_six, hexDir, -ZMod.natCast_val, ZMod.val_one_eq_one_mod]

/-- **`HB3-a` — NO COARSE RULE CLOSES ON THE BLOCK-CHARGE TWO-TIME STATE** at `L = 4`, `b = 2`:
there is no `Ψ` with `hexSum β w (Φ c) = Ψ (blocks at t, blocks at t − 1) β w` for all `c`, the
blocks carrying `(hexSum β 1, hexSum β d₁, hexSum β d₂)`. **Reported status for H3: HO** — this
block variable needs more than its own two-time state to predict its next value; nothing is said
about a statistical closure at another scale or in another variable, and no timescale is
asserted. -/
theorem hb3a_no_closure :
    ¬ ∃ Ψ : ((Fin 2 → ℕ) → Fin 3 → ℤ) × ((Fin 2 → ℕ) → Fin 3 → ℤ) → (Fin 2 → ℕ) → Fin 3 → ℤ,
      ∀ c : (Fin 2 → ZMod 4) → Fin 6 → ZMod 2, ∀ (β : Fin 2 → ℕ) (j : Fin 3),
        hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
            (![1, fun k => hexDir k 0, fun k => hexDir k 1] j) (hexGas 4 c)
          = Ψ (fun β j => hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
                  (![1, fun k => hexDir k 0, fun k => hexDir k 1] j) c,
                fun β j => hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
                  (![1, fun k => hexDir k 0, fun k => hexDir k 1] j) ((hexGas 4).symm c)) β j := by
  rintro ⟨Ψ, hΨ⟩
  obtain ⟨c, c', -, -, ht, htm, h1, h0⟩ := hb3a_block_state_not_closed
  have hstate : (fun β j => hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
        (![1, fun k => hexDir k 0, fun k => hexDir k 1] j) c,
      fun β j => hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
        (![1, fun k => hexDir k 0, fun k => hexDir k 1] j) ((hexGas 4).symm c))
      = (fun β j => hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
        (![1, fun k => hexDir k 0, fun k => hexDir k 1] j) c',
      fun β j => hexSum (univ.filter fun i : Fin 2 → ZMod 4 => (fun j => (i j).val / 2) = β)
        (![1, fun k => hexDir k 0, fun k => hexDir k 1] j) ((hexGas 4).symm c')) := by
    refine Prod.ext ?_ ?_
    · funext β j
      exact ht β _
    · funext β j
      exact htm β _
  have e1 := hΨ c ![0, 0] 1
  have e2 := hΨ c' ![0, 0] 1
  rw [hstate, ← e2] at e1
  simp only [Matrix.cons_val_one, Matrix.cons_val_zero] at e1
  rw [h1, h0] at e1
  exact absurd e1 (by decide)

variable (L : ℕ) [NeZero L]

/-- **`HB3-b` — THE CHARGE SECTORS ARE INVARIANT**: for every `m : ℤ` and `p : ℤ × ℤ`, the gas maps
`{c | M c = m ∧ (P₁ c, P₂ c) = p}` bijectively onto itself, so the counting measure on each charge
sector is `Φ`-invariant. Immediate from `HB1-c` and bijectivity. This is the exact statement that
sits beneath any local-equilibrium hypothesis for the candidate, and all the round says in that
direction: it licenses no ergodicity, mixing or equidistribution statement within a sector. -/
theorem hexGas_bijOn_sector (m : ℤ) (p : ℤ × ℤ) :
    Set.BijOn (hexGas L)
      {c | hexSum univ 1 c = m
        ∧ (hexSum univ (fun k => hexDir k 0) c, hexSum univ (fun k => hexDir k 1) c) = p}
      {c | hexSum univ 1 c = m
        ∧ (hexSum univ (fun k => hexDir k 0) c, hexSum univ (fun k => hexDir k 1) c) = p} := by
  refine ⟨fun c hc => ?_, (hexGas L).injective.injOn, fun c hc => ⟨(hexGas L).symm c, ?_,
    Equiv.apply_symm_apply _ _⟩⟩
  · simp only [Set.mem_ofPred_eq] at hc ⊢
    rw [hexSum_mass_hexGas, hexSum_momentum_hexGas, hexSum_momentum_hexGas]
    exact hc
  · simp only [Set.mem_ofPred_eq] at hc ⊢
    rw [← hexSum_mass_hexGas L ((hexGas L).symm c), ← hexSum_momentum_hexGas L 0 ((hexGas L).symm c),
      ← hexSum_momentum_hexGas L 1 ((hexGas L).symm c), Equiv.apply_symm_apply]
    exact hc

end Block

/-! ### Section G — `HB1-e`: covariance under the lattice's `60°` rotation -/

section Rotation

variable (L : ℕ)

/-- **THE `60°` LATTICE ROTATION ON CONFIGURATIONS** (budget slot 8, conditional, fired) —
`ρ (a, b) := (−b, a + b)` carries `c_k` to `c_{k+1}`; it acts on configurations by
`(ρ·c) (ρ i) (k + 1) := c i k`, i.e. `(ρ·c) i k = c (ρ⁻¹ i) (k − 1)` with
`ρ⁻¹ (a, b) = (a + b, −a)`. -/
def hexRot : Equiv.Perm ((Fin 2 → ZMod L) → Fin 6 → ZMod 2) where
  toFun c i k := c ![i 0 + i 1, -(i 0)] (k - 1)
  invFun c i k := c ![-(i 1), i 0 + i 1] (k + 1)
  left_inv c := by
    funext i k
    have hi : (![-(i 1) + (i 0 + i 1), -(-(i 1))] : Fin 2 → ZMod L) = i := by
      funext j
      fin_cases j <;> simp
    show c ![-(i 1) + (i 0 + i 1), -(-(i 1))] (k + 1 - 1) = c i k
    rw [hi, add_sub_cancel_right]
  right_inv c := by
    funext i k
    have hi : (![-(-(i 0)), i 0 + i 1 + -(i 0)] : Fin 2 → ZMod L) = i := by
      funext j
      fin_cases j <;> simp
    show c ![-(-(i 0)), i 0 + i 1 + -(i 0)] (k - 1 + 1) = c i k
    rw [hi, sub_add_cancel]

theorem hexRot_apply (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) (i : Fin 2 → ZMod L) (k : Fin 6) :
    hexRot L c i k = c ![i 0 + i 1, -(i 0)] (k - 1) := rfl

theorem hexRot_apply' (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) (i : Fin 2 → ZMod L) :
    hexRot L c i = fun k => c ![i 0 + i 1, -(i 0)] (k - 1) := rfl

/-- `ρ⁻¹` is linear and carries `c_k` to `c_{k−1}`: `ρ⁻¹ (i − c_k) = ρ⁻¹ i − c_{k−1}`. -/
theorem hexRot_site (i : Fin 2 → ZMod L) (k : Fin 6) :
    (![(i - fun j => (hexDir k j : ZMod L)) 0 + (i - fun j => (hexDir k j : ZMod L)) 1,
        -((i - fun j => (hexDir k j : ZMod L)) 0)] : Fin 2 → ZMod L)
      = ![i 0 + i 1, -(i 0)] - fun j => (hexDir (k - 1) j : ZMod L) := by
  obtain ⟨h0, h1⟩ := hexDir_sub_one k
  funext j
  fin_cases j
  · simp [h0]
    ring
  · simp [h1]
    ring

/-- **`HB1-e` — THE GAS COMMUTES WITH THE `60°` ROTATION**: `Φ (ρ·c) = ρ·(Φ c)` for every `c`,
because streaming is carried along by `ρ⁻¹ (i − c_k) = ρ⁻¹ i − c_{k−1}` and the collision
commutes with the channel rotation on all 64 states. -/
theorem hexGas_hexRot (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) :
    hexGas L (hexRot L c) = hexRot L (hexGas L c) := by
  funext i k
  rw [hexRot_apply, hexGas_apply, hexGas_apply, hexRot_apply', hexCollide_channel_rot, hexRot_site]

variable [NeZero L]

/-- Under the rotation, a channel-weighted total is the total with the weight rotated. -/
theorem hexSum_hexRot (w : Fin 6 → ℤ) (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) :
    hexSum univ w (hexRot L c) = hexSum univ (fun k => w (k + 1)) c := by
  unfold hexSum
  have hbij : Function.Bijective
      fun i : Fin 2 → ZMod L => (![i 0 + i 1, -(i 0)] : Fin 2 → ZMod L) :=
    Function.bijective_iff_has_inverse.mpr ⟨fun i => ![-(i 1), i 0 + i 1],
      fun i => by funext j; fin_cases j <;> simp, fun i => by funext j; fin_cases j <;> simp⟩
  rw [← hbij.sum_comp fun i => ∑ k, ((c i k).val : ℤ) * w (k + 1)]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [← Equiv.sum_comp (Equiv.addRight (1 : Fin 6))
    fun k => ((hexRot L c i k).val : ℤ) * w k]
  refine Finset.sum_congr rfl fun k _ => ?_
  simp only [Equiv.coe_addRight, hexRot_apply, add_sub_cancel_right]

/-- **`HB1-e` — MASS IS `ρ`-INVARIANT AND MOMENTUM IS `ρ`-COVARIANT**:
`(P₁, P₂) (ρ·c) = (−P₂ c, P₁ c + P₂ c) = ρ (P₁ c, P₂ c)`. -/
theorem hexRot_charges (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) :
    hexSum univ 1 (hexRot L c) = hexSum univ 1 c
    ∧ hexSum univ (fun k => hexDir k 0) (hexRot L c) = -hexSum univ (fun k => hexDir k 1) c
    ∧ hexSum univ (fun k => hexDir k 1) (hexRot L c)
        = hexSum univ (fun k => hexDir k 0) c + hexSum univ (fun k => hexDir k 1) c := by
  refine ⟨?_, ?_, ?_⟩
  · rw [hexSum_hexRot]
    rfl
  · rw [hexSum_hexRot, ← hexSum_neg_weight]
    congr 1
    funext k
    exact (hexDir_add_one k).1
  · rw [hexSum_hexRot, ← hexSum_add_weight]
    congr 1
    funext k
    exact (hexDir_add_one k).2

end Rotation

end HexLatticeGas
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.HexLatticeGas.hexDir_add_three
#print axioms OIBridge.HexLatticeGas.hexDir_cast_add_three
#print axioms OIBridge.HexLatticeGas.hexDir_add_one
#print axioms OIBridge.HexLatticeGas.hexDir_sub_one
#print axioms OIBridge.HexLatticeGas.hexDir_conditions
#print axioms OIBridge.HexLatticeGas.hexCollide_apply
#print axioms OIBridge.HexLatticeGas.hexCollide_moved
#print axioms OIBridge.HexLatticeGas.hexCollide_of_ne
#print axioms OIBridge.HexLatticeGas.hexCollide_symm_of_ne
#print axioms OIBridge.HexLatticeGas.hexCollide_moved_support
#print axioms OIBridge.HexLatticeGas.hexCollide_of_single
#print axioms OIBridge.HexLatticeGas.hexCollide_symm_of_single
#print axioms OIBridge.HexLatticeGas.hexCollide_zero
#print axioms OIBridge.HexLatticeGas.hexCollide_channel_rot
#print axioms OIBridge.HexLatticeGas.hexCollide_not_reflection
#print axioms OIBridge.HexLatticeGas.hexStream_apply
#print axioms OIBridge.HexLatticeGas.hexGas_eq
#print axioms OIBridge.HexLatticeGas.hexGas_apply
#print axioms OIBridge.HexLatticeGas.hexGas_symm_apply
#print axioms OIBridge.HexLatticeGas.hexSubstratum_F
#print axioms OIBridge.HexLatticeGas.hexSubstratum_N
#print axioms OIBridge.HexLatticeGas.hexSubstratum_A1
#print axioms OIBridge.HexLatticeGas.hexSubstratum_A2
#print axioms OIBridge.HexLatticeGas.hexSubstratum_A3
#print axioms OIBridge.HexLatticeGas.hexSubstratum_A4Exact
#print axioms OIBridge.HexLatticeGas.hexSubstratum_A4
#print axioms OIBridge.HexLatticeGas.hexSum_apply
#print axioms OIBridge.HexLatticeGas.hexSum_single
#print axioms OIBridge.HexLatticeGas.hexSum_single_site
#print axioms OIBridge.HexLatticeGas.hexSum_two_sites
#print axioms OIBridge.HexLatticeGas.hexSum_neg_weight
#print axioms OIBridge.HexLatticeGas.hexSum_add_weight
#print axioms OIBridge.HexLatticeGas.hexSum_intCast_two
#print axioms OIBridge.HexLatticeGas.hexSum_add_intCast_two
#print axioms OIBridge.HexLatticeGas.hexSum_hexStream
#print axioms OIBridge.HexLatticeGas.hexCollide_conserved_iff
#print axioms OIBridge.HexLatticeGas.collide_single
#print axioms OIBridge.HexLatticeGas.hexSum_collide_iff
#print axioms OIBridge.HexLatticeGas.hexCollide_conditions_iff_span
#print axioms OIBridge.HexLatticeGas.hexSum_hexGas
#print axioms OIBridge.HexLatticeGas.hexSum_hexGas_iff
#print axioms OIBridge.HexLatticeGas.hexSum_hexGas_iff_span
#print axioms OIBridge.HexLatticeGas.hexSum_mass_hexGas
#print axioms OIBridge.HexLatticeGas.hexSum_momentum_hexGas
#print axioms OIBridge.HexLatticeGas.hexSum_shiftBy
#print axioms OIBridge.HexLatticeGas.single_channel_zero
#print axioms OIBridge.HexLatticeGas.hexGas_single_channel
#print axioms OIBridge.HexLatticeGas.hexGas_symm_single_channel
#print axioms OIBridge.HexLatticeGas.hexCollide_symm_channel_one
#print axioms OIBridge.HexLatticeGas.hexSubstratum_A5_witness
#print axioms OIBridge.HexLatticeGas.hexSubstratum_not_A5
#print axioms OIBridge.HexLatticeGas.hexSubstratum_sector
#print axioms OIBridge.HexLatticeGas.hexSum_leap_sector
#print axioms OIBridge.HexLatticeGas.hexSubstratum_mass_not_conserved_off_sector
#print axioms OIBridge.HexLatticeGas.hexMoment2_eq
#print axioms OIBridge.HexLatticeGas.hexMoment4_eq
#print axioms OIBridge.HexLatticeGas.hexMoment4_quartic
#print axioms OIBridge.HexLatticeGas.hexMoment4_isotropic
#print axioms OIBridge.HexLatticeGas.axisMoment4_two_not_isotropic
#print axioms OIBridge.HexLatticeGas.hexMoment6_not_isotropic
#print axioms OIBridge.HexLatticeGas.hb3a_gas_values
#print axioms OIBridge.HexLatticeGas.hb3a_mem
#print axioms OIBridge.HexLatticeGas.hb3a_block_state_not_closed
#print axioms OIBridge.HexLatticeGas.hb3a_no_closure
#print axioms OIBridge.HexLatticeGas.hexGas_bijOn_sector
#print axioms OIBridge.HexLatticeGas.hexRot_apply
#print axioms OIBridge.HexLatticeGas.hexRot_apply'
#print axioms OIBridge.HexLatticeGas.hexRot_site
#print axioms OIBridge.HexLatticeGas.hexGas_hexRot
#print axioms OIBridge.HexLatticeGas.hexSum_hexRot
#print axioms OIBridge.HexLatticeGas.hexRot_charges
