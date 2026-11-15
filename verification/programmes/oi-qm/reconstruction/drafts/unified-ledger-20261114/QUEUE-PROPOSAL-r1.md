# Queue proposal r1: manuscript corrections, ledger coverage and research obligations

**UNREVIEWED. Proposal for owner decision.** This document decides nothing. It changes no manuscript
wording, tier, readiness, authorization, Issue, label, Project card or queue. Every proposed change of
planning attribute below is marked **(proposal)** and takes effect only by a recorded owner decision
(`AGENTS.md` §A.45 rule 3, line 1225 on `main`: "**A priority is never authorization.**"). The work
was read-only and paper-only: no computation on OI rules was run, and nothing was committed, pushed or
posted.

**Inputs.**
- `LEDGER-r5.md` (unreviewed), the minimal revision of `LEDGER-r4.md` that applies `REVIEW-r4.md`
  (ACCEPT WITH CHANGES). Row identifiers are those of r5; r5 changes no identifier of r4. It changes
  the classes or support of B-QM-22 (support K), B-GR-12 (adds "minimal-coupling factorization
  δ = 1"), B-STR-2 ("preliminary"), B-QCD-9 and B-QCD-10, and the statuses of J-3 and J-4 (now
  carrying the factorization interface of `papers/Main.md`:558), per `diff` of r4 against r5.
- `COVERAGE-AUDIT-r4.md`, accepted by `REVIEW-AUDIT-r4.md` (ACCEPT). "Audit F-n" is its §3.1, "§3.2"
  its single-source table, "K-n" its §8.
- Owner records, read through the GitHub API on 2026-11-14: #914 comments 6877871344 (ledger
  conditions), 6877908458 (QCD group), 6878200172 (scientific emphasis), 6878781541 (guidance on the
  audit and this proposal); #1169 comments 6877981234 and 6878199016 (S-J and EXACT); and the
  planning-status blocks and latest comments of #914, #1169, #1143, #1007, #868, #1060, #873, #1211,
  #1063 and #872.
- `AGENTS.md` at `main` `dfeec843`, §A.45 (lines 1209 onward), §A.25 (line 317 onward), §A.14
  (line 553).
- Manuscript lines were read at `main` `dfeec843`, the ledger's base (`LEDGER-r5.md` header,
  "Base"). Book-to-FULL mirror lines in Part 1 were located by exact line match against
  `book/The-Incompleteness-of-Observation-FULL.md`.

**The governing owner guidance, quoted.**
- #914 comment 6878781541 (`amaybaum`, 2026-11-14T14:26:48Z): "The subsequent queue proposal should
  distinguish manuscript corrections, missing ledger coverage, and scientific research
  obligations—they require different work and authorization." and "The audit does not yet justify
  promoting QCD or another downstream branch ahead of the shared foundational gaps."
- #914 comment 6878200172 (`amaybaum`, 2026-11-14T13:47:10Z): "Emphasis is not execution order.
  Prioritizing sector justification must not make it a new prerequisite for already authorized Bell,
  gravity or mechanism work." It "sets no execution order and changes no Issue's prerequisites,
  readiness or authorization", and queue changes "are then a separate decision".
- Coordinator relay for this draft: each research move must name the obligation it advances with its
  ledger row, its recorded prerequisites, readiness and authorization, and the concrete next unit and
  why it outranks the alternatives; the emphasis "is not a predetermined ranking", and the evidence
  decides the order.

The three parts are kept separate. Each names the authorization it would need.

***

## Part 1. Manuscript corrections (MC)

### 1.0 What any MC unit needs

No MC item below is authorized. Each would need, separately:
1. a recorded owner authorization for that correction unit (§A.45 rule 3; §A.43);
2. an accountable Issue (§A.45 rule 6, line 1263: "A pull request is never an accountable home").
   None of the MC candidates has one; the ledger asks the owner whether any should be scheduled
   (`LEDGER-r5.md` §12, Q11). **(proposal)** One accountable Issue per MC unit below;
3. a manuscript PR limited to the minimum necessary change (`AGENTS.md`:317–330);
4. §A.25 propagation: a corpus-wide grep for the phrase and its paraphrases, every chapter edit
   mirrored into FULL and the reverse (§A.14), and regeneration of the affected `.tex`/`.pdf` with
   `sh ./build.sh` (papers: `papers/<NAME>.tex`, `.pdf`; book:
   `book/The-Incompleteness-of-Observation-FULL.tex`, `.pdf`, all present on `main`);
5. for paper edits, the §A.32/§A.33 added-lines battery;
6. independent review, and a separate owner decision to integrate (§A.45 rule 7, line 1278).

This proposal drafts no manuscript text. "Minimal correction" below names the defect the correction
would remove, not its wording.

**Mirrors.** "Mirrors" lists the mirrors the ledger or audit recorded and those this pass located by
exact line match. A §A.25 grep at correction time may find more. Where a phrase grep of
`papers/*.md` and `book/*.md` found hits whose context was not read, they are listed as "to check".

**Recovery before concession.** Where the finding is unresolved (U-n), the Code Review Rules require a
documented, proportionate recovery attempt before a substantive narrowing of an unrefuted
mathematical claim "solely because its proof is missing" (`AGENTS.md`, Code Review Rules,
"Theorem recovery before concession"). Those items are placed in MC-5 for that reason.

### 1.1 MC-1. Book passages that contradict a paper anchor already in the corpus

Direct contradictions in the book whose authoritative anchor (§A.25 step 2) is already a careful paper
statement. No new science is needed.

| ID | Passage A (book) | Passage B (anchor) | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| D7 | `book/ch18-beyond.md`:256: "$\mathrm{SU}(2)$ as chiral and $\mathrm{SU}(3)$ as vector-like, derived from the staggered trace-out" | `papers/SM.md`:543: "Theorem 13 (Chirality — conditional identification; minimal embedding certified vector-like; H-χ' sharpened, open)"; `book/ch19-open-problems.md`:328: "Open — named hypothesis H-χ'" | DC (`LEDGER-r5.md` §F.1) | Remove "derived"; state chirality at its source status (conditional, H-χ′ open) | FULL:5062; FULL `.tex`/`.pdf`; grep ch05 (the sentence cites "Chapter 5") |
| D8 | `book/ch10-chemistry.md`:86: "SU(3) color confinement (Chapter 5 §5.4) produces bound hadrons"; :88: "The mechanism is derived from the gauge structure of SU(3)" | `papers/SM.md`:801: whether the induced theory "is in the deconfined phase required for the perturbative matching to be valid", the Haar-measure theory confining (:801–811); `book/ch05-gauge-structure.md` §5.4 (from :81) carries no confinement statement (ledger §11 D8) | DC | Remove the derivation claim and the citation to a section that does not carry it; state confinement as open for the framework's measure | FULL:2894 and FULL:2896 (the ledger lists only :2894; :88 mirrors at :2896, located by this pass) |
| F-31 (K-1) | `book/ch19-open-problems.md`:106: "anomaly cancellation forces exactly three candidate matter sectors" | `papers/SM.md`:458: "anomaly cancellation fixes charges given the sector pattern; the selection of the observed family pattern … is not supplied by either" | DC (audit F-31) | Restate at SM's scope | FULL:5253 |
| F-32 (K-2) | ch19:196: "The framework derives exactly one scalar doublet" | `papers/SM.md`:468: "This theorem does **not** derive the existence of a Higgs doublet" | DC (audit F-32) | Remove the derivation claim | FULL:5343 |
| F-33 (K-4) | ch19:118: "The framework derives the total budget" | ch19:116: "the total fraction is partly definitional, equal to $1-\Omega_B$ by construction"; `papers/GR.md`:541: "partly definitional" | DC within the chapter (audit F-33) | Align :118 with :116 | FULL:5265 (and :5263 for :116) |
| D1 | ch19:20, the §19.2 heading "Problems resolved" | ch19:72: "the paradox is not resolved"; ch19:80: "Not resolved." | DC within the chapter (ledger §F.1) | Bring the heading into line with its entries | FULL:5167 |
| F-34 | `book/appendix-a-prediction-status.md`:145–158: eleven biology rows (B1, B2, B6–B14) labelled S; :28 defines S as "no fitted input and no open link specific to the entry" | `book/ch16-medicine.md`:6 and `book/ch17-bioinformatics.md`:6: "**Status — conjectural extension.** … offered as a *conjecture*, not an established result" | DC (audit F-34) | Relabel the eleven rows to the chapters' conjectural status; B3 unchecked (audit §10) | FULL:5669–5682; to check: `papers/Medicine.md`, `papers/Bioinformatics.md` (companion papers present on `main`; not read) |
| F-36 | appendix-a:131: "Normal mass ordering \| structural … \| C" | appendix-a:135: "the ordering a heuristic consequence of taste-breaking rather than a theorem"; `papers/SM.md`:1460 | DC between label and note (audit F-36) | Relabel N5 to its note's status | FULL:5655, :5659 |

### 1.2 MC-2. Paper passages that contradict an anchor in the corpus

| ID | Passage A | Passage B | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| F-3 | `papers/Substratum.md`:165: "Partition-spinor identification (Theorem 12) and trace-out (Theorem 13) give chirality."; also :151–152, :169, :173, :201, :203 | `papers/SM.md`:543 (Theorem 13 conditional; H-χ′ open); :468 (Higgs doublet not derived); :448 ("free-kernel identification refuted; H-spin' open"); Substratum:161, :193, :199 carry the conditions | DC on chirality; DA on generations and the Higgs (audit F-3) | Carry Theorem 23's own conditions (:193) into the Stage 2 text and the :201, :203 remarks | Substratum `.tex`/`.pdf`; grep `book/ch02-substratum.md` and FULL for the Stage 2 restatement |
| F-21 | `papers/SM.md`:567: "the 'wrong-chirality' doublers … become, in OI, the physical generations (Theorem 9)" | `papers/SM.md`:448: Theorem 9, "free-kernel identification refuted; H-spin' open" | DC (audit F-21) | State the generation identification as conditional on H-spin′ | SM `.tex`/`.pdf`; grep book ch05 |
| F-24 | `papers/SM.md`:863: "the GST relation [21] follows as a corollary" | `papers/SM.md`:887: "The GST relation [21] is an external empirical relation … inherits GST's empirical status" | DC within one section (audit F-24) | Make :863 agree with :887 (scope: :863 gives a scaling argument, audit F-24) | SM `.tex`/`.pdf` |
| F-18 | `papers/Structure.md`:417: "the emergent QFT's parameters are derived from the cubic-lattice structure rather than being moduli to be selected" | `papers/SM.md`:1396 (couplings at $M_Z$ "set by the threshold $\delta_0$ and the resummation parameters $A, B$, matched"); :1440 (Layer 3 mass scales, CP) | DC (audit F-18) | Restrict "derived" to the structural content SM derives | Structure `.tex`/`.pdf` |
| F-17 | `papers/Structure.md`:179: dark-sector phenomenology at Level G3 × D; :703: "OI's substratum produces $SU(3) \times SU(2) \times U(1)$ uniquely" | Structure:191 ("*[SM]:* Level D × Levels G1–G2"), :192 ("*[GR]:* Level D × Levels G1–G2"); `papers/SM.md`:14, :1424 (lattice selected by the observed group) | DC within Structure (:179 against :191–192); DA (:703) (audit F-17) | Reconcile the placements; carry H-link, H-cust and the selection at :703 | Structure `.tex`/`.pdf`; interacts with LC-1 (T-6) |
| F-2 (coupling clause only) | `papers/Structure.md`:733: "random permutations on finite sets typically lack the coupled-dynamics … features required for C1–C4" | `papers/Main.md`:147–151: "the fraction of bijections failing C1 at the $T$-level decays exponentially in the hidden-sector capacity $n_H$" (exact counting over all bijections for a fixed product partition, audit F-2) | DC for the coupling clause; the C2–C4 clauses unresolved (U-2) | Remove the coupling clause; leave the C2–C4 clauses to MC-5 (the corpus proves neither direction, audit F-2) | `book/ch03-structural-realism.md`:26 and FULL:891 (audit K-11); Structure `.tex`/`.pdf` |

### 1.3 MC-3. Differences in assumptions or scope, and single-source overstatements, with a settled anchor

Each item has a settled anchor and needs no new result.

**Substratum** (`papers/Substratum.md`; artifacts `Substratum.tex`/`.pdf`):

| ID | Passage A | Passage B / support | Class | Minimal correction |
|---|---|---|---|---|
| F-4 | :199: "no fitted parameters, no model-building choices, no landscape of alternatives at the level of the gauge sector" | `papers/SM.md`:1424: Theorem 7b selects the lattice "*because* $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ is observed" | DS (audit F-4) | State that the lattice input is selected by the structure counted as evidence |
| F-5 | :525: "**1 is structural with no open link of its own** (B-S), **2 are conditional structural** (B-C) …" | `papers/SM.md`:1269–1316: 2 S and 5 C among 22 | DS with unexplained residue (audit F-5) | State the mapping between the two counts |
| F-16 | :231–233: "a bidirectional correspondence for the **local reconstructed residue**", displayed with ⟷ | Theorem 23 (:193) witnesses data → class only; no witness for class → data (audit F-16; §A.34) | SO of directionality | Display the proved direction only (§A.34) |
| S-1 | :389: "Both are derived rather than fundamental" | `papers/GR.md`:162 (Einstein equations imported); Substratum:423 (conditional on G3) | SO (audit §3.2) | Carry the G3 condition |
| S-2 | :421: "does establish … derived from the same object by the same procedure under the same conditions" | ledger §9 GR–SM undetermined; Q4 | SO | Narrow to what is established |
| S-3 | :46: "The dark sector is the gravitational effect of the unreadable storage" | `papers/GR.md`:452, :540 (conditional, partly definitional) | SO | Carry the conditions |
| S-10 | :239: weak ER=EPR "as a structural consequence of the framework's holographic architecture" | `papers/Structure.md`:463 (OI "does not naturally produce full AdS/CFT-style correspondence") | SO | State it as proposed (ledger C-ERP, PE) |
| S-17 | :459: "generates every concept in fundamental physics" | G3 open | SO | Narrow |
| S-19 | :475–479: Class A "structural theorems" | generations on H-spin′; gauge reading on H-link, H-cust | SO | Carry the named hypotheses |

To check for mirrors: `book/ch02-substratum.md`:198 and FULL:832 contain "derived rather than
fundamental" (phrase grep; context not read).

**GR** (`papers/GR.md`; artifacts `GR.tex`/`.pdf`):

| ID | Passage A | Passage B / support | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| F-7 | :410: "all three results match the OI predictions of normal ordering with $\Sigma m_\nu$ near the oscillation minimum"; "both follow from the same lattice structure" | `papers/SM.md`:1464 (genericity heuristic, :1456); :1460 ("generically"); appendix-a:87, :130 (L, "oscillation inputs") | DA; SO in the coupling sentence (audit F-7) | State the neutrino items as heuristics; remove the unsupported coupling to the running vacuum | — |
| F-11 | :48: "$\tau_B \gtrsim 1/H$ … **Satisfied.**" | :456: "which is not derived from the substratum dynamics" | DS (audit F-11) | Align :48 with :456 | — |
| F-12 | :536: "no predictions are fit to the quantities they predict" | :539–545: "factor imported", "partly definitional", two "in tension" | DS (audit F-12) | Carry the table's own qualifications into the preamble | — |
| F-13 (K-3) | :454: "no particle dark matter exists"; `book/ch19-open-problems.md`:46: "Dark matter is not a particle" | GR:458: "a consistency check for the total dark sector budget, not a derivation of its internal structure"; GR:530: "$\rho_E \approx \Omega_{\text{CDM}}\,\rho_{\text{crit}}$ — an input" | DS (audit F-13) | Narrow to the corollary's scope | FULL:5193; to check: `book/ch00-introduction.md`:83 / FULL:310 and `book/ch09-universality.md`:254 / FULL:2721 (phrase grep "no particle dark matter"; context not read) |
| F-15 (K-10) | :530(iii): "adiabatic initial conditions set by inflation" | `book/ch19-open-problems.md`:194: "**Framework status.** Not addressed." | DA (audit F-15) | State inflationary initial conditions as an input at :530 | ch19:194 / FULL:5341 is the other passage, not changed |
| D5 | :418: "*Under Lemmas 1–3 and conditions (C1)–(C4)*" | proof uses the geometry-first ordering (:448–450), Jacobson's Clausius relation (:426), $T_{cl}$ resting on H-count (:422, :58); abstract places it at G4, conditional on G3 (:12) | DA (ledger §11 D5) | List the premises the proof uses | — |
| G-2 | :12: "the counting $S = \sigma A/\epsilon^2$ itself unconditional" | :40 (the partition presupposes GR causal structure) | SO (audit §3.2) | Carry the condition | — |
| G-30 | :615: "(a) *Unconditional.*" | (U1) uses Jacobson and H-count; S1 presupposes a horizon (audit §3.2); ledger B-GR-10, CD[S1–S4] | SO | Carry S1–S4 | — |
| F-10 (optional) | :90: "Lemma 1 is a consequence of partition geometry" | :585: "(independent in Part I; consequence of geometry in Part II)" | no conflict (withdrawn); optional (audit F-10) | Optional only | — |

**SM** (`papers/SM.md`; artifacts `SM.tex`/`.pdf`; appendix-a and FULL where noted):

| ID | Passage A | Passage B / support | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| F-6 | :1293 (composite Higgs row, **S**); appendix-a:91 (row 22, S) | :1116 ("The Higgs is the $A_1$ taste — a composite scalar"); :468; appendix-a:28 (S definition) | DA (audit F-6) | Relabel to carry the composite-hosting link | appendix-a:91 / FULL:5615 |
| F-25 | :871: "$A = \sin\theta$"; :1279 class **S** | :881: the identification "is a leading-order statement whose correction is the same open object as the Condition-2 ratio" | DA (audit F-25) | Carry the open identification link in the class | appendix-a row 6 (audit §5) and its FULL line, to check |
| F-35 | appendix-a:70: "S \| 0" | `papers/SM.md`:793: "conditional on single-copy H-link, Theorem 6" | DA (audit F-35) | Relabel row 1 | FULL:5594 |
| F-8 | :1353: "The same construction forces the following"; :1360: "with no free parameter to adjust" | :1290–1291 and footnote ᶠ (L, "given Condition 2"); :1048 ($b_{23} = 1$ a choice) | DA (audit F-8) | Carry Cond 2 and $b_{23} = 1$ | — |
| F-23 | :14: "contain no parameters fit to the predicted quantities"; :847; :14 and :1588: "six fermion masses from a single empirical input"; :989 | :971 ($Q_{\text{down}}$ "as a phenomenological input"); :887 (GST empirical); :1215 (K = 1/2 by "empirical fitting"); table E, R, P rows | SO within SM (audit F-23) | List the further empirical inputs | — |
| F-38 | :1110: "the substrate-level mechanism … is realized in the bijection"; :1100; :1092 | :1108 (mechanisms examined excluded; Cond 2 "a stated condition"); :1349 (values known beforehand) | SO (audit F-38) | Remove the match-to-mechanism inference | — |
| SM-36 | :1339: "strong evidence for the underlying $C_2/d$ identity" | one row "via Cond 2"; :1349 (retrodictions) | SO (audit §3.2) | Narrow | — |
| F-12 row (appendix-a) | appendix-a:190, F12 listed under forward predictions | the same row: "*retrodiction, not a forward bet*"; "does not discriminate" | placement (audit §5) | Move or relabel the row | FULL:5714 |

**Structure** (`papers/Structure.md`; artifacts `Structure.tex`/`.pdf`):

| ID | Passage A | Passage B / support | Class | Minimal correction |
|---|---|---|---|---|
| F-19 | :403: "OI's [SM §8.4] predicts Majorana neutrinos"; :1317: "so $0\nu\beta\beta$ should be observed" | `papers/SM.md`:1452: "On the branch where the singlet taste hosts the Higgs (Theorem 11, taken as input) and no gauge-singlet fermion" | DA (audit F-19) | Carry the branch condition |
| F-20 | :13: "The substratum-level equivalence reading does not hold."; :369 | :351: "in their standard formulation"; :242: "The provisional conclusion is (c)" | DS (audit F-20) | Carry the standard-formulation scope |
| T-4 | :453: "any horizon entropy in OI's framework is bounded by $A/4$ under the conditions of the horizon calibration" | calibration equality only; GSL open (`papers/GR.md`:781) | SO (audit §3.2) | Narrow to the calibration's conditions |
| T-9 | :813: the pair "captures … gauge couplings at $M_Z$, Yukawa structure producing CKM/PMNS" | `papers/SM.md`:1396, :1440 (fitted thresholds; solution-specific Yukawas) | SO | Narrow |
| T-12 | :970: "moderately favors the no-GUT universality class" | `papers/SM.md`:841 (not unique to OI) | SO | Narrow |

**Book, further** (book chapters; FULL mirrors):

| ID | Passage A | Passage B / support | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| D9 | `book/ch19-open-problems.md`:88: the lattice "eliminates the divergence and with it the cutoff sensitivity of $m_H$" (ledger §11 D9) | `papers/SM.md`:1570: "*structurally identified* … the theorem-level derivation is deferred"; :613 ("derivation deferred there") | DS (ledger §F.1) | State the protection as identified, its derivation deferred | FULL:5235 |
| D10 | `book/ch10-chemistry.md`:80: "the necessary ingredients are derived"; "the *possibility* of baryogenesis as a theorem" | `papers/SM.md`:1320 (three physical generations conditional on H-spin′; H-χ′ open); `papers/Substratum.md`:415 and ch19:184 (CP phases solution-specific inputs); `papers/SM.md`:1486–1490 (baryon number conserved at the substratum), :1496–1506 (violation emergent) | DA (ledger §F.1) | Carry the conditions; remove "theorem" | FULL:2886–2888 |
| K-5 | ch19:356: "The framework derives the fundamental laws" | `papers/GR.md`:162 (Einstein equations imported); `papers/SM.md`:14, :1428 ("compression") | SO (audit §8) | Narrow | FULL:5503 |

**Citations and conditions across papers.**

| ID | Passage A | Passage B | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| D2 | `papers/Main.md`:20, `papers/SM.md`:14, :60 cite [Substratum §3.3] for H-Bell; `papers/Introduction.md`:145 cites [Substratum §3.2] | definition at `papers/Substratum.md`:131–133 (§3.2); Stage-2 use at :171 (§3.3) (ledger §11 D2) | citation | One consistent citation to the definition | Main, SM, Introduction `.tex`/`.pdf` |
| D4 | the book chapters carrying the preparation-indexed Bell route; `papers/Substratum.md`:131–133, :193 | `papers/Main.md`:362, :414 and `papers/SM.md`:104: a coupling graph that varies between state classes needs an update outside (vii)/A5 (ledger §11 D4) | DA | Carry the (vii) condition where the route is stated. The book sites are not located in the ledger ("the book chapters carrying the preparation-indexed route") and must be located first; the wording depends on Q2 (linearity) if A5 is restricted | to be located |

### 1.4 MC-4. Manuscript-revision differences

| ID | Passages | Class | Minimal correction | Mirrors |
|---|---|---|---|---|
| F-9 | `papers/SM.md`:1118 ($m_H \approx 129$–$132$ GeV, "4–7 GeV below", "consistent … within the current $m_t$ uncertainty"); :1126 ("128–132 GeV … to ∼2–3σ (reduced to ≲1σ for the CMS $m_t$)"); :1294 ("$m_t$-consistent") | MR (audit F-9) | One comparison, stated once | SM `.tex`/`.pdf`; appendix-a row 22 if its comparison text differs (to check) |
| F-29 | `papers/SM.md`:981 ("0.474 ± 0.056. Match: 0.05σ"); :1289 ("0.465 ± 0.024 \| 0.27σ"); :1335 ("0.474"); appendix-a:86 ("Within 1σ") | MR (audit F-29) | One data value and comparison | appendix-a:86 / FULL:5610 |

### 1.5 MC-5. Contingent candidates: each waits for an LC trace, an RO outcome, a recovery note or an owner question

| ID | Passages | Class | What it waits for | Mirrors |
|---|---|---|---|---|
| F-2 (C2–C4 clauses), U-2 | `papers/Structure.md`:733 against `papers/Main.md`:147–151 (C1 only) | unresolved: "The corpus proves neither that typical bijections fail C2–C4 nor that they satisfy them" (`LEDGER-r5.md` §U, U-2) | recovery note (Code Review Rules) or RO-9 below | ch03:26, FULL:891 |
| F-22, U-3 | `papers/SM.md`:1448: "it does not affect any prediction of the OI framework"; `papers/Substratum.md`:225 | `papers/SM.md`:801: the deconfined phase "required for the perturbative matching to be valid"; :803–811 | DS; whether the nonperturbative phase affects the coupling predictions is open (U-3) | scope narrowing is possible for the structural results; the coupling question waits for RO-10 | SM, Substratum `.tex`/`.pdf` |
| F-27, U-5 | `papers/SM.md`:1036 ($\sin^2\theta_{13}$ coefficient used to determine $A_1$) | :1034 (path sum resting on the open $1/d$ normalization, :944) | DA; which route is load-bearing for "independent of Condition 2" (:1026) is not stated | recovery note, or a statement of the load-bearing route | — |
| F-28, U-6 | `papers/SM.md`:1048: "The natural-normalization choice $b_{23} = 1$"; :1056 | SM footnote ᶠ; appendix-a:96 name only Condition 2 | DA; normalization not derived | listing the choice among the open links needs no new result; a derivation is RO | appendix-a:96 / FULL:5620 |
| F-30, U-7 | `papers/SM.md`:1152: "The matching scale is derived"; :1172 ("a representation-theoretic structural identity") | :1160, :1196, :1215 ("empirical fitting on a moderately-restricted set"), :1219 | DS; analytical K open | recovery note on K | — |
| M-33 / U-10 | `papers/Main.md`:704: "quantitative predictions"; with :76, :20, :660–674 | not yet fixed: the paired passage "is to be fixed by the trace" (`LEDGER-r5.md` §U, U-10) | MC or LC, depending on the trace | LC-3 below (the Main-independence trace) | Main `.tex`/`.pdf` |
| D6 | `book/ch19-open-problems.md`:178: no obligation to derive η_B | Part 4 (#914 comment 6877420015) requires accounting for "other claimed downstream consequences" | scope; planning record against manuscript | owner question Q6 (`LEDGER-r5.md` §12) | FULL:5325 |
| D11 | `papers/SM.md`:1526: the full quantitative prediction "is open work" | `book/ch19-open-problems.md`:184–188: CP phases "solution-specific inputs"; no longer "an unmet derivation obligation" | DA | Q6: which statement is the anchor is undecided (ledger §F.1, MC column "SM:1526 or ch19:184–188") | FULL lines for ch19:184–188, to locate |

### 1.6 Proposed order (proposal)

1. **MC-1** (book direct contradictions). The paper anchors already state the careful form, so each
   correction is narrow and needs no new science. D7, D8 and F-32 assert as derived what SM states is
   not derived (SM:543, :801, :468). The lessons register records that the book has both lagged and
   led the papers (`AGENTS.md`, lessons register, first item).
2. **MC-2** (paper direct contradictions). Same reasoning. F-2's book mirror (ch03:26, FULL:891) moves
   with Structure in this unit, not in MC-1, so that the mirror follows its anchor.
3. **MC-3**, one unit per paper (Substratum, GR, SM, Structure), then the book and citation items. The
   per-paper grouping keeps each PR's propagation to one paper's mirrors and artifacts.
4. **MC-4** (revision differences), which needs only the current values chosen.
5. **MC-5**, each only after the item it waits for.

MC-1 and MC-2 touch disjoint files apart from FULL, so the order between them is a preference, not a
dependency. Nothing in Part 1 depends on Part 3 except MC-5.

**Authorization Part 1 needs.** For each unit: owner authorization of a correction unit, an
accountable Issue, and later a separate integration decision (§1.0). None exists now.

***

## Part 2. Missing ledger coverage (LC)

Ledger work only: reading, classifying and writing rows, then independent review. No manuscript
change and no research.

| ID | Gap | Source of the gap | Proposed closure |
|---|---|---|---|
| LC-0 | `LEDGER-r5.md` is unreviewed | r5 header ("r5 itself has not been reviewed") | A focused independent review of the r4 → r5 diff against `REVIEW-r4.md` S1–S4 and N1–N7, before any queue decision relies on r5 |
| LC-1 | **T-6**: Structure's level hierarchy and placements, and its Born test (`papers/Structure.md`:98–198, 892–954) has no row | `LEDGER-r5.md` §F, "Missing coverage still outstanding"; audit §4.5 T-6 (U, O, T) | Add rows: the hierarchy as a classification scheme (class per source); the placements, cross-referenced to F-17 (the :179 against :191–192 contradiction stays an MC); the Born test with its T flag (audit §4.5 notes "the Born form is in the definition of Q_fb (Main:14)") |
| LC-2 | **U-1**: whether Structure coverage is complete | §U, U-1: "Whether coverage is complete is for a re-audit" | After LC-1, a focused re-audit of Structure only, against T-1 to T-17 |
| LC-3 | **U-10**: Main's independence (Main:76, :20, :660–674, :704) | §U, U-10; audit observation after §4.5 | A read-only trace under the Code Review Rules' Main-independence rule: for each passage, illustration, stated input or dependency; fix the paired companion passage. Its outcome decides whether U-10 is MC (MC-5) or LC |
| LC-4 | **U-9 / K-9**: the "direct computation … R ≈ ε" (`book/ch19-open-problems.md`:244; FULL:5391) has no record cited | §U, U-9; audit §8 K-9 | A read-only search of `verification/` and `papers/` for the computation's record. Found: cite it at its stated scope. Not found: record the absence; the computation itself is RO-10's group |
| LC-5 | Material read at reduced depth: book ch13–17 derivations behind C-BIO (B1–B14, F1–F12); ch13 §13.6 (B3's S label unchecked); SM:960–966; Main §3.4 and GR §3.3 proof bodies; Structure §13.1.1.1 and §14.7–§14.9 | audit §1 ("Every count below is therefore a lower bound") and §10 | One bounded pass per area, ordered by substantive physical content: ch13 §13.6 first (it decides F-34's B3 row), then the reduced-depth proof bodies |
| LC-6 | Kernel identifiers not checked against `verification/lean-manuscript-census.json`, including the directional witnesses of the equivalence displays (audit F-16) and the question at G-9 | audit §10, "Kernel and census" | A read-only census lookup; no Lean build |
| LC-7 | Mirror lists in the ledger are incomplete: D8's FULL mirror is :2894 and :2896 (ch10:88 mirrors at :2896, found by exact line match) | this pass, §1.1 | Correct the D8 mirror cell in the next ledger revision |
| LC-8 | J-1/J-2 (§F.5) name an owner question (Q2) but no accountable Issue; M1–M9 (§10) name none | `LEDGER-r5.md` §F.5, §10 | Record the accountable Issue in the ledger once the owner names one (Part 3, RO-4 and RO-6); the ledger names none itself |

**Proposed order (proposal).** LC-0, then LC-1 and LC-7 (ledger r6), then LC-2, LC-3, LC-4 and LC-6
(each read-only and independent of the others), then LC-5.

**Authorization Part 2 needs.** The ledger expansion and coverage audit are authorized under #914
comment 6877871344, condition 7 ("This approval authorizes the proposed ledger expansion and coverage
audit after the r2 review"), and #914 comment 6877420015, item 2 ("reading, analysis, writing and
independent review only"). LC-0, LC-1 and LC-7 appear to fall inside that scope. Whether a second
audit pass (LC-2), the Main-independence trace (LC-3) and the further reads (LC-4 to LC-6) are covered
is not stated in either record: **owner question**.

***

## Part 3. Research obligations (RO)

### 3.0 The mandatory obligations, and what is already running

**Mandatory obligations** are the Level A rows of `LEDGER-r5.md` §L.A, each UO:
- **A-QM**: inclusion QM ⊆ OI + E on one common realization, and the sector equivalence for a
  physically justified C;
- **A-BELL**: BELL-QSET, H-Bell and Tsirelson selection;
- **A-GR**: GR ⊆ OI on the same substratum and observer;
- **A-REAL**: one common physical realization satisfying the necessary premises jointly (Part 4 and
  joint satisfiability; §9, §10).

Their sources: #914 comments 6875046763, 6875548603 and 6877420015; #1169 comment 6876591512.

**Already authorized work, not ranked here and not gated by this proposal.** The emphasis "must not
make it a new prerequisite for already authorized Bell, gravity or mechanism work" (#914 comment
6878200172). These continue under their own records:
- **Mechanism.** MECH-1 (#1169 body table): "ready for authorized paper source selection; a
  qualifying physical lead remains the gate for candidate derivation"; owner scope #1169 comment
  6714000230 and writer activation 6714078965. It advances A-QM and A-BELL through M2 and M3
  (`LEDGER-r5.md` §10).
- **Bell.** #868 comment 6874036684: "Next step, authorized as paper-only": a full independent review
  of BS r2, and drafting the `SB-L3.md` extract with its reviews. It advances A-BELL.
- **Gravity.** #873 / #1275: G3 units 1, 2(a) and B_G are completed paper-only units (#873 comments
  6863416405, 6865179466, 6872004336). The QB5(a) preregistration is frozen at `8dd0de90` (#873
  comment 6872998421); its execution is not authorized (RO-2 below).
- **Selection.** #1143: SEL-ACCESS-1 focused confirmation (#1143 body) and the Codex target-neutral
  discriminator (#1143 comment 6863602000).
- **Carrier.** #1007 LA-GAP: "ready (owner activation …)", paper-only, writer `writer-1007`; "its
  remaining checks … are computations, which c.6642603567 does not authorize" (#1007 body).
- **QCD / Yang–Mills.** #1063: "the paper-only Yang–Mills source review: ready", PO-1102 workstream E
  (#1063 body). It stays at its recorded tier (below).

### 3.1 Criteria and evidence

Criteria, in the order given: (1) how many mandatory obligations a unit advances; (2) how decisively it
tests a candidate; (3) whether it is ready, as recorded on GitHub.

| Unit | Advances (Level A; ledger rows) | Decisiveness | Readiness and authorization on GitHub |
|---|---|---|---|
| RO-1 S-J with S-A | A-QM, A-BELL, A-REAL (3) | Specifies the condition every sector and Bell-set test is stated relative to; not itself a test | S-J: not ready (undetermined); not authorized. S-A: no planning row found |
| RO-2 QB5(a) execution | A-GR, A-REAL (2): §9 QM–CC and GR–CC; B-CC-2; M6 in part | Decisive for its question: a frozen, independently reviewed decision rule with green controls | #873 ready; execution not authorized |
| RO-3 EXACT carrier inventory | A-QM, A-REAL (2): J-3, J-4, M5, B-QM-8 | Decides whether J-3 and J-4 are conflicts of the target or only of one fixed finite carrier | EXACT: not ready (undetermined); not authorized |
| RO-4 Linearity (J-1, J-2) | A-BELL, A-REAL (2): B-BELL-4, B-BELL-5, SM §3.1 | Needs owner question Q2 first; then fixes preserved controls (§A.29) | no accountable Issue named |
| RO-5 #1211 next unit | A-REAL (1): §9 QM–SM; Q9 | Bounded audit | #1211 ready; unit 2 not authorized or scoped |
| RO-6 M1 interface lift | A-QM, A-GR, A-REAL (3); blocks five branches (§10 M1) | No candidate exists to test | no single accountable Issue; #914 O-IF-SELECT blocked |
| RO-7 to RO-10 downstream | one branch each | various | below |

**What the evidence shows.** On criterion 1, RO-1 (and RO-6, which has no startable unit) ranks first.
On criteria 2 and 3, RO-2 ranks first: it is the only unit with a frozen decision rule, and the only
one whose start needs nothing but an owner authorization. **The evidence therefore does not put the
recommended emphasis first on every criterion.** The proposed order below puts RO-1 first because
criterion 1 was given first and because no sector or Bell-set test can be decisive before C is
stated. It also proposes that RO-2 not wait for RO-1: they need different writers, and the owner's
emphasis is "not execution order" (#914 comment 6878200172). If only one new authorization is given,
the owner chooses between reach (RO-1) and readiness and decisiveness (RO-2).

### 3.2 Proposed ranking (proposal)

**RO-1. Sector condition C: confinement (S-J) with closure within C (S-A). Paper-only specification.**
- *Obligations advanced.* A-QM (the sector equivalence "for a physically justified C"), A-BELL
  (BELL-QSET is stated "for the physically justified OI sector C", #1060 body, question 3), A-REAL.
  Ledger: §L.A A-QM, A-BELL; §12 Q7 (is H-Bell the route to C's recorded exclusion?).
- *Recorded planning.* S-J (#1169 comment 6878199016): Tier Foundational; Prerequisites, Readiness
  "undetermined pending owner decision"; Authorization "not authorized"; status source "open; no
  result on `main` establishes it". S-A: no planning row was found in #1169's body or its 229
  comments, or in #914's body or 75 comments. It is named as an obligation in #1169 comment
  6877981234 ("Kept separate from S-A, closure within C") and in #914 comment 6878200172. #1169's
  labels: `tier: foundational`, `readiness: partly ready`.
- *Concrete next unit.* A paper-only specification: state C as a condition on the underlying model
  with its consequences for experiment families (#1169 comment 6876591512, answer 1); list each
  candidate physical ground for confinement to C, with its source on `main`, whether it is a premise,
  derived or newly proposed, and its §A.29 controls. It carries #1060's constraint that C "may not be
  chosen by testing whether the resulting correlations match quantum predictions" (#1060 body).
- *Why it outranks the alternatives.* Widest reach among startable units (three Level A rows). The
  sector directions (#914 comment 6875548603) and BELL-QSET are stated relative to C, so their tests
  are not decisive until C is stated. The owner records S-J and EXACT as determining "whether the
  central physical explanation succeeds" (#1169 comment 6878199016).
- *Needed before it can start.* Owner decisions on S-J's prerequisites, readiness and authorization; a
  planning row for S-A (§A.45 rule 6); a designated writer; and a check that no active item with a
  different writer writes the same question (§A.45 rule 3). The Codex discriminator on #1143 (comment
  6863602000: "the smallest target-neutral restriction … that excludes the explicit reversible
  PR/supraquantum countercontrol") overlaps this question.
- **(proposal)** S-J readiness → `ready` for this paper-only unit only; S-A receives a planning row
  under #1169.

**RO-2. G3 offset coupling: execute the frozen QB5(a) preregistration.**
- *Obligations advanced.* A-GR and A-REAL, in part. Ledger: B-CC-2 (CD[G3, open]); §9 QM–CC
  ("undetermined") and GR–CC; §10 M6. It does not decide the covariant field equation (B-GR-6, UO) or
  discharge A-GR.
- *Recorded planning.* #873 body: Tier "High (provisional)"; Prerequisites "none recorded"; Readiness
  "ready"; Authorization "not authorized". Unit records: QB5(a) authorized as a paper-only source
  audit (#873 comment 6872004336, "QB5 | Authorize (a)"); F designated, "I designate 8dd0de90 as F;
  execution needs separate authorization" (#873 comment 6872998421); the final check found "All
  controls are green" and returned "ACCEPT FOR FREEZE" (#873 comment 6872959810). A finding for the
  owner: #873 comment 6600178826 says the planning attributes of its obligations "are kept in
  #1074", while the body carries its own block.
- *Concrete next unit.* Execution of QB5(a) at F under its frozen rule, by its designated writer, with
  the review chain the preregistration names.
- *Why it ranks here.* Most decisive and most ready of all units; its verdict comes from a frozen rule
  that "must apply equally to the corpus's own metric-dependent source terms and the disputed
  vacuum-offset coupling" (#873 comment 6872277416). It ranks below RO-1 only on reach.
- *Needed before it can start.* One owner execution authorization recorded on #873. Nothing else is
  recorded as missing.

**RO-3. Exactness (EXACT): which results depend on one fixed finite total carrier.**
- *Obligations advanced.* A-QM (exact inclusion), A-REAL. Ledger: J-3 ("known not to, on one fixed
  finite carrier, under the factorization interface of `papers/Main.md`:558 (unboundedness
  imported)"), J-4 ("undetermined on a completion"), §10 M5, B-QM-8, and Q5.
- *Recorded planning.* EXACT (#1169 comment 6878199016): Tier Foundational; Prerequisites, Readiness
  "undetermined pending owner decision"; Authorization "not authorized". Related: #1007, Tier
  Foundational, LA-GAP ready and paper-only, other SUBSTATE-1 work "undetermined pending owner
  decision (Q-D …)"; #872, "High (provisional)", "blocked: finite reconstruction", "not authorized";
  "#872's narrower scope does not cover all of exactness" (#1169 comment 6877981234).
- *Concrete next unit.* A paper-only inventory: every ledger result that uses one fixed finite total
  carrier (A1 recurrence and C-PRED-8; B-QM-8; B-QM-21; B-QM-28; B-BH-3, B-BH-4 and A.8's cycle
  averages; P-indivisibility at `papers/GR.md`:585), with what is known of each on an admitted
  carrier. A recorded countercontrol already exists: on a countable carrier, recurrence of every state
  does not give a common visible return time (#872 comment 6526240419, research-only, not on `main`).
- *Why it ranks here.* It decides whether two of the four recorded joint-satisfiability conflicts bind
  the target. It ranks below RO-1 on reach, and below RO-2 on readiness.
- *Needed before it can start.* Owner answer to Q5 (which carrier is admitted), or a scope that
  tabulates per candidate carrier; owner decisions on EXACT's prerequisites, readiness and
  authorization; coordination with `writer-1007` (#1007) and #872.
- **(proposal)** EXACT prerequisites → "owner answer to Q5".

**RO-4. Linearity: global A5 against the preparation-indexed Bell route and SM §3.1 (J-1, J-2).**
- *Obligations advanced.* A-BELL, A-REAL. Ledger: J-1, J-2 (§F.5); B-BELL-4, B-BELL-5; §9 Bell–SM;
  Q2.
- *Recorded planning.* No accountable Issue is named for J-1 or J-2 (`LEDGER-r5.md` §F.5 gives only
  "Q2"). #1060 (H-Bell): Tier High; Prerequisites O-K2; "blocked: O-K2"; "not authorized".
- *Concrete next unit.* After Q2 is answered: a paper-only list of the A5-dependent results to serve as
  preserved controls under §A.29 (Q2 names the wave equation, Stage 2(b), harmonic boundary modes and
  "the eight located uses in round H-D").
- *Why it ranks here.* Two Level A rows, but its first step is an owner question, not a test.
- *Needed before it can start.* Q2; an accountable Issue (§A.45 rule 6). **(proposal)** The owner names
  one.

**RO-5. Cross-branch QM–SM trace: #1211 unit 2.**
- *Obligations advanced.* A-REAL (§9 QM–SM, "undetermined"); Q9.
- *Recorded planning.* #1211 body: Tier Foundational; Readiness "ready"; Authorization "**unit 1
  only**". Unit 1 accepted at r5, "ACCEPT WITH NITS"; "The ACCEPT authorizes nothing further" (#1211
  comment 6742071797).
- *Concrete next unit.* Not scoped on GitHub. Its finding FI-1 ("nothing on `main` supplies a
  non-monomial admissible operator on the configuration carrier", same comment) is M2, which MECH-1
  already addresses.
- *Why it ranks here.* One Level A row, and its next question overlaps authorized mechanism work.
- *Needed before it can start.* A scope and an owner authorization.

**RO-6. Observer-interface lift (M1).**
- *Obligations advanced.* A-QM, A-GR, A-REAL; §10 M1 blocks QM, SM, GR, cosmology and CC, more branches
  than any other mechanism.
- *Recorded planning.* No single accountable Issue is named in the ledger (§10). Nearest: #914
  O-IF-SELECT, "High (provisional; existing O-PHASE tier)", "blocked: no qualifying candidate in the
  bounded checked record" (#914 body).
- *Concrete next unit.* None can start: there is no candidate to test.
- *Why it ranks here.* Its reach is the largest, but nothing is ready. **(proposal)** The owner names an
  accountable Issue, so the obligation is tracked (§A.45 rule 6).

**RO-7 to RO-10. Downstream and branch-local obligations: kept below the shared gaps.** "The audit does
not yet justify promoting QCD or another downstream branch ahead of the shared foundational gaps"
(#914 comment 6878781541). No tier or readiness change is proposed for any of them.
- **RO-7, SM flavour** (U-4 to U-8): the $1/d$ amplitude (B-SM-FLAV-9), the $b_{23} = 1$
  normalization (B-SM-FLAV-6), the analytical K (B-SM-FLAV-3), and the $O(\lambda^3)$ route or exact
  diagonalization for Cond 2 (B-SM-FLAV-10). No accountable Issue named in the ledger.
- **RO-8, energy shell and W1** (§10 M9; B-GR-7): blocks GR, cosmology, CC and BH. No accountable Issue
  named in the ledger. It is shared, and is a candidate for an owner-named Issue.
- **RO-9, observer genericity** (U-2): whether C2 and C4 fail for typical bijections.
- **RO-10, QCD and nonperturbative questions** (U-3; B-QCD-5, B-QCD-6, B-QCD-8; K-9 / U-9): #1063, Tier
  "Exploratory"; the paper-only Yang–Mills source review is ready under PO-1102 workstream E;
  integration is "blocked: #872" (#1063 body). Q14 (`LEDGER-r5.md` §12) asks whether the mass gap,
  confinement and the hadron spectrum are Part 4 obligations or recorded scope limits.

### 3.3 Proposed planning changes, all marked (proposal)

None takes effect without a recorded owner decision.
1. S-J readiness → `ready` for the RO-1 paper-only specification only (§3.2, RO-1).
2. A planning row for S-A under #1169 (RO-1).
3. EXACT prerequisites → "owner answer to Q5" (RO-3).
4. An accountable Issue for J-1 and J-2 (RO-4), for M1 (RO-6) and for M9 (RO-8).
5. One accountable Issue per MC unit (Part 1, §1.0).

No tier change is proposed. No change is proposed for #1063 or any other downstream item.

**Authorization Part 3 needs.** Each new unit (RO-1, RO-3, RO-4, RO-5) needs readiness, a recorded
owner authorization, a designated writer and no conflicting writer (§A.45 rule 3). RO-2 needs one
execution authorization. Any new premise, mechanism or selection principle is judged under §A.29
(§A.45 rule 5). Integration and publication are each separate decisions (§A.45 rule 7).

***

## Owner questions this proposal raises

1. Which MC units, if any, to authorize, and in what order (§1.6)? Each needs an accountable Issue.
2. Whether LC-2 to LC-6 fall within the existing ledger authorization (Part 2).
3. Whether to authorize RO-1 and RO-2 together, or which first (§3.1).
4. Q2 and Q5 (`LEDGER-r5.md` §12), which RO-4 and RO-3 wait for.
5. Where #873's planning attributes live: its body, or #1074 (#873 comment 6600178826).
6. MECH-1's writer: the #1169 body row names "Claude Code sole writer", while the body's coordination
   note says "Claude is paused as a writer" and the 2026-11-08 Claude assignment "is superseded for
   **new work only**" (#1169 body). This proposal does not resolve it.

## Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #914 comments 6875046763, 6875548603, 6877420015, 6877871344, 6877908458, 6878200172, 6878781541; #1169 comments 6876591512, 6877981234, 6878199016 | The obligations and guidance the proposal is organized by | Provenance: owner records quoted for scope; no scientific claim rests on them |
| Planning blocks and comments of #868, #873, #872, #914, #1007, #1060, #1063, #1143, #1169, #1211 | Recorded tier, readiness and authorization in Part 3 | Provenance: planning records (§A.45 rule 1) |
| #872 comment 6526240419 | The countable-carrier countercontrol named in RO-3 | Provenance only: a research-only paper result not on `main`; RO-3 cites it as motivation, not as support |
| QB5(a) preregistration at `8dd0de90` on #1275 | RO-2 | Provenance: a frozen record not on `main`; no claim here rests on its content |
| `LEDGER-r5.md`, `LEDGER-r4.md`, `REVIEW-r4.md`, `COVERAGE-AUDIT-r4.md`, `REVIEW-AUDIT-r4.md` (drafts, not on `main`) | The findings and rows the proposal lists | Provenance: every manuscript passage quoted here is cited by its line on `main` at `dfeec843` |

Every manuscript passage cited in this proposal is a line of a file on `main` at `dfeec843`.
