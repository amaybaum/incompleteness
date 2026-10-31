# Editorial re-check: Introduction r2

- **Object:** `S/paper/draft/Introduction-r2.md`, sha256 `98d35eec5d4ecb48b63b24f7101444e695379c4b588cad5cabc4c4cd181274fe`. This is byte-identical to `draft/build2/papers/Introduction.md`. The PDF text extracted from my rebuild matches the text extracted from build2's PDF.
- **Basis:** my review `ed-review/REVIEW.md` and the drafter's `CHANGES-r2.md`.
- **Read-only:** no repository file was changed. Probes are in `S/paper/ed-review/r2/`.
- Line numbers below refer to `Introduction-r2.md`.

## Verdict: ACCEPT WITH NITS

- **Applied correctly:** every required change (RC1–RC14) and every finding (F1–F15, F17).
- **Not applied, by design:** F16, the title hyphenation, because it waits on owner decision R1.
- **Register:** clean except one phrase, N1 below. N1 came in through the conflict resolution for §6.5 and should be reworded.
- **Typesetting:** 15 pages in the repository default format, with no dropped glyphs. The 8 remaining overfull boxes can be removed without a repository-wide header change (§4 below).
- **Landing gates:** unchanged and outside editorial scope. Five R11 markers, the §A.42 retention marker, 4 VERIFY entries and the OWNER D1/D2/R12 options remain; 12 OWNER markers in all.

## 1. Checks re-run

All checks ran in a fresh `git archive` of `687e885b`, with r2 placed at `papers/Introduction.md`.

- `voice_check`: OK, 41 files scanned, r2 included.
- `claims_check`: OK.
- `lean_manuscript_census`: OK, every cited identifier resolves.
- Lists: every list now has a blank line before it (scripted check). No list collapses into running text in the PDF (checked with pdftotext and page images).
- Rebuild with the repository recipe: 15 pages, 0 missing characters, 8 overfull boxes.
  - Seven are in Appendix A, at 5.2, 8.1, 77.7, 44.9, 43.1, 22.1 and 28.2 pt.
  - One is in [Bar23], at 7.8 pt.
- My own §A.32/§A.33 grep of r2 found:
  - **Meta-commentary, reader instruction, "honest", "discipline", "kept apart":** the only hit is the verbatim Main remark title "(three notions, kept apart)" at line 122, which is legitimate.
  - **History phrases** ("now", "no longer", "corrected", "reversed", "after the plan", "package"): no hits in prose. Line 72's "packaged as one iterated bijection" is mathematical usage.
  - **ALL-CAPS words:** only CADE, CHSH, SIGPLAN and DRAFT PRE-PRINT, all legitimate.
  - **First person:** one "We", at line 24.
  - **Process narration:** one hit, N1.

## 2. Item-by-item

| Item | Status | Note |
|---|---|---|
| RC1 / F1 lists | ✔ | Short fragment lists are now prose |
| RC2 / F2 App. A as a list | ✔ | No overprinting (PDF p. 13). Residual overfull lines: see §4 |
| RC3 / F3a comb sentence | ✔ | Dropped altogether, the right fallback |
| RC4 / F3b review sentence | ✔ in §5 | The phrase reappears in §6.5 item 4 (N1) |
| RC5 / F3c "package", Shamir | ✔ | [Sha79] added, VERIFY |
| RC6 / F3d–e decoupling | ✔ | Declarative, in §5.4 (line 208). No reference to GR's former ground and no "reversed" |
| RC7 / F6 abstract | ✔ | See conflict K1 |
| RC8 Corollary | ✔ | Line 96. [Main §1.5] is the right citation: Main:99 states the vanishing criterion there |
| RC9 | ✔ | Line 124 |
| RC10 Theorem 4 as a sentence | ✔ | Line 220. Direction witnesses are at line 222 (§A.34) |
| RC11 card table | ✔ | Probability, protocol rows, a separate Markov row, "street" defined |
| RC12 conventions | ✔ | Line 36. "Kernel" is gone from the body; $\pi_V$ and $J$ are defined |
| RC13 leads and pointer to Main | ✔ | §2 (44), §3 (106), §4 (130), §1.2 (32) |
| RC14 | ✔ | — |
| F7 terms | ✔ mostly | Residual: N3 |
| F8 notation | ✔ | $\mathsf S_K=\mathsf D_K=\mathsf Q_K$; $\mathcal U$, $\mathcal M$; Hadamard; product form. Owner item: the notation now differs from Main's (noted in DRAFT-NOTES-r2) |
| F9 openings | ✔ | — |
| F10 Theorem 4 placement and citation | ✔ | §6.1 is titled "Operational completion". The GR:228 witness question is resolved correctly: `main_result` belongs to the OI-conjunct box, which is not cited |
| F11 Main remark titles | ✔ | Verbatim. GR citations are uniform "[GR, Thm A.n]" |
| F13 contributions | ✔ | See owner note O1 |
| F14 pointer to Main | ✔ | Main's subtitle risk is noted in DRAFT-NOTES-r2 |
| F15 overfull lines | ✔ | 28 reduced to 8; §4 below gives the route to 0 |
| F16 title hyphenation | open | Owner decision R1 |
| F17 bibliography | ✔ | One journal pattern, first page only, arXiv versions throughout, author-year keys, clean BH entries. Nits in N6 |
| Cuts C1–C7, C9–C12, C14–C17 | ✔ | — |
| Nit list | ✔ except one | The β sentence (line 199) is still verbless, although CHANGES says it was applied (N2) |

## 3. Conflict resolutions

- **K1. Abstract without "(machine-checked)" (science RC-6 against editorial RC7).** Acceptable.
  - A Lean-check claim in the abstract should wait for the §A.42 retention.
  - The abstract still separates proved, open and hypothesis ("one step proved on paper only"; "Open are…"; "the hypothesis").
  - Once retention lands, the owner may restore the tags.
- **K2. Machine-checked defined as the owner's wording, with an OWNER marker (line 36–38).** Acceptable. It is one definition in one place, so the owner's choice of wording propagates automatically.
- **K3. C8 not taken: the card-table decomposition is kept, compressed (science RC-2).** Acceptable.
  - Content is the science reviewer's call, and the compression into prose at lines 164–166 reads cleanly.
  - The cost is about 120 words, and the paper still fits in 15 pages.
- **K4. C13 not taken: §6.5 kept as a compact six-item list (science RC-7).** Acceptable as structure: a scope list is admissible under §A.30, and it costs about half a page. One clause in item 4 is not acceptable as worded (N1).

## 4. Removing the remaining overfull boxes without a repository-wide header change

The question was whether Appendix A's identifiers can be made to break or fit, for example with `\allowbreak`, `\seqsplit` or a smaller font.

**Diagnosis.** No single identifier is wider than the line inside the list. The longest, `pIndivisible_of_rooted_identity_return_of_overlap`, is about 270 pt, against about 320 pt of line. The overflow comes from justified text: TeX prefers an overfull line to a very loose one that would put the identifier on its own line.

**Fix.** Break the lines; do not split the identifiers.

**Variants tested** (`ed-review/r2/v-*.md`). Each wraps raw LaTeX group lines around the Appendix A list, and the variants marked "→ end" extend the group through the References:

| Opening line | Pages | Overfull |
|---|---|---|
| `\begingroup\sloppy` | 15 | 2 |
| `\begingroup\small\sloppy` | 15 | 2 |
| `\begingroup\setlength{\emergencystretch}{3em}` | 15 | 8 |
| `\begingroup\footnotesize` | 15 | 5 |
| `\begingroup\raggedright` | 16 | 1 |
| `\begingroup\raggedright` → end | 16 | 0 |
| **`\begingroup\small\raggedright` → end** | **15** | **0** |

**Recommended edit.**

- Insert one line before the first Appendix A bullet (line 275):

  ```
  \begingroup\small\raggedright
  ```

  followed by a blank line.
- Append, as the last line of the file after the references:

  ```
  \endgroup
  ```

**Measured result:**

- 15 pages and 0 overfull boxes;
- `lean_manuscript_census` and `voice_check` still pass, because the identifiers stay in backticks;
- the body text is untouched.

A ragged right margin in an appendix and bibliography is conventional.

**Trade-offs (owner):**

- On GitHub's Markdown view the two raw lines show as literal text. The precedent is that the book's FULL.md already carries raw `\newpage` / `\clearpage` lines.
- `\seqsplit` and `\allowbreak` inside identifiers are worse options:
  - `\seqsplit` needs a package, which means a header change or YAML front matter;
  - raw `\texttt{…\allowbreak…}` takes the identifiers out of backticks. That would hide them from `lean_manuscript_census`, which resolves cited identifiers, and it splits Lean names mid-token.

  Neither is recommended.

## 5. Nits (none blocking)

**N1. Line 247, §6.5 item 4: "…finite toy models whose reviews are internal, not external validation."**

- This is the process / self-assessment phrase that RC4 removed from §5. Moving it into a non-claims list does not change its register (§A.32 self-assessment; §A.27 manuscript voice).
- Every preprint is unreviewed, so the clause tells an external reader nothing about the result except the process behind it.
- **Suggested wording** (science content kept: scope and verification layer, not process): "…and the black-hole results are finite toy-model computations, verified by exhaustive enumeration and exact algebra at small size."
- Coordinator to arbitrate with the science reviewer if RC-7 insists on the review clause.

**N2. Line 199.** "In the quasi-stationary semiclassical regime $\beta>1$ [Pag05, Eqs. (5)–(10)]." is still a sentence without a verb. Replace with: "$\beta>1$ in the quasi-stationary semiclassical regime [Pag05, Eqs. (5)–(10)]."

**N3. Terms still undefined for an external reader:**

- **"rooted form" (114), "root-conditioned", "rooted families" (230).** "Rooted" is no longer defined, since r2's line 110 dropped the word. Restore it in 110: "the *rooted* visible transition matrix from time 0 to time $t$ (rows indexed by $x_0$)".
- **"routed-readback form of (C4)" (116).** Use "Steps (2)–(3) are machine-checked; step (1) is proved on paper."
- **$d$ in "$(d+1)$-dimensional ancilla" (122).** Add "($d$ the system dimension)".
- **$S_{\mathrm{Page}}(d_B,d_R)$ (194).** Add "the Page value for subsystem dimensions $d_B,d_R$".
- **Line 32 uses $\Gamma_s^{-1}\Gamma_t$ before $\Gamma$ is defined (§3.1).** Use "(the candidate intermediate matrix, where it exists, has negative entries)".
- **"coherent lift", "fixed-basis datum", "lift with trivial ancilla" (228–230).** §6.2's second paragraph is the hardest one in the paper. It is the science text, verbatim, so the content stays. As presentation, a one-clause gloss of "coherent lift" would help, as would moving its three `(identifier, File.lean:line)` parentheticals to Appendix A, where line 280 already lists them. That would also make the identifier format uniform: Module:line, not File.lean:line.

**N4. Small wording points:**

- **Line 26.** "Bijectivity is the reversible representative of the hidden dynamics" is a category slip. Write "The bijection $\varphi$ is the reversible representative…".
- **Line 14.** "Exact finite operational quantum mechanics is characterized exactly by…" uses "exact" twice. Drop the second, "characterized by five completion conditions", or write "Finite operational quantum mechanics is characterized exactly by…".
- **Line 64.** The notation remark "[Main] writes this $S\iff D\iff Q_{\mathrm{fb}}$." sits inside the italic theorem statement. Move it to the following sentence, in roman.
- **Line 185.** "These conditions are sufficient, not necessary" follows a bound and is ambiguous. Use "The recovery conditions above are sufficient, not necessary."
- **Line 114.** The proof sketch runs backwards (conclusion first, then "a non-permutation matrix has overlapping rows, and finite order gives $\Gamma_N=I$"). Reorder: finite order gives $\Gamma_N=I$; a non-permutation one-step matrix has overlapping rows; the distance drops below 1 at $s$ and returns to 1 at $N$, which no stochastic divisor permits.
- **Line 24.** "We" is the paper's only first-person use. Either is fine; "Embedded observation is modelled by a triple" keeps the voice uniform.

**N5. Line 269.** "Probes and the black-hole computations … are in the repository" no longer says where.

- Give the two directory names: `papers/oi_lattice_code/foundations/` and `verification/programmes/black-hole-information/`.
- With the §4 ragged-right group extended to cover this section, or with a line break before each path, they set without overfull lines.
- The [BHa]/[BHb] entries say "black-hole-information programme, `bh01_access_v1/`". "Programme" is house vocabulary. Write instead "repository directory `verification/programmes/black-hole-information/bh01_access_v1/`".

**N6. Bibliography:**

- Several keys carry a year that the entry does not print, because those entries are arXiv-only: [Bar23], [Bar26], [BB18], [Dou26], [EGGH26], [Sch21]. Add the year to each entry. [BB18] is also arXiv 2012, with the book in 2018, so either cite the book or key it [BB12].
- Two keys break the scheme: [Bell64] (others use 3 letters, so [Bel64]) and [Milz20]. The latter is acceptable as is.
- Four VERIFY markers remain: BBS24, CT06, Har04 and Sha79.

**N7. F16.** The title still hyphenates "Repre-sentations" on p. 1. This is pending R1; all three alternative titles in REVIEW.md avoid it.

## Owner notes

- **O1.** The Contributions paragraph (line 34) now presents every component as known or as a form of a standard inequality. The only contribution it claims is packaging and machine-checking.
  - The paper is positioned as "a technical perspective with original mathematical components".
  - The owner may want the paragraph to name what is original, if anything: for example the access separations of §5.1, Theorem 4 (proved in GR), or the hidden-memory theorem in this form.
  - That is a content decision for the owner and the science reviewer; editorially the paragraph is clear and correctly registered.
- **O2.** The notation $\mathsf S_K=\mathsf D_K=\mathsf Q_K$ differs from Main's $S\iff D\iff Q_{\mathrm{fb}}$. Line 64 bridges the two. Propagating it to Main is optional.
