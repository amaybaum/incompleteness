# Introduction r6 (rescoped): corpus overclaims r6 must not lean on

These are corpus sites at `687e885b` that state more than their support. They are listed for the paper's three
topics: quantum emergence, the cosmological constant and black-hole information. The corrections belong to
**separate, reviewed manuscript-consistency changes** under:
- §A.14 and §A.25: mirrors, paraphrases and counts;
- §A.27 and §A.30: correct in place;
- §A.25 step 5: regenerate or flag `GR.tex/.pdf` and `FULL.tex/.pdf`.

r6 edits none of them.

**Rule for r6.**
- Its text stands on its own permitted sentences (`OUTLINE-r6.md`) and the Results register.
- It does not quote, paraphrase or cite any site below for the overclaimed content.
- Where it cites a document containing such a site, it cites the anchor in the "r6 cites instead" column.

**Sources:**
- AUDIT §9;
- R11 FINDINGS, as amended by REVIEW.md (including M1–M12);
- the r5-design review (R18, R19, §6);
- #936 DIFF-REVIEW §6 and R1.

FULL mirrors were byte-checked by the audit and by R11.

## A. Cosmological constant (AW-2, AW-4, AW-5, AW-6)

| Site (FULL) | Overclaim | r6 cites instead |
|---|---|---|
| GR:24 | "is dissolved by …", then qualified (§A.30 pattern) | GR:356 sentences 1–4 |
| GR:356, last two sentences | "never enters the stress-energy tensor; no decoupling mechanism is needed", which asserts and then qualifies | GR:356, up to "the dissolution is conditional" |
| GR:360; ch07:201 (2078) | "eliminates the 122-digit cancellation entirely" | GR:360 sentence 2 ("set by initial conditions via the Friedmann equation") |
| GR:366; ch07:195; Explainer:549 | "the value the framework expects" / "independent reason to expect" | `cc.py` (a normalization and a dimensional identity) |
| GR:583 | "a theorem of the reconstruction … gauge degree of freedom", which contradicts GR:356 | GR:356 |
| GR §6.3; ch07 §7.7 | "a triangulation that strengthens the empirical case for both programs" (§A.32) | — |
| GR:581 (§8.3) | classifies the Higgs shift as not gravitating; the rule does not decide phase transitions (AW-3) | — (r6's N-CC7 states it is open) |
| ch07:167 (2044); ch02:192 (835); Explainer:533 | "dissolves", unconditional | GR:356, up to "the dissolution is conditional" (R19) |
| ch19:330 (5506) | "Dissolved (10¹²² = S_dS)" | GR:356, up to "the dissolution is conditional" (R19) |
| ch19:38 (5214) (R19) | states the condition ("the dynamical form is conditional on the covariant coupling theorem"), then asserts unconditionally "The QFT zero-point energy … does not gravitate" and "The 10¹²² discrepancy is the de Sitter entropy" (§A.30). **Not usable as an anchor** | GR:356, up to "the dissolution is conditional" |
| preface:7 (78) (R19) | "The cosmological constant discrepancy of 10¹²² … becomes a calculable compression ratio" | — |
| ch00:89 (325), CC clause (R19) | "The 10¹²² vacuum-energy discrepancy as an information compression ratio", listed among results that "all follow from the single statement that observation occurs" | — |
| Explainer:22 (R19) | the 10¹²² discrepancy "is the strongest piece of existing evidence we have that quantum mechanics is not the fundamental bedrock of reality" | — |
| Explainer:547 (R19) | "The 10¹²² ratio between the two answers is not a discrepancy. It equals S_dS" | `cc.py` (a dimensional identity whose factor depends on the cutoff convention) |
| appendix-a:113 (G7, 5666), :119 (G14, 5672) | class S for a descriptive relation and a normalization identity | — |
| **Naming** | "G3" names three objects: GR's covariant field equations, the appendix-a ħ row, and Structure/ch03's gauge group (AW-6) | r6 always writes "the covariant field equations (Level G3 of [GR])" |

## B. Quantum emergence and scope

| Site (FULL) | Overclaim | r6 cites instead |
|---|---|---|
| Main title | "The Equivalence of Quantum Mechanics and Embedded Observation". **Owner decision.** r6's bibliography cites the title; r6's text says "finite-horizon correspondence" and never "equivalence of quantum mechanics" | Main's abstract scope; `oi_alone_not_qm` |
| GR:567 | "so the equivalence applies in our universe", which contradicts GR:20 and GR:52 | GR:20, GR:52 |
| GR:711 | "quantum mechanics emerging as the unique self-consistent description …"; "[Main] establishes the equivalence …" | — |

## C. Black hole (R11, adopted as amended by REVIEW.md)

**r6's statement, N-BH3, is independent of these corrections landing:** it states the conditions itself. r6 must not
cite any of the following for the overclaimed content.

**Primary sites (REVIEW §1):**
- ch07:110 (1987): "resolves the paradox … because φ is bijective". REVIEW: claims more than its support.
- ch07:126 (2003) s1 and s2: the derivation is attributed to combinatorics; "PSW corrections vanish exponentially"
  (false at turnover).
- ch07:159–161 (2036–2038): an empty falsifier.
- ch18:146 (4966): resolution from bijectivity; the Page curve unconditional.
- ch18:158 (4978): "(which it does, through the nested partition)".
- ch19:334 (5510): "Resolved (Page curve from typicality)".
- GR:811: a false decoupling inequality (≥ 10⁵⁷).
- GR:869: "invokes only PSW … no ergodicity assumption"; undefined "horizon-factorization hypotheses" (O-5).
- **GR:841–847, Thm A.9 "Proof. Direct substitution"**: SITE-ERROR of proof scope (REVIEW §C.4). A.9 is to be
  restated for cycle averages, or a pointwise hypothesis named (owner). r6 never cites A.9 as a pointwise curve.
- **R12, ch18:148 (4968):** "mass-independent fraction", missing the constant-coefficient condition. The Page time is not in r6; this is listed for completeness.
- **GR Thm A.8 (GR:817–839), statement level (#936 DIFF-REVIEW §6):** the Page value $S_{\rm Page}(d_B,d_R)$ holds
  only when the energy shell is the full product space; on the diagonal shell the Haar mean is exactly $H_m-1$. The
  cycle-averaged A.9, the turnover at $d_R=d_B$ and min·ln q inherit this. The remedy is the owner's (review O3). r6
  states the full-product-shell scope itself (N-BH2, N-BH3).
- **H-decouple (#936, DIFF-REVIEW R1):** the accepted definition is closure of B∪R in a pure joint state, with no
  coupling to D or V∖R, over whole cycles. r6 states it in words; the label waits for #936 to land.

**Paraphrases (FINDINGS §D plus REVIEW §3):**
- ch07:12 (1889); ch09:108 (2588); the ch07:118 heading (1995); GR:611; glossary:113 (6735); ch07:132 (2009);
  ch07:151 (2028); GR:871.
- The REVIEW additions:
  - **M1** GR:605: "the Page curve follows under … H-scramble" (sufficiency form).
  - **M2** book/README.md:64.
  - **M3** ch07:149 (2026): an exhaustive open-steps list that omits decoupling, A.8 → A.9 and C6(c).
  - **M4** ch07:116 (1993); **M5** GR:717 ("deriving the Page curve under … H-scramble").
  - **M9** ch18:156 (4976); **M10** ch07:130 (2007).
- **Sufficiency forms needing the decoupling condition (O-1, mandatory):** GR:841, :717, :605, :611, :869 (last
  sentence); ch07:116, :149; ch19:72; the replacement text for ch18:146.
- **Assumption watch:**
  - **M6:** GR Thm A.7's proof restricts a pure state on V⊗B to a pure state on B⊗R, which is a second implicit
    decoupling. r6 makes no claim that A.7 holds; it carries only the non-claim that it is not shown to fail within
    its stated scope.
  - **M7:** GR:829 cites PSW for an entropy bound (Lévy/HLW).
  - **M8:** the book bibliography lacks PSW and Page 1993.
  - **M12:** "B" means two different things across GR A.5 and §3.2.

**r6 cites instead:**
- BH-01 REPORT:17, :36 (claim A) for the preservation-versus-recovery split. ch19:72 states preservation only (R18).
- GR:817 and :841 for the theorem labels only.
- BH-01 and BH-02 REPORT lines, as in CLAIMS.

**The R11 markers in r6** stay as landing gates, under the owner rule of 2026-10-26: neither the Introduction nor any
existing manuscript is authoritative. Each marker names the REVIEW verdict for its site.

## R. Topics outside the paper: not leaned on

These sites concern topics the owner removed from the paper on 2026-10-26. r6 neither states nor cites their content.

**Handled only by PR #937** (per the coordinator):
- **Horizon entropy and the 1/4 (AW-1).**
  - GR:12, :24, :162, :320, :322, :546, :707;
  - Explainer:477;
  - ch07:12 (1889), ch07:104 (1981);
  - ch00:21 (257): "derivation rather than a postulate";
  - preface:7 (78): "The Bekenstein-Hawking factor of 1/4 in black-hole entropy becomes a derivation" (quotation
    corrected, R18);
  - ch00:81 (317), ch00:89 (325);
  - glossary:17 (6639);
  - appendix-a:110 (G4) and :93 (row 24).
- **Cabibbo.**
  - appendix-a:74 (5627), class S: under AGENTS, S needs every link Solid.
  - SM:849 asserts "established at the structural level rather than merely hypothesized" in the same paragraph as
    "This is a hypothesis, not a derivation" (§A.30; R19). AUDIT cites both at SM:851 (R18).
  - The dispersion was selected against data (SM:851).
- **JUNO.** Juno.md and appendix-a:81–97: the central value postdates JUNO's first result, and the 4/3 ratio
  (`77ac23ce`) postdates the comparison.
- **Echoes (AW-12).** GR:603 against ch18:164–180 (4984 ff.) and appendix-a:183 (F5) and :208.

**Outside the paper and not leaned on; routed to the separate consistency change (review O5):**
- **The past-hypothesis family**, confirmed by the independent review (review §6):
  - Main:726 and Main:740 (the title "past-hypothesis replacement", the last sentence, and "SUFFICIENTLY
    FAST-MIXING" in capitals, §A.33);
  - Substratum:56; Substratum:356 ("No additional axiom is needed");
  - Explainer:930;
  - Complexity:204.
- **Measurement:** ch19:333 (5509) and Main:666, "Dissolved" / "the Everettian measure problem dissolves" (AW-7).
- **Counts and summaries:** ch18:349 (5169), ch19:362 (5538), ch19:28 (5204), ch19:339 (5515), GR:709, ch19:336
  (5512), ch19:370. r6 states no count of predictions or problems.
- **Dark sector and a₀:** ch00:89 (a₀ clause), GR:709, G6, G9.
- **AW-9:** the status scheme has no postdiction marker (owner, review O6).

## H. Gates on r6 itself

| Gate | Item | Condition |
|---|---|---|
| Lean retention | the code section; "machine-checked" | An expected result for `687e885b` is retained, or the commit falls inside an archive the evidence-retention step covers (§A.42; decision 2). Carried from r4 |
| R11 | §5, the abstract, §6 limitation 4, the conclusion | Landing gates per the r4 markers (owner rule of 2026-10-26). R12 (Page time) is dropped with its content |
| #936 | the label "H-decouple" | Used only once #936 lands and the owner adopts the label with DIFF-REVIEW R1's definition. r6's wording holds without it |
| VERIFY | [BBS24], [Cal26], [CT06], [Har04], [Sha79] (r4); [tH14], [EvEMU11], [KP14], [Vol06] (new) | Read the body, or keep the sentence at abstract strength. 9 markers |
| To-read list | Weinberg 1989, Padmanabhan, Adler 2004, Wetterich, Spekkens 2007, Elze | Nothing is claimed from them until read |
| Census | the Introduction's identifiers | `lean_manuscript_census` is vacuous for this paper (it resolves only `(kernel: …)` parentheticals). Re-run `identcheck.py` on the r6 draft, or extend the tool (§A.35) |
