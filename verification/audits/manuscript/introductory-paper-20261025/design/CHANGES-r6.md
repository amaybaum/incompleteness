# Introduction design r6: changes

## What this applies

1. **The owner's scope decision of 2026-10-26.** "One fundamental idea with two major consequences, rather than a
   catalogue of possible applications." The three topics are quantum emergence (the thesis), the cosmological
   constant (the leading application) and black-hole information (the second application). Both applications must
   be stated explicitly as not demonstrated resolutions.
2. **The owner's direction of the same day.** The paper cites derivations rather than re-deriving them. Each result
   carries its exact statement, status, reference and §A.34 witnesses, and the proof sketches become citations.
3. **The r5-design review** (`S/paper/design-r5-review/REVIEW.md`, ACCEPT WITH CHANGES), for every item that touches
   retained content. Items that touched only removed content are marked moot.

**Provenance.**
- The r5 design files are unchanged.
- A pre-scope r6, written before items 1 and 2, is kept in `design-r6/pre-scope/` and is superseded. Its sha256 values
  are `8966f83c…` (OUTLINE), `6299488c…` (CLAIMS), `c08a2098…` (CHANGES) and `3f5ab699…` (DEPENDENCIES).

## 1. Structure

| r6 § | Owner's heading | Content and origin |
|---|---|---|
| 1 | Introduction: OI and the emergence of quantum behaviour | r4 §1.1, verbatim; r4 §1.2 with the new one-idea/two-consequences sentence (N-INT1) and the adapted Contributions |
| 2 | Theoretical foundation | r4 §2 and r4 §3.1, with the sketches replaced by citations (§3 below) |
| 3 | Quantum emergence: demonstrated / open | r4 §3.2 (demonstrated); r4 §6.1–§6.3 plus the Born-exponent pointer and r4 §6.4(5) Bell (open) |
| 4 | Cosmological constant | pre-scope r6 §5.1 (R6–R9 applied); closes with the owner's caution |
| 5 | Black-hole information | pre-scope r6 §5.2 (R1–R3 applied), without the Page time |
| 6 | Discussion and conclusion | implications (N-DI1); limitations (r4 §6.5 adapted, R5, R12, a CC item); decisive open tests (N-DT1); conclusion |
| App. A | Kernel declarations | r4, verbatim |
| App. B | Examples | r4 §4.1, §4.2 and the card table (r4 §4.3), verbatim |

**Removed (owner):**
- horizon thermodynamics (pre-scope §5.3): no sentence is needed; §4 uses S_dS only as a standard quantity;
- PE-01 (§5.4); the arrow of time and the measurement reading (§5.5);
- the Cabibbo and JUNO items (§6.7 N-EX2/N-EX3); the status key (§5.0);
- the Page time and β (N-BH4);
- the dark sector, echoes and quantum computing (already excluded).

## 2. Review items

| Item | Status in r6 |
|---|---|
| R1 (A.8's full-product shell) | Applied verbatim (§5 N-BH2) |
| R2 (Page curve "not established"; H-decouple scope; GR:12 ladder) | Applied, with "in a pure joint state" added (Departures 1) (§5 N-BH3) |
| R3 (r4:172, s1–3 and s5) | Applied; s4 goes to §6 limitation 4 |
| R4 (β > 1) | **Moot: content removed.** The owner removed the Page time and β, which §5 does not need |
| R5 (non-claim 4) | Applied, minus its Page-time clause, which refers to removed content; "§5.2" becomes "§5" (Departures 2) |
| R6 (remaining vacuum term) | Applied verbatim (§4 N-CC4) |
| R7 (completions; "same partition" unverified) | Applied verbatim (§4 N-CC3) |
| R8 (visible statistics) | Applied verbatim (§4 N-CC1) |
| R9 (convention-dependent 10¹²² and factor) | Applied verbatim (§4 N-CC0, N-CC6) |
| R10 ("the one quantitative item") | **Moot: content removed.** No numerical item remains |
| R11 (JUNO) | **Moot: content removed** |
| R12 (non-claim 10, no priority) | Applied verbatim (§6 limitation 8) |
| R13 (arrow of time) | **Moot: content removed** |
| R14 (N-GC1, Page curve under the covariant field equations) | Applied in substance: the Page-curve dependence is in N-BH3, the CC dependence in N-CC2 and N-CC8, and both are in §6 N-DT1. The separate paragraph and its §5.3 clause are gone with that content |
| R15 (page arithmetic) | Superseded by the new 10–12 pp budget (§4 below) |
| R16 (abstract keeps memory and indivisibility) | Applied |
| R17 (look-elsewhere) | **Moot: content removed** (Cabibbo). The AUDIT correction is still recommended (§6) |
| R18 (line references) | Applied: N-BH1 does not cite ch19:72; DEPENDENCIES §C cites BH-01 claim A; preface:7's quotation is corrected (now in DEPENDENCIES §R); SM:849 is used |
| R19 (DEPENDENCIES sites) | Applied: §A (CC) carries preface:7, ch00:89, Explainer:22 and :547 and ch19:38, and ch19:38 is not used as an anchor. The Main:726 family (Main:740, Substratum:56, Explainer:930, Complexity:204) and SM:849 go to §R (outside the paper) |
| Nit 1 (N-HT1) | Moot: content removed |
| Nit 2 (§6.1 heading) | Applied in §3.2: "From the correspondence to operational quantum mechanics" |
| Nit 3 (§4 lead) | Adapted: the examples go to Appendix B with one pointer sentence in §2, keeping r4:128's "smallest realization of Theorem 3" |
| Nit 4 (N-INT2) | Applied |
| Nit 5 (N-EX2) | Moot: content removed |
| Nit 6 (PE-01 citation) | Moot: content removed |
| Nit 7 ("are defined at different levels") | Applied (§4 N-CC1) |
| Nit 8 (Weinberg) | To-read list; not cited until read |
| Nit 9 (in-repo AUDIT) | Applied |
| Literature (review O4; coordinator) | Weinberg 1989, Padmanabhan, Adler, Wetterich, Spekkens and Elze are listed to read; nothing is claimed from them |

## 3. Proof sketches replaced by citations (owner direction)

| r4 | Sketch removed | Citation now |
|---|---|---|
| r4:66 | Theorem 1, S ⊆ D construction steps: clock, record, injectivity, extension to a bijection | one descriptive sentence + [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); EGGH26, Prop. 13]. The prior-independence sentence and its status are kept |
| r4:68 | Theorem 1, D ⊆ Q non-disturbance argument | one descriptive sentence + [Main §3.4] |
| r4:92, last sentence | Theorem 2's data-processing proof | [Main §3.4, Theorem (unavoidable hidden predictive memory); CT06] |
| r4:94 | the Corollary's two direction arguments | citation form [Main §1.5], keeping a source for each direction (§A.34): ⇒ T2(a) per realization; ⇐ T2(a) with `S_imp_D`. Its not-machine-checked steps are named |
| r4:112, sentences 1–2 | Theorem 3's overlap-and-return route | removed; the theorem cites [Main §2.3] and its kernel identifier |
| r4:114, steps (1)–(3) | the readback ⇒ indivisibility route | the statement with [Main §2.3, Theorem (history readback + finite recurrence implies indivisibility)]. The status sentence (machine-checked from the routed form; on paper from history-level (C4)) is kept verbatim |

- **Intuition kept:** r4:108's contraction-criterion sentence, cited to [RHP14; BD16], and the two one-clause reasons in
  r4:78–80 (the Born exponent; periodicity). Each states what a cited result gives.
- **Exception kept:** the card table's Pauli-twirl decomposition, the one step not in the corpus. It stays in Appendix
  B as r4:162's sentence; its source is ERRATUM-r4, via Σ_o σ_o X σ_o = 2 tr(X) I.
- **Saving:** about 275 words, about 0.7 pp at 395 words per page. It is used toward the 10–12 pp target.

**Results register.** OUTLINE-r6 now carries one row per theorem and result (T1, PD, T2, C, CAP, PIN, SI, T3, RB, CP,
HAD, BORN, T4, IND, REL, BR, FC, BELL). Each row gives the exact statement with its hypotheses and quantifiers, the
status and layer, the reference, and the witness for each direction.

## 4. Theorems 1–4: nothing lost

- **Statements, hypotheses and quantifiers.** Carried verbatim: r4:58–62, :86–90, :110, :216.
- **Status words.** Carried verbatim: r4:64, :92 (first two sentences), :114 (last sentence), :218.
- **References.** Carried verbatim, and made explicit in the register.
- **§A.34 witnesses.** Carried verbatim:
  - Theorem 1: three directional identifiers and the assembly;
  - Theorem 4: ⇒ and ⇐ identifiers;
  - BR: forward direction only.
- **What was removed.** Only the derivation sketches listed in §3, each replaced by its citation.
- **Appendix A** is unchanged, so the identifier check (28 identifiers, 0 unresolved, 0 line mismatches) carries
  over. It is re-run on the r6 draft.

## 5. Page count

| Part | Words | Pages |
|---|---|---|
| Abstract | 240 | |
| §1 | 430 | |
| §2 | 980 | |
| §3 | 900 | |
| §4 | 530 | |
| §5 | 520 | |
| §6 | 500 | |
| **Total** | **≈4,100** | **≈10.4** (at r4's 395 words per page) |

- **Applications:** about 1,050 words, about 2.65 pp.
- **Fit:** inside the owner's 10–12 pp, and 2–3 pp for the applications. No qualification is cut.
- **If the build runs over 12 pp,** the first move is r4:226 to Appendix A. That needs a §A.34 re-check. Beyond it,
  the honest count is reported, not a cut.

## 6. Departures from a reviewer's exact text

1. **R2: "in a pure joint state" added.** This matches #936's accepted H-decouple (DIFF-REVIEW R1; DIFF-RECHECK §2)
   and the coordinator's definition. It is no stronger than the source.
2. **R5:** the clause "the Page-time fraction is conditional on its three inputs" is dropped because the owner removed
   that content, and "§5.2" becomes "§5". The R5 text is otherwise verbatim.
3. **R14:** folded into N-BH3, N-CC2/N-CC8 and N-DT1. The separate paragraph's §5.3 clause refers to removed content.
4. **Nit 8:** Weinberg is not cited until read.
5. **The Corollary (r4:94)** keeps a one-clause source for each direction rather than becoming a bare citation. The
   result is an "exactly when" statement, and §A.34 requires each direction to be identified.

## 7. AUDIT corrections for the coordinator

These are outside the r6 file set. They are still correct for the audit record, although the paper no longer uses
these items.
- **AUDIT §6.2 look-elsewhere:** "Six land within 1σ … about 2.5 are expected" → "5 distinct values of 752 within 1σ
  … about 3.5% …". The full text is in the review's R17.
- **AUDIT §0 Cabibbo row and §9 "Classification":** SM:851 → SM:849.
- **AUDIT §9:** split preface:7 ("The Bekenstein-Hawking factor of 1/4 in black-hole entropy becomes a derivation")
  from ch00:21 ("derivation rather than a postulate").
- **AUDIT §7.1:** replace "Undetermined" with the dating. The 4/3 ratio first appears in `77ac23ce` (2026-04-30),
  after the comparison in `054eb99a` (2026-04-04); Juno:237 shows the equivalence.

## 8. Owner items

- **H-decouple label.** Adopt it once #936 lands with DIFF-REVIEW R1's definition. r6 holds either way.
- **A.8 remedy** (full product space, or Haar-on-shell mean). r6 holds either way.
- **Reading list.** Padmanabhan is the likeliest referee comparison for §4.
- **The corpus queue.** These go to the separate consistency changes:
  - the past-hypothesis family, ch19:38 and the R19 CC sites;
  - the Main title. r6 cites it and never writes "equivalence of quantum mechanics".
- **Carried items.** The title (hyphenation; "from … to"), the §A.42 Lean retention, the R11 landing gates, and 9
  VERIFY markers.
