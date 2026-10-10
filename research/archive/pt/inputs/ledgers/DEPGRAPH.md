# EQ4-F — dependency graph, hardest steps, minimal assumptions (design only)

**Status.**
- Design only: no F, no CI dispatch, no merge, no ROADMAP or manuscript edit.
- Objects:
  - the preflight commit `f0d37906`, with D, P and S as elaborated in run 37900638054;
  - the certified base `bcbc516f`, read-only.
- No Lean toolchain is available locally, so every Lean statement proposed here is UNBUILT.

Evidence tags, as in FORMAL.md:
- **[K]** kernel-checked at the base or in the preflight's completed layer;
- **[X]** exact computation, replayed byte for byte;
- **[W]** written argument;
- **[M]** Mathlib v4.33.0 declaration.

Exact evidence in this note (§9). Every script runs with `python3 -I -B`, and every replay is byte-identical.

| script | checks | verdict | runs |
|---|---|---|---|
| `precheck_ie1first.py` | 12/12: K0 and M1–M11 | `IE1FIRST-PRECHECK-EXACT` | run 1 |
| `precheck_core.py` | 24/24: K0–K3, N1–N9, S0–S6, F1–F2 | `IE1FIRST-CORE-EXACT` | run 2; see below |
| `precheck_schmidt.py` | 4/4: K0, T1, T2, C1 | `SCHMIDT-ROUTE-EXACT` | run 1 |
| `review/review_checks.py` (the independent review, own code) | 21/21 | `REVIEW-CHECKS-EXACT` | run 1 |

Run 1 of `precheck_core.py` was a harness error: it computed N9 but did not assert it. That run is kept as `.run1.*`.
The decision rule is unchanged.

Independent review of this note: `review/REVIEW-DEPGRAPH.md`.
- Every mathematical claim was confirmed: Tasks 1–5.
- The eight errors (E1–E8) and ten gaps (G1–G10) it found are corrected in this version.

## 1. Findings

1. **IE₁ and the parity need no Pauli layer.**
   - The headline conclusion IE₁ (every pair, both tokens) follows from KT(4) without the Pauli dictionary, the PSD cone
     or complex numbers. So does the orientation parity `EvenCycle (orient A B)`.
   - Only the classification `K_p = twistQ3 (orient A_p B_p)` needs the Pauli layer.
   - The route:
     - Bell data and the cross relation `K01 = Θ(K23*)`; this uses the bipolar theorem and, on the ⊆ side, the Bell
       effects;
     - maximally entangled *rotation links* (gate images of product states);
     - invariance under conjugated z- and x-rotations;
     - Euler, which gives IE₁.
   - Parity: IE₁ reduces every post-local pair to `{I, reflY}²`, and Lemma P's witnesses then appear as memberships.
   - `hinv` (or the recurrence lemma (R) that replaces it) enters IE₁ itself, through the Bell effects of the ⊆ half of
     the cross relation, as well as the parity.
   - Independent review confirmed: review Task 1 (a)–(f), with no hidden Pauli use, no circularity and no (o) step.
2. **Headline closure under the recommended route ("IE₁-first", §5).**
   - The full headline needs **16** of the 48 open obligations.
   - The Pauli-free part (IE₁ + parity + cross relation) needs **11**; IE₁ alone needs 10.
   - **32** are off-headline: aligned-chart forms, Lemma B2, the remark, and the link-filter and chart-rule machinery of
     the earlier route. Under the earlier route the headline needed 30 (listed in §5).
3. **Hidden content.** The single obligation `kt4_general` hides:
   - 15 Pauli-free sub-lemmas (G1–G15, §4.1);
   - 13 Pauli-layer sub-lemmas (L1–L13, §4.2);
   - an optional recurrence lemma (R) that removes `hinv`.

   Exact-check coverage:
   - Every algebraic identity among them is covered by an exact pre-check, with these exceptions:
     - G3's composition and commutation laws;
     - L11(i);
     - the reflection bookkeeping of L9, L12 and G14 (`A = R_A ε_A`, `ε R ε ∈ SO(3)`).
   - Those exceptions are covered by the independent review's exact checks C7, C9, P2 and P3.
   - G2's inverse formula is N9.
   - The theorems (bipolar, Euler, Schmidt existence) are [W]/[M].
   - The Schmidt *construction* is checked exactly on seven matrices, including the rank-deficient cases.
4. **Hardest steps (§6):**
   1. the 2×2 Schmidt decomposition with SU(2) factors (L7; a constructive route with a real square root, pre-checked);
   2. the complex Pauli identities (L1, L2, L5, L6);
   3. self-duality of Q3 (O28);
   4. the bipolar theorem on `W 3` (O33);
   5. the bridge, Lemma B1 (O22);
   6. the Euler stabilizer lemma (O39).
5. **Minimal assumptions (§7).**
   - The proof reads: N-CLASS gates, products of unit ball states in each cone, the maximal-cone bound, convex cone,
     closed, forward gate preservation, and a core of the KT(4) structure (`KT4Core`).
   - `hinv` and `hgate` are each derivable from the other under `hcls ∧ hcl` [W, recurrence (R); confirmed by review].
   - The PreComposite fields `convex`, `prodEff_unit` and `prodState_combo_*` are not read.
   - Four-copy local tomography is not assumed.
   - Each remaining hypothesis row has a foil for at least one conclusion. The foils show that no hypothesis can simply be
     deleted; they do not show necessity.
   - **What the base supplies** (EQ4-SOURCE, audited, §7.7):
     - the KT(4) fields other than `tok` are constructible for every quadruple of nonempty pair bodies;
     - `tok` is supplied by nothing at the base;
     - `hgate`, `hinv` and `hcl` are implied by no stated premise.

## 2. The 48 obligations

Numbering is the file order of `FourCopyPackage.lean` at `f0d37906`; the review's independent enumeration agrees.

Difficulty: **c** cheap (finite real table algebra), **m** moderate, **h** heavy.

Columns:
- **A′**: in the closure of the Pauli-free headline (IE₁ + parity + cross relation).
- **A**: in the closure of the full headline (A′ + classification).
- "→" lists the open obligations and new lemmas it depends on.

| # | obligation | diff | route / evidence | → depends on | A′ | A | consumer if off-headline |
|---|---|---|---|---|---|---|---|
| O1 | `fourVal_eq_01` | c | `Finset.sum_comm` reshuffle [X f1 R1; review C6] | — | ✓ | ✓ | |
| O2 | `fourVal_eq_23` | c | [X f1 R2] | — | | | `target23` |
| O3 | `fourVal_eq_02` | c | [X f1 R3; review C6] | — | ✓ | ✓ | |
| O4 | `fourVal_eq_13` | c | [X f1 R4] | — | | | `target13` |
| O5 | `target23` | c | relabelling | O1, O2 | | | Lemma R completeness; not read by the IE₁-first route (target-side links replace it) |
| O6 | `target13` | c | relabelling | O1, O4 | | | as O5 |
| O7 | `effA_prodA` | c | [X f1 W1] | — | | | Lemma B2 (⇒) |
| O8 | `effB_prodB` | c | [X f1 W1] | — | | | Lemma B2 (⇒) |
| O9 | `effB_prodA` | c | [X f1 W2] | — | | | Lemma B2 (both) |
| O10 | `effA_prodB` | c | [X f1 W2] | — | | | Lemma B2 (both) |
| O11 | `effA_tens_eq_effB` | c | [X f1 W3] | — | | | W4 realizations of foils (§7.6) |
| O12 | `gateOf_symm_apply` | c | involutions [K CD:790] | — | | | O43 (supplies `hinv` for aligned gates, unless (R) removes `hinv`) |
| O13 | `nativeGate_cnotTw` | m | NativeGate clauses [X f1 C3–C4; W] | — | | | none: satisfiability control for `cnotTw` |
| O14 | `actC_reflY_cnot_actC_reflY` | c | `fin_cases` on units [X N7; review C9] | — | ✓ | ✓ | (parity witness reduction G14; orientation cases of L12. Avoidable: G14's four cases are concrete tables, review C7) |
| O15 | `NClass.ipW_map` | c–m | orthogonal `homMap`; `ipW_cnot` [K] | — | ✓ | ✓ | |
| O16 | `NClass.bell_state` | c–m | witness `A'⁻¹ xplus`, `B'⁻¹ z3` [X M9] | — | ✓ | ✓ | |
| O17 | `NClass.bell_effect` | c–m | same witness, `tens_sharpVec` [K] [X M9] | — | ✓ | ✓ | |
| O18 | `chartR_gateOf` | c | [X f2 X1–X2] | — | | | an alternative chart-transport route to Theorem B; not read by O43 as routed |
| O19 | `fourCopyCoherent_chart` | m | dual transport under reflections | O18 | | | as O18; also an alternative route for O47 |
| O20 | `abs_le_one_of_maxCone` | c | sharp effects ±eᵢ ⊗ ±eⱼ [review B1]; **restate** as `abs_le_00_of_maxCone` (§8) | — | ✓ | ✓ | |
| O21 | `exists_effect_of_dualW` | c–m | scale `c = 1/(1 + Σ|E_μν|)` | O20 | ✓ | ✓ | |
| O22 | `fourCopyCoherent_of_kt4` (B1) | m | §4.3 [review B2] | O1, O20, O21 | ✓ | ✓ | |
| O23 | `phiW_mem_Q3` | c–m | `pauliW phiW = v vᴴ` [X S6] | — | | | Theorem B, remark (subsumed by O34 on the headline) |
| O24 | `phiW_not_mem_twin` | m | singlet witness [X S6] | — | | | Theorem B, remark |
| O25 | `idW_not_mem_Q3` | m | the same fact as O24 through `actT reflY` | — | | | as O24 |
| O26 | `candidateCone_Q3` | m | products PSD; `Q3 ⊆ maxCone` | — | | | remark (realizations) |
| O27 | `isConvexCone_Q3` | c | `PosSemidef.add/smul` [M] | — | | | remark |
| O28 | `dualW_Q3` | m–h | ⊇: L1 + `psd_trace_mul_nonneg` [K OR:917]; ⊆: L3 with O34 | L1, L3, O34 | | ✓ | |
| O29 | `dualW_twin` | c | O28 and `ipW_actT_reflY` [K] | O28 | | ✓ | |
| O30 | `isClosed_dualW` | c | `isClosed_iInter` of closed half-spaces | — | | | `isClosed_Q3`, Theorem D |
| O31 | `chart_rule` | h | needs `ie1_Q3` (SU(2) ↠ SO(3)) | O40 | | | Theorem B / earlier route; not read by the IE₁-first route |
| O32 | `bellOf_mem_twistQ3` | m | from O31 and O23 | O31, O23 | | | as O31 |
| O33 | `dualW_dualW` (bipolar) | m | `geometric_hahn_banach_closed_point` [M]; functionals on `W 3` are `ipW E` | — | ✓ | ✓ | |
| O34 | `pureTab_mem_Q3` | c–m | L2 and `posSemidef_vecMulVec_self_star` [M] | L2 | | ✓ | |
| O35 | `link_conditional` | h | [X p1 C2, D2–D3] | — | | | earlier route only |
| O36 | `coverage` | h | complex square roots | — | | | earlier route only |
| O37 | `dense_generic` | m | `dense_pi`, `dense_compl_singleton` [M] | — | | | earlier route only |
| O38 | `Q3_subset_of_generic` | m–h | needs density; **restate** as `Q3_subset_of_pure` = L10 (§8), which needs none | O28, O33 (+ O37 as stated) | | ✓ (as L10) | |
| O39 | `so3_euler` | m | stabilizer lemma + `exists_euler_angles` [K ON:614] + `euler_apply_pole` [K ON:589; review C4] | — | ✓ | ✓ | |
| O40 | `ie1_Q3` | h | generator spin lifts with half angles + O39 | O39 | | | O31, O41; not read by the IE₁-first route |
| O41 | `ie1_twin` | m | from O40 | O40 | | | as O40 |
| O42 | `ie1Drive_of_ie1` | c–m | drive words are rotations [K ON:571–577] | — | | | corollary `kt4_forward_drive` |
| O43 | `kt4_aligned` | m | corollary of O44 (aligned gates are N-CLASS) + `kt4_parity_aligned` [K] | O44, O12 | | | Theorem B |
| O44 | `kt4_general` | m (assembly) | G1–G15, L1–L13 | §3 | (A′ part) | ✓ | |
| O45 | `kt4_closure` | m | O44 applied to closures + interior sandwich [M] | O44, O30 | | | Theorem D |
| O46 | `fcc_uniform_Q3` | m–h | `PosSemidef.kronecker` [M]; trace positivity [K OR:917] | O28 (⊆ half: dual-cone factors are PSD), O1 | | | remark; also the uniform-interface step of the convexity and closedness foils (§7.6) |
| O47 | `fcc_uniform_twin` | m | partial transposes of O46 | O46, O29 (or O46 + O19 + L11 with charts ε = (0, 1, 1, 0)) | | | remark |
| O48 | `not_fcc_odd` | m | Lemma P witness, value −1/8 [X f2 X3] | O26, `CandidateCone twin`, the gate preservations `cnot '' Q3 ⊆ Q3` and `cnotTw '' twin ⊆ twin`, via `kt4_parity_aligned` [K]; or O23 + O28 + O29 | | | remark |

Counts (confirmed by the review):
- **A′: 11** — O1, O3, O14, O15, O16, O17, O20, O21, O22, O33, O39. O14 enters through the parity only; IE₁ alone needs 10.
- **A: 16** — A′ plus O28, O29, O34, O38 (as L10) and O44.
- **Off-headline: 32**:

  | group | obligations | count |
  |---|---|---|
  | relabellings | O2, O4, O5, O6 | 4 |
  | Lemma B2 | O7–O11 | 5 |
  | aligned forms | O12, O13, O18, O19 | 4 |
  | Pauli facts | O23–O27 | 5 |
  | closedness and chart rule | O30, O31, O32 | 3 |
  | link filters | O35, O36, O37 | 3 |
  | spin lifts | O40, O41 | 2 |
  | drive corollary | O42 | 1 |
  | Theorems B and D | O43, O45 | 2 |
  | remark | O46–O48 | 3 |
  | **total** | | **32** |

- 16 + 32 = 48.

## 3. The graph of the headline closure

Edges point from a result to what it reads.
- **[K]** marks results completed at `f0d37906` or landed at the base.
- **new** marks a lemma to be stated (§4).

**The two headline theorems.**
- `kt4_forward` (A, full) reads O22 (B1), `kt4_general` and L13.
- `kt4_forward_ie1` (A′, new) reads O22 (B1) and `kt4_general_ie1` (new).

**`kt4_general_ie1` reads three results:**
- G5, the cross relation, which reads:
  - `incl_I` [K], `incl_II` [K];
  - O33 (bipolar);
  - G2 (Θ orthogonal, Θ⁻¹);
  - G4 (Bell data), which reads O15, O16, O17, `dualW_of_inv` [K] and G4a (sharp products in `dualW K`, from
    `sharpEff_isEffectOn` [K]).
- G13 (IE₁ for every pair), which reads:
  - `target01` [K], and `target02` [K mod O1, O3];
  - G9 (invariance transfer, 8 instances), which reads G5, G6, G7 (link family), G8 (rotated-link identities), O33,
    G2 (Θ injective) and `incl_I` [K];
  - G10 (rotations generate SO(3)), which reads O39 (Euler) and G3;
  - G11 (inclusion gives image equality) and G12 (IE₁ of the dual cone).
- G14 (parity), which reads:
  - G13 and G12;
  - G7 (state witnesses as gate images);
  - G4a, `dualW_of_inv` [K] and O15 (effect witnesses);
  - O14 and `cnotTw_apply` [K] (witness reduction);
  - `kt4_parity_of_witnesses`, which reuses the computation of `kt4_parity_aligned` [K].

**L13, the squeeze, reads** G5, G6, O28, O29 and L12 (the lower bound, once per pair).
- L12 reads:
  - L9 (pure tables in the cone), which reads L6, L7, L8, G7, G13 (IE₁) and cone scaling;
  - L10 (`Q3_subset_of_pure`), which reads L3, O28 and O33;
  - L11 (`transposeW` and reflection bookkeeping on Q3).
- O28 reads L1 (pairing identity), L3 (PSD criterion on pure tables), O34 and `psd_trace_mul_nonneg` [K OR:917].
  O34 reads L2.
- L6 reads L5, which reads L4.

**O22, Lemma B1, reads:**
- O1, O20 (restated), O21;
- the sub-lemmas B1a–B1e (§4.3);
- the fields of `KT4Core`.

## 4. Hidden sub-lemmas (to be stated before any freeze)

The statements are mathematical. Proposed Lean names are in code font.

Notation:
- `Θ g = bellOf(A02, B02) · g · bellOf(A13, B13)ᵀ`;
- `R_p = A_p · reflY · B_pᵀ`;
- `Mᵀ := toLin' (toMatrix' M)ᵀ`.

The unbuilt statement layer of G1–G15 is `drafts/FourCopyIE1Core.lean` (§10).

### 4.1 The Pauli-free core (IE₁, parity, cross relation)

G5, G6 and G9 are stated for a generic target in the `PairLinked` form. Instances:
- target 01, from `target01` [K], with links 02, 13 and `Θ = Theta A02 B02 A13 B13`;
- target 02, from `target02` (`upper` is `famII`, `lower` is `famI`), with links 01, 23 and
  `Θ′ = Theta A01 B01 A23 B23`.

Nonemptiness of the target cone, which O33 needs, comes from the products clause.

| id | statement | evidence | diff |
|---|---|---|---|
| G1 `Theta_eq` | `Θ g = actC R02 (actT R13 g)` (no orthogonality needed) | [X M5; review C1] (countercontrol without reflY fails) | c |
| G2 `Theta_orth`, `Theta_symm` | Θ is ipW-orthogonal; `Θ⁻¹ g = actC R02ᵀ (actT R13ᵀ g)` | [X M8, N9; review C2] | c |
| G3 `ipW_actC_adj`, `ipW_actT_adj`, `actC_comp`, `actC_actT_comm` | `ipW E (actC M X) = ipW (actC Mᵀ E) X` (same for `actT`); `actC M₁ ∘ actC M₂ = actC (M₁M₂)`; `actC` and `actT` commute | adjoints [X N6]; composition and commutation [review C9] | c |
| G4 `bell_mem`, `bell_mem_dual` (+ G4a `sharp_mem_dualW`) | `bellOf A_p B_p ∈ K_p` and `∈ dualW K_p`; G4a: `tens (sharpVec b) (sharpVec c) ∈ dualW K` for `K ⊆ maxCone`, unit b, c | O15–O17, `dualW_of_inv` [K]; G4a from the proof of `gate_sharp_mem_dualW` [K] | c |
| G5 `cross_rel` (generic) | for `PairLinked K K′ La Lb` with K closed convex, `bellOf Aa Ba ∈ La ∩ La*` and `bellOf Ab Bb ∈ Lb ∩ Lb*` (orthogonal locals): `K = Θ '' dualW K′` | (I) + (II) [K] + O33 + G2 [review Task 1(a)] | c given O33 |
| G6 `cross_rel_symm` (generic) | `K′ = Θ⁻¹ '' dualW K` (K′ closed convex) | G5 + O33 for K′ + G2 | c |
| G7 `link_family` | (i) `N (prodState (A'⁻¹x) (B'⁻¹y)) = actC A (actT B (cnot (prodState x y)))` for unit x, y; (ii) `cnot (prodState (rot3 a xplus) (rotX b z3)) = actC (rot3 a ∘ rotX b) phiW`; (iii) `actT (rotX b ∘ rot3 a) phiW = actC (rot3 a ∘ rotX b) phiW` | (i) [X M10 (equatorial x and yz-plane y); review C3 (general unit x, y)]; (ii) and (iii) [X N4, N5; review C4] (36 rational angle pairs each, base `rotFun`/`cyc3` transcribed [X K2]) | c–m (trig) |
| G8 `rot_link_*` (4) | links: `L₀₂ = actC A02 (actT B02 (actC M phiW))` and `L₁₃ = actC A13 (actT B13 (actC M phiW))`, with M = `rot3 a ∘ rotX b`. By G7(i)–(ii) these are the gate images `N_p(prodState …)`, hence in K02 and K13. By G7(iii) the same tables equal `actC A (actT B (actT M′ phiW))` with M′ = `rotX b ∘ rot3 a`. Identities: control side, left `L₀₂·g·bell13ᵀ = actC (A02 M A02ᵀ) (Θ g)` and right `bell02·g·L₁₃ᵀ = actT (A13 M A13ᵀ) (Θ g)`; target side, left `= Θ (actC (B02 M′ᵀ B02ᵀ) g)` and right `= Θ (actT (B13 M′ᵀ B13ᵀ) g)` | [X M6, M7, N1, N2; review C5 (links built as gate images)]; countercontrols (other conjugation order) fail on 48 units | c |
| G9 `invariant_of_links` (8 instances) | target 01: `actC (A02 M A02ᵀ) '' K01 ⊆ K01` and `actT (A13 M A13ᵀ) '' K01 ⊆ K01`; `actC (B02 M′ᵀ B02ᵀ) '' K23* ⊆ K23*` and `actT (B13 M′ᵀ B13ᵀ) '' K23* ⊆ K23*`; target 02 likewise with links 01 and 23 (tokens 0, 2 on K02; tokens 1, 3 on K13*) | famII + G5, G6, G7, G8, O33, G2 (Θ injective), `incl_I` [K] [review Task 1(d)] | m (bookkeeping) |
| G10 `so3_of_generators` | a set of maps closed under composition, containing `A·rot3 a·Aᵀ` and `A·rotX b·Aᵀ` for all a, b (A orthogonal), contains every rotation | O39; `A SO(3) Aᵀ = SO(3)` [review Task 1(e)] | m |
| G11 `image_eq_of_subset` | `(∀ R ∈ SO(3), actC R '' K ⊆ K) → ∀ R ∈ SO(3), actC R '' K = K` | inverse in SO(3) | c |
| G12 `ie1_dualW` | IE₁ K → IE₁ (dualW K); and IE₁ (dualW K) ∧ K closed convex → IE₁ K | G3, O33 | c |
| G13 `ie1_of_four_copy` | `∀ p, IE1 (K p)` | G9–G12 at targets 01 and 02 | m |
| G14 `parity_of_ie1` | IE₁ reduces post-locals to `ε ∈ {I, reflY}` (`A = R_A ε_A`, `R_A ∈ SO(3)`); then `actC ε_A (actT ε_B (cnot P)) = gateOf (ε_A ≠ ε_B) P` on Lemma P's witnesses, for states and effects; `kt4_parity_of_witnesses` gives `EvenCycle (orient A B)` | [X N8; review C7, C8 (all 16 patterns end to end: 0 even, −1/8 odd)]; O14; computation of `kt4_parity_aligned` [K] | c–m |
| G15 `kt4_general_ie1` | the assembly: IE₁ ∧ parity ∧ G5 | G5, G13, G14 | c |

**The IE₁ argument in four lines.**
1. With Bell links: `K01 = Θ(K23*)`.
2. With a rotated link `actC A02 (actT B02 (actC M phiW)) ∈ K02`, M = `rot3 a ∘ rotX b`, which is the gate image of
   `prodState (A02′⁻¹ rot3 a xplus) (B02′⁻¹ rotX b z3)`: family II gives `actC (A02 M A02ᵀ) (Θ f) ∈ K01**` for every
   `f ∈ K23*`.
3. With `K01 = K01** = Θ(K23*)`: `actC (A02 M A02ᵀ) '' K01 ⊆ K01`.
4. The maps M generate SO(3) (Euler), so `actC R '' K01 = K01` for every rotation R. The three other token sides follow
   in the same way (G8, G9, Lemma R at target 02).

Step tags:
- Steps 1 and 2 consume (2)-type data:
  - the native gate of a standalone link pair applied to its own product states (the Bell and rotated links);
  - the inverse gate's dual action on its own product effects (the Bell effects).
- Every inference step, 1–4, is (s)-type, "(s) on (2) data" (FORMAL S11).
- No step uses Q3, the twin, `pauliW` or ℂ. No (o) step occurs.

### 4.2 The Pauli layer (classification)

| id | statement | evidence | diff |
|---|---|---|---|
| L1 `ipW_eq_trace` | `ipW E X = 4·Re tr (pauliW E · pauliW X)` | [X S3; review P1] | m (elaboration) |
| L2 `pauliW_pureTab` | `pauliW (pureTab C) = v vᴴ`, `v = (C00, C01, C10, C11)` in `tensorOf` order | [X S2; review P1] (`pauli1`, `pauliW`, `pureTab`, `tensorOf` transcribed [X K1]) | m |
| L3 `mem_Q3_of_nonneg_pure` | `(∀ C, 0 ≤ ipW E (pureTab C)) → E ∈ Q3` | L1, L2, `posSemidef_iff_dotProduct_mulVec` [M], `pauliW E` Hermitian | m |
| L4 `su2_form`, `spinRot_mem` | U ∈ SU(2) has the form `!![a, b; -b̄, ā]` with `‖a‖²+‖b‖² = 1`; `R_U[j][k] = ½ Re tr(σⱼ U σₖ Uᴴ)` is in SO(3) | [X S4a; review P5] (rational unit quaternions) | m |
| L5 `pauli_conj` | `Uᴴ σⱼ U = Σₖ R_U[j][k] σₖ` | [X S4b] | m |
| L6 `pureTab_conj` | `pureTab (U C Vᵀ) = actC R_U (actT R_V (pureTab C))` | [X S4c; review P5] (with `R_Uᵀ` it fails) | m |
| L7 `schmidt2` | `∀ C, ∃ U V ∈ SU(2), ∃ d₀ d₁, C = U · diag(d₀, d₁) · Vᵀ` | constructive route [W] with exact check [X precheck_schmidt T1, 7 matrices incl. rank one, `q = 0` both orders, real, zero]. Steps: 1. M = CᴴC = [[p, q], [q̄, r]]. 2. For q ≠ 0, the eigenvalue `λ = (p + r + √((p − r)² + 4|q|²))/2` (a **real** square root) with eigenvector `(q, λ − p)`; for q = 0, `e₀` or `e₁`. 3. `W = [w, (−w̄₁, w̄₀)] ∈ SU(2)` by construction. 4. `c₁ = Cw`, `U = [u, (−ū₁, ū₀)]` with `u = c₁/|c₁|` (U = 1 if C = 0). 5. `D = Uᴴ C W` is diagonal and `V = W̄`. No SVD and no algebraic closure are needed. | **h** |
| L8 `pureTab_diag` | `pureTab (diag(d₀, d₁)) = (‖d₀‖²+‖d₁‖²) • cnot (prodState x z3)` with x the Bloch vector of `(d₀, d₁)` (`d ≠ 0`) | [X S1 (real d₀), precheck_schmidt T2 (complex d₀); review P4] and [X S0] (`cnot` is `Ad CNOT`) | m |
| L9 `pure_mem_of_ie1` | K a cone (closed under nonnegative scaling, including 0), IE₁ K, and `actC A (actT B (cnot (prodState x y))) ∈ K` for unit x, y → `∀ C, actC ε_A (actT ε_B (pureTab C)) ∈ K`. Uses `ε R ε ∈ SO(3)` for `ε ∈ {I, reflY}`, `R ∈ SO(3)` | L6–L8, G7, G13; the chain is [X precheck_schmidt T2]; reflection bookkeeping [review C7, P3] | m |
| L10 `Q3_subset_of_pure` (replaces O38) | K closed convex cone, `∀ C, pureTab C ∈ K` → `Q3 ⊆ K` | `K* ⊆ Q3` by L3, then `Q3 = Q3* ⊆ K** = K` (O28, O33) | m |
| L11 `transposeW_pureTab`, `actC_reflY_Q3` | (i) `transposeW (pureTab C) = pureTab (C.map star)`; (ii) `actC reflY '' Q3 = twin` | (i) [review P2; also derived from X S5 + S2]; (ii) [X S5; review P3] | c–m |
| L12 `lower_bound` | `twistQ3 (orient A_p B_p) ⊆ K_p` | L9–L11 [review Task 2: all four ε cases] | m |
| L13 `squeeze` | `K_p = twistQ3 (orient A_p B_p)` for every p | `C01 ⊆ K01 = Θ(K23*) ⊆ Θ(C23*) = Θ(C23)` and `Θ(C23) ⊆ Θ(K23) ⊆ C01` (G5, G6, O28, O29, L12); the other pairs through G5, G6 at target 02 | c |

The squeeze needs neither `chart_rule`, nor `Q3 ≠ twin`, nor `ie1_Q3`. That is why O24, O25, O31, O32, O40 and O41
leave the headline.

**Optional (R) `inv_mem_of_orth`.**
- Statement: for N ipW-orthogonal, K closed and `N '' K ⊆ K`, also `N.symm '' K ⊆ K`. Confirmed by the review.
- Pointwise proof [W], the simpler Lean route:
  - fix ω ∈ K. The orbit `Nⁿω` lies on a Euclidean sphere, so by `tendsto_subseq_of_bounded` [M] it has a convergent
    subsequence;
  - hence for every ε there is m ≥ 1 with `‖N^m ω − ω‖₂ < ε`, using the isometry;
  - so `‖N^{m−1} ω − N⁻¹ω‖₂ < ε` and `N^{m−1}ω ∈ K`;
  - K is closed, so `N⁻¹ω ∈ K`.
- The Euclidean norm `√(ipW X X)` is within a factor 4 of `W 3`'s sup norm.
- Difficulty: m.

### 4.3 Lemma B1 (O22), the bridge, in detail

Route [W], confirmed by the review [review Task 3, B1, B2]. Every step was traced against the COMP-1 fields at
CI:200–246. Unbuilt proof draft: `drafts/FourCopyBridge.lean`.

| step | content | reads |
|---|---|---|
| B1a | `|ω μ ν| ≤ ω 0 0` on `maxCone (eball 3)`, hence `ω 0 0 = 0 → ω = 0` | sharp effects `±eᵢ ⊗ ±eⱼ` and the unit (restated O20) |
| B1b | `X ∈ K`, `X 0 0 > 0` → `flatW (X 0 0⁻¹ • X) ∈ pairBody K` | the cone half of `IsConvexCone` |
| B1c | `E ∈ dualW K` → `c • Σ E μν • tabCoord μ ν` is `IsEffectOn (pairBody K)` | O21 (CandidateCone, maximal-cone half) |
| B1d | `tabCoord μ ν (flatW ω) = ω μ ν`; bilinear expansion `prodEff (Σ…) (Σ…) = Σ Σ E F • prodEff (tabCoord) (tabCoord)` | `prodEff` is a bilinear `LinearMap`; `map_sum`, `map_smul` |
| B1e | famI: state `PA.prodState x̂ ŷ ∈ PA.Ω = PB.Ω`; effect `PB.prodEff e_E f_F` (an effect by `prodEff_effect`); `tok` turns `PB` coordinate products into `PA` ones; `prodEff_apply`; the value is `c c′ · fourVal x̂ ŷ E F`, which O1 identifies. famII is symmetric (`PB.Ω ⊆ PA.Ω`; `tok` read in the other direction) | `prod_mem`, `prodEff_effect`, `prodEff_apply`, `one_body` (both inclusions), `tok` |

Fields read:
- `prodState`, `prodEff` (linearity), `prodEff_apply`, `Ω`, `prod_mem`, `prodEff_effect`;
- `one_body` and `tok`.

Fields not read: `convex`, `prodEff_unit`, `prodState_combo_left/right` and `Composite.lt`. Closedness and the gates are
not read either.

## 5. Route comparison

| | IE₁-first (recommended) | link-filter (FORMAL S8–S16) |
|---|---|---|
| how IE₁ is obtained | rotation links + Euler, before any classification; Pauli-free | from `K_p = twistQ3` and `ie1_Q3`/`ie1_twin` (SU(2) ↠ SO(3) generator lifts with half angles + Euler) |
| how the lower bound is obtained | IE₁ + Schmidt (L7) + spin lift in the easy direction U ↦ R_U (L4–L6), polynomial in a, b, with no trigonometry | filtered conditionals (O35) + coverage with complex square roots (O36) + density (O37) |
| upper bound and orientation | squeeze through both cross relations (L13); no `chart_rule` | `chart_rule` (O31) on `Θ(C23)` |
| parity | Pauli-free (G14: IE₁ + Lemma P's witnesses) | determinant bookkeeping after classification |
| open obligations of the 48 on the headline | 16 (11 for A′) | 30 |
| new statements | G1–G15, L1–L13 (+ R) | about 15 hidden assembly lemmas |
| smallest stop answering "KT(4) ⇒ IE₁" | A′: B1, bipolar, Euler, N-CLASS facts and cheap algebra | none short of the full Pauli layer |

The 30 obligations of the earlier route (review §4 reconstruction, adopted):
- O1–O6, O15–O17, O20–O22;
- O23–O25, O28–O30, O31–O32;
- O33, O34, O35–O38;
- O39–O41, O44.

Both routes need the bipolar theorem, Euler and Lemma B1. The IE₁-first route replaces O31, O35–O37, O40 and O41 by
L4–L8 and the cheap G-series. Its decisive identities are pre-checked exactly:
- M1–M11 and N1–N9 (rotation links, Θ, reflection charts, witness reduction);
- S0–S6 (Pauli conventions at the package's exact definitions);
- precheck_schmidt T1–T2 (the constructive L7 and the chain L6–L8).

## 6. Critical path and hardest steps

**Critical path to A′:**
1. O33 (bipolar), then G5/G6, then G9, then G10 (with O39), then G13, then G15.
2. In parallel: O20, then O21, then O22 (B1); and O15–O17, then G4.

**Critical path to A:** the A′ path, then L7 (Schmidt), then L9, then L12, then L13. In parallel: L1/L2, then L3, then
O28, then L10, and L4, then L5, then L6.

| rank | step | why hard | Mathlib / base anchors | risk |
|---|---|---|---|---|
| 1 | L7 `schmidt2` | no SVD in Mathlib. The constructive route (real square root, explicit SU(2) completion, phase handled by `V = W̄`) is pre-checked; the Lean work is complex arithmetic in 2×2 and the rank-deficient branches | `Real.sqrt` [M]; no eigenvalue API needed | medium |
| 2 | L1, L2, L5, L6 | complex polynomial identities over 16 entries; heartbeat pressure | structure through Pauli orthogonality and `tr` of Kronecker products (`Matrix.trace_kronecker` [M]) instead of brute `simp` | medium |
| 3 | O28 `dualW_Q3` | glue of L1, L3, O34 and `psd_trace_mul_nonneg` [K OR:917]; Hermitian bookkeeping | `posSemidef_iff_dotProduct_mulVec` [M] | medium |
| 4 | O33 `dualW_dualW` | `W 3` carries the sup norm (no inner-product instance); continuous functionals must be represented as `ipW E` | `geometric_hahn_banach_closed_point` [M] (used at the base, CI:174) | medium |
| 5 | O22 Lemma B1 | affine-map algebra of COMP-1 (`→ᵃ[ℝ]` as a module, `coord`, `flatW` through `finProdFinEquiv`); `tok` in both directions | CI:85, CI:104–117 (`evalAddHom`, `affine_sum_apply`), CI:216–230 [K] | medium (unbuilt draft written) |
| 6 | O39 `so3_euler` | the stabilizer lemma (a rotation fixing `e₃` is `rot3 φ`); angles from (c, s) | `exists_euler_angles` [K ON:614], `euler_apply_pole` [K ON:589], `Complex.cos_arg`/`sin_arg` [M] | low–medium (unbuilt draft written) |
| 7 | G9/G13 | volume: 8 invariance instances, images of `LinearEquiv` coercions in `''` | — | medium (elaboration) |
| 8 | (R) | only if `hinv` is dropped | `tendsto_subseq_of_bounded` [M] (Topology/MetricSpace/Sequences.lean:38) | medium |

The rest of the headline:
- **c:** O1, O3, O14, O20, G1–G6, G8, G11, G12, G15 and L13.
- **c–m:** O15–O17, O21, G7, G14 and L11.
- **m:** G10 (O39 plus bookkeeping).

## 7. Exact minimal assumptions for the headline

### 7.1 Hypotheses the IE₁-first proof reads (field level)

| hypothesis | where it is read |
|---|---|
| **`KT4Core`**: of each pre-composite, `prodState`, bilinear `prodEff`, `prodEff_apply`, `Ω`, `prod_mem`, `prodEff_effect`; plus `one_body` and `tok` | B1 only (§4.3) |
| **CandidateCone, products**: `prodState x y ∈ K_p` for unit x, y (all ball points follow by convexity) | Bell state (G4), link states (G7), gate images (L9) |
| **CandidateCone, maximal-cone bound**: `K_p ⊆ maxCone (eball 3)` | B1a/B1c (effects from dual tables); sharp products in `dualW K_p` (G4a), hence Bell and parity effects |
| **IsConvexCone** | B1b (scaling); bipolar O33 in G5, G6, G9, G12, L10; scaling in L9 |
| **IsClosed** | bipolar `K = K**` (G5, G6, G9, G12, L10); (R) |
| **N-CLASS** `hcls` | Θ (G1, G2); Bell data (O15–O17); link family (G7); orientation (G14, L12); orthogonality of all four locals (O15, through `dualW_of_inv` and (R)) |
| **forward gate preservation** `hgate` | Bell states, link states, gate images |
| (`hinv`, the backward half) | Bell effects in `dualW K_p` (G4): the ⊆ half of the cross relation, hence **IE₁ itself**; parity effects (G14). Both through `dualW_of_inv` [K] |

### 7.2 Redundant given the others

- **`hinv` and `hgate` are each redundant given the other**, under `hcls ∧ hcl` [W, (R); confirmed by the review]:
  - (R) gives `N_p⁻¹ '' K_p ⊆ K_p` from orthogonality (O15), forward preservation and closedness;
  - (R) applied to `N_p.symm` gives `hgate` from `hinv`.
  - The minimal list keeps `hgate` and drops `hinv`, at the cost of (R), which is moderate.
- **Closedness is redundant for the parity conclusion** [W; confirmed by the review]:
  - every hypothesis passes to closures (dual cones unchanged; both families are continuous in their state slots;
    `maxCone` is closed; the gates are continuous);
  - the parity speaks only of the gates' post-locals.
- **Pre-locals `A′, B′`** are read in two ways only:
  - through their orthogonality: O15, used by `dualW_of_inv` and by (R), and keeping `A′ᵀx`, `B′ᵀy` in the ball;
  - through the reparametrized inputs `A′ᵀx`, `B′ᵀy`.

  No conclusion depends on their values.

### 7.3 Carried but not read

- The `PreComposite` fields `convex`, `prodEff_unit` and `prodState_combo_left/right`.
- `Composite.lt` (four-copy local tomography) in `kt4_forward_lt`.
- This holds at route level [W; confirmed by the review]. A statement over `KT4Core` would certify it (§8, SC7).

### 7.4 Built in (definitional, not hypotheses)

- Two-copy local tomography: pair cones are read in DIM-1's table carrier `W 3` [K CD:95–97].
- The elementary body `eball 3`.
- Fixed per-token charts, shared by the pairs containing the token.
- The instance: pairs 01, 23, 02, 13.
- The Euclidean pairing `ipW` and full dual cones in the interface. This is the full-effect reading, the COMP-1
  quantifier over `IsEffectOn` [K KF:116, CI:228].

### 7.5 Not assumed

- Four-copy local tomography.
- IE₁, of any pair or any token.
- Uniform composition: the four cones may differ.
- `IsNot`, `CtrlGate` positivity, unit preservation, or any other two-copy premise beyond N-CLASS.
- Any operation on part of the four-copy composite ((o) steps).
- Purification, transitivity, Choi-state availability.
- Any three-copy structure.
- Any complex or Pauli structure: ℂ enters only the statement and proof of the classification conclusion.

### 7.6 Deletion foils per conclusion

A foil is a model of the other hypotheses in which the conclusion fails. It shows that the deleted hypothesis cannot be
removed without replacement. It does not show necessity (the P/A/C rule).

Notes for reading the table:
- Conclusions: (A1) classification, (A2) IE₁, (A3) parity.
- Foils are given per table row. The individual `KT4Core` fields `prod_mem`, `prodEff_effect`, `prodEff_apply` and
  bilinearity have no separate foils.
- The rows are relative to the minimal list (§7.2: `hinv` removed).
- R1 denotes the cone of pure tables `{s • pureTab C | s ≥ 0}`, the rank-≤ 1 part of Q3.
- "given O46" marks a foil whose uniform interface rests on the open obligation O46 (`fcc_uniform_Q3`).

| deleted | (A1) | (A2) | (A3) |
|---|---|---|---|
| KT(4) (whole `KT4Core`) | `C_H`, `K_F` [X EQ3 p6 H3, p2 F1] | `C_H`: KT(4) fails at −1/200 [X EQ3 p6 H3]; not IE₁, since `phiW ∈ C_H` while `ψ₁ = actT R_H phiW ∉ C_H` (linear witness `W = 2e₀₀ − ψ₁`, value −2 [review F1]; non-product images [X F2]) | odd pattern (Q3, Q3, Q3, Tw) [X f2 X3; audit P1] |
| `tok` | the anchor sum with C_H: every other `KT4Core` field holds for every quadruple of nonempty pair bodies [X SOURCE s1 A1–A3; coordinator audit AS + W], and C_H ∉ {Q3, Tw} | the same, with C_H not IE₁ [review F1] | M_ρ and M_tw: every other hypothesis of `kt4_forward` holds, local tomography of both groupings too; cones (Q3, Q3, Q3, Tw), so the twist bits are forced odd [X SOURCE s1 R1–R6, T1–T5; coordinator audit MR (−1/8) + W] |
| `one_body` | `C_H` in the `W4` table model with separate product hulls [W, O11] | the same [W] | odd pattern in the same model [W] |
| products in `K_p` | `K_p = {0}` [W, trivial] | none known (trivial cones are IE₁) | `{0}` with an odd gate pattern [W] |
| maximal-cone bound | `K_p = W 3` [W] | none known (`W 3` is IE₁) | `W 3` with an odd gate pattern [W] |
| convexity | `R1 ∪ SEP ∪ cnot SEP` [X F1 + W, given O46]: closed, contains the products, `cnot`-invariant, uniform interface since its dual is Q3 | the same: `ρ = cnot σ` lies in it while the rotated `ρ′ = actT R_H ρ` (PSD, rank 2, neither ρ′ nor `cnot ρ′` PPT; determinants −135/4096) does not [X F1; review F2] | not examined |
| closedness | `int Q3 ∪ conv(SEP ∪ cnot SEP)` [X+W EQ3 p2 F4, given O46] | the same: `ψ₁` is pure, entangled and `cnot`-entangled [X F2; review F3], and `conv(SEP ∪ cnot SEP) ⊆ C_H`, which F1's witness separates from ψ₁ | none possible: redundant (§7.2) [W] |
| N-CLASS | SEP with `N = id` [X EQ3 p2 F2 for KT(4)] | none known | not applicable (the conclusion names N-CLASS data) |
| forward gate (with `hinv` removed) | SEP, max [X EQ3 p2 F2] (they also violate `hinv`, as `cnot` is an involution) | none known | Q3 uniform with an odd gate pattern [W, given O46] |
| `hinv` | redundant given `hgate` (§7.2) [W] | redundant [W] | redundant [W] |
| full-effect reading | `K_F` with Q3-restricted effects [X+W EQ3 p2 F3] | `K_F` (finite Clifford symmetry) [X+W] | not examined |

What the table shows:
- For **(A1)**, every row of the minimal list has a foil.
- For **(A2)**, the foils cover KT(4), `tok`, `one_body`, convexity, closedness and the effect reading. For N-CLASS, the
  forward gate and the two CandidateCone clauses no non-IE₁ foil is known. Whether they are redundant for IE₁ alone is
  **open**.

**Scope.**
- No hypothesis is claimed necessary. Necessity of A relative to P needs a proof of P ∧ C ⇒ A, and none is given.
- `tok` is in fact not necessary relative to the other hypotheses: M_id and M_T [X SOURCE s1 I1–I2] satisfy every
  other hypothesis and the conclusion, with `tok` false.
- The (A2) rows marked "none known" are open questions, not redundancy claims.
- The realizations of FCC-level foils as `KT4Core` data are written arguments:
  - EQ4-SOURCE's σ-construction gives `FourCopyCoherent ⇒ ∃ KT4` [W + X SOURCE s1 S1–S4, T1];
  - building it would need O7–O11 and a realization lemma, which is not among the 48.

### 7.7 What the base supplies (EQ4-SOURCE, audited)

USES (§7.1) against SUPPLIES:

| hypothesis | SUPPLIES class | basis |
|---|---|---|
| `KT4` fields `PA`, `PB`, `pairBody` normalization | **[K]** | `Model.modelData.minPre` [K CI:528, CI:686] for every quadruple |
| `one_body` | **[U] route** | the anchor sum constructs it for every quadruple of nonempty pair bodies. It is supplied vacuously, with `tok` false there |
| `tok` | **[U] countermodel** | no structure with three or more tokens exists at the base [X SOURCE s0]. Without `tok` the headline fails (M_ρ, M_tw) |
| `FourCopyCoherent` (produced by B1) | **[U] countermodel** | relative to `KT4` minus `tok`: M_ρ and M_tw at −1/8 |
| `hadm` | **[T]** | transported from COMP-1's body bounds. The two-copy composite itself is K2, OPEN |
| the `W 3` carrier | **[T]** | DIM-1's carrier premise |
| `hcls` (N-CLASS) | **[U] route** | EQ2-B's derivation from the K1 gate premises (unbuilt; the K1 premises are unsourced) |
| `hgate`, `hinv` | **[U] countermodel** | implied by no stated premise: the landed `ball3MaxComposite` and `ball3MinComposite` bodies with `cnot` violate them (`cnot idW = chainW` at −1/2; `F(phiW) = −2`) [X SOURCE s2 G1–G2; coordinator audit G] |
| `hcl` | **[U] countermodel** | the closure foil |

The four-token content of KT(4) is carried by `tok` alone, since every other field is supplied vacuously.

The missing physical link is token identity across groupings. TokProdState says that four token states prepared
independently give one state of the four-token body, whichever grouping composes them. Relative to local tomography of
one grouping, TokProdState is equivalent to `tok` [W, with a separate witness for each direction].

This corrects FORMAL §2, which labelled H-gate, H-inv and H-NCLASS "transported".

## 8. Recommended statement changes before any freeze

| id | change | reason |
|---|---|---|
| SC1 | add `kt4_forward_ie1` and `kt4_general_ie1` (conclusions: IE₁, `EvenCycle (orient A B)`, cross relation) beside the full forms | the owner's target, KT(4) ⇒ IE₁, is reachable without the Pauli layer (11 of the 48 + G1–G15) |
| SC2 | add `kt4_parity_of_witnesses` (the four witness memberships as hypotheses); `kt4_parity_aligned` becomes a corollary | general-chart parity reuses the kernel-checked computation |
| SC3 | restate O20 as `abs_le_00_of_maxCone : |ω μ ν| ≤ ω 0 0` | yields both the slice bound and `ω 0 0 = 0 → ω = 0` (B1a) |
| SC4 | replace O38 by `Q3_subset_of_pure` (L10) | the IE₁-first route supplies all pure tables; no density needed |
| SC5 | state G1–G15 and L1–L13 explicitly, each citing its pre-check; G5, G6 and G9 in the generic `PairLinked` form | `kt4_general` must not hide about 28 lemmas behind one `sorry` at freeze time |
| SC6 | state (R) and drop `hinv` from the headline (recommended), or keep `hinv` and record its redundancy in the design note | minimal hypothesis list; (R) is moderate |
| SC7 | introduce `KT4Core` (the consumed fields) with `KT4.toCore` and `KT4LT.toCore`; state B1 over `KT4Core` | certifies that `convex`, `prodEff_unit` and `prodState_combo_*` are not read |
| SC8 | move O5, O6, O2 and O4 (Lemma R for targets 23/13) out of the headline round (prove them, cheap, or defer) | no headline consumer |
| SC9 | defer O31, O32, O35–O37, O40, O41 (chart rule, filters, generator lifts) to a later round or drop them | no headline consumer under the IE₁-first route |
| SC10 | keep the remark (O46–O48), Lemma B2 (O7–O11) and Theorems B and D (O43, O45) in separate rounds | off-headline; B2 and O11 also back the foil realizations, and O46 backs two foils |

**Proposed round order** (each would be a native round, §A.39; owner decides):
1. **R-A′.** O1, O3, O14–O17, O20′, O21, O22 (B1 over `KT4Core`), O33, O39, G1–G15, (R), and `kt4_forward_ie1`.
   KT(4) ⇒ IE₁ ∧ parity, Pauli-free.
2. **R-A.** O28, O29, O34, O38 (as L10) and O44, the five A adds to A′, with L1–L13. `kt4_forward` follows by
   composition. This is the classification.
3. Later rounds: Theorems B and D, Lemma B2, the remark, and the drive corollary O42.

**Before R-A′ can freeze**, its heavy steps (O33, O39, O22, G9/G13) need proofs that compile. Without a local toolchain
that needs design runs on the disposable branch, which are not authorized now.

## 9. Evidence log

Scripts in `scratchpad/eq5/F/` run as `python3 -I -B <script> <base>/verification/lean-mathlib/OIBridge [<package>]`.
- Exact arithmetic only.
- Each decision rule was fixed before the first run.
- No timing appears in stdout.
- `.err` files are empty.
- Python 3.11.15, sympy 1.14.0.
- Hashes are the first 16 hex digits of sha256.

| script | sha | output sha | checks | verdict | runs |
|---|---|---|---|---|---|
| `precheck_ie1first.py` | `f6c287e5939e8c97` | `f563c32d4cbea024` | 12/12 | `IE1FIRST-PRECHECK-EXACT` | run 1; replay identical |
| `precheck_core.py` | `03d7ede627597fc7` | `0821b76e67eb3084` | 24/24 | `IE1FIRST-CORE-EXACT` | run 2; replay identical. Run 1 is kept as `.run1.*` (`.py` `e9b4bdbb851c3967`, `.out` `003120466b92f22b`): a harness error, as N9 was computed but not asserted, so its 23/23 verdict did not implement the stated rule |
| `precheck_schmidt.py` | `e960458112c5f4b2` | `dd7045d68be5c570` | 4/4 | `SCHMIDT-ROUTE-EXACT` | run 1; replay identical |
| `review/review_checks.py` (independent reviewer) | `96a147de0eb2ca45` | `8127bfd9e7f239bc` | 21/21 | `REVIEW-CHECKS-EXACT` | run 1; replay identical |

Inputs read by the scripts:
- `precheck_core.py` reads the package at `f0d37906` (`FourCopyPackage.lean`) for `pauli1`, `pauliW` and `pureTab`.
- It reads the base for `tensorOf`, `rotFun`, `cycEquiv`, `rotX`, `nflip`, `reflY`, `sgn`, `pc` and `pt` (K0–K3).

**Countercontrols that failed as required:**
- M5: without reflY, 60 unit failures.
- M6, N1: the other conjugation order, 48 each.
- S1: the conjugate phase.
- S4c: `R_Uᵀ`, 20 of 25 pairs. Five pairs coincide because `R_U` is symmetric when `q₀ = 0`.
- F1 control: separable σ is PPT, with determinant 0.
- F2 control: a product state has marginal norm 1.
- precheck_schmidt C1: `V = W` without conjugation.

## 10. Unbuilt Lean drafts (`drafts/`; no toolchain; design evidence only after a design run)

| file | content | status |
|---|---|---|
| `FourCopyBridge.lean` | B1a (restated O20) and corollaries, B1d, O21, O1, `KT4Core`, `KT4.toCore`, `KT4LT.toCore`, B1 over `KT4Core`, O22 as its corollary | proofs written in full; `-- ITER:` marks the points likely to need elaboration iteration |
| `FourCopyEuler.lean` | fixing the origin, rotation matrices, `IsRot3` closure, the stabilizer lemma, O39 | proofs written in full; `-- ITER:` markers |
| `FourCopyIE1Core.lean` | the statement layer of G1–G15 and `kt4_forward_ie1`; short proofs (G4a, G4b, G9 generic, G14a, A′ from C′) | statements; other proofs are explicit design placeholders |

Consistency-axis work only; bands unchanged.
