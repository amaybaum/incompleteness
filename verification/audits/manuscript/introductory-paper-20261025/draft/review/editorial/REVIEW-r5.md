# Editorial review: Introduction r5 (rescoped rewrite)

- **Object.** `verification/audits/manuscript/introductory-paper-20261025/draft/Introduction-r5.md` on #918 at `423e83da`, sha256 `c538d9e165489cd9c09a56f473c90e153ef3c30dff861b3e773049d2531a5c24` (verified).
- **Read with it.** `CHANGES-r5.md`, `design/OUTLINE-r7.md` and the owner direction: one idea with two consequences, six sections, 10–12 pp, derivations cited rather than re-derived, the owner's title, and two raw lines used for layout only.
- **Read-only.** No repository file was changed.
- **Build tree.** `S/paper/ed-review/tree5/` is a fresh `git archive` of `687e885b` with r5 at `papers/Introduction.md`.
- **Probes.** `S/paper/ed-review/r5/`.
- **Line numbers** below refer to r5.

## Verdict: ACCEPT WITH CHANGES

The rescoping works. The paper now reads as idea (§1), foundation (§2), what the foundation does and does not give for quantum mechanics (§3), consequence 1 (§4), consequence 2 (§5), and discussion (§6). Every application carries its non-resolution caution. The build is clean, the identifiers resolve, and the bibliography is closed.

Five required changes are needed before the next round:

- **RC1.** One sentence that misstates the paper's own "two consequences".
- **RC2.** An abstract sentence whose antecedent was cut.
- **RC3–RC4.** Notation in §4 and §5 used without definition, now that the proof sketches are gone.
- **RC5.** A non-claims sentence that contradicts Contributions.

All five are small. Their net cost (about +60 words) can be absorbed by the trims in §1.

## 1. Build and length

`sh ./build.sh Introduction` reports `build: OK`.

| Measure | Value |
|---|---|
| Pages | **17** |
| Overfull boxes | **0** (3 underfull) |
| Missing glyphs | **0** |
| Median characters per page | **2,602** (pp. 1–12: 2,663) |

**Layout.**
- Abstract through §6.4: pp. 1–12.
- Code section and Appendix A: p. 13.
- Appendix B: pp. 14–15.
- References: pp. 15–17.

**Main-text length.** I counted rendered lines (`r5/measure.py`). The main text ends at line 39 of 44 on p. 12, which is **11.9 pp**. The drafter's figure is 12.0. Either way it sits inside the owner's 10–12, at the top edge. Page 12 has no room left for the Code heading, so the back matter starts on p. 13.

**Can it come under 12 pp without cutting a qualification?** Yes, but only by tenths of a page. The variants were measured by the same line count (`r5/v-*.md`); all have 0 overfull boxes.

| Variant | Main text | Change |
|---|---|---|
| r5 | 11.89 pp | — |
| **L1.** Drop the six `***` rules inside the main text | 11.77 pp | Layout only, no wording. It departs from the house rule style |
| **T.** Two restatement trims (below) | 11.77 pp | Wording; no qualification removed at its source |
| **M1.** Outline fallback: move the fixed-basis-datum paragraph (line 142) to Appendix A | 11.76 pp | Moves text |
| **M1 + T** | 11.73 pp | — |
| **All (L1 + T + M1)** | **11.57 pp** | — |

The two trims in T:
- **Line 150.** Write "The origin of the quadratic Born exponent, which the correspondence does not select (§2.3), is open [Main §3.4; Bar26, Thm 3.1]." The current sentence re-states line 80, which the outline says is "not repeated".
- **§6.2 item 4 (line 207).** Replace the recap of §5 with "the Page curve of [GR App. A] is not established (§5)". Keep its last sentence, "No claim is made that information reaches $D$, …". That sentence is stated only here, so it must stay.

A further ≈30 words come from deleting line 74 ('t Hooft). §6.2 item 8 already makes that citation (see N2).

**About M1 and §A.34.** Line 142 states two directions separately, each with its witness (`bridge_traj`; `rooted_eq_iff_slice_eq`, forward direction). It displays no equivalence, so moving it with its witnesses is §A.34-safe. The sentence left in §3.3, "the correspondence acts on the quotient by visible equality", implicitly asserts well-definedness and separation. If M1 is taken, write that sentence with its witnesses beside it: "…acts on the quotient by visible equality (well defined by `bridge_traj`; classes separated by the forward direction of `rooted_eq_iff_slice_eq`; Appendix A)". Keep "A selection condition … none is supplied here" in §3.3, because it is a qualification.

**Recommendation.** M1 is not needed, since 11.9 pp is within the target. Apply RC1–RC5, which add about 60 words. Offset them with T and the line-74 deletion, about −100 words. That should land near 11.7–11.8 pp, with no layout change.

## 2. The two raw lines

- `\begingroup\small\raggedright` is at line 240 and `\endgroup` at line 374.
- Pandoc's `.tex` with and without them differs by exactly those two lines.
- The extracted text is identical up to pdftotext's reading order of two matrices (Γ₁ and $\tfrac12J$ at different sizes).
- Without the lines: 17 pp and 8 overfull boxes. With them: 0 overfull boxes. They are layout only. ✔
- **Scope note for the owner.** The group now also covers Appendix B's prose, displays and card table, not only Appendix A and the references. Appendix B is therefore set small and ragged-right. That is still layout only, but it extends what the two lines were approved for.

## 3. Flow (one argument, two consequences)

**What works:**
- §1.2 announces the structure.
- §2 opens with a lead that says derivations are cited.
- §3 separates what is demonstrated from what is open.
- §4 and §5 each end on their condition.
- §6 gathers implications, non-claims and the tests that would decide each part.

The cautions are explicit in the abstract, §1.2, §4, §5, §6.2 and §6.4, as the owner required.

**Required:**

- **RC1, line 30 (N-INT1).** The sentence "The paper develops one idea, OI, and two of its consequences: the foundation and its quantum-emergence results (§§2–3), and two applications, the cosmological constant (§4) and black-hole information (§5)." makes the foundation one of the two consequences and the applications the other. Everywhere else the two consequences are the cosmological constant and black-hole information: the abstract, the §1.2 heading, Contributions ("states two consequences with their conditions and limitations"), §6.1 ("Two long-standing problems") and §6.4. Replace with:

  > The paper develops one idea, OI: its foundation and quantum-emergence results (§§2–3), and two of its consequences, for the cosmological constant (§4) and for black-hole information (§5).

- **RC2, line 12 (abstract).**
  - "The Born exponent is not selected." now stands alone. The next sentence, "The discriminating content concerns memory", has lost its antecedent. The reader is not told what fails to discriminate.
  - This is the universality qualification of Theorem 1, stated in §2.3 and in §6.2 item 1. Without it the abstract reads as though Theorem 1 itself had content about memory.
  - Restore it in one sentence (+18 words):

    > Each class contains the Markov laws, so representability does not distinguish a law with memory from one without, and the Born exponent is not selected.

**Recommended:**

- **Bridges into §4 and §5.** Neither section points back to the foundation. One clause each would make the "consequence" relation visible:
  - §4, line 161: "In OI (§1.1) the zero-point sum of the emergent quantum description (§§2–3) and …".
  - §5, line 177: "Under OI two questions separate" → "Because the dynamics of OI is a bijection observed through a partition (§1.1), two questions separate".
- **Literature in the middle of the foundation.**
  - The Calvo sentence (line 72) and the 't Hooft sentence (line 74) sit inside "§2.2 The finite-horizon correspondence" as unconnected one-sentence paragraphs. They read as a catalogue.
  - Calvo's sentence carries a scope statement ("derives no such axioms"), so keep it, but move it to the end of §1.2 or to §3.1.
  - Delete line 74; §6.2 item 8 already cites [tH14].
- **Line 110.** The stochastic-inverse lemma no longer has a visible role now that steps (1)–(3) are gone. One connective, without proof content, fixes this: "With this lemma, history readback forces indivisibility …".
- **Conclusion (lines 221–224).** It no longer mentions memory, the paper's discriminating content: the abstract's "the discriminating content concerns memory" and §2.4–§2.5. The r4 sentence that was dropped "for length" is the right one to restore if the trims above make room. Otherwise §6.1's sentence covers it adequately.
- **Line 152.** The Bell sentence runs to about 110 words in one sentence. Split it after "must give up one of the two;".

## 4. Register (§A.32 / §A.33)

**Method.** I scanned the 127 lines added relative to r4 (comments stripped) by grep, and read every new sentence F1–F10 and the outline's N-* text in place.

**Grep results:**
- **Meta-commentary, reader-instruction or discipline phrases.** None. The only hits are:
  - Main's remark title "(three notions, kept apart)";
  - "familiar" at line 161 ("the familiar statement that no non-gravitational measurement sees the absolute vacuum energy"), which is acceptable;
  - "long-standing problems" at line 200, which is acceptable.
- **History voice.** Two items:
  - "Until then" (171) is conditional on a future derivation, not revision history. Acceptable.
  - "no experiment **yet** distinguishes" (215) is time-relative. Drop "yet" (nit).
- **Caps.** CHSH only.
- **First person.** None.

**The flagged sentences F1–F10:**

| Flag | Sentence | Verdict |
|---|---|---|
| F1 | line 30 | Register clean; logic wrong (RC1) |
| F2 | line 42 | Clean |
| F3 | line 94, "The written proof is [Main §3.4, …; CT06]." | Clean, but a citation used as a predicate reads oddly. Write "The written proof is in [Main §3.4, Theorem (unavoidable hidden predictive memory)]; see also [CT06]." (nit) |
| F4 | line 150 | Clean; near-repeat of line 80 (trim T) |
| F5 | line 179 | Clean |
| F6 | line 184 | Clean; see N4 for the appositive |
| F7 | line 200 | Clean. "with measurement independence kept" correctly keeps the adopted branch conditional |
| F8 | line 217 | Clean |
| F9 | line 224 | Clean; at the strength of §4/§5 |
| F10 | line 288 | Clean. The source comment is invisible in the PDF |

**RC5, line 211 (§6.2 item 8).** "The paper's results are the theorems and their scopes" contradicts Contributions, line 32: "The paper claims no new theorem or physical result". Replace with:

> The paper's content is the cited theorems and their scopes.

## 5. Definitions (proof sketches removed)

The foundation sections hold up: rooted Γ_t, P-divisible, faithful realization, substratum, routed readback, readout-relevant memory, coherent lift and $J$ are all defined at or before first use. The gaps are in the two new application sections.

**Required:**

- **RC3, §4.**
  - **"The proposal" before the proposal is stated.** Line 161 says "the proposal's content lies in how the two levels couple to geometry", but the proposal itself is first stated at line 163 ("The proposal that the mismatch requires no cancellation"). Fix at 161: "…; OI's proposal is that the mismatch requires no cancellation, and its content lies in how the two levels couple to geometry." Line 163's "The proposal … is therefore conditional" then follows naturally.
  - **Undefined symbols:**
    - $\mathcal G_{\mu\nu}$, $T^{\rm cl}_{\mu\nu}$, $\rho_C$ (163);
    - $E_{\mu\nu}[g,\mathrm{OI}]$, $\mathcal F[g,T]$ (165);
    - $H$ in $\rho\sim H^2/G$ (165). This also clashes with the hidden-sector $H$/$H_t$ of §2.

    One clause each is enough, e.g. "with $\mathcal G_{\mu\nu}$ the Einstein tensor, $T^{\rm cl}_{\mu\nu}$ the classical stress-energy and $\rho_C$ the zero-point density" and "$H$ the Hubble rate".
  - **"Mismatch".** Name it at its source, line 159: "…above the observed one (the mismatch), …".
- **RC4, §5.**
  - **Timescales.** $\tau_B^D$ and $t_{\rm evap}$ (190) are undefined. $\tau_B^D$ has never been defined in any revision. Use: "with $t_{\rm evap}$ the evaporation time and $\tau_B^D$ the time scale of the $B$–$D$ coupling [GR App. A.7]".
  - **"Accessible advantage"** is used at line 182 and defined at line 184. Move the gloss to 182.
  - **"H-scramble"** is used at line 187 before the next sentence defines it. Swap the two sentences, or gloss it in place.

**Nits:**
- "cosmological partition" (215): one clause or "[GR §2.2]" suffices.
- "dependency ladder of [GR]" (190, 215).
- "remnant-capacity form" (184, carried from r4).
- "spatial coupling graph" (152).
- "Level G3 of [GR]" (163) is a pointer label. Acceptable.

## 6. Identifiers

`identcheck.py` on r5 (tree5):
- 52 backticked tokens, 28 of them distinct Lean identifiers: **0 unresolved**.
- 28 Appendix A identifier–module–line entries: **0 mismatches**.
- Equivalence:466–468 are the three composition lines.
- The census is still vacuous for this paper (RECHECK-r3 §6). This direct check is the evidence, and it should be re-run at landing.
- `voice_check`, `claims_check` and `duplicate_check` all report OK.

## 7. Bibliography

- **Keys.** 38 keys are defined: 5 corpus and 33 external. Every defined key is cited in the body, and every cited key is defined. There are no duplicates.
- **[Pag05].** Removed with β, and no longer cited. ✔
- **Order.** Alphabetical by key, with Page's entries in chronological order. ✔
- **Format.** The four new entries ([EvEMU11], [KP14], [tH14], [Vol06]) follow the house pattern.
- **VERIFY markers.** 9 remain, invisible in the PDF: BBS24, Cal26, CT06, Har04, Sha79, tH14, EvEMU11, KP14 and Vol06.
- **[BHa].** Still the unquoted lower-case description (RECHECK-r4 §4 nit).

## 8. Other nits

- **Section headings.** They are long, with colon subtitles, and wrap to two lines. They are the outline's and owner's wording. "Observational Incompleteness" is capitalized in the §1 heading but lower case in the text.
- **Line 184.** "1,376 give zero accessible advantage, the gain in success probability over a blind guess, for a binary message…" reads as though "zero" were the gain. This is moot if RC4 moves the gloss.
- **Line 165.** "The scale $\rho\sim H^2/G$ is the Friedmann normalization…" comes without motivation for an external reader. Anchor it as "[GR]'s scale $\rho\sim H^2/G$".
- **§3 heading versus §3.1.** §3.1 is titled "What is demonstrated" but opens with a limitation ("is global … not on every window"). Acceptable as scope; a one-line lead for §3 would help.
- **Title hyphenation** ("Determinis-tic", p. 1). Still an owner item; see RECHECK-r3 §5.

## Owner items carried

1. The Weinberg landing gate (line 158).
2. R11: abstract, §5 (×3), §6.2 item 4 and §6.4.
3. Decision 2 / §A.42 retention (×2).
4. The 9 VERIFY markers.
5. Title hyphenation.
6. The raw group's extended scope (§2).
