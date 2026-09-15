import OIBridge.HexLatticeGas

/-!
# Hydrodynamics round H-E — H3 as a candidate bridge condition toward closure

Executed under the frozen control plane
`verification/programmes/hydrodynamics/round-h-e-h3-closure-bridge/preregistration.md`, blob
`9f3f4ff4115c8d95215462acd257b4f6b32c9926`, from `main` at
`0975bbab380b26cd2bb06ec65ed68f8bcc23937f` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base.

## The object

Round H-B's frozen streaming-and-collision candidate, consumed unmodified: `hexDir`, `hexCollide`,
`hexStream`, `hexGas`, `hexSubstratum`, `hexSum`, `hexMoment2_eq`, `hexSum_hexStream`,
`hexCollide_conserved_iff`, `hexCollide_conditions_iff_span`, `hexSum_hexGas_iff_span` and
`hexCollide_of_single` are cited and none is re-proved. On top of it this module states **one
candidate bridge condition** against the programme's H3 obligation — the Gibbs family in H-B's
three conserved charges, parameterized by a real triple `(a, b₁, b₂)` through the channel
fugacities `z k = exp (a + b₁ (c k)₁ + b₂ (c k)₂)` — and decides the part of it that is an exact
finite statement.

**H3 is a candidate.** This module does not assert that it is correct, that it is the right shape
of bridge condition, or that its clauses are the weakest with the property; **no extremal claim is
made**, and H3 is not a new condition of the framework but a candidate for an obligation the
programme's ladder already carries.

## What is decided here, and what is not

* **`HE2-a`, product form** — `hexLocalWeight_hexFugacity`: the local Gibbs weight in the three
  charges **is** the channel product.
* **`HE2-b`, the collision** — `hexLocalWeight_hexCollide`: the local weight is constant on
  `hexCollide` orbits, by H-B's integer-weight classification read in the exponent. The frozen
  fallback — a direct 64-state case analysis at real parameters — was **not** used: the real
  parameters multiply integer charges, so H-B's statement transfers by reuse.
* **`HE2-c`, streaming** — `hexConfWeight_hexStream`: for **site-independent** fugacities the
  configuration weight is streaming invariant. **The statement carries "site-independent" and it is
  not dropped anywhere below.**
* **`HE2-d`, family invariance** — `hexConfWeight_hexGas`: for **site-independent** fugacities the
  configuration weight is `Φ`-invariant.
* **`HE2-e`, the flux in the parameters** — `hexFamilyFlux_apply`, `hexFamilyFlux_isotropic`: the
  momentum-flux tensor of a family member over the embedded stencil is a function of the parameter
  triple `(a, b₁, b₂)`, equal to `3 θ δ` at `b₁ = b₂ = 0` through H-B's `hexMoment2_eq`. **This is
  an identity about a family of measures on finite configurations. It is not a stress tensor, not a
  constitutive law, and not a term of any equation**, and **its variable is the parameter triple,
  not the coarse charges**.
* **`HE2-f`, identifiability** — `hexMeanCharge_injective`: the mean-charge map is injective on the
  whole of `ℝ³`, so a triple of mean-charge values names **at most one** parameter triple.
  **Injectivity is all that is established.** The recovery it supplies is defined **on `im Ψ` and
  nowhere else**; the image of the map is **not characterized here**, that characterization is not
  a target of this round, and no statement here places any coarse charge data in the image.
* **`HE4-a`, the non-discrimination bound** — `hexStream_clauses_and_six_invariants`: pure
  streaming, the identity-collision rule, satisfies the same three clauses with the same family and
  preserves the channel-weighted total for **every** weight, where the gas preserves exactly the
  span of mass and the two momentum rows. **This bounds what those clauses supply; it is a finding
  against neither rule.**
* **`HE4-b`, the homogeneity bound** — `hexConfWeight_site_dependent_not_invariant`: with
  **site-dependent** fugacities the configuration weight is not `Φ`-invariant. **So `HE2-d`'s
  invariance is an invariance of the homogeneous family only**, and nothing here is asserted about
  families whose parameters vary from site to site.

**The propagation clause of the candidate condition is not stated and not proved here**, and
nothing in this module is closure: no hydrodynamic limit is taken, no continuum equation is
written, no transport coefficient is named, and no ergodicity, mixing, equidistribution or
propagated local-equilibrium statement is made. The invariance of a family of measures is none of
those things.

**Round H-B is not reported closed by this module**, no label here is a label "for OI", and nothing
here bears on the OI → QM chain, on Bell or on gravity. Nothing here is a statement about `d = 3`,
about any manuscript, or about whether the framework requires a further condition.
-/

namespace OIBridge
namespace HydroClosureBridge

open Finset
open OIBridge.HexLatticeGas

/-! ### Section A — the frozen candidate family, and its product form -/

section Family

/-- **THE CHANNEL FUGACITIES** (budget slot 1) — the frozen candidate family is parameterized by a
real triple `(a, b₁, b₂)` through `z k = exp (a + b₁ (c k)₁ + b₂ (c k)₂)`, with `c k = hexDir k`
H-B's six lattice directions. Every fugacity is strictly positive at every parameter triple, so the
family is defined on the whole of `ℝ³`. -/
noncomputable def hexFugacity (a b₁ b₂ : ℝ) : Fin 6 → ℝ := fun k =>
  Real.exp (a + b₁ * (hexDir k 0 : ℝ) + b₂ * (hexDir k 1 : ℝ))

/-- **THE LOCAL WEIGHT** (budget slot 2) — `∏ k, z k ^ n k`, the weight a channel-fugacity vector
gives one local state, the occupations `n k` being the integer lift `(v k).val` of the Boolean
channel occupation H-B's `hexSum` uses. -/
noncomputable def hexLocalWeight (z : Fin 6 → ℝ) (v : Fin 6 → ZMod 2) : ℝ :=
  ∏ k, z k ^ (v k).val

/-- **THE CONFIGURATION WEIGHT** (budget slot 3) — the product of the local weight over the finite
site type. **The fugacity vector is one vector, the same at every site**: this is the weight of the
*homogeneous* family, and every invariance statement about it below carries that qualifier. -/
noncomputable def hexConfWeight {ι : Type} [Fintype ι] (z : Fin 6 → ℝ)
    (c : ι → Fin 6 → ZMod 2) : ℝ :=
  ∏ i, hexLocalWeight z (c i)

/-- **THE MEAN CHANNEL OCCUPATIONS** (budget slot 4) — `θ k = z k / (1 + z k)`. -/
noncomputable def hexMeanOcc (z : Fin 6 → ℝ) : Fin 6 → ℝ := fun k => z k / (1 + z k)

theorem hexFugacity_pos (a b₁ b₂ : ℝ) (k : Fin 6) : 0 < hexFugacity a b₁ b₂ k :=
  Real.exp_pos _

theorem hexLocalWeight_zero (z : Fin 6 → ℝ) : hexLocalWeight z 0 = 1 := by
  unfold hexLocalWeight
  simp

/-- **`HE2-a` — PRODUCT FORM (`H3-prod`)**: for every parameter triple and every local state, the
Gibbs weight in H-B's three conserved charges **is** the channel product. The charges are written
in H-B's `hexSum` form at a single site: mass with weight `1`, the two momentum components with the
two coordinate rows of `hexDir`. -/
theorem hexLocalWeight_hexFugacity (a b₁ b₂ : ℝ) (v : Fin 6 → ZMod 2) :
    hexLocalWeight (hexFugacity a b₁ b₂) v
      = Real.exp (a * (hexSum (univ : Finset (Fin 1)) 1 (fun _ => v) : ℝ)
          + b₁ * (hexSum (univ : Finset (Fin 1)) (fun k => hexDir k 0) (fun _ => v) : ℝ)
          + b₂ * (hexSum (univ : Finset (Fin 1)) (fun k => hexDir k 1) (fun _ => v) : ℝ)) := by
  unfold hexLocalWeight hexFugacity hexSum
  simp only [Fin.sum_univ_one]
  have hpow : ∀ k : Fin 6,
      Real.exp (a + b₁ * (hexDir k 0 : ℝ) + b₂ * (hexDir k 1 : ℝ)) ^ (v k).val
        = Real.exp (((v k).val : ℝ) * (a + b₁ * (hexDir k 0 : ℝ) + b₂ * (hexDir k 1 : ℝ))) :=
    fun k => (Real.exp_nat_mul _ _).symm
  simp only [hpow, ← Real.exp_sum]
  congr 1
  push_cast
  rw [Finset.mul_sum, Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib,
    ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun k _ => by simp; ring

/-- The three charges of the frozen family are exactly the weights H-B's classification admits:
mass, and the two coordinate rows of `hexDir`. -/
theorem hexCollide_charges (v : Fin 6 → ZMod 2) :
    (∑ k, ((hexCollide v k).val : ℤ) * (1 : Fin 6 → ℤ) k
        = ∑ k, ((v k).val : ℤ) * (1 : Fin 6 → ℤ) k)
    ∧ ∀ j : Fin 2, ∑ k, ((hexCollide v k).val : ℤ) * hexDir k j
        = ∑ k, ((v k).val : ℤ) * hexDir k j := by
  refine ⟨(hexCollide_conserved_iff 1).mpr ⟨by simp, by simp, by simp⟩ v, fun j => ?_⟩
  exact (hexCollide_conserved_iff _).mpr (hexDir_conditions j) v

/-- **`HE2-b` — THE LOCAL WEIGHT IS CONSTANT ON COLLISION ORBITS**: for every parameter triple and
every local state, `∏ k, z k ^ (hexCollide v k).val = ∏ k, z k ^ (v k).val`.

The mechanism is **H-B's collision classification read in the exponent**, reused and not re-proved:
`hexCollide_conserved_iff` is stated for **integer** weights, the frozen family's parameters are
**real**, and the transfer goes through because the real parameters multiply the *integer* charges
— the exponent of the family is `a · m + b₁ · p₁ + b₂ · p₂` with `m`, `p₁`, `p₂` integer-valued.
**The frozen fallback — the direct 64-state case analysis at real parameters — was not used.** -/
theorem hexLocalWeight_hexCollide (a b₁ b₂ : ℝ) (v : Fin 6 → ZMod 2) :
    hexLocalWeight (hexFugacity a b₁ b₂) (hexCollide v)
      = hexLocalWeight (hexFugacity a b₁ b₂) v := by
  obtain ⟨hm, hp⟩ := hexCollide_charges v
  rw [hexLocalWeight_hexFugacity, hexLocalWeight_hexFugacity]
  unfold hexSum
  simp only [Fin.sum_univ_one]
  rw [hm, hp 0, hp 1]

variable (L : ℕ) [NeZero L]

/-- **`HE2-c` — STREAMING INVARIANCE OF THE HOMOGENEOUS WEIGHT**: with the fugacities
**site-independent** — one vector `z`, the same at every site — the configuration weight is
invariant under `hexStream`, by reindexing each channel's site product along the translation
`i ↦ i − c k`. **The "site-independent" qualifier is part of the statement**; `HE4-b` below exhibits
its failure for site-dependent fugacities. -/
theorem hexConfWeight_hexStream (z : Fin 6 → ℝ)
    (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) :
    hexConfWeight z (hexStream L c) = hexConfWeight z c := by
  unfold hexConfWeight hexLocalWeight
  simp only [hexStream_apply]
  rw [Finset.prod_comm]
  conv_rhs => rw [Finset.prod_comm]
  refine Finset.prod_congr rfl fun k _ => ?_
  exact Equiv.prod_comp (Equiv.subRight fun j => (hexDir k j : ZMod L))
    fun i => z k ^ (c i k).val

/-- **`HE2-d` — FAMILY INVARIANCE (`H3-inv`)**: with the fugacities **site-independent**, the
configuration weight of the frozen family is invariant under the gas `Φ = hexGas L`, for every
parameter triple, every configuration and every lattice size. The collision half is `HE2-b`, the
streaming half `HE2-c`.

**The statement is about the homogeneous family.** It is not a local-equilibrium statement for
slowly varying data, it is not ergodicity, mixing or equidistribution, and `HE4-b` bounds it. -/
theorem hexConfWeight_hexGas (a b₁ b₂ : ℝ) (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) :
    hexConfWeight (hexFugacity a b₁ b₂) (hexGas L c)
      = hexConfWeight (hexFugacity a b₁ b₂) c := by
  rw [hexGas_eq, hexConfWeight_hexStream]
  unfold hexConfWeight
  exact Finset.prod_congr rfl fun i _ => hexLocalWeight_hexCollide a b₁ b₂ (c i)

end Family

/-! ### Section B — `HE2-e`: the flux tensor of the family, in the parameters -/

section Flux

/-- **THE FAMILY'S MOMENTUM-FLUX TENSOR** (budget slot 5) — `Σ_k θ_k (u_k)_x (u_k)_y` over the six
embedded unit vectors `u_k = ((c_k)₁ + (c_k)₂/2, (c_k)₂ √3/2)`, the embedding written inline as
H-B writes `hexMoment4`'s.

**Its argument is the parameter triple.** It is an identity about a family of measures on finite
configurations; it is **not** a stress tensor of a continuum theory, **not** a constitutive law,
and **not** a term of any equation. Whether it is a function of the coarse charges is a separate
statement, decided in Section C and nowhere else. -/
noncomputable def hexFamilyFlux (a b₁ b₂ : ℝ) (x y : Fin 2) : ℝ :=
  ∑ k : Fin 6, hexMeanOcc (hexFugacity a b₁ b₂) k
    * (![(hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2, (hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)]
        : Fin 2 → ℝ) x
    * (![(hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2, (hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)]
        : Fin 2 → ℝ) y

/-- **`HE2-e` — THE FLUX IS A FUNCTION OF THE PARAMETERS (`H3-flux`)**: under the family member
`(a, b₁, b₂)` the mean channel occupations are `θ k = z k / (1 + z k)` and the momentum-flux tensor
over the embedded stencil is the stated sum. **The variable of this statement is the parameter
triple `(a, b₁, b₂)` and nothing else.** -/
theorem hexFamilyFlux_apply (a b₁ b₂ : ℝ) (x y : Fin 2) :
    hexFamilyFlux a b₁ b₂ x y
      = ∑ k : Fin 6,
          (Real.exp (a + b₁ * (hexDir k 0 : ℝ) + b₂ * (hexDir k 1 : ℝ))
            / (1 + Real.exp (a + b₁ * (hexDir k 0 : ℝ) + b₂ * (hexDir k 1 : ℝ))))
          * (![(hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2, (hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)]
              : Fin 2 → ℝ) x
          * (![(hexDir k 0 : ℝ) + (hexDir k 1 : ℝ) / 2, (hexDir k 1 : ℝ) * (Real.sqrt 3 / 2)]
              : Fin 2 → ℝ) y := rfl

/-- **`HE2-e`, the isotropic member**: at `b₁ = b₂ = 0` every `θ k` is the common value
`θ = eᵃ / (1 + eᵃ)` and the tensor is `3 θ δ_{xy}`, through H-B's second-moment identity
`hexMoment2_eq`, consumed and not re-proved. **Still a statement in the parameter `a`**, and still
an identity about the family and not a constitutive law. -/
theorem hexFamilyFlux_isotropic (a : ℝ) (x y : Fin 2) :
    hexFamilyFlux a 0 0 x y
      = 3 * (Real.exp a / (1 + Real.exp a)) * (if x = y then 1 else 0) := by
  have hconst : ∀ k : Fin 6, hexMeanOcc (hexFugacity a 0 0) k
      = Real.exp a / (1 + Real.exp a) := by
    intro k
    unfold hexMeanOcc hexFugacity
    norm_num
  unfold hexFamilyFlux
  simp only [hconst, mul_assoc]
  rw [← Finset.mul_sum, hexMoment2_eq]
  ring

end Flux

/-! ### Section C — `HE2-f`: does the mean charge data recover the parameters? -/

section Identifiability

/-- **THE MEAN-CHARGE MAP** (budget slot 6) — `Ψ : ℝ³ → ℝ³`, the expected mass and the two expected
momentum components at one site under the family member `λ = (a, b₁, b₂)`, the momentum components
taken in H-B's lattice coordinates as `hexSum`'s weights `d₁`, `d₂` take them.

**The domain is the whole of `ℝ³`**: no parameter is restricted, no degenerate set is excised, and
no bound is placed on the triple — every fugacity is strictly positive, so every `θ k` lies
strictly between `0` and `1` at every triple. -/
noncomputable def hexMeanCharge (lam : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![∑ k : Fin 6, hexMeanOcc (hexFugacity (lam 0) (lam 1) (lam 2)) k,
    ∑ k : Fin 6, hexMeanOcc (hexFugacity (lam 0) (lam 1) (lam 2)) k * (hexDir k 0 : ℝ),
    ∑ k : Fin 6, hexMeanOcc (hexFugacity (lam 0) (lam 1) (lam 2)) k * (hexDir k 1 : ℝ)]

/-- The mean-charge map written against the three sufficient-statistic vectors
`t k = (1, (c k)₁, (c k)₂)`, written out inline: `Ψ λ = Σ_k σ ⟨t k, λ⟩ · t k` with
`σ x = eˣ / (1 + eˣ)`. -/
theorem hexMeanCharge_apply (lam : Fin 3 → ℝ) (j : Fin 3) :
    hexMeanCharge lam j
      = ∑ k : Fin 6,
          (Real.exp (lam 0 + lam 1 * (hexDir k 0 : ℝ) + lam 2 * (hexDir k 1 : ℝ))
            / (1 + Real.exp (lam 0 + lam 1 * (hexDir k 0 : ℝ) + lam 2 * (hexDir k 1 : ℝ))))
          * (![(1 : ℝ), (hexDir k 0 : ℝ), (hexDir k 1 : ℝ)] : Fin 3 → ℝ) j := by
  fin_cases j <;> simp [hexMeanCharge, hexMeanOcc, hexFugacity]

/-- The logistic function is strictly increasing. -/
theorem hexSigma_strictMono :
    StrictMono (fun x : ℝ => Real.exp x / (1 + Real.exp x)) := by
  intro x y hxy
  have hx : (0 : ℝ) < 1 + Real.exp x := by positivity
  have hy : (0 : ℝ) < 1 + Real.exp y := by positivity
  have hlt : Real.exp x < Real.exp y := Real.exp_lt_exp.mpr hxy
  rw [div_lt_div_iff₀ hx hy]
  nlinarith [Real.exp_pos x, Real.exp_pos y]

theorem hexSigma_mul_nonneg (x y : ℝ) :
    0 ≤ (Real.exp x / (1 + Real.exp x) - Real.exp y / (1 + Real.exp y)) * (x - y) := by
  rcases lt_trichotomy x y with h | h | h
  · have := hexSigma_strictMono h
    nlinarith
  · simp [h]
  · have := hexSigma_strictMono h
    nlinarith

theorem hexSigma_mul_eq_zero (x y : ℝ)
    (h : (Real.exp x / (1 + Real.exp x) - Real.exp y / (1 + Real.exp y)) * (x - y) = 0) :
    x = y := by
  rcases lt_trichotomy x y with hxy | hxy | hxy
  · have := hexSigma_strictMono hxy
    nlinarith
  · exact hxy
  · have := hexSigma_strictMono hxy
    nlinarith

/-- Six reals whose three `t`-weighted sums vanish annihilate every combination of the three
sufficient statistics, the vectors `t k = (1, (c k)₁, (c k)₂)` written out inline. -/
theorem hexSpan_sum_zero (s : Fin 6 → ℝ) (v : Fin 3 → ℝ)
    (h0 : ∑ k : Fin 6, s k * (![(1 : ℝ), (hexDir k 0 : ℝ), (hexDir k 1 : ℝ)] : Fin 3 → ℝ) 0 = 0)
    (h1 : ∑ k : Fin 6, s k * (![(1 : ℝ), (hexDir k 0 : ℝ), (hexDir k 1 : ℝ)] : Fin 3 → ℝ) 1 = 0)
    (h2 : ∑ k : Fin 6, s k * (![(1 : ℝ), (hexDir k 0 : ℝ), (hexDir k 1 : ℝ)] : Fin 3 → ℝ) 2 = 0) :
    ∑ k : Fin 6, s k * (v 0 + v 1 * (hexDir k 0 : ℝ) + v 2 * (hexDir k 1 : ℝ)) = 0 := by
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val_two,
    Matrix.tail_cons, mul_one] at h0 h1 h2
  have hsplit : ∑ k : Fin 6, s k * (v 0 + v 1 * (hexDir k 0 : ℝ) + v 2 * (hexDir k 1 : ℝ))
      = v 0 * (∑ k : Fin 6, s k) + v 1 * (∑ k : Fin 6, s k * (hexDir k 0 : ℝ))
        + v 2 * (∑ k : Fin 6, s k * (hexDir k 1 : ℝ)) := by
    rw [Finset.mul_sum, Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib,
      ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun k _ => by ring
  rw [hsplit, h0, h1, h2]
  ring

/-- **`HE2-f` — THE MEAN CHARGES RECOVER THE PARAMETERS (`H3-ident`)**: the mean-charge map of the
frozen family is injective on the whole of `ℝ³`, so a triple of mean-charge values is produced by
**at most one** parameter triple.

The mechanism: for `v = λ − μ`, `⟨Ψ λ − Ψ μ, v⟩` is a sum of six terms
`(σ ⟨t k, λ⟩ − σ ⟨t k, μ⟩) · ⟨t k, v⟩`, each the product of two quantities of the same sign because
`σ` is strictly increasing; the sum vanishes, so each term does, so `⟨t k, v⟩ = 0` for every `k`;
and `t 0 = (1, 1, 0)`, `t 1 = (1, 0, 1)`, `t 2 = (1, −1, 1)` span `ℝ³`, forcing `v = 0`.

**The statement is injectivity and nothing more.** It does **not** say that a triple of charge
values arising anywhere lies in the image of `Ψ`. The recovery it supplies is therefore defined
**on `im Ψ` and nowhere else**; the image is **not characterized** here, that characterization is
not a target of this round, and no statement of this module extends the recovery by continuity, by
approximation, or by taking a nearest family member. -/
theorem hexMeanCharge_injective : Function.Injective hexMeanCharge := by
  intro lam mu h
  -- the six differences of mean occupations
  set s : Fin 6 → ℝ := fun k =>
    (Real.exp (lam 0 + lam 1 * (hexDir k 0 : ℝ) + lam 2 * (hexDir k 1 : ℝ))
      / (1 + Real.exp (lam 0 + lam 1 * (hexDir k 0 : ℝ) + lam 2 * (hexDir k 1 : ℝ))))
    - (Real.exp (mu 0 + mu 1 * (hexDir k 0 : ℝ) + mu 2 * (hexDir k 1 : ℝ))
      / (1 + Real.exp (mu 0 + mu 1 * (hexDir k 0 : ℝ) + mu 2 * (hexDir k 1 : ℝ)))) with hs
  have hc : ∀ j : Fin 3,
      ∑ k : Fin 6, s k * (![(1 : ℝ), (hexDir k 0 : ℝ), (hexDir k 1 : ℝ)] : Fin 3 → ℝ) j = 0 := by
    intro j
    have hj := congrFun h j
    rw [hexMeanCharge_apply, hexMeanCharge_apply] at hj
    simp only [hs, sub_mul]
    rw [Finset.sum_sub_distrib]
    exact sub_eq_zero.mpr hj
  -- the exponent differences
  have hsum : ∑ k : Fin 6, s k
      * ((lam 0 - mu 0) + (lam 1 - mu 1) * (hexDir k 0 : ℝ)
          + (lam 2 - mu 2) * (hexDir k 1 : ℝ)) = 0 :=
    hexSpan_sum_zero s ![lam 0 - mu 0, lam 1 - mu 1, lam 2 - mu 2] (hc 0) (hc 1) (hc 2)
  have hnn : ∀ k ∈ (univ : Finset (Fin 6)), 0 ≤ s k
      * ((lam 0 - mu 0) + (lam 1 - mu 1) * (hexDir k 0 : ℝ)
          + (lam 2 - mu 2) * (hexDir k 1 : ℝ)) := by
    intro k _
    have := hexSigma_mul_nonneg (lam 0 + lam 1 * (hexDir k 0 : ℝ) + lam 2 * (hexDir k 1 : ℝ))
      (mu 0 + mu 1 * (hexDir k 0 : ℝ) + mu 2 * (hexDir k 1 : ℝ))
    rw [hs]
    convert this using 2
    ring
  have heach := (Finset.sum_eq_zero_iff_of_nonneg hnn).mp hsum
  have hexp : ∀ k : Fin 6,
      lam 0 + lam 1 * (hexDir k 0 : ℝ) + lam 2 * (hexDir k 1 : ℝ)
        = mu 0 + mu 1 * (hexDir k 0 : ℝ) + mu 2 * (hexDir k 1 : ℝ) := by
    intro k
    refine hexSigma_mul_eq_zero _ _ ?_
    have hk := heach k (Finset.mem_univ k)
    rw [hs] at hk
    convert hk using 2
    ring
  have d00 : ((hexDir 0 0 : ℤ) : ℝ) = 1 := by
    rw [show hexDir 0 0 = (1 : ℤ) from by decide]; norm_num
  have d01 : ((hexDir 0 1 : ℤ) : ℝ) = 0 := by
    rw [show hexDir 0 1 = (0 : ℤ) from by decide]; norm_num
  have d10 : ((hexDir 1 0 : ℤ) : ℝ) = 0 := by
    rw [show hexDir 1 0 = (0 : ℤ) from by decide]; norm_num
  have d11 : ((hexDir 1 1 : ℤ) : ℝ) = 1 := by
    rw [show hexDir 1 1 = (1 : ℤ) from by decide]; norm_num
  have d20 : ((hexDir 2 0 : ℤ) : ℝ) = -1 := by
    rw [show hexDir 2 0 = (-1 : ℤ) from by decide]; norm_num
  have d21 : ((hexDir 2 1 : ℤ) : ℝ) = 1 := by
    rw [show hexDir 2 1 = (1 : ℤ) from by decide]; norm_num
  have e0 := hexp 0
  have e1 := hexp 1
  have e2 := hexp 2
  rw [d00, d01] at e0
  rw [d10, d11] at e1
  rw [d20, d21] at e2
  funext j
  fin_cases j
  · show lam 0 = mu 0
    linarith
  · show lam 1 = mu 1
    linarith
  · show lam 2 = mu 2
    linarith

end Identifiability

/-! ### Section D — `HE4`: the two bounds -/

section Bounds

variable (L : ℕ) [NeZero L]

/-- **`HE4-a` — THE NON-DISCRIMINATION BOUND**. The identity-collision rule — pure streaming,
`hexStream L`, with no collision — satisfies the frozen candidate's product-form, invariance and
flux clauses with the **same** frozen family: product form and the flux identity do not mention the
rule at all (`hexLocalWeight_hexFugacity`, `hexFamilyFlux_apply`), and invariance is exactly
`hexConfWeight_hexStream`, which uses no collision. And pure streaming preserves the channel-weighted
total for **every** weight (H-B's `hexSum_hexStream`), where the gas preserves exactly the weights in
the span of mass and the two momentum rows (H-B's `hexSum_hexGas_iff_span`) — in particular the gas
does **not** preserve a single-channel total, with the head-on pair `{0, 3}` at the origin pinned by
equation in the statement.

**This bounds what those three clauses supply. It is a finding against neither rule**: nothing here
says either lacks closure, and nothing here says the candidate condition fails. -/
theorem hexStream_clauses_and_six_invariants (z : Fin 6 → ℝ) :
    (∀ c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2, hexConfWeight z (hexStream L c) = hexConfWeight z c)
    ∧ (∀ w : Fin 6 → ℤ, ∀ c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2,
        hexSum univ w (hexStream L c) = hexSum univ w c)
    ∧ (∀ w : Fin 6 → ℤ,
        (∀ c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2, hexSum univ w (hexGas L c) = hexSum univ w c)
          ↔ ∃ a b₁ b₂ : ℤ, w = fun k => a + b₁ * hexDir k 0 + b₂ * hexDir k 1)
    ∧ ∃ (w : Fin 6 → ℤ) (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2),
        w = ![1, 0, 0, 0, 0, 0]
        ∧ c = Pi.single ![0, 0] ![1, 0, 0, 1, 0, 0]
        ∧ hexSum univ w c = 1
        ∧ hexSum univ w (hexGas L c) = 0
        ∧ hexSum univ w (hexGas L c) ≠ hexSum univ w c := by
  refine ⟨fun c => hexConfWeight_hexStream L z c, fun w c => hexSum_hexStream L w c,
    fun w => hexSum_hexGas_iff_span L w, ⟨![1, 0, 0, 0, 0, 0],
      Pi.single ![0, 0] ![1, 0, 0, 1, 0, 0], rfl, rfl, ?_, ?_, ?_⟩⟩
  · rw [hexSum_single]
    decide
  · rw [hexGas_eq, hexSum_hexStream, collide_single, hexSum_single]
    rw [(hexCollide_moved.1 : hexCollide ![1, 0, 0, 1, 0, 0] = ![0, 1, 0, 0, 1, 0])]
    decide
  · rw [hexGas_eq, hexSum_hexStream, collide_single, hexSum_single, hexSum_single]
    rw [(hexCollide_moved.1 : hexCollide ![1, 0, 0, 1, 0, 0] = ![0, 1, 0, 0, 1, 0])]
    decide

omit [NeZero L] in
/-- The gas on the single-particle configuration of `HE4-b`: single particles do not collide
(H-B's `hexCollide_of_single`), so the particle simply moves one step along `c₀`. -/
theorem hexGas_single_zero :
    hexGas L (Pi.single ![0, 0] ![1, 0, 0, 0, 0, 0])
      = Pi.single (![1, 0] : Fin 2 → ZMod L) ![1, 0, 0, 0, 0, 0] := by
  have hs : ∀ k' : Fin 6, k' ≠ 0 → (![1, 0, 0, 0, 0, 0] : Fin 6 → ZMod 2) k' = 0 := by decide
  have hzero : (![0, 0] : Fin 2 → ZMod L) = 0 := by
    funext j
    fin_cases j <;> rfl
  have hd0 : (fun j => ((hexDir 0 j : ℤ) : ZMod L)) = (![1, 0] : Fin 2 → ZMod L) := by
    funext j
    fin_cases j <;> simp [hexDir]
  funext i k
  rw [hexGas_apply,
    hexCollide_of_single _ 0 fun k' hk' => single_channel_zero _ _ _ _ (hs k' hk')]
  by_cases hk : k = 0
  · subst hk
    rw [hd0, hzero]
    by_cases hi : i = (![1, 0] : Fin 2 → ZMod L)
    · subst hi
      rw [sub_self, Pi.single_eq_same, Pi.single_eq_same]
    · rw [Pi.single_eq_of_ne hi, Pi.single_eq_of_ne (sub_ne_zero_of_ne hi)]
  · have hlhs : (Pi.single (![0, 0] : Fin 2 → ZMod L)
          (![1, 0, 0, 0, 0, 0] : Fin 6 → ZMod 2) : (Fin 2 → ZMod L) → Fin 6 → ZMod 2)
        (i - fun j => (hexDir k j : ZMod L)) k = 0 :=
      single_channel_zero _ _ _ _ (hs k hk)
    have hrhs : (Pi.single (![1, 0] : Fin 2 → ZMod L)
        (![1, 0, 0, 0, 0, 0] : Fin 6 → ZMod 2) : (Fin 2 → ZMod L) → Fin 6 → ZMod 2) i k = 0 :=
      single_channel_zero _ _ _ _ (hs k hk)
    exact hlhs.trans hrhs.symm

/-- **`HE4-b` — THE HOMOGENEITY BOUND**. With **site-dependent** fugacities the configuration
weight is not `Φ`-invariant: for `L ≥ 2`, take the configuration with a single particle in channel
`0` at the origin and the fugacity assignment taking the value `2` at the origin and `1` at every
other site — in particular at the site `c₀`, where the particle arrives. Both configurations and
the assignment are pinned by equation in the statement.

**Consequently `HE2-d`'s invariance is an invariance of the homogeneous family only**, and this
module asserts nothing about families whose parameters vary from site to site — which is the shape a
local-equilibrium statement for a hydrodynamic limit would need. -/
theorem hexConfWeight_site_dependent_not_invariant (hL : 2 ≤ L) :
    ∃ (Z : (Fin 2 → ZMod L) → Fin 6 → ℝ) (c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2),
      Z = (fun i => if i = (![0, 0] : Fin 2 → ZMod L) then (fun _ => (2 : ℝ))
            else (fun _ => (1 : ℝ)))
      ∧ c = Pi.single ![0, 0] ![1, 0, 0, 0, 0, 0]
      ∧ (∏ i, hexLocalWeight (Z i) (c i)) = 2
      ∧ (∏ i, hexLocalWeight (Z i) (hexGas L c i)) = 1
      ∧ (∏ i, hexLocalWeight (Z i) (hexGas L c i)) ≠ ∏ i, hexLocalWeight (Z i) (c i) := by
  classical
  set Z : (Fin 2 → ZMod L) → Fin 6 → ℝ := fun i =>
    if i = (![0, 0] : Fin 2 → ZMod L) then (fun _ => (2 : ℝ)) else (fun _ => (1 : ℝ)) with hZ
  set c : (Fin 2 → ZMod L) → Fin 6 → ZMod 2 :=
    Pi.single ![0, 0] ![1, 0, 0, 0, 0, 0] with hc
  have h10 : (![1, 0] : Fin 2 → ZMod L) ≠ (![0, 0] : Fin 2 → ZMod L) := by
    intro hcon
    have := congrFun hcon 0
    simp at this
    have h1 : (1 : ZMod L) ≠ 0 := by
      have : Fact (1 < L) := ⟨hL⟩
      exact one_ne_zero
    exact h1 this
  have hoff : ∀ k : Fin 6, k ≠ 0 → ((![1, 0, 0, 0, 0, 0] : Fin 6 → ZMod 2) k).val = 0 := by decide
  have hon : ((![1, 0, 0, 0, 0, 0] : Fin 6 → ZMod 2) 0).val = 1 := by decide
  have hbefore : (∏ i, hexLocalWeight (Z i) (c i)) = 2 := by
    rw [Finset.prod_eq_single (![0, 0] : Fin 2 → ZMod L)]
    · have hZ0 : Z (![0, 0] : Fin 2 → ZMod L) = fun _ => (2 : ℝ) := by
        rw [hZ]; simp
      rw [hc, Pi.single_eq_same, hZ0]
      unfold hexLocalWeight
      rw [Finset.prod_eq_single (0 : Fin 6)]
      · rw [hon, pow_one]
      · intro k _ hk
        rw [hoff k hk, pow_zero]
      · intro hcon
        exact absurd (Finset.mem_univ _) hcon
    · intro i _ hi
      rw [hc, Pi.single_eq_of_ne hi, hexLocalWeight_zero]
    · intro hcon
      exact absurd (Finset.mem_univ _) hcon
  have hafter : (∏ i, hexLocalWeight (Z i) (hexGas L c i)) = 1 := by
    rw [hc, hexGas_single_zero L]
    rw [Finset.prod_eq_single (![1, 0] : Fin 2 → ZMod L)]
    · have hZ1 : Z (![1, 0] : Fin 2 → ZMod L) = fun _ => (1 : ℝ) := by
        rw [hZ]; simp [h10]
      rw [Pi.single_eq_same, hZ1]
      unfold hexLocalWeight
      simp
    · intro i _ hi
      rw [Pi.single_eq_of_ne hi, hexLocalWeight_zero]
    · intro hcon
      exact absurd (Finset.mem_univ _) hcon
  exact ⟨Z, c, rfl, rfl, hbefore, hafter, by rw [hafter, hbefore]; norm_num⟩

end Bounds

end HydroClosureBridge
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.HydroClosureBridge.hexFugacity_pos
#print axioms OIBridge.HydroClosureBridge.hexLocalWeight_zero
#print axioms OIBridge.HydroClosureBridge.hexLocalWeight_hexFugacity
#print axioms OIBridge.HydroClosureBridge.hexCollide_charges
#print axioms OIBridge.HydroClosureBridge.hexLocalWeight_hexCollide
#print axioms OIBridge.HydroClosureBridge.hexConfWeight_hexStream
#print axioms OIBridge.HydroClosureBridge.hexConfWeight_hexGas
#print axioms OIBridge.HydroClosureBridge.hexFamilyFlux_apply
#print axioms OIBridge.HydroClosureBridge.hexFamilyFlux_isotropic
#print axioms OIBridge.HydroClosureBridge.hexMeanCharge_apply
#print axioms OIBridge.HydroClosureBridge.hexSigma_strictMono
#print axioms OIBridge.HydroClosureBridge.hexSigma_mul_nonneg
#print axioms OIBridge.HydroClosureBridge.hexSigma_mul_eq_zero
#print axioms OIBridge.HydroClosureBridge.hexSpan_sum_zero
#print axioms OIBridge.HydroClosureBridge.hexMeanCharge_injective
#print axioms OIBridge.HydroClosureBridge.hexStream_clauses_and_six_invariants
#print axioms OIBridge.HydroClosureBridge.hexGas_single_zero
#print axioms OIBridge.HydroClosureBridge.hexConfWeight_site_dependent_not_invariant
