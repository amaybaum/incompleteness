# Editorial re-check: Introduction r6 (confirmation)

- **Object:** `verification/audits/manuscript/introductory-paper-20261025/draft/Introduction-r6.md` on #918 at `17aabc3b`.
  - sha256 `fc55c1e336c20bd0ac8c13a6f73eb1d93355db498bdc1c9df741ae0889df5183` (verified).
- **Read with it:** `CHANGES-r6.md`.
- **Method:** the r5→r6 diff, read hunk by hunk.
- **Read-only:** no repository file changed.
- **Build tree:** `S/paper/ed-review/tree6/`, a fresh `git archive` of `687e885b` with r6 in place.
- **Probes:** `S/paper/ed-review/r6/`.
- **Line numbers** refer to r6.

## Verdict: ACCEPT WITH NITS

- Every required change is applied. RC5 is settled by the science wording.
- Every recommended flow item is applied.
- Both departures are justified by their sources.
- The build is clean: 11.73 pp of main text, 0 overfull boxes, 0 missing glyphs.
- Dropping the six `***` rules is layout-only.
- Identifiers resolve, the bibliography is closed, and the changed lines are register-clean.
- Three nits remain, none blocking.

## 1. Required changes

| Item | r6 | Verdict |
|---|---|---|
| RC1 | l.28: "The paper develops one idea, OI: its foundation and quantum-emergence results (§§2–3), and two of its consequences, for the cosmological constant (§4) and for black-hole information (§5)." | ✔ verbatim |
| RC2 | abstract: "Each class contains the Markov laws, so representability does not distinguish a law with memory from one without, and the Born exponent is not selected." "Discriminating" has its antecedent again | ✔ verbatim |
| RC3 (i) | l.147 "(the mismatch)" | ✔ |
| RC3 (ii) | l.149 "OI's proposal is that the mismatch requires no cancellation, and its content lies in …" The proposal is now stated before its content and before l.151's "The proposal … is therefore conditional" | ✔ |
| RC3 (iii) | l.151: $\mathcal G_{\mu\nu}$ the Einstein tensor, $T^{\rm cl}_{\mu\nu}$, $\rho_C$ "the energy density of the offset". The offset is introduced at l.149 ("A uniform shift … the offset"). l.153: $E_{\mu\nu}[g,\mathrm{OI}]$, $\mathcal F[g,T]$, $T_{\mu\nu}$ as "the classical stress-energy of the substratum as source"; $H_{\rm Hub}$ the Hubble rate. No clash with the hidden $H$ | ✔ Every symbol is glossed at first use, and no claim is added |
| RC4 (i) | l.176: "$t_{\rm evap}$ the evaporation time and $\tau_B^D$ the $D$-sector timescale [GR App. A.5; …]" | ✔ (departure 1, §3 below) |
| RC4 (ii) | l.168 glosses accessible advantage at first use; the second gloss is removed from l.170 | ✔ This also clears the r5 appositive nit |
| RC4 (iii) | l.173 glosses H-scramble at first use; the separate defining sentence is removed | ✔ |
| RC5 / sci C2 | l.195: "What the paper states are the cited theorems and their scopes." | ✔ The contradiction with Contributions is gone. Science governs the content here, so this form is accepted over mine. A grammar nit is in §6 |

## 2. Recommended flow items

| Item | r6 | Verdict |
|---|---|---|
| Bridge into §4 | l.149: "In OI (§1.1) the zero-point sum of the emergent quantum description (§§2–3) and …" | ✔ |
| Bridge into §5 | l.163: "Because the dynamics of OI is a bijection observed through a partition (§1.1), two questions separate: …" | ✔ Both consequences now point back to the foundation |
| Calvo moved | to the end of §3.1 (l.114), after "Theorem 1 is a representation result …" | ✔ It fits there, as a second scope statement on Theorem 1 |
| 't Hooft deleted | [tH14] stays cited in §6.2 item 8 (l.195) | ✔ |
| l.102 connective | "With this lemma, on a fixed finite reversible substratum history readback forces …" | ✔ Comma nit in §6 |
| Bell split | l.142, after "must give up one of the two." | ✔ |
| Memory in the conclusion | l.205: "…; because the representation is universal, the discriminating content lies in memory, which every deterministic completion carries in its hidden state." | ✔ |
| F3 nit | l.86: "The written proof is in [Main §3.4, …]; see also [CT06]." | ✔ |
| Trims T | l.140 (Born exponent); §6.2 item 4 (l.191), which keeps the verification-layer clause and the three "No claim is made …" disclaimers. The removed Page-curve conditions are all stated in §5 (l.176, l.178) | ✔ No qualification is lost at its source |

## 3. Departures

1. **$\tau_B^D$ (RC4 i).** r6 uses GR's own definition, citing [GR App. A.5]. I checked GR:761 (Theorem A.5): "Let $\tau_B^D$ be the $D$-sector timescale and $\tau_B^B$ the $B$-sector timescale". The departure is correct: the source's wording governs, and my "[GR App. A.7]" pointer was the wrong subsection. **Accepted.** Nit: "the $D$-sector timescale" is still terse for an external reader. Since it is GR's own phrase, leave it.
2. **"No experiment yet".** r6 l.199 reads "no experiment distinguishing OI from standard quantum theory, and no memory-witness constraint, is established [Main §4.5]". This is time-neutral and stays at Main:704's strength. A bare deletion would have read as "none can", an overclaim. **Accepted;** it is better than my suggestion. The singular "is" after "no X …, and no Y" is acceptable usage.
3. **Memory as a clause in the conclusion.** Accepted.
4. **sci N1 not applied.** This is outside editorial scope; noted.

**Additional change, not requested by me: F1 reverted.** The r5 sentence "Exact operational quantum mechanics is reached only under conditions that OI alone does not imply (§3.2)." is removed from §1.2, as OUTLINE-r7 specifies.
- The qualification survives in the abstract, §3.2, §6.2 items 1–2 and §6.4, so no qualification is lost.
- §1.2 now says the correspondence is "exact and universal" (l.28) without that qualifier anywhere in §1. Nit 1 in §6 gives a one-clause fix.

## 4. Build and the dropped rules

Build: `sh ./build.sh Introduction` in tree6 reports `build: OK`.

| Measure | Value |
|---|---|
| Pages | **17** |
| Overfull boxes | **0** |
| Missing glyphs | **0** |
| Median characters per page | **2,575** |

- **Main text:** abstract to §6.4 ends on p. 12, line 33 of 45. By `measure.py` that is **11.73 pp**, which matches the drafter (r5: 11.89).
- **Back matter:** "Code, data and formal verification" starts on p. 12, Appendix A on p. 13, Appendix B on p. 14, the References on pp. 15–17.

**Rules removal is layout only.** I rebuilt r6 with the six `***` rules re-inserted before §§1–6 (`r6/r6rules.md`).
- The pandoc `.tex` files differ by exactly six `\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}` lines and their blank lines.
- The extracted texts differ only by extraction artifacts:
  - two page numbers caught inside words hyphenated across a page break;
  - one period displaced around a superscript by pdftotext.
- With the rules the main text is 12.07 pp; without them, 11.73 pp.
- The remaining rule, under the title block (l.8), is kept.
- **Confirmed: the change is layout only.**

**The two approved raw lines** (l.224 `\begingroup\small\raggedright`, l.358 `\endgroup`) are unchanged.

## 5. Identifiers, checks and register

- **`identcheck.py`** on r6:
  - 52 backticked tokens, 28 of them distinct Lean identifiers: **0 unresolved**;
  - 28 Appendix A identifier–module–line entries: **0 mismatches**.
- **`voice_check`, `claims_check`, `duplicate_check`:** all OK.
- **Bibliography:** 38 keys; none uncited; none undefined.
- **Markers:** 9 OWNER and 9 VERIFY, the same as r5.
- **§A.32/§A.33 scan** of the 21 changed lines (comments stripped):
  - **0 hits** for meta-commentary, reader instruction, self-assessment, history voice ("now", "yet", "no longer", …) or first person;
  - caps: CHSH only;
  - every changed sentence was also read in place. The new glosses and bridges are neutral and add no claim.

## 6. New problems, and nits

**Defined before use.** Nothing new.
- The new symbols are each glossed at first use.
- "Offset" (l.149) precedes $\rho_C$ (l.151).
- "The mismatch" is named at its source.
- H-scramble and accessible advantage are glossed at first use.
- One older ordering remains, carried from r4: "the Page value" (l.173) is used one sentence before "$S_{\rm Page}$ … Page's average" defines it. Optional.

**Nits (none blocking):**

1. **l.28, §1 without the operational qualifier.** Suggested, +10 words: "…its foundation and quantum-emergence results, which stop short of operational quantum mechanics (§§2–3), and two of its consequences…".
2. **l.102.** Add a comma after "substratum": "With this lemma, on a fixed finite reversible substratum, history readback forces …".
3. **l.195.** "What the paper states are the cited theorems and their scopes." This is acceptable. "What the paper states is …" or "The paper states the cited theorems and their scopes." reads more easily. This is science wording, so change it only if the science reviewer agrees.

## Owner items carried (unchanged)

- Weinberg landing gate.
- R11 markers (×6).
- Decision 2 / §A.42 retention.
- 9 VERIFY markers.
- Title hyphenation.
- The raw group covering Appendix B as well as Appendix A and the references.
