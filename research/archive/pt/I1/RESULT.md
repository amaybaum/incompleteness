# I1 RESULT — premise inventory, foundations (stage 6, Q-EX-FULL, step 1; L = `9f9f8257…`)

Thread I1. Governing text `pt/PROTOCOL-STAGE6.md` (`b277b7c1…`) with the protocols it names.
Read-only on the corpus; no derivation, no verdict on (b); no status upgraded. Records in
`INVENTORY.md`, censuses in `CENSUS.md`, running record in `NOTES.md`.

## §0 Answer

**Counts — 85 records, `I1.1`–`I1.85`.**
- By kind: axiom 8 · condition 5 · hypothesis 4 · hypothesis-structure (`def … : Prop`) 17 ·
  definition-as-hypothesis 3 · theorem 23 (kernel 20, manuscript 3) · lemma (manuscript) 6 ·
  manuscript-principle 16 · obligation (ROADMAP) 3 · lemma-folded: none standalone (folded lemmas
  are named inside the record of the theorem they serve).
- By status (from the record that fixes it): proved [K] 28 · definition [K] 8 · proved
  [manuscript, not K] 9 · conditional-on 7 (I1.17 layer 4 on lifting/composition hypotheses; I1.30,
  I1.31 on the mixing hypothesis; I1.35 on M1-T; I1.61, I1.68 ROADMAP CONDITIONAL; I1.62 on the
  named carrier hypothesis) · assumed 25 · empirically motivated 2 (I1.10, I1.64) · open (ROADMAP)
  3 (I1.73, I1.74, I1.76) · condition with a split status 3 (I1.20, I1.23, I1.24) · refuted 0 (the
  reading `A6-inv` inside I1.61 is refuted on the frozen carriers, ROADMAP.md:65).
- By level: H 52 · H/X 6 · H→X 1 · H→M 8 · M 18 · O 0 · P 0 · G 0 · X 0.

**Items with `bearing` other than `none at L`.** None in substance. One record carries the formal
value "constrains the composite only through <bridge>" with the bridge `none at L`: I1.17
(Main.md:82: the full operational extension "requires the additional operational-lifting and
composition hypotheses stated in §3.4"). No I1 item constrains `K`, (b_min) or the single-token
structure at L.

**Bridges found — all H→M; none reaches level O or P.**
I1.41 `oi_core_underdetermines_completion` (one C1–C4 core, three coherent completions: a
non-selection result) · I1.43 `RealizesSealedOICore` (the core transported into level four of a
`FiniteOperationalTheory (Fin 2)`) · I1.44 `realizesSealedOICore_of_control` (composite unitary
control ⇒ the core is realized) · I1.49 `DerivedOI` (the substratum-class sourcing theorems
collected) · I1.52 `substratumTheory_realizesSealedOICore` · I1.56 `ConfigurationLevel` bound
(configuration-level sourcing ⇒ not QM on the two-state carrier) · I1.59 `obsTheory` (substratum ⟶
observer theory; `obs_not_qm`) · I1.60 `permTheory_realizesSealedOICore`, `permTheory_twoState`.

**Bridges absent.**
- Mechanical, at L (scripts with countercontrols, replayed): no module imports both an I1 module
  and `CompositeDimension`/`K2Guard`, nor an I1 module and the K∞ modules (`bridge_check.out`: two
  VERDICT NO-MODULE); no module imports both `OperationalAssembly` (the M-level carrier) and a
  pair-cone module (`bridge_check2.out`: NO-MODULE); the pair-cone modules' import closure does
  contain the passive-observation layer (`ObservabilityQuotient`, `PassiveQuotient`), but none of
  the 21 K-programme/pair modules mentions that layer's objects in a signature or anywhere in its
  source (`bridge_check3.out`, `bridge_check4.out`: NONE-FOUND). So H→P: none at L; H→O: none at L;
  and no module at L is placed to state an M→P bridge for the I1 objects.
- Stated by the corpus: ManuscriptAxioms.lean:18–21, :24–26 (nothing identifies the core with a
  manuscript substratum; the A1/A2 images "are images, not the axioms") — I1.55;
  ManuscriptAxioms.lean:48–50 ("The kernel has no map from a substratum to an implementation
  class") — I1.56; RouteB.lean:49–52 (stochastic-level results, C3 necessity included, "constrain
  no candidate") — I1.49; OIRealization.lean:50–52 with `finiteOI_not_implies_inert` and
  `finiteOI_not_implies_closure` (bare finite OI implies neither inert-spectator compositionality
  nor iterated ancilla closure) — I1.46, and I1.80–I1.83 (each completion condition, inert
  spectators included, independent of OI realization); Main.md:99 ("A Layer-1 result does not by
  itself establish any Layer-4 claim") — I1.16; Main.md:82, :22 (composites need additional
  lifting and composition hypotheses) — I1.17; Main.md:286 ("(C1) constrains the diagonal of
  $\Phi$, whereas entanglement-breaking is a property of $\mathrm{id} \otimes \Phi$") — I1.34;
  ROADMAP.md:44–49 (operational completion principles remain explicit additional conditions) —
  I1.78; ROADMAP.md:69 (the observation-map leg is not supplied on `Substratum.Conf`) — I1.76;
  README.md:636–640 (`OICore` an existential condition about a four-state gadget; "No ontological
  necessity") — I1.47; PhysicalC4Discharge.lean:22 (nothing says C4 holds or fails at either
  physical cut) — I1.71.

**Do-not-assume items.** None of the 85 records is itself a flagged item. Flagged notions occur
only as named dependencies inside I1 theorems, never as premises of a derivation; their records
belong to thread I4: `InertSpectatorCompositionality` (observational independence restated,
CompletedOI.lean:24–27) in I1.45, I1.46, I1.80–I1.83; `HasCompositeUnitaryControl` (full
reversible control, the operational condition reversible richness compresses) in I1.44, I1.45,
I1.80–I1.83; `IteratedAncillaClosure` (iterated composition) in I1.45, I1.46, I1.80–I1.83;
`ObserverRecursion` in I1.83. (b), IE1, IE2, frame covariance and `Q3`/PSD/pure-state
reachability do not occur in I1's records.

**Status variances recorded, not adjudicated.** Bijectivity a lemma (Methodology.md:251) versus a
representation/reconstruction choice (Main.md:38, :62) — I1.10. C2 defined in its slow form
(ch01:55, Explainer.md:67) versus persistence (Main.md:76) — I1.21/I1.22. "The framework's four
conditions are therefore *logically* independent" (ch01:71) versus "only (C4) is logically
independent" (Main.md:602) — I1.25/I1.26. "a deterministic dynamics" (ch01:26) versus "a dynamics"
(Main.md:44) — I1.6. The general C1, C2 and C4 have no kernel predicate at L (only the sealed-core
instances `CoreC1C4`, the candidate forms `C4e`/`C4r`, the realization clauses); C3's necessity is
a general kernel theorem (I1.32).

**Censuses.** (a) Kernel: 41 census entries in twelve modules plus `OICore`, all mapped; no `axiom`
or `opaque` in any I1 module; 94 core-token declarations (82 → I1 records, 12 → thread I4); 10
zero-import heads out of scope (thread I2). (b) Manuscript: 946 sentences, 0 unmapped (565 → I1
records, 381 → thread I2); all 231 counted book sentences mirrored in FULL.md. (c) Roadmap: 96
items, 0 unmapped (10 → I1 records, 86 out of scope with the thread named).

**Unfinished.** Three modules touching the observer structure were not censused whole
(`StochasticInterface`, `ObservabilityQuotient`, `PassiveQuotient`; their cited or capstone
theorems are recorded at I1.76, I1.84, I1.85); their other declarations are unmapped. The
manuscript mapping is rule-based (rules in `census_ms.py`'s header) with 18 manual mappings, and
maps every use-site of a condition to that condition's record. Quotation exactness is checked
mechanically for 164 fragments (`quote_check.out`, ALL-EXACT); Lean code quoted in backticks was
copied from tool output of the source and is outside that check.

## §1 The inventory by section (records in `INVENTORY.md`)

| section | records | content |
|---|---|---|
| A. Observation base (manuscript; H) | I1.1–I1.18 | Axioms 1–2, the two-axiom base and the no-go, the perspectival reading, the C1–C4 selection condition, the Definition, the composition law, Lemmas 1–3 split into their components (finite resolution, partition, bijective representative, total finiteness, measure selection, μ_H), the fallback postulate, partition-relativity, the four layers, the layered theorem statement, Methodology's rung analysis |
| B. Hidden-sector conditions (manuscript; H) | I1.19–I1.37 | the diagnostics remark; (C1), (C2-structural), (C2-slow), (C3), (C4) with every variant (book, Explainer, Substratum); which condition is primitive; the book's independence variant; readback ⇒ indivisibility in the cycle; fast bath; accessible backflow; C2 necessity and physical memory (conditional on mixing); C3 necessity [K]; existential/universal readings; (C1) and `id ⊗ Φ`; Substratum Stage 1; M1-T; the Explainer's access reading |
| C. The sealed core and its realization (kernel) | I1.38–I1.48 | the core; `CoreC1C4`; observer-minimality; the independence census; `SealedCoreIsFiniteOI`; `RealizesSealedOICore`; control realizes the core; the capstone; bare finite OI implies neither compositional principle; `OICore`; the forward-redundancy entry |
| D. Route B (kernel) | I1.49–I1.54 | `DerivedOI`, `DerivedOICore`, the falsifier and target, the substratum theory realizes the core, the closure does not entail phase-free richness, QM satisfies the closure |
| E. Substratum axioms A1–A6 | I1.55–I1.69 | realized-core images (bridge absent); the configuration-level bound; the kernel `Substratum` and A1–A5; the wave rule; the observer theory (H→M); `SourcedOI`; A6 readings and instantiation; the manuscript A1–A6; joint sufficiency |
| F. C4 in the kernel | I1.70–I1.74 | `C4e`/`C4r` and the no-go chain; `RoutedReadback`; `RoutedReadbackAtStorage` (incomparable); `LatticeCutReadback`; the ROADMAP P1 Physical C4 row (OPEN) |
| G. Observer structure | I1.75–I1.78, I1.84–I1.85 | the internal observer; the stochastic observer interface (OPEN); declared inputs; the interpretation boundary; the finite-horizon observability quotient; bare OI does not make the ontic carrier observable |
| H. Core-carrying realization theorems (M) | I1.79–I1.83 | passive incompleteness vs `OICore`; control independent; five-way minimality; the substantive census; level-one seam and inert spectators independent of OI realization |
| I. Out-of-scope names | — | definitions used in I1's statements, owned by I4 (completion layer) or I2 (hidden memory, recurrence) |

## §2 Ledger of sources read (all read-only)

- Protocols and records: `pt/PROTOCOL-STAGE6.md`, `PROTOCOL-STAGE5.md`, `PROTOCOL-STAGE5-AMENDMENT-1.md`,
  `PROTOCOL-STAGE4.md`, `PROTOCOL-STAGE3.md`, `PROTOCOL.md`, `INTEGRATION-NOTE-STAGE4.md`,
  `INTEGRATION-NOTE-STAGE3.md` — in full. `pt/base/AGENTS.md` — byte-identical to the AGENTS.md in
  this session's context (sha256 `959c4333…`), read there in full. Stage-1 records `pt/A/`–`pt/D/`:
  not needed, not read. Not read, as required: `pt/I2/`, `pt/I3/`, `pt/I4/`, `pt/D5/`, `pt/C5/`,
  `pt/audit/stage3-inputs/OWNER-*`, `pt/audit/stage4-inputs/OWNER-*`, `pt/audit/stage5-inputs/`,
  `pt/audit/stage6-inputs/`, `pt/audit/reviews/`, `pt/audit/aborted-launches/` (the
  `ns.manifest.sha256` check hashes `ns/NS-INPUT.md` without displaying it).
- Kernel (`verification/lean-mathlib/OIBridge/`): OIRealization.lean (full); IndependenceCensus.lean
  1–300, 540–560, 790–840; ManuscriptAxioms.lean (full); RouteB.lean 1–60, 110–180, 223–270,
  310–400; CompletedOI.lean 1–40, 86–120, 545–565; SubstratumInterfaceAudit.lean 1–135, 600–640,
  730–870; BackgroundIndependence.lean 1–30; A6Instantiation.lean 1–30; C3Necessity.lean (full);
  CausalReadback.lean 1–75, 290–330; PhysicalC4Discharge.lean 1–128, 140–152, 486–496;
  InternalObserver.lean 1–72, 169–226, 315–318; SpectatorBridge.lean 218–232; AncillaClosure.lean
  243–252; OperationalAssembly.lean 660–670; ReadbackRobustness.lean 1–14; ObservabilityQuotient.lean
  1–40, 267–274; PassiveQuotient.lean 1–30, 218–226, 444–480, 530–567; theorem lists and grep
  excerpts of PhysicalC4StorageReadback, StochasticInterface, DiagonalTheory, RankGapTheory,
  SubstantiveCensus, LevelOneSeam, LevelOneRecursion, PhysicalCharacterization, IsometryExtension,
  PassiveIndependence, HiddenMemory, RootedClassification; `verification/lean/OI_Structural_Core.lean`
  1–25. Script reads (byte-exact, outputs kept): every OIBridge module (census part B, bridge
  checks), the twelve I1 modules (census part A), `verification/lean/*.lean` (part C), the 104
  declarations of `statements.out`.
- Manuscripts: Main.md 1–110 in full; the labelled statements of 111–659 (scan) and lines 137,
  141, 159, 167, 286, 433, 447, 456, 484–492, 594, 602, 612, 614 in full; Methodology.md 140–164,
  216–286; Substratum.md 70–130; Explainer.md 63–69, 905 and a grep of the file; book
  ch01-observation.md 18–75 and a grep; the census scripts read Main 24–659, Methodology 160–163,
  216–286, Substratum 88–130, 204–219, the whole Explainer, the whole of every book file and FULL.md.
- Status records: verification/ROADMAP.md 1–76, 665–970, 1392–1469 (and the whole file by script);
  verification/README.md 60–100, 625–640 and a grep.

## §3 What is not claimed

- No status is upgraded: every status is the one the cited record states; `proved [manuscript, not
  K]` marks a manuscript's own proof claim and is never read as [K].
- No derivation and no verdict on (b), (b_min), `K = Q3` or the stage's question; no item is
  declared applicable or inapplicable to the pair cone beyond recording that no bridge at L reaches
  it. "Bridge absent" means: no kernel declaration at L, by the stated mechanical searches, and the
  corpus sentences quoted; it does not say no bridge can exist.
- The H→M bridges listed transfer objects to the matrix level only; nothing here says what they
  imply for a field-neutral pair (that is thread I4's matrix-to-pair question).
- The status variances in §0 are recorded, not resolved; no manuscript wording is judged.
- The kernel census is complete for the twelve modules and `OICore` and for the token census; it is
  not a census of every module that mentions an observer (three named modules unfinished, §0).

## §4 Evidence log

Scripts (all `python3 -I -B <script>` from `pt/I1/`, stdout `.out`, stderr plus `exit N` in `.err`;
decision rule in each header before the first run; every final run replayed byte-identically to
`.replay.*`; earlier runs kept):

| script | runs | final result | replay |
|---|---|---|---|
| `kernel_census.py` | 1 | 41 entries (part A), 94 (part B), 10 (part C) | identical |
| `bridge_check.py` | 1 | controls green; PAIR NO-MODULE; OPER NO-MODULE | identical |
| `bridge_check2.py` | 1 | control green; NO-MODULE | identical |
| `bridge_check3.py` | 1 | control green; DISJOINT (closures listed) | identical |
| `bridge_check4.py` | 1 | control green (43); NONE-FOUND over 21 modules | identical |
| `statements.py` | 2 (run 1 kept: imprecise manuscript line picks) | 104 declarations, 0 missing, 153 lines | identical |
| `census_ms.py` | 2 (run 1 kept: 18 unmapped) | 946 sentences, 0 unmapped | identical |
| `census_rm.py` | 2 (run 1 kept: settled-negatively rows missed) | 96 items, 0 unmapped | identical |
| `quote_check.py` | 7 (runs 1–6 kept; run 5's replay removed after `cmp`, NOTES) | 164 fragments, ALL-EXACT, countercontrol green | identical |

sha256 of every file written by this thread except RESULT.md (computed 17:23 UTC, after NOTES.md
was closed):

```
7af59f380a5b400359f16e3327e7d0e33e0c454958afa4c11e130e53809c41d1  .end_marker
0827ab56cd2bdb167bbe5ea84c8c2c9648c405de408adb1fc72754b15231de9f  .start_marker
216468746cf63eda3028618d31979b1018f973caec0598e42ef756ee7edfc506  CENSUS.md
a4a8806b219141975b6e2f6e5ccc13e723cb29c0b158386fa19049966eb66a99  INVENTORY.md
b4e1b00de0e53e60ad573c04145496c1fad26cd59eba583f11761e908db7c09e  NOTES.md
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  bridge_check.err
8833ddfb0e06c0e69e6855281aa26e8800d8e2ce54a6938b8a0126e2d23bf656  bridge_check.out
a30bfd5533262e7539de443c4d284606aad33efdd5aee233d52124b424466a1a  bridge_check.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  bridge_check.replay.err
8833ddfb0e06c0e69e6855281aa26e8800d8e2ce54a6938b8a0126e2d23bf656  bridge_check.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  bridge_check2.err
61025a730e1fc7b58b28a788de22ae72ce1b812f03e23227d5d105570bc9b12b  bridge_check2.out
fe87382f2846f24096cec32b482e1a54fa7e0bb06062b39f7295d07b544588d7  bridge_check2.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  bridge_check2.replay.err
61025a730e1fc7b58b28a788de22ae72ce1b812f03e23227d5d105570bc9b12b  bridge_check2.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  bridge_check3.err
e9af3cdaaea1ce8c61e44bba6c2514c3070663224f7ba964ce90bf9b86a663c8  bridge_check3.out
cbbf48ed8a7c56f392042d71f503a0cc9dc488245a0272cc0bb327bd5dfb73b8  bridge_check3.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  bridge_check3.replay.err
e9af3cdaaea1ce8c61e44bba6c2514c3070663224f7ba964ce90bf9b86a663c8  bridge_check3.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  bridge_check4.err
e9397ea31606b137eac36c5238d28037a5fc15ac899da6039e71571358e378cb  bridge_check4.out
705d199557576016576d2fc36b2a7e052a7dfbb8560aa0999cf0272bdc4cdb67  bridge_check4.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  bridge_check4.replay.err
e9397ea31606b137eac36c5238d28037a5fc15ac899da6039e71571358e378cb  bridge_check4.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  census_ms.err
de2c08c8cfe82e848d74759ae164a6e7168599a70e613dc2031a5b10a2abfa4c  census_ms.out
11289f3b2f119236e59c5a7ff5b022bb48f8ae32a363ee6a1237ab292ce19714  census_ms.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  census_ms.replay.err
de2c08c8cfe82e848d74759ae164a6e7168599a70e613dc2031a5b10a2abfa4c  census_ms.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  census_ms.run1.err
c1d7bf73141c4f5d7ddd524dd0cc1ea8bf33a589a9196a6423df05e06a1121e6  census_ms.run1.out
1e52e67294762fddc44593933d593206f729dc52cd3035f59ee9b36bc71c9f06  census_ms.run1.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  census_rm.err
26a9e67bf50d6303a90f01f092674205157f1740d9307d00629c70040a95fd16  census_rm.out
74084dfda5dc83fc85bce9e9a14a9f4440546d3c327658954e5f7e4a57c7a281  census_rm.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  census_rm.replay.err
26a9e67bf50d6303a90f01f092674205157f1740d9307d00629c70040a95fd16  census_rm.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  census_rm.run1.err
6782fbb5da7a35e02832970270818b39d434e8120f6707a613126557cfd15d4b  census_rm.run1.out
c912212c572910afa1eeda0a0407c282f5697a2412fd4d923f8f84906c04283a  census_rm.run1.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  kernel_census.err
427fc24083a5ff9d3ac5c6205fa0436fc204faa30812ff2c72a24b2880ca7e75  kernel_census.out
24c403a720306e75d415766622fa4a1f83c83514b096399f03b79a165b2325d2  kernel_census.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  kernel_census.replay.err
427fc24083a5ff9d3ac5c6205fa0436fc204faa30812ff2c72a24b2880ca7e75  kernel_census.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  quote_check.err
c20aa745161d4585b30f9a05885015d3008aebbc6f8f1f90307f1c6770bd0f84  quote_check.out
fe16963ceef9c73a3c3d798282068926179ec56e1fd934a6315ae9621acde1f0  quote_check.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  quote_check.replay.err
c20aa745161d4585b30f9a05885015d3008aebbc6f8f1f90307f1c6770bd0f84  quote_check.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  quote_check.run1.err
f22e9d4d57827c6b86a14fe9f3bdb5ef84aad9d26bc1d2ffe4807bab06ce7f62  quote_check.run1.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  quote_check.run2.err
895c27ca0e65c4ca46128e5d03e00da25686a13b4ec687abcba1eb89d7efb7b9  quote_check.run2.out
2b5b2ffd9074ef20e89b6dc064ba1c666ed32cc1f019888d1d600495a6336a2a  quote_check.run2.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  quote_check.run3.err
e7dcda5143e054ce8eb7046f0a50202557345849a560d8950a82305d45868766  quote_check.run3.out
c40c85c88c92d6a8ba394077eec68a41abb8f6dbac0ff41226fe488f215b1527  quote_check.run3.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  quote_check.run4.err
00828c5a5da973a81e86151e36762816bbfe004675230cf167ad4648b2b16d96  quote_check.run4.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  quote_check.run5.err
9ec20aa7e8c1b424d747b32438ada44060a97e596077ec87d22b46629cc04fc4  quote_check.run5.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  quote_check.run6.err
9ec20aa7e8c1b424d747b32438ada44060a97e596077ec87d22b46629cc04fc4  quote_check.run6.out
13cbba8548993856531193af362ff21995caaf366653ea42d06a100eac1c4aa4  quote_check.run6.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  quote_check.run6.replay.err
9ec20aa7e8c1b424d747b32438ada44060a97e596077ec87d22b46629cc04fc4  quote_check.run6.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  statements.err
8bfedd8ccf7845a9be35e13dd159f46f0a279c6231d3517074b69a7313efcb51  statements.out
5d71b4aff9b0e1908242ba17cf7a00fdf4d65643505c7eb9cf6798a1334bc992  statements.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  statements.replay.err
8bfedd8ccf7845a9be35e13dd159f46f0a279c6231d3517074b69a7313efcb51  statements.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  statements.run1.err
c98d1d9c2b5c1f105eb4296ab233b18dd15af1773ccd2c43781141e8fdd4dab4  statements.run1.out
94d7cfab6a570bf630bd91a3f55b9f702b4392011c8cdff199503bb732ac3831  statements.run1.py
```

## §5 Integrity

- Start (`.start_marker`, 16:51:54Z, written first into a directory confirmed absent at 16:50:48Z):
  six manifests `sha256sum -c --quiet` exit 0 with no complaint; `audit/stage3-inputs/ns.manifest.sha256`
  OK from its own directory; `pt/base` HEAD = `9f9f8257a980a1819fbbc1dc0019917cf8678626`, `status
  --porcelain` empty, no `__pycache__`/`.pyc`; the ten protocol files match their prefixes
  (`239dc123`, `b41aa0e7`, `2a2f78f3`, `38603692`, `086a4cb8`, `1a649168`, `d3da2811`, `9e01f098`,
  `1f639115`, `b277b7c1`) and the ten sidecars verify (six from `pt/`, four from SCRATCH); `pt/`
  top-level listing with mtimes recorded.
- End (`.end_marker`, 17:22:57Z): the same checks, all green; the listing shows the sibling
  directories `I3`, `I4` created and `C5`, `D5`, `I2`, `audit` modified since the start — all
  excluded areas. Anomaly sweep: 0 files under `pt/` newer than `.start_marker` outside `pt/I1/`,
  `pt/I2/`, `pt/I3/`, `pt/I4/`, `pt/D5/`, `pt/C5/`, `pt/audit/`, `pt/audit*-replay/`; nothing
  quarantined; `pt/I1/` holds only files this thread wrote.
- Writes: only inside `pt/I1/`; every file written in parts of at most 250 lines per write call
  (script outputs are produced by the scripts). Git: read-only (`rev-parse`, `status` with
  `GIT_OPTIONAL_LOCKS=0`). No branch, PR, CI, network, publication or sub-agent.
