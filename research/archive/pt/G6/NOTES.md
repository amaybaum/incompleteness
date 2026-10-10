# G6 NOTES — stage 6 (Q-EX-FULL), step 2: the dependency graph

Thread G6. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`, read-only). Governing texts:
`PROTOCOL-STAGE6.md` (`b277b7c1…`) and its amendment 1 (`59019538…`, §A1.4 the assignment; §A1.2–A1.3,
§A1.7 binding); `pt/audit/stage6-inputs/I-audit/AUDIT-I.md` §4–§5 binding. Running record; UTC times from
`date -u`.

## N0 — 17:56:31Z start

`.start_marker` written first into `pt/G6/` (absent at 17:56:15Z). All start checks green: six manifests
exit 0; `ns.manifest` OK; HEAD = L, porcelain empty, no bytecode; eleven protocol files at their prefixes,
sidecars OK. No `pt/R6/` or `pt/T6/` existed at 17:56:31Z.

Governing texts read in the instructed order (17:56–18:00Z): PROTOCOL-STAGE6, its amendment 1, AUDIT-I,
PROTOCOL-STAGE5 with amendment 1, PROTOCOL-STAGE4, PROTOCOL, amendments 1–2, INTEGRATION-NOTE-STAGE5,
INTEGRATION-NOTE-STAGE4, `pt/base/AGENTS.md` 41–94, §A.21, §A.26, §A.31. Step-1 RESULT files I1–I4 read in
full. Inventory formats inspected (headers and field conventions only) before any node was processed.

## N1 — 18:02Z productivity test and decision vocabulary (fixed before the first node)

**Productivity test (§A.31, fixed now).** A finding of this thread is a gem iff it is (1) an exact,
mechanically checked statement about the graph at a stated scope (an edge completed from a kernel signature
with file:line; a path, or the proved absence of a path, between named node sets), (2) an exact obstruction
for a stated class of routes (no path, under the stated edge rules, from the descendants of Axioms 1–2 to the
premises of a named pair-level object, with the missing edge named by its obligation), or (3) an exposed
hidden assumption (a recorded dependency field that omits a kernel hypothesis; an edge that crosses levels
with no kernel theorem; a do-not-assume item reached as a premise; a class assignment that changes when a
manuscript-only edge is removed). Anything else is record-only. Output labels per §A.31: NEW / POSITIVE /
ELABORATING / CONFIRMING / BORDERLINE.

**Graph.** Nodes: the 633 inventory records by id (`I1.1`–`I1.85`, `I2.1`–`I2.113`, `I3.1`–`I3.187`,
`I4.1`–`I4.248`), never renumbered, never merged (AUDIT-I §4). An edge `u → v` reads "`u` uses `v`" (`v` is a
hypothesis, premise or definition of `u`). Edge kinds:
- `R` — recorded in `u`'s `depends_on`: an id, an id range (expanded), or a kernel name that resolves to the
  record carrying that name;
- `RA` — "as `Ix.n`" in a `depends_on` field: `u` inherits the resolved `R` targets of `Ix.n`;
- `RN` — recorded kernel name that resolves to no record: target `K:<name>` (a declaration at L) or
  `D:<name>` (a design-module declaration, for [D] records); the existence check looks it up in the tree;
- `KC` — kernel completion: a hypothesis of `u`'s declaration at L (a declared argument whose type is a
  proposition, file:line cited) that the recorded field omits; target resolved as for `R`/`RN`;
- `Y` — from a `yields` field (`v` yields `u`): kept in the edge table as a separate kind, never used in the
  partition or the meeting analysis, used once as a robustness control (the analyses are re-run with `Y`
  edges added and any change is reported).
Free-text hypotheses that are neither an id nor a kernel name are kept per node in the column *named
hypotheses*, not as edges.

**Levels.** A node's span is the set of level letters in its `level` field (H, O, P, M, G, X). An edge is
cross-level iff the spans of its ends are disjoint. A cross-level edge is *kernel-supplied* iff its source is
a kernel declaration at L (status proved [K] or a kernel definition) whose statement names the target object;
otherwise it is *manuscript-asserted* (manuscript, PT-record or [D] source). Paths that count as bridges in
item 3 use only within-level edges and kernel-supplied cross-level edges; manuscript-asserted cross-level
edges are listed separately.

**Derived.** A node is derived at L iff its status is proved (proved [K], kernel status `K`, proved [M],
proved [manuscript, not K]) or conditional-on (a derivation from named items). Every other status
(assumed, definition, open, empirically motivated, refuted, [D], PT-record, scope statement, split
statuses without a proved part for the general item) is non-derived. Statuses are read, never changed.

**Root categories** (for non-derived nodes; assigned by the table in N2, fixed before classification):
`AX` (Axiom 1, Axiom 2); `C1`, `C2`, `C3`, `C4` (the hidden-sector conditions and their recorded variants);
`FOUND` (an H-level posit of the observation base that is none of C1–C4 and not physical: an adopted reading,
the definition of an observation, the measure choice); `OPER` (an operational hypothesis: any non-derived
item at level O, P, M or G, every do-not-assume item, every K-programme premise, H1–H3, (b), P-STAGE2,
P-ACT2, K2, the OI⁺ conjuncts, implementation locality, structural closure of an extension,
`LayerFlowExecutable`); `PHYS` (a physical hypothesis: level X, status empirically motivated, the Substratum
axioms A1–A6, named physical hypotheses such as H-Bell, H-local-lift, M1-T, (EM), total finiteness); `DEF`
(a definition with no truth value).

**Partition (A1.4 item 1)**, for a derived node `u` with closure roots `R(u)` (every non-derived node
reachable from `u` by `R`/`RA`/`RN`/`KC` edges, traversing through non-derived nodes, with the named
hypotheses of every node met, each categorized):
- (a) no root outside `AX`, `FOUND`, `DEF`: sub-label `a0` (no `AX` root: premise-free, a closed statement
  about defined objects), `a1` (`AX` and `DEF` only), `a2` (`FOUND` present, named);
- (b) some C-root, no `OPER`, no `PHYS` (which of C1–C4 named);
- (c) some `OPER` root, no `PHYS` (named);
- (d) some `PHYS` root (named; any `OPER` roots named as well).
A non-derived node is a generator: Axioms 1–2 in (a) (sub-label `gen`), the C1–C4 records in (b) (`gen`),
every other non-derived node in (e), sub-labelled by its category and kind (definition, hypothesis-structure,
hypothesis, obligation, [D], PT-record, refuted, scope). The extension of (e) beyond "definitions and
hypothesis-structures" to every non-generator item without a derivation at L is stated in GRAPH.md.

**Check outcomes (item 4)**: per check `PASS` / `FAIL`; per sampled theorem `AGREE` (graph dependencies ⊇
the signature's propositional hypotheses, and every recorded kernel-name dependency occurs in the
declaration), `INCOMPLETE-RECORDED` (the recorded field misses a signature hypothesis that the graph
completes by `KC`), `DISAGREE` (the graph misses a signature hypothesis, or carries a dependency absent from
the declaration with no recorded reason). A `VERDICT` line prints only if every check and every
countercontrol passes.

**Meeting (item 3)**: `MEET-K` (a path from a descendant of Axioms 1–2 into the premises of a pair-level
object whose cross-level steps are all kernel-supplied), `MEET-MS` (a path only through manuscript-asserted
cross-level edges), `NO-MEET` (no path); each missing link named by the obligation that would supply it.

## N2 — 18:11Z parse and edges; the root-category table (fixed before classification)

**parse.py** (18:04Z, run 1, exit 0): 633 records, P1–P3 and countercontrol C1 PASS, `VERDICT PARSE VALID`;
565 id edges (R, RA), 495 yields edges, 0 dangling ids. **edges.py**: run 1 (18:08Z) printed `VERDICT EDGES
VALID` but review of its completion log showed one-letter title fragments and bound variables resolved as
records (`V`, `S` from I1.4's title `V ⊊ S`; `T.`, `E`); kept as `edges.run1.*`; resolution rules amended in
the header (not the decision rule). Run 2 (18:10Z) resolved an unqualified name against opened namespaces
before the source's own (I4.102 took the qubit `ObservationalIndependence`); kept as `edges.run2.{out,err}`
(the run-2 script was amended in place, the amendment written into the header). Run 3 (18:10:43Z) is final:
1054 edges (R 801, RA 31, RN 70, KC 152), 495 `Y`; E1–E3 PASS. Every one of the 13 ambiguities resolves to the
declaration the source text qualifies or shares a namespace with (checked by reading `OIPlusEmbedded`,
EmbeddedObservation.lean:366–368, which writes `OIHierarchyGeneral.ObservationalIndependence`). Edits to the
scripts between runs were made with inline Python editing helpers reading stdin (not evidence runs).

**Root categories of non-derived nodes** (applied by `classify.py`; first matching rule wins):
1. `AX`: I1.1, I1.2.
2. `C1`: I1.20 · `C2`: I1.21, I1.22 · `C3`: I1.23 · `C4`: I1.24, and the kernel C4 forms I1.70, I1.71, I1.72,
   I1.73.
3. `FOUND` (observation-base posits, neither C1–C4 nor physical): I1.4 (perspectival reading), I1.6
   (definition of an observation), I1.9 (Lemma 2, definitional), I1.12 (selected measure), I1.13 (measure as
   realization datum), I1.14 (reversibility fallback).
4. `PHYS`: I1.5 (that our universe lies in the observer-admitting subset), I1.10 (bijective representative,
   empirically motivated), I1.11 (total finiteness), I1.36 (M1-T), I1.61 (A6 readings), I1.63–I1.68 (Substratum
   A1–A6), I1.74 (physical C4 discharge), I1.77 (declared inputs), I2.6 (adopted Bell branch), I2.46 (open
   variational identity, H), I2.73, I2.76, I2.86, I2.87, I2.102, I2.113.
5. `NEUTRAL` (framing, scope, status or restatement records whose content is carried by their own edges):
   I1.16, I1.18, I1.19, I1.26, I1.37, I1.76, I1.78, I2.70, I2.78, I2.84, I2.85, I2.110, I2.111, and every
   record with status `scope statement`.
6. `DEF`: status a definition (`-`, `definition`, `definition [K]`, `definitions [K]`, `proved [K]
   (definition)`), and the hypothesis-structures discharged for the one object they are stated on: I1.38,
   I1.39 (`CoreC1C4`, proved for the core), I1.42 (`SealedCoreIsFiniteOI`, proved for the core), I1.57.
7. `OPER`: every other non-derived node whose span meets {O, P, M, G}, or whose flag is do-not-assume.
8. `PHYS`: every other non-derived node at level H or X (none expected after rules 1–7; any is listed).
External kernel targets `K:<name>` and design targets `D:<name>` carry no category of their own unless the
name is Prop-valued or a structure at L, in which case `OPER` (level of the source: a kernel hypothesis).

**Named (free-text) hypotheses** of a node, first matching rule: (n) pure references (module or file names,
thread names, citation brackets, remarks such as "negated", "presupposition") are dropped; (c) `C1–C4` → all
four, `C1`…`C4` → that one, "persistence" → `C2`, "readback" → `C4`, "recurrence" → `AX`; (f) "counting
measure", "Lemma 3" → `FOUND`; (m) purely mathematical setting ("finite visible alphabet", "finite horizon",
"initial law", "rational law", "finite order", "bijection", "non-permutation", "ρ_H", "[U,R_g]", "gaps",
"genericity", "q prime", "uniform" (a law), "faithful deterministic realization", "response-complete") →
`DEF`; (o) operational vocabulary ("inert spectators", "reversible control", "iterated composition", "valid
probabilities", "trivial-ancilla", "three principles", "OI core", "well-formedness", "phase intervention",
"controllability", "typed operational", "operational lift", "quantum experiment", "instrument", "interventions",
"ancilla", "OI_Q", "observable algebra", "observer projection", "QM description") → `OPER`; (p) physical
vocabulary ("mixing hypothesis", "ETH", `E1`–`E7`, "M1-T", "M1-B", `A1`–`A6`, "H-local-lift", "H-scramble",
"H-Bell", "holographic", "Liouville", "typicality", "determinism", "setting operations", "readout", "ensemble",
"nearest-neighbor", "translation invariance", "range-1", "coupling", "energy-conserving", "site factorization",
"spatial locality", "wave equation", "foliation", "lattice", "staggered", "Barandes", "finiteness",
"trace-out", "gauge", "commutation") → `PHYS`; otherwise the level of the node carrying it decides (X or H
→ `PHYS`, O/P/M/G → `OPER`), and the piece is listed as level-defaulted in GRAPH.md.

## N3 — 18:16Z classification; graph.tsv

**classify.py** run 1 (18:13Z, exit 0, `#VERDICT GRAPH VALID`, G1–G3 PASS) kept as `classify.run1.*`. Review of
its (d) list showed the N2 rules written for the manuscript H level acting on kernel records: rule 8 sent ten
kernel hypothesis-structures at level H (I4.50, I4.60, I4.149, I4.156, I4.198, I4.226, I4.227, I4.242, I4.247,
I4.248 — I4's substratum-class objects, which I4's header states are matrix-level theories or classes) to
PHYS, and the level default sent kernel binder fragments ('Fin 2', 'Λ nonempty', 'T (T on Fin 2') to PHYS.
The amendment (classify.py header, A1–A4) is post hoc and is disclosed as such: it re-scopes two N2 rules
to the records they were written for; it touches no edge and no status. Run 2 (18:14Z) is final.
Sensitivity, run 1 → run 2: a0 74 → 104, b 13 → 15, c 178 → 171, d 63 → 38; the (e) categories move only
between PHYS and OPER for the ten records named. Outside I1, run 1 places only I2.11 (a2) and I2.54 (b, C4)
in (a1), (a2) or (b); run 2 adds I2.53 and I2.61 to (b) (C2, from the free-text pieces restored by edges.py
run 4: 'τ_B ≪ τ_S', 'C2 (I1)'). All are manuscript H-level records. Re-running both final scripts after correcting two
timestamps in the amendment headers gave byte-identical outputs (`cmp`; the temporary outputs were written in
`pt/G6/` and removed). `graph.tsv` is a byte copy of `classify.out` (sha256 identical).

**Pair-level seed set for item 3** (fixed now, before `analyze.py` is written): `W d` I3.1, `actT` I3.6,
`actC` I3.7, `cnot` (with `nflip`, `z3`, `phiW`) I3.11, `CandidateCone` I3.43 (the kernel's admissible `K`),
H1 I3.147, H2 I3.148, H3 I3.149, (b_S4) I3.150, (b_n) I3.151, (b_R1) I3.152, (b_DJ) I3.153. Ancestors: every
node reachable from a seed by R, RA, RN, KC edges (its premises, transitively). Descendants of Axioms 1–2:
every node from which I1.1 or I1.2 is reachable by the same edges. Robustness control: both sets recomputed
with `Y` edges added.

**Obligation table for missing links** (from AUDIT-I §5, I3's B1–B7 / A1–A13, I4's bridge findings; a
root of the pair ancestor set not in this table is printed with its own `bridge` field and marked unmapped):
- manuscript H → kernel H: none at L as a theorem; the kernel carries images only (`SealedCoreIsFiniteOI`,
  `CoreC1C4` on one eight-state carrier; ManuscriptAxioms.lean:18–26 "images, not the axioms"; I1.55, I1.56);
  nearest open row: the stochastic observer interface (I1.76, ROADMAP.md:69, OPEN).
- H or M or G → O: K∞ (I3.166) and its seams K∞-Stage I3.167, K∞-Act I3.168, K∞-Drive I3.169, K∞-Trans
  I3.170, K∞-Seed I3.171, K∞-V4 I3.172, K∞-Copy I3.173 (OPEN).
- H or M or G → P: K2 (I3.165; ROADMAP.md:1001–1005, OPEN: two-copy local tomography; local actions compatible
  with the composite cone).
- per seed root: I3.1 `W d` (local tomography encoded) → K2; I3.43 `CandidateCone` and H1 I3.147 (products in
  `K`, `K ⊆ maxCone`) → K2 (`hadm`); closedness `hcl` I3.131 → P-STAGE2 I3.145; H2 I3.148 and `hgate` I3.132 →
  P-ACT2 I3.146; H3 I3.149 → none at L (no ROADMAP row; `dualW`, `ipW`, `Q3` design-only, AUDIT-I §5.4);
  (b) forms I3.150–I3.153 and IE1 I3.137 → K2 ("local actions compatible with the composite cone") with
  K∞-Act I3.168 and K∞-Drive I3.169 (availability of the flow and `J`); `IsNot` I3.8, `NativeGate` I3.9,
  `GateRel` I3.23, `CtrlGate` I3.29 → K1 I3.164 (CONDITIONAL) for the selector, P-ACT2 for the gate as an
  operation of the pair system; `EffectsOn` I3.48 → K∞ (effect soundness); `SharpSeed` I3.73 → K∞-Seed;
  `PreservesBody` I3.74 → K∞-Act; `SeedOrbitAvailable` I3.75 → K∞-V4; `BoundaryTransitive` I3.76 → K∞-Trans;
  `ElementaryDrivability` I3.66 → K∞-Drive; `DirectedStages`/`SCInf`/`FiniteRank` I3.92/I3.94/I3.96 →
  K∞-Stage; `OpDatum` I3.99 → K∞-Act; COMP-1 `PreComposite`/`Composite`/`LocallyTomographic` I3.114–I3.116 →
  K2 (adapter to `W d` open).

## N4 — 18:24Z analysis and check

**analyze.py**: run 1 (on the graph of classify run 2) had its output overwritten by run 2 (the same script on
the graph of classify run 3; the two graphs differ only in I3.11's sublabel) — a deviation, recorded here; run
2 kept as `analyze.run2.*`; run 3 (amended discharge extraction, header) is final. Results (item 3, depth-first
on the decisive branch): **NO-MEET**. Anc(P) = 25 nodes, all at levels P and O; Desc(AX) = 31 nodes, all
manuscript H records plus two kernel H theorems (I1.84, I1.85, reached through their recorded links to Lemmas 2
and 3); shared nodes 0, with and without `Y` edges (Anc 32 / Desc 41 with `Y`, shared 0). Countercontrol (a
synthetic edge I3.1 → I1.1) returns MEET-K. Pressure test of the favourable-to-closure direction: none needed
(the result is a non-meeting); pressure test of the non-meeting: it survives adding every `yields` edge and
counting manuscript-asserted cross-level edges (the shared set is empty even over all edges), so it does not
rest on the level rule. Class: CONFIRMING (AUDIT-I §5.3 at the level of the whole record graph) with one NEW
element: the descendant set of Axioms 1–2 contains no kernel declaration outside level H, and the ancestor set
of the pair objects contains no node at H, M or G.

**check.py**: run 1 (18:21Z) C2 FAIL, C3 FAIL (11 DISAGREE); review found its C3 stricter than N1 ("no recorded
reason" omitted) and blind to records whose kernel names stand in their statements; amended (header), run 2
(18:22Z) C3 4 DISAGREE; the cycle printed differed between runs 1 and 2 because the search started from an
unordered set (string-hash seed); amended to numeric order with a full SCC listing; run 3 (18:23Z) final:
C0 PASS, C1 PASS, **C2 FAIL** (two 2-cycles: I2.6 ⇄ I2.10, I2.42 ⇄ I2.56, each between two assumed records),
**C3 FAIL** (44 sampled: 19 AGREE-RECORDED, 21 INCOMPLETE-RECORDED, 4 DISAGREE: I2.25, I2.36, I2.96, I3.105),
CC1–CC3 behave; no VERDICT line. Both failures are findings about the step-1 records, not repaired here (no
record is edited; the graph keeps the recorded edges).

**18:25Z.** classify run 3 (I3.11 plural-definition fix, 18:18Z) and run 4 (18:25Z: rule A3 had not reached
I3.184 because the noise test dropped its condition text '(Main.md:352)'; file references are now removed
from status-condition pieces first) — run 3 kept as `classify.run3.*`; run 4 final: a0 103, c 172 (I3.184 →
c). `graph.tsv` re-copied from `classify.out`. analyze.py (run 3 script) and check.py (run 3 script) were re-run
on the final graph; their earlier outputs on the run-3 graph were overwritten (scripts unchanged; the graphs
differ in I3.184's class only); results unchanged: NO-MEET; C2 FAIL, C3 FAIL (4 DISAGREE).

**18:27Z.** classify run 5: the implementation read 'proved' inside the component lists of two scope
statements (I2.3, I2.69) as their own status, against N2 rule 5; fixed (header amendment), run 4 kept as
`classify.run4.*`. Final partition: a 109 (gen 2, a0 103, a1 1, a2 3), b 15, c 172, d 36, e 301. graph.tsv
re-copied; analyze.py and check.py re-run on it (scripts unchanged, earlier outputs overwritten): NO-MEET;
C0 PASS, C1 PASS, C2 FAIL, C3 FAIL (4 DISAGREE), countercontrols behave.

## N5 — 18:31Z GRAPH.md, replays

GRAPH.md written in parts (each write ≤ 250 lines; §3's table of the 75 flagged rows formatted with `awk` from
`analyze.out` S2/S2d into a temporary file `s3.tmp` inside `pt/G6/`, appended, and removed). Corrections made
to GRAPH.md after reading its own counts against the outputs: (d)/(e) totals after classify run 5; the M ↔ G
cross-level count (34, first written 28); the supply wording for I2.3 → I2.17; the incomplete-record list
(I1.54, I2.27 added).

Replays (18:30:49Z–18:30:51Z), each final script run again into `<name>.replay.{out,err}` and compared with
`cmp`: parse, edges, classify, analyze, check — 5/5 byte-identical on stdout and stderr. `graph.tsv` is
byte-identical to `classify.out`.

Fixed point (§A.31): after the classify and check amendments, three further passes over the outputs (the
partition lists against `graph.tsv`; the meeting computation with `Y` and over all edges; the sampled
signatures against `check.out`) produced no NEW finding beyond N4's; the thread's question (A1.4 items 1–5) is
answered. Gems: NEW (descendant set of Axioms 1–2 confined to level H; Lemmas 1–3 not consequences of Axiom 1
alone in the records; two co-presupposition cycles and four recorded dependencies absent from their
declarations); CONFIRMING (NO-MEET, the missing links K∞ / K2 / P-STAGE2 / P-ACT2 / K1 / none for H3);
BORDERLINE (the physical / operational convention for roots, a sensitivity between (c) and (d) only).

## N6 — 18:31:23Z end marker

`.end_marker`: six manifests exit 0; `ns.manifest` OK; HEAD = L, porcelain empty, no bytecode under `pt/base`
or `pt/G6`; eleven protocol files at their prefixes, sidecars OK. Top-level listing against the start: new
name `R6` (18:31:06Z, the sibling thread's directory; names only, never read); `pt/` itself and `G6` modified.
Sweep (files newer than `.start_marker`, pruning `pt/G6/`, `pt/R6/`, `pt/T6/`, `pt/I1/`–`pt/I4/`, `pt/D5/`,
`pt/C5/`, `pt/audit/`, `pt/audit*-replay/`): no file; the only path printed is the directory `pt` (its mtime
changed when `R6` was created). No anomaly; nothing quarantined; no `evidence/` directory was needed. Every
write of this thread is inside `pt/G6/`; temporary files (`*.tmp`) were written there and removed. RESULT.md
follows, with the sha256 of every other file in `pt/G6/`.
