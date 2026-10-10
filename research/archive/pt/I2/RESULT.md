# I2 — RESULT (stage 6, Q-EX-FULL, step 1: established theorems and the physical layer)

Thread I2. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`. Governing text `pt/PROTOCOL-STAGE6.md`
(`b277b7c1…`). Read-only on the corpus; every file written is in `pt/I2/`. Started 16:51:44Z, records frozen
17:20:32Z, end checks 17:20:56Z. The inventory records; it does not decide, derive or upgrade.

## §0 Summary

**Counts (113 records, `tally.out`, run 3, replay identical).**

| by kind | n | by status | n | by level (primary) | n |
|---|---|---|---|---|---|
| theorem | 57 | proved [M] (manuscript proof, no kernel anchor at L) | 47 | H | 47 |
| manuscript-principle | 25 | proved [K] | 25 | M | 33 |
| lemma | 11 | assumed | 10 | G | 14 |
| obligation (ROADMAP or manuscript-open) | 9 | conditional-on | 8 | X | 19 |
| hypothesis | 6 | scope statement | 11 | O | 0 |
| hypothesis-structure / definition-as-hypothesis | 4 | open | 7 | P | 0 |
| theorem clause | 1 | empirically motivated | 2 | | |
| | | other (I2.70 status table; I2.84 = as I2.89; I2.101 mixed: `DC1` unrevised, `D5` not certified) | 3 | | |

Status classes are the first status keyword of each record (a coarse aid; the full status text in INVENTORY.md
governs: e.g. I2.2 is proved [M] for the causal-cone part only, I2.112 proved [M] for one observer class and
assumed for others). Of the 25 proved [K], nine (I2.29–I2.37) are manuscript statements resting wholly or partly on
kernel modules that belong to thread I4 (not verified by I2), and eight (I2.91, I2.94–I2.100) are ROADMAP round
results recorded as merged; I2 resolved kernel names to file:line only inside its own 32 modules, and built no Lean
(no toolchain; the certified status at L is taken as recorded). "proved [M]" and "scope statement"
are values this thread needed beyond the protocol's six; both are defined at the head of INVENTORY.md.

**Items with bearing other than `none at L`: none.** All 113 records have `bearing: none at L`.

**Bridges found: none.** No theorem at L in I2's scope transfers a level-H, level-M or level-G statement to the
pair cone (`W 3`, `K`). Mechanical support (`checks.py`, check B, countercontrol green): none of the 32 kernel
modules of I2's census names or imports `CompositeDimension`, `K2Guard`, `KInfFoundations`, `maxCone`, `cnot`,
`prodState`, `dualW`, `NativeGate`, `W 3` or `eball`. Further: no manuscript (papers/, book/) mentions the
field-neutral K programme, `W 3`, the pair cone, `CompositeDimension`, `K2Guard` or `NativeGate`; at L the pair
level exists only in the kernel and the ROADMAP.

**Bridges absent — and where the corpus itself says the transfer is not available (14 records).**
- I2.2 dynamical causal separation (Main.md:628): "does not alone establish statistical product structure after
  conditioning, local tomography, or one common tensor-product instrument category".
- I2.3 operational-extension boundary (Main.md:542): local tomography / composite completeness / operational
  purification are reconstruction routes "only after their hypotheses are actually established".
- I2.4 composites "on a different footing" (Main.md:212): kinematic locality does not prove local tomography.
- I2.18 gluing theorem (Main.md:562): a realization theorem, "not a uniqueness theorem".
- I2.21 separability threshold (Main.md:320): "supplies neither the observable algebra, nor preparations and
  interventions, nor tensor composition".
- I2.22 failure of (C1) (Main.md:286): entanglement-breaking "is a property of id ⊗ Φ and is not fixed by the
  action on single-system inputs".
- I2.45 canonical predictive quotient (Main.md:600): its translation into the operational composite language open.
- I2.62 dependency scope (Main.md:350): instrument algebra and coherent preparation supplied only by the five
  completion conditions, "none of which bare finite OI provides".
- I2.63 operational-reconstruction route (Main.md:352): tomographic locality is not what the finite characterization
  uses; "Bare finite OI therefore does not select quantum mechanics".
- I2.68 entanglement predictions need the operational bridge, "stated as open" (Main.md:632).
- I2.69 "A Layer-1 result does not by itself establish any Layer-4 claim" (Main.md:99).
- I2.85 observer access suffices for the trace-outs, "not enough for the Bell-violating deterministic completion"
  (Substratum.md:48).
- I2.108 locality of φ does not by itself give a local observer generator; locality inheritance holds only under
  **H-local-lift** (GR.md:328), a hypothesis with no ROADMAP row.
- I2.111 "Bare C1–C4 or graph locality do not enforce Tsirelson" (Substratum.md:430).
The remaining composite-level statements are recorded with `bridge: none at L` without a corpus denial: I2.12
(gluing clause (4) takes the quantum `I_a ⊗ I_b` as input — the direction is M → H), I2.19 (the visible–hidden
tensor product V ⊗ H, not token ⊗ token), I2.11 (the classical joint law of two observers), I2.20/I2.109 (nested
trace-outs), I2.79 (area law across a lattice bipartition), I2.107 (GR.md:326 Hilbert-space tensor product of
configuration cells, at level M).

**Do-not-assume items (11).** I2.29 operational-completion characterization, conditions (i)–(v); I2.30 the boxed
classification with (i)–(v); I2.31 OI⁺ (observational independence, reversible richness, observer recursion);
I2.32 primitive-source form (implementation locality's spectator clause; embedded observation); I2.33
substratum-source form (structural closure of an extension; the controllability resource); I2.34 layer-flow form
(`LayerFlowExecutable`); I2.35 typed form (inherits I2.33's resource); I2.3, I2.62, I2.63, I2.69 (statements that
name the five completion conditions or the operational-lifting and composition hypotheses). The kernel side of
I2.29–I2.35 is out of scope: I4. No record of I2 is (b), IE1, IE2, frame covariance or `Q3`/PSD/pure-state
reachability; I2.71 (rest-frame selection) concerns Lorentz frames of the substratum, not the native frame of the
pair carrier.

**Findings for the coordinator (record-only; no status changed).**
1. Kernel anchor weaker than the cited statement: Main.md:500 cites `S_imp_D` for the finite-horizon process
   dilation, whose statement requires a hidden prior independent of the visible initial state; the kernel class
   (D) allows an arbitrary initial law, and its docstring says the stronger form is "NOT what this theorem's class
   `(D)` asks for" (Equivalence.lean:150–155). I2.40.
2. Dangling cross-reference: Main.md:562 refers to "The Kochen–Specker inheritance (§3.2)"; Main §3.2 contains no
   Kochen–Specker statement; the inheritance statement is in the book (FULL.md:1042, ch03:168). I2.14.
3. Named hypotheses with no ROADMAP row: H-local-lift (GR.md:328, I2.108); H-observer-bundle and H-Y-vertex
   (SM.md:791, I2.113). H-blind is named in the ROADMAP's H-link section (ROADMAP.md:1122) but not as a row (I2.112).
4. Book mirror gaps: the book never restates the canonical predictive quotient (I2.45) or the process-dilation
   theorem (I2.40) by name, and never names local tomography (I2.2, I2.3, I2.63).
5. Composite-related kernel modules not cited by any manuscript or by I2's ROADMAP rows (outside I2's
   citation-based census): `CompositeInterface` (COMP-1, local tomography a premise field — I3's K2 scope),
   `SpectatorBridge` (I4), `MonoidalCompletion`, `CompositionalIndependence`, `FactorExchange`, `PartialTranspose`,
   `Purification`, `FactorUniqueness` (operational-completion programme, I4's scope by content).

## §1 The inventory by section (by reference to INVENTORY.md)

- A. Composition, locality, subsystems, operations: I2.1–I2.38 (causal cone, causal separation, the
  operational-extension boundary, Bell ceiling and branch, no-signaling, gluing and its clauses, Kochen–Specker,
  continuum density, classical-dimension obstruction, visible–hidden tensor product, nested partitions,
  separability threshold, passive observation, coherent extension, relating evolution, coherent-completion
  classification, reconstruction theorems, Bekir–Golomb premise, operational-completion characterization, OI⁺,
  primitive-source, substratum-source, layer-flow and typed forms, Level III completion, continuous time,
  classification premises).
- B. Equivalence, dilation, hidden memory, recurrence: I2.39–I2.74 (S ⟺ D ⟺ Q_fb, process dilation,
  characterization theorem, (T), fixed-Ĥ form, unavoidable hidden predictive memory, canonical predictive
  quotient, variational question, P-indivisibility and recurrence, readback lemmas, ancilla dilation, imported
  correspondence, phase-locking, Stinespring route, CP-indivisibility, intervention dilation, obstructions,
  consolidation, scope remarks, claim structure, status ledger, rest-frame lemma, observer selection under (EM),
  falsifiability, dimensional obstruction).
- C. Physical layer (SM, Substratum, GR physical statements): I2.75–I2.89, I2.105–I2.113.
- D. ROADMAP obligations (Track B P0 and acts 9–17, H-Bell, H-∞, P3 Level III): I2.90–I2.104.
- E. Kernel-census entries: mapped in CENSUS.md §(a).

## §2 Ledger of sources read (all under `pt/`, read-only)

- Governing texts, in full: `PROTOCOL-STAGE6.md`, `PROTOCOL-STAGE5.md`, `PROTOCOL-STAGE5-AMENDMENT-1.md`,
  `PROTOCOL-STAGE4.md`, `PROTOCOL-STAGE3.md`, `PROTOCOL.md`, `INTEGRATION-NOTE-STAGE4.md`,
  `INTEGRATION-NOTE-STAGE3.md`; `base/AGENTS.md` (byte-identical to the repository copy in context, sha256
  `959c4333…`). Protocol amendments 1–2, STAGE2 and STAGE2-DS: hash-checked only.
- `base/papers/Main.md`: lines 1–762 in full (reference list 772–886 screened only).
- `base/papers/GR.md`: §3.3 (164–296) in full; 322–334; 689–752 in full; Appendix A theorem lines (725–841);
  residual-screen lines (20, 60–76, 118, 306, 340–362, 376–452, 530, 551, 585–601, 649, 755, 763, 813) at line level.
- `base/papers/SM.md`: lines 12, 14, 48, 60, 70, 84, 100, 104, 108, 118, 152, 220, 226, 238, 262, 304–339 and
  655–823 (keyword skim), 328, 537–551, 683, 791, 1356–1368, 1586–1630; residual-screen lines at line level.
- `base/papers/Substratum.md`: 14–56 (selected), 78, 106–124, 142–172, 186–194, 238–242, 264–266, 416, 430;
  residual-screen lines at line level.
- `base/verification/ROADMAP.md`: queue rows 59–75 (row 63 by lead and bullet structure), 77–128 in full, the
  bullet and bold lines of 129–664, 630–663 in full, 936–970, 1148–1157; mentions at 909, 1006, 1122.
- Kernel (`base/verification/lean-mathlib/OIBridge/`): the full declaration index of 214 modules (by the census
  script); statements and docstrings read in `Equivalence.lean` (140–225, 405–470), `HiddenMemory.lean` (1–200);
  module headers of `TrackBQfbBridge`, `WeylLift`, `CoherentContinuumSource`, `RegionLimit`, `PartialTranspose`,
  `FactorExchange`, `CompositeInterface`, `CompositionalIndependence`, `MonoidalCompletion`, `SpectatorBridge`,
  `Purification`, `FactorUniqueness`; declaration lines of every cited name in the 32 I2 modules.
- Book: `The-Incompleteness-of-Observation-FULL.md:1042` and its mirror `ch03-structural-realism.md:168` in full;
  the 19 mirror phrases over `book/*.md` by the census script.
- Not read (per protocol): `pt/I1/`, `pt/I3/`, `pt/I4/`, `pt/D5/`, `pt/C5/` (names only, through the top-level
  listing), `pt/audit/stage3-inputs/OWNER-*` (hashed through `ns.manifest.sha256` only — it lists `ns/NS-INPUT.md`),
  `pt/audit/stage4-inputs/OWNER-*`, `pt/audit/stage5-inputs/`, `pt/audit/stage6-inputs/`, `pt/audit/reviews/`,
  `pt/audit/aborted-launches/`. Stage-1 to stage-5 thread records (`pt/A/`–`pt/Z/`) were not needed and not read.

## §3 What is not claimed

- No status upgrade and no derivation. Every status is the one the corpus record fixes (the manuscript's own
  statement or status ledger, the ROADMAP row, the kernel docstring); "proved [M]" records the manuscript's claim of
  proof and nothing more. No verdict on (b_min), on `K = Q3`, or on any countermodel is given or implied.
- "bridge: none at L" is established mechanically only for I2's 32 kernel modules (check B) and by search for the
  manuscripts (no pair-level vocabulary in papers/ or book/). Kernel bridges in modules outside I2's census (I3's K
  programme, I4's completion modules, the uncited composite modules of §0 finding 5) are not examined here.
- The kernel side of I2.29–I2.37 (I4's modules) and the act results of I2.91–I2.100 were not verified; the ROADMAP
  round records were read at their summary lines, not at their result notes.
- Coverage limits, stated: the manuscript census is sentence-level only inside the 26 listed sections; SM §4.4 and
  §6 were read for observer and composite constraints (yielding I2.112, I2.113) but not censused sentence by
  sentence; GR §2, §4–§5, §7–§8 and Substratum §4–§7 were covered only by the residual screen (classified by block
  in CENSUS.md §(e)); the book is covered by mirror phrases, not by sentences. Sentences in the sections that state
  an item without any keyword of the protocol's list are caught only by reading (CENSUS.md §(b) lists the records
  reached that way).
- The partition between I1 and I2 inside Main §1–§3 (C1–C4 and their necessity theorems to I1; the equivalence,
  hidden-memory and recurrence theorems to I2) is this thread's reading of the protocol; the coordinator may merge
  differently.
- No Lean was built; no claim is made about the kernel beyond the declaration text at L.

## §4 Evidence log

**Scripts and runs** (all `python3 -I -B <script>` from `pt/I2/`; stdout to `<name>.out`, stderr plus an appended
`exit N` line to `<name>.err`; every final run replayed to `<name>.replay.*`, byte-identical on stdout and stderr;
earlier runs kept as `<name>.runN.*`):

| script | final run | kept runs | result |
|---|---|---|---|
| `kernel_census.py` | run 3 | run 1 (failed: labels resolved as Lean names; its script kept as `kernel_census.run1.py`), run 2 (superseded by the section extension; identical output) | 32 I2 modules, 72 entries, 38 out-of-scope modules; no `axiom`/`opaque` |
| `manuscript_census.py` | run 6 | run 1 (listing pass, no map), runs 2–5 (superseded: book part added, residual screen added, sections extended, map extended) | 593 keyword sentences on 332 lines, 0 unmapped; 83 ROADMAP entries, 0 unmapped; 19 book phrases; residual screen |
| `checks.py` | run 7 | run 1 (failed: three off-by-one line numbers, corrected in INVENTORY), runs 2–6 (superseded as records were added); one dry run at 17:20:05Z not kept (NOTES N7) | Q 251/251 fragments verbatim; X 113 records, 0 dangling; B 0 pair-cone hits, countercontrol 247 hits; VERDICT Q PASS, X PASS, B PASS |
| `tally.py` | run 3 | runs 1–2 (superseded: 111 and 112 records) | the counts of §0 |

Script versions: `kernel_census.py` and `manuscript_census.py` were amended in place between runs; each
amendment is written into the script's header before the run it governs (decision rules unchanged). The run-1
version of `kernel_census.py` is kept as `kernel_census.run1.py`; intermediate versions are not kept separately.

**sha256 of every file written in `pt/I2/` except RESULT.md** (taken 17:21:09Z, re-verified unchanged before
this section was written):

```
2b94ace4441623bc80e766b8c7c76f9627d398955f86e3e2d94bcb7555c613c6  .end_check
de46a8c22216a573ea6687934e2d18517499e37851749c1847a008f1e8ff20db  .start_marker
71d1d10c68e1e8316d4591b6c713cf60883dd9ac98b7b4e92e6df253b179f1db  CENSUS.md
d923e63013c7fdf0fc2be61f6ce5566816ef1c339e7f070aee966ada6952325b  INVENTORY.md
3a68c360fe243a8e17def27af356637e0c0c7bfcda7007e64d01e9b45dd74251  NOTES.md
f50ac3f1ed406069fd81d55ee6705ad66c79069725cdac48828900db031f60be  census_map.tsv
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.err
6452c85101e886885c9f984ce501baf37ba62f5b0a8bc986da6d3d754e620ecf  checks.out
d2cddabb97398c3ab3c1d794e948c2737aa53145c056e52e92aeb34fe08c9cc6  checks.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.replay.err
6452c85101e886885c9f984ce501baf37ba62f5b0a8bc986da6d3d754e620ecf  checks.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.run1.err
a633c2b0b7503e0b410100bb7430aa406a1fba100fe433476507415bac1fb36c  checks.run1.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.run2.err
cf226af9ccd787aaf252b7e1f5b315cea408565606672cc5f9239419f0b4930c  checks.run2.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.run3.err
6a925251baff7eb05064808634537007ee31c085fa1184a4f99f86aec5843ea0  checks.run3.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.run3.replay.err
6a925251baff7eb05064808634537007ee31c085fa1184a4f99f86aec5843ea0  checks.run3.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.run4.err
226cb324749e4ce91e00a5add99fa329085afbbc1ee8a13c4c108786d93e2516  checks.run4.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.run4.replay.err
226cb324749e4ce91e00a5add99fa329085afbbc1ee8a13c4c108786d93e2516  checks.run4.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.run5.err
226cb324749e4ce91e00a5add99fa329085afbbc1ee8a13c4c108786d93e2516  checks.run5.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.run5.replay.err
226cb324749e4ce91e00a5add99fa329085afbbc1ee8a13c4c108786d93e2516  checks.run5.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.run6.err
6452c85101e886885c9f984ce501baf37ba62f5b0a8bc986da6d3d754e620ecf  checks.run6.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  checks.run6.replay.err
6452c85101e886885c9f984ce501baf37ba62f5b0a8bc986da6d3d754e620ecf  checks.run6.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  kernel_census.err
b127fec5eb44c8700059156c7a1abc9f4d9eff2f6d4d58b4c090f3c79fb2b094  kernel_census.out
40ea357160c341c591aeeba4af7d0a115d758bbab92472f5a927aa1a6ad4ef11  kernel_census.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  kernel_census.replay.err
b127fec5eb44c8700059156c7a1abc9f4d9eff2f6d4d58b4c090f3c79fb2b094  kernel_census.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  kernel_census.run1.err
9821c8c6ca6d726c09940d0f395bf062076e3f0820d137bf626e154c464db38f  kernel_census.run1.out
f7de0c4812a1a38887e42d8c7107e02bfb9bd236eb1a7cde96def0be274f5aed  kernel_census.run1.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  kernel_census.run2.err
b127fec5eb44c8700059156c7a1abc9f4d9eff2f6d4d58b4c090f3c79fb2b094  kernel_census.run2.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  kernel_census.run2.replay.err
b127fec5eb44c8700059156c7a1abc9f4d9eff2f6d4d58b4c090f3c79fb2b094  kernel_census.run2.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  manuscript_census.err
d0659af4d84638ed5d74be4e9adb5f2640222010f899ecf020d8f9d7abb3f8a9  manuscript_census.out
bc669fc5e639ae59c5e4d5444d6219520df3de7fa5866a6b33f10f5d03e8a7f0  manuscript_census.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  manuscript_census.replay.err
d0659af4d84638ed5d74be4e9adb5f2640222010f899ecf020d8f9d7abb3f8a9  manuscript_census.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  manuscript_census.run1.err
2209e09bd9a27ab9f89bd94025288a4740332ef1d0f1b6cc9c969917da2538bf  manuscript_census.run1.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  manuscript_census.run2.err
d0d385f504eaac1adb58d4fc77131fd7e98d21aac96271c2811024cf45fe26bd  manuscript_census.run2.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  manuscript_census.run2.replay.err
d0d385f504eaac1adb58d4fc77131fd7e98d21aac96271c2811024cf45fe26bd  manuscript_census.run2.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  manuscript_census.run3.err
b25f7cd0ce769c644516752d2309c48bfc35bd53deccec85c693741ba341697c  manuscript_census.run3.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  manuscript_census.run3.replay.err
b25f7cd0ce769c644516752d2309c48bfc35bd53deccec85c693741ba341697c  manuscript_census.run3.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  manuscript_census.run4.err
c8a57062b9c48094554698ce6021115893056e25da68940e347fdd3c82e02a10  manuscript_census.run4.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  manuscript_census.run5.err
0789fd94966dc3e84b4e6e9faed4fd57177b24056414588f78eabe27fd816383  manuscript_census.run5.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  manuscript_census.run5.replay.err
0789fd94966dc3e84b4e6e9faed4fd57177b24056414588f78eabe27fd816383  manuscript_census.run5.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  tally.err
5b723a6247d3e5e17a4be768c530b89cd81cdb26cf7942580cba7fe46f7c1286  tally.out
8d59353eff37a9148f2c7738de70bb1d86dee19f8de3b026543b160d59921fe7  tally.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  tally.replay.err
5b723a6247d3e5e17a4be768c530b89cd81cdb26cf7942580cba7fe46f7c1286  tally.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  tally.run1.err
0cca0907503dd587bcce3d6182fff89f4af53f30830d9078925b06015b1afba9  tally.run1.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  tally.run1.replay.err
0cca0907503dd587bcce3d6182fff89f4af53f30830d9078925b06015b1afba9  tally.run1.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  tally.run2.err
958e6072125a4ff0d157bec236a9ca951d131e005050337bc3533baaa91c416e  tally.run2.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  tally.run2.replay.err
958e6072125a4ff0d157bec236a9ca951d131e005050337bc3533baaa91c416e  tally.run2.replay.out
```

## §5 Integrity

- **Start (16:51:44Z, `.start_marker`).** `pt/I2/` absent at 16:51:22Z, created with `mkdir` and the marker written
  first. The six manifests (`inputs`, `stage1`, `inputs2`, `inputs3`, `stage2`, `inputs4`) verified with
  `sha256sum -c --quiet`, exit 0 each; `audit/stage3-inputs/ns.manifest.sha256` from its own directory: OK, exit 0;
  base HEAD `9f9f8257a980a1819fbbc1dc0019917cf8678626`, porcelain empty, no `__pycache__`/`.pyc`; the ten protocol
  files match their prefixes (`239dc123`, `b41aa0e7`, `2a2f78f3`, `38603692`, `086a4cb8`, `1a649168`, `d3da2811`,
  `9e01f098`, `1f639115`, `b277b7c1`) and each sidecar verifies (STAGE4, STAGE5, STAGE5-AMENDMENT-1, STAGE6 from
  SCRATCH; the others from `pt/`); top-level listing recorded.
- **End (17:20:56Z, `.end_check`).** Identical results for all four checks. Top-level names new since the start:
  `I1`, `I3`, `I4` (sibling threads). Top-level entries modified since the start: `C5`, `D5`, `I1`, `I2`, `I3`, `I4`,
  `audit` — all in the excluded set.
- **Sweep.** `find pt/ -newer I2/.start_marker` with `I1`, `I2`, `I3`, `I4`, `D5`, `C5`, `audit`, `audit*-replay`
  pruned (their contents not listed): the only path reported is the directory `pt` itself, whose mtime changed when
  the sibling directories were created. No file outside the excluded areas is newer than the marker. **No anomaly;
  nothing quarantined; no `evidence/` directory was needed.**
- **Own directory.** `pt/I2/` holds only files written by this thread (78 files after this one: the 77 hashed in §4
  plus RESULT.md). A temporary hash list `.hashes.tmp` (written 17:21:09Z, this thread's own) was removed after its
  content was copied into §4.
- **Procedural notes.** Script edits between runs were made with inline Python editing helpers reading stdin
  (not evidence runs); one `checks.py` dry run (17:20:05Z) was written to a temporary file and not kept (NOTES N7).
  No write outside `pt/I2/`; no git write (only `rev-parse` and `status --porcelain` with
  `GIT_OPTIONAL_LOCKS=0`); no branch, PR, CI, network or URL fetch, publication or sub-agent.
