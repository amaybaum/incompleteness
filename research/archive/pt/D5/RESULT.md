# Thread D5 (BRIDGE-DERIVE), stage 5 — Q-EX-BRIDGE — RESULT (research only)

Governing texts: `PROTOCOL-STAGE5.md` (`9e01f098…`) with amendment 1 (`1f639115…`: working directory `pt/D5/`), and
the stage-1–4 protocols they name. Base L = `9f9f8257…`, read-only. Evidence levels: [K] certified at L
(file:line, paths under `verification/lean-mathlib/OIBridge/` unless marked), [D] design module, [W] written
argument, [X] exact computation (instance-scoped unless lifted by [W]), [N] numerical (none used), [L] unverified
literature (none used). Outcomes DERIVED / INDEPENDENT / CONDITIONAL(P; A) exactly as the protocol defines them.
(b)[G]: "every element of G, acting on one token of the pair by `actC`/`actT`, maps K into K", for a closed K ⊆ W 3
with H1–H3. Single-token data at L: the ball; the NOT `nflip` = R_x(π) (CompositeDimension.lean:797, d1 A2); the
drive = the flow through the NOT about its axis x (`ElementaryDrivability`, KInfFoundations.lean:264); J = `cyc3`
(:416–425, `ball3Drive` :449), with J·R_x(t)·J⁻¹ = R_y(t) (d1 A3). Process event: an anomaly sweep found files
of another writer under `pt/` (§5); none is an input of this thread.

## 0. Answer

**Bottom line.**
- **Nothing at L below the OI⁺ layer yields L2.** Single-token principles are pair-blind; the native-gate relations
  are identities of linear maps on W 3, true for every K; observer recursion is satisfied by an exotic cone; and the
  only spectator clause that is a theorem at L — context stability of the substratum's monomial class — is a
  theorem about the complex matrix carrier, whose composite cone is PSD by construction. Transcribed to W 3 it is
  (b) for the monomial operations: not certified there, and even granted it leaves an exact unreachable state
  (φ₀ = (1,2,3,4)/√30, cap seed c = 513/512): EXOTIC-E. [W + X d1 C, E, F, B3]
- **Every candidate whose content is a spectator clause** (α; β through context stability; γ for an extension;
  δ's every-level clause) gives (b_min) only CONDITIONALLY on that clause together with L1 (the flow and an
  off-frame partner available on one token), and fails the disguise test.
- **The candidates that pass the disguise test** split: ε and ζ (drivability form) are INDEPENDENT with exact
  countermodels; λ (KT(4) with `tok`) passes as written and implies IE1 ⊇ (b_min): DERIVED(λ) in the protocol's
  sense, on [D] + audited [W + X] evidence. But λ is a four-token principle with no source at L, equivalent to IE1
  relative to the uniform pair premises; it produces the composite action by conditioning across groupings through
  gate-supplied links, the cross-grouping positivity stage 2 recorded as FCC's own content.
- **Matrix-level exposed assumption.** Inside `DerivedOI`, the "every level" of `LayerFlowExecutable` is redundant:
  the closure's implementation locality already gives the flow's spectator extension at every level (N1c; exact
  identity d2). The spectator clause of the layer-flow form (GR.md:262) thus sits in the closure's context
  stability, which is a hypothesis for any theory that executes the flow (the monomial class cannot realize it,
  LiftAudit.lean:187).

**Verdict table.**

| candidate | field-neutral transcription (pair: W 3, K closed, H1–H3) | outcome | assumption named (status) | disguise test | evidence |
|---|---|---|---|---|---|
| α OI⁺-1 | available token operation O ⇒ actC O, actT O available on the pair, i.e. (b)[available token ops]; form exact, availability by analogy | CONDITIONAL(α; L1) | L1: flow and J available on a token — K∞-Act/K∞-Drive OPEN (ROADMAP.md:1014–1017); α itself: added OI⁺ principle (GR.md:228), independent of the core (CompletedOI.lean:506); field-neutral K2 OPEN (ROADMAP.md:1004) | FAILS (α is the spectator clause) | [K] anchors; [X] d1 A4, B1; stage-4 Y2 [W + X] |
| β implementation locality | generation (pair availability = realization by a pair class, available ⇒ K-preserving) + ContextStable (O ∈ token class ⇒ actC O, actT O in pair class) + label invariance | CONDITIONAL(β; ContextStable for a class containing the flow and J, + L1); β without ContextStable INDEPENDENT (K(Z_F)) | ContextStable: theorem for the monomial class (StructuralClosure.lean:261); hypothesis for every class realizing the drive (:365, :408; N1b) | FAILS through ContextStable | [K] ImplementationLocality.lean:359–371, :943–960; [W] |
| γ structural closure, substratum class | (b) for every monomial pair operation (O(2) about z on each token, CNOT, SWAP) and the transpose, plus closure properties | INDEPENDENT (EXOTIC-E, exact seed φ₀, c = 513/512) | — (and not certified for K at L: K(Z_F) has no one-parameter local symmetry, stage-4 Z z1) | passes for the closure clauses; the spectator clause FAILS | [X] d1 C1–C3, C2c; [W] Y1 dichotomy (audited) |
| γ structural closure, extension | as above for a class containing the drive | CONDITIONAL(γ; spectator stability of the extended class, + L1) | hypothesis of `quantumArchitecture_iff_drives_of_closed`, `substratum_extension_quantum_iff_drives` (StructuralClosure.lean:365, :408); GR.md:256 | FAILS | [K]; [X] d1 B1, d3 W1 |
| δ layer flow, native drive, every level | (b)[drive R_x(t)] on one or both tokens | INDEPENDENT (EXOTIC-E, stage-4 seed c = 4609/4608) | — | FAILS (every-level clause) | [X] d1 B1c, B2c, d3 W2c; stage-4 Y4 (audited) |
| δ restricted to level 1 | the drive available on an isolated token (= L1) | INDEPENDENT (pair-blind: stage-3 cones) | — | passes | [W]; [X] d1 B3 |
| δ for the drive with an off-frame partner (J-conjugate, or the phase flow), every level | (b) for two non-commuting flows on one token | CONDITIONAL(δ; partner available + every-level clause) | J: part of `ElementaryDrivability` (hypothesis); phase flow: substratum class (matrix theorem, field-neutral premise) | FAILS | [X] d1 B1, d3 W1, W4; [W + X] d2 (matrix level identity) |
| ε causal separation | no-signalling (actC O ω)₀ν = ω₀ν — an identity of W 3, true for every K | INDEPENDENT (stage-3 cones) | — (Main.md:628 itself says it does not give the composite structure) | passes | [K] CompositeDimension.lean:112–113, :201–202; [W] |
| ε substratum-source spectator stability (GR.md:256) | = γ for the substratum class | INDEPENDENT (as γ, substratum class) | — | FAILS (spectator clause) | [X] d1 C |
| ζ observer recursion, drivability form | the pair body is itself drivable (`ElementaryDrivability` of the slice of K) | INDEPENDENT (K(Z_F): Bell-diagonal flow, involution, J = Ad(X⊗I) off-axis) | — | passes | [X] d1 F1–F3, F6c, B3b; [K] `redundancy_fails` (ImplementationLocality.lean:207, matrix scope) |
| ζ, transitivity form | literal `BoundaryTransitive` of the pair body; extreme-ray form = stage-4 node T | literal: not retained (fails for Q3); T: UNRESOLVED | — | passes | [K] TransitiveBody.lean:301 + [W] (stage 4); stage-4 T EXCLUDES-KNOWN |
| λ KT(4) with `tok` | native: one four-token body composite under 01\|23 and 02\|13, full effect sets, token identity | DERIVED(λ) (λ unsourced at L; λ ⟺ IE1 relative to uniform pair premises) | λ itself: no structure with ≥ 3 tokens at L (EQ5-SOURCE §1; KT4-PREM-1 result.md:196–201) | passes as written (pressure test §1) | [D] `kt4_forward_ie1` (recorded at L, KT4-PREM-1 result.md:186–192); [W + X] EQ3 (audited); [X] d1 D, Dc |

**Dependency chain L0–L3.**

| link | content | status at L (anchor) | field-neutral transcription |
|---|---|---|---|
| L0 | substratum operations are monomial (bijections, phases, read-write); the class is structurally closed, incl. context-stable | [K] `substratumClass` StructuralClosure.lean:180; `substratumClass_structurallyClosed` :316 (`substratumClass_contextStable` :261); SubstratumInterface.lean:91, :94; Main.md:628 (causal separation, scope stated there) | single token: O(2) about the corner axis z (d1 C1), exact; the spectator theorem only by analogy: on the matrix carrier the composite cone is PSD by construction (N1e) |
| L1 | an off-frame or continuous operation available on one token | open obligation: K∞-Act, K∞-Drive (ROADMAP.md:1014–1017); `ElementaryDrivability` a structure/hypothesis (KInfFoundations.lean:264); matrix: not supplied by the substratum already at level 1 (LiftAudit.lean:183–187, :200; ExecSource.lean:129; ReadWriteControl.lean:174); hypothesis of the endpoints (`DrivesElementary`, SubstratumSource.lean:77; DerivedQ3.lean:222) | exact: the drive R_x(t), J = cyc3 |
| L2 | the composite action (b) | OI⁺-1 = `HasParallelReferenceExtension` (CompletedOI.lean:129; ReferenceExtension.lean:447): added principle (GR.md:228), independent (CompletedOI.lean:506; ReferenceExtension.lean:507); supplied by implementation locality (ImplementationLocality.lean:370 → :957) through `ContextStable` (:359); theorem for the substratum class (StructuralClosure.lean:261), hypothesis for an extension (:365, :408; GR.md:256); `LayerFlowExecutable`'s every level (LiftAudit.lean:112) = spectator extension of level 1, redundant inside `DerivedOI` (RouteB.lean:141; MicroscopicReversibility.lean:223) [W + X d2]; field-neutral: K2 OPEN (ROADMAP.md:1001–1005); IE1 derived at KT(4) with tok, premises unsourced (EQ3, EQ5-SOURCE, KT4-PREM-1) | by analogy (form exact: d1 A4) |
| L3 | (b_min) ⇒ S4 ⇒ K = Q3 | stage 4 [W + X], audited; re-checked here: the flow, its J-conjugate and cnot generate su(2)⊗P₊ ⊕ su(2)⊗P₋ (d1 B1, dim 6); so do the flow and the phase flow on one token (d3 W1, W4) | exact |

**Weakest sufficient added content.**
- *Field-neutral:* (b) for two non-commuting one-parameter rotation groups of one token — the native drive with its
  J-conjugate (d1 B1), or the drive with the substratum phase flow about z (d3 W1, W4) — or stage 4's single
  off-frame flow (S3[n]) or single off-frame order-3 rotation (R1). Each single on-frame flow, and the phase flows
  on both tokens, is insufficient (d1 B1c, B2c; d3 W1c, W2c, W3c; stage-4 Y4).
- *Matrix:* beyond the substratum class (structurally closed, a theorem) and L1 (the flow at level 1), the flow's
  spectator stability (1_R ⊗ its implementation admissible for every R) — equivalently, given level 1,
  `LayerFlowExecutable` at every level (N1c, d2). Minimality is not claimed in either setting.
- *Relation to OI⁺-1:* in both settings the added content is OI⁺-1 restricted to the flow (and, field-neutrally,
  one off-frame partner): a sub-instance of OI⁺-1, not derived from anything at L.
- *Relation to the layer-flow hypothesis:* at the matrix level it is exactly the every-level clause. The matrix
  theorem succeeds with one flow because `DerivedOI` supplies the phases at every level; field-neutrally the NOT's
  flow alone is on the exceptional set, and its sufficient partner (the phase flow, d3 W1) needs its own (b).

## 1. Candidate by candidate

### 1.0 The sourcing map of L2 (decides the shape of every verdict)
- **Theorems of the substratum class.** Exactly one spectator family: `ContextStable substratumClass`
  (StructuralClosure.lean:261, within `substratumClass_structurallyClosed` :316). Through
  `parallel_of_implementationLocal` (ImplementationLocality.lean:943–955) it gives observational independence of
  the theory the monomial class generates. Scope: monomial operators on the complex matrix carrier.
- **Hypotheses of an extension.** `hc : StructurallyClosed 𝓘` in `quantumArchitecture_iff_drives_of_closed`
  (:364–366) and `substratum_extension_quantum_iff_drives` (:408–411); `ContextStable 𝓘` inside `DerivedOI T`
  (RouteB.lean:141–143 → MicroscopicReversibility.lean:223–225) for any T executing a flow at level 1, since its
  generating class must realize the flow and so is not configuration-level (LiftAudit.lean:183–187); OI⁺-1
  (CompletedOI.lean:419); the every-level clause of `LayerFlowExecutable` (LiftAudit.lean:112–113).
- **What `ImplementationLocality` says, and what :957 needs.** `∃ 𝓘, ImplementationGenerated T 𝓘 ∧ ContextStable 𝓘 ∧
  LabelInvariant 𝓘` (:370–371). `observationalIndependence_of_implementationLocality` (:957–960) needs that and
  `[Nonempty A]`, nothing else. Its only spectator content is `ContextStable` (:359–361: `𝓘 S K → 𝓘 (R × S)
  (1_R ⊗ K)`). On the matrix carrier the spectator extension of a conjugation is a conjugation
  (ReferenceSufficiency.lean:754) and is PSD-preserving for every R (ReferenceExtension.lean:182). So the clause
  constrains which operators are admissible, never which composite cone they preserve.
- **Level 1 plus spectator extension gives every level (N1c).** Given `HasParallelReferenceExtension T` and
  `∀ t, T.availExt 1 Unit (conjChannel (gateFlow (levelPerm σ 1) t))`, level 0 is free (`availExt_zero`,
  PhysicalCharacterization.lean:164). For n ≥ 1, apply the extension with R = Fin n and e_n(r, (s, 0)) = (s, r); by
  `withSpectator_conjChannel` the result is the conjugation by `reindex e_n e_n (1_n ⊗ gateFlow (levelPerm σ 1) t)`.
  This equals `gateFlow (levelPerm σ n) t` because `gateFlow g t = 1 + (exp(iπt) − 1)(1 − permMat g)/2`
  (SecondOrderCircuit.lean:352–357) is affine in g with 1 ↦ 1. The identity is checked exactly in d2 L1 for
  S = Fin 2, Fin 3 and n = 1, 2, 3, with countercontrols L1c (spectator placed in the system slot) and L1c2 (flow on
  the ancilla). Since `DerivedOI T` ⇒ `ImplementationLocality T` (RouteB.lean:149) ⇒
  `HasParallelReferenceExtension T`, the every-level clause in `derivedOI_qm_iff_layerFlowExecutable'`
  (DerivedQ3.lean:222) is redundant given its own hypothesis `DerivedOI`. Pressure test: the redundancy relocates the
  spectator clause into the closure; it does not shrink the resource below "the flow at level 1 plus spectator
  stability of a class realizing it".
- **Exposed assumption (N1e).** All matrix-level spectator statements are properties of a `FiniteOperationalTheory`.
  Its level-n carrier is `Matrix (A × Fin n) (A × Fin n) ℂ` with the PSD cone, so the composite cone is Q3 by
  construction (ROADMAP.md:68: K, "to the complex matrix kinematics the finite characterization assumes", OPEN).
  None of them is about which K ⊆ W 3 a token's operations preserve. Their field-neutral transcriptions are (b)
  for the corresponding operations, and none of these is certified (K2, ROADMAP.md:1004).

### 1.1 α — OI⁺-1, observational independence
Transcription: an available operation O of a token (a body map, homogenized by `homMap`) remains available with
the other token adjoined untouched, as `actC O` / `actT O`, available meaning K-preserving. The form is exact:
`actC R(U)` is `Ad(U ⊗ I)` on all 16 basis tables (d1 A4, two exact unitaries; countercontrol A4c), the W 3
analogue of `isSpectatorExtension_iff` (SpectatorBridge.lean:188). Availability is by analogy (N1e). Derivation:
α + L1 (flow and J available on one token) ⇒ (b_DJ) ⇒ the generated Lie algebra with cnot is su(2)⊗P₊ ⊕
su(2)⊗P₋ (d1 B1) ⇒ every pure state is reachable (stage-4 Y2, audited) ⇒ K ⊇ Q3 ⇒ K = Q3 by H3. Exclusion
controls: K(E0) is moved by actC(R_x(π)R_y(π)) (d1 B3a, pairing −1); K(Z_F) is moved by actC J (d1 B3b: witness
P_χ with all four Bell-type overlaps 1/4, pairing −1/2). Retention: d1 B4. Disguise: fails. **CONDITIONAL(α; L1)**,
the bridge resting on α itself. α is sourced as an added OI⁺ principle at the matrix level (GR.md:228;
independence `oiPlus_independence` CompletedOI.lean:506, `redundancy_fails` ImplementationLocality.lean:207). It is
an open obligation (K2) field-neutrally.

### 1.2 β — implementation locality
Transcription: a token class 𝓘₁ and a pair class 𝓘₂ with (G) pair availability = realization by 𝓘₂, available ⇒
K-preserving; (C) O ∈ 𝓘₁ ⇒ actC O, actT O ∈ 𝓘₂; (L) label invariance (token relabelling, SWAP). (C) is the spectator
clause and fails the disguise test; with it, β ⇒ (b)[𝓘₁], and with L1 ⇒ Q3 as in 1.1. Without (C): take
𝓘₂ = the automorphism group of K(Z_F) (closed under composition and inverses; SWAP-invariant, stage-4 Z z1) and
𝓘₁ = the body automorphisms. (G) and (L) hold by construction, H1–H3 hold (stage 3, audited), and K(Z_F) ≠ Q3:
β minus (C) is INDEPENDENT [W]. **CONDITIONAL(β; ContextStable of a class containing the flow and J, + L1)**.
(C) is a theorem only for the monomial class, whose transcription is insufficient (1.3).

### 1.3 γ — structural closure
(i) **The substratum class (a theorem at L).** On one token the monomial unitaries map to O(2) about the corner
axis: diag(1, i) ↦ R_z(π/2), X ↦ `nflip` (d1 C1). The transcription of its structural closure to the pair is (b)
for all monomial pair operations, which include the local monomials, CNOT and SWAP, together with the transpose.
The generated compact group D·P ⋊ {1, T} sends pure products to vectors whose magnitudes are a permutation of
|a_i||b_j|, with free phases. The best overlap of φ with that set is therefore σ_max² of a 2×2 arrangement of
|φ|, = (1 + √(1 − 4 det²))/2 [W; nonnegative matrices have nonnegative top singular vectors]. For φ₀ =
(1,2,3,4)/√30 the minimum |det| over the 24 arrangements is 1/15 > 0 (d1 C2; countercontrol C2c: the product
magnitudes (1,2,2,4)/5 give 0). So φ₀ is unreachable with m = (1 + √(221/225))/2, and c = 513/512 lies in
(1, min(2, 1/m)] (d1 C3, exact by squaring with signs checked). By the audited dichotomy (stage-4 Y1, Z claim D)
the cap seed (I − cφ₀φ₀†)/8 extends to an exotic invariant self-dual K with H1–H3. **INDEPENDENT(γ_substratum)**,
EXOTIC-E with an exact seed. This transcription is also not certified for K at L: K(Z_F) is preserved by no
one-parameter group of local maps (stage-4 Z z1, audited), hence not by actC R_z(φ).
(ii) **An extension containing the drive.** The structural closure is a hypothesis (StructuralClosure.lean:365,
:408); its spectator clause fails the disguise test. With L1, the drive plus the substratum phase flow on one token
generate su(2) ⊕ su(2) with cnot (d3 W1, W4), so **CONDITIONAL(γ_ext; spectator stability of the extended class,
+ L1)**. The other closure clauses (composition, coarse-graining, relabelling, adjoint) are properties of a class
that the automorphism group of K(Z_F) also has; they carry no link between token and pair.

### 1.4 δ — layer-flow executability
Matrix: `LayerFlowExecutable` (LiftAudit.lean:112) quantifies over every level n and every time t;
`levelPerm σ n` keeps the ancilla a spectator (:51–52; GR.md:262). Field-neutral: σ = the NOT (an involution of the
body moving the corners), whose flow is the drive R_x(t); "every level, the ancilla a spectator" = (b)[drive] on
one token (and on the other by label invariance). For the native drive alone the Lie closure with cnot has
dimension 2 on the control and 1 on the target (d1 B1c, B2c; d3 W2c), which is the exceptional set; stage-4 Y4 gives
an exact EBF seed (c = 4609/4608). **INDEPENDENT(δ, native drive)**. Restricted to level 1, δ is L1 itself, a
single-token statement: **INDEPENDENT** (pair-blind, 1.8). δ over the NOT and its J-conjugates, or with the phase
flow on the same token, reaches dim 6 (d1 B1, d3 W1): **CONDITIONAL(δ; the partner available + the every-level
clause)**, which fails the disguise test. The protocol's sub-question: level 1 plus implementation locality /
`HasParallelReferenceExtension` gives every level — YES (1.0, d2), but that added content is itself the spectator
clause.

### 1.5 ε — substratum locality
Main.md:628: causal separation "does not alone establish statistical product structure after conditioning, local
tomography, or one common tensor-product instrument category. … The common local quantum composite/instrument
structure is the content of the inert-spectator and iterated-composition conditions". Transcription:
no-signalling, (actC O ω)₀ν = ω₀ν for every linear token map O (`homMap` fixes coordinate 0,
CompositeDimension.lean:112–113; `actC` :201–202). This is an identity of the carrier, true for every K, so the
stage-3 cones satisfy it: **INDEPENDENT(ε)**; it passes the disguise test (no preservation clause). ε's second
reading, spectator stability of the substratum-source form (GR.md:256), is γ(i): **INDEPENDENT** (d1 C).

### 1.6 ζ — observer recursion / embedded observation
Matrix: `ObserverRecursion` (CompletedOI.lean:327) and `EmbeddedObservation` (EmbeddedObservation.lean:123) supply
iterated composition, not inert spectators. Kernel independence at matrix scope: `redundancy_fails`
(ImplementationLocality.lean:207: validity, reversible richness and embedded observation with the core do not give
observational independence; all operations, matrix carrier). Field-neutral transcription: the pair body (slice
ω₀₀ = 1 of K) is itself a system carrying the single-system structure.
- Drivability: K(Z_F) has it. The flow U(w) = I + (w − 1)ψ₀ψ₀† (|w| = 1, symbolic) fixes every defect (d1 F1); the
  flow is unitary and ipW-orthogonal, so it preserves K(Z_F) = (Q3 ∩ Z*) + cone Z [W]. U(−1) is an involution that
  moves the pure state on ψ₀ + ψ₁, which lies in K(Z_F) (d1 F2). J = Ad(X⊗I) permutes Z_F, and J·U(−1)·J⁻¹ moves a
  point of K(Z_F) that every flow member fixes: J is off-axis (d1 F3). Control F6c: a Householder member off the
  Bell basis moves a defect out. K(Z_F) fails (b_DJ) (d1 B3b): **INDEPENDENT(ζ, drivability)**.
- Literal transitivity (`BoundaryTransitive`, OrbitGeneration.lean:79) fails for Q3 itself (TransitiveBody.lean:301
  + W, stage 4): not retained. Extreme-ray transitivity is stage 4's node T, EXCLUDES-KNOWN only: **UNRESOLVED**.
  Both pass the disguise test.

### 1.7 λ — four-token composition coherence KT(4) with `tok`
Transcription exact (λ is stated on W 3 tables). Derivation: `kt4_forward_ie1` ([D], design run; recorded at L by
the certified KT4-PREM-1 result.md:17–22, :186–192) gives IE1 at every pair from hcls ∧ hadm ∧ hcl ∧ hgate ∧ H. With
uniform K, gates exactly cnot (hcls trivial, KT4-PREM-1 M_cl.1), hadm from H1 and H3 (K = K* ⊆ SEP* = maxCone), hcl
the setting, hgate = H2 and H = λ: λ ⇒ IE1 ⊇ (b_S4) ⇒ Q3. EQ3 (base `bcbc516f`, [W + X], audited 29/29) obtains the
same, Q3 directly in aligned charts (T3′). Disguise: λ is stated through a four-copy body, products of states and
effects across two groupings and token identity, with no operation on part of a composite (EQ3-AUDIT §2 item 4):
**passes as written**. Pressure test of this favourable branch:
- (a) uniform K(E0) violates λ: family (i) value −1 at gate-supplied effects (d1 D, reproducing the stage-3 record);
  the Q3 control is ≥ 0 (d1 Dc).
- (b) Content. Relative to hadm, λ ⟺ FCC (EQ5-SOURCE §3.6, two witnesses). FCC's family (ii), "L·f·L′ᵀ ∈ K", is
  by the four-copy table identity the closure of K under index-wise maps encoded by its own elements; through the
  gate's links these are local filters and rotations (EQ3 §1). So the composite action is produced by conditioning
  across groupings, not assumed. Stage 2's renaming test lists this cross-grouping positivity as FCC's own content
  (PROTOCOL-STAGE2.md:77–78).
- (c) Relative to uniform pair premises λ ⟺ IE1 (EQ3-AUDIT §4). This is not by itself a disguise: every retained
  sufficient P is equivalent to K = Q3 given H1–H3.
- (d) λ has no source at L: there is no structure with three or more tokens, and `tok` has none (EQ5-SOURCE §1,
  row 9; ROADMAP Kₙ OPEN).
**DERIVED(λ)** in the protocol's sense, on [D + W + X]. λ is strictly stronger than (b_min), since it gives IE1 on
both tokens, and it is unsourced at L.

### 1.8 Below the OI⁺ layer at L (the protocol's last question)
No principle yields L2 [W + X], an exact obstruction for the stated classes:
- (i) K∞-Stage, K∞-Act, K∞-Drive, K∞-Trans, K∞-Seed, K∞-V4, K∞-Geom (ROADMAP.md:1010–1033) and `CopyNatural`
  (KInfFoundations.lean:284) speak of one body, its effects, its operation data and the copies' NOTs. None mentions
  a pair cone, so every K with H1–H3 carries the same single-token data. The stage-3 cones satisfy H1–H3 with Q3's
  single-token structure and fail (b_DJ) (d1 B3a, B3b).
- (ii) The native-gate relations `relT`, `relC` (CompositeDimension.lean:224–225) are identities of linear maps
  (d1 A5) and hold whatever K is. K(E0) satisfies H2 and is moved by actC nflip (d1 E: a pure φ with ⟨φ|pW(E0)|φ⟩ = 1
  and ⟨φ|pW(actC nflip E0)|φ⟩ = −1; control E0c: the NOT permutes Z_F). So the relations do not give (b) even for
  the NOT.
- (iii) Observer recursion: 1.6. (iv) Causal separation: 1.5.
- (v) The single spectator theorem at L (the substratum class) transcribes to monomial (b), which is insufficient
  (1.3).

## 2. Ledger — certified versus added; flagged premises

| item | class | anchor | used in |
|---|---|---|---|
| `W 3`, `homMap`, `prodState`, `actT`, `actC`; `IsNot`, `NativeGate` (`relT`, `relC`); `cnot` (`sgn`, `pc`, `pt`), `z3`, `nflip`, `phiW`, `cnot_prodState_xplus_z3` | [K] | CompositeDimension.lean:97, 112, 161, 198, 201, 210, 218–225, 741–790, 793, 797, 1220, 1222 | all; transcribed by parsing the source (d1 A1–A2, A5; d3 W0) |
| `ElementaryDrivability` (a structure: hypothesis-type), `CopyNatural`, `cyc3`, `ball3Drive` (positive control) | [K] | KInfFoundations.lean:264–276, 284, 416–425, 449 | L1, J (d1 A3) |
| `HasParallelReferenceExtension`, `control_not_implies_parallelReferenceExtension`, `conjChannel_referencePositive` | [K] | ReferenceExtension.lean:447, 507, 182 | L2, N1e |
| `ObservationalIndependence`, `OIPlus`, `ObserverRecursion`, `oiPlus_independence` | [K] | CompletedOI.lean:129, 418, 327, 506 | α, ζ |
| `ImplementationGenerated`, `ContextStable`, `LabelInvariant`, `ImplementationLocality`, `redundancy_fails`, `form_fixed_existence_fails`, `parallel_of_implementationLocal`, `observationalIndependence_of_implementationLocality` | [K] | ImplementationLocality.lean:352, 359, 364, 370, 207, 223, 943, 957 | β, ζ, N1c–N1d |
| `isSpectatorExtension_iff`; `withSpectator_conjChannel`; `availExt_zero` | [K] | SpectatorBridge.lean:188; ReferenceSufficiency.lean:754; PhysicalCharacterization.lean:164 | N1c |
| `substratumClass`, `StructurallyClosed`, `substratumClass_contextStable`, `substratumClass_structurallyClosed`, `quantumArchitecture_iff_drives_of_closed`, `substratumClass_not_drivesElementary`, `substratum_extension_quantum_iff_drives`; `DrivesElementary` | [K] | StructuralClosure.lean:180, 183, 261, 316, 364, 370, 408; SubstratumSource.lean:77 | γ, L0, L2 |
| `DerivedOI`; `ReversibleImplementationLocality` | [K] | RouteB.lean:141; MicroscopicReversibility.lean:223 | δ, N1c |
| `gateFlow`, `levelPerm`, `LayerFlowExecutable`, `configurationLevel_not_layerFlowExecutable`, `substratumTheory_not_layerFlowExecutable`; `derivedOI_qm_iff_layerFlowExecutable'`; `obs_not_layerFlowExecutable`; `readWriteSourced_not_qm`; `unit`, `proj`, `permMat` | [K] | LiftAudit.lean:47, 51, 112, 183, 200; DerivedQ3.lean:222; ExecSource.lean:129; ReadWriteControl.lean:174; SecondOrderCircuit.lean:352–357, 710 | δ, L1, d2 |
| `BoundaryTransitive`, `boundaryTransitive_fullAut3`; `not_boundaryTransitive_of_nonextreme_boundary` | [K] | OrbitGeneration.lean:79, 537; TransitiveBody.lean:301 | ζ |
| `ipW`, `dualW`; `pauliW`, `Q3`; `IE1`; `kt4_forward_ie1` (design run) | [D] | FourCopyDefs.lean:31, 34; FourCopyPackage.lean:176, 180; FourCopyCore.lean:156; KT4-PREM-1 result.md:186–192 | comparison objects; λ |
| status records: K, K2, K∞ items; OI⁺ and its primitive and substratum forms; causal separation | [A] record | ROADMAP.md:68, 1001–1005, 1010–1033; GR.md:228, 244, 256, 262; Main.md:628 | chain, α, β, γ, δ, ε |
| stage-3 cones and EBF; stage-4 dichotomy (Y1/Z claim D), S4 reachability (Y2), exceptional-set seeds (Y4), K(Z_F) stabilizer (Z z1); EQ3 route; EQ3-AUDIT §4; EQ5-SOURCE | [W + X], audited records | INTEGRATION-NOTE-STAGE3/4, AUDIT-Y, AUDIT-Z, ledgers | L3, exclusions, λ |
| N1c redundancy; N1e carrier exposure; monomial obstruction (seed φ₀, c = 513/512); ζ countermodel on K(Z_F); native relations vs (b) for the NOT; (b_DJ) closure; drive + phase-flow closure | [W + X], added here | §1; d1, d2, d3 | verdicts |

**Flagged premises and where they enter (as candidates only).** Local operations on entangled states, i.e. (b),
enter only as the candidate under test: α; β's ContextStable; γ's spectator clause; δ's every-level clause. They
also enter in the L3 link, where (b_min) is the antecedent. IE1 appears only as λ's conclusion and in EQ3-AUDIT's
equivalence. Frame covariance (μ) and IE2 are not used. No (o) step is used. Q3 and PSD appear only as comparison
objects and in verification (d1 B4, Dc; the EBF seeds of Y1). Reachability appears only inside L3.

## 3. What is not claimed
- **No derivation of (b) from L.** DERIVED(λ) is relative to λ, a four-token principle that is absent at L. Every
  other route to (b_min) is CONDITIONAL on a spectator clause or INDEPENDENT.
- **Scope of INDEPENDENT.** It is relative to the stated transcription and to the premises certified at L as stated
  (amendment 2), not to every observer-native extension. EXOTIC-E verdicts (γ for the substratum class, δ for the
  native drive) are existence by EBF (audited), non-constructive; only their seeds are exact.
- **λ's evidence.** It is [D] (design run; certified at L only as a record of the dependency) plus [W + X] from base
  `bcbc516f` (EQ3, audited). It was not re-derived at L beyond the countercontrol d1 D/Dc. Its equivalence to IE1 is
  relative to the uniform pair premises.
- **Transcriptions marked "by analogy".** Matrix availability read as K-preservation is a written identification
  [W]. Only the form (actC = Ad(U ⊗ I), actT = Ad(I ⊗ U)) is exact (d1 A4).
- **Weakest content.** Sufficient, not shown minimal, in either setting. The matrix "smallest hypothesis" is the one
  identified here, not proved smallest. The minimal-subset census is thread C's and is not done here.
- **Not decided.** ζ in the extreme-ray transitivity form (stage-4 T); whether context stability is redundant given
  implementation generation (left open at L, ImplementationLocality.lean:85–87).
- **No kernel claim.** No Lean was written. The [K] anchors are read, not rebuilt. Bands are unchanged
  (consistency-axis work).

## 4. Evidence log
Every script ran as `python3 -I -B <script>` from `pt/D5/`, stdout in `<name>.out`, stderr plus an appended
`exit N` line in `<name>.err`. Decision rules were fixed in each header before its first run, with no pre-run edits
after that. Every final script was replayed into `<name>.replay.{out,err}`: `cmp` gives 3/3 byte-identical on
stdout and stderr. There were no failed runs, so there are no `.runK` files. Every `.err` is the single line
`exit 0`. The scripts read only CompositeDimension.lean and KInfFoundations.lean at L, and use no floats in any
verdict.

| script | node | checks | verdict line | runs | replay |
|---|---|---|---|---|---|
| `d1_bridge.py` | N2: transcription (A), L3 for (b_DJ) (B), the monomial class (C), λ control (D), native relations (E), ζ (F) | 26/26, of which 9 are countercontrols/controls (A1c, A2c, A4c, B1c, B2c, C2c, Dc, E0c, F6c) | `VERDICT D1-BRIDGE-EXACT: …` | 1 (17:01:16Z) | identical |
| `d2_levels.py` | N3: the level identity behind N1c | 5/5 (countercontrols L1c, L1c2) | `VERDICT D2-LEVELS-EXACT: the level-n layer flow is the reindexed spectator extension of the level-1 flow` | 1 (17:02:10Z) | identical |
| `d3_weakest.py` | N4: drive + phase flow on one token | 6/6 (countercontrols W1c, W2c, W3c) | `VERDICT D3-WEAKEST-EXACT: …` | 1 (17:05:33Z) | identical |

Key exact values: d1 B1 dim 6 (B1c 2, B2c 1); B3a pairing −1; B3b overlaps (1/4, 1/4, 1/4, 1/4), pairing −1/2;
C2 min |det| 1/15 (C2c 0); C3 c = 513/512 with 1 − 4d₀² = 221/225; D min −1 (Dc min 0); E values 1 and −1;
d3 W1 6, W1c 1, W2c 2, W3c 3, W4 6.

sha256 of every file this thread wrote, except RESULT.md (whose hash is in the final report):
```
6f0e5f4e1ceb0bcb0c7cfc333bd789081e309362cb6cfae12a1a936cdf1bcfba  .start_marker
588bb840703bf82beb2e87583670c710846cae5d57f8a79f752cb0d03fad3e82  .end_marker
e6add11549a67112252615b4f131c594081a25634cc9f82e5b93af6943f16163  NOTES.md
dc1e885a8a334e6cef721afa8faad5cb878f8f030a2c47bcc8b62fc817d53bbe  d1_bridge.py
c4c109306ffb864b22493df0c324d1ddabdcf1589e4dbd9fe9ee425f2b2a5e19  d1_bridge.out  (= d1_bridge.replay.out)
5b4aeaca0b0131147ec9f62f8ce9abece96266541e1492d38911271b8acd33f6  d2_levels.py
8464b5c8785f0978b6c4703b3ed626b2fe29f46c7c00668fc58a2bfb44266d02  d2_levels.out  (= d2_levels.replay.out)
b21f37f8c250d5c4040284a2e787d2c5fa8c65817f9cd9edbaf07e663220c13e  d3_weakest.py
2d4360e692ea92acdd311d82e7d8fe3c142fe37424806b8e5fe008804373a949  d3_weakest.out  (= d3_weakest.replay.out)
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  every .err and .replay.err (6 files, "exit 0")
61816c5820276b5c829015b0fd2e615ab92014bd96c95199ff6c59b75cc723f6  evidence/sweep1/LIST.txt
0e02690febea9a33c30cd77b4a44e3c67334b39d948f501438dbd37c2576744e  evidence/sweep1/MANIFEST-at-sweep.txt
9dcbda2ce9e63bbe71e5947708a388ec708eb76f39f14dfd7b374d4b48b5ab4a  evidence/sweep1/COPY-MANIFEST.txt
2bf9ffd2e8d8b82ad1040eaac14a09577f7de529734ee9716b6055d2b4cafb5a  evidence/sweep1/README.txt
```
The 77 quarantine copies under `evidence/sweep1/files/` are hashed in `COPY-MANIFEST.txt`, whose hash is above.
At 17:12:50Z all 77 matched it.

## 5. Integrity
- **Start.** `pt/D5/` was checked absent at 16:44:07Z and created at 16:44:15Z. `.start_marker` was written first:
  two part files inside `pt/D5/` were assembled at 16:44:35Z and the parts removed, a deviation recorded in NOTES N0.
  - The six manifests and `audit/stage3-inputs/ns.manifest.sha256` (from its own directory, `sha256sum -c` only)
    were OK.
  - Base HEAD was `9f9f8257a980a1819fbbc1dc0019917cf8678626`, porcelain empty (GIT_OPTIONAL_LOCKS=0), and there was
    no bytecode under `pt/base/`.
  - The nine protocol prefixes matched and all nine sidecars verified (STAGE4, STAGE5, STAGE5-AMENDMENT-1 from the
    scratchpad; the other six from `pt/`). The `pt/` top-level listing was recorded.
- **End (17:09:20Z, `.end_marker`).** The same checks were all green, and there was no bytecode under `pt/base/`
  or `pt/D5/`.
- **Sweep: anomaly found (§A.26).** Entries newer than the marker outside `D5/`, `C5/`, `audit/` and
  `audit*-replay/`:
  - `pt/PROTOCOL-STAGE6.md` (16:49:36Z) and `pt/PROTOCOL-STAGE6.sha256` (16:49:55Z);
  - directories `pt/I1`–`pt/I4`, with start markers from 16:51:44Z to 16:53:28Z and files still being written at
    17:08Z.

  In total 77 files and 4 directories (sweep 1, 17:08:20Z; sweep 2 at the end shows the same set, still growing).
  None of them was written by this thread.
  - Recorded with mtime, size and sha256 in `evidence/sweep1/`. Only hashes were taken; no content was read or
    displayed.
  - Quarantined as byte copies (17:08:37Z; `COPY-MANIFEST.txt`). The originals were left in place and untouched:
    moving them would write outside `pt/D5/` and remove files an active writer uses, and nothing was deleted.
  - One copy (`I2/INVENTORY.md`) reflects a state later than the sweep.
  - The decisive scripts ran from 17:01:16Z to 17:07:02Z. That is after the anomalous writer began and before
    detection (17:07:10Z). Their only inputs, two Lean files under `pt/base/`, are covered by the end checks (HEAD,
    empty porcelain, manifests).
  - No measurement was run after detection. The coordinator is asked to attribute the files.
- **Sweep slip.** The first sweep command (17:07:48Z) bound `-newer` to the wrong branch and listed and hashed every
  non-excluded file under `pt/` (names and hashes only). The tool runner saved that output, and one earlier grep
  output, to tool-results files outside `pt/`; no command of mine redirected output there.
- **Reads.**
  - The nine protocol files and the prescribed records, in order.
  - The ledgers named by the protocol and the certified premise audit.
  - `pt/base/AGENTS.md` (code-review rules, §A.21, §A.31).
  - At L: the Lean files and lines listed in NOTES N1 and §2, GR.md :205–275, Main.md :628 and ROADMAP.md :66–70,
    :998–1035, :1072–1095.
  - The design modules at the lines in §2.
- **Not read.** `pt/C5/`; `audit/stage3-inputs/OWNER-*`; `audit/stage4-inputs/OWNER-*`; `audit/stage5-inputs/`;
  `audit/reviews/`; `audit/aborted-launches/`; the contents of `pt/I1`–`pt/I4` and of `PROTOCOL-STAGE6.md` (hashed
  only).
- **Writes.** Only inside `pt/D5/`. Transient files of this thread (`.chk`, `d1_time.tmp`, the two
  `.start_marker` parts) were removed at once. `.sweep1.list` and `.sweep1.manifest` were moved into
  `evidence/sweep1/`.
- **Limits observed.** No git write, branch, PR, CI, GitHub call, network or URL fetch, publication or sub-agent.
  Git commands were read-only (`rev-parse`, `status`). Budget about 30 of the 100 minutes. Nothing is unfinished
  among the D assignments (what is not done is listed in §3).
