# K2, Kₙ and operational equivalence — design v2 (after the owner's decisions)

Research and design only. Base: certified main `bcbc516f`, read-only at `scratchpad/eq/base/`.
- Nothing here is adopted, frozen or governed.
- No Lean was built: there is no local toolchain, and every Lean statement below is UNBUILT.
- No F, round, branch, PR, ROADMAP or manuscript change follows from this note.
- v1 is kept as `INTEGRATION-DESIGN.v1.md`.

**What changed from v1.**
1. **Decisions and layers.** The owner's decisions D1–D3 are recorded in §1, and the target is layered as the owner set
   it in §2.
2. **Compactness.** v1 stated it for "any group of reversible maps of an admissible cone", which is false as stated
   (positive scalars; the owner's quadrant example). §4.1 states it for maps preserving the normalization. Theorem A
   already assumes this, so Theorem A is unchanged.
3. **The all-copy statement.** v1 gave a sketch. §5 gives a written proof: a leaf-removal induction for generation, plus
   the chart-compatibility steps across overlapping pairs and idle extensions. It is conditional on Theorem A in group
   form (§4.2).
4. **A cheaper twin witness.** The twin has no type-uniform presentation because the kernel point `idW` is fixed by
   every uniform chart (§3.2).
5. **Formalization design.** §6 covers the Pauli/twin package and the typed IE₂ bridge.

## 1. The owner's decisions (recorded; no premise is adopted)

- **D1 — equivalence.** Operational equivalence with a coherent family of representations, one per token and not one
  per type.
  - The representations preserve states, effects, probabilities, available operations, composition and idle
    extension.
  - The stricter per-type result is kept as a separate theorem identifying the exchange symmetry it needs.
- **D2 — dimension.** The gate route is the primary route to d = 3, and the continuous route continues independently.
  Neither route's assumptions stand in for the other's.
- **D3 — IE₂.** IE₂ is the native idle-extension obligation that corresponds to observational independence.
  - It is an instance or consequence, not an equivalence of definitions.
  - `ObservationalIndependence` is `HasParallelReferenceExtension` on an already matrix-based theory (CGOP:73), so a
    typed bridge from native IE₂ is required (§6.2).

## 2. The target and its layers

**Eventual target (owner):** native operational premises ⟺ finite quantum theory up to operational equivalence.

| layer | statement | status |
|---|---|---|
| (I) conditional | Given a coherent chart family (§3.1): native premises ⟺ the presented theory is finite quantum theory, through `oiPlus_iff_qm` and `typed_determined_iff` | design (§6). Explicitly conditional on chart existence |
| (II-1) one token | Chart existence for one elementary system: F1–F4 (stage → body → ball → d = 3) | kernel pieces; K∞ walls open |
| (II-2) two tokens | Theorem A′, group form (§4.2) | written on exact inputs; IE₁ unsourced |
| (II-3) n tokens | Lemma Kₙ-COPIES (§5) | written proof, conditional on (II-2); exact instances |
| (II-4) every carrier | FP-O (EQ-D Theorem L), and the kernel form EQ-D T1 | written, plus exact at Fin 1–7; FP-O independent |

Layer (I) does not close K∞, K2 or Kₙ (the owner's distinction). They close in layer (II).

## 3. Coherent chart families and the twin

### 3.1 Definition

**The native theory.**
- **Tokens.** Finite token sets S, with native carrier NC_S := (S → Fin 4) → ℝ. These are homogeneous Pauli tables,
  with local tomography (LT) built in.
- **Composites.** A cone K_S ⊆ NC_S, with unit effect u_S (the entry at the all-zero index).
- **Operations.** Available maps g with g(K_S) = K_S and u_S∘g = u_S.
- **Idle extension.** g ↦ g ⊗ id.

**A coherent chart family** gives, for each S, a real-linear isomorphism χ_S : NC_S → Herm(2^S) satisfying:
- (C1) states: χ_S(K_S) = PSD_S;
- (C2) effects: the dual cone and the unit go to {E ≥ 0} and the identity;
- (C3) probabilities: the native pairing equals the trace pairing;
- (C4) operations: χ_S avail_S χ_S⁻¹, complexified, is the presented availability;
- (C5) composition: automatic for conjugation;
- (C6) idle extension: χ_{R⊔S} = χ_R ⊗ χ_S, up to the fixed reindexing. Hence χ(g ⊗ id)χ⁻¹ = (χ g χ⁻¹) ⊗ id.

**For qubit tokens** [written]:
- (C6) reduces each χ_S to a tensor product of single-token charts.
- Each single-token chart sends the unit to the identity (the unit clause of (C2)) and the ball cone onto PSD_2 (C1).
  So it is pauli_1 ∘ hom(ε_s), where ε_s is an affine automorphism of the Euclidean ball. Such an automorphism fixes
  the centre, so it is orthogonal: ε_s ∈ O(3).
- (C3) and (C5) are then automatic, and the cone clause of (C2) follows from (C1) by duality.
- So a coherent chart family is exactly a per-token orthogonal chart, χ_S = pauli_S ∘ ⊗_s hom(ε_s). The substantive
  conditions are (C1) and (C4).

### 3.2 The twin (two tokens)

| fact | statement | evidence |
|---|---|---|
| T1 | The twin `R_B Q3` is presented by the per-token chart (I, R) | exact: pass 1 U2, pass 2 C2. Countercontrol: the same chart does not present Q3 (phiW ↦ idW ∉ Q3) |
| T2 | The twin has no type-uniform presentation | exact: pass 2 C1 (proof below) |
| T3 | Per-token charts of a connected interacting family are unique up to local SO(3) and one global transpose | written (§5, Step 6) |
| T4 | The twin's native exchange is presented as T∘SWAP, which does not extend idly to a third copy | exact: pass 2 C3 (spectrum contains −1/2). Control: Ad SWAP keeps the state PSD |

**T2 in one line.** A uniform chart actC a ∘ actT a with a orthogonal fixes `idW`, because its correlation block
a·I·aᵀ is I; two proper and two improper a were checked exactly. Since `idW` lies in the twin (landed:
`actT_reflY_phiW`), the image of the twin contains `idW`. But pauli(idW) = F/2, with ⟨singlet|F/2|singlet⟩ = −1/2, so
`idW` ∉ Q3. The argument needs neither a reduction to {I, R} nor the SU(2) → SO(3) cover, which makes it kernel-cheap.

### 3.3 The stricter per-type theorem (kept separate, D1)

A type-uniform presentation of an n-token family exists ⟺ every native twist bit vanishes. Any one of the following
suffices:
- **EX + IE₂** at n ≥ 3 (T4);
- **uniform composition** (the EQ-C T6 corollary);
- **CX** (EQ-C T4).

EX alone at two tokens is not enough, because the twin is SWAP-invariant (EQ-C P1.8).

## 4. Compactness and K2

### 4.1 Lemma COMPACT (corrected)

**Statement.**
- Let V be finite-dimensional, u ∈ V*, and K ⊆ V a convex cone.
- Assume the closed normalized slice S = cl K ∩ {u = 1} is bounded and has nonempty interior in the hyperplane
  {u = 1}.
- Let Aut_u(K) = {g ∈ GL(V) : g(K) = K, u∘g = u}. Equivalently, these are the linear maps that act as affine
  automorphisms of the normalized state space.

Then Aut_u(K) ⊆ Aut_u(cl K), and Aut_u(cl K) is compact. So the closure of any subgroup of Aut_u(K) is a compact Lie
group (closed-subgroup theorem).

**Without u∘g = u the lemma fails.** Positive scalars λ·id are automorphisms of every cone. On the positive quadrant,
diag(a, b) with a, b > 0 gives an unbounded group (the owner's example).

**Proof** [written; standard]:
1. g(cl K) = cl K and u∘g = u together give g(S) = S.
2. g fixes the centroid b of S, because an affine bijection of S onto itself preserves its normalized volume measure.
3. Take balls B(b, r) ⊆ S ⊆ B(b, R) in the hyperplane, and write V = ℝb ⊕ ker u. Since g(b) = b and g(ker u) = ker u,
   ‖g‖ ≤ max(1, R/r) in an adapted norm. The same bound holds for g⁻¹.
4. Aut_u(cl K) is closed in GL(V), hence compact. ∎

**Where it applies.**
- Theorem A's maps all preserve u = ω₀₀:
  - `homMap` fixes the unit coordinate, so actC R and actT R fix ω₀₀;
  - the gate or flow maps K ∩ {ω₀₀ = 1} onto itself by hypothesis, and that slice spans, so u∘G = u.
- Admissibility supplies both slice conditions:
  - boundedness, because the slice of `maxCone` is bounded;
  - nonempty interior, because the product hull spans by LT.
- COMP-1's `JointReversible` (CompositeInterface:445) is already of this form: affine maps preserving the normalized
  body.

So Theorem A is unchanged, but every formal statement must carry u∘g = u explicitly.

### 4.2 Theorem A′ (group form)

Assume the hypotheses of Theorem A (EQ-C T3). Step e of the proof (v1 §5.1) establishes more than the cone statement:
the arcwise-connected group H′ is exactly the PU(4)-image or its R_B-conjugate. Here H′ is:
- ⟨L, G L G⁻¹⟩ in the gate case;
- ⟨L, {G_t}⟩ in the flow case.

The proof of §5 uses this group form. Steps a–g of v1 §5.1 stand, with step a read through Lemma COMPACT. For the
primary K2 route (D2), the interaction is the gate route's own native gate: Theorem A(a) for a CtrlGate with the
entangling clause.

## 5. Lemma Kₙ-COPIES — written proof

**Setting.**
- Copies 1..n, each with the 3-ball, and the native carrier V_n = (ℝ⁴)^{⊗n}, with u_n(ω) = ω_{0…0}.
- Local maps act_i(R) for R ∈ SO(3).
- Conditioning: for a pair e = {i, j} and a product effect f = ⊗_{k∉e} f_k on the other copies, c_f : V_n → V_2
  contracts those copies with f.

**Hypotheses.**
- **H1.** K_n is a convex cone. It contains every n-fold product state and is nonnegative on every n-fold product
  effect.
- **H2 (IE₁ at n copies).** act_i(R)(K_n) = K_n for every i and every R ∈ SO(3).
- **H3 (interactions with IE₂ on a spanning tree).** Γ is a spanning tree on {1..n}. For each edge e ∈ Γ, take either:
  - (a) a linear G_e on V_2 with u_2∘G_e = u_2 that maps some pair product to a non-product; or
  - (b) a continuous one-parameter group of such maps, not inside the pair's local group L_e.

  In either case the idle extension G_e ⊗ id maps K_n onto K_n.

**Conclusion.** There is ε ∈ {I, R}ⁿ such that, with χ_ε = pauli_n ∘ ⊗_i hom(ε_i):
1. χ_ε(K_n) = PSD_n;
2. ε is unique up to the global flip ε ↦ εR^{⊗n};
3. the presented edge groups, together with the local maps, generate PU(2ⁿ);
4. for every pair {i, j}, the conditional pair cone is Q3 if ε_i = ε_j and R_B Q3 otherwise. This is the parity rule
   for all pairs.

**Step 0 (conditioning commutes with idle extension, local maps and charts).**
- c_f ∘ (g ⊗ id) = g ∘ c_f for any map g on e.
- c_f ∘ act_k(R) = c_{f′} for k ∉ e, where f′ replaces f_k by f_k∘hom(R), which is still an effect.
- c_f ∘ act_i(R) = act_i(R) ∘ c_f for i ∈ e.
- c_f ∘ χ_ε = (ε_i ⊗ ε_j) ∘ c_{f∘ε} (on Pauli tables), and f ↦ f∘ε is a bijection of the product effects.

So the pair cone of χ_ε(K_n) is (ε_i ⊗ ε_j) applied to the pair cone of K_n. This is the compatibility of the charts
with the pair cones. [linear algebra on disjoint tensor factors]

**Step 1 (pair cones satisfy Theorem A′).** For e ∈ Γ, let K_e be the cone generated by ⋃_f c_f(K_n). Then:
- it is convex by construction;
- it contains the pair products: take f to be the unit effects;
- it lies in max_2, because a pair product effect applied to c_f(ω) is an n-fold product effect applied to ω (H1);
- it is invariant under L_e, by Step 0 and H2;
- it is invariant under G_e and G_e⁻¹, by Step 0 and H3 ("onto");
- u_2∘G_e = u_2.

Lemma COMPACT applies to K_e with u_2, and Theorem A′ gives H′_e = P_e: the PU(4)-image (twist bit τ_e = 0) or its
R_B-conjugate (τ_e = 1).

**Step 2 (idle extension of the pair groups).** L_e ⊗ id (H2) and G_e ⊗ id (H3) preserve K_n, so the group they
generate does too. That group contains H′_e ⊗ id, because g ↦ g ⊗ id is a homomorphism:
(G_e L_e G_e⁻¹) ⊗ id = (G_e⊗id)(L_e⊗id)(G_e⊗id)⁻¹.

**Step 3 (choosing the charts: compatibility across overlapping pairs).**

How conjugation by (ε_i ⊗ ε_j) acts on P_e:
- (I,I) and (R,R) leave P_e unchanged, because R⊗R = T normalizes PU(4) (T Ad_U T = Ad_Ū);
- (I,R) and (R,I) exchange standard and twisted, since R_A PU(4) R_A = R_B PU(4) R_B (because R_A R_B = T).

So edge e becomes standard iff [ε_i ≠ ε_j] = τ_e. Choose the ε as follows:
1. Root Γ at copy 1 and set ε_1 = I.
2. Visit the tree in BFS order and set each child's ε_c so that [ε_p ≠ ε_c] = τ_{pc}.

Every vertex has one parent edge, and every edge condition involves only its two endpoints. A tree has no cycles, so
no condition is over-determined (H¹(tree; ℤ/2) = 0). Each copy carries one chart, which serves every pair containing
it.

After relabelling, K′ = χ_ε(K_n) satisfies:
- H1: χ_ε maps products to products and product effects to product effects;
- H2: χ_ε act_i(R) χ_ε⁻¹ = act_i(ε_i R ε_i), with ε_i R ε_i ∈ SO(3);
- for each e ∈ Γ, the relabelled edge group is (ε_i⊗ε_j) H′_e (ε_i⊗ε_j) ⊗ id = PU(4)_e ⊗ id, standard.

This is compatibility with idle extension (C6): χ_ε(g ⊗ id)χ_ε⁻¹ = (χ g χ⁻¹) ⊗ id, because χ_ε is a tensor product of
per-copy maps.

**Step 4 (generation).**
- The Lie algebra generated by {su(4)_e ⊗ 1 : e ∈ Γ} is su(2ⁿ) (the Generation Lemma below).
- The group H generated by the connected subgroups PU(4)_e ⊗ id is arcwise connected.
- By Yamabe, H is an analytic subgroup. Its Lie algebra contains the generated algebra su(2ⁿ), so H = PU(2ⁿ).
- H preserves K′ (Steps 2 and 3).

**Step 5 (the cone).**
- **Lower bound.** PU(2ⁿ) is transitive on pure states, and K′ contains the pure product states. So K′ contains every
  pure state, and K′ ⊇ PSD_n by convexity.
- **Upper bound.** Suppose ω ∈ K′ has a negative eigenvector v. Choose U with Uv = |0…0⟩. Then Ad_U ω ∈ K′, and the
  product effect |0…0⟩⟨0…0| (a presented native product effect) takes a negative value on it, contradicting H1. So
  K′ ⊆ PSD_n.

**Step 6 (uniqueness).** Suppose two charts satisfying the conclusion differ by δ, up to SO(3)ⁿ. Then δ preserves
PSD_n. If δ_i ≠ δ_j for some pair, take a Bell state on (i, j) tensored with a product state elsewhere: its image has
eigenvalue −1/2. So δ is constant, and δ = R^{⊗n} is the global transpose, an automorphism of the whole quantum theory.

**Step 7 (parity for every pair).** The conditional pair cone of PSD_n is Q3. By Step 0, the pair cone of K_n is
(ε_i⊗ε_j)⁻¹Q3. ∎

**Coherence over all finite composites.** This needs one more native hypothesis.
- **H0 (composite consistency).** For S ⊆ S′, the cone obtained by conditioning K_{S′} on the unit effects of
  S′ ∖ S is K_S. QM satisfies it, through the partial trace.
- **Sub-composites.** Under H0, the chart of a sub-collection is the restriction of χ_ε. Restriction means
  conditioning on unit effects, i.e. the partial trace (Step 0). Without H0, the lemma gives a chart for each K_n
  separately, and nothing ties K_n's charts to the theory's own K_S.
- **Growing families.** Attach each new copy to an earlier one by an interacting edge. With H0, the nested trees give
  charts that agree on initial segments once ε_1 = I is fixed (Step 6).

**Generation Lemma** (leaf-removal induction). Let Γ be a tree on n ≥ 2 vertices. Then the 2-local su(4)'s on the
edges of Γ generate su(2ⁿ).

*Setup.* Let S be the closure of the edge strings under products of anticommuting pairs; the generated algebra is the
real span of iS. This works because [iP, iQ] is 0 when P and Q commute, and is ±2i times a Pauli string when they
anticommute.

*Induction.* The case n = 2 is immediate. For n > 2:
- Let ℓ be a leaf with neighbour p, and let Γ′ = Γ − ℓ.
- By induction, S contains Q ⊗ I_ℓ for every non-identity string Q on the other copies.
- The generators on the edge {p, ℓ} include σ_a(p)σ_b(ℓ) and I⊗σ_b(ℓ).
- It remains to show that S contains Q⊗σ_b(ℓ) for every Q and every b.

*The three cases.*
- **Q = I.** I⊗σ_b(ℓ) is a generator.
- **Q_p ≠ I.**
  - Choose σ_a anticommuting with Q_p. Then Q′ := Qσ_a(p) is not the identity, so Q′⊗I_ℓ ∈ S.
  - Q′⊗I_ℓ and σ_a(p)σ_b(ℓ) anticommute: they anticommute at p only.
  - Their product is ∝ Q⊗σ_b(ℓ).
- **Q_p = I, Q ≠ I.**
  - By the previous case, (Qσ_c(p))⊗σ_{b′}(ℓ) ∈ S.
  - It anticommutes with σ_c(p)σ_{b″}(ℓ) for b″ ≠ b′: they anticommute at ℓ only.
  - Their product is ∝ Q⊗σ_b(ℓ), where b is the third index. Varying b′ and b″ gives every b.

So S contains every non-identity string. ∎

Exact confirmation (pass 2 G):
- For every unlabelled tree with n = 3..7 (1, 2, 3, 6 and 11 trees), the closure is 4ⁿ − 1.
- Countercontrol: every forest obtained by deleting one edge closes exactly at Σ over components with |C| ≥ 2 of
  (4^|C| − 1).

**Status.**
- Written proof, conditional on Theorem A′. The literature imports are Yamabe 1950 and the closed-subgroup theorem
  (standard; unverified, because egress is blocked).
- None of H1–H3 is sourced from field-neutral premises.
- The lemma is chart existence (layer II-3) relative to those hypotheses.

## 6. Formalization design (UNBUILT; for the owner's separate review)

### 6.1 The Pauli/twin package

Module name for design purposes: `OperationalCharts`. It uses only landed vocabulary:
- `W`, `hom`, `homMap`, `prodState`, `pairVal`, `actT`, `actC`, `maxCone`, `phiW` (CompositeDimension);
- `reflY`, `idW`, `actT_reflY_phiW`, `CandidateCone` (K2Guard);
- `transpose_not_inner` (OrientationSelection:239).

```lean
-- §A  Pauli presentation (EQ-E T7)
def pauli1 : Fin 4 → Matrix (Fin 2) (Fin 2) ℂ        -- 0 ↦ 1, 1 ↦ X, 2 ↦ Y, 3 ↦ Z (kernel coordinate order)
noncomputable def pauliW (ω : W 3) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  (1/4 : ℂ) • ∑ μ, ∑ ν, ((ω μ ν : ℝ) : ℂ) • Matrix.kroneckerMap (· * ·) (pauli1 μ) (pauli1 ν)
theorem pauliW_prodState (x y) : pauliW (prodState x y) = Matrix.kroneckerMap (· * ·) (rho x) (rho y)
theorem pauliW_injective : Function.Injective pauliW
def Q3 : Set (W 3) := {ω | (pauliW ω).PosSemidef}
theorem phiW_mem_Q3 : phiW ∈ Q3
theorem candidateCone_Q3 : CandidateCone Q3
-- §B  per-token charts
def IsOrth (a : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop := LinearMap.toMatrix' a * (LinearMap.toMatrix' a)ᵀ = 1
def chart2 (a b) (ω : W 3) : W 3 := actC a (actT b ω)
def PresentedBy (K : Set (W 3)) (a b) : Prop := IsOrth a ∧ IsOrth b ∧ chart2 a b '' K = Q3
-- §C  the twin
def twin : Set (W 3) := actT reflY '' Q3
theorem twin_presentedBy : PresentedBy twin LinearMap.id reflY                   -- T1
theorem chart2_idW {a} (ha : IsOrth a) : chart2 a a idW = idW
theorem idW_not_mem_Q3 : idW ∉ Q3                                                -- singlet, −1/2
theorem idW_mem_twin : idW ∈ twin                                                -- actT_reflY_phiW
theorem twin_not_uniformlyPresented : ¬ ∃ a, PresentedBy twin a a               -- T2
-- §D  the per-type theorem's exchange ingredient
def swapW (ω : W 3) : W 3 := fun μ ν => ω ν μ
theorem chart_swap_twin (ω) : chart2 LinearMap.id reflY (swapW (chart2 LinearMap.id reflY ω))
    = transposeW (swapW ω)                                                       -- T∘SWAP
theorem idleExt_transposeSwap_not_positive :                                     -- T4, three copies
    ∃ ω ∈ Q_ABC, idleExt₁₂ (transposeW ∘ swapW) ω ∉ Q_ABC
```

**Cost.**
- §B–§C are cheap: `fin_cases`, explicit witnesses, and the identity a·aᵀ = 1.
- §A is moderate: Pauli algebra over ℂ, positive semidefiniteness of Kronecker products, and the trace pairing. Whether
  Mathlib has a Kronecker `PosSemidef` lemma at the pin is to be checked.
- §D needs a three-copy table carrier and its Pauli map: cheap to moderate.
- A Lie-free route for the conditional n-copy theorem. If Theorem A′'s conclusion enters as a hypothesis at the group
  level (K_n is invariant under Ad(U ⊗ 1) for every 2-local unitary U on each tree edge), then K_n = PSD_n follows
  from exact universality: every unitary on 2ⁿ levels is a finite product of 2-local unitaries along the tree. The
  route is: two-level decomposition, then the exact Barenco-type decomposition of multi-controlled gates into 2-local
  gates, routed along the tree by 2-local SWAPs. It is exact and standard, but laborious to formalize. Steps 4–5 then
  need no Lie theory; only Theorem A′ itself does.

**Controls** (exact; pass 2):
- T1's chart does not present Q3.
- A non-orthogonal a, such as diag(2, 1, 1), does not fix `idW`. This is to be added as a design control.
- Q3 is uniformly presented, by a = id.
- Ad SWAP extends idly.

### 6.2 The typed IE₂ bridge

```lean
abbrev NC (S : Type) [Fintype S] := (S → Fin 4) → ℝ                              -- native n-token carrier
def idleExt (R S) (g : NC S →ₗ[ℝ] NC S) : NC (R ⊕ S) →ₗ[ℝ] NC (R ⊕ S)          -- g on S-indices, id on R
def chartN (ε : S → (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : NC S →ₗ[ℝ] NC S            -- ⊗ homMap (ε s)
noncomputable def pauliString (idx : S → Fin 4) : Matrix (S → Fin 2) (S → Fin 2) ℂ :=
  Matrix.of fun i j => ∏ s, pauli1 (idx s) (i s) (j s)
noncomputable def presentN (g : NC S →ₗ[ℝ] NC S) :
    Matrix (S → Fin 2) (S → Fin 2) ℂ →ₗ[ℂ] Matrix (S → Fin 2) (S → Fin 2) ℂ      -- complexified conjugation
-- B1  naturality (presentation respects composition, idle extension and charts)
theorem presentN_comp : presentN (g.comp h) = (presentN g).comp (presentN h)
theorem presentN_idleExt : presentN (idleExt R S g) = transportT eRS.symm eRS.symm (amplRefL (R → Fin 2) (presentN g))
theorem chartN_idleExt : chartN (Sum.elim εR εS) ∘ idleExt R S g ∘ (chartN (Sum.elim εR εS))⁻¹
    = idleExt R S (chartN εS ∘ g ∘ (chartN εS)⁻¹)
-- B2  instance-level equivalence (qubit-power carriers, deterministic families)
def NativeIE (availN : ∀ S, Set (NC S →ₗ[ℝ] NC S)) : Prop :=
  ∀ R S g, g ∈ availN S → idleExt R S g ∈ availN (R ⊕ S)
def PresentedIdleClosed (availM : ∀ S, Set (Matrix (S → Fin 2) (S → Fin 2) ℂ →ₗ[ℂ] _)) : Prop :=
  ∀ R S Φ, Φ ∈ availM S → transportT eRS.symm eRS.symm (amplRefL (R → Fin 2) Φ) ∈ availM (R ⊕ S)
theorem nativeIE_iff_presentedIdleClosed :
    NativeIE availN ↔ PresentedIdleClosed (fun S => presentN '' availN S)      -- presentN injective
-- B3  the typed landing
def TypedIdleExtension (𝒯 : TypedOperationalTheory) : Prop :=
  ∀ S S' R O F, 𝒯.availT S S' O F → 𝒯.availT (R × S) (R × S') O (fun a => amplRefL R (F a))
theorem shadow_parallelReferenceExtension (h : TypedIdleExtension 𝒯) (A) :
    HasParallelReferenceExtension (𝒯.shadow A)                                    -- relabel + withSpectator unfolding
theorem typedDiag_typedIdleExtension : TypedIdleExtension typedDiag               -- carries no quantum content
```

Here `eRS` is `Equiv.sumArrowEquivProdArrow`. `withSpectator R e Φ` is definitionally
`transportT e e (amplRefL R Φ)` (ReferenceExtension:422, TypedCompletion:96). So B3 needs only the typed `relabel`
rule.

**B1 — naturality.** Definitional in substance: the Pauli strings of R ⊔ S are tensor products of those of R and S.
The work is the reindexing, and the orthogonality tr(P_a P_b) = 2ⁿδ_ab for general S.

**B2 — instance, not identity of definitions.** It covers only qubit-power carriers and deterministic families.
`HasParallelReferenceExtension` quantifies over every finite spectator and every outcome family; the other carriers
enter only through Kₙ (FP-O).

**B3 — the typed landing.**
- The typed interface (TypedCompletion:165) has no idle-extension rule, so `TypedIdleExtension` is a new predicate.
- It implies `ObservationalIndependence` of every shadow, through the `relabel` rule and the unfolding of
  `withSpectator`.
- `typedDiag` satisfies it: diagonal preservation is stable under amplification. So it adds no quantum content, which
  is the expected outcome for a closure rule.

### 6.3 What the package settles about CX, and what it does not

**Settled at the kernel level** (once built):
- The twin is quantum mechanics under a coherent chart family: T1.
- The per-type theorem's extra content is exactly exchange symmetry: T2, T4.
- Native IE₂ is the deterministic, qubit-power instance of the matrix-side idle extension under any coherent chart
  family: B2.
- Typed idle extension implies `ObservationalIndependence` of every shadow: B3.

**Not settled:** chart existence, i.e. all of layer II.
- Theorem A′ and Lemma Kₙ-COPIES are written proofs. Their hypotheses are IE₁, IE₂ on a tree, and the interactions;
  they contain no exchange premise, and none of them is sourced.
- FP-O remains independent.

So the package shows that CX is removable in layer (I) and in the per-type separation. Its removal in layer (II) rests
on the written Theorem A′ and Lemma Kₙ-COPIES.

### 6.4 Order after the package (as the owner set it)

1. EQ-D T1 `drivesElementary_of_qubit`, with Architecture, ContextStable and LabelInvariant explicit, plus T4
   `cardSplit_independence`.
2. C7b at d = 7.
3. EQ-E T3 `typedKraus_theory`.
4. Last: Theorem A′, first through its exact ingredients as certificates, then the Lie glue (closed-subgroup theorem,
   Yamabe). For the explicit `cnot` and its twin, an elementary KAK route is available.

## 7. Open walls and precautions

- **Layer (I) stays conditional** until chart existence (layer II) and the all-copy extension are proved in the
  kernel, as the owner set it.
- **Compactness** is stated only for maps that preserve the normalization (Lemma COMPACT).
- **IE₁** is unsourced: the composite lift of `driveWords3`. No joint tower exists (CompositeInterface:54-55).
- **Other open walls:**
  - boundary purity at capacity two;
  - a compactness source for FiniteRank;
  - kernel vocabulary for Kₙ's kinematic half;
  - generalized deterministic port-based teleportation (EQ-D T9);
  - balanced d ≡ 1 mod 4 with d ≥ 13.
- **Literature** is unverified throughout, because egress is blocked. The references are Masanes et al. 2014,
  de la Torre et al. 2012, Krumm–Müller 2019, and Yamabe 1950.

## 8. Evidence

| script | sha256 (16) | output sha256 (16) | result |
|---|---|---|---|
| `eqreview/review_jkflow_positivity.py` | 41a2f7724d494475 | 125020018c2258b4 | 8/8 |
| `eqreview/review_integration.py` | 6bfccbc66e7209fc | b31251ea33577f9e | 12/12; replay identical |
| `eqreview/review_pass2.py` | 24316e9c3f28ec7e | 4b58a33e0bb3ff7c | 20/20; replay identical. Run 1 (`review_pass2.run1.*`, e43ceb4a9a1e5b8a / 75e71e3d303fb427) gave 19/20: the test code composed χ∘X∘χ⁻¹ with the wrong chart (a harness error); fixed and re-run |

**Lean read at the base:**
- CGOP:60–207
- OperationalAssembly:585–640
- LevelOneSeam:185–205
- ReferenceExtension:85–100, 405–450
- SpectatorBridge:210–235
- KInfFoundations:270–300
- CompositeDimension:90–235
- K2Guard:40–110
- CompositeInterface:48–60, 440–470
- TypedCompletion:1–60, 150–300, 895–945
