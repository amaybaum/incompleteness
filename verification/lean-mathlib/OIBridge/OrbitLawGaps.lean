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

/-! ### Section B — `G1`: the `L1` rung status at the product configuration, via `Φ_MD`

`Φ_MD`, the merge-then-drop transition, pinned by its two-time statement: at `t = 0` it sends
the class `[G(Hᵢ) ⊠ G(H₁)]` onto `G(H₁) ⊠ G(H₁)` and fixes every other tuple; at every `t ≥ 1` it
sends that class to the zero tuple and fixes every other tuple. It is time-inhomogeneous by construction,
which `L1`'s prefix — `ProperAt`, `PropagatesFrom`, `EvolvesTotally` — permits, `L2` being after
`L1` in `LadderConds` order. -/

open Classical in
/-- **`G1` — `Φ_MD` at the frozen product configuration: the prefix of `L1` holds and `L1` fails.**
`ProperAt` with the constant solutions at `G(H₁) ⊠ G(H₁)` and at `G(H₁) ⊠ G(Hᵢ)` — neither in the
fired class, and inequivalent through the product cross-invariant at `((0,0),(0,1))`, `1/256`
against `i/256` — and the constant trajectory at `G(Hᵢ) ⊠ G(H₁)` no solution, its image at time
`0` being `G(H₁) ⊠ G(H₁)`, inequivalent to it at `((0,0),(1,0))`; `PropagatesFrom` with clause (i)
from `ol1a_descent` under descent and clause (ii) the two constant solutions at `t = 1`;
`EvolvesTotally` with the trajectory `G₀, G(H₁) ⊠ G(H₁), G(H₁) ⊠ G(H₁), …` on the fired class and
the constant trajectory elsewhere. **`L1` fails at the transition index `t = 1`** on the realizable
tuple `G(Hᵢ) ⊠ G(H₁)` — realizable by `product_realizable` from `sh1_necessity` — whose image is
the zero tuple, which fails the conjunct `∑ i, G i = 1` of `RealizableGram`
(`zero_not_realizable`); the separating class is `[G(Hᵢ) ⊠ G(H₁)]`. -/
theorem phiMD_l1_restricts :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)),
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun t G =>
            if t = 0 then
              (if GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                  FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
                then (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                  FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
                else G)
            else
              (if GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                  FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
                then (fun _ : Fin 4 × Fin 4 => (0 : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
                else G)) →
          ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
              (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ
          ∧ RealizableGram (Fin 1 × Fin 1) (Γ 1)
              (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
          ∧ Φ 1 (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
              = (fun _ : Fin 4 × Fin 4 => (0 : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
          ∧ ¬ (∑ i, Φ 1 (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2) i = 1)
          ∧ ¬ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨d1, di, c1, ci, ci2, ci3, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  obtain ⟨-, -, sA, sB, -⟩ := gap_separations H₁ Hᵢ hH₁ hHᵢ
  obtain ⟨U₁₁, hU₁₁, hF₁₁⟩ := product_realizable hadm₁ hadm₁
  obtain ⟨U₁ᵢ, hU₁ᵢ, hF₁ᵢ⟩ := product_realizable hadm₁ hadmᵢ
  obtain ⟨Uᵢ₁, hUᵢ₁, hFᵢ₁⟩ := product_realizable hadmᵢ hadm₁
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, ?_⟩
  intro Γ Φ hΓ hΦ
  subst hΓ
  set Γp : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ :=
    Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2 with hΓp
  set P₁₁ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2
    with hP₁₁
  set P₁ᵢ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) Hᵢ i.2 j.2 k.2
    with hP₁ᵢ
  set Pᵢ₁ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2
    with hPᵢ₁
  have hR₁₁ : RealizableGram (Fin 1 × Fin 1) Γp P₁₁ := by
    have := sh1_necessity hU₁₁; rwa [hF₁₁] at this
  have hR₁ᵢ : RealizableGram (Fin 1 × Fin 1) Γp P₁ᵢ := by
    have := sh1_necessity hU₁ᵢ; rwa [hF₁ᵢ] at this
  have hRᵢ₁ : RealizableGram (Fin 1 × Fin 1) Γp Pᵢ₁ := by
    have := sh1_necessity hUᵢ₁; rwa [hFᵢ₁] at this
  -- the separation the two standing hypotheses read: `[G(H₁) ⊠ G(H₁)] ≠ [G(H₁) ⊠ G(Hᵢ)]`
  have s11i : ¬ GramPhaseEquiv P₁₁ P₁ᵢ := by
    intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4))
    rw [hP₁₁, hP₁ᵢ, product_cross, product_cross, c1, ci, d1] at this
    norm_num [Complex.ext_iff] at this
  -- the two-time statement, read branch by branch
  have hΦ0 : ∀ G, Φ 0 G = if GramPhaseEquiv G Pᵢ₁ then P₁₁ else G := by
    intro G; rw [hΦ]; exact if_pos rfl
  have hΦs : ∀ t, t ≠ 0 → ∀ G, Φ t G
      = if GramPhaseEquiv G Pᵢ₁ then (fun _ => (0 : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)) else G := by
    intro t ht G; rw [hΦ]; simp only [if_neg ht]
  have hno : ∀ t G, ¬ GramPhaseEquiv G Pᵢ₁ → Φ t G = G := by
    intro t G h
    rcases Nat.eq_zero_or_pos t with ht | ht
    · subst ht; rw [hΦ0, if_neg h]
    · rw [hΦs t (Nat.pos_iff_ne_zero.mp ht), if_neg h]
  have hfix11 : ∀ t, Φ t P₁₁ = P₁₁ := fun t => hno t P₁₁ sA
  have hfix1i : ∀ t, Φ t P₁ᵢ = P₁ᵢ := fun t => hno t P₁ᵢ sB
  have hΦ1 : Φ 1 Pᵢ₁ = fun _ => (0 : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := by
    rw [hΦs 1 one_ne_zero, if_pos (gramPhaseEquiv_refl _)]
  -- descent
  have hd : ∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G') := by
    intro t G G' h
    by_cases hc : GramPhaseEquiv G Pᵢ₁
    · have hc' : GramPhaseEquiv G' Pᵢ₁ := gramPhaseEquiv_trans (gramPhaseEquiv_symm h) hc
      rcases Nat.eq_zero_or_pos t with ht | ht
      · subst ht; rw [hΦ0, hΦ0, if_pos hc, if_pos hc']; exact gramPhaseEquiv_refl _
      · rw [hΦs t (Nat.pos_iff_ne_zero.mp ht), hΦs t (Nat.pos_iff_ne_zero.mp ht), if_pos hc,
          if_pos hc']
        exact gramPhaseEquiv_refl _
    · have hc' : ¬ GramPhaseEquiv G' Pᵢ₁ := fun hc' => hc (gramPhaseEquiv_trans h hc')
      rw [hno t G hc, hno t G' hc']; exact h
  refine ⟨?_, ?_, ?_, hRᵢ₁, hΦ1, ?_, ?_⟩
  · -- proper
    refine ⟨fun _ => P₁₁, fun _ => P₁ᵢ, fun _ => Pᵢ₁, fun _ => hR₁₁, fun _ => hR₁ᵢ, fun _ => hRᵢ₁,
      fun t => by rw [hfix11]; exact gramPhaseEquiv_refl _,
      fun t => by rw [hfix1i]; exact gramPhaseEquiv_refl _,
      fun h => s11i (h 0), fun h => ?_⟩
    have := h 0
    rw [hΦ0, if_pos (gramPhaseEquiv_refl _)] at this
    exact sA (gramPhaseEquiv_symm this)
  · -- propagates
    exact ⟨fun G₁ G₂ _ _ h₁ h₂ h0 =>
        (ol1a_descent ((0 : Fin 1), (0 : Fin 1)) (fun _ => Γp) hd).2.1 G₁ G₂ h₁ h₂ h0,
      1, fun _ => P₁₁, fun _ => P₁ᵢ, le_rfl, fun _ => hR₁₁, fun _ => hR₁ᵢ,
      fun t => by rw [hfix11]; exact gramPhaseEquiv_refl _,
      fun t => by rw [hfix1i]; exact gramPhaseEquiv_refl _, s11i⟩
  · -- total
    intro G₀ hG₀
    by_cases hc : GramPhaseEquiv G₀ Pᵢ₁
    · refine ⟨fun t => if t = 0 then G₀ else P₁₁, fun t => ?_, fun t => ?_, ?_⟩
      · dsimp only
        split_ifs
        · exact hG₀
        · exact hR₁₁
      · rcases Nat.eq_zero_or_pos t with ht | ht
        · subst ht
          simp only [zero_add, one_ne_zero, if_false, if_true]
          rw [hΦ0, if_pos hc]
          exact gramPhaseEquiv_refl _
        · have ht' := Nat.pos_iff_ne_zero.mp ht
          simp only [Nat.succ_ne_zero, if_false, if_neg ht']
          rw [hfix11]
          exact gramPhaseEquiv_refl _
      · simp only [if_true]
        exact gramPhaseEquiv_refl _
    · exact ⟨fun _ => G₀, fun _ => hG₀, fun t => by rw [hno t G₀ hc]; exact gramPhaseEquiv_refl _,
        gramPhaseEquiv_refl _⟩
  · -- the failing conjunct: the image's fibres sum to `0`, not to `1`
    intro h
    rw [hΦ1] at h
    simp only [Finset.sum_const_zero] at h
    exact zero_ne_one h
  · -- not L1
    intro hL1
    have := hL1 1 Pᵢ₁ hRᵢ₁
    rw [hΦ1] at this
    exact zero_not_realizable _ this

/-! ### Section C — `G2`: the `L3i` rung status at the product configuration, via `Φ_PC`

`Φ_PC`, the partial collapse, pinned by its statement: at every `t` it sends the class
`[G(Hᵢ) ⊠ G(H₁)]` onto `G(H₁) ⊠ G(H₁)` and fixes every other tuple. It is time-homogeneous. -/

open Classical in
/-- **`G2` — `Φ_PC` at the frozen product configuration: the prefix of `L3i` holds and `L3i`
fails.** `ProperAt` and `PropagatesFrom` with the constant solutions at `G(H₁) ⊠ G(H₁)` and at
`G(H₁) ⊠ G(Hᵢ)` — neither in the fired class, inequivalent at `((0,0),(0,1))` — and the constant
trajectory at `G(Hᵢ) ⊠ G(H₁)` no solution; `EvolvesTotally` with the iterates of the one map;
`PreservesAdmissible` because the image of a realizable tuple is `G(H₁) ⊠ G(H₁)` or the tuple
itself; the inline `L2` with `Φ₀ = Φ_PC 0`. **`L3i` fails at every `t`**: `G(Hᵢ) ⊠ G(H₁)` and
`G(H₁) ⊠ G(H₁)` are realizable, their images are the same tuple `G(H₁) ⊠ G(H₁)`, and they are
inequivalent — the product cross-invariant at `((0,0),(1,0))`, `i/256` against `1/256`. The failing
conjunct is injectivity on classes, the first conjunct of `Reversible`, stated here in its own
words; the second conjunct is not read. -/
theorem phiPC_l3i_restricts :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)),
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun _ G =>
            if GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
              then (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
              else G) →
          ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
              (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ
          ∧ (∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t, Φ t = Φ₀)
          ∧ (∀ t, RealizableGram (Fin 1 × Fin 1) (Γ t)
              (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2))
          ∧ (∀ t, RealizableGram (Fin 1 × Fin 1) (Γ t)
              (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2))
          ∧ (∀ t, Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
              = Φ t (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2))
          ∧ ¬ GramPhaseEquiv
              (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
              (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
          ∧ ∀ t, ¬ (∀ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
              RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) G' →
                GramPhaseEquiv (Φ t G) (Φ t G') → GramPhaseEquiv G G') := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨d1, di, c1, ci, ci2, ci3, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  obtain ⟨-, -, sA, sB, -⟩ := gap_separations H₁ Hᵢ hH₁ hHᵢ
  obtain ⟨U₁₁, hU₁₁, hF₁₁⟩ := product_realizable hadm₁ hadm₁
  obtain ⟨U₁ᵢ, hU₁ᵢ, hF₁ᵢ⟩ := product_realizable hadm₁ hadmᵢ
  obtain ⟨Uᵢ₁, hUᵢ₁, hFᵢ₁⟩ := product_realizable hadmᵢ hadm₁
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, ?_⟩
  intro Γ Φ hΓ hΦ
  subst hΓ
  set Γp : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ :=
    Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2 with hΓp
  set P₁₁ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2
    with hP₁₁
  set P₁ᵢ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) Hᵢ i.2 j.2 k.2
    with hP₁ᵢ
  set Pᵢ₁ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2
    with hPᵢ₁
  have hR₁₁ : RealizableGram (Fin 1 × Fin 1) Γp P₁₁ := by
    have := sh1_necessity hU₁₁; rwa [hF₁₁] at this
  have hR₁ᵢ : RealizableGram (Fin 1 × Fin 1) Γp P₁ᵢ := by
    have := sh1_necessity hU₁ᵢ; rwa [hF₁ᵢ] at this
  have hRᵢ₁ : RealizableGram (Fin 1 × Fin 1) Γp Pᵢ₁ := by
    have := sh1_necessity hUᵢ₁; rwa [hFᵢ₁] at this
  -- the separation the two standing hypotheses read: `[G(H₁) ⊠ G(H₁)] ≠ [G(H₁) ⊠ G(Hᵢ)]`
  have s11i : ¬ GramPhaseEquiv P₁₁ P₁ᵢ := by
    intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4))
    rw [hP₁₁, hP₁ᵢ, product_cross, product_cross, c1, ci, d1] at this
    norm_num [Complex.ext_iff] at this
  -- the one map, read branch by branch
  have hΦe : ∀ t G, Φ t G = if GramPhaseEquiv G Pᵢ₁ then P₁₁ else G := by
    intro t G; rw [hΦ]
  have hΦt : ∀ t, Φ t = Φ 0 := fun t => by rw [hΦ]
  have hyes : ∀ t G, GramPhaseEquiv G Pᵢ₁ → Φ t G = P₁₁ := by
    intro t G h; rw [hΦe, if_pos h]
  have hno : ∀ t G, ¬ GramPhaseEquiv G Pᵢ₁ → Φ t G = G := by
    intro t G h; rw [hΦe, if_neg h]
  have hfix11 : ∀ t, Φ t P₁₁ = P₁₁ := fun t => hno t P₁₁ sA
  have hfix1i : ∀ t, Φ t P₁ᵢ = P₁ᵢ := fun t => hno t P₁ᵢ sB
  have hcoll : ∀ t, Φ t Pᵢ₁ = P₁₁ := fun t => hyes t Pᵢ₁ (gramPhaseEquiv_refl _)
  -- descent and admissibility preservation
  have hd : ∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G') := by
    intro t G G' h
    by_cases hc : GramPhaseEquiv G Pᵢ₁
    · rw [hyes t G hc, hyes t G' (gramPhaseEquiv_trans (gramPhaseEquiv_symm h) hc)]
      exact gramPhaseEquiv_refl _
    · rw [hno t G hc, hno t G' (fun hc' => hc (gramPhaseEquiv_trans h hc'))]; exact h
  have hrel : ∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      RealizableGram (Fin 1 × Fin 1) Γp G → RealizableGram (Fin 1 × Fin 1) Γp (Φ t G) := by
    intro t G hG
    by_cases hc : GramPhaseEquiv G Pᵢ₁
    · rw [hyes t G hc]; exact hR₁₁
    · rw [hno t G hc]; exact hG
  refine ⟨?_, ?_, ?_, fun t G hG => hrel t G hG, ⟨Φ 0, hΦt⟩, fun _ => hRᵢ₁, fun _ => hR₁₁,
    fun t => by rw [hcoll, hfix11], fun h => sA (gramPhaseEquiv_symm h), ?_⟩
  · -- proper
    refine ⟨fun _ => P₁₁, fun _ => P₁ᵢ, fun _ => Pᵢ₁, fun _ => hR₁₁, fun _ => hR₁ᵢ, fun _ => hRᵢ₁,
      fun t => by rw [hfix11]; exact gramPhaseEquiv_refl _,
      fun t => by rw [hfix1i]; exact gramPhaseEquiv_refl _,
      fun h => s11i (h 0), fun h => ?_⟩
    have := h 0
    rw [hcoll] at this
    exact sA (gramPhaseEquiv_symm this)
  · -- propagates
    exact ⟨fun G₁ G₂ _ _ h₁ h₂ h0 =>
        (ol1a_descent ((0 : Fin 1), (0 : Fin 1)) (fun _ => Γp) hd).2.1 G₁ G₂ h₁ h₂ h0,
      1, fun _ => P₁₁, fun _ => P₁ᵢ, le_rfl, fun _ => hR₁₁, fun _ => hR₁ᵢ,
      fun t => by rw [hfix11]; exact gramPhaseEquiv_refl _,
      fun t => by rw [hfix1i]; exact gramPhaseEquiv_refl _, s11i⟩
  · -- total
    intro G₀ hG₀
    refine ⟨fun t => (Φ 0)^[t] G₀, ?_, ?_, gramPhaseEquiv_refl _⟩
    · intro t
      induction t with
      | zero => exact hG₀
      | succ n ih =>
        show RealizableGram (Fin 1 × Fin 1) Γp ((Φ 0)^[n + 1] G₀)
        rw [Function.iterate_succ_apply']
        exact hrel 0 _ ih
    · intro t
      show GramPhaseEquiv ((Φ 0)^[t + 1] G₀) (Φ t ((Φ 0)^[t] G₀))
      rw [Function.iterate_succ_apply', hΦt t]
      exact gramPhaseEquiv_refl _
  · -- not L3i, at every t
    intro t h
    have := h Pᵢ₁ P₁₁ hRᵢ₁ hR₁₁ (by rw [hcoll, hfix11]; exact gramPhaseEquiv_refl _)
    exact sA (gramPhaseEquiv_symm this)

/-! ### Section D — `G3`: the `L3s` rung status at the product configuration, via `Φ_HS`

`Φ_HS`, the Hilbert shift, pinned by its statement over supply item 7: `H(z)` is act 12's family
read at an arbitrary parameter, `z_n = ((n² − 1) + 2n·i)/(n² + 1)` the Pythagorean sequence on the
unit circle with `z_1 = i`, and `F_n = FibreGram 0 (H(z_n)) ⊠ G(H₁)`. At every `t`, `Φ_HS t G = F_{n+1}`
if `G ∼ F_n` for some `n ≥ 1` — the index written with `Nat.find`, and unique because the classes
`[F_n]` are pairwise distinct — and `G` otherwise. It is time-homogeneous. -/

open Classical in
/-- **`G3` — `Φ_HS` at the frozen product configuration: the prefix of `L3s` holds, `L3i`
included, and `L3s` fails.** The family is admissible at every unit parameter
(`hadamard_z_admissible`), each `F_n` is realizable (`product_realizable`, `sh1_necessity`), and
the classes `[F_n]` are pairwise distinct and distinct from `[G(H₁) ⊠ G(H₁)]` and
`[G(H₁) ⊠ G(Hᵢ)]` through the product cross-invariant at `((1,0),(0,0))`, `z_n/256` against
`1/256` (`fibreGram_z_entries`, `zseq_facts`, `product_cross`). Descent, `EvolvesTotally`,
`PreservesAdmissible`, the inline `L2`, `ProperAt` and `PropagatesFrom` follow as for the partial
collapse, with the non-solution the constant trajectory at `F_1`, whose image `F_2` is inequivalent
to it; **`L3i` holds** by the case split on membership in the family. **`L3s` fails at every `t`**:
`F_1 = G(Hᵢ) ⊠ G(H₁)` is realizable and no realizable tuple has image equivalent to it — an image
in the family is some `F_{n+1}` with `n ≥ 1`, and an image outside the family is the tuple itself,
outside the family. The failing conjunct is surjectivity onto classes, the second conjunct of
`Reversible`, stated here in its own words; the separating class is `[F_1] = [G(Hᵢ) ⊠ G(H₁)]`. -/
theorem phiHS_l3s_restricts :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Hz : ℂ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) (zs : ℕ → ℂ)
            (F : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)),
          Hz = (fun z => Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) →
          zs = (fun n : ℕ => Complex.mk (((n : ℝ) ^ 2 - 1) / ((n : ℝ) ^ 2 + 1))
            (2 * (n : ℝ) / ((n : ℝ) ^ 2 + 1))) →
          F = (fun n => fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            FibreGram (0 : Fin 1) (Hz (zs n)) i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2) →
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun _ G => if h : ∃ n, 1 ≤ n ∧ GramPhaseEquiv G (F n) then F (Nat.find h + 1) else G) →
          ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
              (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ
          ∧ (∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t, Φ t = Φ₀)
          ∧ (∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) G' →
                GramPhaseEquiv (Φ t G) (Φ t G') → GramPhaseEquiv G G')
          ∧ (∀ t n, RealizableGram (Fin 1 × Fin 1) (Γ t) (F n))
          ∧ (∀ n m, GramPhaseEquiv (F n) (F m) → n = m)
          ∧ F 1 = (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
          ∧ (∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              RealizableGram (Fin 1 × Fin 1) (Γ t) G → ¬ GramPhaseEquiv (Φ t G) (F 1))
          ∧ ∀ t, ¬ (∀ G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
              RealizableGram (Fin 1 × Fin 1) (Γ (t + 1)) G' →
                ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
                  RealizableGram (Fin 1 × Fin 1) (Γ t) G ∧ GramPhaseEquiv (Φ t G) G') := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨d1, di, c1, ci, ci2, ci3, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  obtain ⟨U₁₁, hU₁₁, hF₁₁⟩ := product_realizable hadm₁ hadm₁
  obtain ⟨U₁ᵢ, hU₁ᵢ, hF₁ᵢ⟩ := product_realizable hadm₁ hadmᵢ
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, ?_⟩
  intro Hz zs F Γ Φ hHz hzs hF hΓ hΦ
  subst hΓ
  obtain ⟨hunit, hz1, hzinj, hzne1, -⟩ := zseq_facts zs hzs
  set Γp : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ :=
    Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2 with hΓp
  set P₁₁ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2
    with hP₁₁
  set P₁ᵢ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) Hᵢ i.2 j.2 k.2
    with hP₁ᵢ
  have hR₁₁ : RealizableGram (Fin 1 × Fin 1) Γp P₁₁ := by
    have := sh1_necessity hU₁₁; rwa [hF₁₁] at this
  have hR₁ᵢ : RealizableGram (Fin 1 × Fin 1) Γp P₁ᵢ := by
    have := sh1_necessity hU₁ᵢ; rwa [hF₁ᵢ] at this
  -- the family: admissibility, entries, realizability, the product form
  have hadmz : ∀ z : ℂ, star z * z = 1 → AdmissibleDilationAt Γ₀ (0 : Fin 1) (Hz z) := by
    intro z hz; rw [hHz]; exact hadamard_z_admissible Γ₀ hΓ₀ z hz
  have hdz : ∀ z : ℂ, FibreGram (0 : Fin 1) (Hz z) 0 0 0 = 1 / 4 := by
    intro z; rw [hHz]; exact (fibreGram_z_entries z).1
  have hcz : ∀ z : ℂ, FibreGram (0 : Fin 1) (Hz z) 1 0 1 * FibreGram (0 : Fin 1) (Hz z) 0 1 0
      = z / 16 := by
    intro z; rw [mul_comm, hHz]; exact (fibreGram_z_entries z).2
  have hFn : ∀ n, F n = fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
      FibreGram (0 : Fin 1) (Hz (zs n)) i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2 := by
    intro n; rw [hF]
  have hRF : ∀ n, RealizableGram (Fin 1 × Fin 1) Γp (F n) := by
    intro n
    obtain ⟨U, hU, hFU⟩ := product_realizable (hadmz (zs n) (hunit n)) hadm₁
    have := sh1_necessity hU
    rwa [hFU, ← hFn n] at this
  have hF1 : F 1 = fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
      FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2 := by
    rw [hFn, hz1, hHz, hHᵢ]
  have c1' : FibreGram (0 : Fin 1) H₁ 1 0 1 * FibreGram (0 : Fin 1) H₁ 0 1 0 = 1 / 16 := by
    rw [mul_comm]; exact c1
  -- the classes of the family are pairwise distinct, and distinct from the two fixed classes
  have hFinj : ∀ n m, GramPhaseEquiv (F n) (F m) → n = m := by
    intro n m h
    have := gramPhaseEquiv_cross_invariant h ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4))
    rw [hFn, hFn, product_cross, product_cross, hcz, hcz, d1] at this
    apply hzinj
    linear_combination (-256 : ℂ) * this
  have hnot11 : ¬ ∃ n, 1 ≤ n ∧ GramPhaseEquiv P₁₁ (F n) := by
    rintro ⟨n, -, h⟩
    have := gramPhaseEquiv_cross_invariant h ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4))
    rw [hFn, hP₁₁, product_cross, product_cross, hcz, c1', d1] at this
    apply hzne1 n
    linear_combination 256 * this
  have hnot1i : ¬ ∃ n, 1 ≤ n ∧ GramPhaseEquiv P₁ᵢ (F n) := by
    rintro ⟨n, -, h⟩
    have := gramPhaseEquiv_cross_invariant h ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4))
    rw [hFn, hP₁ᵢ, product_cross, product_cross, hcz, c1', d1, di] at this
    apply hzne1 n
    linear_combination 256 * this
  have s11i : ¬ GramPhaseEquiv P₁₁ P₁ᵢ := by
    intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4))
    rw [hP₁₁, hP₁ᵢ, product_cross, product_cross, c1, ci, d1] at this
    norm_num [Complex.ext_iff] at this
  -- the shift, read branch by branch
  have hΦe : ∀ t G, Φ t G
      = if h : ∃ n, 1 ≤ n ∧ GramPhaseEquiv G (F n) then F (Nat.find h + 1) else G := by
    intro t G; rw [hΦ]
  have hΦt : ∀ t, Φ t = Φ 0 := fun t => by rw [hΦ]
  have hyes : ∀ t G n, 1 ≤ n → GramPhaseEquiv G (F n) → Φ t G = F (n + 1) := by
    intro t G n hn h
    have hex : ∃ m, 1 ≤ m ∧ GramPhaseEquiv G (F m) := ⟨n, hn, h⟩
    rw [hΦe, dif_pos hex]
    have hspec := Nat.find_spec hex
    rw [hFinj _ _ (gramPhaseEquiv_trans (gramPhaseEquiv_symm hspec.2) h)]
  have hno : ∀ t G, (¬ ∃ n, 1 ≤ n ∧ GramPhaseEquiv G (F n)) → Φ t G = G := by
    intro t G h; rw [hΦe, dif_neg h]
  have hfix11 : ∀ t, Φ t P₁₁ = P₁₁ := fun t => hno t P₁₁ hnot11
  have hfix1i : ∀ t, Φ t P₁ᵢ = P₁ᵢ := fun t => hno t P₁ᵢ hnot1i
  have hshift : ∀ t n, 1 ≤ n → Φ t (F n) = F (n + 1) :=
    fun t n hn => hyes t (F n) n hn (gramPhaseEquiv_refl _)
  -- membership in the family is a property of the class
  have hmem : ∀ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      GramPhaseEquiv G G' → (∃ n, 1 ≤ n ∧ GramPhaseEquiv G (F n)) →
        ∃ n, 1 ≤ n ∧ GramPhaseEquiv G' (F n) :=
    fun G G' h ⟨n, hn, hG⟩ => ⟨n, hn, gramPhaseEquiv_trans (gramPhaseEquiv_symm h) hG⟩
  -- descent and admissibility preservation
  have hd : ∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G') := by
    intro t G G' h
    by_cases hc : ∃ n, 1 ≤ n ∧ GramPhaseEquiv G (F n)
    · obtain ⟨n, hn, hG⟩ := hc
      rw [hyes t G n hn hG, hyes t G' n hn (gramPhaseEquiv_trans (gramPhaseEquiv_symm h) hG)]
      exact gramPhaseEquiv_refl _
    · rw [hno t G hc, hno t G' (fun hc' => hc (hmem G' G (gramPhaseEquiv_symm h) hc'))]; exact h
  have hrel : ∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      RealizableGram (Fin 1 × Fin 1) Γp G → RealizableGram (Fin 1 × Fin 1) Γp (Φ t G) := by
    intro t G hG
    by_cases hc : ∃ n, 1 ≤ n ∧ GramPhaseEquiv G (F n)
    · obtain ⟨n, hn, hG'⟩ := hc
      rw [hyes t G n hn hG']; exact hRF _
    · rw [hno t G hc]; exact hG
  -- L3i: injectivity on classes, by the case split on membership in the family
  have hinj : ∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      RealizableGram (Fin 1 × Fin 1) Γp G → RealizableGram (Fin 1 × Fin 1) Γp G' →
        GramPhaseEquiv (Φ t G) (Φ t G') → GramPhaseEquiv G G' := by
    intro t G G' _ _ h
    by_cases hc : ∃ n, 1 ≤ n ∧ GramPhaseEquiv G (F n)
    · obtain ⟨n, hn, hG⟩ := hc
      by_cases hc' : ∃ m, 1 ≤ m ∧ GramPhaseEquiv G' (F m)
      · obtain ⟨m, hm, hG'⟩ := hc'
        rw [hyes t G n hn hG, hyes t G' m hm hG'] at h
        have hnm : n = m := Nat.succ_injective (hFinj _ _ h)
        subst hnm
        exact gramPhaseEquiv_trans hG (gramPhaseEquiv_symm hG')
      · rw [hyes t G n hn hG, hno t G' hc'] at h
        exact absurd ⟨n + 1, Nat.le_add_left 1 n, gramPhaseEquiv_symm h⟩ hc'
    · by_cases hc' : ∃ m, 1 ≤ m ∧ GramPhaseEquiv G' (F m)
      · obtain ⟨m, hm, hG'⟩ := hc'
        rw [hno t G hc, hyes t G' m hm hG'] at h
        exact absurd ⟨m + 1, Nat.le_add_left 1 m, h⟩ hc
      · rw [hno t G hc, hno t G' hc'] at h
        exact h
  -- the class `[F_1]` is never reached
  have hmiss : ∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      RealizableGram (Fin 1 × Fin 1) Γp G → ¬ GramPhaseEquiv (Φ t G) (F 1) := by
    intro t G _ h
    by_cases hc : ∃ n, 1 ≤ n ∧ GramPhaseEquiv G (F n)
    · obtain ⟨n, hn, hG⟩ := hc
      rw [hyes t G n hn hG] at h
      have := hFinj _ _ h
      omega
    · rw [hno t G hc] at h
      exact hc ⟨1, le_rfl, h⟩
  refine ⟨?_, ?_, ?_, fun t G hG => hrel t G hG, ⟨Φ 0, hΦt⟩, hinj, fun _ n => hRF n, hFinj, hF1,
    hmiss, ?_⟩
  · -- proper
    refine ⟨fun _ => P₁₁, fun _ => P₁ᵢ, fun _ => F 1, fun _ => hR₁₁, fun _ => hR₁ᵢ, fun _ => hRF 1,
      fun t => by rw [hfix11]; exact gramPhaseEquiv_refl _,
      fun t => by rw [hfix1i]; exact gramPhaseEquiv_refl _,
      fun h => s11i (h 0), fun h => ?_⟩
    have := h 0
    rw [hshift 0 1 le_rfl] at this
    have := hFinj _ _ this
    omega
  · -- propagates
    exact ⟨fun G₁ G₂ _ _ h₁ h₂ h0 =>
        (ol1a_descent ((0 : Fin 1), (0 : Fin 1)) (fun _ => Γp) hd).2.1 G₁ G₂ h₁ h₂ h0,
      1, fun _ => P₁₁, fun _ => P₁ᵢ, le_rfl, fun _ => hR₁₁, fun _ => hR₁ᵢ,
      fun t => by rw [hfix11]; exact gramPhaseEquiv_refl _,
      fun t => by rw [hfix1i]; exact gramPhaseEquiv_refl _, s11i⟩
  · -- total
    intro G₀ hG₀
    refine ⟨fun t => (Φ 0)^[t] G₀, ?_, ?_, gramPhaseEquiv_refl _⟩
    · intro t
      induction t with
      | zero => exact hG₀
      | succ n ih =>
        show RealizableGram (Fin 1 × Fin 1) Γp ((Φ 0)^[n + 1] G₀)
        rw [Function.iterate_succ_apply']
        exact hrel 0 _ ih
    · intro t
      show GramPhaseEquiv ((Φ 0)^[t + 1] G₀) (Φ t ((Φ 0)^[t] G₀))
      rw [Function.iterate_succ_apply', hΦt t]
      exact gramPhaseEquiv_refl _
  · -- not L3s, at every t
    intro t h
    obtain ⟨G, hG, hGF⟩ := h (F 1) (hRF 1)
    exact hmiss t G hG hGF

/-! ### Section E — `G4`: the corner, via `Φ_SC`

`Φ_SC`, the self-controlled relabelling, pinned by its statement: at every `t` it applies
`RelabelTransition (Equiv.prodCongr σ 1)`, `σ = (2 3)` on the **first** factor, to a tuple
whose class has a product representative `G(Hᵢ) ⊠ G₂` or `(RelabelTransition σ G(Hᵢ)) ⊠ G₂` with
`G₂` realizable, and fixes every other tuple. The control class and the relabelled factor are the same
factor, and the controlled set is closed under the relabelling. -/

open Classical in
/-- **`G4` — `Φ_SC` at the frozen product configuration: the prefix through `L4d` and `L5` hold,
and `L4n` fails.** The branch condition is a property of the class; descent by
`relabel_gramPhaseEquiv`; `PreservesAdmissible` by `realizable_relabel`; `L2` by construction;
`EvolvesTotally` with the iterates; both conjuncts of `Reversible` because `Φ_SC t ∘ Φ_SC t = id`
exactly, the fired set being closed under the relabelling (`relabel_product`,
`relabel_relabel_symm`); `ProperAt` and `PropagatesFrom` with the constant solutions at
`G(H₁) ⊠ G(H₁)` and `G(H₁) ⊠ G(Hᵢ)` — neither fired, by the product-marginal lemma against act
12's `[G(H₁)] ≠ [G(Hᵢ)]` and act 21's `[G(H₁)] ≠ [σ G(Hᵢ)]` — and the constant trajectory at
`G(Hᵢ) ⊠ G(H₁)` no solution, its image `(σ G(Hᵢ)) ⊠ G(H₁)` inequivalent to it at `((0,0),(2,0))`.
**`L5` holds** with `Φ₁` the conditional single-carrier relabelling — `RelabelTransition σ G₁` when
`G₁ ∼ G(Hᵢ)` or `G₁ ∼ σ G(Hᵢ)`, `G₁` otherwise — and `Φ₂ = id`, both fixed before the inputs; on
the fired branch the two sides are equal tuples by `relabel_product` and `relabel_one`, on the
other branch both are `G₁ ⊠ G₂`, and the branch of `Φ_SC` on a product of realizable tuples is
decided by the first factor through the product-marginal lemma. **`L4n` fails at every `t`**, by
`phiCTRL_census`'s refutation with the roles of the factors exchanged: the weak anchored gauge
`K = diagonal c` with `c (3,0) = −1`, read at the entry `((0,0),(0,0),(2,0))` on a dilation of
`G(Hᵢ) ⊠ G(H₁)` (fired; the entry carried across is `G(Hᵢ)^{(0)}_{03} · G(H₁)^{(0)}_{00} = 1/16`) and
on a dilation of `G(H₁) ⊠ G(H₁)` (not fired; the entry `G(H₁)^{(0)}_{02} · G(H₁)^{(0)}_{00} = 1/16`),
forces `star (c' (0,0)) · c' (2,0)` to be `−1` and `1`. The failing conjunct is the right closure and
right intertwining conjuncts of `TwistedNatural` read together with the lifting obligation; the
separating classes are `[G(Hᵢ) ⊠ G(H₁)]` and `[G(H₁) ⊠ G(H₁)]`. -/
theorem phiSC_corner :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)),
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun _ G => if ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
                ∧ (GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                      FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
                  ∨ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                      RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) Hᵢ)
                        i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
              then RelabelTransition
                (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4))) G
              else G) →
          ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
              (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ
          ∧ (∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t, Φ t = Φ₀)
          ∧ Reversible (Fin 1 × Fin 1) Γ Φ
          ∧ (∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
          ∧ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ
          ∧ (∀ t, ¬ ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ
                → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
              (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
              ∧ (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
              ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨d1, di, c1, ci, ci2, ci3, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  obtain ⟨g02, -, -, -, sC⟩ := gap_separations H₁ Hᵢ hH₁ hHᵢ
  obtain ⟨U₁₁, hU₁₁, hF₁₁⟩ := product_realizable hadm₁ hadm₁
  obtain ⟨U₁ᵢ, hU₁ᵢ, hF₁ᵢ⟩ := product_realizable hadm₁ hadmᵢ
  obtain ⟨Uᵢ₁, hUᵢ₁, hFᵢ₁⟩ := product_realizable hadmᵢ hadm₁
  have hG₁r := sh1_necessity hadm₁
  have hGᵢr := sh1_necessity hadmᵢ
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, ?_⟩
  intro Γ Φ hΓ hΦ
  subst hΓ
  set σ : Equiv.Perm (Fin 4) := Equiv.swap (2 : Fin 4) 3 with hσ
  set τ : Equiv.Perm (Fin 4 × Fin 4) := Equiv.prodCongr σ (1 : Equiv.Perm (Fin 4)) with hτ
  set Γp : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ :=
    Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2 with hΓp
  set G₁ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ := FibreGram (0 : Fin 1) H₁ with hG₁
  set Gᵢ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ := FibreGram (0 : Fin 1) Hᵢ with hGᵢ
  set P₁₁ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => G₁ i.1 j.1 k.1 * G₁ i.2 j.2 k.2 with hP₁₁
  set P₁ᵢ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => G₁ i.1 j.1 k.1 * Gᵢ i.2 j.2 k.2 with hP₁ᵢ
  set Pᵢ₁ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => Gᵢ i.1 j.1 k.1 * G₁ i.2 j.2 k.2 with hPᵢ₁
  have hR₁₁ : RealizableGram (Fin 1 × Fin 1) Γp P₁₁ := by
    have := sh1_necessity hU₁₁; rwa [hF₁₁] at this
  have hR₁ᵢ : RealizableGram (Fin 1 × Fin 1) Γp P₁ᵢ := by
    have := sh1_necessity hU₁ᵢ; rwa [hF₁ᵢ] at this
  have hRᵢ₁ : RealizableGram (Fin 1 × Fin 1) Γp Pᵢ₁ := by
    have := sh1_necessity hUᵢ₁; rwa [hFᵢ₁] at this
  have hΦt : ∀ t, Φ t = Φ 0 := fun t => by rw [hΦ]
  -- the relabelling: an involution preserving the visible family
  have hΓinv : ∀ i j, Γp (τ i) (τ j) = Γp i j := fun i j => by simp [hΓp, hΓ₀]
  have hσs : σ.symm = σ := by rw [hσ, Equiv.symm_swap]
  have hτs : τ.symm = τ := by rw [hτ, Equiv.prodCongr_symm, hσs]; rfl
  have hσσ : ∀ X : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
      RelabelTransition σ (RelabelTransition σ X) = X := by
    intro X
    calc RelabelTransition σ (RelabelTransition σ X)
        = RelabelTransition σ.symm (RelabelTransition σ X) := by rw [hσs]
      _ = X := relabel_relabel_symm _ X
  have hττ : ∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      RelabelTransition τ (RelabelTransition τ G) = G := by
    intro G
    calc RelabelTransition τ (RelabelTransition τ G)
        = RelabelTransition τ.symm (RelabelTransition τ G) := by rw [hτs]
      _ = G := relabel_relabel_symm _ G
  have hτprod : ∀ (X : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
      RelabelTransition τ (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
          X i.1 j.1 k.1 * Y i.2 j.2 k.2)
        = fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
          RelabelTransition σ X i.1 j.1 k.1 * Y i.2 j.2 k.2 := by
    intro X Y; rw [hτ, relabel_product, relabel_one]
  -- the branch condition, a property of the class, closed under the relabelling
  have hdiag : ∀ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂ →
      G₂ 0 0 0 = 1 / 4 := by
    intro G₂ hG₂
    rw [hG₂.2.2.2 0 0, hΓ₀, Matrix.of_apply]
    norm_num
  have hcond : ∀ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      GramPhaseEquiv G G' →
      (∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ (GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
          ∨ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))) →
      ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ (GramPhaseEquiv G' (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
          ∨ GramPhaseEquiv G' (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)) := by
    rintro G G' h ⟨G₂, h2, hh | hh⟩
    · exact ⟨G₂, h2, Or.inl (gramPhaseEquiv_trans (gramPhaseEquiv_symm h) hh)⟩
    · exact ⟨G₂, h2, Or.inr (gramPhaseEquiv_trans (gramPhaseEquiv_symm h) hh)⟩
  have hclos : ∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      (∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ (GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
          ∨ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))) →
      ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ (GramPhaseEquiv (RelabelTransition τ G)
              (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
          ∨ GramPhaseEquiv (RelabelTransition τ G)
              (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)) := by
    rintro G ⟨G₂, h2, hh | hh⟩
    · refine ⟨G₂, h2, Or.inr ?_⟩
      have := relabel_gramPhaseEquiv τ hh
      rwa [hτprod] at this
    · refine ⟨G₂, h2, Or.inl ?_⟩
      have := relabel_gramPhaseEquiv τ hh
      rwa [hτprod, hσσ] at this
  -- the two branches
  have hΦyes : ∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      (∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ (GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
          ∨ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))) →
      Φ t G = RelabelTransition τ G := by
    intro t G h
    simp only [hΦ]
    rw [if_pos h]
  have hΦno : ∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      (¬ ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ (GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
          ∨ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))) →
      Φ t G = G := by
    intro t G h
    simp only [hΦ]
    rw [if_neg h]
  -- the two fixed classes are not fired, and the fired class moves
  have hnot : ∀ X : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, ¬ GramPhaseEquiv X Gᵢ →
      ¬ GramPhaseEquiv X (RelabelTransition σ Gᵢ) →
      ∀ Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, Y 0 0 0 = 1 / 4 →
      ¬ ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ (GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              X i.1 j.1 k.1 * Y i.2 j.2 k.2)
              (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
          ∨ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              X i.1 j.1 k.1 * Y i.2 j.2 k.2)
              (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)) := by
    rintro X hXi hXσ Y hY ⟨G₂, h2, hh | hh⟩
    · exact hXi (gramPhaseEquiv_fst_of_product (m := (0 : Fin 4))
        (by rw [hY, hdiag G₂ h2]) (by rw [hY]; norm_num) hh)
    · exact hXσ (gramPhaseEquiv_fst_of_product (m := (0 : Fin 4))
        (by rw [hY, hdiag G₂ h2]) (by rw [hY]; norm_num) hh)
  have hno11 := hnot G₁ h1i h1move G₁ d1
  have hno1i := hnot G₁ h1i h1move Gᵢ di
  have hΦ11 : ∀ t, Φ t P₁₁ = P₁₁ := fun t => hΦno t P₁₁ hno11
  have hΦ1i : ∀ t, Φ t P₁ᵢ = P₁ᵢ := fun t => hΦno t P₁ᵢ hno1i
  have hfiredᵢ₁ : ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ (GramPhaseEquiv Pᵢ₁ (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
          ∨ GramPhaseEquiv Pᵢ₁ (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)) :=
    ⟨G₁, hG₁r, Or.inl (gramPhaseEquiv_refl _)⟩
  have hΦᵢ₁ : ∀ t, Φ t Pᵢ₁ = fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
      RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₁ i.2 j.2 k.2 := fun t => by
    rw [hΦyes t Pᵢ₁ hfiredᵢ₁, hPᵢ₁, hτprod]
  -- the separation the two standing hypotheses read: `[G(H₁) ⊠ G(H₁)] ≠ [G(H₁) ⊠ G(Hᵢ)]`
  have s11i : ¬ GramPhaseEquiv P₁₁ P₁ᵢ := by
    intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4))
    rw [hP₁₁, hP₁ᵢ, product_cross, product_cross, c1, ci, d1] at this
    norm_num [Complex.ext_iff] at this
  -- descent, admissibility preservation, involution
  have hd : ∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G') := by
    intro t G G' h
    by_cases hc : ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ (GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
          ∨ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
    · rw [hΦyes t G hc, hΦyes t G' (hcond G G' h hc)]
      exact relabel_gramPhaseEquiv τ h
    · rw [hΦno t G hc, hΦno t G' (fun hc' => hc (hcond G' G (gramPhaseEquiv_symm h) hc'))]
      exact h
  have hrel : ∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      RealizableGram (Fin 1 × Fin 1) Γp G → RealizableGram (Fin 1 × Fin 1) Γp (Φ t G) := by
    intro t G hG
    simp only [hΦ]
    split_ifs
    · exact realizable_relabel ((0 : Fin 1), (0 : Fin 1)) _ hΓinv hG
    · exact hG
  have hinv : ∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      Φ t (Φ t G) = G := by
    intro t G
    by_cases hc : ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ (GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
          ∨ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
              RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
    · rw [hΦyes t G hc, hΦyes t _ (hclos G hc), hττ]
    · rw [hΦno t G hc, hΦno t G hc]
  refine ⟨?_, ?_, ?_, fun t G hG => hrel t G hG, ⟨Φ 0, hΦt⟩, ?_, hd, ?_, ?_⟩
  · -- proper
    refine ⟨fun _ => P₁₁, fun _ => P₁ᵢ, fun _ => Pᵢ₁, fun _ => hR₁₁, fun _ => hR₁ᵢ, fun _ => hRᵢ₁,
      fun t => by rw [hΦ11]; exact gramPhaseEquiv_refl _,
      fun t => by rw [hΦ1i]; exact gramPhaseEquiv_refl _,
      fun h => s11i (h 0), fun h => ?_⟩
    have := h 0
    rw [hΦᵢ₁] at this
    exact sC this
  · -- propagates
    exact ⟨fun G₁ G₂ _ _ h₁ h₂ h0 =>
        (ol1a_descent ((0 : Fin 1), (0 : Fin 1)) (fun _ => Γp) hd).2.1 G₁ G₂ h₁ h₂ h0,
      1, fun _ => P₁₁, fun _ => P₁ᵢ, le_rfl, fun _ => hR₁₁, fun _ => hR₁ᵢ,
      fun t => by rw [hΦ11]; exact gramPhaseEquiv_refl _,
      fun t => by rw [hΦ1i]; exact gramPhaseEquiv_refl _, s11i⟩
  · -- total
    intro G₀ hG₀
    refine ⟨fun t => (Φ 0)^[t] G₀, ?_, ?_, gramPhaseEquiv_refl _⟩
    · intro t
      induction t with
      | zero => exact hG₀
      | succ n ih =>
        show RealizableGram (Fin 1 × Fin 1) Γp ((Φ 0)^[n + 1] G₀)
        rw [Function.iterate_succ_apply']
        exact hrel 0 _ ih
    · intro t
      show GramPhaseEquiv ((Φ 0)^[t + 1] G₀) (Φ t ((Φ 0)^[t] G₀))
      rw [Function.iterate_succ_apply', hΦt t]
      exact gramPhaseEquiv_refl _
  · -- reversible, both conjuncts, from the involution
    exact ⟨fun t G G' _ _ h => by have := hd t _ _ h; rwa [hinv, hinv] at this,
      fun t G' hG' => ⟨Φ t G', hrel t G' hG', by rw [hinv]; exact gramPhaseEquiv_refl _⟩⟩
  · -- L5, with the conditional single-carrier relabelling and the identity, fixed before the inputs
    refine ⟨by simp, fun t i j => by simp [hΓp],
      fun _ X => if GramPhaseEquiv X Gᵢ ∨ GramPhaseEquiv X (RelabelTransition σ Gᵢ)
        then RelabelTransition σ X else X,
      fun _ Y => Y, fun t X Y hX hY => ?_⟩
    simp only [Equiv.refl_apply]
    by_cases hc : GramPhaseEquiv X Gᵢ ∨ GramPhaseEquiv X (RelabelTransition σ Gᵢ)
    · have hfired : ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
          ∧ (GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                X i.1 j.1 k.1 * Y i.2 j.2 k.2)
                (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                  Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
            ∨ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                X i.1 j.1 k.1 * Y i.2 j.2 k.2)
                (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                  RelabelTransition σ Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)) := by
        rcases hc with hc | hc
        · exact ⟨Y, hY, Or.inl (product_gramPhaseEquiv_fst Y hc)⟩
        · exact ⟨Y, hY, Or.inr (product_gramPhaseEquiv_fst Y hc)⟩
      rw [hΦyes t _ hfired, hτprod, if_pos hc]
      exact gramPhaseEquiv_refl _
    · have hnf := hnot X (fun h => hc (Or.inl h)) (fun h => hc (Or.inr h)) Y (hdiag Y hY)
      rw [hΦno t _ hnf, if_neg hc]
      exact gramPhaseEquiv_refl _
  · -- not L4n, by the refutation with the roles of the factors exchanged
    intro t
    rintro ⟨Ψ, αL, αR, hlift, -, -, hRclos, -, hR⟩
    obtain ⟨c, hc⟩ : ∃ c : Fin 4 × Fin 4 → ℂ,
        c = fun j => if j = ((3 : Fin 4), (0 : Fin 4)) then -1 else 1 := ⟨_, rfl⟩
    have hcval : ∀ j, c j = 1 ∨ c j = -1 := by
      intro j; rw [hc]; dsimp only; split_ifs <;> simp
    have hcnorm : ∀ j, ‖c j‖ = 1 := by
      intro j; rcases hcval j with h | h <;> simp [h]
    have hcc : ∀ j, c j * star (c j) = 1 := fun j => by
      rw [mul_comm, star_mul_self_eq_norm_sq, hcnorm, one_pow, Complex.ofReal_one]
    have hc00 : c ((0 : Fin 4), (0 : Fin 4)) = 1 := by rw [hc]; simp
    have hc20 : c ((2 : Fin 4), (0 : Fin 4)) = 1 := by rw [hc]; simp
    have hc30 : c ((3 : Fin 4), (0 : Fin 4)) = -1 := by rw [hc]; simp
    set K : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ :=
      Matrix.diagonal (fun p : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) => c p.1) with hK
    have hKc : ∀ (p : (Fin 4 × Fin 4) × (Fin 1 × Fin 1)) (j : Fin 4 × Fin 4),
        K p (j, ((0 : Fin 1), (0 : Fin 1))) = if p = (j, ((0 : Fin 1), (0 : Fin 1))) then c j else 0 := by
      intro p j
      rw [hK, Matrix.diagonal_apply]
      by_cases hp : p = (j, ((0 : Fin 1), (0 : Fin 1)))
      · subst hp; simp
      · simp [hp]
    have hKunit : K ∈ Matrix.unitaryGroup ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ := by
      rw [hK, Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose, Matrix.diagonal_conjTranspose,
        Matrix.diagonal_mul_diagonal]
      ext p q
      rw [Matrix.diagonal_apply, Matrix.one_apply]
      split_ifs with hpq <;> first | rfl | (subst hpq; simp only [Pi.star_apply]; exact hcc p.1)
    have hKw : WeakAnchorStabilizer ((0 : Fin 1), (0 : Fin 1)) K := ⟨hKunit, c, hKc⟩
    obtain ⟨-, c', hc'⟩ := hRclos K hKw
    have hτ00 : τ ((0 : Fin 4), (0 : Fin 4)) = ((0 : Fin 4), (0 : Fin 4)) := by
      simp [hτ, hσ, Equiv.swap_apply_def]
    have hτ20 : τ ((2 : Fin 4), (0 : Fin 4)) = ((3 : Fin 4), (0 : Fin 4)) := by
      simp [hτ, hσ]
    -- the fired branch, read at Uᵢ₁ K and at Uᵢ₁
    have hUyK := weak_preserves_admissible hUᵢ₁ hKw
    have hFyK : FibreGram ((0 : Fin 1), (0 : Fin 1)) (Uᵢ₁ * K)
        = fun i => Matrix.of fun j k => star (c j) * Pᵢ₁ i j k * c k := by
      funext i; ext j k; rw [fibreGram_mul_weak_apply hKc, hFᵢ₁]; rfl
    have hQy : GramPhaseEquiv (fun i => Matrix.of fun j k => star (c j) * Pᵢ₁ i j k * c k) Pᵢ₁ :=
      gramPhaseEquiv_symm ⟨c, hcnorm, fun i j k => rfl⟩
    have E1 := hlift (Uᵢ₁ * K) hUyK
    rw [hR Uᵢ₁ K hKw, hFyK, hΦyes t _ (hcond _ _ (gramPhaseEquiv_symm hQy) hfiredᵢ₁)] at E1
    have E1' := congrFun (congrFun (congrFun E1 ((0 : Fin 4), (0 : Fin 4))) ((0 : Fin 4), (0 : Fin 4)))
      ((2 : Fin 4), (0 : Fin 4))
    rw [fibreGram_mul_weak_apply hc', hlift Uᵢ₁ hUᵢ₁, hFᵢ₁, hΦyes t Pᵢ₁ hfiredᵢ₁] at E1'
    simp only [RelabelTransition, Matrix.submatrix_apply] at E1'
    rw [hτ00, hτ20] at E1'
    simp only [hPᵢ₁, Matrix.of_apply] at E1'
    rw [e3, d1, hc00, hc30, star_one] at E1'
    have hE1 : star (c' ((0 : Fin 4), (0 : Fin 4))) * c' ((2 : Fin 4), (0 : Fin 4)) = -1 := by
      linear_combination 16 * E1'
    -- the identity branch, read at U₁₁ K and at U₁₁
    have hUnK := weak_preserves_admissible hU₁₁ hKw
    have hFnK : FibreGram ((0 : Fin 1), (0 : Fin 1)) (U₁₁ * K)
        = fun i => Matrix.of fun j k => star (c j) * P₁₁ i j k * c k := by
      funext i; ext j k; rw [fibreGram_mul_weak_apply hKc, hF₁₁]; rfl
    have hQn : GramPhaseEquiv (fun i => Matrix.of fun j k => star (c j) * P₁₁ i j k * c k) P₁₁ :=
      gramPhaseEquiv_symm ⟨c, hcnorm, fun i j k => rfl⟩
    have E2 := hlift (U₁₁ * K) hUnK
    rw [hR U₁₁ K hKw, hFnK, hΦno t _ (fun hc' => hno11 (hcond _ _ hQn hc'))] at E2
    have E2' := congrFun (congrFun (congrFun E2 ((0 : Fin 4), (0 : Fin 4))) ((0 : Fin 4), (0 : Fin 4)))
      ((2 : Fin 4), (0 : Fin 4))
    rw [fibreGram_mul_weak_apply hc', hlift U₁₁ hU₁₁, hF₁₁, hΦ11 t] at E2'
    simp only [hP₁₁, Matrix.of_apply] at E2'
    rw [g02, d1, hc00, hc20, star_one] at E2'
    have hE2 : star (c' ((0 : Fin 4), (0 : Fin 4))) * c' ((2 : Fin 4), (0 : Fin 4)) = 1 := by
      linear_combination 16 * E2'
    rw [hE1] at hE2
    norm_num at hE2

/-- **`L5` does not imply `L4n` under the prefix through `L4d` at the frozen product
configuration**, for the ordered decomposition `e = Equiv.refl`: the universal over every
transition family on `Fin 4 × Fin 4` — the first seven conjuncts of act 21's `LadderConds` and
`FactorizesOnProduct` implying the inline `L4n` — is refuted by `Φ_SC`. This is a statement about
the exact declarations at the exact configuration and about nothing in their neighbourhood: it
does not say that `L4n` fails at any other configuration or decomposition, and asserts no
independence of the two rungs. -/
theorem l5_not_implies_l4n :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          ¬ ∀ (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)),
            ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
            ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
                (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
            ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ
            ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ
            ∧ (∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
                → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t, Φ t = Φ₀)
            ∧ Reversible (Fin 1 × Fin 1) Γ Φ
            ∧ (∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
                GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
            → FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
                (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ
            → (∀ t, ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ
                  → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
                (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                  FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
                ∧ (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                  AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
                ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, h⟩ := phiSC_corner
  refine ⟨Γ₀, hΓ₀, fun Γ hΓ hall => ?_⟩
  obtain ⟨h1, h2, h3, h4, h5, h6, h7, h8, hnot⟩ := h Γ _ hΓ rfl
  exact hnot 0 (hall _ ⟨h1, h2, h3, h4, h5, h6, h7⟩ h8 0)

end OrbitLawGaps
end OIBridge

/-! ### The axiom table — one line per named result, printed by the kernel -/

#print axioms OIBridge.OrbitLawGaps.gramPhaseEquiv_fst_of_product
#print axioms OIBridge.OrbitLawGaps.product_gramPhaseEquiv_fst
#print axioms OIBridge.OrbitLawGaps.zero_not_realizable
#print axioms OIBridge.OrbitLawGaps.hadamard_z_admissible
#print axioms OIBridge.OrbitLawGaps.fibreGram_z_entries
#print axioms OIBridge.OrbitLawGaps.zseq_facts
#print axioms OIBridge.OrbitLawGaps.gap_separations
#print axioms OIBridge.OrbitLawGaps.phiMD_l1_restricts
#print axioms OIBridge.OrbitLawGaps.phiPC_l3i_restricts
#print axioms OIBridge.OrbitLawGaps.phiHS_l3s_restricts
#print axioms OIBridge.OrbitLawGaps.phiSC_corner
#print axioms OIBridge.OrbitLawGaps.l5_not_implies_l4n
