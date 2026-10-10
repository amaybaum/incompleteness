# Integration note — stage 6 (Q-EX-FULL: complete OI premise closure)

Research only, at base L = `9f9f8257…`. Governing texts `PROTOCOL-STAGE6.md` (`b277b7c1…`), amendment 1
(`59019538…`) and amendment 2 (`748f1764…`). Threads: I1–I4 (step 1, the inventory, `pt/I1/`–`pt/I4/`, audited
`pt/audit/stage6-inputs/I-audit/AUDIT-I.md`), G6 (step 2, the dependency graph, `pt/G6/`, audited
`G-audit/AUDIT-G.md`), R6 (step 3, the countermodel reassessment, `pt/R6/`, audited `R-audit/AUDIT-R.md` with its
addendum), T6 (step 4, the test of (b), `pt/T6/`, audited `T-audit/AUDIT-T.md`). Pre-audit facts and decision rules
fixed before steps 3–4 reported: `pt/audit/stage6-inputs/PRE-AUDIT-R6T6.md` (11/11; §5 witnesses 6/6). Evidence
levels: [K] certified at L, [D] design module, [W] written argument, [X] exact computation, [A] audited stage
record, [U] unsourced. The owner's procedure (note 8): complete inventory → dependency graph → reassess every stage-4
countermodel against all applicable constraints → test (b) against the complete applicable premises and isolate the
missing assumption; every item at its actual status; the hidden-history and composite-cone levels never transferred
without a proved bridge; read-only, before any governed round. Written 2026-10-10 after all four audits.

## 0. Verdict

**INDEPENDENCE.** The complete applicable premise set at L — every inventory item at its actual status that reaches
the pair cone — does not force the composite action (b), even in its weakest sufficient form ((b) for the drive
with one off-frame partner on one token). In the owner's two-way form:

| question | outcome | basis |
|---|---|---|
| Do the premises at L derive (b)? | **no** — the derivation stops at one step: "the flow and `J`, acting on one token, preserve `K`", for which L has no premise | T6 D1–D4 [X + W], AUDIT-T §2: no H→P, M→P or G→P bridge at declaration level; no theorem at L concludes the invariance of a pair cone under `actC g` or `actT g` (39 theorems mention the actions; only the reflY no-go binds a cone, and it forbids an operation); the ten object-specific discharges are closed statements off the pair carrier |
| Is there a countermodel satisfying every item that reaches the pair cone? | **yes — K(Z_F)**, the explicit stage-3 cone | row by row against the 199 applicable items (R6 Table A2, audited; T6 t4 and the coordinator's recount): 118 SATISFIES (3 vacuously), 68 NOT REACHED (hidden-history, matrix and general-level items: no bridge at L), 13 FAILS — every one a hypothesis (do-not-assume items, design-run [D] hypotheses, PT-record candidates), never a theorem or definition at L |
| How is (b) violated? | by every one-parameter rotation subgroup of either token: for every unit axis `n`, either token and every defect `z_s`, `ipW(R_n(t) z_s, R_n(π/2) p_s) = −sin(t)/8` with the witness `R_n(π/2) p_s` a pure state inside K(Z_F); `cyc3^{±1}` likewise | T6 t3, t5 [X]; AUDIT-T `indep_checkT.py` X1–X4 (symbolic in the axis), PRE-AUDIT §5 [X] |
| The missing assumption, isolated | **(b) itself for ball3Drive's flow and its J-conjugate on one token** — `K` invariant under `actτ R_z(t)` and `actτ R_x(t)` for all `t` — the instance of observational independence (OI⁺-1) for the drive and one off-frame partner. It fails the disguise test: it restates I3.153 (b_DJ), I3.150 for two generators, and K2's clause "local actions compatible with the composite cone" (I3.165) | T6 §5 [W]; stage 5 §2 [A]; with H1–H3 it forces `Q3` (stage 4 Y2 [A]) and hence every form of (b) |
| CONDITIONAL readings | relative to an enlarged premise set adjoining the design-run four-token coherence λ (KT4Core with `tok`, [D], no three-token structure at L) or the PT-record pair homogeneity H ([W + L]): **CONDITIONAL on that item**; neither is an item at L, neither yields a derivation at L | T6 §4 (stricter wording), §2.5; stage 5 λ [A] |

**Bottom line.** Stage 5's classification stands with the premise set now complete: (b) is CONDITIONAL on a
spectator clause (α OI⁺-1, β `ContextStable`, γ-extension, δ's ∀-level clause) — every one of them a level-M clause
with no bridge to `W 3` — and INDEPENDENT of everything else at L. The complete inventory adds no route: the
hidden-history items never reach the pair cone, the kernel-completed dependencies add nothing, and no discharge for
a particular object leaves the matrix carrier or the substratum class. The framework's certified content at L
constrains a pair cone through H1–H3, the gate, products, effects and the reflY no-go, and through nothing that acts
on a non-product pair vector.

## 1. The complete inventory and its graph (steps 1–2, by reference)

- **Inventory.** 633 records in four namespaces (I1 85 manuscript axioms, conditions and lemmas; I2 113
  manuscript-and-kernel bridge records; I3 187 pair-level and K-programme kernel items; I4 248 kernel hypotheses and
  markers), each with kind, level (H hidden-history / O single-token operational / P pair cone / M matrix carrier /
  G general / X cross), status at L, `depends_on`, `yields`, bearing on the pair cone and the do-not-assume flag
  (75 flagged: I2 11, I3 20, I4 44). Merged by namespace, ids kept (AUDIT-I §4).
- **Graph.** 1054 dependency edges (801 recorded, 31 inherited, 70 to declarations without a record, 152 completed
  from kernel signatures at L) plus 495 `yields` edges as a control. Partition (G6's convention, disclosed with its
  sensitivity): (a) 109 consequences of Axioms 1–2 alone (103 premise-free statements about defined objects, the
  non-derivability of Axiom 2, three items needing an observation-base posit), (b) 15 with C1–C4, (c) 172 needing
  an operational hypothesis, (d) 36 needing a physical hypothesis, (e) 301 with no derivation at L.
- **NO-MEET.** The ancestor set of the pair-level objects (25 nodes: 21 records and 4 kernel declarations, all at
  levels P and O) and the descendant set of Axioms 1–2 (31 nodes, all manuscript H/X records, two of whose spans
  also name M) share no node, with or without the `yields` edges; a synthetic edge makes them meet (countercontrol).
  Reproduced by the coordinator's own BFS and against a baseline parsed from the inventories before G6 reported
  (AUDIT-G §2); confirmed by T6 at the level of Lean declarations (t1). Missing links, each an obligation and none a
  premise: manuscript H → kernel H (images only; stochastic observer interface, OPEN); H/M → O: K∞ and its seams
  (I3.166–I3.173); H/M/G → P: K2 (I3.165); O → P beyond products and involutions: K2's local-action clause with
  K∞-Act and K∞-Drive for (b), P-STAGE2 for closedness, P-ACT2 for gate preservation, K1 for the selector; H3: no
  obligation at L.
- **Do-not-assume items.** No flagged item is a hypothesis of a derived node among the pair premises. Discharges for
  particular objects exist only at the matrix or substratum-class level (`ContextStable` and `StructurallyClosed`
  for the substratum class, `HasParallelReferenceExtension` for the full theory, `LayerFlowExecutable` under
  composite unitary control, implementation locality and embedded observation for exact QM, `DerivedOI` for the
  substratum theory); (b), IE1, IE2, frame covariance and `Q3` have no kernel discharge at L.
- **Record items** (hygiene; no status effect; ids kept): two co-presupposition cycles between assumed records
  (I2.6 ⇄ I2.10, I2.42 ⇄ I2.56); four `depends_on` fields naming a proof-level or definition dependency absent from
  the cited declaration's arguments (I2.25, I2.36, I2.96, I3.105); 21 fields omitting a declared argument that the
  kernel completion supplies.

## 2. The countermodels against every applicable item (step 3, by reference)

- **Applicable set.** 199 items: I3's 142 records with bearing other than "none at L", I4.236, I1.17, and the 55
  do-not-assume records of I4 and I2. Alternatives: the explicit cones K(E0) (level (i)) and K(Z_F) (level (ii),
  also the cone of every `Stab_Cl(Z_F)` subgroup); the EXOTIC-E seeds of stage 4 (Y4 `c = 4609/4608`, Y5
  `c = 517/512`, Z `α = 7/8`) and stage 5 (C5 census `d_low = 1/2304, 5/256, 1/8704`; the κ Bell seed; D5's
  monomial seed `c = 513/512`); the torus and finite-group nodes.
- **Excluded by an item at L: none, for every alternative.** Per alternative 118 SATISFIES, 13 FAILS, 68 NOT
  REACHED (EXOTIC-E: 12 FAILS and node T UNDECIDED). Every FAILS row is a hypothesis — the do-not-assume items IE1,
  IE1Drive, Q3/pure-state reachability, (b_S4), (b_n), (b_R1), (b_DJ), frame covariance, K2's clause; the [D]
  four-token hypotheses `H` (KT4Core) and FCC under the uniform assignment; the PT-record candidates homogeneity H
  and extreme-ray transitivity T — never a theorem or definition at L (R6 §7; AUDIT-R §2; recount
  AUDIT-R-ADDENDUM). The one kernel theorem tying a pair cone to a one-copy map, `no_candidateCone_cnot_reflY`
  (K2Guard.lean:143), holds for each alternative: it constrains the operation `actT reflY`, not the cone.
- **NOT REACHED** is the verdict on every H-, M-, G-level item (no bridge at L) and on every item needing three or
  more tokens or the absent P-STAGE2 / P-ACT2 bridges.
- **Embedded-observer realization: nothing at L, either way.** No statement at L attaches a realization, or an
  obstruction to one, to any cone in `W 3` (import-graph scan: only the root aggregator reaches both a pair module
  and an H-level realization module; T6: none of its declarations carries either vocabulary). The realization
  theorems live at level H for the matrix carrier, whose composites are tensor products by construction; the one
  composition clause at L (Main.md:552) takes the local instruments' action `I_a ⊗ I_b` as input — the composite
  action every alternative lacks (assumption-watch marker).
- **Single-token premises** are inherited from Q3's token structure by construction (two copies of `eball 3` with
  `nflip`, `z3`, `cnot`) and verified exactly where checkable (12/12). K∞-Geom's pair reading fails for Q3 and the
  explicit cones alike (I4.236's scope): not a discriminator.
- **Not reassessed:** `K({F, cnot F})` and `K(e_c)` (named in the protocol's step 3, omitted from amendment 1's
  A1.5 — a coordinator omission), covered by the same argument for any closed self-dual `cnot`-invariant cone
  containing the products (AUDIT-R §4); T6 did not use them.

## 3. The test of (b) against the complete applicable premises (step 4)

- **The derivation attempt, exhausted first.** D1: no H→P, M→P or G→P bridge at L at the level of declarations —
  the only module whose import closure reaches both the pair vocabulary and the hidden-history / matrix / general
  vocabulary is the root aggregator, whose declarations carry neither; each route (α, β, γ, δ, ζ, DerivedOI,
  CompletedOI, the sealed core and its realizations) ends at an obligation (K2; P1 ROADMAP.md:68), never at a
  premise. D2: of the 39 theorems at L mentioning `actC`/`actT`, 33 are equalities (carrier identities, gate
  relations with involutions, product identities), one concludes `False` (the reflY no-go), four are memberships
  about products or carry the invariance only as an antecedent of `→ False`, one is `¬ Even d`; no theorem
  concludes that a pair cone is invariant under a single-token action; the kernel-completed edges add no
  hidden-history, matrix or general premise to the 25-node ancestor set of the pair objects. D3: the ten
  object-specific discharges are closed statements about the monomial class, `MixC`, exact QM, `genTheory` or the
  substratum theory, none reaching `CompositeDimension`. D4: the direct chain — products in `K`; `K ⊆ maxCone`;
  `cnot`-invariance; self-duality; the token's drive and `J` — stops at step 6, "`actτ R(t) K ⊆ K` for the flow and
  `J`", which no item at L supplies; every item that would supply it is (b) or contains it (I3.150–I3.153, IE1,
  IE1Drive, K2's clause, P-ACT2's idle-extension reading).
- **The countermodel K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F**, rebuilt by T6 from the kernel's definitions with its own
  exact code (17/17): H1 by a symbolic sum of squares; H2 at level (ii) (a group of order 64 permuting the defects);
  H3 self-duality by a complete written proof (orthogonality of the four Bell-type defects and one Schur-complement
  correction lemma; reviewed in AUDIT-T §2; independent of, and agreeing with, the stage-3 surgery theorems);
  `K ⊆ maxCone`; the slice conditions; the reflY no-go's consequence; `K ≠ Q3`.
- **The violation.** For every unit axis `n`, either token and every `s`: `ipW(R_n(t) z_s, R_n(π/2) p_s) = −sin(t)/8`,
  the witness a pure state in `Q3 ∩ Z_F*` (pairings 0 and `(1 − n_i²)/8` with the defects); so every member with
  `sin t ≠ 0` of every one-parameter rotation subgroup of either token moves K(Z_F) out — the drive through the NOT
  (`R_x`), ball3Drive's flow (`R_z`), their J-conjugates, and `J = cyc3^{±1}` itself, on the control, on the target
  and in the mixed placement. K(Z_F) admits no continuous local rotation symmetry at all. (Coordinator: the identity
  is the Bell-state trace formula — `ipW(z_s, R_n(u) p_s) = −cos(u)/8` for every axis — proved symbolically in
  AUDIT-T.)
- **Clarification of the stage-5 note's §2.** With the certified `ball3Drive` (flow about z, `J = cyc3`,
  `J R_z J⁻¹ = R_x`), the two weakest sufficient forms — the drive with its J-conjugate, and the drive through the
  NOT with the phase flow about z — are the same pair of flows `{R_z, R_x}`; they differ only under the PT
  convention that calls `R_x` the drive. No change of content.

## 4. CONDITIONAL items, named at their status

Every item that any derivation of (b) uses, with its inventory id and status at L (none is proved at L):

| item | id | status at L | level | what it would supply |
|---|---|---|---|---|
| α — OI⁺-1, `HasParallelReferenceExtension` | I4.3 (I4.82, I4.96) | assumed; added principle (GR.md:228); do-not-assume | M | spectator stability of every available operation; transcribed to `W 3` it is (b) for every operation |
| β — `ContextStable` of a class containing the drive and `J` | I4.29 (with I4.31) | theorem for the monomial class only (StructuralClosure.lean:261); assumed otherwise | M | (b) for the generating class; for the monomial class insufficient (seed `c = 513/512`) |
| γ — `StructurallyClosed` for an extension | I4.45 | assumed for any extension; theorem for the substratum class | M | spectator stability of the extended class |
| δ — `LayerFlowExecutable`, ∀-level clause | I4.56 | do-not-assume; the ∀-level clause redundant inside `DerivedOI` (stage 5 D5 N1c) | M | (b) for the drive (and, with the phases, for drive + phase flow) |
| λ — four-token coherence with `tok` | I3.133 (KT4Core), I3.134 (`tok`) | not at L — design-run [D]; no structure with three or more tokens at L | P (four tokens) | IE1 by `kt4_forward_ie1` [D], hence (b_S4), hence `Q3` |
| pair homogeneity H | I3.160 | PT-record candidate; `H ⇒ Q3` is [W + L] | P | `K = Q3` directly |
| extreme-ray transitivity T | I3.161 | PT-record candidate; excludes the known cones only; UNDECIDED for the EXOTIC-E alternatives | P | exclusion of the exotic cones (minimality UNRESOLVED) |
| K2's clause "local actions compatible with the composite cone"; P-ACT2 | I3.165; I3.146 | OPEN obligation (ROADMAP.md:1001–1005); assumed (named premise of KT4-PREM-1) | P | (b) itself; P-ACT2's idle-extension reading is IE1 |
| the gluing clause | I2.12 (Main.md:552) | proved [M], no kernel anchor | H | takes `I_a ⊗ I_b`, the composite action, as input |

## 5. The isolated missing assumption

**Exact content.** For one token τ ∈ {C, T}: `∀ t, ∀ ω ∈ K: actτ R_z(t) ω ∈ K` and `actτ R_x(t) ω ∈ K` — the
spectator stability of ball3Drive's flow and of its J-conjugate (equivalently, of the drive through the NOT and the
substratum phase flow about z). With H1–H3 it forces `K = Q3` (the two flows generate SO(3) on that token; stage 4
Y2 [A]), and then every form of (b) holds. It is minimal within the native repertoire (stage 5 C5 census [A]: each
single flow, `{J}` and `{NOT, J}` leave exotic alternatives); K(Z_F) shows how much is missing — not one
one-parameter rotation subgroup of either token is supplied by L.

**Where it sits.** It is the instance of OI⁺-1 for the drive and one off-frame partner (strictly smaller than OI⁺-1,
not derived from anything at L); field-neutrally it is the clause of K2 (I3.165) that composes the local actions,
with K∞-Act / K∞-Drive (I3.168, I3.169, OPEN) supplying the operations' availability. What would close it: a theorem
at L stating that, for the composite of two tokens with the native gate, the local action of the drive and one
off-frame partner preserves the composite state cone — an obligation G6 names (K2's local-action clause), at level P
or through a proved H→P bridge. The hidden-history route would be an embedded-observer realization of the pair with
local instruments acting as `I_a ⊗ I_b` (Main.md:552); its composition clause is the idle extension itself, so it
fails the disguise test at level H.

**Disguise test.** The assumption restates do-not-assume items (I3.153, I3.150 for two generators, I3.165's clause)
and the level-M observational-independence clause: it is (b) for the minimal native class, not a new principle.
The candidates that pass the test — λ, H, T — are not items at L.

## 6. What remains

- The level-1 drive: K∞-Act and K∞-Drive OPEN (ROADMAP.md:1014–1017); K2 OPEN (ROADMAP.md:1001–1006); the
  bridges NO-MEET names (§1), each an obligation.
- An explicit κ-invariant exotic cone; whether extreme-ray transitivity T excludes every exotic cone (node T
  UNDECIDED for the existence-only alternatives); minimality outside the native repertoire; λ's sourcing (no
  three-token structure at L); a re-derivation at L of λ's route (`kt4_forward_ie1` is a design-run theorem).
- An embedded-observer realization of K(Z_F), or an obstruction to one: open at L, either way.
- `K({F, cnot F})` and `K(e_c)` not reassessed row by row (covered by argument only).

## 7. Manuscript obligations (recorded, not applied; manuscript hold)

M1 (stage 4) and its stage-5 extension stand. Stage 6 adds the eleven propagation items of
`pt/audit/stage6-inputs/MANUSCRIPT-PROPAGATION-ITEMS.md` (book/paper divergences on (C2), logical independence,
"deterministic" and bijectivity; the dangling Kochen–Specker §3.2 reference; the `S_imp_D` anchor weaker than the
manuscript theorem; three named hypotheses without a ROADMAP row; book mirror gaps; a numbering mismatch of the
five completion conditions; M1; the scope of Main.md:552/:562). Any manuscript statement of the operational-
completion route should name the spectator clause for the drive and one off-frame partner as the premise it is; any
statement that a non-quantum composite is "realizable" by the same machinery should say which composite action it
assumes.

## 8. Status, bands, process

- Bands unchanged: consistency-axis work; no certified label changes; nothing in the repository changed; no branch,
  PR, CI, governed round or publication; no manuscript edit.
- Audits: I1–I4 (hashes 76/77/53/73, replays 31/31, import-graph check); G6 (hashes 59/59, replays 5/5, independent
  check 11/11 with replay; NO-MEET reproduced with countercontrol); R6 (hashes 59/59, replays 6/6, every pre-audit
  prediction matched, tables recounted 5/5); T6 (hashes 35/35, replays 5/5, row-by-row check 4/4 against the
  coordinator's recount, witness identities 5/5 symbolic in the axis, the self-duality proof reviewed).
- Process record: (1) the coordinator wrote the stage-6 protocol and launched I1–I4 while stage 5's threads were
  running (recorded in AUDIT-D §2 and AUDIT-C §2 with the lesson); (2) amendment 1 omitted two stage-3 cones named in
  the protocol's step 3 (AUDIT-R §4, covered by argument); (3) amendment 2 fixed T6's inputs after both audits were
  written, and AUDIT-R was frozen at the hash handed to T6 (its later recount went into an addendum); (4) G6's
  classification rules were re-scoped after its first run (disclosed with the sensitivity; the NO-MEET result does
  not depend on the partition; AUDIT-G §4); (5) T6's disclosed deviations are cosmetic or process matters and bear on
  no evidence line (AUDIT-T §3).
- Holds unchanged.
