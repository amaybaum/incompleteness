# EQ3-P — running notes (design only; base `bcbc516f`, read-only at `scratchpad/eq/base/`)

Question (owner): can the requirement that an operation remain valid when an independent system is added (IE₁ at two
copies, IE₂ at three) be derived from a genuinely observational consistency principle, without assuming quantum
composition in advance? Principle under test: composition coherence KT∞ (every regrouping of a finite family into two
parts is a valid COMP-1 composite of the parts; each part carries its full state and effect sets).

Nothing here is adopted, frozen or governed. No Lean was built (no toolchain); Lean text is UNBUILT. Writes only inside
`scratchpad/eq3/P/`. Exact arithmetic for anything certified; floating point is exploration only (`_float` in the
file name, header banner), never evidence.

## N0. Integrity at start (2026-10-08 17:55 UTC)

- `cd scratchpad/eq/base && sha256sum -c --quiet ../base.manifest.sha256`: silent, exit 0; 1317 files on disk, 1317
  manifest lines.
- `/home/user/incompleteness`: `git status --porcelain` empty; HEAD `bc3bf9bc846c138de5f5b45f386a75244da4f21f`.
- `scratchpad/eq3/` held only `PROTOCOL.md`; `scratchpad/eq3/P/` created empty, with `.start_marker` (mtime
  17:55:51) for the end-of-thread write check.
- Tools: python 3.11.15, sympy 1.14.0 (exact work); numpy 2.4.6, scipy 1.17.1 (float exploration only).

## N0.1 Productivity test (fixed before the walk; copied from the protocol, not edited afterwards)

A finding is a **gem** iff it is one of:
1. an exact countermodel to "KT∞ (at a stated finite instance) with the named premises implies IE₁ / parity /
   `K₃ = PSD₈`";
2. a theorem route, every step checked, from KT∞ at a stated instance to one of those;
3. an exposed hidden assumption in the KT∞ formulation: which bipartitions, link states or effect sets it presupposes.

Otherwise record-only. Results are stated for the finite instance actually used (four or six copies), never for
"KT∞" in general unless proved for all instances.

## N0.2 Decision rules for every script (rules, not expected numbers)

- R1 A script's header states its decision rule before its first run. A VERDICT line prints only when every check,
  control and countercontrol passed; otherwise `VERDICT NOT RENDERED`.
- R2 Identities are certified only as exact symbolic identities (generic symbolic entries, `expand(...) == 0`) or
  exact rational / Gaussian-rational evaluations; ranks by exact rational linear algebra; signs by exact values.
  No `sympy.solve` (hash-order dependence under `-I`, EQ2-B N4).
- R3 Every favourable check gets a countercontrol that a wrong convention or a wrong object would fail.
- R4 Kernel conventions (the `W 3` carrier, `cnot`, `reflY`, `phiW`, `idW`) are parsed from the base files and
  compared with hand transcriptions (transcription control), as EQ2-A did; nothing is imported from `eq2/` or
  `eqreview/` (independence of code), though their results are cited.
- R5 Harness errors are recorded; failed runs are kept as `.runN.*`; replays are byte-identical or reported.

## N1 node log (two copies: does KT∞ at four copies imply IE₁?)

(entries below are appended in order)

### N1.0 Reading at the base (read, not built; paths under `verification/lean-mathlib/OIBridge/`)

- `W 3 = Fin 4 → Fin 4 → ℝ` (CompositeDimension:97), index 0 the unit; `prodState x y μ ν = hom x μ * hom y ν`
  (CD:161); `pairVal a b ω = ∑ a μ ω μ ν b ν` (CD:164); `actT N ω = ω · homMap(N)ᵀ` (CD:198), `actC N ω = homMap(N) · ω`
  (CD:201); `cnot` the signed permutation `sgn/pc/pt` (CD:741-786); `phiW = diag(1,1,-1,1)` (CD:1220) with the landed
  `cnot_prodState_xplus_z3 : cnot (prodState xplus z3) = phiW` (CD:1222).
- COMP-1: `PreComposite` (CompositeInterface:223-230): `convex`, `prod_mem` (products of factor states are states),
  `prodEff_effect` (for EVERY effect `e` of body ΩA and EVERY effect `f` of ΩB, `prodEff e f` is an effect of the joint
  body), `prodEff_unit`; `Composite` adds `lt` (CI:243). The quantifier "every effect of the factor body" is the
  no-restriction clause; when the factor is a group, it means every effect of the group's composite.
- `condA_mem` (CI:431): conditional states are states **given `IsCompact ΩA`** (closedness is an explicit hypothesis of
  the kernel's conditional lemma). `subset_maxBody` (CI:467): body ⊆ max body.
- K2Guard: `reflY` (K2G:46), `CandidateCone` (K2G:95), `idW` (K2G:101), `cnot_idW` (K2G:110),
  `no_candidateCone_cnot_reflY` (K2G:143).

### N1.1 Plan of the four-copy derivation (written before any script; to be checked exactly in p1)

Table calculus (native, no Pauli dictionary needed): states of a pair are tables `X ∈ W 3`, effects of a pair are
tables `E` paired by the Euclidean pairing `⟨E, X⟩ = Σ E μν X μν` (for product effects this is `pairVal`). With pair
cones all equal to `K` (closed convex cone) and effect cone `K*` (Euclidean dual), the instance
KT(4; 01|23, 02|13) gives two families of inequalities:
- (i) states `X` on (0,1), `Y` on (2,3) (product across 01|23: `prod_mem`), effects `E` on (0,2), `F` on (1,3)
  (product across 02|13: `prodEff_effect`): `Σ E[μ0,μ2] F[μ1,μ3] X[μ0,μ1] Y[μ2,μ3] = ⟨X, E·Y·Fᵀ⟩ ≥ 0`;
- (ii) states `L` on (0,2), `L'` on (1,3) (product across 02|13), effects `e` on (0,1), `f` on (2,3) (product across
  01|23): `⟨e, L·f·L'ᵀ⟩ ≥ 0`, i.e. the conditional state `L·f·L'ᵀ` lies in `K** = K` (closedness).
Expected consequences (to be checked):
- Bell link `Δ := phiW = cnot(prodState xplus z3)`; `Δ·f·Δ = T f` (`T` = global transpose `transposeW`). With
  `L = L' = Δ` in (ii): `T(K*) ⊆ K`. `cnot` is an orthogonal involution of the tables, so `K*` is `cnot`-invariant and
  `Δ ∈ K*`; with `E = F = Δ` in (i): `K ⊆ T(K*)`. Hence `K = T(K*)` (the coordinator's expectation).
- **Beyond `K = T(K*)`:** with non-maximal links `L_a = cnot(prodState x z3)` (pure input `|a⟩`; the state
  `a0|00⟩ + a1|11⟩`), (ii) gives `L_a·f·L_{a'}ᵀ ∈ K`, which in operator form should be `Ad(D⊗D')(T f)` with
  `D = diag(a)`, `D' = diag(a')`: local diagonal filters. Applied to `f = T(cnot(prodState xplus y))` (in `K*`), this
  should put every pure state with a generic coefficient matrix `D·Circ(b)·D'` into `K`; closedness and convexity
  then give `Q3 ⊆ K`, and `K ⊆ T(K*) ⊆ T(Q3) = Q3`. If every step checks, the four-copy instance forces `K = Q3`
  with NO local invariance assumed, and IE₁ follows (Q3 is invariant under every local unitary).
- Twin analogue: gate `cnot' = actT reflY ∘ cnot ∘ actT reflY`; twin links `L·Δ` (`actT reflY ω = ω·Δ`); expected
  `K = K*` and `K = Tw`.
This is the favourable branch: maximum skepticism, countercontrols, and foils for every hypothesis (gate, closedness,
no-restriction, the coherence of the two groupings).

### N1.1 Node: the four-copy link identities (`p1_four_copy_links.py`, own library `eq3_lib.py`)

- **Run 1** (kept `p1_four_copy_links.run1.{py,out,err}`): 29/30, VERDICT NOT RENDERED. Failing check: the
  countercontrol "the orientation of the second link matters", tested with the Schmidt-diagonal link `L_a`. That link
  is SWAP-symmetric (`|00⟩ + u|11⟩`; `L_aᵀ = L_a`), so the countercontrol was vacuous. Harness error of my design.
- **Run 2** (kept `.run2.*`): 30/31, NOT RENDERED. The replacement link `g = cnot(|+⟩⟨+| ⊗ |b⟩⟨b|)` is also
  SWAP-symmetric (coefficient matrix `Circ(1, v)` is symmetric). Same harness error, second instance.
- **Run 3**: 32/32, `P1-FOUR-COPY-LINKS-EXACT`. The countercontrol now uses the non-symmetric product link
  `|+⟩⟨+| ⊗ |b⟩⟨b|`; both symmetric facts are kept as note-checks. Decision rule unchanged across runs.
- Side fact from the harness errors (useful for the hidden-assumption audit): **every link the derivation uses is
  SWAP-symmetric**, so the derivation does not depend on which token of a link pair is "first".

Verdict at the node (exact, symbolic unless noted):
- A1/A2: family (i) value `= ⟨X, E·Y·Fᵀ⟩`; family (ii) conditional `= L·f·L'ᵀ` (four-copy contraction is matrix
  multiplication of tables). A3: agrees with explicit four-qubit traces (operator cross-check, 3 random exact).
- B: `Δ = phiW = cnot(prodState xplus z3)` (landed CD:1222, re-checked); `cnot` is a Euclidean-self-adjoint
  involution (so `K*` is cnot-invariant); `transposeW` commutes with `cnot`; `Δ·f·Δ = T f`. Hence the instance gives
  **`T(K*) ⊆ K` (Bell links, family ii, closedness) and `K ⊆ T(K*)` (Bell effects, family i): `K = T(K*)`** —
  the coordinator's expectation, now with the exact link identities.
- C: **the Schmidt-diagonal link `L_a = cnot(coords|a⟩⟨a| ⊗ hom z3)` (the state `|00⟩ + u|11⟩`) induces a local
  filter**: `L_a·f·L_a'ᵀ = 4·coordsW(Ad(D⊗D')(pauliW(T f)))`, `D = diag(1,u)`. The induced one-copy map `M_D` is a
  Lorentz boost (it mixes the unit index), outside the `homMap`/`actC`/`actT` vocabulary. So KT(4; 01|23, 02|13)
  says more than `K = T(K*)`: with `K = T(K*)`, `K` is invariant under every local diagonal filter `Ad(D⊗D')`.
- D: `L_a·(T g)·L_a'ᵀ = 4·coordsW(|χ⟩⟨χ|)` with `g = cnot(|+⟩⟨+| ⊗ |b⟩⟨b|)` and `χ` of coefficient matrix
  `D·Circ(b)·D'`; every coefficient matrix with all four entries nonzero has this form (explicit factorization,
  a complex square root). So every **generic pure state lies in `K`** (generic = dense among pure states).
- E (twin): with `cnot' = R_B cnot R_B`, links `L_a·Δ`, the conditional is `4·coordsW(Ad(D⊗D')(pauliW f))` (no
  transpose); twin Bell link `idW`: the twin instance gives `K = K*` and the same filter invariance.
- F (converse): QM values nonnegative (6 random exact); filter conditional of a PSD effect is PSD (2 exact).

## Amendment 1 received (coordinator message, mid-N4; appended to eq3/PROTOCOL.md, read 2026-10-08 ~18:35 UTC)

Read in full. It refines, it does not replace. How the walk absorbs it:
- **Milestones in order:** (1) four-copy co-self-duality `K₂ = T(K₂*)`, proved or refuted exactly — p1 B-section
  proves it exactly (written assembly + exact link identities); the explicit link-state checks (b) are added in p2.
  (2) cone uniqueness, minimal extra structure, in the order: admissibility + co-self-duality alone; + gate
  invariance; + a further finite symmetry. p1 C/D already show the four-copy instance supplies MORE than
  co-self-duality (local filters through the gate's Schmidt-diagonal links); that is reported as the selecting
  structure, and the three-step ladder is still walked for the shadow statements. (3) IE₁. (4) IE₂ incl. every twisted
  configuration. (5) general composition only after 1–4.
- **No circularity:** every derivation step will carry a tag (s) state-level / (2) operation on a standalone
  two-token composite / (o) operation on part of a larger composite (forbidden as a premise).
- **Hidden assumptions (a) uniform composition and (b) link states:** (a) to be removed or stated: the pair cones
  `K_01, K_23, K_02, K_13` are allowed to differ, each with its own native gate in its own orientation (twist bits),
  and the (03)(12) links are included; (b) `Δ` as a state (gate on a product state of the standalone pair) and as an
  effect (dual action of the gate on a product effect), including the twisted orientation `R_B Δ = idW`, checked
  exactly in p2.
- **Independent content of KT:** not treated as adopted; classified as: QM satisfies it; the transported landed
  two-copy premises do not imply it (exact foil `K_F`, p2); then what it implies / does not imply.

## Amendment 2 received (coordinator message; appended to eq3/PROTOCOL.md, read ~18:50 UTC)

Read in full: split `K₂ = T(K₂*)` into (I) `T(K₂*) ⊆ K₂` and (II) `K₂ ⊆ T(K₂*)`, each audited for regrouping,
conditioning, Bell link (state or effect) and uniformity; trace Bell effects to premises; settle whether the gate's
dual action on effects is automatic; fix charts, orientations and link-induced transposes; classify the outcome into
the owner's five cases; answer the decisive question.

### N1.2 Reading for Amendment 2 at the base

- `IsEffectOn Ω e := ∀ x ∈ Ω, 0 ≤ e x ∧ e x ≤ 1` (KInfFoundations:116): an effect is EVERY affine functional with
  values in [0, 1] on the body. COMP-1's `prodEff_effect` (CI:227) quantifies over exactly these.
  **Consequence:** in the base vocabulary the dual (Heisenberg) action of a body-preserving map sends effects to
  effects automatically (`e ↦ e ∘ G` keeps values in [0,1] when `G` maps the body onto itself); no separate
  availability assumption enters the cone statements.
- EFF-1 (EffectSpace.lean header, :519-575) separates two questions. Q-CONE: under OG-1's named hypotheses every
  **sharp** effect is available (`sharpFamily_subset_avail`) and the sharp family determines `maxCone (eball d)`
  (`maxConeOf_sharpFamily`, :549). Q-SET: the full affine effect set is available only with the named
  `MixingClosed` and the unit (`fullEffects_subset_avail`), and fails without it (`not_fullEffects_of_orbit`).
  `sharpVec b = (1/2, b/2)` (EffectSpace:57).
- So the Bell effect needs: (i) `sharp(xplus) ⊗ sharp(z3)` is an effect of the pair body: COMP-1 `prodEff_effect`
  with two sharp single-system effects (effects by `IsEffectOn`; available by EFF-1 Q-CONE under OG-1's hypotheses);
  (ii) its image under the dual action of the standalone pair gate is an effect: automatic for `IsEffectOn` effects.
  If KT's group effect sets were read as AVAILABLE tests rather than `IsEffectOn` effects, (ii) would be a separate
  availability assumption (EFF-1 shows availability of non-sharp effects is itself conditional).

### N1.3 Node: Amendment audit, twisted configurations, general charts, foils (`p2_audit_twists_foils.py`)

Run 1: 23/23, `P2-AUDIT-TWISTS-FOILS-EXACT` (decision rule in the header, fixed before the run; two pre-run edits:
`nsimplify` removed from the rational Cayley rotations, a dead expression removed from Z1/Z2 — both before any run).

**Milestone 1, the two inclusions audited separately** (pair cones `K_ij`, closed convex, effect sets `K_ij*` =
all `IsEffectOn` functionals; tags (s) state-level, (2) operation on a standalone two-token composite, (o) operation
on part of a larger composite):
- **(I) `T(K_23*) ⊆ K_01`.** Regrouping 02|13 contributes a product of STATES `Δ(02) ⊗ Δ(13)` [prod_mem, (s)];
  regrouping 01|23 contributes products of EFFECTS `e(01) ⊗ f(23)` [prodEff_effect, (s)]; conditioning rule: the
  conditional of the 02|13 product given `f(23)` is a state of group 01 [all `e ∈ K_01*` + closedness, the analogue
  of `condA_mem` CI:431, (s)]; Bell link enters as a STATE: `Δ = cnot(prodState xplus z3)` [gate on a product
  state of the standalone pairs 02 and 13, (2)]. Identity: `Δ·f·Δ = T f` (N1). Uniformity: none between 01 and 23;
  only "the link pairs carry the native gate".
- **(II) `K_01 ⊆ T(K_23*)`.** Regrouping 01|23 contributes a product of STATES `X(01) ⊗ Y(23)` [prod_mem, (s)];
  regrouping 02|13 contributes a product of EFFECTS `Δ(02) ⊗ Δ(13)` [prodEff_effect, (s)]; no conditioning; Bell link
  enters as an EFFECT: `Δ/4 = cnot(sharp(xplus) ⊗ sharp(z3))`, the dual image of a product effect [product effect by
  prodEff_effect with two sharp single-system effects (EFF-1 Q-CONE availability), (s); dual action of the standalone
  pair gate, (2), automatic because effects are `IsEffectOn` functionals and `cnot` is a self-adjoint body-preserving
  involution fixing the unit (P2)]. Identity: `⟨X, Δ·Y·Δ⟩ = ⟨X, T Y⟩` (N2).
- The coordinator's expectation is confirmed exactly as stated: (I) Bell states on 02|13 + effect products on 01|23;
  (II) Bell effects on 02|13 + state products on 01|23. Each is proved; together `K_01 = T(K_23*)`; with `K_01 = K_23`
  (equality in a shared chart) this is `K = T(K*)`.
- Twisted orientation (P3): `cnot' = R_B cnot R_B` gives the twin Bell state `idW` and the twin Bell effect `idW/4`;
  link-induced maps (P4): `Φ⁺` induces `T`, `R_B Φ⁺` induces the identity, a mixed pair induces one partial transpose.
  The (03)(12) links give `L·fᵀ·L'ᵀ`, i.e. `T(swap f)` with Bell links (P5).
- **No (o) step occurs.** The gate is applied only to states and effects of a standalone pair composite; everything
  four-copy is products, effect products and conditioning.

**Uniform composition is not needed (general charts, U1-U2).** With arbitrary fixed token charts (each ball chart
fixed up to O(3); no alignment with gate frames) and each pair gate in N-CLASS form `ℓ₁ ∘ cnot ∘ ℓ₂` (EQ2-B, [X+W]),
the Bell links of pairs 02 and 13 induce `Θ(g) = H_R02 · g · H_R13ᵀ` with `R = A·reflY·Bᵀ ∈ O(3)` from the post-local
`ℓ₁ = (A, B)`, and the instance gives `K_01 = Θ(K_23*)`. The filter links then make `K_01` invariant under the
A-conjugated local filters (U2, symbolic), which with the gate's rotation links generate every local rotation and
filter. So each pair cone is classified on its own; the link-induced `R_ij` are the chart identifications the links
define (`Φ⁺` ↦ `reflY`, i.e. the transpose; `R_B Φ⁺` ↦ identity). The twist bits become defined only AFTER this
classification (relative to the fixed charts), and then:

**Twisted configurations (Z1-Z3):** for all 16 assignments `τ` on (01, 23, 02, 13) with gate `cnot^(τ)` on each pair,
the instance is consistent iff the 4-cycle parity `τ01 + τ13 + τ23 + τ02` is even (Z1 sign-map algebra; Z2 own
recomputation of the −2 values, matching EQ2-A D1 on the other labelling); every even pattern is realized by
`K4 = PT_S(PSD_16)` (Z3). So at four copies the twisted pair configurations are exactly the coboundary ones.

**Foils / independent content (F1-F4):**
- F1: `K_F` (Clifford cone; own BFS, order 11520; generators are Ad of explicit unitaries) satisfies admissibility,
  gate invariance and closedness, and violates the instance: four-copy value `−1/200` with states `Δ(02) ⊗ Δ(13)`
  and effects `w(01) ⊗ f(23)`, `w = (49/50)·1 − ψψ†` (in `K_F*` by the exact orbit bound `|r_A|² ≤ 45/49 < (24/25)²`),
  `f = ψψ†`. So the transported landed two-copy premises do NOT imply KT(4; 01|23, 02|13).
- F2: SEP and max satisfy the instance (product identities) and fail the gate: KT alone creates no entanglement;
  the gate is load-bearing.
- F3: with the effect set restricted to Q3 (strictly inside `K_F*`), `K_F` satisfies the restricted instance: the
  full (`IsEffectOn`) effect set is load-bearing.
- F4: `int(Q3) ∪ conv(SEP ∪ cnot SEP)` is convex, cnot-invariant, admissible, not closed, ≠ Q3 (`ψψ†` outside), and
  satisfies the instance (its dual is Q3): closedness is load-bearing (conclusion without it: `int Q3 ⊆ K ⊆ Q3`).

### N1.4 Node: general gate links (`p3_general_links.py`, run 1: 5/5, `P3-GENERAL-LINKS-EXACT`)

The conditional through a general gate link `cnot(coords|a⟩⟨a| ⊗ coords|b⟩⟨b|)` is
`4·coordsW(Ad(C ⊗ C')(pauliW(T f)))` with the NON-symmetric coefficient `C = diag(1,u)·Circ(1,v)` (row = first token;
`Cᵀ` fails: countercontrol). The links supply exact X- and Z-rotation filters (`(1 − t²)·1 + 2it·X`, `diag(1, e^{iθ})`
with rational parametrization), whose induced one-copy maps are `homMap R`, `R ∈ SO(3)`; by the Euler decomposition
(written) they generate SO(3). This certifies the ingredients of the general-chart claim of N1.3.

## N4 node (literature, before writing the N1 theorem up as a closure)

Egress: `arxiv.org`, `ar5iv.arxiv.org`, `alphaxiv.org` and `quantum-journal.org` are blocked by the session's egress
policy (WebFetch `EGRESS_BLOCKED`); per the proxy README this is not to be routed around. Only search-engine summaries
were available, so **every literature item below is UNVERIFIED (not read at the source)**.
- Barnum–Gaebler–Wilce, "Ensemble steering, weak self-duality, and the structure of probabilistic theories" (arXiv
  0912.5532; Found. Phys. 43 (2013) 1411, per Wilce's CV): for weakly self-dual state spaces, steering of every state
  from a two-copy bipartite state ⟺ homogeneity of the cone; with self-duality, Koecher–Vinberg gives a Jordan
  algebra. [unverified]
- Wilce, "Conjugates, filters and quantum mechanics" (arXiv 1206.2897; Quantum 3 (2019) per CV) and "A royal road to
  quantum theory (or thereabouts)" (arXiv 1606.09306): a conjugate system with a perfectly correlating bipartite state
  `η` gives a self-dualizing inner product; with symmetric reversible filters preparing every interior state, the
  model is homogeneous and self-dual, hence Jordan by Koecher–Vinberg. [unverified]
- Barnum–Barrett–Leifer–Wilce, "Teleportation in general probabilistic theories" (arXiv 0805.3553): post-selected
  teleportation needs an isomorphism between the state cone and the effect cone (an isomorphism state and effect);
  conditioning an isomorphism state on an isomorphism effect realizes an order-isomorphism. [unverified]
- Müller–Ududec, PRL 108, 130401 (2012) (arXiv 1110.3516): bit symmetry (reversible interchangeability of logical
  bits) forces self-duality. Krumm–Müller, npj QI 5 (2019) (arXiv 1804.05736): reversible circuit models whose bits are
  balls of arbitrary dimension are severely restricted. [unverified]
- Barnum–Wilce, Found. Phys. 44 (2014) 192 (arXiv 1202.4513): Jordan-algebraic (homogeneous self-dual) systems +
  locally tomographic composites + one qubit leave only complex finite-dimensional QM with superselection rules
  "under natural constraints on systems and composites" (the constraints were not visible). [unverified]
- Barnum–Graydon–Wilce, Quantum 4, 359 (2020) (arXiv 1606.09331): non-signalling composites of EJA models; in InvQM a
  composite of two complex systems picks up an extra classical bit (a direct sum with the conjugate). [unverified]
- Barnum–Beigi–Boixo–Elliott–Wehner, PRL 104, 140401 (2010): quantum local systems + no-signalling force quantum
  bipartite correlations without assuming the tensor-product rule. [unverified]
- Chiribella–D'Ariano–Perinotti, PRA 81, 062348 (2010) (arXiv 0908.1583): purification + local discriminability;
  their operational-probabilistic framework builds parallel composition of tests into its axioms. [unverified]
- Barrett, arXiv quant-ph/0508211, and later GPT surveys: transformations are required to remain valid in parallel
  composition (complete positivity relative to a chosen composite); no source found that DERIVES that requirement from
  the state spaces of composites. [unverified; search summaries]
- Self-dual tensor products: "Self-Dual Cone Systems and Tensor Products" (arXiv 2408.07389) reports that a cone
  system contained in its dual extends to a self-dual one (a Barker–Foran-type existence result), and "Beyond operator
  systems" (arXiv 2312.13983) reports not knowing self-dual tensor products "in the middle" other than simplicial
  cases. [unverified]

Bearing on this thread (my reading of the summaries, not of the sources):
- The N1 mechanism (a Bell link as an isomorphism state/effect gives co-self-duality; non-maximal links give
  filters, i.e. homogeneity-type transitivity) is the known conjugate/steering mechanism in a local, finite form.
  New here (relative to what the summaries describe): (i) the correlating states and the filters are not postulated:
  the native gate on standalone pairs supplies them; (ii) everything happens at one finite instance of state-level
  composition coherence (four copies, two groupings); (iii) the conclusion is the specific cone Q3 / the twin with no
  Koecher–Vinberg step (the gate supplies the pure states directly).
- No summary describes a result that derives parallel composition of OPERATIONS (idle extension) from kinematic
  composite principles; the frameworks either build it in (OPT, categorical) or impose it as complete positivity.
  This node does not establish that no such result exists (sources not read).

### N1.5 Node: milestone 2 ladder — what the two-copy SHADOWS select (`p4_cone_ladder.py`, run 1: 9/9)

Pre-run edits (before any run): `sympy.linsolve` replaced by Cramer's rule (no solver calls); an always-true check
turned into a NOTE.
- **Shadow (S-tw) "admissible + K = K*"** (what twin links give): does NOT select Q3 or the twin. Countermodel
  (written existence proof with exact ingredient): `y = diag(1,1,0,1) ∈ max \ (Q3 ∪ Tw)` (L1); `C0 = SEP + ℝ₊y` is
  Euclidean self-positive; in a Euclidean space a maximal self-positive closed cone is self-dual (if `z ∈ K* \ K`, then
  `K + ℝ₊z` is self-positive since `⟨z,z⟩ ≥ 0`), so Zorn gives a self-dual admissible `K ∋ y`, `K ∉ {Q3, Tw}`.
  Not constructive; not gate-invariant in general.
- **Shadow (S-cn) "admissible + K = T(K*)"** (what Bell links give): OPEN. Evidence, not a decision:
  (L2) the isotropic-sector necessary condition admits the one-parameter family of right-angle wedges `W_s`,
  `s ∈ [0, 1/2]`, between the Q3 wedge (s = 0) and the twin wedge (s = 1/2), all containing the SEP wedge (exact, closed
  forms nonnegative on the interval); (L3) no admissible co-self-dual cone is a T-isometric image of a round Lorentz
  cone with T-even axis (B-null products span 12 dimensions, exact rank, but must map into a 7-dimensional subspace);
  (L4 + written) B-isometric deformations of Q3 have no first-order admissible direction off the boundary at real
  products. The B-form version of the Zorn argument fails (a maximal B-self-positive cone can stop at B-null boundary
  points), so existence is not settled by that route.
- **Shadow + gate invariance:** OPEN for both forms (the gate adds the finite group {1, cnot}; the Zorn route needs
  `⟨z, cnot z⟩ ≥ 0` and fails in general).
- **Further finite symmetry: not needed.** The four-copy instance itself supplies more than its co-self-duality
  shadow: the gate's non-maximal links make every pair cone invariant under all local filters and rotations
  (continuous, not a finite symmetry), and that selects Q3 / the twin (N1.1-N1.4).
- **Minimal selecting structure (answer to milestone 2):** state-level coherence at the four-copy instance, used with
  the gate's links of every Schmidt rank (not only the maximally entangled `Φ⁺`), plus admissibility, the native gate
  on standalone pairs, closedness and the full (`IsEffectOn`) effect sets. No uniform composition and no extra finite
  symmetry. Which of Q3 / the twin a pair carries is fixed by the orientation of its gate in the token charts.

## N2 node log (three copies: EQ2-A's wall; IE₁ is now DERIVED by N1, not assumed)

### N2.1 The six-copy instance (`p5_six_copy.py`, run 1: 9/9, `P5-SIX-COPY-EXACT`)

Instance KT(6): triples 012 and 345; link pairs 03, 14, 25 (standalone pair composites with their native gates,
hence Q3 or twin by N1). Groupings: 012|345 (state products, effect products, conditioning), 03|1425 and 14|25 (to
form the link product as a state, or the link effect product). Three-copy table calculus: family (i3) value
`⟨X, (E⊗F⊗G)·Y⟩` (S1), family (ii3) conditional `(L⊗L'⊗L'')·f` (S2), both symbolic; operator cross-check by explicit
6-qubit placement (S6).
- (I3) `T3(K_345*) ⊆ K_012`: Bell STATES on 03, 14, 25 [prod_mem on 03|1425, 14|25: (s); links from the standalone
  pair gates: (2)], effect products on 012|345 [(s)], conditioning on 012|345 [(s) + closedness].
- (II3) `K_012 ⊆ T3(K_345*)`: state products on 012|345 [(s)], Bell EFFECTS on 03, 14, 25 [effect products: (s);
  dual gate action: (2)]. (S3: `(Δ⊗Δ⊗Δ)·f = T3 f`, `pauli3(T3 f) = pauli3(f)ᵀ`.)
- Filters (S4, symbolic on copies 0 and 2; general links per factor by p3 G1 and the factorization S2): every local
  filter maps `K_012` into itself — **SLOCC invariance of the three-copy cone**, derived, no (o) step.
- Twin / mixed links (S5): identity / partial transposes, as at two copies.

### N2.2 What this does and does not settle

- **GHZ dichotomy (written; exact ingredient S7).** For a closed, SLOCC-invariant `K₃` with (I3)+(II3):
  `K₃ = PSD₈` ⟺ `K₃` contains one GHZ-class pure state (Cayley hyperdeterminant ≠ 0; the GHZ class is one SLOCC orbit,
  dense among pure states — Dür–Vidal–Cirac [L, unverified]; S7 checks the invariant's values and its SLOCC
  covariance exactly). Twisted version: `K₃ = PT_S(PSD₈)` ⟺ `K₃` contains `PT_S` of a GHZ-class state. Hence for
  c = 1 (all pair marginals twins, no coboundary pattern) a valid `K₃` contains NO `PT_S`(GHZ-class) element for any
  S; for c = 0, `K₃ ≠ PSD₈` forces `K₃` to contain no GHZ-class state.
- **No-generation lemma (written).** Every state that KT can GENERATE from pair-level objects (products across
  groupings, conditioning on products of pair/single effects, starting from pair and single states and
  biseparable three-copy states) is a contraction of a tensor network whose nodes have at most two copy-legs, with each
  copy on at most one state node and one effect node; components are paths or cycles, so the result is a product of
  pair and single states. KT generation therefore never puts a GHZ-class state into `K₃`. If KT∞ forces IE₂, it does so
  only through its fixed-point content (co-self-duality at every level, plus the SLOCC invariance it induces), not
  by generation.
- **The minimal hulls are excluded** (cited, not re-run here): `M_bs` (= BS, c = 0) violates (I3) with Bell links and
  effects `½ − Γ` and `Γ` (EQ2-A D4, −1/16; replayed by the coordinator); the all-twisted hull `B_tw` (c = 1; `M_tw`,
  and `M_odd` after the reflection chart) is not self-dual (EQ2-A a4c: `F, G ∈ B_tw*`, `tr(FG) = −½`; independently
  rechecked by the coordinator 13/13). So M_odd, M_tw, M_bs fail KT∞ at six copies.
- **The intermediate candidates survive the derived symmetry (exploration only).** `x1_slocc_orbit_float.py`
  (FLOATING POINT, EXPLORATION ONLY; 60 BFGS starts each): the SLOCC-orbit self-pairing of EQ2-A's c = 1 candidate
  `F + t·1` has minimum `t²` (t = 0.1, 0.15, 0.2, 0.3), and of the c = 0 GHZ-witness `1 − cΓ` has minimum
  `(1 − c/2)²` (c = 1.5, 1.9, 2.0), both attained at rank-one degenerate filters. No negative value was found. This
  is NOT evidence of self-positivity; it only says the one-orbit test with the newly derived SLOCC symmetry did not
  produce an exclusion lead. Analytic remark (written): diagonal SLOCC transition maps on the GHZ-diagonal sector
  scale coherences by `2ρ/(A_b + ρ²/A_b) ≤ 1` (AM-GM), so SLOCC can only contract the non-PSD part of a sector
  element; it cannot amplify a violation.
- **Refined wall (N2, both c):** Is every closed, SLOCC-invariant (`GL(2,ℂ)^{×3}`), co-self-dual
  (`K₃ = T3(K₃*)` for c = 0; `K₃ = K₃*` for c = 1) cone with `BS_τ ⊆ K₃ ⊆ BS_τ*` and pair marginals `R_B^τ Q3`
  equal to `PSD₈` (c = 0) / non-existent (c = 1)? Equivalently (c = 0): must such a cone contain a GHZ-class state?
  EQ2-A's wall was the same question for local-UNITARY invariance; the six-copy instance upgrades it to SLOCC.
  Status: OPEN. N3 (purification fallback) is not entered: N2 produced no KT∞ countermodel.
- `x2_sector_float.py` (FLOATING POINT, EXPLORATION ONLY): the GHZ-diagonal sector of the c = 0 candidate
  `conv(BS ∪ SLOCC·(1 − 2Γ))`, from 6000 sampled generators: (a) pairwise inner products all positive (min 3.7e−3);
  (b) all 200 probed extreme directions of the sampled dual lie outside the sampled cone. **Inconclusive by design**
  (harness lesson, recorded): a sampled hull is strictly smaller than the true cone, so the extreme points of its dual
  always stick out; this test cannot distinguish "not self-dual" from "self-dual after closure". No lead either way;
  not cited as evidence.

### N2.3 Fixed point (§A.31) and the decision not to enter N3

- Passes: N1 (NEW: four-copy filter links; uniformity not needed; twisted configurations = coboundaries; foils),
  N1.5 (ELABORATING: shadows), N2.1 (NEW: six-copy co-self-duality + SLOCC of K₃, both inclusions), N2.2
  (NEW-borderline: GHZ dichotomy and no-generation lemma; the refined wall), x1/x2 (no new finding).
  Two consecutive passes (N2.2 explorations, the x2 probe) produced no NEW finding; the fixed point is NOT reached
  (the protocol asks for 3-4), and the wall is stated with its refinement.
- N3 (purification) is conditional on a KT∞ countermodel from N2; none was found, so N3 is not entered.
- Milestone 5 (general composition) is conditional on milestones 1-4; milestone 4 is open, so it is not taken up.

### N1.6 / N2.4 Node: cheaper certificates (`p6_cheap_foils.py`, run 1: 4/4, `P6-CHEAP-FOILS-EXACT`)

- The native group `H = ⟨cnot, actC nflip, actT nflip⟩` has order 8; its generators are `Ad CNOT`, `Ad(X ⊗ 1)`,
  `Ad(1 ⊗ X)` (symbolic Pauli-dictionary identities). `C_H = cone(H · products)` is admissible, closed, cnot-invariant,
  contains `Δ`, and violates KT(4; 01|23, 02|13) with the same witness as `K_F` (`w = (49/50)·1 − ψψ†`, `f = ψψ†`,
  value `−1/200`), now with an 8-element orbit certificate (max marginal norm² 45/49) instead of 11520.
- Own recheck of EQ2-A D4: the biseparable hull BS violates the six-copy instance (I3): Bell links, effects
  `½ − GHZ` (in BS*) and `GHZ`, value `−1/16` (exact; control with a biseparable state: 0).
- Replay: `run_all.py` now covers p1-p6; all six identical (`run_all.out`); the earlier five-probe replay is kept as
  `run_all.prelim.out`. Float explorations replayed by `run_explorations.py`, both identical.
- Harness note: a `tail -3` with several files errored in a hash-listing shell command (shell usage only; no file
  affected).

## N9. Integrity at the end (2026-10-08 ~19:07 UTC)

- Base: `cd scratchpad/eq/base && sha256sum -c --quiet ../base.manifest.sha256` silent, exit 0; 1317 files; no
  `__pycache__` under the base.
- `/home/user/incompleteness`: `git status --porcelain` empty; HEAD `bc3bf9bc846c138de5f5b45f386a75244da4f21f`
  (unchanged); `git diff-index --cached --quiet HEAD` exit 0. No working-tree file is newer than this thread's start
  marker. The `.git` DIRECTORY mtime moved to 19:06:34, the second of my final `git status --porcelain`. `git status`
  creates and removes a transient `index.lock` when it attempts an index refresh. No file inside `.git` is newer
  than the marker, and `.git/index` is unchanged (mtime 2026-10-07 00:26). Recorded as the only out-of-directory
  side effect of this thread; it came from a read-only command and did not write the index.
- Scratchpad files newer than the start marker outside `eq3/P/`: `eq3/PROTOCOL.md` (Amendments 1 and 2, the
  coordinator's), `eqreview/EQ2-SYNTHESIS.md` (18:09), `eqreview/EQ3-AUDIT-CHECKLIST.md` (18:50),
  `eqreview/audit_eq3_n1.py` (19:05) — the coordinator's files, not this thread's. This thread read
  `eqreview/EQ2-SYNTHESIS.md` and `eqreview/REVIEW.md` at the start (as the protocol required) and did not open the
  later coordinator files.
- Every file this thread wrote is inside `scratchpad/eq3/P/` (listing in RESULT §7); no `__pycache__` there (all runs
  `-B`).
