# Confirmation of Introduction r11 → r12 (read-only, diff only)

- **Object:** branch `draft/oi-introductory-paper-20261025` at `b763e6d6`. It contains the r12 commit `11e58899`,
  then a merge of `main` `c967d6a9`.
- **Files read:** `draft/Introduction-r12.md` (sha256 `87d63d9f…843b`), `draft/CHANGES-r12.md` and
  `draft/scripts/build_r12.py`. The base is r11 (sha256 `a25e973c…f1d7`, matching CHANGES-r12).

## Verdict: ACCEPT WITH NITS

All ten findings (B1, B2, N1–N8) are applied as specified, and the P1 trim removes only repeated content. The build
meets the budget.

One non-blocking wording nit (W1) remains in the B1 sentence, plus an optional nit (W2). Neither blocks landing. The
Weinberg landing gate (line 140) stays open, as the owner recorded.

***

## Merge and reproduction

- **The merge only adds files.** `git diff --name-status c967d6a9 b763e6d6` lists only additions: 151 files under
  `verification/audits/manuscript/` and the two files under `papers/introduction_repro/`. No file on `main` is modified.
  The merge did not touch the introduction folder (`git diff 11e58899 b763e6d6` is empty there).
- **r12 reproduces byte for byte.** `python3 -I build_r12.py Introduction-r11.md out.md` reports
  `applied 12 edits: B1; B2; N1; N2 cite; N2 bib; N3; N4; N5; N6; N7; N8; P1 (repetition)`. `cmp` against
  `Introduction-r12.md` shows the files are identical.
- **The diff contains only the twelve edits.** The `git diff --no-index --word-diff` from r11 to r12 shows exactly those
  replacements and nothing else.

## B1 — Theorem 4's setup against `FiniteOperationalTheory` (OperationalAssembly.lean:594)

| Field | r12 clause | Check |
| --- | --- | --- |
| `avail`, `availExt` | "which finite outcome families … are available on the system and at every ancilla level" | ✓ |
| `avail_id` (system level, `Unit`) | "contains the identity" | ✓ |
| `avail_coarse`, `availExt_coarse` | "closed under coarse-graining of outcomes" (system and every level) | ✓ |
| `availExt_bind` (stated on `availExt n` only) | "at every ancilla level, under outcome-conditioned composition" | ✓ The scoping is correct: the structure has no system-level bind rule. |
| `prepAvail`, `prepAvail_uniform` (`uniformAttach (n+1)`) | "an available preparation of a uniformly mixed ancilla" | ✓ |
| `prepAvail_post` (a one-outcome composite map post-composed onto an available preparation gives an available preparation) | "which an available operation may follow" | ✓ |
| `readout`, `readout_avail`, `readout_local` | "an available spectator-independent local readout of the ancilla" | ✓ The form is derived by `readout_is_localLuders`, so "local" is not an added postulate. |
| `prepAvail_discard` (preparation, then an available instrument `F : O → …`, then discard, gives `avail O …`) | "an available preparation followed by an available instrument, with the ancilla then discarded, is an available operation on the system" | ✓ in content; see W1 |

Every field is covered, and no clause adds a requirement the structure lacks. The B1 counterexample (channels only) is now
excluded by the readout clause. Theorem 4's statement and its §A.34 witnesses are unchanged (⇒ `physical_of_exactAll`,
⇐ `exactAll_of_physical_general`).

**W1 (non-blocking).** "is an available *operation* on the system" can be read as dropping the outcome label. The kernel
keeps it: `prepAvail_discard` yields `avail O (…)`, the same outcome family. That version is the one the sufficiency
direction uses, through `avail_of_availExt_one` in `avail_iff_availExt_one` (LevelOneSeam:128).

- **Why it does not block:** the paper elsewhere uses "operation" for outcome families. Conditions (ii) and (v) are both
  family-level in the kernel and are worded with "operation".
- **Minimal fix:** "is an available *instrument* on the system, with the same outcomes".

## B2 — Corpus pin

- **The pin is moved.** Line 260 reads "**Corpus** (repository commit `c967d6a9`, …)".
- **The Lean pins stay at `17b830bc`** (lines 30, 196, 205). That is correct: `git diff --stat 17b830bc c967d6a9` is
  empty for `verification/lean`, `verification/lean-mathlib`, `tools`, `papers/Main.md`,
  `verification/programmes/black-hole-information`, `papers/oi_lattice_code`, `.gitattributes` and
  `book/ch01-observation.md`. Appendix A's line numbers and `papers/introduction_repro/` therefore hold at both commits.
- **No cited pointer moved.**
  - GR's section headings are identical at the two commits.
  - Book ch07, ch18 and ch01 headings are identical.
  - At `c967d6a9`, GR §6.2 still has the $CI$ invariance, the $\rho_C g_{\mu\nu}$ pair and G3 open.
  - GR §3.3, §2.2 and App. A.1–A.9 are textually unchanged (App. A shifts by two lines; the paper cites sections, not
    lines).
  - Book §7.6 and §18.5 still describe the Page curve as conditional and the islands correspondence as conjectural.
  - [Main], [BHa] and [BHb] are byte-identical.
- **Main.md's own `17b830bc` mention in the paper:** none remains outside the Lean pins.

**W2 (optional).** The paper now names two commits and does not say why. One clause on line 196 would remove the
puzzle: "(the Lean tree, `tools/` and `papers/Main.md` are identical at the corpus commit `c967d6a9`)". This is not
required.

## N1–N8

| # | Line | r12 | Verdict |
| --- | --- | --- | --- |
| N1 | 84 | "(machine-checked in the same form as Theorem 2)" | ✓ This is the wording the review suggested; it imports line 80's scope. |
| N2 | 130, 312 | "…; HKLP24, Thm 4]" and a new [HKLP24] entry | ✓ See below. |
| N3 | 198–201 | Probes "also in the release archive, concept DOI …"; black-hole computations "not part of the release archive" | ✓ See below. |
| N4 | 12 | "which of conditions (iii)–(v)" | ✓ Matches lines 120, 174 and 184. |
| N5 | 92 | "a bijection of $\mathcal C_V\times\mathcal C_H$ with a fixed hidden prior" | ✓ Matches `RootedRealization` (CausalReadback.lean:178). |
| N6 | 176 | "the results of §5 reported from [BHa; BHb] concern finite toy models" | ✓ |
| N7 | 86 | "coincides with $M_t>0$ by the vanishing criterion [CT06], and the Corollary places it in the hidden state" | ✓ The witness is correct. CT06 keeps its VERIFY marker, as recorded by the owner. |
| N8 | 254 | The comment is deleted. | ✓ The remaining HTML comments are the owner's VERIFY gates and the "Read first-hand" provenance notes. |

**N2, checked first-hand.**

- **Source.** I fetched arXiv:2308.07727v4. Its sha256 is `194e52275874fd67d8b683101d577b6a0e575031ac612c89d3f977092f7b6868`,
  the same as CHANGES-r12's `194e5227…6868`.
- **Theorem 4, p. 4:** "For all integers d, m ≥ 2 there is a communication matrix C such that dimQ(C) ≤ d while
  dimC(C) ≥ m."
- **The terms match the paper's sentence.**
  - The proof takes d = 2, a qubit, using Lemma 3's dimC(Aₙ) = rank₊(Aₙ) ≥ m.
  - dimC is defined on p. 3 as "the smallest integer d such that C can be obtained using classical system with d
    distinct states". It is also shown there to equal the nonnegative rank.
- **This is exactly the import the sentence names.** For every N there is a finite qubit prepare-and-measure task that
  no N-state classical model reproduces. It is the result Main:538 imports as its ref. [55]. The bibliographic data
  (PRA 109, 032627 (2024)) agree with Main's reference list.
- **The citation supports the sentence.** No VERIFY marker is needed.

**N3.** `.gitattributes` at `c967d6a9` is identical to `17b830bc`. It reads:

```
verification/programmes export-ignore
verification/audits export-ignore
verification/infrastructure/round-* export-ignore
```

Its header comment says "Release archives (the GitHub zipball Zenodo deposits) omit…". `papers/` is not excluded, so
both of r12's statements are correct. The root `LICENSE` at `c967d6a9` is MIT. "At these repository paths at the corpus
commit" resolves correctly: both paths exist at `c967d6a9` and are identical to `17b830bc`.

## P1 — the §6.1 trim

**Deleted:** "Two long-standing problems would then change form: vacuum energy becomes a question about how two levels
of description couple to geometry, and black-hole information separates into conservation and accessible recovery."

**It is only repetition.** Every half of it is stated elsewhere, at equal or greater strength and with the conditions
attached:

- §4, line 143: "its content lies in how the two levels couple to geometry";
- §5, line 157: "two questions separate: whether information is conserved … and whether it can be recovered";
- §6.4, line 192: both halves restated with their conditions;
- the abstract: both halves again.

The deleted sentence carried no limitation, hypothesis or qualification of evidence. §6.1 still ends on the H-Bell
condition, and §6.2 is unchanged.

## Build (independent rebuild)

I built r12 in scratch with `pandoc 3.1.3 -s --include-in-header=tools/unicode-fix.tex` (unicode-fix taken from
`c967d6a9`), then ran `xelatex` twice.

- **17 pages.**
- **Overfull boxes: 0.** There are 2 underfull boxes; they are harmless.
- **Missing characters: 0.**
- **Main text ends on p. 12, line 43** ("Neither application is a demonstrated resolution of its problem."). "Code, data
  and formal verification" starts at the top of p. 13. The main text is therefore ≤ 12 pp, consistent with CHANGES-r12's
  11.90 pp.
- **Page fill:** characters per page are 2,000–3,400, with no near-empty pages and no table collapse.

## Summary

| Item | Result |
| --- | --- |
| B1 | ✓ All fields mapped and composition scoped correctly; W1 is a wording nit |
| B2 | ✓ Pin moved, no pointer moved, Lean pins correctly retained; W2 optional |
| N1–N8 | ✓ |
| N2 citation | ✓ Verified first-hand |
| N3 archive statement | ✓ |
| P1 | ✓ Repetition only |
| Reproduction | ✓ Byte-identical |
| Build | ✓ 0 overfull, 0 missing glyphs, main text ≤ 12 pp |

**Verdict: ACCEPT WITH NITS.** W1 is a one-word fix and W2 is optional; neither blocks. The Weinberg gate remains the
owner's.
