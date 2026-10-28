# SC-37: the cosmological constant and the open coupling step G3

Unit of PR-A (part). Base `main` at `0d917665`; branch `corpus/sc37-g3-conditional`. Line numbers
below are at the base. Four commits: the unit's corrections; the independent review's findings
B1–B6 with its also-apply list (review of `2ab22504`, ACCEPT WITH CHANGES); the delta review of
`15899d90` (ACCEPT WITH CHANGES: the "by theorem" invisibility, §8 below, and two recommended edits);
and the owner's decision on the dark-sector tier with the reviewer's optional item on `23f0fc97`
(ACCEPT), §9 below.

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
  conditional: "Because the spacetime metric exists at the classical level, *before* the quantum
  description emerges, and the framework's proposal is that gravity is sourced there", with "On that
  proposal," before its compression-ratio sentence. GR:362 "But gravity is sourced by the classical
  Hamiltonian" → "On the proposal, gravity is sourced …" (the paragraph's lead sentence already
  carried the condition). GR:452 (ii-b) "requires the geometry-first ordering established in §6.2:
  the metric exists at the pre-trace-out level, and the stress-energy sourcing gravity is the
  classical stress-energy" → "requires the geometry-first ordering of §6.2, under which the metric
  exists at the pre-trace-out level, together with the proposal of §6.2, conditional on the open
  coupling step, that the stress-energy sourcing gravity is the classical stress-energy" (review B1).
  GR:166 / ch07:44 (the four-route convergence, also named in CON-06) are unchanged: they state the
  routes' inputs and name each route's hypotheses as open obligations; whether "the same conclusion
  is forced" asserts the thermodynamic route while G3 is open is recorded for #970.

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
- **The corollary's statement (review B2).** GR:422 "*Under Lemmas 1–3 and conditions (C1)–(C4), the
  cosmological trace-out … renders ~95% of the universe's gravitational budget invisible to the
  emergent QFT.*" used the coupling (the budget is gravitational) without the hypothesis. Now "*Under
  Lemmas 1–3, conditions (C1)–(C4) and the geometry-first proposal of §6.2 (conditional on the open
  coupling step), …*"; its proof's step (iii) at GR:456 reads "on that proposal gravitationally
  active". The coverage entry `GR:C-invisible-gravitational-budget` is re-affirmed under the same ID:
  fingerprint `ea5d16ff902c196d` → `4f1a95751a4057e8`, level unchanged (GAP, not formalized).
- **Missed mirrors (review B3).** ch07:258 / FULL:2137 "(does gravitate)" → "(on the same proposal,
  does gravitate)"; Explainer:581 "the boundary entropy: gravitationally active" → "on the same
  proposal gravitationally active".

### 3. "Predicts the observed value" (C-B2, Explainer)

- **Original.** Explainer:551 "the other predicts the observed value and explains the discrepancy as
  a derived quantity … One predicts the observed vacuum energy and one misses it by $10^{122}$".
- **Defect.** Contradicts Explainer:549 and GR:366: the value is set by initial conditions, "a
  normalization, not a prediction".
- **Correction** (review B6, which found the first form conditioned only the second clause). Explainer
  :551 now reads: "This contrast bears on the ordering through the open coupling step. … one ordering
  produces the worst prediction in physics and has no solution; the other, if the coupling step
  holds, carries the observed value as a normalization and reads the discrepancy as a derived
  quantity. (… One, conditional on that step, is consistent with the observed vacuum energy as a normalization,
  and one misses it by $10^{122}$; …)". It replaces "This track record is itself evidence for the
  ordering" and "That doesn't prove the ordering is correct, but it's existing evidence, not a future
  hope". Two intermediate forms were replaced in review: "and the evidence rests on that open step"
  (self-assessment under §A.32) and then "The contrast is conditional on that open step.", which
  repeated the paragraph's opening sentence and was removed. Explainer:625 "only the substrate's value
  matches observation" → "is of the observed scale".
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
  convention-dependent factor, $A/(4\,l_p^2)$ (§§6.1, 6.3); that the ratio is a compression ratio
  rather than a failure of cancellation is the dynamical dissolution of (c), conditional on the
  coupling step" (the distinction and the identity stay unconditional). GR:374 "the gauge status of
  the uniform vacuum offset (§6)" → "the status of the uniform vacuum offset, gauge for every quantum
  statistic, with its gravitational coupling the open G3 step (§6)". ch07:175 / FULL:2054 "The two are
  not commensurable as gravitational sources" gains "Conditional on the coupling step,". ch18:142 "On that reading the
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
  statements are; ch09:261 / FULL:2741 cited the same §7.6 for the offset's gauge status and now
  cites "([Main §3.4]; [GR §8.3])" (review B5).

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
  not derived is kept. Matching ch07:297 ("under the conditional physical interpretation"), ch19:116
  adds "the physical interpretation is conditional on the coupling step", and the ch19:339 cell
  "physical interpretation conditional on the coupling step"; ch19:116's second statement of
  "partly definitional … by construction" is removed.
- **GR itself (review B4).** GR:468 "The total dark sector budget is established by §7.2." → "The
  total dark-sector budget is the corollary of §7.2 (partly definitional, and conditional on the
  coupling step)."; GR:545, §7.4 table, "Dark sector fraction … | consistent" → "| partly definitional
  ($1-\Omega_B$ by construction) |".
- **The dark-sector interpretation, same claim class.** Sentences stating that the dark sector *is*
  the gravitational effect of the unreadable content, or that the boundary entropy's uniform
  component *is* dark energy, now carry the proposal: ch03:212 / FULL:1088, ch03:222 / FULL:1098,
  ch02:22 / FULL:665, ch19:54 / FULL:5214, ch19:116 / FULL:5276, Explainer:900, Substratum:46
  ("On the geometry-first proposal ([GR §6.2]), the dark sector is …"). At ch03:222 / FULL:1098
  (coordinator addition) the sentence "The boundary entropy has no operator in the emergent quantum
  field theory, so roughly ninety-five percent of the critical density is invisible to every embedded
  observer *by theorem*; its uniform component is dark energy, and its scale-dependent face is the
  dark-matter regularity $a_0 = cH/6$", with its lead-in "in the flagship case, its energetic
  content", keeps the unconditional part (no operator, hence invisible to the emergent description,
  stated by construction: §8) and places the rest on the proposal: "on the geometry-first proposal,
  conditional on the open
  coupling step (G3), it carries roughly ninety-five percent of the critical density (a fraction equal
  to $1-\Omega_B$ by construction), its uniform component is dark energy, and its scale-dependent face
  is the dark-matter regularity $a_0 = cH/6$, which further requires the horizon conditions of
  Chapter 7, the assumption that a static mass delivers its rest energy $M_Bc^2$ to the boundary, and
  a dimensional factor $1/6$ imported from Verlinde". The $a_0$ conditions are those of GR §7.3
  (GR:470, :510: H-slope, H-frame, H-Hawking; $Q = M_Bc^2$, itself part of the open coupling map;
  the imported factor), ch07:262–266 and appendix A G6 ("factor imported", class C). The rest of the
  section (ch03:218–228) is left to SC-43. GR:26 "The dark-sector
  corollary predicts" → "predicts, conditional on the open coupling step,"; GR:707 "The dark-sector
  corollary explains ~95%" → "accounts, conditional on the coupling step and partly by definition
  (§6.2), for ~95%".
- **Predicted column (delta review).** GR:545's Predicted cell "$\Omega_{\rm dark}\approx 95\%$"
  gains "(conditional on the coupling step)", as in ch07:297's Predicted column.
- **Downstream.** The tier, which ch09 gave as Tier 1 against ch07:297's "2 (cond.)", is settled by
  the owner's decision in §9.

### 8. Hidden-sector invisibility called a theorem (delta review of `15899d90`)

- **Original.** GR:450 (ii-a) "By the trace-out structure, no hidden-sector degree of freedom maps to
  an operator on $\mathcal{H}_V$. This is a theorem of Part I, independent of any gravitational
  content"; Explainer:581 "The paper proves that this entropy has no operator in the emergent QFT";
  ch03:222 / FULL:1098 (as edited in the second commit) "so it is invisible to every embedded
  observer *by theorem*" (base: "roughly ninety-five percent of the critical density is invisible to
  every embedded observer *by theorem*").
- **Defect.** No named theorem in Part I states it (searched `papers/Main.md`); it is a fact of the
  construction: $\mathcal{H}_V$ is spanned by the visible configurations, so a traced-out degree of
  freedom has no operator on it. "To every embedded observer" overscopes it (it is invisibility to the
  emergent quantum description) and contradicts the next clause, in which the same entropy is
  observed gravitationally as the dark sector.
- **Correction.** GR:450 "By the construction of the trace-out, no hidden-sector degree of freedom
  maps to an operator on $\mathcal{H}_V$, which is spanned by the visible configurations. The step uses
  no gravitational content: the hidden sector is invisible to the emergent description by
  construction."; Explainer:581 "By the construction of the trace-out, this entropy has no operator in
  the emergent QFT."; ch03:222 / FULL:1098 "so, by the construction of the trace-out ([GR §7.2], step
  (ii-a)), it is invisible to the emergent quantum description;".
- **Downstream.** Re-grep of papers and book (FULL included) for "by theorem", "proves" or "theorem
  of Part I" together with "no operator", "invisible", "hidden" or "boundary entropy": no further
  claim that invisibility is a theorem. The other hits are about different results and are correct as
  stated: the necessity bound $\log_2|\mathcal C_H|\ge I^*$ (ch01:57 / FULL:401), readback forcing
  hidden predictive memory (ch02:20 / FULL:663; Main:596, :610), the C1 necessity row (Main:731), the
  no-go theorems' own content (ch04:82 / FULL:1201; appendix-c:58 / FULL:6304), and the
  Gödel–Turing–OI analogy (Computation:72, ch12:213 / FULL:3465). Medicine:13 "The OI framework
  proves that any fast subsystem …" concerns C1–C4 memory, not invisibility, and is outside this
  unit. No coverage fingerprint moved (the edits are in the Corollary's proof, not its statement).

### 9. Dark-sector tier (owner decision, round 4)

- **Decision (owner, quoted).** "Dark-sector budget: Tier 2 — conditional. The physical dark-sector
  interpretation requires the open G3 matter-to-boundary coupling. It is not an unconditional Tier 1
  result. Tier 3 is reserved for bijection-specific quantities. … retain the descriptive distinction
  and the partly definitional budget, but distinguish those from a derived gravitational
  explanation."
- **What each column means.** ch09's tables are tiered by level (Tier 1 universality-class, Tier 2
  substratum-properties, Tier 3 bijection-specific; ch09 §§9.3–9.4); ch07:297's last column is the same
  tier; GR §1 and ch07:14 define Tier 2 as the dark-sector phenomenology. Appendix A's G-rows carry
  no tier: "Class" is the S/C/L/R/P/M/E classification and "Layer" the Layer-0–3 axis of
  `AGENTS.md`. G9 "C | 1" (conditional structural; Layer 1) is consistent with the decision and is
  unchanged; appendix A.4.2's lead (appendix-a:102) already states that the physical dark-sector
  interpretation requires the open matter-to-boundary coupling map. Structure §2.4 stratifies by
  hierarchy levels, not tiers; its "dark-sector phenomenology" entry gains the coupling condition.
  The Explainer, ch19 and the book README assign the dark sector no tier (grep), so they need no tier
  edit.
- **Original.** ch09:118 / FULL:2598 "the dark sector budget as a partly definitional concordance —
  follow from these six commitments" (in the list of universality-class results); ch09:125–126 /
  FULL:2605–2606 Tier 1 rows "Dark sector budget $\sim 95\%$ | … partly definitional …" and "No
  dark matter particle | XENON, LUX, etc. null"; ch09:130 / FULL:2610 "Five universality-class
  entries … (information preservation, dark sector budget, no DM particle, no proton decay)";
  ch09:156 / FULL:2636 "The seven Tier 2 entries"; ch09:177 / FULL:2657 "Tier 1 has five entries …
  Tier 2 has seven entries". GR:28, :597, :637 and ch07:14 / FULL:1893 give Tier 2 without the
  coupling condition.
- **Defect.** The physical dark-sector interpretation, of which the gravitational $\sim 95\%$ budget
  and the absence of a dark-matter particle are the two tabulated faces, needs the open G3 coupling;
  ch09 listed both as unconditional Tier 1 results, against ch07:297 and ch07:302 ("2 (cond.)").
- **Correction.**
  - ch09:118: "the dark-sector budget only as a partly definitional count ($1-\Omega_B$ by
    construction) — follow from these six commitments without requiring the specific cubic-lattice
    realization. A derived gravitational explanation of that budget, the physical dark-sector
    interpretation, is Tier 2 and conditional on the open G3 matter-to-boundary coupling (Chapter 7
    §7.9)."
  - Tier 1 table: the two dark-sector rows removed. ch09:130: "Three universality-class entries
    tested against current empirical evidence: one confirmed at high precision (the area law) and
    the remainder consistent with the empirical record at concordance level (information
    preservation, no proton decay). The dark-sector budget and the absence of a dark-matter particle
    are Tier 2 entries (§9.4): the budget is partly definitional, and its gravitational explanation
    is conditional on the open G3 coupling."
  - Tier 2 list (ch09:144): adds "the physical dark-sector interpretation (the gravitational
    explanation of the partly definitional $\sim 95\%$ budget, and the absence of a dark-matter
    particle), conditional on the open G3 matter-to-boundary coupling". Tier 2 table gains "| Dark
    sector budget $\sim 95\%$ | $\Omega_{\text{dark}} \approx 0.95$; partly definitional
    ($1-\Omega_B$ by construction); gravitational explanation conditional on the open G3 coupling |
    Ch 7 §7.9 |" and "| No dark matter particle | XENON, LUX, etc. null; conditional dark-sector
    interpretation | Ch 7 §7.9 |".
  - Counts: "The nine Tier 2 entries combine observed structural features, conditional
    gravitational formulas, consistency with bounds and the conditional dark-sector
    interpretation."; "Tier 1 has three entries … Tier 2 has nine entries"; the total "twenty"
    (3 + 9 + 8) is unchanged.
  - GR:28 and ch07:14 add "Their gravitational reading is conditional on the open G3 coupling step
    (§6.2) [ch07: ([GR §6.2])], and the ~95% fraction itself is partly definitional ($1-\Omega_B$ by
    construction)."; GR:597 "conditional on §3.2 and on the open coupling step of §6.2"; GR:637 "The
    dark-sector phenomenology is Tier 2 and conditional: its gravitational reading requires the open
    G3 coupling step (§6.2), and it inherits the conditions of §3.2 and the dimensional factor
    imported in §7.3."; Structure:179 "dark-sector phenomenology (its gravitational reading
    conditional on the open coupling step of [GR §6.2])".
- **Why "No dark matter particle" moves too.** It is the second face of the same physical
  interpretation, and ch07:302 already gives it "2 (cond.)". Leaving it in Tier 1 would keep exactly
  the unconditional dark-sector entry the decision rules out.
- **Downstream.** The class column is unchanged everywhere (G9 stays C). `check.py` section 2c
  computes each Tier count from its table rows, in the chapter and in FULL, and compares it with
  every stated count ("Tier N has …", "The N Tier 2 entries", "N universality-class entries tested",
  the three-tier total); a stated count that disagrees with its table fails. A negative test (Tier 1
  stated as "four" against three rows) fails as intended. No coverage fingerprint moved.
- **After SC-36 and SC-37 both land the counts must be recounted.** SC-36 removes the
  black-hole-information row and states "four"; this unit removes the two dark-sector rows and states
  "three". Merged, Tier 1 holds two rows (the area law and no GUT-mediated proton decay), so the
  stated Tier 1 counts must read "two" and the three-tier total "nineteen"; SC-36 also changes the
  ch09:130 sentence this unit rewrites. Run `check.py` section 2c on the merge.

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
| GR:374 | "the gauge status of the uniform vacuum offset" | gauge for every quantum statistic; coupling the open G3 step | GR:356, §8.3 |
| GR:422 (Corollary), 452, 456 | coupling used without hypothesis; "ordering established in §6.2: … stress-energy … is the classical" | hypothesis "geometry-first proposal of §6.2 (conditional on the open coupling step)" added; proposal stated as such | GR:356, GR:12 |
| ch09:118, 125–126, 130, 144, Tier 2 table, 156, 177 (FULL:2598, 2605–2606, 2610, 2622, Tier 2 table, 2636, 2657) | dark-sector budget and no-DM particle in Tier 1; "five" / "seven" | partly definitional count kept; physical interpretation Tier 2, conditional; "three" / "nine" | owner decision; ch07:297, :302 |
| GR:28, 597, 637; ch07:14 (FULL:1893); Structure:179 | Tier 2 / dark-sector phenomenology without the coupling condition | gravitational reading conditional on the open coupling step | owner decision; GR:12 |
| GR:26, 468, 545, 707 | corollary "predicts" / "explains"; budget "established"; "consistent"; Predicted "≈ 95%" | conditional; partly definitional; "(conditional on the coupling step)" | GR:358, GR:12, ch07:297 |
| GR:450 (ii-a), Explainer:581 | "a theorem of Part I"; "The paper proves" | "By the construction of the trace-out" | GR:450 itself ("by construction") |
| Explainer:537, 541, 543, 545, 549–551, 579, 581, 593, 625, 689, 900 | as in §§1–4, 6, 7 | conditional / normalization / "depends only on" / on the proposal | GR §6 |
| Substratum:46 | "The dark sector is the gravitational effect …" | on the geometry-first proposal | GR:356 |
| ch02:22, ch03:212, :222 (FULL:665, 1088, 1098) | dark sector / dark energy stated as the gravitational effect; ch03:222 "invisible to every embedded observer *by theorem*" | on the geometry-first proposal; "by the construction of the trace-out ([GR §7.2], step (ii-a)), it is invisible to the emergent quantum description" | GR:356, GR:450 |
| ch07:175, 258 (FULL:2054, 2137) | "not commensurable as gravitational sources"; "(does gravitate)" | conditional on the coupling step; on the same proposal | GR:356 |
| ch19:54 (FULL:5214) | "The framework predicts that dark energy is …" | on the geometry-first proposal | GR:356 |
| SM:1576 | "dissolution … at the descriptive level" | descriptive distinction behind a conditional dissolution | GR:356 |
| Structure:975 | CC "dissolved" | "(conditional on that coupling step)" | GR:356 |
| ch07:163, 177, 185, 197, 209, 319 (FULL:2042, 2056, 2064, 2076, 2088, 2198) | heading; Einstein's equations; "determined"; "geometry-first dissolution" ×2; "dissolution denies" | as GR | GR §6 |
| ch00:97, 101 (FULL:333, 337) | "dissolution … at the descriptive level"; "the CC dissolution" | conditional | GR:356 |
| ch02:120 (FULL:763) | "is the compression ratio" | "is read as …, dissolves conditional on … (G3)" | GR:366 |
| ch09:118, 126, 243, 257, 261 (FULL:2598, 2606, 2723, 2737, 2741) | "concordance"; "CC dissolution"; §7.6 refs ×3; "nothing to manage" | partly definitional; conditional; §7.7 / [Main §3.4]; [GR §8.3]; conditional | GR:358, :356, §8.3 |
| ch18:142, 144 (FULL:4960, 4962) | "first dissolution"; unconditional reading and incommensurability | conditional | GR:366 |
| ch19:20, 38, 116, 118, 339, 366 (FULL:5180, 5198, 5276, 5278, 5499, 5526) | "Problems resolved"; incommensurability; "Derived" ×3; uniform component "is dark energy"; "The CC dissolution" | "Problems addressed"; conditional; partly definitional, physical interpretation conditional; on the proposal | GR:356, :358, ch07:297 |
| appendix-c:317, 349 (FULL:6563, 6595) | "proofs are complete"; "turn out to be category errors" | status recorded with each; framework's reading, conditional | GR:12 |
| readers-guide:15 (FULL:115) | "the cosmological constant dissolution" | "the conditional …" | GR:356 |

Derived artifacts regenerated with `sh ./build.sh GR Explainer SM Structure Substratum` and
`sh ./build.sh --book`: page counts unchanged against the base and median characters per page within
a few characters (GR 88 / 3214→3208, Explainer 70 / 2889→2890, SM 147 / 3194, Structure 99 /
2932→2926, Substratum 53 / 3245, book 558 / 3054). One canonical statement in
`verification/coverage/LEDGER.json` was edited, the GR dark-sector Corollary; its fingerprint is
re-affirmed under the same ID with the same level (GAP), and `coverage_check` is OK (128 statements).
The Lean census registry is untouched.

## Re-grep

`python3 -I check.py <repo-root> 0d917665`, output in `check.out` (the added-lines scan excludes
`check.out`, so the count is stable):

- 58 superseded wordings: **0** occurrences each, corpus-wide (papers, chapters, FULL; the
  Introduction excluded per the unit brief).
- 41 corrected book sentences: present once in the chapter and once in FULL each; 12 corrected paper
  sentences pinned at exactly one occurrence each.
- Chapter 9 tier counts (section 2c): every stated Tier 1, Tier 2 and Tier 3 count and the three-tier
  total equal the rows of their tables, in the chapter and in FULL (3, 9, 8; 20).
- Inventory of chapter and paper sentences pairing a cosmological-constant or dark-sector term with a
  dissolution, gravitation, "commensurable" or "is dark energy / matter" form (the review asked for
  the dark-sector and "commensurable" sentences to be caught): **105** carry a conditional marker in
  the sentence; **47** do not, each reviewed:
  - conditional by the enclosing sentence, paragraph or statement: ch07:177, :258 (the clause
    corrected, the rest descriptive), ch18:130, :150, ch19:32, GR:362 ×2, GR:452 ("Under this
    ordering", after the corrected sentence), GR:462 ×2 (inside the Corollary's proof, whose statement
    now carries the hypothesis), GR:659;
  - descriptive or identity statements making no coupling claim: Explainer:579 ×2, GR:356 (a)/(b),
    ch09:253, :257 "prices the two dissolutions", README:68;
  - falsifiers and observational comparisons: ch07:309, ch18:168, ch19:46 ×2, Explainer:585,
    GR:464, :532, :595;
  - pointers, chapter summaries and lists: ch00:83, ch10:8, ch12:197, ch18:10, Explainer:992,
    Complexity:338 (a list of derived, dissolved or generic items, not specific to this claim);
  - a quoted objection (appendix-c:315);
  - the external closure-theorem route (GR:166, ch07:44), recorded for #970;
  - not about the cosmological-constant coupling or the dark sector: ch01:149, ch06:157, SM:252,
    :849, :851, GR:555, appendix-c:122, Explainer:783, Substratum:157, :500; ch08:246, :264 and
    Explainer:587 concern the neutrino-mass tension, recorded for #970.
- Added lines: 0 register, caps or revision-voice hits (§A.32/§A.33 family, counted against the
  removed text of the same file); 0 secret or local-path hits.

## Conditional or removed

Made conditional on G3: the classical-level field equations and their source coupling (GR:344,
:452, ch07:177, Explainer:541/543/689); every "does not gravitate" for the zero-point sum,
$\rho_{\rm QFT}$ or the absolute emergent vacuum energy (GR:404, :434, :573, :575, ch07:209,
Explainer:579); the dissolution in headings and summaries (CON-04 sites and the downstream list of
§4); the incommensurability "as gravitational sources" (ch07:175, ch18:144, ch19:38); U3's "not a
failure of cancellation"; the dark-sector Corollary (GR:422, a hypothesis added), its predictions
(GR:454) and summaries (GR:26, :468, :707), and the dark-sector interpretation wherever it was stated
as fact (§7). Removed: "the proofs are complete" (appendix-c:317); "predicts the observed value" and
"existing evidence, not a future hope" (Explainer:551); "Derived" for the dark-sector budget
(ch19 ×3); "established by §7.2" (GR:468).

## Cross-unit dependencies

- **SC-36** (`corpus/sc36-page-curve-scope`) retitles ch19 §19.2 to the identical "Problems addressed"
  (ch19:20 / FULL:5180): identical change, merges cleanly. SC-36 deletes the ch09 Tier 1 row at
  ch09:125 / FULL:2605 and rewrites ch09:130 / FULL:2610 and the count at ch09:177 / FULL:2657, all
  of which this unit also changes (it moves the two dark-sector rows to Tier 2): textual conflicts are
  expected. Resolve by keeping all three row removals, writing the ch09:130 sentence from both
  (area law measured; no proton decay at concordance level; information conservation from the
  bijectivity premise, not an empirical entry; the dark-sector entries in Tier 2), and recounting:
  Tier 1 "two", total "nineteen". `check.py` 2c fails on the merge until the counts agree.
- **Open PRs** #961, #962, #963, #964, #967, #968, #969, #971: no changed line in common (checked on
  base line numbers, ±1). sc28/sc31/sc34 edit GR:368 and ch07:199, two lines from this unit's GR:366
  neighbourhood and ch07:197; no overlap.
- Shared sentences other units may rely on: the GR §6 and ch07 §7.7 heading text (cited as "§6",
  "§7.7"; no anchor link uses the old title); GR §8.5 (U3) now places "not a failure of cancellation"
  under (c); the GR §7.2 Corollary (Invisible gravitational budget) carries a new hypothesis, the
  geometry-first proposal conditional on the coupling step, and its coverage fingerprint moved (any
  unit that edits or cites that statement, or the LEDGER.json entry, must merge against it);
  GR:454 now makes the dark-sector corollary conditional on the coupling step; the
  dark-sector budget status "Partly definitional" (ch19, ch09) — any unit restating the dark-sector
  status should use it; GR requirement (iii) and its mirrors now cite boundary-only dependence
  (§3.2, Step 2) instead of the calibration.

## Open, for #970 (recorded, not edited)

- ch08:246, :264 and Explainer:587 say the framework's RVM dark energy "resolves" the DESI $3\sigma$
  neutrino-mass tension; GR:414 says it "would relax" it.
- GR:166 and ch07:44 say an external closure theorem "forces the same conclusion" and that four
  routes "converge on the same dynamics" while G3 (the covariant equations) is open; the inputs are
  stated, but whether the framing asserts the thermodynamic route ahead of G3 is not settled here.
- appendix-c:317 / FULL:6563 keeps "the predictions match empirical data at substantial precision
  (JUNO 0.07$\sigma$, GW250114 99.999%)"; GW250114 tests the classical area theorem, which the
  framework preserves, not a framework prediction (GR:12, ch07 table).
- The research question itself is unchanged: a covariant coupling theorem (G3) that fixes whether the
  uniform offset sources curvature; GR §6.2 exhibits two completions that share the substratum and
  differ only in that offset, so no argument from the reduced quantum data can settle it.
