# Introduction paper: draft notes

- **Draft:** `S/paper/draft/Introduction.md` (sha256 `03c1154b…4b25`; 6,772 source words, 6,342 words in the PDF).
- **Basis:** outline r4 (`OUTLINE-r4.md`, `CONTRIBUTION-r4.md`, `SOURCES-r4.md`), committed on #918 at `7c0a73ec`. Those committed copies are byte-identical to the local files used here.
- **Sources:** read at `main` `687e885b`.
- **Explainer:** no Explainer text is used.
- **Repository:** no file changed. Git ran with `-c gc.auto=0 -c maintenance.auto=false`.

## Defaults applied pending owner decisions

| Decision | Default in the draft | Marker |
|---|---|---|
| Title (R1) | "Observational Incompleteness: Quantum Representations of Partially Observed Deterministic Systems" | `<!-- OWNER: R1 title … -->`, line 1 |
| Scope (decision 1) | The recommended scope. §5.1's access paragraph (outline §7-c, claim A), the decoupling paragraph (§7-f, item F) and §5.2's H-scramble paragraph (§7-h) are drafted, each marked. The paper must not land until the owner corrects the R11 sites (ch07:110, :126 s1, :159–161, GR:811, :869 and their FULL mirrors) or drops these paragraphs | three `<!-- OWNER: R11 … -->` markers, in §5.1 (two) and §5.2 (one) |
| Lean-check wording (decision 2) | "checked in Lean 4/Mathlib at commit `687e885b…` by the recipe `python3 tools/lean_axiom_check.py --require-lake`", with the placeholder "[expected-result file path]" | `<!-- OWNER: retention §A.42 … -->`, in "Code, data and formal verification" |
| Appendix A scope (decision 6) | 16 rows, built from Main's status ledger (Main:710–722) and the claim register. This is one row more than the outline's "about 15", because §2.1's prior result and the CP-indivisibility row were added. It supersedes the Explainer's summary tables for its scope | none |
| Page format (decision 6) | Single column. See "Length" below | none |
| Census (decision 4) | The kernel identifiers are cited as in the outline. In the temporary tree, `tools/lean_manuscript_census.py` passed with `papers/Introduction.md` present: every cited identifier resolves. The §A.35 registration and anchors remain the owner's decision; the tool did not demand them | none |
| Provenance (decision 3) | Originality statements follow AUDIT r4. No class name appears in the paper. Attributions are given as citations to sources read in full | none |
| GR:226 box (decision 5) | Not displayed or cited. Theorem 4 is the carrier-general E2 without the OI conjunct | none |

## Length

The draft was built from a `git archive` of `687e885b` into `S/paper/draft/build/`, with the draft placed at `papers/Introduction.md`, by running `sh ./build.sh Introduction`.

- **Repository default format.** The build gives **20 pages**, at about 317 PDF words per page, with letter paper and the default LaTeX article margins. For calibration, Main and GR in the same build run at about 434 and 418 words per page; the draft is less dense because of its tables, displays and lists.
- **One-inch margins.** The same source built with `-V geometry:margin=1in`, otherwise identical and in the scratch directory only, gives **14 pages**. That is within 12–15.
- **Design estimate.** At the design's 550 words per page, 6,342 words is about 11.5 pages of text before tables and displays.

**Conclusion.** The draft meets 12–15 pages only if the page format of decision 6 is adopted, for example by one-inch margins. In the repository's default format it is 20 pages, and meeting 15 there would need a cut of about 2,000 words.

**Owner decision 6 is therefore live:** adopt the format, or cut. If cutting, the candidates are, in order:
1. §6.4 open problems, to about half;
2. §7 related work, to a list;
3. §2.4's characterization paragraph;
4. the Appendix A rows for prose-only results.

## Glyphs and checks (temporary tree)

- **Dropped glyphs.** The first build dropped one glyph, `⇏`, in the Appendix A table. It was replaced by `$\not\Rightarrow$`, and the rebuild reports `build: OK` with no dropped glyphs.
- **Voice.** `tools/voice_check.py --root .` returned OK (41 manuscript files scanned, the draft included).
- **Claims.** `tools/claims_check.py --root .` returned OK.
- **Other checks**, also OK: `tools/lean_manuscript_census.py`, `tools/dependency_label_check.py`, `tools/proof_census.py` and `tools/staleness_check.py`.
- **Caps scan.**
  - Mid-sentence runs of four or more capitals in visible prose are acronyms or citation keys only: CHSH, CPTP, HKLP.
  - FULL, AUDIT and ACCEPT occur only inside HTML comments. One visible "ACCEPT" in the bibliography was rewritten as "accepted".
- **Register scan.** No hits for the §A.32/§A.33 phrase families ("should not be read", "the reader", "honest", "no longer", "corrected form", "withdraw…").

## Every OWNER marker

1. Line 1: R1, the title.
2. §5.1, access paragraph: R11. It contradicts ch07:110 / FULL:1987, and the falsification framing at ch07:159–161 / FULL:2036–2038.
3. §5.1, decoupling paragraph: R11. It contradicts GR:811.
4. §5.2, H-scramble paragraph: R11. It contradicts ch07:126 sentence 1 / FULL:2003 and GR:869.
5. "Code, data and formal verification": retention under §A.42, with the expected-result placeholder.

## Every VERIFY marker (bibliography, 17)

Each entry is marked for one of the following reasons:
- its bibliographic data is from memory;
- it was taken from Main's or GR's bibliography without its content having been read in the audits;
- its authors' initials are not recorded in the literature study.

| Key | Reason |
|---|---|
| BB | Initials and venue from memory; arXiv id and title per the correspondence literature study |
| Bell64 | From memory |
| CHSH69 | From memory |
| CT | From memory; unread in the audits (AUDIT r4 P3.3) |
| EG | Initials not recorded |
| GH | Initials from memory |
| Hardy04 | Title and content unread (AUDIT C14) |
| Hawking76 | From Main [43]; unread |
| HKLP | From Main [55]; content unread (AUDIT C14) |
| Lean4 | From memory |
| LPW | Publisher and year from memory |
| Mathlib | From memory |
| Milz20 | Initials from memory |
| MO | Initial from memory |
| Pen19 | Title from memory |
| PSW | From GR [29]; unread |
| SGD | Initials from memory |

Entries not marked are recorded in full text by the two literature studies or by AUDIT r4 §8, or come from Main's bibliography with the full text read in AUDIT r4. These are B23, B25, B26, BD, BJA, BLP, DO, Page93, Page05, Page13, RHP10 and RHP14.

## Departures from outline r4

1. **Section order.**
   - The paper follows the owner's six-part structure: §1 central idea, §2 foundation, §3 interpretation, §4 examples, §5 black hole, §6 limitations. Related work is §7 and the conclusion §8.
   - The r4 claim IDs map as follows:

     | r4 | draft |
     |---|---|
     | §1, §2-a, §2-b | §1 |
     | §2-c to §4-f | §2 |
     | §5-a, §5-c to §5-g, §6-a | §3 |
     | §5-b, §5-f, §5-h | §4 |
     | §7 | §5 |
     | §6-b to §6-f, §8 | §6 |
     | §9 | §7 |
     | §10 | §8 |

   - The non-claims sit in §6.5 and §8, the paper's equivalents of r4's §8 and §10.
2. **§4.3, the card table: one clause of r4's scope sentence is corrected.**
   - r4 (from RECHECK-r3 RC-A) says "this swap realization admits no classical-memory decomposition (Main:702)". Main:702 states that for the swap with an **initialized** hidden slot, whose two-step maps are $\rho\mapsto|0\rangle\langle0|$ and $\rho\mapsto\rho$.
   - The card game of §4.3 uses a **uniform** burn card. For it, the one-step map is the completely depolarizing channel, which is the Pauli twirl $\sum_o \tfrac14\sigma_o\rho\sigma_o$. The identity decomposes through it as $\sum_o \sigma_o(\tfrac14\sigma_o\rho\sigma_o)\sigma_o=\rho$. That is a classical-memory decomposition in the sense of [Main §4.5]: an instrument realizing the first step, followed by channels conditioned on its outcome.
   - Checked numerically here: `S/paper/draft/probe/swap_memory.py`, with $\Phi_1=I/2$, $\Phi_2=\mathrm{id}$ and the decomposition reproducing $\rho$ for a random state. The initialized-slot case reproduces Main:702's maps.
   - The draft therefore keeps the parts of RC-A that hold: classical stochastic on card inputs; the population notion (2); the constant, entanglement-breaking one-step channel; the identity two-step map; CP-indivisibility (Main:326). It attributes "no classical-memory decomposition" only to the initialized-slot swap, and states that the uniform-burn realization decomposes.
   - **This also affects `OUTLINE-r4.md` §5-h, `CONTRIBUTION-r4.md` non-claim 13 and `SOURCES-r4.md` §5-h.** Those committed design files carry the uncorrected clause. They need a correction record (r5, or a note), which is for the coordinator and owner to decide.
3. **§7, related work: one attribution added.** The one-step $n^2$ ancilla dilation of [Main §3.1] is attributed to B26 Thm 3.3. AUDIT r4 C6 classes it KNOWN, but r4's outline does not list it. It is attribution only.
4. **Page-curve citations.** [GR App. A.8–A.9] is written as "[GR App. A.7, Theorems A.8–A.9]", because Theorems A.7–A.9 sit inside GR §A.7.
5. **Appendix A has 16 rows, not about 15.** See the table above.

## Not carried, as the outline requires

- Main's descriptions of Calvo, Pimenta and Doukas (F14–F16).
- The [11]/[12] swap (F17). The draft cites B23 and B25 by their arXiv titles.
- The Born-equilibrium sentence (F18).
- The ≤ n³ bound (F13).
- Main:532's "fixed autonomous generator" remark (F3).
- The ε-gluing results as "proved unconditionally" (F7). They are cited, not used, in §6.3.
- GR:226's box.
- C8-R (Alt-X only).
- The book's card-table sentences listed in r4 §5-h.
- Every item on the Explainer stale list.
