# POS-SEP ledger — is either positivity clause of `NativeGate` individually sufficient to exclude odd d ≥ 5?

Read-only research thread. Base snapshot L = `e2426ba4109dcd719d518aefbd3c417b7c6fdc5b` (detached worktree `wt-L`).
Nothing here is adopted, preregistered, frozen or governed. No Lean toolchain was available: every Lean
statement cited below was read from the landed source at L; nothing in this directory has been built.

## 0. Productivity test (written before any node was walked)

The thread is a **gem** iff it yields a fact strictly stronger than the restatement "DIM-1 reads both
positivity clauses" AND either constrains something or exposes a hidden assumption. Concretely, one of:

- (A) a proof outline that `IsNot + frame + relT + relC + posFwd` (or `+ posInv`) alone forces `d ∈ {1,3}`; or
- (B) an explicit countermodel at some odd `d ≥ 5` with `IsNot`, frame, relT, relC and exactly one of the
  two positivity clauses, with the algebraic clauses checked exactly, the failing clause refuted by an exact
  rational witness, and the holding clause established by a written proof (finite sampling alone does not
  count); or
- (C) the exact step of the DIM-1 chain at which the missing clause is read, together with the exact
  property of the gate that would have to hold for a single clause to suffice.

Anything weaker — e.g. "posInv is used in DIM-1" without locating which use is eliminable — is a
non-gem (coherence relabeling) and is recorded only.

Classification vocabulary: NEW / POSITIVE / ELABORATING / CONFIRMING / BORDERLINE (AGENTS.md §A.31).

## 1. Verdict in one paragraph

**(B) — an explicit separating countermodel, at every odd d ≥ 3 and in particular at d = 5.** With the landed
`nK 2 = n5`, `zK 2 = z5` on `eball 5`, the *squeezed gate* `G = G_ε ∘ (I ⊗ K_λ)` (ε = 1/10, λ = 1/2; §N3.1)
satisfies `IsNot`, `frame`, `relT`, `relC` and `posFwd`, and fails `posInv` (exact value −1/2). By N1,
`G.symm` satisfies `IsNot`, `frame`, `relT`, `relC` and `posInv`, and fails `posFwd`. So **neither positivity
clause alone, with the other four clauses, excludes d = 5** (nor any odd d ≥ 5; §N3.5). The DIM-1 selector
reads both clauses, and exactly one step needs the second one: `lor_Minv`. The thing that must hold there
is that the forward corner map `Mfwd` is an automorphism of the cone `Lor` (§N2). Evidence level: a written
proof, plus exact computation of every algebraic clause, of the posInv witness, of the decomposition
identity the proof uses, and of exact cone-membership certificates at 218 + 40 sampled product states. It
is **not kernel-checked**.

## 2. Node tree

### N1 — symmetry reduction: frame, relT and relC transfer from `G` to `G.symm`

Verdict: **TRUE (written proof; exact computational check on four gates).**

Definitions read at L: `actT N ω = fun μ => homMap N (ω μ)` (CompositeDimension.lean:198), `actC N ω μ ν =
homMap N (fun κ => ω κ ν) μ` (:201), `actT_actT`, `actC_actC` (:471, :476; both need only `IsNot.invol`),
`frame` (:220–221), `relT` (:224), `relC` (:225).

- *frame.* In `Fin 2`, `a + (a + b) = b`. Applying `frame a (a+b)` gives `G(c_a ⊗ c_{a+b}) = c_a ⊗ c_b`, so
  `G.symm(c_a ⊗ c_b) = c_a ⊗ c_{a+b}`.
- *relT.* `relT` together with `actT_actT` gives `G ∘ actT = actT ∘ G` (this is `gate_actT`, :1938). Hence
  `G.symm ∘ actT = actT ∘ G.symm`, and that is `relT` for `G.symm`.
- *relC.* `gate_actC` (:1945) gives `G (actC ω') = actC (actT (G ω'))`. Put `ω' = actT (G.symm ω)`. The
  right side becomes `actC (actT (actT ω)) = actC ω`, so `G.symm (actC ω) = actC (actT (G.symm ω))`. Apply
  `actC`, then `actC_actC`.
- *positivity.* `posInv` for `G` is literally `posFwd` for `G.symm`, and `G.symm.symm = G`.

Consequence: "posFwd alone (with IsNot, frame, relT, relC) excludes d ≥ 5" ⇔ "posInv alone does". The
question has one answer. Check: `possep_check.py` "N1: G.symm has frame, relT, relC" on the d = 3, 5, 7
squeezed gates and on the no-squeeze control. Each is computed from the exact inverse matrix, not from a
formula for the inverse. A Lean draft is in `PosSepDraft.lean` §1 (UNBUILT).

### N2 — where DIM-1 reads `posInv`

Verdict: **posInv enters through one load-bearing step, `lor_Minv`. Its other use is eliminable.**

Grep at L (`posInv|lor_Minv|gate_corner_symm`):

- N2.1 `gate_corner_symm` (CompositeDimension.lean:1895–1904) runs S1 (`corner_form`) on `G.symm` with
  `posInv`. **Eliminable.** `Mfwd` is injective: if `Mfwd Y = 0`, then `G(hom z ⊗ Y) = 0` by `gate_corner`,
  so `Y = 0` by `tens_hom_inj`. Hence `Mfwd` is bijective on `HVec d`. Then
  `G.symm(hom z ⊗ Y) = hom z ⊗ Mfwd⁻¹ Y` follows from `gate_corner` alone, so `Minv = Mfwd⁻¹` holds without
  `posInv`. `Mfwd_Minv`, `Minv_Mfwd` and `Minv_homMap` then follow as landed.
- N2.2 `lor_Minv` (:1918–1921) is `lor_cornerMap` applied to `G.symm`, which uses `posInv`. **Load-bearing.**
  It says `Minv(Lor) ⊆ Lor`. Combined with `lor_cornerMap` for `G` (`Mfwd(Lor) ⊆ Lor`, which uses posFwd
  only), it says exactly that **`Mfwd` is a linear automorphism of `Lor`**.
  Consumers of `lor_Minv`:
  - `gt_tangent_corners` (:2080). *Eliminable:* run the same tangent argument with an arbitrary `Y ∈ Lor`
    in place of `Minv t`. The corner values still vanish by `gate_corner` / `gate_corner_neg`, and
    linearity (`linearMap_eq_zero_of_lor`) extends the identity to every `Y`.
  - `gt_sphere` (:2127), `gt_sphere_corner` (:2153, :2163) and `blockData_of_orthonormal`'s `hR` (:2598).
    *Not eliminable as stated.* The tangent argument needs `F ≥ 0` on `Lor` for
    `F(X) = pairVal a (hom(−τ)) (G(X ⊗ Minv(hom τ)))`, so it needs `Minv(hom τ) ∈ Lor` at **boundary**
    rays `hom τ` (τ a unit vector). That is the statement that boundary rays of `Lor` lie in `Mfwd(Lor)`.
- N2.3 **Positive by-product (written proof outline, not kernel):** `IsNot + frame + relT + relC + posFwd`
  together with "`Mfwd` is a cone automorphism", or even only "`Mfwd⁻¹(Lor) ⊆ Lor`", gives `d ∈ {1, 3}`.
  The proof is DIM-1 §Q verbatim with N2.1's `Minv := Mfwd⁻¹` and the hypothesis replacing `lor_Minv`.
  Special case: every gate with `Mfwd = id` (normalized on the `z` slice) is selected by posFwd alone.
  NB-1's own header (NativeGateBall.lean:16, "§E a contraction with a contracting left inverse is an isometry
  (the last step of S1)") names the same step. N3 shows that it cannot be bypassed.

Decisive branch at this level: N2.2 says a countermodel must have `Mfwd` a non-automorphism, contracting
`Lor` strictly while fixing `hom(±z)`. N3 builds one.

### N3 — the d = 5 countermodel ("squeezed gate")

#### N3.1 Definition (indices are DIM-1's homogeneous indices `0..d`, d = 2k+1, k = 2)

- `N = nK k` (OddChar.lean:56), with homogenized signs `s_μ = −1` iff `μ > k`. Axis `z = zK k`, hom index `d`.
  At k = 2 this is the landed `n5` / `z5` (ParityNot.lean:567–573): `odd5` is `μ ∈ {3,4,5}`.
- Control classes: `C = {0, d}` (`hom 0`, `lift z`) and `T = {1..d−1}`, with `T+ = {1..k}` and
  `T− = {k+1..2k}`. `permT` swaps `μ ↔ μ+k` (it exchanges `T±`). The target relabelling `σ` swaps
  `0 ↔ 1` and `d ↔ k+1` and fixes the rest, so it preserves parity.
- `K_λ = diag(1, λ, …, λ, 1)` on `HVec d`. It fixes `hom 0` and `lift z`, scales the tangent by λ, commutes
  with `homMap N`, and maps `Lor` into `Lor` but not onto it.
- `G_ε(e_μ ⊗ e_ν) = e_{μ'} ⊗ e_ν` for μ ∈ C, where `μ' = μ` (ν even) or `d − μ` (ν odd). This is the
  classical controlled-`N`.
- `G_ε(e_μ ⊗ e_ν) = ε · e_{μ''} ⊗ e_{σν}` for μ ∈ T, where `μ'' = μ` (ν even) or `permT μ` (ν odd).
- `G := G_ε ∘ (I ⊗ K_λ)`, with ε = 1/10 and λ = 1/2. Code: `possep_gate.py`; Lean-shaped entry formula:
  `PosSepDraft.lean` `sqzFun`.

The design requirement that DIM-1 does not see is that `Γ := G_ε|_{T⊗HVec}` sends the target directions
`hom 0` and `lift z` into the target tangent (`σ(0) = 1`, `σ(d) = k+1`). Without this, the clause fails at
the target corners `±z`, which `K_λ` cannot squeeze. That is why the landed `gJ5` (whose `Γ` keeps `hom 0`
and `lift z`) fails even after squeezing.

#### N3.2 Algebraic clauses — **exact computation, PASS**

`possep_check.py`, d = 5:

- `IsNot`: unit, invol and flips are exact; preserves holds because a diagonal ±1 map preserves the sum of
  squares.
- `frame`: all four corner pairs.
- `relT` and `relC`: all 36 basis vectors, hence all of `W 5` by linearity.
- Linear equivalence: exact rank 36, with the exact inverse computed.
- Corner form: `G(hom z ⊗ Y) = hom z ⊗ K_λ Y`, i.e. `Mfwd = K_λ`.
- `Minv(hom e₁) = (1, 2, 0, 0, 0, 0) ∉ Lor`. So `lor_Minv` fails, as N2.2 requires of any countermodel.

#### N3.3 `posFwd` — **written proof (for every k ≥ 1, ε ≤ (1−λ)/(2(1+λ)), 0 < λ < 1)**

Let `x, y ∈ eball d` and let `e, f` be effects, with `a = ehom e`, `b = ehom f ∈ Lor` (`lor_ehom`,
CompositeDimension.lean:930). We need `V := pairVal a b (G(prodState x y)) ≥ 0`. Write:

- `α = x_{d−1}` (the z-coordinate) and `c_μ = x_{μ−1}` for μ ∈ T;
- `Y = K_λ hom y = hom w`, where `w = (λ·y_tangent, y_z) ∈ eball d`;
- `p = a_0 + a_d`, `q = a_0 − a_d`;
- `A = b·hom w` and `B = b·hom(N w)`;
- `S_e = Σ_{ν even} Y_ν b_{σν}` and `S_o = Σ_{ν odd} Y_ν b_{σν}`;
- `C_e = Σ_{μ∈T} c_μ a_μ` and `C_o = Σ_{μ∈T} c_μ a_{permT μ}`.

1. **Decomposition identity.**
   `V = (1+α)/2 · pA + (1−α)/2 · qB + ε (S_e C_e + S_o C_o)`.
   By hand: `hom x = (1+α)/2 hom z + (1−α)/2 hom(−z) + lift c`. The classical part sends this to
   `(1+α)/2 hom z ⊗ Y + (1−α)/2 hom(−z) ⊗ (homMap N) Y`. The `T` part pairs to the ε term because `μ''`
   depends only on the parity of ν. **Checked exactly, as a polynomial identity in all 22 / 14 / 30
   variables, at d = 5 / 3 / 7 (sympy `expand(V − formula) == 0`).**
2. All four quantities `p, q, A, B` are `≥ 0`: `|a_d| ≤ a_0`, and pairings of two `Lor` vectors are `≥ 0`.
   AM–GM: the first two terms are `≥ √((1−α²) pq AB)`.
3. `1 − α² ≥ |c|²` because `|x| ≤ 1`. `pq = a_0² − a_d² ≥ |a_T|²` by `Lor(a)`. So the first part is
   `≥ |c| |a_T| √(AB)`.
4. Cauchy–Schwarz: `|C_e|, |C_o| ≤ |c| |a_T|`, since `permT` permutes `T`.
   Hence `V ≥ |c| |a_T| (√(AB) − ε(|S_e| + |S_o|))`.
5. **Key lemma:** `ε(|S_e| + |S_o|) ≤ √(AB)` for all `b ∈ Lor` and `y ∈ eball d`.
   Normalize `b_0 = 1` (both sides are homogeneous of degree 1). Let `ζ = b_d`, `τ` = tangent part of `b`,
   `t = |τ|`. Let `β = y_z`, `v` = tangent part of `y`, `s = |v|`. Then `ζ² + t² ≤ 1` and `β² + s² ≤ 1`,
   and `A = 1 + ζβ + λ τ·v`, `B = 1 − ζβ + λ τ·N'v` (N flips z; `N'` is orthogonal on the tangent).
   - Let `D = 1 − √((1−t²)(1−s²))`. Cauchy–Schwarz gives `|ζβ| ≤ √((1−t²)(1−s²))` and `ts ≤ D`.
   - If `ζβ ≥ 0`: `A ≥ 1 − λts ≥ 1 − λ` and `B ≥ D − λts ≥ (1−λ)D`. If `ζβ ≤ 0`, the same holds with A and
     B swapped.
   - So `AB ≥ (1−λ)² D ≥ (1−λ)² m²/2`, where `m = max(t, s)`, using `D ≥ 1 − √(1−m²) ≥ m²/2`.
   - Upper side, from σ: `S_e = b_1 + λ(v_1 b_0 + Σ_{ν=2..k} v_ν b_ν)` and
     `S_o = β b_{k+1} + λ(v_{k+1} b_d + Σ_{ν=k+2..2k} v_ν b_ν)`.
   - So `|S_e| + |S_o| ≤ (|b_1| + |b_{k+1}|) + λ s √(1 + ζ² + t²) ≤ √2 t + √2 λ s ≤ √2(1+λ) m`.
   - Hence ε ≤ (1−λ)/(2(1+λ)) suffices. At λ = 1/2 the bound is 1/6, so ε = 1/10 and ε = 1/16 qualify.
6. So `V ≥ 0` for every pair of effects, i.e. `G(prodState x y) ∈ maxCone (eball d)`. ∎

Kernel route (for a later round): square steps 2–5 to remove `Real.sqrt` (`P ≥ 0` and `P² ≥ E²` ⇒ `P + E ≥ 0`).
Each step is then a polynomial inequality of the size DIM-1's `cnot_core` already handles. The identity in
step 1 is a `simp [Fin.sum_univ_six]; ring`-type computation over 36 entries.

#### N3.4 `posInv` fails — **exact rational witness, PASS**

`prodEffVal (sharpEff z5) (sharpEff (−x5)) (G.symm (prodState z5 x5)) = 1/2 − 1/(2λ) = −1/2`.
Mechanism: `G.symm(hom z ⊗ hom x5) = hom z ⊗ K_λ⁻¹ hom x5 = hom z ⊗ (1, 2, 0, 0, 0, 0)`.
It is computed from the exact inverse matrix and agrees with the formula. Both effects are sharp along unit
vectors (`sharpEff_isEffectOn`), so this is a valid refutation in the landed vocabulary.
By N1, `G.symm` is the converse countermodel: it has frame, relT, relC and posInv, and it fails posFwd at
the same witness.

#### N3.5 Other odd d — written proof (N3.3 is dimension-free) plus exact checks at d = 3, 7

At d = 3 and d = 7 (ε = 1/16, λ = 1/2), all of N3.2, the posInv witness (−1/2) and the symbolic identity
pass exactly. The d = 3 instance is harmless (DIM-1 allows d = 3). It shows only that posFwd ⇏ posInv
there too.

### N4 — skeptic passes (maximum skepticism on the branch that closed)

The closed branch is unfavourable to a "positivity alone selects" reading. It still got full skepticism,
because it overturns a natural expectation.

- N4.1 *Is the cone test complete?* `maxCone` quantifies over all effects. The proof covers all
  `a, b ∈ Lor ⊇ {ehom e}`, which is sufficient. The sample certifier checks `L(α) = ωᵀ(1,α) ∈ Lor` on the
  whole ball. It uses `L_0` exactly, plus either a rational S-lemma multiplier μ with `ωJωᵀ − μJ ⪰ 0`
  (exact LDLᵀ) or, at tight points, an algebraic μ* (an exact root of `det(ωJωᵀ − μJ)`, with every
  principal minor's sign decided by rational root isolation). Controls: it **certifies the landed positive
  gate `cnot` at 40/40 pure-product samples** (19 of them need the algebraic path). It **rejects the landed
  non-positive `gJ5` image** (`gJ5_not_mem_maxCone`).
- N4.2 *Sampling result (evidence, not proof).* Of 218 sampled product states for the d = 5 gate (random
  rational interior and sphere points, plus near-corner and target-corner states), 218/218 are certified
  exactly. So are 40/40 product states at which a Nelder–Mead search drives the pairing toward its minimum
  (float minimum found: −1.1e−16, i.e. 0 to rounding; tight at products, as expected). Also
  d = 3: 98/98; d = 7: 78/78; d = 5 at ε = 1/16: 78/78.
- N4.3 *Is the squeeze load-bearing? Countercontrols, which must fail and do:*
  - With λ = 1 (no squeeze, `Mfwd = id`), the same `G_ε` fails posFwd. Clean exact witness:
    `prodEffVal (sharpEff e₁) (sharpEff −e₂) (G(prodState e₁ e₂)) = −ε/4 = −1/40`. Here A = B = 0 and
    `S_e = −1`. A float-search-plus-rational witness also gives −0.0262.
  - The same test on the squeezed gate gives `((1−λ) − ελ)/4 = 9/80 ≥ 0`.
  - With ε = 1, λ = 1/2 (above the proof's bound), posFwd fails: there is an exact rational witness of
    value −0.110.
  So posFwd genuinely depends on λ < 1 and on ε being small. The proof's hypotheses are not decorative.
- N4.3b *Key-lemma constants (exploratory float, `keylemma_float.py`, not a certificate):* the ratio
  `(|S_e|+|S_o|)/√(AB)` is at most ≈ 1.82 over 2·10⁵ random and 2·10⁵ near-corner samples (k = 1, 2, 3, with
  λ = 1/2). The proof's bound is 1/ε_max = 6, so the written constant is conservative and nothing
  contradicts it.
- N4.4 *Does the countermodel cheat on a clause's Lean meaning?* `G` is a `W 5 ≃ₗ W 5` (an exact weighted
  permutation composed with a diagonal map). `actT`/`actC` were implemented from their Lean definitions,
  not from a tensor shorthand. Positive control PC3 reproduces the landed `cnot` frame/relT/relC with the
  same code, and PC1/PC2 reproduce `gJ5_value` and `gRev_value` (k = 1, 2, 3) = −1/10.
- N4.5 *Fixed point.* After the N3 finding, passes N4.1–N4.4 and the general-k pass N3.5 produced no
  further NEW finding. The remaining open items (§5) are different questions, not gaps in this one.

## 3. Controls summary (`python3 possep_check.py`; latest run: `run.log`, 66 checks, 0 failed)

| control | kind | result |
|---|---|---|
| PC1 `gJ5_value = −1/10` | positive (landed ParityNot:692) | reproduced |
| PC2 `gRev_value k=1,2,3 = −1/10` | positive (landed OddChar:258) | reproduced |
| PC3 `cnot` frame/relT/relC | positive (landed CompositeDimension:848–864) | reproduced |
| CC0+ certifier on landed `nativeGate_cnot` | positive | 40/40 certified |
| CC0− certifier on `gJ5` image | counter (must fail) | rejected |
| no-squeeze λ = 1 | counter (must fail posFwd) | fails, −1/40 exact |
| ε = 1 | counter (must fail posFwd) | fails, exact rational witness |
| no-squeeze `lor_Minv` | consistency | `Minv = id` preserves `Lor` |

## 4. Classification

- **NEW**: NB-1's open question ("Whether G injective with G(min) ⊆ max alone, without inverse positivity,
  forces d ∈ {1,3}", round-nb-1 result.md:47) and ODD-CHAR-1's ("Whether either clause is needed without
  the other is open", result.md:42–43) have the answer **no**, at d = 5 and at every odd d ≥ 5. Each
  positivity clause is individually load-bearing for DIM-1's exclusion of the odd d ≥ 5: dropping either
  one admits a gate. Evidence: written proof + exact computation; not kernel.
- **POSITIVE**: N1, the clause symmetry under `G ↦ G.symm` (written; trivially formalizable, draft in
  `PosSepDraft.lean` §1).
- **ELABORATING**: N2's localization. Of the five landed uses of `posInv`, only `lor_Minv` is load-bearing,
  and only at boundary rays (`gt_sphere`, `gt_sphere_corner`, `blockData` `hR`). The exact missing
  property is "`Mfwd` is a cone automorphism". N2.3 is the corresponding positive statement: posFwd plus
  that property selects d ∈ {1,3} (written outline).
- **Assumption-watch marker:** any future argument that "positivity of the gate" selects a dimension must
  say which direction it reads. A one-sided positive gate can contract the target cone on the corner slice
  (`Mfwd = K_λ`) and so evade every boundary-ray (sphere) identity except at the corners `±z`.

What is *not* claimed:

- that the squeezed gate is entangling (`Entangling` was not examined);
- anything about `posFwd + Entangling`;
- that N2.3's automorphism hypothesis is strictly weaker than posInv;
- anything about non-ball bodies or smaller effect cones;
- any statement about physics.

## 5. Open gaps (exactly located)

1. Kernel status: none of N1, N2.3 or N3 is kernel-checked. N1 is the cheapest (draft written). N3.3 needs
   the squared-form inequality chain and the 36-entry identity.
2. Whether `IsNot + frame + relT + relC + posFwd + Entangling` excludes d = 5. The squeezed gate is near
   classical (its images are ε-perturbations of separable states), so it is plausibly not entangling.
   Unchecked. A countermodel for that sharper question would need a different construction.
3. Whether N2.3's hypothesis "`Mfwd⁻¹(Lor) ⊆ Lor`" can be replaced by something intrinsic to `G`, e.g.
   posFwd on a larger input set, or a normalization `Mfwd = id` derivable from another clause.

## 6. What a later governed round could freeze (suggestion only; nothing here is frozen)

- **Q-SYM**: `frame_symm`, `gateRel_symm` and the swap lemma (`PosSepDraft.lean` §1). The statements are
  as drafted.
- **Q-SEP5**: at d = 5 with `n5`, `z5`, the squeezed gate `sqz` (ε = 1/10, λ = 1/2) as a `LinearEquiv`:
  - `sqz_frame` and `gateRel_sqz` (via `fin_cases`/`decide`, like `gJ5_frame`);
  - `sqz_symm_value = −1/2` and hence `not_posInv_sqz` (like `gJ5_value`);
  - `sqz_posFwd` (the squared N3.3 chain).
  Headline: `FwdGate (eball 5) z5 n5 sqz`, and by Q-SYM a gate with posInv and without posFwd.
- **Countercontrol to freeze alongside:** the λ = 1 gate with the exact value −1/40, so the round shows
  that the squeeze is load-bearing.
- **Q-AUT** (optional): `dim_of_fwdGate_aut` (N2.3) by re-running DIM-1 §Q with `Minv := Mfwd⁻¹`.
- A preregistered decision rule could read: SEP holds iff the frozen `posFwd` and `¬posInv` statements both
  compile with the axiom whitelist and the countercontrol's negative value compiles.

## 7. Files

- `possep_core.py`: exact carrier model mirroring the Lean definitions, PSD and cone certificates.
- `possep_gate.py`: the squeezed gate for any k ≥ 1.
- `possep_check.py`: all checks; prints PASS/FAIL; exit code 0 iff all pass.
- `run.log`: the latest full run.
- `keylemma_float.py`: exploratory float sanity check of the key-lemma constants (no verdict depends on it).
- `PosSepDraft.lean`: **UNBUILT** Lean draft (N1 proofs written; d = 5 statements with `sorry`).
