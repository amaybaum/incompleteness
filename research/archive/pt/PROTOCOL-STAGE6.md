# PT protocol — stage 6: complete OI premise closure (Q-EX-FULL)

`PROTOCOL.md` (`239dc123…`), amendments 1–2, `PROTOCOL-STAGE2.md`, `PROTOCOL-STAGE2-DS.md`, `PROTOCOL-STAGE3.md`
(`1a649168…`), `PROTOCOL-STAGE4.md` (`d3da2811…`), `PROTOCOL-STAGE5.md` (`9e01f098…`) with its amendment 1
(`1f639115…`) govern except where this file differs. Owner's direction (note 8, `OWNER-NOTE8-FULL-CLOSURE.md`,
verbatim where quoted): "The next round should test the complete existing OI framework, not just the subset of
assumptions used in Stage 4." Name: **Q-EX-FULL: Complete OI Premise Closure**. "Including a condition in the audit
does not mean assuming it is true. Every item must retain its actual status: proved, independently assumed,
conditional, empirically motivated, refuted or open." The four steps: "1. Build a complete premise inventory.
Enumerate every existing axiom, condition, lemma and relevant theorem at the frozen certified base. Record its exact
statement, provenance, assumptions and applicability. Nothing should be excluded merely because it appears unrelated
to quantum mechanics. 2. Construct the dependency graph. Determine what follows from the foundational axioms, what
follows only when C1–C4 apply, and what depends on additional operational or physical hypotheses. Include previously
proved lemmas through their dependencies rather than silently treating them as independent premises. 3. Reassess all
exotic countermodels. Check whether each Stage 4 alternative satisfies every applicable OI constraint. A cone-level
countermodel does not automatically establish the existence of a compatible embedded-observer realization. 4. Test
the missing implication. Determine whether the complete applicable OI premises force the required off-frame
composite mixing or operation-extension principle (b). If not, identify a countermodel satisfying the full
applicable premise set and isolate the genuinely missing assumption." "Crucially, it must distinguish assumptions
about hidden deterministic histories from assumptions about composite state cones. They cannot be transferred
between mathematical levels without a proved bridge." Stage 4 is preserved exactly as archived; this is a read-only
research audit before any governed round. Holds unchanged: no repository change, branch, PR, CI, governed round or
publication. Stage 5 (Q-EX-BRIDGE) finishes under its own frozen protocol; stage 6 consumes the audited stage-4 and
stage-5 records in steps 3–4, while steps 1–2 start at once.

## The question Q-EX-FULL
Let Π(L) be the complete set of axioms, conditions, hypotheses and theorems the corpus carries at the frozen base
L = `9f9f8257…` (kernel, manuscripts, roadmap, landed round records). Let Π_app(L) ⊆ Π(L) be the items that apply to
the two-token pair-cone setting of stages 3–5 — directly, or through a bridge theorem proved at L that transfers them
between levels. Decide: does Π_app(L), with every item at its actual status, force (b_min) (any of the stage-5 forms:
the full rotation group of one token on the pair; one off-frame rotation subgroup; one off-frame rotation of order 3;
the native drive together with `J`), and hence `K = Q3` by stage 4? Outcomes, in the owner's two-way form with the
stage-5 refinement for assumed items:
- **DERIVATION.** Π_app(L) ⇒ (b_min) by a written proof with exact ingredients [W + X], every item used at status
  *proved* [K] or *refuted-not-used*; an item at status *assumed*, *conditional* or *open* that the proof uses makes
  the verdict **CONDITIONAL(item; status)**, never DERIVATION. The OI⁺ completion conditions, (b) itself, IE1, IE2
  and frame covariance are inventoried but carry the flag *do not assume*: a derivation that uses one is circular
  and is recorded as such.
- **INDEPENDENCE.** A full OI-compatible countermodel: a structure satisfying every applicable item at its actual
  status (the *proved* items as theorems it must satisfy, the *assumed* items as hypotheses it must satisfy unless
  the hypothesis is one of the do-not-assume flags) whose pair cone is not `Q3` — the stage-4 cones and seeds if
  they survive step 3, or new ones — with the missing assumption isolated: the weakest item outside Π_app(L) that
  would force (b_min).
- The **level distinction** is mandatory in every record and every verdict: an item about hidden deterministic
  histories (the substratum, Axioms 1–2, C1–C4, realization theorems) constrains the pair cone only through a bridge
  theorem proved at L; a verdict that transfers a constraint across levels without naming the bridge is void.

## Step 1 — the complete premise inventory (threads I1–I4, parallel, read-only)
**Record schema** (one record per item; Markdown table rows or one block per item, uniform across threads):
- `id` — stable: `<thread>.<n>` (never renumbered; retired ids stay retired);
- `name`; `kind` ∈ {axiom, condition, hypothesis-structure (a Lean `structure … : Prop` or `def … : Prop` used as
  a hypothesis), definition-as-hypothesis, theorem, lemma-folded (recorded only as an edge of the theorem it serves),
  obligation (ROADMAP), manuscript-principle};
- `statement` — exact: the Lean declaration signature with its docstring, or the manuscript sentence, quoted;
- `provenance` — file:line at L (kernel name; manuscript section; roadmap entry; landed round result note);
- `status` ∈ {proved [K], assumed (hypothesis of a theorem, never discharged), conditional-on <item>, empirically
  motivated, refuted (by <record>), open (ROADMAP entry)} — taken from the record that fixes it (`verification/
  README.md`, `ROADMAP.md`, the round result notes, the kernel docstrings), never upgraded by the thread;
- `level` ∈ {H hidden deterministic history / substratum; O single-system operational (field-neutral, the K
  programme); P pair / composite cone (`W 3`, `K`); M matrix-level operational theory (`FiniteOperationalTheory`);
  G general carrier / typed / quasilocal; X manuscript physical layer (SM, GR, Substratum, cosmology)};
- `depends_on` — the hypotheses it assumes (ids or names), for theorems the full hypothesis list;
- `yields` — the theorems it feeds, the obligations it discharges;
- `bridge` — for items not at level P: the bridge theorem at L that transfers the item to the pair cone, by name and
  file:line, or `none at L`;
- `bearing` ∈ {direct constraint on `K` or on (b_min); constrains the single-token structure the pair inherits;
  constrains the composite only through <bridge>; none at L};
- `flag` — `do not assume` for the OI⁺ completion conditions ((i)–(v), observational independence, reversible
  richness, observer recursion, implementation locality's spectator clause, structural closure of an extension,
  `LayerFlowExecutable`), for (b), IE1, IE2, frame covariance, `Q3`/PSD/pure-state reachability.

**Coverage controls (mechanical, each thread for its assigned scope; the coordinator across threads).** (a) The
kernel census: every `axiom`, `opaque`, `structure … : Prop`, `class`, and `def … : Prop` in the assigned modules
(`grep -n -E '^(axiom|opaque|structure|class|def) '` filtered to `Prop`-valued declarations, exact Python over the
tree, `python3 -I -B`), each mapped to a record id or listed under *out of scope* with a reason that is never
"unrelated to quantum mechanics" (admissible reasons: a definition with no hypothesis role; a theorem-internal
auxiliary; belongs to another thread's scope, named). (b) The manuscript census: every sentence of the assigned
sections that states an axiom, condition, hypothesis, principle or theorem (`Axiom`, `Condition`, `C1`–`C4`,
`(i)`–`(v)`, `H-`, `K`, `A1`–`A6`, `Theorem`, `Lemma`, `Principle`, `Assumption`, boxed statements). (c) The roadmap
census: every obligation row and bullet of `ROADMAP.md` in scope. Each thread reports its three census counts and
the mapping.

**Partition (scopes; a thread that meets an item outside its scope records it under *out of scope: thread Ik* and
moves on):**
- **I1 — foundations.** Axiom 1 (tokened differentiation), Axiom 2 (recurrence); the observer structure
  (embeddedness, visible/hidden partition, finite resolution, reversible realization); the hidden-sector conditions
  C1–C4 (coupling, memory persistence, capacity, history readback); the sealed OI core and its realization
  (`OICore`, `RealizesSealedOICore`, `OIRealization.lean`, the C1–C4 modules); Methodology §6, Main §1–§3,
  Substratum (the axioms A1–A6 as far as they constrain observers), Explainer where it states a condition.
- **I2 — established theorems and the physical layer.** The finite-horizon equivalence (`S ⟺ D ⟺ Q_fb`), the
  hidden-memory results, recurrence, the canonical predictive quotient, the Stinespring/intervention-dilation route,
  Bell and no-signalling statements, the Level III quasilocal completion, and every constraint in Main, SM, GR and
  Substratum that bears on composition, locality or operations (dynamical causal separation, tensor-product
  structure, the operational-extension boundary, implementation locality and the substratum-source and layer-flow
  forms as *manuscript* statements — their kernel side is I4's).
- **I3 — operational foundations and composite reconstruction.** The K programme: K∞ (Stage, Act, Drive, Trans,
  Seed; `KInfFoundations.lean`, `OrbitGeneration.lean`, `TransitiveBody.lean`, the OPACT modules, the drive and
  stage records), K1 (effects, sharp tests, bridges; `EffectAvailability`-type modules and the K1 round results), K2
  (`K2Guard.lean`, `CompositeDimension.lean`: `W d`, `maxCone`, `IsNot`, `NativeGate`, `Entangling`, `actC`/`actT`,
  cnot, DIM-1's selector, parity and odd-character results, RELC/REL-T), local tomography as `W d` encodes it,
  positivity, trace self-duality as fixed at stage 3 (H3), the PT stage records (stages 1–5) as far as they fix a
  premise's status.
- **I4 — generalization and completion.** Kₙ (the census result), `GeneralCarrier.lean` ((i)–(v), `WellFormed`),
  `CompletedOI.lean` and `CarrierGeneralOIPlus.lean` (OI⁺), `ImplementationLocality.lean`, `MinimalRepertoire.lean`,
  `PositivePackage.lean`, `StructuralClosure.lean`, `SubstratumSource.lean`, `SubstratumInterface.lean`,
  `PhaseSource.lean`, `ReadWriteControl.lean`, `DerivedQ3.lean`, `LiftAudit.lean`, `ExecSource.lean`,
  `LiftSource.lean`, `EmbeddedObservation.lean`, `ReferenceExtension.lean`, `SpectatorBridge.lean`,
  `MicroscopicReversibility.lean`, `PositiveReachability.lean`, `TypedCompletion.lean`, `TypedPositive.lean`,
  `QuasilocalAlgebra.lean`, `QuasilocalCharacterization.lean`, `SecondOrderDrive.lean`, `JordanClassification.lean`,
  `OperationalRigidity.lean` — the matrix-level and general-carrier layer, with every bridge theorem between the
  matrix level and the field-neutral pair level named or its absence recorded.

**Deliverables of each inventory thread** (`pt/I1/` … `pt/I4/`): `INVENTORY.md` (the records), `CENSUS.md` (the
three censuses with the mapping and the out-of-scope list), `NOTES.md`, `RESULT.md` (§0: counts by kind, status and
level; every item with `bearing` other than `none at L`; every bridge found and every bridge absent; the
do-not-assume items; §1 the inventory by section; §2 ledger of sources read; §3 what is not claimed — in
particular no status upgrade and no derivation; §4 evidence log with hashes; §5 integrity).

## Step 2 — the dependency graph (after step 1; thread G, directory `pt/G6/`)
Nodes are the records of I1–I4 merged by the coordinator into `pt/audit/stage6-inputs/INVENTORY-MERGED.md` (ids
kept); edges are `depends_on` (hypothesis of) and `yields`; lemmas are edges. Strata: (S0) what follows from
Axioms 1–2 alone; (S1) what needs C1–C4; (S2) what needs the operational hypotheses of the K programme; (S3) what
needs OI⁺-type or implementation principles; (S4) empirically motivated or physical-layer items; each node carries
its level and its bridge. Output: `GRAPH.md` and a machine-readable `graph.json`, with a check that every node has
a status and every edge a source; the list of every path from S0–S2 to any node at level P; the list of nodes at
level P with no incoming path from S0–S2 (the unsourced pair premises).

## Step 3 — reassessment of the stage-4 countermodels (after step 2 and the stage-5 audit; thread R, `pt/R6/`)
For each exotic cone and seed (`K(E0)`, `K(Z_F)`, `K({F, cnot F})`, `K(e_c)`, the stage-4 and stage-5 EBF seeds):
for each applicable item of Π_app(L): satisfied / violated / not applicable (no bridge), with an exact check wherever
the item is checkable on the cone; and the realization question: whether a pair whose operational cone is `K` admits
an embedded-observer realization at level H (Axioms 1–2, C1–C4, the reversible realization theorems) —
realization exhibited / obstruction proved / open with the missing bridge named. Every "violated" is a candidate
exclusion and is pressure-tested: the item's status, its level, its bridge, and whether it is a do-not-assume item.

## Step 4 — the test of (b) (after step 3; threads named by amendment)
Derivation attempts from Π_app(L) at the proved status, the full countermodel if they fail, the missing assumption
isolated, and the verdict in the two-way form with CONDITIONAL where an assumed item is used.

## Rules
As `PROTOCOL-STAGE5.md`: read-only on `pt/base/`; exact arithmetic; decision rules in headers before the first run;
`python3 -I -B`; byte-identical replays; failed runs kept; evidence levels; no do-not-assume item inside a
derivation except as the item under test, named; `Q3` only as a comparison object. Working directories for step 1:
`pt/I1/`, `pt/I2/`, `pt/I3/`, `pt/I4/` (none exists at launch; a thread that finds its directory present stops);
`.start_marker` first; the anomaly sweep excludes the sibling directories `pt/I*/`, `pt/D5/`, `pt/C5/`, `pt/audit/`
and `pt/audit*-replay/`. Read: everything under `pt/` except `pt/audit/stage3-inputs/OWNER-*`,
`pt/audit/stage4-inputs/OWNER-*`, `pt/audit/stage5-inputs/`, `pt/audit/stage6-inputs/`, `pt/audit/reviews/`,
`pt/audit/aborted-launches/`, and except the sibling threads' directories while they run (`pt/I*/` other than one's
own, `pt/D5/`, `pt/C5/`). Later steps' directories are fixed by append-only amendment when launched.

## Deliverables of the stage (coordinator)
`pt/INTEGRATION-NOTE-STAGE6.md`: the merged inventory and graph (by reference), the countermodel reassessment, the
verdict in the owner's two-way form with every CONDITIONAL item named at its status, the isolated missing
assumption, and what remains; the evidence archive; the report.
