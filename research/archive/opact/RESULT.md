# OPACT: can certified operations act on the CMP-1 completed body? RESULT (read-only)

Base: `D_OPACT = 254ad0a7f19b3cf6f6ce28e1a7b955f18e4337e4`. No repository change, no round, no preregistration.
Evidence levels: **kernel** (landed identifier at D_OPACT), **exact** (`opact_checks.py`, 26 checks + 2
countercontrols, byte-identical replay; sha256 script `a49d8e35…`, output `7317b154…`), **written**.

## 0. Verdict

**An extra premise is genuinely necessary.** Main carries no field-neutral operation at all: KInfFoundations
"sources nothing" and defines no transformation; StageCompletion has only forward stage maps. The only certified
operations are the ℂ-typed matrix channels of `FiniteOperationalTheory` (OperationalAssembly:594). They are not
connected to `DirectedStages`, and connecting them fixes the body as the Bloch ball (circular here; legitimate only
as a reverse instance).

The weakest premise found is **RESPECT**: the operation is given on stage preparations, with values in the
completed body, and it respects every finite affine relation among preparation vectors (indistinguishable
mixtures go to indistinguishable mixtures). With CMP-1's own `FiniteRank`, RESPECT yields the full OPACT package.
A stronger, finite-stage form (NATDUAL) needs no FiniteRank and no SC∞, but it cannot carry a one-parameter group.

## 1. Candidate statements

### OPACT-D (finite-stage, discrete): stage-natural table-dual pairs. Premise NATDUAL.

Data: for each stage i, maps T_i : P_i → P_i and T*_i : E_i → E_i with
- stage duality: p_i(T*_i e, x) = p_i(e, T_i x);
- naturality: map(T_i x) = T_j(map x), map(T*_i e) = T*_j(map e) for i ≤ j.

Conclusion (written; exact E1 on a tower where SC∞ FAILS):
1. completion duality val(a, T x) = val(T* a, x) — no SC∞ (both sides read at the same ub, because T and T*
   keep the stage index);
2. Φ_T f := f ∘ T* is linear on CSpace with ‖Φ_T‖ ≤ 1, Φ_T (prepVec x) = prepVec (T x), Φ_T (body) ⊆ body;
3. the action on the body does not depend on the choice of dual (E4: duals differ off the body);
4. composition on the body: Φ_{S∘T} = Φ_S ∘ Φ_T (equal on generators, both continuous affine);
5. effect transport stays in the stage family: coord a ∘ Φ_T = coord (T* a) ∈ stageEffects.

Limitation (written + exact E9): a reversible T_i permutes the finite set P_i, so any one-parameter group of such
operations acts trivially on every stage (ℝ is divisible; in a finite group every |G|-th power is 1). OPACT-D can
host discrete operations (J, fixed gates, finite symmetries), never a flow.

### OPACT-C (completion-valued; flow-compatible). Premise RESPECT (+ CMP-1's FiniteRank).

Data: τ : Prep D → body D with RESPECT: Σ λ_k prepVec x_k = Σ μ_l prepVec y_l (finite convex combinations)
⇒ Σ λ_k τ x_k = Σ μ_l τ y_l.

Conclusion (written; each step standard):
1. existence and uniqueness: one continuous affine Φ_τ on affineSpan(body) with Φ_τ (prepVec x) = τ x
   (RESPECT ⇔ well-defined affine on the hull, E2; FiniteRank ⇒ the span is finite-dimensional ⇒ continuous);
2. Φ_τ (body) ⊆ body (hull to body by convexity; closure by continuity, `body_subset`);
3. composition: Φ_{σ⋆τ} = Φ_σ ∘ Φ_τ, where (σ⋆τ) x := Φ_σ (τ x) (uniqueness);
4. reversibility: if σ⋆τ and τ⋆σ are the identity on generators, Φ_τ is an affine bijection of the span; with
   the chart (`exists_chart_of_finiteRank`, `exists_chart_leftInverse`, `chartRetract`) it is an element of
   `(Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)` preserving `bodyR L p0 (body D)` both ways, i.e. `PreservesBody` on the chart;
5. effect side: coord a ∘ Φ_τ is an effect on the body (completed effects); it need not be a stage effect.

Under FiniteRank, the state side (affine self-maps of the body) and the effect side (positive unital maps on the
affine functions of the span) are equivalent (finite-dimensional cone duality; the body is compact). Without
FiniteRank they are not, and continuity fails (E5).

## 2. No-go for flows through stage data (written; NEW)

If the stage index ι is countable (so Label and Prep are countable), every one-parameter family that is
probability-continuous (t ↦ val-coordinates continuous) and
- maps preparations to preparations, or
- maps stage effects to stage effects (as functions on the body),
is constant: each coordinate is a continuous real function of t with countable range, hence constant.

Consequences:
- OPACT for a drive must be completion-valued (OPACT-C), never preparation-to-preparation.
- EFFCLOSE with avail = stageEffects (Thread O, D-1) is incompatible with a nontrivial drive. A seed r ∈ stageEffects
  would be flow-invariant on the body (E6 shows a drive must move it), so V4′ + OG-1 could not produce the
  directional family. **Assumption-watch marker:** the P2 available-effect family must be completed beyond
  stageEffects.

## 3. Dependency chain (to landed names)

CMP-1 (`StageCompletion`): `DirectedStages`, `Label`, `Prep`, `ub`, `le_ub_left`, `le_ub_right`, `val`,
`val_nonneg`, `val_le_one`, `CSpace`, `prepVec`, `body`, `prepVec_mem_body`, `body_subset`, `evalLin`, `evalCLM`,
`coord`, `coord_apply`, `coord_prepVec`, `continuous_coord`, `stageEffects`, `coord_isEffectOn`,
`coord_unit_eq_one`, `FiniteRank`, `exists_chart_of_finiteRank`.
OG-1 (`OrbitNormalization`): `chart`, `chart_apply`, `chart_injective`, `exists_chart_leftInverse`, `chartRetract`,
`chartRetract_chart`, `chart_chartRetract`, `bodyR`, `effR`, `words`, `preservesBody_words`.
OG-1 (`OrbitGeneration`): `PreservesBody`, `seedTransport`.
KF: `FiniteStage`, `IsEffectOn`.
Not used: `SCInf`, `val_eq_at`, `sharpSeed_completion`, `BinaryVisible`, anything of IIP-1, `ElementaryDrivability`,
`BoundaryTransitive`, `ball3`, `ball4`, the K∞-1 material.
Mathlib: `lp`, `convexHull`, `closure`, `AffineMap.continuous_of_finiteDimensional`,
`LinearMap.continuous_of_finiteDimensional`.

## 4. Countermodels

| premise omitted | model | what fails | evidence |
|---|---|---|---|
| RESPECT | one stage, preparations x0, x1, xm with xm the midpoint; swap x0 ↔ xm | no affine extension; no dual effect | exact E2 |
| naturality (NATDUAL) | SC∞ bit tower, T₀ = id, T₁ = NOT, each stage dual | equal completed states get different images; completion duality fails | exact E3 |
| FiniteRank / continuity (OPACT-C) | SC∞ tower, prepVec z_n → prepVec w at rate 1/n, affinely independent; τ z_n = z₁ | RESPECT holds, no continuous extension | exact E5 (rank 40) |
| reversibility | reset to one state | affine, body-preserving, not injective | exact E7 |
| completion-valued codomain | any countable tower, any continuous flow | the flow is constant | written (§2); exact E6, E9 |
| (positive control) | natural dual NOT on the bit tower | reflection of the segment; involution | exact E8 |
| (countercontrol of E1) | wrong-direction dual; identity dual | duality fails on 252 of 324 pairs | exact |

## 5. Circularity audit

The premises of OPACT-D and OPACT-C are `DirectedStages` data, an operation datum (NATDUAL or τ with RESPECT),
inverse availability for reversibility, and (OPACT-C only) CMP-1's `FiniteRank`. None mentions or implies:
- DRIVE (no flow, no continuity in a parameter; the no-go shows OPACT-D excludes flows);
- transitivity (no orbit statement);
- the invariant inner product (no moment, no `invMatrix`; IIP-1 is downstream: it consumes the PreservesBody that
  OPACT-C supplies);
- DIM3 (FiniteRank allows any finite d);
- ellipsoid / ball structure (the body is arbitrary; E8's segment is a control);
- SC∞ (E1 runs on a non-SC∞ tower).

What OPACT does not do: it does not source the operations. RESPECT/NATDUAL is the operation datum itself. OPACT
turns any such datum into body automorphisms on the chart; which operations exist is the open sourcing question
(Thread O §5: the choice of physical continuum).

## 6. Classification (§A.31)

- NEW: the countable-stage no-go (§2) and its consequence for EFFCLOSE / P2 (written).
- NEW: OPACT-D needs no SC∞ (exact E1; favorable, so countercontrolled).
- ELABORATING: RESPECT is the exact well-definedness condition (E2); continuity needs FiniteRank (E5).
- CONFIRMING: Thread O's "not stage by stage" (ON:124), now as the divisibility argument (E9).
