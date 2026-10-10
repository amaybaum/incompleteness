# EQ3-P — composition coherence as the source of idle extension (design only)

Research and design only. Base: certified main `bcbc516f`, read-only at `scratchpad/eq/base/` (manifest checked at the
start and at the end). Nothing here is adopted, frozen or governed. No Lean was built (no toolchain); every Lean text
is **UNBUILT**. Evidence tags:
- **[K]** landed kernel identifier at the base, `file:line` (paths under `verification/lean-mathlib/OIBridge/`);
- **[X]** exact computation in this directory, over green controls, replayed byte for byte;
- **[W]** written argument here, not kernel-checked;
- **[L]** literature, **unverified** (the hosts serving the papers were egress-blocked; only search summaries were
  seen);
- **[F]** floating-point exploration, which certifies nothing.

Running record: `NOTES.md`. Amendments 1 and 2 (appended to `eq3/PROTOCOL.md` during the thread) are addressed
throughout and audited in §1.2–§1.5.

Abbreviations: CD CompositeDimension, CI CompositeInterface, K2G K2Guard, KF KInfFoundations. `Q3` = PSD two-qubit
tables, `Tw = actT reflY '' Q3` (the twin), `T` = global transpose (`transposeW`), `Δ = phiW = diag(1,1,−1,1)`,
`R_B = actT reflY` (table map `ω ↦ ω·Δ`), `cnot' = R_B ∘ cnot ∘ R_B`. A pair cone's dual `K*` is the Euclidean dual in
table coordinates (= its `IsEffectOn` effects up to normalization). "Admissible" = `CandidateCone` (K2G:95).

## 0. Answer to the key question

> Can the requirement that an operation remain valid when an independent system is added be derived from a genuinely
> observational consistency principle, without assuming quantum composition in advance?

**Two copies (IE₁): POSITIVE, at a stated finite instance (theorem route).** The instance is KT(4; 01|23, 02|13): four
tokens, and one four-copy body that is a COMP-1 composite of the grouping 01|23 and also of the grouping 02|13. Each
group carries its full body and all of its `IsEffectOn` effects.
- **Premises on each standalone pair composite:**
  - its body is a closed admissible cone;
  - its native gate (IsNot + CtrlGate, in N-CLASS form) is an operation of that standalone pair.
- **Not assumed:**
  - no local invariance;
  - no uniform composition (the four pair cones may differ, in arbitrary token charts);
  - no exchange symmetry;
  - no operation on part of a larger composite.
- **Conclusions:**
  - every pair cone is Q3 or the twin in its token charts, and its gate's orientation decides which;
  - so every pair composite is invariant under all local rotations — this is **IE₁, derived** — and under all local
    filters;
  - the 4-cycle of twist bits is even.
- **Load-bearing premises, each with a countermodel:**
  - coherence of the two groupings: `C_H` and `K_F`, at −1/200 (exact);
  - the gate: SEP and max (exact);
  - closedness: `int Q3 ∪ conv(SEP ∪ cnot SEP)` (written, with exact ingredients);
  - the full effect sets: `K_F` with effects restricted to Q3 (written, with exact ingredients).

**Three copies (IE₂): OPEN, with the named wall refined.**
- **What the six-copy instance KT(6) gives** (groupings 012|345, 03|1425, 14|25):
  - both co-self-duality inclusions, `K₀₁₂ = T₃(K₃₄₅*)`;
  - invariance of the three-copy cone under all local filters (SLOCC);
  - this excludes the minimal hulls `M_bs` (−1/16), `M_tw` and `M_odd`.
- **What it does not decide:** whether a closed, SLOCC-invariant, co-self-dual three-copy cone between the biseparable
  hull and its dual must be `PSD₈` (c = 0), or cannot exist (c = 1).
  - For c = 0 this is equivalent to: must such a cone contain one GHZ-class state?
- **No-generation lemma [W]:** state-level coherence cannot generate a GHZ-class state from pair-level data. If KT∞
  implies IE₂, it does so through its self-duality fixed point at every level, not by generation.
- No exclusion lead was found for the surviving candidates [F]. No countermodel was found either.

**The owner's decisive question:**

> Does consistency of states, effects and conditioning across groupings force the transformations permitted on
> smaller systems to remain valid inside larger systems, with no extended operation among the premises?

- For one-token operations inside two-token systems: **yes**, at the four-copy instance, given the landed two-copy
  premises and closedness. The only operation premise is the native gate on standalone pairs, a (2)-type premise.
- For two-token operations inside three-token systems (IE₂): **not established**.

**Owner's outcome table:**
- At two copies: case 1, "coherence alone selects the quantum cone".
  - It holds given the transported two-copy premises and closedness, with the twin as the per-pair orientation
    alternative.
  - Both inclusions are proved.
  - Uniform composition is not needed, and no additional finite symmetry is needed.
- At three copies: none of the five cases is reached.

## 1. Finding

The four-copy instance of composition coherence says strictly more than co-self-duality. Its two families of
inequalities are:

| family | four-copy states | four-copy effects | in table calculus |
|---|---|---|---|
| (i) | products `X(01) ⊗ Y(23)` | products `E(02) ⊗ F(13)` | `⟨X, E·Y·Fᵀ⟩ ≥ 0` |
| (ii) | products `L(02) ⊗ L'(13)` | products `e(01) ⊗ f(23)`, read through the conditional | `L·f·L'ᵀ ∈ K_01` |

Here four-copy contraction is matrix multiplication of pair tables [X p1 A1-A3].

**The gate supplies the link states and effects.**
- Its maximally entangled link `Δ = cnot(prodState xplus z3)` is the coordinator's expected source of co-self-duality.
  It is used as a state in (ii) and as an effect in (i), and gives `K_01 = T(K_23*)`.
- Its non-maximally entangled links `cnot(prodState x y)` act as **local filters**. Their coefficient matrices are
  `diag(a)·Circ(b)`:
  - the four-copy conditional through them is `Ad(C ⊗ C')(T f)`;
  - this includes exact local rotations and local Lorentz boosts [X p1 C2, p3 G1-G4].

**Filters plus the gate's own effects place every pure state in each pair cone.**
- Every pure state with a generic coefficient matrix `D·Circ(b)·D'` lies in each pair cone [X p1 D1-D3].
- Closedness and convexity then give `Q3 ⊆ K`, and inclusion (II) gives `K ⊆ Q3`.

**Arbitrary token charts (no uniform composition).** The same argument runs in arbitrary token charts [X p2 U1-U2]:
- each Bell link induces a chart identification `R = A·reflY·Bᵀ ∈ O(3)`;
- each pair cone is classified separately as Q3 or the twin;
- twist bits become defined only after this classification;
- the instance holds exactly for the even 4-cycle twist patterns [X p2 Z1-Z3].

**Load-bearing premises (exact foils):**
- coherence: `C_H` (order-8 native group) and `K_F` (Clifford group) satisfy every other hypothesis and violate the
  instance at −1/200 [X p2 F1, p6 H1-H3];
- the gate: SEP and max satisfy the instance and fail the gate [X p2 F2];
- closedness and the full effect sets: [X+W p2 F3-F4].

**Three copies.** The six-copy instance lifts everything except the selection:
- `K₀₁₂ = T₃(K₃₄₅*)` and SLOCC invariance of the three-copy cone [X p5];
- the biseparable hull fails, at −1/16 [X p6 M1, matching EQ2-A D4].

What remains is a classification of SLOCC-invariant co-self-dual multi-qubit cones (§6). Under the derived SLOCC
symmetry, the one-orbit test does not exclude EQ2-A's c = 1 candidate `F + 1/10` or the c = 0 GHZ witness `1 − 2Γ`
[F x1]. This is consistency-axis work only, and the bands are unchanged.

### 1.1 Milestones (Amendment 1)

| milestone | status | evidence |
|---|---|---|
| 1 four-copy co-self-duality `K₂ = T(K₂*)` | **proved**: both inclusions separately (§1.2) | [X p1 A, B; p2 N, P] + [W] assembly |
| 2 cone uniqueness, minimal extra structure | **selected by the four-copy filter links + gate**; shadows: twin-type `K = K*` alone does NOT select (countermodel exists); cnot-type `K = T(K*)` alone, and with gate invariance: OPEN | [X p1 C-D, p3, p4] + [W] |
| 3 IE₁ derived | **proved** (theorem route) at KT(4; 01\|23, 02\|13) | §2 T3 |
| 4 IE₂, all twisted configurations | four-copy twists: exactly the coboundary patterns [X p2 Z]; three-copy minimal hulls `M_bs`, `M_tw`, `M_odd` excluded [X p6 M1; EQ2-A a4c]; **intermediate cones (`B_tw ⊊ K₃ ⊊ B_tw*`, and c = 0 analogues): OPEN** | §6 |
| 5 general composition | not taken up (conditional on 4) | — |

### 1.2 The two inclusions, audited separately (Amendment 2)

Coordinator's expectation, checked and confirmed exactly as stated.

| | (I) `T(K_23*) ⊆ K_01` | (II) `K_01 ⊆ T(K_23*)` |
|---|---|---|
| regrouping that contributes products of **states** | 02\|13: `Δ(02) ⊗ Δ(13)` (prod_mem) | 01\|23: `X(01) ⊗ Y(23)` (prod_mem) |
| regrouping that contributes products of **effects** | 01\|23: `e(01) ⊗ f(23)` (prodEff_effect) | 02\|13: `Δ(02) ⊗ Δ(13)` (prodEff_effect) |
| conditioning rule | conditional of the 02\|13 product given `f(23)` is a state of group 01: all `e ∈ K_01*` plus closedness (the analogue of `condA_mem` CI:431, which assumes `IsCompact`) | none |
| Bell link enters as | a **state** of the standalone link pairs: `Δ = cnot(prodState xplus z3)` [K CD:1222] | an **effect** of the link pairs: `Δ/4 = cnot(sharp xplus ⊗ sharp z3)` (§1.3) |
| identity | `Δ·f·Δ = T f` [X p1 B4] | `⟨X, Δ·Y·Δ⟩ = ⟨X, T Y⟩` [X p2 N2] |
| uniformity / identification used | none between 01 and 23; the link pairs carry their native gates | same |
| twisted orientation | twin link `R_B Δ = idW` induces no transpose: `K* ⊆ K` [X p1 E2, p2 P3-P4] | twin effect `idW/4` gives `K ⊆ K*` |

Each inclusion alone is a partial result; together `K_01 = T(K_23*)`, and with `K_01 = K_23` (equality in a shared
chart) `K = T(K*)`. Neither inclusion is used without the other in the selection argument: (I) plus the filter links
put pure states into `K`, and (II) bounds `K` by `Q3`.

### 1.3 Bell effects traced to premises (Amendment 2)

- (i) `sharp(xplus) ⊗ sharp(z3)` is an effect of the pair body.
  - By COMP-1 `prodEff_effect` [K CI:227] applied to two single-system effects.
  - Sharp effects are `IsEffectOn` [K KF:116] and are **available** under OG-1's named hypotheses
    (`sharpFamily_subset_avail`, EFF-1 Q-CONE; `maxConeOf_sharpFamily` EffectSpace:549).
- (ii) The dual action of the standalone pair gate maps effects to effects. **This is automatic in the base
  vocabulary**, because COMP-1's effects are `IsEffectOn` functionals: every affine map with values in [0,1] on the
  body.
  - `cnot` is a Euclidean-self-adjoint involution, it fixes the unit effect, and it preserves the body [X p2 P2].
  - So `e ∘ cnot` is again an effect, and `cnot(sharp ⊗ sharp) = Δ/4`.
  - The twisted orientation behaves the same way: `cnot'` is self-adjoint and fixes the unit, and `cnot'(sharp ⊗ sharp)
    = idW/4` [X p2 P3].
- It would be a separate availability assumption only if KT's group effect sets were read as AVAILABLE tests. EFF-1
  Q-SET shows that availability of non-sharp effects needs the named `MixingClosed` (`not_fullEffects_of_orbit`).

### 1.4 Charts, orientations, identifications (Amendment 2)

- **Pair cones:** the derivation never uses equality of pair cones in a shared chart, nor an abstract isomorphism.
  - Each token's ball chart is fixed arbitrarily, unique up to O(3).
  - Each pair gate is `ℓ₁ ∘ cnot ∘ ℓ₂` in those charts (N-CLASS, EQ2-B [X+W]).
- **Link identifications:** the Bell link of pair (i,j) defines the identification `R_ij = A·reflY·Bᵀ` from the
  post-local `ℓ₁ = (A, B)`.
  - `Φ⁺` induces the transpose (`R = reflY`), and `R_B Φ⁺` induces none.
  - A mixed pair of links induces one partial transpose [X p2 P4, U1].
- **Filter links:** they act on `K_01` as A-conjugated local filters [X p2 U2]; with the rotation links [X p3] they
  generate all local rotations and filters, whatever the charts.
- **Twist bits:** without local invariance they are undefined. They become defined after the classification, relative
  to the fixed charts, and the instance forces the 4-cycle parity [X p2 Z1].
- **If the charts are aligned with the gate frames** (each pair gate exactly `cnot` or `cnot'`), N-CLASS is not needed.
  The remaining freedom is per-token chart changes that keep the gate forms, which includes the per-token reflection
  that swaps Q3 and the twin on every pair at that token (D1).
- **The (03)(12) links** give the other 4-cycle's relation `K_01 = T(swap K_23*)` [X p2 P5].

### 1.5 Step tags (no circularity; Amendment 1)

N1 derivation (two copies), each step:

| step | content | tag |
|---|---|---|
| 1 | `Δ, L_a ∈ K_02, K_13`: gate applied to product states of the standalone link pairs | (2) |
| 2 | `Δ/4, cnot(product effects) ∈ K_*`: dual gate action on product effects of standalone pairs | (2) |
| 3 | `L(02) ⊗ L'(13)` and `X(01) ⊗ Y(23)` are four-copy states | (s) prod_mem |
| 4 | `e(01) ⊗ f(23)`, `E(02) ⊗ F(13)` are four-copy effects | (s) prodEff_effect |
| 5 | conditional of step 3 given `f(23)` is a state of group 01 | (s) conditioning + closedness |
| 6 | (I), (II), filter invariance, generic pure states in `K`, `Q3 ⊆ K ⊆ Q3` | (s) + exact identities + [W] density, spectral theorem |

No (o) step occurs: the gate never acts on part of a larger composite. The six-copy derivation has the same shape,
with the link pairs (03), (14), (25), all steps (s) or (2) [X p5].

### 1.6 Independent content of composition coherence (Amendment 1)

Composition coherence is not treated as adopted. At the stated instances:
- **QM satisfies it.** `K₄ = PSD₁₆` [X p1 F1]; the twisted patterns are realized by `PT_S(PSD₁₆)` [X p2 Z3].
- **The transported landed two-copy premises do not imply it.** `C_H` and `K_F` are admissible, closed and
  gate-invariant, and violate it [X p6 H3, p2 F1]. The minimal three-copy hulls also violate the six-copy instance.
- **What it implies** (with gate, admissibility, closedness and full effect sets):
  - co-self-duality, both inclusions;
  - local filter invariance;
  - pair cone ∈ {Q3, Tw};
  - IE₁;
  - even 4-cycles;
  - at six copies: co-self-duality and SLOCC invariance of `K₃`.
- **What it does not imply:**
  - entanglement without the gate (SEP, max);
  - a unique cone without closedness or with restricted effects;
  - by any test here, `K₃ = PSD₈` or IE₂.

## 2. Target theorems (Lean-level, UNBUILT)

Native table vocabulary over `W 3`. Every statement is a design candidate; none was compiled.

| id | statement (abbreviated) | layer | direction |
|---|---|---|---|
| **T1** `fourCopy_familyI`, `fourCopy_familyII` | for a four-copy body `K4` that is a COMP-1 composite of 01\|23 and of 02\|13, with closed group bodies and `IsEffectOn` effects: (i) `∀ X ∈ K01, Y ∈ K23, E ∈ K02*, F ∈ K13*, 0 ≤ ⟪X, E * Y * Fᵀ⟫`; (ii) `∀ L ∈ K02, L' ∈ K13, f ∈ K23*, L * f * L'ᵀ ∈ K01` (matrix product of tables) | (II-2) via KT | forward |
| **T2a/b** `incl_I`, `incl_II` | `Δ ∈ K02 → Δ ∈ K13 → transposeW '' K23* ⊆ K01` and `Δ ∈ K02* → Δ ∈ K13* → K01 ⊆ transposeW '' K23*`; with `cnot '' Kij ⊆ Kij` the hypotheses hold (`cnot_prodState_xplus_z3` CD:1222, dual action) | (II-2) | forward |
| **T2c** `link_filter` | `cnot (prodState x y) * f * (cnot (prodState x' y'))ᵀ = 4 • coordsW (Ad (C ⊗ C') (pauliW (transposeW f)))`, `C = coefMat x y` | (I) identity | — |
| **T3** `pairCone_of_kt4` | admissible closed convex `K01 … K13`, each invariant under its native gate (`ℓ₁ ∘ cnot ∘ ℓ₂`), plus T1 ⇒ `K01 = Q3 ∨ K01 = twin` (in the given charts); corollary `ie1_of_kt4 : ∀ R ∈ SO(3), actC R '' K01 = K01 ∧ actT R '' K01 = K01` | (II-2) | forward |
| **T3'** aligned form | gates exactly `cnot` (resp. `cnot'`) ⇒ `K01 = Q3` (resp. `twin`), no N-CLASS | (II-2) | forward |
| **T4** `kt4_twist_parity` | with gates `cnot^(τ)`: T1 consistent ⟺ `τ01 + τ13 + τ23 + τ02` even; every even pattern realized by `PT_S(PSD₁₆)` | (II-3) boundary | both, each witnessed |
| **T5** `sixCopy_coSelfDual`, `sixCopy_slocc` | KT(6) ⇒ `K012 = transpose3 '' K345*` and `Ad(C₀ ⊗ C₁ ⊗ C₂) '' K012 ⊆ K012` for all `C_k : GL(2, ℂ)` | (II-3) | forward |
| **T6** `ghz_dichotomy` | closed SLOCC-invariant `K₃` with T5: `K₃ = PSD₈ ↔ ∃ ψ, hyperdet ψ ≠ 0 ∧ ψψ† ∈ K₃` | (II-3) | both (← needs DVC [L]) |
| **T7** foils | `C_H` and `K_F`: admissible, closed, cnot-invariant, `¬ KT4`; SEP and max: `KT4 ∧ ¬ cnot-invariant`; `int Q3 ∪ conv(SEP ∪ cnot SEP)`: `KT4 ∧ ¬ closed ∧ ≠ Q3` | (II-2) | no-go for the stated class |

## 3. Hypotheses ledger

"QM?" asks whether finite-dimensional complex QM satisfies the hypothesis. Independence evidence is a model that
satisfies the other hypotheses and fails this one.

| hypothesis | status | QM? | independence / necessity evidence |
|---|---|---|---|
| LT (tensor carriers; tables) | [K] `Composite.lt` CI:243 at two copies; n-copy transport unsourced | yes | real QM fails LT (EQ-E) |
| admissibility of each pair body (`CandidateCone`) | COMP-1 transport (prod_mem, prodEff_effect, `subset_maxBody` CI:467) | yes | EQ2-B foils (K_nc, B3) |
| **native gate as an operation of the standalone pair** (IsNot, CtrlGate, cone invariance = `JointReversible` CI:445) | transported two-copy premise; a (2)-type premise, not IE | yes | **SEP, max** satisfy KT4 and admissibility and fail it [X p2 F2] |
| **closedness of pair bodies** | unsourced; the kernel's `condA_mem` (CI:431) assumes `IsCompact` | yes | **`int Q3 ∪ conv(SEP ∪ cnot SEP)`** satisfies everything else, ≠ Q3 [X+W p2 F4]; without it: `int Q3 ⊆ K ⊆ Q3` |
| **full effect sets** (`IsEffectOn`, KF:116; COMP-1 quantifier) | built into COMP-1 | yes | `K_F` with effects restricted to Q3 satisfies the restricted instance [X+W p2 F3] |
| **KT(4; 01\|23, 02\|13)** (one body, two groupings) | unsourced; proposed, not adopted | yes [X p1 F1] | **`C_H`, `K_F`** satisfy every row above and violate it (−1/200) [X p6, p2]; each grouping alone is satisfiable by any admissible cone (min tensor product) [W] |
| uniform composition (equal pair cones in a shared chart) | **not used** | — | — |
| exchange symmetry | not used | — | — |
| N-CLASS (each gate `ℓ₁ ∘ cnot ∘ ℓ₂`) | EQ2-B [X+W]; only for the general-chart T3 | yes | — |
| KT(6) (012\|345, 03\|1425, 14\|25) | unsourced | yes | excludes BS (−1/16) [X p6 M1], B_tw (EQ2-A a4c); implication to IE₂ OPEN |
| shadow (S-tw) admissible + `K = K*` | — | yes | **does not select**: Zorn existence with `y = diag(1,1,0,1) ∈ max \ (Q3 ∪ Tw)` [X p4 L1 + W] |
| shadow (S-cn) admissible + `K = T(K*)` | — | yes | OPEN; sector room [X p4 L2]; no T-isometric spin-factor image [X p4 L3] |

## 4. Missing lemmas

**Kernel vocabulary absent at `bcbc516f`** (as recorded by EQ2-A at the same base):
- there is no carrier with three or more copies;
- COMP-1 is two-factor (CI:210-246);
- there is no statement of composition coherence;
- there is no pair-table matrix calculus, no `transposeW`, and no `pauliW`.

The n-token native vocabulary is EQ2-A's TA2 design (`NC S`, `margN`, `pauliN`).

**New lemmas, each with its exact certificate here:**
- **Table calculus** (T1): the four-copy sums equal matrix products [X p1 A1-A2]; the six-copy version is factorwise
  [X p5 S1-S2].
- **Link identities**:
  - `Δ·f·Δ = T f`, `idW·f·idW = f`, mixed links giving a partial transpose [X p1 B4, p2 P4];
  - the filter formula with non-symmetric coefficient `diag(1,u)·Circ(1,v)` [X p3 G1];
  - the conjugated-filter formula in general charts [X p2 U2].
- **Pure-state supply:**
  - the factorization `D·Circ(w,1)·D'` [X p1 D1];
  - `L_a·(T g)·L_a'ᵀ = 4·coordsW(|χ⟩⟨χ|)` [X p1 D3];
  - density of generic coefficient matrices and closedness [W];
  - PSD as the closed convex hull of pure states (spectral theorem; Mathlib `Matrix.IsHermitian.spectral_theorem`
    per EQ2-A's record of the local v4.33.0 snapshot — **not re-checked here**).
- **Square root:** a complex square root for `w² = ps/(qr)` (`IsAlgClosed.exists_pow_nat_eq`, per EQ2-A's record —
  **not re-checked here**).
- **Euler decomposition** from the X- and Z-rotation links [X p3 G3-G4 ingredients + W].
- **Foils:** `C_H`'s orbit bound (8 elements) [X p6]; the Schmidt bound `max_{product} |⟨ab|φ⟩|² = λ_max(ρ_A)` [W,
  standard].
- **GHZ dichotomy:** hyperdeterminant values and SLOCC covariance [X p5 S7]; GHZ orbit density, Dür–Vidal–Cirac [L].

## 5. Formalization strategy (proposed rounds; nothing frozen)

| round | content | cost | controls / countercontrols |
|---|---|---|---|
| R1 `FourCopyTables` | T1 as `Finset` sum identities; `Δ·f·Δ = transposeW f`; T2a/b from T1 + `cnot_prodState_xplus_z3` (CD:1222) + self-adjointness of `cnot` | cheap (`fin_cases`, `simp`) | control: QM values ≥ 0; countercontrol: odd twist pattern gives −2 (T4) |
| R2 `LinkFilters` | T2c over the Pauli dictionary (needs EQ2-A R1 `pauliW`); twin and mixed links | moderate | countercontrols: dropping the transpose; using `Cᵀ` (p1 C3, p3 G2) |
| R3 `PairConeSelection` | T3' (aligned): generic factorization, density, closedness, spectral theorem; then T3 with N-CLASS (EQ2-B R2) | moderate–heavy | foils: SEP, max (gate), `int Q3 ∪ K_lo` (closedness), `K_F` with effects Q3 (no-restriction) |
| R4 `CoherenceFoils` | `C_H` (order 8, explicit rational witness `w`, value −1/200) — cheaper than `K_F` (11520) | cheap–moderate (the Schmidt bound for 8 explicit pure states) | control: a product's orbit reaches marginal norm 1 |
| R5 `TwistParity` | T4 (sign-map algebra) + realization by `PT_S` | cheap | the 16 assignments |
| R6 `SixCopyLinks` | T5 identities (three-copy tables) | moderate | BS violation −1/16 (p6 M1) |
| R7 (only if the wall closes) | T6 + the three-copy classification | open | — |

Order: R1 → R2 → R5 → R4 → R3 (closes IE₁ at the instance) → R6. R7 waits on §6's wall.

## 6. Research questions

| question | classification | evidence / wall |
|---|---|---|
| **N1** Does KT at four copies, with admissibility and the native gate but no local invariance, force Q3 or the twin, i.e. imply IE₁? | **THEOREM ROUTE** at KT(4; 01\|23, 02\|13) | §1, §2 T3; [X p1, p2, p3] + [W] density/spectral; no uniformity; exact foils for every load-bearing premise |
| milestone 1: `K₂ = T(K₂*)` | **THEOREM ROUTE**, both inclusions separately | §1.2; [X p1 B, p2 N, P] |
| milestone 2: what selects the cone | selected by the four-copy filter links + gate (THEOREM ROUTE); (S-tw) alone: **COUNTEREXAMPLE** (existence, Zorn) [X p4 L1 + W]; (S-cn) alone and with gate: **OPEN** | p4 L2-L4 |
| milestone 3: IE₁ derived | **THEOREM ROUTE** | T3 corollary |
| four-copy twisted configurations | **THEOREM ROUTE**: exactly the coboundary (even) patterns | [X p2 Z1-Z3] |
| **N2** c = 1: LU- (now SLOCC-) invariant `K₃ = K₃*` strictly between `B_tw` and `B_tw*`? | **OPEN** | refined wall: SLOCC invariance is derived [X p5]; `K₃` must avoid every `PT_S`(GHZ-class) state [W T6]; EQ2-A's candidate `F + 1/10` has SLOCC-orbit self-pairing minimum `t²` [F x1] (no exclusion lead) |
| **N2** c = 0: is `PSD₈` the only co-self-dual SLOCC-invariant cone between BS and BS*? | **OPEN** | equivalent to "must it contain a GHZ-class state" [W T6]; no-generation lemma [W]; the GHZ witness `1 − 2Γ` has orbit self-pairing minimum ≈ 0 [F x1]; sector test of `conv(BS ∪ SLOCC·W₂)` inconclusive by design [F x2] |
| three-copy minimal hulls `M_bs`, `M_odd`, `M_tw` | **COUNTEREXAMPLE to their KT∞-consistency** (excluded) | BS: −1/16 [X p6 M1]; `B_tw` not self-dual (EQ2-A a4c, coordinator 13/13); `M_odd` reduces to `M_tw` by the chart |
| N3 purification | not entered (N2 gave no KT∞ countermodel) | — |
| N4 literature | conjugate/steering/self-duality mechanisms known [L]; no source seen that derives parallel composition of operations from kinematic composites [L, summaries] | NOTES N4 |

§A.31 classification of this thread:
- **NEW:**
  - the four-copy filter links, so that co-self-duality is not the whole content of the instance;
  - the instance alone (no uniformity, arbitrary charts) classifies each pair cone, and IE₁ is derived;
  - the six-copy instance gives SLOCC invariance and co-self-duality of `K₃`;
  - the no-generation lemma;
  - the cheaper foil `C_H`;
  - the exposed hidden assumptions: closedness, the full effect sets, the gate as the source of links, and the
    coherence of one body under two groupings.
- **ELABORATING:** the shadows (S-tw)/(S-cn); the GHZ dichotomy.
- **POSITIVE:** the coordinator's expectation (I)/(II) is confirmed exactly.
- **Fixed point:** not reached. The last two passes (x1, x2) produced no NEW finding; the protocol's 3-4 were not
  completed.
- Consistency axis only; bands unchanged.

**Assumption-watch markers.**
1. A "co-self-duality" statement extracted from a coherence instance can discard its content. The four-copy instance
   also carries filter links, so check every link family before reducing to a shadow.
2. Gate links of low Schmidt rank are SWAP-symmetric (`diag(a)·Circ(b)` is symmetric when `a0 = a1` or `b1 = 0`), and
   two countercontrols here were vacuous for that reason (p1 runs 1-2). Test orientation with a product link.
3. KT generation from pair-level data never produces GHZ-class states. Any claim that KT implies IE₂ must go through
   the fixed point, not through generation.
4. A sampled hull's dual always has extreme points outside it (x2). Sampled self-duality tests are inconclusive by
   design.

## 7. Evidence and probe log

Run as `python3 -I -B <script> [args]` from `scratchpad/eq3/P/`. The `.lean` arguments are the base's
`CompositeDimension.lean` and `K2Guard.lean`.
- Hashes are the first 16 hex digits of sha256.
- Every exact probe prints its decision rule in its header and a VERDICT line only over green controls.
- Every probe `.err` holds only the harness's appended `exit=N` line; script stderr was empty.
- All exact probes import `eq3_lib.py` (`9fc4c89bf12310af`). It is own code and imports nothing from `eq2/` or
  `eqreview/`.

| script | sha | output | sha | checks | verdict | run history |
|---|---|---|---|---|---|---|
| `p1_four_copy_links.py` (CD, K2G) | `70d6176dd9cbd4fe` | `.out` | `bfdcd0e7010815e4` | 32/32 | `P1-FOUR-COPY-LINKS-EXACT` | run 1 29/30 and run 2 30/31, both NOT RENDERED: a vacuous orientation countercontrol (SWAP-symmetric links), kept as `.run1.*` (`73248aebe12a72bd` / `a1207f7a86d2d269`) and `.run2.*` (`485c509f461b9b5c` / `1b98c8d3abe48c12`); run 3 |
| `p2_audit_twists_foils.py` (CD, K2G) | `b8cff894baa4902b` | `.out` | `401efe5ca778a00a` | 23/23 | `P2-AUDIT-TWISTS-FOILS-EXACT` | run 1 (two pre-run edits) |
| `p3_general_links.py` (CD) | `78b1d99537b2bbe4` | `.out` | `9c82d156b5cf0754` | 5/5 | `P3-GENERAL-LINKS-EXACT` | run 1 |
| `p4_cone_ladder.py` | `e6bfa5cd8abc5167` | `.out` | `8a0ac009bee1bd28` | 9/9 | `P4-LADDER-INGREDIENTS-EXACT` | run 1 (pre-run edits: no solver, one note) |
| `p5_six_copy.py` (CD) | `32f9ea39f47a4960` | `.out` | `df2f92aed390ac61` | 9/9 | `P5-SIX-COPY-EXACT` | run 1 |
| `p6_cheap_foils.py` (CD) | `0a162d371f34d6f3` | `.out` | `d6263e18beb054f6` | 4/4 | `P6-CHEAP-FOILS-EXACT` | run 1 |

**Replay.**
- `run_all.py` (`c4c0fbaf9248b817`) re-runs p1-p6 into `replay/` and compares byte for byte. Result `run_all.out`
  (`8a386d47dd1ddbf2`): all six exit 0, stderr empty, identical, `run_all: OK`.
- The earlier five-probe replay (before p6 existed) is kept as `run_all.prelim.out` (`dcc33ce3710722bb`, `run_all:
  OK`).
- Every `python3 -I` run has a fresh hash seed, so identical replays also test determinism.

**Floating-point explorations** (they certify nothing; replayed for determinism by `run_explorations.py`
`bea1dc9d23bb11f1`, output `3ea7f85fc33e7099`, both identical, `run_explorations: OK`):

| script | sha | output | sha | outcome |
|---|---|---|---|---|
| `x1_slocc_orbit_float.py` | `366e2bc106c5ed01` | `.out` | `ec61ade6b2aa4905` | SLOCC-orbit self-pairing minima: `t²` for `F + t·1`, `(1 − c/2)²` for `1 − cΓ`; no negative found (no lead) |
| `x2_sector_float.py` | `a24ed1e57a8a0c0c` | `.out` | `f9add1cd09540a84` | sector test inconclusive by design (sampled hull) |

**Harness errors and defects** (each recorded in NOTES):
- the p1 run-1 and run-2 vacuous countercontrols;
- the pre-run edits to p2 and p4;
- a shell `tail -3` usage error in a hash listing (no file affected);
- a design flaw in x2, recorded as "inconclusive by design".

Egress: arXiv, ar5iv, alphaxiv and quantum-journal were blocked by the session's egress policy. That was not routed
around, so all literature is [L] unverified.

**Integrity.** The final check is appended to `NOTES.md` (N9): base manifest, repository status, and writes confined
to `scratchpad/eq3/P/`.
