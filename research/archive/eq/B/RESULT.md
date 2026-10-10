# EQ-B — reversible dynamics and gate sourcing (K∞-Act): RESULT

Research only, ungoverned, nothing adopted. Base: certified `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58`, read at
`scratchpad/eq/base/` (read-only). Every file written is in `scratchpad/eq/B/`. Node log: `NOTES.md`. Scripts and their
outputs are listed in §3; `run_all.sh` replays them. Evidence tags: **[K]** kernel identifier at `bcbc516f`
(file:line), **[X]** exact computation here (script + output), **[W]** written proof here, **[L]** literature,
**[P]** prior off-repo ledger, **[R]** a reading of which hypothesis a landed proof consumes.

Notation (CompositeDimension): `H = HVec d`, joint carrier `W d`, `Ñ = homMap N`, `tens X Y = X ⊗ Y`,
`C = span(e₀, lift z) = span(hom z, hom(−z))` (the classical control sector), `T = lift(z^⊥)` (the tangent control
sector), `M₀ = Mfwd z G`. The J/K data at odd `d ≥ 3`: `E₊ = span(u, x)`, `E₋ = span(y, w…, z)`, `X : u ↔ x`, `K` an
orthogonal complex structure on `E₋`, `J` an orthogonal complex structure on `T` (at `d = 5` the data of the landed
`gC5`, RelcSelectC5.lean:17–23).

## 1. Finding

None of the three principle shapes yields the control gate of RELC-SELECT-1 in its natural existential form, because
one exact family satisfies all three at `d = 5` (and the construction works at every odd `d ≥ 3`) and fails `relC`: the
landed J/K gate `gC5` together with an exact one-parameter extension `G_t` with `G_π = gC5`. The control relation
splits exactly as `relC ⇔ CI ∧ TR`, where CI is the −z-corner identity `G(hom(−z)⊗Y) = hom(−z)⊗Ñ M₀ Y` (the only form
in which the block reduction reads `relC`) and TR is the same relation on the tangent control sector `T⊗H` (the half
the parity count needs beyond CI). Conditioning the copy's NOT on a sharp `z`-test, consistently with the joint cone,
gives the frame and CI, hence `p_N ≤ 1` through the landed block reduction, and nothing of TR (`gC5` is such a
conditioning gate); a continuous reversible interaction — a one-parameter group, two-sided positive,
normalisation-preserving, not of product form and creating entanglement from a pure product — exists at every odd
`d ≥ 3` and passes through `gC5`; and `gC5` has a Hadamard-type role-exchange symmetry. Two shapes become theorem
routes once one named clause is added. For
conditioning the clause is naturality: the conditioned operation is single-valued and coherent under outcome
relabelling (transport by the control's NOT, then relabel, equals post-composition). Given CI this coherence is TR,
it derives `relC` in three lines, and the common `N` then comes from type-level availability of the target's NOT on the
control copy — which is where K∞-Copy goes, since with token-level groups `gC5` satisfies natural conditioning exactly
with two different NOTs. For continuous interaction the clause is local `SO(d)` transitivity inside the same connected
dynamical group: it destroys the J/K interaction at `d = 5` and `d = 7` (exact witnesses outside `maxCone`) and gives
`d = 3` by Krumm–Müller's theorem (literature, not verified against the source). For role exchange no clause was
found. For QB2, K∞-Trans is exactly pure-state transitivity plus boundary purity; continuous reversibility supplies
K∞-Act-type data and pure-state transitivity and holds in all of finite complex QT, but the qutrit — complex QT — has a
non-extreme boundary state and so is boundary transitive for no family, so boundary purity must enter as an
elementary-scoped geometric clause (K∞-Geom's content); whether continuous reversibility forces it at capacity two is
open.

## 2. Evidence level

| claim | level |
|---|---|
| `blockData_of_ctrlGate` reads `relC` only through `gate_corner_neg_ctrl` (CI); `dim_of_ctrlGate` reads it once more, for parity | [R] RelcSelectBlock.lean:95 (`gate_actC_ctrl`, used only at :103), :746; field-access count frame 4, posFwd 7, posInv 3, relC 3 (one in `ctrlGate_of_nativeGate` :56) |
| relC ⇔ CI ∧ TR (under `IsNot`, frame, posFwd) | [W] (Ñ preserves `C` and `T`; on `C⊗H` relC is CI by `corner_form` CompositeDimension.lean:1805); [X] `b1_conditioning` C2 on cnot1, cnot, gC5; C7 a linear map with TR and ¬CI |
| the weak corner form `G(hom(−z)⊗Y) = hom(−z)⊗M₁Y` is automatic from frame + posFwd | [W] (`corner_form` at `−z` applied to `(I⊗ρ̃_z)∘G`, ρ_z the reflection through `z^⊥`); [P] relt N2.1 |
| conditioning COND(N) gives the frame and CI; with P± it gives `BlockData (tangentPlus N)`, hence `p_N ≤ 1`, for `2 ≤ d` | [W] (frame and CI directly); [R] for the block data (the landed proofs re-read with CI); Lean draft `blockData_of_cornerGate` UNBUILT |
| cnot1 (d=1), cnot (d=3) and gC5 (d=5) satisfy COND with `M₀ = I`, `M₁ = Ñ` | [X] `b1_conditioning` C1 |
| gC5: IsNot, frame, posFwd, posInv, relT; ¬relC | [K] RelcSelectC5.lean:68, :154, :360, :369, :161, :179; reproduced [X] C0 |
| gC5 fails TR, at the tangent input `lift(e_w₁)⊗e₃`, entry (4,4): −1 vs +1 | [X] C3 |
| natural conditioning (Cov_N, Rel, Post_N) ⇒ relC(N_A, N) | [W] three lines; Lean draft `relC_of_naturalCond` UNBUILT |
| each pair of the three laws is realised with gC5 at d = 5, and the third fails | [X] C6(i)–(iii) (positivity of every value: [K] gC5 and local NOTs preserve `maxCone` [W]) |
| complex QT satisfies natural conditioning (lift N ↦ X); the SU(2) lift N ↦ iX breaks Post; Ad(\|0⟩⟨0\|⊗I+\|1⟩⟨1\|⊗iX) has COND and fails relC | [X] `b2_qt` Q2 (minimal domain {±z}×{I,N}²). [W] with tests over the whole sphere and Cov over all of SO(3) on the control (conjugation does not see the lift's phase), action domain {I, N}, for every lift with L(I) = I and L(N)² = I; spot checks exact (π-rotation about (3/5, 4/5, 0); R_z with cos φ = −7/25). [W] Post over all target rotations is QT-incompatible: it forces L(S)L(a) = L(Sa), a homomorphic lift SO(3) → U(2), and lifts of π-rotations about x and z anticommute. Post over the rotations about x is QT-consistent (lift t ↦ P₊ + e^{it}P₋, the group of Q5) |
| "conditioning composes" is QT-incompatible on the Klein group: for all 16 phase choices C(X)C(Z) = Ad(Z⊗I) C(Z)C(X) ≠ C(Z)C(X) | [X] Q3; [W] every QT gate with COND(V) is Ad(diag(e^{iα}, e^{iβ})⊗I · controlled-V); [L, unverified] Araújo–Feix–Costa–Brukner, NJP 16, 093026 (2014) (no control of unknown unitaries) |
| Cov over O(3) is QT-incompatible (r_y⊗I does not commute with any QT COND(X) gate) | [X] Q4 (cnot, Ad CNOT); [W] (r_y reverses J) |
| kernel `cnot` = Ad(CNOT) exactly; CNOT lies on the QT group G_t = Ad(\|0⟩⟨0\|⊗I + \|1⟩⟨1\|⊗(P₊ + e^{it}P₋)) | [X] Q1, Q5 |
| J/K flow `G_t` (jk.py): G_0 = I, G_π = kernel cnot (d=3) / kernel gC5 (d=5), G_t G_t = G_2t, G_t G_−t = I, normalisation, COND(R_t), operator-Schmidt rank 4, G_π frame ∧ ¬relC at d = 5, 7; at d = 3 equal to the QT group | [X] `b4_jkflow` F1–F4 (d = 3, 5, 7; cos t = 3/5, −7/25), `b2_qt` Q5 |
| J/K flow two-sided positive for every t, every odd d ≥ 3 | [W] V ≥ \|x_T\|\|e_T\|(√(αβ) − √(a′²+b′²)) by AM–GM and Bessel; [X] the exact identities S1 (value decomposition), S2 (⟨f,Y⟩⟨f,R_tY⟩ − ⟨f,A_tY⟩² − ⟨f,B_tY⟩² = (2 − 2cos t)(PM − \|ω\|²)), S3 (PM − \|ω\|² ≥ 0 by an explicit sum of squares) at d = 3, 5, 7; posInv from G_t⁻¹ = G_−t. For odd d ≥ 9, S1–S3 rest on the written Binet–Cauchy reading below, which is uniform in d, and are not computed |
| no joint state space between products and `maxCone` is invariant under gC5 and the quarter turn of the plane (2,4) | [X] `b5_localwords` W5: exact rational witness, value −13755583160854480616171902/9729699913814233289411449 ≈ −1.4138; W7 at d = 7 (≈ −1.4142) |
| d = 3 control: cnot (I⊗L₃) cnot is the QT channel Ad(CNOT(I⊗V)CNOT) | [X] W3 |
| the J/K interaction creates entanglement: gC5(prodState(e_x, z5)) = diag(1,1,−1,0,0,1) has witness value −2 for Λ(ω) = ω₀₀ − ω_xx + ω_yy − ω_zz, which is ≥ 0 on all products | [X] `b5_localwords` N2; [W] (Λ = 1 − a·Mb on products, M a contraction) |
| gC5 has 8 signed-permutation role-exchange symmetries `SWAP G SWAP = (h⊗h)G(h⊗h)⁻¹` (h z = e_x); cnot has 2 (Hadamard type); cnot1 none | [X] `b3_rolex` |
| gC5 satisfies the two-NOT relation Rc(N_A, nC5), N_A = diag(1,−1,1,−1,−1) balanced (3,3), nC5 unbalanced (2,4); natural conditioning with token groups holds exactly | prior: this pair is NB-1's countermodel C2N (NB-1 preregistration, minimality table, row "one `N`"; positivity written there). Here: [X] C5 (the relation re-verified), C8; [K] for frame, relT(nC5), P± through gC5 |
| BoundaryTransitive ⇔ PureTrans ∧ BP (compact convex body with interior, body-preserving family) | [W] from [K] TransitiveBody.lean:284, :290 |
| qutrit: diag(1,1,0)/2 is a non-extreme boundary state, so no family is boundary transitive on it | [X] `b6_qb2` Q1 + [K] TransitiveBody.lean:301 |
| Carathéodory orbitope: SO(2)-transitive on its extreme points, with a non-extreme boundary point, capacity ≥ 3 | [X] Q2(a)–(e) |
| Krumm–Müller, npj QI 5, 7 (2019), Thm 1: d-ball gbits, local group SO(d), no-signalling, tomographic locality, closed connected global group ⇒ for d ≠ 3 the global group is the local one | [L, unverified]: search summaries only, since arxiv.org, nature.com and discovery.ucl.ac.uk are blocked by the egress policy |
| MMAP, J. Math. Phys. 55, 122203 (2014): among d-ball bipartite theories with LT and continuous reversible dynamics only two-qubit QT has entanglement; MMAP, PNAS 110, 16373 (2013): continuous reversibility, tomographic locality, information unit, no simultaneous encoding ⇒ QT; de la Torre–Masanes–Short–Müller, PRL 109, 090403 (2012): local qubits + one continuous reversible interaction ⇒ QT; Dakić–Brukner 2009 (Deep Beauty 2011): information capacity, locality, continuous reversibility | [L, unverified], as above |
| Gross–Müller–Colbeck–Dahlsten, PRL 104, 080402 (2010): reversible boxworld dynamics are local operations and system permutations; Al-Safi–Short, J. Phys. A 47, 325303 (2014): the same for all strongly non-local boxworld systems (the 2011 Al-Safi–Short paper, PRA 84, 042323, is on information causality) | [L, unverified]; [W]: a COND gate with a non-identity conditioned action is neither local nor a permutation composed with local maps |

**Written proof W-JK (two-sided positivity of the J/K flow).** Let `e`, `f` be the homogenised coefficient vectors of
a control and a target effect (both in `Lor`), `x` a control state and `Y = hom y` a target state.
1. By S1, `V = ½(1+x_z)(e₀+e_z)α + ½(1−x_z)(e₀−e_z)β + (e_T·x_T)a′ + (e_T·Jx_T)b′`, where `α = ⟨f,Y⟩`,
   `β = ⟨f,R_tY⟩`, `a′ = ⟨f,A_tY⟩` and `b′ = ⟨f,B_tY⟩`.
2. The factors `1 ± x_z`, `e₀ ± e_z`, `α` and `β` are all ≥ 0, since `R_t` is an orthogonal map of the ball. By AM–GM
   the first two terms are ≥ `√((1−x_z²)(e₀²−e_z²)αβ) ≥ |x_T||e_T|√(αβ)`.
3. `J` is orthogonal with `J² = −1` on `T`, so `x_T ⊥ Jx_T` and `|Jx_T| = |x_T|`. Bessel then gives
   `|(e_T·x_T)a′ + (e_T·Jx_T)b′| ≤ |e_T||x_T|√(a′²+b′²)`.
4. By S2, `αβ − a′² − b′² = (2 − 2cos t)(PM − |ω|²)`. By S3, `PM − |ω|²` is a sum of nonnegative terms: Lorentz-cone
   factors and the complex Lagrange squares in the coordinates in which `K` is multiplication by `i`.
5. Hence `V ≥ 0`, so `G_t(prodState x y) ∈ maxCone` for every real `t`. Since `G_t⁻¹ = G_−t`, the same bound gives
   posInv.

S2 is the Binet–Cauchy identity `(v₀†Ωv₀)(v_t†Ωv_t) − |v_t†Ωv₀|² = det Ω · |v₀ ∧ v_t|²`. Here `Ω = [[P, ω̄],[ω, M]] ⪰ 0`
on `ℂ²`, with `v₀ = (1, 1)` and `v_t = (1, e^{−it})`. In this form the flow is the d = 3 controlled-U(1) structure
carried by the complex structures `J` and `K`. Provenance: NB-1 already reduced the positivity of the J/K map (its
countermodel C5, the landed gC5) to the complex CNOT by a written argument; the flow `G_t`, its group law and the proof
above for every `t` are this thread's.

## 3. Countermodels and controls

Scripts (run `python3 -I -B <script>` in this directory; `run_all.sh` runs all of them twice and compares):

| script | checks | output | what it shows |
|---|---|---|---|
| `b1_conditioning.py` | 39/39 | `b1_conditioning.out` | C0 controls reproduce the landed facts: frame, `G²=I`, relT, relC/¬relC, and the values 1 and −1 of `gC5_relC_lhs`/`rhs`. C1 COND for cnot1, cnot, gC5. C2 the CI/TR split. C3 the TR witness for gC5. C4 splits. C5 the two-NOT relation. C6 the three-law separations. C7 the linear TR∧¬CI countercontrol. C8 natural conditioning with token groups at d = 5 |
| `b2_qt.py` | 16/16 | `b2_qt.out` | Q1 kernel cnot = Ad(CNOT). Q2 natural conditioning in QT, with the iX-lift countercontrol. Q3 the Klein-group composition obstruction. Q4 the O(3) obstruction. Q5 the QT one-parameter group through CNOT, equal to the J/K flow at d = 3 |
| `b3_rolex.py` | 4/4 | `b3_rolex.out` | role-exchange symmetries of cnot, cnot1 (none) and gC5; gC5's reversed frame on ±e_x |
| `b4_jkflow.py` | 43/43 | `b4_jkflow.out` | F1–F4 exact flow facts at d = 3, 5, 7. S1–S3 symbolic identities at d = 3, 5, 7. Countercontrols CC1 (R_−t with A_t, B_t: −18/25) and CC2 (J-output scaled by 6/5: −1/5) |
| `b5_localwords.py` | 10/10 | `b5_localwords.out` | W5, W7 exact negative witnesses. Control: the (w₁,w₂)-plane word is nonnegative. W3: the d = 3 word is a QT channel. N1: the gC5 image of (e_x, z5) and its ±E_{w₁w₁} perturbations. N2: that image is entangled (witness value −2) |
| `b6_qb2.py` | 10/10 | `b6_qb2.out` | the qutrit; the Carathéodory orbitope (a)–(e) |
| `x1_jk_flow_float.py`, `x2_local_words_float.py`, `x3_simple_words_float.py`, `x4_d7_word_float.py` | exploration | `x*.out` | **floating point, labelled exploration only**: they located the flow's positivity and the failing words; every verdict above is re-derived exactly |

Replay: `sh run_all.sh` ran every script twice and compared the outputs. `run_all.log` records the sha256 prefix of
each script, each output and each helper (`blib.py`, `qlib.py`, `jk.py`, `EqBDraft.lean`). All ten scripts give
`replay=identical`, the six exact scripts print green verdicts (122 checks, none failing), and the run exits 0.

The countermodels, and the clause each one separates:
- **gC5 with nC5, z5 at d = 5** satisfies COND (existential conditioning), P±, IsNot, relT, the frame and CI. It fails
  TR and relC. Its split is (2,4), unbalanced. It separates "conditioning + joint cone" from CtrlGate. It also satisfies
  any two of Cov_N, Rel, Post_N.
- **The J/K flow `G_t` at d = 5 and d = 7** is a one-parameter group, two-sided positive, normalisation-preserving and
  non-product. `G_π` is a frame gate that fails relC. It separates "continuous reversible interaction" from CtrlGate,
  and also from `d ∈ {1,3}`.
- **gC5 with h** (e.g. `h = [[0,0,0,0,1],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,−1,0],[1,0,0,0,0]]`) separates role exchange
  from CtrlGate.
- **gC5 with N_A ≠ nC5** (NB-1's C2N, now with kernel positivity) satisfies the two-NOT native-gate hypotheses. It
  separates K∞-Copy from the two-NOT hypotheses and from token-level natural conditioning.
- **The qutrit** satisfies continuous reversibility and fails K∞-Trans for every family.
- **The Carathéodory orbitope** satisfies continuous reversibility on its extreme points and fails boundary purity. It
  has capacity ≥ 3, so it is not elementary.

Controls that had to come out a specific way, and did:
- The landed `cnot` and `cnot1` satisfy everything they must.
- The d = 3 J/K flow equals the QT group exactly.
- The d = 3 local-rotation word is a QT channel.
- The (w₁,w₂)-plane word, inside the J/K commutant, stays nonnegative.
- The iX lift breaks Post.
- CC1 and CC2 show that the sign structure and the orthogonality of J are load-bearing.
- G_0 has operator-Schmidt rank 1, so the rank test is not vacuous.

Errors found and fixed during the walk: the first sum-of-squares certificate for S3 used conjugated Lagrange minors
and failed at d = 5, 7. It now uses `a_i b_j − a_j b_i` and passes; the identity itself was never in doubt. The early
`b1` import failed under `python3 -I` (no script directory on the path); every script now inserts its own directory.
`-I` also ignores `PYTHONDONTWRITEBYTECODE`, so an early replay left a bytecode cache in this directory; it was removed,
and every run line now passes `-B`. The written QT converse for natural conditioning was first stated "over all of SO(3)
with any lift L(S⁻¹) = L(S)⁻¹" without its action domain. It holds with Cov over SO(3) and the actions {I, N}; with Post
over all target rotations, natural conditioning is QT-incompatible (§2).

## 4. Proposed next theorem(s)

Lean statements are drafted in `EqBDraft.lean`, which is **UNBUILT**.

| id | statement | layer | direction |
|---|---|---|---|
| T1 | `relC_iff_corner_and_tangent`: under IsNot, frame and posFwd, `relC ↔ CornerId z N G ∧ TangentRel z N G` | Lean (linear algebra + `corner_form`) | forward (structure of the selector's premise) |
| T2 | `blockData_of_cornerGate`: `2 ≤ d → IsNot → CornerGate → BlockData (tangentPlus N)` (CtrlGate with relC replaced by CI) | Lean (re-statement of RelcSelectBlock §B–§D with the CI field) | forward |
| T3 | `cond_gC5 : Cond z5 nC5 gC5` and `cond_not_dimension_selecting` | Lean (decide-style, like `gC5_frame`) | separation (forward route needs more than conditioning) |
| T4 | `isNot_nA5`, `gC5_relC_two : actC nA5 (gC5 (actC nA5 ω)) = actT nC5 (gC5 ω)` | Lean (like `gC5_relT`) | separation (K∞-Copy) |
| T5 | `relC_of_naturalCond`; with Slice, P± and `N_B ∈ 𝒢_A` it gives `CtrlGate` and hence `d = 1 ∨ d = 3` by `dim_of_ctrlGate` | Lean (three rewrites) | forward (theorem route given NC) |
| T6 | `exists_jkFlow5`: a continuous one-parameter group through gC5, posFwd at every t | Lean (moderate: polynomial identities S1–S3 with `c² + s² = 1`; AM–GM and Bessel as in `selC5_core`) | separation (continuous interaction ⇏ d ∈ {1,3}) |
| T7 | `not_maxCone_gC5_rot`: the word gC5 (I⊗L) gC5 leaves `maxCone (eball 5)` | Lean/exact (rational evaluation, like `gJ5_value`) | separation (local transitivity is the excluding clause) |
| T8 | import of Krumm–Müller Thm 1 for two copies: closed connected group ⊇ SO(d)×SO(d) with a non-local element preserving an LT joint state space ⇒ d = 3 | written/literature (needs compact Lie theory, absent from Mathlib to my knowledge) | forward |
| T9 | `boundaryTransitive_iff_pureTrans_and_boundaryPure` | Lean (two lines from TransitiveBody :284, :290) | forward (decomposes K∞-Trans) |

## 5. Dependencies

- **Other threads.** None is consumed. The balanced-NOT question (frame + relT + two-sided positivity at a NOT with
  equal eigenspaces, e.g. PARITY-NOT-1's `n5`) belongs to another thread. Nothing here decides it, and the natural
  conditioning route does not need it.
- **Corpus at `bcbc516f`.** Lean files are under `verification/lean-mathlib/OIBridge/`; each identifier below was
  checked at its cited line in the extracted base. NB-1's records are under
  `verification/programmes/oi-qm/reconstruction/round-nb-1-native-gate-ball/`.
  - CompositeDimension.lean: `IsNot` :210, `NativeGate` :218, `corner_form` :1805, `Mfwd` :1878, `gate_corner_neg`
    :1965, `cnot` :775, `cnot_relC` :860, `nativeGate_cnot` :1160, `entangling_cnot` :1380, `dim_of_nativeGate` :2723,
    `cnot1` :2765, `isNot_neg1` :2794, `nativeGate_cnot1` :2861, `not_entangling_cnot1` :2869.
  - RelcSelectBlock.lean: `CtrlGate` :45, `ctrlGate_of_nativeGate` :53, `gate_actC_ctrl` :92, `gate_corner_neg_ctrl`
    :99, `actT_slice_ctrl` :492, `blockData_of_ctrlGate` :716, `dim_of_ctrlGate` :739 (parity read :746),
    `three_of_ctrlGate` :753.
  - RelcSelectParity.lean: `finrank_plus_eq_finrank_minus_relC` :329, `not_even_of_relC` :354.
  - RelcSelectC5.lean: `isNot_nC5` :68, `gC5` :134, `gC5_frame` :154, `gC5_relT` :161, `gC5_not_relC` :179,
    `gC5_posFwd` :360, `gC5_posInv` :369, `relT_not_dimension_selecting` :393.
  - TransitiveBody.lean: `isBoundaryState_of_extreme` :284, `extreme_of_isBoundaryState_of_transitive` :290,
    `not_boundaryTransitive_of_nonextreme_boundary` :301, `eq_qBall_of_boundaryTransitive` :457.
  - OrbitGeneration.lean: `BoundaryTransitive` :79, `not_boundaryTransitive_flow` :620.
  - KInfFoundations.lean: `ElementaryDrivability` :264, `CopyNatural` :284.
  - CompletionAction.lean: `OpDatum` :46, `AffineRespect` :58, `affineRespect_of_induced` :264, `Undoes` :325,
    `preservesBody_inducedEquiv` :352.
- **Unsourced premises**, named:
  - local tomography: the carrier `W d`, which is K2;
  - two identical balls with a common test axis `z`;
  - for the theorem routes: natural conditioning, i.e. single-valued conditioning with Cov over the control's
    reversible group, Rel and Post;
  - type-level availability of the target's NOT on the control copy;
  - for (b2): local `SO(d)` inside one closed connected dynamical group with a common joint state space, plus the
    unverified Krumm–Müller theorem;
  - for QB2: boundary purity (K∞-Geom's content) and the elementary scope.

## 6. Classification

| question | classification | the named clause / wall and the witness |
|---|---|---|
| **QB1(a)** conditioning, as stated (existential, consistent with the joint cone) | **COUNTEREXAMPLE** to "conditioning derives CtrlGate": it derives a strictly weaker gate, the frame and CI, hence `p_N ≤ 1`. The weak corner form with M₁ unrelated to Ñ is automatic and adds nothing | missing TR, the parity half of relC. Exact countermodel: gC5, nC5, z5 at d = 5 (COND exact; positivity, frame and ¬relC kernel) |
| QB1(a′) natural conditioning (single-valued; Cov, Rel, Post on the NOT group) with type-level availability of the NOT | **THEOREM ROUTE** [W + K]: NC ⇒ relC(N,N) ⇒ CtrlGate ⇒ d ∈ {1,3} (`dim_of_ctrlGate`) | its content is the coherence Cov∘Rel = Post (each pair satisfiable by gC5). QT-consistent with Cov over SO(3), not over O(3), and with Post on {I, N} for a lift of N squaring to I; Post over all target rotations is QT-incompatible. "Conditioning composes" is QT-incompatible (Klein group). Excludes d = 2 (`not_even_of_relC`), 5 and 7; includes the bit (cnot1) and the qubit (cnot); the bit is then excluded by DIM-1's Entangling clause (`three_of_ctrlGate`, `not_entangling_cnot1`) |
| **QB1(b)** continuous reversible interaction (one-parameter group, non-product), as stated | **COUNTEREXAMPLE** / strictly weaker: holds at every odd d ≥ 3 (J/K flow; G_π = gC5 at d = 5) | missing: local SO(d) transitivity in the same connected group. Witnesses W5, W7 exact. With that clause: **THEOREM ROUTE** to d = 3 via Krumm–Müller [L, unverified], bypassing the gate; at d = 3 CtrlGate exists [K `nativeGate_cnot`, `ctrlGate_of_nativeGate`] |
| **QB1(c)** role exchange under the NOT (Hadamard type) | **COUNTEREXAMPLE** / strictly weaker | gC5 has 8 exact role-exchange symmetries at d = 5. Missing TR. It excludes the classical bit (cnot1 has none). No strengthening found |
| QB1(c′) the other reading of (c): the gate acts on the NOT group as on the corner labels, `G(N⊗I)G⁻¹ = N⊗N`, `G(I⊗N)G⁻¹ = I⊗N` | **THEOREM ROUTE**, but a restatement: it is relC ∧ relT, with no separation from them | natural conditioning with pre-composition naturality on {I, N} implies it [W]: `Cond(z;I,N)(I⊗Ñ) = Cond(z;N,I) = (I⊗Ñ)Cond(z;I,N)` is relT. gC5 satisfies the relT half (kernel) and fails the relC half |
| **QB2** one principle yielding K∞-Act and K∞-Trans | **INDEPENDENT PREMISE** (boundary purity), with an **OPEN** wall at capacity two | continuous reversibility (MMAP) yields K∞-Act-type data and pure-state transitivity. It holds for every finite complex QT system and fails for the bit and the gbit (discrete groups). K∞-Trans = PureTrans ∧ BP [W+K]. Witnesses: the qutrit fails K∞-Trans for every family while satisfying CR; the Carathéodory orbitope (CR ✓, BP ✗, capacity ≥ 3). Drive kept separate: `not_boundaryTransitive_flow` (BP ✓, PureTrans ✗). Wall: whether CR forces BP at capacity two |
| **QB3** K∞-Copy | **INDEPENDENT PREMISE** of QB1's principles in token form; **THEOREM ROUTE** under natural conditioning with type-level availability | exact countermodel gC5 with N_A = diag(1,−1,1,−1,−1) ≠ nC5 (NB-1's C2N): frame, relT(nC5), P± (kernel), Rc(N_A,nC5), and token-level NC (exact), at d = 5. Under (b2) at d = 3 with SO(3), all z-flipping NOTs are conjugate by SO(2)_z, so type covariance is automatic [W] |

Converse tests per principle:

| principle | qubit QT (cnot) | classical bit (cnot1) | rebit d = 2 | boxworld | d = 5 | d = 7 |
|---|---|---|---|---|---|---|
| (a) COND + P± | ✓ [X] | ✓ [X] | ✗ (frame + P± unsatisfiable at d = 2: relt N2.3 [P], Lsig singularity re-checked [W]) | ✗ [L+W] | ✓ gC5 (not excluded) | ✓ J/K G_π (not excluded) |
| (a′) NC, type-level | ✓ [X + W] | ✓ [X] | ✗ [K `not_even_of_relC`] | ✗ | ✗ [K selector] | ✗ [K selector] |
| (b) one flow | ✓ [X] | ✗ (Aut of the interval is finite) | not examined at d = 2 | ✗ [L] | ✓ (not excluded) | ✓ (not excluded) |
| (b2) flow + local SO(d) | ✓ [X W3, written QT] | ✗ | ✗ [L] | ✗ [L] | ✗ [X W5 for J/K; L in general] | ✗ [X W7 for J/K; L in general] |
| (c) role exchange | ✓ [X] | ✗ [X] | not examined | ✗ (no gate) | ✓ gC5 (not excluded) | not examined |

Where (a) or (a′) admits the classical bit, DIM-1's Entangling clause excludes it: [K] `three_of_ctrlGate` for
(a′); [R] for (a), since `not_entangling_one_ctrl` (RelcSelectBlock.lean:725) reads only the frame (:733), which COND
gives.

**Not claimed.**
- No claim that OI supplies any of the named clauses; nothing here sources them.
- "Natural conditioning" is not derived from anything weaker. It is relC re-expressed as a coherence law, with
  separations and a converse.
- No conclusion is drawn about the balanced-NOT question.
- No conclusion is drawn about whether gC5 or the J/K flow satisfies DIM-1's `Entangling` clause in `maxCone`. The
  Bell-like image `diag(1,1,−1,0,0,1)` of `(e_x, z5)` under gC5 is not extreme there: adding ±E_{w₁w₁} stays in
  `maxCone` by a contraction argument ([W]; image and form [X] `b5_localwords` N1). Whether conditioning with
  Entangling excludes d = 5 is open.
- The literature rows are search-level summaries; theorem numbers and hypotheses are unverified against the sources.
