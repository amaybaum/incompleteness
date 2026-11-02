# Corpus consistency for the Introduction's topics (audit step 4, corpus-wide)

Mapper C. Corpus at `eae01647`; Introduction at `4a260ca9`. Machine-readable rows: `consistency.json`. Sites are `file:line@eae01647`; `[FULL:n]` is the byte-identical mirror line in `book/The-Incompleteness-of-Observation-FULL.md`.

Each row gives the conflicting or incomplete formulations, the authoritative anchor (the most rigorous statement, not the most detailed), its severity, whether it touches the Introduction, and a proposed resolution. Discrepancies outside the Introduction are corpus findings for separate correction; nothing here edits the corpus. The early signals S1–S13 of PROOFS-README.md are each resolved into a row, and #939's ħ and θ₀ corrections were re-checked corpus-wide (CON-40).

**Counts.** 48 rows: 1 high, 15 medium, 31 low, 1 informational. 23 touch the Introduction (as a site, or because the Introduction relies on the conflicting source). Rows on lines #939 edited: 6.

## Findings that touch the Introduction

- **CON-01 (high).** GR Theorem A.8 counts initial *configurations* with the B|R bipartition aligned to them — exactly the setting in which GR:833–835 shows H-scramble fails for every bijection. The conditional result is vacuous as stated; GR:835 assigns the failure only to A.7's proof. The Introduction reports A.8's 'all but an exponentially negligible fraction of initial conditions' without saying this.
- **CON-42 (medium).** Intro L106: 'no unconditional implication holds among' the three notions. Main:334 says only that none 'is asserted', and Main:606 states that Markov implies P-divisible, so P-indivisibility implies memory at some time.
- **CON-25 (medium).** Intro L84 calls the Pinsker-bound probes 'exact'; `c4_backflow_probes.py` evaluates the information quantities in floating point with 1e-12 tolerances (Main:170 says 'Certified exactly').
- **CON-24, CON-41, CON-43, CON-26 (low).** 'Minimal model' with six hidden states beside a two-state 'smallest' realization; the general Theorem 3 is kernel-only (Main §2.3 proves the uniform-prior special case); the cited routed-readback declaration uses a frozen spelling, with a storage-time variant available; the fixed-dimension counterexample used only uniform priors.
- **Faithful against conflicting corpus (the corpus is wrong, the Introduction right):** CON-02 (book: BH paradox 'resolved'), CON-04 (Λ 'dissolution' headings), CON-06 (GR §6.2 asserts Einstein's equations while G3 is open), CON-10 (QM 'derived'), CON-12 and CON-44 (Born exponent framing), CON-21 (bijectivity a 'lemma'), CON-22 (finiteness of S from Lemma 1).

## Anchors by topic

| Topic | Authoritative anchor | Rows |
|---|---|---|
| Embedded observation (finiteness, bijectivity, measure) | Main:62 Remark (status of the early commitments) and Main:708 posit ledger; kernel `CanonicalMeasure` | CON-21, CON-22 |
| Finite-horizon correspondence | Main §3.4 Theorem (finite-horizon equivalence) with kernel `finite_horizon_equivalence`; Main:758 for the meaning of 'equivalence' | CON-16, CON-46, CON-20, CON-28 |
| Characterization theorem | Main:516 with proof Main:608 (prose; not formalized) | CON-17, CON-18, CON-19, CON-27 |
| Hidden memory | Main §3.4 Theorem (unavoidable hidden predictive memory), kernel `HiddenMemory` for the joint-law form | CON-25, CON-26, CON-42 |
| Recurrence and indivisibility | kernel `pIndivisible_of_rooted_identity_return_of_overlap`; Main:137 for readback ⟹ indivisibility | CON-23, CON-24, CON-41, CON-43, CON-38 |
| Quantum emergence, operational QM | GR §3.3 (kernel characterization and substratum-source form); Main:562, :624 | CON-09, CON-10, CON-11, CON-13, CON-14, CON-15, CON-30, CON-46, CON-47, CON-48 |
| Born rule | Main:534 (exponent not selected; origin a frontier item) | CON-12, CON-44 |
| Bell | Main §3.3 Bell ceiling theorem; H-Bell at Substratum:132 | CON-45 |
| Relating evolution / phase locking | Main:624; GR:182 for H-BG's open status | CON-29, CON-47 |
| Cosmological constant | GR §6.2 (:358): descriptive distinction established, dissolution conditional on G3 | CON-04, CON-05, CON-06, CON-07, CON-08 |
| Black-hole information | GR App. A.7 (:833–:845) with ch07:161 (conservation is a premise) | CON-01, CON-02, CON-03 |
| Outside the Introduction's topics | SM §7.6 table (:1255–:1300); #939 CHANGE-NOTE | CON-31–CON-37, CON-39, CON-40 |

## Early signals S1–S13

S1 → CON-17. S2 → CON-29. S3 → CON-30. S4, S6 → CON-34. S5 → CON-32 (extended: SM's abstract, a line #939 edited, also says 0.23σ). S7, S8 → CON-33 (S8's 105.74 MeV row is now distinctly labelled by #939; the chain-table label remains ambiguous). S9 → CON-35. S10 → CON-21. S11 → CON-36. S12, S13 → CON-37.

## #939 (ħ framing and θ₀)

Checked by grep over the core corpus at eae01647: every θ₀ figure is 0.222225 ± 0.000006 / 0.001% / 0.4σ (no '0.02%' remains); every Theorem 23 / Stage 3 restatement carries H-slope; no 'derives ħ' remains outside the sites #939's AUDIT classed CORRECT or CONTEXT-OK; the 'seven relations' count appears nowhere. Residues found on #939-edited lines or tables: CON-32 (SM:14 '0.23σ'), CON-33 (ch06:217–218 labels), CON-35 (ch06:12 'twenty-two'), CON-04 (ch00:97, SM:1576 'dissolution … at the descriptive level'). Optional alignment: CON-08.

## Summary table

| ID | Sev. | Topic | Kind | Touches Intro | #939 line |
|---|---|---|---|---|---|
| CON-01 | high | black-hole information | conflicting statement / vacuous hypothesis | yes |  |
| CON-02 | medium | black-hole information | conflicting statement (status) | yes |  |
| CON-03 | low | black-hole information | status label | yes |  |
| CON-04 | medium | cosmological constant | conflicting statement (headings and summaries) | yes | yes |
| CON-05 | low | cosmological constant | missing assumption | no |  |
| CON-06 | medium | cosmological constant | conflicting statement (open step asserted) | yes |  |
| CON-07 | medium | cosmological constant / OI's reach | conflicting statement | no |  |
| CON-08 | low | cosmological constant (ħ framing, #939) | #939 residue candidate | no |  |
| CON-09 | medium | quantum emergence and operational QM | overstated summary | no |  |
| CON-10 | medium | quantum emergence and operational QM | overstated reach | yes |  |
| CON-11 | medium | quantum emergence (measurement) | overstated status | no |  |
| CON-12 | medium | Born rule | conflicting statement | yes |  |
| CON-13 | low | quantum emergence (continuous time) | conflicting statement | no |  |
| CON-14 | low | operational QM | outdated framing | no |  |
| CON-15 | low | what remains open (operational QM) | missing assumption | yes |  |
| CON-16 | low | finite-horizon correspondence | title stronger than theorem | yes |  |
| CON-17 | low | finite-horizon correspondence (Characterization theorem) | status surface gap | no |  |
| CON-18 | low | finite-horizon correspondence (Characterization theorem) | ambiguous reference | no |  |
| CON-19 | medium | finite-horizon correspondence (Characterization theorem) | conflicting proof structure | no |  |
| CON-20 | low | finite-horizon correspondence (realization) | understated restatement | yes |  |
| CON-21 | medium | embedded observation (bijectivity) | missing qualifier | yes |  |
| CON-22 | low | embedded observation (finiteness) | conflicting statement | yes | yes |
| CON-23 | low | recurrence and indivisibility | misattributed hypothesis | no |  |
| CON-24 | low | recurrence and indivisibility (examples) | unsupported 'minimal' | yes |  |
| CON-25 | medium | hidden memory (probe claims) | exactness overclaim | yes |  |
| CON-26 | low | hidden memory (variational question) | method narrower than statement | yes |  |
| CON-27 | low | finite-horizon correspondence (testability) | conflicting statement | no |  |
| CON-28 | low | finite-horizon correspondence (all-time scope) | outdated open item | yes |  |
| CON-29 | low | relating evolution (phase locking) | missing status | no |  |
| CON-30 | low | quantum emergence (appendix B restatements) | scope/kind mismatch | no |  |
| CON-31 | low | dark sector (adjacent to Λ) | overstated status | no |  |
| CON-32 | medium | #939 residue (SM numerics) | numerical discrepancy | no | yes |
| CON-33 | low | #939 residue (lepton mass labels) | label ambiguity | no | yes |
| CON-34 | low | SM numerics (prediction status) | numerical/status discrepancy | no |  |
| CON-35 | low | SM/GR counts | count discrepancy | no | yes |
| CON-36 | low | GR universality theorem | theorem without written proof | no |  |
| CON-37 | low | labels and hypotheses | label collision / unstated hypotheses | yes |  |
| CON-38 | low | recurrence (C-conditions) | overstated consequence | no |  |
| CON-39 | medium | editorial (appendix B) | drafting residue | no |  |
| CON-40 | info | #939 check (ħ framing and θ₀) | verification summary | no | yes |
| CON-41 | low | recurrence and indivisibility (Theorem 3's source) | kernel result with no manuscript statement | yes |  |
| CON-42 | medium | hidden memory vs indivisibility (three notions) | conflicting statement | yes |  |
| CON-43 | low | recurrence and indivisibility (routed readback) | kernel predicate differs from the clause it transcribes | yes |  |
| CON-44 | medium | Born rule (exponent framing) | conflicting framing | yes |  |
| CON-45 | low | Bell (H-Bell) | hypothesis stated with different clauses | yes |  |
| CON-46 | low | finite-horizon correspondence (scope) | missing scope qualifier | no |  |
| CON-47 | low | relating evolution (trajectory-law biconditional) | equivalence assembled, not one kernel statement | yes |  |
| CON-48 | low | operational QM (Theorem 4's setting) | setting stated incompletely | no |  |

## Rows

### CON-01 — black-hole information (high; conflicting statement / vacuous hypothesis; signal: B3-1 (mapper); new)

**Sites.**

- `papers/GR.md:817@eae01647` — Theorem A.8: φ acts on B∪R with Σ_E = C_B × C_R as one energy shell; under H-scramble, the time average equals the Page value for all initial conditions except a small fraction
- `papers/GR.md:827@eae01647` — proof decomposes the bijection of the configuration set Σ_E into cycles and averages over configurations s ∈ C_j
- `papers/GR.md:841@eae01647` — 'The fraction of initial conditions on Σ_E that land on a bad cycle …' — initial conditions are configurations
- `papers/GR.md:833@eae01647` — every finite bijection acting on a definite configuration visits only product states, S(ρ_R)=0 at the aligned bipartition
- `papers/GR.md:835@eae01647` — 'H-scramble fails for every bijection in the setting of Theorem A.7's proof, a definite initial configuration with the bipartition aligned to the configuration coordinates'
- `book/appendix-a-prediction-status.md:111@eae01647` — G11 Page curve: class C; 'Scrambling, decoupling, proper-shell value open' [FULL:5648]
- `book/ch19-open-problems.md:72@eae01647` — Page curve 'under H-scramble and H-decouple …, neither of which is established' — no statement that H-scramble fails in A.8's setting [FULL:5232]
- `papers/Introduction.md:162@4a260ca9` — 'For all but an exponentially negligible fraction of initial conditions, … equals the Page value …' (Intro, 4a260ca9)

**Anchor.** `papers/GR.md:833@eae01647` — GR:833 proves (by the long-cycle example and its generalization) that every orbit of a definite configuration is product across the aligned bipartition; the B|R bipartition of A.8 is aligned with C_B × C_R, and A.8's proof counts initial configurations. The failure is therefore in A.8's own setting, not only in A.7's.

**Touches the Introduction:** yes. Intro L162 reports A.8's conclusion 'for all but an exponentially negligible fraction of initial conditions' and separately says H-scramble fails for definite configurations; it does not say that A.8's counted initial conditions are exactly those configurations, so the reader is not told that the conditional result is vacuous in the setting as stated.

**Proposed resolution.** GR (separate correction): restate A.8 over an ensemble of initial pure states (initial superpositions) or a non-aligned bipartition, recount the excluded fraction over that ensemble, and move the 'fails' sentence to A.8 itself ('H-scramble fails for every bijection in the setting of this theorem when initial conditions are configurations'); mirror the caveat in appendix A G11 and ch19:72. Introduction: replace 'For all but an exponentially negligible fraction of initial conditions' by a statement that A.8 counts initial configurations, for which H-scramble fails, so its conclusion requires initial superpositions or a non-aligned bipartition, which is open.

### CON-02 — black-hole information (medium; conflicting statement (status); signal: B3-2 (mapper); new)

**Sites.**

- `book/ch07-gravity.md:110@eae01647` — 'The framework resolves the paradox at the level of information preservation' [FULL:1989]
- `book/ch19-open-problems.md:20@eae01647` — '## 19.2 Problems resolved' — section containing 19.2.6 the BH information paradox [FULL:5180]
- `book/ch19-open-problems.md:72@eae01647` — 'Framework status. Resolved at the level of information preservation; the Page curve is conditional' [FULL:5232]
- `book/ch09-universality.md:125@eae01647` — Tier 1 prediction table row 'BH information preserved' with 'Page curve conditional …' in the empirical-match column [FULL:2605]
- `book/ch19-open-problems.md:334@eae01647` — 'Preserved; Page curve conditional' [FULL:5494]

**Anchor.** `book/ch07-gravity.md:161@eae01647` — ch07:161: the conservation claim 'rests on bijectivity as a premise'; GR App. A.7 leaves the Page curve conditional. Preservation is a premise, not a resolved problem or a prediction.

**Touches the Introduction:** yes. Intro L156–L158, L162, L175 say conservation holds because bijectivity is a premise and 'the black-hole information problem is not resolved'. The book's status surfaces say 'resolved'. The Introduction is faithful to the anchor; the book overstates.

**Proposed resolution.** ch07:110, ch19:72 and their FULL mirrors: 'Information is conserved by the bijectivity premise; recovery by an observer (the Page curve) is conditional on H-scramble and H-decouple; the paradox is not resolved.' Move 19.2.6 out of 'Problems resolved' or retitle §19.2. ch09:125: remove from the predictions table (a premise is not a prediction) or relabel the row.

### CON-03 — black-hole information (low; status label; signal: B1/B4 (mapper))

**Sites.**

- `verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:3@eae01647` — 'Status: exploratory research, unreviewed for adoption.'
- `verification/programmes/black-hole-information/bh01_access_v1/review/REVIEW.md:1@eae01647` — independent review of 587d4196 (BLOCK, wording only), with rechecks
- `verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:3@eae01647` — 'Status: exploratory research under OI-BH-1, internally reviewed (review/REVIEW.md), not adopted.'
- `papers/Introduction.md:267@4a260ca9` — [BHa] … 'unpublished research record, internally reviewed'

**Anchor.** `verification/programmes/black-hole-information/bh01_access_v1/review/REVIEW.md:1@eae01647` — the review exists and the report's own text refers to 'the independent review of 587d4196'; 'unreviewed for adoption' means not adopted into the manuscripts, which BHb's header says plainly.

**Touches the Introduction:** yes. The Introduction's reference entry ('internally reviewed') is correct; the BHa header reads as contradicting it.

**Proposed resolution.** No Introduction change. Record-side: a frozen research record is not edited (§A.42 item 4); if wanted, a successor note may say 'internally reviewed; not adopted', matching BHb.

### CON-04 — cosmological constant (medium; conflicting statement (headings and summaries); signal: B3-3, B1, B4 (mappers); new)

**Sites.**

- `papers/GR.md:326@eae01647` — '## 6. Dissolution of the Cosmological Constant Problem'
- `book/ch07-gravity.md:163@eae01647` — '## 7.7 Dissolution of the cosmological constant problem' [FULL:2042]
- `book/ch18-beyond.md:142@eae01647` — 'The first dissolution: the cosmological constant.' [FULL:4960]
- `book/ch19-open-problems.md:20@eae01647` — '## 19.2 Problems resolved' (contains 19.2.2 CC) [FULL:5180]
- `book/ch00-introduction.md:97@eae01647` — '… the dissolution of the cosmological constant problem at the descriptive level' [FULL:333]
- `papers/SM.md:1576@eae01647` — 'the dissolution of the cosmological constant problem at the descriptive level'
- `book/ch02-substratum.md:120@eae01647` — 'The cosmological constant problem is not resolved by tuning; … the apparent 10^122 discrepancy is the compression ratio' (no condition) [FULL:763]

**Anchor.** `papers/GR.md:358@eae01647` — GR §6.2: 'the descriptive-level distinction is established and the dissolution is conditional' on the G3 coupling theorem; ch19:38 and GR:24 say the same.

**Touches the Introduction:** yes. Intro §4 (L142–L152) and L178: 'proposal … not a resolution'. Faithful to the anchor; the corpus headings and three summaries are stronger.

**Proposed resolution.** Headings: 'The cosmological constant: descriptive distinction and conditional dissolution' (GR §6, ch07 §7.7, ch18:142). Summaries: 'the descriptive distinction behind a conditional dissolution' (ch00:97, SM:1576 — both lines edited by #939 for ħ, so the change belongs to a follow-up), ch02:120 add 'conditional on the open coupling step (G3)'. Retitle ch19 §19.2.

### CON-05 — cosmological constant (low; missing assumption; signal: B3-5 (mapper))

**Sites.**

- `papers/GR.md:573@eae01647` — 'The framework denies that the absolute zero-point sum gravitates, because gravity operates at the logically prior classical level (§6.2).'
- `papers/GR.md:581@eae01647` — 'Whether the offset sources curvature is not settled by this invariance; it is the coupling question that §6.2 leaves open at Level G3.'
- `papers/GR.md:583@eae01647` — 'On the geometry-first proposal of §6.2, conditional on the open coupling step, the dissolution applies …'

**Anchor.** `papers/GR.md:581@eae01647` — the next paragraph and GR §6.2 make the claim conditional on G3.

**Touches the Introduction:** no.

**Proposed resolution.** GR:573: 'On the geometry-first proposal (§6.2), conditional on the open coupling step, the absolute zero-point sum does not gravitate'.

### CON-06 — cosmological constant (medium; conflicting statement (open step asserted); signal: new)

**Sites.**

- `papers/GR.md:344@eae01647` — 'Spacetime geometry is part of the classical substratum (Lemma 2): the metric evolves via Einstein's equations before the trace-out.'
- `book/ch07-gravity.md:177@eae01647` — same sentence [FULL:2056]
- `papers/GR.md:166@eae01647` — 'Four routes … converge on the same dynamics; … the dynamics is over-determined rather than underived' (given the emergent cone, matter content and spin-2 mode)

**Anchor.** `papers/GR.md:12@eae01647` — GR's dependency ladder: G3, 'covariant field equations with conservation/Bianchi structure and the continuum limit, open'; GR §6.2 (:358) makes the coupling a G3 theorem not yet proved.

**Touches the Introduction:** yes. Intro L144 cites [GR §6.2] for 'covariant field equations derived from the substratum … are open'. GR §6.2's own opening asserts the metric obeys Einstein's equations at the classical level, so the cited section states both.

**Proposed resolution.** GR:344 and ch07:177: 'the metric belongs to the classical substratum; its covariant field equations and their source coupling are the open Level-G3 step'. GR:166: add that the four routes' inputs (single cone, spin-2 bound state, no extra light modes) are open obligations, so the convergence is conditional.

### CON-07 — cosmological constant / OI's reach (medium; conflicting statement; signal: B4 (mapper))

**Sites.**

- `book/appendix-c-objections.md:317@eae01647` — 'the derivations are explicit and the proofs are complete' [FULL:6563]

**Anchor.** `papers/GR.md:12@eae01647` — G3 open; the ledger has 56 GAP rows among 122 core statements (PROOFS-README); GR:679 says a theorem-style proof of the universality theorem 'has not been written out'.

**Touches the Introduction:** no.

**Proposed resolution.** appendix-c:317: 'the derivations are explicit, and the status of each — proved, conditional or open — is recorded with it'.

### CON-08 — cosmological constant (ħ framing, #939) (low; #939 residue candidate; signal: B3-4 (mapper); #939 check)

**Sites.**

- `papers/GR.md:352@eae01647` — '(iii) Uniqueness of ħ. The emergent action scale is determined by the boundary geometry (§3.2).'
- `book/ch07-gravity.md:185@eae01647` — same requirement (iii) [FULL:2064]
- `book/ch07-gravity.md:305@eae01647` — '… a self-consistency condition that fixes only the ratio ε/√σ = 2 l_p, not an independent determination of ħ' [FULL:2184]

**Anchor.** `papers/GR.md:310@eae01647` — #939's anchor: the calibration fixes only ε/√σ and is conditional on H-slope; boundary-only dependence (Step 2) is not H-slope-conditional.

**Touches the Introduction:** no.

**Proposed resolution.** #939's AUDIT classed GR:352 and ch07:185 CONTEXT-OK, reading 'determined' as boundary-only dependence (its sense D1–D2). The sentence is used as one of three requirements forcing the geometry-first ordering, so the owner may prefer 'depends only on boundary geometry (§3.2, Step 2)', which is true without H-slope. Optional; not an error under #939's reading.

### CON-09 — quantum emergence and operational QM (medium; overstated summary; signal: new)

**Sites.**

- `papers/GR.md:330@eae01647` — 'Part I delivers QM on a finite-dimensional Hilbert space.'

**Anchor.** `papers/Main.md:624@eae01647` — Main: finite observable-law representability is established; exact finite operational QM is characterized conditionally by (i)–(v), none supplied by bare OI.

**Touches the Introduction:** no.

**Proposed resolution.** GR:330: 'Part I delivers the exact fixed-basis unitary/Born representation on a finite-dimensional Hilbert space; the operational theory is reached under the completion conditions of §3.3.'

### CON-10 — quantum emergence and operational QM (medium; overstated reach; signal: new; B1 (ch01:261))

**Sites.**

- `papers/Substratum.md:420@eae01647` — 'the co-derivation of quantum mechanics and general relativity'
- `papers/Structure.md:1294@eae01647` — 'the constructive derivation of quantum mechanics'
- `book/ch01-observation.md:261@eae01647` — 'quantum mechanics … is the dynamics that our specific kind of observation produces' [FULL:605]
- `book/ch02-substratum.md:120@eae01647` — 'The Standard Model gauge group is not chosen; it is derived. The three-generation structure is not posited; it is forced.' [FULL:763]

**Anchor.** `papers/GR.md:228@eae01647` — GR §3.3: the characterization is 'a classification of the completions compatible with embedded observation, not a derivation of quantum mechanics from it'; oi_alone_not_qm (kernel); G3 open (GR:12); the gauge-group reading is conditional on H-link (ch19:337) and the reconstruction on the open Lemma 24.1 (ROADMAP:64).

**Touches the Introduction:** yes. The Introduction (L28, L172) claims no derivation of QM, faithful to the anchor; these corpus sites claim one.

**Proposed resolution.** Substratum:420 'the joint structural account of the quantum representation and the conditional gravitational sector'; Structure:1294 'the constructive representation theorem'; ch01:261 'quantum mechanics is the representation every such observer's laws admit; whether the full operational theory follows depends on completion conditions OI does not imply'; ch02:120 'derived conditionally on H-link … forced on the single-copy branch'.

### CON-11 — quantum emergence (measurement) (medium; overstated status; signal: new)

**Sites.**

- `book/ch19-open-problems.md:64@eae01647` — Measurement problem: 'Framework status. Dissolved. … There is no collapse — only Bayesian updating …' [FULL:5224]
- `book/ch19-open-problems.md:333@eae01647` — table: 'Dissolved (Bayesian updating)' [FULL:5493]
- `papers/Main.md:666@eae01647` — 'The Everettian measure problem dissolves'
- `papers/Main.md:672@eae01647` — Wigner's friend: 'Under C1–C4 applied to (V_F, S∖V_F), Friend's reduced description is quantum-mechanical.'
- `papers/Main.md:668@eae01647` — '… which resolves the standard nested-observer paradoxes'

**Anchor.** `papers/Main.md:632@eae01647` — Main §3.4 Remark (scope) (iii): Lüders updating transcribes Bayesian conditioning only for the represented diagonal sector; the general update for noncommuting interventions belongs to the instrument algebra, reached only under (i)–(v).

**Touches the Introduction:** no.

**Proposed resolution.** ch19:64/:333: 'Dissolved for the represented fixed-basis statistics; the general update belongs to the operational completion (conditional)'. Main:672: 'Friend's reduced law admits the fixed-basis quantum representation (§3.4)'.

### CON-12 — Born rule (medium; conflicting statement; signal: new)

**Sites.**

- `papers/Main.md:220@eae01647` — 'The Born rule is the equilibrium distribution of the indivisible process [11, 12].'
- `papers/Main.md:345@eae01647` — routes table: 'Born rule | Equilibrium of indivisible process'

**Anchor.** `papers/Main.md:534@eae01647` — Main §3.4 Remark: p=|U|^2 is part of the definition of Q_fb and the exponent is not selected; Main:666: 'The equilibrium-of-the-cycle reading is the cosmological realization's mechanism proposal rather than a theorem'; ch18:34 the same.

**Touches the Introduction:** yes. Intro L66 and L134 (exponent not selected; its origin open) cite [Main §3.4] and agree with the anchor; Main §3.1 states the contrary without qualification.

**Proposed resolution.** Main:220: 'In the source's reading the Born rule is the equilibrium distribution of the indivisible process [11, 12]; here it is part of the representation's definition and its exponent is not selected (§3.4).' Main:345: 'Equilibrium reading (imported; a proposal here)'.

### CON-13 — quantum emergence (continuous time) (low; conflicting statement; signal: new)

**Sites.**

- `papers/Main.md:220@eae01647` — 'The Schrödinger equation arises from the differentiability of U(t).'

**Anchor.** `papers/Main.md:268@eae01647` — Main §3.2: 'any continuous one-parameter interpolation is additional structure, chosen rather than derived'; GR:292 and kernel continuous_extension_not_unique (RegionLimit.lean:296).

**Touches the Introduction:** no.

**Proposed resolution.** Main:220: 'Given a chosen continuous interpolation U(t) (§3.2), the Schrödinger form follows from its differentiability.'

### CON-14 — operational QM (low; outdated framing; signal: B4 (Main:758); new)

**Sites.**

- `papers/Main.md:99@eae01647` — Layer 4: 'interventions (classical comb closed, §3.4; quantum instruments open)'
- `papers/Main.md:210@eae01647` — operational completion 'partially established by the one-step coherence theorem … and otherwise open'
- `papers/Main.md:348@eae01647` — 'Level three (open): coherent preparation, noncommuting interventions, and the instrument algebra'
- `papers/Main.md:758@eae01647` — 'It is the remaining operational-lifting problem'

**Anchor.** `papers/Main.md:562@eae01647` — Main:562: existence side 'settled by the operational-completion characterization'; 'what remains is orientation and the physical question of which conditions the substratum supplies, not the size of the family and not a lifting theorem'; GR §3.3 (:218, :260–:264) adds that the stated substratum does not supply (iv).

**Touches the Introduction:** no.

**Proposed resolution.** Main:99, :210, :348, :758: replace 'open'/'lifting problem' by 'characterized exactly by conditions (i)–(v) [GR §3.3]; the stated substratum does not supply continuous state-mixing control; whether a physical substratum does is open'.

### CON-15 — what remains open (operational QM) (low; missing assumption; signal: new)

**Sites.**

- `papers/GR.md:216@eae01647` — operational-completion characterization: 'an operational theory … which finite outcome families of linear maps are available' (matrix carriers)
- `papers/Main.md:562@eae01647` — 'the compositional target is settled as a characterization'
- `verification/ROADMAP.md:68@eae01647` — P1 'K — pre-quantum kinematics: from field-neutral operational premises to the complex matrix kinematics the finite characterization assumes' OPEN

**Anchor.** `verification/ROADMAP.md:68@eae01647` — ROADMAP records that the characterization assumes complex matrix kinematics and that deriving it is open; no manuscript states this (grep 'matrix kinematics', 'pre-quantum' in papers/ and book/: none).

**Touches the Introduction:** yes. Intro L114 states Theorem 4's setting as 'finite outcome families of linear maps' without saying the complex matrix kinematics is assumed (see CMP-17).

**Proposed resolution.** GR §3.3 and Main §3.4: one clause after the characterization: 'The characterization takes complex matrix kinematics as given; deriving it from field-neutral premises is open.'

### CON-16 — finite-horizon correspondence (low; title stronger than theorem; signal: B4 (mapper))

**Sites.**

- `papers/Main.md:2@eae01647` — title 'The Equivalence of Quantum Mechanics and Embedded Observation'
- `papers/Methodology.md:585@eae01647` — same title in [Main] reference
- `papers/Structure.md:1416@eae01647` — same title in [Main] reference
- `papers/Introduction.md:261@4a260ca9` — [Main] reference carries the same title

**Anchor.** `papers/Main.md:758@eae01647` — Main:758 defines the phrase as 'exact bidirectional equivalence of finite observable stochastic laws and their quantum representations'; GR §3.3 (:224) 'bare finite OI ⇏ QM'.

**Touches the Introduction:** yes. The Introduction must cite the title as it is; its body (L12, L28, L172) is faithful to Main:758.

**Proposed resolution.** Owner decision: keep the title with Main:758 as its scope statement, or retitle (e.g. '… The Finite-Law Equivalence of Quantum Representations and Embedded Observation'). If retitled, update Methodology:585, Structure:1416 and the Introduction's reference.

### CON-17 — finite-horizon correspondence (Characterization theorem) (low; status surface gap; signal: S1)

**Sites.**

- `papers/Main.md:516@eae01647` — '**Characterization theorem.**' (lower-case 'theorem'): no census row, no LEDGER row
- `book/appendix-b-derivations.md:454@eae01647` — Theorem B.7.6 restates it [FULL:6221]

**Anchor.** `papers/Main.md:608@eae01647` — the proof: both directions proved in prose, neither formalized; supporting theorems have ledger rows.

**Touches the Introduction:** no. The Introduction does not name it (CMP-10).

**Proposed resolution.** Tooling: let tools/proof_census.py match '**Characterization theorem.**' or rename the head '**Theorem (characterization).**', then add the ledger row (level GAP or P, assumptions '(T) for clause (i); time-homogeneity').

### CON-18 — finite-horizon correspondence (Characterization theorem) (low; ambiguous reference; signal: new)

**Sites.**

- `papers/Main.md:72@eae01647` — 'the equivalence of §3.4 quantifies over none of them' (C1–C4)
- `papers/Main.md:76@eae01647` — 'the characterization's equivalence runs over those three' (C1, C3, C4)

**Anchor.** `papers/Main.md:516@eae01647` — two theorems in §3.4: the finite-horizon equivalence (no C-conditions) and the Characterization theorem, whose (iii) carries C1, C3, C4.

**Touches the Introduction:** no. Intro L86 ('diagnostics …, not hypotheses of Theorem 1') names Theorem 1 and is unambiguous.

**Proposed resolution.** Main:72: 'the finite-horizon equivalence of §3.4 quantifies over none of them'.

### CON-19 — finite-horizon correspondence (Characterization theorem) (medium; conflicting proof structure; signal: new (cf. S3))

**Sites.**

- `book/appendix-b-derivations.md:457@eae01647` — Theorem B.7.6 proof structure: forward direction 'follows from Lemmas B.7.1–B.7.5 combined with the Stinespring construction' [FULL:6224]
- `book/appendix-b-derivations.md:459@eae01647` — 'The reverse direction (necessity) is per-condition … C1, C3, and C4 are individually necessary' [FULL:6226]
- `book/appendix-b-derivations.md:422@eae01647` — Lemma B.7.4, whose status is 'borne out by explicit slow-bath models'; 'the precise functional form is model-dependent rather than a universal inequality' [FULL:6189]

**Anchor.** `papers/Main.md:608@eae01647` — Main's proof: (iii)⟹(ii) is the readback lemma (Pinsker bound, Main:167); (ii)⟹(iii) is existence by process dilation (Main:496). Per-condition necessity does not give existence, and B.7.4 is not a proved lemma.

**Touches the Introduction:** no.

**Proposed resolution.** appendix-b:457–459 and FULL: cite the readback lemma for (iii)⟹(ii) and the process-dilation construction for (ii)⟹(iii); relabel B.7.4 as a 'Remark (model evidence)' or drop it from the proof chain.

### CON-20 — finite-horizon correspondence (realization) (low; understated restatement; signal: new (B1 I-071))

**Sites.**

- `papers/Introduction.md:56@4a260ca9` — 'For a law with rational probabilities, a realization whose hidden prior is independent of x_0 also exists'

**Anchor.** `papers/Main.md:498@eae01647` — Main:498: the response-table form reproduces the full joint for arbitrary real kernels; Main:715 status ledger 'arbitrary-prior form via the response-table extension'.

**Touches the Introduction:** yes. Introduction only; see CMP-22.

**Proposed resolution.** See CMP-22.

### CON-21 — embedded observation (bijectivity) (medium; missing qualifier; signal: S10)

**Sites.**

- `papers/Methodology.md:235@eae01647` — '… finiteness-per-moment, and bijectivity follow as lemmas'
- `papers/Methodology.md:253@eae01647` — 'Everything else in the foundational layer is a lemma: … determinism, finiteness-per-moment, and bijectivity.'

**Anchor.** `papers/Main.md:708@eae01647` — Main posit ledger (iii): the determinism recovery closes its hidden-sector margin with one empirical input, 'so bijectivity is part-empirical rather than a pure lemma'; Main:62: the bijective substratum is a representation choice; Methodology:146 states the empirical input at the derivation.

**Touches the Introduction:** yes. Intro L20 ('the reversible representative …, motivated by observed near-unitarity') follows the anchor; Methodology's summaries contradict it.

**Proposed resolution.** Methodology:235 and :253: 'bijectivity (with one empirical input at the hidden-sector margin, §4.4)'.

### CON-22 — embedded observation (finiteness) (low; conflicting statement; signal: B1 (Main:46); new)

**Sites.**

- `papers/Main.md:46@eae01647` — 'it acts on a finite S (Lemma 1); finiteness, not the dynamics, is the load-bearing commitment'
- `papers/Main.md:48@eae01647` — Lemma 1 proves finiteness of C_V only, citing holographic bounds as 'independent support'
- `papers/Main.md:684@eae01647` — 'invoking holographic bounds at the foundational layer would be circular' (line edited by #939)

**Anchor.** `papers/Main.md:62@eae01647` — Main:62 and :113: total finiteness of S is a posit (ledger item (ii)); Lemma 1 is visible finiteness only; the kernel Finiteness.finiteness (Finiteness.lean:153) proves it as a conditional with the finite-mode premise 'argued for nowhere' (ledger note).

**Touches the Introduction:** yes. Intro L20 says finiteness of all of S is posited, following Main:62.

**Proposed resolution.** Main:46: 'it acts on a finite S (Lemma 1 for the visible sector; the total-finiteness posit, §4.5, for the rest)'. Main:48/:684: state one ground for Lemma 1 (either the axiom-level argument, with holographic bounds as a downstream check, or the boundary-mode premise).

### CON-23 — recurrence and indivisibility (low; misattributed hypothesis; signal: new)

**Sites.**

- `papers/Main.md:131@eae01647` — 'The theorem requires only bijective dynamics (Lemma 3) and non-trivial coupling (C1).'
- `papers/Main.md:717@eae01647` — status ledger: '… bare-recurrence form from (C1) alone at t_R'
- `book/appendix-b-derivations.md:418@eae01647` — B.7.3 proof: the non-permutation witness 'is NOT a consequence of C1' [FULL:6185]
- `book/appendix-b-derivations.md:420@eae01647` — B.7.3 remark: 'the recurrence argument uses C1 and finiteness alone' [FULL:6187]

**Anchor.** `papers/Main.md:115@eae01647` — the §2.3 theorem's hypothesis is 'T is not a permutation matrix' (uniform prior); Main:74 and :143: a non-permutation T is a sufficient witness of (C1), not equivalent (delayed-revival family).

**Touches the Introduction:** no. Intro Theorem 3 (L92) uses the rooted overlap hypothesis and is unaffected.

**Proposed resolution.** Main:131 and :717, appendix-b:418–420: 'requires only bijective dynamics and a non-permutation one-step matrix (a sufficient witness of (C1))'.

### CON-24 — recurrence and indivisibility (examples) (low; unsupported 'minimal'; signal: B5 (mapper))

**Sites.**

- `papers/Main.md:178@eae01647` — '### 2.4 Explicit Construction: A Minimal Model' (six hidden states)
- `book/ch01-observation.md:273@eae01647` — 'The minimal such game is the coin-and-die model of §1.5 dealt onto a table' — the die has six states (ch01:135), the burn card two [FULL:617]
- `papers/Introduction.md:98@4a260ca9` — 'a minimal model of Theorem 3 with six hidden states … and a two-card game, the smallest realization of Theorem 3'

**Anchor.** `papers/Main.md:421@eae01647` — Main:421: φ(v,h)=(v⊕h,h) on two visible and two hidden states is P-indivisible; the card game has |C_V|=|C_H|=2. Two hidden states are necessary for any overlap, so 2×2 is minimal and the six-state model is not.

**Touches the Introduction:** yes. Intro L98 and B.1's heading call the six-state model 'minimal' and the card game 'smallest' in adjacent clauses.

**Proposed resolution.** Main:178, ch01:273 and Intro B.1/L98: 'A worked model' (or 'an explicit model'); keep 'smallest' for the 2×2 card game. ch01:273: say the card game simplifies the coin-and-die model to two hidden states.

### CON-25 — hidden memory (probe claims) (medium; exactness overclaim; signal: B1 (mapper))

**Sites.**

- `papers/Main.md:170@eae01647` — Pinsker readback lemma: '(Certified exactly on gap families, … in c4_backflow_probes.py.)'
- `papers/oi_lattice_code/foundations/c4_backflow_probes.py:23@eae01647` — conditional mutual information accumulated as float(p)*log2(float(...))
- `papers/oi_lattice_code/foundations/c4_backflow_probes.py:52@eae01647` — assertions with tolerance abs(I-1.0)<1e-12
- `papers/Introduction.md:84@4a260ca9` — Pinsker bound 'proved on paper, with exact probes'; Conventions L30 define an exact probe as 'an exhaustive computation in exact rational arithmetic'

**Anchor.** `papers/oi_lattice_code/foundations/c4_backflow_probes.py:11@eae01647` — laws are exact Fractions, but the CMI and the bound are evaluated in floating point with tolerances (AGENTS: floating-point evidence is not certification).

**Touches the Introduction:** yes. Intro L84 calls these 'exact probes' under its own definition (L30).

**Proposed resolution.** Main:170: 'certified numerically (exact laws, floating-point information quantities, tolerance 1e-12)'. Intro L84: 'proved on paper, with numerical probes'. Optionally make the probe exact by comparing exp-free forms or using interval bounds.

### CON-26 — hidden memory (variational question) (low; method narrower than statement; signal: B4 (mapper))

**Sites.**

- `papers/Main.md:594@eae01647` — 'The reading in which the infimum ranges over realizations of FIXED hidden dimension is FALSE: at (2,3) the minimum equals M_t for only one of fifteen distinct processes'
- `papers/oi_lattice_code/foundations/memory_probes.py:25@eae01647` — ensemble(): joint prior uniform, F(1, nV*nH), for every permutation
- `papers/Introduction.md:185@4a260ca9` — '(the fixed-dimension form is false)'

**Anchor.** `papers/Main.md:510@eae01647` — a realization carries its own fixed hidden prior as datum (Main:60, :510); the probe minimizes over bijections at one prior only.

**Touches the Introduction:** yes. Intro L185 relies on the counterexample.

**Proposed resolution.** Main:594: 'over realizations of fixed hidden dimension with uniform prior'. Mapper B4 reports a recheck over arbitrary priors with 14 of 16 failing (so the conclusion stands); I did not reproduce that recheck, and its count differs from Main's 'one of fifteen' — the record should state the prior class and the count it computes.

### CON-27 — finite-horizon correspondence (testability) (low; conflicting statement; signal: B1 (mapper))

**Sites.**

- `papers/Main.md:704@eae01647` — '… no experiment falsifies the theorem itself'
- `papers/Main.md:706@eae01647` — 'Laboratory tests of the characterization theorem may be possible in tabletop systems'

**Anchor.** `papers/Main.md:704@eae01647` — the theorem is mathematical; what is testable is the physical identification.

**Touches the Introduction:** no. Intro L22, L176 (no test established) follow the anchor.

**Proposed resolution.** Main:706: 'Laboratory tests of the physical identification …'.

### CON-28 — finite-horizon correspondence (all-time scope) (low; outdated open item; signal: B4 (mapper))

**Sites.**

- `papers/Main.md:618@eae01647` — Remark (consolidation): '(a) exact gluing for recurrent target families' open
- `verification/lean-mathlib/OIBridge/RootedClassificationAllTime.lean:192@eae01647` — finiteRootedRealizable_iff_pper: rooted family finitely realizable at every time ⟺ periodic

**Anchor.** `verification/lean-mathlib/OIBridge/RootedClassificationAllTime.lean:192@eae01647` — kernel settles the rooted-family case in both directions; no manuscript cites it.

**Touches the Introduction:** yes. Intro open problem (3) (L185) repeats Main:618.

**Proposed resolution.** Main:618: add the rooted-family classification with its scope (rooted maps, not multi-time laws) and register the anchor (§A.35); then narrow Intro open problem (3) (CMP-23).

### CON-29 — relating evolution (phase locking) (low; missing status; signal: S2)

**Sites.**

- `papers/Main.md:224@eae01647` — phase-locking lemma: 'Assume … H-BG' (no open status)
- `papers/Main.md:336@eae01647` — 'the phase-locking lemma (§3.1), under its classification hypothesis H-BG, determines Ĥ_eff …'
- `papers/Main.md:634@eae01647` — 'under H-BG …, its Hamiltonian is determined by the transition data up to the stated gauge freedom'
- `papers/Structure.md:150@eae01647` — 'conditional on H-BG'
- `papers/Substratum.md:284@eae01647` — 'conditional on H-BG'
- `book/ch03-structural-realism.md:70@eae01647` — 'conditional on … H-BG' [FULL:946]

**Anchor.** `papers/GR.md:182@eae01647` — GR:182 and appendix-b:444 scope: comparison with Bekir–Golomb open; the unsigned kernel premise BGIntegerClassification is false; ROADMAP P2 'Sign-aware integer classification' OPEN (:72).

**Touches the Introduction:** no.

**Proposed resolution.** At first use in Main (:224) and in Structure/Substratum: 'H-BG (open: its unsigned formal premise is false and the sign-aware classification is not established; GR §3.3)'.

### CON-30 — quantum emergence (appendix B restatements) (low; scope/kind mismatch; signal: S3; B5 (mapper))

**Sites.**

- `book/appendix-b-derivations.md:92@eae01647` — Theorem B.2.5: 'P-indivisibility of the substratum dynamics (under C1–C4) implies CP-indivisibility' [FULL:5859]
- `book/appendix-b-derivations.md:408@eae01647` — Lemma B.7.1 'Partition relativity' — different content from Main's lemma of that name
- `book/appendix-b-derivations.md:302@eae01647` — B.6.2 6=3⊕2⊕1 'on the internal components' without the H-link qualifier

**Anchor.** `papers/Main.md:326@eae01647` — Main:326 scopes CP-indivisibility to the permutation-dilation (diagonal-preserving) family; C1–C4 play no role in the proof (which B.2.5's own proof confirms).

**Touches the Introduction:** no. Intro L106 follows Main:326.

**Proposed resolution.** appendix-b:92: 'For the permutation-dilation family {Φ_t}, P-indivisibility of the population process implies CP-indivisibility'. B.7.1: rename or align with Main:86. B.6.2: add 'the six geometric links; the physical reading is conditional on H-link'.

### CON-31 — dark sector (adjacent to Λ) (low; overstated status; signal: new)

**Sites.**

- `book/ch19-open-problems.md:116@eae01647` — 'Framework status. Derived (total budget …)' [FULL:5276]
- `book/ch19-open-problems.md:339@eae01647` — 'Dark sector budget | … | Derived (total budget)' [FULL:5499]
- `book/ch09-universality.md:126@eae01647` — Tier 1 prediction 'Dark sector budget ~95% | concordance' [FULL:2606]

**Anchor.** `papers/GR.md:358@eae01647` — GR §6.2 item (4): 'the fraction is 1−Ω_B by construction …, partly definitional'; ch07:297 and appendix A G9 (:110) 'partly definitional'.

**Touches the Introduction:** no.

**Proposed resolution.** ch19:116/:339, ch09:126: 'partly definitional (1−Ω_B by construction); the matter-like/dark-energy split is the tested content'.

### CON-32 — #939 residue (SM numerics) (medium; numerical discrepancy; signal: S5)

**Sites.**

- `papers/SM.md:14@eae01647` — abstract: 'the Wolfenstein A = √(2/3) to 0.23σ' (line edited by #939 for θ₀, A left)
- `papers/Juno.md:140@eae01647` — 'agreeing with the PDG value A = 0.826 ± 0.012 at 0.23σ'
- `papers/SM.md:859@eae01647` — 'Observed: A = 0.826 ± 0.012. Match: 0.8σ (1.2%)'
- `papers/SM.md:1263@eae01647` — §7.6 table: 0.8σ
- `book/ch06-matter-content.md:141@eae01647` — 0.8σ, 1.2% [FULL:1667]

**Anchor.** `papers/SM.md:1263@eae01647` — (0.826−0.8165)/0.012 = 0.79σ.

**Touches the Introduction:** no.

**Proposed resolution.** SM:14 and Juno:140: '0.8σ'.

### CON-33 — #939 residue (lepton mass labels) (low; label ambiguity; signal: S7, S8)

**Sites.**

- `book/ch06-matter-content.md:189@eae01647` — m_e | Koide(Q, θ0; m_τ) | 0.51098 MeV (observed m_τ)
- `book/ch06-matter-content.md:217@eae01647` — m_e | Koide(Q, θ0; m_τ) | Layer 1 | 0.505 MeV | 1.2% (chain m_τ = 1755 MeV) [FULL:1743]
- `book/ch06-matter-content.md:218@eae01647` — m_μ | Koide(Q, θ0; m_τ) | 104.4 MeV [FULL:1744]
- `papers/SM.md:983@eae01647` — m_e | Koide(θ0, m_τ) | 0.505 MeV
- `papers/SM.md:1269@eae01647` — m_e (from m_τ) | 0.51098 MeV
- `papers/SM.md:1316@eae01647` — 'Wolfenstein A² | 0.6667 | 0.683 | 1.2%' (A² deviation is ≈2.4%)
- `papers/SM.md:1317@eae01647` — 'sin²θ13 | 0.0225 | 0.0224 | 0.4%' vs SM:1276 0.02195 ± 0.00056 (1.01σ)

**Anchor.** `papers/SM.md:1269@eae01647` — #939 O6-A: 'make each table state what it computes'; the chain rows use the chain's predicted m_τ=1755 MeV, but carry the same label as the observed-m_τ rows.

**Touches the Introduction:** no.

**Proposed resolution.** ch06:217–218 and SM:983–984: label 'Koide(Q, θ0; m_τ^chain = 1755 MeV)'. SM:1316: 2.4% (or quote A). SM:1317: use the NuFIT value and 1.01σ as at SM:1276.

### CON-34 — SM numerics (prediction status) (low; numerical/status discrepancy; signal: S4, S6)

**Sites.**

- `book/appendix-a-prediction-status.md:75@eae01647` — row 6 Wolfenstein A 'Within 1%' (1.2%, 0.8σ) [FULL:5612]
- `book/appendix-a-prediction-status.md:82@eae01647` — row 13 sin²θ13 'Within 1%' (≈2.6%, 1.01σ) [FULL:5619]
- `book/appendix-a-prediction-status.md:90@eae01647` — row 21 m_b 'Within 1σ' (1.2σ by the quoted error) [FULL:5627]
- `papers/Juno.md:346@eae01647` — 'The formula for sin²θ13 is fully derived'
- `papers/Juno.md:417@eae01647` — 'is conditional structural (Layer 1 …)'

**Anchor.** `papers/SM.md:1255@eae01647` — SM §7.6 table values and classes.

**Touches the Introduction:** no.

**Proposed resolution.** appendix A cells: quote the SM §7.6 figures; Juno:346: 'derived at the formula level; classified conditional structural (C)'.

### CON-35 — SM/GR counts (low; count discrepancy; signal: S9)

**Sites.**

- `book/ch06-matter-content.md:12@eae01647` — 'collects the twenty-two predictions' while the §6.8 table has 24 rows (line edited by #939) [FULL:1538]
- `book/ch07-gravity.md:321@eae01647` — 'the ten entries in this chapter's table' vs 'eight gravitational-sector entries' elsewhere [FULL:2200]
- `book/appendix-a-prediction-status.md:94@eae01647` — 'Total: 23' vs SM §7.6 22 rows (explained in text)

**Anchor.** `papers/SM.md:1255@eae01647` — SM §7.6: 22 rows.

**Touches the Introduction:** no. The Introduction states no prediction count.

**Proposed resolution.** ch06:12: 'twenty-four table entries (the twenty-two of SM §7.6 re-sorted, with additions)'; ch07:321: reconcile with appendix A's eight.

### CON-36 — GR universality theorem (low; theorem without written proof; signal: S11)

**Sites.**

- `papers/GR.md:677@eae01647` — 'Theorem (universality of the partition-geometry results)'
- `papers/GR.md:679@eae01647` — 'A formal proof at the level of explicit theorem-style presentation has not been written out in this paper'

**Anchor.** `papers/GR.md:679@eae01647` — the paper's own statement; ledger GAP.

**Touches the Introduction:** no.

**Proposed resolution.** Label it 'Proposition (universality, argued in §3–§6)' or write the proof.

### CON-37 — labels and hypotheses (low; label collision / unstated hypotheses; signal: S12, S13)

**Sites.**

- `papers/Main.md:224@eae01647` — (G1)–(G3) genericity conditions
- `papers/GR.md:12@eae01647` — G1–G4 gravity levels
- `papers/Juno.md:225@eae01647` — Condition 1/2 vs SM 'Cond 2' (SM:1046)
- `verification/ROADMAP.md:71@eae01647` — H-∞ named only in ROADMAP; H-functor, H-tensor, H-pure-seed, H-readout, H-monoidal only in LEDGER backlog

**Anchor.** `papers/GR.md:12@eae01647` — GR's ladder is the term the Introduction uses ('Level G3 of [GR]').

**Touches the Introduction:** yes. Intro L144 writes 'Level G3 of [GR]', unambiguous with 'Level'.

**Proposed resolution.** Rename Main's genericity conditions (e.g. (N1)–(N3)); align 'Cond 2'/'Condition 2'.

### CON-38 — recurrence (C-conditions) (low; overstated consequence; signal: new)

**Sites.**

- `book/ch18-beyond.md:64@eae01647` — 'a system failing one [of C1–C4] has that sector empty — … genuinely described by memoryless classical stochastic dynamics' [FULL:4882]

**Anchor.** `papers/Main.md:76@eae01647` — (C2) lies outside the equivalence; a fast non-mixing bath violates (C2-slow) while (C4) holds (fastbath_probes.py); only failure of persistence (C2-structural) with uniform erosion carries (C4) down (Main §2.3).

**Touches the Introduction:** no.

**Proposed resolution.** ch18:64: 'a system failing (C4) — and with it (C1) or (C3), or record persistence — has that sector empty'.

### CON-39 — editorial (appendix B) (medium; drafting residue; signal: new)

**Sites.**

- `book/appendix-b-derivations.md:280@eae01647` — 'proton charge +1 = 2 Y_u + Y_d + 2·1/2 = 4/3 − 1/3 + 1 = 2... no, let me reorganize.' [FULL:6047]

**Anchor.** `book/appendix-b-derivations.md:282@eae01647` — the next paragraph gives the corrected computation.

**Touches the Introduction:** no. Outside the Introduction's topics; recorded because it is a published-text defect.

**Proposed resolution.** Delete the false start; keep the corrected computation.

### CON-40 — #939 check (ħ framing and θ₀) (info; verification summary; signal: #939)

**Sites.**

- `papers/SM.md:903@eae01647` — θ₀ = 0.222225 ± 0.000006, 0.001%, 0.4σ
- `papers/Substratum.md:184@eae01647` — Stage 3 'Status: Conditional on H-slope …'
- `papers/Substratum.md:192@eae01647` — Theorem 23 ħ clause 'conditional on H-slope'
- `papers/Structure.md:47@eae01647` — 'conditional on H-slope [GR §3.2]'
- `papers/Methodology.md:339@eae01647` — 'conditional on H-slope ([GR §3.2])'
- `book/ch02-substratum.md:110@eae01647` — Stage 3 'conditional on H-slope with the horizon and frame conditions' [FULL:753]
- `book/ch06-matter-content.md:320@eae01647` — eight Category A relations (O2-a) [FULL:1846]

**Anchor.** `verification/audits/manuscript/hbar-theta0-20261026/CHANGE-NOTE.md:1@eae01647` — #939's applied change set.

**Touches the Introduction:** no. The Introduction makes no ħ or θ₀ claim; its [GR] reference title matches GR:1.

**Proposed resolution.** Checked by grep over the core corpus at eae01647: every θ₀ figure is 0.222225 ± 0.000006 / 0.001% / 0.4σ (no '0.02%' remains); every Theorem 23 / Stage 3 restatement carries H-slope; no 'derives ħ' remains outside the sites #939's AUDIT classed CORRECT or CONTEXT-OK; the 'seven relations' count appears nowhere. Residues found on #939-edited lines or tables: CON-32 (SM:14 '0.23σ'), CON-33 (ch06:217–218 labels), CON-35 (ch06:12 'twenty-two'), CON-04 (ch00:97, SM:1576 'dissolution … at the descriptive level'). Optional alignment: CON-08.

### CON-41 — recurrence and indivisibility (Theorem 3's source) (low; kernel result with no manuscript statement; signal: B2 (mapper))

**Sites.**

- `papers/Introduction.md:92@4a260ca9` — Theorem 3 (recurrence and overlap [Main §2.3]): fixed hidden prior, two rows of Γ_s overlap, Γ_n=I ⇒ not P-divisible
- `papers/Main.md:115@eae01647` — Main §2.3 theorem: uniform hidden prior, one-step T not a permutation ⇒ P-indivisible (the special case s=1, uniform prior)
- `verification/lean-mathlib/OIBridge/RecurrenceHorizon.lean:148@eae01647` — pIndivisible_of_rooted_identity_return_of_overlap (general rooted form)

**Anchor.** `verification/lean-mathlib/OIBridge/RecurrenceHorizon.lean:148@eae01647` — the general overlap-and-return form is proved in the kernel; no manuscript states it (grep of papers/ for the identifier and for 'overlap' in §2.3: none).

**Touches the Introduction:** yes. Intro attributes the general form to [Main §2.3], which proves only the uniform-prior one-step case (and uses rooted maps inside the readback theorem's proof, Main:139).

**Proposed resolution.** Main §2.3: state the rooted overlap form with its kernel anchor (and register it, §A.35); until then the Introduction should cite the kernel declaration and 'Main §2.3 for the uniform-prior case'.

### CON-42 — hidden memory vs indivisibility (three notions) (medium; conflicting statement; signal: B2 (mapper))

**Sites.**

- `papers/Main.md:334@eae01647` — Remark (three notions): '… No unconditional implication among the three is asserted here.'
- `papers/Main.md:606@eae01647` — Remark (two notions): 'Markov implies P-divisible (chain factorization), so P-indivisibility is the strictly stronger property'
- `papers/Introduction.md:106@4a260ca9` — 'Three notions are distinct, and no unconditional implication holds among them [Main §3.2, Remark (three notions, kept apart)]'

**Anchor.** `papers/Main.md:606@eae01647` — Markov ⇒ P-divisible (RHP14 Cor. 2.1), so P-indivisibility (2) implies non-Markovianity, hence M_t>0 at some t (1): one unconditional implication holds. Main:334 only declines to assert one; the Introduction says none holds.

**Touches the Introduction:** yes. Intro L106 strengthens Main:334's 'is asserted' to 'holds', which is false for (2)⟹(1) at some time.

**Proposed resolution.** Main:334: 'Apart from (2)⟹(1) at some time — a P-indivisible law is not Markov — no unconditional implication holds among them'. Introduction L106 the same.

### CON-43 — recurrence and indivisibility (routed readback) (low; kernel predicate differs from the clause it transcribes; signal: B2, B5 (mappers))

**Sites.**

- `verification/lean-mathlib/OIBridge/PhysicalC4Discharge.lean:27@eae01647` — 'A recorded discrepancy, not repaired here. The frozen spelling of rootedPosterior …' vs the round's storage-time clause (:29)
- `verification/lean-mathlib/OIBridge/PhysicalC4Discharge.lean:122@eae01647` — routed_forces_indivisible_somewhere (frozen spelling)
- `verification/lean-mathlib/OIBridge/PhysicalC4StorageReadback.lean:256@eae01647` — routedAtStorage_forces_indivisible_somewhere (storage-time spelling)
- `papers/Introduction.md:96@4a260ca9` — 'machine-checked … from a routed-readback form of (C4), in which a visible-history record written into the hidden state is read back later [Main §1.3]'; Appendix A cites routed_forces_indivisible_somewhere

**Anchor.** `verification/lean-mathlib/OIBridge/PhysicalC4StorageReadback.lean:256@eae01647` — the storage-time variant transcribes the manuscript reading (hidden-state law at the storage time); both proofs use only the overlap, so the conclusion is the same.

**Touches the Introduction:** yes. No manuscript names either predicate; the Introduction cites the frozen-spelling declaration for the manuscript's clause.

**Proposed resolution.** Introduction Appendix A: cite routedAtStorage_forces_indivisible_somewhere (PhysicalC4StorageReadback:256) beside or instead of the frozen-spelling theorem.

### CON-44 — Born rule (exponent framing) (medium; conflicting framing; signal: B2 (mapper))

**Sites.**

- `book/ch18-beyond.md:34@eae01647` — 'The open frontier is not a separate choice of probability exponent inside that representation; it is the common coherent operational extension' [FULL:4852]
- `book/ch19-open-problems.md:126@eae01647` — 'the quadratic Born dictionary is part of the equivalent representation, not a separate exponent-selection problem' [FULL:5286]

**Anchor.** `papers/Main.md:534@eae01647` — Main §3.4: the construction 'does not SELECT the quadratic exponent'; 'Why the quadratic functional is the physical one is therefore a frontier item about the dictionary's origin'.

**Touches the Introduction:** yes. Intro L66 and L134 ('the origin of the quadratic Born exponent … is open') follow Main:534; the book says the exponent is not an open question.

**Proposed resolution.** ch18:34 and ch19:126: 'Inside the representation the dictionary is part of the definition; why the quadratic exponent is the physical one is a separate open question (Main §3.4); the coherent operational extension is a second frontier.'

### CON-45 — Bell (H-Bell) (low; hypothesis stated with different clauses; signal: B2 (mapper))

**Sites.**

- `papers/Substratum.md:132@eae01647` — H-Bell: (i) supply ontic parameter dependence, (ii) preserve operational no-signaling, (iii) metric/Ollivier–Ricci stability
- `papers/Main.md:394@eae01647` — H-Bell: the prepared graph family must preserve operational no-signaling and satisfy a curvature/metric convergence condition
- `papers/Introduction.md:136@4a260ca9` — 'the compatibility of that choice with operational no-signalling and the gravitational continuum limit … is the open hypothesis H-Bell'

**Anchor.** `papers/Substratum.md:132@eae01647` — the definition site carries three clauses; Main's two are (ii) and (iii), (i) being the adopted branch itself.

**Touches the Introduction:** yes. The Introduction's two-clause reading matches Main and is compatible with Substratum's (i) as the branch choice.

**Proposed resolution.** Main:394: cite [Substratum §3.3] for the full statement, or add clause (i).

### CON-46 — finite-horizon correspondence (scope) (low; missing scope qualifier; signal: B2 (mapper))

**Sites.**

- `book/ch00-introduction.md:39@eae01647` — 'Quantum mechanics is therefore an exact observer-level representation of the incomplete finite law' [FULL:275]

**Anchor.** `papers/Main.md:758@eae01647` — the exact equivalence is with fixed-basis unitary/Born representations; operational QM needs (i)–(v).

**Touches the Introduction:** no.

**Proposed resolution.** ch00:39: 'The fixed-basis unitary/Born description is therefore an exact representation …'.

### CON-47 — relating evolution (trajectory-law biconditional) (low; equivalence assembled, not one kernel statement; signal: B2 (mapper))

**Sites.**

- `papers/Main.md:624@eae01647` — 'two such data have equal trajectory laws exactly when their visible laws are equal' (kernel: bridge_traj, rooted_eq_iff_slice_eq, realData_traj_stochastic)
- `verification/lean-mathlib/OIBridge/TrackBQfbBridge.lean:276@eae01647` — bridge_traj: equal one-step visible matrix ⇒ equal trajectory laws

**Anchor.** `verification/lean-mathlib/OIBridge/TrackBQfbBridge.lean:180@eae01647` — the converse uses rooted_eq_iff_slice_eq's forward direction after marginalizing trajectory laws to rooted families — an elementary step not stated as a declaration (§A.34: each direction needs its witness).

**Touches the Introduction:** yes. Intro L126 states the two directions separately, with 'forward direction', which is the faithful form.

**Proposed resolution.** Main:624: name the witness for each direction ('⇐ bridge_traj; ⇒ marginalization to rooted families, then rooted_eq_iff_slice_eq (forward)').

### CON-48 — operational QM (Theorem 4's setting) (low; setting stated incompletely; signal: B2 (mapper))

**Sites.**

- `papers/GR.md:216@eae01647` — setting: closed under coarse-graining and outcome-conditioned composition, with a spectator-independent local readout of the ancilla
- `papers/Introduction.md:114@4a260ca9` — setting adds: an available preparation of a uniformly mixed ancilla, which an available operation may follow, and ancilla discard

**Anchor.** `lean:OIBridge/GeneralCarrier.lean:100:exactAll_iff_physical_general` — the kernel's theory structure fixes the fields; condition (v) uses uniform attachment and discard, so GR's prose omits fields the statement needs.

**Touches the Introduction:** no. The Introduction's fuller setting is the better transcription (mapper B2).

**Proposed resolution.** GR:216: add the uniformly mixed ancilla preparation and the discard rule to the stated setting.

## Mapper items folded in

All were re-verified at the cited lines. B1: Main:46 finiteness (CON-22), Methodology bijectivity (CON-21), GR §6 heading (CON-04), ch01:261 (CON-10), Main:704/:706 (CON-27), BH-01 header (CON-03), Main:170 float probe (CON-25). B2: ch00:39 (CON-46), H-Bell clauses (CON-45), GR:216 setting (CON-48), Born framing (CON-44), Main:624 biconditional (CON-47), Main:334 (CON-42), routed readback spelling (CON-43), Theorem 3 kernel-only (CON-41). B3: A.8 setting (CON-01), 'resolved' status (CON-02), dissolution headings (CON-04), GR:352 ħ (CON-08: #939 classed it CONTEXT-OK; kept as optional), GR:573 (CON-05). B4: Main title (CON-16), headings (CON-04), appendix C:317 (CON-07), Main:758 (CON-14), Main:594 probe priors (CON-26; B4's recheck count not reproduced here), BH-01 header (CON-03). B5: minimal model (CON-24), B.2.5 (CON-30), routed-readback spelling (CON-43: no manuscript names either predicate; it touches only the Introduction's Appendix A).
