import OIBridge.SubstratumInterfaceAudit

/-!
# A6 background independence, round 1 — the readings defined, and closed on the least interface

Executed under the frozen control plane
`verification/programmes/substratum/a6-background-independence/preregistration.md`, blob
`afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3`, from `main` at
`8792801beeeccbf0673db137cae83e6663d21fba` — the merge commit of that control plane (PR #593),
which the freeze fixes as this round's mandated base.

## What this round is

A **definition round**, not a proof round. The `ROADMAP` carries A6 as a `GAP`: the manuscripts
state the condition and `Substratum` has no predicate for it, and the audits that found the gap
found that the manuscript wording admits an invariant reading and a covariant reading which must
not be silently identified. This module freezes what A6 could mean formally — four readings on
three interfaces — and tests them on frozen carriers. **It does not try to prove A6 for anything
physical, and it adopts no reading.** `A6-inv`, `A6-cov`, `A6-glob` and `A6-sd` are four objects on
three interfaces; any sentence using "A6" without a suffix, other than in a quotation or in
"the `ROADMAP` row A6", is a defect.

## The readings, as frozen

Throughout, `ι` is the site type, `V` the alphabet — an additive group — and
`F : (ι → V) → (ι → V)` an update map, the `F` field of a `Rule ι V`. The internal index enters
**only through the alphabet**: the manuscripts' `K`-component site variable in `(ℤ/qℤ)^K` is the
alphabet `V := K → ZMod q`, and `Substratum` already admits it. **No field is added to
`Substratum`.** Site-dependent internal-index transformations are `g : ι → AddAut V`; over the
finite alphabet there is no unitary group and none is introduced.

* **`A6-inv`** (`A6Inv F M`) — invariance of a **fixed** rule under site-dependent transformations
  preserving the site coupling `M : V →+ V` pointwise. The literal first sentence of
  `Substratum.md:102`.
* **`A6-cov`** (`A6Cov N M`) — covariance: the link coupling `M : ι → ι → (V →+ V)` is transported,
  `gaugeLink g M i j = g i ∘ M i j ∘ (g j)⁻¹`, so nothing needs preserving. **Not a predicate of a
  `Substratum`**; a predicate of a neighbourhood function and a link coupling. That `A6-inv` and
  `A6-cov` live on different interfaces is the first reason they must not be identified.
* **`A6-glob`** (`A6Glob F M`) — the global commutant symmetry, the constant-`g` case of `A6-inv`.
* **`A6-sd`** — the state-dependent graph of `SM.md:100`, a structural property of a rule family
  and not an invariance under any group. **No predicate is defined for `A6-sd` in this round**; it
  is frozen as a reading so that it cannot be identified with `A6-cov`.

## The targets reached here

* **`D2-i`, `D2-ii`** — on `waveSubstratum` (`K` a singleton) `A6-inv` is statable but
  **degenerate**: it fails at `d = 1`, `L = 3`, `q = 3`, `α = 1` on the frozen witness
  (`d2i_wave_witness`, `d2i_wave_not_a6inv`), and `A6-glob` holds for every `d L q α`
  (`d2ii_wave_a6glob`). **These are facts about the degenerate form and are labelled so**: the
  degenerate statement is not the manuscripts' A6 (the singleton-`K` rescalings are the A5
  amplitude-scale freedom), and the wave substratum's A6 status at manuscript level stays a gap.
* **`D3-a`** — `A6-cov` is an identity on link-coupled rules (`a6cov_all`): it restricts no
  link-coupled rule; its content is the interface, not a constraint. This is a statement about the
  frozen `A6Cov` over a finite alphabet, **not** "local gauge invariance is trivial" and not a
  statement about `SM.md:114`'s derivation on the complex lift, which is outside the interface.
* **`D3-b`** — a link-coupled rule failing `A6-inv` on the frozen two-site carrier
  (`d3b_witness`, `d3b_not_a6inv`). **The distinction is one-directional**: on link-coupled rules
  `A6-cov` always holds and `A6-inv` sometimes fails, so no rule satisfies `A6-inv` and fails
  `A6-cov`.
* **`D4-a`, `D4-b`** — single-edge rigidity of `A6-inv` on the constant-coupling rule
  (`d4a_single_edge`, `d4b_edge_rigidity`, `d4b_not_a6inv_of_nonconstant`) and its symmetric-point
  consequence (`d4b_symmetric_point`, `d4b_mu_id`): at `M₀ = μ • id` with `μ` a unit, `A6-inv`
  fails whenever `AddAut V` has two elements and `N` has an edge between distinct sites, while
  `A6-glob` holds there (`a6glob_constLink`). **Single-edge, no connectivity**: the connected
  corollary is analysis, not a target, and no connectivity definition is spent.

## What none of this licenses

Nothing here says A6 holds of the physical substratum, or fails of it. Nothing here touches the
Standard-Model gauge-group derivation. No reading is "the" A6: after this round A6 has candidate
predicates and a determination of which coordinate asserts which, and no adopted predicate. Which
of `μ I_6` and the block-scalar equivariant object "the cubic-symmetric coupling matrix" denotes is
not decided: `M` is a parameter of every reading, so both are instances. `A6-sd` is not
formalized. No manuscript is edited.
-/

namespace OIBridge
namespace BackgroundIndependence

open SecondOrderLayer SubstratumInterfaceAudit
open OIBridge.SecondOrderCircuit (leapEquiv leap curOf leap_apply curOf_apply leapEquiv_apply)

variable {ι V : Type} [AddCommGroup V]

/-! ### Section A — the least interface: the seven budget slots that fire -/

/-- **THE POINTWISE ACTION** (slot 1) of a site-dependent internal-index transformation
`g : ι → AddAut V` on configurations: `(g · c) i = g i (c i)`. Because each `g i` is additive, the
action commutes with the second-order leap `(p, c) ↦ (c, F c − p)` exactly when it commutes with
`F` (`leap_siteAct`), so every reading is stated on `F` and its phase-space form is a corollary,
not a separate reading. -/
def siteAct (g : ι → AddAut V) (c : ι → V) : ι → V := fun i => g i (c i)

/-- **POINTWISE PRESERVATION** (slot 2): `g` preserves the site coupling `M` pointwise when each
`g i` lies in the commutant of `M`. -/
def PreservesPointwise (g : ι → AddAut V) (M : V →+ V) : Prop :=
  ∀ i v, g i (M v) = M (g i v)

/-- **`A6-inv`** (slot 3) — invariance of a fixed rule under site-dependent transformations
preserving `M`: the coupling is **fixed**, `F` does not change, `M` does not change, and the
transformation acts on the configuration alone. The literal first sentence of `Substratum.md:102`.
Stated on a bare `F` so that `D2` reads it on `(waveSubstratum d L q α).R.F` with no new
definition. -/
def A6Inv (F : (ι → V) → (ι → V)) (M : V →+ V) : Prop :=
  ∀ g : ι → AddAut V, PreservesPointwise g M → ∀ c, F (siteAct g c) = siteAct g (F c)

/-- **`A6-glob`** (slot 4) — the global commutant symmetry: the special case of `A6-inv` with `g`
constant (`a6glob_of_a6inv`). It is what the second sentence of `Substratum.md:102` names as what
A6 yields before promotion, and it is a reading in its own right because on the manuscripts' own
rule `A6-inv` is predicted to have no content beyond it (`D4`). -/
def A6Glob (F : (ι → V) → (ι → V)) (M : V →+ V) : Prop :=
  ∀ g : AddAut V, (∀ v, g (M v) = M (g v)) → ∀ c, F (fun i => g (c i)) = fun i => g (F c i)

/-- **THE LINK-COUPLED UPDATE MAP** (slot 5): `linkF N M c i = ∑_{j ∈ N i} M i j (c j)`, with the
link coupling `M : ι → ι → (V →+ V)` the manuscripts' link variable `M(n, ê_j)` of `SM.md:112`
indexed by an ordered pair of sites. The site coupling is the constant link coupling
`fun _ _ => M₀`. -/
def linkF (N : ι → Finset ι) (M : ι → ι → (V →+ V)) (c : ι → V) : ι → V :=
  fun i => ∑ j ∈ N i, M i j (c j)

/-- **THE TRANSPORTED LINK COUPLING** (slot 6): `gaugeLink g M i j = g i ∘ M i j ∘ (g j)⁻¹`, the
transformation law of `SM.md:112`. The inverse `(g j)⁻¹` is the inverse additive equivalence
`(g j).symm`, written so that no convention about the group structure on `AddAut V` is used. -/
def gaugeLink (g : ι → AddAut V) (M : ι → ι → (V →+ V)) : ι → ι → (V →+ V) :=
  fun i j => ((g i).toAddMonoidHom.comp (M i j)).comp (g j).symm.toAddMonoidHom

/-- **`A6-cov`** (slot 7) — covariance: the coupling transforms with the configuration. No
pointwise-preservation hypothesis, because the coupling is transported and nothing needs
preserving. **Not a predicate of a `Substratum`**: a predicate of a neighbourhood function and a
link coupling, which is the first reason it must not be identified with `A6-inv`. -/
def A6Cov (N : ι → Finset ι) (M : ι → ι → (V →+ V)) : Prop :=
  ∀ (g : ι → AddAut V) (c : ι → V),
    linkF N (gaugeLink g M) (siteAct g c) = siteAct g (linkF N M c)

/-! ### Section B — the relations among the readings -/

/-- **`A6-inv` ⟹ `A6-glob`**, by specialization to a constant `g`. Always. -/
theorem a6glob_of_a6inv {F : (ι → V) → (ι → V)} {M : V →+ V} (h : A6Inv F M) : A6Glob F M :=
  fun g hg c => h (fun _ => g) (fun _ v => hg v) c

/-- **THE PHASE-SPACE FORM IS A COROLLARY, NOT A READING**: if `g` commutes with `F` then the
pointwise action on both slots of `ι → V × V` commutes with the leap `leapEquiv F`. Recorded as a
theorem about `siteAct` and `leapEquiv`, never as a separate definition. -/
theorem leap_siteAct [DecidableEq ι] {F : (ι → V) → (ι → V)} {g : ι → AddAut V}
    (h : ∀ c, F (siteAct g c) = siteAct g (F c)) (x : ι → V × V) :
    leapEquiv F (fun i => (g i (x i).1, g i (x i).2))
      = fun i => (g i (leapEquiv F x i).1, g i (leapEquiv F x i).2) := by
  funext i
  have hc : curOf (fun i => (g i (x i).1, g i (x i).2)) = siteAct g (curOf x) := rfl
  simp only [leapEquiv_apply, leap_apply]
  rw [hc, h, map_sub]
  rfl

/-- **`D3-a` — `A6-cov` IS AN IDENTITY**: for every neighbourhood function and link coupling,
`linkF N (gaugeLink g M) (g · c) i = ∑_j g i (M i j ((g j)⁻¹ (g j (c j)))) = g i (∑_j M i j (c j))`.

**Bounded reading:** `A6-cov` restricts no link-coupled rule; its content is the interface, not a
constraint. This is a statement about the frozen `A6Cov` on link-coupled rules over a finite
alphabet, **not** "local gauge invariance is trivial" and not a statement about `SM.md:114`'s
derivation on the complex lift, which is outside the interface. -/
theorem a6cov_all (N : ι → Finset ι) (M : ι → ι → (V →+ V)) : A6Cov N M := by
  intro g c
  funext i
  simp only [linkF, siteAct, gaugeLink, AddMonoidHom.comp_apply, AddEquiv.coe_toAddMonoidHom,
    AddEquiv.symm_apply_apply, map_sum]

/-! ### Section C — `D3-b`: the frozen two-site carrier -/

/-- **`D3-b` — THE FROZEN CARRIER, WITH ITS EQUATIONS.** `ι = Fin 2` with `N 0 = {1}`, `N 1 = {0}`;
`V = Fin 2 → ZMod 2`; `M i j = id` (the constant site coupling `id`, which every `g` preserves
pointwise); `g 0 = id`, `g 1` the component swap; `c 1 = (1, 0)`. Then
`linkF N M (g · c) 0 = (0, 1)` and `g 0 (linkF N M c 0) = (1, 0)`. The transformation and the
configuration are bound variables pinned by the equations, never top-level definitions. -/
theorem d3b_witness :
    ∃ (g : Fin 2 → AddAut (Fin 2 → ZMod 2)) (c : Fin 2 → (Fin 2 → ZMod 2)),
      g 0 = AddEquiv.refl _ ∧ (∀ v, g 1 v = fun k => v (k + 1)) ∧ c 1 = ![1, 0]
        ∧ PreservesPointwise g (AddMonoidHom.id (Fin 2 → ZMod 2))
        ∧ linkF (![{1}, {0}] : Fin 2 → Finset (Fin 2)) (fun _ _ => AddMonoidHom.id _)
            (siteAct g c) 0 = ![0, 1]
        ∧ siteAct g (linkF (![{1}, {0}] : Fin 2 → Finset (Fin 2)) (fun _ _ => AddMonoidHom.id _) c)
            0 = ![1, 0] := by
  obtain ⟨σ, hσ⟩ : ∃ σ : AddAut (Fin 2 → ZMod 2), ∀ v, σ v = fun k => v (k + 1) :=
    ⟨{ toFun := fun v k => v (k + 1)
       invFun := fun v k => v (k + 1)
       left_inv := fun v => by
         funext k
         show v (k + 1 + 1) = v k
         congr 1
         fin_cases k <;> rfl
       right_inv := fun v => by
         funext k
         show v (k + 1 + 1) = v k
         congr 1
         fin_cases k <;> rfl
       map_add' := fun _ _ => rfl }, fun _ => rfl⟩
  refine ⟨![AddEquiv.refl _, σ], fun _ => ![1, 0], rfl, fun v => hσ v, rfl, fun _ _ => rfl,
    ?_, ?_⟩
  · show ∑ j ∈ ({1} : Finset (Fin 2)),
        (AddMonoidHom.id _) (![AddEquiv.refl _, σ] j (![1, 0] : Fin 2 → ZMod 2)) = ![0, 1]
    rw [Finset.sum_singleton, AddMonoidHom.id_apply]
    show σ ![1, 0] = ![0, 1]
    rw [hσ]
    funext k
    fin_cases k <;> rfl
  · show (AddEquiv.refl (Fin 2 → ZMod 2))
        (∑ j ∈ ({1} : Finset (Fin 2)), (AddMonoidHom.id _) (![1, 0] : Fin 2 → ZMod 2)) = ![1, 0]
    rw [Finset.sum_singleton, AddMonoidHom.id_apply, AddEquiv.refl_apply]

/-- **`D3-b` — A LINK-COUPLED RULE FAILING `A6-inv`**, on the frozen carrier. Together with
`a6cov_all`, the two readings are provably distinct, **in the one direction available**: on
link-coupled rules `A6-cov` always holds and `A6-inv` sometimes fails, so `A6-inv` is the strictly
stronger condition there, and no rule satisfies `A6-inv` and fails `A6-cov`. -/
theorem d3b_not_a6inv :
    ¬ A6Inv (linkF (![{1}, {0}] : Fin 2 → Finset (Fin 2))
        (fun _ _ => AddMonoidHom.id (Fin 2 → ZMod 2))) (AddMonoidHom.id _) := by
  intro h
  obtain ⟨g, c, -, -, -, hg, h1, h2⟩ := d3b_witness
  have hne : (![0, 1] : Fin 2 → ZMod 2) ≠ ![1, 0] := fun heq => by
    have := congrFun heq 0
    simp at this
  exact hne (h1.symm.trans ((congrFun (h g hg c) 0).trans h2))

/-! ### Section D — `D4`: single-edge rigidity on the constant-coupling rule -/

/-- **`D4-a` — SINGLE-EDGE RIGIDITY.** If `F (g · c) = g · (F c)` for the constant-coupling rule
`linkF N (fun _ _ => M₀)` and a given `g`, and `j ∈ N i`, then `∀ v, g i (M₀ v) = M₀ (g j v)`.
Evaluate at the indicator of `j` with value `v`; the sum over `N i` has one nonzero term. Needs no
connectivity and no pointwise-preservation hypothesis. -/
theorem d4a_single_edge [DecidableEq ι] {N : ι → Finset ι} {M₀ : V →+ V} {g : ι → AddAut V}
    (h : ∀ c, linkF N (fun _ _ => M₀) (siteAct g c) = siteAct g (linkF N (fun _ _ => M₀) c))
    {i j : ι} (hj : j ∈ N i) (v : V) : g i (M₀ v) = M₀ (g j v) := by
  have hc := congrFun (h (Pi.single j v : ι → V)) i
  simp only [linkF, siteAct] at hc
  have h1 : ∑ k ∈ N i, M₀ (g k ((Pi.single j v : ι → V) k)) = M₀ (g j v) := by
    rw [Finset.sum_eq_single_of_mem j hj fun k _ hk => by
      rw [Pi.single_eq_of_ne hk, map_zero, map_zero], Pi.single_eq_same]
  have h2 : ∑ k ∈ N i, M₀ ((Pi.single j v : ι → V) k) = M₀ v := by
    rw [Finset.sum_eq_single_of_mem j hj fun k _ hk => by
      rw [Pi.single_eq_of_ne hk, map_zero], Pi.single_eq_same]
  rw [h1, h2] at hc
  exact hc.symm

/-- **`D4-b` — ON EVERY EDGE, `g i = g j`**: with `M₀` injective and `g` preserving `M₀`
pointwise, commutation with the constant-coupling rule forces `g` equal across every edge. -/
theorem d4b_edge_rigidity [DecidableEq ι] {N : ι → Finset ι} {M₀ : V →+ V}
    (hinj : Function.Injective M₀) {g : ι → AddAut V} (hg : PreservesPointwise g M₀)
    (h : ∀ c, linkF N (fun _ _ => M₀) (siteAct g c) = siteAct g (linkF N (fun _ _ => M₀) c))
    {i j : ι} (hj : j ∈ N i) : g i = g j := by
  refine AddEquiv.ext fun v => hinj ?_
  rw [← hg i v, d4a_single_edge h hj v]

/-- **`D4-b` — A NONCONSTANT `g` IN THE POINTWISE STABILIZER, WITH ONE EDGE BETWEEN SITES WHERE IT
DIFFERS, REFUTES `A6-inv`** for the constant-coupling rule with injective `M₀`. -/
theorem d4b_not_a6inv_of_nonconstant [DecidableEq ι] {N : ι → Finset ι} {M₀ : V →+ V}
    (hinj : Function.Injective M₀) {g : ι → AddAut V} (hg : PreservesPointwise g M₀)
    {i j : ι} (hj : j ∈ N i) (hne : g i ≠ g j) : ¬ A6Inv (linkF N (fun _ _ => M₀)) M₀ :=
  fun h => hne (d4b_edge_rigidity hinj hg (h g hg) hj)

/-- **`A6-glob` HOLDS FOR EVERY CONSTANT-COUPLING RULE**: a global `g` commuting with `M₀` passes
through the neighbour sum by additivity. -/
theorem a6glob_constLink (N : ι → Finset ι) (M₀ : V →+ V) :
    A6Glob (linkF N (fun _ _ => M₀)) M₀ := by
  intro g hg c
  funext i
  simp only [linkF, map_sum, hg]

/-- **`D4-b` — THE SYMMETRIC POINT, ABSTRACTLY.** When the pointwise stabilizer of an injective
`M₀` is all of `AddAut V` — the shape of the manuscripts' symmetric point `M = μ I_6`, where every
internal-index transformation preserves the coupling — `A6-inv` **fails** for the constant-coupling
rule whenever `AddAut V` has two elements and `N` has an edge between distinct sites, while
`A6-glob` **holds** there.

**Single-edge by design.** The connected-carrier corollary — on a connected `N` with injective
`M₀`, `A6-inv` holds iff every pointwise-stabilizing `g` is constant — is analysis, not a target,
because "connected" is a definition this round does not spend. **What this says about the
manuscripts:** under reading (a) their `K`-component rule at `M = μ I_6` violates A6 for every
nonconstant `G(n)`; under (b) it satisfies A6; under (c) A6 is an identity on it. `D4` does not
choose among these. -/
theorem d4b_symmetric_point [DecidableEq ι] {N : ι → Finset ι} {M₀ : V →+ V}
    (hinj : Function.Injective M₀) (hcentral : ∀ (g : AddAut V) (v : V), g (M₀ v) = M₀ (g v))
    (hV : ∃ g₁ g₂ : AddAut V, g₁ ≠ g₂) {i j : ι} (hij : i ≠ j) (hj : j ∈ N i) :
    ¬ A6Inv (linkF N (fun _ _ => M₀)) M₀ ∧ A6Glob (linkF N (fun _ _ => M₀)) M₀ := by
  obtain ⟨g₁, g₂, hne⟩ := hV
  refine ⟨d4b_not_a6inv_of_nonconstant hinj (g := fun k => if k = i then g₁ else g₂)
    (fun k v => hcentral _ v) hj ?_, a6glob_constLink N M₀⟩
  simp only [if_neg (Ne.symm hij)]
  exact hne

/-- **`AddAut V` HAS TWO ELEMENTS AS SOON AS SOME `v ≠ -v`**: negation and the identity. On
`ZMod q` with `q ≥ 3` this is `1 ≠ -1`. -/
theorem addAut_nontrivial_of_ne_neg (v : V) (hv : v ≠ -v) : ∃ g₁ g₂ : AddAut V, g₁ ≠ g₂ :=
  ⟨AddEquiv.neg V, AddEquiv.refl V, fun heq => hv (by
    have := congrArg (fun e : AddAut V => e v) heq
    simpa using this.symm)⟩

/-- **EVERY ADDITIVE AUTOMORPHISM OF `K → ZMod q` IS `ZMod q`-LINEAR** — the additive-to-linear
step the freeze named as `D2-ii`'s only formal risk: a `ZMod q` scalar is the cast of an integer,
and an additive map commutes with integer multiples. It is why, on the alphabet `V = K → ZMod q`,
the pointwise stabilizer of `μ • id` is all of `AddAut V`. -/
theorem addAut_zmod_smul {K : Type} {q : ℕ} (g : AddAut (K → ZMod q)) (μ : ZMod q)
    (v : K → ZMod q) : g (μ • v) = μ • g v := by
  rw [← ZMod.intCast_zmod_cast μ, Int.cast_smul_eq_zsmul, Int.cast_smul_eq_zsmul, map_zsmul]

/-- **`D4-b` — THE SYMMETRIC POINT `M₀ = μ • id` ON `K → ZMod q`, `μ` A UNIT**: `A6-inv` fails
for the constant-coupling rule whenever `AddAut (K → ZMod q)` has two elements and `N` has an edge
between distinct sites, and `A6-glob` holds there. The coupling is pinned by its equation
`M₀ v = μ • v`; injectivity is the unit, and the pointwise stabilizer is everything by
`addAut_zmod_smul`. -/
theorem d4b_mu_id [DecidableEq ι] {K : Type} {q : ℕ} {N : ι → Finset ι} (μ : (ZMod q)ˣ)
    {M₀ : (K → ZMod q) →+ (K → ZMod q)} (hM : ∀ v, M₀ v = (μ : ZMod q) • v)
    (hV : ∃ g₁ g₂ : AddAut (K → ZMod q), g₁ ≠ g₂) {i j : ι} (hij : i ≠ j) (hj : j ∈ N i) :
    ¬ A6Inv (linkF N (fun _ _ => M₀)) M₀ ∧ A6Glob (linkF N (fun _ _ => M₀)) M₀ :=
  d4b_symmetric_point
    (fun v w h => by
      rw [hM, hM, ← Units.smul_def, ← Units.smul_def] at h
      exact smul_left_cancel μ h)
    (fun g v => by rw [hM, hM, addAut_zmod_smul]) hV hij hj

/-! ### Section E — `D2`: the manuscripts' wave rule against the degenerate form -/

/-- **`D2-i` — THE FROZEN WITNESS, WITH ITS EQUATIONS.** `d = 1`, `L = 3`, `q = 3`, `α = 1`;
`g 0 = 1`, `g 1 = 2`, `g 2 = 1` as unit multiplications on `ZMod 3`; `c` the indicator of site `1`
with value `1`. Then `F (g · c) 0 = 2` and `g 0 (F c 0) = 1`. Every `g` preserves the site
coupling `mulLeft 1` pointwise. **A fact about the degenerate form** — `K` a singleton, the
transformation group the alphabet's unit group acting by rescaling — **and labelled so**: this is
not the manuscripts' A6. -/
theorem d2i_wave_witness :
    ∃ (g : (Fin 1 → ZMod 3) → AddAut (ZMod 3)) (c : (Fin 1 → ZMod 3) → ZMod 3),
      PreservesPointwise g (AddMonoidHom.mulLeft (1 : ZMod 3))
        ∧ (∀ v, g (fun _ => 0) v = v) ∧ (∀ v, g (fun _ => 1) v = 2 * v)
        ∧ (∀ v, g (fun _ => 2) v = v)
        ∧ (∀ i, c i = if i 0 = 1 then 1 else 0)
        ∧ (waveSubstratum 1 3 3 1).R.F (siteAct g c) (fun _ => 0) = (2 : ZMod 3)
        ∧ g (fun _ => 0) ((waveSubstratum 1 3 3 1).R.F c (fun _ => 0)) = (1 : ZMod 3) := by
  obtain ⟨u, hu⟩ : ∃ u : AddAut (ZMod 3), ∀ v, u v = 2 * v :=
    ⟨{ toFun := fun v => 2 * v
       invFun := fun v => 2 * v
       left_inv := by intro v; revert v; decide
       right_inv := by intro v; revert v; decide
       map_add' := fun _ _ => mul_add _ _ _ }, fun _ => rfl⟩
  have e1 : ((fun _ => 0 : Fin 1 → ZMod 3) + dir 1 3 (0, true)) = fun _ => 1 := by
    funext k
    fin_cases k
    simp [dir]
  have e2 : ((fun _ => 0 : Fin 1 → ZMod 3) + dir 1 3 (0, false)) = fun _ => 2 := by
    funext k
    fin_cases k
    simp [dir]
    decide
  have h21 : (2 : ZMod 3) ≠ 1 := by decide
  have h01 : (0 : ZMod 3) ≠ 1 := by decide
  refine ⟨fun i => if i 0 = 1 then u else AddEquiv.refl (ZMod 3), fun i => if i 0 = 1 then 1 else 0,
    fun i v => ?_, fun v => ?_, fun v => ?_, fun v => ?_, fun _ => rfl, ?_, ?_⟩
  · simp only [AddMonoidHom.coe_mulLeft, one_mul]
  · show (if (0 : ZMod 3) = 1 then u else AddEquiv.refl (ZMod 3)) v = v
    rw [if_neg h01, AddEquiv.refl_apply]
  · show (if (1 : ZMod 3) = 1 then u else AddEquiv.refl (ZMod 3)) v = 2 * v
    rw [if_pos rfl, hu]
  · show (if (2 : ZMod 3) = 1 then u else AddEquiv.refl (ZMod 3)) v = v
    rw [if_neg h21, AddEquiv.refl_apply]
  · show waveF 1 3 3 1 (siteAct (fun i => if i 0 = 1 then u else AddEquiv.refl (ZMod 3))
      (fun i => if i 0 = 1 then 1 else 0)) (fun _ => 0) = 2
    unfold waveF
    rw [Fintype.sum_prod_type, Fin.sum_univ_one, Fintype.sum_bool, e1, e2]
    simp only [siteAct, ite_true, if_neg h21, hu, AddEquiv.refl_apply]
    decide
  · show (if (0 : ZMod 3) = 1 then u else AddEquiv.refl (ZMod 3))
      (waveF 1 3 3 1 (fun i => if i 0 = 1 then 1 else 0) (fun _ => 0)) = 1
    rw [if_neg h01, AddEquiv.refl_apply]
    unfold waveF
    rw [Fintype.sum_prod_type, Fin.sum_univ_one, Fintype.sum_bool, e1, e2]
    simp only [ite_true, if_neg h21]
    decide

/-- **`D2-i` — `A6-inv` FAILS ON THE DEGENERATE FORM** at `d = 1`, `L = 3`, `q = 3`, `α = 1`: the
frozen witness. Statable; degenerate; false in the degenerate form; and not the axiom. -/
theorem d2i_wave_not_a6inv :
    ¬ A6Inv (ι := Fin 1 → ZMod 3) (V := ZMod 3) (waveSubstratum 1 3 3 1).R.F
        (AddMonoidHom.mulLeft 1) := by
  intro h
  obtain ⟨g, c, hg, -, -, -, -, h1, h2⟩ := d2i_wave_witness
  have := congrFun (h g hg c) (fun _ => 0)
  exact absurd ((h1.symm.trans this).trans h2) (by decide : (2 : ZMod 3) ≠ 1)

/-- **`D2-ii` — `A6-glob` HOLDS FOR EVERY WAVE SUBSTRATUM**: a global `g` commuting with `mulLeft α`
passes through `α · Σ` by additivity. The additive-to-linear step the freeze named as the only risk
is not needed here: the commutation with `α` is the hypothesis of `A6Glob` itself. -/
theorem d2ii_wave_a6glob (d L q : ℕ) (α : ZMod q) :
    A6Glob (ι := Fin d → ZMod L) (V := ZMod q) (waveSubstratum d L q α).R.F
      (AddMonoidHom.mulLeft α) := by
  intro g hg c
  funext i
  show waveF d L q α (fun i => g (c i)) i = g (waveF d L q α c i)
  simp only [AddMonoidHom.coe_mulLeft] at hg
  unfold waveF
  rw [hg, map_sum]

end BackgroundIndependence
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.BackgroundIndependence.a6glob_of_a6inv
#print axioms OIBridge.BackgroundIndependence.leap_siteAct
#print axioms OIBridge.BackgroundIndependence.a6cov_all
#print axioms OIBridge.BackgroundIndependence.d3b_witness
#print axioms OIBridge.BackgroundIndependence.d3b_not_a6inv
#print axioms OIBridge.BackgroundIndependence.d4a_single_edge
#print axioms OIBridge.BackgroundIndependence.d4b_edge_rigidity
#print axioms OIBridge.BackgroundIndependence.d4b_not_a6inv_of_nonconstant
#print axioms OIBridge.BackgroundIndependence.a6glob_constLink
#print axioms OIBridge.BackgroundIndependence.d4b_symmetric_point
#print axioms OIBridge.BackgroundIndependence.addAut_nontrivial_of_ne_neg
#print axioms OIBridge.BackgroundIndependence.addAut_zmod_smul
#print axioms OIBridge.BackgroundIndependence.d4b_mu_id
#print axioms OIBridge.BackgroundIndependence.d2i_wave_witness
#print axioms OIBridge.BackgroundIndependence.d2i_wave_not_a6inv
#print axioms OIBridge.BackgroundIndependence.d2ii_wave_a6glob
