# A1-09 — A1 dependency census (A1-C01)

**Status: PARTIAL SOURCE AUDIT / UNCLASSIFIED COVERAGE — NOT A1-C01 COMPLETION OR G2 SIGN-OFF.** First pass independently reviewed (ACCEPT WITH CHANGES); the review's three required changes are applied in this revision by the coordinating session as writer (owner decision #1169 c.6922450446).
Scientific source claims remain governed by their own evidence and reviews. A1 is OPEN / UNADOPTED; physical source is NOT PASSED. This file changes no manuscript, Lean declaration, hypothesis, grade or completion-register entry.

**Accountable Issue:** [#1334](https://github.com/amaybaum/incompleteness/issues/1334); [owner activation](https://github.com/amaybaum/incompleteness/issues/1334#issuecomment-6918420877), [in-session execution clarification](https://github.com/amaybaum/incompleteness/issues/1334#issuecomment-6919384575); **coordination:** [#1169, A1-C00–C11 checklist](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6916312927). Writer of the first pass (to `a64e2528`): **ChatGPT in the owner-directed session**, not Codex. Writer of the later revisions: the coordinating Claude Code session (owner decision #1169 c.6922450446). The first pass was independently reviewed; later revisions are checked by their own delta reviews. Integration gates remain separate.

**Immutable source snapshot:** `6eac91ee25a1afaea4ed148b0c54967a08b12ac3` (GitHub `main` at preparation). The reader must distinguish this from later `main`. Source positions below refer to this exact commit, not to a moving branch.

## 1. Claim and coverage semantics

- **A — existing A1-free mathematical result:** check its explicitly supplied state, finite observable interface, positivity, continuity, carrier or operational assumptions. A finite *tested observable alphabet* does not by itself posit a finite *total physical universe*.
- **F — valid finite-model / finite-representative result:** keep the exact finite hypothesis; do not promote to a general infinite system or to a claim about nature.
- **W — weaker contract identified but not proved in the physical model:** no scientific promotion. A conditional algebraic identity may be A even if its native/physical realization remains W.
- **U — candidate unqualified or unsupported physical inference:** submit for separately authorized minimum-change manuscript correction or independent proof; no edit here.
- **X — UNCLASSIFIED:** source inaccessible or chain not traced; cannot be counted as cleared. Scan absence or a green CI is not a proof of independence.

An observation-window realization is not automatically a single coherent state-and-dynamics system across all windows. A finite *link representation*, finite *matrix rank*, finite *region*, finite *entropy*, finite *time horizon* and finite *total configuration set* are six different statements.

## 2. Reproducible source inventory and search recipe

### 2.1 Snapshot and files actually inspected

The Git tree was read at the pinned commit, not inferred from GitHub search ranking.

| Corpus | Inventory at pin | Read in this revision | Coverage limitation |
|---|---|---|---|
| Maintained manuscript sources | All **12** root `papers/*.md` files: Bioinformatics, Complexity, Computation, GR, Introduction, Juno, Main, Medicine, Methodology, SM, Structure, Substratum | All 12 were read through a lexical/dependency-hit pass; contextual source ranges checked for Main, Substratum, SM, GR, Structure, Complexity, Medicine and selected chapters | Not every mathematical proof paragraph in every paper received a backwards semantic proof-chain audit |
| Paper publication mirrors | Corresponding 12 `papers/*.tex` and 12 `papers/*.pdf`, identified in the root paper tree; `papers/main_repro/` and `papers/oi_lattice_code/` are additional subtrees | File inventory only | `.tex` parity/diffs, PDFs and nested papers evidence are **X** |
| Book chapter/back matter sources | 29 accessible `book/*.md` files other than `The-Incompleteness-of-Observation-FULL.md`, including chapters ch00–ch19, appendices, bibliography, glossary and guides | All 29 read by lexical/dependency-hit pass; contextual ranges checked for ch01/ch02/ch09/ch14, appendix B/C and ch18 | Unmatched indirect proof imports must still be checked semantically |
| Generated FULL book | `book/The-Incompleteness-of-Observation-FULL.md` (1,685,004 bytes), `FULL.tex` (1,777,635 bytes), `FULL.pdf` (2,107,612 bytes), plus `unicode-fix.tex` | Tree/blob metadata only; connector returned empty text for the two >1MB textual FULL files, PDF is binary | **X: all FULL mirror claim sites and text parity**. Do not equate chapter scanning with verified FULL regeneration |
| Lean proof corpus | **241** `verification/lean-mathlib/OIBridge/*.lean` modules; `OIBridge.lean` root import; **6** `verification/lean/OI_*.lean` legacy modules (248 identified Lean files) | The module tree was enumerated. Source inspected in `Equivalence`, `RecurrenceHorizon`, `ObservableFactorRecurrence`, `ObservableMeasureReturn`, `MeasuredReciprocity`, `SubstratumInterfaceAudit`, `GeneralCarrier`, `ShellAssignment` and `LinkDecomposition` | **X: 232 other OIBridge files, root import, 6 legacy modules** lack individual declaration-by-declaration premise tracing in this revision; no fresh Lean build |
| Proof registries | `verification/lean-manuscript-census.json` (123 families, manuscript list 12), `verification/coverage/LEDGER.json` (133 entries, 20 unattached), `verification/audit-census.json` | JSON parsed; A1-sensitive entries and notes located; not every entry checked against its anchor | **X: remaining family/entry-level backward traces and declaration-to-claim exhaustiveness** |
| Other verification | `verification/audits/`, `verification/programmes/`, `verification/receipts/`, `verification/lean/`, `verification/lean-mathlib/`, `verification/infrastructure/`, `verification/seals/`, `verification/archive/` | Major directory trees enumerated, the merged recovery matrix read in full, #1015/#1029 scopes and #1169 closure register consulted | **X: recursive verification evidence inventory, proof probes, code, PDFs, and historical/branch-only records**. Source material beyond pinned main is not automatically current proof |

The 29 book files inspected **exclude** the FULL Markdown file; the book directory contains 30 Markdown files including that FULL file. No claim that the complete corpus was scanned is made. The initial lexical scan used, case-insensitively, A1, total configuration/state/substratum, finite carrier/system/substratum, recurrence, P-indivisibility, canonical typicality, uniform prior/count/measure, finite determinant, equilibrium, cosmic recurrence, and infinite carrier/sector/system. A filename or textual zero-hit is **not** a dependency clearance; e.g. local empirical claims can inherit P7/P12(b) silently.

### 2.2 Mandatory fresh-run recipe (not claimed executed locally)

From an actual full checkout, including generated mirrors and all subdirectories, run:

```bash
git checkout 6eac91ee25a1afaea4ed148b0c54967a08b12ac3
git status --porcelain=v1
git ls-files papers book verification > a1-09-paths.txt
git ls-files '*.md' '*.tex' '*.lean' '*.json' '*.py' > a1-09-text-paths.txt
rg -n -i '(\bA1\b|total.{0,35}(finite|finiteness|state|carrier|substratum)|finite.{0,35}(state|carrier|substratum|configuration|representative)|recurren|P.indivis|uniform.{0,30}(count|prior|measure)|determinant|typicality|equilibrium|infinite.time|all.time)' papers book verification > a1-09-explicit-hits.txt
rg -n -i '(permutation.{0,30}(order|cycle)|finite.{0,30}(spectrum|dimension|rank|matrix)|canonical|microcanonical|gibbs|count.{0,25}(shell|fibre|state)|transfer.{0,40}(representative|window|horizon)|exact.{0,25}return)' papers book verification > a1-09-indirect-hits.txt
rg -n '^((private )?(theorem|lemma|def|instance|noncomputable def)|variable|section|namespace)|(\[Fintype|\[Finite|\bFinset\b|\bMeasurePreserving\b)' verification/lean-mathlib verification/lean > a1-09-lean-declarations.txt
```

Then (i) reconcile source paths against the `git ls-files` inventory and every Lean declaration against its enclosing `section`/`variable`/imported hypotheses; (ii) enumerate every claim in `LEDGER.json`, census family/anchor/supersession, programme and proof receipt; (iii) deduplicate by claim and first load-bearing inference rather than by word hit; (iv) examine both positive and negative controls; (v) verify `.md` vs `.tex` vs FULL/chapter mirrors and render-to-source provenance; (vi) record a line-anchored decision for every site or an **X** entry. For a theorem on a finite observable type with an arbitrary hidden type, do **not** tag it A1-dependent merely because `Fintype V` appears. For a finite spatial torus with finite alphabet, tag total-carrier finiteness even if the proof does not spell out A1.

**This execution did not run the above local recipe.** The GitHub connector provided immutable trees and selected full-file/range reads, not a locally cloned corpus; that is a material closure blocker.

## 3. Claim-by-claim dependency trace (first pass)

Source citations are `path:line` at the pinned commit; short Lean references are below `verification/lean-mathlib/OIBridge/`. A paper-only result is distinguished from the formal proof of one of its ingredients. Review statuses are not upgraded by this table.

| ID / closure ID | Earliest load-bearing statement and reference | Dependency and evidence classification | Required disposition / proof or correction gate |
|---|---|---|---|
| D01 / C00,C02 | `papers/Main.md:42–46`; `book/ch01-observation.md:25–32`; `#1015` | Finite distinguishable visible states (Lemma 1), **A** at its observational scope; extrapolation to all of `S` is **not** supplied | Preserve observer-relative statement; explicitly separate physical A1 |
| D02 / C02 | `papers/Main.md:433–437, 518–524`; `Equivalence.lean:2–39, 422` | `S⇔D⇔Q_fb` **A** as an existential finite-horizon law equivalence; construction **F** for each finite witness's total carrier; Lean `S_imp_D` may use correlated initial law | Keep common-prior paper proof separate; prohibit single-carrier all-horizons promotion |
| D03 / C02 | `papers/Main.md:163–178` and `CausalReadback` / `TrajectoryMemory` registry | Accessible history-readback conditional memory does not require global finite permutation order; **A** where finite history, positivity and stipulated readback gap are supplied; not a universal physically sourced readback | Preserve exact window, full-support, history and physical-source caveats; do not equate C4 with P-indivisibility |
| D04 / C00,C03 | `papers/Substratum.md:92,98,193`; `SubstratumInterfaceAudit.lean:83–110,175–185` | A1 explicit **F**; finite A4 torus and finite alphabet already imply a finite global configuration set. Independent infinite-carrier variant **W** | Retain conditional Theorem 23 class; no word-only deletion of A1 and no infinite physical carrier inference |
| D05 / C03 | `papers/Substratum.md:94` (A2 eventual image) | Eventual-image injectivity→surjectivity/bijection for a self-map uses finiteness of the total set **F**; does not follow for an arbitrary infinite shift | Scope finite eventual image or prove a different replacement; check wording in Main and book |
| D06 / C10 | `papers/Main.md:109–127`; `book/ch01-observation.md:93–119`; `book/ch18-beyond.md:174–192` | Exact `φ^N=id` uses finite global carrier **F**; neither one visible return nor an arbitrary infinite measure-preserving system implies it | Preserve finite theorem; A1-10/#1335 controls exact return, visible return and accessible-history return separately |
| D07 / C10 | `papers/Main.md:135–139,178`; `RecurrenceHorizon.lean:104–148` | Identity return plus earlier overlapping rooted rows implies recurrence-scale P-indivisibility; algebraic horizon theorem **A** given identity return, **F** for native finite-cycle supply | State identity-return hypothesis explicitly; conditional result is not universal infinite-time indivisibility |
| D08 / C10 | `ObservableFactorRecurrence.lean:48,68`, `ObservableMeasureReturn.lean:63,83` | **A** set/change-event and ENNReal measured-return identities with finite visible alphabet, specified measure and positive finite cell masses; no total finite carrier. **W** as physical rooted stochastic law | Do not count as a universal return theorem; source/normalize a real row-stochastic law separately |
| D09 / C10 | `papers/Main.md:439–441` | Nonpermutation-one-step ⇒ indivisible uses **F** finite-cycle return. The lemma concerns the marginalized dilation of Main:437, a finite construction, and its proof cites §2.3's finite recurrence theorem | **No defect; optional precision at most.** #1313 row M-30 ruled it "a lemma in the finite-realization setting of §2.3/§3.2". `book/appendix-b-derivations.md:413` (Lemma B.7.3) already states finiteness and the recurrence scale, so no book change |
| D10 / C10 | `papers/Main.md:330–336`; `book/appendix-b-derivations.md:92–96` | CP-indivisibility consequence **F** for diagonal-preserving finite permutation-dilation family; does not hold for arbitrary CPTP processes | Preserve existing scope and ancilla distinction; no independent universal quantum conclusion |
| D11 / C02,C10 | `papers/Introduction.md:87–95,178`; `book/ch18-beyond.md:166–192` | Recurrence and repeated forecasting examples **F** when derived from finite recurrence; same-world extension beyond fixed horizons **W** | Check all-time language against exact carrier premises; preserve limitation on gluing independent horizon models |
| D12 / C02 | `papers/Main.md:433–441,457–463`; `Equivalence.lean:60–90,422` | Uniform-prior finite permutation construction/counting and specific doubly stochastic marginal **F**; an arbitrary normalized prior or infinite hidden carrier changes it | Keep correlated-law vs common-prior forms distinct, and no physical uniform-prior selection |
| D13 / C02 | `papers/Main.md:471,520–524`; `verification/audits/foundations/p1-application-20261116/` | Finite-horizon weighted channel and process dilution **A** as bounded mathematical constructions; global shared dynamics **W** | Carry the prior, interventions, accessible histories and common-carrier scope explicitly |
| D14 / C03,C07 | `papers/Substratum.md:253,262–266` (Theorem 24), `papers/GR.md:118,126–128` | Exact invisibility for independently prepared normalized **finite decoupled** deep factor **F**; slow coupled sector has a quantitative finite-model comparison, not exact gauge invariance | Limit physical transfer to those hypotheses; **W** for infinitely extended interacting deep sector and matched preparation law |
| D15 / C04 | `papers/Substratum.md:157–167`; `papers/SM.md:340–376,523–597`; `LinkDecomposition.lean:49–55,316–326,479–488` | Local six-link `3⊕2⊕1` representation **A** conditional on supplied cubic module, link action, scalar kinetics, condensate and matter representation. Six links are finite-dimensional, not a finite universe | Keep local algebra separate from sourced gauge bosons, Yang–Mills dynamics, particle mass spectrum and QCD; A1-11/#1336 owns new forward trace |
| D16 / C04,C07 | `papers/SM.md:390–416,432–466,535–547,577–597` | Reverse cubic identification, taste/fermion family, charge solution have distinct lattice, chiral, anomaly and condensate inputs; **F** for selected finite periodic examples; **W** for physical selection | Do not infer actual matter spectrum from existence of a representation |
| D17 / C06 | `papers/Substratum.md:123–137,145,157,193–195`; `papers/SM.md:242–248` | Stage 1 finite witness not identified with the fixed A4 spatial carrier; projection requires a selected law, observation and dynamics. Fixed-lag block identity **A** for supplied operators; native bridge **W** | Preserve A1-01 #1321, A1-06 #1326 and A1-08 #1333 SOURCE GAP. Stop before a fabricated scalar observer-field identification |
| D18 / C07 | `papers/SM.md:252–256` (Lemma 1c(ii)) | Block resolvent and determinant cancellation use finite-dimensional matrices; meromorphic pole transfer is **F** here, infinite-carrier analytically continued spectrum **W** | A true infinite operator theorem needs domains, boundedness/spectral control and analytic continuation; do not cite finite determinant as that proof |
| D19 / C07 | `papers/SM.md:252(iii),270–282` | Companion temporal block and factor-2 spatial normalization are **supplied**, not derived from canonical trace-out. **W** observer-to-wave identification | Source same-carrier projected kernel, memory response and companion law before physical dispersion |
| D20 / C03,C07 | `papers/SM.md:150–156,196–210` | Finite graph-family continuum/curvature limit **W**; cubic nearest-neighbour hop metric fails stated Euclidean stretch control | Retain explicit metric/curvature regularity and d=3 filters; no automatic continuum from finite cells |
| D21 / C05 | `papers/SM.md:641–649`; `Reciprocity.lean:67,79,129,142` | Reversal bijects transition fibres, counting turns fibre cardinalities into probabilities **F**; same uniform hidden prior used across roots | Keep exact finite-count statement; differentiate conditional-probability reciprocity from weighted flux |
| D22 / C05 | `MeasuredReciprocity.lean:90–136`, merged by #1327 | **A** probability-measure flux reciprocity on arbitrary measurable total carrier with reversibility, measure preservation, measurable visible map/reversal, positive masses for conditional ratios and equal roots when needed | Existing formal mathematical result. Source of actual physical reference law, time reversal and observer cut remains **W**; no independent native physical P6 |
| D23 / C08 | `papers/GR.md:58–70`, `ShellAssignment.lean:69,90,104,119` | Uniform finite energy-shell counting, weak boundary interaction and shell weights **F**; kernel shell lemmas do not select a physically conserved energy or shell | Keep H-count explicitly conditional; A1-07 #1328 SOURCE GAP at physically interpreted real coupled energy |
| D24 / C08 | `papers/GR.md:70–88,98–102,617,623–627` | Scalar horizon calibration can be **A** as algebra given externally supplied classical slope and same-transition positive detector-rate slope; counting-based derivation **F** / physical justification **W** | H-slope, H-frame, state, horizon identity and detector matching are separately unsourced; no independent physical `1/4` derivation |
| D25 / C08 | `papers/GR.md:118,126–128` | Finite uniform-fibre boundary transition error under H-BD **F**; relative log-rate and energy derivatives are not bounded by rowwise absolute error alone | Require positivity, relative errors, coupled shell and source, before P7 transfer |
| D26 / C08,C11 | `papers/GR.md:663–669` | Claim "A1 (finiteness) implies S3 with finite ε" is a **U candidate**: a finite abstract state set does not alone specify a physical length, horizon mode-count unit or identification with ε | Correction candidate: S3 must be separately specified or derived from additional geometry/operational premises. Recheck GR theorem's purported weaker-than-A1–A6 comparison |
| D27 / C09 | `papers/Main.md:746–758,762`; `verification/coverage/LEDGER.json` observer-selection entries | Compressed-channel forward decay uses separately posited reference law, (EM), record/erosion and time-window controls. **W** as a physical observer selection; finite permutation spectrum **F** only for exact microscopic evolution | Retain A1-05 #1332 conditional P8-M reading; do not equate `(PUP)^n` with `PU^nP` |
| D28 / C09 | `papers/Main.md:754–760` | Canonical typicality imports a specified typical state on a finite quantum region/energy shell, not every microstate or region. P8-S physical state and finite-region record transfer **W** | Keep state, quantifier, error and coupling assumptions; A1-05 P8-S SOURCE GAP |
| D29 / C09,C11 | `papers/Substratum.md:401–413`; `papers/Main.md:760–762` | An observed arrow, time direction, and anti-Boltzmann-brain universal exclusion do not follow from recurrence or stationarity. **W** for physical arrow; narrower local fast-mixing conditional exclusion survives | Retain preparation, asymmetry and readback premises, and no unconditional cosmological prediction |
| D30 / C11 | `papers/Main.md:360–371`; `book/appendix-c-objections.md:29–50`; #1313 | Causal-cone Bell ≤2 theorem **A** on finite wing/readout regions and finite-range local dynamics, even on an arbitrary-cardinality site set for specified nearest-neighbour rule; ontic parameter-dependence route is a **W** physical assumption | Do not infer full Bell violation, measurement independence or no-signalling from A1 or local algebra |
| D31 / C11 | `GeneralCarrier.lean:97–113,160–170`; `papers/Main.md:646–660` | Operational QM characterization **A** on given nonempty *finite observable* systems under five physical-completion conditions; bare OI has a countermodel. Native sources for the conditions **W** | Do not identify fixed-basis representation with physical full OI↔QM, coherent instruments/composites or quantum-set exclusion |
| D32 / C11 | `papers/SM.md:835,1416`; `papers/Structure.md:929–968` | QCD, strong CP, couplings, mass predictions and no-GUT claims inherit selected carrier, gauge/representation, dynamics, state and native observer gaps. **W** wherever physical reconstruction is claimed; local algebra is narrower **A** | Trace individual downstream predictions against #914/#1063 and retained SM assumptions in later full pass; **X** for unaudited per-claim dependency chains |
| D33 / C11 | `papers/Computation.md:176–180`; `book/ch14-quantum-computing.md:96–110,268` | BQP characterization explicitly assumes *finite* OI model plus operational closure, gate and efficiency postulates: **F / conditional**, not a theorem about nature. Finite-system exclusion of infinite-time resources **F** | Retain model-conditioned claim, no unconditional ceiling for all physical technologies |
| D34a / C11 | `papers/Medicine.md:35` | **A1 part.** "Proves … P-indivisibility, on a common window" conflicts with Main:137–139: the full-support coincidence is a global recurrence-cycle result on a finite representative, and C4 does not force P-indivisibility on accessible windows. **U** | Corrected on `main` by #1341 (`5ea8672f`), using Medicine:13's wording |
| D34b / C11 | `papers/Medicine.md:37` | **Not an A1 matter.** "At every scale, C1–C4 are satisfied" is an unsourced empirical assertion | Tracked separately as #1342 R4 |
| D35 / C11 | `papers/Complexity.md:372–376,484–486` | Enzyme analogy itself acknowledges non-closed/non-bijective biology; quantum backflow and P-indivisibility should not be silently read as finite-substratum proofs. **F** for finite theory; experimental biological extrapolation **W** | Preserve enzyme scope note; inspect individual computational predictions before propagating recurrence |
| D36 / C03,C11 | `papers/Structure.md:224–230,264–272` | Document correctly states finite-rank BFSS has continuous matrix entries, then asserts lattice spacing plus fixed rank gives finite-cardinality configuration space. This inference is **U candidate / internal inconsistency** absent a *separate finite-valued matrix-entry discretization* | Separately correct the fixed-N/fixed-spacing ⇒ finite-cardinality claim or supply a genuinely finite alphabet/constrained phase space. No bridge established |
| D37 / C03,C11 | `book/ch09-universality.md:190–196` | "For any finite N the bridge is consistent" uses finite matrix rank as if it resolves A1; finite rank alone does not give finite-cardinality `S`. **U candidate** | Narrow to hypothetical discretized finite-state representation with separately verified A2–A6, or withdraw bridge consistency |
| D38 / C00,C10 | `book/ch18-beyond.md:164–192` | Explicitly under A1, exact recurrence and finite information are **F**, not claims of actual total finiteness | Preserve hypotheticals; check all summary restatements in FULL mirror |
| D39 / C00,C11 | `book/appendix-c-objections.md:114–132` | The continuum-QFT "artifact" language can be read as an actual metaphysical conclusion even though A1 is open. **U candidate** in last two paragraphs, with correct conditional qualifications earlier | Qualify as possibility *if* finite microscopic model is physically realized; no established universe-wide cutoff |
| D40 / C02,C11 | `book/ch14-quantum-computing.md:105` | Finite substratum ⇒ finite-dimensional representation for that selected finite model **F**; the theorem's own finite hypothesis prevents universal inference | Retain condition and distinguish per-horizon Hilbert space from fixed global physical Hilbert space |
| D41 / C11 | `papers/Structure.md:47,80,134–140,646,718,1138–1177` | Multiple cross-theory summaries reimport A1–A6 and recurrence-scale indivisibility; **F** where local structural class/cycle is stated, **X** where broad physics or another programme inherits an OI theorem | Audit every such target sentence, not only the term A1; cross-program partial-trace analogy is not a physical carrier identification |
| D42 / C01 | `verification/lean-manuscript-census.json:479–516,733–756,1697–1717`; `verification/coverage/LEDGER.json:454–502,923–930,1381–1420` | Registry includes scope notes but is not a complete full-source A1 proof audit. Rooted recurrence, axioms and observer selection have distinct premises. **X** for the remaining 123-family/133-entry comparison | Reconcile each claim, grade and live theorem anchor on pinned main; no grade move on search alone |
| D43 / C01 | `book/The-Incompleteness-of-Observation-FULL.md`, `FULL.tex`, `FULL.pdf` | FULL Markdown resolved for claim coverage by batch 1 (§7); `FULL.tex` stamped; `FULL.pdf` not stamped | PDF rendering parity not checked by this census |
| D44 / C01 | Remaining `OIBridge`, six legacy Lean modules, `verification/programmes` and nested proof and probe evidence | Enumerated but not fully premise-traced: **X** | Declaration/import-level audit, identify every nonobvious implicit finite-state dependency, verify ledger anchors and negative controls |

### 3.1 Distinct A1-free controls already on `main`

1. `Equivalence.lean` finite-horizon S/D/Q_fb representation theorem: a **finite witness** exists per finite visible law; not a physical single-carrier world theorem.
2. `RecurrenceHorizon.lean` abstract identity-return + earlier overlap ⇒ P-indivisibility: does **not** obtain the required return from arbitrary infinite dynamics.
3. `ObservableFactorRecurrence.lean` and `ObservableMeasureReturn.lean` visible-change / measured-return equivalences for arbitrary hidden type with measured finite visible cells; not an autonomous measured-return mechanism.
4. `MeasuredReciprocity.lean` measured reciprocal flux and conditional ratios from a specified preserved probability law and reversible structure; physical law selection is open.
5. `LinkDecomposition.lean` exact six-link rational representation and finite local decomposition; it supplies neither H-link physical selection nor real-world QCD.
6. `SubstratumInterfaceAudit.lean` finite sites + finite alphabet imply A1, thereby protecting finite-model consistency but **not** giving an infinite-model reconstruction.
7. `ShellAssignment.lean` finite invariant shell implies invariant finite weights in a possibly larger ambient carrier; no physical energy-shell selection.
8. `GeneralCarrier.lean` finite operational quantum characterization under extra completion conditions with a bare-OI countermodel, not a native OI-to-QM derivation.

The declarations were inspected as repository source. Kernel-check status is inherited from existing project records, not a newly run build or independent review of all theorem assumptions.

## 4. A1-C00–C11 closure crosswalk (do not edit authoritative register)

| Closure item | First-pass status and next gate |
|---|---|
| C00 | #1313 public A1 qualification retained; D26/D39 corrected by #1341, D09 withdrawn (§5.1) |
| C01 | **OPEN / X**: 232 Lean modules, registry entry-by-entry, other verification and indirect paper chains not exhaustive (FULL Markdown resolved by §7) |
| C02 | **Scoped** finite-window equivalence; common physical world/continuity of carriers unresolved (D02/D03/D12/D13) |
| C03 | **Finite-class only**; A4 torus finite alphabet still finite. Matrix-model "finite rank = finite carrier" wording check (D36/D37) |
| C04 | **A** conditional local link algebra; physical gauge/representation selection open and A1-11 separately assigned |
| C05 | **A** measured P6 conditional theorem on main, **F** counted specialization; native law source open |
| C06 | **OPEN** actual scalar observer field and projected kernel, as A1-06/A1-08 |
| C07 | **OPEN** companion wave/spectrum/continuum and same-realization transfer |
| C08 | **OPEN** coupled physical energy, shells, relative weights, rate and detector calibration; finite shell valid |
| C09 | **OPEN** P8-M forward mathematical step conditional; P8-S state/record transfer and arrow unsourced |
| C10 | **F** exact finite recurrence, **A** abstract/measure return conditionals; weak-premise study belongs A1-10 |
| C11 | **OPEN / X** propagation through quantum Bell, SM/QCD, GR, computation, biology and full book claims |

## 5. Correction candidates (no source edits authorized)

These are source-review referrals, **not** accepted textual corrections or independent mathematical refutations. Their existence blocks treating this audit as an all-clear.

| Priority | Site | Minimum required decision |
|---|---|---|
| P0 | `papers/Structure.md:230`, `book/ch09-universality.md:194` | Distinguish continuous finite-dimensional matrix models from finite-cardinality carrier; require finite-valued cutoff *as a separate input* for the latter. Inspect `Structure.md:272,320` for propagation. **Corrected by #1341 (§5.1); Structure:270 is #1342 R1** |
| P0 | `papers/GR.md:665–669` | Remove/justify the bare "A1 implies finite ε/mode-unit S3" inference; it needs spatial/metric/mode-count premises, not set cardinality alone. **Corrected by #1341 (§5.1)** |
| — | `papers/Main.md:439–441` | Withdrawn as a candidate: see D09 |
| P1 | `papers/Medicine.md:35–39`, downstream biological predictions | Do not conflate conditional readback memory, measured P-indivisibility and verified natural biological realization of C1–C4. **A1 part corrected by #1341; Medicine:37 is #1342 R4** |
| P1 | `book/appendix-c-objections.md:128–132` | Keep "QFT infinity is an artifact" expressly conditional on a physically supported finite underlying model. **Corrected by #1341 (§5.1)** |
| — | `papers/Main.md:746–762` and downstream arrow / anti-BB claims | Not assessed in this pass and not counted as a candidate; deferred to A1-05 (#1332) |

### 5.1 Disposition after the first-pass review

The independent first-pass review ([#1340 review at `a64e2528`](https://github.com/amaybaum/incompleteness/pull/1340)) checked each candidate against CHANGEMAP-A1C-r6-min, #1313's minimum-change map (`verification/audits/foundations/a1-foundations-20261115/change-map/` on branch `research/a1-foundations-1169-20261115` at `c6e85058`). That map asked only whether a sentence presents finiteness as a fact about nature.

**Reference classification (§A.42 item 8).** The map is not on `main`, so its rulings below are **provenance only**. Each disposition rests on `main` text: D09 on Main:437, Main §2.3 and Lemma B.7.3 (`book/appendix-b-derivations.md:413`); D26 on GR:665 and :669; D34a on Main:137–139; D36 on Structure:224, :230 and :270; D37 on Structure:224; D39 on appendix-c:128 and :130.

| Candidate | #1313 ruling | Why this is a different defect, or none | Disposition |
|---|---|---|---|
| D09 Main:439–441 | M-30: "lemma in the finite-realization setting" | Same question; no defect | Withdrawn |
| D26 GR:669 | G-17: label kept | Internal-logic defect: A1 is a cardinality condition and does not imply S3's discreteness scale or its mode-count identification, which S3 itself calls an additional requirement | Corrected by #1341 |
| D34a Medicine:35 | not in the map | Recurrence-scale P-indivisibility stated for a common window | Corrected by #1341 |
| D34b Medicine:37 | not in the map | Empirical assertion, not A1 | #1342 R4 |
| D36 Structure:230 | T-07: label and class membership kept | Internal inconsistency with Structure:270's entry-discretization proviso | Corrected by #1341; Structure:270's description of lattice techniques is #1342 R1 |
| D37 ch09:194 | K-ch09-184/190/194: only :184 edited; :194 kept as a model/class/conditional statement | Different question: finite N leaves the matrix entries continuous, so the sentence was false as stated | Corrected by #1341, with FULL; #1342 R1 also bears on it |
| D39 appendix-c:130 | N-Kappc-C6 changed this paragraph's opening | Residue: the "artifact" clause stayed unconditional | Corrected by #1341, with FULL |

The review's further findings outside these candidates are tracked in #1342 (R1–R4).

Manuscript corrections must use the separately designated #1015/#1029 or other accountable issue with owner approval, review, generated mirror update and registry consistency. A1-09 does not edit the source or overwrite #1317.

## 6. UNCLASSIFIED blockers and completion decision

**Current A1-C01 verdict: INCOMPLETE — UNCLASSIFIED**, not "all A1 claims classified". Specifically:
- CENSUS-X1: resolved for claim coverage by batch 1 (§7).
- CENSUS-X2: the 232 other OIBridge modules, root import, six legacy Lean sources, and theorem declarations/imported hypotheses are not individually traced. Batch 2a (§8) is a triage inventory that flags 53 modules by type name and 5 by concrete finite types for the semantic check; it classifies none. Batch 2b (§9) classifies 16 of the flagged modules; no correction candidate.
- CENSUS-X3: 123 proof-census families, 133 coverage entries and 20 unattached items are parsed/inventoried but not independently linked one-by-one to source statements.
- CENSUS-X4: recursively maintained verification files, programmes, probes and archival or branch-only evidence remain unscanned as complete corpora. Published `.tex` mirrors are resolved for claim content by batch 1 (§7); PDFs are not stamped and are not checked.
- CENSUS-X5: all 12 primary papers and 29 accessible chapter/back-matter Markdown files received a textual search pass, but not full manual negative-proof semantic review of every theorem and implicit inheritance; zero lexical hits cannot discharge this.
- CENSUS-X6: resolved for the six first-pass candidates (§5.1): five corrected on `main` by #1341, D09 withdrawn, D34b moved to #1342. Further candidates found in later batches need their own review and owner authorization.

To close A1-C01, obtain full text/source parity for X1–X4; review and classify every site and theorem in X2–X5, including implicit dependencies; resolve or explicitly narrow X6 by separately approved evidence; and reconcile against the existing closure register with a reviewed exact-head audit. Only an independent final G2/owner sign-off on reviewed manuscript propagation can change the foundational completion label.

## 7. Coverage batch 1 — book mirror and generated artifacts (X1, part of X4)

**Pin:** `main` at `5ea8672f67f3fd44498c7aa65e2eac22ed14a315` (after #1341). Read from a local checkout.

**Recipe.** For each of the 29 Markdown files under `book/` other than the FULL file, list its non-blank lines; check each is present verbatim in `book/The-Incompleteness-of-Observation-FULL.md`; then list the FULL file's non-blank lines that occur in no chapter file. Run `python3 -I tools/staleness_check.py`.

**Result.**
- Every non-blank line of the 28 chapter and back-matter files occurs verbatim in FULL. `book/README.md` (65 non-blank lines) is the directory's landing page and is not mirrored.
- FULL has 31 non-blank lines found in no chapter file: the LaTeX title page, the table-of-contents commands, page breaks and the copyright page. None states a mathematical or physical claim.
- `staleness_check` reports 13 stamped artifacts matched (the 12 papers and FULL) and none unstamped: every generated `.tex` carries the `source-sha256` of its current Markdown source. PDFs carry no stamp and are not checked.
- `book/README.md`, read in full: lines 15, 17, 50, 82 and 100 summarize the finite-horizon equivalence (observable scope, **A**), the finite-model BQP hypothesis (**F**, conditional) and the appendix-C contents. No U candidate.

**Disposition.** X1 is resolved for claim coverage: FULL contains no claim line absent from the chapters, so the chapter classifications in §3 apply to FULL line for line. (§3 is pinned at `6eac91ee`, this check at `5ea8672f`; the only book change between them is #1341, which mirrored both of its book edits into FULL.) For published `.tex` mirrors (part of X4), the files are generated from stamped sources, so their claim content is that of the `.md` files; PDFs are outside this check. A line-level presence check does not test ordering or duplication; those are covered by the build and by `tools/duplicate_check.py`, not by this census.

## 8. Coverage batch 2a — Lean triage inventory (X2, first step)

**Pin:** `main` at `5ea8672f`. **This is a triage list, not a classification.** It narrows which Lean modules need a semantic check; it classifies none of them.

**Recipe.** For every `.lean` file under `verification/lean-mathlib/OIBridge/` and `verification/lean/` (247 files), collect the first type token after every `Fintype` or `Finite` that follows `[` or `:`. This covers instance arguments, binders such as `(_ : Fintype ι)`, `have … : Finite …` and `instance … : Fintype …`. Map each module to its families in `verification/lean-manuscript-census.json`. Flag a module when any such occurrence falls on a type whose name the corpus uses for a hidden, total, site, history, ancilla or carrier type: `H`, `ι`, `𝒮.ι`, `𝒮.V`, `Conf`, `Ω`, `X`, `Hist`, `Anc`, `W`, `C`. Separately, list modules that assert finiteness of a concrete type built from `Fin` or `ZMod` (`Fintype (Fin …` / `Finite ((Fin …`).

**Result.** 72 files contain no `Fintype`/`Finite` occurrence of these forms. 53 modules are flagged by type name. 5 modules assert finiteness of a concrete `Fin`/`ZMod` type: `A6Instantiation.lean`, `ExecSource.lean`, `HexLatticeGas.lean`, `KTokenMaxCone.lean`, `SubstratumInterfaceAudit.lean`.

**Limits of the heuristic.** Type names are not semantics. `ι` and `X` are often generic indices (a family index, a Kraus index, a matrix index) rather than a site set or carrier, so many flags will be cleared on reading. Finiteness of `V` (visible) is not flagged, because a finite visible alphabet is not a total-finiteness premise (§2.2). Finiteness that enters through concrete types, such as a configuration space `(Fin d → ZMod L) → …`, escapes the name filter; the concrete-type list above catches the explicit cases, and an implicit case can still be missed. All unflagged modules remain under X2 until checked.

| Module | Flagged finite types | Census families |
|---|---|---|
| `BarandesTuple.lean` | W, C, H | tuple instantiation and the Source-A branch test |
| `C3Necessity.lean` | Hist, H | equivalence chain and memory |
| `CandidateSelection.lean` | Anc | candidate selection: the representation does not determine the candidate intermediate |
| `CausalReadback.lean` | H | causal readback: the candidate forms and the divisibility no-go |
| `ClosureObstruction.lean` | ι, C | completion classification and the primitive-source chain |
| `CoherentLift.lean` | ι, W | coherent completions |
| `ContinuousExtension.lean` | X | the continuous-extension round (act 8, Track I layer 0 and Track B layers 1-2) |
| `DimensionalCountermodel.lean` | ι | instruments, dilation and assembly |
| `EquivalenceChain.lean` | H | equivalence chain and memory |
| `ExecSource.lean` | 𝒮.ι, 𝒮.V | executability source: the stated access and the layer flows |
| `FrozenSourcing.lean` | 𝒮.ι, 𝒮.V, ι | frozen substratum sourcing: the ceilings of the stated architecture |
| `FullFutureMemory.lean` | H | entire visible future as an exact finite-image trajectory random variable |
| `HexLatticeGas.lean` | ι | hydrodynamics round H-B: the reversible streaming-and-collision substratum |
| `HiddenMemory.lean` | Hist, H | equivalence chain and memory |
| `HydroClosureBridge.lean` | ι | hydrodynamics round H-E: H3 as a candidate bridge condition toward closure |
| `HydroSourceAudit.lean` | ι | hydrodynamics round H-A: source audit of the concrete wave representative |
| `ImplementationLocality.lean` | ι | completion classification and the primitive-source chain |
| `InstrumentDilation.lean` | ι | instruments, dilation and assembly |
| `InstrumentRealization.lean` | ι | instrument realization: one-instrument provenance |
| `KInfFoundations.lean` | ι | the corrected field-neutral vocabulary of the pre-quantum completion — proper effects, boundary states read in the body, relative strict convexity, group-flow drivability — with Lemma C and its converse, the semantic controls, Lemmas B and D and the finite-exposure bounds (round KINF-2, reconstruction) |
| `KTokenMaxCone.lean` | ι | conditional k-token cone theorem: products, cone closure, the k-fold maxCone bound and CNOT plus rotation/cyclic invariance give the PSD cone of the k-fold Pauli dictionary (round KTOKEN-MAXCONE-1, reconstruction) |
| `LiftSource.lean` | 𝒮.ι, 𝒮.V | lift source: the observer-level lift in the operational interface |
| `MeasuredReciprocity.lean` | H | P6 measured reciprocity |
| `MicroscopicReversibility.lean` | C, ι | completion classification and the primitive-source chain |
| `OperationalSourcing.lean` | Anc, H, W | operational sourcing at the Arc C boundary: what representation supplies, what the canonical witness supplies, and what the access verdict is stable against |
| `OrbitGeometryIsometries.lean` | W | the orbit-geometry isometries — the normalized realizable quotient, the finite family that acts on it, the internal description of its classes at the single carrier, a gated classification of its surjective isometries, and the prefix-constrained corollary (act 25, Track B) |
| `OrbitGeometrySelector.lean` | W | the orbit-geometry selector audit — the mixed-triple invariants, their metric, its controls, the twelve families against it and the rigidity cells, at act 12's and act 21's configurations (act 24, Track B) |
| `PhysicalC4Discharge.lean` | H, 𝒮.ι, 𝒮.V | physical C4 discharge: the realization clause as a rooted predicate, its controls, and the lattice residual |
| `PhysicalC4StorageReadback.lean` | H | physical C4 round 2: the storage-time reading of the store clause, and the two readings' relation |
| `PhysicalCharacterization.lean` | ι | completion classification and the primitive-source chain |
| `Purification.lean` | ι | instruments, dilation and assembly |
| `QuantumRepresentationT3.lean` | H | quantum representation: the all-time translation layer of the representation boundary |
| `RankGapTheory.lean` | ι | completion classification and the primitive-source chain |
| `Reciprocity.lean` | H | equivalence chain and memory |
| `RecurrenceHorizon.lean` | H | recurrence horizon: an identity return with an earlier overlap forbids divisibility |
| `ReferenceSufficiency.lean` | C | completion classification and the primitive-source chain |
| `RootedClassification.lean` | H | rooted classification: the finite-visible intrinsic characterization of the realizable class |
| `RootedClassificationAllTime.lean` | H | rooted classification: the finite-visible intrinsic characterization of the realizable class |
| `RootedRecurrenceBridge.lean` | H | exact microscopic iterate return to actual rooted identity and horizon indivisibility |
| `SemigroupTransfer.lean` | H | Substratum Lemma 24.1 — the semigroup-transfer step (reconstruction) |
| `Separability.lean` | ι | equivalence chain and memory |
| `ShellAssignment.lean` | H | Hamiltonian reconstruction |
| `StochasticInterface.lean` | 𝒮.ι, 𝒮.V | stochastic observer interface: the determination gap of the stated architecture |
| `SubstantiveCensus.lean` | ι | completion classification and the primitive-source chain |
| `SubstratumInterfaceAudit.lean` | 𝒮.ι, 𝒮.V, ι | substratum interface: sourced observer theory |
| `TrackBQfbBridge.lean` | W | the fixed-basis image of a single-time lift: trajectory laws determined by the visible law, stable under contractively scaled partial permutations, equal exactly when the visible laws are equal (act 45, Track B) |
| `TrajectoryMemory.lean` | C, H | actual finite-permutation trajectory bridge for hidden memory and C3 capacity |
| `TransposeBridge.lean` | H | transpose bridge: the two orientations of P-divisibility are the same predicate |
| `TurnpikeScopeTransfer.lean` | ι | Hamiltonian reconstruction |
| `TypedCompletion.lean` | X, ι, C | typed completion |
| `UhlmannUniqueness.lean` | ι | completion classification and the primitive-source chain |
| `WeylLift.lean` | ι | equivalence chain and memory |
| `WordTraceSufficiency.lean` | H | Substratum Lemma 24.1A — ST5 sufficiency, the word-trace kernel (reconstruction) |

**Next steps (batches 2b onward).** For each flagged module, and each module on the concrete-type list:
- read the declarations that carry the assumption;
- decide whether it is a finite visible or index type (no A1 relevance), a finite hidden or total carrier stated as a hypothesis (**F**, valid in its finite scope), or a finiteness used to support a claim stated more generally;
- check the manuscript anchors of its families against that scope.

Only the last case is a correction candidate.

## 9. Coverage batch 2b — recurrence, memory and rooted-family modules (X2)

**Pin:** `main` at `5ea8672f`. **Modules (16):** CausalReadback, C3Necessity, EquivalenceChain, FullFutureMemory, HiddenMemory, MeasuredReciprocity, PhysicalC4Discharge, PhysicalC4StorageReadback, QuantumRepresentationT3, Reciprocity, RecurrenceHorizon, RootedClassification, RootedClassificationAllTime, RootedRecurrenceBridge, TrajectoryMemory, TransposeBridge.

**Recipe.** For each module, locate the declarations or `variable` lines that carry the flagged finiteness. Map the module to its families in `verification/lean-manuscript-census.json`. For every manuscript anchor of those families, read the paragraph containing the anchor and decide whether the manuscript states the result within its finite scope.

**Lean side.** In all 16 modules the flagged finiteness is a finite hidden carrier `H` (with `Hist` or `C` alongside in C3Necessity, HiddenMemory and TrajectoryMemory), stated as an explicit typeclass hypothesis on `variable` lines or on the `RootedRealization` structure (CausalReadback.lean:178). Each such result is **F**, valid in its finite scope. Exceptions:
- CausalReadback's Section A (`c4r_implies_pIndivisible` and its companions) assumes only a finite visible alphabet; it is **A**.
- MeasuredReciprocity's general theorems assume a measurable carrier; `[Fintype H]` enters only at :276, for the finite counting specialization. They are **A**, with an **F** specialization.

**Manuscript side.**
- **Kernel-only families, no manuscript anchor (7 modules):** P6 measured reciprocity, causal readback, quantum representation T3, transpose bridge, finite-permutation trajectory bridge, entire visible future, microscopic iterate return. None of the seven module names occurs in `papers/*.md` or the book chapters. No manuscript claim rests on them through the registry.
- **Recurrence horizon, physical C4 discharge and storage readback, rooted classification:** the anchors are Main:137–145 and Main:642. Each paragraph states its finite setting: Main:137 "Because φ is a permutation of a finite set"; Main:141 "finite sets"; Main:145 derives periodicity within §2.3's finite-carrier setting; Main:642 "on a finite 𝒞_V", "one fixed finite substratum". **F**, correctly scoped.
- **Equivalence chain and memory:**
  - Main:95 and Main:552: the finite-horizon equivalence, finite scope stated. **A** at observable scope.
  - Main:312 and Main:314: the separability threshold for abelian Weyl subgroups on s qubits. A finite qubit register, not total finiteness; no A1 relevance.
  - Main:518 (`c3_necessity`, `card_hidden_ge_two_pow_Istar`): a lower bound on the hidden capacity |𝒞_H| ≥ 2^{I*}. It holds trivially for an infinite hidden carrier, so stating it without a finiteness qualifier makes no A1-dependent claim.
  - Main:612 (`capacity_floor`, M_t ≤ log₂|𝒞_H|): likewise vacuous for an infinite carrier; no A1-dependent claim.
  - SM:643 (`theorem_19`): states its hypothesis, "let the hidden prior be the counting measure", which presupposes a finite hidden carrier. **F**, correctly scoped; the measured generalization is kernel-only (`MeasuredReciprocity`).

**Result.** No correction candidate in this batch. All 16 modules are classified: the finite-carrier results are **F** and stated within their finite scope wherever a manuscript carries them, and the exceptions above are **A**.

**No new physics premise, scientific computation, proof, manuscript revision, Lean revision, evidence deletion, status promotion, or merge occurred in this audit.**
