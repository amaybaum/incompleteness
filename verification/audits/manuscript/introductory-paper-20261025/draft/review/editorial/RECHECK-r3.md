# Editorial re-check: Introduction r3

- **Object:** `verification/audits/manuscript/introductory-paper-20261025/draft/Introduction-r3.md` on #918 at `270728cb`.
  - sha256 `83313e2cb86dd094505f66ace99db0d2e8ad3849b40145e5eb932b2b1f3a6a68`.
  - Byte-identical to `S/paper/draft/Introduction-r3.md`.
- **Basis:** `CHANGES-r3.md` at the same commit, my `RECHECK-r2.md`, and the owner decisions of 2026-10-26.
- **Read-only.** No repository file was changed. Probes are in `S/paper/ed-review/r3/` and `S/paper/ed-review/tree3/`; the latter is a fresh `git archive` of `687e885b` with r3 at `papers/Introduction.md`.
- **Line numbers** refer to r3.

## Verdict: ACCEPT WITH NITS

- Every nit from my r2 re-check is applied, or its departure is justified in CHANGES-r3.
- The two raw lines change layout only.
- The register of the new text is clean, apart from two optional wording nits (N-a, N-b).
- The build is 15 pages with 0 overfull boxes and 0 missing glyphs.
- Every backticked Lean identifier resolves, and every Appendix A line number matches.
- Two items are left to the owner:
  1. Title hyphenation. No fix needs neither a raw line nor a page, and the drafter's tested fix adds an 11 pt overfull title line (§5).
  2. A possible tension between "no new … result" and §5's sources (O-1).
- Landing gates outside editorial scope are unchanged: the R11 markers, R12, the §A.42 retention marker and 5 VERIFY entries (9 OWNER markers in all).

## 1. Build

`sh ./build.sh Introduction` in a fresh `git archive` of `687e885b` gives `build: OK` and 15 pages. Measurements:

| Measure | Value |
|---|---|
| Pages | 15 |
| Overfull hboxes | 0 |
| Missing characters | 0 |
| Median characters per page (pdftotext) | 2,505 (the drafter reports 2,504) |
| Median words per page | 415 |

Words per page, pp. 1–15: 353 458 402 438 461 394 441 466 415 409 418 362 222 309 346.

- **Layout:** §1–§7 and the Code section end on p. 12, Appendix A is on p. 13 and the References on pp. 14–15. The main narrative is 12 pages, inside the owner's 12–15.
- **Visual check of p. 13:** the appendix sets cleanly in `\small` ragged-right, with no overprinting.

## 2. The two raw lines change layout only

- **TeX output.** Running pandoc with and without lines 272 (`\begingroup\small\raggedright`) and 359 (`\endgroup`), the two `.tex` files differ by exactly those two lines plus their blank separators. Nothing else in the generated LaTeX changes.
- **Rendered text.** The same holds for the extracted text once whitespace, hyphens and bare page-number lines are removed:

  | Build | Pages | Normalized text |
  |---|---|---|
  | With the lines | 15 | 34,176 characters |
  | Without them | 16 | 34,176 characters |

  `cmp` shows the two texts are identical (`r3/w2.txt`, `r3/wo2.txt`).
- An earlier normalization that kept intra-word hyphens showed four one-character differences. Each was a compound ("Running-Vacuum", "Page-time", "non-Markovian", "quant-ph") broken at a line end in one build and not the other. That is layout, not content.
- **Conclusion:** the lines affect font size, ragging and grouping only. This meets the owner's condition.

## 3. Nits of RECHECK-r2

| r2 nit | r3 | Verdict |
|---|---|---|
| N1 internal-review clause | 241: "the results of §5 are finite toy-model computations, checked exhaustively at small size and by exact arithmetic" | ✔ register clean. "Exact arithmetic" covers both the exact algebra and the interval arithmetic of §5 |
| N2 verbless β sentence | 195: "In the quasi-stationary semiclassical regime, $\beta$ exceeds 1 [Pag05 …]" | ✔ |
| N3 "rooted" | 108 defines it (rows indexed by $x_0$) | ✔ |
| N3 "routed readback" | 114 glosses it | ✔ The drafter's departure from my suggested wording is correct and important (see below) |
| N3 $d$ | 120 | ✔ |
| N3 $S_{\mathrm{Page}}$ | 190, with [Pag93] | ✔ |
| N3 Γ before definition | 30: "the candidate intermediate matrix" | ✔ |
| N3 coherent lift | 224 glosses it | ✔ |
| N3 `File.lean:line` in §6.2 | Moved to Appendix A; identifiers stay beside the claims | ✔ |
| N4 "The bijection $\varphi$" | 24 | ✔ |
| N4 single "exactly" | 12 | ✔ |
| N4 notation remark outside the italic theorem | 64 | ✔ |
| N4 "endpoint guarantees" | 181 | ✔ |
| N4 forward-order proof sketch | 112, which also fixes the $\Gamma_N$/$\Gamma_L$ mismatch | ✔ |
| N4 impersonal voice | 22; no "we" remains | ✔ |
| N5 repository paths | 263–266, a two-item list that sets without overfull lines; [BHa]/[BHb] without "programme" | ✔ |
| N6 bibliography | Years printed for arXiv-only entries; [BB12]; [Bel64] | ✔ |
| N7 title hyphenation | Owner item | §5 below |
| §4 raw group | 272, 359 | ✔ §2 above |

**Accepted departures in CHANGES-r3:**

- **Sci-N2 / line 114.** My r2 suggestion, "Steps (2)–(3) are machine-checked; step (1) is proved on paper", is the wording the drafter set aside, and correctly so. It would assert a history-level-(C4) → routed-readback step that has no proof. The converse fails on a kernel carrier (round C4-1, RD1/RD3). r3's wording keeps the two routes apart: "machine-checked … from a routed-readback form of (C4) …; from history-level (C4) it is proved on paper". Appendix A line 278 matches it.
- **Sci-N5.** "steps … that lack one" (234) avoids mislabelling the time-$t$ identification, which after R2-4 is "not machine-checked" rather than "proved on paper".

## 4. Register (§A.32 / §A.33) of the text new in r3

**Method.** I diffed r2 and r3 with comments stripped, giving 56 added lines, and grepped them.

**Meta-commentary, reader instruction, honesty or discipline.** No hits. The matches were:

- "(three notions, kept apart)", which is Main's verbatim remark title;
- "explicit tasks" (230), which is mathematical usage;
- Contributions (32), discussed under N-a.

**History voice.** No hits for "now", "no longer", "corrected", "reversed", "superseded", "formerly" or "revised". The other matches were:

- "Access audit" in the [BHa] title. This is the cited document's own title; see N-c.
- "SIGPLAN", matching "plan". A false positive.

**Caps.** CADE, CHSH and SIGPLAN, all acronyms.

**New sentences, read individually:**

- **Calvo (72).** It places another work's stronger claim and states what Theorem 1 does not derive. Neutral.
- **§6.3 premise order (230).** "the factorization is proved, and the unboundedness is imported". This is a status statement and is fine.
- **Bell item (234).** "the framework keeps measurement independence and adopts ontic parameter dependence". This is a status statement of an adopted branch with its open hypothesis, so it is admissible. "the lattice" is undefined in this paper (N-b).
- **Decoupling scope (204).** Declarative, with no reference to a former ground.

**Contributions (32).** The paragraph reads: "The paper claims no new theorem or physical result; its contribution is expository. This paper brings together a unified presentation …, an explicit separation …, a concise account …, and a synthesis …".

- It follows owner decision 2 and is admissible as a scope statement.
- "Unified", "explicit" and "concise" are favourable self-description of the paper. They are not of the framework, so they fall outside §A.32's letter. They add nothing and are easily removed (N-a).

## 5. Title hyphenation

The setting on p. 1 is "From Determinis- / tic Dynamics". Variants tested, with the same header and recipe (`r3/t-*.md`):

| Variant | Raw LaTeX | Pages | Overfull | Missing glyphs | Result |
|---|---|---|---|---|---|
| No-break space at four positions (between "From" and "Deterministic", after the colon, inside "Observational Incompleteness", between "Deterministic" and "Dynamics") | none | 15 | 0 | 0 | still "Determinis-tic" |
| U+2060 word joiner or U+200C inside the word | none | 15 | 0 | 1 / 0 | new hyphenation points ("Deter-", "Determin-"); one variant drops a glyph |
| **Pandoc title block** (`% Observational Incompleteness: From Deterministic Dynamics to Quantum Observations` replacing the `#` line) | **none** | **16** | 0 | 0 | No hyphen: a centred `\maketitle` reading "Observational Incompleteness: From / Deterministic Dynamics to Quantum / Observations" |
| `\hyphenation{Deterministic}` as a third raw line (the drafter's fix) | 1 line | 15 | **1 (11.1 pt, the title line)** | 0 | "…From Deterministic / Dynamics…". The title line overruns the margin |
| inline `\mbox{Deterministic}` in the heading | inline | 15 | **1 (11.1 pt)** | 0 | Same as the `\hyphenation` line, and the heading shows TeX on GitHub |

**Conclusion.** No raw-free fix keeps both the corpus convention and the page count.

- The only raw-free fix is the pandoc title block (`%` line).
  - It is markdown metadata, not raw LaTeX.
  - It costs one page (16 pp).
  - Every one of the 13 sibling papers starts with a `#` heading, so it departs from that convention.
  - No tool in `tools/` depends on the `#` title line (checked by grep).
  - GitHub shows the `%` line as plain text.
- Correction to CHANGES-r3: the drafter's `\hyphenation{Deterministic}` fix is **not clean**. It removes the hyphen but leaves an 11.1 pt overfull title line, because "Observational Incompleteness: From Deterministic" at 14.4 pt bold is wider than the text block. A forced break before "From" or after it would need further raw LaTeX.

**Owner item.** Choose one of:

- (a) accept the hyphen;
- (b) the `%` title block, which needs no raw LaTeX but adds a page and departs from the sibling papers;
- (c) a third raw line, accepting an 11 pt margin overrun.

My editorial preference is (a) or (b). (c) trades a hyphen for a visible overrun.

## 6. The census, and a correction to my r2 record

The drafter reports that `tools/lean_manuscript_census.py` resolves only identifiers inside `(kernel: …)` parentheticals. **This is confirmed.**

- **Code.** Lines 84–86 extract identifiers only from `re.finditer(r'kernel:([^)]*)\)', s)`. Only `OIBridge/….lean` paths (`PATH`) are checked file-wide. r3 contains no `kernel:` parenthetical, so for this paper the check is vacuous.
- **Countercontrol.** I renamed `` `pIndivisible_of_rooted_identity_return_of_overlap` `` to `…_overlapX` in r3. The census still printed `OK`, exit 0.
- **Positive control.** I appended `(kernel: `bogus_identifier_zz`)`. The census printed `IDENT … declared nowhere in OIBridge` and `FAILED (1 problem(s))`. So the tool works as designed; its scope just does not cover backticked identifiers outside that form.

**Correction to my record.**

- `RECHECK-r2.md` §1 reports "`lean_manuscript_census`: OK, every cited identifier resolves". That reproduced the tool's own output string. For this paper it is **unsupported**: the tool resolved no identifier of the Introduction.
- `REVIEW.md` made no census claim of its own, but it did not challenge DRAFT-NOTES' census note either.
- The direct check below replaces both.

**Direct check.** `scripts/identcheck.py` runs against `tree3/verification/lean-mathlib/OIBridge/*.lean` at `687e885b`.

- **Resolution.** r3 (comments stripped) has 51 backticked tokens; 28 distinct of them are Lean identifiers, after excluding `propext`, `Classical.choice`, `Quot.sound` and the paths. Every one of the 28 is declared in OIBridge (theorem/lemma/def/…), with **0 unresolved**. The drafter reports 30; the difference is only in what is counted.
- **Line numbers.** I checked all 28 identifier–module–line triples in Appendix A against the line where each declaration begins, with **0 mismatches**. Theorem 1's "compositions :466–468" are the three anonymous-constructor lines inside `finite_horizon_equivalence`, Equivalence.lean:466–468. They are correctly cited as lines, not declarations.
- **Placeholders.** The cited modules contain no `sorry` or `axiom` declaration. The two grep hits are comment headers. The axiom audit itself remains the job of `lean_axiom_check.py` and the §A.42 retention.

## 7. Nits (none blocking)

- **N-a (32), Contributions.** Drop the self-descriptive adjectives and the repetition of "The paper … This paper". Suggested: "The paper claims no new theorem or physical result; its contribution is expository. It presents the established mathematical results of OI together, separates the mathematical correspondence from its physical interpretation, states their implications and limitations, and summarizes the black-hole information discussion within the scope stated in §5."
- **N-b (234).** "the gravitational continuum limit of the lattice". "Lattice" is undefined here. The drafter flagged it for the science reviewer; "of the substratum" fits the conventions paragraph.
- **N-c (293).** The [BHa] title "Access audit: …" carries house vocabulary in a cited title. It is the document's own title, so retitling the source is the owner's call. Alternatively cite it by its descriptive part only: "Recovery from accessible records in finite reversible models".
- **N-d (257–259).** The page break falls between "by the recipe" (p. 12) and the code block (p. 13). This is cosmetic. Rewording the line to "by the recipe `python3 tools/lean_axiom_check.py --require-lake`, which builds …" (inline code, no block) would avoid it, and pandoc may then set the path without an overfull line. Not tested; optional.

## Owner notes

- **O-1 [SCI].** Contributions says the paper "claims no new theorem or physical result". §5.1, §5.2 (C6(c)) and §5.4 (item F), however, state results whose only cited source is the repository computations [BHa]/[BHb], not a companion paper. If those count as results, the sentence and §5 are in tension. Either:
  - state the source status, for example "the results of §5 are taken from the repository computations [BHa; BHb]"; or
  - narrow the claim, for example "no new theorem; the toy computations of §5 are reported from [BHa; BHb]".

  This is for the owner and the science reviewer.
- **O-2.** Title hyphenation, §5 above.
- **O-3.** The census vacuity is a property of the tool, not of this paper. If the Introduction is to be covered by the release-gate census, either the tool must also resolve backticked identifiers (a tool change) or the paper must carry `(kernel: …)` parentheticals (a format change). Until then the direct check of §6 is the evidence; it should be re-run at landing.
