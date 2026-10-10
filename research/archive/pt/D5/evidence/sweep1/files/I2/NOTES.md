# I2 — running notes (stage 6, Q-EX-FULL, step 1: inventory of established theorems and the physical layer)

Thread I2. Governing text `pt/PROTOCOL-STAGE6.md` (sha256 `b277b7c1…`). Read-only on the corpus; writes only in
`pt/I2/`. Clock times are UTC from `date -u`.

## N0 — start (16:51Z)

- 16:51:22Z `pt/I2/` absent; created with `mkdir` (no `-p`) at 16:51:44Z; `.start_marker` written first.
- Start checks (all green, recorded in `.start_marker`): the six manifests `sha256sum -c --quiet` exit 0;
  `audit/stage3-inputs/ns.manifest.sha256` from its own directory: `ns/NS-INPUT.md: OK`, exit 0; base HEAD
  `9f9f8257a980a1819fbbc1dc0019917cf8678626`, porcelain empty, no `__pycache__`/`.pyc`; the ten protocol files match
  their prefixes and each sidecar verifies (STAGE4/STAGE5/STAGE5-AMENDMENT-1/STAGE6 from SCRATCH, the others from
  `pt/`); the `pt/` top-level listing with mtimes. At the listing, `pt/I1/`, `pt/I3/`, `pt/I4/` did not yet exist;
  `pt/D5/`, `pt/C5/` existed (16:45Z).

## N1 — governing texts read (16:51–16:53Z)

Read in full: `PROTOCOL-STAGE6.md`, `PROTOCOL-STAGE5.md`, `PROTOCOL-STAGE5-AMENDMENT-1.md`, `PROTOCOL-STAGE4.md`,
`PROTOCOL-STAGE3.md`, `PROTOCOL.md`, `INTEGRATION-NOTE-STAGE4.md`, `INTEGRATION-NOTE-STAGE3.md`. `pt/base/AGENTS.md`
(824 lines, sha256 `959c4333…`) is byte-identical to the repository AGENTS.md loaded in this session's context; its
section list was checked against that copy.

Points fixed for this thread from the governing text:
- Scope I2 (stage-6 partition): finite-horizon equivalence `S ⟺ D ⟺ Q_fb`, hidden-memory results, recurrence,
  canonical predictive quotient, Stinespring/intervention-dilation, Bell and no-signalling, Level III quasilocal
  completion (manuscript statement), and every Main/SM/GR/Substratum constraint bearing on composition, locality or
  operations (dynamical causal separation, tensor-product structure, the operational-extension boundary,
  implementation locality and the substratum-source and layer-flow forms as manuscript statements; kernel side: I4).
- Record schema: id, name, kind, statement (exact), provenance (file:line at L), status (never upgraded), level
  (H/O/P/M/G/X), depends_on, yields, bridge (to the pair cone, or `none at L`), bearing, flag.
- Do-not-assume flags: OI⁺ completion conditions (i)–(v), observational independence, reversible richness, observer
  recursion, implementation locality's spectator clause, structural closure of an extension, `LayerFlowExecutable`;
  (b), IE1, IE2, frame covariance, `Q3`/PSD/pure-state reachability.
- Level distinction mandatory: an H-level item constrains the pair cone only through a bridge proved at L.
- The pair-cone setting (stages 3–5): `K ⊆ W 3` with H1 (products), H2 (`cnot`-invariance; level (ii) `G16`),
  H3 (`K = dualW K`); exotic cones `K(E0)`, `K(Z_F)`, `K({F, cnot F})`, `K(e_c)`; (b_min) any of (b_S4), (b_n),
  (b_R1), (b_DJ).

## N2 — corpus survey (16:53–17:02Z)

- Read in full: `papers/Main.md` 1–762 (all sections except the reference list); `papers/GR.md` §3.3 (164–296),
  §8.7 and Appendix A.1–A.4 (689–752); `papers/Substratum.md` §3.3 (142–173) and selected lines (14–48, 78,
  106–124, 186–195); `papers/SM.md` selected lines (14, 48, 60, 70, 84, 118, 537–551, 1356–1368, 1586–1630);
  ROADMAP queue rows 63, 67, 70, 75, P0 section 77–128 and the bullet/bold lines of 129–664, H-∞ 936–952,
  H-Bell 953–970, Level III 1148–1157; kernel module headers and statements of `Equivalence.lean`,
  `HiddenMemory.lean`, `TrackBQfbBridge.lean`, `WeylLift.lean`, `CoherentContinuumSource.lean`,
  `RegionLimit.lean`; the book's Kochen–Specker paragraph (`FULL.md:1042`, mirror `ch03-structural-realism.md:168`).
- Sections fixed for I2's censuses (identical lists in both scripts): Main 14–22, 82, 95–99, 101–196, 200–656,
  660–678, 696–720, 722–740, 744–756; GR 164–296, 709–752; SM 10–16, 40–95, 96–165, 216–279, 535–566,
  1354–1369, 1576–1635; Substratum 12–40, 42–65, 70–173, 186–195; ROADMAP 63, 67, 70, 75, 77–664, 936–970,
  1148–1157. Within Main §1–§3 the axioms, Definition, Lemmas 1–3, C1–C4 and their necessity theorems are
  I1's (mapped out of scope: I1); GR 212–276 and Main 564–568 kernel side is I4's.

## N3 — kernel census (16:56–16:58Z)

- `kernel_census.py` run 1 (kept as `kernel_census.run1.*`): harness error — round labels and single letters
  (`A`, `S`, `N`, `D3`, `G₁`, `a4`) resolved to same-named Lean declarations (spurious modules RankGapTheory as
  I2, Reciprocity, KInfFoundations, LinkDecomposition). Pre-run edit for run 2 recorded in the script header
  (eligibility rule for identifiers; matched identifiers printed per module). Run 2: 32 I2 modules, 38
  out-of-scope modules, 72 census entries (all literal-pattern matches), no `axiom` or `opaque` in the I2 modules
  (and no column-0 `axiom` anywhere in OIBridge). Four `class` entries are doc-comment lines beginning with the
  word "class" (not declarations). Replay byte-identical (stdout and stderr).
- Name collisions noted: `permMatrix_mem_unitaryGroup` is declared in both `EquivalenceChain.lean:178` (the cited
  one) and `DilationChoice.lean:213`; `corner_form` resolves to `CompositeDimension` (I3) besides
  `JordanClassification` (I4).
- Finding (provenance): Main.md:500 cites `S_imp_D` as the kernel anchor of the finite-horizon process-dilation
  theorem, whose statement requires "an initial hidden prior μ_H independent of the visible initial state";
  the kernel docstring of `RevReal` (Equivalence.lean:150–155) says that stronger form "is the manuscript's
  separate finite-horizon process-dilation theorem ... and it is NOT what this theorem's class `(D)` asks for".
  The kernel anchor therefore covers the weaker class (D) only. Recorded at I2.40; no status changed.
- Finding (dangling cross-reference): Main.md:562 refers to "The Kochen–Specker inheritance (§3.2)"; no
  Kochen–Specker statement exists in Main §3.2 at L (grep: Main.md:550 and :562 only). The inheritance statement
  is in the book (FULL.md:1042, ch03:168). Recorded at I2.14.
- Ad-hoc check (later scripted): none of the 32 I2 modules mentions or imports CompositeDimension, K2Guard,
  KInfFoundations, `maxCone`, `cnot`, `prodState`, `dualW`, `NativeGate`, `W 3`, `eball`.

## N4 — manuscript census listing pass (16:59Z)

- `manuscript_census.py` run 1 with no map file (listing pass by design, kept as `manuscript_census.run1.*`):
  567 keyword sentences on 313 lines; 83 ROADMAP entries.
