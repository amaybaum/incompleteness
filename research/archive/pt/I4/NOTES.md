# pt/I4/NOTES.md — running record (thread I4, stage 6, Q-EX-FULL; inventory: generalization and completion)

Clock times are UTC from `date -u`. Read-only on the corpus; writes only inside `pt/I4/`.

## N0 — start (16:52:52Z)
- Directory `pt/I4/` absent at launch; created; `.start_marker` written first (16:52:52Z), then the four start
  checks appended (manifests 6/6 + ns OK; base HEAD 9f9f8257…, porcelain empty, no bytecode; ten protocol files at the
  expected prefixes, sidecars OK; `pt/` top-level listing with mtimes, 64 names). All passed.

## N1 — governing texts read (by 16:54:33Z)
- `PROTOCOL-STAGE6.md` (b277b7c1…) in full: record schema; censuses (a)/(b)/(c); I4 scope; deliverables.
- `PROTOCOL-STAGE5.md` (9e01f098…), `PROTOCOL-STAGE5-AMENDMENT-1.md` (1f639115…), `PROTOCOL-STAGE4.md`
  (d3da2811…), `PROTOCOL-STAGE3.md` (1a649168…), `PROTOCOL.md` (239dc123…), `INTEGRATION-NOTE-STAGE4.md`,
  `INTEGRATION-NOTE-STAGE3.md`; `pt/base/AGENTS.md` (959c4333…, byte-identical to the working copy's AGENTS.md).
- Not read (protocol exclusions): pt/I1, pt/I2, pt/I3, pt/D5, pt/C5, pt/audit/stage{3,4}-inputs/OWNER-*,
  pt/audit/stage5-inputs, pt/audit/stage6-inputs, pt/audit/reviews, pt/audit/aborted-launches.
- Scope check at L: all listed modules present except `OIHierarchy`, which is a namespace, not a file:
  `namespace OIHierarchy` is CompletedOI.lean:77; `namespace OIHierarchyGeneral` is CarrierGeneralOIPlus.lean:50.
  ImplementationLocality.lean's namespace is `InterventionLocality` (:95); EmbeddedObservation.lean's is
  `PrimitiveSource` (:74); MicroscopicReversibility.lean's is `MicroReversibility` (:67).
  "Related passive modules": PassiveIndependence.lean (361 lines), PassiveQuotient.lean (675) beside
  PassiveObservation.lean (365).
- Plan (depth-first, per the launch order): kernel census script first (coverage control (a)); then
  ReferenceExtension, SpectatorBridge, ImplementationLocality, StructuralClosure, LiftAudit; then the OI⁺
  characterizations (GeneralCarrier, CompletedOI, CarrierGeneralOIPlus) and independence theorems; then the
  substratum-source chain; then typed and quasilocal completions; Kₙ census; roadmap census; manuscript cross-refs.

## N2 — kernel census (a) (16:56–16:58Z)
- `census_kernel.py` (decision rule R1–R7 in its header, written before the first run): 35 modules (the I4
  list plus PassiveIndependence, PassiveQuotient). Run 1: exit 0, controls C1–C5 PASS, VERDICT CENSUS VALID.
  Counts: census (a) entries 76; theorems 1164; non-Prop defs 169; non-Prop structures 6; instances 22;
  strict-grep hits 154 outside comments (all parsed) and 3 inside comments.
- `decl_dump.py` (exact docstrings + signatures for the inventory). Run 1 FAILED its control D4a: a Prop-valued
  `def` was printed only to its `:=` line, omitting the body that is the hypothesis' content. Kept as
  `decl_dump.run1.{py,out,err}`. Pre-run edit for run 2 recorded in the header (rule D2 widened to the whole
  declaration for non-theorems). Run 2: exit 0, D4a/D4b PASS, 1415 declaration blocks, 557 headline.

## N3 — bridge scans (16:58–17:02Z)
- `bridge_scan.py` (B1–B6): import closure over the 214 OIBridge modules + root. Only the root aggregator
  `OIBridge.lean` reaches both the pair-level definitions (CompositeDimension.lean:97/:198/:201/:775,
  K2Guard.lean:95) and any of M (OperationalAssembly.lean:594), H (RouteB.lean:279, StructuralClosure.lean:180),
  G (TypedCompletion.lean:165, QuasilocalCharacterization.lean:168); the root has 0 pair-token lines.
  13 modules reach P, 136 reach M, 88 reach H, 85 reach G. VERDICT: no declaration mentions both.
- `bridge_scan2.py`: H widened to the passive hidden-dynamics modules (PassiveQuotient, ControlledQuotient,
  ObservabilityQuotient; 85 declared names), because PassiveQuotient lies in CompositeDimension's import closure
  (chain printed). No pair-level module (12) uses any of those names.
- `bridge_scan3.py`: the single-token level O (KInfFoundations.lean:264 ElementaryDrivability, :425 cyc3).
  22 modules reach O; none but the root reaches O and M/H/G; no I4 module reaches O; JordanClassification,
  OperationalRigidity and PassiveQuotient do not reach M.
- `bridge_scan4.py` (copy of scan 2 with rule E2 changed to the ancestors of CompositeDimension, 23 modules):
  no use of the 85 hidden-dynamics names in the single-token chain.
- N5 (supplementary grep, 17:03Z, not a script): in those 35 chain/pair modules the strings PassiveQuotient,
  ControlledQuotient, ObservabilityQuotient occur once, the import line CoherentExtension.lean:63; no
  qualified use and no `open` of those namespaces. (The scans' matchers exclude dot-qualified names; this grep
  closes that gap.)

## N4 — reading, depth-first (17:00–17:15Z)
- ReferenceExtension (full), SpectatorBridge, ImplementationLocality, StructuralClosure, LiftAudit headers and
  headline declarations; then GeneralCarrier, CompletedOI, CarrierGeneralOIPlus, EmbeddedObservation,
  MinimalRepertoire, PositivePackage, MicroscopicReversibility, PositiveReachability; then the
  substratum-source chain; then typed/quasilocal/Jordan/rigidity/passive modules; the Kₙ census (ledger and
  landed audit); ROADMAP rows; GR.md 206–272 and Main.md 538–570, 624–632 (cross-reference only).
- Location corrections against the launch text (record only): `control_of_lieRank` and
  `inverseAccessibility_of_lieRank` are MicroscopicReversibility.lean:114 and :132, not PositiveReachability.lean
  (which carries `universalReachability_of_lieRank_positive`, :996). `parallel_of_observationalIndependence`
  exists twice (CompletedOI.lean:147, CarrierGeneralOIPlus.lean:87).
- Numbering finding (record only): GR.md:212 numbers the five conditions (i) valid probabilities, (ii)
  trivial-ancilla consistency, (iii) inert spectators, (iv) full reversible control, (v) iterated composition;
  the kernel's PhysicalCompletionConditions (PhysicalCharacterization.lean:295) has the conjunct order validity,
  inert, control, closure, level-one. The records use the manuscript numerals and name the conjunct position.
  First drafts of the records used the conjunct order as numerals; corrected before any render (17:15Z).
- Kₙ audit base: the landed census (audits/foundations/kn-elementary-carrier-census.md) is at base 95cb01ff;
  its "CompositeDimension is imported by no module" no longer holds verbatim at L (K2Guard and 10 others
  descend from it), while the no-shared-import content holds at L except for the root aggregator.

## N6 — the dictionary (17:18Z)
- `dictionary_scan.py` (P1–P4): no `.lean` file under pt/base/verification (221 files, both Lean projects)
  defines `pauliW`, `pauli1`, `Q3` or `twin`, and none uses `pauliW`/`Q3`. The definitions exist only in the
  design module inputs/fourcopy/FourCopyPackage.lean:172/:176/:180/:183 (ff9c3a35, not certified; the file
  contains `sorry`). Assumption-watch marker (record only, no verdict): the stage protocols' `Q3 = {w : pauliW w ⪰
  0}` and the [K] tag on `Q3 = dualW Q3` (PROTOCOL-STAGE3.md:66, citing JordanClassification.lean:84 and
  OperationalRigidity.lean:917, statements on Matrix n n ℂ) pass through a dictionary that is not a kernel object
  at L.

## N7 — records and census mapping (17:04–17:17Z; written at 17:17:38Z)
- records.txt written in parts (≤ 250 lines per write), 239 records I4.1–I4.239 (ids issued once; I4.4a was
  renamed I4.23 before any render, when the renderer's id rule was fixed; cross-references inside records use
  names and file:line, not ids, except backward references in Section E).
- `census_map.py` (M1–M5): 76 census entries: 70 mapped, 6 out of scope (theorem-internal auxiliaries / a
  definition with no hypothesis role), 0 unmapped. VERDICT ALL ENTRIES ACCOUNTED.
- `render_inventory.py` development run `render_inventory.dev1.*` on the first 78 records (placeholder header):
  all source checks passed; kept.

## N8 — pressure tests of the decisive field (bridge), §A.31 skepticism (17:21–17:24Z)
- Root aggregator: no module imports the bare root `OIBridge`; the root's own declarations (cubic-face
  representation theory, ROADMAP §A1/§A5) mention no pair-level or single-token name, qualified or not
  (grep for CompositeDimension, K2Guard, K1Bridge, actC, actT, prodState, maxCone, CandidateCone, NativeGate, cnot,
  eball, "W 3", "W d", KInfFoundations, ElementaryDrivability: 0 hits outside import lines). This closes the
  dot-qualified-name gap of `bridge_scan.py`'s token matcher for the only module that could state a bridge.
- Field: none of the 12 pair-level modules contains the character ℂ (grep, 0 lines each); the matrix level M is
  complex (`Matrix … ℂ`). With no dictionary at L (`dictionary_scan.out`), no kernel object at L maps the real
  bilinear tables `W d` to complex matrices.
- Other Lean trees: the `verification/lean/` project (6 .lean files) mentions none of FiniteOperationalTheory,
  withSpectator, actC, actT. Design modules (inputs/fourcopy, ff9c3a35, [D], not at L): FourCopyPackage.lean
  imports the pair chain (via FourCopyHeadline → … → K2Guard) and MonoidalCompletion, and defines `pauliW`,
  `Q3`, `twin` with open `sorry` obligations — the nearest P-to-matrix dictionary, not certified, not at L, and
  not a link to FiniteOperationalTheory.
- Anchors cited by PROTOCOL-STAGE5.md (L0–L2) all resolve at L; `StructuralClosure.lean:365` is the second line of
  `quantumArchitecture_iff_drives_of_closed`, whose declaration starts at :364.
- Flag added before the final render: `DrivesElementary` (I4.143) carries "do not assume" (the controllability
  resource completing the substratum class); render and counts re-run (run 1 outputs kept as `*.run1.*`).
- Written at 17:22:37Z.

## N9 — final renders, counts, replays (17:19–17:25Z)
- Line-range audit of the record notes (17:23Z): ten cited header ranges corrected to the exact lines
  (ImplementationLocality.lean:85-87, :87-88, :21-26, :58-83; StructuralClosure.lean:68-71;
  OperationalAssembly.lean:591-593; GeneralCarrier.lean:48-51; PassiveQuotient.lean:63-67;
  SpectatorBridge.lean:61-62; reversibleRichness_iff at MicroscopicReversibility.lean:100) and
  physical_of_exactAll at PhysicalCharacterization.lean:301 (not :299). I4.236 gained the census's scope
  sentence (KN-CENSUS-RESULT.md:10-11: "false for complex quantum systems of level ≥ 3").
- Runs of `render_inventory.py`: dev1 (78 records, placeholder header), run1 (248 records, before the
  DrivesElementary flag), run2 (before the line-range corrections), final (248 records): every run VERDICT
  INVENTORY RENDERED; superseded outputs kept as `render_inventory.{dev1,run1,run2}.*` (run2 also with its
  replay). `counts.py`: run1, run2 kept; final VERDICT COUNTS VALID. INVENTORY.md = byte copy of the final
  `render_inventory.out` (cmp identical).
- Replays: census_kernel, decl_dump, bridge_scan, bridge_scan2, bridge_scan3, bridge_scan4, dictionary_scan
  (17:22:54Z), census_map, render_inventory, counts (17:24:24Z): stdout and stderr byte-identical, 10/10.
- Final counts (`counts.out`): 248 records; kind: theorem 140, hypothesis-structure 73, definition-as-hypothesis
  28, obligation 7; status: proved [K] 141, assumed 82, definition (no status) 18, open 4, refuted 2,
  conditional-on 1; level: M 165, H 44, G 38, O 1; bearing other than none at L: 1 (I4.236); do-not-assume: 44.
- Written at 17:24:36Z.

## N10 — end integrity (17:24:48Z) and sweep (17:24:57Z)
- (1) the six manifests `sha256sum -c --quiet` rc=0, no output; ns.manifest OK. (2) base HEAD 9f9f8257…,
  porcelain 0 lines, bytecode 0; no file under pt/base newer than the marker. (3) the ten protocol files at
  their expected prefixes, sidecars OK (six from pt/, four from SCRATCH). (4) 64 top-level names; newer than
  the marker: C5, D5, I1, I2, I3, I4, audit only.
- Sweep: my first sweep command was malformed (`find . -newer M ( … ) -prune -o -print` applies `-newer` only
  to the pruned branch, so it printed every non-excluded path, e.g. PROTOCOL-STAGE2.md of 07:12Z and the
  auditS2-replay files); a harness error of mine, no file changed. Corrected
  `find . ( -path ./I1 -o … -o -path './audit*-replay' ) -prune -o -newer I4/.start_marker -print`: no path
  outside the excluded directories; control (maxdepth 1 without the prune list) shows exactly the seven
  expected names. No anomaly; nothing quarantined; `evidence/` not created.
- Writes: only inside pt/I4/ (the scripts, their outputs, records.txt, INVENTORY-HEADER.md, INVENTORY.md,
  CENSUS.md, NOTES.md, .start_marker, and RESULT.md last). One temporary file (`.permod.tmp`, the per-module
  count rows extracted from census_kernel.out for CENSUS.md) was created and removed at 17:20Z.
- Written at 17:25:08Z.

## N11 — RESULT.md (from 17:25:40Z; this entry written at 17:26:48Z)
- RESULT.md written last, in three parts (§0–§1, §2–§3, §4–§5), each ≤ 250 lines. Its §4 lists the sha256 of
  every other file in pt/I4/ computed after this entry; NOTES.md is not modified after this entry. A final
  re-verification of the manifests, the base checkout and the protocol hashes, with a last sweep, is run after
  RESULT.md is written and reported in the thread's final report only (so that no hashed file changes).
- Addendum (17:27Z): a temporary hash list `.hashes.tmp` was created at 17:25Z for drafting §4 and removed before
  the final hash list was computed; it is not part of the evidence. The NOTES.md row of RESULT.md §4 is updated
  to this file's final hash.
- Addendum 2 (17:28Z), a procedural slip of mine: to verify the 73 hash rows of RESULT.md §4 I wrote a temporary
  list `hashcheck_i4.txt` (hash rows only) to the scratchpad root, one level above `pt/`, outside `pt/I4/`, and
  deleted it at once (17:27Z). No file under `pt/` was touched; no result depends on it. Later checks use a pipe.
