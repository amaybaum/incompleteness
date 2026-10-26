# Introduction r5: corpus overclaims r5 must not lean on

These are corpus sites at `687e885b` that state more than their support. The corrections belong to a **separate,
reviewed manuscript-consistency change**: §A.14 and §A.25 (mirrors, paraphrases and counts), §A.27 and §A.30
(correct in place), and §A.25 step 5 (regenerate or flag `GR.tex/.pdf` and `FULL.tex/.pdf`). r5 edits none of them.

**The rule for r5:** its text stands on its own permitted sentences (`OUTLINE-r5.md`). It must not quote, paraphrase
or cite any site below for the overclaimed content. Where r5 cites a document that contains such a site, it cites
the anchor named in the "r5 cites instead" column.

Sources:
- AUDIT §9;
- R11 FINDINGS as amended by REVIEW.md, including REVIEW's missed sites M1–M12;
- AUDIT §§3.3, 5 and 7.

FULL mirrors were byte-checked by the audit and by R11.

## A. Horizon entropy and ħ (AW-1: the 1/4 is a calibration identity)

| Site (FULL) | Overclaim | r5 cites instead |
|---|---|---|
| GR:12, GR:24 | "obtains … the 1/4 coefficient by direct boundary-mode counting"; "follows by mode counting" | GR:148 (Step 4), GR:310, GR:320 ("whatever σ"; 2π/8π) |
| GR:162; Explainer:477 | "Any alternative ħ(ε) would fail …" (circular) | — |
| GR:320 | "historically introduced as a proportionality constant" | — |
| GR:322; GR:546 | GW250114 presented as "observational confirmation" in the 1/4's context; "derived (2π/8π)" | — (r5 non-claim: GW250114 tests the area law) |
| GR:707 | "direct mode counting … structural constant rather than an empirical fit" | — |
| ch07:12 (1889), ch07:104 (1981) | "derives … by direct boundary-mode counting"; "a derived structural constant" | — |
| ch00:21 (257), preface:7 (78), ch00:81 (317), ch00:89 (325) | "derivation rather than a postulate"; "1/4 … from mode counting"; "as a derivation" | — |
| glossary:17 (6639) | "conventionally treated as a postulate … derives the 1/4" | — |
| appendix-a:110 (G4, 5663), :93 (row 24) | class C, "No direct test", where it should be an identity like G14 | — |

## B. Cosmological constant (AW-2, AW-4, AW-5, AW-6)

| Site (FULL) | Overclaim | r5 cites instead |
|---|---|---|
| GR:24 | "is dissolved by …", then qualified (§A.30 pattern) | GR:356 sentences 1–4 |
| GR:356, last two sentences | "never enters the stress-energy tensor; no decoupling mechanism is needed", which asserts and then qualifies | GR:356, up to "the dissolution is conditional" |
| GR:360; ch07:201 (2078) | "eliminates the 122-digit cancellation entirely" | GR:360 sentence 2 ("set by initial conditions via the Friedmann equation") |
| GR:366; ch07:195; Explainer:549 | "the value the framework expects" / "independent reason to expect" | `cc.py` (a normalization and a dimensional identity) |
| GR:583 | "a theorem of the reconstruction … gauge degree of freedom", which contradicts GR:356 | GR:356 |
| GR §6.3; ch07 §7.7 | "a triangulation that strengthens the empirical case for both programs" (§A.32) | — |
| GR:581 (§8.3) | classifies the Higgs shift as not gravitating; the rule does not decide phase transitions (AW-3) | — (r5's N-CC7 states it is open) |
| ch07:167 (2044); ch02:192 (835); Explainer:533 | "dissolves", unconditional | ch19:38 (5214), conditional form |
| ch19:330 (5506) | "Dissolved (10¹²² = S_dS)" | ch19:38 |
| appendix-a:113 (G7, 5666), :119 (G14, 5672) | class S for a descriptive relation and a normalization identity | — |
| **Naming** | "G3" names three objects: GR's covariant field equations, the appendix-a ħ row, and Structure/ch03's gauge group (AW-6) | r5 always writes "the covariant field equations (Level G3 of [GR])" |

## C. Emergence of QM and scope

| Site (FULL) | Overclaim | r5 cites instead |
|---|---|---|
| Main title | "The Equivalence of Quantum Mechanics and Embedded Observation". **Owner decision.** r5's bibliography cites the title; r5's text says "finite-horizon correspondence" and never "equivalence of quantum mechanics" | Main's abstract scope; `oi_alone_not_qm` |
| GR:567 | "so the equivalence applies in our universe", which contradicts GR:20 and GR:52 | GR:20, GR:52 |
| GR:711 | "quantum mechanics emerging as the unique self-consistent description …"; "[Main] establishes the equivalence …" | — |
| Main:726 | "replaces [the past hypothesis] … with a theorem conditional on (EM)". A selection rule on where observers can exist does not by itself supply low initial entropy, so "replaces" exceeds the conditional theorem. **This is a design finding, not in AUDIT §9; it is for review** | Main:730 (theorem statement only) |
| Substratum:356 | "No additional axiom is needed" (AW-8) | Main:730 |
| ch19:333 (5509); Main:666 | "Measurement problem — Dissolved"; "the Everettian measure problem dissolves" (AW-7) | Main:632 (diagonal sector only) |

## D. Black hole (R11, adopted as amended by REVIEW.md)

**r5's statement, N-BH3, is independent of these corrections landing:** it states the conditions itself. r5 must not
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
  restated for cycle averages, or a pointwise hypothesis named (owner). r5 never cites A.9 as a pointwise curve.
- **R12, ch18:148 (4968):** "mass-independent fraction", missing the constant-coefficient condition.

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
    decoupling. r5 makes no claim that A.7 holds; it carries only the non-claim that it is not shown to fail within
    its stated scope.
  - **M7:** GR:829 cites PSW for an entropy bound (Lévy/HLW).
  - **M8:** the book bibliography lacks PSW and Page 1993.
  - **M12:** "B" means two different things across GR A.5 and §3.2.

**r5 cites instead:**
- ch19:72 (5248) for the preservation-versus-recovery split. Its Page-curve sentence is a sufficiency form (O-1), so
  r5 does not cite that sentence.
- GR:817 and :841 for the theorem labels only.
- BH-01 and BH-02 REPORT lines, as in CLAIMS.

**The R11 markers in r5** stay as landing gates, under the owner rule of 2026-10-26: neither the Introduction nor any
existing manuscript is authoritative. Each marker names the REVIEW verdict for its site.

## E. Counts and evidential summaries

| Site (FULL) | Overclaim | r5 rule |
|---|---|---|
| ch18:349 (5169) | "Twenty-two parameter-free SM predictions match observation. Thirteen gravitational …" — contradicts appendix-a:95, :121, :231 | r5 states **no count** of predictions |
| ch19:362 (5538) | "preregistered structural predictions matching observation" — contradicts appendix-a:217 | r5 cites appendix-a:217 ("no pre-registered forward confirmation") |
| ch19:28 (5204) | "seven independent consistency checks and no fitted parameters" — GR:358 says that item (7) includes fits | — |
| ch19:339 (5515); GR:709 | dark-sector budget "Derived" / "explains ~95%" (G9 is "partly definitional") | excluded from r5 |
| ch00:89 (325) | a₀ = cH/6 "parameter-free prediction" (factor imported) | excluded |
| ch19:336 (5512) | "Hierarchy problem — Dissolved" (outside the audit's scope; flagged) | excluded |
| ch19:370; ch19 heading 19.2 | "ten disparate hard problems" — recount after the ch19:334 and :330 changes (REVIEW M11) | r5 states no count |

## F. Classification

- **appendix-a:74 (5627), Cabibbo S.** Under AGENTS, S needs every link Solid. SM:849 says "a hypothesis, not a
  derivation", and the dispersion was selected against data. The proposal is C, with a postdiction marker (AW-9).
  The same question applies to rows 6, 10, 11, 13 and 22, which are not audited. **r5 rule:** call the Cabibbo form a
  postdiction (N-EX2) and quote no class.
- **The S/C/L/… scheme has no postdiction marker (AW-9).** This is a methodology item for the owner. r5 uses its own
  status key, N-INT3.

## G. Echoes (AW-12)

GR:603 says there is "no OI-specific echo", and its null stack agrees. ch18:164–180 (4984 ff.), appendix-a:183 (F5)
and :208 list echoes as a forward prediction, so one side must be corrected. **r5 rule:** echoes are not mentioned.

## H. Gates on r5 itself

| Gate | Item | Condition |
|---|---|---|
| PE-01 | §5.4 and [PE01] | The package lands on `main` (#923, branch `research/oi-pseudoentropy-20261025` at `efbfd0d7`) with its expected result retained (§A.42). Until then §5.4 is omitted |
| Lean retention | the code section and "machine-checked" | An expected result for `687e885b` is retained, or the commit falls inside an archive the evidence-retention step covers (§A.42; decision 2). Carried from r4 |
| R11 | §5.2, the abstract, §7 item 4, the conclusion | Landing gate per the r4 markers; owner rule of 2026-10-26 |
| VERIFY | [BBS24], [Cal26], [CT06], [Har04], [Sha79] (r4); [tH14], [EvEMU11], [KP14], [Vol06], [Haw75] (new) | Read the body, or keep the sentence at abstract strength |
| Census | the Introduction's identifiers | `lean_manuscript_census` resolves only `(kernel: …)` parentheticals and is vacuous for this paper (ed RECHECK-r3 §6). Re-run `identcheck.py` at landing, or extend the tool (§A.35) |
