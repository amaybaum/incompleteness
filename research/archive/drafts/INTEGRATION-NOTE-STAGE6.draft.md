# Integration note — stage 6 (Q-EX-FULL: complete OI premise closure)

Research only, at base L = `9f9f8257…`. Governing texts `PROTOCOL-STAGE6.md` (`b277b7c1…`), amendment 1
(`59019538…`) and amendment 2 (`748f1764…`). Threads: I1–I4 (step 1, the inventory, `pt/I1/`–`pt/I4/`, audited
`pt/audit/stage6-inputs/I-audit/AUDIT-I.md`), G6 (step 2, the dependency graph, `pt/G6/`, audited
`G-audit/AUDIT-G.md`), R6 (step 3, the countermodel reassessment, `pt/R6/`, audited `R-audit/AUDIT-R.md`), T6
(step 4, the test of (b), `pt/T6/`, audited `T-audit/AUDIT-T.md`). Pre-audit facts and decision rules fixed before
steps 3–4 reported: `pt/audit/stage6-inputs/PRE-AUDIT-R6T6.md` (11/11). Evidence levels: [K] certified at L, [D]
design module, [W] written argument, [X] exact computation, [A] audited stage record, [U] unsourced. Owner's
procedure (note 8): complete inventory → dependency graph → reassess every stage-4 countermodel against all
applicable constraints → test (b) against the complete applicable premises and isolate the missing assumption;
every item at its actual status; hidden-history and composite-cone levels never transferred without a proved
bridge; read-only before any governed round.

## 0. Verdict

[T6 VERDICT — two-way form: DERIVATION / CONDITIONAL on named items / INDEPENDENCE with the isolated missing
assumption / UNRESOLVED. Fill from TEST.md and AUDIT-T.]

## 1. The complete inventory and its graph (steps 1–2, by reference)

- **Inventory.** 633 records across the four namespaces (I1 85 manuscript axioms/conditions/lemmas; I2 113
  manuscript-and-kernel bridge records; I3 187 pair-level and K-programme kernel items; I4 248 kernel
  hypotheses and markers), each with kind, level (H hidden-history / O single-token operational / P pair cone /
  M matrix carrier / G general / X cross), status at L, `depends_on`, `yields`, bearing on the pair cone and the
  do-not-assume flag (75 flagged: I2 11, I3 20, I4 44). Merged by namespace, ids kept (AUDIT-I §4).
- **Graph.** 1054 dependency edges (801 recorded, 31 inherited, 70 to declarations without a record, 152
  completed from kernel signatures at L) plus 495 `yields` edges as a control. Partition (G6's convention,
  disclosed with its sensitivity): (a) 109 consequences of Axioms 1–2 alone (a0 103 premise-free statements about
  defined objects; a1 the non-derivability of Axiom 2; a2 three items needing an observation-base posit), (b) 15
  with C1–C4, (c) 172 needing an operational hypothesis, (d) 36 needing a physical hypothesis, (e) 301 with no
  derivation at L.
- **NO-MEET (the result of step 2).** The ancestor set of the pair-level objects (25 nodes: 21 inventory records
  and 4 kernel declarations, all at levels P and O) and the descendant set of Axioms 1–2 (31 nodes, all
  manuscript H/X records, two of whose spans also name M) share no node, with or without the `yields` edges;
  a synthetic edge makes them meet (countercontrol). Reproduced by the coordinator's own BFS over G6's edge
  table and against a baseline parsed from the inventories before G6 reported (AUDIT-G §2). The missing links,
  each named by the obligation that would supply it: manuscript H → kernel H (images only; stochastic observer
  interface, OPEN); H/M → O: K∞ and its seams (I3.166–I3.173); H/M/G → P: K2 (I3.165); O → P beyond products and
  involutions: K2's local-action clause with K∞-Act and K∞-Drive for (b), P-STAGE2 for closedness, P-ACT2 for
  gate preservation, K1 for the selector; H3: no obligation at L.
- **Do-not-assume items.** No flagged item is a hypothesis of a derived node among the pair premises.
  Discharges for particular objects exist only at the matrix or substratum-class level (`ContextStable` and
  `StructurallyClosed` for the substratum class, `HasParallelReferenceExtension` for the full theory,
  `LayerFlowExecutable` under composite unitary control, implementation locality and embedded observation for
  exact QM, `DerivedOI` for the substratum theory); (b), IE1, IE2, frame covariance and `Q3` have no kernel
  discharge at L.
- **Record items (hygiene, no status effect).** Two co-presupposition cycles between assumed records
  (I2.6 ⇄ I2.10, I2.42 ⇄ I2.56); four `depends_on` fields naming a proof-level or definition dependency absent
  from the cited declaration's arguments (I2.25, I2.36, I2.96, I3.105); 21 fields omitting a declared argument
  that the kernel completion supplies. Ids are kept; nothing renumbered.

## 2. The countermodels against every applicable item (step 3, by reference)

- **Applicable set.** 199 items: I3's 142 records with bearing other than "none at L", I4.236, I1.17, and the
  55 do-not-assume records of I4 and I2. Alternatives: the explicit cones K(E0) (level (i)) and K(Z_F) (level
  (ii), also the cone of every `Stab_Cl(Z_F)` subgroup); the EXOTIC-E seeds of stage 4 (Y4 `c = 4609/4608`, Y5
  `c = 517/512`, Z `α = 7/8`) and stage 5 (C5 census `d_low = 1/2304, 5/256, 1/8704`; the κ Bell seed; D5's
  monomial seed `c = 513/512`); the torus and finite-group nodes.
- **Excluded by an item at L: none, for every alternative.** Per alternative 118 SATISFIES, 13 FAILS, 68 NOT
  REACHED (EXOTIC-E: 12 FAILS and node T UNDECIDED). Every FAILS row is a hypothesis — the do-not-assume items
  IE1, IE1Drive, Q3/pure-state reachability, (b_S4), (b_n), (b_R1), (b_DJ), frame covariance, K2's clause
  "local actions compatible with the composite cone"; the [D] four-token hypotheses `H` (KT4Core) and FCC under
  the uniform assignment; the PT-record candidates homogeneity H and extreme-ray transitivity T — never a theorem
  or definition at L (R6 §7 pressure test; AUDIT-R §2). The one kernel theorem tying a pair cone to a one-copy
  map, `no_candidateCone_cnot_reflY` (K2Guard.lean:143), holds for each alternative: it constrains the operation
  `actT reflY`, not the cone (PRE-AUDIT P1a–P1d).
- **NOT REACHED** is the verdict on every H-, M-, G-level item (no bridge at L; NO-MEET) and on every item
  needing three or more tokens or the absent P-STAGE2 / P-ACT2 bridges.
- **Embedded-observer realization: nothing at L, either way.** No statement at L attaches a realization, or an
  obstruction to one, to any cone in `W 3` (import-graph scan: only the root aggregator reaches both a pair
  module and an H-level realization module). The realization theorems live at level H for the matrix carrier,
  whose composites are tensor products by construction; the one composition clause at L (Main.md:552) takes
  `I_a ⊗ I_b` as input, the composite action every alternative lacks (assumption-watch marker).
- **Single-token premises** are inherited from Q3's token structure by construction (two copies of `eball 3`
  with `nflip`, `z3`, `cnot`) and verified exactly where checkable (12/12). K∞-Geom's pair reading fails for
  Q3 and the explicit cones alike (I4.236's scope): not a discriminator.
- **Not reassessed:** `K({F, cnot F})` and `K(e_c)` (named in the protocol's step 3, omitted from amendment 1's
  A1.5 — a coordinator omission); covered by the same argument for any closed self-dual `cnot`-invariant cone
  containing the products (AUDIT-R §4 item 1).

## 3. The test of (b) against the complete applicable premises (step 4)

[T6 — derivation routes tried with every step labelled and the step at which each fails (the missing bridge or
the do-not-assume premise it would need); the countermodel with its row-by-row table; the exact witness; the
isolated missing assumption with its disguise test. Fill from TEST.md and AUDIT-T.]

## 4. CONDITIONAL items, named at their status

[From T6 and stage 5: every assumed / conditional / open / empirically motivated inventory item that any
derivation of (b) uses, with its inventory id and status at L. Stage 5's α (OI⁺-1 `HasParallelReferenceExtension`,
added principle, GR.md:228), β (`ContextStable` of a class containing the flow and J; theorem for the monomial
class only, StructuralClosure.lean:261), γ-extension (`StructurallyClosed` for an extension), δ (∀-level clause of
`LayerFlowExecutable`; redundant inside `DerivedOI`, relocated to `ContextStable`) carry over unless T6 finds a
route that avoids them.]

## 5. The isolated missing assumption

[T6 — exact content; relation to OI⁺-1 (instance for the drive and one off-frame partner on one token); relation
to K2's local-action clause (I3.165) and to K∞-Act / K∞-Drive (I3.168, I3.169); what would close it: a theorem at
L of the form "…", at which level, and which obligation names it.]

## 6. What remains

- The level-1 drive: K∞-Act and K∞-Drive OPEN (ROADMAP.md:1014–1017); K2 OPEN (ROADMAP.md:1001–1006).
- An explicit κ-invariant exotic cone; whether extreme-ray transitivity T excludes every exotic cone (node T
  UNDECIDED for the existence-only alternatives); minimality outside the native repertoire; λ's sourcing (no
  three-token structure at L).
- The bridges NO-MEET names (§1), each an obligation, none a premise at L.
- [T6 additions.]

## 7. Manuscript obligations (recorded, not applied; manuscript hold)

M1 (stage 4) and its stage-5 extension stand. Stage 6 adds: the eleven propagation items of
`pt/audit/stage6-inputs/MANUSCRIPT-PROPAGATION-ITEMS.md` (book/paper divergences on (C2), logical independence,
"deterministic", bijectivity; the dangling Kochen–Specker §3.2 reference; the `S_imp_D` anchor weaker than the
manuscript theorem; three named hypotheses without a ROADMAP row; book mirror gaps; a numbering mismatch of the
five completion conditions; M1; the scope of Main.md:552/:562). [T6 additions, if any.]

## 8. Status, bands, process

- Bands unchanged: consistency-axis work; no certified label changes; nothing in the repository changed; no
  branch, PR, CI, governed round or publication.
- Audits: I1–I4 (hashes 76/77/53/73, replays 31/31, import-graph check); G6 (hashes 59/59, replays 5/5,
  independent check 11/11 with replay); R6 (hashes 59/59, replays 6/6, every pre-audit prediction matched);
  T6 [fill].
- Process record: (1) the coordinator wrote the stage-6 protocol and launched I1–I4 while stage 5's threads
  were running (recorded in AUDIT-D §2 and AUDIT-C §2 with the lesson); (2) amendment 1 omitted two stage-3 cones
  named in the protocol's step 3 (recorded in AUDIT-R §4, covered by argument); (3) amendment 2 fixed T6's
  inputs (the frozen G6/R6 records and the three audits) after both audits were written; (4) G6's classification
  rules were re-scoped after its first run (disclosed with the sensitivity; the NO-MEET result does not depend
  on the partition; AUDIT-G §4); (5) [T6 deviations].
- Holds unchanged.
