# Integration note — stage 5 (Q-EX-BRIDGE: observer-native origin of off-frame reversible mixing)

Research only, at base L = `9f9f8257…`. Governing texts `PROTOCOL-STAGE5.md` (`9e01f098…`) and
`PROTOCOL-STAGE5-AMENDMENT-1.md` (`1f639115…`). Threads: D5 (derivation side, `pt/D5/`, audited
`pt/audit/D5/AUDIT-D.md`) and C5 (countermodel side, `pt/C5/`, audited `pt/audit/C5/AUDIT-C.md`). Pre-audit
facts: `pt/audit/stage5-inputs/PRE-AUDIT-BRIDGE.md` (7/7). Evidence levels: [K] certified at L, [D] design module,
[W] written argument, [X] exact computation, [U] unsourced. Written 2026-10-10 after both audits.

## 0. Verdict

**No principle present at L derives the composite action (b).** Stage 4 left (b) — "the native reversible
single-token operations, idle-extended to one token of the pair, preserve the pair cone" — as the one missing
implication; stage 5 asked whether a genuinely observer-native principle at L justifies its weakest sufficient
form without assuming it in disguise. The answer, in the protocol's three outcomes:

| candidate (principle at L) | field-neutral transcription | outcome | basis |
|---|---|---|---|
| α — OI⁺-1, observational independence (`HasParallelReferenceExtension`) | (b) for every available single-token operation | **CONDITIONAL** on α itself, plus L1 (availability of the flow and J) | α is the spectator clause; fails the disguise test; added principle at L (GR.md:228), independent of the core and the other OI⁺ conjuncts (`oiPlus_independence`) |
| β — implementation locality (`ImplementationGenerated ∧ ContextStable ∧ LabelInvariant`) | (b) for the generating class | **CONDITIONAL** on `ContextStable` of a class containing the flow and J, plus L1; β minus `ContextStable` is INDEPENDENT (Stab K(Z_F)) | `ContextStable` is a theorem for the monomial class only (StructuralClosure.lean:261) and a hypothesis for every class realizing a drive |
| γ — structural closure | for the substratum class: (b) for monomial pair operations; for an extension: spectator stability of the extended class | substratum class: **INDEPENDENT** (exact seed `c = 513/512` at `φ₀ = (1,2,3,4)/√30`, EXOTIC-E); extension: **CONDITIONAL** | D5 C1–C3, coordinator check C1–C6: the monomial orbit of the products has rank-1 magnitude patterns, `φ₀` has none (min arrangement det 1/15) |
| δ — layer flow (`LayerFlowExecutable`, ∀ level ∀ time) | (b) for the drive; with the phases, (b) for drive + phase flow | native drive alone: **INDEPENDENT** (EXOTIC-E, `d_low = 1/2304`, stage-4 Y4's `c = 4609/4608`); with J or the phase flow on the same token: **CONDITIONAL** on the ∀-level clause | the ∀-level clause is the spectator clause; inside `DerivedOI` it is redundant given level 1 (D5 N1c, exact identity d2 / coordinator G1–G2) |
| ε — substratum locality / causal separation | no-signalling identity of the carrier | **INDEPENDENT** | an identity true of every K (row 0 fixed by `actC`); Main.md:628 says the same |
| ζ — observer recursion / embedded observation | the pair body is itself a drivable system (pair-level `ElementaryDrivability`) | drivability form: **INDEPENDENT** (K(Z_F) carries a pair drive and fails (b_DJ)); literal transitivity not admissible (Q3 fails it); extreme-ray transitivity **UNRESOLVED** (stage 4's T) | D5 F1–F3, C5 ZETA-1/2, coordinator F0–F3 / K5; `redundancy_fails` at the matrix level |
| η — native-gate relations, copy naturality | `relT`, `relC`; NOT preserves K; copies' NOTs agree | **INDEPENDENT** (K(Z_F), EXOTIC-X; K(E0) at level (i) for η-a) | identities of linear maps; K(Z_F) is invariant under both NOTs and SWAP |
| θ — steering / conditional-state admissibility | `K ⊆ maxCone`, no-signalling | **INDEPENDENT** (implied by H1–H3; K(Z_F), K(E0)) | the defects steer to pure states; θ does not give H2 |
| ι — token exchange | SWAP preserves K | **INDEPENDENT** (K(Z_F); `⟨G16, SWAP⟩` of order 48) | |
| κ — the gate's own flow `U(w)` | K invariant under `Ad U(w)` with G16 | **INDEPENDENT** (EXOTIC-E over the Bell seed on the invariant circles); explicit cone UNRESOLVED | K(Z_F) is not κ-invariant |
| α–δ restricted to the NOT; to NOT + J; to native finite groups; to the drive alone (one or both tokens) | spectator stability for that class only | **INDEPENDENT** in every case (K(Z_F) for the NOT; exact seeds `d_low = 5/256` or `1/2304` otherwise) | C5 census, coordinator L1–L12, O4–O6, S1–S6 |
| λ — KT(4) with `tok` (four-copy coherence) | exact on `W 3` tables | **DERIVED at [D + W + X] relative to λ**; λ itself **unsourced at L** ([U]: no three-token structure, `tok` without source) | `kt4_forward_ie1` is a design-run theorem (KT4-PREM-1 record), λ ⇒ IE₁ ⇒ (b_S4) ⇒ Q3; disguise test passes (EQ3-AUDIT §2 item 4); λ without `tok` is INDEPENDENT of (b_min) (anchor sum with K(Z_F)) |

**Bottom line.** Every candidate that yields (b) contains (b) for its class as a spectator clause (α, β, γ for an
extension, δ's ∀-level clause) — which at L is a hypothesis of every extension and a theorem only for the monomial
class, where its transcription is insufficient. Every candidate that does not contain such a clause is satisfied
by an exotic cone (the explicit K(Z_F), or an existence seed). The one derivation available, from λ, relocates the
gap to λ's own sourcing. So the stage-4 conditional classification stands as stated: (b) is a premise that the
certified framework does not supply.

## 1. The dependency chain at L

- **L0 (substratum).** Monomial interventions, structurally closed (`substratumClass_structurallyClosed`, [K]).
  Transcribed to `W 3` by analogy only; the native gate is a signed permutation of the sixteen table entries.
- **L1 (single-token availability).** The continuous drive is not sourced at any level (`substratumTheory_not_
  layerFlowExecutable`, `obs_not_layerFlowExecutable`, `readWriteSourced_not_qm`, [K]); field-neutrally,
  K∞-Act/K∞-Drive are OPEN (ROADMAP.md:1014–1017). `U_J` is not monomial. Status: OPEN hypothesis.
- **L2 (composite action).** Not supplied by any principle at L (table above). The matrix-level spectator
  clauses live on `Matrix (A × Fin n)` with the PSD cone, where the composite is the tensor product by
  construction and the spectator extension of a conjugation is always valid; transcribed to the pair they become
  (b) for their class. No theorem at L connects the matrix carrier to `W 3` (stage-6 inventory threads I3, I4;
  coordinator import-graph check: only the root aggregator reaches both). Status: hypothesis of the extension
  results; obligation K2 "local actions compatible with the composite cone" (ROADMAP.md:1001–1005, OPEN).
- **L3 (stage 4).** Given L1 and L2 for {flow, J} on one token (either), Q3 is forced [W + X, audited]; given
  them for any proper native subset, an exotic invariant cone exists. The minimal native content is exactly
  {flow, J} (or the flow on the control with J on the target). Matrix level: the drive's spectator stability given
  its level-1 availability (equivalently `LayerFlowExecutable` at every level).

## 2. Weakest sufficient added content

- **Field-neutral:** (b) for two non-commuting one-parameter rotation groups of one token — the drive with its
  J-conjugate (D5 B1; C5 census; coordinator B1, L7/L8), or the drive with the substratum phase flow about z (D5
  d3; coordinator B5, B7). Each family alone is insufficient (exact seeds). Minimality within the native
  repertoire holds for the first pair (C5 census); minimality in general is not claimed (stage 4's single
  off-frame rotation subgroup and single order-3 rotation are smaller but not native operations).
- **Matrix:** beyond the structurally closed substratum class and the level-1 drive, the drive's spectator
  stability (`1_R ⊗ K` admissible for every finite `R`), equivalently `LayerFlowExecutable` at every level given
  level 1. Inside `DerivedOI` this clause is carried by `ContextStable` of the generating class (D5 N1c).
- **Relation to OI⁺-1:** in both settings the added content is the instance of OI⁺-1 for the drive (and, field-
  neutrally, one off-frame partner) — strictly smaller than OI⁺-1, not derived from anything at L.
- **Relation to the layer-flow hypothesis:** it is exactly the ∀-level clause (matrix); field-neutrally the layer
  flow of the NOT alone is insufficient because the matrix endpoint also uses the phases at every level, whose
  counterpart is the phase flow on the same token.

## 3. Exposed assumptions (record for stage 6)

1. The ∀-level quantifier of `LayerFlowExecutable` is redundant inside `DerivedOI` (level 1 plus
   `HasParallelReferenceExtension` gives every level; exact identity `reindex e_n (1_n ⊗ gateFlow(levelPerm σ 1) t)
   = gateFlow(levelPerm σ n) t`). The spectator content is relocated to `ContextStable`, not removed.
2. Every matrix-level spectator clause presupposes the tensor-product composite with the quantum cone; `pauliW`,
   `Q3`, `dualW` are not kernel objects at L (design modules only), so the dictionary between `W 3` and complex
   matrices used by stages 3–5 is itself uncertified.
3. The protocol's "flow through the NOT" (rotations about `nflip`'s axis x) is the `cyc3`-conjugate of the
   certified `ball3Drive` flow (rotations about z), whose own NOT `rot3 π = diag(−1,−1,1)` fixes the corner axis and
   is not `nflip`. The two NOTs are unrelated in the kernel.
4. Mixed placement is asymmetric: the flow on the control with J on the target generates `su(4)`; the flow on the
   target with J on the control stays one-dimensional (EXOTIC-E).
5. `M_ρ` and `M_tw` (the `tok` countermodels) satisfy (b); they refute only the parity part. The λ-without-`tok`
   countermodel is the anchor sum with K(Z_F).
6. The single spectator theorem at L (monomial class) transcribes to an insufficient (b): the substratum's own
   structural closure does not reach quantum composition even granted the transcription.

## 4. What stays open

- An explicit κ-invariant exotic cone (existence only, by EBF over an exact seed).
- Whether extreme-ray transitivity (stage 4's T) excludes every exotic cone (only the known cones are excluded).
- Minimality of the weakest content outside the native repertoire.
- A re-derivation at L of λ's route (`kt4_forward_ie1` is a design-run theorem, not certified) and λ's sourcing
  (no structure with three or more tokens at L).
- The level-1 drive (L1): K∞-Act and K∞-Drive remain OPEN.

## 5. Manuscript obligation (recorded, not applied; manuscript hold)

M1 (from stage 4) stands: eliminating every stage-3 exotic cone is not classifying every composite cone; the
uniqueness claim rests on the conditional group theorem. Stage 5 adds its content: the condition (b) is not
supplied by any principle at L; it is conditional on a spectator clause that is a hypothesis of every extension of
the substratum class and a theorem only for that class, where it does not suffice. Any manuscript statement of the
operational-completion route should name that clause (the instance of observational independence for the drive
and one off-frame partner) as the premise it is.

## 6. Status, bands, process

- Bands unchanged: consistency-axis work; no certified label changes; nothing in the repository changed.
- Threads D5 and C5 converged independently on the dependency map, the minimal native content and the
  countermodel structure without reading each other.
- Audits: D5 — hashes verified, replays 3/3 (thread) and 3/3 (coordinator) identical, independent check 32/32
  (run 1 kept); C5 — hashes verified, replays 2/2 and 2/2 identical, independent check 41/44 with the three
  mismatches reconciled as the level of the reported orbit counts (C5's correction recorded in AUDIT-C §3).
- Process record: the first stage-5 launch collided with the stage-1 directory names (`pt/D/`, `pt/C/`) and was
  recovered by amendment 1 (`pt/audit/aborted-launches/stage5-launch1.md`); the coordinator then wrote the stage-6
  protocol and launched threads I1–I4 while D5 and C5 were running, which both threads flagged as an anomaly and
  quarantined by copy. Attribution: all of it is the coordinator's stage-6 launch; no result is affected. The
  breach of the "coordinator writes only under `pt/audit/` while threads run" rule, and the lesson (create a
  stage's directories only after the running stage's threads have reported, or name them in the running
  protocol), are recorded in AUDIT-D §2.
- Holds unchanged: no repository change, no branch, no PR, no CI, no governed round, no publication.
