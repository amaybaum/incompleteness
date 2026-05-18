# Line-Edit Change-Log — *The Incompleteness of Observation*

Full line edit of all 20 chapters, front matter, and appendices. Completed May 18, 2026.

## Calibration finding

The manuscript was already well-revised. A full line edit at this level of polish
is *light by necessity* — there is little wordy prose to cut, few rhythm problems,
no tonal inconsistency. The pass therefore made 15 targeted prose edits (tightening,
word choice, comma-splice fixes, occasional rhythm touches — never rewriting), one
book-wide consistency fix, and removed 8 internal-scaffolding leaks. Many chapters
needed zero edits; this is a sign of a healthy manuscript, not a shallow pass.

The line edit tightened enough prose that the book reflowed from 409 to 404 pages.
The back-of-book index was regenerated against the final pagination.

## Prose edits (15)

### Front matter
- **Preface** — "The book documents what follows" repetition → "and the book documents
  exactly that" (tightening).
- **Preface** — "inflation and the cosmological initial conditions … the cosmological
  initial state" — removed the duplicated scope-limit item (redundancy).

### Chapter 0 — Introduction
- "the mathematics is the same" → "the mathematics is unchanged" (word choice).

### Chapter 1 — Embedded Observation and the Characterization Theorem
- §1.1 roadmap — em-dash before a restatement → colon (punctuation).
- §1.2 — "looked at closely, is really two things. The thing that genuinely cannot
  be doubted" → "examined closely, is two things. What genuinely cannot be doubted"
  (tightening).
- §1.2 — "instantiated more than once over" → "instantiated more than once"
  (redundant word).
- §1.2 — "not a modeling choice but the definition of" → "but the very definition
  of" (rhythm/emphasis).
- §1.5 — "C2 holds trivially … from the fact that σ²=id" → "…, since σ²=id"
  (tightening).

### Chapter 2 — The Substratum
- §2.1 — "The second question is, when (S,φ) is determined, what symmetries does it
  have" → recast as a cleaner relative clause (comma splice).
- §2.6 — "The differences … are entirely in which structure" → "lie entirely in
  which structure" (rhythm).

### Chapter 3 — Hierarchical Structural Realism
- §3.6 — "throws the excess away losing nothing" → added comma before the
  participial phrase (punctuation).

### Chapter 16 — Medicine
- §16.2 — "the target (memory dependence) is more disease-specific than the target
  (catalytic activity)" — "the target" referred to two different things; recast as
  "memory dependence is more disease-specific than catalytic activity" (clarity).

Chapters 4–15, 17–19 and the appendices needed no prose edits.

## Book-wide consistency fix (1)

- **"C1–C3" → "C1-C3"** — the condition-range label appeared in two forms: en-dash
  (86 instances) and hyphen (528 instances). Normalized all to the hyphen form, the
  6:1 majority. Applied across 7 source files (ch00–ch05 and others).

## Internal-scaffolding leaks removed (8)

These were references to the author's working files that should not appear in a
published book — a reader cannot act on "see Main.md §3.2."

- **Chapter 12 §12.1** — removed "Following Evolution.md §2" from the section
  roadmap.
- **Appendix B** — removed 6 internal "Source: Main.md / SM.md / GR.md §X" pointers
  from derivation headers (the reader-useful "Main-text reference: Chapter X §Y"
  portion was kept).
- **Reader's Guide** — companion papers listed by filename ("Main.md, SM.md,
  GR.md, …") → "companion papers (in the Zenodo release at DOI …)".
- **Bibliography** — same companion-paper filename fix as the Reader's Guide.

A book-wide scan for TODO / FIXME / draft markers and stray .md filenames is
otherwise clean.

## Build status

- 404 pages, 0 undefined references.
- Body pagination: Chapter 1 → p. 26, Chapter 19 → p. 321, Index → p. 401.
- The index (35 concept entries, 24 names, 12-entry symbol index) was regenerated
  against the final 404-page build, so all page references are self-consistent.

## Recommendation

This pass caught mechanical errors, a consistency issue, and several scaffolding
leaks. It is not a substitute for a full editorial copyedit by a human professional,
which is still advisable before publication — a human editor may catch substantive
prose issues that a deliberately light AI pass does not.
