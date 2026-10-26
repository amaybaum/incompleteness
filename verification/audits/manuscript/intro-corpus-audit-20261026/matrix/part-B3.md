# Mapping part B3: I-172 to I-245 (§4 the cosmological constant, §5 black-hole information)

**Objects:** `papers/Introduction.md` at `4a260ca9`. The corpus is `main` at `eae01647`, read from the `tree939` extraction, with `verification/programmes/black-hole-information/**` read by `git show eae01647:`. Rows are in `part-B3.json`.

## Counts

74 rows: I-172 to I-245. No claim in this range has directional sub-claims.

| Verdict | Count | IDs |
|---|--:|---|
| FAITHFUL | 64 | all others |
| IMPRECISE | 9 | I-182, I-208, I-209, I-217, I-218, I-219, I-220, I-222, I-225 |
| MISCITED | 1 | I-206 |
| OVERCLAIM / UNDERCLAIM / UNSUPPORTED | 0 | — |

§4 is faithful throughout, apart from one label ambiguity (I-182). The cosmological-constant passage matches GR §6.1–§6.3 and §8.3, its dependency ladder at GR.md:12 and the book mirrors, including the conditional status and the open G3 rung.

## Non-FAITHFUL rows, by severity

1. **I-225, IMPRECISE (moderate).** The sentence "For all but an exponentially negligible fraction of initial conditions … equals the Page value" leaves out one fact: Theorem A.8 counts its initial conditions as configurations of Σ_E, with the bipartition aligned (GR.md:817, :837–841). In exactly that setting, H-scramble fails for every bijection and the conclusion fails for every initial configuration. The sources are GR.md:833, BHb C6(a), and the BHb review at REVIEW.md:69–76, which recommends A.8's counting as the anchor. GR attributes the failing setting only to "Theorem A.7's proof" (GR.md:835). The conditional is therefore vacuous where its fraction is counted.
   - **Fix:** extend the I-227 sentence with "…aligned to the configuration coordinates, which is the setting in which Theorem A.8 counts its initial conditions; it requires an initial superposition of configurations or a bipartition not aligned with them, and is not established".
2. **I-206, MISCITED (low–moderate).** [Pag93], "Average entropy of a subsystem", is cited for the statement of the information problem. Its abstract is about the entropy of random pure states. Page's black-hole paper from the same year is "Information in black hole radiation", PRL 71, 3743, hep-th/9306083. This was checked at abstract level only.
   - **Fix:** use [Haw76; Pag13], or add the hep-th/9306083 entry. Pag93 stays at I-225.
3. **I-217 / I-218, IMPRECISE (low).** BHa proves P_succ ≥ 1/|U| and the |U| ≥ |M| requirement under a uniform message prior with uniform unread data (BHa REPORT:297). The "so" step in I-218 uses 1/|M| as the blind guess. Resolves the I-218 attention item.
   - **Fix:** one sentence stating the prior.
   - **Auditor's note, not in the corpus:** the bound itself holds for any prior.
4. **I-208, IMPRECISE (low).** "The results below are finite computations" misdescribes written universal proofs (BHa C1/C2, BHb C1) and GR's analytic conditional theorem. §6.2 item 4 of the Introduction describes the same results correctly.
5. **I-209, IMPRECISE (low).** This is the surrogate check of the Code Review Rules. The toy results use the construction's layout with arbitrary bijections, not the substratum dynamics (BHa REPORT:288–292).
6. **I-219, IMPRECISE (low).** Resolves the attention item. The population is the 256 self-maps of {0,1}², with a two-bit message and one register unread, so |U| = 2 and the bound is 1/2. The 32 maps are exactly those whose read register is constant (2·2⁴).
7. **I-220, IMPRECISE (low).** Resolves the attention item. The conditions are sufficient for recovery (exact recovery under C1, the P_succ floor under C2) and not necessary for it: 14,496 and 36,416 bijections recover exactly with registers unread (BHa REPORT:66–86).
8. **I-222, IMPRECISE (low).** BHa's C4 rank bound is proved. Its identification with the secret-sharing threshold rests on [Sha79], which nobody has read (VERIFY; #918 FINDINGS: UNREACHABLE).
9. **I-182, IMPRECISE (low).** GR uses "Level G1–G4" for two objects: its dependency ladder, and Structure's gauge axis (GR.md:30, :597, :681). This is signal S12. Suggest "rung G3 of the dependency ladder of [GR]".

## Attention items resolved

- **I-218:** the uniform message prior is required for the inference as written. See item 3.
- **I-219:** the population is the 256 maps of {0,1}² with a two-bit message, one step and one register unread. See item 6.
- **I-220:** sufficient and not necessary for recovery. See item 7.
- **I-227:** FAITHFUL. "H-scramble fails for every bijection" does not rest on unpublished BHb C1 alone.
  - It is a one-line universal written proof: a permutation unitary maps basis vectors to basis vectors, and these are product states across an aligned cut.
  - The published corpus states it at GR App. A.7 (GR.md:833) and ch07:126.
  - BHb's sweeps only exercise the code (BHb REPORT:194–195).

## The questions from the brief

- **ħ (#939): no §4 statement depends on ħ's status.**
  - The offset invariance holds for any constant shift of Ω_eff (GR.md:140, :356).
  - The Planck-cutoff/de Sitter relation is a dimensional identity with the measured ħ.
  - GR's reading of the ratio as the compression ratio does share the calibration (GR.md:162). The Introduction does not adopt that reading.
  - #939's rewording of ch09's CC-distinction rows is consistent with the Introduction.
- **Weinberg placement:** matches WEI89.md's applied Option A exactly. [Wei89, §I; §III, Eqs. (3.4)–(3.6)] follows "observational value", [Wei89, §III] follows the cancellation clause, and the convention clause is uncited.
- **GR Thm A.7 / I-267:** A.7 is the Effective-pure-state theorem (GR.md:811). BHa item F removes its timescale support beyond t ≪ τ_B^D. It does not show A.7 false within that scope, which agrees with §6.2 item 4.

## Corpus findings (for CONSISTENCY.md; not Introduction edits)

1. **GR Thm A.8 is stated in a setting where its hypothesis fails for every φ.** GR.md:817 and :837–841 sit against :833–835. Appendix A row G11 classes the Page curve C with "scrambling … open" (appendix-a:111). In the configuration setting the scrambling hypothesis is refuted, not merely open. ch19:72 omits the failure that ch07:126 states.
2. **"Resolved at the level of information preservation."** ch07:110 (FULL:1989), ch19:72 (FULL:5232) and the "19.2 Problems resolved" title differ from the Introduction's "not resolved". Under BHa, preservation is the premise, and recovery is the problem.
3. **"Dissolution" headings are stronger than their conditional bodies.** GR §6 (GR.md:326), ch07 §7.7 (ch07:163) and ch19 §19.2 (ch19:20).
4. **Geometry-first requirement (iii) was not updated by #939.** GR.md:352 and ch07:185 say "ħ … determined by the boundary geometry", while ch07:305 says the calibration "fixes only the ratio ε/√σ = 2 l_p, not an independent determination of ħ". (iii) also omits the H-slope condition.
5. **GR.md:573 is unconditional.** It says "The framework denies that the absolute zero-point sum gravitates", while GR.md:581–583 conditions the same claim on the coupling step.
6. **Label collision S12 inside GR:** the G-levels name both the ladder and the gauge axis.
7. **Signal S10:** bijectivity is "premise/part-empirical" in Main.md:708 and the Introduction, and a "lemma" in Methodology.md:158 and :166.

## Completeness (candidates for COMPLETENESS.md)

These are established, related results that the Introduction does not report. None is required for its scope.
- BHb C2, proved: under a permutation, aligned-cut entanglement is capped by the initial basis entropy H(p₀). H-scramble would therefore need an initial state spread over about e^{S_Page} configurations.
- GR Thm A.6: the sector-entropy inequality, proved on paper.
- BHa D1: accessible advantage is monotone under cumulative records.
- BHa C4: the linear rank law.

## For the owner

1. Whether §5 should say that A.8's own counting setting is the one where H-scramble fails (recommended: item 1).
2. Whether to keep [Pag93] at line 156.
3. Whether to resolve the [Sha79] VERIFY or drop the citation.
4. Whether the corpus findings 1–5 go to separate correction proposals.
