import OIBridge.OrbitLawRigidityTwisted
import OIBridge.OrbitLawNaturalityFactorization

/-!
# Act 23 — the gaps of act 21's ladder, bundled: `L1`, `L3i`, `L3s` and the fourth corner of `L4n`/`L5`, at act 21's product configuration

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/preregistration.md`,
blob `93c06674792fa3565f6f94e5e954e484dca33cf2`, from `main` at
`64214bfb0ae41b9f0a4fb11159089fff32d4dd85` — the certified merge commit of that control plane, the
round's mandated execution base `B`, whose frozen blob this execution verified as its first act.

## What this round is

The first **bundled round**: four targets frozen together, each with its own proposition, its own
named witness, its own verdict rule and its own failure interpretation, executed in the fixed order
`G1` → `G2` → `G3` → `G4` with one verdict commit per target. It tests the three rungs act 21
reported undecided and act 22 did not touch — `L1`, `L3i`, `L3s` — and the one corner of the
`L4n`/`L5` square act 22 left outside, all at act 21's frozen product configuration —
`V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = (0,0)`, `Γ ≡ 1/16 = Γ₀ ⊗ Γ₀`, `e = Equiv.refl` —
with act 21's ladder, quotient list, configuration, one-`|A|` limitation and non-adoption clause
**consumed unchanged** and act 22's three verdicts consumed exactly as landed.

**The definition budget is zero.** This module states no rung and introduces no top-level
definition: every rung it discharges or refutes is act 21's declaration applied to a transition
family pinned by an equation in the statement that needs it, and each target's prefix is the
corresponding conjuncts of act 21's `LadderConds`, written out. Every object is the merged record's
own, consumed unmodified at merged strength — act 12's `FibreGram`, `GramPhaseEquiv`,
`RealizableGram` and `gramPhaseEquiv_cross_invariant`; act 18's `ProperAt` and `PropagatesFrom`;
act 20's `RelabelTransition`, `RelabelLift`, `TwistedNatural` and its exact law; act 21's ladder
declarations, `witness_supply`, `product_realizable`, `product_cross`, `relabel_product`,
`hadamard_entries`, `product_separations`, `ol1a_descent`, `realizable_relabel`,
`relabel_gramPhaseEquiv`, `gramPhaseEquiv_of_relabel`; act 22's `gramPhaseEquiv_diag`. **A merged
statement is not enlarged by being consumed.**

**This module's first commit carries Section A only** — shared lemmas that answer no target by
themselves: the product-marginal lemma in both directions, the Fourier family at an arbitrary unit
parameter with its Pythagorean sequence, the non-realizability of the zero tuple, and the
separations the four verdicts read. Each verdict enters in its own later commit, in the frozen
order.

**THE CLAUSE, carried at this mention — the module docstring.**
Act 23 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
none. A law that survives every condition this freeze names is a law that survives **those**
conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
**No law gains physical status by surviving, no carrier and no principle is adopted as the physical
one, and nothing here derives, recognises or approaches quantum evolution.**

**Act 7's boundary is carried at every use of the visible family**: act 7's `D4b` came back negative
— Source A supplies no general map carrying the relative candidate on the dilated carrier back to
`V` — and the readback is the repository's own, frozen by act 7's readback amendment.
-/

namespace OIBridge
namespace OrbitLawGaps

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization

/-! ### Section A — the shared lemmas, before any verdict

Four facts the freeze's proof routes rest on that the merged record does not carry in the form
needed. None is a verdict of any target, and none names any of the four witnesses. -/

/-- **The product-marginal lemma, one direction.** A phase equivalence of two product tuples whose
second factors carry the same nonzero diagonal entry at one index `m` restricts to a phase
equivalence of the first factors, with the phases `c₁ j₁ := c (j₁, m)`: reading the equivalence at
the matrix indices `(j₁, m)`, `(k₁, m)` in the fibre `(i₁, m)` gives
`G₁' i₁ j₁ k₁ · G₂' m m m = star (c (j₁,m)) · G₁ i₁ j₁ k₁ · c (k₁,m) · G₂ m m m`, and the diagonal
entries cancel. For realizable second factors the diagonal entry is the visible slice `Γ₂ m m`. -/
theorem gramPhaseEquiv_fst_of_product {V₁ V₂ : Type} {m : V₂}
    {G₁ G₁' : V₁ → Matrix V₁ V₁ ℂ} {G₂ G₂' : V₂ → Matrix V₂ V₂ ℂ}
    (hd : G₂ m m m = G₂' m m m) (hm : G₂ m m m ≠ 0)
    (h : GramPhaseEquiv
      (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
      (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => G₁' i.1 j.1 k.1 * G₂' i.2 j.2 k.2)) :
    GramPhaseEquiv G₁ G₁' := by
  obtain ⟨c, hc, hG⟩ := h
  refine ⟨fun j => c (j, m), fun j => hc (j, m), fun i j k => ?_⟩
  have e := hG (i, m) (j, m) (k, m)
  simp only [Matrix.of_apply] at e
  rw [← hd] at e
  have e' : G₁' i j k * G₂ m m m = (star (c (j, m)) * G₁ i j k * c (k, m)) * G₂ m m m := by
    rw [e]; ring
  exact mul_right_cancel₀ hm e'

/-- **The product-marginal lemma, the other direction.** A phase equivalence of first factors
lifts to the products with any common second factor, with the phases `c (j₁, j₂) := c₁ j₁`. -/
theorem product_gramPhaseEquiv_fst {V₁ V₂ : Type} {G₁ G₁' : V₁ → Matrix V₁ V₁ ℂ}
    (G₂ : V₂ → Matrix V₂ V₂ ℂ) (h : GramPhaseEquiv G₁ G₁') :
    GramPhaseEquiv
      (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
      (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => G₁' i.1 j.1 k.1 * G₂ i.2 j.2 k.2) := by
  obtain ⟨c, hc, hG⟩ := h
  refine ⟨fun j => c j.1, fun j => hc j.1, fun i j k => ?_⟩
  simp only [Matrix.of_apply]
  rw [hG]
  ring

/-- **The zero tuple is not realizable** on a nonempty carrier: its fibres sum to `0`, not to `1`. -/
theorem zero_not_realizable {V A : Type} [Fintype V] [DecidableEq V] [Nonempty V] [Fintype A]
    (Γ : Matrix V V ℝ) : ¬ RealizableGram A Γ (fun _ : V => (0 : Matrix V V ℂ)) := by
  rintro ⟨-, -, hsum, -⟩
  simp only [Finset.sum_const_zero] at hsum
  exact zero_ne_one hsum

/-- **The Fourier family at an arbitrary parameter `z` with `star z * z = 1`** — act 12's `H(z)`,
read at any unit `z` — is an admissible dilation of `Γ₀ ≡ ¼` at the anchor `0`: the rows are
pairwise orthogonal, each computation using `star z * z = 1` once, and every entry has squared
modulus `¼`. Act 12's three values are the instances `z ∈ {1, i, −1}`. -/
theorem hadamard_z_admissible (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))) (z : ℂ) (hz : star z * z = 1) :
    AdmissibleDilationAt Γ₀ (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) := by
  have hz' : z * star z = 1 := by rw [mul_comm]; exact hz
  have hnsq : z.re ^ 2 + z.im ^ 2 = 1 := by
    have h1 : (Complex.normSq z : ℂ) = 1 := by rw [← Complex.mul_conj, ← Complex.star_def]; exact hz'
    have h2 : Complex.normSq z = 1 := by exact_mod_cast h1
    rw [Complex.normSq_apply] at h2; nlinarith [h2]
  have hnorm : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← star_mul_self_eq_norm_sq, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  refine ⟨?_, ?_⟩
  · rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
    ext p q
    obtain ⟨x, y⟩ := p
    obtain ⟨u, v⟩ := q
    fin_cases x <;> fin_cases y <;> fin_cases u <;> fin_cases v <;>
      simp [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_four,
        Matrix.conjTranspose_apply, Complex.ext_iff] <;>
      (try constructor) <;>
      first
        | linear_combination (1 / 2 : ℝ) * hnsq
        | linear_combination (-1 / 2 : ℝ) * hnsq
        | ring1
  · intro i j
    rw [hΓ₀, Matrix.of_apply]
    simp only [Fin.sum_univ_one, Matrix.of_apply]
    fin_cases i <;> fin_cases j <;> simp [norm_neg, hnorm] <;> norm_num

/-- **The entries of the Fourier family's fibre-Gram tuple** at any parameter: the diagonal entry
`¼` and the cross-invariant `G^{(0)}_{10} · G^{(1)}_{01} = z/16`, act 12's invariant at the fibre
pair `(0,1)`. -/
theorem fibreGram_z_entries (z : ℂ) :
    FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) 0 0 0 = 1 / 4
      ∧ FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) 0 1 0
        * FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) 1 0 1
        = z / 16 := by
  constructor
  · simp [fibreGram_apply]
    norm_num
  · simp [fibreGram_apply]
    ring

/-- **The Pythagorean sequence on the unit circle**, `z_n = ((n² − 1) + 2n·i)/(n² + 1)`, written
with its real and imaginary parts: `star z_n * z_n = 1`, `z_1 = i`, the real part is
`1 − 2/(n² + 1)`, strictly increasing in `n`, so `n ↦ z_n` is injective and `z_n ≠ 1`; and for
`n ≥ 1`, `z_{n+1} ≠ z_1`. -/
theorem zseq_facts (zs : ℕ → ℂ)
    (hzs : zs = fun n : ℕ => Complex.mk (((n : ℝ) ^ 2 - 1) / ((n : ℝ) ^ 2 + 1))
      (2 * (n : ℝ) / ((n : ℝ) ^ 2 + 1))) :
    (∀ n, star (zs n) * zs n = 1) ∧ zs 1 = Complex.I
      ∧ (∀ n m, zs n = zs m → n = m) ∧ (∀ n, zs n ≠ 1)
      ∧ (∀ n, 1 ≤ n → zs (n + 1) ≠ zs 1) := by
  subst hzs
  have hpos : ∀ n : ℕ, (0 : ℝ) < (n : ℝ) ^ 2 + 1 := fun n => by positivity
  have hre : ∀ n : ℕ, (((n : ℝ) ^ 2 - 1) / ((n : ℝ) ^ 2 + 1)) = 1 - 2 / ((n : ℝ) ^ 2 + 1) := by
    intro n
    field_simp
    ring
  refine ⟨fun n => ?_, ?_, fun n m h => ?_, fun n h => ?_, fun n hn h => ?_⟩
  · apply Complex.ext <;> simp [Complex.mul_re, Complex.mul_im] <;> field_simp <;> ring
  · apply Complex.ext
    · simp
    · simp; norm_num
  · have := congrArg Complex.re h
    simp only at this
    rw [hre, hre] at this
    have h2 : (2 : ℝ) / ((n : ℝ) ^ 2 + 1) = 2 / ((m : ℝ) ^ 2 + 1) := by linarith
    have h3 : ((n : ℝ) ^ 2 + 1) = ((m : ℝ) ^ 2 + 1) := by
      have hn := hpos n
      have hm := hpos m
      field_simp at h2
      linarith
    have h4 : (n : ℝ) ^ 2 = (m : ℝ) ^ 2 := by linarith
    have h5 : (n : ℝ) = (m : ℝ) :=
      (pow_left_inj₀ (Nat.cast_nonneg n) (Nat.cast_nonneg m) two_ne_zero).mp h4
    exact_mod_cast h5
  · have := congrArg Complex.re h
    simp only [Complex.one_re] at this
    rw [hre] at this
    have := hpos n
    have h2 : (0 : ℝ) < 2 / ((n : ℝ) ^ 2 + 1) := by positivity
    linarith
  · have := congrArg Complex.re h
    simp only at this
    have hn' : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
    have h1 : (((1 : ℕ) : ℝ) ^ 2 - 1) / (((1 : ℕ) : ℝ) ^ 2 + 1) = 0 := by norm_num
    rw [h1, div_eq_zero_iff] at this
    rcases this with h2 | h2
    · push_cast at h2
      nlinarith
    · have := hpos (n + 1)
      push_cast at h2 this
      linarith

/-- **The entries and separations the verdicts read on the pinned objects**, each a finite
computation on act 12's `H(1)` and `H(i)`: the entry `G(H₁)^{(0)}_{02} = ¼`; the cross-invariant of
`G(H₁)` at the fibre pair `(0,2)`, `1/16`; and, on the product carrier through act 21's
`product_cross`, the separations `[G(H₁) ⊠ G(H₁)] ≠ [G(Hᵢ) ⊠ G(H₁)]` and
`[G(H₁) ⊠ G(Hᵢ)] ≠ [G(Hᵢ) ⊠ G(H₁)]` at `((0,0),(1,0))`, values `1/256` against `i/256`, and
`[G(Hᵢ) ⊠ G(H₁)] ≠ [Φ_σ G(Hᵢ) ⊠ G(H₁)]` at `((0,0),(2,0))`, values `1/256` against `i/256`. -/
theorem gap_separations (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ)
    (hH₁ : H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1))
    (hHᵢ : Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
        1, -Complex.I, -1, Complex.I] p.1 q.1)) :
    FibreGram (0 : Fin 1) H₁ 0 0 2 = 1 / 4
      ∧ FibreGram (0 : Fin 1) H₁ 0 2 0 * FibreGram (0 : Fin 1) H₁ 2 0 2 = 1 / 16
      ∧ ¬ GramPhaseEquiv
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
      ∧ ¬ GramPhaseEquiv
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) Hᵢ i.2 j.2 k.2)
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
      ∧ ¬ GramPhaseEquiv
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) Hᵢ) i.1 j.1 k.1
              * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2) := by
  obtain ⟨d1, di, c1, ci, ci2, ci3, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  have g02 : FibreGram (0 : Fin 1) H₁ 0 0 2 = 1 / 4 := by
    subst hH₁; simp [fibreGram_apply]; norm_num
  have g1c : FibreGram (0 : Fin 1) H₁ 0 2 0 * FibreGram (0 : Fin 1) H₁ 2 0 2 = 1 / 16 := by
    subst hH₁; simp [fibreGram_apply]; norm_num
  refine ⟨g02, g1c, ?_, ?_, ?_⟩
  · intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    rw [product_cross, product_cross, c1, d1, ci] at this
    norm_num [Complex.ext_iff] at this
  · intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    rw [product_cross, product_cross, c1, di, ci, d1] at this
    norm_num [Complex.ext_iff] at this
  · intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4))
    rw [product_cross, product_cross, ci2, d1, r2] at this
    norm_num [Complex.ext_iff] at this

end OrbitLawGaps
end OIBridge
