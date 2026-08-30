/-
  OIBridge/StinespringUniqueness.lean — [Structure] Proposition 9.7b.

      two MINIMAL pure-reference dilations of the same channel
        ⟹ equal environment dimension, and a unique unitary W with V₂ = (1 ⊗ W) V₁.

  AND NO FURTHER. The conclusion is about the ISOMETRY. The dilating unitary is not determined off
  the prepared reference subspace, and `stinespring_scope_probe.py`'s CNOT pair is the permanent
  record of that: `CNOT` and `CNOT·(1 ⊗ Z)` realize the same channel on the same environment, both
  minimally, and minimality forces `W = 1`, so the two unitaries cannot be conjugate. The former
  Proposition 9.7 asserted exactly that conjugation, and was false.

  THREE GATES, not one reassembly.

  1. MINIMALITY IS KRAUS INDEPENDENCE, in the manuscript's own form. `Minimal` is the cyclicity
     condition `span {(M ⊗ 1) V ψ} = H_V ⊗ H_H` with `M` ranging over ALL of `B(H_V)` — not a
     dimension count, and not the independence it is being proved equivalent to.
     `minimal_iff_linearIndependent` is the only real work in the file.
  2. THE STINESPRING CHANNEL IS THE KRAUS MAP of `krausOf V`, entrywise, so that
     `KrausUniqueness` can consume it. The channel is defined as what it is — conjugate by `V`,
     sum over the environment index — rather than as a Kraus sum in disguise.
  3. THE ORIENTATION. `FactorUniqueness` produces the COLUMN factor `H_H^(2) → H_H^(1)`; the
     environment unitary in `V₂ = (1 ⊗ W) V₁` runs the other way. `hiddenUnitary` is the adjoint
     of the factor, and `V2_eq_hiddenUnitary_V1` is stated in that direction, so the arrow cannot
     silently reverse — the same discipline `KrausUniqueness.krausMatrix_eq_transpose` applies to
     the index order.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.KrausUniqueness

namespace OIBridge

namespace StinespringUniqueness

set_option autoImplicit false

/- The statements below use different parts of the section's typeclass assumptions; they are kept
under shared variables because they exist to serve `proposition_9_7b`, which uses all of them. -/
set_option linter.unusedSectionVars false

open LinearMap Matrix Finset KrausUniqueness

variable {n e f : Type*} [Fintype n] [DecidableEq n]
  [Fintype e] [DecidableEq e] [Fintype f] [DecidableEq f]

local notation "⟪" x ", " y "⟫" => inner ℂ x y

/-! ### The dilation, its matrix, and its Kraus family

`H_V ⊗ H_H` is `EuclideanSpace ℂ (n × e)`, the same coordinate idiom `KrausUniqueness` uses for
matrices. A dilation is a linear map `V : H_V → H_V ⊗ H_H`; isometry is not needed for any
statement here and so is not assumed. -/

/-- The matrix of a dilation: column `b` is `V e_b`. -/
noncomputable def vmat (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e)) : Matrix (n × e) n ℂ :=
  fun p b => V (EuclideanSpace.single b 1) p

/-- **The Kraus family a dilation carries**, `A_i (a, b) = V(a, i ; b)` — that is,
`A_i = (1 ⊗ ⟨i|) V`. -/
noncomputable def krausOf (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e)) : e → Matrix n n ℂ :=
  fun i a b => vmat V (a, i) b

/-- Every vector of `EuclideanSpace` is its own basis expansion. -/
theorem sum_single (w : EuclideanSpace ℂ n) :
    ∑ b, w b • (EuclideanSpace.single b 1 : EuclideanSpace ℂ n) = w := by
  refine (WithLp.ext_iff 2).2 (funext fun a => ?_)
  rw [WithLp.ofLp_sum]
  simp [Pi.single_apply, mul_ite, Finset.sum_ite_eq]

/-- Any map out of `EuclideanSpace`, in coordinates. -/
theorem apply_eq' {m : Type*} [Fintype m] [DecidableEq m]
    (T : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ m) (ψ : EuclideanSpace ℂ n) (q : m) :
    T ψ q = ∑ b, ψ b * T (EuclideanSpace.single b 1) q := by
  conv_lhs => rw [← sum_single ψ]
  rw [map_sum, WithLp.ofLp_sum, Finset.sum_apply]
  simp

/-- A dilation applied to a vector, in coordinates. -/
theorem apply_eq (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e))
    (ψ : EuclideanSpace ℂ n) (p : n × e) : V ψ p = ∑ b, ψ b * vmat V p b := by
  conv_lhs => rw [← sum_single ψ]
  rw [map_sum, WithLp.ofLp_sum, Finset.sum_apply]
  simp [vmat]

/-! ### Gate 2: the Stinespring channel is a Kraus map

The channel is written as what it is — conjugate by `V`, then sum over the environment index — and
proved equal to `KrausUniqueness.krausMap` of the family above. -/

/-- `Tr_H [V ρ V*]`, written out. -/
noncomputable def stinespringChannel (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e))
    (ρ : Matrix n n ℂ) : Matrix n n ℂ :=
  fun a c => ∑ i : e, (vmat V * ρ * (vmat V)ᴴ) (a, i) (c, i)

/-- **Gate 2.** -/
theorem channel_eq_krausMap (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e)) :
    stinespringChannel V = krausMap (krausOf V) := by
  funext ρ
  refine Matrix.ext fun a c => ?_
  simp only [stinespringChannel, krausMap, Matrix.sum_apply, Matrix.mul_apply,
    Matrix.conjTranspose_apply, krausOf, RCLike.star_def]

/-! ### Gate 1: minimality is Kraus independence

The manuscript's condition, with `M` ranging over all of `B(H_V)`. This is the one place in the
file where anything has to be proved rather than unfolded. -/

/-- `M ⊗ 1` acting on `H_V ⊗ H_H`. -/
def ampl (M : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ n) :
    EuclideanSpace ℂ (n × e) →ₗ[ℂ] EuclideanSpace ℂ (n × e) where
  toFun w := WithLp.toLp 2 fun p => M (WithLp.toLp 2 fun a' => w (a', p.2)) p.1
  map_add' w v := by
    refine (WithLp.ext_iff 2).2 (funext fun p => ?_)
    show M (WithLp.toLp 2 fun a' => w (a', p.2) + v (a', p.2)) p.1 = _
    rw [show (WithLp.toLp 2 fun a' => w (a', p.2) + v (a', p.2))
        = (WithLp.toLp 2 fun a' => w (a', p.2)) + WithLp.toLp 2 fun a' => v (a', p.2) from rfl,
      map_add]
    rfl
  map_smul' c w := by
    refine (WithLp.ext_iff 2).2 (funext fun p => ?_)
    show M (WithLp.toLp 2 fun a' => c * w (a', p.2)) p.1 = _
    rw [show (WithLp.toLp 2 fun a' => c * w (a', p.2))
        = c • WithLp.toLp 2 fun a' => w (a', p.2) from rfl, map_smul]
    rfl

@[simp] theorem ampl_apply (M : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ n)
    (w : EuclideanSpace ℂ (n × e)) (p : n × e) :
    ampl M w p = M (WithLp.toLp 2 fun a' => w (a', p.2)) p.1 := rfl

/-- **The manuscript's minimality condition**: the cyclic span of the dilation under
`B(H_V) ⊗ 1` is everything. -/
def Minimal (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e)) : Prop :=
  Submodule.span ℂ {w : EuclideanSpace ℂ (n × e) |
    ∃ (M : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ n) (ψ : EuclideanSpace ℂ n),
      w = ampl M (V ψ)} = ⊤

/-- The `i`-th environment slice of a vector in `H_V ⊗ H_H`. -/
noncomputable def slice (u : EuclideanSpace ℂ (n × e)) (i : e) : EuclideanSpace ℂ n :=
  WithLp.toLp 2 fun a => u (a, i)

/-- The rank-one operator `|x⟩⟨y|`. -/
noncomputable def rankOne (x y : EuclideanSpace ℂ n) : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ n where
  toFun v := ⟪y, v⟫ • x
  map_add' _ _ := by rw [inner_add_right, add_smul]
  map_smul' c v := by
    simp [inner_smul_right, smul_smul]

@[simp] theorem rankOne_apply (x y v : EuclideanSpace ℂ n) : rankOne x y v = ⟪y, v⟫ • x := rfl

/-- The vector `A_i ψ`, in the coordinates this file works in. -/
theorem ampl_apply_dilation (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e))
    (M : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ n) (ψ : EuclideanSpace ℂ n) (a : n) (i : e) :
    ampl M (V ψ) (a, i)
      = M (WithLp.toLp 2 fun a' => ∑ b, ψ b * krausOf V i a' b) a := by
  have harg : (WithLp.toLp 2 fun a' => (V ψ) (a', i))
      = WithLp.toLp 2 fun a' => ∑ b, ψ b * krausOf V i a' b :=
    (WithLp.ext_iff 2).2 (funext fun a' => apply_eq V ψ (a', i))
  rw [ampl_apply, harg]

/-- The matrix the orthogonality condition produces: for a fixed visible index `a`, the
combination of the Kraus family with coefficients `conj (u (a, i))`. -/
noncomputable def annihilator (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e))
    (u : EuclideanSpace ℂ (n × e)) (a : n) : Matrix n n ℂ :=
  ∑ i, (starRingEnd ℂ) (u (a, i)) • krausOf V i

theorem slice_sum_eq (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e))
    (u : EuclideanSpace ℂ (n × e)) (ψ : EuclideanSpace ℂ n) (a a' : n) :
    (∑ i, u (a, i) * (starRingEnd ℂ) (∑ b, ψ b * krausOf V i a' b))
      = (starRingEnd ℂ) (∑ b, ψ b * annihilator V u a a' b) := by
  simp only [annihilator, Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul, map_sum, map_mul,
    Complex.conj_conj, Finset.mul_sum]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun b _ => by ring

/-- **The inner product against the cyclic set, in closed form.** Both directions of Gate 1 read
off this one computation. -/
theorem inner_ampl_eq (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e))
    (M : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ n) (ψ : EuclideanSpace ℂ n)
    (u : EuclideanSpace ℂ (n × e)) :
    ⟪ampl M (V ψ), u⟫
      = ∑ a, ∑ a', (starRingEnd ℂ) (M (EuclideanSpace.single a' 1) a)
          * (starRingEnd ℂ) (∑ b, ψ b * annihilator V u a a' b) := by
  rw [PiLp.inner_apply]
  simp only [RCLike.inner_apply]
  rw [Fintype.sum_prod_type]
  have hstep : ∀ a : n, ∀ i : e,
      u (a, i) * (starRingEnd ℂ) (ampl M (V ψ) (a, i))
        = ∑ a', (starRingEnd ℂ) (M (EuclideanSpace.single a' 1) a)
            * (u (a, i) * (starRingEnd ℂ) (∑ b, ψ b * krausOf V i a' b)) := by
    intro a i
    rw [ampl_apply_dilation, apply_eq' M _ a]
    rw [map_sum, Finset.mul_sum]
    exact Finset.sum_congr rfl fun a' _ => by rw [map_mul]; ring
  simp only [hstep]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun a' _ => ?_
  rw [← Finset.mul_sum, slice_sum_eq]

/-- **Orthogonality to the cyclic set, in coordinates.** -/
theorem orthogonal_iff (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e))
    (u : EuclideanSpace ℂ (n × e)) :
    (∀ (M : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ n) (ψ : EuclideanSpace ℂ n),
        ⟪ampl M (V ψ), u⟫ = 0)
      ↔ ∀ a : n, annihilator V u a = 0 := by
  constructor
  · intro h a₀
    refine Matrix.ext fun a' b => ?_
    have hz := h (rankOne (EuclideanSpace.single a₀ 1) (EuclideanSpace.single a' 1))
      (EuclideanSpace.single b 1)
    rw [inner_ampl_eq] at hz
    simp only [rankOne_apply, EuclideanSpace.inner_single_left, map_one,
      PiLp.smul_apply, PiLp.single_apply, smul_eq_mul, mul_ite, mul_one, mul_zero] at hz
    simp only [apply_ite, map_one, map_zero, ite_mul, zero_mul] at hz
    simpa using hz
  · intro h M ψ
    rw [inner_ampl_eq]
    refine Finset.sum_eq_zero fun a _ => Finset.sum_eq_zero fun a' _ => ?_
    rw [h a]
    simp

/-- Membership in the orthogonal complement of a span, tested on the generating set. -/
theorem mem_orthogonal_span {S : Set (EuclideanSpace ℂ (n × e))}
    (u : EuclideanSpace ℂ (n × e)) :
    u ∈ (Submodule.span ℂ S)ᗮ ↔ ∀ w ∈ S, ⟪w, u⟫ = 0 := by
  constructor
  · intro hu w hw
    exact (Submodule.mem_orthogonal _ u).1 hu w (Submodule.subset_span hw)
  · intro h
    refine (Submodule.mem_orthogonal _ u).2 fun w hw => ?_
    induction hw using Submodule.span_induction with
    | mem x hx => exact h x hx
    | zero => simp
    | add x y _ _ hx hy => rw [inner_add_left, hx, hy, add_zero]
    | smul c x _ hx => rw [inner_smul_left, hx, mul_zero]

/-! ### Gate 1

The manuscript's cyclicity condition and linear independence of the Kraus family are the same
statement. `Nonempty n` is required and is not decoration: with a zero visible space every
dilation is vacuously cyclic while its Kraus family need not be independent, and a zero visible
space is not an embedded observer. -/

/-- **Gate 1: minimality is Kraus independence.** -/
theorem minimal_iff_linearIndependent [Nonempty n]
    (V : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e)) :
    Minimal V ↔ LinearIndependent ℂ (krausOf V) := by
  have hkey : Minimal V ↔ ∀ u : EuclideanSpace ℂ (n × e),
      (∀ a : n, annihilator V u a = 0) → u = 0 := by
    rw [Minimal, ← Submodule.orthogonal_eq_bot_iff, Submodule.eq_bot_iff]
    constructor
    · intro h u hu
      refine h u ((mem_orthogonal_span u).2 ?_)
      rintro w ⟨M, ψ, rfl⟩
      exact (orthogonal_iff V u).2 hu M ψ
    · intro h u hu
      exact h u ((orthogonal_iff V u).1 fun M ψ =>
        (mem_orthogonal_span u).1 hu _ ⟨M, ψ, rfl⟩)
  rw [hkey]
  constructor
  · intro h
    refine Fintype.linearIndependent_iff.2 fun c hc i => ?_
    obtain ⟨a₀⟩ := ‹Nonempty n›
    have hu : (WithLp.toLp 2 fun p : n × e => (starRingEnd ℂ) (c p.2)) = 0 := by
      refine h _ fun a => ?_
      simpa [annihilator, Complex.conj_conj] using hc
    have := congrArg (fun w : EuclideanSpace ℂ (n × e) => w (a₀, i)) hu
    simpa using this
  · intro hind u hu
    refine (WithLp.ext_iff 2).2 (funext fun p => ?_)
    have := Fintype.linearIndependent_iff.1 hind
      (fun i => (starRingEnd ℂ) (u (p.1, i))) (by simpa [annihilator] using hu p.1) p.2
    simpa using this

/-! ### Gate 3: the orientation of the environment unitary

`FactorUniqueness` produces the COLUMN factor `W : H_H^(2) → H_H^(1)`, and the environment unitary
in `V₂ = (1 ⊗ T) V₁` runs the other way. It is NOT the adjoint of the factor: writing
`V₁ψ = Σ_i (A_i ψ) ⊗ e_i`, the identity `(1 ⊗ T)(V₁ψ) = V₂ψ` reads `T_ji = W(e_j)_i` in
coordinates, so `T`'s matrix is the TRANSPOSE of the factor's column matrix — the adjoint would
conjugate the entries and is a different operator whenever they are not real. That transpose is
exactly `KrausUniqueness.krausMatrix`, which is why the Kraus relation there is already in the
manuscript's `B_j = Σ_i U_ji A_i` order. -/

/-- `1 ⊗ T`, changing the environment factor. -/
noncomputable def amplR (T : EuclideanSpace ℂ e →ₗ[ℂ] EuclideanSpace ℂ f) :
    EuclideanSpace ℂ (n × e) →ₗ[ℂ] EuclideanSpace ℂ (n × f) where
  toFun w := WithLp.toLp 2 fun q => T (WithLp.toLp 2 fun i => w (q.1, i)) q.2
  map_add' w v := by
    refine (WithLp.ext_iff 2).2 (funext fun q => ?_)
    show T (WithLp.toLp 2 fun i => w (q.1, i) + v (q.1, i)) q.2 = _
    rw [show (WithLp.toLp 2 fun i => w (q.1, i) + v (q.1, i))
        = (WithLp.toLp 2 fun i => w (q.1, i)) + WithLp.toLp 2 fun i => v (q.1, i) from rfl,
      map_add]
    rfl
  map_smul' c w := by
    refine (WithLp.ext_iff 2).2 (funext fun q => ?_)
    show T (WithLp.toLp 2 fun i => c * w (q.1, i)) q.2 = _
    rw [show (WithLp.toLp 2 fun i => c * w (q.1, i))
        = c • WithLp.toLp 2 fun i => w (q.1, i) from rfl, map_smul]
    rfl

@[simp] theorem amplR_apply (T : EuclideanSpace ℂ e →ₗ[ℂ] EuclideanSpace ℂ f)
    (w : EuclideanSpace ℂ (n × e)) (q : n × f) :
    amplR T w q = T (WithLp.toLp 2 fun i => w (q.1, i)) q.2 := rfl

/-- **The environment unitary**, built from the coefficient factor with the transpose orientation
described above. -/
noncomputable def hiddenUnitary (W : EuclideanSpace ℂ f →ₗ[ℂ] EuclideanSpace ℂ e) :
    EuclideanSpace ℂ e →ₗ[ℂ] EuclideanSpace ℂ f where
  toFun x := WithLp.toLp 2 fun j => ∑ i, W (EuclideanSpace.single j 1) i * x i
  map_add' x y := by
    refine (WithLp.ext_iff 2).2 (funext fun j => ?_)
    show (∑ i, W (EuclideanSpace.single j 1) i * (x i + y i)) = _
    rw [show ((WithLp.toLp 2 fun j => ∑ i, W (EuclideanSpace.single j 1) i * x i)
        + WithLp.toLp 2 fun j => ∑ i, W (EuclideanSpace.single j 1) i * y i).ofLp j
        = (∑ i, W (EuclideanSpace.single j 1) i * x i)
          + ∑ i, W (EuclideanSpace.single j 1) i * y i from rfl]
    rw [← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun i _ => by ring
  map_smul' c x := by
    refine (WithLp.ext_iff 2).2 (funext fun j => ?_)
    simp only [RingHom.id_apply]
    show (∑ i, W (EuclideanSpace.single j 1) i * (c * x i))
        = c * ∑ i, W (EuclideanSpace.single j 1) i * x i
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun i _ => by ring

@[simp] theorem hiddenUnitary_apply (W : EuclideanSpace ℂ f →ₗ[ℂ] EuclideanSpace ℂ e)
    (x : EuclideanSpace ℂ e) (j : f) :
    hiddenUnitary W x j = ∑ i, W (EuclideanSpace.single j 1) i * x i := rfl

/-- **The environment unitary's matrix is `KrausUniqueness.krausMatrix`** — the manuscript's `U`,
in the manuscript's index order. -/
theorem hiddenUnitary_matrix (W : EuclideanSpace ℂ f →ₗ[ℂ] EuclideanSpace ℂ e)
    (x : EuclideanSpace ℂ e) (j : f) :
    hiddenUnitary W x j = ∑ i, krausMatrix W j i * x i := rfl

/-- **Gate 3: the reassembly.** -/
theorem V2_eq_hiddenUnitary_V1 {V₁ : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e)}
    {V₂ : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × f)}
    {W : EuclideanSpace ℂ f →ₗ[ℂ] EuclideanSpace ℂ e}
    (hW : synth (krausOf V₁) ∘ₗ W = synth (krausOf V₂)) :
    ∀ ψ, V₂ ψ = amplR (hiddenUnitary W) (V₁ ψ) := by
  intro ψ
  refine (WithLp.ext_iff 2).2 (funext fun q => ?_)
  obtain ⟨a, j⟩ := q
  have hrel := kraus_relation hW j
  show V₂ ψ (a, j) = _
  rw [apply_eq V₂ ψ (a, j)]
  have hB : ∀ b, krausOf V₂ j a b = ∑ i, krausMatrix W j i * krausOf V₁ i a b := by
    intro b
    have := congrArg (fun N : Matrix n n ℂ => N a b) hrel
    simpa [Matrix.sum_apply] using this
  show (∑ b, ψ b * vmat V₂ (a, j) b) = hiddenUnitary W (WithLp.toLp 2 fun i => V₁ ψ (a, i)) j
  rw [hiddenUnitary_matrix]
  simp only [show ∀ b, vmat V₂ (a, j) b = krausOf V₂ j a b from fun _ => rfl, hB]
  have hV1 : ∀ i : e, V₁ ψ (a, i) = ∑ b, ψ b * krausOf V₁ i a b :=
    fun i => apply_eq V₁ ψ (a, i)
  simp only [hV1, Finset.mul_sum]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun b _ => by ring

/-! ### The environment unitary is unitary

Column orthonormality of `U` is exactly `W ∘ₗ W* = 1`, which `KrausUniqueness` already delivers. -/

theorem hiddenUnitary_inner {W : EuclideanSpace ℂ f →ₗ[ℂ] EuclideanSpace ℂ e}
    (h : W ∘ₗ adjoint W = LinearMap.id) (x y : EuclideanSpace ℂ e) :
    ⟪hiddenUnitary W x, hiddenUnitary W y⟫ = ⟪x, y⟫ := by
  have hadj : ∀ (i : e) (j : f), adjoint W (EuclideanSpace.single i 1) j
      = (starRingEnd ℂ) (W (EuclideanSpace.single j 1) i) := by
    intro i j
    have h0 := adjoint_inner_left W (EuclideanSpace.single j 1)
      (EuclideanSpace.single i 1 : EuclideanSpace ℂ e)
    rw [EuclideanSpace.inner_single_right, EuclideanSpace.inner_single_left] at h0
    simp only [map_one, one_mul] at h0
    have := congrArg (starRingEnd ℂ) h0
    simpa [Complex.conj_conj] using this
  have hcol : ∀ i i' : e, (∑ j, (starRingEnd ℂ) (W (EuclideanSpace.single j 1) i)
      * W (EuclideanSpace.single j 1) i') = if i' = i then 1 else 0 := by
    intro i i'
    have hx : W (adjoint W (EuclideanSpace.single i 1)) i'
        = (EuclideanSpace.single i 1 : EuclideanSpace ℂ e) i' :=
      congrArg (fun g : EuclideanSpace ℂ e →ₗ[ℂ] EuclideanSpace ℂ e =>
        g (EuclideanSpace.single i 1) i') h
    rw [apply_eq' W _ i'] at hx
    simp only [hadj] at hx
    rw [PiLp.single_apply] at hx
    exact hx
  rw [PiLp.inner_apply, PiLp.inner_apply]
  simp only [RCLike.inner_apply, hiddenUnitary_apply, map_sum, map_mul]
  have hexp : ∀ j : f,
      (∑ i', W (EuclideanSpace.single j 1) i' * y i')
        * (∑ i, (starRingEnd ℂ) (W (EuclideanSpace.single j 1) i) * (starRingEnd ℂ) (x i))
      = ∑ i, ∑ i', ((starRingEnd ℂ) (W (EuclideanSpace.single j 1) i)
          * W (EuclideanSpace.single j 1) i') * ((starRingEnd ℂ) (x i) * y i') := by
    intro j
    rw [Finset.sum_mul_sum, Finset.sum_comm]
    exact Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun i' _ => by ring
  simp only [hexp]
  rw [Finset.sum_comm]
  have hstep : ∀ i : e, (∑ j, ∑ i', ((starRingEnd ℂ) (W (EuclideanSpace.single j 1) i)
      * W (EuclideanSpace.single j 1) i') * ((starRingEnd ℂ) (x i) * y i'))
      = y i * (starRingEnd ℂ) (x i) := by
    intro i
    rw [Finset.sum_comm]
    have hin : ∀ i' : e, (∑ j, ((starRingEnd ℂ) (W (EuclideanSpace.single j 1) i)
        * W (EuclideanSpace.single j 1) i') * ((starRingEnd ℂ) (x i) * y i'))
        = (if i' = i then (1 : ℂ) else 0) * ((starRingEnd ℂ) (x i) * y i') := by
      intro i'
      rw [← Finset.sum_mul, hcol i i']
    simp only [hin]
    simp [mul_comm]
  simp only [hstep]

theorem hiddenUnitary_adjoint_comp {W : EuclideanSpace ℂ f →ₗ[ℂ] EuclideanSpace ℂ e}
    (h : W ∘ₗ adjoint W = LinearMap.id) :
    adjoint (hiddenUnitary W) ∘ₗ hiddenUnitary W = LinearMap.id := by
  refine LinearMap.ext fun y => ?_
  refine ext_inner_left ℂ fun x => ?_
  rw [LinearMap.comp_apply, adjoint_inner_right, hiddenUnitary_inner h]
  rfl

/-! ### Uniqueness of the environment unitary

The manuscript says "a unique unitary", and uniqueness is not inherited from the coefficient
factor for free: it has to be read back through `1 ⊗ ·`. Independence of the Kraus family is again
what supplies it. -/

/-- **The environment operator is determined.** -/
theorem amplR_ext {V₁ : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e)}
    (hA : LinearIndependent ℂ (krausOf V₁))
    {T T' : EuclideanSpace ℂ e →ₗ[ℂ] EuclideanSpace ℂ f}
    (h : ∀ ψ, amplR T (V₁ ψ) = amplR T' (V₁ ψ)) : T = T' := by
  have hbasis : ∀ (i : e) (j : f),
      T (EuclideanSpace.single i 1) j = T' (EuclideanSpace.single i 1) j := by
    intro i j
    have key : ∀ j' : f, (∑ i', (T (EuclideanSpace.single i' 1) j'
        - T' (EuclideanSpace.single i' 1) j') • krausOf V₁ i') = 0 := by
      intro j'
      refine Matrix.ext fun a b => ?_
      have hb := congrArg (fun w : EuclideanSpace ℂ (n × f) => w (a, j'))
        (h (EuclideanSpace.single b 1))
      simp only [amplR_apply] at hb
      rw [apply_eq' T _ j', apply_eq' T' _ j'] at hb
      have hw : ∀ i' : e, V₁ (EuclideanSpace.single b 1) (a, i') = krausOf V₁ i' a b := by
        intro i'
        rw [apply_eq V₁ _ (a, i')]
        simp [PiLp.single_apply, Finset.sum_ite_eq', krausOf, vmat]
      simp only [hw] at hb
      rw [Matrix.sum_apply, Matrix.zero_apply]
      have hterm : ∀ i' : e, ((T (EuclideanSpace.single i' 1) j'
          - T' (EuclideanSpace.single i' 1) j') • krausOf V₁ i') a b
          = krausOf V₁ i' a b * T (EuclideanSpace.single i' 1) j'
            - krausOf V₁ i' a b * T' (EuclideanSpace.single i' 1) j' := by
        intro i'
        simp only [Matrix.smul_apply, smul_eq_mul]
        ring
      simp only [hterm, Finset.sum_sub_distrib, hb, sub_self]
    exact sub_eq_zero.1 (Fintype.linearIndependent_iff.1 hA _ (key j) i)
  refine LinearMap.ext fun x => (WithLp.ext_iff 2).2 (funext fun j => ?_)
  rw [apply_eq' T x j, apply_eq' T' x j]
  exact Finset.sum_congr rfl fun i _ => by rw [hbasis i j]

/-! ### Proposition 9.7b -/

/-- **[Structure] Proposition 9.7b.**

Two minimal dilations of the same channel have equal environment dimension and are related by a
unitary on the environment: `V₂ = (1 ⊗ T) V₁`. The conclusion stops at the isometry, which is the
whole point of the repair — the dilating unitaries are not determined off the prepared reference
subspace, and `stinespring_scope_probe.py`'s CNOT pair is the standing witness. -/
theorem proposition_9_7b [Nonempty n]
    {V₁ : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × e)}
    {V₂ : EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ (n × f)}
    (h₁ : Minimal V₁) (h₂ : Minimal V₂)
    (hchan : stinespringChannel V₁ = stinespringChannel V₂) :
    Fintype.card f = Fintype.card e ∧
    ∃! T : EuclideanSpace ℂ e →ₗ[ℂ] EuclideanSpace ℂ f,
      (∀ ψ, V₂ ψ = amplR T (V₁ ψ)) ∧ adjoint T ∘ₗ T = LinearMap.id := by
  have hA : LinearIndependent ℂ (krausOf V₁) := (minimal_iff_linearIndependent V₁).1 h₁
  have hB : LinearIndependent ℂ (krausOf V₂) := (minimal_iff_linearIndependent V₂).1 h₂
  have hk : krausMap (krausOf V₁) = krausMap (krausOf V₂) := by
    rw [← channel_eq_krausMap, ← channel_eq_krausMap, hchan]
  obtain ⟨W, ⟨hWf, hWa, hWb⟩, -⟩ := kraus_uniqueness hA hB hk
  refine ⟨card_eq hA hB hk, hiddenUnitary W,
    ⟨V2_eq_hiddenUnitary_V1 hWf, hiddenUnitary_adjoint_comp hWb⟩, ?_⟩
  rintro T ⟨hT, -⟩
  refine amplR_ext hA fun ψ => ?_
  rw [← hT ψ, V2_eq_hiddenUnitary_V1 hWf ψ]

/-! ### What these proofs rest on -/

#print axioms apply_eq'
#print axioms channel_eq_krausMap
#print axioms inner_ampl_eq
#print axioms orthogonal_iff
#print axioms minimal_iff_linearIndependent
#print axioms hiddenUnitary_matrix
#print axioms V2_eq_hiddenUnitary_V1
#print axioms hiddenUnitary_inner
#print axioms amplR_ext
#print axioms proposition_9_7b

end StinespringUniqueness

end OIBridge
