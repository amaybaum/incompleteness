# Thread D5 (BRIDGE-DERIVE) — stage 5 — running record

All clock times are UTC read from `date -u` at the moment of writing; none is estimated.

## N0 — start (16:44:15Z – 16:44:56Z)

- 16:44:07Z `pt/D5/` checked absent; created 16:44:15Z.
- Start checks (full output in `.start_marker`, assembled 16:44:35Z): 6/6 manifests OK
  (`inputs`, `stage1`, `inputs2`, `inputs3`, `stage2`, `inputs4`); `audit/stage3-inputs/ns.manifest.sha256`
  OK from its own directory (one line, `ns/NS-INPUT.md: OK`; nothing else read there); base HEAD
  `9f9f8257a980a1819fbbc1dc0019917cf8678626`, `status --porcelain` empty, no `__pycache__`/`.pyc` under
  `pt/base/`; the nine protocol files carry the expected sha256 prefixes and all nine sidecars verify
  (STAGE4, STAGE5, STAGE5-AMENDMENT-1 from SCRATCH; the other six from `pt/`); `pt/` top-level listing with
  mtimes recorded.
- Process deviation, recorded: `.start_marker` was written as two part files (`.start_marker.part1`,
  `.start_marker.part2`, both inside `pt/D5/`) and concatenated into `.start_marker` at 16:44:35Z; the parts were
  then removed. A transient `pt/D5/.chk` (capture of `sha256sum -c --quiet`) was created and removed during
  check (1). No file outside `pt/D5/` was written. `pt/C5/` did not exist at 16:44:07Z.
- Governing texts read in full, 16:44:40Z–16:44:56Z: `PROTOCOL-STAGE5.md`, `PROTOCOL-STAGE5-AMENDMENT-1.md`
  (working directory `pt/D5/`; sibling `pt/C5/`, never read), then `PROTOCOL-STAGE4.md`, `PROTOCOL-STAGE3.md`,
  `PROTOCOL-STAGE2.md`, `PROTOCOL.md`, `PROTOCOL-AMENDMENT-1.md`, `PROTOCOL-AMENDMENT-2.md`,
  `PROTOCOL-STAGE2-DS.md`.
- Prescribed records read 16:44:56Z–16:46:20Z, in order: `INTEGRATION-NOTE-STAGE4.md`, `audit/Y/AUDIT-Y.md`,
  `audit/Z/AUDIT-Z.md`, `Y/RESULT.md`, `Z/RESULT.md`, `INTEGRATION-NOTE-STAGE3.md`; ledgers `EQ2-SYNTHESIS.md`,
  `EQ3-P-RESULT.md`, `EQ3-AUDIT.md`, `EQ5-SOURCE-RESULT.md`, `EQ5-SOURCE-AUDIT.md`; the certified premise audit
  `round-kt4-prem-1-premise-audit/result.md`; `pt/base/AGENTS.md` (code-review rules :41–94, §A.31 :306–342,
  §A.21 :436–438). Not read: `pt/C5/`, `audit/stage3-inputs/OWNER-*`, `audit/stage4-inputs/OWNER-*`,
  `audit/stage5-inputs/`, `audit/reviews/`, `audit/aborted-launches/`.

## N0.1 — productivity test and plan (fixed 16:46:23Z, before the first node)

**Productivity test (§A.31, fixed now).** A node's finding is a gem iff it is strictly stronger than the obvious
restatement — the obvious restatement here being "the spectator clause is a hypothesis, so the bridge is
CONDITIONAL on it", which the protocol already says — AND it is one of: (1) an exact certificate at a stated
instance (a derivation with every step checked, or an exact countermodel with the candidate's transcription
verified exactly); (2) an exact obstruction for a stated class of routes (e.g. every principle stated on
single-token data alone, or every principle below the OI⁺ layer at L); (3) an exposed hidden assumption (a
kernel definition or manuscript sentence whose content differs from what the chain L0–L3 attributes to it, with
file:line). Otherwise record-only. Propagation bar: better than coherence relabelling.

**Decision rules for verdicts (fixed now).** DERIVED(P) only with [W + X] proof, P passing the disguise test, and a
recorded pressure test of the favourable branch. INDEPENDENT(P) only with an exact structure verified to satisfy P's
transcription, H1–H3 and the certified single-token structure, cone ≠ Q3 — or a kernel theorem cited with scope.
CONDITIONAL(P; A) with A named, A's status and A's disguise result. A failed derivation alone is UNRESOLVED, never
INDEPENDENT (amendment 2). A clause failing the disguise test is never called DERIVED.

**Plan (depth-first; decisive first).**
- N1 — L2 sourcing map at the matrix level (decides the shape of every verdict): read and quote at L the
  definitions and theorems the protocol names (ReferenceExtension, CompletedOI, ImplementationLocality,
  StructuralClosure, LiftAudit, DerivedQ3, ExecSource, ReadWriteControl, SubstratumInterface; GR.md, Main.md,
  ROADMAP). Sub-nodes: N1a which spectator clauses are theorems of the substratum class; N1b which are hypotheses
  of an extension; N1c whether `LayerFlowExecutable` at level 1 plus implementation locality /
  `HasParallelReferenceExtension` gives every level; N1d what `ImplementationLocality` (:370) says and what
  `observationalIndependence_of_implementationLocality` (:957) needs.
- N2 — candidates α, β, γ, δ: field-neutral transcription to the pair setting (W 3, K with H1–H3, actC/actT,
  body, NOT, flow, J); derivation attempt for (b_min); disguise test; outcome.
- N3 — candidates ε, ζ, λ, same treatment.
- N4 — exact scripts (python3 -I -B, sympy/Fractions; decision rule in the header before the first run):
  transcription of the single-token data from the Lean source (cnot, nflip, z3, J = cyc3, the drive's flow);
  the L3 link for the weakest sufficient field-neutral content ((b) for the flow and J; (b) for one off-frame
  rotation) with Q3 retention and stage-3-cone exclusion countercontrols; any exact countermodel a verdict needs
  (the pair-blindness of single-token principles, on K(E0) / K(Z_F)).
- N5 — whether any principle at L below the OI⁺ layer yields L2; weakest sufficient added content in both
  settings; hard-to-vary review; end checks; RESULT.md.

## N1 — the L2 sourcing map at the matrix level (16:46:44Z – 16:56:32Z; reads only, closed by citation)

Reads at L (all `pt/base/verification/lean-mathlib/OIBridge/` unless marked): ReferenceExtension.lean (all),
CompletedOI.lean (all), StructuralClosure.lean (all), ImplementationLocality.lean :1–130, :236–385, :840–1040,
LiftAudit.lean :1–260, DerivedQ3.lean (all), RouteB.lean :100–160, MicroscopicReversibility.lean :195–240,
SpectatorBridge.lean :176–236, ReferenceSufficiency.lean :750–760, ExecSource.lean :120–140,
ReadWriteControl.lean :165–182, SubstratumInterface.lean (declaration list), EmbeddedObservation.lean :93–130,
PhysicalCharacterization.lean :160–172, SecondOrderCircuit.lean :352–360, :708–716, KInfFoundations.lean :1–130,
:240–489, CompositeDimension.lean :1–240, :735–834; GR.md :205–275; Main.md :628; ROADMAP.md :66–70, :998–1035,
:1072–1095; design modules `pt/inputs/fourcopy/FourCopyDefs.lean` :25–55, `FourCopyPackage.lean` :165–190,
`FourCopyCore.lean` :156–158.

**What each spectator clause is, at L (quoted, with file:line).**
- `HasParallelReferenceExtension T` (ReferenceExtension.lean:447–451): "every available composite family stays
  available with any untouched finite spectator appended": `T.availExt n O F → T.availExt m O (fun a =>
  withSpectator R e (F a))` for every `e : R × (A × Fin n) ≃ A × Fin m`. A property of a
  `FiniteOperationalTheory A`, whose level-n carrier is `Matrix (A × Fin n) (A × Fin n) ℂ`.
- OI⁺-1 `ObservationalIndependence T := HasParallelReferenceExtension T` (CompletedOI.lean:129), equivalent to
  inert-spectator compositionality (:131–133 via SpectatorBridge.lean:233); it is one conjunct of `OIPlus`
  (:418–420); `oiPlus_independence` (:506–513): it fails on a theory with the core, well-formedness, reversible
  richness and observer recursion (the round-34 `countermodel`, :475–484). GR.md:228 states it ("an available
  operation remains the same operation when an untouched system is adjoined") as an added principle.
- Form is free, existence is the content: `isSpectatorExtension_iff` (SpectatorBridge.lean:188) and
  `form_fixed_existence_fails` (ImplementationLocality.lean:223).
- `ContextStable 𝓘` (ImplementationLocality.lean:359–361): `𝓘 S K → 𝓘 (R × S) (tensorOf 1_R K)` — the spectator
  clause at the level of implementation operators. `ImplementationLocality T` (:370–371) = `∃ 𝓘,
  ImplementationGenerated T 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘`; `ImplementationGenerated` (:352–355):
  availability at every positive level IS instrument realization by `𝓘`.
- `observationalIndependence_of_implementationLocality` (:957–960) needs `[Nonempty A]` and the three conjuncts;
  its proof is `parallel_of_implementationLocal hg hc hl` (:943–955), which uses `instAvail_withSpectator hc hl`
  (:820) and `availExt_zero` for level 0. So the spectator clause it delivers is exactly `ContextStable` of the
  generating class, transported through generation; nothing else in it is spectator content.
- Substratum class: `substratumClass := IsMonomial` (StructuralClosure.lean:180); `StructurallyClosed`
  (:183–187) = Architecture ∧ ContextStable ∧ LabelInvariant ∧ DaggerStable; THEOREM for the substratum class:
  `substratumClass_contextStable` (:261), `substratumClass_structurallyClosed` (:316). But it does not drive:
  `substratumClass_not_drivesElementary` (:370), `substratumGen_not_qm` (:359).
- HYPOTHESIS for an extension: `quantumArchitecture_iff_drives_of_closed` (:364–366) takes `hc : StructurallyClosed
  𝓘`; `substratum_extension_quantum_iff_drives` (:408–411) takes `ExtendsSubstratum 𝓘` and `hc :
  StructurallyClosed 𝓘`. GR.md:256 says so: "a structurally closed extension of the substratum class is a quantum
  architecture exactly when it drives … The controllability resource … entering as a hypothesis on the extended
  architecture".
- `LayerFlowExecutable T σ := ∀ (n : ℕ) (t : ℝ), T.availExt n Unit (fun _ => conjChannel (gateFlow (levelPerm σ n)
  t))` (LiftAudit.lean:112–113), `levelPerm σ n = σ.prodCongr (Equiv.refl (Fin n))` (:51–52) "the ancilla is a
  spectator". GR.md:262: "the continuous layer flow … the ancilla a spectator, is an available operation at every
  level and every intermediate time". Endpoint `derivedOI_qm_iff_layerFlowExecutable'` (DerivedQ3.lean:222–226)
  under `hd : DerivedOI T`.
- `DerivedOI T := ReversibleImplementationLocality T ∧ EmbeddedObservation T ∧ ExchangesAvailable T ∧
  PhasesAvailable T ∧ ReadWriteAvailable T` (RouteB.lean:141–143); `ReversibleImplementationLocality T := ∃ 𝓘,
  ImplementationGenerated T 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘 ∧ DaggerStable 𝓘` (MicroscopicReversibility
  .lean:223–225); `DerivedOI.implementationLocality` (RouteB.lean:149–151).
- L1 at the matrix level is not sourced, already at level 1: `configurationLevel_not_layerFlowExecutable`
  (LiftAudit.lean:183–196) uses only `hex 1 (1/2)` (:187); `substratumTheory_not_layerFlowExecutable` (:200);
  `obs_not_layerFlowExecutable` (ExecSource.lean:129); `readWriteSourced_not_qm` (ReadWriteControl.lean:174).

**N1a — spectator clauses that are theorems of the substratum class.** Exactly one family: `ContextStable
substratumClass` (StructuralClosure.lean:261, :316), hence (via ImplementationLocality.lean:943, :957, with the
monomial class generating `substratumTheory`) observational independence of the substratum theory. These hold for
monomial operators only. Verdict: [K], scope = monomial class on the complex matrix carrier.

**N1b — spectator clauses that are hypotheses of an extension.** `hc : StructurallyClosed 𝓘`
(StructuralClosure.lean:365, :409) — its `context` field for a class containing a driving (non-monomial)
operator; `DerivedOI T`'s `ContextStable 𝓘` (RouteB.lean:141 → MicroscopicReversibility.lean:224) for any `T`
that executes a drive at level 1 (its generating class realizes the drive, so it is not configuration-level,
LiftAudit.lean:183); the ∀-level clause of `LayerFlowExecutable`; OI⁺-1 itself (CompletedOI.lean:419).

**N1c — does `LayerFlowExecutable` at level 1 plus implementation locality / HasParallelReferenceExtension give
every level? YES [W over K; exact identity to be checked in N4, script d2].** Argument: given `hP :
HasParallelReferenceExtension T` and level-1 executability `∀ t, T.availExt 1 Unit (conjChannel (gateFlow
(levelPerm σ 1) t))`: for n = 0 use `availExt_zero` (PhysicalCharacterization.lean:164); for n ≥ 1 apply `hP`
with `R = Fin n`, `e_n : Fin n × (S × Fin 1) ≃ S × Fin n`, `(r, (s, 0)) ↦ (s, r)`; by
`withSpectator_conjChannel` (ReferenceSufficiency.lean:754) the extended family is `conjChannel (reindex e_n e_n
(1_n ⊗ gateFlow (levelPerm σ 1) t))`, and the identity `reindex e_n e_n (1_n ⊗ gateFlow (levelPerm σ 1) t) =
gateFlow (levelPerm σ n) t` holds because `gateFlow g t = unit (permMat g) t = 1 + (exp(iπt) − 1)·(1 − g)/2`
(SecondOrderCircuit.lean:352–357, LiftAudit.lean:47–48) is affine in `g` with `1 ↦ 1`, and `reindex e_n e_n (1_n ⊗
permMat (levelPerm σ 1)) = permMat (levelPerm σ n)` (`permMat σ x y = [σ y = x]`, SecondOrderCircuit.lean:710).
Consequence (gem candidate, type 3, exposed assumption): **within `DerivedOI`, the "every level" of
`LayerFlowExecutable` is redundant** — `DerivedOI T` gives `ImplementationLocality T` (RouteB.lean:149), hence
`HasParallelReferenceExtension T` (ImplementationLocality.lean:943), hence every level from level 1. So the
spectator clause of the layer-flow form (GR.md:262 places it in the resource: "the ancilla a spectator … at every
level") is already carried by the closure `DerivedOI`, through `ContextStable` of a class that, for any `T`
executing the flow at level 1, must realize the flow — a hypothesis about an extended class, not a property the
substratum supplies (the monomial class cannot realize the flow at level 1, LiftAudit.lean:187). Pressure test
(favourable-to-economy branch): the redundancy does not shrink the resource below "level-1 flow + spectator
stability of a class realizing it"; it relocates the spectator clause, it does not remove it.

**N1d — what ImplementationLocality says and what :957 needs.** Stated above: `∃ 𝓘, ImplementationGenerated T 𝓘 ∧
ContextStable 𝓘 ∧ LabelInvariant 𝓘` (:370); :957 needs `[Nonempty A]` and that conjunction, no more (proof
:958–960 → :943–955). The only spectator content is `ContextStable 𝓘` = "admissible K ⇒ admissible 1_R ⊗ K"; the
carrier makes `1_R ⊗ K`'s conjugation a valid (CP) map automatically (`conjChannel_referencePositive`,
ReferenceExtension.lean:182), so on the matrix carrier the clause carries no state-space content.

**N1e — exposed assumption, the decisive one for the field-neutral transcription (gem candidate, type 3).** Every
spectator clause above is a property of a `FiniteOperationalTheory A`, whose level-n state space is the PSD cone of
`Matrix (A × Fin n) (A × Fin n) ℂ`: the composite is the complex tensor product with the quantum cone by
construction (ROADMAP.md:68: K is "from field-neutral operational premises to the complex matrix kinematics the
finite characterization assumes", OPEN). On that carrier the spectator extension of a conjugation is a conjugation
(ReferenceSufficiency.lean:754) and preserves PSD for every R (ReferenceExtension.lean:182). So the matrix-level
theorems (N1a) and hypotheses (N1b) are about availability/admissibility of operations on a composite whose cone is
already Q3; none of them is about which pair cone K ⊆ W 3 a token's operations preserve. Transcribed to the
field-neutral pair (W 3, K free, H1–H3), each becomes the composite action (b) for its class of operations, and
none of them is certified there (K2 "local actions compatible with it", ROADMAP.md:1004, OPEN). In particular the
one spectator THEOREM at L (N1a) transcribes to (b) for the monomial class — to be tested exactly in N4 (is it even
sufficient?).

## N2 — exact script d1_bridge.py (written 16:56:40Z–17:00:54Z; decision rules in its header, fixed before run 1)

Scope: transcription controls (A), the L3 Lie closure for (b_DJ) with countercontrols (B), the field-neutral
transcription of the substratum (monomial) class and an exact unreachable seed (C), a λ countercontrol (D), the
native-gate relations against (b) for the NOT (E), and ζ's drivability transcription on K(Z_F) (F). No pre-run
edits after the header was fixed. sha256 before run 1: dc1e885a8a334e6cef721afa8faad5cb878f8f030a2c47bcc8b62fc817d53bbe.
- d1 run 1 at 17:01:16Z: 26/26 PASS, `VERDICT D1-BRIDGE-EXACT`, exit 0, stderr empty (5.1 s; the timing was
  captured in a transient `pt/D5/d1_time.tmp`, removed at once; no timing in stdout). No failed run.

## N3 — exact script d2_levels.py (written 17:01:21Z–17:02:01Z, file mtime; rules in header, fixed before run 1)

Scope: the matrix identity that carries node N1c (level-1 layer flow + spectator extension = level-n layer flow),
with two countercontrols and sanity/unitarity controls. No pre-run edits after the header. sha256 before run 1:
5b4aeaca0b0131147ec9f62f8ce9abece96266541e1492d38911271b8acd33f6.
- d2 run 1 at 17:02:10Z: 5/5 PASS, `VERDICT D2-LEVELS-EXACT`, exit 0, stderr empty. No failed run.

## N4 — exact script d3_weakest.py (written 17:05:25Z, file mtime; rules in header, fixed before run 1)

Scope: the field-neutral counterpart of "substratum class + one drive": Lie closures with cnot for the drive (axis
x, the NOT's axis) together with the substratum phase flow (axis z) on one token, and countercontrols. No pre-run
edits. sha256 before run 1: b21f37f8c250d5c4040284a2e787d2c5fa8c65817f9cd9edbaf07e663220c13e.
- d3 run 1 at 17:05:33Z: 6/6 PASS, `VERDICT D3-WEAKEST-EXACT`, exit 0, stderr empty. No failed run.

## N5 — candidates, transcriptions, derivation attempts, disguise tests (17:05:40Z–, [W] over N1–N4)

Notation: (b)[G] = "every element of G, acting on one token by actC/actT, maps K into K"; W 3, H1–H3, closed K.
Field-neutral single-token data at L: body `eball 3`; NOT `nflip = R_x(π)` (CompositeDimension.lean:797; d1 A2);
corner axis z3 (:793); drive = the flow through the NOT about its axis x (`ElementaryDrivability`,
KInfFoundations.lean:264, a hypothesis, K∞-Drive OPEN ROADMAP.md:1017); J = cyc3 (:416–425, `ball3Drive` :449;
d1 A3: J e_x = e_y, so J·flow·J⁻¹ = R_y(t)). The substratum class transcribes to O(2) about z (d1 C1).

- **α (OI⁺-1).** Matrix: `ObservationalIndependence := HasParallelReferenceExtension` (CompletedOI.lean:129;
  ReferenceExtension.lean:447). Transcription: available single-token O ⇒ actC O, actT O available on the pair,
  available = K-preserving. Form exact (W 3's actC is the unique linear extension acting as O on products, the
  analogue of `isSpectatorExtension_iff`, SpectatorBridge.lean:188; d1 A4 identifies actC R(U) = Ad(U⊗I));
  availability by analogy (on the matrix carrier validity is automatic, ReferenceExtension.lean:182). So α_FN =
  (b)[available single-token operations]. Derivation: α_FN + L1 (flow, J available on a token) ⇒ (b_DJ) ⇒ [d1 B1
  dim 6 + stage-4 Y2 reachability, audited] K = Q3. Disguise: FAILS (α is the spectator clause). Outcome:
  CONDITIONAL(α; L1 = K∞-Act/K∞-Drive availability of the flow and J, OPEN), the bridge resting on α itself.
  α's sourcing: matrix — added OI⁺ principle (GR.md:228), independent of core + other conjuncts (kernel
  `oiPlus_independence`, CompletedOI.lean:506; `redundancy_fails`, ImplementationLocality.lean:207);
  field-neutral — K2 "local actions compatible with it" OPEN (ROADMAP.md:1004).
- **β (implementation locality).** Matrix (:370): generation ∧ ContextStable ∧ LabelInvariant; :957 needs only that
  and `[Nonempty A]`. Transcription: classes 𝓘₁ (token maps), 𝓘₂ (pair maps); generation (pair availability =
  realization by 𝓘₂, available ⇒ K-preserving); ContextStable: O ∈ 𝓘₁ ⇒ actC O, actT O ∈ 𝓘₂ (exact form, d1 A4);
  label invariance (token relabelling, SWAP). β_FN ⇒ (b)[𝓘₁]. Disguise: FAILS through ContextStable (the
  protocol names it). β minus ContextStable is INDEPENDENT [W]: take 𝓘₂ = the automorphisms of K(Z_F) (closed under
  composition, inverses, SWAP — K(Z_F) is SWAP-invariant, stage-4 Z z1), 𝓘₁ = body automorphisms; generation and
  label invariance hold by construction; K(Z_F) ≠ Q3 with H1–H3 (stage 3, audited). Outcome: CONDITIONAL(β;
  ContextStable of a class containing the flow and J, plus L1). Sourcing of ContextStable: theorem for the monomial
  class (StructuralClosure.lean:261); hypothesis for every class realizing the drive (N1b).
- **γ (structural closure).** Theorem for the substratum class (StructuralClosure.lean:316); hypothesis for an
  extension (:365, :408). Only "stable under an uncoupled spectator" links token and pair operations (disguise
  FAILS there; the other clauses — composition, coarse-graining, ancilla blocks, relabelling, adjoint — are closure
  properties satisfied by Stab(K(Z_F)), a closed group [W]). (i) γ for the substratum class, transcribed: (b) for
  every monomial pair operation (incl. actC/actT of O(2)_z, CNOT, SWAP) and the transpose: INSUFFICIENT — d1 C2–C3:
  φ₀ = (1,2,3,4)/√30 is unreachable (min |det| over the 24 magnitude arrangements = 1/15 > 0; [W]: phases are free
  under the diagonal torus, so the best overlap with D·P(a⊗b) is σ_max² of the 2×2 arrangement, = (1 + √(1 −
  4det²))/2), and c = 513/512 lies in the window (1, min(2, 1/m)]; by the audited dichotomy (stage-4 Y1, Z claim D)
  an exotic invariant K exists: INDEPENDENT(γ_substratum) with an exact seed (EXOTIC-E). Even this transcription is
  not certified at L: K(Z_F) is moved by every one-parameter group of local maps (stage-4 Z z1, audited), hence by
  actC R_z(φ). (ii) γ for an extension: CONDITIONAL(γ_ext; spectator stability of the extended class + L1).
- **δ (layer flow).** Matrix: ∀ level ∀ time (LiftAudit.lean:112); the ∀-level clause is the spectator extension of
  the level-1 flow (N1c; d2 L1 exact; countercontrols L1c, L1c2) and is redundant inside `DerivedOI`, which carries
  it through ContextStable (N1c). Level-1 restriction: not supplied by the substratum, already at level 1
  (LiftAudit.lean:187). Transcription: σ = the NOT; its flow = the drive R_x(t); "the ancilla a spectator, every
  level" = actC/actT of the drive preserving K. δ_FN (native drive only) ⇒ (b)[drive] only: Lie closure with cnot
  dim 2 (control) / 1 (target) (d1 B1c, B2c; d3 W2c); EXOTIC-E by stage-4 Y4 (exact seed c = 4609/4608, audited):
  INDEPENDENT(δ, native drive). δ restricted to level 1: single-token availability = L1, pair-blind (below):
  INDEPENDENT. δ over every native involution (the NOT and its J-conjugates) or with the substratum phase flow on the
  same token: ⇒ (b) for an su(2) on one token (d1 B1, d3 W1/W4: dim 6) ⇒ Q3: CONDITIONAL(δ; J or the phase flow
  available on the token, plus the ∀-level clause), disguise FAILS (the ∀-level clause is the spectator clause).
  LayerFlowExecutable at level 1 + implementation locality / HasParallelReferenceExtension gives every level: YES
  (N1c), but the added content is a spectator clause, so no reduction.
- **ε (substratum locality).** Main.md:628: dynamical causal separation "does not alone establish statistical
  product structure after conditioning, local tomography, or one common tensor-product instrument category. … The
  common local quantum composite/instrument structure is the content of the inert-spectator and
  iterated-composition conditions". Transcription (no-signalling): (actC O ω)_{0ν} = ω_{0ν} for every linear O
  (homMap fixes coordinate 0, CompositeDimension.lean:112–113, :201–202) — an identity of the carrier, true for every
  K, so it constrains no cone: INDEPENDENT [W + stage-3 cones]; disguise: passes (no preservation clause). ε's
  "spectator stability of the substratum-source form" (GR.md:256) = γ(i): INDEPENDENT (d1 C).
- **ζ (observer recursion / embedded observation).** Matrix: `ObserverRecursion` (CompletedOI.lean:327),
  `EmbeddedObservation` (EmbeddedObservation.lean:123) supply iterated composition, not inert spectators — kernel
  scope statement: `redundancy_fails` (ImplementationLocality.lean:207: validity + reversible richness + embedded
  observation ⇏ observational independence; matrix carrier, all operations). Transcription: the pair body (slice
  ω00 = 1 of K) is itself a system with the single-system structure — drivability (ElementaryDrivability of the
  pair body) and transitivity. Drivability form: K(Z_F) satisfies it (d1 F1–F3: Bell-diagonal flow U(w) fixes every
  defect; U(−1) an involution moving a pure state of K(Z_F); J = Ad(X⊗I) permutes Z_F and is off-axis; F6c control)
  and fails (b_DJ) (d1 B3b): INDEPENDENT(ζ-drive) [X + W + stage-3 H1–H3 of K(Z_F)]. Literal transitivity
  (BoundaryTransitive, OrbitGeneration.lean:79) fails for Q3 itself (TransitiveBody.lean:301 + W, stage-4 Y O):
  not retained. Extreme-ray transitivity = stage-4 node T: EXCLUDES-KNOWN, EXCLUDES-ALL UNRESOLVED. Disguise: passes
  (pair-level automorphisms, no single-token action). Outcome: INDEPENDENT (drivability form); transitivity forms
  not retained (literal) or UNRESOLVED (T).
- **λ (KT(4) with tok).** Transcription exact (natively on W 3 tables). Derivation (record): EQ3 [W + X, base
  bcbc516f, audited 29/29] and `kt4_forward_ie1` (design run [D], recorded at L by KT4-PREM-1 result.md:17–22,
  :186–192): hcls ∧ hadm ∧ hcl ∧ hgate ∧ H ⇒ IE1 at every pair; with uniform K, aligned gates exactly cnot (hcls
  holds trivially, KT4-PREM-1 M_cl.1), hadm from H1 + H3 (K ⊆ SEP* = maxCone), hcl the setting, hgate = H2: λ ⇒
  IE1 ⊇ (b_S4) ⇒ Q3. Disguise: PASSES as written (four-copy body, product states and effects across two
  groupings, token identity; no operation on part of a composite — EQ3-AUDIT §2 item 4). Pressure test (favourable
  branch): (1) d1 D: uniform K(E0) violates λ (family-(i) value −1 at gate-supplied effects, reproducing the
  stage-3 record); d1 Dc: the Q3 control is ≥ 0. (2) Content: relative to hadm λ ⟺ FCC (EQ5-SOURCE §3.6, two
  witnesses); FCC's family (ii) "L·f·L'ᵀ ∈ K" is, by the four-copy table identity, closure of K under the
  index-wise maps encoded by its own elements, which through the gate's links are local filters and rotations (EQ3
  §1, C2, p3): the composite action is produced by conditioning across groupings, not assumed — and stage 2's
  renaming test lists exactly this cross-grouping positivity as FCC's own content (PROTOCOL-STAGE2.md:77–78).
  (3) Relative to uniform pair premises λ ⟺ IE1 (EQ3-AUDIT §4) — not by itself a disguise, since every retained
  sufficient P is equivalent to K = Q3 given H1–H3. (4) Sourcing: no structure with three or more tokens at L
  (EQ5-SOURCE §1; ROADMAP Kₙ OPEN); tok has no source (EQ5-SOURCE row 9). Outcome: DERIVED(λ) in the protocol's
  sense, at [D + W + X] (no re-derivation at L beyond d1 D/Dc), with λ unsourced at L and strictly stronger than
  (b_min) (it yields IE1 on both tokens).

**Below the OI⁺ layer at L (the protocol's last question): no principle yields L2.** [W + X] (gem, type 2: exact
obstruction for a stated class). (i) Single-token principles — K∞-Stage, K∞-Act, K∞-Drive, K∞-Trans, K∞-Seed,
K∞-V4, K∞-Geom (ROADMAP.md:1010–1033), CopyNatural (KInfFoundations.lean:284) — quantify over one body, its
effects, its operation data and the copies' NOTs; none mentions a pair cone, so every K with H1–H3 carries the same
single-token data: the stage-3 cones satisfy them with Q3's single-token structure and fail (b_DJ) (d1 B3a, B3b).
(ii) Native-gate relations relT, relC (CompositeDimension.lean:224–225): identities of linear maps on W 3 (d1 A5),
K-independent; K(E0) satisfies H2 and is moved by actC nflip (d1 E) — the relations do not give (b) even for the
NOT; K(Z_F) is moved by actC J (d1 B3b). (iii) Observer recursion: ζ above. (iv) Causal separation: ε above.
(v) The one spectator THEOREM at L (substratum class) transcribes to monomial (b), insufficient (d1 C).

**Weakest sufficient added content.** Field-neutral: (b) for two non-commuting one-parameter rotation groups of
ONE token — the drive with its J-conjugate (d1 B1), or the drive with the substratum phase flow about z (d3 W1,
W4) — or stage 4's single off-frame rotation (R1) / generic axis (S3[n]); each single family alone is insufficient
(d1 B1c/B2c, d3 W1c/W2c/W3c; stage-4 Y4). Matrix: beyond the substratum class (structurally closed, theorem) and
L1 (the drive at level 1): the drive's spectator stability (1_R ⊗ its implementation admissible, every R) —
equivalently, given level 1, `LayerFlowExecutable` at every level (N1c, d2). Relation to OI⁺-1: in both settings
the added content is the instance of OI⁺-1 for the drive (and, field-neutrally, one off-frame partner) — strictly
smaller than OI⁺-1, not derived from anything at L. Relation to the layer-flow hypothesis: it is exactly
LayerFlowExecutable's ∀-level clause (matrix); field-neutrally the layer flow of the NOT alone is insufficient —
the matrix theorem succeeds with one flow because `DerivedOI` adds the phases at every level, whose field-neutral
counterpart is the phase flow on the same token (d3 W1). Minimality is not claimed.

**Fixed point.** Passes N1 (NEW: N1c redundancy; N1e carrier exposure), N2 (NEW: monomial obstruction, ζ
countermodel), N3 (CONFIRMING N1c), N4 (ELABORATING: phase+drive parallel), N5 (no NEW beyond N1–N4). Stopped at
the question answered, before 3–4 null passes; recorded as such.
N5 closed 17:06:38Z.

## N6 — replays and the anomaly sweep (17:06:53Z–17:08:48Z)

- Replays 17:06:53Z–17:07:02Z: d1, d2, d3 into `<name>.replay.{out,err}`; `cmp` of stdout and stderr: 3/3
  IDENTICAL. No `__pycache__`/`.pyc` under `pt/D5/`.
- **Anomaly (§A.26).** At 17:07:10Z the `pt/` top level showed entries newer than `.start_marker` outside `D5/`,
  `C5/`, `audit/`, `audit*-replay/`: `PROTOCOL-STAGE6.md` (16:49:36Z), `PROTOCOL-STAGE6.sha256` (16:49:55Z), and
  directories `I1`–`I4` (start markers 16:51:44Z–16:53:28Z, files still being written at 17:08Z: thread-like
  directories with NOTES, scripts, `INVENTORY.md`). Not written by this thread; not named in the protocol or the
  launch message. Full file-level sweep 17:08:20Z: 77 files + 4 directories (`evidence/sweep1/LIST.txt`,
  `MANIFEST-at-sweep.txt`: mtime, size, sha256; hashing only, no content read or displayed).
- **Sweep slip, recorded.** A first sweep command at 17:07:48Z had a wrong `find` expression (`-newer` bound to the
  pruned branch only), so it listed and hashed every non-excluded file under `pt/` (names and hashes only; `C5/`,
  `audit/`, `audit*-replay/` pruned). Its output was saved by the tool runner to a tool-results file outside `pt/`
  (not redirected there by any command of mine). Its list file `pt/D5/.sweep1.list` was overwritten by the correct
  sweep at 17:08:20Z.
- **Quarantine.** Byte copies (`cp -p`) of all 77 files into `evidence/sweep1/files/` at 17:08:37Z, originals left
  in place and untouched: moving them would write outside `pt/D5/` (forbidden) and remove files an active writer is
  using; "never delete" is honoured. `COPY-MANIFEST.txt` gives copy-time hashes; one file (`I2/INVENTORY.md`) changed
  between sweep and copy. `README.txt` states all this.
- **Bearing on the results.** The decisive scripts ran 17:01:16Z–17:07:02Z, after the anomalous writer began
  (16:49:36Z) and before detection (17:07:10Z). Their only inputs are two Lean files under `pt/base/`
  (CompositeDimension.lean, KInfFoundations.lean), which the end checks below verify unchanged (base HEAD, empty
  porcelain, manifests). No anomalous file is an input to anything in this thread. Per §A.26 no further
  measurement is run; the remaining work is the end checks and the write-up of results already obtained, with the
  anomaly reported for the coordinator's attribution.

## N7 — end checks, hard-to-vary review (17:09:20Z–)

- `.end_marker` (17:09:20Z): 6/6 manifests OK; ns manifest OK (from its own directory); base HEAD
  `9f9f8257a980a1819fbbc1dc0019917cf8678626`, porcelain empty; no `__pycache__`/`.pyc` under `pt/base/` or
  `pt/D5/`; nine protocol prefixes and nine sidecars OK; top-level listing recorded. Sweep 2: the same anomaly set as
  sweep 1 (`PROTOCOL-STAGE6.md`, `.sha256`, `I1`–`I4`, the directories still growing); no new class of entry;
  `C5/` and `audit/` present (excluded, names only).
- **Hard-to-vary review.** Preserved results (controls): Q3 retention (d1 B4, Dc); every exclusion claimed for the
  stage-3 cones fails on them exactly (d1 B3a −1, B3b −1/2, D −1, E −1); transcription controls A1–A5 with
  countercontrols A1c, A2c, A4c; d2 countercontrols L1c, L1c2; d3 countercontrols W1c, W2c, W3c. Predictions
  beyond the problem, written before their checks: N1c (written 16:56:32Z) predicted the level identity that d2
  then confirmed (17:02:10Z); the monomial obstruction (C2–C3) was predicted EXOTIC by the dimension count in the
  header before run 1; d3's phase-plus-drive closure (W1, W4) was predicted from the matrix endpoint's use of the
  phases. Not adjustable: c = 513/512 and every dimension rule fixed in headers; no rule changed after a run; no
  failed run. Skepticism on favourable branches: λ (four pressure points, N5), N1c (relocates the spectator clause,
  does not remove it), ζ-transitivity (literal form not retained; T form left UNRESOLVED, not counted).
- What remains unfinished: none of the protocol's D-assignments is open; not done (outside budget, recorded in
  RESULT §3): a re-derivation at L of EQ3's four-copy route (λ rests on [D] + audited [W + X]); minimality of the
  weakest content.

## N8 — write-up (17:09:37Z–17:12:41Z); NOTES frozen

RESULT.md §0–§3 written 17:09:37Z–17:12:27Z; anchors re-verified at 17:12:34Z (FourCopyDefs.lean:31, 34, 49;
FourCopyPackage.lean:176, 180, 183; CompletedOI.lean:327, 418; EmbeddedObservation.lean:123). This file is frozen
at 17:12:41Z; its sha256 and those of every other file written by this thread are in RESULT §4; RESULT.md's own hash is in
the final report. No script run after 17:07:02Z; no file outside `pt/D5/` written.
