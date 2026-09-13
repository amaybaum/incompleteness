import OIBridge.AnchorRobustness

/-!
# Act 11 — the coherent-lift stabilizer no-go

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-11-coherent-lift-gauge/preregistration.md`, blob
`0f6d37fafd857d9e54d5dbff6d062cc360ea08e5`, from `main` at
`6cff07cc0655124f1f29e04b156cc05a3d717a48` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base.

## The level this round attacks

`AdmissibleDilationAt G a₀ U` constrains `U` **only** through
`G i j = ∑_a ‖U (i,a) (j,a₀)‖²`. That fixes an anchored modulus-squared marginal and **determines no
channel**, so Stinespring uniqueness cannot close the gap — it speaks about dilations *of a given
channel*, and here the channel is not yet pinned. Acts 9 and 10 characterized *conventions* (the
readback map, the anchor) on a structure underdetermined one level up; this round asks what a
coherent time-indexed lift on a fixed carrier determines and what it leaves free.

**Act 11 is intentionally in dilation-choice territory.** Construction and deformation of dilated
families are within scope here. This does not amend or evade act 10; act 10 prohibited those
constructions because its frozen question held the act 7 dilations fixed.

## Two stabilizers, and why conflating them was the error the freeze was corrected for

Fixing the anchored columns is **sufficient** for invisibility, **not necessary**. So the round
carries two nested objects:

* `StrongAnchorStabilizer` — fixes each anchored column pointwise. This is exactly the freedom act
  7's merged `admissible_mul_of_fixes_anchor` consumes. Its size is a **lower bound** on invisible
  freedom, never its measure.
* `WeakAnchorStabilizer` — preserves each anchored *line*, so anchored phases are included. This is
  the maximal **uniform** visibility-preserving class, for `|V| ≥ 2`.

## What is proved

* **`GL1s`** — `strong_mem_weak`, `weak_anchor_coeff_norm_one`, `strong_column_offAnchor_eq_zero`
  (the `S_{a₀}^⊥`-invariance that makes the block structure), `strong_eq_one_of_ancilla_subsingleton`
  (the `|A| = 1` triviality), `card_offAnchor` (the complement's cardinality is `|V|(|A| − 1)`), and
  `gaugeRelated_strong_iff_agree_on_anchor` (the orbit classification).
* **`GL1w`** — `weak_preserves_admissible` (invisibility), and
  `weak_of_preserves_every_admissible` (**maximality**, under uniformity and for `|V| ≥ 2`), with
  `visible_marginal_eq_one_of_visible_subsingleton` and
  `all_preserve_admissible_of_visible_subsingleton` recording that at `|V| = 1` the visible datum is
  constant and **every** unitary preserves it, so `𝒢ʷ` is *not* maximal there.

  **Scope, as for `GL1s`**: what is kernel-checked is the **structural characterization** —
  membership, the unit-circle coefficients, maximality, the `|V| = 1` exception. The Lie-group
  identification `𝒢ʷ ≅ U(1)^{|V|} × U(|V|(|A| − 1))` and its dimension are **not** theorems of this
  module and nothing here rests on them.
* **`GL2`** — `gl2_strong_gauge_moves_relative_candidate`: a time-dependent element of the
  **strong** class carries a coherent lift to another coherent lift of the same visible family while
  the relative candidate moves. Using the smaller class makes the statement stronger.
* **`GL3`** — `gl3_constant_gauge_preserves_relative`, **necessity only**: a constant gauge leaves
  every relative object unchanged. `GL2` supplies existential sufficiency. Neither says every
  time-dependent gauge moves every candidate.
* **the witness controls** — `forced_gauge_witnessB`, `forced_gauge_witnessA`: computing
  `K = Uᴴ U'` puts **both** act 7 witnesses in the strong class. Witness A's element *conjugates*
  under act 7's convention, which is why reading it off the constructor is wrong.
* **`GI2`** — `gi2_lifts_not_weakly_gauge_related`: two coherent lifts of the same visible family
  whose forced element lies **outside** the weak class, so the **lift space** is not exhausted by
  the maximal uniform weak stabilizer. The theorem's final conjunct proves this pair nevertheless
  has the **same relative object at every pair of times**, so it is *not* evidence of non-gauge
  ambiguity in the relative evolution. `GL2` is the round's only relative-evolution no-go.

**The cocycle condition is vacuous and nothing here uses it.** With relatives defined as
`U t (U s)ᴴ`, `U'_{t←s} U'_{s←r} = U'_{t←r}` holds for every family whatsoever.

## What is NOT established

`P0` is **not** closed. Act 7 layer 2's caveat, as act 9 sharpened it, **stands unchanged** —
`GL2` makes it structural rather than provisional. Nothing here proves OI and QM inequivalent: the
statement is that the visible family does not *by itself* fix the relative evolution. No
candidate-selection principle is claimed or shown to be required. `𝒢ˢ`'s size is a lower bound, not
the size of the ambiguity. Act 7's `D3` **existence/regularity audit stays open** — act 11 subsumes
`D3` only as a proposed *uniqueness mechanism*. Act 7's `DC1`, act 8's `CE1`, act 9's `RB3`/`RB1-*`
and act 10's `AB0-*` are consumed unmodified, and act 7 layer 2's `D5` control stands **NOT
CERTIFIED**. Regularity is act 5's merged continuous-side countercontrol, **not** a theorem here:
`CoherentLift` is `ℕ`-indexed, so no smoothness claim is made about it. No manuscript propagation.
-/

namespace OIBridge
namespace CoherentLiftGauge

open Finset Matrix CausalReadback RootedClassification TransposeBridge BarandesTupleRound
  ContinuousExtension DilationChoice ReadbackRobustness AnchorRobustness

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — the two stabilizers, lifts, and gauge-relatedness -/

/-- **THE STRONG ANCHORED STABILIZER** (act 11's budget slot 1) — unitaries fixing every anchored
column *pointwise*, i.e. acting as the identity on `S_{a₀} = span {e_{(j,a₀)}}`.

This is exactly the freedom act 7's merged `admissible_mul_of_fixes_anchor` consumes: its hypothesis
`∀ p j, P p (j, a₀) = if p = (j, a₀) then 1 else 0` is membership here, verbatim.

**Its size is a LOWER BOUND on invisible freedom, not its measure** — fixing the anchored columns is
sufficient to preserve the anchored marginal, not necessary. See `WeakAnchorStabilizer`. -/
def StrongAnchorStabilizer (a₀ : A) (K : Matrix (V × A) (V × A) ℂ) : Prop :=
  K ∈ Matrix.unitaryGroup (V × A) ℂ ∧ ∀ p j, K p (j, a₀) = if p = (j, a₀) then 1 else 0

/-- **THE WEAK ANCHORED STABILIZER** (slot 2) — unitaries preserving each anchored *line*.

The coefficients `c j` are forced onto the unit circle by unitarity
(`weak_anchor_coeff_norm_one`), so this is genuinely "phase on each anchored column". It **strictly**
contains the strong class, and the extra elements are exactly what makes act 5's time-dependent
diagonal-phase construction invisible.

**For `|V| ≥ 2` this is the MAXIMAL uniform visibility-preserving class**
(`weak_of_preserves_every_admissible`). At `|V| = 1` it is **not** maximal — the visible datum is
constant there and every unitary preserves it. -/
def WeakAnchorStabilizer (a₀ : A) (K : Matrix (V × A) (V × A) ℂ) : Prop :=
  K ∈ Matrix.unitaryGroup (V × A) ℂ ∧
    ∃ c : V → ℂ, ∀ p j, K p (j, a₀) = if p = (j, a₀) then c j else 0

/-- **A COHERENT LIFT** (slot 3) — one family on **one fixed carrier and anchor**, admissible for
the visible family at every time.

**Indexed by `ℕ`, deliberately and with consequences.** No smoothness or continuity claim can be
made about this object, so none is; act 5's smooth construction is a separate merged countercontrol
on the continuous side. -/
def CoherentLift (a₀ : A) (Γ : ℕ → Matrix V V ℝ) (U : ℕ → Matrix (V × A) (V × A) ℂ) : Prop :=
  ∀ t, AdmissibleDilationAt (Γ t) a₀ (U t)

/-- **GAUGE-RELATEDNESS, PARAMETERIZED BY THE CLASS** (slot 4) — one definition serving both
stabilizers, so no statement can drift between them.

**`K` is not required to be constant in time**, which is the whole point: see `GL2` and `GL3`.

**The relating family is FORCED**, since each `U t` is unitary: `U' t = U t * K t` has the unique
solution `K t = (U t)ᴴ (U' t)`. So gauge-relatedness is a **membership check on a computed element**,
never a search over the class — `gaugeRelated_iff_forced` records this. -/
def GaugeRelated (𝒞 : Matrix (V × A) (V × A) ℂ → Prop)
    (U U' : ℕ → Matrix (V × A) (V × A) ℂ) : Prop :=
  ∃ K : ℕ → Matrix (V × A) (V × A) ℂ, (∀ t, 𝒞 (K t)) ∧ ∀ t, U' t = U t * K t

/-- The strong class sits inside the weak one, with all coefficients `1`. -/
theorem strong_mem_weak {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (h : StrongAnchorStabilizer a₀ K) : WeakAnchorStabilizer a₀ K :=
  ⟨h.1, fun _ => 1, fun p j => h.2 p j⟩

/-- **UNITARITY FORCES THE WEAK COEFFICIENTS ONTO THE UNIT CIRCLE**, so the weak class really is
"a phase on each anchored line" and not something looser. -/
theorem weak_anchor_coeff_norm_one {a₀ : A} {K : Matrix (V × A) (V × A) ℂ} {c : V → ℂ}
    (hK : K ∈ Matrix.unitaryGroup (V × A) ℂ)
    (hc : ∀ p j, K p (j, a₀) = if p = (j, a₀) then c j else 0) (j : V) : ‖c j‖ = 1 := by
  have h1 : (star K * K) = 1 := by
    have h := Matrix.mem_unitaryGroup_iff'.1 hK
    rwa [Matrix.star_eq_conjTranspose] at h ⊢
  have hjj := congrFun (congrFun h1 (j, a₀)) (j, a₀)
  rw [Matrix.mul_apply, Matrix.one_apply_eq] at hjj
  have hterm : ∀ r : V × A, (star K) (j, a₀) r * K r (j, a₀) = ((‖K r (j, a₀)‖ ^ 2 : ℝ) : ℂ) := by
    intro r
    rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_apply, mul_comm, RCLike.star_def,
      Complex.mul_conj]
    norm_cast
    exact Complex.normSq_eq_norm_sq _
  rw [Finset.sum_congr rfl fun r _ => hterm r, ← Complex.ofReal_sum] at hjj
  have hsum : (∑ r : V × A, ‖K r (j, a₀)‖ ^ 2) = 1 := by exact_mod_cast hjj
  rw [Finset.sum_eq_single (j, a₀) (fun b _ hb => by rw [hc b j, if_neg hb]; simp)
    (fun h => absurd (Finset.mem_univ _) h), hc (j, a₀) j, if_pos rfl] at hsum
  nlinarith [norm_nonneg (c j), hsum]

/-! ### Section B — `GL1s`: the strong stabilizer's exact shape -/

/-- **THE `S_{a₀}^⊥`-INVARIANCE, WHICH IS WHAT MAKES THE BLOCK STRUCTURE.**

For `K` in the strong class, every off-anchor column is orthogonal to `S_{a₀}`: the anchored rows of
such a column vanish. Together with the definition — the anchored columns are the standard basis
vectors — this is the statement that `K` is the identity on `S_{a₀}` and a unitary on `S_{a₀}^⊥`,
whose index set is the off-anchor pairs. `card_offAnchor` gives that set's size. -/
theorem strong_column_offAnchor_eq_zero {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (h : StrongAnchorStabilizer a₀ K) (j : V) (q : V × A) (hq : q.2 ≠ a₀) :
    K (j, a₀) q = 0 := by
  have h1 : (star K * K) = 1 := by
    have hh := Matrix.mem_unitaryGroup_iff'.1 h.1
    rwa [Matrix.star_eq_conjTranspose] at hh ⊢
  have hne : ((j, a₀) : V × A) ≠ q := fun hcon => hq (by rw [← hcon])
  have hjq := congrFun (congrFun h1 (j, a₀)) q
  rw [Matrix.mul_apply, Matrix.one_apply_ne hne] at hjq
  rw [Finset.sum_eq_single (j, a₀)
    (fun b _ hb => by
      rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_apply, h.2 b j, if_neg hb]
      simp)
    (fun hc => absurd (Finset.mem_univ _) hc)] at hjq
  rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_apply, h.2 (j, a₀) j, if_pos rfl] at hjq
  simpa using hjq

/-- **THE `|A| = 1` TRIVIALITY, part of `GL1s`'s target.** With a single ancilla configuration every
column is anchored, so the strong class collapses to the identity. -/
theorem strong_eq_one_of_ancilla_subsingleton [Subsingleton A] {a₀ : A}
    {K : Matrix (V × A) (V × A) ℂ} (h : StrongAnchorStabilizer a₀ K) : K = 1 := by
  ext p q
  obtain ⟨j, a⟩ := q
  rw [show a = a₀ from Subsingleton.elim a a₀, h.2 p j, Matrix.one_apply]

/-- **THE COMPLEMENT'S CARDINALITY**, which is the `|V| · (|A| − 1)` in `GL1s`'s isomorphism type.

The strong class is the identity on `S_{a₀}` and unitary on `S_{a₀}^⊥`; this counts the index set of
that complement, so "`𝒢ˢ_{a₀} ≅ U(|V|(|A| − 1))`" has its carrier size proved here rather than
asserted. **The real dimension `(|V|(|A| − 1))²` is the standard dimension of a unitary group and is
recorded in the result note as arithmetic, not as a theorem of this module.** -/
theorem card_offAnchor (a₀ : A) :
    Fintype.card {p : V × A // p.2 ≠ a₀} = Fintype.card V * (Fintype.card A - 1) := by
  classical
  have e : {p : V × A // p.2 ≠ a₀} ≃ V × {a : A // a ≠ a₀} :=
    { toFun := fun p => (p.1.1, ⟨p.1.2, p.2⟩)
      invFun := fun q => ⟨(q.1, q.2.1), q.2.2⟩
      left_inv := fun p => by cases p; rfl
      right_inv := fun q => by obtain ⟨x, y, hy⟩ := q; rfl }
  rw [Fintype.card_congr e, Fintype.card_prod]
  congr 1
  rw [Fintype.card_subtype_compl, Fintype.card_subtype_eq]

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- `Uᴴ U'` is unitary when both are: the shape the forced gauge element needs. -/
theorem conjTranspose_mul_mem_unitaryGroup {n : Type} [Fintype n] [DecidableEq n]
    {U U' : Matrix n n ℂ} (hU : U ∈ Matrix.unitaryGroup n ℂ)
    (hU' : U' ∈ Matrix.unitaryGroup n ℂ) : Uᴴ * U' ∈ Matrix.unitaryGroup n ℂ := by
  have h1 : U'ᴴ * U' = 1 := by
    have h := Matrix.mem_unitaryGroup_iff'.1 hU'
    rwa [Matrix.star_eq_conjTranspose] at h
  have h2 : U * Uᴴ = 1 := by
    have h := Matrix.mem_unitaryGroup_iff.1 hU
    rwa [Matrix.star_eq_conjTranspose] at h
  rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose, Matrix.conjTranspose_mul,
    Matrix.conjTranspose_conjTranspose, ← mul_assoc, mul_assoc U'ᴴ, h2, mul_one, h1]

/-- **THE ORBIT CLASSIFICATION** — two lifts are strongly gauge-related exactly when they agree on
the anchored subspace at every time.

The reverse direction is the forced element `K t = (U t)ᴴ (U' t)`, which fixes `S_{a₀}` pointwise
precisely because the two agree there. -/
theorem gaugeRelated_strong_iff_agree_on_anchor {a₀ : A} {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (hU' : ∀ t, U' t ∈ Matrix.unitaryGroup (V × A) ℂ) :
    GaugeRelated (StrongAnchorStabilizer a₀) U U'
      ↔ ∀ t p j, U' t p (j, a₀) = U t p (j, a₀) := by
  constructor
  · rintro ⟨K, hKmem, hfac⟩ t p j
    rw [hfac t, Matrix.mul_apply]
    rw [Finset.sum_eq_single (j, a₀)
      (fun b _ hb => by rw [(hKmem t).2 b j, if_neg hb, mul_zero])
      (fun hc => absurd (Finset.mem_univ _) hc)]
    rw [(hKmem t).2 (j, a₀) j, if_pos rfl, mul_one]
  · intro hagree
    refine ⟨fun t => (U t)ᴴ * U' t,
      fun t => ⟨conjTranspose_mul_mem_unitaryGroup (hU t) (hU' t), fun p j => ?_⟩, fun t => ?_⟩
    · show ((U t)ᴴ * U' t) p (j, a₀) = _
      rw [Matrix.mul_apply]
      have hcol : ∀ r, U' t r (j, a₀) = U t r (j, a₀) := fun r => hagree t r j
      rw [Finset.sum_congr rfl fun r _ => by rw [hcol r]]
      have h1 : ((U t)ᴴ * U t) = 1 := by
        have h := Matrix.mem_unitaryGroup_iff'.1 (hU t)
        rwa [Matrix.star_eq_conjTranspose] at h
      have := congrFun (congrFun h1 p) (j, a₀)
      rw [Matrix.mul_apply] at this
      rw [this, Matrix.one_apply]
    · have h2 : (U t * (U t)ᴴ) = 1 := by
        have h := Matrix.mem_unitaryGroup_iff.1 (hU t)
        rwa [Matrix.star_eq_conjTranspose] at h
      rw [← mul_assoc, h2, one_mul]

/-! ### Section C — `GL1w`: invisibility, and maximality for `|V| ≥ 2` -/

/-- **THE WEAK CLASS IS INVISIBLE** — right multiplication by it preserves admissibility, hence the
whole visible family.

This is the direction that makes "invisible freedom" the right name, and it is why the weak class
and not the strong one is the class `GI1`/`GI2` must be asked over. -/
theorem weak_preserves_admissible {a₀ : A} {G : Matrix V V ℝ}
    {U K : Matrix (V × A) (V × A) ℂ} (hU : AdmissibleDilationAt G a₀ U)
    (hK : WeakAnchorStabilizer a₀ K) : AdmissibleDilationAt G a₀ (U * K) := by
  obtain ⟨hKmem, c, hc⟩ := hK
  refine ⟨mul_mem hU.1 hKmem, fun i j => ?_⟩
  have hcol : ∀ p : V × A, (U * K) p (j, a₀) = c j * U p (j, a₀) := by
    intro p
    rw [Matrix.mul_apply, Finset.sum_eq_single (j, a₀)
      (fun b _ hb => by rw [hc b j, if_neg hb, mul_zero])
      (fun hcon => absurd (Finset.mem_univ _) hcon), hc (j, a₀) j, if_pos rfl, mul_comm]
  rw [hU.2 i j]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [hcol (i, a), norm_mul, weak_anchor_coeff_norm_one hKmem hc j, one_mul]

/-- Left multiplication by a permutation matrix reindexes rows, in the form the maximality proof
consumes. Act 7 has the right-handed version (`mul_permMatrix_apply`); this is its partner. -/
theorem permMatrix_mul_apply (σ : Equiv.Perm (V × A)) (K : Matrix (V × A) (V × A) ℂ)
    (p q : V × A) : (σ.permMatrix ℂ * K) p q = K (σ p) q := by
  rw [Matrix.mul_apply]
  simp only [permMatrix_apply_eq]
  rw [Finset.sum_eq_single (σ p) (fun r _ hr => by rw [if_neg hr, zero_mul])
    (fun hc => absurd (Finset.mem_univ _) hc), if_pos rfl, one_mul]

/-- **`GL1w`'s MAXIMALITY, AND IT HOLDS ONLY FOR `|V| ≥ 2`.**

If a unitary `K` preserves the visible marginal of **every** admissible dilation, then `K` lies in
the weak class. So the weak class is the largest *uniform* visibility-preserving right action.

**Two test dilations do all the work**, so no search over unitaries is needed. The identity
(admissible for `𝟙` at every anchor, by act 10's merged `one_admissible_at_every_anchor`) forces
each anchored column into its own visible fibre. Then, for each off-anchor `a`, the transposition
`swap ((j,a), (j',a))` with `j' ≠ j` — admissible for its own closed-form marginal by act 7's merged
`admissible_permMatrix` — moves that one slot into a different fibre, where the first test has
already shown the mass is zero. Subtracting leaves `‖K (j,a) (j,a₀)‖ = 0`.

**`|V| ≥ 2` is where the force comes from**: the argument needs a second fibre `j'` to move mass
into. At `|V| = 1` there is none, and indeed the conclusion is false there — see
`all_preserve_admissible_of_visible_subsingleton`. -/
theorem weak_of_preserves_every_admissible {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (hKmem : K ∈ Matrix.unitaryGroup (V × A) ℂ)
    (htwo : ∀ j : V, ∃ j' : V, j' ≠ j)
    (hpres : ∀ (G : Matrix V V ℝ) (U : Matrix (V × A) (V × A) ℂ),
      AdmissibleDilationAt G a₀ U → AdmissibleDilationAt G a₀ (U * K)) :
    WeakAnchorStabilizer a₀ K := by
  classical
  -- TEST 1: the identity dilation of the identity slice, admissible at every anchor (act 10).
  have hone := hpres 1 1 (one_admissible_at_every_anchor a₀)
  have hfibre : ∀ i j : V, (if i = j then (1 : ℝ) else 0)
      = ∑ a : A, ‖K (i, a) (j, a₀)‖ ^ 2 := by
    intro i j
    have h := hone.2 i j
    rw [Matrix.one_apply] at h
    refine h.trans (Finset.sum_congr rfl fun a _ => ?_)
    rw [show ((1 : Matrix (V × A) (V × A) ℂ) * K) (i, a) (j, a₀) = K (i, a) (j, a₀) from by
      rw [one_mul]]
  -- from test 1: off-fibre entries of an anchored column vanish
  have hoff : ∀ i j : V, i ≠ j → ∀ a : A, K (i, a) (j, a₀) = 0 := by
    intro i j hij a
    have h := (hfibre i j).symm
    rw [if_neg hij] at h
    have hz : ∀ b : A, ‖K (i, b) (j, a₀)‖ ^ 2 = 0 :=
      fun b => le_antisymm
        (by
          rw [← h]
          exact Finset.single_le_sum (f := fun b => ‖K (i, b) (j, a₀)‖ ^ 2)
            (fun c _ => by positivity) (Finset.mem_univ b))
        (by positivity)
    have := hz a
    simpa using (pow_eq_zero_iff (n := 2) (by norm_num)).1 this
  -- TEST 2: one transposition per off-anchor slot
  have hslot : ∀ (j : V) (a : A), a ≠ a₀ → K (j, a) (j, a₀) = 0 := by
    intro j a ha
    obtain ⟨j', hj'⟩ := htwo j
    set τ : Equiv.Perm (V × A) := Equiv.swap ((j, a) : V × A) ((j', a) : V × A) with hτ
    have hτsymm : τ.symm ((j, a₀) : V × A) = (j, a₀) := by
      rw [hτ, Equiv.symm_swap]
      exact Equiv.swap_apply_of_ne_of_ne
        (fun hcon => ha ((Prod.ext_iff.mp hcon).2).symm)
        (fun hcon => hj' ((Prod.ext_iff.mp hcon).1).symm)
    have hadm : AdmissibleDilationAt
        (Matrix.of fun i m => if (τ.symm (m, a₀)).1 = i then (1 : ℝ) else 0) a₀ (τ.permMatrix ℂ) :=
      admissible_permMatrix a₀ τ (fun i m => rfl)
    have h := (hpres _ _ hadm).2 j j
    rw [show (Matrix.of fun i m => if (τ.symm (m, a₀)).1 = i then (1 : ℝ) else 0 : Matrix V V ℝ)
        j j = if (τ.symm ((j, a₀) : V × A)).1 = j then (1 : ℝ) else 0 from rfl,
      hτsymm] at h
    simp only [if_true] at h
    -- the perturbed sum splits: the anchored slot stays, the `a` slot has moved to fibre j'
    have hsplit : (∑ b : A, ‖(τ.permMatrix ℂ * K) (j, b) (j, a₀)‖ ^ 2)
        = ∑ b : A, ‖K (τ (j, b)) (j, a₀)‖ ^ 2 :=
      Finset.sum_congr rfl fun b _ => by rw [permMatrix_mul_apply]
    rw [hsplit] at h
    have hterm : ∀ b : A, ‖K (τ (j, b)) (j, a₀)‖ ^ 2
        = if b = a then 0 else ‖K (j, b) (j, a₀)‖ ^ 2 := by
      intro b
      by_cases hb : b = a
      · subst hb
        rw [if_pos rfl, hτ, Equiv.swap_apply_left, hoff j' j hj' b]
        simp
      · rw [if_neg hb, hτ]
        by_cases hb' : ((j, b) : V × A) = (j', a)
        · exact absurd ((Prod.ext_iff.mp hb').1).symm hj'
        · rw [Equiv.swap_apply_of_ne_of_ne (fun hcon => hb (Prod.ext_iff.mp hcon).2) hb']
    rw [Finset.sum_congr rfl fun b _ => hterm b] at h
    have hbase := (hfibre j j).symm
    rw [if_pos rfl] at hbase
    have hdiff : ‖K (j, a) (j, a₀)‖ ^ 2 = 0 := by
      have e1 : (∑ b : A, ‖K (j, b) (j, a₀)‖ ^ 2)
          = ‖K (j, a) (j, a₀)‖ ^ 2 + ∑ b ∈ Finset.univ.erase a, ‖K (j, b) (j, a₀)‖ ^ 2 :=
        (Finset.add_sum_erase _ _ (Finset.mem_univ a)).symm
      have e2 : (∑ b : A, if b = a then (0 : ℝ) else ‖K (j, b) (j, a₀)‖ ^ 2)
          = ∑ b ∈ Finset.univ.erase a, ‖K (j, b) (j, a₀)‖ ^ 2 := by
        rw [← Finset.add_sum_erase _ _ (Finset.mem_univ a), if_pos rfl, zero_add]
        exact Finset.sum_congr rfl fun b hb => if_neg (Finset.ne_of_mem_erase hb)
      rw [e2] at h
      rw [e1, ← h] at hbase
      linarith
    simpa using (pow_eq_zero_iff (n := 2) (by norm_num)).1 hdiff
  refine ⟨hKmem, fun j => K (j, a₀) (j, a₀), fun p j => ?_⟩
  obtain ⟨i, a⟩ := p
  by_cases hij : i = j
  · subst hij
    by_cases ha : a = a₀
    · subst ha; rw [if_pos rfl]
    · rw [if_neg (fun hcon => ha (Prod.ext_iff.mp hcon).2), hslot i a ha]
  · rw [if_neg (fun hcon => hij (Prod.ext_iff.mp hcon).1), hoff i j hij a]

/-- **AT `|V| = 1` THE VISIBLE DATUM IS CONSTANT**: the only entry is the squared norm of an
anchored column of a unitary, hence `1`. -/
theorem visible_marginal_eq_one_of_visible_subsingleton [Subsingleton V] {a₀ : A}
    {G : Matrix V V ℝ} {U : Matrix (V × A) (V × A) ℂ} (h : AdmissibleDilationAt G a₀ U)
    (i j : V) : G i j = 1 := by
  have h1 : (star U * U) = 1 := by
    have hh := Matrix.mem_unitaryGroup_iff'.1 h.1
    rwa [Matrix.star_eq_conjTranspose] at hh ⊢
  have hjj := congrFun (congrFun h1 (j, a₀)) (j, a₀)
  rw [Matrix.mul_apply, Matrix.one_apply_eq] at hjj
  have hterm : ∀ r : V × A, (star U) (j, a₀) r * U r (j, a₀) = ((‖U r (j, a₀)‖ ^ 2 : ℝ) : ℂ) := by
    intro r
    rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_apply, mul_comm, RCLike.star_def,
      Complex.mul_conj]
    norm_cast
    exact Complex.normSq_eq_norm_sq _
  rw [Finset.sum_congr rfl fun r _ => hterm r, ← Complex.ofReal_sum] at hjj
  have hsum : (∑ r : V × A, ‖U r (j, a₀)‖ ^ 2) = 1 := by exact_mod_cast hjj
  rw [h.2 i j, ← hsum, Fintype.sum_prod_type,
    Fintype.sum_subsingleton (fun x : V => ∑ y : A, ‖U (x, y) (j, a₀)‖ ^ 2) i]

/-- **SO AT `|V| = 1` EVERY UNITARY IS INVISIBLE, AND `𝒢ʷ` IS NOT MAXIMAL THERE.**

Both `U` and `U * K` are admissible for the same `G`, for **any** unitary `K` — because the visible
datum is constant at `1` and carries no information. The maximal uniform visibility-preserving class
is therefore all of `U(V × A)`, which strictly contains the weak class whenever `|A| ≥ 2`.

**This is why `weak_of_preserves_every_admissible` hypothesises a second visible state**, and why
the `GI` labels' reading as "maximal uniform invisible gauge" is scoped to `|V| ≥ 2`. -/
theorem all_preserve_admissible_of_visible_subsingleton [Subsingleton V] {a₀ : A}
    {G : Matrix V V ℝ} {U K : Matrix (V × A) (V × A) ℂ} (hU : AdmissibleDilationAt G a₀ U)
    (hK : K ∈ Matrix.unitaryGroup (V × A) ℂ) : AdmissibleDilationAt G a₀ (U * K) := by
  refine ⟨mul_mem hU.1 hK, fun i j => ?_⟩
  have hUK : AdmissibleDilationAt
      (Matrix.of fun i j => ∑ a : A, ‖(U * K) (i, a) (j, a₀)‖ ^ 2) a₀ (U * K) :=
    ⟨mul_mem hU.1 hK, fun _ _ => rfl⟩
  rw [visible_marginal_eq_one_of_visible_subsingleton hU i j]
  exact (visible_marginal_eq_one_of_visible_subsingleton hUK i j).symm

/-! ### Section D — `GL3`: necessity of time-dependence, and nothing more -/

/-- **`GL3` — A CONSTANT GAUGE LEAVES EVERY RELATIVE OBJECT UNCHANGED.**

So time-dependence of the gauge is **necessary** for this right action to move a relative object.

**This is one direction only.** `GL2` supplies that time-dependence **can be** sufficient,
existentially, at one exhibited lift. Neither statement says — and the round does not say — that
*every* time-dependent gauge moves *every* relative candidate: a gauge whose consecutive ratios
happen to act trivially on the readback would not.

Note the class is irrelevant here: only unitarity is used. -/
theorem gl3_constant_gauge_preserves_relative {K : Matrix (V × A) (V × A) ℂ}
    (hK : K ∈ Matrix.unitaryGroup (V × A) ℂ) (U : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) :
    (U t * K) * ((U s * K))ᴴ = U t * (U s)ᴴ := by
  have h : K * Kᴴ = 1 := by
    have hh := Matrix.mem_unitaryGroup_iff.1 hK
    rwa [Matrix.star_eq_conjTranspose] at hh
  rw [Matrix.conjTranspose_mul, ← mul_assoc, mul_assoc (U t), h, mul_one]

/-! ### Section E — the forced elements of act 7's two witnesses -/

/-- **WITNESS B's FORCED ELEMENT IS ITS OWN ANCHOR-FIXING PERMUTATION**, so witness B is
gauge-related in the **strong** class.

`U' = U * P(ρ)` gives `K = Uᴴ U' = P(ρ)` directly, because `Uᴴ U = 1`. Act 7 proved `P(ρ)` fixes
every anchored column — that is the `hfix` hypothesis its exhibition discharges. -/
theorem forced_gauge_witnessB {a₀ : A} {U : Matrix (V × A) (V × A) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (V × A) ℂ) (ρ : Equiv.Perm (V × A))
    (hfix : ∀ p j, (ρ.permMatrix ℂ) p (j, a₀) = if p = (j, a₀) then 1 else 0) :
    Uᴴ * (U * ρ.permMatrix ℂ) = ρ.permMatrix ℂ ∧
      StrongAnchorStabilizer a₀ (Uᴴ * (U * ρ.permMatrix ℂ)) := by
  have h1 : (Uᴴ * U) = 1 := by
    have h := Matrix.mem_unitaryGroup_iff'.1 hU
    rwa [Matrix.star_eq_conjTranspose] at h
  have hEq : Uᴴ * (U * ρ.permMatrix ℂ) = ρ.permMatrix ℂ := by
    rw [← mul_assoc, h1, one_mul]
  exact ⟨hEq, by rw [hEq]; exact ⟨permMatrix_mem_unitaryGroup ρ, hfix⟩⟩

/-- **WITNESS A's FORCED ELEMENT CONJUGATES, AND THAT IS THE TRAP.**

Act 7 builds witness A's second dilation as `P(σ · τ)`. Under act 7's convention
`permMatrix σ p q = if q = σ p then 1 else 0` the product rule is `P(g) P(h) = P(h * g)`, so

    K = P(σ)ᴴ P(σ · τ) = P(σ⁻¹) P(σ · τ) = P( (σ · τ) · σ⁻¹ ) = P( σ τ σ⁻¹ ),

**not** `P(τ)`. Reading the constructor's `τ` off directly is therefore wrong — and for witness A it
is wrong in a way that matters, since `τ = swap((1,0),(1,1))` moves the anchored vector `e_{(1,0)}`
while the conjugate `σ τ σ⁻¹ = swap((0,1),(1,1))` does not. The forced element must be **computed**.

This lemma is the general identity; `forced_gauge_witnessA_is_strong` instantiates it at act 7's
data and lands in the strong class. -/
theorem forced_gauge_perm (σ τ : Equiv.Perm (V × A)) :
    (σ.permMatrix ℂ)ᴴ * ((σ * τ).permMatrix ℂ) = (σ * τ * σ⁻¹).permMatrix ℂ := by
  rw [Matrix.conjTranspose_permMatrix, ← Matrix.permMatrix_mul]

/-- **BOTH ACT 7 WITNESSES ARE STRONG-CLASS `GL2` INSTANCES**, on act 7's own data.

Witness A's forced element is `σ τ σ⁻¹` with `σ = prodComm` and `τ = swap((1,0),(1,1))`, which is
`swap((0,1),(1,1))` — the **same** element as witness B's `ρ`. It fixes both anchored columns, so it
is in the strong class.

**Consequence, and it is the reason this is a control rather than a finding: neither merged witness
is a `GI2` candidate.** `GI2` needed a pair whose forced element escapes the *weak* class, and
section F supplies one that act 7 did not. -/
theorem forced_gauge_witnessA_is_strong :
    (Equiv.prodComm (Fin 2) (Fin 2) *
        Equiv.swap ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) *
        (Equiv.prodComm (Fin 2) (Fin 2))⁻¹ : Equiv.Perm (Fin 2 × Fin 2))
      = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
    ∧ StrongAnchorStabilizer (0 : Fin 2)
        ((Equiv.swap ((0 : Fin 2), (1 : Fin 2))
          ((1 : Fin 2), (1 : Fin 2)) : Equiv.Perm (Fin 2 × Fin 2)).permMatrix ℂ) := by
  refine ⟨?_, permMatrix_mem_unitaryGroup _, fun p j => ?_⟩
  · refine Equiv.ext (fun p => ?_)
    fin_cases p <;> decide
  · obtain ⟨x, y⟩ := p
    fin_cases x <;> fin_cases y <;> fin_cases j <;> simp +decide

/-! ### Section F — `GL2` and `GI2` on explicit data -/

/-- **`GL2` — A TIME-DEPENDENT STRONG-CLASS GAUGE MOVES THE RELATIVE CANDIDATE.**

Two coherent lifts of the **same** visible family, on one fixed carrier and anchor, related by a
time-dependent element of the **strong** class — the smaller of the two classes, which makes the
statement stronger — whose relative candidates **differ**.

The visible family is act 7 witness B's, period-two in the frozen sense: `Γ 0 = Bᵀ` and `Γ t = 𝟙`
for `t ≥ 1`. The lift is `U 0 = U_B`, `U t = 𝟙` thereafter; the gauge is `K 0 = P(ρ)`, `K t = 𝟙`
thereafter, which is time-dependent exactly because `P(ρ) ≠ 𝟙`. The relative candidate at `(1 ← 0)`
moves from `1/2` to `0` at the entry `(0,1)`.

**Bounded exactly as act 7's `DC1` is bounded**, and inheriting all of its bounds: one visible pair,
one anchor, one time pair, under the frozen readback. **The cocycle condition is not used**: it is
vacuous, holding for every family whatsoever.

**No regularity is claimed.** `CoherentLift` is `ℕ`-indexed; act 5's smooth construction is a
separate merged countercontrol on the continuous side. -/
theorem gl2_strong_gauge_moves_relative_candidate :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ) (U U' K : ℕ → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
      CoherentLift (0 : Fin 2) Γ U ∧ CoherentLift (0 : Fin 2) Γ U'
        ∧ (∀ t, StrongAnchorStabilizer (0 : Fin 2) (K t))
        ∧ (∀ t, U' t = U t * K t)
        ∧ (∃ t s : ℕ, K t ≠ K s)
        ∧ readback (0 : Fin 2)
              (Matrix.of fun p q => ‖(U 1 * (U 0)ᴴ) p q‖ ^ 2)
            ≠ readback (0 : Fin 2)
              (Matrix.of fun p q => ‖(U' 1 * (U' 0)ᴴ) p q‖ ^ 2) := by
  classical
  obtain ⟨s, hsdef⟩ : ∃ s : ℝ, s = Real.sqrt (1 / 2) := ⟨_, rfl⟩
  have hs : s * s = 1 / 2 := by rw [hsdef]; exact Real.mul_self_sqrt (by norm_num)
  have hs2 : s ^ 2 = 1 / 2 := by rw [sq]; exact hs
  have hsC : ((s : ℝ) : ℂ) * ((s : ℝ) : ℂ) = ((1 / 2 : ℝ) : ℂ) := by
    rw [← Complex.ofReal_mul, hs]
  obtain ⟨UB, hUB⟩ : ∃ UB : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ,
      UB = Matrix.of fun p q =>
        if p = (0, 0) then (if q = (0, 0) then 1 else 0)
        else if p = (0, 1) then
          (if q = (0, 1) then ((s : ℝ) : ℂ) else if q = (1, 0) then ((s : ℝ) : ℂ) else 0)
        else if p = (1, 0) then
          (if q = (0, 1) then -((s : ℝ) : ℂ) else if q = (1, 0) then ((s : ℝ) : ℂ) else 0)
        else (if q = (1, 1) then 1 else 0) := ⟨_, rfl⟩
  obtain ⟨ρ, hρ⟩ : ∃ ρ : Equiv.Perm (Fin 2 × Fin 2),
      ρ = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) := ⟨_, rfl⟩
  have hUBunit : UB ∈ Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ := by
    rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
    ext p q
    obtain ⟨x, y⟩ := p
    obtain ⟨u, v⟩ := q
    fin_cases x <;> fin_cases y <;> fin_cases u <;> fin_cases v <;>
      simp [hUB, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
        Matrix.conjTranspose_apply, Complex.conj_ofReal, hsC] <;>
      ring_nf
  have hBT : AdmissibleDilationAt
      ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) UB := by
    refine ⟨hUBunit, fun i j => ?_⟩
    fin_cases i <;> fin_cases j <;> simp [hUB, Fin.sum_univ_two, Matrix.transpose_apply, hs2]
  have hfix : ∀ p j, (ρ.permMatrix ℂ) p (j, (0 : Fin 2))
      = if p = (j, (0 : Fin 2)) then 1 else 0 := by
    intro p j
    obtain ⟨x, y⟩ := p
    fin_cases x <;> fin_cases y <;> fin_cases j <;> simp +decide [hρ]
  refine ⟨fun t => if t = 0 then
      ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ))ᵀ else 1,
    fun t => if t = 0 then UB else 1,
    fun t => if t = 0 then UB * ρ.permMatrix ℂ else 1,
    fun t => if t = 0 then ρ.permMatrix ℂ else 1, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro t
    by_cases ht : t = 0
    · subst ht
      show AdmissibleDilationAt
        ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
          Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) UB
      exact hBT
    · simp only [if_neg ht]; exact one_admissible_at_every_anchor _
  · intro t
    by_cases ht : t = 0
    · subst ht
      show AdmissibleDilationAt
        ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
          Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) (UB * ρ.permMatrix ℂ)
      exact admissible_mul_of_fixes_anchor hBT (permMatrix_mem_unitaryGroup ρ) hfix
    · simp only [if_neg ht]; exact one_admissible_at_every_anchor _
  · intro t
    by_cases ht : t = 0
    · subst ht
      show StrongAnchorStabilizer (0 : Fin 2) (ρ.permMatrix ℂ)
      exact ⟨permMatrix_mem_unitaryGroup ρ, hfix⟩
    · simp only [if_neg ht]
      exact ⟨one_mem _, fun p j => by rw [Matrix.one_apply]⟩
  · intro t
    by_cases ht : t = 0
    · subst ht
      show UB * ρ.permMatrix ℂ = UB * ρ.permMatrix ℂ
      rfl
    · simp only [if_neg ht, mul_one]
  · refine ⟨0, 1, ?_⟩
    show ρ.permMatrix ℂ ≠ (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    intro hcon
    have h01 := congrFun (congrFun hcon ((0 : Fin 2), (1 : Fin 2))) ((1 : Fin 2), (1 : Fin 2))
    rw [permMatrix_apply_eq, Matrix.one_apply] at h01
    simp +decide [hρ] at h01
  · show readback (0 : Fin 2)
        (Matrix.of fun p q => ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * UBᴴ) p q‖ ^ 2)
      ≠ readback (0 : Fin 2)
        (Matrix.of fun p q => ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          * (UB * ρ.permMatrix ℂ)ᴴ) p q‖ ^ 2)
    intro hEq
    have h01 := congrFun (congrFun hEq 0) 1
    have hL : readback (0 : Fin 2)
        (Matrix.of fun p q => ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * UBᴴ) p q‖ ^ 2) 0 1
        = 1 / 2 := by
      show (∑ a : Fin 2, ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * UBᴴ)
        ((0 : Fin 2), a) ((1 : Fin 2), (0 : Fin 2))‖ ^ 2) = 1 / 2
      simp [one_mul, Matrix.conjTranspose_apply, hUB, Fin.sum_univ_two, hs2]
    have hR : readback (0 : Fin 2)
        (Matrix.of fun p q => ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          * (UB * ρ.permMatrix ℂ)ᴴ) p q‖ ^ 2) 0 1 = 0 := by
      show (∑ a : Fin 2, ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
        * (UB * ρ.permMatrix ℂ)ᴴ) ((0 : Fin 2), a) ((1 : Fin 2), (0 : Fin 2))‖ ^ 2) = 0
      simp only [one_mul, Matrix.conjTranspose_apply, mul_permMatrix_apply]
      simp +decide [hρ, hUB, Fin.sum_univ_two, Equiv.swap_apply_def]
    rw [hL, hR] at h01
    norm_num at h01

/-- **`GI2` — THE AMBIGUITY IS NOT EXHAUSTED BY THE MAXIMAL UNIFORM INVISIBLE GAUGE.**

Two coherent lifts of the **same** visible family whose forced element lies **outside the weak
class**, on a carrier with `|V| = 2` so that `GL1w`'s maximality applies and the reading is
licensed.

The visible family is act 7 witness A's `G₁` slice `Aᵀ`, whose mass sits entirely in row `0`. The
two dilations are act 7's own `P(prodComm)` and `P(swap((0,0),(1,0)) · prodComm)`. Both are
admissible at `a₀ = 0`: admissibility constrains only the **fibre-summed** modulus, so row `0`'s
mass may be carried by either ancilla slot, and the two dilations differ in which.

The forced element is `P(swap((0,0),(1,0)))` — a transposition of two **anchored** basis vectors. It
therefore maps the anchored line at `j = 0` onto the anchored line at `j = 1`, and no element of the
weak class does that: weak membership requires each anchored column to be a multiple of its own
basis vector.

**What this does and does not say — and the bound is proved, not promised.** The final conjunct
states that this pair has the **same relative object at every pair of times**. Both lifts are
constant in `t`, so each relative object is identically `1`; equivalently, the forced element
`P(ρ)` is constant, and `gl3_constant_gauge_preserves_relative` applies to it.

So `GI2` says the lift space is **not exhausted by the maximal uniform weak stabilizer**, and that
is all it says. It does **not** exhibit non-gauge ambiguity in the relative quantum evolution, does
**not** show that the structure needed to pin the relative evolution must be larger than a gauge
fixing, and does **not** show a connection cannot suffice — this very pair is a counterexample to
reading it that way. `GL2` remains the round's only relative-evolution no-go. It does not say OI and
QM are inequivalent, does not close `P0`, and shows no candidate-selection principle required.

**The stronger target stays open**: a same-visible pair that lies outside the weak class *and*
differs in relative evolution. Nothing here supplies one. -/
theorem gi2_lifts_not_weakly_gauge_related :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ) (U U' : ℕ → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
      CoherentLift (0 : Fin 2) Γ U ∧ CoherentLift (0 : Fin 2) Γ U'
        ∧ ¬ GaugeRelated (WeakAnchorStabilizer (0 : Fin 2)) U U'
        ∧ ∀ t s, U' t * (U' s)ᴴ = U t * (U s)ᴴ := by
  classical
  obtain ⟨σ, hσ⟩ : ∃ σ : Equiv.Perm (Fin 2 × Fin 2), σ = Equiv.prodComm (Fin 2) (Fin 2) := ⟨_, rfl⟩
  obtain ⟨ρ, hρ⟩ : ∃ ρ : Equiv.Perm (Fin 2 × Fin 2),
      ρ = Equiv.swap ((0 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (0 : Fin 2)) := ⟨_, rfl⟩
  have hAT : ∀ σ' : Equiv.Perm (Fin 2 × Fin 2),
      (∀ i j : Fin 2,
        (((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ) i j
          = if (σ'.symm (j, (0 : Fin 2))).1 = i then (1 : ℝ) else 0) →
      AdmissibleDilationAt
        (((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ)
        (0 : Fin 2) (σ'.permMatrix ℂ) := fun σ' h => admissible_permMatrix _ σ' h
  refine ⟨fun _ =>
      (((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ),
    fun _ => σ.permMatrix ℂ, fun _ => (ρ * σ).permMatrix ℂ, fun _ => ?_, fun _ => ?_, ?_, ?_⟩
  · refine hAT σ (fun i j => ?_)
    fin_cases i <;> fin_cases j <;> simp +decide [hσ, Matrix.transpose_apply]
  · refine hAT (ρ * σ) (fun i j => ?_)
    fin_cases i <;> fin_cases j <;>
      simp +decide [hσ, hρ, Matrix.transpose_apply, Equiv.swap_apply_def]
  · rintro ⟨K, hKmem, hfac⟩
    -- the forced element is P(rho), which moves an anchored basis vector
    have hforced : K 0 = ρ.permMatrix ℂ := by
      have h1 : ((σ.permMatrix ℂ))ᴴ * (σ.permMatrix ℂ) = 1 := by
        have h := Matrix.mem_unitaryGroup_iff'.1 (permMatrix_mem_unitaryGroup σ)
        rwa [Matrix.star_eq_conjTranspose] at h
      have h2 := hfac 0
      have h3 : ((σ.permMatrix ℂ))ᴴ * ((ρ * σ).permMatrix ℂ)
          = ((σ.permMatrix ℂ))ᴴ * ((σ.permMatrix ℂ) * K 0) := by rw [← h2]
      rw [← mul_assoc, h1, one_mul] at h3
      rw [← h3, Matrix.conjTranspose_permMatrix]
      ext p q
      rw [Matrix.mul_apply]
      simp only [permMatrix_apply_eq, Equiv.Perm.mul_apply]
      rw [Finset.sum_eq_single (σ⁻¹ p) (fun r _ hr => by rw [if_neg hr, zero_mul])
        (fun hc => absurd (Finset.mem_univ _) hc), if_pos rfl, one_mul]
      refine if_congr ?_ rfl rfl
      constructor
      · intro h; rw [h, hσ]; simp
      · intro h; rw [h, hσ]; simp
    obtain ⟨c, hc⟩ := (hKmem 0).2
    have hbad := hc ((1 : Fin 2), (0 : Fin 2)) (0 : Fin 2)
    rw [hforced] at hbad
    rw [if_neg (by decide : ((1 : Fin 2), (0 : Fin 2)) ≠ ((0 : Fin 2), (0 : Fin 2)))] at hbad
    rw [permMatrix_apply_eq, hρ] at hbad
    simp +decide at hbad
  · -- both lifts are constant, so each relative object is identically `1`
    have hunit : ∀ π : Equiv.Perm (Fin 2 × Fin 2),
        (π.permMatrix ℂ) * (π.permMatrix ℂ)ᴴ = 1 := by
      intro π
      have h := Matrix.mem_unitaryGroup_iff.1 (permMatrix_mem_unitaryGroup π)
      rwa [Matrix.star_eq_conjTranspose] at h
    intro t s
    show ((ρ * σ).permMatrix ℂ) * ((ρ * σ).permMatrix ℂ)ᴴ
      = (σ.permMatrix ℂ) * (σ.permMatrix ℂ)ᴴ
    rw [hunit, hunit]

end CoherentLiftGauge
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.CoherentLiftGauge.strong_mem_weak
#print axioms OIBridge.CoherentLiftGauge.weak_anchor_coeff_norm_one
#print axioms OIBridge.CoherentLiftGauge.strong_column_offAnchor_eq_zero
#print axioms OIBridge.CoherentLiftGauge.strong_eq_one_of_ancilla_subsingleton
#print axioms OIBridge.CoherentLiftGauge.card_offAnchor
#print axioms OIBridge.CoherentLiftGauge.conjTranspose_mul_mem_unitaryGroup
#print axioms OIBridge.CoherentLiftGauge.gaugeRelated_strong_iff_agree_on_anchor
#print axioms OIBridge.CoherentLiftGauge.weak_preserves_admissible
#print axioms OIBridge.CoherentLiftGauge.permMatrix_mul_apply
#print axioms OIBridge.CoherentLiftGauge.weak_of_preserves_every_admissible
#print axioms OIBridge.CoherentLiftGauge.visible_marginal_eq_one_of_visible_subsingleton
#print axioms OIBridge.CoherentLiftGauge.all_preserve_admissible_of_visible_subsingleton
#print axioms OIBridge.CoherentLiftGauge.gl3_constant_gauge_preserves_relative
#print axioms OIBridge.CoherentLiftGauge.forced_gauge_witnessB
#print axioms OIBridge.CoherentLiftGauge.forced_gauge_perm
#print axioms OIBridge.CoherentLiftGauge.forced_gauge_witnessA_is_strong
#print axioms OIBridge.CoherentLiftGauge.gl2_strong_gauge_moves_relative_candidate
#print axioms OIBridge.CoherentLiftGauge.gi2_lifts_not_weakly_gauge_related
