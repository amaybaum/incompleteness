# RelcSelectParity.lean — design notes (UNBUILT; no local Lean toolchain)

Target: `OIBridge/RelcSelectParity.lean`, namespace `OIBridge.RelcSelect`, `import OIBridge.OddChar`,
open line copied from `OddChar.lean:30`. Source snapshot: `wt-L` (L = e2426ba4). Never compiled.
`sorry` count: **0**.

## Route chosen

Route 1 (fixed spaces), but using only **forward** maps and **upper** bounds, so `G.symm` is never
needed (relC is not closed under inverse — LEDGER assumption-watch marker) and no trace API is used.

1. `opGate G` (landed) is injective (`opGate_injective_relC`) and, from relC alone,
   `opGate G (H ∘ F) = H ∘ opGate G F ∘ H` (`opGate_homMap_comp_relC`, verbatim copy of
   `ParityNot.opGate_homMap_comp_rel` with `hR.relC` replaced by `hC`).
2. On `End := HVec d →ₗ HVec d`: `relCLeft N : F ↦ H ∘ F`, `relCConj N : F ↦ H ∘ F ∘ H`.
   Generic lemma (copy of `NativeGateBall.parity`'s restrict/injective pattern): an injective `A`
   with `A ∘ L = T ∘ A` gives `dim ker(L ∓ id) ≤ dim ker(T ∓ id)`.
3. Exact: `dim ker(relCLeft − id) = (d+1)·P`, `dim ker(relCLeft + id) = (d+1)·Q`
   (landed `finrank_ker_eq_of_pointwise`, same proof shape as `finrank_ker_Pop_sub/add`).
4. Upper bounds: restriction `F ↦ (F|E₊, F|E₋)` is an injective linear map
   `ker(relCConj − id) → End(E₊) × End(E₋)` and `ker(relCConj + id) → Hom(E₊,E₋) × Hom(E₋,E₊)`
   (injectivity via the landed `v = ½(v+Hv) + ½(v−Hv)` decomposition from `Lop_eq_zero_rel`),
   so the dimensions are `≤ P² + Q²` and `≤ PQ + QP`.
5. `(P+Q)P ≤ P²+Q²` ⇒ `QP ≤ QQ`; `(P+Q)Q ≤ 2PQ` ⇒ `QQ ≤ QP`; `Q ≥ 1` ⇒ `P = Q`
   (`Nat.eq_of_mul_eq_mul_left`, same as the landed parity proof).

Exact sanity checks run (sympy, ranks over ℚ, not floats): for diagonal `H` with `P,Q ∈ {1,2,3}` the
four eigenspace dimensions are `nP, nQ, P²+Q², 2PQ`; brute force over `P < 30, 1 ≤ Q < 30` confirms the
arithmetic lemma.

## Landed declarations used (file:line at L)

CompositeDimension.lean: `HVec` 93, `W` 97, `homMap` 112, `homMap_homMap` 152, `actT` 198, `actC` 201,
`IsNot` 210, `plusSpace` 257, `minusSpace` 261, `mem_plusSpace` 264, `mem_minusSpace` 268,
`finrank_plus_add_finrank_minus` 274, `one_le_finrank_minusSpace` 306, `not_even_of_balanced` 324,
`toOp` 406, `fromOp` 409, `toOp_fromOp` 411, `toOp_injective` 417, `toOp_actC` 451, `toOp_actT` 464,
`actC_actC` 476, `opGate` 486, `opGate_toOp` 489, `projMinus` 515 (`.2` membership),
`finrank_ker_eq_of_pointwise` 622.
TransitiveBody.lean: `eball` 518.
Patterns copied (not called): ParityNot.lean `opGate_homMap_comp_rel` 59, `Lop_eq_zero_rel` 80
(decomposition block 100–107), `finrank_plus_eq_finrank_minus_rel` 128, `not_even_of_gateRel` 137;
NativeGateBall.lean `parity` 194 (restrict/injective block).

## Mathlib / core names

Used elsewhere in landed OIBridge (treated as verified): `LinearMap.ext`, `.comp_apply`, `.add_apply`,
`.sub_apply`, `.smul_apply`, `.id_apply`, `.zero_apply`, `.mem_ker`, `.congr_fun`, `.restrict`,
`.restrict_apply`, `.codRestrict`, `.finrank_le_finrank_of_injective`, `Module.finrank_fin_fun`,
`Module.finrank_linearMap` (explicit args `R S M N`), `Submodule.subtype`, `Prod.ext` (two explicit
args), `Subtype.ext`, `LinearEquiv.injective`, `map_add/map_smul/map_neg/map_zero`, `RingHom.id_apply`,
`sub_eq_zero`, `add_eq_zero_iff_eq_neg`, `neg_neg`, `sub_self`, `Nat.eq_of_mul_eq_mul_left`, `module`.

Not used elsewhere in OIBridge (marked `MATHLIB-NAME-UNVERIFIED` in the file; both read in the pinned
sources over the network, not compiled):
- `Module.finrank_prod` — Mathlib v4.33.0 `LinearAlgebra/Dimension/Constructions.lean:162`,
  implicit `R M M'`, `@[simp]`. Wrapped in `first | rw … | simp only …`.
- `Nat.le_of_add_le_add_left` — Lean v4.33.0 `Init/Data/Nat/Basic.lean:520`. Wrapped in
  `first | exact … | linarith | nlinarith`.

## Riskiest steps (in order)

1. `relCSplitEven` / `relCSplitOdd` (def bodies): `map_add'`/`map_smul'` by
   `Prod.ext (LinearMap.ext fun u => rfl) (LinearMap.ext fun u => rfl)` — relies on definitional
   unfolding through `Prod` add/smul, `codRestrict`, submodule add/smul and `RingHom.id`; same idiom
   as `finrank_ker_eq_of_pointwise`'s `A`, plus one `Prod` layer. Also the codRestrict proof argument
   `fun u => mem_plusSpace_of_comm_relC hN F.2 u` is accepted only up to defeq of
   `(F ∘ₗ subtype) u` with `F ↑u`. Fallback if it fails: `by ext u <;> rfl`, or define the components
   with `LinearMap.lcomp ℝ (HVec d) (plusSpace N).subtype` as in `Lop`.
2. `relCSplitEven_injective`: `exact this` where `this` is
   `↑((relCSplitEven hN F₁).1 ⟨u,hu⟩) = …`, closed by defeq to `F₁.1 u = F₂.1 u`.
   Fallback: add `rfl` apply-lemmas for the two components and `rw` with them.
3. `finrank_ker_relCConj_*_le`: matching the `Module (A × B)` / `Module (P →ₗ Q)` instances in `h`
   (from the def's codomain) with those in `e` (elaborated afresh), and `rw`/`simp` with
   `Module.finrank_prod` + `Module.finrank_linearMap`.
Lesser: `simp only … at h` shapes in `homMap_comm_relC`/`homMap_anticomm_relC`; the instance path of
`LinearMap.id` when `rw [finrank_ker_relCLeft_sub] at hle` (same situation as the landed
`rw [finrank_ker_Pop_sub, …] at hpar`).

## Exported statements (all in `OIBridge.RelcSelect`)

```lean
noncomputable def relCLeft (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    (HVec d →ₗ[ℝ] HVec d) →ₗ[ℝ] (HVec d →ₗ[ℝ] HVec d)
noncomputable def relCConj (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    (HVec d →ₗ[ℝ] HVec d) →ₗ[ℝ] (HVec d →ₗ[ℝ] HVec d)
theorem relCLeft_apply (N) (F : HVec d →ₗ[ℝ] HVec d) (v : HVec d) : relCLeft N F v = homMap N (F v)
theorem relCConj_apply (N) (F) (v) : relCConj N F v = homMap N (F (homMap N v))
theorem relCLeft_eq (N) (F) : relCLeft N F = homMap N ∘ₗ F
theorem relCConj_eq (N) (F) : relCConj N F = homMap N ∘ₗ F ∘ₗ homMap N
theorem opGate_homMap_comp_relC {z N} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N)
    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) (F : HVec d →ₗ[ℝ] HVec d) :
    opGate G (homMap N ∘ₗ F) = homMap N ∘ₗ opGate G F ∘ₗ homMap N
theorem opGate_injective_relC (G : W d ≃ₗ[ℝ] W d) : Function.Injective (opGate G)
theorem finrank_ker_sub_le_relC {V : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V]
    (A L T : V →ₗ[ℝ] V) (hA : Function.Injective A) (hAL : ∀ v, A (L v) = T (A v)) :
    finrank ℝ (ker (L - id)) ≤ finrank ℝ (ker (T - id))
theorem finrank_ker_add_le_relC  -- same hypotheses: finrank ℝ (ker (L + id)) ≤ finrank ℝ (ker (T + id))
theorem finrank_ker_relCLeft_sub (N) :
    finrank ℝ (ker (relCLeft N - id)) = (d + 1) * finrank ℝ (plusSpace N)
theorem finrank_ker_relCLeft_add (N) :
    finrank ℝ (ker (relCLeft N + id)) = (d + 1) * finrank ℝ (minusSpace N)
theorem eq_zero_of_plus_minus_relC {N} (hN : ∀ x, N (N x) = x) (F : HVec d →ₗ[ℝ] HVec d)
    (hp : ∀ u ∈ plusSpace N, F u = 0) (hm : ∀ u ∈ minusSpace N, F u = 0) : F = 0
theorem homMap_comm_relC {N} (hN) {F} (hF : F ∈ ker (relCConj N - id)) (v) :
    homMap N (F v) = F (homMap N v)
theorem homMap_anticomm_relC {N} (hN) {F} (hF : F ∈ ker (relCConj N + id)) (v) :
    homMap N (F v) = -F (homMap N v)
theorem mem_plusSpace_of_comm_relC     {N} (hN) {F} (hF : F ∈ ker (relCConj N - id)) (u : plusSpace N)  : F u ∈ plusSpace N
theorem mem_minusSpace_of_comm_relC    {N} (hN) {F} (hF : F ∈ ker (relCConj N - id)) (u : minusSpace N) : F u ∈ minusSpace N
theorem mem_minusSpace_of_anticomm_relC {N} (hN) {F} (hF : F ∈ ker (relCConj N + id)) (u : plusSpace N) : F u ∈ minusSpace N
theorem mem_plusSpace_of_anticomm_relC  {N} (hN) {F} (hF : F ∈ ker (relCConj N + id)) (u : minusSpace N) : F u ∈ plusSpace N
noncomputable def relCSplitEven {N} (hN : ∀ x, N (N x) = x) :
    ker (relCConj N - id) →ₗ[ℝ] (plusSpace N →ₗ[ℝ] plusSpace N) × (minusSpace N →ₗ[ℝ] minusSpace N)
noncomputable def relCSplitOdd {N} (hN : ∀ x, N (N x) = x) :
    ker (relCConj N + id) →ₗ[ℝ] (plusSpace N →ₗ[ℝ] minusSpace N) × (minusSpace N →ₗ[ℝ] plusSpace N)
theorem relCSplitEven_injective {N} (hN) : Function.Injective (relCSplitEven hN)
theorem relCSplitOdd_injective {N} (hN) : Function.Injective (relCSplitOdd hN)
theorem finrank_ker_relCConj_sub_le {N} (hN : ∀ x, N (N x) = x) :
    finrank ℝ (ker (relCConj N - id)) ≤ P * P + Q * Q
theorem finrank_ker_relCConj_add_le {N} (hN : ∀ x, N (N x) = x) :
    finrank ℝ (ker (relCConj N + id)) ≤ P * Q + Q * P
theorem balance_of_bounds_relC {n P Q : ℕ} (hn : P + Q = n) (hQ : 1 ≤ Q)
    (h1 : n * P ≤ P * P + Q * Q) (h2 : n * Q ≤ P * Q + Q * P) : P = Q
theorem finrank_plus_eq_finrank_minus_relC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N)
    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) :
    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N)
theorem not_even_of_relC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N)
    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) : ¬ Even d
```
(`P`/`Q` abbreviate `Module.finrank ℝ (plusSpace N)` / `(minusSpace N)`; `ker`/`id` are
`LinearMap.ker`/`LinearMap.id`; the file carries the full types.) All 28 names were grepped against
every `.lean` file under `verification/lean-mathlib/` at L: zero hits, and the namespace `RelcSelect`
is unused.

## Optional controls (not in the file; a round may add them)

Positive non-vacuity controls, each one line, using landed objects:
`finrank_plus_eq_finrank_minus_relC isNot_nflip cnot_relC`,
`not_even_of_relC (isNot_nK k) (gateRel_gRev k).relC` (any `k`), and
`not_even_of_relC isNot_neg1 cnot1_relC`. They need fresh names if added as theorems (landed modules
use no `example`s). The ledger's countercontrol (d = 2 `swapgate`: frame + relT, not relC) is not
in this module.
