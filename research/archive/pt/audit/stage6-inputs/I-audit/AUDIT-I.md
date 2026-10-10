# Audit of the stage-6 inventory threads I1–I4 (Q-EX-FULL, step 1: complete premise inventory) — coordinator

Base L = `9f9f8257…` (read-only). Governing text `pt/PROTOCOL-STAGE6.md` (`b277b7c1…`). Threads: I1
(foundations, `pt/I1/`, 85 records), I2 (theorems and physical layer, `pt/I2/`, 113 records), I3 (K programme and
composite, `pt/I3/`, 187 records), I4 (OI⁺ and completion, `pt/I4/`, 248 records). Written 2026-10-10, 17:58Z,
before step 2 is launched.

## 1. Records and integrity

- **Hashes.** Every file each thread lists in its RESULT §4 verifies on disk: I1 76/76, I2 77/77, I3 53/53, I4
  73/73 (`HASH-VERIFY.txt`); the only unlisted file in each directory is RESULT.md itself, whose hash matches the
  value each thread reported (I1 `64b0bc27…`, I2 `50aecb7f…`, I3 `84ba625f…`, I4 `0467cb98…`). All `.err` files are
  `exit 0` except I4's kept failed run `decl_dump.run1.err`.
- **Replays.** Every final script of the four threads (31 scripts; none writes a file) replayed by the coordinator
  from each thread's directory into `replay/<thread>/`: 31/31 byte-identical on stdout and stderr
  (`replay/REPLAY-LOG.txt`, 17:47:10Z–17:47:27Z).
- **Start/end checks.** Each thread: manifests 6/6, `ns.manifest` OK, base HEAD = L with empty porcelain, ten
  protocol prefixes and sidecars OK at start and end; sweeps found nothing outside the excluded areas (the four
  threads excluded their siblings and `pt/D5/`, `pt/C5/`, `pt/audit*`), so none quarantined anything.
- **Disclosed deviations** (none affecting a record): I1 deleted the replay files of `quote_check` run 5 after
  `cmp` against the kept run; I2 did not keep one dry run and amended two census scripts in place between runs
  (each amendment written into the script header; the run-1 version of one kept); I3 and I4 each wrote one
  temporary hash list outside their directories (`scratchpad/I3-hashes.tmp`, `scratchpad/hashcheck_i4.txt`,
  both one level above `pt/`, both deleted at once); I4's `decl_dump` run 1 failed its own control and is kept.

## 2. Coordinator's mechanical check of the central negative finding

All four threads report that no theorem at L carries a substratum-level (H), matrix-level (M) or general-carrier
(G) statement to the pair cone (P: `W 3`, `K`, `actC`/`actT`, `cnot`). My own import-graph computation over the
Lean tree at L (`verification/lean-mathlib/`, 214 modules plus the root): the only module whose import closure
reaches both a pair-level module (`CompositeDimension`, `K2Guard`, `KInfFoundations`) and a matrix/substratum/
general module (`OperationalAssembly`, `CompletedOI`, `RouteB`, `StructuralClosure`, `TypedCompletion`,
`QuasilocalCharacterization`, `ReferenceExtension`, `ImplementationLocality`, `LiftAudit`) is the root aggregator
`OIBridge`; the closures of the three pair-level modules contain none of the listed matrix modules; the direct
importers of `CompositeDimension` are `EffectSpace` and the root. This confirms I3's exposed fact 1 (the K
modules are a leaf cluster), I4's bridge finding and I4's marker 3 (the Kₙ audit's "imported by no module" held at
95cb01ff; at L `EffectSpace` and its descendants import it).

Spot checks of the threads' other mechanical claims at L: no `.lean` file defines `pauliW`, `Q3`, `twin` or
`pauli1` (I4 marker 1; grep count 0); `control_of_lieRank` MicroscopicReversibility.lean:114,
`inverseAccessibility_of_lieRank` :132, `universalReachability_of_lieRank_positive` PositiveReachability.lean:996,
`parallel_of_observationalIndependence` at CompletedOI.lean:147 and CarrierGeneralOIPlus.lean:87, namespaces
`OIHierarchy` (CompletedOI.lean:77) and `OIHierarchyGeneral` (CarrierGeneralOIPlus.lean:50) (I4 marker 4).

## 3. Spot checks of the threads' corpus findings (all confirmed by reading at L)

- I2 finding 1: Equivalence.lean:150–155 says of class (D) that the initial law "is not required to factor as
  visible prior × hidden prior" and that the stronger form "is NOT what this theorem's class `(D)` asks for";
  Main.md:500 is the constructive proof of the finite-horizon process-dilation theorem. The record of a kernel
  anchor weaker than the cited manuscript statement is correct.
- I2 finding 2: the only occurrence of "Kochen" in Main.md is line 562 ("Kochen–Specker inheritance (§3.2)");
  Main §3.2 is "Independent Derivation via Stinespring Dilation". The cross-reference is dangling within Main.
- I2 finding 3: ROADMAP.md contains no row for `H-local-lift` (named GR.md:328), `H-observer-bundle` or
  `H-Y-vertex`; `H-blind` appears only at ROADMAP.md:1122 inside the H-link paragraph.
- I1 status variances: ch01-observation.md:55 defines C2 as "Slow-bath timescale separation" while Main.md:76
  states "(C2) Memory persistence … in two named forms"; ch01:71 says "The framework's four conditions are
  therefore *logically* independent" while Main.md:602 says "only (C4) is logically independent. (C1) follows from
  it … and (C3) follows by data processing"; ch01:26 says "a deterministic dynamics" where Main.md:44 says "a
  dynamics". These are book-versus-papers divergences of the kind §A.25 governs. Under the manuscript hold they are
  recorded here for the owner and not edited.

## 4. Merge decisions for steps 2–4

- The four inventories are used as they stand, by their id namespaces (`I1.n`, `I2.n`, `I3.n`, `I4.n`); no
  renumbering, no physical merge (ids are identifiers, §A.30). Overlaps are cross-references: OI⁺ and the five
  completion conditions appear at the manuscript level in I2 (I2.29–I2.35) and at the kernel level in I4
  (I4.65–I4.70, I4.82–I4.105); the OI core in I1 (I1.38–I1.48); K2 and the pair premises in I3 (I3.145–I3.165).
- The partition of Main §1–§3 between I1 and I2 is accepted as the threads drew it.
- Coverage limits stand as the threads state them (I1: three observer modules not censused whole; I2: sentence
  census inside 26 sections, book by mirror phrases; I3: theorems lemma-folded by round; I4: 1164 theorems
  lemma-folded by module). Step 2 may add records for items it finds load-bearing; it may not change any status.

## 5. Findings carried to step 2 (the graph)

1. Every do-not-assume item (I4's 44, I3's nine, I2's eleven) stands at status *assumed* or *hypothesis* at L,
   except where a kernel theorem discharges it for a particular object (`StructurallyClosed substratumClass`,
   `HasParallelReferenceExtension` for the full theory). None is a premise of any derivation in the inventories.
2. The only O→P bridges at L are I3's B1–B7: effect-availability transfer (`maxConeOf_avail_eq` and its dense
   form), products in `maxCone`, the carrier-map identities on products, the Lorentz effect cone, the π-rotation NOT
   and `eball_three`. None transfers an operation beyond products or an involution; none transfers a flow, `J`, or
   `cyc3`.
3. H→M bridges exist (I1.41–I1.60: the core realized at the matrix level) and M↔G links exist (I4: shadows, gate
   flows at stage level, substratum dynamics into the quasilocal algebra); no H→P, M→P or G→P bridge exists.
4. The K∞ geometric premises are elementary-scoped (I4.236); the matrix-level `Q3` self-duality cited by the PT
   stage protocols passes through a dictionary (`pauliW`) defined only in design modules (I3 fact 4, I4 marker 1):
   an assumption-watch marker for every PT-stage result that uses H3 or the comparison object `Q3`.
5. The manuscript divergences of §3 are propagation items, not premises.

## 6. Verdict

Step 1 is complete and audited: four inventories, 633 records, three censuses each with no unmapped entry, every
status the one the corpus fixes, no derivation attempted, no bridge from the hidden-history or matrix levels to
the pair cone at L. Steps 2–4 proceed under amendment 1 to the stage-6 protocol.
