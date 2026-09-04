import OIBridge.QuasilocalAlgebra

/-!
# The reversible second-order update as a depth-two local circuit

The substratum update of the framework is second order in time: a site's next value is a
function of its neighbours' current values minus its own previous value. Reversibility is what
forces the `- p` — the general second-order form carries a coefficient on the previous slice, and
only the value `-1` makes the phase-space map a bijection. This file takes that shape as given and
shows what it implies about the one-step map as an automorphism.

Writing the per-site state as the pair `(prev, cur)`, the phase-space map is

> `leap : (p, c) ↦ (c, F c - p)`

for an arbitrary `F` on configurations. The content of this section is that `leap` factors into
**two layers**,

> `leap = swap ∘ shear`,  `shear (p, c) = (F c - p, c)`,  `swap (p, c) = (c, p)`,

that **each layer is an involution**, and that each layer is a product of **commuting single-site
gates**. The shear gate at a site writes only that site's previous component and reads only the
current components, which is why the gates commute: no gate reads what another writes.

Nothing here assumes `F` is linear, or that the lattice is finite, or anything about the
neighbourhood structure. Finite range enters later, where it bounds how many gates can move a
given local observable; the algebra of this section is independent of it.

## Scope

This file is the combinatorial layer. It says the one-step map is a depth-two circuit of
commuting local involutions. It does **not** by itself construct a continuous-time flow; that
needs the operator layer, where each gate involution `g` gives a projection `(1 - g)/2` and a
one-parameter unitary. What is proved here is the input that construction consumes.
-/

namespace OIBridge.SecondOrderCircuit

open OIBridge.QuasilocalAlgebra

variable {ι : Type} [DecidableEq ι] {Q : Type} [AddCommGroup Q]

/-! ### Section A — the phase-space form -/

section Form

/-- The previous-slice component of a phase-space configuration. -/
def prevOf (x : ι → Q × Q) : ι → Q := fun i => (x i).1

/-- The current-slice component of a phase-space configuration. -/
def curOf (x : ι → Q × Q) : ι → Q := fun i => (x i).2

@[simp] theorem prevOf_apply (x : ι → Q × Q) (i : ι) : prevOf x i = (x i).1 := rfl

@[simp] theorem curOf_apply (x : ι → Q × Q) (i : ι) : curOf x i = (x i).2 := rfl

/-- **THE SHEAR LAYER**: write the previous slice using the current slice, leaving the current
slice fixed. -/
def shear (F : (ι → Q) → (ι → Q)) (x : ι → Q × Q) : ι → Q × Q :=
  fun i => (F (curOf x) i - (x i).1, (x i).2)

/-- **THE SWAP LAYER**: exchange the two components at each site. This is on-site — it is not a
lattice translation, and in particular is not a shift. -/
def swapLayer (x : ι → Q × Q) : ι → Q × Q := fun i => ((x i).2, (x i).1)

/-- **THE ONE-STEP MAP** of a reversible second-order update, in phase-space form. -/
def leap (F : (ι → Q) → (ι → Q)) (x : ι → Q × Q) : ι → Q × Q :=
  fun i => ((x i).2, F (curOf x) i - (x i).1)

@[simp] theorem shear_apply (F : (ι → Q) → (ι → Q)) (x : ι → Q × Q) (i : ι) :
    shear F x i = (F (curOf x) i - (x i).1, (x i).2) := rfl

@[simp] theorem swapLayer_apply (x : ι → Q × Q) (i : ι) :
    swapLayer x i = ((x i).2, (x i).1) := rfl

@[simp] theorem leap_apply (F : (ι → Q) → (ι → Q)) (x : ι → Q × Q) (i : ι) :
    leap F x i = ((x i).2, F (curOf x) i - (x i).1) := rfl

/-- The shear does not touch the current slice. This is the fact every commutation argument
below rests on. -/
@[simp] theorem curOf_shear (F : (ι → Q) → (ι → Q)) (x : ι → Q × Q) :
    curOf (shear F x) = curOf x := rfl

/-- **THE DEPTH-TWO FACTORIZATION**: the one-step map is the swap layer after the shear layer. -/
theorem leap_eq_swap_shear (F : (ι → Q) → (ι → Q)) (x : ι → Q × Q) :
    leap F x = swapLayer (shear F x) := rfl

/-- **THE SHEAR LAYER IS AN INVOLUTION.** -/
@[simp] theorem shear_shear (F : (ι → Q) → (ι → Q)) (x : ι → Q × Q) :
    shear F (shear F x) = x := by
  funext i
  simp only [shear_apply, curOf_shear]
  exact Prod.ext (by ring_nf; abel) rfl

/-- **THE SWAP LAYER IS AN INVOLUTION.** -/
@[simp] theorem swapLayer_swapLayer (x : ι → Q × Q) : swapLayer (swapLayer x) = x := rfl

/-- The shear layer as an equivalence. -/
def shearEquiv (F : (ι → Q) → (ι → Q)) : (ι → Q × Q) ≃ (ι → Q × Q) where
  toFun := shear F
  invFun := shear F
  left_inv := shear_shear F
  right_inv := shear_shear F

/-- The swap layer as an equivalence. -/
def swapEquiv : (ι → Q × Q) ≃ (ι → Q × Q) where
  toFun := swapLayer
  invFun := swapLayer
  left_inv := swapLayer_swapLayer
  right_inv := swapLayer_swapLayer

/-- **THE ONE-STEP MAP IS A BIJECTION**, exhibited as the composite of the two layers. This is
reversibility, obtained from the factorization rather than assumed. -/
def leapEquiv (F : (ι → Q) → (ι → Q)) : (ι → Q × Q) ≃ (ι → Q × Q) :=
  (shearEquiv F).trans swapEquiv

@[simp] theorem leapEquiv_apply (F : (ι → Q) → (ι → Q)) (x : ι → Q × Q) :
    leapEquiv F x = leap F x := rfl

/-- The inverse step is the two layers in the other order. -/
@[simp] theorem leapEquiv_symm_apply (F : (ι → Q) → (ι → Q)) (x : ι → Q × Q) :
    (leapEquiv F).symm x = shear F (swapLayer x) := rfl

theorem leap_leap_symm (F : (ι → Q) → (ι → Q)) (x : ι → Q × Q) :
    leap F (shear F (swapLayer x)) = x := (leapEquiv F).apply_symm_apply x

theorem leap_symm_leap (F : (ι → Q) → (ι → Q)) (x : ι → Q × Q) :
    shear F (swapLayer (leap F x)) = x := (leapEquiv F).symm_apply_apply x

end Form

/-! ### Section B — the layers as products of commuting single-site gates -/

section Gates

variable (F : (ι → Q) → (ι → Q))

/-- **THE SHEAR GATE AT A SITE**: write that one site's previous component, read only current
components. -/
def gate (i : ι) (x : ι → Q × Q) : ι → Q × Q :=
  Function.update x i (F (curOf x) i - (x i).1, (x i).2)

/-- **THE SWAP GATE AT A SITE**: exchange the two components at that site only. -/
def swapGate (i : ι) (x : ι → Q × Q) : ι → Q × Q :=
  Function.update x i ((x i).2, (x i).1)

variable {F}

@[simp] theorem gate_self (i : ι) (x : ι → Q × Q) :
    gate F i x i = (F (curOf x) i - (x i).1, (x i).2) := by
  simp [gate]

@[simp] theorem gate_of_ne {i j : ι} (h : j ≠ i) (x : ι → Q × Q) :
    gate F i x j = x j := by
  simp [gate, Function.update_of_ne h]

@[simp] theorem swapGate_self (i : ι) (x : ι → Q × Q) :
    swapGate i x i = ((x i).2, (x i).1) := by
  simp [swapGate]

@[simp] theorem swapGate_of_ne {i j : ι} (h : j ≠ i) (x : ι → Q × Q) :
    swapGate i x j = x j := by
  simp [swapGate, Function.update_of_ne h]

/-- **A GATE DOES NOT TOUCH THE CURRENT SLICE.** Every commutation fact below is a corollary. -/
@[simp] theorem curOf_gate (i : ι) (x : ι → Q × Q) : curOf (gate F i x) = curOf x := by
  funext j
  by_cases h : j = i
  · subst h; simp
  · simp [gate_of_ne h]

/-- **EACH SHEAR GATE IS AN INVOLUTION.** -/
@[simp] theorem gate_gate (i : ι) (x : ι → Q × Q) : gate F i (gate F i x) = x := by
  funext j
  by_cases h : j = i
  · subst h
    simp only [gate_self, curOf_gate]
    exact Prod.ext (by ring_nf; abel) rfl
  · simp [gate_of_ne h]

/-- **EACH SWAP GATE IS AN INVOLUTION.** -/
@[simp] theorem swapGate_swapGate (i : ι) (x : ι → Q × Q) :
    swapGate i (swapGate i x) = x := by
  funext j
  by_cases h : j = i
  · subst h; simp
  · simp [swapGate_of_ne h]

/-- **THE SHEAR GATES COMMUTE.** A gate writes only its own site's previous component and reads
only current components, which no gate writes. -/
theorem gate_comm (i j : ι) (x : ι → Q × Q) :
    gate F i (gate F j x) = gate F j (gate F i x) := by
  funext k
  by_cases hi : k = i
  · subst hi
    by_cases hj : k = j
    · subst hj; rfl
    · rw [gate_self, curOf_gate, gate_of_ne hj, gate_of_ne hj, gate_self]
  · by_cases hj : k = j
    · subst hj
      rw [gate_of_ne hi, gate_self, gate_self, curOf_gate, gate_of_ne hi]
    · rw [gate_of_ne hi, gate_of_ne hj, gate_of_ne hj, gate_of_ne hi]

/-- **THE SWAP GATES COMMUTE.** They act on disjoint sites. -/
theorem swapGate_comm (i j : ι) (x : ι → Q × Q) :
    swapGate i (swapGate j x) = swapGate j (swapGate i x) := by
  funext k
  by_cases hi : k = i
  · subst hi
    by_cases hj : k = j
    · subst hj; rfl
    · rw [swapGate_self, swapGate_of_ne hj, swapGate_of_ne hj, swapGate_self]
  · by_cases hj : k = j
    · subst hj
      rw [swapGate_of_ne hi, swapGate_self, swapGate_self, swapGate_of_ne hi]
    · rw [swapGate_of_ne hi, swapGate_of_ne hj, swapGate_of_ne hj, swapGate_of_ne hi]

/-- The shear restricted to a finite set of sites: the layer, applied only where told. -/
def shearOn (F : (ι → Q) → (ι → Q)) (s : Finset ι) (x : ι → Q × Q) : ι → Q × Q :=
  fun i => if i ∈ s then (F (curOf x) i - (x i).1, (x i).2) else x i

@[simp] theorem shearOn_of_mem {s : Finset ι} {i : ι} (h : i ∈ s) (x : ι → Q × Q) :
    shearOn F s x i = (F (curOf x) i - (x i).1, (x i).2) := by
  simp [shearOn, h]

@[simp] theorem shearOn_of_notMem {s : Finset ι} {i : ι} (h : i ∉ s) (x : ι → Q × Q) :
    shearOn F s x i = x i := by
  simp [shearOn, h]

@[simp] theorem curOf_shearOn (s : Finset ι) (x : ι → Q × Q) :
    curOf (shearOn F s x) = curOf x := by
  funext i
  by_cases h : i ∈ s <;> simp [h]

/-- **THE LAYER IS BUILT ONE GATE AT A TIME.** Adding a site to the covered region is applying
that site's gate. -/
theorem shearOn_insert {s : Finset ι} {i : ι} (hi : i ∉ s) (x : ι → Q × Q) :
    shearOn F (insert i s) x = gate F i (shearOn F s x) := by
  classical
  funext k
  by_cases hk : k = i
  · subst hk
    rw [shearOn_of_mem (Finset.mem_insert_self k s), gate_self, curOf_shearOn,
      shearOn_of_notMem hi]
  · rw [gate_of_ne hk]
    by_cases hks : k ∈ s
    · rw [shearOn_of_mem (Finset.mem_insert_of_mem hks), shearOn_of_mem hks]
    · have hnot : k ∉ insert i s := by
        simp only [Finset.mem_insert, not_or]
        exact ⟨hk, hks⟩
      rw [shearOn_of_notMem hnot, shearOn_of_notMem hks]

/-- The composite of the shear gates along a list of sites. Using a list rather than a fold over
a finite set keeps the order explicit; `gate_comm` is what makes the order immaterial. -/
def gateList (F : (ι → Q) → (ι → Q)) (l : List ι) (x : ι → Q × Q) : ι → Q × Q :=
  l.foldr (fun i y => gate F i y) x

@[simp] theorem gateList_nil (x : ι → Q × Q) : gateList F ([] : List ι) x = x := rfl

@[simp] theorem gateList_cons (i : ι) (l : List ι) (x : ι → Q × Q) :
    gateList F (i :: l) x = gate F i (gateList F l x) := rfl

/-- **THE SHEAR LAYER IS THE COMPOSITE OF ITS GATES**, over any list of distinct sites. The layer
is an infinite product only in the sense that the lattice is infinite; on every finite region it
is an honest finite composite, and that is all any local observable ever sees. -/
theorem gateList_eq_shearOn {l : List ι} (hl : l.Nodup) (x : ι → Q × Q) :
    gateList F l x = shearOn F l.toFinset x := by
  classical
  induction l with
  | nil => funext i; simp [shearOn]
  | cons i t ih =>
      have hi : i ∉ t.toFinset := by
        simpa using (List.nodup_cons.mp hl).1
      rw [gateList_cons, ih (List.nodup_cons.mp hl).2, List.toFinset_cons,
        ← shearOn_insert hi x]

/-- **THE COMPOSITE AGREES WITH THE FULL LAYER ON THE SITES IT COVERS.** Off the list it is the
identity, so a local observable supported there cannot tell the finite composite from the layer.
This is the mechanism by which an infinite layer acts locally. -/
theorem gateList_eq_shear_of_mem {l : List ι} (hl : l.Nodup) {i : ι} (h : i ∈ l)
    (x : ι → Q × Q) : gateList F l x i = shear F x i := by
  classical
  rw [gateList_eq_shearOn hl, shearOn_of_mem (List.mem_toFinset.mpr h), shear_apply]

theorem gateList_eq_self_of_notMem {l : List ι} (hl : l.Nodup) {i : ι} (h : i ∉ l)
    (x : ι → Q × Q) : gateList F l x i = x i := by
  classical
  rw [gateList_eq_shearOn hl, shearOn_of_notMem (fun hc => h (List.mem_toFinset.mp hc))]

/-- The partial layer is an involution, for every covered region. -/
@[simp] theorem shearOn_shearOn (s : Finset ι) (x : ι → Q × Q) :
    shearOn F s (shearOn F s x) = x := by
  classical
  funext k
  by_cases hk : k ∈ s
  · rw [shearOn_of_mem hk, curOf_shearOn, shearOn_of_mem hk]
    exact Prod.ext (by ring_nf; abel) rfl
  · rw [shearOn_of_notMem hk, shearOn_of_notMem hk]

end Gates

/-! ### Section C — the summary of the combinatorial layer -/

section Summary

variable {F : (ι → Q) → (ι → Q)}

/-- **THE DEPTH-TWO CIRCUIT THEOREM.** The one-step map of a reversible second-order update is
the composite of two layers, each an involution, each a product of commuting single-site gates
which are themselves involutions. The factorization holds for an arbitrary `F`: it uses
reversibility's `- p` and nothing else, so it is insensitive to linearity, to the alphabet, to
the neighbourhood structure, and to whether the coupling is state-dependent. -/
theorem depth_two_circuit (x : ι → Q × Q) (s : Finset ι) :
    leap F x = swapLayer (shear F x)
    ∧ shear F (shear F x) = x
    ∧ swapLayer (swapLayer x) = x
    ∧ shearOn F s (shearOn F s x) = x
    ∧ (∀ i, gate F i (gate F i x) = x)
    ∧ (∀ i, swapGate i (swapGate i x) = x)
    ∧ (∀ i j, gate F i (gate F j x) = gate F j (gate F i x))
    ∧ (∀ i j, swapGate i (swapGate j x) = swapGate j (swapGate i x)) :=
  ⟨leap_eq_swap_shear F x, shear_shear F x, swapLayer_swapLayer x, shearOn_shearOn s x,
    fun i => gate_gate i x, fun i => swapGate_swapGate i x, fun i j => gate_comm i j x,
    fun i j => swapGate_comm i j x⟩

end Summary


/-! ### Section D — the operator layer: an involution generates a one-parameter unitary

The combinatorial sections give, for each gate, an involution of configurations. Lifted to the
algebra, an involution becomes a self-adjoint unitary `g`, and `p = (1 - g)/2` is a projection.
That is the whole reason a continuous-time drive is available without any functional calculus:
the exponential of `t · π · p` is a **polynomial** in `p`,

> `u t = 1 + (exp (π i t) - 1) • p`,

because `p² = p` collapses the series. The three facts that matter — `u 0 = 1`, `u 1 = g`, and
the one-parameter group law — are then algebra, and the generator `π p` is bounded and supported
wherever `g` is.

This section is stated for an arbitrary star algebra over `ℂ`, so it applies verbatim to a gate
sitting inside a finite region's matrix algebra, to the local algebra, and to the quasilocal
completion.
-/

section Operator

variable {A : Type*} [Ring A] [Algebra ℂ A] [StarRing A] [StarModule ℂ A]

/-- The projection attached to a self-adjoint unitary: `p = (1 - g)/2`. -/
noncomputable def proj (g : A) : A := (2 : ℂ)⁻¹ • (1 - g)

/-- The one-parameter unitary generated by `π p`. Written as a polynomial in the projection,
which is exact because `p² = p`. -/
noncomputable def unit (g : A) (t : ℝ) : A :=
  1 + (Complex.exp (Real.pi * Complex.I * t) - 1) • proj g

variable {g : A}

theorem proj_mul_proj (hg : g * g = 1) : proj g * proj g = proj g := by
  have e : (1 - g) * (1 - g) = (2 : ℂ) • (1 - g) := by
    have e1 : (1 - g) * (1 - g) = 1 - g - g + g * g := by noncomm_ring
    rw [e1, hg, two_smul]
    abel
  simp only [proj, smul_mul_smul_comm, e, smul_smul]
  norm_num

theorem star_proj (hs : star g = g) : star (proj g) = proj g := by
  simp only [proj, star_smul, star_sub, star_one, hs]
  norm_num

@[simp] theorem unit_zero (g : A) : unit g 0 = 1 := by
  simp [unit]

/-- **AT TIME ONE THE FLOW ARRIVES AT THE GATE.** -/
theorem unit_one (hg : g * g = 1) : unit g 1 = g := by
  have hpi : Complex.exp ((Real.pi : ℂ) * Complex.I * ((1 : ℝ) : ℂ)) = -1 := by
    rw [Complex.ofReal_one, mul_one, Complex.exp_pi_mul_I]
  simp only [unit, hpi, proj, smul_smul]
  norm_num

theorem exp_pi_I_neg (t : ℝ) :
    Complex.exp ((Real.pi : ℂ) * Complex.I * ((-t : ℝ) : ℂ))
      = (starRingEnd ℂ) (Complex.exp ((Real.pi : ℂ) * Complex.I * (t : ℂ))) := by
  rw [← Complex.exp_conj]
  congr 1
  simp [Complex.ext_iff]

/-- **THE ONE-PARAMETER GROUP LAW.** The gates' unitaries compose by adding times: this is where
`p * p = p` does the work that a functional calculus would otherwise have to do. -/
theorem unit_mul_unit (hg : g * g = 1) (t s : ℝ) :
    unit g t * unit g s = unit g (t + s) := by
  have hp := proj_mul_proj hg
  have expand : ∀ u v : ℂ, (1 + u • proj g) * (1 + v • proj g)
      = 1 + (u + v + u * v) • proj g := by
    intro u v
    have e : (1 + u • proj g) * (1 + v • proj g)
        = 1 + v • proj g + u • proj g + (u * v) • (proj g * proj g) := by
      simp only [add_mul, mul_add, one_mul, mul_one, smul_mul_assoc, mul_smul_comm]
      module
    rw [e, hp]
    module
  have hexp : Complex.exp ((Real.pi : ℂ) * Complex.I * (((t + s : ℝ)) : ℂ))
      = Complex.exp ((Real.pi : ℂ) * Complex.I * (t : ℂ))
        * Complex.exp ((Real.pi : ℂ) * Complex.I * (s : ℂ)) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  simp only [unit]
  rw [expand, hexp]
  congr 2
  ring

/-- The adjoint of the unitary is its reverse-time value. -/
theorem star_unit (hs : star g = g) (t : ℝ) :
    star (unit g t) = unit g (-t) := by
  simp only [unit, star_add, star_one, star_smul, star_sub, star_proj hs, exp_pi_I_neg t,
    Complex.star_def]

/-- **THE UNITARY IS UNITARY.** -/
theorem star_unit_mul_unit (hg : g * g = 1) (hs : star g = g) (t : ℝ) :
    star (unit g t) * unit g t = 1 := by
  rw [star_unit hs, unit_mul_unit hg, neg_add_cancel, unit_zero]

theorem unit_mul_star_unit (hg : g * g = 1) (hs : star g = g) (t : ℝ) :
    unit g t * star (unit g t) = 1 := by
  rw [star_unit hs, unit_mul_unit hg, add_neg_cancel, unit_zero]

/-- **THE GATE FLOW**: conjugation by the one-parameter unitary. -/
noncomputable def flow (g : A) (t : ℝ) (a : A) : A := unit g t * a * star (unit g t)

@[simp] theorem flow_zero (g : A) (a : A) : flow g 0 a = a := by
  simp [flow]

/-- **AT TIME ONE THE FLOW IS THE GATE'S ACTION.** -/
theorem flow_one (hg : g * g = 1) (hs : star g = g) (a : A) :
    flow g 1 a = g * a * g := by
  rw [flow, unit_one hg, hs]

theorem flow_add (hg : g * g = 1) (hs : star g = g) (t s : ℝ) (a : A) :
    flow g (t + s) a = flow g t (flow g s a) := by
  simp only [flow, star_unit hs]
  rw [← unit_mul_unit hg t s, show -(t + s) = -s + -t by ring, ← unit_mul_unit hg (-s) (-t)]
  simp only [mul_assoc]

theorem flow_mul (g : A) (hg : g * g = 1) (hs : star g = g) (t : ℝ) (a b : A) :
    flow g t (a * b) = flow g t a * flow g t b := by
  simp only [flow, mul_assoc]
  congr 2
  rw [← mul_assoc, star_unit_mul_unit hg hs, one_mul]

theorem flow_one_eq_one (hg : g * g = 1) (hs : star g = g) (t : ℝ) :
    flow g t (1 : A) = 1 := by
  rw [flow, mul_one, unit_mul_star_unit hg hs]

theorem flow_star (t : ℝ) (a : A) :
    flow g t (star a) = star (flow g t a) := by
  simp only [flow, star_mul, star_star, mul_assoc]

theorem flow_add_map (g : A) (t : ℝ) (a b : A) :
    flow g t (a + b) = flow g t a + flow g t b := by
  simp only [flow, mul_add, add_mul]

/-- **THE DRIVE OF ONE GATE.** A gate involution is reached at time one by a one-parameter group
of `*`-automorphisms generated by the bounded element `π p`, `p` the gate's projection. Existence
and the group law are exact, not asymptotic. -/
theorem gate_drive (hg : g * g = 1) (hs : star g = g) :
    flow g 0 = id
    ∧ (∀ a : A, flow g 1 a = g * a * g)
    ∧ (∀ t s : ℝ, ∀ a : A, flow g (t + s) a = flow g t (flow g s a))
    ∧ (∀ t : ℝ, ∀ a b : A, flow g t (a * b) = flow g t a * flow g t b)
    ∧ (∀ t : ℝ, ∀ a b : A, flow g t (a + b) = flow g t a + flow g t b)
    ∧ (∀ t : ℝ, ∀ a : A, flow g t (star a) = star (flow g t a))
    ∧ (∀ t : ℝ, flow g t (1 : A) = 1) :=
  ⟨funext fun a => flow_zero g a, fun a => flow_one hg hs a,
    fun t s a => flow_add hg hs t s a, fun t a b => flow_mul g hg hs t a b,
    fun t a b => flow_add_map g t a b, fun t a => flow_star t a,
    fun t => flow_one_eq_one hg hs t⟩


/-! #### Commuting families: the layer drive

A layer is a product of gates that commute. Their unitaries then commute at all times, so the
composite of the individual flows is again a one-parameter group, and at time one it is
conjugation by the product. Only finitely many gates of a layer move a given local observable —
that is Section B — so this finite statement is what an infinite layer amounts to locally.
-/

theorem proj_comm {g h : A} (hgh : g * h = h * g) : proj g * proj h = proj h * proj g := by
  simp only [proj, smul_mul_smul_comm, sub_mul, mul_sub, one_mul, mul_one, hgh]
  congr 1
  abel

theorem unit_comm {g h : A} (hgh : g * h = h * g) (t s : ℝ) :
    unit g t * unit h s = unit h s * unit g t := by
  have hp := proj_comm hgh
  simp only [unit, add_mul, mul_add, one_mul, mul_one, smul_mul_assoc, mul_smul_comm, smul_smul,
    hp]
  module

/-- The composite of the flows of a list of gates. -/
noncomputable def flowList (l : List A) (t : ℝ) (a : A) : A :=
  l.foldr (fun g b => flow g t b) a

@[simp] theorem flowList_nil (t : ℝ) (a : A) : flowList ([] : List A) t a = a := rfl

@[simp] theorem flowList_cons (g : A) (l : List A) (t : ℝ) (a : A) :
    flowList (g :: l) t a = flow g t (flowList l t a) := rfl

@[simp] theorem flowList_zero (l : List A) (a : A) : flowList l 0 a = a := by
  induction l with
  | nil => rfl
  | cons g t ih => rw [flowList_cons, ih, flow_zero]

/-- A predicate packaging what a layer's gates are: self-adjoint unitaries that commute. -/
structure IsGateList (l : List A) : Prop where
  unitary : ∀ g ∈ l, g * g = 1
  selfAdj : ∀ g ∈ l, star g = g
  comm : ∀ g ∈ l, ∀ h ∈ l, g * h = h * g

theorem IsGateList.tail {g : A} {l : List A} (h : IsGateList (g :: l)) : IsGateList l :=
  ⟨fun x hx => h.unitary x (List.mem_cons_of_mem _ hx),
   fun x hx => h.selfAdj x (List.mem_cons_of_mem _ hx),
   fun x hx y hy => h.comm x (List.mem_cons_of_mem _ hx) y (List.mem_cons_of_mem _ hy)⟩

/-- An element commuting with every entry of a list commutes with the product. -/
theorem mul_prod_comm {g : A} {l : List A} (h : ∀ x ∈ l, g * x = x * g) :
    g * l.prod = l.prod * g := by
  induction l with
  | nil => simp
  | cons x r ih =>
      rw [List.prod_cons, ← mul_assoc, h x (List.mem_cons_self ..), mul_assoc,
        ih fun y hy => h y (List.mem_cons_of_mem _ hy), ← mul_assoc]

/-- A commuting gate list has a self-adjoint unitary product. -/
theorem isGateList_prod {l : List A} (h : IsGateList l) :
    l.prod * l.prod = 1 ∧ star l.prod = l.prod := by
  induction l with
  | nil => simp
  | cons g t ih =>
      obtain ⟨hu, hs⟩ := ih h.tail
      have hgt : g * t.prod = t.prod * g :=
        mul_prod_comm fun x hx =>
          h.comm g (List.mem_cons_self ..) x (List.mem_cons_of_mem _ hx)
      refine ⟨?_, ?_⟩
      · rw [List.prod_cons]
        calc g * t.prod * (g * t.prod) = g * (t.prod * g) * t.prod := by simp only [mul_assoc]
          _ = g * (g * t.prod) * t.prod := by rw [hgt]
          _ = g * g * (t.prod * t.prod) := by simp only [mul_assoc]
          _ = 1 := by rw [h.unitary g (List.mem_cons_self ..), hu, one_mul]
      · rw [List.prod_cons, star_mul, hs, h.selfAdj g (List.mem_cons_self ..), hgt]

/-- **AT TIME ONE THE LAYER DRIVE IS THE LAYER.** -/
theorem flowList_one {l : List A} (h : IsGateList l) (a : A) :
    flowList l 1 a = l.prod * a * l.prod := by
  induction l with
  | nil => simp
  | cons g t ih =>
      have hgt : g * t.prod = t.prod * g :=
        mul_prod_comm fun x hx =>
          h.comm g (List.mem_cons_self ..) x (List.mem_cons_of_mem _ hx)
      rw [flowList_cons, ih h.tail,
        flow_one (h.unitary g (List.mem_cons_self ..)) (h.selfAdj g (List.mem_cons_self ..)),
        List.prod_cons]
      calc g * (t.prod * a * t.prod) * g
          = g * t.prod * a * (t.prod * g) := by simp only [mul_assoc]
        _ = g * t.prod * a * (g * t.prod) := by rw [hgt]

/-- The individual gate flows commute, so the composite is order-independent in time. -/
theorem flow_flow_comm {g h : A} (hgs : star g = g) (hhs : star h = h)
    (hgh : g * h = h * g) (t s : ℝ) (a : A) :
    flow g t (flow h s a) = flow h s (flow g t a) := by
  have hst : star (unit g t) * star (unit h s) = star (unit h s) * star (unit g t) := by
    rw [star_unit hgs, star_unit hhs, unit_comm hgh]
  simp only [flow]
  calc unit g t * (unit h s * a * star (unit h s)) * star (unit g t)
      = unit g t * unit h s * a * (star (unit h s) * star (unit g t)) := by
        simp only [mul_assoc]
    _ = unit h s * unit g t * a * (star (unit g t) * star (unit h s)) := by
        rw [unit_comm hgh, hst]
    _ = unit h s * (unit g t * a * star (unit g t)) * star (unit h s) := by
        simp only [mul_assoc]

/-- A gate's flow commutes with the flow of a list of gates it commutes with. -/
theorem flowList_flow_comm {g : A} {l : List A} (hgs : star g = g)
    (hls : ∀ x ∈ l, star x = x) (hcomm : ∀ x ∈ l, g * x = x * g) (tg ts : ℝ) (b : A) :
    flowList l ts (flow g tg b) = flow g tg (flowList l ts b) := by
  induction l with
  | nil => rfl
  | cons x u ihu =>
      rw [flowList_cons,
        ihu (fun y hy => hls y (List.mem_cons_of_mem _ hy))
          (fun y hy => hcomm y (List.mem_cons_of_mem _ hy)),
        flowList_cons,
        flow_flow_comm (hls x (List.mem_cons_self ..)) hgs
          (hcomm x (List.mem_cons_self ..)).symm ts tg]

/-- **THE LAYER DRIVE IS A ONE-PARAMETER GROUP.** -/
theorem flowList_add {l : List A} (h : IsGateList l) (t s : ℝ) (a : A) :
    flowList l (t + s) a = flowList l t (flowList l s a) := by
  induction l with
  | nil => simp
  | cons g r ih =>
      have hg := h.unitary g (List.mem_cons_self ..)
      have hgs := h.selfAdj g (List.mem_cons_self ..)
      rw [flowList_cons, flowList_cons, flowList_cons, ih h.tail, flow_add hg hgs t s,
        flowList_flow_comm hgs (fun x hx => h.selfAdj x (List.mem_cons_of_mem _ hx))
          (fun x hx => h.comm g (List.mem_cons_self ..) x (List.mem_cons_of_mem _ hx))
          s t (flowList r s a)]

/-- **THE LAYER DRIVE.** A layer of commuting gate involutions is reached at time one by a
one-parameter group of `*`-automorphisms whose generator is the sum of the gates' bounded local
terms. Existence, the group law, and arrival at the layer are exact. -/
theorem layer_drive {l : List A} (h : IsGateList l) :
    (∀ a : A, flowList l 0 a = a)
    ∧ (∀ a : A, flowList l 1 a = l.prod * a * l.prod)
    ∧ (∀ t s : ℝ, ∀ a : A, flowList l (t + s) a = flowList l t (flowList l s a))
    ∧ l.prod * l.prod = 1
    ∧ star l.prod = l.prod :=
  ⟨fun a => flowList_zero l a, fun a => flowList_one h a, fun t s a => flowList_add h t s a,
    (isGateList_prod h).1, (isGateList_prod h).2⟩


/-! #### The two-layer drive

The one-step map is two layers. The drive runs the first layer's group on `[0,1]` and the
second's on `[1,2]`, which is a piecewise-constant time-dependent generator: bounded, finite
range, and equal to a fixed local sum on each interval. At the junction the two pieces agree,
and at the end the drive is conjugation by the product of the two layers — the one-step map.
-/

/-- The two-piece drive: the first layer's group, then the second's. -/
noncomputable def drive (lS lW : List A) (t : ℝ) (a : A) : A :=
  if t ≤ 1 then flowList lS t a else flowList lW (t - 1) (flowList lS 1 a)

@[simp] theorem drive_zero (lS lW : List A) (a : A) : drive lS lW 0 a = a := by
  simp [drive]

theorem drive_of_le_one {lS lW : List A} {t : ℝ} (ht : t ≤ 1) (a : A) :
    drive lS lW t a = flowList lS t a := by
  simp [drive, ht]

theorem drive_of_one_le {lS lW : List A} {t : ℝ} (ht : 1 ≤ t) (a : A) :
    drive lS lW t a = flowList lW (t - 1) (flowList lS 1 a) := by
  rcases eq_or_lt_of_le ht with rfl | hlt
  · simp [drive]
  · rw [drive, if_neg (not_le.mpr hlt)]

/-- **THE PIECES AGREE AT THE JUNCTION.** The drive is a single path, not two unrelated ones. -/
theorem drive_one (lS lW : List A) (a : A) :
    drive lS lW 1 a = flowList lS 1 a := by
  simp [drive]

/-- **THE DRIVE ARRIVES AT THE ONE-STEP MAP.** -/
theorem drive_two {lS lW : List A} (hS : IsGateList lS) (hW : IsGateList lW) (a : A) :
    drive lS lW 2 a = lW.prod * lS.prod * a * (lS.prod * lW.prod) := by
  rw [drive_of_one_le (by norm_num) a, show (2 : ℝ) - 1 = 1 by norm_num,
    flowList_one hS a, flowList_one hW]
  simp only [mul_assoc]

/-- **THE CONTINUOUS-TIME DRIVE OF A DEPTH-TWO CIRCUIT.** A one-step map that factors into two
layers of commuting gate involutions is reached exactly, at finite time, by a drive whose
generator on each interval is a sum of the layer's bounded local terms. The endpoint is
conjugation by a self-adjoint unitary, so the drive is by `*`-automorphisms throughout.

Existence, locality of the generator, and arrival are exact. What is **not** claimed is a single
time-independent generator: the drive here is piecewise constant in time, and nothing below
asserts that the two pieces can be replaced by one. -/
theorem two_layer_drive {lS lW : List A} (hS : IsGateList lS) (hW : IsGateList lW) :
    (∀ a : A, drive lS lW 0 a = a)
    ∧ (∀ a : A, drive lS lW 1 a = flowList lS 1 a)
    ∧ (∀ a : A, drive lS lW 2 a = lW.prod * lS.prod * a * (lS.prod * lW.prod))
    ∧ star (lW.prod * lS.prod) = lS.prod * lW.prod
    ∧ lW.prod * lS.prod * (lS.prod * lW.prod) = 1
    ∧ (∀ t s : ℝ, ∀ a : A, flowList lS (t + s) a = flowList lS t (flowList lS s a))
    ∧ (∀ t s : ℝ, ∀ a : A, flowList lW (t + s) a = flowList lW t (flowList lW s a)) := by
  obtain ⟨hSu, hSs⟩ := isGateList_prod hS
  obtain ⟨hWu, hWs⟩ := isGateList_prod hW
  refine ⟨fun a => drive_zero lS lW a, fun a => drive_one lS lW a,
    fun a => drive_two hS hW a, ?_, ?_, fun t s a => flowList_add hS t s a,
    fun t s a => flowList_add hW t s a⟩
  · rw [star_mul, hSs, hWs]
  · calc lW.prod * lS.prod * (lS.prod * lW.prod)
        = lW.prod * (lS.prod * lS.prod) * lW.prod := by simp only [mul_assoc]
      _ = 1 := by rw [hSu, mul_one, hWu]

end Operator



/-! ### Section E — the drive on the quasilocal algebra

The abstract sections apply to any star algebra over `ℂ`. This section supplies the gates as
elements of the **quasilocal algebra of the infinite lattice**: an involutive permutation of a
finite region's configurations gives a permutation matrix, which is a self-adjoint unitary, and
`stage` carries it into the completion. The resulting generator `π · proj g` lies in the image of
the same finite region's stage, so it is strictly local — bounded, and supported where the gate is.

This is what makes the drive an infinite-volume statement rather than a finite-lattice one: the
algebra is the quasilocal completion, and each generator is a finite-region element of it.
-/

section Localized

open OIBridge.QuasilocalAlgebra OIBridge.RegionTower Matrix

/-- The permutation matrix of a bijection of a finite set. -/
def permMat {α : Type*} [Fintype α] [DecidableEq α] (σ : α ≃ α) : Matrix α α ℂ :=
  fun x y => if σ y = x then 1 else 0

section Perm

variable {α : Type*} [Fintype α] [DecidableEq α]

theorem permMat_apply (σ : α ≃ α) (x y : α) :
    permMat σ x y = if σ y = x then 1 else 0 := rfl

theorem permMat_refl : permMat (Equiv.refl α) = (1 : Matrix α α ℂ) := by
  funext x y
  simp only [permMat_apply, Equiv.refl_apply, Matrix.one_apply]
  by_cases h : y = x
  · simp [h]
  · have h' : ¬ x = y := fun hc => h hc.symm
    simp [h, h']

theorem permMat_mul (σ τ : α ≃ α) :
    permMat σ * permMat τ = permMat (τ.trans σ) := by
  funext x z
  simp only [Matrix.mul_apply, permMat_apply, Equiv.trans_apply]
  rw [Finset.sum_eq_single (τ z)]
  · have : (if τ z = τ z then (1 : ℂ) else 0) = 1 := if_pos rfl
    rw [this, mul_one]
    rfl
  · intro y _ hy
    rw [show (if τ z = y then (1 : ℂ) else 0) = 0 from if_neg (Ne.symm hy), mul_zero]
  · intro h
    exact absurd (Finset.mem_univ (τ z)) h

theorem permMat_conjTranspose (σ : α ≃ α) :
    (permMat σ).conjTranspose = permMat σ.symm := by
  funext x y
  simp only [Matrix.conjTranspose_apply, permMat_apply, Equiv.symm_apply_eq]
  by_cases h : σ x = y
  · rw [if_pos h, if_pos h.symm, star_one]
  · rw [if_neg h, if_neg fun hc => h hc.symm, star_zero]

/-- A permutation matrix of an involution is a self-adjoint unitary. -/
theorem permMat_involutive {σ : α ≃ α} (hσ : ∀ x, σ (σ x) = x) :
    permMat σ * permMat σ = 1 ∧ (permMat σ).conjTranspose = permMat σ := by
  have hsymm : σ.symm = σ := Equiv.ext fun x => by
    rw [Equiv.symm_apply_eq]; exact (hσ x).symm
  refine ⟨?_, by rw [permMat_conjTranspose, hsymm]⟩
  rw [permMat_mul, ← permMat_refl]
  congr 1
  exact Equiv.ext fun x => hσ x

end Perm

section Quasi

variable {J : Type} [DecidableEq J] {R : Type} [Fintype R] [DecidableEq R] [Nonempty R]

/-- **A LOCAL GATE IN THE QUASILOCAL ALGEBRA.** An involutive permutation of a finite region's
configurations, carried into the completion by that region's stage. -/
noncomputable def localGate (Λ : Finset J) (σ : Conf Λ R ≃ Conf Λ R) : Quasilocal J R :=
  stage Λ (permMat σ)

/-- **THE LOCAL GATE IS A SELF-ADJOINT UNITARY** of the quasilocal algebra. -/
theorem localGate_isGate {Λ : Finset J} {σ : Conf Λ R ≃ Conf Λ R} (hσ : ∀ x, σ (σ x) = x) :
    localGate Λ σ * localGate Λ σ = 1 ∧ star (localGate Λ σ) = localGate Λ σ := by
  obtain ⟨hu, hs⟩ := permMat_involutive hσ
  refine ⟨?_, ?_⟩
  · rw [localGate, ← map_mul, hu, map_one]
  · rw [localGate, ← map_star, Matrix.star_eq_conjTranspose, hs]

/-- **THE GENERATOR IS STRICTLY LOCAL.** The bounded element whose flow reaches the gate lies in
the image of the very region the gate acts on: it is a finite-region element of the infinite
quasilocal algebra, not a formal infinite sum. -/
theorem proj_localGate_mem_stage (Λ : Finset J) (σ : Conf Λ R ≃ Conf Λ R) :
    proj (localGate Λ σ) = stage Λ ((2 : ℂ)⁻¹ • (1 - permMat σ)) := by
  rw [proj, localGate, map_smul, map_sub, map_one]

/-- **THE UNITARY IS SUPPORTED IN THE SAME REGION**, at every time. -/
theorem unit_localGate_mem_stage (Λ : Finset J) (σ : Conf Λ R ≃ Conf Λ R) (t : ℝ) :
    unit (localGate Λ σ) t
      = stage Λ (1 + (Complex.exp ((Real.pi : ℂ) * Complex.I * (t : ℂ)) - 1)
          • ((2 : ℂ)⁻¹ • (1 - permMat σ))) := by
  rw [map_add, map_one, map_smul, ← proj_localGate_mem_stage, unit]

/-- **THE QUASILOCAL DRIVE THEOREM.** On the quasilocal algebra of the infinite lattice, a layer
of commuting local gate involutions is reached exactly at finite time by a one-parameter group of
`*`-automorphisms whose generator is a sum of bounded elements, each supported in the finite
region of its gate. Composing two such layers over two intervals reaches the composite — which,
by the depth-two factorization, is the one-step map of a reversible second-order update.

Existence, locality, and arrival are exact. A **single time-independent** generator is not
claimed: the drive is piecewise constant across the two layers. -/
theorem quasilocal_drive {lS lW : List (Quasilocal J R)}
    (hS : IsGateList lS) (hW : IsGateList lW) :
    (∀ a, drive lS lW 0 a = a)
    ∧ (∀ a, drive lS lW 1 a = flowList lS 1 a)
    ∧ (∀ a, drive lS lW 2 a = lW.prod * lS.prod * a * (lS.prod * lW.prod))
    ∧ star (lW.prod * lS.prod) = lS.prod * lW.prod
    ∧ lW.prod * lS.prod * (lS.prod * lW.prod) = 1
    ∧ (∀ t s : ℝ, ∀ a, flowList lS (t + s) a = flowList lS t (flowList lS s a))
    ∧ (∀ t s : ℝ, ∀ a, flowList lW (t + s) a = flowList lW t (flowList lW s a)) :=
  two_layer_drive hS hW

end Quasi

end Localized

#print axioms shear_shear
#print axioms swapLayer_swapLayer
#print axioms leap_eq_swap_shear
#print axioms leapEquiv
#print axioms leap_leap_symm
#print axioms leap_symm_leap
#print axioms curOf_shear
#print axioms curOf_gate
#print axioms gate_gate
#print axioms swapGate_swapGate
#print axioms gate_comm
#print axioms swapGate_comm
#print axioms shearOn_insert
#print axioms gateList_eq_shearOn
#print axioms gateList_eq_shear_of_mem
#print axioms gateList_eq_self_of_notMem
#print axioms shearOn_shearOn
#print axioms depth_two_circuit
#print axioms proj_mul_proj
#print axioms star_proj
#print axioms unit_zero
#print axioms unit_one
#print axioms unit_mul_unit
#print axioms star_unit
#print axioms star_unit_mul_unit
#print axioms unit_mul_star_unit
#print axioms flow_zero
#print axioms flow_one
#print axioms flow_add
#print axioms flow_mul
#print axioms flow_star
#print axioms flow_one_eq_one
#print axioms gate_drive
#print axioms proj_comm
#print axioms unit_comm
#print axioms mul_prod_comm
#print axioms isGateList_prod
#print axioms flowList_zero
#print axioms flowList_one
#print axioms flow_flow_comm
#print axioms flowList_flow_comm
#print axioms flowList_add
#print axioms layer_drive
#print axioms drive_zero
#print axioms drive_one
#print axioms drive_two
#print axioms two_layer_drive
#print axioms permMat_refl
#print axioms permMat_mul
#print axioms permMat_conjTranspose
#print axioms permMat_involutive
#print axioms localGate_isGate
#print axioms proj_localGate_mem_stage
#print axioms unit_localGate_mem_stage
#print axioms quasilocal_drive

end OIBridge.SecondOrderCircuit
