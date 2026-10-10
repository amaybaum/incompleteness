# Thread S2 — PAIR-CONS: a pair system built from data — RESULT

Research only. Base: certified `main` at L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`, read-only).
Governing texts: `PROTOCOL.md` (`239dc123…`), amendment 1 (`b41aa0e7…`), amendment 2 (`2a2f78f3…`),
`PROTOCOL-STAGE2.md` (`38603692…`), which governs where they differ. Nothing here is adopted, frozen or governed. No git
write, PR, CI, publication or agent was used. There is no Lean toolchain: every Lean text below is UNBUILT.

Evidence levels, kept apart in every statement:
- kernel: **[K]** certified at L (`file:line` in `pt/base/verification/lean-mathlib/OIBridge/`), **[D]** kernel-checked in
  the design run `ff9c3a35` (`pt/inputs/fourcopy/`), not certified;
- **[W]** written argument (given here);
- **[X]** exact computation in `pt/S2/`, replayed byte for byte, stated for the instance it checks (check ids in brackets,
  e.g. [X R5] = check R5 of `s2_1_native.py`);
- **[L, unverified]** literature or standard results not read at the source;
- **UNBUILT** Lean.

File abbreviations: CD `CompositeDimension.lean`, CI `CompositeInterface.lean`, SC `StageCompletion.lean`, CA
`CompletionAction.lean`, KIF `KInfFoundations.lean`, K2G `K2Guard.lean`, RSB `RelcSelectBlock.lean`, PN `ParityNot.lean`,
OG `OrbitGeneration.lean`, TB `TransitiveBody.lean`, ON `OrbitNormalization.lean`, ES `EffectSpace.lean`; design: FDefs,
FCore, FIE1, FHead, FBridge, FBip, FLocal (`FourCopy*.lean`). Scripts: `s2_1_native` … `s2_7_supp` (§6).

**Notation.** `SEP` is the convex cone of the product states `prodState x y`, x, y in the ball. `K_gen = SEP + cnot SEP`.
`σ = actT reflY` (the one-copy transpose on token 2, [X R1]). `Q3` is the Pauli-coordinate PSD cone, used only as a
property of models, never as a premise; `twin = σ Q3`. `K_E = dualW K_gen`. `T_ψ = actT R_H phiW` (landed M_cl.6).
`ψ_w = (3|00⟩ + 4|01⟩ + 5|11⟩)/√50`, written in the computational basis of the certified frame (z3 ↦ |0⟩); its table is
rational. `F = E00/2 − T_ψ/4` (Thread A's dual witness). `E_gen` is the cone of tables of the generated tests.
- **Product action:** a pair-system gate N has the certified product action if the product-test table of N applied to a
  product preparation is `cnot` of its table, `π(N p) = cnot(π p)`. This is the certified datum read on product inputs.
- **INV2:** the native gate is an operational involution on the pair system, `N ∘ N = id`.
- **PTQ:** K2-LEDGER's product-test-quotient condition: the gate descends to product-test tables.
- **Classes of constructions.**
  - `𝒞_nat`: consistent sets of gates satisfying the landed `NativeGate (eball 3) z3 nflip`.
  - `𝒞_mono`: operations that are Q3-automorphisms monomial in the frame's computational basis. This covers every
    Q3-preserving gate meeting the frame clause, token exchange, diagonal phases, local Paulis and z-rotations. It also
    contains the global transpose, and the σ-conjugates of all of these for the twin class.
  - `𝒞_fin`: finite groups of Q3-automorphisms.

## 0. Answer

| target | label | principle | renames the target? | strength vs target | vs certified L |
|---|---|---|---|---|---|
| **FR**: finite rank of a pair completion generated from the data | **CONDITIONAL** | INV2, or more generally a finite operation group, with COMP-1 bi-affine products | no | strictly stronger: the register model has finite rank and N⁴ = id, N² ≠ id | independent: the clock model; Thread A's `D_cl` |
| **LT**: local tomography of that completion | **CONDITIONAL** | INV2, together with the certified product action and generation (preparations and tests) | no: INV2 is an identity of one operation, LT a separation property of all states | equivalent at the completion level, relative to generation and the product action (both directions proved); strictly stronger at the carrier level (order-3 model) | independent: the register model; landed `paddedBall3` |
| **GC**: native-gate compatibility (body closed under the gate, tables valid, hgate ∧ hinv for the generated cone) | **DERIVED** for the constructed system (table rule); CONDITIONAL on INV2 on an abstract carrier | generativity, with [K] `cnot_prodState_mem_maxCone` and `cnotFun_cnotFun` | n/a: the cone is generated, not given | — | — |
| **SS**: the required state space (H/FCC, IE1; Q3 at the instance) from data, without operation-level idle extension | **INDEPENDENT** of L as stated (the cnot-generated system K_gen), with an impossibility proof for the classes `𝒞_nat`, `𝒞_mono`, `𝒞_fin` | none found; only the flagged routes reach it | — | — | a non-flagged source in general: UNRESOLVED |
| **FC**: frame covariance of the native gate | flagged route, classified: **FC ⟺ IE1 given hgate**, both directions proved | — | it is IE1 restated, given hgate | equivalent | — |
| **EFF**: the effect set the premises consume | established | — | — | — | — |

The EFF row in full:
- hadm (b) reads product effects only.
- (BD) reads one generated effect per pair.
- FCC is read at generated effects, except in the free effect slots of `cross_rel`'s second half and the four
  invariance lemmas. There it reads the full duals: no-restriction.

**Sufficiency proved** (as opposed to surviving the countermodels):
- **INV2 ⇒ LT** for a pair system that realizes the certified product action, with preparations and tests generated from
  products by the gate. Evidence: [W] with symbolic and exact identities [X L1–L3]. The read-out cone is then K_gen.
- **INV2 or a finite operation group ⇒ finite rank** [W; instances X K3].
- **Generativity ⇒ hgate ∧ hinv** for the generated cone [X T4–T6, W].
- **Consistent fixed-frame native constructions have cone exactly K_gen (even class) or σK_gen (odd class).** Exact over
  the 32 gates and the 1024 ordered pairs [X R2–R6], with [W] for the cone equality. Completeness of the family beyond
  signed-diagonal dressings rests on Thread D's D1.4 [W + X, audited].
- **No construction in `𝒞_mono` or `𝒞_fin` generates Q3 or an IE1 cone.** Exact witnesses [X Q1–Q2, U1]; the Milman and
  dimension steps are [W + L].
- **FC ⟺ IE1 given hgate.** Exact symbolic word identities [X Q5] and [W].
- **The theorem consumes no-restriction**, by an exact source scan [X F6] over [D]. Uniform K_gen satisfies FCC on every
  checked generated instance [X F5]; the written step holds for all of them because all generated objects lie in Q3. Its
  consumed failing instance uses non-generated effects [X F4].

**Survives the countermodels only:** nothing is asserted on that basis.

**Route refuted.** In each of the following a model satisfies the candidate and violates the target:
- "test generation ⇒ LT": the register model;
- "a reversible gate with the certified product action, test generation and valid tables ⇒ finite rank": the clock model;
- "compactness ⇒ finite rank": the compact padded model;
- "FCC with generated effects, plus the per-pair premises ⇒ the theorem's conclusion": K_gen;
- every construction class above, for Q3 and for IE1.

**The owner's central question, as far as S2 reaches.** Two independently observable systems, combined by the
observer-native data alone (products, product tests, the native gate as an involution, mixtures and completion), form a
consistent composite with finite rank, local tomography and gate compatibility. That composite is K_gen. Its generated
states and tests already obey the quantum consistency rules: four-copy coherence holds on every generated instance
checked, and in writing on all of them, since every generated object lies in Q3. It is a sub-theory of two-qubit quantum
theory.

What the data do not supply is the rest of the quantum state space. Consider every construction examined that contains
the native gate and lets no frame-moving single-system operation act on entangled pair states. Each one either stays
strictly inside Q3 and fails IE1, or overshoots Q3 (the dual completion K_E) and fails IE1 and four-copy coherence.
Four-copy coherence excludes K_gen only through effects the data do not generate.

On the routes examined, the full quantum rules are therefore reached only after adding one of two principles. Each
suffices at the instance (uniform cones, cnot gates, identity locals):
- local agency: each token's operations act on it inside any pair state. Given the gate this is equivalent to frame
  covariance. With cnot it gives Q3 [W + L].
- four-copy coherence in the theorem's form, whose effects range over the full duals (no-restriction). With the
  per-pair premises it gives Q3, through the design theorem [D] and the written classification [W + L].

L supplies neither. That the examined classes cannot do without one of them is proved only for those classes.

## 1. Routes and countermodels, node by node

### S2.1 — Data and construction (Verdict: CONFIRMING; the construction is defined and exact at finite stages)

**Data** (the owner's list; anchors at L):
- **D1. Single system.** The ball `eball 3 = ball3` [K TB:671] and its effects `IsEffectOn` [K KIF:116] (affine,
  [0, 1]-valued). Its reversible operations are `fullAut3`, all affine automorphisms of the ball [K OG:521]: rotations
  `rot3`, `rotX` [K KIF:411, ON:581] and reflections `refls3` [K TB:700], acting transitively [K TB:694].
  - **Upstream dependency.** The ball is taken as given. The OI-native substratum towers tested so far (RANK, QUOTIENT,
    RECORD; `pt/inputs2/oi-substratum/`) do not produce a qubit-sized single system: the rank or effect dimension is
    over or under the target, ALL FAIL. A pair built from substratum data inherits that open problem (K∞-Stage).
- **D2. The native pair operation `cnot : W 3 ≃ₗ W 3`** [K CD:775]. Its properties: `nativeGate_cnot` [K CD:1160],
  `cnotFun_cnotFun` (an involution) [K CD:770], `cnot_prodState_mem_maxCone` [K CD:1152]. Its type `W 3 ≃ W 3` is a map
  of product-test tables; `W` carries the docstring "Local tomography is the premise this carrier encodes" [K CD:95–96].
- **D3. Product preparations** `x ⊗ y` with table `prodState x y` [K CD:161]. These are COMP-1 `ProductData`, bi-affine
  [K CI:210].
- **D4. Product tests** `e ⊗ f` with value `prodEffVal e f` [K CD:182].
- **D5. Tests generated by operations:** "apply w, then test e ⊗ f".

**Construction `P(𝒪)`** (a `DirectedStages` [K SC:63]; `s2_5_tower`):
- index ℕ;
- stage n: preparations `w·(x ⊗ y)` for x, y in a finite nested rational set Q_n and w a word in 𝒪;
- labels `(w′, e, f)`;
- the table (rule below);
- stage maps are inclusions.

The completion is `body` = the closed convex hull of `prepVec` [K SC:141, SC:135] in ℓ^∞. The read-out through 16 product
labels goes to `W 3`. **The generated cone `K(𝒪)` is the cone over the read-out**: defined, not chosen.

**Every choice the construction makes:**

| # | choice | made here |
|---|---|---|
| C1 | single-system states and effects | the certified ball and effects; dense rational subsets at finite stages |
| C2 | single-system reversible operations | `fullAut3` acts on single systems, hence on pairs only through product preparations (x ↦ gx) and product tests (e ↦ e∘g). This product-level action is an identity of product data (Thread B, B3). These maps are **not** pair operations, so operation-level idle extension is excluded |
| C3 | independent preparation | products are preparations with multiplicative tables (D3) |
| C4 | the pair operation set 𝒪 | {cnot}. Variants: other fixed-frame native gates, `CtrlGate` gates, token exchange. Flagged: local operations on all states, frame conjugates |
| C5 | the operation rule | (R-tab) operations act on tables by their `W 3` matrices, the certified datum's type; or (R-abs) operations act on an abstract carrier and the datum fixes only the product action |
| C6 | generation | preparations are 𝒪-words on products; no ungenerated preparation |
| C7 | test generation | labels are product tests after 𝒪-words |
| C8 | mixtures and completion | convex hull; closure in ℓ^∞ |
| C9 | stages | nested finite sets, inclusion maps (SC∞ by construction) |
| C10 | consistency | every table value in [0, 1]: a check that restricts C4 |
| C11 | the cone | the cone over the completed read-out (a definition) |

**Instance results** for 𝒪 = {cnot} under R-tab [X `s2_5_tower`, 17/17]:
- valid on stages 1–3 [T1], with SC∞ by inclusion [T2];
- every label value is `ipW(w′ᵀ(ehom e ⊗ ehom f), table)` [T3]: **LT is built in by the table rule**, named;
- read-out rank 16 [T3];
- the gate is generative: `prepVec(cnot s)` is the label-shifted `prepVec(s)` [T4]; the datum respects every affine
  relation [T5], so it is an `OpDatum` [K CA:46] with `AffineRespect` [K CA:58], its own inverse;
- the read-out set is cnot-closed [T6];
- countercontrol: closing under `g_D = actT reflY ∘ cnot` is invalid [T7].

With dense points the read-out is the normalized slice of K_gen (Thread A, W-A1 [W, audited]).

### S2.2 — Finite rank (Verdict: NEW countermodels; sufficiency proved for INV2 / finite groups)

| candidate | result | evidence |
|---|---|---|
| LT with finite single-system ranks | sufficient: under LT the body maps injectively and affinely into the 15-dimensional slice, so rank ≤ 15. LT itself is the next target | [W]; instance rank 16 (linear) [X K3] |
| finitely many independent tests | FiniteRank restated: rank of the protocol matrix = affine rank + 1 (inputs2 RANK, R0) | [W, inputs2] |
| compactness of the completed body | **refuted** as a source of finite rank. Compact padded model: rank = 16 + L at each L tested; sup-distance 2^−(J+1) → 0, so a compact closure (Mazur [L, unverified]) of infinite rank. Compactness **suffices for closedness** of the read-out cone (Thread A, W-A3.1 steps 3–4 use only compactness) | [X K2] + [W] |
| **INV2, or any finite operation group G, with bi-affine products** | **sufficient**: products span ≤ 16 dimensions (bi-affinity), the G-orbit spans ≤ 16·|G|, labels are affine, so rank ≤ 16·|G| − 1. INV2 gives `|⟨N⟩| = 2` | [W]; register model (`|⟨N⟩| = 4`) rank 22 [X K3] |
| a reversible gate with the certified product action, valid tables and test generation | **refuted** by the **clock model** (described below) | [X K1] + [W] |

The clock model:
- **Definition.** `N(ω ⊗ δ_k) = c_k(ω) ⊗ δ_{k+1}`, with `c_k = cnot` iff k is a square.
- **Rank.** Protocol sections have rank L at L = 8, 16, 32, 48, 64 [X K1]. The parity σ(j) has run lengths 1, 3, 5, …
  [X K1]. If the Hankel rank were finite, a linear recurrence would make σ a function of a finite window, hence
  eventually periodic by pigeonhole [W]. So the rank is infinite.
- **Other properties.** The model is not LT either [X K1]. Countercontrol: a periodic clock has bounded rank 4.

**Verdict.** Finite rank is not given by finite single-system ranks plus products plus a reversible native gate. It is
given by the gate's finite order (INV2), or by LT.

### S2.3 — Local tomography (Verdict: NEW — a non-restating source, with exact countermodels for each ingredient)

1. **R-tab builds LT in** [X T3]. This is the place where the certified datum's typing `W 3 ≃ W 3` enters (K2-LEDGER D3:
   DIM-1 consumes PTQ).
2. **LT ⟺ PTQ for test-generated towers** [W, each direction separately].
   - (⇒) Under LT, body points are their product tables. Each generator acts on the body (labels are closed under
     preceding generators), hence on tables.
   - (⇐) By induction on words, the product table of `w·b` is a function of that of b, so every label value is.
   - This sharpens K2-LEDGER D3/D6. The padded "PTQ but not LT" control is invisible to a test-generated completion,
     since no label reads its padding.
3. **Block lemma** (carrier `V = W 3 ⊕ H`, `π` the projection, `N = [[A, B], [C, D]]` linear with the product action):
   - products span `W 3` [X L1], so A = cnot [W];
   - on `S = span(products ∪ N·products)`, `π N s = cnot π s` ⟺ `B C = 0`: the defect is exactly `B C u` (symbolic, generic
     B, C, D, u) [X L2(i)];
   - the `W 3`-block of `N∘N` is `I + B C` [X L2(ii)];
   - countercontrol: the defect is nonzero at `pxz` when `B C ≠ 0` [X L2].
4. **Theorem (INV2 ⇒ LT)** [W + X]. INV2 gives `B C = 0`; the N-orbit of the products is products ∪ N·products; PTQ holds
   on the generated span; by item 2 the completion is LT, and its read-out cone is K_gen.
   - Positive control: an involutive gate whose hidden register is excited (`C pxz ≠ 0`) still yields LT through tables
     [X L3].
   - Countercontrol: the hidden part is not a function of the table on the span [X L3].
5. **Each ingredient is load-bearing** (exact countermodels):
   - **Register model** (`N = [[cnot, I − cnot], [cnot, −cnot]]`, N² = cnot ⊕ cnot, N⁴ = I) [X L4].
     - It satisfies the product action, validity, unit, closure under N and N⁻¹ = N³, COMP-1 pre-composite data and
       finite rank.
     - It is **not LT**: `s = N(pxz,0)` and `s′ = N²(pxz,0)` have equal tables (phiW), while `π(N s) = phiW ≠ pxz =
       π(N s′)`.
     - Thus "every test is a product test preceded by available operations" does not give LT (route refuted).
   - **Rebit control** (d = 2, real QT) [X L6]. `Ad(CNOT)` is an involution of the 10-dimensional real symmetric span,
     but its product action C on the 9-dimensional table space kills X⊗Z, so C∘C ≠ I. `(I + Y⊗Y)/4` (a CNOT image of a
     mixture of products) and `I/4` have equal tables and different CNOT-test tables. So INV2 alone does not suffice;
     the certified involutive table datum is needed.
   - **Hidden-parameter model** (`N = [[cnot, Δ], [0, 1]]`, `cnot Δ = −Δ`, plus the ungenerated preparations
     `(E00, ±1/4)`) [X T8]. INV2 and the product action hold, the values are valid, and LT fails. So generation is
     load-bearing.
6. **Strength** [W].
   - Completion level: INV2 ⟺ LT, relative to generation and the product action. (⇐) is item 4. (⇒): under LT, N acts
     on the read-out by an affine map equal to cnot on the product slice, which affinely spans the slice. So N² acts as
     cnot² = id, and LT gives N² = id on the body.
   - Carrier level: INV2 is strictly stronger. Order-3 model: B = 0, LT holds, N² ≠ I [X L5].
7. **Renaming test and independence.**
   - INV2's content: one operation composed with itself is the identity.
   - LT's content: product tests separate all states.
   - These are different statements, equivalent only relative to the construction: not a renaming.
   - Independent motivation:
     - the certified table datum is an involution [K CD:770];
     - DIM-1 already requires the single-system NOT to be an involution, `IsNot.invol` [K CD:213];
     - INV2 asserts that the native operation is the involution its datum is;
     - the register model shows the datum alone does not force this.
8. **Other candidates.**
   - Parameter counting (dim of the pair span ≤ 16): LT restated relative to the COMP-1 fields [W; K2-LEDGER D4 α].
   - Local discriminability: LT restated [L, unverified].

**Every place LT is used** (named):
- (i) R-tab (C5);
- (ii) the read-out of any completion into `W 3`. Every cone statement here is about the product-test read-out, which is
  the theorem's own typing `K_p ⊆ W 3`;
- (iii) the flagged local agency, through its coordinate action;
- (iv) the frame-covariance words, computed as `W 3` maps.

LT is **not** used by:
- item 4 (it is derived there);
- the finite-group rank bound;
- the register, clock, order-3, hidden-parameter and rebit models.

### S2.4 — Native-gate compatibility (Verdict: NEW classification; DERIVED for generated cones)

- **Generativity ⇒ hgate ∧ hinv for the generated cone.** With the gate in 𝒪, the generated preparations are closed
  under it [X T4, T6]. With INV2 (or `cnotFun_cnotFun` under R-tab), so are its inverse images. Under PTQ the gate acts
  on the read-out as cnot. The gate datum is an `OpDatum` with `AffineRespect` [X T5]; `preservesBody_inducedEquiv`
  [K CA:352] then gives the body-preserving equivalence. This is a theorem about the constructed cone, not an assumption
  about a given one: the cone is defined by generation.
- **Which operation sets are consistent: the certified frame `(z3, nflip)`** [X `s2_1_native`, 42/42]:
  - **The family.** Among all 4096 signed-diagonal dressings `actC D ∘ actT E ∘ cnot ∘ actC D′ ∘ actT E′`, frame, relT
    and relC select exactly D1.4's family: 32 distinct gates [R2]. Each gate has one orientation pair (pre, post) [R3],
    and there are 8 per pair.
  - **Absorption.** `cnot ∘ L ∘ cnot` is a signed-diagonal local iff L is orientation-even (all 64 locals). Every odd L
    has a non-product axis image [R4].
  - **Odd residues are inconsistent.** All 512 ordered pairs with odd residue
    (`orient_pre(G_i) ≠ orient_post(G_j)`) have an exact negative product-effect value of `G_i(G_j(prodState x y))` on
    axis data [R5].
  - **Even residues are consistent.** Even residues are absorbed and keep images in Q3 or twin [R4, R7 + W].
  - **Hence:** a set of fixed-frame native gates is consistent **iff** all its gates share one orientation pair,
    (even, even) or (odd, odd). Each direction has its own witness:
    - (⇒) a set with any odd residue, including a gate whose pre- and post-orientation differ, has an exact invalid value
      [R5];
    - (⇐) a single class has only even residues; by [R4, R6] every element is `L` or `L ∘ cnot ∘ L′` with L even, which
      maps SEP into Q3 (or twin) [R1, R7 + W].
- **Other sets.**
  - Local rotations on all states, together with cnot: consistent; local reflections are not [K K2G:143].
  - cnot with token exchange: consistent [X Q1 + W].
  - The `CtrlGate` family [K RSB:45; keeps relC, drops relT] with proper target pre-rotation about z3: consistent
    [X Q3 + W]. With an improper one (`Rz ∘ reflY`): inconsistent (−11/50) [X U2].
  - The common criterion: **orientation coherence**. No orientation-odd local may act between two entangling steps.
- **Relation to the theorem's cone.** Generativity gives hgate ∧ hinv exactly for generated cones, and no generated cone
  in `𝒞_nat ∪ 𝒞_mono ∪ 𝒞_fin` satisfies H (S2.5). So generativity sources hgate only where H fails.

### S2.5 — What the generated systems are (Verdict: NEW exact obstruction for `𝒞_nat`; class obstruction for `𝒞_mono`, `𝒞_fin`)

**Theorem N (fixed-frame native constructions)** [X R2–R6 + W]. Let S be a nonempty consistent set of gates satisfying
`NativeGate (eball 3) z3 nflip`. Then the generated cone is K_gen if S is in the even class, and σK_gen if S is in the odd
class.
- Proof:
  1. By R5 the gates share a class.
  2. In the even class every element of ⟨S⟩ is L or `L ∘ cnot ∘ L′`, with signed-diagonal L, L′ and L even [R6, the
     whole class group, order 16].
  3. `L ∘ cnot = cnot ∘ L″` with L″ local [R6].
  4. Hence every generated table lies in `SEP ∪ cnot SEP`, and the element `L ∘ cnot ∘ L′` maps SEP onto `cnot SEP`.
  5. The odd class is σ-conjugate to the even class [R6].
- Completeness of the family beyond signed-diagonal dressings is Thread D's T1/D1.4 [W + X, audited].
- With cnot alone there is no local operation on entangled states. The full even class generates discrete local
  Paulis/transposes acting on every table, and these are absorbed.

**Theorem M (monomial class)** [X Q2 + W + L].
- **Statement.** Let H be a group of operations in `𝒞_mono`. Then every pure state of `cl cone(H·SEP)` lies in
  `cl(H)·(pure products)`.
- **Proof of the statement.** `cl(H)` is compact. Milman's converse of Krein–Milman [L, unverified] and the extremality
  of pure states in Q3 [W] give the inclusion.
- **Patterns.** Those pure states have computational modulus patterns that are permutations of rank-one patterns.
- **The witness.** `ψ_w` has pattern (9, 16, 0, 25)/50, with no rank-one arrangement among all 24 permutations [X Q2].
  `ψ_w` is pure, lies in Q3, and is Schmidt-equivalent to `cnot(prodState((3/5,0,4/5), z3))`: equal reduced Bloch length
  16/25 [X Q2] and the Schmidt theorem [L].
- **Hence:** no construction in `𝒞_mono` generates Q3; and none containing cnot images is IE1.
- **Which gates are monomial.** Every Q3-automorphism meeting the frame clause is monomial: `Ad_U(|ab⟩⟨ab|) =
  |a,a⊕b⟩⟨…|` forces `U|ab⟩ ∝ |a,a⊕b⟩` [W]; exact instance `G′ = Ad(CNOT(I⊗U_z))` [X Q3].

**Theorem F (finite groups)** [W + L]. For a finite group G of Q3-automorphisms, the pure states of `K(G)` lie in a finite
union of images of S²×S² (dimension 4). The pure states of Q3 form CP³ (dimension 6) [L], so `K(G) ≠ Q3`. An LU-orbit of
a non-maximally entangled pure state has dimension 5 [L], so IE1 fails once `K(G)` contains one.
- Exact instance `⟨cnot, SWAP⟩`: order 6 [X Q1]; `ψ_w` lies in no `g(SEP)` (rank test over all 6 elements) [X Q2].

**The generated systems** (uniform assignment with cnot gates and identity locals unless stated; ✓ holds, ✗ fails):

| construction | state cone | generated effects | hadm | hcl | hgate | hinv | H/FCC | IE1 | evidence |
|---|---|---|---|---|---|---|---|---|---|
| G0: products only | SEP | product effects (= SEP as a cone) | ✓ | ✓ | ✗ (−2, landed I2) | ✗ | ✓ (one separable argument; Thread C) | ✓ | landed + C |
| G1: {cnot}, or any even-class native set | **K_gen** | **= K_gen** [X F1] | ✓ | ✓ | ✓ [X T6] | ✓ | ✗ (−1/8 [X F4]; −1 Thread C) | ✗ (T_ψ [X F7]) | Theorem N |
| G1′: odd-class native set (gate g_Tw) | **σ K_gen** | σ K_gen | ✓ | ✓ | ✓ for g_Tw [X U3]; ✗ for cnot (chainW, −1/2) [X U3] | ✓ | ✗ ([D] contrapositive: IE1 fails) | ✗ (σ conjugates rotations to rotations) | Theorem N |
| G2: {cnot, SWAP} (SWAP an [N] datum) | K_swap ⊋ K_gen (pure witness s_w, ranks 4, 4 [X Q1]) | = K_swap | ✓ | ✓ | ✓ | ✓ | ✗ ([D] contrapositive) | ✗ (ψ_w [X Q2]) | Theorems M, F |
| G3: all `CtrlGate` gates of the frame (proper R0) | K_ctrl ⊋ K_gen (s_c, ranks 4, 4 [X U1]) | = K_ctrl | ✓ | ✓ | ✓ | ✓ | ✗ ([D] contrapositive) | ✗ (ψ_w) | Theorem M; it generates local target z-rotations on every table [X Q3] |
| G4: dual completion (states := dualW of the generated tests) | K_E ⊋ Q3 | — | ✓ | ✓ | ✓ | ✓ | ✗ (−1/2, Thread A) | ✗ (−2/5, Thread A) | Thread A [X, audited] |
| LA (flagged): cnot + local SO(3) on every state | Q3 | Q3 = dualW Q3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (by construction) | [W + L]; instance T_ψ [X Q6] |
| LA-O(3) (flagged): with reflections | inconsistent | — | — | — | — | — | — | — | [K K2G:143] |
| FC (flagged): all SO(3) conjugates of cnot | Q3 (generates LA) | Q3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | [X Q5 + W] |

In rows G1′, G2 and G3, H fails by the contrapositive of `kt4_forward_ie1` [D FHead:120]. Each of those cones meets
`hcls ∧ hadm ∧ hcl ∧ hgate`, and IE1 fails exactly.

**Answer to "does any construction from data that excludes operation-level idle extension produce more than K_gen?"**
- From the certified data, the native gate of the certified frame, alone or with all its fixed-frame companions: **no**.
  The cone is exactly K_gen (or its twin).
- With additional pair data: **yes**. Token exchange gives K_swap; the `CtrlGate` family gives K_ctrl; the dual completion
  gives K_E. None of them reaches Q3 or satisfies H.

**Where the gap is filled:**
- Within `𝒞_mono` and `𝒞_fin`, never. This holds even though the `CtrlGate` family and the even native class *generate*
  local operations (z-rotations, Paulis) acting on entangled states.
- The gap from K_gen to Q3 is filled, in every case found, only by frame-moving local rotations acting on entangled pair
  states: local agency, or frame covariance, which generates them [X Q5].
- A non-monomial, non-local operation family with no local elements is not excluded abstractly. It is not in the data,
  and its existence as a source is UNRESOLVED.

**Flagged routes, analysed only** (neither is used as a premise; neither is counted as sourcing S2):
- **Local agency** = operation-level idle extension: excluded by the protocol.
  - What it yields: IE1 by construction; with cnot, the cone Q3 [W + L, Schmidt]; with reflections, inconsistency
    [K K2G:143].
  - Exact instance: `T_ψ` is one rotation of phiW and lies outside K_gen (ranks 4, 4) [X Q6].
- **Frame covariance** (every SO(3)-conjugate `C(R,S)` of cnot is an available operation, hence preserves the cone):
  **FC ⟺ IE1 ∧ hgate**, so **given hgate, FC ⟺ IE1**. FC is equivalent to local agency for rotations, given cnot, and is
  therefore flagged in both senses.
  - (⇒) Exact words:
    - `cnot ∘ C(Rx,I) ∘ C(I,Zπ) ∘ C(Rx,Zπ) = actC(rotation about x0 by −2φ)`;
    - `cnot ∘ C(I,Rz) ∘ C(Xπ,I) ∘ C(Xπ,Rz) = actT(rotation about x2 by −2φ)`.

    Both hold symbolically modulo c² + s² = 1 [X Q5]; the countercontrol `cnot ∘ C(Rx,I)` is not local [X Q5].
    Conjugating a word by `(Q, I)` gives a word of conjugates with value `actC(Q M Qᵀ)`, so every rotation is reached
    [W]. Image equality: [W; D FIE1:398].
  - (⇐) IE1 ∧ hgate make every `C(R,S)` preserve the cone [W]. FC contains cnot itself, so FC ⇒ hgate.
  - With O(3) conjugates, FC contains `g_Tw` and cnot, whose odd residue is inconsistent [X U3; K K2G:143].

UNBUILT (no toolchain; not a kernel proof):

```lean
-- UNBUILT. S2.3: an involutive gate realizing cnot on product tables descends to tables on the generated span.
theorem ptq_of_invol {V : Type} [AddCommGroup V] [Module ℝ V] (π : V →ₗ[ℝ] W 3) (N : V →ₗ[ℝ] V)
    (pr : (Fin 3 → ℝ) → (Fin 3 → ℝ) → V) (hpr : ∀ x y, π (pr x y) = prodState x y)
    (hact : ∀ x y, π (N (pr x y)) = cnot (prodState x y)) (hinv : ∀ v, N (N v) = v) :
    ∀ v ∈ Submodule.span ℝ (Set.range (Function.uncurry pr) ∪ N '' Set.range (Function.uncurry pr)),
      π (N v) = cnot (π v) := sorry
-- UNBUILT. Flagged route: frame covariance and IE1 (design vocabulary IE1, IsRot3, trn).
def FrameCov (K : Set (W 3)) : Prop :=
  ∀ R S, IsRot3 R → IsRot3 S → ∀ ω ∈ K, actC R (actT S (cnot (actC (trn R) (actT (trn S) ω)))) ∈ K
theorem frameCov_iff_ie1 (K : Set (W 3)) (hgate : ∀ ω ∈ K, cnot ω ∈ K) : FrameCov K ↔ IE1 K := sorry
```

### S2.6 — Generated effects versus full duals (Verdict: NEW)

- **Generated effects equal generated states** [X F1 + W]. cnot is symmetric and ipW-orthogonal, so the table of
  "cnot then e⊗f" is `cnot(ehom e ⊗ ehom f)`. Sharp product effect tables are `prodState/4`, so `E_gen = K_gen` as cones.
  The same holds for every adjoint-closed group of Q3-automorphisms (ipW = 4 Tr ρρ [X F2]).
- **The full dual is strictly larger.**
  - `F ∈ dualW K_gen`: `ipW(F, prodState x y) = 1/4 − xᵀMy/4` and `ipW(F, cnot prodState x y) = 1/4 − xᵀM′y/4`, with
    M, M′ orthogonal [X F3] and the Cauchy–Schwarz step [W].
  - F is not PSD: `Tr ρ(F) ρ(T_ψ) = −1/8` [X F3].
  - So `F ∈ K_E \ Q3 ⊇ K_E \ E_gen`.
- **FCC on generated objects holds for uniform K_gen**: every checked instance is ≥ 0 [X F5, three families]. Written for
  all instances: generated states and effects lie in Q3, and FCC(Q3) holds (landed F0–F3). The failing instance
  `famI(phiW, phiW, T_ψ/4, F) = −1/8` [X F4] uses two non-generated effects.
- **What the theorem's premises consume** [X F6 source scan over D]:

  | premise or use | slots | effect set needed |
  |---|---|---|
  | hadm (b) `K ⊆ maxCone` | — | product effects |
  | (BD) `bellOf A B ∈ dualW K` | — | one generated effect per pair: the gate image of a sharp product, i.e. the test "N⁻¹ then sharp ⊗ sharp" |
  | FCC in `cross_rel` (⊆) | upper: effects bound to Bell tables, states free | generated effects |
  | FCC in `cross_rel` (⊇) and `inv_left_ctrl`, `inv_right_ctrl`, `inv_left_partner`, `inv_right_partner` | lower: states bound to Bell/link tables, **effects free over dualW K_p** | **the full duals (no-restriction)** |
  | FCC in `kt4_parity_of_witnesses` | all slots bound to gate images | generated |

  `target02` maps upper ↦ famII and lower ↦ famI [X F6], so both families are consumed with free full-dual effects. The
  bidual step `bidual_of_adm` [D FBip:110] needs the free slots to range over a set whose dual is K_p.
- **Exact consequence.** Uniform K_gen satisfies:
  - hcls, hadm, hcl, hgate (Threads A/C; [X T6]);
  - FCC restricted to generated effects (on every checked instance [X F5]; in general [W]);

  and it fails IE1. So **no-restriction is consumed and cannot be replaced by generated effects** (route refuted). The
  −1/8 instance of F4 is exactly a free-slot instance: famI with Bell states, as read through `target02`.
- **No-restriction ⟺ Q3 for unitary-generated systems** [W + L]. For an adjoint-closed group G of Q3-automorphisms,
  `E(G) = K(G) ⊆ Q3 = dualW Q3 ⊆ dualW K(G)`. So `E(G) = dualW K(G)` forces `K(G) = Q3`; the converse is self-duality of
  the PSD cone [L].

### Passes and fixed point (§A.31)

| node | outcome |
|---|---|
| N1 Theorem N, the consistency classification | NEW |
| N2 monomial obstruction, CtrlGate family, FC words, SWAP | NEW |
| N3 INV2 ⇒ LT, LT ⟺ PTQ for test-generated towers, four countermodels | NEW |
| N4 clock and compact models, finite-group rank bound | NEW |
| N5 effect consumption, `E_gen = K_gen`, FCC on generated objects | NEW |
| N6 supplementary table cells | CONFIRMING |
| passes A–C: GateRel scope, dual completion (Thread A), self-dual completion (S3's open W2), reflections | no NEW finding: fixed point; the question is answered |

`GateRel` [K PN:42] (relT + relC only, no frame, no positivity) does not define an available native gate. It is outside
the scope of availability and is not analysed further.

## 2. Ledger — certified versus added

| premise | class | anchor | used by | note |
|---|---|---|---|---|
| `W`, `prodState`, `pairVal`, `prodEffVal`, `maxCone`, `actT`, `actC` | [K] | CD:97, 161, 164, 182, 186, 198, 201 | all | `W`'s docstring (CD:95–96) states that it encodes LT |
| `cnot`, `cnotFun_cnotFun`, `cnot_frame`, `cnot_relT`, `cnot_relC`, `cnot_prodState_mem_maxCone`, `nativeGate_cnot`, `cnot_prodState_xplus_z3`, `phiW` | [K] | CD:775, 770, 848, 854, 860, 1152, 1160, 1222, 1220 | construction, validity, R0 transcription | transcribed from the source and re-checked in every script |
| `IsNot` (with `invol`), `isNot_nflip`, `NativeGate` | [K] | CD:210, 213, 838, 218 | native family, INV2 motivation | — |
| `CtrlGate`, `ctrlGate_of_nativeGate`, `GateRel` | [K] | RSB:45, 53; PN:42 | CtrlGate family; scope | — |
| `reflY`, `CandidateCone`, `idW`, `chainW`, `no_candidateCone_cnot_reflY`, `prodState_mem_maxCone`, `cnotOrbit` | [K] | K2G:46, 95, 101, 104, 143, 165, 182 | consistency, countercontrols | — |
| `ProductData`, `PreComposite`, `LocallyTomographic`, `Composite`, `JointReversible`, `paddedPre`, `paddedBall3`, `not_locallyTomographic_paddedBall3` | [K] | CI:210, 223, 235, 243, 445, 848, 909, 912 | carrier models, LT | — |
| `DirectedStages`, `SCInf`, `prepVec`, `body`, `FiniteRank`, `FiniteStage`, `body_isClosed`, `OpDatum`, `AffineRespect`, `preservesBody_inducedEquiv` | [K] | SC:63, 78, 135, 141, 299; KIF:63; CA:202, 46, 58, 352 | construction, rank, generativity | — |
| `ball3`, `eball`, `eball_three`, `IsEffectOn`, `fullAut3`, `transBody_fullAut3`, `rot3`, `rotX`, `sharpVec`, `sharpEff`, `PreservesBody` | [K] | KIF:311; TB:518, 671; KIF:116; OG:521; TB:694; KIF:411; ON:581; ES:57, 65; OG:69 | single-system data (C1, C2) | the upstream ball is taken as given (K∞-Stage) |
| `ipW`, `dualW`, `FourCopyCoherent`, `PairAdm`, `fourVal`, `PairLinked`, `target01`, `KT4Core`, `NClass`, `bellOf`, `orient`, `IE1` | [D] | FDefs:31, 34, 56, 43; FCore:30, 33, 40, 99, 132, 137, 152, 156 | S2.5, S2.6, FC | design run only |
| `cross_rel`, `link_mem`, `inv_*`, `image_eq_of_rot`, `kt4_parity_of_witnesses`, `ie1_all`, `kt4_general_ie1`, `kt4_forward_ie1`, `target02`, Lemma B1, `bidual_of_adm`, `inv_mem_of_orth`, `NClass.ipW_map`, `bell_mem`, `bell_mem_dual` | [D] | FIE1:155, 286, 304, 318, 333, 353, 398, 443; FHead:37, 102, 120; FBridge:46, 269; FBip:110, 148; FLocal:221, 266, 274 | contrapositive for H; consumption scan | design run only |
| Stage-1 audited results: Thread D's T1/D1.4/T2, Thread A's K_E and N2, Thread C's entangled core and K_c, Thread B's B1.4/B3 | audited [W + X] | `pt/D`, `pt/A`, `pt/C`, `pt/B`; `pt/audit/` | completeness of the native family; table rows G0, G4 | read as leads, re-verified where used |
| K1 gate premises, K∞-Stage, K∞-Act, K2 (LT, composite cone) | [A] open | ROADMAP K1, K∞, K2 | context | none discharged |
| **INV2** (the native gate is an operational involution) | **[N]** | — | FR, LT, GC (abstract carrier) | independently motivated (CD:770, CD:213); not a renaming; equivalent to LT at the completion level |
| generation (C6) and test generation (C7) | [N], construction | — | everything | the owner's "from data"; generation is load-bearing [X T8] |
| product action (the pair gate realizes cnot on product tables) | [N], identification of the datum | — | LT, FR | it reads only product tests of gate images of products |
| table rule R-tab (C5) | [N], construction | — | S2.1, S2.5 | builds LT in (named) |
| token exchange SWAP | [N] additional datum | — | G2 | not landed on `W 3` (SWAP occurs only in matrix-carrier modules) |
| local agency; frame covariance | flagged | — | analysis only | never a premise |
| Milman's converse of Krein–Milman; Schmidt decomposition; self-duality of the PSD cone; dimensions of CP³ and S²×S²; Mazur's theorem | [L, unverified] | — | Theorems M, F; S2.2; S2.6 | standard |

No forbidden premise is used. IE1, IE2, Q3/PSD as a premise, the complex region tower, (o) steps, operation-level idle
extension and the targets in other words occur only as properties of models or inside flagged analyses.

## 3. Candidate table

Codes: **suff** = sufficiency proved; **ref** = route refuted by an exact model; **restate** = the target restated.

| # | candidate | target | class | verdict | models | renaming / independence |
|---|---|---|---|---|---|---|
| 1 | LT + finite single-system ranks | FR | [N] (LT) | suff [W] | — | LT is a target itself |
| 2 | finitely many independent tests | FR | restatement | restate | — | inputs2 RANK R0 |
| 3 | compactness of the body | FR | [N] | ref | compact padded model [X K2] | it suffices for hcl [W] |
| 4 | INV2 / finite operation group + bi-affine products | FR | [N] | **suff** [W + X K3] | the clock model fails the candidate and FR | strictly stronger (register model) |
| 5 | reversible gate with product action + test generation + validity | FR | [N] | ref | clock [X K1] | — |
| 6 | every test is a product test after available operations | LT | [N] | ref | register [X L4] | — |
| 7 | INV2 + product action + generation | LT | [N] | **suff** [W + X L1–L3] | register, rebit, hidden-parameter models each fail one ingredient and LT; order-3 has LT without carrier INV2 | not a renaming; completion-level equivalent |
| 8 | parameter counting / local discriminability | LT | restatement | restate | — | K2-LEDGER D4; [L] |
| 9 | generativity | hgate ∧ hinv of the generated cone | construction | **suff** [X T4–T6] | — | a theorem about the generated cone |
| 10 | consistent fixed-frame native gates | Q3 / H / IE1 | [K]-predicate class | ref (exactly K_gen / σK_gen) | Theorem N [X R2–R6] | — |
| 11 | frame-monomial operations (incl. CtrlGate, SWAP, phases, Paulis) | Q3 / IE1 | [N] class | ref | ψ_w [X Q2] | — |
| 12 | finite operation groups | Q3 / IE1 | [N] class | ref | dimension [W + L]; K_swap [X Q2] | — |
| 13 | dual completion (states := dualW of the generated tests) | H | [N] | ref | K_E (Thread A) | overshoots Q3 |
| 14 | FCC on generated effects + per-pair premises | conclusion C | restriction of H | ref | K_gen [X F5, F7] | — |
| 15 | local agency (rotations) | IE1, Q3 | flagged | IE1 by construction; Q3 [W + L] | reflections inconsistent [K] | it IS operation-level idle extension |
| 16 | frame covariance | IE1 | flagged | ⟺ IE1 given hgate [W + X Q5] | — | restatement of IE1 given hgate |
| 17 | no-restriction (unitary-generated systems) | K = Q3 | [N] | ⟺ [W + L] | — | — |

## 4. Cross-thread notes

- **S3 (COMP-CONS).**
  - (i) **FCC's force against the native construction lies entirely in no-restriction.** On generated objects, FCC holds
    for uniform K_gen; the consumed failing instance uses non-generated effects (S2.6). COMP-1's `PreComposite`
    quantifies `prodEff_effect` over *all* `IsEffectOn` effects of the factor bodies [K CI:223–230]. So Thread C's N0,
    read with the pair bodies as factors, builds no-restriction for the pair systems into the four-token principle.
    That is the ingredient the native data lack.
  - (ii) **Orientation coherence is forced by consistency of a generated pair system.** The consistent native sets are
    exactly one orientation class (S2.4), so a consistent generated pair system carries one orientation bit. This bears
    on token-level orientation coherence; EvenCycle is a four-pair statement and is not derived here.
  - (iii) On generated objects, FCC is the validity of the two-layer native circuit on four tokens (cnot on 01, 23, then
    on 02, 13, read through product tests) [W, definitional]. That circuit is an (o)-type construction, so it cannot
    serve as a premise.
  - (iv) A self-dual completion is a choice, not a generation. Whether the cnot-invariant self-dual cone between K_gen
    and K_E is unique is S3's open W2. Bit symmetry ⇒ self-duality (Müller–Ududec) [L, unverified] would need a rich
    reversible group: a lead only.
- **Thread A.**
  - Generalizes A's N2 (native closures) from {cnot} to every consistent fixed-frame native set (exactly K_gen or its
    twin), and to the monomial class.
  - Compactness, not finite rank, is what closedness consumes.
  - The INV2 route gives FiniteRank of a data-generated pair completion without assuming LT.
- **Thread B.**
  - Generativity sources hgate ∧ hinv for generated cones without restating them, but only for cones where H fails.
  - B's "a product-only system admits no OpDatum for cnot" agrees: generation must include gate images.
  - The consistency criterion (one orientation pair) is B's B1.4 (`hgate ⟺ orient(A′,B′) = orient(A,B)` on aligned
    families), read as a validity condition of generated systems.
- **Thread D.** D1.4's finite native family is confirmed exactly within signed-diagonal dressings (32 gates), and T2
  (one orientation per gate) on that family.
- **Integration review.**
  - U1–U3 are sharpened. A non-restating route to S2 = hadm ∧ hcl ∧ hgate exists for data-generated pair systems:
    DERIVED under R-tab with LT built in, CONDITIONAL on INV2 on an abstract carrier. Its cone is K_gen.
  - **S2 ∧ S3 is unsatisfiable by every construction class examined** that does not let frame-moving local operations
    act on entangled states.
  - U6 (LT) becomes CONDITIONAL on INV2 for data-generated systems.
- **K2-LEDGER.** LT ⟺ PTQ for test-generated towers sharpens D3/D6. The PTQ-not-LT padded control is invisible to a
  test-generated completion.

## 5. What is not claimed

- **Not kernel-checked.** Nothing here is a kernel proof. The Lean in §1 is UNBUILT. The audited theorem and Lemma B1 are
  [D].
- **INV2 is not derived.** It is a named [N] principle. LT and FR are CONDITIONAL on it for data-generated systems, not
  DERIVED. Relative to L alone, LT and finite rank remain independent (register and clock models; landed
  `paddedBall3`).
- **Scope of the obstructions.**
  - Theorems N, M and F are for the stated classes. They are not impossibility statements about every observer-native
    extension.
  - A non-monomial, non-local operation family without local elements is not excluded; it is not in the data.
  - Completeness of the fixed-frame native family beyond signed-diagonal dressings rests on Thread D's audited T1/D1.4
    [W + X].
- **Scope of [X].** Exact computations are stated for their instances: the finite stages, axis and Pythagorean data, and
  the named models. Universal statements rest on the cited [W] arguments or on symbolic identities. In particular:
  - FCC on all generated objects of K_gen rests on [W] (all of them lie in Q3, and the landed FCC(Q3)), not on the
    sampled checks;
  - the clock model's infinite rank rests on the [W] pigeonhole step.
- **Q3 as a property.** Q3/PSD appear only as properties of models (membership tests and witnesses), never as premises.
- **No physical claim.** The countermodels (register, clock, hidden-parameter, order-3, compact padded) are mathematical
  models. Local agency is excluded here as a premise by the protocol. Nothing is claimed about nature.
- **Substratum.** No OI-native pair system is constructed. The single-system ball is taken from L, and its substratum
  source is open (inputs2: ALL FAIL; K∞-Stage).
- **No repository changes.** Nothing edits or proposes edits to `main`, the ROADMAP, manuscripts or Lean results. Bands
  are unchanged; this is consistency-axis work.

## 6. Evidence log

All scripts were run as `python3 -I -B <script> ../base/verification/lean-mathlib/OIBridge` from `pt/S2/`.
`s2_6_effects` also takes `../inputs/fourcopy`. Python 3.11.15, sympy 1.14.0, exact arithmetic only. Decision rules were
fixed in each header before the first run, and VERDICT lines print only over green checks and countercontrols. No timing
appears in stdout. Each `.err` holds only the appended `exit=0` (sha256 `19eaf438…f061`).

| script | sha256 (script) | sha256 (output) | checks | countercontrols | runs | replay |
|---|---|---|---|---|---|---|
| `s2_1_native.py` | `bfc060b4a13dbc51bd6c627e9007ee3757cab9979b68f74c8cac5a27ff23f810` | `b108e6bc93a3f14b865771c4965e499bb4640d08e78d9a6794f3de1bdd978835` | 42 PASS, 0 FAIL | 5 | 1 | byte-identical |
| `s2_2_beyond.py` | `a18988f5087cad66075b07cb3e568e352c2c99cf1c742adde1dc75ba259e04d7` | `81742db2c4e7a9111b6199f8100f94937abc41d9b3f4d1a0d478bb8faca5b9e8` | 38 PASS, 0 FAIL | 5 | 1 | byte-identical |
| `s2_3_lt.py` | `d614b9fd20574b419feb6247125a7a31a9379845fae703ef9d009f89f6585e3a` | `6c3567146390cc0138dff77d07676aec6b1d856a9e7805a98e8c0c79c3bd174c` | 35 PASS, 0 FAIL | 4 | 1 | byte-identical |
| `s2_4_rank.py` | `62969064aa56ba608b11b86076394b3714d31805cd06ff0cf8db82683ee898aa` | `279a9d691f9c4fc4c483a9126fa6ef117aa48fd8a28b1515bf7c627bf08a816b` | 15 PASS, 0 FAIL | 2 | 1 | byte-identical |
| `s2_5_tower.py` | `321ac1ee664ec8050b7a693ccbf41d824ee3c7f06b399e42ef084a7b54777df0` | `af620ebefdebe8f009a41c0c37ecffa10925792d7beb66e4b69ec71aa64ebc64` | 17 PASS, 0 FAIL | 1 | 1 | byte-identical |
| `s2_6_effects.py` | `9c3f1d9f2987be3bd49e713da66a3c2831d57e054c9becbf256b952227fde4a4` | `79d17b0dbbe8dc3068027ed230cd912fbca27cbf707d1b30a09fafca7e0c3e4b` | 22 PASS, 0 FAIL | 2 | 1 | byte-identical |
| `s2_7_supp.py` | `6e43f7627647311f88ebde43fb65b611385e458f90d5eda0ed0dad7cdd247a49` | `83de5a691122cf44a16156863591965e139b3d02c74297782a7d560cd557b213` | 13 PASS, 0 FAIL | 1 | 1 | byte-identical |

Total: 182 PASS, 0 FAIL. Every countercontrol failed as required. No failed run occurred, so there are no `.runN.*` files.

**Pre-run edits** (each made before the script's first and only run; NOTES N2, N4, N5):
- `s2_2`: header wording of Q2's cross-check; Q3's monomiality check made convention-free.
- `s2_5`: a vacuous T2 comparison was removed and restated as the inclusion check; T3/T5 were moved to stage 2; T5 is
  tested by exact rank equality; table caching.
- `s2_6`: non-PSD of ρ(F) is certified by a trace with a pure state instead of symbolic eigenvalues.

## 7. Integrity

**Start.** Recorded in `.start_marker`, written before any other file, at 2026-10-10T07:26:56Z. `pt/S2/` was empty
beforehand.
- `sha256sum -c --quiet` on `inputs.manifest.sha256`, `stage1.manifest.sha256` and `inputs2.manifest.sha256`: all OK.
- `git -C base rev-parse HEAD` = `9f9f8257a980a1819fbbc1dc0019917cf8678626`; `git -C base status --porcelain` empty
  (0 lines).
- Protocol hashes, recorded = actual: `PROTOCOL.md` `239dc123…fa9b23`, amendment 1 `b41aa0e7…31cf83`, amendment 2
  `2a2f78f3…c530a`, `PROTOCOL-STAGE2.md` `38603692…da18da`.

**End.** Run at 2026-10-10T08:34:50Z, after every script run and replay and before this section was written.
- The three manifests: OK.
- Base HEAD `9f9f8257a980a1819fbbc1dc0019917cf8678626`; status empty (0 lines); no `__pycache__` or `.pyc` under
  `base/`.
- The four protocol files: unchanged (the same four hashes).
- No file newer than `S2/.start_marker` exists under `pt/` outside `S2/` and the parallel thread's `S3/`.
- `pt/S2/` holds 38 entries, each written by this thread:
  - `.start_marker`, `NOTES.md`, `RESULT.md`;
  - for each of the seven scripts, `.py`, `.out`, `.err`, `.replay.out` and `.replay.err`.
- Every script and output hash in §6 was recomputed and matches, and every replay is again byte-identical.

**Conduct.**
- Writes were made only inside `pt/S2/`. Python ran as `python3 -I -B`, so no bytecode was written. The inline edit
  helpers (Python read from stdin) wrote only `pt/S2/` files.
- Git was used read-only (`rev-parse`, `status`). There was no branch, push, PR, CI, GitHub access or publication, and no
  agent was spawned. Network: none used.
- Integrity events: none. No file this thread did not write appeared in `pt/S2/`, so no `INTEGRITY.md` or
  `quarantine/` was needed.
