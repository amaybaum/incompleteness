# EQ4-P — running notes (design only; base `bcbc516f`, read-only at `scratchpad/eq/base/`)

Protocol: `scratchpad/eq4/PROTOCOL.md` (frozen; never edited here). Part: EQ4-P, nodes N1–N5, Priorities 1 and 2.
Nothing here is adopted, frozen or governed. No Lean toolchain: every Lean text is UNBUILT. Writes only inside
`scratchpad/eq4/P/`. Exact arithmetic for anything certified; floating point only in files named `*_float*`, with a
banner, never cited as evidence. No import from `eq3/` or `eqreview/`.

## N0. Integrity at start (2026-10-09 04:01 UTC)

- `.start_marker` written 2026-10-09T04:01:01Z (content = that timestamp).
- `cd scratchpad/eq/base && sha256sum -c --quiet ../base.manifest.sha256`: silent, exit 0.
- `/home/user/incompleteness`: `git status --porcelain` empty (0 lines); HEAD
  `bc3bf9bc846c138de5f5b45f386a75244da4f21f`.
- `scratchpad/eq4/P/` was empty at start (`eq4/F/` belongs to the other thread; not touched).
- Tools: Python 3.11.15, sympy 1.14.0 (small symbolic identities only), `fractions.Fraction` (own Gaussian-rational
  arithmetic for all operator work); numpy 2.4.6 / scipy 1.17.1 only for `_float` exploration.

Inputs read in full before any work: `eq4/PROTOCOL.md`; `eq3/P/RESULT.md`, `eq3/P/NOTES.md`; `eq3/PROTOCOL.md` (for the
owner's five-way outcome table, Amendment 2); `eqreview/EQ3-AUDIT.md`, `eqreview/EQ3-AUDIT-CHECKLIST.md`;
`eqreview/audit_eq3_n1.py`, `eqreview/audit_eq3_n2.py`; `eqreview/EQ2-SYNTHESIS.md`; `eqreview/eq4_precheck.py` and
`.out` (coordinator pre-checks, not evidence here). For the c = 1 witnesses I read (only) the header and output of
`eq2/A/a4c_twisted_selfduality.py` (definition of `F`, `G`); membership is re-derived here in own code.

Kernel conventions read at the base (paths under `verification/lean-mathlib/OIBridge/`; read, not built):
- CompositeDimension (CD): `W d` :97; `hom` :100; `homMap` :112; `prodState` :161; `pairVal` :164; `actT` :198;
  `actC` :201; `sgn` :741; `pc` :744; `pt` :751; `cnotFun` :758; `cnot` :775; `z3` :793; `xplus` :1213; `phiW` :1220;
  `cnot_prodState_xplus_z3` :1222.
- K2Guard (K2G): `reflY` :46; `CandidateCone` :95; `idW` :101; `chainW` :104; `cnot_idW` :110.
- EffectSpace: `sharpVec` :57. KInfFoundations (KF): `IsEffectOn` :116.
- CompositeInterface (CI): `PreComposite` :223 (`prod_mem` :227, `prodEff_effect` :228); `Composite` :243 (`lt` :245);
  `condA_mem` :431 (assumes `IsCompact ΩA`); `subset_maxBody` :467.

## N0.1 Productivity test (copied from the protocol before the walk; not edited afterwards)

A finding is a **gem** iff it is one of:
1. an exact certificate deciding Priority 1 at a stated instance;
2. a theorem route, every step checked, for a stated equivalence of E3 or for a closure of the wall;
3. an exact countermodel at a stated finite instance with `K₃ ≠ PSD₈`;
4. an exposed hidden assumption;
5. a classification of a candidate principle as disguised IE₂, or as strictly new, with the required proof and model.

Otherwise it is record-only. Results are stated for the instance actually used, never for "KT∞" in general unless
proved for all instances.

## N0.2 Decision rules for every script (rules, not expected numbers)

- R1 A script's header states its decision rule before its first run. A VERDICT line prints only when every check,
  control and countercontrol passed; otherwise `VERDICT NOT RENDERED`.
- R2 Linear (multilinear) identities are certified by exact evaluation on a full basis of matrix units (a linear map is
  determined by its values on a basis), or as exact symbolic identities (`expand(...) == 0`). Random exact instances
  are used only as cross-checks of identities proved in writing, and are labelled so. Signs by exact values; PSD by an
  exact Hermitian elimination (negative pivot or nonzero row at a zero pivot = not PSD). No `sympy.solve`.
- R3 Every favourable check gets a countercontrol that a wrong convention or a wrong object would fail.
- R4 Kernel conventions are parsed from the base files and compared with hand transcriptions (transcription
  control); the operator calculus is tied to the kernel tables by exact dictionary identities.
- R5 Harness errors are recorded; failed runs are kept as `.runN.*`; every exact script is replayed byte for byte at
  the end, with hashes recorded.

## N0.3 Plan (written before any script)

Depth-first, decisive node first:
1. N1 (Priority 1). Own library `eq4_lib.py` (Gaussian rationals, labelled n-qubit operators, conditionals,
   partial transposes, kernel transcription control). Then:
   - `p1_e1_triangle.py`: E1 exactly — the 3|3 Bell-link identities for all six matchings (states and effects), the
     written triangle argument's ingredients, the pigeonhole certificate (c = 0), the c = 1 analogue (twin links, the
     `B_tw` witnesses re-derived), the general-k link identities (k = 2, 3, 4).
   - Pressure point noticed while planning (to be checked, not assumed): the crossing calculus also acts on *mixed*
     triples (one token from each side). A five-token crossing with one Bell state and one Bell effect is a
     teleportation of one token, which would relate the cones of two triples sharing two tokens. If that holds,
     KT restricted to six tokens already relates `K₀₁₂` and `K₃₄₅` (protocol N1.2), without nine tokens.
     `p2_teleport.py` tests this exactly, aligned charts first, then general O(3) charts.
2. N2 (Priority 2): `p3_crossing_calculus.py` (E2: written proof + exact checks on 5- and 6-token crossings of every
   type; the one-empty-intersection remark), `p4_e3_directions.py` (each direction of E3 with its own witness),
   then the owner's distinction and the generation question (pair-network closure).
3. N3: reduce the wall with the derived calculus (what 5 and 6 tokens add), then exact sector computations.
4. N4 only if N3 does not close. N5 literature (cheap; egress may be blocked).

## N1 node log — Priority 1, the mixed configuration (BS*, BS)

### N1.1 E1 verified exactly (`p1_e1_triangle.py`, run 1: 26/26, `P1-E1-TRIANGLE-EXACT`)

One pre-run edit (a dead expression removed from K3; no run before it). Decision rule unchanged.

Exact facts (all on full bases of matrix units unless stated):
- K: transcription control; kernel `cnot` = Ad(CNOT) in the Pauli dictionary (16 unit tables); `cnot(prodState xplus
  z3) = phiW = coords(Φ⁺)`; `idW = coords(SWAP/2)`; one-qubit transpose = `homMap(reflY)`; `pairVal(sharpVec x,
  sharpVec y, ·)` = pairing with the operator `E_x ⊗ E_y`, `E_b = (1 + b·σ)/2`; the gate's dual image of the product
  effect `|+⟩⟨+| ⊗ |0⟩⟨0|` is `|Φ⁺⟩⟨Φ⁺|` (Bell effect). So the operator calculus is tied to the kernel tables.
- L (c = 0): on each six-token subfamily A∪B, B∪C, A∪C and for each of the six matchings π, the Bell-state
  conditional is `(1/8)·T(Π_π f)` and the Bell-effect value is `(1/8)·tr(x·T(Π_π y))`; T and Π_π preserve the trace
  pairing and commute. Countercontrols: matchings differ; T is not the identity.
- C (c = 1, twin links SWAP/2): conditional `(1/8)·Π_π f`, value `(1/8)·tr(x·Π_π y)`.
- P (pigeonhole, c = 0): W3 = ½ − GHZ ∈ BS* (Cauchy–Schwarz SOS identity, symbolic, plus GHZ's permutation symmetry);
  GHZ ∈ BS* (PSD); W3 ∉ BS (eigenvalue −½ on GHZ). (BS, BS) fails (I3) and (BS*, BS*) fails (II3), each at −1/16, for
  every matching; all 8 assignments of {BS, BS*} to three triples repeat a cone on a linked pair. Controls: biseparable
  and PSD substitutes give 1/32 and 1/8.
- T (c = 1): F, G ∈ B_tw* by an exact symbolic conditional SOS (block determinant `(|α|²−|β|²)²/4`), re-derived here;
  tr(FG) = −½; (B_tw*, B_tw*) fails (II) at −1/16, (B_tw, B_tw) fails (I) at −1/16. Control: W3 ∈ B_tw by an explicit
  six-term decomposition `W3 = Σ p_k PT_1(σ_k ⊗ ρ_k)` (own construction); tr(W3F) = ½, tr(W3G) = 5/2.
  Countercontrol: coherence 2 leaves B_tw* (−½).
- K' (general k = 1..4): Bell conditional `2^{-k} T(Π f)`, twin conditional `2^{-k} Π f`.

Written assembly (W), from L/C with KT on each six-token subfamily, closedness and full effects:
1. For each linked pair (X, Y) and every matching π: `K_X = T Π_π(K_Y*)` [(I3) from L1 + closedness; (II3) from L2].
2. Symmetry: `Π_π(K_Y*) = Π_σ(K_Y*)` for all π, σ, so `K_Y*` and hence `K_Y = (K_Y*)*` are invariant under all token
   permutations of Y (L3: permutations preserve the pairing); `K_X = TΠ(K_Y*)` is then symmetric too.
3. Triangle: `K_A = T(K_B*)`, `K_B = T(K_C*)` give `K_A = T((T K_C*)*) = K_C` (using `(TK)* = T(K*)`, `K** = K`); then
   `K_A = T(K_C*) = T(K_A*)` and `K_B = T(K_A*) = K_A`. All three coincide (up to relabeling) and `K = T(K*)`.
4. c = 1: the same with T replaced by the identity: `K = K*`.
5. General k: steps 1–4 are k-independent; three disjoint k-groups (3k tokens) force k-level uniformity, S_k symmetry
   and co-self-duality (c = 0) / self-duality (c = 1).
6. General charts: each link pair (a, b) induces `homMap(R_ab)` on its token (factorwise, as L1); `det R_ab = −1` iff
   the pair is Q3 in its token charts (p2 D1). With LU invariance of triple cones (settled, EQ3 six-copy) the induced
   triple map is `PT_{S_π} Π_π` with `S_π` = tokens whose link pair is Q3; with `τ = δε + c` (KT(4) on every
   four-token subfamily, settled) the per-token reflections ε (one-token transposes, p1 K3) turn every `S_π` into all
   tokens (c = 0) or none (c = 1). So arbitrary charts reduce to the aligned case. (Exact ingredients: p2 D1–D4.)

**Verdict N1.1: E1 CONFIRMED** (aligned and general charts, c = 0 and c = 1, general k), as a theorem route
[X + W]: exact link identities and membership certificates, written assembly.

### N1.2 Teleportation: the six-token family already decides it (`p2_teleport.py`, run 1: 14/14, `P2-TELEPORT-EXACT`)

One pre-run edit (D3 restructured so every determinant pattern gets a quaternion check; no run before it).

**Lemma T (one-token teleportation).** Tokens z, p, q, s, t. KT on the five-token family {z,p,q,s,t} with the two
bipartitions `zp|qst` and `zq|pst`; the Bell state of the standalone pair (z,q) (gate on a product state, a (2) step);
the Bell effect of the standalone pair (z,p) (dual gate image of a product effect, (2)); `y ∈ K_pst` and
`g ∈ K_qst*` arbitrary (prod_mem, prodEff_effect: (s) steps). Then
`0 ≤ tr[(Φ⁺_zp ⊗ g)(Φ⁺_zq ⊗ y)] = ¼·tr(g · y(p→q))` [X A1], so with closedness and full effects
`K_pst ⊆ K_qst` (renamed p→q); the reverse roles give `⊇` [X A2]. Twin links on both pairs: the same; one twin and one
Bell link: `PT_q` of the renamed cone [X A3]. A product link does not teleport [X A4].

Consequences, each exact in its ingredients:
- **Uniformity inside six tokens.** Steps 0→3 (z = 4), 1→4 (z = 5), 2→5 (z = 0), each inside a five-token subfamily
  of {0..5}, compose to the relabeling `y ↦ (1/64) y(0→3, 1→4, 2→5)` [X B1]: `K_012 = K_345` (relabeled).
- **(BS*, BS) excluded by KT restricted to six tokens.** GHZ ∈ BS* = K_012 is carried by steps 1–2 to GHZ on (3,4,2)
  ∈ K_342; the step-3 crossing with the effect W3 ∈ BS* = K_345* has value **−1/8** [X B2]. Same for c = 1:
  (B_tw*, B_tw) fails at −1/8 with G carried over and the effect F [X B3]. Controls [X B4].
- **Permutation symmetry inside five tokens.** In {0,1,2,3,4} with z = 4, the teleportations 0→3, 1→0, 3→1 compose to
  the swap (0 1), and 1→3, 2→1, 3→2 to (1 2) [X C]: `K_012` is S_3-invariant from KT on five tokens.
- **General charts.** With link identifications R1 (state, pair zq) and R2 (effect, pair zp) the moved token is
  transformed by `homMap(R1ᵀR2)` [X D2]; `det = det R1·det R2`; equal pair types give an explicit rational local
  unitary, mixed types a transpose up to a local unitary [X D3]; with `τ = δε + c`, the parity is `ε_p + ε_q` [X D4]:
  c cancels, and after the ε gauge every teleportation is a local unitary.
- Co-self-duality then needs only the 3|3 Bell-link instance KT(6; 012|345, 03|1425, 14|25) (p1 L1/L2):
  `K_012 = T(K_345*) = T(K_012*)` (relabeled).

Premises used, exposed: (i) one body per token set — the triple {0,1,2} is the same object in every family containing
it (KT's "each group's body is the body of the composite of its members"); (ii) closedness of the intermediate triples
K_312, K_342; (iii) their full `IsEffectOn` effect sets; (iv) the gate on the standalone link pairs (2). No uniform
composition, no (o) step.

Pressure test of this favourable branch: (a) the crossing is a genuine KT pairing (the two bipartitions of one
five-token body; products of states under one, products of effects under the other) — no new premise; (b) the
intermediate cones are unknown, and the lemma is applied to whatever they are; (c) the countercontrol A4 shows the
identity is not automatic; (d) the c = 1 analogue and the mixed links behave as the twist structure predicts.

**Verdict N1.2: GEM (productivity test item 1).** KT restricted to the six-token family {0..5} — in fact only the three
five-token instances KT(5; 40|312, 43|012), KT(5; 51|432, 54|132), KT(5; 02|534, 05|234) — excludes (BS*, BS) (−1/8),
and forces `K_012 = K_345` (relabeled). Uniformity at the triple level is derived at six tokens, not nine. The
coordinator's remark that an exclusion "would come through the four-token group cones" is not the route: it comes
through the cones of the mixed triples (one token moved at a time). Smallest instance for two disjoint triples: six
tokens (necessary, since two disjoint triples need six tokens). Hidden assumption exposed: the audit's statement that
(BS*, BS) "satisfies every family" held only for the fixed grouping 012|345 and its link groupings; the other subsets of
the same six tokens exclude it.

## N2 node log — Priority 2, the CNOT Choi lever

### N2.1 E2, the crossing-constraint calculus (`p3_crossing_calculus.py`, run 1: 10/10, `P3-CROSSING-CALCULUS-EXACT`)

No pre-run edit.

**Proof (W).** Family S = A ⊔ B = C ⊔ D, P = A∩C, Q = A∩D, R = B∩C, U = B∩D. KT on S makes `x ⊗ y` a state for
`x ∈ K_C`, `y ∈ K_D` (prod_mem on C|D) and `e ⊗ f` an effect for `e ∈ K_A*`, `f ∈ K_B*` (prodEff_effect on A|B; the
effect sets are the full `IsEffectOn` sets). So `0 ≤ tr[(e ⊗ f)(x ⊗ y)] = tr[e · Cond_A]` with
`Cond_A = tr_B[(f ⊗ 1_A)(x ⊗ y)]`. For a product `f = g_R ⊗ h_U`, `Cond_A = Λ_x(g) ⊗ Λ_y(h)` with
`Λ_x(g) = tr_R[(g ⊗ 1_P) x]` (an R→P map) and `Λ_y(h) = tr_U[(h ⊗ 1_Q) y]`; by linearity `Cond_A = (Λ_x ⊗ Λ_y)(f)` for
every f. Since this holds for all `e ∈ K_A*`, `Cond_A ∈ K_A** = K_A` (closedness). Hence
`(Λ_x ⊗ Λ_y)(K_B*) ⊆ K_A`. The Choi matrix of `Λ_x` is `Σ_ij |i⟩⟨j|_R ⊗ Λ_x(|i⟩⟨j|) = PT_R(x)` ("with transposes").
Exact: Choi(Λ_x) = PT_R(x) [E1]; the conditional equals the map built independently from the Choi matrix
`PT_R(x) ⊗ PT_U(y)` on all units, for crossing types (1,1,1,2) [5 tokens], (1,1,1,3), (1,1,2,2), (2,1,1,2), (1,2,1,2)
[6 tokens] [E2]; value identity [E3]; countercontrol: dropping the partial transposes changes the map.

**Coordinator's remark (one intersection empty), checked.** If Q = ∅ then A = P ⊆ C, D = U ⊆ B, and
`tr[(e⊗f)(x⊗y)] = tr[f · (cond_A(e; x) ⊗ y)]` [X M]. `cond_A(e; x)` is a state of R by C's coherence (C is a composite
of A|R; conditioning + closedness), and `cond_A(e; x) ⊗ y` is a state of B by B's coherence (R|U, prod_mem); so the
constraint follows from the subfamilies' coherence. **Confirmed** (written, exact identity).

**Uniform corollary, with the convention made exact.** With Bell links x between P and R (|P| = |R| = m) and
co-self-duality `K_B* = T(K_B)`, writing `f = T(g)`: `Cond_A = 2^{-m} (rename_{R→P} ⊗ Φ_y)(g)` where
`Φ_y = Λ_y ∘ T_U` has **Choi matrix y itself** (U first) [X U1, U2; cases (n,a,b) = (3,2,2), (4,1,2), (2,2,1),
(3,1,2)]. So `K_n ⊇ (id_{n−b} ⊗ Φ)(K_{n−b+a})` for every map Φ from a tokens to b tokens whose Choi matrix (input
first, in this convention) is a state of `K_{a+b}`. Twin form (c = 1, `K* = K`): the same with `Λ_y`, Choi `PT_U(y)`
[X U3]. The audit's lever is (n, a, b) = (3, 2, 2). Also exact: general-chart 3|3 links act factorwise by
`homMap(R_i)` [X G] (used in N1.1 item 6); teleportation for k = 2 and k = 4 [X T].

**Verdict N2.1: E2 CONFIRMED** (written proof + exact operator checks; the "transposes" are pinned:
Choi(Λ_x) = PT_R(x), Choi(Λ_y ∘ T) = y).

### N2.2 E3, one direction at a time (`p4_e3_directions.py`, run 2: 12/12, `P4-E3-DIRECTIONS-EXACT`)

Run 1 (kept as `p4_e3_directions.run1.{py,out,err}`): 11 checks passed, then a crash in D2 before any verdict
(harness error of mine: `1 / trw` with `trw` a Gaussian rational; the class has no `__rtruediv__`). Fixed to
`L.ONE / trw`; decision rule unchanged; run 2 12/12.

Setting: aligned c = 0, the uniform hierarchy derived in N1 (triples: six tokens; k-groups: 2k tokens),
co-self-duality `K_k = T(K_k*)` from the k|k Bell instance (2k tokens), closedness, full effects.

| direction | witness | instance used | evidence |
|---|---|---|---|
| (iv)⇒(ii) | the gate on (0,1) applied to `\|+⟩⟨+\| ⊗ Φ⁺` (∈ BS ⊆ K₃) gives `ψ = (\|000⟩+\|011⟩+\|101⟩+\|110⟩)/2`, Det ψ = 1/4 ≠ 0 | K₃ ⊇ BS (three tokens) + (iv) | [X IV2]; the native gate on two tokens of a triple = Ad(CNOT ⊗ 1) [X K1] |
| (ii)⇒(i) | orbit lemma: Det ψ ≠ 0 ⇒ ψ ∈ SLOCC·GHZ (own elementary proof: Det = discriminant of `det(sM₀ + tM₁)` [X II1a]; Det = 0 on cut-products [X II1b]; constructive A, B, C from the two roots [W + X II1c, 3 instances]); density (Det a nonzero polynomial); SLOCC invariance (re-derived at five tokens: filter links Ad(A), A arbitrary, even singular [X II1d]); closedness ⇒ PSD₈ ⊆ K₃; co-self-duality ⇒ K₃ ⊆ T(PSD₈*) = PSD₈ | five tokens (filters), six tokens (co-self-duality) | [W + X]; no Dür–Vidal–Cirac citation needed for this direction |
| (i)⇒(iv) | PSD₈ is invariant under unitary conjugation | — | [W]; control [X I4] |
| (iii)⇒(iv) | six-token crossing (012\|345, 03\|1245): Bell link on (0,3), CNOT Choi state C on (1,2,4,5): `cond[T(g)] = ½ (rename ⊗ Ad CNOT)(g)`; with `K_B* = T(K_B)`: `Ad(1 ⊗ CNOT) K₃ ⊆ K₃` | six tokens (+ S₄-symmetry of K₄ from six-token teleportation, for the arrangement of C) | [X III4]; countercontrol: identity Choi gives the rename only |
| (i)⇒(iii) | seven-token crossing (0123\|456, 0145\|236): Bell links (0,4), (1,5), copy Choi `2·GHZ` on (6,2,3); with g = ψ₃ (PSD, Det = 4): the conditional is ¼·C on (0,1,2,3) | seven tokens | [X I3]; equals the coordinator's `(CNOT₁₂ ⊗ 1)(Ω₁₄ ⊗ Ω₂₅)` after relabelling |
| (iii) state ⟺ effect | `T(C) = C`; under `K₄ = T(K₄*)`: `C ∈ K₄* ⟺ C ∈ K₄` | eight tokens (4\|4 Bell instance) | [X D1] + [W] |

**Verdict N2.2: E3 CONFIRMED** as stated, at the instance "KT on families of up to seven tokens" for the state form
of (iii) (eight for the effect form), with every direction separately witnessed (§A.34). Classification:
theorem route [X + W], nothing kernel-checked.

### N2.3 The owner's distinction (written; exact ingredients p4 D1–D2)

- **Definable.** C ⪰ 0, C² = 4C, T(C) = C [X D1]. So `ρ ↦ tr(Cρ)/4 ∈ [0, 1]` for every normalized PSD ρ: the
  functional is `IsEffectOn` on **every four-token body contained in PSD₁₆**. That is all its "definability" says.
- **Not automatic.** Whether it is an effect of a given body depends on the body: the normalized operator
  `w ∝ 1/16 − C/32` is nonnegative on every product across every 2|2 and 1|3 cut of four qubits (largest Schmidt
  weight of `c/2` is ½ on each cut) and has `tr(Cw) = −2/7` [X D2]; any body containing such a w has C outside its
  effect set.
- **Availability on the actual composite.** Under co-self-duality at k = 4, `K₄* = T(K₄)` and `T(C) = C`, so
  `C ∈ K₄* ⟺ C ∈ K₄` ⟺ (E3) IE₂. Hence the CNOT Choi effect's availability on the actual four-token composite is
  **equivalent to IE₂**; it cannot derive IE₂ unless sourced independently of the hierarchy.

### N2.4 Generation (`p5_generation.py`, run 1: 5/5, `P5-GENERATION-EXACT`)

One pre-run edit (countercontrol moved to crossing type (1,2,1,2); the drafted one was vacuous by design: a PN link
carries one token). Decision rule otherwise unchanged.

**Extended no-generation lemma (W, exact ingredients).** Let `PN_n` be the closed convex cone generated by tensor
products of PSD operators over partitions of the n tokens into blocks of size ≤ 2. PN is closed under: products;
transposition; relabeling; local CP maps; closure; and **conditioning in every crossing of PN states on PN effects,
and of PN effects on PN states** — the contraction graph has maximal degree 2, so its components are paths and cycles
with at most two open tokens per path, and each component is a conditional of PSD on PSD [X C, five crossing types,
including 2|4 crossings where the effect sits on a four-token group]. A derivation from pair-level data by (s) and (2)
steps, whose effects on any group (of any size) are those it has already generated — with co-self-duality, effects
= transposes of generated states — therefore stays in PN. C ∉ PN₄ (Schmidt ranks [2,4,4,2,2,2,2] across all 2|2 and
1|3 cuts; C rank one) and GHZ, ψ₃ ∉ PN₃ = BS [X N1, N2]. Countercontrol: a GHZ-class input escapes PN [X C'].

**Circularity.** Conditioning on an effect E of a larger group G is licensed only by `E ∈ K_G*`. The only effects a
derivation can certify are products of certified effects and (co-self-duality) transposes of certified states; upper
bounds `K_G ⊆ Z` give `Z* ⊆ K_G*` only with Z built from certified effects, i.e. `Z* ⊆ PN`. So using the CNOT Choi
effect on (1,4,2,5) requires `C ∈ K₄* = T(K₄)`, i.e. (iii) itself. **Verdict N2.4: no KT instance of any size forces
(iii) (or (ii)) by generation from (s) and (2) steps; such generation is circular.** What KT can still do is
*exclude*: a hypothetical cone is refuted when its own full dual (not a certified effect set) produces a
contradiction — that is how BS, B_tw, M_odd and (BS*, BS) fall. Any route to (iii) must be of that kind: a
classification of the admissible fixed points (N3).

## N3 node log — the reduced wall

With N1 (uniformity, symmetry and co-self-duality derived at six tokens) and N2 (E3; no generation), the wall is:
does KT∞ (with the pair premises, closedness, full effects) admit a hierarchy (K_n) with K₃ ≠ PSD₈? Equivalently
(E3) with no GHZ-class state in K₃. Every K₃ must be closed, convex, S₃-symmetric, local-CP-invariant (five tokens,
p4 II1d), co-self-dual (six tokens), with BS ⊆ K₃ ⊆ BS*.

### N3.1 Exploration x1 (`x1_networks_float.py`, FLOATING POINT, not evidence)

One pre-run edit (two einsum index orders fixed, a dead line removed; no run before it). 12 BFGS starts per network,
general PSD links, nodes in the SLOCC orbit of W3 (states and, as T(K₃), effects). Minima of the normalized values:
theta 4.5e-18, ring 1.5e-17, K4 split 0 8.1e-18, split 1 1.2e-18; controls (GHZ in place of W3) 1.6e-17, 1.6e-16.
No violation lead. (Explained exactly in N3.4.)

### N3.2 An exact countermodel at five tokens (`p6_five_token_model.py`, run 1: 7/7, `P6-FIVE-TOKEN-MODEL-EXACT`)

No pre-run edit. **The pair-network hierarchy** `K_F = PN_F` (|F| ≤ 5): K₂ = PSD₄, **K₃ = BS ≠ PSD₈**, K₄ = PN₄,
K₅ = PN₅, full duals as effect sets, satisfies **every KT constraint among families of at most five tokens**, with the
gate premise. Written proof: at ≤ 5 tokens every crossing has parts of size ≤ 3 and is of type (1,1,1,2); the
conditional of a BS state through a pair state and a pair effect is a local CP image (Choi PSD) [X F1], which keeps
BS; every pairing of products with product effects (full duals) reduces to such a conditional or to a QM pair-level
pairing [X F2, N: 60 + 30 exact instances with non-PN dual elements W3, Ad(k)W3, and the PN₄* witness w]. It fails at
six tokens (−1/16) [X S]. **Verdict N3.2: GEM (productivity item 3), as a lower bound:** KT on families of ≤ 5 tokens
does not force K₃ = PSD₈ (nor exclude BS); any closure needs six tokens or more. It decides nothing at six tokens.

### N3.3 What six tokens add (`p7_wall_reduction.py`, run 1: 7/7, `P7-WALL-REDUCTION-EXACT`)

Pre-run edits (no run before them): the ring contractions use a partial trace of a product over P only (not a full
conditional); the slice orthogonality pair fixed to satisfy su = tv/2; an unused expression removed.

Reduction (W, with exact identities): at six tokens the constraints on K₃ are (i) co-self-duality (3|3 Bell links);
(ii) local-CP invariance (five tokens); (iii) the 3|3 × 3|3 ring — **implied by (ii)**: ring = tr(M·N) with M, N the
two-token contractions [X R1], and five tokens confine both to the twin cone, which is self-dual [X R2, R3];
(iv) the existence of K₄. With K₄ taken minimal (generated by glued states, products), every crossing involving K₄
reduces to (ii), to theta-type pairings, or to the **K₄ ("glue") network** — glued states against glued effects with
crossing splits; the Choi-closure crossing (1,2,1,2) is the same network [X G]. Exact Bell-link values for W3:
theta 1/4, ring 7/4, K₄ splits 5/16, 5/16 [X W]. Stabilizer slice of the GHZ-diagonal sector (record only): the
averaged slice admits a non-orthant self-dual cone (a rotated Lorentz cone) containing negative-defect points [X S],
so slice tests cannot exclude.

Sector bookkeeping (W): in coordinates (P_b, C_b) per GHZ fibre b, the sector symmetry group is S₄ on fibres ⋉ even
sign changes of C (the D₄ Weyl group on C); the diagonal-filter semigroup (fibre population boosts, uniform
dephasing) and single-token filters add nothing beyond G-invariance and convexity (boosts add PSD populations,
dephasing is a convex combination with the s-flip). So the sector conditions are: a G-invariant self-dual cone between
S = cone{e_j + e_k} and S*.

### N3.4 Twisted network positivity and the maximality certificate (`p8_coloring.py`, run 1: 10/10, `P8-COLORING-EXACT`)

No pre-run edit. Let `Z = {X : PT₁(X), PT₂(X), PT₃(X) ⪰ 0}` (then PT_S(X) ⪰ 0 for all |S| ∈ {1,2}; T(Z) = Z; Z is
closed under local filters [X Z2]). W3 ∈ Z (W3 itself not PSD; PSD pair marginals) [X Z1].

**Coloring lemma (W, exact instances).** In any closed KT network — each token shared by one state node and one
effect node — whose nodes are one-token PSD operators, two-token PSD operators and elements of Z, the value is ≥ 0.
Proof: choose a token set X meeting each two-token node in 0 or 2 tokens and each Z node in 1 or 2 tokens; contract
two-token nodes to edges; an edge 2-colouring of the resulting multigraph with no monochromatic degree-3 vertex exists
(add a vertex adjacent to every odd-degree vertex, take an Euler circuit starting there, colour alternately: each
original degree-3 vertex is passed twice through alternating pairs, so it sees both colours among its own three edges).
Applying PT_X to every node preserves the value (each token's transpose appears on its state and its effect) and makes
every node PSD; a pairing of PSD tensor products is ≥ 0. Exact instances: colourings found and positivity certified on
theta (Bell and random PSD links), ring, both K₄ splits and the nine-token 3×3 "Latin square" network [X C1].
Countercontrol: GHZ (a PSD triple, PSD only under T^0 or T) against W3 admits no colouring and gives −1/16 [X C2].

Consequences:
- **No finite network constraint of KT** — of any size, built from single, pair and triple nodes — **can exclude a
  Z-type element such as W3.** This explains x1 and the exact positive values (13/8 for the 3×3 Latin square, checked
  separately in exploration).
- **Maximality forces K₃ out of cone(BS ∪ Z)** [X M]: ν = I − 2GHZ₊ + 4GHZ₋ (λ = (−1,5,1,…,1)) lies in BS*
  (ν − 4GHZ₋ = 2W3) [M1], pairs nonnegatively with all of Z (twirl, then
  `2⟨ν,z⟩ = 4P₀₀ + 2Σ_{b≠00}(P_b − C₀₀)` on Z^GD, symbolic) [M2], hence ν ∈ T(cone(BS∪Z)*); and
  ⟨ν, Zν⟩ = −4 for the Pauli Z on one token [M3]. So a co-self-dual K₃ ⊆ cone(BS ∪ Z) would contain ν and Zν and
  violate its own self-positivity. Every co-self-dual K₃ — quantum or not — contains elements outside cone(BS ∪ Z).
  In QM those are the GHZ-class (and other NPT) states; in a non-quantum completion they would be GHZ-free elements
  such as W-class states or "rigid" non-PSD elements like κ = ½ + |000⟩⟨111| + h.c. (in BS*, PSD under no partial
  transpose, ⟨κ, ν⟩ = −1) [X P]. Exploration (exact, Bell links): κ with W3 gives theta 1/16, K₄ values 11/32–11/16,
  Latin 25/8–43/16 — all positive.

**Verdict N3.4: NEW (gem, item 4: exposed structure).** KT's discriminating power against Z-type candidates lies
entirely in the maximality clause (co-self-duality, i.e. the full-effect quantifier, at each level), never in a finite
network inequality of triple-, pair- and single-token nodes. The wall is the existence of a maximal (co-self-dual)
completion that leaves cone(BS ∪ Z) through GHZ-free elements while staying network-positive at every level. QM is one
such completion (through GHZ-class states). No other was constructed; none was excluded.

### N3.5 c = 1

The c = 1 hull B_tw contains W3 ∈ Z [p1 T5]; twin pair nodes need an odd transpose count, and the twisted-colouring
version of the lemma applies to pair networks (cycles alternate state and effect nodes, so have even length). B_tw is
self-positive and not self-dual [p1 T2]; any c = 1 K₃ is a self-dual completion strictly between B_tw and B_tw*. Not
decided: no c = 1 completion was constructed and no obstruction was found. **c = 1 is not excluded by any instance
tested.**

### N3.6 Fixed point (§A.31)

Passes: N1.1 (CONFIRMING E1), N1.2 (NEW: six-token teleportation), N2.1–N2.3 (CONFIRMING E2/E3, with the convention
made exact), N2.4 (NEW: extended no-generation, circularity), N3.2 (NEW-borderline: five-token countermodel, a lower
bound), N3.3 (ELABORATING: six-token reduction), N3.4 (NEW: colouring lemma + maximality certificate), x1/x2 and the
κ explorations (no NEW finding). Two consecutive passes without a NEW finding; the protocol's 3–4 not reached. N3 does
not close: **OPEN**. N4 is entered.

## N4 node log — candidate missing principles (entered because N3 did not close)

P = KT∞ (one body per token set; COMP-1 on every bipartition), the transported pair premises (closed admissible pair
cones, native gate and inverse on standalone pairs, N-CLASS in general charts), closedness, full `IsEffectOn` effect
sets. C = IE₂ for the native gate.

**A common fact for (c).** P ∧ IE₂ ⇒ K_n = PSD_n for every n (W): (iv) ⇒ (ii) ⇒ (i) at n = 3 (E3, six tokens);
(i) ⇒ (iii) (seven tokens); E2 with a = b = 2 then makes every K_n invariant under the gate on any two tokens (2n
tokens); with the local unitaries (five-token filters) the gate and locals generate a dense subgroup of PU(2ⁿ) (EQ2's
generation result [X instances, W general, L Barenco]); closedness puts every pure state in K_n; co-self-duality at 2n
tokens gives K_n = PSD_n. QM satisfies each candidate below, so **P ∧ IE₂ ⇒ A holds for all three** (no model of
P ∧ IE₂ ∧ ¬A exists for any of them: none is strictly stronger than IE₂ relative to P).

### N4.1 Choi availability of the native gate (statement (iii))

- (a) State-level in form (a state of the four-token composite); operation content (the gate's Choi state).
- (b) P ∧ A ⇒ IE₂: proved [X p4 III4 + W] (six tokens).
- (c) P ∧ IE₂ ⇒ A: proved [p4 IV2, II1, I3 + W] (seven tokens).
- **Classification: IE₂ in disguise relative to P** (both directions, each separately witnessed). As E3 predicted.

### N4.2 Purification, "pure" = extreme ray (`p9_purification.py`, run 1: 6/6, `P9-PURIFICATION-EXACT`)

No pre-run edit. Candidate Pur₁: every state of a two-token composite is the marginal of an extreme ray of a
three-token composite. (Full Pur: every state of every K_n has a purification in some K_{n+m}.)
- (a) State-level.
- **Support lemma (W, exact ingredients S1–S4).** If w ∈ BS* and tr₃ w = D/2 (D = |00⟩⟨00| + |11⟩⟨11|, the
  classically correlated pair state), then w is supported on E = span{|00⟩,|11⟩} ⊗ C² and PSD there. Proof in the
  probe header: zero diagonals on |01·⟩, |10·⟩ from block positivity, rows through them vanish (block positivity across
  each cut plus polarization [X S1]), and PSD on E because (|0⟩+|1⟩) ⊗ (|0⟩|u⟩+|1⟩|w⟩) = v + (terms outside E)
  [X S2]. **So non-PSD extreme rays cannot purify D/2 within one extra token** (the protocol's check: they do not break
  it). Countercontrol: W3 ∈ BS* has entries outside E (its marginal is not ∝ D) [X S4].
- Rank-one purifications of D/2 within one token are GHZ-class: ψ = |00⟩|u⟩ + |11⟩|w⟩ with |u| = |w|, u ⊥ w;
  Det ψ = (u₀w₁ − u₁w₀)² ≠ 0 [X S3] ⇒ (ii) ⇒ IE₂ (E3).
- (b) P ∧ Pur₁ ⇒ IE₂ **unless** an admissible K₃ ≠ PSD₈ has a mixed (rank ≥ 2) PSD extreme ray on E with logical
  marginal ½·1. Such operators exist (ω = ½GHZ + ½(D/2 ⊗ 1/2): PSD, rank 4 on E, marginal D/2, not biseparable,
  NPT across L|3 [X R]); whether one can be an extreme ray of a KT-consistent K₃ is the wall again. **(b): OPEN,
  reduced to that question.**
- (c) holds (common fact).
- **Classification: implied by IE₂ relative to P; sufficiency open (reduced). Not shown to be a new principle, not
  shown to be IE₂ in disguise.**

### N4.3 Transitivity of reversible dynamics on the pure states of composites

- (a) Operation-level.
- Reading 1 (dynamics = the available reversible operations, acting on composites): the premise asserts operations on
  parts of larger composites — the (o) tag — so as a premise it reintroduces idle extension (circular relative to the
  question). (c) holds (common fact).
- Reading 2 (dynamics = the linear automorphism group of the cone K_n, a geometric property): (b) OPEN. For a
  Z-type or κ-type completion transitivity would need automorphisms mapping product extreme rays to non-PSD extreme
  rays; nothing here excludes or constructs them.
- **Classification: in reading 1, the extension principle reintroduced (o-type); in reading 2, implied by IE₂ relative
  to P, sufficiency open.**

### N4.4 Summary for the owner's question "which principle is missing"

- Choi availability: IE₂ restated (proved both ways).
- Purification and transitivity: necessary relative to P in the owner's sense (P ∧ IE₂ ⇒ A, via full QM), sufficiency
  not established; purification's sufficiency reduces to excluding mixed GHZ-free extreme rays on E.
- What would have to be added is located by N3.4: a principle that selects the maximal completion through GHZ-class
  states rather than through GHZ-free elements. No candidate tested here was shown to do that without being IE₂ in
  disguise.

Side fact recorded (W + exact reasoning, not load-bearing): the GHZ-diagonal twirl of BS is exactly
S = cone{e_j + e_k} — "⊆" from the Cauchy–Schwarz bound (p1 P1) applied to every GHZ-basis state (all LU-equivalent);
"⊇" because e_{s,b} + e_{s,b'} is itself biseparable, e.g. GHZ₊,₀₀ + GHZ₊,₀₁ = Φ⁺₁₂ ⊗ |+⟩⟨+| + Φ⁻₁₂ ⊗ |−⟩⟨−|, and
same-fibre pairs are twirls of products. So the sector bound S* does not depend on the Gühne–Seevinck citation.

## N5 node log — literature (cheap; egress)

`WebFetch https://arxiv.org/abs/1006.4651` failed with `getaddrinfo ENOTFOUND arxiv.org` (not routed around). The
search tool returned summaries only. **Everything below is [L, unverified]** (not read at the source):
- Gühne–Seevinck, NJP 12, 053002 (2010), arXiv 0905.1349: criteria for genuine multiparticle entanglement, necessary
  and sufficient for GHZ states mixed with white noise; GHZ-fidelity > ½ certifies genuine entanglement of GHZ-diagonal
  states (the summary's own wording flagged this as not confirmed). Not load-bearing here (own Cauchy–Schwarz proof).
- Dür–Vidal–Cirac, PRA 62, 062314 (2000), quant-ph/0005115: two SLOCC classes of genuine three-qubit entanglement,
  GHZ and W; GHZ-type = two product terms. Consistent with the own orbit lemma (p4 II1), which makes (ii)⇒(i)
  independent of this citation.
- Chiribella–D'Ariano–Perinotti, PRA 81, 062348 (2010), arXiv 0908.1583: purification unique up to reversible maps on
  the purifying system; every process realizable reversibly; a Choi-type isomorphism; uses local discriminability and
  causality. Their purification includes uniqueness and builds parallel composition into the framework.
- Barnum–Wilce, arXiv 1202.4513: Jordan-algebraic systems + locally tomographic composites + one qubit ⇒ complex QM
  with superselection, "under natural constraints". Barnum–Graydon–Wilce, Quantum 4, 359 (2020): EJA composites
  without local tomography; InvQM. These presuppose Jordan (homogeneous self-dual) systems, i.e. homogeneity of the
  composite cones, which KT does not supply (N3).
- Müller–Ududec, PRL 108, 130401 (2012), arXiv 1110.3516: bit symmetry (an operation-level reversibility postulate)
  forces self-duality.
- A search for tripartite composites with quantum bipartite subsystems returned no source addressing the three-party
  wall (summaries only; this does not establish that none exists).

Bearing: the known reconstructions close the gap with operation-level or homogeneity postulates (reversible
transitivity, bit symmetry, purification with uniqueness, Jordan structure). N3.4 locates where such a postulate would
have to act: on the choice of the maximal completion.

## Addenda after the N5 entry (appended in order; earlier entries are not edited)

### N3.5a c = 1 maximality certificate (`p10_c1_maximality.py`, run 1: 5/5, `P10-C1-MAXIMALITY-EXACT`)

No pre-run edit. The c = 1 witnesses F, G (p1 T1) are GHZ-diagonal with fibre coordinates F: (P, C) = (0, 2) on
fibre 00 and (1, 0) on the other fibres, G: (0, −2) and (1, 0) [X F1]; on Z^GD, 2⟨F, z⟩ = (P₀₁ + C₀₀) + (P₁₀ + C₀₀)
+ P₁₁ and 2⟨G, z⟩ = (P₀₁ − C₀₀) + (P₁₀ − C₀₀) + P₁₁, nonnegative combinations of the Z^GD inequalities [X F2, symbolic];
tr(FG) = −½ [X F3]; control W3 ∈ Z, tr(W3F) = ½, tr(W3G) = 5/2 [X F4]. With p1 (F, G ∈ B_tw*): F, G ∈
cone(B_tw ∪ Z)*, so a Euclidean self-dual K₃ ⊆ cone(B_tw ∪ Z) would contain F and G and violate tr(FG) ≥ 0. **Every
c = 1 K₃ leaves cone(B_tw ∪ Z)**, the c = 1 analogue of N3.4's ν certificate. c = 1 remains not decided.

### N3.1a Exploration x2 (`x2_kappa_float.py`, FLOATING POINT, not evidence) — completed

Nodes: SLOCC images of W3 or of κ (keyed to the sign of the first parameter of each node; the script's own comment
records that BFGS can cross 0, so a start is not a clean κ-only search, but every evaluated configuration is a valid
candidate configuration). 16 starts per network. Minima of the normalized values: theta 1.6e-18, ring 4.8e-18,
K4 split 0 −2.0e-20, K4 split 1 −1.1e-18. The two negative minima are at round-off level (normalized values of order
1); no lead. Harness note: the docstring carries one stray line copied from x1 (cosmetic). Hashes in N9.

### N9.0 Replay of p1–p10 (`run_all.py`, first run)

`VERDICT RUN-ALL-OK`: every probe exit 0, stderr empty, stdout byte-identical to the recorded `.out` (fresh hash
seed per run). Script / recorded = replay (sha256, first 16 hex): p1 8e7d701fc4b5ea3f / 14ba9e6cfab7924d; p2
ca6ec9111fdddf31 / 658c3c3bf3b6bc4e; p3 2250f6fb65113148 / 650e2945f0678ac5; p4 bfdb1c1f8624f018 / 37c59c5366bb2747;
p5 cb73c052ba0e1994 / bbf6fcbf20f0acfa; p6 2983706025fe7966 / 7c563f65161a7cf0; p7 da018fbebd67a5f6 / a1f7d3242234c2b9;
p8 ad1c3a6223febb4f / 68f03717d57ff60f; p9 39e26888d1b15936 / d6214a8c255207ea; p10 ce76aaf573f3a918 / 6b332a3197881cc1;
library cc2c6aca94007ac8. (A second replay including p11+ is recorded in N9.)

### N3.7 The GHZ-diagonal sector problem, decided (depth-first continuation of N3; entered because N3 was open)

**Correction to N3.3's sector bookkeeping.** N3.3 lists "a G-invariant self-dual cone between S and S*" as *the*
sector conditions. That list is a set of necessary conditions; the claim that filters add nothing was checked for
single-token filters and diagonal product filters only, not for general product filters A ⊗ B ⊗ C (the twirl does
not factor through them). Single-token filters are now certified exactly (p11 F); general product filters are tested
below for the specific cone K_A (x9).

**Reduction (W; exact ingredients p11).** For an admissible K₃ (closed, convex, LU-invariant and S₃-symmetric from
five tokens, co-self-dual from six, BS ⊆ K₃): (1) the twirl over the GHZ stabilizer group ⟨XXX, ZZ1, 1ZZ⟩ is the
pinching in the GHZ basis [X H1], and these are local unitaries, so twirl(K₃) = K₃ ∩ GD; (2) T fixes GD pointwise
[X H3], and the twirl is HS-self-adjoint, so K₃ ∩ GD is self-dual for the trace pairing inside GD; (3) the group
generated by Z₁, X₁, X₂, X₃, S₁S₂, SWAP₁₂, SWAP₂₃ permutes the GHZ projectors and equals G = S₄ ⋉ (even
within-fibre swaps), order 192 [X H2], so K₃ ∩ GD is G-invariant; (4) twirl(BS) = S = cone{e_j + e_k}: "⊇" from
[X S1] (a product state and the biseparable identity P₀ + P₂ = Φ⁺ ⊗ |+⟩⟨+| + Φ⁻ ⊗ |−⟩⟨−|, transported by G, which has
two orbits on pairs), "⊆" from p1 P1 (tr(bP₀) ≤ tr(b)/2 on BS) transported by G; hence S ⊆ K₃ ∩ GD ⊆ S*;
(5) single-token filters act on GD as c₁I + c_sΣ + c_pΠ + c_psΠΣ with nonnegative coefficients and Σ, Π ∈ G
[X F]. **Sector problem SP:** G-invariant K = K* with S ⊆ K ⊆ S* in R⁸. If the orthant were its only solution, then
GHZ₊ ∈ K₃ and E3 ((ii) ⇒ (i)) would give K₃ = PSD₈: closure at six tokens. Conversely a non-orthant solution shows
that no argument using only these sector conditions can close the wall.

**Exploration (x3–x8; exact integer arithmetic, but searches: leads only).**
- x3 (`x3_sector_search.py`, sha 5b487f04a24a1ee8, out 8cde8d761f48f259): greedy orbit completion from S ∪ G·κ by
  extreme rays of K*; controls (orthant self-dual; S* not self-positive) correct; stuck after adding W3.
- x4 (`x4_sector_dfs.py`): depth-first over extreme-ray orbit choices from S, κ, W3; from S it finds the orthant
  (control) and every other branch is STUCK. Not evidence of uniqueness: only extreme rays were tried.
- x5 (`x5_sector_greedy.py`, one pre-run edit: a dead statement removed): non-extreme candidates z + c·w; from W3 it
  entered a non-terminating regress (added rays (−5,5⁶,9), (−9,9⁶,25), (−35,37⁶,115), (−139,141⁶,427),
  (−555,557⁶,1675), approaching (−1,1⁶,3)); stopped by hand (`pkill`) after step 5, so its `.err` has no exit line.
- x6 (`x6_sector_family.py`): a two-parameter family (face parameters m_t, m_s); never self-dual on the grid.
- x7 (`x7_filter_orbit_float.py`, FLOAT): for ρ(β, z) = −P₀ + βP₁ + z(rest), min over local m of
  tr(ρ Ad(m) ρ) is ≈ 0 at β = 3z² and positive inside: the filter-orbit condition coincides with the sector
  condition β ≤ 3z² on these elements. No lead.
- x8 (`x8_sector_limit.py`, x4 with new roots W3 + ω₃, κ + ω₃, ω₃ = (−1,1⁶,3) the x5 limit ray): **FOUND two
  self-dual cones**: K_A = cone(S ∪ G·W3 ∪ G·κ ∪ G·ω₃) and K_B = cone(S ∪ G·κ ∪ G·ω₃ ∪ G·(1⁷,9)).

**Certificate (`p12_sector_selfdual.py`, run 1: 5/5, `P12-SECTOR-SELFDUAL-EXACT`; no pre-run edit).**
K_A = cone{e_j + e_k (j ≠ k), m_j = 1 − 2e_j, n_jp = 1 − 2e_j + 2e_p (p ≠ j)} (92 generators; as operators
P_j + P_k, I − 2P_j = 2·LU(W3), I − 2P_j + 2P_p; n₀₁ = 2κ′, κ′ = ½ + P₁ − P₀ = G-image of κ). Written proof of
K_A = K_A* in the probe header: pairwise nonnegativity (⟨n_jp, n_j′p′⟩ = 8 + 4(δ − δ − δ + δ) ≥ 0, the bound 8 being
the dimension) and an explicit decomposition of every x ∈ K_A* (x ≥ 0 ⇒ x ∈ S; x_q = −1 ⇒ x = m_q + z or
x = (1 − d/2)m_q + (d/2)n_qm + (z − d e_m) with d ∈ (0, 2]). Exact checks: S₈-invariance and pairwise ≥ 0 [A1];
exact double description in two constraint orders returns exactly the 92 generators, each in K_A* with a tight set of
rank 7, orthant control and S* countercontrol [A2]; the written decomposition reproduces 300 random exact points of
K_A* (150 with a negative entry) with nonnegative coefficients [A3]; K_A ∩ R⁸₊ = S, GHZ₊ ∉ K_A, operator tie-in of
W3 and κ′ [A4].

**Verdict N3.7: NEW (gem, item 4 — a closure route ruled out, with an exact model).** SP has a non-orthant solution:
K_A is a self-dual, S₈-invariant (so G-invariant) polyhedral cone with S ⊆ K_A ⊆ S*, containing W3 and κ, whose PSD
part is exactly S = twirl(BS) — a GHZ-free sector. So the GHZ-diagonal twirl together with LU/permutation symmetry,
co-self-duality and single-token filters cannot force GHZ ∈ K₃. Any closure at six tokens must use information that
the GHZ-diagonal twirl discards (general product filters, the full 64-dimensional co-self-duality, K₄ and the
crossing constraints). Scope: this is a model of the sector conditions only, not of KT at six tokens; it is not a
countermodel to IE₂. K_B (exploration only, not certified) is a second solution whose PSD part contains I + 8P_j.

**Pressure tests of K_A beyond the sector conditions (explorations; leads only, none found).**
- x9 (`x9_KA_filters_float.py`, FLOAT): if K_A were the GHZ-diagonal section of an admissible K₃, every local-filter
  image of a generator would lie in K₃, and co-self-duality (T fixes GD) would need tr(W′ Ad(k) W) ≥ 0 for all
  generators W, W′ and all local k (this is also the sector filter condition, since the pinching is self-adjoint).
  Minimum of the normalized value over 6 BFGS starts per (generator, representative) pair: −2.4e-17 for K_A,
  −4.3e-17 for K_B (round-off; no lead).
- x10 (`x10_e2_contraction.py`, exact, sampled): E2 case (n, a, b) = (2, 2, 1) (a five-token crossing plus
  co-self-duality) requires M(x, y) = tr_U[(PT_U(x) ⊗ 1_Q)(1_R ⊗ y)] ⪰ 0 for x, y ∈ K₃. All 92² generator pairs
  and 128 random exact filter-image pairs give PSD M. Controls: PSD pairs give PSD M; dropping PT_U gives a
  non-PSD M for some PSD pair.
- x11 (`x11_KA_networks.py`, exact, sampled): Bell-link ring (400 + 400 mixed), K₄ both splits (150 each), 3×3
  Latin square (60), filtered ring and K₄ (60 each), nodes drawn from K_A's generators: all values ≥ 0 (minima
  24, 15/2, 198 for unfiltered negative-generator nodes; 0 when pair sums are allowed).
So K_A survives every necessary condition tested so far. These are samples, not proofs.

### N3.8 c = 1: the twin sector problem also has a solution (`p13_c1_sector.py`, run 1: 8/8, `P13-C1-SECTOR-EXACT`)

Two pre-run edits (no run before them): B2 compared with t instead of t/2 (twirl of the B_tw operator has trace 2);
the matching header line. Setting (W): for c = 1, K₃ = K₃* (p1 C), B_tw ⊆ K₃, S₃ symmetry and LU invariance from
twin-link teleportation (p2 A3 exact; the filtered twin link (1 ⊗ A)·SWAP/2·(1 ⊗ A)† = PT₂(Ad(1 ⊗ Ā)Φ⁺) lies in
the twin cone, so the five-token filter argument transfers; written, not separately certified). The GHZ stabilizer
group consists of real local Paulis, so the twirl commutes with every PT_j and PT_j maps GD into GD [X B1]. Hence
K₃ ∩ GD is a G-invariant Euclidean self-dual cone containing S_tw = twirl(B_tw). Written: twirl(Sep_{ij|k}) is the
cone of pair sums inside each of the two blocks {b, b + d_k} (GHZ states of a block are the Bell states of a
logical qubit of (i, j) with k; separable states have Bell fidelity ≤ ½ in each block); with [X B2] (the operator
PT₂(Φ⁺)⊗|+⟩⟨+| + PT₂(Φ⁻)⊗|−⟩⟨−| twirls to t/2, t = (1,1,1,1,1,−1,1,−1)) this gives S_tw = cone(G·p, G·t), 28
generators; cross-check: 30 random B_tw generators twirl into cone(S_tw) [X B3].
K_tw = cone(S_tw ∪ G·κ′), κ′ = (−1, 3, 1⁶) (36 generators). In (P, C) coordinates
K_tw* = {P ≥ 0; |C_c| + |C_d| ≤ P_a + P_b for every split {a,b}|{c,d}; |C_b| ≤ ΣP/2}. Exact: G-invariant and
pairwise ≥ 0 [T1] (by hand: t·t′ = 2k − 2k′ ≥ 0 because complementary pairs meet as often as the pairs do; t·κ′ ≥ 0;
κ′·κ′′ ≥ 0); double description in two orders returns exactly the 36 generators, each extreme [T2]; independent
cross-check by an exact phase-I simplex (Bland): 300 random exact points of K_tw* (212 with a negative entry) are
nonnegative combinations of the generators, reconstruction verified [T3]; S_tw ⊆ K_tw, W3 ∈ cone(S_tw), GHZ₊ ∉ K_tw,
p10's F ∉ K_tw [T4]. (A first hand decomposition attempt, using only positive-sign generators after a sign
normalization, was wrong — x = (P = (0,2c,2c,2c), C = (0,c,c,c)) needs t's of opposite sign on fibre 0 — so the
self-duality rests on the exact double description and the independent simplex cross-check, not on a written
proof.)
Explorations: x12 (S_tw, its dual; from S_tw alone the extreme-ray completion is stuck at p10's F, whose orbit is
not self-positive); x13 (non-extreme greedy, regress, stopped at its step limit); x14 (DFS with seed κ′: FOUND
K_tw, also with W3 added — W3 already lies in cone(S_tw)); x15 (exact, sampled: the twin-link (2,2,1) contraction
condition PT_Q(M) ⪰ 0 holds on all 36² generator pairs and 96 filter-image pairs, but its countercontrol x = y = GHZ
also passes, so this test does not discriminate at this instance; twin-link ring and K₄ values ≥ 0); x16 (FLOAT:
filter-orbit self-positivity of K_tw's generators, worst −5.0e-17, round-off).
**Verdict N3.8: NEW (item 4, the c = 1 question narrowed).** The GHZ-diagonal sector conditions do not exclude
c = 1: K_tw is an exact G-invariant Euclidean self-dual sector cone containing twirl(B_tw). With p10, every c = 1 K₃
leaves cone(B_tw ∪ Z); K_tw does so through κ′. c = 1 remains not decided; any exclusion must use constraints the
GHZ-diagonal twirl discards. Both completions found (K_A for c = 0, K_tw for c = 1) contain κ-type elements.

### N3.9 Fixed point (update of N3.6)

Passes after N3.6: N3.7 (NEW: SP decided, K_A), x9–x11 (no NEW), N3.8 (NEW: K_tw), x15–x16 (no NEW). The last two
passes produced no NEW finding; the protocol's 3–4 consecutive passes without NEW are not reached. N3 remains OPEN,
with the wall sharpened to the lifting question (RESULT §0).

### N4.5 Bearing of N3.7 on the candidate principles (record; written, partly heuristic)

- In any K₃ whose GHZ-diagonal section is K_A, a PSD element X must have twirl(Ad(k)X) ∈ K_A ∩ R⁸₊ = S for every
  local filter k (filter invariance), i.e. GHZ-fidelity ≤ ½ after every local filter. ω_{1/2} (p9 R) has GHZ-fidelity
  5/8 and so is excluded. Whether every mixed PSD operator on E with marginal D/2 and nonzero |00⟩⟨11| coherence is
  excluded in the same way (which would make Pur₁ fail in every K_A-type completion) is not shown: research
  question, not a claim.
- Choi availability and transitivity: unchanged (N4.1, N4.3).

Correction to N3.8 (notation): the pairing of two t-generators is ⟨t, t′⟩ = 2k + 2Σ_{x ∈ {c,d} ∩ {c′,d′}} s_x s′_x ≥ 0,
with k = |{a,b} ∩ {a′,b′}| = |{c,d} ∩ {c′,d′}| (complements of two 2-subsets of a 4-set meet as often as the subsets);
"2k − 2k′" in N3.8 is a slip for this bound.

## N9. Replays, hashes and end integrity (2026-10-09 07:12 UTC)

**Replays.** `run_all.py` (p1–p13; runs 1 and 2, covering p1–p10 and p1–p12, kept as `run_all.run1.*`,
`run_all.run2.*`, `replay.run1/`): `VERDICT RUN-ALL-OK`, every probe exit 0, stderr empty, stdout byte-identical
(script / recorded = replay, sha256 first 16 hex: p11 cac1d35e0838b198 / 8c246bf96c570713; p12 cf549d138c825579 /
27776d481e2eba78; p13 0e3dbec81d2ba7a8 / 6345758fd01285aa; p1–p10 as in N9.0; library cc2c6aca94007ac8).
`run_x.py` (exact explorations x3, x4, x6, x8, x10–x15; run 1 kept as `run_x.run1.*`): `VERDICT RUN-X-OK`, all
byte-identical. x5 is not replayed (stopped by hand). Floats (x1, x2, x7, x9, x16) not replayed.
Exploration hashes (script / output): x1 5597005861fae762 / 2bf16532da45dec8; x2 fc59980cc9cf5276 / 8e97986814257da9;
x3 5b487f04a24a1ee8 / 8cde8d761f48f259; x4 0184400cb6153e8a / ec5d70e45a718ebe; x5 b10153ff6e69cc34 /
dbbbcf7f2c153889 (partial); x6 17f283384f8c6727 / 84adf8fbc4940511; x7 bfbde79f0ccb55fb / e322ed93d51abf4a;
x8 d4dd7d026cd846e8 / c80ada7505ebc04e; x9 3294eea75d54a11d / cfe725f3c948f93e; x10 bb2662048b071ae1 /
61cfc8a1af8eb564; x11 73b7259d86272d44 / 27782abde8b401a7; x12 934f6a9519ea1035 / 2459eb7ccae290b3; x13
766a48606dae60bc / 7649eabc1477a9a5; x14 ba3ca08625c4d52a / b180ff52b3cf011d; x15 f48eee4df9eb5c08 /
1bf7368dcfd0bcc9; x16 a5804b3632439d73 / dd28b4bdd811a8a7.

**End integrity (07:11:53 UTC).**
- `cd scratchpad/eq/base && sha256sum -c --quiet ../base.manifest.sha256`: silent, exit 0.
- `/home/user/incompleteness`: `git status --porcelain` empty. **HEAD is `f0d37906a83585efdaca8e3ee3404410e869c43e`,
  not `bc3bf9bc846c138de5f5b45f386a75244da4f21f`** (HEAD was bc3bf9bc at this thread's start, recorded output at
  04:01:02Z). Read-only inspection: bc3bf9bc is an ancestor of HEAD; the reflog shows checkouts to the branches
  `claude/eq4f-preflight` (at bcbc516f) and `claude/network-tool-access-8jtdhm`, then a commit f0d37906 "EQ4-F preflight
  (design only, not for merge): four-copy package statement layer", 2026-10-09 06:58:32 +0000, author "Claude". This
  thread made no git write of any kind (every git command it ran was `status`, `rev-parse`, `cat-file`,
  `merge-base --is-ancestor`, `log`, `diff --stat`, `reflog`). The repository was moved by another writer during the
  thread. Per §A.26 this is recorded as a provenance anomaly in the repository; it does not touch this thread's
  evidence, which reads kernel conventions only from the base snapshot (manifest intact) and inputs only from the
  scratchpad. No measurement was run after the anomaly was detected; nothing was quarantined or modified (the
  repository is outside this thread's write area).
- Writes: every file under `scratchpad/eq4/P/` is newer than `.start_marker` and was written by this thread (scripts,
  outputs, replays, NOTES, RESULT). Files newer than the marker elsewhere in the scratchpad (`eqreview/REVIEW.md`,
  `eqreview/audit_eq4f.*`, `eqreview/replayEQ4F/*`, `eq4/names.txt`, `eq4/preflight/*`) belong to other agents; they
  were neither written nor read by this thread.

Correction to N3.9: the passes after the last NEW finding (N3.8, K_tw) are x15–x16 only, i.e. one pass without a NEW
finding (not two); the fixed point is not reached.
