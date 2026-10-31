# SC-36 (PR-E): black-hole status and the scope of the Page-curve theorem

Base `main` at `0d917665`. Line numbers are at that base unless marked otherwise. Three commits: the
first correction; the independent-review round (REVISE on 2eab9186) with the owner decision on G11; and
round 3 (ACCEPT WITH CHANGES on 9d11a5dd): the three-tier total, the full-tier K7, an A.7 proof clause
and an appendix A wording fix.

## Findings corrected

- **CON-01** (high; R-01 context; OD-9). GR Theorem A.8 counts initial conditions that are
  configurations of Σ_E, with the B|R bipartition aligned to them (GR:817, :827, :841). There
  H-scramble fails for every bijection (GR:833–:835; BHb C1, C6(a)), so the theorem holds only
  vacuously and has no instance; A.9 inherits this. The Page value enters only through H-scramble
  (BHb C6(b)); under any permutation the entanglement at an aligned bipartition is at most the entropy
  of the initial configuration distribution (BHb C2).
- **CON-02** (medium). Book status surfaces said the paradox is "resolved" at the level of information
  preservation. Information conservation is the bijectivity premise (ch07:161), not a result or a
  tested prediction.
- **CON-03** (low). The BHa report header read "unreviewed for adoption" against its retained review.
- **Outside-slice items** from the #918 audit: GR A.5's coupling chain against A.1's geometry; A.7's
  proof step; GR:366's convention range. All three confirmed and corrected.
- **Review round (REVISE on 2eab9186).** B1: A.7 was still false under the product hypothesis added
  in the first commit (counterexample below). B2: GR §8 (iii) still reported the count. B3: ch09
  Tier 1 count. B4: ch18:130. C1: A.5's 30 M_⊙ figures. C2: ch18 headings. Smaller items as listed.
- **Owner decision on G11** (2026-10-28): "Open research target; remove from counted Class C
  predictions for now. … preserve the conditional mathematical result, its hypotheses, and its
  evidence. Do not reclassify it as L merely to retain a prediction entry. … Update the prediction
  counts and mirrors accordingly, without reusing the G11 identifier."

## Route for A.8: (b)

Route (a), restating A.8 over an ensemble of initial pure states with the excluded fraction counted
in that ensemble's measure, was not taken: the proof counts configurations on permutation cycles and
no restated theorem with a complete proof was produced. Route (b) keeps the statement, puts the
no-instance fact and H-scramble's operative content into it, and adds a proved scope paragraph.

## Per-claim record

Evidence: **WP** written proof in the manuscript; **EX** exhaustive or exact finite computation
(`sc36_checks.py`); **NUM** numerical evaluation; **PR** prose/status; **OD** owner decision.

| # | Original (quoted, file:line) | Defect | Correction (new text, abridged where long) | Evidence | Downstream |
|---|---|---|---|---|---|
| 1 | GR:817–825 A.8: "Then the time-averaged entanglement entropy of the radiation equals the Page value … for all initial conditions except a fraction ≤ …" | Counts configurations at an aligned cut, where H-scramble fails for every bijection: vacuous (CON-01) | Statement ends: "The initial conditions counted are the configurations of Σ_E, and the bipartition B\|R is aligned with the configuration coordinates. In that setting, for d_B, d_R > 1 and ε < S_Page, H-scramble in the form the proof uses (at most a fraction e^{−c d_min ε²} of the states on the orbit atypical) fails for every bijection, and the time-averaged entropy is zero for every initial condition, so the theorem as stated has no instance (scope below)." | WP; EX K1c | A.9, GR §8 (iii), App. A intro, QES remark; book ch07/ch18/ch19/appendix A/glossary/README |
| 2 | GR:835: "in the sense of an approximate unitary design or comparable scrambling property. Under H-scramble the counting step below goes through …" | "Fails" depended on how "design" is read: a full cycle of configurations is an exact state 1-design | Adds: "…and it uses H-scramble only through that bound: at most η\|Σ_E\| of the states on the orbit are atypical. A full cycle of configurations is an exact state 1-design, so a design property of low order does not supply the bound, and the failure stated next is a failure of the bound." | WP | — |
| 3 | GR:835: "H-scramble fails for every bijection in the setting of Theorem A.7's proof, …" | Anchored to A.7 (whose setting is now different); the failure is in A.8's own counting | "…in the setting of this theorem's own counting, a definite initial configuration with the bipartition aligned to the configuration coordinates (scope below), where every configuration is atypical once ε < S_Page:" | WP | — |
| 4 | GR:841: "For all but an exponentially negligible fraction of initial conditions, the time-averaged entanglement entropy equals the Page value. □" | Conclusion without its hypothesis | "Under H-scramble, therefore, …" | PR | — |
| 5 | (new) GR App. A.7 "Scope of Theorem A.8" | — | S(ρ_R(t)) ≤ H(p₀) ≤ ln\|supp ψ₀\| for every bijection, t and aligned bipartition, proved (amplitude relabelling; Schur majorization of the diagonal; marginal ≤ joint); a value within δ of S_Page needs ≥ e^{S_Page−δ} configurations or a non-aligned cut; which the substratum supplies is open; no ensemble restatement is given | WP; EX K1 (0 violations, 40,320 permutations × 3 cuts × 5 states), K2 (tight), CC1 (non-permutation countercontrol violates it) | ch07:126, ch19:72 |
| 6 | GR:853 after A.9 | A.9 inherits A.8's vacuity | Adds the inherited scope (S = 0 from a configuration; entropy requirement per stage) | WP | — |
| 7 | GR:609 (iii): "For an evaporating black hole, the entanglement entropy … follows … (Theorem A.9) …; and the Page value is recovered, as a cycle average, for all but an exponentially negligible fraction (∼e^{−10^77} for 30 M_⊙) of initial conditions, when …" | Curve asserted unconditionally; vacuous count reported as a result (R-01 pattern; review B2) | Heading "…, conditional."; curve stated under H-scramble and H-decouple; then: "Theorem A.8 derives the Page value as a cycle average from H-scramble, which carries measure concentration [29, 61] to the orbit, the cycle decomposition of the finite configuration space supplying exact time averages. It counts initial configurations, with the bipartition aligned to the configuration coordinates, and there H-scramble fails for every bijection: every state on the orbit is a product state and the radiation's entropy is zero, so Theorems A.8–A.9 as stated have no instance. Under a bijection … a Page value requires an initial superposition whose distribution over configurations has entropy close to the Page value or above it, or a bipartition not aligned with the configuration coordinates; neither is specified, …" | PR over WP | e^{−10^77} now only in A.8's proof (K5) |
| 8 | GR:603 "Appendix A also obtains a cycle-averaged Page curve, conditional on …"; GR:715 "deriving a cycle-averaged Page curve under …" | No-instance fact absent | Clause added at both | PR | — |
| 9 | GR:875 "…is that a cycle-averaged Page curve … is reproducible from a finite deterministic substratum without invoking the replica machinery." | The Page value comes from H-scramble, not the dynamics (BHb C6(b)) | "…is conditional: under H-scramble and H-decouple … follows without the replica machinery. The Page value enters through H-scramble, not through the finite deterministic dynamics: …" | WP (5) | ch07:149 |
| 10 | GR:877 "…need not be gravitational — it can be combinatorial, on the substratum side of the trace-out — and the derivation here is a microscopic realization …" | A bijection cannot supply it across an aligned cut | "…need not be gravitational, and the derivation here would be a microscopic realization …; on the substratum side the bijection alone does not supply that ingredient, since … (§A.7)." | WP (5) | ch07:151 |
| 11 | GR:811–813 A.7: "*On timescales t ≪ τ_B^D, the joint state of V and B is effectively pure …*"; proof: "pure (deterministic evolution from a definite initial state). … ρ_D is approximately constant, and \|Ψ⟩ ≈ \|ψ_VB⟩⊗\|χ_D⟩ …" | "ρ_D ≈ constant ⇒ product" invalid. The first commit's fix (initial VB\|D product with pure D) is still false (review B1): with qubits and φ(v,b,d) = (v, b⊕d, d), D's configuration is frozen, yet from \|0⟩\|0⟩\|+⟩ one step gives purity(ρ_VB) = 1/2. A frozen configuration fixes ρ_D's diagonal, not its coherences | Statement: "*Let the initial state be \|ψ_VB(0)⟩ ⊗ \|d₀⟩, with d₀ ∈ 𝒞_D a configuration. On timescales t ≪ τ_B^D, …*". Proof: the D-configuration of φ_t(x, d₀) equals d₀ except for x in a set E_t of weight w_t = Σ_{x∈E_t}\|ψ(x)\|² = O(t/τ_B^D) (§3.2 lemma, step (ii), applied to (W, D); step (ii) bounds the displacement of every configuration pointwise, so the bound on w_t holds for arbitrary ψ_VB); by injectivity the rest sums to \|a(t)⟩⊗\|d₀⟩ with ‖a‖² = 1 − w_t; ⟨d₀\|ρ_D\|d₀⟩ = 1 − w_t; equal nonzero spectra give ρ_VB within trace distance 2w_t of its top eigenprojector. New **Remark (initial state of D)** with the counterexample | WP; EX K3 (mixed constant ρ_D), K3b (must-fire countercontrol: D-configuration fixed, purity 1/2 exactly), K3c (576 D-preserving bijections × 2 d₀ × 3 ψ_VB × 3 steps: ρ_VB exactly pure) | Coverage `GR:T-a.7` re-affirmed, same ID, GAP (fingerprint d1d4eef7e2582a07, line 813). Corpus citations of A.7: GR:609, :811, :817 (none depend on a superposed D). Introduction L298 (r32) must add "from an initial state in which D is in a definite configuration" |
| 12 | GR:785–789 "**Bound for the cosmological + stellar black hole case.** For a 30 M_⊙ black hole inside the cosmological horizon: … The three terms: … The cross term is negligible by 12 orders of magnitude …" | Applies A.5's chain V↔B↔D to an object with chain B↔V↔D: an assumption added to keep the conclusion (review C1) | "**Orders of magnitude.** For a 30 M_⊙ black hole …, τ_S ∼ 10⁻¹⁵ s, … Inserted into the orders of Theorem A.5, these timescales give: [display] The cross term is then 12 orders of magnitude below the smaller primary correction. These are the orders the theorem gives under its chain V ↔ B ↔ D. They are not derived for this black hole, which has the chain B ↔ V ↔ D (below), for which the decomposition and the order of the cross term are not derived." | PR | — |
| 13 | GR:759 A.5 "coupling chain V ↔ B ↔ D (no direct V-D coupling)" against A.1 (GR:719) | A.1 places V between the horizons: locality gives B ↔ V ↔ D | Statement unchanged (conditional theorem). New "**Scope of the coupling chain.**" paragraph: step (i) concerns only (W, D) (coupling H_VD rather than H_BD); steps (ii)–(iii) and the cross-term order are derived only for V ↔ B ↔ D | PR (geometry of A.1) | A.7 uses only step (i) |
| 14 | GR:366 "holding up to a convention-dependent factor between 1/(96π²) and 8/3" | Weinberg's convention [7] gives 1/(384π⁴Ω_Λ) ≈ 3.9×10⁻⁵, outside the range | "…holding up to a convention-dependent numerical factor. With ρ_QFT = M_Pl⁴ and ρ_classical = H²/G … the ratio is exactly S_dS/π; the mode sum k⁴/(16π²) cut off at 1/ε = M_Pl/(2√σ) (§4) against ρ_crit = 3H²/(8πG) gives S_dS/(96π²σ²); and the same mode sum cut off at the reduced Planck mass (8πG)^{−1/2} [7] against the observed dark-energy density Ω_Λρ_crit gives S_dS/(384π⁴Ω_Λ) ≈ 3.9 × 10⁻⁵ S_dS." | NUM K4a–f (SI constants; closed forms to 1e-12; σ = ln 2 case; 8/3 for M_Pl⁴ against ρ_crit) | ch07:193, appendix A:117 |
| 15 | ch07:193 "between 1/(96π²) and 8/3: the numerator depends on where the emergent sum is cut off, at 1/ε …, and on how the zero-point integral is normalized." | As 14 | "…numerical factor: the numerator depends on where the emergent sum is cut off, at 1/ε = M_Pl/(2√σ) in natural units or at another Planck-scale cutoff, and on how the zero-point integral is normalized, and the denominator on which classical density is compared. M_Pl⁴ against H²/G gives S_dS/π; the mode sum k⁴/(16π²) cut off at 1/ε against the critical density ρ_crit gives S_dS/(96π²σ²); the conventional estimate, … gives S_dS/(384π⁴Ω_Λ) ≈ 3.9×10⁻⁵ S_dS." | NUM | — |
| 16 | appendix A:117 "its compression ratio ρ_QFT/ρ_crit ∼ S_dS … between 1/(96π²) and 8/3" | As 14; label must match denominators | "its compression ratio ρ_QFT/ρ_classical ∼ S_dS … up to a convention-dependent numerical factor, 1/π for M_Pl⁴ against H²/G and 1/(384π⁴Ω_Λ) ≈ 3.9×10⁻⁵ for a mode sum cut off at the reduced Planck mass against the observed dark-energy density (Ch 7 §7.7)." | NUM | — |
| 17 | ch07:110 "The framework resolves the paradox at the level of information preservation: …" | Premise as resolution (CON-02) | "The framework does not resolve the paradox. Information is never lost … because φ is bijective, and bijectivity is a premise of the framework (Chapter 1), not a result; … The Page-curve derivation below bears on it under two conditions, H-scramble and H-decouple, neither of which is established, and H-scramble fails for every bijection acting on an initial configuration with the bipartition aligned to the configuration coordinates. On the framework's reading the apparent information loss is an artifact of the trace-out …" | PR | — |
| 18 | ch07:12 "Section 7.6 treats the black hole information paradox: information is never lost …" | Status and failure absent | "…, which the framework does not resolve: …, bijectivity being a premise; …"; failure clause appended | PR | — |
| 19 | ch07:116 "The framework provides an alternative derivation …, conditional on …" | — (aligned) | "The framework offers a conditional alternative …: a derivation from …" | PR | — |
| 20 | ch07:126 "H-scramble therefore fails in that setting and requires an initial superposition …" | Not tied to the counted setting | Adds the counted setting, no instance, the entropy budget and e^{S_Page} configurations | PR over WP | — |
| 21 | ch07:149, :151 | As 9–10 | Mirrored | PR | — |
| 22 | ch07:288 "and the Page curve requires H-scramble and H-decouple." | Caveat absent | "…requires H-scramble and H-decouple, of which H-scramble fails for every bijection acting on an initial configuration with the bipartition aligned to the configuration coordinates." | PR | — |
| 23 | book/README.md:64 "…a cycle-averaged Page curve …, conditional on the scrambling condition H-scramble and the decoupling condition H-decouple." | Caveat absent | Same clause appended (README has no FULL mirror) | PR | — |
| 24 | ch09:108 "(the information-preservation half of Chapter 7 §7.6)" | Premise framed as a result | "(the premise of information conservation in Chapter 7 §7.6)" | PR | — |
| 25 | ch09:125 Tier 1 row "BH information preserved"; ch09:130 "Five universality-class entries … (information preservation, …)" | A premise is not a tested prediction | Row removed; "Four …"; "Information conservation follows from the bijectivity premise and is not an empirical entry: a measurement of the radiation alone does not test it, and the Page curve is conditional (Chapter 7 §7.6)." | PR | SC-37 conflict at this row (below) |
| 26 | ch09:177 "Tier 1 has five entries:" | Stale count after 25 (review B3) | "Tier 1 has four entries:" | EX K7 (computed from the table) | Reconciliation with SC-37 must recount (below) |
| 26a | ch09:179 (FULL:2659) "The three tiers contain twenty entries of unequal evidential weight." | Stale total after 25 (round 3): 4 + 7 + 8 = 19 | "The three tiers contain nineteen entries of unequal evidential weight." | EX K7 (sum of the three tables; fires on "twenty") | As 26 |
| 27 | appendix A:111 G11 "\| G11 \| Page curve \| Nested trace-out, H-scramble, H-decouple; full product space \| C \| 1 \| Scrambling, decoupling, proper-shell value open \| Ch 7 §7.6 \|" | CON-01; owner decision | "\| G11 \| Page curve \| Nested trace-out, H-scramble (fails from configurations), H-decouple; full product space \| Open research target (not counted) \| 1 \| A non-vacuous version needs a specified initial ensemble or a non-aligned bipartition, a valid proof and independent verification; decoupling and proper-shell value open \| Ch 7 §7.6 \|" | OD | Identifier kept; no successor renumbered |
| 28 | appendix A:102 "The Page curve requires H-scramble and H-decouple." | CON-01; owner decision | "…requires H-scramble and H-decouple; H-scramble fails for every bijection acting on an initial configuration with the bipartition aligned to the configuration coordinates, so the Page value requires an initial superposition over many configurations or a non-aligned bipartition; no such realization is established, and the Page curve (G11) is an open research target." | PR; OD | — |
| 29 | appendix A:115 "**Summary statistics.** Counts: 6 C + 2 L. Total: 8. The conditional entries carry the calibration, horizon-state, coupling, scrambling or interacting-sector obligations stated above." | Count includes G11 (owner decision) | "**Summary statistics.** Counts: 5 C + 2 L. Total: 7. G11, an open research target, is not counted. The conditional entries carry the calibration, horizon-state, coupling or interacting-sector obligations stated above." | EX K7 | — |
| 30 | appendix A:225 "the eight gravitational-sector entries comprise six conditional results and two layered estimates, with four consistency or descriptive relations stated beside them," | As 29 | "the seven gravitational-sector entries comprise five conditional results and two layered estimates, with the Page curve (G11), an open research target, and four consistency or descriptive relations stated beside them," | EX K7 | — |
| 31 | "eight gravitational(-sector) entries" at appendix A:8, preface:7, ch08:272, ch09:8, ch09:322, ch17:234, ch18:335, ch19:362, appendix C:8, :273 (and FULL:78, :2475, :2488, :2803, :4813, :5153, :5522, :5545, :6254, :6519) | As 29 | "seven gravitational(-sector) entries" | EX K7 | — |
| 32 | ch18:130 "receive the *same* structural resolution in the framework, with each dissolution following …; … the information account preserves information with the Page curve conditional, …; … not a completed theory of quantum gravity. This section pulls the three resolutions together …" | Disagrees with ch07:110 and ch19:72 (review B4, C2) | "receive the *same* structural reading in the framework, each following …; … the information account, in which information is conserved by the bijectivity premise and the Page curve is conditional, …; … not a completed theory of quantum gravity, and the information paradox is not resolved. This section pulls the three readings together …" | PR | — |
| 33 | ch18:146 "**The second dissolution: the black hole information paradox.** … the Page curve at the emergent level is a conditional result (Chapter 7 §7.6)." | Heading claims dissolution; caveat absent | "**The second component: the black hole information paradox.** … a conditional result, on a scrambling condition that no bijection meets from an initial configuration with the bipartition aligned to the configuration coordinates (Chapter 7 §7.6)." | PR | ch18:142 is SC-37's |
| 34 | ch18:156 "…and, at the level of information preservation, for the information paradox." | As 17 | Clause removed | PR | — |
| 35 | ch19:20 "## 19.2 Problems resolved"; :22 section intro | Holds unresolved entries | "## 19.2 Problems addressed" (identical to SC-37's change); :22 lists the paradox "as an unresolved entry whose information conservation is a premise and whose Page curve is conditional" | PR | — |
| 36 | ch19:30 "which preserves information while the Page curve is conditional" | Premise as achievement | "in which information is conserved by the bijectivity premise and the Page curve is conditional" | PR | — |
| 37 | ch19:72 "**Framework status.** Resolved at the level of information preservation; the Page curve is conditional. …" | CON-01, CON-02 | "**Framework status.** Not resolved; information conservation is a premise and the Page curve is conditional. …"; failure clause and e^{S_Page} requirement | PR | — |
| 38 | ch19:334 "Preserved; Page curve conditional" | CON-02 | "Not resolved — information conserved by premise; Page curve conditional" | PR | — |
| 39 | glossary:113 "The framework obtains a cycle-averaged Page curve … under … H-scramble and … H-decouple" | Caveat absent | Failure clause added | PR | — |
| 40 | BHa `bh01_access_v1/REPORT.md`:3 "Status: exploratory research, unreviewed for adoption." | Contradicts the retained review (CON-03) | "Status: exploratory research, internally reviewed (review/README.md), not adopted."; listed under "Post-review changes" as "After landing (status line only)"; `SHA256SUMS` REPORT line recomputed (`sha256sum -c` passes) | PR | Not frozen: absent from `verification/infrastructure/legacy-records.json` and from every receipt; no evidence-retention archive exists in the tree |

All book edits are mirrored into `book/The-Incompleteness-of-Observation-FULL.md` (K6; release-gate `mirror`).

## Claims removed or made conditional

- **Removed:**
  - "resolves the paradox at the level of information preservation" and "Resolved at the level of information preservation";
  - "Preserved" as a status;
  - "BH information preserved" as a Tier 1 prediction, with its count;
  - "reproducible from a finite deterministic substratum" and "it can be combinatorial";
  - the 1/(96π²)–8/3 range;
  - "at the level of information preservation" for the paradox (ch18);
  - "same structural resolution" and "second dissolution" for the paradox (ch18);
  - A.5's 30 M_⊙ figures as results for that black hole (now orders the theorem would give, not derived for it);
  - G11 from the counted predictions, by owner decision (the row and identifier remain).
- **Conditional or scoped:**
  - GR §8 (iii);
  - the conclusion of A.8's proof, and A.9's inherited scope;
  - A.7, now restricted to D in a configuration, which is the strongest form the lemma supports.
- **Preserved, by owner decision:** A.8–A.9 as conditional mathematical results with their hypotheses
  and evidence.

## Counts (computed, K7)

Each stated count is checked against its table, with no number hard-coded. A merge that leaves a stale count fails.

| Table | Stated count | Rows counted |
|---|---|---|
| Appendix A G-table | "Counts: 5 C + 2 L. Total: 7." | 5 C + 2 L; G11 uncounted |
| Appendix A SM table | 23 | 23 |
| Appendix A neutrino table | 7 | 7 |
| Appendix A biology/medicine table | 12 S + 2 C | 12 S + 2 C |
| "\<n\> gravitational(-sector) entries" | "seven", at 22 sites (11 in chapters, preface and appendices; 11 in FULL) | 7 |
| ch09 tiers (chapter and FULL) | "Four universality-class entries tested", "Tier 1 has four entries", "The seven Tier 2 entries", "Tier 2 has seven entries", "The eight Tier 3 entries", "Tier 3 has eight entries", "The three tiers contain nineteen entries" | Tier 1 = 4, Tier 2 = 7, Tier 3 = 8, total 19 |

Mutation tests: changing "5 C … 7" to "6 C … 8" and "four" to "five" failed K7 on both; restoring "The three
tiers contain twenty entries" in the chapter and FULL failed K7 on both files with
`wrong [('three tiers contain twenty entries', 20, 19)]`.

## Re-grep (`sc36_checks.py`, K5; papers/*.md and book/*.md, Introduction excluded)

Each of these retired phrases now has a count of 0:
- "resolves the paradox";
- "Resolved at the level of information preservation";
- "at the level of information preservation";
- "Problems resolved";
- the 1/(96π²)–8/3 range;
- "reproducible from a finite deterministic substratum";
- "it can be combinatorial";
- "| BH information preserved |";
- "Preserved; Page curve conditional";
- "Five universality-class entries";
- "Tier 1 has five entries";
- "second dissolution: the black hole";
- "*same* structural resolution";
- "preserves information with the Page curve";
- "information-preservation half";
- "of Theorem A.7's proof and";
- A.7's `|\chi_D\rangle` hypothesis;
- "Bound for the cosmological + stellar".

e^{−10^77} now appears only on A.8's proof line. The surviving counts are recorded in `sc36_checks.out`. `papers/Introduction.md` is untouched.

## Lean

No Lean theorem bears on GR A.5–A.9 or on the book sites: `GR:T-a.7`, `T-a.8` and `T-a.9` are GAP, not formalized, and none has a census entry. **Nothing requires a formal change.** `lean-manuscript-census.json` is not touched.

## Coverage

`GR:T-a.7` is re-affirmed under the same ID at the same grade (GAP): fingerprint ef7fd4160d9c1506 → d1d4eef7e2582a07, line 815 → 813. A.8's census statement (its first paragraph) is unchanged.

## Owner items

- **G11 decided:** it is an open research target, not counted (applied above).
- **Class letters.** G11's cell reads "Open research target (not counted)". The A.2 classification scheme has no letter for open targets, and no letter was invented for it.

## Cross-unit dependencies and reconciliation notes

- **GR A.8 scope.** This covers A.8's statement (no instance; H-scramble's operative bound) and its entropy-budget paragraph. Introduction §5 (R-01, r32) and any unit quoting A.8's "for all but an exponentially negligible fraction" depend on it.
- **GR A.7.** The theorem is restricted to D in a configuration. **Introduction L298 (r32) must add "from an initial state in which D is in a definite configuration".** Any unit citing A.7's purity or the boundary-only lemma's freezing is affected.
- **GR A.5.** Its chain V↔B↔D is a hypothesis; the A.1 geometry has B↔V↔D. The 30 M_⊙ orders are not derived for that black hole.
- **10^122 convention factor** (GR:366, ch07:193, appendix A:117). PR-A / SC-37 edit GR §6 and ch07 §7.7 (SC-37 also edits GR:374 and ch19:38, not these lines).
- **ch09.**
  - SC-37 conflict at ch09:125/126 and FULL:2605/2606. On reconciliation, drop the BH row (this unit's) and keep SC-37's dark-sector row; SC-37's text is not pre-applied here.
  - SC-37 also moves the dark-sector entry out of Tier 1 ("Dark-sector budget: Tier 2 — conditional"). The
    reviewer verified the correct merged ch09 text against SC-37: Tier 1 = 2, Tier 2 = 9, Tier 3 = 8, total
    19; "Two universality-class entries tested …: one confirmed at high precision (the area law) and one
    consistent with the empirical record (no proton decay)."; then this unit's information-conservation
    sentence, then SC-37's dark-sector Tier 2 sentence; "Tier 1 has two entries …", "Tier 2 has nine
    entries", "The three tiers contain nineteen entries".
  - A wholesale "ours" resolution passes K7 but fails SC-37's §2c; a wholesale "theirs" resolution passes
    both while reinstating the BH row, which only K5's retired-phrase grep catches. The resolution must
    therefore be by merits, and K5, K7 and SC-37's §2c must all be re-run on the merged tree. The owner
    requires that this unit's deletion of the BH row survive.
- **ch18.**
  - :130 and :146 are changed here. SC-37 retitles ch18:142 and :144; resolution "keep both". ch18:142 is not edited here.
  - Headings: SC-37 owns :142, :152 and :160 and applies this unit's :146 heading text identically
    ("**The second component: the black hole information paradox.**"), so the merged sequence is
    coherent with "not resolved". This unit keeps :146 as it is and does not edit :142, :152 or :160.
- **ch19.** :20 is the same change as SC-37's ("Problems addressed"), which merges identically. :22, :30, :72 and :334 are also changed.
- **Gravitational counts.** "seven gravitational(-sector) entries" appears at 22 sites, and appendix A:115/:225 carry the G-table counts. Any unit editing those sentences or the G-table must keep K7 green.
- **BHa `REPORT.md` and `SHA256SUMS`.** PR-I (S9-M6, BHa REPORT:61–62) changes the same checksum line, which must be recomputed on merge.
- **Open PRs #961–#971.** None edits a line changed here.
  - #964 (SC-22) changes FULL:6715–6716 and the glossary next to the Page-curve entry, with one unchanged line between them.
  - #962, #967 and #971 change GR:368.

## Open, for #970

- **Route (a).** This is an observation, not adopted. For Haar-random initial ψ₀ and any unitary, the time average of S(ρ_R) concentrates at Page's mean by Lévy's lemma, with no scrambling hypothesis. The Page value then comes from the initial ensemble. No constants or written proof are supplied.
- **Realization.** It is open whether the substratum supplies an initial superposition over ≥ e^{S_Page} configurations, or a bipartition not aligned with the configurations. A non-vacuous G11 needs this, a valid proof and independent verification.
- **A.5.** Its decomposition for the A.1 chain B ↔ V ↔ D is open.
- **A.7 for a superposed D.** It is open what replaces A.7 when D's initial state is a superposition and the V∪B dynamics depends on D's configuration.

## Checks (at the head of this branch)

- `python3 -I sc36_checks.py 0d917665` → `sc36_checks.out`: all controls pass, including the must-fire K3b and the computed counts K7.
- `python3 -I sc36_scan.py 0d917665` → `sc36_scan.out`: 0 hits for §A.32/§A.33 phrases, revision voice, caps, secrets and local paths. The .out files and the scan's own pattern file are excluded from the scan.
- `tools/release_gate.py`: all steps pass except `lean-axioms` (no local toolchain).
- `tools/coverage_check.py`: OK.
- `verification/lean/edge_rigidity_probe.py`: all pass.
- **Builds:** GR goes from 88 to 90 pages, median 3,228 characters per page. The book stays at 558 pages, median 3,058.
