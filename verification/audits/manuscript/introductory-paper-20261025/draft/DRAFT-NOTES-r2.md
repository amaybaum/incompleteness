# Introduction draft, revision 2: notes

## Files and provenance

- **Draft:** `S/paper/draft/Introduction-r2.md`, sha256 `98d35eec5d4ecb48b63b24f7101444e695379c4b588cad5cabc4c4cd181274fe`.
  - Size: 5,823 source words, 5,418 PDF words.
  - Reviewed object: r1 `Introduction.md` (`03c1154b…4b25`), kept unchanged.
  - Changes: `CHANGES-r2.md` maps every review item to its edit or to the reason it was not adopted.
- **Design erratum:** `ERRATUM-r4.md` covers the card-table classical-memory clause in OUTLINE-r4, SOURCES-r4, CONTRIBUTION-r4 and RECHECK-r4.
- **Sources:** `main` `687e885b`, outline r4 (with the erratum), and the two reviews.
- **The Explainer:** no Explainer text is used, and the migration audit found nothing to absorb.
- **Repository:** no repository file was changed. Git ran with `-c gc.auto=0 -c maintenance.auto=false`.

## Build (fresh `git archive` of 687e885b, draft as papers/Introduction.md)

The build ran in `S/paper/draft/build2/`, using `sh ./build.sh Introduction` in the repository default format.

| Check | Result |
|---|---|
| Pages | **15** (r1: 20) |
| Dropped glyphs | none |
| Overfull boxes | **8**, from a separate `xelatex` run of the generated `.tex` in `S/paper/draft/ovf/`. Seven are in Appendix A (up to 78 pt) and come from unbreakable monospace Lean identifiers; one is 7.8 pt in the references. Removing them needs breakable identifiers, which means a header change (repository-wide) or splitting identifiers across lines. r1 had 28 |
| `tools/voice_check.py --root .` | OK (41 files) |
| `tools/claims_check.py --root .` | OK |
| Every list preceded by a blank line | checked by script |
| Every cited key has a reference entry, and the reverse | checked |
| Caps or register scan of visible prose | clean (acronyms only) |

The final page is full (325 words). There is little slack, so any addition of a paragraph or more needs a matching cut.

## OWNER markers in the draft

| # | Location | Decision |
|---|---|---|
| 1 | line 1 | **R1 title.** The working title is kept. Editorial alternatives: (1) "What an Embedded Observer Can Record: Stochastic, Reversible and Quantum Laws at Finite Horizon"; (2) "Observational Incompleteness: Memory, Recurrence and Indivisibility in Partially Observed Reversible Systems"; (3) "Hidden Memory and Finite Recurrence in Partially Observed Reversible Dynamics". The current title hyphenates on p. 1 (editorial F16) |
| 2 | after the abstract | **R11.** The abstract's black-hole sentence restates claim A and the H-scramble finding |
| 3 | §1.2 conventions | **Decision 2 and §A.42 retention.** The word: "machine-checked" or "checked in Lean 4/Mathlib at commit X by recipe Y" |
| 4 | §2.2 | **D2, the Calvo sentence.** Optional; not included |
| 5 | §4.3 | **D1, the CP-indivisibility versus quantum-memory sentence.** Optional; not included |
| 6 | §5.1 | **R11, claim A.** It meets ch07:110 / FULL:1987, ch18:146 / FULL:4966, ch18:158 / FULL:4978, ch07:159–161 / FULL:2036–2038 and ch18:130 / FULL:4950 |
| 7 | §5.2 | **R11, H-scramble.** It meets ch07:126 s1 / FULL:2003, GR:869, ch18:146 / FULL:4966 and ch19:334 / FULL:5510 |
| 8 | §5.3 | **R12, conditions level, non-blocking.** ch18:148 / FULL:4968, "mass-independent fraction" |
| 9 | §5.4 | **R11, decoupling.** It meets GR:811 |
| 10 | §6.5 item 4 | **R11.** A restatement |
| 11 | conclusion, second paragraph | **R11.** A restatement |
| 12 | "Code, data and formal verification" | **§A.42 retention**, with the placeholder "[expected-result file path]" |

The paper must not land until R11 is resolved for every marked site, either by correcting the live corpus sites or by dropping the marked paragraphs together with their restatements, and until the §A.42 expected result is retained.

## VERIFY markers (bibliography; 4, down from 17)

| Key | Reason |
|---|---|
| [BBS24] | Bibliographic data verified on Crossref by the science review. The content was not read: the definition is taken through Main:702 |
| [CT06] | Bibliographic data verified. The content was not read in the audits (AUDIT r4 P3.3) |
| [Har04] | Title and data verified. The content was not read; it is cited only as reported in [Mon08] |
| [Sha79] | From memory. Added for the editorial review's secret-sharing citation |

## Owner decisions raised by the reviews

| ID | Decision | Default in the draft |
|---|---|---|
| D1 (science) | Add "CP-indivisibility of this family therefore does not by itself witness quantum memory" to §4.3 | not added |
| D2 (science) | One scoped sentence on Calvo's claim to derive the textbook axioms, stronger than this equivalence (AUDIT r4 F14) | not added |
| D3 (science) | Read HKLP, Hardy04 and PSW before landing, or rest on read sources only | rests on read sources: §6.3 uses [GH03; Mon08], with Hardy only as reported; PSW and HKLP removed |
| Page format (editorial) | The default format now gives 15 pp. The alternative is 1 in / 11 pt, about 13 pp per the editorial measurement, which would make this the only paper with its own geometry | default format |
| Title (editorial) | See OWNER marker 1 | working title |
| Notation (editorial F8) | The Introduction writes $\mathsf S_K=\mathsf D_K=\mathsf Q_K$; Main writes $S\iff D\iff Q_{\mathrm{fb}}$. Either keep the difference (it is noted in Theorem 1) or align Main later | Introduction notation, noted |
| Main subtitle (editorial F14) | Main's subtitle, "The Equivalence of Quantum Mechanics and Embedded Observation", reads against this paper's "no derivation of quantum mechanics". This is the same exposure as F4 (open) | unchanged; flagged |
| Design-record erratum | ERRATUM-r4 as a note, or an r5 of the design files (science D5) | erratum note drafted |
| Earlier open decisions | Census registration (decision 4), the GR:226 check (decision 5) and provenance retention (decision 3) | unchanged |

## Conflicts between the reviews

Content follows the science review and presentation the editorial review. CHANGES-r2 gives the detail.

| Conflict | Resolution |
|---|---|
| C8 (compress the card-table quantum paragraph and drop the decomposition contrast) vs science RC-2 | Content kept, presentation compressed |
| C13 (delete §6.5) vs science RC-7 (complete it) | Kept as a compact six-item list |
| Editorial RC7 abstract with "(machine-checked)" vs science RC-6 (no Lean-check claim in the abstract before retention) | Parentheticals omitted |
| Editorial RC4 (remove the review mention) vs science M5 (state that the reviews are internal) | Removed from §5's opening; kept in non-claim 4 |
| Editorial RC12 "machine-checked" vs the coordinator's default wording | The convention defines the term as the default wording; marker 3 |

## Departures from outline r4

r1's departures stand: the six-part order, the card-table correction (now ERRATUM-r4), and the GR theorem citations. Revision 2 adds three more:

1. **Related work is gone as a section** (editorial C14). The attributions sit at their point of use.
2. **The per-horizon characterization paragraph is cut** (editorial C4). r4 §4-e said "one sentence, no display", and this is now zero sentences. Nothing proved, hypothesised or open is lost, because the memory corollary carries the content.
3. **The ε-gluing mention is cut** (editorial C12). r4 §6-f was "cited, not used", and no claim rested on it.
