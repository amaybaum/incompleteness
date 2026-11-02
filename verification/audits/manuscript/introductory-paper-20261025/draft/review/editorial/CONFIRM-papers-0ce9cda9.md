## Confirmation of #918 r18 (`0ce9cda9`): one must-fix remains

**Verdict: CONFIRM, after one remaining must-fix.** The `[Sti55]` reference entry renders wrongly. Everything else you asked me to check holds.

I worked read-only: no edits, commits, pushes or comments. My worktree has been removed.

### Must-fix: the [Sti55] entry is mis-typeset (`papers/Introduction.md` L367)
- **Source:** `"Positive functions on C*-algebras," *Proc. Amer. Math. Soc.*`
- **Problem:** the unescaped `*` in "C\*" opens an italic span. The rendered entry reads `Positive functions on C-algebras," Proc. Amer. Math. Soc.*`: the asterisk is lost from the title, part of the title is italicised, and a stray `*` follows "Soc.".
- **History:** the defect has been there since r16, and I missed it in my earlier citation passes.
- **Fix:** write `C\*-algebras`, or `$C^*$-algebras`.

### 1. M1–M5 and S1–S8: all resolved
- **M1:** `[SM] A. Maybaum, "The Standard Model from a Cubic Lattice," papers/SM.md` is in the Corpus list. Its title matches the first line of SM.md.
- **M2:** the abstract now says "places the zero-point sum and the effective cosmological constant at different levels of description".
- **M3:** L97 now uses M_k and defines π_H, so I\* keeps one meaning.
- **M4:** the sentence now reads "needs only finite reversibility and one non-deterministic visible step … does not separate them from memory-bearing laws at accessible orders". The scope is correct.
- **M5:** "of equal length" is added.
- **Should-fixes:**
  - S1: "accessible" is defined at its first use in L97.
  - S2: the Bell clause is restructured, and "preparation-indexed" is glossed.
  - S3: the access sentence now scopes the reading schedule to the first count, and the 32-map count states its configuration.
  - S4: "the Hubble time" is added.
  - S5: the de Sitter identity has moved to §4's opening, with [GR §6.3].
  - S6: §3.1 is split into three paragraphs.
  - S7: see the departures below.
  - S8: the Attribution sentence is fixed.
- **Other r18 edits, checked:**
  - The H-decouple sentence is stated within its scope, with [GR App. A.7].
  - The §6 regrouping is consistent with §2.5: "proved on paper, with Theorem 3 as machine-checked core".
- **Departures, both sound:**
  - S7: defining "root" in place keeps the explicit zero-probability rows.
  - O2: not changing the coverage ID is the right call.

### 2. Build
- **Result:** `sh ./build.sh Introduction` is OK. The `.tex` is identical to the committed one.
- **Length:** 15 pages; the main text ends on p12. Page 15 holds only about 6 lines, so any further addition makes 16 pages.
- **Line length:** a median of 99 characters per line, against 111 at r17's 10 pt.
- **Boxes and glyphs:** 0 overfull boxes and 0 missing characters. There are 7 underfull lines, all in the `\sloppy` code note.
  - Optional: `\begingroup\raggedright` instead of `\sloppy` gave 0 underfull lines and the same 15 pages in my scratch test. It also matches Appendix A's group.
- **Rendered pages (80 dpi):**
  - p1: the abstract and §1 start fit on the page.
  - p6: the Γ matrices display fully, and the card table is aligned.
  - p10: both field-equation displays are inside the margins.
  - p12: the code note is legible, with no overflow, though its sloppy spacing is visibly loose.
  - pp13–15: the hanging indents work, and the entries are now clearly separated. [Sti55] is the only rendering defect.

### 3. Voice and citations
- **Voice:** the r18 added lines contain no §A.32/§A.33 phrases, no caps emphasis and no HTML comments.
- **Citations:** 52 entries; every key resolves and there are no orphans.

### 4. Readability (owner's condition)
11 pt reads better than r17's 10 pt. At 10 pt the 6.5-inch measure carried about 111 characters per line, too long for comfortable reading. 11 pt brings it to about 99, with larger glyphs and no layout defects. That is still longer than the classic 66–80 range, but it is normal for a single-column preprint with one-inch margins.

I consider the readability condition met.
