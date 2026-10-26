# Introduction draft, revision 3: changes

**Applies:**
- the scientific re-check `S/paper/sci-review/RECHECK-r2.md`;
- the editorial re-check `S/paper/ed-review/RECHECK-r2.md`;
- the owner's decisions of 2026-10-26.

Both re-checks concern r2 (`98d35eec…74fe`), which is kept unchanged. The output is `Introduction-r3.md`.

**Rule for conflicts:** science governs content, editorial governs presentation, and the owner's decisions govern both. Line numbers refer to r3.

## Scientific re-check

| Item | Status | r3 line |
|---|---|---|
| R2-1 Bell branch adopted, not necessary | Applied verbatim; `[Bell64]` is rekeyed `[Bel64]` (ed N6) | 234 (6.4 item 5) |
| R2-2 §6.3 premise order | Applied verbatim; both paragraphs replaced | 230 |
| R2-3 decoupling scope limit | Applied verbatim | 204 |
| R2-4 status words | Applied verbatim at both sites | 92, 275 |
| N1 abstract parenthetical | Applied: "(each with one step not machine-checked)" | 12 |
| N2 kernel route of the readback theorem | **Applied with a deviation.** The suggested "the step from history-level (C4) to that form is proved on paper" asserts that history-level (C4) implies routed readback. No proof of that exists. Round C4-1 (`result.md` RD1, RD3) records that routed readback implies the history-level condition and that the converse fails on a kernel carrier. r3 instead says: "The conclusion is machine-checked, by the route of Theorem 3, from a routed-readback form of (C4), [gloss] [Main §1.3]; from history-level (C4) it is proved on paper." Appendix A is aligned | 114, 278 |
| N3 nonempty carrier | Applied | 218 |
| N4 "the correspondence of §2 (Theorem 1)" | Applied | 30 |
| N5 §6.4(1) includes §2.2 | **Applied with a deviation:** "machine checks of the steps of §2.2, §2.4 and §3.1 that lack one". After R2-4, the time-$t$ identification in §2.4 is not machine-checked, but it is not "proved on paper" either. The suggested wording would mislabel it | 234 |
| N6 §6.5 item-4 marker | Applied: "§5.4's decoupling sentence" dropped | 241 |
| N7 [Sha79] | Content-VERIFY kept and made specific (Crossref data confirmed; content from memory) | 357 |
| E1–E4 erratum | Applied in `ERRATUM-r4.md` (E1 SOURCES quote and separate replacement; E2 citations restored; E3 range reason; E4 Pauli-twirl identity carries the claim, probe is provenance) | — |

## Editorial re-check

| Item | Status | r3 line |
|---|---|---|
| N1 review clause in §6.5 item 4 | Applied: "the results of §5 are finite toy-model computations, checked exhaustively at small size and by exact arithmetic". "Exact arithmetic" covers both the exact algebra and the exact interval arithmetic of §5. The R11 marker is kept | 241 |
| N2 β sentence | Applied: "In the quasi-stationary semiclassical regime, $\beta$ exceeds 1 [Pag05 …]" | 195 |
| N3 undefined terms | Applied as follows. "Rooted" is defined at 108 (rows indexed by $x_0$). Routed readback is glossed at 114. $d$ is "a $d$-dimensional system" (120). $S_{\mathrm{Page}}$ is glossed with [Pag93] (190). The candidate in §1.2 is "the candidate intermediate matrix" (30). "Coherent lift" is glossed from Main:624 (224). The `File.lean:line` parentheticals of §6.2 are moved to Appendix A, which already lists them; the identifiers and "forward direction" stay beside the claims (§A.34) | as listed |
| N4 wording | All applied: "The bijection $\varphi$ is…" (24); single "exactly" in the abstract (12); the notation remark moved out of the italic theorem (64); "The endpoint guarantees above are sufficient, not necessary" (181, BH-01 REPORT:24); "Embedded observation is modelled…" (22). The proof sketch at 112 is put in forward order and uses $\Gamma_L$ in place of the inconsistent $\Gamma_N$; it does not overlap sci N2 (114) | as listed |
| N5 repository paths | Applied. Both paths exist at `687e885b`, and they are given as a two-item list so they set without overfull lines (265–266). [BHa]/[BHb] drop "programme" and name their subdirectory "in the black-hole computations' directory" | 265, 293–295 |
| N6 bibliography | Applied: years printed on all arXiv-only entries; [BB18] rekeyed [BB12], because the cited object is arXiv:1209.3632v5 (first version 2012); [Bell64] rekeyed [Bel64]; [Milz20] kept. All four VERIFY markers kept. [dMU21] and [Mathlib20] venues are abbreviated for length | 297–357 |
| N7 / F16 title hyphenation | See owner item 1 | 1 |
| §4 overfull fix | Owner-approved (item 3) | 272, 359 |

## Owner decisions (2026-10-26)

| Item | Status | r3 line |
|---|---|---|
| 1 Title | Applied; the OWNER marker is removed. **Open:** p. 1 still sets "Determinis-tic", and a no-break space does not stop it. A third raw line, `\hyphenation{Deterministic}` before the title, gives "…From Deterministic / Dynamics to Quantum Observations" at 15 pp (tested). It is not applied, because it is a raw LaTeX line outside the approval | 1 |
| 2 Contributions (O1) | Applied: "claims no new theorem or physical result; its contribution is expository. This paper brings together…" with the four items and the component attributions. "Within its reviewed scope" is rendered as "within the scope stated in §5" (§A.32: no review-process reference in paper prose). "Machine-checked theorem" becomes "one theorem" | 32 |
| 3 Raw group | Applied. With and without the two lines, the pdftotext output is identical after whitespace, hyphens and page numbers are removed (32,470 characters each). Overfull: 0. Pages: 15 with the group, 16 without | 272, 359 |
| 4 Length | 15 pp in all. §1–§7 fill pp. 1–12, and pp. 13–15 are the code note, Appendix A and the references. Kernel identifiers stay in Appendix A. No qualification was cut; the length trims are wording only (listed below) | — |
| 5 D1 | Resolved: no sentence added. §4.3 states CP-indivisibility per RC-2 / Main:326; the D1 marker is removed | 162 |
| 5 D2 | Resolved: one sentence states Calvo's claim from the arXiv v2 abstract, read first-hand through the arXiv API, with [Cal26] and a content-VERIFY (body not read) | 72, 317 |
| 5 D3 | Already met by R2-2: [GH03; Mon08], with [Har04] as reported (VERIFY kept) | 230 |
| 6 R11/R12 | No book or GR text edited. All R11 markers and the R12 marker are kept | 14, 178, 187, 194, 203, 241, 251 |

## Length trims (wording only; no claim or qualification removed)

- "Proofs, the status ledger…" (30).
- "defines three classes … where a law's memory must sit" (42).
- "a clock and a complete trajectory record" (66).
- "A finite bijection has finite order" (80).
- One-sentence Corollary directions (94).
- "the divisibility criterion of [RHP14]"; "rooted visible transition matrix" (108).
- "discarding it" (214).
- "P-indivisibility" in §6.5 item 3 (240).
- "the card game (§4.3)" (243).
- Shorter Appendix A entries (278, 281).

## Checks

- **Build:** 15 pp, 0 overfull boxes, 0 missing characters, median 2,504 characters per page.
- **`voice_check`, `claims_check`, `duplicate_check` and `lean_manuscript_census`:** OK on a fresh `git archive` of `687e885b`.
- **Census coverage:** the census resolves only `(kernel: …)` parentheticals, and the Introduction has none, so its OK is vacuous for this paper. A countercontrol with a misspelled identifier still passed. All 30 backticked identifiers were therefore resolved directly against OIBridge, and every Appendix A line number was matched: 0 unresolved, 0 mismatches.
- **§A.32/§A.33 scan of added lines:** clean. The one hit is the verbatim Main remark title "(three notions, kept apart)".

## Open review findings

- **Title hyphenation** (owner item 1, above).
- **"The lattice" in R2-1.** The phrase is verbatim from R2-1 but is not defined in this paper. The science reviewer could replace it with "the substratum".
- **VERIFY markers.** Five remain: BBS24, Cal26, CT06, Har04 and Sha79.
- **Retention §A.42 / decision 2.** The OWNER markers stay at 36 and 256.
