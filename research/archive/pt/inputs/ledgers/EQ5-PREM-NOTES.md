# EQ5-PREM — running notes (research only; nothing adopted, frozen or governed)

Thread directory: `scratchpad/eq5/PREM/` (the only place this thread writes). Protocol:
`scratchpad/eq5/PROTOCOL-PREM.md` (sha256 `7d3dcf6f44455650…`, verified) and the "Shared rules" of
`scratchpad/eq5/PROTOCOL.md`. Not read: `scratchpad/eq5/SIX/` (concurrent, unaudited). No Lean toolchain: every Lean
text is UNBUILT. No git write, no CI, no agents.

## N0. Start (integrity)

- `integrity_start.log` (written before any other file of this thread):
  - PROTOCOL-PREM sha256 `7d3dcf6f444556505bc7ec6d7b1e756adbfaa757876a51829675567464ac4ef7` (prefix matches the frozen
    `7d3dcf6f44455650`);
  - base manifest (`cd scratchpad/eq/base && sha256sum -c --quiet ../base.manifest.sha256`): silent, exit 0;
  - inputs manifest (`cd scratchpad/eq5/inputs && sha256sum -c --quiet ../inputs.manifest.sha256`): silent, exit 0;
  - HEAD `f0d37906a83585efdaca8e3ee3404410e869c43e` on `claude/network-tool-access-8jtdhm`; `git status --porcelain`
    empty; reflog top `f0d37906 HEAD@{0}: commit: EQ4-F preflight …`.
- `.start_marker` was present at launch (2026-10-09T10:18:43Z), written by the coordinator; not modified.
- Python 3.11.15, sympy 1.14.0.

## N1. Reading log

- Protocols: PROTOCOL-PREM (whole), PROTOCOL.md (whole; shared rules apply, other sections context only).
- SOURCE: `RESULT.md`, `NOTES.md` (whole); scripts `s1_kt4_models.py`, `s2_pair_premises.py`, `e1_stmc_twist.py` (whole,
  read to re-derive, not imported); `s0_census.py` (not needed beyond its recorded findings); outputs of s1, s2, e1.
- Coordinator audit `eqreview/EQ5-SOURCE-AUDIT.md` (whole). Its scope note §3.1 (M_ρ/M_tw refute the parity part only;
  the anchor sum with C_H refutes classification and IE₁) is taken over.
- `eq5/F/DEPGRAPH.md` §1, §4.1–§4.3, §5–§7 (USES §7.1, foils §7.6, SUPPLIES §7.7).
- Inputs: `FourCopyDefs.lean`, `FourCopyPackage.lean` (whole).
- Base kernel (read-only): `CompositeInterface.lean` (whole), `CompositeDimension.lean` §A–§B, `K1Bridge.lean` §A–§B,
  `CompletionAction.lean` header + declaration list, `OrbitGeneration.lean` (`PreservesBody`), `EmbeddedObservation.lean`
  (whole), headers of `CompletedOI`, `CarrierGeneralOIPlus`, `CompositionalIndependence`, `PassiveIndependence`,
  `IndependenceCensus`, `SpectatorBridge`, `MonoidalCompletion`; `ReferenceExtension.lean` (`withSpectator`,
  `HasParallelReferenceExtension`).
- Base records: ROADMAP P1-K (:971–1102) and H-∞, H-Bell rows; `papers/Main.md` §1.2 (axioms), :82, :212, :352, :534,
  :542, :564–568, :628, §4.5 (posit ledger, status ledger); round results CMP-1, IIP-1, ORD-1, COMP-1; audits
  `foundations/kn-elementary-carrier-census.md`, `foundations/kinf-seams-audit.md`,
  `operational/census-oi-compatible-theories.md` (§ embedded observation), `operational/typed-completion-audit.md`
  (coherence outcome C).
- Architecture record `scratchpad/sa/SA-LEDGER.md` §0–§2.3 and §5–§6 (the protocol tower PT/CT; K2-a/K2-b).

## N2. Productivity test and node plan (fixed before any probe was written)

**Productivity test (§A.31).** A finding is a gem iff it is strictly stronger than the obvious restatement ("X is
unsourced", "X ⟺ tok by definition") and it does one of: (i) decides a candidate implication exactly (an exact
countermodel, or a written derivation whose ingredients are exact or landed); (ii) exposes a hidden assumption in how a
premise, a candidate or the setting is stated; (iii) reduces a premise to a strictly weaker one with a checked
derivation and with every hypothesis of the derivation shown load-bearing by a countercontrol. Otherwise record-only.

**Skepticism rule.** A branch that would let a candidate supply `tok`/`TokProdState` or `hgate` is accepted only after
(a) every EQ4-SOURCE countermodel (anchor sum, M_ρ, M_tw, M_id, M_T) and, for Part B, the landed `ball3MaxComposite` /
`ball3MinComposite` bodies with `cnot` are evaluated on the candidate; (b) each hypothesis of its derivation has an
exact countercontrol in which dropping it breaks the conclusion; (c) the derivation is checked for IE₁, IE₂, the
quantum cone as a premise, the complex region tower, and (o)-type steps.

**Nodes (depth-first; decisive first).**
- A-N1 the A1 predicates and their implication lattice: IP₀, IP₁, IP, TokProdState, STMC, RI₀ (one body), RI_L
  (relabelling covariance), RI_op, tok; each implication with one witness per direction or a countermodel.
- A-N2 the census (A2): every candidate, its status, and its verdict on each countermodel.
- A-N3 the survivors (A3): derivations and independence.
- B-N1 the B1 formulations; B-N2 the tests against the landed countermodels and any others found; B-N3 survivors.
- C record only.

## N3. Scripts, pre-run edits and runs (all `python3 -I -B`, run from `scratchpad/eq5/PREM/`; arguments in RESULT §5)

- `q0_census.py` (base text census). Pre-run edit: the typing rule T was widened, before the first run, to count an
  object as complex-typed when its declaration block names `FiniteOperationalTheory` or `TheoryFamily` (whose own
  structure block contains ℂ, which the control checks); the first draft would have misread the one-line
  `EmbeddedObservation` definition. Run 1: 11/11, `Q0-CENSUS-COMPLETE`.
- `q1_tok_models.py` (Part A models and predicates). Pre-run edits, all before the first run: (1) the body evaluation of
  `tok` and `STMC` for hull bodies was rewritten to range over symbolic pair-state generators (the draft used only
  four-token products, which would have let a "holds" verdict rest on a non-generating set); (2) the anchor sum is
  evaluated on two explicit members, ANCc (anchors at the pair-body centre) and ANCz (anchors at the +z product), because
  the symbolic-anchor form has unconstrained anchors and is not a body; the symbolic form is kept for the identity checks
  V1, V3 only; the header was updated accordingly; (3) the body-in-span check uses symbolic pair tables. Run 1: 13/13,
  `Q1-PART-A-MODELS-EXACT`.
- `q2_purity.py` (purity-factorization lemma ingredients). Run 1: 8/8, `Q2-PURITY-LEMMA-INGREDIENTS-EXACT`; leads: all
  four STMC-respecting twists get exact negative witnesses (−1/2, −1/8, −1/2, −1/8).
- `q3_gate.py` (Part B). Run 1: 7/7, `Q3-PART-B-GATE-EXACT`.
- `q4_pair_gates.py` (pair premises of cnotTw, for the census). Run 1: 5/5, `Q4-PAIR-GATES-EXACT`.
- `q5_resets.py` (operation-level identity for irreversible token operations). Run 1: 4/4, `Q5-RESETS-EXACT`.
- No failed runs; no `.runN.*` files exist. Each `.err` holds only the appended `exit=0`.
- Replays: all six byte-identical (`cmp` on `.out` and `.err`).

## N4. The depth-first walk (§A.31), verdict per node

A-N1 (A1 predicates):
- A-N1.1 IP₀ (within-grouping product statistics): automatic from `prod_mem`, `prodEff_apply`, COMP-1 L1. CONFIRMING.
- A-N1.2 RI₀ = one body: vacuous; anchor sum (q1). CONFIRMING (SOURCE).
- A-N1.3 RI_L (relabelling covariance): holds in M_id (Φ = id), M_T (Φ = σ∘τ₁) and both anchor members (swap), with tok
  false (q1). ELABORATING.
- A-N1.4 RI_op (token-wise product effects grouping-independent) ⟺ tok by multilinearity (`tabCoord a b` is the product
  of the token basis functionals). Relabelling. ELABORATING.
- A-N1.5 TPS vs tok: PAD1 (TPS, IP, ¬tok, ¬LT(PA)), PAD2 (tok, ¬TPS, ¬LT(PA)) (q1). ELABORATING (SOURCE's padding remark
  made exact, both directions).
- A-N1.6 IP₁ ⇒ IP ⇒ tok (purity lemma + LT of one grouping + one body + the maxCone bound) [W + X q2, q1]. **NEW.**
  Favourable branch, skepticism applied: IP₁ fails in every SOURCE countermodel and in M_θ (q1); every hypothesis is
  shown load-bearing: LT (PAD1, PAD3), one body (SEPB, with an exact negative A-effect at a B-product), all four tokens
  (M_tw and M_θ: tokens 0, 1, 2 coherent, token 3 not), purity (q2 CC1), positivity (q2 CC2). No IE₁, IE₂, quantum
  cone, region tower or (o) step (every step is (s)).
- A-N1.7 STMC: tok ⇒ STMC ⇒ IP₁; PAD3 has STMC ∧ ¬tok without LT. ELABORATING (SOURCE CP4's sufficiency, open there, is
  settled relative to LT of one grouping).
A-N2 (census):
- A-N2.1 matrix-world principles (observational independence, inert spectators / H_comp, embedded observation (R)+(L),
  typed interface, region tower): complex-typed (q0 T1), import-separated from the ball side (q0 I1); flagged
  circular; OI and H_comp also (o). Their field-neutral shadows: (R) ↦ one body (anchor sum), (L) ↦ RI_L (M_id, M_T,
  anchor), product-type carriers ↦ TIC (relabelling, carries four-copy LT). CONFIRMING / ELABORATING.
- A-N2.2 operation-level token identity for reversible token operations (OLTI): **M_θ** (token 3's chart inverted
  through the antipodal map, central in O(3)) satisfies it, every hypothesis of `kt4_forward` other than tok, and local
  tomography of both groupings; tok and the parity conclusion fail (q1). Also refuted by ANCc. **NEW.** Interpretation
  [W]: θ = Ad(σ_y)∘T (q1 V4), the one-token analogue of the global antiunitary ambiguity that the landed
  `AntiunitaryInvariance.lean` shows invisible to all circuit data.
- A-N2.3 operation-level identity for irreversible token operations (resets, OLTIres): fails in every countermodel,
  M_θ included; with the span condition it gives TPS (q5 D + W). (o)-type. **NEW** (locates which part of an
  observational-independence-type principle carries token identity).
- A-N2.4 pair-level and single-system principles (K1, K2, K∞ incl. Copy, Kₙ as stated, SC/CMP-1, ORD-1, IIP-1, OPACT-1,
  EFF-1, K1-BRIDGE-1, TRB-1, OG-1, NB-1, DIM-1, COMP-1 L1/L9, no-signalling): refutation schema by M_id (same pair data
  as the token-coherent M_σ for uniform Q3 with cnot) and by M_ρ, M_tw, M_θ for the odd pattern (q4 for cnotTw's pair
  premises). CONFIRMING.
- A-N2.5 PT/CT: not landed; classical towers give polytopes; a joint four-token tower with token-indexed labels gives tok
  by construction (relabelling); CT routes through RegionTower (flag). CONFIRMING (SOURCE, SA-LEDGER).
- A-N2.6 Axiom 1, Lemma 2 (substratum product), posit ledger: no composition posit (q0 R). CONFIRMING.
A-N3 (survivors): TPS, RI_state, RI_op, CP2, CP3, TIC — relabellings; IP, STMC, IP₁ — reductions, not restatements;
OLTIres — (o). Weakest: IP₁ (one direction, pure products; a tetrahedral 4⁴ set suffices by multi-affinity, q2 L4).
B-N1/B-N2:
- K1, NativeGateOf (EFF-1/K1-BRIDGE-1 availability with all effects), pair premises (N-CLASS, CandidateCone, convex cone,
  closed): refuted by MAX, MIN and TWIN (q3). CONFIRMING (landed countermodels re-derived) + new model.
- PRP (product-level reversibility relative to K): refuted by MAX (q3). ELABORATING.
- Self-duality and IIP-1 isometry: refuted by TWIN = (twin, cnot), which also satisfies IE₁ (q3). **NEW**: hgate is a
  gate–cone chart alignment; a principle that factors into a gate-only clause true of cnot and a cone-only clause true of
  Q3 and invariant under the target reflection chart cannot supply it.
- KT(4) does not supply hgate: uniform SEP and uniform maxCone are FourCopyCoherent (q3 F) with cnot. CONFIRMING
  (DEPGRAPH §7.6 foils).
B-N3 (survivors): JR/PreservesBody, OAE (effect-side availability, V4′ transported), OPACT (K∞-Act transported), the
operational-completion body — each a restatement of hgate (∧ hinv ∧ hcl) on the whole body, on generators, or by
duality. CONFIRMING (the seams audit :44 already derives body preservation from K∞-Act).
C: record only (RESULT §C).

Passes. Pass 1: A-N1, B-N2 (NEW: A-N1.6, A-N2.2, B TWIN). Pass 2: follow-ups (NEW: A-N2.3; the rest ELABORATING).
Pass 3: re-read of the census sources for missed candidates (KINF-2, AntiunitaryInvariance, typed-completion audit,
Main.md no-signalling, Axiom 1, Lemma 2): no NEW. Pass 4: hidden assumptions in the setting (per-token charts =
IP₁'s content, refining SOURCE row 13; the existential headline form `∃ τ` does not display the gate–cone alignment —
uniform (twin, cnot) satisfies `kt4_forward`'s conclusion with τ ≡ 1 though not Theorem C's `orient` form; the
replacement of tok by IP₁ needs `KT4LT`): no NEW. Pass 5: Part C items: no NEW. Pass 6: skeptical re-check of A-N1.6's
steps (source of positivity, vanishing argument, spanning, multi-affinity, LT) and of A-N2.3's span condition: no gap,
no NEW. Four consecutive passes without NEW: fixed point reached.

## N5. Replays and hashes

- Replays of all six scripts, same arguments, `python3 -I -B`: `.replay.out` and `.replay.err` byte-identical to `.out`
  and `.err` (`cmp`). Hashes (sha256, 16 hex): q0 `a64bf2636650ea77`/`db99032569b6e59e`; q1
  `db688057771bfe0a`/`9dded6d5707e9406`; q2 `a9f95269a0a61cb6`/`d24a769210c29707`; q3 `4be541b1f28d8637`/
  `5907132ff66297e1`; q4 `2d92ca5af97c3b71`/`5e643f28a4bd4e19`; q5 `38b448576fc7e746`/`04a05cb6916c85d9`; every `.err`
  `19eaf43821a7660e` (`exit=0`).
- Cited evidence re-hashed, matching its records: SOURCE s1 `3c7b3c993b7d5527`/`c0d3c490f42a46bb`, s2
  `fcf2c56b103ed2cc`/`1815cb58c292e8e0`, e1 `8f7ed449ccbbd674`/`73bd137b9965f487`; coordinator audit `audit_source`
  `95b0f2477977b104`/`b3d5ff9382e6d1f6`.
- RESULT corrections before finalizing (reading against the evidence): Theorem A's hypotheses restated as PairAdm (not
  only the maxCone bound), and "every hypothesis load-bearing" narrowed to the hypotheses actually given countercontrols
  (PairAdm is assumed throughout and was not tested); the Part B table's KT(4) row given per-model entries; the IE₁ row
  tagged [W].

## N6. End (integrity)

- Anomaly found during the preliminary end check (§A.26, recorded, not repaired): the repository working tree, clean at
  start, has eight untracked files `verification/lean-mathlib/OIBridge/FourCopy{Bipolar,Bridge,Core,Euler,Headline,IE1,
  Local,Tables}.lean`, mtimes 10:54–11:12Z (hashes in RESULT §4). HEAD and the reflog are unchanged. This thread wrote
  none of them, read none of their contents, and no script of this thread reads the working tree; every input it reads
  (the base snapshot, the inputs package, one Mathlib file) verifies unchanged. All measurements and replays had
  finished before the files were found; no measurement was run afterwards. Not quarantined: moving them would be a write
  outside this directory, and the rule here is never to repair. For the coordinator.
- `scratchpad/eqreview/quarantine-SIX-stray/` (MANIFEST.txt 10:21:33Z): the coordinator's quarantine of a SIX stray;
  names and mtimes listed only.
- Write audit: every file in `scratchpad/eq5/PREM/` is this thread's (`integrity_start.log`, `NOTES.md`, `RESULT.md`,
  `q0`–`q5` `.py`/`.out`/`.err`/`.replay.out`/`.replay.err`), plus the launch `.start_marker` (not modified).
- Final end check (2026-10-09T11:21:13Z, after the last substantive write): base manifest and inputs manifest silent,
  exit 0; no `__pycache__` under the base or here; HEAD `f0d37906…` with the reflog top three entries unchanged; the
  working tree shows exactly the same eight untracked `FourCopy*.lean` files and nothing else; Mathlib `db584cd6`,
  clean; files newer than `.start_marker` outside this directory lie only in `eq5/SIX/` (96) and
  `eqreview/quarantine-SIX-stray/` (1).
