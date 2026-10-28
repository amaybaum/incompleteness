# SC-37: the cosmological constant and the open coupling step G3

Unit of PR-A (part). Base `main` at `0d917665`; branch `corpus/sc37-g3-conditional`. Line numbers
below are at the base.

## Finding

**C-B2** (the #918 full-corpus audit, confirmed by its verifier), which is FINDINGS **CON-04**,
**CON-05** and **CON-06**, with the in-scope items **CON-07**, **CON-08** (optional, applied) and
**CON-31** of the same PR-A row.

The anchor is GR §6.2 (GR:356): the descriptive distinction between the emergent zero-point sum and
the effective cosmological constant is established; that the zero-point sum does not source
curvature is a coupling statement, which GR's dependency ladder (GR:12) places in the open step G3,
so the dissolution is conditional. Several sentences stated the coupling step, or its consequences,
without that condition.

What GR §6.3 and §8.3 establish is unchanged: the dimensional identity
$\rho_{\rm QFT}/\rho_{\rm classical}\sim S_{\rm dS}$ up to a convention-dependent factor; that a
uniform energy shift changes no visible transition probability; and that two gravitational
completions differing only in the offset share the substratum, partition, reduced law and
calibration.

## Claims corrected

Evidence level of every corrected claim after the edit: the descriptive distinction is a structural
argument (prose derivation, no machine check); the coupling step is open (G3); the dimensional
identity is exact algebra up to the stated convention factor; nothing here is Lean-checked, and no
Lean statement or proof is touched or needed (none of these claims has a kernel counterpart; checked
by grep over `verification/lean`, `verification/lean-mathlib` and the census registry). **Requires
formal change: none.**

### 1. The coupling step asserted as settled (CON-06)

- **Original.** GR:344 "Spacetime geometry is part of the classical substratum (Lemma 2): the metric
  evolves via Einstein's equations *before* the trace-out. The stress-energy sourcing gravity is the
  classical stress-energy of the total microstate … at the classical level, the gravitational field
  equations never encounter the zero-point sum." ch07:177 / FULL:2056 open with the same first clause.
- **Defect.** The covariant field equations and their source coupling are G3, open (GR:12, GR:356);
  the paragraph states them as fact, against GR:356 three paragraphs later.
- **Correction.** "the metric belongs to the substratum, prior to the trace-out, and its covariant
  field equations and their source coupling are the open G3 step. The geometry-first proposal of this
  section is that the stress-energy sourcing gravity is the classical stress-energy …; on that
  proposal, which the coupling step must establish, … never encounter the zero-point sum." ch07:177
  and FULL:2056 take the same first clause; their remainder was already marked as the proposal.
- **Downstream.** Explainer:541 and :543 (Level 1 / Level 2: "The metric tensor evolves via Einstein's
  field equations"; "not a source term in Einstein's equations, because …") rewritten to the same
  conditional form; Explainer:689 (FAQ "Why does gravity see the classical vacuum energy") made
  conditional on the proposal and the open step. GR:362 "But gravity is sourced by the classical
  Hamiltonian" → "On the proposal, gravity is sourced …" (the paragraph's lead sentence already
  carried the condition). GR:166 (the four-route convergence, also named in CON-06) is **not a flaw**:
  it already states "given the emergent cone, matter content, and spin-2 mode" and names each route's
  hypotheses as open obligations; unchanged.

### 2. "Denies that the zero-point sum gravitates" (CON-05)

- **Original.** GR:573 "The framework denies that the *absolute* zero-point sum gravitates, because
  gravity operates at the logically prior classical level (§6.2)." Same form at GR:434 ("The framework
  denies that $\rho_{\rm QFT}$ gravitates (§6.2)"), GR:404 ("§8.3 denies that the emergent zero-point
  sum gravitates absolutely"), ch07:209 / FULL:2088 ("Section 7.7's dissolution denies …"),
  Explainer:579 ("The framework denies that the zero-point energy gravitates").
- **Defect.** Unconditional statement of the open coupling step; GR:581 and :583 in the same section
  state it conditionally.
- **Correction.** "On the geometry-first proposal (§6.2), conditional on the open coupling step, the
  *absolute* zero-point sum does not gravitate …", and the parallel conditional at each listed site.
  GR:575's "applied as a precise principle" (the What-gravitates / What-does-not list of §8.3) now
  says the principle holds on the proposal and is conditional on the same step.
- **Downstream.** GR:454: the dark-sector corollary's predictions are conditional on the ordering
  *and* on the open coupling step (they read "conditional on the same geometry-first ordering" only,
  while GR:12 puts the dark sector in G4, conditional on G3); GR:434's "gravitates at the classical
  level" for $\rho_s$ is placed on the same proposal. Explainer:579 likewise.

### 3. "Predicts the observed value" (C-B2, Explainer)

- **Original.** Explainer:551 "the other predicts the observed value and explains the discrepancy as
  a derived quantity … One predicts the observed vacuum energy and one misses it by $10^{122}$".
- **Defect.** Contradicts Explainer:549 and GR:366: the value is set by initial conditions, "a
  normalization, not a prediction".
- **Correction.** "the other is consistent with the observed value as a normalization and,
  conditional on the open coupling step, reads the discrepancy as a derived quantity"; "One is
  consistent with the observed vacuum energy, as a normalization, and one misses it by $10^{122}$".
  Explainer:625 "only the substrate's value matches observation" → "is of the observed scale".
- **Downstream.** None outside the Explainer: no other corpus site says the framework predicts the
  vacuum-energy value (re-grep below).

### 4. "Dissolution" headings and summaries (CON-04)

- **Original.** GR:326 "## 6. Dissolution of the Cosmological Constant Problem"; ch07:163 / FULL:2042
  "## 7.7 Dissolution of the cosmological constant problem"; ch18:142 / FULL:4960 "**The first
  dissolution: the cosmological constant.**"; ch19:20 / FULL:5180 "## 19.2 Problems resolved";
  ch00:97 / FULL:333 and SM:1576 "the dissolution of the cosmological constant problem at the
  descriptive level"; ch02:120 / FULL:763 "the apparent $10^{122}$ discrepancy is the compression
  ratio Chapter 7 develops" (no condition).
- **Defect.** Headings and summaries state the dissolution without the condition their sections carry.
- **Correction.** GR §6 "The Cosmological Constant: Descriptive Distinction and Conditional
  Dissolution"; ch07 §7.7 the same in sentence case; ch18 "The first conditional dissolution"; ch19
  §19.2 "Problems addressed"; ch00:97 and SM:1576 "the descriptive distinction behind a dissolution of
  the cosmological constant problem conditional on the open coupling step"; ch02:120 "is read as the
  compression ratio Chapter 7 develops, a reading on which the problem dissolves conditional on the
  open coupling step (G3)".
- **Downstream (same claim class, re-grep).** GR:336 "The CC dissolution requires only" → "The
  conditional dissolution of §6.2 requires only"; GR:625 (U3, listed among the *unconditional*
  universality results) said "the $10^{122}$ ratio is a compression ratio, not a failure of
  cancellation", which is the conditional dissolution: now "their $10^{122}$ ratio is, up to a
  convention-dependent factor, the de Sitter entropy (§§6.1, 6.3); that the ratio is a compression
  ratio rather than a failure of cancellation is the dynamical dissolution of (c), conditional on the
  coupling step" (the distinction and the identity stay unconditional). ch18:142 "On that reading the
  ratio is not a fine-tuning failure" and ch18:144, ch19:38 "the two energy scales are not
  commensurable as gravitational sources" gain the condition. ch07:197, :319 / FULL:2076, :2198
  "geometry-first dissolution" → "geometry-first proposal". ch09:243, ch19:366, ch00:101,
  readers-guide:15, Explainer:537, :581, :593 "CC dissolution" → "conditional CC dissolution" (or
  equivalent). ch09:261 "the offset is gauge outright and there is nothing to manage" → "gauge
  outright for every quantum statistic and, conditional on the coupling step, there is nothing to
  manage". appendix-c:349 "Where apparent puzzles turn out to be category errors (cosmological
  constant, …)" → "Where the framework reads apparent puzzles as category errors (the cosmological
  constant, conditional on the open coupling step; …)". Structure:975 "Three of the four — hierarchy,
  cosmological constant, gauge structure — are dissolved" gains "(conditional on that coupling step)"
  for the cosmological constant (the hierarchy and gauge-structure entries are other units' claims and
  are not touched). ch09:257 cited "Chapter 7 §7.6" (the information-paradox section) twice for the
  cosmological-constant levels and the offset gauge: corrected to §7.7 and [GR §8.3], where those
  statements are.

### 5. "The proofs are complete" (CON-07)

- **Original.** appendix-c:317 / FULL:6563 "the derivations are explicit and the proofs are complete".
- **Defect.** G3 is open (GR:12); the coverage ledger has GAP rows; GR §8.5 records a theorem whose
  proof is not written out (CON-36).
- **Correction.** "the derivations are explicit, and the status of each — proved, conditional or
  open — is recorded with it". Downstream: none (no other "proofs are complete" in the corpus).

### 6. "Determined by the boundary geometry" (CON-08, optional, applied)

- **Original.** GR:352 "(iii) Uniqueness of $\hbar$. The emergent action scale is determined by the
  boundary geometry (§3.2)."; ch07:185 / FULL:2064 and Explainer:545 the same.
- **Defect.** Not an error under #939's reading (boundary-only dependence), but "determined" reads as
  the calibration, which is conditional on H-slope; requirement (iii) needs only the dependence.
- **Correction.** "depends only on the boundary geometry (§3.2, Step 2)" — the boundary-only
  dependence lemma (spatially local Hamiltonian, leading order in $t/\tau_B$), which does not use
  H-slope. Downstream: none; requirement (iii)'s argument is unchanged.

### 7. Dark-sector budget "Derived" (CON-31)

- **Original.** ch19:116 / FULL:5276 "**Framework status.** Derived (total budget; …)"; ch19:118 /
  FULL:5278 "The framework derives the total budget"; ch19:339 / FULL:5499 "Derived (total budget)";
  ch09:126 / FULL:2606 "$\Omega_{\rm dark}\approx 0.95$ concordance" with ch09:118 / FULL:2598 "the
  dark sector budget as concordance".
- **Defect.** GR §6.2 item (4) (GR:358), ch07:297 and appendix A G9: the fraction is $1-\Omega_B$ by
  construction, partly definitional.
- **Correction.** "Partly definitional (the total fraction is $1-\Omega_B$ by construction; the
  coefficient of $S_{\rm dS}$ inherits the horizon conditions of Chapter 7)"; table cells "Partly
  definitional ($1-\Omega_B$ by construction)"; "The framework supplies the total budget, partly by
  definition"; ch09 "a partly definitional concordance". The ch19:118 statement that the 27/68 split is
  not derived is kept.
- **Downstream.** ch09 lists the budget as a Tier 1 universality-class entry while ch07:297 gives
  "2 (cond.)"; recorded as an open item below, not changed.

## Site table

| Site (base) | Was | Now | Source |
|---|---|---|---|
| GR:326 | §6 "Dissolution of the Cosmological Constant Problem" | "…: Descriptive Distinction and Conditional Dissolution" | GR:356 |
| GR:336 | "The CC dissolution requires only" | "The conditional dissolution of §6.2 requires only" | GR:356 |
| GR:344 | metric evolves via Einstein's equations; never encounters zero-point sum | metric in the substratum; field equations and coupling the open G3 step; rest on the proposal | GR:12, :356 |
| GR:352 | ħ "determined by the boundary geometry" | "depends only on the boundary geometry (§3.2, Step 2)" | GR:112–122 |
| GR:362 | "But gravity is sourced by …" | "On the proposal, gravity is sourced by …" | GR:362 lead sentence |
| GR:404 | "§8.3 denies that the … sum gravitates absolutely" | on the proposal, conditional on the coupling step | GR:581–583 |
| GR:434 | "The framework denies that ρ_QFT gravitates" | on the proposal, conditional on the open step | GR:356 |
| GR:454 | corollary conditional on the ordering | on the ordering and the open coupling step | GR:12 |
| GR:573 | "The framework denies that the absolute zero-point sum gravitates" | on the proposal, conditional on the open step | GR:581–583 |
| GR:575 | "applied as a precise principle" | principle holds on the proposal, conditional on the step | GR:583 |
| GR:625 (U3) | "compression ratio, not a failure of cancellation" (unconditional list) | identity unconditional; dissolution conditional per (c) | GR:366, :637 |
| Explainer:537, 541, 543, 545, 551, 579, 581, 593, 625, 689 | as in §§1–4, 6 | conditional / normalization / "depends only on" | GR §6 |
| SM:1576 | "dissolution … at the descriptive level" | descriptive distinction behind a conditional dissolution | GR:356 |
| Structure:975 | CC "dissolved" | "(conditional on that coupling step)" | GR:356 |
| ch07:163, 177, 185, 197, 209, 319 (FULL:2042, 2056, 2064, 2076, 2088, 2198) | heading; Einstein's equations; "determined"; "geometry-first dissolution" ×2; "dissolution denies" | as GR | GR §6 |
| ch00:97, 101 (FULL:333, 337) | "dissolution … at the descriptive level"; "the CC dissolution" | conditional | GR:356 |
| ch02:120 (FULL:763) | "is the compression ratio" | "is read as …, dissolves conditional on … (G3)" | GR:366 |
| ch09:118, 126, 243, 257, 261 (FULL:2598, 2606, 2723, 2737, 2741) | "concordance"; "CC dissolution"; §7.6 refs; "nothing to manage" | partly definitional; conditional; §7.7 / [GR §8.3]; conditional | GR:358, :356, §8.3 |
| ch18:142, 144 (FULL:4960, 4962) | "first dissolution"; unconditional reading and incommensurability | conditional | GR:366 |
| ch19:20, 38, 116, 118, 339, 366 (FULL:5180, 5198, 5276, 5278, 5499, 5526) | "Problems resolved"; incommensurability; "Derived" ×3; "The CC dissolution" | "Problems addressed"; conditional; partly definitional | GR:356, :358 |
| appendix-c:317, 349 (FULL:6563, 6595) | "proofs are complete"; "turn out to be category errors" | status recorded with each; framework's reading, conditional | GR:12 |
| readers-guide:15 (FULL:115) | "the cosmological constant dissolution" | "the conditional …" | GR:356 |

Derived artifacts regenerated with `sh ./build.sh GR Explainer SM Structure` and
`sh ./build.sh --book`: page counts and median characters per page unchanged against the base
(GR 88 / 3214, Explainer 70 / 2889→2890, SM 147 / 3194, Structure 99 / 2932→2926, book 558 / 3054).
No coverage fingerprint moved (no canonical statement in `verification/coverage/LEDGER.json` was
edited; `coverage_check` OK, 128 statements); the Lean census registry is untouched.

## Re-grep

`python3 -I check.py <repo-root> 0d917665`, output in `check.out`:

- 24 superseded wordings: **0** occurrences each, corpus-wide (papers, chapters, FULL; the
  Introduction excluded per the unit brief).
- 27 corrected book sentences: present once in the chapter and once in FULL each.
- Inventory of chapter and paper sentences pairing a cosmological-constant term with a dissolution or
  gravitation verb: **79** carry a conditional marker in the sentence; **29** do not, each reviewed:
  conditional by the enclosing sentence or paragraph (ch07:177, ch18:130, :150, ch19:32, GR:362 ×2,
  GR:659), descriptive or identity statements that make no coupling claim (Explainer:579 first
  sentence, GR:356 (a)/(b), GR:462, ch09:253, :257 "prices the two dissolutions", ch19:54, README:68),
  a quoted objection (appendix-c:315), the external closure-theorem route already scoped by its
  stated inputs (GR:166, ch07:44; §1 above), or not about the cosmological-constant coupling at all
  (ch01:149, ch06:157, SM:252, :849, :851, GR:532, :555, appendix-c:122, ch03:212; ch08:246, :264 and
  Explainer:587, which concern the neutrino-mass tension, listed below).
- Added lines: 0 register, caps or revision-voice hits (§A.32/§A.33 family, counted against the
  removed text of the same file); 0 secret or local-path hits.

## Conditional or removed

Made conditional on G3: the classical-level field equations and their source coupling (GR:344,
ch07:177, Explainer:541/543/689); every "does not gravitate" for the zero-point sum, $\rho_{\rm QFT}$
or the absolute emergent vacuum energy (GR:404, :434, :573, :575, ch07:209, Explainer:579); the
dissolution in headings and summaries (CON-04 sites and the downstream list of §4); U3's "not a
failure of cancellation"; the dark-sector corollary's predictions (GR:454). Removed: "the proofs are
complete" (appendix-c:317); "predicts the observed value" (Explainer:551); "Derived" for the
dark-sector budget (ch19 ×3).

## Cross-unit dependencies

- **SC-36** (`corpus/sc36-page-curve-scope`) retitles ch19 §19.2 to the identical "Problems addressed"
  (ch19:20 / FULL:5180): identical change, merges cleanly. SC-36 deletes the ch09 Tier 1 row at
  ch09:125 / FULL:2605, adjacent to this unit's ch09:126 / FULL:2606 cell: a textual conflict is
  expected; resolve by taking both (row deleted, the dark-sector cell as corrected here).
- **Open PRs** #961, #962, #963, #964, #967, #968, #969, #971: no changed line in common (checked on
  base line numbers, ±1). sc28/sc31/sc34 edit GR:368 and ch07:199, two lines from this unit's GR:366
  neighbourhood and ch07:197; no overlap.
- Shared sentences other units may rely on: the GR §6 and ch07 §7.7 heading text (cited as "§6",
  "§7.7"; no anchor link uses the old title); GR §8.5 (U3) now places "not a failure of cancellation"
  under (c); GR:454 now makes the dark-sector corollary conditional on the coupling step; the
  dark-sector budget status "Partly definitional" (ch19, ch09) — any unit restating the dark-sector
  status should use it; GR requirement (iii) and its mirrors now cite boundary-only dependence
  (§3.2, Step 2) instead of the calibration.

## Open, for #970

- ch09 lists the dark-sector budget as a Tier 1 universality-class result (ch09:118, :126), ch07:297
  gives it "2 (cond.)", and appendix A G9 "C | 1": the tier assignment needs one owner decision.
- ch08:246, :264 and Explainer:587 say the framework's RVM dark energy "resolves" the DESI $3\sigma$
  neutrino-mass tension; GR:414 says it "would relax" it. Outside this unit's claim class; not changed.
- ch03:212 "the dark sector is the gravitational effect of the substrate's content" states the
  physical dark-sector interpretation, which ch07:288 makes conditional on the matter-to-boundary
  coupling map; not changed here.
- The research question itself is unchanged: a covariant coupling theorem (G3) that fixes whether the
  uniform offset sources curvature; GR §6.2 exhibits two completions that share the substratum and
  differ only in that offset, so no argument from the reduced quantum data can settle it.
