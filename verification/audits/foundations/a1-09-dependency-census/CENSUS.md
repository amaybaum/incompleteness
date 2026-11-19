# A1-09 — A1 dependency census (A1-C01)

**Status: PARTIAL SOURCE AUDIT / UNCLASSIFIED COVERAGE — NOT A1-C01 COMPLETION OR G2 SIGN-OFF.** First pass independently reviewed (ACCEPT WITH CHANGES); the review's three required changes are applied in this revision by the coordinating session as writer (owner decision #1169 c.6922450446).
Scientific source claims remain governed by their own evidence and reviews. A1 is OPEN / UNADOPTED; physical source is NOT PASSED. This file changes no manuscript, Lean declaration, hypothesis, grade or completion-register entry.

The continuation begins at §12, written by Codex Foundations. It uses the November 19 source pin for new observations and keeps the earlier pins for the historical batches. The new findings are pending independent review.

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
- CENSUS-X2: §§8–11 cover the original 53 name-flagged modules and five concrete-type modules. §14 adds the root Lean file, all six legacy modules and selected omitted signatures, including a finite-orbit step under `S` and a finite-stage step with no `[Finite S]` binder. §19 reconciles the file changes since batch 2 and counts 163 bridge modules without a module-specific trace in this census. The §8 counts are historical.
- CENSUS-X3: §12 resolves the mechanical source crosswalk at the new pin (124 families, 132 coverage entries and 20 unattached items). §13 records source scopes for all 20 unattached items. Proof scope and dependencies outside the specific backward traces remain open.
- CENSUS-X4: §16 inventories the recursive verification and paper-supplement tree and runs a focused text search. Untraced evidence chains and archive or branch-only content are still **X**. Published `.tex` mirrors are resolved for claim content by batch 1 (§7). PDFs are not stamped and are not checked in this census.
- CENSUS-X5: the original textual pass covers 12 primary papers and 29 chapter/back-matter Markdown files. §15 adds backward traces for selected observer, GR and SM statements. §17 assigns a first-pass input scope to each of the 132 registered paper statements. §18 visits major downstream transfers in the six papers outside that register. Other implicit inheritance and untraced claims remain **X**.
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

**Lean side.** In all 16 modules the flagged finiteness is a finite hidden carrier `H` (with `Hist` alongside in C3Necessity and HiddenMemory), stated as an explicit typeclass hypothesis on `variable` lines, on theorem binders or on the `RootedRealization` structure (CausalReadback.lean:178). In RootedClassification.lean:116 the finiteness sits inside the existential that defines the realizable class (`∃ (H) (hH : Fintype H)`), so it is part of that class's definition rather than a hypothesis. TrajectoryMemory's flagged `C` is a generic type in `cmi_marg`/`cmiBits_marg` (:45–54), not a carrier. Each such result is **F**, valid in its finite scope. Exceptions:
- CausalReadback's Section A (`c4r_implies_pIndivisible` and its companions) assumes only a finite visible alphabet; it is **A**.
- MeasuredReciprocity's general theorems assume a measurable carrier; `[Fintype H]` enters only at :276, for the finite counting specialization. They are **A**, with an **F** specialization.

**Manuscript side.**
- **Kernel-only families, no manuscript anchor (7 modules):** P6 measured reciprocity, causal readback, quantum representation T3, transpose bridge, finite-permutation trajectory bridge, entire visible future, microscopic iterate return. None of the seven module names occurs in `papers/*.md` or the book chapters. No manuscript claim rests on them through the registry.
- **Recurrence horizon, physical C4 discharge and storage readback, rooted classification:** the anchors are Main:137–145 and Main:642. Each paragraph states its finite setting: Main:137 "Because φ is a permutation of a finite set"; Main:141 "finite sets"; Main:145 derives periodicity within §2.3's finite-carrier setting; Main:642 "on a finite 𝒞_V", "one fixed finite substratum". **F**, correctly scoped.
- **Equivalence chain and memory:**
  - Main:97 and Main:550–554: the finite-horizon equivalence; Main:550 "Fix a finite visible alphabet", Main:553 "finite reversible". **A** at observable scope.
  - Main:312 and Main:314: the separability threshold for abelian Weyl subgroups on s qubits. A finite qubit register, not total finiteness; no A1 relevance.
  - Main:508–518 (`c3_necessity`, `card_hidden_ge_two_pow_Istar`): "Let m = |𝒞_H|" and the corollary "requires m ≥ 2^{I*}" (with the conditional m ≳ 2^{K I₀}). m appears only as a lower bound, so the statement holds trivially for an infinite hidden carrier and makes no A1-dependent claim; "m = 2 < n = 3" is an example, not a premise.
  - Main:612 (`capacity_floor`, M_t ≤ log₂|𝒞_H|): likewise vacuous for an infinite carrier; no A1-dependent claim.
  - SM:641–643 (`theorem_19`): the statement (SM:641) assumes "let the hidden prior be the counting measure", which presupposes a finite hidden carrier, and the proof (SM:643) divides by |𝒞_H|. **F**, correctly scoped; the measured generalization is kernel-only (`MeasuredReciprocity`).
  - Further registry anchors of the same family: Main:524 constructs a finite 𝒞_H (**F**, stated); Main:556 is the (S⇒D) proof within class (D) (**F**, stated); Main:596 "every finite stochastic law" (**A**, observable scope); Main:616 "every deterministic completion … capacity at least M_t", where completions are finite faithful realizations in class (D) (Main:97), and the capacity bound is in any case vacuous for an infinite carrier; Main:782 is a list of verification code (no claim).
  - A citation outside the registry: Main:618 (`c3_necessity_via_hidden`) is a data-processing step and does not use finiteness; the kernel covers bijective realizations, and the manuscript states that the non-injective and staged cases are proved on paper. Main:97 also cites `pushforward_identity` and `distinguishability_floor` within class (D).
  - No book chapter cites an identifier from these 16 modules.

**Result.** No correction candidate in this batch. All 16 modules are classified: the finite-carrier results are **F** and stated within their finite scope wherever a manuscript carries them, and the exceptions above are **A**.

## 10. Coverage batch 2c — quantum completion, instrument and lift modules (X2)

**Pin:** `main` at `5ea8672f`. **Modules (25):** ClosureObstruction, CoherentLift, DimensionalCountermodel, InstrumentDilation, InstrumentRealization, KInfFoundations, KTokenMaxCone, MicroscopicReversibility, PhysicalCharacterization, Purification, RankGapTheory, ReferenceSufficiency, SubstantiveCensus, TypedCompletion, UhlmannUniqueness, WeylLift, Separability, ImplementationLocality, BarandesTuple, OperationalSourcing, CandidateSelection, TrackBQfbBridge, OrbitGeometryIsometries, OrbitGeometrySelector, ContinuousExtension.

**Recipe.** As for §9, with one addition. Besides the anchors in the registry, search the manuscripts for every declaration name defined in these modules, and read each citing paragraph.

**Lean side.** The finite types fall into four kinds.
1. **Finite family index.** No A1 relevance. This is `ι` as a Kraus, outcome or projector-family index, or as the index of a finite family of points or channels, in:
   - ClosureObstruction, DimensionalCountermodel, InstrumentDilation, InstrumentRealization, KInfFoundations, KTokenMaxCone, MicroscopicReversibility (:189), PhysicalCharacterization, Purification, RankGapTheory;
   - SubstantiveCensus, UhlmannUniqueness, WeylLift, Separability, ImplementationLocality, CoherentLift (:482) and TypedCompletion (:455, :480).
2. **Dimension of a finite quantum system, register or visible alphabet.** This is finiteness of an observable system or representation, not of the substratum, so it has no A1 relevance. It covers:
   - `C` as a span-lemma vector type in ClosureObstruction (:343), MicroscopicReversibility (:142) and ReferenceSufficiency (:101);
   - `C` as a register in TypedCompletion (:479), and `X`/`Y` in TypedCompletion;
   - `X` in ContinuousExtension, and `W` as a readout outcome set in CoherentLift;
   - `W` as the visible alphabet of a rooted family `Γ : ℕ → Matrix W W ℝ`, in TrackBQfbBridge, both OrbitGeometry modules, BarandesTuple (:282, :479, :487) and OperationalSourcing (:820);
   - `C` in BarandesTuple (:100), which is the visible alphabet ("The declaration is `C := V`", :377);
   - KTokenMaxCone's concrete `instance carrierFintype` (:63), a Pauli-label register.
3. **Hidden or ancilla carrier of a realization, stated as a hypothesis (F).** It covers:
   - `H` and `Anc` in OperationalSourcing (:209, :259 and following);
   - `H` in BarandesTuple (:416), the hidden carrier of `RootedRealization V H`;
   - `Anc` in CandidateSelection (:343);
   - the ancilla `A` (`[Fintype A]`) of the OrbitGeometry lifts on `W × A`, which the name filter does not flag.
4. **Finite configuration set of a realization, stated as a hypothesis (F).** In CoherentLift, `S` (:87, `[Fintype S]`) is the domain of `permMatrix (g : S ≃ S)`: the configuration set of the finite realization in the D ⇒ Q_fb step. The name filter does not flag it either.

**Manuscript side.** None of the kernel-only or verification-only families (instruments, dilation and assembly; instrument realization; the K∞ vocabulary; the k-token cone; tuple instantiation; candidate selection; both orbit-geometry families; the continuous-extension round) is named in `papers/*.md`, `book/ch*.md` or `book/appendix*.md`. Of their declarations, only `countermodel` (DimensionalCountermodel.lean:621) is cited, at GR:216. Every citing paragraph read:
- **Coherent completions.** GR:188 is the heading; GR:190–192 give "an explicit finite carrier" and "the same finite visible dimension", citing `shell_representation_from_comb`, `comb_mixture_of_shell_representation` and `uniform_overlap_obstruction`. The setting is a finite class (D)/Q_fb realization (Main:554), so CoherentLift's kind-4 `S` is used within its finite scope. **F**, stated.
- **Completion classification and the primitive-source chain.**
  - GR:214 is the theorem statement: "For every nonempty finite visible system".
  - GR:216 cites the minimality witnesses `five_way_minimality` and `countermodel`, which are finite qubit countermodels; a finite witness suffices.
  - GR:230, 242, 244, 246 and 252–254 ("holds on every nonempty finite carrier") concern finite quantum systems, at observable scope.
  - Main:356 says "every fixed finite representative", and states the characterization, citing `physical_of_exactAll`, "for every nonempty finite visible system".
  - Main:566 "What no fixed finite carrier can do" is scoped.
  - The substratum-source sentence in Main:592 and its mirror FULL:500 reads "the concrete OI substratum, in its finite model (ledger item (ii))", and GR:256 states the GR counterpart as a condition: "The concrete OI substratum under A1 — finite states and bijective microscopic dynamics" (A1 is defined at GR:669). GR:260 adds that the controllability resource "is not entailed by A1–A6". **F**, stated.
  - The same phrases recur at ch01:165, ch19:126 and FULL:5271, with the same scope.
- **Typed completion (GR:272):** a classification "between any two nonempty finite carriers", meaning quantum registers. Observable scope.
- **Operational sourcing and the fixed-basis image of a single-time lift.** Main:648, ch01:187 and ch19:285 (mirrored at FULL:522 and FULL:5430) concern lifts and ancillas of finite visible laws. Main:554 defines Q_fb as "finite-dimensional unitary systems", so a tensor-factor ancilla of a Q_fb datum is finite by definition, even where the sentence ("an ancilla attached as a tensor factor … leaves the rooted family unchanged (kernel: `padData_rooted`)") does not say "finite". Finite-horizon representation layer; no total-finiteness claim.
- **Main:314** (WeylLift, Separability) is covered in §9.

**Result.** No correction candidate in this batch. All 25 modules are classified: kinds 1 and 2 carry no A1 relevance, and kinds 3 and 4 are **F**, stated or used within their finite scope.

## 11. Coverage batch 2d — substratum-interface, hydrodynamics and Hamiltonian modules (X2)

**Pin:** `main` at `5ea8672f`. **Modules (13):** ExecSource, FrozenSourcing, LiftSource, StochasticInterface, SubstratumInterfaceAudit, HexLatticeGas, HydroClosureBridge, HydroSourceAudit, ShellAssignment, TurnpikeScopeTransfer, SemigroupTransfer, WordTraceSufficiency, A6Instantiation. A6Instantiation is the last module on the §8 concrete-type list; the other four are classified in §10 (KTokenMaxCone) and here.

**Recipe.** As for §10: the `Fintype`/`Finite` lines of these modules, read and grouped by kind (the lists below give representative lines of each kind, not every line), the registry families, and every manuscript citation of a declaration name defined in these modules.

**Lean side.** This group works directly with the substratum, and its finiteness is mostly substratum finiteness stated as a hypothesis (**F**):
- **Finite sites and alphabet:** `[Fintype 𝒮.ι] [Fintype 𝒮.V]` on a `Substratum`, in ExecSource (:125), FrozenSourcing (:84, :277; and on a `Rule ι V` at :296, :303), LiftSource (:196, :296), StochasticInterface (:111, :182) and SubstratumInterfaceAudit (:115, `a3_of_fintype`; :766; and on a `Rule ι V` at :781). SubstratumInterfaceAudit defines A1 itself (`def A1 : Prop := Finite 𝒮.Conf`, :84) and proves `a1_of_finite`, finite sites and alphabet ⇒ A1 (:109); `obs_a1` (:786) applies it. That is one direction only: finite sites and alphabet is a sufficient condition for A1, at least as strong as A1, and no converse is proved there.
- **Finite configuration sets** `S` of a reversible realization: ExecSource (:47, :84, :179), LiftSource (:65, :88), StochasticInterface (:27, :140), SubstratumInterfaceAudit (:238, :501, which are generic matrix carriers; see the next bullet).
- **Finite operational-theory carriers** `A`, the carrier of a `FiniteOperationalTheory A`: FrozenSourcing (:59, :94, :260), instantiated at `𝒮.Conf` (:84) and at `ι → V × V` (:296, :303); SubstratumInterfaceAudit (:577, :603), instantiated at `𝒮.Conf` (:770). **F** where instantiated at a substratum's configuration space; otherwise a generic finite carrier, at observable scope as in §10.
- **Concrete finite tori:** ExecSource (:161, `Fin d → ZMod L`), HexLatticeGas (:313), SubstratumInterfaceAudit (:184–186, `waveSubstratum_A1`, `Finite ((Fin d → ZMod L) → …)`), and A6Instantiation (:279, :517). A6Instantiation:499 records that A1 *fails* for the complex lift (`Fin 6 → ℂ` is infinite).
- **Finite hidden carriers `H`:** ShellAssignment (:61), SemigroupTransfer (:78), WordTraceSufficiency (:85).
- **Finite family or matrix indices**, with no A1 relevance: FrozenSourcing (`m`, `n`), LiftSource `O` (:71), HexLatticeGas `ι` (:364), HydroClosureBridge `ι`, HydroSourceAudit `ι` and `M`, TurnpikeScopeTransfer `ι`, `σ` and `κ` (integer rulers and rational points), and SemigroupTransfer `D`.

**Manuscript side.**
- **Kernel-only families:** frozen sourcing, stochastic interface, substratum interface audit, the three hydrodynamics rounds and A6 instantiation. No declaration from these modules is cited by name in `papers/*.md`, `book/ch*.md` or `book/appendix*.md`.
- **Semigroup transfer and word-trace sufficiency** (SemigroupTransfer, WordTraceSufficiency). Substratum:276, :282 and :284 name six declarations, without backticks: `ST3_pairC`, `pairC_wordTraces` and `trace_wordEval_hiddenConjugate` from SemigroupTransfer; `WT2gen_oneSided`, `WT3_spanning_iff` and `blockSpanning_of_wordTracesEqual` from WordTraceSufficiency.
  - Proposition 24.2 (Substratum:280) opens "Let $V,H$ be finite index sets". **F**, stated.
  - Substratum:276 states that equal visible channels "does not determine the bijection up to hidden unitary". This is a non-implication, shown by a finite counterexample ($|V|=2$, $|H|=3$). A counterexample in the finite class is one in any class that contains it, so the non-implication needs no A1.
  - Separate from A1: `verification/lean-manuscript-census.json` records both families with `"manuscript": []`, which these citations contradict. This is a registry finding under §A.35, to be routed separately.
- **Executability source and lift source** (ExecSource, LiftSource):
  - **Main:592.** The negative results, `obs_not_layerFlowExecutable` and `coherentLiftClass_eq_substratumClass`, are stated in the paragraph's last sentence. That sentence comes after the typed-form sentence and after the sentence on the infinite-region quasilocal completion. Their finite scope comes from the sentence before them ("not a consequence of the finite states with the bijective dynamics"; "exact finite endomorphic operational quantum mechanics"). The same sentence is carried by ch01:165, ch19:126, FULL:500 and FULL:5271. **F**, stated by context.
  - **GR:266–268.** GR:266 cites both declarations, together with `exists_nonMonomial_of_layerFlowExecutable`, `waveSubstratum_not_layerFlowExecutable_swap`, `avail_one_not_layerFlowExecutable`, `correlationExtension_preservesDiag`, `reversibleExtension_conj_monomial` and `stochasticChannel_kraus_monomial`. It sits in the "Layer-flow form" paragraph (GR:262–268), a bold-labelled paragraph of GR §3.3 that follows the "Substratum-source form" paragraph (GR:256, "under A1 — finite states and bijective microscopic dynamics"). The scope is in the paragraph itself: GR:266 says "not a consequence of the finite states with the bijective read-write dynamics", and GR:262/264 say "finite endomorphic". **F**, stated.
  - Why the GR:268 display ("stated substratum dynamics with observer access ⇏ one nontrivial layer flow executable") is not a correction candidate:
    - The universal prose claim is proved only where it can be stated: `obsTheory : FiniteOperationalTheory 𝒮.Conf` is defined only under `[Fintype 𝒮.ι] [Fintype 𝒮.V]` (SubstratumInterfaceAudit:766–770).
    - The display is a non-implication. The finite wave substratum (`waveSubstratum_not_layerFlowExecutable_swap`, ExecSource:166) is a countermodel. It also satisfies any weaker premise set that omits A1, so the non-implication holds when read without A1.
  - **Optional precision (not a correction candidate):** naming A1 beside the negative results would make the class explicit, as the claim/evidence rule on negative results asks. Main:592 and its four mirrors are the stronger place for it, because the infinite-region sentence sits between the finite-scope sentence and the negative results; the GR:268 display is a second, weaker place.
- **Hamiltonian reconstruction** (ShellAssignment, TurnpikeScopeTransfer):
  - GR:174–184 and appendix-b:443 (with FULL:6194) concern reconstructing a finite-dimensional visible Hamiltonian (GR:174: dimension $m\ge3$), conditional on H-BG or (G4). This is observable scope. Main:242 cites PairIdentification, not these modules, so it is family context only.
  - The citations at GR:178, appendix-b:439 (`real_to_integer_surrogate`) and appendix-b:445 (`BGIntegerClassification`, `twoBranch_of_BGClassification`), mirrored at FULL:6190 and FULL:6196, concern integer rulers, a finite index.
  - `ShellRepresentationConsistency` (GR:190, :202) is a stated premise.
  - ShellAssignment's finite shell is the counting route of P7. It is scoped by GR:58, whose H-count carries A1 explicitly ("that the total system is finite (A1)", through #1313), and by GR:186 ("exact finite-bath counting").

**Adjacent finding, outside the A1 scope (route separately).** Main:592 and its four mirrors say the lift "derives neither a non-monomial admissible operator nor the layer flow". They drop GR:266's qualifier, "whether every realization of those channels is configuration-level is not decided"; the LiftSource header (:41–43) likewise leaves open whether every Kraus realization is configuration-level. This reads as a negative result for a broader class than the one ruled out, on the realization axis rather than the finiteness axis, and a cross-document difference under §A.25.

**Result.** No correction candidate in this batch. One optional precision is noted, at Main:592 with its mirrors and at GR:268. All 13 modules are classified, and the module lists of §9–§11 equal §8's 53 flagged modules plus A6Instantiation, with all five concrete-type modules covered. **This completes the Lean triage list of §8.** It does not complete X2: 175 of the 247 files contain a `Fintype`/`Finite` occurrence, and the 121 files, other than A6Instantiation, whose occurrences are only on unflagged names were not read. §10 and §11 found finite carriers under unflagged names (`S`, `A`), so the name filter can miss a carrier. The 72 files with no occurrence (the six legacy modules among them) also remain outside this check.

**No new physics premise, scientific computation, proof, manuscript revision, Lean revision, evidence deletion, status promotion, or merge occurred in this audit.**

## 12. Registry-to-source crosswalk (X3)

**Source pin:** `baeb7723743e99b137ae3d0a1694e99ff97e2a73`. `Main:137` below means line 137 of `papers/Main.md` at this pin. Lean basenames refer to `verification/lean-mathlib/OIBridge/` unless stated otherwise. The accountable Issue is #1334. Its activation record covers this source-only continuation; the earlier, merged #1340 is provenance for §§1–11. The Main-only audit lives in `verification/audits/foundations/a1-main-roots-20261118/AUDIT.md`. This checkpoint uses its distinctions for the Main evidence and does not redo its research or take over P8, P12(b), or the new recurrence proof.

**Goal.** Establish where a reader must look to check whether a manuscript statement quietly depends on a finite total carrier. A registry match supplies a pointer. It cannot establish a mathematical implication between the Lean and manuscript statements.

From a source checkout at the pin, run the continuation's `registry_index.py` with that checkout as its positional argument. The script reads current canonical statement IDs and fingerprints from `tools/proof_census.py`. It emits their live lines alongside the ledger lines, all literal matches for each whitespace-normalized family anchor, named Lean declaration lines and named evidence-string matches, and the paths of unattached checkers. Run `tools/lean_manuscript_census.py` and `tools/coverage_check.py` in the source checkout to reproduce the existing integrity checks. The index scans for plain manuscript mentions of recognizable, unique OIBridge declaration names in families with no anchor. This last pass misses some names and cannot distinguish mathematical citations from incidental prose without reading the matches.

| Surface | Verified locator result at the pin | Inference still required |
|---|---|---|
| Lean family registry | All **124** families indexed. All **107** distinct family anchors found across **132** textual matches. Sixteen anchors have more than one match. All 17 named supersession targets resolve to a tracked OIBridge module by declaration name. | Read the intended paragraphs and actual hypotheses. A repeated phrase may be used at more than one scope. Forty-character source pins and live locators govern these traces. |
| Coverage ledger | All **132** canonical IDs match the ledger one-to-one with fresh fingerprints. **95** stored line numbers differ from their current lines. For example, `GR:T-a.6` points to 797 in the ledger and starts at 779. | Use the live source line in a dependency trace. The old line metadata gives no evidence of a changed theorem. |
| Attached checks | **76** Lean and **93** probe mappings across **106** files exist. All **117** explicit or named declaration pointers resolve to a single textual declaration within their recorded file. All **63** named probe mappings have their evidence string. The other **30** are section mappings. | Verify what the theorem uses and what model a probe tests. No execution or change of coverage grades occurred. |
| Unattached checks | All **20** paths exist and each has a recorded scope. | A scope description is not a verified theorem dependency or a link to a live manuscript claim. |

### 12.1 Citations absent from family anchors

The no-anchor scan yielded 23 textual mentions in four families. Reading those mentions identifies the following three genuine manuscript uses. The `instantiates` matches are ordinary prose, including the tuple discussion in Main:532. The bare `countermodel` in GR:217 is a real citation to the five-witness list; matches in Main:36,730 use the ordinary noun.

| Family and source declaration | Consumer and earliest use | A1 disposition |
|---|---|---|
| Semigroup transfer (`SemigroupTransfer.lean:78,468,749,792`) | Substratum:276,282,284 uses `ST3_pairC`, `pairC_wordTraces` and hidden-conjugacy trace invariance. The equality countermodel evaluates finite normalized hidden traces and uses two explicit finite matrices. | **F** for those finite matrix calculations. The claimed non-implication extends to any broader class containing both witnesses. This confirms the prior registry finding in §11. |
| Word-trace sufficiency (`WordTraceSufficiency.lean:85,563,606,625`) | Substratum:280,282 invokes the word-trace sufficiency implication, transfer of spanning, and its converse. Fixed finite hidden index (H) enters at normalized or unnormalized matrix traces and the span of the finite matrix algebra, as appropriate to the cited result. | **F** at the stated finite-index, full-span scope. A finite hidden index of the two compared realizations does not assert a finite universe. This confirms §11. |
| Instruments, dilation and assembly (`OperationalAssembly.lean:594,658,665`, `KrausSoundness.lean:197`, `DimensionalCountermodel.lean:621`) | GR:213,217 and Main:566 explicitly use the operational theory, local Lüders readout, composite unitary control and qubit witnesses. The first size requirement is a finite visible matrix index; each ancilla level attaches a finite register, with a variable level. GR:217 draws its five-witness inference through `RankGapTheory.lean:702`. | **A** with respect to total physical finiteness at the declared finite-visible, complex-matrix scope. The absent anchors are a registry finding under §A.35. The finite operational carrier is not identified with a physical total carrier by these uses. |

### 12.2 Scope checks where an identical pointer could be misread

| Source row | Backward trace and disposition |
|---|---|
| Main:135–143, `pIndivisible_of_rooted_identity_return_of_overlap` | Main:135–137 reaches a common period via the order of a permutation of a finite configuration set (**F** as stated). Main:141–143 then uses a strictly overlapping pair and an identity return. The contraction of TV under a stochastic intermediate only needs a visible stochastic family with the return and the overlap, as stated in `RecurrenceHorizon.lean:43,98–130` (**A** conditional). The cited rooted wrapper at :134–156 has a finite hidden realization. The return of an arbitrary infinite hidden system still requires its own argument. |
| SM:641–643, `SM:T-19` | The source counts full hidden fibres and divides by their cardinality. `Reciprocity.lean:40,129` makes the finite-hidden count explicit (**F**). `MeasuredReciprocity.lean:198–271` handles the separate measurable route from a supplied invariant law and reversing symmetry (**A** conditional), with its own requirements on the observed roots. The finite counting result is the ledger's argument. The existence of a measured result does not supply the physical law. |
| Main:97,554,596, `finite_horizon_equivalence` | The appearances cite the same per-window construction in distinct settings. Main:550–556 and `Equivalence.lean:365–462` use a finite visible alphabet, a finite observation horizon and a finite *constructed* response/trajectory space. The claim about those record laws is **A**. A physical transfer or extension to one fixed finite all-time representative does not follow from the finite-horizon proof, as Main:642 and the separate Main roots audit distinguish. |

**Disposition.** The source pointers can now be regenerated at the pinned snapshot. The instrument-family omission is a third confirmed case beyond the two recorded in §11. The ledger line drift and empty anchor lists are documentary findings for the registry owners. Proof-by-proof and undeclared dependencies remain under X2–X5. The other 94 no-anchor families still need semantic tracing of their use or an explicit negative scope.

## 13. Unattached coverage records at the November 19 pin

Each of the 20 paths from `verification/coverage/LEDGER.json` was read for its stated model and the use of finiteness in the named result. The following are source dispositions of the recorded evidence. Probe results were inspected as code and are not rerun here. Lean files use the directories of §12 or `verification/lean/` for the `OI_*` files. Probe basenames use `papers/oi_lattice_code/foundations/`.

| Recorded evidence | First finite object or genuine restriction | Disposition at the claimed scope |
|---|---|---|
| `OI_Structural_Chain.lean:90–127` | Invertible comparison weights and a finite path of balanced edges. The path argument concerns ratios, and the connectedness needed to tie all states together is additional. | **A** for the proportionality implication on supplied paths. GR:62–76 still supplies H-balance, and normalization of a Gibbs law needs its own input. |
| `OI_Regulator_Symmetry.lean:46–251` | Finite symmetry groups of signed coordinate permutations, of orders 384 and 96. Character sums and the displayed invariant forms use only that representation. | **A** with respect to total cardinality. The finite-group calculation has no total physical carrier input. |
| `CombRealization.lean:79–116,146–189` | Repetition of the orbit in a finite reversible realization precedes the two saturated-class lower bounds. | **F** for the b76B comb and finite realizing machine. See §14. |
| `primitive_probes.py:2–17` | Explicit small reversible models with a common uniform prior and short windows. The capacity estimate uses the declared hidden alphabet. | **F** probe scope. The logical implication for general finite-window records uses the separate Main proof. |
| `review3_probes.py:2–19` | Concrete diagonal, fair-coin and two-bit examples. The construction producing the finite fair-coin record is per horizon. | **F** witnesses with the stated horizons. A universal assertion over any class containing a witness is falsified by that witness. |
| `review4_probes.py:2–16` | Explicit finite record laws distinguish C4 from P-indivisibility and allow a later overlap when the first rooted step is a permutation. | **F** witnesses, with the same counterexample scope as above. |
| `coherence_boundary_probes.py:4–29` | The b76B finite operational architecture and an explicitly supplied ancillary coherent lift. | **F** comparisons of the declared constructions. The passive-law constraints do not supply the coherent lift. |
| `native_group_probes.py:4–25` | Alternative completions of one partial finite dynamics change the order of the completed permutation. Genuine paths are traced on that construction. | **F** counterexamples to dependence on genuine b76B data alone. An arbitrary infinite system's operation group is open here. |
| `finite_horizon_probes.py:4–24,105–139` | The bounded progress counter at each `K` in the response-table machine. | **F** for this family. The lack of genuine returning paths applies to the declared progress rule. |
| `recurrence_entropy_probes.py:12–41,228–254` | The ring/stack examples use fixed buffers. The general ceiling uses the entropy of a fixed finite initial carrier and no fresh randomness. | **F** for the uniform finite entropy bound on the entire record. An infinite carrier would require a separate entropy or access bound. |
| `comb_dimension_probes.py:4–26,150–180,238–275` | A support count on fixed-horizon deterministic strategies in the b76B comb. Cardinality of a constructed machine and intrinsic strategy count differ. | **A** for the finite-horizon table's strategy bound with respect to total physical finiteness. The probes compare finite witnesses. |
| `comb_realization_probes.py:4–22` | Exact lower and upper bounds for a finite reversible machine at horizon two. Lower bound uses the finite-return obstruction above. | **F**. The explicit ten states and the bound do not assert any actual carrier cardinality. |
| `source_lift_probes.py:4–21` | Finite-dimensional fixed-basis phase family and a supplied coherent operation that distinguishes it. | **F** evidence for that model-level non-identification, which also gives a counterexample in any class containing it. |
| `induced_source_probes.py:4–23` | Finite lattice test for link responses, with the induced link a difference of site values. | **F** evidence for the concrete lattice. The cancellation of a pure-difference plaquette is local algebra, as proved separately by the gauge certificates in §14. |
| `gauge_support_probes.py:4–23` | A pair of extensions agree on the induced Abelian links but have different second derivatives when independent links are allowed. The witness uses finite lattice data. | **F** evidence for the source-extension ambiguity. There is no sourced independent-link process in this test. |
| `bargmann_bridge_probes.py:4–19` | The finite b76B operational construction and external coherent states used for its comparison. | **F** evidence for the stated construction's reach. It cannot exclude every larger native operation class. |
| `comb_reachability_probes.py:4–25,305–331` | Fixed action menu and horizon for the hulls. The shift identity uses invariance of the starting law under each declared permutation, realized by uniform counting on the finite machine. | **F** for the tested hulls and uniform finite models. The first logical input to the shift identity is invariance of the chosen law. |
| `IdempotentTrace.lean:119–144` | The trace/restriction formula uses an idempotent in finite-dimensional linear algebra. The proof has a local finite vector-space dimension as input. | **A** with respect to total configuration cardinality. |
| `OIBridge.lean:827–874` | The obsolete face-link identification is checked by a concrete finite group and two six-dimensional representations. | **A** finite-representation counterexample. The accepted cubic link result uses the actual signed links, as explained in §14. |
| `HiddenMemory.lean:66–114,132–185` | The kernel pushforward works on a supplied finite joint law of histories, present and hidden records. The per-horizon existence part of the Main argument uses a constructed realization. | **F** for the kernel's joint-law form. The paper's faithful-realization comparison remains **A** at finite-record scope, with the kernel delta identified in the Main roots audit. |

## 14. Additional Lean dependency traces

There are 242 named bridge modules, the root `verification/lean-mathlib/OIBridge.lean`, and six legacy files at this pin. The root includes substantive proofs after its import list. The following table covers the root and each legacy source's mathematical role. None is a new kernel certification.

| Source | Source scope relevant to A1 |
|---|---|
| `OIBridge.lean:315–574,613–895` | Counting fixed points of a finite cubic group on a six-element local representation, then applying the averaging identity. The two-subset action and signed-link action are distinguished by `char_two_subset_ne_link` at :840. SM:374–380 uses the actual six signed directions, with the physical single-copy conclusion conditional on H-link. The group and representation size are **A** with respect to total physical cardinality. |
| `OI_Gauge_Certificates.lean:135–177,179–238,277–457` | Telescoping and central-sign collapse use the homomorphism and odd torsion assumptions. The 24 elements counted are a cubic rotation group. The proof explains the local layer used by SM's pure-gradient and representation arguments, at their stated algebraic scope (**A**). |
| `OI_Regulator_Symmetry.lean:46–251` | Finite coordinate groups and explicit invariant quadratic forms, as in §13. The certificate does not supply a choice of physical regulator or a symmetry-restoration mechanism (**A** at the algebraic scope). |
| `OI_Staggered_Relations.lean:123–146,327–461` | Generator relations and list induction over the number of axes. The index counts terms in the factorization. The stated ring identities supporting SM:286 require neither finitely many sites nor one total configuration space (**A**). |
| `OI_Structural_Chain.lean:42–127,188–276` | Invertible path weights and a finite local rotation group, as in §13. A normalized state on a physical carrier is separate from the relative-weight identity (**A**). |
| `OI_Structural_Core.lean:152–303,308–397,401–484,489–530` | Operator/ring identities for the projected recurrence, staggered square, chirality and quadratic Ward coefficient. An idempotent and the indicated algebraic relations suffice. SM:242's finite-configuration model is a specialization. Neither the ring proof nor a smoke instance selects the physical observer projection (**A**). |
| `OI_Time_Reversal.lean:99–145,171–185` | The second-order time-reversal identity uses an additive commutative group and a fixed stencil, on `Int` spatial/time indices as written. SM:625's identity and the transport countercontrol have no total carrier premise (**A**). |

### 14.1 Carrier names and definitions missed by the earlier filter

| Declaration and consumer | First use and disposition |
|---|---|
| `CombRealization.lean:79–116`, unattached lower bound | `Finite.exists_ne_map_eq_of_infinite` forces a collision among the iterates in `S`. Injectivity transports it to a return to the starting state. The saturated-class argument contradicts this return after propagating the readout condition to all positive iterates. The existing proof therefore uses exact return, supplied by `Finite S`. The bound is **F** and the ledger keeps it as research evidence. The declaration names and b76B lower bound do not occur in the primary paper or chapter statements checked by the source index. |
| `CanonicalMeasure.lean:54,63,178,276`, Main:54–60 | The representative carrier is `S`. Its finite orbit normalizes the cycle measure. Maximizing over probability assignments on the whole finite carrier selects the uniform global law. The proof does not recover a physically chosen measure from bare invariance (**F** for the counted representative). |
| `ObservabilityQuotient.lean:73,281,303–322` and `PassiveQuotient.lean:95,222,383,534–597` | The fixed-window quotient uses finitely many readouts on a finite matrix carrier. The all-time algebra statement explicitly collapses the horizon to the order of that finite permutation. The passive trajectory comparison uses the induced pushforward of finite state weights, including in decoupled extensions. These results are **F** as stated. Substratum:331–342 presents a distinct paper proof at a fixed finite-permutation scope, also using finite order for backward invariance. |
| `ControlledQuotient.lean:51,185–252` and `CycleFibreHull.lean:68–86,169–235,371–411` | The controlled quotient uses finite carrier matrices and all action words. The cycle readout hull uses finite orbit counts and normalizes them on `S`. These are **F** statements about the declared research models. |
| `CompositionOrder.lean:100–116,149–165,348–382` | A finite set of operations gives repeating powers under multiplication closure. A different proof needs a preserved finite `Finset` sufficient to determine the map on the chart body. The latter finiteness is in the preserved determining data, not a typeclass on the body or a total configuration set. Both are **A** with respect to A1 under their own contracts. |
| `RecordFibreIdentification.lean:18–89`, Substratum:348–357 | The set-theoretic implication uses a nonempty preparation-supported fibre and injectivity of the actual iterate. The current hidden-state clause also uses the final visible readout and the product carrier (**A**). The kernel leaves the probability-support step and the separate `N-1` cutoff to the paper. The paper's cutoff uses bounded strict partition refinement of a finite carrier (**F**). |
| `ManuscriptAxioms.lean:76–112`, `A1Realized` | This predicate is an operational image on the already typed two-state carrier. The proof fixes `Fin 2` before testing further predicates. This is **F** as a witness and does not discharge the physical A1 premise of Theorem 23. |

The combination of `CombRealization` and `CompositionOrder` is a pair of controls for the search recipe. The same surface cue (a finite return) serves a whole model carrier in one proof and finite determining data inside a larger body in the other. Skipping either a name-based or a binder-based search would miss a relevant distinction. Modules with untraced uses through imported definitions remain **X**.

### 14.2 Source inventory without a type-name filter

Run `registry_index.py --lean <pinned-checkout>` for the Lean source inventory. It gives direct imports, candidate declaration start lines and line numbers for finite-type, finite-set/count and return/order cues. The lexical index sees **249** files and **10,169** candidate declaration starts. The root directly names 236 distinct bridge imports. Following source import edges reaches all 242 bridge modules, including the six indirectly imported modules `BridgeConverge`, `BridgeDictionary`, `EqvK2Block`, `EqvK2Converse`, `EqvK2Generation` and `EqvK2Schema`. Import reachability does not show which definitions a theorem uses.

Eight files have none of these cues. Five are covered in the legacy table above. The other three are small algebraic controls:

- `ChiralCenterRecovery.lean:87–129,134–177,245–271` uses a ring, a parity map on arbitrary `X` and a no-two-torsion condition. The entries are functions on `X × X` and require no finite carrier. The local identity underlying SM:302 is **A** in this form.
- `GaugeDimension.lean:37–54` uses dimensional balance for the declared field-strength weight. The integer (d) counts spatial dimensions, and the algebraic implication for SM:603 is **A** with respect to A1.
- `GradientLinkFlatness.lean:23–49` uses an arbitrary additive commutative group. The plaquette telescope and second-order update inverse use its algebraic operations and a supplied (F) (**A**). This covers the local identities and leaves their application to the native package separate.

This read of the zero-cue set is a control on the indexing method. `--lean` also records the cue locations in the other files for subsequent proof-level comparison. Its declaration count is a textual match count, without elaborated binders or guaranteed coverage of every Lean declaration form.

## 15. Additional manuscript backward traces

These entries use the §12 pin. They add to the earlier rows and draw on the existing P12(b), P7 and Main roots records where they already supply the relevant source chain.

| Statement and proof | First use of finiteness and actual scope |
|---|---|
| GR:112–132, GR Appendix B:873–905 (boundary and deep-sector comparison) | The finite uniform argument cancels the multiplicity of identical deep-sector terms at :122. Appendix B uses a finite dependency patch and the product prior of a uniform finite boundary law with a normalized arbitrary deep measure. The integral of the deep factor is one. This is an existing **A** route for the exact no-H-BD part over the declared finite horizon. The H-BD correction at :124 uses the fraction of all deep configurations and injective transport of surviving trajectories. It remains **F** on that counting proof. |
| GR:719,729–751 (A.1–A.3, nested descriptions) | A.1 is the finite double sum with a product normalization. A.2 composes partial traces on the same dilation and preparation. A.3 adds the finite visible spectral reconstruction hypotheses, including H-BG, or exact all-time unitary equality. **F** for the given finite representatives. Matching marginal channels alone supplies neither a common dilation for arbitrary instruments nor a unique physical Hamiltonian in the presence of the reflection branch. |
| GR:753–755 (A.4) and book ch07:42–59 | Equality across horizons substitutes the one-scale calibration at each horizon. The first total counting step is GR:58, H-count for the finite conserved shell. The detected slope, same transition, shared \(\epsilon\) and \(\sigma\), and the horizon conditions are needed separately. **F** for the printed calibration. P7 boundary-count replaces the finite total count only under its own conditional inputs. |
| GR:759–763,779–785,793–795 (A.5–A.7) | A.5 first uses finite injective-surjective equivalence on the frozen fibre before the block-diagonal mixture. Full bijectivity preserving every (d) itself also supplies fibrewise surjectivity. The channel claim is scoped to the appendix's finite sectors. A.6 uses the finite von Neumann entropy setup, subadditivity and unitarity. It leaves the generalized second law's entropy identifications and monotonicity open. A.7 sums the weight of the exceptional configurations under the supplied near-freezing bound. **F** as printed for these sectors, with **W** for the identified physical horizon claims and timescales. |
| GR:789–841, book ch07:126–149 and ch18:138–140 (A.8–A.9, cycle-averaged Page curve) | The finite subsystem (B\cup R) is treated as closed under H-decouple, with fixed dimensions for each stage. Counting cycle lengths relative to the full finite product shell is the first global count for **that subsystem**. The proof also needs H-scramble to transfer Haar concentration to the configuration count. The paper and book state that it fails for aligned definite configurations and leave the proper-shell and moving-cut claims open. **F** for the scoped conditional implication. **W** for native evaporation. This classifies the finite-subsystem Page route in the previously open U1 family in the finiteness-classes audit. The other U1 endpoints need their own traces. |
| Substratum:306–329 (P24.3), :331–344 (P24.4), :348–357 (P24.5) | The word-length bounds for linear models use stabilization of a finite-dimensional span. That restriction is on a representation (**A** regarding A1). The passive all-time quotient instead needs finite order for backward-invariance, then a bounded partition refinement and full-support quotient masses (**F**). The known-model fibre criterion and its bound have distinct premises, as §14.1 records. |
| SM:242–256,334–338 (observer kernel) | The finite-carrier Theorem 1a specializes an operator identity. Lemma 1c(i) uses preservation of the specified probability and conditioning. Lemma 1c(ii) uses a finite determinant and clearing denominators at :254. A structured prior does not remove that spectral restriction. Part (iii) has a supplied companion. Proposition 4b uses product counting of six identical components and the common component-complete projection. **A** for the conditional covariance identity, **F** for the determinant and product-counting proofs, **W** for physical selection. |
| SM:1376–1388 (observer genericity, ledger `SM:T-22` and `SM:C-unnamed-235f5cba`) | C1 at :1378 uses a connected coupling graph and a nonempty proper cut. The C3 numerical estimate at :1382 uses a finite site count (N) and the same finite alphabet (q) at every hidden site. Data processing for the realized law remains a different implication. The record conditions C2 and C4 are separately supplied. **F** for the numerical estimate. **U** candidate for review: give the alphabet condition at the quantitative estimate and retain a nontrivial-coupling hypothesis in the corollary. Bounded degree and energy conservation allow a finite edgeless identity dynamics, for which no cut has C1. The C1 problem survives even when A1 is granted. |

### 15.1 Correction and replacement decision packet

- **SM:1376–1388.** Check the stated graph class and alphabet assumption against the inherited lattice setting. If the corollary is intended for arbitrary finite deterministic systems, restore the nontrivial coupling condition. The fixed-basis representation applies to the supplied finite observable record laws, with its own premise.
- **SM:252.** The optional scope precision is to put finite-dimensional meromorphic continuation next to the pole assertion. The broader proof obligation is already accounted for in the P12(b) trace. This census does not discharge it.
- **Registry.** Restore the cited-family anchors in a separately reviewed ledger change if the registry owners accept §12.1. A ledger line-number refresh can use live IDs and fingerprints without inferring any change of scientific scope.
- **Existing replacement boundaries.** GR Appendix B already removes deep cardinality from the exact finite-window marginal with its stated locality and prior. A1-10 and the normalized-recurrence records keep the visible return requirement separate from finite microscopic cycles. The current A1-RIGID-1 work and the P8 and P12(b) continuations enter this census only through their own landed, reviewed scope when available. No current disposition depends on their draft proofs.

## 16. Recursive verification and supplemental source inventory (X4)

At the §12 pin, `git ls-tree -r --name-only` under `verification`, `papers/main_repro` and `papers/oi_lattice_code` lists **3,269** tracked paths. The following deterministic screen traverses the text at that same commit.

```bash
pin=baeb7723743e99b137ae3d0a1694e99ff97e2a73
git ls-tree -r --name-only "$pin" -- verification papers/main_repro papers/oi_lattice_code
git grep -I -l -i -E 'total (finiteness|configuration (space|set)|state space)|finite (total (state|carrier|configuration)|universe|substratum)|H-count|P12\(b\)|common (exact )?(period|return)' "$pin" -- verification papers/main_repro papers/oi_lattice_code
```

The screen hits **106** paths, including 70 programmes, 30 audits, two paper-supplement scripts, two Lean modules, and two registry files. The registry and unattached evidence are checked in §§12–13. The raw hit list mixes primary claim records, earlier revisions/reviews, ledgers, status notes and independent instrumentation. The screen can miss a proof carried only by a normalized count, an imported finite instance, or a file with no matching text. The 3,163 paths without a hit have no negative classification from this run. Off-pin branches and archived claims with no current source consumer need an explicit provenance or support decision when encountered.

**Closure state.** A1-C01 remains incomplete. Review can check the positive traces, the source crosswalk and the proposed SM scope correction against this pin. Closure still needs declaration-level classification of the remaining bridge corpus and earlier evidence consumers, a semantic pass over the rest of the manuscript and its mirrors, and a disposition for the remaining implicit claims. The finite-window representation, supported finite-mode and finite-carrier theorems, and the gaps in the native physical chains retain their respective scopes.

## 17. Canonical paper statements and their first scope restriction

The lines below partition the live statement list from `tools/proof_census.py --json` at the §12 pin. A row identifies the first kind of finite object or a source premise to which the statement refers. The line list can be joined to the registry index for the exact statement ID and its evidence grade. A mathematical result may have narrower scope than its physical reading. A row for a definition records its stipulated types. An imported or incomplete proof is marked **X** where its actual dependency remains untraced. This pass does not change any ledger grades.

### Main (47)

| Statement lines | Scope used |
|---|---|
| 42, 46, 48 | The finite-capacity definition is about the observer. The proper-subsystem clause defines the complement. Both give the stated visible and partition implications without global counting (**A**). |
| 54, 84 | Finite cycle and global entropy maximization in Lemma 3, with bijectivity given. For :84 the specified conditional preparation suffices for an observed law, but its uniform canonical specialization invokes the finite counting step (**A/F**). §14.1 and Main roots R0. |
| 80 | Summary row. R1 and R2 of the Main roots audit supply finite-window realizability and history-law equivalences. R3 supplies the rooted return distinction. R4 and R5 identify additional kinematics and instrument hypotheses. The operational realization extension has its own approximation and control scope. |
| 113, 135, 141, 439 | Finite sets or a finite model by reference. Exact common permutation order supplies the identity return, and the relevant shared prior supplies normalized rooted rows. The stochastic obstruction after a return has the weaker scope in §12.2 (**F/A**). |
| 131, 171, 330 | Finite visible stochastic matrix for the inverse test, finite records and positive histories for the conditional mutual information bound, and an already supplied P witness on the diagonal subalgebra for the CP implication. These proof steps give no microscopic return premise (**A**). |
| 163, 457, 471 | Uniform conditional erosion or the earlier finite uniform-prior coupling model with a supplied mixing bound. The readback estimate uses the contraction comparison under these laws. The finite uniform prior in :457–471 is part of the stated model (**F**). The native input and quantitative decay remain **W** (Main roots R2, R7). |
| 210, 228, 246, 250 | A finite observed stochastic matrix gives the isometry. Phase locking and linearized block constraints use finite chosen Hilbert-space dimensions and spectral/identifiability hypotheses. The certified block-size cases in :250 remain discretely enumerated cases, with source selection **W** (Main roots R4). None needs A1 at that matrix scope (**A**). |
| 268, 274, 286, 534 | :268 uses basis permutation; the printed application is the declared finite tensor-product model. :274 uses finite uniform-hidden multiplicities, and :286 and :534 use normalized finite hidden sums or their specified weights. :534 adds the logarithm on the finite permutation unitary for integer steps. The counted constructions are **F**. |
| 298, 304, 312, 316, 318, 326 | Finite block ranks, twirls and the channel's fixed matrix basis in the particular binary lattice or permutation model. :312 is an independent finite-qubit Weyl twirl theorem (**A**). The specific lattice and partial-trace instances are **F** as stated. |
| 414 | Local response factorization under finite reading sets, separated cones and the setting-law/outcome conditions, with a finite cubic specialization. The proof edge uses the causal cone, not total finiteness (**A**). Main roots R6. |
| 484, 496, 520, 528, 550 | Finite menus, observed alphabets or horizons give the response tables and constructed realizations. The fixed-dimension obstruction compares the parameter count against the growing family of tables. The source correspondence in :528 is conditional on the source theorem's tuple and the translation hypothesis (T). The results for the stated representation classes have no physical A1 input (**A**). |
| 508, 516, 608, 626 | The capacity inequality counts the hidden states of a realization when that count is finite. The memory equivalence concerns an already realized conditional law and the per-window existence theorem. The canonical tail object is drawn from positive-probability finite words. **F** for the finite hidden count, **A** for the per-window statements, with the kernel delta in Main roots R2. |
| 568, 600 | Finite experimental dimension, outcomes, horizon and gate/instrument approximation or a finite diamond-net. These are construction inputs, with precision, preparation and control conditions (**A** with respect to total cardinality). Main roots R5. |
| 670, 674 | A horizon foliation singles out a timelike line, which restricts the symmetry group of the coarse-graining. The input is the foliation and the stabilizer assumption (**A** conditional). A physical selection argument is separate. |
| 752, 760, 762 | Selection in the specified finite coarse model depends first on the exact versus effective dynamics distinction, then on (EM), the rate and the record-erosion condition. The exact finite return is **F**. The conditional effective-channel refinement and the physical history gap are distinguished by Main roots R7 and the A1-05 source matrix. |

### GR (22)

| Statement lines | Scope used |
|---|---|
| 112, 132, 889, 893, 897 | Finite-causal-patch and normalized-deep-law distinction in §15. **A** for the exact finite-window generalization under (D1)–(D5). The counted H-BD step remains **F**. |
| 168, 174, 180, 184, 194, 200, 215 | Finite-dimensional spectra, visible matrices, finite operation words or supplied finite visible systems. At :184 the Gibbs orientation concerns the finite represented spectrum and supplied thermal weights. The actual finite-bath orientation enters separately through GR:186 and H-count. **A** at the stated mathematical scope and **F** for the counting application. §12.1 and §11. |
| 675 | This heading fingerprints a summary. The theorem body at :677 invokes S1–S4 and, for its calibrated coefficients, H-count, H-slope, H-frame, H-Hawking, boost structure and the matched rate ratio. The boundary-count inputs concern the counted modes. The calibration inherits the finite total shell at :58 (**F**). The full universality chain retains the source's stated proof limit (**X** where its route is not shown). |
| 729, 743, 749, 753 | Same product law or dilation for nested trace-outs, then visible spectral fit or other specifically stated hypotheses. :753 depends on the finite-count calibration. §15 locates each step (**F** in the printed finite setup). |
| 759, 779, 793, 801, 835 | Finite appendix sectors with distinct preparation hypotheses. Finite fibre or entropy counting for A.5–A.7 and cycle counting in the closed (B\cup R) subsystem for A.8–A.9. §15 traces the latter conditional statement and the native gap (**F/W**). |

### SM (41)

| Statement lines | Scope used |
|---|---|
| 122, 126, 140 | Boundary estimate for the stated state classes, one-dimensional stencil dispersion, and conditional low-energy entanglement-Hamiltonian form. The Fourier stencil uses local steps (**A** for that identity). The reference and state-class details of the area-law proof remain **X**, as does physical discharge of the supplied lattice Bisognano-Wichmann premise (**W**). |
| 210 | A4's periodic lattice, nearest-neighbor choice and the continuum filters. Finite alphabet plus a finite site model supplies finite total cardinality even without a separate name for A1. The metric/continuum step remains open (D20; A1-08 and the P12(b) trace), so the physical dimension selection stays **W**. |
| 224, 242, 252, 258, 270, 278 | Local symmetry and stencil identities apply to supplied projected operators (**A**). The finite-carrier theorem and finite-matrix spectral cancellation within Lemma 1c(ii) have their own scope (**F**). The actual scalar observer kernel and the temporal law entering :278 remain **W**. See §15. |
| 286, 302, 318, 328, 334, 340, 354 | Staggered and chiral operator algebra, real-diagonalizable finite component matrix, and conditional one-cone form or local stabilizer (**A** at the scoped form). The component-complete product count at :334 uses the finite counting specialization (**F**). Native projection, H-link and H-cust are separate physical conditions (**W**). |
| 366, 374, 390, 434, 440 | Counting signed links, group representation, comparison among the stated Bravais lattices and fixed neighbor/taste kinematics. Their finite indices have no total-state cardinality role (**A** at those algebraic scopes). The physical carrier-copy and charged-action identifications remain conditional (D15–D16). |
| 448, 454, 456, 464, 535, 543 | Finite spin/taste matrices, parity, and selected representation and action inputs. The algebraic identities use local modules. The assignment of physical spin, families, Higgs compatibility and chirality needs the stated H-spin', H-χ' and embedding information. That interpretation remains **W**. The census does not extend any finite lattice probe beyond its representative. |
| 575, 579, 589, 593, 599, 603 | Algebra of the supplied condensate stabilizer, central quotient, specified chiral matter family, anomaly conditions, charge identity and dimensional analysis in a specified (d). These conditional algebraic steps do not count total configurations (**A**). The native production of the stabilizer and charged family remains **W**. |
| 625, 633, 641, 647, 651 | Reversal of a supplied second-order local law and the topological angle's time-reversal fixed points use no total carrier count. :641 uses equal hidden fibre counts and the finite normalizer (**F**). :647 is a finite spectral counterexample to an implication, and :651 inherits the reversal/rate distinction and open topological and determinant selection. §12.2 and §14. |
| 1376, 1388 | Graph connectivity, the finite site and alphabet count in the numerical bound, and supplied memory conditions. §15 locates the scope candidate. **F/U**. |

### Substratum (8)

| Statement lines | Scope used |
|---|---|
| 189, 193 | Stage 1 supplies per-horizon representation, and Stage 2 takes a shared finite periodic representative and observer inputs. Theorem 23 explicitly invokes A1–A6. Reuse of the local algebra does not supply the transition from Stage 1 to that carrier or the native projection. **F/W**, as traced in the retained P12(b) source record. |
| 251, 268 | Uniform finite hidden prior for the relabelling specialization and a normalized independent finite factor for the exact stated enlargement. The finite bound in :268 is a visible/boundary cutoff interpretation, the no-H-BD finite-window result has the Appendix B extension, and exact fixed-interface transfer has its own conditions. **F/A** at these different scopes. |
| 280, 306, 331, 348 | Finite hidden block traces for P24.2, finite-dimensional linear realization for P24.3, finite permutation order and partition refinement for P24.4, and a split between the general compatible-fibre core and finite refinement bound in P24.5. §§12.1, 14.1 and 15 locate the first uses (**F/A**). |

### Structure (12)

| Statement lines | Scope used |
|---|---|
| 624, 629, 635, 638 | Embedded-observer algebra, specified separable hidden Hilbert space and channel equivalence. These definitions do not force a finite hidden carrier. Use :629's separate structural-class clause when comparing A1–A6 realizations. |
| 646, 652 | The finite OI-class examples inherit A1 and Substratum Theorem 24's fixed-interface preparation and channel hypotheses (**F**). The broader equivalence of embedded observers uses the supplied visible algebra and channels. |
| 660, 669, 681 | Finite-dimensional Kraus/Choi factorization at :660. At :669 the finite proof uses minimal Kraus families; the general statement invokes minimal Stinespring uniqueness for supplied pure-reference dilations. The local finite dimension does not impose A1 (**A**). The source distinguishes the finite formalization from the general imported result. |
| 713, 724, 728 | Admission definitions and structural distinction scope C1–C4 to the partition and realized readout. No genericity probability follows from the definitions. The following finite-permutation examples and counting claims require their specified model and ensemble, independently of the definitions. |

### Computation (2)

| Statement lines | Scope used |
|---|---|
| 106 | Uniform family of finite experiments, efficient operations and fault-tolerance/precision hypotheses. The class claim is for a scalable model. Its fixed finite implementation has a separate resource envelope (**A** conditional with respect to total finiteness). |
| 132 | The patch-budget premise is the first cap on physically available entanglement dimension. The preceding section distinguishes that premise from A1 and names the further rate and simulation-cost assumptions for the computational ceiling. **W** for the physical budget and transfer. A dimension cap can exclude strategies requiring more resources than the cap; it does not provide a realization of every approximable correlation. |

**Scope check.** The row counts are 47 + 22 + 41 + 8 + 12 + 2 = 132. This is the canonical bold-heading inventory. The unnumbered propagation in every paper and chapter still needs its own source review. §18 samples the highest-impact imports in the six papers without registered headings. Where no first inference can be followed past a cited result, the remaining step is **X**, even if a consumer has a verified statement fingerprint.

## 18. Selected downstream claims outside the canonical register

| Site at the §12 pin | Earliest dependency, scope and remaining question |
|---|---|
| `papers/Introduction.md:48–98,131–145,163–169` | Finite-alphabet and finite-window realizability, followed by hidden memory on a supplied law (**A**). Recurrence needs a common rooted prior and an identity return, which the finite permutation supplies (**F**). The finite experiment and Bell discussions use specified controls and source questions. The black-hole application separates preserving the state from recovering a record and does not supply H-scramble. |
| `papers/Methodology.md:140–164,220–235,335–357` | The finite-eventual-image restriction needs stabilization of the descending sequence of images, and the printed injectivity-to-surjectivity step uses a finite total carrier (**F**). Per-occurrence distinguishability supplies neither a uniform alphabet bound nor a count of total states. Record preservation only treats distinct registered records. General hidden-margin recovery remains **X** at the proposed dichotomy. The reconstruction and gauge accounts inherit the A1–A6 class of Theorems 23–24, the finite counting prior and the stated fixed-interface comparison, with the wider physical selection open. |
| `papers/Complexity.md:35–45,166–178,202–214` | The chemical tree inherits the A4 dimensional branch, the continuum conditions and supplied spin/statistics and chiral interaction, rather than obtaining them from counting configurations. The fixed structural class is **F** and native reconstruction is **W**. The anti-Boltzmann-brain and past-hypothesis claims explicitly cite Main §4.6 for the finite model and require (EM), readback erosion and the relatively fast rate on the same observer. P8's effective operator argument alone supplies no corresponding physical record ensemble. |
| `papers/Juno.md:38–46,107–128,168–183,362–375` | The sum rule uses finite-dimensional flavor matrices under a declared coefficient relation, normalization and reactor projection. The symbol (A_1) in §3 names a perturbation coefficient. The cubic geometry and propagator normalization imports have their own source conditions, including the open dressing. Finite recurrence and shell counting enter only in the fixed lattice candidate discussion in §6.3. **A** for the stated coefficient algebra and **F** for the lattice tests. The common physical source remains **W**. |
| `papers/Medicine.md:25–39,86–110,421–429` | The relevant mathematical implication is matched-present readback on a finite record (**A**). The printed recurrence-scale statement keeps its independent finite-model condition (**F**). A finite store and its repeated writes give a capacity count at the specified operational partition. They neither bound the whole physical carrier nor supply the empirical C1–C4 claim for each example. The remaining empirical obligation is already routed to #1342 R4. No clinical claim is evaluated by this census. |
| `papers/Bioinformatics.md:42–48,118–143` | The inference about a regulatory target is conditional on completions sharing the available law and disagreeing on that target. The finite-horizon predictive quotient and conditional-memory comparison refer to Main §3.4 (**A** at record scope). The actual equivalence of completions and the records carried in each assay remain **W**. There is no total-universe count in this implication. |
| `book/ch18-beyond.md:166–185,288` | Exact all-time recurrence uses finite permutation order. The upper bounds invoke cycle lengths of the full finite configuration space, and the linear sharpened bound uses the algebra generated by an invertible operator on a finite free (q)-alphabet module. The book explicitly takes A1 for this route (**F**). Visible/deep-state cardinality comparison on a finite window uses the narrower GR conditions. An information-capacity assertion for experiences would additionally need a specified finite encoding and accessible record model (**W**). |

The sampled transfer rows keep the A1-dependent model steps visible without assigning new physical premises to this unit. They leave the rest of the unnumbered paper and chapter evidence at its prior status. The largest remaining task is proof-level dependency classification of the bridge modules and recursive verification evidence. The current index enables exact source selection but neither an empty cue set nor an attached proof grade can stand in for that trace.

## 19. Lean source changes since the earlier coverage batches

The comparison

```bash
git diff --name-status 5ea8672f67f3fd44498c7aa65e2eac22ed14a315 baeb7723743e99b137ae3d0a1694e99ff97e2a73 -- verification/lean-mathlib/OIBridge/ verification/lean/
```

returns five changed or added bridge sources and two changed Python probes. None of the 54 module files listed in §§9–11 changed bytes between these pins. That confirms those source locators. Imported evidence still has to be checked at the required scope for each conclusion.

| Changed source | Scope at the current pin |
|---|---|
| `ReadWriteControl.lean:54–78,128–151` | The fixed-shape model is a finite matrix model. The historical predicate requires every matrix representative of each available channel to be an exact permutation. The relevant quantifier is over channel representatives at each level, which leads to the vacuity identified on the two-state visible carrier. |
| `ReadWriteNonvacuity.lean:44–84,104–157` | Level-one identity is available from the readout. A quarter-phase multiple of the identity has the same conjugation channel, so the exact-permutation representative condition fails on `Fin 2`. The surviving positive witness tests `MonomialSource` for the particular generated permutation theory. This is a finite operational witness, with an observable matrix size and ancilla levels. It gives no native physical sourcing verdict. |
| `SubstratumInterface.lean:46–81,97–123,151–170` | Permutation and phase operators are monomial in the stated finite representation and preserve the diagonal under conjugation. The conditional no-go on `Fin 2` then compares composite control to the specified nonmonomial rotation. The argument uses that finite system and exact scope of availability. It does not require the older vacuous antecedent. |
| `StructuralClosure.lean:162,171–279,330–345` | The implementation class is monomial and its finite lifts and sums preserve the stated diagonal sector. A control assumption would make a rotation available in this particular generated theory, contradicting the invariant. This is the two-state negative clause discussed in Main roots R5, with an explicit finite matrix and implementation scope. |
| `RouteB.lean:283–325,382–397` | `DerivedOICore` is instantiated through the sealed two-state construction and actual readout. The falsifier reduction excludes phase-free richness for this theory. This finite witness is a countermodel to an implication for the stated functional class. It neither establishes nor assumes a finite physical universe. |

The scopes above preserve finite witness results (**F**) and their model-class non-implications. The operative restrictions are the available representations, controls and explicit finite model. Passing from them to the admissible operations of one physical OI realization remains **W**. The two changed Python probes concern Bohr-frequency and edge-rigidity evidence. The finite visible spectral scope of GR §3.3 is accounted for in §17. A new line-by-line comparison of both probe bodies against the source proof remains in X4.

### 19.1 Coverage boundary and material replacements

The nine originally read bridge modules in §2 and the 54 named in §§9–11 together name 59 different files. This continuation gives a module-specific trace to 20 additional bridge files: `CombRealization`, `CanonicalMeasure`, `ObservabilityQuotient`, `PassiveQuotient`, `ControlledQuotient`, `CycleFibreHull`, `CompositionOrder`, `RecordFibreIdentification`, `ManuscriptAxioms`, `ChiralCenterRecovery`, `GaugeDimension`, `GradientLinkFlatness`, `IdempotentTrace`, `OperationalAssembly`, `KrausSoundness` and the five just listed in §19. Subtracting that union of 79 basenames from the 242 indexed bridge modules gives 163 without a module-specific trace in this census. This is a lower bound on the remaining proof work. A traced declaration does not classify every declaration in its file. The imported proof assumptions of the rest and the primary consumers of unnumbered claims remain **X**.

| Closure family | Mathematical replacement or scope condition that the source record still calls for |
|---|---|
| C02/C10 · representation and recurrence | Keep the per-horizon construction for the representation statement. Exact microscopic periodicity is sufficient for the common visible return in Main §2.3. A1-10's matrix obstruction works on an already supplied total-variation revival and its near-return form needs a common quantitative return after overlap under a compatible rooted law. A coherent carrier across horizons, the law and physical access to the return remain distinct. See `a1-10-recurrence-premises/PREMISE-LADDER.md:144–164` under this directory's parent. |
| C03/C06/C07 · A4 and P12(b) | State the finite periodic class as a sufficient specialization. A broader result would need one compatible carrier, law and readout, the native scalar one-step kernel, the same-system temporal response and a valid continuum/spectral transfer. The finite determinant proof cannot act as that transfer. See `a1-free-p12b-observer/TRACE.md:13–30`. |
| C04/C05 · local algebra and reciprocal flux | The local link implication takes the designated carrier and action as inputs. The measurable reciprocity kernel replaces finite hidden counting by a supplied normalized invariant and reversing law. Its conditional row version needs positive initial cell masses and the appropriate equality of the compared masses. See `a1-11-local-gauge-forward/FORWARD-ALGEBRA.md` and `MeasuredReciprocity.lean:198–276`. |
| C08 · shell and action calibration | A boundary-only count can derive the stated slope on the declared product branch. The coupled physical result needs a conserved, physically interpreted energy, corresponding normalized shell law, and the two rates for the same operational transition. Compare `p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md` with `a1-07-p7-energy-state/DECISION.md`. |
| C09 · selection from actual histories | The effective operator decay is conditional on the specified law, projection and mixing bound. To transfer it to a native observer, show a relation to the exact retained record dynamics, the relevant accessible-time rate and an appropriate state/ensemble. See `a1-05-p8-observer-selection/SOURCE-MATRIX.md:13–43`. |
| C11 · gravity, matter and applications | The finite Page-curve route requires H-scramble, H-decouple and the full product shell. Exact causal-patch marginals on an arbitrary deep carrier already have the stated Appendix B route. The further gravity, QCD and biological source obligations use those conditional imports only at their own scopes. The manuscript and evidence still need a search for other implicit propagation. |

These are scope and replacement obligations already present on the source pin. Draft follow-ons under other workstreams may supply more specific results after their own review. A1-C01 remains **INCOMPLETE / UNCLASSIFIED**. Independent review applies to this checkpoint's observed findings.
