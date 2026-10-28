# SC-36 (PR-E): black-hole status and the scope of the Page-curve theorem

Base `main` at `0d917665`. Line numbers below are at that base unless marked otherwise.

## Findings corrected

- **CON-01** (high; R-01 context; owner decision OD-9). GR Theorem A.8 counts initial conditions that
  are configurations of Σ_E, with the B|R bipartition aligned to them (GR:817, :827, :841). In exactly
  that setting H-scramble fails for every bijection (GR:833–:835; BHb C1, C6(a)), so the theorem holds
  only vacuously and has no instance there; A.9 inherits this. The Page value enters only through
  H-scramble (BHb C6(b)), and under any permutation the entanglement at an aligned bipartition is at
  most the entropy of the initial configuration distribution (BHb C2).
- **CON-02** (medium). Book status surfaces say the paradox is "resolved" at the level of information
  preservation (ch07:110, ch19:20, ch19:72, ch19:334, ch09:125, and FULL). Information conservation is
  the bijectivity premise (ch07:161), not a result or a tested prediction.
- **CON-03** (low). The BHa report header read "unreviewed for adoption" against its retained review.
- **Outside-slice items** raised by the #918 audit and checked here: GR A.5's coupling chain against
  A.1's geometry; A.7's proof step; GR:366's convention range.

## Route for A.8: (b)

Route (a) — restating A.8 over an ensemble of initial pure states and recounting the excluded fraction
in that ensemble's measure — was not taken. The theorem's proof counts configurations on cycles of the
permutation; over a continuous ensemble that counting has no direct analogue, and no restated theorem
with a complete proof was produced. Route (b) keeps the statement and puts the no-instance fact into
the theorem statement itself, adds a scope paragraph with a self-contained proof of the entropy budget
(BHb C2), and states what a Page value then requires. Research note for #970 below.

## Per-claim record

Evidence levels: **WP** written proof in the manuscript; **EX** exhaustive finite computation
(`sc36_checks.py`); **NUM** numerical evaluation; **CIT** external citation; **PR** prose/status.

| # | Original claim (quoted, file:line) | Defect | Correction | Evidence | Downstream |
|---|---|---|---|---|---|
| 1 | GR:817–825, A.8 statement: "Then the time-averaged entanglement entropy of the radiation equals the Page value … for all initial conditions except a fraction ≤ …" | Counts configurations at an aligned bipartition, where H-scramble fails for every bijection: vacuous, no instance (CON-01) | Statement now ends: "The initial conditions counted are the configurations of Σ_E, and the bipartition B\|R is aligned with the configuration coordinates; in that setting H-scramble fails for every bijection and the time-averaged entropy is zero for every initial condition, so the theorem has no instance there (scope below)." | WP (one-line: a permutation maps basis vectors to basis vectors); EX K1c | A.9, GR §8 (iii), App. A intro, QES remark, book ch07/ch19/appendix A/glossary/ch18 |
| 2 | GR:841: "For all but an exponentially negligible fraction of initial conditions, the time-averaged entanglement entropy equals the Page value. □" | Proof's conclusion stated without its hypothesis | "Under H-scramble, therefore, …" | PR | — |
| 3 | (new) GR App. A.7, "Scope of Theorem A.8" | — | Entropy budget S(ρ_R(t)) ≤ H(p₀) ≤ ln\|supp ψ₀\| for every bijection, t and aligned bipartition, with proof (amplitude relabelling; Schur majorization of the diagonal; marginal ≤ joint). A cycle average within δ of S_Page needs H(p₀) ≥ S_Page − δ, hence ≥ e^{S_Page−δ} configurations, or a non-aligned bipartition; which the substratum supplies is open; a restatement over an ensemble of initial pure states is not given | WP; EX K1 (0 violations over 40,320 permutations × 3 cuts × 5 states), K2 (tight), CC1 (non-permutation countercontrol violates the bound) | Book ch07:126, ch19:72 cite it |
| 4 | GR:835: "H-scramble fails for every bijection in the setting of Theorem A.7's proof, …" | Anchored to A.7 only; the failure is in A.8's own counting (CON-01) | "… in the setting of Theorem A.7's proof and of this theorem's own counting, … (scope below)" | WP | — |
| 5 | GR:853, after A.9 | A.9 inherits A.8's vacuity unstated | Adds: from an initial configuration at aligned stage bipartitions S(ρ_R) = 0 at every step; the curve needs, at each stage, initial configuration entropy ≥ S̄_rad(t) up to tolerance, or non-aligned bipartitions | WP (from 3) | — |
| 6 | GR:609 (iii): "For an evaporating black hole, the entanglement entropy … follows S̄_rad(t) = … (Theorem A.9) …; and the Page value is recovered, as a cycle average, for all but an exponentially negligible fraction (∼e^{−10^77} for 30 M_⊙) of initial conditions, when …" | Leads with the curve unconditionally; reports the vacuous count as a result (R-01 pattern) | Heading "…, conditional."; curve stated under H-scramble and H-decouple; the count attributed to A.8 over "the initial conditions it counts"; then: those are configurations, H-scramble fails, A.8–A.9 have no instance there; Page value needs a superposition with configuration entropy near S_Page, or a non-aligned bipartition; neither specified | PR over WP | — |
| 7 | GR:603: "Appendix A also obtains a cycle-averaged Page curve, conditional on …" ; GR:715: "deriving a cycle-averaged Page curve under …" | No statement that the derivation has no instance in its counted setting | Clause added at both | PR | — |
| 8 | GR:875: "What the present derivation establishes … is that a cycle-averaged Page curve … is reproducible from a finite deterministic substratum without invoking the replica machinery." | The Page value comes from H-scramble, not from the finite deterministic dynamics (BHb C6(b)); no bijection produces it from a configuration | "What the present derivation establishes, at the G1 register, is conditional: under H-scramble and H-decouple … follows without the replica machinery. The Page value enters through H-scramble, not through the finite deterministic dynamics: …" | WP (3) | Book ch07:149 |
| 9 | GR:877: "the typicality-providing ingredient need not be gravitational — it can be combinatorial, on the substratum side of the trace-out — and the derivation here is a microscopic realization …" | A bijection cannot supply the ingredient across an aligned cut (C1/C2) | "… need not be gravitational, and the derivation here would be a microscopic realization …; on the substratum side the bijection alone does not supply that ingredient, since … bounded by the entropy of the initial distribution over configurations (§A.7)." | WP (3) | Book ch07:151 |
| 10 | GR:811–813, A.7: "The total state … is pure (deterministic evolution from a definite initial state). … ρ_D is approximately constant, and \|Ψ⟩ ≈ \|ψ_VB⟩ ⊗ \|χ_D⟩ …" | "ρ_D approximately constant ⇒ product" is invalid unless ρ_D(0) is pure: a constant mixed ρ_D is compatible with a mixed ρ_VB (K3) | Statement gains the hypothesis "Let the initial state be a product \|ψ_VB(0)⟩ ⊗ \|χ_D⟩ across VB\|D, as a definite initial configuration is."; proof made explicit (largest eigenvalue of ρ_D(t) is 1 − O(t/τ); equal nonzero spectra across VB\|D); notes that from a configuration ρ_VB is exactly pure | WP; EX K3 | Coverage `GR:T-a.7` fingerprint re-affirmed (GAP, not formalized) |
| 11 | GR:759/:785: A.5 "coupling chain V ↔ B ↔ D (no direct V-D coupling)", applied at :785 to "a 30 M_⊙ black hole inside the cosmological horizon" | A.1 (GR:719) places V between the horizons, B inside and D beyond: locality gives B ↔ V ↔ D, so the theorem's chain is not the A.1 geometry | A.5 statement unchanged (a conditional theorem); :785 now reads "under the coupling chain of Theorem A.5"; new "Scope of the coupling chain" paragraph: the A.1 chain is B ↔ V ↔ D; step (i) concerns only the partition (W, D) (coupling H_VD rather than H_BD); steps (ii)–(iii) and the cross-term order are derived only for V ↔ B ↔ D; for the A.1 chain the decomposition is not derived | PR (geometry read from A.1) | A.7 uses only step (i); no other corpus site cites A.5 |
| 12 | GR:366: "holding up to a convention-dependent factor between 1/(96π²) and 8/3" ("for any theory with a Planck cutoff") | Weinberg's convention [7] (mode sum k⁴/16π² cut off at (8πG)^{−1/2}, against Ω_Λρ_crit) gives 1/(384π⁴Ω_Λ) ≈ 3.9×10⁻⁵, outside the range; M_Pl⁴ against the displayed H²/G gives 1/π | Range removed; three conventions stated with their exact factors: 1/π, 1/(96π²) (cutoff 1/ε at σ = 1, against ρ_crit), 1/(384π⁴Ω_Λ) ≈ 3.9×10⁻⁵ | NUM K4a–d (SI constants; agreement to 1e-12 with the closed forms) | Book ch07:193, appendix A:117 (and FULL) |
| 13 | ch07:110 "The framework resolves the paradox at the level of information preservation: …" (FULL:1989) | Preservation is a premise (ch07:161); CON-02 | "The framework does not resolve the paradox. Information is never lost … because φ is bijective, and bijectivity is a premise of the framework (Chapter 1), not a result; … The Page-curve derivation below bears on it under two conditions, … and H-scramble fails for every bijection acting on an initial configuration …. On the framework's reading the apparent information loss is an artifact of the trace-out" | PR | — |
| 14 | ch07:12 summary (FULL:1891) "Section 7.6 treats the black hole information paradox: information is never lost …" | Silent on status and on the no-instance fact | "…, which the framework does not resolve: …, bijectivity being a premise; …"; failure clause appended | PR | — |
| 15 | ch07:116 "The framework provides an alternative derivation …, conditional on …" (FULL:1995) | — (wording aligned) | "The framework offers a conditional alternative …: a derivation from …" | PR | — |
| 16 | ch07:126 "H-scramble therefore fails in that setting and requires an initial superposition …" (FULL:2005) | Does not say the failing setting is the counted one | Adds: that is the setting the derivation counts, so it has no instance there; entropy budget; e^{S_Page} configurations or non-aligned bipartition | PR over WP (3) | — |
| 17 | ch07:149, :151 (FULL:2028, :2030) | As rows 8–9 | Mirrored | PR | — |
| 18 | ch07:193 (FULL:2072) "between 1/(96π²) and 8/3" | As row 12 | As row 12 | NUM | — |
| 19 | ch09:125 table row "BH information preserved" as a Tier 1 prediction; ch09:130 "Five universality-class entries … (information preservation, …)" (FULL:2605, :2610) | A premise is not a tested prediction (CON-02) | Row removed; "Four …"; sentence: "Information conservation follows from the bijectivity premise and is not an empirical entry: a measurement of the radiation alone does not test it, and the Page curve is conditional (Chapter 7 §7.6)." | PR | Count re-grepped: no other "Five universality-class" site |
| 20 | appendix A:102 "The Page curve requires H-scramble and H-decouple." ; G11 (:111) "Nested trace-out, H-scramble, H-decouple; full product space" (FULL:5639, :5648) | Caveat absent (CON-01/OD-9) | Failure clause added at :102; G11 cell "H-scramble (fails from configurations)". Class C kept: the hypothesis is open for superpositions and non-aligned cuts | PR | Counts "6 C + 2 L" unchanged |
| 21 | appendix A:117 "between 1/(96π²) and 8/3" (FULL:5654) | As row 12 (found by the K5 re-grep control) | 1/π and 1/(384π⁴Ω_Λ) ≈ 3.9×10⁻⁵ stated | NUM | — |
| 22 | ch19:20 "## 19.2 Problems resolved" (FULL:5180) | The section holds partial, split and unresolved entries; CON-02 | "## 19.2 Problems addressed"; :22 adds the BH paradox "as an unresolved entry whose information conservation is a premise and whose Page curve is conditional" | PR | Overlaps CON-04 (PR-A) |
| 23 | ch19:30 "the black-hole information account, which preserves information while the Page curve is conditional" (FULL:5190) | Premise as achievement | "in which information is conserved by the bijectivity premise and the Page curve is conditional" | PR | — |
| 24 | ch19:72 "**Framework status.** Resolved at the level of information preservation; the Page curve is conditional. …" (FULL:5232) | CON-01, CON-02 | "Not resolved; information conservation is a premise and the Page curve is conditional. …"; failure clause and e^{S_Page} requirement added | PR | — |
| 25 | ch19:334 "Preserved; Page curve conditional" (FULL:5494) | CON-02 | "Not resolved — information conserved by premise; Page curve conditional" | PR | — |
| 26 | ch18:146 "the Page curve at the emergent level is a conditional result (Chapter 7 §7.6)." ; ch18:156 "… and, at the level of information preservation, for the information paradox." (FULL:4964, :4974) | Same overstatement as ch19:72 | Failure clause added at :146; the BH clause removed at :156 | PR | Overlaps CON-04 (PR-A) |
| 27 | glossary:113 "The framework obtains a cycle-averaged Page curve … under … H-scramble and … H-decouple" (FULL:6713) | Caveat absent | Failure clause added | PR | — |
| 28 | BHa `bh01_access_v1/REPORT.md`:3 "Status: exploratory research, unreviewed for adoption." | Reads as contradicting the retained review (CON-03) | "Status: exploratory research, internally reviewed (review/README.md), not adopted." `SHA256SUMS` REPORT line updated (`sha256sum -c` passes) | PR | Not legacy- or receipt-protected: `verification/infrastructure/legacy-records.json` and `verification/receipts/` do not cover `verification/programmes/black-hole-information/` |

## Claims removed or made conditional

- Removed: "resolves the paradox at the level of information preservation" (ch07, FULL); "Resolved at the
  level of information preservation" (ch19, FULL); "Preserved" status (ch19 table); "BH information
  preserved" as a Tier 1 prediction (ch09, FULL) and its count; "reproducible from a finite deterministic
  substratum" (GR, ch07); "it can be combinatorial" (GR, ch07); the 1/(96π²)–8/3 range (GR, ch07,
  appendix A); "at the level of information preservation" for the paradox (ch18).
- Made explicitly conditional or scoped: GR §8 (iii) Page curve (conditional heading; A.8's count attributed
  with its no-instance scope); A.8's proof conclusion ("Under H-scramble"); A.9 (inherits scope);
  A.5's application to the black hole inside the cosmological horizon (under its chain hypothesis);
  A.7 (initial VB|D product hypothesis).
- Unchanged and not a flaw: A.8–A.9's class C in appendix A G11 (the hypothesis is open, not refuted, for
  superposed initial states or non-aligned cuts); the Page-time relation and β discussion.

## Re-grep (`sc36_checks.py`, K5; papers/*.md and book/*.md, Introduction excluded)

Retired phrases, count after the change: "resolves the paradox" 0; "Resolved at the level of information
preservation" 0; "at the level of information preservation" 0; "Problems resolved" 0; the
1/(96π²)–8/3 range 0; "reproducible from a finite deterministic substratum" 0; "it can be combinatorial"
0; "| BH information preserved |" 0; "Preserved; Page curve conditional" 0; "Five universality-class
entries" 0. Surviving corrected statement "H-scramble fails for every bijection": 14 (GR 6, ch07 2,
appendix A 1, glossary 1, FULL 4); "no instance": 5 (GR 3, ch07 1, FULL 1). Lines pairing "information
paradox" with "resolv": 9, all now negative or neutral (ch07:12/:110, ch19:22/:334 and FULL mirrors) plus
Main:66, which reports the field's view of the paradox. K6: every changed chapter line is present in FULL.
`papers/Introduction.md` is untouched; its L162 is R-01's (r32).

## Lean

No Lean theorem bears on GR A.5–A.9 or the book sites (ledger: `GR:T-a.7`, `T-a.8`, `T-a.9` are GAP, not
formalized; no census entry). Nothing here requires a formal change. `verification/lean-manuscript-census.json`
is not touched.

## Coverage

`GR:T-a.7` fingerprint re-affirmed (ef7fd4160d9c1506 → f49c9f0ad4a4887e, line 813), same ID, grade GAP
unchanged. A.8's census statement (first paragraph) is unchanged; the scope sentence sits in the
statement's closing paragraph. `coverage_check`: OK (128 canonical statements).

## Cross-unit dependencies

Shared statements this unit changes, which other units or open PRs may rely on:

- **GR Theorem A.8 scope** (no instance for initial configurations at an aligned bipartition) and the
  **entropy-budget paragraph** "Scope of Theorem A.8" (GR App. A.7): the Introduction's §5 (R-01; r32)
  should cite these; any unit quoting A.8's "for all but an exponentially negligible fraction".
- **GR Theorem A.7 statement** (new hypothesis: initial VB|D product) and **A.5 scope** (chain V↔B↔D is a
  hypothesis; not the A.1 geometry): any unit citing A.5's decomposition or A.7's purity.
- **GR:366 / ch07:193 / appendix A:117 convention factor**: any unit quoting the 10^122 identity's
  factor (PR-A, CON-04/CON-05 area: GR §6, ch07 §7.7).
- **ch19 §19.2 heading** ("Problems addressed") and its intro sentence (:22); **ch18:146, :156**: the
  same lines are in CON-04's scope (PR-A, "Dissolution" headings at GR §6, ch07 §7.7, ch18:142, ch19 §19.2).
  Expect a textual conflict if PR-A edits ch19:20/:22 or ch18:156; resolve by merits.
- **ch09 Tier 1 table and count** ("Four universality-class entries").
- **BHa `REPORT.md`:3 and `SHA256SUMS`**: PR-I (S9-M6, BHa REPORT:61–62) will also change the REPORT
  line of `SHA256SUMS`; the two edits touch the same checksum line and must be recomputed on merge.
- Open PRs: none of #961–#971 edits a line changed here. Nearest: #964 (SC-22) changes FULL:6715–6716 and
  glossary next to the Page-curve entry (FULL:6713, glossary:113; one unchanged line between);
  #962/#967/#971 change GR:368 (next paragraph after GR:366) and ch07:199 (not :193).

## Open, for #970

- Restating A.8 over an ensemble of initial pure states (route (a)). Observation, not adopted: for
  Haar-random initial ψ₀ and any unitary U, each U^tψ₀ is Haar-distributed and the time average of
  S(ρ_R) is Lipschitz with the same constant as S, so Lévy's lemma concentrates it at Page's mean with no
  scrambling hypothesis; the Page value then comes from the initial ensemble, not the dynamics. Constants
  and a written proof are not supplied here.
- Whether the substratum supplies an initial superposition over ≥ e^{S_Page} configurations or a
  bipartition not aligned with the configuration coordinates.
- A.5's dissipator decomposition for the A.1 chain B ↔ V ↔ D.

## Checks

- `python3 -I sc36_checks.py 0d917665` → `sc36_checks.out`: all controls pass.
- `python3 -I sc36_scan.py 0d917665` → `sc36_scan.out`: 0 hits (§A.32/§A.33 phrases, revision voice,
  caps, secrets, local paths).
- `tools/release_gate.py`: all steps pass except `lean-axioms` (no local toolchain).
  `tools/coverage_check.py` OK; `verification/lean/edge_rigidity_probe.py` all pass.
- Builds: GR 88 → 89 pages, median 3,229 characters per page; book 558 → 558 pages, median 3,056.
