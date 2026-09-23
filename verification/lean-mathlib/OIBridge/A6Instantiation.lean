import OIBridge.BackgroundIndependence

/-!
# A6 instantiation, round 2 — does the manuscripts' substratum instantiate the covariant interface?

Executed under the frozen control plane
`verification/programmes/substratum/a6-instantiation/preregistration.md`, blob
`6f991c1348e0c568261894c41b129b7f942abee6`, from `main` at
`3e5d6a8f75166581213b6c5b7c0dbca1671b030e` — the merge commit of that control plane (PR #623),
which the freeze fixes as this round's mandated base.

## What this round is

An **instantiation round**. The interpretation problem is settled elsewhere: `A6-cov` is the
adopted publication meaning of the sixth structural assumption and the `ROADMAP` row `P1 — A6`
reads `CONDITIONAL`. The named hypothesis that row carries is that the manuscripts' substratum
instantiates the covariant interface, in two halves the freeze keeps **apart**: the `K = 6`
link-coupled rule is not packaged as a `Substratum` (the interface's `waveSubstratum` has a
singleton internal index), and the complex lift on which `[SM §3.1]` conducts the gauge derivation
is outside the interface. This module discharges what it can of each half separately.

**Notation.** The four readings are always suffixed — `A6-cov`, `A6-inv`, `A6-glob`, `A6-sd` — as
round 1's rule requires. They are four objects on three interfaces and **no two of them are ever
identified**. The bare name appears only inside a quotation or in the `ROADMAP` row name.

## The trap this module sits over, stated first

Round 1 proved `a6cov_all : ∀ N M, A6Cov N M` — **the adopted reading holds identically on every
link-coupled rule of the interface, so its content is the covariant interface itself and not a
constraint**. It follows that an instantiation positive carries exactly the information that the
manuscripts' rule **is of the link-coupled form**, and carries no information that a condition was
tested and survived. Any sentence of the form "the assumption was checked on the substratum and
holds" would be a defect even on a full positive.

## What is here

* **`PK` — the packaging.** `linkRule` and `linkSubstratum` package a link-coupled rule as a
  `Substratum` of the kernel's own structure, with `Rule.dep` and `Rule.mem_infl` discharged and
  **no field added to `Substratum`**. `pk1_packaging` records the packaged carrier's data at the
  manuscripts' site type, alphabet and neighbourhood; `pk2a_bridge` is the bridge equation
  `R.F = linkF R.N M`, which is the content of `PK2`; `pk2b_covariance` is `A6Cov` on the packaged
  carrier's own link data, an **instance of a merged identity and not a new theorem**.
  `pk3a_A1`–`pk3e_A5` put the packaged carrier against `A1`–`A5`, `A4Exact` **under the
  translation-invariance hypothesis on the link coupling, which is part of the statement and is
  reported with it every time**. `pk4_shift_not_scalar` exhibits a non-scalar additive
  automorphism of `Fin 6 → ZMod q`. `pk5_symmetric_point` is the separate stronger
  fixed-background condition `A6-inv` failing at `M = μ I_6` on the packaged carrier while
  `A6-glob` holds.
* **`CX` — the complex lift.** `cx1_complex_covariance` is the interface's own predicate at
  `V = Fin 6 → ℂ`, with **no new definition and no structure added**. `cx2_clinear_forgets`,
  `cx2_manuscript_law` and `cx2_unitary_gaugeLink` exhibit the manuscripts' site-dependent
  transformation as an instance of the interface's transformation class.
  `cx3a_complex_axioms` and `cx3b_complex_not_A1` are the round's load-bearing distinction: the
  **covariance statement** comes inside the interface, the **complex carrier does not come inside
  as a substratum**, because finiteness is the first of the interface's axioms and the complex
  carrier is infinite.
* **`AS` — the assembled statement.** `as1_leap_covariant` carries the covariant form to the
  second-order dynamics, stated once polymorphically in the alphabet and instantiated at both.

## What none of this licenses

Nothing here says the sixth assumption holds of the **physical** substratum, or fails of it: the
packaged carrier is a formal object built from the data the manuscripts state, and that the
physical substratum is that object is a premise no round can discharge. Nothing here touches the
Standard-Model gauge-group derivation: Theorems 5 and 7 of `SM`, H-link, H-cust, the `(3,2,1)`
decomposition, the condensate stabilizer, the reduction to `SU(3) × SU(2) × U(1)` and the Wilson
action are neither consumed nor judged. `pk5_symmetric_point` is the separate stronger
fixed-background condition failing, which is the recorded reason it is not the adopted meaning;
**it is not "the substratum violates the assumption"**, and that sentence is forbidden in terms.
`AddAut (Fin 6 → ZMod q)` is not `GL(6, ℤ/qℤ)` and `AddAut (Fin 6 → ℂ)` is not `U(6)`; the one
containment used is proved, in `cx2_unitary_gaugeLink`, and the interface's class is strictly
larger, so the interface's statement **contains** the manuscripts' law as a specialization and is
not identical to it. No inner product, unitarity as a constraint on the interface, condensate,
state or cubic group action enters, `A1` is not weakened, no second substratum structure is
introduced, and no field is added to `Substratum`. No manuscript is edited. No `ROADMAP` label is
moved, and no label change is recommended.
-/

namespace OIBridge
namespace A6Instantiation

open SecondOrderLayer SubstratumInterfaceAudit BackgroundIndependence
open OIBridge.SecondOrderCircuit (leapEquiv leap curOf leap_apply curOf_apply leapEquiv_apply)

/-! ### Section A — the packaging: the two budget slots that fire

Budget slot 1 and budget slot 2. Slots 3, 4 and 5 are conditional and do not fire: the
translation-invariance hypothesis is written inline in the two statements that carry it, so that
hazard 11 is discharged by the statement itself rather than by a name; `Fin 6 → ℂ` is written out;
and `PK2-a` is stated as the equation it is, on the packaged carrier, without a packaging
predicate. -/

section Packaging

variable {ι V : Type} [DecidableEq ι] [AddCommGroup V]

/-- **THE LINK-COUPLED RULE** (budget slot 1): the merged `linkF N M` as a `Rule ι V`, with the
given neighbourhood function serving as both `N` and `infl`.

`dep` is the observation that the sum over `N i` reads the configuration only on `N i`;
`mem_infl` is exactly the symmetry of the neighbourhood, carried as a hypothesis rather than
assumed of every neighbourhood function. **No field is added to `Substratum` or to `Rule`.** -/
def linkRule (N : ι → Finset ι) (M : ι → ι → (V →+ V))
    (hsymm : ∀ i j, j ∈ N i → i ∈ N j) : Rule ι V where
  F := linkF N M
  N := N
  infl := N
  dep i c c' h := Finset.sum_congr rfl fun j hj => by rw [h j hj]
  mem_infl := hsymm

/-- **THE PACKAGED CARRIER** (budget slot 2): the `Substratum` a link-coupled rule builds, at a
site type, an alphabet, a neighbourhood function and a link coupling, **all parameters**.

Stated once and instantiated at both alphabets — `Fin 6 → ZMod q` for `PK` and `Fin 6 → ℂ` for
`CX3` — so that the finite and the complex carriers are the same construction and the difference
between them is visible. The internal index enters **only through the alphabet**, exactly as
round 1 froze it; `Substratum` has no field for it and none is added. -/
def linkSubstratum (ι V : Type) [DecidableEq ι] [AddCommGroup ι] [AddCommGroup V]
    (N : ι → Finset ι) (M : ι → ι → (V →+ V)) (hsymm : ∀ i j, j ∈ N i → i ∈ N j) : Substratum where
  ι := ι
  V := V
  R := linkRule N M hsymm

variable [AddCommGroup ι]

/-- **THE BRIDGE EQUATION, POLYMORPHIC IN THE ALPHABET**: the packaged carrier's update map is the
interface's link-coupled map, for the very link coupling the packaging carries, read on the
carrier's own neighbourhood function. `PK2-a` is this equation at the manuscripts' data.

Stating it as a theorem rather than leaving it to definitional unfolding is what makes the bridge
auditable. -/
theorem linkSubstratum_bridge (N : ι → Finset ι) (M : ι → ι → (V →+ V))
    (hsymm : ∀ i j, j ∈ N i → i ∈ N j) :
    (linkSubstratum ι V N M hsymm).R.F
      = linkF (linkSubstratum ι V N M hsymm).R.N M := rfl

/-- **THE PACKAGED CARRIER SATISFIES A2**, for every site type, alphabet, neighbourhood and link
coupling: bijectivity of the phase-space map is automatic for the second-order form
(`a2_every_substratum`). -/
theorem linkSubstratum_A2 (N : ι → Finset ι) (M : ι → ι → (V →+ V))
    (hsymm : ∀ i j, j ∈ N i → i ∈ N j) : (linkSubstratum ι V N M hsymm).A2 :=
  Substratum.a2_every_substratum _

/-- **THE PACKAGED CARRIER SATISFIES A5**, for every site type, alphabet, neighbourhood and link
coupling: each `M i j` is additive and the neighbour sum is finite. **The proof does not use
finiteness of the alphabet**, which is why `CX3-a` gets it at the complex carrier. -/
theorem linkSubstratum_A5 (N : ι → Finset ι) (M : ι → ι → (V →+ V))
    (hsymm : ∀ i j, j ∈ N i → i ∈ N j) : (linkSubstratum ι V N M hsymm).A5 := by
  intro c c'
  funext i
  show ∑ j ∈ N i, M i j (c j + c' j) = (∑ j ∈ N i, M i j (c j)) + ∑ j ∈ N i, M i j (c' j)
  rw [← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun j _ => map_add _ _ _

end Packaging

/-! ### Section B — the packaged carrier on the manuscripts' axis neighbourhood

`A3` and the exact form of `A4` are the two axioms that see the neighbourhood function, so they
are stated at `nbrs d L` — the merged axis neighbourhood of the cubic torus — and still
polymorphically in the alphabet, for the same reason. -/

section Axis

variable (V : Type) [AddCommGroup V] (d L : ℕ)

/-- **THE PACKAGED CARRIER ON THE AXIS NEIGHBOURHOOD SATISFIES A3 WITH DEGREE `2d`**: the merged
`waveSubstratum_A3` argument, `Finset.card_image_le` against the `d × Bool` index of the axis
steps, applies to the same neighbourhood. **The proof does not use finiteness of the alphabet.** -/
theorem linkSubstratum_A3
    (M : (Fin d → ZMod L) → (Fin d → ZMod L) → (V →+ V)) :
    (linkSubstratum (Fin d → ZMod L) V (nbrs d L) M
      (fun _ _ h => mem_nbrs_symm d L h)).A3 (2 * d) := by
  intro i
  show (nbrs d L i).card ≤ 2 * d
  refine Finset.card_image_le.trans ?_
  simp [mul_comm]

/-- **THE AXIS NEIGHBOURHOOD TRANSLATES**: `nbrs d L (i - w)` is `nbrs d L i` shifted by `w`. The
step the freeze named as the only place `A4Exact` could fail, and it does not: `nbrs` is an image
of `i + dir p`, and the translation passes through the sum. -/
theorem nbrs_sub (w i : Fin d → ZMod L) :
    nbrs d L (i - w) = (nbrs d L i).image (fun j => j - w) := by
  show Finset.univ.image (fun p => (i - w) + dir d L p)
      = (Finset.univ.image (fun p => i + dir d L p)).image (fun j => j - w)
  rw [Finset.image_image]
  refine Finset.image_congr (fun p _ => ?_)
  show (i - w) + dir d L p = (i + dir d L p) - w
  abel

/-- **THE PACKAGED CARRIER ON THE AXIS NEIGHBOURHOOD SATISFIES THE EXACT FORM OF A4 UNDER
TRANSLATION INVARIANCE OF THE LINK COUPLING.**

**The hypothesis `∀ v i j, M (i + v) (j + v) = M i j` is part of the statement and is reported
with it every time.** The manuscripts' isotropic coupling supplies it and the constant coupling
satisfies it outright. **`A4Exact` for a general link coupling is false**: without the hypothesis
the rule at a translated site consults a translated coupling, and nothing makes the two agree.
**The proof does not use finiteness of the alphabet.** -/
theorem linkSubstratum_A4Exact
    (M : (Fin d → ZMod L) → (Fin d → ZMod L) → (V →+ V))
    (hM : ∀ v i j, M (i + v) (j + v) = M i j) :
    (linkSubstratum (Fin d → ZMod L) V (nbrs d L) M
      (fun _ _ h => mem_nbrs_symm d L h)).A4Exact := by
  intro (w : Fin d → ZMod L) (c : (Fin d → ZMod L) → V)
  funext (i : Fin d → ZMod L)
  show ∑ j ∈ nbrs d L i, M i j (c (j - w)) = ∑ j ∈ nbrs d L (i - w), M (i - w) j (c j)
  rw [nbrs_sub d L w i, Finset.sum_image (fun a _ b _ h => by simpa using h)]
  refine Finset.sum_congr rfl fun j _ => ?_
  have hMij : M (i - w) (j - w) = M i j := by
    have h2 := hM w (i - w) (j - w)
    rw [sub_add_cancel, sub_add_cancel] at h2
    exact h2.symm
  rw [hMij]

end Axis

/-! ### Section C — `PK`: the first obstacle, packaging the six-fold link-coupled rule

The manuscripts' data, as `PK0` records them by quotation: the site type is the cubic torus
`Fin d → ZMod L`; the alphabet is `Fin 6 → ZMod q`, the `K = 6` component vector over `ℤ/qℤ`; the
neighbourhood is the axis neighbourhood `nbrs d L`; the coupling in link-valued form is `linkF`'s
parameter `M : ι → ι → (V →+ V)`, with the normalization `1/d` absorbed into it and the isotropy
constraint carried by the link-coupled form; and the second-order term `-φ(n, t-1)` is carried by
the phase-space map `leapEquiv` and is not part of `F`. **`d`, `L`, `q` and the coupling stay
parameters**: the packaged carrier is a family in them, `d = 3` is an empirical filter in the
manuscripts that no target of this round asserts, and no instance of `M` is chosen. -/

section PK

variable (d L q : ℕ)
  (M : (Fin d → ZMod L) → (Fin d → ZMod L) → ((Fin 6 → ZMod q) →+ (Fin 6 → ZMod q)))

/-- **`PK1` — THE PACKAGING EXISTS.** There is a `Substratum` of the kernel's own structure with
site type the cubic torus `Fin d → ZMod L`, alphabet the six-component vector `Fin 6 → ZMod q`,
neighbourhood and influence the axis neighbourhood `nbrs d L`, and update map the interface's
link-coupled map for a link coupling carried as a parameter — with `Rule.dep` and `Rule.mem_infl`
discharged, `mem_infl` by the merged `mem_nbrs_symm`.

**Bounded reading:** this is a formal object built from the data the manuscripts state. It is not
a statement that the manuscripts' physical substratum is this object; that identification is a
premise no round can discharge. -/
theorem pk1_packaging :
    (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) M
        (fun _ _ h => mem_nbrs_symm d L h)).R.N = nbrs d L
      ∧ (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) M
          (fun _ _ h => mem_nbrs_symm d L h)).R.infl = nbrs d L
      ∧ (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) M
          (fun _ _ h => mem_nbrs_symm d L h)).R.F = linkF (nbrs d L) M :=
  ⟨rfl, rfl, rfl⟩

/-- **`PK2-a` — THE BRIDGE EQUATION**, at the manuscripts' data: the packaged carrier's update map
is the interface's link-coupled map for the very link coupling the packaging carries, read on the
carrier's own neighbourhood function.

**This is the content of `PK2`**: the identification of the manuscripts' carrier with the
interface's. -/
theorem pk2a_bridge :
    (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) M
        (fun _ _ h => mem_nbrs_symm d L h)).R.F
      = linkF (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) M
          (fun _ _ h => mem_nbrs_symm d L h)).R.N M :=
  linkSubstratum_bridge _ _ _

/-- **`PK2-b` — THE ADOPTED READING HOLDS OF THE PACKAGED CARRIER'S OWN LINK DATA**, an instance
of the merged `a6cov_all`.

**Bounded reading, and it is the whole point of the round:** `A6Cov` holds for **every**
neighbourhood function and **every** link coupling, so this instance carries exactly the
information that the packaged carrier's rule is link-coupled, and carries **no** information that
a condition was tested and survived. It is an instance of a merged identity and **not a new
theorem**. -/
theorem pk2b_covariance : A6Cov (nbrs d L) M := a6cov_all _ _

/-- **`PK3-a` — A1** on the packaged carrier, for a nonzero torus size and a nonzero alphabet
modulus: the configuration space `ι → V × V` is finite. -/
theorem pk3a_A1 [NeZero L] [NeZero q] :
    (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) M
      (fun _ _ h => mem_nbrs_symm d L h)).A1 := by
  show Finite ((Fin d → ZMod L) → (Fin 6 → ZMod q) × (Fin 6 → ZMod q))
  infer_instance

/-- **`PK3-b` — A2** on the packaged carrier, by `a2_every_substratum`. -/
theorem pk3b_A2 :
    (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) M
      (fun _ _ h => mem_nbrs_symm d L h)).A2 :=
  linkSubstratum_A2 _ _ _

/-- **`PK3-c` — A3 WITH DEGREE `2d`** on the packaged carrier. -/
theorem pk3c_A3 :
    (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) M
      (fun _ _ h => mem_nbrs_symm d L h)).A3 (2 * d) :=
  linkSubstratum_A3 _ d L M

/-- **`PK3-d` — THE EXACT FORM OF A4 UNDER THE TRANSLATION-INVARIANCE HYPOTHESIS ON THE LINK
COUPLING**, `∀ v i j, M (i + v) (j + v) = M i j`, on the packaged carrier.

**The hypothesis is part of the statement and is reported with it every time**; the manuscripts'
isotropic coupling supplies it and the constant coupling satisfies it outright. **`A4Exact` for a
general link coupling is false.** -/
theorem pk3d_A4Exact (hM : ∀ v i j, M (i + v) (j + v) = M i j) :
    (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) M
      (fun _ _ h => mem_nbrs_symm d L h)).A4Exact :=
  linkSubstratum_A4Exact _ d L M hM

/-- **`PK3-e` — A5** on the packaged carrier. -/
theorem pk3e_A5 :
    (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) M
      (fun _ _ h => mem_nbrs_symm d L h)).A5 :=
  linkSubstratum_A5 _ _ _

end PK

/-- **`PK4` — THE INTERNAL INDEX OF THE PACKAGED CARRIER IS NOT THE DEGENERATE ONE.** On
`V = Fin 6 → ZMod q` with `q ≥ 2` the cyclic component shift `v ↦ fun k => v (k + 1)` — pinned by
that equation, as in the merged `d3b_witness` — is an additive automorphism that is **not**
multiplication by any scalar of the alphabet. So the site-dependent transformations available to
the packaged carrier are strictly more than the alphabet-rescaling freedom of the singleton-index
case.

**Bounded reading, frozen:** round 1's degeneracy verdict — the singleton-`K` rescalings are the
amplitude-scale freedom the manuscripts assign to A5, not the internal-index freedom of the sixth
assumption — **stands for `waveSubstratum`**, is not touched, and **does not apply to the packaged
carrier**. That is what this says and all it says. It does **not** say that
`AddAut (Fin 6 → ZMod q)` is the manuscripts' `G(n)`: over the finite alphabet there is no unitary
group and none is introduced. -/
theorem pk4_shift_not_scalar (q : ℕ) (hq : 2 ≤ q) :
    ∃ g : AddAut (Fin 6 → ZMod q),
      (∀ v, g v = fun k => v (k + 1)) ∧ ∀ μ : ZMod q, ∃ v, g v ≠ μ • v := by
  have : Fact (1 < q) := ⟨hq⟩
  obtain ⟨σ, hσ⟩ : ∃ σ : AddAut (Fin 6 → ZMod q), ∀ v, σ v = fun k => v (k + 1) :=
    ⟨{ toFun := fun v k => v (k + 1)
       invFun := fun v k => v (k - 1)
       left_inv := fun v => by
         funext k
         show v (k - 1 + 1) = v k
         rw [sub_add_cancel]
       right_inv := fun v => by
         funext k
         show v (k + 1 - 1) = v k
         rw [add_sub_cancel_right]
       map_add' := fun _ _ => rfl }, fun _ => rfl⟩
  refine ⟨σ, hσ, fun μ => ⟨Pi.single 0 1, fun h => ?_⟩⟩
  have h5 := congrFun (hσ (Pi.single 0 1) ▸ h) 5
  rw [show (5 : Fin 6) + 1 = 0 from rfl, Pi.single_eq_same, Pi.smul_apply,
    Pi.single_eq_of_ne (by decide : (5 : Fin 6) ≠ 0), smul_zero] at h5
  exact one_ne_zero h5

/-- **`PK5` — THE SEPARATE STRONGER CONDITION ON THE PACKAGED CARRIER AT THE SYMMETRIC POINT.** At
the manuscripts' symmetric point, the constant coupling pinned by `M₀ v = μ • v` for a unit
`μ : (ZMod q)ˣ`, on the packaged carrier with `d ≥ 1`, `L ≥ 2`, `q ≥ 2`: the **fixed-background**
condition `A6-inv` **fails**, and the global specialization `A6-glob` **holds** — instances of the
merged `d4b_mu_id` and `a6glob_constLink` at the manuscripts' site type and component count, with
the edge between distinct sites supplied by `i + dir (k, true) ≠ i` and the two elements of
`AddAut (Fin 6 → ZMod q)` by `PK4`'s shift.

`L = 1` is excluded by hypothesis, not by a counterexample: the one-site torus has no edge between
distinct sites, so `d4b_mu_id`'s hypothesis is unavailable there.

**Bounded reading, frozen, and it is the sharpest place this round can be misread:** this is
`A6-inv`, the separate and strictly stronger **fixed-background** condition, failing — and
`A6-inv` is **not** the adopted meaning. The failure is the recorded reason it is not the adopted
meaning: as the definition it would refute the manuscripts' own rule for exactly the
site-dependent transformations the gauge reading needs. It is neither a defect of the manuscripts'
rule nor a failure of the sixth assumption, and **the sentence "the substratum violates A6" is
forbidden in terms**. -/
theorem pk5_symmetric_point (d L q : ℕ) (hd : 1 ≤ d) (hL : 2 ≤ L) (hq : 2 ≤ q)
    (μ : (ZMod q)ˣ) (M₀ : (Fin 6 → ZMod q) →+ (Fin 6 → ZMod q))
    (hM : ∀ v, M₀ v = (μ : ZMod q) • v) :
    ¬ A6Inv (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) (fun _ _ => M₀)
        (fun _ _ h => mem_nbrs_symm d L h)).R.F M₀
      ∧ A6Glob (linkSubstratum (Fin d → ZMod L) (Fin 6 → ZMod q) (nbrs d L) (fun _ _ => M₀)
          (fun _ _ h => mem_nbrs_symm d L h)).R.F M₀ := by
  have : Fact (1 < L) := ⟨hL⟩
  obtain ⟨σ, hσ, hns⟩ := pk4_shift_not_scalar q hq
  obtain ⟨v₀, hv₀⟩ := hns 1
  set k : Fin d := ⟨0, hd⟩ with hk
  refine d4b_mu_id (ι := Fin d → ZMod L) (K := Fin 6) (N := nbrs d L) μ hM
    ⟨σ, AddEquiv.refl _, fun heq => hv₀ ?_⟩ (i := 0) (j := 0 + dir d L (k, true)) ?_ ?_
  · rw [heq, one_smul]
    rfl
  · intro heq
    have hd1 : (dir d L (k, true)) k = 0 := by
      have := congrFun heq k
      simpa [dir] using this.symm
    rw [show dir d L (k, true) = Pi.single k 1 from rfl, Pi.single_eq_same] at hd1
    exact one_ne_zero hd1
  · exact Finset.mem_image.mpr ⟨(k, true), Finset.mem_univ _, rfl⟩

/-! ### Section D — `CX`: the second obstacle, the complex lift

The freeze's scope decision, recorded as a decision: `A6Cov` is stated for an alphabet that is any
additive commutative group, so instantiating the alphabet at `Fin 6 → ℂ` introduces **no
definition and no structure** — it is the interface's own predicate at a carrier the interface
already admits. **No unitary group is introduced as a structure on the interface**, and no inner
product, condensate, state, cubic group action or field on `Substratum` enters. -/

section CX

/-- **`CX1` — THE COVARIANCE STATEMENT AT A COMPLEX CARRIER IS INSIDE THE INTERFACE.** `A6Cov` at
`V = Fin 6 → ℂ`, for every neighbourhood function and every link coupling: the interface's own
predicate at an alphabet the interface already admits, with **no new definition and no structure
added**, and `a6cov_all` gives it.

**Bounded reading, frozen:** what comes inside the interface is the **covariance identity**. The
inner product, unitarity as a constraint, the condensate `Σ`, the stabilizer in `U(6)`, the cubic
decomposition and the reduction to `SU(3) × SU(2) × U(1)` do **not** come inside, and none of them
is introduced. `A6Cov` here quantifies over **all** additive automorphisms of `Fin 6 → ℂ`, a
strictly larger class than the unitary group, so the statement **contains** the manuscripts'
transformation law as a specialization and is **not identical to it**. Reporting the general
statement as a `U(6)` theorem, or the specialization as the general statement, is a defect. -/
theorem cx1_complex_covariance {ι : Type} (N : ι → Finset ι)
    (M : ι → ι → ((Fin 6 → ℂ) →+ (Fin 6 → ℂ))) : A6Cov N M :=
  a6cov_all N M

/-- **`CX2` — A `ℂ`-LINEAR AUTOMORPHISM FORGETS TO AN ADDITIVE ONE.** A site-dependent family of
`ℂ`-linear automorphisms of `Fin 6 → ℂ` is a `g : ι → AddAut V` of the interface, with the
transformation, its inverse and the transported link coupling pinned by their equations; the
transported coupling is `SM.md:112`'s law `G(n) M(n, ê_j) G(n + ê_j)⁻¹`.

**Bounded reading, frozen:** this is a statement about the **class**, not about a group. It does
not identify `AddAut (Fin 6 → ℂ)` with `U(6)`, does not say that unitarity is derivable, and does
not say that unitarity is dispensable in the manuscripts' derivation — only that the covariance
identity does not consume it. -/
theorem cx2_clinear_forgets {ι : Type} (G : ι → ((Fin 6 → ℂ) ≃ₗ[ℂ] (Fin 6 → ℂ)))
    (M : ι → ι → ((Fin 6 → ℂ) →+ (Fin 6 → ℂ))) :
    ∃ g : ι → AddAut (Fin 6 → ℂ),
      (∀ i v, g i v = G i v) ∧ (∀ i v, (g i).symm v = (G i).symm v)
        ∧ ∀ i j v, gaugeLink g M i j v = G i (M i j ((G j).symm v)) :=
  ⟨fun i => (G i).toAddEquiv, fun _ _ => rfl, fun _ _ => rfl, fun _ _ _ => rfl⟩

/-- **`CX2` — THE MANUSCRIPTS' TRANSFORMATION LAW IS AN INSTANCE OF THE INTERFACE'S COVARIANCE.**
For a site-dependent family of `ℂ`-linear automorphisms, the link-coupled rule with the
transported coupling carries the transformed configuration exactly as the untransformed rule
carries the configuration — the identity `SM.md:114` displays, at the complex six-component
carrier, as an instance of `a6cov_all` and of nothing else.

**Bounded reading, frozen:** this is the covariance identity, not the manuscripts' derivation. It
is an instance of an identity that holds for **every** link coupling, so it carries exactly the
information that the rule is link-coupled. -/
theorem cx2_manuscript_law {ι : Type} (N : ι → Finset ι)
    (G : ι → ((Fin 6 → ℂ) ≃ₗ[ℂ] (Fin 6 → ℂ)))
    (M : ι → ι → ((Fin 6 → ℂ) →+ (Fin 6 → ℂ))) (c : ι → (Fin 6 → ℂ)) :
    linkF N (fun i j => ((G i).toAddEquiv.toAddMonoidHom.comp (M i j)).comp
        (G j).toAddEquiv.symm.toAddMonoidHom) (fun i => G i (c i))
      = fun i => G i (linkF N M c i) :=
  a6cov_all N M (fun i => (G i).toAddEquiv) c

/-- **`CX2` — THE MATRIX-UNITARY PACKAGING, IN THE KERNEL.** A site-dependent family of unitary
`6 × 6` complex matrices acts on `Fin 6 → ℂ` by `mulVec`, and that action is an additive
automorphism of the carrier; the transported coupling is `SM.md:112`'s law with `G(n)` unitary and
`G(n + ê_j)⁻¹` its conjugate transpose, and the covariance identity holds of it, by `a6cov_all`.

**The containment is proved here and not asserted**: `AddAut (Fin 6 → ℂ)` is **not** `U(6)`, and
what this exhibits is that each unitary supplies an element of the interface's transformation
class — a containment, in one direction, with the interface's class strictly larger. Unitarity is
**not consumed** by the covariance identity: it is used only to invert the action. Nothing here
introduces a unitary group as a structure on the interface, and nothing here says that unitarity
is derivable or that it is dispensable in the manuscripts' derivation. -/
theorem cx2_unitary_gaugeLink {ι : Type} (N : ι → Finset ι)
    (U : ι → Matrix (Fin 6) (Fin 6) ℂ) (hU : ∀ i, star (U i) * U i = 1 ∧ U i * star (U i) = 1)
    (M : ι → ι → ((Fin 6 → ℂ) →+ (Fin 6 → ℂ))) :
    ∃ g : ι → AddAut (Fin 6 → ℂ),
      (∀ i v, g i v = (U i).mulVec v) ∧ (∀ i v, (g i).symm v = (star (U i)).mulVec v)
        ∧ ∀ c, linkF N (gaugeLink g M) (siteAct g c) = siteAct g (linkF N M c) := by
  refine ⟨fun i =>
    { toFun := fun v => (U i).mulVec v
      invFun := fun v => (star (U i)).mulVec v
      left_inv := fun v => by
        show (star (U i)).mulVec ((U i).mulVec v) = v
        rw [Matrix.mulVec_mulVec, (hU i).1, Matrix.one_mulVec]
      right_inv := fun v => by
        show (U i).mulVec ((star (U i)).mulVec v) = v
        rw [Matrix.mulVec_mulVec, (hU i).2, Matrix.one_mulVec]
      map_add' := fun _ _ => Matrix.mulVec_add _ _ _ },
    fun _ _ => rfl, fun _ _ => rfl, fun c => a6cov_all N M _ c⟩

/-- **`CX3-a` — A2, A3, A5 AND A4Exact-UNDER-HYPOTHESIS HOLD AT THE COMPLEX CARRIER.** The
packaging of Section A at `V = Fin 6 → ℂ` is the same construction as the packaged carrier of
`PK1`; the `PK3` proofs of A2, A3, A5 and A4Exact do not use finiteness of the alphabet, so they
transport unchanged.

**The translation-invariance hypothesis on the link coupling is part of the A4Exact conjunct and
is reported with it every time.** -/
theorem cx3a_complex_axioms (d L : ℕ)
    (M : (Fin d → ZMod L) → (Fin d → ZMod L) → ((Fin 6 → ℂ) →+ (Fin 6 → ℂ)))
    (hM : ∀ v i j, M (i + v) (j + v) = M i j) :
    (linkSubstratum (Fin d → ZMod L) (Fin 6 → ℂ) (nbrs d L) M
        (fun _ _ h => mem_nbrs_symm d L h)).A2
      ∧ (linkSubstratum (Fin d → ZMod L) (Fin 6 → ℂ) (nbrs d L) M
          (fun _ _ h => mem_nbrs_symm d L h)).A3 (2 * d)
      ∧ (linkSubstratum (Fin d → ZMod L) (Fin 6 → ℂ) (nbrs d L) M
          (fun _ _ h => mem_nbrs_symm d L h)).A5
      ∧ (linkSubstratum (Fin d → ZMod L) (Fin 6 → ℂ) (nbrs d L) M
          (fun _ _ h => mem_nbrs_symm d L h)).A4Exact :=
  ⟨linkSubstratum_A2 _ _ _, linkSubstratum_A3 _ d L M, linkSubstratum_A5 _ _ _,
    linkSubstratum_A4Exact _ d L M hM⟩

/-- **`CX3-b` — THE COMPLEX CARRIER IS NOT A SUBSTRATUM SATISFYING A1, AND THIS IS THE PROOF.**
`Substratum.A1` is `Finite (ι → V × V)` and `Fin 6 → ℂ` is infinite, so the configuration space of
the complex carrier is infinite: the constant families exhibit an injection from `ℂ`. **A proved
negative, computed in the kernel, not a failed proof search.**

**Bounded reading, frozen, and it is this round's most load-bearing distinction:** "bringing the
complex lift inside the interface" can mean two different things, and they come apart here. The
**covariance statement** comes inside (`CX1`, `CX2`). The **complex carrier does not come inside
as a substratum in the kernel's sense**, because finiteness is the first of the interface's axioms
and the complex carrier is infinite. That is **not a defect of the interface and not a defect of the
manuscripts**: the manuscripts' substratum is the finite object of `SM.md:306` and the complex
carrier is the object on which the derivation of `SM.md:114` and Theorem 5 is conducted. **`A1` is
not weakened**, no finiteness parameter is added, and no second substratum structure is
introduced. -/
theorem cx3b_complex_not_A1 (d L : ℕ)
    (M : (Fin d → ZMod L) → (Fin d → ZMod L) → ((Fin 6 → ℂ) →+ (Fin 6 → ℂ))) :
    ¬ (linkSubstratum (Fin d → ZMod L) (Fin 6 → ℂ) (nbrs d L) M
      (fun _ _ h => mem_nbrs_symm d L h)).A1 := by
  intro h
  have hfin : Finite ((Fin d → ZMod L) → (Fin 6 → ℂ) × (Fin 6 → ℂ)) := h
  have hinj : Function.Injective
      (fun z : ℂ => (fun _ => ((fun _ => z : Fin 6 → ℂ), (fun _ => z : Fin 6 → ℂ)) :
        (Fin d → ZMod L) → (Fin 6 → ℂ) × (Fin 6 → ℂ))) := by
    intro z w hzw
    exact congrFun (congrArg Prod.fst (congrFun hzw (fun _ => 0))) 0
  have := Finite.of_injective _ hinj
  exact not_finite ℂ

end CX

/-! ### Section E — `AS`: the assembled statement -/

/-- **`AS1` — THE COVARIANT FORM REACHES THE SECOND-ORDER DYNAMICS.** For a link-coupled rule, any
site-dependent `g`, and the phase-space map `leapEquiv`: the second-order map of the **transported**
rule is carried to the second-order map of the **original** by the pointwise action on both slots.
Stated once, polymorphically in the alphabet.

The proof shape is the merged `leap_siteAct`, with `a6cov_all` supplying the commutation instead of
a hypothesis; the second-order term `-φ(n, t-1)` passes because each `g i` is additive (`map_sub`).

**Bounded reading, frozen:** this is what makes the covariance a statement about **the dynamics**
of `SM.md:306`–`:308` rather than about the first-order half of it. It is still the identity
`a6cov_all` records, and it is still a statement whose content is the interface. -/
theorem as1_leap_covariant {ι V : Type} [DecidableEq ι] [AddCommGroup V]
    (N : ι → Finset ι) (M : ι → ι → (V →+ V)) (g : ι → AddAut V) (x : ι → V × V) :
    leapEquiv (linkF N (gaugeLink g M)) (fun i => (g i (x i).1, g i (x i).2))
      = fun i => (g i (leapEquiv (linkF N M) x i).1, g i (leapEquiv (linkF N M) x i).2) := by
  funext i
  have hc : curOf (fun i => (g i (x i).1, g i (x i).2)) = siteAct g (curOf x) := rfl
  simp only [leapEquiv_apply, leap_apply]
  rw [hc, a6cov_all N M g (curOf x), map_sub]
  rfl

/-- **`AS1` AT THE FINITE ALPHABET** `Fin 6 → ZMod q`, on the manuscripts' cubic torus and axis
neighbourhood. -/
theorem as1_finite (d L q : ℕ)
    (M : (Fin d → ZMod L) → (Fin d → ZMod L) → ((Fin 6 → ZMod q) →+ (Fin 6 → ZMod q)))
    (g : (Fin d → ZMod L) → AddAut (Fin 6 → ZMod q))
    (x : (Fin d → ZMod L) → (Fin 6 → ZMod q) × (Fin 6 → ZMod q)) :
    leapEquiv (linkF (nbrs d L) (gaugeLink g M)) (fun i => (g i (x i).1, g i (x i).2))
      = fun i => (g i (leapEquiv (linkF (nbrs d L) M) x i).1,
          g i (leapEquiv (linkF (nbrs d L) M) x i).2) :=
  as1_leap_covariant _ _ _ _

/-- **`AS1` AT THE COMPLEX ALPHABET** `Fin 6 → ℂ`, on the same torus and neighbourhood. Read with
`CX3-b`: the identity holds at this carrier, and this carrier is **not** a substratum satisfying
`A1`. -/
theorem as1_complex (d L : ℕ)
    (M : (Fin d → ZMod L) → (Fin d → ZMod L) → ((Fin 6 → ℂ) →+ (Fin 6 → ℂ)))
    (g : (Fin d → ZMod L) → AddAut (Fin 6 → ℂ))
    (x : (Fin d → ZMod L) → (Fin 6 → ℂ) × (Fin 6 → ℂ)) :
    leapEquiv (linkF (nbrs d L) (gaugeLink g M)) (fun i => (g i (x i).1, g i (x i).2))
      = fun i => (g i (leapEquiv (linkF (nbrs d L) M) x i).1,
          g i (leapEquiv (linkF (nbrs d L) M) x i).2) :=
  as1_leap_covariant _ _ _ _

end A6Instantiation
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.A6Instantiation.linkSubstratum_bridge
#print axioms OIBridge.A6Instantiation.linkSubstratum_A2
#print axioms OIBridge.A6Instantiation.linkSubstratum_A5
#print axioms OIBridge.A6Instantiation.linkSubstratum_A3
#print axioms OIBridge.A6Instantiation.nbrs_sub
#print axioms OIBridge.A6Instantiation.linkSubstratum_A4Exact
#print axioms OIBridge.A6Instantiation.pk1_packaging
#print axioms OIBridge.A6Instantiation.pk2a_bridge
#print axioms OIBridge.A6Instantiation.pk2b_covariance
#print axioms OIBridge.A6Instantiation.pk3a_A1
#print axioms OIBridge.A6Instantiation.pk3b_A2
#print axioms OIBridge.A6Instantiation.pk3c_A3
#print axioms OIBridge.A6Instantiation.pk3d_A4Exact
#print axioms OIBridge.A6Instantiation.pk3e_A5
#print axioms OIBridge.A6Instantiation.pk4_shift_not_scalar
#print axioms OIBridge.A6Instantiation.pk5_symmetric_point
#print axioms OIBridge.A6Instantiation.cx1_complex_covariance
#print axioms OIBridge.A6Instantiation.cx2_clinear_forgets
#print axioms OIBridge.A6Instantiation.cx2_manuscript_law
#print axioms OIBridge.A6Instantiation.cx2_unitary_gaugeLink
#print axioms OIBridge.A6Instantiation.cx3a_complex_axioms
#print axioms OIBridge.A6Instantiation.cx3b_complex_not_A1
#print axioms OIBridge.A6Instantiation.as1_leap_covariant
#print axioms OIBridge.A6Instantiation.as1_finite
#print axioms OIBridge.A6Instantiation.as1_complex
