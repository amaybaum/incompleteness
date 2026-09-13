import OIBridge.SubstratumInterfaceAudit
import OIBridge.CubicIsotropy

/-!
# Hydrodynamics round H-A — the source audit of the concrete wave representative

Executed under the frozen control plane
`verification/programmes/hydrodynamics/round-h-a-source-audit/preregistration.md`, blob
`934cd6aff1cfb07b823c9b131693ee59bb98c632`, from `main` at
`ae81459372887cfbe27b427b30bbdad1b564f2b7` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base.

## The object

Exactly the kernel's `waveSubstratum d L q α`: sites `Fin d → ZMod L`, alphabet `ZMod q`, and the
second-order update in phase-space form `x_{t+1} = F(x_t) − x_{t−1}` with
`F(x)(i) = α · Σ_{p : Fin d × Bool} x(i + dir p)` — `α` times the sum over the `2d` axis neighbours.
The trajectory step is the kernel's `leap`: `curOf (leap F x) = F (curOf x) − prevOf x`. `q` is a
gauge parameter by [SM §2.7] and [Substratum, Theorem 24 (ii)]; **there is no manuscript-fixed `q`
to discover**, and this module does not go looking for one. `waveF`, `waveRule`,
`waveSubstratum`, `waveSubstratum_A5`, `dir`, `leap`, `curOf`, `prevOf`, `IsSign`, `flip`,
`isSign_flip`, `quartic_ohInvariant` and `quartic_not_isotropic` are consumed unmodified; none is
re-proved.

## The targets, and what each is read as

* **`H0` — the linearity gate** (Section A). For every additive coarse map `C : (ι → V) →+ (B → V)`
  and every additive microscopic rule, the coarse two-time evolution
  `(x_{t−1}, x_t) ↦ (C x_t, C x_{t+1})` is additive (`coarse_evolution_additive`), and any coarse
  rule `Φ` that **closes** (`CoarseCloses`) agrees with an additive map on the range of `(C, C)`
  (`coarseCloses_additive_on_range`), hence is `ℕ`-homogeneous of degree one there
  (`coarseCloses_nsmul`). Over `ZMod q` additive is `ZMod q`-linear. **Status for the advection
  obligation: HI, conditional on the coarse-variable class** — `ZMod q`-linear coarse-graining,
  named in the statement. **Real-valued or nonlinear coarse variables are HO**: the mod-`q`
  wraparound is *a* nonlinearity of a faithful finite realization, not shown to be the only one,
  and whether a real lift followed by products carries an advective term is neither asked nor
  answered here.
* **`H1` — the total-sum conservation law and its `q`-gauge invariance** (Section B). On the torus
  `Σ_i F(x)(i) = 2dα · Σ_i x(i)` (`totalSum_waveF`), so `S_{t+1} = 2dα S_t − S_{t−1}`
  (`totalSum_leap`). `H1-a`: `ΔS = S_t − S_{t−1}` is conserved on every trajectory **iff**
  `(2dα − 2 : ZMod q) = 0` (`deltaS_conserved_iff`). `H1-b`: `a S_t + b S_{t−1}` is conserved on
  every trajectory iff `b = −a` and `a (2dα − 2) = 0` (`combination_conserved_iff`). `H1-c`, the
  manuscript instance `d = 3`, `α = 1`: conserved iff `q ∣ 4` (`deltaS_conserved_iff_dvd_four`),
  i.e. for `q ≥ 2` iff `q ∈ {2, 4}` (`deltaS_conserved_iff_two_or_four`). **The `q`-gauge test,
  in the freeze's words**: the candidate conserved field `ΔS` holds for two alphabet sizes and
  fails for every other `q ≥ 2`, so **this candidate field, under this rule, is not `q`-gauge
  invariant**. **This is not a universal no-go for all possible hydrodynamic variables**: block
  variables, real-lifted variables, currents built from differences, and any variable of a
  different substratum are outside `H1` and are HO. **No `q` is chosen to rescue the field.**
* **`H2a` — the fully symmetric rank-4 invariants** (Section C). `SymInvariantQuartic` is the
  fully symmetric, sign-invariant, coordinate-permutation-invariant rank-4 tensors on `ℝ³`, i.e.
  the `O_h`-invariant homogeneous quartic forms. `symInvariantQuartic_iff`: a tensor is one **iff**
  it is `x · D + y · P` for a **unique** pair `(x, y)`, where `D_{abce} = [a = b = c = e]` is the
  tensor of `Σ_i k_i⁴` and `P = δ_{ab}δ_{ce} + δ_{ac}δ_{be} + δ_{ae}δ_{bc}` is three times the
  tensor of `(Σ_i k_i²)²` (`quartic_form_diag`, `quartic_form_pair`): the space is two-dimensional,
  coordinatized by the spanning pair. `symInvariant_isotropic_iff`: such a tensor's form is a
  function of `|k|²` **iff** `x = 0`, so the rotation-invariant ones are exactly the multiples of
  `P`, one-dimensional. **The counts are the fully symmetric ones, 2 versus 1**; general rank-4
  invariant counts are other objects. Reached at evidence level 2; the frozen level-3 fallback is
  not used.
* **`H2b` — the axis stencil against the isotropy the stress expansion needs** (Section C).
  `axisMoment4 d` is the fourth moment `Σ_p (dir p)_a (dir p)_b (dir p)_c (dir p)_e` of the `2d`
  axis directions `±e_k`, taken in the real embedding of the same integer stencil `dir` casts into
  `ZMod L` (`dir_eq_intCast`). It equals `2 · [a = b = c = e]` (`axisMoment4_eq`), its quartic form
  is `2 Σ_i k_i⁴` (`axisMoment4_quartic`), it is `O_h`-invariant (`axisMoment4_symInvariant`) and
  **not** rotation-invariant (`axisMoment4_form_not_isotropic`, `axisMoment4_not_isotropic`,
  consuming `quartic_not_isotropic`). **Status for `H2`: exact stencil anisotropy proved;
  conditional HI if H5's stress closure consumes this tensor; otherwise `H2` remains HO.** Whether
  the bare fourth moment of the stencil is the tensor H5's closure consumes is a bridge this round
  does not build. Corollary 1a's quadratic isotropy is consumed unchanged and not contradicted:
  quadratic order is isotropic, quartic order is not, and Navier–Stokes needs the quartic order.
* **`H3a` — a block-observable diagnostic for closure** (Section D). `blockSum` is the block sum
  over cubes of side `b`. At `d = 1`, `L = 6`, `b = 3`, `α = 1`, for **every** `q ≥ 2`, two
  microscopic pairs with equal block states at `t` and `t − 1` have different block states at
  `t + 1` (`h3a_block_state_not_closed`), so no coarse rule closes on this block variable
  (`h3a_no_closure`). The smaller candidate `L = 4`, `b = 2` is **not** a witness: its block
  variable closes (`h3a_control_L4_closes`). **Status for `H3`: HO.** Non-closure of one exact
  coarse observable is not an impossibility of a statistical closure at another scale or in
  another variable; **no timescale separation is asserted** and no local-equilibrium or mixing
  statement is made in either direction.
* **`H4a`** has no theorem; the scaling skeleton is recorded in the result note. **HO.**

## What none of this licenses

**Nothing here says OI cannot support fluid hydrodynamics.** The findings are about one
representative rule, one stencil, one class of coarse variables, and one candidate conserved field;
round H-B's construction question is untouched and alive. **Nothing here is a continuum
statement**: no limit is taken and no PDE is asserted or denied. **Nothing here changes A1–A6**;
A5 is consumed as proved. **Nothing here bears on the OI → QM chain, on Track B, on Bell, or on
gravity.** The `q`-gauge principle is consumed as the manuscripts state it, not tested. No
manuscript is edited.
-/

namespace OIBridge
namespace HydroSourceAudit

open Finset
open OIBridge.SecondOrderCircuit (leap curOf prevOf)
open OIBridge.SubstratumInterfaceAudit (dir waveF waveRule waveSubstratum waveSubstratum_A5
  Substratum)
open OIBridge.CubicIsotropy (IsSign isSign_flip quartic_ohInvariant quartic_not_isotropic)

/-! ### Section A — `H0`: the linearity gate -/

section Coarse

variable {ι V B : Type} [AddCommGroup V]

/-- **CLOSURE OF A COARSE RULE** (budget slot 3) — a coarse map `C` and a coarse two-time rule
`Φ` close on the microscopic rule `F` when `C x_{t+1} = Φ (C x_t, C x_{t−1})` for **every**
microscopic phase-space configuration, the step being the kernel's `leap`. This is exact closure of
one coarse observable; it is not a statistical closure, and its failure (`H3a`) is not the absence
of one. -/
def CoarseCloses (C : (ι → V) →+ (B → V)) (F : (ι → V) → (ι → V))
    (Φ : (B → V) × (B → V) → (B → V)) : Prop :=
  ∀ x : ι → V × V, C (curOf (leap F x)) = Φ (C (curOf x), C (prevOf x))

theorem curOf_add (x y : ι → V × V) : curOf (x + y) = curOf x + curOf y := rfl

theorem prevOf_add (x y : ι → V × V) : prevOf (x + y) = prevOf x + prevOf y := rfl

/-- The current slice after one step is `F` of the current slice minus the previous slice. -/
theorem curOf_leap (F : (ι → V) → (ι → V)) (x : ι → V × V) :
    curOf (leap F x) = F (curOf x) - prevOf x := rfl

theorem map_zero_of_additive {F : (ι → V) → (ι → V)} (hF : ∀ c c', F (c + c') = F c + F c') :
    F 0 = 0 := by
  have h := hF 0 0
  rw [add_zero] at h
  have h2 : F 0 + F 0 - F 0 = F 0 - F 0 := by rw [← h]
  rwa [add_sub_cancel_right, sub_self] at h2

/-- **`H0-a` — THE COARSE TWO-TIME EVOLUTION IS ADDITIVE.** For every additive coarse map `C` and
every additive microscopic rule `F`, the map `(x_{t−1}, x_t) ↦ (C x_t, C x_{t+1})` is an additive
map of the phase space. Over `ZMod q` an additive map is `ZMod q`-linear, which is the class the
status of `H0` carries. -/
theorem coarse_evolution_additive (C : (ι → V) →+ (B → V)) {F : (ι → V) → (ι → V)}
    (hF : ∀ c c', F (c + c') = F c + F c') :
    ∃ Λ : (ι → V × V) →+ (B → V) × (B → V),
      ∀ x, Λ x = (C (curOf x), C (curOf (leap F x))) := by
  have h0 : curOf (0 : ι → V × V) = 0 := rfl
  have hp : prevOf (0 : ι → V × V) = 0 := rfl
  refine ⟨AddMonoidHom.mk' (fun x => (C (curOf x), C (curOf (leap F x)))) ?_, fun _ => rfl⟩
  intro x y
  refine Prod.ext ?_ ?_
  · simp only [curOf_add, map_add, Prod.fst_add]
  · simp only [curOf_leap, curOf_add, prevOf_add, hF, Prod.snd_add, map_sub, map_add]
    abel

/-- **`H0-b` — A CLOSED COARSE RULE IS ADDITIVE ON THE RANGE OF `(C, C)`.** If `Φ` closes on an
additive `F` through an additive `C`, then on the coarse states `(C x_t, C x_{t−1})` it actually
takes, `Φ` respects addition. **Consequently no closed `ZMod q`-linear coarse description of the
present rule carries a quadratic (advective) term on the coarse states it is defined on.** The
class is `ZMod q`-linear coarse-graining, stated here; real-valued or nonlinear coarse variables
are outside this theorem and are HO. -/
theorem coarseCloses_additive_on_range (C : (ι → V) →+ (B → V)) {F : (ι → V) → (ι → V)}
    (hF : ∀ c c', F (c + c') = F c + F c') {Φ : (B → V) × (B → V) → (B → V)}
    (h : CoarseCloses C F Φ) (x y : ι → V × V) :
    Φ (C (curOf x) + C (curOf y), C (prevOf x) + C (prevOf y))
      = Φ (C (curOf x), C (prevOf x)) + Φ (C (curOf y), C (prevOf y)) := by
  rw [← h x, ← h y, ← map_add, ← map_add, ← curOf_add, ← prevOf_add, ← h (x + y),
    curOf_leap, curOf_leap, curOf_leap, curOf_add, prevOf_add, hF, map_sub, map_sub, map_sub,
    map_add, map_add]
  abel

/-- **`H0-b`, THE DEGREE-ONE CONSEQUENCE.** On the coarse states it takes, a closed coarse rule is
`ℕ`-homogeneous of degree one: `Φ (n · u, n · v) = n · Φ (u, v)`. An advective term `(u·∇)u` is
quadratic and would scale as `n²`; it cannot appear on the range of a `ZMod q`-linear
coarse-graining of an additive rule. -/
theorem coarseCloses_nsmul (C : (ι → V) →+ (B → V)) {F : (ι → V) → (ι → V)}
    (hF : ∀ c c', F (c + c') = F c + F c') {Φ : (B → V) × (B → V) → (B → V)}
    (h : CoarseCloses C F Φ) (x : ι → V × V) (n : ℕ) :
    Φ (n • C (curOf x), n • C (prevOf x)) = n • Φ (C (curOf x), C (prevOf x)) := by
  have hc : ∀ m : ℕ, curOf (m • x) = m • curOf x := fun _ => rfl
  have hp : ∀ m : ℕ, prevOf (m • x) = m • prevOf x := fun _ => rfl
  have key : ∀ m : ℕ, Φ (C (curOf (m • x)), C (prevOf (m • x)))
      = m • Φ (C (curOf x), C (prevOf x)) := by
    intro m
    induction m with
    | zero =>
      have h0 : curOf (0 : ι → V × V) = 0 := rfl
      have hp0 : prevOf (0 : ι → V × V) = 0 := rfl
      rw [zero_smul, zero_smul, ← h 0, curOf_leap, h0, hp0, map_zero_of_additive hF, sub_zero,
        map_zero]
    | succ m ih =>
      rw [succ_nsmul, curOf_add, prevOf_add, map_add, map_add,
        coarseCloses_additive_on_range C hF h, ih, succ_nsmul]
  rw [← map_nsmul, ← map_nsmul, ← hc, ← hp, key]

end Coarse

section WaveH0

variable (d L q : ℕ) (α : ZMod q) {B : Type}

/-- The wave substratum's rule is `waveF`, by definition. -/
theorem waveSubstratum_F : (waveSubstratum d L q α).R.F = waveF d L q α := rfl

/-- **`H0-a` FOR THE WAVE SUBSTRATUM**, consuming `waveSubstratum_A5`. -/
theorem wave_coarse_evolution_additive (C : ((Fin d → ZMod L) → ZMod q) →+ (B → ZMod q)) :
    ∃ Λ : ((Fin d → ZMod L) → ZMod q × ZMod q) →+ (B → ZMod q) × (B → ZMod q),
      ∀ x, Λ x = (C (curOf x), C (curOf (leap (waveF d L q α) x))) :=
  coarse_evolution_additive C (waveSubstratum_A5 d L q α)

/-- **`H0-b` FOR THE WAVE SUBSTRATUM**, consuming `waveSubstratum_A5`. -/
theorem wave_coarseCloses_additive_on_range (C : ((Fin d → ZMod L) → ZMod q) →+ (B → ZMod q))
    {Φ : (B → ZMod q) × (B → ZMod q) → (B → ZMod q)} (h : CoarseCloses C (waveF d L q α) Φ)
    (x y : (Fin d → ZMod L) → ZMod q × ZMod q) :
    Φ (C (curOf x) + C (curOf y), C (prevOf x) + C (prevOf y))
      = Φ (C (curOf x), C (prevOf x)) + Φ (C (curOf y), C (prevOf y)) :=
  coarseCloses_additive_on_range C (waveSubstratum_A5 d L q α) h x y

end WaveH0

/-! ### Section B — `H1`: the total-sum conservation law and its `q`-gauge invariance -/

section TotalSum

variable {ι V : Type} [Fintype ι] [AddCommMonoid V]

/-- **THE TOTAL SUM** (budget slot 1) — `S(x) = Σ_i x(i)`, as an additive functional; over
`ZMod q` that is a `ZMod q`-linear functional. -/
def totalSum : (ι → V) →+ V where
  toFun x := ∑ i, x i
  map_zero' := by simp
  map_add' x y := by
    show ∑ i, (x i + y i) = ∑ i, x i + ∑ i, y i
    exact Finset.sum_add_distrib

theorem totalSum_apply (x : ι → V) : totalSum x = ∑ i, x i := rfl

end TotalSum

section WaveH1

variable (d L q : ℕ) [NeZero L] (α : ZMod q)

/-- **THE TORUS SUM IDENTITY**: every translate of a configuration has the same total, so
`Σ_i F(x)(i) = 2dα · Σ_i x(i)`. -/
theorem totalSum_waveF (x : (Fin d → ZMod L) → ZMod q) :
    totalSum (waveF d L q α x) = 2 * d * α * totalSum x := by
  rw [totalSum_apply, totalSum_apply]
  unfold waveF
  rw [← Finset.mul_sum, Finset.sum_comm]
  have hshift : ∀ p : Fin d × Bool, ∑ i, x (i + dir d L p) = ∑ i, x i := fun p =>
    Equiv.sum_comp (Equiv.addRight (dir d L p)) x
  simp only [hshift, Finset.sum_const, Finset.card_univ, Fintype.card_prod, Fintype.card_fin,
    Fintype.card_bool, nsmul_eq_mul]
  push_cast
  ring

/-- **THE ZERO-MODE RECURRENCE**: `S_{t+1} = 2dα S_t − S_{t−1}` along every trajectory. -/
theorem totalSum_leap (x : (Fin d → ZMod L) → ZMod q × ZMod q) :
    totalSum (curOf (leap (waveF d L q α) x))
      = 2 * d * α * totalSum (curOf x) - totalSum (prevOf x) := by
  rw [curOf_leap, map_sub, totalSum_waveF]

/-- **A RECORDED READING OF THE COEFFICIENT, ANALYSIS ONLY**: the zero-mode second difference is
`(2dα − 2) S_t`, the on-site coefficient a discrete Laplacian would cancel and this rule does not.
This is an interpretation of the same identity, not a separate target, and it licenses no claim
about a mass, a metric, or a continuum operator. -/
theorem totalSum_second_difference (x : (Fin d → ZMod L) → ZMod q × ZMod q) :
    totalSum (curOf (leap (waveF d L q α) x)) - 2 * totalSum (curOf x) + totalSum (prevOf x)
      = (2 * d * α - 2) * totalSum (curOf x) := by
  rw [totalSum_leap]
  ring

theorem totalSum_single :
    totalSum (Pi.single (0 : Fin d → ZMod L) (1 : ZMod q) : (Fin d → ZMod L) → ZMod q) = 1 := by
  rw [totalSum_apply, Finset.sum_pi_single']
  simp

/-- **`H1-a` — THE FIRST DIFFERENCE OF THE TOTAL SUM IS CONSERVED ON EVERY TRAJECTORY IFF
`2dα − 2 = 0` IN `ZMod q`.** Forward: the trajectory with `x_{t−1} = 0` and `x_t = δ_{i₀}` (one
site, which a nonempty torus supplies) has `ΔS_t = 1` and `ΔS_{t+1} = 2dα − 2`. Backward:
`ΔS_{t+1} = (2dα − 2) S_t + ΔS_t`. -/
theorem deltaS_conserved_iff :
    (∀ x : (Fin d → ZMod L) → ZMod q × ZMod q,
        totalSum (curOf (leap (waveF d L q α) x)) - totalSum (curOf x)
          = totalSum (curOf x) - totalSum (prevOf x))
      ↔ (2 * d * α - 2 : ZMod q) = 0 := by
  constructor
  · intro h
    have hx := h (fun i => ((0 : ZMod q),
      (Pi.single (0 : Fin d → ZMod L) (1 : ZMod q) : (Fin d → ZMod L) → ZMod q) i))
    have hc : curOf (fun i => ((0 : ZMod q),
        (Pi.single (0 : Fin d → ZMod L) (1 : ZMod q) : (Fin d → ZMod L) → ZMod q) i))
        = Pi.single 0 1 := rfl
    have hp : prevOf (fun i => ((0 : ZMod q),
        (Pi.single (0 : Fin d → ZMod L) (1 : ZMod q) : (Fin d → ZMod L) → ZMod q) i))
        = 0 := rfl
    rw [totalSum_leap, hc, hp, map_zero, totalSum_single] at hx
    linear_combination hx
  · intro h x
    rw [totalSum_leap]
    linear_combination totalSum (curOf x) * h

/-- **`H1-b` — THE CLASSIFICATION OF CONSERVED TOTAL-SUM COMBINATIONS.** `a S_t + b S_{t−1}` is
conserved on every trajectory iff `b = −a` and `a · (2dα − 2) = 0`: the first difference is the
only shape a universally conserved total-sum combination can take, available exactly when the
coefficient `2dα − 2` annihilates `a`. -/
theorem combination_conserved_iff (a b : ZMod q) :
    (∀ x : (Fin d → ZMod L) → ZMod q × ZMod q,
        a * totalSum (curOf (leap (waveF d L q α) x)) + b * totalSum (curOf x)
          = a * totalSum (curOf x) + b * totalSum (prevOf x))
      ↔ (b = -a ∧ a * (2 * d * α - 2) = 0) := by
  constructor
  · intro h
    have h1 := h (fun i => ((0 : ZMod q),
      (Pi.single (0 : Fin d → ZMod L) (1 : ZMod q) : (Fin d → ZMod L) → ZMod q) i))
    have h2 := h (fun i =>
      ((Pi.single (0 : Fin d → ZMod L) (1 : ZMod q) : (Fin d → ZMod L) → ZMod q) i, (0 : ZMod q)))
    have hc1 : curOf (fun i => ((0 : ZMod q),
        (Pi.single (0 : Fin d → ZMod L) (1 : ZMod q) : (Fin d → ZMod L) → ZMod q) i))
        = Pi.single 0 1 := rfl
    have hp1 : prevOf (fun i => ((0 : ZMod q),
        (Pi.single (0 : Fin d → ZMod L) (1 : ZMod q) : (Fin d → ZMod L) → ZMod q) i))
        = 0 := rfl
    have hc2 : curOf (fun i =>
        ((Pi.single (0 : Fin d → ZMod L) (1 : ZMod q) : (Fin d → ZMod L) → ZMod q) i, (0 : ZMod q)))
        = 0 := rfl
    have hp2 : prevOf (fun i =>
        ((Pi.single (0 : Fin d → ZMod L) (1 : ZMod q) : (Fin d → ZMod L) → ZMod q) i, (0 : ZMod q)))
        = Pi.single 0 1 := rfl
    rw [totalSum_leap, hc1, hp1, map_zero, totalSum_single] at h1
    rw [totalSum_leap, hc2, hp2, map_zero, totalSum_single] at h2
    constructor
    · linear_combination (-1 : ZMod q) * h2
    · linear_combination h1 + h2
  · rintro ⟨rfl, h⟩ x
    rw [totalSum_leap]
    linear_combination totalSum (curOf x) * h

/-- **`H1-c` — THE MANUSCRIPT INSTANCE `d = 3`, `α = 1`**: `ΔS` is conserved on every trajectory
iff `q ∣ 4`. -/
theorem deltaS_conserved_iff_dvd_four :
    (∀ x : (Fin 3 → ZMod L) → ZMod q × ZMod q,
        totalSum (curOf (leap (waveF 3 L q 1) x)) - totalSum (curOf x)
          = totalSum (curOf x) - totalSum (prevOf x))
      ↔ q ∣ 4 := by
  rw [deltaS_conserved_iff]
  have h4 : (2 * (3 : ℕ) * (1 : ZMod q) - 2 : ZMod q) = ((4 : ℕ) : ZMod q) := by
    push_cast
    ring
  rw [h4, ZMod.natCast_eq_zero_iff]

/-- **`H1-c`, THE EXACT SET**: for `q ≥ 2`, `ΔS` is conserved on every trajectory of the
manuscript instance iff `q ∈ {2, 4}`. **The candidate field holds for two alphabet sizes and fails
for every other `q ≥ 2`; under the `q`-gauge principle it is therefore not `q`-gauge invariant.**
This is a statement about this candidate field under this rule, not a universal no-go, and no `q`
is chosen to rescue it. -/
theorem deltaS_conserved_iff_two_or_four (hq : 2 ≤ q) :
    (∀ x : (Fin 3 → ZMod L) → ZMod q × ZMod q,
        totalSum (curOf (leap (waveF 3 L q 1) x)) - totalSum (curOf x)
          = totalSum (curOf x) - totalSum (prevOf x))
      ↔ (q = 2 ∨ q = 4) := by
  rw [deltaS_conserved_iff_dvd_four]
  constructor
  · intro h
    have hle : q ≤ 4 := Nat.le_of_dvd (by norm_num) h
    interval_cases q <;> simp_all
  · rintro (rfl | rfl) <;> norm_num

end WaveH1

/-! ### Section C — `H2a`, `H2b`: the fourth-rank tensor and the axis stencil against it -/

section Quartic

/-- **FULLY SYMMETRIC `O_h`-INVARIANT RANK-4 DATA** (budget slot 5) — a rank-4 tensor on `ℝ³`
that is fully symmetric (invariant under the three adjacent slot transpositions, which generate
`S_4`), invariant under every sign flip of the axes, and invariant under every coordinate
permutation. Identified with the `O_h`-invariant homogeneous quartic forms through
`k ↦ Σ_{abce} T_{abce} k_a k_b k_c k_e`. -/
def SymInvariantQuartic (T : Fin 3 → Fin 3 → Fin 3 → Fin 3 → ℝ) : Prop :=
  ((∀ a b c e, T a b c e = T b a c e) ∧ (∀ a b c e, T a b c e = T a c b e)
      ∧ (∀ a b c e, T a b c e = T a b e c))
    ∧ (∀ ε : Fin 3 → ℝ, IsSign ε → ∀ a b c e, ε a * ε b * ε c * ε e * T a b c e = T a b c e)
    ∧ (∀ σ : Equiv.Perm (Fin 3), ∀ a b c e, T (σ a) (σ b) (σ c) (σ e) = T a b c e)

/-- **ROTATION INVARIANCE OF A QUARTIC FORM** (budget slot 6) — the form of `T` is a function of
`|k|²`: two vectors of the same length give it the same value. For a homogeneous polynomial this
is rotation invariance, since the rotations act transitively on each sphere; it is the notion
`quartic_not_isotropic` already speaks in. -/
def IsotropicQuartic (T : Fin 3 → Fin 3 → Fin 3 → Fin 3 → ℝ) : Prop :=
  ∀ k k' : Fin 3 → ℝ, (∑ i, k i ^ 2) = (∑ i, k' i ^ 2) →
    (∑ a, ∑ b, ∑ c, ∑ e, T a b c e * (k a * k b * k c * k e))
      = ∑ a, ∑ b, ∑ c, ∑ e, T a b c e * (k' a * k' b * k' c * k' e)

/-- The quartic form of the diagonal tensor `D_{abce} = [a = b = c = e]` is `Σ_i k_i⁴`. -/
theorem quartic_form_diag (k : Fin 3 → ℝ) :
    (∑ a, ∑ b, ∑ c, ∑ e, (if a = b ∧ b = c ∧ c = e then (1 : ℝ) else 0)
        * (k a * k b * k c * k e))
      = ∑ i, k i ^ 4 := by
  simp only [Fin.sum_univ_three]
  simp
  ring

/-- The quartic form of `P = δ_{ab}δ_{ce} + δ_{ac}δ_{be} + δ_{ae}δ_{bc}` is `3 (Σ_i k_i²)²`. -/
theorem quartic_form_pair (k : Fin 3 → ℝ) :
    (∑ a, ∑ b, ∑ c, ∑ e, ((if a = b then (1 : ℝ) else 0) * (if c = e then 1 else 0)
          + (if a = c then 1 else 0) * (if b = e then 1 else 0)
          + (if a = e then 1 else 0) * (if b = c then 1 else 0))
        * (k a * k b * k c * k e))
      = 3 * (∑ i, k i ^ 2) ^ 2 := by
  simp only [Fin.sum_univ_three]
  simp
  ring

/-- The quartic form of `x · D + y · P` is `x Σ_i k_i⁴ + y · 3 (Σ_i k_i²)²`. -/
theorem quartic_form_span (x y : ℝ) (k : Fin 3 → ℝ) :
    (∑ a, ∑ b, ∑ c, ∑ e, (x * (if a = b ∧ b = c ∧ c = e then (1 : ℝ) else 0)
          + y * ((if a = b then (1 : ℝ) else 0) * (if c = e then 1 else 0)
            + (if a = c then 1 else 0) * (if b = e then 1 else 0)
            + (if a = e then 1 else 0) * (if b = c then 1 else 0)))
        * (k a * k b * k c * k e))
      = x * (∑ i, k i ^ 4) + y * (3 * (∑ i, k i ^ 2) ^ 2) := by
  rw [← quartic_form_diag, ← quartic_form_pair, Finset.mul_sum, Finset.mul_sum,
    ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun e _ => ?_
  ring

/-- A sign flip kills every entry whose first index differs from the other three. -/
theorem symInvariant_eq_zero_of_single {T : Fin 3 → Fin 3 → Fin 3 → Fin 3 → ℝ}
    (h : SymInvariantQuartic T) {a b c e : Fin 3} (hab : a ≠ b) (hac : a ≠ c) (hae : a ≠ e) :
    T a b c e = 0 := by
  have hf := h.2.1 (OIBridge.CubicIsotropy.flip a) (isSign_flip a) a b c e
  have h1 : OIBridge.CubicIsotropy.flip a a = -1 := by simp [OIBridge.CubicIsotropy.flip]
  have h2 : OIBridge.CubicIsotropy.flip a b = 1 := by
    simp [OIBridge.CubicIsotropy.flip, Ne.symm hab]
  have h3 : OIBridge.CubicIsotropy.flip a c = 1 := by
    simp [OIBridge.CubicIsotropy.flip, Ne.symm hac]
  have h4 : OIBridge.CubicIsotropy.flip a e = 1 := by
    simp [OIBridge.CubicIsotropy.flip, Ne.symm hae]
  rw [h1, h2, h3, h4] at hf
  linarith

/-- For `a ≠ c` there is a coordinate permutation carrying `0 ↦ a` and `1 ↦ c`. -/
theorem exists_perm_zero_one {a c : Fin 3} (hac : a ≠ c) :
    ∃ σ : Equiv.Perm (Fin 3), σ 0 = a ∧ σ 1 = c := by
  classical
  set τ : Equiv.Perm (Fin 3) := Equiv.swap 0 a with hτ
  have hτ0 : τ 0 = a := by rw [hτ]; exact Equiv.swap_apply_left 0 a
  have hc' : τ c ≠ 0 := by
    intro h0
    apply hac
    have := congrArg τ h0
    rw [Equiv.swap_apply_self, hτ0] at this
    exact this.symm
  refine ⟨τ * Equiv.swap 1 (τ c), ?_, ?_⟩
  · rw [Equiv.Perm.mul_apply, Equiv.swap_apply_of_ne_of_ne zero_ne_one (Ne.symm hc'), hτ0]
  · rw [Equiv.Perm.mul_apply, Equiv.swap_apply_left, hτ, Equiv.swap_apply_self]

/-- **THE CLOSED FORM OF A FULLY SYMMETRIC `O_h`-INVARIANT TENSOR**: `T₀₀₀₀` on `aaaa`, `T₀₀₁₁`
on every arrangement of `aabb` with `a ≠ b`, and zero elsewhere — the finite averaging argument,
carried out on the 81 index tuples. -/
theorem symInvariant_closed_form {T : Fin 3 → Fin 3 → Fin 3 → Fin 3 → ℝ}
    (h : SymInvariantQuartic T) (a b c e : Fin 3) :
    T a b c e = if a = b ∧ b = c ∧ c = e then T 0 0 0 0
      else if (a = b ∧ c = e) ∨ (a = c ∧ b = e) ∨ (a = e ∧ b = c) then T 0 0 1 1 else 0 := by
  obtain ⟨t1, ht1⟩ : ∃ t, t = T 0 0 0 0 := ⟨_, rfl⟩
  obtain ⟨t2, ht2⟩ : ∃ t, t = T 0 0 1 1 := ⟨_, rfl⟩
  rw [← ht1, ← ht2]
  have hs1 := h.1.1
  have hs2 := h.1.2.1
  have hs3 := h.1.2.2
  have hperm := h.2.2
  have hdiag : ∀ a, T a a a a = t1 := fun a => by
    have := hperm (Equiv.swap 0 a) 0 0 0 0
    rwa [Equiv.swap_apply_left, ← ht1] at this
  have hpair : ∀ a c, a ≠ c → T a a c c = t2 := fun a c hac => by
    obtain ⟨σ, h0, h1⟩ := exists_perm_zero_one hac
    have := hperm σ 0 0 1 1
    rwa [h0, h1, ← ht2] at this
  have hpair2 : ∀ a b, a ≠ b → T a b a b = t2 := fun a b hab => by
    rw [hs2, hpair a b hab]
  have hpair3 : ∀ a b, a ≠ b → T a b b a = t2 := fun a b hab => by
    rw [hs3, hpair2 a b hab]
  have hz1 : ∀ a b c e, a ≠ b → a ≠ c → a ≠ e → T a b c e = 0 := fun a b c e h1 h2 h3 =>
    symInvariant_eq_zero_of_single h h1 h2 h3
  have hz2 : ∀ a b c e, b ≠ a → b ≠ c → b ≠ e → T a b c e = 0 := fun a b c e h1 h2 h3 => by
    rw [hs1]; exact hz1 b a c e h1 h2 h3
  have hz3 : ∀ a b c e, c ≠ a → c ≠ b → c ≠ e → T a b c e = 0 := fun a b c e h1 h2 h3 => by
    rw [hs2]; exact hz2 a c b e h1 h2 h3
  have hz4 : ∀ a b c e, e ≠ a → e ≠ b → e ≠ c → T a b c e = 0 := fun a b c e h1 h2 h3 => by
    rw [hs3]; exact hz3 a b e c h1 h2 h3
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases e <;>
    simp [hdiag, hpair, hpair2, hpair3, hz1, hz2, hz3, hz4]

/-- **THE SPANNING PAIR IS INVARIANT**: `x · D + y · P` is a fully symmetric `O_h`-invariant
tensor for every `x, y`. -/
theorem symInvariantQuartic_span (x y : ℝ) :
    SymInvariantQuartic (fun a b c e =>
      x * (if a = b ∧ b = c ∧ c = e then (1 : ℝ) else 0)
        + y * ((if a = b then (1 : ℝ) else 0) * (if c = e then 1 else 0)
          + (if a = c then 1 else 0) * (if b = e then 1 else 0)
          + (if a = e then 1 else 0) * (if b = c then 1 else 0))) := by
  refine ⟨⟨?_, ?_, ?_⟩, ?_, ?_⟩
  · intro a b c e
    by_cases hab : a = b
    · subst hab; rfl
    · simp only [hab, Ne.symm hab, false_and, if_false, mul_zero, zero_mul, zero_add]
      ring
  · intro a b c e
    by_cases hbc : b = c
    · subst hbc; rfl
    · simp only [hbc, Ne.symm hbc, false_and, and_false, if_false, mul_zero, add_zero]
      ring
  · intro a b c e
    by_cases hce : c = e
    · subst hce; rfl
    · simp only [hce, Ne.symm hce, and_false, if_false, mul_zero, zero_add]
      ring
  · intro ε hε a b c e
    have hsq : ∀ i, ε i * ε i = 1 := fun i => by
      rcases hε i with h | h <;> rw [h] <;> norm_num
    have key1 : ε a * ε b * ε c * ε e * (if a = b ∧ b = c ∧ c = e then (1 : ℝ) else 0)
        = if a = b ∧ b = c ∧ c = e then 1 else 0 := by
      split_ifs with h
      · obtain ⟨rfl, rfl, rfl⟩ := h
        calc ε a * ε a * ε a * ε a * 1 = (ε a * ε a) * (ε a * ε a) := by ring
          _ = 1 := by rw [hsq]; ring
      · ring
    have key2 : ∀ a b c e : Fin 3, ε a * ε b * ε c * ε e
        * ((if a = b then (1 : ℝ) else 0) * (if c = e then 1 else 0))
        = (if a = b then 1 else 0) * (if c = e then 1 else 0) := by
      intro a b c e
      by_cases hab : a = b
      · subst hab
        by_cases hce : c = e
        · subst hce
          simp only [if_true]
          calc ε a * ε a * ε c * ε c * (1 * 1) = (ε a * ε a) * (ε c * ε c) := by ring
            _ = 1 * 1 := by rw [hsq, hsq]
        · simp [hce]
      · simp [hab]
    have k2 := key2 a b c e
    have k3 := key2 a c b e
    have k4 := key2 a e b c
    rw [show ε a * ε c * ε b * ε e = ε a * ε b * ε c * ε e by ring] at k3
    rw [show ε a * ε e * ε b * ε c = ε a * ε b * ε c * ε e by ring] at k4
    calc ε a * ε b * ε c * ε e * (x * (if a = b ∧ b = c ∧ c = e then (1 : ℝ) else 0)
          + y * ((if a = b then (1 : ℝ) else 0) * (if c = e then 1 else 0)
            + (if a = c then 1 else 0) * (if b = e then 1 else 0)
            + (if a = e then 1 else 0) * (if b = c then 1 else 0)))
        = x * (ε a * ε b * ε c * ε e * (if a = b ∧ b = c ∧ c = e then (1 : ℝ) else 0))
          + y * (ε a * ε b * ε c * ε e * ((if a = b then (1 : ℝ) else 0) * (if c = e then 1 else 0))
            + ε a * ε b * ε c * ε e * ((if a = c then (1 : ℝ) else 0) * (if b = e then 1 else 0))
            + ε a * ε b * ε c * ε e * ((if a = e then (1 : ℝ) else 0) * (if b = c then 1 else 0)))
          := by ring
      _ = _ := by rw [key1, k2, k3, k4]
  · intro σ a b c e
    simp only [Equiv.apply_eq_iff_eq]

/-- **`H2a` — THE FULLY SYMMETRIC `O_h`-INVARIANT RANK-4 TENSORS ARE EXACTLY `x · D + y · P`, WITH
`(x, y)` UNIQUE.** `D` is the tensor of `Σ_i k_i⁴` and `P` three times the tensor of
`(Σ_i k_i²)²`; the space is two-dimensional, coordinatized by this spanning pair. **The count is
the fully symmetric one, 2**; general (non-symmetric) rank-4 invariant counts are other objects and
are not this round's. -/
theorem symInvariantQuartic_iff (T : Fin 3 → Fin 3 → Fin 3 → Fin 3 → ℝ) :
    SymInvariantQuartic T ↔ ∃! xy : ℝ × ℝ, T = fun a b c e =>
      xy.1 * (if a = b ∧ b = c ∧ c = e then (1 : ℝ) else 0)
        + xy.2 * ((if a = b then (1 : ℝ) else 0) * (if c = e then 1 else 0)
          + (if a = c then 1 else 0) * (if b = e then 1 else 0)
          + (if a = e then 1 else 0) * (if b = c then 1 else 0)) := by
  constructor
  · intro h
    refine ⟨(T 0 0 0 0 - 3 * T 0 0 1 1, T 0 0 1 1), ?_, ?_⟩
    · funext a b c e
      rw [symInvariant_closed_form h a b c e]
      fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases e <;> simp <;> ring
    · rintro ⟨x, y⟩ hxy
      have h0 := congrFun (congrFun (congrFun (congrFun hxy 0) 0) 0) 0
      have h1 := congrFun (congrFun (congrFun (congrFun hxy 0) 0) 1) 1
      simp at h0 h1
      ext <;> simp <;> linarith
  · rintro ⟨⟨x, y⟩, rfl, -⟩
    exact symInvariantQuartic_span x y

/-- **`H2a`, THE "1" SIDE — THE ROTATION-INVARIANT ONES ARE EXACTLY THE MULTIPLES OF `P`.** For
the spanning family, the quartic form is a function of `|k|²` iff `x = 0`; the rotation-invariant
fully symmetric rank-4 tensors on `ℝ³` form a one-dimensional space. Consumes
`quartic_not_isotropic`. -/
theorem symInvariant_isotropic_iff (x y : ℝ) :
    IsotropicQuartic (fun a b c e =>
      x * (if a = b ∧ b = c ∧ c = e then (1 : ℝ) else 0)
        + y * ((if a = b then (1 : ℝ) else 0) * (if c = e then 1 else 0)
          + (if a = c then 1 else 0) * (if b = e then 1 else 0)
          + (if a = e then 1 else 0) * (if b = c then 1 else 0))) ↔ x = 0 := by
  constructor
  · intro hiso
    obtain ⟨k, k', h2, h4⟩ := quartic_not_isotropic
    have := hiso k k' h2
    beta_reduce at this
    rw [quartic_form_span, quartic_form_span, h2] at this
    have hx : x * (∑ i, k i ^ 4 - ∑ i, k' i ^ 4) = 0 := by linear_combination this
    rcases mul_eq_zero.mp hx with hx | hx
    · exact hx
    · exact absurd (sub_eq_zero.mp hx) h4
  · rintro rfl k k' h2
    beta_reduce
    rw [quartic_form_span, quartic_form_span, h2]
    ring

/-- **THE STENCIL, IN THE INTEGERS**: `dir d L p` is the `ZMod L`-cast of the integer axis vector
`±e_{p.1}`. This is what ties the real fourth moment below to the kernel's own stencil. -/
theorem dir_eq_intCast (d L : ℕ) (p : Fin d × Bool) :
    dir d L p = fun k =>
      (((if p.2 then (Pi.single p.1 (1 : ℤ) : Fin d → ℤ) else -Pi.single p.1 1) k : ℤ) : ZMod L) := by
  rcases p with ⟨k, s⟩
  funext j
  cases s <;> simp only [dir, Bool.false_eq_true, if_false, if_true, Pi.neg_apply, Pi.single_apply,
    Int.cast_neg, Int.cast_ite, Int.cast_one, Int.cast_zero]

/-- **THE FOURTH MOMENT OF THE AXIS STENCIL** (budget slot 4) —
`T_{abce} = Σ_{p} (dir p)_a (dir p)_b (dir p)_c (dir p)_e` over the `2d` axis directions `±e_k`,
taken in the real embedding of the integer stencil that `dir_eq_intCast` identifies with the
kernel's `dir`. -/
def axisMoment4 (d : ℕ) (a b c e : Fin d) : ℝ :=
  ∑ p : Fin d × Bool,
    (((if p.2 then (Pi.single p.1 (1 : ℤ) : Fin d → ℤ) else -Pi.single p.1 1) a : ℤ) : ℝ)
      * (((if p.2 then (Pi.single p.1 (1 : ℤ) : Fin d → ℤ) else -Pi.single p.1 1) b : ℤ) : ℝ)
      * (((if p.2 then (Pi.single p.1 (1 : ℤ) : Fin d → ℤ) else -Pi.single p.1 1) c : ℤ) : ℝ)
      * (((if p.2 then (Pi.single p.1 (1 : ℤ) : Fin d → ℤ) else -Pi.single p.1 1) e : ℤ) : ℝ)

/-- **`H2b` — THE AXIS-STENCIL FOURTH MOMENT IS `2 · [a = b = c = e]`**: nonzero only on the
diagonal. -/
theorem axisMoment4_eq (d : ℕ) (a b c e : Fin d) :
    axisMoment4 d a b c e = if a = b ∧ b = c ∧ c = e then 2 else 0 := by
  unfold axisMoment4
  have hterm : ∀ (k : Fin d) (s : Bool),
      (((if s then (Pi.single k (1 : ℤ) : Fin d → ℤ) else -Pi.single k 1) a : ℤ) : ℝ)
        * (((if s then (Pi.single k (1 : ℤ) : Fin d → ℤ) else -Pi.single k 1) b : ℤ) : ℝ)
        * (((if s then (Pi.single k (1 : ℤ) : Fin d → ℤ) else -Pi.single k 1) c : ℤ) : ℝ)
        * (((if s then (Pi.single k (1 : ℤ) : Fin d → ℤ) else -Pi.single k 1) e : ℤ) : ℝ)
        = if a = k ∧ b = k ∧ c = k ∧ e = k then 1 else 0 := by
    intro k s
    by_cases hak : a = k <;> by_cases hbk : b = k <;> by_cases hck : c = k <;>
      by_cases hek : e = k <;> cases s <;> simp [hak, hbk, hck, hek]
  rw [Fintype.sum_prod_type]
  simp only [Fintype.sum_bool, hterm]
  rw [Finset.sum_eq_single a]
  · by_cases h : a = b ∧ b = c ∧ c = e
    · obtain ⟨rfl, rfl, rfl⟩ := h
      simp
      norm_num
    · have h' : ¬ (a = a ∧ b = a ∧ c = a ∧ e = a) := by
        rintro ⟨-, hb, hc, he⟩
        exact h ⟨hb.symm, hb.trans hc.symm, hc.trans he.symm⟩
      rw [if_neg h, if_neg h']
      ring
  · intro k _ hk
    simp [Ne.symm hk]
  · intro h
    exact absurd (Finset.mem_univ _) h

/-- **`H2b` — THE QUARTIC FORM OF THE AXIS-STENCIL MOMENT IS `2 Σ_i k_i⁴`.** -/
theorem axisMoment4_quartic (d : ℕ) (k : Fin d → ℝ) :
    (∑ a, ∑ b, ∑ c, ∑ e, axisMoment4 d a b c e * (k a * k b * k c * k e)) = 2 * ∑ i, k i ^ 4 := by
  simp only [axisMoment4_eq]
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Finset.sum_eq_single a]
  · rw [Finset.sum_eq_single a]
    · rw [Finset.sum_eq_single a]
      · simp
        ring
      · intro e _ he
        simp [Ne.symm he]
      · intro h
        exact absurd (Finset.mem_univ _) h
    · intro c _ hc
      exact Finset.sum_eq_zero fun e _ => by simp [Ne.symm hc]
    · intro h
      exact absurd (Finset.mem_univ _) h
  · intro b _ hb
    exact Finset.sum_eq_zero fun c _ => Finset.sum_eq_zero fun e _ => by simp [Ne.symm hb]
  · intro h
    exact absurd (Finset.mem_univ _) h

/-- The `d = 3` axis-stencil moment is `2 · D + 0 · P` in the spanning pair of `H2a`. -/
theorem axisMoment4_three_eq :
    axisMoment4 3 = fun a b c e =>
      (2 : ℝ) * (if a = b ∧ b = c ∧ c = e then (1 : ℝ) else 0)
        + 0 * ((if a = b then (1 : ℝ) else 0) * (if c = e then 1 else 0)
          + (if a = c then 1 else 0) * (if b = e then 1 else 0)
          + (if a = e then 1 else 0) * (if b = c then 1 else 0)) := by
  funext a b c e
  rw [axisMoment4_eq]
  by_cases h : a = b ∧ b = c ∧ c = e <;> simp [h]

/-- **`H2b` — THE AXIS-STENCIL MOMENT IS `O_h`-INVARIANT** (fully symmetric, sign-invariant,
coordinate-permutation-invariant). Quadratic order is isotropic by Corollary 1a; this is the
quartic order. -/
theorem axisMoment4_symInvariant : SymInvariantQuartic (axisMoment4 3) := by
  rw [axisMoment4_three_eq]
  exact symInvariantQuartic_span 2 0

/-- **`H2b` — THE AXIS-STENCIL MOMENT IS NOT ROTATION-INVARIANT**, in the freeze's form: two
vectors of the same length on which its quartic form differs, consuming `quartic_not_isotropic`.
**This is a proved fact about the stencil; it is a conditional finding about hydrodynamics** —
HI only if H5's stress closure consumes this tensor, otherwise `H2` remains HO. -/
theorem axisMoment4_form_not_isotropic :
    ∃ k k' : Fin 3 → ℝ, (∑ i, k i ^ 2) = (∑ i, k' i ^ 2)
      ∧ (∑ a, ∑ b, ∑ c, ∑ e, axisMoment4 3 a b c e * (k a * k b * k c * k e))
        ≠ ∑ a, ∑ b, ∑ c, ∑ e, axisMoment4 3 a b c e * (k' a * k' b * k' c * k' e) := by
  obtain ⟨k, k', h2, h4⟩ := quartic_not_isotropic
  refine ⟨k, k', h2, ?_⟩
  rw [axisMoment4_quartic, axisMoment4_quartic]
  intro hc
  exact h4 (mul_left_cancel₀ two_ne_zero hc)

/-- **`H2b`, IN THE PREDICATE OF `H2a`**: the axis-stencil moment fails `IsotropicQuartic`. -/
theorem axisMoment4_not_isotropic : ¬ IsotropicQuartic (axisMoment4 3) := by
  rw [axisMoment4_three_eq]
  intro h
  have := (symInvariant_isotropic_iff 2 0).mp h
  norm_num at this

end Quartic

/-! ### Section D — `H3a`: a block-observable diagnostic for closure -/

section Block

variable (d L q b : ℕ) [NeZero L]

/-- **THE BLOCK SUM** (budget slot 2) — for the partition of the torus into cubes of side `b`,
the block `β(i)_k = ⌊i_k / b⌋` of a site and the block sums `B_β(x) = Σ_{i ∈ β} x(i) ∈ ZMod q`, as
an additive coarse map onto `Fin d → ZMod (L / b)`. The partition into cubes of side `b` is the
case `b ∣ L`; the definition is stated for every `b`. -/
def blockSum : ((Fin d → ZMod L) → ZMod q) →+ ((Fin d → ZMod (L / b)) → ZMod q) where
  toFun x β := ∑ i, if (fun k => (((i k).val / b : ℕ) : ZMod (L / b))) = β then x i else 0
  map_zero' := by
    funext β
    simp
  map_add' x y := by
    funext β
    show (∑ i, if (fun k => (((i k).val / b : ℕ) : ZMod (L / b))) = β then x i + y i else 0)
      = (∑ i, if (fun k => (((i k).val / b : ℕ) : ZMod (L / b))) = β then x i else 0)
        + ∑ i, if (fun k => (((i k).val / b : ℕ) : ZMod (L / b))) = β then y i else 0
    rw [← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    split_ifs <;> simp

theorem blockSum_apply (x : (Fin d → ZMod L) → ZMod q) (β : Fin d → ZMod (L / b)) :
    blockSum d L q b x β
      = ∑ i, if (fun k => (((i k).val / b : ℕ) : ZMod (L / b))) = β then x i else 0 := rfl

end Block

section OneDim

/-- A sum over `Fin 1 → M` is a sum over `M`. -/
theorem sum_fin_one_fun {M N : Type} [Fintype M] [AddCommMonoid N] (g : (Fin 1 → M) → N) :
    ∑ i, g i = ∑ j : M, g (fun _ => j) :=
  Fintype.sum_equiv (Equiv.funUnique (Fin 1) M) g (fun j => g (fun _ => j)) fun i => by
    congr 1
    funext k
    rw [Subsingleton.elim k default]
    rfl

/-- The one-dimensional wave rule at a site: `α` times the two neighbours. -/
theorem waveF_one_dim (L q : ℕ) (α : ZMod q) (c : (Fin 1 → ZMod L) → ZMod q) (j : ZMod L) :
    waveF 1 L q α c (fun _ => j) = α * (c (fun _ => j + 1) + c (fun _ => j - 1)) := by
  unfold waveF
  rw [Fintype.sum_prod_type, Fin.sum_univ_one, Fintype.sum_bool]
  have h1 : ((fun _ : Fin 1 => j) + dir 1 L (0, true)) = fun _ => j + 1 := by
    funext k
    simp [dir, Fin.eq_zero k]
  have h2 : ((fun _ : Fin 1 => j) + dir 1 L (0, false)) = fun _ => j - 1 := by
    funext k
    simp [dir, Fin.eq_zero k, sub_eq_add_neg]
  rw [h1, h2]

/-- The one-dimensional block sum as a sum over `ZMod L`. -/
theorem blockSum_one_dim (L q b : ℕ) [NeZero L] (x : (Fin 1 → ZMod L) → ZMod q)
    (β0 : ZMod (L / b)) :
    blockSum 1 L q b x (fun _ => β0)
      = ∑ j : ZMod L, if ((j.val / b : ℕ) : ZMod (L / b)) = β0 then x (fun _ => j) else 0 := by
  rw [blockSum_apply, sum_fin_one_fun]
  refine Finset.sum_congr rfl fun j _ => ?_
  simp only [funext_iff, Fin.forall_fin_one]

theorem sum_zmod_six {N : Type} [AddCommMonoid N] (f : ZMod 6 → N) :
    ∑ j, f j = f 0 + f 1 + f 2 + f 3 + f 4 + f 5 :=
  Fin.sum_univ_six f

theorem sum_zmod_four {N : Type} [AddCommMonoid N] (f : ZMod 4 → N) :
    ∑ j, f j = f 0 + f 1 + f 2 + f 3 :=
  Fin.sum_univ_four f

/-- **`H3a` — THE BLOCK STATE DOES NOT CLOSE**, at `d = 1`, `L = 6`, `b = 3`, `α = 1`, for
**every** `q ≥ 2`, the witness pinned by equations in the statement: both pairs have
`x_{t−1} = 0`; one has `x_t = 0`, the other `x_t = y = (−1, 1, 0, 0, 0, 0)`. Both block states are
`(0, 0)` at `t` and at `t − 1`. At `t + 1` the zero trajectory stays zero, while on block
`{0, 1, 2}` the block sum of `F(y)` is `(y₅ + y₁) + (y₀ + y₂) + (y₁ + y₃) = 1 ≠ 0`. -/
theorem h3a_block_state_not_closed (q : ℕ) (hq : 2 ≤ q) :
    ∃ x y : (Fin 1 → ZMod 6) → ZMod q × ZMod q,
      prevOf x = 0 ∧ prevOf y = 0 ∧ curOf x = 0
      ∧ curOf y = (fun i => if i 0 = 0 then -1 else if i 0 = 1 then 1 else 0)
      ∧ blockSum 1 6 q 3 (curOf x) = blockSum 1 6 q 3 (curOf y)
      ∧ blockSum 1 6 q 3 (prevOf x) = blockSum 1 6 q 3 (prevOf y)
      ∧ blockSum 1 6 q 3 (curOf x) = 0 ∧ blockSum 1 6 q 3 (prevOf x) = 0
      ∧ blockSum 1 6 q 3 (curOf (leap (waveF 1 6 q 1) x)) = 0
      ∧ blockSum 1 6 q 3 (curOf (leap (waveF 1 6 q 1) y)) (fun _ => 0) = 1
      ∧ blockSum 1 6 q 3 (curOf (leap (waveF 1 6 q 1) x))
          ≠ blockSum 1 6 q 3 (curOf (leap (waveF 1 6 q 1) y)) := by
  have : Fact (1 < q) := ⟨hq⟩
  have hF0 : waveF 1 6 q 1 0 = 0 := map_zero_of_additive (waveSubstratum_A5 1 6 q 1)
  refine ⟨fun _ => (0, 0), fun i => (0, if i 0 = 0 then -1 else if i 0 = 1 then 1 else 0),
    rfl, rfl, rfl, rfl, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · -- the block state of `y` at time `t` is zero
    have hc : curOf (fun _ : Fin 1 → ZMod 6 => ((0 : ZMod q), (0 : ZMod q))) = 0 := rfl
    rw [hc, map_zero]
    funext β
    have hβ : β = fun _ => β 0 := funext fun k => by rw [Fin.eq_zero k]
    rw [hβ]
    show (0 : ZMod q) = blockSum 1 6 q 3 (fun i => if i 0 = 0 then -1 else if i 0 = 1 then 1 else 0) _
    rw [blockSum_one_dim, sum_zmod_six]
    rcases (show ∀ z : ZMod (6 / 3), z = 0 ∨ z = 1 by decide) (β 0) with h | h <;> rw [h] <;>
      simp +decide
  · rfl
  · have hc : curOf (fun _ : Fin 1 → ZMod 6 => ((0 : ZMod q), (0 : ZMod q))) = 0 := rfl
    rw [hc, map_zero]
  · have hp : prevOf (fun _ : Fin 1 → ZMod 6 => ((0 : ZMod q), (0 : ZMod q))) = 0 := rfl
    rw [hp, map_zero]
  · have hc : curOf (fun _ : Fin 1 → ZMod 6 => ((0 : ZMod q), (0 : ZMod q))) = 0 := rfl
    have hp : prevOf (fun _ : Fin 1 → ZMod 6 => ((0 : ZMod q), (0 : ZMod q))) = 0 := rfl
    rw [curOf_leap, hc, hp, hF0, sub_zero, map_zero]
  · have hp : prevOf (fun i : Fin 1 → ZMod 6 =>
        ((0 : ZMod q), if i 0 = 0 then (-1 : ZMod q) else if i 0 = 1 then 1 else 0)) = 0 := rfl
    have hc : curOf (fun i : Fin 1 → ZMod 6 =>
        ((0 : ZMod q), if i 0 = 0 then (-1 : ZMod q) else if i 0 = 1 then 1 else 0))
        = fun i => if i 0 = 0 then (-1 : ZMod q) else if i 0 = 1 then 1 else 0 := rfl
    rw [curOf_leap, hp, hc, sub_zero, blockSum_one_dim, sum_zmod_six]
    simp only [waveF_one_dim]
    simp +decide
  · intro hcon
    have hc : curOf (fun _ : Fin 1 → ZMod 6 => ((0 : ZMod q), (0 : ZMod q))) = 0 := rfl
    have hp : prevOf (fun _ : Fin 1 → ZMod 6 => ((0 : ZMod q), (0 : ZMod q))) = 0 := rfl
    have hp' : prevOf (fun i : Fin 1 → ZMod 6 =>
        ((0 : ZMod q), if i 0 = 0 then (-1 : ZMod q) else if i 0 = 1 then 1 else 0)) = 0 := rfl
    have hc' : curOf (fun i : Fin 1 → ZMod 6 =>
        ((0 : ZMod q), if i 0 = 0 then (-1 : ZMod q) else if i 0 = 1 then 1 else 0))
        = fun i => if i 0 = 0 then (-1 : ZMod q) else if i 0 = 1 then 1 else 0 := rfl
    have h0 := congrFun hcon (fun _ => 0)
    rw [curOf_leap, hc, hp, hF0, sub_zero, map_zero, curOf_leap, hp', hc', sub_zero,
      blockSum_one_dim, sum_zmod_six] at h0
    simp only [waveF_one_dim] at h0
    simp +decide at h0

/-- **`H3a` — NO COARSE RULE CLOSES ON THE BLOCK VARIABLE** at `d = 1`, `L = 6`, `b = 3`,
`α = 1`, for every `q ≥ 2`. **Status for `H3`: HO** — this block variable needs more than its own
two-time state to predict its next value; nothing is said about a statistical closure at another
scale or in another variable, and no timescale is asserted. -/
theorem h3a_no_closure (q : ℕ) (hq : 2 ≤ q) :
    ¬ ∃ Φ : ((Fin 1 → ZMod (6 / 3)) → ZMod q) × ((Fin 1 → ZMod (6 / 3)) → ZMod q)
        → ((Fin 1 → ZMod (6 / 3)) → ZMod q),
      CoarseCloses (blockSum 1 6 q 3) (waveF 1 6 q 1) Φ := by
  rintro ⟨Φ, hΦ⟩
  obtain ⟨x, y, -, -, -, -, hbc, hbp, -, -, -, -, hne⟩ := h3a_block_state_not_closed q hq
  apply hne
  rw [hΦ x, hΦ y, hbc, hbp]

/-- **THE CLOSING CONTROL `d = 1`, `L = 4`, `b = 2` IS NOT A WITNESS**: there the block sum of `F`
over `{0, 1}` is `α · ((x₃ + x₁) + (x₀ + x₂))`, `α` times the total sum, which the two block sums
determine, so this block variable closes — for every `q` and every `α`. -/
theorem h3a_control_L4_closes (q : ℕ) (α : ZMod q) :
    CoarseCloses (blockSum 1 4 q 2) (waveF 1 4 q α)
      (fun uv β => α * (uv.1 (fun _ => 0) + uv.1 (fun _ => 1)) - uv.2 β) := by
  intro x
  funext β
  have hβ : β = fun _ => β 0 := funext fun k => by rw [Fin.eq_zero k]
  rw [curOf_leap, map_sub, Pi.sub_apply, hβ]
  simp only []
  rw [blockSum_one_dim, blockSum_one_dim, blockSum_one_dim, blockSum_one_dim, sum_zmod_four,
    sum_zmod_four, sum_zmod_four, sum_zmod_four]
  simp only [waveF_one_dim]
  have e1 : (0 : ZMod 4) + 1 = 1 := by decide
  have e2 : (0 : ZMod 4) - 1 = 3 := by decide
  have e3 : (1 : ZMod 4) + 1 = 2 := by decide
  have e4 : (1 : ZMod 4) - 1 = 0 := by decide
  have e5 : (2 : ZMod 4) + 1 = 3 := by decide
  have e6 : (2 : ZMod 4) - 1 = 1 := by decide
  have e7 : (3 : ZMod 4) + 1 = 0 := by decide
  have e8 : (3 : ZMod 4) - 1 = 2 := by decide
  simp only [e1, e2, e3, e4, e5, e6, e7, e8]
  rcases (show ∀ z : ZMod (4 / 2), z = 0 ∨ z = 1 by decide) (β 0) with h | h <;> rw [h] <;>
    simp +decide <;> ring

end OneDim

end HydroSourceAudit
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.HydroSourceAudit.curOf_add
#print axioms OIBridge.HydroSourceAudit.prevOf_add
#print axioms OIBridge.HydroSourceAudit.curOf_leap
#print axioms OIBridge.HydroSourceAudit.map_zero_of_additive
#print axioms OIBridge.HydroSourceAudit.coarse_evolution_additive
#print axioms OIBridge.HydroSourceAudit.coarseCloses_additive_on_range
#print axioms OIBridge.HydroSourceAudit.coarseCloses_nsmul
#print axioms OIBridge.HydroSourceAudit.waveSubstratum_F
#print axioms OIBridge.HydroSourceAudit.wave_coarse_evolution_additive
#print axioms OIBridge.HydroSourceAudit.wave_coarseCloses_additive_on_range
#print axioms OIBridge.HydroSourceAudit.totalSum_apply
#print axioms OIBridge.HydroSourceAudit.totalSum_waveF
#print axioms OIBridge.HydroSourceAudit.totalSum_leap
#print axioms OIBridge.HydroSourceAudit.totalSum_second_difference
#print axioms OIBridge.HydroSourceAudit.totalSum_single
#print axioms OIBridge.HydroSourceAudit.deltaS_conserved_iff
#print axioms OIBridge.HydroSourceAudit.combination_conserved_iff
#print axioms OIBridge.HydroSourceAudit.deltaS_conserved_iff_dvd_four
#print axioms OIBridge.HydroSourceAudit.deltaS_conserved_iff_two_or_four
#print axioms OIBridge.HydroSourceAudit.quartic_form_diag
#print axioms OIBridge.HydroSourceAudit.quartic_form_pair
#print axioms OIBridge.HydroSourceAudit.quartic_form_span
#print axioms OIBridge.HydroSourceAudit.symInvariant_eq_zero_of_single
#print axioms OIBridge.HydroSourceAudit.exists_perm_zero_one
#print axioms OIBridge.HydroSourceAudit.symInvariant_closed_form
#print axioms OIBridge.HydroSourceAudit.symInvariantQuartic_span
#print axioms OIBridge.HydroSourceAudit.symInvariantQuartic_iff
#print axioms OIBridge.HydroSourceAudit.symInvariant_isotropic_iff
#print axioms OIBridge.HydroSourceAudit.dir_eq_intCast
#print axioms OIBridge.HydroSourceAudit.axisMoment4_eq
#print axioms OIBridge.HydroSourceAudit.axisMoment4_quartic
#print axioms OIBridge.HydroSourceAudit.axisMoment4_three_eq
#print axioms OIBridge.HydroSourceAudit.axisMoment4_symInvariant
#print axioms OIBridge.HydroSourceAudit.axisMoment4_form_not_isotropic
#print axioms OIBridge.HydroSourceAudit.axisMoment4_not_isotropic
#print axioms OIBridge.HydroSourceAudit.blockSum_apply
#print axioms OIBridge.HydroSourceAudit.sum_fin_one_fun
#print axioms OIBridge.HydroSourceAudit.waveF_one_dim
#print axioms OIBridge.HydroSourceAudit.blockSum_one_dim
#print axioms OIBridge.HydroSourceAudit.sum_zmod_six
#print axioms OIBridge.HydroSourceAudit.sum_zmod_four
#print axioms OIBridge.HydroSourceAudit.h3a_block_state_not_closed
#print axioms OIBridge.HydroSourceAudit.h3a_no_closure
#print axioms OIBridge.HydroSourceAudit.h3a_control_L4_closes
