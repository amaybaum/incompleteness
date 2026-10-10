# DRIVE-operation sourcing: RESULT (read-only)

**Base.** `D_DRIVE = 0f2687b7b87925b53c6e3d8c6d1a233f36624dea`, in the detached worktree `scratchpad/wt-drive`.

**What was not done.** No branch, round, preregistration, repository edit or GitHub write.

**Evidence levels.**
- **kernel**: a landed identifier, checked at `D_DRIVE` with file:line.
- **exact**: `drive_checks.py`, which prints `OK -- 28/28 checks, 3 countercontrols expected-false`. It replays
  byte-identically. sha256 of the script `5ddd142e…8a1a`, of the output `a26afc01…a28f530`. It uses sympy, and
  transcendental inequalities only through mpmath interval enclosures.
- **written**: an argument given here.
- **citation**: literature, not in Mathlib.

Paths are under `verification/lean-mathlib/OIBridge/`. Abbreviations:
- CA CompletionAction
- SC StageCompletion
- KF KInfFoundations
- OG OrbitGeneration
- ON OrbitNormalization
- LA LiftAudit
- DC DiscreteCompletion
- SIA SubstratumInterfaceAudit
- IIP InvariantInnerProduct

**Productivity test, fixed before starting (§A.31).** A finding counts as a gem only if both hold:
1. it says something strictly stronger than "DRIVE needs a premise";
2. it either constrains the DRIVE premise or exposes an assumption hidden in the phase-plus-Clifford route.

***

## 0. Verdict

**The route needs a new operational premise.** The phase continuum plus one Clifford operation does not work
cleanly from the existing construction, so no kernel design is proposed. The reasons follow, one per layer.

1. **Operation existence: no.**
   - Main has **no instance of `DirectedStages` or `FiniteStage` built from any OI construction**. The only
     instances are the controls `badD`, `bitTower` (SC) and `midD` (CA); this was checked by search.
   - The only landed operations are the ℂ-matrix channels of `FiniteOperationalTheory`. Two of them are relevant:
     the phases `diagonal_avail` (LA:754) under `SubstratumAvail` (LA:745), and the fixed gate `FixedGateSourced`
     (DC:34).
   - Feeding those channels to OPACT-1 needs a stage tower whose probability table is the trace rule. That
     imports Born structure.
   - **NEW (exact M1–M5):** even granting that tower, the route forces its own body.
     - AffineRespect for the phases and for the Clifford gate, together with visibility of the phases, forces
       the stage effect span to be tomographically complete.
     - The data's `mem_body` then forces the completed body to be **exactly the Bloch ball**.
     - So the matrix route is circular for DRIVE. It is the reverse instance only.

2. **Reversibility: settled once the data exist.**
   - The phase family's inverse data are `T(−θ)`, by the datum-level group law.
   - The Clifford datum is its own inverse, because `H² = 1`.
   - Either way OPACT-1's `inducedEquiv` (CA:333) and `preservesBody_inducedEquiv` (CA:352) apply.

3. **Continuous generation: yes on the completed body, under a premise. The premise can be weakened sharply.**
   - **(Φ)** The phase continuum, given as data, yields a continuous one-parameter action on the chart exactly
     under two conditions:
     - a datum-level group law;
     - continuity in θ of finitely many completed-state probabilities, d(d+1) of them.

     Given OPACT-1, this premise is equivalent to a continuous drive on `chartBody`. It restates DRIVE and is not
     a source.
   - **NEW (Γ):** no continuum premise is needed at all. On a finite-rank completed body:
     - a single reversible AffineRespect datum whose induced map has infinite order generates a continuous
       circle of body automorphisms, by closure;
     - one further datum that does not normalize that circle completes the drive.

     The continuity premise is eliminable. The Clifford operation supplies J and OFF only.
   - **NEW:** a stage-preserving operation always has finite order on a finite-rank completed body. So the
     generator must cross stages: it maps preparations to finer stages, or it is completion-valued.

**Weakest premise found.**
- **OPS-Γ** consists of two reversible, AffineRespect, completion-valued operation data:
  - `g`, whose induced map has infinite order;
  - `J`, satisfying OFF-Γ′: for every m ≥ 1, `J g^m J⁻¹` and `g^m` do not commute on the body.
- It also needs two inputs that are not new: a stage tower `D` from OI, which no landed object supplies, and
  CMP-1's `FiniteRank`.
- OPS-Γ is stated without any flow, parameter or continuity. Via a cited theorem, it is equivalent to body-level
  DRIVE (§2). This is disclosed in the circularity audit (§7).
- For the **operational** drive that V4′ consumes, add **LIMCLOSE-C**: available operation data are closed under
  pointwise probability limits on stage preparations.

***

## 1. Layer 1 — operation existence

### 1.1 What is landed

- `OpDatum`, `AffineRespect` and `StateRespect` are at CA:46, :58 and :53. They act on any `D : DirectedStages`.
- The `DirectedStages` instances at `D_DRIVE` are `badD` (SC:342), `bitTower` (SC:393) and `midD` (CA:404). All
  three are controls.
- `FiniteStage` (KF:63) has no other instances.
- Landed operations exist only in ℂ-typed `FiniteOperationalTheory`:
  - the diagonal phases are available under `SubstratumAvail` (LA:745, LA:754);
  - `permTheory_not_substratumAvail` (SIA:695) shows the observer-sourced theory lacks them;
  - fixed gates: `FixedGateSourced` (DC:34), `fixedGateTheory_fixedGateSourced` (DC:1933),
    `fixedGateTheory_not_qm` (DC:1948).
- None of these is connected to `DirectedStages`. Connecting them requires a table p(e, x) = tr(E_e ρ_x), which
  is Born structure.

### 1.2 The matrix instance: definitions

This is the reverse instance only.

**Stages.** Stage n has:
- preparations: the pure states whose Bloch polar and azimuthal angles lie in (π/2ⁿ)ℤ;
- effects: (1 + u·σ)/2 for u on the same grid, together with 1;
- table: tr(E ρ);
- forward maps: inclusions, which satisfy SC∞.

**Data.** Read each density matrix out as a vector in ℓ^∞ over the labels.
- **Phase datum:** τ_θ x := (a ↦ tr(E_a U_θ ρ_x U_θ†)), with U_θ = diag(1, e^{iθ}).
- **Clifford datum:** τ_H x := (a ↦ tr(E_a H ρ_x H)).

### 1.3 AffineRespect criterion (written, standard; instances exact)

Setting:
- Let W be the real span of the stage effects. It contains 1.
- Let r be the read-out, r(ρ) = (tr(E_a ρ))_a.
- Suppose the preparations span Herm(2).

The criterion:
- A finite relation with Σc = 0 and Σc·prepVec = 0 is exactly an element N = Σc_x ρ_x of W^⊥. Such an N is
  traceless, because 1 ∈ W.
- So AffineRespect(Ad U) ⟺ U W^⊥ U† ⊆ W^⊥ ⟺ R_U(W₀) ⊆ W₀.
  - R_U is the Bloch (adjoint) rotation.
  - W₀ is the traceless part of W.
  - The second equivalence holds because the conjugation is Hilbert–Schmidt orthogonal.

Exact instances on the six-preparation stage {0, 1, ±, ±i}:

| W | phase datum (symbolic θ) | Clifford datum H | the phases on the body |
|---|---|---|---|
| span{1, Z}, the substratum's diagonal read-out | respects (M1) | **fails** (M1) | **identity**: VIS fails (M2) |
| span{1, X, Y, Z} | respects (M3) | respects (M3) | Bloch rotations |

The failure of H with diagonal effects has an explicit witness (M1):
- ρ₊ and ρ₊ᵢ have the same read-out.
- H ρ₊ H and H ρ₊ᵢ H read (1, 1) and (1, 0).

### 1.4 NEW: the route forces tomographic completeness and the Bloch ball (exact M4–M5 + written)

**Step 1: W₀ is forced to be all of ℝ³.**
- W₀ must be invariant under R_z(π/2), which is the S phase, and under R_H.
- R_z(π/2) has characteristic polynomial −(λ−1)(λ²+1), so the xy-plane is irreducible over ℝ (M4). Its
  invariant subspaces are therefore 0, z, xy and ℝ³.
- Of those, only 0 and ℝ³ are R_H-invariant (M4).
- VIS excludes W₀ = 0, so W₀ = ℝ³. The effect span is tomographically complete.
- The discrete Clifford pair {S, H} already forces this. The phase continuum is not needed for it.

**Step 2: the body is forced to be the ball.**
- `mem_body` requires the orbit of a pure preparation under ⟨phases, H⟩ to lie in the body.
- R_H R_z(θ) R_H = R_x(θ) (M5), and R_z(φ) R_x(θ) e_z sweeps the sphere (M5).
- So the body contains the closed ball. It is contained in the read-out of the density matrices.
- Hence **body = Bloch ball**, exactly.

**Consequence.** On this route, DRIVE would deliver the ball at its input. That makes DIM3 and the ellipsoid
trivial, as Thread O found for the availability routes.

***

## 2. Layer 3 — continuous generation (field-neutral)

**Setting.** `D : DirectedStages`, `(body D).Nonempty`, `FiniteRank (body D)`, and `C : CompletionChart D` (CA:144,
`exists_completionChart` CA:154).

### 2.1 Route Φ: the phase continuum as data

**Premises on `T : ℝ → OpDatum D` and `J, J′ : OpDatum D`.**
- **(A)** `AffineRespect (T θ)` for every θ.
  - Written: it suffices for a dense set of θ together with (C). Each relation Σ c_x (T θ).τ x = 0 is
    coordinatewise continuous in θ, and an element of ℓ^∞ is determined by its coordinates.
- **(G)** `(T 0).τ = prepVec D` and `after C (T s) (T t) = T (s + t)`, as τ (CA:305).
- **(C) PROB-CONT.** For every a and x, θ ↦ `coord D a ((T θ).τ x)` is continuous. Only finitely many of these
  functions are needed (§2.2).
- **(R)** `AffineRespect J`, `AffineRespect J′`, `Undoes C J′ J`, `Undoes C J J′` (CA:325).
  - Clifford-type: J′ = J, with `Undoes C J J`.
- **(VIS)** There is t₀ with `T (2t₀)` the identity datum and `(T t₀).τ x ≠ prepVec D x` for some x.
- **(OFF)** There is t such that for every s some x has (J after T t after J′).τ x ≠ (T s).τ x.

**Conclusion (written).** `ElementaryDrivability (chartBody C)` (KF:264), with:
- `flow t := inducedEquiv C (T(−t)) (T t)` (CA:333);
- J := `inducedEquiv C J′ J`.

**Proof, field by field.**
- **Undoes.** From (G): `after C (T(−t)) (T t) = T 0 = prepVec`.
- **flow_add.** From `induced_after` (CA:319) and `induced_unique` (CA:254).
- **flow_preserves, J_preserves, J_symm_preserves.** From `preservesBody_inducedEquiv` (CA:352).
- **flow_continuous.** §2.2.
- **N_involutive, N_moves and J_off_axis are decidable on stage preparations.**
  - Two affine maps of the chart are equal iff they agree on every `gen x` (`induced_unique`).
  - Every `gen x` lies in `chartBody`.
  - So a body-level difference exists iff a difference exists at some stage preparation, read
    **completion-valued**.

**Converse (written).** Every `ElementaryDrivability (chartBody C)` arises this way. Take
τ_t x := chart(flow t (gen x)). Its AffineRespect is `affineRespect_of_induced` (CA:264).

**Consequence.** Given OPACT-1, premise Φ is **equivalent** to a continuous drive on the chart. It is DRIVE in
datum form, not a source. This confirms Thread O §2 D-2.

### 2.2 The continuity argument in chart coordinates (written; exact illustration C1)

1. **An affine basis of generators.** `affineSpan_gen` (CA:218) gives `affineSpan (range (gen C)) = ⊤` in the
   finite-dimensional space ℝ^d. So some x₀ … x_d have `gen x_k` forming an affine basis.
2. **Finitely many labels coordinatize the chart.** The coordinate functionals `coord D a` are point evaluations
   on ℓ^∞, so they separate points of the finite-dimensional direction space F = range C.L. Hence some labels
   a₁ … a_d make v ↦ (v a_j)_j injective on F. This gives a fixed invertible affine map κ with
   coordsOf v = κ⁻¹((coord a_j v)_j) on the span.
3. **The induced map is a fixed combination of probabilities.**
   - `induced C (T θ)` is the unique affine map sending gen x_k ↦ coordsOf((T θ).τ x_k).
   - Its matrix entries are fixed linear combinations, through the inverse basis matrix, of the d(d+1) numbers
     coord a_j ((T θ).τ x_k).
   - These are probabilities of stage effects on **completed** states.
4. **Hence the equivalence.** θ ↦ induced(T θ) is continuous iff those d(d+1) functions are continuous. That in
   turn is equivalent to (C) for all a and x, since every `coord a` is affine in the chart on the span. Joint
   continuity in (t, w) follows in finite dimension.
5. **Exact illustration (C1).** On the ball tower, the chart matrix of R_z(θ) is reconstructed from its 12
   probabilities by a fixed rational formula. The datum-level group law holds on those 12 probabilities (C2).
6. **FiniteRank is essential (X-FR).**
   - Take a product of disks, with block N rotating at frequency N.
   - Every coordinate is continuous.
   - At t = π/N block N is displaced by 2, so sup-norm continuity fails at 0. There is no chart.

### 2.3 Route Γ: one infinite-order operation; the continuum comes from the completion

**Written + citation.** The decisive facts:

- **Γ0. chartBody is compact with nonempty interior.**
  - It is bounded: body coordinates lie in [0, 1], and an injective linear chart from finite dimension is bounded
    below.
  - It is closed, since it is a preimage of a closed set.
  - Its interior is nonempty: it is convex with `affineSpan = ⊤` (CA:218).
  - IIP's `isCompact_bodyR` and `interior_bodyR_nonempty` need `[FiniteDimensional ℝ V]`. They do **not** apply
    to V = ℓ^∞, so a new lemma is needed.
- **Γ1. Aut(chartBody) is a compact group.**
  - It is the group of affine equivalences preserving the body in both directions.
  - Linear parts are bounded by 2R/r, where B(c, r) ⊆ K ⊆ B(0, R).
  - It is closed, because limits of inverses also preserve K.
  - This is elementary: no inner product and no Haar measure.
- **Γ2. The closure contains a circle.**
  - Let g = `inducedEquiv` of an infinite-order datum. A = closure⟨g⟩ is an infinite compact abelian subgroup of
    GL(d+1).
  - By Cartan's closed-subgroup theorem it is a Lie group of positive dimension. Its identity component T₀ is a
    torus (citation).
  - A primitive circle S : ℝ → T₀ with period 1 gives S(1/2) involutive and nontrivial.
  - S(1/2) moves a point of K, because K affinely spans.
  - So D1–D8 hold.
- **Γ3. OFF.**
  - If J does not normalize T₀, some circle in T₀ is not normalized. That gives D9: two distinct maps differ on
    the spanning K.
  - **OFF-Γ′ is sufficient and discrete:** for every m ≥ 1, J g^m J⁻¹ does not commute with g^m.
    - Proof of sufficiency: if J normalized T₀, take m = [A : T₀]. Then g^m ∈ T₀ and J g^m J⁻¹ ∈ T₀, which
      commute.
- **Γ4. The circle members are OPACT-1 data.**
  - τ_t x := chart(S t (gen x)) lies in the body.
  - It satisfies AffineRespect (`affineRespect_of_induced`).
  - S(−t) is its inverse datum.
  - They are completion-valued (§3).
- **Exact illustration on the control.** g = R_z(1) radian.
  - g^355 = R_z(π + δ) and g^710 = R_z(δ′), with 0 < δ, δ′ < 10⁻⁴, by interval arithmetic (G1).
  - J = R_H gives OFF-Γ′ for m = 1 … 40 (G2).
  - Finite order gives no flow (G3).

**Converse (written).** DRIVE ⇒ OPS-Γ.
- N is involutive and moves a state, so the flow has a minimal period p > 0.
- g := flow(p√2) has infinite order, and closure⟨g⟩ is the flow circle.
- J_off_axis is exactly the statement that J does not normalize that circle.

**So, on a finite-rank completed body:**
- D1–D8 ⟺ Aut(chartBody) is infinite ⟺ some reversible AffineRespect datum has infinite order.
- D9 ⟺ non-normalization.

**Kernel cost.**
- To my knowledge Mathlib has no Cartan theorem. This was not checked locally, because there is no Mathlib
  checkout here.
- The cheap kernel path would orthogonalize through IIP-1's `invariant_inner_product_span` (IIP:455) and then use
  Kronecker density (`dense_angles` DC:518 covers one block). The circularity rule excludes that path.

### 2.4 The countable form: a dyadic square-root tower (written)

**Premise.** Data g_n with:
- g₀ = id;
- g₁ moves a state;
- after(g_{n+1}, g_{n+1}) = g_n;
- continuity at the identity: coordinatewise, g_n.τ x → prepVec x.

**Conclusion.** These give a homomorphism from the dyadic rationals into Aut(chartBody), continuous at 0, which
extends uniquely to a continuous ℝ-flow. The members at non-dyadic times are completion-valued.

**Necessity of the continuity premise (X-CONT, exact; no choice).** The branch tower is a square-root tower with
g₀ = 1 and g₁ = NOT whose every g_n (n ≥ 1) sits at an angle in [π/2, 3π/2]. It has no continuous extension. The
regular tower is the control.

***

## 3. The distinction: completed body versus stage preparations and effects

1. **Countable no-go.** This is written; it is the OPACT design constraint 1, re-verified.
   - Suppose the stage index is countable.
   - Then any probability-continuous ℝ-family that maps preparations to preparations, or stage effects to stage
     effects, is constant.
2. **NEW: stage-preserving ⇒ finite order (written; kernel-cheap).**
   - The claim: if T is Prep-valued and maps each finite P_i into itself, its induced map has finite order on a
     finite-rank body.
   - Proof:
     - Finitely many preparations x₀ … x_d affinely span.
     - Each orbit Tⁿ x_k lies in the finite P_{i_k}.
     - So T^N fixes all of them for N the lcm of the orbit lengths.
     - Then induced^N = id by uniqueness.
   - No SC∞ and no naturality are used.
   - **Consequence:** OPACT-D operations (NATDUAL) can never generate a drive, not even by closure. The generator
     of a drive must cross stages.
3. **Generators can be Prep-valued; flow members cannot.**
   - On the 1-radian tower, stage n holds the equatorial preparations at angles k, |k| ≤ n.
   - g = R_z(1) maps stage n into stage n+1, so it is Prep-valued (N2).
   - The NOT = R_z(π) of its closure maps **no** preparation to a preparation: checked for |k| ≤ 50 with interval
     arithmetic (N1), and in general because π is irrational.
   - By cardinality, the flow member at all but countably many t leaves `range prepVec`.
   - On the effect side, `isEffectOn_pullback` (CA:364) makes each pullback a completed effect. It is a stage
     effect for at most countably many t.
4. **Design consequence.** DRIVE must be typed with completion-valued flow members, as OPACT-1 provides. Its
   generators may be stage operations only if they cross stages. EFFCLOSE must range over completed effects.

***

## 4. Dependency chain

```
[D : DirectedStages from OI]                                      MISSING (no instance; only controls SC:342, SC:393, CA:404)
[FiniteRank (body D)]                                             open premise (CMP-1 vocabulary SC:299)
  → exists_completionChart CA:154 → C : CompletionChart D
[OPS-Γ: g, g′, J, J′ : OpDatum D, AffineRespect, Undoes both ways] new premise
  → inducedEquiv CA:333, preservesBody_inducedEquiv CA:352         (kernel)
  → chartBody compact, interior nonempty (Γ0)                      NEW lemma (written; IIP's bodyR lemmas need finite-dim V)
  → Aut(chartBody) compact (Γ1)                                    written
  → closure⟨g⟩ ⊇ circle S (Γ2)                                     citation (Cartan; compact connected abelian = torus)
  → OFF-Γ′ ⇒ D9 (Γ3)                                               written
  ⇒ ElementaryDrivability (chartBody C)                            KF:264 (target)
  ⇒ flow members as data: affineRespect_of_induced CA:264, induced_mem CA:300, isEffectOn_pullback CA:364
  ⇒ preservesBody_driveWords ON:107 (kernel), into OG-1's chain
[+ LIMCLOSE-C]  ⇒ operational availability of the flow members (for V4′ / Thread O D-1)

Route Φ (equivalent to DRIVE given OPACT-1):
  (A)(G)(C)(R)(VIS)(OFF) → induced_after CA:319, induced_unique CA:254, comp_eq_id CA:328,
  inducedEquiv CA:333, preservesBody_inducedEquiv CA:352, affineSpan_gen CA:218 (continuity, §2.2)
  ⇒ ElementaryDrivability (chartBody C)

Matrix instance (reverse only):
  SubstratumAvail LA:745 / diagonal_avail LA:754 + Clifford gate + trace-rule tower (Born, imported)
  ⇒ AffineRespect + VIS force W = Herm(2), body = Bloch ball (§1.4)
```

Not used: `SCInf`, `BinaryVisible`, `sharpSeed_completion`, anything of IIP-1, `ball3`/`ball4` as premises, NB-1,
`elementaryDrivability_of_substratum`, P2 and EFFCLOSE.

***

## 5. Countermodels, one for each new premise

| premise | model | what breaks | evidence |
|---|---|---|---|
| a stage tower from OI | main at `D_DRIVE` | no OI instance exists, so nothing can be stated | kernel (search; controls only) |
| AffineRespect (generator) | diagonal read-out with H | no induced map: ρ₊ ~ ρ₊ᵢ, but the images differ | exact M1; kernel `midOp_not_affineRespect` CA:461 |
| reversibility (inverse datum) | reset to the centre | affine, maps the body in, not injective | exact X-INV (OPACT E7) |
| VIS | diagonal read-out with the phases | the phases respect affine relations but act as the identity on the body | exact M2 |
| infinite order (Γ) | R_z(2π/3); H; any stage-preserving datum | the closure is finite, so no flow | exact G3; §3.2 written |
| OFF | disk: every J ∈ O(2) normalizes SO(2) | D9 fails | exact X-OFF |
| group law (Φ) | θ ↦ R_z(θ²) | continuous and AffineRespect, but not additive | exact X-LAW |
| continuity (Φ, dyadic) | the branch square-root tower | no continuous extension | exact X-CONT |
| continuity (Φ, ℝ) | Hamel: R_z(πφ(t)) with φ additive and ℚ-valued | every field except continuity | written (choice) |
| FiniteRank | product of disks with frequencies N | there is no chart and coordinate continuity is not norm continuity | exact X-FR |
| LIMCLOSE-C (operational only) | `fixedGateTheory α` | dense, countable, no available flow, not QM | kernel DC:1933, DC:1948 |

***

## 6. Circularity audit

Premises of OPS-Γ: `D`, nonemptiness, `FiniteRank`, `C`, the data `g, g′, J, J′` with AffineRespect and Undoes,
infinite order, and OFF-Γ′.

| excluded item | verdict |
|---|---|
| **DIM3** | Absent. `FiniteRank` allows any d. The B⁴ drive (R_z ⊕ 1, J ⊕ 1) satisfies OPS-Γ (Thread O F1–F3). |
| **Ellipsoid or ball** | Absent. B³ × [−1, 1] satisfies OPS-Γ (g = R_z(1) ⊕ id, J = R_H ⊕ id) and is not an ellipsoid. The ball enters only as a joint-satisfiability control and in the matrix reverse instance. |
| **IIP conclusions** | Not used. Γ1 needs no inner product. Γ2 is a citation, not IIP-1. The IIP shortcut is identified and excluded. IIP's `bodyR` lemmas do not even apply (finite-dimensional V). |
| **Born structure** | Absent from the field-neutral statements. FiniteStage tables are arbitrary. Born enters only the matrix instance, which §1.4 shows is circular. |
| **Equivalence to DRIVE** | Premise Φ is DRIVE in datum form (§2.1), so it is **not** a source. OPS-Γ mentions no flow, parameter or continuity. It is equivalent to body-level DRIVE only through Cartan (§2.3), so it is a characterization, not a restatement. It does not by itself say where g and J come from. |
| **SC∞, BinaryVisible, P2, EFFCLOSE** | Not used. |

***

## 7. Classification (§A.31)

- **NEW, F-D1.** In the matrix regime, AffineRespect of the phases and the Clifford gate, together with VIS, forces
  a tomographically complete effect span and body = Bloch ball. The pair {S, H} alone suffices.
  - Hidden assumption exposed: the phase-plus-Clifford route presupposes coherence-detecting effects.
  - Cross-propagation: the route cannot source DRIVE ahead of P2.
- **NEW, F-D2.** The continuum is free on the completed body.
  - D1–D8 ⟺ an infinite-order reversible AffineRespect datum, on a finite-rank body.
  - The continuity premise is eliminable.
  - Cross-propagation: for body-level drivability, DC's deliberately unadopted closure is supplied by the
    completion. It stays a premise for availability.
- **NEW, F-D3.** Stage-preserving operations have finite order on a finite-rank body, so the generator crosses
  stages. This refines OPACT design constraint 1 to cover closures.
- **ELABORATING, F-D4.** Chart continuity ⟺ d(d+1) completed-state probabilities.
- **ELABORATING, F-D5.** The branch square-root tower is a choice-free countermodel to continuity at the identity.
- **CONFIRMING, F-D6.** Route Φ is DRIVE restated (Thread O D-2).

***

## 8. Kernel candidates if a premise is later adopted

These are not designed and not proposed; they are cheap and premise-free.
- (K1) The route-Φ reduction and its converse, with D9 decidable on stage preparations.
- (K2) Stage-preserving ⇒ finite order.
- (K3) The countable no-go.
- (K4) Γ0, compactness of `chartBody`.

Route Γ itself (Γ2) needs Cartan, which is absent from Mathlib to my knowledge.
