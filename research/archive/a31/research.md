# A31 pre-freeze research (read-only). Base: origin/main = d61c6c5409db201e3c25abbf3ec0ecce1f530684

Note: the local ref `main` is stale (b9388cf, an ancestor). Everything below was read at origin/main = d61c6c5.
The draft is origin/claude/a31-off-locus-uniqueness @ ce300b78 (one commit on top of D).

## 1. Off-locus: the exact statement

There is no Lean predicate for the locus. It appears in two places only:

- As an in-proof `set` inside `a28_0_construction` (ProductLocusFreedom.lean:405-406):
  `set Loc := fun G => ∃ X Y, R X ∧ R Y ∧ GramPhaseEquiv (prod X Y) G`
  where `R G := RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G` (:399-400) and
  `prod X Y := fun i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2` (:401-404).
- As the third conjunct of `a28_s_proper` (ProductLocusFreedom.lean:207-217), stated in its negated form:

```lean
theorem a28_s_proper :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
      (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ RealizableGram (Fin 1 × Fin 1)
            (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) G
        ∧ ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
            RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →
              ¬ GramPhaseEquiv
                  (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                    X i.1 j.1 k.1 * Y i.2 j.2 k.2) G
```

Recommended off-locus clause for A31, copied from that form (product first, `G` second):
`∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) G`

The necessary condition for membership is landed as a general lemma. `a28_s_locus_first_index` (:178-191) says
that if `GramPhaseEquiv (X ⊠ Y) G` holds with `X` realizable, then for all `i₁ i₁' i₂ j₁ j₂ k₂`,
`G (i₁, i₂) (j₁, j₂) (j₁, k₂) = G (i₁', i₂) (j₁, j₂) (j₁, k₂)`.

**How many off-locus classes are landed?** Exactly one, and it is opaque. `a28_s_proper` packs its witness
under `∃ G`, so after `obtain` its entries cannot be computed. The concrete witness appears only in the
proof (:219-240): `W := RelabelTransition τ₀ (X ⊠ Y)` with
`τ₀ = Equiv.swap ((0:Fin 4),(1:Fin 4)) ((1:Fin 4),(0:Fin 4))`, `X = FibreGram 0 H₁`, `Y = FibreGram 0 Hᵢ`,
where `H₁` and `Hᵢ` come from `witness_supply`. No landed theorem gives two inequivalent off-locus tuples.
`a29_shared_product_separated` (ProductAdmission.lean:53) gives two inequivalent realizable tuples, but both
are products, so both lie on the locus.

**Product relabellings.** Nothing landed says they preserve the locus or its complement. The claim is true and
easy to prove from landed pieces:
- `relabel_product` (OrbitLawRigidityTwisted.lean:975);
- `relabel_gramPhaseEquiv` (:397);
- `realizable_relabel` (:388, with Γ₀ constant);
- `relabel_relabel_symm` / `relabel_symm_relabel` (:405/:412).

**An obvious second off-locus class, checked with exact Gaussian-integer arithmetic** (scratch `exact.py`):

`W2 := RelabelTransition τ₀ (X ⊠ RelabelTransition σ Y)` with `σ = Equiv.swap (2:Fin 4) 3`.
Also `W2 = RelabelTransition (Equiv.prodCongr 1 σ) W` exactly, because τ₀ and 1×σ commute.

- **Off-locus.** Same indices as a28, fibres (0,1) and (1,1), j=(2,0), k=(2,1). The entries are
  `1/16` and `I/16`, identical to W's, because `Rσ Y 0 0 1 = Y 0 0 1` and `Rσ Y 1 0 1 = Y 1 0 1`.
  The proof is a28_s_proper's computation again, plus the unfolding of `RelabelTransition σ`.
- **`¬ GramPhaseEquiv W W2`.** Fibres (0,0) and (0,2), j=(0,0), k=(0,2). All four indices are τ₀-fixed.
  - `W (0,0)(0,0)(0,2) = W (0,2)(0,0)(0,2) = 1/16`, from `X 0 0 0 · Y 0 0 2` and `X 0 0 0 · Y 2 0 2`.
  - `W2 (0,0)(0,0)(0,2) = 1/16`, but `W2 (0,2)(0,0)(0,2) = X 0 0 0 · Y 3 0 3 = I/16`.
  - The proof pattern is the one in `a28_s_locus_first_index`: equal entries of W force equal entries of W2
    under any common phase `c`, and `1/16 ≠ I/16`. This is a product-level shadow of witness_supply's
    `[G(Hᵢ)] ≠ [Φ_σ G(Hᵢ)]` at (0,2).
- Side facts, both exact: `RelabelTransition (Equiv.prodCongr σ 1)` fixes W and fixes W2.

## 2. The frozen pair

The pair is stated in prose only, never as a Lean term.
- act-28 preregistration.md:295-298: "let `σ = Equiv.swap (2 : Fin 4) (3 : Fin 4)`. Then `f★₁` is the
  bijection of the single-carrier realizable class space induced by `RelabelTransition σ` … and `f★₂` is the
  identity bijection."
- act-29 preregistration.md:378-380 repeats it verbatim.
- act-28 result.md:178-179 restates it.
- `git grep` finds no Lean occurrence of `Equiv.swap (2 : Fin 4) 3` except inside `witness_supply`
  (OrbitLawRigidityTwisted.lean:431 ff).

Faithful Lean rendering in act 28's tuple-map idiom: `f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3)`,
`f₂ = fun G => G` (or `id`).

**No single landed theorem discharges the eight prescribed-pair hypotheses for f★.** Each one is short from
landed lemmas:
- hr₁: `realizable_relabel (0 : Fin 1) σ (by intro i j; rfl or simp) h` (OrbitLawRigidityTwisted.lean:388)
- hd₁: `relabel_gramPhaseEquiv σ` (:397)
- hi₁: `gramPhaseEquiv_of_relabel σ` (:420)
- hs₁: `⟨RelabelTransition σ.symm G', realizable_relabel _ σ.symm _ h, by rw [relabel_symm_relabel]; exact gramPhaseEquiv_refl _⟩` (:412)
- f₂ = id: the realizability hypothesis itself, `id` of the equivalence, and `⟨G', h, gramPhaseEquiv_refl _⟩`.

**A fully eligible law for f★ is already reachable from landed theorems alone:**
`Φa := fun _ => RelabelTransition (Equiv.prodCongr (Equiv.swap (2:Fin 4) 3) 1)`.
- `a29_n_relabel_instance` (ProductAdmission.lean:211) with σ₁ = swap 2 3 and σ₂ = 1 gives conjuncts 3–7,
  FactorizesOnProduct, conjunct 8, and the exact product equation.
- `relabel_one` (OrbitLawRigidityTwisted.lean:986) turns the second factor into `G₂`, which gives the pair clause.
- `a29_p_hold` (ProductAdmission.lean:168) gives conjuncts 1–2.
- Alternatively, `a30_0_admits` (ProductStrictLift.lean:904), applied to the eight hypotheses above, gives an
  opaque eligible Φ.

## 3. The NONUNIQUE route: feasible with landed theorems, and it avoids a28's hidden off-locus values

**Obstacle confirmed.** "a28 fixes every class without a product representative" is only inside the proof of
`a28_0_construction`: `Φ₀ := fun G => if h : Loc G then … else G` at :407-409. The statement at :369-397
exposes existence and properties, not values. The family from `a30_c_lift`, `a30_n_lifts` and
`a30_0_admits` is also opaque, since those statements are existential in Φ. Any route that needs the
base law's off-locus value would have to re-build a28's construction.

**Recommended route: compose on the right with a class transposition.** Right composition needs only the base
law's injectivity (conjunct 6), not its off-locus values.

- Let `Φ` be any eligible law for f★: `Φa` above, or `a30_0_admits`'s. Let `Φh` be its homogeneous value.
- Let `W`, `W2` be two realizable off-locus tuples with `¬ W ≈ W2` (§1).
- In the proof, with `classical`:
  `τ G := if GramPhaseEquiv G W then W2 else if GramPhaseEquiv G W2 then W else G`.
- Properties of τ, each a case split with `gramPhaseEquiv_refl`, `symm` and `trans`:
  - **Realizability.** τ preserves it, because W and W2 are realizable.
  - **Descent on ALL tuples.** Conjunct 7 has no realizability hypothesis, so this matters, and it holds.
  - **Injective and surjective on classes.** `τ (τ G) ≈ G`; this uses `¬ W ≈ W2`.
  - **Fixes the locus.** `τ (X ⊠ Y) = X ⊠ Y` literally for realizable X and Y. If `X ⊠ Y ≈ W`, then W would
    be on the locus, contradicting its off-locus clause. The same holds for W2.
- `Φh ∘ τ` then carries conjuncts 3–7, FactorizesOnProduct (the same Φ₁, Φ₂) and the pair clause:
  - conjunct 3 by iterating, as in a28 :520-530 and a29 :278-290;
  - conjunct 6 injectivity from Φ's L3i plus τ's injectivity;
  - L3s from Φ's L3s plus `τ (τ G₀) ≈ G₀` plus Φ's descent;
  - Fac and the pair clause because τ is the identity on products.
- **Conjunct 8:** `a30_s_strictify` (ProductStrictLift.lean:449) on `Φh ∘ τ` gives `Φ₁` and `Ψ`.
- **Conjuncts 3–7 + Fac + pair for Φ₁:** `a30_t_transfer` (:479).
- **Lift:** `⟨Ψ, id, id, hlift, hadm, rnt1_strict_imp_twisted hstrict⟩` (RepresentativeNaturality.lean:192).
  This is a30_c_lift's own assembly at :663-676, re-done for this Φh, after `subst hΓ` so that `Γ t` reduces
  to `Γ 0`.
- **Conjuncts 1–2:** `a29_p_hold` (ProductAdmission.lean:168).
- **Disagreement at t = 0, G = W.** `Φ 0 W = Φh W`, and `Φ' 0 W = Φ₁ W ≈ Φh (τ W) = Φh W2`.
  If `Φh W ≈ Φ₁ W`, then `Φh W ≈ Φh W2`, and Φ's L3i at t=0 (W and W2 realizable at Γ 0) gives `W ≈ W2`,
  a contradiction. With `Φa = R(σ×1)` the step is even more literal: Φa fixes W and W2 exactly, but
  injectivity via `gramPhaseEquiv_of_relabel` is enough.
- **Nothing in this route needs a28's off-locus values or a28_0_construction's internals.** The new work is:
  1. the explicit witnesses W and W2, with realizability, off-locus and inequivalence. This re-derives a28's
     off-locus computation for W, because `a28_s_proper` is opaque. `a28_s_proper` remains non-vacuity
     provenance and is not the disagreement point;
  2. τ's five properties;
  3. the conjunct bundle for `Φh ∘ τ`;
  4. the strictify, transfer and lift assembly.
- **Route-authorization lesson (a28 DF1).** The freeze must list every consumption:
  - `witness_supply`, `product_realizable`, `sh1_necessity` (or `a28_shared_product_realizable`),
    `realizable_relabel`, `a27_shared_fibreGram_entry` and `a28_s_locus_first_index`;
  - `gramPhaseEquiv_refl/symm/trans`, `relabel_gramPhaseEquiv`, `gramPhaseEquiv_of_relabel`,
    `relabel_symm_relabel`, `relabel_one`;
  - `a29_n_relabel_instance` and/or `a30_0_admits`, and `a29_p_hold`;
  - `a30_s_strictify`, `a30_t_transfer`, `rnt1_strict_imp_twisted`.
  A29's route row for A29-1 (act-29 prereg :524) authorized only A29-0's witness, `a28_s_proper`,
  `a28_s_locus_first_index` and the "universally authorized helpers", so it is too narrow for this route.

**Direct two-law construction alternative.** Strictify both `Φh` and `Φh ∘ τ`. It gains nothing: Φa is already
strictly lifted, since its lift is `RelabelLift`.

## 4. The UNIQUE side

**Structural argument (worth proving or recording as the reason for the prediction).**
- Any eligible law maps locus classes onto locus classes. This follows from the pair clause and f★ being a
  class bijection.
- It is a bijection on realizable classes (conjunct 6).
- So it permutes the off-locus classes.
- Right composition with any locus-fixing class permutation keeps eligibility, with conjunct 8 restored by
  act 30's strictification.
- Hence, at this pair, UNIQUE holds iff there is exactly one off-locus class. W and W2 are two.

**No landed rigidity result forces off-locus values.** Act 21 reached `L-WIDE`, act 26 reached `A26-1-SEVERAL`,
and act 22/23 give only RESTRICTS labels on specific laws.

**Prediction: NONUNIQUE. Strength: very high.** The one computation it rests on — two exact entries, 1/16 vs
I/16 — is checked exactly. UNIQUE is predicted false.

## 5. Consumed declarations (file:line at d61c6c5) and module blobs

ProductLocusFreedom.lean (blob 325c09a180366765ae4d742b752099d3b219d3c9):
- a28_shared_factor_diagonal :56
- a28_s_locus_first_index :178
- a28_s_proper :207 (provenance only)
- a28_shared_product_equiv :286
- a28_shared_product_realizable :304
- a28_0_construction :349 (not needed by the recommended route)

ProductAdmission.lean (90533c832477ad25e8725f20b7759ac71149c251):
- a29_shared_product_separated :53 (not needed)
- a29_p_hold :168
- a29_n_relabel_instance :211

ProductStrictLift.lean (902581e3f33aade4c3366276046a03157248d237):
- a30_shared_strictify :294
- a30_s_strictify :449
- a30_t_transfer :479
- a30_c_lift :561
- a30_c_admit :680
- a30_c_restrict :771
- a30_n_lifts :861
- a30_0_admits :904

OrbitLawRigidityTwisted.lean (860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8):
- EvolvesTotally :96
- PreservesAdmissible :108
- Reversible :123
- FactorizesOnProduct :143
- ol1a_descent :279
- realizable_of_gramPhaseEquiv :355
- realizable_relabel :388
- relabel_gramPhaseEquiv :397
- relabel_relabel_symm :405
- relabel_symm_relabel :412
- gramPhaseEquiv_of_relabel :420
- witness_supply :431
- relabel_product :975
- relabel_one :986
- product_realizable :1015
- product_separations :1093

RepresentativeNaturality.lean (4c1137f35600320b9273c857ec62271341b05cd0):
- StrictNatural :106
- TwistedNatural :128
- RelabelTransition :167
- rnt1_strict_imp_twisted :192

TwoSidedGauge.lean (4bba2040c33424fafbc6d31c0d63b86dff33691a):
- FibreGram :95
- GramPhaseEquiv :102
- RealizableGram :108
- sh1_necessity :168
- sh1_sufficiency :1070

GramTrajectorySelection.lean (afc22cfc93b244c80e1c55a273dcfda1ddebb121):
- gramPhaseEquiv_refl :141
- gramPhaseEquiv_symm :146
- gramPhaseEquiv_trans :162

StrictNaturalLift.lean (038f8e77de14f45790fddba69a4a659522d5fa81):
- a27_shared_fibreGram_entry :20

IntermediateCrossTimeStructure.lean (cb14c43b0becfe1a379ae3615d5553723ede9163):
- ProperAt :167
- PropagatesFrom :186

OIBridge.lean (7a6aaa6cd4011d03932a0c65fe622e6fc521b2c8): its last product import is `import OIBridge.ProductStrictLift` at :219.

## 6. Reserved-name freedom at origin/main

`git grep -l -F` for each of ProductOffLocusUniqueness, act-31, A31- and a31_ returned 0 hits.
`git grep -w A31` also returned 0 hits. The only hit anywhere is the draft preregistration on the A31 branch.

## 7. Recommended frozen shapes (act-30 written-out style; same header convention; f★ bound by equations)

Let `Elig(Φ)` denote exactly P_0's body (ProductStrictLift.lean:924-948) with `Φ` substituted:
ProperAt ∧ PropagatesFrom ∧ EvolvesTotally ∧ PreservesAdmissible ∧ (∃ Φh, ∀ t, Φ t = Φh) ∧ Reversible ∧
descent ∧ (∀ t, ∃ Ψ αL αR, lift ∧ adm ∧ TwistedNatural) ∧ FactorizesOnProduct … ∧ pair clause in f₁ f₂.
The frozen text must write `Elig` out twice. It is not a definition.

P_N (A31-NONUNIQUE):
```
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),
    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
  ∀ (f₁ f₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)),
    f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3) → f₂ = (fun G => G) →
  ∃ Φ Φ' : ℕ → (Fin 4 × Fin 4 → Matrix …) → (Fin 4 × Fin 4 → Matrix …),
    (Elig Φ, written out) ∧ (Elig Φ', written out)
    ∧ ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
        RealizableGram (Fin 1 × Fin 1) (Γ 0) G
        ∧ (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →
            ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                X i.1 j.1 k.1 * Y i.2 j.2 k.2) G)
        ∧ ¬ GramPhaseEquiv (Φ 0 G) (Φ' 0 G)
```

P_U (A31-UNIQUE):
```
∀ Γ₀, Γ₀ = … → ∀ Γ, Γ = … → ∀ f₁ f₂, f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3) → f₂ = (fun G => G) →
  ∀ Φ Φ' : ℕ → …, (Elig Φ) → (Elig Φ') →
  ∀ G, RealizableGram (Fin 1 × Fin 1) (Γ 0) G →
    (∀ X Y, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → ¬ GramPhaseEquiv (X ⊠ Y written out) G) →
    GramPhaseEquiv (Φ 0 G) (Φ' 0 G)
```

Quantifier and scope notes:
- **(a) Time index.** Use t = 0 in both propositions, with realizability at `Γ 0`. This is A29-1's own choice
  (act-29 prereg :385-388), justified by conjunct 5. Do not state UNIQUE with `∀ t`: its negation would
  become `∃ t`, and the two would stop being syntactic negations. Homogeneity makes the forms equivalent,
  but that is a theorem, not syntax.
- **(b) Negations.** Γ₀, Γ, f₁ and f₂ are pinned by equations, so P_N ↔ ¬P_U classically. Freeze a
  corollary `a31_c_exclusive : (P_N) → ¬ (P_U)` as a mechanical duality control. Its proof instantiates
  P_U at P_N's witnesses. Holding both labels is a round failure, as in act 30.
- **(c) Eligibility.** "Eligible" means all eight conjuncts + FactorizesOnProduct + pair clause, with the
  pair clause separate from Fac's own existential Φ₁ and Φ₂ (act 30's P_0 shape). Act 29's
  "eligible family" vocabulary meant conjuncts 3–7 + Fac + pair. The A31 text should call this
  "fully eligible" or "carrying all eight conjuncts" to avoid that collision.
- **(d) Domain of G.** G is existential and is not pinned to a28's witness, as act-29 :390-392 requires.
  The off-locus clause is copied from a28_s_proper, including the equivalence direction `(X ⊠ Y) ≈ G`.
- **(e) f★₂.** Written `fun G => G`. With the equation style, the pair clause text stays byte-identical to
  P_0's, so `a30_0_admits` can be applied after `subst`.
- **(f) Optional stronger form, beyond A29-1's scope.** `∀ Φ, Elig Φ → ∃ Φ', Elig Φ' ∧ ∃ G off-locus,
  ¬ GramPhaseEquiv (Φ 0 G) (Φ' 0 G)`: no fully eligible law is off-locus rigid. The same proof gives it.
  Include it only if the owner wants it, as a separately named target.
- **(g) Elaboration.** Pre-freeze elaboration of P_N, P_U and the corollary should run as act 30 did, as
  design evidence with a countercontrol.
